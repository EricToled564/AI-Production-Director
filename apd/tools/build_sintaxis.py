#!/usr/bin/env python3
"""Construye apd/data/sintaxis_fuente.json. Cada cita es verbatim de la fuente."""
import json, os

import sys as _s, pathlib as _p
_s.path.insert(0, str(_p.Path(__file__).resolve().parents[1]))
from apd import fuentes as _F
PKG = str(_F.extraer_paquete() / "skills")
REPO = str(_F.REPO)
OUT = os.path.join(REPO, "apd/data/sintaxis_fuente.json")

# ---- archivos ----
IS = 'skills/image/SKILL.md'
GI = 'skills/image/references/gpt-image.md'
NB = 'skills/image/references/nano-banana.md'
MD = 'skills/image/references/models.md'
GR = 'skills/image/references/golden-rules.md'
PF = 'skills/image/references/prompt-framework.md'
CH = 'skills/image/references/characters.md'
ED = 'skills/image/references/editing.md'
MP = 'skills/image/references/multi-panel.md'
TR = 'skills/image/references/text-rendering.md'
ECO = 'skills/image/references/patterns/ecommerce.md'
VS = 'skills/video/SKILL.md'
UR = 'skills/video/references/universal-rules.md'
KL = 'skills/video/references/kling.md'
VE = 'skills/video/references/veo.md'
SD = 'skills/video/references/seedance.md'
S25 = 'skills/video/references/seedance-25.md'
FX = 'skills/video/references/fixes-and-skeletons.md'
AK = 'skills/video/references/animatic-keyframes.md'
RS = 'skills/video/references/race-and-speed.md'
CL = 'skills/video/references/camera-lighting-vocabulary.md'
FC = 'skills/visual-prompt-forge/adapters/_capabilities.json'
FMJ = 'skills/visual-prompt-forge/adapters/midjourney.md'
FFL = 'skills/visual-prompt-forge/adapters/flux.md'
FID = 'skills/visual-prompt-forge/adapters/ideogram.md'
FSR = 'skills/visual-prompt-forge/adapters/seedream.md'
FGI = 'skills/visual-prompt-forge/adapters/gpt-image.md'
FNB = 'skills/visual-prompt-forge/adapters/nano-banana.md'
FKL = 'skills/visual-prompt-forge/adapters/kling.md'
FVE = 'skills/visual-prompt-forge/adapters/veo.md'
FSD = 'skills/visual-prompt-forge/adapters/seedance.md'
FHA = 'skills/visual-prompt-forge/adapters/hailuo.md'
FPA = 'skills/visual-prompt-forge/references/prompt-anatomy.md'
FCL = 'skills/visual-prompt-forge/references/consistency-locks.md'
FFM = 'skills/visual-prompt-forge/references/failure-modes.md'
SW = 'skills/produccion-visual-sw30/SKILL.md'
AU = 'skills/aurora-prompt-linter/SKILL.md'
APD = 'skills/ai-production-director/SKILL.md'
VY = '.claude/hooks/aurora/vocabularies.yaml'
PL = '.claude/hooks/aurora/prompt_linter.py'
DE = '.claude/rules/DECISIONES.md'
FA = 'apd/originales/flujo-anclas.html'


def C(f, a, b, t):
    return {"archivo": f, "linea_ini": a, "linea_fin": b, "texto": t}


def R(req, sec, cita, **kw):
    d = {"requisito": req, "seccion_afectada": sec, "cita": cita}
    d.update(kw)
    return d


def S(id_, lit, orden, oblig, cont, cita):
    return {"id": id_, "etiqueta_literal": lit, "orden": orden, "obligatoria": oblig, "contenido": cont, "cita": cita}


def L(texto, cuando, cita):
    return {"texto": texto, "cuando": cuando, "cita": cita}


def P(nombre, valores, cita):
    return {"nombre": nombre, "valores": valores, "cita": cita}


def X(texto, cita):
    return {"texto": texto, "cita": cita}


def SL(caso, secciones, cita):
    return {"caso_linter": caso, "secciones_requeridas": secciones, "bloquea": True, "cita": cita}


INF = "derivado: flujo-anclas.html lo marca como INFERENCIA o síntesis de reglas vecinas; no es texto literal de un skill"

# =====================================================================
# MODELOS
# =====================================================================
modelos = {}

modelos["gpt-image-2"] = {
    "medio": "imagen",
    "formato": "labels",
    "autoridad_sintaxis": C(APD, 34, 34, "Sintaxis final de prompts de imagen"),
    "secciones": [
        S("scene", "Scene:", 1, True, "lugar, hora del día, fondo, entorno", C(GI, 10, 10, "Scene: location, time of day, background, environment")),
        S("subject", "Subject:", 2, True, "foco primario: quién o qué es central", C(GI, 11, 11, "Subject: primary focus — who or what is central")),
        S("important_details", "Important Details:", 3, True, "materiales, texturas, luz, ángulo de cámara, mood, composición", C(GI, 12, 12, "Important Details: materials, textures, lighting, camera angle, mood, composition")),
        S("use_case", "Use Case:", 4, True, "editorial, mockup de producto, UI, póster, infografía", C(GI, 13, 13, "Use Case: editorial, product mockup, UI, poster, infographic")),
        S("constraints", "Constraints:", 5, True, "qué NO debe cambiar/aparecer; el quinto slot es donde fallan los prompts mediocres", C(GI, 14, 17, "The fifth slot is where most mediocre prompts fail silently.")),
        S("text", "Text:", 6, False, "solo si hay texto: línea literal entre comillas con fuente, color, posición (plantilla Marketing Creative)", C(GI, 164, 165, 'Text: "EXACT HEADLINE" in [font style], [color], [position]')),
    ],
    "formato_regla": C(GI, 7, 7, "Пиши лейблами, не сплошным текстом."),
    "cabecera_salida": [
        L("Model: <nano-banana-2 | nano-banana-pro | gpt-image-2>", "siempre, fuera del cuerpo del prompt", C(IS, 89, 89, "Model: <nano-banana-2 | nano-banana-pro | gpt-image-2>")),
        L("Quality: <low | medium | high>", "solo gpt-image-2", C(IS, 90, 90, "Quality: <low | medium | high>          (only for gpt-image-2)")),
        L("Size / Ratio:", "siempre", C(IS, 91, 91, "Size / Ratio: <e.g. 1536×1024 or 16:9>")),
        L("Prompt: / Notes:", "siempre; Notes fuera del cuerpo", C(IS, 93, 96, "Notes:")),
        L("metadatos fuera del cuerpo", "SW30: el motor rechaza metadatos dentro del cuerpo", C(SW, 90, 90, "se cuela un metadato (Model/Quality/Size/Aspect ratio) dentro del cuerpo del prompt")),
    ],
    "literales_obligatorios": [
        L("no extra words, no duplicate text, no watermarks", "hay texto en la imagen", C(GI, 72, 72, "no extra words, no duplicate text, no watermarks")),
        L("100 percent readable and physically believable", "texto pequeño que sale ilegible", C(GI, 73, 73, "100 percent readable and physically believable")),
        L("Change: [single concrete change]", "edición", C(GI, 81, 81, "Change: [single concrete change]")),
        L("Preserve: face, identity, pose, lighting, framing, background, geometry, text, layout", "edición; repetir en cada iteración", C(GI, 82, 82, "Preserve: face, identity, pose, lighting, framing, background, geometry, text, layout")),
        L("Constraints: no extra objects, no redesign, no drift", "edición", C(GI, 83, 83, "Constraints: no extra objects, no redesign, no drift")),
        L("preserve-list explícita", "ediciones: obligatoria en gpt-image-2", C(IS, 100, 100, "mandatory for gpt-image-2, recommended for nano-banana")),
        L("Image 1: base scene / Image 2: <rol> reference (...)", "multi-imagen: cada ref con rol", C(GI, 106, 107, "Image 1: base scene")),
        L("texto literal entre comillas o ALL CAPS; fuente, tamaño, color, posición explícitos", "texto en imagen", C(GI, 69, 70, "Шрифт, размер, цвет, позиция — явно.")),
    ],
    "parametros_externos": [
        P("model", "gpt-image-2 (default de producción); gpt-image-1.5 / gpt-image-1 solo migración; gpt-image-1-mini barato", C(GI, 3, 3, "Production default OpenAI: `gpt-image-2`")),
        P("quality", "low | medium (default de arranque) | high", C(GI, 45, 47, "Default starting point")),
        P("quality=high", "obligatorio para texto pequeño/denso/multi-font; recomendado en retratos, edits sensibles a identidad, brand assets", C(GI, 74, 74, "`quality: high` обязательно")),
        P("size", "ambos lados múltiplos de 16; max edge <3840px; ratio máx 3:1; límite fiable 2560×1440; ходовые 1024×1536 / 1536×1024 / 1024×1024", C(GI, 53, 57, "Обе стороны: кратны 16")),
        P("size (ratio)", "máximo 3:1 (long:short); extremos 1:8/8:1 no soportados", C(GI, 55, 55, "Aspect ratio: max 3:1 (long:short)")),
        P("size (forge)", "1024x1792 para 9:16, 1792x1024 para 16:9, 1024x1024 para 1:1", C(FGI, 25, 25, "`1024x1792` for 9:16")),
        P("style (forge)", "natural para fotorreal, vivid para estilizado", C(FGI, 27, 27, "`natural` for photoreal, `vivid` for stylized")),
        P("mask_image_url", "opcional, ediciones puntuales", C(GI, 90, 90, "mask_image_url")),
        P("input_fidelity", "high solo en gpt-image-1.5/1; en gpt-image-2 high-fidelity por defecto", C(GI, 96, 96, "в gpt-image-2 high-fidelity по умолчанию")),
        P("endpoint edición", "openai/gpt-image-2/edit (fal.ai) o equivalente OpenAI", C(GI, 78, 78, "openai/gpt-image-2/edit")),
        P("aspect_param (forge)", "size", C(FC, 66, 66, '"aspect_param": "size"')),
    ],
    "negativos": {"campo_aparte": False, "formato": "exclusiones dentro del slot Constraints: del propio prompt; positivo + preserve list explícito", "limite": None,
                  "cita": C(MD, 51, 51, "Использовать позитив + явный preserve list"),
                  "citas_adicionales": [C(FC, 65, 65, '"supports_negative_prompt": false'), C(VY, 396, 396, "gpt-image: optional")]},
    "longitud": {"min": 150, "max": 300, "unidad": "palabras", "bloquea": False, "cita": C(FGI, 38, 38, "GPT Image handles **150–300 words** comfortably."),
                 "citas_adicionales": [C(FC, 60, 60, '"max_prompt_words": 300'), C(SW, 79, 80, "Un slot de 300+ palabras compite"), C(DE, 9, 9, "El conteo de palabras nunca bloquea")]},
    "prohibido": [
        X("stunning, incredible, epic, gorgeous, masterpiece (anti-slop: empeoran el resultado)", C(GI, 36, 36, "stunning, incredible, epic, gorgeous, masterpiece")),
        X("vague praise daña GPT Image 2", C(MD, 49, 49, "вредит, делает результат хуже")),
        X("etiquetas de estilo sueltas", C(GI, 37, 37, "minimalist brutalist luxury photoreal")),
        X("comparaciones externas ('como en anuncio de Apple')", C(GI, 38, 38, "как в Apple-рекламе")),
        X("ratios extremos 1:8 / 8:1", C(GI, 65, 65, "Экстрим вроде 1:8 / 8:1 GPT Image 2 НЕ умеет")),
        X("flags --ar o sintaxis de pesos", C(FGI, 89, 89, "Don't include `--ar` flags or weight syntax")),
        X("comma stacks estilo Midjourney", C(FGI, 86, 86, "Don't write Midjourney-style comma stacks")),
        X("más de cinco elementos distintos por escena", C(FGI, 88, 88, "five or fewer distinct elements per scene")),
    ],
    "referencias": {"max": 16, "sintaxis_rol": "Image N: <rol> (apply only ... from Image N)", "cita": C(GI, 102, 104, "не только номером"),
                    "citas_adicionales": [C(MD, 54, 54, "До 16, индексировать с ролью")]},
    "secciones_linter": [
        SL("1", ["subject", "action_or_pose", "environment", "style", "camera_or_lens", "lighting", "anti_style", "use_case", "constraints_slot"], C(VY, 514, 514, "gpt_image_2__1:")),
        SL("2", ["ref_roles", "subject_action", "camera_or_lens", "lighting", "style_consistency", "constraints_slot"], C(VY, 571, 571, "gpt_image_2__2:")),
    ],
}

_nb_common_prohibido = [
    X("números de lente/exposición (50mm, 85mm, f/2.8, ISO 400): NB los ignora; usar descripción", C(NB, 24, 24, "50mm, 85mm, f/2.8, ISO 400")),
    X("tag-soup", C(NB, 25, 25, "cool, modern, 4k, cinematic")),
    X("sintaxis de flags estilo Midjourney (--ar)", C(FNB, 101, 101, "Don't use Midjourney-style flag syntax")),
    X("varias modificaciones en un solo prompt image-to-image", C(FNB, 103, 103, "Don't pile multiple modifications in one image-to-image prompt")),
    X("texto en el prompt (forge: componer aparte)", C(FNB, 105, 105, "Don't include text content in image prompts")),
    X("framing negativo", C(GR, 12, 12, "Describe what you WANT, not what you don't want.")),
]
_nb_common_literales = [
    L("verbo inicial (Create / Generate / Design / Transform / Convert / Edit)", "siempre (golden rule 1)", C(GR, 8, 8, "Tell the model the primary operation")),
    L("[Image 1: face] [Image 2: outfit] [Image 3: background] + Combine: face from Image 1, ...", "multi-referencia", C(NB, 69, 72, "Combine: face from Image 1, outfit style from Image 2, setting from Image 3.")),
    L("Match lighting and perspective.", "multi-referencia / producto en contexto", C(NB, 73, 73, "Match lighting and perspective.")),
    L("Keep [PRESERVED ELEMENTS] exactly the same.", "edición", C(NB, 93, 93, "Keep [PRESERVED ELEMENTS] exactly the same.")),
    L("Keep facial features exactly the same as Image 1", "identidad desde referencia", C(CH, 14, 14, 'Key phrase: "Keep facial features exactly the same as Image 1"')),
    L("natural contrast, no HDR look", "contrarrestar la tendencia a HDR/sobresaturación", C(NB, 138, 138, "natural contrast, no HDR look")),
    L("Keep {what to preserve}. Change {what to vary}.", "image-to-image (forge); sin la cláusula preserve la ref es inspiración suelta", C(FNB, 104, 104, "Don't forget the \"preserve\" clause in image-to-image")),
    L("texto entre comillas + fuente + posición", "texto en imagen", C(MD, 50, 50, "в кавычках, font + position")),
]
_nb_common_params = [
    P("image_size", "0.5K / 1K (default) / 2K / 4K; mayúscula K obligatoria ('1k' se rechaza)", C(NB, 122, 122, "пишется строго с заглавной K")),
    P("image_size (omitido)", "si no se indica, iguala la entrada o 1:1", C(NB, 122, 122, "Без указания размера модель матчит вход, иначе 1:1")),
    P("aspect ratio estándar", "1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 (en el prompt: 'Format: 16:9.')", C(NB, 51, 51, "Стандартные: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9.")),
    P("aspectRatio (forge)", "9:16, 16:9, 1:1, 4:5, 3:4, 21:9; nombre camelCase; ignora --ar", C(FC, 82, 84, '"aspect_param": "aspectRatio"')),
    P("model (forge)", "gemini-2.5-flash-image", C(FNB, 29, 29, "`gemini-2.5-flash-image`")),
    P("numberOfImages (forge)", "1 para series, 4 para exploración", C(FNB, 31, 31, "`numberOfImages`")),
    P("referenceImages (forge)", "array de imágenes base64", C(FNB, 32, 32, "`referenceImages`")),
    P("workflow de resolución", "variantes en 0.5K → ganador a 2K/4K", C(NB, 120, 120, "прогон вариантов на `0.5K` flash")),
]

modelos["nano-banana-2"] = {
    "medio": "imagen",
    "formato": "prosa",
    "autoridad_sintaxis": C(APD, 34, 34, "Sintaxis final de prompts de imagen"),
    "model_id": C(NB, 8, 8, "gemini-3.1-flash-image"),
    "secciones": [
        S("subject", None, 1, False, "sujeto", C(NB, 13, 14, "Subject + Action + Location/context + Composition + Style")),
        S("action", None, 2, False, "acción", C(NB, 14, 14, "Subject + Action")),
        S("location_context", None, 3, False, "lugar / contexto", C(NB, 14, 14, "Location/context")),
        S("composition", None, 4, False, "composición", C(NB, 14, 14, "Composition + Style")),
        S("style", None, 5, False, "estilo", C(NB, 14, 14, "Composition + Style")),
        S("format", "Format:", 6, False, "aspect ratio dentro del texto", C(NB, 19, 19, "Format: 16:9.")),
    ],
    "formato_regla": C(NB, 13, 13, "Натуральный язык, 1-2 параграфа. Структура свободная, но порядок помогает:"),
    "formato_json": L("JSON (subject / photography / background)", "escenas de 5+ elementos", C(NB, 76, 76, "JSON для сложных сцен (5+ элементов)")),
    "literales_obligatorios": _nb_common_literales + [
        L("Generate a ... photograph of [SPECIFIC REAL PLACE]. Ensure the architectural details ... are accurate to reality.", "image grounding de lugar real (solo NB2)", C(NB, 33, 34, "Ensure the architectural details, the spire, the surrounding square, and")),
    ],
    "parametros_externos": _nb_common_params + [
        P("thinking_level", "minimal (default) | high", C(NB, 55, 55, "thinking_level: minimal | high")),
        P("aspect ratio extremo", "1:8, 8:1, 1:4, 4:1 (solo NB2)", C(NB, 41, 43, "1:8, 8:1, 1:4, 4:1 — для баннеров, скроллов, комикс-стрипов.")),
        P("image_size 512px", "solo NB2; Lite solo 1K", C(NB, 122, 122, "есть только у NB2; Lite — только 1K")),
    ],
    "negativos": {"campo_aparte": False, "formato": "framing positivo; sin bloque negativo", "limite": None,
                  "cita": C(MD, 51, 51, "Использовать позитив"),
                  "citas_adicionales": [C(FC, 81, 81, '"supports_negative_prompt": false'), C(VY, 397, 397, "nano-banana: optional")]},
    "longitud": {"min": 60, "max": 120, "unidad": "palabras", "bloquea": False, "cita": C(FNB, 42, 42, "Nano Banana handles **60–120 words** efficiently."),
                 "citas_adicionales": [C(FC, 76, 76, '"max_prompt_words": 120'), C(NB, 13, 13, "Натуральный язык, 1-2 параграфа"), C(DE, 9, 9, "El conteo de palabras nunca bloquea")]},
    "prohibido": _nb_common_prohibido + [X("grounding con personas concretas (no funciona)", C(NB, 39, 39, "конкретные люди"))],
    "referencias": {"max": 10, "max_personaje": 4, "max_estilo": 0, "sintaxis_rol": "[Image N: rol] + Combine: X from Image N",
                    "cita": C(NB, 64, 66, "High-fidelity объекты | до 14 | до 10 | до 6"),
                    "citas_adicionales": [C(NB, 65, 65, "Character-consistency рефы | нет | до 4 | до 5"), C(NB, 66, 66, "Style рефы | нет | нет | до 3")]},
    "secciones_linter": [
        SL("1", ["subject", "action_or_pose", "environment", "style", "lighting", "details"], C(VY, 541, 541, "nano_banana_2__1:")),
        SL("2", ["ref_roles", "subject_action", "camera_or_lens", "lighting", "placement_anchor"], C(VY, 593, 593, "nano_banana_2__2:")),
    ],
}

modelos["nano-banana-pro"] = {
    "medio": "imagen",
    "formato": "prosa",
    "autoridad_sintaxis": C(APD, 34, 34, "Sintaxis final de prompts de imagen"),
    "model_id": C(NB, 9, 9, "gemini-3-pro-image"),
    "secciones": [dict(s) for s in modelos["nano-banana-2"]["secciones"]],
    "formato_regla": C(NB, 13, 13, "Натуральный язык, 1-2 параграфа. Структура свободная, но порядок помогает:"),
    "formato_json": L("JSON (subject / photography / background)", "escenas de 5+ elementos", C(NB, 76, 76, "JSON для сложных сцен (5+ элементов)")),
    "literales_obligatorios": list(_nb_common_literales),
    "parametros_externos": _nb_common_params + [
        P("thinking", "siempre activo; no se puede desactivar en NBP", C(NB, 55, 55, "у NBP отключить нельзя")),
    ],
    "negativos": {"campo_aparte": False, "formato": "framing positivo; sin bloque negativo", "limite": None,
                  "cita": C(PF, 88, 88, 'Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"'),
                  "citas_adicionales": [C(FC, 81, 81, '"supports_negative_prompt": false'), C(VY, 397, 397, "nano-banana: optional")]},
    "longitud": {"min": 60, "max": 120, "unidad": "palabras", "bloquea": False, "cita": C(FNB, 42, 42, "Nano Banana handles **60–120 words** efficiently."),
                 "citas_adicionales": [C(FC, 76, 76, '"max_prompt_words": 120'), C(DE, 9, 9, "El conteo de palabras nunca bloquea")]},
    "prohibido": list(_nb_common_prohibido),
    "referencias": {"max": 6, "max_personaje": 5, "max_estilo": 3, "sintaxis_rol": "[Image N: rol] + Combine: X from Image N",
                    "cita": C(NB, 144, 144, "(6 объектов + 5 character + 3 style)"),
                    "citas_adicionales": [C(NB, 64, 66, "High-fidelity объекты | до 14 | до 10 | до 6"), C(MD, 20, 20, "Nano Banana Pro** (до 14)")]},
    "notas": [X("NBP a veces sostiene peor los rostros que NB2: probar ambos en series de retrato", C(NB, 146, 146, "для портретной серии сначала тестируй оба"))],
    "secciones_linter": [
        SL("1", ["subject", "action_or_pose", "environment", "style", "lighting", "details"], C(VY, 533, 533, "nano_banana_pro__1:")),
        SL("2", ["ref_roles", "subject_action", "camera_or_lens", "lighting", "placement_anchor"], C(VY, 586, 586, "nano_banana_pro__2:")),
    ],
}

modelos["midjourney"] = {
    "medio": "imagen",
    "formato": "mixto",
    "formato_nota": "frases cortas separadas por comas + flags -- al final; sin oraciones completas",
    "autoridad_sintaxis": C(APD, 126, 126, "la autoridad es el adaptador de `visual-prompt-forge`"),
    "secciones": [
        S("subject", None, 1, True, "sujeto (con character anchor)", C(FMJ, 10, 10, "{subject}, {action}, {composition}, {environment}, {lighting}, {color/mood}, {style modifiers} --ar {ratio}")),
        S("action", None, 2, False, "acción", C(FMJ, 10, 10, "{subject}, {action}")),
        S("composition", None, 3, False, "composición", C(FMJ, 10, 10, "{composition}")),
        S("environment", None, 4, False, "entorno de series_lock", C(FMJ, 10, 10, "{environment}")),
        S("lighting", None, 5, False, "luz de series_lock", C(FMJ, 10, 10, "{lighting}")),
        S("color_mood", None, 6, False, "grade y mood", C(FMJ, 10, 10, "{color/mood}")),
        S("style_modifiers", None, 7, False, "modificadores de estilo", C(FMJ, 10, 10, "{style modifiers}")),
        S("params", "--ar", 8, True, "flags al final", C(FMJ, 10, 10, "--ar {ratio} --style {style} --s {stylize} {extras}")),
    ],
    "formato_regla": C(FMJ, 13, 13, "Comma-separated phrases. No full sentences."),
    "literales_obligatorios": [],
    "parametros_externos": [
        P("--ar", "9:16, 16:9, 1:1 (desde project.aspect)", C(FMJ, 19, 19, "`--ar 9:16`, `--ar 16:9`, `--ar 1:1`")),
        P("--style", "raw / 4a / 4b / 4c; raw para fotorreal", C(FMJ, 20, 20, "`raw` / `4a` / `4b` / `4c`")),
        P("--s", "0–1000; 50 marca, 250 artístico", C(FMJ, 21, 21, "`50` for branded, `250` for artistic")),
        P("--c", "0–100; omitir salvo exploración", C(FMJ, 22, 22, "Use only when exploring variations")),
        P("--seed", "entero; fijar por storyboard", C(FMJ, 23, 23, "For series consistency, set per-storyboard")),
        P("--cref / --cw", "URL de referencia de personaje; --cw 0–100 (default 50)", C(FMJ, 24, 25, "Character weight. 100 = strict character match, 0 = clothing only")),
        P("--sref", "URL de referencia de estilo", C(FMJ, 26, 26, "Style reference")),
    ],
    "negativos": {"campo_aparte": None, "formato": None, "limite": None, "cita": C(FC, 17, 17, '"supports_negative_prompt": true'),
                  "nota": "la matriz declara soporte pero el adaptador no documenta la sintaxis (ver sin_fuente)"},
    "longitud": {"min": 40, "max": 80, "unidad": "palabras", "bloquea": False, "cita": C(FMJ, 30, 30, "Aim for **40–80 words per prompt** including parameters. Anything over 100 words underperforms."),
                 "citas_adicionales": [C(FC, 12, 12, '"max_prompt_words": 100')]},
    "prohibido": [
        X("'AI' o 'rendered'", C(FMJ, 97, 97, "Don't use \"AI\" or \"rendered\"")),
        X("más de tres adjetivos por frase nominal", C(FMJ, 98, 98, "three adjectives per noun phrase max")),
        X("texto en el prompt", C(FMJ, 99, 99, "Don't include text content")),
        X("--c en series", C(FMJ, 100, 100, "Don't use `--c` for series work")),
        X("cambiar --seed a mitad del storyboard", C(FMJ, 101, 101, "Don't change `--seed` mid-storyboard")),
    ],
    "referencias": {"max": None, "sintaxis_rol": "--cref {url} --cw 50 (personaje) / --sref {url} (estilo)", "cita": C(FCL, 64, 64, "For Midjourney: `--cref {url} --cw 50`")},
    "secciones_linter": [SL("1", ["subject", "style", "composition", "lighting", "aspect_ratio", "quality"], C(VY, 525, 525, "midjourney__1:"))],
}

modelos["flux"] = {
    "medio": "imagen",
    "formato": "prosa",
    "autoridad_sintaxis": C(APD, 126, 126, "la autoridad es el adaptador de `visual-prompt-forge`"),
    "secciones": [
        S("subject_action", None, 1, True, "encuadre + character anchor + acción", C(FFL, 63, 63, "{Framing description with character anchor and action}.")),
        S("environment", None, 2, True, "entorno de series_lock", C(FFL, 63, 63, "{Environment description from series_lock}.")),
        S("lighting", None, 3, True, "luz de series_lock", C(FFL, 63, 63, "{Lighting sentence from series_lock}.")),
        S("photographic_spec", None, 4, True, "cámara, lente, profundidad de campo", C(FFL, 63, 63, "{Photographic spec, camera, lens, depth of field}.")),
        S("grade_mood", None, 5, True, "grade y mood de brand_lock", C(FFL, 63, 63, "{Color grade and mood from brand_lock}.")),
        S("photoreal_closing", None, 6, True, "cierre fotorreal obligatorio", C(FFL, 66, 66, "Include in every prompt.")),
    ],
    "formato_regla": C(FFL, 13, 13, "Periods separate beats. Each sentence does one job. No bracket weights, no `--` flags."),
    "literales_obligatorios": [L("Photorealistic, natural skin texture, no AI artifacts.", "todo prompt", C(FFL, 63, 63, "Photorealistic, natural skin texture, no AI artifacts."))],
    "parametros_externos": [
        P("aspect_ratio", "campo de API, desde project.aspect", C(FFL, 21, 21, "`aspect_ratio` | API call field")),
        P("output_format", "png para composición", C(FFL, 22, 22, "`png` for compositing")),
        P("safety_tolerance", "2", C(FFL, 23, 23, "`safety_tolerance`")),
        P("prompt_upsampling", "false en series", C(FFL, 24, 24, "`false` for series work")),
        P("seed", "fijo por storyboard", C(FFL, 25, 25, "set per-storyboard for series consistency")),
    ],
    "negativos": {"campo_aparte": False, "formato": None, "limite": None, "cita": C(FC, 33, 33, '"supports_negative_prompt": false')},
    "longitud": {"min": 80, "max": 150, "unidad": "palabras", "bloquea": False, "cita": C(FFL, 36, 36, "Flux handles **80–150 words** comfortably."),
                 "citas_adicionales": [C(FC, 28, 28, '"max_prompt_words": 150')]},
    "prohibido": [
        X("muletillas de SD: highly detailed, 4k, masterpiece", C(FFL, 90, 90, "Don't write \"highly detailed, 4k, masterpiece\"")),
        X("sintaxis de pesos (thing:1.4)", C(FFL, 91, 91, "Don't use weight syntax `(thing:1.4)`")),
        X("prompt upsampling en series", C(FFL, 92, 92, "Don't enable prompt upsampling for series work")),
        X("texto en el prompt", C(FFL, 93, 93, "Don't include text content")),
        X("omitir el cierre fotorreal", C(FFL, 94, 94, "Don't omit the photoreal closing line")),
    ],
    "referencias": {"max": None, "sintaxis_rol": None, "cita": C(FCL, 78, 78, "Flux: not directly supported; bake style language into prompt instead"),
                    "citas_adicionales": [C(FC, 31, 32, '"supports_style_ref": false')]},
    "secciones_linter": [SL("1", ["subject", "action_or_pose", "environment", "lighting", "photographic_spec", "photoreal_closing"], C(VY, 549, 549, "flux__1:"))],
}

modelos["ideogram"] = {
    "medio": "imagen",
    "formato": "prosa",
    "autoridad_sintaxis": C(APD, 126, 126, "la autoridad es el adaptador de `visual-prompt-forge`"),
    "secciones": [
        S("subject_composition", None, 1, True, "sujeto y composición", C(FID, 27, 27, "{Subject and composition}.")),
        S("environment_lighting", None, 2, True, "entorno y luz", C(FID, 27, 27, "{Environment and lighting}.")),
        S("text", None, 3, False, "solo Modo 2: The text \"...\" appears {posición}, in {fuente}", C(FID, 27, 27, 'The text "{exact text}" appears {position description}, in {font style description}.')),
        S("brand_closing", None, 4, True, "mood y color de marca", C(FID, 27, 27, "{Brand mood and color closing.}")),
    ],
    "literales_obligatorios": [
        L("texto exacto entre comillas dobles rectas", "Modo 2 (texto en imagen)", C(FID, 30, 30, "The exact text must be in straight double-quotes.")),
        L("flag de override en rationale", "requisito para activar Modo 2", C(FID, 17, 17, "To trigger Mode 2, the shot must have an explicit override flag in rationale")),
        L("Clean composition with negative space for text overlay placement.", "Modo 1 (compuesto, default)", C(FID, 59, 59, "Clean composition with negative space for text overlay placement.")),
    ],
    "parametros_externos": [
        P("aspect_ratio", "campo de API", C(FID, 36, 36, "`aspect_ratio` | API field")),
        P("model", "V_3", C(FID, 37, 37, "`V_3`")),
        P("magic_prompt", "OFF en series", C(FID, 38, 38, "`OFF` for series work")),
        P("style_type", "DESIGN pósters / REALISTIC escenas", C(FID, 39, 39, "`DESIGN` for posters, `REALISTIC` for scenes")),
        P("seed", "fijo por storyboard", C(FID, 40, 40, "set per-storyboard")),
    ],
    "negativos": {"campo_aparte": None, "formato": None, "limite": None, "cita": C(FC, 49, 49, '"supports_negative_prompt": true'),
                  "nota": "soporte declarado; sintaxis no documentada (ver sin_fuente)"},
    "longitud": {"min": 60, "max": 120, "unidad": "palabras", "bloquea": False, "cita": C(FID, 50, 50, "Ideogram handles **60–120 words** comfortably."),
                 "citas_adicionales": [C(FC, 44, 44, '"max_prompt_words": 120')]},
    "prohibido": [
        X("Modo 2 sin override", C(FID, 90, 90, "Don't use Mode 2 without the rationale override")),
        X("magic_prompt", C(FID, 91, 91, "Don't trust magic_prompt")),
        X("varios elementos de texto", C(FID, 92, 92, "Don't pile multiple text elements in one prompt")),
        X("fuentes cursivas/decorativas", C(FID, 93, 93, "Don't use cursive/decorative fonts")),
    ],
    "referencias": {"max": None, "sintaxis_rol": "omni-reference (parámetro)", "cita": C(FCL, 66, 66, "For Ideogram: `omni-reference` parameter with the image."),
                    "citas_adicionales": [C(FC, 47, 48, '"supports_character_ref": false')]},
    "secciones_linter": [SL("1", ["subject", "environment", "lighting", "composition"], C(VY, 557, 557, "ideogram__1:"))],
}

modelos["seedream"] = {
    "medio": "imagen",
    "formato": "mixto",
    "formato_nota": "frases separadas por comas, sin oraciones completas",
    "autoridad_sintaxis": C(APD, 126, 126, "la autoridad es el adaptador de `visual-prompt-forge`"),
    "secciones": [
        S("framing_anchor", None, 1, True, "{Framing} of {character anchor}", C(FSR, 43, 43, "{Framing} of {character anchor}")),
        S("action", None, 2, True, "acción", C(FSR, 43, 43, "{action}")),
        S("environment", None, 3, True, "entorno de series_lock", C(FSR, 43, 43, "{environment from series_lock}")),
        S("lighting", None, 4, True, "luz de series_lock", C(FSR, 43, 43, "{lighting from series_lock}")),
        S("grade", None, 5, True, "grade de brand_lock", C(FSR, 43, 43, "{color grade from brand_lock}")),
        S("mood", None, 6, True, "un adjetivo de mood", C(FSR, 43, 43, "{one mood adjective}, photorealistic")),
    ],
    "formato_regla": C(FSR, 17, 17, "Comma-separated, no full sentences."),
    "literales_obligatorios": [L("photorealistic", "cierre del patrón", C(FSR, 43, 43, "{one mood adjective}, photorealistic"))],
    "parametros_externos": [
        P("aspect_ratio", "desde project.aspect", C(FSR, 25, 25, "`aspect_ratio` | from `project.aspect`")),
        P("seed", "por storyboard; crítico", C(FSR, 26, 26, "Critical for series consistency")),
        P("guidance_scale", "4.5", C(FSR, 27, 27, "`guidance_scale` | `4.5`")),
        P("steps", "28 (50 más calidad)", C(FSR, 28, 28, "`steps` | `28`")),
    ],
    "negativos": {"campo_aparte": None, "formato": None, "limite": None, "cita": C(FC, 97, 97, '"supports_negative_prompt": true'),
                  "nota": "soporte declarado; sintaxis no documentada (ver sin_fuente)"},
    "longitud": {"min": 40, "max": 70, "unidad": "palabras", "bloquea": False, "cita": C(FSR, 38, 38, "**40–70 words per prompt**. Shorter than most. Don't pad."),
                 "citas_adicionales": [C(FC, 92, 92, '"max_prompt_words": 120')]},
    "prohibido": [
        X("párrafos", C(FSR, 80, 80, "Don't write paragraphs")),
        X("sintaxis --ar", C(FSR, 81, 81, "Don't use `--ar` syntax")),
        X("texto en el prompt", C(FSR, 82, 82, "Don't include text content")),
        X("saltarse el seed lock en series", C(FSR, 84, 84, "Don't skip the seed lock for series work")),
    ],
    "referencias": {"max": None, "sintaxis_rol": None, "cita": C(FC, 95, 96, '"supports_character_ref": true')},
    "secciones_linter": [SL("1", ["subject", "framing", "environment", "lighting", "style"], C(VY, 563, 563, "seedream__1:"))],
}

# ------------------------- VIDEO -------------------------
modelos["kling-3"] = {
    "medio": "video",
    "formato": "shots_timecode",
    "autoridad_sintaxis": C(APD, 37, 37, "Sintaxis final de prompts de video"),
    "secciones": [
        S("characters", "[Character A: ...]", 1, True, "todos los personajes y objetos clave al inicio, con identificador único", C(KL, 65, 68, "[Character A: Exhausted Partner — late 40s, gray-streaked beard, navy peacoat, hollow eyes]")),
        S("master_intent", "Master intent:", 2, False, "intención de la escena (ejemplo oficial)", C(KL, 80, 80, "Master intent: tense negotiation in a glass-walled office at dusk.")),
        S("shots", "Shot 1 (0-3s).", 3, True, "un shot por línea con timecode; cada uno encuadre + sujeto + movimiento", C(KL, 82, 93, "framing + subject + motion")),
        S("camera", "Camera.", 4, False, "cámara global", C(KL, 88, 88, "Camera. Slow, deliberate. Sony FX6 feel, 35mm and 85mm.")),
        S("lighting", "Lighting.", 5, False, "luz global", C(KL, 89, 89, "Lighting. Cold blue dusk through floor-to-ceiling windows.")),
        S("audio", "Audio.", 6, False, "audio nativo", C(KL, 90, 90, "Audio. Distant city ambience.")),
        S("negative_field", "Negative field.", 7, True, "campo negativo dedicado (fuera del prompt principal)", C(KL, 360, 360, "Negative field. blurry, distorted hands, extra fingers, melted face, watermark, subtitles, jitter, dialogue overlap.")),
    ],
    "orden_capas": C(KL, 58, 61, "Scene → Characters → Action → Camera → Audio"),
    "literales_obligatorios": [
        L("[Character A: <identidad completa>]", "todo personaje; luego 'Character A' dentro de los shots", C(UR, 109, 109, "in-prompt `[Character A: <full identity>]` labels")),
        L("[Character A, raspy deep voice]: \"...\"", "diálogo: tono de voz dentro de la etiqueta (P3)", C(KL, 108, 108, '[Character A, raspy deep voice]: "We\'re out of time."')),
        L("anclaje visual antes del diálogo (P2)", "toda línea de diálogo", C(KL, 104, 104, "Character A pulls a folded note from his pocket and reads aloud")),
        L("Immediately,", "entre líneas de diálogo consecutivas (P4)", C(KL, 113, 113, "Immediately,")),
        L("Preserve identity, wardrobe, and the storefront sign exactly.", "image-to-video 3.0", C(KL, 121, 121, "Preserve identity, wardrobe, and the storefront sign exactly.")),
        L("[Character A: same person from the image]", "image-to-video 3.0", C(KL, 122, 122, "[Character A: same person from the image]")),
        L("locked static frame / camera fixed, no movement", "deriva de cámara en escena estática", C(KL, 265, 265, 'Say "locked static frame" or "camera fixed, no movement."')),
    ],
    "parametros_externos": [
        P("cfg_scale", "0-1, default 0.5; 0.3-0.4 libertad, 0.7-1.0 adherencia estricta", C(KL, 155, 155, "cfg_scale` 0-1, default 0.5")),
        P("duration", "suma de duraciones por shot ≤ 15s", C(KL, 156, 156, "per-shot durations must sum to ≤ 15s")),
        P("duration (forge)", "5s o 10s", C(FKL, 21, 21, "5s and 10s are the supported lengths")),
        P("aspect_ratio", "16:9 / 9:16 / 1:1", C(KL, 157, 157, "16:9 / 9:16 / 1:1")),
        P("generate_audio", "bool; no hay toggle 'no music'", C(KL, 158, 158, "the model lays music even against a negative prompt")),
        P("start_image", "opcional; fija el frame de apertura", C(FKL, 24, 24, "to lock the opening frame")),
        P("tail_image", "opcional; frame final objetivo", C(FKL, 25, 25, "End-frame target for controlled moves")),
        P("negative_prompt", "soportado", C(FKL, 26, 26, "`negative_prompt` | per series | Supported.")),
        P("tiers", "v3/pro, v3/standard; Turbo 3-15s tope 1080p; Omni 4K edición/referencias", C(KL, 35, 35, "capped at 1080p — no 4K")),
    ],
    "negativos": {"campo_aparte": True, "formato": "escribir la cosa misma, no 'no X'", "limite": "lista corta; SW30 R16 ≤8 ítems",
                  "cita": C(KL, 189, 189, 'Do not write "no X". Write the thing itself.'),
                  "citas_adicionales": [C(KL, 203, 203, "Keep the list short. Long negative stacks reduce motion and detail."), C(SW, 143, 144, "negativos sin \"no X\", ≤8 ítems"), C(VY, 393, 393, "kling: required")]},
    "longitud": {"min": 30, "max": 60, "unidad": "palabras por shot", "bloquea": False, "cita": C(KL, 182, 182, "Plan ~30-60 words per shot."),
                 "i2v": {"min": 20, "max": 40, "cita": C(KL, 183, 183, "Image-to-video (any version). 20-40 words.")},
                 "citas_adicionales": [C(FKL, 37, 37, "Kling handles **80–150 words** comfortably."), C(FC, 108, 108, '"max_prompt_words": 150'), C(VY, 437, 437, "i2v: [20, 40]")]},
    "prohibido": [
        X("etiquetas genéricas [Man]: / [Woman]:", C(KL, 110, 110, "(vague — model picks a generic voice)")),
        X("dos líneas de diálogo consecutivas sin transición", C(KL, 114, 114, "lines with no transition (model overlaps them)")),
        X("dos shots adyacentes con mismo encuadre y ángulo", C(KL, 289, 289, "If two adjacent shots share both framing and angle, the model merges them.")),
        X("dos personajes que hablan con una sola descripción visual", C(KL, 305, 305, "Never let two speaking characters share one visual description.")),
        X("texto en pantalla", C(FKL, 83, 83, "Don't include text content.")),
        X("varios movimientos de cámara por shot (forge)", C(FKL, 81, 81, "Don't request multiple camera moves in one shot.")),
    ],
    "referencias": {"max": 4, "max_nota": "Elements 3.0 (Omni): video 3-8s o hasta 4 stills multi-ángulo + voice binding 5-30s por elemento",
                    "sintaxis_rol": "@Grace picks up the folder (elemento etiquetado en prosa)",
                    "cita": C(KL, 232, 233, "@Grace picks up the folder"),
                    "citas_adicionales": [C(KL, 232, 232, "(front, three-quarter, profile, back)"), C(KL, 234, 234, "has its own element"), C(KL, 235, 235, "visible image-quality degradation the moment elements/references are enabled")]},
    "secciones_linter": [
        SL("3a", ["scene_or_motion", "subject_action", "camera", "style", "anti_morphing"], C(VY, 601, 601, "kling_3.0__3a:")),
        SL("3b", ["scene_or_motion", "transition_FF_LF", "camera", "style", "anti_morphing"], C(VY, 634, 634, "kling_3.0__3b:")),
        SL("3c", ["scene", "motion_reference", "character_orientation", "camera"], C(VY, 656, 656, "kling_3.0__3c:")),
        SL("4", ["character_tags", "shot_list", "dialogue", "voice_tag", "temporal_link", "audio"], C(VY, 663, 663, "kling_3.0__4:")),
    ],
}

modelos["kling-2x"] = {
    "medio": "video",
    "formato": "prosa",
    "autoridad_sintaxis": C(APD, 37, 37, "Sintaxis final de prompts de video"),
    "versiones": C(KL, 162, 162, "For 1.6, 2.1 Pro, 2.5 Turbo Pro, 2.6 Pro:"),
    "secciones": [
        S("subject", None, 1, True, "sujeto con detalles / ancla de identidad", C(KL, 165, 165, "Subject (with specific details)")),
        S("subject_movement", None, 2, True, "un verbo limpio", C(KL, 166, 166, "+ Subject Movement (one clean verb phrase)")),
        S("scene", "Scene.", 3, True, "3-5 elementos máx.", C(KL, 167, 167, "+ Scene (3-5 elements max)")),
        S("camera", "Camera.", 4, True, "un movimiento + lente", C(KL, 168, 168, "+ Camera Language")),
        S("lighting", "Lighting.", 5, True, "fuente + calidad", C(KL, 169, 169, "+ Lighting")),
        S("atmosphere", "Atmosphere.", 6, True, "mood", C(KL, 170, 170, "+ Atmosphere")),
        S("negative_field", "Negative field.", 7, True, "campo negativo dedicado", C(KL, 322, 322, "Negative field. blurry, distorted hands, extra fingers, melted face, watermark, subtitles, jitter.")),
    ],
    "esqueleto_literal": C(KL, 320, 320, "Scene. [3-5 environment elements]. Camera. [one movement + lens]. Lighting. [source + quality]. Atmosphere. [mood]."),
    "formato_regla": C(KL, 173, 173, "Write as flowing prose. Kling 1.x – 2.x dislikes fragmented tag-style inputs."),
    "literales_obligatorios": [
        L("Preserve [silhouette / label / specific feature].", "image-to-video", C(KL, 328, 328, "Preserve [silhouette / label / specific feature].")),
        L("preserve X", "image-to-video: cues de continuidad", C(KL, 251, 251, 'Kling responds well to "preserve X" instructions.')),
    ],
    "parametros_externos": [
        P("Bind Elements", "activar en ajustes Image-to-Video (1.x–2.x)", C(KL, 215, 215, 'enable "Bind Elements" to lock features')),
        P("Motion Brush", "hasta 6 regiones; el texto DEBE coincidir con el pincel (2.1 Pro)", C(KL, 241, 241, "The text prompt MUST match the brush motion.")),
        P("End frame control", "2.1 Pro", C(KL, 31, 31, "End frame control.")),
        P("Motion Control", "2.6 Pro: copia movimiento de video de referencia; el prompt describe solo al sujeto", C(KL, 245, 245, "The prompt then focuses on subject description only, the reference handles motion.")),
    ],
    "negativos": {"campo_aparte": True, "formato": "la cosa misma, no 'no X'", "limite": "lista corta", "cita": C(KL, 189, 189, 'Do not write "no X". Write the thing itself.'),
                  "citas_adicionales": [C(FX, 220, 220, "For Kling field. Rewrite as positive entities.")]},
    "longitud": {"min": 50, "max": 80, "unidad": "palabras", "bloquea": False, "cita": C(KL, 180, 181, "2.6 Pro. 5-7 elements. 50-80 words."),
                 "i2v": {"min": 20, "max": 40, "cita": C(KL, 183, 183, "Image-to-video (any version). 20-40 words.")},
                 "citas_adicionales": [C(KL, 185, 185, "Long prompts on 1.x – 2.x = melted outputs.")]},
    "prohibido": [
        X("exceder elementos: 3-4 Turbo, 5-7 2.6 Pro", C(KL, 269, 269, "Cut to model-appropriate element count. 3-4 for Turbo, 5-7 for 2.6 Pro.")),
        X("re-describir elementos estáticos en I2V", C(KL, 249, 249, "Do not re-describe static elements the model already sees.")),
    ],
    "referencias": {"max": 4, "sintaxis_rol": "Element Library: 3-4 refs frente / perfil / tres cuartos + Bind Elements", "cita": C(KL, 207, 207, "Upload 3-4 reference images of the character from different angles."),
                    "citas_adicionales": [C(KL, 220, 220, "Even lighting. Avoid hard shadows. The AI can mistake them for permanent facial features.")]},
}

modelos["veo-3.1"] = {
    "medio": "video",
    "formato": "mixto",
    "formato_nota": "prosa + etiquetas Audio:/Says:/SFX:/Duration:; JSON opcional para continuidad estricta",
    "autoridad_sintaxis": C(APD, 37, 37, "Sintaxis final de prompts de video"),
    "secciones": [
        S("subject_action", None, 1, True, "sujeto y acción", C(VE, 35, 35, "[Subject / Action]")),
        S("environment", None, 2, True, "entorno", C(VE, 36, 36, "+ [Environment / Setting]")),
        S("camera", None, 3, True, "encuadre + lente + movimiento", C(VE, 37, 37, "+ [Camera / Shot Type / Lens]")),
        S("lighting", None, 4, True, "dirección + temperatura", C(VE, 38, 38, "+ [Lighting / Atmosphere]")),
        S("style", None, 5, False, "estilo, mood, paleta (al final)", C(VE, 39, 39, "+ [Style / Quality]")),
        S("audio", "Audio:", 6, True, "ambiente, SFX, textura musical; señal explícita", C(VE, 232, 232, "Audio: [ambient sounds, SFX, music texture].")),
        S("says", "Says:", 7, False, "diálogo, máx 8 s de habla", C(VE, 233, 233, 'Says: [character] says, "[dialogue, max 8 seconds of speech]."')),
        S("sfx", "SFX:", 8, False, "eventos sonoros puntuales", C(VE, 234, 234, "SFX: [punctual sound events].")),
        S("duration", "Duration:", 9, True, "4 / 6 / 8 segundos", C(VE, 236, 236, "Duration: [4 / 6 / 8] seconds.")),
    ],
    "orden_regla": C(VE, 32, 32, "Order matters. Lead with subject and camera. Quality modifiers go at the end."),
    "formato_json": L("JSON: version / output / global_style / continuity / scenes[]", "varias escenas, continuidad estricta, props que no deben cambiar de color", C(VE, 99, 105, '"version": "veo-3.1",')),
    "literales_obligatorios": [
        L("<Personaje> says: \"<línea>\" (comillas dobles + verbo introductor; dos puntos más fiable)", "diálogo", C(VE, 63, 66, 'A woman says: "Welcome to the future."')),
        L("modificadores de voz antes del verbo", "diálogo", C(VE, 71, 71, "Place modifiers before the lead-in verb.")),
        L("maintain the subject from the first frame", "image-to-video", C(VE, 178, 178, "maintain the subject from the first frame")),
        L("The character from reference_1 ... location from reference_2 ... object from reference_3", "reference ingredients", C(VE, 194, 194, "The character from reference_1 walks into the location from reference_2 holding the object from reference_3.")),
        L("Audio: / Says: / SFX:", "siempre que se quiera audio: señal explícita", C(VE, 95, 95, "The model needs an explicit signal that audio should be generated.")),
    ],
    "parametros_externos": [
        P("duration", "4, 6 u 8 s", C(VE, 27, 27, "Duration. 4, 6, or 8 seconds.")),
        P("duration (forge)", "8s nativo", C(FVE, 19, 19, "Veo's native clip length")),
        P("output (JSON)", "duration_sec, fps, resolution, aspect_ratio", C(VE, 106, 110, '"aspect_ratio": "16:9"')),
        P("generate_audio (forge)", "true; false solo en shots mudos", C(FVE, 21, 21, "Set `false` only for silent shots")),
        P("start_image (forge)", "image-to-video desde still aprobado", C(FVE, 22, 22, "Image-to-video from an accepted still")),
        P("First Frame", "3.1: imagen estática como primer frame", C(VE, 172, 172, "Uses the static image as First Frame.")),
    ],
    "negativos": {"campo_aparte": False, "formato": "en el cuerpo del texto; bans directos fiables ('Pure video, no subtitles, no background music')", "limite": None,
                  "cita": C(FX, 214, 214, "Where negatives are supported (Kling field, Veo body text, Seedance 2.0 fragile)."),
                  "citas_adicionales": [C(FX, 157, 157, "On Seedance 2.5 and Veo this is reliable."), C(FC, 129, 129, '"supports_negative_prompt": false'), C(VY, 398, 398, "veo: optional")]},
    "longitud": {"min": 50, "max": 200, "unidad": "palabras", "bloquea": False, "cita": C(VE, 44, 44, "Sweet spot. 50-200 words."),
                 "citas_adicionales": [C(VE, 223, 223, "Compress to the 50-100 word range."), C(FVE, 31, 31, "Veo handles **80–150 words**."), C(FC, 124, 124, '"max_prompt_words": 150')]},
    "dialogo_limite": {"max_segundos_habla": 8, "cita": C(VE, 28, 28, "Dialogue budget. Max 8 seconds of spoken audio per clip."),
                       "citas_adicionales": [C(FVE, 39, 39, "roughly 12–18 words for an 8s clip")]},
    "prohibido": [
        X("re-describir elementos estáticos en I2V", C(VE, 176, 176, "Do not re-describe static elements.")),
        X("texto en pantalla (sí líneas habladas)", C(FVE, 77, 77, "Don't put on-screen text in the prompt.")),
        X("dos movimientos de cámara", C(FVE, 78, 78, "Don't stack two camera moves.")),
        X("Veo para B-roll mudo", C(FVE, 75, 75, "Don't use Veo for silent B-roll.")),
    ],
    "referencias": {"max": None, "sintaxis_rol": "reference_1 / reference_2 / reference_3 (personaje, locación, prop)", "cita": C(VE, 191, 191, "Upload multiple reference images (character, location, prop) and tag them in the prompt.")},
    "secciones_linter": [
        SL("3a", ["subject_action", "timing_or_beat", "camera", "style", "physics_cue"], C(VY, 608, 608, "veo_3.1__3a:")),
        SL("3b", ["transition_FF_LF", "timing_or_beat", "camera", "physics_cue", "anti_morphing"], C(VY, 641, 641, "veo_3.1__3b:")),
        SL("4", ["subject_action", "dialogue", "tone_or_accent", "timing", "audio_specs"], C(VY, 671, 671, "veo_3.1__4:")),
    ],
}

modelos["seedance-2.0"] = {
    "medio": "video",
    "formato": "shots_timecode",
    "autoridad_sintaxis": C(APD, 37, 37, "Sintaxis final de prompts de video"),
    "secciones": [
        S("anti_mush_guard", "Important direction:", 0, False, "arriba de todo cuando el modelo fusiona cortes o preventivo en multi-shot pesado", C(SD, 200, 203, "Important direction:")),
        S("character_lock", "[1] Character lock.", 1, True, "@img1 + bloque de identidad completo + vestuario exacto", C(SD, 99, 100, "Use @img1 as the main character reference and preserve the exact same person")),
        S("length_genre_editing", "[2] Length + genre + editing intent.", 2, True, "duración, género, ritmo de edición", C(SD, 105, 105, "[2] Length + genre + editing intent.")),
        S("story", "[3] Story (one paragraph).", 3, True, "eventos físicos en presente; punto de quiebre", C(SD, 109, 109, "[3] Story (one paragraph).")),
        S("visual_style", "[4] Visual style.", 4, True, "paleta, contraste, grano, qué evitar", C(SD, 113, 113, "[4] Visual style.")),
        S("camera_style", "[5] Camera style.", 5, True, "cámara, lentes con propósito, cortes", C(SD, 117, 117, "[5] Camera style.")),
        S("editing_style", "[6] Editing style.", 6, True, "cortes, escalada rítmica", C(SD, 123, 123, "[6] Editing style.")),
        S("audio", "[7] Audio.", 7, True, "sonidos diegéticos en orden", C(SD, 127, 127, "[7] Audio.")),
        S("timeline", "[8] Shot-by-shot timeline.", 8, True, "Shot N, t–t sec: encuadre, lente, movimiento, acción", C(SD, 132, 133, "Shot 1, 0.0–X.X sec")),
        S("lighting", "[9] Lighting (recap and specifics).", 9, True, "fuente principal, relleno, rim, temperatura", C(SD, 139, 139, "[9] Lighting (recap and specifics).")),
        S("composition", "[10] Composition.", 10, True, "posición en cuadro; la imagen final debe nombrarse", C(SD, 143, 145, "The final image must be named.")),
        S("output_specs", "[11] Output specs.", 11, True, "duración, ratio, realismo, cola CLI", C(SD, 147, 149, "[11] Output specs.")),
    ],
    "formato_regla": C(SD, 96, 96, "Each block answers a specific failure mode. Skipping a block reintroduces that failure."),
    "formato_rapido": L("Subject. / Motion. / Camera. / Environment. / Lighting. / Style.", "un solo shot de 5s con una acción", C(SD, 84, 89, "Style. [Realism level, genre reference]")),
    "literales_obligatorios": [
        L("Use @img1 as the main character reference and preserve the exact same person ...", "personaje con referencia", C(SD, 100, 100, "Use @img1 as the main character reference and preserve the exact same person")),
        L("This must be a clearly edited multi-shot sequence with visible cuts between shots. Do not generate a single continuous take.", "multi-shot (anti-mush)", C(SD, 204, 205, "Do not generate a single continuous take.")),
        L("Cut to. / Camera cut to. / Camera switching. / Lens switch to.", "marcadores de corte", C(SD, 176, 179, "Cut to. [description]")),
        L("no music", "cuando no se quiere música", C(SD, 275, 275, "explicitly when you want none")),
        L("diálogo entre comillas dobles (1.5/2.0)", "diálogo", C(SD, 273, 273, "on 1.5/2.0 — the model voices it")),
        L("rol de cada referencia en prosa: @img1 protagonista, @img2 locación, @img3 vestuario", "varias referencias", C(SD, 228, 228, "is the protagonist,")),
    ],
    "parametros_externos": [
        P("CLI (al final del prompt)", "--resolution 1080p --duration 5 --camerafixed false --seed 42", C(SD, 45, 48, "--resolution 1080p --duration 5 --camerafixed false --seed 42")),
        P("--duration", "2 a 12 (Pro)", C(SD, 52, 52, "2 to 12 (Pro)")),
        P("--camerafixed", "true bloquea la cámara", C(SD, 53, 53, "true locks the camera. false allows movement.")),
        P("--resolution", "480p | 720p | 1080p; 2.0 añade 4K nativo", C(SD, 37, 37, "Resolutions. 480p, 720p, 1080p; 2.0 adds native 4K")),
        P("aspect ratio", "16:9, 4:3, 1:1, 3:4, 9:16, 21:9, 9:21", C(SD, 38, 38, "Aspect ratios. 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, 9:21.")),
        P("shots (forge)", "número de cortes en modo multi-shot", C(FSD, 28, 28, "Number of cuts in the sequence when using multi-shot mode")),
        P("start_image (forge)", "referencia del frame de apertura", C(FSD, 27, 27, "Image-to-video reference for the opening frame")),
    ],
    "negativos": {"campo_aparte": False, "formato": "invertir a positivo en el cuerpo (1.x/2.0); 2.0 soporte limitado y frágil", "limite": None,
                  "cita": C(SD, 250, 252, "Always invert to positive phrasing."),
                  "citas_adicionales": [C(SD, 248, 248, "Seedance 1.0 Pro does NOT support negative prompts."), C(FC, 145, 145, '"supports_negative_prompt": false'), C(VY, 395, 395, "seedance: optional")]},
    "longitud": {"min": 80, "max": 150, "unidad": "palabras", "bloquea": False, "cita": C(FSD, 37, 37, "Seedance handles **80–150 words**."),
                 "citas_adicionales": [C(FC, 140, 140, '"max_prompt_words": 150')]},
    "multi_shot_limite": {"max": 5, "cita": C(SD, 196, 196, "Hard cap: 5 shots per generation"), "citas_adicionales": [C(FSD, 75, 75, "Don't write more than ~4 cuts per generation.")]},
    "prohibido": [
        X("fraseo perezoso: cinematic, professional, high quality, masterpiece", C(SD, 71, 71, '"cinematic, professional, high quality, masterpiece"')),
        X("describir elementos ya visibles en la imagen (I2V)", C(SD, 258, 258, "DO NOT describe elements already visible in the image.")),
        X("rostros humanos en 2.0 (filtro agresivo)", C(SD, 41, 41, "2.0 aggressively filters human faces")),
        X("texto en pantalla (forge)", C(FSD, 77, 77, "Don't include text content.")),
    ],
    "referencias": {"max": 12, "max_nota": "hasta 9 imágenes, 3 videos, 3 audios", "sintaxis_rol": "@img1, @img2 ... / @Video1 / @Audio1 con rol en prosa",
                    "cita": C(SD, 229, 229, "Limits: 12 files total on 2.0 (up to 9 images, 3 videos, 3 audio); up to 50 on 2.5.")},
    "secciones_linter": [SL("3a", ["subject_action", "camera", "audio"], C(VY, 615, 615, "seedance__3a:"))],
}

modelos["seedance-2.5"] = {
    "medio": "video",
    "formato": "mixto",
    "formato_nota": "declaración de referencias + resumen + plot por timeline/etapas + cola global; marcadores ( ) < > { } 【 】",
    "autoridad_sintaxis": C(APD, 37, 37, "Sintaxis final de prompts de video"),
    "secciones": [
        S("reference_declaration", None, 1, False, "cada asset por orden de subida + su rol", C(S25, 70, 73, "Complete prompt = [reference declaration] + [one-line summary] + [plot by timeline] + [global tail]")),
        S("one_line_summary", None, 2, False, "sujeto + lugar + evento + género/estilo + tratamiento de cámara", C(S25, 74, 74, "One-line summary.")),
        S("plot_by_timeline", "[Stage N] / [start-end s]", 3, True, "por beat: contenido positivo + bans locales; una acción principal por etapa con estado final visible", C(S25, 144, 149, "[Stage 1] Initial state: ... Primary event: <one primary action>. End state: <visible state>.")),
        S("maintain_consistency", "[Maintain Consistency]", 4, False, "identidad, conteo, vestuario, pertenencia de props, dirección espacial, audio", C(S25, 153, 153, "[Maintain Consistency] Keep <identity, count, clothing, prop ownership,")),
        S("global_tail", None, 5, True, "re-declarar globales y repetir bans globales", C(S25, 76, 76, "Re-state the must-hold globals")),
        S("negative_prompts", "[Negative Prompts]", 6, False, "prohibiciones específicas del colapso de ESTA escena", C(S25, 368, 368, "[Negative Prompts] No exaggerated crying, no fast cuts, no large body")),
    ],
    "formula_base": C(S25, 61, 64, "<Subject> performs <primary action or event> in <scene and environment>."),
    "esqueleto_3_modulos": C(S25, 172, 185, "[start-end s] [beat name] — physical directives"),
    "literales_obligatorios": [
        L("(música) <SFX> {diálogo} 【títulos】", "todo audio/diálogo/texto: no describir audio en prosa suelta", C(S25, 82, 89, "do not describe audio in loose prose")),
        L("Dialogue language + regional variety or accent + delivery style + speaker + {line}", "diálogo", C(S25, 91, 91, "Dialogue language + regional variety or accent + delivery style + speaker + {line}")),
        L("@Image 1 defines <subject>'s <appearance, clothing, structure, or material>.", "toda referencia", C(S25, 108, 108, "@Image 1 defines <subject>'s <appearance, clothing, structure, or material>.")),
        L("Pure video, no subtitles, no background music", "evitar subtítulos/BGM; repetir en la cola global", C(S25, 34, 34, '"Pure video, no subtitles, no background music"')),
        L("retaining real fine pores and skin texture", "humanos realistas (anti piel plástica)", C(S25, 202, 202, '"retaining real fine pores and skin texture"')),
        L("prohibit rigid cutting, prohibit objects appearing out of thin air", "toda transición", C(S25, 225, 225, '"prohibit rigid cutting, prohibit objects appearing out of thin air"')),
        L("One continuous shot, no cuts of any kind", "one-take", C(S25, 329, 329, '"One continuous shot, no cuts of any kind"')),
        L("@Video 1 is the sole editing master", "edición de video", C(S25, 245, 245, "[Source Video Role] @Video 1 is the sole editing master.")),
    ],
    "parametros_externos": [
        P("duration / aspect ratio / resolution", "en la página de generación o API; NO en el prompt", C(S25, 52, 52, "they do not belong in the prompt")),
        P("duration", "-1 o 4-30 s", C(S25, 45, 45, "(duration `-1` or 4-30)")),
        P("resolution", "480p / 720p en Jimeng web", C(S25, 49, 49, "480p / 720p")),
        P("Ultra Long", "30-180 s; re-declarar duración y ratio arriba del prompt", C(S25, 283, 283, "Restate duration and aspect ratio at the top of the prompt.")),
        P("auto-lock", "edición bloquea ratio y duración; first/last frame bloquea ratio al primer frame", C(S25, 54, 54, "first/last frame locks ratio to the first image (a mismatched last frame gets stretched)")),
        P("extension", "+4-30 s por pase, techo 60 s", C(S25, 262, 262, "hard ceiling 60s")),
    ],
    "negativos": {"campo_aparte": False, "formato": "bans directos 'no X' fiables; lista específica de modos de colapso en [Negative Prompts]/Prohibitions", "limite": None,
                  "cita": C(S25, 191, 191, "The prohibition list is specific, not generic."),
                  "citas_adicionales": [C(SD, 254, 254, "Direct bans are reliable"), C(VY, 394, 394, "seedance_2.5: required")]},
    "longitud": {"min": None, "max": None, "unidad": "palabras", "bloquea": False, "cita": C(VY, 452, 452, "seedance-25.md no fija número y sus ejemplos oficiales (§19) la superan"),
                 "nota": "sin cifra en la fuente; la tabla del linter usa 80-150 del adaptador forge 2.0 solo como referencia"},
    "timestamps": [
        X("rangos consecutivos y sin solape", C(S25, 159, 159, "Ranges must be consecutive and non-overlapping.")),
        X("ventanas de 3 s o más", C(S25, 160, 160, "Windows of 3 seconds or more.")),
        X("una acción central + un movimiento de cámara por ventana", C(S25, 161, 161, "One core action + one camera move per window.")),
    ],
    "prohibido": [
        X("forma colectiva '@Images 1 through 4 define four characters respectively'", C(S25, 115, 115, "The officially forbidden pattern")),
        X("re-describir lo que la referencia ya define", C(S25, 117, 117, "Do not restate what a reference already defines.")),
        X("cola CLI de 1.x/2.0", C(SD, 56, 56, "Not 2.5 syntax.")),
    ],
    "referencias": {"max": 50, "max_nota": "30 imágenes + 10 videos + 10 audios", "sintaxis_rol": "@Image N defines ... / @Video N defines ... / @Audio N defines ...; exclusiones explícitas",
                    "cita": C(S25, 32, 32, "(30 images + 10 videos + 10 audio)"),
                    "citas_adicionales": [C(S25, 103, 103, "Every material's role must be written in the prompt."), C(S25, 116, 116, '"Do not use the image background."')]},
    "secciones_linter": [
        SL("3a", ["reference_role", "subject_action", "camera", "audio_markers", "end_state"], C(VY, 620, 620, "seedance_2.5__3a:")),
        SL("3b", ["reference_role", "subject_action", "camera", "transition", "end_state"], C(VY, 648, 648, "seedance_2.5__3b:")),
        SL("4", ["dialogue_marker", "dialogue_language", "subject_action", "camera", "end_state"], C(VY, 678, 678, "seedance_2.5__4:")),
    ],
}

modelos["hailuo"] = {
    "medio": "video",
    "formato": "prosa",
    "autoridad_sintaxis": C(APD, 126, 126, "la autoridad es el adaptador de `visual-prompt-forge`"),
    "secciones": [
        S("camera", None, 1, True, "oración de movimiento de cámara, al frente", C(FHA, 12, 12, "{Camera motion sentence, leading.}")),
        S("subject_action", None, 2, True, "sujeto y acción durante la duración", C(FHA, 12, 12, "{Subject and action over the duration.}")),
        S("environment_lighting", None, 3, True, "entorno y luz de series_lock", C(FHA, 12, 12, "{Environment and lighting from series_lock.}")),
        S("grade_mood", None, 4, True, "grade y mood de brand_lock", C(FHA, 12, 12, "{Color grade and mood from brand_lock.}")),
    ],
    "literales_obligatorios": [],
    "parametros_externos": [
        P("duration", "6s", C(FHA, 19, 19, "`duration` | `6s`")),
        P("aspect_ratio", "desde project.aspect", C(FHA, 20, 20, "`aspect_ratio` | from `project.aspect`")),
        P("start_image", "image-to-video", C(FHA, 21, 21, "Image-to-video from an accepted still")),
        P("prompt_optimizer", "false en series", C(FHA, 22, 22, "`prompt_optimizer` | `false` for series")),
    ],
    "negativos": {"campo_aparte": False, "formato": None, "limite": None, "cita": C(FC, 161, 161, '"supports_negative_prompt": false'),
                  "citas_adicionales": [C(VY, 403, 403, "hailuo: optional")]},
    "longitud": {"min": 60, "max": 120, "unidad": "palabras", "bloquea": False, "cita": C(FHA, 31, 31, "Hailuo handles **60–120 words** efficiently."),
                 "citas_adicionales": [C(FC, 156, 156, '"max_prompt_words": 120')]},
    "prohibido": [
        X("entregar borradores Hailuo como finales", C(FHA, 65, 65, "Don't ship Hailuo drafts as finals.")),
        X("prompt optimizer en series", C(FHA, 66, 66, "Don't enable the prompt optimizer for series work.")),
        X("dos movimientos de cámara", C(FHA, 67, 67, "Don't stack two camera moves.")),
        X("texto en el prompt", C(FHA, 68, 68, "Don't include text content.")),
    ],
    "referencias": {"max": None, "sintaxis_rol": None, "cita": C(FC, 159, 159, '"supports_character_ref": true')},
    "secciones_linter": [SL("3a", ["camera", "subject_action", "light_change", "mood"], C(VY, 627, 627, "hailuo__3a:"))],
}

modelos["sora"] = {
    "medio": "video",
    "formato": None,
    "cobertura": "parcial: solo snapshot de secciones del linter para caso 4 y menciones en descripciones; sin archivo de modelo ni adaptador",
    "mencion": C(AU, 3, 3, "Kling 3.0/Veo 3.1/Sora 2/GPT Image 2/Nano Banana Pro/Midjourney"),
    "secciones": [],
    "literales_obligatorios": [],
    "parametros_externos": [],
    "negativos": None,
    "longitud": None,
    "prohibido": [],
    "referencias": None,
    "secciones_linter": [SL("4", ["subject_action", "dialogue", "tone_or_accent", "timing", "audio_specs"], C(VY, 685, 685, "sora_2__4:"))],
}

# =====================================================================
# POR CASO IMAGEN
# =====================================================================
por_caso_imagen = {
    "T1_genesis_rostro": [
        R("La génesis fija solo la parte del sujeto que lleva la identidad; rostro T1 antes que cuerpo T2", "orden de producción", C(DE, 20, 20, "Rostro T1 antes que cuerpo T2, siempre.")),
        R("Template canónico T1 obligatorio con cuatro bloques; el motor lanza TemplateViolation si se sustituye alguno", "estructura", C(SW, 66, 67, "Todo maestro de rostro")),
        R("light_hard: luz dura sin relleno, rasante; softbox PROHIBIDA en rostros", "light", C(SW, 71, 71, "luz dura sin relleno, rasante: los poros proyectan sombra")),
        R("skin_doc: defectos concretos de piel, no 'imperfecciones sutiles'", "skin / details", C(SW, 72, 72, "defectos concretos (rojeces, descamación, sudor, pigmento desigual")),
        R("usecase_doc: fotografía documental Kodak Tri-X; Kodak Portra PROHIBIDO en rostros", "usecase", C(SW, 73, 73, "fotografía documental Kodak Tri-X de reportaje")),
        R("clean_doc: anti-belleza explícito", "constraints / clean", C(SW, 74, 74, "no beauty retouching, no skin smoothing, no even complexion, no soft fill light")),
        R("Describir una cara IRREGULAR (caballete, cicatriz, ojos hundidos, asimetrías)", "subject / rasgos", C(SW, 76, 76, "describir una cara IRREGULAR")),
        R("Longitud ~250 palabras; un slot de 300+ compite consigo mismo", "prompt completo", C(SW, 79, 80, "el prompt completo se mantiene alrededor de 250 palabras")),
        R("Ensamblar con P(scene, subject, [details], mood, usecase, [constraints])", "estructura", C(SW, 42, 42, "P(scene, subject, [details], mood,")),
        R("Metadatos Model/Quality/Size fuera del cuerpo", "cabecera", C(SW, 90, 90, "se cuela un metadato (Model/Quality/Size/Aspect ratio) dentro del cuerpo del prompt")),
        R("Probar NB2 y NBP para rostros; GPT Image 2 high para piel e identidad", "modelo", C(NB, 146, 146, "для портретной серии сначала тестируй оба")),
        R("GPT Image 2 quality high para retratos", "parámetro quality", C(GI, 47, 47, "Маленький/плотный текст, infographics, портреты, identity-sensitive edits, brand assets")),
        R("Linter: T1 se mapea a caso 1 (génesis)", "gate aurora", C(PL, 193, 193, '"T1": "1"')),
        R("Ángulo eye-level para maestros de identidad", "cámara / D9", C(FA, 139, 139, "Eye-level para maestros de identidad"), origen=INF),
        R("Como character ref para Kling: luz pareja, sin sombras duras, fondo limpio, 1080p+, sin texto (ver conflicto con light_hard)", "light", C(KL, 219, 222, "Even lighting. Avoid hard shadows. The AI can mistake them for permanent facial features.")),
    ],
    "T2_cuerpo_con_ref": [
        R("Todo lo que extiende la génesis es un paso posterior con la génesis adjunta como referencia", "referencias", C(DE, 20, 20, "todo lo que la extiende es un paso posterior con esa génesis adjunta como referencia")),
        R("Herencia mínima: 'same face and clothes' + solo deltas; cero re-descripción", "subject", C(SW, 123, 124, 'Herencia mínima: "same face and clothes" + solo los deltas')),
        R("Autocontención: todo 'same X' exige ambos referentes adjuntos en ese prompt", "referencias", C(SW, 122, 122, "Autocontención: toda comparación (\"same X\") exige ambos referentes adjuntos en ESE prompt.")),
        R("Ancla con refs de personaje: bloque de identidad completo y verbatim (decisión 3)", "subject / identity block", C(DE, 10, 10, "Referencia de personaje sin start frame, casos con @img, Elements o ancla con refs: bloque de identidad completo y verbatim")),
        R("Frase clave de identidad desde Image 1", "subject", C(CH, 14, 14, 'Key phrase: "Keep facial features exactly the same as Image 1"')),
        R("Indexar referencias con rol (NB)", "referencias", C(NB, 69, 72, "Combine: face from Image 1, outfit style from Image 2, setting from Image 3.")),
        R("Indexar referencias con rol (GPT Image 2)", "referencias", C(GI, 104, 107, "Image 1: base scene")),
        R("Linter: T2 se mapea a caso 1 (génesis)", "gate aurora", C(PL, 193, 193, '"T2": "1"')),
    ],
    "T3_1_persona": [
        R("Un solo trabajo por generación", "estructura", C(SW, 116, 116, "Un solo trabajo por generación.")),
        R("Posición siempre por ancla legible de la propia imagen; prohibido 'left half', 'centre'", "composición", C(SW, 118, 119, "Prohibido \"left half\", \"centre\", \"just left of X\".")),
        R("Stills en instante congelado ('frozen mid-stride'); nada de movimiento en imagen fija", "action", C(SW, 129, 129, "Stills en instante congelado (\"frozen mid-stride\")")),
        R("Mundos por dos pasos: placa vacía primero; insert con 'use only the person from image N, ignore its setting'", "referencias", C(SW, 127, 128, "\"use only the person from image N, ignore its setting\"")),
        R("Los cuerpos nunca tapan logo ni lettering en frames congelados", "composición", C(SW, 133, 133, "cuerpos nunca tapan logo ni lettering en frames congelados")),
        R("Usar la cara de la referencia y mantener rasgos exactos", "subject", C(GR, 108, 108, "Use this person's face. Keep features exactly the same.")),
        R("Anatomía solo en decisión: nombrar el verbo de la mano", "action", C(FA, 168, 168, "Anatomía solo en decisión: nombrar el verbo de la mano"), origen=INF),
        R("Linter: T3 se mapea a caso 2 (ancla con refs)", "gate aurora", C(PL, 194, 194, '"T3": "2"')),
    ],
    "T4_2_personas_contacto": [
        R("Con dos personajes: un sujeto por generación o técnica de colocación probada", "estructura", C(SW, 116, 117, "Con dos personajes: un sujeto por generación, o técnica")),
        R("Contacto entre personas: 'a natural high five'; la anatomía la fija el keyframe aprobado, nunca la asignación de manos por texto", "action", C(SW, 130, 131, 'Contactos entre personas: "a natural high five"')),
        R("Solo un ejemplar de cada personaje por imagen", "subject", C(CH, 38, 38, "Rule: Only one of each character per image.")),
        R("Forzar diferenciación: ropa, peinado y rasgos distintos", "subject", C(FX, 134, 134, "Clothing colors, hairstyles, and facial features must all be distinct.")),
        R("Producción en pasos: placa → inserto A → inserto B", "orden de producción", C(FA, 172, 172, "Producción en pasos: placa del café → inserto A → inserto B"), origen=INF),
        R("Contacto en el pico: T4, manos nombradas, blur parcial solo en la extremidad", "action", C(FA, 196, 196, "High five o choque en el pico: T4, manos nombradas, blur parcial solo en la extremidad"), origen=INF),
        R("Linter: T4 se mapea a caso 2", "gate aurora", C(PL, 194, 194, '"T4": "2"')),
    ],
    "T5_edicion": [
        R("GPT Image 2: lógica de dos columnas Change / Preserve / Constraints", "estructura", C(GI, 81, 83, "Constraints: no extra objects, no redesign, no drift")),
        R("Preserve-list obligatoria en gpt-image-2", "preserve", C(IS, 100, 100, "mandatory for gpt-image-2, recommended for nano-banana")),
        R("Un edit por iteración", "change", C(GI, 87, 87, "Один edit за итерацию.")),
        R("Repetir la preserve list en cada iteración", "preserve", C(GI, 88, 88, "Preserve list повторять каждую итерацию.")),
        R("Surgical edits: enumerar qué NO tocar", "constraints", C(GI, 89, 89, "явно перечисли что НЕ трогать")),
        R("Nano Banana: conversacional, sin máscaras, 'Keep X same, change Y'", "estructura", C(ED, 5, 5, "«Keep X same, change Y»")),
        R("NB: hasta 3 ediciones sucesivas se apilan sin perder el original", "iteración", C(NB, 102, 102, "до 3 последовательных правок стэкаются без потери исходника")),
        R("SW30: E(change, preserve, [constraints]) para edición", "estructura", C(SW, 43, 43, "E(change, preserve, [constraints]) para edición")),
        R("El editor no tiene memoria: solo verbos operativos, cero narrativa", "change", C(SW, 120, 121, "solo verbos operativos (Move/Replace/Add/Remove/Swap)")),
        R("Swap de identidad = última operación, sola", "change", C(SW, 125, 126, "Swap de identidad = última operación, sola")),
        R("Edit, don't re-roll: ≥80% correcto → cambio puntual (hasta 3 apiladas)", "iteración", C(SW, 135, 136, "Edit, don't re-roll")),
        R("GPT Image 2 tiene la mejor preservación de identidad en edición", "modelo", C(MD, 14, 14, "в editing у него лучшая identity-preservation")),
        R("Linter: T5 se mapea a caso 2", "gate aurora", C(PL, 194, 194, '"T5": "2"')),
    ],
    "PROD": [
        R("Un producto con logo o etiqueta real no nace de texto: es flujo con referencia", "referencias", C(DE, 23, 23, "Un producto con logo o etiqueta real no nace de texto: es flujo con referencia.")),
        R("Producto como referencia: colocar en nuevo contexto y casar luz y perspectiva", "subject / referencias", C(GR, 115, 116, "Place this product in [NEW CONTEXT].")),
        R("Mockup: preservar legibilidad de etiqueta y geometría exactas", "important_details", C(GI, 142, 142, "preserve label legibility exactly, preserve geometry")),
        R("Logos solo heredados de asset aprobado o descripción canónica del brand-lock", "constraints", C(SW, 132, 132, "Logos solo heredados de asset aprobado o descripción canónica del brand-lock")),
        R("El producto debe seguir reconocible e inalterado", "constraints", C(ECO, 18, 18, "product must remain recognizable and unaltered")),
        R("Series de marca: generar una a la vez", "iteración", C(CH, 53, 53, "Generate one at a time.")),
        R("Máximo cinco elementos distintos por escena (GPT Image, forge)", "composición", C(FGI, 88, 88, "five or fewer distinct elements per scene")),
        R("Etiqueta de producto / UI / texto pequeño → GPT Image 2 quality high", "modelo", C(FA, 248, 248, "Etiqueta de producto, UI, texto pequeño legible"), origen="síntesis de models.md / gpt-image.md en flujo-anclas.html"),
    ],
    "GRAF_texto": [
        R("Todo texto a renderizar va entre comillas; especificar peso y posición", "text", C(GR, 48, 52, "Any text for rendering goes in quotes:")),
        R("GPT: literal entre comillas o ALL CAPS", "text", C(GI, 69, 69, "или ALL CAPS")),
        R("GPT: deletrear palabras complejas y marcas", "text", C(GI, 71, 71, "Сложные слова и бренды: спеллинг по буквам.")),
        R("GPT: guardia 'no extra words, no duplicate text, no watermarks'", "constraints", C(GI, 72, 72, "no extra words, no duplicate text, no watermarks")),
        R("GPT: texto pequeño/denso/multi-font → quality high obligatorio", "parámetro quality", C(GI, 74, 74, "`quality: high` обязательно")),
        R("NB: se pueden nombrar fuentes; multi-idioma en un frame", "text", C(NB, 107, 107, "Font можно называть")),
        R("Text-first hack: generar el texto primero, luego la imagen con ese texto", "flujo", C(TR, 125, 125, "For complex text in images, generate text FIRST, then ask for the image:")),
        R("Estructura de infografía: Create ... / Target Audience / Content / Title / Visual Style / Layout / Format", "estructura", C(TR, 11, 17, "Layout: [LAYOUT TYPE]")),
        R("NB: el texto pequeño se emborrona en 1K → 2K+ o GPT Image 2", "parámetro image_size", C(NB, 136, 136, "Мелкий текст мылится на 1K")),
        R("Forge: la capa de texto nunca entra al prompt de imagen (salvo Ideogram Modo 2 con override)", "text", C(FPA, 60, 60, "Never appears in image prompts")),
        R("Forge GPT: un solo elemento de texto por prompt", "text", C(FGI, 80, 80, "Limit to one text element per prompt for reliability")),
        R("Ideogram Modo 2: The text \"...\" appears {posición}, in {fuente}", "text", C(FID, 27, 27, 'The text "{exact text}" appears {position description}, in {font style description}.')),
        R("Ancla: texto en pantalla es capa separada (text-overlays.json)", "text", C(FA, 104, 104, "Texto en pantalla: capa separada, text-overlays.json."), origen="flujo-anclas.html cita forge Rule 1 y 6"),
    ],
    "MULTI_panel": [
        R("Numerar y describir cada panel explícitamente", "important_details", C(MP, 5, 5, "Core principle: explicitly number and describe every panel.")),
        R("Declarar dimensiones del grid (columnas x filas)", "scene", C(MP, 310, 310, "Always state the grid dimensions")),
        R("Bordes/gaps explícitos: el default varía por modelo", "scene", C(MP, 312, 312, "Default behavior varies by model and is unreliable.")),
        R("Orden de lectura explícito", "important_details", C(MP, 314, 314, '"left-to-right, top-to-bottom"')),
        R("Instrucción explícita 'same person / same character / same product across all panels' + marcadores de identidad", "subject", C(MP, 308, 308, 'Always include an explicit instruction: "same person / same character / same product across all panels."')),
        R("12 paneles: descripciones breves de 3-8 palabras", "important_details", C(MP, 306, 306, "12 panels need brief, visually distinct descriptions (3-8 words each)")),
        R("Captions bajo 5 palabras cada una", "text", C(MP, 299, 299, "keep captions under 5 words each for legibility")),
        R("Omitir números de panel hace que el modelo fusione o salte paneles", "important_details", C(MP, 49, 49, "Omitting panel numbers causes the model to merge or skip panels")),
        R("Texto/etiquetas en paneles → GPT Image 2 quality high; sin texto y composición compleja → NBP", "modelo", C(MP, 317, 318, "No text, complex composition --> Nano Banana Pro")),
        R("Borderless: decir explícitamente 'no white lines, no black borders, no gaps'", "constraints", C(MP, 165, 165, 'explicitly state "no white lines, no black borders, no gaps"')),
        R("Tiras extremas 4:1 solo NB2", "parámetro ratio", C(NB, 41, 43, "1:8, 8:1, 1:4, 4:1 — для баннеров, скроллов, комикс-стрипов.")),
    ],
    "LUGAR_placa": [
        R("Mundos por dos pasos: placa vacía primero", "orden de producción", C(SW, 127, 127, "Mundos por dos pasos: placa vacía primero")),
        R("Image grounding (solo NB2) para lugares reales: exigir exactitud arquitectónica", "subject / scene", C(NB, 33, 34, "Ensure the architectural details, the spire, the surrounding square, and")),
        R("Grounding funciona en edificios, puentes, plazas, especies", "modelo", C(NB, 38, 38, "здания, мосты, площади, виды животных, виды растений, насекомые")),
        R("thinking_level high cuando grounding + razonamiento espacial", "parámetro", C(NB, 58, 58, "Grounding + spatial reasoning одновременно")),
        R("Anclas de época/cultura funcionan mejor en GPT Image 2", "scene", C(GR, 161, 161, "С Nano Banana результат менее предсказуем")),
        R("Entorno verbatim en todos los shots (Lock 2)", "scene", C(FCL, 29, 29, "The environment string is identical in every shot prompt.")),
        R("Environment ref: placa vacía; su texto es series_lock.environment verbatim", "scene", C(FA, 83, 83, "placa de entorno vacía; su texto es"), origen="síntesis en flujo-anclas.html"),
        R("Placa con marcas legibles de posición para insertar personas", "composición", C(FA, 209, 209, "Placa del escenario vacía con marcas legibles de posición"), origen=INF),
    ],
    "ENSAMBLE": [
        R("Grupo ensamble: todos con rostro legible (técnica distinta de la multitud)", "subject", C(DE, 21, 21, "en el ensamble todos")),
        R("Génesis por miembro: rostro T1 y cuerpo T2, canonizados con hash", "orden de producción", C(FA, 208, 208, "Génesis por miembro: rostro T1, después cuerpo T2"), origen=INF),
        R("Inserción secuencial: un miembro por generación sobre la placa", "referencias", C(FA, 210, 210, "keep the world and the people already placed untouched"), origen=INF),
        R("Alternativa en una generación: todos los maestros adjuntos con rol nombrado", "referencias", C(FA, 211, 211, "Image 1 base, Image 2 miembro A, Image 3 miembro B"), origen=INF),
        R("Cada sujeto vinculado individualmente; nunca forma colectiva", "referencias", C(UR, 168, 168, 'Never the collective form "@Images 1 through 4 define four characters respectively"')),
        R("Límites de referencias de personaje: NB2 4, NBP 5", "referencias", C(NB, 65, 65, "Character-consistency рефы | нет | до 4 | до 5")),
        R("GPT Image 2: hasta 16 referencias indexadas con rol", "referencias", C(GI, 102, 104, "не только номером")),
        R("Kling: 3+ personajes sin mezclar rasgos solo si cada uno tiene su elemento", "video", C(KL, 234, 234, "has its own element")),
        R("Diferenciación obligatoria, sin clones", "subject", C(FX, 134, 134, "No identical clones in the background.")),
        R("Hueco: el ensamble no tiene sección propia en ninguna fuente", "cobertura", C(FA, 177, 177, "no tienen sección propia en ninguna fuente")),
    ],
    "MULTITUD": [
        R("Multitud anónima: nadie tiene rostro legible", "subject", C(DE, 21, 21, "En la multitud nadie tiene rostro legible")),
        R("La multitud es entorno: placa con figuras anónimas sin rostros legibles; luego insertar héroes", "orden de producción", C(FA, 173, 173, "se produce como placa con figuras anónimas y sin rostros legibles"), origen=INF),
        R("Máximo 3 héroes con identidad, cada uno con su referencia y rol", "referencias", C(FA, 173, 173, "Máximo 3 héroes con identidad; cada uno con su propia referencia y rol."), origen=INF),
        R("Sin clones idénticos al fondo", "constraints", C(FX, 134, 134, "No identical clones in the background.")),
        R("Público en la periferia: borroso, fragmentado (escala + peligro)", "composición", C(RS, 71, 71, "Marshal / crowd at periphery | blurred, fragmented")),
        R("Prompt sobrecargado: declarar prioridades en vez de añadir descripción", "estructura", C(UR, 176, 176, "declare priorities")),
        R("Hueco: el tipo F no tiene sección propia en ninguna fuente", "cobertura", C(FA, 177, 177, "no tienen sección propia en ninguna fuente")),
    ],
}

# =====================================================================
# POR ACCIÓN VIDEO
# =====================================================================
por_accion_video = {
    "A_pose": [
        R("Cámara estática: 'locked static frame' o 'camera fixed, no movement'", "camera", C(KL, 265, 265, 'Say "locked static frame" or "camera fixed, no movement."')),
        R("Seedance 1.x/2.0: --camerafixed true", "parámetro", C(SD, 242, 242, "Static (via `--camerafixed true`). Locked frame.")),
        R("Forge: 'Static camera, locked off.'", "camera", C(FKL, 45, 45, '"Static camera, locked off."')),
        R("Una transición emocional: 2-4 cues observables", "action", C(UR, 77, 77, "2-4 observable cues")),
        R("Imagen final nombrada", "final", C(UR, 146, 146, "Every clip needs a clear final frame.")),
        R("Tres detalles por shot: presión ambiental, micro-acción física, ancla sonora/motivo", "todas", C(UR, 154, 154, "Each shot must carry at least one of each:")),
    ],
    "B_pico": [
        R("Describir la consecuencia de la acción, no solo la acción", "action", C(UR, 126, 126, "describe the consequence of an action, not just the action")),
        R("Narrar consecuencias; cadenas de acción como QA", "action", C(S25, 234, 234, "Narrate consequences, not just actions.")),
        R("Condicionar eventos a disparadores", "timing", C(S25, 236, 236, "Gate events on triggers.")),
        R("Movimiento rápido con morphing: generar en cámara lenta y acelerar en post", "action", C(KL, 309, 309, "Generate the action in slow motion and speed it up in post")),
        R("Pico congelado: blur parcial solo en lo que deforma", "keyframe", C(RS, 143, 143, "Frozen partial blur at the peak")),
        R("Hueco: el tipo B no tiene sección propia en ninguna fuente", "cobertura", C(FA, 177, 177, "no tienen sección propia en ninguna fuente")),
    ],
    "C_movimiento": [
        R("Un movimiento de cámara primario por shot; como mucho un micro-ajuste", "camera", C(UR, 85, 85, "Pick one dominant move (dolly-in, pan, tracking, static).")),
        R("Un movimiento dominante por shot de 5 s", "camera", C(CL, 68, 68, "Pick one dominant move per 5-second shot. Layer one subtle secondary move at most.")),
        R("No describir movimiento más rápido de lo que permite la duración", "action", C(FKL, 82, 82, "Don't describe motion faster than the duration allows.")),
        R("Duración mínima 5 s para escenas con varias acciones o movimientos", "duration", C(SD, 290, 290, "Minimum duration 5s for any scene that has multiple actions or camera moves.")),
        R("Una acción central + un movimiento por ventana (Seedance 2.5)", "timeline", C(S25, 161, 161, "One core action + one camera move per window.")),
        R("Palabras de tempo que Kling obedece", "camera", C(KL, 136, 136, '"ultra-slow motion" (2-3s feel)')),
        R("Velocidad auténtica, nunca CGI-limpia ni acelerada (race)", "style", C(RS, 28, 28, "Authentic speed, never CGI-clean or sped-up.")),
    ],
    "D_luz_clima": [
        R("Nombrar fuente dominante y dirección y repetirla verbatim en cada clip", "lighting", C(FX, 106, 106, "Name the dominant source and direction and repeat it verbatim in every clip.")),
        R("Bloque 'Lighting constant.'", "lighting", C(FX, 109, 109, "Lighting constant. Cold fridge light as key from frame-right.")),
        R("Veo I2V: describir solo movimiento, cámara, cambio de luz y audio", "lighting", C(VE, 177, 177, "Describe only motion, camera, light change, and audio.")),
        R("No invertir la dirección de luz entre shots consecutivos", "lighting", C(FKL, 75, 75, "Do not flip lighting direction between consecutive shots")),
        R("Paleta con colores concretos; nunca 'cinematic colors'", "style", C(CL, 138, 138, 'Define palette with concrete colors. Never write "cinematic colors."')),
        R("Declarar el régimen físico al inicio", "global", C(S25, 233, 233, "Declare the physics regime up front.")),
        R("El fenómeno es la fuente de luz motivada", "lighting", C(FA, 171, 171, "El fenómeno es la fuente de luz motivada"), origen=INF),
    ],
    "E_interaccion_dialogo": [
        R("Kling P1: identificadores únicos por personaje", "characters", C(KL, 100, 100, "[Character A: Black-suited Agent]")),
        R("Kling P2: anclaje visual antes del diálogo", "shots", C(KL, 104, 104, "Character A pulls a folded note from his pocket and reads aloud")),
        R("Kling P3: tono de voz en la etiqueta", "shots", C(KL, 108, 108, '[Character A, raspy deep voice]: "We\'re out of time."')),
        R("Kling P4: palabras de enlace entre líneas", "shots", C(KL, 113, 113, "Immediately,")),
        R("Veo: comillas dobles + verbo introductor; dos puntos más fiable", "says", C(VE, 55, 63, "Colon after the lead-in verb works too and is often more reliable.")),
        R("Veo: máx 8 s de habla por clip", "says", C(VE, 28, 28, "Dialogue budget. Max 8 seconds of spoken audio per clip.")),
        R("Veo (forge): ~12-18 palabras para un clip de 8 s", "says", C(FVE, 39, 39, "roughly 12–18 words for an 8s clip")),
        R("Seedance 2.5: diálogo en { } con idioma/acento/entrega", "dialogue", C(S25, 91, 91, "Dialogue language + regional variety or accent + delivery style + speaker + {line}")),
        R("Seedance 1.5/2.0: diálogo entre comillas dobles; líneas cortas", "dialogue", C(SD, 273, 274, "Keep lines short.")),
        R("Dos personajes que hablan nunca comparten descripción visual", "characters", C(KL, 305, 305, "Never let two speaking characters share one visual description.")),
    ],
    "F_multitud": [
        R("Vincular cada sujeto a su referencia y forzar diferenciación", "references", C(FX, 131, 134, "No identical clones in the background.")),
        R("Seedance 2.5: sujetos en refs de video/audio 1-5 estable, 6-10 inestable", "references", C(S25, 136, 136, "Subjects in a reference video/audio | 1-5 | 6-10")),
        R("Seedance 2.5: sujetos en imágenes de referencia 1-8 estable", "references", C(S25, 138, 138, "Subjects across reference images | 1-8 | 9-12")),
        R("Kling: 3+ personajes solo con un elemento cada uno", "references", C(KL, 234, 234, "has its own element")),
        R("Declarar prioridades: sujeto central, shots clave, transiciones libres, frame final", "estructura", C(UR, 176, 181, "The mandatory final frame.")),
        R("Hueco: el tipo F no tiene sección propia en ninguna fuente", "cobertura", C(FA, 177, 177, "no tienen sección propia en ninguna fuente")),
    ],
    "i2v_frame_inicial": [
        R("Kling 3.0: prompt corto, centrado en movimiento; describir cómo evoluciona la escena desde la imagen", "prompt", C(KL, 118, 118, "how the scene evolves from the image")),
        R("Kling: 20-40 palabras; no re-describir estáticos", "longitud", C(KL, 249, 249, "Keep the prompt short (20-40 words).")),
        R("Veo 3.1: no re-describir estáticos; 'maintain the subject from the first frame'", "prompt", C(VE, 176, 178, "maintain the subject from the first frame")),
        R("Seedance: NO describir lo ya visible; solo movimiento y cámara", "prompt", C(SD, 258, 258, "DO NOT describe elements already visible in the image.")),
        R("Keyframe de inicio en imagen a video: no re-describir (decisión 3)", "identity block", C(DE, 10, 10, "Keyframe de inicio o fin en imagen a video: no re-describir.")),
        R("Handoff = motion brief, no re-narración", "prompt", C(NB, 130, 130, "Хэндофф в видеомодель — motion brief, не пересказ.")),
        R("Motion brief: el anchor ya fija la escena (Etapa 6)", "prompt", C(APD, 99, 99, "motion brief (no re-describir la escena que el anchor ya fija)")),
        R("Forge Kling: start_image fija el frame de apertura", "parámetro", C(FKL, 24, 24, "to lock the opening frame")),
        R("Aurora casos I2V 3a/3b/3c: linter obligatorio", "gate", C(AU, 17, 17, "Casos 3a/3b/3c (I2V con FF/LF refs)")),
        R("Linter: con rol ff/lf se prohíben descriptores P/O", "gate", C(PL, 33, 34, "descriptores P/O solo aplica con rol ff/lf")),
        R("Paso 7: prompt corto que solo dice cómo evoluciona", "prompt", C(FA, 316, 316, "El ancla aprobada entra al modelo de video con un prompt corto que solo dice cómo evoluciona.")),
        R("Paso 7 Kling: preserve + un movimiento de cámara primero + shots con timecode + audio; 20-40 palabras", "prompt", C(FA, 321, 321, "Un movimiento de cámara primero. Shots con timecodes.")),
        R("Paso 7 Veo: maintain the subject + movimiento, cámara, cambio de luz, audio", "prompt", C(FA, 322, 322, "Maintain the subject from the first frame. Movimiento, cámara, cambio de luz, audio")),
        R("El keyframe es el primer frame bloqueado; un movimiento dominante", "camera", C(AK, 186, 186, "the keyframe is the locked first frame")),
    ],
    "i2v_frame_final": [
        R("Forge Kling: tail_image como objetivo de frame final", "parámetro", C(FKL, 25, 25, "End-frame target for controlled moves")),
        R("SW30 R16: roles start/tail explícitos ('The tail image defines X — inherit exactly')", "prompt", C(SW, 143, 144, 'roles de start/tail ("The tail image defines X — inherit')),
        R("Seedance 2.5: primer y último frame declarados por separado, mismo ratio", "prompt", C(S25, 308, 308, "never jointly. Same aspect ratio required.")),
        R("Seedance 2.5: un último frame con otro ratio se estira", "parámetro", C(S25, 54, 54, "(a mismatched last frame gets stretched)")),
        R("Extensión hacia atrás: el primer frame del source es el estado final explícito", "prompt", C(S25, 275, 275, "first frame as the extension's explicit end state")),
        R("Kling 2.1 Pro: control de frame final", "parámetro", C(KL, 31, 31, "End frame control.")),
        R("LF con el mismo aspect ratio que FF; se declara por separado en Seedance", "parámetro", C(FA, 85, 85, "Mismo aspect ratio que el FF o el modelo lo estira; se declara por separado del FF en Seedance.")),
        R("Linter kling_3.0__3b: sección transition_FF_LF", "gate", C(VY, 636, 636, "transition_FF_LF: [from, into, to, through, evolves, transitions, becomes, settles, ends, arrives, tail image, last frame]")),
    ],
    "multi_shot": [
        R("Kling 3.0: hasta 6 shots por generación", "shots", C(KL, 34, 34, "Multi-shot in one generation (up to 6 shots).")),
        R("Kling 3.0: límites de shot explícitos con timecode; encuadre o ángulo distinto en cada shot", "shots", C(KL, 289, 289, "Make shot boundaries explicit")),
        R("Kling 3.0: duraciones por shot suman ≤15 s", "duration", C(KL, 156, 156, "per-shot durations must sum to ≤ 15s")),
        R("Seedance: marcadores de corte", "shots", C(SD, 174, 179, "Camera cut to. [description]")),
        R("Seedance: tope duro de 5 shots; dimensionar duración al número de shots; anclas compartidas entre vecinos", "shots", C(SD, 196, 196, "Every shot must share an anchor with its neighbors")),
        R("Seedance: bloque anti-mush arriba del todo", "estructura", C(SD, 200, 200, "very top of the prompt")),
        R("Forge Seedance: no más de ~4 cortes", "shots", C(FSD, 75, 75, "Don't write more than ~4 cuts per generation.")),
        R("Seedance 2.5: etapas con un cambio de estado y estado final visible", "timeline", C(S25, 144, 144, "One primary state change per stage, and always state the visible end state")),
        R("Seedance 2.5: ventanas ≥3 s", "timeline", C(S25, 160, 160, "Windows of 3 seconds or more.")),
        R("Veo: JSON para varias escenas en una generación", "estructura", C(VE, 161, 163, "Multiple scenes in one generation.")),
        R("Clips separados: cada prompt repite el bloque de identidad completo", "identity block", C(UR, 102, 102, "repeat the full identity block in every single prompt")),
        R("Formato B: etiquetar Clip 1 / 5 y nota de cómo cortan", "salida", C(FX, 253, 255, "Label them `Clip 1 / 5`")),
        R("No meter una historia de 30 s en un prompt de 5 s", "duration", C(UR, 130, 130, "Do not cram a 30-second story into a 5-second prompt.")),
    ],
}

# =====================================================================
# POR ROL DE REFERENCIA
# =====================================================================
por_rol_referencia = {
    "genesis": [
        R("La génesis fija solo la identidad; lo demás se extiende después con la génesis adjunta", "flujo", C(DE, 20, 20, "La génesis fija solo la parte del sujeto que lleva la identidad")),
        R("Aurora caso 1 = génesis text-to-image (linter recomendado)", "gate", C(AU, 20, 20, "Caso 1 (Génesis text-to-image)")),
        R("Linter: T1/T2/placa → caso 1", "gate", C(PL, 75, 75, "T1/T2/placa → 1")),
        R("Presupuesto aurora caso 1 y 2: 75-130 palabras (original; en el repo solo advierte)", "longitud", C(AU, 110, 110, "75-130 palabras | Max es HARD FAIL")),
        R("Character ref / maestro: front, three-quarter, profile, back para Kling Elements", "ángulos", C(FA, 82, 82, "maestro de identidad. Front, three-quarter, profile, back para Kling Elements"), origen="síntesis de kling.md §7 en flujo-anclas.html"),
    ],
    "personaje": [
        R("Bloque de identidad: forma de cara, color de ojos, tono de piel, pelo, vello facial, ropa exacta, accesorios", "subject", C(UR, 104, 104, "Identity block must include: face shape, eye color, skin tone.")),
        R("Anclar identidad al INICIO de cada prompt; repetir en cada clip", "subject", C(UR, 102, 102, "Anchor identity at the START of every prompt.")),
        R("Seedance: el bloque de identidad completo debe seguir a @img1", "subject", C(SD, 226, 226, "The full identity block must follow the")),
        R("Toda referencia lleva un rol explícito escrito en el prompt y qué ignorar", "references", C(UR, 166, 166, "every asset gets an explicit role written in the prompt")),
        R("Kling 1.x-2.x: 3-4 imágenes frente/perfil/tres cuartos + Bind Elements", "references", C(KL, 207, 215, "Upload 3-4 reference images of the character from different angles.")),
        R("Kling: imágenes fuente 1080p+, luz pareja, sin texto, fondo limpio, centrado", "references", C(KL, 219, 224, "Clean uncluttered background.")),
        R("Kling 3.0 Omni: 3-8 s de video o hasta 4 stills + voice binding; no re-describir la voz", "references", C(KL, 232, 232, "Once bound, the voice belongs to the subject — do not re-describe it in the prompt.")),
        R("Seedance 2.5: Subject Profile para personaje recurrente", "references", C(S25, 121, 122, "[Subject Profile: Conservator]")),
        R("Midjourney: --cref con --cw", "parámetro", C(FCL, 64, 64, "For Midjourney: `--cref {url} --cw 50`")),
        R("Referencia de imagen: el lock más efectivo para consistencia de personaje", "references", C(FCL, 70, 70, "This is the most effective lock for character consistency")),
        R("Linter P3: con rol character, identity block obligatorio (≥3 grupos)", "gate", C(PL, 36, 40, "identity block absent")),
        R("Con referencia de personaje sin start frame: bloque de identidad completo y verbatim", "subject", C(DE, 10, 10, "bloque de identidad completo y verbatim")),
    ],
    "frame_inicial": [
        R("Veo 3.1: la imagen estática es el First Frame", "parámetro", C(VE, 172, 172, "Uses the static image as First Frame.")),
        R("Kling 3.0: la imagen de entrada ancla identidad, layout y texto en imagen", "prompt", C(KL, 118, 118, "The input image serves as the anchor for identity, layout, and on-image text.")),
        R("Forge: start_image (Kling/Veo/Seedance/Hailuo)", "parámetro", C(FVE, 22, 22, "Image-to-video from an accepted still")),
        R("Seedance 2.5: '@Image 1 is the first frame...' declarado por separado", "prompt", C(S25, 308, 308, "declare each anchor separately")),
        R("El aspect ratio del ancla debe ser el destino desde el primer intento", "parámetro", C(NB, 129, 129, "Aspect ratio сразу целевой.")),
        R("Keyframe FF: fija identidad, layout y texto; el prompt describe solo cómo evoluciona", "prompt", C(FA, 84, 84, "Fija identidad, layout y texto en imagen; el prompt de video describe solo cómo evoluciona."), origen="síntesis en flujo-anclas.html"),
        R("Linter rol ff/lf: no describir P/O", "gate", C(PL, 33, 34, "descriptores P/O solo aplica con rol ff/lf")),
    ],
    "frame_final": [
        R("Forge Kling: tail_image", "parámetro", C(FKL, 25, 25, "End-frame target for controlled moves")),
        R("SW30 R16: 'The tail image defines X — inherit exactly'", "prompt", C(SW, 143, 144, 'roles de start/tail ("The tail image defines X — inherit')),
        R("Seedance 2.5: último frame declarado por separado; mismo ratio", "prompt", C(S25, 308, 308, "never jointly. Same aspect ratio required.")),
        R("Keyframe LF: mismo ratio que FF o el modelo lo estira", "parámetro", C(FA, 85, 85, "Mismo aspect ratio que el FF o el modelo lo estira"), origen="síntesis en flujo-anclas.html"),
    ],
    "edicion": [
        R("GPT Image 2: endpoint de edición", "parámetro", C(GI, 78, 78, "openai/gpt-image-2/edit")),
        R("GPT Image 2: Change / Preserve / Constraints; preserve cada iteración", "estructura", C(MD, 53, 53, "повторять preserve каждую итерацию")),
        R("NB: conversacional, sin máscaras", "estructura", C(NB, 88, 88, "Conversational, без масок:")),
        R("Forge NB: Reference: ... Modify the image to ... Preserve ... Change ...", "estructura", C(FNB, 55, 55, "Modify the image to {specific change}.")),
        R("SW30: el editor no tiene memoria; solo verbos operativos", "change", C(SW, 120, 120, "El editor no tiene memoria")),
        R("Seedance 2.5: @Video 1 como único master de edición; alcance y preservación explícitos", "estructura", C(S25, 243, 249, "[Content to Preserve] Keep <everything that must not change> from @Video 1.")),
        R("Seedance 2.5: cuanto más larga la keep-list, menos deriva", "preserve", C(S25, 253, 253, "The longer the keep-list, the less drift.")),
        R("Seedance 2.5: fuente ≤20 s", "parámetro", C(S25, 255, 255, "Editing works best on clips ≤20s")),
    ],
    "estilo": [
        R("Estilo como referencia: 'in this exact visual style. Match colors, textures, mood.'", "estructura", C(GR, 122, 123, "Match colors, textures, mood.")),
        R("NBP: hasta 3 referencias de estilo; NB2 ninguna", "references", C(NB, 66, 66, "Style рефы | нет | нет | до 3")),
        R("GPT Image 2: nombrar propiedades visuales concretas del referente", "important_details", C(GI, 113, 113, "Назови конкретные визуальные свойства референса")),
        R("Midjourney: --sref", "parámetro", C(FMJ, 26, 26, "Style reference")),
        R("Flux: sin style ref; hornear el lenguaje de estilo en el prompt", "prompt", C(FCL, 78, 78, "Flux: not directly supported; bake style language into prompt instead")),
        R("Excluir lo que pueda filtrarse ('Do not use the image background')", "references", C(UR, 166, 166, '"Do not use the image background"')),
        R("Grid de storyboard como referencia: no usar su estilo de línea, textos ni placeholders", "references", C(S25, 306, 306, "Do not use the grid's line-art style, text labels, or placeholder characters.")),
        R("Linter P12: con ref S, el vocabulario de estilo queda prohibido y la sección style se dispensa", "gate", C(PL, 88, 92, "Con S cubierto la sección `style` se dispensa")),
    ],
}

# =====================================================================
# FLUJO ANCLAS (Paso 6 / Paso 7)
# =====================================================================
flujo_anclas = {
    "paso6_orden_bloques_still": [
        {"orden": 1, "bloque": "Encuadre + lente", "cita": C(FA, 264, 264, "Encuadre + lente: el modelo pone más atención al primer 30 a 40% de tokens")},
        {"orden": 2, "bloque": "Sujeto ancla en su umbral", "cita": C(FA, 265, 265, "Sujeto ancla en su umbral")},
        {"orden": 3, "bloque": "Tres cláusulas de profundidad FG/MG/BG", "cita": C(FA, 266, 266, "Tres cláusulas de profundidad con trabajo")},
        {"orden": 4, "bloque": "Cue de movimiento congelado explícita", "cita": C(FA, 267, 267, "Cue de movimiento congelado nombrada explícitamente")},
        {"orden": 5, "bloque": "Luz + paleta", "cita": C(FA, 268, 268, "Luz + paleta: una fuente, dirección, qué superficie rima, colores concretos, bans repetidos")},
        {"orden": 6, "bloque": "Textura", "cita": C(FA, 269, 269, "Textura: grano, halación, un flare, negros aplastados")},
        {"orden": 7, "bloque": "Regla de rostro", "cita": C(FA, 270, 270, "Regla de rostro: sin rostro, o fragmentado, o maestro canonizado adjunto")},
        {"orden": 8, "bloque": "Ratio y nota", "cita": C(FA, 271, 271, "Ratio y nota: sin speed-up, la velocidad construida en el frame")},
    ],
    "paso6_fuente_skill": C(AK, 164, 164, "Lead with framing + lens + light + palette + anchor object"),
    "paso6_bloques_persona_sw30": [
        R("Ensamblar con P o E", "estructura", C(FA, 278, 278, "Ensamblar con P scene, subject, details, mood, usecase, constraints o E change, preserve, constraints")),
        R("Bloques nombrados", "estructura", C(FA, 279, 279, "Bloques nombrados: light_hard, skin_doc, usecase_doc, clean_doc, idlock, contact_*, autocontain_*")),
        R("Herencia mínima", "subject", C(FA, 280, 280, "Herencia mínima: same face and clothes + solo deltas")),
        R("Autocontención de 'same X'", "referencias", C(FA, 281, 281, "exige ambos referentes adjuntos en ese prompt")),
        R("~250 palabras", "longitud", C(FA, 282, 282, "Alrededor de 250 palabras; un slot de 300+ compite consigo mismo")),
        R("Metadatos fuera del cuerpo", "cabecera", C(FA, 283, 283, "Metadatos Model, Quality, Size fuera del cuerpo del prompt")),
    ],
    "paso6_lints": [
        R("gate_image: verbo inicial, lenguaje natural, modelo declarado", "lint", C(FA, 290, 290, "gate_image: empieza con verbo, lenguaje natural, modelo declarado")),
        R("gate_dramaturgy: vocabulario prohibido", "lint", C(FA, 291, 291, "gate_dramaturgy: vocabulario prohibido de video e image")),
        R("aurora caso 1/2: 75-130 palabras, negativo obligatorio (ver conflicto con DECISIONES 2)", "lint", C(FA, 293, 293, "aurora caso 1 génesis o caso 2 ancla con refs: 75 a 130 palabras, negativo obligatorio")),
        R("audit_gi2: 15 columnas", "lint", C(FA, 294, 294, "audit_gi2: 15 columnas incluidos los 5 efectos ópticos y framing positivo")),
    ],
    "paso7_motion_brief": [
        R("Kling 3.0", "motion brief", C(FA, 321, 321, "Preserve identity, wardrobe, sign exactly. Un movimiento de cámara primero. Shots con timecodes. Audio")),
        R("Veo 3.1", "motion brief", C(FA, 322, 322, "Maintain the subject from the first frame. Movimiento, cámara, cambio de luz, audio")),
        R("Seedance 2.5", "motion brief", C(FA, 323, 323, "Etapas consecutivas, un cambio de estado por etapa, estado final visible")),
        R("Todos", "motion brief", C(FA, 324, 324, 'Preserve-cues, roles start/tail, movimiento puro, imagen final nombrada, negativos sin "no X" y ≤8 ítems.')),
    ],
}

# =====================================================================
# CONFLICTOS
# =====================================================================
RES_62 = C(APD, 126, 126, "Todo prompt FINAL se escribe en la sintaxis del modelo destino según el archivo smixs correspondiente.")
RES_64 = C(APD, 132, 132, "El borrador del forge se reescribe a sintaxis smixs; nunca al revés.")
RES_D2 = C(DE, 9, 9, "El conteo de palabras nunca bloquea")
RES_D3 = C(DE, 10, 10, "Resuelve la contradicción entre U7, Seedance §10, forge Rule 3 y Kling §10, Veo §7, Seedance §13, SW30 R5 y R16")
RES_61 = C(APD, 123, 123, "gana siempre")


def K(desc, a, b, res, **kw):
    d = {"descripcion": desc, "lado_a": {"cita": a}, "lado_b": {"cita": b}, "resolucion_documentada": ({"cita": res} if res else None)}
    d.update(kw)
    return d


conflictos = [
    K("Nano Banana: versión de modelo y parámetro de ratio. forge declara Gemini 2.5 Flash Image + aspectRatio; el skill image usa gemini-3.x y image_size (1K/2K/4K).",
      C(FC, 73, 82, "Gemini 2.5 Flash Image"), C(NB, 8, 9, "gemini-3.1-flash-image"), RES_62,
      lado_a_extra=[C(FNB, 30, 30, "`aspectRatio`")], lado_b_extra=[C(NB, 122, 122, "пишется строго с заглавной K")]),
    K("Nano Banana y números de lente: el skill image prohíbe 50mm/f-stops; el adaptador forge y failure-modes los usan como ejemplo y como fix.",
      C(NB, 24, 24, "50mm, 85mm, f/2.8, ISO 400"), C(FNB, 64, 64, "Shot on 50mm prime, f/2.0"), RES_64,
      lado_b_extra=[C(FFM, 16, 16, "Add specific lens and aperture (\"50mm prime, f/2.0\")")]),
    K("Nano Banana y texto: forge prohíbe texto en prompts NB (render mediocre); el skill image lo da como SOTA en 100+ idiomas.",
      C(FNB, 105, 105, "composite separately; text rendering is mediocre"), C(NB, 106, 106, "SOTA по 100+ языкам."), None),
    K("GPT Image: estructura. image/gpt-image.md exige 5 slots con etiquetas; forge usa 3 párrafos sin etiquetas.",
      C(GI, 7, 7, "Пиши лейблами, не сплошным текстом."), C(FGI, 10, 14, "{Paragraph 1: subject, action, spatial composition}"), RES_64),
    K("GPT Image: número de elementos de texto. forge limita a uno por prompt; la plantilla Marketing Creative de image usa titular + subtítulo.",
      C(FGI, 80, 80, "Limit to one text element per prompt for reliability"), C(GI, 164, 165, '"exact subhead" in [font style], [color], [position]'), RES_64),
    K("GPT Image: tamaños por defecto. forge usa 1024x1792 para 9:16 y el parámetro style natural/vivid; el skill image lista 1024×1536 como retrato habitual y no menciona style.",
      C(FGI, 25, 27, "`1024x1792` for 9:16"), C(GI, 60, 60, "Portrait 1024×1536"), RES_62),
    K("GPT Image: obligatoriedad de Constraints. gpt-image.md hace del quinto slot el crítico y el linter lo exige; la firma P() de SW30 lo marca opcional y añade un slot mood.",
      C(GI, 17, 17, "The fifth slot is where most mediocre prompts fail silently."), C(SW, 42, 42, "P(scene, subject, [details], mood,"), None,
      lado_a_extra=[C(VY, 523, 523, 'constraints_slot: ["constraints:"]')]),
    K("Longitud: la plantilla T1 de SW30 pide ~250 palabras; aurora original marca 75-130 como HARD FAIL en casos 1/2 y forge pone techo de 120 en Nano Banana.",
      C(SW, 79, 79, "el prompt completo se mantiene alrededor de 250 palabras"), C(AU, 110, 110, "75-130 palabras | Max es HARD FAIL"),
      C(DE, 9, 9, "Los templates de 250 palabras de SW30 y los prompts de 5 slots de GPT Image pasan"),
      lado_b_extra=[C(FC, 76, 76, '"max_prompt_words": 120')]),
    K("flujo-anclas Paso 6 aplica aurora caso 1/2 con 75-130 palabras y negativo obligatorio; la decisión 2 y la política del linter del repo lo vuelven advertencia y negativo opcional en NB/GPT.",
      C(FA, 293, 293, "75 a 130 palabras, negativo obligatorio"), C(VY, 397, 397, "nano-banana: optional"), RES_D2,
      lado_b_extra=[C(DE, 24, 24, "un límite de longitud es dirección, no bloqueo")]),
    K("Identity block en imagen a video: U7 y flujo-anclas Paso 7 lo repiten en cada clip aunque haya imagen; Kling §10, Veo §7 y Seedance §13 prohíben re-describir lo estático.",
      C(FA, 324, 324, "El identity block se repite en cada clip aunque haya imagen"), C(KL, 249, 249, "Do not re-describe static elements the model already sees."), RES_D3,
      lado_a_extra=[C(UR, 102, 102, "repeat the full identity block in every single prompt")], lado_b_extra=[C(VE, 176, 176, "Do not re-describe static elements."), C(SD, 258, 258, "DO NOT describe elements already visible in the image.")]),
    K("Herencia mínima (SW30 R5) frente a bloque de identidad completo tras @img1 (Seedance §10).",
      C(SW, 123, 124, "Cero re-descripción de lo que"), C(SD, 226, 226, "The full identity block must follow the"), RES_D3),
    K("Negativos 'no X': SW30 R16 y flujo-anclas prohíben 'no X' en clips; Seedance 2.5 usa bans directos 'no X' como parte oficial del prompt (y GPT Image los usa en Constraints).",
      C(SW, 143, 144, "negativos sin \"no X\", ≤8 ítems"), C(S25, 191, 191, "No exaggerated crying, no fast cuts, no large body movements"), None,
      lado_b_extra=[C(SD, 254, 254, "Direct bans are reliable"), C(GI, 14, 14, "(no watermarks, preserve face, no extra text)")],
      nota="el linter del repo solo advierte 'no X' para la familia kling (prompt_linter.py 758-763); no es una resolución declarada"),
    K("Seedance 2.0: máximo de cortes por generación. seedance.md fija tope duro de 5; forge dice ~4.",
      C(SD, 196, 196, "Hard cap: 5 shots per generation"), C(FSD, 75, 75, "Don't write more than ~4 cuts per generation."), RES_62,
      lado_b_extra=[C(FC, 148, 148, "Up to ~4 cuts per generation.")]),
    K("Seedance 2.0: negativos. seedance.md: soporte limitado y frágil; _capabilities.json: sin soporte.",
      C(SD, 250, 250, "Seedance 2.0 adds limited negative prompt support but it's fragile and often ignored."), C(FC, 145, 145, '"supports_negative_prompt": false'), RES_62),
    K("Seedance 2.0: repetición del ancla de identidad. forge: una vez para toda la secuencia; seedance.md: en cada frontera de shot.",
      C(FSD, 76, 76, "Restate it once for the whole sequence, verbatim."), C(SD, 286, 286, "Repeat the full identity block at each shot boundary inside the prompt."), RES_64),
    K("Kling 3.0: duración. kling.md hasta 15 s (suma por shot ≤15 s); forge solo 5 s o 10 s.",
      C(KL, 156, 156, "per-shot durations must sum to ≤ 15s"), C(FKL, 21, 21, "5s and 10s are the supported lengths"), RES_62),
    K("Kling 3.0: longitud. kling.md ~30-60 palabras por shot con hasta 6 shots; forge 80-150 y techo 150 en _capabilities.json.",
      C(KL, 182, 182, "Plan ~30-60 words per shot."), C(FC, 108, 108, '"max_prompt_words": 150'), RES_D2),
    K("Kling: posición de la cámara. forge exige la cámara primero; kling.md ordena Scene → Characters → Action → Camera → Audio y U2 pide sujeto y acción primero.",
      C(FKL, 15, 15, "Camera motion goes **first**."), C(KL, 58, 58, "Scene → Characters → Action → Camera → Audio"), RES_64,
      lado_b_extra=[C(UR, 68, 68, "Lead with subject and action.")]),
    K("Kling: movimientos compuestos. kling.md acepta 'pan right while tilting up'; forge dice que los compuestos se rompen.",
      C(KL, 134, 134, 'Composites work: "pan right while tilting up".'), C(FKL, 81, 81, "Pick one; compound moves break."), RES_64),
    K("Veo: orden. veo.md pone sujeto/acción primero ('Lead with subject and camera'); forge pone la cámara primero.",
      C(VE, 32, 35, "[Subject / Action]"), C(FVE, 12, 12, "{Camera motion sentence, leading.}"), RES_64,
      lado_a_extra=[C(VE, 211, 211, "Lead the prompt with camera.")]),
    K("Veo: longitud. veo.md 50-200 palabras; forge 80-150 y techo 150.",
      C(VE, 44, 44, "Sweet spot. 50-200 words."), C(FC, 124, 124, '"max_prompt_words": 150'), RES_D2),
    K("Veo: negativos. fixes-and-skeletons los da por soportados en el cuerpo y fiables; _capabilities.json declara que no hay soporte y el linter advierte ante un bloque 'Negative:'.",
      C(FX, 214, 214, "Where negatives are supported (Kling field, Veo body text, Seedance 2.0 fragile)."), C(FC, 129, 129, '"supports_negative_prompt": false'), None,
      lado_b_extra=[C(PL, 764, 764, 'if neg_policy == "optional" and pinfo["family"] in ("nano-banana", "gpt-image", "veo", "flux"):')]),
    K("Nano Banana: límites de referencias. models.md, golden-rules y characters.md dicen NBP/NB hasta 14; la tabla de nano-banana.md da NBP 6 objetos + 5 personaje + 3 estilo (14 solo en Lite).",
      C(MD, 20, 20, "Nano Banana Pro** (до 14)"), C(NB, 64, 64, "High-fidelity объекты | до 14 | до 10 | до 6"), None,
      lado_a_extra=[C(GR, 93, 93, "NB до 14"), C(CH, 3, 3, "Up to 14 reference images (6 high-fidelity).")]),
    K("Meta-instrucción de consistencia: multi-panel exige escribir 'same person...'; consistency-locks dice que los generadores no leen meta-instrucciones.",
      C(MP, 308, 308, 'Always include an explicit instruction: "same person / same character / same product across all panels."'),
      C(FCL, 115, 115, "Adding \"consistent character\" or \"same person\" to the prompt"), RES_64),
    K("'slow motion': aurora original lo banea siempre en MAIN; kling.md lo recomienda contra el morphing y reconoce 'ultra-slow motion' como tempo.",
      C(AU, 67, 67, "Cross-platform: `slow motion`"), C(KL, 309, 309, "Generate the action in slow motion and speed it up in post"),
      C(PL, 65, 70, '"slow motion" deja de ser BANNED global')),
    K("'cinematic': las plantillas de Nano Banana/golden-rules y el patrón de Midjourney lo usan; el director y el linter lo prohíben.",
      C(NB, 33, 33, "Generate a cinematic, golden-hour photograph of [SPECIFIC REAL PLACE]."), C(VY, 323, 323, "- cinematic"), RES_61,
      lado_a_extra=[C(GR, 28, 28, "A cinematic wide shot of a futuristic sports car"), C(FMJ, 61, 61, "cinematic photography")]),
    K("Lenguaje de posición: SW30 R2 prohíbe 'left half' / 'centre' y exige anclas legibles; golden-rules y forge usan tercios y porcentajes.",
      C(SW, 118, 119, "Prohibido \"left half\", \"centre\", \"just left of X\"."), C(GR, 37, 37, '"right third, bleeding off edge"'), None,
      lado_b_extra=[C(FGI, 44, 44, "positioned in the left third of the frame"), C(FFM, 87, 87, "subject at left 30% of frame")]),
    K("Película Kodak Portra: SW30 T1 la prohíbe en rostros; forge failure-modes la propone como fix del look AI.",
      C(SW, 73, 73, "Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO en rostros"), C(FFM, 17, 17, "Kodak Portra 400 film stock"), None),
    K("Luz del maestro de identidad: SW30 T1 exige luz dura rasante; kling.md pide luz pareja sin sombras duras en imágenes fuente de personaje (flujo-anclas recoge ambas).",
      C(SW, 71, 71, "luz dura sin relleno, rasante: los poros proyectan sombra"), C(KL, 220, 220, "Even lighting. Avoid hard shadows. The AI can mistake them for permanent facial features."), None,
      lado_b_extra=[C(FA, 168, 168, "Para maestros: luz pareja, fondo limpio, sin sombras duras")], lado_a_extra=[C(FA, 128, 128, "Rostros documentales: luz dura rasante.")]),
    K("Orden de bloques del still: animatic-keyframes y flujo-anclas Paso 6 abren con encuadre + lente; nano-banana.md abre con Subject + Action y prohíbe números de lente.",
      C(AK, 164, 164, "Lead with framing + lens + light + palette + anchor object"), C(NB, 14, 14, "Subject + Action + Location/context + Composition + Style"), RES_62,
      lado_a_extra=[C(FA, 264, 264, "Encuadre + lente")]),
    K("Referencia de personaje en Ideogram: _capabilities.json dice que no; consistency-locks y el adaptador seedream citan omni-reference de Ideogram para personaje.",
      C(FC, 47, 47, '"supports_character_ref": false'), C(FCL, 66, 66, "For Ideogram: `omni-reference` parameter with the image."),
      C(FC, 2, 2, "This file is the single source of truth for 'what each generator can do'"),
      lado_b_extra=[C(FSR, 71, 71, "Ideogram omni-reference")]),
    K("Capa de texto: forge prohíbe texto en prompts de imagen (salvo Ideogram Modo 2); el skill image enruta pósters con EXACT TEXT a GPT Image 2.",
      C(FPA, 60, 60, "Never appears in image prompts"), C(MD, 16, 16, "Брендовая полиграфия / постеры с EXACT TEXT"), None),
    K("Caso del linter para T2: prompt_linter.py mapea T2 (cuerpo con referencia) a caso 1 génesis; aurora SKILL.md define el caso 2 como ancla con refs.",
      C(PL, 193, 193, '"T2": "1"'), C(AU, 21, 21, "Caso 2 (Ancla con refs parciales)"), None),
    K("Parámetros de salida dentro del prompt: el esqueleto de 11 bloques de Seedance lleva cola CLI; en 2.5 no van en el prompt.",
      C(SD, 147, 149, "[11] Output specs."), C(S25, 52, 52, "they do not belong in the prompt"), C(SD, 56, 56, "Not 2.5 syntax.")),
    K("Keywords de sports broadcast (60fps, broadcast realism) exigidos por aurora frente a stills congelados (SW30 R8).",
      C(AU, 69, 69, "`60fps`, `broadcast realism`"), C(SW, 129, 129, "Stills en instante congelado"), C(PL, 71, 71, "--sports-broadcast solo aplica a casos de video")),
]

ESPECIFICAS = {8, 10, 11, 25, 26, 34, 35}
for _i, _c in enumerate(conflictos, 1):
    if _c["resolucion_documentada"]:
        _c["resolucion_documentada"]["tipo"] = "especifica" if _i in ESPECIFICAS else "regla_general"

sin_fuente = [
    "sora: sin archivo de modelo en video/ ni adaptador forge; solo snapshot sora_2__4 del linter (vocabularies.yaml:685) y menciones en descripciones. Faltan formato, parámetros, negativos, longitud, referencias e I2V.",
    "midjourney: sintaxis del negativo (p.ej. --no) no documentada aunque _capabilities.json declara supports_negative_prompt true.",
    "ideogram: sintaxis del campo negativo no documentada aunque se declara soportado.",
    "seedream: sintaxis del campo negativo no documentada aunque se declara soportado.",
    "veo-3.1: frame final (last frame / tail image) no documentado; solo First Frame.",
    "veo-3.1: número máximo de reference ingredients no documentado (flujo-anclas.html:214 'Veo ingredients sin límite documentado').",
    "seedance-2.5: presupuesto de palabras sin cifra (vocabularies.yaml:452).",
    "nano-banana-2 / nano-banana-pro: nombre del parámetro de aspect ratio en la API gemini-3.x no aparece en el skill image (solo image_size y 'Format:' dentro del texto); el aspectRatio documentado es de gemini-2.5 (forge).",
    "gpt-image-2: presupuesto de palabras solo en el adaptador forge (declarado para 1.5/2) y en SW30; gpt-image.md no fija cifra.",
    "kling-3: número máximo de Elements por generación no documentado; solo la advertencia de degradación.",
    "kling-2x: parámetros de API (cfg_scale, duration, aspect_ratio) documentados solo para 3.0.",
    "hailuo: límite de referencias y sintaxis de rol no documentados; solo existe el adaptador forge.",
    "flux / midjourney / ideogram / seedream / hailuo: sin archivo smixs; la autoridad es el adaptador forge (ai-production-director §6.2).",
    "Acción B (pico), D (luz/clima), F (multitud) y grupo ensamble: sin sección propia en ninguna fuente (flujo-anclas.html:177); las reglas se derivan.",
    "Modelos mencionados sin archivo: Runway, Luma, Pika (video/SKILL.md), Gemini Omni Flash (nano-banana.md:131), Minimax H3 (seedance-25.md:337).",
]

data = {
    "_meta": {
        "version": "1.0",
        "fecha": "2026-09-28",
        "descripcion": "Matriz de sintaxis de prompts de generación imagen/video extraída solo de las fuentes; cada requisito lleva cita verbatim verificable.",
        "raiz_skills": PKG,
        "raiz_repo": REPO,
        "convencion_archivo": "'skills/...' es relativo a raiz_skills; el resto es relativo a raiz_repo. Líneas 1-based del archivo tal como está guardado.",
        "verificacion": "cita.texto con espacios colapsados es substring de las líneas linea_ini..linea_fin unidas y colapsadas",
        "tipo_resolucion": "especifica = la fuente nombra este caso; regla_general = regla de precedencia general (p.ej. director §6.2/§6.4, DECISIONES 2) que la fuente declara aplicable a todo conflicto de ese tipo",
        "campo_origen": "cuando un ítem lleva 'origen', la fuente es un documento derivado (flujo-anclas.html) y no texto literal de un skill",
    },
    "modelos": modelos,
    "por_caso_imagen": por_caso_imagen,
    "por_accion_video": por_accion_video,
    "por_rol_referencia": por_rol_referencia,
    "flujo_anclas": flujo_anclas,
    "conflictos_de_sintaxis": conflictos,
    "sin_fuente": sin_fuente,
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)
print("written", OUT)
