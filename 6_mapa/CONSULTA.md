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
| Taxonomía, templates y casos | §1, carpetas `3_taxonomia/` y `4_diseno/` |


## 1. Archivos del repo (85)


**`.claude/rules/`**

- `DECISIONES.md`: sus decisiones, en §2

**`./`**

- `.gitignore`: 19 bytes

**`1_originales/`**

- `AI_Production_Director_v3.4.0.zip`: 719 archivos: repo 465, skills 214, (raíz) 30, project_knowledge_pack 8, original_source 2. El corpus (§4) sale de `skills/`, salvo `aurora-prompt-linter`, `produccion-visual-sw30` y 3 PNG (taxonomía §0.1). Lo demás está en revisión con Eric (PENDIENTES P-18)
- `SHA256SUMS`: 266 bytes
- `flujo-anclas.html`: 121,395 bytes
- `flujo-spot.html`: 161,157 bytes

**`2_corpus/`**

- `BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite`: tablas: textos (13003 filas)
- `CORPUS_LITERAL_COMPLETO_13005.jsonl`: 13003 líneas JSON

**`3_taxonomia/`**

- `00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md`: 4366 líneas: L1 TAXONOMÍA CONSOLIDADA — CORRECCIÓN DE CLASIFICACIÓN 2026-10-19 · L5 Contrato vigente de esta consolidación · L25 Seleccionabilidad obligatoria — corrección 2026-10-11 22:36 UTC · L37 0. Corpus autorizado, inventario y conteos de control · L39 0.1 Corpus autorizado · L77 0.2 Inventario literal (primer paso del orden de trabajo) · L101 0.3 Inventario por capa de la taxonomía · L121 0.4 Conciliación de los 1 369 términos · L135 0.5 Respaldo de las definiciones en las fuentes autorizadas (punto 16) · L146 0.6 Disposición de contenido y límite de activación (C12) · L157 1. Principios · L184 1.12 Contrato obligatorio de lectura y clasificación por texto — 2026… · L202 1.13 Correspondencia exhaustiva entre taxonomía y templates — 2026-10… · L210 2. Bloque A — Proceso · L212 2.1 Faceta 1. Etapa — ¿en qué etapa del pipeline se aplica? (director… · L228 2.2 Faceta 2. Paso — ¿en qué paso de esa etapa? (Mapa del Spot) · L244 2.3 P-01 — Faceta de flujo (incluida por decisión del usuario) · L265 2.4 Estructura de los flujos según las fuentes (extracción mecánica d… · L267 2.4.1 FL01 — niveles y pasos de flujo-spot.html · L337 2.4.2 FL02 — Nivel 4 · subflujo atómico de génesis (flujo-spot.html) · L432 2.4.3 FL03 — pasos y subproceso de grupo de flujo-anclas.html · L469 3. Bloque B — La pieza · L471 3.1 Faceta 3. Ruta operativa — Video publicitario o Clip (DEC-000022;… · L481 3.2 Faceta 4. Tipo de pieza — ¿qué pieza se entrega? · L595 3.3 Faceta 5. Temática o industria — ¿de qué sector o tema es la piez… · L634 3.4 Faceta 6. Formato de salida — ¿en qué proporción se entrega? (sho… · L674 3.5 Faceta 7. Género narrativo (rama video y guion) — ¿qué drama cuen… · L693 3.6 Faceta 8. Estructura de beats — ¿qué arco sigue la pieza completa… · L748 3.7 Faceta 9. Patrón de montaje — ¿cómo se encadenan los planos de un… · L786 3.8 P-04 — Subcategoría contextual «Lugar de publicación» (diseño apr… · L814 4. Bloque C — El cuadro o el clip · L816 4.1 Faceta 10. Modo de generación (solo etapas 5 y 6) — ¿génesis o an… · L934 4.2 Faceta 11. Rol del ancla (solo etapa 5) — ¿para qué sirve la imag… · L959 4.3 Faceta 12. Función del plano — ¿qué trabajo hace este plano en la… · L1002 4.4 Faceta 13. Tipo de acción — ¿qué pasa en el cuadro? (flujo-anclas… · L1030 4.5 Faceta 14. Régimen físico — ¿en qué medio físico ocurre? · L1059 4.6 Faceta 15. Sujeto — ¿qué clase de cosa se fija en la imagen? (flu… · L1090 4.7 Faceta 16. Espacio — ¿dónde ocurre? · L1105 4.8 Faceta 17. Estilo visual — ¿qué look tiene? (flujo-anclas D4; ima… · L1145 4.9 Faceta 18. Técnica de representación — ¿con qué técnica se hace l… · L1188 4.10 Faceta 19. Número de sujetos — ¿cuántos sujetos individuales hay… · L1207 4.11 Faceta 20. Identidad de las personas — ¿se deben reconocer? · L1226 4.12 Faceta 21. Contacto físico entre personas — ¿se tocan? · L1241 4.13 Faceta 22. Tamaño del rostro — ¿cuánto ocupa del cuadro? · L1258 4.14 Faceta 23. Referencias adjuntas (solo etapas 5 y 6) — ¿qué refer… · L1324 4.15 Faceta 24. Tamaño de plano — ¿cuánto del sujeto entra en cuadro?… · L1354 4.16 Faceta 25. Ángulo — ¿desde dónde mira la cámara? (flujo-anclas D… · L1392 4.17 Faceta 26. Movimiento de cámara (clip y contexto de ancla/keyfra… · L1453 4.18 Faceta 27. Transición (clip y contexto de ancla/keyframe según F… · L1503 4.19 Faceta 28. Audio (clip y contexto de ancla/keyframe según F11 y … · L1534 4.20 Faceta 29. Modelo (solo etapas 5 y 6) — ¿para qué modelo vale la… · L1581 5. Bloque D — Atributos de la regla · L1583 5.1 Faceta 30. Qué regula — ¿sobre qué aspecto decide la regla? · L1610 5.1.1 P-03 — tres valores nuevos (decisión de diseño aprobada) · L1620 5.1.2 Vocabulario de términos por valor de la faceta 30 · L1622 «estrategia y concepto» — 13 términos · L1640 «estructura narrativa y diálogo» — 0 términos · L1644 «dramaturgia» — 37 términos · L1686 «encuadre y lente» — 52 términos · L1743 «ángulo» — 0 términos · L1747 «movimiento de cámara» — 0 términos · L1751 «luz» — 68 términos · L1824 «color, grade y textura» — 44 términos · L1873 «composición» — 76 términos · L1954 «identidad y consistencia» — 21 términos · L1980 «anatomía, rostro y piel» — 35 términos · L2020 «física y movimiento congelado» — 50 términos · L2075 «texto en pantalla» — 36 términos · L2116 «marca y logos» — 39 términos · L2160 «estructura y sintaxis del prompt» — 46 términos · L2211 «parámetros técnicos» — 70 términos · L2286 «audio» — 18 términos · L2309 «continuidad entre clips» — 11 términos · L2325 «crítica y revisión» — 43 términos · L2373 «trazabilidad y entrega» — 94 términos · L2472 «materialidad y superficie» — 25 términos · L2502 «puesta en escena y blocking» — 14 términos · L2521 «animación» — 12 términos · L2540 5.2 Faceta 31. Condición para avanzar — ¿bloquea el paso a la siguien… · L2560 5.3 P-05 — Faceta «Ámbito funcional» y campo «uso operativo» (decisió… · L2584 5.4 P-02 — Autoridad como metadato (decisión de diseño aprobada) · L2588 6. Bloque E — Metadatos de la regla · L2590 6.0 Campos · L2614 6.1 Valores de los campos tomados del borrador · L2616 Campo «medio» — 5 valores · L2628 Campo «unidad» — 5 valores · L2640 Campo «tipo de enunciado» — 3 valores · L2648 Campo «fuerza normativa» — 4 fuerzas y estado no normativo · L2659 Campo «origen de evidencia» — 8 valores (incluye delta DOC01) · L2673 Campo «evidencia de la afirmación fuente» — 4 descriptores documental… · L2682 Campo «adopción canónica» — 2 valores · L2691 Campo «operador de condición» — 6 valores · L2702 Campo «estado de evidencia» — 5 valores · L2712 Campo «dependencia» — 2 valores · L2719 6.2 Precedencias establecidas por los textos originales · L2742 6.3 Autoridad declarada por las fuentes (tabla del director §1) · L2764 6.4 P-07 — E6.5 conservado, Aurora excluida y fallback del original · L2780 6.5 P-06 — Paginación asignada (convención aprobada) · L2784 7. Registro, condiciones, brief y consulta · L2786 7.1 Registro mínimo de una regla · L2798 7.2 Lógica de condiciones · L2802 7.3 Brief: exploración frente a selección definitiva · L2806 7.4 Consulta: una sola salida por regla · L2818 Anexo 1 — HISTÓRICO: cambios v3 → v4 por sección e ID · L2846 Anexo 2 — Conciliación término por término (1 369 filas) · L4222 Anexo 3 — Términos sin presencia en fuente autorizada · L4287 Anexo 4 — HISTÓRICO: decisiones de la edición base C18; complementada… · L4304 Anexo 5 — HISTÓRICO: comprobaciones de C11–C17 y sus límites · L4312 Anexo 6 — Correspondencias con la taxonomía anterior (no son fuentes … · L4328 Anexo de conciliación de citas · L4334 Actualización estructural P-04 · L4338 Gate final de aceptación bidireccional · L4352 Historial: canonización de la edición base C18 (2026-10-03) · L4356 Anexo histórico de tracks (no operativo; DEC-000022)
- `TAXONOMIA_IMAGENES_PROPUESTA.md`: 1864 líneas: L1 Taxonomía de clasificación para imágenes — PROPUESTA para aprobación … · L6 Nivel 1 · Qué hace el texto con el prompt · L10 1.1 ¿Impacta la redacción? · L17 1.2 Si impacta: efecto · L30 1.3 Si impacta: cómo entra al prompt · L41 1.4 Si no impacta: qué es · L54 Nivel 2 · Precatalogación por encabezado · L58 F29 · Modelo · L136 F35 · Migración de versión de modelo · L142 F10 · Operación (modo de generación) · L261 F11 · Rol del ancla · L273 F23 · Referencias adjuntas · L289 F04 · Tipo de pieza · L356 F05 · Temática o industria · L367 F06 · Formato de salida · L377 F03 · Ruta operativa · L387 F07 · Género narrativo · L397 F08 · Estructura de beats · L425 F09 · Patrón de montaje · L431 F12 · Función del plano · L445 F14 · Régimen físico · L451 F15 · Sujeto · L460 F17 · Estilo visual · L476 F18 · Técnica de representación · L487 F24 · Tamaño de plano · L494 F25 · Ángulo · L500 F26 · Movimiento de cámara · L507 F27 · Transición · L514 F28 · Audio · L520 F30 · Qué regula · L999 F31 · Condición para avanzar · L1013 F01 · Etapa · L1093 FLUJO · Flujo · L1103 BIB · Biblioteca de plantillas de look · L1125 EJ · Ejemplos (efecto probable: da un ejemplo o una plantilla) · L1174 Q · Probablemente no impacta (qué es) · L1266 Sin categoría por encabezado · L1283 Nivel 3 · Caso de uso, de lo general a lo específico · L1288 3.1 Qué se hace · L1290 FLUJO · Flujo · L1299 F10 · Modo de generación · L1319 F29 · Modelo · L1335 F35 · Migración de versión de modelo · L1342 F04 · Tipo de pieza · L1364 PUBLICACION · Lugar de publicación (subcategoría de F04) · L1380 F06 · Formato de salida · L1397 F34 · Resolución · L1405 3.2 Contexto · L1407 F03 · Ruta operativa · L1414 F05 · Temática o industria · L1435 F07 · Género narrativo · L1444 F08 · Estructura de beats · L1458 F09 · Patrón de montaje · L1469 F12 · Función del plano · L1486 F11 · Rol del ancla · L1497 F23 · Referencias adjuntas · L1516 3.3 Qué hay en el cuadro · L1518 F15 · Sujeto · L1530 F19 · Número de sujetos · L1539 F20 · Identidad de las personas · L1547 F21 · Contacto físico entre personas · L1554 F13 · Tipo de acción · L1567 F14 · Régimen físico · L1581 F16 · Espacio · L1588 F32 · Texto en la imagen · L1596 F33 · Complejidad de escena · L1603 3.4 Cómo se ve · L1605 F17 · Estilo visual · L1623 F18 · Técnica de representación · L1635 3.5 Cámara · L1637 F24 · Tamaño de plano · L1651 F25 · Ángulo · L1665 F22 · Tamaño del rostro · L1673 F26 · Movimiento de cámara · L1699 F27 · Transición · L1715 F28 · Audio · L1727 3.6 Detalles del caso por materia · L1748 Nivel 4 · Atributos de la regla · L1751 F01 · Etapa · L1766 F02 · Paso · L1780 F30 · Qué regula · L1809 F31 · Condición para avanzar · L1818 AMBITO · Ámbito funcional · L1831 USO OPERATIVO · Uso operativo (por aplicación de la regla) · L1842 METADATOS · Campos de la regla

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
- `rutas_documentadas.json`: lista de 183 elementos
- `validar.py`: sin docstring

**`4_diseno/copias_identicas/casos_templates/`**

- `CONTRATO_IMAGEN_ORQUESTACION.schema.json`: copia idéntica de `4_diseno/templates/CONTRATO_IMAGEN_ORQUESTACION.schema.json`
- `REGISTRO_DESTINOS_TEMPLATE.json`: copia idéntica de `4_diseno/templates/REGISTRO_DESTINOS_TEMPLATE.json`

**`4_diseno/copias_identicas/decisiones/`**

- `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`: copia idéntica de `4_diseno/templates/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`

**`4_diseno/`**

- `jerarquia_de_lectura.md`: 21 líneas: L1 Jerarquía de lectura de la clasificación · L4 Texto · L18 Dónde más aparece, en parte
- `niveles_de_generalidad.md`: 20 líneas: L1 Niveles de generalidad de una regla (universalidad) · L4 Texto · L16 Dónde más aparece, en parte

**`4_diseno/templates/`**

- `CONTRATOS_OPERACION_MODELO.json`: 8 claves: version, operation_contracts, model_adapters, binding_contract, variant_contracts, parameter_serialization, limitations, conditional_modules
- `CONTRATO_IMAGEN_ORQUESTACION.schema.json`: 7 claves: $schema, $id, title, type, properties, additionalProperties, required
- `FIELD_MAP.csv`: 94 filas; columnas: item_id,destino_path,tipo_destino,schema
- `FUENTES_CONTRATOS.json`: 3 claves: taxonomia, fuentes, alcance
- `MANIFIESTO.json`: 2 claves: version, files
- `REGISTRO_DESTINOS_TEMPLATE.json`: 7 claves: version, schema_file, facet_destinations, aliases, fields, f30_destinations, scope_destinations
- `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`: 387 líneas: L1 Templates revisados de entrada y salida: imagen y orquestación · L5 1. Autoridad y alcance · L9 2. Secuencia obligatoria de uso · L21 3. Ficha rellenables T-BRIEF-IMG · L138 4. Tarjeta de ancla D1–D9 · L142 5. Contratos por operación · L144 T-GENESIS · L149 T-REF-COMP · L154 T-ANCLA-REF · L159 T-ANCLA-FF · L164 T-ANCLA-LF · L169 T-EDIT · L174 T-STYLE · L179 T-SKETCH · L184 6. Templates de salida por modelo · L187 GPT2-GEN · L201 GPT2-EDIT · L213 NB-PROSE · L223 NB-COMP · L234 NB-EDIT · L244 NB-COMPLEX · L268 FLUX-GEN · L278 MJ-GEN · L288 IDEOGRAM-COMPOSITED · L298 IDEOGRAM-TEXT · L308 SEEDREAM-GEN · L318 GPT15-GEN · L329 GPT-IMAGE-1-MIGRATION · L340 GPT-IMAGE-1-MINI-MIGRATION · L351 Reglas de serialización de variantes · L357 7. Salida común rellenables · L371 8. T-ORQ: contrato ejecutable de eventos y gates · L375 9. T-ACEPTACIÓN y T-TRAZA · L379 10. Cobertura y validación · L383 11. Fuentes y atribución · L386 12. Obligatoriedad revisada por módulo

**`4_diseno/validadores/`**

- `README.md`: 214 líneas: L1 Gates de producción — enforcement fuera del modelo · L11 Qué hace cada gate · L21 El gate que importa más que los demás · L86 Verificación · L99 Cobertura real — el número que ningún gate verde reemplaza · L113 Medición · L135 Cómo se usa el ledger · L151 Dos contradicciones encontradas en los skills · L169 Estado de verificación — honesto · L197 Requisito · L206 Límites reales
- `gate_dramaturgy.py`: Stop hook: blocks delivery of visual prompts that carry banned vocabulary.
- `gate_image.py`: Stop hook: enforces the image skill's own golden rules on delivered prompts.
- `gate_microgate.py`: Stop hook: enforce the 3-line micro-gate header on any visual delivery.
- `gate_shots.py`: PostToolUse hook: runs the shotkit validator whenever shots.json is written.
- `inject_rules.py`: UserPromptSubmit hook: put the mandatory rules in context before Claude chooses.
- `prompt_detect.py`: Decide si un bloque cercado es la entrega de un prompt visual.
- `settings.json`: 1 claves: hooks

**`5_decisiones/`**

- `01021_DECISIONES_APLICADAS_20261011_224300.md`: sus decisiones, en §2
- `01022_DELTA_DECISIONES_CONSOLIDADO_20261011_224300.md`: sus decisiones, en §2
- `01062_registro_decisiones_DOC01.md`: sus decisiones, en §2
- `DECISIONES_ERIC_20261023.md`: sus decisiones, en §2
- `DECISIONES_ERIC_20261024.md`: sus decisiones, en §2
- `DECISIONES_ERIC_20261026.md`: sus decisiones, en §2
- `DECISIONES_ERIC_20261027_30.md`: sus decisiones, en §2
- `DECISIONES_ERIC_RESCATADAS_20261027.md`: sus decisiones, en §2
- `DECISIONES_repo_20260925.md`: sus decisiones, en §2

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

- `CONSULTA.md`: 379 líneas: L1 Índice del repo (memoria del agente) · L17 1. Archivos del repo (85) · L168 2. Decisiones e instrucciones de Eric (archivo y línea) · L350 3. Pendientes (`PENDIENTES.md`) · L364 4. Corpus: 206 archivos, 141 contenidos distintos, 13,003 textos
- `INVENTARIO_SHA256.md`: 88 líneas: L1 Inventario del repo con sha256

**`6_mapa/herramientas/`**

- `indice_consulta.py`: indice_consulta.py: escribe ../CONSULTA.md, el índice que el agente consulta antes de preguntar a Eric o de afirmar
- `utilidad_corpus.json`: 141 claves: flujos/flujo-anclas.html, flujos/flujo-spot.html, skills/ai-production-director/SKILL.md, skills/ai-production-director/reference…, skills/ai-production-director/reference…, skills/ai-video-storyboard/SKILL.md, skills/ai-video-storyboard/examples/tik…, skills/brand-lock-extractor/LICENSE, skills/brand-lock-extractor/SKILL.md, skills/brand-lock-extractor/brand-packs…, skills/brand-lock-extractor/brand-packs…, skills/brand-lock-extractor/brand-packs… …

**`6_mapa/lecturas/`**

- `catalogo_casos_de_uso.md`: 17 líneas: L1 Lectura: catálogo de casos de uso (2026-10-30)
- `prueba_24_textos_imagen.md`: 5 líneas: L1 Lectura: 24 textos del universo de imagen (2026-10-30)
- `taxonomia_00688.md`: 16 líneas: L1 Lectura: taxonomía 00688 (2026-10-30)

**`7_auditorias_y_verificaciones/casos/`**

- `verificacion.json`: 9 claves: rutas_comprobadas_en_schema, validacion_estructural, registros, TRM, IDs_duplicados, destinos_vacios, facetas, asociaciones_REG, compatibilidad_semantica

**`7_auditorias_y_verificaciones/`**

- `decision4_casos_en_taxonomia.md`: 21 líneas: L1 Lectura: los casos de la decisión 4 (25-sep) en la taxonomía 00688 (2…
- `prueba_taxonomia_imagenes_20261030.md`: 83 líneas: L1 Investigación y prueba del nivel 1 de la taxonomía para imágenes (202… · L6 1. Investigación · L30 2. Prueba con 24 textos reales · L65 3. Lo que decidió la prueba · L81 4. Corrección del 2026-10-30 (orden de Eric)
- `revision_estructura_taxonomia_y_casos_20261030.md`: 260 líneas: L1 Revisión de la estructura: taxonomía y catálogo de casos de uso (2026… · L6 Qué se revisó · L20 1. Qué hay hoy dentro de la taxonomía · L36 2. Veredicto por sección · L75 3. Comprobaciones de las 2,796 filas de término · L113 4. Hallazgos en el catálogo de casos (`4_diseno/casos/`) · L153 5. Recomendación final · L157 5.1 La taxonomía (`3_taxonomia/`) · L197 5.2 El catálogo (`4_diseno/casos/`) · L211 5.3 Qué cambia y qué no · L226 5.4 Cómo se verifica · L241 6. Pendientes que resuelve Eric antes de reestructurar · L253 7. Hallado de paso, fuera de la taxonomía y del catálogo
- `taxonomia_que_sale_20261030.md`: 134 líneas: L1 Taxonomía: lo que se queda, lo que sale y sirve, lo que sale y no sir… · L10 Lo que se queda (esto es la taxonomía) · L43 Lista 1. Sale de la taxonomía y sirve · L58 Lista 2. Sale de la taxonomía y no sirve (para revisar y borrar) · L88 Coincidencia entre el catálogo de casos y la taxonomía (verificado el… · L119 Forma más barata y rápida de hacerlo
- `taxonomia_sin_estados_de_exclusion_20261030.md`: 47 líneas: L1 Verificación: la taxonomía prohíbe y no usa estados que dejen una reg… · L7 Dónde lo prohíbe · L25 Si los usa · L38 Catálogo de casos · L44 Límite

**`7_auditorias_y_verificaciones/templates/`**

- `RESULTADOS_PRUEBAS_ESTRUCTURALES.json`: 4 claves: scope, tests, passed, total
- `VERIFICACION_ESTRUCTURAL.json`: 9 claves: schema_valid, facets, f30_materials, typed_fields, operation_contracts, model_adapter_contracts, path_occurrences_checked, invalid_paths, scope
- `probar_contratos.py`: Fixtures sintéticos de estructura: no son testigos semánticos de reglas.
- `verificar_templates.py`: Structural checks plus instance checks. No claim of corpus semantic review.

**`./`**

- `CAMBIOS.md`: 29 líneas: L1 Registro de cambios del repo
- `CLAUDE.md`: sus decisiones, en §2
- `LEEME.md`: 27 líneas: L1 AI Production Director: sistema que genera prompts · L6 Dónde está cada cosa
- `PENDIENTES.md`: 33 líneas: L1 Pendientes por etapa · L10 Etapa 1 — Mapa del repositorio (registro de la lectura) · L18 Etapa 2 — Preparación de la clasificación (antes de clasificar el cor… · L31 Etapas siguientes (no empiezan hasta cerrar la etapa 2)

## 2. Decisiones e instrucciones de Eric (archivo y línea)


**`CLAUDE.md`**

- L3 **Alcance y vocabulario de los prompts**
- L8 **Antes de decir que algo no existe**
- L16 **Consultar el mapa antes de preguntar o de dar algo por faltante (instrucción de Eric, 202…**
- L25 **Riesgos, pendientes y avance de etapa (decisión de Eric, 2026-10-29)**
- L35 **Toda lectura deja registro en el repo**
- L42 **Basura, auditorías y registro de cambios (instrucción de Eric, 2026-10-30)**

**`.claude/rules/DECISIONES.md`**

- L8 | 3 | Bloque de identidad con referencia de persona adjunta | Por rol de la referencia. Keyframe de inicio o fin en imagen a video: no re-describir. …
- L9 | 4 | Taxonomía de la base de reglas | Caso ampliado con LUGAR, EDIF, ANIMAL, OBJ, MULTITUD, ENSAMBLE. Tarea por subproceso, E0.1 a POST.2 | Las 852 …
- L10 | 5 | Tarjeta de ancla en la base | Las nueve dimensiones D1 a D9 como facetas multivalor de cada regla | Una pasada de clasificación adicional sobre…
- L11 | 6 | Modelo de embeddings | `intfloat/multilingual-e5-large` local, sin API key; la tabla admite añadir OpenAI después | Cubre inglés, español y rus…
- L12 | 8 | Cómo entran las inferencias | Con etiqueta `[A PRUEBA]`; investigación de campo en foros y tutoriales para confirmar o refutar cada una; un eje…
- L13 | 9 | Quién clasifica | Clasificador de dos capas, determinista por ruta y regex más similitud vectorial con confianza, y auditoría de Eric en hoja x…
- L15 **Principios que salieron de la sesión y quedan como reglas de trabajo**
- L23 **Cambios**

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
- L13 2. «No estás aprobado para asumir nada, siempre lo verificas»: toda afirmación sobre un texto se comprueba leyendo el
- L15 3. «Siempre que hay una supuesta contradicción o incoherencia tienes que leer exhaustivamente los textos
- L18 4. **Interfaces de GPT Image 2: OpenAI API y fal.ai** (respuesta a la decisión 1 de 6). Manda
- L23 5. **F20 con una sola persona que debe seguir reconocible: «todas»** (decisión 2 de 6). Base: TRM-0175 (taxonomía L1220,
- L26 6. **Extensión F24 + «objeto entero»** (decisión 3 de 6): un objeto completo como sujeto del cuadro. Los 8 valores
- L29 7. **F05 de B1 y B4 deja de ser lista vacía** (decisión 4 de 6; la lista vacía viola taxonomía §1.12.8): B1 (pescadora en
- L32 8. **Interfaz de generación de la prueba: App de ChatGPT para escritorio** (corregido 2026-10-27). Palabras de Eric:
- L37 9. **Muestra de auditoría** (2026-10-27): Eric revisa al azar el 10 % del total de reglas marcadas «no aplica» en cada
- L40 10. **Repetición antes de auditar** (2026-10-27): si una imagen sale mal, se genera el mismo prompt por lo menos dos veces
- L45 11. **Longitud del prompt** (2026-10-27): ya estaba decidida (`.claude/rules/DECISIONES.md` decisión 2; T-BRIEF-IMG L355).
- L49 12. **Alcance de la prueba: solo imagen con aspecto de foto real** (2026-10-27). Palabras de Eric: «solo quiero que se
- L57 13. **vision-decomposer y transferencia de estilo son cosas distintas** (2026-10-27). Palabras de Eric: «porque si son
- L62 14. **Caso de descripción de imagen** (2026-10-27).
- L70 15. **Sin veredicto d en el diagnóstico** (2026-10-27, responde la pregunta 3). Palabras de Eric: «no hay límite de
- L76 16. **Lista de casos de la prueba** (2026-10-27). Eric
- L85 17. **Boceto o plano a final: 5 casos** (2026-10-27). Eric eligió un caso por cada plantilla fotográfica, igual que en
- L94 18. **Dos textos mal excluidos entran al universo** (2026-10-27). Eric respondió «Sí, meterlos» a la pregunta «¿Meto
- L103 19. **La decisión por sección se mantiene** (2026-10-27, 00:28–00:37 UTC; registrada tarde, el 2026-10-27). Se decidió en

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
- L35 8. **Nada sin verificar** (2026-10-30): «no me des una aseveración que no has verificado personalmente». Toda
- L38 9. **Para qué es el mapa** (2026-10-30): el mapa es para que el agente lo consulte y no pierda la memoria de las
- L42 11. **Borrar de forma irrecuperable** (2026-10-30): «cuando digo bórralos no es para que los escondas en algún archivo
- L45 12. **Repo, hooks y mapa** (2026-10-30, segunda parte):
- L64 13. **Basura, auditorías y registro de cambios** (2026-10-30): borrar siempre los archivos basura que se generen; una
- L68 14. **Ninguna referencia a documentos borrados** (2026-10-30): se borran todos los documentos que Eric ordenó borrar y toda

**`5_decisiones/DECISIONES_ERIC_RESCATADAS_20261027.md`**

- L5 **De la app anterior (2026-09-28)**
- L10 **Directivas del 21 y 22 de octubre (hoy en `5_decisiones/directivas_20261021/`)**

**`5_decisiones/DECISIONES_repo_20260925.md`**

- L8 | 3 | Bloque de identidad con referencia de persona adjunta | Por rol de la referencia. Keyframe de inicio o fin en imagen a video: no re-describir. …
- L9 | 4 | Taxonomía de la base de reglas | Caso ampliado con LUGAR, EDIF, ANIMAL, OBJ, MULTITUD, ENSAMBLE. Tarea por subproceso, E0.1 a POST.2 | Las 852 …
- L10 | 5 | Tarjeta de ancla en la base | Las nueve dimensiones D1 a D9 como facetas multivalor de cada regla | Una pasada de clasificación adicional sobre…
- L11 | 6 | Modelo de embeddings | `intfloat/multilingual-e5-large` local, sin API key; la tabla admite añadir OpenAI después | Cubre inglés, español y rus…
- L12 | 8 | Cómo entran las inferencias | Con etiqueta `[A PRUEBA]`; investigación de campo en foros y tutoriales para confirmar o refutar cada una; un eje…
- L13 | 9 | Quién clasifica | Clasificador de dos capas, determinista por ruta y regex más similitud vectorial con confianza, y auditoría de Eric en hoja x…
- L15 **Principios que salieron de la sesión y quedan como reglas de trabajo**
- L23 **Cambios**

**`5_decisiones/directivas_20261021/directivas_taller.json`**

- `ERIC-IDIOMA-PROMPT-INGLES`: «en ingles esto es siemore»
- `ERIC-BLOQUES-1-2-NO-TOPE`: «La expectativa de una o dos reglas por bloque sirve para evaluar los filtros, no para imponer un tope ni excluir reglas válidas.»

**`5_decisiones/directivas_20261021/user_directives.json`**

- `ERIC-B1-PHOTOREALISTIC`: «Prohibido el término photorealistic en prompts»
- `ERIC-DELEGATION-TERMS`: «Se perdió la prohibición explícita del usuario de photorealistic y fotorealista.»

## 3. Pendientes (`PENDIENTES.md`)

- L14 **P-17** (Eric; Cerrado 2026-10-30: restaurados por orden de Eric…): Hooks del paquete original
- L15 **P-18** (Eric, con el agente; Abierto): Revisar con Eric los archivos del zip que no están en `skills/` antes de decidir qué se borra
- L16 **P-05** (Eric; Abierto): Aprobación del índice `6_mapa/CONSULTA.md`
- L22 **P-06** (Agente, con aprobación de Eric; Abierto): Incorporar las extensiones de la taxonomía del 23 y del 26 de octubre (F32–F35 y valores nuevos en F04, F05, F06, F10, …
- L23 **P-07** (Agente propone, Eric aprueba; Abierto): Mecanismo para clasificar sin perder el estado: cómo retoma el trabajo un agente cuya conversación se compacta a mitad …
- L24 **P-08** (Eric; Abierto): `text-rendering.md`: Nano Banana con más de 100 idiomas (INV-003296); en la sección «Multilingual / Localization», sin …
- L25 **P-09** (Eric; Abierto): `screenwriter/SKILL.md`: 8–15 escenas (INV-003470) frente a 6–10 para 5 minutos (INV-003574)
- L26 **P-10** (Eric; Abierto): Seedream y el texto: `_capabilities.json` frente a su adaptador
- L27 **P-11** (Eric; Abierto): `validate_prompts.py`: la regla del tercio lleva `or True` (INV-012830)
- L28 **P-12** (Eric; Abierto): `patterns-and-genres.md` (7 o 8 géneros) y `shot-grammar.md` (`rack`)
- L29 **P-13** (Eric; Abierto): Tope de costo de la clasificación

## 4. Corpus: 206 archivos, 141 contenidos distintos, 13,003 textos

Por skill: sus documentos (ruta dentro de la skill). Utilidad ALTA salvo que diga [MEDIA] (regula el proceso) o [NULA] (ni una ni otra). «= x» marca una copia idéntica de x. Textos, ids y secciones de un documento: `SELECT id, encabezado, linea_inicial FROM textos WHERE archivo=?`.

- **flujos** (2 archivos, 612 textos): flujo-anclas.html; flujo-spot.html
- **ai-production-director** (3 archivos, 162 textos): SKILL.md; references/creative-strategy.md [MEDIA]; references/production-package.md
- **ai-video-storyboard** (2 archivos, 165 textos): SKILL.md; examples/tiktok-reel-30s-coffee.md
- **brand-lock-extractor** (23 archivos, 970 textos): LICENSE [NULA]; SKILL.md [MEDIA]; brand-packs/README.md [MEDIA]; brand-packs/_template.md; brand-packs/examples/saas-clean.md; examples/brand-lock.md; examples/input-brief.md; references/extraction-rubric.md; templates/brand-lock.md.tpl; tools/README.md; tools/_shotkit.py [MEDIA]; tools/_template.py [NULA]; tools/check.sh [MEDIA]; tools/copy-prompt.py [MEDIA]; tools/shots-to-html.py [MEDIA]; tools/validate_brand_lock.py [MEDIA]; tools/validate_capabilities.py; tools/validate_critique.py [MEDIA]; tools/validate_prompts.py; tools/validate_provenance.py [MEDIA]; tools/validate_schemas.py [MEDIA]; tools/validate_shots.py [MEDIA]; tools/validate_skills.py [MEDIA]
- **image** (25 archivos, 1,548 textos): LICENSE [NULA]; NOTICE [NULA]; SKILL.md; references/characters.md; references/creative-direction.md; references/dimensional.md; references/editing.md; references/golden-rules.md; references/gpt-image.md; references/models.md; references/multi-panel.md; references/nano-banana.md; references/patterns/character-design.md; references/patterns/ecommerce.md; references/patterns/fashion-editorial.md; references/patterns/food-beverage.md; references/patterns/portrait-cinema.md; references/patterns/poster-illustration.md; references/patterns/ui-social.md; references/prompt-framework.md; references/slides.md; references/storyboards.md; references/structural.md; references/text-rendering.md; references/vision-decomposer.md
- **screenwriter** (3 archivos, 392 textos): SKILL.md [MEDIA]; references/advanced-techniques.md [MEDIA]; references/pipeline-integration.md [MEDIA]
- **storyboard-architect** (44 archivos, 3,119 textos): LICENSE = `skills/brand-lock-extractor/LICENSE`; SKILL.md; brand-packs/README.md = `skills/brand-lock-extractor/brand-packs/README.md`; brand-packs/_template.md = `skills/brand-lock-extractor/brand-packs/_template.md`; examples/30s-pain-proof-promise/brand-lock.snapshot.md; examples/30s-pain-proof-promise/preview.html; examples/30s-pain-proof-promise/run.json [MEDIA]; examples/30s-pain-proof-promise/shots.json; examples/30s-pain-proof-promise/storyboard.md; examples/30s-pain-proof-promise/text-overlays.json [MEDIA]; examples/60s-founder-explainer/brand-lock.snapshot.md = `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md`; examples/60s-founder-explainer/preview.html; examples/60s-founder-explainer/run.json [MEDIA]; examples/60s-founder-explainer/shots.json; examples/60s-founder-explainer/storyboard.md; examples/60s-founder-explainer/text-overlays.json [MEDIA]; examples/shotkit-explainer/brand-lock.snapshot.md; examples/shotkit-explainer/preview.html; examples/shotkit-explainer/run.json [MEDIA]; examples/shotkit-explainer/shots.json; examples/shotkit-explainer/storyboard.md; examples/shotkit-explainer/text-overlays.json [MEDIA]; references/beat-frameworks.md [MEDIA]; references/on-screen-text.md; references/shot-grammar.md; references/timing-rules.md [MEDIA]; templates/run.schema.json [MEDIA]; templates/shots.schema.json [MEDIA]; templates/storyboard.md.tpl [MEDIA]; templates/text-overlays.schema.json; tools/README.md = `skills/brand-lock-extractor/tools/README.md`; tools/_shotkit.py = `skills/brand-lock-extractor/tools/_shotkit.py`; tools/_template.py = `skills/brand-lock-extractor/tools/_template.py`; tools/check.sh = `skills/brand-lock-extractor/tools/check.sh`; tools/copy-prompt.py = `skills/brand-lock-extractor/tools/copy-prompt.py`; tools/shots-to-html.py = `skills/brand-lock-extractor/tools/shots-to-html.py`; tools/validate_brand_lock.py = `skills/brand-lock-extractor/tools/validate_brand_lock.py`; tools/validate_capabilities.py = `skills/brand-lock-extractor/tools/validate_capabilities.py`; tools/validate_critique.py = `skills/brand-lock-extractor/tools/validate_critique.py`; tools/validate_prompts.py = `skills/brand-lock-extractor/tools/validate_prompts.py`; tools/validate_provenance.py = `skills/brand-lock-extractor/tools/validate_provenance.py`; tools/validate_schemas.py = `skills/brand-lock-extractor/tools/validate_schemas.py`; tools/validate_shots.py = `skills/brand-lock-extractor/tools/validate_shots.py`; tools/validate_skills.py = `skills/brand-lock-extractor/tools/validate_skills.py`
- **storyboard-html-preview** (19 archivos, 843 textos): LICENSE = `skills/brand-lock-extractor/LICENSE`; SKILL.md [MEDIA]; templates/preview.html.tpl [MEDIA]; templates/print.css.tpl [MEDIA]; templates/styles.css.tpl [MEDIA]; tools/README.md = `skills/brand-lock-extractor/tools/README.md`; tools/_shotkit.py = `skills/brand-lock-extractor/tools/_shotkit.py`; tools/_template.py = `skills/brand-lock-extractor/tools/_template.py`; tools/check.sh = `skills/brand-lock-extractor/tools/check.sh`; tools/copy-prompt.py = `skills/brand-lock-extractor/tools/copy-prompt.py`; tools/shots-to-html.py = `skills/brand-lock-extractor/tools/shots-to-html.py`; tools/validate_brand_lock.py = `skills/brand-lock-extractor/tools/validate_brand_lock.py`; tools/validate_capabilities.py = `skills/brand-lock-extractor/tools/validate_capabilities.py`; tools/validate_critique.py = `skills/brand-lock-extractor/tools/validate_critique.py`; tools/validate_prompts.py = `skills/brand-lock-extractor/tools/validate_prompts.py`; tools/validate_provenance.py = `skills/brand-lock-extractor/tools/validate_provenance.py`; tools/validate_schemas.py = `skills/brand-lock-extractor/tools/validate_schemas.py`; tools/validate_shots.py = `skills/brand-lock-extractor/tools/validate_shots.py`; tools/validate_skills.py = `skills/brand-lock-extractor/tools/validate_skills.py`
- **video** (15 archivos, 1,918 textos): LICENSE = `skills/image/LICENSE`; NOTICE = `skills/image/NOTICE`; SKILL.md; references/animatic-keyframes.md; references/camera-lighting-vocabulary.md; references/dramaturgy.md; references/fixes-and-skeletons.md; references/kling.md; references/patterns-and-genres.md; references/race-and-speed.md; references/role-modes.md; references/seedance-25.md; references/seedance.md; references/universal-rules.md; references/veo.md
- **visual-asset-critic** (30 archivos, 1,417 textos): LICENSE = `skills/brand-lock-extractor/LICENSE`; SKILL.md; examples/critique.accept.json [MEDIA]; examples/critique.revise.json; examples/worked-run/brand-lock.snapshot.md = `skills/storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md`; examples/worked-run/critiques/round-1/shot_01.critique.json [MEDIA]; examples/worked-run/critiques/round-1/shot_02.critique.json; examples/worked-run/critiques/round-2/shot_02.critique.json [MEDIA]; examples/worked-run/preview.html [MEDIA]; examples/worked-run/prompts/round-1/flux.txt; examples/worked-run/prompts/round-2/revised-flux.txt; examples/worked-run/run.json [MEDIA]; examples/worked-run/shots.json [MEDIA]; examples/worked-run/text-overlays.json [MEDIA]; references/critique-rubric.md; templates/critique.schema.json [MEDIA]; tools/README.md = `skills/brand-lock-extractor/tools/README.md`; tools/_shotkit.py = `skills/brand-lock-extractor/tools/_shotkit.py`; tools/_template.py = `skills/brand-lock-extractor/tools/_template.py`; tools/check.sh = `skills/brand-lock-extractor/tools/check.sh`; tools/copy-prompt.py = `skills/brand-lock-extractor/tools/copy-prompt.py`; tools/shots-to-html.py = `skills/brand-lock-extractor/tools/shots-to-html.py`; tools/validate_brand_lock.py = `skills/brand-lock-extractor/tools/validate_brand_lock.py`; tools/validate_capabilities.py = `skills/brand-lock-extractor/tools/validate_capabilities.py`; tools/validate_critique.py = `skills/brand-lock-extractor/tools/validate_critique.py`; tools/validate_prompts.py = `skills/brand-lock-extractor/tools/validate_prompts.py`; tools/validate_provenance.py = `skills/brand-lock-extractor/tools/validate_provenance.py`; tools/validate_schemas.py = `skills/brand-lock-extractor/tools/validate_schemas.py`; tools/validate_shots.py = `skills/brand-lock-extractor/tools/validate_shots.py`; tools/validate_skills.py = `skills/brand-lock-extractor/tools/validate_skills.py`
- **visual-media** (1 archivos, 83 textos): SKILL.md [MEDIA]
- **visual-prompt-forge** (39 archivos, 1,774 textos): LICENSE = `skills/brand-lock-extractor/LICENSE`; SKILL.md; adapters/_capabilities.json; adapters/capabilities.schema.json [MEDIA]; adapters/flux.md; adapters/gpt-image.md; adapters/hailuo.md; adapters/ideogram.md; adapters/kling.md; adapters/midjourney.md; adapters/nano-banana.md; adapters/seedance.md; adapters/seedream.md; adapters/veo.md; examples/one-shot-all-adapters/README.md; examples/one-shot-all-adapters/flux.txt; examples/one-shot-all-adapters/gpt-image.txt; examples/one-shot-all-adapters/ideogram.txt; examples/one-shot-all-adapters/kling.txt; examples/one-shot-all-adapters/midjourney.txt; examples/one-shot-all-adapters/nano-banana.txt; examples/one-shot-all-adapters/seedream.txt; references/consistency-locks.md; references/failure-modes.md; references/prompt-anatomy.md; tools/README.md = `skills/brand-lock-extractor/tools/README.md`; tools/_shotkit.py = `skills/brand-lock-extractor/tools/_shotkit.py`; tools/_template.py = `skills/brand-lock-extractor/tools/_template.py`; tools/check.sh = `skills/brand-lock-extractor/tools/check.sh`; tools/copy-prompt.py = `skills/brand-lock-extractor/tools/copy-prompt.py`; tools/shots-to-html.py = `skills/brand-lock-extractor/tools/shots-to-html.py`; tools/validate_brand_lock.py = `skills/brand-lock-extractor/tools/validate_brand_lock.py`; tools/validate_capabilities.py = `skills/brand-lock-extractor/tools/validate_capabilities.py`; tools/validate_critique.py = `skills/brand-lock-extractor/tools/validate_critique.py`; tools/validate_prompts.py; tools/validate_provenance.py = `skills/brand-lock-extractor/tools/validate_provenance.py`; tools/validate_schemas.py = `skills/brand-lock-extractor/tools/validate_schemas.py`; tools/validate_shots.py = `skills/brand-lock-extractor/tools/validate_shots.py`; tools/validate_skills.py = `skills/brand-lock-extractor/tools/validate_skills.py`
