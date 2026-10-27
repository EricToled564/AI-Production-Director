# Relectura del universo y de la adenda con el plan delante — 2026-10-27

Qué se leyó: los 2,722 textos de `v3/universo/universo_prueba_textos.jsonl` (volcado completo por archivo y línea,
2,803 líneas, comprobado: los 2,722 ids presentes) y los 40 textos de la adenda que entran. Cada texto se leyó entero.

Pregunta por texto: ¿cambia algo del plan (una regla común, una fila del mapa, un caso, una tarea, un control)?
Esto no es la lista de referencia por caso (tarea 4 del plan): no decide si un texto aplica a un caso, solo si el plan
tiene que cambiar.

Códigos de veredicto:

- **N1** sin cambio al plan: regla de contenido, técnica o criterio; la tarea 4 la marca caso por caso.
- **N2** sin cambio al plan: rótulo, título, nodo de diagrama, leyenda o texto sin norma propia; la tarea 4 lo marca.
- **N3** sin cambio al plan: el plan ya lo recoge (se indica dónde).
- **N4** sin cambio al plan: rige video, clip o movimiento; en imagen fija solo cuenta por su efecto en el ancla.
- **C** cambia el plan: se dice qué.

Cada fila cubre un intervalo de ids consecutivos del universo dentro de un mismo archivo; todos los ids del intervalo
que existen en el universo llevan ese veredicto (los huecos son textos fuera del universo).

## flujos/flujo-anclas.html

| Ids | Veredicto | Motivo |
|---|---|---|
| 000001–000011 | N2 | título, leyenda y encabezados |
| 000012–000016 | N1 | roles del ancla (character ref con luz pareja y fondo limpio; environment ref; FF; LF; hero) |
| 000018–000024 | N1 | lo que el video hereda del still: ratio desde el inicio, identidad, luz, geometría |
| 000025–000030 | N3 | texto superpuesto en capa aparte y logos solo heredados: `01_texto_en_imagen.md` |
| 000031–000052 | N1 | tarjeta D1–D9 y ángulo por tipo de acción |
| 000053–000120 | N3 | flujo A0–A12 citado en el §3 del plan |
| 000121–000131 | N1 | seis tipos de acción y cómo se congela cada uno |
| 000132–000206 | N1 | tratamiento de personas por número de sujetos; grupo ensamble EN.1–EN.6 |
| 000207–000212, 000214–000215 | N1 | defaults por tratamiento |
| 000213 | C | el tratamiento «comercial pulido» prohíbe «texto en imagen»: el caso con texto no puede llevar ese tratamiento salvo decisión; se diseña con otro tratamiento (§4 del plan) |
| 000216–000219, 000222, 000225 | N1 | modelo y resolución por situación; GPT Image 2 high para rostro, etiqueta y texto; ratio máximo 3:1 |
| 000220 | C | arquitectura real, landmark, especie animal o vegetal: NB2 con grounding; «GPT solo anclas de época». Con solo GPT Image 2 (23 §6) la ruta NB2 queda excluida por decisión; el caso se prueba con GPT Image 2 anclado en época o lugar. Una falla de ese caso puede deberse a la regla excluida: el diagnóstico necesita esa salida (tarea 12) |
| 000226–000249, 000251–000260 | N1 | orden de bloques del still, bloques SW30, lints y checks del crítico por tipo de acción |
| 000250 | N3 | aurora: excluida (PILOTO §0.4) |
| 000261–000269 | N4 | motion brief y consecuencia para la base de reglas |
| 000270–000293 | N1 | familias de régimen y etiquetas de origen: gobierno de reglas del repo |

## flujos/flujo-spot.html

| Ids | Veredicto | Motivo |
|---|---|---|
| 000297–000358 | N2 | presentación del megaflujo y sus etapas |
| 000392–000401 | N3 | subprocesos E5.1–E5.9; E5.3–E5.5 citados en el §3 del plan |
| 000417–000430, 000435–000438, 000440–000447, 000449, 000457–000464, 000470–000475, 000478–000479, 000482–000517, 000523–000524 | N1 | taxonomía de génesis por clase, cadena de dependencia, nodos del diagrama |
| 000431–000432, 000450–000452, 000476 | C | edificación o landmark: grounding solo NB2; «GPT Image 2 para época y cultura, no para geometría exacta». El caso de edificación se diseña con GPT Image 2 anclado en época y cultura; la parte NB2 queda excluida por decisión (23 §6) |
| 000433–000434, 000456, 000477 | C | animal: NB2 con grounding para la especie; sin template de identidad; «anatomía y pelaje se auditan como manos y rostros». Con GPT Image 2 el caso de animal entra; la QA (tarea 11) incluye anatomía y pelaje al 100 % |
| 000448 | C | lugar desde plano: `dimensional.md` (plano → interior o exterior). Es el caso de boceto o plano a final con `dimensional.md` (falta en el plan, ver `03_citas_plan.md` B5) |
| 000465–000469 | N1 | producto o logo de marca real sin foto: no es génesis, entra por el flujo con referencia |
| 000480 | C | principio de dos pasos por clase: animal, cabeza y pelaje antes que poses; producto, hero frontal antes que producto en escena. Las cadenas de casos siguen ese orden (§4 del plan) |
| 000481 | N1 | hueco de códigos de caso en la base de reglas del repo (no es la taxonomía de la prueba) |
| 000525–000614 | N3 | génesis paso a paso: citado en el §3 del plan |

## skills/ai-production-director/SKILL.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 000678–000680 | N1 | etapa 5: forge borrador, `image` sintaxis final, el usuario genera, el crítico evalúa |
| 000681 | N3 | máximo 2 rondas de revisión y replanteo a la tercera: tarea 12 del plan (bucles R12, R13) |
| 000698–000699 | N3 | vocabulario prohibido gana: §2 del plan |
| 000700–000705 | N3 | sintaxis final la manda `image` (smixs) y el forge solo el flujo de datos: base de la verificación de texto en imagen |

## skills/image/SKILL.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 001998–002006 | N1 | descripción del skill y enrutamiento previo; 002004 remite a otro skill no instalado |
| 002007–002019, 002037–002041 | N1 | orden de lectura obligatorio: models → archivo de modelo → golden-rules → lectura por tarea |
| 002020 | N3 | texto en imagen → `text-rendering.md`: `01_texto_en_imagen.md` |
| 002021, 002025 | N3 | cargas de `editing.md` y `structural.md`: §3 del plan |
| 002026 | C | carga de `dimensional.md` (2D → 3D, planos): falta en el §3 del plan (B5) |
| 002027 | C | carga de `vision-decomposer.md`: es el caso de descripción de imagen (26 §12, §13); ver `04_preguntas_eric.md` |
| 002022–002024, 002028–002036 | N1 | cargas por tarea: personajes, slides, storyboards, multipanel, bibliotecas de patrones |
| 002042–002046 | N3 | formato de salida y preserve-list de edición: tareas 9 y 10 del plan |
| 002047–002052 | N1 | estilo de respuesta (5 slots para GPT Image, sin tag soup, sin elogio vago, encuadre positivo); atribución: EXCLUIDA POR DECISIÓN (DEC-000024) en material al cliente |

## skills/image/references/characters.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002053 | N2 | título |
| 002054 | N3 | 16 referencias con rol (corregido, 26 §1): §3 del plan |
| 002055–002082 | N1 | identity locking, miniaturas, varios personajes, producto como referencia, expresión, pose, vestuario, entorno |
| 002083 | N1 | atribución: EXCLUIDA POR DECISIÓN en material al cliente (DEC-000024) |

## skills/image/references/creative-direction.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002084–002124, 002126–002155, 002159, 002161–002165 | N1 | luz, cámara y hardware, ángulos, foco, grade y película, materialidad, ejemplos |
| 002125 | N1 | parámetros de lente con nombre menos fiables que términos descriptivos: entra en la búsqueda de reglas de lente para la cara (decisión 24 §3), tarea 4 |
| 002156–002158, 002160 | N3 | ejemplos con «photorealistic» / «hyper-realistic» y marca de agua de un tercero: el vocabulario prohibido manda (§2 del plan); la tarea 4 los marca |
| 002166 | N1 | atribución: EXCLUIDA POR DECISIÓN (DEC-000024) |

## skills/image/references/dimensional.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002167–002168, 002187–002191 | N1 | encabezados y niveles de calidad («Photorealistic» como nivel: la palabra no va al prompt) |
| 002169–002170, 002180–002184 | C | plano 2D → interior y elevación → exterior: casos de boceto o plano a final con `dimensional.md` (falta en el plan) |
| 002171–002179, 002185–002186 | N1 | boceto → 3D, 3D → plano técnico, meme, producto 2D → 3D: la tarea 4 decide si aplican al caso fotográfico |
| 002192–002193 | N1 | separador y atribución (DEC-000024) |

## skills/image/references/editing.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002194–002195, 002198 | N1 | encabezado; un edit por iteración |
| 002197 | N3 | GPT Image 2: Change / Preserve / Constraints; `mask_image_url` opcional: sin máscara por 26 §8 |
| 002199–002225, 002228–002229 | C | patrones de cada hijo de edición: quitar objeto, añadir, luz, estación o clima, colorizar foto B/N, restaurar foto dañada, traducir texto, física. Cada hijo de F10 tiene caso (26 §12); colorizar y restaurar necesitan como entrada una foto B/N o dañada, que la cadena de casos produce antes |
| 002226 | N2 | encabezado |
| 002230–002237 | N1 | refinamiento conversacional y atribución (DEC-000024) |

## skills/image/references/golden-rules.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002238–002239 | N1 | alcance: ambas familias de modelos |
| 002240–002241 | N3 | empezar con verbo: dentro del slot Scene (`armar.py` REQUERIDOS; OVERRIDE R1 de la tarea 10) |
| 002242–002246, 002252–002265 | N1 | encuadre positivo, lenguaje natural, especificidad, contexto: tarea 4 |
| 002247–002251, 002279–002284 | N3 | editar, no re-tirar; refinamiento: tarea 12 |
| 002266–002273 | N3 | texto entre comillas y plantilla con tipografía: `01_texto_en_imagen.md` |
| 002274–002278 | N3 | quality low → high: decisión 23 §7 y 26 §8 (la app no expone quality) |
| 002285–002297 | N3 | referencias con rol, 16 en GPT Image 2; estilo como referencia: §3 del plan |
| 002298–002318 | C | anclas de época, cultura y género: «funcionan mejor con GPT Image 2». Es la vía documentada para el caso de edificación o landmark sin grounding |
| 002319–002328 | N1 | ejemplos de anclas |
| 002329–002330 | N1 | separador y atribución (DEC-000024) |

## skills/image/references/gpt-image.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002331–002338 | N3 | 5 slots y ejemplo con letrero: §3 del plan y `01_texto_en_imagen.md` |
| 002339–002346 | N3 | anti-slop: vocabulario prohibido (§2 del plan) |
| 002347–002353 | N3 | quality: decisión 23 §7; la app no la expone (26 §8) |
| 002354–002365 | N3 | tamaños y ratio máximo 3:1: el ratio va en Scene y la QA lo mide (tareas 9 y 11) |
| 002366–002372 | N3 | texto en imagen: `01_texto_en_imagen.md` |
| 002373–002381, 002384 | N3 | edición Change / Preserve / Constraints; endpoint de API y máscara no aplican en la app (26 §8) |
| 002382 | C | virtual try-on: patrón del hijo «edición: cambiar vestuario», con caso propio |
| 002385 | C | interior swap: patrón del hijo «edición: cambiar mobiliario u objeto», con caso propio; contiene «Photorealistic», que no pasa al prompt |
| 002386–002392 | N3 | referencias con rol, transferencia de estilo y conocimiento del mundo: §3 del plan |
| 002393–002397 | N3 | iteración: un cambio por ronda (tarea 12) |
| 002398–002400 | N3 | plantilla editorial fotográfica: base de `armar.py` |
| 002401–002408 | N1 | plantillas de producto, UI, creativo con texto, infografía: dependen de qué valores de F04 entran (`02_facetas_tipo_imagen.md` §C) |
| 002409–002414 | N1 | migración (F35 «no» en la prueba) y atribución (DEC-000024) |

## skills/image/references/models.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002415–002431 | N1 | tabla de elección de modelo; la prueba fija GPT Image 2 (23 §6); 002430 transferencia de estilo sin referencia adjunta va a GPT Image 2 |
| 002432–002459 | N1 | dónde gana cada modelo y diferencias de sintaxis; ya reflejado en el armador (5 slots, texto, edición) |
| 002460–002472 | N1 | coste orientativo y atribución (DEC-000024) |

## skills/image/references/multi-panel.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002473–002567 | N1 | rejillas, collage, secuencia de 6 cuadros, antes/después en una sola imagen: son el valor F04 «storyboard o multipanel»; entran como casos si Eric cuenta F04 como tipo (`02_facetas_tipo_imagen.md` §C) |
| 002568–002596 | N1 | póster de 12 paneles y consejos generales de multipanel (mismo veredicto que el bloque anterior); atribución (DEC-000024) |

## skills/image/references/patterns/character-design.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002675–002713 | N1 | hoja de giro, hoja de expresiones, rejilla de vestuario, coleccionable chibi y ficha de anime: técnicas sobre todo no fotográficas (fuera de la prueba por 26 §12; se clasifican en la prueba posterior); la rejilla de vestuario puede ser fotográfica y depende de F04 «diseño de personaje» (`02_facetas_tipo_imagen.md` §C2) |

## skills/image/references/patterns/ecommerce.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002718–002754 | N1 | patrones de producto (diorama en miniatura, cosmético de lujo, storyboard de 9 paneles, ingredientes flotando congelados, póster inflable): la tarea 4 los marca para los casos de producto |

## skills/image/references/patterns/fashion-editorial.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002760–002795 | N1 | collage de campaña, rejilla 2x2, póster con tipografía, campaña retro en prosa, editorial con formas 3D: la tarea 4 los marca; el póster con tipografía es candidato del caso con texto |

## skills/image/references/patterns/food-beverage.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002801–002843 | N1 | chocolate, tablero de bebida, póster de comida: patrones fotográficos de producto o comida |
| 002844–002855 | N1 | lámina naturalista y mapa ilustrado de ciudad: ilustración, fuera de la prueba (26 §12) |

## skills/image/references/patterns/portrait-cinema.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002861–002896 | N1 | retrato a contraluz en la calle, neón de tienda, perfil monocromo con glitch, película negativa en azotea, retrato subacuático: patrones de retrato que la tarea 4 marca para los casos con persona |

## skills/image/references/patterns/poster-illustration.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002902–002919 | N1 | ciudad en dos épocas (ancla de época sobre un lugar: candidato del caso de edificación), collage de boxeo |
| 002920–002933 | N1 | smartphone con titular y póster de moda con tipografía: candidatos del caso con texto y de F04 «póster o key art» |
| 002934–002939 | N1 | lámina de pavo real: ilustración, fuera de la prueba (26 §12) |

## skills/image/references/patterns/ui-social.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 002945–002983 | N1 | historia de Instagram, post 1:1, captura de App Store, dashboard, tablero de análisis de color: dependen de F04 (post para redes, UI o mockup) y F32 (`02_facetas_tipo_imagen.md` §C) |

## skills/image/references/prompt-framework.md (primera parte)

| Ids | Veredicto | Motivo |
|---|---|---|
| 002988–002996 | N1 | encabezados y remisión a los archivos de modelo |
| 002997–003005 | C | tipos de tarea del corpus: fotográfico, ilustración, producto, minimalista, secuencial, edición, transferencia de estilo, composición, texto en imagen. Con 26 §12 entran los fotográficos: producto, secuencial con fotos, edición, transferencia, composición y texto; ilustración queda fuera. Refuerza `01_texto_en_imagen.md` y la pregunta de F04 |
| 003006–003016 | N1 | elementos universales del prompt |
| 003017–003019 | N1 | materiales, paleta en hex, formato |
| 003020 | N1 | parámetros de lente: GPT Image 2 admite «50mm feel» como look; entra en la búsqueda de reglas de lente para la cara (decisión 24 §3), tarea 4 |
| 003021–003027 | N1 | modos de detalle |
| 003028–003036 | N3 | estructura de salida: prompt, parámetros, exclusiones en positivo y supuestos (Notes): tarea 10 |
| 003037–003038 | C | árbol de decisión de tipos: mismo listado que 002997–003005 |
| 003039 | N3 | grounding y ratios extremos solo en Nano Banana: excluidos por 23 §6; ratios de F06 fuera de 3:1 no entran (`02_facetas_tipo_imagen.md` §B) |
| 003040–003048 | N1 | ejemplos por tipo; 003047–003048 ejemplo de texto en imagen (`01_texto_en_imagen.md`) |
| 003049–003063 | N1 | plantillas parametrizadas en 5 slots |
| 003064–003085 | N1 | modo cinematic verbose y checklist de microdetalles |
| 003086–003087 | N1 | separador y atribución (DEC-000024) |

## skills/image/references/slides.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 003088–003184 | N1 | principios, tipos, tipografía, color y retículas de diapositivas: F04 «slide o presentación», no fotográfico por técnica (`02_facetas_tipo_imagen.md` §C2) |
| 003185–003224 | N1 | resto de retículas, estilo brutalista y SaaS de diapositivas, atribución (mismo veredicto que el bloque anterior) |

## skills/image/references/storyboards.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 003225–003254 | N1 | secuencias de varias imágenes «one at a time» con identidad constante: serie de imágenes, no un tipo de imagen única; si la prueba incluyera una serie, el chat nuevo por prompt del plan obliga a adjuntar la referencia en cada paso (ya en §2 del plan). Concept art y sprites: no fotográficos |

## skills/image/references/structural.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 003255–003259 | N3 | boceto → final, con posición del texto: §3 del plan |
| 003260–003271 | N1 | wireframe → mockup, retícula, pixel art: UI y pixel art dependen de F04 o quedan fuera por técnica |
| 003272–003277, 003280–003291 | N1 | guía de layout y plantillas de composición desde una referencia (F23 «estructura o composición») |
| 003278–003279 | N1 | sistema de identidad desde un logo: F04 «identidad de marca», no fotográfico (§C2) |
| 003292–003293 | N1 | separador y atribución (DEC-000024) |

## skills/image/references/text-rendering.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 003294–003299 | N3 | alcance y estructura del texto en imagen: `01_texto_en_imagen.md` |
| 003300–003349 | N1 | estilos visuales y layouts de infografía: casi todos no fotográficos; F04 «infografía o diagrama» queda en §C2 |
| 003350–003392 | N1 | resto de layouts, ejemplos ilustrados, texto primero, fuentes, localización, consejos y atribución; 003374–003380 multilingüe: base del hijo «edición: traducir texto» |

## skills/image/references/vision-decomposer.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 003393–003457 | C | análisis de imagen a prompt. Es el caso de descripción de imagen que exige 26 §12: dos pasos (descomposición en cuatro bloques y síntesis), salida en dos bloques (registro de análisis y prompt) más Model / Quality / Size. Choca con el plan en dos puntos que solo Eric resuelve (`04_preguntas_eric.md`): el contrato no tiene esa operación (schema L45–54; taxonomía L260, «un modo sin contrato original suficiente permanece no habilitado»), y el prompt sale en palabras clave por comas (`:61`) mientras `verificar_templates.py` L62–65 exige los 5 slots para GPT Image 2 (`CONTRADICCIONES.md` §3). La mención de «style transfer» en `:3` y `:104` no cambia K07 (26 §13) |
| 003458–003459 | N1 | separador y atribución (DEC-000024) |

## skills/storyboard-architect/references/on-screen-text.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 005729–005731 | N3 | reservar espacio para texto superpuesto: texto de capa aparte (`01_texto_en_imagen.md` §1) |

## skills/storyboard-architect/references/shot-grammar.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 005774–005804, 005806–005832 | N1 | encuadre, ángulo, profundidad de campo, luz fijada una vez, descripción del sujeto sin adjetivos de emoción, brand_lock frente a series_lock |
| 005805 | N4 | movimiento de cámara: intención para el montaje en stills |

## skills/video/references/animatic-keyframes.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 007978–007990 | N1 | qué hace un keyframe y su tarjeta: base de los casos de ancla (D1–D9 del plan) |
| 008002–008019 | N1 | seis cues de movimiento congelado y presupuesto de velocidad |
| 008021–008036 | N1 | emoción sin rostro: anatomía solo en decisión, objetos que cambian de estado |
| 008038–008050 | N1 | cuadro cargado: un foco, tres planos con trabajo, ángulo como emoción |
| 008052–008060 | N1 | del keyframe al prompt de imagen: orden de tokens, blur diferencial, sin rostro o fragmentado, anti-estéril |
| 008061 | N4 | el keyframe pasa a Seedance, Kling o Veo |
| 008082–008092 | N1 | checklist del keyframe; paleta fría y ban de ámbar son del registro race |
| 008096–008097 | N1 | separador y atribución (DEC-000024) |
| 008020, 008037, 008051, 008062 | N2 | separadores de sección |

## skills/video/references/camera-lighting-vocabulary.md (primera parte)

| Ids | Veredicto | Motivo |
|---|---|---|
| 008113–008129 | N1 | vocabulario de encuadre |
| 008157–008167 | N1 | lenguaje de lente (85mm retrato y fondo comprimido, 24mm distorsión de proximidad): entra en la búsqueda de reglas de lente para la cara (decisión 24 §3), tarea 4 |
| 008168–008170 | N1 | fuentes de luz |
| 008171–008214 | N1 | fuentes, dirección y calidad de luz |
| 008215–008225 | N1 | disciplina de color con colores concretos; paletas nombradas |

## skills/video/references/fixes-and-skeletons.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 008582–008584 | N1 | caras de aspecto IA: sin «hyperrealistic 8k masterpiece», lenguaje de producción; parte de la búsqueda de decisión 24 §3 |
| 008585–008588 | N1 | gemelos y fusión de rostros en escenas de varias personas |

## skills/video/references/race-and-speed.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 008982–008997 | N1 | vender velocidad en un still: presupuesto de cues, referencia de primer plano, compresión de teleobjetivo |
| 009054–009076 | N1 | luz y color sin rostros: paleta fría y recetas de luz del registro race |
| 009098–009112 | N1 | guardia anti-fake del registro race; atribución (DEC-000024) |

## skills/visual-asset-critic/SKILL.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 009765–009775 | N1 | descripción y cuándo usar |
| 009776–009871 | C | la crítica de cada imagen: markdown más critique JSON 1.1 con procedencia y sha256 de imagen y prompt, seis capas, severidades y veredicto derivado (ACCEPT / REVISE / REJECT), y la validación con `tools/validate_critique.py` (existe en el skill instalado). Los flujos lo exigen (`flujo-anclas.html:214` INV-000109, `flujo-spot.html:570–572` INV-000580–000581). La tarea 11 del plan hace la QA visual con esta crítica, no con una tabla propia |
| 009872–009882 | C | reglas duras del crítico; la regla 4 (fallos conocidos del generador, como manos deformadas: re-roll o post) pide una salida del diagnóstico que hoy no existe en a/b/c (`04_preguntas_eric.md`) |
| 009883–009891 | N1 | referencia, ejemplo y traspaso a la revisión |

## skills/visual-asset-critic/references/critique-rubric.md (primera parte)

| Ids | Veredicto | Motivo |
|---|---|---|
| 010313–010330 | N1 | capas 1 y 2 de la rúbrica: la usa la crítica de la tarea 11; el ratio equivocado es fallo duro (coincide con ADD-0043) |
| 010331–010354, 010356–010386 | N1 | capas 3 a 6, de pass/fail a severidad, veredicto agregado: los usa la crítica de la tarea 11 |
| 010355, 010387 | C | los fallos técnicos duros casi siempre son re-roll (2–3) porque el prompt estaba bien; distinguir fallo del prompt de fallo del generador. Mismo punto que 009880 sobre el diagnóstico (`04_preguntas_eric.md`) |

## skills/visual-media/SKILL.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 011159–011171 | N1 | fundamentos de fotografía: exposición, composición, luz |

## skills/visual-prompt-forge/SKILL.md (primera parte)

| Ids | Veredicto | Motivo |
|---|---|---|
| 011265–011280 | N1 | descripción, cuándo usar, archivos por ronda: el forge trabaja desde `shots.json`; la prueba es de activo directo (FL04) sin `shots.json` |
| 011281–011288 | N3 | anatomía de cinco capas; capa de texto superpuesto fuera del prompt (`01_texto_en_imagen.md` §1) |
| 011289–011311, 011315–011329 | N1 | flujo del forge: validar `shots.json`, leer el adaptador, componer, escribir por ronda, registrar en `run.json` |
| 011312–011314 | N3 | `_capabilities.json` manda sobre el `.md` del adaptador dentro del forge; para el texto final de GPT Image 2 manda `image` (`CONTRADICCIONES.md` §1; taxonomía §6.2 filas 2 y 4) |
| 011330–011359 | N1 | registro en `run.json`, traspaso y modo revisión del forge: re-roll sin cambiar el prompt, parar en REJECT, la edición mínima del fix. Coherente con la tarea 12 del plan |
| 011360–011363 | N3 | regla 1, texto superpuesto fuera del prompt: ámbito forge (taxonomía §6.2 fila 11; `01_texto_en_imagen.md`) |
| 011364–011375, 011384–011385 | N1 | colores de marca no en la prosa del sujeto, anclas de series_lock literales, el adaptador manda en sintaxis dentro del forge, prompts reproducibles |
| 011376–011383 | N1 | regla 6, lógica del plano: tercio del cuerpo, punto de vista, dirección, lateralidad, sin marcas (011383: ver `01_texto_en_imagen.md` §3) |
| 011386–011425 | N1 | referencias, adaptadores, quality bar con `validate_prompts.py` (pipeline de `shots.json`), ejemplos |

## skills/visual-prompt-forge/adapters/_capabilities.json

| Ids | Veredicto | Motivo |
|---|---|---|
| 011426–011494, 011591–011592 | N3 | matriz de capacidades; fila de GPT Image: 300 palabras como techo (aviso del §2 del plan), `supports_style_ref: false` sin efecto en GPT Image 2 (`CONTRADICCIONES.md` §1) |

## skills/visual-prompt-forge/adapters/gpt-image.md (primera parte)

| Ids | Veredicto | Motivo |
|---|---|---|
| 011718–011723 | N3 | el adaptador pide tres párrafos; para el texto final de GPT Image 2 mandan los 5 slots de `image` (taxonomía §6.2 filas 2 y 4) |
| 011724–011733 | N3 | parámetros de API (size, quality, style): la app no los expone (26 §8) |
| 011734–011735 | N3 | 150–300 palabras: referencia de longitud (decisión 26 §11) |
| 011736–011747 | N1 | lenguaje espacial y patrón de composición; cierre «natural skin texture, no AI rendering artifacts» (ya en `armar.py`) |
| 011748–011754 | N3 | texto en imagen en GPT Image: `01_texto_en_imagen.md` §2 |
| 011755–011760 | N1 | errores a evitar: listas con comas, más de cinco elementos, flags; el «AI look» es real |
| 011761–011762 | N3 | acceso: API o la interfaz de ChatGPT (26 §8) |

## skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 012171–012196 | N1 | ejemplo de un plano en todos los adaptadores |
| 012197–012199 | N3 | texto superpuesto fuera de todo prompt (`01_texto_en_imagen.md` §1) |

## skills/visual-prompt-forge/references/consistency-locks.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 012217–012218 | N3 | generadores sin estado: §2 del plan (chat nuevo por prompt; redacción a corregir, `03_citas_plan.md` B7) |
| 012219–012276 | N1 | candados de personaje, entorno, luz, referencia, estilo, dirección de luz y grade; lo que no funciona; presupuestar re-rolls |

## skills/visual-prompt-forge/references/failure-modes.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 012277–012306, 012319–012362 | N1 | fallos y arreglos: aspecto IA, deriva de personaje, dirección de luz, espacio para texto superpuesto, serie distinta, no coincide con el brief |
| 012307–012317 | N3 | fallo 3, texto: ámbito de texto superpuesto del forge (`01_texto_en_imagen.md`) |
| 012363–012368 | C | cuándo dejar de iterar: tras 5 o más re-rolls sin mejora, el prompt está bien y el modelo no puede: es la misma salida de diagnóstico que falta en a/b/c (`04_preguntas_eric.md`) |

## skills/visual-prompt-forge/references/prompt-anatomy.md

| Ids | Veredicto | Motivo |
|---|---|---|
| 012369–012399, 012407–012425 | N1 | las cinco capas del forge (pipeline de `shots.json`) |
| 012400–012406 | N3 | capa de texto superpuesto (`01_texto_en_imagen.md` §1) |

## Adenda: los 40 textos que entran (`v3/universo/adenda/adenda_universo.jsonl`)

| Ids | Veredicto | Motivo |
|---|---|---|
| ADD-0004 | N3 | arquitectura por secciones y salida con References y Notes fuera del cuerpo: §2 y tarea 10 del plan |
| ADD-0006, ADD-0007 | N3 | plantilla T1 y cara irregular: tarea 3 (campos de `armar.py`) |
| ADD-0008 | N3 | unas 250 palabras; slot de 300 o más: §2 (decisión 26 §11) |
| ADD-0010, ADD-0011 | N3 | Notes obligatorio; metadatos fuera del cuerpo: §2 y tarea 9 |
| ADD-0014 | N1 | 15 columnas de `audit_gi2.py` (no está en el repo): la tarea 4 marca cada columna como regla |
| ADD-0018–ADD-0028 | N1 | reglas R1 a R11 de SW30: la tarea 4 las marca por caso |
| ADD-0029, ADD-0030 | N3 | R12 y R13: tarea 12 |
| ADD-0031 | N3 | R14, zoom al 100 % de rostros y manos: tarea 11 |
| ADD-0038–ADD-0041, ADD-0044–ADD-0046, ADD-0048–ADD-0051 | N1 | reglas aprendidas: conservación de candados, cambio mínimo, pose literal, aislamiento del rol de cada referencia, sin amplificar cantidades, oclusión física bajo el agua, geometría de cámara, edición quirúrgica, ruta Nano Banana para clavados (excluida por 23 §6), composición abstraída sin adjuntar la imagen, sin arrastre de atributos entre tareas |
| ADD-0042, ADD-0043 | N3 | parámetro de ratio si la plataforma lo expone y QA de ratio con 1 %: §2 y tarea 11 |
| ADD-0047 | N3 | QA antes de declarar éxito: §2 y tarea 11 |
| ADD-0052–ADD-0055 | N3 | brief congelado por sha256, campos resueltos antes de compilar, delta autorizado, AST inmutable: tareas 3, 7 y 9 |
| ADD-0092 | N1 | la nacionalidad no se expande a rasgos estereotipados: la tarea 4 la marca para los casos con persona |
