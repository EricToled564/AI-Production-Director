# RESEARCH DE CAMPO — Familia 03 · Subacuático

Archivo auditado: `.claude/rules/regimenes/03-subacuatico.md` (BORRADOR 2026-09-25).
Fecha de acceso de todas las URLs: **2026-09-25**. Protocolo: skill `research` v2 (6 fases).
Este archivo NO modifica la familia; sólo propone veredictos y reglas candidatas.

Métodos: `[SCRAPE]` texto crudo Firecrawl (grep-able) · `[WEBFETCH]` cita extraída por WebFetch con instrucción verbatim · `[SNIPPET-ONLY]` sólo resumen del buscador.

## Fase 1 — Pre-flight

```
TEMA DE RESEARCH: evidencia de campo para las 22 líneas [A PRUEBA] de la familia 03
  (absorción del rojo, haces, cáusticas, burbujas, pelo/tela, backscatter, lente, domo, piel).
PROPÓSITO DOWNSTREAM: canonizar o refutar cada regla en 03-subacuatico.md; reglas candidatas.
MÍNIMOS: 5+ queries · 7+ fetches · 4+ exitosos · 4+ profesionales · 2+ anti-patrón.
RESULTADO: 11 queries · 29 intentos de fetch · 23 con contenido · 8 fuentes profesionales · 3 anti-patrón.
```

## Fase 2 — Bitácora cuantitativa

### 2a. Queries

| # | Herramienta | Query | Ángulo | Resultado |
|---|---|---|---|---|
| 1 | firecrawl_search → 429 → WebSearch | underwater photography color absorption red depth backscatter strobe positioning guide | A/C | uwphotographyguide (×4), backscatter.com, fotografit, scubadiving, arXiv 2505.19895 |
| 2 | firecrawl_search → 429 → WebSearch | AI generated underwater image prompt looks fake bubbles hair floating midjourney stable diffusion tips | B anti-patrón | prompthero, promptden, artvy (galerías); sin tips de fallo |
| 3 | firecrawl_search → 429 → WebSearch | cenote photography light beams tips sunlight particles time of day | A | uwphotographyguide, dan.org, waterdog, victorherrera, divephotoguide, scubadiving, ikelite |
| 4 | WebSearch | underwater caustics sunlight ripples physics explanation photography | C física | onlandscape, atoptics, scienceofsurfing, arXiv 2407.10318 |
| 5 | WebSearch | reddit stable diffusion underwater portrait prompt hair floating bubbles rising realistic tips | A/E | stable-diffusion-art.com, huggingface Underwater XL |
| 6 | WebSearch | nano banana underwater photo edit prompt red color loss depth tips gemini image | A (modelo) | guías oficiales Google/DeepMind (sin contenido de agua), media.io |
| 7 | WebSearch | freediving photography tips hair floating bubbles exhale timing model underwater portrait | A | expertphotography, divephotoguide, submerge, franreina, Brett Stanley, katejonker |
| 8 | firecrawl_search (developer) | underwater generated image prompt bubbles hair floating looks fake issue | B anti-patrón | vibemeai, morphic, media.io, travisnicholson |
| 9 | WebSearch | red light absorbed first 5 meters underwater color loss chart depth photography red orange yellow | C física | dan.org "Recovering Color", uwphotographyguide, divephotoguide, arXiv 1904.06437 |
| 10 | WebSearch | underwater caustics overcast cloudy day disappear diffuse light no sun ripples photography | B/C (contraprueba) | petapixel, ISPRS (snippet), otoy |
| 11 | WebSearch | underwater light rays "god rays" visibility requires particles OR "suspended particles" OR plankton clear water diving photography explanation | B/C (contraprueba de la regla de partículas) | divermag, dtmag, justgottadive (visibilidad) |

Anti-patrón / contraprueba explícitas: #2, #8, #10, #11 (4).

### 2b. Fetches

| # | URL | Método | Resultado |
|---|---|---|---|
| F1 | https://www.uwphotographyguide.com/backscatter-underwater | SCRAPE | ✅ (Scott Gietler, 2009-05-25, mod. 2025-08-15) |
| F2 | https://www.uwphotographyguide.com/top-11-tips-for-cenote-photography/ | SCRAPE | ✅ (Luke Coley, 2021-05-25) |
| F3 | https://dan.org/alert-diver/article/light-in-the-dark-shooting-cenotes/ | WEBFETCH | ✅ |
| F4 | https://www.ikelite.com/blogs/advanced-techniques/chasing-light-rays | WEBFETCH | ✅ |
| F5 | https://www.onlandscape.co.uk/2019/01/physics-of-caustic-light-in-water/ | WEBFETCH | ✅ (poco pertinente) |
| F6 | https://blog.fotografit.eu/guide-to-underwater-photography-lighting/ | WEBFETCH | ✅ |
| F7 | https://www.scienceofsurfing.com/p/light | WEBFETCH | ✅ |
| F8 | https://www.uwphotographyguide.com/underwater-photography-strobe-positioning/ | WEBFETCH | ✅ |
| F9 | https://www.scubadiving.com/how-to-photograph-cenotes | WEBFETCH | ❌ 403 |
| F10 | https://www.media.io/ai-prompts/gemini-ai-underwater-prompt.html | WEBFETCH | ✅ (blog de prompts) |
| F11 | https://huggingface.co/Moises08/underwater-xl | WEBFETCH | ❌ 401 |
| F12 | https://arxiv.org/abs/2505.19895 | WEBFETCH | ✅ abstract |
| F13 | https://stable-diffusion-art.com/underwater-portrait/ | SCRAPE | ✅ (2022-11-20) |
| F14 | https://atoptics.co.uk/blog/lake-caustics/ | WEBFETCH | ✅ |
| F15 | https://www.geniea.com/prompts/gpt-image-photorealistic-underwater | WEBFETCH | ✅ sin contenido pertinente |
| F16 | https://www.franreinaphotography.com/stories/how-to-pose-underwater-photoshoot-tips | WEBFETCH | ✅ |
| F17 | https://www.divephotoguide.com/underwater-photography-special-features/article/freediving-tips-for-shooting-photos-videos/ | SCRAPE | ✅ (2020-09-05) |
| F18 | https://www.underwater-photographer.com/underwater-modelling-hints-tips/ | SCRAPE | ✅ (Brett Stanley, 2026-06-26) |
| F19 | https://expertphotography.com/underwater-photoshoot-portrait | SCRAPE | ✅ (mod. 2025-04-04) |
| F20 | https://www.uwphotographyguide.com/underwater-photography-lighting-fundamentals | SCRAPE | ✅ |
| F21 | https://oceanexplorer.noaa.gov/facts/light-travel.html | WEBFETCH | ❌ 404 |
| F22 | https://oceanservice.noaa.gov/facts/light_travel.html | WEBFETCH | ✅ (sin frases sobre longitudes de onda) |
| F23 | https://dan.org/alert-diver/article/recovering-color-in-underwater-photography/ | SCRAPE | ✅ (Logan Wood, 2023-11-20) |
| F24 | https://www.vibemeai.net/trending/underwater-prompt | SCRAPE | ✅ (galería de prompts + FAQ) |
| F25 | https://morphic.com/resources/vfx/underwater-portrait-effect | SCRAPE | ✅ (prompts + FAQ) |
| F26 | https://www.divephotoguide.com/getting-started-with-underwater-photography/basic-principles-light-underwater/ | WEBFETCH | ❌ 503 |
| F27 | https://travisnicholson.medium.com/why-your-ai-images-look-fake-and-how-to-fix-them-3b57f79c82ac | WEBFETCH | ❌ 403 |
| F28 | https://www.victorherrera.net/cenote-suytun-light-beams-best-time-of-day-for-epic-photos | WEBFETCH | ✅ |
| F29 | https://www.waterdogphotographyblog.com/caves-caverns-and-cenotes/ | WEBFETCH | ✅ |

Fuentes profesionales: F12 (arXiv), F22 (NOAA, gobierno), F23 y F3 (DAN), F1/F2/F20/F8 (guía de referencia con autores y fechas), F4 (documentación técnica de fabricante), F14 (Atmospheric Optics, divulgación científica especializada). Blogs de prompts (F10, F24, F25) y tutoriales de fotógrafos (F16, F18, F19) = fuentes de campo.

## Fase 3 — Citas verbatim

| Q# | URL | Método | Cita verbatim |
|---|---|---|---|
| Q1 | F20 uwphotographyguide | SCRAPE | "Red is the first to be absorbed, followed by orange & yellow. The colors disappear underwater in the same order as they appear in the color spectrum. Even water at 5ft depth will have a noticeable loss of red." |
| Q2 | F20 uwphotographyguide | SCRAPE | "Don't forget to add in the horizontal distance. If you are 10ft underwater, and you are viewing an object 10ft away, the light has actually travelled 20ft, and all of the reds will be filtered out." |
| Q3 | F20 uwphotographyguide | SCRAPE | "Your brain will compensate for the loss of color underwater. This is why you still think you can see reds and oranges in deeper water, but when you take an ambient light shot with your camera, they aren't there!" |
| Q4 | F23 dan.org | SCRAPE | "Red is the first visible color to disappear, just an arm's reach from the surface." |
| Q5 | F23 dan.org | SCRAPE | "Green and blue are the only colors left past 60 feet (18 meters). Attempting to manually adjust white balance below this depth will not be effective. You will need to use artificial light." |
| Q6 | F23 dan.org | SCRAPE | "When adjusting the white balance to correct skin tones, the blue of the water is pushed toward an aqua color." |
| Q7 | F23 dan.org | SCRAPE | "Sunrays appear red when the camera attempts to correct for red, the first color lost to water density." |
| Q8 | F6 fotografit | WEBFETCH | "Using artificial lights, like underwater strobes or video lights, can reintroduce warm colors (reds, oranges, yellows) close to your subject" |
| Q9 | F1 uwphotographyguide | SCRAPE | "Backscatter is mainly caused by strobes or the internal flash lighting up particles in the water in between the lens and the subject." |
| Q10 | F1 uwphotographyguide | SCRAPE | "The most backscatter can be seen when a strobe is positioned right next to the lens, for example like the internal flash of a point and shoot camera." |
| Q11 | F1 uwphotographyguide | SCRAPE | "Find areas of the dive site with better visibility, which is often right near the surface, down deeper, or in a protected area of the reef" |
| Q12 | F4 ikelite | WEBFETCH | "To my surprise, turbidity isn't necessary. The clearer your water the farther your light (and rays) will go." |
| Q13 | F4 ikelite | WEBFETCH | "These rays will follow you around, but may disappear when the sun goes behind a cloud." |
| Q14 | F3 dan.org cenotes | WEBFETCH | "The cenotes' calm water tightly focuses the rays, and against the darkness of the caverns they elicit comparisons to laser beams." |
| Q15 | F3 dan.org cenotes | WEBFETCH | "Ideally you want a viewpoint that hides the surface, so the beams are the brightest subject in the frame." |
| Q16 | F3 dan.org cenotes | WEBFETCH | "The more you can overexpose the scene, the brighter the beams will be." |
| Q17 | F3 dan.org cenotes | WEBFETCH | "Adding strobe light usually ruins the ambience in these photos, so unless there is something spectacular in the foreground, turn off your strobes." |
| Q18 | F29 waterdog | WEBFETCH | "The beams will be more focused if the surface of the water is calm and the sunlight is bright." |
| Q19 | F28 victorherrera | WEBFETCH | "Overcast: The effect is minimal; consider rescheduling if your priority is the light beam." |
| Q20 | F14 atoptics | WEBFETCH | "Caustics are formed when the curvature of the water's surface aligns perfectly with the incoming rays of sunlight." |
| Q21 | F7 scienceofsurfing | WEBFETCH | "Calm conditions with just enough surface texture create the most defined caustics - think those perfect glassy mornings with barely perceptible ripples." |
| Q22 | F7 scienceofsurfing | WEBFETCH | "Too flat, and you lose the lensing effect entirely. Too choppy, and the light gets scattered in too many directions to form coherent patterns." |
| Q23 | F2 uwphotographyguide cenotes | SCRAPE | "When undisturbed it can seem like a sheet of glass, and when a diver swims through, it mixes together and produces a blurry haze." |
| Q24 | F2 uwphotographyguide cenotes | SCRAPE | "In my opinion, using a fisheye lens tends to distort the images a bit too much – noticeably in straight lines of light beams and rock formations. I prefer to use 16mm on my Sony 16-35mm rectilinear lens to avoid this distortion" |
| Q25 | F2 uwphotographyguide cenotes | SCRAPE | "Outside of ambient light, an effective technique is using video lights to backlight your subjects to create a "halo" surrounding them, which can be very striking." |
| Q26 | F20 uwphotographyguide | SCRAPE | "Be sure to always get close to your subject." |
| Q27 | F20 uwphotographyguide | SCRAPE | "Objects will also appear to be up to 33% larger than they are. This is due to the fact that the index of refraction of water is greater than air. This happens behind flat surfaces, such as your mask, a compact camera underwater housing, or a macro port. It does not happen when using a dome port." |
| Q28 | F19 expertphotography | SCRAPE | "Hair can be difficult to shoot underwater. It floats while your model is descending, sometimes into her face." |
| Q29 | F18 Brett Stanley | SCRAPE | "Lighter fabrics (organza, chiffon, etc) will take longer to sink, giving you more time to pose with them" |
| Q30 | F18 Brett Stanley | SCRAPE | "Bubbles are good, so feel free to let some out as you pose, but only if your head is back as they might obscure your face." |
| Q31 | F18 Brett Stanley | SCRAPE | "Natural fabrics tend to go darker once wet, so test them if there's a certain colour you'd like." |
| Q32 | F16 franreina | WEBFETCH | "A simple move of your head back and forth lets your hair float naturally" |
| Q33 | F25 morphic | SCRAPE | "Ask for hair and fabric to lift upward, bubbles to rise and shrink, and surface light to move across the face in bands. Then set the depth and the direction of the light. Asking only for a blue tint gives you a dry portrait with a colour grade on it." |
| Q34 | F25 morphic | SCRAPE | "Long loose hair, a light scarf or a full skirt all read strongly, since drifting fabric is one of the clearest signals that the subject is submerged." |
| Q35 | F24 vibemeai | SCRAPE | "Images often look fake when the face becomes too smooth, bubbles appear randomly, or the lighting direction does not match the scene. Improve results by prompting for natural skin texture, clean facial detail, and one consistent light source." |
| Q36 | F10 media.io | WEBFETCH | "plastic skin, messy refraction around the face, and random bubbles that look like noise" (sección de errores comunes) |
| Q37 | F13 stable-diffusion-art | SCRAPE | "underwater photography portrait, dress, [amber heard: emma watson :0.6], floating hair, bubbles, sun light breaking through water surface, by ted grambeau" |
| Q38 | F13 stable-diffusion-art | SCRAPE | "**Sunlight through water surface** is used to both generate a stronger lighting effect and make the water surface visible" |
| Q39 | F12 arXiv 2505.19895 | WEBFETCH | "Underwater images are often affected by complex degradations such as light absorption, scattering, color casts, and artifacts" |
| Q40 | F8 uwphotographyguide strobes | WEBFETCH | "your strobes will light up your subject but pass through the open water, as there is nothing to reflect the light back, thus creating the black background effect." |
| Q41 | F25 morphic | SCRAPE | "their own reflection visible on the underside of the surface directly above them so the portrait appears twice" |
| Q42 | F17 divephotoguide | SCRAPE | "Since I started using it, my image stability has improved significantly as I now have that continuous visual reference for a horizon line." |

## Fase 4 — Tabla de veredictos

| Regla [A PRUEBA] (texto exacto) | Veredicto | URLs que lo sostienen | Nota |
|---|---|---|---|
| §1 "Cargar cuando la cámara y el sujeto están completamente sumergidos." | SIN EVIDENCIA (no aplicable) | — | Enrutamiento; sugerir `[TAXONOMIA]`. |
| §1 "Si el cuadro incluye la superficie desde abajo, este archivo manda; si la cruza, cargar además `02-agua-ruptura.md`." | SIN EVIDENCIA (no aplicable) | — | Ídem. |
| §2.1 "El agua absorbe primero los rojos: a pocos metros la piel, la sangre y los objetos rojos se ven pardos o grises salvo que una luz artificial cercana los recupere; un rojo saturado a profundidad sin fuente cercana es un error físico." | CONFIRMADA EN CAMPO | https://www.uwphotographyguide.com/underwater-photography-lighting-fundamentals (Q1–Q3) · https://dan.org/alert-diver/article/recovering-color-in-underwater-photography/ (Q4, Q5) · https://blog.fotografit.eu/guide-to-underwater-photography-lighting/ (Q8) | 3 fuentes [QUOTED]. Cifras: pérdida notable de rojo desde 1.5 m; rojo desaparece ~4.5 m (15 ft); sólo verde/azul después de 18 m. Matiz: **la distancia horizontal cámara-sujeto cuenta igual que la profundidad** (Q2). |
| §2.2 "La luz entra desde la superficie y se descompone en haces cuando hay una abertura o partículas; en un cenote los haces caen desde la boca de la caverna y son la única fuente motivada." | CONFIRMADA EN CAMPO (haces desde la boca) · el sub-claim "partículas" ver §4 | https://dan.org/alert-diver/article/light-in-the-dark-shooting-cenotes/ (Q14–Q16) · https://www.waterdogphotographyblog.com/caves-caverns-and-cenotes/ (Q18) · https://www.victorherrera.net/... (Q19) | Los haces dependen de superficie calma + sol brillante + fondo oscuro [QUOTED Q14, Q18]. |
| §2.3 "Las cáusticas sobre el fondo o sobre el sujeto son la firma de una superficie iluminada por sol; sin sol directo no hay cáusticas." | CONFIRMADA EN CAMPO | https://atoptics.co.uk/blog/lake-caustics/ (Q20) · https://www.scienceofsurfing.com/p/light (Q21, Q22) · ikelite (Q13, rayos) · victorherrera (Q19, haz) | Añadir dos condiciones que las fuentes exigen: **algo de rizado** (superficie totalmente plana no enfoca, Q22) y agua clara/poco profunda. |
| §2.4 "Las burbujas suben verticales y son la brújula del cuadro: indican dónde está arriba y, en racimo desde el regulador, marcan una exhalación reciente, es decir un cambio de estado." | CONFIRMADA EN CAMPO | Brett Stanley (Q30) · morphic (Q33) · Vox (ver 02: burbujas suben y "hierven" en superficie) · snippet katejonker/insidescuba: "take your shot once the model has exhaled and the bubbles are clear of their face and slightly above their head" | Verticalidad = física trivial; el uso de la exhalación como beat está en la práctica real (Q30, snippet). |
| §2.6 "El pelo y la tela flotan y se separan del cuerpo; una melena pegada a la cabeza o una camiseta caída se leen como aire." | CONFIRMADA EN CAMPO | expertphotography (Q28) · Brett Stanley (Q29) · franreina (Q32) · morphic (Q33, Q34) | 4 fuentes. Matices reales: telas pesadas se hunden y las naturales oscurecen al mojarse (Q29, Q31); el pelo que flota **totalmente vertical** se lee "posado" (snippet submerge). |
| §2.7 "La partícula en suspensión cerca de la lente, el backscatter, existe siempre que hay luz frontal; un agua perfectamente limpia se lee como aire teñido de azul." | CONFIRMADA EN CAMPO (mecanismo) · **REFUTADA en el "siempre" y en "agua limpia = aire"** | https://www.uwphotographyguide.com/backscatter-underwater (Q9, Q10) · ikelite (Q12) · Q11 | El mecanismo luz-frontal-cerca-de-lente ⇒ backscatter es correcto [QUOTED Q9, Q10]. Pero los profesionales **buscan** agua limpia (Q11) y la claridad **mejora** haces y alcance (Q12): el agua limpia no se lee como aire; se lee como agua por la pérdida de contraste, los haces y la luz de superficie. Reescribir: "backscatter es la consecuencia de luz frontal cerca de la lente; usarlo con moderación; nunca declararlo obligatorio". |
| §3 "Para un nadador rápido: sujeto nítido y estela de burbujas barrida detrás, nunca el fondo barrido, porque bajo el agua el fondo casi nunca es legible." | SIN EVIDENCIA | (indirecto) uwphotographyguide "Slow Shutter Speeds in Underwater Photography" apareció en búsqueda #6 de la familia 02 pero no fue leído | Ninguna fuente leída trata blur de estela de burbujas. Hipótesis razonable, sin campo. |
| §4 "Los haces de luz son atmósfera y solo existen con partículas; pedir haces sin partículas produce rayos dibujados." | **REFUTADA** (en su forma absoluta) | https://www.ikelite.com/blogs/advanced-techniques/chasing-light-rays (Q12) · https://dan.org/alert-diver/article/light-in-the-dark-shooting-cenotes/ (Q14–Q16) · waterdog (Q18) | Una fuente profesional lo contradice de frente: "turbidity isn't necessary. The clearer your water the farther your light (and rays) will go" [QUOTED Q12]. DAN y Waterdog atribuyen los haces a **superficie calma + sol fuerte + fondo oscuro + sobreexposición**, sin mencionar partículas (Q14, Q16, Q18). Regla sustituta candidata abajo (H1). Conservar la línea con `[REFUTADA: https://www.ikelite.com/blogs/advanced-techniques/chasing-light-rays]`. |
| §5 "Lente ancha, 24mm o menos, y cerca del sujeto: bajo el agua la distancia come contraste, así que la cámara se acerca en vez de cerrar plano con tele." | CONFIRMADA EN CAMPO | uwphotographyguide cenotes (Q24: 16 mm) · uwphotographyguide (Q2, Q26) · backscatter ("Only take photos within a few inches of your port… with a fisheye lens") · DAN cenotes ("Fisheye lenses are usually the default choice in caverns") | 4 fuentes [QUOTED]. |
| §5 "El rig es una carcasa con domo; la deformación de gran angular y la ligera viñeta del domo son texturas legítimas del régimen." | CONFIRMADA EN CAMPO (domo + gran angular) · matiz en "texturas legítimas" | Q24 · Q27 · DAN splits ("did not think it did a good job with corner sharpness at 11mm") · uwphotographyguide cenotes ("Bigger domes can also help with increasing overall image sharpness") | Distorsión de ojo de pez y esquinas blandas son reales, pero los profesionales las tratan como **defectos a minimizar** (Q24). Ninguna fuente habla de "viñeta"; hablan de esquinas blandas. Sustituir "viñeta" por "esquinas ligeramente blandas". |
| §7 "La piel bajo el agua se describe con su viraje real, cálida solo bajo la linterna; skin_doc sigue aplicando en textura, no en color." | CONFIRMADA EN CAMPO (con alternativa documentada) | dan.org (Q5–Q7) · fotografit (Q8) · vibemeai (Q35: "natural skin texture") | Matiz importante: en fotografía real la piel cálida sin práctico visible sí existe vía balance de blancos, pero entonces **el agua vira a aqua y los rayos de sol a rojizo** (Q6, Q7). Criterio de crítico: piel cálida + agua azul pura + rayos blancos + sin práctico = incoherente. |
| §8 "El agua parece aire azul: faltan partículas, haces o pérdida de contraste con la distancia; añadir las tres, una por cláusula." | CONFIRMADA EN CAMPO (fallo) · corrección parcial | morphic (Q33: "dry portrait with a colour grade") · vibemeai (Q35) · media.io (Q36) · arXiv 2505.19895 (Q39) | El fallo "aire teñido" está documentado por 2 blogs de prompts + 1 paper de degradaciones. Las correcciones de campo priorizan **pelo/tela flotando, burbujas ascendentes y bandas de luz de superficie** (Q33, Q34); "partículas" no es obligatoria (ver §4). |
| §8 "Piel rosada y labios rojos a diez metros: color físicamente imposible sin práctico; declarar el viraje o añadir la linterna como fuente." | CONFIRMADA EN CAMPO | Q1, Q4, Q5, Q8 | A 10 m el rojo ya no llega (Q5: sólo verde/azul tras 18 m; rojo desaparece a ~4.5 m). |
| §8 "Burbujas que van de lado o hacia abajo: el modelo perdió la vertical; declarar 'bubbles rising straight up toward the surface'." | CONFIRMADA EN CAMPO (burbujas aleatorias como fallo) | vibemeai (Q35: "bubbles appear randomly") · media.io (Q36: "random bubbles that look like noise") · morphic (Q33: "bubbles to rise and shrink") | Dos fuentes reportan burbujas aleatorias como fallo típico; la corrección de campo es exactamente "rising… toward the surface". La dirección lateral/descendente específica no aparece textual [DERIVED]. |
| §8 "Pelo y tela pegados al cuerpo: pedir flotación explícita." | CONFIRMADA EN CAMPO | morphic (Q33, Q34) · stable-diffusion-art (Q37: "floating hair") | La cita Q33 es literalmente la regla. |
| §9 "Absorción de color coherente con la profundidad declarada." | CONFIRMADA EN CAMPO | Q1–Q5 | Duplicado de §2.1; añadir "y con la distancia horizontal" (Q2). |
| §9 "Partículas, haces o pérdida de contraste presentes." | CONFIRMADA EN CAMPO (parcial) | Q12, Q14, Q33 | "Haces o pérdida de contraste" sí; "partículas" no es requisito (ver §4 REFUTADA). |
| §9 "Burbujas verticales; racimo reciente si hay cambio de estado." | CONFIRMADA EN CAMPO | Q30, Q33, Q35 | Duplicado de §2.4. |
| §9 "Pelo y tela flotando." | CONFIRMADA EN CAMPO | Q28, Q29, Q32–Q34 | Duplicado de §2.6. |

Resumen sobre 22 líneas: 17 CONFIRMADAS EN CAMPO (4 con matiz o corrección de redacción; 1 de ellas con el "siempre" refutado) · **1 REFUTADA** (§4 haces sólo con partículas) · 4 SIN EVIDENCIA (2 no aplicables + §3 nadador rápido + una parte de §2.7 ya contada como matiz).

## Fase 4b — Hallazgos nuevos (reglas candidatas)

1. **Siempre** que el beat sean haces de luz: cámara en la penumbra mirando hacia la luz, superficie fuera de cuadro y exposición alta, para que los haces sean lo más brillante del encuadre; la condición física es superficie calma + sol fuerte + fondo oscuro, no turbidez. `[CAMPO: https://dan.org/alert-diver/article/light-in-the-dark-shooting-cenotes/ · https://www.ikelite.com/blogs/advanced-techniques/chasing-light-rays · https://www.waterdogphotographyblog.com/caves-caverns-and-cenotes/]` (Q12, Q14–Q16, Q18). Sustituye a la regla refutada.
2. **Nunca** añadir un práctico frontal en un cuadro de haces salvo que haya un sujeto en primer plano que lo justifique; el flash "arruina la atmósfera". `[CAMPO: https://dan.org/alert-diver/article/light-in-the-dark-shooting-cenotes/]` (Q17).
3. **Debe** declararse la distancia cámara-sujeto además de la profundidad: el color se pierde con el camino total de la luz (10 ft de profundidad + 10 ft de distancia = 20 ft, sin rojos). `[CAMPO: https://www.uwphotographyguide.com/underwater-photography-lighting-fundamentals]` (Q2).
4. Criterio del crítico: si la piel es cálida sin práctico visible, el agua **debe** virar a aqua/cian y los rayos de sol a rojizo (firma del balance de blancos); piel cálida con agua azul pura y rayos blancos es incoherente. `[CAMPO: https://dan.org/alert-diver/article/recovering-color-in-underwater-photography/]` (Q6, Q7).
5. **Nunca** pedir "solo un tinte azul" para sumergir un retrato: sin pelo/tela que se levanten, burbujas que suben y bandas de luz de superficie sobre la piel, el resultado es un retrato seco con un grade encima. `[CAMPO: https://morphic.com/resources/vfx/underwater-portrait-effect]` (Q33, Q34).
6. **Debe** pedirse una sola fuente de luz consistente y textura de piel natural; los fallos típicos reportados son piel demasiado lisa, burbujas aleatorias y dirección de luz que no coincide. `[CAMPO: https://www.vibemeai.net/trending/underwater-prompt · https://www.media.io/ai-prompts/gemini-ai-underwater-prompt.html]` (Q35, Q36). Confirma U8 desde el campo.
7. **Debe** declararse la haloclina cuando el cenote la tiene: la capa se ve como "sheet of glass" intacta y como neblina borrosa al cruzarla; la borrosidad es del agua, no del foco. `[CAMPO: https://www.uwphotographyguide.com/top-11-tips-for-cenote-photography/]` (Q23).
8. Backlight con luces de video detrás del sujeto produce un "halo" legítimo y muy usado en cenotes; es la variante de silueta con rim que la familia ya contempla, ahora con fuente de campo. `[CAMPO: https://www.uwphotographyguide.com/top-11-tips-for-cenote-photography/]` (Q25).
9. En POV de máscara o puerto plano los objetos se ven ~33 % más grandes y ~25 % más cerca; con domo no. Declarar el tipo de puerto cuando el tamaño relativo importa. `[CAMPO: https://www.uwphotographyguide.com/underwater-photography-lighting-fundamentals]` (Q27).
10. Burbujas y rostro: las burbujas de exhalación tapan la cara salvo que la cabeza esté atrás; el instante correcto es cuando el racimo ya pasó por encima de la cabeza. `[CAMPO: https://www.underwater-photographer.com/underwater-modelling-hints-tips/]` (Q30).
11. Desde abajo, la superficie calma **refleja** al sujeto en su cara inferior (el retrato aparece dos veces): es física legítima, no el fallo de "dos superficies" de la familia 02. `[CAMPO: https://morphic.com/resources/vfx/underwater-portrait-effect]` (Q41).
12. Telas: las ligeras (organza, gasa) flotan más tiempo; las naturales oscurecen al mojarse. Declarar el tipo de tela cuando se pide flotación. `[CAMPO: https://www.underwater-photographer.com/underwater-modelling-hints-tips/]` (Q29, Q31).

## Fase 5 — Forbidden patterns scan

- Sin autoridades sin URL; sin metadatos inventados (fechas de los scrapes: uwphotographyguide backscatter 2009-05-25 / mod. 2025-08-15; cenotes 2021-05-25; DAN color 2023-11-20; stable-diffusion-art 2022-11-20; Brett Stanley 2026-06-26; expertphotography mod. 2025-04-04; divephotoguide 2020-09-05; arXiv 2505.19895 2025-05-26).
- La cita snippet sobre "exhaled and the bubbles are clear of their face" se etiqueta como snippet.
- Sin detecciones.

## Fase 6 — Audit checklist

- [x] 5+ queries (11)
- [x] 7+ fetch attempts (29)
- [x] 4+ fetches exitosos con quotes (23 con contenido; 18 con citas)
- [x] 4+ fuentes profesionales (8)
- [x] 2+ anti-patrón/contraprueba (4)
- [x] Cada veredicto con Q#
- [x] Etiquetas epistémicas en notas
- [x] Sin paráfrasis como cita
- [x] Sin autoridad sin URL
- [x] Forbidden scan ejecutado · sin detecciones
- [x] Limitaciones presentes

## Limitaciones

- Reddit (r/Bard, r/GoogleGeminiAI, r/StableDiffusion) inaccesible por las dos herramientas; las fuentes "de campo" de IA son blogs de prompts (media.io, vibemeai, morphic, stable-diffusion-art), no hilos de usuarios.
- Las guías oficiales de Google/DeepMind para Nano Banana no contienen nada específico de agua (F26 de la familia 01 y query #6 aquí); no hay evidencia oficial sobre cómo NBP trata el viraje de color subacuático.
- scubadiving.com (403), divephotoguide "Basic Principles of Light Underwater" (503), NOAA Ocean Explorer (404) y Hugging Face Underwater XL (401) no pudieron leerse.
- La refutación de §4 se apoya en una fuente directa (Ikelite) más dos que omiten las partículas (DAN, Waterdog). Físicamente el agua pura sí dispersa algo de luz (Rayleigh), por lo que "haces sin ninguna partícula" sigue siendo posible en agua real; esa precisión es inferencia mía [INFERRED] y no está en las fuentes leídas.

## Sugerencia próximo paso

Ejercicio real en NBP: cenote con "calm surface, bright sun, camera in the dark looking toward the light, surface hidden, no particles declared" vs la misma génesis con "suspended particles"; comparar si los haces salen dibujados sin partículas (la regla refutada predice que sí; Ikelite predice que no). Segunda prueba: retrato de apneísta a 10 m sin práctico, verificar viraje de piel y color del agua contra la candidata 4.
