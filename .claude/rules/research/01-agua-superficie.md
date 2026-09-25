# RESEARCH DE CAMPO — Familia 01 · Agua en superficie

Archivo auditado: `.claude/rules/regimenes/01-agua-superficie.md` (BORRADOR 2026-09-25).
Fecha de acceso de todas las URLs: **2026-09-25**. Protocolo: skill `research` v2 (6 fases).
Este archivo NO modifica la familia; sólo propone veredictos y reglas candidatas.

Convenciones de la columna "Método":
- `[SCRAPE]` — texto crudo obtenido con Firecrawl; la cita es verificable char-level con grep sobre la URL.
- `[WEBFETCH]` — cita extraída por WebFetch (modelo pequeño con instrucción de copiar verbatim); verificable con grep, pero con un eslabón intermedio.
- `[SNIPPET-ONLY]` — sólo apareció en el resumen del buscador; el cuerpo no se pudo leer. Estatus epistémico inferior.

## Fase 1 — Pre-flight

```
TEMA DE RESEARCH: evidencia de campo (foros de IA generativa, tutoriales, guías de fotografía
  de deportes acuáticos, física de fluidos) para las 11 reglas [A PRUEBA] de la familia 01.
PROPÓSITO DOWNSTREAM: canonizar ([CAMPO: url]) o refutar ([REFUTADA: url]) cada regla en
  01-agua-superficie.md; añadir reglas candidatas nuevas.
MÍNIMOS DE ESTA FAMILIA: 5+ queries · 7+ fetches · 4+ exitosos · 4+ fuentes profesionales · 2+ anti-patrón.
RESULTADO: 15 queries · 27 intentos de fetch · 20 con contenido útil · 7 fuentes profesionales · 5 anti-patrón.
```

## Fase 2 — Bitácora cuantitativa

### 2a. Queries

| # | Herramienta | Query | Ángulo | Resultado |
|---|---|---|---|---|
| 1 | firecrawl_search | wakeboarding photography tips tow rope spray backlight low angle boat tower | A best practices | 8 resultados (alliancewake, monstertower, jetboaters) |
| 2 | firecrawl_search | reddit stable diffusion water looks like gel jelly plastic splash prompt fix | B anti-patrón | 8 hilos r/StableDiffusion sobre "plasticky"; ninguno específico de agua |
| 3 | firecrawl_search | midjourney water splash prompt realistic droplets tips "splash" fake looking | A/B | 8 (promptatlas, banana-prompts, medium) |
| 4 | firecrawl_search | surf photography water housing shooting spray backlit sunrise tips guide | A | 8 (surfsimply, louloubphoto, uwphotographyguide, gdome, tonypalmer) |
| 5 | WebSearch | nano banana prompt water splash physics realistic tips reddit | A (modelo) | theneuralpost "physics prompting"; sin Reddit |
| 6 | WebSearch | AI image generation water physics fails splash wrong direction tilted horizon common problems | B/D anti-patrón | arxiv 2405.15406, arxiv 2607.25321, arxiv 2304.06470, gadrex |
| 7 | WebSearch | reddit midjourney surfing wakeboarding prompt spray realistic water wake tips | E casos | **Sin resultados pertinentes** (sólo Wikipedia y Shopify) |
| 8 | WebSearch | wetsuit skin wet specular highlights photography sports water shine why | C física | mdavid.com.au, diyphotography |
| 9 | WebSearch | reddit AI generated splash "looks like" glass OR frozen OR gel OR jelly water midjourney OR "stable diffusion" OR flux | B anti-patrón | **Sin resultados pertinentes** (stock images) |
| 10 | WebSearch | wakeboard photography rope tension slack "rope" photo tips rider edge spray pole cam | A/C | wakeworld "Low Rope Tension", buckeyemarine |
| 11 | WebSearch | AI generated image water horizon tilted OR crooked underwater surface "two horizons" OR "double horizon" generation problem | B anti-patrón | cliprise, zsky, lovino, p20v (genéricos) |
| 12 | WebSearch | gpt-image OR "gpt image" OR "dall-e" water splash refraction test realistic liquid prompt tips | A (modelo) | community.openai thread, pixverse, gadrex |
| 13 | firecrawl_search (developer) | water splash generation looks like glass frozen gel prompt issue stable diffusion | B anti-patrón | rapidata wine-glasses, gadrex; GitHub issues no pertinentes |
| 14 | WebSearch | oblique drop impact asymmetric splash crown physics angle of impact study | C física | arxiv 1611.05670, 2608.29762, MDPI Fluids 8(11):301, Cambridge |
| 15 | WebSearch | AI generated image rope OR leash OR cable "goes nowhere" OR "ends in mid-air" OR "floating rope" artifact | B anti-patrón | **Sin resultados pertinentes** |

Anti-patrón explícitas: #2, #6, #9, #11, #13, #15 (6). Dominio sin estándares formales (ángulo C cubierto con física de fluidos y óptica).

### 2b. Fetches

| # | URL | Método | Resultado |
|---|---|---|---|
| F1 | https://arxiv.org/html/2405.15406v1 | SCRAPE | 429 en 1er intento; ✅ 2º intento (114 KB, extraído con script) |
| F2 | https://alliancewake.com/wake/wake-photography-101-2/ | SCRAPE | 429 en 1er intento; ✅ 2º intento |
| F3 | https://www.louloubphoto.com/journal/camera-settings-surf-photography | WEBFETCH | ✅ |
| F4 | https://www.uwphotographyguide.com/5-tips-for-surf-photography/ | WEBFETCH | ✅ |
| F5 | https://www.tonypalmer.photos/blog/random-tips-for-surf-photography-and-water-housings/ | WEBFETCH | ✅ |
| F6 | https://theneuralpost.com/2025/12/10/mastering-nano-banana-the-physics-prompting-guide-for-perfect-lighting/ | WEBFETCH | ✅ (blog, 2025-12-10) |
| F7 | https://www.reddit.com/r/StableDiffusion/comments/1dab9zg/... | WEBFETCH | ❌ "unable to fetch from www.reddit.com" |
| F8 | https://old.reddit.com/r/StableDiffusion/comments/1dab9zg/... | SCRAPE | ❌ Firecrawl: "we do not support this site" |
| F9 | https://monstertower.com/blog/post/the-science-of-wake-... | WEBFETCH | ❌ 403 |
| F10 | https://www.diyphotography.net/5-ways-to-achieve-that-wet-skin-look-in-your-photos/ | WEBFETCH | ❌ sólo navegación, sin cuerpo |
| F11 | https://surfsimply.com/magazine/a-guide-to-getting-started-at-in-water-surf-photography-with-damea-dorsey | WEBFETCH | ✅ (sólo lente) |
| F12 | https://gadrex.com/ai-water-and-fluid-generation-prompts/ | WEBFETCH | ✅ (blog, feb 2026) |
| F13 | https://promptatlas.co/prompts/splash-photography-prompt | WEBFETCH | ✅ |
| F14 | https://arxiv.org/abs/2607.25321 | WEBFETCH | ✅ (abstract, 2026-07-28) |
| F15 | https://arxiv.org/abs/2304.06470 | WEBFETCH | ✅ abstract; sin frases sobre fluidos |
| F16 | https://www.buckeyemarine.com/news/wakeboarding-rope-tips | WEBFETCH | ✅ |
| F17 | https://www.surfertoday.com/surfing/underwater-surf-photography-tips-for-beginners | WEBFETCH | ❌ 403 |
| F18 | https://getgdome.com/blogs/gdome-blog/surf-photography-tips | WEBFETCH | ✅ |
| F19 | https://www.wakeworld.com/forum/showthread.php?t=806153 | SCRAPE + WEBFETCH | ❌ timeout ×2 |
| F20 | https://www.mdavid.com.au/photography/specularhighlights.shtml | WEBFETCH | ✅ |
| F21 | https://www.cliprise.app/learn/guides/best-practices/common-ai-image-artifacts-fixes | WEBFETCH | ✅ (sin contenido sobre horizonte) |
| F22 | https://lovino.ai/blog/how-to-fix-common-ai-image-problems | WEBFETCH | ✅ (sin contenido pertinente, 2026-03-05) |
| F23 | https://zsky.ai/blog/ai-image-artifacts-guide | WEBFETCH | ✅ (sin contenido pertinente, 2026-02-21) |
| F24 | https://community.openai.com/t/dalle3-and-gpt-image-1-prompt-tips-and-tricks-thread/498040 | WEBFETCH | ✅ (sólo un prompt de cóctel; nada de spray) |
| F25 | https://pixverse.ai/en/blog/gpt-image-2-review-and-prompt-guide | WEBFETCH | ✅ (sin agua; 1 cita sobre vocabulario) |
| F26 | https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana | WEBFETCH | ✅ (sin menciones de agua/física) |
| F27 | https://www.banana-prompts.net/splash-photography-prompt-for-beverage-can/ | WEBFETCH | ✅ (blog, 2026-02-19) |

Fuentes profesionales según definición del skill (papers, docs oficiales, publicaciones técnicas datadas con autor): F1 (arXiv), F14 (arXiv), F15 (arXiv), MDPI Fluids 8(11):301 (peer-reviewed, ver 02), arXiv 2608.29762 (ver 02), F2 (revista especializada, autor y fecha), F20 (fotógrafo técnico, explicación óptica). Los blogs de prompts (F6, F12, F13, F27) cuentan como **fuentes de campo**, no profesionales.

## Fase 3 — Citas verbatim

| Q# | URL | Método | Cita verbatim |
|---|---|---|---|
| Q1 | F2 alliancewake | SCRAPE | "There are two times during the day to get good light: dawn and dusk." |
| Q2 | F2 alliancewake | SCRAPE | "During the afternoons when the sun is high in the sky pictures can be very unflattering. The light source is now coming from above and casting harsh shadows across the rider's face (and everything else), often causing the picture to appear flat" |
| Q3 | F2 alliancewake | SCRAPE | "Shooting when the light is too high will leave too many shadows on the rider and the image will have less depth." |
| Q4 | F3 louloubphoto | WEBFETCH | "Some of my favourite surf photos were shot when I stopped trying to avoid shooting into the sun and started leaning into it instead." |
| Q5 | F3 louloubphoto | WEBFETCH | "Spray starts to glow. Reflections sparkle on the surface of the ocean." |
| Q6 | F3 louloubphoto | WEBFETCH | "If I want really blue tones after first light, I'll shoot with the sun behind me" |
| Q7 | F4 uwphotographyguide surf | WEBFETCH | "This setting will most likely yield excellent results, especially after sunrise and before sunset." |
| Q8 | F18 gdome | WEBFETCH | "Try to avoid strong direct sunlight, as this can create harsh shadows and overexposed images." |
| Q9 | F5 tonypalmer | WEBFETCH | "Sometimes the spray off the back of the wave can leave small mist of droplets on the lens, so I usually do a dunk and pull the port out of the water and let the water sheet run off leaving a clear port" |
| Q10 | F20 mdavid | WEBFETCH | "Shiny, wet surfaces tend to have strong, hard-edged specular highlights and matt surfaces tend to have weak soft-edged specular highlights." |
| Q11 | F16 buckeyemarine | WEBFETCH | "The non-stretch characteristic also helps to provide consistent tension for better control and trick execution" |
| Q12 | wakeworld (query #10) | SNIPPET-ONLY | "Rope tension is key to everything wakeboarding, whether its slack on a spin or gnarly tight tension on a raley." |
| Q13 | F13 promptatlas | WEBFETCH | "impossible gravity, frozen solid-looking fluid, random droplets, warped packaging, broken refraction, fake labels, logos, signatures, and watermarks" (bloque de negativos) |
| Q14 | F13 promptatlas | WEBFETCH | "Define one impact point and captured instant so the splash reads as an event rather than random liquid decoration." |
| Q15 | F13 promptatlas | WEBFETCH | "Use backlight to describe transparent edges while preserving a stable hero silhouette and contact shadow." |
| Q16 | F12 gadrex | WEBFETCH | "Why does my AI water sometimes look like blue smoke? This usually happens if you don't use keywords like "Refraction," "Transparency," or "Reflections." Without these, the AI treats the fluid as an opaque gas." |
| Q17 | F12 gadrex | WEBFETCH | "If the water doesn't distort the objects behind it, it won't look real." |
| Q18 | F14 arXiv 2607.25321 | WEBFETCH | "Video diffusion models generate visually compelling content but routinely violate elementary physics when the subject involves fluids: liquid columns break apart in mid-air, container water levels fail to rise as liquid is poured in, and splashes disperse without regard to momentum or gravity." |
| Q19 | F1 arXiv 2405.15406 | SCRAPE | "The splash is symmetric, and the physics behind this phenomenon involve the surface tension of the water and the forces exerted upon the initial impact, likely from a droplet falling into the water." |
| Q20 | arXiv 2608.29762 (abs) | WEBFETCH | "Oblique drop impact onto a deep liquid pool produces asymmetric crowns, directional jetting, and splashing transitions that cannot be characterized by the total impact inertia alone." |
| Q21 | MDPI Fluids 8(11):301 | SCRAPE | "This study investigates the asymmetric crown morphology resulting from an oblique impact (α= 60°) of a single droplet on a horizontal and quiescent wall film of the same liquid." |
| Q22 | F6 theneuralpost | WEBFETCH | "Nano Banana has an internal database of IOR (Index of Refraction) values." |
| Q23 | F25 pixverse | WEBFETCH | "Using decorative quality words for functional tasks. 'Beautiful' does not make a label readable." |
| Q24 | F27 banana-prompts | WEBFETCH | "Make sure to specify that the liquid is 'translucent' and that light should 'bend through the droplets.'" |
| Q25 | F21 cliprise | WEBFETCH | "State one light source and remove conflicting lighting terms." |
| Q26 | divephotoguide freediving (ver 03, F17) | SCRAPE | "One setting I'd suggest is customizing your camera's display so that it includes a little level indicator overlaying the picture" |
| Q27 | balazsfodor (ver 02, F9) | SCRAPE | "Make sure to straighten the horizon and crop if needed." |
| Q28 | monstertower (query #1) | SNIPPET-ONLY | "Attaching your rope to a wakeboard tower instead of a low transom eye raises the angle of pull." |

## Fase 4 — Tabla de veredictos

| Regla [A PRUEBA] (texto exacto) | Veredicto | URLs que lo sostienen | Nota |
|---|---|---|---|
| §1 "Cargar este archivo siempre que el sujeto se desplace sobre una superficie de agua: tabla, casco, remo, pie descalzo o esquí." | SIN EVIDENCIA (no aplicable) | — | Regla de enrutamiento interno; no admite evidencia de campo. Recomiendo etiqueta propia `[TAXONOMIA]` en vez de `[A PRUEBA]`. |
| §1 "Si el sujeto cruza la superficie hacia adentro o hacia afuera, cargar además `02-agua-ruptura.md`." | SIN EVIDENCIA (no aplicable) | — | Ídem. |
| §2.5 "Toda cuerda de remolque se dibuja tensa y recta desde el mango hasta fuera de cuadro; una cuerda con comba dice que no hay tracción y desmiente la velocidad." | CONFIRMADA EN CAMPO (con matiz) | https://www.buckeyemarine.com/news/wakeboarding-rope-tips (Q11) · https://www.wakeworld.com/forum/showthread.php?t=806153 (Q12, snippet) | Tensión = control es consenso [QUOTED Q11]. Pero el propio foro documenta **slack intencional en spins** (Q12): el "Toda" es excesivo. Reescribir: "por defecto tensa; comba sólo en un beat de spin/handle-pass declarado". Física trivial: un cable sólo transmite fuerza en tensión [DERIVED]. |
| §2.7 "El agua desplazada tiene masa: la pared de agua junto al canto se levanta más alta en el lado de presión y se rompe en el lado libre; no es simétrica." | CONFIRMADA EN CAMPO (por física verificable) | https://arxiv.org/abs/2608.29762 (Q20) · https://www.mdpi.com/2311-5521/8/11/301 (Q21) | Dos papers peer-reviewed: impacto oblicuo ⇒ corona asimétrica y "directional jetting" [QUOTED]. No encontré fuente específica de spray de canto de tabla; la analogía canto-que-corta = impacto oblicuo continuo es inferencia mía [DERIVED]. |
| §3 "Las gotas sobre la lente o la carcasa son la cue de vibración de este medio y se nombran como tal." | CONFIRMADA EN CAMPO (fenómeno) | https://www.tonypalmer.photos/blog/random-tips-for-surf-photography-and-water-housings/ (Q9) · https://www.backscatter.com/reviews/post/Underwater-Split-Photography-Tips-A-View-Of-Two-Worlds ("Water spots on the dome are image killers") · https://dan.org/alert-diver/article/ten-tips-for-stunning-splits/ | Las gotas en el puerto son ubicuas y reales (3 fuentes). Matiz: los fotógrafos las tratan como **defecto** y las eliminan. Como cue deliberada: pocas, fuera del sujeto, nunca sobre el rostro. |
| §4 "Piel y neopreno mojados devuelven speculares duros; un cuerpo mojado sin brillos speculares se lee seco y falso." | CONFIRMADA EN CAMPO | https://www.mdavid.com.au/photography/specularhighlights.shtml (Q10) · diyphotography (snippet: "that metallic skin sheen… helps to sculpt and shape the body through highlight") | Óptica verificable: superficie mojada ⇒ specular duro de borde definido [QUOTED Q10]. Segunda fuente sólo snippet (cuerpo no cargó). |
| §4 "Con sol alto el agua pierde textura y el spray se quema: preferir sol bajo, y declararlo en el prompt con hora y dirección, no con 'golden hour' suelto." | CONFIRMADA EN CAMPO | https://alliancewake.com/wake/wake-photography-101-2/ (Q1–Q3) · https://getgdome.com/blogs/gdome-blog/surf-photography-tips (Q8) · https://www.louloubphoto.com/journal/camera-settings-surf-photography (Q4–Q6) · https://www.uwphotographyguide.com/5-tips-for-surf-photography/ (Q7) | 4 fuentes de fotógrafos de wake/surf. Q6 sostiene que la **dirección** cambia el resultado (sol detrás = azules; contraluz = spray que brilla, Q5). "Pierde textura" no aparece textual; las fuentes dicen "flat" y "harsh shadows" [DERIVED]. |
| §8 "El agua congelada parece vidrio o gel: falta textura direccional y blur parcial en el spray; añadir chop, gotas con rim y blur diferencial." | CONFIRMADA EN CAMPO (fallo) / parcial (corrección) | https://promptatlas.co/prompts/splash-photography-prompt (Q13, Q15) · https://gadrex.com/ai-water-and-fluid-generation-prompts/ (Q16, Q17) · https://arxiv.org/abs/2607.25321 (Q18) · https://www.banana-prompts.net/splash-photography-prompt-for-beverage-can/ (Q24) | El fallo "frozen solid-looking fluid" está en el negativo estándar de campo [QUOTED Q13]; el fallo inverso ("blue smoke", gas opaco) también existe [QUOTED Q16]. De la corrección propuesta, el campo sostiene **rim/contraluz** (Q15) y **refracción** (Q17, Q24); **"blur diferencial"** no aparece en ninguna fuente [ABSENT: retraída como evidencia de campo, queda como criterio propio]. |
| §8 "Horizonte inclinado sin querer: el modelo interpreta el movimiento como dutch; pedir horizonte nivelado salvo en el beat de caída." | SIN EVIDENCIA | (análogo real) https://www.divephotoguide.com/underwater-photography-special-features/article/freediving-tips-for-shooting-photos-videos/ (Q26) · https://www.balazsfodor.com/ocean-blog/how-to-shoot-split-shots (Q27) | Horizonte torcido es artefacto real de cámara en agua (2 fuentes) y aparece como artefacto genérico de IA sólo en snippets no verificables (query #11). **La causa atribuida ("interpreta el movimiento como dutch") no tiene ninguna fuente.** Mantener como hipótesis. |
| §8 "Cuerda floja o que termina en el aire: nombrar el destino de la cuerda fuera de cuadro y su tensión." | SIN EVIDENCIA | — | Query #15 sin resultados pertinentes. Sólo el ítem genérico "floating objects that hang in mid-air" en snippets de guías de artefactos. |
| §9 "Cuerpo con vector de maniobra, cuerda tensa si existe." | CONFIRMADA EN CAMPO (con el mismo matiz que §2.5) | ver §2.5 | Duplicado de §2.5. |

Resumen: 6 CONFIRMADAS EN CAMPO (2 con matiz, 1 parcial en la corrección) · 0 REFUTADAS · 5 SIN EVIDENCIA (2 de ellas no aplicables por ser enrutamiento).

## Fase 4b — Hallazgos nuevos (reglas candidatas)

1. **Siempre** nombrar qué objeto o textura se ve deformado a través del agua (refracción, transparencia, reflejos); un agua que no distorsiona lo que hay detrás se lee como humo azul u opaco. `[CAMPO: https://gadrex.com/ai-water-and-fluid-generation-prompts/]` (Q16, Q17; reforzado por Q24).
2. **Siempre** incluir en el negativo de cualquier cuadro de spray: "frozen solid-looking fluid, random droplets, impossible gravity, broken refraction". `[CAMPO: https://promptatlas.co/prompts/splash-photography-prompt]` (Q13).
3. **Nunca** pedir spray sin un punto de impacto y un instante únicos; la salpicadura debe leerse como evento, no como decoración líquida. `[CAMPO: https://promptatlas.co/prompts/splash-photography-prompt]` (Q14). Confirma de campo la U9 ya existente.
4. **Nunca** confiar el spray a un modelo de video: los difusores de video rompen columnas en el aire y dispersan salpicaduras sin momento ni gravedad; el spray se fija en el still y el clip lo hereda. `[CAMPO: https://arxiv.org/abs/2607.25321]` (Q18).
5. **Debe** declararse el ángulo del impacto cuando el spray sale de un canto o casco: sólo el impacto vertical produce corona simétrica; el oblicuo produce corona asimétrica con jet direccional. `[CAMPO: https://arxiv.org/abs/2608.29762]` (Q19–Q21).
6. **Debe** describirse la cuerda con su punto de anclaje: desde torre sube en ángulo, desde el espejo de popa va casi horizontal. `[CAMPO: monstertower, SNIPPET-ONLY, Q28]` — candidata débil hasta leer el cuerpo.
7. **Nunca** usar adjetivos decorativos como sustituto de una instrucción funcional ("beautiful" no hace nada). `[CAMPO: https://pixverse.ai/en/blog/gpt-image-2-review-and-prompt-guide]` (Q23). Coincide con `image/references/gpt-image.md:36`.
8. Afirmación de blog, no verificada: "Nano Banana has an internal database of IOR values" y "describe the physics". `[CAMPO débil: https://theneuralpost.com/2025/12/10/...]` (Q22). No canonizar sin ejercicio propio.

## Fase 5 — Forbidden patterns scan

- Paraphrased fabrication: todas las citas llevan URL + método; las que vienen de WebFetch quedan marcadas. Sin detecciones.
- Authority addition: ninguna autoridad citada sin URL.
- Metadata fabrication: fechas sólo cuando la fuente las dio (alliancewake 2009-11-30; theneuralpost 2025-12-10; gadrex feb 2026; banana-prompts 2026-02-19; arXiv 2607.25321 2026-07-28; arXiv 2608.29762 2026-08-30).
- Claim retraído: "blur diferencial" como corrección de campo → [ABSENT], retraído arriba.

## Fase 6 — Audit checklist

- [x] 5+ queries ejecutadas (15)
- [x] 7+ fetch attempts (27)
- [x] 4+ fetches exitosos con quotes (20 con contenido; 13 aportaron citas)
- [x] 4+ fuentes profesionales (arXiv ×3, MDPI, alliancewake, mdavid, arXiv 2608)
- [x] 2+ queries anti-patrón (6)
- [x] Cada veredicto referencia Q#
- [x] Etiquetas [QUOTED]/[DERIVED]/[ABSENT] en las notas
- [x] Ninguna paráfrasis presentada como cita (las WEBFETCH están marcadas)
- [x] Ninguna autoridad sin URL
- [x] Forbidden patterns scan ejecutado · 1 retracción
- [x] Sección "Limitaciones" presente

## Limitaciones

- **Reddit inaccesible** por WebFetch y por Firecrawl ("we do not support this site"). r/StableDiffusion, r/midjourney, r/Bard no pudieron leerse; sólo snippets de títulos.
- wakeworld (hilo "Low Rope Tension") agotó el tiempo dos veces: la cita Q12 es snippet.
- No se encontró ninguna fuente que hable específicamente de cuerdas de remolque en imágenes generadas ni de horizontes inclinados como fallo de agua en IA.
- Ningún tutorial de YouTube específico de wakeboarding/prompting pudo leerse en esta familia (los dos YouTube leídos están en la familia 02).

## Sugerencia próximo paso

Ejercicio real con Nano Banana Pro: rider de wake, sol a 15° detrás-izquierda, negativo de la candidata 2, cuerda declarada desde torre. Comparar con la misma génesis sin refracción declarada para medir la candidata 1.
