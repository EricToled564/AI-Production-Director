# Lectura: universo de imagen completo para el piloto del caso caballo (2026-10-31)

Documentos: los 1,511 textos del universo del 23 de octubre (`skills/image/**` sin LICENSE ni NOTICE, el adaptador
`skills/visual-prompt-forge/adapters/gpt-image.md` y el ejemplo `gpt-image.txt`), leídos completos. Pregunta de la
lectura: qué textos aplican al caso «imagen documental de un caballo galopando en la playa al atardecer», GPT Image 2.
Los números son IDs INV. Resultado: `7_auditorias_y_verificaciones/piloto_caso_caballo_20261031.md`.
## SKILL.md (leído completo, L1-L118)
Aplican: 2000 (salida = modelo+calidad+tamaño+prompt; template, parámetro), 2010-2011 (modelo; dado por el caso), 2044 (formato de salida: Model/Quality/Size/Prompt/Notes; template), 2049 (preferir hex, materiales concretos, composiciones nombradas, 5-slot en GPT Image; template), 2050 (evitar tag soup, elogios vagos, negaciones -> invertir a positivo, comparaciones externas; template).
No aplican: 2003-2005 ruteo (control); 2014/2017/2038/2040 descripciones-puntero; 2045-2046 edición (F10 edición); 2020-2036 ruteo por tarea; 1998,2052 frontmatter/licencia.
## characters.md (completo)
Ninguno aplica: todo es persona con referencia (F15 persona, F23) o edición. 2072 «Mid-stride, dynamic motion» es control de pose de un personaje con identidad fijada.
## creative-direction.md (completo)
Aplican: 2087 (decir exactamente cómo se ilumina; template), 2094 golden hour backlighting long shadows (ejemplo; momento del día hora dorada), 2103 nombrar cámara cambia el ADN (selección), 2112-2124 ángulos, planos y foco (selección), 2125 preferir términos descriptivos sobre 50mm/f (template; choca con ejemplos de GPT Image que usan 50mm f/2.0), 2127-2139 grades y películas (selección; 2136 high contrast desaturated), 2141 decir de qué está hecho el sujeto (template), 2150-2153 propiedades de superficie (selección).
No: 2089-2091 estudio; 2093,2095-2097,2099-2101 otros efectos (opciones de selección no pedidas por el caso); 2156-2164 ejemplos de edición/estilos ajenos.
## dimensional.md (completo)
Ninguno aplica: conversiones 2D/3D, planos, memes, arquitectura con referencia. 2182 (Time: dawn/midday/dusk/night) es plantilla de exterior arquitectónico desde un alzado (F10 conversión), no génesis.
## editing.md (completo)
Ninguno aplica: todo es edición de imagen existente (F10 edición). 2209 «Golden hour / sunset / warm backlight» es vocabulario de reluminación (edición).
## golden-rules.md (completo)
Aplican: 2241 empezar con verbo (template), 2243-2246 encuadre positivo (template; fija restricciones/forma), 2253 lenguaje natural, no tag soup (template), 2255-2260 ser específico: sujeto, material, color hex, posición (template), 2262-2265 dar contexto de uso (template; selección del contexto), 2299 anclas de conocimiento del mundo en GPT Image 2 (selección), 2301-2313 tipos de ancla (selección), 2315-2318 reglas de uso de anclas: alto nivel, combinar con detalles, una sola ancla de género, mejor en GPT Image 2 (template), 2328 «Peter Lindbergh influence» ejemplo de ancla con playa (ejemplo, no pedido).
No: 2248-2251, 2280-2284 refinamiento tras generar (iteración, no génesis); 2267-2271 texto (F32 sin texto); 2273 plantilla con tipografía (póster); 2274 puntero; 2276-2278 costo en lote (control, no redacción); 2286-2297 referencias (F23 ninguna).
## gpt-image.md (completo)
Aplican (template de GPT Image 2 salvo nota): 2332 gpt-image-2 por defecto (parámetro), 2334 secciones con etiquetas, 2335 5 slots Scene/Subject/Important Details/Use Case/Constraints, 2336 sin constraints el modelo deriva, 2338 ejemplo mínimo (ejemplo; blue hour, 50mm feel), 2340-2346 anti-slop (no elogios vagos, no etiquetas de estilo, no comparaciones, no lenguaje de mood; escribir hechos visuales), 2350-2353 calidad (medium es el punto de partida; 2353 dice empezar en low), 2355-2364 tamaños (inserción mecánica por F06: horizontal 1536×1024), 2392 ancla de conocimiento del mundo (selección), 2394 prompt base limpio, 2397 secciones con etiqueta, 2400 plantilla Photoreal Editorial (inserción mecánica por F04 editorial + F18 fotorrealista: constraints no glamorization, no heavy retouching, no studio gloss).
No: 2366-2372 texto (F32 sin texto), 2374-2385 edición, 2387-2388 referencias, 2390 transferencia de estilo, 2395-2396 iteración, 2402-2408 plantillas de otras piezas, 2410-2412 migración (F35 sí).
Hallazgos: (a) calidad: 2351 «medium por defecto» frente a 2353 «empezar en low» y models.md 2468 «high para fotorrealismo»: contradicción para Eric. (b) 2400 pide F04 editorial; el caso «imagen documental» no tiene tipo de pieza que lo nombre.
## models.md (completo)
Aplican: 2416 el modelo cambia la estructura (template), 2434 GPT Image 2 no hace grounding de especies (selección: el caballo genérico no lo necesita), 2442 5 slots, 2453 en GPT Image «50mm feel» solo como look de alto nivel (template), 2454 anti-slop, 2456 positivo + lista de preservación, 2457 escenas complejas en 5 slots, 2468 high para fotorrealismo (inserción mecánica F18), 2470 modelo y calidad van como meta junto al prompt (template).
No: 2420-2431 resto de la tabla de elección (modelo ya dado), 2435-2437 NB, 2439-2441 edición/texto/UI, 2445-2448 descripción, 2458-2459 edición/referencias, 2463-2467,2469 costos de otros niveles.
## multi-panel.md (completo)
Ninguno aplica como regla del caso (F04 storyboard o multipanel), salvo 2550: «la instrucción de motion blur debe ser específica (blur en manos y pies) o el modelo lo aplica a todo»; está dentro de una plantilla multipanel pero habla del modelo en general → selección si el caso pide desenfoque de movimiento (galope). Hallazgo: regla general escondida en una sección de pieza.
## nano-banana.md (completo)
Ninguno aplica: F29 Nano Banana. 2612/2614 (grounding de especies animales) es solo NB2; confirma que GPT Image 2 no tiene grounding (models.md 2434).
## patterns/character-design.md (completo)
Ninguno aplica: F04 diseño de personaje (plantillas de biblioteca y su modelo/calidad).
## patterns/ecommerce.md, fashion-editorial.md, food-beverage.md (completos)
Ninguno aplica: plantillas de biblioteca de producto, moda y comida (F04 e-commerce, editorial de moda; F05 moda, comida). 2787 (roller skating) es una plantilla de moda con golden hour backlight y halo cálido: ejemplo de cómo se escribe la contraluz de hora dorada, pero es biblioteca de otra pieza y su modelo recomendado es NB2.
## patterns/portrait-cinema.md, poster-illustration.md, ui-social.md (completos)
Ninguno aplica: biblioteca de retrato (F15 persona), póster y UI. Hallazgo: 2867 (Golden Hour Street Backlit Portrait) es la descripción más completa de luz de hora dorada del corpus (sol 5-10° sobre el horizonte, ámbar, bruma, contraluz con borde, sombra larga hacia cámara, flare contenido), pero vive dentro de una plantilla de retrato; no existe una regla general de luz de atardecer.
## prompt-framework.md (completo)
Aplican: 2997 tipo Photorealistic: claves luz, materiales, atmósfera (inserción mecánica F18 fotorrealista), 3038 árbol: foto de objeto real → Photorealistic (inserción mecánica), 3009-3010 obligatorios sujeto y contexto de uso (template), 3012-3019 por situación: acción, entorno, plano, luz, ánimo, materiales, paleta, formato (template, el caso los llena), 3020 en GPT Image 2 «50mm feel» solo como look (template), 3022-3027 modos de detalle (selección; el caso simple pide estándar), 3029-3036 salida: prompt, parámetros si no son 1:1, exclusiones en positivo, supuestos (template), 3042 ejemplo fotorrealista «Mood: authentic, documentary style» con hora dorada (ejemplo), 3075 partículas («pollen floating in golden hour air») y 3080 señales de movimiento («slight motion blur on trailing hair strand») del modo cinematográfico detallado (selección).
No: 2989-2992 punteros; 2998-3005 otros tipos; 3039 NB; 3044-3048 ejemplos de otras piezas; 3050-3063 plantillas parametrizadas para series (el caso es pieza única); 3065-3070 cuándo usar cinematic verbose (hero, key visual: no es el caso); 3083-3085 ejemplo café.
Hallazgo: los ejemplos del corpus escriben «Mood: …» como línea del prompt; gpt-image.md 2346 lo prohíbe en GPT Image 2 y la decisión de Eric (F36) pide la traducción. Para GPT Image 2 manda 2346.
## slides.md (completo)
Ninguno aplica: F04 slide o presentación. 3174 regla de tercios y 3184 espacio negativo están bajo «Layout Systems» de slides.
## storyboards.md, structural.md, text-rendering.md, vision-decomposer.md (completos)
Ninguno aplica: secuencias, estructura con referencia, texto e infografía, análisis de imagen a prompt (3457: no se carga sin imagen de referencia).
## visual-prompt-forge/adapters/gpt-image.md (completo)
Aplican: 11720 lenguaje espacial explícito (template), 11722-11723 sintaxis en 3 párrafos (choca con los 5 slots de gpt-image.md), 11728-11731 parámetros: size 1792x1024 para 16:9, quality high en hero y medium en series, style natural para fotorreal, modelo (parámetros; 1792x1024 no es una de las medidas «ходовые» de gpt-image.md), 11735 150-300 palabras (template), 11737-11741 relaciones espaciales (selección), 11743 cierre «natural skin texture, no AI rendering artifacts» si es fotorreal (inserción mecánica F18; escrito para piel humana), 11756-11760 no listas con comas, usar lenguaje espacial, máximo 5 elementos, sin --ar, línea anti «AI look» (template).
No: 11719 nota de capacidades, 11733 comentario de parámetros (registro), 11747 ejemplo del fundador (ejemplo), 11749-11754 texto, 11762 API.
## one-shot-all-adapters/gpt-image.txt (completo)
Ninguno aplica como regla: ejemplo de storyboard con gpt-image-1.5.
