# Instrucciones de proyecto

## Prompts de retrato para GPT Image 2

Todo prompt de retrato (una persona, sin referencias) para GPT Image 2 se arma con
`produccion/template-retrato-gpt2/armar.py`. No se escribe a mano.

1. Pasar el brief del usuario a un JSON con los campos de `produccion/template-retrato-gpt2/LEEME.md`.
   Copiar la forma de `produccion/template-retrato-gpt2/aprobados-20261024/briefs.json` (seis casos que Eric aprobó
   al primer intento el 2026-10-24).
2. `python3 -I produccion/template-retrato-gpt2/armar.py <briefs.json>`.
3. Si sale con código 1, corregir el campo que nombra el rechazo y repetir. Nunca entregar un prompt rechazado.
4. Entregar el prompt tal como lo escribe `PROMPTS.txt`, con Model `gpt-image-2`, Quality `high` y el Size que indica,
   y aparte la lista de lo que se infirió porque el brief no lo decía.

El alcance de las reglas es solo GPT Image 2 (decisión de Eric, 2026-10-24). La palabra «photorealistic» está prohibida
en los prompts.

## Antes de decir que algo no existe

Nunca se afirma que el corpus no tiene una regla, un texto o un dato sin haber leído completos todos los textos que
podrían contenerlo (el universo de la prueba o el documento entero). Buscar por palabras clave no basta y no se presenta
como lectura. Ejemplo del 2026-10-27: a la pregunta «¿hay reglas para la imagen fija de un choque de auto?» se respondió
tras buscar por palabras y leer 63 coincidencias recortadas; la lectura completa de los 2,722 textos
(archivo borrado el 2026-10-27) encontró muchas más reglas aplicables que la búsqueda.

## Toda lectura deja registro en el repo

Una lectura no cuenta como hecha sin su registro en el repo: por texto o por sección, qué dice (con su línea) y qué
consecuencia tiene para el trabajo en curso, o por qué no tiene ninguna. El registro se escribe mientras se lee y se sube
al terminar cada documento, para que una compactación del contexto no obligue a volver a leer. Registros vigentes:
ninguno. Por instrucción de Eric (2026-10-27) se borró del repo todo lo construido por el agente en el catálogo: pruebas,
planes, registros, herramientas y resultados. Quedan solo los originales y las decisiones de Eric
(`taller/catalogo/ORIGINALES.md`).
