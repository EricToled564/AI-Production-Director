# Preguntas que solo Eric puede resolver — 2026-10-27

Salen de `02_facetas_tipo_imagen.md`, `03_citas_plan.md` y `05_lectura_universo.md`. Sin estas respuestas no se puede
fijar la lista de casos del plan.

## 1. Qué cuenta como «tipo de imagen» (decisión 26 §12)

La taxonomía tiene varias facetas que describen la imagen. Las que dicen qué imagen se produce:

- F10 modo: génesis, ancla, composición, edición y sus 8 hijos, transferencia de estilo, boceto o plano a final,
  descripción de imagen.
- F15 sujeto: persona, lugar, edificación o landmark, animal, producto, objeto, planta.
- F32 texto en la imagen: sin texto, texto corto, texto extenso o pequeño (`01_texto_en_imagen.md`: GPT Image 2 sí
  lo hace cuando el texto es parte de lo fotografiado).
- F11 rol del ancla, F13 tipo de acción, F14 régimen físico.
- F04 tipo de pieza: editorial, key visual, e-commerce, retrato, póster, post para redes, miniatura, mockup de
  dispositivo, multipanel con fotos, visualización arquitectónica, campaña.

Pregunta: ¿cada valor de cuáles de esas facetas necesita su propio caso? Recomendación: F10, F15 y F32 con un caso por
valor, y F11, F13, F14 y F04 cubiertos dentro de esos mismos casos, cada valor al menos una vez.

Pregunta aparte de F04: identidad de marca, infografía, diapositiva, diseño de personaje y concept art suelen no ser
fotográficos. ¿Quedan fuera como las técnicas no fotográficas?

Eric (2026-10-27): «no lo sé, dame una recomendación». Recomendación detallada, con las definiciones de la taxonomía
00688 L486–503 y L525–591:

- **Un caso por valor:** F10 (cada modo, con los 8 hijos de edición y la descripción de imagen), F15 (persona, lugar,
  edificación, animal, producto, objeto, planta) y F32 (sin texto, texto corto, texto extenso o pequeño). Son las tres
  facetas que cambian la técnica del prompt: otro adaptador u otra operación (F10), otra génesis por clase de sujeto
  (INV-000539, 000593), otro tratamiento del texto (`gpt-image.md:67–74`).
- **Edición: un caso por cada plantilla fotográfica de la fuente.** Los 8 hijos de 23 §4 (quitar objeto, añadir
  objeto, cambiar luz o clima, colorizar, restaurar, traducir texto, cambiar vestuario, cambiar mobiliario u objeto)
  tienen plantilla en `editing.md` y `gpt-image.md:94–100`. La fuente trae además cuatro plantillas de edición
  fotográfica que no caben en ningún hijo (taxonomía L858, L865, L867, L927): cambio de fondo o entorno con la misma
  persona («Change background to [SCENE], maintain lighting on face», `characters.md:80`, TRM-0511); textura de material
  («Add [MATERIAL] texture to [SURFACE]», `editing.md:98`, TRM-0518); relleno con física («Fill this glass with
  [LIQUID]», `editing.md:92`, TRM-1142); adaptación de un anuncio a otro mercado (escenario e idioma, `editing.md:82`,
  TRM-0520). Recomendación: un caso para cada una de las cuatro, igual que los 8 hijos. Quedan fuera: colorizar manga
  (no es foto, `editing.md:59`), máscara (la app no la expone, 26 §8) y refinamiento conversacional (es la forma de
  iterar, no un tipo de imagen).
- **Boceto o plano a final: pregunta abierta (2026-10-27, al cerrar la lectura de la taxonomía).** Leí completo
  `dimensional.md` (L1–88). Cuatro de sus plantillas dan una foto: plano 2D → interior (L5–18, L61–68), boceto →
  concepto 3D (L20–27), alzado → exterior (L53–59) y diseño plano → mockup de producto (L70–77). A esas se suma
  boceto → final de `structural.md`. Si se aplica el mismo criterio que en edición (un caso por plantilla
  fotográfica), salen 5 casos en lugar de 1. Recomendación: los 5, por coherencia con edición. Registro:
  `06_documentos_rectores.md`, fila L3916–4020.
- **Cubiertas dentro de esos casos, cada valor al menos una vez:** F11 (los 6 roles del ancla), F13 y F14 (tipos de
  acción y regímenes) y F04 en sus valores fotográficos: editorial, key visual, e-commerce o catálogo, retrato
  (individual y de grupo, TRM-1260), visualización arquitectónica (`dimensional.md:51`), multipanel de fotos, mockup de
  dispositivo fotografiado. Póster, post o historia para redes y miniatura son una foto más un titular o un CTA
  sobrepuesto; ese texto sobrepuesto nunca va en el prompt y se compone después (`01_texto_en_imagen.md`), así que la
  parte que genera el modelo es una foto cubierta por los casos de F15 y F32.
- **Fuera de esta prueba (siguen en el universo, se clasifican en la prueba posterior, 26 §12):** identidad de marca
  (logo y sistema, TRM-0022), slide (TRM-0016), infografía y diagrama (TRM-1258, 1259), diseño de personaje (hojas de
  giro, expresiones, chibi: TRM-1116–1120), UI de pantalla (TRM-0014), scroll (CAT-F04-SCROLL).

## 2. El caso de descripción de imagen

Lo que es: se le da al sistema una foto, el sistema la analiza y escribe un prompt para recrearla sin adjuntarla; la
prueba es si la imagen generada se parece a la original. Lo gobierna `vision-decomposer.md`.

Dos choques con lo que ya existe:

- **No hay operación en el contrato.** El schema tiene 8 operaciones y ninguna es esta (L45–54), y la taxonomía dice
  que un modo sin contrato «permanece no habilitado» (L260). Propuesta: probarlo como una génesis (cero referencias),
  con el brief lleno a partir del análisis de la foto; cada valor sacado de la foto entra con el origen que el schema ya
  tiene, `inferencia_para_aprobacion`, y la foto con su sha256 como fuente (schema L1312–1318). No hace falta cambiar el
  schema.
- **Formato del prompt.** `vision-decomposer.md:61` pide el prompt como palabras sueltas separadas por comas; para GPT
  Image 2, `gpt-image.md:7–15` y el validador del contrato (`verificar_templates.py` L62–65) exigen los 5 apartados
  (Scene, Subject, Important Details, Use Case, Constraints). Es la contradicción de `CONTRADICCIONES.md` §3, que ahora
  sí entra porque tú pediste probar la descripción de imagen.

Pregunta: ¿se prueba como génesis con el brief salido del análisis, y el prompt sale en los 5 apartados? Recomendación:
sí a las dos (DEC-000025: los templates siguen la sintaxis del modelo).

**Respuesta de Eric (2026-10-27):** sí, como génesis; aprueba si la imagen generada se parece a la foto. Registrada en
`DECISIONES_ERIC_20261026.md` §14.

## 3. Un veredicto de diagnóstico que falta

Hoy cada falla repetida se clasifica a (el selector no tomó la regla), b (el prompt no la cumple) o c (falta la regla
en el corpus). El corpus describe dos causas más que no caben en ninguna:

- **Límite del modelo:** el crítico manda decir cuándo un fallo es una debilidad conocida del generador (manos, ojos)
  y no del prompt (`visual-asset-critic/SKILL.md` regla 4; `critique-rubric.md` L59 y L111); y tras 5 o más re-rolls
  sin mejora «the model can't render this concept» (`failure-modes.md` L128).
- **Regla excluida por decisión:** para edificación, animal y planta reales la fuente manda Nano Banana 2 con
  grounding (`flujo-spot.html:620`, `flujo-anclas.html:436`); con solo GPT Image 2 (23 §6) esa regla queda fuera y
  una falla puede venir de ahí.

Pregunta: ¿se añade un veredicto d, «límite documentado del modelo o regla excluida por decisión», con la cita del texto
que lo documenta como evidencia? Recomendación: sí; sin él, esas fallas quedarían mal clasificadas como b o c.

**Respuesta de Eric (2026-10-27):** no. Solo a, b o c; la regla de grounding está fuera del alcance y no es pertinente.
Registrada en `DECISIONES_ERIC_20261026.md` §15.
