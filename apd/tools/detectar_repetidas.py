"""Detecta reglas repetidas: registros distintos que dicen lo mismo con otras palabras.

Paso 1 (vectores): cada registro (su contenido, sin la ruta de sección) se vectoriza con
intfloat/multilingual-e5-large, el mismo modelo de la base. Candidatos = pares con coseno ≥ --umbral
entre los --k vecinos más cercanos. Los candidatos se agrupan por componentes conexas.
Paso 2 (juez): un modelo LLM recibe cada grupo candidato con el texto completo y la ubicación de cada
registro y devuelve subgrupos de registros que establecen la MISMA regla, indicando cuál es la versión
más completa y qué añade cada una. Nada se borra: el resultado se guarda en la tabla registros_repetidas.

Uso:
  python3 tools/detectar_repetidas.py vectores            # calcula y guarda data/registros_e5.npz
  python3 tools/detectar_repetidas.py candidatos --umbral 0.90 --k 10
  python3 tools/detectar_repetidas.py juzgar              # necesita OPENAI_API_KEY / OPENAI_MODEL
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

import numpy as np

APD = Path(__file__).resolve().parents[1]
DB = APD / "data/rules.sqlite"
NPZ = APD / "data/registros_e5.npz"
CAND = APD / "data/repetidas_candidatos.json"
CACHE_JUEZ = APD / "data/repetidas_juez_cache"


def registros():
    con = sqlite3.connect(DB)
    regs = con.execute("select id, texto from registros order by orden").fetchall()
    ubic = {}
    for rid, arch, li, lf, sec in con.execute(
            "select registro_id, archivo, linea_ini, linea_fin, seccion from registros_fuente"):
        ubic.setdefault(rid, []).append(f"{arch}:{li}-{lf} [{sec}]")
    con.close()
    return regs, ubic


def contenido(t: str) -> str:
    return t.split("] ", 1)[1] if t.startswith("[") and "] " in t else t


def cmd_vectores(_a):
    from fastembed import TextEmbedding
    regs, _ = registros()
    modelo = TextEmbedding("intfloat/multilingual-e5-large",
                           cache_dir=os.environ.get("FASTEMBED_CACHE_PATH", "/tmp/fastembed_cache"))
    textos = ["passage: " + re.sub(r"\s+", " ", contenido(t))[:2000] for _, t in regs]
    vec = np.array(list(modelo.embed(textos, batch_size=16)), dtype=np.float32)
    vec /= np.linalg.norm(vec, axis=1, keepdims=True)
    np.savez_compressed(NPZ, ids=np.array([r for r, _ in regs]), vectores=vec)
    print(f"{len(regs)} registros vectorizados → {NPZ}")


def cmd_candidatos(a):
    regs, ubic = registros()
    d = np.load(NPZ)
    ids = list(d["ids"])
    V = d["vectores"]
    pos = {r: i for i, r in enumerate(ids)}
    texto = {r: t for r, t in regs}
    S = V @ V.T
    np.fill_diagonal(S, -1)
    pares = []
    for i in range(len(ids)):
        vecinos = np.argsort(-S[i])[:a.k]
        for j in vecinos:
            if S[i, j] >= a.umbral and i < j:
                pares.append((i, int(j), float(S[i, j])))
    # componentes conexas
    padre = list(range(len(ids)))

    def raiz(x):
        while padre[x] != x:
            padre[x] = padre[padre[x]]
            x = padre[x]
        return x
    for i, j, _ in pares:
        padre[raiz(i)] = raiz(j)
    grupos = {}
    for i, j, _ in pares:
        grupos.setdefault(raiz(i), set()).update((i, j))
    out = []
    for g in grupos.values():
        miembros = sorted(g)
        out.append({"miembros": [{"id": ids[m], "texto": texto[ids[m]], "ubicacion": ubic.get(ids[m], [])}
                                 for m in miembros],
                    "sim_max": max(s for i, j, s in pares if i in g and j in g)})
    out.sort(key=lambda g: -len(g["miembros"]))
    CAND.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    tam = [len(g["miembros"]) for g in out]
    print(f"umbral {a.umbral} · k {a.k}: {len(pares)} pares · {len(out)} grupos candidatos · "
          f"{sum(tam)} registros implicados · tamaño máx {max(tam) if tam else 0}")


SIS_JUEZ = """Eres auditor de una base de reglas de producción audiovisual con IA. Recibes un grupo de registros
candidatos (texto completo + ubicación). Decide cuáles establecen LA MISMA REGLA aunque estén redactados distinto.

Criterio estricto:
- MISMA regla = misma obligación, prohibición, límite o instrucción de sintaxis, con el mismo alcance. Un registro
  puede ser más completo que otro (añade ejemplos o razones) y sigue siendo la misma regla.
- NO es la misma regla si cambia el alcance (otro modelo, otro caso, otra etapa), el valor (3-4 elementos vs 5-7),
  o si solo comparten tema. En ese caso, si el contenido normativo es idéntico pero el alcance declarado es otro
  modelo o contexto, márcalo como "misma_regla_otro_alcance".
- Un ejemplo que aplica una regla NO es repetición de la regla.

Devuelve JSON: {"grupos": [{"ids": [...], "relacion": "misma_regla" | "misma_regla_otro_alcance",
"mas_completo": "<id>", "regla_en_una_frase": "...", "diferencias": "qué añade o cambia cada id respecto al más completo"}]}
Incluye solo subgrupos de 2 o más ids. Si ninguno repite, devuelve {"grupos": []}. Usa solo ids del grupo recibido."""


def cmd_juzgar(a):
    sys.path.insert(0, str(APD))
    from apd import llm
    grupos = json.loads(CAND.read_text(encoding="utf-8"))
    CACHE_JUEZ.mkdir(parents=True, exist_ok=True)
    resultados = []
    for n, g in enumerate(grupos):
        ids_g = [m["id"] for m in g["miembros"]]
        # grupos grandes se parten en bloques de 12 por orden de similitud interna para caber en contexto
        bloques = [g["miembros"][i:i + 12] for i in range(0, len(g["miembros"]), 12)] if len(g["miembros"]) > 12 \
            else [g["miembros"]]
        for b_i, b in enumerate(bloques):
            clave = "-".join(sorted(m["id"] for m in b))
            f = CACHE_JUEZ / (str(abs(hash(clave)) % 10**12) + ".json")
            if f.exists():
                r = json.loads(f.read_text(encoding="utf-8"))
            else:
                user = json.dumps([{"id": m["id"], "ubicacion": m["ubicacion"], "texto": m["texto"]} for m in b],
                                  ensure_ascii=False)
                r = None
                for intento in range(3):
                    try:
                        r = llm.extraer_json(llm.proveedor().completar(SIS_JUEZ, user)["texto"])
                        break
                    except Exception as e:  # noqa: BLE001
                        print("reintento", n, b_i, e, file=sys.stderr)
                if r is None:
                    print(f"FALLA grupo {n}", file=sys.stderr)
                    sys.exit(1)
                validos = {m["id"] for m in b}
                r["grupos"] = [x for x in r.get("grupos", []) if len(set(x.get("ids", [])) & validos) >= 2]
                for x in r["grupos"]:
                    x["ids"] = [i for i in x["ids"] if i in validos]
                f.write_text(json.dumps(r, ensure_ascii=False), encoding="utf-8")
            resultados.extend(r["grupos"])
        print(f"grupo {n + 1}/{len(grupos)} juzgado", file=sys.stderr, flush=True)
    con = sqlite3.connect(DB)
    con.executescript("""DROP TABLE IF EXISTS registros_repetidas;
        CREATE TABLE registros_repetidas (grupo TEXT NOT NULL, registro_id TEXT NOT NULL, relacion TEXT NOT NULL,
            es_mas_completo INTEGER NOT NULL, regla TEXT, diferencias TEXT);""")
    for k, x in enumerate(resultados, 1):
        gid = f"REP-{k:04d}"
        for rid in x["ids"]:
            con.execute("insert into registros_repetidas values (?,?,?,?,?,?)",
                        (gid, rid, x.get("relacion", "misma_regla"), int(rid == x.get("mas_completo")),
                         x.get("regla_en_una_frase"), x.get("diferencias")))
    con.commit()
    n_misma = sum(1 for x in resultados if x.get("relacion") == "misma_regla")
    print(f"{len(resultados)} grupos de repetidas ({n_misma} misma regla, {len(resultados) - n_misma} misma regla con otro alcance) · "
          f"{sum(len(x['ids']) for x in resultados)} registros")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("vectores")
    c = sub.add_parser("candidatos")
    c.add_argument("--umbral", type=float, default=0.90)
    c.add_argument("--k", type=int, default=10)
    sub.add_parser("juzgar")
    a = ap.parse_args()
    {"vectores": cmd_vectores, "candidatos": cmd_candidatos, "juzgar": cmd_juzgar}[a.cmd](a)


if __name__ == "__main__":
    main()
