#!/usr/bin/env python3
"""Antes/después sobre un prompt REAL del repo: produccion/vivaldi-invierno/output/genesis/T2_vera.txt.
Aplica los controles de secciones y contradicciones de la app al texto tal como se entregó."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from apd import auditoria as A, fuentes as F

casos = []
md = F.REPO / "produccion/vivaldi-invierno/05-genesis-anclas.md"
bloque = md.read_text(encoding="utf-8").split("### T2 · Vera")[1].split("```")[1]
t_md = bloque.split("Prompt:")[1].split("Notes:")[0].strip()
casos.append((md, t_md, "bloque T2 · Vera documentado en 05-genesis-anclas.md (HEAD)"))
txt = F.REPO / "produccion/vivaldi-invierno/output/genesis/T2_vera.txt"
casos.append((txt, txt.read_text(encoding="utf-8"), "archivo T2_vera.txt corregido a mano (commit 24cb0c3)"))
etiquetas = ["Scene:", "Subject:", "Important Details:", "Use Case:", "Constraints:"]
res = []
for p, t, que in casos:
    dup = {e: t.count(e) for e in etiquetas if t.count(e) > 1}
    contr = [d for a, b, d in A.CONTRADICCIONES if A.afirmado(a, t) and A.afirmado(b, t)]
    res.append({"fuente": str(p.relative_to(F.REPO)), "que": que, "sha256_archivo": F.sha256_file(p),
                "palabras": len(t.split()), "secciones_duplicadas": dup, "contradicciones": contr,
                "veredicto_app": "BLOQUEADO" if dup or contr else "PASA controles de estructura"})
print(json.dumps(res, ensure_ascii=False, indent=1))
