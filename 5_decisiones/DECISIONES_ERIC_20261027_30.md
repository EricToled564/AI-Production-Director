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
   (registro borrado el 2026-10-30 por instrucción de Eric, punto 11).
8. **Nada sin verificar** (2026-10-30): «no me des una aseveración que no has verificado personalmente». Toda
   afirmación del agente se verifica en el archivo o en la base antes de darla. Si no se verificó, se dice que no se
   verificó.
9. **Para qué es el mapa** (2026-10-30): el mapa es para que el agente lo consulte y no pierda la memoria de las
   instrucciones de Eric, de la estructura del repo, de lo que existe y lo que no, y de las decisiones ya tomadas. No se
   da por faltante algo que ya existe ni se repite una decisión tomada. Registrado en CLAUDE.md, sección «Consultar el
   mapa antes de preguntar».
10. **PLAN_V5 fuera** (2026-10-30): «no hace sentido que nada dependa de un plan fracasado; ya te dije que necesitamos otro plan». Se
    borra PLAN_V5 y ningún archivo lo nombra ni depende de él. Su estado era «propuesta consolidada para aprobación» y no
    hay registro de que Eric lo aprobara.
11. **Borrar lo que el sistema no usa, de forma irrecuperable** (2026-10-30): «cuando digo bórralos no es para que los
    escondas en algún archivo para que al rato los puedas recuperar, es borrarlos de forma irrecuperable». Se borraron
    las primeras lecturas y copias del mapa, los registros de verificación y auditoría, los hooks y `settings.json`, y
    `produccion/template-retrato-gpt2/` con sus prompts de prueba. Después, por la misma instrucción, las 9 familias
    de régimen físico y su investigación (`.claude/rules/regimenes/` y `research/`): «bórralos, no lo sigues».
12. **Repo, PLAN_V5, hooks y mapa** (2026-10-30, segunda parte):
    1. Los templates y los casos de uso van en carpetas propias, y el repo se acomoda «de una forma profesional, fácil
       de encontrar y navegar y que haga sentido al desarrollo del sistema». Hecho: carpetas `1_originales/` a
       `6_mapa/` y `LEEME.md`.
    2. De PLAN_V5 se extraen los niveles de generalidad y la jerarquía de lectura a archivos propios, y se borra el
       resto del plan. Hecho: `4_diseno/niveles_de_generalidad.md` y `4_diseno/jerarquia_de_lectura.md`.
    3. «Restaura todos los hooks y ponlos en un archivo en la sección que les corresponde». Hecho:
       `4_diseno/validadores/`. Esto deja sin efecto, para los hooks, el borrado del punto 11.
    4. El mapa tiene que cumplir su función: el agente decide su tamaño, pero debe cubrir todos los puntos que
       contienen los archivos, sin duplicar la información; solo los indexa. Hecho: `6_mapa/CONSULTA.md`.
    5. Sobre el argumento del agente de que borrar los gates dejaba sin ejecutar el paso de validación de los flujos
       originales (INV-000247, INV-000248, INV-000565): «estamos haciendo un sistema nuevo, esto no aplica más». Ese
       paso y sus herramientas no obligan al sistema nuevo. Las reglas que esos gates revisaban siguen en el corpus.
    6. «Todo del sistema anterior se borra, porque por eso te vuelves loco cada vez que revisas algo y metes cosas que no
       tienen nada que ver con el nuevo sistema y perdemos millones de tokens con eso». Hecho: el zip quedó solo con
       `skills/` (`1_originales/AI_Production_Director_v3.4.0_skills.zip`) y se borraron los hooks de
       `4_diseno/validadores/`, lo que deja sin efecto el punto 12.3.
