---
description: Producir un prompt de imagen con el proceso APD v3.4 (sin criterio del asistente)
---

Sigue `.claude/rules/APD_RUNTIME.md` al pie de la letra para el brief: $ARGUMENTS

1. Escribe `apd/runs/<id>/in/facts.json` (schema `apd/facts.schema.json`) con procedencia
   en cada hoja (user | skill | research) y `apd/runs/<id>/in/case.json`
   (`.claude/rules/v3/case-fingerprint.schema.json`). Sin inventar: lo que Eric no dijo y
   ningún skill fija va a `unknowns[]` y se pregunta.
2. `python3 apd/apd_run.py new --run apd/runs/<id> --facts … --case …`
3. `python3 apd/apd_run.py audit-pack --run apd/runs/<id>`; por cada tanda de
   `audit_request.json`, lanza un subagente auditor (Agent, general-purpose) con
   `apd/AUDITOR.md` + la tanda; une sus JSON en `apd/runs/<id>/evidence.json`.
4. `python3 apd/apd_run.py ledger --run apd/runs/<id> --evidence apd/runs/<id>/evidence.json`
5. Entrega íntegro `DELIVERABLE.txt` con la cabecera SKILL / RIESGOS / TÉCNICA. Si el ledger
   falla: reporta los `FAIL` en una línea cada uno y espera el delta autorizado de Eric.
