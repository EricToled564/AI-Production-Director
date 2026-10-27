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
