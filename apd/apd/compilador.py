"""Especificación + decisiones → Prompt AST v2 → texto final determinista.

El texto final NUNCA se escribe libremente: es el render del AST (misma semántica que
prompt_render_v34.py del paquete, que la auditoría ejecuta para comprobarlo). Cada
bloque dice qué slot de plantilla llena, qué campos del brief liga y qué reglas APLICA
satisface. Si se quiere otra redacción, se edita el campo o el bloque y se recompila.

Formatos por modelo (sintaxis de secciones) — fuente citada en cada uno:
  gpt-image-2      5 slots con etiqueta: image/references/gpt-image.md:5-15
  nano-banana-*    prosa natural 1–2 párrafos, orden Subject+Action+Location+Composition+Style,
                   sin números de lente: image/references/nano-banana.md:11-25; orden de bloques
                   flujo-anclas.html Paso 6
  edición (T5)     Change / Preserve / Constraints: gpt-image.md:81-85 · SW30 template T5
  kling            capas Scene → Characters → Action → Camera → Audio con etiquetas, [Character A: …]:
                   video/references/kling.md:55-72; I2V 'Preserve identity…' kling.md:116-126;
                   negativos en campo aparte sin "no X": kling.md:187-204
  veo              [Subject/Action]+[Environment]+[Camera]+[Lighting]+[Style]+[Audio]: veo.md:30-44;
                   diálogo con comillas y verbo: veo.md:49-66
"""

from __future__ import annotations

import copy
import importlib.util
import json
import re
import sys

from . import fuentes as F
from . import spec as S

VERSION_COMPILADOR = "apd-compilador-1.2"

FORMATOS = {
    "gpt-image-2": {
        "tipo": "labels", "fuente": "image/references/gpt-image.md:5-15 (5 slots)",
        "secciones": [
            {"id": "lead", "etiqueta": None, "campos": ["verbo_inicial"], "destinos": ["estructura"],
             "literal": "Create a {tipo_pieza}.",
             "literal_fuente": "image/references/golden-rules.md R1 'Start with a Verb' (gate_image R1) — primera línea antes de los 5 slots: "
                               "composición de la app que satisface R1 y los 5 slots de gpt-image.md a la vez"},
            {"id": "scene", "etiqueta": "Scene:", "campos": ["fondo", "luz_escena"], "destinos": ["fondo"]},
            {"id": "subject", "etiqueta": "Subject:", "campos": ["referencias_linea", "identidad_linea", "identidad", "contexto", "personalidad", "encuadre_linea", "encuadre_sin_mirada"],
             "destinos": ["identidad", "encuadre"]},
            {"id": "details", "etiqueta": "Important Details:",
             "campos": ["rasgos", "camara", "foco", "luz", "textura", "color"],
             "destinos": ["camara", "luz", "textura", "color", "identidad"]},
            {"id": "usecase", "etiqueta": "Use Case:", "campos": ["uso"], "destinos": ["estructura"],
             "literal_final": "Looks like a real photo.",
             "literal_final_fuente": "image/references/gpt-image.md:128-133 plantilla 'Photoreal Editorial': 'Use Case: editorial photograph, looks like a real photo'",
             "literal_si": "fotorreal"},
            {"id": "constraints", "etiqueta": "Constraints:", "campos": ["restricciones"], "destinos": ["restricciones", "vocabulario"]},
        ],
    },
    "nano-banana": {
        "tipo": "prosa", "fuente": "image/references/nano-banana.md:11-25 · flujo-anclas.html Paso 6 'Orden de bloques'",
        "secciones": [
            {"id": "lead", "etiqueta": None, "campos": [], "destinos": ["estructura"],
             "literal": "Create a {tipo_pieza}.",
             "literal_fuente": "image/references/golden-rules.md R1 'Start with a Verb'"},
            {"id": "encuadre", "etiqueta": None, "campos": ["encuadre_linea", "encuadre_sin_mirada", "camara"], "destinos": ["encuadre", "camara"]},
            {"id": "sujeto", "etiqueta": None, "campos": ["referencias_linea", "identidad_linea", "identidad", "contexto", "personalidad", "rasgos"], "destinos": ["identidad", "referencias"]},
            {"id": "escena", "etiqueta": None, "campos": ["fondo"], "destinos": ["fondo"]},
            {"id": "luz", "etiqueta": None, "campos": ["luz", "color"], "destinos": ["luz", "color"]},
            {"id": "textura", "etiqueta": None, "campos": ["textura", "foco"], "destinos": ["textura", "camara"]},
            {"id": "uso", "etiqueta": None, "campos": ["uso"], "destinos": ["estructura"]},
            {"id": "restricciones", "etiqueta": None, "campos": ["restricciones"], "destinos": ["restricciones", "vocabulario"]},
        ],
    },
    "edicion": {
        "tipo": "labels", "fuente": "image/references/gpt-image.md:81-85 · SW30 template T5 (Change/Preserve/Constraints)",
        "secciones": [
            {"id": "lead", "etiqueta": None, "campos": ["edicion_linea"], "destinos": ["estructura", "referencias"]},
            {"id": "change", "etiqueta": "Change:", "campos": ["cambio"], "destinos": ["estructura", "identidad"]},
            {"id": "preserve", "etiqueta": "Preserve:", "campos": ["preservar"], "destinos": ["identidad", "referencias"]},
            {"id": "constraints", "etiqueta": "Constraints:", "campos": ["restricciones"], "destinos": ["restricciones"]},
        ],
    },
    "kling": {
        "tipo": "labels", "fuente": "video/references/kling.md:55-72 (Scene → Characters → Action → Camera → Audio)",
        "secciones": [
            {"id": "preserve", "etiqueta": None, "campos": ["preservar"], "destinos": ["referencias", "identidad"], "solo_si": "i2v"},
            {"id": "characters", "etiqueta": None, "campos": ["personajes"], "destinos": ["identidad"]},
            {"id": "scene", "etiqueta": "Scene.", "campos": ["fondo"], "destinos": ["fondo"], "omitir_si": "i2v"},
            {"id": "action", "etiqueta": "Action.", "campos": ["accion_video"], "destinos": ["movimiento"]},
            {"id": "camera", "etiqueta": "Camera.", "campos": ["movimiento", "angulo_video", "camara"], "destinos": ["camara", "movimiento"]},
            {"id": "lighting", "etiqueta": "Lighting.", "campos": ["luz"], "destinos": ["luz"]},
            {"id": "audio", "etiqueta": "Audio.", "campos": ["audio"], "destinos": ["audio"]},
            {"id": "negative", "etiqueta": "Negative field.", "campos": ["negativos"], "destinos": ["restricciones"]},
        ],
        "negativos_aparte": True,
    },
    "veo": {
        "tipo": "prosa", "fuente": "video/references/veo.md:30-44 (orden Subject/Action → Environment → Camera → Lighting → Style → Audio)",
        "secciones": [
            {"id": "sujeto", "etiqueta": None, "campos": ["personajes", "accion_video"], "destinos": ["identidad", "movimiento"]},
            {"id": "entorno", "etiqueta": None, "campos": ["fondo"], "destinos": ["fondo"]},
            {"id": "camara", "etiqueta": None, "campos": ["movimiento", "angulo_video", "camara"], "destinos": ["camara", "movimiento"]},
            {"id": "luz", "etiqueta": None, "campos": ["luz", "color"], "destinos": ["luz", "color"]},
            {"id": "audio", "etiqueta": None, "campos": ["audio"], "destinos": ["audio"]},
            {"id": "restricciones", "etiqueta": None, "campos": ["restricciones"], "destinos": ["restricciones"]},
        ],
    },
}
FORMATOS["seedance"] = copy.deepcopy(FORMATOS["veo"])
FORMATOS["seedance"]["fuente"] = "video/references/seedance.md · seedance-25.md (roles @Image por separado) — orden de veo.md usado como aproximación: NUEVA"

# Plantillas de frase para cada campo lógico (texto de enlace de la app, no de reglas).
FRASES = {
    "fondo": "{fondo}.",
    "luz_escena": "",
    "identidad_linea": "{sujeto}.",
    "contexto": "One of the {contexto}.",
    "personalidad": "Expression and posture: {personalidad}.",
    "encuadre_linea": "{encuadre}, {angulo} camera, looking {mirada}.",
    "encuadre_sin_mirada": "{encuadre}, {angulo} camera.",
    "rasgos": "Distinct features: {rasgos}.",
    "identidad": "Character lock: {identidad}.",
    "camara": "{camara}.",
    "foco": "{foco}.",
    "luz": "{luz}.",
    "textura": "{textura}.",
    "color": "{color}.",
    "uso": "{uso}.",
    "restricciones": "{restricciones}.",
    "cambio": "{cambio}",
    "preservar": "{preservar}",
    "personajes": "{personajes}",
    "accion_video": "{accion_video}",
    "movimiento": "{movimiento}.",
    "angulo_video": "Camera angle: {angulo}.",
    "referencias_linea": "{referencias_linea}",
    "edicion_linea": "{edicion_linea}",
    "negativos": "{negativos}",
    "audio": "{audio}",
}

DESTINOS_PARAMETROS = {"parametros", "referencias", "proceso", "longitud", "vocabulario"}


def es_fotorreal(spec: dict) -> bool:
    return (spec["comunes"]["tratamiento"]["valor"] or "") not in ("animacion",)


def tipo_pieza(spec: dict, ent: dict) -> str:
    c = spec["comunes"]
    casos = ent["casos"]
    if "T1" in casos:
        # el encuadre, si el brief lo fija, va una sola vez en Subject (screenwriter/SKILL.md:253 'Lean prose')
        base = "portrait photograph" if (c.get("encuadre") or {}).get("valor") else "head-and-shoulders portrait photograph"
        if "casting" in (c["objetivo"]["valor"] or "").lower():
            base = base.replace("portrait", "casting portrait")
        return base
    if "T2" in casos:
        return "full-body portrait photograph"
    if (c.get("d1") or {}).get("valor") == "keyframe_ff" or (c.get("tarjeta_d1") or {}).get("valor") == "keyframe_ff":
        return "keyframe photograph (first frame of a video clip)"
    if "PROD" in casos:
        return "product photograph"
    return "photograph"


def formato_de(modelo: str, casos: list[str]) -> str:
    if casos and casos[0] == "T5":
        return "edicion"
    if modelo.startswith("nano-banana"):
        return "nano-banana"
    return modelo if modelo in FORMATOS else "gpt-image-2"


def _v34(nombre: str):
    p = F.extraer_paquete() / "repo" / ".claude" / "hooks" / f"{nombre}.py"
    sys.path.insert(0, str(p.parent))
    spec = importlib.util.spec_from_file_location(f"apd_{nombre}", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def hechos_entrega(spec: dict, ent: dict) -> tuple[dict, dict]:
    """Hechos planos para el brief congelado de ESTA entrega + estados (formato v3.4)."""
    c = spec["comunes"]
    e = ent["campos"]

    def v(k):
        f = e.get(k) or c.get(k)
        return f if f else None

    def val(k):
        f = v(k)
        if not f or f["estado"] != "LOCKED":
            return None
        x = f["valor"]
        if isinstance(x, list):
            x = ", ".join(str(i) for i in x if not isinstance(i, dict))
        return x

    sexo, edad, origen = val("sexo"), val("edad"), val("origen")
    partes = []
    if sexo:
        partes.append(f"a {sexo}")
    if edad:
        partes.append(f"{edad} years old")
    if origen:
        partes.append(str(origen))
    sujeto = ", ".join(partes) if partes else val("sujeto")
    if sujeto:
        sujeto = sujeto[0].upper() + sujeto[1:]
    rest = val("restricciones")
    medio = (c.get("medio") or {}).get("valor")
    refs = [r for r in ((c.get("referencias") or {}).get("valor") or []) if isinstance(r, dict)]
    rol_txt = {"personaje": "is the approved character reference — same face and clothes; apply only the changes below",
               "estilo": "is a style reference — apply only its palette and light, not its content",
               "frame_inicial": "is the start frame", "frame_final": "is the end frame",
               "edicion": "is the image to edit"}
    ref_linea = " ".join(f"Image {i + 1} ({r.get('nombre')}) {rol_txt.get(r.get('rol'), 'is a reference')}." for i, r in enumerate(refs)
                         if r.get("rol") in ("personaje", "estilo")) or None
    hechos = {
        # T1 (maestro de rostro): el contexto del casting no se ve en el cuadro y puede meter un instrumento; va en notas
        # (screenwriter/SKILL.md:253 'Lean prose', señalado por la revisión semántica independiente, ronda 2)
        "fondo": val("fondo"), "sujeto": sujeto, "contexto": None if "T1" in ent["casos"] else val("contexto"),
        "personalidad": val("personalidad"),
        "encuadre": val("encuadre"), "angulo": val("angulo"),
        "mirada": val("mirada") or ("straight into the lens" if medio == "imagen" and val("encuadre") and "T1" in ent["casos"] else None),
        "rasgos": val("rasgos"), "identidad": val("identidad"), "camara": val("camara"), "foco": val("foco"), "luz": val("luz"),
        "textura": val("textura"), "color": val("color"), "uso": val("uso"), "restricciones": rest,
        "cambio": val("cambio"), "preservar": val("preservar"), "personajes": val("personajes"),
        "accion_video": val("accion_video"), "movimiento": val("movimiento"), "audio": val("audio"),
        "referencias_linea": ref_linea,
        "negativos": val("negativos"),
        "edicion_linea": (f"Edit Image 1 ({next((r.get('nombre') for r in refs if r.get('rol') == 'edicion'), 'the attached image')}): "
                          "change only what is listed below.") if val("cambio") else None,
        # parámetros: van al brief congelado pero no al texto
        "modelo": val("modelo"), "formato": val("formato"), "calidad": val("calidad"), "duracion": val("duracion"),
    }
    if medio == "video":
        hechos["angulo"] = hechos.get("angulo")
        if not hechos.get("personajes") and val("sujeto"):
            hechos["personajes"] = f"[Character A: {val('sujeto')}]"
        hechos.pop("sujeto", None)
        hechos.pop("encuadre", None) if not val("encuadre") else None
    hechos = {k: x for k, x in hechos.items() if x not in (None, "")}
    for k in ("fondo", "encuadre", "camara", "foco", "luz", "textura", "color", "uso", "restricciones", "movimiento"):
        if isinstance(hechos.get(k), str) and hechos[k][:1].islower():
            hechos[k] = hechos[k][0].upper() + hechos[k][1:]
    no_prompt = {"modelo", "formato", "calidad", "duracion"}
    estados = {k: {"state": "LOCKED", "source_type": "user", "source_id": _origen(spec, ent, k),
                   "prompt_required": k not in no_prompt} for k in hechos}
    if "mirada" in estados and not (e.get("mirada") or c.get("mirada")):
        estados["mirada"]["source_id"] = "app:valor por defecto de la frase de encuadre"
    return hechos, estados


def _origen(spec, ent, k):
    f = ent["campos"].get(k) or spec["comunes"].get(k)
    if k == "sujeto" and not f:
        return "derivado: sexo+edad+origen"
    return f"{(f or {}).get('origen', 'derivado')}"


def congelar(spec: dict, ent: dict, brief_id: str) -> dict:
    bf = _v34("brief_freeze_v34")
    hechos, estados = hechos_entrega(spec, ent)
    h = bf.canon_hash(brief_id, 1, hechos, estados)
    return {"schema_version": "1.1", "brief_id": brief_id, "brief_version": 1, "status": "FROZEN",
            "facts": hechos, "field_states": estados, "brief_hash": h}


def parametros(spec: dict, ent: dict, fmt: str) -> list[dict]:
    c = spec["comunes"]
    mod = c["modelo"]["valor"]
    out = [{"nombre": "model", "valor": mod, "fuente": "spec.modelo"}]
    fr = c["formato"]["valor"] if c["formato"]["estado"] == "LOCKED" else None
    q = c["calidad"]["valor"] if c["calidad"]["estado"] == "LOCKED" else None
    if mod == "gpt-image-2":
        tam = {"2:3": "1024x1536", "3:2": "1536x1024", "1:1": "1024x1024", "16:9": "2560x1440"}.get(fr or "", None)
        out.append({"nombre": "size", "valor": tam or fr, "fuente": "gpt-image.md:52-66 (tamaños; ambos lados múltiplos de 16)"})
        out.append({"nombre": "quality", "valor": q, "fuente": "gpt-image.md:43-49 (high: портреты, identity-sensitive)"})
    elif mod and mod.startswith("nano-banana"):
        out.append({"nombre": "model_id", "valor": {"nano-banana-pro": "gemini-3-pro-image", "nano-banana-2": "gemini-3.1-flash-image"}[mod],
                    "fuente": "image/references/nano-banana.md:5-9"})
        out.append({"nombre": "aspectRatio", "valor": fr, "fuente": "visual-prompt-forge/adapters/_capabilities.json (aspect_param) — ver conflicto CF-SX-NB"})
        out.append({"nombre": "image_size", "valor": q, "fuente": "image/references/nano-banana.md:122 ('1K','2K','4K' con K mayúscula)"})
    elif mod in ("kling", "veo", "seedance", "hailuo"):
        out.append({"nombre": "aspect_ratio", "valor": fr, "fuente": "kling.md:157 · _capabilities.json"})
        out.append({"nombre": "duration", "valor": c.get("duracion", {}).get("valor"), "fuente": "kling.md:156"})
        if mod == "kling":
            out.append({"nombre": "negative_prompt", "valor": (c.get("negativos") or {}).get("valor"), "fuente": "kling.md:187-204"})
    refs = c["referencias"]["valor"] or []
    out.append({"nombre": "references", "valor": [f"Image {i + 1} = {r.get('nombre')} (rol: {r.get('rol')})" for i, r in enumerate(refs)] or "none",
                "fuente": "gpt-image.md:100-107 (índice con rol) · U13"})
    return out


def compilar(spec: dict, ent: dict, dec: dict[str, dict], reg, prompt_id: str, revision: int = 1) -> dict:
    c = spec["comunes"]
    modelo = c["modelo"]["valor"]
    fmt_id = formato_de(modelo, ent["casos"])
    fmt = FORMATOS[fmt_id]
    brief = congelar(spec, ent, prompt_id)
    hechos = brief["facts"]
    i2v = any((r or {}).get("rol") in ("frame_inicial", "frame_final") for r in (c["referencias"]["valor"] or []))
    aplica = {k: v for k, v in dec.items() if v["estado"] == "APLICA"}
    bloques = []
    usados = set()
    for sec in fmt["secciones"]:
        if sec.get("solo_si") == "i2v" and not i2v:
            continue
        if sec.get("omitir_si") == "i2v" and i2v:
            continue
        segs = []
        if sec["etiqueta"]:
            segs.append({"id": "label", "kind": "adapter_text", "text": sec["etiqueta"],
                         "source_rules": [f"SX:{fmt_id}:{sec['id']}"], "fuente": fmt["fuente"]})
        campos = []
        if sec.get("literal"):
            segs.append({"id": "literal", "kind": "adapter_text", "text": sec["literal"].format(tipo_pieza=tipo_pieza(spec, ent)),
                         "source_rules": [f"SX:{fmt_id}:{sec['id']}"], "fuente": sec["literal_fuente"]})
        for campo in sec["campos"]:
            plantilla = FRASES.get(campo, "")
            if not plantilla:
                continue
            ph = re.findall(r"\{(\w+)\}", plantilla)
            if not ph or not all(p in hechos for p in ph):
                continue
            if campo == "encuadre_sin_mirada" and "mirada" in hechos:
                continue
            segs.append({"id": campo, "kind": "brief_template", "template": plantilla,
                         "bindings": {p: p for p in ph}, "source_rules": []})
            usados |= set(ph)
            campos += ph
        if sec.get("literal_final") and (sec.get("literal_si") != "fotorreal" or es_fotorreal(spec)):
            segs.append({"id": "literal_final", "kind": "adapter_text", "text": sec["literal_final"],
                         "source_rules": [f"SX:{fmt_id}:{sec['id']}:final"], "fuente": sec["literal_final_fuente"]})
        if len(segs) == (1 if sec["etiqueta"] else 0):
            continue  # sección sin contenido: no se emite
        satisface = sorted(k for k, v in aplica.items() if set(v.get("destino") or []) & set(sec["destinos"]))
        bloques.append({"id": sec["id"], "slot": sec["etiqueta"] or sec["id"], "segments": segs,
                        "campos": campos, "destinos": sec["destinos"], "satisface": satisface})
    ast = {"schema_version": "2.0", "prompt_id": prompt_id, "prompt_revision": revision, "brief_hash": brief["brief_hash"],
           "model": modelo, "parameters": {p["nombre"]: p["valor"] for p in parametros(spec, ent, fmt_id) if p["nombre"] != "references"},
           "formato": fmt_id, "compilador": VERSION_COMPILADOR,
           "blocks": [{"id": b["id"], "segments": b["segments"]} for b in bloques]}
    texto = render(ast, brief, prosa=fmt["tipo"] == "prosa")
    for b, ab in zip(bloques, ast["blocks"]):
        b["texto"] = render({"blocks": [ab]}, brief).strip()
        b["hash"] = F.sha256_text(b["texto"])[:16]
    # evidencia fuera del cuerpo: parámetros, notas de proceso, lints globales
    fuera = {}
    for k, v in aplica.items():
        d = set(v.get("destino") or [])
        if d & DESTINOS_PARAMETROS:
            fuera[k] = sorted(d & DESTINOS_PARAMETROS)
    notas = notas_entrega(spec, ent, aplica, reg, fmt_id)
    return {"ast": ast, "brief": brief, "texto": texto, "hash": F.sha256_text(texto), "formato": fmt_id,
            "fuente_formato": fmt["fuente"], "bloques": bloques, "parametros": parametros(spec, ent, fmt_id),
            "evidencia_fuera_del_cuerpo": fuera, "notas": notas,
            "campos_no_usados": sorted(k for k, s in brief["field_states"].items() if s["prompt_required"] and k not in usados)}


def render(ast: dict, brief: dict, prosa: bool = False) -> str:
    """Misma semántica que prompt_render_v34.py: bloques unidos por línea en blanco,
    segmentos por espacio. En formato prosa los bloques se unen en un párrafo."""
    r = _v34("prompt_render_v34")
    partes = []
    for block in ast["blocks"]:
        segtexts = []
        for s in block["segments"]:
            if s["kind"] == "brief_template":
                vals = {name: r.fmt(r.getp(brief["facts"], path)) for name, path in s["bindings"].items()}
                segtexts.append(s["template"].format(**vals).strip())
            else:
                segtexts.append(s["text"].strip())
        partes.append(" ".join(t for t in segtexts if t))
    sep = " " if prosa else "\n\n"
    return sep.join(partes) + "\n"


def notas_entrega(spec, ent, aplica, reg, fmt_id) -> dict:
    proceso = sorted(k for k, v in aplica.items() if "proceso" in (v.get("destino") or []))
    c = spec["comunes"]
    riesgos = []
    if "T1" in ent["casos"] and (c.get("contexto") or {}).get("valor"):
        riesgos.append(f"contexto del casting fuera del cuerpo del prompt: {c['contexto']['valor']} (no se ve en un maestro de rostro)")
    if "T1" in ent["casos"]:
        riesgos.append("identidad del rostro: génesis sin referencia; maestro de rostro T1 que se canoniza con hash antes de derivar T2 "
                       "(SW30 R11). El rol en el pipeline va aquí y no en el cuerpo: el generador no lee meta-instrucciones "
                       "(visual-prompt-forge/references/consistency-locks.md:115-116)")
    if c["tratamiento"]["valor"] != "documental":
        riesgos.append("apariencia de render/piel plástica: textura de piel explícita en Important Details")
    return {"micro_gate": {"SKILL": f"formato {fmt_id} — {FORMATOS[fmt_id]['fuente']}",
                           "RIESGOS": "; ".join(riesgos) or "—",
                           "TÉCNICA": "compilación por bloques del AST v2 (v3.4) con brief congelado"},
            "proceso": [{"id": k, "texto": reg.reglas[k]["texto"][:200]} for k in proceso],
            "advertencia": "Las instrucciones del texto no controlan físicamente el generador: lente, ángulo o mirada "
                           "descritos son pedidos, no garantías. Parámetros como modelo, tamaño y calidad se fijan en la herramienta."}
