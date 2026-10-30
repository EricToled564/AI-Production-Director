# Taxonomía de clasificación para imágenes — PROPUESTA para aprobación de Eric

Vale igual para cualquier modelo. La clasificación se hace modelo por modelo (hoy GPT Image 2) con el valor de F29 de cada texto.
Armada solo con: (1) la clasificación que Eric definió al empezar esta etapa; (2) los nombres de los documentos del corpus y sus encabezados; (3) el catálogo de casos de uso, en su orden de general a específico; (4) las categorías de la taxonomía actual, tal cual, más las extensiones que Eric aprobó el 23 y el 26 de octubre. Los 1,369 términos del tesauro no se copian: no son categorías (la taxonomía actual los define como etiquetas que cuelgan de las categorías).

## Nivel 1 · ¿El texto impacta la redacción del brief o del prompt?

| Valor | Definición |
|---|---|
| Impacta | El texto cambia lo que se escribe en el brief o en el prompt de una imagen |
| No impacta | El texto no cambia el brief ni el prompt; se clasifica solo por lo que es |

### 1.1 Si impacta: efecto en la redacción

Qué le hace el texto al brief o al prompt. Un texto puede tener varios efectos; se marcan todos.

| Valor | Definición |
|---|---|
| Agrega contenido | Pide que se escriba algo: un dato, un elemento, una descripción o un valor |
| Fija la forma | Fija cómo se escribe: estilo de redacción, estructura, formato, apartados, longitud o sintaxis |
| Establece un orden | Fija en qué orden van los bloques o los elementos |
| Excluye | Prohíbe palabras, elementos o formas de escribir |
| Fija un parámetro | Fija un valor técnico de la generación: ratio, tamaño, calidad u otro |

### 1.2 Si impacta: dónde actúa

| Valor | Definición |
|---|---|
| Brief | Cambia lo que el brief pide o registra |
| Prompt | Cambia lo que se escribe en el prompt |
| Brief y prompt | Cambia los dos |

### 1.3 Si impacta: alcance y destino

El alcance decide adónde va la regla: al template, como instrucción de llenado, o a la selección caso por caso.

| Valor | Definición | Destino |
|---|---|---|
| Universal | Vale para todo brief o prompt de imagen, de cualquier modelo y cualquier caso. Si su forma cambia según el modelo, cada template la lleva en la forma de su modelo | Instrucción de llenado en el template de cada modelo; se usa una vez y no se vuelve a seleccionar. Uso operativo: INCORPORADA A TEMPLATE |
| Semiuniversal | Depende solo del modelo, de la operación o de los dos, y de ningún otro dato del caso | Instrucción de llenado en el template de ese modelo u operación; se usa una vez y no se vuelve a seleccionar. Uso operativo: INCORPORADA A TEMPLATE |
| Específica del caso | Depende de algún otro dato del caso (los del nivel 3: tipo de pieza, sujeto, acción, estilo, cámara, etc.) | Se selecciona caso por caso con su condición. Uso operativo: ACTIVO EN SELECCIÓN |

### Si no impacta: qué es el texto

Propuesta: los tipos que la base del corpus ya asigna a cada texto, sin leerlos.

| Tipo de documento | Textos |
|---|---|
| referencia | 4,010 |
| herramienta | 2,892 |
| ejemplo | 2,171 |
| SKILL | 1,165 |
| plantilla | 853 |
| adaptador | 745 |
| flujo | 612 |
| licencia | 337 |
| brand-pack | 218 |

| Tipo de unidad | Textos |
|---|---|
| bloque de código fuente | 2,487 |
| ítem de lista | 2,416 |
| párrafo | 1,972 |
| línea JSON | 1,483 |
| encabezado | 1,263 |
| línea de texto (HTML) | 1,223 |
| fila de tabla | 536 |
| bloque de código | 429 |
| puntuación JSON | 380 |
| bloque de texto | 359 |
| separador | 189 |
| separador de tabla | 104 |
| cabecera de tabla | 90 |
| cita en bloque | 61 |
| frontmatter | 11 |

## Nivel 2 · Documento y encabezado

Dónde está el texto: skill → documento (con su tipo) → encabezado. 12 skills, 206 documentos, 1,393 encabezados. Sale de la base del corpus tal cual.


### ai-production-director

- **skills/ai-production-director/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - AI Production Director
  - AI Production Director › 1. Mapa de sub-skills
  - AI Production Director › 2. Selección de track
  - AI Production Director › 3. Las etapas
  - AI Production Director › 3. Las etapas › Etapa 0 — Brand Lock *(solo si hay marca/cliente)*
  - AI Production Director › 3. Las etapas › Etapa 1 — Creative Strategy
  - AI Production Director › 3. Las etapas › Etapa 2 — Screenwriting
  - AI Production Director › 3. Las etapas › Etapa 3 — Cinematic Direction
  - AI Production Director › 3. Las etapas › Etapa 4 — Shot Planning
  - AI Production Director › 3. Las etapas › Etapa 5 — Anchor Images
  - AI Production Director › 3. Las etapas › Etapa 6 — Video Prompts
  - AI Production Director › 3. Las etapas › Etapa 7 — Package & Delivery
  - AI Production Director › 4. Interacción con el usuario entre etapas
  - AI Production Director › 5. Ejecución por etapa — regla de carga
  - AI Production Director › 6. Reglas de resolución de conflictos
  - AI Production Director › 6. Reglas de resolución de conflictos › 6.1 Vocabulario
  - AI Production Director › 6. Reglas de resolución de conflictos › 6.2 Sintaxis de modelo
  - AI Production Director › 6. Reglas de resolución de conflictos › 6.3 Fuente de verdad estructural
  - AI Production Director › 6. Reglas de resolución de conflictos › 6.4 División forge ↔ smixs
  - AI Production Director › 6. Reglas de resolución de conflictos › 6.5 Atribución
  - AI Production Director › 7. Rol de visual-media (decisión de alcance)
  - AI Production Director › 8. Degradación
  - AI Production Director › 9. Referencias de este skill
- **skills/ai-production-director/references/creative-strategy.md** (referencia)
  - Etapa 1 — Creative Strategy
  - Etapa 1 — Creative Strategy › 1. Lectura del brief
  - Etapa 1 — Creative Strategy › 2. Territorios creativos
  - Etapa 1 — Creative Strategy › 3. Big ideas y concept cards
  - Etapa 1 — Creative Strategy › 4. Matriz de selección
  - Etapa 1 — Creative Strategy › 5. Dirección narrativa del concepto ganador
- **skills/ai-production-director/references/production-package.md** (referencia)
  - Etapa 7 — Final AI Video Production Package
  - Etapa 7 — Final AI Video Production Package › 1. Estructura del paquete
  - Etapa 7 — Final AI Video Production Package › 2. Reglas de trazabilidad
  - Etapa 7 — Final AI Video Production Package › 3. Checklist de post-producción (07-delivery/post-production.md)
  - Etapa 7 — Final AI Video Production Package › 4. Checklist maestro del pipeline (gate de la Etapa 7)

### ai-video-storyboard

- **skills/ai-video-storyboard/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - AI Video Storyboard Generator
  - AI Video Storyboard Generator › Overview
  - AI Video Storyboard Generator › When to Use
  - AI Video Storyboard Generator › Workflow
  - AI Video Storyboard Generator › Workflow › Step 1 — Brief Intake
  - AI Video Storyboard Generator › Workflow › Step 2 — Infer Structure
  - AI Video Storyboard Generator › Workflow › Step 3 — Establish Visual Consistency Layer
  - AI Video Storyboard Generator › Workflow › Step 4 — Write Each Shot
  - AI Video Storyboard Generator › Workflow › Step 5 — Add Narrative Structure
  - AI Video Storyboard Generator › Workflow › Step 6 — Add Post-Production Checklist
  - AI Video Storyboard Generator › Workflow › Step 7 — Explain Why It Works
  - AI Video Storyboard Generator › Output Format
  - AI Video Storyboard Generator › License
- **skills/ai-video-storyboard/examples/tiktok-reel-30s-coffee.md** (ejemplo)
  - 30s TikTok Reel — Coffee Shop Opening
  - 30s TikTok Reel — Coffee Shop Opening › Visual Theme (applied to every shot)
  - 30s TikTok Reel — Coffee Shop Opening › Shot 1 (0-5s) — Hook: The Pour
  - 30s TikTok Reel — Coffee Shop Opening › Shot 2 (5-10s) — Setting: The Space
  - 30s TikTok Reel — Coffee Shop Opening › Shot 3 (10-15s) — Human: The Barista
  - 30s TikTok Reel — Coffee Shop Opening › Shot 4 (15-20s) — Detail: The Beans
  - 30s TikTok Reel — Coffee Shop Opening › Shot 5 (20-25s) — Atmosphere: The Customer Moment
  - 30s TikTok Reel — Coffee Shop Opening › Shot 6 (25-30s) — CTA: Opening Reveal
  - 30s TikTok Reel — Coffee Shop Opening › Post-Production Checklist
  - 30s TikTok Reel — Coffee Shop Opening › Why This Works

### brand-lock-extractor

- **skills/brand-lock-extractor/LICENSE** (licencia)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - Brand Lock Extractor
  - Brand Lock Extractor › When to use
  - Brand Lock Extractor › Inputs
  - Brand Lock Extractor › Workflow
  - Brand Lock Extractor › Workflow › Step 1. Gather the source material
  - Brand Lock Extractor › Workflow › Step 2. Extract each section
  - Brand Lock Extractor › Workflow › Step 3. Assign confidence and flag estimates
  - Brand Lock Extractor › Workflow › Step 4. Write the brand-lock
  - Brand Lock Extractor › Workflow › Step 5. Self-check, then hand off
  - Brand Lock Extractor › Hard rules
  - Brand Lock Extractor › Hard rules › Rule 1. Never invent a hex value
  - Brand Lock Extractor › Hard rules › Rule 2. Never fabricate a typeface
  - Brand Lock Extractor › Hard rules › Rule 3. Source everything
  - Brand Lock Extractor › Hard rules › Rule 4. The never-list is the highest-value section
  - Brand Lock Extractor › Hard rules › Rule 5. Mood adjectives must be specific
  - Brand Lock Extractor › Hard rules › Rule 6. No emojis, no hype
  - Brand Lock Extractor › Reference
  - Brand Lock Extractor › Example
- **skills/brand-lock-extractor/brand-packs/README.md** (brand-pack)
  - Brand Packs
  - Brand Packs › How to use
  - Brand Packs › How to write a good one
  - Brand Packs › Examples
  - Brand Packs › Generating a brand pack from existing assets
  - Brand Packs › Versioning
  - Brand Packs › Contributing examples
- **skills/brand-lock-extractor/brand-packs/_template.md** (brand-pack)
  - Brand Lock: {{BRAND_NAME}}
  - Brand Lock: {{BRAND_NAME}} › Identity
  - Brand Lock: {{BRAND_NAME}} › Palette
  - Brand Lock: {{BRAND_NAME}} › Typography
  - Brand Lock: {{BRAND_NAME}} › Mood adjectives
  - Brand Lock: {{BRAND_NAME}} › Never list
  - Brand Lock: {{BRAND_NAME}} › Aspect ratios
  - Brand Lock: {{BRAND_NAME}} › Color grade direction
  - Brand Lock: {{BRAND_NAME}} › Motion language
  - Brand Lock: {{BRAND_NAME}} › Voice rules
  - Brand Lock: {{BRAND_NAME}} › Reference materials
- **skills/brand-lock-extractor/brand-packs/examples/saas-clean.md** (brand-pack)
  - Brand Lock: Acme SaaS (Example)
  - Brand Lock: Acme SaaS (Example) › Identity
  - Brand Lock: Acme SaaS (Example) › Palette
  - Brand Lock: Acme SaaS (Example) › Typography
  - Brand Lock: Acme SaaS (Example) › Mood adjectives
  - Brand Lock: Acme SaaS (Example) › Never list
  - Brand Lock: Acme SaaS (Example) › Aspect ratios
  - Brand Lock: Acme SaaS (Example) › Color grade direction
  - Brand Lock: Acme SaaS (Example) › Motion language
  - Brand Lock: Acme SaaS (Example) › Voice rules
  - Brand Lock: Acme SaaS (Example) › Reference materials
- **skills/brand-lock-extractor/examples/brand-lock.md** (ejemplo)
  - Brand Lock: Northwind Coffee Roasters
  - Brand Lock: Northwind Coffee Roasters › Identity
  - Brand Lock: Northwind Coffee Roasters › Palette
  - Brand Lock: Northwind Coffee Roasters › Typography
  - Brand Lock: Northwind Coffee Roasters › Mood adjectives
  - Brand Lock: Northwind Coffee Roasters › Never list
  - Brand Lock: Northwind Coffee Roasters › Aspect ratios
  - Brand Lock: Northwind Coffee Roasters › Color grade direction
  - Brand Lock: Northwind Coffee Roasters › Motion language
  - Brand Lock: Northwind Coffee Roasters › Voice rules
  - Brand Lock: Northwind Coffee Roasters › Extraction notes
- **skills/brand-lock-extractor/examples/input-brief.md** (ejemplo)
  - Example input: what the user handed over
  - Example input: what the user handed over › Source 1: website (fetched)
  - Example input: what the user handed over › Source 2: one-page brand sheet (read)
- **skills/brand-lock-extractor/references/extraction-rubric.md** (referencia)
  - Extraction rubric
  - Extraction rubric › Confidence levels
  - Extraction rubric › Identity
  - Extraction rubric › Palette
  - Extraction rubric › Typography
  - Extraction rubric › Mood adjectives
  - Extraction rubric › Never list
  - Extraction rubric › Aspect ratios
  - Extraction rubric › Color grade direction
  - Extraction rubric › Motion language
  - Extraction rubric › Voice rules
- **skills/brand-lock-extractor/templates/brand-lock.md.tpl** (plantilla)
  - Brand Lock: {{BRAND_NAME}}
  - Brand Lock: {{BRAND_NAME}} › Identity
  - Brand Lock: {{BRAND_NAME}} › Palette
  - Brand Lock: {{BRAND_NAME}} › Typography
  - Brand Lock: {{BRAND_NAME}} › Mood adjectives
  - Brand Lock: {{BRAND_NAME}} › Never list
  - Brand Lock: {{BRAND_NAME}} › Aspect ratios
  - Brand Lock: {{BRAND_NAME}} › Color grade direction
  - Brand Lock: {{BRAND_NAME}} › Motion language
  - Brand Lock: {{BRAND_NAME}} › Voice rules
  - Brand Lock: {{BRAND_NAME}} › Extraction notes
- **skills/brand-lock-extractor/tools/README.md** (herramienta)
  - Tools
  - Tools › Requirements
  - Tools › Run everything
  - Tools › Repo checks
  - Tools › Repo checks › `validate_skills.py`
  - Tools › Repo checks › `validate_schemas.py`
  - Tools › Repo checks › `validate_capabilities.py`
  - Tools › Repo checks › `validate_brand_lock.py`
  - Tools › Project checks
  - Tools › Project checks › `validate_shots.py`
  - Tools › Project checks › `validate_prompts.py`
  - Tools › Project checks › `validate_critique.py`
  - Tools › Project checks › `validate_provenance.py`
  - Tools › Rendering
  - Tools › Rendering › `shots-to-html.py`
  - Tools › Rendering › `copy-prompt.py`
  - Tools › Internal modules
  - Tools › Adding new tools
- **skills/brand-lock-extractor/tools/_shotkit.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/_template.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/check.sh** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/copy-prompt.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/shots-to-html.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/validate_brand_lock.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/validate_capabilities.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/validate_critique.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/validate_prompts.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/validate_provenance.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/validate_schemas.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/validate_shots.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/brand-lock-extractor/tools/validate_skills.py** (herramienta)
  - (texto antes del primer encabezado)

### flujos

- **flujos/flujo-anclas.html** (flujo)
  - (texto antes del primer encabezado)
- **flujos/flujo-spot.html** (flujo)
  - (texto antes del primer encabezado)

### image

- **skills/image/LICENSE** (licencia)
  - (texto antes del primer encabezado)
- **skills/image/NOTICE** (licencia)
  - (texto antes del primer encabezado)
- **skills/image/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - Image Prompting — Nano Banana & GPT Image 2
  - Image Prompting — Nano Banana & GPT Image 2 › Route first — is this actually an image-prompt task?
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [models.md](references/models.md)
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [models.md](references/models.md) › Step 2 — read **one** model file (the one you picked)
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [models.md](references/models.md) › Step 3 — always read after the model file → [golden-rules.md](references/golden-rules.md)
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [models.md](references/models.md) › Step 4 — task-shaped reading (load only what matches the request)
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [models.md](references/models.md) › Step 5 — read for production language → [creative-direction.md](references/creative-direction.md)
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [models.md](references/models.md) › Step 6 — read if structuring a complex prompt → [prompt-framework.md](references/prompt-framework.md)
  - Output format
  - Final response style
- **skills/image/references/characters.md** (referencia)
  - Character Consistency
  - Character Consistency › Identity Locking
  - Character Consistency › Viral Thumbnails
  - Character Consistency › Multi-Character Consistency
  - Character Consistency › Brand Asset Generation
  - Character Consistency › Expression Control
  - Character Consistency › Pose/Action Control
  - Character Consistency › Attire Changes
  - Character Consistency › Environment Swaps
- **skills/image/references/creative-direction.md** (referencia)
  - Creative Direction
  - Creative Direction › Lighting Design
  - Creative Direction › Camera & Hardware
  - Creative Direction › Color Grading & Film Stock
  - Creative Direction › Materiality & Texture
  - Creative Direction › Creative Prompt Examples
- **skills/image/references/dimensional.md** (referencia)
  - Dimensional Translation
  - Dimensional Translation › 2D Floor Plan → 3D
  - Dimensional Translation › Sketch → 3D Concept
  - Dimensional Translation › 3D → 2D Technical
  - Dimensional Translation › Meme Conversion
  - Dimensional Translation › Architectural Visualization
  - Dimensional Translation › Product 2D → 3D
  - Dimensional Translation › Quality Levels
- **skills/image/references/editing.md** (referencia)
  - Image Editing
  - Image Editing › Object Removal
  - Image Editing › Object Addition
  - Image Editing › Lighting Control
  - Image Editing › Seasonal/Weather
  - Image Editing › Colorization
  - Image Editing › Restoration
  - Image Editing › Localization
  - Image Editing › Physics-Aware
  - Image Editing › Conversational Refinement
- **skills/image/references/golden-rules.md** (referencia)
  - Golden Rules
  - Golden Rules › 1. Start with a Verb
  - Golden Rules › 2. Positive Framing
  - Golden Rules › 3. Edit, Don't Re-roll
  - Golden Rules › 4. Natural Language
  - Golden Rules › 5. Be Specific
  - Golden Rules › 6. Provide Context
  - Golden Rules › 7. Quote Text Exactly
  - Golden Rules › Prompt Template
  - Golden Rules › Cost Optimization (Batch Work)
  - Golden Rules › Conversational Refinement
  - Golden Rules › Reference Images
  - Golden Rules › World Knowledge Anchors
  - Golden Rules › World Knowledge Anchors › Три типа якорей
  - Golden Rules › World Knowledge Anchors › Правила использования
  - Golden Rules › World Knowledge Anchors › Примеры
- **skills/image/references/gpt-image.md** (referencia)
  - GPT Image 2 — Specific Rules
  - GPT Image 2 — Specific Rules › Структура промпта — 5 slots
  - GPT Image 2 — Specific Rules › Структура промпта — 5 slots › Минимальный пример
  - GPT Image 2 — Specific Rules › Anti-Slop Rules
  - GPT Image 2 — Specific Rules › Quality Settings — рычаг fidelity / latency
  - GPT Image 2 — Specific Rules › Размеры (gpt-image-2)
  - GPT Image 2 — Specific Rules › Text in Image
  - GPT Image 2 — Specific Rules › Editing — двухколоночная логика
  - GPT Image 2 — Specific Rules › Editing — двухколоночная логика › Edit-паттерны
  - GPT Image 2 — Specific Rules › Multi-Image — до 16 рефов
  - GPT Image 2 — Specific Rules › Style Transfer
  - GPT Image 2 — Specific Rules › World Knowledge
  - GPT Image 2 — Specific Rules › Iteration Strategy
  - GPT Image 2 — Specific Rules › Use-Case Templates
  - GPT Image 2 — Specific Rules › Use-Case Templates › Photoreal Editorial
  - GPT Image 2 — Specific Rules › Use-Case Templates › Product Mockup (Clean Background)
  - GPT Image 2 — Specific Rules › Use-Case Templates › UI Mockup
  - GPT Image 2 — Specific Rules › Use-Case Templates › Marketing Creative with Text
  - GPT Image 2 — Specific Rules › Use-Case Templates › Infographic / Diagram
  - GPT Image 2 — Specific Rules › Migration from Older GPT-Image
- **skills/image/references/models.md** (referencia)
  - Model Selection — Nano Banana vs GPT Image 2
  - Model Selection — Nano Banana vs GPT Image 2 › TL;DR
  - Model Selection — Nano Banana vs GPT Image 2 › Когда что выигрывает
  - Model Selection — Nano Banana vs GPT Image 2 › Когда что выигрывает › Nano Banana выигрывает в
  - Model Selection — Nano Banana vs GPT Image 2 › Когда что выигрывает › GPT Image 2 выигрывает в
  - Model Selection — Nano Banana vs GPT Image 2 › Когда что выигрывает › Где обе модели одинаково хороши
  - Model Selection — Nano Banana vs GPT Image 2 › Различия в синтаксисе промпта
  - Model Selection — Nano Banana vs GPT Image 2 › Стоимость (ориентир)
- **skills/image/references/multi-panel.md** (referencia)
  - Multi-Panel Compositions
  - Multi-Panel Compositions › 1. 9-Cell Grid Storyboard
  - Multi-Panel Compositions › 1. 9-Cell Grid Storyboard › Template (5-slot format)
  - Multi-Panel Compositions › 2. 2x2 Editorial Portrait Grid
  - Multi-Panel Compositions › 2. 2x2 Editorial Portrait Grid › Template (5-slot format)
  - Multi-Panel Compositions › 3. 3-Panel Campaign Collage
  - Multi-Panel Compositions › 3. 3-Panel Campaign Collage › Template (5-slot format)
  - Multi-Panel Compositions › 4. 4x3 Borderless Grid
  - Multi-Panel Compositions › 4. 4x3 Borderless Grid › Template (5-slot format)
  - Multi-Panel Compositions › 5. 6-Frame Cinematic Sequence
  - Multi-Panel Compositions › 5. 6-Frame Cinematic Sequence › Template (5-slot format)
  - Multi-Panel Compositions › 6. Before/After Split
  - Multi-Panel Compositions › 6. Before/After Split › Template (5-slot format)
  - Multi-Panel Compositions › 7. 12-Panel Storyboard Poster
  - Multi-Panel Compositions › 7. 12-Panel Storyboard Poster › Template (5-slot format)
  - Multi-Panel Compositions › General Multi-Panel Tips
- **skills/image/references/nano-banana.md** (referencia)
  - Nano Banana — Specific Rules
  - Nano Banana — Specific Rules › Стиль промпта
  - Nano Banana — Specific Rules › Что НЕ указывать
  - Nano Banana — Specific Rules › Уникальные возможности
  - Nano Banana — Specific Rules › Уникальные возможности › Image Grounding (NB2 only)
  - Nano Banana — Specific Rules › Уникальные возможности › Extreme Aspect Ratios (NB2 only)
  - Nano Banana — Specific Rules › Уникальные возможности › Thinking Mode
  - Nano Banana — Specific Rules › Уникальные возможности › Multi-Reference (лимиты по тирам)
  - Nano Banana — Specific Rules › Уникальные возможности › JSON для сложных сцен (5+ элементов)
  - Nano Banana — Specific Rules › Editing у Nano Banana
  - Nano Banana — Specific Rules › Text Rendering
  - Nano Banana — Specific Rules › Resolution / Cost
  - Nano Banana — Specific Rules › Кейфреймы для видео
  - Nano Banana — Specific Rules › Известные фейлы
  - Nano Banana — Specific Rules › Когда переключаться NB2 → NBP
- **skills/image/references/patterns/character-design.md** (referencia)
  - Character Design Patterns
  - Character Design Patterns › Character Turnaround Sheet (3-View)
  - Character Design Patterns › Expression Sheet
  - Character Design Patterns › Outfit Variant Grid
  - Character Design Patterns › Chibi / Mini-Me Collectible
  - Character Design Patterns › Chibi / Mini-Me Collectible › Nano Banana version:
  - Character Design Patterns › Anime-Style Character Card
  - Character Design Patterns › Anime-Style Character Card › Nano Banana version:
- **skills/image/references/patterns/ecommerce.md** (referencia)
  - E-Commerce Product Photography Patterns
  - E-Commerce Product Photography Patterns › Miniature Diorama Product Ad
  - E-Commerce Product Photography Patterns › Luxury Cosmetics Studio Shot
  - E-Commerce Product Photography Patterns › 9-Panel TVC Storyboard Grid
  - E-Commerce Product Photography Patterns › Floating Ingredient Freeze-Frame
  - E-Commerce Product Photography Patterns › Inflatable Surrealism Product Poster
  - E-Commerce Product Photography Patterns › Inflatable Surrealism Product Poster › Nano Banana version:
- **skills/image/references/patterns/fashion-editorial.md** (referencia)
  - Fashion Editorial Patterns
  - Fashion Editorial Patterns › 3-Panel Campaign Collage
  - Fashion Editorial Patterns › 2x2 Editorial Portrait Grid
  - Fashion Editorial Patterns › Streetwear Poster with Oversized Typography
  - Fashion Editorial Patterns › Retro Roller Skating Sportswear Campaign
  - Fashion Editorial Patterns › Futuristic Sportswear Editorial with 3D Blob Shapes
  - Fashion Editorial Patterns › Futuristic Sportswear Editorial with 3D Blob Shapes › Nano Banana version:
- **skills/image/references/patterns/food-beverage.md** (referencia)
  - Food & Beverage Patterns
  - Food & Beverage Patterns › Luxury Chocolate Brand Campaign
  - Food & Beverage Patterns › High-Fashion Beverage Campaign Board
  - Food & Beverage Patterns › Hyper-Realistic Food Poster Template
  - Food & Beverage Patterns › Naturalist Food Specimen Cross-Section
  - Food & Beverage Patterns › City Food Map Illustration
  - Food & Beverage Patterns › City Food Map Illustration › Nano Banana version:
- **skills/image/references/patterns/portrait-cinema.md** (referencia)
  - Portrait & Cinema Patterns
  - Portrait & Cinema Patterns › Golden Hour Street Backlit Portrait
  - Portrait & Cinema Patterns › Convenience Store Neon Portrait
  - Portrait & Cinema Patterns › Monochrome Glitch Profile Portrait
  - Portrait & Cinema Patterns › Japanese Negative Film Rooftop Portrait
  - Portrait & Cinema Patterns › Dreamy Underwater Surreal Portrait
  - Portrait & Cinema Patterns › Dreamy Underwater Surreal Portrait › Nano Banana version:
- **skills/image/references/patterns/poster-illustration.md** (referencia)
  - Poster & Illustration Patterns
  - Poster & Illustration Patterns › City Across Two Centuries (Time-Split Composition)
  - Poster & Illustration Patterns › City Across Two Centuries (Time-Split Composition) › Nano Banana version:
  - Poster & Illustration Patterns › Fitness Boxing Campaign Collage
  - Poster & Illustration Patterns › Lavender Smartphone Hero Ad
  - Poster & Illustration Patterns › Emerald Street Fashion Poster
  - Poster & Illustration Patterns › Peacock Botanical Vintage Art Print
  - Poster & Illustration Patterns › Peacock Botanical Vintage Art Print › Nano Banana version:
- **skills/image/references/patterns/ui-social.md** (referencia)
  - UI Mockups & Social Media Patterns
  - UI Mockups & Social Media Patterns › Instagram Story Ad (9:16)
  - UI Mockups & Social Media Patterns › Social Media Feed Post (1:1)
  - UI Mockups & Social Media Patterns › App Store Screenshot
  - UI Mockups & Social Media Patterns › Dashboard Design Mockup
  - UI Mockups & Social Media Patterns › Dashboard Design Mockup › Nano Banana version:
  - UI Mockups & Social Media Patterns › Personal Color Analysis Board
  - UI Mockups & Social Media Patterns › Personal Color Analysis Board › Nano Banana version:
- **skills/image/references/prompt-framework.md** (referencia)
  - Prompt Framework
  - Prompt Framework › Task Types (Навыки)
  - Prompt Framework › Universal Elements (Чеклист)
  - Prompt Framework › Detail Modes (Режимы)
  - Prompt Framework › Output Structure
  - Prompt Framework › Quick Decision Tree
  - Prompt Framework › Examples by Type
  - Prompt Framework › Examples by Type › Photorealistic
  - Prompt Framework › Examples by Type › Product/Commercial
  - Prompt Framework › Examples by Type › Minimalist
  - Prompt Framework › Examples by Type › Text Rendering
  - Prompt Framework › Parameterized Templates
  - Prompt Framework › Parameterized Templates › Синтаксис
  - Prompt Framework › Parameterized Templates › Шаблон
  - Prompt Framework › Parameterized Templates › Как использовать
  - Prompt Framework › Parameterized Templates › Примеры использования
  - Prompt Framework › Cinematic Verbose Mode
  - Prompt Framework › Cinematic Verbose Mode › Когда использовать
  - Prompt Framework › Cinematic Verbose Mode › Чеклист микро-деталей
  - Prompt Framework › Cinematic Verbose Mode › Before / After
- **skills/image/references/slides.md** (referencia)
  - Presentation Slides
  - Presentation Slides › Design Principles
  - Presentation Slides › Design Principles › One Slide = One Idea
  - Presentation Slides › Design Principles › Content Limits
  - Presentation Slides › Design Principles › Typography
  - Presentation Slides › Design Principles › Contrast & Color
  - Presentation Slides › Design Principles › Whitespace
  - Presentation Slides › Design Principles › Visual Consistency
  - Presentation Slides › Design Principles › Checklist
  - Presentation Slides › Slide Types
  - Presentation Slides › Slide Types › Hero Title (Dark)
  - Presentation Slides › Slide Types › Data Visualization
  - Presentation Slides › Slide Types › Comparison (Light)
  - Presentation Slides › Slide Types › Insight/Problem
  - Presentation Slides › Slide Types › Process/Timeline
  - Presentation Slides › Typography
  - Presentation Slides › Color Systems
  - Presentation Slides › Atmospheric Effects
  - Presentation Slides › Layout Systems
  - Presentation Slides › Layout Systems › Bento Grid
  - Presentation Slides › Layout Systems › Asymmetric Grid
  - Presentation Slides › Layout Systems › Negative Space
  - Presentation Slides › Layout Systems › Split Screen
  - Presentation Slides › Layout Systems › Brutalist
  - Presentation Slides › Futuristic / SaaS Style
  - Presentation Slides › Futuristic / SaaS Style › Visual Language
  - Presentation Slides › Futuristic / SaaS Style › Glassmorphism Cards
  - Presentation Slides › Futuristic / SaaS Style › 3D Visual Anchors
  - Presentation Slides › Futuristic / SaaS Style › Composition by Type
  - Presentation Slides › Futuristic / SaaS Style › Charts Style
  - Presentation Slides › Futuristic / SaaS Style › Example Prompt
- **skills/image/references/storyboards.md** (referencia)
  - Storyboards & Sequential Art
  - Storyboards & Sequential Art › Story Sequence
  - Storyboards & Sequential Art › Commercial Storyboard
  - Storyboards & Sequential Art › Film Storyboard
  - Storyboards & Sequential Art › Concept Art Series
  - Storyboards & Sequential Art › Sprite Sheets
  - Storyboards & Sequential Art › Consistency Rules
  - Storyboards & Sequential Art › Narrative Pacing
  - Storyboards & Sequential Art › Output Control
- **skills/image/references/structural.md** (referencia)
  - Structural Control
  - Structural Control › Sketch → Final
  - Structural Control › Wireframe → Mockup
  - Structural Control › Grid-Based Assets
  - Structural Control › Pixel Art
  - Structural Control › Layout Guidance
  - Structural Control › Brand Identity Systems
  - Structural Control › Composition Templates
  - Structural Control › Precision Control
- **skills/image/references/text-rendering.md** (referencia)
  - Text Rendering & Infographics
  - Text Rendering & Infographics › Prompt Structure
  - Text Rendering & Infographics › Visual Styles
  - Text Rendering & Infographics › Layout Types
  - Text Rendering & Infographics › Examples
  - Text Rendering & Infographics › Text-First Hack
  - Text Rendering & Infographics › Font Control
  - Text Rendering & Infographics › Multilingual / Localization
  - Text Rendering & Infographics › Tips
- **skills/image/references/vision-decomposer.md** (referencia)
  - Vision Decomposer — Image-to-Prompt Analysis
  - Vision Decomposer — Image-to-Prompt Analysis › STEP 1 — DEEP DECOMPOSITION
  - Vision Decomposer — Image-to-Prompt Analysis › STEP 1 — DEEP DECOMPOSITION › 1. Subject — psychology and mise-en-scène
  - Vision Decomposer — Image-to-Prompt Analysis › STEP 1 — DEEP DECOMPOSITION › 2. Environment — geometry and structure of space
  - Vision Decomposer — Image-to-Prompt Analysis › STEP 1 — DEEP DECOMPOSITION › 3. Lighting — chiaroscuro, color and contrast
  - Vision Decomposer — Image-to-Prompt Analysis › STEP 1 — DEEP DECOMPOSITION › 4. Tech & Cinematography — optics, filters and film texture
  - Vision Decomposer — Image-to-Prompt Analysis › STEP 2 — PROMPT SYNTHESIS
  - Vision Decomposer — Image-to-Prompt Analysis › OUTPUT PROTOCOL
  - Vision Decomposer — Image-to-Prompt Analysis › OUTPUT PROTOCOL › Block 1 — Brief Analysis Log
  - Vision Decomposer — Image-to-Prompt Analysis › OUTPUT PROTOCOL › Block 2 — Final Prompt
  - Vision Decomposer — Image-to-Prompt Analysis › When to load this file

### screenwriter

- **skills/screenwriter/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - Screenwriter Skill
  - Screenwriter Skill › Overview
  - Screenwriter Skill › Core Workflow
  - Screenwriter Skill › Core Workflow › 1. Analyze Input Concept
  - Screenwriter Skill › Core Workflow › 2. Generate Scene Breakdown
  - Screenwriter Skill › Core Workflow › 3. Write Professional Screenplay
  - Screenwriter Skill › Core Workflow › 4. Output XML-Tagged Markdown
  - Screenwriter Skill › Screenplay Format Standards
  - Screenwriter Skill › Screenplay Format Standards › Scene Structure (Master Scene Heading)
  - Screenwriter Skill › Screenplay Format Standards › Action Lines (Visual Description)
  - Screenwriter Skill › Screenplay Format Standards › Character Introduction
  - Screenwriter Skill › Screenplay Format Standards › Dialogue (Use Sparingly)
  - Screenwriter Skill › Screenplay Format Standards › Transitions (Minimal Use)
  - Screenwriter Skill › XML Output Format
  - Screenwriter Skill › XML Output Format › Scene Tag Structure
  - Screenwriter Skill › XML Output Format › Metadata Fields
  - Screenwriter Skill › Short Film Structure (5-10 Minutes)
  - Screenwriter Skill › Short Film Structure (5-10 Minutes) › Scene Count Guidelines
  - Screenwriter Skill › Short Film Structure (5-10 Minutes) › Three-Act Structure (Compressed)
  - Screenwriter Skill › Short Film Structure (5-10 Minutes) › Pacing Tips
  - Screenwriter Skill › Best Practices
  - Screenwriter Skill › Best Practices › For Pipeline Integration
  - Screenwriter Skill › Best Practices › For Quality Output
  - Screenwriter Skill › Best Practices › Common Pitfalls to Avoid
  - Screenwriter Skill › Additional Resources
  - Screenwriter Skill › Additional Resources › Pipeline Integration Guide
  - Screenwriter Skill › Additional Resources › Advanced Techniques
- **skills/screenwriter/references/advanced-techniques.md** (referencia)
  - Advanced Screenwriting Techniques
  - Advanced Screenwriting Techniques › Table of Contents
  - Advanced Screenwriting Techniques › Camera Movement Hints (For Arch-V)
  - Advanced Screenwriting Techniques › Camera Movement Hints (For Arch-V) › Suggesting Camera Movement Through Description
  - Advanced Screenwriting Techniques › Camera Movement Hints (For Arch-V) › Scene Structure for Camera Flow
  - Advanced Screenwriting Techniques › Dialogue Polish Techniques
  - Advanced Screenwriting Techniques › Dialogue Polish Techniques › Subtext Over Direct Statement
  - Advanced Screenwriting Techniques › Dialogue Polish Techniques › Character Voice Consistency
  - Advanced Screenwriting Techniques › Dialogue Polish Techniques › Dialogue Rhythm
  - Advanced Screenwriting Techniques › Pacing Optimization
  - Advanced Screenwriting Techniques › Pacing Optimization › Scene Length Variation
  - Advanced Screenwriting Techniques › Pacing Optimization › Tension Escalation
  - Advanced Screenwriting Techniques › Pacing Optimization › Visual Momentum
  - Advanced Screenwriting Techniques › Advanced Visual Storytelling
  - Advanced Screenwriting Techniques › Advanced Visual Storytelling › Using Objects as Story Beats
  - Advanced Screenwriting Techniques › Advanced Visual Storytelling › Environmental Storytelling
  - Advanced Screenwriting Techniques › Advanced Visual Storytelling › Color Progression
  - Advanced Screenwriting Techniques › Short Film Specific Techniques
  - Advanced Screenwriting Techniques › Short Film Specific Techniques › Economy of Storytelling
  - Advanced Screenwriting Techniques › Short Film Specific Techniques › Opening Hook Strategies
  - Advanced Screenwriting Techniques › Short Film Specific Techniques › Ending Impact
- **skills/screenwriter/references/pipeline-integration.md** (referencia)
  - Pipeline Integration Guide
  - Pipeline Integration Guide › Table of Contents
  - Pipeline Integration Guide › Scene Metadata Standards
  - Pipeline Integration Guide › Scene Metadata Standards › Metadata Completeness
  - Pipeline Integration Guide › Scene Metadata Standards › Metadata Quality Guidelines
  - Pipeline Integration Guide › Imagine-Ready Visual Descriptions
  - Pipeline Integration Guide › Imagine-Ready Visual Descriptions › Visual Element Extraction
  - Pipeline Integration Guide › Imagine-Ready Visual Descriptions › Visual Description Best Practices
  - Pipeline Integration Guide › Imagine-Ready Visual Descriptions › Color and Lighting Vocabulary
  - Pipeline Integration Guide › Character Consistency Tracking
  - Pipeline Integration Guide › Character Consistency Tracking › First Appearance Template
  - Pipeline Integration Guide › Character Consistency Tracking › Subsequent References
  - Pipeline Integration Guide › Character Consistency Tracking › Character Tracking Checklist
  - Pipeline Integration Guide › Scene Numbering Conventions
  - Pipeline Integration Guide › Scene Numbering Conventions › Sequential Numbering
  - Pipeline Integration Guide › Scene Numbering Conventions › Scene Splits and Inserts
  - Pipeline Integration Guide › Duration Estimation Guidelines
  - Pipeline Integration Guide › Duration Estimation Guidelines › Per-Scene Duration
  - Pipeline Integration Guide › Duration Estimation Guidelines › Total Film Duration
  - Pipeline Integration Guide › Output Format Validation
  - Pipeline Integration Guide › Output Format Validation › XML Well-Formedness
  - Pipeline Integration Guide › Output Format Validation › Common XML Errors
  - Pipeline Integration Guide › Pipeline Handoff Checklist

### storyboard-architect

- **skills/storyboard-architect/LICENSE** (licencia)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - Storyboard Architect
  - Storyboard Architect › When to use
  - Storyboard Architect › What you produce
  - Storyboard Architect › Inputs
  - Storyboard Architect › Workflow
  - Storyboard Architect › Workflow › Step 1. Read the brand-lock
  - Storyboard Architect › Workflow › Step 2. Pick the beat framework
  - Storyboard Architect › Workflow › Step 3. Block out timing
  - Storyboard Architect › Workflow › Step 4. Draft the shot list
  - Storyboard Architect › Workflow › Step 5. Separate the text layer
  - Storyboard Architect › Workflow › Step 6. Lock the series
  - Storyboard Architect › Workflow › Step 7. Write rationale
  - Storyboard Architect › Workflow › Step 8. Snapshot the brand-lock
  - Storyboard Architect › Workflow › Step 9. Write run.json
  - Storyboard Architect › Output formats
  - Storyboard Architect › Output formats › `storyboard.md`
  - Storyboard Architect › Output formats › `shots.json`
  - Storyboard Architect › Output formats › `text-overlays.json`
  - Storyboard Architect › Quality bar
  - Storyboard Architect › Reference files
  - Storyboard Architect › Examples
  - Storyboard Architect › Handoff
- **skills/storyboard-architect/brand-packs/README.md** (brand-pack)
  - Brand Packs
  - Brand Packs › How to use
  - Brand Packs › How to write a good one
  - Brand Packs › Examples
  - Brand Packs › Generating a brand pack from existing assets
  - Brand Packs › Versioning
  - Brand Packs › Contributing examples
- **skills/storyboard-architect/brand-packs/_template.md** (brand-pack)
  - Brand Lock: {{BRAND_NAME}}
  - Brand Lock: {{BRAND_NAME}} › Identity
  - Brand Lock: {{BRAND_NAME}} › Palette
  - Brand Lock: {{BRAND_NAME}} › Typography
  - Brand Lock: {{BRAND_NAME}} › Mood adjectives
  - Brand Lock: {{BRAND_NAME}} › Never list
  - Brand Lock: {{BRAND_NAME}} › Aspect ratios
  - Brand Lock: {{BRAND_NAME}} › Color grade direction
  - Brand Lock: {{BRAND_NAME}} › Motion language
  - Brand Lock: {{BRAND_NAME}} › Voice rules
  - Brand Lock: {{BRAND_NAME}} › Reference materials
- **skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md** (ejemplo)
  - (texto antes del primer encabezado)
  - Brand Lock: WhyStrohm
  - Brand Lock: WhyStrohm › Identity
  - Brand Lock: WhyStrohm › Palette
  - Brand Lock: WhyStrohm › Typography
  - Brand Lock: WhyStrohm › Mood adjectives
  - Brand Lock: WhyStrohm › Never list
  - Brand Lock: WhyStrohm › Aspect ratios
  - Brand Lock: WhyStrohm › Color grade direction
  - Brand Lock: WhyStrohm › Motion language
  - Brand Lock: WhyStrohm › Voice rules
- **skills/storyboard-architect/examples/30s-pain-proof-promise/preview.html** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/30s-pain-proof-promise/run.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/30s-pain-proof-promise/shots.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md** (ejemplo)
  - WhyStrohm. The Content Infrastructure Pitch
  - WhyStrohm. The Content Infrastructure Pitch › Brief
  - WhyStrohm. The Content Infrastructure Pitch › Beat framework: Pain-Reframe-Promise
  - WhyStrohm. The Content Infrastructure Pitch › Series lock
  - WhyStrohm. The Content Infrastructure Pitch › Shots
  - WhyStrohm. The Content Infrastructure Pitch › Shots › shot_01 · 0.0–2.0s · MCU · static
  - WhyStrohm. The Content Infrastructure Pitch › Shots › shot_02 · 2.0–7.0s · MS · static
  - WhyStrohm. The Content Infrastructure Pitch › Shots › shot_03 · 7.0–11.0s · ECU · static
  - WhyStrohm. The Content Infrastructure Pitch › Shots › shot_04 · 11.0–16.0s · MCU · push
  - WhyStrohm. The Content Infrastructure Pitch › Shots › shot_05 · 16.0–20.0s · MS · static
  - WhyStrohm. The Content Infrastructure Pitch › Shots › shot_06 · 20.0–26.0s · MCU · static
  - WhyStrohm. The Content Infrastructure Pitch › Shots › shot_07 · 26.0–30.0s · MS · static
  - WhyStrohm. The Content Infrastructure Pitch › Handoff notes
  - WhyStrohm. The Content Infrastructure Pitch › Audit trail
- **skills/storyboard-architect/examples/30s-pain-proof-promise/text-overlays.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/60s-founder-explainer/brand-lock.snapshot.md** (ejemplo)
  - (texto antes del primer encabezado)
  - Brand Lock: WhyStrohm
  - Brand Lock: WhyStrohm › Identity
  - Brand Lock: WhyStrohm › Palette
  - Brand Lock: WhyStrohm › Typography
  - Brand Lock: WhyStrohm › Mood adjectives
  - Brand Lock: WhyStrohm › Never list
  - Brand Lock: WhyStrohm › Aspect ratios
  - Brand Lock: WhyStrohm › Color grade direction
  - Brand Lock: WhyStrohm › Motion language
  - Brand Lock: WhyStrohm › Voice rules
- **skills/storyboard-architect/examples/60s-founder-explainer/preview.html** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/60s-founder-explainer/run.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/60s-founder-explainer/shots.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md** (ejemplo)
  - WhyStrohm. How The System Actually Works
  - WhyStrohm. How The System Actually Works › Brief
  - WhyStrohm. How The System Actually Works › Beat framework: Founder Explainer
  - WhyStrohm. How The System Actually Works › Series lock
  - WhyStrohm. How The System Actually Works › Shots
  - WhyStrohm. How The System Actually Works › Shots › shot_01 · 0.0–2.0s · MCU · static
  - WhyStrohm. How The System Actually Works › Shots › shot_02 · 2.0–8.0s · MS · static
  - WhyStrohm. How The System Actually Works › Shots › shot_03 · 8.0–14.0s · ECU · static
  - WhyStrohm. How The System Actually Works › Shots › shot_04 · 14.0–24.0s · MCU · push
  - WhyStrohm. How The System Actually Works › Shots › shot_05 · 24.0–32.0s · MS · static
  - WhyStrohm. How The System Actually Works › Shots › shot_06 · 32.0–42.0s · MCU · static
  - WhyStrohm. How The System Actually Works › Shots › shot_07 · 42.0–50.0s · MS · pull
  - WhyStrohm. How The System Actually Works › Shots › shot_08 · 50.0–60.0s · MCU · static
  - WhyStrohm. How The System Actually Works › Handoff notes
  - WhyStrohm. How The System Actually Works › Audit trail
- **skills/storyboard-architect/examples/60s-founder-explainer/text-overlays.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md** (ejemplo)
  - (texto antes del primer encabezado)
  - Brand Lock: WhyStrohm
  - Brand Lock: WhyStrohm › Identity
  - Brand Lock: WhyStrohm › Palette
  - Brand Lock: WhyStrohm › Typography
  - Brand Lock: WhyStrohm › Mood adjectives
  - Brand Lock: WhyStrohm › Never list
  - Brand Lock: WhyStrohm › Aspect ratios
  - Brand Lock: WhyStrohm › Color grade direction
  - Brand Lock: WhyStrohm › Motion language
  - Brand Lock: WhyStrohm › Voice rules
  - Brand Lock: WhyStrohm › Reference materials
- **skills/storyboard-architect/examples/shotkit-explainer/preview.html** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/shotkit-explainer/run.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/shotkit-explainer/shots.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/examples/shotkit-explainer/storyboard.md** (ejemplo)
  - shotkit. The Explainer.
  - shotkit. The Explainer. › Brief
  - shotkit. The Explainer. › Series lock
  - shotkit. The Explainer. › Shots
  - shotkit. The Explainer. › Shots › shot_01: 0.0 to 12.0s. WS. eye-level. static.
  - shotkit. The Explainer. › Shots › shot_02: 12.0 to 30.0s. MS. eye-level. static.
  - shotkit. The Explainer. › Shots › shot_03: 30.0 to 50.0s. MS. eye-level. push.
  - shotkit. The Explainer. › Shots › shot_04: 50.0 to 65.0s. MCU. eye-level. push.
  - shotkit. The Explainer. › Shots › shot_05: 65.0 to 80.0s. MS. eye-level. static.
  - shotkit. The Explainer. › Shots › shot_06: 80.0 to 90.0s. WS. eye-level. static.
  - shotkit. The Explainer. › Audit trail
- **skills/storyboard-architect/examples/shotkit-explainer/text-overlays.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/references/beat-frameworks.md** (referencia)
  - Beat Frameworks
  - Beat Frameworks › Pain-Reframe-Promise (PRP)
  - Beat Frameworks › Hero Trilogy
  - Beat Frameworks › Founder Explainer
  - Beat Frameworks › Content Spiral
  - Beat Frameworks › Educational Demo
  - Beat Frameworks › Custom
- **skills/storyboard-architect/references/on-screen-text.md** (referencia)
  - On-Screen Text
  - On-Screen Text › When on-screen text earns its keep
  - On-Screen Text › When on-screen text doesn't earn its keep
  - On-Screen Text › Composition rules
  - On-Screen Text › Composition rules › Negative-space-aware composition
  - On-Screen Text › Composition rules › Positions
  - On-Screen Text › Composition rules › Sizes
  - On-Screen Text › Composition rules › Animation
  - On-Screen Text › Color rules
  - On-Screen Text › Typography rules
  - On-Screen Text › The "read twice" rule
  - On-Screen Text › Stacking text across shots
- **skills/storyboard-architect/references/shot-grammar.md** (referencia)
  - Shot Grammar
  - Shot Grammar › Framing (subject size in frame)
  - Shot Grammar › Angle (camera vertical position)
  - Shot Grammar › Motion (camera movement)
  - Shot Grammar › Depth of field
  - Shot Grammar › Lighting style (referenced from series_lock)
  - Shot Grammar › Subject description
  - Shot Grammar › What goes in `subject` vs `series_lock` vs `brand_lock`
- **skills/storyboard-architect/references/timing-rules.md** (referencia)
  - Timing Rules
  - Timing Rules › Shot duration baselines
  - Timing Rules › Hook timing (the first beat)
  - Timing Rules › CTA timing (the final beat)
  - Timing Rules › On-screen text duration math
  - Timing Rules › Pacing curve
  - Timing Rules › Validating timing
- **skills/storyboard-architect/templates/run.schema.json** (plantilla)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/templates/shots.schema.json** (plantilla)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/templates/storyboard.md.tpl** (plantilla)
  - {{PROJECT_TITLE}}
  - {{PROJECT_TITLE}} › Brief
  - {{PROJECT_TITLE}} › Series lock
  - {{PROJECT_TITLE}} › Shots
  - {{PROJECT_TITLE}} › Shots › {{id}} · {{start}}–{{end}}s · {{framing}} · {{motion}}
  - {{PROJECT_TITLE}} › Text overlays
  - {{PROJECT_TITLE}} › Text overlays › {{id}}: `{{shot_id}}`
  - {{PROJECT_TITLE}} › Handoff notes
  - {{PROJECT_TITLE}} › Audit trail
- **skills/storyboard-architect/templates/text-overlays.schema.json** (plantilla)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/README.md** (herramienta)
  - Tools
  - Tools › Requirements
  - Tools › Run everything
  - Tools › Repo checks
  - Tools › Repo checks › `validate_skills.py`
  - Tools › Repo checks › `validate_schemas.py`
  - Tools › Repo checks › `validate_capabilities.py`
  - Tools › Repo checks › `validate_brand_lock.py`
  - Tools › Project checks
  - Tools › Project checks › `validate_shots.py`
  - Tools › Project checks › `validate_prompts.py`
  - Tools › Project checks › `validate_critique.py`
  - Tools › Project checks › `validate_provenance.py`
  - Tools › Rendering
  - Tools › Rendering › `shots-to-html.py`
  - Tools › Rendering › `copy-prompt.py`
  - Tools › Internal modules
  - Tools › Adding new tools
- **skills/storyboard-architect/tools/_shotkit.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/_template.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/check.sh** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/copy-prompt.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/shots-to-html.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/validate_brand_lock.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/validate_capabilities.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/validate_critique.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/validate_prompts.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/validate_provenance.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/validate_schemas.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/validate_shots.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-architect/tools/validate_skills.py** (herramienta)
  - (texto antes del primer encabezado)

### storyboard-html-preview

- **skills/storyboard-html-preview/LICENSE** (licencia)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - Storyboard HTML Preview
  - Storyboard HTML Preview › When to use
  - Storyboard HTML Preview › What you produce
  - Storyboard HTML Preview › Workflow
  - Storyboard HTML Preview › Workflow › Step 1. Read inputs
  - Storyboard HTML Preview › Workflow › Step 2. Extract brand parameters
  - Storyboard HTML Preview › Workflow › Step 3. Generate the HTML
  - Storyboard HTML Preview › Workflow › Step 4. Embed frames if available
  - Storyboard HTML Preview › Workflow › Step 5. Render text overlays visually
  - Storyboard HTML Preview › Workflow › Step 6. Print stylesheet
  - Storyboard HTML Preview › Hard rules
  - Storyboard HTML Preview › Hard rules › Rule 1. Single file, no exceptions
  - Storyboard HTML Preview › Hard rules › Rule 2. No external dependencies at runtime
  - Storyboard HTML Preview › Hard rules › Rule 3. Print must work
  - Storyboard HTML Preview › Hard rules › Rule 4. Brand-aware but quiet
  - Storyboard HTML Preview › Hard rules › Rule 5. Mobile-readable
  - Storyboard HTML Preview › Templates
  - Storyboard HTML Preview › Quality bar
  - Storyboard HTML Preview › Two timestamps, not one
  - Storyboard HTML Preview › Examples
- **skills/storyboard-html-preview/templates/preview.html.tpl** (plantilla)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/templates/print.css.tpl** (plantilla)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/templates/styles.css.tpl** (plantilla)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/README.md** (herramienta)
  - Tools
  - Tools › Requirements
  - Tools › Run everything
  - Tools › Repo checks
  - Tools › Repo checks › `validate_skills.py`
  - Tools › Repo checks › `validate_schemas.py`
  - Tools › Repo checks › `validate_capabilities.py`
  - Tools › Repo checks › `validate_brand_lock.py`
  - Tools › Project checks
  - Tools › Project checks › `validate_shots.py`
  - Tools › Project checks › `validate_prompts.py`
  - Tools › Project checks › `validate_critique.py`
  - Tools › Project checks › `validate_provenance.py`
  - Tools › Rendering
  - Tools › Rendering › `shots-to-html.py`
  - Tools › Rendering › `copy-prompt.py`
  - Tools › Internal modules
  - Tools › Adding new tools
- **skills/storyboard-html-preview/tools/_shotkit.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/_template.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/check.sh** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/copy-prompt.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/shots-to-html.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/validate_brand_lock.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/validate_capabilities.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/validate_critique.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/validate_prompts.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/validate_provenance.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/validate_schemas.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/validate_shots.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/storyboard-html-preview/tools/validate_skills.py** (herramienta)
  - (texto antes del primer encabezado)

### video

- **skills/video/LICENSE** (licencia)
  - (texto antes del primer encabezado)
- **skills/video/NOTICE** (licencia)
  - (texto antes del primer encabezado)
- **skills/video/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - AI Director, Screenwriter & Editor
  - AI Director, Screenwriter & Editor › Route first — is this actually a video-prompt task?
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [dramaturgy.md](references/dramaturgy.md)
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [dramaturgy.md](references/dramaturgy.md) › Step 2 — always read second → [universal-rules.md](references/universal-rules.md)
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [dramaturgy.md](references/dramaturgy.md) › Step 3 — pick the model and read **one** model file
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [dramaturgy.md](references/dramaturgy.md) › Step 4 — task-shaped reading (load only those that match)
  - Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS › Step 1 — always read first → [dramaturgy.md](references/dramaturgy.md) › Step 5 — apply the dramaturgy check and the three-detail check
  - Output
  - Final response style
- **skills/video/references/animatic-keyframes.md** (referencia)
  - Keyframes for an animatic (opornye kadry)
  - Keyframes for an animatic (opornye kadry) › Contents
  - Keyframes for an animatic (opornye kadry) › 1. What an animatic keyframe must do
  - Keyframes for an animatic (opornye kadry) › 2. The keyframe card
  - Keyframes for an animatic (opornye kadry) › 3. How many keyframes per beat — the density ladder
  - Keyframes for an animatic (opornye kadry) › 4. Composing a still that reads as MOTION
  - Keyframes for an animatic (opornye kadry) › 5. Emotion without faces in a still
  - Keyframes for an animatic (opornye kadry) › 6. The loaded frame for one panel
  - Keyframes for an animatic (opornye kadry) › 7. From keyframe to image-gen prompt
  - Keyframes for an animatic (opornye kadry) › 8. Worked keyframe board for a 30s race spot
  - Keyframes for an animatic (opornye kadry) › 9. Checklist: does this keyframe earn its place
- **skills/video/references/camera-lighting-vocabulary.md** (referencia)
  - Camera, lighting, color, sound vocabulary
  - Camera, lighting, color, sound vocabulary › Contents
  - Camera, lighting, color, sound vocabulary › 1. Framing
  - Camera, lighting, color, sound vocabulary › 2. Camera movement
  - Camera, lighting, color, sound vocabulary › 3. Lens language
  - Camera, lighting, color, sound vocabulary › 4. Light sources
  - Camera, lighting, color, sound vocabulary › 5. Light direction
  - Camera, lighting, color, sound vocabulary › 6. Light quality
  - Camera, lighting, color, sound vocabulary › 7. Color discipline
  - Camera, lighting, color, sound vocabulary › 8. Sound categories
  - Camera, lighting, color, sound vocabulary › 9. Blocking language
  - Camera, lighting, color, sound vocabulary › 10. Translating uncommon terms
  - Camera, lighting, color, sound vocabulary › 11. Transition vocabulary
- **skills/video/references/dramaturgy.md** (referencia)
  - Dramaturgy, detail, montage
  - Dramaturgy, detail, montage › Contents
  - Dramaturgy, detail, montage › 1. Core law. Scene formula
  - Dramaturgy, detail, montage › 2. Second law. Details intensify emotion. Laziness kills the prompt.
  - Dramaturgy, detail, montage › 2. Second law. Details intensify emotion. Laziness kills the prompt. › The three-detail rule
  - Dramaturgy, detail, montage › 2. Second law. Details intensify emotion. Laziness kills the prompt. › What is banned
  - Dramaturgy, detail, montage › 2. Second law. Details intensify emotion. Laziness kills the prompt. › How details map to dramaturgy
  - Dramaturgy, detail, montage › 3. The three-jobs rule
  - Dramaturgy, detail, montage › 4. Walter Murch Rule of Six
  - Dramaturgy, detail, montage › 5. Blocking as choreography of desire
  - Dramaturgy, detail, montage › 6. Staging controls subtext
  - Dramaturgy, detail, montage › 7. Camera must have a reason
  - Dramaturgy, detail, montage › 8. Spatial clarity beats montage hysteria
  - Dramaturgy, detail, montage › 9. Environment plays
  - Dramaturgy, detail, montage › 10. Three-layer storyboard method
  - Dramaturgy, detail, montage › 10. Three-layer storyboard method › Layer 1. Dramatic beats
  - Dramaturgy, detail, montage › 10. Three-layer storyboard method › Layer 2. Shot functions
  - Dramaturgy, detail, montage › 10. Three-layer storyboard method › Layer 3. Editing rhythm
  - Dramaturgy, detail, montage › 11. Shot card template
  - Dramaturgy, detail, montage › 12. Rhythm ladder
  - Dramaturgy, detail, montage › 12. Rhythm ladder › Slow-burn drama
  - Dramaturgy, detail, montage › 12. Rhythm ladder › Commercial product arc
  - Dramaturgy, detail, montage › 12. Rhythm ladder › Anxiety build
  - Dramaturgy, detail, montage › 12. Rhythm ladder › Impact scene
  - Dramaturgy, detail, montage › 13. One-anchor principle
  - Dramaturgy, detail, montage › 14. Worked example. Guilt, 30 seconds
  - Dramaturgy, detail, montage › 14. Worked example. Guilt, 30 seconds › Five anchors
  - Dramaturgy, detail, montage › 14. Worked example. Guilt, 30 seconds › Layer 1. Dramatic beats
  - Dramaturgy, detail, montage › 14. Worked example. Guilt, 30 seconds › Layer 2. Shot functions (selected)
  - Dramaturgy, detail, montage › 14. Worked example. Guilt, 30 seconds › Layer 3. Rhythm (final 10 seconds)
  - Dramaturgy, detail, montage › 15. Dramaturgy check before sending any prompt
- **skills/video/references/fixes-and-skeletons.md** (referencia)
  - Fixes, checklist, and cross-model skeletons
  - Fixes, checklist, and cross-model skeletons › Contents
  - Fixes, checklist, and cross-model skeletons › 1. Continuity checklist
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › One continuous take instead of montage
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Character face changes between shots
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Object disappears mid-scene
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Weak drama. Scene feels flat.
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Messy random cuts in fast montage
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Dialogue too fast (Veo)
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Melting hands / extra fingers
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Lighting drifts between clips
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Model ignores camera instruction
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Weird AI-looking faces
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Twins / face-blending in multi-person scenes
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Objects or characters appear too early in an extension
  - Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Random subtitles or unwanted background music
  - Fixes, checklist, and cross-model skeletons › 3. Cross-model prompt skeletons
  - Fixes, checklist, and cross-model skeletons › 3. Cross-model prompt skeletons › Seedance
  - Fixes, checklist, and cross-model skeletons › 3. Cross-model prompt skeletons › Kling text-to-video
  - Fixes, checklist, and cross-model skeletons › 3. Cross-model prompt skeletons › Kling image-to-video
  - Fixes, checklist, and cross-model skeletons › 3. Cross-model prompt skeletons › Veo prose
  - Fixes, checklist, and cross-model skeletons › 3. Cross-model prompt skeletons › Veo JSON
  - Fixes, checklist, and cross-model skeletons › 4. Default negative constraints
  - Fixes, checklist, and cross-model skeletons › 5. Prompt compression order
  - Fixes, checklist, and cross-model skeletons › 6. Output format templates
  - Fixes, checklist, and cross-model skeletons › 6. Output format templates › Format A. Single prompt
  - Fixes, checklist, and cross-model skeletons › 6. Output format templates › Format B. Multi-clip prompts
  - Fixes, checklist, and cross-model skeletons › 6. Output format templates › Format C. Storyboard (раскадровка)
  - Fixes, checklist, and cross-model skeletons › 6. Output format templates › Format D. Prompt audit
  - Fixes, checklist, and cross-model skeletons › 6. Output format templates › Format E. Director treatment
  - Fixes, checklist, and cross-model skeletons › 6. Output format templates › Format F. Veo JSON
- **skills/video/references/kling.md** (referencia)
  - Kling reference (Kuaishou)
  - Kling reference (Kuaishou) › Contents
  - Kling reference (Kuaishou) › 1. What Kling is
  - Kling reference (Kuaishou) › 2. Versions and element limits
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s › What changed vs 2.x
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s › Five-layer prompt structure
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s › Anchor subjects early
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s › Multi-shot syntax (think in shots, not clips)
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s › Dialogue protocol (P1-P4)
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s › Image-to-video on 3.0 — lock first, then move
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s › Cinematic vocabulary that 3.0 actually understands
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s › Default model choice
  - Kling reference (Kuaishou) › 3. Kling 3.0 — multi-shot, native audio, 15s › API parameters (3.0, fal/official)
  - Kling reference (Kuaishou) › 4. Prompt formula (1.x – 2.x)
  - Kling reference (Kuaishou) › 5. Prompt length by model
  - Kling reference (Kuaishou) › 6. Negative prompts (critical rule)
  - Kling reference (Kuaishou) › 7. Element Library and Element Binding (1.x – 2.x)
  - Kling reference (Kuaishou) › 7. Element Library and Element Binding (1.x – 2.x) › Elements 3.0 (Omni)
  - Kling reference (Kuaishou) › 8. Motion Brush (unique)
  - Kling reference (Kuaishou) › 9. Motion Control (2.6 Pro, unique)
  - Kling reference (Kuaishou) › 10. Image-to-video rule
  - Kling reference (Kuaishou) › 11. Failure modes and fixes
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Random camera drift in static scenes
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Prompt exceeds model capacity, output melts
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Character face changes between generations
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Negative prompts ignored
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Motion Brush artifact
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Element overload melts hands
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Kling 3.0 collapses multi-shot into one continuous take
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Kling 3.0 dialogue lip-sync drifts
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Kling 3.0 picks the wrong voice
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Image quality drops when Elements / references are enabled
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Two similar characters blend features in one frame
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Morphing artifacts on fast motion
  - Kling reference (Kuaishou) › 11. Failure modes and fixes › Music appears even though the prompt says "no music"
  - Kling reference (Kuaishou) › 12. Skeleton
  - Kling reference (Kuaishou) › 12. Skeleton › Text-to-video (1.x – 2.x)
  - Kling reference (Kuaishou) › 12. Skeleton › Image-to-video
  - Kling reference (Kuaishou) › 12. Skeleton › Worked example. Fashion, image-to-video (2.6 Pro)
  - Kling reference (Kuaishou) › 12. Skeleton › Multi-shot with dialogue (Kling 3.0)
- **skills/video/references/patterns-and-genres.md** (referencia)
  - Montage patterns and genre modules
  - Montage patterns and genre modules › Contents
  - Montage patterns and genre modules › 1. Montage patterns
  - Montage patterns and genre modules › 1. Montage patterns › Pattern 1. Escalation
  - Montage patterns and genre modules › 1. Montage patterns › Pattern 2. Anxiety
  - Montage patterns and genre modules › 1. Montage patterns › Pattern 3. Discovery
  - Montage patterns and genre modules › 1. Montage patterns › Pattern 4. Catastrophe
  - Montage patterns and genre modules › 1. Montage patterns › Pattern 5. Commercial product drama
  - Montage patterns and genre modules › 1. Montage patterns › Pattern 6. Music video loop
  - Montage patterns and genre modules › 2. Genre modules
  - Montage patterns and genre modules › 2. Genre modules › Domestic tragedy
  - Montage patterns and genre modules › 2. Genre modules › Music video
  - Montage patterns and genre modules › 2. Genre modules › Commercial
  - Montage patterns and genre modules › 2. Genre modules › Psychological drama
  - Montage patterns and genre modules › 2. Genre modules › Action
  - Montage patterns and genre modules › 2. Genre modules › Race / speed
  - Montage patterns and genre modules › 2. Genre modules › Fashion
  - Montage patterns and genre modules › 2. Genre modules › UGC / Social
  - Montage patterns and genre modules › 3. Multi-clip story structure
  - Montage patterns and genre modules › 3. Multi-clip story structure › Default splits
  - Montage patterns and genre modules › 3. Multi-clip story structure › What every clip must repeat
  - Montage patterns and genre modules › 3. Multi-clip story structure › Timecoded internal beats
  - Montage patterns and genre modules › 3. Multi-clip story structure › Continuity across clips
- **skills/video/references/race-and-speed.md** (referencia)
  - Race, speed and faceless kinetic montage
  - Race, speed and faceless kinetic montage › Contents
  - Race, speed and faceless kinetic montage › 1. Core laws (the non-negotiables)
  - Race, speed and faceless kinetic montage › 2. Four schools worth stealing
  - Race, speed and faceless kinetic montage › 3. Selling speed in a single frame
  - Race, speed and faceless kinetic montage › 4. Storytelling without faces — the race captioning system
  - Race, speed and faceless kinetic montage › 5. The race ritual (liturgy) + the 5 shot families
  - Race, speed and faceless kinetic montage › 5. The race ritual (liturgy) + the 5 shot families › The 5 shot families
  - Race, speed and faceless kinetic montage › 6. Camera grammar for speed
  - Race, speed and faceless kinetic montage › 7. Light & color for speed without faces
  - Race, speed and faceless kinetic montage › 7. Light & color for speed without faces › The cold combative palette
  - Race, speed and faceless kinetic montage › 7. Light & color for speed without faces › Concrete lighting recipes (drop-in for the format-C Light column: source · direction · quality · what it rims)
  - Race, speed and faceless kinetic montage › 8. Sound & rhythm
  - Race, speed and faceless kinetic montage › 9. 30-second structure (beat map)
  - Race, speed and faceless kinetic montage › 10. Anti-fake guard
- **skills/video/references/role-modes.md** (referencia)
  - Role modes
  - Role modes › Contents
  - Role modes › 1. Director mode
  - Role modes › 1. Director mode › Trigger
  - Role modes › 1. Director mode › Mindset
  - Role modes › 1. Director mode › Output format. Director treatment
  - Role modes › 1. Director mode › Style references
  - Role modes › 2. Screenwriter mode
  - Role modes › 2. Screenwriter mode › Trigger
  - Role modes › 2. Screenwriter mode › Mindset
  - Role modes › 2. Screenwriter mode › Output format. Beat breakdown
  - Role modes › 2. Screenwriter mode › Dialogue format (for Veo specifically)
  - Role modes › 2. Screenwriter mode › Internal monologue rule
  - Role modes › 3. Editor mode
  - Role modes › 3. Editor mode › Trigger
  - Role modes › 3. Editor mode › Mindset
  - Role modes › 3. Editor mode › Rules
  - Role modes › 3. Editor mode › Output format. Timecoded beat sheet
  - Role modes › 3. Editor mode › Density
  - Role modes › 4. Shot function taxonomy
- **skills/video/references/seedance-25.md** (referencia)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › Contents
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 1. What 2.5 changes
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 2. Specs and hard limits
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 3. Official prompt formula
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 4. Syntax markers for audio, dialogue and text
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 5. Reference discipline (the 50-slot system)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 6. The 30-second structure: stages and end states
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 7. The anti-collapse skeleton (3 modules)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 8. Realistic human formula (anti-AI-face)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 9. Camera language
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 10. Transitions
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 11. Physics through consequences and triggers
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 12. Video editing (partial re-render)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 13. Video extension
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 14. Ultra Long mode (30-180s)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 15. Blockout and green screen
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 16. Storyboard grids and keyframes
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 17. Failure modes and fixes
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 17. Failure modes and fixes › Twins / face-blending in multi-person scenes
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 17. Failure modes and fixes › Same character in two states appears at the wrong time
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 17. Failure modes and fixes › Random subtitles or unwanted BGM
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 17. Failure modes and fixes › Plastic AI skin
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 17. Failure modes and fixes › Long-context plausibility slips
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 17. Failure modes and fixes › The one-take that refuses to stay one take
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 17. Failure modes and fixes › Edit mode stalls or ignores the instruction
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 18. Economics and model choice
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 19. Worked examples (official, verbatim)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 19. Worked examples (official, verbatim) › A. Restrained micro-acting — "Riverside Farewell" (29s one-shot)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 19. Worked examples (official, verbatim) › B. Physics and prohibitions — sci-fi mecha chase (30s one-shot)
  - Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31) › 19. Worked examples (official, verbatim) › C. Reference orchestration — museum heist one-take (17 refs, translated from the Jimeng manual cases)
- **skills/video/references/seedance.md** (referencia)
  - Seedance reference (ByteDance)
  - Seedance reference (ByteDance) › Contents
  - Seedance reference (ByteDance) › 1. What Seedance is
  - Seedance reference (ByteDance) › 2. Versions and specs
  - Seedance reference (ByteDance) › 3. CLI parameters (1.x / 2.0 only)
  - Seedance reference (ByteDance) › 4. The Details Law (read this first)
  - Seedance reference (ByteDance) › 5. Six-step prompt formula (quick scenes)
  - Seedance reference (ByteDance) › 6. Production-grade skeleton (11 blocks)
  - Seedance reference (ByteDance) › 7. The 5-second shot timeline (rhythm template)
  - Seedance reference (ByteDance) › 8. Multi-shot syntax (unique)
  - Seedance reference (ByteDance) › 9. Anti-mush guard block
  - Seedance reference (ByteDance) › 10. `@img1` character reference syntax
  - Seedance reference (ByteDance) › 11. Camera movements (9 presets)
  - Seedance reference (ByteDance) › 12. Negative prompts
  - Seedance reference (ByteDance) › 13. Image-to-video rule
  - Seedance reference (ByteDance) › 14. Audio (1.5+)
  - Seedance reference (ByteDance) › 15. Failure modes and fixes
  - Seedance reference (ByteDance) › 15. Failure modes and fixes › One continuous take when multi-shot was requested
  - Seedance reference (ByteDance) › 15. Failure modes and fixes › Character drift across shots
  - Seedance reference (ByteDance) › 15. Failure modes and fixes › Motion ignored below 5 seconds
  - Seedance reference (ByteDance) › 15. Failure modes and fixes › Negative phrasing ignored
  - Seedance reference (ByteDance) › 15. Failure modes and fixes › Multi-shot fails on 4+ shots in 5s
  - Seedance reference (ByteDance) › 15. Failure modes and fixes › Mood smear / "everything looks the same"
  - Seedance reference (ByteDance) › 15. Failure modes and fixes › Lazy abstract phrasing produces lifeless clips
  - Seedance reference (ByteDance) › 15. Failure modes and fixes › Human faces rejected or degraded (2.0)
  - Seedance reference (ByteDance) › 16. Worked example. 15-second tragicomedy as 3 × 5s clips
  - Seedance reference (ByteDance) › 16. Worked example. 15-second tragicomedy as 3 × 5s clips › Story spine
  - Seedance reference (ByteDance) › 16. Worked example. 15-second tragicomedy as 3 × 5s clips › Clip A. Hunger (production-grade skeleton applied)
  - Seedance reference (ByteDance) › 16. Worked example. 15-second tragicomedy as 3 × 5s clips › Older single-clip skeleton (kept for quick scenes)
  - Seedance reference (ByteDance) › 17. Seedance 2.5 → read `seedance-25.md`
- **skills/video/references/universal-rules.md** (referencia)
  - Universal rules — apply to every video model
  - Universal rules — apply to every video model › Contents
  - Universal rules — apply to every video model › 1. The non-negotiable. Details intensify emotion. Laziness kills the prompt.
  - Universal rules — apply to every video model › 2. U1. Universal prompt skeleton
  - Universal rules — apply to every video model › 3. U2. Weight-at-start
  - Universal rules — apply to every video model › 4. U3. Show don't tell
  - Universal rules — apply to every video model › 5. U4. Natural language beats tag spam
  - Universal rules — apply to every video model › 6. U5. One primary camera move per shot
  - Universal rules — apply to every video model › 7. U6. Precise lens language
  - Universal rules — apply to every video model › 8. U7. Character consistency anchor
  - Universal rules — apply to every video model › 9. U8. No contradictions
  - Universal rules — apply to every video model › 10. U9. Concrete physical detail over abstract concept
  - Universal rules — apply to every video model › 11. U10. Duration discipline
  - Universal rules — apply to every video model › 12. U11. The final image rule
  - Universal rules — apply to every video model › 13. U12. The three-detail check (audit before sending)
  - Universal rules — apply to every video model › 14. U13. Reference role discipline
  - Universal rules — apply to every video model › 15. U14. Priority declaration
- **skills/video/references/veo.md** (referencia)
  - Veo reference (Google)
  - Veo reference (Google) › Contents
  - Veo reference (Google) › 1. What Veo is
  - Veo reference (Google) › 2. Versions and specs
  - Veo reference (Google) › 3. Prompt structure and length
  - Veo reference (Google) › 4. Dialogue syntax (critical)
  - Veo reference (Google) › 4. Dialogue syntax (critical) › Required format
  - Veo reference (Google) › 4. Dialogue syntax (critical) › Voice character modifiers
  - Veo reference (Google) › 4. Dialogue syntax (critical) › Timing rule
  - Veo reference (Google) › 5. SFX syntax
  - Veo reference (Google) › 6. JSON prompts (powerful, unique)
  - Veo reference (Google) › 6. JSON prompts (powerful, unique) › Full schema
  - Veo reference (Google) › 6. JSON prompts (powerful, unique) › When to use JSON
  - Veo reference (Google) › 7. Image-to-video (Veo 3.1)
  - Veo reference (Google) › 8. Reference ingredients (3.1)
  - Veo reference (Google) › 9. Failure modes and fixes
  - Veo reference (Google) › 9. Failure modes and fixes › Dialogue speeds up unnaturally
  - Veo reference (Google) › 9. Failure modes and fixes › Audio missing from output
  - Veo reference (Google) › 9. Failure modes and fixes › Camera direction ignored
  - Veo reference (Google) › 9. Failure modes and fixes › Character color changes when mood words are added
  - Veo reference (Google) › 9. Failure modes and fixes › Lip-sync off
  - Veo reference (Google) › 9. Failure modes and fixes › Prompt too long, model cherry-picks
  - Veo reference (Google) › 10. Skeleton
  - Veo reference (Google) › 10. Skeleton › Prose version
  - Veo reference (Google) › 10. Skeleton › JSON version
  - Veo reference (Google) › 10. Skeleton › Worked example. Commercial hero shot

### visual-asset-critic

- **skills/visual-asset-critic/LICENSE** (licencia)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - Visual Asset Critic
  - Visual Asset Critic › When to use
  - Visual Asset Critic › What you produce
  - Visual Asset Critic › Inputs
  - Visual Asset Critic › Workflow
  - Visual Asset Critic › Workflow › Step 1. Establish intent
  - Visual Asset Critic › Workflow › Step 2. Critique by layer
  - Visual Asset Critic › Workflow › Step 3. Map issues to fixes
  - Visual Asset Critic › Workflow › Step 4. Verdict
  - Visual Asset Critic › Workflow › Step 5. Confidence
  - Visual Asset Critic › Workflow › Step 6. Emit structured output (critique JSON)
  - Visual Asset Critic › Workflow › Step 7. Run the gate
  - Visual Asset Critic › Hard rules
  - Visual Asset Critic › Hard rules › Rule 1. No vibes-based critique
  - Visual Asset Critic › Hard rules › Rule 2. Prompt-level fixes must be specific
  - Visual Asset Critic › Hard rules › Rule 3. Don't critique what wasn't asked
  - Visual Asset Critic › Hard rules › Rule 4. Be honest about generator limits
  - Visual Asset Critic › Hard rules › Rule 5. When in doubt, ACCEPT and recommend post
  - Visual Asset Critic › Reference
  - Visual Asset Critic › Example output
  - Visual Asset Critic › Handoff
- **skills/visual-asset-critic/examples/critique.accept.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/critique.revise.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/worked-run/brand-lock.snapshot.md** (ejemplo)
  - (texto antes del primer encabezado)
  - Brand Lock: WhyStrohm
  - Brand Lock: WhyStrohm › Identity
  - Brand Lock: WhyStrohm › Palette
  - Brand Lock: WhyStrohm › Typography
  - Brand Lock: WhyStrohm › Mood adjectives
  - Brand Lock: WhyStrohm › Never list
  - Brand Lock: WhyStrohm › Aspect ratios
  - Brand Lock: WhyStrohm › Color grade direction
  - Brand Lock: WhyStrohm › Motion language
  - Brand Lock: WhyStrohm › Voice rules
- **skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot_01.critique.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot_02.critique.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/worked-run/critiques/round-2/shot_02.critique.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/worked-run/preview.html** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/worked-run/prompts/round-1/flux.txt** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/worked-run/prompts/round-2/revised-flux.txt** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/worked-run/run.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/worked-run/shots.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/examples/worked-run/text-overlays.json** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/references/critique-rubric.md** (referencia)
  - Critique Rubric
  - Critique Rubric › Layer 1. Brand Lock check
  - Critique Rubric › Layer 2. Series Lock check
  - Critique Rubric › Layer 3. Shot Spec check
  - Critique Rubric › Layer 4. Composition check
  - Critique Rubric › Layer 5. Technical check
  - Critique Rubric › Layer 6. Continuity check (if previous shots available)
  - Critique Rubric › From pass/fail to severity
  - Critique Rubric › Aggregating verdict
  - Critique Rubric › Speed bumps to remember
- **skills/visual-asset-critic/templates/critique.schema.json** (plantilla)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/README.md** (herramienta)
  - Tools
  - Tools › Requirements
  - Tools › Run everything
  - Tools › Repo checks
  - Tools › Repo checks › `validate_skills.py`
  - Tools › Repo checks › `validate_schemas.py`
  - Tools › Repo checks › `validate_capabilities.py`
  - Tools › Repo checks › `validate_brand_lock.py`
  - Tools › Project checks
  - Tools › Project checks › `validate_shots.py`
  - Tools › Project checks › `validate_prompts.py`
  - Tools › Project checks › `validate_critique.py`
  - Tools › Project checks › `validate_provenance.py`
  - Tools › Rendering
  - Tools › Rendering › `shots-to-html.py`
  - Tools › Rendering › `copy-prompt.py`
  - Tools › Internal modules
  - Tools › Adding new tools
- **skills/visual-asset-critic/tools/_shotkit.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/_template.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/check.sh** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/copy-prompt.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/shots-to-html.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/validate_brand_lock.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/validate_capabilities.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/validate_critique.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/validate_prompts.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/validate_provenance.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/validate_schemas.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/validate_shots.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-asset-critic/tools/validate_skills.py** (herramienta)
  - (texto antes del primer encabezado)

### visual-media

- **skills/visual-media/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - Creación Visual — Visual Media
  - Creación Visual — Visual Media › Cuándo aplica
  - Creación Visual — Visual Media › Fundamentos de fotografía
  - Creación Visual — Visual Media › Fundamentos de fotografía › Triángulo de exposición
  - Creación Visual — Visual Media › Fundamentos de fotografía › Reglas de composición
  - Creación Visual — Visual Media › Fundamentos de fotografía › Uso de la luz
  - Creación Visual — Visual Media › Producción de video
  - Creación Visual — Visual Media › Producción de video › Flujo de producción
  - Creación Visual — Visual Media › Producción de video › Movimientos de cámara
  - Creación Visual — Visual Media › Producción de video › Uso de los tipos de plano
  - Creación Visual — Visual Media › Contenido de formato corto
  - Creación Visual — Visual Media › Contenido de formato corto › Perfil de cada plataforma
  - Creación Visual — Visual Media › Contenido de formato corto › Estructura de un video corto
  - Creación Visual — Visual Media › Fundamentos de animación
  - Creación Visual — Visual Media › Fundamentos de animación › Los 12 principios
  - Creación Visual — Visual Media › Fundamentos de animación › Flujo de producción de animación
  - Creación Visual — Visual Media › Postproducción y edición
  - Creación Visual — Visual Media › Postproducción y edición › Ritmo de edición
  - Creación Visual — Visual Media › Postproducción y edición › Fundamentos de colorización
  - Creación Visual — Visual Media › Herramientas recomendadas
  - Creación Visual — Visual Media › Herramientas recomendadas › Equipo de captura
  - Creación Visual — Visual Media › Herramientas recomendadas › Software de edición
  - Creación Visual — Visual Media › Herramientas recomendadas › Herramientas de animación
  - Creación Visual — Visual Media › Recursos

### visual-prompt-forge

- **skills/visual-prompt-forge/LICENSE** (licencia)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/SKILL.md** (SKILL)
  - (texto antes del primer encabezado)
  - Visual Prompt Forge
  - Visual Prompt Forge › When to use
  - Visual Prompt Forge › What you produce
  - Visual Prompt Forge › The five-layer prompt anatomy
  - Visual Prompt Forge › Workflow
  - Visual Prompt Forge › Workflow › Step 1. Read inputs
  - Visual Prompt Forge › Workflow › Step 2. Pick the adapters
  - Visual Prompt Forge › Workflow › Step 3. Compose per shot
  - Visual Prompt Forge › Workflow › Step 4. Write output files
  - Visual Prompt Forge › Workflow › Step 4b. Append the round to run.json
  - Visual Prompt Forge › Workflow › Step 5. Hand off
  - Visual Prompt Forge › Revision mode (closing the QA loop)
  - Visual Prompt Forge › Revision mode (closing the QA loop) › Trigger
  - Visual Prompt Forge › Revision mode (closing the QA loop) › Workflow
  - Visual Prompt Forge › Revision mode (closing the QA loop) › Output
  - Visual Prompt Forge › Revision mode (closing the QA loop) › Determinism, and its limits
  - Visual Prompt Forge › Hard rules
  - Visual Prompt Forge › Hard rules › Rule 1. Text is never in the prompt
  - Visual Prompt Forge › Hard rules › Rule 2. Brand colors never in shot subject prose
  - Visual Prompt Forge › Hard rules › Rule 3. Series_lock anchors are verbatim
  - Visual Prompt Forge › Hard rules › Rule 4. Adapters are the source of truth on syntax
  - Visual Prompt Forge › Hard rules › Rule 6. Shot logic before shot poetry
  - Visual Prompt Forge › Hard rules › Rule 5. Prompts must be reproducible
  - Visual Prompt Forge › Reference files
  - Visual Prompt Forge › Adapters
  - Visual Prompt Forge › Quality bar
  - Visual Prompt Forge › Examples
- **skills/visual-prompt-forge/adapters/_capabilities.json** (adaptador)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/adapters/capabilities.schema.json** (adaptador)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/adapters/flux.md** (adaptador)
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev)
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › Syntax pattern
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › Where parameters go
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › Length
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › Composition mapping
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › Photographic specifics
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › Composition pattern
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › Example
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › Flux variant selection
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › Pitfalls to avoid
  - Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev) › API access
- **skills/visual-prompt-forge/adapters/gpt-image.md** (adaptador)
  - Adapter: GPT Image (1.5 / 2)
  - Adapter: GPT Image (1.5 / 2) › Syntax pattern
  - Adapter: GPT Image (1.5 / 2) › Parameters
  - Adapter: GPT Image (1.5 / 2) › Length
  - Adapter: GPT Image (1.5 / 2) › Spatial language strength
  - Adapter: GPT Image (1.5 / 2) › Composition pattern
  - Adapter: GPT Image (1.5 / 2) › Example
  - Adapter: GPT Image (1.5 / 2) › Text rendering
  - Adapter: GPT Image (1.5 / 2) › Pitfalls to avoid
  - Adapter: GPT Image (1.5 / 2) › API access
- **skills/visual-prompt-forge/adapters/hailuo.md** (adaptador)
  - Adapter: Hailuo 02 Pro (motion-aware video, budget iteration)
  - Adapter: Hailuo 02 Pro (motion-aware video, budget iteration) › Syntax pattern
  - Adapter: Hailuo 02 Pro (motion-aware video, budget iteration) › Parameters
  - Adapter: Hailuo 02 Pro (motion-aware video, budget iteration) › Length
  - Adapter: Hailuo 02 Pro (motion-aware video, budget iteration) › Motion vocabulary
  - Adapter: Hailuo 02 Pro (motion-aware video, budget iteration) › Iteration workflow
  - Adapter: Hailuo 02 Pro (motion-aware video, budget iteration) › Example
  - Adapter: Hailuo 02 Pro (motion-aware video, budget iteration) › Pitfalls to avoid
  - Adapter: Hailuo 02 Pro (motion-aware video, budget iteration) › Output handoff
- **skills/visual-prompt-forge/adapters/ideogram.md** (adaptador)
  - Adapter: Ideogram (v3)
  - Adapter: Ideogram (v3) › Mode 1: Composited (default)
  - Adapter: Ideogram (v3) › Mode 2: Text-in-image (override)
  - Adapter: Ideogram (v3) › Syntax pattern (Mode 2)
  - Adapter: Ideogram (v3) › Parameters
  - Adapter: Ideogram (v3) › Length
  - Adapter: Ideogram (v3) › Composition pattern (Mode 1, composited)
  - Adapter: Ideogram (v3) › Composition pattern (Mode 2, text-in-image)
  - Adapter: Ideogram (v3) › Example (Mode 2)
  - Adapter: Ideogram (v3) › When NOT to use Ideogram
  - Adapter: Ideogram (v3) › Pitfalls to avoid
- **skills/visual-prompt-forge/adapters/kling.md** (adaptador)
  - Adapter: Kling 3.0 (motion-aware video)
  - Adapter: Kling 3.0 (motion-aware video) › Syntax pattern
  - Adapter: Kling 3.0 (motion-aware video) › Parameters
  - Adapter: Kling 3.0 (motion-aware video) › Length
  - Adapter: Kling 3.0 (motion-aware video) › Motion vocabulary
  - Adapter: Kling 3.0 (motion-aware video) › Subject motion
  - Adapter: Kling 3.0 (motion-aware video) › Example
  - Adapter: Kling 3.0 (motion-aware video) › Continuity across shots
  - Adapter: Kling 3.0 (motion-aware video) › Pitfalls to avoid
  - Adapter: Kling 3.0 (motion-aware video) › Output handoff
- **skills/visual-prompt-forge/adapters/midjourney.md** (adaptador)
  - Adapter: Midjourney (v7)
  - Adapter: Midjourney (v7) › Syntax pattern
  - Adapter: Midjourney (v7) › Parameter reference (current as of Q2 2026)
  - Adapter: Midjourney (v7) › Length
  - Adapter: Midjourney (v7) › Composition mapping
  - Adapter: Midjourney (v7) › Lighting language
  - Adapter: Midjourney (v7) › Composition pattern
  - Adapter: Midjourney (v7) › Example
  - Adapter: Midjourney (v7) › Pitfalls to avoid
  - Adapter: Midjourney (v7) › API access note
- **skills/visual-prompt-forge/adapters/nano-banana.md** (adaptador)
  - Adapter: Nano Banana (Gemini 2.5 Flash Image)
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › Syntax pattern
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › Parameters
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › Length
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › Composition pattern (text-to-image)
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › Composition pattern (image-to-image, the strength)
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › Example (text-to-image)
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › Example (image-to-image variant)
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › Variant-generation workflow
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › Pitfalls to avoid
  - Adapter: Nano Banana (Gemini 2.5 Flash Image) › API access
- **skills/visual-prompt-forge/adapters/seedance.md** (adaptador)
  - Adapter: Seedance 2.0 (motion-aware video, multi-shot)
  - Adapter: Seedance 2.0 (motion-aware video, multi-shot) › Syntax pattern
  - Adapter: Seedance 2.0 (motion-aware video, multi-shot) › Parameters
  - Adapter: Seedance 2.0 (motion-aware video, multi-shot) › Length
  - Adapter: Seedance 2.0 (motion-aware video, multi-shot) › When to use multi-shot vs single
  - Adapter: Seedance 2.0 (motion-aware video, multi-shot) › Motion vocabulary
  - Adapter: Seedance 2.0 (motion-aware video, multi-shot) › Example
  - Adapter: Seedance 2.0 (motion-aware video, multi-shot) › Pitfalls to avoid
  - Adapter: Seedance 2.0 (motion-aware video, multi-shot) › Output handoff
- **skills/visual-prompt-forge/adapters/seedream.md** (adaptador)
  - Adapter: Seedream (4.5 / 4.0)
  - Adapter: Seedream (4.5 / 4.0) › Syntax pattern
  - Adapter: Seedream (4.5 / 4.0) › Parameters
  - Adapter: Seedream (4.5 / 4.0) › Length
  - Adapter: Seedream (4.5 / 4.0) › Composition pattern
  - Adapter: Seedream (4.5 / 4.0) › Example
  - Adapter: Seedream (4.5 / 4.0) › When Seedream is the right choice
  - Adapter: Seedream (4.5 / 4.0) › When Seedream is the wrong choice
  - Adapter: Seedream (4.5 / 4.0) › Series consistency
  - Adapter: Seedream (4.5 / 4.0) › Pitfalls to avoid
  - Adapter: Seedream (4.5 / 4.0) › API access
- **skills/visual-prompt-forge/adapters/veo.md** (adaptador)
  - Adapter: Veo 3 (motion-aware video, native audio)
  - Adapter: Veo 3 (motion-aware video, native audio) › Syntax pattern
  - Adapter: Veo 3 (motion-aware video, native audio) › Parameters
  - Adapter: Veo 3 (motion-aware video, native audio) › Length
  - Adapter: Veo 3 (motion-aware video, native audio) › Dialogue and lipsync
  - Adapter: Veo 3 (motion-aware video, native audio) › Motion vocabulary
  - Adapter: Veo 3 (motion-aware video, native audio) › Audio direction
  - Adapter: Veo 3 (motion-aware video, native audio) › Example
  - Adapter: Veo 3 (motion-aware video, native audio) › Pitfalls to avoid
  - Adapter: Veo 3 (motion-aware video, native audio) › Output handoff
- **skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md** (ejemplo)
  - One Shot, All Adapters
  - One Shot, All Adapters › The source shot
  - One Shot, All Adapters › Series lock context (constant across all adapters)
  - One Shot, All Adapters › Brand mood
  - One Shot, All Adapters › Outputs
  - One Shot, All Adapters › What's not in any prompt
- **skills/visual-prompt-forge/examples/one-shot-all-adapters/flux.txt** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/examples/one-shot-all-adapters/ideogram.txt** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/examples/one-shot-all-adapters/kling.txt** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/examples/one-shot-all-adapters/midjourney.txt** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/examples/one-shot-all-adapters/nano-banana.txt** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/examples/one-shot-all-adapters/seedream.txt** (ejemplo)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/references/consistency-locks.md** (referencia)
  - Consistency Locks
  - Consistency Locks › Lock 1. Verbatim character anchors
  - Consistency Locks › Lock 2. Verbatim environment anchors
  - Consistency Locks › Lock 3. Verbatim lighting anchors
  - Consistency Locks › Lock 4. Seed locking
  - Consistency Locks › Lock 5. Reference images (`--cref`, omni-reference, image-to-image)
  - Consistency Locks › Lock 6. Style references
  - Consistency Locks › Lock 7. Lighting direction continuity
  - Consistency Locks › Lock 8. Color grade flow-through
  - Consistency Locks › Failure modes when locks are missing
  - Consistency Locks › What doesn't work
- **skills/visual-prompt-forge/references/failure-modes.md** (referencia)
  - Failure Modes
  - Failure Modes › Failure 1. The "AI look"
  - Failure Modes › Failure 2. Character drift across shots
  - Failure Modes › Failure 3. Text in image looks bad
  - Failure Modes › Failure 4. Lighting direction inconsistency
  - Failure Modes › Failure 5. Composition doesn't reserve space for text overlay
  - Failure Modes › Failure 6. Series feels "different" even with locks applied
  - Failure Modes › Failure 7, "Looks fine but doesn't match the brief"
  - Failure Modes › When to stop iterating prompts
- **skills/visual-prompt-forge/references/prompt-anatomy.md** (referencia)
  - Prompt Anatomy: The Five Layers
  - Prompt Anatomy: The Five Layers › Layer 1. Brand Lock
  - Prompt Anatomy: The Five Layers › Layer 2. Series Lock
  - Prompt Anatomy: The Five Layers › Layer 3. Shot Spec
  - Prompt Anatomy: The Five Layers › Layer 4. Text Layer
  - Prompt Anatomy: The Five Layers › Layer 5. Generator Adapter
  - Prompt Anatomy: The Five Layers › How layers compose
  - Prompt Anatomy: The Five Layers › Why this matters operationally
- **skills/visual-prompt-forge/tools/README.md** (herramienta)
  - Tools
  - Tools › Requirements
  - Tools › Run everything
  - Tools › Repo checks
  - Tools › Repo checks › `validate_skills.py`
  - Tools › Repo checks › `validate_schemas.py`
  - Tools › Repo checks › `validate_capabilities.py`
  - Tools › Repo checks › `validate_brand_lock.py`
  - Tools › Project checks
  - Tools › Project checks › `validate_shots.py`
  - Tools › Project checks › `validate_prompts.py`
  - Tools › Project checks › `validate_critique.py`
  - Tools › Project checks › `validate_provenance.py`
  - Tools › Rendering
  - Tools › Rendering › `shots-to-html.py`
  - Tools › Rendering › `copy-prompt.py`
  - Tools › Internal modules
  - Tools › Adding new tools
- **skills/visual-prompt-forge/tools/_shotkit.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/_template.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/check.sh** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/copy-prompt.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/shots-to-html.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/validate_brand_lock.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/validate_capabilities.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/validate_critique.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/validate_prompts.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/validate_provenance.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/validate_schemas.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/validate_shots.py** (herramienta)
  - (texto antes del primer encabezado)
- **skills/visual-prompt-forge/tools/validate_skills.py** (herramienta)
  - (texto antes del primer encabezado)

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
