# Consulta rápida del agente

Se consulta **antes** de preguntarle algo a Eric y **antes** de decir que algo falta, no existe o no está decidido.
Si la respuesta está aquí o en el archivo que señala, no se pregunta: se lee y se cita. Este índice se regenera con
`herramientas/indice_consulta.py` cada vez que cambia una decisión, un archivo del repo o una explicación.

## 1. Dónde está cada cosa

| Duda | Dónde mirar |
|---|---|
| Instrucciones de trabajo vigentes | `CLAUDE.md` (sección 2 de este índice) |
| ¿Eric ya decidió esto? | Sección 2 de este índice: todas las decisiones con archivo y línea. Orden de autoridad: decisiones de Eric → taxonomía 00688 → C18 base → textos del corpus → PLAN_V5, TEMPLATES y CASOS (capítulo 3 §3.1) |
| Pendientes abiertos y quién los resuelve; qué etapa sigue | `taller/catalogo/PENDIENTES.md` |
| Diseño de la aplicación y del procedimiento de clasificación (propuesta del 2026-10-29) | `taller/catalogo/DISENO_APLICACION_Y_CLASIFICACION.md` |
| Objetivo del sistema | PLAN_V5 L29 (capítulo 3 §3.4): aplicación que extrae exhaustivamente las reglas aplicables a un tipo y caso de imagen y las convierte en prompts de apariencia fotográfica al primer intento. El sistema genera prompts; Eric genera las imágenes |
| Qué contiene un documento del corpus | Sección 3 de este índice → su explicación verificada. La explicación orienta; lo que vale es el texto original de la base |
| Texto original de una regla | Base `taller/catalogo/corpus/BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite`, tabla `textos`, por `id` (INV-xxxxxx). Fiel al original: los 206 archivos coinciden por sha256 y los textos coinciden con sus líneas, salvo los HTML, que son el texto visible sin etiquetas (sus números de línea no son líneas del HTML crudo) |
| Taxonomía: bloques, facetas, valores y términos | `fuentes_20261019/00688_…md`; explicada en el capítulo 7 y detallada en el 8 |
| Etapas y flujos | Capítulo 6; taxonomía §2 |
| Matriz de casos | Capítulo 11; `fuentes_20261019/CASOS_OPCIONES_TAXONOMIA_20261019/casos/` |
| Brief, contratos y adaptadores por modelo | Capítulo 12; `fuentes_20261019/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates/` |
| Universalidad | Capítulo 10 |
| Contradicciones del corpus ya resueltas o pendientes | Capítulo 14 §14.3 |
| Prompt de retrato para GPT Image 2 | `produccion/template-retrato-gpt2/` con `armar.py` (CLAUDE.md) |
| Algo borrado del repo | Desde el commit anterior a cada borrado: `439ddb5` → `git checkout 77678d8 -- <ruta>`; `dfcc4fb` → `git checkout d54bf46 -- <ruta>`; `d54bf46` → `git checkout 4fed3e8 -- <ruta>`; qué se borró, en el capítulo 1 §1.4 |
| Estructura del repo | Sección 4 de este índice |


## 2. Decisiones e instrucciones de Eric (literal, con archivo y línea)


### `CLAUDE.md`

- L3 **Alcance y vocabulario de los prompts** — El alcance de las reglas es solo GPT Image 2 (decisión de Eric, 2026-10-24). La palabra «photorealistic» está prohibida
- L8 **Antes de decir que algo no existe** — Nunca se afirma que el corpus no tiene una regla, un texto o un dato sin haber leído completos todos los textos que
- L16 **Consultar el mapa antes de preguntar o de dar algo por faltante (instrucción de Eric, 202…** — El mapa (`taller/catalogo/mapa/`) es la memoria del agente, no un documento para Eric. Antes de preguntarle algo a Eric
- L25 **Riesgos, pendientes y avance de etapa (decisión de Eric, 2026-10-29)** — - Prohibido dejar riesgos abiertos, salvo los que estén totalmente fuera de control del agente. Todo lo demás se
- L35 **Toda lectura deja registro en el repo** — Una lectura no cuenta como hecha sin su registro en el repo: por texto o por sección, qué dice (con su línea) y qué

### `.claude/rules/DECISIONES.md`

- L8 | 1 | Dónde viven las familias de régimen físico, el vocabulario ampliado del linter y su copia parcheada | En el repo, `.claude/rules/regimenes/` y `.claude/hooks/auror…
- L9 | 2 | Alcance del linter aurora | Copia parcheada en el repo. El conteo de palabras nunca bloquea: es advertencia con el presupuesto de la plataforma como referencia. Si…
- L10 | 3 | Bloque de identidad con referencia de persona adjunta | Por rol de la referencia. Keyframe de inicio o fin en imagen a video: no re-describir. Referencia de person…
- L11 | 4 | Taxonomía de la base de reglas | Caso ampliado con LUGAR, EDIF, ANIMAL, OBJ, MULTITUD, ENSAMBLE. Tarea por subproceso, E0.1 a POST.2 | Las 852 clasificaciones exis…
- L12 | 5 | Tarjeta de ancla en la base | Las nueve dimensiones D1 a D9 como facetas multivalor de cada regla | Una pasada de clasificación adicional sobre reglas de imagen y …
- L13 | 6 | Modelo de embeddings | `intfloat/multilingual-e5-large` local, sin API key; la tabla admite añadir OpenAI después | Cubre inglés, español y ruso |
- L14 | 7 | Familias de régimen físico | Nueve familias con esqueleto de nueve secciones: agua en superficie, ruptura de superficie, subacuático, objeto balístico, vehículo, c…
- L15 | 8 | Cómo entran las inferencias | Con etiqueta `[A PRUEBA]`; investigación de campo en foros y tutoriales para confirmar o refutar cada una; un ejercicio real por caso…
- L16 | 9 | Quién clasifica sin NotebookLM | NotebookLM eliminado del flujo por completo. Clasificador de dos capas, determinista por ruta y regex más similitud vectorial con …
- L18 **Principios que salieron de la sesión y quedan como reglas de trabajo** — - La génesis fija solo la parte del sujeto que lleva la identidad; todo lo que la extiende es un paso posterior con esa génesis adjunta como referencia. Rostro T1 antes …

### `taller/catalogo/v2/decisiones/01021_DECISIONES_APLICADAS_20261011_224300.md`

- L15 **Decisión explícita de las 16:56:54.532502 UTC** — Sentinel_d46f126e89e081919ccb3a120d2ce227: anclas/keyframes en ruta de video llevan F26–F28 VALOR o UNIVERSAL, nunca NO APLICA. F11 y flujo separan imagen/video por apli…
- L19 **Verificación documental y límites de capacidad** — REG-000658/660/663: discrepancia de versiones registrada y delimitada por modelo/interfaz, sin trasladar límites del adaptador histórico a otra versión. REG-000714: resp…
- L23 **Cierre del trabajo de candidatas** — Resultado del trabajo de candidatas: se conciliaron las 3.723 aplicaciones, no se fabricó una lista de 509. Se identificaron 1.976 candidatas documentales: 1.967 activas…

### `taller/catalogo/v2/decisiones/01022_DELTA_DECISIONES_CONSOLIDADO_20261011_224300.md`

- L3 **Estado y autorización** — Correcciones solicitadas y aprobadas por el usuario en dos mensajes de esta conversación:
- L11 **Cambios del contrato** — | Identificador estable de categoría | Campo y valor | Definición y alcance | Evidencia |
- L28 **Jerarquías y estados** — TRM-0249 es un término F31 sin valor padre. TRM-0178/0179 se normalizan a destino principal F14 y secundario F20, preservando las columnas previas contradictorias. TRM-0…
- L34 **DEC-000026 y DEC-000027: evidencia disponible y límite** — No se recibió su registro íntegro original en el paquete. Se conserva únicamente lo que viene citado, sin inventar texto, autor, fecha ni ID de mensaje para estas dos de…
- L42 **Registro histórico recibido** — A continuación se conservan literalmente los registros disponibles DEC01–25, con su archivo de procedencia. Duplicados entre DOC01 y L1 se muestran una vez si el texto c…
- L46 **DEC-000001** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L53 **DEC-000002** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L59 **DEC-000003** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L65 **DEC-000004** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L71 **DEC-000005** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L78 **DEC-000006** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L84 **DEC-000007** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L90 **DEC-000008** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L96 **DEC-000009** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L102 **DEC-000010** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L108 **DEC-000011** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L114 **DEC-000012** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L121 **DEC-000013** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L127 **DEC-000014** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L133 **DEC-000015** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L139 **DEC-000016** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L145 **DEC-000017** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L151 **DEC-000018** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L157 **DEC-000019** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L164 **DEC-000020** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L171 **DEC-000021** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L178 **DEC-000022** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L184 **DEC-000023** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L192 **DEC-000024** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L198 **DEC-000025** — Procedencia: review_20261011/baseline/doc01/doc01_canonico_20261005/13_decisiones_del_usuario.csv
- L205 **Decisión adicional explícita: anclas/keyframes, 2026-10-11 16:56:54.532502 UTC** — Mensaje Sentinel_d46f126e89e081919ccb3a120d2ce227, texto literal recibido:
- L216 **Cierre de verificación documental, sin inventar rendimiento actual** — Resolución documental de Nano Banana en esta consolidación: REG-000658/660/663 conservan los identificadores exactos de nano-banana.md:7–9. El adaptador forge histórico …
- L224 **Resultado de aplicación de la decisión de anclas/keyframes** — Resultado del trabajo de candidatas: se conciliaron las 3.723 aplicaciones, no se fabricó una lista de 509. Se identificaron 1.976 candidatas documentales: 1.967 activas…

### `taller/catalogo/v2/decisiones/01062_registro_decisiones_DOC01.md`

- L4 **DEC-000001** — [Mensaje del usuario] esraba ya decididio que si derrnate la clasificacin neneceustabqmos ampliar la taxonomi entoncers lo hacuamos auqi es un claor ejemplp d euq evamos…
- L8 **DEC-000002** — [Mensaje del usuario] tu ;ectura es cirrecta 6.2 solo aplica si no jhat archivo smixs
- L11 **DEC-000003** — [Respuesta del usuario a «¿Qué etapas NO se ejecutan en modo EXPRESS?»] Solo 1 y 2 (literal): la línea 57 dice solo «salta estrategia formal y guion»; las etapas 0, 3 y …
- L14 **DEC-000004** — [Mensaje del usuario] Esta regla practicamente no tiene sentodo porque no hay sustituto, lo que se debe de poner es lo siguinete y es una reg;a de orquestracion si exist…
- L17 **DEC-000005** — [Respuesta del usuario a «Sustitutos de §8: existen 3 … ¿Los mantengo y añado tu regla de escalamiento para todas las sub-skills sin sustituto?»] Mantener los 3 + gate +…
- L21 **DEC-000006** — [Respuesta del usuario a ««los dos» (x6/x_rev4_1) en la regla de los chequeos: ¿a quiénes se refiere?»] Los dos chequeos de video (Recomendado).
- L24 **DEC-000007** — [Respuesta del usuario a «Etapa 0 (brand-lock): ¿se ejecuta cuando es pieza de autor / cliente SIN marca formal?»] No: solo Visual Theme (Recomendado): la Etapa 0 corre …
- L27 **DEC-000008** — [Respuesta del usuario a «Gate de la Etapa 0 (confirmar valores estimados) vs «los demás gates avanzan solos»»] Gate 0 exige OK; en EXPRESS avanzan solos (Recomendado): …
- L30 **DEC-000009** — [Mensaje del usuario] tienes que difremeciar asi, para evitar confuisiiones un film pubicitario es el flijo mqs largo y para ese aplican todas las etapas sin excepcion, …
- L33 **DEC-000010** — [Mensaje del usuario] la durcion no tiene nda que ver el usuaruio debe de elegir
- L36 **DEC-000011** — [Respuesta del usuario a «Tracks y menú inicial: … ¿cómo lo catalogo?»] Texto + decisión que lo reemplaza (Recomendado): las reglas del texto sobre EXPRESS/STANDARD/FILM…
- L39 **DEC-000012** — [Delegación del usuario] y ve si habria otras opciones
- L43 **DEC-000013** — [Respuesta del usuario a «Tres ambigüedades de alcance de DOC01 (x_rev22_1, x_rev22_2, x_r30_4)»] Aprobar las 3 lecturas (Recomendado): (1) la lista de tipos de pieza (s…
- L46 **DEC-000014** — [Respuesta del usuario a «Shots y entrega (x_r30_3/x_rev33_2, x_r28_2, x_r24_1, x_rev22_4)»] Aprobar las 4 lecturas (Recomendado): (1) shots.json es fuente de verdad des…
- L49 **DEC-000015** — [Mensaje del usuario] no el shot nunca se reconsidera amenos que el usuario lo pida, lo que e sustema hace es reevaluar el set de reglas y si fakka una vez mas entonce s…
- L52 **DEC-000016** — [Respuesta del usuario a «Ámbito de reglas de flujo y de prompts (x_r4a_1, x_rev33_3, x_r30_6, x_r30_8)»] Aprobar las 4 lecturas (Recomendado): (1) «si falla, se corrige…
- L55 **DEC-000017** — [Respuesta del usuario a «Etapas y gates (x_rev33_1, x_r4a_2, x_r4a_p1_1, x_r28_3/x_r4a_p1_3, x_rev22_6)»] Aprobar las 5 lecturas (Recomendado): (1) Etapa 1: la regla de…
- L58 **DEC-000018** — [Mensaje del usuario] no se como solucuonar esto pero si debemos de tener un tracking de las versiones y en cuento slaga una nueva debemos de identificar todas lassregkl…
- L61 **DEC-000019** — [Respuesta del usuario a «Precedencia y nombres (x_r30_2, x_r24_3, x_r30_5)»] aqui como no estan instaladas separadamente no hace sentido decir eso no rees?
- L65 **DEC-000020** — [Respuesta del usuario a «Piezas sueltas: descripción (línea 4) vs menú inicial (DEC-000009/012)»] promot suelto d ebidoe no entra eso es un clip uya te lo havia dicho p…
- L69 **DEC-000021** — [Respuesta del usuario a «Reglas del mapa de capas (líneas 28–38): ¿se aplican igual si la sub-skill no está instalada?»] que sub skill no esta instalada
- L73 **DEC-000022** — [Respuesta del usuario a «Clip vs tracks: DEC-000011 excluye las reglas del texto sobre EXPRESS/STANDARD/FILM, pero DEC-000003/008/014/017 describen comportamientos de C…
- L76 **DEC-000023** — [Respuesta del usuario a «En Clip con la Etapa 4 (shot planning) mantenida, ¿qué sub-skill hace el shot planning?»] den serio me estas preguntando eso? eso claramente de…
- L81 **DEC-000024** — [Mensaje del usuario] las licencias la saplicas al sustemna una vez y ya, y no quieor que parezca ningun tipop de TRUBUCION A UN TERCERO EN NINGUN MATEIRLA QE VA AL CLIN…
- L84 **DEC-000025** — [Mensaje del usuario] LPS TEMPLATES DEBEN DE SEHUIRO LA S REGLAS D ESUNTAXIOS D ELOS MODELOS QUE SE APLICNA UNA VEZ AL TEMPLATE Y NO SE VUELVEN A EXTARER

### `taller/catalogo/v2/decisiones/DECISIONES_ERIC_20261023.md`

- L3 1. Alcance de esta fase: solo textos de imagen y GPT Image 2. Universo: los 1,511 textos de `skills/image/**`
- L7 2. La catalogación previa (2026-10-11, 1,887 registros) y la catalogación provisional del 2026-10-23 no se
- L9 3. Ningún texto queda como pendiente, propuesta, duda, NO APLICA ni equivalente. Lo que no cabe en la taxonomía se
- L11 4. Extensiones de la taxonomía aprobadas (se registran aparte de la taxonomía original):
- L29 5. Toda etiqueta usada en la catalogación debe coincidir al 100% con la taxonomía original (o con una extensión
- L31 6. Las pruebas se hacen solo con GPT Image 2; otros modelos se añaden después.
- L32 7. quality en GPT Image 2 (consulta C1 del piloto): la elige el usuario; «medium como punto de partida» y «empieza con
- L34 8. Biblioteca de prompts efectivos (precisada por Eric el 2026-10-23):

### `taller/catalogo/v2/decisiones/DECISIONES_ERIC_20261024.md`

- L7 1. **Alcance del universo de textos** (amplía la decisión 1 de `DECISIONES_ERIC_20261023.md` y responde D2 del plan v3
- L19 2. «SI EXISTE LA CLASIFICACIÓN EN LA TAXONOMÍA ES PORQUE LA REGLA EXISTE EN EL CORPUS».
- L20 3. «EL SOLO HACER LA GENERACIÓN EN DOS PASOS NO ES SUFICIENTE, HAY VARIAS REGLAS MUY ESPECÍFICAS SOBRE EL LENTE Y EL
- L23 4. Método de prueba aprobado el 2026-10-24: bloque armado por casos (universo completo → filtro por caso → controles

### `taller/catalogo/v2/decisiones/DECISIONES_ERIC_20261026.md`

- L5 1. **Cuando un texto da una cifra que no es la de GPT Image 2, vale la cifra que el corpus da para GPT Image 2**, y el
- L14 2. «No estás aprobado para asumir nada, siempre lo verificas»: toda afirmación sobre un texto se comprueba leyendo el
- L16 3. «Siempre que hay una supuesta contradicción o incoherencia tienes que leer exhaustivamente los textos
- L19 4. **Interfaces de GPT Image 2: OpenAI API y fal.ai** (respuesta a la decisión 1 de 6). Manda
- L24 5. **F20 con una sola persona que debe seguir reconocible: «todas»** (decisión 2 de 6). Base: TRM-0175 (taxonomía L1220,
- L27 6. **Extensión F24 + «objeto entero»** (decisión 3 de 6): un objeto completo como sujeto del cuadro. Los 8 valores
- L30 7. **F05 de B1 y B4 deja de ser lista vacía** (decisión 4 de 6; la lista vacía viola taxonomía §1.12.8): B1 (pescadora en
- L33 8. **Interfaz de generación de la prueba: App de ChatGPT para escritorio** (corregido 2026-10-27). Palabras de Eric
- L42 9. **Muestra de auditoría** (2026-10-27): Eric revisa al azar el 10 % del total de reglas marcadas «no aplica» en cada
- L45 10. **Repetición antes de auditar** (2026-10-27): si una imagen sale mal, se genera el mismo prompt por lo menos dos veces
- L50 11. **Longitud del prompt** (2026-10-27): ya estaba decidida (`.claude/rules/DECISIONES.md` decisión 2; T-BRIEF-IMG L355).
- L54 12. **Alcance de la prueba: solo imagen con aspecto de foto real** (2026-10-27). Palabras de Eric: «solo quiero que se
- L62 13. **vision-decomposer y transferencia de estilo son cosas distintas** (2026-10-27). Palabras de Eric: «porque si son
- L67 14. **Caso de descripción de imagen** (2026-10-27, responde la pregunta 2 de `v3/revision/04_preguntas_eric.md`).
- L75 15. **Sin veredicto d en el diagnóstico** (2026-10-27, responde la pregunta 3). Palabras de Eric: «no hay límite de
- L81 16. **Lista de casos de la prueba** (2026-10-27, responde la pregunta 1 de `v3/revision/04_preguntas_eric.md`). Eric
- L90 17. **Boceto o plano a final: 5 casos** (2026-10-27). Eric eligió un caso por cada plantilla fotográfica, igual que en
- L99 18. **Dos textos mal excluidos entran al universo** (2026-10-27). Eric respondió «Sí, meterlos» a la pregunta «¿Meto
- L108 19. **La decisión por sección se mantiene** (2026-10-27, 00:28–00:37 UTC; registrada tarde, el 2026-10-27). Se decidió en

### `taller/catalogo/v2/decisiones/DECISIONES_ERIC_20261027_30.md`

- L7 1. **Objetivo y reparto** (2026-10-27): «EL SISTEMA NO GENERA IMÁGENES, GENERA PROMPTS Y YO HAGO LAS IMÁGENES». El
- L9 2. **Qué se queda en el repo** (2026-10-27): «LOS ARCHIVOS QUE SE QUEDAN SON LOS QUE NECESITAS PARA EL SISTEMA ENTERO,
- L11 3. **No repetir preguntas ya respondidas** (2026-10-27): no volver a preguntar lo que Eric ya contestó en conversaciones
- L13 4. **Planes** (2026-10-27): un plan tiene como máximo 10 pasos, extremadamente claros y sin riesgos sin mitigar.
- L14 5. **Riesgos y pendientes** (2026-10-29): registrado en CLAUDE.md, sección «Riesgos, pendientes y avance de etapa».
- L15 6. **Procedimiento para terminar** (2026-10-29, palabras de Eric resumidas punto por punto):
- L33 7. **Auditoría con prueba** (2026-10-29): Eric pidió auditar 100 textos corregidos y traer prueba de que están
- L36 8. **Nada sin verificar** (2026-10-30): «no me des una aseveración que no has verificado personalmente». Toda
- L39 9. **Para qué es el mapa** (2026-10-30): el mapa es para que el agente lo consulte y no pierda la memoria de las
- L43 10. **PLAN_V5 fuera** (2026-10-30): «no hace sentido que nada dependa de un plan fracasado; ya te dije que necesitamos otro plan». Se
- L46 11. **Borrar lo que el sistema no usa, de forma irrecuperable** (2026-10-30): «cuando digo bórralos no es para que los

### `taller/catalogo/v2/decisiones/DECISIONES_ERIC_RESCATADAS_20261027.md`

- L5 **De `apd/demo/LEEME.md` (líneas 39–40; app apd, 2026-09-28)** — - `| 14 | director (Eric) | D1: CF-MOTOR-SW30 → b (5 slots de GPT Image), política permanente para todo brief |`
- L10 **De `taller/recursos/` (movidos, no copiados, a `taller/catalogo/fuentes_eric_20261021/`)** — - `user_directives.json`: ERIC-B1-PHOTOREALISTIC («Prohibido el término photorealistic en prompts») y

### `taller/catalogo/v2/decisiones/DECISIONES_repo_20260925.md`

- L8 | 1 | Dónde viven las familias de régimen físico, el vocabulario ampliado del linter y su copia parcheada | En el repo, `.claude/rules/regimenes/` y `.claude/hooks/auror…
- L9 | 2 | Alcance del linter aurora | Copia parcheada en el repo. El conteo de palabras nunca bloquea: es advertencia con el presupuesto de la plataforma como referencia. Si…
- L10 | 3 | Bloque de identidad con referencia de persona adjunta | Por rol de la referencia. Keyframe de inicio o fin en imagen a video: no re-describir. Referencia de person…
- L11 | 4 | Taxonomía de la base de reglas | Caso ampliado con LUGAR, EDIF, ANIMAL, OBJ, MULTITUD, ENSAMBLE. Tarea por subproceso, E0.1 a POST.2 | Las 852 clasificaciones exis…
- L12 | 5 | Tarjeta de ancla en la base | Las nueve dimensiones D1 a D9 como facetas multivalor de cada regla | Una pasada de clasificación adicional sobre reglas de imagen y …
- L13 | 6 | Modelo de embeddings | `intfloat/multilingual-e5-large` local, sin API key; la tabla admite añadir OpenAI después | Cubre inglés, español y ruso |
- L14 | 7 | Familias de régimen físico | Nueve familias con esqueleto de nueve secciones: agua en superficie, ruptura de superficie, subacuático, objeto balístico, vehículo, c…
- L15 | 8 | Cómo entran las inferencias | Con etiqueta `[A PRUEBA]`; investigación de campo en foros y tutoriales para confirmar o refutar cada una; un ejercicio real por caso…
- L16 | 9 | Quién clasifica sin NotebookLM | NotebookLM eliminado del flujo por completo. Clasificador de dos capas, determinista por ruta y regex más similitud vectorial con …
- L18 **Principios que salieron de la sesión y quedan como reglas de trabajo** — - La génesis fija solo la parte del sujeto que lleva la identidad; todo lo que la extiende es un paso posterior con esa génesis adjunta como referencia. Rostro T1 antes …

### `taller/catalogo/fuentes_eric_20261021/directivas_taller.json`

- `ERIC-IDIOMA-PROMPT-INGLES`: «en ingles esto es siemore»
- `ERIC-BLOQUES-1-2-NO-TOPE`: «La expectativa de una o dos reglas por bloque sirve para evaluar los filtros, no para imponer un tope ni excluir reglas válidas.»

### `taller/catalogo/fuentes_eric_20261021/user_directives.json`

- `ERIC-B1-PHOTOREALISTIC`: «Prohibido el término photorealistic en prompts»
- `ERIC-DELEGATION-TERMS`: «Se perdió la prohibición explícita del usuario de photorealistic y fotorealista.»

## 3. Documentos del corpus → explicación verificada

| Documento | Explicación | Utilidad |
|---|---|---|
| `flujos/flujo-anclas.html` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L1 | ALTA |
| `flujos/flujo-spot.html` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L51 | ALTA |
| `skills/ai-production-director/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L92 | ALTA |
| `skills/ai-production-director/references/creative-strategy.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L137 | MEDIA |
| `skills/ai-production-director/references/production-package.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L157 | ALTA |
| `skills/ai-video-storyboard/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L175 | ALTA |
| `skills/ai-video-storyboard/examples/tiktok-reel-30s-coffee.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L207 | ALTA |
| `skills/brand-lock-extractor/LICENSE` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L237 | NULA |
| `skills/brand-lock-extractor/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L255 | MEDIA |
| `skills/brand-lock-extractor/brand-packs/README.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L288 | MEDIA |
| `skills/brand-lock-extractor/brand-packs/_template.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L306 | ALTA |
| `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L328 | ALTA |
| `skills/brand-lock-extractor/examples/brand-lock.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L350 | ALTA |
| `skills/brand-lock-extractor/examples/input-brief.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L369 | ALTA |
| `skills/brand-lock-extractor/references/extraction-rubric.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L383 | ALTA |
| `skills/brand-lock-extractor/templates/brand-lock.md.tpl` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L415 | ALTA |
| `skills/brand-lock-extractor/tools/README.md` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L433 | ALTA |
| `skills/brand-lock-extractor/tools/_shotkit.py` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L467 | MEDIA |
| `skills/brand-lock-extractor/tools/_template.py` | `taller/catalogo/mapa/documentos/verificado/lote1.md` L486 | NULA |
| `skills/brand-lock-extractor/tools/check.sh` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L1 | MEDIA |
| `skills/brand-lock-extractor/tools/copy-prompt.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L26 | MEDIA |
| `skills/brand-lock-extractor/tools/shots-to-html.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L49 | MEDIA |
| `skills/brand-lock-extractor/tools/validate_brand_lock.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L80 | MEDIA |
| `skills/brand-lock-extractor/tools/validate_capabilities.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L111 | ALTA |
| `skills/brand-lock-extractor/tools/validate_critique.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L143 | MEDIA |
| `skills/brand-lock-extractor/tools/validate_prompts.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L168 | ALTA |
| `skills/brand-lock-extractor/tools/validate_provenance.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L204 | MEDIA |
| `skills/brand-lock-extractor/tools/validate_schemas.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L244 | MEDIA |
| `skills/brand-lock-extractor/tools/validate_shots.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L259 | MEDIA |
| `skills/brand-lock-extractor/tools/validate_skills.py` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L296 | MEDIA |
| `skills/image/LICENSE` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L311 | NULA |
| `skills/image/NOTICE` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L331 | NULA |
| `skills/image/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L345 | ALTA |
| `skills/image/references/characters.md` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L373 | ALTA |
| `skills/image/references/creative-direction.md` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L392 | ALTA |
| `skills/image/references/dimensional.md` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L408 | ALTA |
| `skills/image/references/editing.md` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L426 | ALTA |
| `skills/image/references/golden-rules.md` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L446 | ALTA |
| `skills/image/references/gpt-image.md` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L473 | ALTA |
| `skills/image/references/models.md` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L497 | ALTA |
| `skills/image/references/multi-panel.md` | `taller/catalogo/mapa/documentos/verificado/lote2.md` L515 | ALTA |
| `skills/image/references/nano-banana.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L1 | ALTA |
| `skills/image/references/patterns/character-design.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L38 | ALTA |
| `skills/image/references/patterns/ecommerce.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L62 | ALTA |
| `skills/image/references/patterns/fashion-editorial.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L86 | ALTA |
| `skills/image/references/patterns/food-beverage.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L110 | ALTA |
| `skills/image/references/patterns/portrait-cinema.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L134 | ALTA |
| `skills/image/references/patterns/poster-illustration.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L158 | ALTA |
| `skills/image/references/patterns/ui-social.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L182 | ALTA |
| `skills/image/references/prompt-framework.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L206 | ALTA |
| `skills/image/references/slides.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L236 | ALTA |
| `skills/image/references/storyboards.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L276 | ALTA |
| `skills/image/references/structural.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L306 | ALTA |
| `skills/image/references/text-rendering.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L336 | ALTA |
| `skills/image/references/vision-decomposer.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L366 | ALTA |
| `skills/screenwriter/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L392 | MEDIA |
| `skills/screenwriter/references/advanced-techniques.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L423 | MEDIA |
| `skills/screenwriter/references/pipeline-integration.md` | `taller/catalogo/mapa/documentos/verificado/lote3.md` L445 | MEDIA |
| `skills/storyboard-architect/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L1 | ALTA |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L44 | ALTA |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/preview.html` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L66 | ALTA |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/run.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L88 | MEDIA |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/shots.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L104 | ALTA |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L127 | ALTA |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/text-overlays.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L145 | MEDIA |
| `skills/storyboard-architect/examples/60s-founder-explainer/preview.html` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L165 | ALTA |
| `skills/storyboard-architect/examples/60s-founder-explainer/run.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L188 | MEDIA |
| `skills/storyboard-architect/examples/60s-founder-explainer/shots.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L204 | ALTA |
| `skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L228 | ALTA |
| `skills/storyboard-architect/examples/60s-founder-explainer/text-overlays.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L246 | MEDIA |
| `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L265 | ALTA |
| `skills/storyboard-architect/examples/shotkit-explainer/preview.html` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L288 | ALTA |
| `skills/storyboard-architect/examples/shotkit-explainer/run.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L309 | MEDIA |
| `skills/storyboard-architect/examples/shotkit-explainer/shots.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L325 | ALTA |
| `skills/storyboard-architect/examples/shotkit-explainer/storyboard.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L347 | ALTA |
| `skills/storyboard-architect/examples/shotkit-explainer/text-overlays.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L365 | MEDIA |
| `skills/storyboard-architect/references/beat-frameworks.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L386 | MEDIA |
| `skills/storyboard-architect/references/on-screen-text.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L404 | ALTA |
| `skills/storyboard-architect/references/shot-grammar.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L427 | ALTA |
| `skills/storyboard-architect/references/timing-rules.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L446 | MEDIA |
| `skills/storyboard-architect/templates/run.schema.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L464 | MEDIA |
| `skills/storyboard-architect/templates/shots.schema.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L485 | MEDIA |
| `skills/storyboard-architect/templates/storyboard.md.tpl` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L505 | MEDIA |
| `skills/storyboard-architect/templates/text-overlays.schema.json` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L523 | ALTA |
| `skills/storyboard-html-preview/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote4.md` L544 | MEDIA |
| `skills/storyboard-html-preview/templates/preview.html.tpl` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L1 | MEDIA |
| `skills/storyboard-html-preview/templates/print.css.tpl` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L20 | MEDIA |
| `skills/storyboard-html-preview/templates/styles.css.tpl` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L39 | MEDIA |
| `skills/video/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L63 | ALTA |
| `skills/video/references/animatic-keyframes.md` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L85 | ALTA |
| `skills/video/references/camera-lighting-vocabulary.md` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L106 | ALTA |
| `skills/video/references/dramaturgy.md` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L129 | ALTA |
| `skills/video/references/fixes-and-skeletons.md` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L156 | ALTA |
| `skills/video/references/kling.md` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L188 | ALTA |
| `skills/video/references/patterns-and-genres.md` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L212 | ALTA |
| `skills/video/references/race-and-speed.md` | `taller/catalogo/mapa/documentos/verificado/lote5.md` L227 | ALTA |
| `skills/video/references/role-modes.md` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L1 | ALTA |
| `skills/video/references/seedance-25.md` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L37 | ALTA |
| `skills/video/references/seedance.md` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L87 | ALTA |
| `skills/video/references/universal-rules.md` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L133 | ALTA |
| `skills/video/references/veo.md` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L177 | ALTA |
| `skills/visual-asset-critic/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L209 | ALTA |
| `skills/visual-asset-critic/examples/critique.accept.json` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L246 | MEDIA |
| `skills/visual-asset-critic/examples/critique.revise.json` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L260 | ALTA |
| `skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot_01.critique.json` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L274 | MEDIA |
| `skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot_02.critique.json` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L289 | ALTA |
| `skills/visual-asset-critic/examples/worked-run/critiques/round-2/shot_02.critique.json` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L304 | MEDIA |
| `skills/visual-asset-critic/examples/worked-run/preview.html` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L319 | MEDIA |
| `skills/visual-asset-critic/examples/worked-run/prompts/round-1/flux.txt` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L335 | ALTA |
| `skills/visual-asset-critic/examples/worked-run/prompts/round-2/revised-flux.txt` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L349 | ALTA |
| `skills/visual-asset-critic/examples/worked-run/run.json` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L362 | MEDIA |
| `skills/visual-asset-critic/examples/worked-run/shots.json` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L378 | MEDIA |
| `skills/visual-asset-critic/examples/worked-run/text-overlays.json` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L392 | MEDIA |
| `skills/visual-asset-critic/references/critique-rubric.md` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L406 | ALTA |
| `skills/visual-asset-critic/templates/critique.schema.json` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L427 | MEDIA |
| `skills/visual-media/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L444 | MEDIA |
| `skills/visual-prompt-forge/SKILL.md` | `taller/catalogo/mapa/documentos/verificado/lote6.md` L478 | ALTA |
| `skills/visual-prompt-forge/adapters/_capabilities.json` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L1 | ALTA |
| `skills/visual-prompt-forge/adapters/capabilities.schema.json` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L28 | MEDIA |
| `skills/visual-prompt-forge/adapters/flux.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L52 | ALTA |
| `skills/visual-prompt-forge/adapters/gpt-image.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L84 | ALTA |
| `skills/visual-prompt-forge/adapters/hailuo.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L114 | ALTA |
| `skills/visual-prompt-forge/adapters/ideogram.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L142 | ALTA |
| `skills/visual-prompt-forge/adapters/kling.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L174 | ALTA |
| `skills/visual-prompt-forge/adapters/midjourney.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L204 | ALTA |
| `skills/visual-prompt-forge/adapters/nano-banana.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L234 | ALTA |
| `skills/visual-prompt-forge/adapters/seedance.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L266 | ALTA |
| `skills/visual-prompt-forge/adapters/seedream.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L294 | ALTA |
| `skills/visual-prompt-forge/adapters/veo.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L326 | ALTA |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L356 | ALTA |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/flux.txt` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L378 | ALTA |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L392 | ALTA |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/ideogram.txt` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L412 | ALTA |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/kling.txt` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L426 | ALTA |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/midjourney.txt` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L440 | ALTA |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/nano-banana.txt` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L454 | ALTA |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/seedream.txt` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L470 | ALTA |
| `skills/visual-prompt-forge/references/consistency-locks.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L484 | ALTA |
| `skills/visual-prompt-forge/references/failure-modes.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L516 | ALTA |
| `skills/visual-prompt-forge/references/prompt-anatomy.md` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L544 | ALTA |
| `skills/visual-prompt-forge/tools/validate_prompts.py` | `taller/catalogo/mapa/documentos/verificado/lote7.md` L570 | ALTA |

Las 65 copias idénticas remiten al original: capítulo 5 §5.2.

## 4. Archivos versionados del repo (100)


**`.claude/rules/`**

- `DECISIONES.md`

**`./`**

- `.gitignore`
- `CLAUDE.md`

**`apd/originales/`**

- `AI_Production_Director_v3.4.0_COMPLETE.zip`
- `SHA256SUMS`
- `flujo-anclas.html`
- `flujo-spot.html`

**`taller/catalogo/`**

- `DISENO_APLICACION_Y_CLASIFICACION.md`
- `ORIGINALES.md`
- `PENDIENTES.md`

**`taller/catalogo/corpus/`**

- `BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite`
- `CORPUS_LITERAL_COMPLETO_13005.jsonl`

**`taller/catalogo/fuentes_20261019/`**

- `00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md`

**`taller/catalogo/fuentes_20261019/CASOS_OPCIONES_TAXONOMIA_20261019/casos/`**

- `README_CASOS_DE_USO.md`
- `bind_templates.py`
- `build_catalog.py`
- `case.schema.json`
- `casos_opciones.sqlite`
- `catalogo_opciones.csv`
- `catalogo_opciones.json`
- `conteos.json`
- `jerarquia_valores.json`
- `manifest_fuentes.json`
- `mapa_facetas_v5.json`
- `mapa_materias_f30_paths.json`
- `mapa_materias_f30_v5.json`
- `relaciones_documentadas.json`
- `rutas_documentadas.json`
- `validar.py`
- `verificacion.json`

**`taller/catalogo/fuentes_20261019/CASOS_OPCIONES_TAXONOMIA_20261019/templates/`**

- `CONTRATO_IMAGEN_ORQUESTACION.schema.json`
- `REGISTRO_DESTINOS_TEMPLATE.json`

**`taller/catalogo/fuentes_20261019/`**

- `PLAN_V5_COMPLETO_TAXONOMIA_TEMPLATES_20261019_054300.md`

**`taller/catalogo/fuentes_20261019/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates/`**

- `CONTRATOS_OPERACION_MODELO.json`
- `CONTRATO_IMAGEN_ORQUESTACION.schema.json`
- `FIELD_MAP.csv`
- `FUENTES_CONTRATOS.json`
- `MANIFIESTO.json`
- `REGISTRO_DESTINOS_TEMPLATE.json`
- `RESULTADOS_PRUEBAS_ESTRUCTURALES.json`
- `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`
- `VERIFICACION_ESTRUCTURAL.json`
- `probar_contratos.py`
- `verificar_templates.py`

**`taller/catalogo/fuentes_eric_20261021/`**

- `MANIFIESTO.json`
- `canonical_sources.json`
- `catalogo_especificas.json`
- `directivas_taller.json`
- `operation_packs.json`
- `template_brief.json`
- `universal_rules.json`
- `user_directives.json`

**`taller/catalogo/mapa/`**

- `00_indice.md`
- `01_archivos_fuera_del_catalogo.md`
- `01_organizacion_y_utilidad.md`
- `02_catalogo_originales_y_decisiones.md`
- `03_corpus_datos.md`
- `04_etapas_datos.md`
- `04a_etapas_explicacion.md`
- `05_documentos_del_corpus.md`
- `05_taxonomia_datos.md`
- `05a_taxonomia_explicacion.md`
- `06_tipos_de_texto.md`
- `07_universalidad.md`
- `08_casos_datos.md`
- `08a_casos_explicacion.md`
- `09_templates_datos.md`
- `09a_templates_explicacion.md`
- `10_metodologia_clasificacion.md`
- `11_veredicto.md`
- `CONSULTA.md`
- `MAPA_ANEXO_DATOS.html`
- `MAPA_ANEXO_DATOS.pdf`
- `MAPA_DEL_REPO.html`
- `MAPA_DEL_REPO.pdf`

**`taller/catalogo/mapa/documentos/verificado/`**

- `lote1.md`
- `lote2.md`
- `lote3.md`
- `lote4.md`
- `lote5.md`
- `lote6.md`
- `lote7.md`

**`taller/catalogo/mapa/herramientas/`**

- `construir_pdf.py`
- `generar_datos.py`
- `indice_consulta.py`
- `taxonomia.json`
- `taxonomia_a_json.py`
- `unir_documentos.py`
- `verificar_capitulos_datos.py`
- `verificar_documentos.py`

**`taller/catalogo/v2/decisiones/`**

- `01021_DECISIONES_APLICADAS_20261011_224300.md`
- `01022_DELTA_DECISIONES_CONSOLIDADO_20261011_224300.md`
- `01062_registro_decisiones_DOC01.md`
- `DECISIONES_ERIC_20261023.md`
- `DECISIONES_ERIC_20261024.md`
- `DECISIONES_ERIC_20261026.md`
- `DECISIONES_ERIC_20261027_30.md`
- `DECISIONES_ERIC_RESCATADAS_20261027.md`
- `DECISIONES_repo_20260925.md`
- `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`
