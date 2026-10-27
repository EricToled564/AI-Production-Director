"""anotar.py: añade veredictos de lectura a lectura_por_texto/veredictos.jsonl.

    python3 -I anotar.py lote.txt

Cada línea de lote.txt: n|entra o sale|motivo|cita. La cita la escribe quien lee, copiada del texto; el representante
se toma de la cola por n. Un n ya anotado se rechaza. verificar_veredictos.py comprueba después cita y cobertura.
"""
import json
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent / "lectura_por_texto"
cola = {g["n"]: g for g in map(json.loads, open(DIR / "cola.jsonl", encoding="utf-8"))}
archivo = DIR / "veredictos.jsonl"
hechos = {json.loads(l)["n"] for l in open(archivo, encoding="utf-8")} if archivo.exists() else set()
nuevos = []
for linea in open(sys.argv[1], encoding="utf-8"):
    if not linea.strip():
        continue
    n, veredicto, motivo, cita = linea.rstrip("\n").split("|", 3)
    n = int(n)
    if n in hechos:
        raise SystemExit(f"n={n} ya tiene veredicto")
    hechos.add(n)
    nuevos.append({"n": n, "representante": cola[n]["representante"], "veredicto": veredicto.strip(),
                   "motivo": motivo.strip(), "cita": cita.strip()})
with open(archivo, "a", encoding="utf-8") as f:
    for v in nuevos:
        f.write(json.dumps(v, ensure_ascii=False) + "\n")
print(f"{len(nuevos)} veredictos añadidos")
