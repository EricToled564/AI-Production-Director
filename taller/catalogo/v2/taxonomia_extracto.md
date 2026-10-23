# Extracto literal de 00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md

Líneas 157–209 (principios y contrato §1.12–§1.13):
## 1. Principios

1.1 Espina de clasificación: las 31 facetas de caso vigentes, más los cambios puntuales ya aprobados y la codificación de flujo que queda incluida en la aprobación integral C18. Un **caso** es una tupla de valores sobre facetas de los bloques A, B y C. Una **regla** es una unidad (o grupo de unidades) del inventario con su estado en cada faceta, sus atributos del bloque D, sus metadatos del bloque E y, si es condicional, su grupo de condiciones (§7.2).

1.2 Dos formas de alcance por faceta: **VALOR**, uno o más valores concretos y sus condiciones; **UNIVERSAL**, ausencia de restricción de esa faceta dentro del alcance documental comprobado y explícito (modelo, operación, tipo de imagen y casos), con evidencia, responsable y fecha. UNIVERSAL no extiende una regla de un modelo a otros ni elimina excepciones. Todos los ítems y valores se examinan y la matriz §1.12 documenta el resultado. Vacíos, omisiones y etiquetas de duda no son clasificaciones válidas. Una duda impide cerrar ese texto; se resuelve con contexto y decisiones y, si no basta, se consulta antes de avanzar al siguiente texto del bloque. No se sustituye una duda por universalidad. Los objetos no audiovisuales reciben su categoría positiva y su unidad conforme a §6.0.

1.3 Medio del activo, tipo de pieza final y etapa se registran por separado. Las ramas imagen/video de las facetas 10 y 29 se eligen por el medio del activo; la de la faceta 4, por la pieza final; nunca por la etapa. El objeto regulado se tipa positivamente: activo visual o sonoro, documento, archivo, paquete de entrega, registro de ejecución o campo/esquema. El esquema es una unión tipada: la rama activo contiene medio; las otras ramas contienen su categoría y unidad concretas. No se introduce un valor de ausencia en medio para esas ramas. Toda rama conserva condiciones y ruta de uso comprobables.


Decisión del usuario 2026-10-11 16:56:54.532502 UTC, Sentinel_d46f126e89e081919ccb3a120d2ce227: en reglas de ancla o keyframe en ruta de video, F26–F28 llevan VALOR cuando existe restricción pertinente o UNIVERSAL cuando no la hay; nunca NO APLICA. La separación imagen/video se determina por F11 y el flujo de cada aplicación, no solo por que el medio del frame sea imagen fija. El frame sigue la ruta de imagen y la sintaxis de su modelo; F26–F28 conservan el contexto del clip sin obligar a enviar instrucciones de movimiento/audio al prompt de imagen. UNIVERSAL en F26–F28 significa que la regla no impone una restricción independiente sobre esos atributos; no exige generar movimiento, transición ni audio. Una regla compartida entre imagen independiente y ancla de video puede conservar UNIVERSAL y distinguir la instancia por F11 y flujo, sin duplicar reglas ni añadir un mecanismo de condiciones especial. Se evalúan las facetas efectivas de la aplicación (override sobre regla) y sus condiciones.

1.4 Dos capas: facetas (pocas, cerradas, filtran casos) y términos del tesauro (etiquetas multivalor colgadas de una faceta o de un valor de la faceta 30; expanden consultas). Un término no sustituye un valor de faceta ni se fusiona con él por compartir palabras. Excepción de forma, no de principio: los datos de valor tipado (el formato de salida de la faceta 6, escrito ancho:alto, y la referencia adjunta con medio y papel de §6.0) admiten cualquier valor del formato declarado; el selector los registra sin necesitar un término del tesauro, y un término solo respalda el significado documentado de un valor.

1.5 Materia y condición. La faceta 30 describe la materia que regula la regla; las facetas A–C y las condiciones describen cuándo se activa. Mencionar un elemento para prohibirlo lo hace materia, no condición de presencia. Una regla puede tener varias materias.

1.6 Procedencia y alcance se comprueban juntos, sin confundirlos. Documento de origen y jerarquía de encabezados guían la preclasificación y la interpretación de cada texto. Se leen cuerpo, sección completa y contexto necesario. Se heredan únicamente restricciones sustentadas por esa lectura, citando si provienen del cuerpo, encabezado o documento; un nombre de archivo o una palabra aislada no basta para extender automáticamente el alcance a todos sus textos. Documento, encabezado, página asignada, líneas, versión y hashes conservan la procedencia.

1.7 Rutas completas. Toda aplicación conserva la tupla flujo → sección → paso → condición. Varias aplicaciones por regla son varias tuplas completas; nunca listas independientes cuya combinación invente rutas. Las varias aplicaciones de una regla son registros de aplicación subordinados a su único ID de regla (§7.1); se evalúan y se agregan según §7.4.

1.8 Identidad persistente. Cada regla y cada unidad del inventario tiene un ID persistente que no depende de archivo, línea ni texto. Hash del texto, versión del archivo y localización (archivo, encabezado, líneas, páginas asignadas) se registran como atributos separados. Mover una regla de línea no cambia su ID; modificar su texto crea una nueva versión con historial, mismo ID. Los IDs no se reciclan ni cambian por cambios de etiqueta. Una sola ubicación canónica por concepto; el resto, remisiones.

1.9 Ámbito funcional y uso operativo son dos datos distintos (P-05). El ámbito dice a qué parte del trabajo pertenece la regla; el uso operativo dice si participa hoy en la selección de reglas para generar. Ninguna regla sale de la clasificación por su uso operativo.

1.10 Dos vías para completar el brief (§7.3): proyecto integral (los documentos de etapas anteriores producen los datos, con sus aprobaciones vigentes) y activo directo (el usuario aporta los datos; el sistema infiere y recomienda lo faltante para aprobación o modificación). Ninguna vía exige preproducción publicitaria a un activo independiente.

1.11 Cifras, límites y presets de las fuentes se conservan con su alcance declarado (flujo, modelo, skill); no se convierten en leyes universales ni se descartan por ser presets. Una denominación de modelo sin versión, fecha, interfaz y evidencia no acredita capacidad vigente.

## 1.12 Contrato obligatorio de lectura y clasificación por texto — 2026-10-19 UTC

Autoridad: decisión del usuario Sentinel_b3ae132637fc819189f0f80a014b1220; complemento sobre documento y encabezado Sentinel_88910f5731a08191afcf6a10c6a21451. Esta corrección prevalece sobre diseños históricos incompatibles. No declara ejecutada la clasificación ni una nueva canonización del corpus.

1. Partir del inventario de textos originales sin reutilizar etiquetas previas como respuesta. Congelar fuente, versión, hash, IDs y localización. Mantener literalmente las citas y los originales.
2. Dividir el inventario en bloques trazables, sin pérdida ni duplicación de unidades, con un agente responsable por bloque. Cada agente recibe esta misma versión de taxonomía, decisiones aplicables, documento íntegro, encabezados jerárquicos y contexto de cada unidad. Ningún texto se procesa privado de ese contexto.
3. Para cada texto, leer primero documento, encabezados, sección y cuerpo. Preclasificar su ámbito: orquestación, generación de imagen (incluidos FF/LF) y otros ámbitos ya definidos, con todas las asociaciones pertinentes. Una unidad mixta conserva aplicaciones separadas; el ámbito ajeno al alcance de esta fase sigue inventariado y correctamente identificado.
4. Examinar CADA faceta, subfaceta, valor y término del esquema vigente, de lo general a lo particular. La matriz de revisión enumera todos los ítems y valores existentes; no basta una lista de etiquetas encontradas ni una búsqueda por palabras. Registrar para cada ítem la evidencia contextual que fundamenta incorporarlo o descartarlo como etiqueta de ese texto. El descarte de una etiqueta concreta en esta matriz no elimina la regla ni constituye un estado de elegibilidad.
5. Asignar TODAS las clases pertinentes, conservando tipos de enunciado (regla, ejemplo, alternativa, sintaxis, valor de campo, selección y demás valores existentes), ámbito, modelo, tipo de imagen, casos, condiciones y destinos. Una universalidad se circunscribe explícitamente al ámbito probado; varias alternativas se representan como aplicaciones completas, sin producto cartesiano artificial.
6. Evidencia por asignación: ID de texto, ID de aplicación, ítem/valor taxonómico, etiqueta asignada, fragmento literal, origen de la restricción (cuerpo / encabezado / documento / decisión), documento, jerarquía de títulos, líneas, página asignada, hash y justificación. La matriz contiene también la razón contextual por cada ítem examinado que no se incorpora. La evidencia se reutiliza mediante referencias para evitar copiar innecesariamente el corpus.
7. Antes del siguiente texto, verificar cobertura de todos los ítems, coherencia entre clases, condiciones alcanzables y destino de cada aplicación. Si existe duda: releer fuente y decisiones; si no la resuelven, formular una consulta concreta con ambas evidencias y detener ese bloque en ese texto. Los demás bloques pueden continuar. La consulta es una tarea de resolución, jamás una etiqueta del texto ni sustituto de clasificación final.
8. Se prohíben como estados o valores de clasificación NO DETERMINADO, NO APLICA, DESCONOCIDO, PENDIENTE, EN PROCESO y equivalentes semánticos que pospongan la clasificación o impidan permanentemente seleccionar la regla. Tampoco se admite ocultar ese efecto en vacíos, null, listas vacías, flags, razones de uso operativo o condiciones imposibles. Un registro defectuoso se corrige antes de la entrega; no se maquilla con UNIVERSAL.
9. Cada aplicación sin exclusión expresa exige un testigo positivo coherente con su fuente y condición, incluido su destino de orquestación, template o generación. La incorporación a template exige enlace verificable al bloque/campo y a su validación, de manera que la instrucción se ejecute cuando corresponde. Solo una decisión expresa, identificada y aplicable autoriza exclusión permanente.
10. Las citas literales y los anexos históricos pueden contener vocabulario prohibido: son EVIDENCIA CITADA NO OPERATIVA. Las etiquetas documentales de confianza, adopción, prueba y antigüedad nunca integran los estados de clasificación ni el filtro de elegibilidad. El texto de fuente no se altera para hacer desaparecer esas palabras.
11. Congelar cada ronda completa con manifiesto de cobertura y hash; conservar la separación entre clasificación terminada, consulta aún sin resolver y paquete entregable mediante el control de ejecución del trabajo, sin exportar consultas como clases. No entregar como completo mientras existan textos sin resolución. No ampliar ni borrar valores de la taxonomía para forzar cobertura; una necesidad real se fundamenta y consulta.
12. Controles de aceptación: mismos 1.369 IDs TRM; citas literales íntegras; todas las facetas y extensiones conservadas; cero valores de diferimiento habilitados; matriz completa por texto; todas las etiquetas pertinentes; cero aplicaciones sin condición alcanzable salvo decisión expresa; cero generalizaciones no sustentadas; trazabilidad documental y de destino verificable. Estos controles definen la aceptación, no afirman que ya se ejecutó sobre todo el corpus.


## 1.13 Correspondencia exhaustiva entre taxonomía y templates — 2026-10-19 UTC

Autoridad: Sentinel_d7081e5e8c148191a084240ad839e38e. Cada clasificación de la taxonomía, incluidos valores y extensiones, tiene una correspondencia explícita en los contratos de templates. No basta conectar solo las reglas ya recuperadas.

La matriz obligatoria vincula ID de clasificación y valor → template de brief y/o prompt → campo, bloque, parámetro, condición de activación, validación o traza interna concretos → reglas que lo fundamentan → caso positivo. Conserva modelo, versión, operación, medio, flujo y fuente de la correspondencia. Una misma clasificación puede tener varios destinos con condiciones completas. La ubicación interna no obliga a copiar literalmente todas las etiquetas al prompt: sujeto, iluminación o cámara pueden generar texto; modelo y operación pueden seleccionar estructura; una prohibición puede alimentar validación; la evidencia permanece en la traza.

Los ámbitos ajenos a las dos fases actuales conservan su destino identificado en el contrato del template pertinente y el alcance de fase, sin campos vacíos ni estados de aplazamiento. Un template no se declara implementado por tener un contrato de destino. Las clasificaciones compartidas conservan todos sus destinos. Si falta una correspondencia, se resuelve su contenido y ubicación antes de cerrar el bloque, consultando únicamente cuando fuente y decisiones no basten. La comprobación de cobertura exige que todo ID de clasificación y valor tenga destino justificado y que todo campo o bloque del template remita a clasificación y fundamento, sin clases desconectadas ni campos inventados.


Líneas 2560–2613 (§5.3–§6.0):
### 5.3 P-05 — Faceta «Ámbito funcional» y campo «uso operativo» (decisión de diseño aprobada)

| Ámbito funcional | Alcance |
|---|---|
| Preproducción | marca, estrategia, guion, dirección cinematográfica, planificación de shots |
| Creación de imagen | génesis, maestros, cuadros, anclas, edición de imagen |
| Creación de video | prompts de movimiento, sintaxis de modelo, continuidad, clips |
| Crítica, validación y aceptación | crítica de renders, validadores, gates, canonización; se vincula al medio evaluado |
| Audio y música independientes | audio que no sale del modelo de generación visual |
| Postproducción | ensamblado, grade, overlays, exportación |
| Empaquetado y entrega | paquete de producción, preview, trazabilidad y créditos |
| Orquestación y control de flujo | activación, selección de skills, orden de etapas, gates y escalamiento. Cada aplicación tiene disparador, condición y destino de control explícitos; no se le asigna una exclusión por defecto. |

Campo «uso operativo», por aplicación de la regla (no por regla completa):

| Valor | Significado |
|---|---|
| ACTIVO EN SELECCIÓN | la aplicación participa en la selección de reglas para generar imagen o video |
| INCORPORADA A TEMPLATE | aplicación incorporada y verificada en su template; incluye sintaxis de modelo aplicada una vez a la ficha por DEC-000025. No se vuelve a extraer para cada caso; permanece clasificada. La incorporación exige vínculo regla → campo/bloque → condición → validación; si varía por caso, esa condición se evalúa al instanciar el template. |
| APLICACIÓN EN CONSTRUCCIÓN DE TEMPLATE | instrucción estructural seleccionable durante la construcción o actualización del template; exige destino y prueba de incorporación antes de publicar ese template. Expresa cuándo se usa, no aplaza su clasificación. |
| APLICACIÓN EN CONTROL O ENTREGA | aplicación de crítica, audio, postproducción o entrega seleccionable en su ruta específica, con disparador y destino. Su separación de recuperación de prompts requiere decisión aplicable y alcance documentados; una regla mixta conserva cada ruta. |

Una regla mixta conserva activas sus aplicaciones de generación aunque su aplicación de preproducción esté incorporada a un template.

### 5.4 P-02 — Autoridad como metadato (decisión de diseño aprobada)

La faceta 32 no se restituye como categoría temática. Su información se conserva íntegra en metadatos: documento, encabezado, página asignada y versión; materia sobre la que tiene autoridad; ámbito y criterio de precedencia. Si un texto original establece una regla de autoridad o precedencia, esa regla también se inventaría (ya está en el inventario) y se clasificará. No se atribuye autoridad a documentos no suministrados ni prioridad absoluta de una fuente sobre todas las materias: cada autoridad vale para su materia y su ámbito.

## 6. Bloque E — Metadatos de la regla

### 6.0 Campos

| Campo | Valores o formato | Obligatorio |
|---|---|---|
| ID persistente | INV-/REG-nnnnnn; independiente de archivo, línea y texto (§1.8) | sí |
| documento · encabezado | archivo del corpus autorizado y ruta de títulos | sí |
| localización | líneas inicial–final; páginas asignadas inicial–final (P-06, marcadas ASIGNADA); paginación original si existe | sí |
| versión | hash del archivo original, hash de la representación textual (HTML) y hash del texto de la unidad | sí |
| idioma del enunciado | en · es · ru | sí |
| objeto regulado | activo visual o sonoro · documento · archivo · paquete de entrega · registro de ejecución (run) · campo o esquema | sí |
| medio del activo | rama activo: imagen fija · imagen secuencial · video · audio · pieza multimodal; otras ramas: se tipan por objeto regulado, sin valor ficticio de medio | obligatorio en la rama activo |
| unidad | fotograma · panel · clip · secuencia · escena · documento · archivo · paquete de entrega · registro (run) · campo o esquema; según objeto y texto contextual | sí |
| referencia adjunta | tupla (medio ∈ imagen · video · audio; papel ∈ valores de la faceta 23; identificador, archivo y hash del adjunto); una por adjunto, de modo que cada papel queda asociado a su archivo | si la regla o el caso usan referencias |
| rutas de aplicación | una o más tuplas flujo → sección → paso → condición (§1.7) | sí |
| ámbito funcional · uso operativo | P-05, por aplicación | sí |
| tipo de enunciado · fuerza normativa | valores de 6.1 | sí |
| origen de evidencia · evidencia de la afirmación fuente | origen documentado separado de los descriptores de §6.1 como metadatos documentales; nunca estados de clasificación ni filtros de elegibilidad | sí |
| adopción canónica | «adopción documental» (regla original de una skill, con fuente y autoridad resueltas; no exige ejercicio propio) · «Familia de régimen en borrador documental» y «Canonizada» (solo entradas del protocolo de familias de régimen, flujo-anclas.html:538–582) · «excluida por decisión del usuario» · «refutada» · «histórica» | sí |
| condición | grupo de condiciones según §7.2 | si es condicional |
| estado de evidencia de capacidad · dependencia | valores de 6.1 | si declara capacidad de modelo |
| estado del modelo citado | vigente · histórico, con versión y fecha de verificación | si nombra un modelo |
| autoridad | materia sobre la que tiene autoridad · ámbito · criterio de precedencia (P-02) | si el texto la establece |
| precedencia | referencia a una fila de la tabla 6.2 | si hay conflicto documentado |


Líneas 2784–2817 (§7):
## 7. Registro, condiciones, brief y consulta

### 7.1 Registro mínimo de una regla

| Grupo | Campos |
|---|---|
| Identidad | ID persistente (§1.8); unidades de inventario que la componen; texto literal; texto de contexto (sección padre, solo para lectura) |
| Versión y localización | hash del texto, hash del archivo y de la representación, documento, encabezado, líneas y páginas asignadas, historial de versiones |
| Bloque A | etapa, paso y flujo (P-01 incluido por decisión del usuario), con estado por faceta; rutas completas |
| Bloques B y C | facetas 3–29, incluida P-04 dentro de faceta 4, resueltas como VALOR o UNIVERSAL con alcance y evidencia; matriz exhaustiva de todos sus ítems y valores |
| Bloque D | faceta 30 (una o más materias) + términos del tesauro + faceta 31 + ámbito funcional (P-05) |
| Bloque E | todos los campos de §6.0 |
| Aplicaciones | cada aplicación es un registro subordinado al ID de la regla, con su ruta completa (§1.7), su estado por faceta, su condición, su uso operativo (P-05), su adopción y su evidencia de la afirmación fuente; las varias aplicaciones de una regla comparten su ID, su texto y su procedencia |

### 7.2 Lógica de condiciones

Una condición es un grupo con operador TODAS, ALGUNA o NINGUNA y una lista de miembros (átomos o subgrupos). Átomo = (faceta o campo, operador =, ≠, ∈, ∉, <, ≤, >, ≥, entre, existe, no existe; valor o umbral; unidad). Unidades, umbrales, negaciones y excepciones viven dentro de su grupo. (A Y B) O (C Y D) = `{ALGUNA:[{TODAS:[A,B]},{TODAS:[C,D]}]}`. «Cualquiera de estas referencias» = ALGUNA; «todas simultáneamente» = TODAS. Excepción = subgrupo NINGUNA dentro del grupo que la contiene. Evaluación definitiva binaria: VERDADERO o FALSO, tras comprobar que el brief contiene todos los discriminantes requeridos. Si falta uno, se solicita y aprueba antes de ejecutar la selección definitiva; no se produce una tercera clase de regla. Una condición alternativa conserva su caso: dos ramas son dos aplicaciones del mismo ID de regla (§7.1), no dos reglas ni dos versiones, y cada una se evalúa íntegra.

### 7.3 Brief: exploración frente a selección definitiva

Mientras falten datos que puedan cambiar qué reglas aplican, solo se permite búsqueda exploratoria para formular propuestas; no se cierra la selección definitiva. Antes de esa selección se resuelven todos los discriminantes relevantes con datos aportados o propuestas aprobadas. Si una regla exige un dato adicional, ese campo se completa y aprueba antes de generar. Vía proyecto integral: los documentos de etapas anteriores producen los datos y conservan sus aprobaciones vigentes; solo se consultan faltantes, contradicciones o cambios. Vía activo directo: el usuario aporta los datos; el sistema infiere y recomienda lo faltante para aprobación o modificación. Los templates de entrada y salida se diferencian por imagen/video, modelo, versión, interfaz y operación. Ejemplo (flujo de anclas): etapa 5 · E5.2 · FL03 (FL02 para la génesis) · Video publicitario · pieza final spot (video) · 9:16 · medio del activo imagen fija · génesis T1 · character ref · A pose sostenida · persona · 1 · rostro ≥20 % · sin referencias · GPT Image 2.

### 7.4 Consulta: una sola salida por regla

Paso 0: validar integridad de registros y completar discriminantes del brief. Un defecto se corrige antes de cerrar el catálogo; un dato de caso ausente se solicita antes de selección definitiva. No se distribuye el defecto como una clase de regla. Paso 1: evaluar por separado cada aplicación y su tupla íntegra de facetas y condiciones; conservar descartes del caso con evidencia. Paso 2: evaluar las condiciones de §7.2. Paso 3: recuperación híbrida exhaustiva del conjunto elegible; el ranking ordena y no excluye, top-k no acredita cobertura. Paso 4: una regla es APLICABLE CONFIRMADA si al menos una aplicación cumple y ninguna decisión expresa excluye esa aplicación. Se registra FUERA DE ESTE CASO solo cuando todas sus aplicaciones resultan incompatibles con ese caso. EXCLUIDA POR DECISIÓN como resultado de regla exige que todas sus aplicaciones estén cubiertas por decisiones expresas. Si algunas están excluidas por decisión y las restantes son falsas para el caso, el agregado es FUERA DE ESTE CASO, preservando las causas distintas por aplicación. Ningún resultado de consulta sustituye la clasificación estable del catálogo.

| Orden | Clase | Criterio |
|---|---|---|
| 1 | EXCLUIDA POR DECISIÓN | decisión expresa del usuario, identificada, con evidencia de que cubre la aplicación. Verificación técnica o antigüedad no bastan |
| 2 | FUERA DE ESTE CASO | predicado completo FALSO para este caso con brief completo; se conserva el caso positivo en que la aplicación sí es elegible |
| 3 | APLICABLE CONFIRMADA | las condiciones documentales de la aplicación se cumplen en el caso y no hay una exclusión expresa aplicable. Conserva las advertencias de evidencia técnica, sin convertirlas en un veto de selección |

Una regla original con fuente y autoridad resueltas se clasifica por su contenido sin exigirle un ejercicio de canonización ajeno a su protocolo. Requisitos técnicos de ejecución se registran aparte y no borran reglas documentalmente aplicables. Traza de consulta: caso completo, valores y condiciones evaluados, descartes por aplicación, decisiones expresas, aplicación que determina el resultado de cada regla y motivo respaldado.


Líneas 4337–4349 (gate final):
## Gate final de aceptación bidireccional

La aceptación final exige comprobar simultáneamente:

1. Cero reglas o puntos pertinentes del corpus autorizado sin clasificación. Cada unidad inventariada debe quedar conciliada con una regla o punto clasificado, o con una justificación explícita y revisable de que es estructura, código auxiliar, duplicado referenciado u otro contenido no normativo. Una señal léxica ausente no autoriza excluirla. Ninguna regla se elimina para alcanzar el cero.
2. Cero categorías activas sin respaldo de reglas reales del corpus autorizado. Cada categoría conserva IDs de las reglas que la respaldan. En categorías padre se informa por separado el respaldo directo y el respaldo heredado de descendientes; una categoría estructural puede tener cero reglas directas si tiene descendientes realmente respaldados. No se inventan reglas para llenar categorías; una propuesta sin respaldo permanece inactiva y señalada hasta decidir su tratamiento.
3. Todas las citas operativas resolubles: documento original autorizado, versión, encabezado o localizador equivalente, líneas, página asignada y unidad de inventario correspondientes al texto citado. Los contadores agregados no sustituyen el registro individual. Las citas no resolubles no se presentan como respaldo confirmado.
4. Conciliación en ambos sentidos: regla → categorías y categoría → reglas, con totales, incidencias e IDs comprobables. Deben preservarse el texto original, sus condiciones, excepciones y todas sus aplicaciones pertinentes.

Este gate es un criterio de aceptación, no una declaración de resultado logrado. La entrega consolida el catálogo recibido bajo C18 y decisiones aprobadas; no certifica cero reglas sin clasificar ni cero categorías activas sin respaldo de todo el corpus. Las correcciones de enlaces realizadas no certifican por sí solas toda la clasificación ni el respaldo semántico de todas las definiciones.

C17 (2026-10-03): la revisión de cierre de C16 encontró 9 hallazgos parciales (H-011, H-024, H-025, H-029, H-037, H-040, H-043, H-044, H-061) y se cerraron todos: valor «3 o más» de la faceta 19 y TRM-0174 limitados a sujetos individuales con identidad (la multitud anónima queda como placa o capa separada); TRM-0008 sincronizado con el valor padre «retrato» (una o varias personas); localizador de TRM-0653 corregido a portrait-cinema.md:92; alias de TRM-0367 y justificaciones de nivel de TRM-0171, 0293, 0367, 0602, 0603, 0662 y 0748 alineados con las definiciones vigentes. Niveles sin cambio: 1200 COMPLETO, 112 PRESENCIA, 57 SIN PRESENCIA. Citas: 3.096 individualizadas (una más que en C16: la de retrato de grupo que respalda TRM-0008), todas verificadas contra el inventario.

