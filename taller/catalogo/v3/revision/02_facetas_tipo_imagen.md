# Facetas que definen tipos de imagen fotográfica — revisión (2026-10-27)

Fuente: `v2/esquema_taxonomia.json`, las 37 facetas leídas completas, con todos sus valores (volcado de la sesión del
2026-10-27). Alcance: decisión 26 §12 (solo imagen con aspecto de foto real; cada tipo fotográfico con caso propio).

## A. Facetas que dicen QUÉ imagen se produce (candidatas a «tipo»)

| Faceta | Valores fotográficos de imagen fija con GPT Image 2 | Valores fuera y motivo |
|---|---|---|
| F10 Modo de generación | génesis sin referencias; ancla con referencias; composición de varias referencias; edición (T5) y sus 8 hijos (quitar objeto, añadir objeto, cambiar luz o clima, colorizar, restaurar, traducir texto, cambiar vestuario, cambiar mobiliario u objeto); transferencia de estilo; boceto o wireframe a final; análisis de imagen a prompt | texto a video, primer frame (3a), primer y último frame (3b), con referencias (Kling/Seedance/Veo), motion control, lip-sync, motion brush, edición de video, extensión, multi-shot, ultra long, blockout, storyboard como entrada: son modos de video |
| F11 Rol del ancla | character ref, environment ref, keyframe FF, keyframe LF, hero/macro, motif insert | — |
| F15 Sujeto | persona, lugar genérico, edificación o landmark, animal, producto, objeto o prop, planta | — |
| F32 Texto en la imagen | sin texto, texto corto, texto extenso o pequeño (ver `01_texto_en_imagen.md`) | — |
| F04 Tipo de pieza (imagen) | editorial, key visual de campaña, e-commerce o catálogo, retrato, póster o key art, post o historia para redes, miniatura, UI o mockup (dispositivo fotografiado), storyboard o multipanel (paneles fotográficos), visualización arquitectónica, campaña, scroll, pieza de portafolio | identidad de marca (logo), infografía o diagrama, slide, diseño de personaje, concept art: su técnica habitual no es fotográfica (por decidir, ver §C); spot, brand film, videoclip, fashion film, cortometraje, explainer, demo, testimonial, UGC, reel, anuncio para redes, hook: son video |
| F13 Tipo de acción | A pose sostenida, B instante pico, C movimiento continuo, D fenómeno de luz o clima, E interacción o diálogo, F multitud, G acuática en superficie, H subacuática | — |
| F14 Régimen físico | 01 a 09 | — |

## B. Facetas que dicen CÓMO se ve o se encuadra (atributos de cada caso)

F06 formato (16:9, 9:16, 1:1, 4:5, 21:9, 2:3, 3:4, 3:2; fuera 1:4, 1:8, 4:1, 8:1: GPT Image 2 no pasa de 3:1,
`gpt-image.md:55`, `:65`), F16 espacio, F17 estilo visual (13), F19 número de sujetos, F20 identidad, F21 contacto, F22
tamaño del rostro, F24 tamaño de plano, F25 ángulo, F33 complejidad, F34 resolución, F23 referencias adjuntas (solo
las de imagen: persona, vestuario, lugar, producto, estilo, estructura).

## C. Lo que solo Eric puede decidir

1. ¿Qué facetas cuentan como «tipo de imagen» y exigen un caso por valor: solo F10, o también F11, F15, F32, F04, F13 y
   F14? Las de la sección B, ¿se cubren al menos una vez cada valor repartidas entre los casos, o no se exigen?
2. F04: identidad de marca, infografía, slide, diseño de personaje y concept art, ¿entran como pieza fotográfica o
   quedan fuera por técnica?

## D. Fuera de la prueba en cualquier caso

F01–F03, F05, F07–F09, P01, P04, F12, F26–F31, F35: etapa, paso, ruta, temática, género, beats, montaje, flujo,
lugar de publicación, función del plano, movimiento de cámara, transición, audio, modelo, qué regula, gate y migración
no definen el tipo de imagen fija. F29 es fijo: GPT Image 2 (decisión 23 §6).
