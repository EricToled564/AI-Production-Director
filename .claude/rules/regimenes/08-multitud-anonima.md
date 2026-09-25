---
familia: 08
nombre: Multitud anónima
cubre: estadio, manifestación, calle llena, público de concierto, maratón visto de lejos, mercado
d2_accion: [F_multitud, C_movimiento]
d3_sujetos: [multitud]
d4_tratamiento: [documental, narrativo, comercial]
d8_modelo: [nano-banana-pro, gpt-image-2]
d9_angulo: [high, low, eye-level]
especializa: video/references/animatic-keyframes.md
estado_archivo: BORRADOR 2026-09-25
---

# Multitud anónima

Una multitud es entorno, no sujetos. Nadie tiene rostro legible y la masa hace el trabajo de escala,
presión o textura. Los héroes, si los hay, se insertan después, uno por uno, y nunca son más de tres.
Esto es distinto del grupo ensamble, donde cada miembro es una identidad; ese caso vive en
`09-grupo-ensamble.md`.

## 1. Cuándo cargar

- Cargar cuando hay más de seis personas en cuadro y ninguna de las figuras de la masa necesita reconocerse. [A PRUEBA]
- Si tres o más figuras deben reconocerse, no es multitud: cargar `09-grupo-ensamble.md`. [A PRUEBA]

## 2. Leyes físicas que el still debe evidenciar

1. La multitud se produce como placa de entorno: figuras anónimas, sin rostros legibles, siluetas, espaldas, desenfoque o contraluz; después se insertan los héroes con referencia. [FUENTE: produccion-visual-sw30/SKILL.md R7]
2. Un sujeto por generación: nunca se pide a un modelo N rostros distintos desde texto. [FUENTE: produccion-visual-sw30/SKILL.md R1]
3. Los extras de fondo no deben clonar al héroe ni entre sí: ropa, pelo y rasgos distintos, movimientos no sincronizados, "no identical clones in the background". [FUENTE: video/references/fixes-and-skeletons.md §2]
4. Tres planos con trabajos distintos: primer plano como textura que obstruye, plano medio para los héroes, fondo como escala; si los tres planos tienen el mismo desenfoque y tamaño hay un solo plano. [FUENTE: video/references/animatic-keyframes.md §6]
5. La multitud en la periferia se dibuja barrida y fragmentada; da escala y peligro sin identidades. [FUENTE: video/references/race-and-speed.md §3]
6. Una multitud en movimiento, manifestación o carrera callejera, se trata como textura con las cues de velocidad: barrido direccional coherente con la dirección declarada del flujo. [A PRUEBA]
7. Las pancartas, camisetas y pantallas no llevan texto legible: el texto se compone en post o se evita; el modelo lo deforma. [FUENTE: visual-prompt-forge/SKILL.md Rule 1]
8. Una multitud tiene densidad desigual: huecos, filas, cuerpos que se tapan; la retícula uniforme de cabezas es la firma del render. [A PRUEBA]

## 3. Cue de movimiento congelado por defecto

- Estadio o público estático: quietud con un solo elemento que cambia de estado, las manos en alto o el destello de miles de pantallas. [FUENTE: video/references/animatic-keyframes.md §5]
- Manifestación o maratón: la masa barrida en el sentido del flujo y un solo héroe o un solo objeto nítido en plano medio. [FUENTE: video/references/animatic-keyframes.md §4]
- Cada panel carga sus tres detalles aunque no haya rostro: presión ambiental de la masa, micro-acción en el héroe, motivo repetido en la multitud. [FUENTE: video/references/dramaturgy.md §2]

## 4. Luz en este medio

- Estadio nocturno: las torres de luz son los prácticos motivados y crean sombras múltiples y cortas; declararlas. [A PRUEBA]
- Las pantallas de teléfono en la gradería son un campo de speculares fríos y funcionan como motivo visual. [FUENTE: video/references/camera-lighting-vocabulary.md §4]
- Calle o manifestación de día: luz natural con una dirección; a contraluz la masa se convierte en siluetas y el polvo o el humo de bengala gana volumen. [FUENTE: video/references/race-and-speed.md §7]
- Concierto: una fuente escénica domina y el público queda como silueta con rim, el 70% del cuadro sin luz. [FUENTE: video/references/race-and-speed.md §7]

## 5. Cámara, ángulo y rig montable

- Ángulo high o aéreo para escala y patrón; low con la masa como muro para amenaza o presión; eye-level dentro de la masa solo con un héroe canonizado en plano medio. [FUENTE: video/references/animatic-keyframes.md §6]
- Rig montable: grúa, dron, cámara de gradería, cable cam sobre el campo; una cámara dentro de la multitud a la altura de los ojos sin cuerpos que la tapen es irreal. [FUENTE: video/references/race-and-speed.md §2]
- Larga focal para comprimir la masa y multiplicar su densidad aparente. [FUENTE: video/references/race-and-speed.md §3]
- Cámara implícita: un solo movimiento, tracking lateral sobre la masa o descenso lento desde el aire. [FUENTE: video/references/camera-lighting-vocabulary.md §2]

## 6. Modelo recomendado

- Nano Banana Pro con prompt en JSON cuando hay cinco o más elementos que coordinar: masa, héroe, prácticos, escenario, clima. [FUENTE: image/references/nano-banana.md]
- GPT Image 2 quality high si hay objetos del héroe con detalle fino; sin texto en pancartas. [FUENTE: image/references/gpt-image.md]
- Seedance 2.0 filtra rostros humanos de forma agresiva: en video de multitud eso ayuda, siempre que los héroes vayan por referencia en 2.5, 1.5 Pro, Kling o Veo. [FUENTE: video/references/seedance.md]
- Lugar real, estadio o plaza reconocibles: NB2 con image grounding para la placa. [FUENTE: image/references/nano-banana.md]

## 7. Tratamiento de personas dentro del régimen

- Máximo tres héroes con identidad, cada uno insertado con su referencia y su rol explícito, nunca en forma colectiva. [FUENTE: video/references/universal-rules.md U13]
- El crítico cuenta rostros legibles: cada uno debe corresponder a un héroe canonizado; el que no, se convierte en silueta, espalda o desenfoque mediante edición. [FUENTE: produccion-visual-sw30/SKILL.md R12]
- Posición de cada héroe por ancla legible de la imagen, un asiento, una línea del campo, una farola; nunca "left half". [FUENTE: produccion-visual-sw30/SKILL.md R2]
- Al animar, tres o más personajes distintos solo se sostienen si cada uno tiene su propio element o referencia; la masa no los tiene y por eso debe seguir sin rostro. [FUENTE: video/references/kling.md §7]

## 8. Fallos conocidos y su corrección

- Rostros legibles en la masa: editar a desenfoque o silueta, o regenerar la placa con contraluz. [FUENTE: produccion-visual-sw30/SKILL.md R12]
- Clones del héroe entre los extras: forzar diferenciación de ropa y pelo, pedir "no identical clones in the background". [FUENTE: video/references/fixes-and-skeletons.md §2]
- Retícula uniforme de cabezas: pedir densidad desigual y oclusiones. [A PRUEBA]
- Texto inventado en pancartas: quitar toda mención de texto del prompt y componer en post. [FUENTE: visual-prompt-forge/SKILL.md Rule 1]
- Multitud nítida y héroe borroso: la lógica de blur se invirtió; héroe nítido, masa barrida. [FUENTE: video/references/animatic-keyframes.md §4]

## 9. Checklist del crítico

- [ ] Ningún rostro legible que no sea un héroe canonizado. [FUENTE: produccion-visual-sw30/SKILL.md R12]
- [ ] Sin clones; densidad desigual. [FUENTE: video/references/fixes-and-skeletons.md §2]
- [ ] Tres planos con trabajos distintos. [FUENTE: video/references/animatic-keyframes.md §6]
- [ ] Barrido coherente con la dirección del flujo si la masa se mueve. [A PRUEBA]
- [ ] Sin texto legible en pancartas ni camisetas. [FUENTE: visual-prompt-forge/SKILL.md Rule 1]
- [ ] Máximo tres héroes, cada uno con referencia y rol. [FUENTE: video/references/universal-rules.md U13]
