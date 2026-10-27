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

Leídos completos el 2026-10-27, con registro por tramo en `v3/LECTURA_4_DOCUMENTOS.md` (rangos 1..N sin huecos):
- Taxonomía 00688: 4,366 líneas en 29 tramos (sha256 7ec912aa92d8d1a6…).
- T-BRIEF-IMG (`TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`): 387 líneas (ef46fa11a526ed3e…).
- `CONTRATOS_OPERACION_MODELO.json`: 820 líneas (aebeb35cdf9a76f0…).
- `CONTRATO_IMAGEN_ORQUESTACION.schema.json`: 1,361 líneas (49b9470b2b6b2a83…; la copia de `CASOS_OPCIONES_…` es
  idéntica).

Consultado por secciones, no completo: `armar.py` (L45–75).

## 2. Mapa del proceso: qué decisión y qué reglas gobiernan cada paso

| Paso | Qué se hace | Decisiones que lo gobiernan | Reglas del corpus |
|---|---|---|---|
| 1. Brief → caso | Facetas F01–F35 con valores de la taxonomía o de una extensión aprobada; campos del contrato con su procedencia; Eric aprueba cada brief por su sha256 | 23 §3–§5 (sin pendientes ni NO APLICA; etiquetas 100 % de la taxonomía); 26 §5–§7 (F20 «todas» con una persona; F24 «objeto entero»; F05); 26 §8 (interfaz: App de ChatGPT para escritorio) | taxonomía §1.12.8 (sin listas vacías), §7.3 L2804 (discriminantes aprobados antes de la selección definitiva); T-BRIEF-IMG L13–15 (aprobación ligada al sha256 del brief), L19, L26–134 (campos «siempre»), L136 (procedencia por valor); schema L1040–1332 (`procedencia_campos`), L1333–1352 (`aprobacion_brief`), L1355–1360 (raíz obligatoria) |
| 2. Ruta del caso | Flujo FL04 «activo directo sin preproducción» (D01–D05); técnica de persona, lugar o producto de FL02/FL03; operación del contrato (génesis, composición con referencias, edición) con sus campos y módulos | repo 2026-09-25, principios («Rostro T1 antes que cuerpo T2, siempre»; «producto con logo… es flujo con referencia») | taxonomía L248–263 (FL04; L263: con referencias no se llama génesis), F10 (T1 génesis sin referencias; T2–T4 ancla con referencias; T5 edición); `CONTRATOS_OPERACION_MODELO.json` L4–362 (campos por operación), L775–819 (módulos fotografía, acción física, sujetos visibles, materialidad); persona: `MAPA_PERSONA.md` (INV-000394–000397, 000474, 000604, 000610); producto con etiqueta real: INV-000465–000469; texto en imagen y edición: gpt-image.md (INV-002366–002385) |
| 3. Universo de reglas | Textos de generación de imágenes universales, parcialmente universales que incluyen GPT Image 2, y específicos de GPT Image 2 | 24 §1 (alcance, palabras de Eric del 2026-10-27); 26 §1 (cifra de GPT Image 2 manda; correcciones en `correcciones.json`) | 2,722 textos + adenda (SW30 SKILL.md y 18 reglas aprendidas) |
| 4. Selección | Por cada caso aprobado, las reglas cuya condición se cumple con sus facetas y su paso; resultado por regla APLICABLE CONFIRMADA, FUERA DE ESTE CASO o EXCLUIDA POR DECISIÓN, con traza de consulta | 24 §4 (método: universo → filtro por caso → controles → clasificación de lo pertinente → prueba del selector) | condición por facetas, binaria solo con el brief completo (taxonomía §7.2); §7.4 L2806–2816 (tres resultados; «top-k no acredita cobertura»; traza con caso, valores evaluados, descartes y motivo); dependencias de interfaz y versión con acción concreta (TRM-0683, TRM-0684) |
| 5. Redacción | GPT2-GEN de 5 slots o GPT2-EDIT Change/Preserve/Constraints; retratos con `armar.py`; génesis de persona con la plantilla T1; formato escrito en el texto; 300 palabras como techo editorial (advertencia, no bloqueo: DECISIONES.md decisión 2); salida Model / Quality / Size-Ratio / Prompt / Notes | CLAUDE.md (armar.py obligatorio; sin «photorealistic»); 26 §8 (formato en el texto; tamaño y quality como referencia) | gpt-image.md (5 slots, anti-slop, tamaños INV-002355–002365); INV-000604 / 000442 (plantilla T1); INV-002359 (máximo fiable); T-BRIEF-IMG L187–209, L355 (techo editorial histórico de GPT 1.5/2 = 300 palabras; «la longitud nunca se resuelve suprimiendo reglas aplicables»), L357–369 (salida común); taxonomía §6.2 (el vocabulario prohibido gana; la sintaxis final es la del modelo) |
| 6. Validación | Controles mecánicos antes de entregar; enlace de cada aplicación de regla con sus 12 campos | CLAUDE.md (nunca entregar un prompt rechazado) | `correr.py` y `armar.py`; `CONTRATOS_OPERACION_MODELO.json` L671–687 (`binding_contract`); T-BRIEF-IMG L377 (T-TRAZA), L381 (`verificar_templates.py` acredita estructura, no pertinencia) |
| 7. Generación | Eric genera en la app y entrega imagen y veredicto | 26 §8 | — |
| 8. Diagnóstico | Imagen mala → a, b o c, con la traza | 26 §9 (auditoría: 10 % de los «no aplica» de cada caso) | — |

## 3. Plan de trabajo, en orden

Cada tarea termina con un control que sale con código 1 si no se cumple.

1. **Adenda del universo.** Registrar SW30 SKILL.md y las 18 reglas aprendidas con id, archivo, líneas y sha256, sin
   tocar la base de 13,005. Leer completos los 30 informes de la raíz del zip y los casos de prueba de `repo/examples`;
   entra lo que sea regla original de generación de imágenes, sale lo derivado de las skills, con motivo.
   Control: cada texto de la adenda con veredicto y motivo.
   Hecha (2026-10-27): `v3/universo/adenda/construir_adenda.py` lee del zip `apd/originales/…v3.4.0_COMPLETE.zip` y
   escribe `adenda_universo.jsonl`: 125 textos de 68 archivos, 40 entran (21 de SW30 SKILL.md, las 18 reglas
   aprendidas con su condición y fuerza, 1 nota normativa del brief de ejemplo del clavadista) y 85 salen con motivo.
   Sale con código 0.
2. **Casos.** Rehacer B1–B5 con su ruta (rostro T1 → placa del lugar → T3) y B6 (T1 → T2, ya hecho); C1–C4 con su
   ruta. Cada paso lleva `ruta.flujo` FL04, su operación y los campos obligatorios de esa operación, los módulos que
   activa y `procedencia_campos` por valor (usuario, herencia aprobada, inferencia para aprobación o fuente
   documental). Después Eric aprueba cada brief
   completo por su sha256 (`aprobacion_brief`); sin esa aprobación no hay selección definitiva. Control: cada caso
   valida contra `CONTRATO_IMAGEN_ORQUESTACION.schema.json` y los `required_fields` de su operación; `correr.py` sin
   fallas; formato en el texto de cada prompt.
3. **Lista de referencia por caso (pregunta a).** Leer cada texto del universo contra cada caso y marcar APLICABLE
   CONFIRMADA, FUERA DE ESTE CASO o EXCLUIDA POR DECISIÓN con motivo (taxonomía §7.4), sin mirar facetas ni selector.
   El «no aplica» de la decisión 26 §9 es FUERA DE ESTE CASO. Control: `rule_answer_check.py` adaptado a ids INV, 0
   sin veredicto, 0 contradicciones.
4. **Clasificación de lo pertinente.** Clasificar en facetas, con el método del piloto (matriz + verificador), solo
   los textos que aplican a algún caso. Control: `validar_v2.py` sin fallas; etiquetas 100 % de la taxonomía.
5. **Selector y cruce.** Correr el selector sobre la clasificación de los casos aprobados y cruzar con la lista del
   paso 3. La traza de consulta registra caso, valores evaluados, descartes por aplicación y motivo. Control: 0 reglas
   de la referencia sin seleccionar.
6. **Traza por regla (pregunta b).** Por cada aplicación de regla seleccionada, los 12 campos del `binding_contract`:
   regla_id, aplicacion_id, item_taxonomia_ids, fuente_literal, documento, encabezado, pagina, condicion, campo_brief,
   efecto, destino (el slot donde se cumple) y prueba (el control que la verifica). Control: 0 aplicaciones con un
   campo vacío.
7. **Entrega a Eric.** Prompts listos con la salida común (Model / Quality / Size-Ratio / Prompt / Notes), su orden y
   las imágenes que hay que adjuntar en cada paso.
8. **Diagnóstico.** Con las imágenes y el veredicto de Eric. Si una imagen sale mal, Eric genera el mismo prompt por lo
   menos dos veces más antes de auditar (decisión 26 §10): una muestra mala del generador no es falla del prompt
   (INV-010355, «Budget 2–3 re-rolls»; INV-010387). Solo la falla que se repite se diagnostica: a si la regla que la evita está en la lista de
   referencia y el selector no la tomó; b si se tomó y el prompt no la cumple según su traza; c si a y b pasan. Así
   ninguna falla queda sin veredicto. La certeza de a depende de la lista de referencia, que se verifica con la muestra
   de auditoría del 10 % (decisión 26 §9).

## 4. Dudas que solo Eric puede resolver

Ninguna. Las dos lecturas de `MAPA_PERSONA.md` (el «maestro con luz pareja» es la referencia de personaje para video;
el look del brief va en el T3) salen de los textos citados ahí.
