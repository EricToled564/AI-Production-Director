# Pendientes por etapa

Registro vivo, que se actualiza en cada cambio de estado. Regla de Eric (CLAUDE.md, 2026-10-29): no se pasa a una etapa
nueva mientras los pendientes de la anterior no estén cubiertos al 100 %, salvo autorización expresa de Eric.

- **Un pendiente** es una decisión que no se ha tomado, una contradicción sin resolver o un trabajo sin terminar. Cada uno
  tiene responsable.
- **Un riesgo** solo existe si está totalmente fuera de control del agente. Hoy no hay ninguno registrado.

## Etapa 1 — Mapa del repositorio (registro de la lectura)

| # | Pendiente | Responsable | Estado | Cómo se cierra |
|---|---|---|---|---|
| P-01 | Verificar las 141 explicaciones del corpus (borradas el 2026-10-30) contra su original | Agente | Cerrado 2026-10-29: 141 de 141 verificadas por un segundo lector (1,341 correcciones registradas); comprobación determinista con 0 errores y 0 avisos; auditoría de 100 correcciones al azar (semilla 20261029): 99 correctas, 1 con observación, ya corregida. Las 141 explicaciones se borraron el 2026-10-30 por orden de Eric; su utilidad quedó en `6_mapa/herramientas/utilidad_corpus.json` | Las comprobaciones deterministas (`mapa/herramientas/verificar_documentos.py`) dan 0 errores. Un segundo lector, que no escribió la explicación, revisa cada afirmación contra el original  |
| P-02 | La utilidad ALTA, MEDIA o NULA era el juicio de cada lector | Agente | Cerrado 2026-10-29: criterio objetivo aplicado; cada documento cita los ids que prueban su clase | Criterio objetivo: ALTA dice qué va o no va en un prompt; MEDIA regula el proceso; NULA ninguna de las dos (`6_mapa/CONSULTA.md` §4). Cada documento lleva los ids de los textos que prueban su clase. La aplica el segundo lector |
| P-03 | Tercera lectura sellada del 10 % (muestra sellada) | Agente | Cerrado 2026-10-30: muestras con semilla 20261030 (4 errores; lotes 2 y 7 reverificados completos), 20261031 (1 error; lote 6 reverificado completo) y 20261101 (0 errores). Los registros de verificación y auditoría se borraron el 2026-10-30 por instrucción de Eric | Un tercer lector revisa 15 documentos elegidos al azar con semilla registrada. Si encuentra un error, se vuelve a verificar el lote entero de ese documento y se repite la muestra |
| P-04 | `CLAUDE.md` dice que `aprobados-20261024/briefs.json` tiene «seis casos»; tiene cinco (B1–B5). B6 está en `b6-corregido/` | Eric | Sin objeto 2026-10-30: Eric ordenó borrar `produccion/template-retrato-gpt2/` y su sección de CLAUDE.md | Propuesta: «cinco casos (B1–B5) que Eric aprobó al primer intento el 2026-10-24; B6 corregido está en `b6-corregido/`» |
| P-16 | Verificar los capítulos del mapa | Agente | Sin objeto 2026-10-30: Eric ordenó borrar los capítulos; el mapa es solo el índice `6_mapa/CONSULTA.md` | — |
| P-17 | Hooks del paquete original | Eric | Cerrado 2026-10-30: restaurados por orden de Eric en `4_diseno/validadores/`, idénticos a los del zip y sin activar como hooks. Se habían borrado por error del agente con la orden «todo del sistema anterior se borra», que no los incluía | — |
| P-18 | Revisar con Eric los 506 archivos del zip que no son `skills/` ni NotebookLM (el sistema anterior) antes de decidir qué se borra. Incluye `project_knowledge_pack/` (el zip fuente volcado como texto en 7 partes) y `original_source/aiproductiondirectorcompleto.zip`; los dos contienen todavía el material de NotebookLM | Eric, con el agente | Abierto. Eric ordenó no borrar archivos del zip hasta revisarlos, salvo NotebookLM (borrados: 30) | Revisión hecha y decisión de Eric por grupo |
| P-19 | Los niveles de generalidad y la jerarquía de lectura solo estaban completos en PLAN_V5 §13.1–13.2 | Eric | Cerrado 2026-10-30: extraídos literal a `4_diseno/niveles_de_generalidad.md` y `4_diseno/jerarquia_de_lectura.md`; el resto de PLAN_V5 se borró por orden de Eric | — |
| P-05 | Aprobación del índice `6_mapa/CONSULTA.md` | Eric | Abierto | Eric lo revisa y lo aprueba |

## Etapa 2 — Preparación de la clasificación (antes de clasificar el corpus)

| # | Pendiente | Responsable | Estado | Cómo se cierra |
|---|---|---|---|---|
| P-06 | Incorporar las extensiones de la taxonomía del 23 y del 26 de octubre (F32–F35 y valores nuevos en F04, F05, F06, F10, F17 y F24) al catálogo CASOS y a los destinos de TEMPLATES | Agente, con aprobación de Eric | Abierto | Catálogo y destinos actualizados, verificados con `validar.py` y `verificar_templates.py` |
| P-07 | Mecanismo para clasificar sin perder el estado: cómo retoma el trabajo un agente cuya conversación se compacta a mitad de un texto. El diseño no lo especifica | Agente propone, Eric aprueba | Abierto | Especificación escrita y aprobada |
| P-08 | `text-rendering.md`: Nano Banana con más de 100 idiomas (INV-003296); en la sección «Multilingual / Localization», sin nombrar modelo, «Supports 10+ languages» (INV-003375). Hay que decidir a qué modelo se aplica la cifra de 10 | Eric | Abierto | Decisión. Propuesta del agente: registrar las dos cifras con su cita y no usar ninguna como regla hasta que Eric decida; solo afecta a Nano Banana (no verificado: INV-003375 no nombra modelo) |
| P-09 | `screenwriter/SKILL.md`: 8–15 escenas (INV-003470) frente a 6–10 para 5 minutos (INV-003574) | Eric | Abierto | Decisión. Propuesta del agente: leer las dos como compatibles, 6–10 para 5 minutos y 8–15 para el rango de 5 a 10 minutos. Etapa de guion |
| P-10 | Seedream y el texto: `_capabilities.json` frente a su adaptador | Eric | Abierto | Decisión. Propuesta del agente: que mande el adaptador, porque es el más específico, y no pedir texto a Seedream |
| P-11 | `validate_prompts.py`: la regla del tercio lleva `or True` (INV-012830) | Eric | Abierto | Decisión. Propuesta del agente: tratarla como regla solo de planos de cruce o de ancla, que es lo que sugieren las condiciones escritas antes del `or True` («crossing», «crosses the», «anchor»); el código no tiene un comentario que lo diga |
| P-12 | `patterns-and-genres.md` (7 o 8 géneros) y `shot-grammar.md` (`rack`) | Eric | Abierto | Decisión. Propuesta del agente: tomar los 8 géneros y admitir `rack`, como dice el esquema. Sin efecto en GPT Image 2 |
| P-13 | Tope de costo de la clasificación | Eric | Abierto | Decisión |

## Línea aparte — Familias de régimen físico

P-14 y P-15: sin objeto. Las familias y su investigación se borraron el 2026-10-30 por instrucción de Eric.

## Etapas siguientes (no empiezan hasta cerrar la etapa 2)

Clasificación del corpus según la taxonomía §1.12, selector según §7.4 y compilador de prompts por modelo y operación, sobre los adaptadores de `4_diseno/templates/`.
