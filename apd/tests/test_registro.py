"""Registro vigente, reconciliación 852/1,398, clasificación completa y citas de flujo."""

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import util  # noqa: F401
from apd import datos, flujos, fuentes as F, registro as R, sintaxis as SX


class TestRegistro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg = R.cargar()
        cls.val = R.validar(F.RULES_DB)

    def test_1398_ids_de_regla(self):
        self.assertTrue(self.val["ok"], self.val["errores"])
        self.assertEqual(self.val["reglas_ids_distintos"], 1398)
        self.assertEqual(len(self.reg.reglas), 1398)

    def test_relaciones_no_son_reglas(self):
        rel = self.val["relaciones"]
        self.assertGreater(rel["regla_caso"]["filas"], 1398)
        self.assertGreater(rel["regla_tarea"]["filas"], 1398)
        self.assertGreater(rel["regla_faceta"]["filas"], 1398)
        # ninguna relación introduce ids que no sean regla
        for t, info in rel.items():
            self.assertEqual(info.get("ids_que_no_son_regla", 0), 0, t)
        self.assertEqual(len(self.reg.reglas), 1398)

    def test_diferencia_con_852_del_ejecutor(self):
        r = R.reconciliar(self.reg)
        self.assertEqual(r["ejecutor"]["reglas_embebidas"], 852)
        self.assertEqual(r["en_ambos"] + r["solo_en_ejecutor"]["n"], 852)
        self.assertEqual(r["en_ambos"] + r["solo_en_registro"]["n"], 1398)
        suma = sum(v["n"] for v in r["solo_en_registro"]["por_motivo"].values())
        self.assertEqual(suma, 1398 - r["en_ambos"])
        self.assertTrue(any("build_app.py:1142" in c for c in r["causa_en_codigo"]))

    def test_validacion_detecta_base_incorrecta(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "mala.sqlite"
            c = sqlite3.connect(p)
            c.executescript("create table reglas (id text primary key, skill text, archivo text, linea int, texto text);"
                            "create table casos (codigo text, descripcion text);"
                            "create table regla_caso (regla_id text, caso text, origen text);"
                            "insert into reglas values ('0123456789ab','s','a',1,'t');"
                            "insert into regla_caso values ('ffffffffffff','T1','regla');")
            c.commit()
            c.close()
            rep = R.validar(p)
            self.assertFalse(rep["ok"])
            self.assertTrue(any("1398" in e for e in rep["errores"]))
            self.assertTrue(any("no están en reglas" in a for a in rep["avisos"]))

    def test_t1_scratchpad_coincide(self):
        t = datos.comparar_t1()
        self.assertEqual(t["ids_registro_en_t1"], 1398)
        self.assertEqual(t["textos_identicos"], 1398)
        self.assertTrue(all(x["archivo"] == "99-fixture-prueba.md" for x in t["solo_en_t1"]))

    def test_ninguna_regla_sin_clasificar(self):
        comp = json.loads((F.DATA / "clasificacion_app.json").read_text())["complemento"]
        from apd.ledger import Clasif
        cl = Clasif(self.reg, comp)
        for rid in self.reg.reglas:
            self.assertTrue(cl.casos(rid), rid)
            self.assertTrue(cl.tareas(rid), rid)
            for d in ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9"]:
                self.assertTrue(cl.faceta(rid, d)[0], (rid, d))

    def test_citas_de_flujos_literales(self):
        r = flujos.verificar_citas()
        self.assertEqual(r["faltan"], [])
        self.assertGreaterEqual(r["total"], 80)

    def test_citas_de_sintaxis_verificadas(self):
        out = subprocess.run([sys.executable, str(F.APD / "tools" / "check_citas.py"), str(SX.ARCHIVO)],
                             capture_output=True, text=True, timeout=120)
        self.assertEqual(out.returncode, 0, out.stdout[-500:])
        self.assertIn("fallidas=0", out.stdout)

    def test_originales_intactos(self):
        sums = (F.ORIGINALES / "SHA256SUMS").read_text().split("\n")
        for linea in filter(None, sums):
            h, nombre = linea.split()
            self.assertEqual(F.sha256_file(F.ORIGINALES / nombre), h, nombre)


if __name__ == "__main__":
    unittest.main()
