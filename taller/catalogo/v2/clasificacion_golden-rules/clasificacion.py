"""Clasificación de los 93 textos de skills/image/references/golden-rules.md, con los criterios del piloto de
gpt-image.md (taller/catalogo/v2/piloto_gpt-image/clasificacion.py), que se reutilizan sin cambios.

Criterio propio de este archivo:
- Alcance de modelo heredado del documento (§1.6, DEC-000023): L3 declara que estos principios valen para las dos
  familias, Nano Banana y GPT Image 2. F29 por defecto = GPT Image 2 + Nano Banana 2 + Nano Banana Pro +
  Nano Banana 2 Lite, salvo que la línea nombre un solo modelo.
- Los ejemplos que ilustran una regla del mismo encabezado son «Ejemplo» con «validar contra el ejemplo»; las filas de
  tabla «vago → específico» son regla, igual que las filas «Не пиши | Пиши» del piloto.
"""
import importlib.util
from pathlib import Path

_p = Path(__file__).resolve().parent.parent / "piloto_gpt-image" / "clasificacion.py"
_s = importlib.util.spec_from_file_location("piloto", _p)
P = importlib.util.module_from_spec(_s)
_s.loader.exec_module(P)

PASOS_PROMPT, EDICION, CT, SEL, CTRL, GPT2 = P.PASOS_PROMPT, P.EDICION, P.CT, P.SEL, P.CTRL, P.GPT2
AMBAS = ["GPT Image 2", "Nano Banana 2", "Nano Banana Pro", "Nano Banana 2 Lite"]
SLOTS_TEXTO = ["salida.slots.Scene", "salida.slots.Subject", "salida.slots.Important Details", "salida.slots.Use Case"]
REVISION = ["E5.5 edición quirúrgica", "E5.8 revisión"]


def A(id_, **k):
    k.setdefault("f29", AMBAS)
    return P.A(id_, **k)


CONCILIACIONES = {
    # Lote 1 (L1–L37)
    "INV-002238": ("estructura", "título del documento; el alcance de modelo lo fija L3 (002239)"),
    "INV-002239": ("estructura", "declara que los principios del archivo valen para Nano Banana y GPT Image 2; se hereda "
                                 "como F29 de todas las aplicaciones del documento (§1.6, DEC-000023) y no regula nada por sí"),
    "INV-002240": ("estructura", "encabezado «1. Start with a Verb»; la regla es 002241"),
    "INV-002242": ("estructura", "encabezado «2. Positive Framing»; la regla es 002243 y sus ejemplos 002244–002246"),
    "INV-002247": ("estructura", "encabezado «3. Edit, Don't Re-roll»; la regla es 002248 y sus ejemplos 002249–002251"),
    "INV-002252": ("estructura", "encabezado «4. Natural Language»; el ejemplo con la regla implícita es 002253"),
    "INV-002254": ("estructura", "encabezado «5. Be Specific»; las filas de la tabla son 002257–002260"),
    "INV-002255": ("estructura", "cabecera de tabla «Element | Vague | Specific»; las filas son 002257–002260"),
    "INV-002256": ("estructura", "separador de tabla markdown"),
}

APLICACIONES = [
    # Lote 1 (L1–L37)
    A("INV-002241", t112=["regla", "sintaxis"], objeto="campo o esquema", uso=CT, idioma="en",
      f30=["estructura y sintaxis del prompt"], accion=["agregar al prompt", "validar el prompt"],
      destino=["salida.slots.Scene", "salida.validaciones"],
      valor="la primera instrucción abre con el verbo de la operación (Create, Generate, Design, Transform, Convert, Edit), "
            "dentro del contenido del primer slot y sin prefijo antes de «Scene:» (templates §1)",
      fund="«Tell the model the primary operation… This sets the intent before details»; imperativo general del archivo"),
    A("INV-002243", t112=["regla"], objeto="campo o esquema", uso=CT, idioma="en",
      f30=["estructura y sintaxis del prompt"], accion=["validar el prompt"], destino=SLOTS_TEXTO + ["salida.validaciones"],
      valor="describir el estado deseado en positivo; las exclusiones van en Constraints, que gpt-image.md:15 (INV-002335) "
            "define como «what must NOT change/appear»",
      fund="«Describe what you WANT, not what you don't want»; la excepción de Constraints viene del contrato de GPT Image 2"),
    A("INV-002244", t61="Ejemplo", t112=["ejemplo", "sintaxis"], fuerza=["Sin fuerza normativa"], objeto="campo o esquema",
      uso=CTRL, idioma="en", f30=["estructura y sintaxis del prompt"], accion=["validar contra el ejemplo"],
      destino=["salida.validaciones"], valor="«empty street» en vez de «street with no cars»",
      fund="ilustra la regla 002243 bajo el mismo encabezado"),
    A("INV-002245", t61="Ejemplo", t112=["ejemplo", "sintaxis"], fuerza=["Sin fuerza normativa"], objeto="campo o esquema",
      uso=CTRL, idioma="en", f30=["estructura y sintaxis del prompt"], accion=["validar contra el ejemplo"],
      destino=["salida.validaciones"], valor="«clean background» en vez de «no clutter»",
      fund="ilustra la regla 002243 bajo el mismo encabezado"),
    A("INV-002246", t61="Ejemplo", t112=["ejemplo", "sintaxis"], fuerza=["Sin fuerza normativa"], objeto="campo o esquema",
      uso=CTRL, idioma="en", r={"F15": ["persona"], "F19": ["1"]}, f30=["estructura y sintaxis del prompt"],
      accion=["validar contra el ejemplo"], destino=["salida.validaciones"],
      valor="«solo portrait» en vez de «no other people»",
      fund="ilustra 002243; su contenido solo tiene sentido con una persona como sujeto («portrait», «other people»)"),
    A("INV-002248", t112=["regla"], objeto="registro de ejecución (run)", uso=CTRL, idioma="en", f02=["E5.7 crítica", "E5.8 revisión"],
      ambito=["Creación de imagen", "Orquestación y control de flujo"],
      f30=["orquestación y control de flujo", "crítica y revisión"], accion=["seleccionar estructura"],
      destino=["salida.aceptacion"],
      valor="si la imagen está correcta en un 80 % o más, pedir un cambio puntual (edición) en vez de regenerar",
      fund="encabezado «Edit, Don't Re-roll» + «Image 80% correct? Request specific change»; actúa después de generar, "
           "cuando la aceptación decide la siguiente operación (orquestacion.accion no es columna de la matriz del piloto)"),
    A("INV-002249", t61="Ejemplo", t112=["ejemplo", "sintaxis"], fuerza=["Sin fuerza normativa"], objeto="campo o esquema",
      uso=CTRL, idioma="en", r={"F10": EDICION}, f02=REVISION, f30=["estructura y sintaxis del prompt", "luz"],
      accion=["validar contra el ejemplo"], destino=["salida.validaciones"], valor="«Change lighting to sunset»",
      fund="ejemplo del cambio puntual de 002248; es una instrucción de edición"),
    A("INV-002250", t61="Ejemplo", t112=["ejemplo", "sintaxis"], fuerza=["Sin fuerza normativa"], objeto="campo o esquema",
      uso=CTRL, idioma="en", r={"F10": EDICION, "F32": ["texto corto", "texto extenso o pequeño"]}, f02=REVISION,
      f30=["estructura y sintaxis del prompt", "texto en pantalla"], accion=["validar contra el ejemplo"],
      destino=["salida.validaciones"], valor="«Make text neon blue»",
      fund="ejemplo de 002248; supone texto dentro de la imagen"),
    A("INV-002251", t61="Ejemplo", t112=["ejemplo", "sintaxis"], fuerza=["Sin fuerza normativa"], objeto="campo o esquema",
      uso=CTRL, idioma="en", r={"F10": EDICION, "F04": ["infografía o diagrama", "slide o presentación"]}, f02=REVISION,
      f30=["estructura y sintaxis del prompt", "composición"], accion=["validar contra el ejemplo"],
      destino=["salida.validaciones"], valor="«Move chart to right third»",
      fund="ejemplo de 002248; «chart» supone una pieza con gráfico: infografía o slide"),
    A("INV-002253", t61="Ejemplo", t112=["ejemplo", "sintaxis"], fuerza=["Sin fuerza normativa"], objeto="campo o esquema",
      uso=CTRL, idioma="en", f30=["estructura y sintaxis del prompt"], accion=["validar contra el ejemplo"],
      destino=["salida.validaciones"],
      valor="malo: «Cool car, neon, city, night, 8k» · bueno: oraciones con relaciones visuales («A cinematic wide shot of a "
            "futuristic sports car speeding through a rainy Tokyo street at night. Neon signs reflect off wet pavement…»)",
      fund="único contenido bajo «4. Natural Language»; la regla la enuncia el par malo/bueno"),
    A("INV-002257", t112=["regla", "sintaxis"], fuerza=["Prohibición", "Obligación"], objeto="campo o esquema", uso=CT,
      idioma="en", f30=["estructura y sintaxis del prompt"], accion=["excluir del prompt", "agregar al prompt", "validar el prompt"],
      destino=["salida.slots.Subject", "salida.validaciones"],
      valor="sujeto genérico («a woman») → sujeto con edad, aspecto y vestuario concretos",
      fund="fila «Subject» de la tabla «Vague | Specific»; el ejemplo literal cita una marca («Chanel-style»), que no se "
           "copia al prompt por gpt-image.md:38 (INV-002345)"),
    A("INV-002258", t112=["regla", "sintaxis"], fuerza=["Prohibición", "Obligación"], objeto="campo o esquema", uso=CT,
      idioma="en", f30=["estructura y sintaxis del prompt", "materialidad y superficie"],
      accion=["excluir del prompt", "agregar al prompt", "validar el prompt"],
      destino=["salida.slots.Important Details", "salida.validaciones"],
      valor="material vago («shiny») → material y acabado («brushed steel with matte finish»)",
      fund="fila «Material» de la tabla «Vague | Specific»"),
    A("INV-002259", t112=["regla", "sintaxis"], fuerza=["Prohibición", "Obligación"], objeto="campo o esquema", uso=CT,
      idioma="en", f30=["estructura y sintaxis del prompt", "color, grade y textura"],
      accion=["excluir del prompt", "agregar al prompt", "validar el prompt"],
      destino=["salida.slots.Important Details", "salida.validaciones"],
      valor="color vago («dark green») → hex y nombre («#0d3d2d deep emerald»)",
      fund="fila «Color» de la tabla «Vague | Specific»"),
    A("INV-002260", t112=["regla", "sintaxis"], fuerza=["Prohibición", "Obligación"], objeto="campo o esquema", uso=CT,
      idioma="en", f30=["estructura y sintaxis del prompt", "composición"],
      accion=["excluir del prompt", "agregar al prompt", "validar el prompt"],
      destino=["salida.slots.Subject", "salida.slots.Important Details", "salida.validaciones"],
      valor="posición vaga («on the right») → posición en el cuadro («right third, bleeding off edge»)",
      fund="fila «Position» de la tabla «Vague | Specific»"),
]

CONSULTAS = {}
