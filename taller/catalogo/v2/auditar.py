"""auditar.py: estado medible de cada lote clasificado, sin modificar nada.

Por lote: cobertura y validador; y los defectos conocidos regla por regla:
  A. condiciones con valores que no salen de la taxonomía (campo que no es faceta ni campo tipado);
  B. aplicaciones repetidas que solo difieren en el flujo o la sección (compactables);
  C. "INCORPORADA A TEMPLATE" sin template verificado (§5.3 exige incorporación verificada);
  D. flujo y paso usados (para ver criterios distintos entre lotes).
"""
import collections
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
E = json.loads((AQUI / "esquema_taxonomia.json").read_text())
FACETAS, CAMPOS = set(E["facetas"]), set(E["campos"])


def atomos(g):
    for m in g["miembros"]:
        if "grupo" in m:
            yield from atomos(m)
        else:
            yield m


def huella(ap):
    a = dict(ap, ruta=dict(ap["ruta"], flujo=None, seccion=None), aplicacion_id=None)
    a["facetas"] = {k: v for k, v in ap["facetas"].items() if k != "P01"}
    return json.dumps(a, ensure_ascii=False, sort_keys=True)


filas = []
for lote in sorted((AQUI / "lotes").glob("lote_*.json")):
    n = lote.stem.split("_")[1]
    s = AQUI / "salidas" / f"salida_{n}.json"
    if not s.exists():
        filas.append((n, "SIN CLASIFICAR", {}))
        continue
    val = subprocess.run([sys.executable, "-I", str(AQUI / "validar_v2.py"), str(lote), str(s)],
                         capture_output=True, text=True).stdout.splitlines()[0]
    regs = json.loads(s.read_text())
    reglas = [r for r in regs if r["tipo_registro"] == "regla"]
    apps = [a for r in reglas for a in r["aplicaciones"]]
    libres = [(r["id"], m["campo"], m["valor"]) for r in reglas for a in r["aplicaciones"] if a["condicion"]
              for m in atomos(a["condicion"]) if m["campo"] not in FACETAS and m["campo"] not in CAMPOS]
    compactables = sum(len(a) - len({huella(x) for x in a}) for a in (r["aplicaciones"] for r in reglas))
    incorporadas = sum(1 for a in apps if a["uso_operativo"] == "INCORPORADA A TEMPLATE")
    flujos = collections.Counter(a["ruta"]["flujo"].split()[0] for a in apps)
    filas.append((n, val, {"reglas": len(reglas), "concil": len(regs) - len(reglas), "apps": len(apps),
                           "A_libres": len(libres), "B_compactables": compactables, "C_incorporadas": incorporadas,
                           "D_flujos": dict(flujos), "ej_libres": libres[:2]}))

print(f"{'lote':4} {'validador':10} reglas concil apps  A  B  C  flujos")
tot = collections.Counter()
for n, val, d in filas:
    if not d:
        print(f"{n:4} {val}")
        continue
    print(f"{n:4} {val[:10]:10} {d['reglas']:6} {d['concil']:6} {d['apps']:4} {d['A_libres']:2} {d['B_compactables']:3} "
          f"{d['C_incorporadas']:2}  {d['D_flujos']}")
    for k in ("reglas", "concil", "apps", "A_libres", "B_compactables", "C_incorporadas"):
        tot[k] += d[k]
    for e in d["ej_libres"]:
        print("      A:", e)
print("TOTAL", dict(tot), "· lotes clasificados", sum(1 for f in filas if f[2]), "de", len(filas))
