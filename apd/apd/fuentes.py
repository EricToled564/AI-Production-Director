"""Rutas, hashes y procedencia de las fuentes originales.

Regla de la app: los originales no se tocan. El zip entregado vive en
`apd/originales/` en solo lectura; el repo original (commit REPO_COMMIT) se lee
en su lugar y cada archivo usado queda con su sha256 en `data/inventario.json`.
Todo lo transformado se escribe en `apd/data/` como archivo nuevo.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import zipfile
from pathlib import Path

APD = Path(__file__).resolve().parent.parent          # .../apd
REPO = APD.parent                                       # raíz del repo original
DATA = APD / "data"
CACHE = APD / ".cache"
ORIGINALES = APD / "originales"

ZIP_NOMBRE = "AI_Production_Director_v3.4.0_COMPLETE.zip"
ZIP = ORIGINALES / ZIP_NOMBRE
ZIP_SHA256 = "5c55b7886d7e8955be52144f002f1e8b0c8254de6ea846bfbb944fe5242111dc"
PKG = CACHE / "pkg" / "AI_Production_Director_v3.4.0_COMPLETE"
REPO_COMMIT = "e61005ddce19040ca6f913ee0b0de260de6b65f3"

RULES_DB = DATA / "rules.sqlite"
HOOKS = REPO / ".claude" / "hooks"

# Fuentes que el prompt de encargo nombra y que NO se entregaron como archivo.
# Se declaran para no afirmar cobertura de su texto.
FUENTES_NOMBRADAS = [
    {"nombre": "AI-Production-Director-completo.zip", "estado": "SUSTITUIDA",
     "detalle": "Se entregó AI_Production_Director_v3.4.0_COMPLETE.zip (contiene original_source/"
                "aiproductiondirectorcompleto.zip) y el repo en el commit " + REPO_COMMIT[:7] + "."},
    {"nombre": "rules.sqlite", "estado": "RECONSTRUIDA",
     "detalle": "No venía como archivo. Se reconstruye con el constructor original "
                ".claude/hooks/rules_v3.py (sin modificar) sobre los skills del zip + "
                ".claude/rules/regimenes del repo. Resultado: 1,398 reglas, igual al conteo "
                "declarado; no se puede comparar byte a byte con la base del usuario."},
    {"nombre": "scratchpad-completo.zip", "estado": "ENTREGADA_PARCIAL",
     "detalle": "Entregada (sha256 5b63cc64…). USADO: t1.sqlite — 1,398/1,398 ids del registro con texto "
                "idéntico; sus 7 reglas extra son la fixture 99-fixture-prueba.md; en facetas coincide en 5,307 "
                "filas y no trae las 3,415 facetas origen llm que sí tiene el registro reconstruido (instantánea "
                "anterior). flujo-anclas.html/flujo-spot.html del zip son copias de los entregados. NO USADO como "
                "fuente normativa: f07/ f08/ f09/ (páginas web descargadas), reddit/, vivaldi/ (frames de 984 bytes y "
                "audio), reg/*.json (registros legacy por skill), app_clasificacion.json y llm_classify/ (su efecto "
                "ya está en regla_faceta origen llm), scripts de sesión y capturas."},
    {"nombre": "flujo-anclas.html", "estado": "ENTREGADA",
     "detalle": "Entregada (sha256 08dc81cc…). Transcrita en apd/flujos.py con cita literal verificada: "
                "tarjeta D1–D9, D9 por acción, pasos A0–A12, motion brief, roles de referencia."},
    {"nombre": "flujo-spot.html", "estado": "ENTREGADA",
     "detalle": "Entregada (sha256 a18c2094…). Transcrita en apd/flujos.py con cita literal verificada: "
                "etapas por track, dependencias, gates E0/E1/E2/E4, subprocesos Nivel 2."},
]


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def canon_json(o) -> str:
    return json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def verificar_zip() -> str:
    if not ZIP.is_file():
        raise SystemExit(f"falta el original {ZIP}")
    h = sha256_file(ZIP)
    if h != ZIP_SHA256:
        raise SystemExit(f"el zip original cambió: {h} != {ZIP_SHA256}")
    return h


def extraer_paquete() -> Path:
    """Extrae el zip a la caché (una vez). Nunca se escribe dentro de originales/."""
    verificar_zip()
    marca = PKG / ".extraido"
    if not marca.exists():
        (CACHE / "pkg").mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(ZIP) as z:
            z.extractall(CACHE / "pkg")
        marca.write_text(ZIP_SHA256)
    return PKG


def skills_root() -> Path:
    """Raíz para FUPAI_SKILLS_ROOT: rule_registry busca `<root>/*/<skill>`."""
    return extraer_paquete()


def git_blob(path: Path) -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(REPO), "rev-parse", f"{REPO_COMMIT}:{path.relative_to(REPO)}"],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or None
    except Exception:
        return None


def env_constructor() -> dict:
    env = dict(os.environ)
    env["FUPAI_SKILLS_ROOT"] = str(skills_root())
    return env
