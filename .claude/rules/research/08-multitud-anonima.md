# Investigación de campo — Familia 08: Multitud anónima

Archivo bajo prueba: `.claude/rules/regimenes/08-multitud-anonima.md` (BORRADOR 2026-09-25).
Fecha de acceso de todas las URLs: **2026-09-25**. Protocolo: skill `research` v2, seis fases.
Herramientas: WebSearch, Firecrawl (search/scrape), WebFetch, curl + extracción de texto, pullpush.io
(archivo público de Reddit) para un hilo. Ninguna herramienta de generación fue usada.

Criterio de veredicto: **CONFIRMADA EN CAMPO** = dos fuentes independientes con ejemplo concreto o
física verificable; **REFUTADA** = una fuente sólida la contradice con evidencia; **SIN EVIDENCIA** =
nada concluyente.

## Fase 1 — Pre-flight

```
TEMA: evidencia de campo para las 7 líneas [A PRUEBA] de la familia 08 (umbral de multitud, barrido
      direccional, densidad desigual vs retícula, sombras múltiples de estadio) en generación de
      imagen (NBP / GPT Image 2) y en fotografía real de estadio, concierto y calle.
PROPÓSITO DOWNSTREAM: decidir qué líneas pasan a [CAMPO: url] o [REFUTADA: url].
MÍNIMOS: 5+ queries · 7+ fetch attempts · 4+ exitosos · 4+ fuentes profesionales · 2+ anti-patrón.
```

## (1) Bitácora cuantitativa

### Queries (11 ejecutadas, 3 anti-patrón)

| # | Herramienta | Query | Resultado |
|---|---|---|---|
| 1 | WebSearch **(anti-patrón)** | reddit AI generated crowd stadium faces distorted duplicate faces nano banana midjourney | ⚠ sin Reddit; promptsera, emarketer (Midjourney y equipos deportivos) |
| 2 | WebSearch | stadium floodlights multiple shadows player four shadows explanation | ✅ UEFA Stadium Lighting Guide 2023, Quora, Brainly, infinitylearn |
| 3 | WebSearch | concert photography crowd shots backlight silhouettes stage lights | ✅ aftershoot, DPS, DIYP, photographyicon |
| 4 | WebSearch **(anti-patrón)** | how to spot AI generated crowd images identical faces repeated pattern | ✅ caniphish, picassoia, Scientific American, arXiv 2406.08651 |
| 5 | WebSearch | panning motion blur crowd photography marathon protest streaks direction | ✅ DIYP panning, photographylife, DPS motion blur |
| 6 | WebSearch | nano banana pro crowd stadium prompt "crowd" faces realistic JSON | ⚠ librerías de prompts (imagine.art, apiyi); sin caso de fallo |
| 7 | WebSearch **(anti-patrón)** | "crowd" AI generation tips avoid repeated faces uniform pattern occlusion stable diffusion | ✅ Hakky Handbook (Regional Prompter/Latent Couple), stable-diffusion-art |
| 8 | WebSearch | r/StableDiffusion crowd scene tips repeated face latent couple thread | ❌ sin resultados pertinentes de Reddit |
| 9 | Firecrawl search | site:reddit.com crowd scene stable diffusion OR midjourney OR "nano banana" faces repeated | ✅ r/StableDiffusion 1are9rn, 1oic1d0, 196dc2x, r/Bard 1mvhhh1 |
| 10 | WebSearch | site:youtube.com AI crowd scene stadium concert generation tutorial | ⚠ comparativas genéricas; ningún tutorial específico de multitud |
| 11 | WebSearch | simonwillison.net gpt-image-2 Where's Waldo crowd quality high | ✅ post del 2026-04-21 |

### Fetches (20 intentos, 14 exitosos)

| # | URL | Método | Resultado |
|---|---|---|---|
| F1 | https://documents.uefa.com/r/UEFA-Stadium-Lighting-Guide-2023-2023/Player-shadows-Online | curl → WebFetch | curl solo shell JS (2.7 KB); **WebFetch OK** con citas `[WEBFETCH]` (no verificables char-level) |
| F2 | https://www.quora.com/Why-do-players-have-shadows-around-them-in-all-four-directions-while-playing-on-the-stadium | curl | ❌ bloqueado |
| F3 | https://infinitylearn.com/question-answer/during-a-night-match-we-can-see-multiple-shadows-of-players-becau-611932 | curl | ✅ (fuente educativa, débil) |
| F4 | https://en.wikipedia.org/wiki/Floodlight | curl | ✅ pero sin pasaje pertinente sobre sombras múltiples |
| F5 | https://www.diyphotography.net/concert-photography-the-ultimate-guide/ | curl | ✅ |
| F6 | https://photographyicon.com/concert-photography/ | curl | ✅ |
| F7 | https://digital-photography-school.com/concert-photography-tips/ | curl | ✅ |
| F8 | https://aftershoot.com/blog/concert-photography-tips/ | curl | ✅ |
| F9 | https://caniphish.com/blog/how-to-spot-ai-images | curl | ✅ |
| F10 | https://blog.picassoia.com/how-to-spot-ai-generated-images | curl | ✅ |
| F11 | https://promptsera.com/fix-weird-ai-faces/ | curl | ✅ |
| F12 | https://research.everypixel.com/gpt-image-2-0/ | curl | ✅ (benchmark 34 briefs, 4 evaluadores, corrección publicada 2026-09-25) |
| F13 | https://www.diyphotography.net/panning-photography-technique/ | curl | ✅ |
| F14 | https://photographylife.com/motion-blur-panning-photography | curl | ❌ bloqueado (618 chars) |
| F15 | https://digital-photography-school.com/how-to-capture-motion-blur-in-photography/ | curl | ✅ |
| F16 | https://www.reddit.com/r/Bard/comments/1mvhhh1/nanobanana_is_amazing_but_it_does_not_produce/ | pullpush.io | ✅ cuerpo del post (2025-08-20, 30 ups); comentarios no recuperados |
| F17 | https://www.reddit.com/r/StableDiffusion/comments/1oic1d0/tips_for_generating_realistic_crowd_or_reallife/ | pullpush.io ×2 | ❌ rate limit |
| F18 | https://www.reddit.com/r/StableDiffusion/comments/1are9rn/why_is_se_so_bad_for_generating_the_faces_of/ | pullpush.io ×2 | ❌ rate limit |
| F19 | https://www.youtube.com/watch?v=DXlM8J8EZOA (Bijan Bowen, 2026-04-21) | Firecrawl scrape | ✅ transcripción; test "LAN party" con muchas personas en GPT Images 2.0 |
| F20 | https://simonwillison.net/2026/Apr/21/gpt-image-2/ | curl | ✅ |

Fuentes profesionales: UEFA Stadium Lighting Guide 2023 (standards body), everypixel.com (benchmark
con metodología), Digital Photography School / DIYP / photographyicon (guías técnicas de fotógrafos
profesionales), Simon Willison (ingeniero, test publicado con prompt y resultados). Total: 6.

## (2) Citas verbatim

| Q# | URL | Cita verbatim |
|---|---|---|
| Q1 | https://documents.uefa.com/r/UEFA-Stadium-Lighting-Guide-2023-2023/Player-shadows-Online | "Corner tower illuminance systems will generally produce hard shadows, which will vary in different areas of the pitch." `[WEBFETCH]` |
| Q2 | https://documents.uefa.com/r/UEFA-Stadium-Lighting-Guide-2023-2023/Player-shadows-Online | "During the pitch illuminance design, it is important to evaluate the production of player shadows and eliminate any hard shadows." `[WEBFETCH]` |
| Q3 | https://documents.uefa.com/r/UEFA-Stadium-Lighting-Guide-2023-2023/Player-shadows-Online | "This is generally done by using multiple light sources from various locations for each area of the pitch." `[WEBFETCH]` |
| Q4 | https://documents.uefa.com/r/UEFA-Stadium-Lighting-Guide-2023-2023/Player-shadows-Online | "With this type of installation, it is not possible to produce consistently soft shadows." `[WEBFETCH]` |
| Q5 | https://infinitylearn.com/question-answer/during-a-night-match-we-can-see-multiple-shadows-of-players-becau-611932 | "During a night match, we can see multiple shadows of players because of multiple sources of light." |
| Q6 | https://www.diyphotography.net/concert-photography-the-ultimate-guide/ | "Concerts often come with dramatic backlighting and effects like fog or smoke. These can either make or break your photo. Use backlighting to create striking silhouettes or accentuate the artist's shape and movement. The key is to expose for highlights and embrace the mood it creates." |
| Q7 | https://photographyicon.com/concert-photography/ | "Capture the crowd. The audience is a crucial part of the concert experience. Hands raised in unison, faces lit by stage wash, crowd surfers, fans singing every word: these images tell the story of the event in a way that performer shots alone cannot." |
| Q8 | https://photographyicon.com/concert-photography/ | "When a performer stands between you and a brightly lit background, expose for the background to create a dramatic silhouette." |
| Q9 | https://digital-photography-school.com/concert-photography-tips/ | "This kind of photo we'll shoot when there is no light on the subject and the only lights are behind the band / singer / dancer." |
| Q10 | https://aftershoot.com/blog/concert-photography-tips/ | "Look for silhouettes, backlight bursts, and contrasty shadows. Working with the light, not against it, is where the magic happens." |
| Q11 | https://caniphish.com/blog/how-to-spot-ai-images | "When there are multiple people in the frame, the model often reuses the same visual structure, such as faces, poses, or expressions, with only slight changes. This can make the subjects look eerily similar, like clones standing side by side." |
| Q12 | https://caniphish.com/blog/how-to-spot-ai-images | "The result is a group that looks copy-pasted, even if the differences are minor at first glance." |
| Q13 | https://blog.picassoia.com/how-to-spot-ai-generated-images | "When AI generates complex scenes like forests, crowds, or tiled surfaces, it often tiles or mirrors texture patches to fill the frame. This creates repetition that no real photograph would contain." |
| Q14 | https://blog.picassoia.com/how-to-spot-ai-generated-images | "Crowd scenes are particularly prone to this: if you identify two faces that share the same bone structure and proportions, the image was almost certainly generated synthetically." |
| Q15 | https://research.everypixel.com/gpt-image-2-0/ | "The fourth evaluator rejected it outright, rating every criterion 1/10: "Too many people in the distance, almost all identical and walking in one direction, some faces are distorted."" |
| Q16 | https://research.everypixel.com/gpt-image-2-0/ | "What to do: for crowd-heavy scenes, generate several candidates and select, or use licensed photography. Keep AI generation for portraits and small groups, where anatomy is easy to check." |
| Q17 | https://research.everypixel.com/gpt-image-2-0/ | "Crowd and street scenes Not recommended UC08 6.9, faces distort at distance" |
| Q18 | https://research.everypixel.com/gpt-image-2-0/ | "in Simon Willison's test of April 21, 2026, a hidden object in a crowded Where's Waldo scene was missing at default settings and clearly present at high quality and 3840×2160." |
| Q19 | https://research.everypixel.com/gpt-image-2-0/ | "Three evaluators rated it between 7 and 9 on practical value and described the same flaw, distorted faces in the background." |
| Q20 | https://promptsera.com/fix-weird-ai-faces/ | "In my testing, it works exceptionally well on blurry or highly artifacted faces located in the background of wide shots." (sobre GFPGAN) |
| Q21 | https://www.diyphotography.net/panning-photography-technique/ | "You track your subject horizontally as you shoot. That's the basic idea behind panning photography. Your camera follows along at the same speed as your subject moves. The shutter speed stays slow enough to blur the background." |
| Q22 | https://www.diyphotography.net/panning-photography-technique/ | "Speed Matching Issues Your camera speed has to match your subject perfectly. Too fast blurs the subject. Too slow leaves the background sharp." |
| Q23 | https://digital-photography-school.com/how-to-capture-motion-blur-in-photography/ | "But since the shutter speed is slow, the subject still shows that motion blur in the direction they were moving." |
| Q24 | https://www.reddit.com/r/Bard/comments/1mvhhh1/nanobanana_is_amazing_but_it_does_not_produce/ | "Test it for yourself; Upload an image with many people in the background, ideally people you personally know, and ask for a change about something not related to the background. You will observe that the background faces are definitely not the same faces as the people you know." (vía pullpush.io, post 2025-08-20) |
| Q25 | https://www.youtube.com/watch?v=DXlM8J8EZOA | "The faces don't look mangled. Sometimes when doing this test, if you zoom in on a face that's like somewhere over here, it's going to look like something out of a horror film. I don't see that happening here, which is good." `[TRANSCRIPT]` |
| Q26 | https://simonwillison.net/2026/Apr/21/gpt-image-2/ | "I wasn't able to spot the raccoon—I quickly realized that testing image generation models on Where's Waldo style images (Where's Wally in the UK) can be pretty frustrating!" |
| Q27 | https://www.reddit.com/r/StableDiffusion/comments/1are9rn/why_is_se_so_bad_for_generating_the_faces_of/ | "Why is SE so bad for generating the faces of crowds or people" `[SNIPPET-ONLY]` título |
| Q28 | https://www.reddit.com/r/StableDiffusion/comments/1oic1d0/tips_for_generating_realistic_crowd_or_reallife/ | "Tips for generating realistic crowd or real-life scene photos with people?" `[SNIPPET-ONLY]` título |

## (3) Tabla de veredictos

| Regla [A PRUEBA] (texto exacto) | Veredicto | URLs que lo sostienen | Nota |
|---|---|---|---|
| §1 "Cargar cuando hay más de seis personas en cuadro y ninguna de las figuras de la masa necesita reconocerse." | **SIN EVIDENCIA** (el número 6) | indirecto: Q16 https://research.everypixel.com/gpt-image-2-0/ ; ver 09 (Google fija 5 identidades) | `[DERIVED]` (Q16) la única frontera cuantificada en campo es "portraits and small groups"; el tope de identidades sostenidas por proveedor es 5 (NBP) y 4 (NB2 API), así que "más de cinco rostros que deben reconocerse" ya es multitud en la práctica. El "seis" exacto no aparece en ninguna fuente. |
| §1 "Si tres o más figuras deben reconocerse, no es multitud: cargar `09-grupo-ensamble.md`." | **SIN EVIDENCIA** (no evaluable en campo) | — | Regla de enrutado interno. |
| §2.6 "Una multitud en movimiento, manifestación o carrera callejera, se trata como textura con las cues de velocidad: barrido direccional coherente con la dirección declarada del flujo." | **CONFIRMADA EN CAMPO** (física) | Q21, Q22 https://www.diyphotography.net/panning-photography-technique/ · Q23 https://digital-photography-school.com/how-to-capture-motion-blur-in-photography/ | `[QUOTED]` (Q21, Q23) el barrido siempre sigue la dirección real del movimiento y su magnitud la fija la relación obturación/velocidad; dos guías independientes. `[QUOTED]` (Q15) **matiz de campo**: que *toda* la masa camine en una sola dirección con figuras idénticas fue leído como fallo por un evaluador, así que la coherencia direccional del barrido no debe convertirse en uniformidad de poses ni de trayectorias secundarias. |
| §2.8 "Una multitud tiene densidad desigual: huecos, filas, cuerpos que se tapan; la retícula uniforme de cabezas es la firma del render." | **CONFIRMADA EN CAMPO** | Q11, Q12 https://caniphish.com/blog/how-to-spot-ai-images · Q13, Q14 https://blog.picassoia.com/how-to-spot-ai-generated-images · Q15 https://research.everypixel.com/gpt-image-2-0/ | `[QUOTED]` (Q11–Q14) dos guías de detección independientes describen exactamente la firma: clones, patrones "copy-pasted", parches de textura repetidos o espejados en multitudes. `[QUOTED]` (Q15) un benchmark con evaluadores humanos la encontró en GPT Image 2 ("almost all identical"). |
| §4 "Estadio nocturno: las torres de luz son los prácticos motivados y crean sombras múltiples y cortas; declararlas." | **CONFIRMADA EN CAMPO** (con matiz importante) | Q1–Q4 https://documents.uefa.com/r/UEFA-Stadium-Lighting-Guide-2023-2023/Player-shadows-Online · Q5 https://infinitylearn.com/question-answer/during-a-night-match-we-can-see-multiple-shadows-of-players-becau-611932 | `[QUOTED]` (Q1, Q4, Q5) sombras múltiples y duras existen y son físicamente correctas en estadios con **torres de esquina**. `[QUOTED]` (Q2, Q3) **matiz**: la guía UEFA 2023 ordena a los diseñadores *eliminar* las sombras duras mediante muchas fuentes distribuidas; en un estadio moderno de élite las sombras son suaves y multidireccionales, no cuatro sombras nítidas. La regla debe declarar el tipo de instalación (torres de esquina → sombras múltiples duras; anillo de cubierta → sombras suaves). "Cortas" no está en ninguna fuente `[INFERRED]`: depende de la altura de la torre. Q1–Q4 son `[WEBFETCH]`, no char-level. |
| §8 "Retícula uniforme de cabezas: pedir densidad desigual y oclusiones." | **CONFIRMADA EN CAMPO** (diagnóstico) / **SIN EVIDENCIA** (el remedio por prompt) | Q13, Q14, Q15, Q16 | `[QUOTED]` (Q13–Q15) el diagnóstico está probado. `[ABSENT]` ninguna fuente demuestra que pedir "densidad desigual y oclusiones" corrija el render; lo que el benchmark recomienda es generar varios candidatos y seleccionar, o usar foto de stock (Q16). Retraído como remedio garantizado; queda como remedio plausible a probar en ejercicio. |
| §9 "[ ] Barrido coherente con la dirección del flujo si la masa se mueve." | **CONFIRMADA EN CAMPO** (física) | Q21, Q23 | Misma base que §2.6. |

Resumen: **4 CONFIRMADAS EN CAMPO · 0 REFUTADAS · 2 SIN EVIDENCIA** (más una línea, §8, confirmada como
diagnóstico y sin evidencia como remedio).

Reglas [FUENTE] que el campo además toca: §4 "Concierto: … el público queda como silueta con rim, el 70%
del cuadro sin luz" está apoyada como *default* (Q6, Q8, Q9, Q10) pero no como absoluto: Q7 documenta
"faces lit by stage wash" como plano legítimo de público; el 70% no aparece en ninguna fuente.
§2.1 "sin rostros legibles … después se insertan los héroes" recibe apoyo fuerte de Q16, Q17, Q19.

## (4) Hallazgos nuevos (reglas candidatas)

1. Nunca dar por fija la multitud de fondo después de una edición: cualquier edición local de NBP
   regenera los rostros del fondo, así que tras insertar cada héroe el crítico debe volver a contar y
   revisar rostros de fondo, no solo el del héroe. `[QUOTED]` (Q24)
   [CAMPO: https://www.reddit.com/r/Bard/comments/1mvhhh1/nanobanana_is_amazing_but_it_does_not_produce/]
2. Nunca aprobar a la primera una multitud densa con rostros a distancia en GPT Image 2: es el único
   brief que falló el listón de producción del benchmark (6.9/10), con rostros distorsionados al fondo;
   siempre generar varias variantes y seleccionar, o resolver la placa con foto licenciada.
   `[QUOTED]` (Q15, Q16, Q17, Q19) [CAMPO: https://research.everypixel.com/gpt-image-2-0/]
3. En escenas densas de GPT Image 2 debe usarse quality high y la resolución máxima (3840×2160): un
   elemento pequeño en multitud faltaba a calidad por defecto y aparecía a alta. `[QUOTED]` (Q18, Q26)
   [CAMPO: https://research.everypixel.com/gpt-image-2-0/ · https://simonwillison.net/2026/Apr/21/gpt-image-2/]
4. Declarar siempre el tipo de instalación lumínica del estadio: "cuatro torres de esquina" produce
   sombras múltiples duras; "anillo de luminarias en cubierta" produce sombras suaves casi sin dirección.
   Pedir "sombras múltiples" en un estadio moderno es un anacronismo físico. `[QUOTED]` (Q1–Q4)
   [CAMPO: https://documents.uefa.com/r/UEFA-Stadium-Lighting-Guide-2023-2023/Player-shadows-Online]
5. El público de concierto puede llevar rostros iluminados por el wash frontal del escenario cuando el
   beat lo pide ("hands raised, faces lit by stage wash"); la silueta es el default, no una prohibición,
   y esos rostros siguen siendo anónimos aunque estén iluminados. `[QUOTED]` (Q7)
   [CAMPO: https://photographyicon.com/concert-photography/]
6. El crítico debe buscar rostros que compartan la misma estructura ósea y proporciones dentro de la masa,
   no solo "clones" evidentes: es el criterio que usan las guías de detección. `[QUOTED]` (Q14)
   [CAMPO: https://blog.picassoia.com/how-to-spot-ai-generated-images]
7. Los rostros deformados del fondo en planos abiertos se reparan con restauración facial localizada
   (GFPGAN/CodeFormer o inpainting de región), nunca regenerando la placa entera. `[QUOTED]` (Q20)
   [CAMPO: https://promptsera.com/fix-weird-ai-faces/]
8. `[SNIPPET-ONLY]` Hilos r/StableDiffusion 1are9rn y 1oic1d0 tratan exactamente este problema
   (rostros de multitud) pero no pudieron leerse; quedan como lead para el ejercicio.

## Fase 5 — Forbidden patterns scan

☐ Ejecutado. Se retiró la afirmación "photographylife: subject passes perpendicular" por no tener fetch
exitoso (solo snippet). Las citas UEFA quedan marcadas `[WEBFETCH]` y no se presentan como char-level.
Ninguna autoridad sin URL.

## (5) Checklist de auditoría del skill

- [x] 5+ queries (11)
- [x] 7+ fetch attempts (20)
- [x] 4+ fetches exitosos con quotes (14)
- [x] 4+ fuentes profesionales (6)
- [x] 2+ queries anti-patrón (3: #1, #4, #7)
- [x] Cada claim con Q#
- [x] Etiquetas epistémicas en cada claim
- [x] Sin paráfrasis presentada como cita
- [x] Sin autoridad sin URL
- [x] Forbidden patterns scan ejecutado
- [x] Limitaciones presentes

## Limitaciones

- Solo un hilo de Reddit legible (r/Bard 1mvhhh1); los dos hilos de r/StableDiffusion sobre multitudes
  quedaron en título.
- La guía UEFA es JS puro: citas solo vía WebFetch, no verificables por grep.
- No hay ningún caso documentado de NBP generando estadio o manifestación con evaluación de rostros;
  la evidencia de modelo es de GPT Image 2 (benchmark) y de NBP solo en edición (r/Bard).
- El umbral "seis personas" y el "70% sin luz" no tienen fuente de campo; son cifras del repo.

## Próximo paso

Ejercicio real: placa de estadio nocturno en NBP declarando "cuatro torres de esquina" vs "anillo de
cubierta" y comparando sombras; inserción de un héroe y recuento de rostros de fondo antes/después
(hallazgo 1); una manifestación con barrido y densidad desigual para probar si el remedio por prompt
de §8 funciona o si hace falta selección entre variantes.
