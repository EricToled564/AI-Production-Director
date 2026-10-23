"""Copia la interfaz del taller a public/taller/ para servirla dentro del proyecto de Vercel de la raíz del repo.

    python taller/sincronizar_publico.py

Se ejecuta después de cambiar taller/static/; una prueba falla si las copias no coinciden.
"""
import shutil
from pathlib import Path

TALLER = Path(__file__).resolve().parent
DESTINO = TALLER.parent / "public" / "taller"


def sincronizar():
    (DESTINO / "static").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(TALLER / "static" / "index.html", DESTINO / "index.html")
    for nombre in ("app.js", "style.css"):
        shutil.copyfile(TALLER / "static" / nombre, DESTINO / "static" / nombre)


if __name__ == "__main__":
    sincronizar()
    print("Interfaz copiada a", DESTINO)
