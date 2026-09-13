#!/usr/bin/env python3
"""Veredictos aprendidos: un caso nuevo hereda lo ya juzgado cuando nada de lo que ese
juicio miraba cambió, y una discrepancia en la muestra de control borra el aprendizaje.

Lo que este archivo protege es el único riesgo real de la caché: aprobar por herencia
algo que en realidad cambió.
"""
import json, os, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APD = ROOT / "apd" / "apd_run.py"
FX = ROOT / "tests" / "apd" / "fixtures"


class AuditCache(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.base = Path(self.td.name)
        self.cache = self.base / "verdicts.jsonl"
        self.env = {**os.environ, "APD_CACHE": str(self.cache)}

    def tearDown(self):
        self.td.cleanup()

    def run_apd(self, *args, ok=True):
        p = subprocess.run([sys.executable, str(APD), *map(str, args)], capture_output=True, text=True,
                           cwd=str(ROOT), env=self.env)
        if ok:
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        return p

    def new_run(self, name, facts=None):
        d = self.base / name
        f = self.base / f"{name}_facts.json"
        f.write_text(json.dumps(facts or json.loads((FX / "gpt_facts.json").read_text())), encoding="utf-8")
        self.run_apd("new", "--run", d, "--facts", f, "--case", FX / "gpt_case.json", "--brief", FX / "gpt_brief.txt")
        return d

    def audit(self, d, status="PASS", deps=("prompt.text",)):
        """Firma como auditor lo que el pack pida en esta vuelta."""
        self.run_apd("audit-pack", "--run", d)
        req = json.loads((d / "audit_request.json").read_text())
        entries = {r["rule_id"]: {"status": status, "by": "auditor", "reason": "prueba", "depends_on": list(deps)}
                   for t in req["tandas"] for r in t["rules"]}
        ev = d / "ev.json"
        ev.write_text(json.dumps({"nonce": req["nonce"], "prompt_sha256": req["prompt_sha256"], "entries": entries}), encoding="utf-8")
        p = self.run_apd("ledger", "--run", d, "--evidence", ev, ok=False)
        return req, p

    def test_01_first_run_teaches_and_second_reuses(self):
        d1 = self.new_run("r1")
        req1, p1 = self.audit(d1, deps=("prompt.text",))
        self.assertIn("DELIVERED", p1.stdout, p1.stdout)
        n1 = sum(len(t["rules"]) for t in req1["tandas"])
        self.assertTrue(self.cache.exists(), "la primera auditoría no dejó nada aprendido")

        d2 = self.new_run("r2")            # mismo caso, mismos hechos, prompt idéntico
        self.run_apd("audit-pack", "--run", d2)
        req2 = json.loads((d2 / "audit_request.json").read_text())
        n2 = sum(len(t["rules"]) for t in req2["tandas"])
        hits = json.loads((d2 / "audit_cache_hits.json").read_text())
        self.assertGreater(len(hits["reusados"]), 0, "no reutilizó nada")
        self.assertLess(n2, n1, f"el segundo caso mandó {n2} reglas al auditor y el primero {n1}")
        self.assertEqual(len(hits["muestra_de_control"]), n2, "todo lo que va al auditor debe ser la muestra de control")

    def test_02_changing_what_the_verdict_looked_at_forces_a_new_audit(self):
        d1 = self.new_run("r1")
        self.audit(d1, deps=("slots.scene.time",))
        facts = json.loads((FX / "gpt_facts.json").read_text())
        facts["slots"]["scene"]["time"] = "late afternoon"
        facts["provenance"]["slots.scene.time"] = {"source": "user", "ref": "morning"}
        d2 = self.new_run("r2", facts=facts)
        self.run_apd("audit-pack", "--run", d2)
        hits = json.loads((d2 / "audit_cache_hits.json").read_text())
        self.assertEqual(hits["reusados"], {}, "heredó veredictos aunque cambió el slot del que dependían")

    def test_03_a_disagreement_in_the_control_sample_blocks_and_purges(self):
        d1 = self.new_run("r1")
        self.audit(d1, deps=("prompt.text",))
        aprendidas = len(self.cache.read_text().splitlines())
        d2 = self.new_run("r2")
        _, p2 = self.audit(d2, status="FAIL")     # el auditor contradice a la caché
        self.assertIn("cache_control", p2.stdout)
        self.assertIn("BLOCKED", p2.stdout)
        self.assertFalse((d2 / "DELIVERABLE.txt").exists())
        quedan = len(self.cache.read_text().splitlines()) if self.cache.exists() else 0
        self.assertLess(quedan, aprendidas, "no purgó el aprendizaje de las reglas en discrepancia")

    def test_04_a_fail_is_never_inherited(self):
        d1 = self.new_run("r1")
        self.audit(d1, status="FAIL")
        self.assertFalse(self.cache.exists() and self.cache.read_text().strip(),
                         "un FAIL no puede quedar guardado como veredicto heredable")


if __name__ == "__main__":
    unittest.main(verbosity=2)
