# Taxonomía: lo que se queda, lo que sale y sirve, lo que sale y no sirve (2026-10-30)

Orden de Eric: la taxonomía son solo las reglas y las categorías de clasificación. Nada de orígenes, archivos ni nada
más. Lo que sale va en dos listas: la de lo que sirve (con su destino) y la de lo que no sirve (para revisarla y
borrarla). Nada se mueve ni se borra hasta el OK de Eric.

Archivo: `3_taxonomia/00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md` (4,366 líneas). Las líneas
son las de hoy.

## Lo que se queda (esto es la taxonomía)

**Categorías:**
- Facetas F1 a F31 con sus valores y definiciones.
- P-01: flujos FL01–FL04 y pasos D01–D05.
- P-03: los tres valores nuevos de F30.
- P-04: lugar de publicación.
- P-05: ámbito funcional y el campo «uso operativo».
- Los 19 campos de metadatos (§6.0) y sus valores (§6.1).

**Términos:** los 1,369, cada uno una sola vez, en la tabla de su faceta. Los tres tracks (TRM-0001 a 0003) pasan a la
tabla de F3. Columnas:
- ID, término y alias en inglés;
- definición;
- relación con el valor y destino secundario;
- respaldo: se queda porque decide si el término se ofrece como opción (§0.6);
- nota: las 97 notas que explican la ubicación del término o lo remiten a otro. Las 17 que remiten a otro término están
  leídas. Las otras 80 están clasificadas por los patrones más frecuentes, no leídas una por una: se leen completas
  antes de ejecutar.

**Reglas de clasificación:**
- contrato: L13, sobre ORQUESTACIÓN;
- seleccionabilidad: puntos 1–4 y 7;
- §0.5: las definiciones de los niveles de respaldo (L137–142);
- §0.6: L150–153;
- §1: 1.1 a 1.9 y 1.11, con la decisión de F26–F28 una sola vez;
- §1.12;
- §5.4;
- §6.2 y §6.3: solo las dos frases que son regla. Un conflicto entre fuentes se registra con las dos reglas, nunca una;
  la autoridad vale para su materia y no es prioridad absoluta;
- §7.1 y §7.2;
- gate final: L4340–4347.

## Lista 1. Sale de la taxonomía y sirve

| # | Qué es | Líneas | Va a |
|---|---|---|---|
| 1 | Qué documentos son corpus y qué archivos del zip quedan fuera, con su motivo | §0.1 L39–76 | `2_corpus/LEEME_CORPUS.md` |
| 2 | Cómo se partió el corpus en textos: tipos de unidad y datos de cada texto | §0.2 L77–100 | `2_corpus/LEEME_CORPUS.md` |
| 3 | Paginación de 50 líneas (P-06): cómo se calcula la página de cada texto | §6.5 L2780–2783 | `2_corpus/LEEME_CORPUS.md` |
| 4 | Estado de las decisiones P-01 a P-09 y la canonización de la taxonomía del 2026-10-03. Hoy solo están en la taxonomía, salvo P-05; si se borran sin pasarlas se pierden | Anexo 4 L4291–4302 · §0.3 L105–114 · Historial L4352–4355 | `5_decisiones/` (archivo nuevo), sin los Sentinel |
| 5 | P-07: Aurora excluida y en su lugar los dos checks de video; la tabla de qué controles cubren las fuentes | §6.4 L2764–2779 | La decisión a `5_decisiones/`; la tabla a `4_diseno/` |
| 6 | Cita al corpus de cada término | Columna «Cita en fuente autorizada [unidad]», 1,369 filas | `3_taxonomia/respaldo_en_corpus.csv` |
| 7 | Fuentes de facetas y valores | Paréntesis de 21 títulos de faceta (L212, 228, 634, 674, 693, 748, 816, 934, 959, 1002, 1059, 1105, 1145, 1188, 1324, 1354, 1392, 1453, 1503, 1534, 2742) · columnas «Fuente» (L488, L507, L599), «Base» (L246) y «Fuentes [unidad]» (L790) · localizadores dentro de L503, L653, L792–802, L1070, L2558, L2594, L2630, L2684 | `3_taxonomia/respaldo_en_corpus.csv` |
| 8 | Las 12 precedencias entre documentos, los conflictos entre fuentes (Kling, Nano Banana) y la tabla de autoridad del director: son textos del corpus que se usan al seleccionar reglas | §6.2 L2721–2740 · §6.3 L2746–2762 | `4_diseno/precedencias_y_autoridad.md`, con los REG cambiados por su INV |
| 9 | Reglas para seleccionar reglas y completar el brief, no para clasificar | §1.10 · §7.3 · §7.4 · seleccionabilidad, puntos 5 y 6 (L33–34) | `4_diseno/reglas_de_seleccion.md` |
| 10 | Regla de correspondencia entre la clasificación y los templates | §1.13 L202–209 | `4_diseno/templates/` |

## Lista 2. Sale de la taxonomía y no sirve (para revisar y borrar)

| # | Qué es | Líneas |
|---|---|---|
| 1 | Párrafos sobre ediciones (C18, delta, aprobación histórica del paquete anterior) | L3, L7, L18, L20 |
| 2 | Repeticiones de lo que ya dicen las tablas o §1 | L9–12, L14–16 |
| 3 | Líneas «Autoridad: Sentinel…» y prefijos «Decisión del usuario … Sentinel». Son 15 mensajes distintos; 13 no están en ningún archivo del repo | L27, L166 (solo el prefijo), L186, L204 |
| 4 | La misma decisión de F26–F28 copiada tres veces más | L1394, L1455, L1505 |
| 5 | Mención a `selector_documental/explicit_decision_exclusions.json`, que no existe | L31 |
| 6 | Conteos y estados de la taxonomía | §0.3 L101–120 (salvo lo que pasa en la lista 1) · §0.4 L121–134 · §0.5 L143–145 |
| 7 | Columnas de un CSV que no existe; historia de C15 y C16 con `Cambios_definiciones_C15/C16.json` | §0.6 L148, L155 |
| 8 | Copia literal de textos del corpus: el texto está en la base y `rutas_documentadas.json` se genera desde ella | §2.4 L265–468 |
| 9 | Restos de ediciones dentro de las categorías: «aprobación integral C18» (L159, L253); aviso de tracks (L479); «Corrección v4 (punto 14)» (L937, L1033, L1210); «Nota de consolidación» (L2538); «tomados del borrador» (L2614); «añadido en C16» (L2630, L2684); «(incluye delta DOC01)» (L2659); fechas de edición en los títulos (L1, L25, L184, L202) | Las líneas indicadas |
| 10 | Conteos «Términos colgados de esta faceta: N» y «Términos del tesauro conciliados: 1» | 28 líneas y L812 |
| 11 | Columnas del borrador en P-03: «Origen en el borrador» (F043, F048, F049…) y «Términos asociados en tesauro» | L1612–1616 |
| 12 | Columna «ID origen», el ID en el borrador F001–F090, que no está en el repo | 1,369 filas |
| 13 | Columna «Ampliación editorial no admitida (historial en CSV)»: textos retirados en ediciones anteriores | 1,369 filas, 169 con texto |
| 14 | Prefijo «Reubicado por revisión desde faceta X» de 64 notas (la explicación de cada nota se queda) | 64 filas |
| 15 | Anexo 1: cambios v3 → v4 | L2818–2845 |
| 16 | Anexo 2: la segunda copia de los 1,369 términos, con etiqueta, faceta y destino del borrador, y las remisiones del borrador (L4220) | L2846–4221 |
| 17 | Anexo 3: tercera copia de los 58 términos sin presencia | L4222–4286 |
| 18 | Anexo 4 (salvo lo que pasa en la lista 1): mensajes Sentinel y `ACTA_CANONIZACION_C18.md` | L4287–4303 |
| 19 | Anexo 5: comprobaciones de C11–C17 | L4304–4311 |
| 20 | Anexo 6: equivalencias con una taxonomía anterior | L4312–4327 |
| 21 | Conciliación de citas y actualización P-04 (historia; lo que vale ya está en §3.8) | L4328–4337 |
| 22 | Gate final: el párrafo de que no certifica y el de C17 | L4349, L4351 |
| 23 | Historial C18 (salvo la canonización, que pasa en la lista 1), con `MANIFIESTO_C18_SHA256.json` | L4352–4355 |
| 24 | Anexo de tracks: el texto con REG-000034 a 049 y la tabla, una vez pasados los tres términos a F3 | L4356–4366 |
| 25 | Números de decisión DEC dentro de las categorías. Las decisiones están en `5_decisiones/`; en la taxonomía son origen. Faltaban en la primera versión de esta lista | L226 (DEC-000026) · L471, L476, L477, L829 (DEC-000022) · L2578 (DEC-000025) |

## Coincidencia entre el catálogo de casos y la taxonomía (verificado el 2026-10-30, registro por registro)

**Coincide:**
- De los 1,369 términos, 1,366 tienen en el catálogo la misma definición, alias, respaldo y cita que en la taxonomía.
- Los 360 valores del catálogo están en su línea de la taxonomía con su nombre.
- Todos los valores de las tablas de categorías de la taxonomía están en el catálogo, salvo los 5 de abajo.

**No coincide (7 diferencias; la primera versión de esta lista decía 4 y omitía las 5, 6 y 7):**

1. **TRM-0001, 0002 y 0003 (EXPRESS, STANDARD, FILM).** En el catálogo su definición es «—»; la taxonomía sí la tiene
   (L4362–4364). El script no lee el anexo de tracks y toma por error otra columna del Anexo 2.
2. **Los pasos D01–D05 de FL04 (L257–261).** No están en el catálogo como opciones; solo en `rutas_documentadas.json`.
3. **AMBITO.** Mezcla los 8 valores de ámbito con los 4 del campo «uso operativo», que la taxonomía define aparte (§5.3).
4. **Los 19 campos de metadatos de §6.0.** No están en el catálogo como registros; sí sus valores.
5. **42 nombres de término.** El catálogo usa el nombre del Anexo 2, sin el aclarador que tiene la tabla de faceta
   (ejemplo: «editorial» frente a «editorial (Tipo de pieza)»).
6. **Relación de TRM-1366 a 1368.** El catálogo usa la del Anexo 2 («EQUIVALENTE (valor F29 incorporado)»); la tabla de
   faceta dice «EQUIVALENTE → gpt-image-…».
7. **Definición de los 16 valores de modelo de F29.** La escribió el script («Modelo documentado de rama …»); no está
   en la taxonomía.

No es diferencia, pero conviene saberlo: los 45 pasos de F02 no tienen definición en la taxonomía, y el catálogo pone
como definición su propio nombre.

**Lo que falta en los dos:** las facetas F32–F35 y los valores nuevos de las decisiones de Eric del 23 y el 26 de octubre
(`5_decisiones/DECISIONES_ERIC_20261023.md` L12–25). Es el pendiente P-06. Además, en la taxonomía «faceta 32» nombra hoy
otra cosa: una faceta retirada en septiembre (L106 y L4294). Esa mención sale con la lista 2.

Ninguna se corrige sola: las siete se corrigen cambiando `build_catalog.py` para que lea la taxonomía nueva. La primera
versión de este archivo decía que la 1 y la 3 se corregían solas, y era falso.

## Forma más barata y rápida de hacerlo

1. **Un solo script hace la taxonomía nueva** a partir de la actual. Borra por rangos de líneas los anexos y las
   secciones de la lista 2, y quita por columnas «ID origen» y «Ampliación editorial». Así no se reescribe a mano.
2. **Tres archivos de destino en vez de siete**, con los textos movidos tal cual:
   - `5_decisiones/` para P-01 a P-09 y la canonización;
   - `2_corpus/` para §0.1, §0.2 y la paginación;
   - un solo archivo en `4_diseno/` para precedencias, autoridad, P-07, reglas de selección y la correspondencia con
     templates.
3. **El respaldo de cada término** (ID, respaldo y cita) sale a un CSV generado por el mismo script.
4. **`build_catalog.py`** lee solo las tablas de faceta. Se quitan la lectura del Anexo 2 y las cuatro facetas fijadas a
   mano, y el script genera también los tres archivos derivados.
5. **Un script de comparación** verifica que no cambie ningún contenido.
6. **Los informes viejos de `7_auditorias_y_verificaciones/`** no se reescriben: citan la taxonomía con su sha, que
   identifica la versión que auditaron. Solo se actualizan las citas por línea en `4_diseno/jerarquia_de_lectura.md`,
   `4_diseno/niveles_de_generalidad.md` y `4_diseno/DISENO_APLICACION_Y_CLASIFICACION.md`.
