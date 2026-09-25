---
familia: 03
nombre: Subacuático
cubre: buceador explorando un cenote, nadador bajo el agua, apnea, snorkel, fauna marina, piscina desde abajo
d2_accion: [A_pose, C_movimiento, B_pico]
d3_sujetos: [0, 1, 2_sin_contacto]
d4_tratamiento: [documental, narrativo]
d8_modelo: [nano-banana-pro, nano-banana-2]
d9_angulo: [low, eye-level]
especializa: video/references/animatic-keyframes.md
estado_archivo: BORRADOR 2026-09-25
---

# Subacuático

Bajo el agua no hay horizonte, la luz se absorbe por colores y el medio está lleno de materia. El
entorno es la presión ambiental de todo el régimen: la visibilidad, las partículas y la dirección
de la luz hacen el trabajo que en tierra hace el clima.

## 1. Cuándo cargar

- Cargar cuando la cámara y el sujeto están completamente sumergidos. [A PRUEBA]
- Si el cuadro incluye la superficie desde abajo, este archivo manda; si la cruza, cargar además `02-agua-ruptura.md`. [A PRUEBA]

## 2. Leyes físicas que el still debe evidenciar

1. El agua absorbe primero los rojos: a pocos metros la piel, la sangre y los objetos rojos se ven pardos o grises salvo que una luz artificial cercana los recupere; un rojo saturado a profundidad sin fuente cercana es un error físico. [A PRUEBA]
2. La luz entra desde la superficie y se descompone en haces cuando hay una abertura o partículas; en un cenote los haces caen desde la boca de la caverna y son la única fuente motivada. [A PRUEBA]
3. Las cáusticas sobre el fondo o sobre el sujeto son la firma de una superficie iluminada por sol; sin sol directo no hay cáusticas. [A PRUEBA]
4. Las burbujas suben verticales y son la brújula del cuadro: indican dónde está arriba y, en racimo desde el regulador, marcan una exhalación reciente, es decir un cambio de estado. [A PRUEBA]
5. La visibilidad cae con la distancia: contraste y saturación se pierden hacia el fondo y viran al azul o verde, la perspectiva aérea de este medio. [FUENTE: image/references/vision-decomposer.md §2]
6. El pelo y la tela flotan y se separan del cuerpo; una melena pegada a la cabeza o una camiseta caída se leen como aire. [A PRUEBA]
7. La partícula en suspensión cerca de la lente, el backscatter, existe siempre que hay luz frontal; un agua perfectamente limpia se lee como aire teñido de azul. [A PRUEBA]

## 3. Cue de movimiento congelado por defecto

- Cue por defecto: quietud deliberada con una sola cosa en movimiento, el racimo de burbujas o una aleta en blur parcial; el medio ya comunica lentitud. [FUENTE: video/references/animatic-keyframes.md §4]
- Para un nadador rápido: sujeto nítido y estela de burbujas barrida detrás, nunca el fondo barrido, porque bajo el agua el fondo casi nunca es legible. [A PRUEBA]
- El estado de las burbujas es el cambio de estado del panel: exhalación recién liberada, no burbujas decorativas dispersas. [FUENTE: video/references/animatic-keyframes.md §5]

## 4. Luz en este medio

- Una fuente domina: la superficie. Toda luz adicional debe ser un práctico visible, linterna o foco del buzo, y su color cálido cerca del sujeto es la única forma legítima de recuperar rojos. [FUENTE: video/references/camera-lighting-vocabulary.md §5]
- Silueta contre-jour contra la superficie luminosa: cuerpo negro con un rim y un glint en la máscara; el cerebro completa lo que no ve. [FUENTE: video/references/race-and-speed.md §7]
- Los haces de luz son atmósfera y solo existen con partículas; pedir haces sin partículas produce rayos dibujados. [A PRUEBA]
- El 70% del cuadro puede quedar en penumbra azul; no rellenar. [FUENTE: video/references/race-and-speed.md §7]

## 5. Cámara, ángulo y rig montable

- Ángulo por defecto low mirando hacia la superficie: pone la fuente detrás del sujeto y da escala con los haces; el eye-level lateral sirve para la exploración; el picado desde arriba pierde la luz. [FUENTE: video/references/animatic-keyframes.md §6]
- Lente ancha, 24mm o menos, y cerca del sujeto: bajo el agua la distancia come contraste, así que la cámara se acerca en vez de cerrar plano con tele. [A PRUEBA]
- El rig es una carcasa con domo; la deformación de gran angular y la ligera viñeta del domo son texturas legítimas del régimen. [A PRUEBA]
- Cámara implícita: el descenso lento o el avance en una sola dirección; un solo movimiento por clip cuando se anime. [FUENTE: video/references/camera-lighting-vocabulary.md §2]

## 6. Modelo recomendado

- Nano Banana Pro para escenas complejas con física de luz, partículas y tela flotante. [FUENTE: image/references/models.md]
- NB2 con image grounding cuando el cenote, el arrecife o la especie deben ser fieles a la realidad; el grounding cubre lugares, animales y plantas. [FUENTE: image/references/nano-banana.md]
- Pedir "natural contrast, no HDR look": el azul profundo dispara el HDR sobrecocido. [FUENTE: image/references/nano-banana.md]
- thinking_level high en NB2 cuando se combina grounding con razonamiento espacial de la caverna. [FUENTE: image/references/nano-banana.md]

## 7. Tratamiento de personas dentro del régimen

- Con máscara y regulador el rostro no sostiene la identidad: la sostienen traje, aletas, color del tanque y silueta; esos elementos van en el identity block y se repiten verbatim. [FUENTE: video/references/universal-rules.md U7]
- El apneísta sin máscara sí muestra rostro: entonces aplica el maestro T1 seco, y el cuadro sumergido se inserta con referencia, con el viraje de color declarado como cambio de luz, no como cambio de identidad. [FUENTE: produccion-visual-sw30/SKILL.md R5]
- La piel bajo el agua se describe con su viraje real, cálida solo bajo la linterna; skin_doc sigue aplicando en textura, no en color. [A PRUEBA]
- Dos buzos: uno por generación sobre la placa del cenote; la profundidad relativa se declara por tamaño y por pérdida de contraste, no por "detrás". [FUENTE: produccion-visual-sw30/SKILL.md R2]

## 8. Fallos conocidos y su corrección

- El agua parece aire azul: faltan partículas, haces o pérdida de contraste con la distancia; añadir las tres, una por cláusula. [A PRUEBA]
- Piel rosada y labios rojos a diez metros: color físicamente imposible sin práctico; declarar el viraje o añadir la linterna como fuente. [A PRUEBA]
- Burbujas que van de lado o hacia abajo: el modelo perdió la vertical; declarar "bubbles rising straight up toward the surface". [A PRUEBA]
- Pelo y tela pegados al cuerpo: pedir flotación explícita. [A PRUEBA]
- Dos direcciones de luz sin práctico visible: contradicción; una fuente desde la superficie y, si hay otra, que se vea. [FUENTE: video/references/universal-rules.md U8]

## 9. Checklist del crítico

- [ ] Absorción de color coherente con la profundidad declarada. [A PRUEBA]
- [ ] Partículas, haces o pérdida de contraste presentes. [A PRUEBA]
- [ ] Burbujas verticales; racimo reciente si hay cambio de estado. [A PRUEBA]
- [ ] Una sola fuente dominante desde la superficie, prácticos visibles si hay más. [FUENTE: video/references/universal-rules.md U8]
- [ ] Pelo y tela flotando. [A PRUEBA]
- [ ] Identidad sostenida por equipo y silueta, verbatim entre cuadros. [FUENTE: video/references/universal-rules.md U7]
