"""Cliente HTTP mínimo para el servidor de apd (sólo stdlib). Lo usa la prueba de aceptación con modelo real."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

BASE = os.environ.get("APD_URL", "http://127.0.0.1:8765")


def pedir(metodo: str, ruta: str, cuerpo=None, timeout=900):
    data = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(BASE + ruta, data=data, method=metodo, headers={"content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            return r.status, (json.loads(raw) if r.headers.get("content-type", "").startswith("application/json") else raw)
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, raw.decode(errors="replace")


def get(ruta):
    return pedir("GET", ruta)


def post(ruta, cuerpo=None):
    return pedir("POST", ruta, cuerpo or {})


def esperar_trabajo(tid: str, limite_s=1800) -> dict:
    t0 = time.time()
    while time.time() - t0 < limite_s:
        _, t = get(f"/api/trabajos/{tid}")
        if t.get("estado") not in ("EN_CURSO", None):
            return t
        time.sleep(3)
    return {"estado": "TIMEOUT"}
