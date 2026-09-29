"""Vectoriza la lista final sin duplicados (4,093 registros menos dd_eliminado) con intfloat/multilingual-e5-large.

Controles:
  - los vectores se calculan sobre el texto literal de la base, sin tocarlo; solo para el modelo se antepone "passage: ";
  - se aborta si cambió una fuente desde 'congelar' (manifiesto) o si falta el cierre de la depuración;
  - se verifica: un vector por registro de la lista final, dimensión 1024, sin NaN, normas ≈ 1;
  - lo que el modelo no alcanza a leer (más de 512 tokens) se reporta, no se oculta.
Salida: data/vectores_e5.npz (ids, vectores) y data/vectores_e5.json (resumen). Solo lee de la base.
Uso: python3 tools/vectorizar.py
"""

from __future__ import annotations

import json
import sqlite3
import sys
import time
from pathlib import Path

import numpy as np

APD = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APD / "tools"))
import depurar_duplicados as dd  # noqa: E402

MODELO = "intfloat/multilingual-e5-large"
CACHE = "/tmp/fastembed_cache"
SALIDA = APD / "data/vectores_e5.npz"
RESUMEN = APD / "data/vectores_e5.json"


def main():
    dd.exigir_manifiesto()
    if not (dd.DIR / "final.json").exists():
        raise SystemExit("falta el cierre de la depuración (final.json)")
    c = sqlite3.connect(dd.DB)
    elim = {r for (r,) in c.execute("select id from dd_eliminado")}
    filas = [(i, t) for i, t in c.execute("select id, texto from registros order by orden") if i not in elim]
    esperado = json.loads((dd.DIR / "final.json").read_text(encoding="utf-8"))["lista_final"]
    if len(filas) != esperado:
        raise SystemExit(f"la lista final tiene {len(filas)} registros y final.json dice {esperado}")

    from fastembed import TextEmbedding
    modelo = TextEmbedding(MODELO, cache_dir=CACHE)
    tok = modelo.model.tokenizer if hasattr(modelo.model, "tokenizer") else None
    largos = 0
    if tok is not None:
        largos = sum(1 for _, t in filas if len(tok.encode("passage: " + t).ids) > 512)

    t0 = time.time()
    textos = ["passage: " + t for _, t in filas]
    # se ordena por longitud para no rellenar lotes con padding; el orden original se restituye después
    orden = sorted(range(len(textos)), key=lambda k: len(textos[k]))
    crudo = np.array(list(modelo.embed([textos[k] for k in orden], batch_size=16)), dtype=np.float32)
    raw = np.empty_like(crudo)
    raw[orden] = crudo
    seg = time.time() - t0
    np.savez_compressed(SALIDA.with_name("vectores_e5_crudos.npz"), ids=np.array([i for i, _ in filas]), vectores=raw)
    # el modelo ONNX de fastembed entrega vectores sin normalizar: se normalizan (L2) para usar coseno
    vec = raw / np.linalg.norm(raw, axis=1, keepdims=True)

    ids = np.array([i for i, _ in filas])
    assert vec.shape == (len(filas), 1024), vec.shape
    assert not np.isnan(vec).any(), "hay NaN"
    normas = np.linalg.norm(vec, axis=1)
    assert np.allclose(normas, 1.0, atol=1e-3), (normas.min(), normas.max())
    np.savez_compressed(SALIDA, ids=ids, vectores=vec)
    # relectura: lo guardado es lo calculado
    z = np.load(SALIDA, allow_pickle=False)
    assert (z["ids"] == ids).all() and np.array_equal(z["vectores"], vec)
    RESUMEN.write_text(json.dumps({
        "modelo": MODELO, "registros": len(filas), "dimension": 1024, "segundos": round(seg, 1),
        "mas_de_512_tokens": largos, "norma_min": float(normas.min()), "norma_max": float(normas.max()), "norma_cruda_min": float(np.linalg.norm(raw, axis=1).min()), "norma_cruda_max": float(np.linalg.norm(raw, axis=1).max())},
        ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"vectorizados {len(filas)} registros · dim 1024 · {seg:.0f} s · {largos} con más de 512 tokens (el modelo lee los primeros 512)")


if __name__ == "__main__":
    main()
