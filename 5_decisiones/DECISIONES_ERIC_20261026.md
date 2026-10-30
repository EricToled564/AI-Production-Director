# Decisiones de Eric Toledano — 2026-10-26

Fuente: sesión `session_01RkzWqCTfrzRXTVrroB7zfi`, mensajes de Eric citados textualmente.

1. **Cuando un texto da una cifra que no es la de GPT Image 2, vale la cifra que el corpus da para GPT Image 2**, y el
   texto se corrige para que la especifique: «entonces las que valen son las que da el corpus, modifica el texto para
   que especifique el número de GPT 2».
   - Primer caso: INV-002054 (`skills/image/references/characters.md:3`). Original: «Up to 14 reference images
     (6 high-fidelity)», el desglose de Nano Banana Pro (`nano-banana.md:64-66`, `:144`). Corregido: «Up to 16
     reference images, each indexed with its role (GPT Image 2; high fidelity by default)» (`SKILL.md:43`,
     `gpt-image.md:96`, `:102`, `:104`, `golden-rules.md:93`, `models.md:54`).
   - La base de textos no se modifica (está fijada por sha256); las correcciones viven aparte.
2. «No estás aprobado para asumir nada, siempre lo verificas»: toda afirmación sobre un texto se comprueba leyendo el
   documento completo y su jerarquía hacia arriba, no por coincidencia de números o palabras.
3. «Siempre que hay una supuesta contradicción o incoherencia tienes que leer exhaustivamente los textos
   relacionados»: ninguna contradicción se declara, se corrige ni se marca sin haber leído completos todos los textos
   del corpus que tratan el mismo punto, con su sección y su jerarquía de carga.
4. **Interfaces de GPT Image 2: OpenAI API y fal.ai** (respuesta a la decisión 1 de 6). Manda
   `image/references/gpt-image.md:78` («`openai/gpt-image-2/edit` (на fal.ai) или соответствующий через OpenAI API»)
   sobre `visual-prompt-forge/adapters/gpt-image.md:94` («GPT Image is OpenAI-only as of Q2 2026»): DEC-000002
   («6.2 solo aplica si no hay archivo smixs») y T-BRIEF-IMG §1 (gpt-image.md gobierna GPT Image 2; `_capabilities.json`
   no se extrapola).
5. **F20 con una sola persona que debe seguir reconocible: «todas»** (decisión 2 de 6). Base: TRM-0175 (taxonomía L1220,
   «cada persona del cuadro debe mantener un rostro reconocible») y L1210 (reconocimiento separado de cantidad). Aplica a
   C1 y B6; con edición activa INV-002352 A3 (quality high).
6. **Extensión F24 + «objeto entero»** (decisión 3 de 6): un objeto completo como sujeto del cuadro. Los 8 valores
   originales describen el sujeto por el cuerpo (taxonomía L1329–1336). Se registra con
   origen `extension_aprobada_2026-10-26`, aparte de la taxonomía original. Primer uso: C2 (póster del saxofón).
7. **F05 de B1 y B4 deja de ser lista vacía** (decisión 4 de 6; la lista vacía viola taxonomía §1.12.8): B1 (pescadora en
   el muelle) = «hospitalidad y viajes»; B4 (cocina, artículo de estilo de vida) = valor nuevo «estilo de vida», extensión
   de F05. Ninguna regla del piloto condiciona F05: la selección no cambia.
8. **Interfaz de generación de la prueba: App de ChatGPT para escritorio** (corregido 2026-10-27). Palabras de Eric:
   «interfaz es la app de chat gpt para deshtop». La app no expone parámetros: el tamaño y quality quedan como
   referencia y el formato se escribe en el texto del prompt; por eso el Scene de cada caso nombra su ratio. Sin
   parámetro `mask` en C1 (inferencia: la app no expone parámetros de API). Tamaño de B6-T2 1440x2160: máximo fiable en
   2:3 por INV-002359 (gpt-image.md:59), protocolo de rostro <20 %.
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
    los textos del modelo.
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
14. **Caso de descripción de imagen** (2026-10-27).
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
16. **Lista de casos de la prueba** (2026-10-27). Eric
    aprobó la recomendación tal como está escrita en esa pregunta:
    - Un caso por cada valor de F10, incluidos los 8 hijos de edición de 23 §4 y la descripción de imagen.
    - Un caso por cada valor de F15: persona, lugar, edificación, animal, producto, objeto, planta.
    - Un caso por cada valor de F32: sin texto, texto corto, texto extenso o pequeño.
    - Un caso por cada una de las 4 plantillas de edición fotográfica sin hijo: cambio de fondo con la misma persona (`characters.md:80`), textura de material (`editing.md:98`), relleno con física (`editing.md:92`) y adaptación de anuncio a otro mercado (`editing.md:82`).
    - F11, F13, F14 y los valores fotográficos de F04 quedan cubiertos dentro de esos casos, cada valor al menos una vez.
    - Quedan fuera de esta prueba, aunque siguen en el universo: identidad de marca, diapositiva, infografía y diagrama, diseño de personaje, UI de pantalla y scroll.
    - También quedan fuera: colorizar manga, máscara y refinamiento conversacional.
17. **Boceto o plano a final: 5 casos** (2026-10-27). Eric eligió un caso por cada plantilla fotográfica, igual que en
    edición:
    - plano 2D → interior (`dimensional.md:5–18`, `:61–68`);
    - boceto → concepto 3D (`dimensional.md:20–27`);
    - alzado → exterior (`dimensional.md:53–59`);
    - diseño plano → mockup de producto (`dimensional.md:70–77`);
    - boceto → final (`structural.md`).

    3D → 2D técnico y meme no dan foto y quedan fuera.
18. **Dos textos mal excluidos entran al universo** (2026-10-27). Eric respondió «Sí, meterlos» a la pregunta «¿Meto
    al universo los 2 textos mal excluidos?». Origen: la auditoría de los 410 textos excluidos uno por uno.
    Los dos textos:
    - INV-002383, `gpt-image.md:96`: entra como «**Object removal:** «Remove [X]. Do not change anything else.» (в
      gpt-image-2 high-fidelity по умолчанию).».
    - INV-002531, `multi-panel.md:162`: entra solo con la línea del tamaño 1536x1024.

    Mecanismo: el mismo de INV-002054. El universo
    queda en 2,724 textos. Se comprobó que no cambió ninguna otra decisión ni el orden del resto.
19. **La decisión por sección se mantiene** (2026-10-27, 00:28–00:37 UTC; registrada tarde, el 2026-10-27). Se decidió en
    esta sesión y no se había anotado en este archivo.
    - **Condición de Eric** (mensaje de las 00:28:45 UTC, transcripción normalizada): «si el documento del skill hace
      sentido no dejaría una regla que no corresponde a creación de imagen fuera de la sección de creación de imagen […]
      hacemos esto si me das un solo ejemplo de una regla que aplique al scope de la prueba que esté en los documentos
      que se quedarían fuera por sección y que no esté en los textos que están dentro de la sección de creación de
      imagen y que sea relevante para la creación de imágenes; te dejo que clasifiques esos documentos si no; mantenemos
      la decisión de catalogar por sección».
    - **Resultado** (respuesta del agente a las 00:37:19 UTC): los ejemplos propuestos fueron el crash zoom INV-009044,
      `camera-lighting-vocabulary.md` §10 y director §7. Ninguno cumplía la condición: son reglas de clip o de
      enrutamiento, no de imagen suelta. «Se mantiene la decisión por sección».
    - **Consecuencia:** los 9,873 textos de secciones «otro_modelo» y «fuera» no se leen uno por uno.
      Los dos errores de la auditoría de 2026-10-27 (26 §18) no reabren esta decisión.
      Salieron de textos de secciones de imagen decididos uno por uno, no de secciones excluidas.
