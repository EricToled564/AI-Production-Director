"""Selección por catálogo: facetas del caso desde el brief validado y filtro de las reglas catalogadas.

El catálogo (recursos/catalogo_taxonomia.json) se hace por adelantado, de lo general a lo específico:
ámbito → medio → modelo → operación → caso → facetas D1–D9 (taxonomía de .claude/hooks/rules_v3.py).
Las reglas de ámbito plantilla_brief y plantilla_prompt se aplican siempre a las plantillas y no entran
a la selección. Para cada imagen solo se filtran las de ámbito "seleccionable".

Las facetas del caso salen primero de entrada.selecciones_taxonomicas cuando trae códigos de la taxonomía
("caso:T3", "d2:B_pico"…), que el usuario revisó con el brief; si una dimensión no viene así, se deduce
de los campos del brief por palabras clave. Una dimensión que no se puede deducir no filtra: es preferible
mandar una regla de más a la confirmación que perder una que aplica.
"""
import json
import re
import unicodedata

MODELO = "gpt-image-2"
DIMENSIONES = ("d2", "d3", "d4", "d9")


def _n(texto):
    return unicodedata.normalize("NFKD", str(texto).lower()).encode("ascii", "ignore").decode()


def _valores(brief):
    return {c["path"]: c.get("valor") for c in brief}


def _texto(v):
    return _n(json.dumps(v, ensure_ascii=False)) if v not in (None, "", []) else ""


def _hay(texto, *palabras):
    return any(re.search(r"\b" + p, texto) for p in palabras)


def facetas_del_caso(brief):
    """Devuelve {"operacion": set, "caso": set|None, "d2": set|None, ...}; None = no se pudo deducir."""
    v = _valores(brief)
    f = {"operacion": None, "caso": None, "d2": None, "d3": None, "d4": None, "d9": None, "origen": {}}

    # 1) Códigos explícitos de la taxonomía en selecciones_taxonomicas (revisados por el usuario).
    explicitos = {}
    for item in v.get("entrada.selecciones_taxonomicas") or []:
        m = re.match(r"\s*(caso|operacion|d[1-9])\s*:\s*([A-Za-z0-9_\-\.]+)", str(item))
        if m:
            explicitos.setdefault(m.group(1), set()).add(m.group(2))
    for k, vals in explicitos.items():
        if k in f:
            f[k] = vals
            f["origen"][k] = "selecciones_taxonomicas"

    # 2) Deducción por campos del brief para lo que no vino explícito.
    op = _texto(v.get("entrada.operacion"))
    refs = v.get("entrada.referencias[].archivo")
    if f["operacion"] is None:
        ops = set()
        if _hay(op, "genesis", "crear", "generacion"):
            ops.add("genesis")
        if _hay(op, "edicion", "editar"):
            ops.add("edicion")
        if _hay(op, "referencia") or (refs not in (None, "", [])):
            ops.add("referencia")
        f["operacion"] = ops or None

    cantidad = v.get("entrada.sujetos.cantidad")
    try:
        cantidad = int(re.search(r"\d+", str(cantidad)).group()) if cantidad not in (None, "") else None
    except AttributeError:
        cantidad = None
    regimen = _texto(v.get("entrada.fisica.regimen"))
    clases = _texto(v.get("entrada.sujetos.items[].clase"))
    contactos = _texto(v.get("entrada.blocking.contactos"))
    multitud = _hay(regimen + " " + _texto(v.get("entrada.escena.planos")), "multitud", "publico", "asistentes")

    if f["d3"] is None and cantidad is not None:
        d3 = set()
        personas = cantidad if (not clases or _hay(clases, "persona", "humano", "hombre", "mujer", "ciclista")) else 0
        if personas == 0:
            d3.add("0")
        elif personas == 1:
            d3.add("1")
        elif personas == 2:
            d3.add("2_contacto" if _hay(contactos, "entre", "abrazo", "contacto fisico", "choque") else "2_sin_contacto")
        else:
            d3.add("ensamble")
        if multitud:
            d3.add("multitud")
        f["d3"] = d3

    if f["caso"] is None:
        casos = set()
        if f["operacion"] and "edicion" in f["operacion"]:
            casos.add("T5")
        d3 = f["d3"] or set()
        if "1" in d3:
            casos.add("T3")
        if d3 & {"2_contacto", "2_sin_contacto"}:
            casos.add("T4")
        if "ensamble" in d3:
            casos.add("ENSAMBLE")
        if "multitud" in d3:
            casos.add("MULTITUD")
        for palabra, caso in (("producto", "PROD"), ("lugar", "LUGAR"), ("edific", "EDIF"), ("animal", "ANIMAL"),
                              ("objeto", "OBJ"), ("vehiculo", "OBJ")):
            if palabra in clases:
                casos.add(caso)
        if v.get("entrada.texto_marca.literales") not in (None, "", []):
            casos.add("GRAF")
        f["caso"] = casos or None

    accion = " ".join(_texto(v.get(p)) for p in ("entrada.accion.tipo", "entrada.accion.estado_visible", "entrada.fisica.regimen"))
    if f["d2"] is None and accion.strip():
        d2 = set()
        if _hay(accion, "pose", "retrato", "quiet", "estatic"):
            d2.add("A_pose")
        if _hay(accion, "pico", "esfuerzo", "impacto", "salto", "sprint", "apex"):
            d2.add("B_pico")
        if _hay(accion, "movimiento", "velocidad", "barrido", "pedale", "corr"):
            d2.add("C_movimiento")
        if _hay(accion, "lluvia", "rayo", "niebla", "polvo", "clima", "amanecer"):
            d2.add("D_luz_clima")
        if _hay(accion, "interacc", "contacto entre", "abrazo"):
            d2.add("E_interaccion")
        if multitud:
            d2.add("F_multitud")
        f["d2"] = d2 or None

    estilo = " ".join(_texto(v.get(p)) for p in ("entrada.pieza.tipo", "entrada.estilo", "entrada.pieza.objetivo"))
    if f["d4"] is None and estilo.strip():
        d4 = set()
        if _hay(estilo, "documental", "reportaje", "editorial", "fotoperiod"):
            d4.add("documental")
        if _hay(estilo, "comercial", "publicid", "spot", "producto", "campana"):
            d4.add("comercial")
        if _hay(estilo, "narrativ", "cine", "ficcion", "cortometraje"):
            d4.add("narrativo")
        if _hay(estilo, "carrera", "drift", "race"):
            d4.add("race")
        if _hay(estilo, "ugc", "tiktok", "celular"):
            d4.add("ugc")
        if _hay(estilo, "animacion", "ilustracion", "3d", "stop motion"):
            d4.add("animacion")
        f["d4"] = d4 or None

    angulo = _texto(v.get("entrada.camara.angulo")) + " " + _texto(v.get("entrada.camara.altura"))
    if f["d9"] is None and angulo.strip():
        d9 = set()
        if _hay(angulo, "contrapicado", "bajo", "low", "ras"):
            d9.add("low")
        if _hay(angulo, "picado", "alto", "high") and not _hay(angulo, "contrapicado"):
            d9.add("high")
        if _hay(angulo, "cenital", "overhead", "top"):
            d9.add("overhead")
        if _hay(angulo, "holandes", "dutch", "inclinad"):
            d9.add("dutch")
        if _hay(angulo, "pov", "subjetiv", "primera persona"):
            d9.add("pov")
        if _hay(angulo, "ojos", "eye", "frontal", "nivel"):
            d9.add("eye-level")
        f["d9"] = d9 or None
    for k in ("operacion", "caso", *DIMENSIONES):
        f["origen"].setdefault(k, "deducida" if f[k] else "sin_dato")
    return f


def _cruza(valores_regla, valores_caso, comodines=("ninguno",)):
    if valores_caso is None:
        return True
    vals = set(valores_regla or [])
    return bool(vals & set(comodines)) or bool(vals & valores_caso)


PERSONAS = {"T1", "T2", "T3", "T4", "ENSAMBLE"}


def candidatas(catalogo, facetas):
    """Reglas seleccionables que pasan el filtro jerárquico. Un caso con personas acepta las reglas de
    cualquier caso de personas (maestros, cuadros de 1 o 2, ensamble): la confirmación descarta las que no."""
    facetas = dict(facetas)
    if facetas["caso"] and facetas["caso"] & PERSONAS:
        facetas["caso"] = facetas["caso"] | PERSONAS
    salida = []
    for r in catalogo:
        if r.get("ambito") != "seleccionable" or r.get("medio") not in ("imagen", "ambos"):
            continue
        if not _cruza(r.get("modelo"), {MODELO}, ("ninguno", "agnostico")):
            continue
        if not _cruza(r.get("operacion"), facetas["operacion"], ("cualquiera",)):
            continue
        if not _cruza(r.get("caso"), facetas["caso"], ()):
            continue
        if not all(_cruza(r.get(d), facetas[d]) for d in DIMENSIONES):
            continue
        salida.append(r)
    return salida


def plantilla(catalogo, ambito):
    return [r for r in catalogo if r.get("ambito") == ambito]
