# APD runtime — el asistente no redacta prompts de imagen

Regla operativa v3.4 del paquete (`V3_4_BRIEF_FREEZE_REPORT.md`): *the assistant is
not permitted to write a replacement prompt. It may only create an authorized brief
delta. The patch engine and deterministic renderer produce the revised prompt.*

Aquí eso deja de ser una instrucción y pasa a ser mecánica: `apd/apd_run.py`
produce el prompt y el Stop hook `gate_apd_delivery.py` no deja salir ningún bloque
de prompt de imagen que no sea, byte a byte, el `DELIVERABLE.txt` de un run que
terminó en `DELIVERED`.

## Lo único que el asistente escribe

1. `facts.json` — valores de los slots del template del modelo
   (`apd/facts.schema.json`: gpt-image-2 creación / edición T5, Nano Banana; T1 añade
   los bloques canónicos por código). **Cada hoja lleva procedencia**:
   - `user` — instrucción literal de Eric (se cita);
   - `skill` — `<skill>/<archivo>:<línea>` de un skill instalado (se verifica que
     el archivo y la línea existen);
   - `research` — URL verificada en este turno.
   Una hoja sin procedencia bloquea el run. No existe la fuente "criterio del
   asistente".
2. `case.json` — Case Fingerprint (`.claude/rules/v3/case-fingerprint.schema.json`),
   con cada campo respondido desde el brief de Eric; `UNKNOWN` se declara en
   `unknowns[]`, no se inventa.
3. `delta.json` (+ `provenance.json`) — para revisar: sólo rutas `slots.*`,
   `authorized_by: "user"`, `reason` con la instrucción de Eric. Modelo, tamaño,
   tipo o referencias cambian con un run nuevo, nunca con un delta.

## Secuencia obligatoria

```bash
python3 apd/apd_run.py new        --run apd/runs/<id> --facts facts.json --case case.json
python3 apd/apd_run.py audit-pack --run apd/runs/<id>
#   → apd/runs/<id>/audit_request.json: reglas activas sin validador mecánico, en tandas.
#   Cada tanda la audita OTRO agente (Agent tool, subagent_type general-purpose) que recibe
#   apd/AUDITOR.md + la tanda, sin la conversación. Sus JSON se unen en evidence.json.
python3 apd/apd_run.py ledger     --run apd/runs/<id> --evidence evidence.json
#   → DELIVERED sólo si runtime_ledger_v3 = 100% PASS. Cualquier FAIL: no hay entrega.
python3 apd/apd_run.py revise     --run apd/runs/<id> --delta delta.json --provenance prov.json
#   → nuevo brief + mismo AST + prompt_revision_gate; vuelve a AWAITING_AUDIT.
```

## Prohibido (y bloqueado)

- Escribir, corregir, "pulir" o parafrasear el texto de un prompt de imagen.
- Rellenar `evidence.json` uno mismo: `by` debe ser `auditor` y el nonce debe
  coincidir con `audit_request.json`.
- Entregar un prompt de un run que no esté en `DELIVERED`.
- Marcar `OVERRIDE`: sólo Eric, por escrito, con `reason` y `authorized_by`.
- Cambiar `apd/apd_run.py`, `apd/AUDITOR.md`, los schemas o los hooks durante una
  producción para que algo pase.

## Entrega

La respuesta abre con la cabecera de 3 líneas de sw30 (SKILL / RIESGOS / TÉCNICA)
y pega íntegro `apd/runs/<id>/DELIVERABLE.txt`. Después, sólo: el hash del
deliverable y la línea `APD_RUN: DELIVERED` del ledger. Si el run quedó BLOCKED se
reporta la etapa y el detalle en una línea, sin prompt.
