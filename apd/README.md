# apd — ejecutor del proceso AI Production Director v3.4 dentro de Claude Code

Automatiza el proceso del paquete `AI_Production_Director_v3.4.0_COMPLETE`
(SHA-256 `5c55b7886d7e…11dc`) de modo que **ninguna decisión sobre el prompt dependa
del criterio del asistente**. El asistente aporta hechos con procedencia; todo lo
demás lo deciden scripts deterministas del paquete y un ledger que exige el 100 %.

## Qué decide cada pieza

| Decisión | Quién la toma | Archivo |
|---|---|---|
| Estructura y etiquetas del prompt | Template Photoreal Editorial del skill `image` (`gpt-image.md:126-135`), fijado en `build_ast()` | `apd/apd_run.py` |
| Valores de cada slot | `facts.json` — cada hoja con procedencia `user` / `skill:<archivo>:<línea>` / `research:<URL>`; sin procedencia no hay run | `apd/facts.schema.json` |
| Hechos congelados, hash, campos abiertos | `brief_freeze_v34`, `brief_preflight_v34` | `.claude/hooks/` |
| Validez del caso | `case_validate` (schema + invariantes) | `.claude/rules/v3/case-fingerprint.schema.json` |
| Modelo | `model_router_v33` (config canónica + overlay aprendido; el lock explícito de Eric se preserva) | `.claude/rules/v3/build/model-routing.canonical-v3.3.json` |
| Qué reglas aplican (1,704) | `rule_matcher_v3` — lógica ternaria; `UNRESOLVED` bloquea | `.claude/rules/v3/build/ruleset-3.5.0.json` |
| Que las reglas del pipeline de storyboard no se apliquen a una sola imagen | `scope_narrow_v35` — estrecha por sección declarada (`pipeline_track`, `sequence.multi_shot`, `brand.mode`, `text.mode`, `generator.family`) | `.claude/hooks/scope_narrow_v35.py` |
| Secciones exigidas por plataforma+caso y bloque `Negative:` | gate `aurora_linter` del skill `aurora-prompt-linter` (SKILL.md:8, :44-56) | run/`aurora_linter.json` |
| Texto del prompt | `prompt_ast_gate_v34` + `prompt_render_v34` (render determinista del AST contra el brief) | run/`prompt_vN.txt` |
| Verbo inicial, lenguaje natural, vocabulario prohibido | gates léxicos del repo leyendo `golden-rules.md`, `dramaturgy.md`, Anti-Slop de `gpt-image.md` | `gate_image.py`, `gate_dramaturgy.py` |
| Contrato T1..T5, 15 columnas, tope de palabras | `template_engine.py`, `audit_gi2.py`; tope desde `visual-prompt-forge/adapters/_capabilities.json` (gpt-image: **300**) | `production-package/` |
| Cumplimiento de reglas sin validador mecánico | **Otro agente** (auditor, `apd/AUDITOR.md`, texto del ejecutor del paquete); su evidencia lleva nonce y hash del prompt | run/`audit_request.json` → `evidence.json` |
| Entrega | `runtime_ledger_v3`: 100 % de reglas activas `PASS` u `OVERRIDE` autorizado por Eric; si no, no existe `DELIVERABLE.txt` | run/`ledger.json` |
| Revisión | sólo delta autorizado por Eric sobre `slots.*` → `brief_apply_delta_v34` → `prompt_patch_v34` → `prompt_revision_gate_v34` (drift = bloqueo) | run/`delta_vN.json` |
| Que lo entregado sea lo producido | Stop hook `gate_apd_delivery.py`: el bloque entregado debe ser byte a byte el `DELIVERABLE.txt` de un run `DELIVERED` | `.claude/settings.json` |

## Uso

```bash
python3 apd/apd_run.py new        --run apd/runs/<id> --facts facts.json --case case.json
python3 apd/apd_run.py audit-pack --run apd/runs/<id>            # tandas para el auditor
python3 apd/apd_run.py ledger     --run apd/runs/<id> --evidence evidence.json
python3 apd/apd_run.py revise     --run apd/runs/<id> --delta delta.json --provenance prov.json
python3 apd/apd_run.py status     --run apd/runs/<id>
python3 tests/apd/test_apd_run.py; python3 tests/apd/test_apd_variants.py; node tests/apd/test_artifact_core.mjs
```


## Variantes del AST (todas fijas; el asistente sólo llena hojas)

| `facts.model` / `operation` | Estructura (fuente) | Ejemplo |
|---|---|---|
| `gpt-image-2` / `create` | `Create …` + Scene / Subject / Important Details / Use Case / Constraints (`gpt-image.md:126-135`) | — |
| `gpt-image-2` / `edit` (T5) | Change / Preserve / Constraints (`gpt-image.md:80-83`; mismo formato que `template_engine._render_edit`) | — |
| `nano-banana-pro`, `nano-banana-2` | `Create …` + Subject + Action + Location + Composition + Style + `Format: W:H` (`nano-banana.md:13-20`); gate mecánico contra `50mm / f/2.8 / ISO` (`nano-banana.md:24`, regla `c58caa804ddc`) | — |
| `case.base_type = T1` (cualquiera de los anteriores) | Se añaden como `rule_text` los cuatro bloques canónicos `light_hard`, `skin_doc`, `usecase_doc`, `clean_doc` de `template_engine.BLOCKS` (sw30 `SKILL.md:66-74`) | — |
| `case.base_type = T4` | Exige el slot `contact` (gpt: `slots.subject.contact`; nb: `slots.contact`) | — |

## Límites declarados (no decisiones silenciosas)

- Tope de palabras: el que fija `_capabilities.json` del skill (300 GPT Image, 120
  Nano Banana). Se mantiene por decisión de Eric.
- 1,248 de las 1,704 reglas tienen validador `semantic`; el paquete no trae código
  para ellas. Su evidencia sale del auditor (agente separado), nunca del asistente que
  llenó los hechos. Sin evidencia → `PENDING` → sin entrega. Convertir una regla
  semántica en mecánica exige un validador escrito y aprobado por Eric, no por el
  asistente.
- Reclasificación 3.5.0: 111 reglas quedaron condicionadas a que el caso tenga el
  artefacto que presuponen (storyboard, brand-lock, serie de shots, texto en imagen)
  o el modelo correspondiente. Ninguna regla se borró: las 1,704 siguen publicadas y
  `tests/apd/test_scope_v35.py` comprueba que vuelven a aplicar cuando el caso sí es
  un pipeline, y que `UNKNOWN` sigue dando `UNRESOLVED` en vez de `NA`.
- El presupuesto de palabras del linter (75-130) no bloquea: el tope vigente es el de
  `_capabilities.json` (300 / 120), fijado por Eric. El resto del linter sí bloquea.
- El artefacto (`apd_core.js`) no puede correr el linter de aurora, que es un script
  Python. Las nueve reglas que se verifican contra sus archivos pasan al auditor en
  vez de darse por cumplidas o falladas: sin sistema de archivos, la página puede
  confirmar lo que produjo pero no demostrar una ausencia. `test_artifact_core.mjs`
  comprueba que la diferencia con la línea de comandos sea exactamente esas nueve.
- Validadores mecánicos (`.claude/hooks/rule_validators.py`, registro en
  `.claude/rules/v3/validators/`): 55 reglas del KB comprobadas por código en vez de
  por el auditor, aprobadas por Eric una por una. Cada una trae un caso que debe pasar
  y uno que debe fallar; si su autoprueba no sale bien, la regla vuelve al auditor.
  `UNRESOLVED` también: un validador que no puede decidir no decide.
- Dependencias: `requirements.txt` (jsonschema, PyYAML, Pillow, openpyxl). Pillow sólo
  lo usa `output_geometry_check_v32` (QA de la imagen generada) y `tests/v3.2`.
- Pruebas del paquete importadas completas: `tests/v3.2`, `tests/v3.3`, `tests/v3.3.2`,
  `tests/v3.4` (con los rulesets 3.2.1 / 3.3.0 / 3.3.1 que necesitan).
