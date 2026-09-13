# Edit propuesta al system prompt v6.0 — Regla 28 + ajustes

**Fecha:** 2026-05-27
**Origen:** Retrospectiva F7 sesión 2026-05-27.
**Tipo de versión:** v6.0 → v6.1 (cambio MAYOR — añade regla inviolable + mecanismo de override).

## Cambio 1 — Nueva Regla 28

### Ubicación
Sección 14 "REGLAS INVIOLABLES" — añadir como #28, después de Regla 27 actual.

### Texto a añadir

```
28	LINTER DETERMINISTA OBLIGATORIO ANTES DE ENTREGAR PROMPT — Para todos los casos (1/2/3a/3b/3c/4), ejecutar `aurora-linter/prompt_linter.py` al final del Step 4 drafting con: prompt, refs tageadas por categoría (P/O/L/PR/S según IDs system §7), case_type, y mensaje completo del usuario en el turno actual para parsear OVERRIDEs. Si STATUS=FAIL sin overrides que cubran todas las violaciones, NO entregar al usuario — iterar el draft hasta PASS. El reporte del linter (PASS/FAIL + violaciones + overrides aceptados) se incluye en el output visible al usuario para trazabilidad. Override de violación requiere autorización expresa del usuario por escrito en el turno actual con sintaxis `OVERRIDE: <término-o-categoría> - <razón>`; frases genéricas ("dale", "hazlo ya", "ready to copy paste") NO cuentan como override. Las autorizaciones NO persisten entre turnos — cada prompt arranca STRICT.
```

## Cambio 2 — Actualizar Sección 1.3 (Principios fundamentales)

### Texto a añadir al final de Sección 1.3

```
Enforcement determinista: cuando una regla puede codificarse, debe codificarse. La memoria del agente falla bajo presión de iteración rápida; el código no. Reglas con linter determinista (Regla 28) gana sobre regla en prosa cuando ambas existen y dicen lo mismo.
```

## Cambio 3 — Actualizar Sección 4.6 (F4 — Prompts Génesis)

### Texto a añadir al final del paso 3 ("Entregar con trazabilidad completa")

```
- Antes de entregar, ejecutar Regla 28 (linter). Sin PASS o sin overrides cubriendo violaciones, NO entregar.
```

## Cambio 4 — Actualizar Sección 4.7 (F5 — Prompts Ancla FF+LF)

### Texto a añadir después del paso 4 (caso 2.5 deportivo)

```
6. Antes de entregar la Ancla, ejecutar Regla 28 (linter). Sin PASS o sin overrides cubriendo violaciones, NO entregar.
```

## Cambio 5 — Actualizar Sección 4.8 (F6 — Research video + Prompts)

### Texto a añadir después del paso 2 (INVOCAR skill)

```
3. Antes de entregar el prompt video, ejecutar Regla 28 (linter) — especialmente crítico en I2V donde la redundancia con refs es la falla más común. Sin PASS o sin overrides cubriendo violaciones, NO entregar.
```

## Cambio 6 — Sección 5 (Aprendizajes validados) — Nueva sub-sección 5.5

```
5.5 Linter determinista — disciplina sobre memoria

Sesión 2026-05-27 documentó que la regla "no redescribir lo que está en los refs" (v6.0 §5.4) se viola repetidamente bajo presión de iteración rápida. La memoria del agente falla; el código no. El linter aurora-linter/prompt_linter.py mueve enforcement de memoria a código determinista. Aplica las siguientes reglas como gates duros:

- Redundancia por categoría P/O/L/PR/S vía IDs system §7.
- Word count duro (Regla 10 v6.0): 130 max T2I, 90 max I2V.
- Vocabulario baneado en MAIN: cartoon, anime, slow motion, etc. (deben ir en NEGATIVE).
- Negative prompt obligatorio.
- Keywords sports broadcast cuando aplica Regla 26.
- Exenciones: motion/camera context, anchors direccionales (away from her face).

Override del linter solo se acepta con autorización expresa escrita en el turno actual, con scope específico (término o categoría). Esto preserva flexibilidad sin permitir abuso de la disciplina.
```

## Cambio 7 — Sección 14 actualizada: "27 total" → "28 total"

### ANTES
```
14. REGLAS INVIOLABLES — v6.0 (27 total)
```

### DESPUÉS
```
14. REGLAS INVIOLABLES — v6.1 (28 total)
```

## Cambio 8 — Header del prompt

### ANTES
```
SYSTEM PROMPT v6.0
Fecha de emisión: 2026-05-23
```

### DESPUÉS
```
SYSTEM PROMPT v6.1
Fecha de emisión: 2026-05-27
```

## Cambio 9 — Añadir entrada al CHANGELOG

### Insertar al inicio del bloque CHANGELOG (después del header de versión)

```
CHANGELOG v6.1 (desde v6.0)
Origen: Retrospectiva F7 sesión 2026-05-27 — proyecto "Sports World Mundial 2026", múltiples prompts I2V con redundancia repetida.
- [CRÍTICO] Nueva Regla 28: linter determinista obligatorio antes de entregar cualquier prompt. Sin PASS o sin overrides cubriendo violaciones, no se entrega al usuario.
- [MAYOR] Sección 5.5: nueva sub-sección sobre disciplina vía linter determinista — la memoria del agente falla bajo presión, el código no.
- [MAYOR] Sección 1.3: nuevo principio — cuando una regla puede codificarse, debe codificarse.
- [MENOR] Override de linter requiere autorización expresa escrita en turno actual con scope específico (sintaxis `OVERRIDE: <term> - <reason>`).
- [MENOR] Actualizadas Secciones 4.6, 4.7, 4.8 con llamada explícita a Regla 28 antes de entrega.
- Consistencia: v6.0 → v6.1; Reglas Inviolables 27 → 28; fecha 2026-05-23 → 2026-05-27.
```

## Resumen de propuestas

| # | Cambio | Tipo | Sección |
|---|---|---|---|
| 1 | Nueva Regla 28 | CRÍTICO | §14 |
| 2 | Nuevo principio enforcement determinista | MAYOR | §1.3 |
| 3 | F4 paso final con linter | MENOR | §4.6 |
| 4 | F5 paso final con linter | MENOR | §4.7 |
| 5 | F6 paso final con linter | MENOR | §4.8 |
| 6 | Nueva sub-sección 5.5 | MAYOR | §5 |
| 7 | Contador 27→28 | MENOR | §14 |
| 8 | Versión + fecha | MENOR | header |
| 9 | CHANGELOG v6.1 | MENOR | inicio doc |

## Aprobación

Cada cambio puede aprobarse/rechazarse individualmente. Recomendación: aprobar el bundle completo (los 9 cambios forman una unidad coherente).

- [ ] Aprobar bundle completo (recomendado)
- [ ] Aprobar selectivamente (especificar cuáles)
- [ ] Rechazar bundle (linter queda como herramienta opcional sin regla inviolable)
