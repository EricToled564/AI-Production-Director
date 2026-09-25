# RESEARCH DE CAMPO — Familia 06 · Cuerpo en el pico de esfuerzo

Archivo auditado: `.claude/rules/regimenes/06-cuerpo-en-esfuerzo.md` (BORRADOR 2026-09-25).
Fecha de acceso de todas las URLs: **2026-09-25**. Protocolo: skill `research` v2 (6 fases).

## Fase 1 — Pre-flight

```
TEMA DE RESEARCH: evidencia de campo para las 7 líneas [A PRUEBA] de la familia 06
                  (fase de contacto con el suelo en sprint/apex/levantamiento, sombras
                  múltiples de torres de estadio, dos pies plantados en sprint).
PROPÓSITO DOWNSTREAM: cambiar etiqueta [A PRUEBA] → [CAMPO: url] / [REFUTADA: url];
                  capturar frases que producen manos y pies correctos en sprint.
MÍNIMOS: queries 5+ · fetches 7+ (4+ ok) · fuentes profesionales 4+ · anti-patrón 2+
```

## Fase 2 — Bitácora cuantitativa

### Queries (6 ejecutadas, 2 anti-patrón)

| # | Herramienta | Query | Ángulo | Resultado |
|---|---|---|---|---|
| Q-1 | firecrawl_search (web) | `sprint running gait phases flight phase only one foot ground contact biomechanics` | física / estándar | ✅ 6 (Physiopedia, Sports Biomechanics T&F, ochy, ResearchGate) |
| Q-2 | firecrawl_search (web) | `stadium floodlights multiple shadows athletes night photography four shadows` | física / fotografía real | ✅ 6 (Quora, r/NoStupidQuestions, Improve Photography) |
| Q-3 | WebSearch | `AI image runner both feet on ground unnatural stride prompt mid-stride sprint legs fix` | **anti-patrón** | ✅ 9 (prompt-architects, media.io, ai-prompt.jp) |
| Q-4 | WebSearch | `AI generated athlete image fails stadium lighting unrealistic sweat skin prompt tips` | **anti-patrón** | ✅ 9 (rosagranados substack, aipromptoria, The Conversation) |
| Q-5 | WebSearch | `nano banana pro OR gpt-image sprint running prompt hands feet anatomy mid-air stride reddit` | best practice modelo | ✅ 9 (aivideobootcamp, awesome-nanobanana-pro, charliehills) |
| Q-6 | firecrawl_search (web) | `midjourney OR "stable diffusion" prompt ball hitting racket "motion blur" tennis impact reddit` (compartida con 04) | usuarios | ✅ incluye r/ChatGPT "motion-blur running style" |

### Fetches (13 intentos, 10 exitosos)

| # | URL | Resultado |
|---|---|---|
| F-1 | https://www.physio-pedia.com/Running_Biomechanics | ✅ (130 KB, extraído por script) |
| F-2 | https://improvephotography.com/38680/friday-night-lights-photograph-sports-high-school-stadiums/ | ✅ Dave Miller, diagramas foot-candle 4 y 6 postes |
| F-3 | https://www.ochy.io/blog/what-happens-when-you-run-breaking-down-the-gait-cycle-with-biomechanics | ✅ cita Cappellini 2006, Kapri & Mehta 2021 |
| F-4 | https://www.quora.com/Why-do-players-have-shadows-around-them-in-all-four-directions-while-playing-on-the-stadium | ✅ 6 respuestas (incl. ingeniero de iluminación) |
| F-5 | https://prompt-architects.com/blog/359-sports-and-action-motion-prompts | ✅ 28 templates + límites de anatomía, 2026-09-02 |
| F-6 | https://www.media.io/ai-prompts/gemini-ai-runner-photo-prompts.html | ✅ 25 prompts NBP + fórmula |
| F-7 | https://aivideobootcamp.com/blog/gpt-image-2-vs-nano-banana-pro-2026/ | ✅ A/B 10 prompts, 2026-04-22 |
| F-8 | https://charliehills.substack.com/p/how-to-prompt-nano-banana-pt2 | ✅ 13 prompts (negative list) |
| F-9 | https://rosagranados.substack.com/p/finding-the-flaws-how-to-identify | ✅ análisis de 5 imágenes deportivas Midjourney |
| F-10 | https://www.tandfonline.com/doi/full/10.1080/14763141.2021.1873411 | ❌ cuerpo vacío (paywall); solo metadatos |
| F-11 | https://www.reddit.com/r/NoStupidQuestions/comments/9dneh9/in_a_football_stadium_players_have_more_than_one/ | ❌ Reddit no soportado |
| F-12 | https://www.reddit.com/r/ChatGPT/comments/1rptu7h/how_do_photographers_create_this_motionblur/ | ❌ Reddit no soportado |
| F-13 | https://miraflow.ai/blog/ai-motion-blur-photo-prompts-2026 (compartido con 04) | ✅ prompts #1 sprinter, #4 boxer |

Fuentes profesionales (4+): Physiopedia (F-1, referencia clínica con citas a Novacheck); Ochy (F-3, con referencias peer-reviewed DOI); Forensic Focus/Amped (familia 04 F-7, aplicable a sombras); Improve Photography / Dave Miller con datos de diseño lumínico (F-2); prompt-architects con verificación de documentación de vendors fechada (F-5); aivideobootcamp con metodología y fecha (F-7).

## Fase 3 — Citas verbatim

| Q# | URL | Cita verbatim |
|----|-----|---------------|
| C-01 | F-1 physio-pedia | "When running, there is an additional phase: the float phase when both feet are off the ground." |
| C-02 | F-1 physio-pedia | "The demarcation between walking and running occurs when periods of double support during the stance phase of the gait cycle (both feet are simultaneously in contact with the ground) give way to two periods of double float at the beginning and the end of the swing phase of gait (neither foot is touching the ground)" |
| C-03 | F-1 physio-pedia | "The amount of time that the runner spends in float, increases as the runner increases in speed." |
| C-04 | F-3 ochy | "Unlike walking, running has a unique feature: the _aerial phase_. This is the moment when neither foot is on the ground, and you are essentially flying!" |
| C-05 | F-3 ochy | "The running gait is characterized by two main phases: the **stance phase**, where one foot is on the ground, and the **swing phase**, during which the same feet is off the ground" |
| C-06 | F-3 ochy | "_\\- Forefoot strike:_ The ball of the foot makes contact first, often seen in sprinters." |
| C-07 | F-4 quora (Sripad Sambrani) | "For proper illumination of the play area the stadium is installed with Flood-lights at about 6–8 locations on its periphery. Hence as many light sources, so many shadows of each player on the ground." |
| C-08 | F-4 quora (Krishna KumariChalla) | "There will be as many shadows as the number of light sources." |
| C-09 | F-4 quora (OpenBlueprint) | "These masts are built exceptionally high, often exceeding 100 feet, to ensure a steep angle of incidence. The steeper the angle, the shorter the resulting shadow." |
| C-10 | F-4 quora (OpenBlueprint) | "When the ratio is that tight, the human eye—and the camera lens—perceives the entire field as a seamless, shadowless surface." |
| C-11 | F-2 improvephotography | "With only 4 sources of light there are more shadows on the players faces which does not produce very good images. Stadiums with 6 light poles will have more evenly dispersed amount of light and will produce less shadows on the players faces." |
| C-12 | F-2 improvephotography | "It is also important to understand that stadium lighting is designed to provide the most light in the center of the field." |
| C-13 | F-5 prompt-architects | "Extra limbs during a full stride, a joint bending the wrong direction mid-swing, a foot planting through the ground: these are not wording failures." |
| C-14 | F-5 prompt-architects | "A crowded sprint start fails far more often than one runner alone." |
| C-15 | F-5 prompt-architects | "A tight shot on a face, hand or foot at the decisive moment sidesteps a full-body sprint that exposes every joint at once." |
| C-16 | F-5 prompt-architects (#1) | "Shutter fast enough to freeze the driving arm and front leg sharp, a light motion blur on the trailing foot. Camera panning at the runner's exact pace, background streaked, the runner held sharp. Peak moment: the instant the front foot strikes the track." |
| C-17 | F-5 prompt-architects | "Real athletic movement has a wind-up before the action and a follow-through after, weight already shifting, an arm already trailing." |
| C-18 | F-5 prompt-architects | "stop rewriting after two or three genuinely different attempts, and change the model, the shot or the framing instead." |
| C-19 | F-6 media.io | "Name the moment: start, mid-stride, hill climb, finish tape, cooldown, recovery walk." |
| C-20 | F-6 media.io | "Control motion: ask for freeze-frame clarity or panning blur, but not both at maximum." |
| C-21 | F-6 media.io (Start Line Explosion) | "muscles engaged, dust and rubber pellets kicked up, sharp sweat highlights, dramatic stadium floodlights at night, shot on Sony A1 with 85mm f/1.8, low angle near ground, freeze-motion clarity" |
| C-22 | F-7 aivideobootcamp (Round 2 atlético) | "Nano Banana Pro produces a visibly more photographic result — skin pores, lighting, the mid-air water droplets all read as real. GPT Image 2.0 wins on typography" |
| C-23 | F-7 aivideobootcamp (Round 7) | "GPT 2.0's portrait looks like a strong digital painting; Nano Banana Pro's looks like a frame from a real camera." |
| C-24 | F-8 charliehills (Golden Light Stairway) | "Exclude: cartoon, CGI, AI-artifacts, over-smoothing, plastic skin, excessive sharpening, motion blur, warped anatomy, extra fingers, disfigured hands, double shadow, blown highlights" |
| C-25 | F-9 rosagranados | "The lighting on the face does not fully match the general light source, making the image feel artificial." |
| C-26 | F-9 rosagranados | "The transition between the sock and the sneaker is unclear at the front and back. It looks as if they are fused into a single object rather than being separate elements." |
| C-27 | F-9 rosagranados | "With such an intense light source, there should be more pronounced shadows on one side of the face." |
| C-28 | F-13 miraflow (#4 boxer) | "the boxer's arm, gloves and face perfectly sharp with visible sweat droplets frozen in the air near the fist, the ropes and background gym equipment rendered as soft motion blur, harsh single overhead light source" |
| C-29 | F-13 miraflow | "Ignoring lighting consistency between the sharp subject and the blurred background. If the subject is lit warm and the background streaks are lit cool with no logical light source connecting them, the composite reads as fake" |

Citas SNIPPET-ONLY:
- Q-3, service.ai-prompt.jp: "explain which foot bears weight, whether a heel lifts, and what floor, mat, sand, or product set supports the pose" `[SNIPPET-ONLY]`
- Q-1, ResearchGate (Kapri & Mehta): "The sprint gait is divided into two phases: the support phase when one foot is on the ground and the swing phase" `[SNIPPET-ONLY]`
- Q-4, aipromptoria: negativos "plastic skin, CGI appearance, weak lighting, oversharpening, noisy shadows" `[SNIPPET-ONLY]`

## Fase 4 — Tabla de veredictos por regla [A PRUEBA]

| # | Texto exacto de la regla | Veredicto | URLs que lo sostienen | Nota |
|---|---|---|---|---|
| 1 | Cargar cuando el beat es el instante de máximo esfuerzo o el cruce de un umbral físico por una persona: cinta de llegada, apex de un salto, impacto de un golpe, punto muerto de un levantamiento. | **SIN EVIDENCIA** (enrutamiento) | F-5, F-6 como respaldo del principio | Nadie discute cuándo cargar un archivo. El principio "describir el pico, no la actividad" sí está en campo (F-5 "Describe the peak, not the activity"; C-19). |
| 2 | Si hay un objeto impulsado, cargar además `04-objeto-balistico.md`; si hay público detrás, `08-multitud-anonima.md`. | **SIN EVIDENCIA** | — | Enrutamiento. |
| 3 | La fase de contacto con el suelo debe ser coherente con la velocidad: en sprint un solo pie toca o ninguno, en el apex del salto ninguno, en el punto muerto del levantamiento los dos plantados y cargados. | **CONFIRMADA EN CAMPO** | F-1 (C-01, C-02, C-03), F-3 (C-04, C-05), ResearchGate snippet | Biomecánica verificable en dos fuentes independientes con referencias: en carrera nunca hay doble apoyo; el vuelo crece con la velocidad. La parte de levantamiento (dos pies plantados) no aparece en ninguna fuente, aunque es trivial. |
| 4 | En estadio nocturno, las torres de luz son los prácticos motivados y producen sombras múltiples cortas; declararlas o el modelo pone una sola sombra larga de estudio. | **CONFIRMADA EN CAMPO** (física) / **SIN EVIDENCIA** (comportamiento del modelo) | F-4 (C-07, C-08, C-09), F-2 (C-11) | Sombras múltiples: confirmado; "cortas": confirmado por la altura de mástil (>100 ft, ángulo empinado). Matiz importante: en estadios profesionales con ring lighting y uniformidad 0.7–0.8 las sombras casi desaparecen (C-10); las sombras múltiples duras son propias de estadios de 4 postes (C-11). Que el modelo ponga "una sola sombra de estudio" por defecto: ninguna fuente lo documenta; solo hay indicio indirecto de que las sombras son el punto débil (Forensic Focus, familia 04 C-15). |
| 5 | Dos pies plantados en pleno sprint: declarar la fase de zancada. | **CONFIRMADA EN CAMPO** (con reserva) | F-5 (C-16, C-13), F-6 (C-19), snippet ai-prompt.jp | Dos fuentes recomiendan nombrar el momento de la zancada y el pie que carga. Reserva de campo: prompt-architects avisa que el pie que atraviesa el suelo y los miembros extra son límite de capacidad, no de redacción; la corrección funciona a veces. |
| 6 | Sombra única de estudio en estadio nocturno: declarar las torres y las sombras múltiples. | **CONFIRMADA EN CAMPO** (parcial) | F-4 (C-07, C-09), F-2 (C-11) | Misma base que la regla 4. Debe añadirse el tipo de estadio al prompt (4 postes vs ring). |
| 7 | [checklist] Fase de contacto con el suelo coherente. | **CONFIRMADA EN CAMPO** | F-1, F-3 | Misma base que la regla 3. |

**Resumen familia 06:** 7 reglas A PRUEBA → **5 CONFIRMADAS** (2 con matiz/parcial, 1 con reserva), **0 REFUTADAS**, **2 SIN EVIDENCIA** (enrutamiento).

## Fase 4b — Hallazgos nuevos

1. **Nunca** insistir más de dos o tres regeneraciones distintas sobre un sprint de cuerpo entero con anatomía rota; cambiar a plano cerrado de rostro, mano o pie en el instante decisivo, porque los miembros extra y el pie que atraviesa el suelo no son fallos de redacción. [CAMPO: https://prompt-architects.com/blog/359-sports-and-action-motion-prompts] — (C-13, C-15, C-18) `[QUOTED]`
2. **Siempre** un solo atleta por generación en sprint; una salida de tacos con varios corredores falla mucho más que un corredor solo. [CAMPO: https://prompt-architects.com/blog/359-sports-and-action-motion-prompts] — (C-14) `[QUOTED]` — refuerza `produccion-visual-sw30 R9`.
3. El cuerpo en esfuerzo **debe** llevar anticipación y follow-through nombrados (peso ya desplazado, brazo ya arrastrando); una pose que solo muestra el medio del gesto se lee posada. [CAMPO: https://prompt-architects.com/blog/359-sports-and-action-motion-prompts] — (C-17) `[QUOTED]`
4. Frase de campo para sprint con pies correctos: "freeze the driving arm and front leg sharp, a light motion blur on the trailing foot ... Peak moment: the instant the front foot strikes the track". [CAMPO: https://prompt-architects.com/blog/359-sports-and-action-motion-prompts] — (C-16) `[QUOTED]`
5. **Siempre** nombrar el momento de la zancada con vocabulario de fase (start, mid-stride, finish tape) y qué pie carga el peso. [CAMPO: https://www.media.io/ai-prompts/gemini-ai-runner-photo-prompts.html] — (C-19) `[QUOTED]`; snippet ai-prompt.jp lo repite.
6. **Nunca** pedir a la vez "freeze-frame clarity" y "panning blur" al máximo. [CAMPO: https://www.media.io/ai-prompts/gemini-ai-runner-photo-prompts.html] — (C-20) `[QUOTED]` — confirma la ley de una sola lógica de blur.
7. El sudor en campo se pide como "sharp sweat highlights" o "sweat droplets frozen in the air near the fist" bajo "harsh single overhead light source", nunca como piel mojada. [CAMPO: https://www.media.io/ai-prompts/gemini-ai-runner-photo-prompts.html ; https://miraflow.ai/blog/ai-motion-blur-photo-prompts-2026] — (C-21, C-28) `[QUOTED]` — confirma la regla FUENTE de sudor como speculares.
8. La luz del sujeto nítido y la del fondo barrido **deben** compartir fuente y temperatura; si no, se lee compuesto. [CAMPO: https://miraflow.ai/blog/ai-motion-blur-photo-prompts-2026] — (C-29) `[QUOTED]`
9. El prompt **debe** declarar el tipo de estadio: 4 postes = sombras múltiples duras en la cara; 6 postes o ring lighting profesional = sombras múltiples suaves casi invisibles; y el centro del campo es la zona más iluminada. [CAMPO: https://improvephotography.com/38680/friday-night-lights-photograph-sports-high-school-stadiums/ ; https://www.quora.com/Why-do-players-have-shadows-around-them-in-all-four-directions-while-playing-on-the-stadium] — (C-10, C-11, C-12) `[DERIVED]`: la familia asume un solo tipo de estadio; el campo distingue dos regímenes lumínicos.
10. Lista negativa de campo para cuerpo en NBP: "warped anatomy, extra fingers, disfigured hands, double shadow, plastic skin, over-smoothing, excessive sharpening, blown highlights". [CAMPO: https://charliehills.substack.com/p/how-to-prompt-nano-banana-pt2] — (C-24) `[QUOTED]`
11. Inspección al 100% **debe** incluir la transición calcetín–zapatilla y la fusión ropa–piel, fallos deportivos repetidos que la familia no lista. [CAMPO: https://rosagranados.substack.com/p/finding-the-flaws-how-to-identify] — (C-26) `[QUOTED]`
12. **Tensión con una regla FUENTE**: la familia recomienda "GPT Image 2 quality high para piel"; un A/B fechado (2026-04-22) da a Nano Banana Pro la victoria en piel, poros y gotas en el aire, y a GPT Image 2 la tipografía; el flujo de campo es NBP para la placa fotográfica y GPT para el texto. [CAMPO: https://aivideobootcamp.com/blog/gpt-image-2-vs-nano-banana-pro-2026/] — (C-22, C-23) `[QUOTED]` — no refuta la regla FUENTE (es de otro origen) pero merece prueba propia.
13. Bajo luz dura, la cara **debe** mostrar sombra pronunciada en un lado; una cara plana bajo sol intenso es tell de AI. [CAMPO: https://rosagranados.substack.com/p/finding-the-flaws-how-to-identify] — (C-25, C-27) `[QUOTED]` — confirma la regla FUENTE de luz dura rasante.

## Fase 5 — Forbidden patterns scan

☑ Ejecutado · sin detecciones. Cada cita de foro lleva usuario y URL; los snippets están marcados; la tensión con la regla FUENTE (hallazgo 12) se presenta como dato de un A/B fechado, no como autoridad genérica.

## Fase 6 — Checklist de auditoría del skill

- [x] 5+ queries (6)
- [x] 7+ fetch attempts (13)
- [x] 4+ fetches exitosos con quotes (10 exitosos, 29 citas)
- [x] 4+ fuentes profesionales (Physiopedia, Ochy con DOIs, Forensic Focus, Improve Photography, prompt-architects con verificación de vendors)
- [x] 2+ queries anti-patrón (Q-3, Q-4)
- [x] Cada veredicto con C-#/F-#
- [x] Etiquetas epistémicas en hallazgos
- [x] Sin paráfrasis como cita
- [x] Sin autoridad sin URL
- [x] Forbidden patterns scan limpio
- [x] Limitaciones presentes

## Limitaciones del research

- Reddit inaccesible; el hilo r/ChatGPT sobre "motion-blur running style" (el más citado por Q-2/Q-6) no pudo leerse.
- El paper de Sports Biomechanics (T&F) está tras paywall; solo metadatos.
- No se encontró evidencia empírica de que los modelos pongan **por defecto** una sola sombra de estudio en estadio nocturno; la mitad "comportamiento del modelo" de las reglas 4 y 6 sigue siendo inferencia.
- No se encontró ninguna fuente sobre levantamiento de pesas en punto muerto (dos pies plantados, barra flexionada).
- No se encontró ninguna frase de campo verificada con output que garantice manos correctas en sprint; la evidencia dice que es límite de capacidad y la salida es el encuadre.
- GitHub `awesome-nanobanana-pro` fue fetchado (155 KB) pero no contiene prompts deportivos ni de sprint; no se cita.

## Sugerencia de próximo paso

Ejercicio de canonización 06: prompt C-16 (sprint, un solo atleta) en NBP y GPT Image 2, variando solo la cláusula de estadio (4 postes vs ring lighting) y contando sombras en el suelo; inspección al 100% de manos, pies y transición calcetín–zapatilla.
