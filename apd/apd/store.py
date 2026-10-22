"""Persistencia del servidor (SQLite). Un cierre del navegador no pierde nada: el
proyecto, cada versión, los lotes en curso, los ledgers revisados y las evaluaciones
visuales viven aquí, no en el navegador."""

from __future__ import annotations

import json
import sqlite3
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path

from . import fuentes as F

DB = Path(__import__("os").environ.get("APD_DB", F.DATA / "proyectos.sqlite"))
UPLOADS = F.DATA / "uploads"
_lock = threading.RLock()

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
"""


def ahora() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def con() -> sqlite3.Connection:
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
    UPLOADS.mkdir(parents=True, exist_ok=True)
    h = F.sha256_text(data.decode("latin-1")) if False else __import__("hashlib").sha256(data).hexdigest()
    ext = Path(nombre).suffix.lower()[:8]
    p = UPLOADS / f"{h}{ext}"
    if not p.exists():
        p.write_bytes(data)
    return {"sha256": h, "ruta": str(p.relative_to(F.DATA)), "nombre": nombre, "bytes": len(data)}


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
