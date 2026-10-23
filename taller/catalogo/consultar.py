"""consultar.py: reglas del catálogo GPT Image 2 que aplican a un caso, sin llamar a ningún modelo de lenguaje.

Filtro duro por facetas (una faceta que el caso no define no filtra; F10 hereda del padre; `excepto` descarta;
`facetas_alternativas` son condiciones "o") y orden por similitud coseno entre el brief y cada texto.

    python3 taller/catalogo/consultar.py --facetas '{"F10":["génesis sin referencias (caso 1, T1)"], ...}' --brief "..."
"""
import argparse
import json
import sqlite3
import time
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
NO_FILTRAN = {"F29", "F30", "F31"}  # F29 ya se aplicó al construir la base; F30/F31 describen la regla
_modelo = None


def padres():
    tax = json.loads((AQUI / "taxonomia_f.json").read_text())["facetas"]
    return {k: v.get("padres", {}) for k, v in tax.items()}


def expandir(caso, mapa_padres):
    salida = {}
    for f, vals in caso.items():
        vals = set(vals)
        vals |= {mapa_padres.get(f, {})[v] for v in vals if v in mapa_padres.get(f, {})}
        salida[f] = vals
    return salida


def cumple(restricciones, caso):
    """restricciones: {faceta: set(valores)}; vale si toda faceta restringida que el caso define se cruza."""
    return all(f not in caso or (vals & caso[f]) for f, vals in restricciones.items())


def vectorizar_brief(texto, dir_modelos=None):
    global _modelo
    if _modelo is None:
        from fastembed import TextEmbedding
        _modelo = TextEmbedding("intfloat/multilingual-e5-large", cache_dir=dir_modelos)
    v = np.asarray(next(iter(_modelo.embed(["query: " + texto]))), dtype=np.float32)
    return v / np.linalg.norm(v)


def consultar(caso, brief, db_ruta=AQUI / "catalogo_gpt2.sqlite", dir_modelos=None):
    t0 = time.monotonic()
    caso = expandir({f: v for f, v in caso.items() if v}, padres())
    db = sqlite3.connect(db_ruta)
    restr = {}
    for i, f, v in db.execute("SELECT id, faceta, valor FROM facetas WHERE valor != 'TODOS'"):
        if f not in NO_FILTRAN:
            restr.setdefault(i, {}).setdefault(f, set()).add(v)
    filas = db.execute("SELECT t.id, t.aplicacion, t.naturaleza, t.texto, t.plantilla_destino, t.condicion, "
                       "t.excepto, t.facetas_alternativas, t.biblioteca, e.vector FROM textos t "
                       "JOIN embeddings e USING (id) WHERE t.aplicacion != 'SIN EFECTO NORMATIVO'").fetchall()
    t_filtro = time.monotonic()
    plantilla, candidatas = [], []
    for i, apl, nat, texto, destino, cond, excepto, alts, bib, vec in filas:
        excepto = {f: set(v) for f, v in json.loads(excepto).items()}
        if any(f in caso and (v & caso[f]) for f, v in excepto.items()):
            continue
        alternativas = [{f: set(v) for f, v in a.items()} for a in json.loads(alts)]
        if not (cumple(restr.get(i, {}), caso) or any(cumple(a, caso) for a in alternativas if a)):
            continue
        r = {"id": i, "aplicacion": apl, "naturaleza": nat, "texto": texto, "destino": json.loads(destino),
             "condicion": cond, "biblioteca": bool(bib), "_vec": vec}
        (plantilla if apl == "INCORPORADA A TEMPLATE" else candidatas).append(r)
    t_vec = time.monotonic()
    q = vectorizar_brief(brief, dir_modelos)
    t_rank = time.monotonic()
    for r in candidatas:
        r["similitud"] = round(float(np.frombuffer(r.pop("_vec"), dtype=np.float32) @ q), 4)
    for r in plantilla:
        r.pop("_vec")
    candidatas.sort(key=lambda r: -r["similitud"])
    fin = time.monotonic()
    return {"plantilla": plantilla, "candidatas": candidatas,
            "tiempos_s": {"lectura": round(t_filtro - t0, 3), "filtro": round(t_vec - t_filtro, 3),
                          "vector_brief": round(t_rank - t_vec, 3), "orden": round(fin - t_rank, 3),
                          "total": round(fin - t0, 3)}}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--facetas", required=True, help="JSON {faceta: [valores]} del caso")
    ap.add_argument("--brief", required=True)
    ap.add_argument("--modelos")
    ap.add_argument("--top", type=int, default=15)
    a = ap.parse_args()
    r = consultar(json.loads(a.facetas), a.brief, dir_modelos=a.modelos)
    por_apl = {}
    for x in r["candidatas"]:
        por_apl[x["aplicacion"]] = por_apl.get(x["aplicacion"], 0) + 1
    print(f"plantilla (universales): {len(r['plantilla'])} · candidatas: {len(r['candidatas'])} {por_apl} · "
          f"tiempos {r['tiempos_s']}")
    for x in r["candidatas"][:a.top]:
        print(f"  {x['similitud']:.3f} {x['id']} [{x['naturaleza']}] {x['texto'][:110]!r}")
