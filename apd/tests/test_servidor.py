"""La API HTTP real: modo sin modelo honesto, bloqueo de copia/exportación, persistencia entre sesiones,
importación de rules.sqlite, lotes para revisor externo con la misma validación, y que la clave nunca
llega al navegador."""

import base64
import json
import os
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import util
from apd import fuentes as F

import server as SV


class TestServidor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = ThreadingHTTPServer(("127.0.0.1", 0), SV.H)
        cls.base = f"http://127.0.0.1:{cls.srv.server_address[1]}"
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    def req(self, path, body=None, metodo=None):
        data = json.dumps(body).encode() if body is not None else None
        r = urllib.request.Request(self.base + path, data=data, method=metodo or ("POST" if data else "GET"),
                                   headers={"content-type": "application/json"})
        try:
            with urllib.request.urlopen(r, timeout=300) as resp:
                raw = resp.read()
                return resp.status, (json.loads(raw) if resp.headers.get("content-type", "").startswith("application/json") else raw)
        except urllib.error.HTTPError as e:
            raw = e.read()
            try:
                return e.code, json.loads(raw)
            except Exception:
                return e.code, raw

    def test_flujo_http_sin_modelo(self):
        c, cfg = self.req("/api/config")
        self.assertEqual(c, 200)
        self.assertFalse(cfg["ia"]["disponible"])
        self.assertNotIn("key", json.dumps(cfg).lower().replace("clave", ""))
        c, r = self.req("/api/proyectos", {"nombre": "http", "brief": {"texto": util.BRIEF_QUINTETO}})
        self.assertEqual(c, 201)
        pid = r["id"]
        self.req(f"/api/proyectos/{pid}/propuestas", {})
        c, v = self.req(f"/api/proyectos/{pid}")
        self.assertEqual(c, 200)
        self.assertEqual(len(v["entregas"]), 5)
        # sin modelo: la revisión automática se desactiva con explicación (503), la inspección sigue
        c, r = self.req(f"/api/proyectos/{pid}/revisar-modelo", {})
        self.assertEqual(c, 503)
        self.assertIn("modelo", r["error"])
        c, r = self.req(f"/api/proyectos/{pid}/reglas?estado=APLICA&limit=5")
        self.assertEqual(c, 200)
        self.assertEqual(r["total_registro"], 1398)
        # copiar y exportar-aprobado bloqueados
        c, r = self.req(f"/api/proyectos/{pid}/entregas/E1/copiar")
        self.assertEqual(c, 409)
        self.assertIsNone(r["texto"])
        c, r = self.req(f"/api/proyectos/{pid}/exportar?aprobado=1")
        self.assertEqual(c, 409)
        c, raw = self.req(f"/api/proyectos/{pid}/exportar")
        self.assertEqual(c, 200)
        # persistencia: otra "sesión" (nueva petición sin estado de navegador) ve lo mismo
        c, v2 = self.req(f"/api/proyectos/{pid}")
        self.assertEqual(v2["version"], v["version"])
        self.assertEqual(v2["entregas"]["E3"]["hash"], v["entregas"]["E3"]["hash"])
        # ficha de regla con trazabilidad
        rid = r_id = next(iter(v["ledgers"].values()))["recibo"]["registro"] and sorted(util.P.registro().reglas)[0]
        c, f = self.req(f"/api/reglas/{rid}?pid={pid}")
        self.assertEqual(c, 200)
        self.assertIn("decisiones", f)
        self.assertIn("historial", f)

    def test_revisor_externo_misma_validacion(self):
        c, r = self.req("/api/proyectos", {"nombre": "externo", "brief": {"texto": util.BRIEF_QUINTETO}})
        pid = r["id"]
        self.req(f"/api/proyectos/{pid}/propuestas", {})
        c, lotes = self.req(f"/api/proyectos/{pid}/lotes-decision")
        clave, per = next(iter(lotes["perfiles"].items()))
        ids = [i for l in per["lotes"] for i in l["ids"]]
        self.assertEqual(len(ids), 1398)
        self.assertEqual(len(set(ids)), 1398)
        # respuesta incompleta: rechazada, nada se aplica
        malas = {str(l["indice"]): {"decisiones": [{"id": i, "estado": "NO_APLICA", "razon": "no aplica"} for i in l["ids"]]} for l in per["lotes"]}
        c, inf = self.req(f"/api/proyectos/{pid}/lotes-decision", {"perfil": clave, "respuestas": malas, "revisor": "prueba"})
        self.assertFalse(inf["completo"])
        buenas = {str(l["indice"]): {"decisiones": [{"id": i, "estado": "NO_APLICA", "razon": "revisada para esta entrega T1 gpt-image-2 imagen fija"} for i in l["ids"]]}
                  for l in per["lotes"]}
        c, inf = self.req(f"/api/proyectos/{pid}/lotes-decision", {"perfil": clave, "respuestas": buenas, "revisor": "prueba"})
        self.assertTrue(inf["completo"])

    def test_importar_rules_sqlite(self):
        data = base64.b64encode(F.RULES_DB.read_bytes()).decode()
        c, rep = self.req("/api/importar-rules-sqlite", {"data": data})
        self.assertEqual(c, 200)
        self.assertTrue(rep["ok"])
        self.assertEqual(rep["reglas_ids_distintos"], 1398)
        self.assertEqual(rep["comparacion_con_registro_vigente"]["en_ambos"], 1398)

    def test_estaticos_y_rutas(self):
        c, raw = self.req("/")
        self.assertEqual(c, 200)
        self.assertIn(b"Director de Prompts", raw)
        c, raw = self.req("/web/../server.py")
        self.assertEqual(c, 404)


if __name__ == "__main__":
    unittest.main()
