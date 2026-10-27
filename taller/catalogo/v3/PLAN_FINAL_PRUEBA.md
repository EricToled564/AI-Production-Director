# Plan final de la prueba: sistema de prompts para GPT Image 2 (reescrito el 2026-10-27)

## 1. Objetivo y qué demuestra la prueba

**Qué hace el sistema.** Convierte un brief en prompts de GPT Image 2 que den imágenes de apariencia fotográfica y alta
calidad al primer intento. Eric genera las imágenes en la App de ChatGPT para escritorio (decisión 26 §8).

**Qué demuestra la prueba.** Para cada caso, que el sistema selecciona todas las reglas que aplican y que cada prompt
las cumple. Si una imagen sale mal, la falla repetida se diagnostica solo como:
- a: falló la selección;
- b: falló el prompt;
- c: falta la regla en el corpus.

Fuente: 26 §10 y §15.

**Método** (decisión 24 §4): universo → filtro por caso → controles de completitud → clasificación de lo pertinente →
prueba del selector.

**Alcance** (decisión 26 §12): solo imagen con aspecto de foto real. Cada tipo de imagen fotográfica tiene su propio
caso. Los tipos que la prueba cubre están en las decisiones 26 §16 y §17. Las técnicas no fotográficas:
- siguen en el universo;
- se clasifican en una prueba posterior;
- aquí solo pueden servir como entrada de un caso.

**Registros de lo leído para este plan:**
- `LECTURA_PLAN.md`;
- `LECTURA_4_DOCUMENTOS.md`;
- `revision/01_texto_en_imagen.md` a `revision/07_auditoria_salidas_universo.md`.

Cuando un registro de `revision/` difiere de los anteriores, manda el de `revision/`.

## 2. Reglas comunes a todos los casos

| Regla | Fuente |
|---|---|
| Solo GPT Image 2. Las reglas que piden otro modelo, como el grounding de Nano Banana 2 para edificación, animal y planta, son FUERA DE ESTE CASO: su predicado pide otro F29. No son EXCLUIDA POR DECISIÓN | decisiones 23 §6, 26 §15; taxonomía §7.4 (L2806–2816) |
| Universo: textos de generación de imágenes universales, parcialmente universales con GPT Image 2 y específicos de GPT Image 2. Son 2,724 textos más 40 de la adenda. Las secciones «otro_modelo» y «fuera» conservan la decisión por sección | decisión 24 §1; 26 §18 y §19; `v3/universo`, `v3/universo/adenda` |
| Cuando un texto da la cifra de otro modelo, vale la de GPT Image 2 | decisión 26 §1 |
| Etiquetas 100 % de la taxonomía o de una extensión aprobada; sin pendientes ni NO APLICA. La faceta de texto se escribe «F32 texto en la imagen (extensión 2026-10-23)». No es la F32 «fuente con autoridad» que PLAN_V5 L337–350 no restituye | decisiones 23 §3, §4, §5 |
| Brief en español; prompt siempre en inglés | `taller/recursos/directivas_taller.json` (ERIC-IDIOMA-PROMPT-INGLES) |
| Prohibidos «photorealistic» y «fotorealista», también cuando la plantilla de la fuente los trae (`dimensional.md:17`, `gpt-image.md:100`). Aurora excluida. En el vocabulario de prompts, el prohibido gana | CLAUDE.md; `user_directives.json`; PILOTO §0.4; taxonomía §6.2 fila 1 (INV-000698) |
| Formato escrito en el texto: Scene nombra el ratio. Tamaño y quality van como referencia. Sin máscara | decisión 26 §8 |
| Model, Quality, Size, References y Notes van fuera del cuerpo del prompt. El ratio va además dentro de Scene. La app no expone parámetros (26 §8), y ADD-0042 pide el parámetro solo «when the platform exposes them». En este punto 26 §8 manda sobre ADD-0011 | ADD-0004, ADD-0010, ADD-0011, ADD-0042; decisión 26 §8 |
| Quality la elige el usuario. Es high obligatorio en: retrato; texto pequeño o denso; producto con etiqueta; edición que conserva la identidad de una persona | decisión 23 §7; `gpt-image.md:45–47` (INV-002350–002352); `flujo-anclas.html:440` (INV-000222); PLAN_V5 L862 |
| Ninguna atribución a terceros en material al cliente | DEC-000024 |
| Longitud: referencia aspiracional, nunca bloquea. El prompt es lo más corto posible, sin repeticiones ni otra ineficiencia del lenguaje, sin sacrificar la sintaxis que exigen los textos del modelo. Hay aviso si el prompt o un slot pasa de 300 palabras. En `armar.py`, el rechazo por más de 300 (L84–85) pasa a aviso | decisión 26 §11; T-BRIEF-IMG L355; ADD-0008 |
| Una imagen se acepta solo después de su QA, con los controles mecánicos separados de los visuales | ADD-0047 |
| Un chat nuevo por prompt, con las referencias adjuntas en cada uno. Así el prompt no depende de memoria entre imágenes, el dato que falta en `CONTRADICCIONES.md` §4 (no lo resuelve) | INV-012218 (`consistency-locks.md:3`) como práctica de serie |
| Brief aprobado por Eric, ligado a su sha256; cualquier cambio invalida la aprobación | T-BRIEF-IMG L13–15; schema L1333–1352; PILOTO §5 |
| Ningún logo ni texto de marca real sale de texto: solo de asset aprobado | `flujo-anclas.html:50` (INV-000027); `flujo-spot.html:354` (INV-000472); ADD-0027; taxonomía L425–429 |

## 3. Mapa por tipo de imagen

**Tipos.** Son las 8 operaciones del contrato (schema L45–54, `CONTRATOS_OPERACION_MODELO.json` L4–362). La
descripción de imagen se ejecuta como génesis (26 §14).

**Campos de toda operación:**
- Los 12 campos «siempre»: ruta.flujo, operacion, modelo nombre/versión/interfaz, pieza tipo/objetivo/uso, formato.ratio, idioma_prompt, restricciones y selecciones_taxonomicas.
- `procedencia_campos` por valor.
- `aprobacion_brief`.

**Módulos condicionales** (CONTRATOS L775–819). Se activan en el brief aprobado:
- El módulo fotografía va activo en todo caso que no sea edición: plano, ángulo, efecto óptico y luz (L775–790).
- Una edición que conserva la toma no lo redefine.

| Tipo (F10) | Operación · template | Técnica | Referencias | Salida | Lo que la gobierna |
|---|---|---|---|---|---|
| Génesis sin referencias | `genesis` · T-GENESIS | FL04 D01–D05 (taxonomía L257–261); FL02 E5.2 (INV-000525–000614 del universo) | 0 (INV-000610) | GPT2-GEN | Por clase de sujeto (INV-000539, 000593), detallado debajo de esta tabla |
| Descripción de imagen | `genesis` (26 §14) | `vision-decomposer.md` paso 1, descomposición (`:11–55`) | 0: la foto no se adjunta | GPT2-GEN en 5 slots, no las palabras clave de `vision-decomposer.md:61`, `:93` | Cada valor sacado de la foto entra con origen `inferencia_para_aprobacion`; la foto y su sha256 son la fuente (schema L1040–1332). Valores: plano y ángulo con el vocabulario de `vision-decomposer.md:26`; efectos ópticos (`:51–52`) en Important Details. «Sin inventar objetos» vale para el brief. Aprueba si la imagen se parece a la foto |
| Composición con referencias | `composicion_referencias` · T-REF-COMP | E5.3 (cuerpo T2 con el rostro adjunto), E5.4 (persona en lugar), EN.1–EN.6 (grupo) | ≥1, cada una con índice, rol y preservaciones | GPT2-GEN; el rol de cada imagen va dentro de su slot (`verificar_templates.py` L65) | INV-000395, 000396, 000428, 000474, 000486–000487, 000490, 000508–000512, 000590, 000203; taxonomía L263; «Rostro T1 antes que cuerpo T2, siempre» (DECISIONES.md); hasta 16 referencias con rol (INV-002054 corregido). Grupo: EN.1–EN.6, con verificación miembro por miembro (taxonomía L461–466) |
| Edición | `edicion` · T-EDIT | E5.5 | ≥1 (la imagen a editar) | GPT2-EDIT: Change / Preserve / Constraints, un cambio por iteración, lista de preservación repetida en cada iteración (`editing.md:6`, `image/SKILL.md:100`) | INV-000397, 000584–000585; `editing.md` (INV-002021); `gpt-image.md:94–100`; sin máscara (26 §8). La plantilla de cada caso se indica en el §4 |
| Transferencia de estilo | `transferencia_estilo` · T-STYLE | FL04 | ≥1 | GPT2-GEN; la imagen de estilo va adjunta con su rol | `gpt-image.md` Style Transfer: propiedades visuales concretas del referente (INV-002389–002390), referencias con rol (INV-002386–002388); estilo como referencia adjunta (INV-002294–002295) |
| Boceto o plano a final | `boceto_a_final` · T-SKETCH | `structural.md` (INV-002025) y `dimensional.md` (INV-002026) | ≥1 (el boceto o plano) | GPT2-GEN | La plantilla de cada caso (26 §17) se indica en el §4 |
| Ancla | `ancla_referencia`, `ancla_ff`, `ancla_lf` · T-ANCLA-REF, T-ANCLA-FF, T-ANCLA-LF | FL03 A0–A12 (INV-000069–000118) | 0 o más según el rol | GPT2-GEN | D1–D9 completos (`verificar_templates.py` L43). F26–F28 son contexto del clip, no instrucciones al prompt (decisión 2026-10-11 16:56). LF se arma como pareja de su FF y la QA comprueba ratio y continuidad; un FF solo no exige LF (PLAN_V5 L913; CONTRATOS L760) |

### Génesis por clase de sujeto

- **Persona:** plantilla T1 (INV-000604, 000553, 000558, 000561), armada con `armar.py` (CLAUDE.md). La regla de lente y cámara de la cara (24 §3) se escribe con el resultado visible en palabras, además del número (`camera-lighting-vocabulary.md:228`, taxonomía L1686–1695).
- **Lugar:** placa vacía, sin persona, una presión ambiental (INV-000607, 000555, 000560).
- **Edificación o landmark:** lugar real anclado por época y cultura, sin geometría exacta (INV-000431–000432, 000450–000452, 000476; `golden-rules.md:140–150`, INV-002298–002318).
- **Animal:** cabeza y pelaje antes que poses (INV-000433–000434, 000456, 000477, 000480).
- **Producto:** hero frontal antes que producto en escena (INV-000480). Etiquetas en quality high; logo nunca de texto (INV-000606, 000554, 000559, 000611).
- **Objeto:** legible en macro y en general (INV-000608).
- **Planta:** se trata como edificación o animal real. La ruta de grounding es FUERA DE ESTE CASO (INV-000220, 000605).

### Texto en la imagen (F32)

Solo es texto del mundo fotografiado: letrero, etiqueta o pantalla, nunca una marca real. Va en `texto_marca`:
literales, posición y tipografía (T-BRIEF-IMG L125–128; schema L665–692; PLAN_V5 L786–816). Su redacción:
- el literal va en su idioma, entre comillas rectas, dentro de un slot;
- el resto del prompt va en inglés (`text-rendering.md:146–149`);
- «no extra words, no duplicate text, no watermarks»;
- «100 percent readable and physically believable»;
- quality high si es pequeño o denso (`gpt-image.md:67–74`).

El tratamiento «comercial pulido» prohíbe texto en imagen (INV-000213), así que el caso con texto lleva otro.
El texto sobrepuesto (titular, CTA) nunca va en el prompt: se compone aparte (`revision/01_texto_en_imagen.md`).

### Redacción de GPT2-GEN en 5 slots (PLAN_V5 L831–850)

| Slot | Qué lleva |
|---|---|
| Scene | F16, con F05 y F30 ambiental, y el ratio |
| Subject | F15, F19, F13, F20, F21 |
| Important Details | F17, F18, F24, F25 y las materias de F30 |
| Use Case | F04 y la función del activo (F11, F12) |
| Constraints | las prohibiciones y preservaciones de las reglas seleccionadas, no una lista genérica de negativos |

## 4. Casos

Los aprobó Eric (decisiones 26 §16 y §17).

**Cobertura:**
- F10, F15 y F32 tienen un caso por valor.
- F11, F13, F14 y los valores fotográficos de F04 quedan cubiertos dentro de esos casos, cada valor al menos una vez.
- No entran: outpainting y upscaling (sin presencia en el corpus, taxonomía L4245–4246); colorizar manga; máscara; refinamiento conversacional.

**Entradas y aprobación:**
- Las imágenes de entrada salen de otros casos o de las entradas E1–E7 de la tabla de abajo. Eric puede sustituir cualquier entrada por un archivo suyo; se registra su sha256.
- Eric aprueba, cambia o quita cada caso al aprobar su brief (tarea 3).

| Caso | F10 · operación | F15 | F32 | F04 | F11 · F13 · F14 | Entradas | Plantilla o regla propia | Quality |
|---|---|---|---|---|---|---|---|---|
| K01 | génesis | persona (rostro maestro T1) | sin texto | retrato | — · A · — | — | `armar.py` | high |
| K02 | génesis | lugar genérico (agua abierta con clima, placa vacía) | sin texto | editorial | — · D · 07 | — | INV-000607 | usuario |
| K03 | génesis | edificación o landmark | sin texto | editorial | — · A · — | — | anclas de época y cultura | usuario |
| K04 | génesis | animal | sin texto | editorial | — · A · — | — | cabeza y pelaje primero | usuario |
| K05 | génesis | producto genérico, vaso de vidrio sin marca | sin texto | e-commerce o catálogo | — · A · — | — | hero frontal | usuario |
| K06 | génesis | objeto o prop (pelota en el impacto) | sin texto | key visual de campaña | — · B · 04 | — | INV-000608 | usuario |
| K07 | génesis | planta o especie vegetal | sin texto | editorial | — · A · — | — | lugar o especie real por época y cultura | usuario |
| K08 | génesis | lugar genérico con letrero pintado (no marca) | texto corto | miniatura | — · A · — | — | `gpt-image.md:21–27`, `:67–74` | usuario |
| K09 | génesis | producto con etiqueta genérica | texto extenso o pequeño | e-commerce o catálogo | — · A · — | — | `gpt-image.md:67–74`; etiqueta en high | high |
| K10 | composición | persona, cuerpo entero (T2) | sin texto | post o historia para redes | — · B · 06 | K01 | E5.3 | high |
| K11 | composición | persona en lugar (T3), sobre el agua | sin texto | póster o key art (titular aparte) | — · G · 01 | K01, K02 | E5.4 | high |
| K12 | composición | retrato de grupo, 3 miembros | sin texto | retrato (grupo, TRM-1260) | — · E · 09 | K01, G1, G2 (génesis T1 por miembro con `armar.py`, EN.1) | EN.1–EN.6 | high |
| K13 | composición | persona en multipanel 2×2 editorial | sin texto | storyboard o multipanel | — · A · — | K01 | `multi-panel.md` 2×2 (INV-002494, 002586–002590) | high |
| K14 | edición: quitar objeto | lugar | sin texto | editorial | — | K02 | `gpt-image.md:96` (INV-002383 corregido), `editing.md:10–19` | usuario |
| K15 | edición: añadir objeto | edificación | sin texto | editorial | — | K03 | `editing.md:21–27` | usuario |
| K16 | edición: cambiar luz o clima | edificación | sin texto | editorial | — | K03 | `gpt-image.md:98`; `editing.md:29–46` | usuario |
| K17 | edición: colorizar | persona en foto blanco y negro | sin texto | editorial | — | E5 | `editing.md:48–55` | high |
| K18 | edición: restaurar | foto antigua dañada | sin texto | editorial | — | E6 | `editing.md:65–71` | usuario |
| K19 | edición: traducir texto | producto con etiqueta | texto extenso o pequeño | e-commerce o catálogo | — | K09 | `editing.md:73–78` | high |
| K20 | edición: cambiar vestuario | persona | sin texto | post o historia para redes | — | K10 | `gpt-image.md:94` (INV-002382) | high |
| K21 | edición: cambiar mobiliario u objeto | interior | sin texto | visualización arquitectónica | — | K30 | `gpt-image.md:100` (INV-002385) | usuario |
| K22 | edición (cambio de fondo, misma persona) | persona | sin texto | post o historia para redes | — | K10 | `characters.md:80` (TRM-0511) | high |
| K23 | edición (textura de material) | edificación | sin texto | editorial | — | K03 | `editing.md:97–100` (TRM-0518) | usuario |
| K24 | edición (relleno con física) | producto (el vaso de K05) | sin texto | e-commerce o catálogo | — | K05 | `editing.md:91–95` (TRM-1142) | usuario |
| K25 | edición (adaptación de anuncio a otro mercado) | lugar con letrero | texto corto | miniatura | — | K08 | `editing.md:80–86` (TRM-0520) | usuario |
| K26 | transferencia de estilo | producto | sin texto | key visual de campaña | — | K05, K02 | `gpt-image.md` Style Transfer | usuario |
| K27 | boceto a final | objeto | sin texto | key visual de campaña | — | E1 | `structural.md` | usuario |
| K28 | boceto → concepto 3D | objeto | sin texto | key visual de campaña | — | E1 | `dimensional.md:20–27` | usuario |
| K29 | alzado → exterior | edificación | sin texto | visualización arquitectónica | — | E3 | `dimensional.md:51–59` | usuario |
| K30 | plano 2D → interior | lugar interior | sin texto | visualización arquitectónica | — | E2 | `dimensional.md:5–18`, `:61–68` | usuario |
| K31 | diseño plano → mockup de producto | producto | sin texto | UI o mockup | — | E4 | `dimensional.md:70–77` | usuario |
| K32 | descripción de imagen (`genesis`) | el de la foto | el de la foto | el de la foto | — | E7 | `vision-decomposer.md` paso 1 + 5 slots | según la foto |
| K33 | ancla | persona | sin texto | — | character ref · A · — | K01 | FL03 | high |
| K34 | ancla | lugar con multitud anónima | sin texto | — | environment ref · F · 08 | — | FL03 | usuario |
| K35 | ancla FF | vehículo en movimiento | sin texto | — | keyframe FF · C · 05 | — | FL03; T-ANCLA-FF | usuario |
| K36 | ancla LF, pareja de K35 | vehículo en movimiento | sin texto | — | keyframe LF · C · 05 | K35 | FL03; T-ANCLA-LF | usuario |
| K37 | ancla | gota u objeto que rompe la superficie del agua | sin texto | — | hero/macro · B · 02 | — | FL03 | usuario |
| K38 | ancla | detalle subacuático (burbujas, luz de superficie) | sin texto | — | motif insert · H · 03 | — | FL03 | usuario |

### Entradas que no se evalúan como casos

| Entrada | Qué es | Por qué no es caso |
|---|---|---|
| E1 | boceto lineal de un objeto | no es foto (26 §12) |
| E2 | plano 2D de una planta | no es foto (26 §12) |
| E3 | alzado de una fachada | no es foto (26 §12) |
| E4 | diseño plano de un empaque | no es foto (26 §12) |
| E5 | foto en blanco y negro de una persona | solo sirve de entrada a K17 |
| E6 | foto antigua dañada | solo sirve de entrada a K18 |
| E7 | la foto que Eric elige para la descripción | solo sirve de entrada a K32 |
| G1, G2 | maestros de rostro de los otros miembros de K12 | entradas de K12; mismo tipo que K01 |

Sus prompts los escribe el armador como génesis. Su QA comprueba solo que sirven de entrada: es blanco y negro, está
dañada, es un plano.

### Cobertura comprobable

| Faceta | Valores y casos |
|---|---|
| F10 | génesis K01–K09; composición K10–K13; edición K14–K25 (los 8 hijos K14–K21 y las 4 plantillas sin hijo K22–K25); transferencia K26; boceto K27–K31; descripción K32; ancla K33–K38 |
| F15 | persona K01; lugar genérico K02; edificación K03; animal K04; producto K05; objeto K06; planta K07 |
| F32 | sin texto (la mayoría); texto corto K08, K25; texto extenso o pequeño K09, K19 |
| F11 | character ref K33; environment ref K34; keyframe FF K35; keyframe LF K36; hero/macro K37; motif insert K38 |
| F13 | A K01; B K06; C K35; D K02; E K12; F K34; G K11; H K38 |
| F14 | 01 K11; 02 K37; 03 K38; 04 K06; 05 K35; 06 K10; 07 K02; 08 K34; 09 K12 |
| F04 | editorial K02; key visual de campaña K06; e-commerce o catálogo K05; retrato K01, K12; póster o key art K11; post o historia para redes K10; miniatura K08; UI o mockup (mockup fotografiado) K31; storyboard o multipanel (fotos) K13; visualización arquitectónica K29, K30 |

La tarea 2 comprueba esta tabla contra el esquema.

## 5. Tareas, en orden

Cada tarea termina con un control que sale con código 1 si no se cumple. Todo resultado se escribe en archivo y se sube
al repo al cerrar cada tarea.

1. **Universo y adenda.** Hechos: 2,724 textos (26 §18) y la adenda con 40 textos que entran, código 0.
   - Control: `textos_universo.py` regenera `universo_prueba_textos.jsonl` con 2,724 textos.
2. **Mapa en datos.** La tabla del §3 y la del §4 se pasan a `v3/prueba/mapa_tipos.json` y `v3/prueba/casos.json`. Control `verificar_mapa.py`:
   - una fila por operación del schema;
   - campos y mínimo de referencias iguales a `CONTRATOS_OPERACION_MODELO.json`;
   - adaptador igual a `model_adapters`;
   - cada INV citado existe en el universo o la adenda;
   - cada valor de F10, F15, F32, F11, F13, F14 y de los F04 del §4 aparece al menos en el caso que dice la tabla de cobertura;
   - cada valor está en `v2/esquema_taxonomia.json`.
3. **Casos y aprobación.** Por caso se escriben:
   - el brief en español;
   - la instancia del contrato (`entrada`, `procedencia_campos`, `modulos_activos`);
   - el caso del catálogo (`case.schema.json`), con valores de `v2/esquema_taxonomia.json` y las inferencias aparte.

   Lo propio de cada tipo:
   - **Persona sin referencias** (K01, G1, G2): llevan además el brief de `armar.py` con los campos de su `LEEME.md` (CLAUDE.md, paso 1). Las reglas T1 (ADD-0006, ADD-0007) que la tarea 4 marque aplicables entran por esos campos.
   - **Casos con texto:** llenan `texto_marca`. El valor de F32 va en `selecciones_taxonomicas`, porque F32 no tiene destino propio.
   - **Casos que no son edición:** activan el módulo fotografía.
   - **Descripción (K32):** cada valor leído de la foto entra con origen `inferencia_para_aprobacion`, con la foto y su sha256 como fuente.

   Aprobación:
   - Eric aprueba cada brief por su sha256 (serialización de `verificar_templates.py`).
   - `mensaje_id` es el uuid del evento de su mensaje en esta sesión (`list_events`).
   - En los casos con entradas se aprueba primero el contenido. Cuando existe la imagen de entrada se escribe su sha256 y Eric aprueba de nuevo, porque el cambio invalida la aprobación.

   Controles: `verificar_templates.validate_instance(caso, 'brief')` sin errores, y `casos/validar.py caso.json` sin errores tras la aprobación.
4. **Lista de referencia por caso (pregunta a).** Se lee completo cada texto del universo y de la adenda contra cada caso aprobado, sin facetas ni selector.
   - Cada par texto × caso se marca APLICABLE CONFIRMADA, FUERA DE ESTE CASO o EXCLUIDA POR DECISIÓN, con motivo (taxonomía §7.4).
   - Las reglas que piden otro modelo son FUERA DE ESTE CASO. Los textos de atribución a terceros son EXCLUIDA POR DECISIÓN (DEC-000024).
   - La lista se congela con sha256 en el repo antes de la tarea 6 (PILOTO §6.1).

   Control: `rule_answer_check.py` adaptado a ids INV y ADD y a las tres clases: 0 pares sin clase, 0 contradicciones, 0 ids desconocidos.
5. **Muestra de auditoría.** Por caso, el 10 % de los FUERA DE ESTE CASO (redondeo hacia arriba, mínimo 1), al azar con semilla publicada (decisión 26 §9). Eric marca cada uno.
   - Si encuentra un error: se corrige, se releen todos los FUERA de ese caso por la misma causa, se congela la lista nueva y se toma otra muestra.

   Control: la última muestra de cada caso tiene 0 errores.
6. **Clasificación de lo pertinente.** Se clasifican los textos APLICABLE CONFIRMADA en al menos un caso.
   - Formato: el del piloto (`v2/piloto_gpt-image/clasificacion.py`).
   - Condición: grupo TODAS / ALGUNA / NINGUNA de átomos sobre facetas y campos del contrato, con los operadores de `operador_atomo` (taxonomía §7.2).
   - La excepción es un subgrupo NINGUNA; la alternativa es otra aplicación del mismo id.

   Control: verificador de forma extendido (cada texto una vez, valores 100 % del esquema, grupos y operadores válidos).
7. **Discriminantes.** Control: cada faceta o campo que aparece en una condición tiene valor en cada caso (taxonomía §7.3). Si falta, se completa el brief, Eric lo aprueba de nuevo y se repite.
8. **Selector y cruce.** `seleccionar.py` evalúa F29, el paso y la condición §7.2. Devuelve por regla y caso una de las tres clases, con la traza de consulta: caso, valores evaluados, descartes por aplicación y motivo.
   - Antes de usarlo: pruebas unitarias por operador, por grupo y por excepción.

   Control: frente a la lista congelada, 0 faltantes y 0 sobrantes. Cada diferencia se resuelve releyendo el texto fuente y se registra qué se corrigió.
9. **Redacción y traza (pregunta b).**
   - **K01, G1 y G2** se arman con `armar.py` (CLAUDE.md), con su control de más de 300 palabras pasado de rechazo a aviso (26 §11). Su traza enlaza cada aplicación con el campo del brief de `armar.py` que la lleva, o con el texto fijo del programa que la cubre.
   - **Los demás** se arman con `armar_contrato.py`, que escribe la salida del contrato:
     - GPT2-GEN con el mapeo de slots del §3, o GPT2-EDIT con Change / Preserve / Constraints y la lista de preservación;
     - roles de referencia dentro de su slot;
     - Scene con el ratio;
     - prompt en inglés y texto del mundo entre comillas rectas en su idioma.
   - Cada aplicación seleccionada se enlaza con los 12 campos del `binding_contract` (CONTRATOS L671–687), con su slot como destino y su control como prueba.
   - Una regla cuyo efecto es un parámetro que la app no expone lleva ese destino (26 §8).

   Controles:
   - `validate_instance(caso, 'salida')` sin errores;
   - 0 aplicaciones con un campo vacío;
   - 0 apariciones de «photorealistic» o «fotorealista»;
   - 0 metadatos (Model, Quality, Size) dentro del cuerpo;
   - Quality high en los casos del §2;
   - aviso si el prompt o un slot pasa de 300 palabras.

   Si una aplicación necesita un dato que el brief no tiene, el armado se detiene: se completa el brief, Eric lo aprueba de nuevo y se repite desde la tarea 7 (ADD-0053).
10. **Entrega a Eric, paso a paso de la cadena.**
    - **Por prompt:** Model, Quality, Size / Ratio, References (cada Image N con su archivo y su rol), el prompt tal como lo escribe el armador, y Notes con lo inferido (ADD-0004, INV-002044).
    - **Formato del mensaje:** abre con la cabecera SKILL / RIESGOS / TÉCNICA. El prompt va en bloque cercado, con una línea `OVERRIDE: R1 - GPT2-GEN abre con el rótulo Scene: y el verbo dentro del slot (INV-002335)`.
    - **Control:** los tres gates de Stop (`gate_microgate`, `gate_dramaturgy`, `gate_image`), corridos en local sobre el mensaje, salen con código 0 antes de enviarlo.
    - **Instrucciones a Eric:**
      - un chat nuevo por prompt;
      - adjuntar exactamente los archivos indicados, en el orden de Image N;
      - subir aquí la imagen generada. Si el archivo no queda en el disco de la sesión, Eric lo sube por GitHub a `taller/catalogo/v3/prueba/imagenes/`.
    - El sha256 se calcula sobre ese archivo, y ese mismo archivo es el que Eric adjunta en el paso siguiente.
11. **QA y aceptación de cada imagen recibida.**
    - **Controles mecánicos, por script:**
      - sha256 y ratio del archivo contra el pedido;
      - hasta 1 % de desvío es corrección menor; más de 1 % bloquea (ADD-0043);
      - en LF (K36), mismo ratio que su FF.
    - **Controles visuales, por cada aplicación de la traza del caso,** con zoom al 100 % en lo que el caso tenga (ADD-0031; taxonomía L394–399):
      - rostro y manos en persona;
      - etiqueta y texto en K08, K09, K19 y K25: ortografía, kerning, fuente y textos que compiten (`failure-modes.md:45`);
      - arquitectura en edificación;
      - anatomía y pelaje en animal (INV-000477).
    - **Verificación contra la realidad:** en edificación, animal o planta reales, lo que el brief declara se compara con fotos del sujeto real (taxonomía L419–424, L1077–1081).
    - **Grupo (K12):** cada miembro contra su maestro.
    - **Descripción (K32):** el primer criterio es el parecido con la foto (26 §14).
    - Lo que no se puede verificar mirando la imagen se marca así, no como PASS (ADD-0047).
    - **Después, la crítica de `visual-asset-critic`:**
      - seis capas y veredicto ACCEPT / REVISE / REJECT;
      - JSON 1.1 con el sha256 de la imagen y del prompt, `generator` gpt-image-2, y `shot_id`, `brand_lock_ref` y `seed` en null (INV-009776–009871; taxonomía L2427–2442);
      - validada con `tools/validate_critique.py`;
      - escrita en `salida.aceptacion` del caso (schema L757–990; T-BRIEF-IMG L375–376).

    Control: ninguna imagen se da por buena sin las tablas mecánica y visual y la crítica validada escritas en el repo.
12. **Diagnóstico.** Si una imagen sale mal, Eric genera el mismo prompt por lo menos dos veces más (26 §10). Solo la falla que se repite se diagnostica:
    - **a** si la regla que la evita está en la lista de referencia y el selector no la tomó;
    - **b** si se tomó y el prompt no la cumple según su traza;
    - **c** si a y b pasan; entonces se sigue DEC-000004.

    No hay otro veredicto (26 §15). Los bucles de corrección posteriores siguen sus propias reglas: editar si el resultado es correcto en un 80 % o más, y máximo dos intentos por método (ADD-0029, ADD-0030; INV-000584–000591; 26 §10).

    Control: cada falla repetida tiene en el repo su veredicto a, b o c con la evidencia (entrada de la lista de referencia, traza del selector, traza del prompt).

## 6. Eventos inciertos y su mitigación, ya dentro de las tareas

| Evento | Mitigación |
|---|---|
| Una regla de la lista de referencia mal clasificada | muestra de auditoría con corrección y relectura (tarea 5) y cruce 0/0 (tarea 8) |
| El selector no evalúa una excepción o un operador | condición §7.2 (tarea 6) y pruebas unitarias antes del cruce (tarea 8) |
| Falta un dato que decide una regla | control de discriminantes y nueva aprobación (tarea 7) |
| Una entrada no sirve (no es blanco y negro, no está dañada, no es un plano) | se rehace la entrada antes del caso; Eric puede poner un archivo suyo (§4) |
| Un gate del repo bloquea la entrega | gates corridos en local con código 0 antes de enviar (tarea 10) |
| La imagen subida no llega al disco | subida por GitHub a la carpeta indicada (tarea 10) |
| El generador arrastra contexto de otra imagen | chat nuevo por prompt y referencias adjuntas (§2) |
| La imagen sale con otro ratio, porque la app no expone el parámetro | ratio dentro de Scene (§2) y QA de ratio con tolerancia del 1 % (tarea 11) |
| Pérdida de estado por compactación del contexto | cada tarea escribe archivos y se sube al repo; los controles recalculan desde archivos |

## 7. Dudas que solo Eric puede resolver

Ninguna.

Eric aprueba los briefs (tarea 3), puede sustituir entradas (§4), revisa la muestra (tarea 5) y elige la foto de K32 (E7). Todo eso son pasos del método, no dudas abiertas.
