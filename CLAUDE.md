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

## Consultar el mapa antes de preguntar o de dar algo por faltante (instrucción de Eric, 2026-10-30)

El mapa (`taller/catalogo/mapa/`) es la memoria del agente, no un documento para Eric. Antes de preguntarle algo a Eric
y antes de afirmar que algo falta, no existe o no está decidido, se consulta `taller/catalogo/mapa/CONSULTA.md`: dónde
está cada cosa, todas sus decisiones con archivo y línea, la explicación verificada de cada documento del corpus y la
lista de archivos del repo. Si la respuesta está ahí, no se pregunta: se lee el archivo que señala y se cita. Las
explicaciones del corpus orientan; lo que vale es siempre el texto original de la base. El índice se regenera con
`taller/catalogo/mapa/herramientas/indice_consulta.py` cada vez que cambia una decisión, un archivo o una explicación.

## Riesgos, pendientes y avance de etapa (decisión de Eric, 2026-10-29)

- Prohibido dejar riesgos abiertos, salvo los que estén totalmente fuera de control del agente. Todo lo demás se
  entrega con su plan de solución ya incluido, con riesgo cero del lado del agente. Si algo es un riesgo fuera de
  control, se dice claramente que lo es y por qué.
- Un riesgo no es una decisión que no se ha tomado ni una contradicción sin resolver: eso son **pendientes**, y se
  presentan como pendientes, con quién los resuelve.
- Prohibido avanzar a una etapa nueva mientras los pendientes de la etapa anterior no estén cubiertos al 100 %, salvo
  que Eric lo autorice expresamente.

## Toda lectura deja registro en el repo

Una lectura no cuenta como hecha sin su registro en el repo: por texto o por sección, qué dice (con su línea) y qué
consecuencia tiene para el trabajo en curso, o por qué no tiene ninguna. El registro se escribe mientras se lee y se sube
al terminar cada documento, para que una compactación del contexto no obligue a volver a leer. Registro vigente: el mapa
(`taller/catalogo/mapa/`), con la explicación verificada de cada documento del corpus en
`taller/catalogo/mapa/documentos/verificado/`. Lo borrado el 2026-10-27 (pruebas, planes, registros, herramientas y
resultados anteriores del agente) se recupera desde el commit anterior a cada borrado: lo de `439ddb5` con `git checkout 77678d8 -- <ruta>`, lo de `dfcc4fb` con `git checkout d54bf46 -- <ruta>` y lo de `d54bf46` con `git checkout 4fed3e8 -- <ruta>`.
