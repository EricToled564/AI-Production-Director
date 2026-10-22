# Prompt aprobado — GPT Image 2

Brief: 6325f2c6f64f26d32d382ba746c76b7226dd96078927a5a7d18e26a88ce0c61c · Prompt: c88d707529c7739e9c386ff61ca7df5cf91033a7ef671821f75002912cd59ffd · Aprobado: 2026-10-22 07:22

## Instrucciones y reglas aplicadas (texto canónico sin alterar)

### 12 reglas universales de redacción

- **U-LABELS**: INV-002334 (skills/image/references/gpt-image.md:7-7): GPT Image 2 сильнее всего реагирует на разделение по секциям. Пиши лейблами, не сплошным текстом.
- **U-ANTI-SLOP**: INV-002340 (skills/image/references/gpt-image.md:32-32): GPT Image 2 особенно чувствителен к качеству формулировок. Vague praise = деградация результата. | INV-002343 (skills/image/references/gpt-image.md:36-36): | stunning, incredible, epic, gorgeous, masterpiece | overcast daylight, brushed aluminum, chipped paint, 50mm feel |
- **U-VISUAL-SPECIFICITY**: INV-002344 (skills/image/references/gpt-image.md:37-37): | «minimalist brutalist luxury photoreal» (стиль-теги) | «cream background, heavy black sans-serif, asymmetrical type block, one hero object, generous negative space» | | INV-002345 (skills/image/references/gpt-image.md:38-38): | «как в Apple-рекламе» | конкретные визуальные факты | | INV-002049 (skills/image/SKILL.md:112-112): Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano Banana). | INV-002257 (skills/image/references/golden-rules.md:34-34): | Subject | "a woman" | "sophisticated elderly woman in vintage Chanel-style suit" | | INV-002258 (skills/image/references/golden-rules.md:35-35): | Material | "shiny" | "brushed steel with matte finish" | | INV-002259 (skills/image/references/golden-rules.md:36-36): | Color | "dark green" | "#0d3d2d deep emerald" | | INV-002260 (skills/image/references/golden-rules.md:37-37): | Position | "on the right" | "right third, bleeding off edge" |
- **U-FUNCTIONAL-REQUIREMENTS**: INV-002346 (skills/image/references/gpt-image.md:39-39): | мудовый язык, в котором тонут функциональные требования | прямое заявление: «image must contain a transit kiosk» |
- **U-OPERATION-VERB**: INV-002241 (skills/image/references/golden-rules.md:8-8): Tell the model the primary operation: "Create", "Generate", "Design", "Transform", "Convert", "Edit". This sets the intent before details.
- **U-POSITIVE-FRAMING**: INV-002243 (skills/image/references/golden-rules.md:12-12): Describe what you WANT, not what you don't want. The model understands presence better than absence. | INV-002335 (skills/image/references/gpt-image.md:9-15): ```
Scene: location, time of day, background, environment
Subject: primary focus — who or what is central
Important Details: materials, textures, lighting, camera angle, mood, composition
Use Case: editorial, product mockup, UI, poster, infographic
Constraints: what must NOT change/appear (no watermarks, preserve face, no extra text)
```
- **U-NATURAL-LANGUAGE**: INV-002253 (skills/image/references/golden-rules.md:27-28): ❌ Bad: "Cool car, neon, city, night, 8k"
✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neon signs reflect off wet pavement and metallic chassis."
- **U-USE-CONTEXT**: INV-002262 (skills/image/references/golden-rules.md:41-41): Context helps model make logical decisions: | INV-002335 (skills/image/references/gpt-image.md:9-15): ```
Scene: location, time of day, background, environment
Subject: primary focus — who or what is central
Important Details: materials, textures, lighting, camera angle, mood, composition
Use Case: editorial, product mockup, UI, poster, infographic
Constraints: what must NOT change/appear (no watermarks, preserve face, no extra text)
```
- **U-MODEL-SEPARATION**: INV-002011 (skills/image/SKILL.md:36-36): If the user named a model — confirm and proceed. If not — pick using the table in `models.md`, then state your choice in the output header. | INV-002044 (skills/image/SKILL.md:88-98): ```
Model: <nano-banana-2 | nano-banana-pro | gpt-image-2>
Quality: <low | medium | high>          (only for gpt-image-2)
Size / Ratio: <e.g. 1536×1024 or 16:9>

Prompt:
<the prompt text, ready to copy>

Notes:
- <anything you inferred or assumed because the user did not specify>
```
- **U-DELIVERY-SEPARATION**: INV-002000 (skills/image/SKILL.md:16-16): This skill writes image prompts. It does not generate images. The output is: model name + quality / size / aspect ratio + the prompt itself. | INV-002044 (skills/image/SKILL.md:88-98): ```
Model: <nano-banana-2 | nano-banana-pro | gpt-image-2>
Quality: <low | medium | high>          (only for gpt-image-2)
Size / Ratio: <e.g. 1536×1024 or 16:9>

Prompt:
<the prompt text, ready to copy>

Notes:
- <anything you inferred or assumed because the user did not specify>
```
- **U-TECHNICAL-ENVELOPE**: INV-002355 (skills/image/references/gpt-image.md:53-53): - Max edge: <3840px | INV-002356 (skills/image/references/gpt-image.md:54-54): - Обе стороны: кратны 16 | INV-002357 (skills/image/references/gpt-image.md:55-55): - Aspect ratio: max 3:1 (long:short) | INV-002358 (skills/image/references/gpt-image.md:56-56): - Total pixels: 655 360 – 8 294 400 | INV-002044 (skills/image/SKILL.md:88-98): ```
Model: <nano-banana-2 | nano-banana-pro | gpt-image-2>
Quality: <low | medium | high>          (only for gpt-image-2)
Size / Ratio: <e.g. 1536×1024 or 16:9>

Prompt:
<the prompt text, ready to copy>

Notes:
- <anything you inferred or assumed because the user did not specify>
```
- **U-QUALITY-ENVELOPE**: INV-002350 (skills/image/references/gpt-image.md:45-45): | `quality: low` | High-volume, превью, exploratory, latency-sensitive, draft | | INV-002351 (skills/image/references/gpt-image.md:46-46): | `quality: medium` | **Default starting point** | | INV-002352 (skills/image/references/gpt-image.md:47-47): | `quality: high` | Маленький/плотный текст, infographics, портреты, identity-sensitive edits, brand assets | | INV-002353 (skills/image/references/gpt-image.md:49-49): Стартуй с `low`, апгрейди по необходимости. Часто `low` уже достаточно. | INV-002044 (skills/image/SKILL.md:88-98): ```
Model: <nano-banana-2 | nano-banana-pro | gpt-image-2>
Quality: <low | medium | high>          (only for gpt-image-2)
Size / Ratio: <e.g. 1536×1024 or 16:9>

Prompt:
<the prompt text, ready to copy>

Notes:
- <anything you inferred or assumed because the user did not specify>
```

### Directivas del usuario

- **USER::ERIC-DELEGATION-TERMS**: Se perdió la prohibición explícita del usuario de photorealistic y fotorealista.
- **USER::ERIC-IDIOMA-PROMPT-INGLES**: en ingles esto es siemore
- **USER::ERIC-BLOQUES-1-2-NO-TOPE**: La expectativa de una o dos reglas por bloque sirve para evaluar los filtros, no para imponer un tope ni excluir reglas válidas.

### Reglas específicas seleccionadas desde el brief

- **SPEC::INV-000028** → Important Details · activa: entrada.accion.evidencia_fisica «Barrido de movimiento leve solo en el volante de inercia» · flujos/flujo-anclas.html: Movimiento descrito: un still es un instante congelado; el movimiento se prompt como su residuo físico.
- **SPEC::INV-000029** → Subject · activa: entrada.sujetos.items[].expresion «determinación, mirada al frente» · flujos/flujo-anclas.html: Vocabulario prohibido: cinematic, epic, stunning, masterpiece, beautiful lighting, emociones nombradas sin cuerpo.
- **SPEC::INV-000123** → Important Details · activa: entrada.pieza.objetivo «a toda velocidad y con expresión de determinación» · flujos/flujo-anclas.html: Un still no puede mostrar movimiento ni emoción: prompt el residuo físico que cada uno deja. Los cuatro ejemplos del brief están cubiertos: el auto de carreras es tipo C, la clavadista entrando al agua es tipo B, el rayo es tipo D, las dos personas en el café son tipo E.
- **SPEC::INV-000551** → Important Details · activa: entrada.color_material.paleta «cian y azul de neón frío» · flujos/flujo-spot.html: verbo inicial · positivo · hex · texto entre comillas
- **SPEC::INV-000613** → Important Details · activa: entrada.accion.tipo «Pedaleo a toda velocidad» · flujos/flujo-spot.html: Movimiento: un still es un instante congelado
- **SPEC::INV-002017** → Important Details · activa: entrada.color_material.paleta «gris concreto» · skills/image/SKILL.md: Universal rules that apply to both models: start with a verb, positive framing, hex colors, quote text, edit don't re-roll, one change per iteration, reference images.
- **SPEC::INV-002040** → Important Details · activa: entrada.escena.planos «Plano medio: S1, S2 y S3 nítidos, en la misma fila» · skills/image/SKILL.md: Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / standard / verbose / cinematic verbose), parameterized templates, output structure with parameters and exclusions.
- **SPEC::INV-002087** → Important Details · activa: entrada.luz.direccion «Tubos de neón lineales en el techo, ligeramente detrás de los ciclistas» · skills/image/references/creative-direction.md: Tell the model exactly how the scene is illuminated.
- **SPEC::INV-002103** → Important Details · activa: entrada.color_material.grade «grano fino de sensor» · skills/image/references/creative-direction.md: Specify camera type to change the visual DNA of the image.
- **SPEC::INV-002125** → Important Details · activa: entrada.camara.lente_intencion «Focal normal, equivalente a 35-50 mm» · skills/image/references/creative-direction.md: > Note: Named lens parameters (50mm, f/2.8) are less reliable than
> descriptive terms. Prefer "shallow depth of field" over "f/1.8".
- **SPEC::INV-002127** → Important Details · activa: entrada.color_material.grade «Grade frío contenido, negros densos sin aplastar, piel con su calidez natural» · skills/image/references/creative-direction.md: Set emotional tone through color and texture.
- **SPEC::INV-002141** → Important Details · activa: entrada.color_material.materiales «concreto aparente con marcas de encofrado» · skills/image/references/creative-direction.md: Define physical makeup of subjects. Don't just say the thing — describe what it's MADE of.
- **SPEC::INV-002299** → Scene · activa: entrada.estilo «fotografía editorial deportiva» · skills/image/references/golden-rules.md: GPT Image 2 обладает глубокими знаниями о культуре, эпохах и визуальных стилях. Вместо описания каждой детали — дай модели культурный/временной/жанровый якорь, и она сама заполнит аутентичные детали.
- **SPEC::INV-002315** → Scene · activa: entrada.estilo «fotografía editorial deportiva» · skills/image/references/golden-rules.md: 1. **Используй как HIGH-LEVEL steering** — якорь задаёт настроение и эстетику, а не заменяет весь промпт
- **SPEC::INV-002316** → Important Details · activa: entrada.escena.espacio «Estudio de spinning de estilo brutalista minimalista, interior» · skills/image/references/golden-rules.md: 2. **Комбинируй с конкретными визуальными деталями** — якорь устанавливает мир, детали устанавливают специфику
- **SPEC::INV-002317** → Use Case · activa: entrada.estilo «fotografía editorial deportiva» · skills/image/references/golden-rules.md: 3. **Не стакай несколько genre anchors** — выбери один. "Peter Lindbergh + Wes Anderson" = каша
- **SPEC::INV-002336** → Constraints · activa: entrada.restricciones «Ningún ciclista toca el asiento» · skills/image/references/gpt-image.md: > «The fifth slot is where most mediocre prompts fail silently.» Без явных constraints модель дрейфует.
- **SPEC::INV-002392** → Scene · activa: entrada.pieza.tematica «Actividades deportivas en la Ciudad de México» · skills/image/references/gpt-image.md: GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не расписывай каждую деталь.
- **SPEC::INV-002394** → Important Details · activa: entrada.operacion «genesis» · skills/image/references/gpt-image.md: - Стартуй с **чистого** базового промпта.
- **SPEC::INV-002400** → Use Case · activa: entrada.pieza.tipo «Fotografía editorial deportiva» · skills/image/references/gpt-image.md: ```
Scene: [location, time, weather]
Subject: [who, action, framing]
Important Details: [lens feel, light source, surface wear, imperfections, real texture]
Use Case: editorial photograph, looks like a real photo
Constraints: no glamorization, no heavy retouching, no studio gloss
```
- **SPEC::INV-002453** → Important Details · activa: entrada.camara.lente_intencion «equivalente a 35-50 mm» · skills/image/references/models.md: | Камера/линза | **Не указывать** числа (50mm, f/2.8) — NB игнорит | Можно «50mm feel», но как high-level look |
- **SPEC::INV-003009** → Subject · activa: entrada.restricciones «El encuadre se centra en los tres ciclistas» · skills/image/references/prompt-framework.md: - **Субъект** - кто/что в центре внимания
- **SPEC::INV-003012** → Subject · activa: entrada.accion.tipo «Pedaleo a toda velocidad en bicicleta fija de spinning, en el momento pico de la clase» · skills/image/references/prompt-framework.md: - **Действие** - что происходит
- **SPEC::INV-003013** → Scene · activa: entrada.escena.espacio «Estudio de spinning de estilo brutalista minimalista, interior» · skills/image/references/prompt-framework.md: - **Окружение** - где это происходит
- **SPEC::INV-003014** → Important Details · activa: entrada.camara.plano «Plano entero de grupo» · skills/image/references/prompt-framework.md: - **Камера** - крупность плана (close-up, wide shot, etc.)
- **SPEC::INV-003015** → Important Details · activa: entrada.luz.fuente «Iluminación de neón fría del estudio» · skills/image/references/prompt-framework.md: - **Освещение** - тип света
- **SPEC::INV-003017** → Important Details · activa: entrada.color_material.materiales «concreto aparente con marcas de encofrado» · skills/image/references/prompt-framework.md: - **Материалы** - текстуры поверхностей
- **SPEC::INV-003018** → Important Details · activa: entrada.color_material.paleta «cian y azul de neón frío» · skills/image/references/prompt-framework.md: - **Палитра** - цвета (лучше hex)
- **SPEC::INV-003019** → parametros · activa: entrada.formato.ratio «16:9» · skills/image/references/prompt-framework.md: - **Формат** - соотношение сторон
- **SPEC::INV-003020** → Important Details · activa: entrada.camara.lente_intencion «Focal normal, equivalente a 35-50 mm» · skills/image/references/prompt-framework.md: > ⚠️ **Параметры объектива** (50mm, 85mm, f/2.8, ISO):
> - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
> - **GPT Image 2** — допускает «50mm feel» как high-level look, но не как точную физическую симуляцию
- **SPEC::INV-003031** → parametros · activa: entrada.formato.ratio «16:9» · skills/image/references/prompt-framework.md: **2. Parameters** - если нестандартные:
- **SPEC::INV-003032** → parametros · activa: entrada.formato.ratio «16:9» · skills/image/references/prompt-framework.md: - Aspect ratio (если не 1:1)
- **SPEC::INV-003034** → Constraints · activa: entrada.restricciones «Ningún ciclista toca el asiento» · skills/image/references/prompt-framework.md: **3. Exclusions** - что исключить (опционально):
- **SPEC::INV-003243** → Constraints · activa: entrada.accion.evidencia_fisica «para que no parezcan copias» · skills/image/references/storyboards.md: - "Only one of each character per image"
- **SPEC::INV-005826** → Subject · activa: entrada.sujetos.items[].expresion «determinación, mirada al frente» · skills/storyboard-architect/references/shot-grammar.md: Generators reward precision. Adjectives describing emotion ("determined", "passionate") produce stock-photo aesthetics. Describe what the camera actually sees.
- **SPEC::INV-011322** → parametros · activa: entrada.formato.ratio «16:9» · skills/visual-prompt-forge/SKILL.md: 6. Append generator-specific parameters (aspect ratio, style flags, seed if applicable)
- **SPEC::INV-011377** → Scene · activa: entrada.camara.plano «Plano entero de grupo» · skills/visual-prompt-forge/SKILL.md: A prompt can be beautifully written and still be impossible to shoot. Every prompt declares, before anything else:
- **SPEC::INV-011378** → Subject · activa: entrada.sujetos.items[].posicion «centro» · skills/visual-prompt-forge/SKILL.md: - **Where the body sits in frame.** Which third it occupies. On a piece that composites two eras with a vertical mask, a body sitting on the centre line gets split in half and no amount of post fixes it. This is the single most expensive failure in the kit, and it is invisible until the mask goes on.
- **SPEC::INV-011379** → Scene · activa: entrada.camara.angulo «Frontal, desplazado unos 15° del eje, ligeramente contrapicado» · skills/visual-prompt-forge/SKILL.md: - **The point of view.** Profile, frontal, side, rear. "A man walking" is not a shot.
- **SPEC::INV-011381** → Constraints · activa: entrada.camara.plano «Plano entero de grupo» · skills/visual-prompt-forge/SKILL.md: - **Nothing that contradicts the camera.** A subject who walks away from camera cannot also keep the same size in frame.
- **SPEC::INV-011383** → Constraints · activa: entrada.sujetos.items[].vestuario «ropa deportiva de alta gama, negra» · skills/visual-prompt-forge/SKILL.md: - **No brand marks.** Logos and lettering are composited in post. Generators deform them.
- **SPEC::INV-011416** → Constraints · activa: entrada.blocking.relaciones «Separación entre bicicletas suficiente para que ningún cuerpo tape a otro» · skills/visual-prompt-forge/SKILL.md: - **Rule 6**: every shot states which third of the frame the body occupies, its point of
  view and its direction of travel; no scale contradictions, no two people at the same
  frame edge, no unnamed handedness in a two-person contact, no brand marks in frame
- **SPEC::INV-011422** → Important Details · activa: entrada.accion.estado_visible «Los tres de pie sobre los pedales, sin tocar el asiento» · skills/visual-prompt-forge/SKILL.md: - [ ] The prompt actually describes the shot, which is the part no validator will ever do
- **SPEC::INV-011730** → Use Case · activa: entrada.estilo «fotografía editorial deportiva» · skills/visual-prompt-forge/adapters/gpt-image.md: | `style` | `natural` for photoreal, `vivid` for stylized | |
- **SPEC::INV-011737** → Scene · activa: entrada.blocking.relaciones «S2 en el eje central, ligeramente adelantado, como figura dominante; S1 y S3 a los lados» · skills/visual-prompt-forge/adapters/gpt-image.md: GPT Image's distinctive capability, describe spatial relationships explicitly:
- **SPEC::INV-011741** → Scene · activa: entrada.composicion «Simetría central con S2 en el eje vertical; S1 a la izquierda y S3 a la derecha» · skills/visual-prompt-forge/adapters/gpt-image.md: Use this when the shot's composition is load-bearing.
- **SPEC::INV-011757** → Scene · activa: entrada.escena.planos «Plano medio: S1, S2 y S3 nítidos, en la misma fila» · skills/visual-prompt-forge/adapters/gpt-image.md: - **Don't omit spatial language when the shot has specific composition**, you're paying for the model's strength; use it
- **SPEC::INV-011758** → Scene · activa: entrada.escena.planos «Fondo: asistentes sin rostro legible, desenfocados y en penumbra, filas de bicicletas, muro de concreto con tubos de neón» · skills/visual-prompt-forge/adapters/gpt-image.md: - **Don't pile too many objects**, five or fewer distinct elements per scene; more degrades fidelity
- **SPEC::INV-011759** → parametros · activa: entrada.formato.ratio «16:9» · skills/visual-prompt-forge/adapters/gpt-image.md: - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
- **SPEC::INV-011760** → Important Details · activa: entrada.color_material.acabado «piel sin retoque, sin brillo plástico» · skills/visual-prompt-forge/adapters/gpt-image.md: - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't a complete fix. For pure photoreal, Flux is still stronger
- **SPEC::INV-012287** → Important Details · activa: entrada.camara.lente_intencion «Focal normal, equivalente a 35-50 mm» · skills/visual-prompt-forge/references/failure-modes.md: - Add specific lens and aperture ("50mm prime, f/2.0")
- **SPEC::INV-012289** → Important Details · activa: entrada.color_material.acabado «grano fino, piel sin retoque» · skills/visual-prompt-forge/references/failure-modes.md: - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
- **SPEC::INV-012830** → Scene · activa: entrada.camara.angulo «Frontal, desplazado unos 15° del eje, ligeramente contrapicado» · skills/visual-prompt-forge/tools/validate_prompts.py:     # Rule 9: shot logic. Each check here is a failure a director had to catch by hand.
    for sid, body in blocks:
        low_b = body.lower()
        logic = [
            (not any(k in low_b for k in ["profile", "facing camera", "facing frame",
                                          "from the side", "rear", "three quarter",
                                          "seen from", "overhead", "top down"]),
             "does not declare a point of view (profile / frontal / side)"),
            (not any(k in low_b for k in ["left to right", "right to left", "frame right",
                                          "frame left", "towards the camera", "toward the camera",
                                          "away from the camera", "no person", "empty", "still",
                                          "static camera", "locked off"]),
             "does not declare a direction of travel"),
            (any(k in low_b for k in ["deeper into", "walks away", "further into",
                                      "towards the back", "receding"])
             and any(k in low_b for k in ["same size", "same height", "two thirds of frame"]),
             "is impossible: the subject moves away from camera and keeps the same size in frame"),
            ((low_b.count("right edge") >= 2 or low_b.count("left edge") >= 2)
             and "second man" in low_b,
             "puts two people at the same frame edge"),
            (any(k in low_b for k in ["high five", "palm", "slap hands", "hands meet"])
             and not ("left hand" in low_b and "right hand" in low_b),
             "describes a two-handed interaction without naming which hand each person raises"),
            (any(k in low_b for k in ["logo", "lettering", "brand wall"])
             and not any(k in low_b for k in ["no logo", "no lettering", "bare", "plain wall"]),
             "puts brand marks in frame; logos are composited in post, never generated"),
            ((("crossing" in low_b or "crosses the" in low_b)
              or "anchor" in low_b or True)
             and not any(k in low_b for k in ["left third", "right third", "centre third",
                                              "no person", "empty", "black frame"]),
             "does not state which third of the frame the body occupies; a body on the centre "
             "line is split in half by the mask"),
            (("crossing" in low_b or "crosses the" in low_b)
             and not any(k in low_b for k in ["centre stays", "centre strip", "clear of any object",
                                              "away from the centre", "far from the centre"]),
             "is a crossing shot but does not declare the centre of frame clear for the mask"),
        ]
        for failed, reason in logic:
            if failed:
                if _is_fixture(body):
                    warnings.append(f"{label}: {sid} {reason}")
                else:
                    errors.append(f"{label}: {sid} {reason}")

## Salida

```text
Model: GPT Image 2
Quality: high
Size / Ratio: 16:9

Prompt:
Scene: Create a 16:9 landscape sports editorial reportage photograph inside a brutalist minimalist indoor spinning studio in Mexico City, at the peak sprint of a class, in an interior with no daylight. A static camera at handlebar height, about 1 m above the floor, faces the row straight on along the central axis; that low position gives a slight upward angle. It frames a full group shot that runs from a strip of ceiling with neon tubes above the heads down to the bike bases on the floor. The bikes are stationary and face the camera, so nobody travels across the frame. The depth builds in three planes. In the foreground, the dark, out-of-focus edge of a neighboring bike's handlebar sits in one lower corner. In the midground, the three featured riders share one row of parallel stationary bikes facing the same direction, the middle bike half a step ahead of the other two, with enough space between the bikes that no body covers another. In the background, attendees on their bikes form one soft, dim mass, with rows of black bikes and a concrete wall carrying linear neon tubes.
Subject: Three cyclists frozen at the peak of a full-speed sprint, each standing on the pedals with the body leaning slightly forward, both hands gripping the handlebar, feet secured firmly to the pedals and the bikes firmly anchored to the floor. On the first bike of the row, nearest the left side wall and its vertical neon bar, rides a 23-year-old Mediterranean man with blond hair and defined, lean musculature, in high-end black sportswear; his right pedal is at the bottom of the stroke and his right leg is nearly extended. On the middle bike, directly beneath the point where the ceiling neon lines converge, rides the dominant figure: a 32-year-old Mexican man with brown skin, short black hair shaved on the sides, a short full beard, a muscular build and black fine-line tattoos covering both forearms and upper arms, in a high-end black sleeveless top and black athletic shorts that leave the tattoos visible; his right pedal is forward at the three o'clock position and he drives it down with his weight. On the third bike, on the side away from the neon bar, rides a 27-year-old Mediterranean woman with a slim, toned body and long light-brown hair tied in a ponytail that swings sideways with the motion, in high-end black sportswear; her right pedal is at the top of the stroke and her right knee is flexed. These three different crank positions keep the poses from matching. All three faces show clenched teeth with lips parted by hard breathing, lowered brows and a fixed gaze straight ahead; the three gazes run parallel in the same direction.
Important Details: A slight motion blur appears only on the three flywheels, while pedals, shoes, torsos, arms and faces stay sharp. Sweat sits as discrete specular points on foreheads, temples, necks and arms rather than as uniformly wet skin; forearms and hand tendons are taut from the grip; black technical fabric pulls taut across shoulders and thighs, with creases at the elbows and hips. The image reads as taken with a full-frame digital press camera and a normal 35-50mm lens feel that keeps the outer riders undistorted, with a medium depth of field that holds all three riders sharp in the same focal plane while the background falls into soft bokeh. The only light comes from cold neon practicals. Linear neon tubes on the ceiling, slightly behind the riders, draw a rim of light along heads and shoulders, and a vertical neon bar on the left side wall models the faces from about 45 degrees. The light is semi-hard, from narrow linear sources, with defined shadow edges and no soft frontal fill. The three riders sit in the brightest zone, light falls off toward the frame edges and the background, and about 60 percent of the frame stays in shadow with the tubes visible. Contrast is high and natural, with deep, dense blacks that keep detail in the dark clothing and bikes without crushing. Linear specular reflections of the tubes run across the sweat, the bike frames and the satin sheen of the technical fabric. The palette holds near-black #0B0B0D, concrete gray #8A8C8A, cold neon cyan #34D6E8, cold neon blue #2F5BFF and cold white #E8F1F7 around natural skin tones, under a restrained cool grade in which the skin keeps its natural warmth, with fine sensor grain. Surfaces are board-formed exposed concrete with formwork marks, steel, latest-generation black stationary bikes with satin frames, black technical sportswear with visible mesh and compression knit, and a black rubber floor with its surface texture; the skin shows body hair and tattoo ink settled into it. The composition is symmetrical about the central axis, with dark negative space along the top strip. Natural skin texture, no AI rendering artifacts.
Use Case: Image for a web reportage on the city's sports activities, showing the peak moment of a spinning class; it looks like a real photo and fills the whole frame, with no space reserved for a headline.
Constraints: None of the three riders touches the saddle. The first rider's muscle volume stays moderate, never bodybuilder bulk. The background class is full but never crowded, with visible gaps between the bikes. The frame centers on the three riders, and background attendees show no legible faces. Each of the three riders appears exactly once, and no background attendee repeats their features or becomes their clone. No rider is cut by or pressed against a frame edge. The middle rider appears only slightly larger than the other two, never disproportionately, and facial detail stays at the level resolvable at this distance. No logos, lettering or text on clothing, shoes, bikes or walls. No glamorization, no heavy retouching, no studio gloss or plastic sheen on the skin, no HDR look.
```

## Texto para copiar en el generador

```text
Scene: Create a 16:9 landscape sports editorial reportage photograph inside a brutalist minimalist indoor spinning studio in Mexico City, at the peak sprint of a class, in an interior with no daylight. A static camera at handlebar height, about 1 m above the floor, faces the row straight on along the central axis; that low position gives a slight upward angle. It frames a full group shot that runs from a strip of ceiling with neon tubes above the heads down to the bike bases on the floor. The bikes are stationary and face the camera, so nobody travels across the frame. The depth builds in three planes. In the foreground, the dark, out-of-focus edge of a neighboring bike's handlebar sits in one lower corner. In the midground, the three featured riders share one row of parallel stationary bikes facing the same direction, the middle bike half a step ahead of the other two, with enough space between the bikes that no body covers another. In the background, attendees on their bikes form one soft, dim mass, with rows of black bikes and a concrete wall carrying linear neon tubes.
Subject: Three cyclists frozen at the peak of a full-speed sprint, each standing on the pedals with the body leaning slightly forward, both hands gripping the handlebar, feet secured firmly to the pedals and the bikes firmly anchored to the floor. On the first bike of the row, nearest the left side wall and its vertical neon bar, rides a 23-year-old Mediterranean man with blond hair and defined, lean musculature, in high-end black sportswear; his right pedal is at the bottom of the stroke and his right leg is nearly extended. On the middle bike, directly beneath the point where the ceiling neon lines converge, rides the dominant figure: a 32-year-old Mexican man with brown skin, short black hair shaved on the sides, a short full beard, a muscular build and black fine-line tattoos covering both forearms and upper arms, in a high-end black sleeveless top and black athletic shorts that leave the tattoos visible; his right pedal is forward at the three o'clock position and he drives it down with his weight. On the third bike, on the side away from the neon bar, rides a 27-year-old Mediterranean woman with a slim, toned body and long light-brown hair tied in a ponytail that swings sideways with the motion, in high-end black sportswear; her right pedal is at the top of the stroke and her right knee is flexed. These three different crank positions keep the poses from matching. All three faces show clenched teeth with lips parted by hard breathing, lowered brows and a fixed gaze straight ahead; the three gazes run parallel in the same direction.
Important Details: A slight motion blur appears only on the three flywheels, while pedals, shoes, torsos, arms and faces stay sharp. Sweat sits as discrete specular points on foreheads, temples, necks and arms rather than as uniformly wet skin; forearms and hand tendons are taut from the grip; black technical fabric pulls taut across shoulders and thighs, with creases at the elbows and hips. The image reads as taken with a full-frame digital press camera and a normal 35-50mm lens feel that keeps the outer riders undistorted, with a medium depth of field that holds all three riders sharp in the same focal plane while the background falls into soft bokeh. The only light comes from cold neon practicals. Linear neon tubes on the ceiling, slightly behind the riders, draw a rim of light along heads and shoulders, and a vertical neon bar on the left side wall models the faces from about 45 degrees. The light is semi-hard, from narrow linear sources, with defined shadow edges and no soft frontal fill. The three riders sit in the brightest zone, light falls off toward the frame edges and the background, and about 60 percent of the frame stays in shadow with the tubes visible. Contrast is high and natural, with deep, dense blacks that keep detail in the dark clothing and bikes without crushing. Linear specular reflections of the tubes run across the sweat, the bike frames and the satin sheen of the technical fabric. The palette holds near-black #0B0B0D, concrete gray #8A8C8A, cold neon cyan #34D6E8, cold neon blue #2F5BFF and cold white #E8F1F7 around natural skin tones, under a restrained cool grade in which the skin keeps its natural warmth, with fine sensor grain. Surfaces are board-formed exposed concrete with formwork marks, steel, latest-generation black stationary bikes with satin frames, black technical sportswear with visible mesh and compression knit, and a black rubber floor with its surface texture; the skin shows body hair and tattoo ink settled into it. The composition is symmetrical about the central axis, with dark negative space along the top strip. Natural skin texture, no AI rendering artifacts.
Use Case: Image for a web reportage on the city's sports activities, showing the peak moment of a spinning class; it looks like a real photo and fills the whole frame, with no space reserved for a headline.
Constraints: None of the three riders touches the saddle. The first rider's muscle volume stays moderate, never bodybuilder bulk. The background class is full but never crowded, with visible gaps between the bikes. The frame centers on the three riders, and background attendees show no legible faces. Each of the three riders appears exactly once, and no background attendee repeats their features or becomes their clone. No rider is cut by or pressed against a frame edge. The middle rider appears only slightly larger than the other two, never disproportionately, and facial detail stays at the level resolvable at this distance. No logos, lettering or text on clothing, shoes, bikes or walls. No glamorization, no heavy retouching, no studio gloss or plastic sheen on the skin, no HDR look.
```

## Inferencias y supuestos (fuera del texto visual)

- entrada.modelo.nombre: "GPT Image" (inferido)
- entrada.modelo.version: "2" (inferido)
- entrada.sujetos.items[].id: ["S1", "S2", "S3"] (inferido)
- entrada.escena.planos: ["Primer plano: borde de un manubrio o de una bicicleta vecina, oscuro y desenfocado, en una esquina inferior", "Plano medio: S1, S2 y S3 nítidos, en la misma fila", "Fondo: asistentes sin rostro legible, desenfocados y en penumbra, filas de bicicletas, muro de concreto con tubos de neón"] (propuesta_aceptada)
- entrada.representacion: ["fotografía"] (inferido)
- entrada.blocking.relaciones: ["Los tres en la misma fila, bicicletas paralelas y orientadas al mismo frente", "S2 en el eje central, ligeramente adelantado, como figura dominante; S1 y S3 a los lados", "Separación entre bicicletas suficiente para que ningún cuerpo tape a otro", "Las tres miradas al frente en la misma dirección, sin cruzarse"] (propuesta_aceptada)
- entrada.camara.angulo: "Frontal, desplazado unos 15° del eje, ligeramente contrapicado" (propuesta_aceptada)
- entrada.camara.altura: "Cámara a unos 1 m del piso, a la altura de los manubrios" (propuesta_aceptada)
- entrada.camara.lente_intencion: "Focal normal, equivalente a 35-50 mm, a distancia suficiente para no deformar a los ciclistas de los extremos" (propuesta_aceptada)
- entrada.luz.direccion: "Tubos de neón lineales en el techo, ligeramente detrás de los ciclistas, que dibujan un borde de luz en cabeza y hombros, y una barra de neón vertical en el muro lateral izquierdo que modela los rostros desde unos 45°" (propuesta_aceptada)
- entrada.luz.dureza: "Semidura: fuentes lineales estrechas con bordes de sombra definidos y especulares lineales, sin relleno frontal suave" (propuesta_aceptada)
- entrada.luz.distribucion: "Los tres ciclistas en la zona más iluminada; caída de luz hacia los extremos y el fondo; cerca del 60% del cuadro en penumbra con los tubos visibles" (propuesta_aceptada)
- entrada.luz.contraste: "Alto contraste natural: negros profundos con detalle en la ropa negra y en las bicicletas, sin aspecto HDR" (propuesta_aceptada)
- entrada.luz.specular: "Especulares lineales de los tubos reflejados en el sudor, en los cuadros negros de las bicicletas y en el brillo satinado de la tela técnica" (propuesta_aceptada)
- entrada.color_material.paleta: ["negro", "gris concreto", "cian y azul de neón frío", "blanco frío", "tonos de piel naturales"] (propuesta_aceptada)
- entrada.color_material.grade: "Grade frío contenido, negros densos sin aplastar, piel con su calidez natural, grano fino de sensor" (propuesta_aceptada)
- entrada.color_material.acabado: "Acabado de fotografía de reportaje editorial: grano fino, piel sin retoque, sin brillo plástico" (propuesta_aceptada)
- entrada.composicion: ["Simetría central con S2 en el eje vertical; S1 a la izquierda y S3 a la derecha", "Las líneas de los tubos de neón del techo convergen hacia el centro", "Espacio negativo oscuro en la franja superior", "Las fases de pedalada desfasadas rompen la simetría de las poses"] (propuesta_aceptada)

## Notas del redactor

- Aviso de fidelidad (INV-011758): la escena supera los cinco elementos distintos (tres ciclistas con sus bicicletas, manubrio en primer plano, asistentes del fondo, filas de bicicletas, muro de concreto con neón). Se agrupó el fondo como una sola masa en penumbra, pero GPT Image 2 puede perder fidelidad en algún elemento; revisar al 100% rostros, manos, pies y bielas.
- Cambio de esta ronda: cámara frontal en el eje central (se retiró el desplazamiento de unos 15°); el leve contrapicado se atribuye a la altura de 1 m. Con ello se conserva la simetría; la convergencia de los tubos del techo queda como ancla de la bicicleta central.
- Cambio de esta ronda: los ciclistas ya no se ubican por 'left/centre/right third' sino por anclas de la escena (primera bicicleta junto al muro izquierdo y su barra de neón vertical, bicicleta central bajo la convergencia de los tubos, tercera bicicleta del lado opuesto a la barra). Esto deja de cumplir la palabra clave de tercios del validador INV-012830; se prioriza la decisión del usuario.
- Se retiró 'pass just beside the lens' de la mirada: dependía del desplazamiento de 15°, ya eliminado. La mirada queda 'fixed gaze straight ahead', paralela en los tres.
- El ratio 16:9 se pide dentro del texto porque la app de ChatGPT para escritorio no expone parámetro de tamaño; quality high no se puede fijar en la app y se registra como parámetro de referencia.
- Supuesto heredado: las coordenadas hex de la paleta son la traducción del redactor a colores nombrados en el brief (negro, gris concreto, cian y azul neón, blanco frío).

## Trazabilidad de la verificación

- U-LABELS: PASS — El prompt está dividido en cinco secciones rotuladas (Scene, Subject, Important Details, Use Case, Constraints); no es un bloque continuo sin rótulos.
- U-ANTI-SLOP: PASS — No hay elogio vago ni superlativos vacíos (stunning, epic, masterpiece, etc.). "high-end" y "latest-generation" vienen literalmente del usuario ("alta gama", "última generación") y acompañan descripciones concretas (negro, cuadro satinado), no sustituyen una instrucción visual.
- U-VISUAL-SPECIFICITY: PASS — El estilo brutalista se traduce a propiedades observables (concreto con marcas de encofrado, acero, tubos de neón lineales, paleta en hex, posiciones por ancla); no hay comparaciones externas ni pila de etiquetas de estilo.
- U-FUNCTIONAL-REQUIREMENTS: PASS — Todos los requisitos del brief están declarados de forma directa: tres ciclistas con edad, género y rasgos, ropa negra de alta gama, de pie sin tocar el asiento ("None of the three riders touches the saddle"), ambas manos en el manubrio, pies sujetos a los pedales, bicicletas ancladas al piso, estudio brutalista minimalista con neón frío, fondo de clase llena no abarrotada, 16:9, reportaje web sin espacio para titular. Las bielas siguen la decisión del usuario: izquierda abajo con pierna casi extendida, centro a las tres empujando con el peso, derecha arriba con rodilla flexionada; la frase común que las igualaba ya no está.
- U-OPERATION-VERB: PASS — La primera instrucción operativa abre con el verbo "Create", dentro del rótulo Scene.
- U-POSITIVE-FRAMING: PASS — Los estados deseados se describen en positivo; las negaciones fuera de Constraints ("no daylight", "no soft frontal fill", "rather than as uniformly wet skin") acompañan una descripción positiva y no la sustituyen. Las prohibiciones del usuario y del caso quedan en Constraints, como prescribe INV-002335.
- U-NATURAL-LANGUAGE: PASS — Las secciones están en prosa con relaciones visuales inteligibles; no hay listas de palabras clave sueltas.
- U-USE-CONTEXT: PASS — El uso del brief (reportaje web sobre actividades deportivas en la CDMX, sin espacio para titular) se conserva sin sustituirlo por otro.
- U-MODEL-SEPARATION: PASS — La entrega identifica el modelo solicitado en el encabezado y el texto visual no mezcla el contrato del modelo.
- U-DELIVERY-SEPARATION: PASS — La entrega trae modelo, quality, Size / Ratio, el prompt copiable e inferencias/supuestos en una lista aparte; el texto visual no contiene notas operativas. Observación: la lista de inferencias aún muestra el ángulo "desplazado unos 15° del eje" del brief, pero las notas del redactor explican que se retiró por decisión del usuario, así que la entrega no oculta el cambio.
- U-TECHNICAL-ENVELOPE: PASS — Revisado solo el ratio entregado: 16:9 (1,78:1) está dentro del máximo 3:1 y coincide con lo pedido por el usuario. No se entregan dimensiones en píxeles (la app de escritorio no las expone), lo que no es falla; no se afirma cumplimiento en píxeles.
- U-QUALITY-ENVELOPE: PASS — La quality va como metadato fuera del texto visual. "high" corresponde al uso documentado para retratos e identidad: tres rostros distinguibles, manos y tatuajes a escala pequeña. El usuario no fijó otra quality y las notas aclaran que la app no permite fijarla, así que queda como parámetro de referencia.
- PACK::GPT2-GEN::1: PASS — Solo existen las cinco etiquetas del esquema. Los sub-rótulos internos (Camera:, Lighting:, etc.) pasaron a prosa como decidió el usuario. Los dos puntos de "rides the dominant figure:" introducen una aposición dentro de una oración y no forman una etiqueta.
- PACK::GPT2-GEN::2: PASS — El verbo de operación está dentro de la primera sección y nada lo antecede antes del rótulo Scene.
- PACK::GPT2-GEN::3: PASS — Los requisitos funcionales y las restricciones reales del brief se conservan. No se metieron datos administrativos (referencias, rondas, validadores) ni ejemplos de fuente ajenos. El cierre de piel y la plantilla editorial vienen de reglas seleccionadas.
- USER::ERIC-DELEGATION-TERMS: PASS — Los términos "photorealistic" y "fotorealista" no aparecen en el prompt ni en la entrega. La intención realista se expresa como "looks like a real photo", y la prohibición sigue explícita en entrada.restricciones.
- USER::ERIC-IDIOMA-PROMPT-INGLES: PASS — Todo el prompt está en inglés.
- USER::ERIC-BLOQUES-1-2-NO-TOPE: PASS — La directiva gobierna cómo se evalúan los filtros, no el texto. Revisado: ninguna regla válida se excluyó por superar dos reglas por bloque; Important Details aplica muchas reglas sin bloquear ninguna.
- LLENADO::Scene: PASS — Scene abre con el verbo y resuelve espacio, momento (sprint pico, interior sin luz diurna), temática (clase de spinning, CDMX), entorno y los tres planos. El clima no aplica.
- LLENADO::Subject: PASS — Subject cubre cantidad, posición de cada ciclista por ancla, edad, género, rasgos, cabello, vestuario, expresión traducida a señales físicas, postura, contactos y relaciones. La identidad no aplica.
- LLENADO::Important Details: PASS — Important Details concreta efecto óptico, lente, tipo de cámara, luz completa (fuente, dirección, dureza, distribución, contraste, especulares), paleta, grade, materiales, texturas, piel y composición. Plano, ángulo y altura de cámara quedaron en Scene porque INV-011377 pide fijar antes la lógica rodable; están dichos una vez y no se pierden.
- LLENADO::Use Case: PASS — Declara el uso (reportaje web de deportes en la ciudad), el tipo fotográfico y la condición del destino (sin espacio para titular), tal como quedaron en el brief.
- LLENADO::Constraints: PASS — Constraints lista las restricciones del brief (asiento, volumen de S1, clase no abarrotada, encuadre en los tres) y las protecciones del caso (sin clones, sin rostros legibles al fondo, escala, bordes, sin texto ni logos, sin HDR). No incluye datos administrativos ni una lista genérica de negativos.
- SPEC::INV-000028: PASS — El still se plantea como instante congelado ("frozen at the peak") con residuos físicos: volantes barridos, sudor especular, tendones tensos, tela tirante, bielas desfasadas. "swings sideways" y "drives it down" describen el estado de fuerza dentro del instante y no piden una secuencia.
- SPEC::INV-000029: PASS — No aparecen cinematic, epic, stunning, masterpiece ni beautiful lighting, y la emoción "determinación" no se nombra: se dan señales corporales.
- SPEC::INV-000123: PASS — La velocidad y el esfuerzo se expresan por su residuo físico congelado (volantes barridos, bielas desfasadas, tela tensa, tendones, rostro con señales físicas), no por nombres de movimiento o emoción.
- SPEC::INV-000551: PASS — Los colores dominantes llevan nombre y valor hex. Las notas declaran que el hex es traducción del redactor. No hay texto en imagen, así que la parte de comillas no aplica.
- SPEC::INV-000613: PASS — El sprint se describe como instante congelado: postura de pie, tres posiciones de biela fijas y su consecuencia visible (volantes barridos, peso sobre el pedal). Ningún verbo de proceso pide una secuencia.
- SPEC::INV-002017: PASS — La parte activada (colores en hex) se cumple: la paleta declarada lleva valores hex junto al nombre.
- SPEC::INV-002040: PASS — Cada elemento del checklist está en su slot y una sola vez: sujeto, contexto, acción, entorno, cámara, luz, tono por color y textura, materiales, paleta y formato (16:9).
- SPEC::INV-002087: PASS — La iluminación se declara con exactitud: fuente, posición, función, dureza y caída a penumbra.
- SPEC::INV-002103: PASS — Nombra de forma descriptiva y sin marca el tipo de cámara: digital de prensa de sensor completo.
- SPEC::INV-002125: PASS — La óptica se describe como sensación y efecto (sin distorsión en los extremos, profundidad de campo media, bokeh) y sin f-stops, como decidió el usuario. La sensación en mm la admite INV-002453 para GPT Image 2.
- SPEC::INV-002127: PASS — El tono se fija con color y textura (grade frío contenido, piel cálida, negros densos, grano fino), no con adjetivos de ánimo.
- SPEC::INV-002141: PASS — Describe de qué están hechas las superficies: concreto con encofrado, acero, cuadros satinados, tela técnica de malla y compresión, caucho.
- SPEC::INV-002299: PASS — Da un solo ancla de género, reportaje editorial deportivo, para que el modelo complete detalles auténticos. El ancla de ciudad la pide INV-002392 por decisión del usuario.
- SPEC::INV-002315: PASS — El ancla de género da dirección general y no sustituye la descripción concreta del estudio, los sujetos ni la luz.
- SPEC::INV-002316: PASS — El ancla se combina con detalles visuales concretos: concreto, neón lineal, filas de bicicletas negras, piso de caucho.
- SPEC::INV-002317: PASS — Hay un solo ancla de género, sin otros géneros ni nombres de autor o fotógrafo.
- SPEC::INV-002336: PASS — El slot Constraints es explícito: restricciones del usuario más protecciones del caso (sin clones, sin rostros legibles al fondo, sin texto ni logos).
- SPEC::INV-002392: PASS — El ancla Mexico City aparece en Scene, como decidió el usuario.
- SPEC::INV-002394: PASS — El prompt base quedó limpio según la decisión del usuario: cada indicación va una vez en su bloque (barrido solo en Important Details, separación entre bicicletas solo en Scene) y Constraints solo lleva prohibiciones e invariantes que no se dijeron antes; el aviso de escala no repite el medio paso de Scene.
- SPEC::INV-002400: PASS — Sigue la plantilla editorial: Use Case "looks like a real photo"; Important Details con sensación de lente, fuente de luz, texturas reales; Constraints con "no glamorization, no heavy retouching, no studio gloss". No usa "photorealistic".
- SPEC::INV-002453: PASS — La focal se nombra como look de alto nivel y no lleva cifras de diafragma ni ISO: "f/4-style" se quitó como decidió el usuario.
- SPEC::INV-003009: PASS — Subject abre con los tres ciclistas como foco y deja la clase del fondo como entorno.
- SPEC::INV-003012: PASS — La acción se declara como instante congelado del sprint de pie, no como pose estática.
- SPEC::INV-003013: PASS — Scene describe el estudio interior antes que los sujetos.
- SPEC::INV-003014: PASS — El tamaño de plano se nombra: plano entero de grupo, desde el techo hasta la base de las bicicletas.
- SPEC::INV-003015: PASS — La luz se declara como neón frío práctico, con su dirección y dureza.
- SPEC::INV-003017: PASS — Nombra los materiales del brief: concreto con encofrado, acero, cuadros satinados, tela técnica, caucho.
- SPEC::INV-003018: PASS — La paleta aceptada lleva colores concretos y no "colores cinematográficos".
- SPEC::INV-003019: PASS — El 16:9 se declara dentro del texto, porque la app no tiene parámetro de tamaño, y también en el campo Size / Ratio de la entrega.
- SPEC::INV-003020: PASS — Usa la sensación en mm como look general, sin f/ ni ISO; se quitó "f/4-style" como decidió el usuario.
- SPEC::INV-003031: PASS — El bloque de parámetros de la entrega lista el formato no estándar 16:9.
- SPEC::INV-003032: PASS — El aspect ratio distinto de 1:1 está en parámetros y también se pide en el texto.
- SPEC::INV-003034: PASS — Las exclusiones del brief están en Constraints: asiento, volumen muscular de S1 y clase no abarrotada, esta última en positivo ("full but never crowded, with visible gaps").
- SPEC::INV-003243: PASS — Exige que cada personaje aparezca una sola vez y prohíbe clones entre los asistentes del fondo.
- SPEC::INV-005826: PASS — No escribe "determined" ni otro adjetivo de emoción; describe lo que ve la cámara (dientes apretados, labios separados, cejas bajas, mirada fija, sudor especular).
- SPEC::INV-011322: PASS — El 16:9 se pide en lenguaje dentro del texto y no se añaden seed, flags ni el parámetro size de la API, que la app no soporta.
- SPEC::INV-011377: PASS — La lógica rodable (cámara física a 1 m, punto de vista, plano entero, posición de cada bicicleta, contactos) se fija al inicio, antes de la atmósfera y la luz. La primera oración solo sitúa el lugar.
- SPEC::INV-011378: PASS — Cada cuerpo se ubica en el cuadro con anclas legibles de la escena (muro izquierdo y su barra de neón, convergencia de los tubos, lado opuesto a la barra) en lugar de tercios, como decidió el usuario. La composición simétrica sobre el eje completa la ubicación.
- SPEC::INV-011379: PASS — Nombra el punto de vista: frontal, en el eje central, con leve contrapicado por la altura de 1 m. Se retiró el desplazamiento de 15° por decisión del usuario.
- SPEC::INV-011381: PASS — La escala es coherente con la cámara: el medio paso de adelanto produce un tamaño solo algo mayor, con la formulación que decidió el usuario. La cámara frontal en el eje conserva la simetría y la convergencia central, y el contrapicado se atribuye a la altura de 1 m.
- SPEC::INV-011383: PASS — No hay marcas en cuadro, como decidió el usuario.
- SPEC::INV-011416: PASS — Declara punto de vista, ubicación por ancla (decisión del usuario en lugar de tercios), ausencia de desplazamiento ("nobody travels across the frame") y escala coherente, y ningún ciclista queda contra un borde. Las cláusulas de lateralidad entre dos personas no se activan.
- SPEC::INV-011422: PASS — El prompt describe de verdad este plano: de pie fuera del asiento, manos en el manubrio, pies en los pedales, bicicletas ancladas, bielas desfasadas y fondo sin rostros legibles.
- SPEC::INV-011730: PASS — La intención natural y fotográfica se expresa en palabras, sin inventar un parámetro style y sin "photorealistic".
- SPEC::INV-011737: PASS — Las relaciones espaciales van explícitas: misma fila paralela, bicicleta central medio paso adelante, separación para que nadie tape a nadie, foreground en una esquina inferior.
- SPEC::INV-011741: PASS — La composición portante (simetría central, convergencia de los tubos, espacio negativo superior) va con lenguaje espacial explícito.
- SPEC::INV-011757: PASS — Cada uno de los tres planos lleva su posición concreta: primer plano en una esquina inferior, fila de los tres al medio, fondo con asistentes y muro.
- SPEC::INV-011758: PASS — El fondo se agrupa como una sola masa subordinada. El aviso de fidelidad por más de cinco elementos está en las notas de la entrega y no en el texto visual, como decidió el usuario.
- SPEC::INV-011759: PASS — No hay flags --ar ni sintaxis de pesos; la proporción va en lenguaje dentro del prompt, como decidió el usuario.
- SPEC::INV-011760: PASS — La línea de cierre contra el "AI look" está al final de Important Details y se refiere a la piel.
- SPEC::INV-012287: PASS — La focal del brief se concreta. La apertura se omitió por la decisión del usuario sobre el choque con INV-002453 e INV-003020 ("quitar 'f/4-style'; describir la profundidad de campo sin cifras"), y la profundidad media se describe sin número.
- SPEC::INV-012289: PASS — Incluye la línea de cierre "natural skin texture, no AI rendering artifacts".
- SPEC::INV-012830: PASS — Declara el punto de vista (frontal en el eje: "faces the row straight on along the central axis") y que no hay desplazamiento ("static camera", "nobody travels across the frame"). Las cláusulas de tercio, máscara, cruce y choque de manos no se activan según la regla; la ubicación por tercios se sustituyó por anclas por decisión del usuario.
