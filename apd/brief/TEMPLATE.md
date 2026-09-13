# Brief template de imagen — el mismo para crear y para extraer de una imagen

> Generado por `apd/brief/gen_template.py` desde `.claude/rules/v3/case-fingerprint.schema.json`.
> No se edita a mano: si el schema gana una dimensión, este archivo gana su pregunta en la
> siguiente corrida. Se desfasó una vez y costó 41 reglas muertas del lado imagen.

> **APROBADO por Eric, 2026-09-13: "EL TEMPLATE ESTA APROBADO".** Las 14 dimensiones de la
> parte 2 quedan autorizadas a entrar al schema; eso obliga a republicar el ruleset.

> **Alcance: sólo imagen.** Video queda para después, por decisión de Eric. Las dimensiones
> de audio, secuencia y movimiento de cámara no se preguntan todavía; siguen en el schema.

## Cómo se usa

1. Eric pide una imagen — desde cero, o a partir de una que adjunta. **Siempre se llena este
   mismo template**, entero. La ruta cambia de dónde sale cada dato, no qué datos hacen falta.
2. Toda línea `QUIÉN: user` que quede sin valor y esté marcada `BLOQUEA` **se pregunta a Eric
   antes de armar el brief**. No se rellena por criterio del asistente: esa fuente no existe.
3. Con una imagen adjunta, las líneas `QUIÉN: user|asset` se leen de la imagen y se declara
   `source_analysis.mode`. Lo que la imagen no muestre sigue siendo pregunta para Eric.
4. El template lleno se le da a Eric **para aprobación**. Aprobado, se congela como brief y
   de ahí sale el `case.json`. Sin aprobación no hay run.

## Leyenda

| columna | qué significa |
|---|---|
| **QUIÉN** | `user` sólo Eric · `asset` se lee de la imagen adjunta · `regla` lo fija un archivo del skill · `run` lo pone el motor |
| **BLOQUEA** | si falta y es de Eric, se pregunta y el run no arranca |
| **VALORES** | los únicos admitidos. `LIBRE` = hoy es texto libre y **ningún validador puede condicionar sobre él** |

---

## Parte 1 — las 75 dimensiones de imagen que el fingerprint ya tiene

| dimensión | QUIÉN | BLOQUEA | VALORES |
|---|---|:-:|---|
| `schema_version` | run | — | **LIBRE** ⚠️ |
| `case_id` | run | — | **LIBRE** ⚠️ |
| `project_id` | user | — | **LIBRE** ⚠️ |
| `scene_id` | user | — | **LIBRE** ⚠️ |
| `shot_id` | user | — | **LIBRE** ⚠️ |
| `asset_id` | run | — | **LIBRE** ⚠️ |
| `stage` | run | **SÍ** | `brief` · `strategy` · `script` · `scene` · `storyboard` · `shot` · `asset` · `prompt` · `generation` · `qa` · `delivery` |
| `media` | user | **SÍ** | `image` · `video` · `text` · `audio` · `mixed` |
| `operation` | user | **SÍ** | `text_to_image` · `image_edit` · `image_to_image` · `reference_analysis` · `text_to_video` · `image_to_video` · `video_edit` · `script_write` · `scene_design` · `storyboard_design` · `shot_plan` · `brand_extract` · `asset_qa` · `package_delivery` · `other` |
| `base_type` | regla | **SÍ** | `T1` · `T2` · `T3` · `T4` · `T5` · `PROD` · `GRAF` · `MULTI` · `REF` · `CLIP` · `SHOT` · `GUION` · `MARCA` · `QA` · `ENTREGA` · `OTHER` |
| `track` | user | — | `QUICK` · `CONTROLLED` · `CONSISTENT` · `FULL` · `UNKNOWN` |
| `generator.family` | regla | **SÍ** | `gpt_image` · `nano_banana` · `flux` · `midjourney` · `ideogram` · `seedream` · `kling` · `veo` · `seedance` · `hailuo` · `sora` · `runway` · `luma` · `pika` · `other` · `UNKNOWN` |
| `generator.model` | user | **SÍ** | **LIBRE** ⚠️ |
| `generator.adapter_version` | run | — | **LIBRE** ⚠️ |
| `deliverable.purpose` | user | **SÍ** | `editorial` · `campaign_key_visual` · `brochure` · `social` · `storyboard` · `reference_master` · `product` · `poster` · `presentation` · `film` · `internal_draft` · `other` · `UNKNOWN` |
| `deliverable.aspect_ratio` | user | **SÍ** | **LIBRE** ⚠️ |
| `deliverable.channel` | user | — | **LIBRE** ⚠️ |
| `deliverable.approval_level` | user | — | `draft` · `internal` · `client` · `paid_media` · `hero` · `UNKNOWN` |
| `subject.count` | user|asset | **SÍ** | **LIBRE** ⚠️ |
| `subject.kinds` | user|asset | **SÍ** | lista |
| `subject.human` | user|asset | **SÍ** | `True` · `False` · `UNKNOWN` |
| `subject.identity_fidelity` | user | **SÍ** | `none` · `generic` · `consistent` · `exact` · `UNKNOWN` |
| `subject.recurring_character` | user | **SÍ** | `True` · `False` · `UNKNOWN` |
| `subject.product_present` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `subject.product_fidelity` | user | — | `none` · `generic` · `recognizable` · `exact` · `UNKNOWN` |
| `subject.body_visibility` | user | **SÍ** | `none` · `face` · `upper_body` · `full_body` · `partial_occlusion` · `split_boundary` · `UNKNOWN` |
| `subject.hands_visible` | user|asset | **SÍ** | `True` · `False` · `UNKNOWN` |
| `subject.feet_visible` | user|asset | **SÍ** | `True` · `False` · `UNKNOWN` |
| `subject.human_contact` | user|asset | **SÍ** | `True` · `False` · `UNKNOWN` |
| `environment.type` | user|asset | **SÍ** | **LIBRE** ⚠️ |
| `environment.continuity` | user | — | `none` · `local` · `scene` · `project` · `UNKNOWN` |
| `environment.crowd` | user|asset | **SÍ** | `True` · `False` · `UNKNOWN` |
| `environment.indoor_outdoor` | user|asset | **SÍ** | `indoor` · `outdoor` · `mixed` · `UNKNOWN` |
| `environment.time_of_day` | user|asset | **SÍ** | **LIBRE** ⚠️ |
| `composition.load_bearing` | user | **SÍ** | `True` · `False` · `UNKNOWN` |
| `composition.viewpoint` | user|asset | **SÍ** | **LIBRE** ⚠️ |
| `composition.split_level` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `composition.waterline_visible` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `composition.background_dof` | user | **SÍ** | `sharp` · `soft` · `blurred` · `mixed` · `UNKNOWN` |
| `composition.spatial_invariants` | user|asset | **SÍ** | lista |
| `realism.mode` | user | **SÍ** | `stylized` · `semi_real` · `photographic` · `strict_photographic` · `UNKNOWN` |
| `realism.skin_texture` | regla | — | `True` · `False` · `UNKNOWN` |
| `realism.materiality` | regla | — | `True` · `False` · `UNKNOWN` |
| `realism.optical_physics` | regla | — | `True` · `False` · `UNKNOWN` |
| `motion.static_frame` | regla | **SÍ** | `True` · `False` · `UNKNOWN` |
| `motion.frozen_action` | user|asset | **SÍ** | `True` · `False` · `UNKNOWN` |
| `motion.subject_motion` | user|asset | **SÍ** | **LIBRE** ⚠️ |
| `physics.water` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `physics.splash` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `physics.bubbles` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `physics.turbulence` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `physics.refraction` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `physics.reflection` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `physics.gravity` | regla | — | `True` · `False` · `UNKNOWN` |
| `physics.collision` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `physics.deformation` | user|asset | — | `True` · `False` · `UNKNOWN` |
| `continuity.level` | user | **SÍ** | `none` · `local` · `scene` · `project` · `UNKNOWN` |
| `continuity.dimensions` | user | — | lista |
| `brand.mode` | user | **SÍ** | `none` · `guided` · `locked` · `strict` · `UNKNOWN` |
| `brand.brand_lock_ref` | user | **SÍ** | **LIBRE** ⚠️ |
| `text.mode` | user | **SÍ** | `none` · `composite` · `in_image` · `UNKNOWN` |
| `text.readable_text_required` | user | **SÍ** | `True` · `False` · `UNKNOWN` |
| `references.mode` | user | **SÍ** | `none` · `partial` · `full` · `UNKNOWN` |
| `references.roles` | user | **SÍ** | lista |
| `references.style_reference` | user | — | `True` · `False` · `UNKNOWN` |
| `references.identity_reference` | user | — | `True` · `False` · `UNKNOWN` |
| `references.environment_reference` | user | — | `True` · `False` · `UNKNOWN` |
| `risk_flags` | regla | — | lista |
| `unknowns` | run | — | lista |
| `provenance` | run | — | lista |
| `task.family` | user | **SÍ** | `generic` · `portrait` · `ecommerce` · `fashion_editorial` · `food_beverage` · `poster_illustration` · `character_design` · `ui_social` · `presentation_slide` · `storyboard` · `multi_panel` · `dimensional` · `text_rendering` · `reference_analysis` · `sports` · `race_speed` · `dialogue` · `animation` · `brand_asset` · `other` · `UNKNOWN` |
| `task.tags` | user | — | lista |
| `task.genre` | user | **SÍ** | **LIBRE** ⚠️ |
| `pipeline_track` | user | **SÍ** | `EXPRESS` · `STANDARD` · `FILM` · `NONE` · `UNKNOWN` |
| `prompt_case` | regla | **SÍ** | `1` · `2` · `3a` · `3b` · `3c` · `4` · `NONE` · `UNKNOWN` |

---

## Parte 2 — dimensiones que el gate de vida reclama y el schema no tiene

Cada una sale de reglas que **hoy están muertas** porque no hay dónde expresar su condición.
No son propuesta de criterio: son la causa medida de que esas reglas no puedan activarse.

| dimensión nueva | QUIÉN | BLOQUEA | VALORES | reglas que revive |
|---|---|:-:|---|---|
| `lighting.setup` | user|asset | **SÍ** | `studio` · `natural_window` · `open_shade` · `direct_sun` · `overcast` · `practical_ambient` · `stadium_floodlight` · `mixed` · `UNKNOWN` | visual-prompt-forge/SKILL.md:265-290 (el lock de iluminación entra verbatim); vision-decomposer.md:44 (luz quebrada, gobos, luz por persianas) |
| `lighting.quality` | user|asset | **SÍ** | `hard` · `soft` · `diffused` · `high_contrast` · `flat` · `UNKNOWN` | creative-direction.md sección de diseño de luz; image/references/photography.md |
| `lighting.direction` | user|asset | **SÍ** | `frontal` · `side` · `back` · `top` · `grazing` · `mixed` · `UNKNOWN` | los bloques canónicos T1 (light_hard: 'hard grazing light with no fill') |
| `treatment.register` | user | **SÍ** | `editorial` · `documentary` · `advertising` · `fine_art` · `snapshot_mobile` · `vintage_analog` · `cinematic` · `UNKNOWN` | el registro que Eric nombró: editorial ≠ documental ≠ imagen de móvil ≠ vintage |
| `treatment.era` | user | — | `contemporary` · `1970s` · `1980s` · `1990s` · `period_pre1960` · `UNKNOWN` | golden-rules.md:140-161 (era anchors, cultural anchors) |
| `treatment.capture_device` | user | **SÍ** | `pro_camera` · `mobile_phone` · `instant_film` · `film_35mm` · `medium_format` · `action_cam` · `UNKNOWN` | creative-direction.md:28-34 (GoPro, Fujifilm, desechable, Hasselblad, iPhone, Polaroid) |
| `composition.shot_size` | user | **SÍ** | `extreme_close_up` · `close_up` · `medium_close_up` · `medium` · `medium_full` · `full` · `wide` · `extreme_wide` · `UNKNOWN` | creative-direction.md:47 (encuadres nombrados); lo que Eric nombró: close-up de rostro ≠ cuerpo completo |
| `source_analysis.mode` | user | **SÍ** | `none` · `composition_only` · `full_decomposition` · `UNKNOWN` | image/references/vision-decomposer.md completo — 12 reglas muertas hoy; learned v3.2:13 (fuentes de composición se abstraen, no se adjuntan) |
| `series_lock.mode` | user | **SÍ** | `none` · `environment` · `lighting` · `color_grade` · `character` · `full` · `UNKNOWN` | visual-prompt-forge/SKILL.md:265-290 y failure-modes.md:29-39 — 12 reglas muertas hoy |
| `structural_input.mode` | user | **SÍ** | `none` · `sketch` · `wireframe` · `floor_plan` · `line_art` · `UNKNOWN` | image/references/structural.md — 3 reglas muertas hoy |
| `environment.time_of_day` | user|asset | **SÍ** | `dawn` · `morning` · `midday` · `golden_hour` · `blue_hour` · `night` · `overcast_day` · `UNKNOWN` | hoy es string libre: ningún validador puede condicionar sobre la hora del día |
| `task.genre` | user | **SÍ** | `CERRAR A ENUM — hoy string libre` | hoy es string libre; este run guardó 'sports_editorial' y ningún validador puede leerlo |
| `composition.viewpoint` | user|asset | **SÍ** | `CERRAR A ENUM — hoy string libre` | hoy es string libre; el punto de vista gobierna reglas de geometría de cámara |
| `environment.type` | user|asset | **SÍ** | `CERRAR A ENUM — hoy string libre` | hoy es string libre; gobierna reglas de entorno y de continuidad |

---

## Parte 3 — lo que el template pregunta y el fingerprint no guarda

Datos que Eric da, que no son dimensiones de clasificación pero sin los cuales no hay prompt:

| pregunta | QUIÉN | BLOQUEA |
|---|---|:-:|
| ¿Qué se ve en la imagen? (sujeto, acción, entorno, en las palabras de Eric) | user | **SÍ** |
| ¿Qué NO debe aparecer? (va al bloque Negative, no al cuerpo) | user | **SÍ** |
| Colores obligados (hex si los hay: marca, uniforme, producto) | user | **SÍ** |
| Texto que debe leerse en la imagen, literal y entre comillas | user | **SÍ** |
| Materiales que deben verse (tela, metal, piel, superficie) | user | **SÍ** |
| Qué se ancla a un elemento legible de la escena (sw30:118 prohíbe «centre», «left half») | user | **SÍ** |
| Formato exacto y si es negociable | user | **SÍ** |
| Es exploración o es el visual final (cambia el modo de detalle y el costo) | user | **SÍ** |
| Si hay imagen adjunta: ¿se adjunta al generador, o sólo se estudia y se describe? | user | **SÍ** |

---

Dimensiones en la parte 1: **75** · propuestas en la parte 2: **14** · preguntas en la parte 3: **9**
Campos `LIBRE` hoy (nadie puede condicionar sobre ellos): **17**
