"""Servidor local del taller: http://127.0.0.1:8770

Uso:  python taller/server.py            (proveedor según TALLER_PROVEEDOR; por defecto anthropic)
      TALLER_PROVEEDOR=manual python taller/server.py

Si falta la clave del proveedor elegido, la app cae al modo manual y lo avisa.
Las rutas y compuertas son las mismas que en la nube (rutas.py); aquí el estado vive en SQLite y las
operaciones largas corren en un hilo mientras la interfaz consulta su avance.
"""
import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))

import llm  # noqa: E402
import proceso as P  # noqa: E402
import rutas  # noqa: E402

AQUI = Path(__file__).resolve().parent
ESTATICO = AQUI / "static"
TIPOS = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8"}


class Estado:
    """Contexto local para rutas.despachar."""

    def __init__(self):
        self.almacen = P.Almacen(os.environ.get("TALLER_DB", str(AQUI / "datos" / "taller.sqlite3")))
        self.operaciones = {}
        self.nombre = os.environ.get("TALLER_PROVEEDOR", "anthropic")
        self.proceso = None
        self.error_proveedor = ""
        self.cambiar_proveedor(self.nombre)

    def cambiar_proveedor(self, nombre):
        try:
            prov = llm.crear(nombre, self.almacen)
            self.error_proveedor = ""
        except llm.ErrorModelo as e:
            prov = llm.crear("manual", self.almacen)
            self.error_proveedor = f"{e} Se usa el modo manual."
        self.nombre = prov.nombre
        self.proceso = P.Proceso(self.almacen, prov)

    def nombre_proveedor(self):
        return self.nombre

    def aviso_proveedor(self):
        return self.error_proveedor

    def operacion(self, cid):
        return self.operaciones.get(cid)

    def lanzar(self, cid, nombre, nueva):
        actual = self.operaciones.get(cid)
        if actual and actual["estado"] == "en_curso":
            raise P.Compuerta(f"Ya hay una operación en curso: {actual['nombre']}.")
        op = self.operaciones[cid] = rutas.nueva_operacion(nombre)
        pr = self.proceso
        threading.Thread(target=rutas.ejecutar_operacion, args=(pr, cid, nombre, nueva, op), daemon=True).start()
        return 202, {"operacion": nombre}

    def continuar(self, cid, nombre):
        raise P.Compuerta("En el servidor local la operación sigue sola; no hace falta continuarla.")


ESTADO = None


class Manejador(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def _json(self, codigo, datos):
        cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def _cuerpo(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}") if n else {}

    def _responder(self, codigo, datos):
        if codigo == 200 and "_markdown" in datos:
            texto = datos["_markdown"].encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/markdown; charset=utf-8")
            self.send_header("Content-Disposition", f'attachment; filename="{datos["_nombre"]}"')
            self.end_headers()
            return self.wfile.write(texto)
        return self._json(codigo, datos)

    def do_GET(self):
        ruta = urlparse(self.path).path
        if ruta in ("/", "/index.html"):
            return self._archivo(ESTATICO / "index.html")
        if ruta.startswith("/static/"):
            return self._archivo(ESTATICO / Path(ruta).name)
        partes = [p for p in ruta.split("/") if p]
        self._responder(*rutas.despachar("GET", partes, None, ESTADO.proceso, ESTADO))

    def do_POST(self):
        partes = [p for p in urlparse(self.path).path.split("/") if p]
        try:
            b = self._cuerpo()
        except json.JSONDecodeError:
            return self._json(400, {"error": "JSON inválido"})
        self._responder(*rutas.despachar("POST", partes, b, ESTADO.proceso, ESTADO))

    def _archivo(self, ruta):
        if not ruta.exists():
            return self._json(404, {"error": "No encontrado"})
        datos = ruta.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", TIPOS.get(ruta.suffix, "application/octet-stream"))
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)


def main():
    global ESTADO
    ESTADO = Estado()
    puerto = int(os.environ.get("TALLER_PUERTO", "8770"))
    servidor = ThreadingHTTPServer(("127.0.0.1", puerto), Manejador)
    print(f"Taller de prompts en http://127.0.0.1:{puerto}  (proveedor: {ESTADO.nombre})")
    if ESTADO.error_proveedor:
        print("Aviso:", ESTADO.error_proveedor)
    servidor.serve_forever()


if __name__ == "__main__":
    main()
