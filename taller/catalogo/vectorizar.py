"""vectorizar.py: base SQLite vectorizada de los textos catalogados que aplican a GPT Image 2.

    python3 taller/catalogo/vectorizar.py [--modelos DIR]

Entran los textos no estructurales cuyo F29 es "TODOS" o incluye "GPT Image 2". Tablas:
- textos: clasificación completa de cada texto (naturaleza, aplicacion, destino, condición, excepto, alternativas…).
- facetas: una fila por (id, faceta, valor); "TODOS" marca que la regla no se restringe por esa faceta.
- embeddings: vector float32 normalizado de "passage: encabezado + texto" con intfloat/multilingual-e5-large
  (decisión 6 de DECISIONES.md). El vector depende solo del texto: reclasificar no obliga a revectorizar, y
  vectores_cache.npz evita recalcular los que no cambiaron.
- meta: modelo, dimensión, fecha, huella del catálogo y conteos.
"""
import argparse
import hashlib
import json
import sqlite3
import time
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
MODELO = "intfloat/multilingual-e5-large"
MODELO_ID = "GPT Image 2"


def aplica_gpt2(x):
    return x["naturaleza"] != "estructural" and (x["facetas"]["F29"] == "TODOS" or MODELO_ID in x["facetas"]["F29"])


def pasaje(x):
    return "passage: " + (x.get("encabezado") or "").strip() + "\n" + x["texto"].strip()


def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def vectores(textos, dir_modelos):
    cache_ruta = AQUI / "vectores_cache.npz"
    cache = dict(np.load(cache_ruta)) if cache_ruta.exists() else {}
    faltan = [t for t in textos if sha(t) not in cache]
    if faltan:
        from fastembed import TextEmbedding
        modelo = TextEmbedding(MODELO, cache_dir=dir_modelos)
        for t, v in zip(faltan, modelo.embed(faltan, batch_size=16)):
            v = np.asarray(v, dtype=np.float32)
            cache[sha(t)] = v / np.linalg.norm(v)
        np.savez_compressed(cache_ruta, **cache)
    return [cache[sha(t)] for t in textos], len(faltan)


def construir(dir_modelos=None, salida=AQUI / "catalogo_gpt2.sqlite"):
    inicio = time.monotonic()
    crudo = (AQUI / "catalogo_imagen_gpt2.json").read_text()
    catalogo = [x for x in json.loads(crudo) if aplica_gpt2(x)]
    vecs, nuevos = vectores([pasaje(x) for x in catalogo], dir_modelos)
    if salida.exists():
        salida.unlink()
    db = sqlite3.connect(salida)
    db.executescript("""
        CREATE TABLE textos (id TEXT PRIMARY KEY, archivo TEXT, encabezado TEXT, linea TEXT, texto TEXT,
            naturaleza TEXT, aplicacion TEXT, plantilla_destino TEXT, ambito TEXT, condicion TEXT, razon TEXT,
            excepto TEXT, excepto_texto TEXT, facetas_alternativas TEXT, biblioteca INTEGER, sha256 TEXT);
        CREATE TABLE facetas (id TEXT, faceta TEXT, valor TEXT);
        CREATE INDEX facetas_fv ON facetas (faceta, valor);
        CREATE TABLE embeddings (id TEXT PRIMARY KEY, modelo TEXT, dim INTEGER, vector BLOB);
        CREATE TABLE meta (clave TEXT PRIMARY KEY, valor TEXT);""")
    for x, v in zip(catalogo, vecs):
        db.execute("INSERT INTO textos VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            x["id"], x["archivo"], x.get("encabezado", ""), str(x.get("linea", "")), x["texto"], x["naturaleza"],
            x["aplicacion"], json.dumps(x["plantilla_destino"], ensure_ascii=False),
            json.dumps(x["ambito"], ensure_ascii=False), x["condicion"], x["razon"],
            json.dumps(x.get("excepto", {}), ensure_ascii=False),
            json.dumps(x.get("excepto_texto", []), ensure_ascii=False),
            json.dumps(x.get("facetas_alternativas", []), ensure_ascii=False),
            int(bool(x.get("biblioteca"))), sha(x["texto"])))
        for f, val in x["facetas"].items():
            for e in (["TODOS"] if val == "TODOS" else val):
                db.execute("INSERT INTO facetas VALUES (?,?,?)", (x["id"], f, e))
        db.execute("INSERT INTO embeddings VALUES (?,?,?,?)", (x["id"], MODELO, v.shape[0], v.tobytes()))
    conteos = {}
    for x in catalogo:
        conteos[x["aplicacion"]] = conteos.get(x["aplicacion"], 0) + 1
    meta = {"modelo": MODELO, "dim": str(vecs[0].shape[0]), "fecha": time.strftime("%Y-%m-%d %H:%M"),
            "catalogo_sha256": sha(crudo), "textos": str(len(catalogo)),
            "por_aplicacion": json.dumps(conteos, ensure_ascii=False)}
    db.executemany("INSERT INTO meta VALUES (?,?)", meta.items())
    db.commit()
    db.close()
    print(f"{salida.name}: {len(catalogo)} textos · vectores nuevos {nuevos} · {conteos} · "
          f"{time.monotonic() - inicio:.1f} s")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--modelos", help="carpeta de caché del modelo de embeddings")
    construir(ap.parse_args().modelos)
