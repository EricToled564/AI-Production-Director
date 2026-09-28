"""Entrada de Vercel para la app nueva (apd/server.py). Toda ruta se reenvía aquí desde vercel.json.

Vercel no tiene disco escribible fuera de /tmp ni procesos persistentes:
- la base de reglas ya construida viaja en apd/deploy/rules.sqlite (no se reconstruye en cada arranque);
- la caché del paquete de skills original se extrae en /tmp;
- los proyectos van a Turso (TURSO_DATABASE_URL + TURSO_AUTH_TOKEN); sin ellos, a /tmp (se pierden al reiniciar);
- la API exige APP_PASSWORD.
"""

import os
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
os.environ.setdefault("APD_CACHE", "/tmp/apd-cache")
os.environ.setdefault("APD_RULES_DB", str(RAIZ / "apd" / "deploy" / "rules.sqlite"))
os.environ.setdefault("APD_DB", "/tmp/apd-proyectos.sqlite")
sys.path.insert(0, str(RAIZ / "apd"))

import server  # noqa: E402


class handler(server.H):
    pass
