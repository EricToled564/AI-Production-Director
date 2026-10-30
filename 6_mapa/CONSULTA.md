# Índice del repo (memoria del agente)

Se consulta **antes** de preguntarle algo a Eric y **antes** de decir que algo falta, no existe o no está decidido.
Dice qué hay y en qué línea; lo que vale es siempre el archivo señalado. Se regenera con
`6_mapa/herramientas/indice_consulta.py`.

| Duda | Dónde mirar |
|---|---|
| Instrucciones de trabajo | `CLAUDE.md`; `.claude/rules/DECISIONES.md` (§2 de este índice) |
| ¿Eric ya decidió esto? | §2: cada decisión con archivo y línea |
| Qué falta y quién lo resuelve | `PENDIENTES.md` (§3) |
| Texto original de una regla | `2_corpus/…sqlite`, tabla `textos`, por `id` (INV-xxxxxx). Secciones de un documento: `SELECT DISTINCT encabezado FROM textos WHERE archivo=?` |
| Qué documentos tiene el corpus | §4 |
| Taxonomía, templates, casos, validadores | §1, carpetas `3_taxonomia/` y `4_diseno/` |
| Algo borrado del repo | `git log --diff-filter=D --name-only`; se recupera desde el commit anterior al borrado |


## 1. Archivos del repo (112)


**`.claude/rules/`**

- `DECISIONES.md`: 24 líneas: L1 Decisiones de dirección — 2026-09-25 · L18 Principios que salieron de la sesión y quedan como reglas de trabajo

**`./`**

- `.gitignore`: 180 bytes

**`1_originales/`**

- `AI_Production_Director_v3.4.0_COMPLETE.zip`: 750 archivos: repo 496, skills 214, (raíz) 30, project_knowledge_pack 8, original_source 2. Los de `skills/` son el corpus (§4); los demás no están en el corpus (PENDIENTES P-18). Guías: `START_HERE.md`, `INDEX.md`, `repo/.claude/hooks/README.md`
- `SHA256SUMS`: 365 bytes
- `flujo-anclas.html`: 121,772 bytes
- `flujo-spot.html`: 161,157 bytes

**`2_corpus/`**

- `BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite`: tablas: textos (13005 filas)
- `CORPUS_LITERAL_COMPLETO_13005.jsonl`: 13005 líneas JSON

**`3_taxonomia/`**

- `00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md`: 4365 líneas: L1 TAXONOMÍA CONSOLIDADA — CORRECCIÓN DE CLASIFICACIÓN 2026-10-19 · L5 Contrato vigente de esta consolidación · L25 Seleccionabilidad obligatoria — corrección 2026-10-11 22:36 UTC · L37 0. Corpus autorizado, inventario y conteos de control · L39 0.1 Corpus autorizado · L77 0.2 Inventario literal (primer paso del orden de trabajo) · L101 0.3 Inventario por capa de la taxonomía · L121 0.4 Conciliación de los 1 369 términos · L135 0.5 Respaldo de las definiciones en las fuentes autorizadas (punto 16) · L146 0.6 Disposición de contenido y límite de activación (C12) · L157 1. Principios · L184 1.12 Contrato obligatorio de lectura y clasificación por texto — 2026… · L202 1.13 Correspondencia exhaustiva entre taxonomía y templates — 2026-10… · L210 2. Bloque A — Proceso · L212 2.1 Faceta 1. Etapa — ¿en qué etapa del pipeline se aplica? (director… · L228 2.2 Faceta 2. Paso — ¿en qué paso de esa etapa? (Mapa del Spot) · L244 2.3 P-01 — Faceta de flujo (incluida por decisión del usuario) · L265 2.4 Estructura de los flujos según las fuentes (extracción mecánica d… · L267 2.4.1 FL01 — niveles y pasos de flujo-spot.html · L337 2.4.2 FL02 — Nivel 4 · subflujo atómico de génesis (flujo-spot.html) · L432 2.4.3 FL03 — pasos y subproceso de grupo de flujo-anclas.html · L469 3. Bloque B — La pieza · L471 3.1 Faceta 3. Ruta operativa — Video publicitario o Clip (DEC-000022;… · L481 3.2 Faceta 4. Tipo de pieza — ¿qué pieza se entrega? · L595 3.3 Faceta 5. Temática o industria — ¿de qué sector o tema es la piez… · L634 3.4 Faceta 6. Formato de salida — ¿en qué proporción se entrega? (sho… · L674 3.5 Faceta 7. Género narrativo (rama video y guion) — ¿qué drama cuen… · L693 3.6 Faceta 8. Estructura de beats — ¿qué arco sigue la pieza completa… · L748 3.7 Faceta 9. Patrón de montaje — ¿cómo se encadenan los planos de un… · L786 3.8 P-04 — Subcategoría contextual «Lugar de publicación» (diseño apr… · L814 4. Bloque C — El cuadro o el clip · L816 4.1 Faceta 10. Modo de generación (solo etapas 5 y 6) — ¿génesis o an… · L934 4.2 Faceta 11. Rol del ancla (solo etapa 5) — ¿para qué sirve la imag… · L959 4.3 Faceta 12. Función del plano — ¿qué trabajo hace este plano en la… · L1002 4.4 Faceta 13. Tipo de acción — ¿qué pasa en el cuadro? (flujo-anclas… · L1030 4.5 Faceta 14. Régimen físico — ¿en qué medio físico ocurre? (regimen… · L1059 4.6 Faceta 15. Sujeto — ¿qué clase de cosa se fija en la imagen? (flu… · L1090 4.7 Faceta 16. Espacio — ¿dónde ocurre? · L1105 4.8 Faceta 17. Estilo visual — ¿qué look tiene? (flujo-anclas D4; ima… · L1145 4.9 Faceta 18. Técnica de representación — ¿con qué técnica se hace l… · L1188 4.10 Faceta 19. Número de sujetos — ¿cuántos sujetos individuales hay… · L1207 4.11 Faceta 20. Identidad de las personas — ¿se deben reconocer? · L1226 4.12 Faceta 21. Contacto físico entre personas — ¿se tocan? · L1241 4.13 Faceta 22. Tamaño del rostro — ¿cuánto ocupa del cuadro? · L1258 4.14 Faceta 23. Referencias adjuntas (solo etapas 5 y 6) — ¿qué refer… · L1324 4.15 Faceta 24. Tamaño de plano — ¿cuánto del sujeto entra en cuadro?… · L1354 4.16 Faceta 25. Ángulo — ¿desde dónde mira la cámara? (flujo-anclas D… · L1392 4.17 Faceta 26. Movimiento de cámara (clip y contexto de ancla/keyfra… · L1453 4.18 Faceta 27. Transición (clip y contexto de ancla/keyframe según F… · L1503 4.19 Faceta 28. Audio (clip y contexto de ancla/keyframe según F11 y … · L1534 4.20 Faceta 29. Modelo (solo etapas 5 y 6) — ¿para qué modelo vale la… · L1581 5. Bloque D — Atributos de la regla · L1583 5.1 Faceta 30. Qué regula — ¿sobre qué aspecto decide la regla? · L1610 5.1.1 P-03 — tres valores nuevos (decisión de diseño aprobada) · L1620 5.1.2 Vocabulario de términos por valor de la faceta 30 · L1622 «estrategia y concepto» — 13 términos · L1640 «estructura narrativa y diálogo» — 0 términos · L1644 «dramaturgia» — 37 términos · L1686 «encuadre y lente» — 52 términos · L1743 «ángulo» — 0 términos · L1747 «movimiento de cámara» — 0 términos · L1751 «luz» — 68 términos · L1824 «color, grade y textura» — 44 términos · L1873 «composición» — 76 términos · L1954 «identidad y consistencia» — 21 términos · L1980 «anatomía, rostro y piel» — 35 términos · L2020 «física y movimiento congelado» — 50 términos · L2075 «texto en pantalla» — 36 términos · L2116 «marca y logos» — 39 términos · L2160 «estructura y sintaxis del prompt» — 46 términos · L2211 «parámetros técnicos» — 70 términos · L2286 «audio» — 18 términos · L2309 «continuidad entre clips» — 11 términos · L2325 «crítica y revisión» — 43 términos · L2373 «trazabilidad y entrega» — 94 términos · L2472 «materialidad y superficie» — 25 términos · L2502 «puesta en escena y blocking» — 14 términos · L2521 «animación» — 12 términos · L2540 5.2 Faceta 31. Condición para avanzar — ¿bloquea el paso a la siguien… · L2560 5.3 P-05 — Faceta «Ámbito funcional» y campo «uso operativo» (decisió… · L2584 5.4 P-02 — Autoridad como metadato (decisión de diseño aprobada) · L2588 6. Bloque E — Metadatos de la regla · L2590 6.0 Campos · L2614 6.1 Valores de los campos tomados del borrador · L2616 Campo «medio» — 5 valores · L2628 Campo «unidad» — 5 valores · L2640 Campo «tipo de enunciado» — 3 valores · L2648 Campo «fuerza normativa» — 4 fuerzas y estado no normativo · L2659 Campo «origen de evidencia» — 8 valores (incluye delta DOC01) · L2673 Campo «evidencia de la afirmación fuente» — 4 descriptores documental… · L2682 Campo «adopción canónica» — 2 valores · L2691 Campo «operador de condición» — 6 valores · L2702 Campo «estado de evidencia» — 5 valores · L2712 Campo «dependencia» — 2 valores · L2719 6.2 Precedencias establecidas por los textos originales · L2742 6.3 Autoridad declarada por las fuentes (tabla del director §1) · L2764 6.4 P-07 — E6.5 conservado, Aurora excluida y fallback del original · L2780 6.5 P-06 — Paginación asignada (convención aprobada) · L2784 7. Registro, condiciones, brief y consulta · L2786 7.1 Registro mínimo de una regla · L2798 7.2 Lógica de condiciones · L2802 7.3 Brief: exploración frente a selección definitiva · L2806 7.4 Consulta: una sola salida por regla · L2818 Anexo 1 — HISTÓRICO: cambios v3 → v4 por sección e ID · L2846 Anexo 2 — Conciliación término por término (1 369 filas) · L4222 Anexo 3 — Términos sin presencia en fuente autorizada · L4286 Anexo 4 — HISTÓRICO: decisiones de la edición base C18; complementada… · L4303 Anexo 5 — HISTÓRICO: comprobaciones de C11–C17 y sus límites · L4311 Anexo 6 — Correspondencias con la taxonomía anterior (no son fuentes … · L4327 Anexo de conciliación de citas · L4333 Actualización estructural P-04 · L4337 Gate final de aceptación bidireccional · L4351 Historial: canonización de la edición base C18 (2026-10-03) · L4355 Anexo histórico de tracks (no operativo; DEC-000022)

**`4_diseno/`**

- `DISENO_APLICACION_Y_CLASIFICACION.md`: 133 líneas: L1 Diseño de la aplicación y del procedimiento de clasificación · L16 1. La aplicación: qué partes tiene · L31 2. La experiencia del usuario: el flujo de un pedido · L46 3. Procedimiento de clasificación [NUEVO 29-oct] · L48 3.0 Estructura de cada texto (mecánica, antes de clasificar) · L65 3.1 Ronda de tipo de texto · L85 3.2 La matriz · L93 3.3 Primera ronda: mecánica · L103 3.4 Segunda ronda: revisión del texto, una categoría por vez · L107 3.5 Controles de cada ronda · L114 4. Pendientes de este diseño (decide Eric) · L125 5. Orden de ejecución

**`4_diseno/casos/`**

- `README_CASOS_DE_USO.md`: 61 líneas: L1 Base de opciones y composición de casos de uso · L3 Qué contiene esta entrega · L9 Archivos · L24 Diferencias que deben preservarse · L30 Vocabulario operativo y conciliación · L42 Construcción del caso, de general a específico · L55 Verificación y límites medidos
- `bind_templates.py`: sin docstring
- `build_catalog.py`: sin docstring
- `case.schema.json`: 6 claves: $schema, title, type, additionalProperties, required, properties
- `casos_opciones.sqlite`: tablas: opciones (1729 filas)
- `catalogo_opciones.csv`: 1729 filas; columnas: id,kind,facet,subject,label,definition,disposition,case_selectable,physical_paths,destination_inher…
- `catalogo_opciones.json`: lista de 1729 elementos
- `conteos.json`: 10 claves: total_records, terms, facet_values, facets, by_disposition, by_facet, case_selectable, missing_paths, schema_paths_checked, schema_path_errors
- `jerarquia_valores.json`: lista de 1729 elementos
- `manifest_fuentes.json`: 2 claves: taxonomy, limitations
- `mapa_facetas.json`: 31 claves: F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12 …
- `mapa_materias_f30.json`: 24 claves: orquestación y control de flujo, estrategia y concepto, estructura narrativa y diálogo, dramaturgia, encuadre y lente, ángulo, movimiento de cámara, luz, color, grade y textura, composición, identidad y consistencia, anatomía, rostro y piel …
- `mapa_materias_f30_paths.json`: 24 claves: orquestación y control de flujo, estrategia y concepto, estructura narrativa y diálogo, dramaturgia, encuadre y lente, ángulo, movimiento de cámara, luz, color, grade y textura, composición, identidad y consistencia, anatomía, rostro y piel …
- `relaciones_documentadas.json`: lista de 473 elementos
- `rutas_documentadas.json`: lista de 184 elementos
- `validar.py`: sin docstring
- `verificacion.json`: 9 claves: rutas_comprobadas_en_schema, validacion_estructural, registros, TRM, IDs_duplicados, destinos_vacios, facetas, asociaciones_REG, compatibilidad_semantica

**`4_diseno/copias_identicas/casos_templates/`**

- `CONTRATO_IMAGEN_ORQUESTACION.schema.json`: 7 claves: $schema, $id, title, type, properties, additionalProperties, required
- `REGISTRO_DESTINOS_TEMPLATE.json`: 7 claves: version, schema_file, facet_destinations, aliases, fields, f30_destinations, scope_destinations

**`4_diseno/copias_identicas/decisiones/`**

- `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`: 387 líneas: L1 Templates revisados de entrada y salida: imagen y orquestación · L5 1. Autoridad y alcance · L9 2. Secuencia obligatoria de uso · L21 3. Ficha rellenables T-BRIEF-IMG · L138 4. Tarjeta de ancla D1–D9 · L142 5. Contratos por operación · L144 T-GENESIS · L149 T-REF-COMP · L154 T-ANCLA-REF · L159 T-ANCLA-FF · L164 T-ANCLA-LF · L169 T-EDIT · L174 T-STYLE · L179 T-SKETCH · L184 6. Templates de salida por modelo · L187 GPT2-GEN · L201 GPT2-EDIT · L213 NB-PROSE · L223 NB-COMP · L234 NB-EDIT · L244 NB-COMPLEX · L268 FLUX-GEN · L278 MJ-GEN · L288 IDEOGRAM-COMPOSITED · L298 IDEOGRAM-TEXT · L308 SEEDREAM-GEN · L318 GPT15-GEN · L329 GPT-IMAGE-1-MIGRATION · L340 GPT-IMAGE-1-MINI-MIGRATION · L351 Reglas de serialización de variantes · L357 7. Salida común rellenables · L371 8. T-ORQ: contrato ejecutable de eventos y gates · L375 9. T-ACEPTACIÓN y T-TRAZA · L379 10. Cobertura y validación · L383 11. Fuentes y atribución · L386 12. Obligatoriedad revisada por módulo

**`4_diseno/`**

- `jerarquia_de_lectura.md`: 22 líneas: L1 Jerarquía de lectura de la clasificación · L5 Texto · L19 Dónde más aparece, en parte
- `niveles_de_generalidad.md`: 21 líneas: L1 Niveles de generalidad de una regla (universalidad) · L5 Texto · L17 Dónde más aparece, en parte

**`4_diseno/templates/`**

- `CONTRATOS_OPERACION_MODELO.json`: 8 claves: version, operation_contracts, model_adapters, binding_contract, variant_contracts, parameter_serialization, limitations, conditional_modules
- `CONTRATO_IMAGEN_ORQUESTACION.schema.json`: 7 claves: $schema, $id, title, type, properties, additionalProperties, required
- `FIELD_MAP.csv`: 94 filas; columnas: item_id,destino_path,tipo_destino,schema
- `FUENTES_CONTRATOS.json`: 3 claves: taxonomia, fuentes, alcance
- `MANIFIESTO.json`: 2 claves: version, files
- `REGISTRO_DESTINOS_TEMPLATE.json`: 7 claves: version, schema_file, facet_destinations, aliases, fields, f30_destinations, scope_destinations
- `RESULTADOS_PRUEBAS_ESTRUCTURALES.json`: 4 claves: scope, tests, passed, total
- `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`: 387 líneas: L1 Templates revisados de entrada y salida: imagen y orquestación · L5 1. Autoridad y alcance · L9 2. Secuencia obligatoria de uso · L21 3. Ficha rellenables T-BRIEF-IMG · L138 4. Tarjeta de ancla D1–D9 · L142 5. Contratos por operación · L144 T-GENESIS · L149 T-REF-COMP · L154 T-ANCLA-REF · L159 T-ANCLA-FF · L164 T-ANCLA-LF · L169 T-EDIT · L174 T-STYLE · L179 T-SKETCH · L184 6. Templates de salida por modelo · L187 GPT2-GEN · L201 GPT2-EDIT · L213 NB-PROSE · L223 NB-COMP · L234 NB-EDIT · L244 NB-COMPLEX · L268 FLUX-GEN · L278 MJ-GEN · L288 IDEOGRAM-COMPOSITED · L298 IDEOGRAM-TEXT · L308 SEEDREAM-GEN · L318 GPT15-GEN · L329 GPT-IMAGE-1-MIGRATION · L340 GPT-IMAGE-1-MINI-MIGRATION · L351 Reglas de serialización de variantes · L357 7. Salida común rellenables · L371 8. T-ORQ: contrato ejecutable de eventos y gates · L375 9. T-ACEPTACIÓN y T-TRAZA · L379 10. Cobertura y validación · L383 11. Fuentes y atribución · L386 12. Obligatoriedad revisada por módulo
- `VERIFICACION_ESTRUCTURAL.json`: 9 claves: schema_valid, facets, f30_materials, typed_fields, operation_contracts, model_adapter_contracts, path_occurrences_checked, invalid_paths, scope
- `probar_contratos.py`: Fixtures sintéticos de estructura: no son testigos semánticos de reglas.
- `verificar_templates.py`: Structural checks plus instance checks. No claim of corpus semantic review.

**`4_diseno/validadores/`**

- `gate_dramaturgy.py`: Stop hook: blocks delivery of visual prompts that carry banned vocabulary.
- `gate_image.py`: Stop hook: enforces the image skill's own golden rules on delivered prompts.
- `gate_microgate.py`: Stop hook: enforce the 3-line micro-gate header on any visual delivery.
- `gate_shots.py`: PostToolUse hook: runs the shotkit validator whenever shots.json is written.
- `inject_rules.py`: UserPromptSubmit hook: put the mandatory rules in context before Claude chooses.
- `prompt_detect.py`: Decide si un bloque cercado es la entrega de un prompt visual.
- `settings.json`: 1 claves: hooks

**`5_decisiones/`**

- `01021_DECISIONES_APLICADAS_20261011_224300.md`: 25 líneas: L1 Decisiones aplicadas a la entrega corregida — 2026-10-11 · L15 Decisión explícita de las 16:56:54.532502 UTC · L19 Verificación documental y límites de capacidad · L23 Cierre del trabajo de candidatas
- `01022_DELTA_DECISIONES_CONSOLIDADO_20261011_224300.md`: 226 líneas: L1 Delta y decisiones consolidadas — 2026-10-11 · L3 Estado y autorización · L11 Cambios del contrato · L28 Jerarquías y estados · L34 DEC-000026 y DEC-000027: evidencia disponible y límite · L42 Registro histórico recibido · L46 DEC-000001 · L53 DEC-000002 · L59 DEC-000003 · L65 DEC-000004 · L71 DEC-000005 · L78 DEC-000006 · L84 DEC-000007 · L90 DEC-000008 · L96 DEC-000009 · L102 DEC-000010 · L108 DEC-000011 · L114 DEC-000012 · L121 DEC-000013 · L127 DEC-000014 · L133 DEC-000015 · L139 DEC-000016 · L145 DEC-000017 · L151 DEC-000018 · L157 DEC-000019 · L164 DEC-000020 · L171 DEC-000021 · L178 DEC-000022 · L184 DEC-000023 · L192 DEC-000024 · L198 DEC-000025 · L205 Decisión adicional explícita: anclas/keyframes, 2026-10-11 16:56:54.5… · L216 Cierre de verificación documental, sin inventar rendimiento actual · L224 Resultado de aplicación de la decisión de anclas/keyframes
- `01062_registro_decisiones_DOC01.md`: 86 líneas: L1 Registro de decisiones del usuario sobre DOC01 · L4 DEC-000001 · L8 DEC-000002 · L11 DEC-000003 · L14 DEC-000004 · L17 DEC-000005 · L21 DEC-000006 · L24 DEC-000007 · L27 DEC-000008 · L30 DEC-000009 · L33 DEC-000010 · L36 DEC-000011 · L39 DEC-000012 · L43 DEC-000013 · L46 DEC-000014 · L49 DEC-000015 · L52 DEC-000016 · L55 DEC-000017 · L58 DEC-000018 · L61 DEC-000019 · L65 DEC-000020 · L69 DEC-000021 · L73 DEC-000022 · L76 DEC-000023 · L81 DEC-000024 · L84 DEC-000025
- `DECISIONES_ERIC_20261023.md`: 41 líneas: L1 Decisiones de Eric Toledano — 2026-10-23
- `DECISIONES_ERIC_20261024.md`: 25 líneas: L1 Decisiones de Eric Toledano — 2026-10-24
- `DECISIONES_ERIC_20261026.md`: 121 líneas: L1 Decisiones de Eric Toledano — 2026-10-26
- `DECISIONES_ERIC_20261027_30.md`: 60 líneas: L1 Instrucciones de Eric dadas en conversación (2026-10-27 a 2026-10-30)
- `DECISIONES_ERIC_RESCATADAS_20261027.md`: 16 líneas: L1 Decisiones de Eric rescatadas antes de borrar las apps (2026-10-27) · L5 De `apd/demo/LEEME.md` (líneas 39–40; app apd, 2026-09-28) · L10 De `taller/recursos/` (movidos, no copiados, a `taller/catalogo/fuent…
- `DECISIONES_repo_20260925.md`: 24 líneas: L1 Decisiones de dirección — 2026-09-25 · L18 Principios que salieron de la sesión y quedan como reglas de trabajo

**`5_decisiones/directivas_20261021/`**

- `MANIFIESTO.json`: 2 claves: nota, archivos
- `canonical_sources.json`: lista de 36 elementos
- `catalogo_especificas.json`: lista de 607 elementos
- `directivas_taller.json`: lista de 2 elementos
- `operation_packs.json`: lista de 4 elementos
- `template_brief.json`: 4 claves: brief, operation_contract, annotations, source
- `universal_rules.json`: 5 claves: version, status, universal_rule_ids, selection_policy, rules
- `user_directives.json`: lista de 2 elementos

**`6_mapa/`**

- `00_indice.md`: 45 líneas: L1 Mapa del repositorio AI-Production-Director · L5 Qué responde este documento · L18 Cómo se hizo · L27 Capítulos
- `01_archivos_fuera_del_catalogo.md`: 60 líneas: L1 2. Los archivos del repo fuera del catálogo · L11 2.1 `CLAUDE.md` · L22 2.2 `.claude/settings.json` y `.claude/hooks/` · L36 2.3 `.claude/rules/` · L40 `DECISIONES.md` · L44 `regimenes/` y `research/` · L48 2.4 `1_originales/` (4 archivos) · L57 2.5 `produccion/template-retrato-gpt2/`
- `01_organizacion_y_utilidad.md`: 81 líneas: L1 1. Cómo está organizada la información y qué sirve · L3 1.1 Lo que pediste y dónde está · L20 1.2 Las cinco capas de información · L33 1.3 Cómo se usa cada capa en el sistema · L45 1.4 Qué es útil y qué es basura en el repo · L70 1.5 Qué es útil y qué es basura dentro del corpus
- `02_catalogo_originales_y_decisiones.md`: 143 líneas: L1 3. El catálogo: originales, decisiones y jerarquía de autoridad · L5 3.1 Jerarquía de autoridad · L17 3.2 El corpus (`2_corpus/`) · L26 3.3 La taxonomía (`3_taxonomia/00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADO… · L45 3.4 El diseño: PLAN_V5, TEMPLATES y CASOS · L47 PLAN_V5 (`4_diseno/PLAN_V5_COMPLETO_TAXONOMIA_TEMPLATES_20261019_0543… · L74 Paquete TEMPLATES (`4_diseno/templates/`) · L88 Paquete CASOS (`4_diseno/casos/`) · L104 3.5 Paquete y directivas de Eric del 21–22 de octubre (`5_decisiones/… · L126 3.6 Las decisiones de Eric (`5_decisiones/`)
- `03_corpus_datos.md`: 2419 líneas: L1 4. El corpus: cuántos textos hay y cómo están estructurados · L5 4.0 Qué es cada skill (descripción literal de su frontmatter) · L7 `skills/ai-production-director/SKILL.md` · L22 `skills/ai-video-storyboard/SKILL.md` · L31 `skills/brand-lock-extractor/SKILL.md` · L40 `skills/image/SKILL.md` · L57 `skills/screenwriter/SKILL.md` · L73 `skills/storyboard-architect/SKILL.md` · L82 `skills/storyboard-html-preview/SKILL.md` · L91 `skills/video/SKILL.md` · L101 `skills/visual-asset-critic/SKILL.md` · L110 `skills/visual-media/SKILL.md` · L125 `skills/visual-prompt-forge/SKILL.md` · L135 4.1 Totales por skill · L154 4.2 Tipo de documento por skill · L172 4.3 Tipo de unidad por skill · L193 4.4 Los 206 archivos · L405 4.5 Todas las secciones de cada archivo (ruta de encabezados h1–h6 y … · L410 `flujos/flujo-anclas.html` · L414 `flujos/flujo-spot.html` · L418 `skills/ai-production-director/SKILL.md` · L445 `skills/ai-production-director/references/creative-strategy.md` · L454 `skills/ai-production-director/references/production-package.md` · L462 `skills/ai-video-storyboard/SKILL.md` · L479 `skills/ai-video-storyboard/examples/tiktok-reel-30s-coffee.md` · L492 `skills/brand-lock-extractor/LICENSE` · L496 `skills/brand-lock-extractor/SKILL.md` · L518 `skills/brand-lock-extractor/brand-packs/README.md` · L528 `skills/brand-lock-extractor/brand-packs/_template.md` · L542 `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` · L556 `skills/brand-lock-extractor/examples/brand-lock.md` · L570 `skills/brand-lock-extractor/examples/input-brief.md` · L576 `skills/brand-lock-extractor/references/extraction-rubric.md` · L590 `skills/brand-lock-extractor/templates/brand-lock.md.tpl` · L604 `skills/brand-lock-extractor/tools/README.md` · L625 `skills/brand-lock-extractor/tools/_shotkit.py` · L629 `skills/brand-lock-extractor/tools/_template.py` · L633 `skills/brand-lock-extractor/tools/check.sh` · L637 `skills/brand-lock-extractor/tools/copy-prompt.py` · L641 `skills/brand-lock-extractor/tools/shots-to-html.py` · L645 `skills/brand-lock-extractor/tools/validate_brand_lock.py` · L649 `skills/brand-lock-extractor/tools/validate_capabilities.py` · L653 `skills/brand-lock-extractor/tools/validate_critique.py` · L657 `skills/brand-lock-extractor/tools/validate_prompts.py` · L661 `skills/brand-lock-extractor/tools/validate_provenance.py` · L665 `skills/brand-lock-extractor/tools/validate_schemas.py` · L669 `skills/brand-lock-extractor/tools/validate_shots.py` · L673 `skills/brand-lock-extractor/tools/validate_skills.py` · L677 `skills/image/LICENSE` · L681 `skills/image/NOTICE` · L685 `skills/image/SKILL.md` · L700 `skills/image/references/characters.md` · L712 `skills/image/references/creative-direction.md` · L721 `skills/image/references/dimensional.md` · L732 `skills/image/references/editing.md` · L745 `skills/image/references/golden-rules.md` · L764 `skills/image/references/gpt-image.md` · L787 `skills/image/references/models.md` · L798 `skills/image/references/multi-panel.md` · L817 `skills/image/references/nano-banana.md` · L835 `skills/image/references/patterns/character-design.md` · L846 `skills/image/references/patterns/ecommerce.md` · L856 `skills/image/references/patterns/fashion-editorial.md` · L866 `skills/image/references/patterns/food-beverage.md` · L876 `skills/image/references/patterns/portrait-cinema.md` · L886 `skills/image/references/patterns/poster-illustration.md` · L897 `skills/image/references/patterns/ui-social.md` · L908 `skills/image/references/prompt-framework.md` · L931 `skills/image/references/slides.md` · L965 `skills/image/references/storyboards.md` · L977 `skills/image/references/structural.md` · L989 `skills/image/references/text-rendering.md` · L1001 `skills/image/references/vision-decomposer.md` · L1015 `skills/screenwriter/SKILL.md` · L1046 `skills/screenwriter/references/advanced-techniques.md` · L1070 `skills/screenwriter/references/pipeline-integration.md` · L1096 `skills/storyboard-architect/LICENSE` · L1100 `skills/storyboard-architect/SKILL.md` · L1126 `skills/storyboard-architect/brand-packs/README.md` · L1136 `skills/storyboard-architect/brand-packs/_template.md` · L1150 `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lo… · L1164 `skills/storyboard-architect/examples/30s-pain-proof-promise/preview.… · L1168 `skills/storyboard-architect/examples/30s-pain-proof-promise/run.json` · L1172 `skills/storyboard-architect/examples/30s-pain-proof-promise/shots.js… · L1176 `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboa… · L1193 `skills/storyboard-architect/examples/30s-pain-proof-promise/text-ove… · L1197 `skills/storyboard-architect/examples/60s-founder-explainer/brand-loc… · L1211 `skills/storyboard-architect/examples/60s-founder-explainer/preview.h… · L1215 `skills/storyboard-architect/examples/60s-founder-explainer/run.json` · L1219 `skills/storyboard-architect/examples/60s-founder-explainer/shots.jso… · L1223 `skills/storyboard-architect/examples/60s-founder-explainer/storyboar… · L1241 `skills/storyboard-architect/examples/60s-founder-explainer/text-over… · L1245 `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.sn… · L1260 `skills/storyboard-architect/examples/shotkit-explainer/preview.html` · L1264 `skills/storyboard-architect/examples/shotkit-explainer/run.json` · L1268 `skills/storyboard-architect/examples/shotkit-explainer/shots.json` · L1272 `skills/storyboard-architect/examples/shotkit-explainer/storyboard.md` · L1286 `skills/storyboard-architect/examples/shotkit-explainer/text-overlays… · L1290 `skills/storyboard-architect/references/beat-frameworks.md` · L1300 `skills/storyboard-architect/references/on-screen-text.md` · L1315 `skills/storyboard-architect/references/shot-grammar.md` · L1326 `skills/storyboard-architect/references/timing-rules.md` · L1336 `skills/storyboard-architect/templates/run.schema.json` · L1340 `skills/storyboard-architect/templates/shots.schema.json` · L1344 `skills/storyboard-architect/templates/storyboard.md.tpl` · L1356 `skills/storyboard-architect/templates/text-overlays.schema.json` · L1360 `skills/storyboard-architect/tools/README.md` · L1381 `skills/storyboard-architect/tools/_shotkit.py` · L1385 `skills/storyboard-architect/tools/_template.py` · L1389 `skills/storyboard-architect/tools/check.sh` · L1393 `skills/storyboard-architect/tools/copy-prompt.py` · L1397 `skills/storyboard-architect/tools/shots-to-html.py` · L1401 `skills/storyboard-architect/tools/validate_brand_lock.py` · L1405 `skills/storyboard-architect/tools/validate_capabilities.py` · L1409 `skills/storyboard-architect/tools/validate_critique.py` · L1413 `skills/storyboard-architect/tools/validate_prompts.py` · L1417 `skills/storyboard-architect/tools/validate_provenance.py` · L1421 `skills/storyboard-architect/tools/validate_schemas.py` · L1425 `skills/storyboard-architect/tools/validate_shots.py` · L1429 `skills/storyboard-architect/tools/validate_skills.py` · L1433 `skills/storyboard-html-preview/LICENSE` · L1437 `skills/storyboard-html-preview/SKILL.md` · L1461 `skills/storyboard-html-preview/templates/preview.html.tpl` · L1465 `skills/storyboard-html-preview/templates/print.css.tpl` · L1469 `skills/storyboard-html-preview/templates/styles.css.tpl` · L1473 `skills/storyboard-html-preview/tools/README.md` · L1494 `skills/storyboard-html-preview/tools/_shotkit.py` · L1498 `skills/storyboard-html-preview/tools/_template.py` · L1502 `skills/storyboard-html-preview/tools/check.sh` · L1506 `skills/storyboard-html-preview/tools/copy-prompt.py` · L1510 `skills/storyboard-html-preview/tools/shots-to-html.py` · L1514 `skills/storyboard-html-preview/tools/validate_brand_lock.py` · L1518 `skills/storyboard-html-preview/tools/validate_capabilities.py` · L1522 `skills/storyboard-html-preview/tools/validate_critique.py` · L1526 `skills/storyboard-html-preview/tools/validate_prompts.py` · L1530 `skills/storyboard-html-preview/tools/validate_provenance.py` · L1534 `skills/storyboard-html-preview/tools/validate_schemas.py` · L1538 `skills/storyboard-html-preview/tools/validate_shots.py` · L1542 `skills/storyboard-html-preview/tools/validate_skills.py` · L1546 `skills/video/LICENSE` · L1550 `skills/video/NOTICE` · L1554 `skills/video/SKILL.md` · L1568 `skills/video/references/animatic-keyframes.md` · L1582 `skills/video/references/camera-lighting-vocabulary.md` · L1598 `skills/video/references/dramaturgy.md` · L1632 `skills/video/references/fixes-and-skeletons.md` · L1667 `skills/video/references/kling.md` · L1711 `skills/video/references/patterns-and-genres.md` · L1737 `skills/video/references/race-and-speed.md` · L1755 `skills/video/references/role-modes.md` · L1778 `skills/video/references/seedance-25.md` · L1812 `skills/video/references/seedance.md` · L1845 `skills/video/references/universal-rules.md` · L1865 `skills/video/references/veo.md` · L1894 `skills/visual-asset-critic/LICENSE` · L1898 `skills/visual-asset-critic/SKILL.md` · L1923 `skills/visual-asset-critic/examples/critique.accept.json` · L1927 `skills/visual-asset-critic/examples/critique.revise.json` · L1931 `skills/visual-asset-critic/examples/worked-run/brand-lock.snapshot.m… · L1945 `skills/visual-asset-critic/examples/worked-run/critiques/round-1/sho… · L1949 `skills/visual-asset-critic/examples/worked-run/critiques/round-1/sho… · L1953 `skills/visual-asset-critic/examples/worked-run/critiques/round-2/sho… · L1957 `skills/visual-asset-critic/examples/worked-run/preview.html` · L1961 `skills/visual-asset-critic/examples/worked-run/prompts/round-1/flux.… · L1965 `skills/visual-asset-critic/examples/worked-run/prompts/round-2/revis… · L1969 `skills/visual-asset-critic/examples/worked-run/run.json` · L1973 `skills/visual-asset-critic/examples/worked-run/shots.json` · L1977 `skills/visual-asset-critic/examples/worked-run/text-overlays.json` · L1981 `skills/visual-asset-critic/references/critique-rubric.md` · L1994 `skills/visual-asset-critic/templates/critique.schema.json` · L1998 `skills/visual-asset-critic/tools/README.md` · L2019 `skills/visual-asset-critic/tools/_shotkit.py` · L2023 `skills/visual-asset-critic/tools/_template.py` · L2027 `skills/visual-asset-critic/tools/check.sh` · L2031 `skills/visual-asset-critic/tools/copy-prompt.py` · L2035 `skills/visual-asset-critic/tools/shots-to-html.py` · L2039 `skills/visual-asset-critic/tools/validate_brand_lock.py` · L2043 `skills/visual-asset-critic/tools/validate_capabilities.py` · L2047 `skills/visual-asset-critic/tools/validate_critique.py` · L2051 `skills/visual-asset-critic/tools/validate_prompts.py` · L2055 `skills/visual-asset-critic/tools/validate_provenance.py` · L2059 `skills/visual-asset-critic/tools/validate_schemas.py` · L2063 `skills/visual-asset-critic/tools/validate_shots.py` · L2067 `skills/visual-asset-critic/tools/validate_skills.py` · L2071 `skills/visual-media/SKILL.md` · L2099 `skills/visual-prompt-forge/LICENSE` · L2103 `skills/visual-prompt-forge/SKILL.md` · L2134 `skills/visual-prompt-forge/adapters/_capabilities.json` · L2138 `skills/visual-prompt-forge/adapters/capabilities.schema.json` · L2142 `skills/visual-prompt-forge/adapters/flux.md` · L2156 `skills/visual-prompt-forge/adapters/gpt-image.md` · L2169 `skills/visual-prompt-forge/adapters/hailuo.md` · L2181 `skills/visual-prompt-forge/adapters/ideogram.md` · L2195 `skills/visual-prompt-forge/adapters/kling.md` · L2208 `skills/visual-prompt-forge/adapters/midjourney.md` · L2221 `skills/visual-prompt-forge/adapters/nano-banana.md` · L2235 `skills/visual-prompt-forge/adapters/seedance.md` · L2247 `skills/visual-prompt-forge/adapters/seedream.md` · L2261 `skills/visual-prompt-forge/adapters/veo.md` · L2274 `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` · L2283 `skills/visual-prompt-forge/examples/one-shot-all-adapters/flux.txt` · L2287 `skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.… · L2291 `skills/visual-prompt-forge/examples/one-shot-all-adapters/ideogram.t… · L2295 `skills/visual-prompt-forge/examples/one-shot-all-adapters/kling.txt` · L2299 `skills/visual-prompt-forge/examples/one-shot-all-adapters/midjourney… · L2303 `skills/visual-prompt-forge/examples/one-shot-all-adapters/nano-banan… · L2307 `skills/visual-prompt-forge/examples/one-shot-all-adapters/seedream.t… · L2311 `skills/visual-prompt-forge/references/consistency-locks.md` · L2325 `skills/visual-prompt-forge/references/failure-modes.md` · L2337 `skills/visual-prompt-forge/references/prompt-anatomy.md` · L2348 `skills/visual-prompt-forge/tools/README.md` · L2369 `skills/visual-prompt-forge/tools/_shotkit.py` · L2373 `skills/visual-prompt-forge/tools/_template.py` · L2377 `skills/visual-prompt-forge/tools/check.sh` · L2381 `skills/visual-prompt-forge/tools/copy-prompt.py` · L2385 `skills/visual-prompt-forge/tools/shots-to-html.py` · L2389 `skills/visual-prompt-forge/tools/validate_brand_lock.py` · L2393 `skills/visual-prompt-forge/tools/validate_capabilities.py` · L2397 `skills/visual-prompt-forge/tools/validate_critique.py` · L2401 `skills/visual-prompt-forge/tools/validate_prompts.py` · L2405 `skills/visual-prompt-forge/tools/validate_provenance.py` · L2409 `skills/visual-prompt-forge/tools/validate_schemas.py` · L2413 `skills/visual-prompt-forge/tools/validate_shots.py` · L2417 `skills/visual-prompt-forge/tools/validate_skills.py`
- `04_etapas_datos.md`: 276 líneas: L1 6. Las etapas del proceso (datos literales de la taxonomía) · L6 §2.1 Faceta 1. Etapa — ¿en qué etapa del pipeline se aplica? (directo… · L22 §2.2 Faceta 2. Paso — ¿en qué paso de esa etapa? (Mapa del Spot) (L22… · L39 §2.3 P-01 — Faceta de flujo (incluida por decisión del usuario) (L244) · L61 §2.4.1 FL01 — niveles y pasos de flujo-spot.html (L267) · L132 §2.4.2 FL02 — Nivel 4 · subflujo atómico de génesis (flujo-spot.html)… · L228 §2.4.3 FL03 — pasos y subproceso de grupo de flujo-anclas.html (L432) · L266 Rutas documentadas del paquete CASOS (`rutas_documentadas.json`)
- `04a_etapas_explicacion.md`: 204 líneas: L1 6. Las etapas del proceso, explicadas · L11 6.1 Tres facetas describen dónde vive una regla en el proceso · L23 6.2 Los cuatro flujos · L25 FL01: producción de spot publicitario (`flujo-spot.html`, niveles 0 a… · L86 FL02: génesis sin referencia (`flujo-spot.html` L458–638, nivel 4, su… · L135 FL03: imágenes ancla (`flujo-anclas.html`, pasos 1 a 8, A0 a A12) · L166 FL04: activo directo sin preproducción (taxonomía L244–263) · L180 6.3 La secuencia operativa del sistema (TEMPLATES §2 y §8) · L196 6.4 La faceta F31: qué compuerta bloquea
- `05_documentos_del_corpus.md`: 3721 líneas: L1 5. Qué contiene cada documento del corpus · L24 5.1 Utilidad de cada documento · L170 5.2 Copias idénticas · L243 5.3 Los dos flujos HTML (2 documentos) · L245 flujos/flujo-anclas.html · L295 flujos/flujo-spot.html · L337 5.4 ai-production-director (3 documentos) · L339 skills/ai-production-director/SKILL.md · L384 skills/ai-production-director/references/creative-strategy.md · L404 skills/ai-production-director/references/production-package.md · L423 5.5 screenwriter (3 documentos) · L425 skills/screenwriter/SKILL.md · L456 skills/screenwriter/references/advanced-techniques.md · L478 skills/screenwriter/references/pipeline-integration.md · L505 5.6 visual-media (1 documentos) · L507 skills/visual-media/SKILL.md · L542 5.7 brand-lock-extractor (23 documentos) · L544 skills/brand-lock-extractor/SKILL.md · L577 skills/brand-lock-extractor/LICENSE · L595 skills/brand-lock-extractor/brand-packs/README.md · L613 skills/brand-lock-extractor/brand-packs/_template.md · L635 skills/brand-lock-extractor/brand-packs/examples/saas-clean.md · L657 skills/brand-lock-extractor/examples/brand-lock.md · L676 skills/brand-lock-extractor/examples/input-brief.md · L690 skills/brand-lock-extractor/references/extraction-rubric.md · L722 skills/brand-lock-extractor/templates/brand-lock.md.tpl · L740 skills/brand-lock-extractor/tools/README.md · L774 skills/brand-lock-extractor/tools/_shotkit.py · L793 skills/brand-lock-extractor/tools/_template.py · L809 skills/brand-lock-extractor/tools/check.sh · L834 skills/brand-lock-extractor/tools/copy-prompt.py · L857 skills/brand-lock-extractor/tools/shots-to-html.py · L888 skills/brand-lock-extractor/tools/validate_brand_lock.py · L919 skills/brand-lock-extractor/tools/validate_capabilities.py · L951 skills/brand-lock-extractor/tools/validate_critique.py · L976 skills/brand-lock-extractor/tools/validate_prompts.py · L1012 skills/brand-lock-extractor/tools/validate_provenance.py · L1052 skills/brand-lock-extractor/tools/validate_schemas.py · L1067 skills/brand-lock-extractor/tools/validate_shots.py · L1104 skills/brand-lock-extractor/tools/validate_skills.py · L1120 5.8 storyboard-architect (26 documentos) · L1122 skills/storyboard-architect/SKILL.md · L1165 skills/storyboard-architect/examples/30s-pain-proof-promise/brand-loc… · L1187 skills/storyboard-architect/examples/30s-pain-proof-promise/preview.h… · L1209 skills/storyboard-architect/examples/30s-pain-proof-promise/run.json · L1225 skills/storyboard-architect/examples/30s-pain-proof-promise/shots.json · L1248 skills/storyboard-architect/examples/30s-pain-proof-promise/storyboar… · L1266 skills/storyboard-architect/examples/30s-pain-proof-promise/text-over… · L1286 skills/storyboard-architect/examples/60s-founder-explainer/preview.ht… · L1309 skills/storyboard-architect/examples/60s-founder-explainer/run.json · L1325 skills/storyboard-architect/examples/60s-founder-explainer/shots.json · L1349 skills/storyboard-architect/examples/60s-founder-explainer/storyboard… · L1367 skills/storyboard-architect/examples/60s-founder-explainer/text-overl… · L1386 skills/storyboard-architect/examples/shotkit-explainer/brand-lock.sna… · L1409 skills/storyboard-architect/examples/shotkit-explainer/preview.html · L1430 skills/storyboard-architect/examples/shotkit-explainer/run.json · L1446 skills/storyboard-architect/examples/shotkit-explainer/shots.json · L1468 skills/storyboard-architect/examples/shotkit-explainer/storyboard.md · L1486 skills/storyboard-architect/examples/shotkit-explainer/text-overlays.… · L1507 skills/storyboard-architect/references/beat-frameworks.md · L1525 skills/storyboard-architect/references/on-screen-text.md · L1548 skills/storyboard-architect/references/shot-grammar.md · L1567 skills/storyboard-architect/references/timing-rules.md · L1585 skills/storyboard-architect/templates/run.schema.json · L1606 skills/storyboard-architect/templates/shots.schema.json · L1626 skills/storyboard-architect/templates/storyboard.md.tpl · L1644 skills/storyboard-architect/templates/text-overlays.schema.json · L1666 5.9 ai-video-storyboard (2 documentos) · L1668 skills/ai-video-storyboard/SKILL.md · L1700 skills/ai-video-storyboard/examples/tiktok-reel-30s-coffee.md · L1731 5.10 image (25 documentos) · L1733 skills/image/SKILL.md · L1761 skills/image/LICENSE · L1781 skills/image/NOTICE · L1795 skills/image/references/characters.md · L1814 skills/image/references/creative-direction.md · L1830 skills/image/references/dimensional.md · L1848 skills/image/references/editing.md · L1868 skills/image/references/golden-rules.md · L1895 skills/image/references/gpt-image.md · L1919 skills/image/references/models.md · L1937 skills/image/references/multi-panel.md · L1956 skills/image/references/nano-banana.md · L1993 skills/image/references/patterns/character-design.md · L2017 skills/image/references/patterns/ecommerce.md · L2041 skills/image/references/patterns/fashion-editorial.md · L2065 skills/image/references/patterns/food-beverage.md · L2089 skills/image/references/patterns/portrait-cinema.md · L2113 skills/image/references/patterns/poster-illustration.md · L2137 skills/image/references/patterns/ui-social.md · L2161 skills/image/references/prompt-framework.md · L2191 skills/image/references/slides.md · L2231 skills/image/references/storyboards.md · L2261 skills/image/references/structural.md · L2291 skills/image/references/text-rendering.md · L2321 skills/image/references/vision-decomposer.md · L2348 5.11 video (13 documentos) · L2350 skills/video/SKILL.md · L2372 skills/video/references/animatic-keyframes.md · L2393 skills/video/references/camera-lighting-vocabulary.md · L2416 skills/video/references/dramaturgy.md · L2443 skills/video/references/fixes-and-skeletons.md · L2475 skills/video/references/kling.md · L2499 skills/video/references/patterns-and-genres.md · L2514 skills/video/references/race-and-speed.md · L2536 skills/video/references/role-modes.md · L2572 skills/video/references/seedance-25.md · L2622 skills/video/references/seedance.md · L2668 skills/video/references/universal-rules.md · L2712 skills/video/references/veo.md · L2745 5.12 visual-prompt-forge (25 documentos) · L2747 skills/visual-prompt-forge/SKILL.md · L2791 skills/visual-prompt-forge/adapters/_capabilities.json · L2818 skills/visual-prompt-forge/adapters/capabilities.schema.json · L2842 skills/visual-prompt-forge/adapters/flux.md · L2874 skills/visual-prompt-forge/adapters/gpt-image.md · L2904 skills/visual-prompt-forge/adapters/hailuo.md · L2932 skills/visual-prompt-forge/adapters/ideogram.md · L2964 skills/visual-prompt-forge/adapters/kling.md · L2994 skills/visual-prompt-forge/adapters/midjourney.md · L3024 skills/visual-prompt-forge/adapters/nano-banana.md · L3056 skills/visual-prompt-forge/adapters/seedance.md · L3084 skills/visual-prompt-forge/adapters/seedream.md · L3116 skills/visual-prompt-forge/adapters/veo.md · L3146 skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md · L3168 skills/visual-prompt-forge/examples/one-shot-all-adapters/flux.txt · L3182 skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.t… · L3202 skills/visual-prompt-forge/examples/one-shot-all-adapters/ideogram.txt · L3216 skills/visual-prompt-forge/examples/one-shot-all-adapters/kling.txt · L3230 skills/visual-prompt-forge/examples/one-shot-all-adapters/midjourney.… · L3244 skills/visual-prompt-forge/examples/one-shot-all-adapters/nano-banana… · L3260 skills/visual-prompt-forge/examples/one-shot-all-adapters/seedream.txt · L3274 skills/visual-prompt-forge/references/consistency-locks.md · L3306 skills/visual-prompt-forge/references/failure-modes.md · L3334 skills/visual-prompt-forge/references/prompt-anatomy.md · L3360 skills/visual-prompt-forge/tools/validate_prompts.py · L3394 5.13 visual-asset-critic (14 documentos) · L3396 skills/visual-asset-critic/SKILL.md · L3433 skills/visual-asset-critic/examples/critique.accept.json · L3447 skills/visual-asset-critic/examples/critique.revise.json · L3461 skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot… · L3476 skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot… · L3491 skills/visual-asset-critic/examples/worked-run/critiques/round-2/shot… · L3506 skills/visual-asset-critic/examples/worked-run/preview.html · L3522 skills/visual-asset-critic/examples/worked-run/prompts/round-1/flux.t… · L3536 skills/visual-asset-critic/examples/worked-run/prompts/round-2/revise… · L3549 skills/visual-asset-critic/examples/worked-run/run.json · L3565 skills/visual-asset-critic/examples/worked-run/shots.json · L3579 skills/visual-asset-critic/examples/worked-run/text-overlays.json · L3593 skills/visual-asset-critic/references/critique-rubric.md · L3614 skills/visual-asset-critic/templates/critique.schema.json · L3632 5.14 storyboard-html-preview (4 documentos) · L3634 skills/storyboard-html-preview/SKILL.md · L3660 skills/storyboard-html-preview/templates/preview.html.tpl · L3679 skills/storyboard-html-preview/templates/print.css.tpl · L3698 skills/storyboard-html-preview/templates/styles.css.tpl
- `05_taxonomia_datos.md`: 3825 líneas: L1 8. La taxonomía completa: bloques, grupos, subgrupos, valores y térmi… · L6 §3. Bloque B — La pieza (L469) · L9 §3.1 Faceta 3. Ruta operativa — Video publicitario o Clip (DEC-000022… · L19 §3.2 Faceta 4. Tipo de pieza — ¿qué pieza se entrega? (L481) · L205 §3.3 Faceta 5. Temática o industria — ¿de qué sector o tema es la pie… · L259 §3.4 Faceta 6. Formato de salida — ¿en qué proporción se entrega? (sh… · L314 §3.5 Faceta 7. Género narrativo (rama video y guion) — ¿qué drama cue… · L338 §3.6 Faceta 8. Estructura de beats — ¿qué arco sigue la pieza complet… · L429 §3.7 Faceta 9. Patrón de montaje — ¿cómo se encadenan los planos de u… · L489 §3.8 P-04 — Subcategoría contextual «Lugar de publicación» (diseño ap… · L520 §4. Bloque C — El cuadro o el clip (L814) · L523 §4.1 Faceta 10. Modo de generación (solo etapas 5 y 6) — ¿génesis o a… · L725 §4.2 Faceta 11. Rol del ancla (solo etapa 5) — ¿para qué sirve la ima… · L757 §4.3 Faceta 12. Función del plano — ¿qué trabajo hace este plano en l… · L821 §4.4 Faceta 13. Tipo de acción — ¿qué pasa en el cuadro? (flujo-ancla… · L859 §4.5 Faceta 14. Régimen físico — ¿en qué medio físico ocurre? (regime… · L896 §4.6 Faceta 15. Sujeto — ¿qué clase de cosa se fija en la imagen? (fl… · L941 §4.7 Faceta 16. Espacio — ¿dónde ocurre? (L1090) · L959 §4.8 Faceta 17. Estilo visual — ¿qué look tiene? (flujo-anclas D4; im… · L1019 §4.9 Faceta 18. Técnica de representación — ¿con qué técnica se hace … · L1088 §4.10 Faceta 19. Número de sujetos — ¿cuántos sujetos individuales ha… · L1112 §4.11 Faceta 20. Identidad de las personas — ¿se deben reconocer? (L1… · L1135 §4.12 Faceta 21. Contacto físico entre personas — ¿se tocan? (L1226) · L1153 §4.13 Faceta 22. Tamaño del rostro — ¿cuánto ocupa del cuadro? (L1241) · L1172 §4.14 Faceta 23. Referencias adjuntas (solo etapas 5 y 6) — ¿qué refe… · L1276 §4.15 Faceta 24. Tamaño de plano — ¿cuánto del sujeto entra en cuadro… · L1318 §4.16 Faceta 25. Ángulo — ¿desde dónde mira la cámara? (flujo-anclas … · L1375 §4.17 Faceta 26. Movimiento de cámara (clip y contexto de ancla/keyfr… · L1463 §4.18 Faceta 27. Transición (clip y contexto de ancla/keyframe según … · L1540 §4.19 Faceta 28. Audio (clip y contexto de ancla/keyframe según F11 y… · L1583 §4.20 Faceta 29. Modelo (solo etapas 5 y 6) — ¿para qué modelo vale l… · L1663 §5. Bloque D — Atributos de la regla (L1581) · L1666 §5.1 Faceta 30. Qué regula — ¿sobre qué aspecto decide la regla? (L15… · L1693 §5.1.1 P-03 — tres valores nuevos (decisión de diseño aprobada) (L161… · L1704 §5.1.2 Vocabulario de términos por valor de la faceta 30 (L1620) · L1707 «estrategia y concepto» — 13 términos (L1622) · L1740 «estructura narrativa y diálogo» — 0 términos (L1640) · L1745 «dramaturgia» — 37 términos (L1644) · L1825 «encuadre y lente» — 52 términos (L1686) · L1932 «ángulo» — 0 términos (L1743) · L1937 «movimiento de cámara» — 0 términos (L1747) · L1942 «luz» — 68 términos (L1751) · L2077 «color, grade y textura» — 44 términos (L1824) · L2169 «composición» — 76 términos (L1873) · L2326 «identidad y consistencia» — 21 términos (L1954) · L2375 «anatomía, rostro y piel» — 35 términos (L1980) · L2444 «física y movimiento congelado» — 50 términos (L2020) · L2540 «texto en pantalla» — 36 términos (L2075) · L2619 «marca y logos» — 39 términos (L2116) · L2704 «estructura y sintaxis del prompt» — 46 términos (L2160) · L2803 «parámetros técnicos» — 70 términos (L2211) · L2947 «audio» — 18 términos (L2286) · L2990 «continuidad entre clips» — 11 términos (L2309) · L3019 «crítica y revisión» — 43 términos (L2325) · L3112 «trazabilidad y entrega» — 94 términos (L2373) · L3300 «materialidad y superficie» — 25 términos (L2472) · L3357 «puesta en escena y blocking» — 14 términos (L2502) · L3392 «animación» — 12 términos (L2521) · L3425 §5.2 Faceta 31. Condición para avanzar — ¿bloquea el paso a la siguie… · L3449 §5.3 P-05 — Faceta «Ámbito funcional» y campo «uso operativo» (decisi… · L3474 §5.4 P-02 — Autoridad como metadato (decisión de diseño aprobada) (L2… · L3479 §6. Bloque E — Metadatos de la regla (L2588) · L3482 §6.0 Campos (L2590) · L3507 §6.1 Valores de los campos tomados del borrador (L2614) · L3510 Campo «medio» — 5 valores (L2616) · L3529 Campo «unidad» — 5 valores (L2628) · L3548 Campo «tipo de enunciado» — 3 valores (L2640) · L3561 Campo «fuerza normativa» — 4 fuerzas y estado no normativo (L2648) · L3578 Campo «origen de evidencia» — 8 valores (incluye delta DOC01) (L2659) · L3600 Campo «evidencia de la afirmación fuente» — 4 descriptores documental… · L3615 Campo «adopción canónica» — 2 valores (L2682) · L3628 Campo «operador de condición» — 6 valores (L2691) · L3647 Campo «estado de evidencia» — 5 valores (L2702) · L3664 Campo «dependencia» — 2 valores (L2712) · L3675 §6.2 Precedencias establecidas por los textos originales (L2719) · L3699 §6.3 Autoridad declarada por las fuentes (tabla del director §1) (L27… · L3722 §6.4 P-07 — E6.5 conservado, Aurora excluida y fallback del original … · L3739 §6.5 P-06 — Paginación asignada (convención aprobada) (L2780) · L3744 Anexo 3 — Términos sin presencia en fuente autorizada (L4222) · L3810 Anexo histórico de tracks (no operativo; DEC-000022) (L4355)
- `05a_taxonomia_explicacion.md`: 137 líneas: L1 7. La jerarquía de la taxonomía, explicada · L5 7.1 Los cuatro niveles de la jerarquía · L25 7.2 Bloque A — Proceso: dónde vive la regla (L210–468) · L35 7.3 Bloque B — La pieza: qué se entrega (L469–813) · L48 7.4 Bloque C — El cuadro o el clip: qué hay en la imagen (L814–1580) · L77 7.5 Bloque D — Atributos de la regla (L1581–2587) · L88 7.6 Bloque E — Metadatos de la regla (L2588–2783) · L94 7.7 Cómo se relaciona un término con su valor · L117 7.8 Extensiones aprobadas por Eric fuera del documento 00688
- `06_tipos_de_texto.md`: 84 líneas: L1 9. Los tipos de texto y cómo se clasifican · L5 9.1 Dimensiones mecánicas: ya vienen en la base del corpus · L44 9.2 Dimensiones semánticas: se deciden al clasificar · L64 9.3 Cómo se combinan · L82 9.4 El contenido no normativo
- `07_universalidad.md`: 70 líneas: L1 10. La clasificación de universalidad · L5 10.1 Plano 1: en cada faceta, VALOR o UNIVERSAL (taxonomía §1.2) · L18 10.2 Plano 2: niveles de generalidad de una regla (PLAN_V5 §13.2, L62… · L35 10.3 Plano 3: el alcance del sistema para GPT Image 2 (decisiones 23 … · L57 10.4 Cómo se juntan los tres planos en la selección (taxonomía §7.4)
- `08_casos_datos.md`: 696 líneas: L1 11. La matriz de casos: cómo está estructurada (datos) · L5 11.7 Registros por clase y disposición · L26 11.8 Registros por faceta · L67 11.9 Los 360 valores autorizados, faceta por faceta, con su destino e… · L70 AMBITO · L88 F01 Etapa · L104 F02 Paso · L155 F03 Ruta operativa · L163 F04 Tipo de pieza · L196 F05 Temática o industria · L215 F06 Formato de salida · L232 F07 Género narrativo · L242 F08 Estructura de beats · L257 F09 Patrón de montaje · L269 F10 Modo de generación · L294 F11 Rol del ancla · L306 F12 Función del plano · L324 F13 Tipo de acción · L338 F14 Régimen físico · L353 F15 Sujeto · L366 F16 Espacio · L374 F17 Estilo visual · L390 F18 Técnica de representación · L403 F19 Número de sujetos · L413 F20 Identidad de las personas · L422 F21 Contacto físico entre personas · L430 F22 Tamaño del rostro · L439 F23 Referencias adjuntas · L459 F24 Tamaño de plano · L473 F25 Ángulo · L488 F26 Movimiento de cámara · L515 F27 Transición · L532 F28 Audio · L545 F29 Modelo · L567 F30 Qué regula · L597 F31 Condición para avanzar · L607 FLUJO · L617 PUBLICACION · L634 11.10 Formato de un caso (`case.schema.json`) · L655 11.11 Relaciones documentadas (473) · L668 11.12 Destinos de cada materia de F30 (`mapa_materias_f30_paths.json`)
- `08a_casos_explicacion.md`: 101 líneas: L1 11. La matriz de casos, explicada · L5 11.1 Qué es un caso · L23 11.2 De qué está hecha · L45 11.3 Cómo se arma un caso, de lo general a lo específico (README L42–… · L58 11.4 El formato de un caso (`case.schema.json`) · L84 11.5 Las diferencias que hay que preservar (README L24–28) · L93 11.6 Lo que el paquete declara que no hace
- `09_templates_datos.md`: 582 líneas: L1 12. Templates y contratos (datos literales del paquete TEMPLATES) · L5 12.9 Contratos por operación (`operation_contracts`) · L8 T-GENESIS · operación `genesis` · L24 T-REF-COMP · operación `composicion_referencias` · L40 T-ANCLA-REF · operación `ancla_referencia` · L56 T-ANCLA-FF · operación `ancla_ff` · L72 T-ANCLA-LF · operación `ancla_lf` · L88 T-EDIT · operación `edicion` · L104 T-STYLE · operación `transferencia_estilo` · L120 T-SKETCH · operación `boceto_a_final` · L136 12.10 Adaptadores de salida por modelo (`model_adapters`) · L139 GPT2-GEN · L160 GPT2-EDIT · L179 NB-PROSE · L195 NB-COMP · L212 NB-EDIT · L228 NB-COMPLEX · L259 FLUX-GEN · L275 MJ-GEN · L291 IDEOGRAM-COMPOSITED · L308 IDEOGRAM-TEXT · L325 SEEDREAM-GEN · L341 GPT15-GEN · L362 GPT-IMAGE-1-MIGRATION · L380 GPT-IMAGE-1-MINI-MIGRATION · L398 GPT15-EDIT · L415 12.11 Módulos condicionales (`conditional_modules`) · L425 12.12 Contratos por variante de modelo (`variant_contracts`) · L434 12.13 Contrato de vinculación regla → template (`binding_contract`) · L442 12.14 Destino de cada faceta (`REGISTRO_DESTINOS_TEMPLATE.json`) · L484 12.15 Mapa de campos (`FIELD_MAP.csv`)
- `09a_templates_explicacion.md`: 169 líneas: L1 12. Templates y contratos, explicados · L5 12.1 Qué es un contrato · L16 12.2 Autoridad (TEMPLATES §1) · L25 12.3 El brief T-BRIEF-IMG (TEMPLATES §3) · L72 12.4 Módulos condicionales (`CONTRATOS_OPERACION_MODELO.json`) · L83 12.5 Contratos por operación (TEMPLATES §5) · L98 12.6 La salida de GPT Image 2 (TEMPLATES §6 y PLAN_V5 §16.11) · L145 12.7 Orquestación, aceptación y traza (TEMPLATES §8 y §9) · L161 12.8 Destinos ya resueltos
- `10_metodologia_clasificacion.md`: 88 líneas: L1 13. La metodología de clasificación · L9 13.1 El contrato de clasificación por texto (taxonomía §1.12, 12 punt… · L24 13.2 Correspondencia con los templates (§1.13) · L32 13.3 El registro de una regla (taxonomía §7.1) · L44 13.4 La lógica de condiciones (§7.2) · L54 13.5 El procedimiento del PLAN_V5 · L86 13.6 Lo que el método no dice
- `11_veredicto.md`: 60 líneas: L1 14. Qué está construido y qué falta para el sistema · L5 14.1 Lo que ya existe · L21 14.2 Lo que falta · L32 14.3 Contradicciones que la lectura encontró dentro del corpus · L54 14.4 Lo que cuesta en cada turno de trabajo
- `CONSULTA.md`: 522 líneas: L1 Índice del repo (memoria del agente) · L18 1. Archivos del repo (101) · L173 2. Decisiones e instrucciones de Eric (archivo y línea) · L356 3. Pendientes (`PENDIENTES.md`) · L376 4. Corpus: 206 archivos, 141 contenidos distintos
- `INVENTARIO_SHA256.md`: 66 líneas: L1 Lo que queda en el repo (2026-10-27)
- `MAPA_ANEXO_DATOS.html`: 753,469 bytes
- `MAPA_ANEXO_DATOS.pdf`: 2,296,809 bytes
- `MAPA_DEL_REPO.html`: 1,637,906 bytes
- `MAPA_DEL_REPO.pdf`: 3,600,953 bytes

**`6_mapa/documentos/verificado/`**

- `lote1.md`: 501 líneas: L1 flujos/flujo-anclas.html · L51 flujos/flujo-spot.html · L92 skills/ai-production-director/SKILL.md · L137 skills/ai-production-director/references/creative-strategy.md · L157 skills/ai-production-director/references/production-package.md · L175 skills/ai-video-storyboard/SKILL.md · L207 skills/ai-video-storyboard/examples/tiktok-reel-30s-coffee.md · L237 skills/brand-lock-extractor/LICENSE · L255 skills/brand-lock-extractor/SKILL.md · L288 skills/brand-lock-extractor/brand-packs/README.md · L306 skills/brand-lock-extractor/brand-packs/_template.md · L328 skills/brand-lock-extractor/brand-packs/examples/saas-clean.md · L350 skills/brand-lock-extractor/examples/brand-lock.md · L369 skills/brand-lock-extractor/examples/input-brief.md · L383 skills/brand-lock-extractor/references/extraction-rubric.md · L415 skills/brand-lock-extractor/templates/brand-lock.md.tpl · L433 skills/brand-lock-extractor/tools/README.md · L467 skills/brand-lock-extractor/tools/_shotkit.py · L486 skills/brand-lock-extractor/tools/_template.py
- `lote2.md`: 532 líneas: L1 skills/brand-lock-extractor/tools/check.sh · L26 skills/brand-lock-extractor/tools/copy-prompt.py · L49 skills/brand-lock-extractor/tools/shots-to-html.py · L80 skills/brand-lock-extractor/tools/validate_brand_lock.py · L111 skills/brand-lock-extractor/tools/validate_capabilities.py · L143 skills/brand-lock-extractor/tools/validate_critique.py · L168 skills/brand-lock-extractor/tools/validate_prompts.py · L204 skills/brand-lock-extractor/tools/validate_provenance.py · L244 skills/brand-lock-extractor/tools/validate_schemas.py · L259 skills/brand-lock-extractor/tools/validate_shots.py · L296 skills/brand-lock-extractor/tools/validate_skills.py · L311 skills/image/LICENSE · L331 skills/image/NOTICE · L345 skills/image/SKILL.md · L373 skills/image/references/characters.md · L392 skills/image/references/creative-direction.md · L408 skills/image/references/dimensional.md · L426 skills/image/references/editing.md · L446 skills/image/references/golden-rules.md · L473 skills/image/references/gpt-image.md · L497 skills/image/references/models.md · L515 skills/image/references/multi-panel.md
- `lote3.md`: 470 líneas: L1 skills/image/references/nano-banana.md · L38 skills/image/references/patterns/character-design.md · L62 skills/image/references/patterns/ecommerce.md · L86 skills/image/references/patterns/fashion-editorial.md · L110 skills/image/references/patterns/food-beverage.md · L134 skills/image/references/patterns/portrait-cinema.md · L158 skills/image/references/patterns/poster-illustration.md · L182 skills/image/references/patterns/ui-social.md · L206 skills/image/references/prompt-framework.md · L236 skills/image/references/slides.md · L276 skills/image/references/storyboards.md · L306 skills/image/references/structural.md · L336 skills/image/references/text-rendering.md · L366 skills/image/references/vision-decomposer.md · L392 skills/screenwriter/SKILL.md · L423 skills/screenwriter/references/advanced-techniques.md · L445 skills/screenwriter/references/pipeline-integration.md
- `lote4.md`: 569 líneas: L1 skills/storyboard-architect/SKILL.md · L44 skills/storyboard-architect/examples/30s-pain-proof-promise/brand-loc… · L66 skills/storyboard-architect/examples/30s-pain-proof-promise/preview.h… · L88 skills/storyboard-architect/examples/30s-pain-proof-promise/run.json · L104 skills/storyboard-architect/examples/30s-pain-proof-promise/shots.json · L127 skills/storyboard-architect/examples/30s-pain-proof-promise/storyboar… · L145 skills/storyboard-architect/examples/30s-pain-proof-promise/text-over… · L165 skills/storyboard-architect/examples/60s-founder-explainer/preview.ht… · L188 skills/storyboard-architect/examples/60s-founder-explainer/run.json · L204 skills/storyboard-architect/examples/60s-founder-explainer/shots.json · L228 skills/storyboard-architect/examples/60s-founder-explainer/storyboard… · L246 skills/storyboard-architect/examples/60s-founder-explainer/text-overl… · L265 skills/storyboard-architect/examples/shotkit-explainer/brand-lock.sna… · L288 skills/storyboard-architect/examples/shotkit-explainer/preview.html · L309 skills/storyboard-architect/examples/shotkit-explainer/run.json · L325 skills/storyboard-architect/examples/shotkit-explainer/shots.json · L347 skills/storyboard-architect/examples/shotkit-explainer/storyboard.md · L365 skills/storyboard-architect/examples/shotkit-explainer/text-overlays.… · L386 skills/storyboard-architect/references/beat-frameworks.md · L404 skills/storyboard-architect/references/on-screen-text.md · L427 skills/storyboard-architect/references/shot-grammar.md · L446 skills/storyboard-architect/references/timing-rules.md · L464 skills/storyboard-architect/templates/run.schema.json · L485 skills/storyboard-architect/templates/shots.schema.json · L505 skills/storyboard-architect/templates/storyboard.md.tpl · L523 skills/storyboard-architect/templates/text-overlays.schema.json · L544 skills/storyboard-html-preview/SKILL.md
- `lote5.md`: 247 líneas: L1 skills/storyboard-html-preview/templates/preview.html.tpl · L20 skills/storyboard-html-preview/templates/print.css.tpl · L39 skills/storyboard-html-preview/templates/styles.css.tpl · L63 skills/video/SKILL.md · L85 skills/video/references/animatic-keyframes.md · L106 skills/video/references/camera-lighting-vocabulary.md · L129 skills/video/references/dramaturgy.md · L156 skills/video/references/fixes-and-skeletons.md · L188 skills/video/references/kling.md · L212 skills/video/references/patterns-and-genres.md · L227 skills/video/references/race-and-speed.md
- `lote6.md`: 521 líneas: L1 skills/video/references/role-modes.md · L37 skills/video/references/seedance-25.md · L87 skills/video/references/seedance.md · L133 skills/video/references/universal-rules.md · L177 skills/video/references/veo.md · L209 skills/visual-asset-critic/SKILL.md · L246 skills/visual-asset-critic/examples/critique.accept.json · L260 skills/visual-asset-critic/examples/critique.revise.json · L274 skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot… · L289 skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot… · L304 skills/visual-asset-critic/examples/worked-run/critiques/round-2/shot… · L319 skills/visual-asset-critic/examples/worked-run/preview.html · L335 skills/visual-asset-critic/examples/worked-run/prompts/round-1/flux.t… · L349 skills/visual-asset-critic/examples/worked-run/prompts/round-2/revise… · L362 skills/visual-asset-critic/examples/worked-run/run.json · L378 skills/visual-asset-critic/examples/worked-run/shots.json · L392 skills/visual-asset-critic/examples/worked-run/text-overlays.json · L406 skills/visual-asset-critic/references/critique-rubric.md · L427 skills/visual-asset-critic/templates/critique.schema.json · L444 skills/visual-media/SKILL.md · L478 skills/visual-prompt-forge/SKILL.md
- `lote7.md`: 602 líneas: L1 skills/visual-prompt-forge/adapters/_capabilities.json · L28 skills/visual-prompt-forge/adapters/capabilities.schema.json · L52 skills/visual-prompt-forge/adapters/flux.md · L84 skills/visual-prompt-forge/adapters/gpt-image.md · L114 skills/visual-prompt-forge/adapters/hailuo.md · L142 skills/visual-prompt-forge/adapters/ideogram.md · L174 skills/visual-prompt-forge/adapters/kling.md · L204 skills/visual-prompt-forge/adapters/midjourney.md · L234 skills/visual-prompt-forge/adapters/nano-banana.md · L266 skills/visual-prompt-forge/adapters/seedance.md · L294 skills/visual-prompt-forge/adapters/seedream.md · L326 skills/visual-prompt-forge/adapters/veo.md · L356 skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md · L378 skills/visual-prompt-forge/examples/one-shot-all-adapters/flux.txt · L392 skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.t… · L412 skills/visual-prompt-forge/examples/one-shot-all-adapters/ideogram.txt · L426 skills/visual-prompt-forge/examples/one-shot-all-adapters/kling.txt · L440 skills/visual-prompt-forge/examples/one-shot-all-adapters/midjourney.… · L454 skills/visual-prompt-forge/examples/one-shot-all-adapters/nano-banana… · L470 skills/visual-prompt-forge/examples/one-shot-all-adapters/seedream.txt · L484 skills/visual-prompt-forge/references/consistency-locks.md · L516 skills/visual-prompt-forge/references/failure-modes.md · L544 skills/visual-prompt-forge/references/prompt-anatomy.md · L570 skills/visual-prompt-forge/tools/validate_prompts.py

**`6_mapa/herramientas/`**

- `construir_pdf.py`: construir_pdf.py: une los capítulos del mapa en dos documentos y los imprime a PDF con Chromium (Playwright).
- `generar_datos.py`: generar_datos.py: escribe los capítulos de datos literales del mapa (corpus, etapas, taxonomía, casos, templates)
- `indice_consulta.py`: indice_consulta.py: escribe ../CONSULTA.md, el índice que el agente consulta antes de preguntar a Eric o de afirmar
- `muestra_auditoria.py`: muestra_auditoria.py: elige al azar 100 correcciones de los registros de verificación y les pega el texto
- `taxonomia.json`: 6 claves: titulo, nivel, linea, hijos, prosa, tablas
- `taxonomia_a_json.py`: taxonomia_a_json.py: extrae la jerarquía completa de la taxonomía 00688 (bloques → facetas → secciones → tablas)
- `unir_documentos.py`: unir_documentos.py: arma el capítulo 5 (cada documento del corpus explicado) a partir de documentos/lote1..7.md.
- `utilidad_corpus.json`: 141 claves: flujos/flujo-anclas.html, flujos/flujo-spot.html, skills/ai-production-director/SKILL.md, skills/ai-production-director/reference…, skills/ai-production-director/reference…, skills/ai-video-storyboard/SKILL.md, skills/ai-video-storyboard/examples/tik…, skills/brand-lock-extractor/LICENSE, skills/brand-lock-extractor/SKILL.md, skills/brand-lock-extractor/brand-packs…, skills/brand-lock-extractor/brand-packs…, skills/brand-lock-extractor/brand-packs… …
- `verificar_capitulos_datos.py`: verificar_capitulos_datos.py: comprueba de forma mecánica que los capítulos de datos del mapa copian bien sus fuentes.
- `verificar_documentos.py`: verificar_documentos.py: comprobaciones deterministas de las 141 explicaciones del capítulo 5 contra el corpus.

**`6_mapa/lecturas/`**

- `zip_v3.4.0_documentos_de_hooks.md`: 46 líneas: L1 Lectura: documentos del zip original que explican los hooks (2026-10-… · L13 `repo/.claude/hooks/README.md` · L30 `START_HERE.md` · L40 `INDEX.md` (L1–120 de 318)

**`./`**

- `CLAUDE.md`: 42 líneas: L1 Instrucciones de proyecto · L3 Alcance y vocabulario de los prompts · L8 Antes de decir que algo no existe · L16 Consultar el mapa antes de preguntar o de dar algo por faltante (inst… · L25 Riesgos, pendientes y avance de etapa (decisión de Eric, 2026-10-29) · L35 Toda lectura deja registro en el repo
- `LEEME.md`: 25 líneas: L1 AI Production Director: sistema que genera prompts · L6 Dónde está cada cosa
- `PENDIENTES.md`: 43 líneas: L1 Pendientes por etapa · L10 Etapa 1 — Mapa del repositorio (registro de la lectura) · L24 Etapa 2 — Preparación de la clasificación (antes de clasificar el cor… · L37 Línea aparte — Familias de régimen físico · L41 Etapas siguientes (no empiezan hasta cerrar la etapa 2)

## 2. Decisiones e instrucciones de Eric (archivo y línea)


**`CLAUDE.md`**

- L3 **Alcance y vocabulario de los prompts**
- L8 **Antes de decir que algo no existe**
- L16 **Consultar el mapa antes de preguntar o de dar algo por faltante (instrucción de Eric, 202…**
- L25 **Riesgos, pendientes y avance de etapa (decisión de Eric, 2026-10-29)**
- L35 **Toda lectura deja registro en el repo**

**`.claude/rules/DECISIONES.md`**

- L8 | 1 | Dónde viven las familias de régimen físico, el vocabulario ampliado del linter y su copia parcheada | En el repo, `.claude/rules/regimenes/` y …
- L9 | 2 | Alcance del linter aurora | Copia parcheada en el repo. El conteo de palabras nunca bloquea: es advertencia con el presupuesto de la plataforma…
- L10 | 3 | Bloque de identidad con referencia de persona adjunta | Por rol de la referencia. Keyframe de inicio o fin en imagen a video: no re-describir. …
- L11 | 4 | Taxonomía de la base de reglas | Caso ampliado con LUGAR, EDIF, ANIMAL, OBJ, MULTITUD, ENSAMBLE. Tarea por subproceso, E0.1 a POST.2 | Las 852 …
- L12 | 5 | Tarjeta de ancla en la base | Las nueve dimensiones D1 a D9 como facetas multivalor de cada regla | Una pasada de clasificación adicional sobre…
- L13 | 6 | Modelo de embeddings | `intfloat/multilingual-e5-large` local, sin API key; la tabla admite añadir OpenAI después | Cubre inglés, español y rus…
- L14 | 7 | Familias de régimen físico | Nueve familias con esqueleto de nueve secciones: agua en superficie, ruptura de superficie, subacuático, objeto ba…
- L15 | 8 | Cómo entran las inferencias | Con etiqueta `[A PRUEBA]`; investigación de campo en foros y tutoriales para confirmar o refutar cada una; un eje…
- L16 | 9 | Quién clasifica sin NotebookLM | NotebookLM eliminado del flujo por completo. Clasificador de dos capas, determinista por ruta y regex más simi…
- L18 **Principios que salieron de la sesión y quedan como reglas de trabajo**

**`5_decisiones/01021_DECISIONES_APLICADAS_20261011_224300.md`**

- L15 **Decisión explícita de las 16:56:54.532502 UTC**
- L19 **Verificación documental y límites de capacidad**
- L23 **Cierre del trabajo de candidatas**

**`5_decisiones/01022_DELTA_DECISIONES_CONSOLIDADO_20261011_224300.md`**

- L3 **Estado y autorización**
- L11 **Cambios del contrato**
- L28 **Jerarquías y estados**
- L34 **DEC-000026 y DEC-000027: evidencia disponible y límite**
- L42 **Registro histórico recibido**
- L46 **DEC-000001**
- L53 **DEC-000002**
- L59 **DEC-000003**
- L65 **DEC-000004**
- L71 **DEC-000005**
- L78 **DEC-000006**
- L84 **DEC-000007**
- L90 **DEC-000008**
- L96 **DEC-000009**
- L102 **DEC-000010**
- L108 **DEC-000011**
- L114 **DEC-000012**
- L121 **DEC-000013**
- L127 **DEC-000014**
- L133 **DEC-000015**
- L139 **DEC-000016**
- L145 **DEC-000017**
- L151 **DEC-000018**
- L157 **DEC-000019**
- L164 **DEC-000020**
- L171 **DEC-000021**
- L178 **DEC-000022**
- L184 **DEC-000023**
- L192 **DEC-000024**
- L198 **DEC-000025**
- L205 **Decisión adicional explícita: anclas/keyframes, 2026-10-11 16:56:54.532502 UTC**
- L216 **Cierre de verificación documental, sin inventar rendimiento actual**
- L224 **Resultado de aplicación de la decisión de anclas/keyframes**

**`5_decisiones/01062_registro_decisiones_DOC01.md`**

- L4 **DEC-000001**
- L8 **DEC-000002**
- L11 **DEC-000003**
- L14 **DEC-000004**
- L17 **DEC-000005**
- L21 **DEC-000006**
- L24 **DEC-000007**
- L27 **DEC-000008**
- L30 **DEC-000009**
- L33 **DEC-000010**
- L36 **DEC-000011**
- L39 **DEC-000012**
- L43 **DEC-000013**
- L46 **DEC-000014**
- L49 **DEC-000015**
- L52 **DEC-000016**
- L55 **DEC-000017**
- L58 **DEC-000018**
- L61 **DEC-000019**
- L65 **DEC-000020**
- L69 **DEC-000021**
- L73 **DEC-000022**
- L76 **DEC-000023**
- L81 **DEC-000024**
- L84 **DEC-000025**

**`5_decisiones/DECISIONES_ERIC_20261023.md`**

- L3 1. Alcance de esta fase: solo textos de imagen y GPT Image 2. Universo: los 1,511 textos de `skills/image/**`
- L7 2. La catalogación previa (2026-10-11, 1,887 registros) y la catalogación provisional del 2026-10-23 no se
- L9 3. Ningún texto queda como pendiente, propuesta, duda, NO APLICA ni equivalente. Lo que no cabe en la taxonomía se
- L11 4. Extensiones de la taxonomía aprobadas (se registran aparte de la taxonomía original):
- L29 5. Toda etiqueta usada en la catalogación debe coincidir al 100% con la taxonomía original (o con una extensión
- L31 6. Las pruebas se hacen solo con GPT Image 2; otros modelos se añaden después.
- L32 7. quality en GPT Image 2 (consulta C1 del piloto): la elige el usuario; «medium como punto de partida» y «empieza con
- L34 8. Biblioteca de prompts efectivos (precisada por Eric el 2026-10-23):

**`5_decisiones/DECISIONES_ERIC_20261024.md`**

- L7 1. **Alcance del universo de textos** (amplía la decisión 1 de `DECISIONES_ERIC_20261023.md` y responde D2 del plan v3
- L19 2. «SI EXISTE LA CLASIFICACIÓN EN LA TAXONOMÍA ES PORQUE LA REGLA EXISTE EN EL CORPUS».
- L20 3. «EL SOLO HACER LA GENERACIÓN EN DOS PASOS NO ES SUFICIENTE, HAY VARIAS REGLAS MUY ESPECÍFICAS SOBRE EL LENTE Y EL
- L23 4. Método de prueba aprobado el 2026-10-24: bloque armado por casos (universo completo → filtro por caso → controles

**`5_decisiones/DECISIONES_ERIC_20261026.md`**

- L5 1. **Cuando un texto da una cifra que no es la de GPT Image 2, vale la cifra que el corpus da para GPT Image 2**, y el
- L14 2. «No estás aprobado para asumir nada, siempre lo verificas»: toda afirmación sobre un texto se comprueba leyendo el
- L16 3. «Siempre que hay una supuesta contradicción o incoherencia tienes que leer exhaustivamente los textos
- L19 4. **Interfaces de GPT Image 2: OpenAI API y fal.ai** (respuesta a la decisión 1 de 6). Manda
- L24 5. **F20 con una sola persona que debe seguir reconocible: «todas»** (decisión 2 de 6). Base: TRM-0175 (taxonomía L1220,
- L27 6. **Extensión F24 + «objeto entero»** (decisión 3 de 6): un objeto completo como sujeto del cuadro. Los 8 valores
- L30 7. **F05 de B1 y B4 deja de ser lista vacía** (decisión 4 de 6; la lista vacía viola taxonomía §1.12.8): B1 (pescadora en
- L33 8. **Interfaz de generación de la prueba: App de ChatGPT para escritorio** (corregido 2026-10-27). Palabras de Eric
- L42 9. **Muestra de auditoría** (2026-10-27): Eric revisa al azar el 10 % del total de reglas marcadas «no aplica» en cada
- L45 10. **Repetición antes de auditar** (2026-10-27): si una imagen sale mal, se genera el mismo prompt por lo menos dos veces
- L50 11. **Longitud del prompt** (2026-10-27): ya estaba decidida (`.claude/rules/DECISIONES.md` decisión 2; T-BRIEF-IMG L355).
- L54 12. **Alcance de la prueba: solo imagen con aspecto de foto real** (2026-10-27). Palabras de Eric: «solo quiero que se
- L62 13. **vision-decomposer y transferencia de estilo son cosas distintas** (2026-10-27). Palabras de Eric: «porque si son
- L67 14. **Caso de descripción de imagen** (2026-10-27, responde la pregunta 2 de `v3/revision/04_preguntas_eric.md`).
- L75 15. **Sin veredicto d en el diagnóstico** (2026-10-27, responde la pregunta 3). Palabras de Eric: «no hay límite de
- L81 16. **Lista de casos de la prueba** (2026-10-27, responde la pregunta 1 de `v3/revision/04_preguntas_eric.md`). Eric
- L90 17. **Boceto o plano a final: 5 casos** (2026-10-27). Eric eligió un caso por cada plantilla fotográfica, igual que en
- L99 18. **Dos textos mal excluidos entran al universo** (2026-10-27). Eric respondió «Sí, meterlos» a la pregunta «¿Meto
- L108 19. **La decisión por sección se mantiene** (2026-10-27, 00:28–00:37 UTC; registrada tarde, el 2026-10-27). Se decidió en

**`5_decisiones/DECISIONES_ERIC_20261027_30.md`**

- L7 1. **Objetivo y reparto** (2026-10-27): «EL SISTEMA NO GENERA IMÁGENES, GENERA PROMPTS Y YO HAGO LAS IMÁGENES». El
- L9 2. **Qué se queda en el repo** (2026-10-27): «LOS ARCHIVOS QUE SE QUEDAN SON LOS QUE NECESITAS PARA EL SISTEMA ENTERO,
- L11 3. **No repetir preguntas ya respondidas** (2026-10-27): no volver a preguntar lo que Eric ya contestó en conversaciones
- L13 4. **Planes** (2026-10-27): un plan tiene como máximo 10 pasos, extremadamente claros y sin riesgos sin mitigar.
- L14 5. **Riesgos y pendientes** (2026-10-29): registrado en CLAUDE.md, sección «Riesgos, pendientes y avance de etapa».
- L15 6. **Procedimiento para terminar** (2026-10-29, palabras de Eric resumidas punto por punto):
- L16 1. Una estructura clara de la aplicación que va a gobernar y ejecutar el sistema, con un flujo claro de la
- L18 2. Los textos se clasifican primero por tipo de texto. La primera clasificación es si tienen o no impacto en la
- L23 3. Para todos los textos debe existir de qué documento viene y su taxonomía dentro de ese documento: los
- L25 4. Una tabla con el ID de cada texto en la primera columna y, en las siguientes, todas las columnas que
- L27 5. La primera ronda de catálogo es mecánica: usa el documento y los encabezados a los que pertenece el texto.
- L28 6. La segunda ronda revisa los textos, una categoría por vez, no todas al mismo tiempo.
- L29 7. La matriz lleva X si aplica para esa categoría y 0 si no; al final todas las celdas deben estar llenas.
- L33 7. **Auditoría con prueba** (2026-10-29): Eric pidió auditar 100 textos corregidos y traer prueba de que están
- L36 8. **Nada sin verificar** (2026-10-30): «no me des una aseveración que no has verificado personalmente». Toda
- L39 9. **Para qué es el mapa** (2026-10-30): el mapa es para que el agente lo consulte y no pierda la memoria de las
- L43 10. **PLAN_V5 fuera** (2026-10-30): «no hace sentido que nada dependa de un plan fracasado; ya te dije que necesitamos otro plan». Se
- L46 11. **Borrar lo que el sistema no usa, de forma irrecuperable** (2026-10-30): «cuando digo bórralos no es para que los
- L51 12. **Repo, PLAN_V5, hooks y mapa** (2026-10-30, segunda parte):

**`5_decisiones/DECISIONES_ERIC_RESCATADAS_20261027.md`**

- L5 **De `apd/demo/LEEME.md` (líneas 39–40; app apd, 2026-09-28)**
- L10 **De `taller/recursos/` (movidos, no copiados, a `taller/catalogo/fuentes_eric_20261021/`)**

**`5_decisiones/DECISIONES_repo_20260925.md`**

- L8 | 1 | Dónde viven las familias de régimen físico, el vocabulario ampliado del linter y su copia parcheada | En el repo, `.claude/rules/regimenes/` y …
- L9 | 2 | Alcance del linter aurora | Copia parcheada en el repo. El conteo de palabras nunca bloquea: es advertencia con el presupuesto de la plataforma…
- L10 | 3 | Bloque de identidad con referencia de persona adjunta | Por rol de la referencia. Keyframe de inicio o fin en imagen a video: no re-describir. …
- L11 | 4 | Taxonomía de la base de reglas | Caso ampliado con LUGAR, EDIF, ANIMAL, OBJ, MULTITUD, ENSAMBLE. Tarea por subproceso, E0.1 a POST.2 | Las 852 …
- L12 | 5 | Tarjeta de ancla en la base | Las nueve dimensiones D1 a D9 como facetas multivalor de cada regla | Una pasada de clasificación adicional sobre…
- L13 | 6 | Modelo de embeddings | `intfloat/multilingual-e5-large` local, sin API key; la tabla admite añadir OpenAI después | Cubre inglés, español y rus…
- L14 | 7 | Familias de régimen físico | Nueve familias con esqueleto de nueve secciones: agua en superficie, ruptura de superficie, subacuático, objeto ba…
- L15 | 8 | Cómo entran las inferencias | Con etiqueta `[A PRUEBA]`; investigación de campo en foros y tutoriales para confirmar o refutar cada una; un eje…
- L16 | 9 | Quién clasifica sin NotebookLM | NotebookLM eliminado del flujo por completo. Clasificador de dos capas, determinista por ruta y regex más simi…
- L18 **Principios que salieron de la sesión y quedan como reglas de trabajo**

**`5_decisiones/directivas_20261021/directivas_taller.json`**

- `ERIC-IDIOMA-PROMPT-INGLES`: «en ingles esto es siemore»
- `ERIC-BLOQUES-1-2-NO-TOPE`: «La expectativa de una o dos reglas por bloque sirve para evaluar los filtros, no para imponer un tope ni excluir reglas válidas.»

**`5_decisiones/directivas_20261021/user_directives.json`**

- `ERIC-B1-PHOTOREALISTIC`: «Prohibido el término photorealistic en prompts»
- `ERIC-DELEGATION-TERMS`: «Se perdió la prohibición explícita del usuario de photorealistic y fotorealista.»

## 3. Pendientes (`PENDIENTES.md`)

- L14 **P-01** (Agente; Cerrado 2026-10-29: 141 de 141 verificadas por un…): Verificar las 141 explicaciones del capítulo 5 contra su original
- L15 **P-02** (Agente; Cerrado 2026-10-29: criterio objetivo aplicado; c…): La utilidad ALTA, MEDIA o NULA era el juicio de cada lector
- L16 **P-03** (Agente; Cerrado 2026-10-30: muestras con semilla 20261030…): Tercera lectura sellada del 10 % (muestra sellada)
- L17 **P-04** (Eric; Sin objeto 2026-10-30: Eric ordenó borrar `produc…): `CLAUDE.md` dice que `aprobados-20261024/briefs.json` tiene «seis casos»; tiene cinco (B1–B5). B6 está en `b6-corregido…
- L18 **P-16** (Agente; el costo lo aprueba Eric; Abierto): Verificar los capítulos del mapa que escribió el agente (1–4 y 6–14) contra sus fuentes, con el mismo método que las 14…
- L19 **P-17** (Eric; Cerrado 2026-10-30: Eric ordenó restaurarlos todo…): Hooks del paquete original, borrados el 2026-10-30 sobre una evaluación del agente que estuvo mal hecha («el sistema no…
- L20 **P-18** (Agente lee y registra; Eric decide si a…; Abierto): El zip original trae 750 archivos: 214 en `skills/` y 536 fuera (contados el 2026-10-30). Entre los de fuera hay un sis…
- L21 **P-19** (Eric; Cerrado 2026-10-30: extraídos literal a `4_diseno…): Los niveles de generalidad y la jerarquía de lectura solo estaban completos en PLAN_V5 §13.1–13.2
- L22 **P-05** (Eric; Después de P-01 a P-03): Aprobación del mapa
- L28 **P-06** (Agente, con aprobación de Eric; Abierto): Incorporar las extensiones de la taxonomía del 23 y del 26 de octubre (F32–F35 y valores nuevos en F04, F05, F06, F10, …
- L29 **P-07** (Agente propone, Eric aprueba; Abierto): Mecanismo para clasificar sin perder el estado (el diseño no lo especifica, capítulo 13)
- L30 **P-08** (Eric; Abierto): `text-rendering.md`: Nano Banana con más de 100 idiomas (INV-003296); en la sección «Multilingual / Localization», sin …
- L31 **P-09** (Eric; Abierto): `screenwriter/SKILL.md`: 8–15 escenas (INV-003470) frente a 6–10 para 5 minutos (INV-003574)
- L32 **P-10** (Eric; Abierto): Seedream y el texto: `_capabilities.json` frente a su adaptador
- L33 **P-11** (Eric; Abierto): `validate_prompts.py`: la regla del tercio lleva `or True` (INV-012830)
- L34 **P-12** (Eric; Abierto): `patterns-and-genres.md` (7 o 8 géneros) y `shot-grammar.md` (`rack`)
- L35 **P-13** (Eric; Abierto): Tope de costo de la clasificación

## 4. Corpus: 206 archivos, 141 contenidos distintos

Utilidad: ALTA, dice qué va o no va en un prompt; MEDIA, regula el proceso; NULA, ninguna de las dos.

| Documento | Textos | Ids | Utilidad | Copias idénticas |
|---|---:|---|---|---|
| `flujos/flujo-anclas.html` | 293 | INV-000001–INV-000293 | ALTA | — |
| `flujos/flujo-spot.html` | 321 | INV-000294–INV-000614 | ALTA | — |
| `skills/ai-production-director/SKILL.md` | 102 | INV-000615–INV-000716 | ALTA | — |
| `skills/ai-production-director/references/creative-strategy.md` | 34 | INV-000717–INV-000750 | MEDIA | — |
| `skills/ai-production-director/references/production-package.md` | 26 | INV-000751–INV-000776 | ALTA | — |
| `skills/ai-video-storyboard/SKILL.md` | 89 | INV-000777–INV-000865 | ALTA | — |
| `skills/ai-video-storyboard/examples/tiktok-reel-30s-coffee.md` | 76 | INV-000866–INV-000941 | ALTA | — |
| `skills/brand-lock-extractor/LICENSE` | 33 | INV-000942–INV-000974 | NULA | `skills/storyboard-architect/LICENSE`, `skills/storyboard-html-preview/LICENSE`, `skills/visual-asset-critic/LICENSE`, `skills/visual-prompt-forge/LICENSE` |
| `skills/brand-lock-extractor/SKILL.md` | 71 | INV-000975–INV-001045 | MEDIA | — |
| `skills/brand-lock-extractor/brand-packs/README.md` | 28 | INV-001046–INV-001073 | MEDIA | `skills/storyboard-architect/brand-packs/README.md` |
| `skills/brand-lock-extractor/brand-packs/_template.md` | 53 | INV-001074–INV-001126 | ALTA | `skills/storyboard-architect/brand-packs/_template.md` |
| `skills/brand-lock-extractor/brand-packs/examples/saas-clean.md` | 56 | INV-001127–INV-001182 | ALTA | — |
| `skills/brand-lock-extractor/examples/brand-lock.md` | 50 | INV-001183–INV-001232 | ALTA | — |
| `skills/brand-lock-extractor/examples/input-brief.md` | 14 | INV-001233–INV-001246 | ALTA | — |
| `skills/brand-lock-extractor/references/extraction-rubric.md` | 47 | INV-001247–INV-001293 | ALTA | — |
| `skills/brand-lock-extractor/templates/brand-lock.md.tpl` | 40 | INV-001294–INV-001333 | ALTA | — |
| `skills/brand-lock-extractor/tools/README.md` | 81 | INV-001334–INV-001414 | ALTA | `skills/storyboard-architect/tools/README.md`, `skills/storyboard-html-preview/tools/README.md`, `skills/visual-asset-critic/tools/README.md`, `skills/visual-prompt-forge/tools/README.md` |
| `skills/brand-lock-extractor/tools/_shotkit.py` | 41 | INV-001415–INV-001455 | MEDIA | `skills/storyboard-architect/tools/_shotkit.py`, `skills/storyboard-html-preview/tools/_shotkit.py`, `skills/visual-asset-critic/tools/_shotkit.py`, `skills/visual-prompt-forge/tools/_shotkit.py` |
| `skills/brand-lock-extractor/tools/_template.py` | 16 | INV-001456–INV-001471 | NULA | `skills/storyboard-architect/tools/_template.py`, `skills/storyboard-html-preview/tools/_template.py`, `skills/visual-asset-critic/tools/_template.py`, `skills/visual-prompt-forge/tools/_template.py` |
| `skills/brand-lock-extractor/tools/check.sh` | 17 | INV-001472–INV-001488 | MEDIA | `skills/storyboard-architect/tools/check.sh`, `skills/storyboard-html-preview/tools/check.sh`, `skills/visual-asset-critic/tools/check.sh`, `skills/visual-prompt-forge/tools/check.sh` |
| `skills/brand-lock-extractor/tools/copy-prompt.py` | 40 | INV-001489–INV-001528 | MEDIA | `skills/storyboard-architect/tools/copy-prompt.py`, `skills/storyboard-html-preview/tools/copy-prompt.py`, `skills/visual-asset-critic/tools/copy-prompt.py`, `skills/visual-prompt-forge/tools/copy-prompt.py` |
| `skills/brand-lock-extractor/tools/shots-to-html.py` | 53 | INV-001529–INV-001581 | MEDIA | `skills/storyboard-architect/tools/shots-to-html.py`, `skills/storyboard-html-preview/tools/shots-to-html.py`, `skills/visual-asset-critic/tools/shots-to-html.py`, `skills/visual-prompt-forge/tools/shots-to-html.py` |
| `skills/brand-lock-extractor/tools/validate_brand_lock.py` | 46 | INV-001582–INV-001627 | MEDIA | `skills/storyboard-architect/tools/validate_brand_lock.py`, `skills/storyboard-html-preview/tools/validate_brand_lock.py`, `skills/visual-asset-critic/tools/validate_brand_lock.py`, `skills/visual-prompt-forge/tools/validate_brand_lock.py` |
| `skills/brand-lock-extractor/tools/validate_capabilities.py` | 40 | INV-001628–INV-001667 | ALTA | `skills/storyboard-architect/tools/validate_capabilities.py`, `skills/storyboard-html-preview/tools/validate_capabilities.py`, `skills/visual-asset-critic/tools/validate_capabilities.py`, `skills/visual-prompt-forge/tools/validate_capabilities.py` |
| `skills/brand-lock-extractor/tools/validate_critique.py` | 44 | INV-001668–INV-001711 | MEDIA | `skills/storyboard-architect/tools/validate_critique.py`, `skills/storyboard-html-preview/tools/validate_critique.py`, `skills/visual-asset-critic/tools/validate_critique.py`, `skills/visual-prompt-forge/tools/validate_critique.py` |
| `skills/brand-lock-extractor/tools/validate_prompts.py` | 46 | INV-001712–INV-001757 | ALTA | `skills/storyboard-architect/tools/validate_prompts.py`, `skills/storyboard-html-preview/tools/validate_prompts.py`, `skills/visual-asset-critic/tools/validate_prompts.py` |
| `skills/brand-lock-extractor/tools/validate_provenance.py` | 60 | INV-001758–INV-001817 | MEDIA | `skills/storyboard-architect/tools/validate_provenance.py`, `skills/storyboard-html-preview/tools/validate_provenance.py`, `skills/visual-asset-critic/tools/validate_provenance.py`, `skills/visual-prompt-forge/tools/validate_provenance.py` |
| `skills/brand-lock-extractor/tools/validate_schemas.py` | 15 | INV-001818–INV-001832 | MEDIA | `skills/storyboard-architect/tools/validate_schemas.py`, `skills/storyboard-html-preview/tools/validate_schemas.py`, `skills/visual-asset-critic/tools/validate_schemas.py`, `skills/visual-prompt-forge/tools/validate_schemas.py` |
| `skills/brand-lock-extractor/tools/validate_shots.py` | 60 | INV-001833–INV-001892 | MEDIA | `skills/storyboard-architect/tools/validate_shots.py`, `skills/storyboard-html-preview/tools/validate_shots.py`, `skills/visual-asset-critic/tools/validate_shots.py`, `skills/visual-prompt-forge/tools/validate_shots.py` |
| `skills/brand-lock-extractor/tools/validate_skills.py` | 19 | INV-001893–INV-001911 | MEDIA | `skills/storyboard-architect/tools/validate_skills.py`, `skills/storyboard-html-preview/tools/validate_skills.py`, `skills/visual-asset-critic/tools/validate_skills.py`, `skills/visual-prompt-forge/tools/validate_skills.py` |
| `skills/image/LICENSE` | 82 | INV-001912–INV-001993 | NULA | `skills/video/LICENSE` |
| `skills/image/NOTICE` | 4 | INV-001994–INV-001997 | NULA | `skills/video/NOTICE` |
| `skills/image/SKILL.md` | 55 | INV-001998–INV-002052 | ALTA | — |
| `skills/image/references/characters.md` | 31 | INV-002053–INV-002083 | ALTA | — |
| `skills/image/references/creative-direction.md` | 83 | INV-002084–INV-002166 | ALTA | — |
| `skills/image/references/dimensional.md` | 27 | INV-002167–INV-002193 | ALTA | — |
| `skills/image/references/editing.md` | 44 | INV-002194–INV-002237 | ALTA | — |
| `skills/image/references/golden-rules.md` | 93 | INV-002238–INV-002330 | ALTA | — |
| `skills/image/references/gpt-image.md` | 84 | INV-002331–INV-002414 | ALTA | — |
| `skills/image/references/models.md` | 58 | INV-002415–INV-002472 | ALTA | — |
| `skills/image/references/multi-panel.md` | 124 | INV-002473–INV-002596 | ALTA | — |
| `skills/image/references/nano-banana.md` | 78 | INV-002597–INV-002674 | ALTA | — |
| `skills/image/references/patterns/character-design.md` | 43 | INV-002675–INV-002717 | ALTA | — |
| `skills/image/references/patterns/ecommerce.md` | 42 | INV-002718–INV-002759 | ALTA | — |
| `skills/image/references/patterns/fashion-editorial.md` | 41 | INV-002760–INV-002800 | ALTA | — |
| `skills/image/references/patterns/food-beverage.md` | 60 | INV-002801–INV-002860 | ALTA | — |
| `skills/image/references/patterns/portrait-cinema.md` | 41 | INV-002861–INV-002901 | ALTA | — |
| `skills/image/references/patterns/poster-illustration.md` | 43 | INV-002902–INV-002944 | ALTA | — |
| `skills/image/references/patterns/ui-social.md` | 43 | INV-002945–INV-002987 | ALTA | — |
| `skills/image/references/prompt-framework.md` | 100 | INV-002988–INV-003087 | ALTA | — |
| `skills/image/references/slides.md` | 137 | INV-003088–INV-003224 | ALTA | — |
| `skills/image/references/storyboards.md` | 30 | INV-003225–INV-003254 | ALTA | — |
| `skills/image/references/structural.md` | 39 | INV-003255–INV-003293 | ALTA | — |
| `skills/image/references/text-rendering.md` | 99 | INV-003294–INV-003392 | ALTA | — |
| `skills/image/references/vision-decomposer.md` | 67 | INV-003393–INV-003459 | ALTA | — |
| `skills/screenwriter/SKILL.md` | 160 | INV-003460–INV-003619 | MEDIA | — |
| `skills/screenwriter/references/advanced-techniques.md` | 89 | INV-003620–INV-003708 | MEDIA | — |
| `skills/screenwriter/references/pipeline-integration.md` | 143 | INV-003709–INV-003851 | MEDIA | — |
| `skills/storyboard-architect/SKILL.md` | 141 | INV-003885–INV-004025 | ALTA | — |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md` | 53 | INV-004107–INV-004159 | ALTA | `skills/storyboard-architect/examples/60s-founder-explainer/brand-lock.snapshot.md`, `skills/visual-asset-critic/examples/worked-run/brand-lock.snapshot.md` |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/preview.html` | 178 | INV-004160–INV-004337 | ALTA | — |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/run.json` | 24 | INV-004338–INV-004361 | MEDIA | — |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/shots.json` | 130 | INV-004362–INV-004491 | ALTA | — |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/storyboard.md` | 75 | INV-004492–INV-004566 | ALTA | — |
| `skills/storyboard-architect/examples/30s-pain-proof-promise/text-overlays.json` | 77 | INV-004567–INV-004643 | MEDIA | — |
| `skills/storyboard-architect/examples/60s-founder-explainer/preview.html` | 204 | INV-004697–INV-004900 | ALTA | — |
| `skills/storyboard-architect/examples/60s-founder-explainer/run.json` | 24 | INV-004901–INV-004924 | MEDIA | — |
| `skills/storyboard-architect/examples/60s-founder-explainer/shots.json` | 146 | INV-004925–INV-005070 | ALTA | — |
| `skills/storyboard-architect/examples/60s-founder-explainer/storyboard.md` | 50 | INV-005071–INV-005120 | ALTA | — |
| `skills/storyboard-architect/examples/60s-founder-explainer/text-overlays.json` | 65 | INV-005121–INV-005185 | MEDIA | — |
| `skills/storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md` | 64 | INV-005186–INV-005249 | ALTA | — |
| `skills/storyboard-architect/examples/shotkit-explainer/preview.html` | 163 | INV-005250–INV-005412 | ALTA | — |
| `skills/storyboard-architect/examples/shotkit-explainer/run.json` | 24 | INV-005413–INV-005436 | MEDIA | — |
| `skills/storyboard-architect/examples/shotkit-explainer/shots.json` | 114 | INV-005437–INV-005550 | ALTA | — |
| `skills/storyboard-architect/examples/shotkit-explainer/storyboard.md` | 31 | INV-005551–INV-005581 | ALTA | — |
| `skills/storyboard-architect/examples/shotkit-explainer/text-overlays.json` | 89 | INV-005582–INV-005670 | MEDIA | — |
| `skills/storyboard-architect/references/beat-frameworks.md` | 43 | INV-005671–INV-005713 | MEDIA | — |
| `skills/storyboard-architect/references/on-screen-text.md` | 58 | INV-005714–INV-005771 | ALTA | — |
| `skills/storyboard-architect/references/shot-grammar.md` | 61 | INV-005772–INV-005832 | ALTA | — |
| `skills/storyboard-architect/references/timing-rules.md` | 49 | INV-005833–INV-005881 | MEDIA | — |
| `skills/storyboard-architect/templates/run.schema.json` | 154 | INV-005882–INV-006035 | MEDIA | — |
| `skills/storyboard-architect/templates/shots.schema.json` | 200 | INV-006036–INV-006235 | MEDIA | — |
| `skills/storyboard-architect/templates/storyboard.md.tpl` | 50 | INV-006236–INV-006285 | MEDIA | — |
| `skills/storyboard-architect/templates/text-overlays.schema.json` | 107 | INV-006286–INV-006392 | ALTA | — |
| `skills/storyboard-html-preview/SKILL.md` | 113 | INV-007004–INV-007116 | MEDIA | — |
| `skills/storyboard-html-preview/templates/preview.html.tpl` | 18 | INV-007117–INV-007134 | MEDIA | — |
| `skills/storyboard-html-preview/templates/print.css.tpl` | 31 | INV-007135–INV-007165 | MEDIA | — |
| `skills/storyboard-html-preview/templates/styles.css.tpl` | 70 | INV-007166–INV-007235 | MEDIA | — |
| `skills/video/SKILL.md` | 63 | INV-007900–INV-007962 | ALTA | — |
| `skills/video/references/animatic-keyframes.md` | 135 | INV-007963–INV-008097 | ALTA | — |
| `skills/video/references/camera-lighting-vocabulary.md` | 189 | INV-008098–INV-008286 | ALTA | — |
| `skills/video/references/dramaturgy.md` | 235 | INV-008287–INV-008521 | ALTA | — |
| `skills/video/references/fixes-and-skeletons.md` | 144 | INV-008522–INV-008665 | ALTA | — |
| `skills/video/references/kling.md` | 179 | INV-008666–INV-008844 | ALTA | — |
| `skills/video/references/patterns-and-genres.md` | 105 | INV-008845–INV-008949 | ALTA | — |
| `skills/video/references/race-and-speed.md` | 163 | INV-008950–INV-009112 | ALTA | — |
| `skills/video/references/role-modes.md` | 86 | INV-009113–INV-009198 | ALTA | — |
| `skills/video/references/seedance-25.md` | 190 | INV-009199–INV-009388 | ALTA | — |
| `skills/video/references/seedance.md` | 148 | INV-009389–INV-009536 | ALTA | — |
| `skills/video/references/universal-rules.md` | 110 | INV-009537–INV-009646 | ALTA | — |
| `skills/video/references/veo.md` | 85 | INV-009647–INV-009731 | ALTA | — |
| `skills/visual-asset-critic/SKILL.md` | 127 | INV-009765–INV-009891 | ALTA | — |
| `skills/visual-asset-critic/examples/critique.accept.json` | 23 | INV-009892–INV-009914 | MEDIA | — |
| `skills/visual-asset-critic/examples/critique.revise.json` | 36 | INV-009915–INV-009950 | ALTA | — |
| `skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot_01.critique.json` | 33 | INV-010004–INV-010036 | MEDIA | — |
| `skills/visual-asset-critic/examples/worked-run/critiques/round-1/shot_02.critique.json` | 38 | INV-010037–INV-010074 | ALTA | — |
| `skills/visual-asset-critic/examples/worked-run/critiques/round-2/shot_02.critique.json` | 24 | INV-010075–INV-010098 | MEDIA | — |
| `skills/visual-asset-critic/examples/worked-run/preview.html` | 66 | INV-010099–INV-010164 | MEDIA | — |
| `skills/visual-asset-critic/examples/worked-run/prompts/round-1/flux.txt` | 3 | INV-010165–INV-010167 | ALTA | — |
| `skills/visual-asset-critic/examples/worked-run/prompts/round-2/revised-flux.txt` | 2 | INV-010168–INV-010169 | ALTA | — |
| `skills/visual-asset-critic/examples/worked-run/run.json` | 64 | INV-010170–INV-010233 | MEDIA | — |
| `skills/visual-asset-critic/examples/worked-run/shots.json` | 50 | INV-010234–INV-010283 | MEDIA | — |
| `skills/visual-asset-critic/examples/worked-run/text-overlays.json` | 29 | INV-010284–INV-010312 | MEDIA | — |
| `skills/visual-asset-critic/references/critique-rubric.md` | 75 | INV-010313–INV-010387 | ALTA | — |
| `skills/visual-asset-critic/templates/critique.schema.json` | 183 | INV-010388–INV-010570 | MEDIA | — |
| `skills/visual-media/SKILL.md` | 83 | INV-011149–INV-011231 | MEDIA | — |
| `skills/visual-prompt-forge/SKILL.md` | 161 | INV-011265–INV-011425 | ALTA | — |
| `skills/visual-prompt-forge/adapters/_capabilities.json` | 167 | INV-011426–INV-011592 | ALTA | — |
| `skills/visual-prompt-forge/adapters/capabilities.schema.json` | 62 | INV-011593–INV-011654 | MEDIA | — |
| `skills/visual-prompt-forge/adapters/flux.md` | 63 | INV-011655–INV-011717 | ALTA | — |
| `skills/visual-prompt-forge/adapters/gpt-image.md` | 45 | INV-011718–INV-011762 | ALTA | — |
| `skills/visual-prompt-forge/adapters/hailuo.md` | 44 | INV-011763–INV-011806 | ALTA | — |
| `skills/visual-prompt-forge/adapters/ideogram.md` | 47 | INV-011807–INV-011853 | ALTA | — |
| `skills/visual-prompt-forge/adapters/kling.md` | 53 | INV-011854–INV-011906 | ALTA | — |
| `skills/visual-prompt-forge/adapters/midjourney.md` | 57 | INV-011907–INV-011963 | ALTA | — |
| `skills/visual-prompt-forge/adapters/nano-banana.md` | 57 | INV-011964–INV-012020 | ALTA | — |
| `skills/visual-prompt-forge/adapters/seedance.md` | 49 | INV-012021–INV-012069 | ALTA | — |
| `skills/visual-prompt-forge/adapters/seedream.md` | 53 | INV-012070–INV-012122 | ALTA | — |
| `skills/visual-prompt-forge/adapters/veo.md` | 48 | INV-012123–INV-012170 | ALTA | — |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` | 29 | INV-012171–INV-012199 | ALTA | — |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/flux.txt` | 2 | INV-012200–INV-012201 | ALTA | — |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt` | 4 | INV-012202–INV-012205 | ALTA | — |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/ideogram.txt` | 2 | INV-012206–INV-012207 | ALTA | — |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/kling.txt` | 2 | INV-012208–INV-012209 | ALTA | — |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/midjourney.txt` | 2 | INV-012210–INV-012211 | ALTA | — |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/nano-banana.txt` | 3 | INV-012212–INV-012214 | ALTA | — |
| `skills/visual-prompt-forge/examples/one-shot-all-adapters/seedream.txt` | 2 | INV-012215–INV-012216 | ALTA | — |
| `skills/visual-prompt-forge/references/consistency-locks.md` | 60 | INV-012217–INV-012276 | ALTA | — |
| `skills/visual-prompt-forge/references/failure-modes.md` | 92 | INV-012277–INV-012368 | ALTA | — |
| `skills/visual-prompt-forge/references/prompt-anatomy.md` | 57 | INV-012369–INV-012425 | ALTA | — |
| `skills/visual-prompt-forge/tools/validate_prompts.py` | 48 | INV-012804–INV-012851 | ALTA | — |
