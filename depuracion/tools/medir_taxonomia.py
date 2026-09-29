"""Mide la condición de revisión de la taxonomía (decisión 10): ¿alguna regla no encaja en ningún valor?
¿algún valor queda sin reglas? Usa los vectores de la lista final y un vector por valor de la taxonomía
(faceta + valor + definición) con multilingual-e5-large; umbral 0.80 (el de METODO.md para asignar por similitud)."""
import json, re, sqlite3, sys
from pathlib import Path
import numpy as np
APD = Path(__file__).resolve().parents[1]
UMBRAL = 0.80
T = (APD / "TAXONOMIA.md" if (APD / "TAXONOMIA.md").exists() else APD.parent / ".claude/rules/TAXONOMIA.md").read_text(encoding="utf-8")
valores = []  # (faceta, valor, definicion)
for b in re.split(r"\n### ", T)[1:]:
    b = b.split("\n## ")[0]
    cab = b.split("\n", 1)[0]
    faceta = cab.split(" — ")[0].split(" (")[0].strip()
    filas = [l for l in b.split("\n") if l.startswith("|") and not l.startswith("|---")]
    if not filas:
        continue
    hdr = [c.strip() for c in filas[0].strip("|").split("|")]
    for f in filas[1:]:
        cel = [c.strip() for c in f.strip("|").split("|")]
        if hdr[0] == "Etapa":          # faceta 2: pasos separados por ·
            for x in cel[1].split("·"):
                valores.append((faceta, x.strip(), f"paso de la etapa {cel[0]}"))
        elif hdr[:2] == ["Rama", "Valores"]:   # faceta 29
            for x in cel[1].split("·"):
                valores.append((faceta, x.strip(), f"modelo de {cel[0].lower()}"))
        elif hdr[0] == "Rama":         # faceta 10: rama, valor, definición
            valores.append((faceta, cel[1], f"{cel[0]}: {cel[2]}"))
        else:
            valores.append((faceta, cel[0], cel[1] if len(cel) > 1 else ""))
print(len(valores), "valores en", len({f for f, _, _ in valores}), "facetas")
from fastembed import TextEmbedding
m = TextEmbedding("intfloat/multilingual-e5-large", cache_dir="/tmp/fastembed_cache")
P = np.array(list(m.embed([f"passage: {f}: {v}. {d}" for f, v, d in valores], batch_size=16)), dtype=np.float32)
P /= np.linalg.norm(P, axis=1, keepdims=True)
z = np.load(APD / "data/vectores_e5.npz", allow_pickle=False)
V, ids = z["vectores"], [str(i) for i in z["ids"]]
S = V @ P.T
c = sqlite3.connect(APD / "data/rules.sqlite")
texto = dict(c.execute("select id, texto from registros"))
doc = {}
for rid, a in c.execute("select registro_id, archivo from registros_fuente"):
    doc.setdefault(rid, a)
mejor = S.max(axis=1)
sin_valor = [i for i in range(len(ids)) if mejor[i] < UMBRAL]
cuenta = (S >= UMBRAL).sum(axis=0)
sin_reglas = [k for k in range(len(valores)) if cuenta[k] == 0]
print(f"similitud máxima por regla: min {mejor.min():.3f} · mediana {np.median(mejor):.3f} · max {mejor.max():.3f}")
print(f"reglas cuya mejor similitud con TODOS los valores es < {UMBRAL}: {len(sin_valor)} de {len(ids)}")
print(f"valores sin ninguna regla con similitud >= {UMBRAL}: {len(sin_reglas)} de {len(valores)}")
for k in sin_reglas:
    print("  SIN REGLAS:", valores[k][0], "·", valores[k][1], f"(mejor regla {S[:,k].max():.3f})")
por_doc = {}
for i in sin_valor:
    por_doc[doc.get(ids[i], "?")] = por_doc.get(doc.get(ids[i], "?"), 0) + 1
print("reglas sin valor, por documento (top 8):", sorted(por_doc.items(), key=lambda x: -x[1])[:8])
for i in sin_valor[:6]:
    print("  EJEMPLO:", f"{mejor[i]:.3f}", repr(texto[ids[i]][:110]))
json.dump({"umbral": UMBRAL, "reglas": len(ids), "valores": len(valores),
           "reglas_sin_valor": [ids[i] for i in sin_valor],
           "valores_sin_reglas": [{"faceta": valores[k][0], "valor": valores[k][1], "mejor": float(S[:, k].max())} for k in sin_reglas]},
          open(APD / "data/medicion_taxonomia.json", "w"), ensure_ascii=False, indent=1)
