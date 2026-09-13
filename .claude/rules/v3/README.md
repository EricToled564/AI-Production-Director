# AI Production Director — Rule Engine v3.1

## Principio central

> Exhaustividad global al compilar el Knowledge Base. Exhaustividad contextual al ejecutar cada caso.

El LLM puede proponer clasificación, decisiones creativas y artefactos. **No certifica su propio cumplimiento.** El Rule Engine publica un ruleset sólo después del gate offline y en runtime evalúa ese ruleset contra un Case Fingerprint validado.

## Offline: una vez por versión del KB

```text
274 ORIGINAL SOURCES
        ↓
SOURCE CATALOG + AUTHORITY ROLE
        ↓
6,928 MARKDOWN BLOCKS
        ↓
FINAL DISPOSITION FOR EVERY BLOCK
        ↓
1,649 NORMATIVE BLOCKS
        ↓
1,649 CANONICAL BLOCK RULES
        ↓
1,649 CLASSIFIED METADATA ROWS
        ↓
55 DIRECT EXECUTABLE/CONFIG/SCHEMA AUTHORITIES
        ↓
CONFLICT POLICIES
        ↓
STRICT PUBLISH GATE
        ↓
RULESET 3.1.0
```

La compilación block-based reemplaza como autoridad de cobertura al extractor lexical legacy. El extractor legacy se conserva sólo para provenance.

## Runtime: cada task

```text
USER REQUEST
   ↓
CASE COMPILER
   ↓
CASE FINGERPRINT
   ↓
case_validate.py  ← Gate A
   ↓
rule_matcher_v3.py
   ↓
ALL 1,649 RULES EVALUATED
   ↓
APPLIES / NA / SUPPRESSED / UNRESOLVED
   ↓
0 UNRESOLVED
   ↓
ARTIFACT BUILDER + VALIDATORS
   ↓
runtime_ledger_v3.py
   ↓
100% ACTIVE RULES PASS / AUTHORIZED OVERRIDE
   ↓
DELIVERY
```

## Archivos principales v3.1

### Fuente y compilación

- `build/source_catalog.json` — 274/274 archivos originales, roles y hashes.
- `build/source_blocks.json` — 6,928 bloques Markdown significativos.
- `source-dispositions.final-v3.1.jsonl` — disposición final de cada bloque.
- `build/rules.block-v3.1.json` — 1 regla canónica por bloque `NORMATIVE`.
- `rule-metadata.final-v3.1.jsonl` — scope/authority/effect/validator/conflict para las 1,649 reglas.
- `build/direct-authorities-v3.1.json` — validators, configs, schemas y método normativo no duplicados como prosa.
- `conflict-policies.v3.1.json` — resolución machine-readable de conflictos explícitos.
- `build/ruleset-3.1.0.json` — ruleset publicado.

### Compilers/gates

- `kb_source_catalog_v3.py`
- `kb_block_inventory.py`
- `source_dispositions_final_v31.py`
- `block_rule_compile_v31.py`
- `classify_block_rules_v31.py`
- `direct_authorities_v31.py`
- `ruleset_publish_v31.py`

### Runtime

- `case_validate.py`
- `rule_engine_v3.py`
- `rule_matcher_v3.py`
- `runtime_ledger_v3.py`
- `inheritance_resolver_v3.py`

### Verification

- `verify_v31.sh` — 13 checks específicos de publicación/exhaustividad v3.1.
- `verify_v3.sh` — 18 checks de regresión del engine fail-closed.

## Scope vs condición interna

La v3.1 prohíbe estrechar scope mediante keyword spotting en el cuerpo de una regla. El scope se deriva de fuente/sección/adapter/routing explícito.

Ejemplo incorrecto y rechazado:

```text
la regla menciona "feet"
→ inferir subject.feet_visible=true
```

Eso podría excluir la regla por error y generar un falso PASS.

Una condición interna puede permanecer dentro del validator:

```text
regla aplica a image prompt
→ validator: si los pies son visibles, verifica anatomía de pies
```

## UNKNOWN y fail-closed

El DSL usa lógica ternaria. Cuando una condición de matching necesita un campo `UNKNOWN`, devuelve `UNRESOLVED`; nunca lo convierte en `NA` silenciosamente.

Además, el matcher ahora ejecuta obligatoriamente `case_validate.py` antes de empezar. Un fingerprint inválido no se evalúa.

## Conflictos

Los conflictos no se resuelven mediante una prohibición global inventada. Sólo cuando reglas incompatibles coinciden en el mismo case se consulta una política explícita.

Ruleset 3.1.0 publica dos contradicciones maestras declaradas por APD:

- `video.final_prompt.vocabulary_closing` → gana APD §6.1.
- `final_prompt.syntax_authority` → gana APD §6.2.

Si aparece un grupo incompatible sin una política única, runtime devuelve `UNRESOLVED`.

## Publicación reproducible

```bash
cd repo

python3 .claude/hooks/ruleset_publish_v31.py \
  --source-catalog .claude/rules/v3/build/source_catalog.json \
  --source-blocks .claude/rules/v3/build/source_blocks.json \
  --source-dispositions .claude/rules/v3/source-dispositions.final-v3.1.jsonl \
  --block-rules .claude/rules/v3/build/rules.block-v3.1.json \
  --metadata .claude/rules/v3/rule-metadata.final-v3.1.jsonl \
  --metadata-schema .claude/rules/v3/rule-metadata.schema.json \
  --direct-authorities .claude/rules/v3/build/direct-authorities-v3.1.json \
  --conflicts .claude/rules/v3/conflict-policies.v3.1.json \
  --version 3.1.0 \
  --out .claude/rules/v3/build/ruleset-3.1.0.json
```

## Verification

```bash
bash .claude/hooks/verify_v31.sh
# 13 passed · 0 failed

bash .claude/hooks/verify_v3.sh
# 18 passed · 0 failed
```

Las cifras y hashes exactos están en `repo/V3_IMPLEMENTATION_STATUS.md` y en el root `EXHAUSTIVE_CLASSIFICATION_REPORT.md`.
