#!/usr/bin/env python3
"""Variantes del AST: Nano Banana Pro, maestro de rostro T1 y edición T5."""
import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APD = ROOT / "apd" / "apd_run.py"
GATE_IMAGE = ROOT / ".claude" / "hooks" / "gate_image.py"
FX = ROOT / "tests" / "apd" / "fixtures"
# Ninguna prueba toca el aprendizaje real ni la librería de prompts probados.
_SANDBOX = tempfile.mkdtemp(prefix="apd-test-")
AISLADO = {**os.environ, "APD_CACHE": _SANDBOX + "/verdicts.jsonl", "APD_LIBRARY": _SANDBOX + "/library.jsonl"}


def run(*args):
    return subprocess.run([sys.executable, str(APD), *map(str, args)], capture_output=True, text=True, cwd=str(ROOT), env=AISLADO)


class Variants(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.runs = Path(self.td.name)

    def tearDown(self):
        self.td.cleanup()

    def new(self, example, facts=None, case=None):
        f = self.runs / "facts.json"; c = self.runs / "case.json"
        f.write_text(json.dumps(facts or json.loads((FX / f"{example}_facts.json").read_text())))
        c.write_text(json.dumps(case or json.loads((FX / f"{example}_case.json").read_text())))
        r = self.runs / example
        return run("new", "--run", r, "--facts", f, "--case", c, "--brief", FX / f"{example}_brief.txt"), r

    def test_01_nano_banana_renders_skill_order_and_format(self):
        p, r = self.new("nb")
        self.assertEqual(p.returncode, 0, p.stdout)
        t = (r / "prompt_v1.txt").read_text()
        self.assertTrue(t.startswith("Create "))
        # El cuerpo descriptivo cierra con Format (nano-banana.md:20); el bloque
        # Negative que exige aurora-prompt-linter (references/README.md:95) va detrás,
        # porque el linter parte main/negative en la etiqueta "Negative:".
        main, _, negative = t.rstrip().partition("\nNegative: ")
        self.assertTrue(main.rstrip().endswith("Format: 16:9."))
        self.assertTrue(negative.strip())
        self.assertNotIn("Scene:", t)
        params = json.loads((r / "prompt_v1.ast.json").read_text())["parameters"]
        self.assertEqual(params["aspectRatio"], "16:9"); self.assertNotIn("size", params)
        self.assertIn("nb_no_numeric_lens", json.loads((r / "gates.json").read_text())["lexical"])

    def test_02_nano_numeric_lens_blocks(self):
        facts = json.loads((FX / "nb_facts.json").read_text())
        facts["slots"]["composition"] = "85mm f/2.8 ISO 400 " + facts["slots"]["composition"]
        p, _ = self.new("nb", facts=facts)
        self.assertNotEqual(p.returncode, 0); self.assertIn("nb_no_numeric_lens", p.stdout)

    def test_03_nano_format_must_match_size(self):
        facts = json.loads((FX / "nb_facts.json").read_text()); facts["format"] = "4:3"
        p, _ = self.new("nb", facts=facts)
        self.assertNotEqual(p.returncode, 0); self.assertIn("facts.format", p.stdout)

    def test_04_t1_appends_the_four_canonical_blocks(self):
        p, r = self.new("t1")
        self.assertEqual(p.returncode, 0, p.stdout)
        t = (r / "prompt_v1.txt").read_text()
        for needle in ("Hard grazing light with no fill", "Concrete documentary skin detail", "Kodak Tri-X", "No beauty retouching"):
            self.assertIn(needle, t)
        audit = json.loads((r / "audit_gi2.json").read_text())
        self.assertEqual(audit["status"], "PASS")
        ast = json.loads((r / "prompt_v1.ast.json").read_text())
        fixed = [s for b in ast["blocks"] for s in b["segments"] if s["kind"] == "rule_text"]
        self.assertEqual({s["id"] for s in fixed}, {"light_hard", "skin_doc", "usecase_doc", "clean_doc"})
        self.assertTrue(all(s["source_rules"] for s in fixed))

    def test_05_edit_uses_change_preserve_constraints_and_passes_gate_image(self):
        p, r = self.new("edit")
        self.assertEqual(p.returncode, 0, p.stdout)
        t = (r / "prompt_v1.txt").read_text()
        self.assertEqual([l.split(":")[0] for l in t.split("\n\n")], ["Change", "Preserve", "Constraints", "Negative"])
        env = {**os.environ, "CLAUDE_PROJECT_DIR": str(ROOT)}
        g = subprocess.run([sys.executable, str(GATE_IMAGE)], input=json.dumps({"last_assistant_message": f"gpt-image-2\n\n```\n{t}```\n", "session_id": "t"}),
                           capture_output=True, text=True, env=env)
        self.assertEqual(g.returncode, 0, g.stderr)

    def test_06_edit_requires_t5_case_and_reference(self):
        facts = json.loads((FX / "edit_facts.json").read_text())
        case = json.loads((FX / "edit_case.json").read_text()); case["base_type"] = "T3"; case["operation"] = "text_to_image"
        p, _ = self.new("edit", facts=facts, case=case)
        self.assertNotEqual(p.returncode, 0); self.assertIn("operation=image_edit", p.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
