# Plan final de trabajo — prueba del sistema de prompts para GPT Image 2 (2026-10-27)

El sistema convierte un brief en prompts para GPT Image 2. Eric genera las imágenes en la App de ChatGPT para
escritorio. La prueba demuestra que, para cada caso, el sistema selecciona todas las reglas que aplican y que cada
prompt las cumple; y, si una imagen sale mal, dice si falló la selección (a), el armado (b) o falta la regla en el
corpus (c). El alcance no cambia: solo lo decidido hasta hoy.

## 1. Documentos leídos para este plan

Leídos completos en esta sesión:
- Universo de la prueba: 2,722 textos (`v3/universo/universo_prueba_textos.jsonl`).
- SW30 SKILL.md (152 líneas) y las 18 reglas aprendidas (`learned/`), fuera de la base de 13,005.
- Decisiones: `DECISIONES_ERIC_20261023.md` (§1–§5), `_20261024.md`, `_20261026.md` (§1–§9),
  `DECISIONES_repo_20260925.md`, `CLAUDE.md`.
- Casos y código: `produccion/prompts-sistema-20261024/` (casos.json, casos_contraste.json, correr.py),
  `produccion/template-retrato-gpt2/pelirroja-ecu-20261025/` y `b6-corregido/`, `v3/MAPA_PERSONA.md`.

Consultados por secciones, no completos: taxonomía 00688 (§0.1, §1.12.8, §7.2, F15, F20, F22, F24), T-BRIEF-IMG
(L19, L34, L40–42, L122, §12), `CONTRATOS_OPERACION_MODELO.json` (L750–789), `armar.py` (L45–75). Antes de la tarea 3
se leen completos.

## 2. Mapa del proceso: qué decisión y qué reglas gobiernan cada paso

| Paso | Qué se hace | Decisiones que lo gobiernan | Reglas del corpus |
|---|---|---|---|
| 1. Brief → caso | Facetas F01–F35 con valores de la taxonomía o de una extensión aprobada; campos del T-BRIEF-IMG | 23 §3–§5 (sin pendientes ni NO APLICA; etiquetas 100 % de la taxonomía); 26 §5–§7 (F20 «todas» con una persona; F24 «objeto entero»; F05); 26 §8 (interfaz: App de ChatGPT para escritorio) | taxonomía §1.12.8 (sin listas vacías); T-BRIEF-IMG L19 (omisión legítima solo si el campo no condiciona reglas) |
| 2. Ruta del caso | Ubicar el caso en los pasos de producción: génesis (E5.2) → derivado (E5.3) → cuadro (E5.4) → edición (E5.5) | repo 2026-09-25, principios («Rostro T1 antes que cuerpo T2, siempre»; «producto con logo… es flujo con referencia») | persona: `MAPA_PERSONA.md` (INV-000394–000397, 000474, 000604, 000610); producto con etiqueta real: INV-000465–000469; texto en imagen y edición: gpt-image.md (INV-002366–002385) |
| 3. Universo de reglas | Textos de generación de imágenes universales, parcialmente universales que incluyen GPT Image 2, y específicos de GPT Image 2 | 24 §1 (alcance, palabras de Eric del 2026-10-27); 26 §1 (cifra de GPT Image 2 manda; correcciones en `correcciones.json`) | 2,722 textos + adenda (SW30 SKILL.md y 18 reglas aprendidas) |
| 4. Selección | Por cada caso, las reglas cuya condición se cumple con sus facetas y su paso | 24 §4 (método: universo → filtro por caso → controles → clasificación de lo pertinente → prueba del selector) | condición por facetas (taxonomía §7.2); dependencias de interfaz y versión con acción concreta (TRM-0683, TRM-0684) |
| 5. Redacción | Prompt de 5 slots; retratos con `armar.py`; génesis de persona con la plantilla T1; formato escrito en el texto | CLAUDE.md (armar.py obligatorio; sin «photorealistic»); 26 §8 (formato en el texto; tamaño y quality como referencia) | gpt-image.md (5 slots, anti-slop, tamaños INV-002355–002365); INV-000604 / 000442 (plantilla T1); INV-002359 (máximo fiable) |
| 6. Validación | Controles mecánicos antes de entregar | CLAUDE.md (nunca entregar un prompt rechazado) | `correr.py` y `armar.py` |
| 7. Generación | Eric genera en la app y entrega imagen y veredicto | 26 §8 | — |
| 8. Diagnóstico | Imagen mala → a, b o c, con la traza | 26 §9 (auditoría: 10 % de los «no aplica» de cada caso) | — |

## 3. Plan de trabajo, en orden

Cada tarea termina con un control que sale con código 1 si no se cumple.

1. **Adenda del universo.** Registrar SW30 SKILL.md y las 18 reglas aprendidas con id, archivo, líneas y sha256, sin
   tocar la base de 13,005. Leer completos los 30 informes de la raíz del zip y los casos de prueba de `repo/examples`;
   entra lo que sea regla original de generación de imágenes, sale lo derivado de las skills, con motivo.
   Control: cada texto de la adenda con veredicto y motivo.
2. **Casos.** Rehacer B1–B5 con su ruta (rostro T1 → placa del lugar → T3) y B6 (T1 → T2, ya hecho); C1–C4 con su
   ruta. Control: `correr.py` sin fallas; formato en el texto de cada prompt.
3. **Lista de referencia por caso (pregunta a).** Leer cada texto del universo contra cada caso y marcar APLICA o NO
   APLICA con motivo, sin mirar facetas ni selector. Control: `rule_answer_check.py` adaptado a ids INV, 0 sin
   veredicto, 0 contradicciones.
4. **Clasificación de lo pertinente.** Clasificar en facetas, con el método del piloto (matriz + verificador), solo
   los textos que aplican a algún caso. Control: `validar_v2.py` sin fallas; etiquetas 100 % de la taxonomía.
5. **Selector y cruce.** Correr el selector sobre la clasificación y cruzar con la lista del paso 3. Control: 0 reglas
   de la referencia sin seleccionar.
6. **Traza por regla (pregunta b).** Por cada regla seleccionada: el slot donde se cumple o el control que la
   verifica. Control: 0 reglas sin una de las dos.
7. **Entrega a Eric.** Prompts listos, con su orden y las imágenes que hay que adjuntar en cada paso.
8. **Diagnóstico.** Con las imágenes y el veredicto de Eric. Si una imagen sale mal, Eric genera el mismo prompt por lo
   menos dos veces más antes de auditar (decisión 26 §10): una muestra mala del generador no es falla del prompt
   (INV-010355, «Budget 2–3 re-rolls»; INV-010387). Solo la falla que se repite se diagnostica: a si la regla que la evita está en la lista de
   referencia y el selector no la tomó; b si se tomó y el prompt no la cumple según su traza; c si a y b pasan. Así
   ninguna falla queda sin veredicto. La certeza de a depende de la lista de referencia, que se verifica con la muestra
   de auditoría del 10 % (decisión 26 §9).

## 4. Dudas que solo Eric puede resolver

Ninguna. Las dos lecturas de `MAPA_PERSONA.md` (el «maestro con luz pareja» es la referencia de personaje para video;
el look del brief va en el T3) salen de los textos citados ahí.
