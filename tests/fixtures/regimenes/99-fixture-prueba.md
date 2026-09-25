---
regimen: fixture de prueba
d2_accion: C_movimiento
d3_sujetos: 1
d4_tratamiento: [documental, race]
d8_modelo: [nano-banana-pro, kling]
d9_angulo: low
casos: [T3, OBJ]
tareas: [E5.2, E6.2]
---

# Fixture de régimen — sólo para tests

Este archivo existe para probar el extractor. No es un régimen real: los reales los escribe
otra persona en `.claude/rules/regimenes/` y este fixture vive en `tests/fixtures/`.

## 1. Cuándo cargar

- Cargar este régimen siempre que el brief mencione la palabra fixture. [A PRUEBA]
- Nunca cargarlo en producción real; es material de prueba. [FUENTE: produccion-visual-sw30/SKILL.md §REGLAS CRÍTICAS]

## 2. Leyes físicas que el still debe evidenciar

1. El still debe mostrar la estela de agua detrás del sujeto, nunca agua plana. [CAMPO: https://example.com/foro-wake]
2. {d9: high} Desde arriba, el spray debe leerse como un abanico, nunca como niebla. [CANONICA 2026-09-25]
3. {d8: [veo], d2: B_pico} En el pico del salto el cuerpo debe estar comprimido, nunca extendido. [A PRUEBA]
4. El agua debe verse siempre verde esmeralda en cenotes. [REFUTADA: https://example.com/cenote-azul]
5. Esta línea es normativa pero no lleva etiqueta y por eso nunca debe entrar a la base.

## Contents

1. Esta línea de índice nunca debe entrar aunque parezca regla. [A PRUEBA]

## 3. Tabla

| Cue | Nunca | Siempre |
|---|---|---|
| Spray | Niebla difusa sin dirección | Abanico con dirección de viaje [A PRUEBA] |
