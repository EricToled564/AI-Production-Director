# Revisión de la estructura: taxonomía y catálogo de casos de uso (2026-10-30)

Orden de Eric: revisar exhaustivamente todas las secciones de la taxonomía junto con el catálogo de casos de uso y dar
una recomendación final de cómo reestructurarla. Sin analizar las reglas y sin parchar nada antes de que Eric decida.

## Qué se revisó

- **Taxonomía.** `3_taxonomia/00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md`: 4,366 líneas,
  sha256 `eacafc25…0565f`. Se leyeron completas todas las líneas que no son filas de término (L1–L4366). Las 2,796
  filas de término (`| TRM-…`) se compararon por programa, columna por columna.
- **Catálogo.** Los 16 archivos de `4_diseno/casos/`:
  - documentación y scripts: el README, `build_catalog.py`, `bind_templates.py`, `validar.py` y `case.schema.json`;
  - mapas: `mapa_facetas.json`, `mapa_materias_f30.json` y `mapa_materias_f30_paths.json`;
  - derivados: `jerarquia_valores.json`, `relaciones_documentadas.json` y `rutas_documentadas.json`;
  - el catálogo en tres formatos: `catalogo_opciones.json`/`.csv` y `casos_opciones.sqlite`;
  - control: `conteos.json` y `manifest_fuentes.json`.
- **Dependencias.** También se revisaron los archivos que dependen de la taxonomía: los templates (`FUENTES_CONTRATOS.json`),
  `4_diseno/*.md`, `5_decisiones/` y `6_mapa/`.

## 1. Qué hay hoy dentro de la taxonomía

La taxonomía mezcla seis clases de contenido. Solo dos son reglas de clasificación.

| Clase | Secciones (líneas) | Líneas | ¿Es regla de clasificación? |
|---|---|---|---|
| A. Reglas de cómo se clasifica | Contrato L5–24 · Seleccionabilidad L25–36 · §0.6 L146–156 · §1 L157–183 · §1.12 L184–201 · §1.13 L202–209 · §5.4 L2584–2587 · §6.2–6.5 L2719–2783 · §7 L2784–2817 · Actualización P-04 L4334–4337 · Gate final L4338–4351 | ≈ 220 | Sí |
| B. Esquema: facetas, valores y términos | §2.1–2.3 L210–264 · §3 L469–813 · §4 L814–1580 · §5.1–5.3 L1581–2583 · §6.0–6.1 L2588–2718 | ≈ 2,300 | Sí (las categorías con las que se clasifica) |
| C. Descripción del corpus | §0.1–0.5 L37–145 | 109 | No: describe el corpus y cuenta la taxonomía |
| D. Copia literal del corpus | §2.4 L265–468 (FL01, FL02, FL03) | 204 | No: son textos del corpus copiados con su localizador |
| E. Procedencia de los términos (conciliación con el borrador) | Anexo 2 L2846–4221 · Anexo 3 L4222–4286 | 1,441 | No: repite los términos del esquema con datos del borrador |
| F. Historia y evidencia de ediciones anteriores | Anexo 1 · Anexo 4 · Anexo 5 · Anexo 6 · Conciliación de citas · Historial C18 · Anexo de tracks · párrafos históricos dentro de §0.5, §0.6 y el Gate final | ≈ 90 | No |

El 40 % del archivo (clases C, D y E, 1,754 líneas) no son reglas de clasificación. La clase F es poca en líneas, pero
es la que trae casi todas las referencias a documentos que no existen.

## 2. Veredicto por sección

| Sección | Líneas | Qué es | Veredicto |
|---|---|---|---|
| Título | L1–4 | Nombre y fecha de la edición; cita C18 | Se queda el título; sale la mención a C18 |
| Contrato vigente | L5–24 | Regla. L20 remite a `DELTA_DECISIONES_CONSOLIDADO_…md`, que existe en `5_decisiones/01022_…` | Se queda; la remisión se cambia a la ruta real |
| Seleccionabilidad obligatoria | L25–36 | Regla. L27 cita dos mensajes Sentinel que no están en el repo (y DEC-000026, que sí está); L31 cita `selector_documental/explicit_decision_exclusions.json`, que no existe | Se queda; salen las dos referencias, la regla no depende de ellas |
| §0.1 Corpus autorizado | L39–76 | Lista de fuentes y de lo excluido del zip con su motivo | Sale de la taxonomía y va a `2_corpus/` |
| §0.2 Inventario literal | L77–100 | Cómo se partió el corpus en unidades. Nombra `inventario_corpus_autorizado.csv` y `representaciones_congeladas/`, que no existen | Sale y va a `2_corpus/`, apuntando a la base `.sqlite`, que es el inventario real |
| §0.3 Inventario por capa | L101–120 | Conteos de facetas, términos y propuestas | Sale: los conteos los da el catálogo (`conteos.json`) |
| §0.4 Conciliación de los 1,369 términos | L121–134 | Conteos de relación con el borrador | Sale: es procedencia |
| §0.5 Respaldo | L135–145 | Define COMPLETO, PRESENCIA y SIN PRESENCIA (se queda) y cuenta los cambios de C15 y C16, con `Cambios_definiciones_C15.json` y `_C16.json`, que no existen (sale) | Se parte: las definiciones pasan a las reglas y la historia sale |
| §0.6 Disposición y límite de activación | L146–156 | Regla. L155 es historia de C15/C16 | Se queda sin el párrafo L155 |
| §1 Principios | L157–183 | Regla | Se queda |
| §1.12 Lectura y clasificación por texto | L184–201 | Regla | Se queda |
| §1.13 Correspondencia con templates | L202–209 | Regla | Se queda |
| §2.1 F1 Etapa · §2.2 F2 Paso | L212–243 | Esquema (10 y 45 valores) | Se queda |
| §2.3 P-01 Flujo | L244–264 | Esquema (FL01–FL04 y pasos D01–D05) | Se queda |
| §2.4 Estructura de los flujos | L265–468 | 178 filas copiadas del corpus, cada una con su INV; de ellas salen 178 de las 183 filas de `rutas_documentadas.json` (las otras 5 salen de §2.3) | Sale; el archivo de rutas se genera desde la base del corpus por INV |
| §3.1–3.8 Bloque B (F3–F9, P-04) | L469–813 | Esquema | Se queda. En F05 L601–602 la columna «Fuente» dice «regímenes 04 y 06» y «regimen 05»: son las filas 04, 05 y 06 de la tabla de régimen físico del corpus (`flujos/flujo-anclas.html`:550–554, INV-000277 a 279), no documentos borrados. Se cambian al formato de cita normal |
| §4.1–4.20 Bloque C (F10–F29) | L814–1580 | Esquema | Se queda |
| §5.1–5.2 Bloque D (F30, P-03, F31) | L1581–2559 | Esquema | Se queda. En §5.1.1, L1614–1616, la columna «Fuente» cita códigos del borrador (F043, F076.S06, F083.S03, F048, F049), que no está en el repo: se cambian por la cita al corpus o salen |
| §5.3 P-05 Ámbito y uso operativo | L2560–2583 | Esquema (8 valores de ámbito y un campo aparte, «uso operativo») | Se queda; el catálogo los junta (ver §4) |
| §5.4 P-02 Autoridad | L2584–2587 | Regla | Se queda |
| §6.0–6.1 Campos de metadatos | L2588–2718 | Esquema (campos y valores de la regla) | Se queda. El título «tomados del borrador» y las menciones a C16 salen |
| §6.2 Precedencias · §6.3 Autoridad · §6.4 P-07 · §6.5 P-06 | L2719–2783 | Regla. L2738 y L2740 citan REG-000658/660/663/714, que son identificadores de una clasificación anterior: no hay registro REG en el repo | Se queda; los REG se cambian por su INV |
| §7.1–7.4 Registro, condiciones, brief, consulta | L2784–2817 | Regla | Se queda |
| Anexo 1 | L2818–2845 | Historia v3 → v4 (códigos A.1–C.18, H-0xx, C16, `Cambios_definiciones_C16.json`) | Sale |
| Anexo 2 | L2846–4221 | Cada uno de los 1,369 términos otra vez (ver §3) | Sale; sus datos únicos se reubican (ver §5) |
| Anexo 3 | L4222–4286 | Los 58 términos SIN PRESENCIA por tercera vez | Sale: la columna «Respaldo» ya lo dice |
| Anexo 4 | L4287–4303 | Estado de P-01 a P-09 y de la aprobación integral, con 8 mensajes Sentinel distintos que no están en ningún archivo del repo, más `ACTA_CANONIZACION_C18.md`, que no existe | Sale después de pasar a `5_decisiones/` lo que hoy solo está aquí (ver §6) |
| Anexo 5 | L4304–4311 | Historia de C11–C17 | Sale |
| Anexo 6 | L4312–4327 | Equivalencias con una taxonomía anterior | Sale |
| Conciliación de citas | L4328–4333 | Historia de un registro externo de 183 correcciones | Sale |
| Actualización P-04 | L4334–4337 | Regla de P-04 | Pasa a §3.8, donde está P-04 |
| Gate final | L4338–4351 | Regla (L4340–4349); el párrafo C17 es historia | Se queda la regla y sale el párrafo |
| Historial C18 | L4352–4355 | Canonización del 2026-10-03, con `ACTA_CANONIZACION_C18.md` y `MANIFIESTO_C18_SHA256.json`, que no existen | Sale después de pasar a `5_decisiones/` el hecho de la canonización |
| Anexo de tracks | L4356–4366 | TRM-0001/0002/0003 (EXPRESS, STANDARD, FILM), históricos por DEC-000022, que sí existe en `5_decisiones/` | Los tres términos pasan a la tabla de F3, marcados como históricos |

## 3. Comprobaciones de las 2,796 filas de término

**Tablas Markdown.** Las 2,796 filas tienen el número de columnas de su encabezado: 1,369 de 10 columnas, 1,369 de 12 y
58 de 6. Los 481 «|» que van dentro de una celda están escapados.

**Términos repetidos.** Cada término está dos veces: una en su tabla de faceta y otra en el Anexo 2. Los 58 SIN PRESENCIA
están tres veces, porque también aparecen en el Anexo 3.

**Columnas comparadas.** Entre la fila de faceta y la del Anexo 2:

- Seis columnas coinciden en los 1,369 términos: ID origen, alias EN, respaldo, cita, destino secundario y ampliación
  editorial.
- La relación con el valor original difiere solo en 3 términos (TRM-1366 a TRM-1368): «EQUIVALENTE → gpt-image-1.5» en la
  faceta, «EQUIVALENTE (valor F29 incorporado)» en el Anexo 2.
- El nombre difiere en 42 términos, siempre por un aclarador que solo está en la tabla de faceta. Ejemplo: «editorial
  (Tipo de pieza)» frente a «editorial».

**Lo que solo está en el Anexo 2:**

- etiqueta y faceta de origen en el borrador (89 facetas de borrador F001 a F090);
- destino (61 valores distintos);
- «Nota / remisión», con texto en 161 términos.

**Lo que solo está en la tabla de faceta:** la definición.

**Destino viejo en el Anexo 2.** En 51 términos el destino del Anexo 2 todavía dice «(valor nuevo propuesto)». Son los
términos de las materias «materialidad y superficie», «puesta en escena y blocking» y «animación», aunque P-03 ya está
aprobada (§5.1.1).

**Ubicación.** En 1,322 términos la faceta de la tabla donde está escrito coincide con la faceta que usa el catálogo. Los
otros 47 son:

- 43 de los campos de metadatos (§6.1);
- 1 de P-04 (TRM-1369);
- los 3 tracks, que solo tienen fila en el anexo histórico.

Estos 47 no son errores: el catálogo les da otro nombre de faceta (METADATOS, PUBLICACION, F03).

## 4. Hallazgos en el catálogo de casos (`4_diseno/casos/`)

**Estado actual.**

- `validar.py` pasa.
- Las 1,729 filas del catálogo, las 473 relaciones y las 183 rutas apuntan hoy a la línea correcta de la taxonomía: cero
  errores, comprobado fila por fila.
- El sha de `manifest_fuentes.json` y de las 1,729 filas es el de la taxonomía actual.

**Problemas de estructura:**

1. **Dos fuentes para el mismo término.** `build_catalog.py`:
   - lee la definición de la tabla de faceta;
   - lee faceta, nombre, relación, respaldo y cita del Anexo 2;
   - corrige a mano 4 términos en el código porque el Anexo 2 tiene el destino viejo: TRM-0178 y TRM-0179 a F14,
     TRM-0249 a F31 y TRM-1369 a PUBLICACION.

   Es decir, la faceta de esos términos la decide el código y no la taxonomía.
2. **Tres archivos sin generador.** `jerarquia_valores.json`, `relaciones_documentadas.json` y `rutas_documentadas.json`
   no los genera ningún script del repo (ninguno los nombra). Guardan números de línea de la taxonomía. Cualquier cambio de
   líneas los deja desfasados, y nada lo detecta.
3. **El catálogo depende de números de línea.** Cada fila guarda `line` y `concordance_line`. Con la estructura actual,
   borrar o añadir una línea obliga a regenerarlo todo. Así pasó en las ediciones de hoy.
4. **AMBITO junta dos cosas.** Tiene 12 filas: los 8 valores de ámbito funcional y los 4 valores del campo «uso operativo»
   (ACTIVO EN SELECCIÓN, INCORPORADA A TEMPLATE, APLICACIÓN EN CONSTRUCCIÓN DE TEMPLATE y APLICACIÓN EN CONTROL O
   ENTREGA). La taxonomía (§5.3) los define como faceta y campo separados.
5. **README desactualizado.**
   - Dice 112 índices documentales y 57 de conciliación; hoy son 111 y 58.
   - Dice 184 rutas; hay 183.
   - En la línea 28 cita «V5», un documento ya borrado.
6. **Restos en los scripts.**
   - `bind_templates.py` define un diccionario `m` que se reemplaza en la línea siguiente sin usarse.
   - `case_selectable` se calcula en dos scripts: `build_catalog.py` para todo y `bind_templates.py` lo rehace para F30.

**Lo que no se cambia en el catálogo:**

- El esquema del caso (`case.schema.json`), los mapas de destino y la vinculación con los templates.
- El papel de F30: es materia de la regla, y además 19 de sus 24 materias se ofrecen como descriptores del caso. El README
  lo documenta («F30 no es por sí misma una condición que descarte una regla»).

## 5. Recomendación final

**Una taxonomía con solo dos partes, cada dato escrito una vez y el catálogo generado entero por script.**

### 5.1 La taxonomía (`3_taxonomia/`)

Un solo archivo con dos partes:

1. **Parte 1. Reglas de clasificación** (unas 220 líneas). Todo el contenido de clase A, sin historia y sin referencias
   a documentos que no estén en el repo, en este orden:
   - alcance y contrato;
   - principios;
   - lectura y clasificación por texto (§1.12);
   - correspondencia con templates (§1.13);
   - seleccionabilidad y disposición (§0.6 y las definiciones de COMPLETO, PRESENCIA y SIN PRESENCIA de §0.5);
   - precedencias, autoridad, P-06 y P-07 (§6.2–6.5);
   - registro, condiciones, brief y consulta (§7);
   - gate de aceptación.

   Cada decisión se cita por su archivo y línea en `5_decisiones/`.
2. **Parte 2. Esquema** (unas 2,300 líneas): las facetas F1 a F31, los valores, P-01 a P-05 y los campos de metadatos,
   en el orden actual. Cada término aparece una sola vez, en la tabla de su faceta, con estas columnas:
   - ID, término (con su aclarador) y alias EN;
   - definición y relación con el valor;
   - respaldo y cita [INV];
   - destino secundario;
   - nota (las 161 notas del Anexo 2).

   Los 3 tracks van en la tabla de F3, marcados como históricos por DEC-000022.

**Qué sale de la taxonomía y adónde va:**

| Sale | Va a | Motivo |
|---|---|---|
| §0.1–0.2 (fuentes, exclusiones del zip con motivo, cómo se partió el corpus) | `2_corpus/LEEME_CORPUS.md`, apuntando a la base `.sqlite` | Describe el corpus, no clasifica |
| §0.3–0.4, conteos de §0.5 | Nada: los cuenta `conteos.json` | Son conteos que envejecen con cada cambio |
| §2.4 | Nada: el texto está en la base del corpus y `rutas_documentadas.json` se genera desde ella por INV | Es copia del corpus |
| Anexo 2: columnas ID origen, etiqueta origen, faceta origen y ampliación editorial no admitida | Se borran | Remiten al borrador F001–F090, que no está en el repo; la ampliación retirada es historia |
| Anexo 2: destino y nota | El destino se borra (es la tabla donde está el término); la nota pasa a la tabla de faceta | Duplicado |
| Anexo 3 | Se borra | Repite la columna Respaldo |
| Anexos 1, 5 y 6, conciliación de citas, párrafo C17 del Gate, L155 | Se borran | Historia de ediciones; citan documentos que no existen |
| Anexo 4 e Historial C18 | Se borran después de pasar a `5_decisiones/` lo que solo está ahí (§6) | Historia; citan 8 mensajes y 2 archivos que no existen |
| Referencias sueltas en secciones que se quedan: C11–C18 en el texto, REG-000658/660/663/714, los dos Sentinel de L27, `selector_documental/…json`, códigos del borrador de L1614–1616 | Se quitan; los REG se cambian por su INV | No resuelven a nada del repo |

### 5.2 El catálogo (`4_diseno/casos/`)

1. `build_catalog.py` lee solo la Parte 2:
   - la faceta de cada término es la tabla donde está escrito, sin correcciones a mano;
   - el nombre es el de la tabla de faceta.
2. El mismo script genera `jerarquia_valores.json` y `relaciones_documentadas.json`, y genera `rutas_documentadas.json`
   desde §2.3 y la base del corpus. Así no queda ningún archivo derivado escrito a mano.
3. Las filas guardan ID, sección y línea, y `validar.py` comprueba en cada corrida que cada línea tiene su ID. Hoy esa
   comprobación no existe; se hizo a mano para este informe.
4. AMBITO queda con sus 8 valores, y «uso operativo» pasa a ser un campo propio con sus 4 valores.
5. `case_selectable` se calcula en un solo lugar.
6. El diccionario sin uso de `bind_templates.py` se borra.
7. El README se corrige: los conteos y la línea de «V5».

### 5.3 Qué cambia y qué no

**El contenido no cambia.** Siguen los mismos 1,369 términos con la misma definición, alias, respaldo, cita y destino
secundario, los mismos 360 valores y los mismos párrafos de regla. Cada párrafo de regla se mueve palabra por palabra;
solo se quitan las referencias de la tabla anterior.

**Sí cambia, y se dice antes de hacerlo:**

- Las líneas y el sha de la taxonomía. Con ellas cambian el sha en `FUENTES_CONTRATOS.json` y en el catálogo, y las citas
  por línea en `4_diseno/jerarquia_de_lectura.md`, `4_diseno/niveles_de_generalidad.md`, `5_decisiones/` y
  `7_auditorias_y_verificaciones/`.
- El nombre en el catálogo de 42 términos: toman el aclarador de la tabla de faceta.
- La relación de TRM-1366 a TRM-1368: queda «EQUIVALENTE → gpt-image-…», la de la tabla de faceta.
- AMBITO baja de 12 a 8 filas, y aparece el campo «uso operativo» con 4.

### 5.4 Cómo se verifica

Antes del commit, un script compara la taxonomía actual con la nueva y debe dar cero diferencias en:

- IDs de término y de valor;
- definición, alias, respaldo, cita, destino secundario y faceta de cada término (contra la faceta del catálogo actual);
- hash de cada párrafo de la Parte 1 frente a su original.

Además:

- El catálogo regenerado debe tener los mismos 1,729 IDs, con las mismas facetas, disposiciones, `case_selectable` y rutas
  de template. Solo pueden diferir los campos de línea, sección y sha, más los cambios listados en §5.3.
- Tienen que pasar `validar.py`, `verificar_templates.py` y `probar_contratos.py`.
- Una búsqueda en todo el repo, fuera del zip, debe dar cero referencias a archivos que no existen.

## 6. Pendientes que resuelve Eric antes de reestructurar

| # | Pendiente | Recomendación del agente |
|---|---|---|
| R-1 | Aprobar la estructura de §5: un archivo con Parte 1 (reglas) y Parte 2 (esquema) | Aprobarla |
| R-2 | Borrar la historia (Anexos 1, 4, 5 y 6, conciliación de citas, Historial C18, párrafos C15–C17) y las columnas de procedencia del borrador | Borrarla. Antes, pasar a `5_decisiones/` lo único que hoy solo está ahí: (a) P-09, «Seedance 2.5 es la versión vigente; la identidad se refiere por imagen» (L4301), que no está en ningún archivo de `5_decisiones/`; (b) la canonización de la taxonomía del 2026-10-03 (L4302 y L4354), que tampoco está. P-08 (Hailuo) también está en §0.3 L113, que sale, así que va igual a `5_decisiones/` |
| R-3 | Sacar §0.1–0.2 a `2_corpus/` y borrar §0.3–0.4 y §2.4 | Hacerlo |
| R-4 | Separar «uso operativo» de AMBITO en el catálogo | Separarlo, como dice §5.3 de la taxonomía |
| R-5 | Nombres de los 42 términos y relación de TRM-1366 a 1368 | Usar los de la tabla de faceta |

Estos pendientes no tienen que ver con las reglas del corpus: son de estructura. Mientras Eric no decida, no se toca nada.

## 7. Hallado de paso, fuera de la taxonomía y del catálogo

- `4_diseno/DISENO_APLICACION_Y_CLASIFICACION.md` L20 dice «13,005 textos»; la base tiene 13,003 desde el borrado de
  INV-000270 e INV-000272.
- La misma tabla, L21, define la celda de la matriz como «X (aplica) o 0 (no aplica)». Es la pertenencia de un texto a una
  categoría, no un estado que saque una regla de la selección. Si Eric quiere evitar la expresión, se cambia por «X (es de
  esta categoría) o 0 (no es)» al reestructurar.
- `CLAUDE.md` pide el registro de lecturas en `6_mapa/lecturas/`, que no existía. Se crea con este informe.
