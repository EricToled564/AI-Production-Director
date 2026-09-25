---
familia: 02
nombre: Ruptura de superficie
cubre: clavado entrando al agua, nadador emergiendo, salto de ballena o delfín, split-level mitad aire mitad agua, objeto cayendo al agua
d2_accion: [B_pico]
d3_sujetos: [0, 1]
d4_tratamiento: [documental, narrativo, comercial]
d8_modelo: [nano-banana-pro, gpt-image-2]
d9_angulo: [low, eye-level, overhead]
especializa: video/references/animatic-keyframes.md
estado_archivo: BORRADOR 2026-09-25
---

# Ruptura de superficie

El instante en que un cuerpo cruza la frontera entre aire y agua. Es el tipo B en estado puro: un
diezmilésimo de segundo arrestado. La regla que gobierna todo el archivo es boardear el estado
posterior del umbral, nunca el anterior.

## 1. Cuándo cargar

- Cargar cuando el beat es el cruce de la superficie en cualquier sentido: entrada de clavado, salida de un nadador, salto de un animal marino, objeto que cae al agua. [A PRUEBA]
- No cargar para un sujeto totalmente sumergido; eso es `03-subacuatico.md`. Para un sujeto que se desplaza encima sin cruzar, `01-agua-superficie.md`. [A PRUEBA]

## 2. Leyes físicas que el still debe evidenciar

1. Boardear el estado posterior: el agua ya abierta, la corona de salpicadura ya formada, el cuerpo ya parcialmente dentro; el instante anterior se implica. [FUENTE: video/references/animatic-keyframes.md §5]
2. La forma de la salpicadura depende de la entrada y hay que declararla: un cuerpo alineado y vertical produce entrada limpia con corona baja y un chorro fino; un cuerpo abierto produce corona ancha y agua blanca. [A PRUEBA]
3. La parte sumergida se ve desplazada y ligeramente comprimida respecto a la parte emergida por la refracción; una extremidad que cruza la línea del agua sin quiebre óptico se lee como recorte. [A PRUEBA]
4. Arriba de la línea hay gotas; abajo hay burbujas. No se mezclan: las gotas caen, las burbujas suben. [A PRUEBA]
5. El movimiento se prompt por su consecuencia: el cuerpo abre el agua, la superficie se hunde en el punto de entrada y se levanta alrededor. [FUENTE: video/references/universal-rules.md U9]
6. Un still es un instante congelado: usar "frozen mid-entry" o "frozen at the instant the hands break the surface", nunca verbos de proceso como "diving" o "splashing". [FUENTE: produccion-visual-sw30/SKILL.md R8]
7. La línea de superficie es una sola: si el encuadre es split-level, hay exactamente un menisco que cruza el cuadro, con el aire nítido arriba y el agua con su propia atmósfera abajo. [A PRUEBA]

## 3. Cue de movimiento congelado por defecto

- Cue por defecto: blur parcial congelado, el agua en movimiento apenas barrida y el cuerpo o el objeto tack-sharp; es la prueba de un único instante arrestado. [FUENTE: video/references/animatic-keyframes.md §4]
- Alternativa para el beat previo al impacto: vector de trayectoria, el cuerpo en el aire en una postura que solo puede resolverse hacia abajo, con espacio negativo hacia el agua. [FUENTE: video/references/animatic-keyframes.md §4]
- Nunca blur uniforme en toda la imagen: iguala la salpicadura al fondo y borra el instante. [FUENTE: video/references/animatic-keyframes.md §7]

## 4. Luz en este medio

- La corona y las gotas solo se leen a contraluz o con luz lateral dura; iluminarlas de frente produce una mancha blanca sin volumen. [FUENTE: video/references/race-and-speed.md §7]
- En split-level la mitad de aire y la mitad de agua tienen exposiciones distintas: el agua uno o dos pasos más oscura, con cáusticas si hay sol; declararlo evita que el modelo unifique las dos mitades. [A PRUEBA]
- Una presión ambiental por panel: la salpicadura ya es la atmósfera; no sumar niebla, lluvia o spray adicional. [FUENTE: video/references/race-and-speed.md §7]

## 5. Cámara, ángulo y rig montable

- Rig por defecto: carcasa a nivel exacto de la superficie, o cámara de borde de piscina baja; para el split-level, carcasa con domo semisumergido. [A PRUEBA]
- Ángulo por defecto low a nivel del agua, aislando la salpicadura contra cielo o techo; el overhead se reserva para leer la geometría de la corona desde arriba. [FUENTE: video/references/animatic-keyframes.md §6]
- Lente: 35mm a 50mm desde el borde para no deformar el cuerpo; macro solo para el detalle de las manos rompiendo la superficie. [FUENTE: video/references/camera-lighting-vocabulary.md §3]
- El rig debe existir: una cámara dentro del chorro de entrada o en el fondo de la fosa mirando hacia arriba son montajes reales; una cámara flotando a mitad de la salpicadura no. [FUENTE: video/references/race-and-speed.md §2]

## 6. Modelo recomendado

- Nano Banana Pro para la física del agua: corona, gotas, refracción y tela mojada. [FUENTE: image/references/models.md]
- GPT Image 2 con quality high cuando el detalle de gotas y condensación es el centro del cuadro. [FUENTE: image/references/patterns/food-beverage.md]
- Si el sujeto es una especie animal real, NB2 con image grounding para la anatomía correcta. [FUENTE: image/references/nano-banana.md]
- Recorrido de costo: variantes a 0.5K, selección, regeneración del ganador a 2K o 4K. [FUENTE: image/references/golden-rules.md]

## 7. Tratamiento de personas dentro del régimen

- En el instante de entrada el rostro no es la identidad: gorro, gafas, traje y silueta la sostienen; esos accesorios se fijan en el identity block del maestro y se repiten. [FUENTE: video/references/universal-rules.md U7]
- El maestro de rostro se genera aparte y seco; el cuadro de ruptura se inserta con referencia sobre la placa de agua. [FUENTE: produccion-visual-sw30/SKILL.md R7]
- La anatomía en el pico se audita al 100% de zoom como manos y rostros: dedos alineados, muñecas, columna en línea. [FUENTE: produccion-visual-sw30/SKILL.md R14]
- Dos cuerpos entrando a la vez: un sujeto por generación; la sincronía la fija el keyframe aprobado, no el texto. [FUENTE: produccion-visual-sw30/SKILL.md R9]

## 8. Fallos conocidos y su corrección

- Dos superficies de agua o un horizonte de agua duplicado: el prompt mezcló vista de superficie y vista sumergida; declarar una sola línea de agua y desde qué lado mira la cámara. [A PRUEBA]
- El cuerpo aparece entero y nítido bajo el agua sin quiebre de refracción: pedir explícitamente el desplazamiento óptico en la línea del agua. [A PRUEBA]
- El modelo dibuja al clavadista en el aire cuando se pidió la entrada: falta el estado posterior; describir el agua ya abierta y las manos ya dentro. [FUENTE: video/references/animatic-keyframes.md §5]
- Salpicadura sin dirección, simétrica como fuente: nombrar el ángulo de entrada y el lado de presión. [A PRUEBA]
- Corona blanca y plana: luz frontal; mover la fuente detrás del agua. [FUENTE: video/references/race-and-speed.md §7]

## 9. Checklist del crítico

- [ ] Estado posterior visible: agua abierta, corona formada. [FUENTE: video/references/animatic-keyframes.md §5]
- [ ] Una sola línea de superficie; refracción presente en lo sumergido. [A PRUEBA]
- [ ] Gotas arriba, burbujas abajo, nunca invertidas. [A PRUEBA]
- [ ] Blur diferencial, no uniforme. [FUENTE: video/references/animatic-keyframes.md §7]
- [ ] Anatomía del pico correcta al zoom. [FUENTE: produccion-visual-sw30/SKILL.md R14]
- [ ] Rig montable identificable. [FUENTE: video/references/race-and-speed.md §2]
