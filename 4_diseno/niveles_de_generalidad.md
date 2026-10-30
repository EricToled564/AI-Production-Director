# Niveles de generalidad de una regla (universalidad)

Extraído literal de `PLAN_V5_COMPLETO_TAXONOMIA_TEMPLATES_20261019_054300.md` (sha256 `36abfa00f28033c6422342285cd393071a6fade22c2707d62206a29d13e7a493`) el 2026-10-30, por instrucción de Eric, antes de borrar el resto de ese plan. Origen: §13.2, L626–636.

## Texto

Clasificar expresamente, cuando lo permita la fuente:
- Universal para todas las imágenes dentro del alcance.
- Universal para imágenes de un modelo determinado.
- Universal para un tipo de imagen de un modelo y todos sus casos.
- Aplicable a varios casos enumerados de ese modelo y tipo de imagen.
- Específica de modelo, operación, tipo de imagen y caso.
- Combinaciones transversales respaldadas, por ejemplo varios modelos o varios tipos.

«Universal» siempre se interpreta dentro del dominio ya fijado. Una regla universal de un modelo no se extiende a los demás.

## Dónde más aparece, en parte

- `4_diseno/casos/README_CASOS_DE_USO.md` L50, paso 7: «Seleccionar reglas universales y específicas según el alcance real: todas las imágenes, modelo, operación/tipo, conjuntos de casos, caso específico». Tiene los niveles 1 a 5; no nombra las combinaciones transversales.
- `3_taxonomia/00688_…md` §1.2, L161: en cada faceta, VALOR o UNIVERSAL, y «UNIVERSAL no extiende una regla de un modelo a otros ni elimina excepciones».
- `5_decisiones/DECISIONES_ERIC_20261024.md` L11–16: el alcance de la fase por universalidad (universales, parcialmente universales que incluyen GPT Image 2 y específicos de GPT Image 2).
