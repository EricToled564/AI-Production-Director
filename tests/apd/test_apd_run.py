#!/usr/bin/env python3
"""apd_run.py + gate_apd_delivery.py: el prompt sólo sale del proceso, nunca de la mano."""
import copy, json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APD = ROOT / "apd" / "apd_run.py"
GATE = ROOT / ".claude" / "hooks" / "gate_apd_delivery.py"
FX = ROOT / "tests" / "apd" / "fixtures"
# Ninguna prueba toca el aprendizaje real ni la librería de prompts probados.
_SANDBOX = tempfile.mkdtemp(prefix="apd-test-")
AISLADO = {**os.environ, "APD_CACHE": _SANDBOX + "/verdicts.jsonl", "APD_LIBRARY": _SANDBOX + "/library.jsonl"}
sys.path.insert(0, str(ROOT / "apd"))


def run(*args, ok=None):
    p = subprocess.run([sys.executable, str(APD), *map(str, args)], capture_output=True, text=True, cwd=str(ROOT), env=AISLADO)
    if ok is not None and (p.returncode == 0) != ok:
        raise AssertionError(f"exit={p.returncode}\n{p.stdout}\n{p.stderr}")
    return p


def stub_evidence(run_dir: Path) -> Path:
    """Evidencia con la forma exigida al auditor. Prueba la mecánica del ledger, no audita."""
    req = json.loads((run_dir / "audit_request.json").read_text())
    entries = {r["rule_id"]: {"status": "PASS", "by": "auditor", "reason": "stub de prueba", "depends_on": ["prompt.text"]} for t in req["tandas"] for r in t["rules"]}
    p = run_dir / "evidence.json"
    p.write_text(json.dumps({"nonce": req["nonce"], "prompt_sha256": req["prompt_sha256"], "entries": entries}))
    return p


def hook(message: str, runs_dir: Path) -> int:
    env = {**os.environ, "CLAUDE_PROJECT_DIR": str(ROOT), "APD_RUNS_DIR": str(runs_dir)}
    p = subprocess.run([sys.executable, str(GATE)], input=json.dumps({"last_assistant_message": message, "session_id": "t"}),
                       capture_output=True, text=True, env=env)
    return p.returncode


class ApdRun(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.runs = Path(self.td.name)
        self.run = self.runs / "r1"

    def tearDown(self):
        self.td.cleanup()

    def new(self, facts=None, case=None, brief=None, strict=False):
        f = self.runs / "facts.json"; c = self.runs / "case.json"; b = self.runs / "brief.txt"
        f.write_text(json.dumps(facts or json.loads((FX / "gpt_facts.json").read_text())))
        c.write_text(json.dumps(case or json.loads((FX / "gpt_case.json").read_text())))
        b.write_text(brief if brief is not None else (FX / "gpt_brief.txt").read_text())
        return run("new", "--run", self.run, "--facts", f, "--case", c, "--brief", b, *(["--strict"] if strict else []))

    def deliver(self):
        self.new()
        run("audit-pack", "--run", self.run, ok=True)
        run("ledger", "--run", self.run, "--evidence", stub_evidence(self.run), ok=True)
        return json.loads((self.run / "run.json").read_text())

    def test_01_example_reaches_awaiting_audit(self):
        p = self.new()
        self.assertEqual(p.returncode, 0, p.stdout)
        self.assertIn("AWAITING_AUDIT", p.stdout)
        self.assertTrue((self.run / "prompt_v1.txt").read_text().startswith("Create "))
        self.assertFalse((self.run / "DELIVERABLE.txt").exists())

    def test_02_leaf_without_provenance_blocks(self):
        facts = json.loads((FX / "gpt_facts.json").read_text()); del facts["provenance"]["slots.subject.action"]
        p = self.new(facts)
        self.assertNotEqual(p.returncode, 0); self.assertIn("slots.subject.action: sin procedencia", p.stdout)

    def test_03_skill_ref_must_exist(self):
        facts = json.loads((FX / "gpt_facts.json").read_text())
        facts["provenance"]["slots.opening"] = {"source": "skill", "ref": "image/SKILL.md:9999"}
        p = self.new(facts)
        self.assertNotEqual(p.returncode, 0); self.assertIn("fuera de rango", p.stdout)

    def test_04_case_facts_mismatch_blocks(self):
        case = json.loads((FX / "gpt_case.json").read_text()); case["deliverable"]["aspect_ratio"] = "16:9"
        p = self.new(case=case)
        self.assertNotEqual(p.returncode, 0); self.assertIn("aspect_ratio", p.stdout)

    def test_05_ledger_rejects_incomplete_or_self_signed_evidence(self):
        self.new(); run("audit-pack", "--run", self.run, ok=True)
        ev = json.loads(stub_evidence(self.run).read_text())
        bad = copy.deepcopy(ev); bad["entries"].popitem()
        (self.run / "bad.json").write_text(json.dumps(bad))
        p = run("ledger", "--run", self.run, "--evidence", self.run / "bad.json", ok=False)
        self.assertIn("sin entrada del auditor", p.stdout)
        bad = copy.deepcopy(ev)
        rid = next(iter(bad["entries"])); bad["entries"][rid]["by"] = "assistant"
        (self.run / "bad2.json").write_text(json.dumps(bad))
        p = run("ledger", "--run", self.run, "--evidence", self.run / "bad2.json", ok=False)
        self.assertIn("by debe ser 'auditor'", p.stdout)
        bad = copy.deepcopy(ev); bad["nonce"] = "0" * 16
        (self.run / "bad3.json").write_text(json.dumps(bad))
        p = run("ledger", "--run", self.run, "--evidence", self.run / "bad3.json", ok=False)
        self.assertIn("nonce", p.stdout)
        self.assertFalse((self.run / "DELIVERABLE.txt").exists())

    def test_06_one_fail_means_no_delivery(self):
        self.new(); run("audit-pack", "--run", self.run, ok=True)
        ev = json.loads(stub_evidence(self.run).read_text())
        rid = next(iter(ev["entries"])); ev["entries"][rid] = {"status": "FAIL", "by": "auditor", "reason": "ausente", "depends_on": ["prompt.text"]}
        (self.run / "ev.json").write_text(json.dumps(ev))
        p = run("ledger", "--run", self.run, "--evidence", self.run / "ev.json", ok=False)
        self.assertIn("fail 1", p.stdout); self.assertFalse((self.run / "DELIVERABLE.txt").exists())

    def test_07_delivered_and_gate_accepts_only_the_deliverable(self):
        st = self.deliver()
        self.assertEqual(st["status"], "DELIVERED")
        full = (self.run / "DELIVERABLE.txt").read_text()
        prompt = full.split("Prompt:\n", 1)[1].split("\nNotes:\n", 1)[0]
        self.assertEqual(hook(f"SKILL: a.md\nRIESGOS: b\nTÉCNICA: c\n\n```\n{full}```\n", self.runs), 0)
        self.assertEqual(hook(f"gpt-image-2\n\n```\n{prompt}\n```\n", self.runs), 0)
        edited = prompt.replace("morning", "noon")
        self.assertEqual(hook(f"gpt-image-2\n\n```\n{edited}\n```\n", self.runs), 2)
        self.assertEqual(hook("```\nCreate a photo of a cat.\n```\nnano banana", self.runs), 2)
        self.assertEqual(hook("kling\n```\nCreate a slow push-in on the cat.\n```", self.runs), 0)

    def test_08_revise_changes_only_the_delta_and_invalidates_delivery(self):
        self.deliver()
        h = json.loads((self.run / "brief_v1.lock.json").read_text())["brief_hash"]
        (self.runs / "d.json").write_text(json.dumps({"schema_version": "1.1", "base_brief_hash": h, "authorized_by": "user",
                                                     "reason": "Eric: late afternoon", "changes": [{"path": "slots.scene.time", "op": "replace", "value": "late afternoon"}]}))
        (self.runs / "p.json").write_text(json.dumps({"slots.scene.time": {"source": "user", "ref": "late afternoon"}}))
        run("revise", "--run", self.run, "--delta", self.runs / "d.json", "--provenance", self.runs / "p.json", ok=True)
        a = (self.run / "prompt_v1.txt").read_text(); b = (self.run / "prompt_v2.txt").read_text()
        self.assertEqual(a.replace("morning", "late afternoon"), b)
        self.assertFalse((self.run / "DELIVERABLE.txt").exists())
        self.assertEqual(json.loads((self.run / "run.json").read_text())["status"], "AWAITING_AUDIT")

    def test_09_delta_outside_slots_or_not_user_is_refused_without_touching_run(self):
        self.deliver()
        h = json.loads((self.run / "brief_v1.lock.json").read_text())["brief_hash"]
        for d in ({"schema_version": "1.1", "base_brief_hash": h, "authorized_by": "user", "reason": "x", "changes": [{"path": "model", "op": "replace", "value": "nano-banana-pro"}]},
                  {"schema_version": "1.1", "base_brief_hash": h, "authorized_by": "assistant", "reason": "x", "changes": [{"path": "slots.scene.time", "op": "replace", "value": "dusk"}]}):
            (self.runs / "d.json").write_text(json.dumps(d))
            (self.runs / "p.json").write_text(json.dumps({"slots.scene.time": {"source": "user", "ref": "Eric: dusk"}}))
            p = run("revise", "--run", self.run, "--delta", self.runs / "d.json", "--provenance", self.runs / "p.json", ok=False)
            self.assertIn("DELTA RECHAZADO", p.stdout)
            self.assertEqual(json.loads((self.run / "run.json").read_text())["status"], "DELIVERED")
            self.assertTrue((self.run / "DELIVERABLE.txt").exists())

    def test_11_skill_fragment_must_be_literal(self):
        facts = json.loads((FX / "gpt_facts.json").read_text())
        facts["slots"]["details"]["lens_feel"] = "hands hidden in the foam"
        facts["provenance"]["slots.details.lens_feel"] = {"source": "skill", "ref": "image/references/creative-direction.md:50"}
        p = self.new(facts)
        self.assertNotEqual(p.returncode, 0); self.assertIn("no es literal de las líneas citadas", p.stdout); self.assertIn("hands hidden in the foam", p.stdout)

    def test_12_user_quote_must_exist_in_brief(self):
        facts = json.loads((FX / "gpt_facts.json").read_text())
        facts["provenance"]["slots.scene.time"] = {"source": "user", "ref": "Eric pidió que fuera de noche"}
        p = self.new(facts)
        self.assertNotEqual(p.returncode, 0); self.assertIn("no está en el brief", p.stdout)

    def test_13_strict_mode_blocks_invented_fragment_and_omitted_sentence(self):
        p = self.new(strict=True); self.assertEqual(p.returncode, 0, p.stdout); self.assertIn("facts_strict             PASS", p.stdout)
        import shutil; shutil.rmtree(self.run)
        facts = json.loads((FX / "gpt_facts.json").read_text())
        facts["slots"]["scene"]["weather"] = "overcast, soft even light, hands hidden in the foam"
        p = self.new(facts, strict=True)
        self.assertNotEqual(p.returncode, 0); self.assertIn("no es literal del brief ni del skill", p.stdout)
        shutil.rmtree(self.run)
        brief = (FX / "gpt_brief.txt").read_text() + "The woman wears a red cap.\n"
        p = self.new(brief=brief, strict=True)
        self.assertNotEqual(p.returncode, 0); self.assertIn("frase del brief omitida", p.stdout)

    def test_10_padding_is_blocked_and_required_content_may_exceed_the_ceiling(self):
        """Política de Eric (2026-09-13): todas las reglas del caso van en el prompt, por
        encima del tope, y recortar lo decide él. El tope informa y no bloquea; lo que
        bloquea es el relleno. Y el conteo va sólo sobre MAIN, sin el bloque Negative."""
        facts = json.loads((FX / "gpt_facts.json").read_text())
        facts["slots"]["constraints"] += "; " + "no extra element " * 90
        p = self.new(facts)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("minimalidad", p.stdout)
        self.assertIn("no extra element", p.stdout)
        import shutil; shutil.rmtree(self.run)
        facts = json.loads((FX / "gpt_facts.json").read_text())
        facts["slots"]["constraints"] += "; " + ", ".join(f"constraint number {i} is distinct" for i in range(40))
        p = self.new(facts)
        self.assertEqual(p.returncode, 0, p.stdout)
        gates = json.loads((self.run / "gates.json").read_text())["structural"]
        wc = gates["word_count"]
        # Se pasa del tope y NO bloquea: el número queda escrito y la decisión es de Eric.
        self.assertEqual(wc["status"], "PASS"); self.assertEqual(wc["decide"], "user")
        self.assertIn("sobre el tope", wc["detail"]); self.assertIn("decisión suya", wc["detail"])

    def test_11_the_count_covers_main_only(self):
        """El bloque Negative no cuenta (aurora-prompt-linter/SKILL.md:114 y la decisión de
        Eric). Un negativo largo no puede empujar el conteo."""
        import apd_run
        prompt = "Create a scene with six words here.\n\nNegative: " + "no unrelated thing, " * 30
        self.assertEqual(apd_run.word_count(prompt), 7)
        self.assertEqual(apd_run.main_block(prompt).strip(), "Create a scene with six words here.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
