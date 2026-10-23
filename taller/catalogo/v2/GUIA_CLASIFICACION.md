# Guía de clasificación v2 — texto por texto, conforme a la taxonomía original

Carpeta de trabajo: `/home/user/AI-Production-Director/taller/catalogo/v2` (aquí, "v2").
Autoridad: la taxonomía consolidada del 2026-10-19 y las decisiones vigentes. Esta guía no añade reglas: solo
explica cómo producir el registro que la taxonomía exige. Si algo de esta guía choca con la taxonomía, manda la
taxonomía.

## Lee primero, completo

1. `v2/taxonomia_extracto.md`: extracto literal de la taxonomía — principios §1.1–§1.13 (incluido el contrato
   obligatorio de clasificación por texto §1.12), §5.3 ámbito funcional y uso operativo, §6.0 campos, §7 registro,
   condiciones y consulta, gate final.
2. `v2/decisiones/`: todas las decisiones vigentes (DECISIONES_ERIC_20261023.md manda sobre las anteriores en lo
   que trata).
3. `v2/esquema_taxonomia.json`: TODOS los valores permitidos, extraídos de la taxonomía con su ID y su definición:
   `facetas` (P01, F01–F31, P04 y las extensiones aprobadas F32–F34 y valores nuevos), `campos` (§6 y §7),
   `terminos` (1,197 términos TRM del vocabulario operativo, con su faceta o materia y definición) y `destinos`
   (204 rutas del contrato de templates). Usa solo esos textos, copiados carácter por carácter.
4. El archivo fuente completo de cada texto de tu lote:
   `/tmp/claude-0/-home-user-AI-Production-Director/5525717f-6970-5668-b1ce-508e1e3863a0/scratchpad/docs/d4ea0f84-BASE_TEXTOS_ORIGINALES_13005_20261019_055700_1/fuentes_originales/<archivo>`.
   Ningún texto se clasifica sin su documento, encabezados y contexto (§1.12 punto 2–3).

## Qué produces

Para cada unidad de tu lote, de lo general a lo particular (§1.12):

**1. Decide si la unidad es regla o punto, o contenido no normativo.** Una regla es una unidad o un grupo de
unidades contiguas del lote que forman un solo enunciado (por ejemplo, la frase que introduce una lista y cada
ítem cuando el ítem no se entiende sin ella). Toda unidad del lote queda exactamente en un registro.
- Contenido no normativo → registro de **conciliación** (Gate final §1): `tipo_conciliacion` ∈ estructura · código
  auxiliar · duplicado referenciado · otro contenido no normativo, con `justificacion` explícita y revisable y
  `remite_a` (el id de la regla que lo contiene o duplica, o null). Una señal léxica ausente no autoriza a
  excluir: un ejemplo de prompt, una tabla de recomendaciones o una línea de plantilla SÍ pueden ser regla o punto
  de sintaxis.
- Regla o punto de sintaxis → registro de **regla** completo.

**2. Registro de regla (§7.1):**

```json
{
 "id": "INV-xxxxxx",                       // id de su primera unidad (identidad persistente §1.8)
 "tipo_registro": "regla",
 "unidades": ["INV-xxxxxx", "..."],
 "contexto": "ruta de encabezados y sección padre (solo lectura)",
 "bloque_E": {
   "idioma": "en|es|ru",
   "objeto_regulado": "<campos.objeto_regulado>",
   "medio": "<campos.medio> si objeto_regulado es «activo visual o sonoro»; null en las otras ramas (§1.3)",
   "unidad": "<campos.unidad>",
   "tipo_enunciado": "<campos.tipo_enunciado>",
   "fuerza_normativa": "<campos.fuerza_normativa>",
   "origen_evidencia": "<campos.origen_evidencia>",
   "evidencia_afirmacion_fuente": "<campos.evidencia_afirmacion_fuente>",
   "adopcion_canonica": "<campos.adopcion_canonica>",
   "estado_modelo_citado": {"estado": "vigente|histórico", "modelo": "<valor de F29>", "version": "...", "fecha": "..."} o null si no nombra modelo,
   "estado_evidencia": "<campos.estado_evidencia> si declara una capacidad de modelo; si no, null",
   "dependencia": "<campos.dependencia> o null",
   "autoridad": "texto si la regla establece autoridad; si no, null",
   "precedencia": "texto si hay conflicto documentado; si no, null"
 },
 "bloque_D": {
   "F30": {"estado": "VALOR", "valores": ["todas las materias pertinentes"], "evidencia": "..."},
   "F31": {"estado": "VALOR", "valores": ["un valor"], "evidencia": "..."},
   "terminos": ["TRM-nnnn", "..."],          // términos del tesauro pertinentes (campo terminos del esquema)
   "ambito_funcional": ["<campos.ambito_funcional>", "..."]
 },
 "aplicaciones": [
  {
   "aplicacion_id": "A1",
   "ruta": {"flujo": "<valor de P01>", "seccion": "texto", "paso": "<valor de F02>", "condicion": "texto breve"},
   "uso_operativo": "<campos.uso_operativo>",
   "destinos": ["<ruta del contrato: campos.destinos>"],
   "condicion": null o {"grupo": "TODAS|ALGUNA|NINGUNA", "miembros": [{"campo": "F32", "operador": "∈", "valor": ["texto corto"]}, ...]},
   "adopcion": "<campos.adopcion_canonica>",
   "facetas": { "P01": {...}, "F01": {...}, ..., "F29": {...}, "P04": {...}, "F32": {...}, "F33": {...}, "F34": {...} }
  }
 ]
}
```

Cada faceta de cada aplicación: `{"estado": "VALOR", "valores": [...], "evidencia": "..."}` o
`{"estado": "UNIVERSAL", "valores": [], "evidencia": "..."}`. Son obligatorias todas: P01, F01–F29, P04, F32, F33,
F34 (F30 y F31 van en bloque_D). La evidencia (§1.12 puntos 4 y 6) dice en pocas palabras de dónde sale la
asignación o por qué no hay restricción: origen (cuerpo, encabezado, documento o decisión) y fragmento o razón.
UNIVERSAL solo significa "sin restricción de esa faceta dentro del alcance documental comprobado" (§1.2): nunca
extiende una regla de un modelo a otro y nunca sustituye una duda.

Puntos que la taxonomía fija y no se negocian:
- Varias aplicaciones: una unidad mixta (por ejemplo, parte que regula el prompt y parte que regula el proceso o la
  entrega) conserva aplicaciones separadas; una condición alternativa son dos aplicaciones (§1.7, §7.2).
- uso_operativo por aplicación (§5.3): "INCORPORADA A TEMPLATE" exige vínculo regla → destino (campo o bloque del
  contrato) → condición → validación; "APLICACIÓN EN CONTROL O ENTREGA" para crítica, validación o entrega;
  "APLICACIÓN EN CONSTRUCCIÓN DE TEMPLATE" para instrucciones estructurales de construcción del template;
  "ACTIVO EN SELECCIÓN" para lo que se selecciona por caso.
- objeto_regulado distingue lo que regula la imagen ("activo visual o sonoro") de lo que regula documentos,
  archivos, paquetes, registros de ejecución o campos.
- Condiciones con la lógica de §7.2. Excepción = subgrupo NINGUNA dentro del grupo. Sin estados intermedios.
- Prohibidos como valores o estados (§1.12 punto 8): NO DETERMINADO, NO APLICA, DESCONOCIDO, PENDIENTE, EN PROCESO
  y equivalentes, también disfrazados de vacíos, null, listas vacías, flags o condiciones imposibles.
- Decisión del usuario 16:56:54: en reglas de ancla o keyframe F26–F28 llevan VALOR o UNIVERSAL, nunca NO APLICA.
- No amplíes ni borres valores de la taxonomía para forzar cobertura (§1.12 punto 11).

## Duda o necesidad fuera de la taxonomía

Relee fuente y decisiones. Si no lo resuelven, NO inventes un valor ni pongas UNIVERSAL para tapar: deja ese
texto fuera de tu salida, sigue con los demás y lístalo al final de tu respuesta como CONSULTA con el id, las dos
evidencias y la pregunta concreta (§1.12 punto 7). El validador marcará la cobertura incompleta y se resolverá con
Eric.

## Validación (obligatoria)

Escribe la salida con un script de Python (json.dump) en `v2/salidas/salida_NN.json` y ejecuta desde `v2`:
`python3 -I validar_v2.py lotes/lote_NN.json salidas/salida_NN.json`. Corrige hasta que imprima OK (o hasta que lo
único que falte sean las unidades enviadas a CONSULTA).
