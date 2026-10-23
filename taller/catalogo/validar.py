"""validar.py <lote.json> <salida.json>: cobertura total, valores de la taxonomía y ningún estado prohibido."""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
tax = json.loads((AQUI / "taxonomia_f.json").read_text())
lote = json.loads(Path(sys.argv[1]).read_text())
sal = json.loads(Path(sys.argv[2]).read_text())
CLAVES = ["id", "naturaleza", "aplicacion", "plantilla_destino", "ambito", "facetas", "condicion",
          "fuera_de_taxonomia", "razon"]
NAT = {"regla", "sintaxis", "ejemplo", "explicativo", "estructural"}
APL = {"INCORPORADA A TEMPLATE", "ACTIVO EN SELECCIÓN", "APLICACIÓN EN CONTROL O ENTREGA", "SIN EFECTO NORMATIVO"}
PROHIBIDAS = ("pendiente", "propuesta", "duda", "desconocido", "no aplica", "n/a", "tbd")
F = [f"F{i:02d}" for i in range(1, 33)]
err = []
if [x.get("id") for x in sal] != [u["id"] for u in lote]:
    err.append("los ids no coinciden con el lote (faltan, sobran o cambió el orden)")
for x in sal:
    i = x.get("id")
    if sorted(x) != sorted(CLAVES):
        err.append(f"{i}: claves {sorted(set(x) ^ set(CLAVES))}")
        continue
    nat, apl = x["naturaleza"], x["aplicacion"]
    if nat not in NAT:
        err.append(f"{i}: naturaleza {nat}")
    if apl not in APL:
        err.append(f"{i}: aplicacion {apl}")
    if (apl == "SIN EFECTO NORMATIVO") != (nat in ("explicativo", "estructural")):
        err.append(f"{i}: SIN EFECTO NORMATIVO solo y siempre para explicativo/estructural")
    for a in x["ambito"]:
        if a not in tax["AMBITO"]:
            err.append(f"{i}: ambito {a}")
    texto = json.dumps(x, ensure_ascii=False).lower()
    for p in PROHIBIDAS:
        if f'"{p}' in texto:
            err.append(f"{i}: estado prohibido '{p}'")
    fac = x["facetas"]
    if nat == "estructural":
        if fac:
            err.append(f"{i}: estructural lleva facetas vacías")
        continue
    if not x["ambito"]:
        err.append(f"{i}: ambito vacío")
    if sorted(fac) != F:
        err.append(f"{i}: faltan o sobran facetas {sorted(set(F) ^ set(fac))}")
        continue
    exts = 0
    for k in F:
        v = fac[k]
        if v == "TODOS":
            if k in ("F30", "F31"):
                err.append(f"{i}: {k} no puede ser TODOS")
            continue
        if not isinstance(v, list) or not v:
            err.append(f"{i}: {k} debe ser 'TODOS' o lista no vacía")
            continue
        for val in v:
            if isinstance(val, str) and val.startswith("EXT: "):
                exts += 1
            elif val not in tax["facetas"][k]["valores"]:
                err.append(f"{i}: {k} valor fuera de la taxonomía: {val}")
    if isinstance(fac.get("F31"), list) and len(fac["F31"]) != 1:
        err.append(f"{i}: F31 lleva exactamente un valor")
    if exts and not x["fuera_de_taxonomia"]:
        err.append(f"{i}: hay valores EXT sin explicar en fuera_de_taxonomia")
    if apl == "ACTIVO EN SELECCIÓN" and not x["condicion"].strip():
        err.append(f"{i}: falta condicion")
    if apl == "ACTIVO EN SELECCIÓN" and all(fac[k] == "TODOS" for k in F if k not in ("F30", "F31")):
        err.append(f"{i}: ACTIVO EN SELECCIÓN sin ninguna faceta restringida (¿es INCORPORADA A TEMPLATE?)")
    if len(x["razon"].split()) > 30:
        err.append(f"{i}: razon de más de 25 palabras")
print("OK" if not err else "ERRORES:\n" + "\n".join(err[:60]))
