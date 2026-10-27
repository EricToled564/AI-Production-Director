# RULES_MATRIX — reconstructed from authoritative SW30 source

> Status: `SOURCE_RECONSTRUCTED`  
> Source of truth: `skills/produccion-visual-sw30/SKILL.md` in the original package.  
> Reconstruction rule: the missing matrix is rebuilt as **6 explicit process obligations + the 20 numbered critical rules** in that skill = 26 rows. No undocumented rule is invented.  
> Cell values: `REQ` = always required for this type; `COND` = rule must be evaluated and enforced when its stated condition is present; `NA` = outside this still-image type.

## Types

- **T1** — maestro de rostro
- **T2** — maestro de cuerpo
- **T3** — cuadro con 1 persona
- **T4** — cuadro con 2 personas / contacto
- **T5** — edición quirúrgica

## Matrix — 26 rules × 5 types

| ID | Rule / source-backed obligation | Block / validator owner | T1 | T2 | T3 | T4 | T5 | Source |
|---|---|---|:---:|:---:|:---:|:---:|:---:|---|
| PP01 | Catalogar el tipo antes de redactar | `catalog` | REQ | REQ | REQ | REQ | REQ | SW30 §Arquitectura, step 1 |
| PP02 | Definir secciones antes de redactar | `slots` | REQ | REQ | REQ | REQ | REQ | SW30 §Arquitectura, step 2 |
| PP03 | Ensamblar por sección; creación `P(...)`, edición `E(...)` | `template_engine` | REQ | REQ | REQ | REQ | REQ | SW30 §Arquitectura, step 3 |
| PP04 | Registro de reglas derivado de la fuente, no memoria | `rule_registry` | REQ | REQ | REQ | REQ | REQ | SW30 §Sistema de cobertura |
| PP05 | Cada regla aplicable debe cerrar CHECK/NA; cero PENDING | `rule_ledger` | REQ | REQ | REQ | REQ | REQ | SW30 §Sistema de cobertura |
| PP06 | Builder + auditor mecánico deben pasar antes de emitir | `audit_gi2` | REQ | REQ | REQ | REQ | REQ | SW30 §Motor/Verificación mecánica |
| R01 | Un solo trabajo por generación | `unique` | REQ | REQ | REQ | REQ | REQ | SW30 Regla crítica 1 |
| R02 | Posición por ancla legible de la propia imagen; no términos vagos | `framing` | COND | COND | COND | COND | COND | SW30 Regla crítica 2 |
| R03 | En edición: verbos operativos, cero narrativa/memoria | `change` | NA | NA | NA | NA | REQ | SW30 Regla crítica 3 |
| R04 | Toda comparación “same X” exige ambos referentes en ese prompt | `autocontain_refs` | COND | COND | COND | COND | COND | SW30 Regla crítica 4 |
| R05 | Herencia mínima; sólo deltas, no redescribir lo visible en ref | `preserve` | COND | COND | COND | COND | REQ | SW30 Regla crítica 5 |
| R06 | Swap de identidad es última operación y aislada | `idlock` | NA | NA | NA | NA | COND | SW30 Regla crítica 6 |
| R07 | Mundo/composite: placa vacía y luego insert controlado | `world` | NA | NA | COND | COND | COND | SW30 Regla crítica 7 |
| R08 | Still = instante congelado; no prosa de movimiento | `frozen_action` | REQ | REQ | REQ | REQ | COND | SW30 Regla crítica 8 |
| R09 | Contacto humano: anatomía fijada por keyframe aprobado | `contact` | NA | NA | NA | COND | COND | SW30 Regla crítica 9 |
| R10 | Logos sólo heredados/canónicos; cuerpos no tapan lettering | `text_lock` | COND | COND | COND | COND | COND | SW30 Regla crítica 10 |
| R11 | Asset aprobado se canoniza con hash y se edita desde ahí | `canon` | COND | COND | COND | COND | REQ | SW30 Regla crítica 11 |
| R12 | ≥80% correcto → edit, no reroll; hasta 3 ediciones apiladas | `edit_strategy` | COND | COND | COND | COND | REQ | SW30 Regla crítica 12 |
| R13 | Máximo 2 intentos por método; luego cambiar método/consultar | `attempt_policy` | REQ | REQ | REQ | REQ | REQ | SW30 Regla crítica 13 |
| R14 | Validadores y word ceilings verdes; inspección visual antes de entregar | `audit` | REQ | REQ | REQ | REQ | REQ | SW30 Regla crítica 14 |
| R15 | Si existe pipeline de shots, `shots.json` es fuente de verdad | `provenance` | COND | COND | COND | COND | COND | SW30 Regla crítica 15 |
| R16 | Reglas de clips (start/tail, movimiento puro, negativos ≤8) | `video_only` | NA | NA | NA | NA | NA | SW30 Regla crítica 16 |
| R17 | Entregas y revisiones en deltas pequeños; regla nueva se propaga a todos | `delta` | REQ | REQ | REQ | REQ | REQ | SW30 Regla crítica 17 |
| R18 | Respuesta: entregable primero; error en una línea; sin adulación | `delivery` | REQ | REQ | REQ | REQ | REQ | SW30 Regla crítica 18 |
| R19 | No afirmar capacidades/límites de plataforma sin verificar en turno | `capabilities` | REQ | REQ | REQ | REQ | REQ | SW30 Regla crítica 19 |
| R20 | `/research`, `/briefing`, `/handoff` sólo bajo sus condiciones | `workflow` | COND | COND | COND | COND | COND | SW30 Regla crítica 20 |

## Canonical section policy reconstructed from SW30

The source explicitly requires named reusable blocks, including: `optics_*`, `skin_*`, `anatomy`, `idlock`, `text_lock`, `contact_*`, `unique`, `colour`, `hair`, `fabric`, `clean_*`, `autocontain_*`.

The exact missing T2–T5 section lists are **not present in the original ZIP**. Therefore the reconstructed engine uses the smallest source-supported section contracts:

| Type | Required sections | Optional source-supported sections |
|---|---|---|
| T1 | `scene`, `subject`, `light`, `skin`, `usecase`, `clean`, `notes` | `anatomy`, `idlock`, `optics`, `colour`, `hair`, `fabric`, `mood`, `constraints`, `references` |
| T2 | `scene`, `subject`, `anatomy`, `usecase`, `notes` | `idlock`, `optics`, `skin`, `colour`, `hair`, `fabric`, `mood`, `clean`, `constraints`, `references` |
| T3 | `scene`, `subject`, `anatomy`, `usecase`, `notes` | `idlock`, `optics`, `skin`, `colour`, `hair`, `fabric`, `mood`, `clean`, `constraints`, `references` |
| T4 | `scene`, `subject`, `anatomy`, `contact`, `usecase`, `notes` | `idlock`, `optics`, `skin`, `colour`, `hair`, `fabric`, `mood`, `clean`, `constraints`, `references` |
| T5 | `change`, `preserve`, `notes` | `constraints`, `idlock`, `text_lock`, `autocontain`, `references` |

### T1 canonical block lock

The following four mappings are explicitly mandatory in the source and the engine enforces them by block identity:

- `light` → `light_hard`
- `skin` → `skin_doc`
- `usecase` → `usecase_doc`
- `clean` → `clean_doc`

## Reconstruction caveat

This file is not claimed to be the lost historical file byte-for-byte. It is a deterministic reconstruction of the obligations actually supported by the original package. Any future recovered original must supersede this file after diff + regression.
