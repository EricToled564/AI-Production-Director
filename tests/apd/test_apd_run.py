#!/usr/bin/env python3
"""apd_run.py + gate_apd_delivery.py: el prompt sólo sale del proceso, nunca de la mano."""
import copy, json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APD = ROOT / "apd" / "apd_run.py"
GATE = ROOT / ".claude" / "hooks" / "gate_apd_delivery.py"
EX = ROOT / "examples" / "apd" / "tennis-gpt-image-2"


def run(*args, ok=None):
    p = subprocess.run([sys.executable, str(APD), *map(str, args)], capture_output=True, text=True, cwd=str(ROOT))
    if ok is not None and (p.returncode == 0) != ok:
        raise AssertionError(f"exit={p.returncode}\n{p.stdout}\n{p.stderr}")
    return p


def stub_evidence(run_dir: Path) -> Path:
    """Evidencia con la forma exigida al auditor. Prueba la mecánica del ledger, no audita."""
    req = json.loads((run_dir / "audit_request.json").read_text())
    entries = {r["rule_id"]: {"status": "PASS", "by": "auditor", "reason": "stub de prueba"} for t in req["tandas"] for r in t["rules"]}
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

    def new(self, facts=None, case=None):
        f = self.runs / "facts.json"; c = self.runs / "case.json"
        f.write_text(json.dumps(facts or json.loads((EX / "facts.json").read_text())))
        c.write_text(json.dumps(case or json.loads((EX / "case.json").read_text())))
        return run("new", "--run", self.run, "--facts", f, "--case", c)

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
        facts = json.loads((EX / "facts.json").read_text()); del facts["provenance"]["slots.subject.action"]
        p = self.new(facts)
        self.assertNotEqual(p.returncode, 0); self.assertIn("slots.subject.action: sin procedencia", p.stdout)

    def test_03_skill_ref_must_exist(self):
        facts = json.loads((EX / "facts.json").read_text())
        facts["provenance"]["slots.opening"] = {"source": "skill", "ref": "image/SKILL.md:9999"}
        p = self.new(facts)
        self.assertNotEqual(p.returncode, 0); self.assertIn("fuera de rango", p.stdout)

    def test_04_case_facts_mismatch_blocks(self):
        case = json.loads((EX / "case.json").read_text()); case["deliverable"]["aspect_ratio"] = "16:9"
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
        rid = next(iter(ev["entries"])); ev["entries"][rid] = {"status": "FAIL", "by": "auditor", "reason": "ausente"}
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
        edited = prompt.replace("midday", "noon")
        self.assertEqual(hook(f"gpt-image-2\n\n```\n{edited}\n```\n", self.runs), 2)
        self.assertEqual(hook("```\nCreate a photo of a cat.\n```\nnano banana", self.runs), 2)
        self.assertEqual(hook("kling\n```\nCreate a slow push-in on the cat.\n```", self.runs), 0)

    def test_08_revise_changes_only_the_delta_and_invalidates_delivery(self):
        self.deliver()
        h = json.loads((self.run / "brief_v1.lock.json").read_text())["brief_hash"]
        (self.runs / "d.json").write_text(json.dumps({"schema_version": "1.1", "base_brief_hash": h, "authorized_by": "user",
                                                     "reason": "Eric: tarde", "changes": [{"path": "slots.scene.time", "op": "replace", "value": "late afternoon"}]}))
        (self.runs / "p.json").write_text(json.dumps({"slots.scene.time": {"source": "user", "ref": "Eric: tarde"}}))
        run("revise", "--run", self.run, "--delta", self.runs / "d.json", "--provenance", self.runs / "p.json", ok=True)
        a = (self.run / "prompt_v1.txt").read_text(); b = (self.run / "prompt_v2.txt").read_text()
        self.assertEqual(a.replace("midday", "late afternoon"), b)
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

    def test_10_word_ceiling_comes_from_capabilities(self):
        facts = json.loads((EX / "facts.json").read_text())
        facts["slots"]["constraints"] += "; " + "no extra element" * 30
        p = self.new(facts)
        self.assertNotEqual(p.returncode, 0); self.assertIn("word_ceiling", p.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
