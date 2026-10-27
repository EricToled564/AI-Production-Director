"""corregir_cita.py: reemplaza la cita de veredictos ya anotados.  python3 -I corregir_cita.py fix.txt (n|cita)"""
import json
import sys
from pathlib import Path

archivo = Path(__file__).resolve().parent / "lectura_por_texto" / "veredictos.jsonl"
nuevas = {int(n): c for n, c in (l.rstrip("\n").split("|", 1) for l in open(sys.argv[1], encoding="utf-8") if l.strip())}
filas = [json.loads(l) for l in open(archivo, encoding="utf-8")]
for f in filas:
    if f["n"] in nuevas:
        f["cita"] = nuevas.pop(f["n"])
if nuevas:
    raise SystemExit(f"n sin veredicto: {sorted(nuevas)}")
archivo.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")
print("citas corregidas")
