# Edit propuesta al skill `prompt-production-protocol` — Step 5

**Fecha:** 2026-05-27
**Origen:** Retrospectiva F7 sesión 2026-05-27 (errores repetidos de redundancia con refs).
**Tipo:** MAYOR — añade gate determinista al proceso.

## Sección afectada

`protocol/05_self_audit.md` (Step 5 del proceso de 6 pasos).

## Edit concreta

### ANTES (texto actual)

> ### Step 5 — Self-audit VISIBLE
> Leer: `protocol/05_self_audit.md`
> - Ejecutar checklist específico del caso
> - Marcar cada item Pass/Fail en el output
> - **Si algún item crítico es Fail → revisar el draft y re-auditar. No entregar hasta pasar.**

### DESPUÉS (texto propuesto)

> ### Step 5 — Self-audit VISIBLE + Linter determinista
> Leer: `protocol/05_self_audit.md`
>
> **Step 5a — Self-audit cualitativo (igual que antes):**
> - Ejecutar checklist específico del caso
> - Marcar cada item Pass/Fail en el output
> - Si algún item crítico es Fail → revisar el draft y re-auditar
>
> **Step 5b — Linter determinista (NUEVO, obligatorio para casos 3a/3b/3c — recomendado para 1/2/4):**
> - Invocar `aurora-linter/prompt_linter.py` con: prompt, refs (con tags por categoría), case_type, mensaje del usuario (para parsear OVERRIDEs).
> - El linter chequea: redundancia por categoría, word count, negative prompt, vocabulario baneado, keywords requeridos.
> - Si STATUS=PASS → proceder a Step 6.
> - Si STATUS=FAIL sin override válido → NO entregar. Iterar el draft. NO se permite entregar al usuario con FAIL del linter.
> - Si STATUS=FAIL con overrides aceptados que cubren todas las violaciones → proceder a Step 6, declarando los overrides en el output del prompt.
> - Si STATUS=FAIL con overrides parciales (algunas violaciones overrideadas, otras no) → iterar el draft hasta limpiar las no-overrideadas.
>
> **Step 5c — Reporte del linter visible al usuario:**
> Incluir en el output del prompt el resumen del linter:
> ```
> LINTER: PASS (o FAIL con overrides)
> Violaciones detectadas: N
> Overrides aceptados: M
> Categorías cubiertas por refs: [...]
> ```
>
> Esto da trazabilidad y permite al usuario confirmar que el linter corrió antes de la entrega.

## Razón del cambio

Sesión 2026-05-27 documentó 4 errores repetidos de over-description en I2V — la regla v6.0 §5.4 existe pero el agente la olvida bajo presión de iteración rápida. El linter mueve enforcement de memoria a código.

Beneficio adicional: el override mechanism preserva flexibilidad cuando un caso edge justifica violar la regla, sin permitir abuso (requiere expresión escrita específica del usuario en el turno actual).

## Impacto en flujo

Sin linter: agente entrega → usuario corrige error en turno N+1 → agente reescribe → ciclo. Costo: ~3-4 turnos por iteración.

Con linter: agente intenta entregar → linter FAIL → agente reescribe ANTES de mostrar al usuario → entrega clean. Costo: ~0 turnos adicionales para el usuario.

## Cómo se invoca

Desde el agente al final del Step 4 drafting:

```python
# Pseudocódigo del agente
draft = "..."          # el prompt construido
refs = [...]           # tags por ref
case = "3b"            # caso clasificado en Step 0
user_msg = "..."       # mensaje completo del usuario en el turno actual

# Escribir a temp files
write("/tmp/draft.txt", draft)
write("/tmp/refs.yaml", refs_yaml)
write("/tmp/user.txt", user_msg)

# Correr linter
result = bash(f"python3 aurora-linter/prompt_linter.py --prompt /tmp/draft.txt --refs /tmp/refs.yaml --case {case} --overrides /tmp/user.txt")

if result.exit_code == 0:
    # PASS, proceder a Step 6
    deliver(draft, linter_report=result.stdout)
else:
    # FAIL, iterar
    new_draft = revise_based_on_report(draft, result.stdout)
    # vuelve a Step 4 hasta PASS
```

## Aprobación requerida

- [ ] Aprueba la edit a Step 5
- [ ] Modificar (especificar qué)
- [ ] Rechazar (sin cambios, linter queda como herramienta opcional)
