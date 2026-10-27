# Revisión de las citas de `PLAN_FINAL_PRUEBA.md` (versión del commit 0ced62a) — 2026-10-27

Método: para cada cita, leer el texto citado en su archivo, con su sección y lo que hace el archivo, y compararlo con lo
que el plan afirma. Ids INV y ADD: 168 entradas extraídas del plan con prefijo y 15 más citadas como número suelto
(listado completo con texto en el scratchpad de la sesión, regenerable desde el plan y el universo). Las otras citas:
decisiones 23, 24, 26; DEC-000004, 000009, 000024, 000025; T-BRIEF-IMG; schema; CONTRATOS; `verificar_templates.py`;
taxonomía 00688; PILOTO; directivas; DECISIONES.md; CLAUDE.md; `armar.py`; `image/SKILL.md`; `vision-decomposer.md`;
`CONTRADICCIONES.md`.

## A. Citas correctas (dicen lo que el plan les atribuye)

| Cita del plan | Verificado contra |
|---|---|
| Génesis, técnica FL02 E5.2 = INV-000525–000614 | `flujo-spot.html:460–638` «Génesis sin referencias, paso a paso» hasta «Consecuencia para la base de reglas»; 529, 542, 543 y 546 no están en el universo |
| 0 referencias (INV-000610); clase de sujeto (INV-000539, 000593); persona T1 (000604, 000553, 000558, 000561); lugar (000607, 000555, 000560); producto (000606, 000554, 000559, 000611); objeto (000608) | textos leídos uno por uno: coinciden |
| Composición: INV-000395, 000396, 000428, 000474, 000486–000487, 000490, 000508–000512, 000590, 000203 | E5.3, E5.4, pasos T2 y mundos por dos pasos, EN.4 de una sola generación |
| Edición: INV-000397, 000584–000585, 002021 | E5.5; editar, no re-tirar; carga de `editing.md` |
| Transferencia: INV-002386–002390, 002294–002295 | `gpt-image.md:102–113`; `golden-rules.md:119–120` |
| Boceto: INV-002025 | `image/SKILL.md:61` |
| Ancla: FL03 A0–A12 = INV-000069–000118 | `flujo-anclas.html:134` (A0) a `:232` (A12) |
| INV-002044 (formato de salida), INV-002335 (5 slots), INV-002054 (corregido, 16 refs) | `image/SKILL.md:88`; `gpt-image.md:9`; `characters.md:3` con la corrección de 26 §1 |
| ADD-0004, 0006, 0007, 0008, 0010, 0011, 0029, 0030, 0031, 0042, 0043, 0047, 0053 | textos de la adenda: coinciden |
| Decisiones 23 §3, §4, §5, §6; 24 §1, §4; 26 §1, §8, §9, §10, §11 | `DECISIONES_ERIC_20261023.md`, `…20261024.md`, `…20261026.md` |
| DEC-000004, 000009, 000024, 000025 | `01062_registro_decisiones_DOC01.md:14`, `:30`, `:81`, `:84` |
| T-BRIEF-IMG L13–15 y L355 | pasos 4–6 (aprobación ligada al hash) y techos editoriales |
| schema L45–54 (8 operaciones) y L1333–1352 (`aprobacion_brief`) | `CONTRATO_IMAGEN_ORQUESTACION.schema.json` |
| CONTRATOS L4–362, L671–687, L775–819 | `operation_contracts`, `binding_contract` (12 campos), `conditional_modules` |
| `verificar_templates.py` L43 (D1–D9 en ancla) y L65 (el prompt empieza por el primer slot) | líneas exactas |
| taxonomía L257–261 (FL04 D01–D05), L263, §7.2 (L2798), §7.3, §7.4 | 00688 |
| PILOTO §0.4, §5 (último párrafo: aprobación ligada al hash), §6.1 | `PILOTO_V5_INSTRUCCIONES_20261019.md` |
| ERIC-IDIOMA-PROMPT-INGLES; prohibición de «photorealistic» y «fotorealista» | `directivas_taller.json:3`; `user_directives.json:17–22`; CLAUDE.md:16 |
| Decisión 2026-10-11 16:56:54 (F26–F28 contexto del clip) | `01022_DELTA…:205–212` |
| `armar.py` L84–85; `vision-decomposer.md:1–3`, `:61`, `:93`; DECISIONES.md decisión 2 | líneas exactas |

## B. Citas o afirmaciones que el plan tiene que corregir

1. **§1 «El alcance no cambia».** Cambió: decisión 26 §12 (solo imagen fotográfica, cada tipo con caso propio).
2. **§3 génesis: «Edificación, animal y planta … fuera del alcance».** Contradice 26 §12. INV-000605 e INV-000591 mandan
   el sujeto fiel a algo real al grounding de Nano Banana 2; la prueba es solo GPT Image 2 (23 §6), así que esa parte de
   la ruta queda EXCLUIDA POR DECISIÓN y los tres sujetos entran con GPT Image 2.
3. **§3: «Todos los casos llevan F32 "sin texto"».** Error: ver `01_texto_en_imagen.md`. Entran texto corto y texto
   extenso o pequeño dentro del mundo fotografiado.
4. **§3: «análisis de imagen a prompt … no tiene caso propio».** Contradice 26 §12 («descripción de imagen … tiene que
   tener una prueba específica»). Además, taxonomía L260 (FL04 D03): «Un modo sin contrato original suficiente
   permanece no habilitado», y el contrato no tiene esa operación (schema L45–54). Ver `04_preguntas_eric.md`.
5. **§3 boceto a final: solo `structural.md`.** F10 «boceto o wireframe a final» cubre `image/structural` e
   `image/dimensional` (definición en el esquema); falta `dimensional.md` (INV-002026, `image/SKILL.md:62`).
6. **§3 edición: un solo tipo.** Faltan los 8 hijos de F10 (decisión 23 §4).
7. **§2 «… el generador no conserva estado | INV-012218; cierra CONTRADICCIONES §4».** INV-012218
   (`consistency-locks.md:3`) habla de prompts de un storyboard. El chat nuevo por prompt evita depender del dato que
   falta en §4; no lo cierra. Redactar así.
8. **§2 falta la decisión 23 §7:** quality la elige el usuario; high es obligatorio donde la fuente lo exige.
9. **§2 «el vocabulario prohibido gana | taxonomía §6.2».** Precisar: §6.2 fila 1 (INV-000698), vocabulario de prompts.
10. **Persona: falta la decisión 24 §3** (reglas de lente y cámara para que la cara no se deforme, buscadas leyendo).
11. **§4 K08 es ilustración:** fuera de la prueba por 26 §12; solo sirve como entrada de K09.
12. **§4 casos:** hay que rehacerlos para que cada tipo fotográfico tenga su caso (ver `02_facetas_tipo_imagen.md`).
