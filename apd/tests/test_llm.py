"""Adaptadores OpenAI (Responses API) y Anthropic (Messages API) contra un servidor local que imita
sus respuestas. Verifica cabeceras, cuerpo, parseo y el flujo automático completo por lotes.
No prueba la calidad de un modelo real: eso queda BLOQUEADO POR DEPENDENCIA sin clave."""

import json
import os
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import util
from apd import llm, proyecto as P

VISTO = []


def decisiones_para(texto):
    if "IDS DE ESTE LOTE (" not in texto:
        return json.dumps({"comunes": {}, "entregas": [], "propuestas": {}})  # extracción de spec: sin propuestas
    ids = texto.split("IDS DE ESTE LOTE (")[1].split("): ", 1)[1].split("\n")[0].split(", ")
    return json.dumps({"decisiones": [{"id": i, "estado": "NO_APLICA",
                                       "razon": "revisada por el modelo: no gobierna esta entrega T1 gpt-image-2 imagen fija"} for i in ids]})


class Imitador(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["content-length"])))
        VISTO.append({"ruta": self.path, "headers": dict(self.headers), "body": body})
        if self.path.endswith("/responses"):
            texto = body["input"][0]["content"][-1]["text"]
            out = {"output": [{"type": "message", "content": [{"type": "output_text", "text": decisiones_para(texto)}]}],
                   "usage": {"input_tokens": 1000, "output_tokens": 200}}
        else:
            texto = body["messages"][0]["content"][-1]["text"]
            out = {"content": [{"type": "text", "text": decisiones_para(texto)}], "usage": {"input_tokens": 900, "output_tokens": 180}}
        data = json.dumps(out).encode()
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


class TestAdaptadores(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = ThreadingHTTPServer(("127.0.0.1", 0), Imitador)
        cls.url = f"http://127.0.0.1:{cls.srv.server_address[1]}/v1"
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        llm.fijar(None)

    def _flujo(self, prov):
        llm.fijar(prov)
        pid = util.proyecto_quinteto("llm-" + prov.nombre)
        VISTO.clear()
        tid = P.revisar_con_modelo(pid, en_hilo=False)
        t = P.trabajo(tid)
        self.assertEqual(t["estado"], "COMPLETO", t.get("error"))
        n, e = P.cargar(pid)
        led = next(iter(e["_ledgers_completos"].values()))
        self.assertEqual(sum(1 for d in led["decisiones"].values() if d["capa"] == "modelo"), 1398)
        self.assertTrue(led["revision_modelo"] if "revision_modelo" in led else e["ledgers"][next(iter(e["ledgers"]))]["revision_modelo"])
        # consumo y tiempo reales del procesamiento completo, expuestos (no sólo la estimación)
        uso = next(iter(t["resultado"].values()))["uso"]
        self.assertEqual(uso["entrada"], sum(v["body"] and (1000 if v["ruta"].endswith("/responses") else 900) for v in VISTO))
        self.assertGreater(uso["salida"], 0)
        self.assertGreaterEqual(uso["segundos"], 0)
        self.assertEqual(t["progreso"][-1]["lote"], t["progreso"][-1]["de"])
        return VISTO

    def test_openai(self):
        os.environ["OPENAI_API_KEY"] = "sk-prueba-local"
        os.environ["OPENAI_BASE_URL"] = self.url
        try:
            vistos = self._flujo(llm.OpenAI())
        finally:
            os.environ.pop("OPENAI_API_KEY")
            os.environ.pop("OPENAI_BASE_URL")
        self.assertEqual(len(vistos), 24)  # 1,398 ids / 60 por lote
        h = {k.lower(): v for k, v in vistos[0]["headers"].items()}
        self.assertEqual(h["authorization"], "Bearer sk-prueba-local")
        self.assertEqual(vistos[0]["body"]["text"]["format"]["type"], "json_object")
        self.assertIn("instructions", vistos[0]["body"])

    def test_anthropic(self):
        os.environ["ANTHROPIC_API_KEY"] = "sk-ant-prueba-local"
        os.environ["APD_ANTHROPIC_URL"] = self.url
        try:
            vistos = self._flujo(llm.Anthropic())
        finally:
            os.environ.pop("ANTHROPIC_API_KEY")
            os.environ.pop("APD_ANTHROPIC_URL")
        h = {k.lower(): v for k, v in vistos[0]["headers"].items()}
        self.assertEqual(h["x-api-key"], "sk-ant-prueba-local")
        self.assertEqual(h["anthropic-version"], "2023-06-01")
        self.assertIn("system", vistos[0]["body"])

    def test_clave_no_sale_del_servidor(self):
        os.environ["OPENAI_API_KEY"] = "sk-secreta-123"
        try:
            llm.fijar(None)
            est = llm.estado()
            self.assertNotIn("sk-secreta-123", json.dumps(est))
        finally:
            os.environ.pop("OPENAI_API_KEY")
            llm.fijar(None)


class TestEtapaConModelo(unittest.TestCase):
    def tearDown(self):
        llm.fijar(None)

    def test_e4_genera_shots_validado_y_pendiente_de_ok(self):
        from apd import fuentes as F
        shots = json.loads((F.extraer_paquete() / "skills/storyboard-architect/examples/30s-pain-proof-promise/shots.json").read_text())
        recibido = {}

        def fn(sistema, usuario):
            recibido["n"] = usuario.count("\n[")
            return json.dumps({"shots_json": shots, "notas": "ok", "preguntas": []})
        llm.fijar(llm.Falso(fn))
        pid = P.nuevo({"texto": "Spot de 20 segundos para redes, un solo beat."}, "etapa-e4")
        r = P.generar_etapa(pid, "E4")
        self.assertEqual(r["errores"], [])
        self.assertTrue(r["pendiente_ok"])
        self.assertEqual(recibido["n"], len(P.reglas_de_etapa("E4")))  # todas las reglas de la etapa, sin recorte
        n, e = P.cargar(pid)
        self.assertFalse(e["etapas"]["E4"]["aprobada"])
        self.assertTrue(e["entregas"] == {})


if __name__ == "__main__":
    unittest.main()
