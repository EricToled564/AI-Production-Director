# Criterios, instrucciones y definiciones para clasificar

Documento único y centralizado. Quien clasifique (el agente o un subagente) aplica solo lo que está aquí y en
`3_taxonomia/TAXONOMIA_CANONICA.md`; nada queda a su criterio. Requiere la aprobación de Eric antes de crear cualquier
agente de clasificación.

## 1. Qué se clasifica

- **Universo de esta fase:** los textos de imagen fijados por Eric el 23 de octubre (decisión §1): `skills/image/**`
  sin LICENSE ni NOTICE, `skills/visual-prompt-forge/adapters/gpt-image.md` y
  `skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt`.
- **Unidad:** cada texto de la base (`2_corpus/…sqlite`, tabla `textos`), con su ID INV.
- **Copias idénticas:** cada copia se clasifica por separado, en su propio documento y encabezado, porque una misma
  regla puede aplicar a varios casos de uso (decisión de Eric, 2026-10-31). La columna `copia_de` solo indica de qué texto
  es copia; no traslada la clasificación.
- **Modelo:** la taxonomía vale para cualquier modelo. Un texto que solo vale para otro modelo se clasifica igual,
  con su F29.

## 2. Cómo se lee cada texto

1. Se lee el texto completo y, siempre y de forma obligatoria, sus tres niveles: el título del documento, el
   encabezado del texto y el encabezado inmediatamente superior (decisión de Eric, 2026-10-31). Nunca se clasifica por
   palabras clave.
2. Se usa la sección del nivel 2 (`3_taxonomia/precatalogacion_por_encabezado.csv`) solo como punto de partida: el
   texto manda sobre la sección.
3. Si un texto depende del anterior o del siguiente (una lista bajo un párrafo, una fila bajo su tabla), se leen
   juntos y cada uno se clasifica por lo que dice en ese contexto.

## 3. Pasos de clasificación, en este orden

| Paso | Pregunta | Valores | Regla de decisión |
|---|---|---|---|
| 1 | ¿Impacta la redacción? | Impacta · No impacta | Impacta si dice qué se escribe, o qué no se escribe, en el prompt. Si el prompt queda igual con o sin el texto, no impacta. Un control que se hace después de escribir no impacta aunque sea obligatorio |
| 2 | Si no impacta: ¿qué es? | Los 8 valores de 1.4 | Uno solo. Se termina aquí; los pasos 3 a 6 no se llenan |
| 3 | Si impacta: efecto | Los 6 valores de 1.2 | Todos los que tenga. El estilo visual es «agrega contenido»; la manera de redactar es «fija la forma» |
| 4 | Si impacta: cómo entra al prompt | Template · Inserción mecánica · Biblioteca de plantillas · Selección | Uno solo, con el árbol de la §4 |
| 5 | Caso de uso (nivel 3) | Valores de cada faceta | Para cada faceta, el valor o los valores a los que la regla se limita. Si la regla no se limita en esa faceta, se marca «todos los valores» |
| 6 | Atributos (nivel 4) | F29, F30, F01, F02, F31, ámbito, uso operativo y metadatos | F29 es obligatorio: el modelo o los modelos para los que vale la regla, o «todos los valores» si no se limita |

## 4. Árbol para «cómo entra al prompt»

1. ¿Es la plantilla de un look concreto (una escena armada con sus huecos)? → **Biblioteca de plantillas.**
2. Si no: ¿se aplica siempre que se usa el modelo o la operación, sin depender de ningún otro dato del caso? →
   **Template** de ese modelo u operación. Si su forma cambia según el modelo, cada template la lleva en la forma del suyo.
3. Si no: ¿su condición se resuelve solo con valores de listas cerradas del caso (tipo de pieza, sujeto, técnica,
   operación, texto en la imagen, momento del día, etc.)? → **Inserción mecánica.**
4. Si no (depende de un número, una edad, una posición, un texto literal o de interpretar el caso) → **Selección.**

## 5. Valores y etiquetas

- **Prohibidos como valor:** «no aplica», «pendiente», «ausente», «no encontrado», «propuesta», «duda» o cualquier
  equivalente (decisión del 23 de octubre §3).
- **Etiquetas:** cada valor usado debe coincidir al 100 % con la taxonomía canónica. Si no coincide, se corrige y se
  repite.

## 6. Dudas y textos que no caben

- Si la duda persiste después de verificar los tres niveles de la §2, se lleva a Eric antes de terminar ese texto.
- Un texto que no cabe en ningún valor se informa a Eric; no se fuerza ni se amplía la taxonomía sin él (decisión del 23
  de octubre §3).

## 7. Registro de cada texto

Un archivo CSV por documento, con una fila por texto:

`id · documento · linea · copia_de · impacta · que_es · efecto · entra · F04 · F10 · F13 · F15 · F16 · F17 · F18 ·
otras_facetas · F29 · F30 · motivo`

- Las facetas sin límite llevan «todos los valores».
- `motivo` dice en una frase qué dice el texto que justifica la clasificación.
- El registro se sube al terminar cada documento.

## 8. Prueba de concordancia antes de clasificar a escala

1. Dos clasificaciones independientes de la misma muestra, con estos criterios y sin ver la otra.
2. Cada desacuerdo se resuelve corrigiendo la definición que lo causó, aquí o en la taxonomía, con aprobación de Eric.
3. Se repite hasta que no haya desacuerdos que vengan de una definición. Solo entonces se clasifica el universo completo.
