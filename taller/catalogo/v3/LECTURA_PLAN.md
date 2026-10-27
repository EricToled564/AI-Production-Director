# Lectura para el plan de la prueba — 2026-10-27

Registro de lo leído para escribir `PLAN_FINAL_PRUEBA.md`. Cada entrada dice cómo se leyó: completo línea a línea,
campo por campo con volcado completo, o regenerado byte a byte desde fuentes ya leídas. Las cuatro fuentes mayores
(taxonomía, T-BRIEF-IMG, contratos, schema) tienen su registro por tramo en `LECTURA_4_DOCUMENTOS.md`.

## A. Decisiones (completas)

- `v2/decisiones/01021…` (25 l), `01022 DELTA…` (226 l), `01062 registro DOC01` (86 l): DEC-000001…025. Para la prueba:
  DEC-000002 (§6.2 solo si no hay archivo smixs), DEC-000004 (caso sin regla → investigación con permiso), DEC-000009
  (menú: génesis, ancla sin referencia, ancla con referencia, edición), DEC-000024 (L81–82: «las licencias las aplicas
  al sistema una vez y ya… ninguna atribución a un tercero en ningún material que va al cliente»), DEC-000025 (sintaxis
  del modelo, aplicada una vez).
- `DECISIONES_ERIC_20261023.md` (41 l): §2 catalogaciones anteriores no se reutilizan; §3 sin pendientes ni NO APLICA;
  §4 extensiones F32–F35, F04, F05, F06 3:2, F10, F17; §5 etiquetas 100 % de la taxonomía; §6 solo GPT Image 2; §7
  quality; §8 biblioteca después del catálogo.
- `DECISIONES_ERIC_20261024.md` (25 l): §1 alcance ratificado el 2026-10-27; §2; §3 reglas de lente y cámara para la
  cara, buscadas leyendo; §4 método universo → filtro por caso → controles → clasificación de lo pertinente → prueba de
  selección.
- `DECISIONES_ERIC_20261026.md` (49 l): §1 cifra de GPT Image 2; §2 verificar siempre; §3 leer exhaustivamente ante
  contradicción; §5 F20 «todas»; §6 F24 + objeto entero; §8 interfaz App de ChatGPT para escritorio, formato en el
  texto, tamaño y quality como referencia, sin máscara; §9 muestra del 10 % de «no aplica»; §10 dos generaciones más
  antes de auditar.
- `.claude/rules/DECISIONES.md` (24 l) y `METODO.md` (128 l); `CLAUDE.md` (25 l).
- `PILOTO_V5_INSTRUCCIONES_20261019.md` (177 l): vigentes §0.4 (taxonomía, Aurora excluida, sin estados de
  diferimiento, sin «photorealistic», el silencio no aprueba); §3 entradas autorizadas por hash y parada si no
  coinciden; §6.1 referencias construidas sin ver la clasificación y congeladas con hash antes de clasificar.
- `taller/recursos/user_directives.json` y `directivas_taller.json`: prohibidos «photorealistic» y «fotorealista»;
  prompt de GPT Image 2 siempre en inglés, brief en español; «una o dos reglas por bloque» no es tope.

## B. Plan, taxonomía, templates y contratos (completos)

- `PLAN_V5_COMPLETO_TAXONOMIA_TEMPLATES_20261019_054300.md` (1,450 l): §7.4, §7.6, §7.10, §13.2, §16.7–16.14, §17, §24.
- Taxonomía 00688, T-BRIEF-IMG, `CONTRATOS_OPERACION_MODELO.json`, `CONTRATO_IMAGEN_ORQUESTACION.schema.json`: ver
  `LECTURA_4_DOCUMENTOS.md`. Taxonomía §7.2 (L2800): condición = grupo TODAS / ALGUNA / NINGUNA de átomos (faceta o
  campo, operador, valor); excepción = subgrupo NINGUNA; alternativa = dos aplicaciones del mismo id.
- `REGISTRO_DESTINOS_TEMPLATE.json` (2,759 l; L1–700 línea a línea, el resto campo por campo con volcado de los 156
  campos): 155 campos con origen {usuario, herencia_aprobada, inferencia_para_aprobacion, fuente_documental} y
  «cada cambio invalida la aprobación dependiente»; `entrada.modulos_activos` sin inferencia y «activación debe quedar
  en brief aprobado».
- `FUENTES_CONTRATOS.json`, `MANIFIESTO.json`, `RESULTADOS_PRUEBAS_ESTRUCTURALES.json` (14/14; «no acreditan selección
  de reglas ni calidad de imagen»; edición válida sin redefinir luz y cámara), `VERIFICACION_ESTRUCTURAL.json`,
  `verificar_templates.py` (L62–65: slots GPT exactos y el prompt empieza por el primer slot), `probar_contratos.py`.
- `fuentes_20261019/PROCEDENCIA.md`; paquete `CASOS_OPCIONES_TAXONOMIA_20261019`: README (construcción del caso en
  10 pasos), `case.schema.json`, `validar.py` (modo caso: opción existente, seleccionable y en su destino; confirmado;
  requisitos resueltos; aprobación), `build_catalog.py` + `bind_templates.py` regenerados hoy: 8 archivos y la sqlite
  idénticos; `rutas_documentadas.json` 184 filas idénticas celda por celda a la taxonomía;
  `relaciones_documentadas.json` 473; `jerarquia_valores.json` 1,729 coherente con el catálogo.
- `v2/esquema_taxonomia.json`: regenerado hoy con `construir_esquema.py`, idéntico; incluye `grupo_condicion` y
  `operador_atomo` (§7.2) y las extensiones aprobadas.
- `taller/recursos`: `template_brief.json` (109 campos = primeros 109 del registro, redacción anterior),
  `operation_packs.json` y `universal_rules.json` (candidatos de la app anterior, no aceptados), `canonical_sources.json`
  (36 unidades, iguales al corpus), `catalogo_especificas.json` (catálogo provisional; no se reutiliza, decisión 23 §2),
  `instrucciones_llenado.json` (slot ← campos del brief = PLAN_V5 §16.11).

## C. Universo y herramientas de clasificación (completos y regenerados)

- `v3/universo`: los 8 scripts leídos; los 12 archivos de salida regenerados hoy idénticos; `verificar_origen.py`
  contra los originales (SHA256SUMS OK): A, B, C 13,005/13,005, E 6/6, 62 fallos D conocidos; salida idéntica.
  `UNIVERSO.md`, `ESTADO_UNIVERSO.md`, `DECISION_SECCIONES.md`, `CONTRADICCIONES.md`,
  `CLASIFICACION_MISMA_POSICION.md`. Universo: 2,722 textos de 41 archivos.
- Los 2,722 textos del universo, leídos completos uno por uno (`universo_prueba_textos.jsonl` volcado por archivo y
  línea con su encabezado, 2,803 líneas). Solo el universo: las secciones y documentos excluidos por decisión no se
  leyeron, porque no son parte de la prueba.
- `v3/universo/adenda`: 125 textos, 40 entran (`construir_adenda.py`, sale con código 0). Los 40 que entran, leídos
  completos. Cambios que dejaron en el plan: References fuera del cuerpo (ADD-0004); objetivo de unas 250 palabras y aviso
  por slot (ADD-0008); ratio en Scene con 26 §8 por encima de ADD-0011, y ADD-0042 condicionado a que la plataforma
  exponga el parámetro; QA de ratio con tolerancia del 1 % (ADD-0043); QA antes de aceptar, con los controles mecánicos
  separados de los visuales (ADD-0047); zoom al 100 % de rostros y manos (ADD-0031); bucles de corrección R12 y R13
  distintos de la repetición de 26 §10 (ADD-0029, ADD-0030). `audit_gi2.py` (ADD-0014) no está en el repo; el plan no
  depende de él, porque cada regla seleccionada se controla por su traza.
- `v2/piloto_gpt-image/clasificacion.py` y `construir.py` (formato de aplicación y verificador de forma), `GUIA_CLASIFICACION.md`,
  `validar_v2.py`, `match_taxonomia.py`, `matriz.py`, `matriz_eric.py`, `construir_esquema.py`, `taxonomia_extracto.md`,
  `PENDIENTES.md`. La condición del formato del piloto (`r`: por faceta, al menos un valor común) no expresa NINGUNA ni
  átomos con operador sobre campos: hay que llevarla a §7.2.
- `.claude/hooks/rule_answer_check.py` (cobertura; ids de 12 hex y APLICA/NO APLICA: hay que adaptarlo).
- `produccion/template-retrato-gpt2/armar.py` (104 l) y `LEEME.md`: obligatorio para retrato de una persona sin
  referencias (CLAUDE.md). Releído completo el 2026-10-27 contra la adenda: los bloques T1 de ADD-0006 caben en sus
  campos (luz, microdetalle, uso, restriccion_extra); rechaza más de 300 palabras (L84–85), contra la decisión 2 y
  T-BRIEF-IMG L355: duda 2 del plan.
- `v3/rag/*.py`: índice BM25 de búsqueda; no acredita cobertura (taxonomía §7.4).
- `v3/fuentes/PROCEDENCIA.md` y `documentos/PROCEDENCIA.md`: taxonomías del 2026-09-13 y 2026-09-28 son anteriores a
  la entrada autorizada (PILOTO §3); no gobiernan.

## D. Hooks activos en este repo (completos)

- `.claude/settings.json`: Stop → `gate_microgate.py`, `gate_dramaturgy.py`, `gate_image.py`; PostToolUse → `gate_shots.py`
  (solo `shots.json` y `text-overlays.json`); UserPromptSubmit → `inject_rules.py`.
- `prompt_detect.py`: un bloque cercado con «Scene:», «Constraints:», un verbo de generación o un modelo nombrado es
  entrega de prompt.
- `gate_microgate.py`: la respuesta que entrega un prompt abre con SKILL / RIESGOS / TÉCNICA; SKILL nombra un .md
  existente en los skills instalados.
- `gate_dramaturgy.py`: vocabulario prohibido de `video/references/dramaturgy.md` y anti-slop de `gpt-image.md`.
- `gate_image.py`: la primera línea del bloque empieza con verbo (golden-rules §1), sin keyword soup, modelo nombrado;
  admite `OVERRIDE: R1 - <razón>`. Probado hoy en local: un prompt GPT2-GEN en bloque cercado, que por contrato abre con
  «Scene:», se bloquea por R1; con la línea OVERRIDE y la cabecera, los tres gates salen con código 0.
- `rule_query.py`, `rules_v3.py`: base de reglas de skills con ids sha1 y casos T1…T5. `cmd_build` (L685–774) toma
  las reglas de `rule_registry.build_v3` sobre los skills y los regímenes; ninguno de los dos archivos lee el universo
  ni ids INV. No se usan.
- `list_events` (servidor claude-code-remote) con `kinds: ["user"]` sobre esta sesión devuelve el uuid de cada mensaje
  de Eric. Probado hoy: es el `mensaje_id` de la aprobación.

## E. No necesarios para el plan, con motivo

- Clasificar cada texto del universo contra cada caso aprobado es la tarea 4 del plan. Para escribir el plan, los
  textos ya se leyeron completos (sección C).
- App `taller/`, `apd/`, `app/`, `api/`, `public/`: la prueba no usa ninguna app.
- Lotes y salidas de catalogaciones anteriores (`taller/catalogo/lotes`, `salidas`, `amp`, `f32`, `v2/lotes`,
  `v2/salidas`, `catalogo_imagen_gpt2.json`): no se reutilizan (decisión 23 §2; `v2/PENDIENTES.md` §4).
- Pruebas preliminares: sin impacto en la prueba nueva (instrucción de Eric del 2026-10-27).
- `produccion/vivaldi-invierno`, `.claude/rules/regimenes` y `research` (fuera del universo), Aurora (excluida).
