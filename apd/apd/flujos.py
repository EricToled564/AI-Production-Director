"""Recorridos, etapas, tracks, anclas y roles de referencia — transcritos de las fuentes.

Cada elemento lleva `fuente` y, cuando sale de un HTML de flujo, una `cita` literal
que `verificar_citas()` busca en el texto del HTML original. Si una cita no aparece,
la transcripción no está respaldada y el test falla: así nada de aquí se presenta
como original sin estarlo.

Etapas E0–E7 y tracks: `app/build_app.py` (ETAPAS, TRACKS), que a su vez cita
ai-production-director/SKILL.md §3. Subprocesos: `.claude/hooks/rules_v3.py` (TAREAS),
parseados de flujo-spot.html Nivel 2. Tarjeta de ancla y pasos A0–A12: flujo-anclas.html.
"""

from __future__ import annotations

import html as _html
import importlib.util
import re
from functools import lru_cache
from pathlib import Path

from . import fuentes as F

HTML_ANCLAS = F.ORIGINALES / "flujo-anclas.html"
HTML_SPOT = F.ORIGINALES / "flujo-spot.html"


def _texto_html(p: Path) -> str:
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = _html.unescape(t)
    t = re.sub(r"\s+", " ", t)
    return re.sub(r" ([,.;:])", r"\1", t)


@lru_cache(maxsize=None)
def texto_fuente(nombre: str) -> str:
    return _texto_html({"anclas": HTML_ANCLAS, "spot": HTML_SPOT}[nombre])


def _cargar_modulo(nombre: str, ruta: Path):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # sólo define constantes; no ejecuta main
    return mod


@lru_cache(maxsize=None)
def build_app():
    return _cargar_modulo("apd_build_app_original", F.REPO / "app" / "build_app.py")


@lru_cache(maxsize=None)
def rules_v3():
    import sys
    sys.path.insert(0, str(F.HOOKS))
    return _cargar_modulo("apd_rules_v3_original", F.HOOKS / "rules_v3.py")


def etapas() -> list[dict]:
    return build_app().ETAPAS


def tracks() -> dict:
    return build_app().TRACKS


def tareas() -> list[dict]:
    return rules_v3().TAREAS


def facetas() -> dict:
    return rules_v3().FACETAS


# ------------------------------------------------------------------ gates del spot
# flujo-spot.html Nivel 0→1: "Los gates 0, 1, 2 y 4 piden OK explícito del usuario en
# STANDARD y FILM." build_app.py marca ok=True exactamente en E0, E1, E2, E4.
GATES_OK = {"E0", "E1", "E2", "E4"}
CITA_GATES_OK = "Los gates 0, 1, 2 y 4 piden OK explícito del usuario en STANDARD y FILM."

# Etapas por track. Fuente: TRACKS de build_app.py + flujo-spot.html Nivel 0→1.
ETAPAS_POR_TRACK = {
    "EXPRESS": ["E4", "E5", "E6"],
    "STANDARD": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"],
    "FILM": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"],
}
CITA_EXPRESS = "en EXPRESS se entra directo en la Etapa 4"
NOTA_TRACK = {
    "EXPRESS": "≤30s, un beat. Entra en E4 y salta E0–E3 y E7 (build_app.TRACKS).",
    "STANDARD": "30–90s. E1 comprimida (2–3 conceptos), E2 sin treatment (build_app.TRACKS).",
    "FILM": "90s–10min. E0–E7 completas, todos los gates, treatment separado (build_app.TRACKS).",
}

# Dependencias entre etapas (flujo-spot.html Nivel 0→1: cadena de gates).
DEPENDENCIAS = {
    "E0": [], "E1": ["E0"], "E2": ["E1"], "E3": ["E2"], "E4": ["E3"],
    "E5": ["E4"], "E6": ["E5"], "E7": ["E6"],
}

# ------------------------------------------------------------------ tarjeta de ancla
TARJETA_ANCLA = [
    {"dim": "d1", "nombre": "Rol del ancla",
     "valores": "character ref · environment ref · keyframe FF · keyframe LF · hero/macro · motif insert",
     "decide": "Qué se fija, qué modelo de video la recibe, si necesita pareja FF/LF con el mismo ratio",
     "fuente": "director E5 · kling §3 · seedance-25 §16"},
    {"dim": "d2", "nombre": "Tipo de acción",
     "valores": "A pose sostenida · B instante pico congelado · C movimiento continuo · D fenómeno de luz o clima · E interacción o diálogo · F multitud o grupo",
     "decide": "La cue de movimiento congelado, los checks de física y la técnica de composición",
     "fuente": "animatic-keyframes §4 · race-and-speed §3 · dramaturgy §6 · SW30 R1 R8 R9"},
    {"dim": "d3", "nombre": "Número de sujetos",
     "valores": "0 placa · 1 · 2 sin contacto · 2 con contacto · grupo ensamble 3 a 8 con todas las identidades reconocibles · multitud anónima más de 6 sin rostros legibles",
     "decide": "Cuántas generaciones, en qué orden, con qué referencias y roles",
     "fuente": "SW30 R1 R4 R7 R9 · fixes twins · kling §7 Elements · nano-banana multi-reference · U13"},
    {"dim": "d4", "nombre": "Tratamiento artístico",
     "valores": "documental · narrativo cinematográfico · comercial pulido · race/kinetic · UGC · animación (visual-media)",
     "decide": "Film stock, dureza de luz, grano, cuánto del frame queda a oscuras, si hay rostro visible",
     "fuente": "patterns-and-genres §2 · creative-direction · camera-lighting §6-7 · SW30 T1"},
    {"dim": "d5", "nombre": "Paleta y grade",
     "valores": "brand-lock hex · series_lock.color_grade verbatim · paleta nombrada",
     "decide": "Colores concretos y bans repetidos en cada ancla; nunca \"cinematic colors\"",
     "fuente": "camera-lighting §7 · consistency-locks Lock 8 · race-and-speed §7"},
    {"dim": "d6", "nombre": "Cámara",
     "valores": "encuadre ECU a EWS · lente 24, 35, 50, 85, 100 macro, anamórfico 40 · DOF shallow, deep, rack · cámara implícita",
     "decide": "La cámara implícita es el movimiento del que este still es el primer frame; el ángulo va aparte, en D9",
     "fuente": "shot-grammar · camera-lighting §1-3 · animatic §6 · race-and-speed §2"},
    {"dim": "d7", "nombre": "Iluminación",
     "valores": "fuente motivada · dirección · calidad dura o suave · ratio iluminado · specular",
     "decide": "Rostros documentales: luz dura rasante. Atmósfera: solo a contraluz. Cine: una fuente domina. Comercial: clean, pareja",
     "fuente": "SW30 template T1 · race-and-speed §7 · camera-lighting §4-6 · creative-direction"},
    {"dim": "d8", "nombre": "Modelo y resolución",
     "valores": "NB2 · NBP · GPT Image 2 low/medium/high · Flux, Midjourney vía forge · grounding sí/no · 0.5K→2K/4K",
     "decide": "Grounding fuerza NB2 en arquitectura y especies; rostros se prueban en NB2 y NBP; etiquetas y UI en GPT high",
     "fuente": "models.md · nano-banana.md · gpt-image.md · forge failure-modes F1"},
    {"dim": "d9", "nombre": "Ángulo y altura de cámara",
     "valores": "eye-level · high · low · overhead o top-down · dutch · worm's eye · POV · altura física",
     "decide": "Se elige por la dinámica de poder del beat, nunca por variedad. Un ángulo distinto al spec es hard fail en la crítica",
     "fuente": "shot-grammar Angle · dramaturgy §6 · animatic §6 · race §10 · kling §3 · critique-rubric Layer 3"},
]
CITA_TARJETA = "Un campo vacío revela dirección faltante; no se genera con campos vacíos."

# D9 por tipo de acción (flujo-anclas.html, tabla "D9 por tipo de acción").
D9_POR_ACCION = {
    "A_pose": {"defecto": "eye-level", "texto": "Eye-level para maestros de identidad; low o high solo si el beat lo pide",
               "porque": "Un maestro debe leerse neutro para servir a todos los shots; el ángulo dramático se decide en el cuadro, no en la génesis",
               "fuente": "kling §7 source image rules · shot-grammar", "inferencia": False},
    "B_pico": {"defecto": "low", "texto": "Low o a ras de la superficie, aislando al sujeto contra cielo o agua",
               "porque": "El pico se lee como fuerza", "fuente": "animatic §6", "inferencia": True},
    "C_movimiento": {"defecto": "low", "texto": "Altura de parachoques o más baja; rig montable",
                     "porque": "el ángulo alto y limpio es el god-angle que mata la velocidad", "fuente": "race §3 §5 §10", "inferencia": False},
    "D_luz_clima": {"defecto": "low", "texto": "Low con horizonte bajo para cielo y evento",
                    "porque": "La fuente motivada domina si ocupa el frame", "fuente": "race §7 contre-jour", "inferencia": True},
    "E_interaccion": {"defecto": "eye-level", "texto": "Eye-level y OTS; el que domina más alto o en la puerta",
                      "porque": "Staging revela la jerarquía antes del diálogo", "fuente": "dramaturgy §6 · Lock 7", "inferencia": False},
    "F_multitud": {"defecto": "high", "texto": "High o aérea para escala y patrón; low con la masa como muro para amenaza",
                   "porque": "El ángulo decide si la multitud es paisaje o presión", "fuente": "animatic §6 · race §3", "inferencia": False},
    "ensamble": {"defecto": "eye-level", "texto": "Eye-level frontal o ligeramente low para formación; simetría con spine central",
                 "porque": "Todas las identidades deben leerse; el ángulo extremo esconde rostros", "fuente": "animatic §6 · SW30 R14", "inferencia": False},
}
CITA_D9_POSE = "Eye-level para maestros de identidad; low o high solo si el beat lo pide"

# Pasos A0–A12 del flujo de un ancla, con sus gates.
PASOS_ANCLA = [
    ("A0", "Inventario desde shots.json", "series_lock · shot card · function tag · 5 anclas", None),
    ("A1", "Tarjeta de ancla", "nueve dimensiones D1 a D9 llenas", "¿Algún campo vacío o beat no nombrable en una frase?"),
    ("A2", "Plan de dependencias", "qué génesis y qué refs deben existir antes", "¿Existen canonizados persona, placa, producto que este ancla necesita?"),
    ("A3", "Ruta por tipo de acción", "D2", None),
    ("A4", "Tratamiento, paleta, cámara, ángulo, luz", "D4 a D7 y D9", None),
    ("A5", "Modelo y resolución", "D8 ratio destino desde el inicio", None),
    ("A6", "Ensamblar por bloques", "encuadre+lente · sujeto en su umbral · 3 planos con trabajo", None),
    ("A7", "Lints mecánicos", "gate_image · gate_dramaturgy · validate_prompts", "Pregunta de avance ¿todas las reglas del caso? SÍ sin matices"),
    ("A8", "Micro-gate", "3 líneas + preflight de costo", None),
    ("A9", "Generar barato → seleccionar → regenerar en alta", "NB 0.5K → 2K/4K · GPT low → high", None),
    ("A10", "Inspección 100% + crítica 6 capas", "checks específicos del tipo de acción", "ACCEPT / REVISE ≥80% / REJECT o 2ª falla"),
    ("A11", "Canonizar con hash", "registrar en shot.assets.generated", None),
    ("A12", "Motion brief para el video", "Preserve cues · roles FF/LF · un movimiento · sin re-describir", None),
]
CITA_PASOS = "Doce pasos y cinco gates."

# Motion brief por modelo (flujo-anclas.html Paso 7).
MOTION_BRIEF = {
    "kling": {"recibe": "start_image y opcional tail_image; Elements con 4 vistas para personajes recurrentes",
              "dice": "Preserve identity, wardrobe, sign exactly. Un movimiento de cámara primero. Shots con timecodes. Audio",
              "fuente": "kling §3 §10 · forge kling adapter"},
    "veo": {"recibe": "First Frame; reference ingredients para personaje, locación y prop",
            "dice": "Maintain the subject from the first frame. Movimiento, cámara, cambio de luz, audio",
            "fuente": "veo §7 §8"},
    "seedance": {"recibe": "@Image 1 primer frame y @Image 2 último frame declarados por separado, mismo ratio",
                 "dice": "Etapas consecutivas, un cambio de estado por etapa, estado final visible; roles de cada referencia",
                 "fuente": "seedance-25 §5 §6 §16 · U13"},
}
CITA_MOTION = "Preserve-cues, roles start/tail, movimiento puro, imagen final nombrada"

# Roles de referencia e identidad. Autoridad: DECISIONES.md #3 (Eric, 2026-09-25).
ROLES_REFERENCIA = {
    "genesis": {"nombre": "Génesis sin referencia", "identidad": "bloque de identidad completo en texto (no hay imagen que heredar)",
                "fuente": "flujo-spot.html Nivel 4 · DECISIONES #3"},
    "personaje": {"nombre": "Referencia de personaje (sin start frame)", "identidad": "bloque de identidad completo y verbatim + rol explícito de la referencia",
                  "fuente": "DECISIONES.md #3: 'Referencia de personaje sin start frame, casos con @img, Elements o ancla con refs: bloque de identidad completo y verbatim'"},
    "frame_inicial": {"nombre": "Keyframe de inicio (FF) en imagen a video", "identidad": "no re-describir: el frame fija la identidad; el prompt sólo dice cómo evoluciona",
                      "fuente": "DECISIONES.md #3 · SW30 R16 · flujo-anclas Paso 7"},
    "frame_final": {"nombre": "Keyframe final (LF)", "identidad": "no re-describir; mismo aspect ratio que el FF; 'The tail image defines X — inherit exactly'",
                    "fuente": "DECISIONES.md #3 · SW30 R16 · flujo-anclas D1"},
    "edicion": {"nombre": "Edición quirúrgica sobre imagen existente (T5)", "identidad": "Change / Preserve: la identidad va en Preserve, no se re-describe",
                "fuente": "gpt-image.md Editing · SW30 R3 R12 · template T5"},
    "derivacion": {"nombre": "Derivación con referencia (T2/T3/T4)", "identidad": "herencia mínima: 'same face and clothes' + sólo deltas; ambos referentes adjuntos",
                   "fuente": "SW30 R4 R5 · flujo-spot Nivel 3b"},
    "estilo": {"nombre": "Referencia de estilo/entorno", "identidad": "no aplica identidad; rol explícito ('apply only…')",
               "fuente": "gpt-image.md Multi-Image · U13"},
}


def citas() -> list[tuple[str, str]]:
    out = [("spot", CITA_GATES_OK), ("spot", CITA_EXPRESS), ("anclas", CITA_TARJETA),
           ("anclas", CITA_D9_POSE), ("anclas", CITA_PASOS), ("anclas", CITA_MOTION)]
    for d in TARJETA_ANCLA:
        out.append(("anclas", d["decide"].split(";")[0].split(". ")[0]))
    for k, v in D9_POR_ACCION.items():
        out.append(("anclas", v["texto"]))
    for p in PASOS_ANCLA:
        out.append(("anclas", p[1]))
    for t in tareas():
        out.append(("spot", t["nombre"]))
    return out


def verificar_citas() -> dict:
    faltan = []
    for fuente, cita in citas():
        if re.sub(r"\s+", " ", cita).strip() not in texto_fuente(fuente):
            faltan.append((fuente, cita))
    return {"total": len(citas()), "faltan": faltan}
