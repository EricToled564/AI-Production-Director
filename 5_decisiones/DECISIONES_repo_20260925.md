# Decisiones de dirección — 2026-09-25

Ocho decisiones tomadas una por una por Eric Toledano en la sesión del 25 de septiembre de 2026.
No se reabren en medio de un proyecto; se cambian aquí, con fecha, si cambian.

| # | Decisión | Opción elegida | Consecuencia operativa |
|---|---|---|---|
| 1 | Dónde viven las familias de régimen físico, el vocabulario ampliado del linter y su copia parcheada | En el repo, `.claude/rules/regimenes/` y `.claude/hooks/aurora/`; `rule_registry.py` lee la carpeta del repo además de los skills instalados | Versionado en git, auditable por PR; se empaqueta como skill cuando esté canonizado |
| 2 | Alcance del linter aurora | Copia parcheada en el repo. El conteo de palabras nunca bloquea: es advertencia con el presupuesto de la plataforma como referencia. Siguen bloqueando redundancia con referencias, vocabulario prohibido y secciones requeridas | Los templates de 250 palabras de SW30 y los prompts de 5 slots de GPT Image pasan |
| 3 | Bloque de identidad con referencia de persona adjunta | Por rol de la referencia. Keyframe de inicio o fin en imagen a video: no re-describir. Referencia de personaje sin start frame, casos con @img, Elements o ancla con refs: bloque de identidad completo y verbatim | Resuelve la contradicción entre U7, Seedance §10, forge Rule 3 y Kling §10, Veo §7, Seedance §13, SW30 R5 y R16 |
| 4 | Taxonomía de la base de reglas | Caso ampliado con LUGAR, EDIF, ANIMAL, OBJ, MULTITUD, ENSAMBLE. Tarea por subproceso, E0.1 a POST.2 | Las 852 clasificaciones existentes se importan tal cual; los códigos nuevos se clasifican con el clasificador de dos capas de la decisión 9 |
| 5 | Tarjeta de ancla en la base | Las nueve dimensiones D1 a D9 como facetas multivalor de cada regla | Una pasada de clasificación adicional sobre reglas de imagen y video |
| 6 | Modelo de embeddings | `intfloat/multilingual-e5-large` local, sin API key; la tabla admite añadir OpenAI después | Cubre inglés, español y ruso |
| 7 | Familias de régimen físico | Nueve familias con esqueleto de nueve secciones: agua en superficie, ruptura de superficie, subacuático, objeto balístico, vehículo, cuerpo en esfuerzo, luz y clima, multitud anónima, grupo ensamble | Cada regla etiquetada FUENTE o A PRUEBA |
| 8 | Cómo entran las inferencias | Con etiqueta `[A PRUEBA]`; investigación de campo en foros y tutoriales para confirmar o refutar cada una; un ejercicio real por caso; se canonizan según el resultado | Nunca bloquean un gate hasta ser canónicas |
| 9 | Quién clasifica sin NotebookLM | NotebookLM eliminado del flujo por completo. Clasificador de dos capas, determinista por ruta y regex más similitud vectorial con confianza, y auditoría de Eric en hoja xlsx cuyo veredicto manda | Se retiran el servidor MCP, los scripts nblm_* , rule_export.py y el corpus; rule_answer_check.py se conserva para medir cobertura de cualquier respuesta |

## Principios que salieron de la sesión y quedan como reglas de trabajo

- La génesis fija solo la parte del sujeto que lleva la identidad; todo lo que la extiende es un paso posterior con esa génesis adjunta como referencia. Rostro T1 antes que cuerpo T2, siempre.
- Multitud anónima y grupo ensamble son técnicas distintas, no dos tamaños de la misma. En la multitud nadie tiene rostro legible; en el ensamble todos.
- El ángulo de cámara es una dimensión de decisión propia, D9, elegida por la dinámica de poder del beat, nunca por variedad.
- Un producto con logo o etiqueta real no nace de texto: es flujo con referencia.
- Cuando una regla puede codificarse, se codifica; pero un límite de longitud es dirección, no bloqueo.

## Cambios

Registrados por el agente el 2026-10-30, según la regla de la línea 4. Las filas de arriba conservan el texto original.

| # | Qué ya no corresponde al repo | Desde cuándo y por qué |
|---|---|---|
| 1 | `.claude/hooks/aurora/` y `rule_registry.py` ya no existen | Borrados el 2026-10-27 por orden de Eric de dejar solo lo que necesita el sistema (commit `163e903`) |
| 1 y 7 | Las nueve familias de régimen físico y `.claude/rules/regimenes/` ya no existen, tampoco su investigación (`research/`) | Borradas el 2026-10-30 por orden de Eric («bórralos, no lo sigues»), y borradas del historial de `main` el mismo día. Siguen en la rama `wip-verificacion`, que no se ha reescrito. Los valores de la faceta 14 (régimen físico) siguen en la taxonomía 00688 |
| 2 | La copia parcheada del linter aurora ya no existe | Borrada el 2026-10-27 (commit `163e903`). El 2026-10-30 Eric ordenó borrar todo el sistema anterior. Que la longitud no bloquea sigue vigente: decisión del 26-oct (`5_decisiones/DECISIONES_ERIC_20261026.md`) y el último principio de este archivo |
| 9 | `rule_answer_check.py` ya no existe, aunque esta fila dice que «se conserva» | Borrado el 2026-10-27 con los scripts `rule_*` (commit `163e903`) |
