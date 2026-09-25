---
familia: 09
nombre: Grupo ensamble
cubre: quinteto de cuerdas, grupo de K-pop, equipo titular, familia, banda, mesa directiva
d2_accion: [A_pose, E_interaccion, B_pico]
d3_sujetos: [ensamble]
d4_tratamiento: [documental, narrativo, comercial]
d8_modelo: [gpt-image-2, nano-banana-pro]
d9_angulo: [eye-level, low]
especializa: video/references/animatic-keyframes.md
estado_archivo: BORRADOR 2026-09-25
---

# Grupo ensamble

De tres a ocho personas y todas deben reconocerse en el mismo frame. Cada miembro es un héroe con
génesis propia, vestuario propio y, si toca, instrumento propio. El costo se cuenta antes: N miembros
son N génesis de rostro, N de cuerpo y N inserciones. Es lo contrario de la multitud anónima.

## 1. Cuándo cargar

- Cargar cuando tres o más personas del cuadro deben ser reconocibles y consistentes a lo largo de la pieza. [A PRUEBA]
- Si solo uno a tres necesitan identidad y el resto es masa, cargar `08-multitud-anonima.md`. [A PRUEBA]

## 2. Leyes físicas que el still debe evidenciar

1. Un solo trabajo por generación: un miembro por inserción, nunca el grupo completo desde texto. [FUENTE: produccion-visual-sw30/SKILL.md R1]
2. Cada miembro tiene génesis propia en dos pasos, rostro T1 sin referencia y cuerpo T2 con el rostro adjunto, canonizada con hash antes de cualquier cuadro de grupo. [FUENTE: produccion-visual-sw30/SKILL.md R11]
3. La placa del escenario se genera vacía y con anclas legibles de posición, atriles, marcas del escenario, baldosas, sillas, porque la posición de cada miembro se declara por ancla de la imagen, nunca por "left half". [FUENTE: produccion-visual-sw30/SKILL.md R2]
4. La inserción es secuencial: cada nuevo miembro se añade sobre la placa acumulada con "use only the person from image N, keep the world and the people already placed untouched". [FUENTE: produccion-visual-sw30/SKILL.md R7]
5. Toda comparación "same X" exige ambos referentes adjuntos en ese prompt: la autocontención vale para cada inserción. [FUENTE: produccion-visual-sw30/SKILL.md R4]
6. Cada referencia lleva rol explícito e individual: "Image 2 is member A, use only appearance, hair and outfit"; nunca la forma colectiva "images 2 to 6 define five members". [FUENTE: video/references/universal-rules.md U13]
7. Los instrumentos y props de cada miembro son objetos ancla: se canonizan y se heredan, con lateralidad correcta, violín sobre el hombro izquierdo, arco en la mano derecha, salvo zurdo declarado. [A PRUEBA]
8. Poses iguales están permitidas, K-pop o formación de equipo, pero las identidades deben distinguirse al zoom: pelo, cara, estatura, variante de vestuario; dos miembros indistinguibles son clones, no ensamble. [FUENTE: video/references/fixes-and-skeletons.md §2]

## 3. Cue de movimiento congelado por defecto

- Formación estática: quietud deliberada con spine central y simetría, el "breath frame"; un solo elemento cambia de estado, el arco a punto de tocar, la mano en alto. [FUENTE: video/references/animatic-keyframes.md §6]
- Coreografía en el pico: blur parcial en la extremidad que se mueve y torsos nítidos; un solo miembro en el pico máximo, los demás un instante detrás, para que no parezcan copias. [A PRUEBA]
- Romper la simetría cuando aparece el líder: el spine se desplaza y un miembro adelanta medio paso. [FUENTE: video/references/animatic-keyframes.md §6]

## 4. Luz en este medio

- Una sola dirección de luz para todos los miembros; la inserción secuencial obliga a repetir verbatim la cadena de iluminación en cada paso o los miembros se leen pegados. [FUENTE: visual-prompt-forge/references/consistency-locks.md Lock 3]
- Rostros con luz dura modelando y piel documental cuando el tratamiento es documental o narrativo; en comercial, clean lighting pareja, pero la misma para todos. [FUENTE: produccion-visual-sw30/SKILL.md template T1]
- Escenario: un práctico dominante, foco o ventana, y el resto en penumbra; el fondo aplastado ayuda a que N figuras no compitan. [FUENTE: video/references/race-and-speed.md §7]
- Instrumentos con specular: barniz, metal, cuerdas; sin specular no hay material. [FUENTE: video/references/race-and-speed.md §7]

## 5. Cámara, ángulo y rig montable

- Ángulo por defecto eye-level frontal o ligeramente low: todas las caras deben leerse; un ángulo extremo esconde rostros y anula el ensamble. [FUENTE: video/references/animatic-keyframes.md §6]
- La jerarquía se marca con altura y posición: el líder de pie o al centro del spine, los demás a los lados; el staging dice quién manda antes que cualquier gesto. [FUENTE: video/references/dramaturgy.md §6]
- Overhead solo para leer la coreografía como figura geométrica, y en ese plano se renuncia a la identidad. [A PRUEBA]
- Lente 35mm a 50mm a distancia suficiente para no deformar a los extremos; con larga focal los miembros del fondo se comprimen contra los del frente y se tapan. [FUENTE: video/references/camera-lighting-vocabulary.md §3]
- Eyelines coordinadas y declaradas: todos al director, todos a cámara, o cada uno a su instrumento; eyelines mezcladas sin intención se leen como error de continuidad. [FUENTE: visual-asset-critic/references/critique-rubric.md Layer 4]

## 6. Modelo recomendado

- GPT Image 2 acepta hasta dieciséis referencias con rol nombrado: es el modelo para un ensamble de más de cinco cuando se intenta una sola pasada. [FUENTE: image/references/gpt-image.md]
- Nano Banana Pro acepta hasta cinco referencias de personaje y NB2 hasta cuatro: por encima de ese número, subgrupos o inserción secuencial. [FUENTE: image/references/nano-banana.md]
- La regla de una sola pasada con todos los maestros adjuntos es inferencia hasta probarla: dieciséis referencias aceptadas no garantizan dieciséis identidades sostenidas; verificar miembro por miembro. [A PRUEBA]
- GPT Image 2 quality high para identidad y para partituras, logos de instrumento o UI, sin texto generado. [FUENTE: image/references/gpt-image.md]

## 7. Tratamiento de personas dentro del régimen

- Herencia mínima en cada inserción: "same face and clothes" del miembro más solo los deltas de pose; cero re-descripción de lo que la referencia ya muestra. [FUENTE: produccion-visual-sw30/SKILL.md R5]
- El crítico corre la capa de identidad una vez por miembro, cada rostro contra su maestro; un rostro sin maestro es REJECT, no REVISE. [FUENTE: visual-asset-critic/references/critique-rubric.md Layer 2]
- Manos e instrumentos con lateralidad nombrada en cualquier contacto, incluidos dos miembros que se tocan. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]
- Inspección al 100% de todos los rostros y manos antes de presentar; con N miembros son N inspecciones. [FUENTE: produccion-visual-sw30/SKILL.md R14]
- Lo aprobado se canoniza y se edita desde ahí; un miembro que falla se rehace solo su inserción, nunca el grupo entero. [FUENTE: produccion-visual-sw30/SKILL.md R11]

## 8. Fallos conocidos y su corrección

- Dos miembros convergen en la misma cara: cada uno con su propia referencia y forzar diferenciación de rasgos y ropa. [FUENTE: video/references/fixes-and-skeletons.md §2]
- Un miembro cambia de posición al insertar el siguiente: faltó "keep the people already placed untouched" y el ancla de posición. [FUENTE: produccion-visual-sw30/SKILL.md R7]
- Instrumento en la mano equivocada o dos manos derechas: nombrar lateralidad. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]
- La luz cambia entre miembros: repetir la cadena de iluminación verbatim en cada inserción. [FUENTE: visual-prompt-forge/references/consistency-locks.md Lock 3]
- En video, tres o más personajes se funden: un element o una referencia individual por miembro, nunca dos personajes con una sola descripción. [FUENTE: video/references/kling.md §7]

## 9. Checklist del crítico

- [ ] Cada rostro legible corresponde a un maestro canonizado; N rostros, N coincidencias. [FUENTE: visual-asset-critic/references/critique-rubric.md Layer 2]
- [ ] Ningún clon; identidades distinguibles al zoom aunque la pose sea igual. [FUENTE: video/references/fixes-and-skeletons.md §2]
- [ ] Una sola dirección de luz para todos. [FUENTE: visual-prompt-forge/references/consistency-locks.md Lock 3]
- [ ] Posiciones por ancla legible; nadie se movió entre inserciones. [FUENTE: produccion-visual-sw30/SKILL.md R2]
- [ ] Instrumentos y manos con lateralidad correcta. [FUENTE: visual-prompt-forge/SKILL.md Rule 6]
- [ ] Eyelines coordinadas según lo declarado. [FUENTE: visual-asset-critic/references/critique-rubric.md Layer 4]
