# Proyecto demostración — quinteto de cuerdas (regresión A7)

Brief: *«Cinco retratos de casting de un quinteto de cuerdas: tres mujeres y dos hombres de 22–28 años, orígenes
diversos, hombros hacia arriba, fondo gris claro, personalidades distintas y rostros naturales.»*

## Abrirlo en la app

```bash
APD_DB=apd/demo/demo.sqlite python3 apd/server.py      # http://127.0.0.1:8765 → proyecto «quinteto»
```

Trabaje sobre una copia si no quiere añadir versiones al demo: `cp apd/demo/demo.sqlite /tmp/d.sqlite; APD_DB=/tmp/d.sqlite …`

## Qué hay aquí

| Archivo | Qué es |
|---|---|
| `demo.sqlite` | el proyecto con sus 18 versiones inmutables, ledgers, auditorías, revisiones y eventos |
| `prompts/E1..E5.txt` | texto final de cada retrato (el sha256 está en `estado_demo.json`) |
| `auditorias/E1..E5.json` | controles deterministas + gates originales ejecutados sin modificar |
| `export_borrador.zip` | exportación completa marcada **BORRADOR (no liberado)**, con MANIFIESTO de hashes |
| `estado_demo.json` | estado actual: ledger por estado y capa, conflictos, herencia, cuatro niveles y bloqueos por entrega |

## Historia de versiones (qué pasó y por qué)

| v | Autor | Qué |
|---|---|---|
| 1–3 | usuario | creación y aceptación de 36 propuestas (clase fuente o creativa) |
| 4 | externo | revisión externa de las 1,398 reglas por subagentes independientes, importada con la misma validación que el modelo |
| 5 | operador-demo | revisión semántica previa: emociones nombradas → señales físicas (dramaturgy §2) |
| 6 | autoridad-documentada | 2 decisiones de regla: conflicto de longitud resuelto por DECISIONES #2 + U-2026-09-28-LONGITUD. Sobre estos textos, **ronda 1** de revisión semántica independiente: 22/21/13/14/19 NO_CUMPLE |
| 7 | claude-code | correcciones en bloque fuente (cámara, negativos, meta del pipeline, hex, materiales, identidad, asimetría, mirada E5). **Defecto:** esta versión perdió en silencio la revisión externa de reglas |
| 8 | claude-code | reconstrucción de v7 con la revisión **heredada** de forma visible; **ronda 2**: 1/1/1/1/6 |
| 9 | claude-code | lean prose: encuadre sin duplicar, contexto del casting a notas, mirada de E4 una vez |
| 10 | claude-code | catálogo de conflictos aplicado también sobre la revisión (CF-MOTOR-SW30). **Defecto:** cambio de formato de clave perdió 2 decisiones del director |
| 11 | claude-code | migra esas decisiones; lista también conflictos resueltos; **ronda 3** sobre estos textos |
| 12 | claude-code | ronda 3: 0/0/2/4/1 NO_CUMPLE. E4 «calm» (emoción nombrada) → señales físicas. E3 tope de 130 palabras disputado con DECISIONES #2 |
| 13 | claude-code | la redacción de v12 compartía palabras con E1 (lo detectó la regresión A7): E4 pasa a «jaw set, shoulders squared, head held level»; **ronda 4** sólo de E4 |
| 14 | director (Eric) | D1: CF-MOTOR-SW30 → b (5 slots de GPT Image), política permanente para todo brief |
| 15 | director (Eric) | D2: SW30, máximo 2 intentos por método (CF-REROLL-SW30 → b), política permanente para todo brief |
| 16 | claude-code | 17 decisiones de regla cerradas por hecho verificable o autoridad documentada (16 CONDICIONAL + `7077767cb105`); el director puede revertirlas |
| 17 | claude-code | ronda 4 → `c1d814f8c059`: forma del rostro explícita en E4 («square face with a strong jaw»); **ronda 5** sólo de E4: 0 NO_CUMPLE |
| 18 | claude-code | U-2026-09-28-CAMBIO-QUIRURGICO: los niveles anteriores quedan fijos; la revisión de reglas heredada se conserva sin re-revisar |

Los defectos de v7 y v10 no se borraron: quedan en el historial y están corregidos en el código con pruebas
(`test_cambio_de_contexto_hereda_revision_y_bloquea_hasta_confirmar`, `test_decisiones_del_director_sobreviven_a_un_cambio_de_clave`).

## Por qué no es liberable

Las cinco entregas tienen cobertura COMPROBADA, revisión semántica REVISADA_EXTERNO y 0 NO_CUMPLE abiertos (los
disputados citan autoridad: E3 2, E5 1). Lo único que falta es lo que el procedimiento reserva a una persona:

- **aprobar la redacción** de cada texto (Auditoría → «Aprobar redacción», contra el hash exacto).

| Entrega | sha256 (12) | Palabras |
|---|---|---:|
| E1 | `3f719e39dace` | 154 |
| E2 | `ca57dbc6e504` | 159 |
| E3 | `8056f188c066` | 163 |
| E4 | `9bbd5ec413bc` | 159 |
| E5 | `744e1e78bed5` | 149 |

El resumen semántico guardado de E3 repite la etiqueta «disputados con autoridad»: es un defecto de texto
anterior a la corrección de `disputar_semantica` (`proyecto.py:924`); las versiones son inmutables.
