# Reglas del skill: image

167 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## image/SKILL.md

- [11ea00e863de] The body of this SKILL.md is intentionally thin so you cannot fake a result by reading it alone. The actual rules — what the models reward, what they punish, how to phrase a 5-slot template, when to add `quality: high`, when to use image grounding — live only in the reference files.
- [3f921ee68519] **Motion, clips, montage** (Seedance, Kling, Veo, any image-to-video): use the sibling `video` skill. This skill's storyboard and keyframe outputs feed it.
- [e00683c0b45f] Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mode. JSON for 5+ elements. Up to 14 reference images. Why you must NOT write `50mm / f-stop / ISO` numbers.
- [7753f474afb0] 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop banned-words list. `quality: low / medium / high` as a deliberate fidelity lever. Size constraints (multiples of 16, max 3:1, up to 2560×1440). Two-column edit logic (Change / Preserve / Constraints). Up to 16 reference images with explicit roles.
- [485206c1697b] Universal rules that apply to both models: start with a verb, positive framing, hex colors, quote text, edit don't re-roll, one change per iteration, reference images.
- [67a7dd9329dc] For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
- [890a0b28f120] Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano Banana).
- [0e7900ffe2af] Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars" — invert to positive), external comparisons ("like Apple ad" — describe the visual properties instead), numerical lens parameters in Nano Banana prompts (it ignores them).

## image/references/creative-direction.md

- [09ec7d23fe12] Hasselblad — medium format, shallow DOF, fashion/portrait
- [b921448eda9a] "Waist-up portrait", "full body", "over-the-shoulder"
- [b8fa85d560e3] "Shallow depth of field" — blurred background
- [5ad1340da288] > descriptive terms. Prefer "shallow depth of field" over "f/1.8".
- [862a4c0ea3bc] Define physical makeup of subjects. Don't just say the thing — describe what it's MADE of.

## image/references/golden-rules.md

- [d9bcca3cf113] Describe what you WANT, not what you don't want. The model understands presence better than absence.
- [1dd54b582a02] ✅ "empty street" → ❌ "street with no cars"
- [7fff008d0b4a] ✅ "clean background" → ❌ "no clutter"
- [f5bdd52eae18] ✅ "solo portrait" → ❌ "no other people"
- [cc4167f1d432] ❌ Bad: "Cool car, neon, city, night, 8k"
- [8d02f99b51e9] ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neon signs reflect off wet pavement and metallic chassis."
- [8901152207fe] "for Brazilian gourmet cookbook" → infers professional plating, shallow DOF
- [dd9305290d20] Используй для:
- [04c28ccbddf9] **Используй как HIGH-LEVEL steering** — якорь задаёт настроение и эстетику, а не заменяет весь промпт
- [3db8f42e251f] **Комбинируй с конкретными визуальными деталями** — якорь устанавливает мир, детали устанавливают специфику
- [16ec02525ce7] **Не стакай несколько genre anchors** — выбери один. "Peter Lindbergh + Wes Anderson" = каша
- [47652229b5ab] **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные описания

## image/references/gpt-image.md

- [0fdc95a5bbec] ❌ Не пиши | ✅ Пиши
- [1848820351ae] мудовый язык, в котором тонут функциональные требования | прямое заявление: «image must contain a transit kiosk»
- [20e10fa23ffc] Маленький/плотный/multi-font → `quality: high` обязательно.
- [26e0c5fc6ab4] **Object removal:** «Remove [X]. Do not change anything else. Use `input_fidelity: high` to maintain surrounding context» (только gpt-image-1.5/1, в gpt-image-2 high-fidelity по умолчанию).
- [822ae545689f] GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не расписывай каждую деталь.

## image/references/models.md

- [c10c7e21ff29] **Структурированный 5-slot промпт.** Чёткое разделение Scene/Subject/Details/Use case/Constraints даёт предсказуемость.

## image/references/multi-panel.md

- [c842524ed79f] **When to use:** TVC or commercial shot breakdown — one image = 9 panels with scene titles and timestamps.
- [a127cca4810d] **Recommended size:** 1536x1024 (landscape)
- [e01904554508] Vague scene descriptions produce near-identical panels — each must have a distinct action, angle, or subject
- [3d26f71cccce] **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
- [52c7e13d4185] **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis)
- [796a278bda86] **When to use:** Hero shot + close-up + action for a campaign visual — horizontal or vertical triptych.
- [3a5fb89a88b1] **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych)
- [7421490e82fa] **Model:** GPT Image 2 `quality: medium` — if text overlay needed, use `quality: high`
- [576f2ecf7dd2] **When to use:** 12 panels telling a story or showing moods — no gaps between panels, seamless mosaic feel.
- [5eca40f8b2dc] **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution
- [e25ece2ca897] **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
- [0237812f9545] **Recommended size:** 1536x1024 (landscape, 3x2 grid)
- [79ad480edaab] Top-down and low-angle in the same grid confuse the model if you don't anchor each frame to a grid position
- [921aa8a23672] Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
- [d9727650ad44] **When to use:** Product transformation, makeover, time comparison, renovation — two states side by side.
- [90d4b17bba47] **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion)
- [910dd4553129] **Model:** GPT Image 2 `quality: medium` — for text labels ("BEFORE" / "AFTER"), use `quality: high`
- [d8c349628ad4] Left/right assignment matters — always state which side is before and which is after
- [1e4fc13d2d29] **When to use:** Full narrative in one image — 3x4 grid (3 columns, 4 rows) for animation or video pre-production.
- [a0be4760c51c] **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space)
- [1062c830e923] **Model:** GPT Image 2 `quality: high` (text-heavy — scene numbers and captions must be readable)
- [eb71e5086205] Art style must be stated once and applied uniformly; mixing styles across panels produces visual chaos
- [bf6161618f55] **Subject consistency:** Always include an explicit instruction: "same person / same character / same product across all panels." Repeat key identity markers (hair color, clothing, distinguishing features) rather than saying "same as before."
- [f6982091002c] **Grid specification:** Always state the grid dimensions (e.g., "3x2 grid, 3 columns 2 rows"). Saying "6 panels" without layout instruction lets the model choose an unpredictable arrangement.

## image/references/nano-banana.md

- [dabc108ffb16] Числовые параметры объектива: **50mm, 85mm, f/2.8, ISO 400** — NB игнорит. Используй описание: «shallow depth of field», «wide-angle distortion».
- [0456a3106233] Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены платные). У NB2 есть рычаг `thinking_level: minimal | high` (default `minimal`) — поднимай до `high` для:
- [a509f495c750] Interactions API держит контекст сессии — до 3 последовательных правок стэкаются без потери исходника. Правило «Edit, don't re-roll»: картинка верна на 80% — проси точечное изменение, а не новую генерацию.
- [82d4b1aa2d36] **Хэндофф в видеомодель — motion brief, не пересказ.** Движение камеры, движение субъекта, движение фона, длительность, framing lock, запрещённые изменения. Видео-промпт не переописывает то, что уже есть в кадре.
- [3de5ceee5c4e] Инфографика может содержать фактически неверные данные — цифры проверять всегда, grounding помогает, но не гарантирует.

## image/references/patterns/character-design.md

- [f7781b9ee5c2] Use for game or animation pre-production — front, side, and back views of a character on a single white canvas with color callouts and height reference lines.
- [31a9f9f11aa7] **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
- [a8c47d2e697e] Use to produce a grid of 6–9 facial expressions for the same character — consistent head angle and art style, with emotion labels under each face.
- [b5749680d5b1] **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
- [e849bbafb08a] Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
- [608c66f4b15a] **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
- [639574d396e1] Use to transform a realistic character into a cute 3D collectible figurine — oversized head, compact body, multiple poses performing different activities.
- [be07ac1a9f48] **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
- [bc5138b583ba] Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional concept art layout.
- [ee853dd503fd] **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering

## image/references/patterns/ecommerce.md

- [c3d4dd460549] Use when you need a playful, attention-grabbing product visual where tiny workers interact with an oversized product — ideal for social media ads and launch campaigns.
- [19234ef99d6a] **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
- [6a46a42327af] Use for premium beauty or fragrance product photography — dark, moody, tactile surfaces with atmospheric effects.
- [9a00a07b257d] **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
- [afdcc8f7bc89] Use to present a product commercial shot breakdown in a single image — pitch decks, creative presentations, client approvals.
- [4f23b10353c9] **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
- [09817e522cce] Use for food, beverage, or supplement products where suspended ingredients communicate freshness, flavor, or composition.
- [d1f50fd09fa8] **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
- [6fc560223ecb] Use for disruptive, scroll-stopping social ads where the product packaging appears squeezed, inflated, or physically distorted as if made of soft rubber or vinyl.
- [bf758f621b50] **Recommended model:** NBP — complex spatial reasoning for believable physical distortion

## image/references/patterns/fashion-editorial.md

- [e85f3a2c01a5] Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
- [e200695107d8] **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
- [ce04a04c45aa] Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
- [97ef5791058f] **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
- [9b5c3232e804] Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
- [348b0b1ed027] **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
- [1bf69ac8c5e3] Use for playful, nostalgic sportswear or athleisure campaigns with 70s-80s visual language.
- [eb03e137df6e] **Key levers:** `{model_description}`, `{outfit_description}` (high-waisted terry shorts in coral, cropped zip-up in cream, tube socks with racing stripes), `{location_description}` (Venice Beach boardwalk, empty suburban tennis court, coastal promenade), `{film_stock}` (Kodak Gold 200, Fuji Superia 400), `{palette_description}` (terracotta #CC5533, cream #FFF5E1, sky blue #87CEEB, mustard #D4A017
- [c5971eabbb4b] **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
- [6dfcd0919723] Use for forward-looking athletic or techwear editorials where abstract 3D forms create a surreal spatial environment around the model.
- [ce24e75d12a1] **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections

## image/references/patterns/food-beverage.md

- [46ce53039819] Use for premium chocolate or confectionery brand visuals — moody, textural, with controlled color and atmosphere. Adaptable across mood variants (dark indulgence, bright artisan, earthy origin-story).
- [a9c702b552f4] **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
- [20bb122f18fb] Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
- [1ba1ff7577c8] **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
- [d4f497bb93d1] Use for hero food posters — restaurants, delivery apps, menu boards — where the food is the entire composition with fillable content slots.
- [4c926ca35845] **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
- [df532917ca8c] Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the style of 19th-century naturalist prints.
- [a30c3b235f2e] **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
- [de44302b8294] Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties across a city.
- [d62c529d34db] **Recommended model:** NB2 — image grounding for real city landmarks + illustration style

## image/references/patterns/portrait-cinema.md

- [bdc7c98423b2] Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
- [e80f84e82cd7] **Key levers:** `{street_description}` (narrow European alley with stone walls, wide boulevard with linden trees, industrial backstreet with brick), `{person_description}`, `{expression}` (quiet confidence, mid-smile with closed lips, contemplative gaze), `{bounce_surface}` (cream-painted wall, parked white van, sand-colored buildings), `{clothing_detail}` (linen shirt collar, leather jacket shoul
- [2260c15e96b4] **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
- [36bbbe701ad0] Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subject's face.
- [5b0ec72c5a49] **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
- [9a20603f7d87] Use for edgy, tech-forward portraits — artist profiles, electronic music press, tech brand campaigns. High contrast black-and-white with selective red digital artifacts.
- [29940f3cd9ae] **Key levers:** `{person_description}`, `{direction}` (left, right), `{hair_detail}` (tight buzz cut showing skull contour, shoulder-length hair with flyaway strands catching backlight, pulled-back bun), `{glitch_positions}` (across the eye, across the mouth, across the forehead — specify 2-3 positions), `{accent_color}` (#FF0000 red, #00FF41 terminal green, #FF00FF magenta), `{max_glitch_lines}` 
- [f708635c6957] **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
- [b8ecc6c820c5] Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for editorial, zine, or personal project work.
- [25c7ab649b75] **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
- [b6f22ea21acd] Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elements.
- [be5a2e46231a] **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)

## image/references/patterns/poster-illustration.md

- [5c934f24e5bd] Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, one half historical and one half modern.
- [535d74d81a91] **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
- [44c898225d80] Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
- [4c1d2cabad77] **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
- [7b6acbb90a0a] Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient with soft 3D accent elements.
- [57fca5220269] **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
- [c755ff2903b8] Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight on a saturated color field.
- [cd1fa75558c5] **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
- [803245de38c4] Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical elements in a vintage printmaking style.
- [b6a40416c21b] **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species

## image/references/patterns/ui-social.md

- [7a21ad4f3c7d] Use for vertical product or brand ads targeting Instagram Stories — hero product, bold headline, and swipe-up CTA zone at the bottom.
- [be784fefef07] **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
- [f5f07232cc75] Use for square-format posts on Instagram or Facebook — quote cards, feature announcements, or product highlights with centered layout.
- [ac9f15b7d326] **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
- [76fa850073b5] Use to create a polished App Store or Google Play listing screenshot — device frame with app UI inside, feature headline, and clean gradient background.
- [d4e8f76bb757] **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
- [b1a90c3a0a1d] Use for realistic analytics dashboard mockups — dark or light theme with data visualizations, KPI cards, and sidebar navigation.
- [8f24d3e22d84] **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements require high fidelity
- [6b8e9a41cbf9] Use to create a visual color analysis graphic from a portrait — seasonal palette classification, clothing color comparisons, and accessory recommendations in an organized layout.
- [5bb61a5742b2] **Key levers:** `{subject_description}` (age, skin tone, hair color, eye color — needed for accurate seasonal analysis), `{season_type}` (Warm Spring, Cool Summer, Warm Autumn, Cool Winter — or sub-seasons like Soft Autumn, Bright Winter), `{palette_colors}` (12 hex values matching the season, e.g. Warm Autumn: rust #B7410E, olive #708238, mustard #E1AD01, burgundy #722F37...), `{num_palette}` (12
- [e3ff88ae7b6f] **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout

## image/references/prompt-framework.md

- [e3f6e1ce49a2] **Обязательные:**
- [c8d4fff1dabe] **Палитра** - цвета (лучше hex)
- [58817d380494] > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
- [85e2a5dc4aa8] > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
- [5856058c8a75] Переменные записываются как `{name, default="value"}`. Если значение не указано — используется дефолт. Если дефолта нет — переменная обязательна.
- [84828d3c69a2] **Заменяй только то, что меняется** — остальное берётся из дефолтов
- [a90636943228] **Структура стабильна** — порядок слотов одинаковый для всех вариаций, модель получает консистентный формат
- [8005da81a345] **Batch-генерация** — идеально для серий: продуктовые ракурсы, позы персонажа, локации в одном стиле
- [42a42a73fa09] **Surface wear & aging** — "chipped paint on window frame, hairline scratches on metal surface, green patina on copper fittings, oxidation marks on iron hinges"
- [4bc498edcc17] **Micro-textures** — "visible pores on skin, individual hair strands catching backlight, fabric weave pattern on linen shirt, grain of weathered wood"
- [bc6d5c9aff5f] **Atmospheric particles** — "dust motes suspended in light beam, steam wisps rising from coffee cup, pollen floating in golden hour air, fine rain droplets on glass surface"
- [318b118d917d] **Specular behavior** — "specular highlights on metal edges of watch, caustic reflections dancing inside glass bottle, wet surface sheen on cobblestones after rain"
- [92eeb4747a7e] **Fabric & material drape** — "natural fabric folds at elbow crease, gravity pull on loose linen garment, weight distribution visible in heavy wool coat"
- [51b0bfedb210] **Contact shadows** — "soft contact shadow where cup meets saucer, ambient occlusion in crevices of stone wall, dark line where book spine meets table"
- [329aa0a4fa84] **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby sign"
- [11ec80431f42] **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"

## image/references/slides.md

- [796d88912233] Избегай pure white #fff на чёрном - используй #f5f5f5
- [2f0619f0ec28] Контент должен дышать

## image/references/storyboards.md

- [c9068adfe734] "Identity must stay consistent throughout"
- [3244bb3011e7] "Expressions and poses should vary"

## image/references/structural.md

- [2cb77800410c] **What** proportions to use
- [f2ffb547ac87] Use reference for:

## image/references/text-rendering.md

- [8e32b234137b] Ask the model to write/refine the text content
- [7447d548b9f0] Then ask for an image with that exact text
- [0db1539c575d] Upload with prompt: "Use layout from attached image"

## image/references/vision-decomposer.md

- [7e22722f52fa] Use this reference when the user asks to analyze an image and convert it to a generation prompt: **style transfer**, **mood reference**, **"сделай промпт по этой картинке"**, **"перенеси стиль/образ"**, **"проанализируй кадр"**, **"image to prompt"**, **"reverse-engineer this look"**.
- [442a75c51f58] The process has two strict steps. Do not skip Step 1. Do not freestyle Step 2.
- [a712726b25c7] **Figure & ground (Arnheim):** degree of subject isolation, overlapping of forms, mass relationships. Use of reflections (mirrors, windows) to expand context.
- [04cb7f3e5408] **Broken light & reflexes (Zheleznyakov):** use of shadow masks (gobos), light through blinds / foliage, color reflexes from neighboring objects onto skin / clothing.
- [7d2338d1b298] **Camera (angles & viewpoint):** Angle (High angle, Low angle, Eye-level, Dutch tilt). Objective camera, Subjective, POV, Over-the-shoulder (OTS). Movement imitation (Push-in, Tracking shot).
- [3d2a2115477d] Describe **strictly what you see**. Do not invent new objects.
- [7cf887e9d7c2] **No filler.** Never write "The image shows...", "A picture of...", "I can see...".
- [526a0bad384e] Do NOT load this for: pure generation requests where no reference image is given. For those, use the standard model files.