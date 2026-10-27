# Auditoría de los 410 textos que salieron del universo tras leerse uno por uno — 2026-10-27

**Por qué se hace.** Lo pide la pregunta de arranque 1. Al comprobar si los archivos que gobiernan los casos aprobados
(26 §16 y §17) están enteros en el universo, faltaba `gpt-image.md:96` (INV-002383). Es la plantilla de quitar objeto
para GPT Image 2 y salió del universo.

**Regla que se aplica** (Eric, 2026-10-24, 24 §1, `ESTADO_UNIVERSO.md:3–4`): entra todo texto relevante para crear
imágenes con cualquier modelo. Sale solo el que es relevante únicamente para modelos que no son GPT Image 2.

**Fuente.** `v3/universo/decision_textos.json` (1,914 decisiones, 410 «sale»), con el texto de la base
`corpus/BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite`, leídas una por una.

**Veredicto por texto:**
- **OK**: la salida cumple la regla.
- **ERROR**: el texto o una parte de él sirve también para GPT Image 2, así que debía entrar.

| Id | Documento:líneas | Motivo de salida | Veredicto |
|---|---|---|---|
| INV-000017, 000206, 000221, 000223, 000224, 000265–000267, 000439, 000449, 000453–000455, 000458, 000529, 000542, 000543, 000546 | flujos | fuentes de keyframe de NB y video; EN.7 video; NBP; Flux/MJ; NB2 Lite o gpt-image-1-mini; filas I2V de Kling, Veo, Seedance; modelo de rostro NB2/NBP; NB2 para arquitectura, especie y referencias; etiquetas de diagrama de NB | OK: cada texto solo nombra o enruta a otro modelo |
| INV-002003, 002013, 002196, 002227, 002276, 002990, 003296 | image/SKILL.md:22, :40–41; editing.md:5, :90; golden-rules.md:78; prompt-framework.md:4; text-rendering.md:5 | video; enlace a nano-banana.md; edición, materiales, costo y texto en NB | OK |
| INV-002383 | `gpt-image.md:96` | input_fidelity solo en gpt-image-1.5/1 | **ERROR**: «Remove [X]. Do not change anything else.» es la plantilla de quitar objeto de la sección «GPT Image 2 — Specific Rules › Edit-паттерны»; el mismo texto dice que en gpt-image-2 la fidelidad alta viene por defecto. Solo la cláusula `input_fidelity` es de 1.5/1. Gobierna el caso «edición: quitar objeto» (26 §16) |
| INV-002412 | `gpt-image.md:186` | gpt-image-1-mini | OK |
| INV-002531 | `multi-panel.md:162–164` | Borderless Grid: modelo NBP | **ERROR parcial**: L162 «Recommended size: 1536x1024 (landscape) — gives each cell enough resolution» es el tamaño de la plantilla 4×3 «Template (5-slot format)», no depende del modelo; L163 (NBP) sí es de otro modelo |
| INV-002593, 002755, 002789, 002796, 002849, 002856, 002910, 002940 | multi-panel.md:318; patterns | modelo recomendado NBP o NB2 | OK: solo la línea del modelo recomendado; la plantilla de cada patrón está en el universo |
| INV-011301–011303, 011305–011310 | visual-prompt-forge/SKILL.md:89–98 | adaptadores de otros modelos | OK |
| INV-012202–012205 | forge `examples/one-shot-all-adapters/gpt-image.txt:1–13` | ejemplo para gpt-image-1.5 | OK: ejemplo de otro modelo (sección 1344, ya decidida) |
| INV-012231–012236, 012238, 012243–012245, 012249–012251, 012266, 012291, 012298, 012304, 012305, 012311, 012315, 012318, 012411, 012414 | consistency-locks.md, failure-modes.md, prompt-anatomy.md | seed (no existe en GPT Image), --cref, omni-reference, referenceImages, sref, Flux, MJ e Ideogram | OK |
| INV-000294–000296, 000298–000300 | flujo-spot.html:1–11 | título y leyenda del mapa | OK: no son reglas |
| INV-000302–000357 (sin 000337–000342 ni 000358) | flujo-spot.html:14–124 | megaflujo: etapas de marca, estrategia, guion, dirección, storyboard, video y entrega | OK: rótulos del diagrama de etapas que no crean imagen |
| INV-000359–000391 | flujo-spot.html:128–192 | subprocesos de etapas que no crean imagen (E0 a E4.6) | OK: subprocesos de marca, estrategia, guion, dirección y shot planning. E4.4 «Nunca texto dentro de la descripción visual» es de `shots.json`; para la imagen ya está la regla del texto sobrepuesto que se compone aparte (`01_texto_en_imagen.md`) |
| INV-000402–000416 | flujo-spot.html:214–242 | subprocesos E6 video, E7 paquete, POST | OK: prompts de video, paquete, preview y postproducción. E6.6 (cabecera SKILL / RIESGOS / TÉCNICA) ya está en el plan por los hooks del repo (tarea 10) |
| INV-000499, 000500, 000518–000522 | flujo-spot.html:408–454 | herencia hacia el clip; video, NLE y spot | OK |
| INV-002420, 002421, 002423, 002428, 002463–002465, 002469 | models.md:9–66 | enrutamiento y costos de Nano Banana y gpt-image-1-mini | OK |
| INV-002890, 002897 | portrait-cinema.md:77, :97 | modelo recomendado NB2 / NBP | OK: solo la línea del modelo; la plantilla del patrón está en el universo |
| INV-005732 | on-screen-text.md:32 | campo rationale de `shots.json` | OK: la regla de reservar espacio negativo para el texto está en las líneas vecinas del universo; esta solo dice dónde se anota en el storyboard |
| INV-005794–005804 | shot-grammar.md:31–42 | movimiento de cámara | OK: video |
| INV-007991–008001 | animatic-keyframes.md:71–85 | densidad de paneles por beat | OK: planificación del animatic |
| INV-008063–008081 | animatic-keyframes.md:190–212 | tablero de animatic de 30 s | OK: tablero de tiempos, sonido y densidad de una secuencia de video; cada fila es una tarjeta de keyframe para animatic, no una regla de imagen fija independiente |
| INV-008093–008095 | animatic-keyframes.md:227–230 | celda de sonido, densidad, entrega al modelo de video | OK |
| INV-008130 | camera-lighting-vocabulary.md:39 | «locked-off frame» | OK: cámara fija de video |
| INV-008571–008574 | fixes-and-skeletons.md:90–98 | manos: negativos para Kling, frase positiva para Seedance y Veo | OK: cada instrucción nombra su modelo |
| INV-008575 | fixes-and-skeletons.md:100–102 | frase positiva de manos para Seedance y Veo | OK: la línea 98 la asigna a esos dos modelos |
| INV-009107 | race-and-speed.md:229 | orden de los beats rituales | OK: orden de una secuencia de video |
| INV-011394–011396, 011398–011403 | forge SKILL.md:324–333 | filas de adaptadores de otros modelos de imagen y de video | OK |
| INV-011431–011478, 011495–011518 (desde la línea 997 sigue) | `_capabilities.json:6–53`, `:70–93` | entradas de Midjourney, Flux, Ideogram, Nano Banana y Seedream en la matriz | OK: valores de cada modelo |
| INV-011519–011590 | `_capabilities.json:94–165` | Seedream, Kling, Veo, Seedance y Hailuo en la matriz | OK |
| INV-012182–012189, 012191, 012192, 012194, 012195 | forge `examples/one-shot-all-adapters/README.md:41–57` | salidas y sintaxis de otros modelos y de gpt-image-1.5 | OK |

**Control de cobertura.** Un script compara los ids de esta tabla con los 410 «sale» de `decision_textos.json`:
cubiertos 410 de 410, faltan 0, sobran 0.

## Resultado

408 OK y 2 ERROR.

| Id | Qué falta en el universo | Caso aprobado al que afecta |
|---|---|---|
| INV-002383 (`gpt-image.md:96`) | La plantilla de GPT Image 2 para quitar objeto: «Remove [X]. Do not change anything else.». La cláusula `input_fidelity: high` es de gpt-image-1.5/1 y no aplica; el mismo texto dice que en gpt-image-2 la fidelidad alta viene por defecto | edición: quitar objeto (26 §16) |
| INV-002531 (`multi-panel.md:162`) | «Recommended size: 1536x1024 (landscape) — gives each cell enough resolution», el tamaño de la plantilla 4×3 «Template (5-slot format)». L163 (NBP) sigue fuera | multipanel de fotos (F04, 26 §16) |

**Lo que no cubre esta auditoría** (`ESTADO_UNIVERSO.md` §5):
- 9,873 textos decididos por sección, sin leerlos uno por uno: 408 de secciones «otro_modelo» y 9,465 de secciones «fuera».
- Los textos de documentos que declaran su modelo y no nombran otro, que entraron sin leerse uno por uno.
