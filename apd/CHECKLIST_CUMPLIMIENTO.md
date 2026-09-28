# CHECKLIST_CUMPLIMIENTO — Director de Prompts

Estado a 2026-09-28. Repo base `e61005d` (sin modificar). Registro vigente `R1398-0f9efca5f967`.
`CUMPLE` exige evidencia **ejecutada** (test, corrida de la app o del navegador); una captura sola no cuenta.

**Ejecuciones que respaldan esta tabla**

| Evidencia | Qué es | Resultado |
|---|---|---|
| [`evidencia/pruebas_app.txt`](evidencia/pruebas_app.txt) | `python3 -m unittest -v` sobre `apd/tests` (7 módulos) | ver cabecera del archivo: total y OK |
| [`evidencia/ui/ui_aceptacion.json`](evidencia/ui/ui_aceptacion.json) | `node apd/tools/ui_aceptacion.cjs`: Chromium hace clic en la app real, servidor real, sin modelo | 29/29 |
| [`evidencia/ORIGINAL_TESTS_REPORT.md`](evidencia/ORIGINAL_TESTS_REPORT.md) + [`logs_originales/`](evidencia/logs_originales/) | tests y hooks originales del repo y del paquete | 16/21 scripts PASS; 5 `check.sh` fallan (documentado) |
| [`evidencia/revision_semantica/`](evidencia/revision_semantica/) | 3 rondas de revisión semántica independiente del proyecto demo (5 prompts × 195–200 reglas) | ronda 1 → 2 → 3, ver §Revisión semántica |
| [`demo/`](demo/) | proyecto demostración (quinteto) con 13 versiones, exportación y prompts | ver `demo/LEEME.md` |

## Totales por estado

| Estado | Filas |
|---|---:|
| CUMPLE | 71 |
| BLOQUEADO POR DEPENDENCIA | 2 |
| NO CUMPLE | 0 |
| NO VERIFICADO | 0 |
| **Total** | **73** |

(Conteo generado leyendo la columna Estado de cada fila de esta tabla, no a mano.)

Las dos filas bloqueadas dependen de una clave de API que no existe en este entorno (F.8b, A5.3b). No se declara
el trabajo «completo sin reservas»: ver §Limitaciones comprobadas y §Decisiones que son del director.

## Checklist

Columnas: ID | Requisito | Fuente | Ubicación en la app | Prueba | Resultado esperado | Resultado obtenido | Evidencia | Estado | Límite o motivo

### A1 — Inventario y preservación

| ID | Requisito | Fuente | Ubicación | Prueba | Esperado | Obtenido | Evidencia | Estado | Límite |
|---|---|---|---|---|---|---|---|---|---|
| A1.1 | Inventariar archivos relevantes de los 4 anexos | A1.1 | `data/inventario.json`, pestaña Fuentes | `datos.inventario()` al construir; `test_originales_intactos` | ruta, sha256, bytes, función, versión por archivo | 136 ítems + estado de cada fuente nombrada | [`data/inventario.json`](data/inventario.json) | CUMPLE | `scratchpad-completo.zip` entregado **parcialmente usado**: ver A1.4 |
| A1.2 | Hash, función y versión; copia de sólo lectura; transformaciones con procedencia | A1.2, F | `originales/` + `SHA256SUMS`; `data/*` con `generado`/`fuente` | `test_registro.test_originales_intactos` | sha256 de los 4 originales = SHA256SUMS | igual; `git status` del repo sólo muestra `apd/` | [`originales/SHA256SUMS`](originales/SHA256SUMS) | CUMPLE | — |
| A1.3 | Verificar esquema y 1,398 IDs; distinguir reglas de relaciones | A1.3, A7 | `apd/registro.py:validar`; `POST /api/importar-rules-sqlite` | `test_1398_ids_de_regla`, `test_relaciones_no_son_reglas`, `test_validacion_detecta_base_incorrecta`, `test_importar_rules_sqlite` (HTTP) | 1,398 ids; relaciones contadas aparte | 1,398 filas = 1,398 ids; regla_caso 3,471 filas/1,388 reglas; regla_tarea 15,361/1,398; regla_faceta 8,722/1,196; 0 ids ajenos | [`data/registro.json`](data/registro.json) | CUMPLE | `rules.sqlite` no vino como archivo: se reconstruye con `rules_v3.py` original sin modificar; `t1.sqlite` del scratchpad coincide 1,398/1,398 textos |
| A1.4 | Procedencia de cada regla; fuentes normativas no incluidas | A1.4 | ficha de regla (archivo, línea, sha del archivo); `FUENTES_NOMBRADAS` | `test_t1_scratchpad_coincide`, `test_citas_de_flujos_literales` (80/80), `test_citas_de_sintaxis_verificadas` (831) | cada regla con archivo:línea; faltantes declarados | ver columna límite | [`data/comparacion_t1.json`](data/comparacion_t1.json), [`apd/fuentes.py`](apd/fuentes.py) | CUMPLE | No incluidos o no usados: `whystrohm.md` (fixture de shotkit ausente), `ai-production-director/SKILL.md` §6.2 l.126 (sin marcador, no está en el registro; se cita en CF-SINTAXIS-62); del scratchpad no se usan como norma f07/f08/f09 (webs), reddit/, vivaldi/, reg/*.json, llm_classify/ |
| A1.5 | Diferencia 852 vs 1,398 | A · Contexto | `data/reconciliacion.json`; pestaña Fuentes | `test_diferencia_con_852_del_ejecutor` | explicar cada id | 850 en ambos; 2 sólo en ejecutor (redacción cambió → id nuevo); 548 sólo en registro: 361 regímenes v3, 152 sin caso en v2 (`build_app.py:1142-1147`), 23 aurora-linter, 12 sin caso de producción | [`data/reconciliacion.json`](data/reconciliacion.json) | CUMPLE | — |
| A1.6 | Comparar ejecutor anterior con la app (planificación, selección, presupuesto, etapas, aprobaciones, generación, auditoría, persistencia, exportación) | A1.5 | §Matriz antes/después | `tools/evidencia_ejecutor.cjs` ejecuta las funciones reales del ejecutor | comportamiento medido, no supuesto | ver matriz | [`evidencia/ejecutor_anterior_recorte.json`](evidencia/ejecutor_anterior_recorte.json) | CUMPLE | — |

### A2 — Recorridos

| ID | Requisito | Fuente | Ubicación | Prueba | Esperado | Obtenido | Evidencia | Estado | Límite |
|---|---|---|---|---|---|---|---|---|---|
| A2.1 | Imagen aislada: génesis, T1–T5, PROD, GRAF, MULTI | A2 | `spec.detectar_caso`, `compilador.FORMATOS` | `test_flujos.TestCasosImagen` (T2,T3,T4,PROD,GRAF,MULTI), quinteto (T1), `test_edicion` (T5) | caso correcto; compila; gates originales PASS | 6/6 casos + T1 + T5 compilan; gate_image, gate_dramaturgy, ast_gate PASS; render v3.4 idéntico | `tests/test_flujos.py` | CUMPLE | Sin modelo, T2–T4/PROD/GRAF/MULTI piden al usuario sujeto, ángulo, cámara… (ambigüedad decisiva); T1 casting trae propuesta completa |
| A2.2 | Dos personas en un cuadro ≠ dos entregas | A2 | `spec.analizar_determinista` | `test_dos_personas_en_un_cuadro_no_son_dos_entregas` | 1 entrega T4; quinteto sigue en 5 | 1 T4; 5 | idem | CUMPLE | defecto encontrado y corregido en esta sesión |
| A2.3 | Imagen con referencia y roles (génesis, personaje, frame inicial/final, edición) | A2 | `flujos.ROLES_REFERENCIA`, CF-IDENTIDAD-ROL | `test_imagen_con_referencia`, `test_referencia_cambia_recorrido`, `test_edicion` | rol decide identidad (DECISIONES #3) | pasa | `tests/test_e2e.py` | CUMPLE | — |
| A2.4 | Clip aislado: movimiento, parámetros, sintaxis del modelo | A2 | formatos kling/veo/seedance | `test_clip_texto_a_video` | capas Kling, negativos aparte, aurora NO_APLICA citado (`prompt_linter.py:195`) | pasa | idem | CUMPLE | — |
| A2.5 | Spot EXPRESS/STANDARD/FILM, E0–E7, dependencias, gates | A2 | `plan.construir`, pestaña Plan | `test_spot_express`, `test_spot_standard`, `test_spot_film`, `test_shots_invalido_rechazado`, `test_e4_genera_shots_validado_y_pendiente_de_ok` | etapas por track; gates OK_E0/E1/E2/E4 bloquean | pasa | idem; `test_llm.py` | CUMPLE | — |
| A2.6 | Ancla: tarjeta D1–D9, gate de dependencias | A2 | `flujos.TARJETA_ANCLA`, preflight | `test_ancla_tarjeta_y_gate_de_dependencias` | no compila con tarjeta vacía ni sin A2 aprobado | pasa | idem | CUMPLE | — |
| A2.7 | Ancla: ángulo por acción y por número de sujetos; inferencias A PRUEBA | A2, A3.5 | `propuestas.proponer` (D9_POR_ACCION) | `test_d9_por_accion_inferencia_a_prueba`, `test_d9_por_numero_de_sujetos_ensamble`, `test_d9_explicito_del_brief_y_defecto_del_regex_original` | pico → low A PRUEBA; ensamble → eye-level fuente; D9 del brief respetado | pasa | `tests/test_flujos.py` | CUMPLE | Implementado en esta sesión (antes la tabla estaba transcrita pero no se usaba) |
| A2.8 | Vínculo ancla → shot y transferencia al motion brief | A2 | `proyecto.cargar_shots` | `test_ancla_a_clip_transferencia_motion_brief` | clip con `ancla`=FF, `frame_inicial`, identidad NO_APLICA, texto empieza con Preserve | pasa | idem | CUMPLE | — |
| A2.9 | Plan: etapas que aplican y no, con razón; sin saltar gates | A2 | pestaña Plan | UI `A6.2a`; `test_spot_*` | razón por etapa; bloqueo | 17 filas, 6 "no" con razón | [`evidencia/ui/01_plan.png`](evidencia/ui/01_plan.png) + json | CUMPLE | — |

### A3 — Decisión exhaustiva por regla

| ID | Requisito | Fuente | Ubicación | Prueba | Esperado | Obtenido | Evidencia | Estado | Límite |
|---|---|---|---|---|---|---|---|---|---|
| A3.1 | Todos los IDs con estado, fundamento, fuente, versión | A3.1 | `ledger.decidir_todas`; pestaña Reglas | `test_ninguna_regla_sin_clasificar`; UI `A3.6a` | 1,398/1,398 | 1398/1398 ids | tests + json UI | CUMPLE | U1 del usuario |
| A3.2 | NO_APLICA exige razón específica del brief | A3.1, A7 | `ledger.razon_especifica` | `test_no_aplica_sin_razon_especifica`, `test_humano_no_puede_no_aplica_generico` | razón genérica rechazada | rechazada | `tests/test_gates.py` | CUMPLE | — |
| A3.3 | Clasificaciones originales = evidencia, no veto | A3.2 | `ledger.FUERTES` | `test_evidencia_debil_no_descarta` | faceta débil nunca causa descarte | 13 reglas con evidencia débil en contra: 12 APLICA, 1 NO_APLICA por CF-TRIX-COLOR (no por la faceta) | `tests/test_flujos.py` | CUMPLE | excepción documentada: faceta d8 (modelo destino) |
| A3.4 | Lotes: ids exactos, sin duplicados ni inventados; reintento; bloqueo | A3.3, A7 | `ledger.validar_lote`, `revision.revisar_ledger` | `test_regla_omitida`, `test_decision_duplicada`, `test_id_inexistente`, `test_reintento_recupera_lote`, `test_lote_incompleto_bloquea`, `test_id_inventado_rechaza_lote`, `test_revisor_externo_misma_validacion` | rechazo y bloqueo | pasa | `tests/test_gates.py`, `test_servidor.py` | CUMPLE | — |
| A3.5 | Precedencia y conflictos con autoridad; sin resolución → decisión del usuario | A3.4 | `conflictos.CATALOGO` (6), Auditoría «Gana A/B» | `test_conflicto_se_resuelve_por_autoridad_o_por_decision_registrada`, `test_revision_externa_no_salta_el_catalogo_de_conflictos` | autoridad aplica; si falta, abierto y bloquea; decisión con razón y autor | pasa | `tests/test_flujos.py`, `test_gates.py` | CUMPLE | 2 defectos hallados y corregidos: la decisión del director no se aplicaba en 4 de 5 conflictos; una revisión externa saltaba el catálogo |
| A3.6 | Separar fuente / inferencia A PRUEBA / creativa | A3.5 | propuestas con `clase`; recibo `inferencias_a_prueba` | `test_d9_por_accion_inferencia_a_prueba`; propuestas del quinteto `clase=creativa` | tres clases visibles | pasa | idem | CUMPLE | — |
| A3.7 | Recibo verificable | A3.6 | Auditoría › Recibo; export `ledger/*.recibo.json` | UI `A3.6a` | total, estados, motivos, conflictos, no verificables | «1398/1398 ids · APLICA 160 · NO_APLICA 1233 · CONDICIONAL 5…» | json UI; export | CUMPLE | — |
| A3.8 | No llamar «100 % de acierto» a la cobertura | A3 | `auditoria._niveles` | UI `A5.5a` | 4 niveles con su «significa» | «cada id tiene una decisión válida; no prueba que cada decisión sea correcta» | json UI | CUMPLE | — |
| A3.9 | Revisión de reglas no se pierde en silencio al editar el brief | A3, A7 | `proyecto._heredar_revision`, confirmar herencia | `test_cambio_de_contexto_hereda_revision_y_bloquea_hasta_confirmar`, `test_decisiones_del_director_sobreviven_a_un_cambio_de_clave` | heredada visible, bloquea hasta confirmar o re-revisar | pasa | `tests/test_gates.py` | CUMPLE | defecto hallado en esta sesión (1,396 decisiones externas caían a determinista sin aviso) |

### A4 — Especificación, plantillas y ensamblado

| ID | Requisito | Fuente | Ubicación | Prueba | Esperado | Obtenido | Evidencia | Estado | Límite |
|---|---|---|---|---|---|---|---|---|---|
| A4.1 | Spec estructurada; `no aplica` con motivo por medio | A4 | pestaña Especificación | `test_campos_que_no_aplican_al_medio` | clip sin campos de retrato; retrato sin campos de video; motivo | pasa | `tests/test_flujos.py` | CUMPLE | — |
| A4.2 | Plantillas extraídas con procedencia; nuevas etiquetadas | A4 | `data/plantillas.json` | `test_plantillas_originales_citadas_y_nuevas_etiquetadas` | ORIGINAL con archivo; NUEVA etiquetada; notas citan tests que existen | pasa | idem | CUMPLE | se corrigieron 2 notas que citaban tests inexistentes |
| A4.3 | Bloques versionados que dicen qué reglas y campos satisfacen; sintaxis literal | A4 | `compilador.compilar`; Prompts › Bloques | `test_gates_originales_pasan` (render v3.4 idéntico); UI `A6.5b` | render original = texto de la app | igual en 5/5 | json UI | CUMPLE | — |
| A4.4 | Sintaxis por salida, modelo y composición | U2 | `data/sintaxis_fuente.json` (563 requisitos), control `sintaxis_ledger` | `test_citas_de_sintaxis_verificadas` | 831 citas literales verificadas | 831/831 | `tools/check_citas.py` | CUMPLE | U2 del usuario |
| A4.5 | Sin reescritura libre; hash visible = copiado = exportado | A4, A7 | `copiar`, `exportar` | `test_visible_copiado_exportado_mismo_hash`; UI `A7.5a` (portapapeles real) | mismo sha256 | `5d607189ad3b212a` = `5d607189ad3b212a` | json UI | CUMPLE | — |
| A4.6 | Parámetros fuera del texto; no prometer control físico | A4 | Prompts › Parámetros; notas | UI `A6.5a`; `test_no_promete_alinear_ojos` | model/size/quality/references fuera | 4 parámetros fuera; advertencia en notas | json UI | CUMPLE | — |

### A5 — Auditoría posterior

| ID | Requisito | Fuente | Ubicación | Prueba | Esperado | Obtenido | Evidencia | Estado | Límite |
|---|---|---|---|---|---|---|---|---|---|
| A5.1 | Recorrer todos los IDs; APLICA con evidencia | A5.1 | control `cobertura_ids`, `evidencia_aplica` | UI `A6.4a` (resolver 44 bloqueos desde la UI) | bloqueos listados y resolubles | 44 reglas resueltas vía «Resolver en Reglas» | json UI | CUMPLE | — |
| A5.2 | Controles deterministas + gates originales | A5.2 | `auditoria.controles`; gates como subproceso | UI `A5.2a`; `test_gates_originales_pasan` | gate_image, dramaturgy, aurora, ast_gate PASS; render idéntico | 5/5 PASS | json UI | CUMPLE | aurora: se usa la copia v1.2-fupai del repo (DECISIONES #2); la v1.1 del skill da FAIL por el tope de 130 palabras |
| A5.3a | Revisión semántica separada (revisor independiente, misma validación) | A5.3 | lotes semánticos export/import; disputa con autoridad | 3 rondas con subagentes independientes sobre el demo; `test_disputa_exige_autoridad_y_firma_no_borra` | discrepancias registradas y corregidas en bloque fuente | NO_CUMPLE por entrega: ronda 1 22/21/13/14/19 → ronda 2 1/1/1/1/6 → ronda 3 ver §Revisión semántica | [`evidencia/revision_semantica/`](evidencia/revision_semantica/) | CUMPLE | — |
| A5.3b | Revisión semántica automática con modelo por API | A5.3, F | `revision.revisar_semantica` | adaptadores contra servidor local que imita las APIs | — | no ejecutada con modelo real | `tests/test_llm.py` | BLOQUEADO POR DEPENDENCIA | sin clave de API en el entorno |
| A5.4 | Bloquear Copiar/Exportar como aprobado | A5.4 | Prompts, Exportar | UI `A5.4a`, `A6.9a`; `test_flujo_http_sin_modelo` (409) | deshabilitado / 409 | deshabilitado; 409 | json UI | CUMPLE | — |
| A5.5 | Cuatro estados distintos, nunca «fail free» | A5 | Prompts › niveles | UI `A5.5a`, `A6.10b` | cobertura / semántica / redacción / visual | 4 estados; visual EVALUADO_CON_DEFECTOS con cobertura COMPROBADA | json UI | CUMPLE | — |
| A5.6 | NO_CUMPLE semántico sólo se cierra corrigiendo o con autoridad citada; la firma humana no lo borra | A5.3 | `disputar_semantica` | `test_disputa_exige_autoridad_y_firma_no_borra` | autoridad verificable; firma conserva hallazgos | pasa | `tests/test_gates.py` | CUMPLE | implementado en esta sesión |
| A5.7 | Mutaciones concurrentes no se pisan | A5, A6.7 | `proyecto.serializado` | `test_firma_durante_auditoria_no_se_pierde` (falla sin el lock; comprobado) | firma persiste | persiste | `tests/test_gates.py` | CUMPLE | defecto hallado por la prueba de navegador |

### A6 — Experiencia visible (1–12)

| ID | Requisito | Fuente | Ubicación | Prueba | Esperado | Obtenido | Evidencia | Estado | Límite |
|---|---|---|---|---|---|---|---|---|---|
| A6.1 | Entrada de brief y ambigüedades decisivas | A6.1 | Nuevo brief | UI `A6.1a`, `A6.1b` | campos + ambigüedades | 30 ambigüedades (decisiva: modelo) | json UI | CUMPLE | — |
| A6.2 | Plan visual | A6.2 | Plan | UI `A6.2a`, `A6.2b` | recorrido, etapas, propuestas con clase | 17 filas; 36 propuestas | [`evidencia/ui/01_plan.png`](evidencia/ui/01_plan.png) | CUMPLE | — |
| A6.3 | Panel de reglas: conteos, filtros, ficha | A6.3 | Reglas | UI `A6.3a`, `A6.3b`, `A6.3c` | 1398; filtros por estado/caso/tarea/faceta/fuente/motivo; ficha con sha | «1398 de 1398»; APLICA 160 · T1 285 · E5.2 928 · d8 372 · image 166 · motivo 37 | [`evidencia/ui/03_reglas_filtro.png`](evidencia/ui/03_reglas_filtro.png) | CUMPLE | — |
| A6.4 | Editor de decisiones sin tocar originales; invalidación visible | A6.4 | Especificación, Reglas | UI `A6.4a`, `A6.4b`; `test_cambio_de_bloque_sin_cambio_de_reglas` | E2 bloqueada, E1 intacta | E1 LIBERABLE, E2 BLOQUEADA | json UI | CUMPLE | — |
| A6.5 | Previsualización con parámetros y regla por bloque | A6.5 | Prompts | UI `A6.5a`, `A6.5b` | bloque → reglas | 50 reglas enlazadas desde el primer bloque | [`evidencia/ui/02_prompt_ficha.png`](evidencia/ui/02_prompt_ficha.png) | CUMPLE | — |
| A6.6 | Comparación de versiones | A6.6 | Versiones | UI `A6.6a`; `test_visible_copiado_exportado_mismo_hash` (diff E2) | campos, textos, bloques, intactas, aprobaciones, reglas | «E2.edad · Textos regenerados: E2 (subject) · intactas E1, E3–E5» | [`evidencia/ui/06_versiones.png`](evidencia/ui/06_versiones.png) | CUMPLE | — |
| A6.7 | Progreso reanudable, consumo, sin pérdida al cerrar | A6.7 | Auditoría › trabajo; SQLite | `test_reanudable`, `test_openai` (uso real: tokens, segundos, lote n/n), UI `A6.7a`, `A6.7b` | estimación visible; nuevo navegador ve el proyecto | «~163,590 tokens de entrada…»; proyecto v6 visible tras cerrar | json UI | CUMPLE | — |
| A6.8 | Feedback dirigido al primer contrato | A6.8 | Feedback | UI `A6.8a`; `test_parece_render_y_ojos_con_imagen` | primer contrato; dependientes; independientes intactos | `comunes.tratamiento`; sólo `details` regenerado | json UI | CUMPLE | — |
| A6.9 | Exportación completa | A6.9 | Exportar | UI `A6.9a`; `test_visible_copiado_exportado_mismo_hash` | prompt, parámetros, spec, plantillas, ledger 1,398 filas, auditorías, hashes, versiones, aprobaciones | 54 archivos con MANIFIESTO de sha256 | [`evidencia/ui/export_ui.zip`](evidencia/ui/export_ui.zip) | CUMPLE | — |
| A6.10 | Evaluación visual separada | A6.10 | Evaluación visual | UI `A6.10a`, `A6.10b`; `test_parece_render_y_ojos_con_imagen` | defectos ligados a contratos; no cambia cobertura | render + ojos registrados; cobertura intacta | [`evidencia/ui/07_visual.png`](evidencia/ui/07_visual.png) | CUMPLE | registro manual; la propuesta de defectos con modelo de visión no está implementada |
| A6.11 | Sólo prompts por defecto | A6.11 | toda la app | UI `A6.11a` | ninguna ruta genera medios | ninguna | json UI | CUMPLE | — |
| A6.12 | Estado honesto sin modelo | A6.12 | barra lateral, Auditoría | UI `A6.12a`, `A6.12b`; `test_sin_modelo_no_finge`; 503 en `test_flujo_http_sin_modelo` | desactiva con explicación; inspección y revisor externo siguen | pasa | json UI | CUMPLE | — |

### A7 — Pruebas de aceptación

| ID | Requisito | Prueba | Obtenido | Estado |
|---|---|---|---|---|
| A7.1 | Importar 1,398 y detectar 852; reglas ≠ relaciones | `test_1398_ids_de_regla`, `test_diferencia_con_852_del_ejecutor`, `test_relaciones_no_son_reglas`, `test_importar_rules_sqlite` | pasa | CUMPLE |
| A7.2 | Omitida, duplicada, inexistente, lote incompleto, auditoría caducada bloquean | `test_regla_omitida`, `test_decision_duplicada`, `test_id_inexistente`, `test_lote_incompleto_bloquea`, `test_texto_cambiado_invalida_liberacion` | pasa | CUMPLE |
| A7.3 | NO_APLICA sin razón específica no pasa | `test_no_aplica_sin_razon_especifica` | pasa | CUMPLE |
| A7.4 | Cambiar brief/modelo/referencia/bloque/plantilla invalida sólo lo afectado | `test_cambio_de_modelo_invalida_todo_el_perfil`, `test_referencia_cambia_recorrido`, `test_cambio_de_bloque_sin_cambio_de_reglas`, `test_cambio_de_plantilla_invalida`, E2.edad en `test_visible_copiado_exportado_mismo_hash`, `test_cambio_de_contexto_hereda_revision…` | pasa | CUMPLE |
| A7.5 | Visible = copiado = exportado = auditado | `test_visible_copiado_exportado_mismo_hash`; UI `A7.5a` | pasa | CUMPLE |
| A7.6 | Recorridos imagen, clip, referencia, ancla, spot por track | `TestRecorridos` (8), `TestCasosImagen`, `TestAncla` | pasa | CUMPLE |
| A7.7 | Regresión quinteto: restricciones, cámara y ángulo, no genéricos, sin prometer ojos | `TestRegresionQuinteto` (6) | pasa | CUMPLE |
| A7.8 | Feedback «parece render» y «ojos desalineados» con imagen | `test_parece_render_y_ojos_con_imagen`; UI `A6.8a`, `A6.10a` | pasa | CUMPLE |
| A7.9 | Tests y hooks originales | [`ORIGINAL_TESTS_REPORT.md`](evidencia/ORIGINAL_TESTS_REPORT.md) | 16/21 PASS; 5 `check.sh` de shotkit fallan por layout + fixture `whystrohm.md` ausente (y el validador de forge falla con su propio ejemplo); documentado con shim S11 | CUMPLE (documentar fallos era lo exigido) |

### F — Formato y seguridad

| ID | Requisito | Prueba | Obtenido | Evidencia | Estado | Límite |
|---|---|---|---|---|---|---|
| F.1 | App web local ejecutable con instrucciones | UI test arranca `python3 apd/server.py` y la recorre | 29/29 | [`README.md`](README.md) | CUMPLE | — |
| F.2 | Base y datos derivados con procedencia | `datos.construir` | 10 archivos en `data/` con `generado` | [`data/`](data/) | CUMPLE | — |
| F.3 | Pruebas ejecutadas | suite + UI | ver archivos | [`evidencia/pruebas_app.txt`](evidencia/pruebas_app.txt) | CUMPLE | — |
| F.4 | Demo, prompts de muestra, auditorías | exportación del demo | 5 prompts + auditorías + ledger | [`demo/`](demo/) | CUMPLE | el demo **no es liberable**: decisiones del director pendientes (§Decisiones) |
| F.5 | Originales intactos y separados | `test_originales_intactos` | igual | `originales/` | CUMPLE | — |
| F.6 | No publicar ni desplegar | servidor en `127.0.0.1` | sin despliegue ni publicación | `server.py` | CUMPLE | — |
| F.7 | Clave sólo en servidor/entorno | `test_clave_no_sale_del_servidor`; `/api/config` sin clave; grep del repo | la clave no aparece en navegador, exportación ni repo | `tests/test_llm.py` | CUMPLE | — |
| F.8a | Flujo automático funciona con modelo compatible (protocolo) | `test_openai`, `test_anthropic` contra servidor local que imita Responses/Messages API; `test_e4_genera_shots…` | 24 lotes, 1,398 decisiones capa modelo, uso contado | `tests/test_llm.py` | CUMPLE | — |
| F.8b | Flujo automático con un modelo real | — | no ejecutado | — | BLOQUEADO POR DEPENDENCIA | sin clave; además `OPENAI_MODEL` por defecto `gpt-6-astra` viene del original (`api/config.js:12`) y **no verifiqué** que exista hoy |
| F.9 | Tiempo y consumo sin reducir reglas | UI `A6.7a`; `test_openai` (uso); `test_e4…` (reglas enviadas = todas) | todas las reglas; consumo expuesto | idem | CUMPLE | — |
| F.10 | Una sola búsqueda externa, con aprobación | — | no se buscó (no hubo aprobación explícita) | conversación | CUMPLE | — |

### Requisitos añadidos por el usuario

| ID | Requisito | Prueba | Obtenido | Estado |
|---|---|---|---|---|
| U1 | «ninguna regla en absoluto sin clasificar» | `test_ninguna_regla_sin_clasificar` | 1,398/1,398 con caso, tarea y d1–d9 (faltantes marcados `app_derivada`) | CUMPLE |
| U2 | Sintaxis por salida, modelo y composición | `test_citas_de_sintaxis_verificadas`; control `sintaxis_ledger` | 563 requisitos, 831 citas | CUMPLE |
| U3 | Longitud aspiracional; bloquear y regenerar sólo sobre 2× | `TestLongitud` (2) | corto avisa; >2× bloquea y ofrece regenerar | CUMPLE |

## Matriz antes / después

«Antes» = comportamiento comprobado en el código del ejecutor anterior (`app/ejecutor.html`, citado por línea) o
ejecutado con [`tools/evidencia_ejecutor.cjs`](tools/evidencia_ejecutor.cjs).

| Función | Comportamiento comprobado en el original | Cambio | Beneficio visible | Prueba del nuevo comportamiento |
|---|---|---|---|---|
| Planificación | `planificar()` (`ejecutor.html:549-552`) exige modelo: sin Claude falla | plan determinista desde los flujos originales (80/80 citas verificadas) | el plan existe sin modelo y cita su fuente | UI `A6.2a`; `test_spot_*` |
| Universo de reglas | 852 reglas embebidas; `reglasDe(casos)` filtra por caso | 1,398 reglas del registro v3, todas decididas una por una | nadie descarta reglas por no tener caso | `test_ninguna_regla_sin_clasificar`; `test_diferencia_con_852…` |
| Presupuesto de contexto | `empacarReglas` corta al llenar el presupuesto (`:198-201`, `:306`): T1 108/226 a 20 kB; E5 96/416 a 20 kB y 217/416 a 40 kB | lotes de 60 ids con todas las reglas; nada se recorta | cada regla se examina | [`ejecutor_anterior_recorte.json`](evidencia/ejecutor_anterior_recorte.json); `test_todos_los_ids_revisados`; `test_e4…` (enviadas = todas) |
| Auditoría | tandas en paralelo; una tanda que falla sólo añade una nota y el veredicto puede seguir en APRUEBA (`:612`, `:618`); sin control por id | validación exacta de ids por lote, reintento, bloqueo | una tanda perdida bloquea en vez de aprobar | `test_lote_incompleto_bloquea`, `test_id_inventado_rechaza_lote` |
| Aprobaciones | «Aprobar así» aprueba contra el auditor con un segundo clic (`:645-647`) | sin override: liberar exige cobertura, gates, semántica sin NO_CUMPLE abiertos y aprobación del hash; excepción sólo con autoridad citada | nada se libera por insistencia | `test_disputa_exige_autoridad…`; UI `A5.4a/b` |
| Generación | el modelo redacta el prompt completo (reescritura libre) | compilación por bloques + AST v3.4; render original idéntico | la sintaxis obligatoria se conserva literal | `test_gates_originales_pasan` (render igual) |
| Iteración | «Iterar» reinicia todas las etapas posteriores (`:640-643`) | invalidación selectiva por hash de campo/bloque | editar E2 no toca E1 | UI `A6.4b`; `test_visible_copiado…` (E2.edad) |
| Gates originales | el ejecutor no ejecuta `gate_image`, `gate_dramaturgy` ni aurora (1 mención textual en 311 kB) | se ejecutan sin modificar como subproceso en cada auditoría | el texto liberado pasó los hooks del proyecto | UI `A5.2a` |
| Persistencia | `localStorage` del navegador (`:165-180`) | SQLite en el servidor, versiones inmutables | cerrar el navegador no pierde nada; historial auditable | UI `A6.7b` |
| Exportación / hash | sin hash del texto | sha256 visible = copiado = exportado; MANIFIESTO | se puede probar qué texto se auditó | UI `A7.5a`; `test_visible_copiado…` |
| Evaluación de imagen | `evaluarImagen` (`:653`) la hace el modelo | registro manual de defectos ligados a contratos, separado de la cobertura | el veredicto visual no se confunde con la auditoría textual | `test_parece_render_y_ojos_con_imagen` |
| Sin modelo | no funciona | modo determinista honesto + revisor externo con la misma validación | se puede operar e inspeccionar sin clave | UI `A6.12a/b` |

## Revisión semántica del demo (independiente, 3 rondas)

Revisores: subagentes independientes, importados con `importar_semantica` (misma validación que el modelo:
ids exactos, sin duplicados ni inventados). Todos los veredictos y entradas están en
[`evidencia/revision_semantica/`](evidencia/revision_semantica/).

| Ronda | Versión demo | NO_CUMPLE E1/E2/E3/E4/E5 | Qué se hizo |
|---|---|---|---|
| 1 | v6 | 22 / 21 / 13 / 14 / 19 | 10 NO_CUMPLE disputados con autoridad (salían del linter v1.1 sustituido: DECISIONES #2); el resto corregido en bloque fuente: contradicción de altura de cámara, negativos fuera de Constraints, meta del pipeline en el cuerpo, «photoreal», hex del fondo, material de prendas, rasgos de identidad, asimetría facial, mirada de E5 |
| 2 | v8 | 1 / 1 / 1 / 1 / 6 | lean prose compartida corregida (encuadre duplicado, contexto del casting a notas, mirada de E4); los 5 restantes de E5 = CF-MOTOR-SW30 → conflicto para el director |
| 3 | v11 | 0 / 0 / 2 / 4 / 1 | E3: tope de 130 palabras disputado con DECISIONES #2 + U-2026-09-28-LONGITUD; E4: «calm» nombra una emoción → corregido en v12–v13 (v12 chocaba con E1 en el umbral de genericidad de la regresión A7); `54a39fd24578` (stock documental) en E3, E4 y E5 queda **para el director**: los revisores discrepan (E1/E2 lo dieron por no aplicable al tratamiento comercial) |
| 4 | v13 | E4: RONDA4 | sólo E4 (el cambio de v12–v13 invalidó sólo su revisión; E1, E2, E3 y E5 conservan la suya) |

## Decisiones que son del director (la app bloquea hasta que se tomen)

1. **CF-MOTOR-SW30** — SW30 exige instanciar todo prompt con `template_engine.build()` (T1 = luz dura documental);
   la app compila en los 5 slots de GPT Image con luz pareja de character ref. DECISIONES #2 admite ambos formatos
   sin decir cuál manda. Si gana A, la entrega queda bloqueada: la app aún no construye vía `template_engine`.
2. **`54a39fd24578` (stock documental de reportaje del template T1)**: ¿aplica a un casting de tratamiento
   comercial? Los revisores discrepan; la autoridad candidata es flujo-anclas.html Paso 4 (la fila comercial no
   usa Tri-X, CF-TRIX-COLOR). Se resuelve disputándolo con esa cita o añadiendo un look documental a color.
3. **16 CONDICIONAL y 2 CONFLICTO de regla** heredados de la revisión externa (p. ej. si el instrumento se ve;
   `7077767cb105` prohibición de softbox en rostros; `1e898f2c0308` re-rolls del crítico vs SW30 R13).
4. **Confirmar la revisión de reglas heredada** (cambiaron encuadre y textura desde la revisión externa) o re-revisar.
5. **Aprobar la redacción** de cada prompt (hash exacto).

## Limitaciones comprobadas

- Sin clave de API en este entorno: el flujo automático con modelo real y la revisión semántica por API no se
  ejecutaron (F.8b, A5.3b). La lógica está probada contra un servidor que imita ambas APIs.
- El modelo OpenAI por defecto (`gpt-6-astra`, heredado de `api/config.js`) no está verificado; fijar `OPENAI_MODEL`.
- La cobertura de IDs y la revisión semántica no certifican la imagen: ojos, piel y render se evalúan aparte.
- Hallazgos en los originales (no modificados): el patrón d9 «high» de `rules_v3.REGEX_FACETA` captura
  «contrapicado» (ángulo bajo) — la app lo compensa y hay test; los 5 `check.sh` de shotkit fallan (layout y
  fixture ausente); el linter v1.1 del skill contradice a la copia v1.2 vigente.
- Casos de imagen distintos de T1 casting: sin modelo, el usuario completa sujeto, ángulo, cámara, luz… en
  Especificación (la app lo pide como ambigüedad decisiva; no inventa).
- Evaluación visual: registro manual; no hay propuesta automática de defectos con modelo de visión.
