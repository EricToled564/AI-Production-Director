# Taxonomía de clasificación para imágenes — PROPUESTA para aprobación de Eric

Vale igual para cualquier modelo. La clasificación se hace modelo por modelo (hoy GPT Image 2) con el valor de F29 de cada texto.
Armada solo con: (1) la clasificación que Eric definió al empezar esta etapa; (2) los nombres de los documentos del corpus y sus encabezados, asignados a las categorías de la taxonomía; (3) el catálogo de casos de uso, en su orden de general a específico; (4) las categorías de la taxonomía actual, tal cual, más las extensiones que Eric aprobó el 23 y el 26 de octubre. Los 1,369 términos del tesauro no se copian: no son categorías (la taxonomía actual los define como etiquetas que cuelgan de las categorías).

## Nivel 1 · Qué hace el texto con el prompt

Todas las categorías se definen por su efecto en el prompt.

### 1.1 ¿Impacta la redacción?

| Valor | Definición |
|---|---|
| Impacta | El texto dice qué se escribe, o qué no se escribe, en el prompt |
| No impacta | El prompt queda igual con o sin el texto; se clasifica solo por lo que es (1.4) |

### 1.2 Si impacta: efecto

Qué le hace el texto al prompt. Un texto puede tener varios efectos; se marcan todos.

| Valor | Definición | Incluye | No incluye |
|---|---|---|---|
| Agrega contenido | Pide que se escriba algo de la imagen: sujeto, acción, escena, detalles, estilo visual, luz, color, materiales, texto que debe aparecer, términos de calidad | Las frases que describen la imagen, incluido su estilo visual | Cómo se redacta el prompt (eso es «fija la forma») |
| Fija la forma | Fija cómo se redacta el prompt: apartados, formato, etiquetas, sintaxis, longitud, estilo de redacción, cómo se nombran las referencias adjuntas | La estructura y la manera de escribir | El estilo visual de la imagen (eso es «agrega contenido») |
| Establece un orden | Fija en qué orden van los bloques o los elementos del prompt | Orden de apartados y de elementos | — |
| Fija restricciones | Excluye palabras o elementos, o fija lo que no debe cambiar | Prohibiciones, exclusiones, prompt negativo, lo que se preserva en una edición | — |
| Fija un parámetro | Fija un valor técnico de la generación fuera de la descripción | Modelo, calidad, tamaño, ratio, fondo transparente, formato de salida | Lo que se describe dentro del prompt |
| Da un ejemplo o una plantilla | Da una frase, un prompt o una plantilla con huecos que sirve de modelo | Ejemplos, plantillas, opciones de redacción | — |

### 1.3 Si impacta: cómo entra al prompt

Decide el destino de la regla. Solo lo que necesita interpretación pasa por selección.

| Valor | Cuándo | Destino | Uso operativo |
|---|---|---|---|
| Template | No depende de ningún dato del caso, o depende solo del modelo o de la operación. Si su forma cambia según el modelo, cada template la lleva en la forma de su modelo | Instrucción de llenado en el template de cada modelo, o en el de ese modelo u operación. Se usa una vez y no se vuelve a seleccionar. El template guarda la instrucción, no copia texto a cada prompt, para que el prompt siga siendo corto | INCORPORADA A TEMPLATE |
| Inserción mecánica | Su condición se resuelve con datos de lista cerrada del caso (tipo de pieza, sujeto, operación de edición, técnica, texto en la imagen, etc.), uno o varios | Se inserta en el prompt sin selección en cuanto el caso fija esos datos | INSERCIÓN MECÁNICA |
| Biblioteca de plantillas | Es la plantilla de un look concreto | Se ofrece por tipo de pieza y estilo; el usuario confirma como máximo una y se inserta | BIBLIOTECA DE PLANTILLAS |
| Selección | Su condición depende de un valor abierto (número, edad, posición, texto literal) o necesita interpretar el caso | Se selecciona caso por caso | ACTIVO EN SELECCIÓN |

### 1.4 Si no impacta: qué es

| Valor | Definición |
|---|---|
| Rótulo o encabezado | Título, subtítulo o rótulo que solo nombra lo que sigue |
| Descripción o explicación | Dice qué es o qué hace la skill, el documento o un método, sin decir qué escribir |
| Condición de uso de una plantilla | Dice para qué casos sirve una plantilla; se usa para ofrecerla en la biblioteca, no para escribir |
| Control o validación | Revisión, gate o comprobación que se hace después de escribir |
| Código o herramienta | Código, script, esquema o instrucción de una herramienta |
| Dato técnico de interfaz | Endpoint, API o forma de llamar al generador |
| Nota interna o de origen | Comentario, remisión interna o procedencia del texto |
| Licencia o crédito | Texto legal, autoría o atribución |

## Nivel 2 · Precatalogación por encabezado

Cada encabezado del corpus (sección de primer nivel de cada documento) va a las categorías de la taxonomía que su nombre señala. Las categorías del documento entero valen para todas sus secciones. Es la primera precatalogación: orienta la lectura y la búsqueda, y la clasificación de cada texto la confirma o la corrige. «Todos» significa que la sección trata la faceta completa. Las copias idénticas se nombran junto al original.

### F29 · Modelo

**Flux**

- `skills/visual-asset-critic/examples/worked-run/prompts/round-1/flux.txt` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/prompts/round-2/revised-flux.txt` (todo el documento)
- `skills/visual-prompt-forge/adapters/flux.md` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/flux.txt` (todo el documento)

**GPT Image 2**

- `skills/image/references/gpt-image.md` (todo el documento)
- `skills/image/references/models.md` (todo el documento)
- `skills/visual-prompt-forge/adapters/gpt-image.md` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt` (todo el documento)

**Hailuo**

- `skills/visual-prompt-forge/adapters/hailuo.md` (todo el documento)

**Ideogram**

- `skills/visual-prompt-forge/adapters/ideogram.md` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/ideogram.txt` (todo el documento)

**Kling 3.0**

- `skills/video/references/kling.md` (todo el documento)
- `skills/visual-prompt-forge/adapters/kling.md` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/kling.txt` (todo el documento)

**Midjourney**

- `skills/visual-prompt-forge/adapters/midjourney.md` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/midjourney.txt` (todo el documento)

**Nano Banana 2**

- `skills/image/references/models.md` (todo el documento)
- `skills/image/references/nano-banana.md` (todo el documento)
- `skills/visual-prompt-forge/adapters/nano-banana.md` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/nano-banana.txt` (todo el documento)

**Nano Banana Pro**

- `skills/image/references/models.md` (todo el documento)
- `skills/image/references/nano-banana.md` (todo el documento)
- `skills/visual-prompt-forge/adapters/nano-banana.md` (todo el documento)

**Seedance 2.0**

- `skills/video/references/seedance.md` (todo el documento)
- `skills/visual-prompt-forge/adapters/seedance.md` (todo el documento)

**Seedance 2.5**

- `skills/video/references/seedance-25.md` (todo el documento)
- `skills/visual-prompt-forge/adapters/seedance.md` (todo el documento)

**Seedream**

- `skills/visual-prompt-forge/adapters/seedream.md` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/seedream.txt` (todo el documento)

**Veo 3.1**

- `skills/video/references/veo.md` (todo el documento)
- `skills/visual-prompt-forge/adapters/veo.md` (todo el documento)

**gpt-image-1.5**

- `skills/visual-prompt-forge/adapters/gpt-image.md` (todo el documento)

**Todos los valores**

- `skills/visual-prompt-forge/SKILL.md` › Adapters
- `skills/visual-prompt-forge/references/prompt-anatomy.md` › Layer 5. Generator Adapter

### F35 · Migración de versión de modelo

**sí**

- `skills/image/references/gpt-image.md` › Migration from Older GPT-Image

### F10 · Operación (modo de generación)

**ancla con referencias (caso 2, T2 a T4)**

- `skills/image/references/characters.md` (todo el documento)
- `skills/image/references/golden-rules.md` › Reference Images
- `skills/visual-prompt-forge/adapters/nano-banana.md` › Composition pattern (image-to-image, the strength)

**análisis de imagen a prompt**

- `skills/image/references/vision-decomposer.md` (todo el documento)

**blockout o green screen**

- `skills/video/references/seedance-25.md` › 15. Blockout and green screen

**boceto o wireframe a final**

- `skills/image/references/dimensional.md` (todo el documento)
- `skills/image/references/structural.md` › Sketch → Final
- `skills/image/references/structural.md` › Wireframe → Mockup

**composición de varias referencias**

- `skills/image/references/characters.md` › Multi-Character Consistency
- `skills/image/references/gpt-image.md` › Multi-Image — до 16 рефов

**con referencias**

- `skills/video/references/veo.md` › 8. Reference ingredients (3.1)

**diálogo y lip-sync (4)**

- `skills/video/references/veo.md` › 4. Dialogue syntax (critical)
- `skills/visual-prompt-forge/adapters/veo.md` › Dialogue and lipsync

**edición de imagen existente (T5)**

- `skills/image/references/characters.md` › Environment Swaps
- `skills/image/references/editing.md` (todo el documento)
- `skills/image/references/golden-rules.md` › 3. Edit, Don't Re-roll
- `skills/image/references/golden-rules.md` › Conversational Refinement
- `skills/image/references/gpt-image.md` › Editing — двухколоночная логика
- `skills/image/references/nano-banana.md` › Editing у Nano Banana

**edición de video**

- `skills/video/references/seedance-25.md` › 12. Video editing (partial re-render)

**edición: añadir objeto**

- `skills/image/references/editing.md` › Object Addition

**edición: cambiar luz o clima**

- `skills/image/references/editing.md` › Lighting Control
- `skills/image/references/editing.md` › Seasonal/Weather

**edición: cambiar vestuario**

- `skills/image/references/characters.md` › Attire Changes

**edición: colorizar**

- `skills/image/references/editing.md` › Colorization

**edición: quitar objeto**

- `skills/image/references/editing.md` › Object Removal

**edición: restaurar**

- `skills/image/references/editing.md` › Restoration

**edición: traducir texto**

- `skills/image/references/editing.md` › Localization
- `skills/image/references/text-rendering.md` › Multilingual / Localization

**extensión**

- `skills/video/references/seedance-25.md` › 13. Video extension

**motion brush**

- `skills/video/references/kling.md` › 8. Motion Brush (unique)

**motion control (3c)**

- `skills/video/references/kling.md` › 9. Motion Control (2.6 Pro, unique)

**multi-shot**

- `skills/video/references/kling.md` › 3. Kling 3.0 — multi-shot, native audio, 15s
- `skills/video/references/seedance.md` › 8. Multi-shot syntax (unique)
- `skills/visual-prompt-forge/adapters/seedance.md` › When to use multi-shot vs single

**primer frame (3a)**

- `skills/video/references/kling.md` › 10. Image-to-video rule
- `skills/video/references/seedance.md` › 13. Image-to-video rule
- `skills/video/references/veo.md` › 7. Image-to-video (Veo 3.1)

**storyboard como entrada**

- `skills/video/references/seedance-25.md` › 16. Storyboard grids and keyframes

**transferencia de estilo**

- `skills/image/references/gpt-image.md` › Style Transfer

**ultra long**

- `skills/video/references/seedance-25.md` › 14. Ultra Long mode (30-180s)

**Todos los valores**

- `skills/image/references/prompt-framework.md` › Task Types (Навыки)

### F11 · Rol del ancla

**keyframe FF**

- `skills/image/references/nano-banana.md` › Кейфреймы для видео
- `skills/video/references/animatic-keyframes.md` (todo el documento)

**keyframe LF**

- `skills/image/references/nano-banana.md` › Кейфреймы для видео
- `skills/video/references/animatic-keyframes.md` (todo el documento)

### F23 · Referencias adjuntas

**estilo**

- `skills/visual-prompt-forge/references/consistency-locks.md` › Lock 6. Style references

**persona**

- `skills/video/references/seedance.md` › 10. `@img1` character reference syntax

**Todos los valores**

- `skills/video/references/seedance-25.md` › 5. Reference discipline (the 50-slot system)
- `skills/video/references/universal-rules.md` › 14. U13. Reference role discipline
- `skills/visual-prompt-forge/references/consistency-locks.md` › Lock 5. Reference images (`--cref`, omni-reference, image-to-image)

### F04 · Tipo de pieza

**UI o mockup**

- `skills/image/references/patterns/ui-social.md` › App Store Screenshot
- `skills/image/references/patterns/ui-social.md` › Dashboard Design Mockup
- `skills/image/references/structural.md` › Wireframe → Mockup

**concept art**

- `skills/image/references/dimensional.md` › Sketch → 3D Concept
- `skills/image/references/storyboards.md` › Concept Art Series

**diseño de personaje**

- `skills/image/references/patterns/character-design.md` (todo el documento)

**e-commerce o catálogo**

- `skills/image/references/patterns/ecommerce.md` (todo el documento)

**editorial**

- `skills/image/references/patterns/fashion-editorial.md` (todo el documento)

**identidad de marca**

- `skills/image/references/structural.md` › Brand Identity Systems

**miniatura**

- `skills/image/references/characters.md` › Viral Thumbnails

**post o historia para redes**

- `skills/image/references/patterns/ui-social.md` › Instagram Story Ad (9:16)
- `skills/image/references/patterns/ui-social.md` › Social Media Feed Post (1:1)

**póster o key art**

- `skills/image/references/patterns/ecommerce.md` › Inflatable Surrealism Product Poster
- `skills/image/references/patterns/fashion-editorial.md` › Streetwear Poster with Oversized Typography
- `skills/image/references/patterns/food-beverage.md` › Hyper-Realistic Food Poster Template
- `skills/image/references/patterns/poster-illustration.md` (todo el documento)

**retrato**

- `skills/image/references/patterns/fashion-editorial.md` › 2x2 Editorial Portrait Grid
- `skills/image/references/patterns/portrait-cinema.md` (todo el documento)

**slide o presentación**

- `skills/image/references/slides.md` (todo el documento)

**storyboard o multipanel**

- `skills/image/references/multi-panel.md` (todo el documento)
- `skills/image/references/patterns/ecommerce.md` › 9-Panel TVC Storyboard Grid
- `skills/image/references/patterns/fashion-editorial.md` › 2x2 Editorial Portrait Grid
- `skills/image/references/storyboards.md` (todo el documento)
- `skills/video/references/dramaturgy.md` › 10. Three-layer storyboard method

**visualización arquitectónica**

- `skills/image/references/dimensional.md` › 2D Floor Plan → 3D
- `skills/image/references/dimensional.md` › Architectural Visualization

### F05 · Temática o industria

**comida y bebida**

- `skills/image/references/patterns/food-beverage.md` (todo el documento)

**moda**

- `skills/image/references/patterns/fashion-editorial.md` (todo el documento)
- `skills/image/references/patterns/poster-illustration.md` › Emerald Street Fashion Poster

### F06 · Formato de salida

**1:1**

- `skills/image/references/patterns/ui-social.md` › Social Media Feed Post (1:1)

**9:16**

- `skills/image/references/patterns/ui-social.md` › Instagram Story Ad (9:16)

### F03 · Ruta operativa

**Clip**

- `skills/ai-production-director/SKILL.md` › 2. Selección de track

**Video publicitario**

- `skills/ai-production-director/SKILL.md` › 2. Selección de track

### F07 · Género narrativo

**carrera y velocidad**

- `skills/video/references/race-and-speed.md` (todo el documento)

**Todos los valores**

- `skills/video/references/patterns-and-genres.md` › 2. Genre modules

### F08 · Estructura de beats

**Content Spiral**

- `skills/storyboard-architect/references/beat-frameworks.md` › Content Spiral

**Custom**

- `skills/storyboard-architect/references/beat-frameworks.md` › Custom

**Educational Demo**

- `skills/storyboard-architect/references/beat-frameworks.md` › Educational Demo

**Founder Explainer**

- `skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md` › Beat framework: Founder Explainer
- `skills/storyboard-architect/references/beat-frameworks.md` › Founder Explainer

**Hero Trilogy**

- `skills/storyboard-architect/references/beat-frameworks.md` › Hero Trilogy

**Pain-Reframe-Promise**

- `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md` › Beat framework: Pain-Reframe-Promise
- `skills/storyboard-architect/references/beat-frameworks.md` › Pain-Reframe-Promise (PRP)

### F09 · Patrón de montaje

**Todos los valores**

- `skills/video/references/patterns-and-genres.md` › 1. Montage patterns

### F12 · Función del plano

**CTA o logo**

- `skills/storyboard-architect/references/timing-rules.md` › CTA timing (the final beat)

**hook**

- `skills/storyboard-architect/references/timing-rules.md` › Hook timing (the first beat)

**Todos los valores**

- `skills/video/references/role-modes.md` › 4. Shot function taxonomy

### F14 · Régimen físico

**03 subacuático**

- `skills/image/references/patterns/portrait-cinema.md` › Dreamy Underwater Surreal Portrait

### F15 · Sujeto

**producto**

- `skills/image/references/dimensional.md` › Product 2D → 3D
- `skills/image/references/patterns/ecommerce.md` › Inflatable Surrealism Product Poster
- `skills/image/references/patterns/ecommerce.md` › Luxury Cosmetics Studio Shot
- `skills/image/references/patterns/ecommerce.md` › Miniature Diorama Product Ad

### F17 · Estilo visual

**blanco y negro**

- `skills/image/references/patterns/portrait-cinema.md` › Monochrome Glitch Profile Portrait

**futurista**

- `skills/image/references/patterns/fashion-editorial.md` › Futuristic Sportswear Editorial with 3D Blob Shapes
- `skills/image/references/slides.md` › Futuristic / SaaS Style

**retro o vintage**

- `skills/image/references/patterns/fashion-editorial.md` › Retro Roller Skating Sportswear Campaign
- `skills/image/references/patterns/poster-illustration.md` › Peacock Botanical Vintage Art Print

### F18 · Técnica de representación

**fotorrealista**

- `skills/visual-media/SKILL.md` › Fundamentos de fotografía

**pixel art**

- `skills/image/references/storyboards.md` › Sprite Sheets
- `skills/image/references/structural.md` › Pixel Art

### F24 · Tamaño de plano

**Todos los valores**

- `skills/storyboard-architect/references/shot-grammar.md` › Framing (subject size in frame)
- `skills/video/references/camera-lighting-vocabulary.md` › 1. Framing

### F25 · Ángulo

**Todos los valores**

- `skills/storyboard-architect/references/shot-grammar.md` › Angle (camera vertical position)

### F26 · Movimiento de cámara

**Todos los valores**

- `skills/storyboard-architect/references/shot-grammar.md` › Motion (camera movement)
- `skills/video/references/camera-lighting-vocabulary.md` › 2. Camera movement

### F27 · Transición

**Todos los valores**

- `skills/video/references/camera-lighting-vocabulary.md` › 11. Transition vocabulary
- `skills/video/references/seedance-25.md` › 10. Transitions

### F28 · Audio

**Todos los valores**

- `skills/video/references/camera-lighting-vocabulary.md` › 8. Sound categories

### F30 · Qué regula

**anatomía, rostro y piel**

- `skills/image/references/characters.md` › Expression Control
- `skills/video/references/seedance-25.md` › 8. Realistic human formula (anti-AI-face)

**animación**

- `skills/visual-media/SKILL.md` › Fundamentos de animación

**audio**

- `skills/video/references/camera-lighting-vocabulary.md` › 8. Sound categories
- `skills/video/references/kling.md` › 3. Kling 3.0 — multi-shot, native audio, 15s
- `skills/video/references/race-and-speed.md` › 8. Sound & rhythm
- `skills/video/references/seedance-25.md` › 4. Syntax markers for audio, dialogue and text
- `skills/video/references/seedance.md` › 14. Audio (1.5+)
- `skills/video/references/veo.md` › 4. Dialogue syntax (critical)
- `skills/video/references/veo.md` › 5. SFX syntax
- `skills/visual-prompt-forge/adapters/veo.md` › Audio direction
- `skills/visual-prompt-forge/adapters/veo.md` › Dialogue and lipsync

**color, grade y textura**

- `skills/brand-lock-extractor/brand-packs/_template.md` › Color grade direction · idéntico en 1 documento más
- `skills/brand-lock-extractor/brand-packs/_template.md` › Palette · idéntico en 1 documento más
- `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` › Color grade direction
- `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` › Palette
- `skills/brand-lock-extractor/examples/brand-lock.md` › Color grade direction
- `skills/brand-lock-extractor/examples/brand-lock.md` › Palette
- `skills/brand-lock-extractor/references/extraction-rubric.md` › Color grade direction
- `skills/brand-lock-extractor/references/extraction-rubric.md` › Palette
- `skills/brand-lock-extractor/templates/brand-lock.md.tpl` › Color grade direction
- `skills/brand-lock-extractor/templates/brand-lock.md.tpl` › Palette
- `skills/image/references/creative-direction.md` › Color Grading & Film Stock
- `skills/image/references/patterns/ui-social.md` › Personal Color Analysis Board
- `skills/image/references/slides.md` › Color Systems
- `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` › Color grade direction · idéntico en 2 documentos más
- `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` › Palette · idéntico en 2 documentos más
- `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` › Color grade direction
- `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` › Palette
- `skills/storyboard-architect/references/on-screen-text.md` › Color rules
- `skills/video/references/camera-lighting-vocabulary.md` › 7. Color discipline
- `skills/video/references/race-and-speed.md` › 7. Light & color for speed without faces
- `skills/visual-prompt-forge/references/consistency-locks.md` › Lock 8. Color grade flow-through

**composición**

- `skills/image/references/multi-panel.md` (todo el documento)
- `skills/image/references/slides.md` › Design Principles
- `skills/image/references/slides.md` › Layout Systems
- `skills/image/references/structural.md` › Composition Templates
- `skills/image/references/structural.md` › Grid-Based Assets
- `skills/image/references/structural.md` › Layout Guidance
- `skills/image/references/text-rendering.md` › Layout Types
- `skills/storyboard-architect/references/on-screen-text.md` › Composition rules
- `skills/video/references/animatic-keyframes.md` › 4. Composing a still that reads as MOTION
- `skills/video/references/animatic-keyframes.md` › 6. The loaded frame for one panel
- `skills/video/references/dramaturgy.md` › 8. Spatial clarity beats montage hysteria
- `skills/visual-asset-critic/references/critique-rubric.md` › Layer 4. Composition check
- `skills/visual-prompt-forge/adapters/flux.md` › Composition mapping
- `skills/visual-prompt-forge/adapters/flux.md` › Composition pattern
- `skills/visual-prompt-forge/adapters/gpt-image.md` › Composition pattern
- `skills/visual-prompt-forge/adapters/gpt-image.md` › Spatial language strength
- `skills/visual-prompt-forge/adapters/ideogram.md` › Composition pattern (Mode 1, composited)
- `skills/visual-prompt-forge/adapters/ideogram.md` › Composition pattern (Mode 2, text-in-image)
- `skills/visual-prompt-forge/adapters/midjourney.md` › Composition mapping
- `skills/visual-prompt-forge/adapters/midjourney.md` › Composition pattern
- `skills/visual-prompt-forge/adapters/nano-banana.md` › Composition pattern (image-to-image, the strength)
- `skills/visual-prompt-forge/adapters/nano-banana.md` › Composition pattern (text-to-image)
- `skills/visual-prompt-forge/adapters/seedream.md` › Composition pattern
- `skills/visual-prompt-forge/references/failure-modes.md` › Failure 5. Composition doesn't reserve space for text overlay

**continuidad entre clips**

- `skills/video/references/fixes-and-skeletons.md` › 1. Continuity checklist
- `skills/visual-asset-critic/references/critique-rubric.md` › Layer 6. Continuity check (if previous shots available)
- `skills/visual-prompt-forge/adapters/kling.md` › Continuity across shots

**crítica y revisión**

- `skills/ai-production-director/references/production-package.md` › 3. Checklist de post-producción (07-delivery/post-production.md)
- `skills/ai-production-director/references/production-package.md` › 4. Checklist maestro del pipeline (gate de la Etapa 7)
- `skills/screenwriter/references/pipeline-integration.md` › Output Format Validation
- `skills/storyboard-architect/SKILL.md` › Quality bar
- `skills/storyboard-architect/references/timing-rules.md` › Validating timing
- `skills/storyboard-html-preview/SKILL.md` › Quality bar
- `skills/video/references/animatic-keyframes.md` › 9. Checklist: does this keyframe earn its place
- `skills/video/references/dramaturgy.md` › 15. Dramaturgy check before sending any prompt
- `skills/video/references/fixes-and-skeletons.md` › 1. Continuity checklist
- `skills/video/references/universal-rules.md` › 13. U12. The three-detail check (audit before sending)
- `skills/visual-asset-critic/SKILL.md` (todo el documento)
- `skills/visual-asset-critic/references/critique-rubric.md` (todo el documento)
- `skills/visual-prompt-forge/SKILL.md` › Quality bar
- `skills/visual-prompt-forge/SKILL.md` › Revision mode (closing the QA loop)
- `skills/visual-prompt-forge/references/failure-modes.md` › Failure 7, "Looks fine but doesn't match the brief"
- `skills/visual-prompt-forge/references/failure-modes.md` › When to stop iterating prompts

**dramaturgia**

- `skills/video/references/animatic-keyframes.md` › 5. Emotion without faces in a still
- `skills/video/references/dramaturgy.md` (todo el documento)
- `skills/video/references/race-and-speed.md` › 4. Storytelling without faces — the race captioning system
- `skills/video/references/universal-rules.md` › 12. U11. The final image rule

**encuadre y lente**

- `skills/image/references/creative-direction.md` › Camera & Hardware
- `skills/storyboard-architect/references/shot-grammar.md` › Depth of field
- `skills/storyboard-architect/references/shot-grammar.md` › Framing (subject size in frame)
- `skills/video/references/camera-lighting-vocabulary.md` › 1. Framing
- `skills/video/references/camera-lighting-vocabulary.md` › 3. Lens language
- `skills/video/references/race-and-speed.md` › 6. Camera grammar for speed
- `skills/video/references/universal-rules.md` › 7. U6. Precise lens language
- `skills/visual-prompt-forge/adapters/flux.md` › Photographic specifics

**estrategia y concepto**

- `skills/ai-production-director/references/creative-strategy.md` (todo el documento)
- `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md` › Brief
- `skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md` › Brief
- `skills/storyboard-architect/examples/shotkit-explainer/storyboard.md` › Brief
- `skills/storyboard-architect/templates/storyboard.md.tpl` › Brief

**estructura narrativa y diálogo**

- `skills/ai-production-director/references/creative-strategy.md` › 5. Dirección narrativa del concepto ganador
- `skills/image/references/storyboards.md` › Narrative Pacing
- `skills/image/references/storyboards.md` › Story Sequence
- `skills/screenwriter/SKILL.md` › Best Practices
- `skills/screenwriter/SKILL.md` › Screenplay Format Standards
- `skills/screenwriter/SKILL.md` › Short Film Structure (5-10 Minutes)
- `skills/screenwriter/SKILL.md` › XML Output Format
- `skills/screenwriter/references/advanced-techniques.md` › Advanced Visual Storytelling
- `skills/screenwriter/references/advanced-techniques.md` › Dialogue Polish Techniques
- `skills/screenwriter/references/advanced-techniques.md` › Pacing Optimization
- `skills/screenwriter/references/advanced-techniques.md` › Short Film Specific Techniques
- `skills/screenwriter/references/pipeline-integration.md` › Duration Estimation Guidelines
- `skills/screenwriter/references/pipeline-integration.md` › Imagine-Ready Visual Descriptions
- `skills/screenwriter/references/pipeline-integration.md` › Scene Metadata Standards
- `skills/screenwriter/references/pipeline-integration.md` › Scene Numbering Conventions
- `skills/video/references/patterns-and-genres.md` › 3. Multi-clip story structure
- `skills/video/references/race-and-speed.md` › 9. 30-second structure (beat map)
- `skills/video/references/role-modes.md` › 2. Screenwriter mode

**estructura y sintaxis del prompt**

- `skills/ai-video-storyboard/SKILL.md` › Output Format
- `skills/image/references/golden-rules.md` › 1. Start with a Verb
- `skills/image/references/golden-rules.md` › 2. Positive Framing
- `skills/image/references/golden-rules.md` › 4. Natural Language
- `skills/image/references/golden-rules.md` › 5. Be Specific
- `skills/image/references/golden-rules.md` › 6. Provide Context
- `skills/image/references/golden-rules.md` › 7. Quote Text Exactly
- `skills/image/references/golden-rules.md` › Prompt Template
- `skills/image/references/golden-rules.md` › World Knowledge Anchors
- `skills/image/references/gpt-image.md` › Anti-Slop Rules
- `skills/image/references/gpt-image.md` › Iteration Strategy
- `skills/image/references/gpt-image.md` › Use-Case Templates
- `skills/image/references/gpt-image.md` › World Knowledge
- `skills/image/references/gpt-image.md` › Структура промпта — 5 slots
- `skills/image/references/models.md` › Различия в синтаксисе промпта
- `skills/image/references/nano-banana.md` › Известные фейлы
- `skills/image/references/nano-banana.md` › Стиль промпта
- `skills/image/references/nano-banana.md` › Что НЕ указывать
- `skills/image/references/prompt-framework.md` › Cinematic Verbose Mode
- `skills/image/references/prompt-framework.md` › Detail Modes (Режимы)
- `skills/image/references/prompt-framework.md` › Output Structure
- `skills/image/references/prompt-framework.md` › Parameterized Templates
- `skills/image/references/prompt-framework.md` › Universal Elements (Чеклист)
- `skills/image/references/storyboards.md` › Output Control
- `skills/image/references/text-rendering.md` › Prompt Structure
- `skills/image/references/text-rendering.md` › Text-First Hack
- `skills/image/references/vision-decomposer.md` › OUTPUT PROTOCOL
- `skills/image/references/vision-decomposer.md` › STEP 2 — PROMPT SYNTHESIS
- `skills/storyboard-architect/references/shot-grammar.md` › What goes in `subject` vs `series_lock` vs `brand_lock`
- `skills/video/references/animatic-keyframes.md` › 7. From keyframe to image-gen prompt
- `skills/video/references/camera-lighting-vocabulary.md` › 10. Translating uncommon terms
- `skills/video/references/dramaturgy.md` › 11. Shot card template
- `skills/video/references/fixes-and-skeletons.md` › 2. Common failures and fixes
- `skills/video/references/fixes-and-skeletons.md` › 3. Cross-model prompt skeletons
- `skills/video/references/fixes-and-skeletons.md` › 4. Default negative constraints
- `skills/video/references/fixes-and-skeletons.md` › 5. Prompt compression order
- `skills/video/references/fixes-and-skeletons.md` › 6. Output format templates
- `skills/video/references/kling.md` › 11. Failure modes and fixes
- `skills/video/references/kling.md` › 12. Skeleton
- `skills/video/references/kling.md` › 4. Prompt formula (1.x – 2.x)
- `skills/video/references/kling.md` › 5. Prompt length by model
- `skills/video/references/kling.md` › 6. Negative prompts (critical rule)
- `skills/video/references/race-and-speed.md` › 10. Anti-fake guard
- `skills/video/references/seedance-25.md` › 17. Failure modes and fixes
- `skills/video/references/seedance-25.md` › 3. Official prompt formula
- `skills/video/references/seedance-25.md` › 4. Syntax markers for audio, dialogue and text
- `skills/video/references/seedance-25.md` › 7. The anti-collapse skeleton (3 modules)
- `skills/video/references/seedance.md` › 12. Negative prompts
- `skills/video/references/seedance.md` › 15. Failure modes and fixes
- `skills/video/references/seedance.md` › 4. The Details Law (read this first)
- `skills/video/references/seedance.md` › 5. Six-step prompt formula (quick scenes)
- `skills/video/references/seedance.md` › 6. Production-grade skeleton (11 blocks)
- `skills/video/references/seedance.md` › 8. Multi-shot syntax (unique)
- `skills/video/references/seedance.md` › 9. Anti-mush guard block
- `skills/video/references/universal-rules.md` › 10. U9. Concrete physical detail over abstract concept
- `skills/video/references/universal-rules.md` › 15. U14. Priority declaration
- `skills/video/references/universal-rules.md` › 2. U1. Universal prompt skeleton
- `skills/video/references/universal-rules.md` › 3. U2. Weight-at-start
- `skills/video/references/universal-rules.md` › 4. U3. Show don't tell
- `skills/video/references/universal-rules.md` › 5. U4. Natural language beats tag spam
- `skills/video/references/universal-rules.md` › 9. U8. No contradictions
- `skills/video/references/veo.md` › 10. Skeleton
- `skills/video/references/veo.md` › 3. Prompt structure and length
- `skills/video/references/veo.md` › 6. JSON prompts (powerful, unique)
- `skills/video/references/veo.md` › 9. Failure modes and fixes
- `skills/visual-prompt-forge/SKILL.md` › Hard rules
- `skills/visual-prompt-forge/SKILL.md` › The five-layer prompt anatomy
- `skills/visual-prompt-forge/adapters/flux.md` › Length
- `skills/visual-prompt-forge/adapters/flux.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/flux.md` › Syntax pattern
- `skills/visual-prompt-forge/adapters/gpt-image.md` › Length
- `skills/visual-prompt-forge/adapters/gpt-image.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/gpt-image.md` › Syntax pattern
- `skills/visual-prompt-forge/adapters/hailuo.md` › Length
- `skills/visual-prompt-forge/adapters/hailuo.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/hailuo.md` › Syntax pattern
- `skills/visual-prompt-forge/adapters/ideogram.md` › Length
- `skills/visual-prompt-forge/adapters/ideogram.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/ideogram.md` › Syntax pattern (Mode 2)
- `skills/visual-prompt-forge/adapters/kling.md` › Length
- `skills/visual-prompt-forge/adapters/kling.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/kling.md` › Syntax pattern
- `skills/visual-prompt-forge/adapters/midjourney.md` › Length
- `skills/visual-prompt-forge/adapters/midjourney.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/midjourney.md` › Syntax pattern
- `skills/visual-prompt-forge/adapters/nano-banana.md` › Length
- `skills/visual-prompt-forge/adapters/nano-banana.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/nano-banana.md` › Syntax pattern
- `skills/visual-prompt-forge/adapters/seedance.md` › Length
- `skills/visual-prompt-forge/adapters/seedance.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/seedance.md` › Syntax pattern
- `skills/visual-prompt-forge/adapters/seedream.md` › Length
- `skills/visual-prompt-forge/adapters/seedream.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/seedream.md` › Syntax pattern
- `skills/visual-prompt-forge/adapters/veo.md` › Length
- `skills/visual-prompt-forge/adapters/veo.md` › Pitfalls to avoid
- `skills/visual-prompt-forge/adapters/veo.md` › Syntax pattern
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` › What's not in any prompt
- `skills/visual-prompt-forge/references/failure-modes.md` › Failure 1. The "AI look"
- `skills/visual-prompt-forge/references/prompt-anatomy.md` › How layers compose
- `skills/visual-prompt-forge/references/prompt-anatomy.md` › Layer 3. Shot Spec

**física y movimiento congelado**

- `skills/image/references/editing.md` › Physics-Aware
- `skills/video/references/animatic-keyframes.md` › 4. Composing a still that reads as MOTION
- `skills/video/references/race-and-speed.md` › 3. Selling speed in a single frame
- `skills/video/references/seedance-25.md` › 11. Physics through consequences and triggers

**identidad y consistencia**

- `skills/image/references/characters.md` › Identity Locking
- `skills/image/references/characters.md` › Multi-Character Consistency
- `skills/image/references/storyboards.md` › Consistency Rules
- `skills/screenwriter/references/pipeline-integration.md` › Character Consistency Tracking
- `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md` › Series lock
- `skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md` › Series lock
- `skills/storyboard-architect/examples/shotkit-explainer/storyboard.md` › Series lock
- `skills/storyboard-architect/templates/storyboard.md.tpl` › Series lock
- `skills/video/references/kling.md` › 7. Element Library and Element Binding (1.x – 2.x)
- `skills/video/references/seedance.md` › 10. `@img1` character reference syntax
- `skills/video/references/universal-rules.md` › 8. U7. Character consistency anchor
- `skills/visual-asset-critic/references/critique-rubric.md` › Layer 2. Series Lock check
- `skills/visual-prompt-forge/adapters/seedream.md` › Series consistency
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` › Series lock context (constant across all adapters)
- `skills/visual-prompt-forge/references/consistency-locks.md` (todo el documento)
- `skills/visual-prompt-forge/references/failure-modes.md` › Failure 2. Character drift across shots
- `skills/visual-prompt-forge/references/failure-modes.md` › Failure 6. Series feels "different" even with locks applied
- `skills/visual-prompt-forge/references/prompt-anatomy.md` › Layer 2. Series Lock

**luz**

- `skills/image/references/creative-direction.md` › Lighting Design
- `skills/image/references/editing.md` › Lighting Control
- `skills/storyboard-architect/references/shot-grammar.md` › Lighting style (referenced from series_lock)
- `skills/video/references/camera-lighting-vocabulary.md` › 4. Light sources
- `skills/video/references/camera-lighting-vocabulary.md` › 5. Light direction
- `skills/video/references/camera-lighting-vocabulary.md` › 6. Light quality
- `skills/video/references/race-and-speed.md` › 7. Light & color for speed without faces
- `skills/visual-prompt-forge/adapters/midjourney.md` › Lighting language
- `skills/visual-prompt-forge/references/consistency-locks.md` › Lock 3. Verbatim lighting anchors
- `skills/visual-prompt-forge/references/consistency-locks.md` › Lock 7. Lighting direction continuity
- `skills/visual-prompt-forge/references/failure-modes.md` › Failure 4. Lighting direction inconsistency

**marca y logos**

- `skills/brand-lock-extractor/SKILL.md` (todo el documento)
- `skills/brand-lock-extractor/brand-packs/README.md` (todo el documento) · idéntico en 1 documento más
- `skills/brand-lock-extractor/brand-packs/_template.md` (todo el documento) · idéntico en 1 documento más
- `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` (todo el documento)
- `skills/brand-lock-extractor/examples/brand-lock.md` (todo el documento)
- `skills/brand-lock-extractor/examples/input-brief.md` (todo el documento)
- `skills/brand-lock-extractor/references/extraction-rubric.md` (todo el documento)
- `skills/brand-lock-extractor/templates/brand-lock.md.tpl` (todo el documento)
- `skills/image/references/characters.md` › Brand Asset Generation
- `skills/image/references/structural.md` › Brand Identity Systems
- `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` (todo el documento) · idéntico en 2 documentos más
- `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` (todo el documento)
- `skills/visual-asset-critic/references/critique-rubric.md` › Layer 1. Brand Lock check
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` › Brand mood
- `skills/visual-prompt-forge/references/prompt-anatomy.md` › Layer 1. Brand Lock

**materialidad y superficie**

- `skills/image/references/creative-direction.md` › Materiality & Texture

**movimiento de cámara**

- `skills/brand-lock-extractor/brand-packs/_template.md` › Motion language · idéntico en 1 documento más
- `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` › Motion language
- `skills/brand-lock-extractor/examples/brand-lock.md` › Motion language
- `skills/brand-lock-extractor/references/extraction-rubric.md` › Motion language
- `skills/brand-lock-extractor/templates/brand-lock.md.tpl` › Motion language
- `skills/screenwriter/references/advanced-techniques.md` › Camera Movement Hints (For Arch-V)
- `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` › Motion language · idéntico en 2 documentos más
- `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` › Motion language
- `skills/storyboard-architect/references/shot-grammar.md` › Motion (camera movement)
- `skills/video/references/camera-lighting-vocabulary.md` › 2. Camera movement
- `skills/video/references/dramaturgy.md` › 7. Camera must have a reason
- `skills/video/references/race-and-speed.md` › 6. Camera grammar for speed
- `skills/video/references/seedance-25.md` › 9. Camera language
- `skills/video/references/seedance.md` › 11. Camera movements (9 presets)
- `skills/video/references/universal-rules.md` › 6. U5. One primary camera move per shot
- `skills/visual-prompt-forge/adapters/hailuo.md` › Motion vocabulary
- `skills/visual-prompt-forge/adapters/kling.md` › Motion vocabulary
- `skills/visual-prompt-forge/adapters/kling.md` › Subject motion
- `skills/visual-prompt-forge/adapters/seedance.md` › Motion vocabulary
- `skills/visual-prompt-forge/adapters/veo.md` › Motion vocabulary

**orquestación y control de flujo**

- `skills/ai-production-director/SKILL.md` › 1. Mapa de sub-skills
- `skills/ai-production-director/SKILL.md` › 2. Selección de track
- `skills/ai-production-director/SKILL.md` › 3. Las etapas
- `skills/ai-production-director/SKILL.md` › 4. Interacción con el usuario entre etapas
- `skills/ai-production-director/SKILL.md` › 5. Ejecución por etapa — regla de carga
- `skills/ai-production-director/SKILL.md` › 6. Reglas de resolución de conflictos
- `skills/ai-production-director/SKILL.md` › 7. Rol de visual-media (decisión de alcance)
- `skills/ai-production-director/SKILL.md` › 8. Degradación
- `skills/ai-video-storyboard/SKILL.md` › When to Use
- `skills/ai-video-storyboard/SKILL.md` › Workflow
- `skills/brand-lock-extractor/SKILL.md` › When to use
- `skills/brand-lock-extractor/SKILL.md` › Workflow
- `skills/image/SKILL.md` › Route first — is this actually an image-prompt task?
- `skills/image/SKILL.md` › Step 1 — always read first → [models.md](references/models.md)
- `skills/image/references/prompt-framework.md` › Quick Decision Tree
- `skills/image/references/vision-decomposer.md` › When to load this file
- `skills/screenwriter/SKILL.md` › Core Workflow
- `skills/storyboard-architect/SKILL.md` › When to use
- `skills/storyboard-architect/SKILL.md` › Workflow
- `skills/storyboard-html-preview/SKILL.md` › When to use
- `skills/storyboard-html-preview/SKILL.md` › Workflow
- `skills/video/SKILL.md` › Route first — is this actually a video-prompt task?
- `skills/video/SKILL.md` › Step 1 — always read first → [dramaturgy.md](references/dramaturgy.md)
- `skills/visual-asset-critic/SKILL.md` › When to use
- `skills/visual-asset-critic/SKILL.md` › Workflow
- `skills/visual-media/SKILL.md` › Cuándo aplica
- `skills/visual-prompt-forge/SKILL.md` › When to use
- `skills/visual-prompt-forge/SKILL.md` › Workflow

**parámetros técnicos**

- `skills/brand-lock-extractor/brand-packs/_template.md` › Aspect ratios · idéntico en 1 documento más
- `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` › Aspect ratios
- `skills/brand-lock-extractor/examples/brand-lock.md` › Aspect ratios
- `skills/brand-lock-extractor/references/extraction-rubric.md` › Aspect ratios
- `skills/brand-lock-extractor/templates/brand-lock.md.tpl` › Aspect ratios
- `skills/image/references/dimensional.md` › Quality Levels
- `skills/image/references/golden-rules.md` › Cost Optimization (Batch Work)
- `skills/image/references/gpt-image.md` › Quality Settings — рычаг fidelity / latency
- `skills/image/references/gpt-image.md` › Размеры (gpt-image-2)
- `skills/image/references/models.md` › TL;DR
- `skills/image/references/models.md` › Когда что выигрывает
- `skills/image/references/models.md` › Стоимость (ориентир)
- `skills/image/references/nano-banana.md` › Resolution / Cost
- `skills/image/references/nano-banana.md` › Когда переключаться NB2 → NBP
- `skills/image/references/nano-banana.md` › Уникальные возможности
- `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` › Aspect ratios · idéntico en 2 documentos más
- `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` › Aspect ratios
- `skills/video/references/kling.md` › 2. Versions and element limits
- `skills/video/references/seedance-25.md` › 1. What 2.5 changes
- `skills/video/references/seedance-25.md` › 18. Economics and model choice
- `skills/video/references/seedance-25.md` › 2. Specs and hard limits
- `skills/video/references/seedance.md` › 2. Versions and specs
- `skills/video/references/seedance.md` › 3. CLI parameters (1.x / 2.0 only)
- `skills/video/references/universal-rules.md` › 11. U10. Duration discipline
- `skills/video/references/veo.md` › 2. Versions and specs
- `skills/visual-asset-critic/references/critique-rubric.md` › Layer 5. Technical check
- `skills/visual-prompt-forge/adapters/_capabilities.json` (todo el documento)
- `skills/visual-prompt-forge/adapters/flux.md` › Flux variant selection
- `skills/visual-prompt-forge/adapters/flux.md` › Where parameters go
- `skills/visual-prompt-forge/adapters/gpt-image.md` › Parameters
- `skills/visual-prompt-forge/adapters/hailuo.md` › Parameters
- `skills/visual-prompt-forge/adapters/ideogram.md` › Parameters
- `skills/visual-prompt-forge/adapters/ideogram.md` › When NOT to use Ideogram
- `skills/visual-prompt-forge/adapters/kling.md` › Parameters
- `skills/visual-prompt-forge/adapters/midjourney.md` › Parameter reference (current as of Q2 2026)
- `skills/visual-prompt-forge/adapters/nano-banana.md` › Parameters
- `skills/visual-prompt-forge/adapters/seedance.md` › Parameters
- `skills/visual-prompt-forge/adapters/seedream.md` › Parameters
- `skills/visual-prompt-forge/adapters/seedream.md` › When Seedream is the right choice
- `skills/visual-prompt-forge/adapters/seedream.md` › When Seedream is the wrong choice
- `skills/visual-prompt-forge/adapters/veo.md` › Parameters
- `skills/visual-prompt-forge/references/consistency-locks.md` › Lock 4. Seed locking

**puesta en escena y blocking**

- `skills/image/references/characters.md` › Pose/Action Control
- `skills/video/references/camera-lighting-vocabulary.md` › 9. Blocking language
- `skills/video/references/dramaturgy.md` › 5. Blocking as choreography of desire
- `skills/video/references/dramaturgy.md` › 6. Staging controls subtext

**texto en pantalla**

- `skills/brand-lock-extractor/brand-packs/_template.md` › Typography · idéntico en 1 documento más
- `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` › Typography
- `skills/brand-lock-extractor/examples/brand-lock.md` › Typography
- `skills/brand-lock-extractor/references/extraction-rubric.md` › Typography
- `skills/brand-lock-extractor/templates/brand-lock.md.tpl` › Typography
- `skills/image/references/editing.md` › Localization
- `skills/image/references/golden-rules.md` › 7. Quote Text Exactly
- `skills/image/references/gpt-image.md` › Text in Image
- `skills/image/references/nano-banana.md` › Text Rendering
- `skills/image/references/patterns/fashion-editorial.md` › Streetwear Poster with Oversized Typography
- `skills/image/references/slides.md` › Typography
- `skills/image/references/text-rendering.md` (todo el documento)
- `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` › Typography · idéntico en 2 documentos más
- `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` › Typography
- `skills/storyboard-architect/references/on-screen-text.md` (todo el documento)
- `skills/storyboard-architect/references/timing-rules.md` › On-screen text duration math
- `skills/storyboard-architect/templates/storyboard.md.tpl` › Text overlays
- `skills/video/references/seedance-25.md` › 4. Syntax markers for audio, dialogue and text
- `skills/visual-prompt-forge/adapters/gpt-image.md` › Text rendering
- `skills/visual-prompt-forge/adapters/ideogram.md` › Composition pattern (Mode 2, text-in-image)
- `skills/visual-prompt-forge/adapters/ideogram.md` › Mode 1: Composited (default)
- `skills/visual-prompt-forge/adapters/ideogram.md` › Mode 2: Text-in-image (override)
- `skills/visual-prompt-forge/references/failure-modes.md` › Failure 3. Text in image looks bad
- `skills/visual-prompt-forge/references/failure-modes.md` › Failure 5. Composition doesn't reserve space for text overlay
- `skills/visual-prompt-forge/references/prompt-anatomy.md` › Layer 4. Text Layer

**trazabilidad y entrega**

- `skills/ai-production-director/references/production-package.md` › 1. Estructura del paquete
- `skills/ai-production-director/references/production-package.md` › 2. Reglas de trazabilidad
- `skills/ai-production-director/references/production-package.md` › 3. Checklist de post-producción (07-delivery/post-production.md)
- `skills/brand-lock-extractor/brand-packs/README.md` › Versioning · idéntico en 1 documento más
- `skills/brand-lock-extractor/examples/brand-lock.md` › Extraction notes
- `skills/brand-lock-extractor/templates/brand-lock.md.tpl` › Extraction notes
- `skills/screenwriter/references/pipeline-integration.md` › Pipeline Handoff Checklist
- `skills/storyboard-architect/SKILL.md` › Handoff
- `skills/storyboard-architect/SKILL.md` › Output formats
- `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md` › Audit trail
- `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md` › Handoff notes
- `skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md` › Audit trail
- `skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md` › Handoff notes
- `skills/storyboard-architect/examples/shotkit-explainer/storyboard.md` › Audit trail
- `skills/storyboard-architect/templates/storyboard.md.tpl` › Audit trail
- `skills/storyboard-architect/templates/storyboard.md.tpl` › Handoff notes
- `skills/storyboard-html-preview/SKILL.md` › Hard rules
- `skills/storyboard-html-preview/SKILL.md` › Two timestamps, not one
- `skills/storyboard-html-preview/SKILL.md` › What you produce
- `skills/visual-asset-critic/SKILL.md` › Handoff
- `skills/visual-prompt-forge/adapters/hailuo.md` › Output handoff
- `skills/visual-prompt-forge/adapters/kling.md` › Output handoff
- `skills/visual-prompt-forge/adapters/seedance.md` › Output handoff
- `skills/visual-prompt-forge/adapters/veo.md` › Output handoff

**ángulo**

- `skills/storyboard-architect/references/shot-grammar.md` › Angle (camera vertical position)

### F31 · Condición para avanzar

**sí, la aprueba el usuario**

- `skills/ai-production-director/references/production-package.md` › 4. Checklist maestro del pipeline (gate de la Etapa 7)

**sí, la verifica una herramienta**

- `skills/ai-production-director/references/production-package.md` › 4. Checklist maestro del pipeline (gate de la Etapa 7)

**sí, revisión manual obligatoria**

- `skills/ai-production-director/references/production-package.md` › 4. Checklist maestro del pipeline (gate de la Etapa 7)

### F01 · Etapa

**0 Brand Lock**

- `skills/brand-lock-extractor/SKILL.md` (todo el documento)
- `skills/brand-lock-extractor/brand-packs/README.md` (todo el documento) · idéntico en 1 documento más
- `skills/brand-lock-extractor/brand-packs/_template.md` (todo el documento) · idéntico en 1 documento más
- `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` (todo el documento)
- `skills/brand-lock-extractor/examples/brand-lock.md` (todo el documento)
- `skills/brand-lock-extractor/examples/input-brief.md` (todo el documento)
- `skills/brand-lock-extractor/references/extraction-rubric.md` (todo el documento)
- `skills/brand-lock-extractor/templates/brand-lock.md.tpl` (todo el documento)
- `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` (todo el documento) · idéntico en 2 documentos más
- `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` (todo el documento)

**1 Estrategia creativa**

- `skills/ai-production-director/references/creative-strategy.md` (todo el documento)

**2 Guion**

- `skills/screenwriter/SKILL.md` (todo el documento)
- `skills/screenwriter/references/advanced-techniques.md` (todo el documento)
- `skills/screenwriter/references/pipeline-integration.md` (todo el documento)

**3 Dirección cinematográfica**

- `skills/video/references/camera-lighting-vocabulary.md` (todo el documento)
- `skills/video/references/dramaturgy.md` (todo el documento)
- `skills/video/references/patterns-and-genres.md` (todo el documento)
- `skills/video/references/race-and-speed.md` (todo el documento)
- `skills/video/references/role-modes.md` (todo el documento)

**4 Shot planning**

- `skills/ai-video-storyboard/SKILL.md` (todo el documento)
- `skills/ai-video-storyboard/examples/tiktok-reel-30s-coffee.md` (todo el documento)
- `skills/storyboard-architect/SKILL.md` (todo el documento)
- `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md` (todo el documento)
- `skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md` (todo el documento)
- `skills/storyboard-architect/examples/shotkit-explainer/storyboard.md` (todo el documento)
- `skills/storyboard-architect/references/beat-frameworks.md` (todo el documento)
- `skills/storyboard-architect/references/on-screen-text.md` (todo el documento)
- `skills/storyboard-architect/references/shot-grammar.md` (todo el documento)
- `skills/storyboard-architect/references/timing-rules.md` (todo el documento)
- `skills/storyboard-architect/templates/storyboard.md.tpl` (todo el documento)

**5 Imagen**

- `flujos/flujo-anclas.html` (todo el documento)
- `skills/video/references/animatic-keyframes.md` (todo el documento)
- `skills/visual-asset-critic/SKILL.md` (todo el documento)
- `skills/visual-asset-critic/references/critique-rubric.md` (todo el documento)
- `skills/visual-prompt-forge/SKILL.md` (todo el documento)

**6 Video**

- `skills/video/SKILL.md` (todo el documento)
- `skills/video/references/fixes-and-skeletons.md` (todo el documento)
- `skills/video/references/kling.md` (todo el documento)
- `skills/video/references/seedance-25.md` (todo el documento)
- `skills/video/references/seedance.md` (todo el documento)
- `skills/video/references/universal-rules.md` (todo el documento)
- `skills/video/references/veo.md` (todo el documento)
- `skills/visual-media/SKILL.md` › Producción de video
- `skills/visual-prompt-forge/SKILL.md` (todo el documento)

**7 Paquete y entrega**

- `skills/ai-production-director/references/production-package.md` (todo el documento)
- `skills/storyboard-html-preview/SKILL.md` (todo el documento)

**ORQUESTACIÓN**

- `skills/ai-production-director/SKILL.md` (todo el documento)

**Post-producción**

- `skills/visual-media/SKILL.md` › Postproducción y edición

### FLUJO · Flujo

**FL01 Producción de spot publicitario**

- `flujos/flujo-spot.html` (todo el documento)

**FL03 Imágenes ancla**

- `flujos/flujo-anclas.html` (todo el documento)

### BIB · Biblioteca de plantillas de look

**1**

- `skills/image/references/multi-panel.md` › 1. 9-Cell Grid Storyboard
- `skills/image/references/multi-panel.md` › 2. 2x2 Editorial Portrait Grid
- `skills/image/references/multi-panel.md` › 3. 3-Panel Campaign Collage
- `skills/image/references/multi-panel.md` › 4. 4x3 Borderless Grid
- `skills/image/references/multi-panel.md` › 5. 6-Frame Cinematic Sequence
- `skills/image/references/multi-panel.md` › 6. Before/After Split
- `skills/image/references/multi-panel.md` › 7. 12-Panel Storyboard Poster

**Documentos y secciones**

- `skills/image/references/patterns/character-design.md` (todo el documento)
- `skills/image/references/patterns/ecommerce.md` (todo el documento)
- `skills/image/references/patterns/fashion-editorial.md` (todo el documento)
- `skills/image/references/patterns/food-beverage.md` (todo el documento)
- `skills/image/references/patterns/portrait-cinema.md` (todo el documento)
- `skills/image/references/patterns/poster-illustration.md` (todo el documento)
- `skills/image/references/patterns/ui-social.md` (todo el documento)

### EJ · Ejemplos (efecto probable: da un ejemplo o una plantilla)

**1**

- `skills/image/references/creative-direction.md` › Creative Prompt Examples
- `skills/image/references/prompt-framework.md` › Examples by Type
- `skills/image/references/text-rendering.md` › Examples
- `skills/storyboard-architect/SKILL.md` › Examples
- `skills/storyboard-html-preview/SKILL.md` › Examples
- `skills/video/references/animatic-keyframes.md` › 8. Worked keyframe board for a 30s race spot
- `skills/video/references/dramaturgy.md` › 14. Worked example. Guilt, 30 seconds
- `skills/video/references/seedance-25.md` › 19. Worked examples (official, verbatim)
- `skills/video/references/seedance.md` › 16. Worked example. 15-second tragicomedy as 3 × 5s clips
- `skills/visual-asset-critic/SKILL.md` › Example output
- `skills/visual-prompt-forge/SKILL.md` › Examples
- `skills/visual-prompt-forge/adapters/flux.md` › Example
- `skills/visual-prompt-forge/adapters/gpt-image.md` › Example
- `skills/visual-prompt-forge/adapters/hailuo.md` › Example
- `skills/visual-prompt-forge/adapters/ideogram.md` › Example (Mode 2)
- `skills/visual-prompt-forge/adapters/kling.md` › Example
- `skills/visual-prompt-forge/adapters/midjourney.md` › Example
- `skills/visual-prompt-forge/adapters/nano-banana.md` › Example (image-to-image variant)
- `skills/visual-prompt-forge/adapters/nano-banana.md` › Example (text-to-image)
- `skills/visual-prompt-forge/adapters/seedance.md` › Example
- `skills/visual-prompt-forge/adapters/seedream.md` › Example
- `skills/visual-prompt-forge/adapters/veo.md` › Example

**Documentos y secciones**

- `skills/ai-video-storyboard/examples/tiktok-reel-30s-coffee.md` (todo el documento)
- `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` (todo el documento)
- `skills/brand-lock-extractor/examples/brand-lock.md` (todo el documento)
- `skills/brand-lock-extractor/examples/input-brief.md` (todo el documento)
- `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` (todo el documento) · idéntico en 2 documentos más
- `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md` (todo el documento)
- `skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md` (todo el documento)
- `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` (todo el documento)
- `skills/storyboard-architect/examples/shotkit-explainer/storyboard.md` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/prompts/round-1/flux.txt` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/prompts/round-2/revised-flux.txt` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/flux.txt` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/ideogram.txt` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/kling.txt` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/midjourney.txt` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/nano-banana.txt` (todo el documento)
- `skills/visual-prompt-forge/examples/one-shot-all-adapters/seedream.txt` (todo el documento)

### Q · Probablemente no impacta (qué es)

**Código o herramienta**

- `skills/brand-lock-extractor/tools/README.md` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/_shotkit.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/_template.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/check.sh` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/copy-prompt.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/shots-to-html.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/validate_brand_lock.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/validate_capabilities.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/validate_critique.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/validate_prompts.py` (todo el documento) · idéntico en 3 documentos más
- `skills/brand-lock-extractor/tools/validate_provenance.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/validate_schemas.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/validate_shots.py` (todo el documento) · idéntico en 4 documentos más
- `skills/brand-lock-extractor/tools/validate_skills.py` (todo el documento) · idéntico en 4 documentos más
- `skills/storyboard-architect/examples/30s-pain-proof-promise/preview.html` (todo el documento)
- `skills/storyboard-architect/examples/30s-pain-proof-promise/run.json` (todo el documento)
- `skills/storyboard-architect/examples/30s-pain-proof-promise/shots.json` (todo el documento)
- `skills/storyboard-architect/examples/30s-pain-proof-promise/text-overlays.json` (todo el documento)
- `skills/storyboard-architect/examples/60s-founder-explainer/preview.html` (todo el documento)
- `skills/storyboard-architect/examples/60s-founder-explainer/run.json` (todo el documento)
- `skills/storyboard-architect/examples/60s-founder-explainer/shots.json` (todo el documento)
- `skills/storyboard-architect/examples/60s-founder-explainer/text-overlays.json` (todo el documento)
- `skills/storyboard-architect/examples/shotkit-explainer/preview.html` (todo el documento)
- `skills/storyboard-architect/examples/shotkit-explainer/run.json` (todo el documento)
- `skills/storyboard-architect/examples/shotkit-explainer/shots.json` (todo el documento)
- `skills/storyboard-architect/examples/shotkit-explainer/text-overlays.json` (todo el documento)
- `skills/storyboard-architect/templates/run.schema.json` (todo el documento)
- `skills/storyboard-architect/templates/shots.schema.json` (todo el documento)
- `skills/storyboard-architect/templates/text-overlays.schema.json` (todo el documento)
- `skills/storyboard-html-preview/templates/preview.html.tpl` (todo el documento)
- `skills/storyboard-html-preview/templates/print.css.tpl` (todo el documento)
- `skills/storyboard-html-preview/templates/styles.css.tpl` (todo el documento)
- `skills/visual-asset-critic/examples/critique.accept.json` (todo el documento)
- `skills/visual-asset-critic/examples/critique.revise.json` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot_01.critique.json` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot_02.critique.json` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/critiques/round-2/shot_02.critique.json` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/preview.html` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/run.json` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/shots.json` (todo el documento)
- `skills/visual-asset-critic/examples/worked-run/text-overlays.json` (todo el documento)
- `skills/visual-asset-critic/templates/critique.schema.json` (todo el documento)
- `skills/visual-prompt-forge/adapters/capabilities.schema.json` (todo el documento)
- `skills/visual-prompt-forge/tools/validate_prompts.py` (todo el documento)

**Dato técnico de interfaz**

- `skills/visual-prompt-forge/adapters/flux.md` › API access
- `skills/visual-prompt-forge/adapters/gpt-image.md` › API access
- `skills/visual-prompt-forge/adapters/midjourney.md` › API access note
- `skills/visual-prompt-forge/adapters/nano-banana.md` › API access
- `skills/visual-prompt-forge/adapters/seedream.md` › API access

**Licencia o crédito**

- `skills/ai-video-storyboard/SKILL.md` › License
- `skills/brand-lock-extractor/LICENSE` (todo el documento) · idéntico en 4 documentos más
- `skills/image/LICENSE` (todo el documento) · idéntico en 1 documento más
- `skills/image/NOTICE` (todo el documento) · idéntico en 1 documento más

**Nota interna o de origen**

- `skills/ai-production-director/SKILL.md` › 9. Referencias de este skill
- `skills/brand-lock-extractor/brand-packs/README.md` › Contributing examples · idéntico en 1 documento más
- `skills/screenwriter/SKILL.md` › Additional Resources
- `skills/storyboard-architect/SKILL.md` › Reference files
- `skills/video/references/seedance.md` › 17. Seedance 2.5 → read `seedance-25.md`
- `skills/visual-asset-critic/SKILL.md` › Reference
- `skills/visual-media/SKILL.md` › Recursos
- `skills/visual-prompt-forge/SKILL.md` › Reference files

**Rótulo o encabezado**

- `skills/screenwriter/references/advanced-techniques.md` › Table of Contents
- `skills/screenwriter/references/pipeline-integration.md` › Table of Contents
- `skills/video/references/animatic-keyframes.md` › Contents
- `skills/video/references/camera-lighting-vocabulary.md` › Contents
- `skills/video/references/dramaturgy.md` › Contents
- `skills/video/references/fixes-and-skeletons.md` › Contents
- `skills/video/references/kling.md` › Contents
- `skills/video/references/patterns-and-genres.md` › Contents
- `skills/video/references/race-and-speed.md` › Contents
- `skills/video/references/role-modes.md` › Contents
- `skills/video/references/seedance-25.md` › Contents
- `skills/video/references/seedance.md` › Contents
- `skills/video/references/universal-rules.md` › Contents
- `skills/video/references/veo.md` › Contents

### Sin categoría por encabezado

Secciones cuyo nombre no señala ninguna categoría y cuyo documento tampoco la tiene. Se catalogan al clasificar sus textos.

- `skills/image/SKILL.md` › (texto antes del primer encabezado)
- `skills/image/references/creative-direction.md` › (texto antes del primer encabezado)
- `skills/image/references/golden-rules.md` › (texto antes del primer encabezado)
- `skills/image/references/prompt-framework.md` › (texto antes del primer encabezado)
- `skills/image/references/structural.md` › (texto antes del primer encabezado)
- `skills/image/references/structural.md` › Precision Control
- `skills/visual-media/SKILL.md` › (texto antes del primer encabezado)
- `skills/visual-media/SKILL.md` › Contenido de formato corto
- `skills/visual-media/SKILL.md` › Herramientas recomendadas
- `skills/visual-prompt-forge/references/failure-modes.md` › (texto antes del primer encabezado)
- `skills/visual-prompt-forge/references/prompt-anatomy.md` › (texto antes del primer encabezado)
- `skills/visual-prompt-forge/references/prompt-anatomy.md` › Why this matters operationally

## Nivel 3 · Caso de uso, de lo general a lo específico

El orden es el del catálogo de casos de uso (construcción del caso, de lo general a lo específico). Las categorías y sus valores son los de la taxonomía actual, tal cual; se dejan fuera solo los valores de las ramas de video.


### 3.1 Qué se hace

#### FLUJO · Flujo

| Valor | Definición |
|---|---|
| FL01 Producción de spot publicitario | Megaflujo E0–E7 y POST; E5 invoca FL02 y FL03; la ruta operativa vigente es Video publicitario |
| FL02 Génesis sin referencia | Subflujo atómico: solo texto en la entrada; salida activo ACCEPT canonizado con hash |
| FL03 Imágenes ancla | A0–A12: tarjeta de ancla, rutas por acción y sujetos, tratamiento, modelo, ensamblaje, lints, crítica, canonización, motion brief |
| FL04 Activo directo sin preproducción | Operaciones: imagen sin referencia; imagen con referencias, composición o edición; imagen ancla independiente; clip de video independiente |

#### F10 · Modo de generación

| Valor | Definición |
|---|---|
| génesis sin referencias (caso 1, T1) | solo texto; fija la parte del sujeto que lleva la identidad |
| ancla con referencias (caso 2, T2 a T4) | texto más génesis aprobadas: cuerpo con rostro adjunto, cuadro de escena, keyframe |
| composición de varias referencias | une elementos de varias referencias sin ser cuadro de clip: producto en escena, póster |
| edición de imagen existente (T5) | cambia una zona de una imagen aprobada y conserva el resto |
| transferencia de estilo | aplica el estilo de una imagen de referencia a otro contenido |
| boceto o wireframe a final | un boceto, layout o plano controla la composición |
| edición: quitar objeto | subtipo de «edición de imagen existente (T5)» |
| edición: añadir objeto | subtipo de «edición de imagen existente (T5)» |
| edición: cambiar luz o clima | subtipo de «edición de imagen existente (T5)» |
| edición: colorizar | subtipo de «edición de imagen existente (T5)» |
| edición: restaurar | subtipo de «edición de imagen existente (T5)» |
| edición: traducir texto | subtipo de «edición de imagen existente (T5)» |
| edición: cambiar vestuario | subtipo de «edición de imagen existente (T5)» |
| edición: cambiar mobiliario u objeto | subtipo de «edición de imagen existente (T5)» |
| análisis de imagen a prompt | — |

#### F29 · Modelo

| Valor |
|---|
| Nano Banana 2 |
| Nano Banana Pro |
| GPT Image 2 |
| Flux |
| Midjourney |
| Ideogram |
| Seedream |
| Nano Banana 2 Lite |
| gpt-image-1.5 |
| gpt-image-1 |
| gpt-image-1-mini |

#### F35 · Migración de versión de modelo

| Valor | Definición |
|---|---|
| sí | las reglas de migración entre versiones de modelo |
| no | — |

#### F04 · Tipo de pieza

| Valor | Definición |
|---|---|
| editorial | imagen con lenguaje de revista; se combina con la temática: editorial de moda, deportiva, musical, gastronómica |
| key visual de campaña | imagen principal de una campaña publicitaria |
| e-commerce o catálogo | producto para tienda o catálogo |
| retrato | una o varias personas como sujeto de la pieza (retrato individual o de grupo) |
| póster o key art | pieza gráfica con título o composición de cartel |
| post o historia para redes | imagen para feed o historias |
| miniatura | thumbnail de video con rostro y gancho |
| UI o mockup | pantallas, apps, maquetas de interfaz |
| slide o presentación | una diapositiva: portada, datos, comparación, proceso |
| storyboard o multipanel | varios paneles en una imagen |
| diseño de personaje | hoja o maestro de un personaje |
| visualización arquitectónica | render de espacio, plano a 3D |
| identidad de marca | logo, sistema visual, aplicaciones |
| scroll | Subtipo de pieza gráfica de la rama imagen denominado «scroll» en la fuente; sin inferir interfaz, marca, desplazamiento interactivo ni requisitos no expresos. |
| infografía o diagrama | — |
| concept art | — |
| pieza de portafolio | — |

#### PUBLICACION · Lugar de publicación (subcategoría de F04)

| Valor | Definición |
|---|---|
| TikTok → alcance de plataforma; ubicación sin restricción documental | Plataforma de video corto vertical. |
| Instagram → alcance de plataforma; ubicación sin restricción documental | Plataforma social con varias ubicaciones de publicación citadas en las fuentes (feed, Stories, carrusel, anuncio). |
| Instagram → Stories | Ubicación vertical a pantalla completa de Instagram. |
| Instagram → feed | Ubicación de publicaciones en el feed de Instagram. |
| YouTube → alcance de plataforma; ubicación sin restricción documental | Plataforma de video con formato horizontal y ubicación Shorts. |
| YouTube → Shorts | Ubicación de video vertical corto dentro de YouTube. |
| Superficie literal Reels; sin condición de plataforma inferida | Ubicación de video vertical corto. Las fuentes la nombran sola («Reels») y como «TikTok Reel»; no establecen a qué plataforma pertenece. |
| Douyin → alcance de plataforma; ubicación sin restricción documental | Plataforma de video corto vertical citada junto a TikTok, Reels y Shorts. |
| Facebook → feed (alcance de la fuente citada) | Plataforma social citada para publicaciones cuadradas de feed. |
| LinkedIn → piezas sociales; carrusel en el ejemplo citado | Plataforma social profesional citada para piezas visuales y carruseles. |
| Sitio web → hero | Destino propio y sección de cabecera identificada literalmente como «website hero». |

#### F06 · Formato de salida

| Valor | Definición |
|---|---|
| 16:9 | horizontal: TV, web, YouTube |
| 9:16 | vertical: Reels, TikTok, Shorts, historias |
| 1:1 | cuadrado: feed |
| 4:5 | vertical corto: feed de Instagram |
| 21:9 | cinemascope |
| 1:4 | vertical extremo; en Nano Banana, exclusivo de NB2 |
| 1:8 | vertical muy extremo; en Nano Banana, exclusivo de NB2 |
| 2:3 | vertical |
| 3:4 | vertical |
| 4:1 | horizontal extremo; en Nano Banana, exclusivo de NB2 |
| 8:1 | horizontal muy extremo; en Nano Banana, exclusivo de NB2 |
| 3:2 | — |

#### F34 · Resolución

| Valor | Definición |
|---|---|
| 1K | — |
| 2K | — |
| 4K | — |

### 3.2 Contexto

#### F03 · Ruta operativa

| Valor | Definición |
|---|---|
| Video publicitario | Flujo publicitario completo conforme a decisiones aprobadas; corresponde a FILM, sin reactivar reglas históricas excluidas. |
| Clip | Ruta con etapas elegidas; solo hereda lo aprobado para Clip. Etapas 1 y 2 si el usuario las mantiene. |

#### F05 · Temática o industria

| Valor | Definición |
|---|---|
| deporte y fitness | atletas, clubes, competencia |
| automotriz y movilidad | autos, motos, bicis |
| música | artistas, conciertos, videoclips |
| moda | prendas, modelos, pasarela |
| comida y bebida | producto comestible o bebida |
| arquitectura e inmobiliaria | espacios y edificios |
| belleza y cuidado personal | cosmética, piel, cabello |
| hospitalidad y viajes | hoteles, destinos |
| retail y supermercado | tiendas, anaquel, promociones |
| tecnología | apps, dispositivos, SaaS |
| salud y bienestar | clínicas, bienestar |
| educación | cursos, material didáctico |
| corporativo | B2B, institucional |
| finanzas y banca | — |
| sector público | — |
| estilo de vida | — |

#### F07 · Género narrativo

| Valor | Definición |
|---|---|
| tragedia doméstica | drama íntimo en interiores, objetos cotidianos cargados |
| drama psicológico | tensión interna del personaje |
| acción | persecución, pelea, riesgo físico |
| carrera y velocidad | vehículo o atleta a velocidad |

#### F08 · Estructura de beats

| Valor | Definición |
|---|---|
| Pain-Reframe-Promise | dolor, reencuadre, promesa |
| Hero Trilogy | héroe, obstáculo, transformación |
| Founder Explainer | quién, por qué, qué se construyó |
| Content Spiral | una idea que se profundiza en vueltas |
| Educational Demo | paso a paso de una tarea |
| Hook / Build / Payoff / CTA | default de TikTok |
| Problem / Solution / Proof / CTA | default de anuncio |
| Atmosphere → Climax | brand story: atmósfera, revelación lenta, clímax, logo |
| Custom | estructura propia declarada |

#### F09 · Patrón de montaje

| Valor | Definición |
|---|---|
| escalada | cada plano sube la tensión |
| ansiedad | presión creciente e inestable |
| descubrimiento | la información se revela por partes |
| catástrofe | construcción hacia un quiebre |
| drama comercial de producto | el producto resuelve la tensión |
| loop de videoclip | ciclo visual sobre el ritmo |

#### F12 · Función del plano

| Valor | Definición |
|---|---|
| hook | detiene el scroll en el primer segundo |
| establecer | dónde estamos; plano abierto o master |
| revelar | entra información nueva al cuadro |
| poder | quién controla la escena; el staging lo dice |
| presión | la tensión crece; movimiento hacia la amenaza o la decisión |
| detalle | objeto, mano, ojo o textura en close-up o macro |
| reacción | consecuencia emocional en un rostro |
| giro interno | el cuerpo muestra el cambio antes de la decisión |
| impacto | el evento visual decisivo: la caída, el golpe, el quiebre |
| secuela | quietud después del impacto |
| salida | la imagen final que se lleva el espectador |
| CTA o logo | llamado a la acción o cierre de marca |

#### F11 · Rol del ancla

| Valor | Definición |
|---|---|
| character ref | maestro de identidad de un personaje |
| environment ref | placa del lugar, vacía |
| keyframe FF | primer frame del clip |
| keyframe LF | último frame del clip |
| hero/macro | producto u objeto en detalle |
| motif insert | objeto ancla que reaparece entre clips |

#### F23 · Referencias adjuntas

| Valor | Definición |
|---|---|
| ninguna | sin referencias |
| persona | rostro o cuerpo de un personaje |
| vestuario | ropa o accesorios |
| lugar | escenario o locación |
| producto o prop | producto u objeto |
| estilo | referencia de look, color o textura |
| estructura o composición | forma, geometría o disposición espacial del cuadro |
| movimiento | acción o trayectoria de un sujeto |
| cámara | movimiento o posición de cámara |
| ritmo | cadencia de la pieza |
| voz | voz de un personaje |
| diálogo | diálogo de un personaje |
| ambiente | sonido ambiente del entorno |
| música | música de la escena |

### 3.3 Qué hay en el cuadro

#### F15 · Sujeto

| Valor | Definición |
|---|---|
| persona | ser humano; identidad fijada con rostro T1 y cuerpo T2 |
| lugar genérico | sitio sin identidad real: una calle, una cocina |
| edificación o landmark | lugar real y reconocible |
| animal | especie animal |
| producto | empaque, comida, bebida, cosmético o dispositivo, genérico o de marca real; la referencia aprobada se exige solo si lleva logo o etiqueta real |
| objeto o prop | herramienta, vehículo, mobiliario, objeto ancla |
| planta o especie vegetal | Vegetal o especie vegetal cuando es el sujeto regulado. No se asimila a animal, lugar o producto. |

#### F19 · Número de sujetos

| Valor | Definición |
|---|---|
| 0 | placa: cero sujetos individuales; puede contener una multitud anónima, que no cuenta como sujetos |
| 1 | un sujeto individual, con o sin placa de multitud |
| 2 | dos sujetos individuales, con o sin contacto físico |
| 3 o más | tres o más sujetos individuales con identidad: grupo ensamble de 3 a 8 identidades reconocibles; la multitud anónima no cuenta como sujetos y se conserva como placa o capa anónima separada |

#### F20 · Identidad de las personas

| Valor | Definición |
|---|---|
| todas | grupo ensamble: cada miembro reconocible y consistente |
| solo los héroes | hasta 3 reconocibles, el resto anónimo |
| ninguna | multitud anónima: nadie con rostro legible |

#### F21 · Contacto físico entre personas

| Valor | Definición |
|---|---|
| sí | abrazo, tackle, manos que se tocan |
| no | no hay contacto |

#### F13 · Tipo de acción

| Valor | Definición |
|---|---|
| A pose sostenida | quietud; el sujeto no cambia de estado |
| B instante pico | un instante de máxima fuerza, congelado |
| C movimiento continuo | desplazamiento sostenido |
| D fenómeno de luz o clima | el evento es la luz o el clima |
| E interacción o diálogo | dos o más personas se relacionan o hablan |
| F multitud | la masa hace el trabajo |
| G acuática en superficie | el sujeto se desplaza sobre el agua |
| H subacuática | cámara y sujeto sumergidos |

#### F14 · Régimen físico

| Valor | Definición |
|---|---|
| 01 agua en superficie | wakeboarding, surf, jet ski, remo, esquí acuático |
| 02 ruptura de superficie | clavado, nadador emergiendo, salto de ballena, split-level |
| 03 subacuático | buceador en cenote, nadador bajo el agua, apnea |
| 04 objeto balístico | pelota, balón, gota, flecha, chispa |
| 05 vehículo | auto de carreras, moto, bici, tren, dron |
| 06 cuerpo en esfuerzo | corredor en la cinta, salto, golpe, levantamiento |
| 07 luz y clima | rayo, amanecer, lluvia, polvo, niebla, nieve |
| 08 multitud anónima | estadio, manifestación, calle llena, público |
| 09 grupo ensamble | quinteto, grupo de K-pop, equipo, familia |

#### F16 · Espacio

| Valor | Definición |
|---|---|
| interior | bajo techo |
| exterior | al aire libre, incluida el agua abierta |

#### F32 · Texto en la imagen

| Valor | Definición |
|---|---|
| sin texto | — |
| texto corto | — |
| texto extenso o pequeño | — |

#### F33 · Complejidad de escena

| Valor | Definición |
|---|---|
| simple | — |
| compleja | 5 o más elementos |

### 3.4 Cómo se ve

#### F17 · Estilo visual

| Valor | Definición |
|---|---|
| documental | luz dura, piel real, grano de reportaje |
| narrativo cinematográfico | una fuente domina, 70% en sombra |
| comercial pulido | luz limpia, producto legible |
| editorial | contraste alto y desaturado, pose y styling de revista |
| retro o vintage | película de otra época: "1980s color film", tonos análogos, negros levantados |
| blanco y negro | grano clásico tipo Ilford HP5 |
| minimalista | manda el espacio negativo |
| race/kinetic | velocidad, paleta fría |
| UGC/social | celular, luz natural |
| experimental | cross-processing, colores desplazados |
| anclado en época, cultura o autor | — |
| brutalista | — |
| futurista | — |

#### F18 · Técnica de representación

| Valor | Definición |
|---|---|
| fotorrealista | debe parecer foto o filmación real |
| ilustración | stickers, íconos, arte dibujado |
| render 3D | objeto o espacio modelado |
| animación 2D | dibujo animado |
| animación 3D | personajes o mundos 3D animados |
| motion graphics | gráfico y tipografía en movimiento |
| pixel art | imagen por píxeles |

### 3.5 Cámara

#### F24 · Tamaño de plano

| Valor | Definición |
|---|---|
| EWS extreme wide | sujeto pequeño en el entorno |
| WS wide | cuerpo entero con entorno |
| MLS medium wide | cuerpo entero, poco entorno |
| MS medium | de la cintura para arriba |
| MCU medium close-up | cabeza y hombros |
| CU close-up | cabeza, o mano con objeto |
| ECU extreme close-up | ojos, manos, un detalle |
| macro insert | detalle a escala macro |
| objeto entero | un objeto completo como sujeto del cuadro |

#### F25 · Ángulo

| Valor | Definición |
|---|---|
| eye-level | a la altura de los ojos; paridad |
| low | desde abajo; dominio o fuerza |
| high | desde arriba; vulnerabilidad |
| top-down u overhead | cenital; esquema, geometría |
| dutch | cámara inclinada; un beat de inestabilidad |
| worm's eye | desde el suelo |
| POV | lo que ve el personaje |
| over-the-shoulder | sobre el hombro de otro personaje |
| perfil | el sujeto de lado |

#### F22 · Tamaño del rostro

| Valor | Definición |
|---|---|
| ≥20% | el rostro manda; la identidad se verifica al zoom |
| <20% | rostro pequeño en el cuadro |
| sin rostro visible | silueta, casco, espalda |

#### F26 · Movimiento de cámara

| Valor | Definición |
|---|---|
| estática o locked-off | sin movimiento |
| push-in (lento o rápido) | la cámara avanza hacia el sujeto |
| pull-back | la cámara se aleja |
| dolly in / dolly out | avance o retroceso sobre riel |
| tracking o lateral | acompaña al sujeto en paralelo |
| pan | giro horizontal |
| tilt | giro vertical |
| handheld | temblor orgánico de cámara en mano |
| orbit | rodea al sujeto |
| gimbal glide | deslizamiento estabilizado |
| crane | grúa que sube o baja |
| aéreo o dron | desde el aire |
| FPV | vuelo de dron en primera persona |
| whip pan | paneo rápido como transición |
| snap zoom | zoom brusco |
| rack focus | el foco cambia de plano |
| dolly zoom | efecto Hitchcock |
| dive | la cámara se desploma hacia abajo |
| one-take | plano secuencia |
| bullet time | tiempo congelado con cámara girando |
| speed ramp | acelera, frena, acelera |

#### F27 · Transición

| Valor | Definición |
|---|---|
| corte natural | punto de edición simple |
| fade in / fade out | desde o hacia negro |
| disolvencia | fundido cruzado de 1 a 2 s |
| flash blanco o negro | un cuadro de golpe como puntuación |
| wipe | el cuadro nuevo empuja al anterior |
| occlusion mask | un objeto tapa la lente y revela la escena nueva |
| match cut | una forma o movimiento parecido une dos escenas |
| action cut o whip | el corte se esconde en un movimiento rápido |
| motion relay | el sujeto sale del cuadro A y sigue en el B |
| zoom-through | la cámara atraviesa una pupila, cerradura o ventana |
| ink-wash dissolve | sangrado estilizado, animación |

#### F28 · Audio

| Valor | Definición |
|---|---|
| diálogo | personajes hablando en cuadro |
| voz en off | narración fuera de cuadro |
| SFX de ambiente | room tone, ciudad, lluvia, viento |
| SFX de cuerpo y acción | respiración, pasos, tela, puerta |
| SFX de evento dramático | silencio súbito, golpe grave, vidrio que se rompe |
| música | pista musical |
| silencio | ausencia deliberada de sonido |

### 3.6 Detalles del caso por materia

Son las materias de F30 cuyo vocabulario describe el caso (el catálogo las marca así):

- anatomía, rostro y piel
- animación
- audio
- color, grade y textura
- composición
- continuidad entre clips
- dramaturgia
- encuadre y lente
- estrategia y concepto
- física y movimiento congelado
- identidad y consistencia
- luz
- marca y logos
- materialidad y superficie
- puesta en escena y blocking
- texto en pantalla

## Nivel 4 · Atributos de la regla


#### F01 · Etapa

| Valor | Definición |
|---|---|
| 0 Brand Lock | identidad de marca: paleta, tipografía, never list, voz |
| 1 Estrategia creativa | brief, SMP, territorios, concept cards, selección |
| 2 Guion | escenas, sluglines, acción, diálogo, XML |
| 3 Dirección cinematográfica | fórmula de escena, blocking, cámara motivada, 5 anclas, vocabulario prohibido |
| 4 Shot planning | shots.json, timing, texto en pantalla, series lock |
| 5 Imagen | génesis, anclas, edición, crítica y canonización |
| 6 Video | prompts de movimiento |
| 7 Paquete y entrega | carpeta final, preview, trazabilidad, créditos |
| Post-producción | generar clips, ensamblar, grade, audio, export |
| ORQUESTACIÓN | Control del proceso; conserva condiciones de entrada, etapa y cierre de gate. No significa selección incondicional de toda regla multietapa. |

#### F02 · Paso

| Etapa | Pasos |
|---|---|
| 0 | E0.1 reunir fuentes · E0.2 extraer las 9 secciones · E0.3 asignar confianza · E0.4 escribir brand-lock.md |
| 1 | E1.1 lectura del brief · E1.2 territorios · E1.3 concept cards · E1.4 matriz · E1.5 dirección narrativa |
| 2 | E2.1 analizar concepto · E2.2 breakdown · E2.3 escribir escenas · E2.4 XML |
| 3 | E3.1 fórmula de escena · E3.2 blocking y staging · E3.3 cámara y lente · E3.4 luz, color y ritmo · E3.5 5 anclas |
| 4 | E4.1 beat framework · E4.2 timing · E4.3 shot list · E4.4 texto separado · E4.5 series lock · E4.6 rationale y run.json |
| 5 | E5.1 plan de anchors · E5.2 génesis sin referencias · E5.3 maestros derivados · E5.4 cuadros con referencias · E5.5 edición quirúrgica · E5.6 borradores · E5.7 crítica · E5.8 revisión · E5.9 canonizar |
| 6 | E6.1 motion draft · E6.2 sintaxis del modelo · E6.3 continuidad · E6.4 dramaturgy check · E6.5 linter · E6.6 micro-gate y entrega |
| 7 | E7.1 árbol del paquete · E7.2 preview · E7.3 checklist de post · E7.4 trazabilidad |
| Post | POST.1 generar y verificar clips · POST.2 ensamblar y exportar |

#### F30 · Qué regula

| Valor | Definición |
|---|---|
| orquestación y control de flujo | activación, selección de skills, orden de etapas y control de avance; no es materia creativa |
| estrategia y concepto | brief, territorios, concepto |
| estructura narrativa y diálogo | escenas, beats, líneas |
| dramaturgia | fórmula de escena, 3 detalles, emoción traducida a cuerpo |
| encuadre y lente | tamaño de plano, focal, profundidad de campo |
| ángulo | altura y orientación de la cámara |
| movimiento de cámara | cómo se mueve la cámara |
| luz | fuente, dirección, dureza, ratio |
| color, grade y textura | paleta, grade, grano, halación |
| composición | spine, planos, espacio negativo |
| identidad y consistencia | que el sujeto se sostenga entre imágenes y clips |
| anatomía, rostro y piel | manos, rostro, piel documental |
| física y movimiento congelado | cues de velocidad, blur, estado posterior |
| texto en pantalla | overlays y texto dentro de la imagen |
| marca y logos | brand-lock, logos, productos reales |
| estructura y sintaxis del prompt | orden de bloques, slots, palabras permitidas y prohibidas |
| parámetros técnicos | ratio, resolución, duración, calidad |
| audio | diálogo, VO, SFX, música |
| continuidad entre clips | que un clip empate con el siguiente |
| crítica y revisión | criterios para aceptar o rechazar |
| trazabilidad y entrega | registro, carpeta, créditos |
| materialidad y superficie | propiedades visibles de materiales, texturas y acabados |
| puesta en escena y blocking | posiciones, desplazamientos y relaciones espaciales entre sujetos y objetos |
| animación | técnicas y principios de construcción del movimiento animado |

#### F31 · Condición para avanzar

| Valor | Definición |
|---|---|
| no | no es un gate |
| sí, la verifica una herramienta | validate_shots, linter, auditor |
| sí, revisión manual obligatoria | gate que el agente o la persona comprueba sin herramienta y sin nuevo OK del usuario: razón dramática escrita de cada decisión de cámara (etapa 3), dramaturgy check de 6 puntos y auditoría de 3 detalles de video (etapa 6) |
| sí, la aprueba el usuario | gates 1, 2 y 4 del director |

#### AMBITO · Ámbito funcional

| Valor | Definición |
|---|---|
| Preproducción | marca, estrategia, guion, dirección cinematográfica, planificación de shots |
| Creación de imagen | génesis, maestros, cuadros, anclas, edición de imagen |
| Creación de video | prompts de movimiento, sintaxis de modelo, continuidad, clips |
| Crítica, validación y aceptación | crítica de renders, validadores, gates, canonización; se vincula al medio evaluado |
| Audio y música independientes | audio que no sale del modelo de generación visual |
| Postproducción | ensamblado, grade, overlays, exportación |
| Empaquetado y entrega | paquete de producción, preview, trazabilidad y créditos |
| Orquestación y control de flujo | activación, selección de skills, orden de etapas, gates y escalamiento. Cada aplicación tiene disparador, condición y destino de control explícitos; no se le asigna una exclusión por defecto. |

#### USO OPERATIVO · Uso operativo (por aplicación de la regla)

| Valor | Definición |
|---|---|
| ACTIVO EN SELECCIÓN | la aplicación participa en la selección de reglas para generar imagen o video |
| INCORPORADA A TEMPLATE | aplicación incorporada y verificada en su template; incluye sintaxis de modelo aplicada una vez a la ficha. No se vuelve a extraer para cada caso; permanece clasificada. La incorporación exige vínculo regla → campo/bloque → condición → validación; si varía por caso, esa condición se evalúa al instanciar el template. |
| APLICACIÓN EN CONSTRUCCIÓN DE TEMPLATE | instrucción estructural seleccionable durante la construcción o actualización del template; exige destino y prueba de incorporación antes de publicar ese template. Expresa cuándo se usa, no aplaza su clasificación. |
| APLICACIÓN EN CONTROL O ENTREGA | aplicación de crítica, audio, postproducción o entrega seleccionable en su ruta específica, con disparador y destino. Su separación de recuperación de prompts requiere decisión aplicable y alcance documentados; una regla mixta conserva cada ruta. |
| INSERCIÓN MECÁNICA | la regla se agrega al prompt sin selección en cuanto el caso fija los datos de lista cerrada de su condición |
| BIBLIOTECA DE PLANTILLAS | plantilla de un look concreto: se ofrece por tipo de pieza y estilo, el usuario confirma como máximo una y se inserta |

#### METADATOS · Campos de la regla

| Campo | Valores o formato | Obligatorio |
|---|---|---|
| ID persistente | INV-/REG-nnnnnn; independiente de archivo, línea y texto | sí |
| documento · encabezado | archivo del corpus autorizado y ruta de títulos | sí |
| localización | líneas inicial–final; páginas asignadas inicial–final (50 líneas por página, marcadas ASIGNADA); paginación original si existe | sí |
| versión | hash del archivo original, hash de la representación textual (HTML) y hash del texto de la unidad | sí |
| idioma del enunciado | en · es · ru | sí |
| objeto regulado | activo visual o sonoro · documento · archivo · paquete de entrega · registro de ejecución (run) · campo o esquema | sí |
| medio del activo | rama activo: imagen fija · imagen secuencial · video · audio · pieza multimodal; otras ramas: se tipan por objeto regulado, sin valor ficticio de medio | obligatorio en la rama activo |
| unidad | fotograma · panel · clip · secuencia · escena · documento · archivo · paquete de entrega · registro (run) · campo o esquema · imagen fija suelta; según objeto y texto contextual | sí |
| referencia adjunta | tupla (medio ∈ imagen · video · audio; papel ∈ valores de la faceta 23; identificador, archivo y hash del adjunto); una por adjunto, de modo que cada papel queda asociado a su archivo | si la regla o el caso usan referencias |
| rutas de aplicación | una o más tuplas flujo → sección → paso → condición | sí |
| ámbito funcional · uso operativo | por aplicación (ver AMBITO y USO OPERATIVO) | sí |
| tipo de enunciado · fuerza normativa | sus valores del tesauro | sí |
| origen de evidencia · evidencia de la afirmación fuente | origen documentado separado de los descriptores, como metadatos documentales; nunca estados de clasificación ni filtros de elegibilidad | sí |
| adopción canónica | «adopción documental» (regla original de una skill, con fuente y autoridad resueltas; no exige ejercicio propio) · «Familia de régimen en borrador documental» y «Canonizada» (solo entradas del protocolo de familias de régimen) · «excluida por decisión del usuario» · «refutada» · «histórica» | sí |
| condición | grupo de condiciones: operador TODAS, ALGUNA o NINGUNA y sus miembros | si es condicional |
| estado de evidencia de capacidad · dependencia | sus valores del tesauro | si declara capacidad de modelo |
| estado del modelo citado | vigente · histórico, con versión y fecha de verificación | si nombra un modelo |
| autoridad | materia sobre la que tiene autoridad · ámbito · criterio de precedencia | si el texto la establece |
| precedencia | la precedencia aplicable entre los textos en conflicto | si hay conflicto documentado |
