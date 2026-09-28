"""Brief → especificación estructurada.

Dos capas, y la app muestra cuál decidió cada campo:
  * `analizar_determinista` — regex/frases ES-EN, sin modelo. Siempre corre.
  * el modelo (llm.py), si está configurado, propone el mismo JSON; las diferencias se
    marcan y nunca pisan un valor que el usuario fijó.

Cada campo: {valor, valor_brief, estado LOCKED|OPEN|NO_APLICA, origen, motivo,
prompt_required, fuente}. `origen`:
  brief        el texto del brief lo dice
  usuario      lo fijó el usuario en el editor
  modelo       lo propuso el modelo (decisión creativa, no regla)
  propuesta    lo propuso la app desde una fuente citada (flujo/skill); requiere confirmar
  derivado     se sigue mecánicamente de otro campo
Una decisión creativa nunca se atribuye a una regla: `fuente` sólo se llena cuando
una fuente original respalda literalmente el valor.
"""

from __future__ import annotations

import copy
import re
import unicodedata

CAMPOS_IMAGEN = ["objetivo", "medio", "modelo", "tipo_tarea", "sujeto", "identidad", "accion", "camara",
                 "angulo", "lente", "encuadre", "foco", "luz", "fondo", "textura", "tratamiento",
                 "color", "referencias", "restricciones", "formato", "calidad"]
CAMPOS_VIDEO_EXTRA = ["movimiento", "duracion", "continuidad", "audio"]
TODOS = CAMPOS_IMAGEN + CAMPOS_VIDEO_EXTRA

# Campos que la app necesita LOCKED antes de compilar (o NO_APLICA con motivo).
REQUERIDOS_PROMPT = {
    "imagen": ["sujeto", "identidad", "encuadre", "angulo", "camara", "fondo", "luz", "textura", "restricciones"],
    "video": ["sujeto", "accion_video", "movimiento", "angulo", "luz", "audio"],
    "edicion": ["cambio", "preservar", "restricciones"],
}
CAMPOS_VIDEO_EXTRA = ["movimiento", "duracion", "continuidad", "audio", "accion_video"]
TODOS = CAMPOS_IMAGEN + CAMPOS_VIDEO_EXTRA + ["cambio", "preservar"]


def requeridos(spec: dict) -> list[str]:
    c = spec["comunes"]
    if "T5" in (c["tipo_tarea"]["valor"] or []):
        return REQUERIDOS_PROMPT["edicion"]
    return REQUERIDOS_PROMPT[c["medio"]["valor"]]
REQUERIDOS_PARAMETRO = {"imagen": ["modelo", "formato", "calidad"], "video": ["modelo", "formato", "duracion"]}

MODELOS = {
    "gpt-image-2": {"medio": "imagen", "nombre": "GPT Image 2", "re": r"gpt[- ]?image[- ]?2|gpt image|gpt-image"},
    "nano-banana-pro": {"medio": "imagen", "nombre": "Nano Banana Pro", "re": r"nano[- ]?banana[- ]?pro|\bnbp\b"},
    "nano-banana-2": {"medio": "imagen", "nombre": "Nano Banana 2", "re": r"nano[- ]?banana[- ]?2|\bnb2\b|nano[- ]?banana(?![- ]?pro)"},
    "midjourney": {"medio": "imagen", "nombre": "Midjourney", "re": r"midjourney|\bmj\b"},
    "flux": {"medio": "imagen", "nombre": "Flux", "re": r"\bflux\b"},
    "kling": {"medio": "video", "nombre": "Kling 3.0", "re": r"\bkling\b"},
    "veo": {"medio": "video", "nombre": "Veo 3.1", "re": r"\bveo\b"},
    "seedance": {"medio": "video", "nombre": "Seedance", "re": r"\bseedance\b"},
    "hailuo": {"medio": "video", "nombre": "Hailuo", "re": r"\bhailuo\b"},
}

NUMEROS = {"un": 1, "una": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7,
           "ocho": 8, "nueve": 9, "diez": 10, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}

# Frase del brief → valor en inglés para el prompt. Sólo traducción literal; nada creativo.
FRASES = [
    (r"hombros hacia arriba|de hombros para arriba|shoulders[- ]up|head and shoulders|cabeza y hombros",
     "encuadre", "head-and-shoulders framing"),
    (r"primer plano|close[- ]up", "encuadre", "close-up framing"),
    (r"plano medio|medium shot|cintura para arriba|waist[- ]up", "encuadre", "medium shot, waist up"),
    (r"cuerpo (?:entero|completo)|full[- ]body", "encuadre", "full-body framing, head to feet"),
    (r"fondo gris claro|light gr[ae]y background", "fondo", "plain seamless light grey (#D9D9D9) studio background"),
    (r"fondo blanco|white background", "fondo", "plain seamless white (#FFFFFF) studio background"),
    (r"fondo negro|black background", "fondo", "plain black (#111111) background"),
    (r"rostros? naturales?|natural faces?|piel natural|natural skin", "textura",
     "natural skin texture: visible pores, natural tone variation, slight natural facial asymmetry"),
    (r"sin retoque|no retouch", "textura", "unretouched skin"),
    (r"a color|en color|full colou?r|color natural", "color", "natural colour"),
    (r"blanco y negro|black and white|b/n\b", "color", "black-and-white photograph"),
    (r"luz suave|soft light", "luz", "soft even light"),
    (r"luz dura|hard light", "luz", "hard directional light"),
    (r"luz natural|natural light", "luz", "natural available light"),
]
TRATAMIENTO_RE = [
    ("documental", r"documental|documentary|reportaje"),
    ("comercial", r"comercial|commercial|publicitari|advertis|packshot|producto"),
    ("narrativo", r"cinematogr|narrativ|cortometraje|film\b|pel[ií]cula"),
    ("ugc", r"\bugc\b|tiktok|reel org|celular en mano"),
    ("animacion", r"animaci[oó]n|animated|stop motion|\b3d\b"),
    ("race", r"carrera|drift|race\b|racing"),
]
ASPECT_RE = re.compile(r"\b(1:1|4:5|5:4|2:3|3:2|9:16|16:9|3:4|4:3|21:9)\b")
DURACION_RE = re.compile(r"(\d{1,3})\s*(?:s\b|seg|segundos|seconds)", re.I)
EDAD_RE = re.compile(r"(\d{1,2})\s*(?:[–\-a]|to|y)\s*(\d{1,2})\s*(?:años|years|yo\b)", re.I)
SEXOS_RE = re.compile(r"(\w+)\s+(mujeres|hombres|women|men|chicas|chicos)", re.I)
RETRATOS_RE = re.compile(r"(\d+|\w+)\s+(retratos|portraits|headshots|im[aá]genes|images|fotos|photos|clips|videos)", re.I)


def sin_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def campo(valor=None, estado=None, origen="brief", motivo="", prompt_required=True, fuente="", valor_brief=""):
    if estado is None:
        estado = "LOCKED" if valor not in (None, "", []) else "OPEN"
    return {"valor": valor, "valor_brief": valor_brief, "estado": estado, "origen": origen,
            "motivo": motivo, "prompt_required": prompt_required, "fuente": fuente}


def _num(tok: str) -> int | None:
    tok = tok.lower()
    if tok.isdigit():
        return int(tok)
    return NUMEROS.get(sin_acentos(tok))


def detectar_recorrido(texto: str, refs: list[dict]) -> dict:
    t = sin_acentos(texto.lower())
    roles = {r.get("rol") for r in refs or []}
    spot = re.search(r"\bspot\b|comercial de \d+|campa[nñ]a|brand film|explainer|cortometraje|video completo|"
                     r"pipeline completo|de brief a video|production package|\breel con narrativa", t)
    clip = re.search(r"\bclip\b|\bvideo\b|image[- ]to[- ]video|\bkling\b|\bveo\b|\bseedance\b|\bhailuo\b|movimiento de c[aá]mara", t)
    ancla = re.search(r"\bancla\b|\banchor\b|keyframe|tarjeta de ancla|frame inicial|first frame", t)
    edicion = re.search(r"edici[oó]n quir[uú]rgica|\bedita(?:r)?\b|retoque|inpaint|cambia(?:r)? (?:el|la|los)|quita(?:r)?|remove\b", t) or "edicion" in roles
    dur = DURACION_RE.search(t)
    mins = re.search(r"(\d{1,2})\s*(?:min|minutos|minutes)", t)
    if spot:
        seg = int(dur.group(1)) if dur else (int(mins.group(1)) * 60 if mins else None)
        track = None
        if seg is not None:
            track = "EXPRESS" if seg <= 30 and not re.search(r"marca|brand", t) else ("STANDARD" if seg <= 90 else "FILM")
        return {"recorrido": "SPOT", "track": track, "segundos": seg,
                "motivo": "el brief pide una pieza completa (spot/campaña/film)" +
                          (f"; {seg}s" if seg else "; duración no indicada → track pendiente")}
    if ancla:
        return {"recorrido": "ANCLA", "motivo": "el brief pide un ancla/keyframe (imagen que heredará el video)"}
    if clip:
        return {"recorrido": "CLIP", "motivo": "el brief pide un clip de video aislado"}
    if edicion:
        return {"recorrido": "IMAGEN", "subtipo": "edicion", "motivo": "edición sobre imagen existente"}
    if refs:
        return {"recorrido": "IMAGEN", "subtipo": "con_referencia", "motivo": "imagen con referencias adjuntas"}
    return {"recorrido": "IMAGEN", "subtipo": "genesis", "motivo": "imagen sin referencia (génesis)"}


def detectar_caso(texto: str, recorrido: dict, n_sujetos: int | None, en_cuadro: int | None = None) -> tuple[list[str], str]:
    t = sin_acentos(texto.lower())
    if recorrido["recorrido"] == "CLIP":
        return ["CLIP"], "clip de video"
    if recorrido.get("subtipo") == "edicion":
        return ["T5"], "edición quirúrgica"
    if re.search(r"producto|packshot|product shot|comida|bebida|food|beverage", t) and not re.search(r"retrato|portrait", t):
        return ["PROD"], "producto sin persona"
    if re.search(r"poster|slide|\bui\b|thumbnail|banner|tipograf", t):
        return ["GRAF"], "pieza gráfica"
    if re.search(r"multi[- ]?panel|\bgrid\b|cuadricula|character sheet", t):
        return ["MULTI"], "multi-panel"
    if re.search(r"placa|locacion vacia|empty plate|environment", t):
        return ["LUGAR"], "placa de lugar"
    if re.search(r"multitud|estadio|crowd|publico", t):
        return ["MULTITUD"], "multitud anónima"
    retrato = re.search(r"retrato|portrait|headshot|casting|maestro de rostro|rostro", t)
    hombros = re.search(r"hombros|shoulders|cabeza y hombros|head and shoulders|primer plano", t)
    if retrato and (hombros or "casting" in t) and recorrido.get("subtipo") != "con_referencia":
        return ["T1"], "retrato de identidad sin referencia (génesis de rostro T1: flujo-spot Nivel 3 Persona paso 1)"
    if re.search(r"cuerpo (?:entero|completo)|full[- ]body|maestro de cuerpo", t):
        return ["T2"], "maestro de cuerpo"
    if re.search(r"dos personas|two people|pareja|abrazo|high five|apret[oó]n", t) or en_cuadro == 2:
        return ["T4"], "cuadro con 2 personas"
    if n_sujetos and n_sujetos >= 1:
        return ["T3"], "cuadro con 1 persona"
    return ["T3"], "cuadro con persona (por defecto; confirmar)"


def _sexos(texto: str) -> list[str]:
    out = []
    for n, s in SEXOS_RE.findall(texto):
        k = _num(n)
        if not k:
            continue
        s = s.lower()
        val = "woman" if s in ("mujeres", "women", "chicas") else "man"
        out += [val] * k
    return out


def analizar_determinista(brief: dict) -> dict:
    texto = brief.get("texto", "")
    refs = brief.get("referencias", []) or []
    t = texto
    tl = sin_acentos(texto.lower())
    rec = detectar_recorrido(texto, refs)
    medio = {"IMAGEN": "imagen", "ANCLA": "imagen", "CLIP": "video", "SPOT": "video"}[rec["recorrido"]]

    # número de entregas y sexos
    n = None
    m = RETRATOS_RE.search(t)
    if m:
        n = _num(m.group(1))
    sexos = _sexos(t)
    # Los sujetos con sexo cuentan entregas sólo si el brief nombra entregables ("cinco retratos", "portraits");
    # si no, son personas dentro de UNA imagen ("dos hombres jugando ajedrez" = 1 cuadro con 2 personas → T4).
    entregables = bool(m) or bool(re.search(r"\b(retratos|portraits|headshots)\b", tl))
    if sexos and entregables and (n is None or n == len(sexos)):
        n = len(sexos)
    en_cuadro = len(sexos) if sexos and not entregables else None
    n = n or 1
    casos, motivo_caso = detectar_caso(t, rec, n, en_cuadro)

    comunes: dict[str, dict] = {k: campo(None) for k in TODOS}
    comunes["objetivo"] = campo(texto.strip()[:300], origen="brief", prompt_required=False, valor_brief=texto.strip()[:300])
    comunes["medio"] = campo(medio, origen="derivado", motivo=rec["motivo"], prompt_required=False)
    comunes["tipo_tarea"] = campo(casos, origen="derivado", motivo=motivo_caso, prompt_required=False)

    mod = brief.get("modelo") or None
    if not mod:
        for k, v in MODELOS.items():
            if re.search(v["re"], tl):
                mod = k
                break
    if mod:
        comunes["modelo"] = campo(mod, origen="brief" if not brief.get("modelo") else "usuario", prompt_required=False)
    else:
        comunes["modelo"] = campo(None, estado="OPEN", prompt_required=False,
                                  motivo="el brief no nombra modelo destino: decide sintaxis y parámetros")

    for pat, k, val in FRASES:
        mm = re.search(pat, tl)
        if mm:
            prev = comunes[k]["valor"]
            comunes[k] = campo(val if not prev else prev + "; " + val, origen="brief", valor_brief=mm.group(0))

    for trat, pat in TRATAMIENTO_RE:
        mm = re.search(pat, tl)
        if mm and not (trat == "comercial" and casos == ["T1"] and "casting" in tl):
            comunes["tratamiento"] = campo(trat, origen="brief", valor_brief=mm.group(0), prompt_required=False)
            break
    if comunes["tratamiento"]["estado"] == "OPEN":
        comunes["tratamiento"]["prompt_required"] = False
        comunes["tratamiento"]["motivo"] = ("D4 tratamiento no indicado; decide luz dura rasante (documental, SW30 T1) "
                                            "o luz pareja (character ref / comercial) — flujo-anclas D7")

    am = ASPECT_RE.search(t) or (ASPECT_RE.search(brief.get("formato", "") or ""))
    if am:
        comunes["formato"] = campo(am.group(1), origen="brief" if not brief.get("formato") else "usuario", prompt_required=False)
    else:
        comunes["formato"] = campo(None, estado="OPEN", prompt_required=False,
                                   motivo="relación de aspecto no indicada; es parámetro de la herramienta, no texto")
    comunes["calidad"] = campo(None, estado="OPEN", prompt_required=False, motivo="parámetro de la herramienta")
    comunes["referencias"] = campo([{"nombre": r.get("nombre"), "rol": r.get("rol"), "sha256": r.get("sha256")} for r in refs],
                                   estado="LOCKED" if refs else "NO_APLICA", origen="usuario" if refs else "derivado",
                                   motivo="" if refs else "sin referencias adjuntas: génesis desde texto",
                                   prompt_required=bool(refs))
    rest = []
    if re.search(r"sin texto|no text", tl):
        rest.append("no text")
    comunes["restricciones"] = campo(rest or None, origen="brief" if rest else "derivado",
                                     estado="LOCKED" if rest else "OPEN",
                                     motivo="" if rest else "se completa con las restricciones que exijan las reglas APLICA")
    if "casting" in tl:
        comunes["objetivo"]["valor"] = texto.strip()[:300]
        comunes["uso"] = campo("casting reference portrait",
                               origen="derivado", motivo="casting → maestro de identidad (flujo-spot Nivel 3, Persona paso 1); "
                                                         "el rol T1 va en notas, no en el cuerpo (consistency-locks.md:115-116)")
    ctx = re.search(r"(quinteto de cuerdas|string quintet|cuarteto de cuerdas|string quartet|orquesta|banda)", tl)
    if ctx:
        comunes["contexto"] = campo({"quinteto de cuerdas": "members of a string quintet",
                                     "string quintet": "members of a string quintet",
                                     "cuarteto de cuerdas": "members of a string quartet",
                                     "string quartet": "members of a string quartet"}.get(ctx.group(1), ctx.group(1)),
                                    origen="brief", valor_brief=ctx.group(1))

    # campos que no aplican al medio
    if medio == "imagen":
        for k in CAMPOS_VIDEO_EXTRA:
            comunes[k] = campo(None, estado="NO_APLICA", origen="derivado", prompt_required=False,
                               motivo="imagen fija: 'Movimiento: un still es un instante congelado' (flujo-spot Nivel 4)")
    else:
        for k in ("textura", "identidad", "encuadre", "fondo", "restricciones", "camara"):
            comunes[k]["prompt_required"] = False
        dm = DURACION_RE.search(t)
        if dm:
            comunes["duracion"] = campo(f"{dm.group(1)}s", origen="brief", prompt_required=False)
        else:
            comunes["duracion"]["prompt_required"] = False
            comunes["duracion"]["motivo"] = "duración no indicada: parámetro de la herramienta"

    if casos == ["T5"]:
        comunes["cambio"] = campo(None, estado="OPEN", motivo="un solo cambio concreto por iteración (gpt-image.md Editing: 'Один edit за итерацию')")
        for k in ("sujeto", "identidad", "encuadre", "angulo", "camara", "fondo", "luz", "textura", "color", "tratamiento"):
            comunes[k] = campo(None, estado="NO_APLICA", origen="derivado", prompt_required=False,
                               motivo="edición: lo que no cambia va en Preserve, no se re-describe (SW30 R3/R5)")
    else:
        comunes["cambio"] = campo(None, estado="NO_APLICA", origen="derivado", prompt_required=False, motivo="no es edición")
        comunes["preservar"] = campo(None, estado="NO_APLICA", origen="derivado", prompt_required=False, motivo="no es edición")
    if rec["recorrido"] == "ANCLA":
        comunes["medio"] = campo("imagen", origen="derivado", prompt_required=False, motivo="el ancla es una imagen fija")
    # accion (D2) por defecto
    if casos == ["T1"]:
        comunes["accion"] = campo("A_pose", origen="derivado", prompt_required=False,
                                  motivo="maestro de identidad = pose sostenida (flujo-anclas D2 tipo A: 'maestro de identidad')",
                                  fuente="flujo-anclas.html Paso 3 · tipo A")
        comunes["angulo"] = campo("eye-level", origen="propuesta", prompt_required=True,
                                  motivo="D9 por tipo de acción A: 'Eye-level para maestros de identidad; low o high solo si el beat lo pide'",
                                  fuente="flujo-anclas.html · D9 por tipo de acción · kling §7 · shot-grammar")
        comunes["angulo"]["estado"] = "LOCKED"
    edad = EDAD_RE.search(t)
    rango = (int(edad.group(1)), int(edad.group(2))) if edad else None

    entregas = []
    if rec["recorrido"] == "SPOT":
        n = 0  # las entregas salen de shots.json (E4: fuente de verdad, APD §6.3)
    for i in range(n):
        e = {"id": f"E{i + 1}", "nombre": f"Entrega {i + 1}", "casos": casos, "campos": {}}
        if sexos and i < len(sexos) and not en_cuadro:
            e["campos"]["sexo"] = campo(sexos[i], origen="brief", valor_brief=f"{sexos.count(sexos[i])} {sexos[i]}")
        if rango:
            e["campos"]["edad"] = campo(None, estado="OPEN", motivo=f"elegir una edad dentro de {rango[0]}–{rango[1]} (restricción del brief)",
                                        valor_brief=f"{rango[0]}–{rango[1]} años")
            e["campos"]["edad"]["rango"] = list(rango)
        if re.search(r"or[ií]genes diversos|diverse (?:origins|backgrounds|ethnicit)", tl):
            e["campos"]["origen"] = campo(None, estado="OPEN", motivo="el brief exige orígenes diversos: uno distinto por entrega",
                                          valor_brief="orígenes diversos")
        if re.search(r"personalidades distintas|distinct personalit|different personalit", tl):
            e["campos"]["personalidad"] = campo(None, estado="OPEN",
                                                motivo="el brief exige personalidades distintas: una por entrega, legible en expresión/postura",
                                                valor_brief="personalidades distintas")
        if casos and casos[0] in ("T1", "T2", "T3", "T4"):
            e["campos"]["rasgos"] = campo(None, estado="OPEN",
                                          motivo="rasgos de identidad concretos (pelo, rostro, vestuario visible) — decisión creativa")
            if ctx:
                e["campos"]["instrumento"] = campo(None, estado="OPEN", prompt_required=False,
                                                   motivo="rol en el quinteto (decisión creativa; con hombros hacia arriba el instrumento puede no verse)")
        entregas.append(e)

    if rec["recorrido"] == "ANCLA":
        from .flujos import TARJETA_ANCLA, rules_v3
        # D2/D3/D9 desde el texto con los patrones ORIGINALES de rules_v3.REGEX_FACETA (evidencia de regex: editable)
        hall = {}
        for dim, val, pat in rules_v3().REGEX_FACETA:
            if dim in ("d2", "d3", "d9") and pat.search(texto) and not (dim == "d2" and val == "A_pose" and hall.get("d2")):
                # defecto del original: el patrón d9 'high' contiene 'picado' sin límite de palabra y captura
                # 'contrapicado' (ángulo bajo). Se corrige aquí sin tocar rules_v3.py; ver CHECKLIST (hallazgos).
                if dim == "d9" and val == "high" and re.search(r"contrapicad", texto, re.I) and not re.search(r"(?<!contra)picad", texto, re.I):
                    continue
                hall.setdefault(dim, val)
        if hall.get("d2") and comunes["accion"]["estado"] != "LOCKED":
            comunes["accion"] = campo(hall["d2"], origen="brief (rules_v3.REGEX_FACETA)", prompt_required=False,
                                      fuente=".claude/hooks/rules_v3.py REGEX_FACETA d2")
        det = {"d1": ("keyframe_ff" if re.search(r"frame inicial|first frame|keyframe", tl) else None),
               "d2": comunes["accion"]["valor"] if comunes["accion"]["estado"] == "LOCKED" else None,
               "d3": ("1" if n == 1 and re.search(r"\buna? (?:persona|mujer|hombre|atleta|clavadista)\b|\bsolo\b", tl) else None),
               "d4": comunes["tratamiento"]["valor"] if comunes["tratamiento"]["estado"] == "LOCKED" else None,
               "d8": comunes["modelo"]["valor"], "d9": hall.get("d9")}
        if not det["d3"] and hall.get("d3"):
            det["d3"] = hall["d3"]
        for dim in TARJETA_ANCLA:
            v = det.get(dim["dim"])
            comunes[f"tarjeta_{dim['dim']}"] = campo(v, origen="brief" if v else "brief", prompt_required=False,
                                                     motivo=f"{dim['nombre']}: {dim['valores']}", fuente="flujo-anclas.html Paso 1")
            comunes[f"tarjeta_{dim['dim']}"]["tarjeta"] = True
        for k in ("d1", "d3"):
            if det.get(k):
                comunes[k] = campo(det[k], origen="brief", prompt_required=False)
    ambig = ambiguedades({"comunes": comunes, "entregas": entregas, "recorrido": rec})
    return {"version_parser": "det-1", "recorrido": rec, "comunes": comunes, "entregas": entregas,
            "ambiguedades": ambig, "n_entregas": n}


def ambiguedades(spec: dict) -> list[dict]:
    out = []
    c = spec["comunes"]
    medio = c["medio"]["valor"]
    for k in REQUERIDOS_PARAMETRO.get(medio, []):
        if c.get(k, {}).get("estado") == "OPEN":
            out.append({"campo": k, "decisiva": k == "modelo", "motivo": c[k].get("motivo") or "parámetro sin fijar"})
    for k in requeridos(spec):
        f = c.get(k)
        if f and f["estado"] == "OPEN" and f.get("prompt_required", True):
            out.append({"campo": k, "decisiva": True, "motivo": f.get("motivo") or "campo requerido por la plantilla sin valor"})
    if c.get("tratamiento", {}).get("estado") == "OPEN" and "T1" in (c["tipo_tarea"]["valor"] or []):
        out.append({"campo": "tratamiento", "decisiva": True, "motivo": c["tratamiento"]["motivo"]})
    if c.get("color", {}).get("estado") == "OPEN" and medio == "imagen":
        out.append({"campo": "color", "decisiva": True,
                    "motivo": "color o B/N no indicado; SW30 usecase_doc cita Kodak Tri-X (stock B/N): en Vivaldi produjo B/N no pedido "
                              "(produccion/vivaldi-invierno/05-genesis-anclas.md, corrección 1)"})
    for e in spec["entregas"]:
        for k, f in e["campos"].items():
            if f["estado"] == "OPEN" and f.get("prompt_required", True):
                out.append({"campo": f"{e['id']}.{k}", "decisiva": False, "motivo": f["motivo"]})
    if spec["recorrido"]["recorrido"] == "SPOT" and not spec["recorrido"].get("track"):
        out.append({"campo": "track", "decisiva": True, "motivo": "duración/marca no indicadas: EXPRESS, STANDARD o FILM"})
    return out


def aplicar_cambios(spec: dict, cambios: list[dict], autor: str = "usuario") -> tuple[dict, list[str]]:
    """Aplica cambios explícitos {ruta: 'comunes.fondo' | 'E2.edad', valor, estado?, motivo?}.
    Devuelve (spec nueva, rutas cambiadas). Nunca modifica la spec recibida."""
    s = copy.deepcopy(spec)
    tocadas = []
    for c in cambios:
        ruta = c["ruta"]
        if ruta.startswith("comunes."):
            k = ruta.split(".", 1)[1]
            destino = s["comunes"]
        else:
            eid, k = ruta.split(".", 1)
            ent = next((e for e in s["entregas"] if e["id"] == eid), None)
            if ent is None:
                raise KeyError(f"entrega desconocida {eid}")
            destino = ent["campos"]
        prev = destino.get(k, campo(None))
        nuevo = dict(prev)
        if "valor" in c:
            nuevo["valor"] = c["valor"]
        estado = c.get("estado") or ("LOCKED" if nuevo["valor"] not in (None, "", []) else "OPEN")
        if estado == "NO_APLICA" and not (c.get("motivo") or "").strip():
            raise ValueError(f"{ruta}: NO_APLICA exige motivo")
        nuevo["estado"] = estado
        nuevo["origen"] = c.get("origen", autor)
        if c.get("motivo") is not None:
            nuevo["motivo"] = c["motivo"]
        if c.get("fuente"):
            nuevo["fuente"] = c["fuente"]
        if nuevo != prev:
            destino[k] = nuevo
            tocadas.append(ruta)
    s["ambiguedades"] = ambiguedades(s)
    return s, tocadas


def valor(spec: dict, ent: dict | None, k: str):
    if ent and k in ent["campos"]:
        return ent["campos"][k]
    return spec["comunes"].get(k)


def preflight_entrega(spec: dict, ent: dict) -> dict:
    """Preflight de UNA entrega: un campo propio de la entrega manda sobre el común."""
    faltan = []
    s = {"comunes": dict(spec["comunes"], **{k: v for k, v in ent["campos"].items() if k in spec["comunes"] or k in TODOS})}
    for k in requeridos(s):
        f = ent["campos"].get(k) or spec["comunes"].get(k)
        if f is None or (f["estado"] == "OPEN" and f.get("prompt_required", True)):
            faltan.append(f"{ent['id'] if k in ent['campos'] else 'comunes'}.{k}")
    m = ent["campos"].get("modelo") or spec["comunes"]["modelo"]
    if m["estado"] != "LOCKED":
        faltan.append("comunes.modelo")
    for k, f in spec["comunes"].items():
        if f.get("tarjeta") and f["estado"] != "LOCKED":
            faltan.append(f"comunes.{k}")
    for k, f in ent["campos"].items():
        if f["estado"] == "OPEN" and f.get("prompt_required", True) and f"{ent['id']}.{k}" not in faltan:
            faltan.append(f"{ent['id']}.{k}")
    return {"estado": "FAIL" if faltan else "PASS", "faltan": faltan}


def preflight(spec: dict) -> dict:
    """Bloquea la compilación si un campo requerido por el prompt sigue OPEN."""
    faltan = []
    for k in requeridos(spec):
        f = spec["comunes"].get(k)
        if f is None or (f["estado"] == "OPEN" and f.get("prompt_required", True)):
            faltan.append(f"comunes.{k}")
    for k in ["modelo"]:
        if spec["comunes"][k]["estado"] != "LOCKED":
            faltan.append(f"comunes.{k}")
    # flujo-anclas A1: "Un campo vacío revela dirección faltante; no se genera con campos vacíos."
    for k, f in spec["comunes"].items():
        if f.get("tarjeta") and f["estado"] != "LOCKED":
            faltan.append(f"comunes.{k}")
    for e in spec["entregas"]:
        for k, f in e["campos"].items():
            if f["estado"] == "OPEN" and f.get("prompt_required", True):
                faltan.append(f"{e['id']}.{k}")
    return {"estado": "FAIL" if faltan else "PASS", "faltan": faltan}
