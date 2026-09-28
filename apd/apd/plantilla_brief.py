"""Plantilla de brief (NUEVA, de esta app). Sus bloques coinciden con:
  - las facetas de la base de reglas (caso, D1–D9 de rules_v3.FACETAS), que deciden qué reglas aplican;
  - los bloques del prompt (secciones de compilador.FORMATOS), donde cada valor termina escrito.
Cada bloque declara su NIVEL en el flujo (U-2026-09-28-CAMBIO-QUIRURGICO): 0 = medio, 1 = tipo de pieza (perfil de
reglas), 2 = contenido de un bloque del prompt. Cámara, luz, lugar y ángulo NUNCA se preguntan: se infieren de lo que
dio el usuario (instrucción del director, 2026-09-28) y quedan editables con su origen a la vista."""

from __future__ import annotations

import json
import re
import sys

from . import spec as S

BLOQUES = [
    {"id": "medio", "nombre": "Medio", "nivel": 0, "campos": ["medio"], "faceta": "medio", "preguntar": True},
    {"id": "tipo", "nombre": "Tipo de pieza", "nivel": 1, "campos": ["tipo_tarea"], "faceta": "caso", "preguntar": True},
    {"id": "modelo", "nombre": "Modelo destino", "nivel": 1, "campos": ["modelo"], "faceta": "d8", "preguntar": False},
    {"id": "tratamiento", "nombre": "Tratamiento", "nivel": 1, "campos": ["tratamiento"], "faceta": "d4", "preguntar": False},
    {"id": "accion", "nombre": "Acción", "nivel": 1, "campos": ["accion"], "faceta": "d2", "preguntar": False},
    {"id": "sujeto", "nombre": "Sujeto e identidad", "nivel": 2, "campos": ["sujeto", "identidad"], "faceta": "d3",
     "entrega": ["sexo", "edad", "origen", "personalidad", "rasgos"], "preguntar": True},
    {"id": "lugar", "nombre": "Lugar / fondo", "nivel": 2, "campos": ["fondo"], "faceta": "d5", "preguntar": False},
    {"id": "encuadre", "nombre": "Encuadre, lente y foco", "nivel": 2, "campos": ["encuadre", "camara", "foco"], "faceta": "d6",
     "preguntar": False},
    {"id": "luz", "nombre": "Luz", "nivel": 2, "campos": ["luz"], "faceta": "d7", "preguntar": False},
    {"id": "angulo", "nombre": "Ángulo", "nivel": 2, "campos": ["angulo"], "faceta": "d9", "preguntar": False},
    {"id": "acabado", "nombre": "Color y textura", "nivel": 2, "campos": ["color", "textura"], "faceta": "d5", "preguntar": False},
    {"id": "uso", "nombre": "Uso", "nivel": 2, "campos": ["uso"], "faceta": None, "preguntar": False},
    {"id": "restricciones", "nombre": "Restricciones", "nivel": 2, "campos": ["restricciones"], "faceta": None, "preguntar": False},
    {"id": "parametros", "nombre": "Parámetros de la herramienta", "nivel": 2, "campos": ["formato", "calidad"], "faceta": None,
     "preguntar": False},
    {"id": "movimiento", "nombre": "Movimiento y audio (video)", "nivel": 2, "campos": ["movimiento", "audio", "duracion"],
     "faceta": None, "preguntar": False, "solo": "video"},
]
NUNCA_PREGUNTAR = {c for b in BLOQUES if not b["preguntar"] for c in b["campos"]} | {"lente"}
NIVEL_DE_CAMPO = {c: b["nivel"] for b in BLOQUES for c in b["campos"] + b.get("entrega", [])}

# Encuadre por tipo de pieza (sólo si el brief no lo dice). Fuente: definición de cada caso en rules_v3 CASOS / flujo-spot.
ENCUADRE_CASO = {
    "T1": "head-and-shoulders framing", "T2": "full-body framing, head to feet", "T3": "medium shot, waist up",
    "T4": "medium two-shot, both people waist up", "PROD": "product close-up, the product filling most of the frame",
    "GRAF": "centered poster layout with clear margins", "MULTI": "multi-panel grid, one pose per panel",
    "LUGAR": "wide establishing shot", "MULTITUD": "wide shot over the crowd",
}
# Lente por encuadre: video/references/camera-lighting-vocabulary.md §3 (citado por los regímenes 02/04/09).
LENTE = [(r"product", "100mm macro lens feel, shallow depth of field"),
         (r"close|head-and-shoulders|two-shot", "85mm portrait lens feel, shallow depth of field"),
         (r"medium", "50mm lens feel, moderate depth of field"),
         (r"full-body|wide|establishing|crowd", "35mm lens feel, deep depth of field"),
         (r"poster|panel|grid", "straight-on 50mm lens feel, even focus")]
LENTE_NB = {"85mm": "portrait lens perspective with gentle background separation", "50mm": "natural perspective",
            "35mm": "wide natural perspective", "100mm": "macro perspective"}
FONDO_CASO = {"T1": "plain seamless light grey (#D9D9D9) studio background", "T2": "plain seamless light grey (#D9D9D9) studio background",
              "PROD": "clean light grey (#E6E6E6) seamless sweep"}


def _v(c, k):
    return (c.get(k) or {}).get("valor")


def _abierto(c, k):
    return (c.get(k) or {}).get("estado") == "OPEN"


def inferir_app(spec: dict) -> list[dict]:
    """Inferencias deterministas para los bloques que no se preguntan. Cada una con su fuente."""
    from .propuestas import LUZ_POR_TRATAMIENTO
    from .flujos import D9_POR_ACCION, rules_v3
    c = spec["comunes"]
    casos = _v(c, "tipo_tarea") or []
    caso = casos[0] if casos else None
    texto = _v(c, "objetivo") or ""
    medio = _v(c, "medio")
    out = []

    def add(k, valor, fuente):
        if _abierto(c, k) and valor:
            out.append({"ruta": f"comunes.{k}", "valor": valor, "origen": "inferido_app", "fuente": fuente})
            c.setdefault(k, {})["valor"] = valor  # para inferencias encadenadas en esta misma pasada

    if medio == "imagen" and caso == "T5":
        return out  # edición: Preserve conserva todo lo demás; no se infieren campos de creación (el AST gate lo exige)
    if medio == "imagen":
        modelo = "gpt-image-2"
        if re.search(r"\b(agua|water|lluvia|rain|niebla|fog|humo|smoke|polvo|dust|spray|splash)\b", texto, re.I):
            modelo = "nano-banana-pro"
        add("modelo", modelo, "image/references/models.md: GPT Image 2 por defecto para identidad, piel y texto; "
                              "Nano Banana Pro para física de materiales (agua, humo, partículas)")
        trat = next((v for d, v, p in rules_v3().REGEX_FACETA if d == "d4" and p.search(texto)), None)
        add("tratamiento", trat or "comercial", ".claude/hooks/rules_v3.py REGEX_FACETA d4 sobre el brief"
            + ("" if trat else "; sin indicio documental/narrativo en el brief → comercial"))
        persona = caso in ("T1", "T2", "T3", "T4", "MULTI") or caso is None
        if persona:
            add("accion", "A_pose", "flujo-anclas D2 tipo A (pose sostenida) cuando el brief no describe una acción")
        else:
            for k, m in (("accion", "pieza sin persona: no hay acción de cuerpo (faceta d2 = ninguno)"),
                         ("identidad", "pieza sin persona: no hay identidad que fijar")):
                if _abierto(c, k):
                    out.append({"ruta": f"comunes.{k}", "valor": None, "estado": "NO_APLICA", "motivo": m, "origen": "inferido_app"})
                    c[k]["estado"] = "NO_APLICA"
        add("encuadre", ENCUADRE_CASO.get(caso), "tipo de pieza " + str(caso))
        enc = _v(c, "encuadre") or ""
        lente = next((l for p, l in LENTE if re.search(p, enc, re.I)), None)
        if lente and (_v(c, "modelo") or "").startswith("nano-banana"):
            lente = next((d for k, d in LENTE_NB.items() if k in lente), lente) + ", " + lente.split(", ", 1)[-1]
        add("camara", lente, "video/references/camera-lighting-vocabulary.md §3 (lente por encuadre); nano-banana.md:22-24 sin números")
        acc = _v(c, "accion")
        if acc in D9_POR_ACCION:
            add("angulo", D9_POR_ACCION[acc]["defecto"], f"flujo-anclas.html 'D9 por tipo de acción' fila {acc}")
        add("angulo", "eye-level", "storyboard-architect/references/shot-grammar.md:29 'Default to eye-level'")
        add("formato", {"T1": "2:3", "T2": "2:3", "T3": "3:2", "T4": "3:2", "PROD": "4:5", "GRAF": "2:3", "MULTI": "3:2"}.get(caso),
            "relación de aspecto por tipo de pieza (parámetro de la herramienta, editable)")
        t = _v(c, "tratamiento")
        if persona and t in LUZ_POR_TRATAMIENTO:
            add("luz", LUZ_POR_TRATAMIENTO[t][0], LUZ_POR_TRATAMIENTO[t][1])
        elif not persona:
            add("luz", "soft diffused key light from one side with a gentle fill, one clean specular highlight on the material",
                "regimenes/04 §4 (luz lateral para que el material se lea; un specular duro da material y forma)")
        add("fondo", FONDO_CASO.get(caso), "maestro/producto sobre fondo limpio (regimenes/09 hallazgo 'master on plain background')")
        add("foco", "sharp focus on the eyes" if persona else "the whole subject in sharp focus", "enfoque por tipo de pieza")
        add("textura", "natural skin texture: visible pores, natural tone variation, slight natural facial asymmetry" if persona
            else "true material texture", "image/references/golden-rules.md (describe materiales) · SW30 skin_doc (textura)")
        add("color", "natural colour", "sin indicación de B/N en el brief")
    return out


SIS_PLANTILLA = """Llenas una PLANTILLA DE BRIEF de producción visual a partir de lo que escribió el usuario.
Reglas:
- Usa sólo lo que el usuario dio y lo que se infiere de ello. No inventes restricciones.
- Nunca dejes vacíos ni preguntes por cámara, luz, lugar/fondo, ángulo, encuadre, color o textura: INFIÉRELOS de la
  información del usuario (tipo de pieza, tono, lugar mencionado, época, uso) y di en "porque" de qué dato lo infieres.
- Valores del prompt en inglés, concretos y visibles; sin vocabulario prohibido (stunning, epic, masterpiece, cinematic,
  beautiful lighting, professional, high quality); nada de emociones nombradas: señales físicas.
- Si un dato de contenido no está y no se puede inferir (p. ej. quién es el sujeto), pon null: se mostrará como faltante.
- "calidad", "formato" y "duracion" son parámetros de la herramienta, no descripción: calidad sólo low|medium|high|auto
  (GPT Image) o 1K|2K|4K (Nano Banana); formato sólo una relación de aspecto como 4:5; si no lo sabes, null.
Responde SOLO JSON: {"comunes": {"<campo>": {"valor": ..., "origen": "usuario"|"inferido", "porque": "..."}},
 "entregas": [{"id": "E1", "campos": {"<campo>": {"valor": ..., "origen": ..., "porque": "..."}}}]}
Campos comunes posibles: """ + ", ".join(S.TODOS)


# Parámetros de la herramienta (van fuera del texto): el modelo sólo puede poner un valor de su vocabulario cerrado.
# gpt-image.md:43-49 (low/medium/high/auto) · nano-banana (1K/2K/4K) · formato = relación de aspecto.
PARAMETROS = {"calidad": re.compile(r"low|medium|high|auto|[124]K", re.I),
              "formato": re.compile(r"\d{1,2}:\d{1,2}"),
              "duracion": re.compile(r"\d{1,3}\s*s?")}


def rellenar_con_modelo(brief: dict, spec: dict) -> tuple[list[dict], dict]:
    """El modelo llena la plantilla. Devuelve (cambios, uso). Sólo toca campos OPEN; lo LOCKED del brief manda."""
    from . import llm
    p = llm.proveedor()
    usuario = json.dumps({"brief": brief, "plantilla": [{"bloque": b["nombre"], "campos": b["campos"] + b.get("entrega", [])}
                                                        for b in BLOQUES],
                          "ya_fijado": {k: v["valor"] for k, v in spec["comunes"].items() if v["estado"] == "LOCKED"},
                          "entregas": [e["id"] for e in spec["entregas"]]}, ensure_ascii=False)
    r = p.completar(SIS_PLANTILLA, usuario)
    j = llm.extraer_json(r["texto"])
    cambios = []
    for k, x in (j.get("comunes") or {}).items():
        if k in PARAMETROS and not (isinstance(x, dict) and PARAMETROS[k].fullmatch(str(x.get("valor") or ""))):
            continue  # parámetro de la herramienta con valor que no es de su vocabulario: lo decide la app, no el modelo
        if k in spec["comunes"] and spec["comunes"][k]["estado"] == "OPEN" and isinstance(x, dict) and x.get("valor") not in (None, ""):
            cambios.append({"ruta": f"comunes.{k}", "valor": x["valor"], "origen": "inferido_modelo" if x.get("origen") != "usuario" else "brief_modelo",
                            "fuente": f"modelo: {x.get('porque', '')}"[:300]})
    ids = {e["id"]: e for e in spec["entregas"]}
    for ent in j.get("entregas") or []:
        e = ids.get(ent.get("id"))
        for k, x in ((ent.get("campos") or {}).items() if e else []):
            if k in PARAMETROS and not (isinstance(x, dict) and PARAMETROS[k].fullmatch(str(x.get("valor") or ""))):
                continue
            f = e["campos"].get(k)
            if f and f["estado"] == "OPEN" and isinstance(x, dict) and x.get("valor") not in (None, ""):
                cambios.append({"ruta": f"{e['id']}.{k}", "valor": x["valor"], "origen": "inferido_modelo",
                                "fuente": f"modelo: {x.get('porque', '')}"[:300]})
    return cambios, r.get("uso", {})


def completar(spec: dict, brief: dict, con_modelo: bool) -> tuple[dict, dict]:
    """Llena la plantilla: 1) modelo (si hay), 2) fuentes citadas y propuestas de la app para bloques que no se preguntan,
    3) reglas deterministas. Todo queda con su origen; nada se pregunta para cámara/luz/lugar/ángulo."""
    from .propuestas import proponer
    info = {"modelo": None}
    if con_modelo:
        try:
            cambios, uso = rellenar_con_modelo(brief, spec)
            spec, _ = S.aplicar_cambios(spec, cambios, "modelo")
            info["modelo"] = {"campos": [c["ruta"] for c in cambios], "uso": uso}
        except Exception as ex:
            info["modelo"] = {"error": f"{type(ex).__name__}: {ex}"[:300]}
            print(f"plantilla: el modelo falló, se usan las reglas deterministas — {info['modelo']['error']}", file=sys.stderr, flush=True)
    props = [dict(p, origen=f"propuesta_{p['clase']}_inferida") for p in proponer(spec)
             if p["ruta"].startswith("comunes.") and p["ruta"].split(".", 1)[1] in NUNCA_PREGUNTAR | {"modelo", "tratamiento", "calidad", "restricciones", "formato"}]
    spec, _ = S.aplicar_cambios(spec, props, "app")
    spec, _ = S.aplicar_cambios(spec, inferir_app(spec), "app")
    return spec, info


def vista(spec: dict, formato: str | None = None) -> list[dict]:
    """Filas para revisar la plantilla: bloque, nivel, faceta, slot del prompt, valor y origen de cada campo."""
    from .compilador import FORMATOS
    fmt = FORMATOS.get(formato or "") or {}
    slots = {}
    for sec in fmt.get("secciones", []):
        for campo in sec["campos"]:
            slots.setdefault(campo.replace("_linea", "").replace("_sin_mirada", ""), []).append(sec.get("etiqueta") or sec["id"])
    medio = _v(spec["comunes"], "medio")
    filas = []
    for b in BLOQUES:
        if b.get("solo") and b["solo"] != medio:
            continue
        campos = []
        for k in b["campos"]:
            f = spec["comunes"].get(k) or {}
            campos.append({"campo": k, "ruta": f"comunes.{k}", "valor": f.get("valor"), "estado": f.get("estado"),
                           "origen": f.get("origen"), "fuente": f.get("fuente") or f.get("motivo"), "slot": slots.get(k, [])})
        for e in spec["entregas"]:
            for k in b.get("entrega", []):
                f = e["campos"].get(k)
                if f:
                    campos.append({"campo": f"{e['id']}.{k}", "ruta": f"{e['id']}.{k}", "valor": f.get("valor"), "estado": f.get("estado"),
                                   "origen": f.get("origen"), "fuente": f.get("fuente") or f.get("motivo"), "slot": slots.get(k, [])})
        falta = [x["campo"] for x in campos if x["estado"] == "OPEN"]
        filas.append({"bloque": b["id"], "nombre": b["nombre"], "nivel": b["nivel"], "faceta": b["faceta"],
                      "se_pregunta": b["preguntar"], "campos": campos, "faltan": falta})
    return filas
