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
