---
familia: 01
nombre: Agua en superficie
cubre: wakeboarding, surf, jet ski, remo, esquí acuático, lancha, kayak de aguas bravas
d2_accion: [C_movimiento, B_pico]
d3_sujetos: [0, 1, 2_sin_contacto]
d4_tratamiento: [documental, narrativo, comercial, race]
d8_modelo: [nano-banana-pro, gpt-image-2]
d9_angulo: [low, eye-level]
especializa: video/references/animatic-keyframes.md
estado_archivo: BORRADOR 2026-09-25
---

# Agua en superficie

Especializa el método de keyframes para sujetos que se mueven sobre el agua. El agua es a la vez el
suelo, el fondo barrido y la fuente de partículas. La velocidad se lee en la superficie, no en el
sujeto. Las reglas de velocidad de `race-and-speed.md` valen aquí con el agua ocupando el papel del
asfalto.

## 1. Cuándo cargar

- Cargar este archivo siempre que el sujeto se desplace sobre una superficie de agua: tabla, casco, remo, pie descalzo o esquí. [A PRUEBA]
- Si el sujeto cruza la superficie hacia adentro o hacia afuera, cargar además `02-agua-ruptura.md`. [A PRUEBA]
- Si hay motor o vehículo acuático, leer antes `race-and-speed.md` §3 y §10: el presupuesto de velocidad y el anti-fake aplican íntegros. [FUENTE: video/references/race-and-speed.md §3]

## 2. Leyes físicas que el still debe evidenciar

1. La estela y el spray deben salir del punto de contacto y apuntar en sentido contrario a la dirección de viaje declarada; una estela que no coincide con la dirección de viaje es una contradicción y el modelo obedece la señal más fuerte. [FUENTE: video/references/universal-rules.md U8]
2. El spray se prompt como consecuencia física del canto de la tabla o del casco cortando el agua, nunca como "splash" abstracto: describe qué lo provoca y hacia dónde vuela. [FUENTE: video/references/universal-rules.md U9]
3. Las gotas congeladas se describen como constelación de puntos speculares con rim en el borde de ataque; sin ese rim el spray se lee como niebla blanca. [FUENTE: video/references/animatic-keyframes.md §4]
4. La superficie del agua debe mostrar textura direccional, rizado o chop, para que el barrido tenga algo que barrer; agua lisa equivale a asfalto sin textura. [FUENTE: video/references/animatic-keyframes.md §4]
5. Toda cuerda de remolque se dibuja tensa y recta desde el mango hasta fuera de cuadro; una cuerda con comba dice que no hay tracción y desmiente la velocidad. [A PRUEBA]
6. El cuerpo del rider debe mostrar el vector de la maniobra: rodillas flexionadas, cadera cargada hacia el canto, brazos en tensión; un rider erguido y relajado es un panel neutro y se descarta. [FUENTE: video/references/animatic-keyframes.md §4]
7. El agua desplazada tiene masa: la pared de agua junto al canto se levanta más alta en el lado de presión y se rompe en el lado libre; no es simétrica. [A PRUEBA]

## 3. Cue de movimiento congelado por defecto

- Cue por defecto: sujeto nítido contra superficie de agua barrida en el sentido del viaje, con el spray en blur parcial. [FUENTE: video/references/animatic-keyframes.md §4]
- Un still de superficie se considera rápido solo si reúne al menos tres de cinco cues: cámara a ras del agua, agua barriendo el borde inferior, referencia cercana pasando el borde, sujeto nítido contra fondo barrido, cue de vibración o spray golpeando la lente. [FUENTE: video/references/race-and-speed.md §3]
- Las gotas sobre la lente o la carcasa son la cue de vibración de este medio y se nombran como tal. [A PRUEBA]

## 4. Luz en este medio

- El spray solo se lee luminoso a contraluz o a contraluz lateral; el spray frontal es una masa gris muerta, igual que el humo frontal. [FUENTE: video/references/race-and-speed.md §7]
- La superficie del agua es el espejo del régimen: los prácticos y el sol se reflejan como estrías largas; usa el reflejo como spine de composición y saca la fuente real medio fuera de cuadro. [FUENTE: video/references/race-and-speed.md §7]
- Piel y neopreno mojados devuelven speculares duros; un cuerpo mojado sin brillos speculares se lee seco y falso. [A PRUEBA]
- Con sol alto el agua pierde textura y el spray se quema: preferir sol bajo, y declararlo en el prompt con hora y dirección, no con "golden hour" suelto. [A PRUEBA]

## 5. Cámara, ángulo y rig montable

- La cámara debe poder montarse en un rig real: torre de la lancha, pole cam desde la embarcación, carcasa a nivel del agua, dron bajo o cámara en el mango de la cuerda; un ángulo que ningún rig acuático puede ocupar se lee como render. [FUENTE: video/references/race-and-speed.md §2]
- Ángulo por defecto low a ras del agua: la superficie ocupa el tercio inferior y barre; el ángulo alto y limpio es el god-angle que mata la velocidad. [FUENTE: video/references/race-and-speed.md §10]
- El ángulo alto se reserva para el proof shot lejano: estela larga como prueba de distancia cubierta, una sola vez en la secuencia. [FUENTE: video/references/race-and-speed.md §5]
- Reservar el dutch para el único beat de pérdida de canto o caída. [FUENTE: video/references/race-and-speed.md §6]
- Lente: 24mm en el rig cercano para exagerar la proximidad del agua; larga focal desde la orilla para comprimir al rider contra la estela y la lancha. [FUENTE: video/references/race-and-speed.md §3]

## 6. Modelo recomendado

- Escenas con física de agua, spray y tela mojada: Nano Banana Pro, que es el modelo para escenas complejas con física y materiales finos. [FUENTE: image/references/models.md]
- Si la cara del rider está visible y es identidad de campaña, generar el maestro de rostro aparte según el template T1 y probar NB2 y NBP, porque NBP a veces sostiene peor los rostros. [FUENTE: image/references/nano-banana.md]
- Pedir "natural contrast, no HDR look": el agua y el spray disparan la tendencia a sobrecocer el HDR. [FUENTE: image/references/nano-banana.md]
- Lugar reconocible, una bahía o un lago concreto: NB2 con image grounding. [FUENTE: image/references/nano-banana.md]

## 7. Tratamiento de personas dentro del régimen

- El rostro suele quedar fragmentado por spray, gafas o casco: convertirlo en silueta con un glint es más fiable que pedir un rostro nítido a través del agua. [FUENTE: video/references/animatic-keyframes.md §7]
- Cuando la identidad del rider importa, la cara se fija en el maestro T1 y el cuadro de acción se inserta con referencia; nunca se pide identidad y spray en la misma génesis. [FUENTE: produccion-visual-sw30/SKILL.md R1]
- Las manos en el mango son anatomía en decisión: nudillos, tendones y agarre máximo; una mano relajada en el mango es filler. [FUENTE: video/references/animatic-keyframes.md §5]
- Dos riders en el mismo cuadro: uno por generación sobre la placa de agua, con la estela de cada uno coherente con su dirección. [FUENTE: produccion-visual-sw30/SKILL.md R1]

## 8. Fallos conocidos y su corrección

- El agua congelada parece vidrio o gel: falta textura direccional y blur parcial en el spray; añadir chop, gotas con rim y blur diferencial. [A PRUEBA]
- El spray sale como nube blanca sin forma: está iluminado de frente; pasar la fuente detrás o al lado del spray. [FUENTE: video/references/race-and-speed.md §7]
- La estela va hacia el lado equivocado: la dirección de viaje no estaba declarada; declararla antes que el sujeto. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]
- Horizonte inclinado sin querer: el modelo interpreta el movimiento como dutch; pedir horizonte nivelado salvo en el beat de caída. [A PRUEBA]
- Cuerda floja o que termina en el aire: nombrar el destino de la cuerda fuera de cuadro y su tensión. [A PRUEBA]

## 9. Checklist del crítico

- [ ] Estela y spray coherentes con la dirección de viaje declarada. [FUENTE: video/references/universal-rules.md U8]
- [ ] Al menos tres cues de velocidad presentes y nombrables. [FUENTE: video/references/race-and-speed.md §3]
- [ ] Spray con rim de contraluz, no masa gris. [FUENTE: video/references/race-and-speed.md §7]
- [ ] Cuerpo con vector de maniobra, cuerda tensa si existe. [A PRUEBA]
- [ ] Rig montable identificable. [FUENTE: video/references/race-and-speed.md §2]
- [ ] Sin HDR sobrecocido, sin rostro pedido a través del spray. [FUENTE: image/references/nano-banana.md]
