# Registro de lectura de los documentos rectores con el plan delante — 2026-10-27

Regla de CLAUDE.md «Toda lectura deja registro en el repo». Alcance vigente: decisión 26 §12 (cada tipo de imagen
fotográfica con caso propio). Cada fila: líneas leídas, qué dicen y su consecuencia para el plan (C = cambia el plan;
N = no lo cambia, con el motivo). Los registros previos (`v3/LECTURA_4_DOCUMENTOS.md`, `v3/LECTURA_PLAN.md`) se hicieron
para el alcance anterior; este archivo los completa y, donde difieren, manda este.

## 1. T-BRIEF-IMG — `fuentes_20261019/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md` (387 líneas, leídas completas)

| Líneas | Qué dice | Consecuencia |
|---|---|---|
| L1–3 | contratos rellenables; `{{campo}}` nunca va al prompt final | N: el armador no deja variables (lo comprueba `verificar_templates.py`) |
| L6 | autoridad: `gpt-image.md` gobierna los 5 slots y los 3 de edición; los tres párrafos del adaptador no cambian esa estructura; `_capabilities.json` no se extrapola; «photorealistic» se sustituye por atributos observables; el verbo inicial no añade nada antes de `Scene:` | N: ya en el plan (§2, tarea 10) |
| L7 | el paquete cubre entrada y salida de imagen, FF/LF incluidos, y compuertas de orquestación | N |
| L10–18 | secuencia obligatoria: flujo y operación → valores e inferencias → campos dependientes → brief completo → aprobación por hash → selección definitiva → compilar → validar y entregar → criticar y canonizar | N: es el orden de tareas 3 a 12 del plan |
| L19 | ningún campo vacío habilita la selección; sin NO APLICA; «un contrato técnico insuficiente bloquea la ejecución, no la recuperación de reglas» | C: el caso de descripción de imagen no tiene contrato de operación: sin decidir cómo se contrata no se puede ejecutar (pregunta 2 de `04_preguntas_eric.md`) |
| L22–134 | ficha T-BRIEF-IMG: campos, cuándo se exigen y su faceta | N: es la entrada del contrato de la tarea 3 |
| L122 | `edicion.mascara` solo si el modelo o la interfaz la admite | N: sin máscara (26 §8) |
| L125–128 | `texto_marca.literales`, `posicion`, `tipografia` cuando se pide «texto integrado»; `logos_aprobados` solo con marca autorizada | C: la ficha ya prevé el texto dentro de la imagen; los casos de F32 con texto llenan esos campos (`01_texto_en_imagen.md`) |
| L129–130 | `texto_integrado_override` solo para Ideogram | N: no aplica a GPT Image 2 |
| L131–132 | campos de grounding | N: solo Nano Banana (excluido por 23 §6) |
| L133 | presupuesto de créditos antes de ejecutar con costo | N: Eric genera en la app; sin API |
| L136 | procedencia por campo; la inferencia no es hecho hasta aprobarse | N: tarea 3 |
| L139–140 | D1–D9 de ancla resueltos antes de compilar; FF/LF con cámara, transición y audio positivos; génesis de proyecto hereda series_lock y plan_anchors si existen | N: §3 del plan |
| L144–182 | contratos T-GENESIS, T-REF-COMP, T-ANCLA-REF (character, environment, hero-macro, motif insert), T-ANCLA-FF, T-ANCLA-LF, T-EDIT (un cambio), T-STYLE, T-SKETCH | C: `ancla_referencia` cubre cuatro roles de F11; hero/macro y motif insert también necesitan caso si F11 cuenta como tipo (pregunta 1) |
| L187–209 | GPT2-GEN (5 slots) y GPT2-EDIT (Change/Preserve/Constraints); quality y tamaño fuera | N: tarea 9 |
| L213–349 | plantillas de Nano Banana, Flux, Midjourney, Ideogram, Seedream, GPT 1.5 y migraciones | N: otros modelos (23 §6) |
| L352 | serialización de Nano Banana | N |
| L353 | GPT Image 2: 5 slots, edición de un cambio, referencias con rol, quality y size fuera; «los patrones especializados de texto/infografía … no sustituir automáticamente los cinco slots sin resolver la autoridad específica de su operación» | C: el caso con texto conserva los 5 slots; el texto literal entre comillas va dentro de un slot (como el letrero de `gpt-image.md:21–27`) o en la línea `Text:` de la plantilla «Marketing Creative with Text» (`gpt-image.md:158–168`), que el validador admite porque solo cuenta los rótulos de slot; «Quality: high» de esa plantilla va fuera del cuerpo (ADD-0011) |
| L354 | serialización de otros modelos | N |
| L355 | techos editoriales; GPT 300; la longitud nunca se resuelve suprimiendo reglas | N: §2 del plan (26 §11) |
| L357–369 | salida común Model / Quality / Size / Prompt / Notes; traza aparte | N: tarea 10 |
| L371–373 | T-ORQ: gates base | N: tareas 3 a 12 |
| L375–376 | T-ACEPTACIÓN: activo y hash, prompt y hash, brief y hash, resultados por control, ronda; `critique.json` desde `salida.aceptacion.critique`; auditoría de tres detalles con evidencia; los seis controles de dramaturgia cuando se exigen | C: la QA de la tarea 11 escribe el registro de aceptación con estos campos y la crítica del `visual-asset-critic` (ver `05_lectura_universo.md`, 009776–009871) |
| L377 | T-TRAZA: cada aplicación con sus 12 campos de enlace; decisiones con cita verificable | N: tarea 9 |
| L380–381 | REGISTRO_DESTINOS resuelve 31 facetas; `verificar_templates.py` acredita estructura, no pertinencia | N |
| L383–384 | atribución CC BY 4.0 | N: DEC-000024 rige el material al cliente |
| L386–387 | obligatoriedad por módulo: cámara y luz solo cuando hay que definir la toma | N: tarea 3 (módulo fotografía) |

## 2. Contratos — `…/templates/CONTRATOS_OPERACION_MODELO.json` (820 líneas, leídas completas)

| Líneas | Qué dice | Consecuencia |
|---|---|---|
| L4–47 | T-GENESIS: 12 campos base + `sujetos` + `escena`; 0 referencias; cambiar modelo, operación, referencias, identidad o formato invalida aprobación, selección, prompt, validaciones y aceptación | N: tarea 3 y control de re-aprobación |
| L48–91 | T-REF-COMP: + `referencias` + `composicion`; ≥1 referencia con roles y preservaciones | N |
| L92–135 | T-ANCLA-REF: + `ancla.rol` + `ancla.invariantes`; 0 o más referencias; roles character, environment, hero-macro, motif insert | C: igual que T-BRIEF L144–182 (hero/macro y motif insert según pregunta 1) |
| L136–229 | T-ANCLA-FF y T-ANCLA-LF: + estado inicial o final + contexto del clip (cámara, transición, audio); 0 o más referencias | N: §3 del plan |
| L230–274 | T-EDIT: + `edicion.cambio` + `edicion.preservar` + `referencias`; ≥1; un cambio por iteración | N: cada hijo de edición es una instancia de T-EDIT con un solo cambio |
| L275–318 | T-STYLE: + `transferencia.propiedades` + `referencias`; ≥1 | N: K07 |
| L319–362 | T-SKETCH: + `boceto.estructura_preservada` + `referencias`; ≥1 | N: vale para boceto (`structural.md`) y para plano 2D (`dimensional.md`) |
| L364–414 | GPT2-GEN para 7 operaciones y GPT2-EDIT para edición; params quality y tamaño | N: tarea 9 |
| L415–669 | adaptadores de Nano Banana, Flux, Midjourney, Ideogram, Seedream, GPT 1.5 y migraciones | N: otros modelos (23 §6) |
| L671–687 | `binding_contract`: 12 campos de enlace por aplicación | N: tarea 9 |
| L688–748 | contratos de variante de Nano Banana (límites de referencias, grounding solo NB2) | N: excluido por 23 §6; el grounding es la regla que el veredicto d nombra (pregunta 3) |
| L749–773 | serialización de parámetros: GPT Image 2 size y quality | N: la app no los expone (26 §8) |
| L774 | «las combinaciones modelo/operación sin adaptador completo … hay que resolver contrato técnico antes de ejecución. No generar prompt de una combinación usando por defecto un adaptador ajeno» | C: la descripción de imagen no tiene contrato; no se ejecuta sin la respuesta a la pregunta 2 |
| L775–790 | módulo fotografía: plano, ángulo, efecto óptico, luz fuente, dirección, dureza, distribución y contraste cuando el brief exige imagen fotográfica y nueva toma; una edición que preserva no lo exige | C: con 26 §12 todo caso que no sea edición activa el módulo fotografía; la tarea 3 lo marca en `modulos_activos` |
| L791–818 | módulos acción física, sujetos visibles y materialidad, por caso y fuente | N: tarea 3 |

## 3. Schema — `…/templates/CONTRATO_IMAGEN_ORQUESTACION.schema.json` (1,361 líneas, leídas completas)

| Líneas | Qué dice | Consecuencia |
|---|---|---|
| L7–41 | `ruta`: flujo FL01–FL04 obligatorio; sección, etapa, paso, operativa solo si la fuente lo define, «no se inventa un valor» | N: la prueba es FL04 (activo directo) |
| L42–55 | `operacion`: 8 valores; no hay análisis de imagen a prompt | C: pregunta 2 de `04_preguntas_eric.md` |
| L56–125 | modelo, pieza, formato (ratio con patrón N:M), idioma | N: tarea 3 |
| L126–255 | sujetos (clase, rasgos, cabello, vestuario, expresión, posición), acción, física, escena | N |
| L256–269 | `estilo` y `representacion` | N: `representacion` lleva F18 «fotorrealista» como valor de faceta, nunca como palabra del prompt |
| L270–426 | identidad, blocking, rostro (ocupación 0..1), cámara, luz, color y material, composición | N: módulo fotografía (contratos L775–790) |
| L427–470 | `referencias[]`: archivo, sha256 de 64 hex, medio, rol, índice obligatorios; preservar | N: tarea 3 (se aprueba de nuevo cuando existe la imagen de entrada) |
| L471–616 | restricciones, contexto narrativo y de secuencia, función del plano, publicación, ancla con contexto de clip | N |
| L618–664 | edición (máscara solo si la interfaz la admite), transferencia, boceto | N |
| L665–692 | `texto_marca`: literales, posición, tipografía, logos aprobados | C: campos de los casos con texto (ya anotado en T-BRIEF L125–128) |
| L693–740 | override de Ideogram, grounding, presupuesto, selecciones taxonómicas | N |
| L741–753 | `modulos_activos`: fotografía, acción física, sujetos visibles, materialidad | N: tarea 3 |
| L757–990 | `salida`: prompt, slots, parámetros, referencias, validaciones, traza (ruta, materias, procedencia, decisiones, aplicaciones, efectos, compactación, consultas), notas, handoff, aceptación (critique, detalles auditados, rondas, sha256 del activo) | C: la QA de la tarea 11 se escribe en `salida.aceptacion` de cada caso, con la crítica de `visual-asset-critic` en `critique` |
| L991–1033 | orquestación y contratos externos | N |
| L1040–1332 | `procedencia_campos`: path, origen (usuario, herencia_aprobada, inferencia_para_aprobacion, fuente_documental), fuente, valor_sha256, aprobacion_id | C: en el caso de descripción de imagen, lo que el sistema saca de la foto entra como `inferencia_para_aprobacion` con la foto y su sha256 como fuente; el schema no necesita cambios para eso (ajustado en la pregunta 2) |
| L1333–1352 | `aprobacion_brief`: brief_sha256, mensaje_id, aprobado = true | N: tarea 3 |
| L1354–1360 | `additionalProperties: false`; obligatorios contrato_id, version, entrada, procedencia_campos | N: no se agregan campos fuera del schema |

## 4. Registro de destinos — `…/templates/REGISTRO_DESTINOS_TEMPLATE.json` (2,759 líneas; leído completo como datos: 36 destinos de faceta, 3 alias, 156 campos, 24 destinos de F30, 8 destinos de alcance)

| Parte | Qué dice | Consecuencia |
|---|---|---|
| `facet_destinations` | F01–F31, P-01, P-02, P-04, P-05 y E, cada una con su ruta del schema (F04 → `pieza.tipo`, F10 → `operacion`, F11 → `ancla.rol`, F15 → `sujetos.items[].clase`, F18 → `representacion`, F23 → `referencias[]`…) | C: F32 a F35 son extensiones aprobadas el 2026-10-23 y no tienen destino propio; su valor de cada caso va en `selecciones_taxonomicas`, y el texto literal de F32 en `texto_marca` (destino de F30 «texto en pantalla»). La tarea 3 lo hace así |
| `aliases` | `sujetos[].clase`, `estilo_representacion`, `contexto_narrativo.montaje` | N |
| `f30_destinations` | cada materia de F30 con sus rutas; «crítica y revisión» → `salida.aceptacion` y `salida.validaciones`; «texto en pantalla» → `texto_marca` y el override; «trazabilidad» → `salida.traza` y notas | N: coincide con lo anotado en el schema |
| `scope_destinations` | creación de imagen → `entrada` y `salida.prompt`; crítica → `salida.aceptacion`; video, audio y post → `contratos_externos` | N |
| `fields` (155 de 156) | origen permitido: usuario, herencia aprobada, inferencia para aprobación o fuente documental; «todo valor inferido o heredado alterado requiere aprobación de su contenido; cada cambio invalida la aprobación dependiente»; cuándo se exige cada campo, igual que T-BRIEF L22–134 | N: tarea 3 |
| `fields`: `entrada.modulos_activos` | origen sin inferencia; «activación debe quedar en brief aprobado»; depende de operación, modelo y representación | N: la representación «fotorrealista» y una operación que no sea edición activan el módulo fotografía en el brief que Eric aprueba (contratos L775–790) |

## 5. PLAN V5 — `taller/catalogo/fuentes_20261019/PLAN_V5_COMPLETO_TAXONOMIA_TEMPLATES_20261019_054300.md` (1,450 líneas, leídas completas)

Qué es: el plan de catalogación del 2026-10-19 (orquestación e imagen). La prueba actual ejecuta la parte de ese plan que
mide si el sistema produce la imagen; PLAN_FINAL_PRUEBA hereda sus principios, no su calendario.

| Líneas | Qué dice | Consecuencia |
|---|---|---|
| L1–21 | propuesta consolidada; las cifras viejas son antecedentes; índice I–V y anexos A–H | N |
| L25–34 | objetivo rector: extraer todas las reglas aplicables a un tipo y caso y convertirlas en prompts de apariencia fotográfica y alta calidad al primer intento; la meta fotográfica no autoriza palabras prohibidas | N: coincide con el objetivo y con 26 §12; «photorealistic» sigue prohibida |
| L35–46 | ocho capacidades del entregable; no genera imágenes ni despliega servicios | N: la prueba actual sí genera (26 §8); es una etapa posterior a V5 |
| L48–65 | cierre exige todos los efectos comprobados; la verificación no demuestra ausencia absoluta de errores | N |
| L67–81 | acuerdos: reiniciar juicios, FF/LF dentro de imagen, sin límite arbitrario de 15–20 reglas («la cantidad depende del caso y el límite documentado del modelo») | N: la prueba no recorta reglas por número; ya lo cumple la tarea 4 |
| L83–119 | diez correcciones (silencio no aprueba; información ausente separada en vacío taxonómico, dato técnico no documentado y contradicción) y discrepancias | N: la aprobación del brief es explícita (`aprobacion_brief.aprobado = true`) |
| L121–136 | principios: evidencia de originales; cita que existe no prueba sentido; ninguna regla queda inaccesible por «pendiente» o «no aplica»; dato ausente activa completar el brief; Aurora excluido | N: ya en §2 del plan (reglas comunes) |
| L138–160 | definiciones (pasaje, aplicación, obligación, condición, materia, UNIVERSAL, exclusión expresa) | N |
| L164–198 | roles: un propietario por bloque, texto por texto; lector B independiente; adversario; tercera lectura del 10 %; comprobaciones deterministas | N: roles del catálogo; la prueba no usa agentes (instrucción de Eric) |
| L200–228 | artefactos A01–A21; si una entrada cambia se invalidan las salidas dependientes | N: la prueba lo aplica con la aprobación ligada al sha256 del brief |
| L230–256 | catálogo en tres capas (evidencia, interpretación, cumplimiento); registro mínimo por pasaje | N |
| L258–270 | prohibidas NO DETERMINADO, NO APLICA, pendiente; cada faceta VALOR o UNIVERSAL; dato ausente completa el brief; un caso que muestra incompatibilidad no borra otras rutas de la regla; FF/LF conservan F26–F28 sin meter audio o movimiento al prompt fijo | N: el «no aplica» de la prueba es la decisión de la tarea 4 por caso, con motivo, no una etiqueta del catálogo (26 §9 lo audita) |
| L272–283 | seis mecanismos: plantilla fija, módulo condicional, validador, selección contextual, disparador, consulta; una obligación puede pedir varios y todos se verifican | N: tarea 9 verifica efectos por regla |
| L285–293 | cardinalidad (exactamente una, una o varias, opcional, todas); contradicción solo con incompatibilidad en el mismo caso y campo | N: criterio ya usado para declarar contradicciones |
| L295–335 | taxonomía operativa 00688 con SHA-256 `7ec912aa…`; tabla F01–F31 → destino (F10 → `entrada.operacion` «génesis, ancla, composición, edición, transferencia o boceto»; F15 → `sujetos[].clase` con planta) | C: F10 en V5 no tiene descripción de imagen; con 26 §14 se ejecuta como `operacion = genesis` y no necesita destino nuevo |
| L337–350 | extensiones: P-01 flujos FL01–FL04; F04 con scroll; F15 con planta; F29 con 11 modelos; F30 ampliada; P-05 ámbitos; «P-02: autoridad sigue siendo metadato; no se restituye F32» | C: la «F32» que V5 no restituye es la faceta vieja de autoridad; la F32 de esta prueba (texto en la imagen) es la extensión aprobada el 2026-10-23. Son cosas distintas con el mismo número; el plan reescrito dice «F32 texto en la imagen (extensión 2026-10-23)» para no confundirlas |
| L352–368 | cada faceta, valor y término con destino materializado; cero clases sin destino; no inventar reglas para llenar categorías vacías | N |
| L370–376 | certificado de evaluación exhaustiva por texto: comparar IDs evaluados con el conjunto completo; coincidencia léxica no basta | N: es el mismo control que `verificar_lectura.py` aplica a la lectura del universo |
| L379–408 | destino de cada materia F30; «texto en pantalla → literal, tipografía, posición y modo integrado o entrega separada según fuente»; «crítica y revisión → salida.validaciones y contrato de aceptación» | C: el caso con texto declara si el texto va integrado (texto del mundo fotografiado, en el prompt) o se entrega aparte (sobrepuesto, en post), como en `01_texto_en_imagen.md`; la crítica va a `salida.aceptacion` (tarea 11) |
| L410–418 | destinos de P-05; creación de imagen → T-GENESIS, T-REF-COMP, T-ANCLA-REF, FF, LF, T-EDIT, T-STYLE, T-SKETCH | N: la descripción de imagen usa T-GENESIS (26 §14) |
| L419–421 | identificar el contrato de un ámbito externo no lo declara construido | N |
| L423–442 | secuencia por bloque y por texto, cuatro rondas lógicas, terminar un texto antes del siguiente; la congelación no vuelve correcto un error | N: la lectura del universo (`05`) siguió texto por texto |
| L444–453 | fase 0: fuentes autorizadas; «documentos citados pero no proporcionados no se convierten en autoridad disponible» | N: todo lo que cita la prueba está en el ZIP original o en las decisiones de Eric (verificado en `03`) |
| L455–475 | inventario con cobertura bidireccional; repetir hashes prueba reproducibilidad, no cobertura semántica; citas de HTML contra la misma representación | N |
| L477–493 | contrato de interpretación con matriz fuente → obligación → cláusula → prueba; verificar las referencias a C18 en el archivo real | N |
| L495–508 | validadores probados con casos válidos e inválidos | N: tarea 9 corre los validadores sobre cada caso |
| L510–534 | pares mínimos, canarios, escenarios del piloto (casos completos, límites, excepciones, ausencia de datos), reserva del 30 % | N: método del catálogo; esta prueba mide casos reales, sin reserva |
| L536–556 | hoja de trabajo del propietario; «una palabra en una lista de ejemplos no se vuelve requisito general»; el nombre del archivo no restringe por sí solo | N: criterio de la tarea 4 (seleccionar por condición, no por palabra) |
| L558–574 | piloto funcional: génesis, imagen con referencias y ancla FF/LF; ampliar solo con defectos corregidos y reejecutados | N |
| L576–591 | ronda 1: ámbito orquestación / imagen / otros; textos fuera de las dos fases conservan disposición | N |
| L593–608 | ronda 2: naturaleza (prescripción, descripción, ejemplo), fuerza, función, tratamiento | N |
| L610–646 | ronda 3: jerarquía ámbito → etapa → medio y operación → modelo → función de imagen → caso de uso → sujeto y demás; «una regla universal de un modelo no se extiende a los demás» | N: coincide con 23 §6 (solo reglas que alcanzan a GPT Image 2) |
| L648–654 | perturbaciones válidas; quitar contexto solo diagnostica dónde vive la restricción | N |
| L656–678 | adjudicación; tres incidencias: interpretación resoluble (se aplica sin consultar), dato técnico ausente (se investiga, no lo decide el usuario), política no definida (se consulta una vez) | N: criterio con el que `04` separa lo que es de Eric de lo que se resuelve con fuentes |
| L680–695 | ronda 4: todos los efectos por obligación con mecanismo y destino; no declarar incorporada una obligación sin comprobarla | N |
| L697–707 | brief dinámico: discriminantes primero; imagen directa con datos del usuario o inferencias para aprobación; un cambio de discriminante invalida campos y aprobación; un dato ausente se completa, no se universaliza | N: tarea 3; la descripción de imagen usa justo «inferencias para aprobación» (26 §14) |
| L709–715 | plantillas por modelo, operación y tipo de imagen con la sintaxis del documento del modelo; no forzar la sintaxis de un modelo a otro | N |
| L717–725 | compilar obligaciones estables solo tras prueba de presencia y de violación | N |
| L727–736 | antes de compactar: mismo caso, contradicciones resueltas, cardinalidad; después, conservar sujetos, valores, condiciones y sintaxis; la longitud se mide en la unidad del modelo y sin máximo respaldado no se inventa límite | N: coincide con 26 §11 (longitud aspiracional, no bloquea) |
| L738–746 | orquestación con prueba de activación y no activación; controles de video mapeados a imagen sin exigir audio a una imagen; Aurora excluido | N |
| L748–767 | contratos: T-BRIEF-IMG, T-BRIEF-ORQ, T-GENESIS, T-REF-COMP, T-ANCLA-REF (character, environment, hero/macro, motif insert), T-ANCLA-FF, T-ANCLA-LF, T-EDIT, T-STYLE (separa contenido preservado de propiedades transferidas), T-SKETCH, T-ORQ, T-TRAZA | N: la prueba tiene un caso por contrato de creación; descripción de imagen va por T-GENESIS (26 §14) |
| L769–784 | contrato común por campo; la inferencia entra solo aprobada; sin aprobación por silencio | N |
| L786–816 | campos de T-BRIEF-IMG; `texto_integrado_override` solo para Ideogram Mode 2; `texto_marca` = literales, ubicación e invariantes, «ningún logo real se inventa por default», destino «texto citado, preservación o entrega separada según regla» | C: los casos de texto en GPT Image 2 usan `texto_marca`, no el override de Ideogram; el texto del mundo va citado en el prompt y el sobrepuesto se entrega aparte (`01`) |
| L818–829 | salida: prompt solo con texto para el generador; parámetros aparte; la traza no se concatena al prompt | N: tarea 9 |
| L831–850 | GPT Image 2, cinco slots en ese orden y su mapeo: Scene ← F16 (y F05, F30 ambiental); Subject ← F15, F19, F13, F20, F21; Important Details ← F17, F18, F24, F25 y materias F30; Use Case ← F04 y función del activo (F11, F12); Constraints ← prohibiciones y preservaciones de las reglas seleccionadas, no una lista genérica de negativos | C: la tarea 8 del plan reescrito redacta cada slot con este mapeo, citando V5 L845–850 |
| L852–860 | edición: Change / Preserve / Constraints; F10 decide el contrato antes de redactar | N: adaptador GPT2-EDIT ya en el plan |
| L862 | rol explícito por índice con varias referencias; `input_fidelity` no se añade a GPT Image 2; quality y size son parámetros por caso; «una recomendación de borrador no sustituye la de identidad o texto denso cuando esta rige el caso» | C: los casos de identidad y de texto extenso o pequeño se entregan con Quality high (23 §7; corrección B8 de `03`) |
| L864 | el adaptador de forge (tres párrafos) no se mezcla con los cinco slots | N: §6.2 filas 2 y 4 ya en el plan |
| L866–877 | Nano Banana: lenguaje natural, sin números ópticos | N: fuera por 23 §6 |
| L878–892 | Nano Banana: composición `Image 1… Combine… Match`, variantes NB2 Lite, NB2 y NBP con capacidades propias, JSON solo para escenas complejas, FF/LF con estado visible | N: fuera por 23 §6 |
| L894–905 | otros modelos (Flux, Midjourney, Ideogram, Seedream, gpt-image-1.5/1/mini) con contratos separados; no copiar tamaños ni sintaxis de GPT Image 2 a versiones viejas | N: fuera por 23 §6 |
| L907 | Flux y Seedream escriben `photorealistic` en su fórmula; prevalece la prohibición del usuario y el efecto se compila con lenguaje permitido | N: prohibición ya en el plan |
| L909 | `_capabilities.json`: techo editorial de 300 palabras para GPT Image familia 1.5/2; dato histórico, no límite técnico de API | N: coincide con 26 §11 |
| L911 | ningún modelo se elimina por documentación técnica insuficiente; ejecutar el generador sí exige contrato técnico suficiente para la variante e interfaz | N: la descripción de imagen se ejecuta con el contrato de génesis (26 §14) |
| L913 | roles de T-ANCLA-REF por F11; FF y LF usan estado inicial o final; «la pareja se exige únicamente cuando la operación o el caso requiere ambos fotogramas; un FF independiente no obliga a crear un LF»; con pareja se comprueban ratio y continuidad | C: el caso LF del plan reescrito se arma como pareja de su FF (el LF depende del estado final y del vínculo con FF, contratos L760) y la QA comprueba el mismo ratio y la continuidad; el caso FF no exige LF |
| L915–927 | cadena completa campo de brief → faceta → regla → efecto → destino → resultado esperado y observado; cinco conciliaciones | N: es la traza de la tarea 9 |
| L930–934 | módulo propuesto de casos de uso combinables; no enumerar el producto cartesiano; los casos de demostración no acreditan el catálogo | N: la lista de casos de la prueba sale de los tipos fotográficos (26 §12), no del producto cartesiano de facetas; coincide con la recomendación de `04` pregunta 1 |
| L936–981 | verificación de extremo a extremo: referencia independiente, caso positivo por aplicación, fronteras, comparar aplicaciones, obligaciones y todos los efectos (no solo lo escrito en el prompt); pruebas mínimas (datos ausentes que activan completar el brief, compactación sin pérdida, sintaxis por modelo, validadores) | N: verificación del catálogo; la prueba actual cubre la parte de sintaxis, validadores y compactación en las tareas 8 y 9 |
| L983–1005 | mantenimiento y cierre; NO VERIFICADO y NO CUMPLE describen la auditoría y nunca eliminan reglas | N |
| L1007–1076 | riesgos R01–R08 con control, evidencia, bloqueo, límite y responsable | N: controles del catálogo (R03 cita que no respalda, R04 restricción omitida, R08 ausencia confundida con decisión) ya practicados en `03` y `05` |
| L1077–1173 | riesgos R09–R20 (R11 pruebas circulares: referencias desde la fuente congeladas antes; R13 brief incompleto; R14 compactación destructiva; R17 declarar resuelto con cobertura parcial; R18 decisiones inventadas; R20 sesgo compartido) | N: R11 y R13 ya los cubre el plan (tarea 4 por fuente antes de redactar; tarea 3 con brief aprobado); R17 lo cubre `verificar_lectura.py` en la lectura |
| L1175–1188 | riesgos por fase | N |
| L1192–1215 | ahorros autorizados y no aceptados («reemplazar lectura por búsqueda de palabras», «limitar arbitrariamente reglas por prompt»); un desvío de una autorización económica pausa el gasto | N: coincide con CLAUDE.md (antes de decir que algo no existe) y con la prohibición de usar la API sin autorización |
| L1217–1230 | hitos; control de utilidad en cada hito; «no se exige una evaluación visual real durante la fase documental» | N: la evaluación visual real es justamente esta prueba (26 §8) |
| L1232–1241 | el usuario aprueba el plan, decisiones de política nuevas, inferencias o datos del brief de un caso real, presupuesto y paquete final; no decide hechos técnicos | N: es el reparto que sigue `04` |
| L1243–1258 | diez objetivos de aceptación; el 8 exige sintaxis por modelo y límites documentados, «sin inventar un máximo» | N |
| L1260–1273 | paquete de entrega | N |
| L1275–1281 | licencias originales se conservan; V5 es propuesta, no ejecución | N |
| L1285–1296 | anexo A: 31 facetas, 1,369 IDs TRM, extensiones P-01, P-04, P-05 y valores CAT | N |
| L1298–1312 | anexo B: registro de adjudicación; sin aprobación por ausencia de objeciones | N |
| L1314–1324 | anexo C: par mínimo sintético (retrato con y sin condición de dos personas) | N: criterio de condición para la tarea 4 |
| L1326–1339 | anexo D: formato de pregunta al usuario: pregunta sencilla, qué depende, fuentes revisadas, opciones y consecuencias, recomendación fundada, clase a la que se aplica, registro de la respuesta | N: `04_preguntas_eric.md` sigue ese formato y registra las respuestas con fecha (26 §14 y §15) |
| L1341–1356 | anexo E: traza con caso positivo, no activación y violación | N |
| L1358–1373 | anexo F: avance N = obligaciones cerradas / obligaciones del alcance | N |
| L1375–1390 | anexo G: defectos históricos (registros fuera por motivo caducado, citas Sentinel, elipsis, F26–F28 y FF/LF) | N |
| L1392–1449 | anexo H: arranque, correspondencia con V3, entregables nuevos, comprobaciones de la propuesta | N |

Resultado del documento: cinco consecuencias para el plan reescrito (L337–350 nombre de F32; L379–408 y L786–816 texto
integrado o entregado aparte; L831–850 mapeo de los cinco slots; L862 Quality high en identidad y texto denso; L913 LF
como pareja de su FF). Ninguna contradice las decisiones 23, 24 y 26.

## 6. Taxonomía 00688 — `taller/catalogo/fuentes_20261019/00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md` (4,365 líneas, 1.2 MB, leídas completas de nuevo con el alcance 26 §12, §14 y §15)

Base: `v3/LECTURA_4_DOCUMENTOS.md` (tramos T01–T29, escritos para el alcance anterior). Este registro vuelve a leer cada
tramo y anota lo que cambia con el alcance fotográfico.

| Líneas | Qué dice | Consecuencia |
|---|---|---|
| L1–20 | consolidado de C18 y decisiones; F15 añade planta (CAT-F15-PLANTA); F04 añade scroll; F26–F28 nunca NO APLICA en anclas; F29 añade variantes sin acreditar capacidad | N |
| L25–35 | seleccionabilidad: ninguna etiqueta vuelve inelegible una regla; exclusión permanente solo con decisión expresa; «la incompatibilidad concreta con un caso sí excluye esa aplicación para ese caso»; discriminante ausente → completar y aprobar el brief; seleccionar no prueba capacidad | N: es el criterio del «no aplica» por caso de la tarea 4, con motivo y sin borrar la regla |
| L37–75 | corpus autorizado: 206 archivos, 13,005 unidades; fuera del corpus: Aurora, taxonomías derivadas, «produccion-visual-sw30, regímenes del repo, DECISIONES.md, refs.yaml — citados por las fuentes pero no suministrados: no se crean registros ni se les atribuye autoridad» | C: el plan cita «DECISIONES.md decisión 2» como respaldo de la fila de longitud (`PLAN_FINAL_PRUEBA.md:25`). Esa fila se sostiene en la decisión de Eric 26 §11 y en T-BRIEF-IMG L355; `.claude/rules/DECISIONES.md` queda como antecedente, no como fuente. Ninguna regla de `.claude/rules/regimenes/` entra a la prueba: no está en el universo (verificado en `05`) |
| L77–119 | inventario literal por unidades INV; señal léxica normativa no decide; capas de la taxonomía; «Faceta 32 "fuente con autoridad" — retirada el 2026-09-29» | N: confirma que la F32 vieja (autoridad) es otra cosa que la F32 de texto en la imagen (2026-10-23), como se anotó en V5 L350 |
| L121–155 | 1,369 términos; 1,200 COMPLETO, 112 PRESENCIA (solo índice), 57 SIN PRESENCIA fuera de la expansión de consultas; ningún término activa una categoría por sí solo | N |
| L157–182 | principios: caso = tupla de valores de las facetas A–C; VALOR o UNIVERSAL, UNIVERSAL no extiende la regla de un modelo a otros; medio, pieza y etapa por separado; F26–F28 de anclas conservan el contexto del clip sin mandar movimiento ni audio al prompt de imagen; materia ≠ condición («mencionar un elemento para prohibirlo lo hace materia»); dos vías del brief, la de activo directo con inferencias para aprobación; cifras con su alcance | N: la prueba es activo directo (FL04); la descripción de imagen usa esa vía (26 §14) |
| L184–200 | §1.12 contrato de lectura por texto: leer documento, encabezados, sección y cuerpo; examinar cada ítem; prohibidos NO DETERMINADO, NO APLICA, PENDIENTE como clasificación; consulta solo si fuente y decisiones no bastan | N |
| L202–208 | §1.13 cada clasificación con destino en los templates; la ubicación interna no obliga a copiar etiquetas al prompt | N |
| L210–242 | F01 etapas 0–7, post y ORQUESTACIÓN; F02 pasos E0.1–POST.2 | N |
| L244–253 | P-01: FL01 spot, FL02 génesis, FL03 anclas, FL04 activo directo (codificación editorial aprobada, no flujo de las fuentes) | N: la prueba es FL04 |
| L255–258 | FL04 D01 completar brief (ninguna inferencia se atribuye al usuario); D02 confirmar datos (inferencias pendientes bloquean el paso) | N: tarea 3 |
| L259 | D03 elegir contrato: «Un modo sin contrato original suficiente permanece no habilitado» | C, resuelta: con 26 §14 la descripción de imagen corre con el contrato de génesis (operación `genesis`, T-GENESIS, GPT2-GEN), que sí existe; no queda ningún caso sin contrato |
| L260–261 | D04 redactar con sintaxis del modelo y parámetros separados; D05 «para render, crítica/aceptación y trazabilidad según fuente»; el prompt no acredita aceptación de una imagen no generada | N: tareas 8, 9 y 11 |
| L263 | las cuatro operaciones FL04 remiten a FL02 y FL03 sin atribuirles FL04; «una imagen independiente no se denomina ancla si no cumple ese rol» | N: los casos de ancla de la prueba declaran su rol F11 |
| L265–333 | FL01 literal, E0–POST (E4.4 «Nunca texto dentro de la descripción visual» para el texto en pantalla de un spot; E5.2 génesis por clase incluye edificación y animal; E5.7 crítica con `critique.json`; E6.6 cabecera SKILL / RIESGOS / TÉCNICA) | N: E4.4 es el texto sobrepuesto del storyboard, que tampoco entra al prompt en esta prueba (`01`); E5.2 respalda los casos de edificación y animal; la cabecera ya la exige la entrega |
| L335 | E6.5 Aurora conservado como texto, tratado por P-07 | N |
| L337–352 | FL02 nodos: génesis solo texto, «el primer paso es la clase de sujeto, porque decide el modelo y los bloques»; ramas sí/no, NBP o NB2 / GPT Image 2; ACCEPT, REVISE ≥80 %, REJECT o 2ª falla, otro modelo o bloque, 3ª falla | N: el modelo ya está fijo (23 §6); la clase de sujeto sigue decidiendo los bloques |
| L353–358 | INV-000538–000542: catalogar clase (persona, lugar, edificación, animal, producto, objeto); «¿necesita fidelidad a algo real? arquitectura, especie, planta → Nano Banana 2 con Image Grounding» | C: la rama de grounding queda fuera por 23 §6 (26 §15); en la tarea 4 esas reglas se marcan «no aplica» con ese motivo. Los casos de edificación, animal y planta se resuelven con GPT Image 2 |
| L359–367 | elegir modelo (`models.md`); NB prosa sin números de lente; GPT: 5 slots, anti-slop, quality; golden-rules: verbo inicial, positivo, hex, texto entre comillas | N: ya en la técnica de génesis del plan |
| L368–372 | referencias por clase: persona → characters + portrait-cinema; producto → ecommerce, food-beverage; lugar → dimensional, creative-direction; animal → «patterns con grounding» | C: para el caso de animal la referencia de clase que da la fuente es la de grounding (fuera por 23 §6); el caso usa golden-rules, gpt-image.md y las reglas de animal del universo anotadas en `05` (000433–434, 000456, 000477) |
| L373–379 | secciones por clase: persona light_hard, skin_doc, usecase_doc, clean_doc; producto optics, surface, colour, clean; lugar geometría, luz, presión ambiental, sin persona; «~250 palabras»; ensamblar por bloques | N: longitud aspiracional (26 §11) |
| L380–386 | lints mecánicos (audit_gi2, gate_image, gate_dramaturgy; vocabulario prohibido, sin logos); pregunta de avance «¿todas las reglas del caso? SÍ sin matices»; micro-gate SKILL · RIESGOS · TÉCNICA | N: tareas 9 y entrega |
| L387–393 | preflight de costo; generar barato (GPT quality low), seleccionar, regenerar en alta (GPT quality high) | N: en la app no hay créditos que estimar (26 §8); la repetición para diagnosticar es 26 §10 |
| L394–399 | inspección propia «zoom 100%: rostro, manos, anatomía, etiqueta, arquitectura»; visual-asset-critic 6 capas → critique.json; canonizar con hash | C: la QA de la tarea 11 inspecciona al 100 % lo que el caso tenga de esa lista (rostro y manos en persona; etiqueta en producto y texto; arquitectura en edificación; anatomía en animal) antes de la crítica de 6 capas |
| L400–406 | editar, no re-tirar; hasta 3 ediciones apiladas; cambio de método con causa; replantear el shot; referencia para T2, T3, keyframes | N: bucle de corrección del flujo; la prueba diagnostica tras 26 §10 |
| L407 | INV-000591: la clase entra antes que el modelo; grounding NB2 para lo fiel a algo real; «máximo dos intentos por método» | N: 26 §10 ya lo separa de la repetición para diagnosticar |
| L408–418 | entradas (clase, plan de anchors, brand-lock, series_lock, modelo y presupuesto) y salidas (cabecera de 3 líneas + Model / Quality / Size + Prompt + Notes; render ACCEPT con critique.json; asset con SHA-256) | N: la salida de la prueba ya sigue ese formato |
| L419–424 | por clase: persona T1 obligatorio; «edificación y animal: grounding NB2, verificación contra la realidad»; producto «etiquetas en GPT Image 2 high, logo nunca de texto»; lugar sin persona, una presión ambiental; objeto legible en macro y en general | C: (a) el grounding sale (23 §6), pero «verificación contra la realidad» no depende del modelo: si el caso de edificación o animal nombra un sujeto real, la QA lo compara con fotos reales del sujeto; (b) el caso de producto con etiqueta y los casos de texto van con Quality high; un logo real no sale de texto |
| L425–429 | lo que no entra en génesis: referencias (T2 en adelante), logos y etiquetas de marca reales (flujo con referencia), texto en pantalla (capa separada), movimiento (un still es un instante) | C: los casos de texto en el mundo usan un texto que no es marca real; si fuera marca real, entra por composición con el asset aprobado |
| L430 | INV-000614: dimensión caso con LUGAR, EDIF, ANIMAL, OBJ, T1–T5, PROD; «un brief de génesis de landmark filtra por E5.2 + EDIF y trae consigo las reglas de grounding» | C: el filtro del caso de edificación trae esas reglas; la tarea 4 las registra como no aplicables por 23 §6, con motivo, y aplica las demás |
| L432–460 | FL03 pasos 1–8 y A0–A12 | N |
| L461–466 | ensamble EN.1–EN.6: génesis por miembro, placa vacía con anclas, inserción secuencial «use only the person from image N…», EN.4 una sola pasada con todos los maestros (GPT hasta 16 referencias) «a verificar miembro por miembro; la regla de una sola pasada es inferencia hasta probarla», sin clones, crítico por miembro | C: el valor «retrato de grupo» (TRM-1260) que la recomendación de `04` cubre al menos una vez sigue EN.1–EN.6; si se prueba en una pasada (EN.4), la QA verifica cada miembro contra su maestro |
| L467 | EN.7 video por miembro | N: video fuera |
| L469–479 | F03 ruta operativa: Video publicitario / Clip | N |
| L481–503 | F04 rama imagen: editorial, key visual, e-commerce o catálogo, retrato (una o varias personas), póster o key art, post o historia, miniatura, UI o mockup, slide, storyboard o multipanel, diseño de personaje, visualización arquitectónica, identidad de marca, scroll | C: base de la recomendación de la pregunta 1 de `04` (qué valores son fotográficos y cuáles quedan para la prueba posterior) |
| L505–521 | F04 rama video | N: video fuera |
| L523–591 | términos de F04: TRM-0004 editorial (moda, deporte, música); TRM-0008 retrato individual y de grupo; TRM-0009 póster = imagen + tipografía; TRM-0013 miniatura con titular; TRM-0014/0015 UI y mockup de producto sobre fondo limpio o marco de dispositivo; TRM-0019 multipanel; TRM-0020 y 1116–1120 diseño de personaje; TRM-0021 visualización arquitectónica (`dimensional.md:51`); TRM-0022 y 0040–0048 identidad de marca y sus aplicaciones; TRM-1258/1259 infografía y diagrama; TRM-1260 retrato grupal | C: mismo uso; el mockup de producto sobre fondo limpio (TRM-0015, `gpt-image.md:137`) es foto de producto y entra cubierto por el caso de producto |
| L595–632 | F05 temática: 13 valores (deporte y fitness, automotriz, música, moda, comida y bebida, arquitectura e inmobiliaria, belleza, hospitalidad, retail, tecnología, salud — SIN PRESENCIA, educación, corporativo) | N: atributo; la extensión «estilo de vida» es 26 §7. Que deporte y automotriz citen regímenes y race-and-speed como origen del valor no hace fuente a esos archivos (L74) |
| L634–672 | F06 formato tipado ancho:alto; «registrar un valor no afirma que un modelo lo admita: la capacidad por modelo se conserva en la regla que la declara»; 1:4, 1:8, 4:1, 8:1 solo NB2 | N: el formato de cada caso se toma de lo que `gpt-image.md` declara para GPT Image 2 (tamaños de `gpt-image.md:59`, INV-002359), no de esta lista |
| L674–691 | F07 géneros narrativos (rama video y guion) | N: video |
| L693–746 | F08 estructuras de beats | N: video |
| L748–774 | F09 patrones de montaje (inicio) | N: video |
| L775–812 | F09 términos de montaje; P-04 lugar de publicación PLT-01–08 («los ejemplos no establecen regla universal»; Reels sin plataforma inferida; website hero) | N: atributo; un caso con destino de publicación toma el requisito que la fuente liga a ese destino |
| L816–841 | F10 rama imagen: génesis (T1), ancla con referencias (T2–T4), composición, edición (T5), transferencia de estilo, boceto o wireframe a final (structural y dimensional); rama video | N: F10 con un caso por valor (`04` pregunta 1) |
| L845–851 | TRM-0497–0503: texto a imagen, condicionada por referencia, composición, transferencia, conversión de técnica (animación → foto, `creative-direction.md:104`), boceto a final, plano 2D a 3D (`dimensional.md:5`) | C: el caso de boceto o plano a final cubre `structural.md` y `dimensional.md` (corrección B5 de `03`); la conversión de técnica hacia foto es un caso de transferencia de estilo cuyo resultado es fotográfico |
| L852–871 | términos de edición: añadir, quitar, sustituir objeto (`gpt-image.md:100`), inpainting, outpainting (SIN PRESENCIA), recorte (PRESENCIA), cambio de fondo (`characters.md:80`), reluminación, cambio de estación, cambio meteorológico, colorización, restauración, retoque, cambio de material (`editing.md:98`), localización lingüística, adaptación cultural (`editing.md:82`), upscaling (SIN PRESENCIA), refinamiento iterativo, preserve list, máscara | C: cuatro plantillas fotográficas de edición no caben en los 8 hijos de 23 §4 (fondo, material, adaptación cultural y relleno con física de L927); añadidas a la recomendación de la pregunta 1 de `04` como casos propios. Cambio de estación va con «cambiar luz o clima» |
| L872–915 | entradas de texto, imagen, multiimagen, video y audio; edición con máscara y conversacional; términos de video (multi-shot, extensión, edición de video, motion control, elements) | N: máscara fuera (la app no la expone, 26 §8); video fuera |
| L916–922 | TRM-1125–1131: 2D a 3D, 3D a 2D técnico, boceto a 3D, diseño plano a mockup de producto (`dimensional.md:73`), alzado a exterior, planta a interior, meme | C: el caso de boceto o plano a final toma una de las variantes fotográficas de `dimensional.md` (alzado a exterior o planta a interior, que dan una foto de arquitectura); 3D a 2D técnico y meme no dan foto |
| L923–927 | colorización de foto (con época y piel natural) y de manga; virtual try-on; interior swap; relleno físicamente coherente (`editing.md:92`) | C: colorizar usa una foto en blanco y negro de entrada (`05`, 002199–2229); manga queda fuera (no es foto) |
| L928–930 | video a imagen (SIN PRESENCIA); web grounding y Image Grounding de NB2 | N: grounding fuera por 23 §6 |
