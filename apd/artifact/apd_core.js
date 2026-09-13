/* apd_core.js — port determinista de apd/apd_run.py y de las herramientas del paquete
 * v3.4 (brief_freeze / preflight / case_validate / model_router_v33 / rule_matcher_v3 /
 * prompt_ast_gate / prompt_render / prompt_patch / prompt_revision_gate / template_engine /
 * audit_gi2 / runtime_ledger_v3) para correr dentro de una página de Claude.
 *
 * Sin criterio: cada función reproduce la del paquete. Los datos (reglas, schemas,
 * vocabularios, topes) vienen de data.js, generado por build_data.py.
 *
 * API:  const run = await APD.run(D, {facts, case}, {auditor})   // auditor(request) → entries
 *       const run2 = await APD.revise(D, run, delta, provenance, {auditor})
 */
(function (root) {
  "use strict";

  // ------------------------------------------------------------- utilidades
  const MODELS = {
    "gpt-image-2": { family: "gpt_image", capabilities_id: "gpt-image", template: "gpt" },
    "nano-banana-pro": { family: "nano_banana", capabilities_id: "nano-banana", template: "nb" },
    "nano-banana-2": { family: "nano_banana", capabilities_id: "nano-banana", template: "nb" },
  };
  const OPERATIONS = { create: "text_to_image", edit: "image_edit" };
  const TEMPLATE_RULES = ["6d9997eabed1"], VERB_RULES = ["a24fed9220cf"], REF_RULES = ["6d9997eabed1"];
  const NB_RULES = ["f120241be185"], NB_LENS_RULE = "c58caa804ddc", EDIT_RULES = ["6d9997eabed1"];
  const T1_RULES = ["6ea31ee7e2b2", "3821c52f13ac"], T1_BLOCKS = ["light_hard", "skin_doc", "usecase_doc", "clean_doc"];
  const MECHANICAL = {
    "v34:brief-freeze": "brief_freeze", "v34:brief-preflight": "brief_preflight",
    "v34:authorized-delta": "authorized_delta", "v34:prompt-revision-gate": "prompt_revision_gate",
    "v32:generation-params": "generation_params", "v32:aspect-ratio-output": "aspect_ratio",
  };
  const TANDA = 40;
  const UNKNOWN_VALUES = new Set(["UNKNOWN", "UNSPECIFIED", "OPEN", "TBD"]);

  const isObj = (v) => v !== null && typeof v === "object" && !Array.isArray(v);
  const deepcopy = (v) => JSON.parse(JSON.stringify(v));
  const now = () => new Date().toISOString().replace(/\.\d{3}Z$/, "Z");

  // json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",",":"))
  function canonical(v) {
    if (Array.isArray(v)) return "[" + v.map(canonical).join(",") + "]";
    if (isObj(v)) return "{" + Object.keys(v).sort().map((k) => JSON.stringify(k) + ":" + canonical(v[k])).join(",") + "}";
    return JSON.stringify(v);
  }
  async function sha256(text) {
    const bytes = new TextEncoder().encode(text);
    const subtle = (root.crypto && root.crypto.subtle) || (typeof require === "function" ? require("crypto").webcrypto.subtle : null);
    const buf = await subtle.digest("SHA-256", bytes);
    return Array.from(new Uint8Array(buf)).map((b) => b.toString(16).padStart(2, "0")).join("");
  }
  function* leaves(v, prefix = "") {
    if (isObj(v)) { for (const k of Object.keys(v).sort()) yield* leaves(v[k], prefix ? `${prefix}.${k}` : k); }
    else yield [prefix, v];
  }
  function getp(d, path) {
    let cur = d;
    for (const p of path.split(".")) { if (isObj(cur) && p in cur) cur = cur[p]; else return [false, undefined]; }
    return [true, cur];
  }
  function gcd(a, b) { while (b) [a, b] = [b, a % b]; return a; }
  function ratioOf(size) {
    const sep = size.toLowerCase().includes("x") ? "x" : ":";
    const [w, h] = size.toLowerCase().split(sep).map(Number);
    const g = gcd(w, h);
    return `${w / g}:${h / g}`;
  }
  const wordCount = (t) => (t.match(/\b\w+[\w'-]*\b/g) || []).length;
  const variantOf = (facts) => (facts.operation || "create") === "edit" ? "gpt-edit" : MODELS[facts.model].template;

  // ------------------------------------------------ validador JSON Schema mínimo
  // Cubre lo que usan case-fingerprint, facts y authorized-delta: type, enum, const,
  // required, properties, additionalProperties, items, minItems, minimum, pattern,
  // minLength, uniqueItems, allOf/if/then, $ref a #/$defs.
  function validateSchema(obj, schema, rootSchema, path = "$") {
    const errs = [];
    rootSchema = rootSchema || schema;
    const rec = (o, s, p) => errs.push(...validateSchema(o, s, rootSchema, p));
    if (s_ref(schema)) { const target = s_ref(schema).split("/").slice(1).reduce((a, k) => a[k], rootSchema); rec(obj, target, path); return errs; }
    const typeOk = (t, o) => t === "object" ? isObj(o) : t === "array" ? Array.isArray(o) : t === "string" ? typeof o === "string" :
      t === "integer" ? Number.isInteger(o) : t === "number" ? typeof o === "number" : t === "boolean" ? typeof o === "boolean" : t === "null" ? o === null : true;
    if (schema.type !== undefined) {
      const types = Array.isArray(schema.type) ? schema.type : [schema.type];
      if (!types.some((t) => typeOk(t, obj))) { errs.push(`${path}: se esperaba ${types.join("|")}`); return errs; }
    }
    if (schema.enum && !schema.enum.some((e) => JSON.stringify(e) === JSON.stringify(obj))) errs.push(`${path}: valor fuera de enum ${JSON.stringify(schema.enum).slice(0, 80)}`);
    if (schema.const !== undefined && JSON.stringify(schema.const) !== JSON.stringify(obj)) errs.push(`${path}: debe ser ${JSON.stringify(schema.const)}`);
    if (typeof obj === "string") {
      if (schema.pattern && !new RegExp(schema.pattern).test(obj)) errs.push(`${path}: no cumple el patrón ${schema.pattern}`);
      if (schema.minLength !== undefined && obj.length < schema.minLength) errs.push(`${path}: vacío`);
    }
    if (typeof obj === "number" && schema.minimum !== undefined && obj < schema.minimum) errs.push(`${path}: mínimo ${schema.minimum}`);
    if (Array.isArray(obj)) {
      if (schema.minItems !== undefined && obj.length < schema.minItems) errs.push(`${path}: mínimo ${schema.minItems} elementos`);
      if (schema.uniqueItems && new Set(obj.map((x) => JSON.stringify(x))).size !== obj.length) errs.push(`${path}: elementos repetidos`);
      if (schema.items) obj.forEach((x, i) => rec(x, schema.items, `${path}[${i}]`));
    }
    if (isObj(obj)) {
      for (const r of schema.required || []) if (!(r in obj)) errs.push(`${path}: falta '${r}'`);
      const props = schema.properties || {};
      for (const [k, v] of Object.entries(obj)) {
        if (k in props) rec(v, props[k], `${path}.${k}`);
        else if (schema.additionalProperties === false) errs.push(`${path}: propiedad no permitida '${k}'`);
        else if (isObj(schema.additionalProperties)) rec(v, schema.additionalProperties, `${path}.${k}`);
      }
    }
    for (const sub of schema.allOf || []) rec(obj, sub, path);
    if (schema.anyOf && !schema.anyOf.some((sub) => validateSchema(obj, sub, rootSchema, path).length === 0)) errs.push(`${path}: no cumple ninguna de las formas permitidas`);
    if (schema.if) {
      const ok = validateSchema(obj, schema.if, rootSchema, path).length === 0;
      if (ok && schema.then) rec(obj, schema.then, path);
      if (!ok && schema.else) rec(obj, schema.else, path);
    }
    return errs;
  }
  const s_ref = (s) => (typeof s.$ref === "string" && s.$ref.startsWith("#/")) ? s.$ref : null;

  // ---------------------------------------------------- procedencia de hechos
  function resolveSkillRef(D, ref) {
    const m = /^([\w-]+)\/([\w./-]+\.(?:md|json|yaml|yml)):(\d+)(?:-(\d+))?$/.exec(ref);
    if (!m) return [false, "formato esperado <skill>/<ruta>:<línea>"];
    const key = `${m[1]}/${m[2]}`;
    const n = D.skill_manifest[key];
    if (n === undefined) return [false, `archivo no instalado: ${key}`];
    const line = +m[3], end = +(m[4] || m[3]);
    if (line < 1 || end > n || end < line) return [false, `${key} tiene ${n} líneas; ${line}-${end} fuera de rango`];
    return [true, key];
  }
  const entriesOf = (prov, path) => { const e = prov[path]; return Array.isArray(e) ? e : e ? [e] : []; };
  function checkProvenance(D, facts) {
    const prov = facts.provenance || {}, errs = [];
    const body = {}; for (const [k, v] of Object.entries(facts)) if (k !== "provenance" && k !== "brief_id") body[k] = v;
    const paths = new Set();
    for (const [path] of leaves(body)) {
      if (path === "references" || path.startsWith("references.")) continue;
      paths.add(path);
      const ents = entriesOf(prov, path);
      if (!ents.length) { errs.push(`${path}: sin procedencia`); continue; }
      for (const e of ents) {
        const ref = String(e.ref || "").trim();
        if (e.source === "skill") { const [ok, why] = resolveSkillRef(D, ref); if (!ok) errs.push(`${path}: skill ref inválida (${ref}): ${why}`); }
        else if (e.source === "research") { if (!/^https?:\/\//.test(ref)) errs.push(`${path}: research ref debe ser URL (${ref})`); }
        else if (e.source === "user") { if (ref.length < 3) errs.push(`${path}: user ref debe citar la instrucción`); }
        else if (e.source === "asset") { if (ref.length < 3) errs.push(`${path}: asset ref debe nombrar el archivo adjunto`); }
      }
    }
    (facts.references || []).forEach((r, i) => { if (!prov[`references.${i}.role`] && !prov.references) errs.push(`references.${i}.role: sin procedencia`); });
    const stale = Object.keys(prov).filter((p) => !paths.has(p) && !p.startsWith("references"));
    if (stale.length) errs.push("procedencia de rutas inexistentes: " + stale.join(", "));
    return errs;
  }

  const normText = (t) => String(t).toLowerCase().replace(/[’‘]/g, "'").replace(/[“”]/g, '"').replace(/[—–]/g, "-").replace(/\s+/g, " ").trim();
  function citedText(D, ref) {
    const m = /^([\w-]+)\/([\w./-]+):(\d+)(?:-(\d+))?$/.exec(ref); if (!m) return "";
    const text = D.skill_sources[`${m[1]}/${m[2]}`]; if (!text) return "";
    const lines = text.split("\n"), a = +m[3], b = +(m[4] || m[3]);
    return lines.slice(a - 1, b).join("\n");
  }
  const fragmentsOf = (v) => String(v).split(/[,;.]\s+|\s+-\s+|\s+\u2014\s+/).map((f) => f.replace(/^[ .,;]+|[ .,;]+$/g, "")).filter(Boolean);
  // Regla mecánica: lo atribuido al skill es literal de las líneas citadas; toda cita atribuida
  // a Eric existe literalmente en el brief.
  // Hojas descritas desde una imagen que Eric adjuntó (source=asset): la fuente es la
  // imagen, no una cita literal, así que quedan fuera de los gates de literalidad.
  function assetLeaves(facts) {
    const out = new Set();
    for (const [path, v] of Object.entries(facts.provenance || {})) {
      const ents = Array.isArray(v) ? v : [v];
      if (ents.some((e) => e && e.source === "asset")) out.add(path);
    }
    return out;
  }

  function checkLiteralProvenance(D, facts, brief) {
    const errs = [], nb = normText(brief || "");
    if (!nb) return ["brief vacío: cada procedencia 'user' debe citar una instrucción que esté en el brief"];
    const prov = facts.provenance || {};
    const body = {}; for (const [k, v] of Object.entries(facts)) if (k !== "provenance" && k !== "brief_id") body[k] = v;
    const assets = assetLeaves(facts);
    for (const [path, val] of leaves(body)) {
      if (path === "references" || path.startsWith("references.") || assets.has(path)) continue;
      const ents = entriesOf(prov, path), users = ents.filter((e) => e.source === "user"), skills = ents.filter((e) => e.source === "skill");
      for (const e of users) if (!nb.includes(normText(e.ref || ""))) errs.push(`${path}: la cita atribuida a Eric no está en el brief: "${String(e.ref || "").slice(0, 60)}"`);
      if (!path.startsWith("slots.") && path !== "format") continue;
      if (users.length) continue;
      const cited = normText(skills.map((e) => citedText(D, e.ref || "")).join("\n"));
      for (const frag of fragmentsOf(val)) if (!cited.includes(normText(frag))) errs.push(`${path}: fragmento atribuido al skill que no es literal de las líneas citadas: "${frag.slice(0, 60)}"`);
    }
    return errs;
  }

  function checkStrict(D, facts, brief) {
    const errs = [], nb = normText(brief || ""), prov = facts.provenance || {};
    const slotLeaves = [...leaves({ slots: facts.slots || {} })];
    const slotText = slotLeaves.map(([, v]) => normText(String(v))).join(" || ");
    const assets = assetLeaves(facts);
    for (const [path, val] of slotLeaves) {
      if (assets.has(path)) continue;
      const cited = normText(entriesOf(prov, path).filter((e) => e.source === "skill").map((e) => citedText(D, e.ref || "")).join("\n"));
      for (const frag of fragmentsOf(val)) { const nf = normText(frag); if (!nb.includes(nf) && !cited.includes(nf)) errs.push(`${path}: fragmento que no es literal del brief ni del skill: "${frag.slice(0, 60)}"`); }
    }
    for (const sent of String(brief || "").split(/(?<=[.;!?])\s+|\n+/)) {
      const ns = normText(sent).replace(/^[ .;]+|[ .;]+$/g, ""); if (ns.length < 12) continue;
      if (!fragmentsOf(ns).some((f) => slotText.includes(normText(f)))) errs.push(`frase del brief omitida en los slots: "${ns.slice(0, 60)}"`);
    }
    return errs;
  }

  // ------------------------------------------------------- case_validate.py
  function caseValidate(D, c) {
    const errors = validateSchema(c, D.case_schema).map((e) => "schema " + e), warnings = [];
    if (errors.length) return { status: "FAIL", errors, warnings };
    const bt = c.base_type, subj = c.subject, op = c.operation, stage = c.stage, comp = c.composition, phys = c.physics, refs = c.references, brand = c.brand;
    if (bt === "T3" && !(subj.count === 1 && subj.human === true)) errors.push("T3 requires subject.count=1 and subject.human=true");
    if (bt === "T4" && !(Number.isInteger(subj.count) && subj.count >= 2 && subj.human === true)) errors.push("T4 requires at least two human subjects");
    if (bt === "T5" && !["image_edit", "image_to_image"].includes(op)) errors.push("T5 requires an image editing operation");
    if (subj.human_contact === true && !(Number.isInteger(subj.count) && subj.count >= 2)) errors.push("human_contact=true requires at least two subjects");
    if (subj.identity_fidelity === "exact" && refs.identity_reference !== true) errors.push("exact identity fidelity requires references.identity_reference=true");
    if (["locked", "strict"].includes(brand.mode) && !brand.brand_lock_ref) errors.push("locked/strict brand mode requires brand_lock_ref");
    if (comp.split_level === true) {
      if (phys.water !== true) errors.push("split_level=true requires physics.water=true");
      if (comp.waterline_visible !== true) errors.push("split_level=true requires waterline_visible=true");
    }
    if (comp.waterline_visible === true && phys.water !== true) errors.push("waterline_visible=true requires physics.water=true");
    if (c.motion.static_frame === true && ["text_to_video", "image_to_video", "video_edit"].includes(op)) errors.push("video generation/edit cannot have motion.static_frame=true");
    if (["prompt", "generation"].includes(stage) && c.generator.family === "UNKNOWN") errors.push("prompt/generation stage requires a known generator family");
    const task = c.task, audio = c.audio, seq = c.sequence;
    if (audio.dialogue_required === true && c.media !== "video") errors.push("dialogue_required=true requires media=video");
    if (audio.lipsync === true && audio.dialogue_required !== true) errors.push("lipsync=true requires dialogue_required=true");
    if (Number.isInteger(audio.speaker_count) && audio.speaker_count > 0 && audio.dialogue_required !== true) errors.push("speaker_count>0 requires dialogue_required=true");
    if (seq.multi_shot === true && Number.isInteger(seq.shot_count) && seq.shot_count < 2) errors.push("multi_shot=true requires shot_count>=2");
    if (seq.multi_shot === false && Number.isInteger(seq.shot_count) && seq.shot_count !== 1) errors.push("multi_shot=false requires shot_count=1");
    if (task.family === "race_speed" && c.media !== "video") warnings.push("task.family=race_speed is normally video; confirm this is intentional");
    const pc = c.prompt_case;
    if (["prompt", "generation"].includes(stage) && ["image", "video"].includes(c.media) && pc === "NONE") errors.push("visual prompt/generation requires prompt_case classification");
    if (pc === "1" && !(c.media === "image" && op === "text_to_image" && refs.mode === "none")) errors.push("prompt_case=1 requires image text_to_image with references.mode=none");
    if (pc === "2" && !(c.media === "image" && ["partial", "full"].includes(refs.mode))) errors.push("prompt_case=2 requires image with references");
    if (pc === "3a" && !(c.media === "video" && op === "image_to_video" && seq.start_frame_ref === true && seq.end_frame_ref === false)) errors.push("prompt_case=3a requires I2V with start frame only");
    if (pc === "3b" && !(c.media === "video" && op === "image_to_video" && seq.start_frame_ref === true && seq.end_frame_ref === true)) errors.push("prompt_case=3b requires I2V with start and end frames");
    if (pc === "3c" && !(c.media === "video" && seq.motion_reference === true)) errors.push("prompt_case=3c requires video with motion_reference=true");
    if (pc === "4" && !(c.media === "video" && audio.dialogue_required === true)) errors.push("prompt_case=4 requires video dialogue");
    const declared = new Set((c.unknowns || []).map((x) => x.path));
    const blocking = (c.unknowns || []).filter((x) => x.blocking);
    if (blocking.length) errors.push("blocking unknowns remain: " + blocking.map((x) => x.path).join(", "));
    if (["prompt", "generation"].includes(stage) && c.media === "image") {
      if (!c.deliverable.aspect_ratio) errors.push("image prompt/generation requires deliverable.aspect_ratio");
      if (c.deliverable.purpose === "UNKNOWN") warnings.push("deliverable.purpose is UNKNOWN; prompt may be technically valid but under-directed");
    }
    const silent = [];
    (function walk(o, prefix) {
      if (isObj(o)) for (const [k, v] of Object.entries(o)) walk(v, prefix ? `${prefix}.${k}` : k);
      else if (Array.isArray(o)) return;
      else if (o === "UNKNOWN" && !declared.has(prefix)) silent.push(prefix);
    })(c, "");
    if (silent.length) warnings.push("UNKNOWN values not documented in unknowns[]: " + silent.join(", "));
    return { status: errors.length ? "FAIL" : "PASS", errors, warnings };
  }

  // --------------------------------------------------------- rule_engine_v3
  const T = "TRUE", F = "FALSE", U = "UNKNOWN";
  const isUnknown = (v) => v === null || v === undefined || (typeof v === "string" && UNKNOWN_VALUES.has(v.trim().toUpperCase()));
  const triNot = (v) => ({ TRUE: F, FALSE: T, UNKNOWN: U })[v];
  const triAll = (vs) => vs.some((v) => v === F) ? F : vs.some((v) => v === U) ? U : T;
  const triAny = (vs) => vs.some((v) => v === T) ? T : vs.some((v) => v === U) ? U : F;
  const eq = (a, b) => JSON.stringify(a) === JSON.stringify(b);
  function evalLeaf(c, leaf) {
    const op = leaf.op || "eq", expected = leaf.value;
    const [exists, actual] = getp(c, leaf.path);
    if (op === "exists") return exists ? T : F;
    if (!exists || isUnknown(actual)) return U;
    switch (op) {
      case "eq": return eq(actual, expected) ? T : F;
      case "neq": return eq(actual, expected) ? F : T;
      case "in": return expected.some((e) => eq(e, actual)) ? T : F;
      case "not_in": return expected.some((e) => eq(e, actual)) ? F : T;
      case "contains": return (Array.isArray(actual) ? actual.some((x) => eq(x, expected)) : typeof actual === "string" ? actual.includes(expected) : false) ? T : F;
      case "intersects": return Array.isArray(actual) && actual.some((x) => expected.some((e) => eq(e, x))) ? T : F;
      case "truthy": return actual ? T : F;
      case "falsy": return !actual ? T : F;
      case "regex": return new RegExp(String(expected), "i").test(String(actual)) ? T : F;
      case "gt": case "gte": case "lt": case "lte": {
        if (typeof actual !== "number") return F;
        return ({ gt: actual > expected, gte: actual >= expected, lt: actual < expected, lte: actual <= expected })[op] ? T : F;
      }
      default: throw new Error("unsupported condition op: " + op);
    }
  }
  function evalCondition(c, cond) {
    if (!cond || Object.keys(cond).length === 0) return T;
    if ("all" in cond) return triAll(cond.all.map((x) => evalCondition(c, x)));
    if ("any" in cond) return triAny(cond.any.map((x) => evalCondition(c, x)));
    if ("not" in cond) return triNot(evalCondition(c, cond.not));
    if ("path" in cond) return evalLeaf(c, cond);
    throw new Error("invalid condition node");
  }
  function conditionPaths(cond) {
    if (!cond || Object.keys(cond).length === 0) return new Set();
    if ("path" in cond) return new Set([cond.path]);
    const out = new Set();
    for (const k of ["all", "any"]) for (const x of cond[k] || []) for (const p of conditionPaths(x)) out.add(p);
    if ("not" in cond) for (const p of conditionPaths(cond.not)) out.add(p);
    return out;
  }
  function matchRule(c, rule, meta) {
    const st = evalCondition(c, meta.when);
    if (st === T) return { rule_id: rule.id, status: "APPLIES", reason: "condition matched", rule, metadata: meta };
    if (st === F) return { rule_id: rule.id, status: "NA", reason: "condition evaluated false", rule, metadata: meta };
    const paths = [...conditionPaths(meta.when)].sort();
    const unknown = paths.filter((p) => { const [ex, v] = getp(c, p); return !ex || isUnknown(v); });
    return { rule_id: rule.id, status: "UNRESOLVED", reason: "unknown case fields: " + (unknown.length ? unknown : paths).join(", "), rule, metadata: meta };
  }
  const incompatible = (effects) => (effects.has("REQUIRE") && effects.has("FORBID")) || (effects.has("FORBID") && effects.has("RECOMMEND"));

  // -------------------------------------------------------- rule_matcher_v3
  async function ruleMatch(D, c) {
    const rs = D.ruleset;
    if (!rs.published) return { status: "FAIL", reason: "ruleset is not published" };
    const records = [], applies = [], unresolved = [];
    for (const item of rs.rules) {
      const { rule, metadata: meta } = item;
      if (meta.classification_status === "NON_NORMATIVE") { records.push({ rule_id: rule.id, status: "NA", reason: "classified NON_NORMATIVE", rule, metadata: meta }); continue; }
      const rec = matchRule(c, rule, meta);
      records.push(rec);
      if (rec.status === "APPLIES") applies.push(rec); else if (rec.status === "UNRESOLVED") unresolved.push(rec);
    }
    const activeIds = new Set(applies.map((r) => r.rule_id)), suppressed = {};
    for (const r of applies) for (const loser of r.metadata.supersedes || []) if (activeIds.has(loser)) suppressed[loser] = r.rule_id;
    const conflicts = [], groups = {};
    for (const r of applies) { if (r.rule_id in suppressed) continue; const key = r.metadata.conflict_key; if (key) (groups[key] = groups[key] || []).push(r); }
    for (const [key, group] of Object.entries(groups)) {
      const effects = new Set(group.map((r) => r.metadata.effect));
      if (!incompatible(effects)) continue;
      const matches = [], unknown = [];
      for (const p of rs.conflict_policies || []) {
        if (p.conflict_key !== key) continue;
        const st = evalCondition(c, p.when || {});
        if (st === T) matches.push(p); else if (st === U) unknown.push(p);
      }
      if (matches.length !== 1) { conflicts.push({ conflict_key: key, rule_ids: group.map((r) => r.rule_id), effects: [...effects].sort(), status: "UNRESOLVED", reason: "expected exactly one matching conflict policy", matching_policies: matches.map((p) => p.id), unknown_policies: unknown.map((p) => p.id) }); continue; }
      const p = matches[0], winner = p.winner_rule_id;
      if (!group.some((r) => r.rule_id === winner)) { conflicts.push({ conflict_key: key, status: "UNRESOLVED", reason: `policy ${p.id} winner does not apply`, rule_ids: group.map((r) => r.rule_id) }); continue; }
      for (const r of group) if (r.rule_id !== winner) suppressed[r.rule_id] = winner;
      conflicts.push({ conflict_key: key, status: "RESOLVED", policy: p.id, winner_rule_id: winner, rule_ids: group.map((r) => r.rule_id) });
    }
    for (const rec of records) if (rec.rule_id in suppressed && rec.status === "APPLIES") { rec.status = "SUPPRESSED"; rec.reason = "suppressed by " + suppressed[rec.rule_id]; }
    const active = records.filter((r) => r.status === "APPLIES");
    const unresolvedConflicts = conflicts.filter((x) => x.status === "UNRESOLVED");
    const status = unresolved.length || unresolvedConflicts.length ? "FAIL" : "PASS";
    return {
      status, case_id: c.case_id, case_sha256: await sha256(canonical(c)), ruleset_version: rs.ruleset_version, ruleset_sha256: rs.ruleset_sha256,
      counts: { rules_evaluated: records.length, active: active.length, na: records.filter((r) => r.status === "NA").length, suppressed: records.filter((r) => r.status === "SUPPRESSED").length, unresolved: unresolved.length, unresolved_conflicts: unresolvedConflicts.length },
      conflicts, unresolved: unresolved.slice(0, 8), active_rules: active,
    };
  }

  // ------------------------------------------------------- model_router_v33
  function parseRatio(s) { if (!s || !String(s).includes(":")) return null; const [a, b] = String(s).split(":").map(Number); return a > 0 && b > 0 ? a / b : null; }
  function derivedFeatures(c) {
    const tags = new Set((c.task || {}).tags || []), phys = c.physics || {};
    const pcount = ["water", "splash", "bubbles", "turbulence", "refraction", "reflection", "gravity", "collision", "deformation"].filter((k) => phys[k] === true).length;
    const ratio = parseRatio((c.deliverable || {}).aspect_ratio), fam = (c.task || {}).family, text = c.text || {}, refs = c.references || {};
    const purpose = (c.deliverable || {}).purpose, brand = (c.brand || {}).mode, op = c.operation, sid = (c.subject || {}).identity_fidelity, product = (c.subject || {}).product_fidelity;
    const roles = refs.roles || [], photo = ["photographic", "strict_photographic"].includes((c.realism || {}).mode);
    const has = (...xs) => xs.some((x) => tags.has(x));
    return {
      requires_real_world_grounding: has("REAL_WORLD_GROUNDING", "GROUNDING_REQUIRED"),
      complex_scene_physics_composition: (c.composition || {}).load_bearing === true && (pcount >= 2 || has("COMPLEX_PHYSICS", "PHYSICS_HEAVY")),
      extreme_aspect_ratio: ratio !== null && (ratio > 3.0 || ratio < 1 / 3),
      bulk_low_cost: has("BULK_LOW_COST", "MASS_GENERATION"),
      photographic_fine_typography_ui: photo && (fam === "ui_social" || (text.readable_text_required === true && has("FINE_TYPOGRAPHY", "UI"))),
      exact_edit_preservation: op === "image_edit" && (["consistent", "exact"].includes(sid) || ["recognizable", "exact"].includes(product)),
      dense_small_text: text.readable_text_required === true && (fam === "text_rendering" || has("DENSE_SMALL_TEXT")),
      brand_print_exact_text: purpose === "poster" && ["guided", "locked", "strict"].includes(brand) && text.readable_text_required === true,
      storyboard_sequence: ["storyboard", "multi_panel"].includes(fam) && text.readable_text_required !== true,
      storyboard_typography: ["storyboard", "multi_panel"].includes(fam) && text.readable_text_required === true,
      style_transfer_without_refs: has("STYLE_TRANSFER") && refs.mode === "none",
      many_references_14_plus: roles.length >= 14 || has("MANY_REFERENCES_14_PLUS"),
      photographic_portrait: fam === "portrait" && photo,
      neutral_product_shot: purpose === "product" && ["neutral_studio", "studio", "neutral_background"].includes((c.environment || {}).type),
      minimalist_poster: purpose === "poster" && has("MINIMALIST"),
      editorial_photography: purpose === "editorial" && photo,
      physics_signal_count: pcount,
    };
  }
  function modelRoute(D, c) {
    const current = c.generator || {};
    const explicit = ![null, undefined, "UNKNOWN", "other"].includes(current.family) && ![null, undefined, "UNKNOWN", ""].includes(current.model);
    const features = derivedFeatures(c), candidates = [], neutrals = [];
    const canon = D.routing.canonical;
    for (const r of canon.routes || []) if (features[r.feature] === true) candidates.push({ source: "KB_CANONICAL", id: r.id, priority: r.priority, kind: r.kind, candidates: r.candidates, feature: r.feature });
    for (const r of canon.neutral_routes || []) if (features[r.feature] === true) neutrals.push({ source: "KB_CANONICAL", id: r.id, priority: r.priority, kind: "NEUTRAL", candidates: r.candidates, feature: r.feature });
    for (const r of (D.routing.learned || {}).routes || []) if (evalCondition(c, r.when || {}) === T) candidates.push({ source: "LEARNED_PRODUCTION", id: r.id, priority: r.priority || 0, kind: "DECISIVE", candidates: [r.preferred] });
    candidates.sort((a, b) => b.priority - a.priority);
    if (explicit) return { status: "USER_MODEL_LOCK_PRESERVED", selected: current, features, matching_routes: candidates, neutral_routes: neutrals };
    if (candidates.length) {
      const top = candidates[0];
      if (top.kind === "CHOICE" && top.candidates.length > 1) return { status: "MODEL_CHOICE_REQUIRED", selected: null, choices: top.candidates, route: top, features };
      return { status: "ROUTED", selected: top.candidates[0], route: top, features };
    }
    if (neutrals.length) return { status: "MODEL_TIE", selected: null, choices: neutrals[0].candidates, route: neutrals[0], features };
    return { status: "NO_CANONICAL_ROUTE", selected: null, features };
  }

  // ------------------------------------------------------- brief_freeze_v34
  const under = (path, prefixes) => prefixes.some((x) => path === x || path.startsWith(x + "."));
  async function canonHash(briefId, version, facts, states) {
    return sha256(canonical({ brief_id: briefId, brief_version: version, facts, field_states: states }));
  }
  async function briefFreeze(facts, briefId, sourceId, optional, required = []) {
    const states = {};
    for (const [p, val] of leaves(facts)) {
      const isOpt = under(p, optional), isReq = under(p, required);
      states[p] = { state: val === null ? "OPEN" : "LOCKED", source_type: "user", source_id: sourceId, prompt_required: !!(isReq || (val !== null && !isOpt)) };
    }
    const h = await canonHash(briefId, 1, facts, states);
    return { schema_version: "1.1", brief_id: briefId, brief_version: 1, status: "FROZEN", facts, field_states: states, brief_hash: h };
  }
  const preflight = (b) => Object.entries(b.field_states).filter(([, s]) => s.prompt_required && s.state !== "LOCKED").map(([p]) => p);

  async function briefApplyDelta(b, d) {
    const errors = [];
    if (d.base_brief_hash !== b.brief_hash) errors.push("delta base_brief_hash does not match frozen brief");
    const facts = deepcopy(b.facts), states = deepcopy(b.field_states), seen = new Set();
    for (const c of d.changes || []) {
      const p = c.path, op = c.op;
      if (seen.has(p)) { errors.push(`duplicate delta path: ${p}`); continue; }
      seen.add(p);
      const old = states[p] || { prompt_required: true };
      const parts = p.split("."); let cur = facts, bad = false;
      for (const k of parts.slice(0, -1)) { if (!(k in cur) || !isObj(cur[k])) { if (op === "add") cur[k] = {}; else { bad = true; break; } } cur = cur[k]; }
      const last = parts[parts.length - 1];
      if (!bad && op === "replace" && !(last in cur)) bad = true;
      if (!bad && op === "remove" && !(last in cur)) bad = true;
      if (bad) { errors.push(`unknown path for ${op}: ${p}`); continue; }
      if (op === "remove") cur[last] = null; else cur[last] = c.value;
      states[p] = { state: op === "remove" ? "OPEN" : "LOCKED", source_type: "user", source_id: d.authorized_by, prompt_required: !!(old.prompt_required ?? true) };
    }
    if (errors.length) return { errors };
    const version = b.brief_version + 1, h = await canonHash(b.brief_id, version, facts, states);
    const history = [...(b.delta_history || []), { delta_hash: await sha256(canonical(d)), authorized_by: d.authorized_by, reason: d.reason || "", paths: [...seen].sort() }];
    return { brief: { schema_version: "1.1", brief_id: b.brief_id, brief_version: version, status: "FROZEN", facts, field_states: states, brief_hash: h, delta_history: history } };
  }

  // ------------------------------------------------------------ AST fijo
  function buildAst(D, facts, brief, baseType) {
    const s = facts.slots, v = variantOf(facts), canon = D.blocks;
    const seg = (id, template, bindings, rules) => ({ id, kind: "brief_template", template, bindings, source_rules: rules });
    const fixed = (id, text, rules) => ({ id, kind: "rule_text", text, source_rules: rules });
    const blocks = [];
    if (v === "gpt") {
      blocks.push({ id: "opening", segments: [seg("verb", "Create {opening}.", { opening: "slots.opening" }, VERB_RULES)] });
      if ("references_line" in s) blocks.push({ id: "references", segments: [seg("roles", "{references_line}", { references_line: "slots.references_line" }, REF_RULES)] });
      blocks.push({ id: "scene", segments: [seg("scene", "Scene: {location}, {time}, {weather}.", { location: "slots.scene.location", time: "slots.scene.time", weather: "slots.scene.weather" }, TEMPLATE_RULES)] });
      const subject = [seg("subject", "Subject: {who}, {action}, {framing}.", { who: "slots.subject.who", action: "slots.subject.action", framing: "slots.subject.framing" }, TEMPLATE_RULES)];
      if ("contact" in s.subject) subject.push(seg("contact", "{contact}.", { contact: "slots.subject.contact" }, TEMPLATE_RULES));
      blocks.push({ id: "subject", segments: subject });
      const details = [seg("details", "Important Details: {lens_feel}, {light_source}, {surface_wear}, {imperfections}, {real_texture}.",
        { lens_feel: "slots.details.lens_feel", light_source: "slots.details.light_source", surface_wear: "slots.details.surface_wear", imperfections: "slots.details.imperfections", real_texture: "slots.details.real_texture" }, TEMPLATE_RULES)];
      const useCase = [seg("use_case", "Use Case: {use_case}.", { use_case: "slots.use_case" }, TEMPLATE_RULES)];
      const constraints = [seg("constraints", "Constraints: {constraints}.", { constraints: "slots.constraints" }, TEMPLATE_RULES)];
      if (baseType === "T1") {
        details.push(fixed("light_hard", canon.light_hard, T1_RULES), fixed("skin_doc", canon.skin_doc, T1_RULES));
        useCase.push(fixed("usecase_doc", canon.usecase_doc, T1_RULES));
        constraints.push(fixed("clean_doc", canon.clean_doc, T1_RULES));
      }
      blocks.push({ id: "details", segments: details }, { id: "use_case", segments: useCase }, { id: "constraints", segments: constraints });
      if ("negative" in s) blocks.push({ id: "negative", segments: [seg("negative", "Negative: {negative}.", { negative: "slots.negative" }, TEMPLATE_RULES)] });
    } else if (v === "nb") {
      blocks.push({ id: "opening", segments: [seg("verb", "Create {opening}.", { opening: "slots.opening" }, VERB_RULES)] });
      if ("references_line" in s) blocks.push({ id: "references", segments: [seg("roles", "{references_line}", { references_line: "slots.references_line" }, REF_RULES)] });
      const body = [seg("subject", "{subject} {action} {location}.", { subject: "slots.subject", action: "slots.action", location: "slots.location" }, NB_RULES),
        seg("composition", "{composition}.", { composition: "slots.composition" }, NB_RULES),
        seg("style", "{style}.", { style: "slots.style" }, NB_RULES)];
      if ("contact" in s) body.splice(1, 0, seg("contact", "{contact}.", { contact: "slots.contact" }, NB_RULES));
      blocks.push({ id: "body", segments: body });
      if (baseType === "T1") blocks.push({ id: "t1", segments: T1_BLOCKS.map((b) => fixed(b, canon[b], T1_RULES)) });
      blocks.push({ id: "format", segments: [seg("format", "Format: {format}.", { format: "format" }, NB_RULES)] });
      if ("negative" in s) blocks.push({ id: "negative", segments: [seg("negative", "Negative: {negative}.", { negative: "slots.negative" }, NB_RULES)] });
    } else {
      blocks.push({ id: "change", segments: [seg("change", "Change: {change}.", { change: "slots.change" }, EDIT_RULES)] });
      blocks.push({ id: "preserve", segments: [seg("preserve", "Preserve: {preserve}.", { preserve: "slots.preserve" }, EDIT_RULES)] });
      blocks.push({ id: "constraints", segments: [seg("constraints", "Constraints: {constraints}.", { constraints: "slots.constraints" }, EDIT_RULES)] });
      if ("negative" in s) blocks.push({ id: "negative", segments: [seg("negative", "Negative: {negative}.", { negative: "slots.negative" }, EDIT_RULES)] });
    }
    const parameters = { quality: facts.quality, aspectRatio: ratioOf(facts.size) };
    if (facts.size.toLowerCase().includes("x")) parameters.size = facts.size;
    return { schema_version: "2.0", prompt_id: facts.brief_id, prompt_revision: 1, brief_hash: brief.brief_hash, model: facts.model, parameters, blocks };
  }
  const placeholders = (t) => new Set([...t.matchAll(/\{([A-Za-z_][A-Za-z0-9_]*)\}/g)].map((m) => m[1]));
  function astGate(b, ast) {
    const errs = [], used = [], ids = new Set(), states = b.field_states;
    if (ast.schema_version !== "2.0") errs.push("prompt AST schema_version must be 2.0");
    if (ast.brief_hash !== b.brief_hash) errs.push("prompt AST brief_hash mismatch");
    const openReq = Object.entries(states).filter(([, s]) => s.prompt_required && s.state !== "LOCKED").map(([p]) => p);
    if (openReq.length) errs.push("prompt-required fields are OPEN: " + openReq.join(", "));
    for (const block of ast.blocks || []) {
      if (!(block.segments || []).length) errs.push(`block ${block.id} has no segments`);
      for (const seg of block.segments || []) {
        const sid = `${block.id}.${seg.id}`;
        if (ids.has(sid)) errs.push(`duplicate segment id ${sid}`);
        ids.add(sid);
        if (seg.kind === "brief_template") {
          const binds = seg.bindings || {};
          const ph = placeholders(seg.template || ""), keys = new Set(Object.keys(binds));
          if (ph.size !== keys.size || [...ph].some((k) => !keys.has(k))) errs.push(`${sid} template placeholders do not match bindings`);
          if (!keys.size) errs.push(`${sid} has no brief bindings`);
          for (const p of Object.values(binds)) { used.push(p); if (!(p in states)) errs.push(`${sid} references unknown brief path ${p}`); else if (states[p].state !== "LOCKED") errs.push(`${sid} binds OPEN brief field ${p}`); }
        } else if (seg.kind === "rule_text" || seg.kind === "adapter_text") {
          if (!seg.text) errs.push(`${sid} has empty text`);
          if (!(seg.source_rules || []).length) errs.push(`${sid} lacks rule provenance`);
          if (seg.bindings) errs.push(`${sid} rule/adapter segment may not bind brief fields`);
        } else errs.push(`${sid} invalid kind ${seg.kind}`);
      }
    }
    const usedSet = new Set(used);
    const missing = Object.entries(states).filter(([p, s]) => s.prompt_required && s.state === "LOCKED" && !usedSet.has(p)).map(([p]) => p);
    if (missing.length) errs.push("locked prompt-required fields omitted: " + missing.join(", "));
    return { status: errs.length ? "FAIL" : "PASS", segments: ids.size, used_paths: [...usedSet].sort(), errors: errs };
  }
  const fmt = (v) => typeof v === "boolean" ? (v ? "true" : "false") : Array.isArray(v) ? v.map(String).join(", ") : String(v);
  function render(ast, b) {
    if (ast.brief_hash !== b.brief_hash) throw new Error("PROMPT_RENDER: FAIL brief_hash mismatch");
    const blocks = [];
    for (const block of ast.blocks) {
      const texts = [];
      for (const s of block.segments) {
        if (s.kind === "brief_template") {
          let t = s.template;
          for (const [name, path] of Object.entries(s.bindings)) { const [, val] = getp(b.facts, path); t = t.split(`{${name}}`).join(fmt(val)); }
          texts.push(t.trim());
        } else texts.push(s.text.trim());
      }
      blocks.push(texts.filter(Boolean).join(" "));
    }
    return blocks.join("\n\n") + "\n";
  }
  function promptPatch(ast, oldB, newB, d, deltaHash) {
    const errs = [];
    if (ast.brief_hash !== oldB.brief_hash) errs.push("AST does not target old brief");
    if (d.base_brief_hash !== oldB.brief_hash) errs.push("delta does not target old brief");
    const hist = newB.delta_history || [];
    if (!hist.length || hist[hist.length - 1].delta_hash !== deltaHash) errs.push("new brief was not produced by supplied delta");
    if (errs.length) return { errors: errs };
    const out = deepcopy(ast); out.brief_hash = newB.brief_hash; out.prompt_revision = (ast.prompt_revision || 1) + 1;
    return { ast: out };
  }
  function revisionGate(oldAst, newAst, oldB, newB, d) {
    const errs = [], norm = (x) => { const y = deepcopy(x); delete y.brief_hash; delete y.prompt_revision; return canonical(y); };
    if (oldAst.brief_hash !== oldB.brief_hash) errs.push("before AST/brief mismatch");
    if (newAst.brief_hash !== newB.brief_hash) errs.push("after AST/brief mismatch");
    if (d.base_brief_hash !== oldB.brief_hash) errs.push("delta base mismatch");
    if (norm(oldAst) !== norm(newAst)) errs.push("UNAUTHORIZED PROMPT DRIFT: AST content/model/parameters/templates changed");
    if ((newAst.prompt_revision || 1) !== (oldAst.prompt_revision || 1) + 1) errs.push("revision counter did not increment exactly once");
    return { status: errs.length ? "FAIL" : "PASS", authorized_paths: (d.changes || []).map((c) => c.path), errors: errs };
  }

  // ---------------------------------------------------------------- gates
  const NB_LENS_RE = /\b\d{2,3}\s?mm\b|\bf\/\d|\bISO\s?\d/i;
  function isKeywordSoup(line) {
    const parts = line.split(",").map((p) => p.trim()).filter(Boolean);
    if (parts.length < 4 || line.trimEnd().endsWith(".")) return false;
    return parts.every((p) => p.split(/\s+/).length <= 3);
  }
  const escapeRe = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  function lexicalGates(D, prompt, facts) {
    const out = {}, v = variantOf(facts), verbs = D.verbs;
    const first = (prompt.split("\n").map((l) => l.trim()).find(Boolean)) || "";
    if (v === "gpt-edit") out.start_with_verb = { status: first.toLowerCase().startsWith("change:") ? "PASS" : "FAIL", detail: `edición: primera línea "${first.slice(0, 60)}" debe ser "Change:"`, source: "image/references/gpt-image.md:80-83" };
    else out.start_with_verb = { status: verbs.length && verbs.some((x) => first.toLowerCase().startsWith(x)) ? "PASS" : "FAIL", detail: `primera línea: "${first.slice(0, 60)}"; verbos: ${verbs.join(", ")}`, source: D.sources_of_truth.verbs };
    if (v === "nb") { const hits = prompt.match(new RegExp(NB_LENS_RE.source, "gi")) || []; out.nb_no_numeric_lens = { status: hits.length ? "FAIL" : "PASS", detail: hits.length ? hits : "sin 50mm / f/2.8 / ISO", source: "image/references/nano-banana.md:24" }; }
    const soup = prompt.split("\n").filter((l) => isKeywordSoup(l)).map((l) => l.trim());
    out.natural_language = { status: soup.length ? "FAIL" : "PASS", detail: soup.length ? soup.slice(0, 3) : "sin keyword soup", source: D.sources_of_truth.verbs };
    const low = prompt.toLowerCase(), banned = D.banned.filter((t) => new RegExp("(?<![\\w-])" + escapeRe(t) + "(?![\\w-])").test(low));
    out.banned_vocabulary = { status: banned.length || !D.banned.length ? "FAIL" : "PASS", detail: banned.length ? banned : (D.banned.length ? "sin términos prohibidos" : "listas no encontradas"), source: D.sources_of_truth.banned };
    return out;
  }
  function auditContext(c, ceiling) {
    const subj = c.subject, refs = c.references, brand = c.brand;
    return {
      optics_required: false, mood_required: ["T1", "T2", "T3", "T4"].includes(c.base_type), colour_required: false,
      identity_required: ["consistent", "exact"].includes(subj.identity_fidelity) || refs.identity_reference === true,
      brand_text_required: !["none", "UNKNOWN"].includes(brand.mode),
      gaze_required: subj.human === true && ["face", "upper_body", "full_body"].includes(subj.body_visibility),
      hands_required: subj.hands_visible === true, max_prompt_words: ceiling, jobs: 1, max_negative_phrases: 4,
    };
  }
  function sectionsFrom(facts, prompt, baseType) {
    const s = facts.slots, v = variantOf(facts), labelled = {};
    for (const para of prompt.split("\n\n")) { const head = para.split(":")[0]; labelled[head.trim().toLowerCase()] = para.trim(); }
    const blk = {}; let sec;
    if (v === "gpt") {
      sec = { scene: labelled.scene || "", subject: labelled.subject || "", optics: labelled["important details"] || "", usecase: labelled["use case"] || "", constraints: labelled.constraints || "" };
      blk.anatomy = { name: "anatomy", text: s.subject.action };
      if ("contact" in s.subject) blk.contact = { name: "contact", text: s.subject.contact };
    } else if (v === "nb") {
      sec = { scene: s.location, subject: `${s.subject} ${s.action}`, optics: s.composition, usecase: s.style };
      blk.anatomy = { name: "anatomy", text: s.action };
      if ("contact" in s) blk.contact = { name: "contact", text: s.contact };
    } else sec = { change: s.change, preserve: s.preserve, constraints: s.constraints };
    if (baseType === "T1") for (const b of T1_BLOCKS) { const section = { light_hard: "light", skin_doc: "skin", usecase_doc: "usecase", clean_doc: "clean" }[b]; delete sec[section]; blk[section] = { name: b, text: null }; }
    return [sec, blk];
  }
  // template_engine.build(): contrato T1..T5
  const META_RE = /(?:^|\n)\s*(?:model|quality|size|aspect\s*ratio|size\s*\/\s*ratio)\s*:\s*|\b--ar\b/i;
  function templateEngine(D, tipo, sections, blocks, notes) {
    tipo = tipo.toUpperCase();
    const spec = D.templates[tipo];
    if (!spec) return { status: "FAIL", detail: `Unknown template type '${tipo}'` };
    const allowed = new Set([...spec.required, ...spec.optional]);
    const supplied = { ...sections, notes }; for (const [k, v] of Object.entries(blocks)) supplied[k] = v;
    const unknown = Object.keys(supplied).filter((k) => !allowed.has(k));
    if (unknown.length) return { status: "FAIL", detail: `${tipo}: undeclared section(s): ${unknown.sort().join(", ")}` };
    const missing = spec.required.filter((s) => !(s in supplied) || supplied[s] === "" || supplied[s] == null);
    if (missing.length) return { status: "FAIL", detail: `${tipo}: missing required section(s): ${missing.join(", ")}` };
    const values = {}, blockAllowed = (section, name) => { const pre = D.block_families[section]; return !pre || pre.some((p) => name === p || name.startsWith(p)); };
    for (const [section, value] of Object.entries(supplied)) {
      if (section === "notes") { values.notes = String(value).trim(); continue; }
      const isBlock = isObj(value), requiredBlock = section in spec.block_required ? spec.block_required[section] : "__not__";
      if (requiredBlock !== "__not__") {
        if (!isBlock) return { status: "FAIL", detail: `${tipo}.${section} must come from BLOCKS/a named Block` };
        if (requiredBlock && value.name !== requiredBlock) return { status: "FAIL", detail: `${tipo}.${section} requires block '${requiredBlock}', got '${value.name}'` };
        if (!requiredBlock && !blockAllowed(section, value.name)) return { status: "FAIL", detail: `${tipo}.${section}: block '${value.name}' does not belong to section family` };
        values[section] = (value.text == null ? D.blocks[value.name] : value.text).trim();
      } else if (isBlock) {
        if (!blockAllowed(section, value.name)) return { status: "FAIL", detail: `${tipo}.${section}: invalid block '${value.name}'` };
        values[section] = (value.text == null ? D.blocks[value.name] : value.text).trim();
      } else values[section] = String(value).trim();
    }
    if (!values.notes) return { status: "FAIL", detail: `${tipo}: Notes block is mandatory` };
    const order = ["scene", "subject", "anatomy", "contact", "idlock", "optics", "light", "skin", "colour", "hair", "fabric", "mood", "usecase", "clean", "constraints", "autocontain", "text_lock"];
    const body = tipo === "T5" ? [`Change: ${values.change}`, `Preserve: ${values.preserve}`, ...(values.constraints ? [`Constraints: ${values.constraints}`] : [])].join("\n")
      : order.filter((k) => (values[k] || "").trim()).map((k) => values[k].trim()).join("\n\n");
    if (META_RE.test(body)) return { status: "FAIL", detail: "Model/Quality/Size/Aspect ratio metadata must stay outside the prompt body" };
    return { status: "PASS", detail: `${tipo}: ${Object.keys(values).length} secciones` };
  }
  // audit_gi2.py — 15 columnas
  const STANDARD_RATIOS = new Set(["1:1", "3:2", "2:3", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]);
  const SLOP = /\b(?:masterpiece|stunning|epic|beautiful lighting|professional|high quality|highly detailed|4k|8k)\b/gi;
  const NEG = /\b(?:don't|do not|without|avoid)\b/gi;
  const GAZE = /\b(?:gaze|looking|looks|eyes?|face(?:s|d)?|toward(?:s)? camera|off-camera)\b/i;
  const HAND = /\b(?:hand|hands|finger|fingers|grip|fist|palm)\b/i;
  const IDENT = /\b(?:identity|same face|preserve face|facial structure|character anchor|idlock)\b/i;
  const BRAND = /\b(?:logo|brand|wordmark|trademark|signage|lettering|text_lock)\b/i;
  const MOOD = /\b(?:mood|calm|tense|intimate|documentary|editorial|joyful|somber|serene|urgent)\b/i;
  const COLOUR = /\b(?:color|colour|palette|red|blue|green|amber|teal|cyan|magenta|black|white|gray|grey|warm|cool)\b/i;
  function auditGi2(D, a) {
    const tipo = String(a.type || "").toUpperCase(), prompt = String(a.prompt || ""), sections = a.sections || {}, blocks = a.block_ids || {}, metadata = a.metadata || {}, notes = String(a.notes || "").trim(), ctx = a.audit_context || {};
    const checks = [], C = (name, status, detail) => checks.push({ name, status, detail });
    const spec = D.templates[tipo]; let missing = [];
    if (spec) for (const s of spec.required) { if (s === "notes") { if (!notes) missing.push(s); } else if (!String(sections[s] || "").trim()) missing.push(s); }
    else missing = ["known template type"];
    C("slots", missing.length ? "FAIL" : "PASS", missing.length ? "missing: " + missing.join(", ") : "all required slots present");
    const bad = [...new Set((prompt.match(SLOP) || []).map((x) => x.toLowerCase()))].sort();
    C("anti_slop", bad.length ? "FAIL" : "PASS", bad.length ? "found: " + bad.join(", ") : "no banned slop tokens");
    const raw = String(metadata.aspect_ratio || metadata.size_or_ratio || metadata.ratio || ""), rm = /\b(\d{1,2}:\d{1,2})\b/.exec(raw), ratio = rm ? rm[1] : null;
    C("ratio_standard", STANDARD_RATIOS.has(ratio) ? "PASS" : "FAIL", `ratio=${ratio || "missing"}`);
    C("metadata_outside_prompt", META_RE.test(prompt) ? "FAIL" : "PASS", META_RE.test(prompt) ? "metadata syntax found inside prompt" : "metadata outside body");
    C("notes", notes ? "PASS" : "FAIL", notes ? "Notes present" : "Notes missing");
    const opticsText = `${sections.optics || ""} ${prompt}`.toLowerCase();
    const effects = { "compression": ["compression", "compressed perspective", "telephoto compression"], "bokeh/wash": ["bokeh", "background wash", "softly out of focus", "shallow depth"], "vignette": ["vignette", "edge falloff"], "halation": ["halation", "bloom around highlights"], "grain": ["grain", "film grain"] };
    const absent = Object.entries(effects).filter(([, terms]) => !terms.some((t) => opticsText.includes(t))).map(([k]) => k);
    if (ctx.optics_required) C("camera_5_effects", absent.length ? "FAIL" : "PASS", absent.length ? "missing: " + absent.join(", ") : "all five present"); else C("camera_5_effects", "NA", "optics_required=false");
    const moodReq = "mood_required" in ctx ? !!ctx.mood_required : ["T1", "T2", "T3", "T4"].includes(tipo), moodOk = !!(String(sections.mood || "").trim() || MOOD.test(prompt));
    C("mood", moodOk ? "PASS" : moodReq ? "FAIL" : "NA", moodOk ? "mood/use-case signal present" : "mood not established");
    const colourOk = !!(String(sections.colour || "").trim() || COLOUR.test(prompt));
    C("colour", colourOk ? "PASS" : ctx.colour_required ? "FAIL" : "NA", colourOk ? "colour signal present" : "no explicit colour requirement");
    const idOk = "idlock" in blocks || IDENT.test(prompt);
    C("identity_lock", idOk ? "PASS" : ctx.identity_required ? "FAIL" : "NA", idOk ? "identity lock present" : "identity not required");
    const brandOk = "text_lock" in blocks || BRAND.test(prompt);
    C("brand_text", brandOk ? "PASS" : ctx.brand_text_required ? "FAIL" : "NA", brandOk ? "brand/text rule present" : "brand text not required");
    const negatives = (prompt.match(NEG) || []).length;
    C("framing_positive", negatives <= (ctx.max_negative_phrases ?? 4) ? "PASS" : "FAIL", `negative phrases=${negatives}`);
    const gazeOk = GAZE.test(prompt); C("gaze", gazeOk ? "PASS" : ctx.gaze_required ? "FAIL" : "NA", gazeOk ? "gaze/orientation described" : "gaze not required");
    const handsOk = HAND.test(prompt); C("hands", handsOk ? "PASS" : ctx.hands_required ? "FAIL" : "NA", handsOk ? "hands/grip described" : "hands not load-bearing");
    const wc = wordCount(prompt);
    if (ctx.max_prompt_words == null) C("word_ceiling", "NA", `word_count=${wc}; no ceiling supplied`); else C("word_ceiling", wc <= ctx.max_prompt_words ? "PASS" : "FAIL", `${wc}/${ctx.max_prompt_words} words`);
    if (ctx.jobs == null) C("single_job", "NA", "jobs not supplied"); else C("single_job", ctx.jobs === 1 ? "PASS" : "FAIL", `jobs=${ctx.jobs}`);
    return { status: checks.some((c) => c.status === "FAIL") ? "FAIL" : "PASS", checks };
  }
  function structuralGates(D, facts, c, prompt) {
    const out = {}, ceiling = D.ceilings[MODELS[facts.model].capabilities_id] ?? null;
    out.word_ceiling_source = `${D.sources_of_truth.ceilings}#${MODELS[facts.model].capabilities_id}`;
    const tipo = c.base_type, [sec, blk] = sectionsFrom(facts, prompt, tipo);
    const meta = { model: facts.model, quality: facts.quality, size_or_ratio: `${facts.size} (${ratioOf(facts.size)})` };
    out.template_engine = templateEngine(D, tipo, sec, blk, facts.notes);
    const artifact = { type: tipo, prompt, sections: { ...sec, ...Object.fromEntries(Object.entries(blk).map(([k, v]) => [k, v.text == null ? D.blocks[v.name] : v.text])) },
      block_ids: Object.fromEntries(Object.entries(blk).map(([k, v]) => [k, v.name])), metadata: { ...meta, aspect_ratio: ratioOf(facts.size) }, notes: facts.notes, audit_context: auditContext(c, ceiling) };
    const audit = auditGi2(D, artifact);
    out.audit_gi2 = { status: audit.status, detail: audit.checks.filter((x) => x.status === "FAIL").map((x) => `${x.name}: ${x.detail}`) };
    if (!out.audit_gi2.detail.length) out.audit_gi2.detail = "15 columnas sin falla";
    out.audit_checks = audit.checks;
    out.word_count = { status: ceiling && wordCount(prompt) <= ceiling ? "PASS" : "FAIL", detail: `${wordCount(prompt)}/${ceiling}` };
    return out;
  }

  // ---------------------------------------------- validadores mecánicos
  // Mismo motor declarativo que .claude/hooks/rule_validators.py: el artefacto tiene
  // que comprobar las mismas reglas por código, o la paridad sería una mentira.
  function vTarget(art, name) {
    if (name === "prompt") return art.prompt || "";
    if (name === "prompt.main") return String(art.prompt || "").split(/^\s*negative\s*:/im)[0];
    if (name === "prompt.negative") { const p = String(art.prompt || "").split(/^\s*negative\s*:/im); return p.length > 1 ? p[1] : ""; }
    if (name === "notes") return art.notes || "";
    if (name === "provenance") return JSON.stringify(art.provenance || {});
    if (name === "stages") return art.stages || [];
    if (name === "files") return art.files || [];
    if (name.startsWith("slots.")) {
      let cur = art.slots || {};
      for (const p of name.split(".").slice(1)) { cur = cur && typeof cur === "object" ? cur[p] : undefined; if (cur === undefined) return null; }
      return cur;
    }
    return null;
  }
  function vWhen(cond, art) {
    if (!cond) return true;
    if (Array.isArray(cond)) { const r = cond.map((c) => vWhen(c, art)); return r.includes(null) ? null : r.every(Boolean); }
    let cur = art.case || {};
    for (const p of cond.path.split(".")) { cur = cur && typeof cur === "object" ? cur[p] : undefined; if (cur === undefined || cur === null) return null; }
    if (cur === "UNKNOWN") return null;
    const val = Array.isArray(cond.value) ? cond.value : [cond.value];
    return (cond.op || "in") === "in" ? val.includes(cur) : !val.includes(cur);
  }
  // Los patrones vienen de Python, que admite banderas en línea como (?im); JS no.
  // Se quitan y se aplican como banderas del RegExp, que es lo mismo.
  const vRe = (pat) => new RegExp(String(pat).replace(/^\(\?[a-z]+\)/, ""), "im");
  function vEval(spec, art) {
    const ok = vWhen(spec.when, art);
    if (ok === null) return ["UNRESOLVED", "el caso no declara la precondición"];
    if (ok === false) return ["NA", "no aplica a este caso por su precondición"];
    const op = spec.op;
    if (op === "all" || op === "any") {
      const res = spec.checks.map((s) => vEval(s, art));
      if (res.some((r) => r[0] === "UNRESOLVED")) return ["UNRESOLVED", res.filter((r) => r[0] === "UNRESOLVED").map((r) => r[1]).join("; ")];
      const bien = res.map((r) => r[0] === "PASS" || r[0] === "NA");
      const pasa = op === "all" ? bien.every(Boolean) : bien.some(Boolean);
      return pasa ? ["PASS", res.map((r) => r[1]).join("; ").slice(0, 300)]
                  : ["FAIL", res.filter((r) => r[0] === "FAIL").map((r) => r[1]).join("; ").slice(0, 300)];
    }
    if (op === "stage_pass") {
      const st = Object.fromEntries((vTarget(art, "stages") || []).map((s) => [s.name, s.status]));
      if (!(spec.stage in st)) return ["FAIL", `la etapa ${spec.stage} no se ejecutó`];
      return st[spec.stage] === "PASS" ? ["PASS", `etapa ${spec.stage} PASS`] : ["FAIL", `etapa ${spec.stage} en ${st[spec.stage]}`];
    }
    if (op === "file_exists") {
      // La página no tiene sistema de archivos: puede confirmar lo que produjo, no puede
      // demostrar una ausencia. Sin prueba no hay veredicto, así que la regla pasa al
      // auditor en vez de darse por fallada o, peor, por cumplida.
      if ((vTarget(art, "files") || []).includes(spec.file)) return ["PASS", `${spec.file} presente en el run`];
      // Con lista de archivos completa la ausencia es prueba; en el run real de la página
      // la lista es parcial —no hay sistema de archivos— y entonces no hay veredicto: la
      // regla pasa al auditor en vez de darse por fallada o, peor, por cumplida.
      return art.files_complete === false
        ? ["UNRESOLVED", `el artefacto no puede comprobar ${spec.file}: esa etapa corre sólo en la línea de comandos`]
        : ["FAIL", `falta ${spec.file} en el run`];
    }
    const t = vTarget(art, spec.in);
    if (t === null || t === undefined) return ["UNRESOLVED", `sin ${spec.in} en el artefacto`];
    const txt = String(t).toLowerCase();
    if (op === "any_term") { const hit = spec.terms.find((w) => txt.includes(w.toLowerCase())); return hit ? ["PASS", `${spec.in} contiene ${JSON.stringify(hit)}`] : ["FAIL", `${spec.in} no contiene ninguno de: ${spec.terms.slice(0, 6).join(", ")}`]; }
    if (op === "no_term") { const hit = spec.terms.find((w) => txt.includes(w.toLowerCase())); return hit ? ["FAIL", `${spec.in} contiene ${JSON.stringify(hit)}, prohibido`] : ["PASS", `${spec.in} sin términos prohibidos`]; }
    if (op === "regex") return vRe(spec.pattern).test(String(t)) ? ["PASS", `${spec.in} cumple el patrón`] : ["FAIL", spec.fail_reason || `${spec.in} no cumple /${spec.pattern}/`];
    if (op === "no_regex") { const m = String(t).match(vRe(spec.pattern)); return m ? ["FAIL", `${spec.fail_reason || spec.in + " coincide con el patrón"}: ${JSON.stringify(m[0])}`] : ["PASS", `${spec.in} no coincide con /${spec.pattern}/`]; }
    return ["UNRESOLVED", `operación desconocida: ${op}`];
  }
  function vSelftest(e) {
    const t = e.tests || {};
    if (!(t.pass || []).length || !(t.fail || []).length) return [false, "faltan casos de prueba"];
    for (const a of t.pass) { const [s] = vEval(e.check, a); if (s !== "PASS" && s !== "NA") return [false, `el caso que debía pasar dio ${s}`]; }
    for (const a of t.fail) { const [s] = vEval(e.check, a); if (s !== "FAIL") return [false, `el caso que debía fallar dio ${s}`]; }
    return [true, "distingue"];
  }
  function vLoad(D) {
    const out = {};
    for (const e of D.validators || []) {
      if (e.approved_by !== "user") continue;
      if (vSelftest(e)[0]) out[e.rule_id] = e;
    }
    return out;
  }
  function validatorArtifact(facts, caso, prompt, stages, files) {
    return { prompt, notes: facts.notes || "", slots: facts.slots || {}, provenance: facts.provenance || {},
             case: caso, stages: (stages || []).map((s) => ({ name: s.name, status: s.status })),
             files: files || [], files_complete: false };
  }

  function mechanicalEvidence(match, gates, mode, D, art) {
    const ev = {}, pending = [], lex = gates.lexical.banned_vocabulary;
    const validadores = art ? vLoad(D) : {};
    for (const r of match.active_rules) {
      const rid = r.rule_id, vid = (r.metadata.validator || {}).id, kind = (r.metadata.validator || {}).kind;
      if (vid in MECHANICAL) {
        const key = MECHANICAL[vid];
        if ((key === "authorized_delta" || key === "prompt_revision_gate") && mode === "new") ev[rid] = { status: "PASS", by: "apd_run:new", reason: "sin revisión en este run; toda revisión pasa por revise (delta autorizado + prompt_revision_gate_v34)" };
        else if (key === "authorized_delta" || key === "prompt_revision_gate") ev[rid] = { status: "PASS", by: `apd_run:${key}`, reason: "brief_apply_delta_v34 + prompt_patch_v34 + prompt_revision_gate_v34 PASS" };
        else if (key === "generation_params") ev[rid] = { status: "PASS", by: "apd_run:ast.parameters", reason: JSON.stringify(gates.parameters) };
        else if (key === "aspect_ratio") ev[rid] = { status: "PASS", by: "apd_run:ast.parameters", reason: `aspectRatio=${gates.parameters.aspectRatio} derivado de size=${gates.parameters.size || gates.parameters.aspectRatio}` };
        else ev[rid] = { status: "PASS", by: `apd_run:${key}`, reason: `${key}_v34 PASS` };
      } else if (rid === NB_LENS_RULE && gates.lexical.nb_no_numeric_lens) {
        const g = gates.lexical.nb_no_numeric_lens;
        ev[rid] = g.status === "PASS" ? { status: "PASS", by: "apd_run:nb-lens-gate", reason: String(g.detail) } : { status: "FAIL", reason: `parámetros numéricos de objetivo: ${g.detail}` };
      } else if (kind === "lexical") {
        ev[rid] = lex.status === "PASS" ? { status: "PASS", by: "apd_run:lexical-gate", reason: "0 términos prohibidos (dramaturgy.md + gpt-image.md Anti-Slop)" } : { status: "FAIL", reason: `términos prohibidos: ${lex.detail}` };
      } else if (rid in validadores) {
        const [estado, razon] = vEval(validadores[rid].check, art);
        if (estado === "PASS" || estado === "NA") ev[rid] = { status: "PASS", by: `validador:${validadores[rid].source}`, reason: razon };
        else if (estado === "FAIL") ev[rid] = { status: "FAIL", reason: razon };
        else pending.push({ rule_id: rid, kind, source_path: r.rule.source_path, line: r.rule.line, effect: r.metadata.effect, text: r.rule.text, validador_indeciso: razon });
      } else pending.push({ rule_id: rid, kind, source_path: r.rule.source_path, line: r.rule.line, effect: r.metadata.effect, text: r.rule.text });
    }
    return [ev, pending];
  }
  // runtime_ledger_v3.py
  function runtimeLedger(match, evidence) {
    if (match.status !== "PASS") return { status: "FAIL", reason: "rule matching is not PASS" };
    const active = Object.fromEntries(match.active_rules.map((r) => [r.rule_id, r]));
    const pending = [], failed = [], malformed = [], passed = [], overridden = [];
    for (const rid of Object.keys(active)) {
      const e = evidence[rid];
      if (!e) { pending.push(rid); continue; }
      const st = String(e.status || "").toUpperCase();
      if (!["PASS", "FAIL", "OVERRIDE"].includes(st)) { malformed.push([rid, "invalid status"]); continue; }
      if (st === "PASS") { if (!e.by) malformed.push([rid, "PASS requires by"]); else passed.push(rid); }
      else if (st === "FAIL") { if (!e.reason) malformed.push([rid, "FAIL requires reason"]); else failed.push(rid); }
      else { if (!e.reason || !e.authorized_by) malformed.push([rid, "OVERRIDE requires reason + authorized_by"]); else overridden.push(rid); }
    }
    const stale = Object.keys(evidence).filter((k) => !(k in active)).sort();
    const status = !pending.length && !failed.length && !malformed.length ? "PASS" : "FAIL";
    return { status, active_rules: Object.keys(active).length, pass: passed.length, override: overridden.length, fail: failed.length, pending: pending.length, malformed: malformed.length, stale_evidence: stale.length, pending_ids: pending, failed_ids: failed, malformed_items: malformed, stale_ids: stale };
  }

  // ------------------------------------------- tipo sw30 derivado del caso
  // sw30 SKILL.md:37-38: T1 maestro rostro · T2 maestro cuerpo · T3 cuadro 1 persona ·
  // T4 cuadro 2 personas · T5 edición quirúrgica. Las precondiciones T3/T4/T5 son las
  // invariantes de case_validate.py; "maestro" = deliverable.purpose reference_master
  // (enum del Case Fingerprint), rostro/cuerpo = subject.body_visibility.
  function deriveBaseType(c) {
    const subj = c.subject || {}, op = c.operation, purpose = (c.deliverable || {}).purpose, bv = subj.body_visibility;
    if (["image_edit", "image_to_image"].includes(op)) return { base_type: "T5", reason: "operation=image_edit → T5 edición quirúrgica (sw30 SKILL.md:38; case_validate T5)" };
    if (subj.human !== true) return { base_type: null, reason: "sin persona: fuera de la matriz sw30 T1..T5 (SKILL.md:37-38); esta versión sólo renderiza T1..T5" };
    if (isUnknown(subj.count) || typeof subj.count !== "number") return { base_type: null, reason: "subject.count desconocido: no se puede catalogar el tipo" };
    if (subj.count >= 2) return { base_type: "T4", reason: `${subj.count} personas → T4 cuadro 2 personas (sw30 SKILL.md:37; case_validate T4)` };
    if (purpose === "reference_master") {
      if (bv === "face") return { base_type: "T1", reason: "reference_master + body_visibility=face → T1 maestro de rostro (sw30 SKILL.md:37, :65)" };
      if (["full_body", "upper_body"].includes(bv)) return { base_type: "T2", reason: `reference_master + body_visibility=${bv} → T2 maestro de cuerpo (sw30 SKILL.md:37)` };
      return { base_type: null, reason: `reference_master con body_visibility=${bv}: no es rostro ni cuerpo` };
    }
    return { base_type: "T3", reason: "1 persona, cuadro → T3 (sw30 SKILL.md:37; case_validate T3)" };
  }

  // ---------------------------------------------------------------- run
  function makeRun() { return { status: "NEW", created: now(), stages: [], brief_version: 0, prompt_revision: 0, prompt_sha256: null, blocked_by: null, briefs: [], asts: [], prompts: [] }; }
  function stage(run, name, status, detail, onStage) {
    run.stages.push({ name, status, detail, at: now() });
    if (onStage) onStage(run.stages[run.stages.length - 1], run);
    if (status === "FAIL") { run.status = "BLOCKED"; run.blocked_by = name; const e = new Error(`${name}: ${typeof detail === "string" ? detail : JSON.stringify(detail)}`); e.blocked = true; throw e; }
  }
  const short = (errs, n = 6) => errs.slice(0, n).join("; ");

  async function newRun(D, inputs, opts = {}) {
    const run = makeRun(), onStage = opts.onStage;
    const facts = deepcopy(inputs.facts), c = deepcopy(inputs.case);
    run.facts = facts; run.case = c;
    try {
      const errs = validateSchema(facts, D.facts_schema);
      const op = facts.operation || "create";
      if ((facts.references || []).length && op !== "edit" && !("references_line" in (facts.slots || {}))) errs.push("slots.references_line es obligatoria cuando hay references");
      if (!(facts.references || []).length && "references_line" in (facts.slots || {})) errs.push("slots.references_line sin references");
      stage(run, "facts_schema", errs.length ? "FAIL" : "PASS", short(errs) || "facts.schema.json", onStage);
      const perrs = checkProvenance(D, facts);
      stage(run, "facts_provenance", perrs.length ? "FAIL" : "PASS", short(perrs) || `${Object.keys(facts.provenance).length} hojas trazadas`, onStage);
      run.brief = String(inputs.brief || "");
      const lerrs = checkLiteralProvenance(D, facts, run.brief);
      stage(run, "facts_literal", lerrs.length ? "FAIL" : "PASS", short(lerrs) || "todo lo atribuido al skill es literal; todas las citas de Eric están en el brief", onStage);
      if (inputs.strict) { const serrs = checkStrict(D, facts, run.brief); run.strict = true; stage(run, "facts_strict", serrs.length ? "FAIL" : "PASS", short(serrs) || "cada fragmento es literal del brief o del skill; ninguna frase del brief omitida", onStage); }
      const cerrs = [], fam = MODELS[facts.model].family, cop = OPERATIONS[op];
      if (c.media !== "image" || c.stage !== "prompt" || c.operation !== cop) cerrs.push(`case debe ser media=image, stage=prompt, operation=${cop}`);
      if (op === "edit") { if (c.base_type !== "T5") cerrs.push("operation=edit exige case.base_type=T5"); if (!(facts.references || []).length) cerrs.push("operation=edit exige references (la imagen a editar)"); }
      else if (c.base_type === "T5") cerrs.push("case.base_type=T5 exige operation=edit");
      if (variantOf(facts) === "nb" && facts.format !== ratioOf(facts.size)) cerrs.push(`facts.format debe ser ${ratioOf(facts.size)} (nano-banana.md:20 'Format: W:H')`);
      if ((c.generator || {}).model !== facts.model || (c.generator || {}).family !== fam) cerrs.push(`case.generator debe ser ${fam}/${facts.model}`);
      if ((c.deliverable || {}).aspect_ratio !== ratioOf(facts.size)) cerrs.push(`case.deliverable.aspect_ratio debe ser ${ratioOf(facts.size)} (size ${facts.size})`);
      const rmode = (c.references || {}).mode;
      if ((facts.references || []).length && rmode === "none") cerrs.push("facts tiene references pero case.references.mode=none");
      if (!(facts.references || []).length && rmode !== "none") cerrs.push("facts sin references pero case.references.mode≠none");
      if ((facts.references || []).length && ((c.references || {}).roles || []).length !== facts.references.length) cerrs.push("case.references.roles debe tener una entrada por referencia");
      const holder = variantOf(facts) === "gpt" ? (facts.slots || {}).subject : facts.slots, hasContact = isObj(holder) && "contact" in holder;
      if (c.base_type === "T4" && !hasContact) cerrs.push("T4 exige el slot contact");
      if (c.base_type !== "T4" && hasContact) cerrs.push("el slot contact sólo existe en T4");
      const bt = deriveBaseType(c);
      if (bt.base_type !== c.base_type) cerrs.push(`case.base_type=${c.base_type} pero las reglas dan ${bt.base_type || "ninguno"}: ${bt.reason}`);
      stage(run, "facts_case_consistency", cerrs.length ? "FAIL" : "PASS", short(cerrs), onStage);
      stage(run, "tipo_sw30", "PASS", `${bt.base_type}: ${bt.reason}`, onStage);

      const briefInput = {}; for (const [k, v] of Object.entries(facts)) if (k !== "provenance" && k !== "brief_id") briefInput[k] = v;
      const brief = await briefFreeze(briefInput, facts.brief_id, `facts.json sha256:${await sha256(canonical(facts))}`, ["model", "operation", "quality", "size", "references", "notes"]);
      run.briefs.push(brief); run.brief_version = 1;
      stage(run, "brief_freeze", "PASS", `hash: ${brief.brief_hash}`, onStage);
      const missing = preflight(brief);
      stage(run, "brief_preflight", missing.length ? "FAIL" : "PASS", missing.length ? missing.join(", ") : "BRIEF_PREFLIGHT: PASS", onStage);
      const cv = caseValidate(D, c); run.case_validation = cv;
      stage(run, "case_validate", cv.status, short(cv.errors, 5) || `warnings: ${cv.warnings.length}`, onStage);
      const route = modelRoute(D, c); run.route = route;
      const sel = route.selected || {};
      const rok = ["ROUTED", "USER_MODEL_LOCK_PRESERVED"].includes(route.status) && sel.model === facts.model;
      stage(run, "model_router", rok ? "PASS" : "FAIL", `${route.status} → ${sel.family}/${sel.model}`, onStage);
      const match = await ruleMatch(D, c); run.match = match;
      stage(run, "rule_matcher", match.status, match.status === "PASS" ? JSON.stringify(match.counts) : (match.reason || JSON.stringify(match.counts)) + (match.unresolved || []).slice(0, 3).map((r) => ` ${r.rule_id}: ${r.reason}`).join(";"), onStage);
      const ast = buildAst(D, facts, brief, c.base_type);
      run.asts.push(ast); run.prompt_revision = 1;
      stage(run, "ast_schema", "PASS", "prompt-ast v2.0", onStage);
      await renderAndGate(D, run, "new", onStage);
      return run;
    } catch (e) {
      if (e.blocked) return run;
      throw e;
    }
  }
  async function renderAndGate(D, run, mode, onStage) {
    const facts = run.facts, c = run.case, brief = run.briefs[run.brief_version - 1], ast = run.asts[run.prompt_revision - 1];
    const g = astGate(brief, ast); run.ast_gate = g;
    stage(run, "prompt_ast_gate", g.status, g.errors.length ? short(g.errors, 4) : `${g.segments} segmentos, ${g.used_paths.length} rutas`, onStage);
    const prompt = render(ast, brief);
    run.prompts[run.prompt_revision - 1] = prompt; run.prompt = prompt; run.prompt_sha256 = await sha256(prompt);
    stage(run, "prompt_render", "PASS", `${ast.blocks.length} bloques`, onStage);
    const gates = { lexical: lexicalGates(D, prompt, facts), parameters: ast.parameters };
    gates.structural = structuralGates(D, facts, c, prompt); run.gates = gates;
    const fails = [];
    for (const [k, v] of Object.entries(gates.lexical)) if (v.status === "FAIL") fails.push(`${k}: ${Array.isArray(v.detail) ? v.detail.join(", ") : v.detail}`);
    for (const [k, v] of Object.entries(gates.structural)) if (isObj(v) && v.status === "FAIL") fails.push(`${k}: ${Array.isArray(v.detail) ? v.detail.join("; ") : v.detail}`);
    stage(run, "prompt_gates", fails.length ? "FAIL" : "PASS", fails.length ? fails.join("; ").slice(0, 500) : "verbo inicial, lenguaje natural, vocabulario, template_engine, audit_gi2, word ceiling", onStage);
    // Los archivos que este run produjo de verdad. El linter de aurora es un script
    // Python: en el artefacto no corre, así que sus reglas no se dan por comprobadas y
    // pasan al auditor. Es un límite declarado, no una aprobación silenciosa.
    const archivos = ["prompt_v1.ast.json", "template_spec.json", "match.json"];
    const art = validatorArtifact(facts, c, prompt, run.stages, archivos);
    const [ev, pending] = mechanicalEvidence(run.match, gates, mode, D, art);
    run.evidence_mechanical = ev; run.audit_pending = pending;
    const mechFail = Object.entries(ev).filter(([, v]) => v.status === "FAIL").map(([k]) => k);
    stage(run, "mechanical_evidence", mechFail.length ? "FAIL" : "PASS", `${Object.keys(ev).length} mecánicas, ${pending.length} para el auditor` + (mechFail.length ? `; FAIL ${mechFail.join(",")}` : ""), onStage);
    delete run.audit_request; delete run.evidence; delete run.ledger; delete run.deliverable; delete run.deliverable_sha256;
    run.status = "AWAITING_AUDIT";
  }
  function auditPack(D, run, tanda = TANDA) {
    if (run.status !== "AWAITING_AUDIT") throw new Error(`estado ${run.status}; audit-pack requiere AWAITING_AUDIT`);
    const pending = run.audit_pending, f = run.facts, tandas = [];
    for (let i = 0; i < pending.length; i += tanda) tandas.push({ i: tandas.length + 1, rules: pending.slice(i, i + tanda) });
    const nonce = Array.from(root.crypto ? root.crypto.getRandomValues(new Uint8Array(8)) : require("crypto").randomBytes(8)).map((b) => b.toString(16).padStart(2, "0")).join("");
    run.audit_request = { nonce, created: now(), prompt_revision: run.prompt_revision, prompt_sha256: run.prompt_sha256, prompt: run.prompt,
      facts: { slots: f.slots, references: f.references, notes: f.notes, provenance: f.provenance, model: f.model, size: f.size, quality: f.quality }, instructions: D.auditor_md, tandas };
    return run.audit_request;
  }
  function ledger(D, run, evIn, onStage) {
    const retryOk = run.status === "BLOCKED" && ["auditor_evidence", "runtime_ledger"].includes(run.blocked_by);
    if (run.status !== "AWAITING_AUDIT" && !retryOk) throw new Error(`estado ${run.status}; ledger requiere AWAITING_AUDIT`);
    try {
      const req = run.audit_request, errs = [];
      if (!req) stage(run, "auditor_evidence", "FAIL", "no existe audit_request (corre audit-pack)", onStage);
      if (evIn.nonce !== req.nonce) errs.push("nonce no coincide con audit_request");
      if (evIn.prompt_sha256 !== req.prompt_sha256 || req.prompt_sha256 !== run.prompt_sha256) errs.push("prompt_sha256 no coincide con el prompt vigente");
      const entries = evIn.entries || {}, pendingIds = req.tandas.flatMap((t) => t.rules.map((r) => r.rule_id));
      for (const rid of pendingIds) {
        const e = entries[rid];
        if (!e) errs.push(`${rid}: sin entrada del auditor`);
        else if (e.by !== "auditor") errs.push(`${rid}: by debe ser 'auditor'`);
        else if (!["PASS", "FAIL"].includes(e.status)) errs.push(`${rid}: status debe ser PASS o FAIL (OVERRIDE sólo con autorización escrita de Eric)`);
        else if (!String(e.reason || "").trim()) errs.push(`${rid}: reason vacío`);
        else if (!Array.isArray(e.depends_on) || !e.depends_on.length) errs.push(`${rid}: depends_on ausente`);
      }
      stage(run, "auditor_evidence", errs.length ? "FAIL" : "PASS", short(errs) || `${pendingIds.length} entradas válidas`, onStage);
      const merged = deepcopy(run.evidence_mechanical);
      for (const rid of pendingIds) merged[rid] = { status: entries[rid].status, by: "auditor", reason: entries[rid].reason };
      run.evidence = merged;
      const led = runtimeLedger(run.match, merged); run.ledger = led;
      let detail = `active ${led.active_rules} pass ${led.pass} fail ${led.fail} pending ${led.pending} malformed ${led.malformed}`;
      if ((led.failed_ids || []).length) detail += " — FAIL: " + led.failed_ids.slice(0, 5).map((rid) => `${rid}: ${merged[rid].reason.slice(0, 120)}`).join("; ");
      stage(run, "runtime_ledger", led.status, detail, onStage);
      return deliver(run).then(() => run);
    } catch (e) { if (e.blocked) return Promise.resolve(run); throw e; }
  }
  async function deliver(run) {
    const f = run.facts, refs = (f.references || []).map((r) => `Image ${r.index}: ${r.role}`).join(", ") || "none";
    const text = [`Model: ${f.model}`, `Quality: ${f.quality}`, `Size / Ratio: ${f.size} (${ratioOf(f.size)})`, `References: ${refs}`, "Prompt:", run.prompt.trimEnd(), "Notes:", f.notes.trim()].join("\n") + "\n";
    run.deliverable = text; run.deliverable_sha256 = await sha256(text); run.status = "DELIVERED"; run.delivered_at = now();
  }
  async function revise(D, run, delta, prov, opts = {}) {
    const onStage = opts.onStage, prior = { status: run.status, blocked_by: run.blocked_by };
    if (!["DELIVERED", "AWAITING_AUDIT", "BLOCKED"].includes(run.status)) throw new Error(`estado ${run.status}`);
    try {
      const derrs = validateSchema(delta, D.delta_schema);
      if (delta.authorized_by !== "user") derrs.push("authorized_by debe ser 'user' (sólo Eric autoriza un delta)");
      if (!String(delta.reason || "").trim()) derrs.push("reason vacío");
      stage(run, "delta_schema", derrs.length ? "FAIL" : "PASS", short(derrs) || "authorized-delta.schema.json", onStage);
      const perrs = [];
      for (const ch of delta.changes || []) {
        const path = ch.path;
        if (!path.startsWith("slots.")) { perrs.push(`${path}: un delta sólo puede tocar slots.* (modelo, tamaño y referencias exigen run nuevo)`); continue; }
        if (ch.op === "remove") { perrs.push(`${path}: remove deja un campo requerido abierto; usa replace`); continue; }
        const ents = entriesOf(prov || {}, path);
        if (!ents.length || ents.some((e) => !["user", "skill", "research", "asset"].includes(e.source))) perrs.push(`${path}: sin procedencia`);
        for (const e of ents) {
          if (e.source === "skill") { const [ok, why] = resolveSkillRef(D, e.ref); if (!ok) perrs.push(`${path}: skill ref inválida: ${why}`); }
          else if (e.source === "research" && !/^https?:\/\//.test(e.ref)) perrs.push(`${path}: research ref debe ser URL`);
        }
      }
      if (!perrs.length) {
        const tmp = { slots: {}, provenance: {} };
        for (const ch of delta.changes || []) { const parts = ch.path.split("."); let cur = tmp; for (const k of parts.slice(0, -1)) cur = cur[k] = cur[k] || {}; cur[parts[parts.length - 1]] = ch.value; tmp.provenance[ch.path] = (prov || {})[ch.path]; }
        perrs.push(...checkLiteralProvenance(D, tmp, (run.brief || "") + "\n" + String(delta.reason || "")));
      }
      stage(run, "delta_provenance", perrs.length ? "FAIL" : "PASS", short(perrs) || `${(delta.changes || []).length} cambios trazados`, onStage);
      const oldB = run.briefs[run.brief_version - 1];
      const applied = await briefApplyDelta(oldB, delta);
      stage(run, "brief_apply_delta", applied.errors ? "FAIL" : "PASS", applied.errors ? short(applied.errors) : `BRIEF_DELTA: PASS v${applied.brief.brief_version}`, onStage);
      const newB = applied.brief;
      const missing = preflight(newB);
      stage(run, "brief_preflight", missing.length ? "FAIL" : "PASS", missing.length ? missing.join(", ") : "BRIEF_PREFLIGHT: PASS", onStage);
      const oldAst = run.asts[run.prompt_revision - 1];
      const patched = promptPatch(oldAst, oldB, newB, delta, await sha256(canonical(delta)));
      stage(run, "prompt_patch", patched.errors ? "FAIL" : "PASS", patched.errors ? short(patched.errors) : `revision ${patched.ast.prompt_revision}`, onStage);
      const rg = revisionGate(oldAst, patched.ast, oldB, newB, delta);
      stage(run, "prompt_revision_gate", rg.status, rg.errors.length ? short(rg.errors) : "PROMPT_REVISION_GATE: PASS", onStage);
      run.facts.slots = deepcopy(newB.facts.slots); Object.assign(run.facts.provenance, prov || {});
      run.briefs.push(newB); run.brief_version = newB.brief_version; run.asts.push(patched.ast); run.prompt_revision = patched.ast.prompt_revision;
      await renderAndGate(D, run, "revise", onStage);
      return run;
    } catch (e) {
      if (!e.blocked) throw e;
      if (["delta_schema", "delta_provenance"].includes(run.blocked_by)) { run.status = prior.status; run.blocked_by = prior.blocked_by; run.delta_rejected = e.message; }
      return run;
    }
  }
  function auditRequestText(req, tanda) {
    return `${req.instructions}\n\n## audit_request (tanda ${tanda.i} de ${req.tandas.length})\n\n` +
      JSON.stringify({ nonce: req.nonce, prompt_sha256: req.prompt_sha256, prompt: req.prompt, facts: req.facts, rules: tanda.rules }, null, 1) +
      `\n\nResponde ÚNICAMENTE con el JSON de salida descrito arriba, con una entrada por cada uno de los ${tanda.rules.length} rule_id de esta tanda.`;
  }

  root.APD = { MODELS, deriveBaseType, run: newRun, revise, auditPack, ledger, auditRequestText, validateSchema, checkProvenance, checkLiteralProvenance, checkStrict, caseValidate, ruleMatch, modelRoute, buildAst, render, ratioOf, wordCount, sha256, canonical, variantOf, auditGi2, templateEngine, TANDA };
})(typeof window !== "undefined" ? window : globalThis);
