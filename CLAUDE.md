# Instrucciones de proyecto

## Alcance y vocabulario de los prompts

El alcance de las reglas es solo GPT Image 2 (decisión de Eric, 2026-10-24). La palabra «photorealistic» está prohibida
en los prompts.

## Antes de decir que algo no existe

Nunca se afirma que el corpus no tiene una regla, un texto o un dato sin haber leído completos todos los textos que
podrían contenerlo (el universo de la prueba o el documento entero). Buscar por palabras clave no basta y no se presenta
como lectura. Ejemplo del 2026-10-27: a la pregunta «¿hay reglas para la imagen fija de un choque de auto?» se respondió
tras buscar por palabras y leer 63 coincidencias recortadas; la lectura completa de los 2,722 textos
encontró muchas más reglas aplicables que la búsqueda.

## Consultar el mapa antes de preguntar o de dar algo por faltante (instrucción de Eric, 2026-10-30)

El mapa (`6_mapa/`) es la memoria del agente, no un documento para Eric. Antes de preguntarle algo a Eric
y antes de afirmar que algo falta, no existe o no está decidido, se consulta `6_mapa/CONSULTA.md`. Es un índice: cada
archivo del repo con sus secciones y su línea, cada decisión de Eric con archivo y línea, los pendientes y los
documentos del corpus con su utilidad. No repite contenido. Si la respuesta está ahí, no se pregunta: se lee el
archivo que señala y se cita. El índice se regenera con `6_mapa/herramientas/indice_consulta.py` cada vez que cambia
una decisión o un archivo.

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
al terminar cada documento, para que una compactación del contexto no obligue a volver a leer. Registro vigente:
`6_mapa/lecturas/`, un archivo por documento leído.

## Basura, auditorías y registro de cambios (instrucción de Eric, 2026-10-30)

- Se borran todos los archivos basura que genere el agente: la carpeta temporal (scratchpad), las cachés y las copias
  de trabajo. El agente no puede saber cuándo se cierra la sesión, así que lo hace al terminar cada tarea, antes de la
  respuesta final.
- Todo lo que tenga que ver con auditorías y verificaciones va en `7_auditorias_y_verificaciones/`.
- Cada cambio al repo se registra en `CAMBIOS.md`, en el mismo commit que lo hace: fecha, commit, qué cambió y con qué
  orden.
