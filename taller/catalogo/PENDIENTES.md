# Pendientes por etapa

Registro vivo, que se actualiza en cada cambio de estado. Regla de Eric (CLAUDE.md, 2026-10-29): no se pasa a una etapa
nueva mientras los pendientes de la anterior no estén cubiertos al 100 %, salvo autorización expresa de Eric.

- **Un pendiente** es una decisión que no se ha tomado, una contradicción sin resolver o un trabajo sin terminar. Cada uno
  tiene responsable.
- **Un riesgo** solo existe si está totalmente fuera de control del agente. Hoy no hay ninguno registrado.

## Etapa 1 — Mapa del repositorio (registro de la lectura)

| # | Pendiente | Responsable | Estado | Cómo se cierra |
|---|---|---|---|---|
| P-01 | Verificar las 141 explicaciones del capítulo 5 contra su original | Agente | Cerrado 2026-10-29: 141 de 141 verificadas por un segundo lector (1,341 correcciones registradas en `mapa/documentos/verificacion/`); comprobación determinista con 0 errores y 0 avisos; auditoría de 100 correcciones al azar (semilla 20261029): 99 correctas, 1 con observación, ya corregida | Las comprobaciones deterministas (`mapa/herramientas/verificar_documentos.py`) dan 0 errores. Un segundo lector, que no escribió la explicación, revisa cada afirmación contra el original y deja registro de cada corrección en `mapa/documentos/verificacion/` |
| P-02 | La utilidad ALTA, MEDIA o NULA era el juicio de cada lector | Agente | Cerrado 2026-10-29: criterio objetivo aplicado; cada documento cita los ids que prueban su clase | Criterio objetivo escrito en el capítulo 5. Cada documento lleva los ids de los textos que prueban su clase. La aplica el segundo lector |
| P-03 | Tercera lectura sellada del 10 % (método PLAN_V5 §5) | Agente | Cerrado 2026-10-30: muestras con semilla 20261030 (4 errores; lotes 2 y 7 reverificados completos), 20261031 (1 error; lote 6 reverificado completo) y 20261101 (0 errores). Registros en `mapa/documentos/auditoria/` | Un tercer lector revisa 15 documentos elegidos al azar con semilla registrada. Si encuentra un error, se vuelve a verificar el lote entero de ese documento y se repite la muestra |
| P-04 | `CLAUDE.md` dice que `aprobados-20261024/briefs.json` tiene «seis casos»; tiene cinco (B1–B5). B6 está en `b6-corregido/` | Eric | Abierto | Propuesta: «cinco casos (B1–B5) que Eric aprobó al primer intento el 2026-10-24; B6 corregido está en `b6-corregido/`» |
| P-16 | Verificar los capítulos del mapa que escribió el agente (1–4 y 6–14) contra sus fuentes, con el mismo método que las 141 explicaciones: programa, segundo lector y muestra sellada. Hasta hoy nunca se verificaron; ya se halló una afirmación sin verificar en el capítulo 1 (descripción del commit `439ddb5`) | Agente; el costo lo aprueba Eric | Abierto | 0 errores del programa y una muestra sellada con 0 errores |
| P-05 | Aprobación del mapa | Eric | Después de P-01 a P-03 | Eric lo lee y lo aprueba |

## Etapa 2 — Preparación de la clasificación (antes de clasificar el corpus)

| # | Pendiente | Responsable | Estado | Cómo se cierra |
|---|---|---|---|---|
| P-06 | Incorporar las extensiones de la taxonomía del 23 y del 26 de octubre (F32–F35 y valores nuevos en F04, F05, F06, F10, F17 y F24) al catálogo CASOS y a los destinos de TEMPLATES | Agente, con aprobación de Eric | Abierto | Catálogo y destinos actualizados, verificados con `validar.py` y `verificar_templates.py` |
| P-07 | Mecanismo para clasificar sin perder el estado (el diseño no lo especifica, capítulo 13) | Agente propone, Eric aprueba | Abierto | Especificación escrita y aprobada |
| P-08 | `text-rendering.md`: Nano Banana con más de 100 idiomas (INV-003296); en la sección «Multilingual / Localization», sin nombrar modelo, «Supports 10+ languages» (INV-003375). Hay que decidir a qué modelo se aplica la cifra de 10 | Eric | Abierto | Decisión. Propuesta en el capítulo 14 §14.3 |
| P-09 | `screenwriter/SKILL.md`: 8–15 escenas (INV-003470) frente a 6–10 para 5 minutos (INV-003574) | Eric | Abierto | Decisión. Propuesta en §14.3 |
| P-10 | Seedream y el texto: `_capabilities.json` frente a su adaptador | Eric | Abierto | Decisión. Propuesta en §14.3 |
| P-11 | `validate_prompts.py`: la regla del tercio lleva `or True` (INV-012830) | Eric | Abierto | Decisión. Propuesta en §14.3 |
| P-12 | `patterns-and-genres.md` (7 o 8 géneros) y `shot-grammar.md` (`rack`) | Eric | Abierto | Decisión. Propuesta en §14.3 |
| P-13 | Tope de costo de la clasificación | Eric | Abierto | Decisión |

## Línea aparte — Familias de régimen físico

No bloquea la clasificación del corpus: las familias no son corpus autorizado (taxonomía §0.1) mientras no se canonicen.

| # | Pendiente | Responsable | Estado | Cómo se cierra |
|---|---|---|---|---|
| P-14 | Aplicar los veredictos de `.claude/rules/research/` a las etiquetas de `.claude/rules/regimenes/` (`[CAMPO: url]`, `[REFUTADA: url]`) | Agente | Abierto | Etiquetas aplicadas, cada una con su URL de la investigación |
| P-15 | Ejercicio real por familia de régimen para canonizar (decisión 8 del 2026-09-25) | Eric genera las imágenes; el agente prepara los prompts | Abierto | `[CANONICA fecha]` con el template que funcionó |

## Etapas siguientes (no empiezan hasta cerrar la etapa 2)

Clasificación del corpus según §1.12, selector según §7.4 y compilador de prompts por modelo y operación (capítulo 14 §14.2).
