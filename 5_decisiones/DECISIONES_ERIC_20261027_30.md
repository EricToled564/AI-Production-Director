# Instrucciones de Eric dadas en conversación (2026-10-27 a 2026-10-30)

Registradas por el agente el 2026-10-30 para que no se pierdan. Las palabras de Eric van entre comillas, normalizadas
solo en ortografía (las escribió con errores de tecleo). Las del 27 vienen del resumen de la conversación anterior;
las del 29 y del 30, de esta conversación.

1. **Objetivo y reparto** (2026-10-27): «EL SISTEMA NO GENERA IMÁGENES, GENERA PROMPTS Y YO HAGO LAS IMÁGENES». El
   objetivo del agente es construir el sistema; las imágenes y su entrega son responsabilidad de Eric.
2. **Qué se queda en el repo** (2026-10-27): «LOS ARCHIVOS QUE SE QUEDAN SON LOS QUE NECESITAS PARA EL SISTEMA ENTERO,
   PARA TODAS LAS ETAPAS Y TODOS LOS MODELOS, NO SOLO PARA EL PILOTO». Lo demás se borra.
3. **No repetir preguntas ya respondidas** (2026-10-27): no volver a preguntar lo que Eric ya contestó en conversaciones
   anteriores. Se cumple consultando `6_mapa/CONSULTA.md` (CLAUDE.md).
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
   `4_diseno/DISENO_APLICACION_Y_CLASIFICACION.md`.
7. **Auditoría con prueba** (2026-10-29): Eric pidió auditar 100 textos corregidos y traer prueba de que están
   correctos. La prueba es el texto original sacado de la base, al lado de cada corrección.
8. **Nada sin verificar** (2026-10-30): «no me des una aseveración que no has verificado personalmente». Toda
   afirmación del agente se verifica en el archivo o en la base antes de darla. Si no se verificó, se dice que no se
   verificó.
9. **Para qué es el mapa** (2026-10-30): el mapa es para que el agente lo consulte y no pierda la memoria de las
   instrucciones de Eric, de la estructura del repo, de lo que existe y lo que no, y de las decisiones ya tomadas. No se
   da por faltante algo que ya existe ni se repite una decisión tomada. Registrado en CLAUDE.md, sección «Consultar el
   mapa antes de preguntar».
11. **Borrar de forma irrecuperable** (2026-10-30): «cuando digo bórralos no es para que los escondas en algún archivo
    para que al rato los puedas recuperar, es borrarlos de forma irrecuperable». Lo que Eric ordena borrar se borra
    también del historial de git.
12. **Repo, hooks y mapa** (2026-10-30, segunda parte):
    1. Los templates y los casos de uso van en carpetas propias, y el repo se acomoda «de una forma profesional, fácil
       de encontrar y navegar y que haga sentido al desarrollo del sistema». Hecho: carpetas `1_originales/` a
       `6_mapa/` y `LEEME.md`.
    3. «Restaura todos los hooks y ponlos en un archivo en la sección que les corresponde». Hecho:
       `4_diseno/validadores/`. Esto deja sin efecto, para los hooks, el borrado del punto 11.
    4. El mapa tiene que cumplir su función: el agente decide su tamaño, pero debe cubrir todos los puntos que
       contienen los archivos, sin duplicar la información; solo los indexa. Hecho: `6_mapa/CONSULTA.md`.
    5. Sobre el argumento del agente de que borrar los gates dejaba sin ejecutar el paso de validación de los flujos
       originales (INV-000247, INV-000248, INV-000565): «estamos haciendo un sistema nuevo, esto no aplica más». Ese
       paso y sus herramientas no obligan al sistema nuevo. Las reglas que esos gates revisaban siguen en el corpus.
    6. «Todo del sistema anterior se borra, porque por eso te vuelves loco cada vez que revisas algo y metes cosas que no
       tienen nada que ver con el nuevo sistema y perdemos millones de tokens con eso». Lo precisan los puntos 7 y 9.
    7. Corrección del punto 6: los archivos del zip no se borran hasta revisarlos con Eric, salvo los que él ya ordenó
       borrar.
    9. Los hooks que Eric ordenó restaurar (punto 3) se quedan. El agente los había borrado al aplicar el punto 6, que
       no los incluía; se restauraron el 2026-10-30 en `4_diseno/validadores/`.
       Su `README.md`, que el agente había borrado el 27 de octubre y no restauró con ellos, se restauró el mismo día
       en la misma carpeta, literal, por orden de Eric.
13. **Basura, auditorías y registro de cambios** (2026-10-30): borrar siempre los archivos basura que se generen; una
    carpeta en el repo para auditorías y verificaciones, con todo lo que tenga que ver con eso; un registro de cambios
    en el que se anota cada cambio a partir de que el contenido del repo se dio por bueno. Registrado en `CLAUDE.md`;
    carpeta `7_auditorias_y_verificaciones/`; registro `CAMBIOS.md`.
14. **Ninguna referencia a documentos borrados** (2026-10-30): se borran todos los documentos que Eric ordenó borrar y toda
    referencia a ellos, sin excepción, también en la taxonomía, el catálogo de casos, el corpus y los flujos originales.
    El zip no se modifica salvo lo que Eric ordenó. Para los textos borrados queda sin efecto que la base del corpus no se
    modifica (26-oct, punto 1).
