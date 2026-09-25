# Aurora Prompt Linter — copia parcheada (v1.2-fupai)

Copia del linter del skill `aurora-prompt-linter` (v1.1, 2026-05-27) con el vocabulario
ampliado y las contradicciones con el resto del pipeline resueltas **a favor de la fuente**.
El original no se toca; vive en
`~/.claude/skills/synced/<id>/aurora-prompt-linter/scripts/` y sigue siendo la referencia
de la CLI. Esta copia conserva la misma interfaz (`--prompt --refs --case --platform --vocab
--overrides --sports-broadcast --json`), los mismos exit codes (`0` PASS, `1` FAIL, `2` uso)
y añade tres opciones: `--ref-role`, `--series-lock`, `--treatment`.

```
.claude/hooks/aurora/
├── prompt_linter.py      # copia parcheada; cabecera con changelog P1..P12 y fuente por parche
├── vocabularies.yaml     # vocabulario ampliado; se carga por defecto (o con --vocab)
├── README.md             # este archivo
└── tests/
    ├── run.sh            # 18 pruebas; exit 0 si todas pasan
    └── fixtures/         # prompts, refs, series_lock y mensaje de override
```

Requisitos: Python 3.11 y `pyyaml`. Nada más.

## Por qué existe esta copia

El linter original es la única pieza del pipeline que convierte "no re-describir lo que está en
la referencia" en código. Eso es valioso y se conserva íntegro. El problema es que fue
calibrado para un flujo anterior (system v6.0, casos Aurora de ciclismo/fútbol) y, leído
junto a los skills que hoy gobiernan la producción (`video`, `image`, `visual-prompt-forge`,
`produccion-visual-sw30`, `ai-production-director`), **bloquea prompts que esos skills exigen**
y **deja pasar palabras que esos skills prohíben**. Las doce contradicciones están abajo, con
el parche que las resuelve y la fuente que lo sustenta. Ninguna decisión es de criterio del
agente: cada fila cita el archivo y la sección.

## Contradicción → parche → fuente

| # | Contradicción detectada | Parche en esta copia | Fuente que lo sustenta |
|---|---|---|---|
| 1 | **Presupuesto de palabras.** El original hace HARD FAIL por encima de 130 (T2I) o 90 (I2V). SW30 canoniza un maestro de rostro T1 de ~250 palabras; GPT Image tolera 150–300; Kling 3.0 "structure beats length". | P1 — el conteo **nunca bloquea**: WARN con el presupuesto por plataforma (tabla `WORD_BUDGET_BY_PLATFORM`) y el techo de `_capabilities.json`. Si la plataforma no está en la tabla, el presupuesto original del caso se reporta como referencia, también WARN. | forge `adapters/_capabilities.json` ("`max_prompt_words` is a ceiling, not a target"); rangos de cada adaptador (kling/veo/flux/seedance 80–150, gpt-image 150–300, nano-banana/ideogram/hailuo 60–120, midjourney 40–80, seedream 40–70); `kling.md` §5 y §10 (I2V 20–40); `veo.md` §3 (50–200) y §9; SW30 "Template canónico T1 … alrededor de 250 palabras". |
| 2 | **Negativo obligatorio.** El original exige bloque `Negative:` en todos los casos y plataformas. Nano Banana, Veo, Flux, Hailuo no tienen campo negativo; `image` manda positive framing; GPT Image usa el slot `Constraints:`. | P2 — `NEGATIVE_BLOCK_POLICY`: **required** solo en Kling y Seedance 2.5; `Constraints:` cuenta como bloque negativo en GPT Image; en el resto no se exige (si aparece con marcador `Negative:` en NB/GPT/Veo/Flux se avisa). Si el bloque existe se valida SW30 R16: sin "no X" en Kling y ≤8 ítems → WARN. Sin `--platform` se mantiene el comportamiento v1.1 (required) con WARN. | `universal-rules.md` U1 ("Negative constraints — only if the model supports them"); `kling.md` §6 ("dedicated negative prompts field … Do not write 'no X' … Keep the list short"); `seedance-25.md` §7 y §19-A (`[Negative Prompts]`); `seedance.md` §12 (1.x/2.0 sin soporte fiable); `veo.md` §7; `image/golden-rules.md` §2; `image/gpt-image.md` "5 slots" (Constraints); SW30 R16 ("negativos sin 'no X', ≤8 ítems"). |
| 3 | **Identity block por rol de la referencia.** El original banea los descriptores P/O siempre que un ref cargue P/O. En I2V eso es correcto (no re-describir el first frame). En caso 2 con refs `@img1` / Elements / `Image 1` es al revés: U7 y Seedance §10 **exigen** el identity block completo junto a la referencia. | P3 — `--ref-role {ff,lf,character,location,prop,style}` (si no se pasa, se deriva del campo `role` de `refs.yaml` y del caso). Con **ff/lf** los descriptores P/O siguen prohibidos. Con **character** se permiten y el identity block es obligatorio: si faltan ≥3 de {pelo, ojos/piel, prenda, accesorio, rasgo distintivo} → WARN "identity block absent". | `kling.md` §3 ("Describe how the scene evolves from the image, not what is in the image") y §10; `veo.md` §7 ("Do not re-describe static elements"); `seedance.md` §13; SW30 R5 y R16; `universal-rules.md` U7 ("Identity block must include: face shape, eye color, skin tone. Hair … Exact clothing items. Distinctive accessories"); `seedance.md` §10 ("The full identity block must follow the @img1 mention"); forge SKILL.md Rule 3 y `consistency-locks.md` Lock 1. |
| 4 | **series_lock verbatim vs L.** Forge Rule 3 exige que `environment`/`lighting`/`color_grade` aparezcan **verbatim** en cada prompt y `validate_prompts.py` bloquea si faltan. El original banea "gym", "polished light wood floor", "floor-to-ceiling windows" cuando L está cubierta: un validador exige lo que el otro castiga. | P4 — `--series-lock <json|yaml>`: todo término del vocabulario de redundancia que caiga dentro de una de esas cadenas exactas queda exento. Si una cadena no aparece verbatim se avisa (WARN), porque `validate_prompts.py` la bloqueará. | forge SKILL.md Rule 3 ("flow into every prompt **verbatim** … no synonym, no inserted adjective"); `tools/validate_prompts.py` check 7; `references/consistency-locks.md` Locks 1–3 y 8. |
| 5 | **Micro-acción corporal.** El original lista `sweat`, `sweaty`, `jawline` en P: con un ref de persona quedan prohibidos. La Ley de Detalles obliga a que cada shot tenga una micro-acción física ("Jaw locks. Knuckles whiten. He swallows hard"). | P5 — salen de P y existe `BODY_MICRO_ACTION_EXEMPT` (sweat, sweat bead, sweaty, jaw, jawline, knuckles, breath, exhale, swallow, tendon, vein, blink) que el código respeta aunque un vocab custom los reintroduzca. | `dramaturgy.md` §2 "Physical micro-action on the body"; `universal-rules.md` §1 (Details Law) y U3; `race-and-speed.md` §1 ley 2 ("feeling renders only on a knuckle … or a sweat bead") y §7 ("sweat reads as discrete specular dots"). |
| 6 | **"cinematic" requerido vs prohibido.** El original lo pone en S (se banea solo si hay ref de estilo) **y** lo usa como patrón que satisface la sección `style` en 6 snapshots. El director §6.1 dice que el vocabulario prohibido de dramaturgy "gana siempre". | P6 — `cinematic` sale de S y de **todos** los patrones de secciones; entra en `BANNED` con professional, high quality, masterpiece, stunning, epic, amazing, beautiful lighting, dynamic camera, intense moment, powerful scene, incredible, gorgeous. Una mención negada ("no cartoon") no cuenta (P11). | `ai-production-director/SKILL.md` §6.1; `dramaturgy.md` §2 "What is banned"; `universal-rules.md` §1 y U12; `image/gpt-image.md` Anti-Slop (stunning, incredible, epic, gorgeous, masterpiece); `models.md` ("Anti-slop: вредит" en GPT Image 2). |
| 7 | **slow motion.** BANNED global en el original. `kling.md` lo recomienda como técnica anti-morphing y define "ultra-slow motion" como palabra de tempo que el modelo obedece; `race-and-speed` lo prohíbe de verdad (ley 1). | P7 — deja de ser BANNED global: **WARN** en fotorreal/ilustración/animación (pide causa), **FAIL** con `--treatment race`, **permitido sin aviso** con prefijo `ultra-` o con `OVERRIDE: slow motion - <razón>`. | `kling.md` §3 tempo words ("ultra-slow motion (2-3s feel)") y §11 ("Generate the action in slow motion and speed it up in post"); `dramaturgy.md` §7 (toda decisión de cámara con razón); `race-and-speed.md` §1 ley 1 ("never CGI-clean or sped-up … Over-crank … drain all threat"). |
| 8 | **anime / cartoon / 3D render.** BANNED global en el original. Los patterns del skill `image` los usan de forma legítima (character cards anime, grids Pixar-style). | P7 — `--treatment {fotorreal,ilustracion,animacion,race}` (default fotorreal). `STYLE_BANNED_FOTORREAL` solo aplica en fotorreal/race. En ilustración/animación además se sustituyen los patrones de la sección `style` (`TREATMENT_SECTION_OVERRIDES`) y se retira `anti_style`. | `image/references/patterns/character-design.md` ("Anime-Style Character Card", "clean cel-shaded anime"); `multi-panel.md` ("Pixar-style 3D", "anime cel shading"); `editing.md` ("vibrant anime"); `dimensional.md` ("photorealistic 3D render"). |
| 9 | **Flag broadcast en stills.** `--sports-broadcast` exige `60fps` y `broadcast realism` también en casos 1 y 2 (imagen), donde "60fps" no significa nada y SW30 prohíbe cualquier idea de movimiento. | P8 — en casos 1/2 el flag se ignora con WARN explicativo; en 3a/3b/3c/4 sigue siendo FAIL si faltan las keywords. | `kling.md` §2 ("up to 60 fps" es especificación de video); SW30 R8 ("Stills en instante congelado; nada de movimiento en imagen fija"); Regla 26 v6.0 (origen del flag) habla de clips. |
| 10 | **Presupuesto I2V Veo/Seedance.** El original aplica 50–90 a todo I2V. Veo tiene sweet spot 50–200 y comprime a 50–100; Seedance no fija número y su skeleton de 11 bloques supera cualquier techo; Kling I2V es 20–40. | P1 — presupuesto `i2v` por familia: Kling 20–40, Veo 50–100; Seedance usa el rango del adaptador (80–150) como única cifra disponible y lo declara en `source`. Todo WARN. | `kling.md` §5 y §10; `veo.md` §3 y §9; `seedance.md` §6 y §13; `seedance-25.md` §19 (ejemplos oficiales largos); forge `adapters/seedance.md`. |
| 11 | **S vs secciones requeridas.** Con un ref de estilo, `photorealistic/documentary/editorial` quedan prohibidos en MAIN y a la vez la sección `style` exige exactamente una de esas palabras: imposible de satisfacer. | P12 — si S está cubierta por refs, la sección `style` se **dispensa** y se reporta como WARN informativo. | `universal-rules.md` U13 ("Do not restate what a reference already defines"); `seedance-25.md` §5; `consistency-locks.md` Lock 6 (style refs). |
| 12 | **Plataformas omitidas.** Snapshots solo para gpt_image_2, midjourney, nano_banana_pro, kling_3.0, veo_3.1, sora_2. Forge produce prompts para flux, ideogram, seedream, hailuo, seedance; el pipeline usa nano_banana_2 y seedance_2.5. Sin snapshot, el linter opera en "honor system". | P10 — snapshots nuevos: `flux__1`, `ideogram__1`, `seedream__1`, `nano_banana_2__1/__2`, `seedance__3a`, `seedance_2.5__3a/__3b/__4`, `hailuo__3a`, `kling_3.0__4`. Resolución por familia (`--platform kling` → `kling_3.0`, `seedance_2.5` → su propio snapshot). Reconoce `Negative field.`, `[Negative Prompts]`, `Constraints:`. Vocabulario L/PR/O ampliado a agua, automotriz, café/interior, clima y música. | forge `adapters/*.md` (patrón de composición de cada uno); `kling.md` §3 (protocolo P1–P4 y `Shot N (t)`); `seedance-25.md` §3–§7, §16; `seedance.md` §13–§14; `veo.md` §10; `image/models.md` (NB2 mismo estilo que NBP). |

## Qué NO cambió

- La capa 1 (redundancia con refs por categoría P/O/L/PR/S) sigue bloqueando exactamente igual
  cuando el rol es ff/lf. Es la razón de ser del linter y se conserva.
- Las secciones requeridas siguen bloqueando (salvo los dispensados por P12 y los overrides
  por tratamiento).
- El vocabulario prohibido sigue bloqueando; ahora es más largo, no más corto.
- El mecanismo `OVERRIDE: <término-o-categoría> - <razón>` es idéntico: solo el turno actual,
  solo con scope específico.
- Exenciones de contexto de cámara y anclas direccionales: idénticas.
- `--json`: misma salida con las claves originales intactas; se añaden `case_alias`,
  `treatment`, `ref_role`, `ref_role_source`, `word_budget_source`, `negative_policy`,
  `negative_marker`, `series_lock_keys`, `linter_version`.

## Uso

```bash
python3 .claude/hooks/aurora/prompt_linter.py \
  --prompt draft.txt --refs refs.yaml --case CLIP-FF --platform kling_3.0 \
  --ref-role ff --series-lock series_lock.json --treatment fotorreal \
  --overrides user_msg.txt [--sports-broadcast] [--json]
```

### Mapeo de casos (P9)

| Del pipeline | Linter | Etapa del director | Notas |
|---|---|---|---|
| `T1`, `T2`, `PLACA` / `PLATE`, `GENESIS` | `1` | Etapa 5 (anchors) | maestro de rostro, maestro de cuerpo, placa vacía (SW30 R7) — sin refs |
| `T3`, `T4`, `T5`, `ANCLA` / `ANCHOR` | `2` | Etapa 5 | cuadro 1 persona, 2 personas, edición quirúrgica — con refs `Image N` / `@img` |
| `CLIP-FF`, `CLIP`, `I2V`, `CLIP-I2V` | `3a` | Etapa 6 (video prompts) | image-to-video con first frame |
| `CLIP-FF-LF`, `CLIP-LF`, `CLIP-TAIL` | `3b` | Etapa 6 | first + tail image (Kling start/tail; Seedance 2.5 first & last) |
| `CLIP-MC`, `CLIP-MOTION`, `MOTION-CONTROL` | `3c` | Etapa 6 | Kling Motion Control (§9) |
| `CLIP-DIALOGO`, `CLIP-DIALOG`, `CLIP-DIALOGUE` | `4` | Etapa 6 | Kling 3.0 P1–P4, Veo `Says:`, Seedance 2.5 `{ }` |

Mayúsculas, guiones y guiones bajos son indiferentes. Un alias desconocido sale con `2`.

### Rol de la referencia (P3)

| `--ref-role` | Descriptores P/O en MAIN | Identity block | Cuándo |
|---|---|---|---|
| `ff` / `lf` | **prohibidos** (FAIL) | no aplica | casos 3a/3b/3c/4: la imagen ancla identidad y wardrobe |
| `character` | permitidos | **obligatorio** (WARN si <3 grupos) | caso 2 con `Image 1: face`, `@img1`, Elements, `--cref` |
| `location` / `prop` / `style` | permitidos (WARN si además hay tags P/O) | no aplica | refs que no son de persona; L/PR/S se rigen por sus tags |

Si no se pasa, se deriva del campo `role` de `refs.yaml` (`FF`, `LF`, `TAIL`, `CHARACTER`,
`ELEMENT`, `IMG`…) y, en su defecto, del caso (video → ff; 1/2 → character).

### Tratamiento (P7)

`--treatment fotorreal` (default) banea anime/cartoon/3D render y avisa sobre slow motion.
`ilustracion` y `animacion` levantan esos bans y ajustan la sección `style`. `race` mantiene
los bans fotorreal y convierte slow motion en FAIL (`race-and-speed.md` ley 1).

## Invocación desde el pipeline

El director (`ai-production-director`) nombra al linter como "gate final" con "veto final
sobre prompts" (§1) y lo exige en la Etapa 6; la Etapa 5 lo recomienda. Con esta copia:

### Etapa 5 — imágenes ancla (casos 1 y 2)

1. `refs.yaml` se escribe desde el plan de anchors: cada referencia con `role` (`CHARACTER`,
   `LOCATION`, `PROP`, `STYLE`) y `tags` (`P1`, `O1`, `L1`, `PR1`, `S1`).
2. `series_lock.json` se extrae de `shots.json` (`series_lock.character/environment/
   lighting/color_grade`) — son las mismas cadenas que forge exige verbatim.
3. Se ejecuta por prompt, con el caso SW30 tal cual (`--case T1`, `--case T3`) y la
   plataforma del header `Model:` del skill `image` (`nano_banana_pro`, `nano_banana_2`,
   `gpt_image_2`).

```bash
python3 .claude/hooks/aurora/prompt_linter.py \
  --prompt out/anchors/T3_shot_04.txt --refs out/anchors/refs_shot_04.yaml \
  --case T3 --platform nano_banana_pro --ref-role character \
  --series-lock out/series_lock.json --overrides /tmp/user_turn.txt
```

Exit `0` → se entrega con el reporte adjunto (trazabilidad, SKILL.md del linter §"Interpretar el
resultado"). Exit `1` → no se entrega; se itera. Los WARN de palabras se leen junto al techo
del adaptador, no se "arreglan" recortando el T1.

### Etapa 6 — prompts de video (casos 3 y 4)

1. `refs.yaml` con la imagen aprobada como `role: FF` (y `LF`/`TAIL` si hay tail image),
   tags de lo que esa imagen ya fija — normalmente `P`, `O`, `L`, `PR`.
2. Plataforma del archivo de modelo destino (`kling_3.0`, `veo_3.1`, `seedance_2.5`, `hailuo`).
3. `--treatment race` en spots de velocidad; `--sports-broadcast` solo si aplica la Regla 26.

```bash
python3 .claude/hooks/aurora/prompt_linter.py \
  --prompt out/clips/shot_04_kling.txt --refs out/clips/refs_shot_04.yaml \
  --case CLIP-FF-LF --platform kling_3.0 --series-lock out/series_lock.json \
  --overrides /tmp/user_turn.txt
```

El gate de la Etapa 6 sigue siendo doble: los dos checks de `video` (dramaturgy check de 6
puntos + auditoría de 3 detalles) **y** este linter limpio.

## Cómo se cablearía como hook `Stop` (no está cableado)

Los tres gates `Stop` del repo (`gate_microgate.py`, `gate_dramaturgy.py`, `gate_image.py`)
comparten el mismo esqueleto: leen el payload JSON del hook por stdin, abren el transcript,
toman el último mensaje del asistente, extraen los bloques cercados que `prompt_detect.
visual_blocks()` clasifica como entrega de prompt visual, y devuelven `exit 2` con el motivo
en stderr para que el turno no cierre. Un `gate_aurora.py` haría lo mismo delegando en este
linter:

1. **Entrada**: para cada bloque visual detectado, escribir el bloque a un archivo temporal
   (`--prompt`) y el último mensaje del usuario a otro (`--overrides`), igual que hoy hace
   `gate_dramaturgy.py` con los `OVERRIDE:`.
2. **Caso y plataforma**: leer del propio bloque o de sus líneas inmediatas la cabecera que el
   pipeline ya obliga a emitir — `Model:` del skill `image` (→ `--platform`), el tipo SW30
   (`T1..T5`) o el `shot_NN` + `CLIP-*` de la Etapa 6 (→ `--case`). Si no se resuelve, el gate
   **no opina** (mismo default de `prompt_detect.py`: "un gate que bloquea texto que no es un
   prompt se desactiva a la semana").
3. **Refs y series_lock**: `refs.yaml` y `series_lock.json` del run activo (`output/` del
   storyboard-architect); si no existen, correr sin refs y avisar en stderr que la capa 1 no
   se aplicó.
4. **Semántica de salida**: linter `1` → hook `exit 2` con el reporte; linter `0` → `exit 0`
   (los WARN se dejan pasar al transcript por stderr sin bloquear).
5. **Registro en `settings.json`**: una entrada más en `hooks.Stop`, después de
   `gate_dramaturgy.py`:

   ```json
   {
     "type": "command",
     "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/gate_aurora.py\"",
     "timeout": 30,
     "statusMessage": "Aurora linter: redundancia, secciones, vocabulario..."
   }
   ```

6. **Anti-bucle**: reutilizar el contador por sesión de `gate_dramaturgy.py`
   (`MAX_CONSECUTIVE_BLOCKS = 3`) para que un prompt imposible no deje el turno colgado.

Nada de esto está hecho. Esta copia es la herramienta invocable a mano y desde el pipeline;
el hook es el siguiente paso, cuando el cableado de caso/plataforma desde la cabecera esté
validado en sesiones reales.

## Pruebas

```bash
bash .claude/hooks/aurora/tests/run.sh           # 18 pruebas, exit 0 si pasan todas
VERBOSE=1 bash .claude/hooks/aurora/tests/run.sh # con la salida completa de cada una
```

| # | Qué reproduce | Parche |
|---|---|---|
| T01 | T1 SW30 de ~250 palabras en nano_banana_pro caso 1 → exit 0 con WARN de palabras | P1 |
| T02 | GPT Image 2 con `Constraints:` y sin `Negative:` caso 1 → exit 0 | P2 |
| T03 | Kling caso 3a sin bloque negativo → exit 1 | P2 |
| T04 / T04b | Caso 2 `--ref-role character` con identity block → exit 0 y descriptores P permitidos; sin identity block → exit 0 con WARN | P3 |
| T05 | Caso 3a `--ref-role ff` con descriptores P → exit 1 | P3 |
| T06 / T06b | `--series-lock` con "gym" y prompt con "gym" verbatim → exit 0; el mismo prompt sin series-lock → exit 1 `FAIL [L] 'gym'` | P4 |
| T07 | "her jaw locks, sweat beads" con ref P rol ff → exit 0 | P5 |
| T08 | "cinematic" → exit 1 | P6 |
| T09 | "anime" con `--treatment ilustracion` → exit 0; fotorreal → exit 1 | P7 |
| T10 | "ultra-slow motion" Kling → exit 0 sin WARN; "slow motion" `--treatment race` → exit 1; fotorreal → WARN | P7 |
| T11 | `--sports-broadcast` en caso 1 → exit 0 con WARN | P8 |
| T12 | `--case T1` → 1, `CLIP-FF` → 3a, `CLIP-DIALOGO` → 4 (snapshot `kling_3.0__4`); alias desconocido → exit 2 | P9, P10 |
| T13 | Negativo Kling con "no blur" y 10 ítems → exit 0 con dos WARN R16 | P2 |
| T14 | GOOD del README del skill pasa (con y sin `--platform`), BAD falla con las mismas violaciones y overrides aceptados; ya no falla por longitud | todos |
| T15 | `--json` sigue produciendo las claves originales | — |
| T16 | Ref con S y prompt sin palabras de estilo → exit 0 con la sección `style` dispensada; sin ref S → exit 1 | P12 |

Los fixtures `prompt_GOOD.txt`, `prompt_BAD.txt`, `refs_session.yaml` y `override_msg.txt`
se reconstruyeron según `references/README.md` del skill, porque el paquete instalado no
trae los `test_*` que ese README lista.

## Decisiones tomadas fuera de la spec (y la alternativa descartada)

1. **Sin `--platform`, el negativo sigue siendo obligatorio** (política `legacy_required`,
   con WARN). Alternativa descartada: hacerlo opcional por defecto. Se descartó porque el
   SKILL.md original invoca el linter sin plataforma y su README promete "Negative prompt:
   bloque obligatorio"; sin plataforma no hay forma de aplicar U1, y relajar en silencio
   habría cambiado el contrato del original.
2. **La exención de series_lock no cubre `BANNED`.** Alternativa descartada: eximir
   "cualquier término del vocabulario", literal. Se descartó porque el director §6.1 dice que
   el vocabulario prohibido gana siempre; un `color_grade: "cinematic teal"` no debe colar
   "cinematic". Solo se eximen P/O/L/PR/S.
3. **La regla "sin 'no X'" del negativo solo se aplica a Kling.** Alternativa descartada:
   aplicarla a todo bloque negativo. Se descartó porque `seedance-25.md` §7 y §19-A muestran
   que en Seedance 2.5 el formato oficial de `[Negative Prompts]` **es** "no X". El ≤8 ítems sí
   aplica a todas (SW30 R16 habla de clips en general).
4. **Mención negada no dispara BANNED ni bans de estilo** (P11: "no cartoon", "not anime").
   Alternativa descartada: flaggear igual y obligar a moverlo al negativo. Se descartó porque
   el propio snapshot `gpt_image_2__1` del original exige "no cartoon, no anime" en MAIN como
   patrón de `anti_style`; el linter se contradecía a sí mismo.
5. **La sección `style` se dispensa cuando S está cubierta** (P12). Alternativa descartada:
   sacar `photorealistic/documentary/editorial` de S. Se descartó porque eso vacía la categoría
   S y U13 es explícito en que lo que define la referencia no se restata.
6. **`--treatment race` existe como cuarto valor** aunque la spec lo enuncia como
   `{fotorreal,ilustracion,animacion}`: la spec misma pide "salvo `--treatment race`" para slow
   motion, y no hay otra forma de expresarlo. `race` hereda los bans de fotorreal.
7. **Presupuesto de Seedance 2.5**: se usa 80–150 del adaptador de Seedance 2.0 con la nota
   de que `seedance-25.md` no fija cifra y sus ejemplos oficiales la superan. Alternativa
   descartada: inventar un rango "razonable" para 30 s; SW30 R19 prohíbe afirmar límites de
   plataforma sin fuente.
8. **Alias desconocido de `--case` → exit 2** (error de uso), no un reporte FAIL. Alternativa
   descartada: exit 1 con "Unknown case". Se descartó porque el original usaba `choices=` de
   argparse, cuyo contrato ya era exit 2; se conserva.
9. **Vocabulario nuevo evita términos de una sola palabra con colisión conocida**: no se
   añadió `stage` a secas (rompería `[Stage 1]` de Seedance 2.5), ni `counter`
   (`counter-steer`), ni `cup` (`World Cup`); se usaron formas compuestas (`concert stage`,
   `bar counter`, `coffee cup`). Alternativa descartada: añadirlos y confiar en la exención
   direccional, que no cubre esos contextos.
10. **`--ref-role location/prop/style` no altera P/O** y solo avisa si los refs traen tags
    P/O. Alternativa descartada: tratar esos roles como `character`. Se descartó porque el
    identity block de U7 no tiene sentido para una placa o un prop.
