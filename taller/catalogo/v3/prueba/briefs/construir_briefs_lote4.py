"""construir_briefs_lote4.py: tarea 3, lote 4 (PLAN_FINAL_PRUEBA.md §5). Entradas E5 y E6, sus ediciones K17 y K18, y
la transferencia de estilo K26.

    python3 -I taller/catalogo/v3/prueba/briefs/construir_briefs_lote4.py

E5 y E6 son entradas, no casos (PLAN §4, tabla de entradas): sus prompts los escribe el armador como génesis y su QA solo
comprueba que sirven de entrada. Las dos son una persona sin referencias, así que llevan brief de `armar.py`
(CLAUDE.md). Sus facetas no están en la lista aprobada: van como propuesta del sistema (origen `INFERENCIA_PROPUESTA`
en el catálogo e `inferencia_para_aprobacion` en el contrato). Se aprueban por el sha256 del brief.

K17 y K18 son ediciones GPT2-EDIT de E5 y E6, como las del lote 3. K26 es transferencia de estilo (T-STYLE, GPT2-GEN):
el contenido de K05 con el estilo de K02, nombrando las propiedades visuales concretas del referente
(`gpt-image.md:113`, INV-002390) y cada imagen con su rol (INV-002386–002388). No es edición, así que activa el módulo
fotografía (PLAN §5, tarea 3). Las tres usan imágenes que aún no existen y se aprueban por el sha256 del contenido.
"""
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import construir_briefs as cb  # noqa: E402
from construir_briefs_lote2 import construir  # noqa: E402

E_PLAN = {e: dict(cb.PLAN["K01"], id=e, descripcion=desc, F04="editorial",
                  etiqueta_facetas=f"propuesta del sistema: {e} es entrada de {caso}, no caso (PLAN §4)")
          for e, desc, caso in (("E5", "foto en blanco y negro de una persona", "K17"),
                                ("E6", "foto antigua dañada de una persona", "K18"))}
E_COMUN = dict(lista_aprobada=False, origen_facetas="INFERENCIA_PROPUESTA", ratio="4:5", px=(1024, 1280),
               representacion=["fotorrealista"])
FUENTE_E = ("propuesta del sistema para la entrada {} (PLAN §4, tabla de entradas: «{}»; génesis escrita por el "
            "armador)")
SIN_DERIVA = ["sin objetos nuevos fuera del cambio", "sin rediseño", "sin deriva de color, contraste ni encuadre"]


def edicion(entrada, brief, pieza, cambio, preservar, restricciones):
    d = LOTE_4[entrada]
    return dict(brief=brief, paso="E5.5", plantilla_id="T-EDIT", adaptador="GPT2-EDIT", ratio=d["ratio"], px=d["px"],
                pieza=pieza, edicion=dict(cambio=cambio, preservar=preservar), restricciones=restricciones,
                requisitos_base=("entrada.edicion.cambio", "entrada.edicion.preservar"),
                motivo_requisitos="campo exigido por T-EDIT",
                motivo_ref="T-EDIT exige la imagen a editar con su sha256; la imagen aún no existe y se aprueba de "
                           "nuevo cuando exista (PLAN §5, tarea 3)",
                referencias=[dict(indice=1, entrada=entrada, medio="imagen", rol="imagen a editar",
                                  preservar=preservar)])


LOTE_4 = {
 "E5": dict(E_COMUN, fuente_facetas=FUENTE_E.format("E5", "foto en blanco y negro de una persona"),
   brief="Entrada de K17 (colorizar): retrato de estudio en blanco y negro de los años cincuenta de una persona "
         "inventada (no real). Hombre de unos 30 años, cabeza y hombros, traje oscuro y corbata, luz dura de estudio. "
         "Su QA solo comprueba que es blanco y negro y sirve de entrada.",
   pieza=("editorial", "retrato de época en blanco y negro", "entrada de K17 (colorizar)"),
   sujetos=[dict(id="hombre", clase="persona", descripcion="hombre de unos 30 años de los años cincuenta", edad=30,
                 genero="hombre", rasgos=["nariz algo desviada", "hoyuelo en el mentón", "lunar pequeño en la mejilla "
                                          "izquierda", "cara ovalada"],
                 cabello="oscuro y ondulado, peinado hacia atrás con brillantina",
                 vestuario="saco de lana oscuro, camisa blanca y corbata angosta estampada",
                 expresion="tranquila, boca cerrada", posicion="centrado, cuerpo girado tres cuartos, mirada junto a "
                                                              "la lente")],
   escena=dict(espacio="interior", entorno="estudio fotográfico de los años cincuenta con fondo pintado gris moteado"),
   camara=dict(plano="CU close-up", angulo="eye-level", efecto_optico="profundidad de campo corta",
               lente_intencion="85mm feel"),
   luz=dict(fuente="una luz dura de estudio", direccion="desde arriba a la izquierda de cámara",
            dureza="dura", distribucion="sombra en lazo bajo la nariz, fondo con luz suave", contraste="alto"),
   rostro=dict(ocupacion=0.35, detalles=["poros visibles", "grano de película"]),
   restricciones=["en blanco y negro, sin color", "sin texto ni marcas de agua", "una sola persona"],
   estilo=["blanco y negro", "anclado en época, cultura o autor"],
   armar=dict(id="E5", ratio="4:5", pronombre="him", rostro_menor_20=False,
              escena="in black and white, taken in a 1950s photo studio against a mottled grey painted backdrop "
                     "#8A8A86.",
              elementos=["hombre", "fondo pintado"],
              sujeto="A man of about 30, head and shoulders (close-up), body turned three-quarters to camera, looking "
                     "just past the lens with a calm closed-mouth expression; an oval face with a slightly bent nose, "
                     "a cleft chin and a small mole on the left cheek, dark wavy hair combed back with pomade, a dark "
                     "wool suit jacket, a white shirt and a narrow patterned tie.",
              luz="One hard studio light from above camera left casts a small loop shadow under the nose and models "
                  "the cheekbones; a soft light grazes the backdrop behind him.",
              microdetalle="Fine film grain across the frame; pomade sheen on the hair; the wool weave and the tie "
                           "pattern read in grey tones.",
              camara="Eye-level camera, 85mm feel, shallow depth of field",
              paleta=[["black", "#111111"], ["mid grey", "#8A8A86"], ["paper white", "#EDEBE6"]],
              uso="black and white period portrait used as the source image for a colorization edit",
              restriccion_extra="", libre_de="text, watermarks and any colour")),
 "E6": dict(E_COMUN, fuente_facetas=FUENTE_E.format("E6", "foto antigua dañada"),
   brief="Entrada de K18 (restaurar): copia en sepia de los años treinta, dañada, con el retrato de una persona "
         "inventada (no real). Mujer de unos 20 años, cabeza y hombros. Daños: rotura diagonal en la esquina inferior "
         "derecha, un pliegue, rayones finos, una mancha de agua en el borde superior y luces desvanecidas. Su QA solo "
         "comprueba que está dañada y sirve de entrada.",
   pieza=("editorial", "copia antigua dañada", "entrada de K18 (restaurar)"),
   sujetos=[dict(id="mujer", clase="persona", descripcion="mujer de unos 20 años de los años treinta", edad=20,
                 genero="mujer", rasgos=["cara redonda de mejillas llenas", "nariz estrecha", "cicatriz pequeña en el "
                                         "mentón"],
                 cabello="oscuro y corto, con ondas al agua de los años treinta",
                 vestuario="blusa clara de cuello redondo y una cadena delgada al cuello",
                 expresion="sonrisa leve con la boca cerrada", posicion="centrada, de frente, cabeza un poco inclinada")],
   escena=dict(espacio="interior", entorno="estudio fotográfico de los años treinta con fondo pintado liso; la copia "
               "en papel tiene rotura, pliegue, rayones, mancha de agua y luces desvanecidas"),
   camara=dict(plano="CU close-up", angulo="eye-level", efecto_optico="profundidad de campo corta",
               lente_intencion="85mm feel"),
   luz=dict(fuente="una luz de estudio de borde suave", direccion="desde la izquierda de cámara", dureza="suave",
            distribucion="el lado derecho de la cara cae en una sombra suave", contraste="medio"),
   rostro=dict(ocupacion=0.35, detalles=["grano de plata", "textura del papel"]),
   restricciones=["copia en sepia dañada: rotura, pliegue, rayones, mancha y desvanecido", "la rotura lejos del rostro",
                  "sin texto ni marcas de agua", "una sola persona"],
   estilo=["retro o vintage", "anclado en época, cultura o autor"],
   armar=dict(id="E6", ratio="4:5", pronombre="her", rostro_menor_20=False,
              escena="as a 1930s sepia studio print that is now damaged, against a plain painted backdrop #B49A78: a "
                     "diagonal tear across the bottom-right corner, a crease through the backdrop, fine scratches, a "
                     "brown water stain along the top edge and faded highlights.",
              elementos=["mujer", "fondo pintado", "daños de la copia"],
              sujeto="A woman of about 20, head and shoulders (close-up), facing the camera with her head slightly "
                     "tilted and a faint closed-mouth smile; a round face with full cheeks, a narrow nose and a small "
                     "scar on the chin, short dark hair set in 1930s finger waves, a light blouse with a rounded "
                     "collar and a thin chain necklace.",
              luz="One soft-edged studio light from camera left lights her face; the right side falls into a gentle "
                  "shadow.",
              microdetalle="Paper texture and silver grain show through the image; the torn edge reveals white paper "
                           "fibres; fine scratches cross her blouse.",
              camara="Eye-level camera, 85mm feel, shallow depth of field",
              paleta=[["sepia brown", "#7A5A3A"], ["faded cream", "#E6D8BC"], ["stain brown", "#9C7A4E"]],
              uso="damaged 1930s portrait print used as the source image for a restoration edit",
              restriccion_extra="with the tear kept away from her face", libre_de="text and watermarks")),
 "K26": dict(
   brief="Transferencia de estilo: el vaso de K05 (contenido, Image 1) con el estilo de la bahía de K02 (Image 2): su "
         "paleta de gris acero, azul pizarra y franjas ámbar, su contraluz lateral duro, sus sombras sin relleno, su "
         "contraste alto y su bruma fina. No se copia el contenido de K02. Key visual. Plantilla: gpt-image.md Style "
         "Transfer (INV-002389–002390), referencias con rol (INV-002386–002388).",
   paso="FL04 transferencia de estilo", plantilla_id="T-STYLE", ratio="1:1", px=(1024, 1024),
   pieza=("key visual de campaña", "producto con el estilo de otra imagen", "key visual de campaña"),
   sujetos=[dict(id="vaso", clase="producto", descripcion="el vaso de la imagen 1: vidrio transparente, recto, liso, "
                 "sin marca, vacío", posicion="centrado, frontal")],
   escena=dict(espacio="interior", entorno="superficie de piedra oscura mojada y fondo degradado gris tormenta"),
   camara=dict(plano="objeto entero", angulo="eye-level", altura="frontal, a la altura del vaso",
               efecto_optico="nitidez total"),
   luz=dict(fuente="una sola luz baja", direccion="contraluz lateral desde la derecha, como el sol de la imagen 2",
            dureza="dura", distribucion="franjas brillantes en el borde del vidrio y en la superficie mojada, frente "
            "del vaso en penumbra", contraste="alto"),
   transferencia=dict(propiedades=["paleta de la imagen 2: gris acero del cielo, azul pizarra del agua y franjas de "
                                   "luz ámbar", "contraluz lateral duro desde la derecha que deja franjas brillantes",
                                   "sombras profundas sin relleno", "contraste alto",
                                   "bruma fina y grano suave en el aire"]),
   restricciones=["no copiar el contenido de la imagen 2: sin mar, boya, nubes ni horizonte", "un solo vaso",
                  "sin marca, logo ni texto", "sin marcas de agua"],
   estilo=["comercial pulido"], representacion=["fotorrealista"],
   motivo_ref="T-STYLE exige las imágenes de contenido y de estilo con su sha256; aún no existen y se aprueba de nuevo "
              "cuando existan (PLAN §5, tarea 3)",
   referencias=[dict(indice=1, entrada="K05", medio="imagen", rol="contenido: el vaso",
                     preservar=["forma y proporción del vaso", "vidrio liso y transparente", "vaso vacío"]),
                dict(indice=2, entrada="K02", medio="imagen", rol="estilo: paleta, luz, contraste y bruma; no su "
                     "contenido", preservar=["paleta gris acero, azul pizarra y ámbar", "contraluz lateral duro",
                                             "sombras sin relleno"])]),
}
LOTE_4["K17"] = edicion(
    "E5", "Colorizar la foto en blanco y negro de E5 con colores propios de los años cincuenta y tonos de piel "
          "naturales. Todo lo demás queda igual. Plantilla: editing.md:48–55.",
    ("editorial", "foto de época colorizada", "pieza editorial de archivo"),
    "colorear la foto en blanco y negro con colores propios de los años cincuenta y tonos de piel naturales",
    ["rostro e identidad", "peinado", "pose y expresión", "forma de la ropa", "luz y sombras", "grano de película",
     "encuadre"],
    SIN_DERIVA + ["sin texto ni marcas de agua"])
LOTE_4["K18"] = edicion(
    "E6", "Restaurar la copia dañada de E6: reparar rotura, pliegue, rayones, mancha y desvanecido, y recuperar "
          "nitidez y contraste, conservando el carácter y el grano de la época. Plantilla: editing.md:65–71.",
    ("editorial", "foto antigua restaurada", "pieza editorial de archivo"),
    "restaurar la copia: reparar la rotura, el pliegue, los rayones, la mancha de agua y el desvanecido, y recuperar "
    "nitidez y contraste",
    ["rostro e identidad", "peinado", "pose y expresión", "blusa y collar", "tono sepia", "grano original de la época",
     "encuadre"],
    SIN_DERIVA + ["sin colorear", "sin texto ni marcas de agua"])
LOTE_4 = {k: LOTE_4[k] for k in ("E5", "E6", "K17", "K18", "K26")}

CABECERA_4 = ["# Lote 4 de briefs: entradas E5 y E6, ediciones K17 y K18, transferencia K26 (tarea 3)", "",
              "E5 y E6 son entradas (génesis de persona con `armar.py`) y se aprueban por el sha256 del brief; sus",
              "facetas son propuesta del sistema. K17, K18 y K26 usan imágenes que aún no existen y se aprueban por el",
              "«sha256 del contenido»; se aprueban de nuevo cuando existan (PLAN §5, tarea 3).", ""]

if __name__ == "__main__":
    construir(4, LOTE_4, CABECERA_4, planes=E_PLAN)
