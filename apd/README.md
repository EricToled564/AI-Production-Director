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
| Qué reglas aplican (1,704) | `rule_matcher_v3` — lógica ternaria; `UNRESOLVED` bloquea | `.claude/rules/v3/build/ruleset-3.4.0.json` |
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
python3 tests/apd/test_apd_run.py                                # 10 pruebas
```

Ejemplo completo: `examples/apd/tennis-gpt-image-2/` (facts + case; llega a
`AWAITING_AUDIT` con 365 reglas activas: 18 certificadas mecánicamente, 347 al auditor).

## Límites declarados (no decisiones silenciosas)

- Modelos soportados: `gpt-image-2`. Otro modelo bloquea en `facts_schema` hasta que
  exista su template fijo (el de Nano Banana no se ha transcrito desde `nano-banana.md`).
- Tipos: T2/T3 (una persona) y T4 (dos personas, exige `slots.subject.contact`). T1 y
  T5 tienen contratos con bloques fijos en `template_engine` que este AST no cubre.
- Tope de palabras: el que fija `_capabilities.json` del skill (300 para GPT Image).
  Los prompts de ~400 palabras de la sesión anterior no pasan este tope.
- 1,248 de las 1,704 reglas tienen validador `semantic`; el paquete no trae código
  para ellas. Su evidencia sale del auditor (agente separado), nunca del asistente que
  llenó los hechos. Sin evidencia → `PENDING` → sin entrega.
- Requiere `pip install jsonschema pyyaml`; `output_geometry_check_v32` (imagen
  generada) requiere además Pillow y no forma parte del run de prompt.
