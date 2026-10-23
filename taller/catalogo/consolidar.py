"""consolidar.py: une las salidas, comprueba cobertura total contra el universo y lista lo que va a discusión."""
import collections
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
universo = json.loads((AQUI / "universo_ids.json").read_text())
lotes = sorted((AQUI / "lotes").glob("lote_*.json"))
todos, faltan_lotes, errores = [], [], []
textos = {}
for l in lotes:
    s = AQUI / "salidas" / l.name.replace("lote_", "salida_")
    for u in json.loads(l.read_text()):
        textos[u["id"]] = u
    if not s.exists():
        faltan_lotes.append(l.name)
        continue
    r = subprocess.run([sys.executable, "-I", str(AQUI / "validar.py"), str(l), str(s)], capture_output=True, text=True)
    if r.stdout.strip() != "OK":
        errores.append(f"{l.name}: {r.stdout.strip()[:300]}")
    todos += json.loads(s.read_text())
ids = [x["id"] for x in todos]
print(f"universo {len(universo)} · catalogados {len(ids)} · únicos {len(set(ids))} · lotes sin salida {faltan_lotes}")
print("sin catalogar:", len(set(universo) - set(ids)), "· errores de validación:", errores or "ninguno")
print("naturaleza:", dict(collections.Counter(x["naturaleza"] for x in todos)))
print("aplicacion:", dict(collections.Counter(x["aplicacion"] for x in todos)))
gpt = [x for x in todos if x["facetas"] and (x["facetas"]["F29"] == "TODOS" or "GPT Image 2" in x["facetas"]["F29"])]
print("normativos que aplican a GPT Image 2:",
      dict(collections.Counter(x["aplicacion"] for x in gpt if x["aplicacion"] != "SIN EFECTO NORMATIVO")))
disc = collections.defaultdict(list)
for x in todos:
    for f in x["fuera_de_taxonomia"]:
        disc[(f.get("faceta", "?"), f.get("valor_necesario", "?"))].append(x["id"])
print(f"\nPARA DISCUTIR ({len(disc)} necesidades, {sum(len(v) for v in disc.values())} textos):")
for (fac, val), v in sorted(disc.items(), key=lambda kv: -len(kv[1])):
    print(f"  {fac} · {val} · {len(v)} textos · ej. {v[0]}")
if "--escribir" in sys.argv:
    salida = [dict(x, texto=textos[x["id"]]["texto"], archivo=textos[x["id"]]["archivo"],
                   encabezado=textos[x["id"]]["encabezado"], linea=textos[x["id"]]["linea_inicial"]) for x in todos]
    (AQUI / "catalogo_imagen_gpt2.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1))
    print("escrito catalogo_imagen_gpt2.json")
