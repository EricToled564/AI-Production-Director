ef46fa11a526ed3e 387 líneas 3538 palabras 28122 bytes  TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md
aebeb35cdf9a76f0 820 líneas 1553 palabras 23946 bytes  TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates/CONTRATOS_OPERACION_MODELO.json
49b9470b2b6b2a83 1361 líneas 3011 palabras 44719 bytes  TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates/CONTRATO_IMAGEN_ORQUESTACION.schema.json
7ec912aa92d8d1a6 4365 líneas 175123 palabras 1210862 bytes  00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md

## T-BRIEF-IMG (TEMPLATES_REVISADOS...md) — leído L1-387 en 1 lectura
Hallazgos que obligan a la prueba:
- L13-15: brief completo mostrado, aprobación vinculada al sha256 del brief, solo entonces selección definitiva.
- L19: ningún campo vacío habilita selección; ninguna regla NO APLICA/pendiente como clasificación.
- L26-134 + L387: campos "siempre": ruta.flujo, operacion, modelo nombre/version/interfaz, pieza tipo/objetivo/uso, formato.ratio, idioma_prompt, restricciones, selecciones_taxonomicas.
- L136: procedencia_campos por valor (path, origen usuario|herencia_aprobada|inferencia_para_aprobacion|fuente_documental, fuente, valor_sha256, aprobacion_id); aprobación global brief_sha256, mensaje_id, aprobado=true.
- L187-197 GPT2-GEN 5 slots; L201-209 GPT2-EDIT Change/Preserve/Constraints; L353 refs indexadas con rol; quality/size fuera del prompt.
- L355 techo GPT2 = 300 palabras; longitud nunca se resuelve suprimiendo reglas.
- L357-369 salida común Model/Quality/Size-Ratio/Prompt/Notes; traza separada.
- L377 T-TRAZA: cada aplicación enlaza regla_id, aplicacion_id, ítems taxonómicos, fuente literal, condición, campo de brief, efecto, destino y prueba.
- L381 verificar_templates.py acredita estructura, no pertinencia ni exhaustividad.

## CONTRATOS_OPERACION_MODELO.json — leído L1-820 en 1 lectura
- L4-362: 8 contratos de operación con required_fields; base común de 12 campos (L8-19) + propios: genesis +sujetos +escena, refs 0..0 (L20-32); composicion_referencias +referencias +composicion, refs ≥1 (L64-75); edicion +edicion.cambio +edicion.preservar +referencias, refs ≥1 (L246-258).
- L40-46 etc.: invalidates_on_change: aprobacion_brief, seleccion_reglas, prompt, validaciones, aceptacion.
- L365-414: GPT2-GEN y GPT2-EDIT (slots y params quality/tamano).
- L671-687 binding_contract: 12 campos de enlace por aplicación: regla_id, aplicacion_id, item_taxonomia_ids, fuente_literal, documento, encabezado, pagina, condicion, campo_brief, efecto, destino, prueba.
- L750-753 serialización GPT Image 2: size, quality.
- L774: no generar con adaptador ajeno; contrato técnico antes de ejecutar.
- L775-819 módulos condicionales: fotografia (camara.plano, angulo, efecto_optico, luz.fuente/direccion/dureza/distribucion/contraste), accion_fisica, sujetos_visibles (cantidad, items), materialidad (materiales, texturas).

## CONTRATO_IMAGEN_ORQUESTACION.schema.json — leído L1-1361 en 1 lectura (copia idéntica en CASOS_OPCIONES_..., sha 49b9470b)
- L13-21 flujo enum FL01-FL04; L45-54 operacion enum de 8.
- L102-106 ratio con patrón N:M obligatorio.
- L427-469 referencias[] requiere archivo, sha256 (64 hex), medio, rol, indice.
- L741-753 modulos_activos enum fotografia/accion_fisica/sujetos_visibles/materialidad.
- L881-942 salida.traza: ruta, materias, procedencia, decisiones, aplicaciones, efectos, compactacion, consultas.
- L957-987 salida.aceptacion: critique, detalles_auditados, rondas, sha256_activo.
- L1040-1332 procedencia_campos requiere path, origen (usuario|herencia_aprobada|inferencia_para_aprobacion|fuente_documental), fuente, valor_sha256, aprobacion_id.
- L1333-1352 aprobacion_brief requiere brief_sha256, mensaje_id, aprobado=true.
- L1355-1360 required raíz: contrato_id, version, entrada, procedencia_campos.

## TAXONOMÍA 00688 — tramos (≤60,000 caracteres)
- T01 L1-309 leído. L29-35 seleccionabilidad (L32: discriminante ausente en el brief → completar y aprobar antes de selección definitiva). L180 §1.10 vía activo directo. L184-199 §1.12 contrato de lectura por texto (8: prohibido NO APLICA/PENDIENTE como clasificación). L202-208 §1.13 correspondencia taxonomía↔templates. L248-263 P-01: FL04 «Activo directo sin preproducción» con D01-D05 (D02 brief con propuestas aprobadas; D05 el prompt no acredita aceptación); L263: imagen con referencias no se llama génesis; técnicas compartidas remiten a FL02/FL03.
- T02 L310-576 leído. L310-333 E5.1-E7/POST de FL01 (E5.2 génesis por clase; E5.3 T2; E5.4 T3/T4 «mundos por dos pasos»; E5.5 edición ≥80 %; E5.8 máximo 2 rondas). L337-430 FL02 completo (INV-000525-000614; L430 caso T1-T5, LUGAR, EDIF...). L432-467 FL03 A0-A12 y EN.1-EN.7. L471-477 F03. L481-576 F04 (rama imagen: retrato = una o varias personas, L493) y TRM-0004…0051 (TRM-0051 pieza única/standalone).
- T03 L577-770 leído. F04 términos restantes (TRM-1260 retrato grupal). L595-632 F05 (13 valores; «estilo de vida» no está: es la extensión de 26 §7). L634-672 F06 valor tipado ancho:alto; L653: 3:2 admitido como valor tipado (PRESENCIA, TRM-0074) — B2 3:2 válido; «registrar un valor no afirma que un modelo lo admita». L674-746 F07, F08. L748-770 F09.
- T04 L771-909 leído. F09 términos. L786-812 P-04 lugar de publicación (PLT-01…08; PLT-02b feed IG 1:1 y 4:5 «ejemplos no establecen regla universal»). L816-841 F10: rama imagen «génesis sin referencias (T1)», «ancla con referencias (T2 a T4)», composición, edición (T5), transferencia, boceto. TRM-0497…0879 (TRM-0524/0665 máscara mask_image_url INV-002380).
- T05 L910-1083 leído. F10 términos finales. L934-957 F11 rol del ancla (solo etapa 5 de ancla). L959-1000 F12 función del plano. L1002-1028 F13 tipo de acción A–H (TRM-0117 A pose sostenida; «Para maestros: luz pareja» = flujo-anclas, video). L1030-1057 F14 regímenes 01-09. L1059-1083 F15 sujeto (persona = T1+T2; lugar genérico = placa vacía sin persona, «mundo para el insert T3», TRM-0136; producto con logo real exige asset).
- T06 L1084-1300 leído. F15 restos (TRM-0141 producto de marca real exige asset). L1090-1103 F16 interior/exterior. L1105-1143 F17 estilo (documental = luz dura, Tri-X, anti-belleza; comercial pulido; narrativo 70 % sombra). L1145-1186 F18 técnica («fotorrealista» es valor de faceta, no palabra de prompt). L1188-1205 F19 número de sujetos. L1207-1224 F20 identidad. L1226-1239 F21 contacto. L1241-1256 F22 rostro ≥20 %/<20 %/sin rostro (TRM-0182/0183 SIN PRESENCIA: los términos, no los valores). L1258-1300 F23 referencias por papel (persona, lugar, vestuario…); tupla por adjunto (medio, papel, id, archivo, hash).
- T07 L1301-1492 leído. F23 términos de audio/video. L1324-1352 F24 tamaño de plano (WS cuerpo entero; MS cintura; MCU cabeza y hombros; CU cabeza). L1354-1390 F25 ángulo. L1392-1451 F26 movimiento de cámara (decisión: F26-F28 contexto de clip, no van al prompt de imagen). L1453-1492 F27 transición.
- T08 L1493-1689 leído. F27 restos. L1503-1532 F28 audio. L1534-1579 F29 modelo (GPT Image 2 = gpt-image-2, TRM-0239). L1581-1618 F30 qué regula (21 + 3 P-03). L1620-1685 vocabulario F30: estrategia (13), dramaturgia (37).
- T09 L1690-1826 leído. Vocabulario F30 «encuadre y lente» (52; TRM-0267 L1695: «the intended visible result phrased in words is what actually steers the model»), «ángulo» y «movimiento» (0), «luz» (68; TRM-0367 fuente dominante, TRM-0368 luz dura).
- T10 L1827-1965 leído. Vocabulario F30 «color, grade y textura» (44; TRM-0291 «natural contrast, no HDR look» es NB), «composición» (76; TRM-0985 capas FG/MG/BG; TRM-1148 perspectiva aérea), «identidad y consistencia» (inicio).
- T11 L1966-2081 leído. Vocabulario F30 «identidad y consistencia» (TRM-0478 maestro de identidad = flujo-anclas luz pareja para Kling, ya en MAPA_PERSONA §2), «anatomía, rostro y piel» (35; TRM-0452 piel plástica), «física y movimiento congelado» (50), «texto en pantalla» (inicio).
- T12 L2082-2205 leído. Vocabulario F30 «texto en pantalla» (36; TRM-1045 texto literal entre comillas dobles), «marca y logos» (39), «estructura y sintaxis del prompt» (46; TRM-0533 vocabulario excluido; TRM-0541 parámetro estructurado fuera de la prosa; TRM-0939 GPT Image por párrafos — adaptador forge, gpt-image.md manda por T-BRIEF §1).
- T13 L2206-2332 leído. TRM-1232 5 slots (INV-002333). «parámetros técnicos» (70; TRM-0919 quality, TRM-0921 size, TRM-1356-1358 quality low/medium/high INV-002350-002352; TRM-1354 techo > intervalo). «audio» (18). «continuidad» (11). «crítica y revisión» (inicio).
- T14 L2333-2447 leído. «crítica y revisión» (43; TRM-0773 re-roll: «budget 2–3 attempts» INV-009780 — coincide con 26 §10; TRM-0702-0704 ACCEPT/REVISE/REJECT). «trazabilidad y entrega» (94; TRM-1189 shot_id null para imagen independiente; TRM-1191 image_sha256; TRM-1196 seed null si no se expone).
- T15 L2448-2645 leído. Vocabulario «materialidad» (25; TRM-1177 sombra de contacto), «puesta en escena» (14), «animación» (12). L2540-2558 F31 condición para avanzar. L2560-2582 P-05 ámbito funcional y uso operativo. L2584-2586 P-02 autoridad como metadato. L2588-2612 §6.0 campos del Bloque E (referencia adjunta como tupla; rutas de aplicación). L2614-2645 §6.1 medio, unidad, tipo de enunciado.
- T16 L2646-2878 leído. §6.1 fuerza normativa, origen de evidencia, adopción, operador de condición, estado de evidencia, dependencia (TRM-0683 interfaz). L2719-2740 §6.2 precedencias (1: vocabulario prohibido gana; 2: sintaxis final del modelo destino). L2742-2762 §6.3 autoridad (image = sintaxis final de imagen). L2764-2778 §6.4 Aurora excluida. L2780-2782 §6.5 paginación. **L2784-2816 §7**: §7.2 condición binaria tras brief completo; **§7.3 L2804** discriminantes resueltos y aprobados antes de la selección definitiva; vía activo directo; **§7.4 L2808-2816** resultado por regla y caso: EXCLUIDA POR DECISIÓN / FUERA DE ESTE CASO / APLICABLE CONFIRMADA; «top-k no acredita cobertura»; traza de consulta (caso, valores evaluados, descartes por aplicación, motivo). L2818-2844 Anexo 1 histórico. L2846- Anexo 2 conciliación (inicio).
- T17 L2879-2986 leído. Anexo 2 conciliación TRM-0030…0137 (repite tesauro; nota TRM-0128 reubicado a F13 H). Sin obligaciones nuevas.
- T18 L2987-3095 leído. Anexo 2 TRM-0138…0246 (TRM-0143 reubicado a F14). Sin obligaciones nuevas.
- T19 L3096-3237 leído. Anexo 2 TRM-0247…0388. Sin obligaciones nuevas.
- T20 L3238-3368 leído. Anexo 2 TRM-0389…0519. Sin obligaciones nuevas.
- T21 L3369-3498 leído. Anexo 2 TRM-0520…0649. Sin obligaciones nuevas.
- T22 L3499-3606 leído. Anexo 2 TRM-0650…0757 (reubicaciones de F29 a F10/F30). Sin obligaciones nuevas.
- T23 L3607-3710 leído. Anexo 2 TRM-0758…0861. Sin obligaciones nuevas.
- T24 L3711-3806 leído. Anexo 2 TRM-0862…0957. Sin obligaciones nuevas.
- T25 L3807-3917 leído. Anexo 2 TRM-0958…1068 (audio F068, metadatos F069, texto F070, iteración F071, estilos F072). Sin obligaciones nuevas para imagen fija salvo TRM-1045 (texto literal entre comillas dobles, ya en gpt-image.md).
- T26 L3918-4032 leído. Anexo 2 TRM-1069…1183 (layouts F073, multipanel F074, operaciones F075, parámetros finos F076, crítica F078). Sin obligaciones nuevas; F075 virtual try-on / interior swap remiten a gpt-image.md:94/:100 (ya en el universo).
- T27 L4033-4151 leído. Anexo 2 TRM-1184…1302 (crítica, procedencia F079 con image_sha256/prompt_sha256, preview F080, modos de prompt F081 incl. 5-slot TRM-1232 → gpt-image.md:5, óptica F083, salida F084, instrumento F085, derechos F086, marca F087). Observación: L4092 TRM-1243 «Sombras múltiples», L4099 TRM-1250 backscatter, L4103 TRM-1254 chop, L4111 TRM-1262 fondo transparente = SIN PRESENCIA EN FUENTE AUTORIZADA (no admitidos en el vocabulario operativo). Consecuencia (L4284): quedan fuera del vocabulario operativo y de la expansión de consultas; no son reglas.
- T28 L4152-4341 leído. Anexo 2 TRM-1303…1369; Anexo 3 (L4222-4284, 57 términos SIN PRESENCIA fuera del vocabulario operativo, incl. L4229-4230 TRM-0182/0183 «Rostro ≥20 % / <20 %» de faceta 22); Anexo 4 (P-01: FL04 D01–D05 incluido; P-07 Aurora excluida); Anexos 5-6; gate final de aceptación L4337-4344.
- T29 L4342-4366 leído. Gate final puntos 2-4 (L4342-4344), L4346 «el gate es criterio, no resultado»; C17; historial C18; anexo de tracks no operativo. FIN: 4,366 líneas leídas (archivo tiene 4,365 \n + última línea).
- Verificación F22: los valores «≥20%» y «<20%» son valores vigentes de la faceta (L1246-1247) y aparecen en el ejemplo de §7.3 (L2804); lo SIN PRESENCIA es solo el término de tesauro TRM-0182/0183 (L1252-1253), que queda fuera de la expansión de consultas. casos.json no se toca.
