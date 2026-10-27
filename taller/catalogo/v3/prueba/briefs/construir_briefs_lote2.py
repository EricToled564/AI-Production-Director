"""construir_briefs_lote2.py: tarea 3, lote 2 (PLAN_FINAL_PRUEBA.md §5). G1, G2 y la composición K10–K13.

    python3 -I taller/catalogo/v3/prueba/briefs/construir_briefs_lote2.py

Usa las funciones de `construir_briefs.py` (contrato, caso del catálogo, sha256, validación), en archivo aparte para
que los briefs aprobados del lote 1 no cambien. Escribe lo mismo que el lote 1 más, en los casos de composición,
`Kxx.referencias.json`: las referencias previstas con su índice, rol y preservaciones.

G1 y G2 son del mismo tipo que K01 (PLAN §4, tabla de entradas): génesis de persona con brief de `armar.py`. Se
aprueban por el sha256 del brief, igual que el lote 1.

K10–K13 son composición con referencias. Sus imágenes de entrada (K01, K02, G1, G2) todavía no existen, así que
`entrada.referencias` no puede llevar su sha256 (schema: patrón de 64 hex). El plan (§5, tarea 3) pide aprobar primero
el contenido y aprobar de nuevo cuando la imagen exista. Aquí el contenido es la entrada sin `referencias` más las
referencias previstas, y se aprueba por su «sha256 del contenido». Hasta entonces los controles esperan exactamente estos
errores, y fallan si falta alguno o aparece otro:
- `validate_instance(…, 'brief')`: «Falta campo: entrada.referencias» y «Operación requiere referencia real»;
- `casos/validar.py`: «Brief incompleto» (requisito `entrada.referencias` sin resolver), más los de aprobación pendiente.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import construir_briefs as cb  # noqa: E402
import verificar_templates as vt  # noqa: E402  (cb ya puso su carpeta en sys.path)

G_PLAN = {g: dict(cb.PLAN["K01"], id=g, descripcion=f"rostro maestro T1 del miembro {m} de K12")
          for g, m in (("G1", "B"), ("G2", "C"))}
PENDIENTE_REF = {"path": "entrada.referencias", "motivo": "T-REF-COMP exige referencia real con sha256; la imagen de "
                 "entrada aún no existe y se aprueba de nuevo cuando exista (PLAN §5, tarea 3)", "resuelto": False}
ESPERADOS_CONTRATO = {"Falta campo: entrada.referencias", "Operación requiere referencia real"}

ESTUDIO_T1 = dict(escena=dict(espacio="interior", entorno="estudio con fondo continuo gris claro liso"),
                  camara=dict(plano="CU close-up", angulo="eye-level", efecto_optico="profundidad de campo corta",
                              lente_intencion="85mm feel, sin distorsión de gran angular en la cara"),
                  luz=dict(fuente="una sola luz dura", direccion="lateral desde la izquierda de cámara, rasante",
                           dureza="dura", distribucion="el lado de sombra queda uno o dos pasos más oscuro, sin relleno",
                           contraste="alto"),
                  restricciones=["sin texto ni marcas de agua", "sin retoque ni piel de estudio", "una sola persona"],
                  estilo=["documental"], representacion=["fotorrealista"], ratio="4:5", px=(1024, 1280))

LOTE_2 = {
 "G1": dict(ESTUDIO_T1,
   brief="Rostro maestro T1 de una persona inventada (no real), miembro B del grupo de K12. Hombre de unos 50 años, "
         "distinto de K01 y de G2 en cara, pelo y vestuario (EN.5). Mismo estudio y misma luz que K01, para que los "
         "tres maestros lleguen a K12 con la misma dirección de luz.",
   pieza=("retrato", "maestro de identidad de rostro del miembro B", "referencia de identidad para K12"),
   sujetos=[dict(id="hombre", clase="persona", descripcion="hombre de unos 50 años, cara ancha e irregular", edad=50,
                 genero="hombre", rasgos=["mandíbula cuadrada", "entradas pronunciadas", "cicatriz pequeña que corta "
                                          "la ceja derecha", "ojeras marcadas"],
                 cabello="castaño entrecano muy corto, barba de tres días gris y castaña",
                 vestuario="camisa de franela azul marino con el cuello abierto", expresion="neutra, boca cerrada",
                 posicion="centrado, cuerpo girado tres cuartos, mirada a cámara")],
   rostro=dict(ocupacion=0.35, detalles=["poros visibles", "barba de tres días", "rojeces en nariz", "pigmento desigual"]),
   armar=dict(id="G1", ratio="4:5", pronombre="him", rostro_menor_20=False,
              escena="in a studio against a seamless light grey backdrop #C8C8C6.", elementos=["hombre", "fondo"],
              sujeto="A man of about 50, head and shoulders (close-up), body turned three-quarters to camera, looking "
                     "into the lens with a neutral closed-mouth expression; a broad irregular face with a square jaw "
                     "and a receding hairline, three-day grey-and-brown stubble, a small scar cutting through the right "
                     "eyebrow, heavy under-eye bags, very short greying brown hair, a navy blue flannel shirt with an "
                     "open collar.",
              luz="One hard raking light from camera left grazes his face so pores, stubble and the brow scar cast "
                  "small shadows; the shadow side stays one to two stops darker, with no fill.",
              microdetalle="Individual stubble hairs catch the light; visible redness on the nose and uneven pigment "
                           "on the cheeks; the flannel weave shows at the collar.",
              camara="Eye-level camera, 85mm feel, shallow depth of field",
              paleta=[["light grey", "#C8C8C6"], ["navy blue", "#1F2A44"], ["grey brown", "#6B5E52"]],
              uso="face master for identity references in a group portrait",
              restriccion_extra="", libre_de="text and watermarks, with no retouching or studio gloss")),
 "G2": dict(ESTUDIO_T1,
   brief="Rostro maestro T1 de una persona inventada (no real), miembro C del grupo de K12. Mujer de unos 24 años, "
         "distinta de K01 y de G1 en cara, pelo y vestuario (EN.5). Mismo estudio y misma luz que K01.",
   pieza=("retrato", "maestro de identidad de rostro del miembro C", "referencia de identidad para K12"),
   sujetos=[dict(id="mujer_joven", clase="persona", descripcion="mujer de unos 24 años, rostro alargado e irregular",
                 edad=24, genero="mujer", rasgos=["nariz ancha", "cejas gruesas y rectas", "lunar pequeño sobre el "
                                                  "lado izquierdo del labio superior", "frente amplia"],
                 cabello="negro, rizado y voluminoso, recogido con una pinza y rizos sueltos en las sienes",
                 vestuario="suéter de punto acanalado color mostaza de cuello alto", expresion="neutra, boca cerrada",
                 posicion="centrada, cuerpo girado tres cuartos, mirada a cámara")],
   rostro=dict(ocupacion=0.35, detalles=["poros visibles", "lunar sobre el labio", "rojeces alrededor de la nariz",
                                         "pigmento desigual en la frente"]),
   armar=dict(id="G2", ratio="4:5", pronombre="her", rostro_menor_20=False,
              escena="in a studio against a seamless light grey backdrop #C8C8C6.", elementos=["mujer", "fondo"],
              sujeto="A woman of about 24, head and shoulders (close-up), body turned three-quarters to camera, "
                     "looking into the lens with a neutral closed-mouth expression; a long irregular face with a wide "
                     "nose, thick straight eyebrows, a broad forehead and a small mole above the left side of the "
                     "upper lip, voluminous black curly hair pinned up with a clip and loose curls at the temples, a "
                     "mustard ribbed-knit turtleneck sweater.",
              luz="One hard raking light from camera left grazes her face so pores, the mole and the fine curls cast "
                  "small shadows; the shadow side stays one to two stops darker, with no fill.",
              microdetalle="Loose curls catch the light; visible redness around the nose and uneven pigment on the "
                           "forehead; the ribbed knit texture shows at the neck.",
              camara="Eye-level camera, 85mm feel, shallow depth of field",
              paleta=[["light grey", "#C8C8C6"], ["mustard", "#C49A2C"], ["black", "#1A1A1A"]],
              uso="face master for identity references in a group portrait",
              restriccion_extra="", libre_de="text and watermarks, with no retouching or studio gloss")),
 "K10": dict(
   brief="Cuerpo entero T2 de la mujer de K01, con su rostro maestro adjunto como Image 1 y «keep facial features "
         "exactly the same» (INV-000474, 000487). Instante pico de esfuerzo: corre en una pista de atletismo al aire "
         "libre, vista de perfil, en plena zancada, con el pie delantero tocando la pista. Post vertical para redes. "
         "Es la entrada de K20 (cambiar vestuario) y K22 (cambiar fondo).",
   paso="E5.3", plantilla_id="T-REF-COMP", ratio="9:16", px=(1008, 1792),
   pieza=("post o historia para redes", "cuerpo entero T2 en el instante pico", "post vertical; entrada de K20 y K22"),
   sujetos=[dict(id="mujer", clase="persona", descripcion="la mujer de la imagen 1 (K01), cuerpo entero, corriendo",
                 edad=35, genero="mujer",
                 cabello="castaño oscuro a la altura de la mandíbula, como en la imagen 1, con mechones movidos por la "
                         "carrera",
                 vestuario="la camiseta de algodón gris carbón de la imagen 1, short negro de running y zapatillas de "
                           "running blancas sin marca",
                 expresion="boca entreabierta exhalando, mandíbula tensa",
                 posicion="de perfil, corre hacia el borde derecho del cuadro sobre el carril marcado por las líneas "
                          "blancas")],
   escena=dict(espacio="exterior", entorno="pista de atletismo de tartán rojo con líneas blancas de carril, césped y "
               "gradas vacías al fondo", momento="última hora de la tarde", clima="despejado",
               planos=["líneas del carril en primer plano", "corredora", "gradas vacías barridas al fondo"]),
   accion=dict(tipo="B instante pico", estado_visible="en plena zancada: el pie delantero acaba de tocar la pista con "
               "el antepié, el pie trasero ya despegado, brazos opuestos a las piernas",
               postura="torso un poco inclinado hacia delante, rodilla delantera alta, pierna trasera extendida",
               evidencia_fisica=["sudor como puntos especulares en sienes y clavículas", "tendones del cuello marcados",
                                 "manos abiertas y rígidas", "fondo y líneas del carril barridos en horizontal"]),
   fisica=["06 cuerpo en esfuerzo"],
   camara=dict(plano="WS wide", angulo="low", altura="a la altura de la cadera de la corredora",
               efecto_optico="paneo a la velocidad de la corredora: ella nítida, fondo barrido en horizontal, ligero "
               "barrido solo en el pie trasero", lente_intencion="85mm feel"),
   luz=dict(fuente="sol bajo de la tarde", direccion="lateral desde la derecha de cámara, del lado hacia donde corre",
            dureza="dura", distribucion="rostro y frente del cuerpo iluminados, espalda en sombra sin relleno",
            contraste="alto"),
   rostro=dict(ocupacion=0.02, detalles=["los mismos rasgos de la imagen 1", "sudor en las sienes"]),
   identidad=dict(invariantes=["rasgos faciales exactamente iguales a la imagen 1", "cabello castaño oscuro a la "
                               "altura de la mandíbula", "camiseta de algodón gris carbón"],
                  referencias=["Image 1: maestro de rostro K01"]),
   composicion=["la corredora ocupa el cuadro de la cabeza a los pies, con aire arriba y abajo",
                "espacio libre delante de ella, hacia donde corre"],
   restricciones=["una sola persona", "exactamente dos brazos, dos manos y dos piernas",
                  "sin dorsal, texto ni logos en ropa o calzado", "sin marcas de agua"],
   estilo=["documental"], representacion=["fotorrealista"],
   referencias=[dict(indice=1, entrada="K01", medio="imagen", rol="maestro de rostro: identidad de la corredora",
                     preservar=["rasgos faciales exactamente iguales", "cabello", "camiseta gris carbón"])]),
 "K11": dict(
   brief="Persona en lugar (T3): la mujer de K01 rema de pie sobre una tabla de paddle en la bahía de K02, con la "
         "tormenta entrando y el sol bajo a contraluz. Póster vertical; el titular se compone aparte sobre el cielo. "
         "Referencias: K02 como lugar, cielo y luz (Image 1) y K01 como rostro (Image 2). Posición por ancla legible: "
         "entre la cámara y la boya roja.",
   paso="E5.4", plantilla_id="T-REF-COMP", ratio="2:3", px=(1024, 1536),
   pieza=("póster o key art", "persona en lugar sobre el agua", "póster; titular compuesto aparte sobre el cielo"),
   sujetos=[dict(id="mujer", clase="persona", descripcion="la mujer de la imagen 2 (K01), cuerpo entero, de pie "
                 "sobre una tabla de paddle", edad=35, genero="mujer",
                 cabello="castaño oscuro a la altura de la mandíbula, mojado en las puntas",
                 vestuario="top de neopreno negro de manga corta y legging negro, mojados",
                 expresion="concentrada, labios apretados",
                 posicion="entre la cámara y la boya roja, un poco a la izquierda de la boya, avanzando hacia el "
                          "borde derecho del cuadro"),
            dict(id="tabla", clase="objeto o prop", descripcion="tabla de paddle blanca sin marca"),
            dict(id="remo", clase="objeto o prop", descripcion="remo de carbono negro con la pala hundida en el agua")],
   escena=dict(espacio="exterior", entorno="la bahía de la imagen 1 con su boya roja", momento="atardecer",
               clima="tormenta entrando, lluvia lejana",
               planos=["agua con textura de oleaje a ras de cámara", "remadora sobre la tabla", "boya roja",
                       "horizonte con cortina de lluvia"]),
   accion=dict(tipo="G acuática en superficie", estado_visible="a mitad de la palada: la pala hundida a la altura de "
               "los pies, rodillas flexionadas, cadera cargada hacia delante",
               evidencia_fisica=["estela pequeña en V desde la punta de la tabla hacia atrás",
                                 "gotas que caen del borde de la pala, con brillo de contraluz",
                                 "piel y neopreno mojados con especulares duros"]),
   fisica=["01 agua en superficie"],
   camara=dict(plano="WS wide", angulo="low", altura="a ras del agua, carcasa acuática a nivel de la superficie",
               efecto_optico="remadora nítida, agua del primer plano con desenfoque leve", lente_intencion="24mm feel"),
   luz=dict(fuente="sol bajo bajo las nubes, el mismo de la imagen 1", direccion="contraluz lateral desde la derecha",
            dureza="dura", distribucion="rim en el contorno de la remadora y en las gotas; frente del cuerpo en penumbra",
            contraste="alto"),
   rostro=dict(ocupacion=0.01, detalles=["los mismos rasgos de la imagen 2", "rostro en tres cuartos, legible"]),
   identidad=dict(invariantes=["rasgos faciales exactamente iguales a la imagen 2", "cabello castaño oscuro a la "
                               "altura de la mandíbula"],
                  referencias=["Image 1: lugar K02", "Image 2: maestro de rostro K01"]),
   composicion=["horizonte bajo: el cielo de tormenta ocupa el tercio superior, libre para el titular",
                "la remadora en el tercio central, con la boya roja detrás de ella a su derecha"],
   blocking=dict(relaciones=["la remadora entre la cámara y la boya roja",
                             "la estela apunta al lado contrario de su avance, hacia el borde izquierdo del cuadro"]),
   restricciones=["una sola persona", "sin barcos ni construcciones", "sin texto, logos ni marcas en tabla, remo o ropa",
                  "sin marcas de agua", "horizonte nivelado"],
   estilo=["documental"], representacion=["fotorrealista"],
   referencias=[dict(indice=1, entrada="K02", medio="imagen", rol="lugar, cielo y luz: la bahía, la boya roja, la "
                     "tormenta y la dirección del sol", preservar=["boya roja", "cielo de tormenta y cortina de lluvia",
                                                                   "dirección del sol"]),
                dict(indice=2, entrada="K01", medio="imagen", rol="maestro de rostro: identidad de la remadora",
                     preservar=["rasgos faciales exactamente iguales", "cabello"])]),
 "K12": dict(
   brief="Retrato de grupo de tres personas que deben reconocerse (K01, G1 y G2), en una sola pasada con los tres "
         "maestros de rostro adjuntos, cada uno con su rol (EN.4; GPT Image 2 admite hasta 16 referencias). Conversan "
         "alrededor de una mesa de cocina con luz de ventana. Se verifica rostro por rostro contra su maestro (EN.6). "
         "La escena va en texto, porque las entradas aprobadas de K12 no incluyen placa vacía (EN.2) ni cuerpos T2 "
         "de los miembros (EN.1).",
   paso="EN.4", plantilla_id="T-REF-COMP", ratio="3:2", px=(1536, 1024),
   pieza=("retrato", "retrato de grupo de tres identidades", "retrato de grupo editorial"),
   sujetos=[dict(id="miembro_A", clase="persona", descripcion="la mujer de la imagen 1 (K01)", edad=35, genero="mujer",
                 vestuario="camiseta de algodón gris carbón, como en la imagen 1",
                 expresion="habla a media frase, con la mano derecha abierta sobre la mesa",
                 posicion="sentada en la cabecera de la mesa, junto a la ventana"),
            dict(id="miembro_B", clase="persona", descripcion="el hombre de la imagen 2 (G1)", edad=50, genero="hombre",
                 vestuario="camisa de franela azul marino, como en la imagen 2", expresion="escucha con media sonrisa",
                 posicion="sentado en el lado largo del fondo de la mesa, de frente a la cámara, con los antebrazos "
                          "sobre la mesa"),
            dict(id="miembro_C", clase="persona", descripcion="la mujer de la imagen 3 (G2)", edad=24, genero="mujer",
                 vestuario="suéter mostaza de cuello alto, como en la imagen 3",
                 expresion="ríe con la cabeza un poco hacia atrás",
                 posicion="de pie en el extremo de la mesa más cercano a la cámara, con la mano derecha en el respaldo "
                          "de una silla")],
   escena=dict(espacio="interior", entorno="cocina de casa con mesa de madera gastada, ventana de marco blanco, dos "
               "tazas y un frutero sobre la mesa", momento="media mañana"),
   accion=dict(tipo="E interacción o diálogo", estado_visible="conversación: A habla a media frase, B y C reaccionan"),
   fisica=["09 grupo ensamble"],
   camara=dict(plano="MS medium", angulo="eye-level", altura="a la altura de los ojos de las personas sentadas",
               efecto_optico="los tres rostros nítidos, fondo de la cocina con desenfoque leve",
               lente_intencion="40mm feel, a distancia suficiente para no deformar a las personas de los extremos"),
   luz=dict(fuente="sol de media mañana por la ventana", direccion="lateral desde la ventana, a la izquierda de cámara",
            dureza="dura", distribucion="una sola dirección de luz para los tres; lado de sombra sin relleno",
            contraste="medio"),
   rostro=dict(ocupacion=0.02, detalles=["tres rostros legibles, cada uno igual a su maestro"]),
   identidad=dict(invariantes=["A tiene el rostro de la imagen 1", "B tiene el rostro de la imagen 2",
                               "C tiene el rostro de la imagen 3",
                               "tres identidades distintas en cara, pelo, estatura y vestuario"],
                  referencias=["Image 1: maestro K01, miembro A", "Image 2: maestro G1, miembro B",
                               "Image 3: maestro G2, miembro C"]),
   blocking=dict(relaciones=["B y C miran a A; A mira a B",
                             "A en la cabecera junto a la ventana, B en el lado largo del fondo, C de pie en el extremo "
                             "cercano a la cámara"],
                 contactos=["mano derecha de C sobre el respaldo de la silla", "mano derecha de A abierta sobre la mesa"]),
   composicion=["los tres rostros a alturas distintas: C de pie más alta, A y B sentados",
                "ningún rostro tapado por otra persona ni por objetos"],
   restricciones=["exactamente tres personas", "sin texto, logos ni marcas", "sin marcas de agua",
                  "ningún rostro sin dueño: cada rostro corresponde a su maestro"],
   estilo=["documental"], representacion=["fotorrealista"],
   referencias=[dict(indice=1, entrada="K01", medio="imagen", rol="miembro A: usar solo la persona de esta imagen",
                     preservar=["rasgos faciales exactamente iguales", "cabello", "camiseta gris carbón"]),
                dict(indice=2, entrada="G1", medio="imagen", rol="miembro B: usar solo la persona de esta imagen",
                     preservar=["rasgos faciales exactamente iguales", "cabello y barba", "camisa de franela azul"]),
                dict(indice=3, entrada="G2", medio="imagen", rol="miembro C: usar solo la persona de esta imagen",
                     preservar=["rasgos faciales exactamente iguales", "cabello rizado recogido", "suéter mostaza"])]),
 "K13": dict(
   brief="Multipanel 2x2 editorial de la mujer de K01 con la plantilla «2x2 Editorial Portrait Grid» de "
         "`multi-panel.md`: arriba a la izquierda retrato frontal, arriba a la derecha macro del rostro, abajo a la "
         "izquierda ángulo bajo, abajo a la derecha perfil. Misma persona y vestuario en los cuatro paneles, con su "
         "maestro de rostro adjunto.",
   paso="E5.4", plantilla_id="T-REF-COMP", ratio="1:1", px=(1024, 1024),
   pieza=("storyboard o multipanel", "multipanel 2x2 editorial de una persona", "composite editorial o de casting"),
   sujetos=[dict(id="mujer", clase="persona", descripcion="la mujer de la imagen 1 (K01), una vez en cada panel",
                 edad=35, genero="mujer", cabello="castaño oscuro a la altura de la mandíbula, como en la imagen 1",
                 vestuario="camiseta de algodón gris carbón, como en la imagen 1",
                 expresion="neutra en tres paneles; segura, con el mentón un poco levantado, abajo a la izquierda",
                 posicion="arriba izquierda de frente con mirada a cámara; arriba derecha rostro en macro; abajo "
                          "izquierda vista desde abajo; abajo derecha de perfil")],
   escena=dict(espacio="interior", entorno="estudio con fondo continuo gris claro liso, el mismo en los cuatro paneles"),
   camara=dict(plano="arriba izquierda CU close-up de hombros arriba; arriba derecha ECU extreme close-up macro del "
               "rostro; abajo izquierda CU close-up desde abajo; abajo derecha CU close-up de perfil",
               angulo="eye-level arriba; low abajo a la izquierda; perfil abajo a la derecha",
               efecto_optico="profundidad de campo corta en cada panel; separación mínima entre paneles",
               lente_intencion="85mm feel; macro en el panel de arriba a la derecha"),
   f24=["CU close-up", "ECU extreme close-up"], f25=["eye-level", "low", "perfil"],
   luz=dict(fuente="una sola luz dura", direccion="lateral desde la izquierda de cámara, rasante, la misma en los "
            "cuatro paneles", dureza="dura", distribucion="el lado de sombra queda uno o dos pasos más oscuro, sin "
            "relleno", contraste="alto"),
   rostro=dict(ocupacion=0.3, detalles=["poros visibles", "pecas en los pómulos", "sin retoque"]),
   identidad=dict(invariantes=["misma persona en los cuatro paneles, con los rasgos de la imagen 1",
                               "mismo cabello y misma camiseta en los cuatro paneles"],
                  referencias=["Image 1: maestro de rostro K01"]),
   composicion=["cuadrícula 2x2: dos columnas y dos filas, lectura de izquierda a derecha y de arriba abajo",
                "separación mínima entre paneles"],
   restricciones=["la misma persona en cada panel", "sin cambios de vestuario entre paneles", "sin otras personas",
                  "sin texto superpuesto", "sin marcas de agua"],
   estilo=["editorial"], representacion=["fotorrealista"],
   referencias=[dict(indice=1, entrada="K01", medio="imagen", rol="maestro de rostro: identidad de la persona en los "
                     "cuatro paneles", preservar=["rasgos faciales exactamente iguales", "cabello",
                                                 "camiseta gris carbón"])]),
}


def contenido_sha(entrada, refs):
    return hashlib.sha256(json.dumps({"entrada": entrada, "referencias_previstas": refs}, ensure_ascii=False,
                                     sort_keys=True, separators=(",", ":")).encode()).hexdigest()


CABECERA_2 = ["# Lote 2 de briefs: G1, G2 y composición K10–K13 (tarea 3)", "",
              "G1 y G2 se aprueban por el sha256 del brief, como el lote 1. K10–K13 llevan referencias a imágenes que "
              "aún",
              "no existen: se aprueba su contenido (la entrada sin `referencias` más las referencias previstas) por el",
              "«sha256 del contenido». Cuando exista cada imagen de entrada se escribe su sha256 y se aprueba de nuevo",
              "(PLAN §5, tarea 3). Todo lo que no viene de la lista de casos aprobada es propuesta del sistema.", ""]


def construir(n, lote, cabecera, planes=None):
    """Escribe los archivos de cada caso del lote y `LOTE_<n>.md`, corre los controles y sale con código 1 si fallan."""
    fallas, aprobados = [], []
    md = list(cabecera)
    for kid, d in lote.items():
        p = (planes or {}).get(kid) or G_PLAN.get(kid) or cb.PLAN[kid]
        d = dict(d)
        refs = d.pop("referencias", None)
        if refs:
            d["requisitos"] = [dict(PENDIENTE_REF, motivo=d["motivo_ref"]) if "motivo_ref" in d else PENDIENTE_REF]
        x = cb.contrato(kid, d, p)
        errs = cb.validate_instance(x, "brief")
        # verificar_templates.py:32 solo rechaza '' y None: una lista vacía en un campo exigido pasa. Se rechaza aquí.
        contrato_op = next(o for o in vt.C["operation_contracts"] if o["operacion"] == x["entrada"]["operacion"])
        for ruta in contrato_op["required_fields"]:
            try:
                if vt.get(x, ruta) == []:
                    errs.append(f"Lista vacía en campo exigido: {ruta}")
            except (KeyError, TypeError):
                pass
        if refs:
            faltan = ESPERADOS_CONTRATO - set(errs)
            errs = [e for e in errs if e not in ESPERADOS_CONTRATO]
            if faltan:
                errs.append(f"no aparecen los errores esperados por referencia pendiente: {sorted(faltan)}")
        for sv in x["entrada"]["selecciones_taxonomicas"]:
            fac, val = sv.split(": ", 1)
            if fac in cb.VALORES and val not in cb.VALORES[fac]:
                errs.append(f"{fac} «{val}» no está en el esquema")
        if x["entrada"]["modelo"]["nombre"] != "GPT Image 2":
            errs.append("modelo.nombre distinto de «GPT Image 2»")
        c = cb.caso_catalogo(kid, d, x, p)
        ap = cb.APROBACIONES.get(kid)
        digest = contenido_sha(x["entrada"], refs) if refs else cb.brief_sha(x)
        clave = "contenido_sha256" if refs else "brief_sha256"
        aprobado = bool(ap) and ap.get(clave) == digest
        if ap and not aprobado:
            print(f"  aviso {kid}: el brief cambió desde su aprobación; la aprobación queda invalidada")
        if aprobado:
            for campo in c["campos"]:
                campo["confirmado"] = True
            c["aprobacion"] = {"aprobado": True, "evidencia": f"mensaje {ap['mensaje_id']} ({ap['fecha']}): "
                               f"«{ap['texto']}» sobre {ap['documento']}; {clave} {digest}"}
            if not refs:
                x["aprobacion_brief"] = {"aprobado": True, "mensaje_id": ap["mensaje_id"], "brief_sha256": digest}
                for pc in x["procedencia_campos"]:
                    pc["aprobacion_id"] = ap["mensaje_id"]
                errs += cb.validate_instance(x, "seleccion")
            aprobados.append(kid)
        if errs:
            fallas.append(f"{kid} contrato: {errs}")
        (AQUI / f"{kid}.contrato.json").write_text(json.dumps(x, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        if refs:
            (AQUI / f"{kid}.referencias.json").write_text(json.dumps(refs, ensure_ascii=False, indent=1) + "\n",
                                                          encoding="utf-8")
        cp = AQUI / f"{kid}.caso.json"
        cp.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        gate = cb.validar_caso(cp)
        permitidos = (("Brief incompleto",) if refs else ()) + \
                     (() if aprobado else ("Dato propuesto sin confirmar", "Falta aprobación"))
        if refs and "Brief incompleto" not in gate:
            fallas.append(f"{kid} caso: falta el error esperado «Brief incompleto» por referencia pendiente")
        resto = [e for e in gate if not e.startswith(permitidos)] if permitidos else gate
        if resto:
            fallas.append(f"{kid} caso: {resto}")
        if "armar" in d:
            bp = AQUI / kid / "briefs.json"
            bp.parent.mkdir(exist_ok=True)
            bp.write_text(json.dumps([d["armar"]], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", str(cb.REPO / "produccion/template-retrato-gpt2/armar.py"),
                                str(bp)], capture_output=True, text=True)
            (bp.parent / "PROMPTS.txt").unlink(missing_ok=True)  # el prompt es de la tarea 9; aquí solo se valida
            if r.returncode != 0:
                fallas.append(f"{kid} armar.py: {r.stdout.strip()}")
        e = x["entrada"]
        md += [f"## {kid} · {p['descripcion'] or p['F10']}", "", d["brief"], "",
               f"- Facetas ({p.get('etiqueta_facetas') or ('mismo tipo que K01, PLAN §4' if kid.startswith('G') else 'lista aprobada')}): F10 {p['F10']} · F15 {p['F15']} · F32 {p['F32']} · F04 {p['F04']}"
               + "".join(f" · {f} {p[f]}" for f in ("F11", "F13", "F14") if p[f]),
               f"- Formato: {d['ratio']} · tamaño de referencia {d['px'][0]}x{d['px'][1]} · quality {p['quality']}",
               "- Propuesto por el sistema (inferencia para aprobación): " + "; ".join(
                   [f"{t} {json.dumps(e[k], ensure_ascii=False)}" for k, t in (("escena", "escena"), ("camara", "cámara"),
                                                                              ("luz", "luz")) if k in e]
                   + ([f"sujetos {json.dumps(e['sujetos']['items'], ensure_ascii=False)}"] if "sujetos" in e else [])
                   + [f"{k} {json.dumps(e[k], ensure_ascii=False)}" for k in
                      ("accion", "rostro", "identidad", "blocking", "composicion", "edicion", "texto_marca") if k in e]),
               f"- Restricciones: {'; '.join(d['restricciones'])}",
               f"- Módulos activos: {', '.join(e['modulos_activos'])}"]
        if refs:
            md += [f"- Referencia {r['indice']}: {r['entrada']} · rol: {r['rol']} · preservar: {'; '.join(r['preservar'])}"
                   for r in refs]
            md += [f"- **sha256 del contenido (referencias pendientes):** `{digest}`", ""]
        else:
            md += [f"- **sha256 del brief:** `{digest}`", ""]
    (AQUI / f"LOTE_{n}.md").write_text("\n".join(md), encoding="utf-8")
    for f in fallas:
        print("  FALLA", f)
    print(f"lote {n}: {len(lote)} casos · aprobados {len(aprobados)} · " + ("OK" if not fallas else f"{len(fallas)} fallas"))
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    construir(2, LOTE_2, CABECERA_2)
