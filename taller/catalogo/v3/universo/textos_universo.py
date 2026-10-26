"""textos_universo.py: el texto de cada uno de los 2,722 textos del universo, listo para filtrar y clasificar.

    python3 -I textos_universo.py   → universo_prueba_textos.jsonl (una línea por texto, en el orden de universo_prueba.json)

La base de 13,005 textos no se modifica: está fijada por su sha256. Las correcciones que Eric decide viven en
correcciones.json y se aplican aquí, solo si el texto de la base sigue siendo el que se corrigió (sha256_original).
El encabezado sale de secciones.py, con la reparación de los 62 encabezados de image/SKILL.md y video/SKILL.md.
"""
import hashlib
import json
import sqlite3
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parents[1] / "corpus" / "BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite"


def main():
    universo = json.loads((AQUI / "universo_prueba.json").read_text(encoding="utf-8"))
    correcciones = {c["id"]: c for c in json.loads((AQUI / "correcciones.json").read_text(encoding="utf-8"))}
    verif = json.loads((AQUI / "verificacion_origen.json").read_text(encoding="utf-8"))
    encabezado_reparado = {f["id"]: f["reconstruido"] for f in verif["fallos"] if f["prueba"] == "D"}
    db = sqlite3.connect(f"file:{BASE}?mode=ro", uri=True)
    filas = {r[0]: r for r in db.execute("SELECT id, archivo, encabezado, linea_inicial, linea_final, texto FROM textos")}
    assert set(correcciones) <= set(universo), "corrección de un texto que no está en el universo"
    salida = []
    for i in universo:
        _, archivo, encabezado, li, lf, texto = filas[i]
        fila = {"id": i, "archivo": archivo, "encabezado": encabezado_reparado.get(i, encabezado),
                "linea_inicial": int(li), "linea_final": int(lf), "texto": texto, "corregido": False}
        c = correcciones.get(i)
        if c:
            assert hashlib.sha256(texto.encode("utf-8")).hexdigest() == c["sha256_original"] == \
                hashlib.sha256(c["texto_original"].encode("utf-8")).hexdigest(), f"{i}: el original cambió"
            fila.update(texto=c["texto_corregido"], corregido=True, texto_original=texto)
        salida.append(json.dumps(fila, ensure_ascii=False))
    (AQUI / "universo_prueba_textos.jsonl").write_text("\n".join(salida) + "\n", encoding="utf-8")
    print("textos", len(salida), "corregidos", len(correcciones), "encabezados reparados",
          sum(1 for i in universo if i in encabezado_reparado))


if __name__ == "__main__":
    main()
