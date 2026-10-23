"""Función de Vercel: atiende /api/* del taller en modo nube (ver nube.py)."""
import json
import sys
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import nube  # noqa: E402

LIMITE_CUERPO = 4_000_000  # Vercel limita el cuerpo a 4.5 MB


class handler(BaseHTTPRequestHandler):
    def _json(self, codigo, datos):
        cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def _partes(self):
        url = urlparse(self.path)
        ruta = parse_qs(url.query).get("ruta", [""])[0]  # la reescritura de vercel.json pasa la ruta original
        if ruta:
            return ["api"] + [p for p in ruta.split("/") if p]
        return [p for p in url.path.split("/") if p]

    def do_GET(self):
        partes = self._partes()
        if partes != ["api", "estado"]:
            return self._json(405, {"error": "En la nube todas las llamadas son POST con la instantánea."})
        self._json(*nube.atender(partes, {}, self.headers.get("X-Taller-Clave")))

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n > LIMITE_CUERPO:
            return self._json(413, {"error": "La instantánea supera 4 MB. Exporta un respaldo y archiva casos terminados."})
        try:
            sobre = json.loads(self.rfile.read(n) or b"{}") if n else {}
        except json.JSONDecodeError:
            return self._json(400, {"error": "JSON inválido"})
        self._json(*nube.atender(self._partes(), sobre, self.headers.get("X-Taller-Clave")))
