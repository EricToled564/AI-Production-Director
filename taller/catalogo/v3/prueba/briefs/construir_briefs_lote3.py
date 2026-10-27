"""construir_briefs_lote3.py: tarea 3, lote 3 (PLAN_FINAL_PRUEBA.md §5). Ediciones cuya entrada ya tiene brief aprobado.

    python3 -I taller/catalogo/v3/prueba/briefs/construir_briefs_lote3.py

K14, K15, K16, K19, K20, K22, K23, K24 y K25. Quedan para el lote de sus entradas K17 (E5), K18 (E6) y K21 (K30),
cuyas entradas todavía no tienen brief.

Cada edición es GPT2-EDIT (Change / Preserve / Constraints) sobre una sola imagen, con un cambio y la lista de lo que se
preserva (PLAN §3, fila Edición; `gpt-image.md` Editing; `editing.md:6`, `:8`). La edición conserva la toma, así que no
redefine escena, cámara ni luz y no activa el módulo fotografía (PLAN §3, módulos condicionales). El formato es el de la
imagen de entrada, leído de su contrato aprobado.

La imagen a editar todavía no existe: se aprueba el contenido como en el lote 2 (`construir_briefs_lote2.construir`),
con los mismos controles y los mismos errores esperados por referencia pendiente.
"""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from construir_briefs_lote2 import construir  # noqa: E402

FUENTE = {"K14": "gpt-image.md:96 (INV-002383 corregido); editing.md:10–19",
          "K15": "editing.md:21–27", "K16": "gpt-image.md:98; editing.md:29–46", "K19": "editing.md:73–78",
          "K20": "gpt-image.md:94 (INV-002382)", "K22": "characters.md:80 (TRM-0511)",
          "K23": "editing.md:97–100 (TRM-0518)", "K24": "editing.md:91–95 (TRM-1142)",
          "K25": "editing.md:80–86 (TRM-0520)"}
SIN_DERIVA = ["sin objetos nuevos fuera del cambio", "sin rediseño", "sin deriva de color, contraste ni encuadre"]


def edicion(kid, entrada, brief, pieza, cambio, preservar, restricciones, **extra):
    x = json.loads((AQUI / f"{entrada}.contrato.json").read_text(encoding="utf-8"))["entrada"]["formato"]
    d = dict(brief=f"{brief} Plantilla: {FUENTE[kid]}.", paso="E5.5", plantilla_id="T-EDIT", adaptador="GPT2-EDIT",
             ratio=x["ratio"], px=(x["ancho_px"], x["alto_px"]), pieza=pieza,
             edicion=dict(cambio=cambio, preservar=preservar), restricciones=restricciones,
             requisitos_base=("entrada.edicion.cambio", "entrada.edicion.preservar"),
             motivo_requisitos="campo exigido por T-EDIT",
             motivo_ref="T-EDIT exige la imagen a editar con su sha256; la imagen aún no existe y se aprueba de nuevo "
                        "cuando exista (PLAN §5, tarea 3)",
             referencias=[dict(indice=1, entrada=entrada, medio="imagen", rol="imagen a editar", preservar=preservar)])
    d.update(extra)
    return d


LOTE_3 = {
 "K14": edicion("K14", "K02",
   "Quitar un objeto del lugar: sacar la boya roja de la bahía de K02 y llenar su lugar con agua que continúa el "
   "oleaje y los reflejos de alrededor. Todo lo demás queda igual.",
   ("editorial", "lugar sin el objeto", "variante limpia de la placa de K02"),
   "quitar la boya roja y llenar su lugar con agua abierta que continúa el oleaje y los reflejos de alrededor",
   ["cielo de tormenta y cortina de lluvia", "dirección y color de la luz del sol bajo", "línea del horizonte",
    "textura del oleaje en el resto del cuadro", "encuadre y ángulo de cámara"],
   SIN_DERIVA + ["sin texto ni marcas de agua"]),
 "K15": edicion("K15", "K03",
   "Añadir un objeto a la edificación de época de K03: un puesto de periódicos de madera de los años cincuenta en la "
   "banqueta del primer plano, bajo el primer árbol de la Alameda, a escala de una persona adulta y con la misma luz "
   "de media mañana.",
   ("editorial", "lugar de época con un objeto añadido", "variante editorial de K03"),
   "añadir un puesto de periódicos de madera pintado de verde, de los años cincuenta, en la banqueta del primer plano "
   "bajo el primer árbol de la Alameda, del alto de una persona adulta, iluminado por el mismo sol de media mañana "
   "desde la izquierda y con su sombra hacia la derecha",
   ["fachada y cúpulas del Palacio de Bellas Artes", "árboles de la Alameda", "autos y transeúntes de la época y su "
    "posición", "luz de media mañana desde la izquierda", "encuadre y ángulo de cámara"],
   SIN_DERIVA + ["los periódicos sin texto legible", "sin marcas de agua"]),
 "K16": edicion("K16", "K03",
   "Cambiar el clima de K03: la mañana despejada pasa a una mañana de lluvia, con cielo cubierto, luz difusa y "
   "pavimento mojado que refleja la fachada. La arquitectura y todo lo demás quedan igual.",
   ("editorial", "lugar de época con otro clima", "variante editorial de K03"),
   "cambiar solo el clima: de mañana despejada a mañana de lluvia, con cielo cubierto, luz difusa sin sombras duras, "
   "lluvia fina y pavimento mojado que refleja la fachada",
   ["arquitectura del Palacio de Bellas Artes exactamente igual", "árboles de la Alameda", "autos y transeúntes de la "
    "época y su posición", "encuadre y ángulo de cámara"],
   SIN_DERIVA + ["sin paraguas ni personas nuevas", "una sola presión ambiental: la lluvia", "sin marcas de agua"]),
 "K19": edicion("K19", "K09",
   "Traducir al inglés el texto de la etiqueta del frasco de K09: «Miel de azahar» → «Orange Blossom Honey», «Peso "
   "neto 500 g» → «Net weight 500 g», «Hecho en Veracruz» → «Made in Veracruz». Misma tipografía, tamaño y posición.",
   ("e-commerce o catálogo", "producto con etiqueta traducida", "ficha de catálogo para mercado de habla inglesa"),
   "traducir al inglés las tres líneas de la etiqueta: «Miel de azahar» por «Orange Blossom Honey», «Peso neto 500 g» "
   "por «Net weight 500 g» y «Hecho en Veracruz» por «Made in Veracruz»",
   ["frasco, miel y tapa", "mesa de madera y fondo", "luz de ventana desde la izquierda",
    "tipografía serif oscura, tamaño y posición de cada línea", "papel crema de la etiqueta", "encuadre"],
   SIN_DERIVA + ["no extra words, no duplicate text, no watermarks", "texto legible al 100 %", "ninguna marca real"],
   texto_marca=dict(literales=["Orange Blossom Honey", "Net weight 500 g", "Made in Veracruz"],
                    posicion="etiqueta frontal, nombre arriba y dos líneas pequeñas debajo, en el lugar de las originales",
                    tipografia="la misma serif oscura de la etiqueta original")),
 "K20": edicion("K20", "K10",
   "Cambiar el vestuario de la corredora de K10: solo la ropa pasa a una camiseta de tirantes técnica azul cobalto y "
   "unas mallas cortas negras. Rostro, cuerpo, pose, pelo, expresión, zapatillas, fondo y luz quedan igual.",
   ("post o historia para redes", "misma persona con otro vestuario", "variante de K10 para redes"),
   "cambiar solo la ropa: camiseta de tirantes técnica azul cobalto y mallas cortas negras, con la luz y las sombras "
   "de la foto para que se vean llevadas de verdad",
   ["rostro exacto", "forma del cuerpo", "pose de la zancada", "cabello", "expresión", "zapatillas blancas",
    "pista y fondo barrido", "luz desde la derecha de cámara", "ángulo de cámara y encuadre"],
   SIN_DERIVA + ["sin logos ni texto en la ropa", "sin marcas de agua"]),
 "K22": edicion("K22", "K10",
   "Cambiar el lugar de la corredora de K10: la pista pasa a un paseo marítimo de concreto con barandal y el mar al "
   "fondo, con el mismo barrido horizontal del paneo. La misma persona y la misma luz en la cara y el cuerpo.",
   ("post o historia para redes", "misma persona en otro lugar", "variante de K10 para redes"),
   "cambiar el fondo y el suelo de la pista por un paseo marítimo de concreto con barandal y el mar al fondo, a última "
   "hora de la tarde, barrido en horizontal como el fondo original",
   ["rostro exacto", "forma del cuerpo", "pose de la zancada", "cabello", "ropa y zapatillas",
    "luz en la cara y el cuerpo desde la derecha de cámara", "ángulo de cámara y encuadre"],
   SIN_DERIVA + ["sin otras personas", "sin texto ni logos", "sin marcas de agua"]),
 "K23": edicion("K23", "K03",
   "Cambiar la textura de un material en K03: la banqueta del primer plano pasa a adoquín de basalto gris, mate y "
   "rugoso. El palacio y todo lo demás quedan igual.",
   ("editorial", "lugar de época con otra textura de superficie", "variante editorial de K03"),
   "dar a la banqueta del primer plano textura de adoquín de basalto gris, mate y rugosa",
   ["fachada y cúpulas del Palacio de Bellas Artes", "árboles de la Alameda", "autos y transeúntes de la época y su "
    "posición", "luz de media mañana desde la izquierda", "encuadre y ángulo de cámara"],
   SIN_DERIVA + ["sin marcas de agua"]),
 "K24": edicion("K24", "K05",
   "Llenar con física el vaso de K05: agua mineral con gas hasta tres cuartos de la altura del vaso, con refracción, "
   "menisco, burbujas finas y condensación en el vidrio, con la misma luz.",
   ("e-commerce o catálogo", "producto con líquido", "ficha de catálogo"),
   "llenar el vaso con agua mineral con gas hasta tres cuartos de su altura, con refracción del fondo a través del "
   "agua, menisco en el borde del líquido, burbujas finas y condensación en el vidrio, con la luz existente",
   ["forma, tamaño y posición del vaso", "fondo y superficie blancos", "luces laterales y trasera",
    "sombra de contacto suave", "encuadre"],
   SIN_DERIVA + ["sin hielo, rodajas ni salpicaduras", "sin marca, logo ni texto", "sin marcas de agua"]),
 "K25": edicion("K25", "K08",
   "Adaptar la miniatura de K08 al mercado francés con la plantilla de adaptación cultural: la calle pasa a una calle "
   "de París con adoquines y fachadas de piedra clara, y el letrero dice «Boulangerie». La plantilla junta en un "
   "cambio el lugar y el texto; se conservan la fachada de la panadería, su composición y la luz.",
   ("miniatura", "adaptación a otro mercado", "miniatura de video para Francia; titular aparte"),
   "adaptar al mercado francés: la calle pasa a una calle de París con adoquines y fachadas de piedra clara, y el "
   "letrero de madera dice «Boulangerie»",
   ["fachada de la panadería, puerta de madera y escaparate con pan", "posición y forma del letrero",
    "letras serif blancas pintadas a mano", "luz de primera hora desde la derecha", "composición y encuadre"],
   SIN_DERIVA + ["no extra words, no duplicate text, no watermarks", "el único texto es el letrero",
                 "ninguna marca real"],
   texto_marca=dict(literales=["Boulangerie"], posicion="letrero de madera sobre la puerta, en el lugar del original",
                    tipografia="las mismas letras serif blancas pintadas a mano")),
}

CABECERA_3 = ["# Lote 3 de briefs: ediciones K14–K16, K19, K20, K22–K25 (tarea 3)", "",
              "Cada edición cambia una sola cosa de una imagen de un lote aprobado y lista lo que se preserva. La imagen",
              "a editar aún no existe: se aprueba el contenido (la entrada sin `referencias` más la referencia prevista)",
              "por el «sha256 del contenido», y se aprueba de nuevo cuando exista (PLAN §5, tarea 3). K17, K18 y K21",
              "van con el lote de sus entradas (E5, E6, K30). Lo que no viene de la lista aprobada es propuesta del",
              "sistema.", ""]

if __name__ == "__main__":
    construir(3, LOTE_3, CABECERA_3)
