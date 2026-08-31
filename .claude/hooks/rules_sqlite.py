#!/usr/bin/env python3
"""Base de datos SQLite de reglas del pipeline visual.

Esquema:

  reglas        una fila por enunciado normativo extraido de los skills
  casos         la taxonomia cerrada de casos de produccion
  regla_caso    que reglas aplican a que casos, con quien lo dijo y que tan fino
  auditorias    correcciones de un criterio externo, con fecha

`origen` en regla_caso distingue como se clasifico:
  archivo   por defecto del archivo completo — grueso, es lo que hay que auditar
  regla     decidido regla por regla — mas fino
  auditoria corregido por un criterio externo — manda sobre los otros dos

Asi la auditoria puede priorizar lo grueso, y siempre se sabe de donde salio
cada dato en vez de tener que creerle a alguien.

Uso:
    python3 rules_sqlite.py init   --registry r_*.json --db rules.sqlite
    python3 rules_sqlite.py load   --db rules.sqlite --clasificacion c.txt --origen regla
    python3 rules_sqlite.py caso   --db rules.sqlite T1
    python3 rules_sqlite.py stats  --db rules.sqlite
    python3 rules_sqlite.py export --db rules.sqlite --csv reglas.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

CASOS = {
    "T1": "maestro de rostro (still, persona, identidad)",
    "T2": "maestro de cuerpo (still, persona completa)",
    "T3": "cuadro con 1 persona (still de escena)",
    "T4": "cuadro con 2 personas (still, contacto/interaccion)",
    "T5": "edicion quirurgica sobre imagen existente",
    "CLIP": "prompt de video / movimiento",
    "SHOT": "planeacion de shots, storyboard, shots.json",
    "GUION": "escritura de guion o tratamiento",
    "MARCA": "extraccion o uso de brand-lock",
    "QA": "critica de render, revision de asset generado",
    "ENTREGA": "empaquetado, preview, entrega a cliente",
    "PROD": "still de producto, comida u objeto (sin persona)",
    "GRAF": "pieza grafica: poster, slide, UI, social, tipografia dominante",
    "MULTI": "multi-panel o grid dentro de una sola imagen",
    "REF": "analisis de imagen de referencia, image-to-prompt",
    "NINGUNO": "no aplica a ningun caso de produccion (meta, ejemplos, docs)",
}

SCHEMA = """
CREATE TABLE IF NOT EXISTS reglas (
    id        TEXT PRIMARY KEY,
    skill     TEXT NOT NULL,
    archivo   TEXT NOT NULL,
    linea     INTEGER NOT NULL,
    texto     TEXT NOT NULL,
    marcadores TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS casos (
    codigo      TEXT PRIMARY KEY,
    descripcion TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS regla_caso (
    regla_id TEXT NOT NULL REFERENCES reglas(id),
    caso     TEXT NOT NULL REFERENCES casos(codigo),
    origen   TEXT NOT NULL CHECK (origen IN ('archivo','regla','auditoria')),
    fecha    TEXT NOT NULL,
    PRIMARY KEY (regla_id, caso)
);
CREATE TABLE IF NOT EXISTS auditorias (
    regla_id  TEXT NOT NULL REFERENCES reglas(id),
    antes     TEXT NOT NULL,
    despues   TEXT NOT NULL,
    razon     TEXT,
    auditor   TEXT NOT NULL,
    fecha     TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_rc_caso  ON regla_caso(caso);
CREATE INDEX IF NOT EXISTS ix_reglas_sk ON reglas(skill, archivo);

CREATE VIEW IF NOT EXISTS v_sin_clasificar AS
  SELECT r.* FROM reglas r
  LEFT JOIN regla_caso rc ON rc.regla_id = r.id
  WHERE rc.regla_id IS NULL;

CREATE VIEW IF NOT EXISTS v_por_caso AS
  SELECT c.codigo, c.descripcion, COUNT(rc.regla_id) AS reglas
  FROM casos c LEFT JOIN regla_caso rc ON rc.caso = c.codigo
  GROUP BY c.codigo ORDER BY reglas DESC;
"""

LINE_RE = re.compile(r"\[?([0-9a-f]{12})\]?\s*[-—:]?\s*([A-Z0-9,\s]+?)\s*$", re.MULTILINE)


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def connect(path: str) -> sqlite3.Connection:
    con = sqlite3.connect(path)
    con.execute("PRAGMA foreign_keys = ON")
    return con


def cmd_init(args) -> int:
    con = connect(args.db)
    con.executescript(SCHEMA)
    con.executemany(
        "INSERT OR REPLACE INTO casos (codigo, descripcion) VALUES (?,?)", CASOS.items()
    )
    n = 0
    for p in args.registry:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        skill = data.get("skill", "?")
        for r in data.get("rules", []):
            con.execute(
                "INSERT OR REPLACE INTO reglas VALUES (?,?,?,?,?,?)",
                (r["id"], skill, r["file"], r["line"], r["text"], ",".join(r["markers"])),
            )
            n += 1
    con.commit()
    total = con.execute("SELECT COUNT(*) FROM reglas").fetchone()[0]
    print(f"{n} reglas insertadas · {total} en la base · {len(CASOS)} casos")
    return 0


def cmd_load(args) -> int:
    con = connect(args.db)
    texto = Path(args.clasificacion).read_text(encoding="utf-8")
    ok = mal = desc = 0
    for m in LINE_RE.finditer(texto):
        rid, crudo = m.group(1), m.group(2)
        if not con.execute("SELECT 1 FROM reglas WHERE id=?", (rid,)).fetchone():
            desc += 1
            continue
        casos = [c.strip().upper() for c in crudo.split(",") if c.strip()]
        if not casos or any(c not in CASOS for c in casos):
            mal += 1
            continue
        if args.origen == "auditoria":
            antes = ",".join(
                r[0] for r in con.execute(
                    "SELECT caso FROM regla_caso WHERE regla_id=? ORDER BY caso", (rid,))
            )
            con.execute(
                "INSERT INTO auditorias VALUES (?,?,?,?,?,?)",
                (rid, antes, ",".join(sorted(casos)), args.razon, args.auditor, now()),
            )
            con.execute("DELETE FROM regla_caso WHERE regla_id=?", (rid,))
        for c in casos:
            con.execute(
                "INSERT OR REPLACE INTO regla_caso VALUES (?,?,?,?)", (rid, c, args.origen, now())
            )
        ok += 1
    con.commit()
    pend = con.execute("SELECT COUNT(*) FROM v_sin_clasificar").fetchone()[0]
    print(f"clasificadas: {ok} · invalidas: {mal} · ids inexistentes: {desc}")
    print(f"sin clasificar en la base: {pend}")
    return 1 if (mal or desc) else 0


def cmd_caso(args) -> int:
    con = connect(args.db)
    filas = con.execute(
        """SELECT r.skill, r.archivo, r.linea, r.texto, rc.origen
           FROM regla_caso rc JOIN reglas r ON r.id = rc.regla_id
           WHERE rc.caso = ? ORDER BY r.skill, r.archivo, r.linea""",
        (args.codigo,),
    ).fetchall()
    if not filas:
        print(f"sin reglas para el caso {args.codigo}", file=sys.stderr)
        return 1
    print(f"# {args.codigo} — {CASOS.get(args.codigo,'?')}")
    print(f"# {len(filas)} reglas\n")
    actual = None
    for skill, arch, _ln, texto, origen in filas:
        ruta = f"{skill}/{arch}"
        if ruta != actual:
            actual = ruta
            print(f"\n## {ruta}")
        marca = "" if origen != "archivo" else "  [clasificacion gruesa]"
        print(f"- {texto}{marca}")
    return 0


def cmd_stats(args) -> int:
    con = connect(args.db)
    tot = con.execute("SELECT COUNT(*) FROM reglas").fetchone()[0]
    cls = con.execute("SELECT COUNT(DISTINCT regla_id) FROM regla_caso").fetchone()[0]
    print(f"reglas          {tot}")
    print(f"clasificadas    {cls}  ({cls/max(tot,1)*100:.1f}%)")
    print(f"sin clasificar  {tot-cls}")
    print()
    print("por origen de la clasificacion:")
    for origen, n in con.execute(
        "SELECT origen, COUNT(DISTINCT regla_id) FROM regla_caso GROUP BY origen ORDER BY 2 DESC"
    ):
        print(f"  {origen:10} {n:>5}")
    print()
    print("reglas por caso:")
    for cod, desc, n in con.execute("SELECT * FROM v_por_caso"):
        if n:
            print(f"  {cod:8} {n:>5}   {desc}")
    print()
    print("por skill:")
    for skill, n in con.execute(
        "SELECT skill, COUNT(*) FROM reglas GROUP BY skill ORDER BY 2 DESC"
    ):
        print(f"  {skill:26} {n:>5}")
    aud = con.execute("SELECT COUNT(*) FROM auditorias").fetchone()[0]
    print(f"\ncorrecciones de auditoria: {aud}")
    return 0


def cmd_export(args) -> int:
    con = connect(args.db)
    filas = con.execute(
        """SELECT r.id, r.skill, r.archivo, r.linea, r.texto,
                  GROUP_CONCAT(rc.caso), MIN(rc.origen)
           FROM reglas r LEFT JOIN regla_caso rc ON rc.regla_id = r.id
           GROUP BY r.id ORDER BY r.skill, r.archivo, r.linea"""
    ).fetchall()
    with open(args.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "skill", "archivo", "linea", "regla", "casos", "origen"])
        w.writerows(filas)
    print(f"{len(filas)} filas -> {args.csv}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Base SQLite de reglas por caso")
    ap.add_argument("--db", default="rules.sqlite")
    sub = ap.add_subparsers(dest="cmd", required=True)

    i = sub.add_parser("init"); i.add_argument("--registry", nargs="+", required=True)
    i.set_defaults(fn=cmd_init)

    l = sub.add_parser("load")
    l.add_argument("--clasificacion", required=True)
    l.add_argument("--origen", choices=("archivo", "regla", "auditoria"), required=True)
    l.add_argument("--auditor", default="notebooklm")
    l.add_argument("--razon", default="")
    l.set_defaults(fn=cmd_load)

    c = sub.add_parser("caso"); c.add_argument("codigo"); c.set_defaults(fn=cmd_caso)
    s = sub.add_parser("stats"); s.set_defaults(fn=cmd_stats)
    e = sub.add_parser("export"); e.add_argument("--csv", default="reglas.csv")
    e.set_defaults(fn=cmd_export)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
