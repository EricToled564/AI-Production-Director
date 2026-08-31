# SKILL: produccion-visual-sw30

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: produccion-visual-sw30/SKILL.md

---
name: produccion-visual-sw30
description: Reglas criticas y micro-gate de produccion visual AI para Final Upgrade (proyecto SW30 y cualquier generacion de imagen/video). USA ESTE SKILL SIEMPRE que se escriba o entregue un prompt visual (imagen o video), se genere con Nano Banana, Kling, Veo, GPT Image o el conector Higgsfield, se gasten creditos de generacion, se trabaje cualquier shot, ancla, clip o asset del proyecto SW30/Sports World, o Eric escriba "gate", "micro-gate" o "reglas de produccion". APLICAR ANTES de producir - el micro-gate de 3 lineas es obligatorio antes de gastar creditos o entregar prompts; entrega sin cabecera es invalida.
---

# Producción visual SW30 — micro-gate + 20 reglas críticas

OBJETIVO ÚNICO: máxima calidad de imagen conforme al script, al menor costo de créditos.
Toda decisión se evalúa contra ese objetivo. El production-package es la fuente de verdad.

## PREGUNTA DE AVANCE (gate de entrega, antes del micro-gate)
Ninguna respuesta es satisfactoria para el usuario — y viola el prompt maestro — mientras la
respuesta honesta a esta pregunta no sea SÍ SIN MATICES:

  RESPONDE HONESTAMENTE: ¿UTILIZASTE DE FORMA EXHAUSTIVA Y CORRECTA TODAS LAS REGLAS DEL SKILL
  APLICABLES A ESTE CASO? RESPONDE SI O NO.

Reglas de uso:
- La pregunta se responde ANTES de entregar, no después de que el usuario la haga.
- Si la respuesta es NO: no se entrega. Se leen los archivos faltantes, se aplica lo que falte y
  se vuelve a preguntar. Se repite cuantas veces sea necesario.
- Prohibido responder SÍ para complacer. Un SÍ falso es una mentira y cuesta más que el NO.
- Prohibido responder SÍ con matices, condiciones o notas al pie disfrazadas de honestidad.
- "Exhaustiva" significa: leídos COMPLETOS todos los archivos del skill aplicables al caso
  (SKILL.md indica el orden obligatorio), no fragmentos ni grep.
- "Correcta" significa: cada regla verificable corre en un lint o auditor ejecutable por el
  usuario; las no mecanizables se contrastan una a una contra el texto del archivo.
- Ante duda sobre si un archivo aplica, se lee su sección "cuándo cargar / when to load" en vez
  de decidirlo por criterio propio.
- Se permite preguntar al usuario cuando la duda es de dirección creativa, no de reglas.

## ARQUITECTURA POR SECCIONES (obligatoria antes de escribir cualquier prompt)
Orden de dirección: nunca se escribe un prompt de corrido ni se parchea texto. Tres pasos, en este orden:

1. **CATALOGAR** — identificar el TIPO de prompt y leer qué reglas aplican a ese tipo en la matriz
   (production-package/RULES_MATRIX.md: 26 reglas × 5 tipos, con fuente y bloque de cada una).
   Tipos: T1 maestro rostro · T2 maestro cuerpo · T3 cuadro 1 persona · T4 cuadro 2 personas ·
   T5 edición quirúrgica.
2. **DEFINIR SECCIONES** — antes de redactar, listar las secciones que ese tipo exige. Cada regla vive
   en UN bloque nombrado y compartido (optics_*, skin_*, anatomy, idlock, text_lock, contact_*, unique,
   colour, hair, fabric, clean_*, autocontain_*), nunca en texto suelto dentro del brief.
3. **ENSAMBLAR POR SECCIÓN** — el prompt se construye llamando P(scene, subject, [details], mood,
   usecase, [constraints]) para creación o E(change, preserve, [constraints]) para edición, pasando
   bloques. Salida en el formato de SKILL.md del skill image: cabecera Model/Quality/Size + References
   + "Prompt:" + "Notes:" fuera del cuerpo.

### Sistema de cobertura de reglas — la fuente manda, no la memoria
Causa raíz medida: el catálogo de reglas salía de la memoria y cubría 26 de 209 enunciados de la
fuente (12%). Todos los controles derivaban de ese catálogo, así que compartían un único punto de
falla. Cadena corregida, con tres herramientas en production-package:

1. `rule_registry.py` — relee los 23 archivos del skill image y EXTRAE mecánicamente cada enunciado
   normativo (209). Si el skill cambia, el registro cambia solo. Mi interpretación deja de ser etapa.
2. `rule_ledger.py` — obliga a que CADA regla aplicable tenga disposición explícita: CHECK (existe
   verificación) o NA (con razón escrita y auditable). Sale con código 1 si queda una sola PENDING.
3. `audit_gi2.py` — verifica los prompts columna por columna.

**GATE DE COBERTURA**: el builder corre `rule_ledger.py` antes de emitir; si no cierra en 100%
dispuesto, no hay archivo de prompts. Estado actual: 124 reglas aplicables · 100 con verificación
(80%) · 24 excluidas con razón (19%) · 0 pendientes · 100% dispuesto.

Cuando el usuario detecte un defecto: se añade su regla al ledger con su check en el mismo turno.
Así el sistema aprende de su detector más confiable en vez de perder el hallazgo.

### Template canónico de MAESTRO DE ROSTRO (T1) — obligatorio, aplicado por código
Dirección canonizó el template que resolvió el look plástico (2026-08-25). Todo maestro de rostro
se instancia con estos cuatro bloques y el motor lanza TemplateViolation si se sustituye alguno:

| Sección | Bloque obligatorio | Por qué |
|---|---|---|
| light | `light_hard` | luz dura sin relleno, rasante: los poros proyectan sombra. La luz suave de softbox aplana la piel y produce el look plástico — PROHIBIDA en rostros |
| skin | `skin_doc` | defectos concretos (rojeces, descamación, sudor, pigmento desigual, pelos de barba individuales, labios agrietados), no "imperfecciones sutiles" |
| usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO en rostros |
| clean | `clean_doc` | anti-belleza explícito: no beauty retouching, no skin smoothing, no even complexion, no soft fill light |

Además, en el slot de rasgos: describir una cara IRREGULAR (nariz con caballete, cicatriz, ojos
hundidos, asimetrías). La cara regular y simétrica es la que lee como maniquí.

Longitud: el prompt completo se mantiene alrededor de 250 palabras. Un slot de 300+ palabras compite
consigo mismo — causa documentada de artefactos en gpt-image-2.

### Motor de plantillas — el molde se cumple por código, no por disciplina
`production-package/template_engine.py` es OBLIGATORIO para construir cualquier prompt visual.
Un prompt no se escribe: se INSTANCIA con `build(tipo, ..., notes=...)`. El motor lanza
`TemplateViolation` y no devuelve nada si:
- falta cualquier sección obligatoria del tipo (T1..T5 declaran su lista, en orden);
- se pasa una sección que la plantilla no declara;
- una sección que debe venir de `BLOCKS` llega como texto suelto — el mensaje dice qué bloque editar;
- falta el bloque `Notes`;
- se cuela un metadato (Model/Quality/Size/Aspect ratio) dentro del cuerpo del prompt.
`python3 template_engine.py` corre su autotest: comprueba que rechaza secciones faltantes, texto
suelto y tipos desconocidos, y que una instancia válida sí se construye.

### Ante un cambio
- Identificar a qué BLOQUE pertenece → editar ese bloque UNA vez → recompilar → auditar.
- El cambio se propaga solo a todos los briefs que usan ese bloque.
- **PROHIBIDO editar el texto de un brief individual.** Eso es parchar: arregla una cosa y rompe otra,
  y es la causa raíz de los ciclos de tres reescrituras.

### Verificación mecánica (no depende de criterio)
- `audit_gi2.py` valida 15 columnas: slots · anti-slop · ratio estándar · metadatos fuera del prompt ·
  Notes · cámara con los 5 efectos ópticos (compresión, bokeh/wash, viñeta, halación, grano) · mood ·
  color · identity-lock · texto de marca · framing positivo · mirada · manos.
- El lint del builder ROMPE la compilación ante cualquier desviación de plantilla.

## MICRO-GATE (obligatorio en los dos puntos de no retorno)
Antes de (a) cualquier generación que gaste créditos y (b) entregar cualquier prompt visual,
la respuesta abre con exactamente 3 líneas:
  SKILL: <archivo y sección leídos EN ESTE turno>
  RIESGOS: <qué puede fallar y qué línea del prompt lo mitiga>
  TÉCNICA: <técnica probada encontrada y fuente, o "no encontrada">
Entrega sin cabecera = inválida; Eric la rechaza sin leerla. Generación sin preflight de
costo = prohibida.

## REGLAS CRÍTICAS
1. Un solo trabajo por generación. Con dos personajes: un sujeto por generación, o técnica
   de colocación probada; nunca "a ver si sale".
2. Posición SIEMPRE por ancla legible de la propia imagen (letterforms del mundo: "his back
   level with the letter L of WORLD"). Prohibido "left half", "centre", "just left of X".
3. El editor no tiene memoria: solo verbos operativos (Move/Replace/Add/Remove/Swap), cero
   narrativa ("has become", "again").
4. Autocontención: toda comparación ("same X") exige ambos referentes adjuntos en ESE prompt.
5. Herencia mínima: "same face and clothes" + solo los deltas. Cero re-descripción de lo que
   la referencia ya muestra.
6. Swap de identidad = última operación, sola: "Replace X with Y — same position, same pose,
   same scale".
7. Mundos por dos pasos: placa vacía primero; insert con "use only the person from image N,
   ignore its setting" + "keep the world of image 1 untouched".
8. Stills en instante congelado ("frozen mid-stride"); nada de movimiento en imagen fija.
9. Contactos entre personas: "a natural high five" — la anatomía la fija el keyframe
   aprobado, nunca la asignación de manos por texto.
10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los
    cuerpos nunca tapan logo ni lettering en frames congelados.
11. Lo aprobado se canoniza con hash y se EDITA desde ahí; lo caro nunca se regenera.
12. "Edit, don't re-roll": resultado ≥80% correcto → cambio puntual (hasta 3 ediciones
    apiladas), nunca re-tirar.
13. Máximo 2 intentos por método. A la 2ª falla: cambio de método con causa declarada, o
    alto y consulta. Nunca tercera vuelta de lo mismo.
14. Validadores del paquete y techos de palabras en verde antes de entregar; inspección
    visual propia (zooms 100% de rostros y manos) antes de presentar. Si algo falla: no se
    entrega, se repite — y se dice qué falló en una línea.
15. shots.json es la fuente de verdad: todo cambio entra ahí primero y se propaga.
16. Clips: solo Preserve-cues, roles de start/tail ("The tail image defines X — inherit
    exactly"), movimiento puro, imagen final nombrada; negativos sin "no X", ≤8 ítems.
17. Entregas en unidades chicas con OK de dirección; se entrega el delta, no el paquete.
    Una regla nueva de dirección se aplica a TODOS los prompts, no a la mitad.
18. Respuestas: el dato o entregable en la primera línea. Cero adulación y cero evaluación
    de las acciones de Eric salvo que la pida. Error = una línea de corrección, sin disculpas.
19. Prohibido afirmar capacidades, límites o hechos de plataforma sin verificarlos en este
    turno (leer la fuente o buscar); lo no verificado se etiqueta como inferencia.
20. /research solo para problemas genuinamente nuevos; /briefing solo al retomar tras días
    fuera; /handoff al cerrar sesión. Ninguno por default.

