# Investigación de campo — Familia 09: Grupo ensamble

Archivo bajo prueba: `.claude/rules/regimenes/09-grupo-ensamble.md` (BORRADOR 2026-09-25).
Fecha de acceso de todas las URLs: **2026-09-25**. Protocolo: skill `research` v2, seis fases.
Herramientas: WebSearch, Firecrawl (search/scrape, incluida transcripción de YouTube), WebFetch,
curl + extracción de texto, pullpush.io para Reddit. Ninguna herramienta de generación fue usada.

Criterio de veredicto: **CONFIRMADA EN CAMPO** = dos fuentes independientes con ejemplo concreto o
física verificable; **REFUTADA** = una fuente sólida la contradice con evidencia; **SIN EVIDENCIA** =
nada concluyente.

## Fase 1 — Pre-flight

```
TEMA: evidencia de campo para las 6 líneas [A PRUEBA] de la familia 09 y, en especial, la pregunta
      central: ¿GPT Image 2 con hasta 16 referencias con rol sostiene 5 o más identidades en una
      sola pasada? ¿Cuántas identidades sostienen de verdad NBP y NB2 según campo?
PROPÓSITO DOWNSTREAM: decidir qué líneas pasan a [CAMPO: url] o [REFUTADA: url] y fijar la
      estrategia de inserción (secuencial vs una pasada) antes del ejercicio.
MÍNIMOS: 5+ queries · 7+ fetch attempts · 4+ exitosos · 4+ fuentes profesionales · 2+ anti-patrón.
```

## (1) Bitácora cuantitativa

### Queries (17 ejecutadas, 4 anti-patrón)

| # | Herramienta | Query | Resultado |
|---|---|---|---|
| 1 | WebSearch | "gpt-image-2" reference images how many input images multiple people consistency | ✅ replicate, Luma, apiyi, rewarx, chatgptimages.app |
| 2 | WebSearch | nano banana pro group photo multiple people references reddit "5 people" | ❌ resultados irrelevantes (grupos de Steam) |
| 3 | WebSearch | nano banana 2 reference images limit characters "up to" | ✅ Runware docs, glbgpt, Curious Refuge, Flowith |
| 4 | WebSearch | group portrait photography eyelines everyone looking same direction | ✅ Digital Photography School (18 tips) |
| 5 | WebSearch | violin held on left shoulder bow in right hand left-handed violinist | ✅ Normans, violinist.com, Wikipedia |
| 6 | WebSearch **(anti-patrón)** | AI image multiple characters faces blend into each other same face group photo fix | ⚠ herramientas de face-swap; Adobe community; PhotoMaker |
| 7 | WebSearch | dance group photography timing jump peak moment | ✅ Skylum, School of Photography, Pete Xavier |
| 8 | WebSearch | top-down overhead choreography formation drone dance identity faces | ✅ sschoreography.com, UNCSA |
| 9 | WebSearch | youtube nano banana pro multiple characters group scene consistency | ✅ ud.hk, YouTube Lenny Blonde aiKGYFx3VPg |
| 10 | WebSearch **(anti-patrón)** | ChatGPT Images 2.0 group photo multiple people test faces consistent | ✅ queststudio, mindstudio, OpenAI, apiyi |
| 11 | WebSearch | nano banana pro test 5 characters consistency group scene review | ✅ Curious Refuge "11 tests", selfielab |
| 12 | WebSearch | gpt-image-2 openai announcement "input images" limit editing | ✅ OpenAI API reference (edit), Wikipedia GPT Image |
| 13 | WebSearch | reddit "How to generate 6 characters in a single image while keeping consistency" | ⚠ solo arXiv CharCom; sin Reddit |
| 14 | Firecrawl search **(anti-patrón)** | site:reddit.com nano banana pro group photo faces reference consistency | ✅ r/Bard 1mvhhh1, r/aiArt 1tgajli, r/Bard 1pb4nvc, r/StableDiffusion 1wetnrt |
| 15 | WebSearch | site:youtube.com nano banana pro group photo "5 people" | ✅ blog.google, Digital Camera World, datastudios |
| 16 | WebSearch | site:youtube.com GPT Image 2 multiple characters group scene consistency test | ✅ Bijan Bowen DXlM8J8EZOA, ReviewAIVideos ob5LSLWEzgI, d7EOD-rdDNw |
| 17 | WebSearch **(anti-patrón)** | "Images 2.0" OR "gpt-image-2" test "group photo" reference faces recognizable | ✅ everypixel, image2.im, fal.ai |

### Fetches (31 intentos, 24 exitosos)

| # | URL | Método | Resultado |
|---|---|---|---|
| F1 | https://ai.google.dev/gemini-api/docs/image-generation | curl | ✅ (doc oficial; tabla de límites por modelo) |
| F2 | https://blog.google/innovation-and-ai/products/nano-banana-pro/ | curl | ✅ (anuncio oficial NBP) |
| F3 | https://developers.openai.com/api/reference/python/resources/images/methods/edit | curl | ✅ (referencia oficial API) |
| F4 | https://developers.openai.com/api/docs/models/gpt-image-2 | curl | ✅ sin cifra de referencias en el texto extraído |
| F5 | https://developers.openai.com/api/docs/guides/image-generation | WebFetch (redirect) → curl | ✅ |
| F6 | https://openai.com/index/new-chatgpt-images-is-here/ | curl + WebFetch | ❌ 403 / texto vacío |
| F7 | https://replicate.com/openai/gpt-image-2 | curl | ✅ |
| F8 | https://lumalabs.ai/learning-center/articles/gpt-image-2-complete-guide | WebFetch | ✅ `[WEBFETCH]` ("Up to 4 input images", 2026-06-03) |
| F9 | https://help.apiyi.com/en/gpt-image-multi-image-generation-consistency-guide-en.html | curl | ✅ (2026-06-13) |
| F10 | https://www.glbgpt.com/hub/nano-banana-2-subject-consistency/ | curl | ✅ (contenido SEO; 2026-02-27) |
| F11 | https://www.atlascloud.ai/blog/guides/nanobanana-14-reference-images-consistency | curl | ❌ texto vacío (JS) |
| F12 | https://runware.ai/docs/models/google-nano-banana-2/guides/character-consistency | curl | ✅ |
| F13 | https://www.rewarx.com/blogs/gpt-image-2-face-consistency-ecommerce | curl | ✅ (SEO, sin datos) |
| F14 | https://research.everypixel.com/gpt-image-2-0/ | curl | ✅ |
| F15 | https://curiousrefuge.com/blog/11-nano-banana-2-tests | curl | ✅ |
| F16 | https://queststudio.io/blog/chatgpt-group-photo-prompts | curl | ✅ (2026-08-14) |
| F17 | https://www.mindstudio.ai/blog/chatgpt-images-2-5-review | curl | ✅ (Images 2.5, sept 2026) |
| F18 | https://www.datacamp.com/blog/chatgpt-images-2-5 | curl + WebFetch | ❌ curl vacío; WebFetch sin pasajes de grupo |
| F19 | https://www.ud.hk/en/blogs/insight/article/2026-06-29-nano-banana-consistent-characters | curl | ✅ |
| F20 | https://selfielab.me/blog/nano-banana-2-multi-character-consistency-prompts-20260301 | curl | ✅ (SEO; cifras sin fuente) |
| F21 | https://flowith.io/blog/nano-banana-consistent-characters-storyboard/ | curl | ✅ |
| F22 | https://aimeetsgirlboss.substack.com/p/how-to-get-consistent-character-images | WebFetch | ✅ `[WEBFETCH]` (2026-05-13) |
| F23 | https://aiblewmymind.substack.com/p/nano-banana-2-vs-gpt-images-2 | WebFetch | ✅ `[WEBFETCH]` (solo un sujeto) |
| F24 | https://www.digitalcameraworld.com/tech/artificial-intelligence/nano-banana-has-gone-pro-… | curl | ✅ (2025-11-20) |
| F25 | https://digital-photography-school.com/how-to-take-great-group-photos/ | curl | ✅ |
| F26 | https://www.normans.co.uk/blogs/blog/can-the-violin-be-played-left-handed | curl | ✅ |
| F27 | https://en.wikipedia.org/wiki/Violin_technique | curl | ✅ |
| F28 | https://sschoreography.com/elevating-dance-cinematography-the-impact-of-drone-cameras/ | curl | ✅ |
| F29 | https://skylum.com/blog/dance-photography | curl | ✅ (theschoolofphotography sin pasajes útiles) |
| F30 | YouTube aiKGYFx3VPg (Lenny Blonde, 2025-11-27) · yOki0sHXE_8 (WealthWise, 2025-12-11) · Jmr8EoVux-g (Phylux, 2026-07-25) · ob5LSLWEzgI · DXlM8J8EZOA (Bijan Bowen, 2026-04-21) | Firecrawl scrape | ✅ 5/5 con descripción y transcripción |
| F31 | Reddit r/aiArt 1tgajli · r/Bard 1pb4nvc · r/StableDiffusion 1wetnrt | pullpush.io / curl / WebFetch | ❌ bloqueados o rate limit (solo r/Bard 1mvhhh1 legible, ver 08) |

Fuentes profesionales: Google AI for Developers (doc oficial), Google Keyword blog (anuncio oficial),
OpenAI API reference (doc oficial), Replicate model card, Runware docs, everypixel.com (benchmark),
Digital Photography School (guía técnica), Digital Camera World (prensa especializada). Total: 8.

## (2) Citas verbatim

| Q# | URL | Cita verbatim |
|---|---|---|
| Q1 | https://ai.google.dev/gemini-api/docs/image-generation | "gemini-2.5-flash-image works best with up to 3 images as input, while gemini-3-pro-image supports 5 images with high fidelity, and up to 14 images in total. gemini-3.1-flash-image supports character resemblance of up to 4 characters and the fidelity of up to 10 objects in a single workflow." |
| Q2 | https://ai.google.dev/gemini-api/docs/image-generation | "Up to 4 images of characters to maintain character consistency Up to 5 images of characters to maintain character consistency" (tabla por modelo) |
| Q3 | https://ai.google.dev/gemini-api/docs/image-generation | prompt de ejemplo oficial: "An office group photo of these people, they are making funny faces." |
| Q4 | https://blog.google/innovation-and-ai/products/nano-banana-pro/ | "With Nano Banana Pro, you can blend more elements than ever before, using up to 14 images and maintaining the consistency and resemblance of up to 5 people." |
| Q5 | https://blog.google/innovation-and-ai/products/nano-banana-pro/ | "Put these five people and this dog into a single image, they should fit into a stunning award-winning shot in the style if [sic] a fashion editorial. The identity of all five people and their attire and the dog must stay consistent throughout" |
| Q6 | https://developers.openai.com/api/reference/python/resources/images/methods/edit | "each image should be a png, webp, or jpg file less than 50MB. You can provide up to 16 images." |
| Q7 | https://replicate.com/openai/gpt-image-2 | "Reference multiple images clearly: When working with several input images, label them by number and describe how they relate." |
| Q8 | https://replicate.com/openai/gpt-image-2 | "When you pass reference images, GPT Image 2 processes them at high fidelity automatically. There's no knob to adjust — the model always does its best to preserve the details of the input." |
| Q9 | https://help.apiyi.com/en/gpt-image-multi-image-generation-consistency-guide-en.html | "GPT Image 2 can accept multiple reference images in editing/reference scenarios (official documentation notes up to 16, though you should verify this on the platform)." |
| Q10 | https://lumalabs.ai/learning-center/articles/gpt-image-2-complete-guide | "Up to 4 input images" `[WEBFETCH]` |
| Q11 | https://research.everypixel.com/gpt-image-2-0/ | "Many consistent characters in a batch Consider Nano Banana 2 Not tested by us; fal.ai reports 14 references, 5 people" |
| Q12 | https://research.everypixel.com/gpt-image-2-0/ | "Keep AI generation for portraits and small groups, where anatomy is easy to check." |
| Q13 | https://curiousrefuge.com/blog/11-nano-banana-2-tests | "Nano Banana 2 now supports up to five consistent characters in a single frame. Multi-Character References Nano Banana 2 We successfully placed five reference characters at a restaurant table." |
| Q14 | https://queststudio.io/blog/chatgpt-group-photo-prompts | "Label every person, make one change at a time, and review faces individually before the group image leaves your screen." |
| Q15 | https://queststudio.io/blog/chatgpt-group-photo-prompts | "Review at face level Zoom into every face, every visible hand, uniform number, piece of jewelry, and repeated pattern. A group can look convincing from far away while one person is wrong." |
| Q16 | https://queststudio.io/blog/chatgpt-group-photo-prompts | "Change one region at a time Fix the background before faces, or one person before another. Large instructions invite the model to redraw areas that were already correct." |
| Q17 | https://www.ud.hk/en/blogs/insight/article/2026-06-29-nano-banana-consistent-characters | "A second mistake is describing the face in heavy text detail instead of relying on the reference image. Long facial descriptions fight the reference and produce a blended stranger." |
| Q18 | https://www.ud.hk/en/blogs/insight/article/2026-06-29-nano-banana-consistent-characters | "More images are not automatically better. Feeding in five inconsistent photos, where the lighting and expression differ wildly, can confuse the model rather than help it." |
| Q19 | https://www.glbgpt.com/hub/nano-banana-2-subject-consistency/ | "For character consistency, the model supports up to 5 unique characters within the Gemini App and 4 characters via the Developer API." |
| Q20 | https://runware.ai/docs/models/google-nano-banana-2/guides/character-consistency | "A single request accepts up to 14 reference images, enough to lock a character, a product, or several subjects together." |
| Q21 | https://www.digitalcameraworld.com/tech/artificial-intelligence/nano-banana-has-gone-pro-and-it-can-generate-group-photos-change-camera-angles-and-adjust-lighting-plus-its-already-inside-photoshop | "Nano Banana Pro takes that a step further – it's now capable of generating group photos of up to five people while still "maintaining the consistency and resemblance," Google says." |
| Q22 | https://digital-photography-school.com/how-to-take-great-group-photos/ | "If there are other photographers, just wait until they've all finished their shots, then get the attention of the full group. Otherwise, you'll get everyone looking in different directions." |
| Q23 | https://digital-photography-school.com/how-to-take-great-group-photos/ | "(you can add variation by taking some shots of everyone looking at the camera and other shots of everyone looking at the person/couple)" |
| Q24 | https://www.normans.co.uk/blogs/blog/can-the-violin-be-played-left-handed | "The violin is traditionally played by placing it on the left shoulder, balancing the neck using the left hand, and bowing with the right arm." |
| Q25 | https://en.wikipedia.org/wiki/Violin_technique | "The left hand regulates the sounding length of the strings by stopping them against the fingerboard with the fingers, producing different pitches." |
| Q26 | https://sschoreography.com/elevating-dance-cinematography-the-impact-of-drone-cameras/ | "The best angles for dance are not always eye level and what better way to explore formations and choreography than from a bird's eye view?" |
| Q27 | https://skylum.com/blog/dance-photography | "Study when the peak movement happens. Knowing the rhythm is the first step to syncing your shutter with their leap." |
| Q28 | https://skylum.com/blog/dance-photography | "Shoot in bursts : Use continuous shooting to catch the peak of motion." |
| Q29 | https://www.youtube.com/watch?v=aiKGYFx3VPg | "With a few extra prompt tricks, you can turn this into a full storytelling workflow that even works with two characters, staying consistent in every scene." `[TRANSCRIPT]` |
| Q30 | https://www.youtube.com/watch?v=aiKGYFx3VPg | "If you only use the face as your input, Nano Banana has to guess the rest of the body. And that's where things start falling apart." `[TRANSCRIPT]` |
| Q31 | https://www.youtube.com/watch?v=aiKGYFx3VPg | "The half body shot also stays very consistent, but with the full body shot, the tattoos shift a bit" `[TRANSCRIPT]` |
| Q32 | https://aimeetsgirlboss.substack.com/p/how-to-get-consistent-character-images | "I figured out maybe I need one image per person, in multiple perspectives." `[WEBFETCH]` |
| Q33 | https://aimeetsgirlboss.substack.com/p/how-to-get-consistent-character-images | "Every character sheet has a name on it visually. Now when I say 'Quinn does this and Kristina does that in the image,' GPT understands perfectly who it is about." `[WEBFETCH]` |
| Q34 | https://www.youtube.com/watch?v=DXlM8J8EZOA | "The faces don't look mangled. Sometimes when doing this test, if you zoom in on a face that's like somewhere over here, it's going to look like something out of a horror film. I don't see that happening here, which is good." `[TRANSCRIPT]` (GPT Images 2.0, escena de muchas personas **sin** referencias) |
| Q35 | https://www.mindstudio.ai/blog/chatgpt-images-2-5-review | "Identity consistency is the headline improvement: reference photos of real people now produce results that look noticeably closer to the original subject than the prior model managed." (Images 2.5, 2026-09) |
| Q36 | https://flowith.io/blog/nano-banana-consistent-characters-storyboard/ | "For very long sequences, periodic re-anchoring is essential. Consider breaking the project into chapters, with fresh reference establishment at each chapter's beginning." |
| Q37 | https://www.reddit.com/r/Bard/comments/1mvhhh1/nanobanana_is_amazing_but_it_does_not_produce/ | "You will observe that the background faces are definitely not the same faces as the people you know." (pullpush.io) |
| Q38 | https://www.reddit.com/r/aiArt/comments/1tgajli/gpt_image_vs_nano_banana_pro_on_the_same_9_gaze/ | "Honest comparison after looking at both: Identity consistency goes to NB Pro by a clear margin. Same face structure across all 9 cells" `[SNIPPET-ONLY]` |
| Q39 | https://www.rewarx.com/blogs/gpt-image-2-face-consistency-ecommerce | "GPT Image 2 processes each image independently without maintaining facial reference data across generations" (SEO sin datos; se cita solo como afirmación de campo no verificada) |
| Q40 | (resultado de búsqueda, URL no localizada entre las páginas leídas; candidatas mindstudio/datacamp no lo contienen) | "Images 2.0 duplicated three faces across an image when asked to generate a specific count of people" `[SNIPPET-ONLY]` — **no verificado**, se registra solo como lead |

## (3) Tabla de veredictos

| Regla [A PRUEBA] (texto exacto) | Veredicto | URLs que lo sostienen | Nota |
|---|---|---|---|
| §1 "Cargar cuando tres o más personas del cuadro deben ser reconocibles y consistentes a lo largo de la pieza." | **SIN EVIDENCIA** (no evaluable en campo) | — | Enrutado interno. El campo sí fija el techo del régimen: 5 identidades (NBP) y 4 (NB2 API), ver §6. |
| §1 "Si solo uno a tres necesitan identidad y el resto es masa, cargar `08-multitud-anonima.md`." | **SIN EVIDENCIA** (no evaluable en campo) | — | Idem. |
| §2.7 "Los instrumentos y props de cada miembro son objetos ancla: se canonizan y se heredan, con lateralidad correcta, violín sobre el hombro izquierdo, arco en la mano derecha, salvo zurdo declarado." | **CONFIRMADA EN CAMPO** (la lateralidad; la canonización es método del repo) | Q24 https://www.normans.co.uk/blogs/blog/can-the-violin-be-played-left-handed · Q25 https://en.wikipedia.org/wiki/Violin_technique | `[QUOTED]` (Q24, Q25) dos fuentes independientes: hombro izquierdo, mano izquierda en el diapasón, arco con el brazo derecho; la excepción zurda existe pero es rara e incluso zurdos tocan del modo tradicional (Q24 contexto). `[ABSENT]` no se encontró caso documentado de un modelo invirtiendo el violín; el riesgo de lateralidad en modelos solo tiene apoyo indirecto (07 Q26, Midjourney 2023 sin distinguir izquierda/derecha). |
| §3 "Coreografía en el pico: blur parcial en la extremidad que se mueve y torsos nítidos; un solo miembro en el pico máximo, los demás un instante detrás, para que no parezcan copias." | **SIN EVIDENCIA** (y con una tensión) | Q27, Q28 https://skylum.com/blog/dance-photography · 08 Q11 https://caniphish.com/blog/how-to-spot-ai-images | `[QUOTED]` (Q27, Q28) la fotografía de danza real busca el pico y lo **congela** en ráfaga (1/500–1/1000 en los resúmenes de búsqueda), no blur parcial; el blur parcial es una elección estética del repo, no una práctica documentada. `[DERIVED]` (08 Q11) desfasar a los miembros sí ataca la firma de clones ("matching head tilts, identical smiles, or arms posed at the same angle"), pero ninguna fuente prueba que "uno en el pico y los demás un instante detrás" sea lo que funciona en generación. Queda para el ejercicio. |
| §5 "Overhead solo para leer la coreografía como figura geométrica, y en ese plano se renuncia a la identidad." | **CONFIRMADA EN CAMPO** (fotografía real) | Q26 https://sschoreography.com/elevating-dance-cinematography-the-impact-of-drone-cameras/ · Q22 https://digital-photography-school.com/how-to-take-great-group-photos/ | `[QUOTED]` (Q26) el cenital se usa para formaciones y patrones. `[DERIVED]` (Q22 y su contexto "want to be able to see each person's face") el retrato de grupo exige ver cada rostro, lo que el cenital no da. Dos fuentes de dominios distintos convergen. |
| §6 "La regla de una sola pasada con todos los maestros adjuntos es inferencia hasta probarla: dieciséis referencias aceptadas no garantizan dieciséis identidades sostenidas; verificar miembro por miembro." | **CONFIRMADA EN CAMPO** | Q6 https://developers.openai.com/api/reference/python/resources/images/methods/edit · Q1, Q2 https://ai.google.dev/gemini-api/docs/image-generation · Q4 https://blog.google/innovation-and-ai/products/nano-banana-pro/ · Q12 https://research.everypixel.com/gpt-image-2-0/ · Q14, Q15 https://queststudio.io/blog/chatgpt-group-photo-prompts | `[QUOTED]` (Q6) OpenAI documenta 16 imágenes de entrada y **no publica ninguna cifra de identidades sostenidas**. `[QUOTED]` (Q1, Q4) Google demuestra que entrada ≠ identidad: 14 imágenes de entrada pero 5 personas (NBP) o 4 personajes (NB2 API). `[QUOTED]` (Q12, Q15) el benchmark y la guía de producción coinciden: grupos pequeños y revisión rostro por rostro porque "one person is wrong" no se ve de lejos. Ver la respuesta a la pregunta central más abajo. |

Resumen: **3 CONFIRMADAS EN CAMPO · 0 REFUTADAS · 3 SIN EVIDENCIA** (dos de enrutado, una de estética de pico).

### Respuesta a la pregunta central: ¿GPT Image 2 con 16 referencias sostiene 5+ identidades en una pasada?

- `[QUOTED]` (Q6, Q9) El límite de **16 imágenes** es real y oficial (API de edición) y lo repite la
  guía de apiyi; la guía de Luma dice "Up to 4 input images" (Q10, `[WEBFETCH]`), discrepancia que
  probablemente refleja la UI de ChatGPT o una versión anterior. El repo puede seguir citando 16 para API.
- `[ABSENT]` **No se encontró ninguna fuente, profesional ni de comunidad, que documente a GPT Image 2
  sosteniendo cinco o más identidades con referencias en una sola pasada.** La única evidencia de "muchas
  personas" en GPT Image 2 es sin referencias (Q34: rostros de fondo "not mangled" en una LAN party) y el
  benchmark lo desaconseja para multitudes (Q12). La guía de producción de grupos para ChatGPT (Q14–Q16)
  trabaja etiquetando persona por persona y cambiando una región por vez, es decir, el mismo método
  secuencial del repo. Hipótesis "5+ identidades en una pasada en GPT Image 2": **sin evidencia, retraída
  hasta ejercicio propio.**
- `[QUOTED]` (Q1, Q2, Q4, Q5, Q13, Q19, Q21) Para Nano Banana la cifra sí está documentada y probada por
  terceros: **NBP = 5 personas** (Google oficial, con ejemplo publicado de 5 personas + perro en una
  pasada desde 6 fotos); **NB2 = 4 personajes vía API y 5 en la app Gemini** (doc oficial + glbgpt);
  Curious Refuge reporta 5 personajes de referencia colocados con éxito en una mesa de restaurante con
  NB2. Un tutorial de campo solo llega a demostrar **2** personajes consistentes en NBP (Q29).
- `[QUOTED]` (Q37) Aun dentro del límite, cualquier edición regenera los rostros que no son el sujeto de
  la edición: la verificación miembro por miembro tras cada paso no es opcional.
- `[QUOTED]` (Q35) Images 2.5 (sept 2026) mejora la fidelidad de identidad **de un sujeto** desde foto;
  ninguna fuente extiende esa mejora a grupos.
- **Conclusión operativa:** para ensambles de hasta 5 con NBP (o 4 con NB2 API) la pasada única con
  referencias tiene respaldo de proveedor y de terceros y merece ejercicio; para más de 5, o para GPT
  Image 2 con cualquier N, la inserción secuencial sigue siendo la única estrategia con evidencia.

Reglas [FUENTE] que el campo confirma o matiza: §6 "NBP hasta cinco referencias de personaje y NB2 hasta
cuatro" confirmada literalmente (Q1, Q2, Q4, Q19). §2.1 "nunca el grupo completo desde texto" confirmada
en su enunciado (desde texto) pero **matizada**: con referencias y N ≤ 5, Google publica el grupo completo
en una pasada como caso de uso oficial (Q5). §7 "herencia mínima … cero re-descripción" confirmada por
Q17 (la descripción larga del rostro produce "a blended stranger").

## (4) Hallazgos nuevos (reglas candidatas)

1. Nunca describir el rostro en texto cuando ya viaja en la referencia: la descripción facial larga
   compite con la imagen y produce un "blended stranger". `[QUOTED]` (Q17)
   [CAMPO: https://www.ud.hk/en/blogs/insight/article/2026-06-29-nano-banana-consistent-characters]
2. Para una inserción de cuerpo entero debe adjuntarse una hoja lado a lado (rostro en primer plano +
   cuerpo entero con vestuario) y no solo el maestro de rostro: con solo la cara el modelo "has to guess
   the rest of the body" y los detalles de cuerpo entero derivan (tatuajes desplazados). `[QUOTED]` (Q30, Q31)
   [CAMPO: https://www.youtube.com/watch?v=aiKGYFx3VPg]
3. Siempre etiquetar a cada persona por número o nombre visible en su hoja de referencia y usar esa
   etiqueta en el prompt; nunca "la mujer del fondo". `[QUOTED]` (Q7, Q14, Q33)
   [CAMPO: https://replicate.com/openai/gpt-image-2 · https://queststudio.io/blog/chatgpt-group-photo-prompts]
4. Nunca corregir dos regiones en la misma instrucción: cambiar una región por vez, porque una
   instrucción grande "invita" al modelo a redibujar lo que ya estaba bien. `[QUOTED]` (Q16)
   [CAMPO: https://queststudio.io/blog/chatgpt-group-photo-prompts]
5. Más referencias no es mejor: nunca adjuntar del mismo miembro fotos con luz y expresión dispares;
   una referencia limpia primero, escalar a varias solo si el rostro no se sostiene. `[QUOTED]` (Q18)
   [CAMPO: https://www.ud.hk/en/blogs/insight/article/2026-06-29-nano-banana-consistent-characters]
6. En secuencias largas debe re-anclarse al maestro original por capítulos en lugar de encadenar
   siempre sobre la última salida. `[QUOTED]` (Q36)
   [CAMPO: https://flowith.io/blog/nano-banana-consistent-characters-storyboard/]
7. El presupuesto de referencias de NBP debe contarse en identidades, no en imágenes: 14 imágenes de
   entrada, 5 identidades; el resto del cupo es para props, escenario y estilo. `[QUOTED]` (Q1, Q4)
   [CAMPO: https://ai.google.dev/gemini-api/docs/image-generation · https://blog.google/innovation-and-ai/products/nano-banana-pro/]
8. Tras cada inserción el crítico debe re-verificar a **todos** los miembros ya colocados, no solo al
   nuevo: la edición regenera rostros que no eran el objetivo. `[QUOTED]` (Q37)
   [CAMPO: https://www.reddit.com/r/Bard/comments/1mvhhh1/nanobanana_is_amazing_but_it_does_not_produce/]
9. `[SNIPPET-ONLY]` r/aiArt reporta que NBP supera a GPT Image en consistencia de identidad en una
   rejilla de 9 miradas (Q38); r/StableDiffusion 1wetnrt describe un flujo "Multi Reference Shot" con
   referencias separadas para luz, composición y blocking. Ambos ilegibles; leads para el ejercicio.

## Fase 5 — Forbidden patterns scan

☐ Ejecutado. Detecciones: (a) la cifra "Keep the group to 2-5 people" apareció en un resumen de búsqueda
sin URL verificable → **eliminada** de veredictos; (b) "Images 2.0 duplicated three faces … 41 people /
35" no se localizó en ninguna página leída → degradada a Q40 `[SNIPPET-ONLY]` sin uso en veredictos;
(c) las cifras de selfielab ("85%", "90% consistency") carecen de fuente → no se usan. Ninguna autoridad
sin URL.

## (5) Checklist de auditoría del skill

- [x] 5+ queries (17)
- [x] 7+ fetch attempts (31)
- [x] 4+ fetches exitosos con quotes (24)
- [x] 4+ fuentes profesionales (8)
- [x] 2+ queries anti-patrón (4: #6, #10, #14, #17)
- [x] Cada claim con Q#
- [x] Etiquetas epistémicas en cada claim
- [x] Sin paráfrasis presentada como cita (WEBFETCH/TRANSCRIPT/SNIPPET marcados)
- [x] Sin autoridad sin URL
- [x] Forbidden patterns scan ejecutado (3 correcciones)
- [x] Limitaciones presentes

## Limitaciones

- Ningún test público de GPT Image 2 con ≥3 referencias de personas distintas fue localizado; la
  respuesta a la pregunta central es una ausencia documentada, no una refutación.
- Reddit casi inaccesible (1 de 12 hilos legible); r/aiArt 1tgajli (comparación de identidad NBP vs GPT
  Image) sería la fuente comunitaria más directa y quedó en snippet.
- La página oficial de OpenAI "The new ChatGPT Images is here" devolvió 403; el límite de 16 se toma de la
  referencia de API, que es igualmente oficial.
- Curious Refuge no publica método ni cuántas variantes necesitó para los 5 personajes.
- Los transcritos de YouTube son automáticos; se citan solo pasajes inequívocos.

## Próximo paso

Ejercicio en dos brazos: (A) quinteto en NBP en **una pasada** con 5 maestros (2 imágenes por miembro,
hoja rostro+cuerpo) y anclas de posición en placa vacía; (B) el mismo quinteto por inserción secuencial.
Crítico rostro por rostro en ambos y recuento de miembros alterados tras cada paso. Si (A) sostiene 5,
la regla §2.1 se matiza a "desde texto" y §6 se canoniza con N ≤ 5 en NBP; GPT Image 2 se prueba aparte
con 3, 5 y 8 referencias etiquetadas para medir dónde se rompe.
