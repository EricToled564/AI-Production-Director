# Diseño de la aplicación y del procedimiento de clasificación

Propuesta para aprobación de Eric. Recoge su instrucción del 2026-10-29 y la monta sobre:
- la jerarquía de lectura (`4_diseno/jerarquia_de_lectura.md`) y los niveles de generalidad (`4_diseno/niveles_de_generalidad.md`);
- el paquete TEMPLATES (brief T-BRIEF-IMG, contratos por operación, adaptadores por modelo y orquestación T-ORQ);
- el paquete CASOS;
- la taxonomía canónica (`3_taxonomia/TAXONOMIA_CANONICA.md`), que desde el 2026-10-31 reemplaza a la 00688;
- las decisiones del 23, 24 y 26 de octubre.

Lo que la instrucción del 29 cambia del diseño anterior está marcado **[NUEVO 29-oct]**. Lo que queda por decidir está en la §4 como pendiente, con su propuesta.

El sistema no genera imágenes: genera prompts. Eric genera las imágenes y las entrega.

---

## 1. La aplicación: qué partes tiene

| Parte | Qué hace | Sobre qué está hecha |
|---|---|---|
| **A. Corpus** | Guarda los 13,005 textos con su documento y su ruta completa de encabezados | Base del corpus y originales |
| **B. Matriz de clasificación** | Una fila por texto. Columnas: tipo de texto y cada categoría de la taxonomía. Cada celda vale X (aplica) o 0 (no aplica) | Taxonomía 00688 y catálogo CASOS |
| **C. Consola de clasificación** (gobierno) | Ejecuta las rondas, muestra el avance celda por celda, las auditorías y los pendientes. Ninguna ronda avanza con pendientes abiertos | `PENDIENTES.md` |
| **D. Brief** | Formulario del contrato T-BRIEF-IMG. Cada valor guarda su origen: lo dio el usuario, lo hereda de un documento o es una inferencia propuesta | TEMPLATES §3, `case.schema.json` |
| **E. Catalogador de caso** | Ubica el pedido dentro de la taxonomía, usando las columnas de la matriz marcadas como reglas de selección o catálogo | Matriz B, CASOS |
| **F. Selector de reglas** | Lee la matriz y da a cada regla una sola salida: excluida por decisión, fuera de este caso o aplicable confirmada | Taxonomía §7.4 |
| **G. Compilador** | Arma el prompt con las reglas aplicables, en el contrato de la operación y el adaptador del modelo (para GPT Image 2: GPT2-GEN o GPT2-EDIT) | TEMPLATES §5–§6 |
| **H. Validadores** | Comprueban el prompt antes de entregarlo: vocabulario prohibido (incluida «photorealistic»), secciones, ratio en el Scene y longitud (solo aviso) | Decisiones de Eric y reglas del corpus clasificado |
| **I. Biblioteca de prompts efectivos** | Guarda el prompt aprobado con su traza. Si un brief nuevo se parece al menos en un 85 % a uno guardado, sugiere reusar su prompt | Decisión 23 §8 |
| **J. Traza** | Une cada regla aplicada con su texto original, su condición, el campo del brief y su efecto en el prompt | T-TRAZA, `binding_contract` |

## 2. La experiencia del usuario: el flujo de un pedido

Los pasos 1–6 y el 8 ocurren dentro de la aplicación. El paso 7 lo hace Eric fuera de ella.

| Paso | Qué ve y qué hace Eric | Qué hace la aplicación |
|---|---|---|
| 1. Nuevo pedido | Escribe el pedido en español | Detecta la operación (génesis, edición, composición, ancla, estilo, boceto) y el modelo. Hoy el único modelo es GPT Image 2 |
| 2. Brief | Ve el formulario ya prellenado y solo completa lo que falta | Prellena con lo que dijo Eric y lo que heredan los documentos aprobados. Marca cada inferencia como propuesta y pide cada dato que decide una regla |
| 3. Caso | Ve la ubicación del pedido en la taxonomía, faceta por faceta, y la confirma | El catalogador de caso (E) la arma con las reglas de selección |
| 4. Aprobación | Aprueba el brief completo | Registra la aprobación ligada al hash del brief. Antes de este paso no se seleccionan reglas (TEMPLATES §2) |
| 5. Reglas | Ve las reglas aplicables, cada una con su texto original, su documento y por qué aplica. Las que no aplican también se ven, con su motivo | El selector (F) recorre toda la matriz |
| 6. Prompt | Recibe el prompt en inglés, listo para pegar en la app de ChatGPT de escritorio. El ratio va dentro del Scene; model, quality y size van aparte | El compilador (G) lo arma y los validadores (H) lo comprueban. Si falla una validación, no se entrega |
| 7. Generación | Genera la imagen en la app de ChatGPT | — |
| 8. Resultado | Sube la imagen y da su veredicto | Hace la crítica contra el brief. Si Eric aprueba, guarda el prompt en la biblioteca (I) con su traza |

## 3. Procedimiento de clasificación [NUEVO 29-oct]

### 3.0 Estructura de cada texto (mecánica, antes de clasificar)

Cada texto tiene que llevar su documento y su **ruta completa de encabezados**: todos los encabezados de mayor jerarquía de los que depende, no solo el inmediato.

- **Estado actual.** La base guarda la ruta completa (h1 › h2 › h3) en los documentos Markdown. Pero **6,068 de los 13,005 textos (130 archivos) no tienen ningún encabezado**:
  - los dos flujos HTML, cuyos originales sí tienen h1, h2 y h3;
  - los JSON y los esquemas, que tienen la ruta de claves;
  - el código Python, que tiene módulo, clase y función;
  - los ejemplos y las plantillas.
- **Cómo se cierra.** Un programa reconstruye la ruta a partir del archivo original de cada texto:
  - en HTML, por h1–h6 y la sección o tabla que lo contiene;
  - en JSON, por la ruta de claves;
  - en Python, por clase y función;
  - en Markdown, por el encabezado de cada nivel.

  Se comprueba que el 100 % de los textos quede con documento y ruta, o con «sin estructura interna» declarado y justificado (por ejemplo, una licencia de un solo bloque).

### 3.1 Ronda de tipo de texto

Primero, para cada uno de los 13,005 textos:

1. **¿Tiene impacto en la redacción del brief o del prompt?** X o 0.
2. **¿Qué tipo de texto es?** Una columna por tipo, con X o 0; un texto puede ser de más de un tipo. Lista propuesta, ajustada a lo que pidió Eric:

| Código | Tipo | Definición |
|---|---|---|
| T-SIN | Regla de sintaxis o construcción | Dice cómo se escribe o se ordena el brief o el prompt: estructura, slots, orden, longitud, forma |
| T-VAL | Regla que asigna un valor | Fija el valor de un campo o parámetro: ratio, quality, size, lente, luz, número de referencias |
| T-SEL | Regla de selección o catálogo | Sirve para catalogar un caso dentro de la taxonomía o para elegir modelo, operación o técnica |
| T-EXC | Excepción o exclusión | Excluye palabras, valores o combinaciones de la sintaxis: vocabulario prohibido, «nunca X», listas negativas |
| T-PRO | Regla de proceso u orquestación | Ordena etapas, gates, aprobaciones, entregas y trazabilidad. Es el «otro tipo de reglas» que pidió Eric |
| T-VLD | Regla de validación o crítica | Dice cómo se comprueba o se juzga un prompt o un activo |
| T-EJE | Ejemplo | Un prompt, brief o caso de muestra |
| T-TAB | Tabla o matriz | Fila o cabecera de tabla, o matriz de decisión |
| T-DEF | Definición o contexto | Explica un concepto sin mandar nada |
| T-NUL | Sin contenido de regla | Licencia, código de infraestructura, separador, puntuación |

### 3.2 La matriz

- **Filas:** los 13,005 textos. La primera columna es el id INV; la segunda, el documento; la tercera, la ruta completa de encabezados.
- **Columnas:**
  - las de la §3.1 (impacto y tipos);
  - una columna por cada categoría de la taxonomía: los 360 valores autorizados del catálogo CASOS (facetas F01–F31 y P-01, P-04 y P-05), más los valores de las extensiones del 23 y del 26 de octubre (pendiente P-06).
- **Celdas:** X si la categoría aplica a ese texto; 0 si no. Al terminar, **todas las celdas llevan X o 0; ninguna queda vacía**. Con unas 370 columnas son unos 4.8 millones de celdas (13,005 × 370).

### 3.3 Primera ronda: mecánica

Se llena con el documento y la ruta de encabezados a la que pertenece cada texto. Cada uno de los 1,393 pares documento + encabezado recibe sus X por lo que dicen el documento y sus encabezados:

- `skills/video/...` → F01 = 6 Video;
- `image/references/gpt-image.md` → F29 = GPT Image 2;
- el encabezado «Editing» → F10 = edición.

Esas X se propagan a todos los textos de ese documento y encabezado, y el resto de la fila queda en 0. Cada asignación lleva su motivo, por ejemplo «documento» o «encabezado h2 Editing», para que se pueda revisar.

### 3.4 Segunda ronda: revisión del texto, una categoría por vez

Para cada columna, una por una y nunca todas a la vez, se leen los textos y se confirma o cambia la celda de cada uno: un 0 de la ronda mecánica puede pasar a X y una X puede pasar a 0. Cada cambio guarda su motivo y el texto que lo prueba.

### 3.5 Controles de cada ronda

Son los mismos que se usaron para cerrar el mapa:
1. Un programa comprueba que no quede ninguna celda vacía, que cada X tenga su motivo y que cada id exista.
2. Un segundo lector independiente revisa.
3. Un tercer lector hace una lectura sellada del 10 % al azar. Si encuentra un error, se repite toda la columna.

## 4. Pendientes de este diseño (decide Eric)

| # | Pendiente | Propuesta |
|---|---|---|
| D-01 | Aprobar la lista de tipos de texto de la §3.1 | La tabla tal cual. T-PRO y T-VLD son el «otro tipo de reglas» |
| D-02 | ¿Las columnas de la taxonomía son los valores (360 más extensiones) o también los 1,369 términos del tesauro? | Solo los valores. Los términos son vocabulario que cuelga de los valores (taxonomía §1.4) y sirven para buscar, no para catalogar |
| D-03 | Cómo se marca un texto que vale para todos los valores de una faceta (UNIVERSAL en la taxonomía §1.2) | X en todos los valores de esa faceta, más una columna «universal en Fxx» con X, para que no se confunda con un texto que nombra cada valor |
| D-04 | Los textos sin impacto en brief ni prompt, ¿se revisan en la segunda ronda? | Sí en las columnas de proceso (F01 Etapa, F02 Paso, P-01 Flujo y P-05 Ámbito); en las demás, 0 de la ronda mecánica, con el motivo «sin impacto» |
| D-05 | Alcance de esta clasificación: los 13,005 textos o solo los de imagen de la decisión 24 §1 (universales, parcialmente universales que incluyen GPT Image 2 y específicos de GPT Image 2) | Los 13,005 en la ronda de tipo de texto y en la ronda mecánica. La segunda ronda, primero sobre los textos de imagen que incluyen GPT Image 2 y después sobre el resto |
| D-06 | Costo de la segunda ronda (pendiente P-13) | Se calcula con números reales cuando termine la ronda de tipo de texto, porque depende de cuántos textos tienen impacto. Se presenta antes de empezar la segunda ronda |

## 5. Orden de ejecución

1. Cerrar los pendientes de la etapa 1 (mapa) y de la etapa 2 en `PENDIENTES.md`, más D-01 a D-05; o que Eric autorice expresamente empezar sin ellos.
2. Reconstruir la ruta de encabezados de los 6,068 textos sin estructura (§3.0).
3. Ronda de tipo de texto (§3.1).
4. Ronda mecánica (§3.3).
5. Presentar el costo de la segunda ronda (D-06).
6. Segunda ronda, columna por columna (§3.4).
7. Construir el selector, el compilador y la aplicación sobre la matriz terminada.
