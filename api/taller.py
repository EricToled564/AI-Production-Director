"""Función de Vercel del proyecto raíz: sirve la API del taller en /taller/api/* (ver taller/nube.py)."""
import importlib.util
import sys
from pathlib import Path

_TALLER = Path(__file__).resolve().parent.parent / "taller"
sys.path.insert(0, str(_TALLER))
_spec = importlib.util.spec_from_file_location("taller_api_index", _TALLER / "api" / "index.py")
_modulo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_modulo)

handler = _modulo.handler
