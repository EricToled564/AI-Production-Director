# APD v3.1 — Implementation & Publication Status

Fecha de publicación: 2026-09-11

## Estado

**PUBLISHED — Ruleset 3.1.0**

La clasificación exhaustiva offline quedó separada de la exhaustividad runtime:

- **Offline / por versión del KB:** todo el universo fuente original se contabiliza, cada bloque Markdown significativo recibe disposición final, cada bloque normativo genera una regla canónica, cada regla obtiene scope/authority/effect/validator metadata, las autoridades ejecutables/config/schema quedan inventariadas y los conflictos explícitos requieren política.
- **Runtime / por task:** un Case Fingerprint válido se compara contra **todas** las reglas publicadas. El matcher devuelve `APPLIES / NA / SUPPRESSED / UNRESOLVED`; `UNKNOWN` relevante nunca se convierte silenciosamente en `NA`.

## Universo congelado auditado

- Archivos originales contabilizados: **274 / 274**
- Archivos sin clasificación de fuente: **0**
- Archivos Markdown fuente: **94**
- Bloques Markdown significativos: **6,928 / 6,928**
- Bloques `NORMATIVE`: **1,649**
- Bloques `NON_NORMATIVE`: **1,988**
- Bloques `STRUCTURE`: **2,185**
- Bloques `EXAMPLE`: **1,106**
- Bloques pendientes: **0**
- Reglas canónicas block-based: **1,649**
- Metadata de reglas: **1,649 / 1,649 `CLASSIFIED`**
- Autoridades normativas directas (validator/config/schema/method): **55**
  - `EXECUTABLE_VALIDATOR`: 47
  - `NORMATIVE_CONFIG`: 2
  - `NORMATIVE_SCHEMA`: 5
  - `NORMATIVE_METHOD`: 1
- Condiciones de scope rechazadas por inferencia body-keyword: **0**

## Por qué el registro final es block-based

El extractor legacy encontró 1,221 enunciados, pero la auditoría de los 6,928 bloques demostró que podía omitir obligaciones escritas sin sus marcadores léxicos esperados. Por ejemplo, instrucciones imperativas como `Include in every prompt` podían no convertirse en regla.

Por eso v3.1 usa esta autoridad:

```text
SOURCE UNIVERSE
→ SOURCE ROLE
→ MARKDOWN BLOCK INVENTORY
→ FINAL BLOCK DISPOSITION
→ NORMATIVE BLOCK = 1 CANONICAL RULE
→ RULE METADATA
→ PUBLISHED RULESET
```

Los IDs legacy permanecen únicamente como trazabilidad cuando existe enlace; no determinan cobertura.

## Scope: política de seguridad

El scope de aplicabilidad se deriva de **identidad de fuente + sección/heading + decisiones manuales explícitas de routing/conflict**, no de encontrar palabras casuales dentro del texto de la regla.

En particular, el sistema rechaza la estrategia anterior que podía inferir condiciones como `feet_visible=true` sólo porque la palabra “feet” aparecía en una regla. Esa estrategia producía falsos `N/A` y fue descartada.

Se distingue:

- **scope de aplicabilidad** — decide si una regla entra al effective ruleset;
- **condición interna de cumplimiento** — la evalúa el validator una vez que la regla ya aplica.

## Conflictos explícitos publicados

Dos contradicciones declaradas por el propio AI Production Director tienen políticas machine-readable:

1. `video.final_prompt.vocabulary_closing`
   - gana APD §6.1 (`2bdbd8488f44`)
   - suprime la regla EXPRESS de cerrar con `cinematic 1080p, synchronized audio` cuando ambas aplican.
2. `final_prompt.syntax_authority`
   - gana APD §6.2 (`8b582880dec3`)
   - model-agnostic queda permitido como artefacto intermedio; el prompt final usa sintaxis del modelo destino.

También se preservaron como reglas maestras explícitas:

- §6.3 `shots.json` como fuente estructural de verdad desde Etapa 4;
- §6.4 división de autoridad forge ↔ smixs;
- §6.5 atribución en delivery/package.

## Gate A: Case Qualification

`rule_matcher_v3.py` ahora ejecuta `case_validate.py` antes de cualquier matching. Un fingerprint inválido no puede producir un ruleset efectivo.

Esto cierra un bug encontrado durante la regresión v3.1: antes era posible llamar directamente al matcher con un JSON que no pasaba el schema.

## Pruebas runtime

### Caso clavadista split-level

- Case validation: **PASS**
- Reglas evaluadas: **1,649**
- Activas: **346**
- N/A: **1,303**
- Unresolved: **0**
- Unresolved conflicts: **0**
- Resultado matcher: **PASS**

### Regresión EXPRESS video final prompt

- Reglas evaluadas: **1,649**
- Activas: **631**
- N/A: **1,016**
- Suprimidas por conflicto: **2**
- Unresolved: **0**
- Ambos conflictos maestros: **RESOLVED**

## Verification

`verify_v31.sh`:

```text
13 passed · 0 failed
```

`verify_v3.sh` (regresión de infraestructura previa):

```text
18 passed · 0 failed
```

## Hashes de publicación

- Ruleset 3.1.0: `373879d791cbe88313642736d3c7e248f6e849bd7ec4265ddadc16237cf71e56`
- Source catalog: `96f45a8ee1bf8d443e23a99f8065e5d04dc59c3aed47db342633ffdaba1e67bb`
- Final source dispositions: `5d43b85fdb707e45007a920657a879da143c76a044c06001f4b0e91581882f8d`
- Rule metadata: `a526c09bf57070d863de493f041c0e05cc79b98d1986a58b9ad7f34e3bf14d76`
- Direct authorities: `6a9af80c4218bcbe10a7d63c9338962d8cd1a3bd65aa63d042ea34b7a2cd9f9b`

## Alcance de la certificación

`EXHAUSTIVE_RELATIVE_TO_KB_SOURCE_UNIVERSE_V3_1` significa que, para el universo fuente original congelado en esta versión:

- ninguna fuente desaparece sin clasificación;
- ningún bloque Markdown significativo queda sin disposición;
- ningún bloque normativo queda sin regla canónica;
- ninguna regla canónica queda sin metadata;
- las autoridades ejecutables/config/schema están contabilizadas por hash;
- los conflictos explícitos conocidos no quedan abiertos;
- el runtime evalúa el 100% del ruleset publicado contra cada Case Fingerprint válido.

No significa que una máquina pueda demostrar matemáticamente que toda interpretación semántica humana sea infalible. Los cambios futuros del KB obligan a una nueva versión, re-clasificación de las fuentes modificadas y nueva publicación/hash.
