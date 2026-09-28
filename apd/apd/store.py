"""Persistencia del servidor. Un cierre del navegador no pierde nada: el proyecto, cada versión, los lotes en curso,
los ledgers revisados y las evaluaciones visuales viven aquí, no en el navegador.

Dos motores con el mismo SQL (dialecto SQLite):
- local: un archivo SQLite (APD_DB, por defecto apd/data/proyectos.sqlite);
- Turso/libSQL por HTTP cuando existen TURSO_DATABASE_URL y TURSO_AUTH_TOKEN (despliegue sin disco, p. ej. Vercel).
"""

from __future__ import annotations

import base64
import json
import os
import sqlite3
import threading
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

from . import fuentes as F

DB = Path(os.environ.get("APD_DB", F.DATA / "proyectos.sqlite"))
UPLOADS = F.DATA / "uploads"
_lock = threading.RLock()


def motor() -> str:
    return "turso" if os.environ.get("TURSO_DATABASE_URL") and os.environ.get("TURSO_AUTH_TOKEN") else "sqlite"

SCHEMA = """
CREATE TABLE IF NOT EXISTS proyectos (id TEXT PRIMARY KEY, nombre TEXT NOT NULL, creado TEXT NOT NULL,
  actual INTEGER NOT NULL DEFAULT 1);
CREATE TABLE IF NOT EXISTS versiones (proyecto_id TEXT NOT NULL, n INTEGER NOT NULL, creado TEXT NOT NULL,
  autor TEXT NOT NULL, nota TEXT, estado TEXT NOT NULL, PRIMARY KEY (proyecto_id, n));
CREATE TABLE IF NOT EXISTS ledgers (clave TEXT NOT NULL, registro TEXT NOT NULL, capa TEXT NOT NULL,
  decisiones TEXT NOT NULL, creado TEXT NOT NULL, PRIMARY KEY (clave, registro, capa));
CREATE TABLE IF NOT EXISTS lotes (id TEXT PRIMARY KEY, proyecto_id TEXT, clave TEXT NOT NULL, tipo TEXT NOT NULL,
  indice INTEGER NOT NULL, ids TEXT NOT NULL, estado TEXT NOT NULL, intentos INTEGER NOT NULL DEFAULT 0,
  errores TEXT, uso TEXT, respuesta TEXT, actualizado TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS ix_lotes ON lotes(clave, tipo);
CREATE TABLE IF NOT EXISTS eventos (proyecto_id TEXT, ts TEXT NOT NULL, tipo TEXT NOT NULL, detalle TEXT);
CREATE TABLE IF NOT EXISTS visual (id TEXT PRIMARY KEY, proyecto_id TEXT NOT NULL, version INTEGER NOT NULL,
  entrega_id TEXT NOT NULL, archivo TEXT NOT NULL, sha256 TEXT NOT NULL, media_type TEXT, prompt_hash TEXT,
  defectos TEXT NOT NULL, veredicto TEXT, nota TEXT, creado TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS archivos (nombre TEXT PRIMARY KEY, datos TEXT NOT NULL, creado TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS trabajos (id TEXT PRIMARY KEY, datos TEXT NOT NULL, actualizado TEXT NOT NULL);
"""


def ahora() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------------- Turso / libSQL por HTTP (Hrana v2)

class _Cursor:
    def __init__(self, filas):
        self._f = filas

    def fetchone(self):
        return self._f[0] if self._f else None

    def fetchall(self):
        return list(self._f)

    def __iter__(self):
        return iter(self._f)


def _arg(v):
    if v is None:
        return {"type": "null"}
    if isinstance(v, bool):
        return {"type": "integer", "value": str(int(v))}
    if isinstance(v, int):
        return {"type": "integer", "value": str(v)}
    if isinstance(v, float):
        return {"type": "float", "value": v}
    if isinstance(v, (bytes, bytearray)):
        return {"type": "blob", "base64": base64.b64encode(v).decode()}
    return {"type": "text", "value": str(v)}


def _val(x):
    t = x.get("type")
    if t == "null":
        return None
    if t == "integer":
        return int(x["value"])
    if t == "float":
        return float(x["value"])
    if t == "blob":
        return base64.b64decode(x.get("base64", ""))
    return x.get("value")


class _Turso:
    """Subconjunto de sqlite3.Connection que usa este módulo, sobre la API HTTP de Turso. Cada execute va en su propia
    petición (autocommit); el `with` no abre transacción. Sin dependencias: sólo urllib."""
    _esquema_listo = False

    def __init__(self):
        url = os.environ["TURSO_DATABASE_URL"].strip()
        self.url = ("https://" + url.split("://", 1)[1] if url.startswith("libsql://") else url).rstrip("/") + "/v2/pipeline"
        self.token = os.environ["TURSO_AUTH_TOKEN"].strip()

    def _pipeline(self, stmts):
        reqs = [{"type": "execute", "stmt": {"sql": s, "args": [_arg(a) for a in args]}} for s, args in stmts]
        body = json.dumps({"requests": reqs + [{"type": "close"}]}).encode()
        req = urllib.request.Request(self.url, data=body, method="POST",
                                     headers={"authorization": f"Bearer {self.token}", "content-type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.loads(r.read().decode())
        out = []
        for x in res.get("results", [])[:len(stmts)]:
            if x.get("type") != "ok":
                raise sqlite3.OperationalError(f"Turso: {(x.get('error') or {}).get('message', x)}")
            rs = x["response"]["result"]
            out.append([tuple(_val(c) for c in fila) for fila in rs.get("rows", [])])
        return out

    def execute(self, sql, params=()):
        return _Cursor(self._pipeline([(sql, tuple(params))])[0])

    def executescript(self, script):
        stmts = [(s.strip(), ()) for s in script.split(";") if s.strip()]
        if stmts:
            self._pipeline(stmts)

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def con():
    if motor() == "turso":
        c = _Turso()
        if not _Turso._esquema_listo:
            c.executescript(SCHEMA)
            _Turso._esquema_listo = True
        return c
    DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB, timeout=30, check_same_thread=False)
    c.executescript(SCHEMA)
    return c


def evento(pid, tipo, detalle=None):
    with _lock, con() as c:
        c.execute("insert into eventos values (?,?,?,?)", (pid, ahora(), tipo, json.dumps(detalle or {}, ensure_ascii=False)))


def crear_proyecto(nombre: str, estado: dict, autor="usuario") -> str:
    pid = uuid.uuid4().hex[:10]
    with _lock, con() as c:
        c.execute("insert into proyectos values (?,?,?,1)", (pid, nombre, ahora()))
        c.execute("insert into versiones values (?,?,?,?,?,?)", (pid, 1, ahora(), autor, "creación",
                                                                   json.dumps(estado, ensure_ascii=False)))
    evento(pid, "crear", {"nombre": nombre})
    return pid


def guardar_version(pid: str, estado: dict, autor: str, nota: str) -> int:
    with _lock, con() as c:
        n = (c.execute("select max(n) from versiones where proyecto_id=?", (pid,)).fetchone()[0] or 0) + 1
        c.execute("insert into versiones values (?,?,?,?,?,?)", (pid, n, ahora(), autor, nota,
                                                                   json.dumps(estado, ensure_ascii=False)))
        c.execute("update proyectos set actual=? where id=?", (n, pid))
    evento(pid, "version", {"n": n, "nota": nota, "autor": autor})
    return n


def reemplazar_version(pid: str, n: int, estado: dict):
    """Sólo para adjuntar resultados calculados de la MISMA versión (auditoría, ledger revisado)."""
    with _lock, con() as c:
        c.execute("update versiones set estado=? where proyecto_id=? and n=?", (json.dumps(estado, ensure_ascii=False), pid, n))


def version(pid: str, n: int | None = None) -> tuple[int, dict]:
    with con() as c:
        if n is None:
            n = c.execute("select actual from proyectos where id=?", (pid,)).fetchone()[0]
        row = c.execute("select estado from versiones where proyecto_id=? and n=?", (pid, n)).fetchone()
    if not row:
        raise KeyError(f"{pid} v{n}")
    return n, json.loads(row[0])


def listar() -> list[dict]:
    with con() as c:
        return [{"id": r[0], "nombre": r[1], "creado": r[2], "version": r[3]}
                for r in c.execute("select id, nombre, creado, actual from proyectos order by creado desc")]


def versiones(pid: str) -> list[dict]:
    with con() as c:
        return [{"n": r[0], "creado": r[1], "autor": r[2], "nota": r[3]}
                for r in c.execute("select n, creado, autor, nota from versiones where proyecto_id=? order by n", (pid,))]


def eventos(pid: str) -> list[dict]:
    with con() as c:
        return [{"ts": r[0], "tipo": r[1], "detalle": json.loads(r[2] or "{}")}
                for r in c.execute("select ts, tipo, detalle from eventos where proyecto_id=? order by ts", (pid,))]


def ledger_get(clave: str, registro: str, capa: str) -> dict | None:
    with con() as c:
        r = c.execute("select decisiones from ledgers where clave=? and registro=? and capa=?", (clave, registro, capa)).fetchone()
    return json.loads(r[0]) if r else None


def ledger_put(clave: str, registro: str, capa: str, dec: dict):
    with _lock, con() as c:
        c.execute("insert or replace into ledgers values (?,?,?,?,?)",
                  (clave, registro, capa, json.dumps(dec, ensure_ascii=False), ahora()))


def lote_put(l: dict):
    with _lock, con() as c:
        c.execute("insert or replace into lotes values (?,?,?,?,?,?,?,?,?,?,?,?)",
                  (l["id"], l.get("proyecto_id"), l["clave"], l["tipo"], l["indice"], json.dumps(l["ids"]), l["estado"],
                   l.get("intentos", 0), json.dumps(l.get("errores", []), ensure_ascii=False),
                   json.dumps(l.get("uso", {})), json.dumps(l.get("respuesta"), ensure_ascii=False), ahora()))


def lotes(clave: str, tipo: str) -> list[dict]:
    with con() as c:
        rows = c.execute("select id, proyecto_id, clave, tipo, indice, ids, estado, intentos, errores, uso, respuesta, actualizado "
                         "from lotes where clave=? and tipo=? order by indice", (clave, tipo)).fetchall()
    return [{"id": r[0], "proyecto_id": r[1], "clave": r[2], "tipo": r[3], "indice": r[4], "ids": json.loads(r[5]),
             "estado": r[6], "intentos": r[7], "errores": json.loads(r[8] or "[]"), "uso": json.loads(r[9] or "{}"),
             "respuesta": json.loads(r[10] or "null"), "actualizado": r[11]} for r in rows]


def guardar_archivo(data: bytes, nombre: str) -> dict:
    h = __import__("hashlib").sha256(data).hexdigest()
    ext = Path(nombre).suffix.lower()[:8]
    archivo = f"{h}{ext}"
    if motor() == "turso":  # sin disco persistente: el archivo vive en la base
        with _lock, con() as c:
            c.execute("insert or ignore into archivos values (?,?,?)", (archivo, base64.b64encode(data).decode(), ahora()))
    else:
        UPLOADS.mkdir(parents=True, exist_ok=True)
        p = UPLOADS / archivo
        if not p.exists():
            p.write_bytes(data)
    return {"sha256": h, "ruta": f"uploads/{archivo}", "nombre": nombre, "bytes": len(data)}


def leer_archivo(archivo: str) -> bytes | None:
    """Bytes de un archivo subido (sólo el nombre sha256+ext; nunca una ruta)."""
    archivo = Path(archivo).name
    if motor() == "turso":
        with con() as c:
            r = c.execute("select datos from archivos where nombre=?", (archivo,)).fetchone()
        return base64.b64decode(r[0]) if r else None
    p = UPLOADS / archivo
    return p.read_bytes() if p.is_file() and p.resolve().is_relative_to(UPLOADS.resolve()) else None


def trabajo_put(tid: str, datos: dict):
    """Estado de un trabajo largo (revisión por lotes). Persistido para que otra instancia del servidor lo lea."""
    with _lock, con() as c:
        c.execute("insert or replace into trabajos values (?,?,?)", (tid, json.dumps(datos, ensure_ascii=False, default=str), ahora()))


def trabajo_get(tid: str) -> dict | None:
    with con() as c:
        r = c.execute("select datos from trabajos where id=?", (tid,)).fetchone()
    return json.loads(r[0]) if r else None


def visual_put(v: dict):
    with _lock, con() as c:
        c.execute("insert or replace into visual values (?,?,?,?,?,?,?,?,?,?,?,?)",
                  (v["id"], v["proyecto_id"], v["version"], v["entrega_id"], v["archivo"], v["sha256"], v.get("media_type"),
                   v.get("prompt_hash"), json.dumps(v.get("defectos", []), ensure_ascii=False), v.get("veredicto"),
                   v.get("nota"), v.get("creado") or ahora()))


def visual_list(pid: str) -> list[dict]:
    with con() as c:
        rows = c.execute("select id, version, entrega_id, archivo, sha256, media_type, prompt_hash, defectos, veredicto, nota, creado "
                         "from visual where proyecto_id=? order by creado", (pid,)).fetchall()
    return [{"id": r[0], "version": r[1], "entrega_id": r[2], "archivo": r[3], "sha256": r[4], "media_type": r[5],
             "prompt_hash": r[6], "defectos": json.loads(r[7]), "veredicto": r[8], "nota": r[9], "creado": r[10]} for r in rows]
