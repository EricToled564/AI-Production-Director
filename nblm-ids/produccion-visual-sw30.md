# Reglas del skill: produccion-visual-sw30

45 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## produccion-visual-sw30/SKILL.md

- [dadff5459383] respuesta honesta a esta pregunta no sea SÍ SIN MATICES:
- [67008f8c2960] Si la respuesta es NO: no se entrega. Se leen los archivos faltantes, se aplica lo que falte y
- [ab216a6c933f] Prohibido responder SÍ para complacer. Un SÍ falso es una mentira y cuesta más que el NO.
- [5c17fa63163e] Prohibido responder SÍ con matices, condiciones o notas al pie disfrazadas de honestidad.
- [760b8e4708d1] (SKILL.md indica el orden obligatorio), no fragmentos ni grep.
- [26da6aecb6fb] Orden de dirección: nunca se escribe un prompt de corrido ni se parchea texto. Tres pasos, en este orden:
- [e420b46bb400] **CATALOGAR** — identificar el TIPO de prompt y leer qué reglas aplican a ese tipo en la matriz
- [2d922b05c376] **DEFINIR SECCIONES** — antes de redactar, listar las secciones que ese tipo exige. Cada regla vive
- [6ca53cccfb89] colour, hair, fabric, clean_*, autocontain_*), nunca en texto suelto dentro del brief.
- [91c96c167fa3] **ENSAMBLAR POR SECCIÓN** — el prompt se construye llamando P(scene, subject, [details], mood,
- [34d661f0601e] `rule_registry.py` — relee los 23 archivos del skill image y EXTRAE mecánicamente cada enunciado
- [33f4eb1675f2] `rule_ledger.py` — obliga a que CADA regla aplicable tenga disposición explícita: CHECK (existe
- [b37aa531231e] `audit_gi2.py` — verifica los prompts columna por columna.
- [d39e08ccf999] Sección | Bloque obligatorio | Por qué
- [5a5348b20c81] usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO en rostros
- [7ba769efe2d7] `production-package/template_engine.py` es OBLIGATORIO para construir cualquier prompt visual.
- [c0bc3ce2b122] Un prompt no se escribe: se INSTANCIA con `build(tipo, ..., notes=...)`. El motor lanza
- [08823c86198b] **PROHIBIDO editar el texto de un brief individual.** Eso es parchar: arregla una cosa y rompe otra,
- [bebb99bf97f5] Un solo trabajo por generación. Con dos personajes: un sujeto por generación, o técnica
- [faf775460a18] de colocación probada; nunca "a ver si sale".
- [a384c44a2c78] Posición SIEMPRE por ancla legible de la propia imagen (letterforms del mundo: "his back
- [8ec5e9322188] level with the letter L of WORLD"). Prohibido "left half", "centre", "just left of X".
- [cbef3fae6beb] El editor no tiene memoria: solo verbos operativos (Move/Replace/Add/Remove/Swap), cero
- [cb50b580f819] Autocontención: toda comparación ("same X") exige ambos referentes adjuntos en ESE prompt.
- [521775e327c8] Herencia mínima: "same face and clothes" + solo los deltas. Cero re-descripción de lo que
- [51cca5b2efc6] Swap de identidad = última operación, sola: "Replace X with Y — same position, same pose,
- [b9c774059bf0] Mundos por dos pasos: placa vacía primero; insert con "use only the person from image N,
- [b6df20344be1] Stills en instante congelado ("frozen mid-stride"); nada de movimiento en imagen fija.
- [da9c2b7805b2] Contactos entre personas: "a natural high five" — la anatomía la fija el keyframe
- [5a6617eee79e] aprobado, nunca la asignación de manos por texto.
- [0f5ddb9db10d] Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los
- [0cdb2895402f] cuerpos nunca tapan logo ni lettering en frames congelados.
- [0895bf9c3c72] Lo aprobado se canoniza con hash y se EDITA desde ahí; lo caro nunca se regenera.
- [ad949972d434] "Edit, don't re-roll": resultado ≥80% correcto → cambio puntual (hasta 3 ediciones
- [aabccd80baaf] apiladas), nunca re-tirar.
- [fa22c737a647] Máximo 2 intentos por método. A la 2ª falla: cambio de método con causa declarada, o
- [55b0509b18b5] alto y consulta. Nunca tercera vuelta de lo mismo.
- [86d8cbf3a110] Validadores del paquete y techos de palabras en verde antes de entregar; inspección
- [0e2d999b1256] visual propia (zooms 100% de rostros y manos) antes de presentar. Si algo falla: no se
- [aeb5f5e9292c] shots.json es la fuente de verdad: todo cambio entra ahí primero y se propaga.
- [0e27fd6783a1] Clips: solo Preserve-cues, roles de start/tail ("The tail image defines X — inherit
- [23a76633c745] Entregas en unidades chicas con OK de dirección; se entrega el delta, no el paquete.
- [abcfd077a336] Respuestas: el dato o entregable en la primera línea. Cero adulación y cero evaluación
- [9d8d3f84a47e] Prohibido afirmar capacidades, límites o hechos de plataforma sin verificarlos en este
- [229b9b46e2e4] /research solo para problemas genuinamente nuevos; /briefing solo al retomar tras días