# Clasificación aumentada — textos en la misma posición que INV-002054

98 textos del universo cuelgan directamente del título principal de su documento (o están antes de él, en el frontmatter), sin subsección. Para cada documento: la cadena que lo carga, de arriba abajo, con la línea exacta, y el modelo que resulta. Para cada texto: su ruta y el dictamen de la lectura.

## `skills/image/SKILL.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»

Modelo que resulta: **los dos: Nano Banana y GPT Image 2**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-001998 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › (frontmatter) | --- name: image license: CC-BY-4.0 (attribution required — Serge Shima, github.com/smixs/visual-skills) description: >   Image prompting skill for Nano Banan… | declara los dos modelos (NB y GPT Image 2) y excluye video, 3D y audio |
| INV-001999 | 14 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Image Prompting — Nano Banana & GPT Image 2 | # Image Prompting — Nano Banana & GPT Image 2 | título, separador o autor; sin contenido normativo |
| INV-002000 | 16 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Image Prompting — Nano Banana & GPT Image 2 | This skill writes image prompts. It does not generate images. The output is: model name + quality / size / aspect ratio + the prompt itself. | la salida es modelo + quality/size/ratio + prompt; vale para GPT Image 2 |
| INV-002001 | 18 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Image Prompting — Nano Banana & GPT Image 2 | The body of this SKILL.md is intentionally thin so you cannot fake a result by reading it alone. The actual rules — what the models reward, what they punish,… | las reglas viven en los archivos de referencia; obliga a leerlos |
| INV-002007 | 28 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS | # Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS | título, separador o autor; sin contenido normativo |
| INV-002008 | 30 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS | Past attempts to write prompts directly from this skill body produced lazy, generic results. Each model has its own physics; common rules collapse into mush … | obliga al orden de lectura antes de escribir cualquier prompt |
| INV-002042 | 84 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Output format | # Output format | título, separador o autor; sin contenido normativo |
| INV-002043 | 86 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Output format | When you return the prompt, structure it like this: | introduce la cabecera de salida |
| INV-002044 | 88 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Output format | ``` Model: <nano-banana-2 \| nano-banana-pro \| gpt-image-2> Quality: <low \| medium \| high>          (only for gpt-image-2) Size / Ratio: <e.g. 1536×1024 o… | cabecera: Model, Quality (solo gpt-image-2), Size/Ratio, Prompt, Notes; vale para GPT Image 2 |
| INV-002045 | 100 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Output format | For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana): | lista preserve obligatoria en ediciones con gpt-image-2 |
| INV-002046 | 102 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Output format | ``` Change: <one concrete thing> Preserve: <face, pose, lighting, framing, geometry, ...> Constraints: <no extra objects, no drift, ...> ``` | bloque Change / Preserve / Constraints de edición |
| INV-002047 | 108 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Output format | --- | título, separador o autor; sin contenido normativo |
| INV-002048 | 110 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Final response style | # Final response style | título, separador o autor; sin contenido normativo |
| INV-002049 | 112 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Final response style | Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano Banana). | preferir sintaxis del modelo: 5-slot para GPT Image |
| INV-002050 | 114 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Final response style | Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars" — inv… | el elogio vago daña a GPT Image 2; la parte de lente numérica es solo de Nano Banana y no aplica a GPT Image 2 (que admite «50mm feel» como look, prompt-framework.md:42) |
| INV-002051 | 116 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Final response style | --- | título, separador o autor; sin contenido normativo |
| INV-002052 | 118 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › SKILL.md › Final response style | *Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · Licen… | título, separador o autor; sin contenido normativo |

## `skills/image/references/characters.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :58 «Character continuity across multiple images / panels»

Modelo que resulta: **el modelo elegido; el Paso 4 no restringe**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002053 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › characters.md › Character Consistency | # Character Consistency | título, separador o autor; sin contenido normativo |
| INV-002054 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › characters.md › Character Consistency | Up to 16 reference images, each indexed with its role (GPT Image 2; high fidelity by default). Identity locking across scenes. | CORREGIDO (correcciones.json): el original daba el desglose de NBP (14 = 6+5+3, nano-banana.md:64-66, :144); ahora da la cifra de GPT Image 2 (16 con rol, alta fidelidad por defecto) |

## `skills/image/references/creative-direction.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :74 Step 5 «read for production language»

Modelo que resulta: **el modelo elegido; el paso no restringe**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002084 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › creative-direction.md › Creative Direction | # Creative Direction | título, separador o autor; sin contenido normativo |
| INV-002085 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › creative-direction.md › Creative Direction | Studio-quality controls for lighting, camera, color, and materiality. | alcance del documento: luz, cámara, color y materialidad; sin cifra de modelo |

## `skills/image/references/dimensional.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :62 «2D → 3D, floor plans, isometric»

Modelo que resulta: **el modelo elegido; el Paso 4 no restringe**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002167 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › dimensional.md › Dimensional Translation | # Dimensional Translation | título, separador o autor; sin contenido normativo |
| INV-002168 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › dimensional.md › Dimensional Translation | 2D↔3D conversions. Floor plans to renders, memes to 3D. | alcance: conversiones 2D↔3D; sin cifra de modelo |

## `skills/image/references/editing.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :57 «Edit existing image»

Modelo que resulta: **los dos, con diferencias por modelo (línea 3 del propio documento)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002194 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › editing.md › Image Editing | # Image Editing | título, separador o autor; sin contenido normativo |
| INV-002195 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › editing.md › Image Editing | Универсальные паттерны. Логика edit'а различается по моделям: | el edit difiere por modelo; las dos líneas siguientes lo desglosan (la de NB, INV-002196, salió) |
| INV-002197 | 6 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › editing.md › Image Editing | - **GPT Image 2:** двухколоночная логика **Change / Preserve / Constraints**. Preserve list повторять каждую итерацию, иначе drift. Опционально `mask_image_u… | edición en GPT Image 2: Change / Preserve / Constraints, preserve en cada iteración |
| INV-002198 | 8 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › editing.md › Image Editing | Общее правило: **один edit за итерацию**, не пытайся менять всё разом. | un edit por iteración, para cualquier modelo |

## `skills/image/references/golden-rules.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :48 Step 3 «always read after the model file» («Universal rules that apply to both models», :50)

Modelo que resulta: **los dos**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002238 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › golden-rules.md › Golden Rules | # Golden Rules | título, separador o autor; sin contenido normativo |
| INV-002239 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › golden-rules.md › Golden Rules | Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md), [gpt-… | declara el documento universal para los dos modelos |

## `skills/image/references/gpt-image.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :38 Step 2 «read one model file» › :43 «GPT Image 2 → gpt-image.md»

Modelo que resulta: **solo GPT Image 2**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002331 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › gpt-image.md › GPT Image 2 — Specific Rules | # GPT Image 2 — Specific Rules | título, separador o autor; sin contenido normativo |
| INV-002332 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › gpt-image.md › GPT Image 2 — Specific Rules | Production default OpenAI: `gpt-image-2`. Migration-only: `gpt-image-1.5`, `gpt-image-1`. Бюджетный: `gpt-image-1-mini`. | gpt-image-2 es el default; 1.5 y 1 solo migración; 1-mini presupuesto |

## `skills/image/references/models.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :32 Step 1 «always read first → models.md» («Decide: Nano Banana (NB2 or NBP) or GPT Image 2», :34)

Modelo que resulta: **los dos; sirve para elegir modelo**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002415 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › models.md › Model Selection — Nano Banana vs GPT Image 2 | # Model Selection — Nano Banana vs GPT Image 2 | título, separador o autor; sin contenido normativo |
| INV-002416 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › models.md › Model Selection — Nano Banana vs GPT Image 2 | Skill пишет промпты под две семьи моделей. Они мыслят по-разному — выбор модели меняет структуру промпта. | el skill escribe para dos familias y el modelo cambia la estructura del prompt |

## `skills/image/references/multi-panel.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :64 «Multi-panel compositions»

Modelo que resulta: **el modelo elegido; el Paso 4 no restringe**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002473 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › multi-panel.md › Multi-Panel Compositions | # Multi-Panel Compositions | título, separador o autor; sin contenido normativo |
| INV-002474 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › multi-panel.md › Multi-Panel Compositions | Single-image layouts containing multiple frames, panels, or grid cells. Unlike [storyboards.md](storyboards.md) (sequential images generated one-at-a-time), … | una sola imagen con todos los paneles, a diferencia de storyboards.md |
| INV-002475 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › multi-panel.md › Multi-Panel Compositions | Core principle: explicitly number and describe every panel. Models need panel-by-panel instructions — vague requests like "show multiple angles" produce inco… | numerar y describir cada panel; sin cifra de modelo |
| INV-002476 | 7 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › multi-panel.md › Multi-Panel Compositions | --- | título, separador o autor; sin contenido normativo |

## `skills/image/references/patterns/character-design.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :71 «Character design»

Modelo que resulta: **GPT Image 2 por defecto («Default model: GPT Image 2 (5-slot format) unless noted», línea 3 del propio documento)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002675 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › character-design.md › Character Design Patterns | # Character Design Patterns | título, separador o autor; sin contenido normativo |
| INV-002676 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › character-design.md › Character Design Patterns | Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}` for cu… | plantillas con GPT Image 2 (5-slot) por defecto salvo nota |
| INV-002677 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › character-design.md › Character Design Patterns | --- | título, separador o autor; sin contenido normativo |

## `skills/image/references/patterns/ecommerce.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :66 «E-commerce product shots»

Modelo que resulta: **GPT Image 2 por defecto («Default model: GPT Image 2 (5-slot format) unless noted», línea 3 del propio documento)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002718 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › ecommerce.md › E-Commerce Product Photography Patterns | # E-Commerce Product Photography Patterns | título, separador o autor; sin contenido normativo |
| INV-002719 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › ecommerce.md › E-Commerce Product Photography Patterns | Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Image 2 (… | plantillas con GPT Image 2 (5-slot) por defecto salvo nota |
| INV-002720 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › ecommerce.md › E-Commerce Product Photography Patterns | --- | título, separador o autor; sin contenido normativo |

## `skills/image/references/patterns/fashion-editorial.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :67 «Fashion editorial campaigns»

Modelo que resulta: **GPT Image 2 por defecto («Default model: GPT Image 2 (5-slot format) unless noted», línea 3 del propio documento)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002760 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › fashion-editorial.md › Fashion Editorial Patterns | # Fashion Editorial Patterns | título, separador o autor; sin contenido normativo |
| INV-002761 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › fashion-editorial.md › Fashion Editorial Patterns | Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GPT Image… | plantillas con GPT Image 2 (5-slot) por defecto salvo nota |
| INV-002762 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › fashion-editorial.md › Fashion Editorial Patterns | --- | título, separador o autor; sin contenido normativo |

## `skills/image/references/patterns/food-beverage.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :68 «Food & beverage advertising»

Modelo que resulta: **GPT Image 2 por defecto («Default model: GPT Image 2 (5-slot format) unless noted», línea 3 del propio documento)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002801 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › food-beverage.md › Food & Beverage Patterns | # Food & Beverage Patterns | título, separador o autor; sin contenido normativo |
| INV-002802 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › food-beverage.md › Food & Beverage Patterns | Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Default mod… | plantillas con GPT Image 2 (5-slot) por defecto salvo nota |
| INV-002803 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › food-beverage.md › Food & Beverage Patterns | --- | título, separador o autor; sin contenido normativo |

## `skills/image/references/patterns/portrait-cinema.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :69 «Cinematic portraits»

Modelo que resulta: **GPT Image 2 por defecto («Default model: GPT Image 2 (5-slot format) unless noted», línea 3 del propio documento)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002861 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › portrait-cinema.md › Portrait & Cinema Patterns | # Portrait & Cinema Patterns | título, separador o autor; sin contenido normativo |
| INV-002862 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › portrait-cinema.md › Portrait & Cinema Patterns | Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for custom… | plantillas con GPT Image 2 (5-slot) por defecto salvo nota |
| INV-002863 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › portrait-cinema.md › Portrait & Cinema Patterns | --- | título, separador o autor; sin contenido normativo |

## `skills/image/references/patterns/poster-illustration.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :70 «Posters & illustration»

Modelo que resulta: **GPT Image 2 por defecto («Default model: GPT Image 2 (5-slot format) unless noted», línea 3 del propio documento)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002902 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › poster-illustration.md › Poster & Illustration Patterns | # Poster & Illustration Patterns | título, separador o autor; sin contenido normativo |
| INV-002903 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › poster-illustration.md › Poster & Illustration Patterns | Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. Default m… | plantillas con GPT Image 2 (5-slot) por defecto salvo nota |
| INV-002904 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › poster-illustration.md › Poster & Illustration Patterns | --- | título, separador o autor; sin contenido normativo |

## `skills/image/references/patterns/ui-social.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :72 «UI mockups & social media formats»

Modelo que resulta: **GPT Image 2 por defecto («Default model: GPT Image 2 (5-slot format) unless noted», línea 3 del propio documento)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002945 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › ui-social.md › UI Mockups & Social Media Patterns | # UI Mockups & Social Media Patterns | título, separador o autor; sin contenido normativo |
| INV-002946 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › ui-social.md › UI Mockups & Social Media Patterns | Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for customiz… | plantillas con GPT Image 2 (5-slot) por defecto salvo nota |
| INV-002947 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › ui-social.md › UI Mockups & Social Media Patterns | --- | título, separador o autor; sin contenido normativo |

## `skills/image/references/prompt-framework.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :78 Step 6 «read if structuring a complex prompt»

Modelo que resulta: **el modelo elegido; el paso no restringe**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-002988 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › prompt-framework.md › Prompt Framework | # Prompt Framework | título, separador o autor; sin contenido normativo |
| INV-002989 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › prompt-framework.md › Prompt Framework | Универсальный чеклист для построения промпта. Применим к **обеим** семьям моделей. Для отличий смотри: | checklist universal para los dos modelos |
| INV-002991 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › prompt-framework.md › Prompt Framework | - [gpt-image.md](gpt-image.md) — GPT Image 2 (5-slot template, anti-slop, quality settings) | enlace a gpt-image.md (5-slot, anti-slop, quality) |
| INV-002992 | 6 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › prompt-framework.md › Prompt Framework | - [models.md](models.md) — какую модель когда выбрать | enlace a models.md para elegir modelo |

## `skills/image/references/slides.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :59 «Presentation slides»

Modelo que resulta: **el modelo elegido; el Paso 4 no restringe**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-003088 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › slides.md › Presentation Slides | # Presentation Slides | título, separador o autor; sin contenido normativo |
| INV-003089 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › slides.md › Presentation Slides | Professional slide visuals for decks and pitches. | alcance: diapositivas; sin cifra de modelo |

## `skills/image/references/storyboards.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :60 «Sequential narrative (storyboard, comic, panel sequence)»

Modelo que resulta: **el modelo elegido; el Paso 4 no restringe**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-003225 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › storyboards.md › Storyboards & Sequential Art | # Storyboards & Sequential Art | título, separador o autor; sin contenido normativo |
| INV-003226 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › storyboards.md › Storyboards & Sequential Art | One-shot narrative sequences. Concept art. Consistent across frames. | alcance: secuencias y concept art; sin cifra de modelo |

## `skills/image/references/structural.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :61 «Sketch → final, wireframes, structural input»

Modelo que resulta: **el modelo elegido; el Paso 4 no restringe**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-003255 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › structural.md › Structural Control | # Structural Control | título, separador o autor; sin contenido normativo |
| INV-003256 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › structural.md › Structural Control | Input images control composition. Sketch→final, wireframes, grids. | alcance: imágenes de entrada controlan la composición; sin cifra de modelo |

## `skills/image/references/text-rendering.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :56 «Text in image, infographic, diagram, multilingual rendering»

Modelo que resulta: **los dos, con diferencias por modelo (línea 3 del propio documento)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-003294 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › text-rendering.md › Text Rendering & Infographics | # Text Rendering & Infographics | título, separador o autor; sin contenido normativo |
| INV-003295 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › text-rendering.md › Text Rendering & Infographics | Универсальные стили, layout-типы, примеры. Применимо к обеим моделям, но детали рендера расходятся: | universal para los dos modelos, con detalles de render distintos |
| INV-003297 | 6 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › text-rendering.md › Text Rendering & Infographics | - **GPT Image 2:** EXACT TEXT в `"..."` или ALL CAPS, добавляй «no extra words / no duplicate text», для мелкого текста — `quality: high`. См. [gpt-image.md]… | texto en GPT Image 2: EXACT TEXT entre comillas o ALL CAPS, quality high para texto pequeño |

## `skills/image/references/vision-decomposer.md`

Cadena de carga:

1. ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)
2. image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»
3. image/SKILL.md:28 «Mandatory reading order» › :52 Step 4 «task-shaped reading (load only what matches the request)» › :63 «Vision analysis / image-to-prompt / style transfer from a reference image»

Modelo que resulta: **el modelo elegido; el Paso 4 no restringe**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-003393 | 1 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › vision-decomposer.md › Vision Decomposer — Image-to-Prompt Analysis | # Vision Decomposer — Image-to-Prompt Analysis | título, separador o autor; sin contenido normativo |
| INV-003394 | 3 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › vision-decomposer.md › Vision Decomposer — Image-to-Prompt Analysis | Use this reference when the user asks to analyze an image and convert it to a generation prompt: **style transfer**, **mood reference**, **"сделай промпт по … | cuándo usar el documento: análisis de imagen a prompt |
| INV-003395 | 5 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › vision-decomposer.md › Vision Decomposer — Image-to-Prompt Analysis | You become a **professional Vision Agent**. Your task is deep cinematic, psychological and optical-colorimetric analysis of the image, translating it into a … | rol de Vision Agent; sin cifra de modelo |
| INV-003396 | 7 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › vision-decomposer.md › Vision Decomposer — Image-to-Prompt Analysis | The process has two strict steps. Do not skip Step 1. Do not freestyle Step 2. | dos pasos estrictos; el Paso 2 (INV-003433, con nota) pide keywords con comas, que choca con adapters/gpt-image.md:86 |
| INV-003397 | 9 | ai-production-director/SKILL.md:34 › image/SKILL.md:5 › image/SKILL.md:28 › vision-decomposer.md › Vision Decomposer — Image-to-Prompt Analysis | --- | título, separador o autor; sin contenido normativo |

## `skills/visual-asset-critic/SKILL.md`

Cadena de carga:

1. ai-production-director/SKILL.md:36 (§1) «visual-asset-critic | 5 · QA» y :94 (Etapa 5)
2. visual-asset-critic/SKILL.md:3 (frontmatter): no nombra modelo; critica cualquier imagen generada

Modelo que resulta: **cualquier modelo de imagen**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-009765 | 1 | ai-production-director/SKILL.md:36 › visual-asset-critic/SKILL.md:3 › SKILL.md › (frontmatter) | --- name: visual-asset-critic description: Critique a generated image against its source storyboard shot and prompt, producing revision notes. Use when the u… | crítica de cualquier imagen generada; no nombra modelo |
| INV-009766 | 6 | ai-production-director/SKILL.md:36 › visual-asset-critic/SKILL.md:3 › SKILL.md › Visual Asset Critic | # Visual Asset Critic | título, separador o autor; sin contenido normativo |
| INV-009767 | 8 | ai-production-director/SKILL.md:36 › visual-asset-critic/SKILL.md:3 › SKILL.md › Visual Asset Critic | You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structured rev… | rol de revisión editorial; sin cifra de modelo |
| INV-009768 | 10 | ai-production-director/SKILL.md:36 › visual-asset-critic/SKILL.md:3 › SKILL.md › Visual Asset Critic | The output is a critique with concrete, actionable revision notes. Not vibes. Not "looks good." Specific, prompt-level or post-level fixes. | la salida son arreglos concretos de prompt o de post |

## `skills/visual-asset-critic/references/critique-rubric.md`

Cadena de carga:

1. ai-production-director/SKILL.md:36 (§1) «visual-asset-critic | 5 · QA» y :94 (Etapa 5)
2. visual-asset-critic/SKILL.md:3 (frontmatter): no nombra modelo; critica cualquier imagen generada
3. visual-asset-critic/SKILL.md:79 «Workflow › Step 2. Critique by layer» :81 «Read references/critique-rubric.md for the full rubric» y :244 «Reference»

Modelo que resulta: **cualquier modelo de imagen**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-010313 | 1 | ai-production-director/SKILL.md:36 › visual-asset-critic/SKILL.md:3 › visual-asset-critic/SKILL.md:79 › critique-rubric.md › Critique Rubric | # Critique Rubric | título, separador o autor; sin contenido normativo |
| INV-010314 | 3 | ai-production-director/SKILL.md:36 › visual-asset-critic/SKILL.md:3 › visual-asset-critic/SKILL.md:79 › critique-rubric.md › Critique Rubric | The structured layer-by-layer pass. Use this as the checklist when reviewing a generated image. | checklist por capas para revisar una imagen generada |

## `skills/visual-prompt-forge/SKILL.md`

Cadena de carga:

1. ai-production-director/SKILL.md:35 (§1) «visual-prompt-forge | 5–6 · Prompts» y :94 (Etapa 5: forge genera borradores, image es la autoridad de sintaxis final)
2. visual-prompt-forge/SKILL.md:3 (frontmatter) «stills (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream) and motion video»

Modelo que resulta: **varios generadores, GPT Image incluido**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-011265 | 1 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › SKILL.md › (frontmatter) | --- name: visual-prompt-forge description: Generate model-specific prompts from shots.json. Outputs copy-paste-ready prompts for stills (Midjourney, Flux, Id… | GPT Image es uno de los generadores de imagen fija del skill |
| INV-011266 | 6 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › SKILL.md › Visual Prompt Forge | # Visual Prompt Forge | título, separador o autor; sin contenido normativo |
| INV-011267 | 8 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › SKILL.md › Visual Prompt Forge | You are turning structured shot data into prompts that work in production. Each image generator rewards a different prompting style, short and high-signal fo… | cada generador premia un estilo: párrafo para GPT Image |
| INV-011268 | 10 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › SKILL.md › Visual Prompt Forge | This skill adapts. Same shot, different syntax. | mismo shot, distinta sintaxis |

## `skills/visual-prompt-forge/adapters/gpt-image.md`

Cadena de carga:

1. ai-production-director/SKILL.md:35 (§1) «visual-prompt-forge | 5–6 · Prompts» y :94 (Etapa 5: forge genera borradores, image es la autoridad de sintaxis final)
2. visual-prompt-forge/SKILL.md:3 (frontmatter) «stills (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream) and motion video»
3. visual-prompt-forge/SKILL.md:85 «Workflow › Step 2. Pick the adapters» :87 «For each target generator, read the matching adapter file» :92 «adapters/gpt-image.md»; :327 tabla «GPT Image 1.5 / 2»

Modelo que resulta: **GPT Image 1.5 y 2**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-011718 | 1 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:85 › gpt-image.md › Adapter: GPT Image (1.5 / 2) | # Adapter: GPT Image (1.5 / 2) | título, separador o autor; sin contenido normativo |
| INV-011719 | 3 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:85 › gpt-image.md › Adapter: GPT Image (1.5 / 2) | > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_pro… | manda _capabilities.json sobre el adaptador; la entrada GPT Image (_capabilities.json:54-69) da 300 palabras máximo, aspect_param size, sin style ref ni negative prompt |
| INV-011720 | 5 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:85 › gpt-image.md › Adapter: GPT Image (1.5 / 2) | GPT Image rewards paragraph-form prompts with explicit spatial reasoning and complex composition descriptions. It interprets relational language ("to the lef… | GPT Image: párrafos, razonamiento espacial explícito, texto preciso |

## `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md`

Cadena de carga:

1. ai-production-director/SKILL.md:35 (§1) «visual-prompt-forge | 5–6 · Prompts» y :94 (Etapa 5: forge genera borradores, image es la autoridad de sintaxis final)
2. visual-prompt-forge/SKILL.md:3 (frontmatter) «stills (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream) and motion video»
3. visual-prompt-forge/SKILL.md:369 «Examples» :371 «one-shot-all-adapters … Use it to calibrate output quality»

Modelo que resulta: **todos los adaptadores; su salida GPT Image es 1.5 (README.md:44)**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-012171 | 1 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:369 › README.md › One Shot, All Adapters | # One Shot, All Adapters | título, separador o autor; sin contenido normativo |
| INV-012172 | 3 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:369 › README.md › One Shot, All Adapters | This example takes a single shot from the WhyStrohm 30-second pitch and renders it through the generator adapters in the pack. Use it as a calibration refere… | ejemplo de calibración con 6 adaptadores de imagen y Kling; su salida GPT Image es 1.5 y salió (sección 1344) |

## `skills/visual-prompt-forge/references/consistency-locks.md`

Cadena de carga:

1. ai-production-director/SKILL.md:35 (§1) «visual-prompt-forge | 5–6 · Prompts» y :94 (Etapa 5: forge genera borradores, image es la autoridad de sintaxis final)
2. visual-prompt-forge/SKILL.md:3 (frontmatter) «stills (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream) and motion video»
3. visual-prompt-forge/SKILL.md:312 «Reference files» :315

Modelo que resulta: **cualquier generador; cada lock nombra los suyos**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-012217 | 1 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:312 › consistency-locks.md › Consistency Locks | # Consistency Locks | título, separador o autor; sin contenido normativo |
| INV-012218 | 3 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:312 › consistency-locks.md › Consistency Locks | Visual consistency across a storyboard is the hardest problem in AI image generation. Generators are stateless, every prompt is interpreted fresh. Without co… | los generadores no tienen estado; sin locks hay deriva; sin cifra de modelo |
| INV-012219 | 5 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:312 › consistency-locks.md › Consistency Locks | This document covers the techniques that actually work in 2026. | técnicas vigentes en 2026; sin cifra de modelo |

## `skills/visual-prompt-forge/references/failure-modes.md`

Cadena de carga:

1. ai-production-director/SKILL.md:35 (§1) «visual-prompt-forge | 5–6 · Prompts» y :94 (Etapa 5: forge genera borradores, image es la autoridad de sintaxis final)
2. visual-prompt-forge/SKILL.md:3 (frontmatter) «stills (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream) and motion video»
3. visual-prompt-forge/SKILL.md:312 «Reference files» :316

Modelo que resulta: **cualquier generador; cada arreglo nombra los suyos**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-012277 | 1 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:312 › failure-modes.md › Failure Modes | # Failure Modes | título, separador o autor; sin contenido normativo |
| INV-012278 | 3 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:312 › failure-modes.md › Failure Modes | What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work. | qué falla y qué se arregla en el prompt o en edición; sin cifra de modelo |

## `skills/visual-prompt-forge/references/prompt-anatomy.md`

Cadena de carga:

1. ai-production-director/SKILL.md:35 (§1) «visual-prompt-forge | 5–6 · Prompts» y :94 (Etapa 5: forge genera borradores, image es la autoridad de sintaxis final)
2. visual-prompt-forge/SKILL.md:3 (frontmatter) «stills (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream) and motion video»
3. visual-prompt-forge/SKILL.md:51 «The five-layer prompt anatomy» y :312 «Reference files» :314

Modelo que resulta: **cualquier generador**

| Id | Línea | Ruta aumentada | Texto | Dictamen |
|---|---:|---|---|---|
| INV-012369 | 1 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:51 › prompt-anatomy.md › Prompt Anatomy: The Five Layers | # Prompt Anatomy: The Five Layers | título, separador o autor; sin contenido normativo |
| INV-012370 | 3 | ai-production-director/SKILL.md:35 › visual-prompt-forge/SKILL.md:3 › visual-prompt-forge/SKILL.md:51 › prompt-anatomy.md › Prompt Anatomy: The Five Layers | Every image prompt this skill produces is composed from five layers. Four are inputs, one is applied at compose-time. Understanding the layers is the differe… | cinco capas por prompt; sin cifra de modelo |
