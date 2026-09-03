# SKILL: image

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: image/SKILL.md

---
name: image
license: CC-BY-4.0 (attribution required — Serge Shima, github.com/smixs/visual-skills)
description: >
  Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2. Writes ready-to-use
  prompts with model/quality/size recommendations. Use when: "нарисуй", "сгенерируй
  картинку", "image prompt", "промпт для картинки", blog covers, slides, posters,
  product shots, UI mockups, storyboards, character sheets, edit/colorize, style transfer,
  vision analysis, image-to-prompt, nb, NBP, NB2, gpt-image-2, multi-panel grids,
  ecommerce product photography, fashion editorial, food/beverage ads, cinematic portraits.
  Do NOT use for: video (use video skill), 3D models, audio, non-image tasks.
---

# Image Prompting — Nano Banana & GPT Image 2

This skill writes image prompts. It does not generate images. The output is: model name + quality / size / aspect ratio + the prompt itself.

The body of this SKILL.md is intentionally thin so you cannot fake a result by reading it alone. The actual rules — what the models reward, what they punish, how to phrase a 5-slot template, when to add `quality: high`, when to use image grounding — live only in the reference files.

## Route first — is this actually an image-prompt task?

- **Motion, clips, montage** (Seedance, Kling, Veo, any image-to-video): use the sibling `video` skill. This skill's storyboard and keyframe outputs feed it.
- **No idea or script yet** (user wants a concept or an ad scenario, not a picture): if the `creative-director` skill is installed, start there — it develops ideas and scripts for commercials and beyond ([github.com/smixs/creative-director-skill](https://github.com/smixs/creative-director-skill)).
- **A concrete image is needed** — this skill. Continue below.

---

# Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS

Past attempts to write prompts directly from this skill body produced lazy, generic results. Each model has its own physics; common rules collapse into mush when applied without model-specific syntax. Read in this order before producing any prompt:

### Step 1 — always read first → [models.md](references/models.md)

Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot template, quality settings, which features exist (image grounding only on NB, EXACT TEXT discipline only on GPT Image, etc.).

If the user named a model — confirm and proceed. If not — pick using the table in `models.md`, then state your choice in the output header.

### Step 2 — read **one** model file (the one you picked)

- **Nano Banana** → [nano-banana.md](references/nano-banana.md)
  Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mode. JSON for 5+ elements. Up to 14 reference images. Why you must NOT write `50mm / f-stop / ISO` numbers.

- **GPT Image 2** → [gpt-image.md](references/gpt-image.md)
  5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop banned-words list. `quality: low / medium / high` as a deliberate fidelity lever. Size constraints (multiples of 16, max 3:1, up to 2560×1440). Two-column edit logic (Change / Preserve / Constraints). Up to 16 reference images with explicit roles.

The model file is non-negotiable. Skipping it is the single biggest cause of weak prompts.

### Step 3 — always read after the model file → [golden-rules.md](references/golden-rules.md)

Universal rules that apply to both models: start with a verb, positive framing, hex colors, quote text, edit don't re-roll, one change per iteration, reference images.

### Step 4 — task-shaped reading (load only what matches the request)

Pick zero or more, depending on what the user asked for:

- Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
- Edit existing image (object removal, lighting swap, colorization, restoration, localization) → [editing.md](references/editing.md)
- Character continuity across multiple images / panels → [characters.md](references/characters.md)
- Presentation slides → [slides.md](references/slides.md)
- Sequential narrative (storyboard, comic, panel sequence) → [storyboards.md](references/storyboards.md)
- Sketch → final, wireframes, structural input → [structural.md](references/structural.md)
- 2D → 3D, floor plans, isometric → [dimensional.md](references/dimensional.md)
- **Vision analysis / image-to-prompt / style transfer from a reference image** → [vision-decomposer.md](references/vision-decomposer.md). Load this whenever the user attaches an image and asks to recreate, match, decompose, or transfer its style.
- **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 portrait grids, 3-panel campaign collages, 4x3 borderless grids, 6-frame cinematic sequences, before/after splits, 12-panel storyboard posters.
- **Industry pattern libraries** — proven prompt templates by vertical. Load the matching file:
  - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)
  - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - Food & beverage advertising → [patterns/food-beverage.md](references/patterns/food-beverage.md)
  - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - Posters & illustration → [patterns/poster-illustration.md](references/patterns/poster-illustration.md)
  - Character design (turnarounds, expression sheets, outfit grids) → [patterns/character-design.md](references/patterns/character-design.md)
  - UI mockups & social media formats → [patterns/ui-social.md](references/patterns/ui-social.md)

### Step 5 — read for production language → [creative-direction.md](references/creative-direction.md)

Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise terms beyond what `golden-rules.md` covers.

### Step 6 — read if structuring a complex prompt → [prompt-framework.md](references/prompt-framework.md)

Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / standard / verbose / cinematic verbose), parameterized templates, output structure with parameters and exclusions.

---

# Output format

When you return the prompt, structure it like this:

```
Model: <nano-banana-2 | nano-banana-pro | gpt-image-2>
Quality: <low | medium | high>          (only for gpt-image-2)
Size / Ratio: <e.g. 1536×1024 or 16:9>

Prompt:
<the prompt text, ready to copy>

Notes:
- <anything you inferred or assumed because the user did not specify>
```

For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):

```
Change: <one concrete thing>
Preserve: <face, pose, lighting, framing, geometry, ...>
Constraints: <no extra objects, no drift, ...>
```

---

# Final response style

Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano Banana).

Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars" — invert to positive), external comparisons ("like Apple ad" — describe the visual properties instead), numerical lens parameters in Nano Banana prompts (it ignores them).

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/characters.md

# Character Consistency

Up to 14 reference images (6 high-fidelity). Identity locking across scenes.

## Identity Locking

```
Using person from [IMAGE REFERENCE]:
Keep facial features exactly the same.
Change: [EXPRESSION / POSE / CLOTHING / SETTING]
Maintain: identity, recognizable features
```

Key phrase: "Keep facial features exactly the same as Image 1"

## Viral Thumbnails

```
Design viral thumbnail using person from Image 1.

Face: Keep features same, change expression to [excited/surprised/shocked]
Action: Pose on [left/right], pointing toward [OBJECT]
Subject: [OBJECT] on opposite side
Graphics: Bold [COLOR] arrow connecting person to object
Text: "[HEADLINE]" in massive pop-style, white outline, drop shadow
Background: Blurred [SETTING]

High saturation and contrast.
```

## Multi-Character Consistency

```
Create [NUMBER]-part story with these [N] characters.

Identity: Keep attire and features consistent throughout.
Variation: Different angles, expressions, distances per image.
Rule: Only one of each character per image.

Story arc: [DESCRIPTION with emotional highs/lows]
```

## Brand Asset Generation

```
Using this [PRODUCT] as reference:
Create [NUMBER] [TYPE] shots.

Maintain: Brand consistency, quality level
Vary: Angles, lighting, context
Style: [editorial / lifestyle / product]

Generate one at a time.
```

## Expression Control

While maintaining identity:
- "Change expression to excited and surprised"
- "Make them look thoughtful, gazing left"
- "Add confident smile, direct eye contact"

## Pose/Action Control

- "Pose pointing finger toward [DIRECTION]"
- "Standing with arms crossed"
- "Mid-stride, dynamic motion"
- "Seated, leaning forward"

## Attire Changes

- "Same person, but wearing [NEW OUTFIT]"
- "Keep face, change to formal business attire"
- "Maintain identity, add [ACCESSORY]"

## Environment Swaps

- "Same person in [NEW SETTING]"
- "Transport to [LOCATION], keep identity"
- "Change background to [SCENE], maintain lighting on face"

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/creative-direction.md

# Creative Direction

Studio-quality controls for lighting, camera, color, and materiality.

## Lighting Design

Tell the model exactly how the scene is illuminated.

**Studio setups:**
- "Three-point softbox setup" — even product/portrait lighting
- "Single key light from upper left" — dramatic shadow
- "Ring light, frontal" — beauty/fashion, flat lighting

**Dramatic effects:**
- "Chiaroscuro lighting with harsh, high contrast"
- "Golden hour backlighting creating long shadows"
- "Rim lighting, subject silhouetted against bright background"
- "Volumetric god rays through window"
- "Neon underglow, cyberpunk street"

**Natural:**
- "Soft overcast daylight, even diffusion"
- "Dappled sunlight through trees"
- "Blue hour, cold ambient light"

## Camera & Hardware

Specify camera type to change the visual DNA of the image.

**Hardware names that work:**
- GoPro — immersive, wide-angle distortion, action feel
- Fujifilm — authentic color science, warm tones
- Disposable camera — raw, nostalgic flash aesthetic, grain
- Hasselblad — medium format, shallow DOF, fashion/portrait
- iPhone — casual, smartphone aesthetic
- Polaroid — instant film, white border, faded colors

**Angles:**
- "Low angle" — power, drama
- "Aerial view" / "bird's eye" — scale, pattern
- "Eye-level" — neutral, relatable
- "Dutch angle" — tension, unease
- "Worm's eye view" — extreme drama

**Shot types:**
- Close-up, medium shot, wide shot, extreme close-up
- "Waist-up portrait", "full body", "over-the-shoulder"

**Focus:**
- "Shallow depth of field" — blurred background
- "Deep focus" — everything sharp
- "Rack focus" — shift attention
- "Tilt-shift" — miniature effect

> Note: Named lens parameters (50mm, f/2.8) are less reliable than
> descriptive terms. Prefer "shallow depth of field" over "f/1.8".

## Color Grading & Film Stock

Set emotional tone through color and texture.

**Film stocks:**
- "Shot on 1980s color film, slightly grainy" — nostalgic
- "Kodak Portra 400" — warm skin tones, pastel highlights
- "Fuji Velvia" — hyper-saturated, vivid
- "Ilford HP5" — classic B&W grain
- "Cinestill 800T" — tungsten, halation around lights

**Digital grades:**
- "Cinematic color grading with muted teal tones"
- "High contrast, desaturated" — gritty, editorial
- "Warm analog tones, lifted blacks" — vintage
- "Cool blue shadows, warm highlights" — modern cinema
- "Cross-processed, shifted greens" — experimental

## Materiality & Texture

Define physical makeup of subjects. Don't just say the thing — describe what it's MADE of.

| Vague | Specific |
|-------|----------|
| "a suit" | "navy blue tweed suit, visible weave" |
| "armor" | "ornate elven plate armor, etched with silver leaf patterns" |
| "a mug" | "minimalist ceramic coffee mug, matte glaze, slight imperfections" |
| "skin" | "weathered, sun-damaged skin, deep expression lines" |
| "metal" | "brushed steel with matte finish, fingerprint smudges" |

**Surface properties:**
- Matte / glossy / satin
- Rough / smooth / textured
- Translucent / opaque / refractive
- Worn / pristine / aged / patinated

## Creative Prompt Examples

**Cartoon Portrait (3D + Real):**
```
Based on the uploaded reference image, create a photorealistic scene
featuring the real human standing next to a giant 3D animation-style
version of themselves. Both must have identical facial structures,
clothing, and poses. Clean gray-blue studio background, cinematic lighting.
```

**Animation → Photorealistic:**
```
Convert this uploaded animated still into an ultra-realistic, cinematic
scene. Transform the animated characters into real humans while preserving
their original identities, facial structures, outfits, and expressions.
```

**Historical Maps (Google Street View style):**
```
Generate a hyper-realistic image of [HISTORICAL EVENT], perfectly
replicating a Google Maps Street View capture. Include wide-angle barrel
distortion, semi-transparent Maps UI overlay (compass, chevron arrows),
and '© Google [YEAR]' watermark. Automatically blur faces for privacy.
```

**Kindergarten Filter:**
```
A child's crayon drawing on white lined notebook paper of [SUBJECT].
Use chunky wax-crayon strokes, wobbly outlines, bold colors that overflow
the lines. Visible pressure marks, waxy smudges, uneven scribble shading.
Joyful, naive art style.
```

**Fashion Editorial:**
```
[Subject description]. [Action/pose]. [Setting].
Medium-full shot, center-framed.
Fashion magazine style editorial, shot on medium-format analog film,
pronounced grain, high saturation, cinematic lighting effect.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/dimensional.md

# Dimensional Translation

2D↔3D conversions. Floor plans to renders, memes to 3D.

## 2D Floor Plan → 3D

```
Based on this 2D floor plan, generate interior visualization.

Layout: Design board format
Main image: Wide-angle [ROOM] perspective (top 60%)
Below: 3 smaller renders - [ROOM A], [ROOM B], [ROOM C]

Style: [Modern minimalist / Scandinavian / Industrial]
Materials: [flooring], [walls], [textiles]
Lighting: Soft natural light, large windows
Quality: Photorealistic rendering
```

## Sketch → 3D Concept

```
Convert this sketch into [STYLE] visualization.
Perspective: [CAMERA ANGLE]
Lighting: [SETUP]
Quality: [photorealistic / stylized / rendered]
```

## 3D → 2D Technical

```
Flatten this 3D scene into [STYLE].
Views: [plan / elevation / section]
Labels: [ANNOTATIONS]
Line work: technical, precise
```

## Meme Conversion

```
Turn "[MEME NAME]" meme into [NEW STYLE].
Keep composition identical.
Character: [plush toy / realistic / cartoon]
Environment: [realistic flames / stylized / etc]
```

Example:
- "Turn 'This is Fine' dog into photorealistic 3D render"
- "Make the dog look like plush toy, fire realistic"

## Architectural Visualization

**Exterior:**
```
Generate exterior visualization from this elevation.
Time: [dawn / midday / dusk / night]
Weather: [clear / overcast / dramatic clouds]
Context: [landscaping / street / aerial view]
```

**Interior:**
```
Generate interior from this plan.
View: [living area / kitchen / bedroom]
Style: [AESTHETIC]
Lighting: [natural / artificial / mixed]
Props: [furniture / decor / people]
```

## Product 2D → 3D

```
Convert this flat design into 3D product mockup.
Material: [plastic / metal / fabric / glass]
Lighting: [studio / environmental]
Angle: [front / 3-quarter / top-down]
```

## Quality Levels

- "Sketch quality" - rough, conceptual
- "Presentation quality" - clean, professional
- "Photorealistic" - indistinguishable from photo
- "Stylized render" - artistic interpretation

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/editing.md

# Image Editing

Универсальные паттерны. Логика edit'а различается по моделям:

- **Nano Banana:** conversational, без масок. «Keep X same, change Y». Хорошо понимает физику и материалы.
- **GPT Image 2:** двухколоночная логика **Change / Preserve / Constraints**. Preserve list повторять каждую итерацию, иначе drift. Опционально `mask_image_url` для точечных edit'ов. Лучшая identity preservation. См. [gpt-image.md](gpt-image.md#editing--двухколоночная-логика).

Общее правило: **один edit за итерацию**, не пытайся менять всё разом.

## Object Removal
```
Remove [OBJECT] from this image.
Fill with [LOGICAL REPLACEMENT] matching surroundings.
Keep [PRESERVED ELEMENTS] exactly the same.
```

Examples:
- "Remove tourists, fill with cobblestones"
- "Remove car, extend street naturally"

## Object Addition
```
Add [OBJECT] to this image.
Position: [LOCATION]
Style: matching existing lighting
Scale: [RELATIVE SIZE]
```

## Lighting Control
```
Change lighting to [NEW LIGHTING].
Keep subject and composition same.
```

Vocabulary:
- Golden hour / sunset / warm backlight
- Overcast / soft / diffused
- Night / dramatic / single source
- Rim lighting / silhouette

## Seasonal/Weather
```
Turn scene into [SEASON/WEATHER].
Keep architecture exactly same.
Adjust: [snow/leaves/reflections/sky]
```

## Colorization

**Photo:**
```
Colorize this B&W photograph.
Era-appropriate colors for [DECADE].
Skin tones: natural, realistic
```

**Manga:**
```
Colorize this manga panel.
Style: [vibrant anime / muted realistic]
Effects: [glowing/neon] for energy elements
Maintain: line art integrity
```

## Restoration
```
Restore this damaged photograph.
Fix: [tears/scratches/fading/stains]
Enhance: sharpness, contrast
Preserve: original character and grain
```

## Localization
```
Translate all [SOURCE] text to [TARGET].
Keep everything else same.
Maintain: font style, sizing, position
```

Cultural adaptation:
```
Localize this [ORIGINAL] ad to [TARGET MARKET].
Background: [NEW LOCATION]
Translate: text to [LANGUAGE]
Keep: brand elements, core composition
```

## Physics-Aware

NBP understands materials:
```
Fill this glass with [LIQUID].
Add: refraction, meniscus, condensation
Match: existing lighting
```

```
Add [MATERIAL] texture to [SURFACE].
Properties: [matte/glossy], [rough/smooth]
```

## Conversational Refinement

After initial edit:
- "Make it warmer"
- "Increase contrast"
- "Soften the edges"
- "Add more detail to shadows"

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/golden-rules.md

# Golden Rules

Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2).
Для модельной специфики см. [nano-banana.md](nano-banana.md), [gpt-image.md](gpt-image.md).

## 1. Start with a Verb

Tell the model the primary operation: "Create", "Generate", "Design", "Transform", "Convert", "Edit". This sets the intent before details.

## 2. Positive Framing

Describe what you WANT, not what you don't want. The model understands presence better than absence.

- ✅ "empty street" → ❌ "street with no cars"
- ✅ "clean background" → ❌ "no clutter"  
- ✅ "solo portrait" → ❌ "no other people"

## 3. Edit, Don't Re-roll

Image 80% correct? Request specific change:
- "Change lighting to sunset"
- "Make text neon blue"
- "Move chart to right third"

## 4. Natural Language

❌ Bad: "Cool car, neon, city, night, 8k"
✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neon signs reflect off wet pavement and metallic chassis."

## 5. Be Specific

| Element | Vague | Specific |
|---------|-------|----------|
| Subject | "a woman" | "sophisticated elderly woman in vintage Chanel-style suit" |
| Material | "shiny" | "brushed steel with matte finish" |
| Color | "dark green" | "#0d3d2d deep emerald" |
| Position | "on the right" | "right third, bleeding off edge" |

## 6. Provide Context

Context helps model make logical decisions:
- "for Brazilian gourmet cookbook" → infers professional plating, shallow DOF
- "for executive strategy presentation" → infers corporate aesthetic
- "for children's educational app" → infers friendly, colorful style

## 7. Quote Text Exactly

Any text for rendering goes in quotes:
- "[HEADLINE TEXT]"
- Labels: "[Revenue Growth]", "[Net Income]"
- Specify weight: bold, thin, extra bold
- Specify position: "upper third", "centered"

## Prompt Template

```
Create a [TYPE] for [CONTEXT].

Background: [Description with hex colors]. [Atmospheric effects].

[HERO ELEMENT]:
[Detailed description - position, lighting, angle]

Typography:
Line 1: "[TEXT]" in [weight], [color], [size], [position]
Line 2: "[TEXT]" in [weight], [color], [size], [position]

[ADDITIONAL ELEMENTS]

Mood: [Emotional descriptor]
Format: [ASPECT RATIO]
```

> **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.

## Cost Optimization (Batch Work)

- **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
- **GPT Image 2:** прогон на `quality: low` → отбор → переген на `medium` или `high`.

В обоих случаях: дешёвая разведка → дорогой финал.

## Conversational Refinement

After generation:
- "Change the headline color to #3b82f6"
- "Add subtle drop shadow to text"
- "Increase contrast, make it more dramatic"
- "Soften the background, add blur"

## Reference Images

Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.

Используй для:

**Вписать в существующий дизайн:**
```
[Attach design/layout image]
Create content following this exact layout and style.
Replace [ELEMENT] with [NEW CONTENT].
Keep colors, typography, composition.
```

**Лицо/персонаж как референс:**
```
[Attach portrait]
Use this person's face. Keep features exactly the same.
Change: [expression/pose/setting]
```

**Продукт/объект как референс:**
```
[Attach product photo]
Place this product in [NEW CONTEXT].
Match lighting and perspective.
```

**Стиль как референс:**
```
[Attach style reference]
Create [NEW CONTENT] in this exact visual style.
Match colors, textures, mood.
```

**Несколько референсов сразу:**
```
[Attach Image 1 - face]
[Attach Image 2 - outfit]
[Attach Image 3 - background]
Combine: face from Image 1, outfit style from Image 2, setting from Image 3.
```

## World Knowledge Anchors

GPT Image 2 обладает глубокими знаниями о культуре, эпохах и визуальных стилях. Вместо описания каждой детали — дай модели культурный/временной/жанровый якорь, и она сама заполнит аутентичные детали.

### Три типа якорей

**Era anchors** — временной и географический маркер, который вызывает целый визуальный мир:
- "Bethel, NY, August 1969" → Woodstock aesthetic без необходимости описывать тай-дай, грязь, сцены
- "Berlin, November 1989" → падение стены, толпы, граффити, эйфория
- "Tokyo, 1982" → неоновый Shinjuku, аналоговая электроника, ранний cyberpunk

**Cultural anchors** — перенос визуального языка одного культурного объекта на другой контекст:
- "{game_title} in {real_city}" → автоматически применяет визуальный стиль игры к реальной локации (GTA style, Persona style, и т.д.)
- "Soviet constructivism poster about {modern_topic}" → стиль Родченко/Эль Лисицкого на современную тему
- "Ukiyo-e print of {modern_scene}" → японская гравюра с современным содержанием

**Genre anchors** — режиссёр/фотограф/движение как линза:
- "Peter Lindbergh influence" → сильный Ч/Б, минимальная ретушь, raw editorial
- "Wes Anderson palette" → симметричный кадр, пастельная палитра, центрированная композиция
- "Studio Ghibli mood" → мягкое акварельное небо, зелёная листва, тёплый ностальгический свет
- "Roger Deakins lighting" → натуральный свет, глубокие тени, кинематографичный объём

### Правила использования

1. **Используй как HIGH-LEVEL steering** — якорь задаёт настроение и эстетику, а не заменяет весь промпт
2. **Комбинируй с конкретными визуальными деталями** — якорь устанавливает мир, детали устанавливают специфику
3. **Не стакай несколько genre anchors** — выбери один. "Peter Lindbergh + Wes Anderson" = каша
4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные описания

### Примеры

**Era anchor + конкретные детали:**
```
Create an editorial portrait set in Havana, 1957.

Subject: jazz musician leaning against pastel-colored colonial building,
holding trumpet loosely at his side. Linen suit, open collar.
Lighting: harsh Caribbean afternoon sun, deep shadows under awning.
Format: 3:4
```
> "Havana, 1957" вызывает: старые американские машины на заднем плане, облупившаяся штукатурка, кованые балконы, тропическая атмосфера — без необходимости это описывать.

**Cultural anchor + новый контекст:**
```
Create a scene of a quiet Kyoto temple garden, rendered in the visual style
of Studio Ghibli. Morning mist over moss-covered stones, a single monk
sweeping fallen maple leaves. Soft watercolor textures, warm nostalgic palette.
Format: 16:9
```
> "Studio Ghibli" задаёт акварельность, теплоту, ностальгию. Детали (мох, клён, монах) задают конкретную сцену.

**Genre anchor + специфика:**
```
Create a fashion editorial portrait with Peter Lindbergh influence.

Subject: model in oversized men's blazer, no makeup, wind-tousled hair.
Setting: empty winter beach, overcast sky.
Mood: raw, unpolished beauty
Format: 2:3
```
> "Peter Lindbergh influence" даёт: мощный Ч/Б (или desaturated), отсутствие ретуши, raw emotional quality. Детали (пляж, блейзер, ветер) конкретизируют кадр.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/gpt-image.md

# GPT Image 2 — Specific Rules

Production default OpenAI: `gpt-image-2`. Migration-only: `gpt-image-1.5`, `gpt-image-1`. Бюджетный: `gpt-image-1-mini`.

## Структура промпта — 5 slots

GPT Image 2 сильнее всего реагирует на разделение по секциям. Пиши лейблами, не сплошным текстом.

```
Scene: location, time of day, background, environment
Subject: primary focus — who or what is central
Important Details: materials, textures, lighting, camera angle, mood, composition
Use Case: editorial, product mockup, UI, poster, infographic
Constraints: what must NOT change/appear (no watermarks, preserve face, no extra text)
```

> «The fifth slot is where most mediocre prompts fail silently.» Без явных constraints модель дрейфует.

### Минимальный пример

```
Scene: small Lisbon florist storefront at blue hour, wet cobblestones
Subject: woman in navy apron locking the front door, half-turned to camera
Important Details: warm interior glow spilling onto pavement, 50mm feel,
  soft contact shadows, brushed brass door handle, "Florista" hand-painted sign
Use Case: editorial photography
Constraints: no extra signage, no people in background, no text other than the sign
```

## Anti-Slop Rules

GPT Image 2 особенно чувствителен к качеству формулировок. Vague praise = деградация результата.

| ❌ Не пиши | ✅ Пиши |
|-----------|---------|
| stunning, incredible, epic, gorgeous, masterpiece | overcast daylight, brushed aluminum, chipped paint, 50mm feel |
| «minimalist brutalist luxury photoreal» (стиль-теги) | «cream background, heavy black sans-serif, asymmetrical type block, one hero object, generous negative space» |
| «как в Apple-рекламе» | конкретные визуальные факты |
| мудовый язык, в котором тонут функциональные требования | прямое заявление: «image must contain a transit kiosk» |

## Quality Settings — рычаг fidelity / latency

| Setting | Когда |
|---------|-------|
| `quality: low` | High-volume, превью, exploratory, latency-sensitive, draft |
| `quality: medium` | **Default starting point** |
| `quality: high` | Маленький/плотный текст, infographics, портреты, identity-sensitive edits, brand assets |

Стартуй с `low`, апгрейди по необходимости. Часто `low` уже достаточно.

## Размеры (gpt-image-2)

- Max edge: <3840px
- Обе стороны: кратны 16
- Aspect ratio: max 3:1 (long:short)
- Total pixels: 655 360 – 8 294 400
- Reliable upper bound: 2560×1440

**Ходовые:**
- Portrait 1024×1536
- Landscape 1536×1024
- Square 1024×1024
- 2K 2560×1440

> Экстрим вроде 1:8 / 8:1 GPT Image 2 НЕ умеет — иди в Nano Banana.

## Text in Image

- Литеральный текст в `"..."` или ALL CAPS.
- Шрифт, размер, цвет, позиция — явно.
- Сложные слова и бренды: спеллинг по буквам.
- Защита от мусора: «**no extra words, no duplicate text, no watermarks**».
- Для нечитаемого мелкого текста: «**100 percent readable and physically believable**».
- Маленький/плотный/multi-font → `quality: high` обязательно.

## Editing — двухколоночная логика

Endpoint: `openai/gpt-image-2/edit` (на fal.ai) или соответствующий через OpenAI API.

```
Change: [single concrete change]
Preserve: face, identity, pose, lighting, framing, background, geometry, text, layout
Constraints: no extra objects, no redesign, no drift
```

**Правила edit:**
- **Один edit за итерацию.** Не пытайся менять всё разом.
- **Preserve list повторять каждую итерацию.** Иначе дрейф.
- **Surgical edits:** явно перечисли что НЕ трогать (saturation, contrast, layout, arrows, labels, camera angle).
- Опционально: `mask_image_url` для точечных edits.

### Edit-паттерны

**Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows so outfit looks naturally worn.»

**Object removal:** «Remove [X]. Do not change anything else. Use `input_fidelity: high` to maintain surrounding context» (только gpt-image-1.5/1, в gpt-image-2 high-fidelity по умолчанию).

**Lighting/weather swap:** «Change ONLY environmental conditions: lighting direction/quality, shadows, atmosphere, precipitation. Preserve identity, geometry, camera angle, object placement.»

**Interior swap:** «Swap [furniture]. Preserve camera angle, lighting, shadows, surrounding context. Photorealistic contact shadows.»

## Multi-Image — до 16 рефов

Индексируй с **ролью**, не только номером:
```
Image 1: base scene
Image 2: jacket reference (apply only the jacket fabric/cut to subject in Image 1)
Image 3: lighting reference (apply golden-hour quality from Image 3)
```

## Style Transfer

Не пиши абстрактно («minimalist», «editorial»). Назови конкретные визуальные свойства референса: палитра, edge treatment, силуэт, обработка теней, plane логика.

## World Knowledge

GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не расписывай каждую деталь.

## Iteration Strategy

- Стартуй с **чистого** базового промпта.
- Один change за раунд. «Make lighting warmer», «remove extra tree», «restore original background».
- При drift — перечисли invariants заново.
- Для длинных промптов — labeled sections, не одна простыня.

## Use-Case Templates

### Photoreal Editorial
```
Scene: [location, time, weather]
Subject: [who, action, framing]
Important Details: [lens feel, light source, surface wear, imperfections, real texture]
Use Case: editorial photograph, looks like a real photo
Constraints: no glamorization, no heavy retouching, no studio gloss
```

### Product Mockup (Clean Background)
```
Scene: plain white opaque background
Subject: [product] centered
Important Details: crisp silhouette, no halos/fringing, light contact shadow,
  preserve label legibility exactly, preserve geometry
Use Case: product mockup
Constraints: no restyling, only background removal + light polish
```

### UI Mockup
```
Scene: [device frame, e.g. iPhone 15 Pro]
Subject: [screen/app name] — describe AS IF IT EXISTS, not concept art
Important Details: layout, hierarchy, real interface elements, exact copy in quotes,
  typography behavior, spacing, state
Use Case: shipped product screenshot
Constraints: no sketch language, no placeholder text, no Lorem Ipsum
Quality: high (for small UI text)
```

### Marketing Creative with Text
```
Scene: [environment]
Subject: [hero element]
Important Details: [composition, palette, mood]
Use Case: ad creative for [audience]
Text: "EXACT HEADLINE" in [font style], [color], [position]
      "exact subhead" in [font style], [color], [position]
Constraints: no extra text, no duplicate text, no watermarks, no unrelated logos
Quality: high
```

### Infographic / Diagram
```
Title: "[TITLE]"
Content flow: [step 1] → [step 2] → [step 3]
Visual format: [layout type — flowchart, pyramid, isometric, etc.]
Use Case: educational infographic for [audience]
Constraints: readable labels at all sizes, clear hierarchy, no clutter,
  no decorative noise, ample whitespace
Quality: high
Size: 1536×1024
```

## Migration from Older GPT-Image

- Промпты в основном переносятся как есть.
- После переноса — посмотри качество, latency, retry-rate; ретюнь.
- `gpt-image-1-mini` — только если главное снизить цену batch'а на низкорисковых задачах.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/models.md

# Model Selection — Nano Banana vs GPT Image 2

Skill пишет промпты под две семьи моделей. Они мыслят по-разному — выбор модели меняет структуру промпта.

## TL;DR

| Задача | Модель |
|--------|--------|
| Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
| Сложная сцена с физикой/композицией | **Nano Banana Pro** |
| Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
| Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
| Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
| Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
| Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
| Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
| Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
| Storyboard с фокусом на типографике | **GPT Image 2** |
| Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
| Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |

## Когда что выигрывает

### Nano Banana выигрывает в
- **Image grounding.** NB2 ищет реальные изображения в интернете перед генерацией — точная архитектура конкретного храма, моста, площади; конкретные виды животных, растений. GPT Image 2 этого не делает.
- **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
- **«Thinking» режим.** Сложные инфографики со spatial logic.
- **Цена/скорость.** NB2 = $0.04/img.

### GPT Image 2 выигрывает в
- **Identity preservation в edit.** Меняешь одежду / погоду / фон — лицо, поза, геометрия не плывут. Двухколоночная логика (change / preserve) работает как контракт.
- **Тонкий текст в кадре.** Маленькие подписи, легенды, footnotes, multi-font layouts. На `quality: high` рендерит чётче.
- **UI-моки и продуктовые скриншоты.** Иерархия, реальные интерфейс-элементы, читаемые лейблы.
- **Структурированный 5-slot промпт.** Чёткое разделение Scene/Subject/Details/Use case/Constraints даёт предсказуемость.
- **`quality` рычаг.** low/medium/high — осознанный trade-off скорости и точности.

### Где обе модели одинаково хороши
- Photorealistic портреты.
- Product shots на нейтральном фоне.
- Минималистичные постеры.
- Editorial-фотография.

## Различия в синтаксисе промпта

| Аспект | Nano Banana | GPT Image 2 |
|--------|-------------|-------------|
| Стиль промпта | Натуральный язык, 1-2 параграфа | 5-slot с лейблами секций |
| Камера/линза | **Не указывать** числа (50mm, f/2.8) — NB игнорит | Можно «50mm feel», но как high-level look |
| «Stunning/epic/masterpiece» | Игнорит, не вредит | **Anti-slop**: вредит, делает результат хуже |
| Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
| Negative framing | Использовать позитив | Использовать позитив + явный preserve list |
| Сложные сцены | JSON для 5+ элементов | 5-slot template со секциями |
| Edit | «Keep X same, change Y» | «Change: X / Preserve: Y / Constraints: Z» — повторять preserve каждую итерацию |
| Множественные референсы | До 14, индексировать | До 16, индексировать с ролью («Image 1: base», «Image 2: jacket reference») |

## Стоимость (ориентир)

| Модель | Цена | Заметки |
|--------|------|---------|
| Nano Banana 2 Lite | ~$0.034/img | Только 1K, ~4 сек. Черновики и массовые батчи |
| Nano Banana 2 (Flash) | ~$0.04/img | Default для большинства задач |
| Nano Banana Pro | ~$0.15/img | Сложные сцены, до 14 рефов |
| GPT Image 2 (`low`) | дёшево | Latency-sensitive, превью |
| GPT Image 2 (`medium`) | средне | Default для GPT Image |
| GPT Image 2 (`high`) | дороже | Маленький текст, brand-sensitive, photorealism |
| gpt-image-1-mini | дешёвый | Высокообъёмная exploratory-генерация |

> Скилл сам не запускает генерацию — выдаёт промпт. Модель/quality указываем рядом с промптом как мета.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/multi-panel.md

# Multi-Panel Compositions

Single-image layouts containing multiple frames, panels, or grid cells. Unlike [storyboards.md](storyboards.md) (sequential images generated one-at-a-time), these patterns produce **one image** with all panels baked in.

Core principle: explicitly number and describe every panel. Models need panel-by-panel instructions — vague requests like "show multiple angles" produce inconsistent grids.

---

## 1. 9-Cell Grid Storyboard

> For a product-focused narrative variant, see [patterns/ecommerce.md](patterns/ecommerce.md#9-panel-tvc-storyboard-grid).

**When to use:** TVC or commercial shot breakdown — one image = 9 panels with scene titles and timestamps.

### Template (5-slot format)

```
Scene: Dark storyboard layout — 3x3 grid of cinematic frames for a {duration}-second {product_name} commercial. Each cell has a thin dark border. Below each cell: scene number, title, and timestamp in small white sans-serif text on dark background.

Subject: {product_name} commercial storyboard showing the complete narrative arc across 9 panels.

Important Details:
Panel 1 (0:00–{t1}): {scene_1_description}
Panel 2 ({t1}–{t2}): {scene_2_description}
Panel 3 ({t2}–{t3}): {scene_3_description}
Panel 4 ({t3}–{t4}): {scene_4_description}
Panel 5 ({t4}–{t5}): {scene_5_description}
Panel 6 ({t5}–{t6}): {scene_6_description}
Panel 7 ({t6}–{t7}): {scene_7_description}
Panel 8 ({t7}–{t8}): {scene_8_description}
Panel 9 ({t8}–{duration}): {scene_9_description}

Each panel labeled below: "Scene {N}: {title}" and "{start}–{end}"

Use Case: Pre-production storyboard for video production team
Constraints: All 9 panels must be clearly separated, no merged cells, every panel must contain distinct content, timestamps must be legible, {language} titles
```

**Variables:**
- `{product_name}` — brand/product
- `{duration}` — total spot length (e.g., "30", "60")
- `{t1}` through `{t8}` — timestamp boundaries
- `{scene_1_description}` through `{scene_9_description}` — shot description per panel
- `{language}` — "Chinese" / "English" / "bilingual"

**Recommended size:** 1536x1024 (landscape)
**Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility)
**Common pitfalls:**
- Omitting panel numbers causes the model to merge or skip panels
- Vague scene descriptions produce near-identical panels — each must have a distinct action, angle, or subject
- Timestamps in very small text need `quality: high` to remain readable

---

## 2. 2x2 Editorial Portrait Grid

**When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.

### Template (5-slot format)

```
Scene: 2x2 grid of four editorial portraits, minimal gap between panels. {background_description}. {lighting_style}.

Subject: {subject_description} — same person in all four panels, consistent identity and wardrobe.

Important Details:
Top-left: front-facing portrait, direct eye contact, shoulders up
Top-right: extreme macro close-up of face — eyes, skin texture, freckles visible
Bottom-left: lower angle looking up, chin slightly raised, confident expression
Bottom-right: side profile, clean silhouette against background

Consistent lighting across all four panels. Skin texture realistic, no airbrushing.

Use Case: editorial photography, model portfolio, casting composite
Constraints: same person in every panel, no wardrobe changes between panels, no extra people, no text overlays
```

**Variables:**
- `{subject_description}` — age, appearance, wardrobe (e.g., "woman in her 30s, dark curly hair, white linen shirt")
- `{background_description}` — (e.g., "soft gray studio backdrop")
- `{lighting_style}` — (e.g., "single key light from upper left, subtle fill from right")

**Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis)
**Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (both handle photorealistic portraits well)
**Common pitfalls:**
- Not specifying "same person" in every panel — model may generate four different people
- Omitting which quadrant gets which angle — model arranges arbitrarily
- Requesting too-different crops (full body + extreme close-up) creates scale inconsistency within the grid

---

## 3. 3-Panel Campaign Collage

**When to use:** Hero shot + close-up + action for a campaign visual — horizontal or vertical triptych.

### Template (5-slot format)

```
Scene: Three-panel {orientation} collage for {brand_name} campaign. Panels separated by thin white lines.

Subject: {model_description} showcasing {product_description}.

Important Details:
Panel 1 (left/top): Hero wide shot — full figure of model with product, environmental context, lifestyle setting
Panel 2 (center/middle): Close-up product detail — {product_detail_description}, tactile textures, sharp focus
Panel 3 (right/bottom): Action shot — model using/wearing/interacting with product, candid energy, slight motion blur on extremities

Consistent warm golden-hour lighting across all panels. Same model identity throughout.
{typography_instruction}

Use Case: social media campaign visual, brand lookbook
Constraints: same person across all panels, consistent color grading, no stock-photo stiffness, {product_name} must be visible in every panel
```

**Variables:**
- `{orientation}` — "horizontal" (side by side) or "vertical" (stacked)
- `{brand_name}`, `{product_name}`, `{product_description}` — brand context
- `{model_description}` — who appears
- `{product_detail_description}` — what the close-up shows
- `{typography_instruction}` — e.g., `Text: "{HEADLINE}" in bold condensed white, overlaid on Panel 1 lower third` or omit for no text

**Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych)
**Model:** GPT Image 2 `quality: medium` — if text overlay needed, use `quality: high`
**Common pitfalls:**
- Not specifying panel order — "hero, close-up, action" without left/center/right assignment
- Lighting inconsistency when mixing indoor close-up with outdoor hero shot — specify unified lighting
- Forgetting to mention subject consistency causes three different models

---

## 4. 4x3 Borderless Grid

**When to use:** 12 panels telling a story or showing moods — no gaps between panels, seamless mosaic feel.

### Template (5-slot format)

```
Scene: 4x3 borderless grid (4 columns, 3 rows) where each of the 12 panels is an independent image but panels share no borders, gaps, or dividers — edges touch seamlessly. Overall theme: {theme}.

Subject: {subject_description} — maintain strong subject consistency across all 12 panels.

Important Details:
Row 1: {panel_1}, {panel_2}, {panel_3}, {panel_4}
Row 2: {panel_5}, {panel_6}, {panel_7}, {panel_8}
Row 3: {panel_9}, {panel_10}, {panel_11}, {panel_12}

Style: {style_description}
Mood progression: {mood_arc}
Each panel is an independent composition but the overall grid reads as a unified artwork.

Use Case: mood board, editorial spread, social media carousel preview, album artwork
Constraints: borderless — no white lines, no black borders, no gaps between panels. Same subject identity across all panels. No text in panels.
```

**Variables:**
- `{subject_description}` — who/what appears across panels
- `{theme}` — overarching concept (e.g., "solitude in a city", "four seasons of a garden")
- `{panel_1}` through `{panel_12}` — brief shot description per cell
- `{style_description}` — visual style (e.g., "35mm film grain, desaturated palette")
- `{mood_arc}` — how energy changes across the grid (e.g., "calm morning to chaotic night")

**Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution
**Model:** Nano Banana Pro (handles complex multi-element compositions with thinking mode; no text needed)
**Common pitfalls:**
- Saying "borderless" is not enough — explicitly state "no white lines, no black borders, no gaps"
- 12 panels in one image pushes detail limits — keep per-panel descriptions short and visually distinct
- Without explicit subject consistency instructions, each panel may feature a different person/object

---

## 5. 6-Frame Cinematic Sequence

**When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.

### Template (5-slot format)

```
Scene: 6-frame cinematic sequence arranged in a 3x2 grid. Dark film-strip aesthetic with thin black borders. {location_description}.

Subject: {subject_description}, wearing {wardrobe_description}. Same person, same outfit, same location across all 6 frames.

Important Details:
Frame 1 (top-left): Top-down bird's eye view — subject seen from directly above, full body visible against ground/floor
Frame 2 (top-center): Low angle looking up — subject towering over camera, dramatic perspective, sky/ceiling visible
Frame 3 (top-right): Wide isolation shot — subject small in frame, vast environment dominates, sense of scale
Frame 4 (bottom-left): Close-up with slight tilt — face and upper body, Dutch angle, intimate intensity
Frame 5 (bottom-center): Motion frame — subject mid-action ({motion_action}), natural motion blur on limbs
Frame 6 (bottom-right): Grounded final — medium shot, subject at rest, direct gaze, resolving the sequence

Photographer reference: {photographer_style}
Lighting: consistent {lighting_description} across all frames

Use Case: fashion editorial, film lookbook, director's shot list visualization
Constraints: same person and wardrobe in every frame, no costume changes, consistent color grading, no text overlays
```

**Variables:**
- `{subject_description}` — model details
- `{wardrobe_description}` — clothing
- `{location_description}` — setting
- `{motion_action}` — what the motion frame captures (e.g., "walking forward", "turning sharply", "jumping")
- `{photographer_style}` — (e.g., "Peter Lindbergh desaturated realism", "Helmut Newton dramatic contrast")
- `{lighting_description}` — (e.g., "overcast natural light, soft shadows")

**Recommended size:** 1536x1024 (landscape, 3x2 grid)
**Model:** GPT Image 2 `quality: medium` or Nano Banana Pro
**Common pitfalls:**
- Not naming each frame explicitly — "various angles" is too vague, the model needs per-frame instructions
- Top-down and low-angle in the same grid confuse the model if you don't anchor each frame to a grid position
- Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere

---

## 6. Before/After Split

**When to use:** Product transformation, makeover, time comparison, renovation — two states side by side.

### Template (5-slot format)

```
Scene: Single image split into left and right halves with a {divider_style} dividing line down the center. Before/after comparison.

Subject: {subject_description}

Important Details:
Left half (BEFORE): {before_description} — {before_condition}
Right half (AFTER): {after_description} — {after_condition}

The transition at the center line should feel {transition_style}. Same camera angle, same framing, same background perspective in both halves — only the subject's state changes.

Use Case: {use_case}
Constraints: identical composition and camera angle on both sides, same lighting direction, no text unless specified, the dividing line must be clearly visible
```

**Variables:**
- `{subject_description}` — what is being compared
- `{before_description}` / `{before_condition}` — left side state (e.g., "faded, cracked wall with peeling paint")
- `{after_description}` / `{after_condition}` — right side state (e.g., "freshly painted wall, smooth finish, vibrant color")
- `{divider_style}` — "thin white line" / "subtle gradient blend" / "sharp vertical cut"
- `{transition_style}` — "clean and abrupt" / "natural, as if wiping away"
- `{use_case}` — "product marketing", "renovation portfolio", "skincare results"

**Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion)
**Model:** GPT Image 2 `quality: medium` — for text labels ("BEFORE" / "AFTER"), use `quality: high`
**Common pitfalls:**
- Not specifying "same camera angle both sides" — model may show two completely different viewpoints
- Without a visible divider, the two halves can merge into one ambiguous scene
- Left/right assignment matters — always state which side is before and which is after

---

## 7. 12-Panel Storyboard Poster

**When to use:** Full narrative in one image — 3x4 grid (3 columns, 4 rows) for animation or video pre-production.

### Template (5-slot format)

```
Scene: 12-panel storyboard poster, 3 columns x 4 rows. Dark background with each panel in a clean rectangular frame. "{title}" in bold white text at the top of the image. Below each panel: scene number and one-line description in small white text.

Subject: {character_description} — maintain consistent character design, proportions, and colors across all 12 panels.

Important Details:
Panel 1: {scene_1} — "{caption_1}"
Panel 2: {scene_2} — "{caption_2}"
Panel 3: {scene_3} — "{caption_3}"
Panel 4: {scene_4} — "{caption_4}"
Panel 5: {scene_5} — "{caption_5}"
Panel 6: {scene_6} — "{caption_6}"
Panel 7: {scene_7} — "{caption_7}"
Panel 8: {scene_8} — "{caption_8}"
Panel 9: {scene_9} — "{caption_9}"
Panel 10: {scene_10} — "{caption_10}"
Panel 11: {scene_11} — "{caption_11}"
Panel 12: {scene_12} — "{caption_12}"

Panels read left-to-right, top-to-bottom (like a comic page). Character appearance, clothing, and color palette must stay identical across all 12 panels — only pose, expression, angle, and environment change.

Style: {art_style}

Use Case: animation pre-production, pitch deck visualization, narrative overview poster
Constraints: all 12 panels must be distinct scenes (no duplicates), character consistency is critical, scene numbers must be legible, {language} captions
Quality: high
```

**Variables:**
- `{title}` — project/episode title displayed at top
- `{character_description}` — detailed character design (colors, outfit, distinguishing features)
- `{scene_1}` through `{scene_12}` — visual description of each panel
- `{caption_1}` through `{caption_12}` — text label under each panel
- `{art_style}` — (e.g., "Pixar-style 3D", "anime cel shading", "watercolor illustration", "graphic novel ink")
- `{language}` — caption language

**Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space)
**Model:** GPT Image 2 `quality: high` (text-heavy — scene numbers and captions must be readable)
**Common pitfalls:**
- Character drift is the biggest risk at 12 panels — repeat character design details in the prompt, not just "same character"
- Without explicit scene numbering in the prompt, panels may appear in random order
- 12 panels with captions is extremely text-dense — keep captions under 5 words each for legibility
- Art style must be stated once and applied uniformly; mixing styles across panels produces visual chaos

---

## General Multi-Panel Tips

**Panel count vs. detail trade-off:** More panels = less detail per panel. 4 panels allow rich per-panel descriptions; 12 panels need brief, visually distinct descriptions (3-8 words each).

**Subject consistency:** Always include an explicit instruction: "same person / same character / same product across all panels." Repeat key identity markers (hair color, clothing, distinguishing features) rather than saying "same as before."

**Grid specification:** Always state the grid dimensions (e.g., "3x2 grid, 3 columns 2 rows"). Saying "6 panels" without layout instruction lets the model choose an unpredictable arrangement.

**Borders and gaps:** Be explicit — "thin white border between panels" or "borderless, no gaps." Default behavior varies by model and is unreliable.

**Reading order:** State it: "left-to-right, top-to-bottom" or "numbered 1-9 starting top-left." Without this, narrative flow may be jumbled.

**Model selection summary:**
- Text/labels in panels --> GPT Image 2 `quality: high`
- No text, complex composition --> Nano Banana Pro
- Budget/exploration --> Nano Banana 2 or GPT Image 2 `quality: low`

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/nano-banana.md

# Nano Banana — Specific Rules

Три тира. «Thinking» модели — понимают намерение, физику, композицию.

| Тир | Model ID | Роль |
|-----|----------|------|
| **NB2 Lite** | `gemini-3.1-flash-lite-image` | Самая быстрая и дешёвая ($0.034, ~4 сек), только 1K. Черновики, массовые батчи |
| **NB2** (Flash) | `gemini-3.1-flash-image` | Дефолтный workhorse: Pro-фичи (текст, 4K, grounding, консистентность) на скорости Flash |
| **NBP** (Pro) | `gemini-3-pro-image` | Топ-тир: сложные многослойные сцены, максимум reasoning и контроля |

## Стиль промпта

Натуральный язык, 1-2 параграфа. Структура свободная, но порядок помогает:
**Subject + Action + Location/context + Composition + Style**

```
A cinematic wide shot of a futuristic sports car speeding through a rainy
Tokyo street at night. Neon signs reflect off wet pavement and metallic
chassis. Format: 16:9.
```

## Что НЕ указывать

- Числовые параметры объектива: **50mm, 85mm, f/2.8, ISO 400** — NB игнорит. Используй описание: «shallow depth of field», «wide-angle distortion».
- Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.

## Уникальные возможности

### Image Grounding (NB2 only)
NB2 ищет реальные изображения в интернете до генерации. Архитектурно точные конкретные локации, корректные виды животных/растений.

```
Generate a cinematic, golden-hour photograph of [SPECIFIC REAL PLACE].
Ensure the architectural details, the spire, the surrounding square, and
the landscape are accurate to reality.
```

**Работает:** здания, мосты, площади, виды животных, виды растений, насекомые.
**Не работает:** конкретные люди.

### Extreme Aspect Ratios (NB2 only)

1:8, 8:1, 1:4, 4:1 — для баннеров, скроллов, комикс-стрипов.

```
Create a 4-panel horizontal comic strip (aspect ratio 4:1).
The story follows [CHARACTER] doing [ACTION] that ends with a twist.
Use a vibrant comic book style. Keep character design consistent.
```

Стандартные: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9.

### Thinking Mode

Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены платные). У NB2 есть рычаг `thinking_level: minimal | high` (default `minimal`) — поднимай до `high` для:
- Невнятных результатов, требующих reasoning
- Сложных инфографик со spatial logic
- Grounding + spatial reasoning одновременно

### Multi-Reference (лимиты по тирам)

| | NB2 Lite | NB2 | NBP |
|---|---|---|---|
| High-fidelity объекты | до 14 | до 10 | до 6 |
| Character-consistency рефы | нет | до 4 | до 5 |
| Style рефы | нет | нет | до 3 |

```
[Image 1: face]
[Image 2: outfit]
[Image 3: background]
Combine: face from Image 1, outfit style from Image 2, setting from Image 3.
Match lighting and perspective.
```

### JSON для сложных сцен (5+ элементов)

```json
{
  "subject": {"description": "main subject", "expression": "emotion/pose"},
  "photography": {"angle": "eye-level", "shot_type": "waist-up", "aspect_ratio": "16:9"},
  "background": {"setting": "location", "lighting": "soft natural"}
}
```

## Editing у Nano Banana

Conversational, без масок:

```
Remove [OBJECT] from this image.
Fill with [LOGICAL REPLACEMENT] matching surroundings.
Keep [PRESERVED ELEMENTS] exactly the same.
```

После генерации добавляй итеративно:
- «Make it warmer»
- «Increase contrast»
- «Soften background, add blur»
- «Change headline color to #3b82f6»

Interactions API держит контекст сессии — до 3 последовательных правок стэкаются без потери исходника. Правило «Edit, don't re-roll»: картинка верна на 80% — проси точечное изменение, а не новую генерацию.

## Text Rendering

- SOTA по 100+ языкам.
- Font можно называть: «Century Gothic 12px», «Brush Script», «Impact», «Heavy blocky sans-serif».
- Multi-language в одном кадре работает.
- Hack: для сложного текста — сначала попроси модель **написать текст**, потом отдельным промптом «вставь этот текст в картинку».

## Resolution / Cost

| Resolution | Использование |
|------------|---------------|
| 0.5K | Самая дешёвая, batch и А/B варианты |
| 1K | Default |
| 2K | Финальный отбор |
| 4K | Печать, hero-ассеты |

**Workflow:** прогон вариантов на `0.5K` flash (или NB2 Lite на 1K) → отбор → переген победителя на `2K`/`4K`.

В API `image_size` пишется строго с заглавной K (`1K`, `2K`, `4K`) — `1k` отклоняется. `512px` есть только у NB2; Lite — только 1K. Без указания размера модель матчит вход, иначе 1:1.

## Кейфреймы для видео

Nano Banana — image-слой перед motion-слоем. Всё критичное фиксируется на картинке ДО анимации: identity, композиция, aspect ratio, видимый текст, состояние продукта. Видеомодель усиливает любую неоднозначность стилла.

- **Character sheet / hero frame.** Утверди один кадр-эталон персонажа, на него ссылаются все последующие video-промпты.
- **Aspect ratio сразу целевой.** Кампании нужен вертикальный ролик — генери 9:16, а не кропай после анимации (тихая точка отказа).
- **Хэндофф в видеомодель — motion brief, не пересказ.** Движение камеры, движение субъекта, движение фона, длительность, framing lock, запрещённые изменения. Видео-промпт не переописывает то, что уже есть в кадре.
- Downstream любой: Veo 3.1, Kling 3.0, Seedance 2.0/2.5, Gemini Omni Flash (штатная пара Google, 10-сек клипы). Батч картинок → ревью-гейт → в видео уходят только одобренные стиллы.

## Известные фейлы

- Руки и лица всё ещё плывут (пальцы, суставы, дрейф likeness) — явные anatomy-инструкции + рефы + перегенерации. Есть отчёты, что NBP держит лица хуже NB2.
- Мелкий текст мылится на 1K — для плотного текста 2K+ или GPT Image 2.
- Инфографика может содержать фактически неверные данные — цифры проверять всегда, grounding помогает, но не гарантирует.
- Склонность к overcooked HDR / пересату — проси «natural contrast, no HDR look».
- SynthID-водяной знак стоит на всех генерациях (невидимый); на Vertex дополнительно C2PA.

## Когда переключаться NB2 → NBP

- NB2 не справляется со сложным многослойным промптом.
- Нужен максимум референсов с разбивкой по ролям (6 объектов + 5 character + 3 style).
- Photoreal с очень тонкой работой по материалам и свету.
- NBP медленнее и дороже; на лицах иногда проигрывает NB2 — для портретной серии сначала тестируй оба.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/patterns/character-design.md

# Character Design Patterns

Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}` for customization. Default model: GPT Image 2 (5-slot format) unless noted.

---

## Character Turnaround Sheet (3-View)

Use for game or animation pre-production — front, side, and back views of a character on a single white canvas with color callouts and height reference lines.

<!-- Source concept: character model sheet / turnaround sheet for 3D modelers and animators -->

```
Scene: clean white background, flat even lighting with no cast shadows, thin horizontal height reference lines in #CCCCCC spanning the full width at head, shoulder, waist, knee, and foot level
Subject: {character_name} — {character_description} — shown in three views arranged left to right: front view (facing camera), three-quarter side view (turned 75 degrees right), back view (facing away)
Important Details: all three views share identical proportions and vertical alignment along the height lines, feet on the same baseline, arms relaxed at sides for clear silhouette reading, color callout annotations — small circles of each key color ({color_1} {hex_1}, {color_2} {hex_2}, {color_3} {hex_3}) connected by thin #999999 leader lines to the corresponding material on the front view, fine line weight for height markers, clothing folds and seam lines consistent across all three angles
Use Case: game character pre-production, animation model sheet, 3D reference handoff
Constraints: no background elements, no props in hands, no dramatic poses — neutral standing pose only, all three views must depict the exact same character with identical outfit and proportions, no drop shadows, no gradient backgrounds
```

**Key levers:** `{character_name}`, `{character_description}` (age, build, hairstyle, outfit — be specific), `{color_1}`/`{hex_1}` through `{color_3}`/`{hex_3}` (key palette colors for callouts, e.g. jacket navy #1B2A4A, skin warm beige #D4A574, hair auburn #8B3A2F)

**Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering

---

## Expression Sheet

Use to produce a grid of 6–9 facial expressions for the same character — consistent head angle and art style, with emotion labels under each face.

<!-- Source concept: character expression/emotion reference sheet for animation or visual novel production -->

```
Scene: white background, 3x3 grid (or 3x2 for 6 expressions) with thin #DDDDDD divider lines, each cell contains one head-and-shoulders portrait
Subject: {character_name} — {character_description} — same head angle (three-quarter left), same hairstyle, same lighting across all cells
Important Details:
  Cell 1: neutral — relaxed brow, closed mouth, calm eyes. Label: "NEUTRAL"
  Cell 2: happy — genuine smile reaching the eyes, raised cheeks. Label: "HAPPY"
  Cell 3: angry — furrowed brow, clenched jaw, narrowed eyes. Label: "ANGRY"
  Cell 4: sad — downturned mouth, glistening eyes, slightly lowered head. Label: "SAD"
  Cell 5: surprised — wide eyes, raised eyebrows, open mouth. Label: "SURPRISED"
  Cell 6: disgusted — wrinkled nose, upper lip raised, squinted eyes. Label: "DISGUSTED"
  {extra_expressions}
  Labels in small {label_font} beneath each cell, #555555 text
  Consistent {art_style} rendering across all cells — skin tone, line weight, shading approach identical
Use Case: animation expression reference, visual novel sprite guide, game character documentation
Constraints: same character identity in every cell — no variation in hair, accessories, skin tone, or clothing between expressions, head angle stays fixed, no hand gestures, labels must be legible
```

**Key levers:** `{character_name}`, `{character_description}` (face shape, skin tone, hair, distinguishing marks), `{art_style}` (clean cel-shaded anime, painterly semi-realism, flat vector illustration), `{label_font}` (condensed sans-serif, monospace, rounded sans), `{extra_expressions}` (add cells 7-9: e.g. "Cell 7: smirk — one corner of mouth raised, knowing look. Label: 'SMIRK'")

**Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control

---

## Outfit Variant Grid

Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.

<!-- Source concept: character costume/skin variant sheet for fashion or game design -->

```
Scene: light neutral background ({bg_color}), {grid_layout} grid, thin white gaps between cells, soft even front lighting in every cell
Subject: {character_name} — {character_description} — same pose ({pose_description}) in every cell, only the outfit changes
Important Details:
  Cell 1: {outfit_1_name} — {outfit_1_description}
  Cell 2: {outfit_2_name} — {outfit_2_description}
  Cell 3: {outfit_3_name} — {outfit_3_description}
  Cell 4: {outfit_4_name} — {outfit_4_description}
  Cell 5: {outfit_5_name} — {outfit_5_description}
  Cell 6: {outfit_6_name} — {outfit_6_description}
  Outfit name in small bold sans-serif centered below each cell, #333333 text
  Character body proportions, face, hairstyle, and skin tone identical across all cells — only clothing and accessories differ
Use Case: game skin lineup, fashion mood board, costume design exploration
Constraints: same character identity and pose in every cell, no background scenery — character only, outfit labels must be readable, no overlapping garments between cells, {grid_layout} layout must be uniform
```

**Key levers:** `{character_name}`, `{character_description}` (build, face, hair — anchor identity), `{bg_color}` (#F0F0F0 light gray, #FFF8F0 warm cream, #E8EDF2 cool blue-gray), `{grid_layout}` (2x3 or 3x3), `{pose_description}` (hands on hips, relaxed standing, one hand raised), `{outfit_N_name}` / `{outfit_N_description}` (e.g. "Street Casual" — oversized denim jacket, white tee, black cargo pants, chunky sneakers)

**Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility

---

## Chibi / Mini-Me Collectible

Use to transform a realistic character into a cute 3D collectible figurine — oversized head, compact body, multiple poses performing different activities.

<!-- Source concept: chibi/super-deformed vinyl collectible figurine with consistent identity across poses -->

```
Scene: soft gradient background ({bg_gradient}), studio product lighting with rim light from behind and soft fill from front, subtle ground shadow beneath each figurine
Subject: chibi-style 3D collectible figurine of {character_name} — {character_description_simplified} — large head (roughly 1:2 head-to-body ratio), rounded limbs, smooth matte vinyl surface, {num_poses} poses arranged in a row
Important Details:
  Pose 1: {pose_1_description}
  Pose 2: {pose_2_description}
  Pose 3: {pose_3_description}
  {extra_poses}
  Face retains recognizable features from the original character — {face_markers} — simplified into the chibi style with large round eyes and small nose/mouth
  Outfit matches the original: {outfit_simplified} — colors preserved ({color_palette}), details reduced to clean shapes
  Each figurine sits on a small circular base ({base_color} matte finish)
  Vinyl toy aesthetic — visible seam line at sides, slight glossy highlight on forehead and cheeks
Use Case: merchandise concept, social media avatar set, fan collectible design
Constraints: consistent face and outfit across all poses, chibi proportions must stay uniform (no realistic proportions creeping in), no text on bases, smooth render — not cel-shaded, matte vinyl material throughout
```

**Key levers:** `{character_name}`, `{character_description_simplified}` (key outfit and hair only), `{face_markers}` (e.g. round glasses, scar on left cheek, green eyes), `{color_palette}` (hex values for 2-3 dominant colors), `{bg_gradient}` (#F5F0EB to #FFFFFF warm, #E0E8F0 to #FFFFFF cool), `{num_poses}` (3-5), `{pose_N_description}` (e.g. sitting cross-legged reading a book, waving with both hands, holding a coffee cup), `{base_color}` (white, black, matching character's main color)

**Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups

### Nano Banana version:

```
A row of {num_poses} chibi-style 3D vinyl collectible figurines of {character_name}, each in a different pose. Large head (1:2 head-to-body ratio), rounded limbs, smooth matte vinyl surface with visible seam lines and subtle glossy highlights on the forehead. Face retains {face_markers} simplified into chibi proportions with large round eyes. Outfit: {outfit_simplified} in {color_palette}. Poses left to right: {pose_1_description}, {pose_2_description}, {pose_3_description}. Each figurine on a small circular {base_color} matte base. Soft gradient background ({bg_gradient}), studio product lighting with rim light from behind and soft fill from front, subtle ground shadow. Format: 16:9.
```

---

## Anime-Style Character Card

Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional concept art layout.

<!-- Source concept: anime/game character reference sheet with stats, items, and palette swatches -->

```
Scene: white background, organized reference card layout divided into clear sections with thin #CCCCCC separator lines
Subject: {character_name} — {character_description} — anime-style rendering with clean line art and flat cel shading
Important Details:
  Left section (40% width): full-body standing pose, front-facing, arms slightly away from body to show full outfit, feet visible, confident neutral expression
  Upper-right section: portrait bust — head and shoulders, three-quarter angle, detailed face rendering showing {face_details}
  Mid-right section: {num_items} key items arranged in a row — {item_1}, {item_2}, {item_3} — each drawn at consistent scale with thin outline, labeled in small text below
  Lower-right section: color palette — {num_swatches} rectangular swatches in a horizontal strip showing the character's key colors ({swatch_colors}), hex code below each swatch
  Bottom strip: brief stat block or bio text in clean sans-serif — "Name: {character_name} | Class: {class} | Height: {height} | Affiliation: {affiliation}"
  Consistent line weight and shading style across all sections
Use Case: game character documentation, light novel illustration guide, animation production reference
Constraints: unified anime art style across all sections — portrait and full body must be the same character with identical design, items must match what the character wears/carries in the full body view, no decorative borders or ornamental frames, text must be legible at screen resolution
```

**Key levers:** `{character_name}`, `{character_description}` (detailed: hair color/style, eye color, outfit layers, accessories), `{face_details}` (distinctive facial features — e.g. heterochromia, facial tattoo, sharp jawline), `{item_1}`/`{item_2}`/`{item_3}` (signature weapon, accessory, artifact), `{swatch_colors}` (e.g. midnight blue #191970, cherry red #C41E3A, silver #C0C0C0, warm skin #E8B89D), `{num_swatches}` (4-6), `{class}` / `{height}` / `{affiliation}` (stat block fields)

**Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering

### Nano Banana version:

```
An anime-style character reference card for {character_name} on a white background. Left side: full-body standing pose, front-facing, clean cel-shaded anime rendering — {character_description}. Upper right: portrait bust at three-quarter angle showing {face_details}. Mid-right: key items laid out in a row — {item_1}, {item_2}, {item_3} — each drawn consistently and labeled. Lower right: horizontal color palette strip with {num_swatches} rectangular swatches ({swatch_colors}). Clean layout with thin gray separator lines between sections. Professional concept art quality, consistent line weight throughout. Format: 3:4.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/patterns/ecommerce.md

# E-Commerce Product Photography Patterns

Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Image 2 (5-slot format) unless noted.

---

## Miniature Diorama Product Ad

Use when you need a playful, attention-grabbing product visual where tiny workers interact with an oversized product — ideal for social media ads and launch campaigns.

<!-- Source concept: miniature/tilt-shift product advertising with construction-worker scale play -->

```
Scene: clean {surface_color} tabletop studio, soft overhead diffused light, shallow depth of field with tilt-shift blur at edges
Subject: oversized {product_name} centered in frame, surrounded by miniature construction workers (1/87 scale figurines) — some climbing the packaging with tiny ladders, others operating a miniature crane to lift the cap/lid, a crew painting the label
Important Details: {product_material} surface catches key light from upper left, visible condensation/texture on product, figurines cast tiny hard shadows, warm {accent_color} hard hats on workers, fine detail on miniature tools, slightly desaturated background, eye-level camera angle
Use Case: social media product ad, Instagram carousel hero
Constraints: no text, no logos other than product label, no floating elements, product must remain recognizable and unaltered, no more than 8 figurines
```

**Key levers:** `{product_name}`, `{product_material}` (frosted glass, matte aluminum, glossy plastic), `{surface_color}` (white marble, raw concrete, light birch wood), `{accent_color}` (safety orange #FF6600, yellow #FFD600)

**Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility

---

## Luxury Cosmetics Studio Shot

Use for premium beauty or fragrance product photography — dark, moody, tactile surfaces with atmospheric effects.

<!-- Source concept: luxury perfume/cosmetics dark-marble studio photography with condensation and smoke -->

```
Scene: dark studio, {background_surface} surface with subtle reflections, thin layer of low-hanging smoke drifting left to right, {time_mood} ambient
Subject: {product_name} bottle/tube centered, three-quarter angle, {product_finish} catching a single key light from upper right
Important Details: fine water droplets on product surface (condensation, not spray), {accent_material} accent elements flanking the product (raw stone, dried botanicals, metal shavings), volumetric haze behind product, reflection on surface below is soft and dark, color palette restricted to {palette}, contact shadow sharp near base fading to soft
Use Case: luxury brand campaign hero, print ad, website banner
Constraints: no text overlays, no human hands, background stays dark (#0a0a0a to #1a1a1a gradient), no color spill outside the defined palette, no lens flare
```

**Key levers:** `{background_surface}` (nero marquina marble, wet obsidian slab, brushed gunmetal), `{product_finish}` (frosted glass, lacquered black, brushed gold), `{accent_material}` (raw quartz crystals, dried lavender stems, black river stones), `{palette}` (golds #C9A84C and blacks, rose #B76E79 and creams, emerald #2D6A4F and silvers), `{time_mood}` (cold blue, warm amber)

**Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail

---

## 9-Panel TVC Storyboard Grid

> For a dark-themed variant with timestamps, see [multi-panel.md](../multi-panel.md#1-9-cell-grid-storyboard).

Use to present a product commercial shot breakdown in a single image — pitch decks, creative presentations, client approvals.

<!-- Source concept: 9-panel television commercial storyboard grid with numbered frames -->

```
Scene: white canvas background, clean 3x3 grid with thin #CCCCCC divider lines (2px), each cell represents one shot in a {duration}-second commercial
Subject: {product_name} commercial storyboard — each panel is a distinct camera setup
Important Details:
  Panel 1 (wide): establishing shot of {setting}, warm natural light, product not yet visible
  Panel 2 (medium): {protagonist} notices/discovers the product on {surface}
  Panel 3 (close-up): hand reaching for {product_name}, shallow depth of field
  Panel 4 (ECU): product detail — texture of {product_material}, label readable
  Panel 5 (medium): {protagonist} using/opening the product, genuine expression
  Panel 6 (reaction): close-up face, {emotion} expression, soft key light
  Panel 7 (wide): product in context of {lifestyle_scene}
  Panel 8 (beauty shot): product hero on {beauty_surface}, studio lighting
  Panel 9 (pack shot): product centered on white with "{tagline}" below in thin sans-serif, #333333
Use Case: creative pitch deck, storyboard for TVC production
Constraints: consistent character identity across all panels, no panel numbering text, uniform lighting temperature within the narrative (panels 1-7), distinct studio lighting for panels 8-9
```

**Key levers:** `{product_name}`, `{protagonist}` (woman in her 30s, young couple, family), `{setting}` (bright kitchen, outdoor terrace, urban cafe), `{emotion}` (satisfied, surprised, relaxed), `{beauty_surface}` (white marble, gradient gray), `{tagline}`, `{duration}` (15, 30)

**Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9

---

## Floating Ingredient Freeze-Frame

Use for food, beverage, or supplement products where suspended ingredients communicate freshness, flavor, or composition.

<!-- Source concept: frozen-motion ingredient explosion around product, high-speed photography aesthetic -->

```
Scene: {background_gradient} gradient backdrop, high-speed flash freeze-frame moment, clean studio environment
Subject: {product_name} container in center, tilted {tilt_angle} degrees, with {liquid_type} mid-pour arcing from the opening
Important Details: individual {ingredient_list} frozen in mid-air around the product — each element sharply focused with visible texture ({texture_details}), micro water droplets suspended alongside ingredients, single hard flash from behind (rim light on ingredients), secondary soft fill from front, liquid splash forms a clean arc with visible viscosity, product label faces camera and remains fully legible, ingredients distributed in a loose orbital pattern
Use Case: beverage packaging, food product poster, social media ad
Constraints: no ingredients overlapping the product label, no motion blur (everything frozen sharp), background must remain clean — no stray splashes hitting edges, no more than {max_ingredients} floating elements, no artificial glow effects
```

**Key levers:** `{product_name}`, `{background_gradient}` (#F5F0EB to #FFFFFF for light, #1A0A2E to #0D0D0D for dark), `{liquid_type}` (amber juice, white milk, green smoothie), `{ingredient_list}` (sliced strawberries + mint leaves + ice cubes, cocoa nibs + hazelnuts + vanilla pod), `{texture_details}` (visible seeds on strawberry cross-section, frost crystals on ice), `{tilt_angle}` (15, 25), `{max_ingredients}` (6-8)

**Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility

---

## Inflatable Surrealism Product Poster

Use for disruptive, scroll-stopping social ads where the product packaging appears squeezed, inflated, or physically distorted as if made of soft rubber or vinyl.

<!-- Source concept: inflatable surrealism — product packaging rendered as squeezed/puffy/distorted soft objects -->

```
Scene: solid {background_color} background, soft even studio lighting with no hard shadows, slightly elevated camera angle (15 degrees above eye level)
Subject: {product_name} packaging reimagined as a puffy inflatable vinyl object — the shape is recognizable but squeezed at the middle as if gripped by an invisible hand, seams visible where vinyl panels meet, surface slightly reflective like a pool float
Important Details: {product_color_scheme} preserved on the inflated surface but stretched and slightly warped around curves, visible air valve at the bottom edge (small brass circle), subtle wrinkles where the vinyl compresses, the brand name/logo distorted by the inflation but still readable, two or three {companion_objects} nearby also inflated (matching aesthetic), environment reflection on glossy vinyl surface, cast shadow soft and diffused below
Use Case: disruptive social media ad, brand campaign poster, billboard
Constraints: product must remain identifiable despite distortion, no liquid, no particles, no humans, no text outside what exists on the packaging, vinyl texture must read as physical (not digital 3D render), background is flat color only
```

**Key levers:** `{product_name}`, `{background_color}` (bubblegum pink #FFB6C1, electric blue #007BFF, acid yellow #E8FF00), `{product_color_scheme}`, `{companion_objects}` (matching accessories, ingredient items, brand mascot elements)

**Recommended model:** NBP — complex spatial reasoning for believable physical distortion

### Nano Banana version:

```
A product poster showing {product_name} packaging transformed into a puffy inflatable vinyl object, squeezed at the middle as if gripped by an invisible hand. The surface is slightly glossy like a pool float, with visible seams where vinyl panels meet and a small brass air valve at the base. The original {product_color_scheme} is preserved but stretched and warped around the inflated curves. Brand text is distorted by the shape but still legible. Two small {companion_objects} sit nearby, also inflated in the same vinyl style. Solid {background_color} background, soft even studio light, slightly elevated camera angle. Soft diffused shadow below. Format: 4:5.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/patterns/fashion-editorial.md

# Fashion Editorial Patterns

Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GPT Image 2 (5-slot format) unless noted.

---

## 3-Panel Campaign Collage

Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

<!-- Source concept: fashion campaign triptych collage — hero + detail + movement panels -->

```
Scene: three vertical panels side by side on a single canvas (left 40% width, right split into two stacked panels 60% height each), thin white divider lines (3px), cohesive {lighting_setup} across all panels
Subject: {model_description} wearing {outfit_description} — same person, same outfit, three perspectives
Important Details:
  Left panel (hero): full-body three-quarter pose, {model_description} standing against {background_1}, weight shifted to one hip, direct gaze at camera, medium-format film grain, {color_grade}
  Top-right panel (detail): extreme close-up of {detail_focus} — visible weave/stitching/texture of {fabric_type}, shallow depth of field, warm directional light raking across surface
  Bottom-right panel (action): mid-stride walking shot from low angle, {background_2}, coat/fabric in motion with natural drape physics, slight motion energy in hair
  Overall: cohesive warm/cool temperature of {color_temperature}, consistent skin tone rendering across panels, editorial magazine quality
Use Case: fashion brand campaign, lookbook cover, social media carousel hero
Constraints: same person with identical features in all three panels, no text, no logos, no visible studio equipment, panels must feel like one shoot not three separate photos, no heavy retouching glow
```

**Key levers:** `{model_description}` (East Asian woman mid-20s, athletic man early 30s), `{outfit_description}`, `{detail_focus}` (collar construction, cuff button, belt buckle, shoe sole), `{fabric_type}` (raw selvedge denim, double-faced cashmere, washed silk), `{background_1}` (concrete wall, sand dune, industrial corridor), `{background_2}` (open street, field, rooftop), `{color_grade}` (lifted blacks with amber cast, desaturated teal), `{color_temperature}` (warm 4000K feel, cool overcast daylight)

**Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail

---

## 2x2 Editorial Portrait Grid

Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.

<!-- Source concept: 2x2 fashion portrait grid — same model, four setups -->

```
Scene: 2x2 grid on white canvas, thin {divider_color} divider lines (2px), all four cells use the same {background_type} with slight variation in angle
Subject: {model_description}, same {outfit_description} in all four frames
Important Details:
  Top-left: straight-on headshot, neutral expression, eyes to camera, even butterfly lighting
  Top-right: three-quarter profile, chin slightly lifted, single key light from camera-left creating defined cheekbone shadow
  Bottom-left: full profile silhouette, rim light from behind outlining jaw and nose, {background_type} slightly darker
  Bottom-right: candid moment — mid-laugh or adjusting {accessory}, natural movement, softer light
  All frames: {film_stock} color science, consistent {skin_tone_handling}, no heavy skin smoothing — visible pores and natural texture, shallow depth of field in all four
Use Case: fashion editorial spread, model comp card, casting portfolio
Constraints: identical person in all four frames (bone structure, skin, hair must match exactly), no makeup changes between frames, no text, no watermarks, backgrounds must feel cohesive not random
```

**Key levers:** `{model_description}`, `{outfit_description}` (black turtleneck, white linen shirt unbuttoned at collar), `{background_type}` (seamless medium gray, textured plaster wall, out-of-focus greenery), `{divider_color}` (#FFFFFF, #E0E0E0), `{film_stock}` (Kodak Portra 400, Fujifilm Pro 400H), `{skin_tone_handling}` (warm undertones preserved, cool-neutral rendering), `{accessory}` (earring, collar, watch)

**Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames

---

## Streetwear Poster with Oversized Typography

Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.

<!-- Source concept: streetwear poster with model integrated into oversized typographic layout -->

```
Scene: solid {background_color} background, graphic poster composition, typography dominates 60% of visual space
Subject: {model_description} in {streetwear_outfit}, standing or crouching in a {pose_description}, positioned {model_position} — partially overlapping the text layers
Important Details: headline "{HEADLINE_TEXT}" in extra-bold condensed {font_style}, {text_color}, occupying upper two-thirds of frame — model breaks in front of some letters and behind others (depth interplay), secondary text "{SUBHEAD_TEXT}" in thin weight {subhead_color} near bottom edge, {lighting_type} on model creating {shadow_quality} shadows, grain overlay across entire image ({grain_intensity}), composition follows rule of thirds with model at {grid_position} intersection
Use Case: streetwear brand drop poster, social media announcement, lookbook cover
Constraints: text must be fully legible even where model overlaps, no extra text or watermarks, no decorative elements besides type and model, model does not obscure more than 30% of any single letter, "{HEADLINE_TEXT}" spelled exactly as provided
Quality: high
```

**Key levers:** `{HEADLINE_TEXT}` (brand name, drop name), `{SUBHEAD_TEXT}` (date, "LIMITED DROP", collection name), `{background_color}` (off-white #F5F1EB, concrete gray #8C8C8C, matte black #0D0D0D), `{text_color}` (#000000, #FF3333, #FFFFFF), `{font_style}` (sans-serif like Druk Wide, slab-serif, stencil), `{streetwear_outfit}`, `{model_position}` (center-left, right third), `{lighting_type}` (harsh direct flash, soft window light), `{grain_intensity}` (subtle film grain, heavy 35mm grain)

**Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay

---

## Retro Roller Skating Sportswear Campaign

Use for playful, nostalgic sportswear or athleisure campaigns with 70s-80s visual language.

<!-- Source concept: retro roller skating / sportswear campaign with analog film aesthetic -->

A sun-drenched wide shot of {model_description} roller skating along a {location_description}. They wear {outfit_description} — the fabric catches light as they move, one leg extended mid-glide, arms relaxed and swinging naturally. The ground is smooth asphalt with painted lane markings in faded {lane_color}. Background shows {background_elements} slightly out of focus through heat haze. Shot on {film_stock} with pronounced grain and slightly lifted shadows. Color palette centers on {palette_description}. Golden hour backlight creates a warm halo around the subject and long shadow stretching toward camera. Genuine movement energy — hair and loose fabric respond to speed. Format: {aspect_ratio}.

**Key levers:** `{model_description}`, `{outfit_description}` (high-waisted terry shorts in coral, cropped zip-up in cream, tube socks with racing stripes), `{location_description}` (Venice Beach boardwalk, empty suburban tennis court, coastal promenade), `{film_stock}` (Kodak Gold 200, Fuji Superia 400), `{palette_description}` (terracotta #CC5533, cream #FFF5E1, sky blue #87CEEB, mustard #D4A017), `{lane_color}` (faded yellow, sun-bleached white), `{background_elements}` (palm trees and pastel buildings, chain-link fence and bleachers), `{aspect_ratio}` (3:2, 16:9)

**Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding

---

## Futuristic Sportswear Editorial with 3D Blob Shapes

Use for forward-looking athletic or techwear editorials where abstract 3D forms create a surreal spatial environment around the model.

<!-- Source concept: futuristic sportswear editorial with organic 3D blob/sphere shapes -->

```
Scene: {studio_environment} studio space, matte {floor_color} floor extending to infinity, ambient fill light with no visible source, three to five large organic 3D blob shapes ({blob_color}, glossy smooth surface with environment reflections) floating at varying heights around the subject
Subject: {model_description} in {techwear_outfit}, posed in an athletic stance — {pose_detail}
Important Details: blobs range from basketball-sized to armchair-sized, each with smooth amoebic curves and a single specular highlight, they cast soft colored shadows onto the floor and the model's clothing, model lit by cool directional light from camera-right creating defined muscle/fabric contour, {fabric_detail} visible in the garment construction, one blob partially behind the model and one in front (spatial depth), color palette limited to {palette}, overall mood is clinical and aspirational
Use Case: sportswear lookbook, techwear campaign, editorial magazine spread
Constraints: blobs must look physically present (not composited), no text, no logos, no additional props, model remains the clear focal point despite the surrounding forms, blobs do not touch or intersect with the model's body, no motion blur
```

**Key levers:** `{studio_environment}` (white void, concrete gray, deep navy), `{floor_color}` (light gray #D0D0D0, charcoal #333333), `{blob_color}` (chrome silver, translucent jade #00A86B, matte coral #FF6B6B), `{techwear_outfit}` (bonded seam track pants + compression top, oversized windbreaker + utility shorts), `{pose_detail}` (low lunge position, standing with one arm extended checking a wrist device, mid-jump), `{fabric_detail}` (visible bonded seams, reflective piping, mesh ventilation panels), `{palette}` (monochrome + single accent, earth tones + neon green #39FF14)

**Recommended model:** NBP — complex spatial reasoning for blob placement and reflections

### Nano Banana version:

```
A futuristic sportswear editorial photograph in a {studio_environment} studio space with a matte {floor_color} floor extending to infinity. {model_description} stands in an athletic {pose_detail}, wearing {techwear_outfit} with {fabric_detail}. Three to five large organic 3D blob shapes in {blob_color} with glossy smooth surfaces float at varying heights around the subject — the largest is armchair-sized, the smallest basketball-sized. Each blob has amoebic curves and casts soft colored shadows onto the floor and the model's clothes. Cool directional light from camera-right defines contour and fabric texture. One blob sits partially behind the model, one in front, creating depth. The model is the clear focal point. No text, no logos. Format: 4:5.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/patterns/food-beverage.md

# Food & Beverage Patterns

Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Default model: GPT Image 2 (5-slot format) unless noted.

---

## Luxury Chocolate Brand Campaign

Use for premium chocolate or confectionery brand visuals — moody, textural, with controlled color and atmosphere. Adaptable across mood variants (dark indulgence, bright artisan, earthy origin-story).

<!-- Source concept: luxury chocolate brand campaign with variant moods and tactile surfaces -->

```
Scene: {surface_material} surface, {lighting_mood} lighting setup — {light_description}, thin atmospheric haze at background edge, color palette restricted to {palette}
Subject: {product_arrangement} — {product_count} pieces of {chocolate_type} arranged in {arrangement_style}
Important Details: visible snap edge on broken piece revealing {interior_texture}, fine cocoa powder dusted across surface (concentrated near product, fading to clean edges), {garnish_elements} placed deliberately as art direction not garnish, one piece mid-break with clean fracture line, surface texture of chocolate shows {surface_quality}, camera angle {camera_angle}, shallow depth of field with sharpest focus on the broken piece
Use Case: luxury chocolate brand campaign, print ad, packaging insert
Constraints: no human hands, no utensils, no wrappers or packaging visible, no text, cocoa dust must look natural not dumped, maximum {product_count} chocolate pieces, no melting

Mood variant — {mood_name}:
{mood_modifier}
```

**Key levers:**
- `{surface_material}` — dark slate, raw walnut wood, black marble, crumpled kraft paper
- `{lighting_mood}` — dramatic chiaroscuro / soft diffused warmth / cold window light
- `{light_description}` — single hard key from upper left / wrap-around softbox / backlit through parchment
- `{palette}` — deep browns #3E2723 + gold #C9A84C + black / warm terracotta #A0522D + cream #FFF8E7 / emerald #2D6A4F + copper #B87333
- `{chocolate_type}` — single-origin dark 72%, white chocolate with matcha veins, ruby chocolate
- `{interior_texture}` — smooth ganache center, crunchy praline layers, salted caramel pocket
- `{garnish_elements}` — single vanilla pod, fleur de sel crystals, edible gold leaf fragments, dried raspberry
- `{arrangement_style}` — diagonal cascade, tight cluster with negative space right, single row
- `{mood_name} / {mood_modifier}` — "Dark Indulgence": push contrast, deepen shadows, add smoke wisp / "Bright Artisan": overcast daylight, lifted blacks, pastel accent / "Origin Story": raw earth tones, burlap texture, raw cacao beans nearby

**Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision

---

## High-Fashion Beverage Campaign Board

Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.

<!-- Source concept: fashion-meets-beverage campaign board with model, hero product, and lineup -->

```
Scene: horizontal triptych layout on single canvas — left panel (45% width), center panel (30%), right panel (25%), thin {divider_color} dividers (2px), unified {color_temperature} color temperature
Subject: {beverage_brand} campaign board featuring {model_description} and {product_name}
Important Details:
  Left panel (lifestyle): {model_description} at {location}, holding {product_name} at {hold_position}, {model_action}, shot on {film_aesthetic} — environment tells the brand story
  Center panel (hero): {product_name} bottle/can beauty shot, {product_angle} angle, {product_surface} surface, single key light with {highlight_style}, condensation droplets on glass/can surface, label sharp and legible
  Right panel (lineup): {lineup_count} product variants arranged in a {lineup_arrangement}, same lighting as center panel but pulled back wider, each label variant distinguishable by color ({variant_colors})
  Typography: none in image
Use Case: brand campaign presentation, pitch deck, retail POS
Constraints: model does not look directly at product (natural interaction), product label consistent and legible in all panels, lighting temperature cohesive, no floating elements, condensation looks physical not painted on
```

**Key levers:** `{product_name}`, `{beverage_brand}`, `{model_description}`, `{location}` (sunlit rooftop bar, marble kitchen counter, poolside), `{hold_position}` (mid-sip, resting at hip, gesturing with it), `{model_action}` (laughing mid-conversation, looking off-frame, walking), `{film_aesthetic}` (warm Kodak Portra feel, clean digital, cold editorial), `{product_angle}` (three-quarter front, straight-on, slight low angle), `{product_surface}` (wet dark stone, frosted glass shelf, white marble), `{lineup_count}` (3-5), `{variant_colors}` (amber/ruby/gold, mint/lemon/berry), `{divider_color}` (#FFFFFF, #1A1A1A)

**Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency

---

## Hyper-Realistic Food Poster Template

Use for hero food posters — restaurants, delivery apps, menu boards — where the food is the entire composition with fillable content slots.

<!-- Source concept: hyper-realistic food poster with controlled composition slots -->

```
Scene: {background_treatment}, {atmosphere_effect}, overall tone {color_tone}
Subject: {dish_name} — {dish_description}, plated on {plate_description}, centered in frame
Important Details:
  Plating: {plating_details}
  Steam/moisture: {steam_detail}
  Garnish: {garnish_detail} placed at {garnish_position}
  Surface: {table_surface}, visible texture extending to frame edges
  Props: {prop_list} — arranged {prop_arrangement}
  Camera: overhead ({overhead_angle}) OR {camera_angle}, {lens_feel}
  Lighting: {food_lighting} — highlights on {highlight_targets}
Use Case: restaurant poster, delivery app hero, menu board, food magazine cover
Constraints: food must look freshly prepared (not cold or sat-out), no human hands or utensils in active use (props only), colors must be appetizing — no blue cast, no desaturated tones on the food itself, {plate_description} must not compete with the dish
```

**Key levers:**
- `{dish_name}` / `{dish_description}` — the hero food item described in appetizing physical detail
- `{plate_description}` — matte white ceramic, dark stoneware, rustic wooden board, banana leaf
- `{plating_details}` — sauce swoosh from 2 o'clock, microgreens at 10 o'clock, sesame seed scatter
- `{steam_detail}` — visible steam wisps rising from center, condensation on glass nearby, no steam
- `{garnish_detail}` — single basil sprig, chili flake scatter, citrus zest curls
- `{table_surface}` — aged oak, dark concrete, white marble with gray veins
- `{prop_list}` — linen napkin, vintage fork, small bowl of sauce, scattered herbs
- `{food_lighting}` — warm directional from upper-left with fill bounce, harsh noon daylight, moody side light
- `{background_treatment}` — dark vignette, clean bright, rustic blur
- `{camera_angle}` — 45-degree three-quarter, straight-on eye-level, overhead flat-lay

**Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity

---

## Naturalist Food Specimen Cross-Section

Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the style of 19th-century naturalist prints.

<!-- Source concept: Audubon-style naturalist botanical/food specimen illustration with cross-section -->

A detailed naturalist illustration of {food_item} rendered in the style of 19th-century scientific specimen plates. The composition shows the item in three states arranged vertically on an aged {paper_color} parchment background: whole specimen at top with botanical accuracy, lateral cross-section at center revealing internal structure ({internal_details}), and an exploded detail of {detail_element} at bottom with fine ink annotation lines pointing to key features. Drawn with precise {medium_description} — visible hatching for shadow, stippling for texture, thin ink outlines. Color is naturalistic but slightly muted as if from a hand-tinted lithograph. A thin decorative border frames the composition. Small italic Latin-style label "{latin_label}" at the bottom in serif font, {ink_color} ink. Format: 3:4.

**Key levers:** `{food_item}` (pomegranate, sourdough loaf, wagyu ribeye, cacao pod), `{internal_details}` (seed chambers with ruby arils, crumb structure with irregular air pockets, marbling fat distribution), `{detail_element}` (individual seed anatomy, crust layering, fat crystal structure), `{paper_color}` (warm cream #FDF5E6, cool ivory #FFFFF0), `{medium_description}` (watercolor wash with ink line, graphite with colored pencil, pure ink with minimal color), `{latin_label}` (a playful Latinized name), `{ink_color}` (sepia #704214, India black #1A1A1A)

**Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics

---

## City Food Map Illustration

Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties across a city.

<!-- Source concept: hand-drawn illustrated food map of a city with dish icons and landmarks -->

A hand-drawn illustrated bird's-eye map of {city_name} showing its food culture. The map covers the {area_description} with simplified but recognizable {landmark_list} drawn in a loose ink-and-watercolor style. Scattered across the map are {dish_count} illustrated food items representing local specialties — each dish ({dish_list}) drawn at exaggerated scale hovering near its neighborhood, rendered in warm appetizing watercolor with visible brushstrokes. Streets are thin ink lines with {street_style}. Water features rendered in soft {water_color} wash. The overall palette is {palette_description}. A decorative hand-lettered title "{MAP_TITLE}" sits in a banner at the top. Small hand-written labels mark each dish and neighborhood. Style references vintage travel poster illustration meets editorial food drawing. Format: {aspect_ratio}.

**Key levers:** `{city_name}`, `{area_description}` (central 5 km, old town quarter, waterfront district), `{landmark_list}` (main cathedral, central market, river bridges), `{dish_count}` (6-10), `{dish_list}` (plov near the bazaar, samsa near the old town, shashlik near the park), `{street_style}` (slightly wobbly freehand, clean but simplified), `{water_color}` (cerulean #0077B6, teal #2A9D8F), `{palette_description}` (warm terracotta and cream with food items in full saturated color, cool blues and greens with warm food accents), `{MAP_TITLE}` ("A Taster's Guide to {city_name}"), `{aspect_ratio}` (3:4, 1:1)

**Recommended model:** NB2 — image grounding for real city landmarks + illustration style

### Nano Banana version:

```
A hand-drawn illustrated bird's-eye food map of {city_name}, covering the {area_description}. Simplified but recognizable {landmark_list} are drawn in loose ink-and-watercolor style. {dish_count} local dishes ({dish_list}) float at exaggerated scale near their neighborhoods, each painted in warm appetizing watercolor with visible brushstrokes. Streets are thin freehand ink lines. Water features in soft {water_color} wash. A hand-lettered banner at top reads "{MAP_TITLE}". Small hand-written labels mark dishes and neighborhoods. Style mixes vintage travel poster illustration with editorial food drawing. Palette: {palette_description}. Format: {aspect_ratio}.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/patterns/portrait-cinema.md

# Portrait & Cinema Patterns

Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for customization. Default model: GPT Image 2 (5-slot format) unless noted.

---

## Golden Hour Street Backlit Portrait

Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.

<!-- Source concept: golden hour backlit street portrait with lens flare and warm atmospheric haze -->

```
Scene: {street_description} at golden hour, sun positioned directly behind subject (5-10 degrees above horizon line), warm amber light flooding the street, slight atmospheric haze diffusing the backlight
Subject: {person_description}, standing at {position_in_street}, body angled three-quarter to camera, face turned toward lens with {expression}
Important Details: strong rim light outlining hair and shoulders in warm gold (#FFAA33), face lit primarily by bounce light from {bounce_surface} on the opposite side — softer and cooler than the backlight, shallow depth of field rendering background into warm bokeh circles, {clothing_detail} catches backlight along edges showing fabric texture, visible lens flare — one or two hexagonal flare artifacts near frame edge (organic, not excessive), long shadow cast toward camera on {ground_surface}, skin rendered naturally with warm undertones — no heavy smoothing, visible pores, {color_grade}
Use Case: editorial portrait, personal brand photography, album art
Constraints: face must be visible and well-exposed despite backlight (not silhouetted), no reflectors or studio equipment visible, lens flare limited to one or two subtle artifacts — not a starburst explosion, no added text, no vignette
```

**Key levers:** `{street_description}` (narrow European alley with stone walls, wide boulevard with linden trees, industrial backstreet with brick), `{person_description}`, `{expression}` (quiet confidence, mid-smile with closed lips, contemplative gaze), `{bounce_surface}` (cream-painted wall, parked white van, sand-colored buildings), `{clothing_detail}` (linen shirt collar, leather jacket shoulder seam, scarf edge), `{ground_surface}` (wet cobblestones, dry asphalt, packed earth), `{color_grade}` (Kodak Portra 400 warmth, slightly lifted blacks with amber cast, clean digital with warm white balance)

**Recommended model:** GPT Image 2 — backlight exposure control and skin rendering

---

## Convenience Store Neon Portrait

Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subject's face.

<!-- Source concept: convenience store / bodega neon portrait — fluorescent + neon mixed light on face -->

```
Scene: exterior of a {store_type} at night, shot through or near the front window/entrance, overhead fluorescent tubes casting flat {fluorescent_color} light from inside, {neon_sign_description} mounted on the wall/window casting {neon_color} glow on one side of the subject's face
Subject: {person_description}, {pose_description}, positioned at the threshold between interior fluorescent zone and exterior neon zone — split lighting across the face
Important Details: face receives {fluorescent_color} fill from the store interior on one side and {neon_color} accent from signage on the other — the two colors mix on the nose bridge and chin, visible product shelves or cooler glow softly in background bokeh, {clothing_description} absorbs and reflects the two light sources differently, condensation or grime on window glass if shot through it (subtle, not obscuring), wet pavement outside reflects both light sources in streaks, shallow depth of field with subject sharp, background a mosaic of colored bokeh, {camera_feel}
Use Case: urban editorial, music press portrait, fashion story, short film still
Constraints: face clearly visible — neither light source blows out features, neon sign text (if present) is secondary to the portrait not the focal point, no additional light sources beyond what exists in the scene, no heavy color grading beyond what the practical lights create naturally, no motion blur
```

**Key levers:** `{store_type}` (Korean convenience store, bodega, late-night pharmacy, 24-hour laundromat), `{fluorescent_color}` (cool blue-white, greenish-white, warm tungsten), `{neon_sign_description}` (red "OPEN" sign, blue beer brand logo, pink cursive word), `{neon_color}` (red #FF2D2D, blue #3366FF, pink #FF69B4, green #39FF14), `{person_description}`, `{pose_description}` (leaning against door frame, sitting on overturned crate, standing with hands in pockets), `{clothing_description}` (dark hoodie that absorbs light, white t-shirt that bounces both colors, leather that reflects), `{camera_feel}` (Cinestill 800T with halation around neon, clean digital night, Fujifilm color science)

**Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin

---

## Monochrome Glitch Profile Portrait

Use for edgy, tech-forward portraits — artist profiles, electronic music press, tech brand campaigns. High contrast black-and-white with selective red digital artifacts.

<!-- Source concept: monochrome profile portrait with digital glitch artifacts and red accent color -->

```
Scene: pure black background (#000000), no environment — subject emerges from darkness
Subject: {person_description} in sharp profile (facing {direction}), head and upper shoulders only, high-contrast black-and-white rendering
Important Details: extreme contrast — skin highlights blow to near-white, shadows fall to pure black with minimal midtone graduation, {hair_detail} silhouetted against black, one eye visible in profile with a single catchlight, horizontal glitch displacement lines cutting across the image at {glitch_positions} — each line offsets a thin horizontal slice (4-8px) to the right by 10-20px, the displaced slices rendered in {accent_color} (#FF0000 default) while the rest remains monochrome, fine horizontal scan lines across entire image (subtle, CRT monitor texture), grain: heavy high-ISO film grain throughout, jaw line and nose bridge are the sharpest elements in frame
Use Case: artist press photo, electronic music EP cover, tech brand portrait, social media profile
Constraints: glitch lines must look digital (clean horizontal displacement, not organic), accent color appears ONLY in the displaced glitch slices — no other colored elements, maximum {max_glitch_lines} glitch lines to avoid visual noise, face must remain recognizable despite artifacts, no text, background is solid black — no gradient or texture
```

**Key levers:** `{person_description}`, `{direction}` (left, right), `{hair_detail}` (tight buzz cut showing skull contour, shoulder-length hair with flyaway strands catching backlight, pulled-back bun), `{glitch_positions}` (across the eye, across the mouth, across the forehead — specify 2-3 positions), `{accent_color}` (#FF0000 red, #00FF41 terminal green, #FF00FF magenta), `{max_glitch_lines}` (3-5)

**Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement

---

## Japanese Negative Film Rooftop Portrait

Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for editorial, zine, or personal project work.

<!-- Source concept: Japanese negative film aesthetic — overexposed, muted tones, rooftop setting -->

A waist-up portrait of {person_description} on a {rooftop_description}. They stand near the edge railing, {pose_description}, with the {city_skyline} visible behind them but washed out and desaturated by {sky_condition}. Shot on expired Japanese negative film — colors shifted toward {color_shift}, highlights blown soft and chalky, shadows lifted with visible grain in the flat midtones. Skin tones slightly green-yellow as if the film has aged. {clothing_description} reads as muted tones, almost monochromatic against the overexposed sky. Wind moves {wind_detail}. The mood is nostalgic and transient — a memory captured on deteriorating film stock. Eye-level framing, subject slightly off-center toward {frame_position}. Format: {aspect_ratio}.

**Key levers:** `{person_description}`, `{rooftop_description}` (concrete apartment building rooftop, industrial warehouse roof with exhaust vents, school building roof with chain-link fence), `{pose_description}` (leaning on railing looking at camera, turned away looking at skyline, sitting on a ledge with knees drawn up), `{city_skyline}` (Tokyo mid-rise apartments, generic Asian city with power lines), `{sky_condition}` (overcast white sky, hazy afternoon sun), `{color_shift}` (green-cyan cast, yellow-amber cast), `{clothing_description}` (oversized vintage windbreaker, plain white t-shirt, navy work jacket), `{wind_detail}` (hair across face, jacket hem, collar), `{frame_position}` (left third, right third), `{aspect_ratio}` (3:2, 4:5)

**Recommended model:** NB2 — analog film grain emulation and atmospheric mood

---

## Dreamy Underwater Surreal Portrait

Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elements.

<!-- Source concept: surreal underwater portrait with translucent fish and dreamy caustic light -->

```
Scene: clear {water_color} water filling the entire frame, caustic light patterns rippling across the subject from above (sunlight through water surface), no visible pool walls or floor — infinite aquatic void
Subject: {person_description}, floating in a relaxed {pose_description}, eyes {eye_state}, hair fanning out in all directions as if weightless, {clothing_description} billowing and suspended in the water
Important Details: {fish_count} translucent {fish_type} swimming in a loose school around the subject — each fish semi-transparent with visible skeletal structure and iridescent scales catching the caustic light, light rays penetrating from above in {light_pattern}, fine air bubbles rising from near the subject's {bubble_source}, fabric of clothing moves independently from the body — folds and hems suspended in mid-drift, skin has a subtle cool {water_tint} cast from the water, overall palette is {palette}, composition framed as a {shot_type}
Use Case: beauty campaign, album cover, conceptual art print, fashion editorial
Constraints: subject's face must be clearly visible and serene (not distressed or holding breath with effort), fish are translucent — not solid opaque tropical fish, no visible water surface edge or pool tiles, no scuba gear or goggles, bubbles are small and delicate not large air pockets, underwater physics must be consistent (everything floats)
```

**Key levers:** `{water_color}` (deep cerulean #0077B6, pale turquoise #AFEEEE, dark teal #004D4D), `{person_description}`, `{pose_description}` (arms slightly outstretched like a slow free-fall, curled fetal position, one arm reaching upward toward the light), `{eye_state}` (softly closed, open and gazing upward at the light, looking directly at camera), `{clothing_description}` (flowing white silk dress, loose linen shirt and trousers, sheer organza wrap), `{fish_count}` (5-8), `{fish_type}` (jellyfish, small reef fish, elongated glass catfish), `{light_pattern}` (parallel god rays from upper right, scattered dappled caustics, single concentrated beam), `{bubble_source}` (lips, fingertips, fabric edges), `{water_tint}` (blue-green, aquamarine), `{palette}` (teal and ivory, deep blue and gold, seafoam and blush), `{shot_type}` (full body vertical, waist-up centered, three-quarter with negative space below)

**Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)

### Nano Banana version:

```
A surreal underwater portrait of {person_description} floating in a relaxed {pose_description} in clear {water_color} water. Eyes {eye_state}, hair fans out weightlessly in all directions. {clothing_description} billows and suspends in the current, folds drifting independently. {fish_count} translucent {fish_type} swim in a loose school around the subject — each semi-transparent with visible skeletal structure and iridescent scales catching caustic light from above. Sunlight penetrates from the surface in {light_pattern}, casting rippling patterns across skin and fabric. Fine air bubbles rise from the subject's {bubble_source}. Skin has a subtle cool {water_tint} cast. No pool walls, no surface edge visible — infinite aquatic void. Serene and dreamlike. Palette: {palette}. Format: 4:5.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/patterns/poster-illustration.md

# Poster & Illustration Patterns

Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. Default model: GPT Image 2 (5-slot format) unless noted.

---

## City Across Two Centuries (Time-Split Composition)

Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, one half historical and one half modern.

<!-- Source concept: time-split composition — same city view, two eras side by side -->

```
Scene: wide establishing shot of {city_landmark_view}, frame divided vertically down the center — left half shows the scene in {historical_era}, right half shows {modern_era}
Subject: the same geographic viewpoint across two time periods, architecture and infrastructure transforming at the dividing line
Important Details:
  Left half ({historical_era}): {historical_details} — muted {historical_palette} palette, {historical_atmosphere}, period-accurate architecture, {historical_figures} going about daily life, {historical_transport}
  Right half ({modern_era}): {modern_details} — {modern_palette} palette, {modern_atmosphere}, contemporary architecture where old buildings once stood (some landmarks preserved), {modern_figures}, {modern_transport}
  Dividing line: not a hard cut — elements morph and blend across a narrow 5% transition zone (a horse-drawn cart becomes a car, a gas lamp becomes LED, cobblestones become asphalt, a tree grows taller)
  Sky transitions too: {historical_sky} on left to {modern_sky} on right
  Camera angle: elevated three-quarter view (roughly 30 degrees above street level) to show depth of both eras
Use Case: city anniversary campaign, urban development feature, cultural exhibition poster, editorial illustration
Constraints: both halves must depict the SAME geographic location (matching terrain, river, hill positions), transition zone should feel organic not pasted, scale and perspective consistent across both halves, no text unless specified, no anachronistic elements (modern items in historical half or vice versa outside the transition)
```

**Key levers:** `{city_landmark_view}` (view down the main avenue toward the central square, riverfront panorama, view from the hill overlooking the old town), `{historical_era}` / `{modern_era}` (1920s / 2020s, medieval / present day, 1960s / 2060s), `{historical_details}` (cobblestone streets, horse-drawn carts, hand-painted shop signs), `{modern_details}` (glass facades, rooftop gardens, digital signage), `{historical_palette}` (sepia and desaturated earth tones, hand-colored photograph quality), `{modern_palette}` (clean contemporary color, cooler blue-grays with warm accent), `{historical_atmosphere}` (coal haze, soft morning fog), `{modern_atmosphere}` (clear sky, light pollution glow at horizon), `{historical_sky}` (warm overcast), `{modern_sky}` (clear gradient blue)

**Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency

### Nano Banana version:

```
A wide elevated view of {city_landmark_view}, divided vertically down the center into two eras. The left half depicts the scene in {historical_era}: {historical_details}, rendered in a muted {historical_palette} palette with {historical_atmosphere}. The right half shows {modern_era}: {modern_details} in a {modern_palette} palette under {modern_atmosphere}. At the center dividing line, elements morph organically across a narrow transition zone — a horse-drawn cart becomes a car, gas lamps become LED lights, cobblestones blend into asphalt, trees grow taller. The sky transitions from {historical_sky} on the left to {modern_sky} on the right. Both halves share the same geographic terrain and perspective. Camera angle roughly 30 degrees above street level. Format: 16:9.
```

---

## Fitness Boxing Campaign Collage

Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.

<!-- Source concept: 3-panel fitness/boxing campaign collage with action and detail shots -->

```
Scene: three-panel horizontal collage on {canvas_color} canvas — left panel (35%), center panel (40%), right panel (25%), {divider_style} dividers, unified {overall_tone} color tone
Subject: {athlete_description} in a boxing/training context — same person across all panels
Important Details:
  Left panel (environment): wide shot of {gym_environment}, atmospheric — {atmosphere_detail}, equipment visible but out of focus, {athlete_description} as a silhouette or distant figure warming up, mood: anticipation
  Center panel (action): medium shot, {athlete_description} mid-{action_type}, captured at peak effort — {action_detail}, sweat visible on skin and {gear_description}, sharp focus on face showing {expression}, directional hard light from {light_direction} creating dramatic shadow on the opposite side of the face, slight motion trail on the {moving_element}
  Right panel (detail): extreme close-up of {detail_subject} — {detail_description}, texture dominates the frame, {detail_lighting}
  Grain: uniform {grain_level} across all panels
  Color: {color_treatment}
Use Case: fitness brand campaign, gym poster, sportswear ad, magazine editorial spread
Constraints: same athlete across all panels (consistent identity, gear, wraps), no text or logos, no sponsor branding, center panel is the visual anchor — should feel like the decisive moment, grain must be uniform not just added to one panel
```

**Key levers:** `{athlete_description}`, `{gym_environment}` (industrial boxing gym with heavy bags, outdoor concrete training yard, dimly lit basement ring), `{atmosphere_detail}` (chalk dust in backlight, steam from breath in cold air, golden light through high windows), `{action_type}` (throwing a cross, landing a hook on a heavy bag, rope-skipping), `{action_detail}` (fist connecting with bag creating visible impact ripple, rope frozen in arc above head), `{gear_description}` (red hand wraps, worn leather gloves, no gloves — taped knuckles), `{expression}` (focused intensity, controlled exhale, battle cry), `{detail_subject}` (taped knuckles against red canvas, worn boxing boot laces, sweat dripping from chin onto canvas), `{detail_description}` (each tape fiber visible, leather cracking at flex points, individual droplets mid-fall), `{color_treatment}` (desaturated with warm midtones, high-contrast monochrome with sepia, teal-and-orange split tone), `{canvas_color}` (matte black #0D0D0D, dark charcoal #1A1A1A), `{divider_style}` (thin white 2px, no dividers — edge bleed)

**Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail

---

## Lavender Smartphone Hero Ad

Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient with soft 3D accent elements.

<!-- Source concept: smartphone product launch hero in monochromatic lavender with floating accent shapes -->

```
Scene: smooth gradient background from {color_light} to {color_dark}, no hard edges, studio void environment
Subject: {device_name} floating at slight {tilt_angle}-degree angle, screen facing camera showing {screen_content}, centered vertically but offset {horizontal_position} horizontally
Important Details: device renders with physically accurate {device_finish} — visible edge chamfer catching a thin highlight line, screen content crisp and legible at this scale, {accent_element_count} soft 3D shapes floating nearby (matte {accent_shape_color} {accent_shapes} — frosted glass or soft plastic appearance, each {accent_size}), shapes are out of focus at varying depths creating a layered composition, soft omnidirectional lighting with a subtle key from upper-left, gentle device shadow projected onto the gradient ({shadow_softness}), overall color palette stays within the {color_family} family — no complementary or clashing tones
  Bottom text area: "{HEADLINE}" in {headline_weight} {headline_font_style}, {headline_color}, centered below device
  Subtext: "{SUBHEADLINE}" in thin weight, {subtext_color}, below headline
Use Case: product launch hero, website header, retail POS, digital ad
Constraints: screen content must be sharp and readable, floating shapes must not obscure the device screen, no reflections of a studio environment on screen, gradient is smooth — no banding, device proportions must match a real smartphone (no stretched or squished body), text exactly as quoted
Quality: high
```

**Key levers:** `{device_name}`, `{color_light}` / `{color_dark}` (lavender #E6D5F5 to #7B4FA0, mint #D0F0E0 to #1B7A5A, coral #FFDDD2 to #C44536), `{device_finish}` (matte aluminum, polished titanium, frosted glass back), `{screen_content}` (a clean home screen with app icons, a camera app showing a landscape, a gradient wallpaper), `{accent_shapes}` (spheres, rounded pills, soft cubes, torus rings), `{accent_shape_color}` — same family as background but slightly lighter or more saturated, `{accent_size}` (golf-ball to grapefruit), `{HEADLINE}` / `{SUBHEADLINE}`, `{headline_color}` (white #FFFFFF, dark tint of the color family), `{color_family}` (lavender-purple, sage-green, warm terracotta), `{tilt_angle}` (5-15), `{horizontal_position}` (left third, center, right third)

**Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy

---

## Emerald Street Fashion Poster

Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight on a saturated color field.

<!-- Source concept: bold emerald fashion poster with oversized type and street style figure -->

```
Scene: solid {background_color} background (flat, no gradient), graphic poster composition split between typography (upper 55%) and figure (lower 60%, overlapping into the type zone)
Subject: {model_description} in {outfit_description}, full-body shot from low angle (worm's eye, approximately 15 degrees below eye level), standing with {pose_description}
Important Details: "{MAIN_TITLE}" in extra-bold extended {title_font_style}, {title_color}, filling the upper half — each letter approximately 20% of frame height, model's head and shoulders break in front of the bottom row of letters (depth layering), "{SUBTITLE}" in lightweight condensed type, {subtitle_color}, running along the bottom edge or lower-right corner, model lit by overcast flat light — even exposure, minimal shadow, fabric textures fully readable ({fabric_details}), shoes visible and grounded (not floating), {graphic_accents} if any
Use Case: fashion brand poster, event flyer, editorial magazine cover, retail window display
Constraints: title text fully legible — model overlap must not obscure more than one letter by more than 40%, no additional decorative elements unless specified in {graphic_accents}, background is flat solid color — no texture or pattern, "{MAIN_TITLE}" and "{SUBTITLE}" spelled exactly as given, model does not hold props unless specified
Quality: high
```

**Key levers:** `{background_color}` (emerald #006B3F, cobalt #0047AB, saffron #F4C430, hot pink #FF1493), `{model_description}`, `{outfit_description}` (oversized leather trench + chunky sneakers, cropped bomber + wide-leg trousers + platform boots), `{pose_description}` (wide stance with arms crossed, one hand adjusting collar, walking stride caught mid-step), `{MAIN_TITLE}` / `{SUBTITLE}`, `{title_font_style}` (geometric sans-serif, grotesque, stencil cut), `{title_color}` (#FFFFFF, #000000, cream #FFF5E1), `{subtitle_color}` (same as title but at 60% opacity), `{fabric_details}` (visible grain in leather, corduroy ridges, denim selvedge edge), `{graphic_accents}` (none, thin white border 20px from edge, small logo mark at bottom-left)

**Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering

---

## Peacock Botanical Vintage Art Print

Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical elements in a vintage printmaking style.

<!-- Source concept: peacock botanical vintage symmetrical art print — ornamental and decorative -->

A symmetrical ornamental art print centered on a {peacock_variant} peacock in full tail display, viewed from {view_angle}. The tail feathers fan into a perfect semicircle filling the upper two-thirds of the frame, each eye-spot rendered with precise detail — iridescent {eye_colors} with fine barb texture. The peacock stands on a {base_element} at the composition's center axis. Flanking the bird symmetrically: {botanical_left} on the left mirrored by {botanical_right} on the right — leaves, stems, and blossoms curve inward framing the peacock. {additional_fauna} perch or fly near the upper corners. The entire composition sits on a {background_texture} background in {background_color}. Rendering style: {print_style} — visible {technique_marks}, rich but slightly flattened color as if from layered printing passes. Border: {border_style}. Color palette: {palette}. Format: 3:4.

**Key levers:** `{peacock_variant}` (Indian blue, white albino, green Java), `{view_angle}` (front-facing straight on, three-quarter turning left), `{eye_colors}` (deep blue #003366 and emerald #006B3F and gold #C9A84C, monochrome — all in shades of navy and silver), `{base_element}` (ornate stone pedestal, flowering branch, decorative tile floor), `{botanical_left}` / `{botanical_right}` (magnolia branches, trailing wisteria, passion flower vines, banksia stems), `{additional_fauna}` (two small butterflies, a dragonfly pair, none), `{background_texture}` / `{background_color}` (aged linen #F5F0E1, dark navy #0A1628, cream parchment #FDF5E6), `{print_style}` (hand-colored etching, woodblock print, chromolithograph), `{technique_marks}` (cross-hatching in shadows, visible plate tone, registration marks at corners), `{border_style}` (thin double-line art nouveau border, ornamental corner flourishes, simple single-line rectangle), `{palette}` (natural jewel tones — emerald, sapphire, gold on cream / limited three-color palette — teal, copper, black on ivory / muted earth tones — sage, terracotta, umber)

**Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species

### Nano Banana version:

```
A symmetrical ornamental art print centered on a {peacock_variant} peacock in full tail display, viewed {view_angle}. Tail feathers fan into a perfect semicircle filling the upper two-thirds, each eye-spot rendered with iridescent {eye_colors} and fine barb texture. The peacock stands on a {base_element}. Flanking it symmetrically: {botanical_left} on the left mirrored by {botanical_right} on the right, stems and blossoms curving inward to frame the bird. {additional_fauna} near the upper corners. Background: {background_texture} in {background_color}. Style: {print_style} with visible {technique_marks} and slightly flattened color as from layered printing passes. Border: {border_style}. Palette: {palette}. Format: 3:4.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/patterns/ui-social.md

# UI Mockups & Social Media Patterns

Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for customization. Default model: GPT Image 2 (5-slot format) unless noted.

---

## Instagram Story Ad (9:16)

Use for vertical product or brand ads targeting Instagram Stories — hero product, bold headline, and swipe-up CTA zone at the bottom.

<!-- Source concept: Instagram Story ad with glassmorphism elements and gradient background -->

```
Scene: vertical 9:16 canvas, smooth gradient background from {gradient_top} to {gradient_bottom}, soft ambient glow behind the product
Subject: {product_name} — {product_description} — centered in the upper two-thirds of the frame, angled slightly for dimension
Important Details: two glassmorphism panels (frosted translucent white, 20% opacity, subtle border highlight at #FFFFFF30) flanking the product — one floating left, one floating right, slightly rotated, adding depth layers. Bold headline "{headline_text}" in {headline_font} at the top third, white or light-colored text with subtle drop shadow for readability. Small subtext "{subtext}" below the headline in lighter weight. Bottom 15% of canvas left as swipe-up CTA zone — thin upward-pointing chevron icon and "{cta_text}" in small caps, both in white. Product casts a soft colored shadow matching the gradient onto the background. Scattered {accent_elements} (glass spheres, soft bokeh circles, translucent geometric shapes) at 10-15% opacity for texture.
Use Case: Instagram Story ad, vertical social media placement, mobile-first brand campaign
Constraints: text must be legible on mobile screens (minimum visual weight), no text in the bottom 5% (system UI overlap zone), product must be the clear focal point, no more than 3 accent elements, glassmorphism panels must not obscure the product
```

**Key levers:** `{product_name}`, `{product_description}` (shape, material, color), `{gradient_top}` / `{gradient_bottom}` (e.g. #6C3CE1 violet to #1A1A2E dark navy, #FF6B6B coral to #FFE66D warm yellow), `{headline_text}`, `{headline_font}` (bold condensed sans-serif, rounded geometric), `{subtext}`, `{cta_text}` (e.g. "Swipe Up", "Shop Now", "Learn More"), `{accent_elements}` (translucent spheres, soft light flares, floating geometric shards)

**Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision

---

## Social Media Feed Post (1:1)

Use for square-format posts on Instagram or Facebook — quote cards, feature announcements, or product highlights with centered layout.

<!-- Source concept: square social media post with brand color palette and centered typography -->

```
Scene: square 1:1 canvas, solid or subtle textured background in {bg_color}, clean centered composition
Subject: {post_type} — {content_description}
Important Details:
  Background: {bg_treatment} (solid color, subtle noise texture at 3% opacity, or soft radial gradient from {bg_color} center to slightly darker edges)
  Primary text: "{primary_text}" in {primary_font}, {text_color}, centered horizontally, positioned in the upper half with comfortable margins (at least 10% padding from edges)
  Supporting element: {supporting_element} — positioned below the primary text, providing visual weight and context
  Brand strip: thin horizontal line or subtle divider in {accent_color} separating the primary content from a bottom section containing "{brand_name}" in small caps and {brand_mark} (logo mark or wordmark)
  Overall palette restricted to {palette} — no colors outside this set
  Text sized for legibility at phone-screen scale — primary text large enough to read in a thumbnail feed scroll
Use Case: Instagram feed post, Facebook post, LinkedIn visual, social media content calendar
Constraints: all text must remain legible at 320px display width, no decorative elements that compete with the message, centered balanced layout, no more than two type sizes (headline + body or headline + brand), background must not reduce text contrast below WCAG AA
```

**Key levers:** `{post_type}` (quote card, product feature, announcement, stat highlight), `{content_description}`, `{primary_text}`, `{primary_font}` (geometric sans-serif, modern serif, handwritten accent), `{text_color}` (#FFFFFF on dark, #1A1A1A on light), `{bg_color}` / `{bg_treatment}`, `{accent_color}`, `{brand_name}`, `{brand_mark}`, `{palette}` (e.g. navy #1B2A4A, gold #C9A84C, white #FFFFFF), `{supporting_element}` (product photo, icon illustration, data number in large type)

**Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical

---

## App Store Screenshot

Use to create a polished App Store or Google Play listing screenshot — device frame with app UI inside, feature headline, and clean gradient background.

<!-- Source concept: App Store marketing screenshot with iPhone device frame and feature callout -->

```
Scene: vertical canvas, smooth gradient background from {gradient_top} to {gradient_bottom}, centered composition
Subject: {device_type} device frame displaying {app_name} UI — {screen_description}
Important Details:
  Device: realistic {device_type} bezel (space black / silver / natural titanium) with accurate corner radius and button placement, screen showing {screen_content} with proper iOS/Android status bar at top
  Headline: "{feature_headline}" in bold {headline_font}, positioned {headline_position} the device frame, {headline_color} text, 2-3 words maximum per line for impact
  Optional subheadline: "{subheadline}" in lighter weight below the headline, 60% opacity of headline color
  Device shadow: soft diffused shadow below the device, matching the gradient color (not pure black)
  Screen UI: {ui_description} — realistic interface elements with proper spacing, {ui_style} design system, readable text within the screen (even if small)
  Device centered vertically with equal breathing room above and below
Use Case: App Store product page, Google Play listing, app marketing material
Constraints: device bezel must look physically accurate (not a flat rectangle), screen content must be realistic and internally consistent UI (not random shapes), headline text must not overlap the device, gradient background only — no patterns or photos behind the device, one device only
```

**Key levers:** `{device_type}` (iPhone 16 Pro, Pixel 9, Galaxy S25), `{app_name}`, `{screen_description}` (brief: what the screen shows), `{screen_content}` / `{ui_description}` (detailed: specific UI elements visible), `{ui_style}` (iOS native, Material 3, custom dark theme), `{feature_headline}`, `{headline_font}` (SF Pro Display, condensed geometric), `{headline_position}` (above, below), `{headline_color}`, `{subheadline}`, `{gradient_top}` / `{gradient_bottom}` (e.g. #1A1A2E to #0D0D1A for dark, #F0F4FF to #FFFFFF for light)

**Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality

---

## Dashboard Design Mockup

Use for realistic analytics dashboard mockups — dark or light theme with data visualizations, KPI cards, and sidebar navigation.

<!-- Source concept: analytics dashboard UI mockup with charts, cards, and navigation -->

```
Scene: full-screen desktop UI mockup, {theme_mode} theme, clean {design_system} design system
Subject: {dashboard_title} — analytics dashboard showing {data_domain} metrics
Important Details:
  Sidebar (left, 220px visual width): dark ({sidebar_bg}) vertical navigation with icon + label pairs for {nav_items}, active item highlighted with {accent_color} left border and slightly lighter background, collapsed user avatar and app logo at top
  Top bar: breadcrumb or page title "{page_title}" in medium weight, date range selector showing "{date_range}", notification bell icon with dot indicator
  KPI row (top of main area): {num_kpis} metric cards in a horizontal row — each card shows metric name in small caps, large number value, and a small trend indicator (green upward arrow or red downward arrow with percentage), card background {card_bg}
  Chart area (main): {chart_layout}
    Chart 1: {chart_1_type} showing {chart_1_data} — using {chart_1_colors}
    Chart 2: {chart_2_type} showing {chart_2_data} — using {chart_2_colors}
  Secondary section: {secondary_widget} (data table with alternating row colors, recent activity feed, or geographic heat map)
  Proper visual hierarchy — KPI numbers largest, chart labels smaller, navigation text smallest
  Realistic data values throughout — no placeholder "lorem ipsum" or obviously fake numbers
Use Case: SaaS product marketing, investor deck, UI/UX portfolio, feature specification
Constraints: data must look plausible (proper scales, reasonable percentages, formatted numbers), charts must use proper axes and labels, no overlapping UI elements, sidebar must not bleed into main content, {theme_mode} theme applied consistently — no mixing dark sidebar with light charts unless intentional
```

**Key levers:** `{theme_mode}` (dark / light), `{design_system}` (minimal flat, glassmorphism cards, shadowed Material), `{dashboard_title}`, `{data_domain}` (SaaS revenue, e-commerce orders, marketing campaign, IoT sensor monitoring), `{sidebar_bg}` (#0F1117 dark, #FFFFFF light), `{accent_color}` (#6366F1 indigo, #10B981 emerald, #F59E0B amber), `{nav_items}` (Dashboard, Analytics, Users, Settings, Reports), `{num_kpis}` (3-5), `{chart_1_type}` / `{chart_2_type}` (line chart, grouped bar chart, donut chart, area chart), `{chart_1_colors}` / `{chart_2_colors}` (hex values), `{card_bg}` (#1E1E2E dark card, #FFFFFF light card), `{secondary_widget}`

**Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements require high fidelity

### Nano Banana version:

```
A {theme_mode}-themed analytics dashboard UI mockup for {dashboard_title}. Left sidebar ({sidebar_bg}) with navigation icons for {nav_items}, active item highlighted in {accent_color}. Top area: {num_kpis} KPI metric cards showing large numbers with trend arrows. Main area: {chart_1_type} visualizing {chart_1_data} in {chart_1_colors}, alongside a {chart_2_type} showing {chart_2_data}. Below: {secondary_widget}. Clean {design_system} design system, realistic plausible data values throughout, proper visual hierarchy. Desktop fullscreen layout. Format: 16:9.
```

---

## Personal Color Analysis Board

Use to create a visual color analysis graphic from a portrait — seasonal palette classification, clothing color comparisons, and accessory recommendations in an organized layout.

<!-- Source concept: personal color analysis / seasonal color palette board with side-by-side comparisons -->

```
Scene: white background, organized multi-section layout with thin #E0E0E0 divider lines, clean editorial formatting
Subject: personal color analysis board for {subject_description}
Important Details:
  Section 1 — Portrait & Season (top, full width): {subject_description} portrait photo (head and shoulders, natural lighting, neutral expression) on the left. To the right: season classification "{season_type}" in medium bold text, with a 4x3 grid of small color swatches showing the {num_palette} best colors for this season type ({palette_colors}), each swatch labeled with its name in tiny text below
  Section 2 — Clothing Comparison (middle): two side-by-side panels. Left panel "{good_label}": the subject wearing a top in {flattering_color} — skin looks healthy, face appears lifted and bright. Right panel "{bad_label}": the same subject wearing a top in {unflattering_color} — skin appears washed out or sallow. Small caption under each explaining the effect in 5-8 words
  Section 3 — Recommendations (bottom): horizontal strip with {num_recs} small squares — each showing a recommended item ({rec_items}) in one of the palette colors, with a one-word label below (e.g. "Scarf", "Blazer", "Lipstick", "Frames")
  Visual-first design — images and swatches dominate, text is short labels only
  Clean editorial feel, no decorative flourishes
Use Case: personal styling consultation, color analysis service deliverable, fashion content
Constraints: same person in all panels showing the subject, swatches must be solid flat color (no gradients), labels are short (1-3 words max), no paragraphs of body text, layout must feel organized and scannable, no overlapping sections
```

**Key levers:** `{subject_description}` (age, skin tone, hair color, eye color — needed for accurate seasonal analysis), `{season_type}` (Warm Spring, Cool Summer, Warm Autumn, Cool Winter — or sub-seasons like Soft Autumn, Bright Winter), `{palette_colors}` (12 hex values matching the season, e.g. Warm Autumn: rust #B7410E, olive #708238, mustard #E1AD01, burgundy #722F37...), `{num_palette}` (12), `{flattering_color}` / `{unflattering_color}` (specific colors with hex), `{good_label}` / `{bad_label}` (e.g. "Warm Coral" / "Cool Pink"), `{num_recs}` (4-6), `{rec_items}` (scarf in olive, blazer in navy, lipstick in warm rose, eyeglass frames in tortoise)

**Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout

### Nano Banana version:

```
A personal color analysis board on a white background for {subject_description}. Top section: portrait of the subject on the left, seasonal classification "{season_type}" on the right with a grid of {num_palette} color palette swatches ({palette_colors}). Middle section: side-by-side comparison — left shows the subject in a {flattering_color} top looking healthy and bright ("{good_label}"), right shows the same subject in {unflattering_color} looking washed out ("{bad_label}"). Bottom strip: {num_recs} recommended items ({rec_items}) each in a palette color with one-word labels. Clean editorial layout, visual-first with minimal text, thin gray dividers between sections. Format: 3:4.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/prompt-framework.md

# Prompt Framework

Универсальный чеклист для построения промпта. Применим к **обеим** семьям моделей. Для отличий смотри:
- [nano-banana.md](nano-banana.md) — NB-специфика (grounding, extreme ratios, thinking mode, JSON)
- [gpt-image.md](gpt-image.md) — GPT Image 2 (5-slot template, anti-slop, quality settings)
- [models.md](models.md) — какую модель когда выбрать

## Task Types (Навыки)

Определи тип задачи - это задаёт стратегию промпта:

| Type | Когда использовать | Ключевые элементы |
|------|-------------------|-------------------|
| **Photorealistic** | Фото людей, продуктов, сцен | Освещение, материалы, атмосфера |
| **Illustration** | Стикеры, иконки, арт | Стиль, контуры, палитра |
| **Product/Commercial** | Продуктовая съёмка | Поверхность, отражения, композиция |
| **Minimalist** | Негативное пространство | Что убрать важнее чем что добавить |
| **Sequential** | Комиксы, сториборды | Панели, переходы, нарратив |
| **Editing** | Изменение существующего | Конкретные инструкции что менять |
| **Style Transfer** | Перенос стиля | Референс + новый контент |
| **Composite** | Объединение элементов | Связность, освещение, масштаб |
| **Text Rendering** | Текст в изображении | Точные кавычки, позиция, вес |

## Universal Elements (Чеклист)

Пройдись по списку - не всё нужно указывать, но полезно проверить:

**Обязательные:**
- **Субъект** - кто/что в центре внимания
- **Контекст** - для чего это (определяет стиль)

**По ситуации:**
- **Действие** - что происходит
- **Окружение** - где это происходит
- **Камера** - крупность плана (close-up, wide shot, etc.)
- **Освещение** - тип света
- **Настроение** - эмоция сцены
- **Материалы** - текстуры поверхностей
- **Палитра** - цвета (лучше hex)
- **Формат** - соотношение сторон

> ⚠️ **Параметры объектива** (50mm, 85mm, f/2.8, ISO):
> - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
> - **GPT Image 2** — допускает «50mm feel» как high-level look, но не как точную физическую симуляцию

## Detail Modes (Режимы)

**Concise** - одно предложение, для быстрых итераций:
```
Minimalist poster: white background, single red apple, centered, dramatic shadow.
```

**Standard** - 1-2 параграфа, баланс контроля и гибкости:
```
Create a product shot for premium headphones marketing.

Matte black headphones on dark slate surface. Single spotlight from upper left creates dramatic shadow. Background gradient from #1a1a1a to pure black.

Format: 16:9
```

**Verbose** - максимум деталей для сложных сцен:
```
Create a cinematic wide shot for sci-fi film concept art.

Setting: Abandoned space station observation deck. Massive curved window spans entire wall, revealing dying red giant star filling half the frame. Station interior in deep shadow except where crimson light bleeds through.

Subject: Lone astronaut in weathered EVA suit, helmet off, sitting on debris pile. Back to camera, facing the star. Pose suggests exhaustion and acceptance.

Atmosphere: Dust particles float in zero-g, catching red light. Abandoned equipment scattered - coffee cup frozen mid-float, papers suspended. Frost crystals on interior surfaces where life support failed.

Mood: Melancholic beauty, end of an era
Lighting: Volumetric god rays from star through window
Format: 2.39:1 cinemascope
```

## Output Structure

При создании промпта выдавай:

**1. Prompt** - готовый к использованию

**2. Parameters** - если нестандартные:
- Aspect ratio (если не 1:1)
- Resolution (если нужно 2K/4K)

**3. Exclusions** - что исключить (опционально):
> Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"

**4. Assumptions** - что додумано, если пользователь не указал

## Quick Decision Tree

```
Что создаём?
├── Фото реального объекта/человека → Photorealistic
├── Рисунок/арт → Illustration  
├── Товар для продажи → Product/Commercial
├── Много пустого места → Minimalist
├── Несколько кадров/история → Sequential
├── Меняем существующее фото → Editing
├── "Как на этой картинке" → Style Transfer
├── Собираем из нескольких элементов → Composite
└── Текст - главный элемент → Text Rendering
```

> Image grounding (поиск реальных мест в интернете) и экстремальные ratio (1:8, 8:1, 4:1) — только Nano Banana. См. [nano-banana.md](nano-banana.md).

## Examples by Type

### Photorealistic
```
Portrait of a weathered fisherman, 60s, deep wrinkles and sun-damaged skin.
Early morning golden hour on wooden dock.
Holding fresh catch, genuine smile of satisfaction.
Background: misty harbor, fishing boats soft focus.
Mood: authentic, documentary style
```

### Product/Commercial
```
Product shot: luxury watch on raw concrete slab.
Single hard light from upper right, creating defined shadow.
Watch face at 10:10 position, metal bracelet draped naturally.
Background: gradient gray, vignette edges.
Style: high-end catalog, editorial
Format: 4:5
```

### Minimalist
```
Single origami crane, red paper, centered.
Pure white infinite background.
Soft diffused light, barely visible shadow.
Extreme negative space - crane occupies <10% of frame.
Format: 1:1
```

### Text Rendering
```
Motivational poster for gym.

Background: dark textured concrete, subtle vignette.

Text:
"DISCIPLINE" in extra bold, white, centered upper third
"beats talent" in thin weight, #808080, centered below

Small icon: minimal dumbbell silhouette, bottom center
Format: 9:16 (stories)
```

## Parameterized Templates

Паттерн `{variable}` для переиспользуемых промптов. Структура промпта остаётся стабильной — меняется только то, что нужно.

### Синтаксис

Переменные записываются как `{name, default="value"}`. Если значение не указано — используется дефолт. Если дефолта нет — переменная обязательна.

### Шаблон

```
Scene: {location, default="small Lisbon florist storefront at blue hour"}
Subject: {person, default="woman in navy apron"} {action, default="locking the front door"}
Important Details: {lighting}, {lens_feel, default="50mm feel"}, {key_texture}
Use Case: {use_case, default="editorial photography"}
Constraints: {constraints, default="no extra signage, no people in background"}
```

### Как использовать

1. **Заменяй только то, что меняется** — остальное берётся из дефолтов
2. **Структура стабильна** — порядок слотов одинаковый для всех вариаций, модель получает консистентный формат
3. **Batch-генерация** — идеально для серий: продуктовые ракурсы, позы персонажа, локации в одном стиле

### Примеры использования

**Серия продуктовых шотов** (меняется только товар и текстура):
```
Scene: {location, default="marble kitchen counter, morning light"}
Subject: {product} on {surface, default="raw linen cloth"}
Important Details: {lighting, default="soft window light from left"}, {lens_feel, default="85mm feel"}, {key_texture}
Use Case: {use_case, default="e-commerce hero shot"}
Constraints: {constraints, default="clean background, no props except surface"}
```

**Серия персонажных поз** (меняется действие и настроение):
```
Scene: {location, default="industrial loft studio"}
Subject: {person, default="man in black turtleneck"} {action}
Important Details: {lighting, default="single softbox, camera right"}, {lens_feel, default="50mm feel"}, {key_texture, default="fabric texture visible"}
Use Case: {use_case, default="fashion editorial"}
Constraints: {constraints, default="no visible logos, neutral expression"}
```

## Cinematic Verbose Mode

Стандартный verbose — 5-7 строк. **Cinematic verbose** — уровень выше, для случаев когда нужен максимум детализации: hero shots, ключевые визуалы, campaign centerpieces.

### Когда использовать

- Финальный визуал кампании, а не итерация
- Hero shot для лендинга или обложки
- Key visual, который будет масштабироваться на все форматы
- Портфолийная работа, где каждый пиксель имеет значение

### Чеклист микро-деталей

Добавляй поверх стандартного verbose — это дополнительные слои, а не замена:

1. **Surface wear & aging** — "chipped paint on window frame, hairline scratches on metal surface, green patina on copper fittings, oxidation marks on iron hinges"
2. **Micro-textures** — "visible pores on skin, individual hair strands catching backlight, fabric weave pattern on linen shirt, grain of weathered wood"
3. **Atmospheric particles** — "dust motes suspended in light beam, steam wisps rising from coffee cup, pollen floating in golden hour air, fine rain droplets on glass surface"
4. **Specular behavior** — "specular highlights on metal edges of watch, caustic reflections dancing inside glass bottle, wet surface sheen on cobblestones after rain"
5. **Fabric & material drape** — "natural fabric folds at elbow crease, gravity pull on loose linen garment, weight distribution visible in heavy wool coat"
6. **Contact shadows** — "soft contact shadow where cup meets saucer, ambient occlusion in crevices of stone wall, dark line where book spine meets table"
7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby sign"
8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"

### Before / After

**Standard Verbose:**
```
Create a cinematic portrait for coffee brand campaign.

Setting: Small Italian café, early morning. Espresso machine prominent in background.
Subject: Barista in white shirt, mid-pour, focused expression.
Atmosphere: Steam rising, warm tones, golden morning light through window.
Mood: Craftsmanship, ritual, quiet dedication
Lighting: Warm directional light from left window
Format: 4:5
```

**Cinematic Verbose:**
```
Create a cinematic portrait for coffee brand campaign.

Setting: Small Italian café, early morning. Brass-and-chrome La Marzocca espresso machine in background, oxidation marks on steam wand, hairline scratches on drip tray from years of use. Chipped paint on wooden window frame behind machine.

Subject: Barista in white linen shirt — fabric weave pattern visible, natural folds at rolled-up sleeves, gravity pull on loose collar. Mid-pour with focused expression, visible pores on forehead, individual eyebrow hairs catching backlight.

Atmosphere: Steam wisps rising from espresso cup, dust motes suspended in morning light beam cutting through window. Fine coffee grounds scattered on worn marble counter — soft contact shadow where cup meets saucer. Wet surface sheen on freshly wiped counter edge.

Details: Specular highlights on chrome portafilter handle. Caustic reflections dancing inside glass water carafe on shelf. Warm neon glow of "APERTO" sign reflecting on barista's forearm. Slight motion blur on trailing steam, frozen droplet mid-drip from group head.

Mood: Craftsmanship, ritual, quiet dedication
Lighting: Warm directional light from left window, volumetric through steam
Format: 4:5
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/slides.md

# Presentation Slides

Professional slide visuals for decks and pitches.

## Design Principles

### One Slide = One Idea
Не комбинируй несвязные концепции. Аудитория запоминает 65% визуального vs 10% услышанного.

### Content Limits
- Max 5 пунктов на слайде
- 15-20 слов в блоке текста
- Заголовок + список ИЛИ абзац, не оба

### Typography
```
Заголовок: 44-54 pt, bold
Подзаголовок: 28-36 pt, medium
Текст: 18-24 pt, regular (min 18 для читаемости)

Шрифты: sans-serif основной (Inter, Helvetica, Roboto)
Serif только для акцента
```

### Contrast & Color
- 3-4 цвета max (основной + 2-3 акцента)
- Один нейтральный фон (white/black/gray)
- Контраст min 4.5:1
- Избегай pure white #fff на чёрном - используй #f5f5f5

### Whitespace
- Контент должен дышать
- Асимметричные макеты (2/3 + 1/3) динамичнее центрированных
- Если тесно - разбей на два слайда

### Visual Consistency
- Один стиль: фото ИЛИ иллюстрации ИЛИ минимал графика
- Смешивание = визуальный хаос
- High-res only, каждый образ усиливает идею

### Checklist
```
☐ Один слайд = одна идея
☐ Max 5 пунктов
☐ Заголовок 44-54pt, текст 18-24pt
☐ 3-4 цвета, высокий контраст
☐ Достаточно whitespace
☐ High-res визуалы, единый стиль
```

---

## Slide Types

### Hero Title (Dark)
```
Create dramatic title slide for [CONTEXT] presentation.

Background: Gradient from [DARK hex] to #0a0a0a.
Atmospheric: subtle mist at lower edge.

Typography:
"[MAIN TITLE]" in extra bold, white, extremely large, upper third
"[SUBTITLE]" in thin, muted, 5x smaller, below

Mood: Confident, premium
Format: 16:9
```

### Data Visualization
```
Create data slide for [CONTEXT] presentation.

Background: Dark gradient [hex] to [hex].

Hero number: "[METRIC]" in bold, [ACCENT], center
Trend: [up/down arrow] in [green/red]
Supporting: 3-4 smaller metrics below

Chart: [TYPE] showing [DATA]

Mood: Analytical, impactful
Format: 16:9
```

### Comparison (Light)
```
Create comparison slide for [CONTEXT].

Background: Off-white #fafafa to #f0efed.

Split layout:
Left: "[OPTION A]" with details
Right: "[OPTION B]" with details

Emphasis: Right side accent bar #3b82f6

Mood: Clear, objective
Format: 16:9
```

### Insight/Problem
```
Create insight slide for [CONTEXT].

Background: Clean off-white.

Focal: "[KEY MESSAGE]" in bold, centered
Supporting: "[CONTEXT]" smaller, below
Emphasis bar: [ACCENT] strip with data point

Mood: Clarity, focus
Format: 16:9
```

### Process/Timeline
```
Create process slide for [CONTEXT].

Flow: [HORIZONTAL/VERTICAL]
Stages: [1]→[2]→[3]→[4]
Each: icon + "[LABEL]" + description
Connectors: arrows in [ACCENT]

Format: 16:9
```

## Typography

**Hierarchy:**
- Hero: "Extremely large, dominating upper third"
- Primary: "Large, commanding"
- Secondary: "3-5x smaller than hero"
- Footer: "Minimal"

**Weight:** thin | regular | medium | bold | extra bold
**Position:** "upper third", "left aligned 10% margin", "centered"

## Color Systems

**Dark palette:**
- Near-black: #0a0a0a, #121212
- Deep tones: #0d3d2d, #1a2a3a
- Text: #ffffff, #e0e0e0

**Light palette:**
- Off-white: #fafafa, #f8f9fa
- Warm gray: #f5f5f4
- Text: #1a1a1a, #374151

**Data colors:**
- Positive: #22c55e
- Negative: #dc2626
- Highlight: #3b82f6

## Atmospheric Effects

- "Subtle gradient haze"
- "White mist at ground level"
- "Soft vignette darkening edges"
- "Noise texture for premium feel"

---

## Layout Systems

Универсальные правила вёрстки. Работают с любым визуальным стилем.

---

### Bento Grid

Модульная система из блоков разного размера.

**Core Rules:**
- Родительский контейнер с явными границами модулей
- Иерархия: важный контент → крупные блоки, второстепенный → мелкие
- Max 9 блоков (иначе перегруз)
- Единообразные gaps (16px стандарт)
- Связанный контент группируется в одном блоке

**Размеры:** широкие/плоские (hero) | узкие/высокие (списки) | квадратные (иконки)

**Сетки:**
```
3-block:           6-block:             9-block:
┌───────┬───┐     ┌───┬───┬───┐       ┌─────┬───┬───┐
│ HERO  │SEC│     │ S │ S │ S │       │HERO │MED│ S │
├───────┴───┤     ├───┴───┼───┤       ├──┬──┴───┼───┤
│  FOOTER   │     │ CHART │LST│       │S │ MED  │ S │
└───────────┘     └───────┴───┘       └──┴──────┴───┘
```

**Prompt:**
```
Layout: bento grid, [N] blocks
Hero block: [MAIN], Medium: [SECONDARY], Small: [ICONS]
Gaps: uniform spacing
```

---

### Asymmetric Grid

Динамичные композиции с визуальным балансом.

**Rules:**
- Начинай с базовой сетки, потом ломай осознанно
- Балансируй вес: крупный элемент слева = несколько мелких справа
- Rule of Thirds для естественного баланса
- Ключевые элементы выделяй размером и положением

**Применять:** креативные презентации, портфолио, fashion, стартапы
**НЕ применять:** банки, госпорталы, B2B с большими данными, пожилая аудитория

**Prompt:**
```
Layout: asymmetric composition
Left: [LARGE - 60%], Right: [2-3 SMALLER stacked]
Balance: visual weight distributed
Rule of thirds positioning
```

---

### Negative Space

Пространство как инструмент фокусировки.

**Rules:**
- Структурирует, а не создаёт пустоту ради красоты
- Управляет вниманием, фокусирует на главном
- Gestalt: элементы с пространством = отдельные, близко = связанные

**Применять:** премиальные бренды, минималистичные презентации, hero-секции
**НЕ применять:** новостные порталы, дашборды, мобильные версии

**Prompt:**
```
Layout: generous whitespace
Focal point: [ELEMENT] with breathing room
Empty space: intentional, guides eye to [CTA]
```

---

### Split Screen

Двухколоночная композиция.

**Пропорции:**
- 50/50 - равноценные элементы
- 60/40 - акцент на одной стороне
- 70/30 - явный герой + поддержка

**Prompt:**
```
Layout: split-screen [RATIO]
Left: [CONTENT], Right: [CONTENT]
Divider: [sharp / gradient / none]
```

---

### Brutalist

Сырая эстетика, огромные шрифты, яркие цвета.

**Rules:**
- Сохраняй чёткую навигацию и иерархию
- Читабельность > экспрессия
- Применяй селективно: яркие цвета ИЛИ огромные шрифты

**Применять:** портфолио художников, fashion, стартапы
**НЕ применять:** e-commerce, корпораты, образование, финтех

**Prompt:**
```
Style: brutalist design
Typography: massive, raw
Colors: high contrast, bold
Hierarchy: clear despite unconventional styling
```

---

## Futuristic / SaaS Style

Apple Keynote minimalism + glassmorphism + 3D objects.

### Visual Language
```
Style: Apple Keynote + SaaS + glassmorphism
Mood: premium, immersive, clean, breathable
Lighting: volumetric, ray-traced reflections, ambient occlusion
Base: deep void black OR pure ceramic white
Accents: aurora gradients (neon purple, electric blue, coral, cyan)
```

### Glassmorphism Cards
```
Material: frosted glass with blur
Edges: delicate white borders
Shadow: soft, diffused
Spacing: generous internal whitespace
```

### 3D Visual Anchors
```
Purpose: abstract 3D artifacts as focal points
Materials: polished metal, iridescent acrylic, transparent glass, soft silicone
Shapes: capsules, spheres, shields, Möbius strips, fluid waves
Quality: looks like expensive collectibles
```

### Composition by Type

**Cover:** huge 3D glass object center + bold title + aurora background
**Content:** bento grid + 3D icons in small cards + text in large cards  
**Data:** split-screen (text left, glowing 3D chart right)

### Charts Style
```
3D donut charts, glowing
Capsule-shaped progress bars
Floating numbers with neon glow
Style: looks like glowing neon toys
```

### Example Prompt
```
Create a futuristic SaaS slide for product presentation.

Style: Apple Keynote + glassmorphism.
Mood: premium, immersive, clean.
Background: void black with aurora gradient (purple → cyan).

Layout: bento grid, 6 blocks.
Cards: frosted glass, blur, white edges, soft shadows.
Hero block: floating iridescent sphere.
Data blocks: glowing 3D donut chart, neon metrics.

Typography: clean sans-serif, high contrast white.
Format: 16:9
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/storyboards.md

# Storyboards & Sequential Art

One-shot narrative sequences. Concept art. Consistent across frames.

## Story Sequence

```
Create [NUMBER]-part story with [NUMBER] images.

Characters: [DESCRIPTION]
Setting: [LOCATION/CONTEXT]
Story arc: [NARRATIVE with emotional highs/lows]

Identity: Characters and attire consistent throughout.
Variation: Different angles, distances, expressions.
Generate: One image at a time.
Format: [ASPECT RATIO] per image.
```

## Commercial Storyboard

```
Create [NUMBER]-part story for [PRODUCT] commercial.

Characters: [man and woman / family / solo]
Product: [DESCRIPTION]
Story: [EMOTIONAL ARC]
Ending: Elegant shot with [LOGO/PRODUCT]

Identity and attire consistent throughout.
Vary angles and distances.
Generate one at a time.
Format: 16:9 landscape.
```

## Film Storyboard

```
Create storyboard for this scene.

Shots:
1. Establishing shot - [DESCRIPTION]
2. Medium shot - [ACTION]
3. Close-up - [DETAIL]
4. POV shot - [PERSPECTIVE]

Style: [B&W sketch / color / cinematic]
Annotations: [CAMERA MOVES / NOTES]
```

## Concept Art Series

```
Create concept art series for [PROJECT].

Subjects: [CHARACTERS / ENVIRONMENTS / PROPS]
Style: [AESTHETIC]
Mood: [TONE]

Consistency: Design language across all pieces.
Generate one at a time.
```

## Sprite Sheets

```
Sprite sheet of [CHARACTER] doing [ACTION].
Grid: [3x3 / 4x4]
Sequence: frame by frame animation
Format: square aspect ratio
Follow reference grid structure exactly.
```

Tip: Extract cells to make GIF.

## Consistency Rules

- "Identity must stay consistent throughout"
- "Attire same across all images"
- "Can be seen from different angles and distances"
- "Expressions and poses should vary"
- "Only one of each character per image"

## Narrative Pacing

- "Story is thrilling with emotional highs and lows"
- "Ends on [happy / dramatic / mysterious] moment"
- "Build tension through first [N] images"
- "Climax in image [N], resolution in final"

## Output Control

- "Generate images one at a time"
- "Make sure every image is [ASPECT RATIO]"
- "Please generate [NUMBER] images, one at a time"

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/structural.md

# Structural Control

Input images control composition. Sketch→final, wireframes, grids.

## Sketch → Final

```
Create [ASSET TYPE] following this sketch exactly.

Sketch defines: composition, element placement, text position
Quality: [polished / professional / specified style]
Text: Render "[EXACT TEXT]" where indicated
```

Hand-drawn layouts become polished assets.

## Wireframe → Mockup

```
Generate [MOCKUP TYPE] following these wireframes.

Layout: Match wireframe structure precisely
Content: [placeholder / realistic]
Style: [UI style / brand guidelines]
```

UI/UX designs from rough wireframes.

## Grid-Based Assets

```
Generate [ASSET] fitting this [SIZE] grid.
Each cell: [CONTENT]
Consistency: Uniform style across cells
```

Use cases:
- Sprite sheets for games
- LED display content
- Tile-based graphics

## Pixel Art

```
Generate pixel art [SUBJECT] fitting [SIZE] grid.
Colors: high contrast
Style: [retro / modern pixel]
```

Tip: Extract cell colors programmatically for LED matrices.

## Layout Guidance

Reference images can control:
- **Where** elements sit
- **What** proportions to use
- **How** text flows
- **Which** areas get emphasis

## Brand Identity Systems

```
[Input: logo sketch or design]
Create identity system using this logo.

Generate one at a time:
1. Logo refinement
2. Business card mockup
3. Letterhead
4. Billboard application
5. Product packaging
6. Digital banner
7. Social media avatar
8. App icon
9. Signage
10. Merchandise

Format: 16:9 each
Maintain: brand consistency across all
```

## Composition Templates

Use reference for:
- Magazine layouts
- Poster compositions
- Social media templates
- Presentation structures

```
Follow the composition of reference image.
Replace: [ELEMENTS] with [NEW CONTENT]
Maintain: proportions, visual hierarchy
```

## Precision Control

- "Position text exactly where sketch indicates"
- "Follow grid structure exactly"
- "Match layout precisely"
- "Keep proportions from reference"

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/text-rendering.md

# Text Rendering & Infographics

Универсальные стили, layout-типы, примеры. Применимо к обеим моделям, но детали рендера расходятся:

- **Nano Banana:** SOTA по 100+ языкам, multi-language в одном кадре, можно называть конкретные шрифты («Century Gothic 12px», «Brush Script»). См. [nano-banana.md](nano-banana.md).
- **GPT Image 2:** EXACT TEXT в `"..."` или ALL CAPS, добавляй «no extra words / no duplicate text», для мелкого текста — `quality: high`. См. [gpt-image.md](gpt-image.md).

## Prompt Structure

```
Create an educational infographic about [TOPIC].
Target Audience: [GRADE/LEVEL]
Content: [SPECIFIC FACTS/SEQUENCE]
Title: "[TITLE TEXT]"
Visual Style: [STYLE]
Layout: [LAYOUT TYPE]
Format: [ASPECT RATIO]
```

## Visual Styles

**Educational/Friendly:**
- Paper Cutout: construction paper collage look
- Claymation/Plasticine: 3D tactile, Wallace & Gromit style
- Kawaii/Cute Vector: rounded edges, pastel colors
- Storybook Watercolor: soft painted textures
- Chalkboard Art: white chalk on green/black
- Pixel Art (8-Bit): retro gaming nostalgia

**Technical/Professional:**
- Isometric 3D: video game map style, processes
- Blueprint/Schematic: white lines on blue
- Da Vinci Notebook: renaissance sketch, scientific
- UI/UX Wireframe: app blueprint style
- Dashboard: analytics screen with numbers

**Stylized:**
- Cyberpunk/Neon: dark + bright neon accents
- Graphic Novel/Comic Book: bold outlines, flat colors
- Vintage Science Poster: muted, aged paper, fine lines
- Pop Art (Warhol): high contrast, bold, dots
- Corporate Memphis/Flat Art: tech company style

**Specialized:**
- Subway/Transit Map: journey, connections
- IKEA Manual: wordless step-by-step
- Knolling (Flat Lay): objects at 90° angles, overhead
- Origami/Paper Folding: geometric, clean

## Layout Types

**Linear:**
- Horizontal Timeline: history, biography
- Step-by-Step Flow: recipes, experiments, processes
- Winding Roadmap: journey through topic

**Comparison:**
- Split Screen (Versus): instant contrast
- Comparison Matrix: multiple items, same criteria
- Before and After: cause and effect
- Venn Diagram: compare and contrast

**Hierarchical:**
- Pyramid: foundation to peak (Maslow, food pyramid)
- Funnel: filtering process (bill→law, sales)
- Iceberg: visible vs invisible (10% above, 90% below)

**Radial/Connected:**
- Hub and Spoke: core topic + attributes
- Tree/Branching Map: genealogy, taxonomy
- Concentric Circles: layers (Earth, proximity)

**Grid-Based:**
- Bento Grid: tidy boxes, modular
- Periodic Table Grid: items by type/family
- Comic Strip: narrative in scenes
- Jigsaw: pieces forming whole

**Spatial:**
- Isometric Map: 3D game world style
- Cross-Section (Cutaway): inside something solid
- Anatomical Call-out: labeling parts of whole
- Exploded View: parts hovering, showing assembly

## Examples

**Science - Water Cycle:**
```
Create educational infographic for Elementary Science.
Topic: The Water Cycle.
Content: Evaporation, Condensation, Precipitation, Collection.
Visual Style: Bright, colorful, 3D claymation style.
Layout: Circular flow diagram with arrows clockwise.
```

**History - Timeline:**
```
Create educational infographic for High School History.
Topic: Timeline of Ancient Egypt.
Content: Old Kingdom (Pyramids), Middle Kingdom (Arts), New Kingdom (Tutankhamun).
Visual Style: Papyrus texture, hieroglyphic icons, gold/sand palette.
Layout: S-curve roadmap flowing top to bottom.
```

**Literature - Iceberg:**
```
Create educational infographic for Sociology class.
Topic: Surface Culture vs Deep Culture.
Content: Above water (Food, Flags, Festivals). Below water (Body Language, Beliefs, Etiquette).
Visual Style: Paper Cutout Style, textured construction paper.
Layout: Iceberg diagram, tip = 10%, submerged = 90%.
```

**Comparison - Matrix:**
```
Create educational infographic for Elementary Science.
Topic: Inner vs Outer Planets.
Content: Compare across Surface Type, Size, Rings.
Visual Style: Kawaii/Cute Vector, pastel colors.
Layout: Comparison Matrix grid.
```

## Text-First Hack

For complex text in images, generate text FIRST, then ask for the image:
1. Ask the model to write/refine the text content
2. Then ask for an image with that exact text

This produces sharper, more accurate typography than cramming everything in one prompt.

## Font Control

Describe typography style or name the font directly:
- "Bold, white, sans-serif font"
- "Century Gothic 12px font"
- "Flowing, elegant Brush Script"
- "Heavy, blocky Impact font"
- "Thin, minimalist Century Gothic"

## Multilingual / Localization

Supports 10+ languages. Two approaches:

**Direct:** Write prompt in target language, text renders in that language.

**Translate:** Write prompt in one language, specify target:
```
Create this product ad. Render all text in Korean.
```

**Multi-language in one image:**
```
Line 1: "GLOW" in Brush Script
Line 2: "10% OFF" in Impact font
Line 3: "Your First Order" in Century Gothic
Then translate all text into Korean and Arabic.
```

## Tips

**Provide your own content:**
- Paste article text, video transcript, your notes
- More accurate than relying only on search

**Sketch-to-Image:**
- Draw messy layout sketch on paper
- Upload with prompt: "Use layout from attached image"

**Iterative editing:**
- "Leave everything else exactly the same, but change [X]"
- Annotate downloaded image, upload back as reference

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: image/references/vision-decomposer.md

# Vision Decomposer — Image-to-Prompt Analysis

Use this reference when the user asks to analyze an image and convert it to a generation prompt: **style transfer**, **mood reference**, **"сделай промпт по этой картинке"**, **"перенеси стиль/образ"**, **"проанализируй кадр"**, **"image to prompt"**, **"reverse-engineer this look"**.

You become a **professional Vision Agent**. Your task is deep cinematic, psychological and optical-colorimetric analysis of the image, translating it into a perfect, highly detailed text prompt for generation.

The process has two strict steps. Do not skip Step 1. Do not freestyle Step 2.

---

## STEP 1 — DEEP DECOMPOSITION

Scan the image as **raw data** and extract facts based on:

- **Cinematic composition** — Bruce Block's visual structure
- **Color theory** — Itten
- **Perceptual psychology** — Arnheim
- **Directing references** — Spielberg / Scorsese / Tarantino
- **Cinematography & colorimetry** — Valentin Zheleznyakov

Evaluate the following four parameter blocks.

### 1. Subject — psychology and mise-en-scène

- **Who / What:** precise clothing (era, style, materials), age, skin texture, makeup / toning, micro-expressions.
- **Shot size (after Mascelli):** Extreme Long Shot (ELS), Long Shot, Medium Shot, Two-shot / Three-shot, Close-Up (CU), Choker CU, Extreme CU, Insert shot.
- **Directing & force placement (Blocking after Kenworthy):** isolating the character at the edge of the frame (anxiety), physical barriers, face turned away from camera, shooting from behind (effect of unknown / powerlessness). Height difference (Level Change) for dominance.
- **Kinetics & perceptual forces (Arnheim):** visual weight of the object, center of gravity. Internal tension of form (compression / stretching / twisting). Pose, plasticity, motion vectors. Imitation of swift action (motion blur) or monumental stillness.
- **Color and emotion (Itten):** psychological impact of the local color of the subject.
- **Gaze:** direction, eyeline anchor, interaction with the frame edges, look into the lens.

### 2. Environment — geometry and structure of space

- **Setting & Art Direction:** place, era, background, architecture, specifics of materials and surface textures (gloss, matte, rust).
- **Three-plane depth (Spielberg):** clear separation into Foreground (with leading details), Midground (action plane), Background.
- **Figure & ground (Arnheim):** degree of subject isolation, overlapping of forms, mass relationships. Use of reflections (mirrors, windows) to expand context.
- **Tonal & aerial perspective (Zheleznyakov):** drop in contrast, desaturation, washing out, shift toward cool (blue-cyan) tones in the background.
- **Frame geometry:** structural framework (axes of symmetry / asymmetry), claustrophobic compression, surface divisions. Illusion of depth via Foreground framing.

### 3. Lighting — chiaroscuro, color and contrast

- **Optical & visual contrast (Zheleznyakov):** ratio of lit and shadow areas (OVK). Depth and density of shadows. Exact local color vs. color modified by lighting (valeurs).
- **Lighting scheme:** Key, Fill, Backlight / Rim, Modeling. Rembrandt lighting, Chiaroscuro. Height, hardness (Hard / Soft) and type of source.
- **Broken light & reflexes (Zheleznyakov):** use of shadow masks (gobos), light through blinds / foliage, color reflexes from neighboring objects onto skin / clothing.
- **Tonality & color:** light key (High-key / Low-key). Threshold Silhouette. Itten's 7 contrasts. White balance (Daylight / Tungsten) and temperature contrast (warm light / cool shadows).

### 4. Tech & Cinematography — optics, filters and film texture

- **Camera (angles & viewpoint):** Angle (High angle, Low angle, Eye-level, Dutch tilt). Objective camera, Subjective, POV, Over-the-shoulder (OTS). Movement imitation (Push-in, Tracking shot).
- **Optics & DOF:** Focal length (wide-angle for distortion / coverage, telephoto for spatial compression). Depth of field. Rack focus, bokeh.
- **Optical filters & attachments (Zheleznyakov):** diffusion filters (Pro-Mist, Black Pro-Mist, Fog, Double Fog, Low Contrast) for highlight bloom (halation), skin softening, lowering of micro-contrast. Polarizers (cutting reflections).
- **Effects & texture:** Frame format (70mm, 35mm, IMAX). Exposure (motion blur). Stylization (Bleach Bypass). Film Grain, chromatic aberration.

---

## STEP 2 — PROMPT SYNTHESIS

Assemble the final prompt from Step 1 data.

Rules:
- Write **only keywords separated by commas, in English**.
- Describe **strictly what you see**. Do not invent new objects.
- **No filler.** Never write "The image shows...", "A picture of...", "I can see...".
- **Strict word order** (this formula is non-negotiable):

```
[Shot type, optics and angle], [Subject, mise-en-scène / blocking, visual weight, clothing and action], [Multi-plane environment (Foreground / Midground / Background), overlapping and geometry], [Lighting scheme, optical contrast, gobos and reflexes], [Color palette, temperature contrast and aerial perspective], [Color Grading, diffusion filters, film stock, textural artifacts]
```

---

## OUTPUT PROTOCOL

When the user gives you an image (or asks to reverse-engineer one), produce the answer in **two blocks**:

### Block 1 — Brief Analysis Log

```
Subject & Blocking: ...
Environment & Depth: ...
Lighting & Contrast: ...
Tech & Optics: ...
```

Each line: 1-2 sentences max. Just the extracted parameters.

### Block 2 — Final Prompt

A code block containing only the prompt text in English, assembled by the formula in Step 2:

````
```
<comma-separated keywords following the strict 6-segment formula>
```
````

After the prompt, append the standard image-skill output header (Model / Quality / Size) so the user can drop it straight into the generator.

---

## When to load this file

Load `vision-decomposer.md` whenever:
- The user attaches an image and asks for a prompt to **recreate / transfer / match** its style
- The user asks to **decompose, deconstruct, reverse-engineer** a visual reference
- The user says **"перенеси стиль", "сделай так же", "повтори образ", "проанализируй кадр", "разбери картинку на промпт"**
- Mood-board work: extracting cinematic DNA from a film still, ad frame, painting, photo

Do NOT load this for: pure generation requests where no reference image is given. For those, use the standard model files.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*

