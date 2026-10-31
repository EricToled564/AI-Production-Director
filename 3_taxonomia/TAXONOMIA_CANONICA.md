# Taxonomía canónica de clasificación para imágenes

Vale igual para cualquier modelo. La clasificación se hace modelo por modelo (hoy GPT Image 2) con el valor de F29 de cada texto.
Armada solo con: (1) la clasificación que Eric definió al empezar esta etapa; (2) los nombres de los documentos del corpus y sus encabezados, asignados a las categorías de la taxonomía; (3) el catálogo de casos de uso, en su orden de general a específico; (4) las categorías de la taxonomía anterior, tal cual, más las extensiones que Eric aprobó el 23 y el 26 de octubre y los valores que faltaban, aprobados el 31 de octubre. Los 1,369 términos del tesauro no se copian: no son categorías (la taxonomía anterior los define como etiquetas que cuelgan de las categorías).

## Nivel 1 · Qué hace el texto con el prompt

Todas las categorías se definen por su efecto en el prompt.

### 1.1 ¿Impacta la redacción?

| Valor | Definición |
|---|---|
| Impacta | El texto dice qué se escribe, o qué no se escribe, en el prompt |
| No impacta | El prompt queda igual con o sin el texto; se clasifica solo por lo que es (1.4) |

### 1.2 Si impacta: efecto

Qué le hace el texto al prompt. Un texto puede tener varios efectos; se marcan todos.

| Valor | Definición | Incluye | No incluye |
|---|---|---|---|
| Agrega contenido | Pide que se escriba algo de la imagen: sujeto, acción, escena, detalles, estilo visual, luz, color, materiales, texto que debe aparecer, términos de calidad | Las frases que describen la imagen, incluido su estilo visual | Cómo se redacta el prompt (eso es «fija la forma») |
| Fija la forma | Fija cómo se redacta el prompt: apartados, formato, etiquetas, sintaxis, longitud, estilo de redacción, cómo se nombran las referencias adjuntas | La estructura y la manera de escribir | El estilo visual de la imagen (eso es «agrega contenido») |
| Establece un orden | Fija en qué orden van los bloques o los elementos del prompt | Orden de apartados y de elementos | — |
| Fija restricciones | Excluye palabras o elementos, o fija lo que no debe cambiar | Prohibiciones, exclusiones, prompt negativo, lo que se preserva en una edición | — |
| Fija un parámetro | Fija un valor técnico de la generación fuera de la descripción | Modelo, calidad, tamaño, ratio, fondo transparente, formato de salida | Lo que se describe dentro del prompt |
| Da un ejemplo o una plantilla | Da una frase, un prompt o una plantilla con huecos que sirve de modelo | Ejemplos, plantillas, opciones de redacción | — |

### 1.3 Si impacta: cómo entra al prompt

Decide el destino de la regla. Solo lo que necesita interpretación pasa por selección.

| Valor | Cuándo | Destino | Uso operativo |
|---|---|---|---|
| Template | No depende de ningún dato del caso, o depende solo del modelo o de la operación. Si su forma cambia según el modelo, cada template la lleva en la forma de su modelo | Instrucción de llenado en el template de cada modelo, o en el de ese modelo u operación. Se usa una vez y no se vuelve a seleccionar. El template guarda la instrucción, no copia texto a cada prompt, para que el prompt siga siendo corto | INCORPORADA A TEMPLATE |
| Inserción mecánica | Su condición se resuelve con datos de lista cerrada del caso (tipo de pieza, sujeto, operación de edición, técnica, texto en la imagen, etc.), uno o varios | Se inserta en el prompt sin selección en cuanto el caso fija esos datos | INSERCIÓN MECÁNICA |
| Biblioteca de plantillas | Es la plantilla de un look concreto | Se ofrece por tipo de pieza y estilo; el usuario confirma como máximo una y se inserta | BIBLIOTECA DE PLANTILLAS |
| Selección | Su condición depende de un valor abierto (número, edad, posición, texto literal) o necesita interpretar el caso | Se selecciona caso por caso | ACTIVO EN SELECCIÓN |

### 1.4 Si no impacta: qué es

| Valor | Definición |
|---|---|
| Rótulo o encabezado | Título, subtítulo o rótulo que solo nombra lo que sigue |
| Descripción o explicación | Dice qué es o qué hace la skill, el documento o un método, sin decir qué escribir |
| Condición de uso de una plantilla | Dice para qué casos sirve una plantilla; se usa para ofrecerla en la biblioteca, no para escribir |
| Control o validación | Revisión, gate o comprobación que se hace después de escribir |
| Código o herramienta | Código, script, esquema o instrucción de una herramienta |
| Dato técnico de interfaz | Endpoint, API o forma de llamar al generador |
| Nota interna o de origen | Comentario, remisión interna o procedencia del texto |
| Licencia o crédito | Texto legal, autoría o atribución |

## Nivel 2 · Dónde buscar: secciones del corpus por categoría

Cada encabezado de primer nivel del corpus (809, sin contar copias idénticas) está asignado a las categorías de la taxonomía que su nombre señala, y por ellas a una sola sección. Es la primera precatalogación. La asignación encabezado por encabezado está en `3_taxonomia/precatalogacion_por_encabezado.csv`; aquí solo están las secciones.

| Sección | Qué agrupa | Destino habitual (1.3) | Encabezados | Textos |
|---|---|---|---|---|
| 2.1 Reglas generales de redacción | Encabezados que solo señalan qué regula la regla (F30), sin modelo, operación, tipo de pieza ni otro dato del caso | Template de todos los modelos | 58 | 713 |
| 2.2 Por modelo | Encabezados de un modelo concreto (F29) | Template del modelo | 175 | 1,195 |
| 2.3 Por operación | Encabezados de una operación o de su contexto: F10, F11, F23, F35 | Template de la operación o inserción mecánica | 51 | 346 |
| 2.4 Por tipo de pieza | Encabezados de un tipo de pieza, temática o formato: F04, F05, F06 | Inserción mecánica | 21 | 216 |
| 2.5 Biblioteca de looks | Plantillas de un look concreto, por tipo de pieza y temática | Biblioteca de plantillas | 49 | 421 |
| 2.6 Por contenido del cuadro y cámara | Encabezados de género, beats, montaje, función del plano, régimen físico, sujeto, estilo, técnica, plano, ángulo, movimiento, transición o audio: F07–F09, F12, F14, F15, F17, F18, F24–F28 | Inserción mecánica o selección | 31 | 422 |
| 2.7 Marca | Encabezados del brand lock (F01 «0 Brand Lock») | Inserción cuando el caso tiene marca | 46 | 316 |
| 2.8 Por etapa del pipeline y flujo | Encabezados de una etapa, un flujo, una ruta o un gate: F01, FLUJO, F03, F31 | Según la etapa; los de imagen son la etapa 5 | 172 | 2,629 |
| 2.9 Ejemplos | Ejemplos y prompts de muestra, por modelo | Efecto probable: da un ejemplo o una plantilla | 112 | 799 |
| 2.10 Probablemente no impacta | Código, esquemas, licencias, índices, notas internas y datos de interfaz | No impacta (1.4) | 82 | 5,887 |
| 2.11 Sin categoría | Encabezados cuyo nombre no señala ninguna categoría, ni su documento | Se decide al clasificar sus textos | 12 | 59 |

Desglose por categoría (número de encabezados):

- **2.1 Reglas generales de redacción:** estructura y sintaxis del prompt (20) · identidad y consistencia (12) · texto en pantalla (11) · composición (5) · orquestación y control de flujo (4) · luz (4) · parámetros técnicos (3) · color, grade y textura (2) · crítica y revisión (2) · encuadre y lente (1) · materialidad y superficie (1) · animación (1) · marca y logos (1)
- **2.2 Por modelo:** Seedance 2.5 (27) · GPT Image 2 (26) · Seedance 2.0 (24) · Nano Banana 2 (23) · Nano Banana Pro (23) · Kling 3.0 (22) · Veo 3.1 (20) · Ideogram (10) · Flux (9) · Seedream (9) · gpt-image-1.5 (8) · Hailuo (8) · Midjourney (8) · Todos los valores (2)
- **2.3 Por operación:** F10 edición de imagen existente (T5) (13) · F10 ancla con referencias (caso 2, T2 a T4) (10) · F10 boceto o wireframe a final (10) · F11 keyframe LF (9) · F11 keyframe FF (9) · F10 análisis de imagen a prompt (5) · F10 edición: cambiar luz o clima (2) · F10 edición: traducir texto (2) · F23 Todos los valores (2) · F10 edición: cambiar vestuario (1) · F10 composición de varias referencias (1) · F10 edición: colorizar (1) · F10 edición: añadir objeto (1) · F10 edición: quitar objeto (1) · F10 edición: restaurar (1) · F10 Todos los valores (1) · F23 estilo (1)
- **2.4 Por tipo de pieza:** F04 storyboard o multipanel (12) · F04 slide o presentación (8) · F04 concept art (1) · F04 identidad de marca (1)
- **2.5 Biblioteca de looks:** F04 storyboard o multipanel (9) · F04 póster o key art (9) · F05 moda (7) · F04 retrato (7) · F04 diseño de personaje (6) · F04 e-commerce o catálogo (6) · F04 editorial (6) · F05 comida y bebida (6) · F04 UI o mockup (2) · F04 post o historia para redes (2)
- **2.6 Por contenido del cuadro y cámara:** F07 carrera y velocidad (11) · F24 Todos los valores (2) · F26 Todos los valores (2) · F18 pixel art (1) · F08 Content Spiral (1) · F08 Custom (1) · F08 Educational Demo (1) · F08 Founder Explainer (1) · F08 Hero Trilogy (1) · F08 Pain-Reframe-Promise (1) · F25 Todos los valores (1) · F12 CTA o logo (1) · F12 hook (1) · F27 Todos los valores (1) · F28 Todos los valores (1) · F09 Todos los valores (1) · F07 Todos los valores (1) · F12 Todos los valores (1) · F18 fotorrealista (1)
- **2.7 Marca:** marca y logos (46) · color, grade y textura (6) · parámetros técnicos (3) · movimiento de cámara (3) · texto en pantalla (3) · orquestación y control de flujo (2) · trazabilidad y entrega (2)
- **2.8 Por etapa del pipeline y flujo:** 4 Shot planning (39) · 6 Video (36) · 3 Dirección cinematográfica (28) · 5 Imagen (26) · 2 Guion (21) · 7 Paquete y entrega (13) · ORQUESTACIÓN (9) · 1 Estrategia creativa (6) · FL03 Imágenes ancla (1) · FL01 Producción de spot publicitario (1) · F03 Clip (1) · F03 Video publicitario (1) · F31 sí, la aprueba el usuario (1) · F31 sí, la verifica una herramienta (1) · F31 sí, revisión manual obligatoria (1) · Post-producción (1)
- **2.9 Ejemplos:** Flux (4) · Nano Banana 2 (3) · Seedance 2.5 (2) · Seedance 2.0 (2) · GPT Image 2 (2) · Ideogram (2) · Kling 3.0 (2) · Midjourney (2) · Nano Banana Pro (2) · Seedream (2) · gpt-image-1.5 (1) · Hailuo (1) · Veo 3.1 (1)
- **2.10 Probablemente no impacta:** Código o herramienta (51) · Rótulo o encabezado (14) · Nota interna o de origen (8) · Dato técnico de interfaz (5) · Licencia o crédito (4)

Si un encabezado tiene varias categorías, va a la primera sección de este orden: no impacta, ejemplo, biblioteca, modelo, operación, tipo de pieza, contenido del cuadro, marca, etapa, reglas generales. En el archivo de datos conserva todas sus categorías.

## Nivel 3 · Caso de uso, de lo general a lo específico

El orden es el del catálogo de casos de uso (construcción del caso, de lo general a lo específico). Las categorías y sus valores son los de la taxonomía anterior, más los valores que el corpus usa y que faltaban; se dejan fuera solo los valores de las ramas de video. Ningún valor es un dato libre del caso: lo que el corpus traduce a hechos visibles entra como su traducción.


### 3.1 Qué se hace

#### FLUJO · Flujo

| Valor | Definición | Tipos |
|---|---|---|
| FL01 Producción de spot publicitario | Megaflujo E0–E7 y POST; E5 invoca FL02 y FL03; la ruta operativa vigente es Video publicitario | — |
| FL02 Génesis sin referencia | Subflujo atómico: solo texto en la entrada; salida activo ACCEPT canonizado con hash | — |
| FL03 Imágenes ancla | A0–A12: tarjeta de ancla, rutas por acción y sujetos, tratamiento, modelo, ensamblaje, lints, crítica, canonización, motion brief | — |
| FL04 Activo directo sin preproducción | Operaciones: imagen sin referencia; imagen con referencias, composición o edición; imagen ancla independiente; clip de video independiente | — |

#### F10 · Modo de generación

| Valor | Definición | Tipos |
|---|---|---|
| génesis sin referencias (caso 1, T1) | solo texto; fija la parte del sujeto que lleva la identidad | Fundamentación web [Web grounding] · Fundamentación con búsqueda de imágenes [Image-search grounding] |
| ancla con referencias (caso 2, T2 a T4) | texto más génesis aprobadas: cuerpo con rostro adjunto, cuadro de escena, keyframe | — |
| composición de varias referencias | une elementos de varias referencias sin ser cuadro de clip: producto en escena, póster | — |
| edición de imagen existente (T5) | cambia una zona de una imagen aprobada y conserva el resto | Edición con máscara · Edición conversacional |
| transferencia de estilo | aplica el estilo de una imagen de referencia a otro contenido | — |
| boceto o wireframe a final | un boceto, layout o plano controla la composición | — |
| edición: quitar objeto | subtipo de «edición de imagen existente (T5)» | — |
| edición: añadir objeto | subtipo de «edición de imagen existente (T5)» | — |
| edición: cambiar luz o clima | subtipo de «edición de imagen existente (T5)» | — |
| edición: colorizar | subtipo de «edición de imagen existente (T5)» | — |
| edición: restaurar | subtipo de «edición de imagen existente (T5)» | — |
| edición: traducir texto | subtipo de «edición de imagen existente (T5)» | — |
| edición: cambiar vestuario | subtipo de «edición de imagen existente (T5)» | — |
| edición: cambiar mobiliario u objeto | subtipo de «edición de imagen existente (T5)» | — |
| análisis de imagen a prompt | — | — |

Otros tipos de esta faceta, sin un valor padre: Generación desde texto · Generación condicionada por referencia · Conversión de técnica · Plano a visualización espacial · Adición de objeto · Eliminación de objeto · Sustitución de objeto · Recorte · Cambio de fondo · Reluminación · Cambio de estación · Cambio meteorológico · Colorización · Restauración · Retoque · Cambio de material · Localización lingüística · Adaptación cultural · Refinamiento iterativo · Preservación selectiva · Máscara de edición · Entrada textual · Entrada de imagen · Entrada multiimagen · Conversión 2D a 3D [2D-to-3D] · Conversión 3D a 2D técnico [3D-to-2D Technical] · Boceto a concepto tridimensional [Sketch-to-3D Concept] · Diseño plano a mockup de producto [Product 2D-to-3D] · Elevación a exterior arquitectónico [Elevation-to-Exterior] · Planta a interior arquitectónico [Floor-Plan-to-Interior] · Conversión estilística de meme [Meme Conversion] · Colorización fotográfica [Photo Colorization] · Colorización de manga [Manga Colorization] · Prueba virtual de vestuario [Virtual Try-On] · Sustitución de mobiliario [Interior Swap] · Relleno material físicamente coherente [Physics-Aware Fill].

#### F29 · Modelo

| Valor | Tipos |
|---|---|
| Nano Banana 2 | — |
| Nano Banana Pro | — |
| GPT Image 2 | — |
| Flux | — |
| Midjourney | — |
| Ideogram | — |
| Seedream | — |
| Nano Banana 2 Lite | — |
| gpt-image-1.5 | — |
| gpt-image-1 | — |
| gpt-image-1-mini | — |

#### F35 · Migración de versión de modelo

| Valor | Definición | Tipos |
|---|---|---|
| sí | las reglas de migración entre versiones de modelo | — |
| no | — | — |

#### F04 · Tipo de pieza

| Valor | Definición | Tipos |
|---|---|---|
| editorial | imagen con lenguaje de revista; se combina con la temática: editorial de moda, deportiva, musical, gastronómica | Lookbook |
| key visual de campaña | imagen principal de una campaña publicitaria | — |
| e-commerce o catálogo | producto para tienda o catálogo | Imagen de comercio electrónico · Imagen de catálogo |
| retrato | una o varias personas como sujeto de la pieza (retrato individual o de grupo) | Retrato grupal |
| póster o key art | pieza gráfica con título o composición de cartel | Póster |
| post o historia para redes | imagen para feed o historias | Post para redes · Historia para redes |
| miniatura | thumbnail de video con rostro y gancho | — |
| UI o mockup | pantallas, apps, maquetas de interfaz | Diseño de interfaz [UI] · Mockup · Captura de tienda de aplicaciones [App Store Screenshot] · Mockup de dashboard [Dashboard Design Mockup] |
| slide o presentación | una diapositiva: portada, datos, comparación, proceso | Diapositiva [slide] · Presentación · Diapositiva de título [Hero Title] · Diapositiva de datos [Data Visualization] · Diapositiva comparativa [Comparison] · Diapositiva de proceso [Process; Timeline] · Diapositiva de hallazgo o problema |
| storyboard o multipanel | varios paneles en una imagen | Storyboard · Composición multipanel · Tablero de análisis de color personal [Personal Color Analysis Board] · Hoja de sprites [Sprite Sheet] · Gráfico por teselas [Tile-Based Graphics] · Contenido para matriz LED [LED Display Content] |
| diseño de personaje | hoja o maestro de un personaje | Hoja de giro de personaje [Turnaround; Model Sheet] · Hoja de expresiones [Expression Sheet] · Retícula de vestuario [Outfit Variant Grid] · Figura chibi coleccionable [Chibi; Mini-Me Collectible] · Ficha de personaje [Character Card] |
| visualización arquitectónica | render de espacio, plano a 3D | — |
| identidad de marca | logo, sistema visual, aplicaciones | Tarjeta de presentación [Business Card] · Membrete [Letterhead] · Valla publicitaria [Billboard] · Empaque [Product Packaging] · Banner digital [Digital Banner] · Avatar social [Social Media Avatar] · Icono de aplicación [App Icon] · Señalética [Signage] · Artículo promocional [Merchandise] |
| scroll | Subtipo de pieza gráfica de la rama imagen denominado «scroll» en la fuente; sin inferir interfaz, marca, desplazamiento interactivo ni requisitos no expresos. | — |
| infografía o diagrama | — | — |
| concept art | — | — |
| pieza de portafolio | — | — |
| portada de álbum | portada cuadrada de un disco o un single | — |
| lámina artística | imagen para imprimir y colgar como obra | — |

Otros tipos de esta faceta, sin un valor padre: Pieza única · Esquema de interfaz [UI/UX Wireframe] · Tablero analítico [Dashboard] · Manual de ensamblaje sin palabras [IKEA Manual] · Infografía · Diagrama.

#### PUBLICACION · Lugar de publicación (subcategoría de F04)

| Valor | Definición | Tipos |
|---|---|---|
| TikTok → alcance de plataforma; ubicación sin restricción documental | Plataforma de video corto vertical. | — |
| Instagram → alcance de plataforma; ubicación sin restricción documental | Plataforma social con varias ubicaciones de publicación citadas en las fuentes (feed, Stories, carrusel, anuncio). | — |
| Instagram → Stories | Ubicación vertical a pantalla completa de Instagram. | — |
| Instagram → feed | Ubicación de publicaciones en el feed de Instagram. | — |
| Instagram → carrusel | Varias imágenes en una sola publicación de Instagram. | — |
| YouTube → alcance de plataforma; ubicación sin restricción documental | Plataforma de video con formato horizontal y ubicación Shorts. | — |
| YouTube → Shorts | Ubicación de video vertical corto dentro de YouTube. | — |
| Superficie literal Reels; sin condición de plataforma inferida | Ubicación de video vertical corto. Las fuentes la nombran sola («Reels») y como «TikTok Reel»; no establecen a qué plataforma pertenece. | — |
| Douyin → alcance de plataforma; ubicación sin restricción documental | Plataforma de video corto vertical citada junto a TikTok, Reels y Shorts. | — |
| Facebook → feed (alcance de la fuente citada) | Plataforma social citada para publicaciones cuadradas de feed. | — |
| LinkedIn → piezas sociales; carrusel en el ejemplo citado | Plataforma social profesional citada para piezas visuales y carruseles. | — |
| Sitio web → hero | Destino propio y sección de cabecera identificada literalmente como «website hero». | — |

#### F06 · Formato de salida

| Valor | Definición | Tipos |
|---|---|---|
| 16:9 | horizontal: TV, web, YouTube | — |
| 9:16 | vertical: Reels, TikTok, Shorts, historias | — |
| 1:1 | cuadrado: feed | — |
| 4:5 | vertical corto: feed de Instagram | — |
| 21:9 | cinemascope | — |
| 1:4 | vertical extremo; en Nano Banana, exclusivo de NB2 | — |
| 1:8 | vertical muy extremo; en Nano Banana, exclusivo de NB2 | — |
| 2:3 | vertical | — |
| 3:4 | vertical | — |
| 4:1 | horizontal extremo; en Nano Banana, exclusivo de NB2 | — |
| 8:1 | horizontal muy extremo; en Nano Banana, exclusivo de NB2 | — |
| 3:2 | — | — |

#### F34 · Resolución

| Valor | Definición | Tipos |
|---|---|---|
| 1K | — | — |
| 2K | — | — |
| 4K | — | — |

### 3.2 Contexto

#### F03 · Ruta operativa

| Valor | Definición | Tipos |
|---|---|---|
| Video publicitario | Flujo publicitario completo conforme a decisiones aprobadas; corresponde a FILM, sin reactivar reglas históricas excluidas. | — |
| Clip | Ruta con etapas elegidas; solo hereda lo aprobado para Clip. Etapas 1 y 2 si el usuario las mantiene. | — |

#### F05 · Temática o industria

| Valor | Definición | Tipos |
|---|---|---|
| deporte y fitness | atletas, clubes, competencia | — |
| automotriz y movilidad | autos, motos, bicis | — |
| música | artistas, conciertos, videoclips | Danza y coreografía |
| moda | prendas, modelos, pasarela | — |
| comida y bebida | producto comestible o bebida | — |
| arquitectura e inmobiliaria | espacios y edificios | — |
| belleza y cuidado personal | cosmética, piel, cabello | — |
| hospitalidad y viajes | hoteles, destinos | — |
| retail y supermercado | tiendas, anaquel, promociones | — |
| tecnología | apps, dispositivos, SaaS | — |
| salud y bienestar | clínicas, bienestar | — |
| educación | cursos, material didáctico | — |
| corporativo | B2B, institucional | — |
| finanzas y banca | — | — |
| sector público | — | — |
| estilo de vida | — | — |

#### F07 · Género narrativo

| Valor | Definición | Tipos |
|---|---|---|
| tragedia doméstica | drama íntimo en interiores, objetos cotidianos cargados | — |
| drama psicológico | tensión interna del personaje | — |
| acción | persecución, pelea, riesgo físico | — |
| carrera y velocidad | vehículo o atleta a velocidad | — |

#### F08 · Estructura de beats

| Valor | Definición | Tipos |
|---|---|---|
| Pain-Reframe-Promise | dolor, reencuadre, promesa | — |
| Hero Trilogy | héroe, obstáculo, transformación | — |
| Founder Explainer | quién, por qué, qué se construyó | — |
| Content Spiral | una idea que se profundiza en vueltas | — |
| Educational Demo | paso a paso de una tarea | — |
| Hook / Build / Payoff / CTA | default de TikTok | — |
| Problem / Solution / Proof / CTA | default de anuncio | — |
| Atmosphere → Climax | brand story: atmósfera, revelación lenta, clímax, logo | — |
| Custom | estructura propia declarada | — |

Otros tipos de esta faceta, sin un valor padre: Gancho–Producto–Acción [Hook–Product–CTA] · Gancho–Problema–Producto–Beneficio–Prueba social–Acción [Hook–Problem–Product–Benefit–Social proof–CTA] · Problema–Solución–Funcionamiento–Resultados–Acción [Problem–Solution–How it works–Results–CTA] · Tres actos [Three-act structure] · Ritual–Preparación–Lanzamiento–Contienda–Liberación [Ritual–Staging–Launch–Contest–Release] · Dolor [Pain; Problem state] · Reencuadre conceptual [Reframe] · Promesa [Promise] · Mundo inicial [World] · Agente de transformación [Hero, en Hero Trilogy] · Transformación narrativa [Transformation] · Prueba [Proof] · Prueba social [Social proof] · Afirmación general [Wide claim] · Profundización narrativa [Zoom 1; Zoom 2] · Retorno reinterpretado [Snap-back] · Aplicación guiada [Walk-through] · Resultado [Result] · Construcción narrativa [Build] · Contexto [Context] · Fisura [Crack] · Aceleración dramática [Acceleration] · Incidente detonante [Inciting incident] · Punto medio [Midpoint] · Crisis [Crisis point] · Insight narrativo.

#### F09 · Patrón de montaje

| Valor | Definición | Tipos |
|---|---|---|
| escalada | cada plano sube la tensión | Escalera rítmica [Rhythm ladder; rhythmic staircase] · Repetición con escalada [Escalating repetition] |
| ansiedad | presión creciente e inestable | — |
| descubrimiento | la información se revela por partes | — |
| catástrofe | construcción hacia un quiebre | Pausa preimpacto [Pre-impact pause] |
| drama comercial de producto | el producto resuelve la tensión | — |
| loop de videoclip | ciclo visual sobre el ritmo | Montaje sonoro [Sound-driven montage] · Corte a pulso [Beat-locked cut] |

Otros tipos de esta faceta, sin un valor padre: Plano–contraplano [Shot–reverse–shot] · Alternancia de energía [Visual momentum] · Variación de duración de escena [Scene length variation] · Montaje de preparación fragmentada [Hip-hop montage] · Micro-ráfaga de paneles [Micro-burst; fragment-cluster] · Panel sostenido [Held panel; hold] · Densidad de beats [Beat density] · Densidad de paneles [Panel density] · Ajuste de montaje por mirada [Eye-trace] · Montaje multiclips [Multi-clip assembly].

#### F12 · Función del plano

| Valor | Definición | Tipos |
|---|---|---|
| hook | detiene el scroll en el primer segundo | Gancho visual [Visual hook] · Gancho de pregunta [Question hook] · Gancho de acción [Action hook; inicio en pleno evento] · Gancho emocional [Emotion hook] |
| establecer | dónde estamos; plano abierto o master | — |
| revelar | entra información nueva al cuadro | — |
| poder | quién controla la escena; el staging lo dice | — |
| presión | la tensión crece; movimiento hacia la amenaza o la decisión | — |
| detalle | objeto, mano, ojo o textura en close-up o macro | — |
| reacción | consecuencia emocional en un rostro | — |
| giro interno | el cuerpo muestra el cambio antes de la decisión | — |
| impacto | el evento visual decisivo: la caída, el golpe, el quiebre | — |
| secuela | quietud después del impacto | — |
| salida | la imagen final que se lleva el espectador | Cierre circular [Circular ending] · Cierre revelador [Revelation ending] · Cierre resonante [Resonance ending] · Cierre interrogativo [Question ending] |
| CTA o logo | llamado a la acción o cierre de marca | — |

#### F11 · Rol del ancla

| Valor | Definición | Tipos |
|---|---|---|
| character ref | maestro de identidad de un personaje | — |
| environment ref | placa del lugar, vacía | — |
| keyframe FF | primer frame del clip | — |
| keyframe LF | último frame del clip | — |
| hero/macro | producto u objeto en detalle | Inserto protagonista [hero] |
| motif insert | objeto ancla que reaparece entre clips | — |

#### F23 · Referencias adjuntas

| Valor | Definición | Tipos |
|---|---|---|
| ninguna | sin referencias | — |
| persona | rostro o cuerpo de un personaje | Referencia de apariencia [Appearance reference] |
| vestuario | ropa o accesorios | — |
| lugar | escenario o locación | — |
| producto o prop | producto u objeto | — |
| estilo | referencia de look, color o textura | Referencia de material [Material reference] |
| estructura o composición | forma, geometría o disposición espacial del cuadro | — |
| movimiento | acción o trayectoria de un sujeto | — |
| cámara | movimiento o posición de cámara | — |
| ritmo | cadencia de la pieza | — |
| voz | voz de un personaje | — |
| diálogo | diálogo de un personaje | — |
| ambiente | sonido ambiente del entorno | — |
| música | música de la escena | — |

Otros tipos de esta faceta, sin un valor padre: Referencia de estilo · Identidad · Material · Composición · Pose · Estructura · Previsualización volumétrica simple [Coarse blockout; white-model blockout] · Previsualización animada detallada [Fine blockout] · Referencia de estructura [Structure reference] · Maestro único de edición [Sole editing master] · Referencia de reemplazo [Target material].

### 3.3 Qué hay en el cuadro

#### F15 · Sujeto

| Valor | Definición | Tipos |
|---|---|---|
| persona | ser humano; identidad fijada con rostro T1 y cuerpo T2 | — |
| lugar genérico | sitio sin identidad real: una calle, una cocina | Lugar |
| edificación o landmark | lugar real y reconocible | Edificación |
| animal | especie animal | — |
| producto | empaque, comida, bebida, cosmético o dispositivo, genérico o de marca real; la referencia aprobada se exige solo si lleva logo o etiqueta real | Producto de marca real · Producto genérico |
| objeto o prop | herramienta, vehículo, mobiliario, objeto ancla | Objeto · Vehículo [05 vehículo] · Objeto ancla |
| planta o especie vegetal | Vegetal o especie vegetal cuando es el sujeto regulado. No se asimila a animal, lugar o producto. | — |

#### F19 · Número de sujetos

| Valor | Definición | Tipos |
|---|---|---|
| 0 | placa: cero sujetos individuales; puede contener una multitud anónima, que no cuenta como sujetos | — |
| 1 | un sujeto individual, con o sin placa de multitud | — |
| 2 | dos sujetos individuales, con o sin contacto físico | — |
| 3 o más | tres o más sujetos individuales con identidad: grupo ensamble de 3 a 8 identidades reconocibles; la multitud anónima no cuenta como sujetos y se conserva como placa o capa anónima separada | — |

#### F20 · Identidad de las personas y animales

Las facetas F20, F21 y F22 valen igual para personas y para animales.

| Valor | Definición | Tipos |
|---|---|---|
| todas | grupo ensamble: cada miembro reconocible y consistente | — |
| solo los héroes | hasta 3 reconocibles, el resto anónimo | — |
| ninguna | multitud anónima: nadie con rostro legible | — |

#### F21 · Contacto físico entre personas o animales

| Valor | Definición | Tipos |
|---|---|---|
| sí | abrazo, tackle, manos que se tocan | — |
| no | no hay contacto | — |

#### F13 · Tipo de acción

| Valor | Definición | Tipos |
|---|---|---|
| A pose sostenida | quietud; el sujeto no cambia de estado | — |
| B instante pico | un instante de máxima fuerza, congelado | — |
| C movimiento continuo | desplazamiento sostenido | — |
| D fenómeno de luz o clima | el evento es la luz o el clima | Fenómeno luminoso · Fenómeno meteorológico |
| E interacción o diálogo | dos o más personas se relacionan o hablan | Diálogo |
| F multitud | la masa hace el trabajo | — |
| G acuática en superficie | el sujeto se desplaza sobre el agua | — |
| H subacuática | cámara y sujeto sumergidos | — |

#### F14 · Régimen físico

| Valor | Definición | Tipos |
|---|---|---|
| 01 agua en superficie | wakeboarding, surf, jet ski, remo, esquí acuático | — |
| 02 ruptura de superficie | clavado, nadador emergiendo, salto de ballena, split-level | Encuadre de interfaz [split-level] |
| 03 subacuático | buceador en cenote, nadador bajo el agua, apnea | — |
| 04 objeto balístico | pelota, balón, gota, flecha, chispa | — |
| 05 vehículo | auto de carreras, moto, bici, tren, dron | — |
| 06 cuerpo en esfuerzo | corredor en la cinta, salto, golpe, levantamiento | — |
| 07 luz y clima | rayo, amanecer, lluvia, polvo, niebla, nieve | — |
| 08 multitud anónima | estadio, manifestación, calle llena, público | — |
| 09 grupo ensamble | quinteto, grupo de K-pop, equipo, familia | — |

#### F16 · Espacio

| Valor | Definición | Tipos |
|---|---|---|
| interior | bajo techo | Estudio · Cocina · Oficina · Hogar · Tienda |
| exterior | al aire libre, incluida el agua abierta | Calle o ciudad · Azotea |

#### F32 · Texto en la imagen

| Valor | Definición | Tipos |
|---|---|---|
| sin texto | — | — |
| texto corto | — | — |
| texto extenso o pequeño | — | — |

#### F33 · Complejidad de escena

| Valor | Definición | Tipos |
|---|---|---|
| simple | — | — |
| compleja | 5 o más elementos | — |

#### F37 · Grado de dificultad

Fija la calidad de generación. En GPT Image 2 la calidad máxima es high; xhigh existe solo en modelos que la admiten.

| Valor | Definición | Tipos |
|---|---|---|
| estándar | imagen sin las exigencias de «muy sofisticada» | — |
| muy sofisticada | escena compleja (F33), o bloque «Acción» activo, o texto extenso o pequeño (F32), o tres o más sujetos con identidad (F19) | — |

### 3.4 Cómo se ve

#### F17 · Estilo visual

| Valor | Definición | Tipos |
|---|---|---|
| documental | luz dura, piel real, grano de reportaje | — |
| narrativo cinematográfico | una fuente domina, 70% en sombra | — |
| comercial pulido | luz limpia, producto legible | — |
| editorial | contraste alto y desaturado, pose y styling de revista | — |
| retro o vintage | película de otra época: "1980s color film", tonos análogos, negros levantados | — |
| blanco y negro | grano clásico tipo Ilford HP5 | — |
| minimalista | manda el espacio negativo | Futurista/SaaS [Futuristic; SaaS Style] |
| race/kinetic | velocidad, paleta fría | — |
| UGC/social | celular, luz natural | — |
| experimental | cross-processing, colores desplazados | — |
| anclado en época, cultura o autor | — | — |
| brutalista | — | — |
| futurista | — | — |

Otros tipos de esta faceta, sin un valor padre: Diseño brutalista [Brutalist] · Glassmorfismo [Glassmorphism] · Surrealismo inflable [Inflatable Surrealism] · Cuaderno científico renacentista [Da Vinci Notebook] · Ciberpunk de neón [Cyberpunk; Neon] · Lámina científica vintage [Vintage Science Poster] · Arte pop [Pop Art] · Memphis corporativo [Corporate Memphis; Flat Art].

#### F36 · Ánimo de la imagen

El ánimo no se escribe en el prompt: cada valor se define por los valores de la taxonomía en que se traduce, y esos son
los que entran al prompt y los que llevan las reglas.

| Valor | Traducción |
|---|---|
| dramática | Fuente única dominante · Luz dura · Luz lateral · Contraste alto · Claroscuro; ángulo contrapicado |
| sombría | Clave baja · Luz lateral · humo o bruma · Paleta restringida · fondo oscuro degradado |
| lujo o premium | Según el tipo de pieza. Producto: estudio oscuro, una sola Luz principal, Reflexión en la superficie, Condensación, Luz volumétrica, Paleta restringida, fondo oscuro degradado, Sombra de contacto. Slide: Glassmorfismo y Luz volumétrica. Diseño gráfico: fondo liso, sans-serif pesada, un objeto héroe, Espacio negativo |
| nostálgica | Cámara desechable · película de los años 80 · Grano fotoquímico · Negativo envejecido · Negros levantados · Desaturación · Sobreexposición; estilo retro o vintage |
| calma | Luz suave de Ventana · Luz lateral · hora dorada · Espacio negativo · Profundidad de campo reducida · Altas luces cálidas con Sombras frías |

«Elegante» se traduce a Familia tipográfica: serif o script.

#### F18 · Técnica de representación

| Valor | Definición | Tipos |
|---|---|---|
| fotorrealista | debe parecer foto o filmación real | — |
| ilustración | stickers, íconos, arte dibujado | Ilustración naturalista [Naturalist Illustration] · Aguafuerte coloreado [Hand-Colored Etching] · Grabado en madera [Woodblock Print] · Cromolitografía [Chromolithograph] |
| render 3D | objeto o espacio modelado | Render estilizado [Stylized Render] |
| animación 2D | dibujo animado | — |
| animación 3D | personajes o mundos 3D animados | — |
| motion graphics | gráfico y tipografía en movimiento | — |
| pixel art | imagen por píxeles | — |

Otros tipos de esta faceta, sin un valor padre: Recorte de papel [Paper Cutout] · Plastilina animada [Claymation; Plasticine] · Vector kawaii [Kawaii; Cute Vector] · Acuarela de cuento [Storybook Watercolor] · Arte de pizarra [Chalkboard Art] · Pixel art de ocho bits [8-Bit] · Representación isométrica tridimensional [Isometric 3D] · Plano azul o esquema técnico [Blueprint; Schematic] · Novela gráfica o cómic [Graphic Novel; Comic Book] · Plegado de papel [Origami; Paper Folding] · Acabado de boceto [Sketch Quality] · Acabado de presentación [Presentation Quality] · Stop-motion.

### 3.5 Cámara

#### F24 · Tamaño de plano

| Valor | Definición | Tipos |
|---|---|---|
| EWS extreme wide | sujeto pequeño en el entorno | — |
| WS wide | cuerpo entero con entorno | — |
| MLS medium wide | cuerpo entero, poco entorno | MLS medium long shot · Medium wide |
| MS medium | de la cintura para arriba | — |
| MCU medium close-up | cabeza y hombros | — |
| CU close-up | cabeza, o mano con objeto | Choker close-up |
| ECU extreme close-up | ojos, manos, un detalle | — |
| macro insert | detalle a escala macro | — |
| objeto entero | un objeto completo como sujeto del cuadro | — |

Otros tipos de esta faceta, sin un valor padre: Insert shot.

#### F25 · Ángulo

| Valor | Definición | Tipos |
|---|---|---|
| eye-level | a la altura de los ojos; paridad | — |
| low | desde abajo; dominio o fuerza | Altura baja |
| high | desde arriba; vulnerabilidad | Altura alta |
| top-down u overhead | cenital; esquema, geometría | Vista aérea [bird’s-eye] |
| dutch | cámara inclinada; un beat de inestabilidad | — |
| worm's eye | desde el suelo | — |
| POV | lo que ve el personaje | Punto de vista externo · Cámara objetiva [Objective Camera] · Cámara subjetiva [Subjective Camera] |
| over-the-shoulder | sobre el hombro de otro personaje | — |
| perfil | el sujeto de lado | — |

Otros tipos de esta faceta, sin un valor padre: Vista frontal · Vista posterior · Vista de tres cuartos.

#### F22 · Tamaño del rostro (persona o animal)

| Valor | Definición | Tipos |
|---|---|---|
| ≥20% | el rostro manda; la identidad se verifica al zoom | — |
| <20% | rostro pequeño en el cuadro | — |
| sin rostro visible | silueta, casco, espalda | — |

#### F26 · Movimiento de cámara

| Valor | Definición | Tipos |
|---|---|---|
| estática o locked-off | sin movimiento | — |
| push-in (lento o rápido) | la cámara avanza hacia el sujeto | — |
| pull-back | la cámara se aleja | — |
| dolly in / dolly out | avance o retroceso sobre riel | — |
| tracking o lateral | acompaña al sujeto en paralelo | — |
| pan | giro horizontal | — |
| tilt | giro vertical | — |
| handheld | temblor orgánico de cámara en mano | — |
| orbit | rodea al sujeto | — |
| gimbal glide | deslizamiento estabilizado | — |
| crane | grúa que sube o baja | — |
| aéreo o dron | desde el aire | — |
| FPV | vuelo de dron en primera persona | — |
| whip pan | paneo rápido como transición | — |
| snap zoom | zoom brusco | — |
| rack focus | el foco cambia de plano | — |
| dolly zoom | efecto Hitchcock | — |
| dive | la cámara se desploma hacia abajo | — |
| one-take | plano secuencia | — |
| bullet time | tiempo congelado con cámara girando | Congelado de fotograma [Freeze frame] |
| speed ramp | acelera, frena, acelera | Cámara lenta [Slow motion; ultra-slow motion] · Aceleración de reproducción [Speed-up] · Expansión temporal [Time expansion] |

Otros tipos de esta faceta, sin un valor padre: Zoom · Rampa de velocidad [speed ramp].

#### F27 · Transición

| Valor | Definición | Tipos |
|---|---|---|
| corte natural | punto de edición simple | Corte de choque [Smash cut] · Corte en reposo |
| fade in / fade out | desde o hacia negro | Aparición desde negro [Fade-in] · Desaparición a negro [Fade-out] |
| disolvencia | fundido cruzado de 1 a 2 s | — |
| flash blanco o negro | un cuadro de golpe como puntuación | Destello blanco [White flash] · Destello negro [Black flash] |
| wipe | el cuadro nuevo empuja al anterior | — |
| occlusion mask | un objeto tapa la lente y revela la escena nueva | — |
| match cut | una forma o movimiento parecido une dos escenas | Emparejamiento gráfico [Graphic match] · Emparejamiento de movimiento [Motion match] |
| action cut o whip | el corte se esconde en un movimiento rápido | Corte sobre acción [Cut on action; action cut] · Corte oculto por paneo [Whip-pan cut] |
| motion relay | el sujeto sale del cuadro A y sigue en el B | — |
| zoom-through | la cámara atraviesa una pupila, cerradura o ventana | — |
| ink-wash dissolve | sangrado estilizado, animación | — |

Otros tipos de esta faceta, sin un valor padre: Fundido de entrada [fade in] · Fundido de salida [fade out] · Destello blanco · Destello negro · Preentrada sonora [J-cut] · Prolongación sonora [L-cut] · Transición condicionada por disparador [Triggered transition; order-gated transition].

#### F28 · Audio

| Valor | Definición | Tipos |
|---|---|---|
| diálogo | personajes hablando en cuadro | — |
| voz en off | narración fuera de cuadro | — |
| SFX de ambiente | room tone, ciudad, lluvia, viento | — |
| SFX de cuerpo y acción | respiración, pasos, tela, puerta | — |
| SFX de evento dramático | silencio súbito, golpe grave, vidrio que se rompe | — |
| música | pista musical | — |
| silencio | ausencia deliberada de sonido | — |

Otros tipos de esta faceta, sin un valor padre: Sonido diegético [Diegetic sound] · Tono de recinto [Room tone] · Señal sonora puntual [Sound cue].

### 3.6 Detalles del caso por materia: tipos

Los términos de la taxonomía anterior, agrupados en tipos dentro de su materia: con ellos se describe el detalle del caso (tipo de cámara, tipo de película, óptica, momento y dirección de la luz, etc.). No incluye los términos sin presencia en el corpus.

#### encuadre y lente

| Tipo | Valores |
|---|---|
| Tipo de óptica | Gran angular [wide angle] · Óptica normal · Teleobjetivo · Óptica macro · Óptica anamórfica · Distancia focal |
| Efecto óptico | Perspectiva de proximidad · Compresión aparente · Distorsión de barril · Distorsión de perspectiva · Inclinación y descentramiento [tilt-shift] · Bloom · Destello de lente [flare] · Destello anamórfico · Aberración cromática · Viñeteado |
| Enfoque y profundidad de campo | Profundidad de campo reducida [shallow DOF] · Foco profundo [deep focus] · Plano de enfoque · Desenfoque de fondo · Foco dividido [split diopter] · Bokeh · Cambio de foco [rack focus] |
| Tipo de cámara | Cámara de acción · Cámara de teléfono · Formato medio · Cámara instantánea · Cámara desechable · Cámara fotográfica digital |
| Soporte y montaje de cámara | Cámara fija en soporte [hard mount] · Montaje de capó · Montaje de parachoques · Montaje de eje · Cámara de cabina · Cámara corporal [body mount] · Grúa · Estabilizador · Dron |
| Filtro óptico | Filtro difusor óptico [Diffusion Filter] · Filtro polarizador [Polarizer] · Pro-Mist · Black Pro-Mist · Fog · Double Fog · Low Contrast |
| Vista técnica | Vista en planta [Plan View] · Vista en alzado [Elevation] · Vista en sección [Section] |
| Reencuadre | Reencuadre |

#### color, grade y textura

| Tipo | Valores |
|---|---|
| Tipo de película | Emulación fotoquímica · Kodak Portra 400 · Fuji Velvia · Ilford HP5 · Cinestill 800T · Negativo envejecido [Expired Negative Film] |
| Textura de captura | Ruido de captura · Grano fotoquímico · Halación |
| Exposición y rango tonal | Altas luces recortadas · Negros empastados · Rango dinámico · Negros levantados · Curvas tonales [Curves] |
| Temperatura y balance de color | Temperatura de color · Balance de blancos · Dominante cromática · Tinte verde–magenta [Tint] · Absorción cromática subacuática |
| Paleta | Paleta monocromática · Paleta complementaria · Paleta restringida · Acento cromático · Color de marca · Color excluido · Contrastes de Itten [Itten's Seven Contrasts] |
| Tratamiento de color | Tono cromático · Saturación · Sombras frías · Altas luces cálidas · Desaturación · Procesado cruzado [cross-processing] · Blanco y negro · Corrección de color · Etalonaje [color grade] · Igualación de planos [shot matching] · Glitch digital [Digital Glitch] · Omisión del blanqueo [Bleach Bypass] |
| Color en pintura | Color local [Local Color] · Color modificado por iluminación [Valeurs] · Silueta de umbral [Threshold Silhouette] |

#### luz

| Tipo | Valores |
|---|---|
| Exposición | Subexposición · Sobreexposición |
| Momento del día | Amanecer · Mañana · Mediodía · Tarde · Hora dorada · Atardecer · Hora azul · Noche |
| Luz natural y ambiente | Luz solar directa · Cielo cubierto · Luz lunar · Ventana · Luz ambiente continua |
| Fuente práctica o artificial | Lámpara práctica · LED de techo · Fluorescente · Neón · Pantalla de teléfono · Monitor · Refrigerador · Faro de vehículo · Farola · Vapor de sodio · Vela · Hoguera · Foco escénico · Luz de emergencia · Estrobo · Luz de baño [Wash light] |
| Equipo de iluminación | Softbox · Anillo luminoso [ring light] · Rebote [bounce] · Luz de modelado [Modeling Light] · Máscara de sombra [Gobo] |
| Esquema de iluminación | Luz principal [key light] · Luz de relleno [fill light] · Iluminación motivada · Esquema de tres puntos · Fuente única dominante · Iluminación Rembrandt [Rembrandt Lighting] |
| Dirección de la luz | Contraluz [backlight] · Luz de contorno [rim light] · Luz frontal · Luz lateral · Luz cenital [top light] · Luz inferior [underlight] |
| Calidad y contraste | Difusión · Luz dura · Luz suave · Contraste alto · Contraste bajo · Relación de iluminación · Clave baja [low-key] · Clave alta [high-key] · Claroscuro [Chiaroscuro] · Contraste óptico-visual [OVK; Optical and Visual Contrast] |
| Patrón y efecto de luz | Luz filtrada por persianas · Luz moteada · Silueta · Brillo especular · Luz volumétrica · Vapor a contraluz · Reflejo húmedo · Parpadeo · Derrame luminoso [spill] · Reflexión cromática de entorno [Color Reflex] |

Momento del día: Amanecer equivale a DAWN, Mañana, Mediodía y Tarde a DAY, Atardecer a DUSK y Noche a NIGHT en la Circunstancia temporal de escena del guion.

#### composición

| Tipo | Valores |
|---|---|
| Regla y equilibrio | Centro compositivo · Simetría · Asimetría · Regla de tercios · Eje compositivo [spine] · Equilibrio visual · Peso visual [Visual Weight] · Centro de gravedad compositivo [Center of Gravity] |
| Recorrido de la mirada | Líneas de fuga · Líneas guía · Encuadre interno · Punto focal · Jerarquía visual |
| Espacio y márgenes | Espacio de desplazamiento · Aire superior [headroom] · Zona segura · Espacio negativo |
| Profundidad y capas | Oclusión · Primer término [foreground] · Plano medio espacial [midground] · Fondo [background] · Separación de planos · Superposición · Función de capa de profundidad [Depth-layer job] · Relación figura–fondo [Figure and Ground] · Perspectiva aérea o tonal [Aerial Perspective; Tonal Perspective] · Compresión espacial expresiva [Claustrophobic Compression] · Fondo opaco |
| Tipo de fondo | Fondo liso (blanco u otro color sólido) · Fondo degradado · Fondo de estudio |
| Escala y densidad | Escala relativa · Densidad visual · Diorama en miniatura [Miniature Diorama] |
| Sujetos en cuadro | Plano de dos sujetos [Two-Shot] · Plano de tres sujetos [Three-Shot] |
| Diagrama e infografía | Mapa de transporte [Subway Map; Transit Map] · Ordenación cenital ortogonal [Knolling] · Cronología horizontal [Horizontal Timeline] · Flujo paso a paso [Step-by-Step Flow] · Hoja de ruta sinuosa [Winding Roadmap] · Comparación en pantalla dividida [Split Screen; Versus] · Matriz comparativa [Comparison Matrix] · Antes y después [Before and After] · Diagrama de Venn [Venn Diagram] · Pirámide [Pyramid] · Embudo [Funnel] · Iceberg [Iceberg] · Núcleo y radios [Hub and Spoke] · Árbol ramificado [Tree; Branching Map] · Círculos concéntricos [Concentric Circles] · Retícula bento [Bento Grid] · Retícula de tabla periódica [Periodic Table Grid] · Rompecabezas [Jigsaw] · Mapa isométrico [Isometric Map] · Corte transversal [Cross-Section; Cutaway] · Llamada anatómica [Anatomical Call-out] · Vista explosionada [Exploded View] |
| Retícula y multipanel | Retícula · Tira de viñetas [Comic Strip] · Storyboard de nueve celdas [9-Cell Grid Storyboard; 9-Panel TVC Grid] · Cuadrícula editorial 2×2 [2x2 Editorial Portrait Grid] · Tríptico de campaña [3-Panel Campaign Collage] · Mosaico 4×3 sin bordes [4x3 Borderless Grid] · Secuencia cinematográfica de seis cuadros [6-Frame Cinematic Sequence] · Póster storyboard de doce paneles [12-Panel Storyboard Poster] · Número de paneles [Panel Count] · Dimensiones de retícula [Grid Dimensions] · Orden de lectura [Reading Order] · Separación de paneles [Borders and Gaps] · Orientación de tríptico [Horizontal; Vertical] · Rotulación de panel [Panel Caption] · Retícula asimétrica [Asymmetric Grid] · División proporcional [Split-Screen Ratio] · Divisor nítido [Sharp Divider] · Divisor degradado [Gradient Divider] · Sin divisor [No Divider] |

#### física y movimiento congelado

| Tipo | Valores |
|---|---|
| Desenfoque y congelado | Desenfoque de movimiento [motion blur] · Movimiento congelado · Barrido de seguimiento [panning blur] · Larga exposición · Flash instantáneo · Desenfoque radial por zoom · Barrido direccional congelado [Directional motion-blur smear] · Desenfoque parcial congelado [Frozen partial blur] · Panel de estelas [Streak-frame; implied whip] · Separación nítido–borroso [Sharp-subject / blurred-field separation] · Quietud congelada [Freeze-frame stillness] · Microvibración mecánica [Mechanical-vibration cue; hard-mounted shake] |
| Fuerza y deformación | Gravedad · Inercia · Aceleración · Frenado · Fricción · Tracción · Tensión · Compresión · Deformación · Elasticidad |
| Impacto y cambio de estado | Impacto · Colisión · Umbral de estado |
| Señal de velocidad | Señal de velocidad · Vector de postura [Posture vector; trajectory vector] |
| Agua y líquido | Flotación · Salpicadura · Ruptura de superficie · Refracción subacuática · Visibilidad subacuática · Cáusticas · Burbujas ascendentes · Flotación de pelo y tejido · Spray direccional |
| Atmósfera y partículas | Estela · Partículas · Reverberación de calor |
| Clima | Niebla o bruma · Lluvia · Nieve · Polvo · Humo · Vapor |

#### anatomía, rostro y piel

| Tipo | Valores |
|---|---|
| Parte del cuerpo | Proporción corporal · Estructura esquelética · Articulación · Extremidad · Mano · Dedos · Pie · Rostro · Ojos · Boca · Piel · Cabello · Músculo y tendón |
| Postura, peso y contacto | Peso y equilibrio · Apoyo corporal · Contacto entre cuerpos · Contacto con objeto · Postura · Esfuerzo corporal · Interpretación instrumental · Lateralidad de ejecución |
| Expresión y gesto | Gesto · Microexpresión · Dirección de mirada · Respiración visible |
| Continuidad y tratamiento de piel | Continuidad anatómica · Suavizado de piel [Skin Softening] |

#### identidad y consistencia

| Tipo | Valores |
|---|---|
| Tipo de identidad | Identidad facial · Identidad corporal · Identidad de vestuario · Identidad de producto · Identidad de lugar · Identidad de personaje estilizado |
| Rasgo que se conserva o cambia | Rasgo invariante · Rasgo variable · Deriva de identidad · Exclusión de atributos de referencia [Reference exclusion] |
| Consistencia | Consistencia intraimagen · Consistencia interimagen · Identidad de instancia continua [Continuous instance] |
| Referencia de identidad | Maestro de identidad · Linaje de derivación · Preservación de identidad · Vinculación por sujeto [Per-subject binding] · Selección por escena [Per-scene reference selection] · Vinculación por estado e intervalo [State-time binding] · Perfil de sujeto [Subject Profile] · Propiedad de objetos [Prop ownership] |

#### materialidad y superficie

| Tipo | Valores |
|---|---|
| Tipo de material | Metal · Vidrio · Madera · Tejido · Plástico o vinilo · Piedra o mármol · Cuero · Cerámica |
| Acabado de superficie | Superficie mate · Superficie brillante · Superficie satinada · Iridiscente · Rugosidad · Textura visible · Microcontraste [Micro-Contrast] |
| Transparencia y reflexión | Opacidad · Translucidez · Transparencia · Refracción · Reflexión · Reflexión del entorno [Environmental Reflection] |
| Desgaste y envejecimiento | Pátina · Desgaste · Suciedad · Imperfección material |
| Humedad y líquido | Condensación · Menisco · Superficie mojada · Gotas adheridas · Sudor visible |
| Tejido | Trama textil · Caída de tejido [Fabric Drape] |
| Partículas y sombra de contacto | Partículas atmosféricas [Atmospheric Particles] · Sombra de contacto [Contact Shadow] |

#### texto en pantalla

| Tipo | Valores |
|---|---|
| Tipo de texto | Texto dentro de imagen · Texto compuesto en postproducción [Composited text; Mode 1] · Texto generado dentro de imagen [Text-in-image; Mode 2] · Texto literal [Exact Text] · Texto multilingüe [Multi-language] · Idioma de destino [Target Language] |
| Función del texto | Sustitución de voz en reproducción silenciada [Mute-autoplay text] · Compresión conceptual [Concept compression] · Dato o prueba textual [Stat / proof point] · Puntuación textual [Beat punctuation] · Persistencia entre planos [Persistent overlay] |
| Posición del texto | Posición central [center] · Tercio inferior [lower-third] · Tercio superior [upper-third] · Tercio izquierdo [left-third] · Tercio derecho [right-third] · Posición porcentual [x/y percentages] |
| Tamaño y jerarquía | Tamaño de exhibición [display] · Tamaño de titular [headline] · Tamaño de cuerpo [body] · Tamaño de nota [caption] · Jerarquía tipográfica |
| Familia tipográfica | Serif · Sans-serif · Script o cursiva · Versalitas |
| Peso tipográfico | Peso regular [regular] · Peso negrita [bold] · Peso negro [black] · Peso fino [thin] · Peso extranegrita [extra bold] · Peso medio [medium tipográfico] |
| Entrada, salida y lectura (video) | Entrada por aparición directa [hard-cut enter] · Salida por desaparición directa [hard-cut exit] · Entrada por fundido [fade-in enter] · Salida por fundido [fade-out exit] · Deslizamiento ascendente [slide-up] · Deslizamiento descendente [slide-down] · Revelado de escritura [type-on] · Tiempo de lectura [Read-time] |

#### marca y logos

| Tipo | Valores |
|---|---|
| Componente del brand lock | Paleta de marca · Tipografía de marca · Logotipo · Lista de exclusiones de marca [never list] · Bloqueo de marca [brand lock] · Nombre de marca · Descripción de una línea · Dirección de etalonaje · Lenguaje de movimiento · Sistema de marca |
| Voz y tono | Identidad verbal · Voz de marca · Tono de pieza · Regla de voz · Postura de voz · Segura [Confident] · Cálida [Warm] · Incisiva [Sharp] · Discreta [Quiet] · Lúdica [Playful] · Autorizada [Authoritative] |
| Arquetipo | Arquetipo · Sabio [Sage] · Cuidador [Caregiver] · Rebelde [Rebel] · Creador [Creator] · Bufón [Jester] · Gobernante [Ruler] · Persona común [Everyman] · Arquetipo Operador |
| Mood | Adjetivo de mood |
| Rol de color de marca | Tinta de marca [Ink] · Color atenuado [Muted] · Línea de marca [Rule] · Fondo de paleta de marca · Acento de paleta de marca |
| Rol tipográfico de marca | Cuerpo tipográfico [Body] · Monoespaciada [Mono] · Exhibición tipográfica de marca |

#### dramaturgia

| Tipo | Valores |
|---|---|
| Conflicto y tensión | Objetivo de personaje · Obstáculo · Conflicto · Riesgo narrativo [stakes] · Decisión · Cambio de estado · Revelación · Anticipación dramática · Clímax · Información retenida · Punto de giro · Contraste dramático · Consecuencia |
| Arco y beats | Preparación [setup] · Resolución [payoff] · Arco de pieza · Beat · Unidad de escena |
| Recurso de significado | Subtexto · Relación de poder · Causalidad visual · Motivo recurrente · Objeto dramático |
| Emoción | Emoción corporalizada · Emoción objetual |
| Función del plano en la historia | Avance de acción [Advance action] · Cambio emocional [Change emotion] · Aumento de presión [Increase pressure] · Revelación de personaje [Reveal character] · Construcción de mundo [Build world] |
| Rótulo de carrera | Compromiso irreversible [Commitment] · Error de ejecución [Mistake] · Recuperación de control [Recovery] · Evidencia de velocidad [Proof-of-speed] · Resultado competitivo [Race result] · Preparación de carrera [setup de carrera] |

#### puesta en escena y blocking

| Tipo | Valores |
|---|---|
| Posición y trayectoria | Blocking · Staging · Posición inicial · Posición final · Trayectoria · Orientación corporal · Cambio de nivel escénico [Level Change] |
| Dirección y eje | Eje de acción · Dirección de pantalla · Regla del eje [180-degree Rule] |
| Entrada, salida y estado | Entrada de cuadro · Salida de cuadro · Estado anterior · Estado posterior |

#### animación

| Tipo | Valores |
|---|---|
| Principio de animación | Compresión y estiramiento [squash and stretch] · Anticipación [anticipation] · Puesta en escena [staging] · Acción directa y pose a pose [straight ahead action and pose to pose] · Acción continuada y superpuesta [follow through and overlapping action] · Entradas y salidas lentas [slow in and slow out] · Arcos [arcs] · Acción secundaria [secondary action] · Timing · Exageración [exaggeration] · Dibujo sólido [solid drawing] · Atractivo expresivo [appeal] |

#### parámetros técnicos

| Tipo | Valores |
|---|---|
| Exposición de cámara | Apertura · Tiempo de exposición · Sensibilidad ISO · Frecuencia de fotogramas [fps] |
| Calidad | Nivel de calidad [quality] · Calidad baja [low] · Calidad media [medium] · Calidad alta [high] |
| Tamaño, proporción y resolución | Resolución admitida · Proporción admitida · Proporción de salida [--ar; aspect_ratio; aspectRatio] · Dimensiones de imagen [size] · Resolución de video [resolution; --resolution] · Formato 2.39:1 |
| Formato de archivo | Profundidad de color [Color bit depth; 10-bit] · Formato de archivo [output_format] · PNG · JPEG · WebP · Compresión de archivo |
| Control de generación | Semilla aleatoria [seed; --seed] · Intensidad de guía [guidance_scale; cfg_scale] · Iteraciones de muestreo [steps] · Peso de estilización [--s; stylize] · Diversidad de exploración [--c; chaos] · Tolerancia de seguridad [safety_tolerance] · Reescritura automática de prompt [prompt_upsampling; magic_prompt; prompt_optimizer] · Campo negativo dedicado [negative_prompt] · Intensidad de razonamiento [thinking_level] |
| Modelo y modo de estilo | Identificador de modelo [model] · Modo de estilo [style; --style; style_type] |
| Referencia y entrada | Límite de referencias · Peso de referencia de personaje [--cw] · Referencia de personaje parametrizada [--cref] · Referencia de estilo parametrizada [--sref] · Imagen de apertura [start_image; First Frame] · Imagen objetivo de cierre [tail_image; Last Frame] · Arreglo de referencias [referenceImages] · Cantidad de referencias por modalidad · Cantidad total de referencias · Tamaño de archivo de entrada · Duración por referencia · Duración acumulada de referencias · Sujetos por referencia · Vistas por sujeto |
| Video y audio | Duración admitida · Selección de movimiento predefinido [Master Shot preset] · Duración de generación [duration; --duration; duration_sec] · Frecuencia de fotogramas de salida [fps] · Bloqueo parametrizado de cámara [--camerafixed] · Activación de audio [generate_audio] · Cantidad de planos [shots] · Planos por generación · Presupuesto de habla |
| Capacidad declarada del generador | Soporte de render de texto [supports_text_render] · Soporte de movimiento [supports_motion] · Soporte de referencia de personaje [supports_character_ref] · Soporte de referencia de estilo [supports_style_ref] · Soporte de exclusión [supports_negative_prompt] · Acceso API completo [full] · Acceso API limitado [limited] · Ausencia de acceso API [none] · Parámetro bloqueado por entrada [Auto-locked parameter] |
| Límite y rango | Techo de longitud [max_prompt_words] · Intervalo recomendado · Límite máximo obligatorio |
| Cantidad de salidas | Cantidad de imágenes [numberOfImages] |

#### estructura y sintaxis del prompt

| Tipo | Valores |
|---|---|
| Bloque del prompt | Descripción de sujeto · Descripción de acción · Descripción de entorno · Bloque de cámara · Bloque de iluminación · Bloque de audio · Bloque temporal · Orden de bloques · Plantilla de cinco bloques [5-Slot] |
| Restricción | Restricción positiva · Restricción negativa · Lista de preservación · Lista de cambios · Prioridad entre instrucciones · Vocabulario excluido · Conflicto de restricciones · Prompt negativo |
| Referencia en el prompt | Referencia identificada · Marcador de referencia · Orden de lectura de referencias [Reference reading order] |
| Parámetro y token | Parámetro estructurado · Token de adaptador |
| Estilo sintáctico | Estilo sintáctico de palabras clave [keyword] · Estilo sintáctico natural [natural] · Estilo sintáctico por párrafos [paragraph] · Prompt estructurado JSON [JSON prompt] · Prosa natural · Plantilla parametrizada [Parameterized Template] · Palabras clave ordenadas · Estructura JSON |
| Marcador de audio y texto (video) | Marcador de música [( ) en la fuente Seedance 2.5] · Marcador de efecto sonoro [< > en la fuente Seedance 2.5] · Marcador de diálogo [{ } en la fuente Seedance 2.5] · Marcador de título o subtítulo [【 】 en la fuente Seedance 2.5] · Etiqueta de hablante [Character A; Character B; speaker tag] |
| Modo de detalle | Conciso [Concise] · Detallado [Verbose] · Cinematográfico detallado [Cinematic Verbose] · Prompt estándar |
| Ancla de conocimiento del mundo | Ancla de época [Era Anchor] · Ancla cultural [Cultural Anchor] · Ancla de género [Genre Anchor] |
| Análisis de imagen a prompt | Análisis inverso de imagen [Vision Analysis; Image-to-Prompt] · Descomposición visual [Deep Decomposition] · Síntesis de prompt desde imagen [Prompt Synthesis] |
| Reformulación observable | Reformulación observable |

#### estrategia y concepto

| Tipo | Valores |
|---|---|
| Brief y objetivo | Objetivo de comunicación · Audiencia · Problema de comunicación · Insight · Propuesta central [SMP] · Beneficio · Razón para creer [RTB] |
| Concepto | Territorio creativo · Concepto creativo · Concept card · Matriz de selección |
| Extracción de marca | Confianza de extracción · Fuente primaria de marca |

#### audio

| Tipo | Valores |
|---|---|
| Voz y diálogo | Timbre vocal [Voice texture] · Modo de emisión vocal [Says; whispers; shouts; mutters; asks] · Idioma de diálogo [Dialogue language] · Variedad regional o acento [Regional variety; accent] · Cadencia de habla [Speech rhythm] · Entrega interpretativa [Delivery style] · Anclaje visual de intervención [Visual anchoring before dialogue] · Separación temporal de turnos [Temporal dialogue control] · Presupuesto de habla [Dialogue budget] |
| Pista y sincronía | Audio generado · Ancla sonora [Sound anchor] · Sincronización audiovisual [Synchronized audio] · Audio nativo conservado [Native-track retention] · Audio de postproducción [Post audio bed] · Responsable de sonido por plano [Audio ownership] · Supresión de pista [Mute; audio strip] · Pulso musical [BPM] · Sonoridad de entrega [Loudness] |

#### continuidad entre clips

| Tipo | Valores |
|---|---|
| Tipo de continuidad | Consistencia interclip · Continuidad de mirada · Continuidad de acción · Continuidad de objeto · Continuidad de vestuario · Continuidad luminosa · Continuidad temporal · Continuidad geográfica · Salto de continuidad · Empalme entre anclas · Continuidad de timbre [Voice-timbre continuity] |

## Nivel 4 · Atributos de la regla


#### F01 · Etapa

| Valor | Definición |
|---|---|
| 0 Brand Lock | identidad de marca: paleta, tipografía, never list, voz |
| 1 Estrategia creativa | brief, SMP, territorios, concept cards, selección |
| 2 Guion | escenas, sluglines, acción, diálogo, XML |
| 3 Dirección cinematográfica | fórmula de escena, blocking, cámara motivada, 5 anclas, vocabulario prohibido |
| 4 Shot planning | shots.json, timing, texto en pantalla, series lock |
| 5 Imagen | génesis, anclas, edición, crítica y canonización |
| 6 Video | prompts de movimiento |
| 7 Paquete y entrega | carpeta final, preview, trazabilidad, créditos |
| Post-producción | generar clips, ensamblar, grade, audio, export |
| ORQUESTACIÓN | Control del proceso; conserva condiciones de entrada, etapa y cierre de gate. No significa selección incondicional de toda regla multietapa. |

#### F02 · Paso

| Etapa | Pasos |
|---|---|
| 0 | E0.1 reunir fuentes · E0.2 extraer las 9 secciones · E0.3 asignar confianza · E0.4 escribir brand-lock.md |
| 1 | E1.1 lectura del brief · E1.2 territorios · E1.3 concept cards · E1.4 matriz · E1.5 dirección narrativa |
| 2 | E2.1 analizar concepto · E2.2 breakdown · E2.3 escribir escenas · E2.4 XML |
| 3 | E3.1 fórmula de escena · E3.2 blocking y staging · E3.3 cámara y lente · E3.4 luz, color y ritmo · E3.5 5 anclas |
| 4 | E4.1 beat framework · E4.2 timing · E4.3 shot list · E4.4 texto separado · E4.5 series lock · E4.6 rationale y run.json |
| 5 | E5.1 plan de anchors · E5.2 génesis sin referencias · E5.3 maestros derivados · E5.4 cuadros con referencias · E5.5 edición quirúrgica · E5.6 borradores · E5.7 crítica · E5.8 revisión · E5.9 canonizar |
| 6 | E6.1 motion draft · E6.2 sintaxis del modelo · E6.3 continuidad · E6.4 dramaturgy check · E6.5 linter · E6.6 micro-gate y entrega |
| 7 | E7.1 árbol del paquete · E7.2 preview · E7.3 checklist de post · E7.4 trazabilidad |
| Post | POST.1 generar y verificar clips · POST.2 ensamblar y exportar |

#### F30 · Qué regula

| Valor | Definición |
|---|---|
| orquestación y control de flujo | activación, selección de skills, orden de etapas y control de avance; no es materia creativa |
| estrategia y concepto | brief, territorios, concepto |
| estructura narrativa y diálogo | escenas, beats, líneas |
| dramaturgia | fórmula de escena, 3 detalles, emoción traducida a cuerpo |
| encuadre y lente | tamaño de plano, focal, profundidad de campo |
| ángulo | altura y orientación de la cámara |
| movimiento de cámara | cómo se mueve la cámara |
| luz | fuente, dirección, dureza, ratio |
| color, grade y textura | paleta, grade, grano, halación |
| composición | spine, planos, espacio negativo |
| identidad y consistencia | que el sujeto se sostenga entre imágenes y clips |
| anatomía, rostro y piel | manos, rostro, piel documental |
| física y movimiento congelado | cues de velocidad, blur, estado posterior |
| texto en pantalla | overlays y texto dentro de la imagen |
| marca y logos | brand-lock, logos, productos reales |
| estructura y sintaxis del prompt | orden de bloques, slots, palabras permitidas y prohibidas |
| parámetros técnicos | ratio, resolución, duración, calidad |
| audio | diálogo, VO, SFX, música |
| continuidad entre clips | que un clip empate con el siguiente |
| crítica y revisión | criterios para aceptar o rechazar |
| trazabilidad y entrega | registro, carpeta, créditos |
| materialidad y superficie | propiedades visibles de materiales, texturas y acabados |
| puesta en escena y blocking | posiciones, desplazamientos y relaciones espaciales entre sujetos y objetos |
| animación | técnicas y principios de construcción del movimiento animado |

#### F31 · Condición para avanzar

| Valor | Definición |
|---|---|
| no | no es un gate |
| sí, la verifica una herramienta | validate_shots, linter, auditor |
| sí, revisión manual obligatoria | gate que el agente o la persona comprueba sin herramienta y sin nuevo OK del usuario: razón dramática escrita de cada decisión de cámara (etapa 3), dramaturgy check de 6 puntos y auditoría de 3 detalles de video (etapa 6) |
| sí, la aprueba el usuario | gates 1, 2 y 4 del director |

#### AMBITO · Ámbito funcional

| Valor | Definición |
|---|---|
| Preproducción | marca, estrategia, guion, dirección cinematográfica, planificación de shots |
| Creación de imagen | génesis, maestros, cuadros, anclas, edición de imagen |
| Creación de video | prompts de movimiento, sintaxis de modelo, continuidad, clips |
| Crítica, validación y aceptación | crítica de renders, validadores, gates, canonización; se vincula al medio evaluado |
| Audio y música independientes | audio que no sale del modelo de generación visual |
| Postproducción | ensamblado, grade, overlays, exportación |
| Empaquetado y entrega | paquete de producción, preview, trazabilidad y créditos |
| Orquestación y control de flujo | activación, selección de skills, orden de etapas, gates y escalamiento. Cada aplicación tiene disparador, condición y destino de control explícitos; no se le asigna una exclusión por defecto. |

#### USO OPERATIVO · Uso operativo (por aplicación de la regla)

| Valor | Definición |
|---|---|
| ACTIVO EN SELECCIÓN | la aplicación participa en la selección de reglas para generar imagen o video |
| INCORPORADA A TEMPLATE | aplicación incorporada y verificada en su template; incluye sintaxis de modelo aplicada una vez a la ficha. No se vuelve a extraer para cada caso; permanece clasificada. La incorporación exige vínculo regla → campo/bloque → condición → validación; si varía por caso, esa condición se evalúa al instanciar el template. |
| APLICACIÓN EN CONSTRUCCIÓN DE TEMPLATE | instrucción estructural seleccionable durante la construcción o actualización del template; exige destino y prueba de incorporación antes de publicar ese template. Expresa cuándo se usa, no aplaza su clasificación. |
| APLICACIÓN EN CONTROL O ENTREGA | aplicación de crítica, audio, postproducción o entrega seleccionable en su ruta específica, con disparador y destino. Su separación de recuperación de prompts requiere decisión aplicable y alcance documentados; una regla mixta conserva cada ruta. |
| INSERCIÓN MECÁNICA | la regla se agrega al prompt sin selección en cuanto el caso fija los datos de lista cerrada de su condición |
| BIBLIOTECA DE PLANTILLAS | plantilla de un look concreto: se ofrece por tipo de pieza y estilo, el usuario confirma como máximo una y se inserta |

#### METADATOS · Campos de la regla

| Campo | Valores o formato | Obligatorio |
|---|---|---|
| ID persistente | INV-/REG-nnnnnn; independiente de archivo, línea y texto | sí |
| documento · encabezado | archivo del corpus autorizado y ruta de títulos | sí |
| localización | líneas inicial–final; páginas asignadas inicial–final (50 líneas por página, marcadas ASIGNADA); paginación original si existe | sí |
| versión | hash del archivo original, hash de la representación textual (HTML) y hash del texto de la unidad | sí |
| idioma del enunciado | en · es · ru | sí |
| objeto regulado | activo visual o sonoro · documento · archivo · paquete de entrega · registro de ejecución (run) · campo o esquema | sí |
| medio del activo | rama activo: imagen fija · imagen secuencial · video · audio · pieza multimodal; otras ramas: se tipan por objeto regulado, sin valor ficticio de medio | obligatorio en la rama activo |
| unidad | fotograma · panel · clip · secuencia · escena · documento · archivo · paquete de entrega · registro (run) · campo o esquema · imagen fija suelta; según objeto y texto contextual | sí |
| referencia adjunta | tupla (medio ∈ imagen · video · audio; papel ∈ valores de la faceta 23; identificador, archivo y hash del adjunto); una por adjunto, de modo que cada papel queda asociado a su archivo | si la regla o el caso usan referencias |
| rutas de aplicación | una o más tuplas flujo → sección → paso → condición | sí |
| ámbito funcional · uso operativo | por aplicación (ver AMBITO y USO OPERATIVO) | sí |
| tipo de enunciado · fuerza normativa | sus valores del tesauro | sí |
| origen de evidencia · evidencia de la afirmación fuente | origen documentado separado de los descriptores, como metadatos documentales; nunca estados de clasificación ni filtros de elegibilidad | sí |
| adopción canónica | «adopción documental» (regla original de una skill, con fuente y autoridad resueltas; no exige ejercicio propio) · «Familia de régimen en borrador documental» y «Canonizada» (solo entradas del protocolo de familias de régimen) · «excluida por decisión del usuario» · «refutada» · «histórica» | sí |
| condición | grupo de condiciones: operador TODAS, ALGUNA o NINGUNA y sus miembros | si es condicional |
| estado de evidencia de capacidad · dependencia | sus valores del tesauro | si declara capacidad de modelo |
| estado del modelo citado | vigente · histórico, con versión y fecha de verificación | si nombra un modelo |
| autoridad | materia sobre la que tiene autoridad · ámbito · criterio de precedencia | si el texto la establece |
| precedencia | la precedencia aplicable entre los textos en conflicto | si hay conflicto documentado |
