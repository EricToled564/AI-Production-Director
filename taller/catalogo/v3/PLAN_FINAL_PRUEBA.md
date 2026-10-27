# Plan final de la prueba — sistema de prompts para GPT Image 2 (2026-10-27)

## 1. Objetivo y qué demuestra la prueba

El sistema convierte un brief en prompts de GPT Image 2 que den imágenes de apariencia fotográfica y alta calidad al
primer intento. Eric genera las imágenes en la App de ChatGPT para escritorio (decisión 26 §8). La prueba demuestra,
para cada caso, que el sistema selecciona todas las reglas que aplican y que cada prompt las cumple; si una imagen sale
mal, dice si falló la selección (a), el prompt (b) o falta la regla en el corpus (c). Método: universo → filtro por
caso → controles de completitud → clasificación de lo pertinente → prueba del selector (decisión 24 §4). El alcance no
cambia. Lo leído para escribir este plan está en `LECTURA_PLAN.md` y `LECTURA_4_DOCUMENTOS.md`.

## 2. Reglas comunes a todos los tipos de imagen

| Regla | Fuente |
|---|---|
| Solo GPT Image 2 | decisión 23 §6 |
| Universo: textos de generación de imágenes universales, parcialmente universales con GPT Image 2 y específicos de GPT Image 2 (2,722 + 40 de la adenda) | decisión 24 §1; `v3/universo`, `v3/universo/adenda` |
| Cifra de GPT Image 2 cuando un texto da la de otro modelo | decisión 26 §1 |
| Etiquetas 100 % de la taxonomía o de una extensión aprobada; sin pendientes ni NO APLICA | decisiones 23 §3, §5 |
| Brief en español; prompt siempre en inglés | `taller/recursos/directivas_taller.json` (ERIC-IDIOMA-PROMPT-INGLES) |
| Prohibidos «photorealistic» y «fotorealista»; Aurora excluida; el vocabulario prohibido gana | CLAUDE.md; `user_directives.json`; PILOTO §0.4; taxonomía §6.2 |
| Formato escrito en el texto (Scene nombra el ratio); tamaño y quality como referencia; sin máscara | decisión 26 §8 |
| Model, Quality, Size, References y Notes van fuera del cuerpo del prompt. El ratio va además dentro de Scene: la app no expone parámetros (26 §8), y ADD-0042 pide el parámetro solo «when the platform exposes them»; en ese punto 26 §8 manda sobre ADD-0011 | ADD-0004, ADD-0010, ADD-0011, ADD-0042; decisión 26 §8 |
| Ninguna atribución a terceros en material al cliente | DEC-000024 |
| Longitud: objetivo alrededor de 250 palabras; aviso si el prompt o un slot pasa de 300; la longitud nunca se resuelve suprimiendo reglas aplicables. En K01, `armar.py` rechaza más de 300 (L84–85): duda 2 del §7 | ADD-0008; T-BRIEF-IMG L355; DECISIONES.md decisión 2; CLAUDE.md |
| Aceptar una imagen solo después de su QA, con los controles mecánicos separados de los visuales | ADD-0047 |
| Un chat nuevo por prompt y las referencias adjuntas en cada uno: el generador no conserva estado | INV-012218; cierra `CONTRADICCIONES.md` §4 |
| Brief aprobado por Eric ligado a su sha256; cualquier cambio invalida la aprobación | T-BRIEF-IMG L13–15; schema L1333–1352; PILOTO §5 |

## 3. Mapa por tipo de imagen

Tipos: menú de DEC-000009 (génesis, ancla sin referencia, ancla con referencia, edición) y las 8 operaciones del
contrato (schema L45–54, `CONTRATOS_OPERACION_MODELO.json` L4–362). Toda operación lleva los 12 campos «siempre»
(ruta.flujo, operacion, modelo nombre/versión/interfaz, pieza tipo/objetivo/uso, formato.ratio, idioma_prompt,
restricciones, selecciones_taxonomicas), `procedencia_campos` por valor y `aprobacion_brief`. Los módulos condicionales
(fotografía, acción física, sujetos visibles, materialidad; CONTRATOS L775–819) se activan en el brief aprobado.

| Tipo (F10) | Operación · template | Flujo y técnica | Referencias | Campos propios | Salida | Lo que la gobierna |
|---|---|---|---|---|---|---|
| Génesis sin referencias | `genesis` · T-GENESIS | FL04 D01–D05 (taxonomía L257–261); técnica FL02 E5.2 (INV-000525–000614 del universo; INV-000529, 000542, 000543 y 000546 salieron por ser solo de Nano Banana) | 0 (INV-000610) | sujetos, escena | GPT2-GEN | Por clase de sujeto (INV-000539, 000593): persona → plantilla T1 (INV-000604, 000553, 000558, 000561) armada con `armar.py` (CLAUDE.md); lugar → placa vacía, sin persona, una presión ambiental (INV-000607, 000555, 000560); producto → etiquetas en quality high, logo nunca de texto, marca real solo con referencia (INV-000606, 000554, 000559, 000611); objeto → legible en macro y en general (INV-000608). Edificación, animal y planta: la fuente pide grounding de Nano Banana 2 (INV-000605), fuera del alcance (decisiones 23 §6, 24 §1) |
| Composición con referencias | `composicion_referencias` · T-REF-COMP | FL04; técnica E5.3 (cuerpo T2 con el rostro adjunto) y E5.4 (persona en lugar, mundos por dos pasos) | ≥1, cada una con índice, rol y preservaciones | referencias, composicion | GPT2-GEN; el rol de cada imagen va dentro del slot que gobierna (verificar_templates L65: nada antes de «Scene:») | INV-000395, 000396, 000428, 000474, 000486–000487, 000490, 000508–000512, 000590, 000203; taxonomía L263 (con referencias no es génesis; una imagen independiente no es ancla); «Rostro T1 antes que cuerpo T2, siempre» (DECISIONES.md); hasta 16 referencias con rol (INV-002054 corregido) |
| Edición | `edicion` · T-EDIT | FL04; técnica E5.5 | ≥1 (la imagen a editar) | edicion.cambio, edicion.preservar, referencias | GPT2-EDIT: Change / Preserve / Constraints, un cambio por iteración | INV-000397, 000584–000585; `editing.md` (INV-002021); hijos de F10 de la decisión 23 §4; sin máscara (26 §8) |
| Transferencia de estilo | `transferencia_estilo` · T-STYLE | FL04 | ≥1 | transferencia.propiedades, referencias | GPT2-GEN | `vision-decomposer.md` (INV-002027), con la duda del §7 |
| Boceto a final | `boceto_a_final` · T-SKETCH | FL04 | ≥1 (el boceto) | boceto.estructura_preservada, referencias | GPT2-GEN | `structural.md` (INV-002025) |
| Ancla sin referencia | `ancla_referencia` (0 refs) · T-ANCLA-REF | FL03 A0–A12 (INV-000069–000118) | 0 | ancla.rol (F11), ancla.invariantes; D1–D9 completos (verificar_templates L43) | GPT2-GEN | F26–F28 son contexto del clip, no instrucciones al prompt (decisión 2026-10-11 16:56) |
| Ancla con referencia | `ancla_referencia`, `ancla_ff`, `ancla_lf` | FL03 | ≥1 | además estado inicial o final y contexto del clip (cámara, transición, audio; efectivo incluso cámara fija y silencio) | GPT2-GEN | ídem |

F10 «análisis de imagen a prompt» no es operación del contrato (schema L45–54) y no produce una imagen: no tiene caso
propio. `vision-decomposer.md` sí entra por la transferencia de estilo (INV-002027), y con él `CONTRADICCIONES.md` §3
(duda del §7). Todos los casos llevan F32 «sin texto».

## 4. Casos: instancias del mapa

Cadena propuesta. Las imágenes de entrada salen de pasos anteriores de la misma prueba; nada depende de fotos
externas. Eric aprueba, cambia o quita cada caso al aprobar su brief.

| Caso | Tipo | Entradas |
|---|---|---|
| K01 | génesis · persona · rostro maestro T1 | — |
| K02 | génesis · lugar · placa vacía | — |
| K03 | composición · persona en lugar, plano medio | K01, K02 |
| K04 | composición · cuerpo entero con el rostro adjunto (T2) | K01 |
| K05 | edición · un cambio sobre K03 | K03 |
| K06 | génesis · producto genérico sin marca real | — |
| K07 | transferencia de estilo · luz y grade de K02 sobre el contenido de K06 | K06, K02 |
| K08 | génesis · boceto lineal (F18 ilustración) | — |
| K09 | boceto a final desde K08 | K08 |
| K10 | ancla sin referencia · environment ref | — |
| K11 | ancla con referencia · character ref | K01 |
| K12, K13 | ancla con referencia · keyframes FF y LF de un mismo clip | K01, K10 |

## 5. Tareas, en orden

Cada tarea termina con un control que sale con código 1 si no se cumple. Todo resultado se escribe en archivo y se
sube al repo al cerrar cada tarea.

1. **Adenda del universo.** Hecha: `v3/universo/adenda/construir_adenda.py`, 125 textos, 40 entran, código 0.
2. **Mapa en datos.** La tabla del §3 como `v3/prueba/mapa_tipos.json`. Control `verificar_mapa.py`: una fila por
   operación del schema; campos y mínimo de referencias iguales a `CONTRATOS_OPERACION_MODELO.json`; adaptador igual a
   `model_adapters`; cada INV citado existe en el universo o la adenda.
3. **Casos y aprobación.** Por caso: brief en español, instancia del contrato (`entrada`, `procedencia_campos`,
   `modulos_activos`) y caso del catálogo (`case.schema.json`), con valores de `v2/esquema_taxonomia.json` y las
   inferencias aparte. K01 lleva además el brief de `armar.py` con los campos de su `LEEME.md` (CLAUDE.md, paso 1);
   las reglas del template T1 (ADD-0006, ADD-0007) que la tarea 4 marque aplicables entran por esos campos. Controles: `verificar_templates.validate_instance(caso, 'brief')` sin errores y
   `casos/validar.py caso.json` sin errores tras la aprobación. Eric aprueba cada brief por su sha256 (serialización de
   `verificar_templates.py`); `mensaje_id` es el uuid del evento de su mensaje en esta sesión (`list_events`). En los
   casos con entradas se aprueba primero el contenido; cuando existe la imagen de entrada se escribe su sha256 y Eric
   aprueba de nuevo (el cambio invalida la aprobación).
4. **Lista de referencia por caso (pregunta a).** Leer completo cada texto del universo y de la adenda contra cada caso
   aprobado, sin facetas ni selector, y marcar APLICABLE CONFIRMADA, FUERA DE ESTE CASO o EXCLUIDA POR DECISIÓN con
   motivo (taxonomía §7.4); los textos de atribución a terceros son EXCLUIDA POR DECISIÓN (DEC-000024). Se congela con
   sha256 en el repo antes de la tarea 6 (PILOTO §6.1). Control: `rule_answer_check.py` adaptado a ids INV y ADD y a
   las tres clases: 0 pares texto × caso sin clase, 0 contradicciones, 0 ids desconocidos.
5. **Muestra de auditoría.** Por caso, el 10 % de los FUERA DE ESTE CASO, redondeo hacia arriba, mínimo 1, al azar con
   semilla publicada (decisión 26 §9). Eric marca cada uno. Si encuentra un error: se corrige, se releen todos los FUERA
   de ese caso por la misma causa, se congela la lista nueva y se toma otra muestra. Control: última muestra de cada
   caso con 0 errores.
6. **Clasificación de lo pertinente.** Los textos APLICABLE CONFIRMADA en al menos un caso, con el formato del piloto
   (`v2/piloto_gpt-image/clasificacion.py`) y la condición escrita como grupo TODAS / ALGUNA / NINGUNA de átomos sobre
   facetas y campos del contrato con los operadores de `operador_atomo` (taxonomía §7.2): la excepción es un subgrupo
   NINGUNA y la alternativa, otra aplicación del mismo id. Control: verificador de forma extendido (cada texto una vez,
   valores 100 % del esquema, grupos y operadores válidos).
7. **Discriminantes.** Control: cada faceta o campo que aparece en una condición tiene valor en cada caso (taxonomía
   §7.3). Si falta, se completa el brief, Eric lo aprueba de nuevo y se repite.
8. **Selector y cruce.** `seleccionar.py` evalúa F29, el paso y la condición §7.2 y devuelve por regla y caso una de
   las tres clases, con la traza de consulta (caso, valores evaluados, descartes por aplicación, motivo). Antes de usarlo,
   pruebas unitarias por operador, por grupo y por excepción. Control: frente a la lista congelada, 0 faltantes y 0
   sobrantes; cada diferencia se resuelve releyendo el texto fuente y se registra qué se corrigió.
9. **Redacción y traza (pregunta b).** K01 con `armar.py` (CLAUDE.md); su traza enlaza cada aplicación con el campo
   del brief de `armar.py` que la lleva o con el texto fijo del programa que la cubre. Los demás con `armar_contrato.py`, que escribe
   la salida del contrato: GPT2-GEN o GPT2-EDIT, roles de referencia dentro de su slot, Scene con el ratio, prompt en
   inglés. Cada aplicación seleccionada se enlaza con los 12 campos del `binding_contract` (CONTRATOS L671–687), con su
   slot como destino y su control como prueba; una regla cuyo efecto es un parámetro que la app no expone lleva ese
   destino (decisión 26 §8). Controles: `validate_instance(caso, 'salida')` sin errores; 0 aplicaciones con un campo
   vacío; 0 apariciones de «photorealistic» o «fotorealista»; 0 metadatos (Model, Quality, Size) dentro del cuerpo;
   aviso si el prompt o un slot pasa de 300 palabras. Si una aplicación necesita un dato que el brief no tiene, el
   armado se detiene: se completa el brief, Eric lo aprueba de nuevo y se repite desde la tarea 7 (ADD-0053).
10. **Entrega a Eric, paso a paso de la cadena.** Por prompt: Model, Quality, Size / Ratio, References (cada Image N con
    su archivo y su rol), el prompt tal como lo escribe el armador, y Notes con lo inferido (ADD-0004, INV-002044). El mensaje abre con la cabecera SKILL / RIESGOS / TÉCNICA,
    el prompt va en bloque cercado y una línea `OVERRIDE: R1 - GPT2-GEN abre con el rótulo Scene: y el verbo dentro del
    slot (INV-002335)`. Control: los tres gates de Stop (`gate_microgate`, `gate_dramaturgy`, `gate_image`) corridos en
    local sobre el mensaje salen con código 0 antes de enviarlo. Instrucciones a Eric: un chat nuevo por prompt; adjuntar
    exactamente los archivos indicados en el orden de Image N; subir aquí la imagen generada. Si el archivo subido no
    queda en el disco de la sesión, Eric lo sube por GitHub a `taller/catalogo/v3/prueba/imagenes/`. El sha256 se
    calcula sobre ese archivo, y ese mismo archivo es el que Eric adjunta en el paso siguiente.
11. **QA de cada imagen recibida.** Controles mecánicos, por script: sha256 y ratio del archivo contra el pedido; hasta
    1 % de desvío es corrección menor, más de 1 % bloquea (ADD-0043). Controles visuales, por cada aplicación de la
    traza del caso, con zoom al 100 % de rostros y manos cuando el caso los tiene (ADD-0031). Lo que no se puede
    verificar mirando la imagen se marca así, no como PASS (ADD-0047). Control: ninguna imagen se da por buena sin
    las dos tablas escritas en el repo.
12. **Diagnóstico.** Si una imagen sale mal, Eric genera el mismo prompt por lo menos dos veces más (decisión 26 §10).
    Solo la falla que se repite se diagnostica: a si la regla que la evita está en la lista de referencia y el selector
    no la tomó; b si se tomó y el prompt no la cumple según su traza; c si a y b pasan, y entonces se sigue DEC-000004.
    La repetición para diagnosticar es la de 26 §10. Los bucles de corrección posteriores siguen sus propias reglas:
    editar si el resultado es correcto en un 80 % o más, y máximo dos intentos por método (ADD-0029, ADD-0030;
    INV-000584–000591; 26 §10). Control: cada falla repetida tiene en el repo su veredicto a, b o c con la evidencia
    (entrada de la lista de referencia, traza del selector, traza del prompt).

## 6. Eventos inciertos y su mitigación, ya dentro de las tareas

| Evento | Mitigación |
|---|---|
| Una regla de la lista de referencia mal clasificada | muestra de auditoría con corrección y relectura (tarea 5) y cruce 0/0 (tarea 8) |
| El selector no evalúa una excepción o un operador | condición §7.2 (tarea 6) y pruebas unitarias antes del cruce (tarea 8) |
| Falta un dato que decide una regla | control de discriminantes y nueva aprobación (tarea 7) |
| Un gate del repo bloquea la entrega | gates corridos en local con código 0 antes de enviar (tarea 10) |
| La imagen subida no llega al disco | subida por GitHub a la carpeta indicada (tarea 10) |
| El generador arrastra contexto de otra imagen | chat nuevo por prompt y referencias adjuntas (§2) |
| La imagen sale con otro ratio, porque la app no expone el parámetro | ratio dentro de Scene (§2) y QA de ratio con tolerancia del 1 % (tarea 11) |
| Pérdida de estado por compactación del contexto | cada tarea escribe archivos y se sube al repo; los controles recalculan desde archivos |

## 7. Dudas que solo Eric puede resolver

Las dos se necesitan antes de la tarea 9 y no detienen las tareas 2 a 8.

**1.** `image/SKILL.md:63` (INV-002027) manda cargar `vision-decomposer.md` «whenever the user attaches an image and asks
to recreate, match, decompose, or transfer its style». Aplica a K07 y a cualquier otro caso en que la tarea 4 lo
marque. Ese archivo pide «solo keywords separadas por comas» (`:61`), contra los 5 slots de `gpt-image.md:7–15`; está
registrado como pendiente de Eric en `v3/universo/CONTRADICCIONES.md` §3.

Para GPT Image 2, ¿el resultado de vision-decomposer se reescribe a los 5 slots o se entrega como keywords?
Recomendación: 5 slots, por `image/SKILL.md:46` («The model file is non-negotiable»), `:112` y DEC-000025 (los
templates siguen la sintaxis del modelo). Vale para todos los casos.

**2.** `armar.py` (obligatorio para K01 por CLAUDE.md) rechaza un prompt de más de 300 palabras (L84–85), y CLAUDE.md
prohíbe entregar un prompt rechazado. La decisión 2 de `.claude/rules/DECISIONES.md` dice que el conteo de palabras
nunca bloquea y que los prompts de 5 slots de GPT Image pasan; T-BRIEF-IMG L355 llama a 300 «techo editorial» y dice
que la longitud nunca se resuelve suprimiendo reglas aplicables. Si K01, con todas sus reglas aplicables, no cabe en 300
palabras, ¿el exceso de `armar.py` pasa a aviso o se mantiene el rechazo? Recomendación: aviso solo cuando no se pueda
acortar la redacción sin perder una regla aplicable, por L355 y la decisión 2. La respuesta vale para K01 y para
cualquier otro retrato de una persona sin referencias.

Eric aprueba los briefs (tarea 3) y revisa la muestra (tarea 5): son pasos del método, no dudas.
