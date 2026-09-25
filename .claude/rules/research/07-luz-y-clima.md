# Investigación de campo — Familia 07: Luz y clima

Archivo bajo prueba: `.claude/rules/regimenes/07-luz-y-clima.md` (BORRADOR 2026-09-25).
Fecha de acceso de todas las URLs: **2026-09-25**. Protocolo: skill `research` v2, seis fases.
Herramientas: WebSearch, Firecrawl (search/scrape), WebFetch, curl + extracción de texto para verificación char-level.
Ninguna herramienta de generación (Higgsfield u otras) fue usada.

Criterio de veredicto (dado por el encargo): **CONFIRMADA EN CAMPO** = dos fuentes independientes con
ejemplo concreto o física verificable; **REFUTADA** = una fuente sólida la contradice con evidencia;
**SIN EVIDENCIA** = nada concluyente.

## Fase 1 — Pre-flight

```
TEMA: evidencia de campo para las 6 líneas [A PRUEBA] de la familia 07 (rayo, lluvia, niebla,
      mojado, halación) en generación de imagen (NBP / NB2 / GPT Image 2) y en fotografía real.
PROPÓSITO DOWNSTREAM: decidir qué líneas pasan a [CAMPO: url] o [REFUTADA: url] antes del
      ejercicio de canonización.
MÍNIMOS: 5+ queries · 7+ fetch attempts · 4+ exitosos · 4+ fuentes profesionales · 2+ anti-patrón.
```

## (1) Bitácora cuantitativa

### Queries (15 ejecutadas, 3 anti-patrón)

| # | Herramienta | Query | Resultado |
|---|---|---|---|
| 1 | Firecrawl search ×6 (paralelo) | rayo/lluvia/niebla/mojado (seis variantes) | ❌ HTTP 429 en las seis; se repitieron con WebSearch |
| 2 | WebSearch | lightning photography overexposed bolt core halation | ✅ 9 res. (Weingart, Stu Short, DPReview) |
| 3 | WebSearch | rain photography backlight flash behind subject streaks shutter speed | ✅ 9 res. (DIYP/Ilko Alexandroff, Canon Asia, Nick Dale) |
| 4 | WebSearch | reddit stable diffusion midjourney rain character looks dry wet skin hair | ✅ 9 res., ninguno de Reddit; PromptHero con prompts de comunidad |
| 5 | WebSearch | AI generated lightning bolt doesn't light the scene fake prompt fix | ⚠ 9 res., mayoría Medium/SEO; útil solo media.io |
| 6 | WebSearch | nano banana pro prompt fog rain weather realistic lighting | ✅ Google Cloud blog, dev.to/googleai |
| 7 | WebSearch **(anti-patrón)** | AI image rain mistakes wet ground reflections missing dry street | ✅ aiformule.com, cyberlink |
| 8 | WebSearch | reddit lightning strike prompt tips illuminate clouds ground | ⚠ genérico, sin Reddit |
| 9 | WebSearch | wet look photography rain portrait wet hair specular glycerin | ✅ DIYP "5 ways wet skin" |
| 10 | WebSearch | aerial perspective fog distant objects lower contrast bluer | ✅ Wikipedia, Shutterbug, D5 |
| 11 | WebSearch **(anti-patrón)** | AI generated storm sky looks fake oversaturated HDR tell-tale signs | ✅ Forbes/M. Shepherd (403 al leer), Fox Weather |
| 12 | Firecrawl search | site:reddit.com lightning prompt looks fake illuminate | ✅ 8 hilos (r/generativeAI 1voxm8r, r/midjourney 1ik2c75) — **no legibles** (ver fetches) |
| 13 | Firecrawl search **(anti-patrón)** | site:reddit.com rain prompt wet hair character looks dry | ✅ r/NovelAi 18b1vqg, r/GeminiAI 1ohwx9q — **no legibles** |
| 14 | WebSearch | "nano banana" OR gemini lightning prompt illuminates clouds | ⚠ librerías de prompts; media.io |
| 15 | WebSearch | site:youtube.com AI prompt lightning storm rain tutorial | ✅ Tao Prompts "Complete Guide to Lighting in Midjourney" |

### Fetches (22 intentos, 13 exitosos)

| # | URL | Método | Resultado |
|---|---|---|---|
| F1 | https://www.diyphotography.net/20-gorgeous-backlit-rainy-photos-tutorial-take/ | WebFetch → curl | WebFetch devolvió solo navegación; **curl OK** (31 KB texto), citas verificadas char-level |
| F2 | https://www.jasonrweingart.com/blog/2014/12/20/how-to-photograph-lightning | WebFetch + curl | ✅ ambos; verificado char-level |
| F3 | https://stushort.com/lightning-photography-guide-2/ | WebFetch + curl | ✅ ambos; verificado char-level (fecha en página 10/01/2023) |
| F4 | https://snapshot.canon-asia.com/article/eng/how-to-take-beautiful-photos-in-the-rain | WebFetch | ❌ 403 |
| F5 | https://aiformule.com/blog/reflections-ai-photos | WebFetch + curl | ✅ (fecha 2026-07-20) |
| F6 | https://www.cyberlink.com/blog/photo-effects/5116/ai-rain-effect | WebFetch | ❌ 410 Gone |
| F7 | https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana | WebFetch + curl | ✅ (fecha 2026-03-06) |
| F8 | https://www.nickdalephotography.com/blog/how-to-photograph-in-the-rain | WebFetch + curl | ✅ |
| F9 | https://www.diyphotography.net/5-ways-to-achieve-that-wet-skin-look-in-your-photos/ | curl | ✅ |
| F10 | https://en.wikipedia.org/wiki/Aerial_perspective | curl | ✅ |
| F11 | https://www.forbes.com/sites/marshallshepherd/2026/01/14/5-tips-for-spotting-fake-ai-generated-weather-images/ | curl + WebFetch ×2 | ❌ 403 (solo snippet de búsqueda) |
| F12 | https://www.foxweather.com/learn/real-or-fake-weather-photos-ai | curl | ✅ (contenido débil: quiz real/fake) |
| F13 | https://www.accuweather.com/en/weather-news/ai-weather-photos-how-to-tell-fact-from-fiction/1746888 | curl | ❌ bloqueado (492 bytes) |
| F14 | https://www.media.io/image-effects/ai-lightning-effect.html | curl | ✅ (página de producto; prompts de ejemplo) |
| F15 | https://tensor.art/articles/874217846148748264 | curl | ❌ shell JS vacío |
| F16 | https://prompthero.com/search?model=Stable+Diffusion&q=wet+clothes | curl | ✅ (prompts de comunidad) |
| F17 | https://filmora.wondershare.com/ai-prompt/gemini-ai-rain-effect-prompt.html | curl | ✅ (marketing; poco valor) |
| F18 | https://freeaipromptmaker.com/blog/2026-02-24-master-ai-art-weather-time-prompts | curl | ❌ texto vacío |
| F19 | https://www.youtube.com/watch?v=uEBihQiuxzY (Tao Prompts, 2023-07-23) | Firecrawl scrape | ✅ descripción + transcripción automática |
| F20 | https://www.reddit.com/r/NovelAi/comments/18b1vqg/… | pullpush.io API | ❌ rate limit; reddit.com y WebFetch bloqueados |
| F21 | https://www.reddit.com/r/GeminiAI/comments/1ohwx9q/… | pullpush.io API | ❌ idem |
| F22 | https://www.reddit.com/r/generativeAI/comments/1voxm8r/… | pullpush.io API | ❌ idem |

Fuentes profesionales que cuentan (definición del skill): Google Cloud blog (doc oficial de proveedor),
Jason Weingart (fotógrafo de tormentas profesional, guía técnica), Stu Short (fotógrafo de tormentas,
guía técnica con datos de exposición), DIYP/Ilko Alexandroff (tutorial de fotógrafo profesional con
setups de luz), Wikipedia Aerial perspective (óptica, con referencias), everypixel.com (benchmark con
metodología publicada, ver 08). Total: 6.

## (2) Citas verbatim

Todas char-level contra el texto extraído con curl salvo marca `[WEBFETCH]` (solo resumen de WebFetch),
`[TRANSCRIPT]` (transcripción automática de YouTube vía Firecrawl) o `[SNIPPET-ONLY]`.

| Q# | URL | Cita verbatim |
|---|---|---|
| Q1 | https://stushort.com/lightning-photography-guide-2/ | "This is when I have to be most careful as it is all too easy to overexpose and blow out the lightning. Just a couple of f-stops can make the difference between luminous, colourful bolts and a fully blown out image." |
| Q2 | https://stushort.com/lightning-photography-guide-2/ | "Knowing then that an unobscured bolt will be too bright to expose for, it's all about minimising that overexposure so as to effectively capture the aura of the strike and the colours in the branches." |
| Q3 | https://stushort.com/lightning-photography-guide-2/ | "as lightning acts as a flash, it will illuminate the scene into sharp relief." |
| Q4 | https://stushort.com/lightning-photography-guide-2/ | "They end up looking translucent and ghostly, which may be the aesthetic choice you're aiming for, but then you miss all the stunning colours in the aura and in the branches." |
| Q5 | https://www.jasonrweingart.com/blog/2014/12/20/how-to-photograph-lightning | "You want to be sure your lightning isn't overexposed, but at the same time you need to have some light in your foreground to add depth to the image." |
| Q6 | https://www.jasonrweingart.com/blog/2014/12/20/how-to-photograph-lightning | "If it's closer and/or strobing several times, you need to stop down your aperture, and keep the ISO relatively low to prevent blowout." |
| Q7 | https://www.diyphotography.net/20-gorgeous-backlit-rainy-photos-tutorial-take/ | "The first setup involves only a bare flash as the backlight. This will "freeze" all the water droplets in the air, and your subject will be a silhouette." |
| Q8 | https://www.diyphotography.net/20-gorgeous-backlit-rainy-photos-tutorial-take/ | "Generally, the backlight should be hidden behind your subject in order to illuminate the model and the rain properly." |
| Q9 | https://www.diyphotography.net/20-gorgeous-backlit-rainy-photos-tutorial-take/ | "If you want only to light the rain drops and don't want the background to show, you should use faster shutter speed (1/200). If you want to include the background, go for the slower shutter speed." |
| Q10 | https://www.nickdalephotography.com/blog/how-to-photograph-in-the-rain | "At slow shutter speeds (anything less than 1/100), you'll get long, blurred streaks that are quite faint. Somewhere in the middle (around 1/160) is the sweet spot, where you get streaks that are long enough to suggest movement but still clearly visible." |
| Q11 | https://www.nickdalephotography.com/blog/how-to-photograph-in-the-rain | "(1/500+), the drops will be frozen, so they'll appear small and round." |
| Q12 | https://www.nickdalephotography.com/blog/how-to-photograph-in-the-rain | "Streaks of rain catch the light, so you make them more visible by shooting into the sun (or any available light). Backlighting will help illuminate the raindrops, so they'll stand out against the background." |
| Q13 | https://aiformule.com/blog/reflections-ai-photos | "A mirror showing a different outfit, a shop window reflecting an empty street while people are standing there, or wet asphalt with light streaks coming from nowhere: it is one of the fastest ways an otherwise convincing image still reads as fake." |
| Q14 | https://aiformule.com/blog/reflections-ai-photos | "Wet road surface mainly throws back vertical light sources as long streaks running toward the camera." |
| Q15 | https://aiformule.com/blog/reflections-ai-photos | "That is why a puddle at your feet shows you almost nothing while the same puddle further down the street hands back the entire skyline." |
| Q16 | https://aiformule.com/blog/reflections-ai-photos | "If you want a strong reflection, put the camera low and look across the surface instead of down onto it." |
| Q17 | https://en.wikipedia.org/wiki/Aerial_perspective | "As the distance between an object and a viewer increases, the contrast between the object and its background decreases, and the contrast of any markings or details within the object also decreases. The colours of the object also become less saturated and shift toward the background colour, which is usually bluish" |
| Q18 | https://www.diyphotography.net/5-ways-to-achieve-that-wet-skin-look-in-your-photos/ | "Now with cameras being far more capable, we love that skin sheen as it helps to sculpt and shape the body through highlight and tone that's simply not possible with dry, flat looking skin." |
| Q19 | https://www.diyphotography.net/5-ways-to-achieve-that-wet-skin-look-in-your-photos/ | "Once the skin has been oiled first, this can then be sprayed on top to get that beaded water effect." |
| Q20 | https://prompthero.com/search?model=Stable+Diffusion&q=wet+clothes | "3/4 shot photograph of a woman with messy blonde highlights walks in the rain, wet hair, wet clothes, wet skin: insanely detailed, elegant, intricate sharp details, cinematic, masterpiece, UHD, natural light, realistic" |
| Q21 | https://www.media.io/image-effects/ai-lightning-effect.html | "multiple bright white-blue forked lightning strikes from dark storm clouds to the ground, lightning illuminates the clouds from within with electric glow" |
| Q22 | https://www.media.io/image-effects/ai-lightning-effect.html | "Add vivid lightning bolts to the background sky behind this person, keep the person unchanged and face sharp, lightning illuminates the subject with a dramatic cinematic electric glow" |
| Q23 | https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana | "Tell the model exactly how the scene is illuminated." `[WEBFETCH]` |
| Q24 | https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana | "You can mix up to 14 reference object images in a single prompt." |
| Q25 | https://www.youtube.com/watch?v=uEBihQiuxzY | "one of my favorites is foggy the color tones are similar to cloudy but there's a slightly opaque texture to the photo" `[TRANSCRIPT]` |
| Q26 | https://www.youtube.com/watch?v=uEBihQiuxzY | "mid Journey can't separate between left and right this is also true for lighting I tried different ways of getting lighting from the left or the right but was unsuccessful" `[TRANSCRIPT]` (Midjourney, 2023) |
| Q27 | https://research.everypixel.com/gpt-image-2-0/ | "Evaluators also flagged fluid physics and overly regular details such as evenly spaced droplets." |
| Q28 | https://www.foxweather.com/learn/real-or-fake-weather-photos-ai | "Double lightning bolts Is this lightning striking offshore real or fake? (FOX Weather) This lightning is fake." |
| Q29 | https://www.reddit.com/r/NovelAi/comments/18b1vqg/how_do_i_make_the_ai_generated_people_wet_for/ | "How do I make the AI generated people wet? (For example water when in the rain)." `[SNIPPET-ONLY]` título del hilo |
| Q30 | https://www.reddit.com/r/GeminiAI/comments/1ohwx9q/ai_rain_effect_trend_how_to_generate_ai_rain/ | "Open Nano Banana app and upload a photo of yourself. · Insert this exact prompt: "A close-up portrait of a beautiful woman, standing under rain" `[SNIPPET-ONLY]` |

## (3) Tabla de veredictos

| Regla [A PRUEBA] (texto exacto) | Veredicto | URLs que lo sostienen | Nota |
|---|---|---|---|
| §1 "Cargar cuando el beat lo lleva un fenómeno de luz o de clima, con o sin persona en cuadro." | **SIN EVIDENCIA** (no evaluable en campo) | — | Regla de alcance editorial del repo; ningún foro o tutorial decide cuándo "cargar un archivo". Se canoniza por ejercicio propio, no por campo. |
| §1 "Si el clima es solo fondo de una acción humana, la familia de la acción manda y este archivo aporta la sección 4." | **SIN EVIDENCIA** (no evaluable en campo) | — | Idem. |
| §3 "Lluvia y nieve se congelan como trazos cortos e iguales en dirección, no como puntos ni como cortinas; la longitud del trazo es la cue de velocidad de obturación y debe ser una sola." | **CONFIRMADA EN CAMPO** (con matiz) | Q9 https://www.diyphotography.net/20-gorgeous-backlit-rainy-photos-tutorial-take/ · Q10, Q11 https://www.nickdalephotography.com/blog/how-to-photograph-in-the-rain | `[QUOTED]` (Q9, Q10) dos fotógrafos independientes: la longitud del trazo la fija la obturación (1/200 congela gotas, <1/100 trazos largos y débiles, ~1/160 trazos legibles). `[QUOTED]` (Q11) **matiz**: a 1/500+ la lluvia se lee como puntos redondos, así que "no como puntos" no es física sino elección de look; lo no negociable es una sola longitud y una sola dirección por cuadro. `[DERIVED]` (Q27) "gotas equidistantes" es una firma de render detectada por evaluadores humanos: pedir espaciado irregular. |
| §7 "Con lluvia, la piel y la ropa mojadas devuelven speculares y el pelo se pega; declararlo o el sujeto se lee seco bajo la lluvia." | **CONFIRMADA EN CAMPO** | Q18, Q19 https://www.diyphotography.net/5-ways-to-achieve-that-wet-skin-look-in-your-photos/ · Q20 https://prompthero.com/search?model=Stable+Diffusion&q=wet+clothes · Q29 https://www.reddit.com/r/NovelAi/comments/18b1vqg/ | `[QUOTED]` (Q18) la piel mojada modela por highlight; sin sheen la piel es "dry, flat". `[QUOTED]` (Q20) la comunidad declara explícitamente "wet hair, wet clothes, wet skin" además de "walks in the rain": la lluvia sola no moja al sujeto. `[SNIPPET-ONLY]` (Q29) el hilo existe con esa pregunta literal, no se pudo leer el cuerpo. Física + práctica de prompting concuerdan. |
| §8 "Rayo decorativo que no ilumina: declarar qué superficies recibe su luz y desde dónde." | **CONFIRMADA EN CAMPO** | Q3 https://stushort.com/lightning-photography-guide-2/ · Q5 https://www.jasonrweingart.com/blog/2014/12/20/how-to-photograph-lightning · Q21, Q22 https://www.media.io/image-effects/ai-lightning-effect.html | `[QUOTED]` (Q3) el rayo actúa como flash y saca la escena "into sharp relief": un rayo sin efecto en el mundo es físicamente falso. `[QUOTED]` (Q5) el primer plano debe recibir luz. `[QUOTED]` (Q21, Q22) los prompts de campo que funcionan declaran qué ilumina el rayo ("illuminates the clouds from within", "illuminates the subject"), justo el remedio que propone la regla. `[ABSENT]` no se encontró un hilo de foro que documente el fallo "rayo que no ilumina" con imagen; la evidencia comunitaria es indirecta (prompts que ya lo evitan). |
| §9 "[ ] Superficies mojadas si llueve; perspectiva aérea si hay niebla." | **CONFIRMADA EN CAMPO** | Q13, Q14 https://aiformule.com/blog/reflections-ai-photos · Q17 https://en.wikipedia.org/wiki/Aerial_perspective · Q25 https://www.youtube.com/watch?v=uEBihQiuxzY | `[QUOTED]` (Q13) el suelo mojado mal resuelto es "one of the fastest ways" de que una imagen AI se lea falsa. `[QUOTED]` (Q17) física de la perspectiva aérea: menos contraste, menos saturación, viraje al azul del fondo. `[QUOTED]` (Q25) un tutor de prompting describe la niebla como textura opaca que baja tonos. |

Resumen: **4 CONFIRMADAS EN CAMPO · 0 REFUTADAS · 2 SIN EVIDENCIA** (las dos de alcance editorial).

Reglas [FUENTE] que el campo además respalda (no estaban a prueba, se anotan para el crítico):
§2.8 núcleo quemado con halación → Q1, Q2, Q4, Q6 (los profesionales exponen para el aura y las ramas
porque el núcleo siempre clipea); §2.4 lluvia solo a contraluz → Q7, Q8, Q12; §4 "no HDR" → Q27
(regularidad y sobrecocido detectados por evaluadores).

## (4) Hallazgos nuevos (reglas candidatas)

1. Nunca pedir reflejos en suelo mojado sin un práctico visible que los origine; cada franja de luz
   en el asfalto debe corresponder a una fuente en cuadro o justo fuera de él, porque las franjas "que
   vienen de ninguna parte" son la delación más rápida de un render. `[QUOTED]` (Q13, Q14)
   [CAMPO: https://aiformule.com/blog/reflections-ai-photos]
2. Si se quiere que el charco o el asfalto devuelvan el skyline o los prácticos, la cámara debe ir baja
   y mirar a través de la superficie, nunca hacia abajo; el reflejo crece con el ángulo rasante (Fresnel).
   `[QUOTED]` (Q15, Q16) [CAMPO: https://aiformule.com/blog/reflections-ai-photos]
3. El rayo se describe siempre por su aura y sus ramas de color, nunca por detalle en el núcleo: el
   fotógrafo real expone para "the aura of the strike and the colours in the branches" porque el canal
   central siempre clipea. `[QUOTED]` (Q2, Q4)
   [CAMPO: https://stushort.com/lightning-photography-guide-2/]
4. La luz de contra para lluvia debe quedar oculta detrás del sujeto; si entra en cuadro, solo como
   flare controlado y declarado. `[QUOTED]` (Q8)
   [CAMPO: https://www.diyphotography.net/20-gorgeous-backlit-rainy-photos-tutorial-take/]
5. Nunca pedir gotas o partículas "uniformes": el espaciado regular de gotas y la regularidad de
   detalle fueron señalados por evaluadores humanos como fallo de GPT Image 2; declarar densidad y
   tamaño desiguales. `[QUOTED]` (Q27) [CAMPO: https://research.everypixel.com/gpt-image-2-0/]
6. La dirección de la luz debe declararse por ancla de la escena (ventana, farola, horizonte), nunca
   por "left/right" a secas: al menos un modelo (Midjourney, 2023) no distinguía izquierda de derecha
   para la luz; coherente con la regla R2 del repo de anclas legibles. `[QUOTED]` (Q26) `[INFERRED]`
   para NBP/GPT Image 2 no se probó. [CAMPO: https://www.youtube.com/watch?v=uEBihQiuxzY]
7. En lluvia, declarar siempre el look de obturación elegido con una sola palabra de longitud
   ("gotas congeladas" o "trazos cortos" o "trazos largos débiles") porque cada uno corresponde a un
   rango de obturación distinto y mezclarlos rompe la física. `[QUOTED]` (Q9, Q10, Q11)
   [CAMPO: https://www.nickdalephotography.com/blog/how-to-photograph-in-the-rain]
8. `[SNIPPET-ONLY]` Los tells meteorológicos de imagen falsa (combinaciones imposibles: arcoíris con
   sol en cuadro, rayo desde cúmulos de buen tiempo, imagen "demasiado cinemática") citados a
   M. Shepherd/Forbes no pudieron leerse (403). Queda como lead, no como regla.
   [https://www.forbes.com/sites/marshallshepherd/2026/01/14/5-tips-for-spotting-fake-ai-generated-weather-images/]

## Fase 5 — Forbidden patterns scan

☐ Ejecutado. Detecciones y correcciones: la afirmación de la búsqueda "Keep the group to 2-5 people"
(no pertenece a esta familia) y las citas de Canon Asia / Cyberlink se descartaron por no tener fetch
exitoso. Ninguna autoridad citada sin URL. Las citas de WebFetch y transcripción están etiquetadas.

## (5) Checklist de auditoría del skill

- [x] 5+ queries ejecutadas (15, visibles en bitácora)
- [x] 7+ fetch attempts (22)
- [x] 4+ fetches exitosos con quotes (13)
- [x] 4+ fuentes profesionales (6)
- [x] 2+ queries anti-patrón (3: #7, #11, #13)
- [x] Cada claim de veredicto/hallazgo lleva Q#
- [x] Cada claim lleva etiqueta [QUOTED]/[DERIVED]/[INFERRED]/[ABSENT]
- [x] Ninguna paráfrasis presentada como cita (WebFetch/transcript/snippet marcados)
- [x] Ninguna autoridad sin URL
- [x] Forbidden patterns scan ejecutado
- [x] Sección Limitaciones presente

## Limitaciones

- Reddit fue inaccesible por los cuatro caminos probados (reddit.com y old.reddit bloquean curl,
  WebFetch lo rechaza, Firecrawl no soporta el sitio, pullpush.io limitó tras una petición). Los hilos
  relevantes quedaron como títulos `[SNIPPET-ONLY]`.
- No se encontró ningún caso de foro con imagen adjunta que documente el fallo "rayo que no ilumina" en
  NBP o GPT Image 2; la confirmación es física + prompts de campo que ya incluyen la corrección.
- Forbes, Canon Asia, AccuWeather y Cyberlink bloquearon la lectura.
- Ninguna fuente compara NBP vs GPT Image 2 específicamente en lluvia/rayo; la asignación de modelo de
  la §6 sigue siendo del skill, no del campo.

## Próximo paso

Ejercicio real: un panel de rayo sobre skyline (NBP) y uno de lluvia a contraluz con persona (NBP con
referencia T1), verificando en el crítico: núcleo quemado + aura de color, superficie mojada con
reflejos que nacen de prácticos visibles, trazos de lluvia de una sola longitud, piel/pelo mojados
declarados. Con eso las cuatro CONFIRMADAS pasan a `[CANONICA fecha]`.
