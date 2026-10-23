"""aplicar_amp.py: integra en las salidas de los 17 lotes la revisión con la taxonomía ampliada (2026-10-23).

Cada texto no estructural recibe sus valores finales de F04, F05, F06, F10, F15, F16, F17, F19, F23, las facetas
nuevas F33 y F34, y los campos excepto, excepto_texto, facetas_alternativas y biblioteca. Los estructurales
reciben los campos nuevos vacíos. Correr antes de f32/aplicar_f32.py.
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CAT = AQUI.parent
FAC = ["F04", "F05", "F06", "F10", "F15", "F16", "F17", "F19", "F23", "F33", "F34"]
NUEVOS = {"excepto": {}, "excepto_texto": [], "facetas_alternativas": [], "biblioteca": False}

amp = {}
for s in sorted(AQUI.glob("salida_amp_*.json")):
    lote = json.loads((AQUI / s.name.replace("salida_", "lote_")).read_text())
    sal = json.loads(s.read_text())
    assert [x["id"] for x in sal] == [u["id"] for u in lote], f"{s.name}: ids distintos al lote"
    amp.update({x["id"]: x for x in sal})

cambiados = 0
for s in sorted((CAT / "salidas").glob("salida_*.json")):
    sal = json.loads(s.read_text())
    for x in sal:
        if x["naturaleza"] == "estructural":
            x.update({k: (v.copy() if hasattr(v, "copy") else v) for k, v in NUEVOS.items()})
            continue
        assert x["id"] in amp, f"{x['id']}: sin revisión de ampliación"
        a = amp[x["id"]]
        antes = json.dumps({k: x["facetas"].get(k) for k in FAC[:-2]}, ensure_ascii=False, sort_keys=True)
        for k in FAC:
            x["facetas"][k] = a[k]
        for k in NUEVOS:
            x[k] = a[k]
        x["fuera_de_taxonomia"] = a["fuera_de_taxonomia"]
        cambiados += antes != json.dumps({k: x["facetas"][k] for k in FAC[:-2]}, ensure_ascii=False, sort_keys=True)
    s.write_text(json.dumps(sal, ensure_ascii=False, indent=1))
print(f"ampliación aplicada a {len(amp)} textos · con facetas cambiadas: {cambiados}")
