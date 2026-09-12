#!/usr/bin/env python3
"""Reclasificación de scope 3.5.0: las reglas del pipeline de storyboard salen del caso
de una sola imagen y siguen entrando cuando el caso SÍ es un pipeline.

El riesgo de estrechar scope es el falso NA: una regla real que deja de evaluarse. Por
eso cada regla estrechada se comprueba en los dos sentidos.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RULESET = ROOT / ".claude" / "rules" / "v3" / "build" / "ruleset-3.5.0.json"
BASE = ROOT / ".claude" / "rules" / "v3" / "build" / "ruleset-3.4.0.json"
MATCHER = ROOT / ".claude" / "hooks" / "rule_matcher_v3.py"
CASE = ROOT / "apd" / "runs" / "nfl-tackle-002" / "in" / "case.json"
FX = ROOT / "tests" / "apd" / "fixtures"

# Reglas citadas por su sección, para que el test falle si la tabla deja de cubrirlas.
SHOTS_JSON = "d0bb2d7f4c90"      # Step 1: `shots.json` (required)
BRAND_LOCK = "6b090ff8637a"      # Step 1: `brand-lock.snapshot.md` (required)
QUALITY_BAR = "0ef3b02d41ef"     # Quality bar: Rule 6 sobre cada shot


def match(case: dict, expect_ok: bool = True) -> dict:
    with tempfile.TemporaryDirectory() as td:
        c = Path(td) / "case.json"
        c.write_text(json.dumps(case), encoding="utf-8")
        out = Path(td) / "match.json"
        p = subprocess.run([sys.executable, str(MATCHER), "--ruleset", str(RULESET), "--case", str(c), "--out", str(out)],
                           capture_output=True, text=True, cwd=str(ROOT))
        if expect_ok:
            assert p.returncode == 0, p.stdout + p.stderr
        return json.loads(out.read_text())


def _stage_admite_prompt(when) -> bool:
    """True si la condición no excluye la etapa 'prompt' por sí misma."""
    if not isinstance(when, dict):
        return True
    for leaf in when.get("all", []) + when.get("any", []):
        if isinstance(leaf, dict) and leaf.get("path") == "stage":
            v = leaf.get("value")
            v = v if isinstance(v, list) else [v]
            if leaf.get("op") in ("eq", "in") and "prompt" not in v:
                return False
    return True


def _medio_admite_imagen(when) -> bool:
    if not isinstance(when, dict):
        return True
    for leaf in when.get("all", []) + when.get("any", []):
        if isinstance(leaf, dict) and leaf.get("path") == "media":
            v = leaf.get("value")
            v = v if isinstance(v, list) else [v]
            if leaf.get("op") in ("eq", "in") and "image" not in v:
                return False
    return True


def active_ids(m: dict) -> set:
    return {a if isinstance(a, str) else a["rule_id"] for a in m["active_rules"]}


class ScopeV35(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rs = json.loads(RULESET.read_text(encoding="utf-8"))
        cls.narrowed = {c["rule_id"] for c in cls.rs["scope_narrowing"]["changes"]}
        cls.single = json.loads(CASE.read_text(encoding="utf-8"))

    def test_01_same_rule_count_only_the_conditions_changed(self):
        base = json.loads(BASE.read_text(encoding="utf-8"))
        self.assertEqual(len(base["rules"]), len(self.rs["rules"]))
        self.assertEqual({e["rule"]["id"] for e in base["rules"]}, {e["rule"]["id"] for e in self.rs["rules"]})
        self.assertEqual(self.rs["ruleset_version"], "3.5.0")
        self.assertEqual(self.rs["scope_narrowing"]["authorized_by"], "user")

    def test_02_single_image_case_drops_the_storyboard_pipeline(self):
        ids = active_ids(match(self.single))
        for rid in (SHOTS_JSON, BRAND_LOCK, QUALITY_BAR):
            self.assertNotIn(rid, ids, f"{rid} no debe aplicar a un brief de una sola imagen")
        self.assertEqual(ids & self.narrowed, set())

    def test_03_pipeline_case_keeps_every_narrowed_rule_reachable(self):
        c = json.loads(json.dumps(self.single))
        c["pipeline_track"] = "STANDARD"
        c["shot_id"] = "SH01"
        c["sequence"]["multi_shot"] = True
        c["sequence"]["shot_count"] = 6
        c["brand"] = {"mode": "locked", "brand_lock_ref": "brand-lock.snapshot.md"}
        c["text"] = {"mode": "in_image", "readable_text_required": True}
        ids = active_ids(match(c))
        for rid in (SHOTS_JSON, BRAND_LOCK, QUALITY_BAR):
            self.assertIn(rid, ids, f"{rid} debe volver a aplicar cuando el caso es un pipeline")
        # El grupo "Failure 1. The AI look" se estrechó por modelo, no por pipeline:
        # lente y diafragma numéricos no aplican a Nano Banana (APD §6.2). Se comprueba
        # aparte, con un caso de GPT Image, para que nada quede inalcanzable.
        por_modelo = {c["rule_id"] for c in self.rs["scope_narrowing"]["changes"]
                      if c["condition"]["path"] == "generator.family"}
        # Reglas cuya etapa o medio propios no son los de este caso (guion, escena,
        # shot, video) no pueden estar activas aquí: eso ya era así antes de estrechar.
        otra_etapa = {e["rule"]["id"] for e in self.rs["rules"]
                      if e["rule"]["id"] in self.narrowed
                      and not (_stage_admite_prompt(e["metadata"].get("when"))
                               and _medio_admite_imagen(e["metadata"].get("when")))}
        faltan = self.narrowed - ids - por_modelo - otra_etapa
        self.assertEqual(faltan, set(), f"{len(faltan)} reglas estrechadas quedaron inalcanzables: {sorted(faltan)[:5]}")
        c["generator"] = {"family": "gpt_image", "model": "gpt-image-2", "adapter_version": "kb-v3.4.0"}
        gpt_ids = active_ids(match(c))
        self.assertEqual(por_modelo - gpt_ids, set(), "las reglas de lente/film stock deben aplicar a GPT Image")

    def test_04_unknown_pipeline_track_does_not_become_na(self):
        c = json.loads(json.dumps(self.single))
        c["pipeline_track"] = "UNKNOWN"
        m = match(c, expect_ok=False)
        self.assertGreater(m["counts"]["unresolved"], 0, "UNKNOWN debe dar UNRESOLVED, nunca NA silencioso")
        self.assertEqual(m["status"], "FAIL")  # fail-closed: no se evalúa un caso incompleto


if __name__ == "__main__":
    unittest.main(verbosity=2)
