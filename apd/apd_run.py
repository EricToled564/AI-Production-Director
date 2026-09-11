#!/usr/bin/env python3
"""apd_run.py — orquestador fail-closed del proceso AI Production Director v3.4.

Encadena, sin criterio propio, las herramientas del paquete v3.4.0 que ya viven en
`.claude/hooks/` y `production-package/`:

    facts.json + case.json
      → brief_freeze_v34      (hechos congelados, hash)
      → brief_preflight_v34   (ningún campo requerido abierto)
      → case_validate         (Gate A: fingerprint válido)
      → model_router_v33      (ruta canónica + overlay aprendido; lock de usuario)
      → rule_matcher_v3       (1,704 reglas → APPLIES / NA / SUPPRESSED / UNRESOLVED)
      → AST fijo por modelo   (apd/ast) + prompt_ast_gate_v34 + prompt_render_v34
      → gates léxicos del repo (verbo inicial, keyword soup, vocabulario prohibido)
      → production-package    (template_engine T1..T5, audit_gi2 15 columnas)
      → evidencia mecánica    (validadores v3.2/v3.4 + léxicos)
      → audit_request.json    (reglas sin validador mecánico → auditor, otro agente)
      → runtime_ledger_v3     (100% reglas activas PASS/OVERRIDE o no hay entrega)
      → DELIVERABLE.txt + sha256

Lo único que escribe el asistente son facts.json / case.json / delta.json, y cada
hoja de facts lleva procedencia (user | skill | research). El prompt lo produce el
renderizador determinista; una revisión es sólo un delta autorizado (v3.4).

Uso:
    python3 apd/apd_run.py new    --run apd/runs/<id> --facts facts.json --case case.json
    python3 apd/apd_run.py audit-pack --run apd/runs/<id>
    python3 apd/apd_run.py ledger --run apd/runs/<id> --evidence evidence.json
    python3 apd/apd_run.py revise --run apd/runs/<id> --delta delta.json --provenance prov.json
    python3 apd/apd_run.py status --run apd/runs/<id>

Código de salida 0 sólo si el run no quedó BLOCKED.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
import re
import secrets
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HOOKS = REPO / ".claude" / "hooks"
RULES = REPO / ".claude" / "rules"
PKG = REPO / "production-package"
APD = REPO / "apd"
SKILLS_ROOT = Path(os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude" / "skills" / "synced"))

RULESET = RULES / "v3" / "build" / "ruleset-3.4.0.json"
ROUTING_CANONICAL = RULES / "v3" / "build" / "model-routing.canonical-v3.3.json"
ROUTING_LEARNED = RULES / "v3" / "learned" / "model-routing.v3.2.json"
CASE_SCHEMA = RULES / "v3" / "case-fingerprint.schema.json"
AST_SCHEMA = RULES / "v3.4" / "prompt-ast.schema.json"
DELTA_SCHEMA = RULES / "v3.4" / "authorized-delta.schema.json"
FACTS_SCHEMA = APD / "facts.schema.json"

sys.path.insert(0, str(HOOKS))
import gate_dramaturgy  # noqa: E402
import gate_image  # noqa: E402

# facts.model → (case generator family, id en visual-prompt-forge/adapters/_capabilities.json)
MODELS = {
    "gpt-image-2": {"family": "gpt_image", "capabilities_id": "gpt-image", "template": "gpt"},
    "nano-banana-pro": {"family": "nano_banana", "capabilities_id": "nano-banana", "template": "nb"},
    "nano-banana-2": {"family": "nano_banana", "capabilities_id": "nano-banana", "template": "nb"},
}
OPERATIONS = {"create": "text_to_image", "edit": "image_edit"}
# Secciones del template del modelo que el asistente NO puede alterar: vienen de
# image/references/gpt-image.md, "Photoreal Editorial" (líneas 126-135).
# Las etiquetas de slot son las del skill; el verbo inicial es la regla universal
# image/SKILL.md:50 ("start with a verb"). Cada segmento cita la regla del ruleset
# que lo respalda (6d9997eabed1 = image/SKILL.md:43, 5-slot template).
TEMPLATE_RULES = ["6d9997eabed1"]
VERB_RULES = ["a24fed9220cf"]
REF_RULES = ["6d9997eabed1"]
# Nano Banana: image/SKILL.md:40 (f120241be185) manda a nano-banana.md, cuyo orden es
# Subject + Action + Location/context + Composition + Style, cerrado con "Format: W:H"
# (nano-banana.md:13-20). c58caa804ddc (:24) prohíbe parámetros numéricos de objetivo.
NB_RULES = ["f120241be185"]
NB_LENS_RULE = "c58caa804ddc"
# Edición (T5): gpt-image.md:80-83 — Change / Preserve / Constraints; un cambio por
# iteración (:87). template_engine._render_edit produce el mismo formato.
EDIT_RULES = ["6d9997eabed1"]
# T1 maestro de rostro: produccion-visual-sw30/SKILL.md:66-74 (6ea31ee7e2b2, 3821c52f13ac)
# — cuatro bloques canónicos cuyo texto vive en production-package/template_engine.BLOCKS.
T1_RULES = ["6ea31ee7e2b2", "3821c52f13ac"]
T1_BLOCKS = ("light_hard", "skin_doc", "usecase_doc", "clean_doc")

# Validadores del ruleset que este orquestador puede certificar mecánicamente.
MECHANICAL = {
    "v34:brief-freeze": "brief_freeze",
    "v34:brief-preflight": "brief_preflight",
    "v34:authorized-delta": "authorized_delta",
    "v34:prompt-revision-gate": "prompt_revision_gate",
    "v32:generation-params": "generation_params",
    "v32:aspect-ratio-output": "aspect_ratio",
}
TANDA = 40


# ---------------------------------------------------------------- utilidades
def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def jload(p: Path):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def jdump(p: Path, obj) -> None:
    Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def leaves(v, prefix=""):
    """Mismo recorrido que brief_freeze_v34: listas y escalares son hojas."""
    if isinstance(v, dict):
        for k in sorted(v):
            yield from leaves(v[k], f"{prefix}.{k}" if prefix else k)
    else:
        yield prefix, v


def ratio_of(size: str) -> str:
    """'1536x1024' → '3:2'; '16:9' → '16:9'. Ambas formas son válidas en facts.size."""
    sep = "x" if "x" in size.lower() else ":"
    w, h = (int(x) for x in size.lower().split(sep))
    g = math.gcd(w, h)
    return f"{w // g}:{h // g}"


def variant_of(facts: dict) -> str:
    """gpt | gpt-edit | nb — la forma del AST depende sólo de modelo y operación."""
    t = MODELS[facts["model"]]["template"]
    return "gpt-edit" if facts.get("operation", "create") == "edit" else t


def canonical_blocks() -> dict:
    sys.path.insert(0, str(PKG))
    import template_engine  # noqa: E402
    return {k: v.text for k, v in template_engine.BLOCKS.items()}


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+[\w'-]*\b", text))


class Blocked(Exception):
    pass


class Run:
    def __init__(self, path: Path):
        self.dir = Path(path).resolve()
        self.dir.mkdir(parents=True, exist_ok=True)
        self.state_path = self.dir / "run.json"
        self.state = jload(self.state_path) if self.state_path.exists() else {
            "status": "NEW", "created": now(), "stages": [], "brief_version": 0,
            "prompt_revision": 0, "prompt_sha256": None, "blocked_by": None,
        }

    def save(self) -> None:
        self.state["updated"] = now()
        jdump(self.state_path, self.state)

    def stage(self, name: str, status: str, detail: str = "") -> None:
        self.state["stages"].append({"name": name, "status": status, "detail": detail, "at": now()})
        print(f"STAGE {name:24} {status}" + (f" — {detail}" if detail else ""))
        self.save()
        if status == "FAIL":
            self.state["status"] = "BLOCKED"
            self.state["blocked_by"] = name
            self.save()
            raise Blocked(f"{name}: {detail}")

    def tool(self, script: Path, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(script), *map(str, args)],
                              capture_output=True, text=True, cwd=str(cwd or self.dir))

    def brief_path(self, version: int | None = None) -> Path:
        v = version or self.state["brief_version"]
        return self.dir / f"brief_v{v}.lock.json"

    def ast_path(self, rev: int | None = None) -> Path:
        r = rev or self.state["prompt_revision"]
        return self.dir / f"prompt_v{r}.ast.json"

    def prompt_path(self, rev: int | None = None) -> Path:
        r = rev or self.state["prompt_revision"]
        return self.dir / f"prompt_v{r}.txt"


# ------------------------------------------------------- procedencia de hechos
def resolve_skill_ref(ref: str) -> tuple[bool, str]:
    m = re.match(r"^(?P<skill>[\w-]+)/(?P<rel>[\w./-]+\.(?:md|json|yaml|yml)):(?P<line>\d+)(?:-(?P<end>\d+))?$", ref)
    if not m:
        return False, "formato esperado <skill>/<ruta>:<línea>"
    for pattern in (f"*/{m['skill']}/{m['rel']}", f"*/*/{m['skill']}/{m['rel']}"):
        for cand in SKILLS_ROOT.glob(pattern):
            n = len(cand.read_text(encoding="utf-8", errors="replace").splitlines())
            line = int(m["line"])
            end = int(m["end"] or line)
            if line < 1 or end > n or end < line:
                return False, f"{cand.name} tiene {n} líneas; {line}-{end} fuera de rango"
            return True, str(cand)
    return False, f"archivo no instalado bajo {SKILLS_ROOT}"


def check_provenance(facts: dict) -> list[str]:
    prov = facts.get("provenance", {})
    errs = []
    body = {k: v for k, v in facts.items() if k not in ("provenance", "brief_id")}
    for path, _ in leaves(body):
        if path.startswith("references.") or path == "references":
            continue
        e = prov.get(path)
        if not e:
            errs.append(f"{path}: sin procedencia")
            continue
        src, ref = e["source"], e["ref"].strip()
        if src == "skill":
            ok, why = resolve_skill_ref(ref)
            if not ok:
                errs.append(f"{path}: skill ref inválida ({ref}): {why}")
        elif src == "research":
            if not re.match(r"^https?://", ref):
                errs.append(f"{path}: research ref debe ser URL ({ref})")
        elif src == "user":
            if len(ref) < 3:
                errs.append(f"{path}: user ref debe citar la instrucción")
    for i, r in enumerate(facts.get("references", [])):
        e = prov.get(f"references.{i}.role") or prov.get("references")
        if not e:
            errs.append(f"references.{i}.role: sin procedencia")
    stale = [p for p in prov if p not in {x for x, _ in leaves(body)} and not p.startswith("references")]
    if stale:
        errs.append("procedencia de rutas inexistentes: " + ", ".join(stale))
    return errs


def validate_schema(obj, schema_path: Path) -> list[str]:
    import jsonschema
    schema = jload(schema_path)
    v = jsonschema.Draft202012Validator(schema)
    return [f"{'.'.join(map(str, e.path)) or '$'}: {e.message}" for e in sorted(v.iter_errors(obj), key=lambda x: list(x.path))]


# ------------------------------------------------------------------- AST fijo
def build_ast(facts: dict, brief: dict, base_type: str) -> dict:
    """AST v2 determinista: la estructura depende sólo de modelo, operación, tipo T y
    de qué hojas existen en facts. Texto fijo = etiquetas del template del skill +
    verbo 'Create' + bloques canónicos T1. Todo lo demás son bindings a hojas LOCKED."""
    s = facts["slots"]
    v = variant_of(facts)

    def seg(sid, template, bindings, rules):
        return {"id": sid, "kind": "brief_template", "template": template, "bindings": bindings, "source_rules": rules}

    def fixed(sid, text, rules):
        return {"id": sid, "kind": "rule_text", "text": text, "source_rules": rules}

    canon = canonical_blocks()
    blocks = []
    if v == "gpt":
        blocks.append({"id": "opening", "segments": [seg("verb", "Create {opening}.", {"opening": "slots.opening"}, VERB_RULES)]})
        if "references_line" in s:
            blocks.append({"id": "references", "segments": [seg("roles", "{references_line}", {"references_line": "slots.references_line"}, REF_RULES)]})
        blocks.append({"id": "scene", "segments": [seg("scene", "Scene: {location}, {time}, {weather}.",
                       {"location": "slots.scene.location", "time": "slots.scene.time", "weather": "slots.scene.weather"}, TEMPLATE_RULES)]})
        subject = [seg("subject", "Subject: {who}, {action}, {framing}.",
                       {"who": "slots.subject.who", "action": "slots.subject.action", "framing": "slots.subject.framing"}, TEMPLATE_RULES)]
        if "contact" in s["subject"]:
            subject.append(seg("contact", "{contact}.", {"contact": "slots.subject.contact"}, TEMPLATE_RULES))
        blocks.append({"id": "subject", "segments": subject})
        details = [seg("details", "Important Details: {lens_feel}, {light_source}, {surface_wear}, {imperfections}, {real_texture}.",
                       {"lens_feel": "slots.details.lens_feel", "light_source": "slots.details.light_source",
                        "surface_wear": "slots.details.surface_wear", "imperfections": "slots.details.imperfections",
                        "real_texture": "slots.details.real_texture"}, TEMPLATE_RULES)]
        use_case = [seg("use_case", "Use Case: {use_case}.", {"use_case": "slots.use_case"}, TEMPLATE_RULES)]
        constraints = [seg("constraints", "Constraints: {constraints}.", {"constraints": "slots.constraints"}, TEMPLATE_RULES)]
        if base_type == "T1":
            details += [fixed("light_hard", canon["light_hard"], T1_RULES), fixed("skin_doc", canon["skin_doc"], T1_RULES)]
            use_case.append(fixed("usecase_doc", canon["usecase_doc"], T1_RULES))
            constraints.append(fixed("clean_doc", canon["clean_doc"], T1_RULES))
        blocks += [{"id": "details", "segments": details}, {"id": "use_case", "segments": use_case}, {"id": "constraints", "segments": constraints}]
    elif v == "nb":
        blocks.append({"id": "opening", "segments": [seg("verb", "Create {opening}.", {"opening": "slots.opening"}, VERB_RULES)]})
        if "references_line" in s:
            blocks.append({"id": "references", "segments": [seg("roles", "{references_line}", {"references_line": "slots.references_line"}, REF_RULES)]})
        body = [seg("subject", "{subject} {action} {location}.", {"subject": "slots.subject", "action": "slots.action", "location": "slots.location"}, NB_RULES),
                seg("composition", "{composition}.", {"composition": "slots.composition"}, NB_RULES),
                seg("style", "{style}.", {"style": "slots.style"}, NB_RULES)]
        if "contact" in s:
            body.insert(1, seg("contact", "{contact}.", {"contact": "slots.contact"}, NB_RULES))
        blocks.append({"id": "body", "segments": body})
        if base_type == "T1":
            blocks.append({"id": "t1", "segments": [fixed(b, canon[b], T1_RULES) for b in T1_BLOCKS]})
        blocks.append({"id": "format", "segments": [seg("format", "Format: {format}.", {"format": "format"}, NB_RULES)]})
    else:  # gpt-edit
        blocks.append({"id": "change", "segments": [seg("change", "Change: {change}.", {"change": "slots.change"}, EDIT_RULES)]})
        blocks.append({"id": "preserve", "segments": [seg("preserve", "Preserve: {preserve}.", {"preserve": "slots.preserve"}, EDIT_RULES)]})
        blocks.append({"id": "constraints", "segments": [seg("constraints", "Constraints: {constraints}.", {"constraints": "slots.constraints"}, EDIT_RULES)]})
    params = {"quality": facts["quality"], "aspectRatio": ratio_of(facts["size"])}
    if "x" in facts["size"].lower():
        params["size"] = facts["size"]
    return {
        "schema_version": "2.0",
        "prompt_id": facts["brief_id"],
        "prompt_revision": 1,
        "brief_hash": brief["brief_hash"],
        "model": facts["model"],
        "parameters": params,
        "blocks": blocks,
    }


# --------------------------------------------------------------------- gates
def capabilities_ceiling(model: str) -> tuple[int | None, str]:
    cid = MODELS[model]["capabilities_id"]
    for pattern in ("*/visual-prompt-forge/adapters/_capabilities.json", "*/*/visual-prompt-forge/adapters/_capabilities.json"):
        for cand in SKILLS_ROOT.glob(pattern):
            for g in jload(cand).get("generators", []):
                if g.get("id") == cid:
                    return int(g["max_prompt_words"]), f"{cand}#{cid}"
    return None, "visual-prompt-forge/adapters/_capabilities.json no instalado"


NB_LENS_RE = re.compile(r"\b\d{2,3}\s?mm\b|\bf/\d|\bISO\s?\d", re.IGNORECASE)


def lexical_gates(prompt: str, facts: dict) -> dict:
    out = {}
    v = variant_of(facts)
    rules = gate_image.find_golden_rules()
    verbs = gate_image.load_verbs(rules) if rules else []
    first = next((l.strip() for l in prompt.splitlines() if l.strip()), "")
    if v == "gpt-edit":
        # El template de edición del modelo abre con "Change:" (gpt-image.md:80-83); la
        # sintaxis del modelo destino manda sobre la regla genérica (APD §6.2, política
        # final_prompt.syntax_authority del ruleset).
        out["start_with_verb"] = {"status": "PASS" if first.lower().startswith("change:") else "FAIL",
                                  "detail": f'edición: primera línea "{first[:60]}" debe ser "Change:"', "source": "image/references/gpt-image.md:80-83"}
    else:
        out["start_with_verb"] = {
            "status": "PASS" if verbs and any(first.lower().startswith(v) for v in verbs) else "FAIL",
            "detail": f'primera línea: "{first[:60]}"; verbos: {", ".join(verbs) or "golden-rules.md no encontrado"}',
            "source": str(rules) if rules else None,
        }
    if v == "nb":
        hits = NB_LENS_RE.findall(prompt)
        out["nb_no_numeric_lens"] = {"status": "FAIL" if hits else "PASS", "detail": hits or "sin 50mm / f/2.8 / ISO", "source": "image/references/nano-banana.md:24"}
    soup = [l.strip() for l in prompt.splitlines() if gate_image.is_keyword_soup(l)]
    out["natural_language"] = {"status": "FAIL" if soup else "PASS", "detail": soup[:3] or "sin keyword soup", "source": str(rules) if rules else None}
    banned = []
    dram = gate_dramaturgy.find_dramaturgy()
    anti = gate_dramaturgy.find_antislop()
    terms = (gate_dramaturgy.load_banned(dram) if dram else []) + (gate_dramaturgy.load_antislop(anti) if anti else [])
    low = prompt.lower()
    for t in sorted(set(terms)):
        if re.search(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", low):
            banned.append(t)
    out["banned_vocabulary"] = {
        "status": "FAIL" if banned or not terms else "PASS",
        "detail": banned or ("sin términos prohibidos" if terms else "listas no encontradas"),
        "source": [str(dram) if dram else None, str(anti) if anti else None],
    }
    return out


def audit_context(case: dict, ceiling: int | None) -> dict:
    subj, refs, brand = case["subject"], case["references"], case["brand"]
    return {
        "optics_required": False,  # RULES_MATRIX: COND; no hay tipo que lo exija por sí solo
        "mood_required": case["base_type"] in {"T1", "T2", "T3", "T4"},
        "colour_required": False,
        "identity_required": subj["identity_fidelity"] in {"consistent", "exact"} or refs.get("identity_reference") is True,
        "brand_text_required": brand["mode"] not in {"none", "UNKNOWN"},
        "gaze_required": subj["human"] is True and subj["body_visibility"] in {"face", "upper_body", "full_body"},
        "hands_required": subj["hands_visible"] is True,
        "max_prompt_words": ceiling,
        "jobs": 1,  # una generación = un trabajo (sw30 regla 1)
        "max_negative_phrases": 4,
    }


def sections_from(facts: dict, prompt: str, base_type: str) -> tuple[dict, dict]:
    """Secciones sw30 (T1..T5) derivadas de los bloques renderizados.
    gpt: anatomy ⇐ Subject.action (gpt-image.md:128 'who, action, framing').
    nb:  scene ⇐ location, subject ⇐ subject+action, anatomy ⇐ action, usecase ⇐ style
         (nano-banana.md:13-14, la posición Style cumple el rol del use case).
    T1:  light/skin/usecase/clean = bloques canónicos (sw30 SKILL.md:66-74)."""
    s = facts["slots"]
    v = variant_of(facts)
    labelled = {}
    for para in prompt.split("\n\n"):
        head, _, _ = para.partition(":")
        labelled[head.strip().lower()] = para.strip()
    blk = {}
    if v == "gpt":
        sec = {"scene": labelled.get("scene", ""), "subject": labelled.get("subject", ""), "optics": labelled.get("important details", ""),
               "usecase": labelled.get("use case", ""), "constraints": labelled.get("constraints", "")}
        blk["anatomy"] = {"name": "anatomy", "text": s["subject"]["action"]}
        if "contact" in s["subject"]:
            blk["contact"] = {"name": "contact", "text": s["subject"]["contact"]}
    elif v == "nb":
        sec = {"scene": s["location"], "subject": f'{s["subject"]} {s["action"]}', "optics": s["composition"], "usecase": s["style"]}
        blk["anatomy"] = {"name": "anatomy", "text": s["action"]}
        if "contact" in s:
            blk["contact"] = {"name": "contact", "text": s["contact"]}
    else:
        sec = {"change": s["change"], "preserve": s["preserve"], "constraints": s["constraints"]}
    if base_type == "T1":
        for b in T1_BLOCKS:
            section = {"light_hard": "light", "skin_doc": "skin", "usecase_doc": "usecase", "clean_doc": "clean"}[b]
            sec.pop(section, None)
            blk[section] = {"name": b, "text": None}
    return sec, blk


def structural_gates(run: Run, facts: dict, case: dict, prompt: str) -> dict:
    out = {}
    ceiling, src = capabilities_ceiling(facts["model"])
    out["word_ceiling_source"] = src
    tipo = case["base_type"]
    sec, blk = sections_from(facts, prompt, tipo)
    refs = [f"Image {r['index']}: {r['role']}" for r in facts["references"]]
    meta = {"model": facts["model"], "quality": facts["quality"], "size_or_ratio": f"{facts['size']} ({ratio_of(facts['size'])})"}
    canon = canonical_blocks()
    spec_blocks = {k: (v["name"] if v["text"] is None else v) for k, v in blk.items()}
    spec = {"type": tipo, "metadata": meta, "references": refs, "sections": {**sec, "notes": facts["notes"]}, "blocks": spec_blocks}
    spec_path = run.dir / "template_spec.json"
    jdump(spec_path, spec)
    p = run.tool(PKG / "template_engine.py", "--build", spec_path, "--json")
    out["template_engine"] = {"status": "PASS" if p.returncode == 0 else "FAIL", "detail": (p.stdout + p.stderr).strip()[-600:]}

    artifact = {"type": tipo, "prompt": prompt, "sections": {**sec, **{k: (canon[v["name"]] if v["text"] is None else v["text"]) for k, v in blk.items()}},
                "block_ids": {k: v["name"] for k, v in blk.items()},
                "metadata": {**meta, "aspect_ratio": ratio_of(facts["size"])}, "notes": facts["notes"],
                "audit_context": audit_context(case, ceiling)}
    art_path = run.dir / "artifact.json"
    jdump(art_path, artifact)
    p = run.tool(PKG / "audit_gi2.py", art_path, "--json")
    try:
        audit = json.loads(p.stdout)
    except json.JSONDecodeError:
        audit = {"status": "FAIL", "raw": (p.stdout + p.stderr)[-600:]}
    jdump(run.dir / "audit_gi2.json", audit)
    failing = [c for c in audit.get("checks", []) if c.get("status") == "FAIL"]
    out["audit_gi2"] = {"status": audit.get("status", "FAIL"), "detail": [f"{c['name']}: {c['detail']}" for c in failing] or "15 columnas sin falla"}
    out["word_count"] = {"status": "PASS" if ceiling and word_count(prompt) <= ceiling else "FAIL", "detail": f"{word_count(prompt)}/{ceiling}"}
    return out


# ------------------------------------------------------------- evidencia mecánica
def mechanical_evidence(run: Run, match: dict, gates: dict, mode: str) -> tuple[dict, list[dict]]:
    """Evidencia que este orquestador puede firmar; el resto va al auditor."""
    ev, pending = {}, []
    lex = gates["lexical"]["banned_vocabulary"]
    for r in match["active_rules"]:
        rid = r["rule_id"]
        vid = r["metadata"]["validator"]["id"]
        kind = r["metadata"]["validator"]["kind"]
        if vid in MECHANICAL:
            key = MECHANICAL[vid]
            if key in ("authorized_delta", "prompt_revision_gate") and mode == "new":
                ev[rid] = {"status": "PASS", "by": "apd_run:new", "reason": "sin revisión en este run; toda revisión pasa por `revise` (delta autorizado + prompt_revision_gate_v34)"}
            elif key in ("authorized_delta", "prompt_revision_gate"):
                ev[rid] = {"status": "PASS", "by": f"apd_run:{key}", "reason": "brief_apply_delta_v34 + prompt_patch_v34 + prompt_revision_gate_v34 PASS"}
            elif key == "generation_params":
                ev[rid] = {"status": "PASS", "by": "apd_run:ast.parameters", "reason": json.dumps(gates["parameters"])}
            elif key == "aspect_ratio":
                ev[rid] = {"status": "PASS", "by": "apd_run:ast.parameters", "reason": f"aspectRatio={gates['parameters']['aspectRatio']} derivado de size={gates['parameters'].get('size', gates['parameters']['aspectRatio'])}"}
            else:
                ev[rid] = {"status": "PASS", "by": f"apd_run:{key}", "reason": f"{key}_v34 PASS"}
        elif rid == NB_LENS_RULE and "nb_no_numeric_lens" in gates["lexical"]:
            g = gates["lexical"]["nb_no_numeric_lens"]
            ev[rid] = {"status": g["status"], "by": "apd_run:nb-lens-gate", "reason": str(g["detail"])} if g["status"] == "PASS" else {"status": "FAIL", "reason": f"parámetros numéricos de objetivo: {g['detail']}"}
        elif kind == "lexical":
            if lex["status"] == "PASS":
                ev[rid] = {"status": "PASS", "by": "apd_run:lexical-gate", "reason": "0 términos prohibidos (dramaturgy.md + gpt-image.md Anti-Slop)"}
            else:
                ev[rid] = {"status": "FAIL", "reason": f"términos prohibidos: {lex['detail']}"}
        else:
            pending.append({"rule_id": rid, "kind": kind, "source_path": r["rule"].get("source_path"),
                            "line": r["rule"].get("line"), "effect": r["metadata"].get("effect"), "text": r["rule"]["text"]})
    return ev, pending


# ------------------------------------------------------------------ comandos
def cmd_new(a) -> int:
    run = Run(a.run)
    if run.state["status"] != "NEW":
        print(f"APD_RUN: el run ya existe con estado {run.state['status']}; usa otro directorio")
        return 1
    try:
        facts = jload(a.facts)
        case = jload(a.case)
        errs = validate_schema(facts, FACTS_SCHEMA)
        if facts.get("references") and facts.get("operation", "create") != "edit" and "references_line" not in facts.get("slots", {}):
            errs.append("slots.references_line es obligatoria cuando hay references")
        if not facts.get("references") and "references_line" in facts.get("slots", {}):
            errs.append("slots.references_line sin references")
        run.stage("facts_schema", "FAIL" if errs else "PASS", "; ".join(errs) or FACTS_SCHEMA.name)
        perrs = check_provenance(facts)
        run.stage("facts_provenance", "FAIL" if perrs else "PASS", "; ".join(perrs[:6]) or f"{len(facts['provenance'])} hojas trazadas")
        jdump(run.dir / "facts.json", facts)
        jdump(run.dir / "case.json", case)

        # consistencia mecánica facts ↔ case
        cerrs = []
        fam = MODELS[facts["model"]]["family"]
        op = OPERATIONS[facts.get("operation", "create")]
        if case.get("media") != "image" or case.get("stage") != "prompt" or case.get("operation") != op:
            cerrs.append(f"case debe ser media=image, stage=prompt, operation={op}")
        if facts.get("operation", "create") == "edit":
            if case.get("base_type") != "T5":
                cerrs.append("operation=edit exige case.base_type=T5")
            if not facts["references"]:
                cerrs.append("operation=edit exige references (la imagen a editar)")
        elif case.get("base_type") == "T5":
            cerrs.append("case.base_type=T5 exige operation=edit")
        if variant_of(facts) == "nb" and facts.get("format") != ratio_of(facts["size"]):
            cerrs.append(f"facts.format debe ser {ratio_of(facts['size'])} (nano-banana.md:20 'Format: W:H')")
        if case.get("generator", {}).get("model") != facts["model"] or case.get("generator", {}).get("family") != fam:
            cerrs.append(f"case.generator debe ser {fam}/{facts['model']}")
        if case.get("deliverable", {}).get("aspect_ratio") != ratio_of(facts["size"]):
            cerrs.append(f"case.deliverable.aspect_ratio debe ser {ratio_of(facts['size'])} (size {facts['size']})")
        rmode = case.get("references", {}).get("mode")
        if facts["references"] and rmode == "none":
            cerrs.append("facts tiene references pero case.references.mode=none")
        if not facts["references"] and rmode != "none":
            cerrs.append("facts sin references pero case.references.mode≠none")
        if facts["references"] and len(case.get("references", {}).get("roles", [])) != len(facts["references"]):
            cerrs.append("case.references.roles debe tener una entrada por referencia")
        contact_holder = facts["slots"].get("subject") if variant_of(facts) == "gpt" else facts["slots"]
        has_contact = isinstance(contact_holder, dict) and "contact" in contact_holder
        if case.get("base_type") == "T4" and not has_contact:
            cerrs.append("T4 exige el slot contact")
        if case.get("base_type") != "T4" and has_contact:
            cerrs.append("el slot contact sólo existe en T4")
        run.stage("facts_case_consistency", "FAIL" if cerrs else "PASS", "; ".join(cerrs))

        # brief freeze
        brief_input = {k: v for k, v in facts.items() if k not in ("provenance", "brief_id")}
        jdump(run.dir / "brief_input.json", brief_input)
        run.state["brief_version"] = 1
        p = run.tool(HOOKS / "brief_freeze_v34.py", "--input", run.dir / "brief_input.json", "--brief-id", facts["brief_id"],
                     "--source-id", f"facts.json sha256:{sha256_file(run.dir / 'facts.json')}",
                     *sum([["--prompt-optional-prefix", x] for x in ("model", "operation", "quality", "size", "references", "notes")], []),
                     "--out", run.brief_path(1))
        run.stage("brief_freeze", "PASS" if p.returncode == 0 else "FAIL", (p.stdout + p.stderr).strip().splitlines()[-2:][0] if p.stdout else p.stderr[-300:])
        p = run.tool(HOOKS / "brief_preflight_v34.py", "--brief", run.brief_path(1))
        run.stage("brief_preflight", "PASS" if p.returncode == 0 else "FAIL", (p.stdout + p.stderr).strip()[-300:])

        # Gate A + routing + matching
        p = run.tool(HOOKS / "case_validate.py", run.dir / "case.json", "--json")
        cv = json.loads(p.stdout) if p.stdout.strip().startswith("{") else {"status": "FAIL", "errors": [p.stderr[-300:]]}
        jdump(run.dir / "case_validation.json", cv)
        run.stage("case_validate", cv["status"], "; ".join(cv.get("errors", [])[:5]) or f"warnings: {len(cv.get('warnings', []))}")
        p = run.tool(HOOKS / "model_router_v33.py", "--case", run.dir / "case.json", "--canonical", ROUTING_CANONICAL,
                     "--learned", ROUTING_LEARNED, "--schema", CASE_SCHEMA, "--json")
        route = json.loads(p.stdout) if p.stdout.strip().startswith("{") else {"status": "CASE_INVALID", "raw": p.stderr[-300:]}
        jdump(run.dir / "route.json", route)
        sel = route.get("selected") or {}
        ok = route["status"] in {"ROUTED", "USER_MODEL_LOCK_PRESERVED"} and sel.get("model") == facts["model"]
        run.stage("model_router", "PASS" if ok else "FAIL", f"{route['status']} → {sel.get('family')}/{sel.get('model')}")
        p = run.tool(HOOKS / "rule_matcher_v3.py", "--ruleset", RULESET, "--case", run.dir / "case.json", "--out", run.dir / "match.json")
        match = jload(run.dir / "match.json") if (run.dir / "match.json").exists() else {"status": "FAIL", "counts": {}}
        run.stage("rule_matcher", match["status"], json.dumps(match.get("counts", {})) if match["status"] == "PASS" else (p.stdout + p.stderr)[-400:])

        # AST + render
        run.state["prompt_revision"] = 1
        ast = build_ast(facts, jload(run.brief_path(1)), case["base_type"])
        aerrs = validate_schema(ast, AST_SCHEMA)
        jdump(run.ast_path(1), ast)
        run.stage("ast_schema", "FAIL" if aerrs else "PASS", "; ".join(aerrs) or AST_SCHEMA.name)
        _render(run, facts, case, match, mode="new")
        return 0
    except Blocked as e:
        print(f"APD_RUN: BLOCKED — {e}")
        return 1


def _render(run: Run, facts: dict, case: dict, match: dict, mode: str) -> None:
    brief = run.brief_path()
    ast = run.ast_path()
    p = run.tool(HOOKS / "prompt_ast_gate_v34.py", "--brief", brief, "--ast", ast, "--json")
    g = json.loads(p.stdout) if p.stdout.strip().startswith("{") else {"status": "FAIL", "errors": [p.stderr[-300:]]}
    jdump(run.dir / "ast_gate.json", g)
    run.stage("prompt_ast_gate", g["status"], "; ".join(g.get("errors", [])[:4]) or f"{g.get('segments')} segmentos, {len(g.get('used_paths', []))} rutas")
    p = run.tool(HOOKS / "prompt_render_v34.py", "--ast", ast, "--brief", brief, "--out", run.prompt_path())
    run.stage("prompt_render", "PASS" if p.returncode == 0 else "FAIL", (p.stdout + p.stderr).strip()[-200:])
    prompt = run.prompt_path().read_text(encoding="utf-8")
    run.state["prompt_sha256"] = sha256_text(prompt)

    gates = {"lexical": lexical_gates(prompt, facts), "parameters": jload(ast)["parameters"]}
    gates["structural"] = structural_gates(run, facts, case, prompt)
    jdump(run.dir / "gates.json", gates)
    fails = [f"{k}: {v['detail']}" for k, v in {**gates["lexical"], **{x: y for x, y in gates["structural"].items() if isinstance(y, dict)}}.items() if v.get("status") == "FAIL"]
    run.stage("prompt_gates", "FAIL" if fails else "PASS", "; ".join(map(str, fails))[:500] or "verbo inicial, lenguaje natural, vocabulario, template_engine, audit_gi2, word ceiling")

    ev, pending = mechanical_evidence(run, match, gates, mode)
    jdump(run.dir / "evidence.mechanical.json", ev)
    jdump(run.dir / "audit_pending.json", pending)
    mech_fail = [k for k, v in ev.items() if v["status"] == "FAIL"]
    run.stage("mechanical_evidence", "FAIL" if mech_fail else "PASS", f"{len(ev)} mecánicas, {len(pending)} para el auditor" + (f"; FAIL {mech_fail}" if mech_fail else ""))
    for stale in ("audit_request.json", "evidence.json", "ledger.json", "DELIVERABLE.txt", "deliverable.sha256"):
        (run.dir / stale).unlink(missing_ok=True)
    run.state["status"] = "AWAITING_AUDIT"
    run.save()
    print(f"APD_RUN: AWAITING_AUDIT — {run.prompt_path().name} sha256 {run.state['prompt_sha256']}")


def cmd_audit_pack(a) -> int:
    run = Run(a.run)
    if run.state["status"] not in {"AWAITING_AUDIT"}:
        print(f"APD_RUN: estado {run.state['status']}; audit-pack requiere AWAITING_AUDIT")
        return 1
    pending = jload(run.dir / "audit_pending.json")
    facts = jload(run.dir / "facts.json")
    prompt = run.prompt_path().read_text(encoding="utf-8")
    req = {
        "nonce": secrets.token_hex(8),
        "created": now(),
        "run": str(run.dir),
        "prompt_revision": run.state["prompt_revision"],
        "prompt_sha256": sha256_text(prompt),
        "prompt": prompt,
        "facts": {k: facts[k] for k in ("slots", "references", "notes", "provenance", "model", "size", "quality")},
        "instructions": str(APD / "AUDITOR.md"),
        "tandas": [{"i": i + 1, "rules": pending[j:j + TANDA]} for i, j in enumerate(range(0, len(pending), TANDA))],
    }
    jdump(run.dir / "audit_request.json", req)
    run.state["audit_nonce"] = req["nonce"]
    run.save()
    print(f"AUDIT_PACK: {len(pending)} reglas en {len(req['tandas'])} tandas → {run.dir / 'audit_request.json'} (nonce {req['nonce']})")
    return 0


def cmd_ledger(a) -> int:
    run = Run(a.run)
    retry_ok = run.state["status"] == "BLOCKED" and run.state.get("blocked_by") in {"auditor_evidence", "runtime_ledger"}
    if run.state["status"] != "AWAITING_AUDIT" and not retry_ok:
        print(f"APD_RUN: estado {run.state['status']}; ledger requiere AWAITING_AUDIT")
        return 1
    try:
        req_path = run.dir / "audit_request.json"
        if not req_path.exists():
            run.stage("auditor_evidence", "FAIL", "no existe audit_request.json (corre audit-pack)")
        req = jload(req_path)
        ev_in = jload(a.evidence)
        errs = []
        if ev_in.get("nonce") != req["nonce"]:
            errs.append("nonce no coincide con audit_request.json")
        if ev_in.get("prompt_sha256") != req["prompt_sha256"] or req["prompt_sha256"] != run.state["prompt_sha256"]:
            errs.append("prompt_sha256 no coincide con el prompt vigente")
        entries = ev_in.get("entries", {})
        pending_ids = [r["rule_id"] for t in req["tandas"] for r in t["rules"]]
        for rid in pending_ids:
            e = entries.get(rid)
            if not e:
                errs.append(f"{rid}: sin entrada del auditor")
            elif e.get("by") != "auditor":
                errs.append(f"{rid}: by debe ser 'auditor'")
            elif e.get("status") not in {"PASS", "FAIL"}:
                errs.append(f"{rid}: status debe ser PASS o FAIL (OVERRIDE sólo con autorización escrita de Eric)")
            elif not str(e.get("reason", "")).strip():
                errs.append(f"{rid}: reason vacío")
        run.stage("auditor_evidence", "FAIL" if errs else "PASS", "; ".join(errs[:6]) or f"{len(pending_ids)} entradas válidas")
        merged = jload(run.dir / "evidence.mechanical.json")
        for rid in pending_ids:
            merged[rid] = {"status": entries[rid]["status"], "by": "auditor", "reason": entries[rid]["reason"]}
        jdump(run.dir / "evidence.json", merged)
        p = run.tool(HOOKS / "runtime_ledger_v3.py", "--matched", run.dir / "match.json", "--evidence", run.dir / "evidence.json", "--json")
        led = json.loads(p.stdout) if p.stdout.strip().startswith("{") else {"status": "FAIL", "raw": (p.stdout + p.stderr)[-400:]}
        jdump(run.dir / "ledger.json", led)
        failed = led.get("failed_ids", [])
        detail = f"active {led.get('active_rules')} pass {led.get('pass')} fail {led.get('fail')} pending {led.get('pending')} malformed {led.get('malformed')}"
        if failed:
            detail += " — FAIL: " + "; ".join(f"{rid}: {merged[rid]['reason'][:120]}" for rid in failed[:5])
        run.stage("runtime_ledger", led["status"], detail)
        _deliver(run)
        return 0
    except Blocked as e:
        print(f"APD_RUN: BLOCKED — {e}")
        return 1


def _deliver(run: Run) -> None:
    facts = jload(run.dir / "facts.json")
    prompt = run.prompt_path().read_text(encoding="utf-8")
    refs = ", ".join(f"Image {r['index']}: {r['role']}" for r in facts["references"]) or "none"
    text = "\n".join([
        f"Model: {facts['model']}",
        f"Quality: {facts['quality']}",
        f"Size / Ratio: {facts['size']} ({ratio_of(facts['size'])})",
        f"References: {refs}",
        "Prompt:",
        prompt.rstrip(),
        "Notes:",
        facts["notes"].strip(),
    ]) + "\n"
    (run.dir / "DELIVERABLE.txt").write_text(text, encoding="utf-8")
    (run.dir / "deliverable.sha256").write_text(f"{sha256_text(text)}  DELIVERABLE.txt\n{sha256_text(prompt)}  {run.prompt_path().name}\n", encoding="utf-8")
    run.state["status"] = "DELIVERED"
    run.state["delivered_at"] = now()
    run.state["deliverable_sha256"] = sha256_text(text)
    run.save()
    print(f"APD_RUN: DELIVERED — {run.dir / 'DELIVERABLE.txt'}")


def cmd_revise(a) -> int:
    run = Run(a.run)
    if run.state["status"] not in {"DELIVERED", "AWAITING_AUDIT", "BLOCKED"}:
        print(f"APD_RUN: estado {run.state['status']}")
        return 1
    prior = {k: run.state.get(k) for k in ("status", "blocked_by")}
    try:
        delta = jload(a.delta)
        derrs = validate_schema(delta, DELTA_SCHEMA)
        if delta.get("authorized_by") != "user":
            derrs.append("authorized_by debe ser 'user' (sólo Eric autoriza un delta)")
        if not str(delta.get("reason", "")).strip():
            derrs.append("reason vacío")
        run.stage("delta_schema", "FAIL" if derrs else "PASS", "; ".join(derrs) or DELTA_SCHEMA.name)
        facts = jload(run.dir / "facts.json")
        prov = jload(a.provenance) if a.provenance else {}
        perrs = []
        for c in delta["changes"]:
            path = c["path"]
            if not path.startswith("slots."):
                perrs.append(f"{path}: un delta sólo puede tocar slots.* (modelo, tamaño y referencias exigen run nuevo)")
                continue
            if c["op"] == "remove":
                perrs.append(f"{path}: remove deja un campo requerido abierto; usa replace")
                continue
            e = prov.get(path)
            if not e or e.get("source") not in {"user", "skill", "research"}:
                perrs.append(f"{path}: sin procedencia en --provenance")
            elif e["source"] == "skill":
                ok, why = resolve_skill_ref(e["ref"])
                if not ok:
                    perrs.append(f"{path}: skill ref inválida: {why}")
            elif e["source"] == "research" and not re.match(r"^https?://", e["ref"]):
                perrs.append(f"{path}: research ref debe ser URL")
        run.stage("delta_provenance", "FAIL" if perrs else "PASS", "; ".join(perrs[:6]) or f"{len(delta['changes'])} cambios trazados")

        old_v = run.state["brief_version"]
        new_v = old_v + 1
        jdump(run.dir / f"delta_v{new_v}.json", delta)
        p = run.tool(HOOKS / "brief_apply_delta_v34.py", "--brief", run.brief_path(old_v), "--delta", run.dir / f"delta_v{new_v}.json", "--out", run.brief_path(new_v))
        run.stage("brief_apply_delta", "PASS" if p.returncode == 0 else "FAIL", (p.stdout + p.stderr).strip()[-300:])
        p = run.tool(HOOKS / "brief_preflight_v34.py", "--brief", run.brief_path(new_v))
        run.stage("brief_preflight", "PASS" if p.returncode == 0 else "FAIL", (p.stdout + p.stderr).strip()[-300:])
        old_r = run.state["prompt_revision"]
        new_r = old_r + 1
        p = run.tool(HOOKS / "prompt_patch_v34.py", "--ast", run.ast_path(old_r), "--old-brief", run.brief_path(old_v), "--new-brief", run.brief_path(new_v),
                     "--delta", run.dir / f"delta_v{new_v}.json", "--out", run.ast_path(new_r))
        run.stage("prompt_patch", "PASS" if p.returncode == 0 else "FAIL", (p.stdout + p.stderr).strip()[-300:])
        p = run.tool(HOOKS / "prompt_revision_gate_v34.py", "--before", run.ast_path(old_r), "--after", run.ast_path(new_r),
                     "--old-brief", run.brief_path(old_v), "--new-brief", run.brief_path(new_v), "--delta", run.dir / f"delta_v{new_v}.json")
        run.stage("prompt_revision_gate", "PASS" if p.returncode == 0 else "FAIL", (p.stdout + p.stderr).strip()[-300:])
        # los hechos vigentes son los del brief nuevo; la procedencia se acumula
        facts["slots"] = jload(run.brief_path(new_v))["facts"]["slots"]
        facts["provenance"].update({k: v for k, v in prov.items()})
        jdump(run.dir / "facts.json", facts)
        run.state["brief_version"] = new_v
        run.state["prompt_revision"] = new_r
        run.save()
        _render(run, facts, jload(run.dir / "case.json"), jload(run.dir / "match.json"), mode="revise")
        return 0
    except Blocked as e:
        if run.state.get("blocked_by") in {"delta_schema", "delta_provenance"}:
            # un delta rechazado no toca el brief: el run conserva su estado anterior
            run.state.update(prior)
            run.save()
            print(f"APD_RUN: DELTA RECHAZADO — {e} (run sigue {prior['status']})")
            return 1
        print(f"APD_RUN: BLOCKED — {e}")
        return 1


def cmd_status(a) -> int:
    run = Run(a.run)
    s = run.state
    print(f"APD_RUN: {s['status']}  brief v{s['brief_version']}  prompt rev {s['prompt_revision']}  sha256 {s.get('prompt_sha256')}")
    for st in s["stages"][-12:]:
        print(f"  {st['at']}  {st['name']:24} {st['status']}  {str(st['detail'])[:100]}")
    return 0 if s["status"] != "BLOCKED" else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new"); p.add_argument("--run", required=True); p.add_argument("--facts", required=True); p.add_argument("--case", required=True); p.set_defaults(fn=cmd_new)
    p = sub.add_parser("audit-pack"); p.add_argument("--run", required=True); p.set_defaults(fn=cmd_audit_pack)
    p = sub.add_parser("ledger"); p.add_argument("--run", required=True); p.add_argument("--evidence", required=True); p.set_defaults(fn=cmd_ledger)
    p = sub.add_parser("revise"); p.add_argument("--run", required=True); p.add_argument("--delta", required=True); p.add_argument("--provenance"); p.set_defaults(fn=cmd_revise)
    p = sub.add_parser("status"); p.add_argument("--run", required=True); p.set_defaults(fn=cmd_status)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
