---
familia: 05
nombre: Vehículo en movimiento
cubre: auto de carreras, moto, bicicleta, tren, lancha rápida, dron, avión ligero; extiende race-and-speed a vehículos fuera del circuito
d2_accion: [C_movimiento]
d3_sujetos: [0, 1]
d4_tratamiento: [race, documental, narrativo, comercial]
d8_modelo: [nano-banana-pro, gpt-image-2, flux]
d9_angulo: [low, eye-level]
especializa: video/references/race-and-speed.md
estado_archivo: BORRADOR 2026-09-25
---

# Vehículo en movimiento

Este régimen ya tiene dueño: `race-and-speed.md` es la autoridad para todo vehículo a velocidad, con
`animatic-keyframes.md` como método base. Este archivo no repite esas reglas; las señala y añade lo
que cambia cuando el vehículo no es un auto de carreras en una pista.

## 1. Cuándo cargar

- Cargar `race-and-speed.md` completo antes que este archivo para cualquier vehículo a velocidad. [FUENTE: video/SKILL.md paso 4]
- Este archivo se carga después, solo para las extensiones: moto, bicicleta, tren, lancha, dron y avión ligero. [A PRUEBA]

## 2. Leyes físicas que el still debe evidenciar

1. Un still vende velocidad solo si reúne al menos tres de cinco cues: cámara a la altura del parachoques o más baja, asfalto barriendo el borde inferior, referencia cercana pasando el borde, héroe nítido contra fondo barrido, cue de vibración mecánica. [FUENTE: video/references/race-and-speed.md §3]
2. La física tiene que estar en el still: squat de la carrocería, nariz levantada, neumático arrugado, rim barrido; nunca depender de que el panel se vea rápido acelerado en post. [FUENTE: video/references/race-and-speed.md §1]
3. Los rayos de una rueda en movimiento siempre van barridos en disco; un rim nítido en un vehículo en marcha es el fallo más frecuente y más delator. [FUENTE: video/references/race-and-speed.md §10]
4. En moto la física visible es el ángulo de inclinación y el borde del neumático trabajando: rodilla o codo cerca del suelo, el cuerpo descolgado hacia el interior de la curva. [A PRUEBA]
5. En bicicleta la velocidad se lee en la cadencia barrida de las piernas y en la cadena, con el cuerpo tenso sobre el manillar; el sudor es el specular de este vehículo. [A PRUEBA]
6. En tren o metro la velocidad se lee por compresión de larga focal y por el andén o los postes barridos; el vehículo en sí apenas se deforma. [FUENTE: video/references/race-and-speed.md §3]
7. En dron o hélice, las palas se dibujan como discos translúcidos, nunca como palas nítidas. [A PRUEBA]
8. Toda consecuencia física declarada obliga a la causa: neumáticos que levantan cortinas de agua, gravilla frenada en el borde de ataque. [FUENTE: video/references/universal-rules.md U9]

## 3. Cue de movimiento congelado por defecto

- Cue por defecto: héroe nítido y mundo barrido en el eje de viaje, con una referencia cercana alargada en varilla de luz. [FUENTE: video/references/animatic-keyframes.md §4]
- Alternar registros: paneles bajos y anchos con paneles de compresión de larga focal; nunca toda la secuencia con una sola lente. [FUENTE: video/references/race-and-speed.md §3]
- Nombrar el blur diferencial de forma explícita porque los modelos estabilizan de más: "motion blur on background, fast-shutter look on subject, rim spokes smeared to a disc". [FUENTE: video/references/animatic-keyframes.md §7]

## 4. Luz en este medio

- Luz specular, no ambiental: un specular duro en metal o goma por panel. [FUENTE: video/references/race-and-speed.md §7]
- El calor, disco de freno o escape, es el único cálido permitido en el registro race y debe ser puntual y rodeado de frío. [FUENTE: video/references/race-and-speed.md §7]
- Fuera del registro race, un spot comercial de vehículo puede usar paleta cálida: entonces se declara el tratamiento comercial en la tarjeta y el ban de ámbar no aplica. [A PRUEBA]
- El humo, el polvo o el spray de rueda solo a contraluz. [FUENTE: video/references/race-and-speed.md §7]

## 5. Cámara, ángulo y rig montable

- La cámara va donde un rig real puede atornillarse: parachoques, capó, hostess-tray, eje, cabina hard-mount; si no, se lee render. [FUENTE: video/references/race-and-speed.md §2]
- Rotar entre las cinco familias de plano: perfil hostess-tray, POV bajo de capó, cabina con vibración, tracking paralelo o joust, proof shot lejano. [FUENTE: video/references/race-and-speed.md §5]
- Ángulo por defecto low a la altura del parachoques; el god-angle alto y limpio mata la velocidad. [FUENTE: video/references/race-and-speed.md §10]
- Dutch solo en el único beat de pérdida de tracción. [FUENTE: video/references/race-and-speed.md §6]
- En bici y moto el rig cercano es la cámara de casco o el chest mount: POV con manillar y manos en primer plano duro. [A PRUEBA]

## 6. Modelo recomendado

- Nano Banana Pro para escenas complejas con física y materiales; GPT Image 2 quality high cuando hay etiquetas, patrocinadores o pantallas legibles. [FUENTE: image/references/models.md]
- Flux 2 Pro o Midjourney v7 vía adaptador de forge para el hero photoreal sin rostro. [FUENTE: visual-prompt-forge/references/failure-modes.md F1]
- Sin marcas de patrocinador generadas: se componen en post o se heredan del asset aprobado. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]
- Al animar en Kling, la acción rápida se genera lenta y se acelera en post para evitar morphing. [FUENTE: video/references/kling.md §11]

## 7. Tratamiento de personas dentro del régimen

- Sin rostro, o rostro fragmentado por casco, visera y reflejos; la emoción va en nudillos, pedal y aguja. [FUENTE: video/references/race-and-speed.md §4]
- Cuando el piloto o ciclista es identidad de campaña, el rostro se fija en el maestro T1 fuera del vehículo y el cuadro de acción hereda casco, traje y número como identity block. [FUENTE: video/references/universal-rules.md U7]
- Anatomía solo en decisión: mano que cambia, pie que pisa, rodilla que baja. [FUENTE: video/references/animatic-keyframes.md §5]

## 8. Fallos conocidos y su corrección

- Rim nítido: pedir explícitamente los rayos barridos en disco. [FUENTE: video/references/race-and-speed.md §10]
- Cabina perfectamente estable: añadir espejo trémulo, aguja doblada, horizonte 1 a 3 grados fuera. [FUENTE: video/references/race-and-speed.md §10]
- Moto vertical en curva: declarar el ángulo de inclinación y el lado de la rodilla. [A PRUEBA]
- Palas de dron nítidas: pedir discos translúcidos. [A PRUEBA]
- Aire alrededor del vehículo en un beat de velocidad: acercar barrera, rival o pared al borde. [FUENTE: video/references/race-and-speed.md §10]

## 9. Checklist del crítico

- [ ] Tres de cinco cues de velocidad presentes. [FUENTE: video/references/race-and-speed.md §3]
- [ ] Rim barrido, física visible en el chasis. [FUENTE: video/references/race-and-speed.md §10]
- [ ] Rig montable. [FUENTE: video/references/race-and-speed.md §2]
- [ ] Un specular duro por panel; cálido solo puntual en registro race. [FUENTE: video/references/race-and-speed.md §7]
- [ ] Inclinación y borde de neumático en moto; cadencia barrida en bici; discos en hélices. [A PRUEBA]
- [ ] Sin marcas generadas. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]
