"""Roles semánticos del proceso, sus esquemas de respuesta y las comprobaciones deterministas.

Cada rol recibe solo lo que necesita y devuelve JSON. Los validadores rechazan respuestas que
omiten campos, inventan rutas o citan texto que no existe; una respuesta rechazada nunca avanza
el proceso.
"""
import json
import re
import unicodedata

from llm import RespuestaInvalida
from recursos import SLOTS_GEN

ESTADOS_CAMPO = ["proporcionado", "inferido", "propuesta", "falta", "condicion_inactiva"]
ESTADOS_REVISION = ["PASS", "FAIL", "UNCERTAIN"]
BLOQUES = SLOTS_GEN + ["parametros"]

# Prohibiciones literales que se comprueban por código además de la revisión semántica.
PALABRAS_USUARIO = [r"photo[\s-]?realistic", r"foto[\s-]?r?realista"]          # USER::ERIC-DELEGATION-TERMS
PALABRAS_ANTI_SLOP = ["stunning", "incredible", "epic", "gorgeous", "masterpiece"]  # INV-002343


def normalizar(texto):
    texto = unicodedata.normalize("NFKC", str(texto)).casefold()
    return re.sub(r"\s+", " ", texto).strip()


def texto_valor(valor):
    if valor is None:
        return ""
    if isinstance(valor, str):
        return valor
    return json.dumps(valor, ensure_ascii=False)


def vacio(valor):
    return valor is None or valor == "" or valor == [] or valor == {}


def _exigir(cond, mensaje):
    if not cond:
        raise RespuestaInvalida(mensaje)


# ---------------------------------------------------------------- 2. Desarrollo del brief

SISTEMA_DESARROLLO = """Eres el desarrollador del brief creativo y técnico de una imagen para GPT Image 2.
Tu trabajo NO es transcribir: es desarrollar la idea del usuario hasta un brief fotográfico completo,
conservando su intención y sus palabras.

Recibes: el texto original íntegro del usuario (no se modifica), aportes posteriores del usuario,
decisiones ya tomadas por él, la lista COMPLETA de campos del template T-BRIEF-IMG con su condición
literal ("Cuándo se exige"), el contrato de la operación y las directivas vigentes del usuario.

Antes de proponer o preguntar cualquier campo, búscalo en el original y en los aportes: si el usuario ya
lo dijo, con esas palabras o con otras equivalentes, el campo es "proporcionado" con su cita. Nunca se
propone ni se pregunta algo que el usuario ya escribió; preguntarlo otra vez es un error grave.

Devuelve cada campo de la lista exactamente una vez, en el mismo orden, con uno de estos estados:
- "proporcionado": el dato está explícito en el original o en un aporte. "cita" debe copiar el fragmento
  carácter por carácter, con sus faltas de ortografía tal cual. El valor se redacta limpio en español.
- "inferido": se deduce sin creatividad del original o de los aportes (por ejemplo, sin referencias
  adjuntas la operación es génesis). "fundamento" explica la deducción verificable.
- "propuesta": desarrollo creativo o técnico necesario para que la imagen funcione y que el usuario
  no dio. Es obligatorio proponer cuando la pieza es fotográfica: plano, ángulo, altura y efecto óptico de
  cámara, intención de lente, fuente, dirección, dureza, distribución, contraste y especulares de la luz,
  paleta, grade, materiales, texturas, acabado, composición y planos. "fundamento" explica por qué esa
  propuesta sirve a la intención del usuario; "alternativas" puede ofrecer otras opciones concretas.
  Una propuesta nunca se presenta como instrucción del usuario.
- "falta": solo el usuario puede darlo, cambia la imagen y no hay base para proponer (o hay un conflicto).
  "pregunta" debe ser concreta y contestable. Úsalo lo menos posible: si existe una opción razonable, es
  "propuesta", no "falta".
- "condicion_inactiva": la condición literal del campo no se cumple en este caso. "fundamento" cita la
  condición y explica por qué no se activa. Prohibido para campos con condición "siempre" y para los
  required_fields del contrato.

Reglas de redacción del brief:
- Respeta las formulaciones del usuario: no sustituyas sus términos ("fotografía editorial deportiva",
  apodos, rasgos) por otros sin fundamento. Si un término es ambiguo, conserva el literal y pregunta.
- Valores concretos y observables. Nunca elogios vagos (stunning, epic, masterpiece, etc.) ni los términos
  prohibidos por las directivas del usuario.
- No inventes referencias, archivos ni identidades. Si el usuario anuncia una imagen que no está adjunta,
  regístralo como falta o conflicto; no cambies la operación sin decisión del usuario.
- En los campos "items[]" el valor es una lista alineada con los sujetos, en orden S1, S2, ...
- entrada.selecciones_taxonomicas: lista de valores de faceta que describen el caso (por ejemplo
  "F10: génesis", "F15: persona"). No es la selección de reglas, que ocurre después.
- entrada.restricciones: todas las prohibiciones o invariantes que impuso el usuario; [] solo si no impuso ninguna.
- Si hay decisiones del usuario sobre un campo, respétalas literalmente.

Brevedad (el tiempo de respuesta depende de cuánto escribes):
- Omite las claves vacías: no escribas "cita": "", "pregunta": "", "alternativas": [] ni "valor": null.
- condicion_inactiva: solo {"path", "estado", "fundamento"}, con el fundamento en 12 palabras o menos.
- fundamento de inferido o propuesta: 25 palabras o menos. cita: el fragmento literal mínimo que prueba el dato.
- alternativas: como máximo 2, solo en propuestas.

Si la entrada trae "rutas_a_desarrollar", el brief se desarrolla por partes: devuelve SOLO esos campos, en
ese orden, y mantén coherencia con "campos_ya_desarrollados" (las partes anteriores, que no repites). En
las partes que no son la última, "resumen_creativo" puede ir vacío; en la última, resume el brief completo.

Devuelve JSON con esta forma:
{"campos": [{"path": "...", "estado": "...", "valor": <texto, número, lista u objeto, o null>,
  "cita": "...", "fundamento": "...", "pregunta": "...", "alternativas": ["..."]}],
 "resumen_creativo": "párrafo en español que explica la propuesta fotográfica en conjunto",
 "conflictos": ["conflicto detectado entre datos del usuario, si existe"]}"""


def carga_desarrollo(rec, original, aportes, decisiones, rutas=None, previos=None, parte=None):
    carga = _carga_desarrollo(rec, original, aportes, decisiones)
    if rutas is not None:
        carga.update({"parte": parte, "rutas_a_desarrollar": rutas, "campos_ya_desarrollados": previos or []})
    return carga


def _carga_desarrollo(rec, original, aportes, decisiones):
    return {
        "texto_original": original,
        "aportes_usuario": aportes,
        "decisiones_usuario": decisiones,
        "modelo": "GPT Image 2",
        "campos_template": [{"path": c["path"], "tipo": c["type"], "condicion": c["condition"], "facetas": c["facets"]} for c in rec.campos],
        "anotacion_template": rec.anotacion_brief,
        "contrato_operacion_genesis": rec.contrato_genesis,
        "directivas_usuario": rec.reglas_directivas(),
    }


def validar_desarrollo(rec, original, aportes, rutas_esperadas=None, exigir_resumen=True):
    fuentes_cita = normalizar(original + "\n" + "\n".join(a["texto"] for a in aportes))
    requeridos = set(rec.contrato_genesis["required_fields"])
    esperadas = rutas_esperadas if rutas_esperadas is not None else rec.rutas

    def validar(valor):
        _exigir(isinstance(valor, dict) and isinstance(valor.get("campos"), list), "Falta la lista 'campos'.")
        rutas = [c.get("path") for c in valor["campos"]]
        _exigir(rutas == esperadas, "Los campos deben ser exactamente los pedidos, una vez y en orden. "
                f"Faltan: {sorted(set(esperadas) - set(rutas))[:8]}; sobran: {sorted(set(rutas) - set(esperadas))[:8]}.")
        for c in valor["campos"]:
            ruta, estado = c["path"], c.get("estado")
            _exigir(estado in ESTADOS_CAMPO, f"{ruta}: estado inválido {estado!r}.")
            condicion = rec.campo_por_ruta[ruta]["condition"]
            if estado == "proporcionado":
                _exigir(c.get("cita"), f"{ruta}: un dato proporcionado exige cita literal.")
                _exigir(normalizar(c["cita"]) in fuentes_cita, f"{ruta}: la cita no aparece literalmente en el original ni en los aportes.")
                _exigir(not vacio(c.get("valor")), f"{ruta}: un dato proporcionado no puede estar vacío.")
            elif estado in ("inferido", "propuesta"):
                _exigir(c.get("fundamento"), f"{ruta}: {estado} exige fundamento.")
                _exigir(not vacio(c.get("valor")), f"{ruta}: {estado} exige valor.")
            elif estado == "falta":
                _exigir(c.get("pregunta"), f"{ruta}: un dato faltante exige una pregunta concreta.")
            elif estado == "condicion_inactiva":
                _exigir(condicion != "siempre" and ruta not in requeridos,
                        f"{ruta}: condición '{condicion}' no admite condicion_inactiva.")
                _exigir(c.get("fundamento"), f"{ruta}: condicion_inactiva exige fundamento con la condición.")
        if exigir_resumen:
            _exigir(isinstance(valor.get("resumen_creativo"), str) and valor["resumen_creativo"].strip(), "Falta resumen_creativo.")
    return validar


# ---------------------------------------------------------------- Corrección de los textos del usuario

SISTEMA_ORTOGRAFIA = """Corrige la ortografía, los acentos, la puntuación, las mayúsculas y la gramática del texto
del usuario, en su idioma. Corrige también letras cambiadas, sobrantes o faltantes por error de tecleo.
No cambies el sentido, no resumas, no agregues ni quites información, no cambies sus términos técnicos,
nombres propios, apodos, cifras ni el registro. Si una palabra es ambigua, deja la más probable por contexto.
Devuelve JSON: {"texto": "el texto corregido completo"}."""


def validar_ortografia(valor):
    _exigir(isinstance(valor, dict) and isinstance(valor.get("texto"), str) and valor["texto"].strip(),
            "Falta el texto corregido.")


# ---------------------------------------------------------------- 4. Corrector del brief

SISTEMA_CORRECTOR_BRIEF = """Eres el corrector independiente del brief. No redactas prompts ni reescribes el brief.
Revisa CADA campo contra el texto original, los aportes y decisiones del usuario, la condición literal del
template y el contrato de la operación, pero reporta SOLO las excepciones: un campo que no aparece en tu
respuesta queda aprobado. No escribas nada sobre los campos correctos.

FAIL (devuelve el brief al usuario) solo por defectos objetivos: un dato marcado como proporcionado no
corresponde a su cita o la deforma; una inferencia no tiene base; se perdió o contradijo algo que el usuario
pidió; un campo requerido quedó vacío; una condición se evaluó mal (por ejemplo, una pieza fotográfica sin
cámara o sin luz desarrolladas); hay contradicción entre campos (cantidad de sujetos, posiciones, operación
frente a referencias, o una imposibilidad física que se deduce solo de lo que dice el propio brief);
aparece vocabulario vago o prohibido por el usuario; una
propuesta se presenta como dato del usuario.

Las decisiones del usuario (origen usuario, propuesta_aceptada, propuesta_rechazada,
vacio_explicado_por_usuario) son finales y mandan sobre el original: no las reviertas. Que un asunto sea
decisión exclusiva del usuario NUNCA es motivo de FAIL ni de devolución: si el usuario ya decidió, el campo
está aprobado. Solo marca FAIL un campo decidido si su valor crea un defecto objetivo de la lista anterior.
UNCERTAIN es una nota para el usuario que NO devuelve el brief: úsala solo si queda una ambigüedad real
que afecta a la imagen, con una pregunta concreta.
Tu conocimiento general del mundo (cómo funciona un aparato, un deporte, un material) no está en el brief ni
en las reglas y puede estar equivocado o no aplicar al caso: si una decisión del usuario choca con ese
conocimiento, nunca es FAIL; es UNCERTAIN, explicando en qué te basas para que el usuario decida.

Sé breve: cada comentario en 40 palabras o menos, observaciones_generales en 60 o menos.
Devuelve JSON: {"observaciones": [{"path": "...", "estado": "FAIL|UNCERTAIN", "comentario": "...",
"pregunta": "..."}], "observaciones_generales": "..."}. Lista vacía si todo el brief es correcto."""


def _compacto(campo):
    return {k: v for k, v in campo.items() if v not in ("", None, [], {})}


def carga_corrector(rec, original, aportes, brief_final):
    return {"texto_original": original, "aportes_usuario": aportes, "brief": [_compacto(c) for c in brief_final],
            "contrato_operacion_genesis": rec.contrato_genesis, "directivas_usuario": rec.reglas_directivas()}


def validar_corrector(rutas):
    """Respuesta por excepción: solo campos FAIL o UNCERTAIN; los ausentes quedan aprobados."""
    validas = set(rutas)

    def validar(valor):
        _exigir(isinstance(valor, dict) and isinstance(valor.get("observaciones"), list), "Falta la lista 'observaciones'.")
        vistos = set()
        for r in valor["observaciones"]:
            _exigir(isinstance(r, dict) and r.get("path") in validas, f"Ruta inexistente en el brief: {r.get('path') if isinstance(r, dict) else r}.")
            _exigir(r["path"] not in vistos, f"{r['path']}: observación duplicada.")
            vistos.add(r["path"])
            _exigir(r.get("estado") in ("FAIL", "UNCERTAIN"), f"{r['path']}: estado debe ser FAIL o UNCERTAIN.")
            _exigir(r.get("comentario"), f"{r['path']}: falta comentario.")
            if r["estado"] == "UNCERTAIN":
                _exigir(r.get("pregunta"), f"{r['path']}: UNCERTAIN exige pregunta.")
    return validar


def validar_registros(ids_esperados, clave="path"):
    def validar(valor):
        _exigir(isinstance(valor, dict) and isinstance(valor.get("registros"), list), "Falta la lista 'registros'.")
        ids = [r.get(clave) for r in valor["registros"]]
        _exigir(sorted(ids) == sorted(ids_esperados) and len(set(ids)) == len(ids),
                f"Cobertura incompleta. Faltan: {sorted(set(ids_esperados) - set(ids))[:8]}; sobran: {sorted(set(ids) - set(ids_esperados))[:8]}.")
        for r in valor["registros"]:
            _exigir(r.get("estado") in ESTADOS_REVISION, f"{r.get(clave)}: estado inválido.")
            _exigir(r.get("comentario") or r.get("explicacion"), f"{r.get(clave)}: falta comentario.")
            if r["estado"] == "UNCERTAIN":
                _exigir(r.get("pregunta"), f"{r.get(clave)}: UNCERTAIN exige pregunta.")
    return validar


# ---------------------------------------------------------------- 5. Selección de reglas específicas

SISTEMA_SELECTOR = """Eres el selector de reglas ESPECÍFICAS del caso. El brief ya fue validado por el usuario y el corrector.
Evalúa TODAS las unidades candidatas que recibes. Para cada una decide:
- "seleccionada": la regla aplica a este caso. Indica "bloque" (Scene, Subject, Important Details, Use Case,
  Constraints o parametros), "campo_brief" (ruta exacta del brief que la activa), "cita_brief" (fragmento
  copiado literalmente del valor de ese campo) y "razon" (por qué aplica y qué efecto debe tener en el prompt).
- "excluida": no aplica; "razon" dice concretamente qué condición de la regla no se cumple en este caso.
- "duda": no puedes decidir sin el usuario; "pregunta" concreta.
Las 12 reglas universales ya están aparte: no las selecciones de nuevo. No traigas reglas de otro medio,
modelo u operación (video, Nano Banana, edición) salvo que el brief lo active. La expectativa de una o dos
reglas por bloque solo sirve para evaluar los filtros: no fuerces ese número, no trunques, no fusiones.
Devuelve JSON: {"decisiones": [{"id": "INV-...", "decision": "seleccionada|excluida|duda", "bloque": "...",
"campo_brief": "...", "cita_brief": "...", "razon": "...", "pregunta": "..."}]}"""


def universales_resumidas(rec):
    """Texto de las 12 universales para que selector y revisor comprueben qué cubren de verdad."""
    return [{"regla_id": u["regla_id"], "intencion": u["intencion"],
             "fuentes": [f"{f['id']}: {f['texto']}" for f in u["fuentes"]]} for u in rec.universales]


def carga_selector(rec, brief_validado, unidades, retro=None):
    return {"brief_validado": brief_validado, "modelo": "GPT Image 2", "operacion": "genesis",
            "reglas_universales_ya_aplicadas": universales_resumidas(rec),
            "bloques": BLOQUES, "candidatas": [rec.unidad_compacta(u) for u in unidades],
            "retroalimentacion_revisor": retro or []}


def validar_selector(ids, brief_validado):
    valores = {c["path"]: normalizar(texto_valor(c["valor"])) for c in brief_validado}

    def validar(valor):
        _exigir(isinstance(valor, dict) and isinstance(valor.get("decisiones"), list), "Falta 'decisiones'.")
        vistos = [d.get("id") for d in valor["decisiones"]]
        _exigir(sorted(vistos) == sorted(ids) and len(set(vistos)) == len(vistos),
                f"El selector omitió o repitió candidatas: faltan {sorted(set(ids) - set(vistos))[:8]}.")
        for d in valor["decisiones"]:
            _exigir(d.get("decision") in ("seleccionada", "excluida", "duda"), f"{d['id']}: decisión inválida.")
            if d["decision"] == "seleccionada":
                _exigir(d.get("bloque") in BLOQUES, f"{d['id']}: bloque inválido {d.get('bloque')!r}.")
                _exigir(d.get("campo_brief") in valores, f"{d['id']}: campo_brief inexistente {d.get('campo_brief')!r}.")
                _exigir(d.get("cita_brief") and normalizar(d["cita_brief"]) in valores[d["campo_brief"]],
                        f"{d['id']}: cita_brief no aparece en el valor de {d['campo_brief']}.")
                _exigir(d.get("razon"), f"{d['id']}: falta razón.")
            elif d["decision"] == "excluida":
                _exigir(d.get("razon"), f"{d['id']}: una exclusión exige razón concreta.")
            else:
                _exigir(d.get("pregunta"), f"{d['id']}: una duda exige pregunta.")
    return validar


SISTEMA_REVISOR_SELECCION = """Eres el revisor independiente de la selección de reglas. No seleccionas ni redactas.
Revisa cada decisión del lote, también las exclusiones, contra el brief validado y el texto literal de la regla.
Busca reglas necesarias que se excluyeron y reglas seleccionadas sin activación real en el brief.
FAIL exige un comentario específico de qué está mal; UNCERTAIN una pregunta concreta para el usuario.
No apruebes por cumplir un conteo. Devuelve JSON: {"registros": [{"id": "INV-...", "estado": "PASS|FAIL|UNCERTAIN",
"comentario": "...", "pregunta": "..."}]} con todas las decisiones del lote."""


def carga_revisor_seleccion(rec, brief_validado, unidades, decisiones, conteos):
    return {"brief_validado": brief_validado, "reglas_universales_ya_aplicadas": universales_resumidas(rec),
            "candidatas": [rec.unidad_compacta(u) for u in unidades],
            "decisiones": decisiones, "conteo_por_bloque_total": conteos}


# ---------------------------------------------------------------- 7. Redacción del prompt

SISTEMA_REDACTOR = """Eres el redactor del prompt para GPT Image 2. No modificas el brief.
Escribe en INGLÉS solo el cuerpo visual con los cinco rótulos exactos y en este orden:
Scene, Subject, Important Details, Use Case, Constraints. La primera instrucción operativa va dentro de Scene
y empieza con un verbo de operación (por ejemplo Create). Nada antes de Scene.
Usa únicamente el brief validado, las instrucciones de llenado por bloque, las 12 reglas universales, las
directivas del usuario y las reglas específicas seleccionadas, que llegan con su texto canónico. Aplícalas
todas; no inventes reglas ni datos. Lenguaje natural concreto: hechos visuales, materiales, luz, color,
posición. Sin elogios vagos, sin términos prohibidos por el usuario, sin marcadores {{ }} ni puntos suspensivos.
Constraints contiene prohibiciones e invariantes efectivas, no datos administrativos del brief.
Si hay comentarios del corrector o decisiones del usuario, corrígelos todos.
Los parámetros quality y tamano van aparte y ya vienen fijados: cópialos.
Devuelve JSON: {"slots": {"Scene": "...", "Subject": "...", "Important Details": "...", "Use Case": "...",
"Constraints": "..."}, "parametros": {"quality": "...", "tamano": "..."},
"aplicacion": [{"regla_id": "...", "slot": "...", "como": "..."}], "notas": ["..."]}
Cada "como" en 20 palabras o menos."""


def carga_redactor(rec, brief_validado, especificas, parametros, previo=None, observaciones=None, decisiones=None, comentario=None):
    return {"brief_validado": brief_validado, "adapter": rec.llenado["template"],
            "instrucciones_llenado": rec.instrucciones_slots(),
            "reglas_universales": rec.universales, "pack_operacion": rec.pack_gen(),
            "directivas_usuario": rec.reglas_directivas(), "reglas_especificas": especificas,
            "parametros_fijados": parametros, "prompt_anterior": previo,
            "observaciones_corrector": observaciones or [], "decisiones_usuario": decisiones or [],
            "comentario_usuario": comentario or ""}


def validar_redactor(parametros):
    def validar(valor):
        _exigir(isinstance(valor, dict) and isinstance(valor.get("slots"), dict), "Falta 'slots'.")
        _exigir(list(valor["slots"].keys()) == SLOTS_GEN or sorted(valor["slots"].keys()) == sorted(SLOTS_GEN),
                f"Los rótulos deben ser exactamente {SLOTS_GEN}.")
        for s in SLOTS_GEN:
            _exigir(isinstance(valor["slots"].get(s), str) and valor["slots"][s].strip(), f"El bloque {s} está vacío.")
        _exigir(isinstance(valor.get("parametros"), dict), "Faltan parámetros.")
    return validar


def cuerpo_prompt(slots):
    return "\n".join(f"{s}: {slots[s].strip()}" for s in SLOTS_GEN)


# ---------------------------------------------------------------- 8. Corrector semántico del prompt

SISTEMA_REVISOR_PROMPT = """Eres el corrector semántico independiente del prompt. No redactas.
Comprueba el cumplimiento REAL de cada regla de la lista sobre el cuerpo del prompt y los parámetros.
Que una regla se haya entregado al redactor no prueba nada: busca la evidencia en el texto.
Para cada regla devuelve:
- PASS: se cumple; "cita" copia el fragmento del prompt que lo demuestra (o explica el alcance revisado si la
  regla prohíbe algo y no aparece).
- FAIL: violación clara; "cita" copia literalmente el fragmento que viola y "explicacion" dice qué corregir.
- UNCERTAIN: ambigüedad real que debe decidir el usuario; "cita" copia el fragmento exacto, "explicacion"
  describe el posible problema y "pregunta" la decisión concreta.
Compara también el prompt con el brief validado: lo que el brief exige debe estar, sin contradicciones ni
datos inventados. Considera las notas contextuales del usuario como aclaraciones vinculadas a su regla.
"entrega" es el paquete que la app exporta junto al prompt (encabezado de modelo, quality, tamaño e
inferencias del brief separadas del texto visual): evalúa con él las reglas de entrega. Para un problema
en la entrega, la "cita" copia literalmente el fragmento de "entrega"; para uno del texto, del prompt.
Sé breve en los PASS: "cita" y "explicacion" de 20 palabras o menos cada una (la respuesta debe caber en el
límite de tiempo por llamada); el detalle completo es para FAIL y UNCERTAIN.
Devuelve JSON: {"registros": [{"regla_id": "...", "estado": "PASS|FAIL|UNCERTAIN", "slot": "...",
"cita": "...", "explicacion": "...", "pregunta": "..."}]} con todas las reglas, una vez cada una."""


def reglas_para_revision(rec, especificas, notas):
    reglas = []
    for u in rec.universales:
        reglas.append({"regla_id": u["regla_id"], "tipo": "universal", "literal": u["fuentes"],
                       "intencion": u["intencion"], "criterio_falla": u["criterio_falla"],
                       "criterio_duda": u["criterio_duda"], "notas": u["notas"]})
    for c in rec.pack_gen()["checks"]:
        reglas.append({"regla_id": c["regla_id"], "tipo": "contrato_operacion", "literal": c["texto"]})
    for d in rec.reglas_directivas():
        reglas.append({"regla_id": d["regla_id"], "tipo": "directiva_usuario", "literal": d["literal"],
                       "interpretacion": d["interpretacion"]})
    for s in rec.instrucciones_slots():
        reglas.append({"regla_id": s["id"], "tipo": "instruccion_llenado", "literal": s["instruccion"],
                       "campos_brief": s["campos_brief"]})
    for e in especificas:
        reglas.append({"regla_id": e["regla_id"], "tipo": "especifica", "literal": e["literal"],
                       "bloque": e["bloque"], "activacion": e["activacion"], "razon": e["razon"]})
    for r in reglas:
        r["notas_contextuales"] = [n for n in notas if n["regla_id"] == r["regla_id"]]
    return reglas


def paquete_entrega(parametros, brief_validado, notas_redactor=None):
    """Lo que la app exporta junto al cuerpo del prompt; el revisor evalúa las reglas de entrega con esto."""
    inferencias = [f"{c['path']}: {json.dumps(c['valor'], ensure_ascii=False)} ({c['origen']})"
                   for c in brief_validado if c.get("origen") in ("inferido", "propuesta_aceptada")]
    return {"model": "Model: GPT Image 2", "quality": f"Quality: {parametros.get('quality')}",
            "size": f"Size / Ratio: {parametros.get('tamano')}", "inferencias_y_supuestos": inferencias,
            "notas_del_redactor": list(notas_redactor or [])}


def validar_revisor_prompt(ids, cuerpo, entrega=None):
    base = validar_registros(ids, clave="regla_id")
    fuentes = [normalizar(cuerpo), normalizar(json.dumps(entrega or {}, ensure_ascii=False))]

    def validar(valor):
        base(valor)
        for r in valor["registros"]:
            if r["estado"] in ("FAIL", "UNCERTAIN"):
                cita = normalizar(r.get("cita") or "")
                _exigir(cita and any(cita in f for f in fuentes),
                        f"{r['regla_id']}: la cita de un {r['estado']} debe copiar un fragmento literal del prompt o de la entrega.")
    return validar


def comprobaciones_deterministas(slots, parametros, brief_validado):
    """Controles por código: no sustituyen al corrector semántico, lo respaldan."""
    registros = []

    def falla(regla, cita, explicacion, slot=""):
        registros.append({"regla_id": regla, "estado": "FAIL", "slot": slot, "cita": cita,
                          "explicacion": explicacion, "pregunta": "", "origen": "determinista"})

    for s in SLOTS_GEN:
        texto = slots.get(s, "")
        if not texto.strip():
            falla("PACK::GPT2-GEN::1", s, f"El bloque {s} está vacío.", s)
        if re.search(r"\{\{|\}\}|\[[^\]]*\]|\.\.\.|…", texto):
            frag = re.search(r"\{\{|\}\}|\[[^\]]*\]|\.\.\.|…", texto).group(0)
            falla("U-DELIVERY-SEPARATION", frag, "El prompt conserva marcadores, corchetes o puntos suspensivos.", s)
        for patron in PALABRAS_USUARIO:
            m = re.search(patron, texto, re.I)
            if m:
                falla("USER::ERIC-DELEGATION-TERMS", m.group(0), "Término prohibido por el usuario.", s)
        sin_comillas = re.sub(r'"[^"]*"', "", texto)
        for palabra in PALABRAS_ANTI_SLOP:
            m = re.search(r"\b" + palabra + r"\b", sin_comillas, re.I)
            if m:
                falla("U-ANTI-SLOP", m.group(0), f"'{m.group(0)}' es un elogio vago listado en INV-002343.", s)
    if parametros.get("quality") not in ("low", "medium", "high"):
        falla("U-QUALITY-ENVELOPE", str(parametros.get("quality")), "quality debe ser low, medium o high.", "parametros")
    ratio = next((c["valor"] for c in brief_validado if c["path"] == "entrada.formato.ratio"), None)
    tamano = str(parametros.get("tamano", ""))
    m = re.fullmatch(r"\s*(\d+)\s*[x×]\s*(\d+)\s*", tamano)
    if m:
        w, h = int(m.group(1)), int(m.group(2))
        if not (w < 3840 and h < 3840 and w % 16 == 0 and h % 16 == 0 and max(w, h) / min(w, h) <= 3 and 655360 <= w * h <= 8294400):
            falla("U-TECHNICAL-ENVELOPE", tamano, "Las dimensiones violan los límites documentales de GPT Image 2.", "parametros")
    elif ratio and normalizar(tamano) != normalizar(ratio):
        falla("U-TECHNICAL-ENVELOPE", tamano, f"El tamaño no coincide con el ratio del brief ({ratio}).", "parametros")
    return registros
