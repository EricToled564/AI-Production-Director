"""aplicar_f32.py: integra la faceta F32 (texto en la imagen) en las salidas de los 17 lotes.

- Cada texto no estructural recibe el F32 decidido en f32/salida_f32_*.json (cobertura total obligatoria).
- Se retiran los marcadores provisionales EXT de "texto renderizado" que los lotes pusieron en otras facetas y
  sus entradas en fuera_de_taxonomia: la faceta nueva los sustituye. Una faceta que se queda vacía vuelve a TODOS.
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CAT = AQUI.parent
VALORES = set(json.loads((CAT / "taxonomia_f.json").read_text())["facetas"]["F32"]["valores"])
TEXTO_RENDER = re.compile(r"texto (o tipograf[ií]a )?renderizad|tipograf[ií]a renderizad", re.I)

f32 = {}
for s in sorted(AQUI.glob("salida_f32_*.json")):
    lote = json.loads((AQUI / s.name.replace("salida_", "lote_")).read_text())
    sal = json.loads(s.read_text())
    assert [x["id"] for x in sal] == [u["id"] for u in lote], f"{s.name}: ids distintos al lote"
    for x in sal:
        v = x["F32"]
        assert v == "TODOS" or (isinstance(v, list) and v and set(v) <= VALORES), f"{x['id']}: F32 inválido {v}"
        f32[x["id"]] = v

retirados = 0
for s in sorted((CAT / "salidas").glob("salida_*.json")):
    sal = json.loads(s.read_text())
    for x in sal:
        if x["naturaleza"] == "estructural":
            continue
        assert x["id"] in f32, f"{x['id']}: sin decisión de F32"
        for k, v in list(x["facetas"].items()):
            if isinstance(v, list):
                limpio = [e for e in v if not (isinstance(e, str) and e.startswith("EXT: ") and TEXTO_RENDER.search(e))]
                retirados += len(v) - len(limpio)
                x["facetas"][k] = limpio or "TODOS"
        x["fuera_de_taxonomia"] = [f for f in x["fuera_de_taxonomia"]
                                   if not TEXTO_RENDER.search(f.get("valor_necesario", "") + " " + f.get("faceta", ""))]
        x["facetas"]["F32"] = f32[x["id"]]
    s.write_text(json.dumps(sal, ensure_ascii=False, indent=1))
print(f"F32 aplicado a {len(f32)} textos · marcadores EXT de texto retirados: {retirados}")
