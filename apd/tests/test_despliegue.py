"""Despliegue sin disco (Vercel): base de proyectos en Turso por HTTP, rutas reenviadas por vercel.json con __ruta,
contraseña obligatoria en la liga pública, trabajos síncronos persistidos.

El servidor Turso de esta prueba es una imitación local del protocolo HTTP v2 (pipeline) sobre sqlite3: prueba que el
cliente arma y lee ese formato, no que el servicio real responda igual. La verificación real es el primer despliegue."""

import json
import os
import sqlite3
import threading
import unittest
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import util
from apd import store as ST, proyecto as P

RAIZ = Path(__file__).resolve().parents[2]


class _TursoFalso(BaseHTTPRequestHandler):
    db = None
    token = "tok-prueba"
    vistos = []

    def log_message(self, *a):
        pass

    def do_POST(self):
        assert self.path == "/v2/pipeline", self.path
        if self.headers.get("authorization") != f"Bearer {self.token}":
            self.send_response(401)
            self.end_headers()
            return
        body = json.loads(self.rfile.read(int(self.headers["content-length"])))
        self.vistos.append(body)
        results = []
        for r in body["requests"]:
            if r["type"] == "close":
                results.append({"type": "ok", "response": {"type": "close"}})
                continue
            st = r["stmt"]
            args = []
            for a in st.get("args", []):
                args.append(None if a["type"] == "null" else int(a["value"]) if a["type"] == "integer"
                            else float(a["value"]) if a["type"] == "float" else a["value"])
            try:
                cur = self.db.execute(st["sql"], args)
                rows = [[{"type": "null"} if v is None else {"type": "integer", "value": str(v)} if isinstance(v, int)
                         else {"type": "text", "value": v} for v in fila] for fila in cur.fetchall()]
                self.db.commit()
                results.append({"type": "ok", "response": {"type": "execute", "result": {
                    "cols": [{"name": d[0]} for d in (cur.description or [])], "rows": rows, "affected_row_count": cur.rowcount}}})
            except sqlite3.Error as ex:
                results.append({"type": "error", "error": {"message": str(ex)}})
        data = json.dumps({"baton": None, "base_url": None, "results": results}).encode()
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


class TestTurso(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _TursoFalso.db = sqlite3.connect(":memory:", check_same_thread=False)
        cls.srv = ThreadingHTTPServer(("127.0.0.1", 0), _TursoFalso)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        os.environ["TURSO_DATABASE_URL"] = f"http://127.0.0.1:{cls.srv.server_address[1]}"
        os.environ["TURSO_AUTH_TOKEN"] = _TursoFalso.token
        ST._Turso._esquema_listo = False

    @classmethod
    def tearDownClass(cls):
        os.environ.pop("TURSO_DATABASE_URL")
        os.environ.pop("TURSO_AUTH_TOKEN")
        cls.srv.shutdown()

    def test_proyecto_completo_en_turso(self):
        self.assertEqual(ST.motor(), "turso")
        pid = P.nuevo({"texto": "Foto de producto de una botella de perfume de vidrio sobre mármol blanco"}, "turso")
        P.cambiar_campos(pid, [{"ruta": "comunes.sujeto", "valor": "a glass perfume bottle"}])
        n, e = P.cargar(pid)
        self.assertGreaterEqual(n, 2)
        self.assertTrue(e["entregas"]["E1"]["compilado"]["hash"])
        self.assertEqual([p["id"] for p in ST.listar()][:1], [pid])
        self.assertEqual([v["n"] for v in ST.versiones(pid)], list(range(1, n + 1)))
        # las filas viven en la base «remota», no en el SQLite local
        self.assertEqual(_TursoFalso.db.execute("select count(*) from versiones where proyecto_id=?", (pid,)).fetchone()[0], n)

    def test_archivos_y_trabajos_en_la_base(self):
        info = ST.guardar_archivo(b"\x89PNG\r\nfalso", "ref.png")
        self.assertEqual(ST.leer_archivo(info["ruta"].split("/")[-1]), b"\x89PNG\r\nfalso")
        self.assertIsNone(ST.leer_archivo("../../etc/passwd"))
        ST.trabajo_put("t1", {"estado": "COMPLETO", "progreso": [{"lote": 1, "de": 1}]})
        self.assertEqual(ST.trabajo_get("t1")["estado"], "COMPLETO")

    def test_argumentos_con_tipo(self):
        tipos = {a["type"] for b in _TursoFalso.vistos for r in b["requests"] if r["type"] == "execute"
                 for a in r["stmt"].get("args", [])}
        self.assertTrue(tipos <= {"text", "integer", "null", "float", "blob"}, tipos)


class TestVercel(unittest.TestCase):
    """El handler tal como lo monta api/index.py: rutas reenviadas con __ruta, contraseña obligatoria."""

    @classmethod
    def setUpClass(cls):
        import server
        cls.server = server
        cls.srv = ThreadingHTTPServer(("127.0.0.1", 0), server.H)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.srv.server_address[1]}"

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.server.PUBLICO = False
        os.environ.pop("APP_PASSWORD", None)

    def get(self, ruta, clave=None):
        req = urllib.request.Request(self.base + ruta, headers={"x-app-password": clave} if clave else {})
        try:
            with urllib.request.urlopen(req) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            return e.code, e.read()

    def test_ruta_reenviada_sirve_la_app_nueva(self):
        c, body = self.get("/api/index?__ruta=/")
        self.assertEqual(c, 200)
        self.assertIn(b"Director de Prompts", body)
        c, body = self.get("/api/index?__ruta=/web/app.js")
        self.assertEqual(c, 200)

    def test_liga_publica_exige_app_password(self):
        self.server.PUBLICO = True
        os.environ.pop("APP_PASSWORD", None)
        c, body = self.get("/api/index?__ruta=/api/config")
        self.assertEqual(c, 200)
        self.assertTrue(json.loads(body)["falta_clave_app"])
        c, body = self.get("/api/index?__ruta=/api/proyectos")
        self.assertEqual(c, 401)
        os.environ["APP_PASSWORD"] = "secreta"
        self.assertEqual(self.get("/api/index?__ruta=/api/proyectos")[0], 401)
        self.assertEqual(self.get("/api/index?__ruta=/api/proyectos", "secreta")[0], 200)
        self.server.PUBLICO = False
        os.environ.pop("APP_PASSWORD")

    def test_config_de_despliegue(self):
        cfg = json.loads((RAIZ / "vercel.json").read_text())
        inc = cfg["functions"]["api/index.py"]["includeFiles"]
        for x in ("apd/apd/**", "apd/web/**", "apd/deploy/rules.sqlite", "apd/originales/**", ".claude/hooks/**"):
            self.assertIn(x, inc)
        self.assertTrue((RAIZ / "apd/deploy/rules.sqlite").is_file())
        ign = (RAIZ / ".vercelignore").read_text().split()
        self.assertIn("public", ign)  # el ejecutor anterior ya no se publica
        self.assertIn("api/sample.js", ign)
        c = sqlite3.connect(RAIZ / "apd/deploy/rules.sqlite")
        self.assertEqual(c.execute("select count(*) from reglas").fetchone()[0], 1398)
        self.assertEqual(c.execute("select count(*) from embeddings").fetchone()[0], 1398)  # tabla vectorial llena

    def test_trabajo_sin_hilos_queda_persistido(self):
        from apd import llm
        P.SIN_HILOS = True
        try:
            llm.fijar(llm.Falso(lambda s, u: json.dumps({"decisiones": []})))
            pid = util.proyecto_quinteto("sin-hilos")
            os.environ["APD_REVISION"] = "abiertas"
            tid = P.revisar_con_modelo(pid)
            P._trabajos.pop(tid)  # otra invocación no comparte memoria
            self.assertIn(P.trabajo(tid)["estado"], ("COMPLETO", "INCOMPLETO"))
        finally:
            P.SIN_HILOS = False
            os.environ["APD_REVISION"] = "todas"
            llm.fijar(None)


if __name__ == "__main__":
    unittest.main()
