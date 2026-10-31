# Herramienta de investigación del movimiento y bloque «Acción» del prompt

Orden de Eric (2026-10-31, decisión 6): para imágenes de acción (deportes, máquinas, vehículos y animales en
movimiento) se hacen dos búsquedas en internet: la anatomía específica del sujeto y la mecánica del movimiento. Las dos
se agregan al prompt: la anatomía del movimiento (la parte o los músculos específicos que se mueven) y la mecánica (el
movimiento que realizan).

## 1. Cuándo se activa

Por inserción mecánica, sin selección, en cuanto el caso fija cualquiera de estos valores:

| Faceta | Valores que la activan |
|---|---|
| F13 Tipo de acción | B instante pico · C movimiento continuo · G acuática en superficie · H subacuática |
| F14 Régimen físico | 01 agua en superficie · 02 ruptura de superficie · 03 subacuático · 04 objeto balístico · 05 vehículo · 06 cuerpo en esfuerzo |

Vale para cualquier sujeto de F15 (persona, animal, objeto, vehículo, producto) y para cualquier modelo.

## 2. La herramienta: dos búsquedas por caso

| Búsqueda | Qué se busca | Resultado que entrega |
|---|---|---|
| B1 Anatomía | La anatomía específica del sujeto concreto (especie, deporte y cuerpo, máquina o vehículo): las partes, músculos, articulaciones o componentes que intervienen en ese movimiento | Lista de partes con su función en el movimiento, con fuente |
| B2 Mecánica | Cómo es ese movimiento: secuencia, fases, apoyos, posiciones y qué no debe confundirse con él (otra marcha, otra fase) | Secuencia de fases, la fase elegida para la imagen y sus rasgos visibles, con fuente |

Reglas de la herramienta:
1. **Fuentes:** primero revistas científicas, manuales técnicos o reglamentos del deporte, y enciclopedias; nunca redes
   sociales. Cada dato lleva URL y la frase literal de la fuente.
2. **Lectura:** se lee completa la parte de la fuente que trata el movimiento; no basta el extracto del buscador.
3. **Una sola fase:** la imagen fija muestra una fase concreta del movimiento, elegida por ser la que mejor se reconoce y
   la que no se confunde con otro movimiento. Se dice cuál y por qué.
4. **Lo que aporte Eric manda** sobre lo que digan las fuentes.
5. **Registro:** la investigación de cada caso queda en el repo, con sus fuentes, antes de entregar el prompt.

## 3. El bloque «Acción» del prompt

| Campo | Qué lleva |
|---|---|
| Mecánica | El movimiento en la fase elegida: qué extremidades o piezas están dónde, qué toca el suelo y qué no, hacia dónde va la energía |
| Anatomía del movimiento | Las partes o músculos concretos que se ven trabajando en esa fase y qué hacen |
| Exclusión | El movimiento con el que se confunde, nombrado para excluirlo (por ejemplo, el trote frente al galope) |

Lugar en cada template:
- **GPT Image 2 (5 slots):** la mecánica va en Subject; la anatomía, en Important Details; la exclusión, en Constraints.
- **Modelos de prosa** (Nano Banana, Flux y otros): en la frase de sujeto y acción, en el estilo del modelo.
- **Longitud:** el prompt respeta el techo del modelo (GPT Image 2: 150 a 300 palabras). Si no cabe, se recortan detalles
  de ambiente antes que el bloque.

## 4. Ejemplo: caballo al galope en la playa al atardecer

**B2 Mecánica** (Wikipedia, «Horse gait», sección *Canter and gallop*, https://en.wikipedia.org/wiki/Horse_gait):
- «The gallop is very much like the canter, except that it is faster … at high speeds, the three-beat sequence is split
  at the second stage into two footfalls, making it a four-beat gait.»
- «Then both gaits end with the striking off of the leading leg, followed by a moment of suspension when all four feet
  are off the ground.»
- «When all four feet are off the ground in the suspension phase of the gallop, the legs are bent rather than extended
  … when the legs are stretched out, at least one foot is still in contact with the ground.»
- Fase elegida: la suspensión, con las patas dobladas. No se confunde con el trote, que mueve las patas en pares
  diagonales.

**B1 Anatomía** (Payne, Hutchinson, Robilliard, Smith y Wilson, «Functional specialisation of pelvic limb anatomy in
horses», *Journal of Anatomy* 206, 2005, https://pmc.ncbi.nlm.nih.gov/articles/PMC1571521/; Payne, Veenman y Wilson,
«The role of the extrinsic thoracic limb muscles in equine locomotion», *Journal of Anatomy* 205, 2004,
https://pmc.ncbi.nlm.nih.gov/articles/PMC1571391/):
- Isquiotibiales (bíceps femoral, semitendinoso, semimembranoso): «Extension and abduction of hip during stance, flexion
  of stifle and extension of hock during swing».
- «The only extrinsic muscles capable of doing the work of protraction were brachiocephalicus, omotransversarius»: son
  los que llevan la mano hacia adelante.
- La protracción de la mano es en gran parte pasiva, «a catapult mechanism, in which energy is stored … in elastic
  tissues … during limb loading but is released quickly at toe-off».

**Aporte de Eric** (decisiones del 31-oct, punto 4): secuencia de apoyos del galope a la derecha y fase de suspensión;
manda sobre las fuentes.

**Prompt** (GPT Image 2, 276 palabras):

```text
Model: gpt-image-2
Quality: high
Size / Ratio: 1536×1024 (3:2)

Prompt:
Scene: A wide, empty sandy beach at sunset. The sun sits just above the horizon behind the subject; the low surf and the wet sand at the waterline reflect the warm sky. Open sea and a clean horizon fill the background.
Subject: One horse galloping on the right lead, left to right along the waterline, at the suspension phase of the stride: the leading right foreleg has just pushed off and all four hooves are in the air at once, every leg bent, the hind legs swinging forward under the belly and the forelegs folded at the knees, head and neck stretched forward, mane and tail streaming back.
Important Details: Hindquarters bunched, hamstring muscles flexing the stifles as the hind legs swing forward; along the neck the brachiocephalic muscle draws the forelegs forward; lower-leg tendons taut. Low, hard sunlight from behind rims the mane, back and ears in warm gold; the shadow on the wet sand sits apart from the hooves, showing the horse airborne. No fill light; the near flank falls into soft shadow. Sand from the last hoof hangs in the backlight. Slight motion blur only on the lower legs; head and eye sharp. Wide shot at eye level, 50mm feel, slightly handheld; horse in the left third. Real coat texture, fine film grain.
Use Case: documentary photograph of a single unstaged moment.
Constraints: a gallop with every leg bent in the air, never a trot: no diagonal pairs of legs moving together, no straight outstretched legs, no hoof touching the sand; one horse only, no rider, no tack, no people, no text, no watermarks, no glamorization, no heavy retouching, no AI rendering artifacts.
```
