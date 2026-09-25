# RESEARCH DE CAMPO — Familia 02 · Ruptura de superficie

Archivo auditado: `.claude/rules/regimenes/02-agua-ruptura.md` (BORRADOR 2026-09-25).
Fecha de acceso de todas las URLs: **2026-09-25**. Protocolo: skill `research` v2 (6 fases).
Este archivo NO modifica la familia; sólo propone veredictos y reglas candidatas.

Métodos: `[SCRAPE]` texto crudo Firecrawl (grep-able) · `[WEBFETCH]` cita extraída por WebFetch con instrucción verbatim · `[SNIPPET-ONLY]` sólo resumen del buscador.

## Fase 1 — Pre-flight

```
TEMA DE RESEARCH: evidencia de campo para las 13 reglas [A PRUEBA] de la familia 02
  (clavado, corona, refracción en la línea de agua, split-level, gotas/burbujas).
PROPÓSITO DOWNSTREAM: canonizar o refutar cada regla en 02-agua-ruptura.md; reglas candidatas.
MÍNIMOS: 5+ queries · 7+ fetches · 4+ exitosos · 4+ profesionales · 2+ anti-patrón.
RESULTADO: 13 queries · 22 intentos de fetch · 19 con contenido · 9 fuentes profesionales · 5 anti-patrón.
```

## Fase 2 — Bitácora cuantitativa

### 2a. Queries

| # | Herramienta | Query | Ángulo | Resultado |
|---|---|---|---|---|
| 1 | firecrawl_search | competitive diving rip entry splash physics why no splash hands flat | C física | 8 (Vox YouTube, whdh, fromthelabbench, theconversation, ResearchGate) |
| 2 | firecrawl_search → 429 ×2 → WebSearch | split level over under underwater photography dome port tips waterline exposure difference | A best practices | backscatter, uwphotographyguide, ikelite, divephotoguide, dan.org |
| 3 | WebSearch | high speed splash photography crown Worthington jet physics drop impact | C física | Cambridge JFM, AIP, arXiv 0806.3050, fyfd |
| 4 | WebSearch | AI image generation water physics fails splash wrong direction tilted horizon common problems | B anti-patrón | arXiv 2405.15406, 2607.25321 |
| 5 | WebSearch | midjourney "split shot" OR "half underwater" prompt two waterlines fail tips | B anti-patrón | sólo fotografía real; **nada específico de IA** |
| 6 | WebSearch | "diving" OR "diver" photography entry splash frozen shutter speed underwater camera pool bottom tips | A | uwphotographyguide shutter, ikelite (genérico) |
| 7 | WebSearch | nano banana prompt water level waterline glass fill liquid respects level trick | E casos/modelo | guías Nano Banana Pro (higgsfield, fal, dev.to); nada específico |
| 8 | WebSearch | reddit AI generated splash "looks like" glass OR frozen OR gel OR jelly water … | B anti-patrón | **Sin resultados pertinentes** |
| 9 | WebSearch | AI generated image water horizon tilted OR crooked … "two horizons" OR "double horizon" | B anti-patrón | genéricos (cliprise, zsky) |
| 10 | WebSearch | split shot underwater half appears larger magnification refraction 33 percent why over-under photo distortion waterline | C óptica | ikelite how-to, terragalleria (QT Luong), outex |
| 11 | WebSearch | oblique drop impact asymmetric splash crown physics angle of impact study | C física | arXiv 1611.05670, 2608.29762, MDPI Fluids, Cambridge CiCP |
| 12 | WebSearch | "half underwater" OR "over-under" OR "split shot" AI image prompt tips waterline midjourney OR "nano banana" OR "gpt image" generated | B/E anti-patrón IA | sólo fotografía real + un prompt genérico de Midjourney (snippet) |
| 13 | firecrawl_search (developer) | water splash generation looks like glass frozen gel prompt issue stable diffusion | B anti-patrón | rapidata "full wine glass" (nivel de líquido) |

Anti-patrón explícitas: #4, #5, #8, #9, #12, #13 (6).

### 2b. Fetches

| # | URL | Método | Resultado |
|---|---|---|---|
| F1 | http://www.fromthelabbench.com/from-the-lab-bench-science-blog/olympic-diving-physics | SCRAPE | ✅ (2012-08-07, autora ex-clavadista) |
| F2 | https://theconversation.com/not-making-a-splash-the-anatomy-of-a-perfect-olympic-dive-8082 | WEBFETCH | ✅ |
| F3 | https://whdh.com/news/team-usa-divers-detail-splash-minimizing-rip-entry-technique/ | WEBFETCH | ✅ (2016-08-03) |
| F4 | https://www.youtube.com/watch?v=8GqWTqDhahM (Vox, "How Olympic divers make the perfect tiny splash") | SCRAPE (descripción + transcripción) | ✅ (2021-08-05) |
| F5 | https://fyfluiddynamics.com/tagged/worthington-jet/ | WEBFETCH | ❌ 403 |
| F6 | https://www.divephotoguide.com/underwater-photography-techniques/article/over-unders/ | WEBFETCH | ❌ 503 ×2 |
| F7 | https://www.ikelite.com/blogs/cheat-sheets/split-shots-half-in-half-out | WEBFETCH | ✅ (1 cita útil) |
| F8 | https://www.backscatter.com/reviews/post/Underwater-Split-Photography-Tips-A-View-Of-Two-Worlds | SCRAPE | 429 en 1er intento; ✅ 2º |
| F9 | https://dan.org/alert-diver/article/ten-tips-for-stunning-splits/ | SCRAPE | ✅ (Alert Diver Q2 2018, Renee Capozzola) |
| F10 | https://www.balazsfodor.com/ocean-blog/how-to-shoot-split-shots | SCRAPE | ✅ (2026-01-28) |
| F11 | https://www.uwphotographyguide.com/book/underwater-photography-guide/underwater-photography-composition/over-under-split-photography/ | WEBFETCH | ✅ |
| F12 | https://arxiv.org/abs/0806.3050 | WEBFETCH | ✅ abstract (Deegan, Brunet, Eggers) |
| F13 | https://www.youtube.com/watch?v=BV5Jzq-DUBI (Ikelite, "Tips for Shooting Split Shots") | SCRAPE (descripción + capítulos + transcripción) | ✅ (2024-04-19) |
| F14 | https://www.terragalleria.com/blog/under-over-water-split-shots-challenges-and-solutions/ | SCRAPE | ✅ (QT Luong, 2024-08-07) |
| F15 | https://arxiv.org/abs/2608.29762 | WEBFETCH | ✅ abstract |
| F16 | https://www.mdpi.com/2311-5521/8/11/301 | SCRAPE | ✅ (120 KB, extraído con script; Fluids 2023/11, DOI 10.3390/fluids8110301) |
| F17 | https://www.ikelite.com/blogs/advanced-techniques/how-to-shoot-split-shots-half-in-half-out-of-the-water | WEBFETCH | ✅ |
| F18 | https://www.uwcamerastore.com/blog/tips-for-shooting-split-shots | WEBFETCH | ✅ sin contenido pertinente |
| F19 | https://www.rapidata.ai/blog/wine-glasses | SCRAPE | ✅ (2025-07-09) |
| F20 | https://www.banana-prompts.net/splash-photography-prompt-for-beverage-can/ | WEBFETCH | ✅ |
| F21 | https://www.divephotoguide.com/underwater-photography-special-features/article/freediving-tips-for-shooting-photos-videos/ | SCRAPE | ✅ (Alex Lindbloom, 2020-09-05) |
| F22 | https://www.uwphotographyguide.com/underwater-photography-lighting-fundamentals | SCRAPE | ✅ (Scott Gietler, 2009-02-27, mod. 2025-08-15) |

Fuentes profesionales: F12, F15, F16 (peer-reviewed), F2 (académicos vía The Conversation), F9 (DAN, organización de seguridad de buceo), F8/F13/F17 (documentación técnica de fabricantes de carcasas con autor), F22 (guía de referencia con autor y fecha), F14 (fotógrafo profesional publicado, texto técnico). Blogs de prompts (F20) = fuente de campo.

## Fase 3 — Citas verbatim

| Q# | URL | Método | Cita verbatim |
|---|---|---|---|
| Q1 | F4 Vox | SCRAPE | "As water is getting displaced, it has to move somewhere. It gets pushed down and out, creating a radial jet that shoots up at 20 - 30 times the speed of the impact." |
| Q2 | F4 Vox | SCRAPE | "The second part of the splash is caused by the air that divers bring in with them." |
| Q3 | F4 Vox | SCRAPE | "There's so much pressure and energy that that water ejects straight back up toward the surface, resulting in a worthington jet - the second pop of the big splash we see here" |
| Q4 | F4 Vox | SCRAPE | "The flat hands create a cavity that's juuuust wide enough for his body to pass through." |
| Q5 | F4 Vox | SCRAPE | "You'll see two white bubbles out to the side of the hole that the athlete went in . Those are the swim bubbles." |
| Q6 | F4 Vox | SCRAPE | "If performed correctly, the bubbles will be so small, that it looks almost like the water is boiling at the surface" |
| Q7 | F2 theconversation | WEBFETCH | "Impact with the water creates a vacuum between the hands, arms and head which, as the diver enters vertically, pulls any splash down and under the water with the diver until they are deep enough (1-2m) to have minimal effect on the surface of the water." |
| Q8 | F2 theconversation | WEBFETCH | "To achieve a rip entry, the diver's arms must be extended forwards in line with the ears, the elbows must be locked and the stomach and back of the diver must be tight." |
| Q9 | F1 fromthelabbench | SCRAPE | "Once under the water's surface, all that water that you have pulled down with you almost 'bubbles' back up to the surface under you" |
| Q10 | F3 whdh | WEBFETCH | "that air shoots back up, and it moves water out of its way when it's coming up" |
| Q11 | F22 uwphotographyguide | SCRAPE | "Objects will also appear to be up to 33% larger than they are. This is due to the fact that the **index of refraction** of water is greater than air. This happens behind flat surfaces, such as your mask, a compact camera underwater housing, or a macro port. It does not happen when using a dome port." |
| Q12 | F14 terragalleria | SCRAPE | "Therefore, what the camera captures underwater is a virtual diffracted image. That is why objects appear closer underwater than above water." |
| Q13 | F9 dan.org | SCRAPE | "Water interface and the virtual image force the focus above and below to be different, so know your camera and housing well enough to quickly adjust the position of the AF zone." |
| Q14 | F9 dan.org | SCRAPE | "Keep in mind that the smaller the port, the less surface area you can cover, which means you will need calmer water to obtain a thinner meniscus (the curve of water against the dome port)." |
| Q15 | F8 backscatter | SCRAPE | "Even in flat sea conditions small ripples in the water can look like tsunamis through your lens. Large dome ports push these ripples further from your lens and help smooth out the waterline in your image." |
| Q16 | F13 Ikelite YouTube | SCRAPE | "You've got a bright sun in the top of your frame and dark water below. There's going to be a range that's too wide for a lot of cameras to capture." |
| Q17 | F13 Ikelite YouTube | SCRAPE | "The solution that most photographers use to fix this is to use two strobes that are submerged to light the lower to the equivalent of the amount of light that you're reading from the sun." |
| Q18 | F14 terragalleria | SCRAPE | "Although to handle the difference some photographers use a 4-stop GND, I found that the dynamic range of digital cameras makes a 2-stop GND generally sufficient at midday." |
| Q19 | F9 dan.org | SCRAPE | "Even with the sun high in the sky, the underwater portion of your image will be darker than the above-water portion" |
| Q20 | F10 balazsfodor | SCRAPE | "expose for the highlights above water" / "Blown skies are gone forever - shadows underwater usually aren't." |
| Q21 | F11 uwphotographyguide over-under | WEBFETCH | "Try to shoot with the sun behind you to minimize the exposure difference between the over and under sections." |
| Q22 | F14 terragalleria | SCRAPE | "I remedied this situation by building a custom floater with a buoyancy calibrated by removing material from two swimming kickboards to place the waterline right at the middle of the dome port." |
| Q23 | F21 divephotoguide | SCRAPE | "a wet lens is not the most ideal when it comes to split shots, as the water between the port and the wet lens gives you a sort of second waterline when it drains out as you lift the camera out of the water." |
| Q24 | F15 arXiv 2608.29762 | WEBFETCH | "Oblique drop impact onto a deep liquid pool produces asymmetric crowns, directional jetting, and splashing transitions that cannot be characterized by the total impact inertia alone." |
| Q25 | F16 MDPI | SCRAPE | "This study investigates the asymmetric crown morphology resulting from an oblique impact (α= 60°) of a single droplet on a horizontal and quiescent wall film of the same liquid." |
| Q26 | F12 arXiv 0806.3050 | WEBFETCH | "In the crown splash parameter regime, the splash pattern is highly regular." |
| Q27 | arXiv 2405.15406 (ver 01) | SCRAPE | "The splash is symmetric, and the physics behind this phenomenon involve the surface tension of the water and the forces exerted upon the initial impact, likely from a droplet falling into the water." |
| Q28 | F20 banana-prompts | WEBFETCH | "A violent, symmetrical crown splash." / "A symmetrical, circular eruption common in milk or water photography." |
| Q29 | F13 Ikelite YouTube | SCRAPE | "But be sure you're going to have to fix water droplets in Lightroom or Photoshop after the capture. It's just part of shooting over-unders." |
| Q30 | F13 Ikelite YouTube | SCRAPE | "If you can get into two, three, four feet of water with a bright overhead sun and hopefully maybe some sand or some bright corals to reflect that light back up. You're going to have a relatively uniform exposure from the top to the bottom." |
| Q31 | F19 rapidata | SCRAPE | "A popular prompt that confuses text-to-image models is "completely full wine glass" [4]. Most of the images of wine glasses on the internet are not completely full, making it hard for models to generate the unexpected image." |
| Q32 | F17 ikelite how-to | WEBFETCH | "Position the sun at you back to minimize the range of tones your lens sees." |

## Fase 4 — Tabla de veredictos

| Regla [A PRUEBA] (texto exacto) | Veredicto | URLs que lo sostienen | Nota |
|---|---|---|---|
| §1 "Cargar cuando el beat es el cruce de la superficie en cualquier sentido: entrada de clavado, salida de un nadador, salto de un animal marino, objeto que cae al agua." | SIN EVIDENCIA (no aplicable) | — | Enrutamiento interno; sugerir `[TAXONOMIA]`. |
| §1 "No cargar para un sujeto totalmente sumergido; eso es `03-subacuatico.md`. Para un sujeto que se desplaza encima sin cruzar, `01-agua-superficie.md`." | SIN EVIDENCIA (no aplicable) | — | Ídem. |
| §2.2 "La forma de la salpicadura depende de la entrada y hay que declararla: un cuerpo alineado y vertical produce entrada limpia con corona baja y un chorro fino; un cuerpo abierto produce corona ancha y agua blanca." | CONFIRMADA EN CAMPO (con precisión) | https://www.youtube.com/watch?v=8GqWTqDhahM (Q1–Q4) · https://theconversation.com/not-making-a-splash-the-anatomy-of-a-perfect-olympic-dive-8082 (Q7, Q8) · https://whdh.com/... (Q10) · fromthelabbench (Q9) | 4 fuentes [QUOTED]. Precisión importante: el "chorro fino" vertical es el **Worthington jet**, que es el **segundo** splash y aparece **después**; la entrada limpia lo suprime (Q3, Q4). Reescribir: "entrada limpia = lámina radial baja y sin chorro central; entrada abierta = corona ancha + chorro vertical posterior". |
| §2.3 "La parte sumergida se ve desplazada y ligeramente comprimida respecto a la parte emergida por la refracción; una extremidad que cruza la línea del agua sin quiebre óptico se lee como recorte." | CONFIRMADA EN CAMPO (quiebre) · **REFUTADA en el detalle "comprimida"** | https://www.uwphotographyguide.com/underwater-photography-lighting-fundamentals (Q11) · https://www.terragalleria.com/blog/under-over-water-split-shots-challenges-and-solutions/ (Q12) · https://dan.org/alert-diver/article/ten-tips-for-stunning-splits/ (Q13) · snippet ikelite how-to: "approximately one quarter closer and one third larger… visual discontinuity at the waterline" | La discontinuidad óptica existe [QUOTED Q11–Q13]. Pero la parte sumergida se ve **~33 % más grande y ~25 % más cerca**, no comprimida (Q11). Además, con domo la magnificación se cancela en gran parte (Q11: "It does not happen when using a dome port"); persiste el desplazamiento/foco distinto. Corregir la redacción. |
| §2.4 "Arriba de la línea hay gotas; abajo hay burbujas. No se mezclan: las gotas caen, las burbujas suben." | CONFIRMADA EN CAMPO | Vox (Q2, Q5, Q6) · fromthelabbench (Q9) · whdh (Q10) · theconversation (Q7) | Cavidad de aire bajo la superficie, burbujas que suben [QUOTED]. Matiz temporal: unas décimas después las burbujas rompen la superficie y "hierven" (Q6); la regla vale para el instante congelado de la entrada. |
| §2.7 "La línea de superficie es una sola: si el encuadre es split-level, hay exactamente un menisco que cruza el cuadro, con el aire nítido arriba y el agua con su propia atmósfera abajo." | CONFIRMADA EN CAMPO | dan.org (Q14) · backscatter (Q15) · terragalleria (Q22) · divephotoguide (Q23, contraejemplo real) | Matiz: el menisco real es una **banda** con grosor, no una línea de pelo; su grosor depende del domo y del oleaje (Q14, Q15). Describir "a single thin meniscus band". Q23 documenta un caso real de **segunda línea de agua** (lente húmeda) = el fallo que la regla prohíbe. |
| §4 "En split-level la mitad de aire y la mitad de agua tienen exposiciones distintas: el agua uno o dos pasos más oscura, con cáusticas si hay sol; declararlo evita que el modelo unifique las dos mitades." | CONFIRMADA EN CAMPO | Ikelite YouTube (Q16, Q17) · terragalleria (Q18) · dan.org (Q19) · balazsfodor (Q20) · uwphotographyguide (Q21) | El valor "uno o dos pasos" queda respaldado exactamente por Q18 (GND de 2 pasos suficiente al mediodía; algunos usan 4). Cáusticas: ver familia 03 (requieren sol directo). |
| §5 "Rig por defecto: carcasa a nivel exacto de la superficie, o cámara de borde de piscina baja; para el split-level, carcasa con domo semisumergido." | CONFIRMADA EN CAMPO | backscatter (Q15, domo ≥ 8") · dan.org (Q14, 9") · Ikelite YouTube ("Eight-inch domes are preferable") · terragalleria (Q22) | 4 fuentes coinciden en domo grande con la línea de agua al centro [QUOTED]. "Cámara de borde de piscina" sin fuente específica, pero no contradicha. |
| §8 "Dos superficies de agua o un horizonte de agua duplicado: el prompt mezcló vista de superficie y vista sumergida; declarar una sola línea de agua y desde qué lado mira la cámara." | SIN EVIDENCIA (como fallo de IA) | análogo real: divephotoguide (Q23) | Queries #5, #9, #12 no encontraron reportes de este fallo en generadores. Sí existe el análogo físico (Q23). Nota adicional: desde abajo, la superficie **refleja** al sujeto (morphic, ver 03: "their own reflection visible on the underside of the surface… so the portrait appears twice"), un duplicado legítimo que un crítico no debe confundir con el fallo. |
| §8 "El cuerpo aparece entero y nítido bajo el agua sin quiebre de refracción: pedir explícitamente el desplazamiento óptico en la línea del agua." | CONFIRMADA EN CAMPO (física) · SIN EVIDENCIA (frecuencia del fallo en IA) | Q11–Q13 | Misma base que §2.3. No hay reportes de foros sobre este fallo específico. |
| §8 "Salpicadura sin dirección, simétrica como fuente: nombrar el ángulo de entrada y el lado de presión." | CONFIRMADA EN CAMPO (con precisión) | arXiv 2608.29762 (Q24) · MDPI (Q25) · arXiv 2405.15406 (Q27) · banana-prompts (Q28) | La simetría es **correcta** para impacto vertical (Q26, Q27) y es lo que las guías de prompts piden para bebidas (Q28); el fallo es la simetría cuando la entrada es **oblicua** (Q24, Q25). La corrección "nombrar el ángulo" es exactamente lo que distingue ambos casos. |
| §9 "Una sola línea de superficie; refracción presente en lo sumergido." | CONFIRMADA EN CAMPO (con la corrección de §2.3) | Q11–Q15 | Duplicado. |
| §9 "Gotas arriba, burbujas abajo, nunca invertidas." | CONFIRMADA EN CAMPO | Q2, Q5–Q10 | Duplicado de §2.4. |

Resumen: 9 CONFIRMADAS EN CAMPO (3 con precisión/corrección de redacción; 1 de ellas con un detalle REFUTADO: "comprimida") · 0 REFUTADAS íntegras · 4 SIN EVIDENCIA (2 no aplicables).

## Fase 4b — Hallazgos nuevos (reglas candidatas)

1. **Nunca** dibujar un chorro vertical central al boardear una entrada limpia: el Worthington jet es la firma de la entrada fallida y llega después de la cavidad; la entrada limpia muestra sólo una lámina radial baja. `[CAMPO: https://www.youtube.com/watch?v=8GqWTqDhahM]` (Q1–Q4).
2. **Debe** aparecer, en el cuadro posterior a una entrada limpia, el par de "swim bubbles" a los lados del agujero de entrada, no una nube única bajo el cuerpo. `[CAMPO: https://www.youtube.com/watch?v=8GqWTqDhahM]` (Q5).
3. **Siempre** que el split-level sea a contraluz (atardecer), declarar un práctico sumergido (dos strobes bajo el agua); sin él la mitad inferior es negra y el modelo la inventará. `[CAMPO: https://www.youtube.com/watch?v=BV5Jzq-DUBI]` (Q16, Q17).
4. **Debe** describirse el menisco como banda fina con grosor, nunca como línea de pelo; su grosor crece con oleaje y domo pequeño. `[CAMPO: https://dan.org/alert-diver/article/ten-tips-for-stunning-splits/ · https://www.backscatter.com/reviews/post/Underwater-Split-Photography-Tips-A-View-Of-Two-Worlds]` (Q14, Q15).
5. **Debe** declararse un fondo claro (arena, azulejo) y poca profundidad para justificar una mitad sumergida bien expuesta con luz natural; de lo contrario el agua va 1–2 pasos más oscura. `[CAMPO: https://www.youtube.com/watch?v=BV5Jzq-DUBI · https://www.terragalleria.com/...]` (Q18, Q30).
6. Las gotas sobre el domo por encima de la línea de agua son inevitables en fotografía real de split-level; una o dos gotas fuera del sujeto son cue de realismo, un rastro sobre el rostro es defecto. `[CAMPO: https://www.youtube.com/watch?v=BV5Jzq-DUBI]` (Q29).
7. **Nunca** confiar en que el modelo respete un nivel de líquido atípico: los generadores regresan al nivel "habitual" del dataset (caso "completely full wine glass"); declarar el nivel con referencia geométrica (a media altura del cuadro, a la altura de los hombros). `[CAMPO: https://www.rapidata.ai/blog/wine-glasses]` (Q31).
8. Posición del sol por defecto en split-level: a la espalda de la cámara, para minimizar el rango tonal. `[CAMPO: https://www.ikelite.com/blogs/advanced-techniques/how-to-shoot-split-shots-half-in-half-out-of-the-water · uwphotographyguide]` (Q21, Q32).

## Fase 5 — Forbidden patterns scan

- Sin autoridades sin URL. Sin metadatos inventados (fechas: Vox 2021-08-05; Ikelite 2024-04-19; DAN Q2 2018; terragalleria 2024-08-07; balazsfodor 2026-01-28; rapidata 2025-07-09; MDPI 2023/11; arXiv 2608.29762 2026-08-30; whdh 2016-08-03; fromthelabbench 2012-08-07).
- La cita del snippet "one quarter closer and one third larger" se etiqueta como snippet; la fuente crudo Q11 sostiene el mismo dato (33 %).
- Sin detecciones.

## Fase 6 — Audit checklist

- [x] 5+ queries (13)
- [x] 7+ fetch attempts (22)
- [x] 4+ fetches exitosos con quotes (19 con contenido; 16 con citas)
- [x] 4+ fuentes profesionales (9)
- [x] 2+ anti-patrón (6)
- [x] Cada veredicto con Q#
- [x] Etiquetas epistémicas en notas
- [x] Sin paráfrasis como cita
- [x] Sin autoridad sin URL
- [x] Forbidden scan ejecutado · sin detecciones
- [x] Limitaciones presentes

## Limitaciones

- Ningún foro de IA (Reddit, Discord) fue accesible; no encontré reportes de usuarios sobre split-level generado ni sobre "dos líneas de agua" en generadores. Los veredictos SIN EVIDENCIA de esta familia son específicamente sobre la **frecuencia del fallo en IA**, no sobre la física.
- divephotoguide "In-Depth Guide to Over-Unders" devolvió 503 dos veces; fyfd 403.
- La evidencia de asimetría de corona viene de gotas sobre líquido (papers), no de cuerpos humanos entrando al agua; la extrapolación es mía [DERIVED].

## Sugerencia próximo paso

Ejercicio real: dos génesis en NBP del mismo clavado, una con "vertical rip entry, low radial sheet, no central jet" y otra con "open-body entry, wide crown, delayed vertical Worthington jet"; medir si el modelo distingue ambos estados. Segunda prueba: split-level con "single thin meniscus band, underwater half two stops darker, sun behind camera".
