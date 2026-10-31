# Prueba completa con un caso real: caballo documental en la playa al atardecer (2026-10-31)

Orden de Eric: aplicar la propuesta completa. Esta prueba recorre la cadena entera, del pedido al prompt, con la
taxonomía canónica y los criterios de `4_diseno/CRITERIOS_CLASIFICACION.md`, antes de clasificar el corpus a escala.

Pedido: «una imagen documental de un caballo galopando en la playa al atardecer». Modelo: GPT Image 2.

## 1. El caso en valores de la taxonomía

| Faceta | Valor | Cómo se fijó |
|---|---|---|
| F10 Modo de generación | génesis sin referencias | El pedido no trae imagen |
| F29 Modelo · F35 Migración | GPT Image 2 · no | Alcance de la fase |
| F04 Tipo de pieza | Pieza única | El pedido no nombra pieza; ver hallazgo H3 |
| F06 Formato | 3:2 | Supuesto declarado en las notas de salida; el brief debe preguntarlo |
| F15 Sujeto · F19 Número | animal · 1 | Caballo |
| F13 Acción · F14 Régimen | C movimiento continuo · 06 cuerpo en esfuerzo | Galopando |
| F16 Espacio | exterior | Playa; no hay tipo «playa» |
| Luz · Momento del día | atardecer | |
| F17 Estilo · F18 Técnica | documental · fotorrealista | |
| F32 Texto · F33 Complejidad · F23 Referencias | sin texto · simple · ninguna | |
| F24 Plano · F25 Ángulo | WS wide · eye-level | Supuesto declarado; el brief debe preguntarlo |
| F20, F21, F22 (personas) | ninguna · no · sin valor que encaje | Ver hallazgo H4 |

## 2. Qué se leyó

Los 1,511 textos del universo de la fase (decisión del 23 de octubre §1), completos, documento por documento:
1,379 textos distintos y 132 copias. Registro por documento y sección en
`6_mapa/lecturas/universo_imagen_piloto_caballo_20261031.md`.

## 3. Reglas que aplican al caso

Aplican 138 textos. Por cómo entran al prompt:

| Cómo entra | Qué reglas | Textos (ejemplos) |
|---|---|---|
| Template de GPT Image 2 (una vez, para todo caso) | 5 slots con etiquetas; sin constraints el modelo deriva; anti-slop (sin elogios vagos, sin etiquetas de estilo, sin lenguaje de ánimo); 150–300 palabras; sin listas con comas; lenguaje espacial; máximo 5 elementos; «50mm feel» solo como look; sin --ar; modelo y calidad como meta junto al prompt; formato de salida Model / Quality / Size / Prompt / Notes | INV-002334, 002335, 002336, 002343–002346, 011735, 011756–011760, 002453, 002470, 002044 |
| Template de todos los modelos | Ser específico (sujeto, material, posición); decir cómo se ilumina; decir de qué está hecho el sujeto; encuadre positivo; contexto de uso | INV-002255–002260, 002087, 002141, 002243, 002262 |
| Inserción mecánica (F18 fotorrealista, F06) | Claves del tipo fotorrealista: luz, materiales, atmósfera; cierre «natural … texture, no AI rendering artifacts»; quality high para fotorrealismo; tamaño horizontal 1536×1024 | INV-002997, 011743, 002468, 002362 |
| Selección | Ángulo, plano, foco, película o grade, ancla de conocimiento del mundo, modo de detalle, señales de movimiento («slight motion blur on trailing…»), motion blur específico | INV-002112–002124, 002127–002139, 002299–002318, 003022–003027, 003080, 002550 |
| Ejemplos | Hora dorada a contraluz con sombras largas; «Mood: authentic, documentary style» | INV-002094, 003042 |

Reglas propias de los valores del caso dentro del universo: casi ninguna. Atardecer y hora dorada solo aparecen en
ejemplos; documental, solo en un ejemplo; animal, solo en que GPT Image 2 no hace grounding de especies (INV-002434);
galope, solo en señales de movimiento. Ver hallazgo H1.

## 4. Prompt resultante

Template: GPT2-GEN de `4_diseno/templates/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md` (5 slots, parámetros
aparte). 230 palabras; no contiene «photorealistic».

```text
Model: gpt-image-2
Quality: high
Size / Ratio: 1536×1024 (3:2)

Prompt:
Scene: A wide, empty sandy beach at sunset. The sun sits just above the horizon behind the subject, and the low surf and the wet sand along the waterline reflect the warm sky. Open sea and a clean horizon fill the background.
Subject: One horse galloping along the waterline from left to right, caught mid-stride with one foreleg reaching forward and the hind legs driving off the sand, mane and tail streaming back with the speed.
Important Details: Low, hard sunlight from behind the horse rims its mane, back and ears in warm gold and throws a long shadow across the wet sand toward the camera; there is no fill light, so the near flank falls into soft shadow. Wet sand and spray kicked up by the hooves catch the backlight. Slight motion blur only on the lower legs and the flying sand; the head and eye stay sharp. Wide shot at eye level, 50mm feel, slightly handheld framing; the horse sits in the left third and moves toward open space on the right. Real coat texture with sand on the legs and fine visible film grain across the frame.
Use Case: documentary photograph of a single unstaged moment.
Constraints: one horse only, no rider, no saddle or tack, no people, no text, no watermarks, no glamorization, no heavy retouching, no studio gloss, natural coat texture, no AI rendering artifacts.

Notes:
- Supuestos: formato 3:2, plano general a la altura de los ojos, caballo sin jinete, pieza suelta.
```

De dónde sale cada parte:
- **Atardecer:** sol bajo detrás del sujeto, contraluz cálida en el borde, sombra larga hacia cámara (INV-002094).
- **Documental:** la definición de F17 en la taxonomía (luz dura, sin relleno, grano de reportaje, cámara en mano) y las
  restricciones sin glamour ni retoque (INV-002400).
- **Galope:** desenfoque solo en patas y arena, cabeza nítida (INV-002550, 003080).
- **Cierre:** «natural … texture, no AI rendering artifacts» (INV-011743), con «coat» en lugar de «skin» porque el
  sujeto es un animal; es una interpretación.

## 5. Qué tan bien funcionó el nivel 2

De los 138 textos que aplican, 131 están en las secciones 2.1 (generales) y 2.2 (por modelo). Los otros 7 están en 2.11
(4, las secciones de primer nivel de `skills/image/SKILL.md`), 2.3 (1), 2.5 (1) y 2.9 (1). Buscar solo en 2.1 y 2.2
habría perdido el formato de salida (INV-002044) y la regla del motion blur (INV-002550).

Corrección del 2026-10-31 (P-27): con las secciones de primer nivel de `skills/image/SKILL.md` ya separadas, esos 4 textos
quedan en 2.1, y 2.1 más 2.2 cubren 135 de los 138.

## 6. Hallazgos

| # | Hallazgo | Quién lo resuelve | Propuesta |
|---|---|---|---|
| H1 | El universo de la fase casi no tiene reglas para documental, animal, movimiento continuo ni atardecer. Esas reglas están en `flujos/flujo-anclas.html` (preset documental, familias de régimen), `skills/visual-media/SKILL.md` (fundamentos de fotografía) y `skills/video/references/race-and-speed.md` (vender velocidad en un cuadro), fuera del universo del 23 de octubre | Eric | Ampliar el universo con flujo-anclas y visual-media, de donde salen las definiciones de F13, F14 y F17 |
| H2 | Calidad de GPT Image 2 contradictoria: medium por defecto (INV-002351), empezar en low (INV-002353), high para fotorrealismo (INV-002468), high en hero y medium en series (INV-011729) | Eric | high cuando F18 es fotorrealista; medium en los demás casos |
| H3 | F04 no tiene un tipo de pieza para una foto suelta documental, y el slot Use Case lo necesita | Eric | Llenar Use Case con F17 cuando F04 es «Pieza única» |
| H4 | F20, F21 y F22 son facetas de personas; con un sujeto animal, F22 no tiene valor que encaje y no se permite «no aplica» | Eric | Que F20 a F22 se fijen solo cuando F15 es persona |
| H5 | Hora dorada y atardecer no tienen definición en la §3.6 y se solapan | Eric | Atardecer: sol en el horizonte y justo después; hora dorada: la hora previa con sol bajo. Al pedir atardecer, las reglas de hora dorada entran por selección |
| H6 | En la precatalogación, las secciones de primer nivel de `skills/image/SKILL.md` quedaron dentro de «texto antes del primer encabezado» (2.11) | Agente | Corregir el CSV y revisar si otros documentos tienen el mismo problema |
| H7 | Los adaptadores dan dos sintaxis para GPT Image (5 slots y 3 párrafos) | Resuelto | El template GPT2-GEN ya fija 5 slots para GPT Image 2 |

## 7. Lo que no se hizo y por qué

El catálogo de casos (P-19) no se regeneró: H1, H3, H4 y H5 pueden cambiar la taxonomía, y regenerarlo antes obligaría a
hacerlo dos veces. Se regenera en cuanto Eric resuelva esos cuatro hallazgos.

## 8. Resultado de la generación (Eric, 2026-10-31) y corrección

Eric generó la imagen: el caballo sale **al trote**, no al galope. Causa: el prompt describía las patas de forma ambigua
(«una mano adelante y los posteriores impulsando»), que el modelo resolvió como trote; y el universo no tiene ninguna
regla sobre la marcha de los animales (hallazgo H8). Eric aportó la biomecánica del galope (registrada en
`5_decisiones/DECISIONES_ERIC_20261031.md`, punto 4): aire asimétrico de tres tiempos seguido de una fase de suspensión
con las cuatro extremidades en el aire.

Corrección: el prompt fija una sola fase del tranco, la que no se confunde con el trote (la suspensión, con las patas
reunidas bajo el cuerpo), nombra la mano de galope y excluye los bípedos diagonales del trote. 282 palabras.

```text
Model: gpt-image-2
Quality: high
Size / Ratio: 1536×1024 (3:2)

Prompt:
Scene: A wide, empty sandy beach at sunset. The sun sits just above the horizon behind the subject, and the low surf and the wet sand along the waterline reflect the warm sky. Open sea and a clean horizon fill the background.
Subject: One horse at full gallop on the right lead, moving left to right along the waterline, shown at the suspension phase of the stride: all four hooves are off the sand at the same instant, the legs gathered under the belly, the hind legs swinging forward beneath the body and the forelegs folded back, head and neck stretched forward, mane and tail streaming back.
Important Details: Low, hard sunlight from behind the horse rims its mane, back and ears in warm gold and throws a long shadow on the wet sand directly beneath and toward the camera, separated from the hooves to show the horse is airborne. No fill light; the near flank falls into soft shadow. Sand kicked up by the last hoof hangs in the backlight. Slight motion blur only on the lower legs and flying sand; the head and eye stay sharp. Wide shot at eye level, 50mm feel, slightly handheld framing; the horse sits in the left third, moving toward open space on the right. Real coat texture and fine visible film grain.
Use Case: documentary photograph of a single unstaged moment.
Constraints: three-beat gallop with a moment of suspension, never a trot: no diagonal pairs of legs moving together, no hoof touching the ground; one horse only, no rider, no saddle or tack, no people, no text, no watermarks, no glamorization, no heavy retouching, no studio gloss, natural coat texture, no AI rendering artifacts.
```

| # | Hallazgo | Quién lo resuelve | Propuesta |
|---|---|---|---|
| H8 | El corpus no tiene reglas de marcha animal; el prompt ambiguo produjo trote | Eric | Que el aporte de Eric sobre el galope entre como regla de selección para sujeto animal (caballo) con acción de movimiento continuo, y que el prompt fije siempre una fase concreta del movimiento |

## 9. Prompt con la herramienta de investigación del movimiento (decisión 6)

Las dos búsquedas del caso (anatomía y mecánica del galope), sus fuentes y el prompt resultante están en
`4_diseno/HERRAMIENTA_INVESTIGACION_MOVIMIENTO.md` §4. Corrección al §8: «three-beat gallop» era incorrecto en inglés;
según la fuente, el galope rápido es de cuatro tiempos y el de tres es el canter. El prompt nuevo dice «galloping» y fija
la fase de suspensión con las patas dobladas, que es común a los dos.

## 10. Cobertura del prompt frente a las 138 reglas del universo (pregunta de Eric)

El prompt de la herramienta de movimiento no cubría todo lo que aplica del universo. Faltaba:

| Regla del universo | Qué faltaba | Corrección |
|---|---|---|
| INV-002049, 002259: colores en hex | El prompt no daba ningún color en hex | Cielo de #E8894A a #3E5A78; borde de luz #F2B35B |
| INV-002262–002265, 003010: contexto de uso | Use Case sin para qué ni para quién | «documentary photograph for an editorial feature» |
| INV-002121–002124: foco | No decía la profundidad de campo | Cabeza y ojo nítidos, horizonte algo suave |
| INV-002127–002139: grade | Solo decía grano; no el tratamiento de color | «natural true-to-life color» |
| INV-002400: Photoreal Editorial (desgaste, imperfecciones, «no studio gloss») | Se había quitado «no studio gloss»; no había rastro real en la superficie | Huellas en la arena mojada; «no studio gloss» de vuelta |
| INV-002044, 003036: Notes con supuestos | La última entrega no traía Notes | Notes de vuelta |

Lo que no se cubre porque depende de decisiones de Eric: universo sin reglas de documental, animal y movimiento (P-22),
calidad (P-23), F04 (P-24), F20–F22 (P-25) y definición de atardecer (P-26).

Prompt corregido (GPT Image 2, 276 palabras):

```text
Model: gpt-image-2
Quality: high
Size / Ratio: 1536×1024 (3:2)

Prompt:
Scene: A wide, empty sandy beach at sunset. The sun sits just above the horizon behind the subject; low surf and wet sand at the waterline reflect a sky graded from amber #E8894A to dusk blue #3E5A78. Hoofprints trail behind in the wet sand.
Subject: One horse galloping on the right lead, left to right along the waterline, at the suspension phase of the stride: the leading right foreleg has just pushed off and all four hooves are in the air at once, every leg bent, the hind legs swinging forward under the belly and the forelegs folded at the knees, head and neck stretched forward, mane and tail streaming back.
Important Details: Hindquarters bunched, hamstring muscles flexing the stifles; along the neck the brachiocephalic muscle draws the forelegs forward; lower-leg tendons taut. Low, hard backlight rims the mane, back and ears in warm gold #F2B35B; the shadow on the wet sand sits apart from the hooves. No fill light; the near flank falls into soft shadow. Sand from the last hoof hangs in the light. Slight motion blur only on the lower legs; head and eye sharp, horizon slightly soft. Wide shot at eye level, 50mm feel, slightly handheld; horse in the left third. Real coat texture, natural true-to-life color, fine film grain.
Use Case: documentary photograph for an editorial feature, a single unstaged moment.
Constraints: a gallop with every leg bent in the air, never a trot: no diagonal leg pairs, no outstretched legs, no hoof on the sand; one horse only, no rider, no tack, no people, no text, no watermarks, no glamorization, no heavy retouching, no studio gloss, no AI rendering artifacts.

Notes:
- Supuestos: formato 3:2; plano general a la altura de los ojos; sin jinete; colores hex y uso editorial elegidos por el agente.
```
