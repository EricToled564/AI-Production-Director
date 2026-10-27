"""cola_lectura.py: cola de lectura texto por texto de los 9,873 textos que se decidieron por sección.

    python3 -I cola_lectura.py   → lectura_por_texto/cola.jsonl

Alcance (Eric, 2026-10-27, DECISIONES_ERIC_20261024.md §1): entran los textos de generación de imágenes universales,
parcialmente universales que incluyen GPT Image 2, y los específicos de GPT Image 2; todo lo demás queda fuera.

Las secciones «fuera» y «otro_modelo» de decision_secciones.json se decidieron leyendo documento y encabezado, no
texto por texto. Aquí cada texto pasa a la cola. Los que repiten texto, sección y nombre de archivo (copias idénticas,
p. ej. los mismos tools/ en cuatro skills) forman un grupo: se lee el primero y el veredicto vale para todo el grupo.
Cada línea: n, representante, ids del grupo, archivo, sección, estado de la sección, encabezado y texto.
"""
import json
import sqlite3
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parents[1] / "corpus" / "BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite"


def main():
    secciones = json.loads((AQUI / "decision_secciones.json").read_text(encoding="utf-8"))
    con = sqlite3.connect(BASE)
    textos = {r[0]: r[1:] for r in con.execute("select id, texto, encabezado, archivo from textos")}
    grupos = {}
    for s in secciones:
        if s["estado"] not in ("fuera", "otro_modelo"):
            continue
        for i in s["ids"]:
            texto, encabezado, archivo = textos[i]
            clave = (texto, s["seccion"], archivo.split("/")[-1])
            g = grupos.setdefault(clave, {"representante": i, "ids": [], "archivo": archivo, "seccion": s["seccion"],
                                          "estado_seccion": s["estado"], "encabezado": encabezado, "texto": texto})
            g["ids"].append(i)
    salida = AQUI / "lectura_por_texto"
    salida.mkdir(exist_ok=True)
    with open(salida / "cola.jsonl", "w", encoding="utf-8") as f:
        for n, g in enumerate(grupos.values(), 1):
            f.write(json.dumps({"n": n, **g}, ensure_ascii=False) + "\n")
    total = sum(len(g["ids"]) for g in grupos.values())
    print(f"{len(grupos)} grupos a leer · {total} textos cubiertos")


if __name__ == "__main__":
    main()
