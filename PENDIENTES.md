# Pendientes por etapa

Registro vivo, que se actualiza en cada cambio de estado. Regla de Eric (CLAUDE.md, 2026-10-29): no se pasa a una etapa
nueva mientras los pendientes de la anterior no estén cubiertos al 100 %, salvo autorización expresa de Eric.

- **Un pendiente** es una decisión que no se ha tomado, una contradicción sin resolver o un trabajo sin terminar. Cada uno
  tiene responsable.
- **Un riesgo** solo existe si está totalmente fuera de control del agente. Hoy no hay ninguno registrado.

## Etapa 1 — Mapa del repositorio (registro de la lectura)

| # | Pendiente | Responsable | Estado | Cómo se cierra |
|---|---|---|---|---|
| P-17 | Hooks del paquete original | Eric | Cerrado 2026-10-30: restaurados por orden de Eric en `4_diseno/validadores/`, idénticos a los del zip y sin activar como hooks. Se habían borrado por error del agente con la orden «todo del sistema anterior se borra», que no los incluía | — |
| P-18 | Revisar con Eric los archivos del zip que no están en `skills/` antes de decidir qué se borra | Eric, con el agente | Abierto | Revisión hecha y decisión de Eric por grupo |
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
| P-19 | Regenerar el catálogo de casos (`4_diseno/casos/`) desde la taxonomía canónica; hoy `build_catalog.py` lo construye desde la 00688. Absorbe la parte de catálogo de P-06. Espera a P-22, P-24, P-25 y P-26 para no regenerarlo dos veces | Agente, con aprobación de Eric | Abierto | Catálogo regenerado, validado y aprobado |
| P-20 | Qué se hace con la taxonomía anterior 00688, que dejó de ser canónica y sigue en `3_taxonomia/` | Eric | Abierto | Decisión de Eric |
| P-21 | Criterios centralizados de clasificación (`4_diseno/CRITERIOS_CLASIFICACION.md`) | Eric | Abierto | Eric los aprueba; antes no se crea ningún agente |
| P-22 | Ampliar el universo de la fase con `flujos/flujo-anclas.html` y `skills/visual-media/SKILL.md`, donde están las reglas de documental, régimen físico y fotografía (piloto, H1) | Eric | Cerrado 2026-10-31: Eric indica que el universo tiene esas reglas; se rehace la revisión (decisión 8 del 31-oct) | — |
| P-23 | Calidad de GPT Image 2: medium por defecto, empezar en low, high para fotorrealismo, high en hero (piloto, H2) | Eric | Cerrado 2026-10-31: high; extra high para imágenes muy sofisticadas, que en GPT Image 2 queda en high porque su máximo es high (decisión 8) | — |
| P-24 | F04 sin tipo para una foto suelta; el slot Use Case lo necesita (piloto, H3) | Eric | Cerrado 2026-10-31: es «imagen fija suelta» del campo unidad, decisión del 23-oct §4 (decisión 8) | — |
| P-25 | F20 a F22 son de personas y no tienen valor para un sujeto animal (piloto, H4) | Eric | Cerrado 2026-10-31: F20, F21 y F22 valen igual para animales (decisión 8) | — |
| P-26 | Definiciones de hora dorada y atardecer (piloto, H5) | Eric | Cerrado 2026-10-31: atardecer ya existe y equivale a DUSK, TRM-0978 (decisión 8) | — |
| P-27 | Precatalogación: las secciones de primer nivel de `skills/image/SKILL.md` quedaron en «texto antes del primer encabezado» (piloto, H6) | Agente | Cerrado 2026-10-31: revisados los 206 documentos; solo `skills/image/SKILL.md` y `skills/video/SKILL.md` tenían varios encabezados de primer nivel. Corregidos en el CSV (805 → 809 encabezados) y en los conteos del nivel 2 de la taxonomía canónica | — |
| P-28 | Que el aporte de Eric sobre la biomecánica del galope (decisiones del 31-oct, punto 4) entre como regla (piloto, H8) | Eric | Cerrado 2026-10-31: lo cubre la decisión 6 (herramienta de investigación del movimiento y bloque «Acción»), que fija una fase concreta por caso y hace que lo que aporte Eric mande sobre las fuentes | — |
| P-29 | Definición de «muy sofisticada» en F37 Grado de dificultad: escena compleja, bloque «Acción», texto extenso o pequeño, o tres o más sujetos con identidad | Eric | Abierto | Aprobación o corrección de la definición |
| P-30 | Relectura exhaustiva del universo para el caso caballo con el criterio corregido (una regla en la plantilla de otra pieza aplica si su contenido aplica) y familias de valores completas | Agente | Abierto | Relectura registrada, prompt nuevo y familias completas |

## Etapas siguientes (no empiezan hasta cerrar la etapa 2)

Clasificación del corpus según la taxonomía canónica y los criterios centralizados que apruebe Eric (hoy el procedimiento está en la 00688 §1.12 y §7.4), selector y compilador de prompts por modelo y operación, sobre los adaptadores de `4_diseno/templates/`.
