# Decisiones de Eric Toledano — 2026-10-26

Fuente: sesión `session_01RkzWqCTfrzRXTVrroB7zfi`, mensajes de Eric citados textualmente.

1. **Cuando un texto da una cifra que no es la de GPT Image 2, vale la cifra que el corpus da para GPT Image 2**, y el
   texto se corrige para que la especifique: «entonces las que valen son las que da el corpus, modifica el texto para
   que especifique el número de GPT 2».
   - Primer caso: INV-002054 (`skills/image/references/characters.md:3`). Original: «Up to 14 reference images
     (6 high-fidelity)», el desglose de Nano Banana Pro (`nano-banana.md:64-66`, `:144`). Corregido: «Up to 16
     reference images, each indexed with its role (GPT Image 2; high fidelity by default)» (`SKILL.md:43`,
     `gpt-image.md:96`, `:102`, `:104`, `golden-rules.md:93`, `models.md:54`).
   - La base de 13,005 textos no se modifica (está fijada por sha256). Las correcciones viven en
     `v3/universo/correcciones.json` y las aplica `v3/universo/textos_universo.py`.
2. «No estás aprobado para asumir nada, siempre lo verificas»: toda afirmación sobre un texto se comprueba leyendo el
   documento completo y su jerarquía hacia arriba, no por coincidencia de números o palabras.
3. «Siempre que hay una supuesta contradicción o incoherencia tienes que leer exhaustivamente los textos
   relacionados»: ninguna contradicción se declara, se corrige ni se marca sin haber leído completos todos los textos
   del corpus que tratan el mismo punto, con su sección y su jerarquía de carga.
4. **Interfaces de GPT Image 2: OpenAI API y fal.ai** (respuesta a la decisión 1 de 6). Manda
   `image/references/gpt-image.md:78` («`openai/gpt-image-2/edit` (на fal.ai) или соответствующий через OpenAI API»)
   sobre `visual-prompt-forge/adapters/gpt-image.md:94` («GPT Image is OpenAI-only as of Q2 2026»): DEC-000002
   («6.2 solo aplica si no hay archivo smixs») y T-BRIEF-IMG §1 (gpt-image.md gobierna GPT Image 2; `_capabilities.json`
   no se extrapola). `correr.py` conserva `INTERFACES = ("OpenAI API", "fal.ai")`.
5. **F20 con una sola persona que debe seguir reconocible: «todas»** (decisión 2 de 6). Base: TRM-0175 (taxonomía L1220,
   «cada persona del cuadro debe mantener un rostro reconocible») y L1210 (reconocimiento separado de cantidad). Aplica a
   C1 y B6; con edición activa INV-002352 A3 (quality high).
6. **Extensión F24 + «objeto entero»** (decisión 3 de 6): un objeto completo como sujeto del cuadro. Los 8 valores
   originales describen el sujeto por el cuerpo (taxonomía L1329–1336). Se registra en `v2/construir_esquema.py` con
   origen `extension_aprobada_2026-10-26`, aparte de la taxonomía original. Primer uso: C2 (póster del saxofón).
7. **F05 de B1 y B4 deja de ser lista vacía** (decisión 4 de 6; la lista vacía viola taxonomía §1.12.8): B1 (pescadora en
   el muelle) = «hospitalidad y viajes»; B4 (cocina, artículo de estilo de vida) = valor nuevo «estilo de vida», extensión
   de F05 registrada en `v2/construir_esquema.py`. Ninguna regla del piloto condiciona F05: la selección no cambia.
8. **Interfaz de generación de la prueba: App de ChatGPT para escritorio** (corregido 2026-10-27). Palabras de Eric
   registradas en `taller/demo/generar_desarrollo_spinning.py:47`: «interfaz es la app de chat gpt para deshtop». La app no
   expone parámetros: el tamaño y quality quedan como referencia y el formato se escribe en el texto del prompt
   (`taller/demo/PRUEBA_SPINNING_prompt_exportado.md:242`); por eso el Scene de cada caso nombra su ratio y `correr.py`
   lo valida. Sin parámetro `mask` en C1 (inferencia: la app no expone parámetros de API). Corrección de un error del
   agente: el primer registro de este punto tomó como interfaz de imagen la clave `OPENAI_API_KEY` de `api/sample.js`,
   que es el modelo de texto de la app anterior; la app vigente, `taller/`, escribe brief y prompt con la API de Anthropic
   (`taller/llm.py:3`) y no genera imágenes. Tamaño de B6-T2 1440x2160: máximo fiable en 2:3 por INV-002359
   (gpt-image.md:59), protocolo de rostro <20 % de `template-retrato-gpt2/b6-corregido`.
9. **Muestra de auditoría** (2026-10-27): Eric revisa al azar el 10 % del total de reglas marcadas «no aplica» en cada
   caso (redondeo hacia arriba, mínimo 1). Palabras de Eric: «la muestra debe de ser 10 % del número total de reglas que
   se marcaron como no aplica».
10. **Repetición antes de auditar** (2026-10-27): si una imagen sale mal, se genera el mismo prompt por lo menos dos veces
    más antes de auditar; solo la falla que se repite se diagnostica como a, b o c. Palabras de Eric: «si la imagen es
    mala hacemos por lo menos dos más antes de auditar». Coincide con INV-010355 («Budget 2–3 re-rolls») e INV-010387.
    INV-000591 («máximo dos intentos por método») rige los bucles de corrección del flujo (editar, cambio de método,
    replantear; INV-000584–000588), no la repetición del mismo prompt para diagnosticar.
11. **Longitud del prompt** (2026-10-27): ya estaba decidida (`.claude/rules/DECISIONES.md` decisión 2; T-BRIEF-IMG L355).
    La longitud que mencionan las reglas no bloquea: es una referencia aspiracional. Se espera que el prompt sea lo más
    corto posible, sin repeticiones ni ninguna otra ineficiencia del lenguaje, pero sin sacrificar la sintaxis que exigen
    los textos del modelo. Vale también para `armar.py`: su rechazo por más de 300 palabras (L84–85) pasa a aviso.
12. **Alcance de la prueba: solo imagen con aspecto de foto real** (2026-10-27). Palabras de Eric: «solo quiero que se
    prueben casos de foto realismo»; «quedan fuera de la prueba no del universo y sus reglas tienen que ser
    clasificadas»; «eso se hará en una prueba posterior, no es prioritario, todos los casos que involucren fotografía con
    aspecto real como transferencia de imagen, descripción de imagen, etc. tienen que tener una prueba específica en este
    ejercicio» (transcripción normalizada de los mensajes de la sesión). Consecuencias: cada tipo de imagen fotográfica
    tiene su propio caso en esta prueba; las técnicas no fotográficas (F18 distinto de «fotorrealista») quedan fuera de
    la prueba pero siguen en el universo; la clasificación de sus reglas se hace en una prueba posterior. La palabra
    «photorealistic» / «fotorealista» sigue prohibida dentro de los prompts.
13. **vision-decomposer y transferencia de estilo son cosas distintas** (2026-10-27). Palabras de Eric: «porque si son
    para cosas diferentes, o no te das cuenta?». `vision-decomposer.md` es análisis de imagen a prompt (`:1–3`): de una
    imagen saca un prompt para recrearla. La transferencia de estilo con la imagen adjunta al generador la gobierna
    `gpt-image.md` Style Transfer (`:111–113`). La mención de «style transfer from a reference image» en
    `image/SKILL.md:63` (INV-002027) no lleva la transferencia con imagen adjunta a vision-decomposer.
14. **Caso de descripción de imagen** (2026-10-27, responde la pregunta 2 de `v3/revision/04_preguntas_eric.md`).
    Palabras de Eric: «se le proporciona una imagen, el sistema la describe y se crea un prompt de generación génesis con
    esa descripción y se genera; si la imagen es similar, entonces pasa la prueba» (transcripción normalizada).
    Consecuencias: el caso se ejecuta como génesis (cero referencias; la foto no se adjunta al generador); lo que el
    sistema saca de la foto entra al brief con origen `inferencia_para_aprobacion` y la foto con su sha256 como fuente
    (schema L1040–1332); el prompt es de génesis para GPT Image 2, así que sale en los 5 apartados del adaptador GPT2-GEN
    (`gpt-image.md:7–15`, `verificar_templates.py` L62–65), no en las palabras sueltas de `vision-decomposer.md:61`. El
    criterio de aprobado es el parecido de la imagen generada con la foto de entrada.
15. **Sin veredicto d en el diagnóstico** (2026-10-27, responde la pregunta 3). Palabras de Eric: «no hay límite de
    modelo porque es un modelo frontera, y regla excluida no puede ser porque el modelo no va a excluir reglas relevantes
    bajo ninguna circunstancia, a menos que estén fuera del scope correcto» (transcripción normalizada). Consecuencias:
    toda falla repetida se diagnostica a, b o c. La regla de Nano Banana 2 con grounding para edificación, animal y planta
    (`flujo-spot.html:620`, `flujo-anclas.html:436`) está fuera del alcance por 23 §6, no es regla pertinente de esta
    prueba; esos sujetos se resuelven con las reglas de GPT Image 2. Una falla que ninguna regla del corpus cubre es c.
