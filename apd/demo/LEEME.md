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
| `demo.sqlite` | el proyecto con sus 13 versiones inmutables, ledgers, auditorías, revisiones y eventos |
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

Los defectos de v7 y v10 no se borraron: quedan en el historial y están corregidos en el código con pruebas
(`test_cambio_de_contexto_hereda_revision_y_bloquea_hasta_confirmar`, `test_decisiones_del_director_sobreviven_a_un_cambio_de_clave`).

## Por qué no es liberable

La app bloquea hasta que el director:

1. decida **CF-MOTOR-SW30** (SW30 `template_engine` vs 5 slots de GPT Image);
2. decida si `54a39fd24578` (stock documental del template T1) aplica a un casting comercial (NO_CUMPLE abierto en E3, E5 y posiblemente E4);
3. resuelva las reglas CONDICIONAL/CONFLICTO restantes (Reglas → bloqueo «abiertas»);
4. confirme la revisión de reglas heredada (Auditoría → «Confirmar herencia») o la vuelva a revisar;
5. apruebe la redacción de cada texto (hash exacto).

Eso es el comportamiento correcto, no una falla: son decisiones de dirección que la app no toma por su cuenta.
