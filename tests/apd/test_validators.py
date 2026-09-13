#!/usr/bin/env python3
"""El registro de validadores: cada uno demuestra que distingue, y uno roto se aparta.

Lo que este archivo protege es el riesgo de mecanizar: un validador que aprueba lo que
debería fallar no duda nunca, a diferencia de un auditor.
"""
import json, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".claude" / "hooks"))
import rule_validators as rv  # noqa: E402

REG = ROOT / ".claude" / "rules" / "v3" / "validators" / "image.jsonl"


def entradas():
    return [json.loads(l) for l in REG.read_text(encoding="utf-8").splitlines() if l.strip()]


class Validadores(unittest.TestCase):
    def test_01_cada_validador_distingue(self):
        for e in entradas():
            ok, why = rv.selftest(e)
            self.assertTrue(ok, f"{e['rule_id']} ({e['source']}): {why}")

    def test_02_sin_los_dos_casos_no_cuenta(self):
        e = dict(entradas()[0]); e["tests"] = {"pass": e["tests"]["pass"], "fail": []}
        ok, why = rv.selftest(e)
        self.assertFalse(ok); self.assertIn("casos de prueba", why)

    def test_03_un_validador_roto_no_se_carga(self):
        """Si su autoprueba falla, la regla vuelve al auditor en vez de aprobarse sola."""
        e = dict(entradas()[0])
        e["check"] = {"op": "any_term", "in": "prompt", "terms": ["zzz-imposible"]}
        ok, _ = rv.selftest(e)
        self.assertFalse(ok)

    def test_04_unknown_no_es_pass(self):
        spec = {"when": {"path": "text.mode", "value": ["in_image"]},
                "op": "any_term", "in": "prompt", "terms": ["x"]}
        estado, _ = rv.evaluate(spec, {"prompt": "x", "case": {}})
        self.assertEqual(estado, rv.UNRESOLVED, "un caso que no declara el campo no puede dar PASS")

    def test_05_ninguno_se_usa_sin_aprobacion_de_eric(self):
        usables = rv.load(approved_only=True)
        pendientes = [e["rule_id"] for e in entradas() if e.get("approved_by") != "user"]
        for rid in pendientes:
            self.assertNotIn(rid, usables, f"{rid} se usaría sin que Eric lo apruebe")

    def test_06_cada_entrada_dice_que_regla_comprueba(self):
        for e in entradas():
            self.assertTrue(e.get("regla", "").strip(), f"{e['rule_id']} sin el texto de la regla")
            self.assertTrue(e.get("comprueba", "").strip(), f"{e['rule_id']} sin explicar qué comprueba")
            # El overlay aprendido v3.2 vive en un .json, no en un .md; lo que el test
            # exige es archivo y línea verificables, no una extensión concreta.
            self.assertRegex(e.get("source", ""), r".+\.(md|json):\d+", f"{e['rule_id']} sin archivo y línea de origen")

    def test_07_stages_ok_solo_pasa_con_todas_las_etapas_en_verde(self):
        spec = {"op": "stages_ok"}
        verde = {"stages": [{"name": "a", "status": "PASS"}, {"name": "b", "status": "NA"}]}
        self.assertEqual(rv.evaluate(spec, verde)[0], "PASS")
        rojo = {"stages": [{"name": "a", "status": "PASS"}, {"name": "b", "status": "FAIL"}]}
        estado, razon = rv.evaluate(spec, rojo)
        self.assertEqual(estado, "FAIL"); self.assertIn("b", razon)
        # Sin etapas no hay veredicto: nunca un PASS a ciegas.
        self.assertEqual(rv.evaluate(spec, {"stages": []})[0], rv.UNRESOLVED)

    def test_08_los_sub_gates_se_ven_como_etapas_y_gates_como_texto(self):
        sys.path.insert(0, str(ROOT / "apd"))
        import apd_run
        gates = {"lexical": {"natural_language": {"status": "PASS"}},
                 "structural": {"audit_gi2": {"status": "FAIL"}, "word_ceiling_source": "…/_capabilities.json"}}
        self.assertEqual(apd_run.gate_stages(gates),
                         [{"name": "gate:natural_language", "status": "PASS"},
                          {"name": "gate:audit_gi2", "status": "FAIL"}])
        # El informe de gates es consultable como texto: así una regla puede exigir que el
        # techo aplicado cite _capabilities.json y no la memoria.
        art = {"gates": gates}
        self.assertEqual(rv.evaluate({"in": "gates", "op": "regex", "pattern": r"_capabilities\.json"}, art)[0], "PASS")
        self.assertEqual(rv.evaluate({"in": "gates", "op": "regex", "pattern": r"_capabilities\.json"}, {"gates": {}})[0], "FAIL")


if __name__ == "__main__":
    unittest.main(verbosity=2)
