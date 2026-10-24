"""Consulta del índice de clasificaciones maestras.

python3 -I consultar_rag.py "escala universal especifica"            → 10 fragmentos más pertinentes (BM25)
python3 -I consultar_rag.py "luz dura" --fuente taxonomia-1019-esquema -k 20
python3 -I consultar_rag.py --id INV-002352                          → todo lo que cita ese id (también TRM-, DEC-, F04…)
python3 -I consultar_rag.py --fuentes                                 → fuentes, estado de autoridad y tamaño

Cada resultado muestra fuente, estado, ruta:línea y el texto literal, para comprobarlo en el archivo original.
"""
import argparse
import re
import sqlite3
import time
import unicodedata
from pathlib import Path

DB = Path(__file__).resolve().parent / "rag.sqlite"


def normal(s):
    return "".join(ch for ch in unicodedata.normalize("NFKD", s) if not unicodedata.combining(ch))


def consulta_fts(q):
    # cada palabra de 4 letras o más busca también por prefijo (español flexiona); OR entre palabras, BM25 ordena
    pal = [p for p in re.findall(r"\w+", normal(q).lower()) if p]
    return " OR ".join(f'"{p}"*' if len(p) >= 4 else f'"{p}"' for p in pal)


def imprimir(rows, t):
    for r in rows:
        fuente, estado, ruta, linea, tipo, enc, texto = r[:7]
        print(f"[{fuente} · {estado}] {ruta}:{linea or '-'} · {tipo}" + (f" · {enc}" if enc else ""))
        print("   " + texto.replace("\n", "\n   ")[:900])
    print(f"-- {len(rows)} resultados en {t * 1000:.1f} ms")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("q", nargs="?")
    ap.add_argument("-k", type=int, default=10)
    ap.add_argument("--fuente")
    ap.add_argument("--id")
    ap.add_argument("--fuentes", action="store_true")
    a = ap.parse_args()
    c = sqlite3.connect(DB)
    if a.fuentes:
        for r in c.execute("select fuente, estado, motivo_estado, count(*) from fragmentos group by fuente order by 4 desc"):
            print(f"{r[0]:26} {r[3]:6}  {r[1]} — {r[2]}")
        return
    t0 = time.perf_counter()
    sel = "select f.fuente, f.estado, f.ruta, f.linea, f.tipo, f.encabezado, f.texto from fragmentos f"
    if a.id:
        rows = c.execute(sel + " where f.texto like ? order by f.fuente, f.linea limit ?", (f"%{a.id}%", a.k * 10)).fetchall()
    else:
        w, p = "fts match ?", [consulta_fts(a.q)]
        if a.fuente:
            w += " and f.fuente = ?"
            p.append(a.fuente)
        rows = c.execute(sel + " join fts on fts.rowid = f.id where " + w + " order by bm25(fts) limit ?", p + [a.k]).fetchall()
    imprimir(rows, time.perf_counter() - t0)


if __name__ == "__main__":
    main()
