# Instrucciones de Eric dadas en conversación (2026-10-27 a 2026-10-30)

Registradas por el agente el 2026-10-30 para que no se pierdan. Las palabras de Eric van entre comillas, normalizadas
solo en ortografía (las escribió con errores de tecleo). Las del 27 vienen del resumen de la conversación anterior;
las del 29 y del 30, de esta conversación.

1. **Objetivo y reparto** (2026-10-27): «EL SISTEMA NO GENERA IMÁGENES, GENERA PROMPTS Y YO HAGO LAS IMÁGENES». El
   objetivo del agente es construir el sistema; las imágenes y su entrega son responsabilidad de Eric.
2. **Qué se queda en el repo** (2026-10-27): «LOS ARCHIVOS QUE SE QUEDAN SON LOS QUE NECESITAS PARA EL SISTEMA ENTERO,
   PARA TODAS LAS ETAPAS Y TODOS LOS MODELOS, NO SOLO PARA EL PILOTO». Lo demás se borra.
3. **No repetir preguntas ya respondidas** (2026-10-27): no volver a preguntar lo que Eric ya contestó en conversaciones
   anteriores. Se cumple consultando `taller/catalogo/mapa/CONSULTA.md` (CLAUDE.md).
4. **Planes** (2026-10-27): un plan tiene como máximo 10 pasos, extremadamente claros y sin riesgos sin mitigar.
5. **Riesgos y pendientes** (2026-10-29): registrado en CLAUDE.md, sección «Riesgos, pendientes y avance de etapa».
6. **Procedimiento para terminar** (2026-10-29, palabras de Eric resumidas punto por punto):
   1. Una estructura clara de la aplicación que va a gobernar y ejecutar el sistema, con un flujo claro de la
      experiencia del usuario.
   2. Los textos se clasifican primero por tipo de texto. La primera clasificación es si tienen o no impacto en la
      redacción del brief o del prompt. Después, qué tipo de texto es: reglas de sintaxis o construcción, reglas que
      asignan un valor, otro tipo de reglas (definirlo), reglas de selección o catálogo (sirven para catalogar un caso
      dentro de la taxonomía), ejemplos, tablas o matrices, excepciones que excluyen palabras o valores de la sintaxis,
      etc.
   3. Para todos los textos debe existir de qué documento viene y su taxonomía dentro de ese documento: los
      encabezados bajo los que está, incluidos todos los de mayor jerarquía, no solo el inmediato.
   4. Una tabla con el ID de cada texto en la primera columna y, en las siguientes, todas las columnas que
      correspondan a las categorías de la taxonomía.
   5. La primera ronda de catálogo es mecánica: usa el documento y los encabezados a los que pertenece el texto.
   6. La segunda ronda revisa los textos, una categoría por vez, no todas al mismo tiempo.
   7. La matriz lleva X si aplica para esa categoría y 0 si no; al final todas las celdas deben estar llenas.

   La propuesta del agente que lo desarrolla, pendiente de aprobación, está en
   `taller/catalogo/DISENO_APLICACION_Y_CLASIFICACION.md`.
7. **Auditoría con prueba** (2026-10-29): Eric pidió auditar 100 textos corregidos y traer prueba de que están
   correctos. La prueba es el texto original sacado de la base, al lado de cada corrección
   (`mapa/documentos/auditoria/`).
8. **Nada sin verificar** (2026-10-30): «no me des una aseveración que no has verificado personalmente». Toda
   afirmación del agente se verifica en el archivo o en la base antes de darla. Si no se verificó, se dice que no se
   verificó.
9. **Para qué es el mapa** (2026-10-30): el mapa es para que el agente lo consulte y no pierda la memoria de las
   instrucciones de Eric, de la estructura del repo, de lo que existe y lo que no, y de las decisiones ya tomadas. No se
   da por faltante algo que ya existe ni se repite una decisión tomada. Registrado en CLAUDE.md, sección «Consultar el
   mapa antes de preguntar».
