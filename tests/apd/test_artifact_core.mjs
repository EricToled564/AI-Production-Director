#!/usr/bin/env node
// Paridad del núcleo JS del artefacto con apd_run.py: mismo prompt, mismo conteo de
// reglas activas, mismos gates, mismo flujo ledger → DELIVERED → revise.
import { readFileSync, mkdtempSync, rmSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import vm from "node:vm";
import assert from "node:assert/strict";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..");
const ctx = { window: undefined, crypto: globalThis.crypto, TextEncoder, require: (await import("node:module")).createRequire(import.meta.url), console };
ctx.globalThis = ctx;
vm.createContext(ctx);
vm.runInContext(readFileSync(join(ROOT, "apd/artifact/data.js"), "utf8").replace(/^window\./, "globalThis."), ctx);
vm.runInContext(readFileSync(join(ROOT, "apd/artifact/apd_core.js"), "utf8"), ctx);
const { APD, APD_DATA: D } = ctx;

const FX = join(ROOT, "tests", "apd", "fixtures");
const EXAMPLES = Object.fromEntries(["gpt", "nb", "t1", "edit"].map((k) => [k, { facts: JSON.parse(readFileSync(join(FX, `${k}_facts.json`), "utf8")), case: JSON.parse(readFileSync(join(FX, `${k}_case.json`), "utf8")), brief: readFileSync(join(FX, `${k}_brief.txt`), "utf8") }]));
function pythonRun(example) {
  const dir = mkdtempSync(join(tmpdir(), "apd-"));
  const p = spawnSync("python3", ["apd/apd_run.py", "new", "--run", join(dir, "r"), "--facts", join(FX, `${example}_facts.json`), "--case", join(FX, `${example}_case.json`), "--brief", join(FX, `${example}_brief.txt`), ...(example === "gpt" ? ["--strict"] : [])], { cwd: ROOT, encoding: "utf8" });
  assert.equal(p.status, 0, p.stdout + p.stderr);
  const prompt = readFileSync(join(dir, "r", "prompt_v1.txt"), "utf8");
  const match = JSON.parse(readFileSync(join(dir, "r", "match.json"), "utf8"));
  const pending = JSON.parse(readFileSync(join(dir, "r", "audit_pending.json"), "utf8"));
  rmSync(dir, { recursive: true, force: true });
  return { prompt, active: match.counts.active, pending: pending.length };
}

function stubEvidence(req) {
  const entries = {};
  for (const t of req.tandas) for (const r of t.rules) entries[r.rule_id] = { status: "PASS", by: "auditor", reason: "stub de prueba", depends_on: ["prompt.text"] };
  return { nonce: req.nonce, prompt_sha256: req.prompt_sha256, entries };
}

let n = 0;
for (const [name, ex] of Object.entries(EXAMPLES)) {
  const py = pythonRun(name);
  const run = await APD.run(D, { ...ex, strict: name === "gpt" });
  assert.equal(run.status, "AWAITING_AUDIT", `${name}: ${JSON.stringify(run.stages.at(-1))}`);
  if (name === "gpt") assert.ok(run.stages.some((s) => s.name === "facts_strict" && s.status === "PASS"));
  assert.equal(run.prompt, py.prompt, `${name}: el prompt JS difiere del de Python`);
  assert.equal(run.match.counts.active, py.active, `${name}: reglas activas`);
  assert.equal(run.audit_pending.length, py.pending, `${name}: pendientes para el auditor`);
  console.log(`ok  ${name}: prompt idéntico, ${py.active} activas, ${py.pending} al auditor`); n++;
}

// ledger → DELIVERED → revise sólo cambia el delta → deltas ilegítimos rechazados sin tocar el run
{
  const ex = EXAMPLES.gpt;
  const run = await APD.run(D, ex);
  const req = APD.auditPack(D, run);
  const bad = stubEvidence(req); delete bad.entries[Object.keys(bad.entries)[0]];
  await APD.ledger(D, run, bad);
  assert.equal(run.status, "BLOCKED"); assert.equal(run.blocked_by, "auditor_evidence");
  await APD.ledger(D, run, stubEvidence(req));
  assert.equal(run.status, "DELIVERED"); assert.ok(run.deliverable.includes("Prompt:\n" + run.prompt.trimEnd()));
  const h = run.briefs[0].brief_hash;
  await APD.revise(D, run, { schema_version: "1.1", base_brief_hash: h, authorized_by: "user", reason: "Eric: late afternoon", changes: [{ path: "slots.scene.time", op: "replace", value: "late afternoon" }] }, { "slots.scene.time": { source: "user", ref: "late afternoon" } });
  assert.equal(run.status, "AWAITING_AUDIT");
  assert.equal(run.prompts[0].replace("morning", "late afternoon"), run.prompts[1]);
  assert.equal(run.deliverable, undefined);
  const req2 = APD.auditPack(D, run); await APD.ledger(D, run, stubEvidence(req2)); assert.equal(run.status, "DELIVERED");
  const h2 = run.briefs[1].brief_hash;
  await APD.revise(D, run, { schema_version: "1.1", base_brief_hash: h2, authorized_by: "assistant", reason: "x", changes: [{ path: "slots.scene.time", op: "replace", value: "dusk" }] }, {});
  assert.equal(run.status, "DELIVERED"); assert.match(run.delta_rejected, /authorized_by/);
  await APD.revise(D, run, { schema_version: "1.1", base_brief_hash: h2, authorized_by: "user", reason: "x", changes: [{ path: "model", op: "replace", value: "nano-banana-pro" }] }, {});
  assert.equal(run.status, "DELIVERED"); assert.match(run.delta_rejected, /slots\.\*/);
  console.log("ok  ledger / revise / deltas rechazados"); n++;
}
// gate literal: fragmento atribuido al skill que no está ahí; cita a Eric que no está en el brief; modo estricto
{
  const ex = JSON.parse(JSON.stringify(EXAMPLES.gpt));
  ex.facts.slots.details.lens_feel = "hands hidden in the foam"; ex.facts.provenance["slots.details.lens_feel"] = { source: "skill", ref: "image/references/creative-direction.md:50" };
  let run = await APD.run(D, ex); assert.equal(run.blocked_by, "facts_literal"); assert.match(run.stages.at(-1).detail, /hands hidden in the foam/);
  const ex2 = JSON.parse(JSON.stringify(EXAMPLES.gpt));
  ex2.facts.provenance["slots.scene.time"] = { source: "user", ref: "Eric pidió que fuera de noche" };
  run = await APD.run(D, ex2); assert.equal(run.blocked_by, "facts_literal"); assert.match(run.stages.at(-1).detail, /no está en el brief/);
  const ex3 = JSON.parse(JSON.stringify(EXAMPLES.gpt)); ex3.strict = true; ex3.brief += "The woman wears a red cap.\n";
  run = await APD.run(D, ex3); assert.equal(run.blocked_by, "facts_strict"); assert.match(run.stages.at(-1).detail, /omitida/);
  console.log("ok  gate literal / modo estricto"); n++;
}
// hoja sin procedencia, ref de skill fuera de rango, tope de palabras
{
  const ex = JSON.parse(JSON.stringify(EXAMPLES.gpt));
  delete ex.facts.provenance["slots.subject.action"];
  let run = await APD.run(D, ex); assert.equal(run.blocked_by, "facts_provenance");
  ex.facts.provenance["slots.subject.action"] = { source: "skill", ref: "image/SKILL.md:9999" };
  run = await APD.run(D, ex); assert.match(run.stages.at(-1).detail, /fuera de rango/);
  ex.facts.provenance["slots.subject.action"] = EXAMPLES.gpt.facts.provenance["slots.subject.action"];
  ex.facts.slots.constraints += "; " + "no extra element ".repeat(90);
  run = await APD.run(D, ex); assert.equal(run.blocked_by, "prompt_gates"); assert.match(run.stages.at(-1).detail, /word/);
  console.log("ok  procedencia / tope de palabras"); n++;
}
console.log(`\n${n} bloques de prueba OK`);
