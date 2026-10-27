"""verificar_veredictos.py: comprueba la lectura texto por texto de los 9,873 textos decididos por sección.

    python3 -I verificar_veredictos.py   → sale con código 1 ante cualquier falla

Cada línea de lectura_por_texto/veredictos.jsonl: {"n", "representante", "veredicto": "entra" | "sale",
"motivo", "cita"}. Comprobaciones:
  1. cobertura: cada grupo de cola.jsonl tiene exactamente un veredicto, y la suma de sus ids da los 9,873;
  2. el representante del veredicto es el del grupo n (no se puede asignar un veredicto al grupo equivocado);
  3. veredicto «entra» o «sale» y motivo no vacío;
  4. la cita está, carácter por carácter, en el texto del representante y tiene al menos 4 palabras, o es el texto
     completo si este tiene menos de 4. Un veredicto sin abrir el texto no pasa.
"""
import json
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent / "lectura_por_texto"


def main():
    cola = {g["n"]: g for g in map(json.loads, open(DIR / "cola.jsonl", encoding="utf-8"))}
    archivo = DIR / "veredictos.jsonl"
    veredictos = list(map(json.loads, open(archivo, encoding="utf-8"))) if archivo.exists() else []
    fallas, vistos = [], {}
    for v in veredictos:
        n = v.get("n")
        if n not in cola:
            fallas.append(f"n={n}: no existe en la cola")
            continue
        if n in vistos:
            fallas.append(f"n={n}: veredicto duplicado")
        vistos[n] = v
        g = cola[n]
        if v.get("representante") != g["representante"]:
            fallas.append(f"n={n}: representante {v.get('representante')} ≠ {g['representante']}")
        if v.get("veredicto") not in ("entra", "sale"):
            fallas.append(f"n={n}: veredicto «{v.get('veredicto')}»")
        if not (v.get("motivo") or "").strip():
            fallas.append(f"n={n}: motivo vacío")
        cita = v.get("cita") or ""
        if not cita or cita not in g["texto"]:
            fallas.append(f"n={n}: la cita no está literal en el texto")
        elif len(cita.split()) < min(4, len(g["texto"].split())):
            fallas.append(f"n={n}: cita de menos de 4 palabras")
    faltan = sorted(set(cola) - set(vistos))
    cubiertos = sum(len(cola[n]["ids"]) for n in vistos if n in cola)
    total = sum(len(g["ids"]) for g in cola.values())
    entra = sum(1 for v in vistos.values() if v.get("veredicto") == "entra")
    print(f"grupos {len(vistos)}/{len(cola)} · textos {cubiertos}/{total} · entra {entra} · sale {len(vistos) - entra}"
          f" · fallas {len(fallas)} · sin veredicto {len(faltan)}")
    for f in fallas[:50]:
        print("  ", f)
    if fallas or faltan:
        sys.exit(1)


if __name__ == "__main__":
    main()
