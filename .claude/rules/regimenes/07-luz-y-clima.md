---
familia: 07
nombre: Luz y clima
cubre: rayo cortando el cielo, amanecer sobre un edificio, lluvia sobre una ventana, tormenta de polvo, niebla, nevada, flash de explosión
d2_accion: [D_luz_clima]
d3_sujetos: [0, 1, multitud]
d4_tratamiento: [documental, narrativo, comercial]
d8_modelo: [nano-banana-pro, nano-banana-2, gpt-image-2]
d9_angulo: [low, eye-level, high]
especializa: video/references/animatic-keyframes.md
estado_archivo: BORRADOR 2026-09-25
---

# Luz y clima

El fenómeno es el sujeto y a la vez la fuente de luz. Kurosawa: el clima es un personaje. Todo el
régimen se reduce a una disciplina: una sola fuente motivada domina, la atmósfera se lee solo a
contraluz y el evento se boardea ya formado.

## 1. Cuándo cargar

- Cargar cuando el beat lo lleva un fenómeno de luz o de clima, con o sin persona en cuadro. [A PRUEBA]
- Si el clima es solo fondo de una acción humana, la familia de la acción manda y este archivo aporta la sección 4. [A PRUEBA]

## 2. Leyes físicas que el still debe evidenciar

1. El evento se boardea completamente formado: el rayo entero de nube a suelo, la explosión ya expandida, el sol ya asomado; el instante de nacimiento del fenómeno se implica. [FUENTE: video/references/animatic-keyframes.md §5]
2. El fenómeno es la fuente motivada y su luz debe verse en el mundo: el rayo ilumina el suelo y las nubes desde su posición, el amanecer proyecta sombras largas desde el horizonte; un rayo que no ilumina nada es un dibujo. [FUENTE: video/references/camera-lighting-vocabulary.md §5]
3. Todas las sombras responden a una sola dirección; dos soles o dos direcciones de sombra son una contradicción y el modelo obedece la señal más fuerte. [FUENTE: video/references/universal-rules.md U8]
4. La lluvia, la nieve y el polvo solo se leen a contraluz; iluminados de frente son gris muerto. [FUENTE: video/references/race-and-speed.md §7]
5. La lluvia deja el mundo mojado: el asfalto y las superficies se vuelven espejo de los prácticos; lluvia sobre suelo seco es un error físico. [FUENTE: video/references/race-and-speed.md §7]
6. La niebla y la distancia bajan contraste y saturación y viran a frío hacia el fondo, la perspectiva aérea; el primer plano conserva contraste pleno. [FUENTE: image/references/vision-decomposer.md §2]
7. Una sola presión ambiental por panel: rayo, o lluvia, o niebla; apilar humo, niebla y spray produce barro. [FUENTE: video/references/race-and-speed.md §7]
8. Un fenómeno de luz quema su núcleo: centro blanco sin detalle, halo de halación alrededor, negros aplastados en lo que no toca; pedir detalle en el núcleo del rayo es pedir una ilustración. [FUENTE: video/references/race-and-speed.md §7]

## 3. Cue de movimiento congelado por defecto

- Cue por defecto: quietud deliberada del paisaje contra la violencia de la luz; el fenómeno es el único elemento que "se mueve" y está congelado en su forma completa. [FUENTE: video/references/animatic-keyframes.md §4]
- Lluvia y nieve se congelan como trazos cortos e iguales en dirección, no como puntos ni como cortinas; la longitud del trazo es la cue de velocidad de obturación y debe ser una sola. [A PRUEBA]
- Polvo y ceniza a contraluz como partículas con rim en el borde de ataque, igual que el spray. [FUENTE: video/references/animatic-keyframes.md §4]

## 4. Luz en este medio

- El fenómeno domina; cualquier otra luz debe ser un práctico visible y subordinado: farola, ventana, faros. [FUENTE: video/references/camera-lighting-vocabulary.md §5]
- Paleta con colores concretos, nunca "cinematic colors": rayo blanco azulado sobre nubes gris acero y suelo mojado con reflejos fríos; amanecer con horizonte ámbar y sombras azules largas. [FUENTE: video/references/camera-lighting-vocabulary.md §7]
- Textura nombrada: grano más pesado en la sombra, halación en el núcleo, un flare si la fuente entra en cuadro. [FUENTE: video/references/animatic-keyframes.md §7]
- Sin HDR sobrecocido: cielos de tormenta y amaneceres disparan la sobresaturación; pedir "natural contrast, no HDR look". [FUENTE: image/references/nano-banana.md]
- Las personas bajo el fenómeno se leen a contraluz: silueta con rim y un glint, sin rasgos. [FUENTE: video/references/race-and-speed.md §7]

## 5. Cámara, ángulo y rig montable

- Ángulo por defecto low con horizonte bajo: el cielo y el fenómeno ocupan dos tercios; high o aéreo para leer lluvia o nieve sobre un patrón urbano. [FUENTE: video/references/animatic-keyframes.md §6]
- Cámara implícita: locked-off en trípode, el fenómeno hace el movimiento; declarar "locked static frame" al animar para que el modelo no invente cámara. [FUENTE: video/references/kling.md §11]
- Lente ancha para el paisaje bajo el rayo; larga focal para un amanecer comprimido detrás de un edificio o landmark. [FUENTE: video/references/camera-lighting-vocabulary.md §3]
- La lluvia sobre la lente o la ventana es una textura legítima de primer plano y crea la tercera capa de profundidad. [FUENTE: video/references/animatic-keyframes.md §6]

## 6. Modelo recomendado

- Nano Banana Pro para la física de luz, partículas y atmósfera. [FUENTE: image/references/models.md]
- NB2 con image grounding cuando el fenómeno cae sobre un lugar real reconocible, edificio o skyline. [FUENTE: image/references/nano-banana.md]
- GPT Image 2 para anclas de época y cultura bajo el clima, "Berlin, November 1989" en la nieve, no para geometría exacta. [FUENTE: image/references/golden-rules.md]
- Recorrido de costo: variantes baratas para elegir la forma del rayo o del cielo, final en alta. [FUENTE: image/references/golden-rules.md]

## 7. Tratamiento de personas dentro del régimen

- La persona es escala y silueta; si necesita identidad, el rostro se fija en el maestro T1 y se inserta con referencia con la luz del fenómeno declarada como rim. [FUENTE: produccion-visual-sw30/SKILL.md R5]
- Con lluvia, la piel y la ropa mojadas devuelven speculares y el pelo se pega; declararlo o el sujeto se lee seco bajo la lluvia. [A PRUEBA]
- Multitud bajo el fenómeno: siluetas sin rostro legible, tratada como entorno según `08-multitud-anonima.md`. [FUENTE: video/references/animatic-keyframes.md §7]

## 8. Fallos conocidos y su corrección

- Rayo decorativo que no ilumina: declarar qué superficies recibe su luz y desde dónde. [A PRUEBA]
- Dos direcciones de sombra: eliminar la segunda fuente o hacerla práctico visible. [FUENTE: video/references/universal-rules.md U8]
- Lluvia uniforme sobre todo el cuadro sin contraluz: mover la fuente detrás de la lluvia y dejar el primer plano con gotas grandes. [FUENTE: video/references/race-and-speed.md §7]
- Suelo seco bajo lluvia: pedir superficies mojadas y reflejos. [FUENTE: video/references/race-and-speed.md §7]
- Cielo HDR de postal: pedir contraste natural y negros aplastados. [FUENTE: image/references/nano-banana.md]

## 9. Checklist del crítico

- [ ] Fenómeno completamente formado y su luz visible en el mundo. [FUENTE: video/references/animatic-keyframes.md §5]
- [ ] Una sola dirección de sombras. [FUENTE: video/references/universal-rules.md U8]
- [ ] Atmósfera a contraluz, una sola presión ambiental. [FUENTE: video/references/race-and-speed.md §7]
- [ ] Superficies mojadas si llueve; perspectiva aérea si hay niebla. [A PRUEBA]
- [ ] Núcleo quemado con halación, sin HDR. [FUENTE: video/references/race-and-speed.md §7]
- [ ] Personas en silueta o insertadas con referencia. [FUENTE: produccion-visual-sw30/SKILL.md R5]
