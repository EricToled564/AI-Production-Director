"""secciones.py: sección de cada uno de los 13,005 textos = documento + ruta de encabezados.

    python3 -I secciones.py   → secciones.json (una fila por sección, con sus ids) y secciones.txt (para leer)

Los textos de .md y .tpl traen su encabezado en la base original. Los que no lo traen se ubican así:
- flujos/*.html: por el último marcador de sección del propio documento («Nivel …», «Paso …» o fila de etapa
  «| E0 |» a «| E7 |» y «| POST |») que aparece antes de la línea;
- .json, .py, .sh, .txt, licencias y avisos: el documento completo es la sección.
"""
import json
import re
import sqlite3
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parents[1] / "corpus" / "BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite"
MARCA = re.compile(r"^(Nivel [0-9][^\n]*|Paso [0-9][^\n]*|\| (E[0-7]|POST) \|[^|\n]*\|[^|\n]*)")


def main():
    db = sqlite3.connect(f"file:{BASE}?mode=ro", uri=True)
    filas = db.execute("SELECT id, archivo, encabezado, CAST(linea_inicial AS INTEGER), texto FROM textos "
                       "ORDER BY archivo, 4, id").fetchall()
    secciones, actual = {}, {}
    for i, a, e, l, t in filas:
        if e.strip():
            s = e.strip()
        elif a.startswith("flujos/"):
            m = MARCA.match(t.strip())
            if m:
                actual[a] = re.sub(r"\s+", " ", m.group(1)).strip(" |")
            s = actual.get(a, "(inicio del documento)")
        else:
            s = "(documento completo)"
        d = secciones.setdefault((a, s), {"archivo": a, "seccion": s, "ids": [], "primera_linea": l})
        d["ids"].append(i)
    out = list(secciones.values())
    assert sum(len(d["ids"]) for d in out) == 13005
    (AQUI / "secciones.json").write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    txt = [f"{n:4} | {d['archivo']} | L{d['primera_linea']} | {len(d['ids'])} | {d['seccion']}" for n, d in enumerate(out, 1)]
    (AQUI / "secciones.txt").write_text("\n".join(txt) + "\n", encoding="utf-8")
    print("secciones", len(out), "textos", sum(len(d["ids"]) for d in out))


if __name__ == "__main__":
    main()
