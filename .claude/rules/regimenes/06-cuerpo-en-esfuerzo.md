---
familia: 06
nombre: Cuerpo en el pico de esfuerzo
cubre: corredor rompiendo la cinta de llegada, salto en el apex, golpe en el impacto, levantamiento en el punto muerto, remate, sprint
d2_accion: [B_pico, C_movimiento]
d3_sujetos: [1, 2_contacto, ensamble]
d4_tratamiento: [documental, narrativo, comercial]
d8_modelo: [gpt-image-2, nano-banana-2, nano-banana-pro]
d9_angulo: [low, eye-level]
especializa: video/references/animatic-keyframes.md
estado_archivo: BORRADOR 2026-09-25
---

# Cuerpo en el pico de esfuerzo

Aquí el cuerpo humano es el objeto que cambia de estado. A diferencia de los regímenes sin rostro,
el rostro suele estar presente y visible, así que el template de piel documental de SW30 aplica
íntegro, sumado a la ley de los tres detalles.

## 1. Cuándo cargar

- Cargar cuando el beat es el instante de máximo esfuerzo o el cruce de un umbral físico por una persona: cinta de llegada, apex de un salto, impacto de un golpe, punto muerto de un levantamiento. [A PRUEBA]
- Si hay un objeto impulsado, cargar además `04-objeto-balistico.md`; si hay público detrás, `08-multitud-anonima.md`. [A PRUEBA]

## 2. Leyes físicas que el still debe evidenciar

1. Boardear el estado posterior del umbral: la cinta ya rota y volando, el pie ya despegado, el guante ya hundido en el saco; un corredor a un paso de la cinta intacta es setup, no impacto. [FUENTE: video/references/animatic-keyframes.md §5]
2. La fase de contacto con el suelo debe ser coherente con la velocidad: en sprint un solo pie toca o ninguno, en el apex del salto ninguno, en el punto muerto del levantamiento los dos plantados y cargados. [A PRUEBA]
3. La emoción se traduce a cuerpo, nunca se nombra: mandíbula trabada, venas como cordones, dedos abiertos, cuello tenso; entre dos y cuatro señales observables, más es sobreactuación. [FUENTE: video/references/universal-rules.md U3]
4. El sudor se describe como puntos speculares discretos bajo luz dura, no como piel mojada uniforme. [FUENTE: video/references/race-and-speed.md §7]
5. El golpe se lee en lo golpeado: el saco ondula en el punto de impacto, la cinta se tensa antes de romper, la barra se flexiona en el punto muerto. [FUENTE: image/references/patterns/poster-illustration.md]
6. El aire frío hace visible la respiración; declararlo solo si la escena lo justifica y como una única presión ambiental. [FUENTE: video/references/dramaturgy.md §9]
7. La ropa técnica se comporta como tela bajo fuerza: pliegues en el codo, tirón en el hombro, peso en el dobladillo. [FUENTE: image/references/prompt-framework.md]

## 3. Cue de movimiento congelado por defecto

- Cue por defecto en la llegada: blur parcial congelado, la cinta y los pies en barrido leve, el torso y el rostro tack-sharp. [FUENTE: video/references/animatic-keyframes.md §4]
- Cue por defecto en el apex: quietud deliberada en el punto más alto, cero blur, el cuerpo en la única postura que puede resolverse hacia abajo. [FUENTE: video/references/animatic-keyframes.md §4]
- Cue por defecto en sprint lateral: atleta nítido y carril barrido con las líneas del suelo como varillas de luz. [FUENTE: video/references/animatic-keyframes.md §4]
- Cada shot carga tres detalles: presión ambiental, micro-acción del cuerpo, motivo o ancla sonora prompteada como consecuencia física. [FUENTE: video/references/dramaturgy.md §2]

## 4. Luz en este medio

- Rostros con luz dura rasante y sin relleno: los poros proyectan sombra; la luz suave de softbox produce el look plástico y está prohibida en rostros. [FUENTE: produccion-visual-sw30/SKILL.md template T1]
- Piel documental con defectos concretos: rojeces, sudor, pigmento desigual, labios agrietados; nunca "imperfecciones sutiles". [FUENTE: produccion-visual-sw30/SKILL.md template T1]
- Stock documental de reportaje; Portra suaviza la piel y está prohibido en rostros. [FUENTE: produccion-visual-sw30/SKILL.md template T1]
- Un side light duro a 45 grados sobre la mano o el hombro que decide, fondo aplastado. [FUENTE: video/references/race-and-speed.md §7]
- En estadio nocturno, las torres de luz son los prácticos motivados y producen sombras múltiples cortas; declararlas o el modelo pone una sola sombra larga de estudio. [A PRUEBA]

## 5. Cámara, ángulo y rig montable

- Ángulo por defecto low: el cuerpo en el pico se lee como fuerza contra cielo o gradería; eye-level para la paridad de un duelo. [FUENTE: video/references/animatic-keyframes.md §6]
- Larga focal desde el final de la pista para comprimir al corredor contra la cinta y contra los rivales, con las líneas del carril como leading lines. [FUENTE: video/references/race-and-speed.md §3]
- Rig montable: cámara de foto de meta a nivel de la cinta, cable cam sobre el carril, cámara robótica en la línea; nunca una cámara flotando frente al atleta a media pista. [FUENTE: video/references/race-and-speed.md §2]
- Cámara implícita: freeze frame en la rotura, o push-in que termina en la mandíbula. [FUENTE: video/references/dramaturgy.md §7]

## 6. Modelo recomendado

- GPT Image 2 quality high para piel, identidad y textura de tela. [FUENTE: image/references/models.md]
- Rostros: probar NB2 y NBP, NBP a veces sostiene peor los rostros. [FUENTE: image/references/nano-banana.md]
- Prompt de unas 250 palabras cuando hay rostro, con los bloques light_hard, skin_doc, usecase_doc y clean_doc; un slot de más de 300 palabras compite consigo mismo. [FUENTE: produccion-visual-sw30/SKILL.md template T1]
- Cinta, dorsal y patrocinadores sin texto ni logo generado; se componen en post. [FUENTE: visual-prompt-forge/SKILL.md Rule 1]

## 7. Tratamiento de personas dentro del régimen

- El maestro de rostro se genera en reposo y seco; el cuadro de esfuerzo se inserta con referencia y solo describe los deltas: sudor, tensión, boca abierta. [FUENTE: produccion-visual-sw30/SKILL.md R5]
- La cara irregular y asimétrica es la que se lee real; la simétrica es maniquí, más aún bajo esfuerzo. [FUENTE: produccion-visual-sw30/SKILL.md template T1]
- Dos atletas en contacto, tackle o abrazo de meta: un sujeto por generación, el contacto lo fija el keyframe aprobado, manos nombradas. [FUENTE: produccion-visual-sw30/SKILL.md R9]
- Rivales detrás del ganador: si necesitan identidad, ensamble; si no, figuras barridas sin rostro legible. [FUENTE: video/references/animatic-keyframes.md §7]
- Inspección al 100% de rostro y manos antes de presentar. [FUENTE: produccion-visual-sw30/SKILL.md R14]

## 8. Fallos conocidos y su corrección

- Cinta intacta con el corredor ya pasado: falta el estado posterior; describir la cinta rota y volando desde el pecho. [FUENTE: video/references/animatic-keyframes.md §5]
- Dos pies plantados en pleno sprint: declarar la fase de zancada. [A PRUEBA]
- Expresión "determinada" o "intensa": emoción nombrada sin cuerpo; sustituir por las señales físicas. [FUENTE: video/references/dramaturgy.md §2]
- Piel plástica bajo esfuerzo: luz demasiado suave o stock equivocado; volver a light_hard y skin_doc. [FUENTE: produccion-visual-sw30/SKILL.md template T1]
- Sombra única de estudio en estadio nocturno: declarar las torres y las sombras múltiples. [A PRUEBA]

## 9. Checklist del crítico

- [ ] Estado posterior del umbral visible. [FUENTE: video/references/animatic-keyframes.md §5]
- [ ] Fase de contacto con el suelo coherente. [A PRUEBA]
- [ ] Dos a cuatro señales corporales, ninguna emoción nombrada. [FUENTE: video/references/universal-rules.md U3]
- [ ] Piel documental bajo luz dura, sudor como speculares. [FUENTE: produccion-visual-sw30/SKILL.md template T1]
- [ ] Rostro y manos correctos al 100%. [FUENTE: produccion-visual-sw30/SKILL.md R14]
- [ ] Sin texto ni logos en cinta o dorsal. [FUENTE: visual-prompt-forge/SKILL.md Rule 1]
