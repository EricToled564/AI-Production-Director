---
familia: 04
nombre: Objeto balístico
cubre: pelota de tenis en el impacto, balón golpeado, gota cayendo, flecha, chispa, vaso que cae, fruta partiéndose
d2_accion: [B_pico, C_movimiento]
d3_sujetos: [0, 1]
d4_tratamiento: [documental, narrativo, comercial, race]
d8_modelo: [gpt-image-2, nano-banana-pro]
d9_angulo: [low, eye-level, overhead]
especializa: video/references/animatic-keyframes.md
estado_archivo: BORRADOR 2026-09-25
---

# Objeto balístico

Un objeto pequeño en vuelo o en el instante de impacto. Sin rostro y casi sin cuerpo, el objeto es
el actor: su deformación, su sombra de contacto y su estela cuentan la fuerza. Es el régimen donde
más fácil se cae en el objeto estático fetiche, que la fuente prohíbe.

## 1. Cuándo cargar

- Cargar cuando el sujeto principal del panel es un objeto en vuelo, en impacto o en el instante posterior al impacto. [A PRUEBA]
- Si el objeto lo impulsa una persona visible, cargar además `06-cuerpo-en-esfuerzo.md`; si el objeto es un vehículo, `05-vehiculo.md`. [A PRUEBA]

## 2. Leyes físicas que el still debe evidenciar

1. Un objeto solo carga emoción cuando cambia de estado: boardear el después del impacto, la pelota aplastada contra las cuerdas, el vaso ya quebrado, la gota ya convertida en corona; el objeto intacto en vuelo es un panel de setup, no de impacto. [FUENTE: video/references/animatic-keyframes.md §5]
2. El impacto se describe por su consecuencia física: la pelota se deforma y las cuerdas ceden, la superficie se astilla en telaraña, el polvo salta de la línea. [FUENTE: video/references/universal-rules.md U9]
3. Una pelota blanda en el impacto no es redonda: se achata contra la superficie, y el material del que está hecha lo dice el borde, fieltro erizado o cuero tenso. [A PRUEBA]
4. Toda acción produce reacción visible en lo que recibe el golpe: cuerdas deflectadas, tela hundida, superficie del agua deprimida; sin reacción, el objeto flota pegado. [A PRUEBA]
5. La sombra de contacto ancla el objeto al mundo: sin sombra de contacto o con sombra doble, el objeto se lee compuesto. [FUENTE: image/references/prompt-framework.md]
6. El vector de trayectoria se compone con el espacio negativo hacia donde el objeto va a resolverse, no de donde viene. [FUENTE: video/references/animatic-keyframes.md §4]
7. Un objeto pequeño necesita referencia de escala en el mismo plano de foco: una mano, una línea de cancha, una etiqueta; sin ella no hay tamaño. [A PRUEBA]

## 3. Cue de movimiento congelado por defecto

- Elegir una sola lógica de blur y declararla: o el objeto nítido y el fondo barrido, cámara que sigue al objeto, o el objeto barrido y el mundo nítido, cámara fija; las dos a la vez es imposible y el modelo mezcla. [FUENTE: video/references/animatic-keyframes.md §4]
- Cue por defecto en el impacto: blur parcial congelado, el objeto deformado tack-sharp y el polvo, las cuerdas o el líquido apenas barridos. [FUENTE: video/references/animatic-keyframes.md §4]
- Cue por defecto en vuelo: sharp-subject contra fondo barrido con macro y foco muy corto. [FUENTE: video/references/animatic-keyframes.md §4]
- Nunca describir la velocidad con adjetivos; describir el residuo: estela de polvo, fibras erizadas, gota alargada en el borde de fuga. [FUENTE: video/references/dramaturgy.md §2]

## 4. Luz en este medio

- Luz dura lateral o contraluz para que el material del objeto se lea: fieltro, cuero, vidrio, líquido; la luz frontal pareja convierte el objeto en un círculo plano. [FUENTE: video/references/camera-lighting-vocabulary.md §6]
- El polvo, el spray o las astillas solo tienen volumen a contraluz. [FUENTE: video/references/race-and-speed.md §7]
- Un specular duro en el objeto es obligatorio: sin él no hay información de material ni de forma. [FUENTE: video/references/race-and-speed.md §7]
- Sombra de contacto suave y definida donde el objeto toca, oclusión ambiental en el punto de deformación. [FUENTE: image/references/prompt-framework.md]

## 5. Cámara, ángulo y rig montable

- Ángulo por defecto low a la altura del plano de impacto: la red, la línea, la mesa; eye-level para seguir un vuelo; overhead solo para leer la geometría de la corona o la dispersión. [FUENTE: video/references/animatic-keyframes.md §6]
- Lente macro 100mm o equivalente descriptivo para textura y detalle; en Nano Banana describir "extreme close-up, shallow depth of field", no números. [FUENTE: video/references/camera-lighting-vocabulary.md §3]
- Rig montable: cámara de alta velocidad en trípode al nivel del impacto, o cámara robótica que sigue; una cámara que gira alrededor del objeto en el aire no existe en el rodaje real y se lee como render. [FUENTE: video/references/race-and-speed.md §2]
- Cámara implícita: crash zoom al detalle del impacto o freeze frame; nombrar cuál. [FUENTE: video/references/race-and-speed.md §6]

## 6. Modelo recomendado

- GPT Image 2 con quality high para el detalle congelado y la legibilidad de texturas finas, como en los patrones de ingrediente flotante. [FUENTE: image/references/patterns/ecommerce.md]
- Nano Banana Pro cuando la deformación física es el centro: razonamiento espacial para distorsión creíble. [FUENTE: image/references/patterns/ecommerce.md]
- Sin logos ni marcas en el objeto: se heredan de asset aprobado o se componen en post; el modelo los deforma. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]
- Prompt en cinco slots para GPT Image 2 con el slot Constraints declarando "no duplicate ball, no second shadow". [FUENTE: image/references/gpt-image.md]

## 7. Tratamiento de personas dentro del régimen

- Si aparece una persona, entra como anatomía en decisión: mano y antebrazo golpeando, no cuerpo entero; nombrar el verbo. [FUENTE: video/references/animatic-keyframes.md §5]
- La mano y el objeto se generan juntos solo si el contacto es el beat; si no, el objeto se genera solo y la persona en su propio cuadro. [FUENTE: produccion-visual-sw30/SKILL.md R1]
- Lateralidad nombrada en cualquier contacto: qué mano, qué lado de la raqueta. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]

## 8. Fallos conocidos y su corrección

- Pelota perfectamente redonda contra las cuerdas: falta el estado posterior; pedir la deformación y la deflexión de las cuerdas. [A PRUEBA]
- Objeto duplicado o sombra doble: pedir "single ball, single contact shadow" en Constraints y bajar la complejidad del fondo. [FUENTE: image/references/gpt-image.md]
- Blur en el objeto y en el fondo: se pidieron dos lógicas de cámara; elegir una. [FUENTE: video/references/animatic-keyframes.md §4]
- El objeto flota sin tocar: falta sombra de contacto y reacción de la superficie. [A PRUEBA]
- Marca o logo deformado en el objeto: quitarlo del prompt y componer en post. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]

## 9. Checklist del crítico

- [ ] Estado posterior visible con deformación y reacción del receptor. [FUENTE: video/references/animatic-keyframes.md §5]
- [ ] Una sola lógica de blur, declarada y cumplida. [FUENTE: video/references/animatic-keyframes.md §4]
- [ ] Sombra de contacto única. [A PRUEBA]
- [ ] Referencia de escala en foco. [A PRUEBA]
- [ ] Specular y material legibles. [FUENTE: video/references/race-and-speed.md §7]
- [ ] Sin marcas en el objeto. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]
