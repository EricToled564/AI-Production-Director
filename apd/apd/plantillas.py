"""Catálogo de plantillas y estructuras realmente disponibles en los originales.

Cada entrada se EXTRAE del archivo en cada build (no se copia a mano): si el
encabezado no está o el bloque cambió, el sha256 cambia y el catálogo lo muestra.
`estado` distingue ORIGINAL, SOURCE_RECONSTRUCTED (el propio paquete declara que
reconstruyó un archivo histórico ausente) y NUEVA (propuesta de esta app).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from . import fuentes as F

SK = "skills"  # relativo a PKG

CATALOGO = [
    # id, archivo (relativo a PKG o REPO), encabezado, bloque, estado, casos, modelos, etapas
    {"id": "gpt5slot", "nombre": "GPT Image 2 — estructura de 5 slots",
     "archivo": "skills/image/references/gpt-image.md", "encabezado": "## Структура промпта — 5 slots",
     "estado": "ORIGINAL", "casos": ["T1", "T2", "T3", "T4", "PROD", "GRAF"], "modelos": ["gpt-image-2"],
     "etapas": ["PROMPT_IMAGEN", "E5.2", "E5.3", "E5.4"]},
    {"id": "gpt_editorial", "nombre": "GPT Image 2 — Photoreal Editorial",
     "archivo": "skills/image/references/gpt-image.md", "encabezado": "### Photoreal Editorial",
     "estado": "ORIGINAL", "casos": ["T1", "T3"], "modelos": ["gpt-image-2"], "etapas": ["PROMPT_IMAGEN", "E5.2"]},
    {"id": "gpt_edit", "nombre": "GPT Image 2 — edición Change/Preserve/Constraints",
     "archivo": "skills/image/references/gpt-image.md", "encabezado": "## Editing — двухколоночная логика",
     "estado": "ORIGINAL", "casos": ["T5"], "modelos": ["gpt-image-2"], "etapas": ["E5.5"]},
    {"id": "gpt_multiref", "nombre": "GPT Image 2 — multi-imagen con rol",
     "archivo": "skills/image/references/gpt-image.md", "encabezado": "## Multi-Image — до 16 рефов",
     "estado": "ORIGINAL", "casos": ["T2", "T3", "T4"], "modelos": ["gpt-image-2"], "etapas": ["E5.3", "E5.4"]},
    {"id": "nb_multiref", "nombre": "Nano Banana — multi-referencia",
     "archivo": "skills/image/references/nano-banana.md", "encabezado": "### Multi-Reference",
     "estado": "ORIGINAL", "casos": ["T2", "T3", "T4", "ENSAMBLE"], "modelos": ["nano-banana-2", "nano-banana-pro"],
     "etapas": ["E5.3", "E5.4"]},
    {"id": "nb_json", "nombre": "Nano Banana — JSON para escenas de 5+ elementos",
     "archivo": "skills/image/references/nano-banana.md", "encabezado": "### JSON для сложных сцен",
     "estado": "ORIGINAL", "casos": ["T3", "T4", "PROD"], "modelos": ["nano-banana-2", "nano-banana-pro"],
     "etapas": ["E5.4"]},
    {"id": "nb_edit", "nombre": "Nano Banana — edición conversacional",
     "archivo": "skills/image/references/nano-banana.md", "encabezado": "## Editing у Nano Banana",
     "estado": "ORIGINAL", "casos": ["T5"], "modelos": ["nano-banana-2", "nano-banana-pro"], "etapas": ["E5.5"]},
    {"id": "kling_t2v", "nombre": "Kling — esqueleto texto a video",
     "archivo": "skills/video/references/fixes-and-skeletons.md", "encabezado": "### Kling text-to-video",
     "estado": "ORIGINAL", "casos": ["CLIP"], "modelos": ["kling"], "etapas": ["PROMPT_VIDEO", "E6.2"]},
    {"id": "kling_i2v", "nombre": "Kling — esqueleto imagen a video",
     "archivo": "skills/video/references/fixes-and-skeletons.md", "encabezado": "### Kling image-to-video",
     "estado": "ORIGINAL", "casos": ["CLIP"], "modelos": ["kling"], "etapas": ["PROMPT_VIDEO", "E6.2"]},
    {"id": "veo_prose", "nombre": "Veo — esqueleto en prosa",
     "archivo": "skills/video/references/fixes-and-skeletons.md", "encabezado": "### Veo prose",
     "estado": "ORIGINAL", "casos": ["CLIP"], "modelos": ["veo"], "etapas": ["PROMPT_VIDEO", "E6.2"]},
    {"id": "seedance_skel", "nombre": "Seedance — esqueleto",
     "archivo": "skills/video/references/fixes-and-skeletons.md", "encabezado": "### Seedance",
     "estado": "ORIGINAL", "casos": ["CLIP"], "modelos": ["seedance"], "etapas": ["PROMPT_VIDEO", "E6.2"]},
    {"id": "video_negativos", "nombre": "Video — negativos por defecto",
     "archivo": "skills/video/references/fixes-and-skeletons.md", "encabezado": "## 4. Default negative constraints",
     "estado": "ORIGINAL", "casos": ["CLIP"], "modelos": ["kling", "veo", "seedance"], "etapas": ["E6.2"]},
    {"id": "tpl_composition_only", "nombre": "v3.2 — composition-only source",
     "archivo": "repo/templates/v3.2/composition-only-source.md", "encabezado": None,
     "estado": "ORIGINAL", "casos": ["REF", "T3"], "modelos": [], "etapas": ["REF"]},
    {"id": "tpl_underwater", "nombre": "v3.2 — underwater human reference policy",
     "archivo": "repo/templates/v3.2/underwater-human-reference-policy.md", "encabezado": None,
     "estado": "ORIGINAL", "casos": ["T3"], "modelos": [], "etapas": ["E5.4"]},
    {"id": "tpl_surgical", "nombre": "v3.2 — surgical image edit",
     "archivo": "repo/templates/v3.2/surgical-image-edit.md", "encabezado": None,
     "estado": "ORIGINAL", "casos": ["T5"], "modelos": [], "etapas": ["E5.5"]},
    {"id": "ast_v34", "nombre": "Prompt AST v2 (v3.4, tenis)",
     "archivo": "repo/examples/v3.4/tennis/prompt_ast_template.json", "encabezado": None,
     "estado": "ORIGINAL", "casos": ["T3"], "modelos": ["nano-banana-pro"], "etapas": ["PROMPT_IMAGEN"]},
    {"id": "sw30_engine", "nombre": "SW30 T1–T5 — secciones obligatorias (template_engine.py)",
     "archivo": "repo/production-package/template_engine.py", "encabezado": None,
     "estado": "SOURCE_RECONSTRUCTED", "casos": ["T1", "T2", "T3", "T4", "T5"], "modelos": [],
     "etapas": ["E5.2", "E5.3", "E5.4", "E5.5"],
     "nota": "El propio archivo dice: 'This is SOURCE_RECONSTRUCTED, not a claim to reproduce a missing historical file.'"},
    {"id": "storyboard_md", "nombre": "storyboard.md.tpl",
     "archivo": "skills/storyboard-architect/templates/storyboard.md.tpl", "encabezado": None,
     "estado": "ORIGINAL", "casos": ["SHOT"], "modelos": [], "etapas": ["E4.6"]},
    {"id": "shots_schema", "nombre": "shots.schema.json",
     "archivo": "skills/storyboard-architect/templates/shots.schema.json", "encabezado": None,
     "estado": "ORIGINAL", "casos": ["SHOT"], "modelos": [], "etapas": ["E4.3"]},
    {"id": "brand_lock_tpl", "nombre": "brand-lock.md.tpl (9 secciones)",
     "archivo": "skills/brand-lock-extractor/templates/brand-lock.md.tpl", "encabezado": None,
     "estado": "ORIGINAL", "casos": ["MARCA"], "modelos": [], "etapas": ["E0.4"]},
    {"id": "critique_schema", "nombre": "critique.schema.json",
     "archivo": "skills/visual-asset-critic/templates/critique.schema.json", "encabezado": None,
     "estado": "ORIGINAL", "casos": ["QA"], "modelos": [], "etapas": ["E5.7"]},
    {"id": "orden_bloques_ancla", "nombre": "Orden de bloques para un still cinematográfico",
     "archivo": "flujo-anclas.html", "encabezado": "Orden de bloques para un still cinematográfico",
     "estado": "ORIGINAL", "casos": ["T3", "T4", "SHOT"], "modelos": [], "etapas": ["E5.4"]},
]

NUEVAS = [
    {"id": "tarjeta_ancla_form", "nombre": "Formulario de tarjeta de ancla D1–D9", "estado": "NUEVA",
     "nota": "Propuesta de esta app. Los campos, valores y fuentes salen literalmente de la tabla "
             "'La tarjeta de ancla' de flujo-anclas.html (Paso 1) y de FACETAS en rules_v3.py; el "
             "formulario como tal no existía. Prueba: tests/test_flujos.py (TestAncla) y tests/test_e2e.py (test_ancla_tarjeta_y_gate_de_dependencias).",
     "casos": ["SHOT", "T3", "T4"], "modelos": [], "etapas": ["E5.1"]},
    {"id": "gpt5slot_bloques", "nombre": "5 slots de GPT Image 2 compuestos por bloques versionados", "estado": "NUEVA",
     "nota": "Composición de esta app: los 5 slots de gpt5slot (ORIGINAL) se llenan con bloques del AST v2 "
             "(ast_v34, ORIGINAL); la asignación bloque→slot es de la app y se prueba en tests/test_e2e.py (TestRegresionQuinteto: render_original del AST v3.4 idéntico) y tests/test_flujos.py (TestCasosImagen).",
     "casos": ["T1", "T2", "T3", "T4"], "modelos": ["gpt-image-2"], "etapas": ["PROMPT_IMAGEN", "E5.2"]},
    {"id": "nb_prosa_bloques", "nombre": "Prosa natural de Nano Banana compuesta por bloques", "estado": "NUEVA",
     "nota": "nano-banana.md pide prosa natural sin tag-soup; no trae un esqueleto de retrato. La app ordena los "
             "bloques según 'Orden de bloques para un still' (flujo-anclas.html Paso 6).",
     "casos": ["T1", "T2", "T3", "T4", "PROD"], "modelos": ["nano-banana-2", "nano-banana-pro"], "etapas": ["PROMPT_IMAGEN", "E5.2"]},
    {"id": "clip_bloques", "nombre": "Motion brief por bloques (Kling/Veo/Seedance)", "estado": "NUEVA",
     "nota": "Ordena los bloques según los esqueletos originales kling_i2v/veo_prose/seedance_skel y la tabla de "
             "motion brief de flujo-anclas.html Paso 7.",
     "casos": ["CLIP"], "modelos": ["kling", "veo", "seedance"], "etapas": ["PROMPT_VIDEO", "E6.2"]},
]


def _ruta(archivo: str) -> Path:
    if archivo.endswith(".html") and "/" not in archivo:
        return F.ORIGINALES / archivo
    return F.extraer_paquete() / archivo


def _bloque_tras(texto: str, encabezado: str) -> tuple[str, int]:
    lineas = texto.splitlines()
    for i, l in enumerate(lineas):
        if l.strip().startswith(encabezado):
            # primer bloque de código tras el encabezado y antes del siguiente encabezado de igual nivel
            j = i + 1
            while j < len(lineas) and not lineas[j].strip().startswith("```"):
                if re.match(r"^#{1,3} ", lineas[j]) and j > i + 1:
                    return "", i + 1
                j += 1
            if j >= len(lineas):
                return "", i + 1
            k = j + 1
            while k < len(lineas) and not lineas[k].strip().startswith("```"):
                k += 1
            return "\n".join(lineas[j + 1:k]), j + 2
    raise KeyError(encabezado)


def extraer() -> list[dict]:
    from .flujos import texto_fuente
    out = []
    for e in CATALOGO:
        d = dict(e)
        p = _ruta(e["archivo"])
        try:
            if e["archivo"].endswith(".html"):
                t = texto_fuente("anclas")
                i = t.index(e["encabezado"])
                d["texto"] = t[i:i + 900]
                d["linea"] = None
            else:
                raw = p.read_text(encoding="utf-8")
                if e["encabezado"]:
                    d["texto"], d["linea"] = _bloque_tras(raw, e["encabezado"])
                    if not d["texto"].strip():
                        d["texto"] = "\n".join(raw.splitlines()[d["linea"] - 1:d["linea"] + 20])
                else:
                    d["texto"], d["linea"] = raw, 1
            d["archivo_sha256"] = F.sha256_file(p)
            d["texto_sha256"] = F.sha256_text(d["texto"])
            d["extraida"] = True
        except (KeyError, ValueError, FileNotFoundError) as ex:
            d["extraida"] = False
            d["error"] = f"no se encontró: {ex}"
        out.append(d)
    for n in NUEVAS:
        out.append(dict(n, extraida=False, texto=None))
    return out


# SW30 T1..T5: secciones obligatorias, leídas del motor reconstruido del paquete.
def secciones_sw30() -> dict:
    import importlib.util
    p = F.extraer_paquete() / "repo" / "production-package" / "template_engine.py"
    spec = importlib.util.spec_from_file_location("apd_sw30_engine", p)
    m = importlib.util.module_from_spec(spec)
    import sys
    sys.modules["apd_sw30_engine"] = m
    spec.loader.exec_module(m)
    return {"modulo": m,
            "templates": {k: {"required": list(v.required), "optional": list(v.optional),
                              "block_required": dict(v.block_required)} for k, v in m.TEMPLATES.items()},
            "blocks": {k: b.text for k, b in m.BLOCKS.items()}}
