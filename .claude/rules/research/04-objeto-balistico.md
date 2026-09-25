# RESEARCH DE CAMPO — Familia 04 · Objeto balístico

Archivo auditado: `.claude/rules/regimenes/04-objeto-balistico.md` (BORRADOR 2026-09-25).
Fecha de acceso de todas las URLs: **2026-09-25**. Protocolo: skill `research` v2 (6 fases).

## Fase 1 — Pre-flight

```
TEMA DE RESEARCH: evidencia de campo para las 9 líneas [A PRUEBA] de la familia 04
                  (deformación de pelota en impacto, reacción del receptor, sombra de
                  contacto, referencia de escala, objeto flotante, sombra doble).
PROPÓSITO DOWNSTREAM: cambiar etiqueta [A PRUEBA] → [CAMPO: url] / [REFUTADA: url] en el
                  registro de reglas; alimentar el ejercicio de canonización.
MÍNIMOS: queries 5+ · fetches 7+ (4+ ok) · fuentes profesionales 4+ · anti-patrón 2+
```

## Fase 2 — Bitácora cuantitativa

### Queries (7 ejecutadas, 2 anti-patrón)

| # | Herramienta | Query | Ángulo | Resultado |
|---|---|---|---|---|
| Q-1 | firecrawl_search (web) | `tennis ball impact deformation high speed photography strings deflect` | física / estándar | ✅ 8 resultados (TWU, JTAM, MDPI, White Rose thesis, YouTube Physics Curriculum) |
| Q-2 | firecrawl_search (web) | `midjourney OR "stable diffusion" prompt ball hitting racket "motion blur" tennis impact reddit` | best practice usuarios | ✅ 8 (r/ChatGPT, r/aiArt, Filmora, Media.io, Aiarty) |
| Q-3 | firecrawl_search (web) | `AI image generation object floating no contact shadow fix prompt "contact shadow"` | **anti-patrón** | ✅ 8 (artarch, nightjar, Instagram, Facebook) |
| Q-4 | firecrawl_search (web) | `nano banana OR "gpt image" prompt motion blur background sharp subject sports ball` | best practice modelo | ✅ 8 (miraflow, pose.ai, r/ChatGPTPromptGenius, YouTube) |
| Q-5 | firecrawl_search (web) | `AI generated image duplicate ball two shadows sports photo failure` | **anti-patrón** | ✅ 8 (Forensic Focus, Envato, Adobe Community) |
| Q-6 | firecrawl_search (web) | `sports photography tennis shutter speed freeze ball deformation on racket strings tips` | fotografía real | ✅ 6 (Alpha Universe, tt.tennis-warehouse, HuffPost) |
| Q-7 | firecrawl_search (web) | `AI generated product image scale wrong size reference object prompt "sense of scale"` | caso comparable | ✅ 6 (promer.ai, pixelpanda, nightjar) |

### Fetches (15 intentos, 13 exitosos)

| # | URL | Resultado |
|---|---|---|
| F-1 | https://twu.tennis-warehouse.com/learning_center/singlestring.php | ✅ cuerpo completo (paper Rod Cross, TWU) |
| F-2 | https://www.artarch.ai/blog/ai-contact-shadow-occlusion-prompt | ✅ A/B medido en Nano Banana Pro, 2026-09-18 |
| F-3 | https://nightjar.so/blog/how-to-make-ai-product-photos-look-real-checklist | ✅ checklist 10 puntos |
| F-4 | https://miraflow.ai/blog/ai-motion-blur-photo-prompts-2026 | ✅ 20 prompts + errores comunes, 2026-09-05 |
| F-5 | https://www.reddit.com/r/ChatGPT/comments/1rptu7h/how_do_photographers_create_this_motionblur/ | ❌ Firecrawl: "we do not support this site"; old.reddit vía WebFetch: bloqueado |
| F-6 | https://pose.ai/blog/sports-event-photo-prompts-guide-2026 | ✅ guía prompts deportivos NB2 |
| F-7 | https://www.forensicfocus.com/articles/how-to-reveal-ai-generated-images-by-checking-shadows-and-reflections-in-amped-authenticate/ | ✅ análisis forense de sombras (Amped/Farid) |
| F-8 | https://elements.envato.com/learn/ai-image-fails | ✅ 10 fallos y correcciones |
| F-9 | https://www.reddit.com/r/aiArt/comments/1o2334l/this_one_prompt_gave_me_a_magazinequality/ | ❌ Reddit no soportado |
| F-10 | https://www.youtube.com/watch?v=7cphkU3l71c | ✅ descripción (Physics Curriculum & Instruction, 2000 fps) |
| F-11 | http://tt.tennis-warehouse.com/index.php?threads/tennis-photography.712575/ | ✅ hilo de foro completo |
| F-12 | https://promer.ai/blog/ai-product-photography-prompts | ✅ 22 prompts, incluye "In-Hand Size Reference" |
| F-13 | https://alphauniverse.com/stories/10-quick-sports-photography-tips-how-to-freeze-action-with-your-alpha-camera/ | ✅ Sony oficial |
| F-14 | https://prompt-architects.com/blog/359-sports-and-action-motion-prompts | ✅ 28 prompts, incluye #24 pelota/raqueta y #9 bate/pelota |
| F-15 | https://www.youtube.com/watch?v=vb_cGHOWWo0 | ✅ transcript (GPT Image, blur de fondo) |

Fuentes profesionales (4+): TWU/Rod Cross (F-1, física publicada); Physics Curriculum & Instruction (F-10, material educativo con parámetros de cámara); Forensic Focus/Amped Software citando Kee–O'Brien–Farid 2014 (F-7); Sony Alpha Universe (F-13, corporativo oficial). Complementarias con metodología visible: artarch (F-2, A/B con métrica de luminancia).

## Fase 3 — Citas verbatim (char-level, del cuerpo del fetch)

| Q# | URL | Cita verbatim |
|----|-----|---------------|
| C-01 | F-10 youtube 7cphkU3l71c | "The 1st segment shows a racquet hitting a tennis ball, the flattening of the ball is clearly seen. The racquet is in contact with the ball for a total time of 0.004 seconds." |
| C-02 | F-10 youtube 7cphkU3l71c | "The racquetball flattens dramatically with a dimple appearing as the ball regains its shape." |
| C-03 | F-1 twu singlestring | "the strings in a tennis racquet are normally woven, are tensioned to about 300 N, the tension rises to about 500 N during a firm impact with the ball, and the strings stretch by about 20 mm in a direction perpendicular to the string plane." |
| C-04 | F-1 twu singlestring | "String motion was easily observed and measured on video film since the displacement of the string during each impact was comparable to the radius of the ball." |
| C-05 | F-14 prompt-architects (#24) | "A tennis ball at the exact instant of racket contact, the strings visibly deforming around the ball, the player's wrist already snapping through the follow-through." |
| C-06 | F-14 prompt-architects (#9) | "Fast shutter freezes the ball deforming slightly against the bat, motion blur trailing the bat's arc." |
| C-07 | F-2 artarch | "Real objects are grounded by a very small piece of the picture. Where a base meets a surface, ambient light is occluded and the two surfaces meet in a narrow band that is darker than either of them." |
| C-08 | F-2 artarch | "Remove it and the geometry still looks plausible in isolation, but the object loses its weight. The base edge reads as a flat cut line" |
| C-09 | F-2 artarch | "\"Add a contact shadow\" alone tends to produce a wide grey puddle under the object." |
| C-10 | F-2 artarch | "When the object is meant to be airborne, when it is lit as a strong backlit silhouette, or when the contact is soft and irregular — fabric draping, a hand holding an object, a base sinking into sand." |
| C-11 | F-3 nightjar | "A floating product. The contact shadow (the tight, dark line directly under where the product touches the surface, produced by ambient occlusion) is missing, blurry, or pointing the wrong way." |
| C-12 | F-3 nightjar | "Use depth of field that matches the product scale." |
| C-13 | F-12 promer | "In-Hand Size Reference _What it does: gives shoppers an instant, accurate sense of scale._" |
| C-14 | F-12 promer | "avoid: distorted label text, warped logo, mismatched product color, extra reflections, floating shadows, low resolution, watermark or text overlay." |
| C-15 | F-7 forensicfocus | "diffusion models tend to create plausible shadows when they are a little blurry and not very detailed. They will more likely fail when there are sharp shadows and objects casting complex shadows" |
| C-16 | F-4 miraflow | "Being specific about direction is the single biggest lever for making the effect look intentional rather than like a rendering glitch." |
| C-17 | F-4 miraflow | "Using the same blur intensity for every subject regardless of implied speed. A sprinter should have more dramatic streaking than someone walking casually" |
| C-18 | F-6 pose.ai | "'freeze-frame sports journalism style', 'ball mid-air', 'motion blur on background, sharp focus on face'. These tags prevent motion artifacts and keep the subject sharp even in dynamic poses." |
| C-19 | F-11 tt.tennis-warehouse (puppybutts) | "you'll probably want a shutter speed of above 1/2000 to ensure there is no motion blur, depending on how fast your subjects are" |
| C-20 | F-11 tt.tennis-warehouse (stringertom) | "1/250 second if the racquet motion is desired to be frozen (sometimes a nice effect is achieved when the body motion is frozen and the racquet is blurred)." |
| C-21 | F-13 alphauniverse | "A fast shutter speed – like 1/1000-sec. or higher – freezes motion, whether it's a soccer player mid-kick or a basketball dunk in progress." |
| C-22 | F-14 prompt-architects | "Frozen and motion-blurred are two different visual languages, not two qualities of one shot, and which one you get is a choice you make out loud." |
| C-23 | F-8 envato | "For any object, describe its appearance, however basic this might seem, like in this example: \"A detailed violin with four strings, wooden body, resting on a table.\"" |
| C-24 | F-3 nightjar | "Drop ornament words (\"8K,\" \"cinematic,\" \"masterpiece,\" \"Unreal Engine\"). Push the variables into ingredients instead." |
| C-25 | F-15 youtube vb_cGHOWWo0 (transcript) | "describe exactly how you want the AI to apply motion blur. And make sure to include subject, direction, speed, and intensity." |

Citas SNIPPET-ONLY (no fetch del cuerpo; estatus epistémico inferior):
- Q-6, Facebook Sports Photography group: "Shutter speeds of 1/4000 to 1/8000 are recommended to freeze the ball." `[SNIPPET-ONLY]`
- Q-2, r/aiArt: "The key is \"hyper-sharp focus\" + \"motion blur\" combo." `[SNIPPET-ONLY]`

## Fase 4 — Tabla de veredictos por regla [A PRUEBA]

| # | Texto exacto de la regla | Veredicto | URLs que lo sostienen | Nota |
|---|---|---|---|---|
| 1 | Cargar cuando el sujeto principal del panel es un objeto en vuelo, en impacto o en el instante posterior al impacto. | **SIN EVIDENCIA** | — | Regla de enrutamiento, no empírica. El principio subyacente (describir el instante pico, no la actividad) sí está en campo: C-22 y F-14 "Describe the peak, not the activity". |
| 2 | Si el objeto lo impulsa una persona visible, cargar además `06-cuerpo-en-esfuerzo.md`; si el objeto es un vehículo, `05-vehiculo.md`. | **SIN EVIDENCIA** | — | Regla de enrutamiento. Nadie en campo discute cómo se organizan familias de reglas. |
| 3 | Una pelota blanda en el impacto no es redonda: se achata contra la superficie, y el material del que está hecha lo dice el borde, fieltro erizado o cuero tenso. | **CONFIRMADA EN CAMPO** (parcial) | F-10 (C-01, C-02), F-1 (C-04), F-14 (C-05, C-06) | Achatamiento: física verificada a 2000 fps y usada en prompts de campo. La parte "fieltro erizado / cuero tenso" no aparece en ninguna fuente; queda como inferencia de material. |
| 4 | Toda acción produce reacción visible en lo que recibe el golpe: cuerdas deflectadas, tela hundida, superficie del agua deprimida; sin reacción, el objeto flota pegado. | **CONFIRMADA EN CAMPO** | F-1 (C-03, C-04), F-14 (C-05) | Deflexión de cuerdas ~20 mm, "comparable to the radius of the ball". Prompt-architects la pide textualmente ("strings visibly deforming around the ball"). Dos fuentes independientes. |
| 5 | Un objeto pequeño necesita referencia de escala en el mismo plano de foco: una mano, una línea de cancha, una etiqueta; sin ella no hay tamaño. | **CONFIRMADA EN CAMPO** (débil) | F-12 (C-13), F-3 (C-12) | Evidencia viene de e-commerce, no de deporte. La "mano" como referencia está confirmada (promer #14). "Mismo plano de foco" solo lo sostiene nightjar de forma indirecta (DOF acorde a la escala). |
| 6 | Pelota perfectamente redonda contra las cuerdas: falta el estado posterior; pedir la deformación y la deflexión de las cuerdas. | **CONFIRMADA EN CAMPO** | F-10 (C-01), F-14 (C-05, C-06) | La corrección propuesta (pedir deformación + deflexión) coincide con el template de campo #24. |
| 7 | El objeto flota sin tocar: falta sombra de contacto y reacción de la superficie. | **CONFIRMADA EN CAMPO** | F-2 (C-07, C-08), F-3 (C-11), F-12 (C-14) | Tres fuentes independientes; artarch lo mide (banda de contacto 79.1% → 25.4% de luminancia relativa). |
| 8 | [checklist] Sombra de contacto única. | **CONFIRMADA EN CAMPO** | F-2 (C-09: "one narrow, soft-edged occlusion shadow in the single gap"), F-7 (C-15), charliehills negative prompt "double shadow" (ver familia 06, F-8) | La unicidad se pide explícitamente en prompts de campo; forense confirma que las sombras son el punto débil de difusión. |
| 9 | [checklist] Referencia de escala en foco. | **CONFIRMADA EN CAMPO** (débil) | F-12 (C-13), F-3 (C-12) | Misma base que la regla 5. |

**Resumen familia 04:** 9 reglas A PRUEBA → **7 CONFIRMADAS** (3 con matiz parcial/débil), **0 REFUTADAS**, **2 SIN EVIDENCIA** (ambas de enrutamiento).

## Fase 4b — Hallazgos nuevos (no contemplados en la familia)

Cada uno redactado como regla candidata con marcador deóntico y etiqueta de campo.

1. **Nunca** pedir "contact shadow" a secas; **siempre** describir la forma de la sombra: estrecha, borde suave, pegada a la línea de contacto, desvaneciéndose en corta distancia; la orden desnuda produce un charco gris ancho. [CAMPO: https://www.artarch.ai/blog/ai-contact-shadow-occlusion-prompt] — (C-09) `[QUOTED]`
2. **Nunca** añadir sombra de contacto a un objeto en vuelo ni a un contacto blando (mano sujetando la pelota, pelota hundiéndose en arcilla); en esos casos la sombra va proyectada y separada, o describe el hundimiento. [CAMPO: https://www.artarch.ai/blog/ai-contact-shadow-occlusion-prompt] — (C-10) `[QUOTED]`
3. **Siempre** declarar la dirección del blur ("horizontal motion blur streaks" para paneo, "radial blur" para giro); la dirección es la palanca principal para que se lea intencional y no glitch. [CAMPO: https://miraflow.ai/blog/ai-motion-blur-photo-prompts-2026] — (C-16) `[QUOTED]`
4. La intensidad del blur **debe** ser proporcional a la velocidad implícita del sujeto; un mismo barrido para todo se lee falso. [CAMPO: https://miraflow.ai/blog/ai-motion-blur-photo-prompts-2026] — (C-17) `[QUOTED]`
5. En un prompt de motion blur **siempre** nombrar cuatro cosas: sujeto que se barre, dirección, velocidad e intensidad. [CAMPO: https://www.youtube.com/watch?v=vb_cGHOWWo0] — (C-25) `[QUOTED]`
6. Bajo luz dura con sombras nítidas y objetos que proyectan sombras complejas, **debe** inspeccionarse la coherencia geométrica de las sombras al 100%: ahí es donde los modelos de difusión fallan más. [CAMPO: https://www.forensicfocus.com/articles/how-to-reveal-ai-generated-images-by-checking-shadows-and-reflections-in-amped-authenticate/] — (C-15) `[QUOTED]`
7. El objeto **siempre** se describe con sus componentes físicos concretos (número de costuras, material, dónde apoya), no como categoría; "a ball" es el equivalente del "an instrument" que produce saxofones comestibles. [CAMPO: https://elements.envato.com/learn/ai-image-fails] — (C-23) `[QUOTED]`
8. **Nunca** usar palabras ornamento ("8K", "cinematic", "masterpiece"); mover las variables a ingredientes fotográficos. [CAMPO: https://nightjar.so/blog/how-to-make-ai-product-photos-look-real-checklist] — (C-24) `[QUOTED]` — coincide con la lista prohibida de `image/references/gpt-image.md:36`.
9. Frases de campo que funcionan en Nano Banana 2 para congelar objeto y barrer fondo: "freeze-frame sports journalism style", "ball mid-air", "motion blur on background, sharp focus on face". [CAMPO: https://pose.ai/blog/sports-event-photo-prompts-guide-2026] — (C-18) `[QUOTED]`
10. Para el look de impacto congelado la referencia física es 1/2000 s o más rápido (el contacto raqueta-pelota dura 0.004 s); a 1/250 s el cuerpo se congela y la raqueta se barre, lo que es un cue de blur parcial legítimo. [CAMPO: http://tt.tennis-warehouse.com/index.php?threads/tennis-photography.712575/] — (C-19, C-20, C-01) `[DERIVED]` — inferencia: la descripción "fast-shutter look" del prompt puede anclarse en "1/2000 s" para GPT Image 2 y en "high-speed freeze" para NBP.
11. El negative prompt reutilizable de campo para objeto incluye "floating shadows" y "extra reflections". [CAMPO: https://promer.ai/blog/ai-product-photography-prompts] — (C-14) `[QUOTED]`

## Fase 5 — Forbidden patterns scan

☑ Ejecutado · sin detecciones. Toda autoridad citada lleva URL fetchada; las dos citas de snippet están marcadas `[SNIPPET-ONLY]`; ningún número (20 mm, 0.004 s, 25.4%) aparece sin su fuente.

## Fase 6 — Checklist de auditoría del skill

- [x] 5+ queries ejecutadas (7, visibles en bitácora)
- [x] 7+ fetch attempts (15)
- [x] 4+ fetches exitosos con quotes extraídas (13 exitosos, 25 citas)
- [x] 4+ fuentes profesionales (TWU/Cross, Physics Curriculum, Forensic Focus/Amped, Sony Alpha Universe)
- [x] 2+ queries anti-patrón (Q-3, Q-5)
- [x] Cada veredicto y hallazgo referencia C-# / F-#
- [x] Etiqueta epistémica en cada hallazgo
- [x] Ninguna paráfrasis presentada como cita directa
- [x] Ninguna autoridad sin URL
- [x] Forbidden patterns scan sin detecciones
- [x] Sección Limitaciones presente

## Limitaciones del research

- Reddit (r/StableDiffusion, r/midjourney, r/Bard, r/ChatGPT) inaccesible por Firecrawl ("we do not support this site") y por WebFetch (old.reddit bloqueado). La evidencia de "usuarios" viene de foros alternativos (tt.tennis-warehouse), blogs de prompts con metodología y descripciones/transcripts de YouTube.
- Facebook e Instagram (donde circulan muchos prompts de Nano Banana) solo aparecen como snippets de búsqueda; no se fetcharon.
- No se encontró ningún caso de uso real que documente específicamente la textura "fieltro erizado" o "cuero tenso" en el borde de la pelota en el impacto; la parte material de la regla 3 sigue siendo inferencia.
- No se encontró ninguna fuente que hable de referencia de escala en fotografía deportiva de objeto; toda la evidencia de escala es de producto/e-commerce.
- No se pudo verificar ningún ejemplo publicado con imagen generada + prompt de pelota deformada contra cuerdas (solo templates de prompt sin output medido).

## Sugerencia de próximo paso

Ejercicio de canonización 04: generar en NBP y GPT Image 2 el prompt #24 de prompt-architects (C-05) con y sin la cláusula de sombra de artarch (C-09), medir la banda de contacto como hace artarch, y registrar el template que funcione como `[CANONICA fecha]`.
