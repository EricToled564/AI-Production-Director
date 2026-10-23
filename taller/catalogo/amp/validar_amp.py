"""validar_amp.py <lote> <salida>: cobertura, valores de la taxonomía ampliada y campos nuevos."""
import json
import sys
from pathlib import Path

CAT = Path(__file__).resolve().parent.parent
tax = json.loads((CAT / "taxonomia_f.json").read_text())["facetas"]
lote = json.loads(Path(sys.argv[1]).read_text())
sal = json.loads(Path(sys.argv[2]).read_text())
FAC = ["F04", "F05", "F06", "F10", "F15", "F16", "F17", "F19", "F23", "F33", "F34"]
CLAVES = ["id", *FAC, "excepto", "excepto_texto", "facetas_alternativas", "biblioteca", "fuera_de_taxonomia",
          "razon_cambio"]
err = []


def valores_ok(i, k, v, permitir_todos=True):
    if v == "TODOS" and permitir_todos:
        return
    if not isinstance(v, list) or not v:
        err.append(f"{i}: {k} debe ser 'TODOS' o lista no vacía")
        return
    if k not in tax:
        err.append(f"{i}: faceta inexistente {k}")
        return
    for val in v:
        if val not in tax[k]["valores"]:
            err.append(f"{i}: {k} valor fuera de la taxonomía: {val}")


if [x.get("id") for x in sal] != [u["id"] for u in lote]:
    err.append("los ids no coinciden con el lote")
for x in sal:
    i = x.get("id")
    if sorted(x) != sorted(CLAVES):
        err.append(f"{i}: claves {sorted(set(x) ^ set(CLAVES))}")
        continue
    for k in FAC:
        valores_ok(i, k, x[k])
    if not isinstance(x["excepto"], dict):
        err.append(f"{i}: excepto debe ser objeto")
    else:
        for k, v in x["excepto"].items():
            valores_ok(i, k, v, permitir_todos=False)
    if not isinstance(x["excepto_texto"], list):
        err.append(f"{i}: excepto_texto debe ser lista")
    if not isinstance(x["facetas_alternativas"], list):
        err.append(f"{i}: facetas_alternativas debe ser lista")
    else:
        for alt in x["facetas_alternativas"]:
            if not isinstance(alt, dict) or not alt:
                err.append(f"{i}: cada alternativa es un objeto no vacío")
                continue
            for k, v in alt.items():
                valores_ok(i, k, v, permitir_todos=False)
    if not isinstance(x["biblioteca"], bool):
        err.append(f"{i}: biblioteca debe ser true/false")
    if "EXT:" in json.dumps({k: x[k] for k in FAC}, ensure_ascii=False):
        err.append(f"{i}: quedan valores EXT")
    texto = json.dumps(x, ensure_ascii=False).lower()
    for p in ("pendiente", "propuesta", "duda", "desconocido", "no aplica"):
        if f'"{p}' in texto:
            err.append(f"{i}: estado prohibido '{p}'")
print("OK" if not err else "ERRORES:\n" + "\n".join(err[:60]))
