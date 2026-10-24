# IMAGEN — todas las reglas, divididas rama por rama

**956 reglas de imagen.** Las de video quedaron fuera por evaluación mecánica del `when` de cada regla con `media=image`.

## TODAS LAS RAMAS — 642 reglas

No nombran ninguna categoría: se aplican a cualquier imagen, con o sin referencia, con o sin personas. Se listan aquí una vez y **no se repiten abajo**; cada rama de abajo las lleva además de las suyas.

  - `ai-production-director/SKILL.md:106` [GATE] — - **Gate:** checklist maestro de la referencia completo; trazabilidad verificada (muestreo: 3 prompts al azar trazan hasta su concepto).
  - `ai-production-director/SKILL.md:110` [GATE] — - Al cerrar cada gate, entrega el artefacto de la etapa y anuncia la siguiente en una línea. En STANDARD/FILM, los gates 1 (selección de concepto), 2 
  - `ai-production-director/SKILL.md:111` [RECOMMEND] — - En EXPRESS, solo el shot list requiere OK antes de escribir prompts.
  - `ai-production-director/SKILL.md:112` [FORBID] — - Nunca preguntes lo que el brief o los artefactos previos ya responden.
  - `ai-production-director/SKILL.md:120` [RECOMMEND] — Estas reglas son decisiones tomadas. Aplícalas sin reabrir el debate en medio de un proyecto.
  - `ai-production-director/SKILL.md:129` [FORBID] — De la Etapa 4 en adelante: `shots.json`. Un cambio creativo se hace primero en shots.json y se propaga hacia abajo; nunca se parcha un prompt de forma
  - `ai-production-director/SKILL.md:132` [REQUIRE] — `visual-prompt-forge` es dueño del **flujo de datos** (shots.json → borrador, critique.json → revisión selectiva). `video`/`image` smixs son dueños de
  - `ai-production-director/SKILL.md:135` [REQUIRE] — Todo entregable que use la capa smixs conserva la línea: *Serge Shima — github.com/smixs/visual-skills* (CC BY 4.0, obligatorio, incluye derivados gen
  - `ai-production-director/SKILL.md:139` [RECOMMEND] — `visual-media` NO participa en el pipeline live-action: todo lo que cubre (composición, tipos de plano, luz, movimientos de cámara, ritmo de edición) 
  - `ai-production-director/SKILL.md:141` [RECOMMEND] — 1. **Proyectos de animación** (2D/3D/motion graphics): es la única skill instalada con los 12 principios de Disney y el flujo de producción de animaci
  - `ai-production-director/SKILL.md:142` [RECOMMEND] — 2. **Material didáctico o de cara al cliente en español**: glosario de terminología audiovisual ES-MX para briefs, capacitaciones o justificar decisio
  - `ai-production-director/SKILL.md:146` [GATE] — Si una sub-skill no está instalada, no improvises su oficio en silencio: dilo en una línea y aplica el sustituto — brand-lock ausente → Visual Theme l
  - `ai-production-director/SKILL.md:150` [REQUIRE] — - `references/creative-strategy.md` — Protocolo completo de la Etapa 1: territorios, big ideas, concept cards, matriz de selección, dirección narrativ
  - `ai-production-director/SKILL.md:151` [GATE] — - `references/production-package.md` — Spec del Final AI Video Production Package, reglas de trazabilidad y checklist maestro. Léelo SIEMPRE al ejecut
  - `ai-production-director/SKILL.md:16` [RECOMMEND] — 1. **Clasificar** el proyecto y elegir el track correcto.
  - `ai-production-director/SKILL.md:17` [RECOMMEND] — 2. **Secuenciar** las etapas y cargar la sub-skill correcta en cada una.
  - `ai-production-director/SKILL.md:18` [GATE] — 3. **Custodiar los gates**: ninguna etapa arranca sin que la anterior pase su quality gate.
  - `ai-production-director/SKILL.md:19` [RECOMMEND] — 4. **Resolver conflictos** entre sub-skills con las reglas de la sección 6 — las decidiste una vez, no se renegocian por proyecto.
  - `ai-production-director/SKILL.md:20` [RECOMMEND] — 5. **Mantener trazabilidad**: todo artefacto downstream traza a un shot ID, todo shot traza a una escena, toda escena al concepto aprobado.
  - `ai-production-director/SKILL.md:22` [RECOMMEND] — El anti-patrón que este skill existe para matar: "escríbeme un guion y dame prompts" en un solo paso. Eso produce prompts sin dramaturgia, sin consist
  - `ai-production-director/SKILL.md:46` [RECOMMEND] — Clasifica el proyecto en el primer mensaje. Si el brief no da los datos, pregunta UNA sola vez, todo junto: plataforma y duración, marca/cliente, obje
  - `ai-production-director/SKILL.md:50` [PROCESS] — | Duración | ≤30s | 30–90s | 90s–10min |
  - `ai-production-director/SKILL.md:51` [PROCESS] — | Cliente/marca formal | No | Sí | Sí o pieza de autor |
  - `ai-production-director/SKILL.md:53` [PROCESS] — | Revisiones esperadas | 0–1 | 1–2 rondas | Rondas formales |
  - `ai-production-director/SKILL.md:54` [PROCESS] — | Etapas | 4 → 5/6 comprimidas | 0–7 con estrategia ligera | 0–7 completas |
  - `ai-production-director/SKILL.md:65` [GATE] — Cada etapa declara: sub-skill, entradas, salidas, y gate. El gate se verifica ANTES de avanzar. Si falla, se corrige en la etapa actual — nunca se "ar
  - `ai-production-director/SKILL.md:70` [GATE] — - **Gate:** el usuario confirma los valores flagged como estimados. Sin marca formal, usa el Visual Theme de la Etapa 3 como sustituto ligero.
  - `ai-production-director/SKILL.md:75` [GATE] — - **Gate:** el usuario selecciona UN concepto. No se escribe una línea de guion con concepto abierto.
  - `ai-production-director/SKILL.md:79` [RECOMMEND] — - **Salida:** treatment (solo FILM) → script con escenas XML-tagged, sluglines, acción y diálogo.
  - `ai-production-director/SKILL.md:80` [GATE] — - **Gate:** cada escena pasa la fórmula de escena de `video`/dramaturgy (deseo + obstáculo + geometría + mirada + ritmo) y la three-jobs rule: cada es
  - `ai-production-director/SKILL.md:85` [GATE] — - **Gate:** cero palabras del vocabulario prohibido (sección 6.1). Cada decisión de cámara tiene razón dramática escrita.
  - `ai-production-director/SKILL.md:91` [REQUIRE] — - Desde aquí, **shots.json es la fuente de verdad**. Ningún prompt, imagen o revisión existe sin shot ID.
  - `ai-production-director/SKILL.md:96` [GATE] — - **Gate:** cada anchor crítico tiene critique ACCEPT, con máximo 2 rondas de revisión vía forge en modo revisión (solo shots reprobados). A la tercer
  - `ai-production-director/references/creative-strategy.md:17` [RECOMMEND] — Si el single-minded proposition no se puede escribir en una frase, la Etapa 1 no puede continuar. Resuélvelo con el usuario primero.
  - `ai-production-director/references/creative-strategy.md:37` [REQUIRE] — De los territorios más fuertes, baja 3–5 conceptos (FILM) o 2–3 (STANDARD). Cada concepto es UNA película posible, no una variación de la anterior. Fo
  - `ai-production-director/references/creative-strategy.md:62` [GATE] — **Gate de la etapa:** el usuario selecciona un concepto (puede pedir un híbrido — trátalo como concepto nuevo con su propia card antes de avanzar).
  - `ai-production-director/references/production-package.md:44` [RECOMMEND] — 1. Todo prompt (imagen o video) lleva en comentario su `shot_id`.
  - `ai-production-director/references/production-package.md:45` [RECOMMEND] — 2. Todo shot en shots.json referencia su escena del script (`scene` field o nota).
  - `ai-production-director/references/production-package.md:46` [RECOMMEND] — 3. El script referencia la concept card ganadora en su encabezado.
  - `ai-production-director/references/production-package.md:47` [FORBID] — 4. Cambios: si un prompt necesita cambiar algo que su shot fija (encuadre, acción, luz), el cambio se hace en shots.json y se regenera hacia abajo. El
  - `ai-production-director/references/production-package.md:48` [GATE] — 5. Verificación de cierre: muestrea 3 prompts al azar y traza la cadena prompt → shot → escena → concepto. Si un eslabón falta, el paquete no se entre
  - `ai-production-director/references/production-package.md:52` [REQUIRE] — Adaptar al proyecto, con specs concretos — no placeholders:
  - `ai-production-director/references/production-package.md:68` [GATE] — - [ ] Concepto seleccionado por el usuario documentado en 01-strategy
  - `ai-production-director/references/production-package.md:69` [GATE] — - [ ] Cada escena del script pasa fórmula de escena + three-jobs rule
  - `ai-production-director/references/production-package.md:70` [GATE] — - [ ] Dirección cinematográfica sin vocabulario prohibido
  - `ai-production-director/references/production-package.md:71` [GATE] — - [ ] shots.json validado (`validate_shots.py` limpio) y auditoría de 3 detalles por shot
  - `ai-production-director/references/production-package.md:72` [GATE] — - [ ] Anchors críticos con critique ACCEPT (≤2 rondas)
  - `ai-production-director/references/production-package.md:73` [GATE] — - [ ] Prompts de video en sintaxis del modelo destino, con los dos checks de `video` pasados
  - `ai-production-director/references/production-package.md:74` [GATE] — - [ ] `aurora-prompt-linter` limpio sobre todos los prompts (si está instalada)
  - `ai-production-director/references/production-package.md:75` [GATE] — - [ ] Trazabilidad muestreada (§2.5)
  - `ai-production-director/references/production-package.md:76` [GATE] — - [ ] preview.html abre offline y refleja el estado final
  - `ai-production-director/references/production-package.md:77` [GATE] — - [ ] Créditos en 00-README.md: atribución *Serge Shima — github.com/smixs/visual-skills* si se usó la capa smixs; licencias de sub-skills anotadas
  - `ai-production-director/references/production-package.md:78` [GATE] — - [ ] 00-README.md explica en ≤1 página qué es el proyecto, qué track se usó y dónde está cada cosa
  - `aurora-prompt-linter/SKILL.md:101` [RECOMMEND] — - Solo válido en el turno actual del usuario. Autorizaciones de turnos pasados NO persisten.
  - `aurora-prompt-linter/SKILL.md:104` [RECOMMEND] — - Override de término específico (ej. `OVERRIDE: red performance tank`) solo cubre ese término.
  - `aurora-prompt-linter/SKILL.md:114` [RECOMMEND] — El conteo se hace solo sobre MAIN (no incluye negative prompt block).
  - `aurora-prompt-linter/SKILL.md:118` [PROCESS] — Reporte de texto plano (o JSON con `--json`). Ejemplo de FAIL:
  - `aurora-prompt-linter/SKILL.md:149` [PROCESS] — Ejemplo de PASS:
  - `aurora-prompt-linter/SKILL.md:16` [REQUIRE] — **Obligatorio** para:
  - `aurora-prompt-linter/SKILL.md:160` [REQUIRE] — - **Vocabulary base**: las listas en `scripts/vocabularies.yaml` están calibradas para casos típicos de Aurora (cycling, soccer, fitness). Si el proye
  - `aurora-prompt-linter/SKILL.md:30` [PROCESS] — 1. **Etiquetar los refs por categoría.** Cada ref carga 0 o más de: P (sujeto), O (outfit), L (locación), PR (prop), S (estilo). Mapea a IDs system v6
  - `aurora-prompt-linter/SKILL.md:40` [PROCESS] — 2. **Escribir el draft del prompt** (incluyendo negative prompt) a un archivo de texto.
  - `aurora-prompt-linter/SKILL.md:42` [PROCESS] — 3. **Capturar el mensaje del usuario** del turno actual a un archivo de texto (para parsear OVERRIDEs).
  - `aurora-prompt-linter/SKILL.md:44` [PROCESS] — 4. **Ejecutar el linter:**
  - `aurora-prompt-linter/SKILL.md:54` [PROCESS] — 5. **Interpretar el resultado:**
  - `aurora-prompt-linter/SKILL.md:55` [PROCESS] — - Exit 0 → STATUS=PASS → entregar al usuario + incluir reporte del linter en el output para trazabilidad.
  - `aurora-prompt-linter/SKILL.md:56` [GATE] — - Exit 1 → STATUS=FAIL → NO entregar. Iterar el draft basándose en las violaciones listadas. Repetir hasta PASS.
  - `aurora-prompt-linter/SKILL.md:67` [REQUIRE] — | **BANNED** | Cross-platform: `slow motion`, `cartoon`, `anime`, `3D render`, `perfume ad`, `dreamlike` | SIEMPRE en MAIN (deben ir en NEGATIVE) |
  - `aurora-prompt-linter/SKILL.md:68` [REQUIRE] — | **STRUCTURE** | Word count, presencia de negative prompt | Siempre |
  - `aurora-prompt-linter/SKILL.md:69` [REQUIRE] — | **REQUIRED** | `60fps`, `broadcast realism` (con flag --sports-broadcast) | Cuando aplica Regla 26 v6.0 |
  - `aurora-prompt-linter/SKILL.md:8` [GATE] — Gate determinista entre el drafting del prompt y la entrega al usuario. Mueve la regla "no redescribir lo que está en los refs" de memoria del agente 
  - `aurora-prompt-linter/references/README.md:109` [RECOMMEND] — El linter NO corre solo. El skill `prompt-production-protocol` Step 5 debe invocarlo como item crítico. Ver `skill_update_step5.md` para la edit propu
  - `aurora-prompt-linter/references/README.md:3` [GATE] — Linter determinista que bloquea entrega de prompts AI con redundancia respecto a refs, violaciones de estructura, vocabulario baneado o falta de keywo
  - `aurora-prompt-linter/references/README.md:65` [REQUIRE] — Word count: el MAX es HARD FAIL (Regla 10 v6.0). El MIN es WARN no-bloqueante (compresión válida si intencional).
  - `aurora-prompt-linter/references/README.md:69` [RECOMMEND] — Si una violación detectada es legítima en este caso, el usuario puede autorizarla por escrito en el turno actual. **Solo se acepta autorización expres
  - `aurora-prompt-linter/references/README.md:88` [RECOMMEND] — El override solo es válido en el turno actual del usuario. Autorizaciones de turnos pasados NO persisten — cada prompt nuevo arranca STRICT.
  - `aurora-prompt-linter/references/README.md:92` [RECOMMEND] — 1. **Redundancia por categoría**: si ref carga categoría X, no describir X en MAIN.
  - `aurora-prompt-linter/references/README.md:93` [RECOMMEND] — 2. **Vocabulario baneado cross-platform**: `slow motion`, `cartoon`, `anime`, `3D render`, etc. solo en NEGATIVE block.
  - `aurora-prompt-linter/references/README.md:94` [REQUIRE] — 3. **Word count**: cap MAX duro = 90 (I2V) o 130 (T2I); MIN soft = 50/75.
  - `aurora-prompt-linter/references/README.md:95` [REQUIRE] — 4. **Negative prompt**: bloque obligatorio.
  - `brand-lock-extractor/SKILL.md:102` [REQUIRE] — Every extracted value traces to an asset. Every inferred value traces to reasoning. This is the same audit-trail discipline as the brand-lock snapshot
  - `brand-lock-extractor/SKILL.md:106` [FORBID] — It is also the hardest to extract, because brands document what they do, not what they avoid. Infer it from consistency: if every image avoids stock-p
  - `brand-lock-extractor/SKILL.md:110` [REQUIRE] — "Professional, modern, clean" describes every brand and constrains nothing. Extract contrast clauses that do work: "operator not creator", "warm not p
  - `brand-lock-extractor/SKILL.md:12` [REQUIRE] — This skill extracts. It does not invent. Every value is sampled from a real asset or flagged as an estimate the user must confirm. A confident-soundin
  - `brand-lock-extractor/SKILL.md:18` [PROCESS] — - Wants to onboard a brand into shotkit and has assets (a site, a brand book, screenshots)
  - `brand-lock-extractor/SKILL.md:19` [PROCESS] — - Says "extract my brand", "build a brand lock", "make a brand pack from my site/PDF"
  - `brand-lock-extractor/SKILL.md:21` [PROCESS] — - Has a brand-lock that is half-filled and wants the gaps extracted from assets
  - `brand-lock-extractor/SKILL.md:23` [PROCESS] — If the user has nothing but a vague idea (no assets, no description), they are not extracting, they are authoring. Point them at `brand-packs/_templat
  - `brand-lock-extractor/SKILL.md:34` [PROCESS] — | Written description | Use directly | Identity, archetype, voice posture |
  - `brand-lock-extractor/SKILL.md:36` [REQUIRE] — At minimum you need one source. If the user offers none, ask for the one they have: **"What can I work from, a website URL, a brand book PDF, screensh
  - `brand-lock-extractor/SKILL.md:46` [FORBID] — Tell the user what you are pulling. Do not ask follow-ups yet, extract first, confirm gaps at the end.
  - `brand-lock-extractor/SKILL.md:50` [PROCESS] — Read `references/extraction-rubric.md`. It maps every brand-lock section to where the signal lives and how to read it. Work the nine sections in order
  - `brand-lock-extractor/SKILL.md:52` [PROCESS] — 1. **Identity** (brand, one-line description, archetype, voice posture)
  - `brand-lock-extractor/SKILL.md:53` [PROCESS] — 2. **Palette** (sampled hex, by role)
  - `brand-lock-extractor/SKILL.md:55` [PROCESS] — 4. **Mood adjectives** (3-5, specific, contrast clauses preferred)
  - `brand-lock-extractor/SKILL.md:56` [FORBID] — 5. **Never list** (what the brand avoids, inferred from consistency)
  - `brand-lock-extractor/SKILL.md:57` [PROCESS] — 6. **Aspect ratios**
  - `brand-lock-extractor/SKILL.md:58` [PROCESS] — 7. **Color grade direction** (one sentence)
  - `brand-lock-extractor/SKILL.md:59` [PROCESS] — 8. **Motion language** (one paragraph)
  - `brand-lock-extractor/SKILL.md:60` [PROCESS] — 9. **Voice rules** (copy-level constraints)
  - `brand-lock-extractor/SKILL.md:62` [PROCESS] — For every value, hold two things: the value, and where it came from (which asset, which quote, which sampled swatch). You will need the source for the
  - `brand-lock-extractor/SKILL.md:69` [FORBID] — - **inferred**, reasoned from evidence but not stated (archetype from positioning, never-list from consistency). Reasonable to ship, worth noting.
  - `brand-lock-extractor/SKILL.md:74` [REQUIRE] — Use `templates/brand-lock.md.tpl`. Fill **every** required section, no placeholders left behind. Then append an `## Extraction notes` section that lis
  - `brand-lock-extractor/SKILL.md:76` [PROCESS] — Set the footer: `Last updated` to today, `Owner` to the user or "extracted", `Version: 1.0`.
  - `brand-lock-extractor/SKILL.md:80` [PROCESS] — Before you present it, confirm the file would pass validation:
  - `brand-lock-extractor/SKILL.md:88` [PROCESS] — > "Here is your brand-lock. I sampled the palette and type from your assets and flagged N values that need your eyes (see Extraction notes). Drop it i
  - `brand-lock-extractor/SKILL.md:94` [FORBID] — Colors are sampled, never guessed. Read them from a brand book, from CSS, or by sampling pixels in a screenshot. If you genuinely cannot determine a c
  - `brand-lock-extractor/SKILL.md:98` [FORBID] — Identify fonts from the brand book, the site's CSS/font files, or clear visual match. If you cannot identify one, say so and flag it, do not name a pl
  - `brand-lock-extractor/brand-packs/README.md:11` [RECOMMEND] — > "30-second founder explainer. Use `brand-packs/acme.md` as the brand lock."
  - `brand-lock-extractor/brand-packs/README.md:13` [RECOMMEND] — 4. The skill reads it, snapshots it into the output as `brand-lock.snapshot.md`, and applies it through the pipeline.
  - `brand-lock-extractor/brand-packs/README.md:21` [FORBID] — **Be exclusive.** The "never" list is more valuable than the "always" list. Listing what the brand will not do narrows the generator's space and produ
  - `brand-lock-extractor/brand-packs/README.md:7` [RECOMMEND] — 1. Copy `_template.md` to a new file (e.g. `acme.md`)
  - `brand-lock-extractor/brand-packs/README.md:8` [RECOMMEND] — 2. Fill in every field. No placeholders left behind.
  - `brand-lock-extractor/brand-packs/README.md:9` [RECOMMEND] — 3. Reference it from your storyboard requests:
  - `brand-lock-extractor/brand-packs/_template.md:25` [FORBID] — Add more rows if the brand has more named colors. Don't add more than 8, past that, the brand stops being recognizable.
  - `brand-lock-extractor/brand-packs/_template.md:33` [RECOMMEND] — Put the font name and weight in backticks immediately after the label, e.g. `` **Display font:** `Inter Black 900`, headlines and hooks ``. The HTML p
  - `brand-lock-extractor/brand-packs/_template.md:37` [REQUIRE] — Two fonts max for production work. Three only if one is reserved for code/data.
  - `brand-lock-extractor/brand-packs/_template.md:41` [RECOMMEND] — Pick 3–5. These flow into prompts as the brand's emotional posture.
  - `brand-lock-extractor/references/extraction-rubric.md:10` [FORBID] — - **inferred**, reasoned from evidence, not stated. Archetype from how the brand frames problems. Never-list from what the assets consistently avoid. 
  - `brand-lock-extractor/references/extraction-rubric.md:17` [RECOMMEND] — **One-line description:** what the brand does and who for. This is the load-bearing sentence; a generator implicitly references it on every prompt. Pu
  - `brand-lock-extractor/references/extraction-rubric.md:19` [REQUIRE] — **Archetype:** one word, Operator, Sage, Caregiver, Rebel, Creator, Jester, Ruler, Everyman, etc. Almost always `inferred`. Read it from how the brand
  - `brand-lock-extractor/references/extraction-rubric.md:36` [FORBID] — **Never guess a hex.** If you cannot read or sample one, estimate, label it `needs confirmation`, and tell the user exactly which role to verify. (See
  - `brand-lock-extractor/references/extraction-rubric.md:42` [REQUIRE] — - **Website:** `font-family` declarations and loaded font files (`fonts.googleapis.com`, `@font-face`, `.woff2` names) name the fonts exactly. Weights
  - `brand-lock-extractor/references/extraction-rubric.md:44` [FORBID] — - **Screenshots:** identify by eye only if confident; otherwise flag `needs confirmation`. Do not invent a plausible name (Rule 2).
  - `brand-lock-extractor/references/extraction-rubric.md:46` [REQUIRE] — Two fonts max; three only if one is mono for code/data.
  - `brand-lock-extractor/references/extraction-rubric.md:50` [RECOMMEND] — 3-5 adjectives, specific, contrast clauses preferred. Read tone from the body copy and the imagery together.
  - `brand-lock-extractor/references/extraction-rubric.md:56` [FORBID] — The hardest and most valuable section. Brands document what they do; you infer what they avoid from consistency across the assets.
  - `brand-lock-extractor/references/extraction-rubric.md:60` [FORBID] — - Copy: no exclamation points? no hype words ("revolutionary", "game-changing")? no emojis? no questions in headlines? Each pattern is a never.
  - `brand-lock-extractor/references/extraction-rubric.md:61` [FORBID] — - Color/layout: never full-bleed photography? never more than one accent? never centered body text?
  - `brand-lock-extractor/references/extraction-rubric.md:63` [FORBID] — Turn each observed constraint into a `never` line. Be specific: "never use stock-photo aesthetic" beats "keep it authentic". Aim for 5+. Never ship an
  - `brand-lock-extractor/references/extraction-rubric.md:7` [RECOMMEND] — Apply one to every value.
  - `brand-lock-extractor/references/extraction-rubric.md:71` [RECOMMEND] — One sentence on how footage and generated images should be graded, with a reference point where possible (Kodak Portra 400, Apple keynote photography,
  - `brand-lock-extractor/references/extraction-rubric.md:75` [FORBID] — One paragraph: camera moves, cut style, text animation, pacing. Read from any existing video or motion on the site; if there is none, infer a conserva
  - `brand-lock-extractor/references/extraction-rubric.md:79` [FORBID] — Copy-level constraints for VO and on-screen text. Many overlap the never-list but are phrased as authoring rules: "no em dashes", "sentences under 14 
  - `brand-lock-extractor/references/extraction-rubric.md:9` [REQUIRE] — - **extracted**, read directly from an asset. A hex in the brand book PDF. A `font-family` in the site CSS. A verbatim quote from the homepage. Ship i
  - `image/SKILL.md:18` [FORBID] — The body of this SKILL.md is intentionally thin so you cannot fake a result by reading it alone. The actual rules — what the models reward, what they 
  - `image/SKILL.md:22` [RECOMMEND] — - **Motion, clips, montage** (Seedance, Kling, Veo, any image-to-video): use the sibling `video` skill. This skill's storyboard and keyframe outputs f
  - `image/SKILL.md:30` [PROCESS] — Past attempts to write prompts directly from this skill body produced lazy, generic results. Each model has its own physics; common rules collapse int
  - `image/SKILL.md:36` [PROCESS] — If the user named a model — confirm and proceed. If not — pick using the table in `models.md`, then state your choice in the output header.
  - `image/SKILL.md:46` [REQUIRE] — The model file is non-negotiable. Skipping it is the single biggest cause of weak prompts.
  - `image/SKILL.md:50` [FORBID] — Universal rules that apply to both models: start with a verb, positive framing, hex colors, quote text, edit don't re-roll, one change per iteration, 
  - `image/SKILL.md:54` [PROCESS] — Pick zero or more, depending on what the user asked for:
  - `image/SKILL.md:58` [PROCESS] — - Character continuity across multiple images / panels → [characters.md](references/characters.md)
  - `image/SKILL.md:59` [PROCESS] — - Presentation slides → [slides.md](references/slides.md)
  - `image/SKILL.md:60` [PROCESS] — - Sequential narrative (storyboard, comic, panel sequence) → [storyboards.md](references/storyboards.md)
  - `image/SKILL.md:61` [PROCESS] — - Sketch → final, wireframes, structural input → [structural.md](references/structural.md)
  - `image/SKILL.md:62` [PROCESS] — - 2D → 3D, floor plans, isometric → [dimensional.md](references/dimensional.md)
  - `image/SKILL.md:65` [PROCESS] — - **Industry pattern libraries** — proven prompt templates by vertical. Load the matching file:
  - `image/SKILL.md:70` [PROCESS] — - Posters & illustration → [patterns/poster-illustration.md](references/patterns/poster-illustration.md)
  - `image/SKILL.md:71` [PROCESS] — - Character design (turnarounds, expression sheets, outfit grids) → [patterns/character-design.md](references/patterns/character-design.md)
  - `image/SKILL.md:72` [PROCESS] — - UI mockups & social media formats → [patterns/ui-social.md](references/patterns/ui-social.md)
  - `image/references/creative-direction.md:28` [RECOMMEND] — Specify camera type to change the visual DNA of the image.
  - `image/references/creative-direction.md:50` [REQUIRE] — - "Shallow depth of field" — blurred background
  - `image/references/creative-direction.md:56` [REQUIRE] — > descriptive terms. Prefer "shallow depth of field" over "f/1.8".
  - `image/references/creative-direction.md:60` [RECOMMEND] — Set emotional tone through color and texture.
  - `image/references/creative-direction.md:7` [REQUIRE] — Tell the model exactly how the scene is illuminated.
  - `image/references/creative-direction.md:78` [FORBID] — Define physical makeup of subjects. Don't just say the thing — describe what it's MADE of.
  - `image/references/golden-rules.md:12` [FORBID] — Describe what you WANT, not what you don't want. The model understands presence better than absence.
  - `image/references/golden-rules.md:126` [REQUIRE] — **Несколько референсов сразу:**
  - `image/references/golden-rules.md:14` [REQUIRE] — - ✅ "empty street" → ❌ "street with no cars"
  - `image/references/golden-rules.md:140` [REQUIRE] — **Era anchors** — временной и географический маркер, который вызывает целый визуальный мир:
  - `image/references/golden-rules.md:145` [REQUIRE] — **Cultural anchors** — перенос визуального языка одного культурного объекта на другой контекст:
  - `image/references/golden-rules.md:15` [REQUIRE] — - ✅ "clean background" → ❌ "no clutter"
  - `image/references/golden-rules.md:150` [REQUIRE] — **Genre anchors** — режиссёр/фотограф/движение как линза:
  - `image/references/golden-rules.md:160` [REQUIRE] — 3. **Не стакай несколько genre anchors** — выбери один. "Peter Lindbergh + Wes Anderson" = каша
  - `image/references/golden-rules.md:165` [REQUIRE] — **Era anchor + конкретные детали:**
  - `image/references/golden-rules.md:176` [REQUIRE] — **Cultural anchor + новый контекст:**
  - `image/references/golden-rules.md:185` [REQUIRE] — **Genre anchor + специфика:**
  - `image/references/golden-rules.md:198` [REQUIRE] — *Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) 
  - `image/references/golden-rules.md:20` [REQUIRE] — Image 80% correct? Request specific change:
  - `image/references/golden-rules.md:41` [REQUIRE] — Context helps model make logical decisions:
  - `image/references/golden-rules.md:42` [REQUIRE] — - "for Brazilian gourmet cookbook" → infers professional plating, shallow DOF
  - `image/references/golden-rules.md:48` [REQUIRE] — Any text for rendering goes in quotes:
  - `image/references/golden-rules.md:50` [REQUIRE] — - Labels: "[Revenue Growth]", "[Net Income]"
  - `image/references/golden-rules.md:51` [REQUIRE] — - Specify weight: bold, thin, extra bold
  - `image/references/golden-rules.md:52` [REQUIRE] — - Specify position: "upper third", "centered"
  - `image/references/golden-rules.md:8` [REQUIRE] — Tell the model the primary operation: "Create", "Generate", "Design", "Transform", "Convert", "Edit". This sets the intent before details.
  - `image/references/golden-rules.md:81` [REQUIRE] — В обоих случаях: дешёвая разведка → дорогой финал.
  - `image/references/golden-rules.md:85` [REQUIRE] — After generation:
  - `image/references/golden-rules.md:95` [REQUIRE] — Используй для:
  - `image/references/golden-rules.md:97` [REQUIRE] — **Вписать в существующий дизайн:**
  - `image/references/gpt-image.md:3` [RECOMMEND] — Production default OpenAI: `gpt-image-2`. Migration-only: `gpt-image-1.5`, `gpt-image-1`. Бюджетный: `gpt-image-1-mini`.
  - `image/references/gpt-image.md:34` [RECOMMEND] — | ❌ Не пиши | ✅ Пиши |
  - `image/references/gpt-image.md:39` [REQUIRE] — | мудовый язык, в котором тонут функциональные требования | прямое заявление: «image must contain a transit kiosk» |
  - `image/references/gpt-image.md:53` [REQUIRE] — - Max edge: <3840px
  - `image/references/gpt-image.md:55` [REQUIRE] — - Aspect ratio: max 3:1 (long:short)
  - `image/references/gpt-image.md:74` [RECOMMEND] — - Маленький/плотный/multi-font → `quality: high` обязательно.
  - `image/references/models.md:34` [RECOMMEND] — - **Структурированный 5-slot промпт.** Чёткое разделение Scene/Subject/Details/Use case/Constraints даёт предсказуемость.
  - `image/references/models.md:38` [PROCESS] — - Photorealistic портреты.
  - `image/references/models.md:40` [PROCESS] — - Минималистичные постеры.
  - `image/references/models.md:41` [PROCESS] — - Editorial-фотография.
  - `image/references/models.md:47` [PROCESS] — | Стиль промпта | Натуральный язык, 1-2 параграфа | 5-slot с лейблами секций |
  - `image/references/models.md:48` [PROCESS] — | Камера/линза | **Не указывать** числа (50mm, f/2.8) — NB игнорит | Можно «50mm feel», но как high-level look |
  - `image/references/models.md:49` [PROCESS] — | «Stunning/epic/masterpiece» | Игнорит, не вредит | **Anti-slop**: вредит, делает результат хуже |
  - `image/references/models.md:51` [PROCESS] — | Negative framing | Использовать позитив | Использовать позитив + явный preserve list |
  - `image/references/models.md:52` [PROCESS] — | Сложные сцены | JSON для 5+ элементов | 5-slot template со секциями |
  - `image/references/models.md:53` [PROCESS] — | Edit | «Keep X same, change Y» | «Change: X / Preserve: Y / Constraints: Z» — повторять preserve каждую итерацию |
  - `image/references/models.md:72` [REQUIRE] — *Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) 
  - `image/references/multi-panel.md:13` [RECOMMEND] — **When to use:** TVC or commercial shot breakdown — one image = 9 panels with scene titles and timestamps.
  - `image/references/multi-panel.md:133` [RECOMMEND] — **When to use:** 12 panels telling a story or showing moods — no gaps between panels, seamless mosaic feel.
  - `image/references/multi-panel.md:209` [FORBID] — - Top-down and low-angle in the same grid confuse the model if you don't anchor each frame to a grid position
  - `image/references/multi-panel.md:248` [REQUIRE] — - Left/right assignment matters — always state which side is before and which is after
  - `image/references/multi-panel.md:254` [RECOMMEND] — **When to use:** Full narrative in one image — 3x4 grid (3 columns, 4 rows) for animation or video pre-production.
  - `image/references/multi-panel.md:300` [REQUIRE] — - Art style must be stated once and applied uniformly; mixing styles across panels produces visual chaos
  - `image/references/multi-panel.md:310` [REQUIRE] — **Grid specification:** Always state the grid dimensions (e.g., "3x2 grid, 3 columns 2 rows"). Saying "6 panels" without layout instruction lets the m
  - `image/references/multi-panel.md:312` [RECOMMEND] — **Borders and gaps:** Be explicit — "thin white border between panels" or "borderless, no gaps." Default behavior varies by model and is unreliable.
  - `image/references/multi-panel.md:50` [REQUIRE] — - Vague scene descriptions produce near-identical panels — each must have a distinct action, angle, or subject
  - `image/references/nano-banana.md:102` [FORBID] — Interactions API держит контекст сессии — до 3 последовательных правок стэкаются без потери исходника. Правило «Edit, don't re-roll»: картинка верна н
  - `image/references/nano-banana.md:130` [RECOMMEND] — - **Хэндофф в видеомодель — motion brief, не пересказ.** Движение камеры, движение субъекта, движение фона, длительность, framing lock, запрещённые из
  - `image/references/nano-banana.md:137` [RECOMMEND] — - Инфографика может содержать фактически неверные данные — цифры проверять всегда, grounding помогает, но не гарантирует.
  - `image/references/nano-banana.md:24` [REQUIRE] — - Числовые параметры объектива: **50mm, 85mm, f/2.8, ISO 400** — NB игнорит. Используй описание: «shallow depth of field», «wide-angle distortion».
  - `image/references/patterns/character-design.md:86` [RECOMMEND] — Use to transform a realistic character into a cute 3D collectible figurine — oversized head, compact body, multiple poses performing different activit
  - `image/references/patterns/character-design.md:9` [RECOMMEND] — Use for game or animation pre-production — front, side, and back views of a character on a single white canvas with color callouts and height referenc
  - `image/references/patterns/fashion-editorial.md:79` [RECOMMEND] — Use for playful, nostalgic sportswear or athleisure campaigns with 70s-80s visual language.
  - `image/references/patterns/fashion-editorial.md:85` [REQUIRE] — **Key levers:** `{model_description}`, `{outfit_description}` (high-waisted terry shorts in coral, cropped zip-up in cream, tube socks with racing str
  - `image/references/patterns/food-beverage.md:9` [RECOMMEND] — Use for premium chocolate or confectionery brand visuals — moody, textural, with controlled color and atmosphere. Adaptable across mood variants (dark
  - `image/references/patterns/portrait-cinema.md:21` [RECOMMEND] — **Key levers:** `{street_description}` (narrow European alley with stone walls, wide boulevard with linden trees, industrial backstreet with brick), `
  - `image/references/patterns/ui-social.md:81` [RECOMMEND] — Use for realistic analytics dashboard mockups — dark or light theme with data visualizations, KPI cards, and sidebar navigation.
  - `image/references/prompt-framework.md:159` [RECOMMEND] — Переменные записываются как `{name, default="value"}`. Если значение не указано — используется дефолт. Если дефолта нет — переменная обязательна.
  - `image/references/prompt-framework.md:173` [RECOMMEND] — 1. **Заменяй только то, что меняется** — остальное берётся из дефолтов
  - `image/references/prompt-framework.md:174` [RECOMMEND] — 2. **Структура стабильна** — порядок слотов одинаковый для всех вариаций, модель получает консистентный формат
  - `image/references/prompt-framework.md:175` [RECOMMEND] — 3. **Batch-генерация** — идеально для серий: продуктовые ракурсы, позы персонажа, локации в одном стиле
  - `image/references/prompt-framework.md:212` [RECOMMEND] — 1. **Surface wear & aging** — "chipped paint on window frame, hairline scratches on metal surface, green patina on copper fittings, oxidation marks on
  - `image/references/prompt-framework.md:216` [RECOMMEND] — 5. **Fabric & material drape** — "natural fabric folds at elbow crease, gravity pull on loose linen garment, weight distribution visible in heavy wool
  - `image/references/prompt-framework.md:28` [RECOMMEND] — **Обязательные:**
  - `image/references/prompt-framework.md:39` [RECOMMEND] — - **Палитра** - цвета (лучше hex)
  - `image/references/slides.md:11` [REQUIRE] — - Max 5 пунктов на слайде
  - `image/references/slides.md:178` [REQUIRE] — - Max 9 блоков (иначе перегруз)
  - `image/references/slides.md:26` [REQUIRE] — - 3-4 цвета max (основной + 2-3 акцента)
  - `image/references/slides.md:29` [RECOMMEND] — - Избегай pure white #fff на чёрном - используй #f5f5f5
  - `image/references/slides.md:32` [RECOMMEND] — - Контент должен дышать
  - `image/references/slides.md:39` [RECOMMEND] — - High-res only, каждый образ усиливает идею
  - `image/references/storyboards.md:78` [REQUIRE] — - "Identity must stay consistent throughout"
  - `image/references/storyboards.md:81` [RECOMMEND] — - "Expressions and poses should vary"
  - `image/references/storyboards.md:82` [RECOMMEND] — - "Only one of each character per image"
  - `image/references/structural.md:37` [RECOMMEND] — Use cases:
  - `image/references/structural.md:56` [RECOMMEND] — - **What** proportions to use
  - `image/references/structural.md:84` [RECOMMEND] — Use reference for:
  - `image/references/text-rendering.md:126` [RECOMMEND] — 1. Ask the model to write/refine the text content
  - `image/references/text-rendering.md:127` [RECOMMEND] — 2. Then ask for an image with that exact text
  - `image/references/text-rendering.md:163` [RECOMMEND] — - More accurate than relying only on search
  - `image/references/text-rendering.md:167` [RECOMMEND] — - Upload with prompt: "Use layout from attached image"
  - `image/references/vision-decomposer.md:103` [PROCESS] — Load `vision-decomposer.md` whenever:
  - `image/references/vision-decomposer.md:3` [RECOMMEND] — Use this reference when the user asks to analyze an image and convert it to a generation prompt: **style transfer**, **mood reference**, **"сделай про
  - `image/references/vision-decomposer.md:49` [PROCESS] — - **Camera (angles & viewpoint):** Angle (High angle, Low angle, Eye-level, Dutch tilt). Objective camera, Subjective, POV, Over-the-shoulder (OTS). M
  - `image/references/vision-decomposer.md:61` [PROCESS] — - Write **only keywords separated by commas, in English**.
  - `image/references/vision-decomposer.md:62` [FORBID] — - Describe **strictly what you see**. Do not invent new objects.
  - `image/references/vision-decomposer.md:63` [FORBID] — - **No filler.** Never write "The image shows...", "A picture of...", "I can see...".
  - `image/references/vision-decomposer.md:7` [REQUIRE] — The process has two strict steps. Do not skip Step 1. Do not freestyle Step 2.
  - `image/references/vision-decomposer.md:85` [REQUIRE] — Each line: 1-2 sentences max. Just the extracted parameters.
  - `image/references/vision-decomposer.md:89` [PROCESS] — A code block containing only the prompt text in English, assembled by the formula in Step 2:
  - `learned/production-learnings.v3.2.json:1` [REQUIRE] — On a revision, every user/project lock remains inherited verbatim unless the user explicitly changes that lock.
  - `learned/production-learnings.v3.2.json:14` [REQUIRE] — Do not carry subject demographics, nationality, ethnicity, gender, wardrobe, brand, or other content locks from a previous task into a new task unless
  - `learned/production-learnings.v3.2.json:2` [REQUIRE] — When correcting a localized failure in an otherwise accepted or strong asset, change only the failed element(s); do not rewrite or reinterpret unaffec
  - `learned/production-learnings.v3.2.json:5` [REQUIRE] — Delivery parameters such as requested aspect ratio are hard generator settings when the platform exposes them; prompt prose alone is not sufficient. V
  - `learned/production-learnings.v3.2.json:6` [REQUIRE] — Post-generation aspect ratio QA: exact requested ratio is preferred; deviation up to 1% is a minor delivery/crop correction, greater deviation is a bl
  - `learned/production-learnings.v3.2.json:7` [REQUIRE] — Do not amplify an unspecified quantity, density, intensity, or prominence. Presence of an element does not authorize sparse/full/dense/large unless th
  - `learned/production-learnings.v3.2.json:9` [REQUIRE] — Scene objects whose locked spatial relationship places them behind the camera must not appear in frame. Camera-relative environment geometry is a crit
  - `learned/production-learnings.v3.4.json:1` [REQUIRE] — Every prompt must target an immutable frozen brief by exact SHA-256. Downstream prompt generation may not mutate brief facts.
  - `learned/production-learnings.v3.4.json:2` [REQUIRE] — Prompt compilation is blocked while any case-relevant prompt-required field is unresolved. Resolve it from an authorized source or ask the user before
  - `learned/production-learnings.v3.4.json:3` [REQUIRE] — After a prompt is approved, every revision must begin with an explicit authorized delta against the exact prior brief hash. No implicit or opportunist
  - `produccion-visual-sw30/SKILL.md:101` [GATE] — - `audit_gi2.py` valida 15 columnas: slots · anti-slop · ratio estándar · metadatos fuera del prompt · Notes · cámara con los 5 efectos ópticos (compr
  - `produccion-visual-sw30/SKILL.md:104` [GATE] — - El lint del builder ROMPE la compilación ante cualquier desviación de plantilla.
  - `produccion-visual-sw30/SKILL.md:107` [GATE] — Antes de (a) cualquier generación que gaste créditos y (b) entregar cualquier prompt visual, la respuesta abre con exactamente 3 líneas: SKILL: <archi
  - `produccion-visual-sw30/SKILL.md:12` [GATE] — Ninguna respuesta es satisfactoria para el usuario — y viola el prompt maestro — mientras la respuesta honesta a esta pregunta no sea SÍ SIN MATICES:
  - `produccion-visual-sw30/SKILL.md:120` [GATE] — 3. El editor no tiene memoria: solo verbos operativos (Move/Replace/Add/Remove/Swap), cero narrativa ("has become", "again").
  - `produccion-visual-sw30/SKILL.md:122` [GATE] — 4. Autocontención: toda comparación ("same X") exige ambos referentes adjuntos en ESE prompt.
  - `produccion-visual-sw30/SKILL.md:129` [GATE] — 8. Stills en instante congelado ("frozen mid-stride"); nada de movimiento en imagen fija.
  - `produccion-visual-sw30/SKILL.md:134` [GATE] — 11. Lo aprobado se canoniza con hash y se EDITA desde ahí; lo caro nunca se regenera.
  - `produccion-visual-sw30/SKILL.md:135` [GATE] — 12. "Edit, don't re-roll": resultado ≥80% correcto → cambio puntual (hasta 3 ediciones apiladas), nunca re-tirar.
  - `produccion-visual-sw30/SKILL.md:137` [GATE] — 13. Máximo 2 intentos por método. A la 2ª falla: cambio de método con causa declarada, o alto y consulta. Nunca tercera vuelta de lo mismo.
  - `produccion-visual-sw30/SKILL.md:139` [GATE] — 14. Validadores del paquete y techos de palabras en verde antes de entregar; inspección visual propia (zooms 100% de rostros y manos) antes de present
  - `produccion-visual-sw30/SKILL.md:142` [GATE] — 15. shots.json es la fuente de verdad: todo cambio entra ahí primero y se propaga.
  - `produccion-visual-sw30/SKILL.md:143` [GATE] — 16. Clips: solo Preserve-cues, roles de start/tail ("The tail image defines X — inherit exactly"), movimiento puro, imagen final nombrada; negativos s
  - `produccion-visual-sw30/SKILL.md:145` [GATE] — 17. Entregas en unidades chicas con OK de dirección; se entrega el delta, no el paquete. Una regla nueva de dirección se aplica a TODOS los prompts, n
  - `produccion-visual-sw30/SKILL.md:147` [GATE] — 18. Respuestas: el dato o entregable en la primera línea. Cero adulación y cero evaluación de las acciones de Eric salvo que la pida. Error = una líne
  - `produccion-visual-sw30/SKILL.md:149` [GATE] — 19. Prohibido afirmar capacidades, límites o hechos de plataforma sin verificarlos en este turno (leer la fuente o buscar); lo no verificado se etique
  - `produccion-visual-sw30/SKILL.md:15` [GATE] — RESPONDE HONESTAMENTE: ¿UTILIZASTE DE FORMA EXHAUSTIVA Y CORRECTA TODAS LAS REGLAS DEL SKILL APLICABLES A ESTE CASO? RESPONDE SI O NO.
  - `produccion-visual-sw30/SKILL.md:151` [GATE] — 20. /research solo para problemas genuinamente nuevos; /briefing solo al retomar tras días fuera; /handoff al cerrar sesión. Ninguno por default.
  - `produccion-visual-sw30/SKILL.md:18` [GATE] — Reglas de uso:
  - `produccion-visual-sw30/SKILL.md:19` [GATE] — - La pregunta se responde ANTES de entregar, no después de que el usuario la haga.
  - `produccion-visual-sw30/SKILL.md:20` [GATE] — - Si la respuesta es NO: no se entrega. Se leen los archivos faltantes, se aplica lo que falte y se vuelve a preguntar. Se repite cuantas veces sea ne
  - `produccion-visual-sw30/SKILL.md:22` [GATE] — - Prohibido responder SÍ para complacer. Un SÍ falso es una mentira y cuesta más que el NO.
  - `produccion-visual-sw30/SKILL.md:23` [GATE] — - Prohibido responder SÍ con matices, condiciones o notas al pie disfrazadas de honestidad.
  - `produccion-visual-sw30/SKILL.md:24` [GATE] — - "Exhaustiva" significa: leídos COMPLETOS todos los archivos del skill aplicables al caso (SKILL.md indica el orden obligatorio), no fragmentos ni gr
  - `produccion-visual-sw30/SKILL.md:26` [GATE] — - "Correcta" significa: cada regla verificable corre en un lint o auditor ejecutable por el usuario; las no mecanizables se contrastan una a una contr
  - `produccion-visual-sw30/SKILL.md:28` [GATE] — - Ante duda sobre si un archivo aplica, se lee su sección "cuándo cargar / when to load" en vez de decidirlo por criterio propio.
  - `produccion-visual-sw30/SKILL.md:30` [GATE] — - Se permite preguntar al usuario cuando la duda es de dirección creativa, no de reglas.
  - `produccion-visual-sw30/SKILL.md:33` [GATE] — Orden de dirección: nunca se escribe un prompt de corrido ni se parchea texto. Tres pasos, en este orden:
  - `produccion-visual-sw30/SKILL.md:42` [GATE] — 3. **ENSAMBLAR POR SECCIÓN** — el prompt se construye llamando P(scene, subject, [details], mood, usecase, [constraints]) para creación o E(change, pr
  - `produccion-visual-sw30/SKILL.md:45` [GATE] — + "Prompt:" + "Notes:" fuera del cuerpo.
  - `produccion-visual-sw30/SKILL.md:48` [GATE] — Causa raíz medida: el catálogo de reglas salía de la memoria y cubría 26 de 209 enunciados de la fuente (12%). Todos los controles derivaban de ese ca
  - `produccion-visual-sw30/SKILL.md:52` [GATE] — 1. `rule_registry.py` — relee los 23 archivos del skill image y EXTRAE mecánicamente cada enunciado normativo (209). Si el skill cambia, el registro c
  - `produccion-visual-sw30/SKILL.md:54` [GATE] — 2. `rule_ledger.py` — obliga a que CADA regla aplicable tenga disposición explícita: CHECK (existe verificación) o NA (con razón escrita y auditable).
  - `produccion-visual-sw30/SKILL.md:56` [GATE] — 3. `audit_gi2.py` — verifica los prompts columna por columna.
  - `produccion-visual-sw30/SKILL.md:58` [GATE] — **GATE DE COBERTURA**: el builder corre `rule_ledger.py` antes de emitir; si no cierra en 100% dispuesto, no hay archivo de prompts. Estado actual: 12
  - `produccion-visual-sw30/SKILL.md:62` [GATE] — Cuando el usuario detecte un defecto: se añade su regla al ledger con su check en el mismo turno. Así el sistema aprende de su detector más confiable 
  - `produccion-visual-sw30/SKILL.md:66` [GATE] — Dirección canonizó el template que resolvió el look plástico (2026-08-25). Todo maestro de rostro se instancia con estos cuatro bloques y el motor lan
  - `produccion-visual-sw30/SKILL.md:69` [GATE] — | Sección | Bloque obligatorio | Por qué |
  - `produccion-visual-sw30/SKILL.md:76` [GATE] — Además, en el slot de rasgos: describir una cara IRREGULAR (nariz con caballete, cicatriz, ojos hundidos, asimetrías). La cara regular y simétrica es 
  - `produccion-visual-sw30/SKILL.md:79` [GATE] — Longitud: el prompt completo se mantiene alrededor de 250 palabras. Un slot de 300+ palabras compite consigo mismo — causa documentada de artefactos e
  - `produccion-visual-sw30/SKILL.md:8` [GATE] — OBJETIVO ÚNICO: máxima calidad de imagen conforme al script, al menor costo de créditos. Toda decisión se evalúa contra ese objetivo. El production-pa
  - `produccion-visual-sw30/SKILL.md:83` [GATE] — `production-package/template_engine.py` es OBLIGATORIO para construir cualquier prompt visual. Un prompt no se escribe: se INSTANCIA con `build(tipo, 
  - `produccion-visual-sw30/SKILL.md:86` [GATE] — - falta cualquier sección obligatoria del tipo (T1..T5 declaran su lista, en orden);
  - `produccion-visual-sw30/SKILL.md:87` [GATE] — - se pasa una sección que la plantilla no declara;
  - `produccion-visual-sw30/SKILL.md:88` [GATE] — - una sección que debe venir de `BLOCKS` llega como texto suelto — el mensaje dice qué bloque editar;
  - `produccion-visual-sw30/SKILL.md:89` [GATE] — - falta el bloque `Notes`;
  - `produccion-visual-sw30/SKILL.md:90` [GATE] — - se cuela un metadato (Model/Quality/Size/Aspect ratio) dentro del cuerpo del prompt.
  - `produccion-visual-sw30/SKILL.md:91` [GATE] — `python3 template_engine.py` corre su autotest: comprueba que rechaza secciones faltantes, texto suelto y tipos desconocidos, y que una instancia váli
  - `produccion-visual-sw30/SKILL.md:95` [GATE] — - Identificar a qué BLOQUE pertenece → editar ese bloque UNA vez → recompilar → auditar.
  - `produccion-visual-sw30/SKILL.md:96` [GATE] — - El cambio se propaga solo a todos los briefs que usan ese bloque.
  - `produccion-visual-sw30/SKILL.md:97` [GATE] — - **PROHIBIDO editar el texto de un brief individual.** Eso es parchar: arregla una cosa y rompe otra, y es la causa raíz de los ciclos de tres reescr
  - `storyboard-architect/SKILL.md:100` [PROCESS] — Read `references/shot-grammar.md` for controlled vocabulary. The field names below are the schema's field names. `templates/shots.schema.json` sets `a
  - `storyboard-architect/SKILL.md:107` [REQUIRE] — - `start` / `end`, timestamps in seconds, decimal allowed. `end` must be after `start`
  - `storyboard-architect/SKILL.md:113` [REQUIRE] — - `depth_of_field`, optional, shallow / deep / rack
  - `storyboard-architect/SKILL.md:115` [PROCESS] — - `environment_ref`, references series-lock language, default `series_lock.environment`
  - `storyboard-architect/SKILL.md:116` [PROCESS] — - `lighting_ref`, references series-lock language, default `series_lock.lighting`
  - `storyboard-architect/SKILL.md:128` [FORBID] — Every piece of on-screen text becomes an entry in `text-overlays.json`. Never bake text into the visual description. Each overlay has:
  - `storyboard-architect/SKILL.md:137` [REQUIRE] — - `color`, hex (must come from brand-lock palette)
  - `storyboard-architect/SKILL.md:147` [PROCESS] — Define environment, lighting, and character anchors that apply across every shot. These go at the top of `shots.json` under `series_lock`. Without the
  - `storyboard-architect/SKILL.md:151` [REQUIRE] — Every shot has a one-sentence rationale. Why this beat. Why this framing. Why this on-screen text. This is the audit trail. Do not skip it.
  - `storyboard-architect/SKILL.md:16` [PROCESS] — - Describes a video they want to make ("30-second explainer for...", "TikTok ad about...")
  - `storyboard-architect/SKILL.md:163` [FORBID] — The timestamp is a full UTC instant, `YYYY-MM-DDThh:mm:ssZ`. A bare date cannot distinguish two runs made on the same day, which is the case that matt
  - `storyboard-architect/SKILL.md:17` [PROCESS] — - Asks to storyboard, plan shots, break out beats, write a shot list
  - `storyboard-architect/SKILL.md:19` [PROCESS] — - Mentions a beat framework by name (Hero Trilogy, Pain-Proof-Promise, etc.)
  - `storyboard-architect/SKILL.md:192` [PROCESS] — Use the template at `templates/storyboard.md.tpl`. Read it before writing.
  - `storyboard-architect/SKILL.md:196` [REQUIRE] — Must validate against `templates/shots.schema.json`. Read it before writing. The structure is:
  - `storyboard-architect/SKILL.md:20` [PROCESS] — - References an existing brand-lock file or pack
  - `storyboard-architect/SKILL.md:22` [PROCESS] — If the user only wants prompts for an image generator (no narrative structure), use `visual-prompt-forge` directly instead.
  - `storyboard-architect/SKILL.md:230` [PROCESS] — Write `1.2` for new storyboards. `1.0` and `1.1` files stay valid; the array form of `on_screen_text` and the hashed `assets` block need `1.2`.
  - `storyboard-architect/SKILL.md:235` [REQUIRE] — Must validate against `templates/text-overlays.schema.json`. Read it before writing.
  - `storyboard-architect/SKILL.md:239` [GATE] — Run the validator. Do not eyeball this list.
  - `storyboard-architect/SKILL.md:247` [GATE] — `validate_shots.py` checks every mechanical rule that used to live here as a checkbox, because a checkbox is a rule enforced by remembering to look:
  - `storyboard-architect/SKILL.md:250` [GATE] — - shots.json and text-overlays.json validate against their schemas
  - `storyboard-architect/SKILL.md:251` [GATE] — - `end` is after `start`, no duplicate ids, no gaps, no overlaps, and the covered span matches `project.duration_s` within 0.1s
  - `storyboard-architect/SKILL.md:253` [GATE] — - every `on_screen_text` resolves to an overlay, every `overlay.shot_id` resolves to a shot, and every overlay is reachable from at least one shot
  - `storyboard-architect/SKILL.md:256` [GATE] — - every overlay color appears in the brand-lock palette
  - `storyboard-architect/SKILL.md:257` [GATE] — - `brand_lock_ref` resolves on disk
  - `storyboard-architect/SKILL.md:265` [GATE] — - [ ] Every rationale says *why this shot at this moment*, not what the shot contains
  - `storyboard-architect/SKILL.md:267` [GATE] — - [ ] The beat structure actually matches the brief's argument
  - `storyboard-architect/SKILL.md:268` [GATE] — - [ ] `run.json` is written and its hashes are the files as shipped
  - `storyboard-architect/SKILL.md:270` [GATE] — If the validator fails, fix it before declaring done. A green validator plus an unread rationale is not a finished storyboard.
  - `storyboard-architect/SKILL.md:275` [RECOMMEND] — Load these as needed:
  - `storyboard-architect/SKILL.md:305` [FORBID] — Don't run those automatically. The user picks.
  - `storyboard-architect/SKILL.md:37` [FORBID] — `run.json` is what makes the rest of the tree auditable later. A filename says nothing about the bytes behind it, so the snapshot sitting next to a se
  - `storyboard-architect/SKILL.md:42` [FORBID] — If the user asks for image prompts or HTML preview, hand off to `visual-prompt-forge` or `storyboard-html-preview`, those skills consume `shots.json` 
  - `storyboard-architect/SKILL.md:48` [REQUIRE] — | Input | Required? | Default if absent |
  - `storyboard-architect/SKILL.md:54` [PROCESS] — | Brand-lock file path | No | Use `brand-packs/_template.md` and flag the gap |
  - `storyboard-architect/SKILL.md:60` [REQUIRE] — Follow this sequence. Don't skip steps even if the brief seems simple.
  - `storyboard-architect/SKILL.md:69` [FORBID] — - "Never" list (what this brand will never do visually)
  - `storyboard-architect/SKILL.md:72` [PROCESS] — - Aspect-ratio preferences
  - `storyboard-architect/SKILL.md:74` [RECOMMEND] — If no brand-lock is provided, copy `brand-packs/_template.md` into the output as `brand-lock.snapshot.md` with a note: `# UNCONFIGURED, using template
  - `storyboard-architect/SKILL.md:78` [PROCESS] — Read `references/beat-frameworks.md`. Pick the one that matches the brief. Common cases:
  - `storyboard-architect/SKILL.md:89` [PROCESS] — Read `references/timing-rules.md` for the math. Default cadence:
  - `storyboard-architect/SKILL.md:96` [FORBID] — Don't fight the framework. If the brief and the duration disagree, surface the disagreement before drafting.
  - `storyboard-architect/brand-packs/README.md:11` [RECOMMEND] — > "30-second founder explainer. Use `brand-packs/acme.md` as the brand lock."
  - `storyboard-architect/brand-packs/README.md:13` [RECOMMEND] — 4. The skill reads it, snapshots it into the output as `brand-lock.snapshot.md`, and applies it through the pipeline.
  - `storyboard-architect/brand-packs/README.md:21` [FORBID] — **Be exclusive.** The "never" list is more valuable than the "always" list. Listing what the brand will not do narrows the generator's space and produ
  - `storyboard-architect/brand-packs/README.md:7` [RECOMMEND] — 1. Copy `_template.md` to a new file (e.g. `acme.md`)
  - `storyboard-architect/brand-packs/README.md:8` [RECOMMEND] — 2. Fill in every field. No placeholders left behind.
  - `storyboard-architect/brand-packs/README.md:9` [RECOMMEND] — 3. Reference it from your storyboard requests:
  - `storyboard-architect/references/beat-frameworks.md:10` [FORBID] — 2. **Reframe**, flip the problem on its head. The point is *not* what they thought it was. "You don't have a content problem. You have an infrastructu
  - `storyboard-architect/references/beat-frameworks.md:11` [RECOMMEND] — 3. **Promise**, what life looks like on the other side. Specific, verifiable, time-bound when possible.
  - `storyboard-architect/references/beat-frameworks.md:16` [RECOMMEND] — Use when: ad creative, landing-page hero video, conversion-focused social.
  - `storyboard-architect/references/beat-frameworks.md:22` [RECOMMEND] — 1. **World**, set the context. Who lives in this world. What's broken about it.
  - `storyboard-architect/references/beat-frameworks.md:24` [RECOMMEND] — 3. **Transformation**, the world changes. Show before/after at scale.
  - `storyboard-architect/references/beat-frameworks.md:3` [FORBID] — Pick one. Don't invent a new one unless the brief genuinely doesn't fit. Document the choice in `storyboard.md`.
  - `storyboard-architect/references/beat-frameworks.md:35` [RECOMMEND] — 1. **Hook**, a one-line provocation (0–2s)
  - `storyboard-architect/references/beat-frameworks.md:36` [RECOMMEND] — 2. **Stakes**, why this matters (2–8s)
  - `storyboard-architect/references/beat-frameworks.md:37` [RECOMMEND] — 3. **Insight**, the actual point (8–20s for 30s, 8–40s for 60s)
  - `storyboard-architect/references/beat-frameworks.md:38` [RECOMMEND] — 4. **Proof**, one concrete example or data point
  - `storyboard-architect/references/beat-frameworks.md:39` [RECOMMEND] — 5. **CTA**, what to do next, narrow and specific
  - `storyboard-architect/references/beat-frameworks.md:47` [RECOMMEND] — 1. **Wide claim**, the headline take
  - `storyboard-architect/references/beat-frameworks.md:48` [RECOMMEND] — 2. **Zoom 1**, one layer of nuance
  - `storyboard-architect/references/beat-frameworks.md:49` [RECOMMEND] — 3. **Zoom 2**, the layer underneath that
  - `storyboard-architect/references/beat-frameworks.md:50` [RECOMMEND] — 4. **Snap-back**, return to the wide claim, now reframed by the zooms
  - `storyboard-architect/references/beat-frameworks.md:54` [RECOMMEND] — Use when: opinion videos, kinetic-type pieces, social-native commentary.
  - `storyboard-architect/references/beat-frameworks.md:58` [RECOMMEND] — Default for how-to content. Four beats:
  - `storyboard-architect/references/beat-frameworks.md:60` [RECOMMEND] — 1. **Problem state**, what someone is stuck on
  - `storyboard-architect/references/beat-frameworks.md:61` [RECOMMEND] — 2. **Reveal**, the technique or trick
  - `storyboard-architect/references/beat-frameworks.md:62` [RECOMMEND] — 3. **Walk-through**, apply it step by step
  - `storyboard-architect/references/beat-frameworks.md:63` [RECOMMEND] — 4. **Result**, the after-state, side-by-side with before
  - `storyboard-architect/references/beat-frameworks.md:65` [RECOMMEND] — Use when: tutorials, demo videos, training content.
  - `storyboard-architect/references/beat-frameworks.md:7` [RECOMMEND] — Default for conversion content. Three beats:
  - `storyboard-architect/references/beat-frameworks.md:9` [RECOMMEND] — 1. **Pain**, name the audience's actual problem in their actual language. Concrete, not abstract. "Your content feels random" not "marketing inefficie
  - `storyboard-architect/references/on-screen-text.md:103` [RECOMMEND] — Document this in rationale: "text persists across shot 3-4 to give 4.8s read-time for 16-word reframe."
  - `storyboard-architect/references/on-screen-text.md:11` [RECOMMEND] — 5. **CTA.** The action you want the viewer to take.
  - `storyboard-architect/references/on-screen-text.md:15` [RECOMMEND] — 1. **Restating the VO.** If the voice says it, the text is noise.
  - `storyboard-architect/references/on-screen-text.md:16` [RECOMMEND] — 2. **Decorative copy.** "Moments matter" floating over b-roll. Cut it.
  - `storyboard-architect/references/on-screen-text.md:18` [RECOMMEND] — 4. **Filler beats.** If the shot doesn't need text, leave it clean.
  - `storyboard-architect/references/on-screen-text.md:26` [REQUIRE] — When a shot has on-screen text, the **shot subject must reserve space for it**. This is enforced at storyboard time, not generation time.
  - `storyboard-architect/references/on-screen-text.md:3` [RECOMMEND] — Text on screen is a load-bearing decision. Most storyboards over-text. The default should be: **does this shot need text to land?** If the visual carr
  - `storyboard-architect/references/on-screen-text.md:36` [RECOMMEND] — | Position | Use when |
  - `storyboard-architect/references/on-screen-text.md:43` [FORBID] — | `{x: %, y: %}` | Custom, only when the standard positions don't fit |
  - `storyboard-architect/references/on-screen-text.md:47` [RECOMMEND] — | Size | Pixel approx (1080p) | Use for |
  - `storyboard-architect/references/on-screen-text.md:56` [RECOMMEND] — Default to clean, not flashy:
  - `storyboard-architect/references/on-screen-text.md:63` [FORBID] — Avoid stacking animations. Pick one per overlay.
  - `storyboard-architect/references/on-screen-text.md:67` [REQUIRE] — The `color` field of every text overlay must be a hex value that exists in the brand-lock palette. If you find yourself wanting a color that's not in 
  - `storyboard-architect/references/on-screen-text.md:7` [RECOMMEND] — 1. **Auto-play-mute environments.** Social feeds. Text replaces VO.
  - `storyboard-architect/references/on-screen-text.md:75` [FORBID] — Already covered in timing-rules.md but worth repeating: text needs to be on screen long enough for someone to read it twice. Calculate, then verify. D
  - `storyboard-architect/references/on-screen-text.md:8` [RECOMMEND] — 2. **Concept compression.** A short phrase lands harder than 4 seconds of narration.
  - `storyboard-architect/references/on-screen-text.md:9` [FORBID] — 3. **Stat or proof point.** Numbers stick visually in a way they don't audibly.
  - `storyboard-architect/references/shot-grammar.md:29` [RECOMMEND] — Default to eye-level. Use the others deliberately, not for variety.
  - `storyboard-architect/references/shot-grammar.md:3` [RECOMMEND] — Controlled vocabulary. Use these exact terms in `shots.json`. Generators interpret loose language inconsistently, locked vocabulary survives translati
  - `storyboard-architect/references/shot-grammar.md:33` [RECOMMEND] — | Code | Effect | Use when |
  - `storyboard-architect/references/shot-grammar.md:50` [REQUIRE] — | `shallow` | Subject sharp, background blurred |
  - `storyboard-architect/references/shot-grammar.md:54` [REQUIRE] — Default to shallow for talking-head, deep for environmental and schematic.
  - `storyboard-architect/references/shot-grammar.md:58` [FORBID] — Don't redefine per shot. Define once in `series_lock.lighting`. Examples:
  - `storyboard-architect/references/shot-grammar.md:90` [FORBID] — - **brand_lock**, locked across the entire project. Palette, type, "never" list.
  - `storyboard-architect/references/timing-rules.md:19` [REQUIRE] — The hook is 0–2s. Always. There are no exceptions in short-form content. Specifically:
  - `storyboard-architect/references/timing-rules.md:21` [REQUIRE] — - 9:16 social: first frame must telegraph the topic. Auto-play on mute means the first half-second is fighting a swipe.
  - `storyboard-architect/references/timing-rules.md:24` [RECOMMEND] — The hook shot framing should be high-contrast against the shots that follow. If shot 2 is MS, shot 1 should not be MS. Visual contrast = retention.
  - `storyboard-architect/references/timing-rules.md:3` [RECOMMEND] — Pacing is math, not feel. Use these as defaults. Override only with reason documented in rationale.
  - `storyboard-architect/references/timing-rules.md:30` [RECOMMEND] — - Last shot should hold long enough for someone to read the CTA text and act
  - `storyboard-architect/references/timing-rules.md:31` [FORBID] — - Don't put motion on the CTA shot, let the text breathe
  - `storyboard-architect/references/timing-rules.md:36` [FORBID] — A text overlay needs to be on screen long enough to be **read twice**. Not once, twice. Why: viewers are skimming, eyes don't always lock on first fra
  - `storyboard-architect/references/timing-rules.md:39` [REQUIRE] — - 1 short word (≤5 chars): 0.6s minimum read
  - `storyboard-architect/references/timing-rules.md:44` [REQUIRE] — Multiply by 2 for the "read twice" rule. So a 6-word phrase needs **2.4s on screen minimum**.
  - `storyboard-architect/references/timing-rules.md:47` [RECOMMEND] — 1. Shorten the copy
  - `storyboard-architect/references/timing-rules.md:48` [RECOMMEND] — 2. Carry the text across two consecutive shots (text persists during cut)
  - `storyboard-architect/references/timing-rules.md:49` [RECOMMEND] — 3. Lengthen the shot
  - `storyboard-architect/references/timing-rules.md:51` [FORBID] — Do not under-time text. It's the most common storyboard failure.
  - `storyboard-architect/references/timing-rules.md:79` [RECOMMEND] — 1. Sum of `(end - start)` across all shots equals project duration ±0.1s
  - `storyboard-architect/references/timing-rules.md:80` [RECOMMEND] — 2. No shot has `start >= end`
  - `storyboard-architect/references/timing-rules.md:81` [RECOMMEND] — 3. No two shots overlap
  - `storyboard-architect/references/timing-rules.md:82` [RECOMMEND] — 4. First shot starts at 0.0
  - `storyboard-architect/references/timing-rules.md:83` [RECOMMEND] — 5. Last shot ends at project duration
  - `storyboard-architect/references/timing-rules.md:84` [RECOMMEND] — 6. Every text overlay's `enter.at` is ≥ its shot's `start`
  - `storyboard-architect/references/timing-rules.md:85` [RECOMMEND] — 7. Every text overlay's `exit.at` is ≤ its shot's `end` (or carries to a flagged successor shot)
  - `storyboard-architect/references/timing-rules.md:86` [RECOMMEND] — 8. Every text overlay's on-screen duration ≥ read-twice threshold
  - `storyboard-html-preview/SKILL.md:10` [REQUIRE] — The constraint is non-negotiable: **single file, no build step, no server, works offline.** Any time the output requires "run this build command" or "
  - `storyboard-html-preview/SKILL.md:149` [PROCESS] — Resolve each shot's frame by the order in "What you produce" above, then reference it by a path relative to the output root:
  - `storyboard-html-preview/SKILL.md:158` [RECOMMEND] — For hard-copy print (a single file with no folder structure), the skill can offer to inline frames as base64. Ask the user which they prefer if frames
  - `storyboard-html-preview/SKILL.md:16` [PROCESS] — - Asks to preview, share, or export a storyboard
  - `storyboard-html-preview/SKILL.md:161` [REQUIRE] — If a shot's `assets.generated` entry carries a `sha256` and the file no longer matches it, render the frame but say so on the page. That mismatch mean
  - `storyboard-html-preview/SKILL.md:169` [REQUIRE] — **Template flag convention.** When composing the per-shot context for `preview.html.tpl`, set exactly one of:
  - `storyboard-html-preview/SKILL.md:18` [PROCESS] — - Says "what's the next step" after a storyboard-architect run
  - `storyboard-html-preview/SKILL.md:181` [REQUIRE] — It is an array because `shots.json` lets a shot carry several overlays and `text-overlays.json` always did. A single set of `overlay_*` fields could h
  - `storyboard-html-preview/SKILL.md:189` [PROCESS] — **Escape everything.** Subjects, rationales, VO lines, and overlay copy are model-generated prose that lands in both text and attribute contexts. One 
  - `storyboard-html-preview/SKILL.md:207` [PROCESS] — Include `@media print` rules that:
  - `storyboard-html-preview/SKILL.md:211` [PROCESS] — - Ensure text overlays render legibly
  - `storyboard-html-preview/SKILL.md:212` [PROCESS] — - Use black-on-white where brand colors won't print well
  - `storyboard-html-preview/SKILL.md:214` [RECOMMEND] — The user should be able to hit Cmd-P / Ctrl-P and get a clean PDF.
  - `storyboard-html-preview/SKILL.md:220` [REQUIRE] — The output is one `.html` file. If you find yourself wanting a separate stylesheet or JS file, inline it. If you find yourself wanting a build step, y
  - `storyboard-html-preview/SKILL.md:224` [REQUIRE] — No CDN scripts. No Google Fonts. No external CSS frameworks. The file must work with no internet connection.
  - `storyboard-html-preview/SKILL.md:226` [REQUIRE] — The exception: if the user explicitly opts in (e.g. "make it pretty, I'm online"), Tailwind via CDN is acceptable. Default is no.
  - `storyboard-html-preview/SKILL.md:23` [RECOMMEND] — One file: `preview.html`. Self-contained. Inline CSS. No JavaScript dependencies (vanilla JS only, embedded). No external font files (uses system stac
  - `storyboard-html-preview/SKILL.md:230` [RECOMMEND] — Hit Cmd-P. The result should be a clean PDF. If layout breaks across page boundaries, the print stylesheet is broken.
  - `storyboard-html-preview/SKILL.md:234` [REQUIRE] — Use brand colors as accents, not as full backgrounds. The reviewer's job is to read the storyboard, not admire the design. Subtle.
  - `storyboard-html-preview/SKILL.md:250` [GATE] — Before declaring done, verify:
  - `storyboard-html-preview/SKILL.md:252` [GATE] — - [ ] File opens in any browser (Chrome, Safari, Firefox) with no errors
  - `storyboard-html-preview/SKILL.md:253` [GATE] — - [ ] No external network requests fire on load
  - `storyboard-html-preview/SKILL.md:254` [GATE] — - [ ] Print preview produces a clean PDF
  - `storyboard-html-preview/SKILL.md:256` [GATE] — - [ ] Brand colors and fonts come from the brand-lock, not from a fallback
  - `storyboard-html-preview/SKILL.md:257` [GATE] — - [ ] Every shot from `shots.json` is present
  - `storyboard-html-preview/SKILL.md:258` [GATE] — - [ ] Every overlay referenced by a shot is rendered, including second and third overlays
  - `storyboard-html-preview/SKILL.md:259` [GATE] — - [ ] `brand_lock_ref` from `shots.json` is what the footer links to, not a hardcoded name
  - `storyboard-html-preview/SKILL.md:260` [GATE] — - [ ] The run date and the render date are both shown, and labelled differently
  - `storyboard-html-preview/SKILL.md:261` [GATE] — - [ ] No `{{` remains anywhere in the output
  - `storyboard-html-preview/SKILL.md:263` [GATE] — The CLI renderer checks the mechanical half of that list against itself:
  - `storyboard-html-preview/SKILL.md:271` [REQUIRE] — "Run" is when the storyboard was produced, read from `run.json`. "Rendered" is when the page was written. They are separate lines in the footer and th
  - `storyboard-html-preview/SKILL.md:40` [RECOMMEND] — 1. An entry in `shot.assets.generated` marked `accepted: true`
  - `storyboard-html-preview/SKILL.md:41` [RECOMMEND] — 2. The newest entry in `shot.assets.generated`
  - `storyboard-html-preview/SKILL.md:42` [RECOMMEND] — 3. `frames/round-{highest}/{shot_id}.{png,jpg,jpeg,webp}`
  - `storyboard-html-preview/SKILL.md:43` [RECOMMEND] — 4. `generated/{shot_id}.{ext}`, the pre-3.0.0 flat layout
  - `storyboard-html-preview/SKILL.md:55` [REQUIRE] — Required:
  - `storyboard-html-preview/SKILL.md:68` [PROCESS] — Validate before rendering, and stop if it fails:
  - `storyboard-html-preview/SKILL.md:82` [RECOMMEND] — The HTML preview should *feel* like the brand without going overboard. Quiet branding, not loud.
  - `storyboard-html-preview/SKILL.md:86` [PROCESS] — Use `templates/preview.html.tpl` as the structural template. Read it before generating.
  - `visual-asset-critic/SKILL.md:145` [REQUIRE] — **Provenance, all of it required at 1.1.** A verdict is a claim about specific bytes. Name them, and hash them:
  - `visual-asset-critic/SKILL.md:16` [PROCESS] — - Uploads or links a generated image with a question about quality
  - `visual-asset-critic/SKILL.md:165` [REQUIRE] — Every one of those fields is required, and every one is nullable. That combination is deliberate: `null` records that an input genuinely was not avail
  - `visual-asset-critic/SKILL.md:17` [PROCESS] — - Asks "does this match the storyboard"
  - `visual-asset-critic/SKILL.md:174` [GATE] — **Severity, assign one per issue.** This is the field the gate runs on, so map it from the layer rubric deterministically:
  - `visual-asset-critic/SKILL.md:18` [RECOMMEND] — - Says "review this render", "is this on-brand", "what should I change"
  - `visual-asset-critic/SKILL.md:182` [REQUIRE] — **Gating rule, the verdict is derived from severities, not chosen freely.** This guarantees the markdown verdict and the JSON verdict always agree:
  - `visual-asset-critic/SKILL.md:187` [PROCESS] — - Only `minor` issues, or none ⇒ verdict is `ACCEPT` (with post notes).
  - `visual-asset-critic/SKILL.md:189` [GATE] — The three-major rule used to read "escalate to REJECT at your discretion." Discretion in a gate is not a gate, and it disagreed with `references/criti
  - `visual-asset-critic/SKILL.md:19` [PROCESS] — - Has a generated image and a `shots.json` shot reference and wants QA
  - `visual-asset-critic/SKILL.md:193` [PROCESS] — Pick the markdown `## Verdict` by this same rule.
  - `visual-asset-critic/SKILL.md:197` [GATE] — Writing a schema-valid critique is not the same as passing the gate. Run it:
  - `visual-asset-critic/SKILL.md:203` [GATE] — Or check the whole tree at once, which also recomputes every hash against the files on disk:
  - `visual-asset-critic/SKILL.md:210` [GATE] — This step is not optional and it is not someone else's job. A critique that says `ACCEPT` while carrying a `major` issue is a bug, and the only reason
  - `visual-asset-critic/SKILL.md:240` [FORBID] — Generation is one stage in a pipeline. If the image is 80% right and the gap is fixable in post, that's an ACCEPT with post notes. Don't send the user
  - `visual-asset-critic/SKILL.md:26` [FORBID] — The JSON goes to `output/critiques/round-{N}/{shot_id}.critique.json`. One file per shot per round, never a shared filename. A 12-shot project reviewe
  - `visual-asset-critic/SKILL.md:263` [REQUIRE] — > - **Hand:** Re-roll required. Generate 2–3 more times with same prompt and pick a clean one.
  - `visual-asset-critic/SKILL.md:276` [GATE] — If the verdict is REJECT, do not offer that. REJECT means a blocking issue or three or more major ones, which is a failure with no clear fix path, and
  - `visual-asset-critic/SKILL.md:281` [FORBID] — Don't auto-revise. The user picks. The critique you just wrote is exactly what closes that loop.
  - `visual-asset-critic/SKILL.md:57` [REQUIRE] — | Input | Required? | Default if absent |
  - `visual-asset-critic/SKILL.md:60` [RECOMMEND] — | Shot ID + shots.json | Recommended | If absent, ask for shot intent in a sentence |
  - `visual-asset-critic/SKILL.md:61` [RECOMMEND] — | brand-lock.snapshot.md | Recommended | If absent, critique only on technical merits |
  - `visual-asset-critic/SKILL.md:64` [PROCESS] — If only the image is provided with no context, ask for one piece of information: **what was this shot supposed to be?** A single sentence is enough to
  - `visual-asset-critic/SKILL.md:77` [FORBID] — If you can't establish intent in one sentence, ask. Don't critique blind.
  - `visual-asset-critic/SKILL.md:81` [PROCESS] — Read `references/critique-rubric.md` for the full rubric. Quick version, check the image against:
  - `visual-asset-critic/SKILL.md:83` [FORBID] — 1. **Brand Lock**, does it respect palette, mood, "never" list?
  - `visual-asset-critic/SKILL.md:84` [PROCESS] — 2. **Series Lock**, does it match character/environment/lighting anchors?
  - `visual-asset-critic/SKILL.md:85` [PROCESS] — 3. **Shot Spec**, does framing/angle/composition match the spec?
  - `visual-asset-critic/SKILL.md:86` [PROCESS] — 4. **Composition**, does it reserve space for on-screen text if applicable?
  - `visual-asset-critic/SKILL.md:88` [PROCESS] — 6. **Continuity**, if previous shots in the series are available, does it match?
  - `visual-asset-critic/SKILL.md:90` [PROCESS] — For each layer, note: pass / soft fail / hard fail. The verdict aggregates these.
  - `visual-asset-critic/SKILL.md:94` [REQUIRE] — For every "not working" point, the critique must say what to do about it. Three buckets:
  - `visual-asset-critic/SKILL.md:99` [PROCESS] — **Post-level fix**, acceptable to address in compositing. Specify what: > "Color grade is slightly cool, push warmth +5 in post, no need to re-generat
  - `visual-asset-critic/references/critique-rubric.md:101` [FORBID] — Soft fails are noted but don't change the verdict on their own. If you have three or more of them, look again: a cluster of soft fails usually means o
  - `visual-asset-critic/references/critique-rubric.md:108` [FORBID] — - **Don't pile-on once verdict is set**, if you're rejecting, list the issues that drive the rejection; don't list every cosmetic concern
  - `visual-asset-critic/references/critique-rubric.md:109` [REQUIRE] — - **Be specific, always**, "lighting is off" is not a critique; "key light is camera-right but series_lock says camera-left" is
  - `visual-asset-critic/references/critique-rubric.md:11` [FORBID] — | "Never" list | None of the items in the never list are present | One item in the never list shows softly | Multiple never-list violations |
  - `visual-asset-critic/references/critique-rubric.md:110` [RECOMMEND] — - **Cite the layer**, every issue gets tagged with which layer it falls under. This makes the fix path obvious
  - `visual-asset-critic/references/critique-rubric.md:14` [RECOMMEND] — Hard fail on Brand Lock = REJECT or REVISE depending on whether prompt fix exists.
  - `visual-asset-critic/references/critique-rubric.md:25` [RECOMMEND] — Hard fail on Series Lock = REJECT (continuity break) or REVISE if specific fix available.
  - `visual-asset-critic/references/critique-rubric.md:3` [RECOMMEND] — The structured layer-by-layer pass. Use this as the checklist when reviewing a generated image.
  - `visual-asset-critic/references/critique-rubric.md:34` [REQUIRE] — | Depth of field | Matches if specified | Slight DOF variation | Deep when shallow was specified |
  - `visual-asset-critic/references/critique-rubric.md:36` [RECOMMEND] — Soft fail = post-level fix or accept. Hard fail = revise.
  - `visual-asset-critic/references/critique-rubric.md:59` [REQUIRE] — Technical hard fails are almost always **re-roll required**. The prompt was probably fine; the generator just produced a bad sample. Budget 2–3 re-rol
  - `visual-asset-critic/references/critique-rubric.md:70` [REQUIRE] — Continuity hard fails break the storyboard. REVISE with verbatim-anchor checks on the prompt.
  - `visual-asset-critic/references/critique-rubric.md:74` [GATE] — The tables above grade each check as pass, soft fail, or hard fail. The JSON critique records a severity instead, and the verdict is derived from thos
  - `visual-asset-critic/references/critique-rubric.md:96` [REQUIRE] — `tools/validate_critique.py` enforces exactly this table, so a critique that disagrees with it fails rather than shipping. Earlier versions of this fi
  - `visual-prompt-forge/SKILL.md:100` [FORBID] — Each adapter file documents the prompting style, parameter syntax, and known pitfalls for that generator. You **must** read the adapter before writing
  - `visual-prompt-forge/SKILL.md:102` [FORBID] — **`adapters/_capabilities.json` is the single source of truth for per-generator limits** (`max_prompt_words`, `supports_text_render`, `supports_motion
  - `visual-prompt-forge/SKILL.md:119` [FORBID] — 1. Pull brand-lock palette, mood, "never" list
  - `visual-prompt-forge/SKILL.md:120` [PROCESS] — 2. Pull series_lock character/environment/lighting
  - `visual-prompt-forge/SKILL.md:121` [PROCESS] — 3. Pull shot framing/angle/motion/subject
  - `visual-prompt-forge/SKILL.md:122` [FORBID] — 4. **Strip any on_screen_text reference**, text never goes in the prompt
  - `visual-prompt-forge/SKILL.md:123` [PROCESS] — 5. Apply the generator adapter's syntax wrapper
  - `visual-prompt-forge/SKILL.md:124` [PROCESS] — 6. Append generator-specific parameters (aspect ratio, style flags, seed if applicable)
  - `visual-prompt-forge/SKILL.md:166` [PROCESS] — This is the only writeable part of `run.json`. Everything else was fixed when the architect wrote it.
  - `visual-prompt-forge/SKILL.md:173` [PROCESS] — > "Want me to QA the generated images against the storyboard? Use `visual-asset-critic` once you have the renders."
  - `visual-prompt-forge/SKILL.md:19` [PROCESS] — - Wants the same shot adapted to multiple generators
  - `visual-prompt-forge/SKILL.md:194` [PROCESS] — 1. Read every critique under `output/critiques/round-{N}/`, where N is the highest round present. Each file is one shot's verdict (`shot_id`, `verdict
  - `visual-prompt-forge/SKILL.md:196` [PROCESS] — 2. Skip any with `verdict: ACCEPT`. Those are done.
  - `visual-prompt-forge/SKILL.md:197` [PROCESS] — 3. **Stop on `REJECT`.** A REJECT means the critic found a blocking issue, or three or more major ones: a failure with no clear fix path. Re-emitting 
  - `visual-prompt-forge/SKILL.md:203` [PROCESS] — 4. For every `REVISE` shot, walk its `issues[]` and branch on `fix_type`:
  - `visual-prompt-forge/SKILL.md:211` [PROCESS] — 5. A shot whose issues are all `post-level` needs no new prompt. Leave it out of the revised file and add its id to `post_only_shots` on the new round
  - `visual-prompt-forge/SKILL.md:219` [PROCESS] — Write `output/prompts/round-{N+1}/revised-{generator}.txt` containing only the revised shots, then append the round to `run.json`. Annotate each shot 
  - `visual-prompt-forge/SKILL.md:230` [PROCESS] — The block header leads with the shot id, same as a full pass. `tools/copy-prompt.py` identifies a block by the shot id near the start of the line, so 
  - `visual-prompt-forge/SKILL.md:235` [PROCESS] — Tell the user which shots were revised, which need only post work, which were rejected, and which were already ACCEPT. Then they generate the revised 
  - `visual-prompt-forge/SKILL.md:241` [RECOMMEND] — Given the same `shots.json`, the same brand-lock, and the same critique, this should produce the same revised prompt. Nothing in the file format fight
  - `visual-prompt-forge/SKILL.md:245` [FORBID] — What the format cannot guarantee is the judgement in between. Applying a `fix` field means reading a sentence of English and editing prose, so hold yo
  - `visual-prompt-forge/SKILL.md:253` [REQUIRE] — These are non-negotiable. Violating them produces broken output even if the prompt looks fine.
  - `visual-prompt-forge/SKILL.md:261` [FORBID] — Colors come from the series_lock color_grade and the brand_lock palette. They get rendered into the prompt by the adapter. Don't write "deep navy blaz
  - `visual-prompt-forge/SKILL.md:265` [REQUIRE] — The series_lock `environment`, `lighting`, and `color_grade` strings flow into every prompt **verbatim**. This is what produces visual consistency acr
  - `visual-prompt-forge/SKILL.md:284` [REQUIRE] — This rule is enforced now, not trusted:
  - `visual-prompt-forge/SKILL.md:290` [REQUIRE] — It exists because a careful authoring pass over a seven-shot storyboard drifted on these anchors in all seven shots while every other validator stayed
  - `visual-prompt-forge/SKILL.md:301` [REQUIRE] — - **Where the body sits in frame.** Which third it occupies. On a piece that composites two eras with a vertical mask, a body sitting on the centre li
  - `visual-prompt-forge/SKILL.md:304` [FORBID] — - **Nothing that contradicts the camera.** A subject who walks away from camera cannot also keep the same size in frame.
  - `visual-prompt-forge/SKILL.md:306` [REQUIRE] — - **No brand marks.** Logos and lettering are composited in post. Generators deform them.
  - `visual-prompt-forge/SKILL.md:310` [REQUIRE] — Every prompt is composed from the same inputs the same way. If two consecutive runs produce different prompts for the same shot, the skill is broken. 
  - `visual-prompt-forge/SKILL.md:320` [RECOMMEND] — One file per generator. Read these on demand, only for the generators being targeted.
  - `visual-prompt-forge/SKILL.md:337` [GATE] — Run the validator. Do not eyeball this list.
  - `visual-prompt-forge/SKILL.md:344` [GATE] — `validate_prompts.py` checks the mechanical half, which is everything that used to be a checkbox here:
  - `visual-prompt-forge/SKILL.md:347` [GATE] — - the header names the storyboard, generator, aspect, brand-lock, run, and round
  - `visual-prompt-forge/SKILL.md:348` [GATE] — - the generator is a real id in `_capabilities.json`
  - `visual-prompt-forge/SKILL.md:349` [GATE] — - the header aspect matches `project.aspect`
  - `visual-prompt-forge/SKILL.md:350` [GATE] — - no prompt exceeds that generator's `max_prompt_words` ceiling
  - `visual-prompt-forge/SKILL.md:351` [GATE] — - a full pass covers every shot; a revision file covers a subset of real shots
  - `visual-prompt-forge/SKILL.md:352` [GATE] — - no shot block is duplicated, and none has a header with no body
  - `visual-prompt-forge/SKILL.md:353` [GATE] — - **Rule 1**: no on-screen text copy appears in any prompt
  - `visual-prompt-forge/SKILL.md:362` [GATE] — - [ ] One output file per requested generator
  - `visual-prompt-forge/SKILL.md:363` [GATE] — - [ ] On a revision pass, the shots you left out are accounted for as ACCEPT, post-only, or rejected, and you said which is which
  - `visual-prompt-forge/SKILL.md:365` [GATE] — - [ ] Generator-specific parameters are right for the surface the user will paste into
  - `visual-prompt-forge/SKILL.md:366` [GATE] — - [ ] The round is appended to `run.json` with a hash per prompt file
  - `visual-prompt-forge/SKILL.md:367` [GATE] — - [ ] The prompt actually describes the shot, which is the part no validator will ever do
  - `visual-prompt-forge/SKILL.md:42` [RECOMMEND] — Round 1 is the first pass. Revision mode writes `output/prompts/round-2/`, and so on. The round in the path is not decoration: prompt files used to be
  - `visual-prompt-forge/SKILL.md:53` [FORBID] — 1. **Brand Lock**, palette, type, mood, "never" list (constant across project)
  - `visual-prompt-forge/SKILL.md:54` [RECOMMEND] — 2. **Series Lock**, character/environment/lighting anchors (constant across storyboard)
  - `visual-prompt-forge/SKILL.md:55` [RECOMMEND] — 3. **Shot Spec**, framing, angle, motion, subject (per shot)
  - `visual-prompt-forge/SKILL.md:56` [FORBID] — 4. **Text Layer**, **never in the prompt**, composited separately
  - `visual-prompt-forge/SKILL.md:57` [RECOMMEND] — 5. **Generator Adapter**, model-specific syntax wrapper
  - `visual-prompt-forge/SKILL.md:67` [REQUIRE] — - `shots.json` (required), the structured shot list
  - `visual-prompt-forge/SKILL.md:68` [REQUIRE] — - `brand-lock.snapshot.md` (required), referenced from shots.json
  - `visual-prompt-forge/SKILL.md:69` [REQUIRE] — - Target generators (required), ask if not specified
  - `visual-prompt-forge/SKILL.md:71` [PROCESS] — Validate before composing:
  - `visual-prompt-forge/SKILL.md:77` [FORBID] — If the brand-lock is missing or `shots.json` does not validate, stop and tell the user. Don't try to forge prompts from incomplete data.
  - `visual-prompt-forge/SKILL.md:80` [FORBID] — If `tools/` is not on hand (a Claude.ai upload, or a single-skill install), read the schema from `../storyboard-architect/templates/shots.schema.json`
  - `visual-prompt-forge/SKILL.md:95` [PROCESS] — - `adapters/kling.md` (motion video, default)
  - `visual-prompt-forge/adapters/flux.md:40` [RECOMMEND] — Translate shot grammar into descriptive language:
  - `visual-prompt-forge/adapters/flux.md:48` [REQUIRE] — | `shallow DOF` | `Shot at f/1.8 with shallow depth of field, background softly out of focus.` |
  - `visual-prompt-forge/adapters/flux.md:92` [FORBID] — - **Don't enable prompt upsampling for series work**, fal.ai's auto-rewrite produces inconsistent shots
  - `visual-prompt-forge/adapters/flux.md:94` [REQUIRE] — - **Don't omit the photoreal closing line**, the "no AI artifacts" anchor measurably reduces the AI-look
  - `visual-prompt-forge/adapters/gpt-image.md:30` [RECOMMEND] — Document in comment:
  - `visual-prompt-forge/adapters/gpt-image.md:48` [RECOMMEND] — Use this when the shot's composition is load-bearing.
  - `visual-prompt-forge/adapters/gpt-image.md:78` [RECOMMEND] — - Specify position explicitly ("centered in the lower third")
  - `visual-prompt-forge/adapters/gpt-image.md:79` [RECOMMEND] — - Specify approximate typeface character ("bold sans-serif", "elegant serif")
  - `visual-prompt-forge/adapters/gpt-image.md:87` [REQUIRE] — - **Don't omit spatial language when the shot has specific composition**, you're paying for the model's strength; use it
  - `visual-prompt-forge/adapters/gpt-image.md:88` [FORBID] — - **Don't pile too many objects**, five or fewer distinct elements per scene; more degrades fidelity
  - `visual-prompt-forge/adapters/ideogram.md:15` [RECOMMEND] — Use when the on-screen text is meant to appear as part of the image itself, a poster headline, a sign in the scene, a packaging label. This is the onl
  - `visual-prompt-forge/adapters/ideogram.md:17` [REQUIRE] — **To trigger Mode 2, the shot must have an explicit override flag in rationale**, e.g.:
  - `visual-prompt-forge/adapters/ideogram.md:22` [FORBID] — If you don't see that override flag, default to Mode 1.
  - `visual-prompt-forge/adapters/ideogram.md:42` [RECOMMEND] — Document in comment block:
  - `visual-prompt-forge/adapters/ideogram.md:7` [RECOMMEND] — This adapter has **two modes**: composited (default) and text-in-image (override).
  - `visual-prompt-forge/adapters/ideogram.md:90` [FORBID] — - **Don't use Mode 2 without the rationale override**, defaults to text-in-image cause double-text (composited + generated) which destroys the comp
  - `visual-prompt-forge/adapters/ideogram.md:91` [FORBID] — - **Don't trust magic_prompt**, it auto-rewrites and produces inconsistent shots across a series
  - `visual-prompt-forge/adapters/ideogram.md:94` [REQUIRE] — - **Don't forget seed**, for any series work, lock the seed at the storyboard level
  - `visual-prompt-forge/adapters/midjourney.md:100` [FORBID] — - **Don't use `--c` for series work**, chaos kills consistency
  - `visual-prompt-forge/adapters/midjourney.md:101` [FORBID] — - **Don't change `--seed` mid-storyboard**, set once at series_lock level
  - `visual-prompt-forge/adapters/midjourney.md:17` [RECOMMEND] — | Param | Values | Default to use | Notes |
  - `visual-prompt-forge/adapters/midjourney.md:22` [RECOMMEND] — | `--c` | 0–100 | omit | Chaos. Use only when exploring variations |
  - `visual-prompt-forge/adapters/midjourney.md:34` [RECOMMEND] — Translate shot grammar into Midjourney-friendly phrases:
  - `visual-prompt-forge/adapters/midjourney.md:43` [REQUIRE] — | `shallow DOF` | `shallow depth of field, f/1.8, bokeh background` |
  - `visual-prompt-forge/adapters/midjourney.md:56` [REQUIRE] — Pull verbatim from `series_lock.lighting`.
  - `visual-prompt-forge/adapters/midjourney.md:97` [FORBID] — - **Don't use "AI" or "rendered"**, produces stylized outputs that look generated
  - `visual-prompt-forge/adapters/midjourney.md:98` [FORBID] — - **Don't over-stack adjectives**, three adjectives per noun phrase max
  - `visual-prompt-forge/adapters/midjourney.md:99` [FORBID] — - **Don't include text content**, even if the shot has `on_screen_text`, leave it out. Composited separately.
  - `visual-prompt-forge/adapters/nano-banana.md:103` [FORBID] — - **Don't pile multiple modifications in one image-to-image prompt**, one change per pass produces cleaner results
  - `visual-prompt-forge/adapters/nano-banana.md:34` [RECOMMEND] — Document:
  - `visual-prompt-forge/adapters/nano-banana.md:88` [PROCESS] — - A modification template comment showing how to use the result for variants:
  - `visual-prompt-forge/adapters/seedream.md:30` [RECOMMEND] — Document:
  - `visual-prompt-forge/adapters/seedream.md:38` [FORBID] — **40–70 words per prompt**. Shorter than most. Don't pad.
  - `visual-prompt-forge/adapters/seedream.md:75` [FORBID] — - **Don't vary** the lighting language between shots, series_lock string in, no paraphrasing
  - `visual-prompt-forge/adapters/seedream.md:81` [FORBID] — - **Don't use `--ar` syntax**, pass aspect_ratio as a parameter
  - `visual-prompt-forge/adapters/seedream.md:84` [REQUIRE] — - **Don't skip the seed lock for series work**, without it, character consistency breaks
  - `visual-prompt-forge/references/consistency-locks.md:116` [FORBID] — - **Numbering shots in the prompt** ("shot 3 of 7, same as before"), generators don't have memory across calls
  - `visual-prompt-forge/references/consistency-locks.md:118` [FORBID] — - **Asking for "exactly the same"**, there is no such thing in stateless image gen; you reduce drift, you don't eliminate it
  - `visual-prompt-forge/references/consistency-locks.md:120` [FORBID] — Accept that some shots will need re-rolls. Budget for it. The locks reduce the failure rate; they don't eliminate it.
  - `visual-prompt-forge/references/consistency-locks.md:25` [REQUIRE] — Even small variations compound. Lock the string. Repeat verbatim.
  - `visual-prompt-forge/references/consistency-locks.md:33` [RECOMMEND] — Same principle for `series_lock.lighting`. Lighting direction in particular is critical, flipping window-left to window-right between shots produces o
  - `visual-prompt-forge/references/consistency-locks.md:60` [RECOMMEND] — 1. Generate the hero shot first (any shot, usually `shot_01` or whichever is most defining)
  - `visual-prompt-forge/references/consistency-locks.md:61` [RECOMMEND] — 2. Use that image as the reference for every subsequent shot
  - `visual-prompt-forge/references/consistency-locks.md:84` [REQUIRE] — A subtle one that breaks scenes when violated. If `series_lock.lighting` says "soft natural side-light, large window LEFT", then every shot's lighting
  - `visual-prompt-forge/references/consistency-locks.md:86` [RECOMMEND] — When a shot reverses character orientation (e.g., over-the-shoulder reverse), update the rationale to acknowledge the lighting flip:
  - `visual-prompt-forge/references/consistency-locks.md:9` [REQUIRE] — The most effective single technique. The character is described in `series_lock.character` once, and that exact string appears in every shot's prompt 
  - `visual-prompt-forge/references/failure-modes.md:102` [REQUIRE] — - Audit every prompt against series_lock and brand-lock, verbatim check
  - `visual-prompt-forge/references/failure-modes.md:119` [RECOMMEND] — - Include a one-phrase intent at the end ("the moment of recognition", "the calm before the decision")
  - `visual-prompt-forge/references/failure-modes.md:122` [FORBID] — **Accept editorially when:** generation is close enough that retouching gets there. Don't burn API credits chasing perfect on-prompt.
  - `visual-prompt-forge/references/failure-modes.md:128` [FORBID] — 1. You've re-rolled the same shot 5+ times with no improvement → the prompt is fine; the model can't render this concept; pick a different shot or dif
  - `visual-prompt-forge/references/failure-modes.md:13` [FORBID] — - No "never" list applied from brand-lock
  - `visual-prompt-forge/references/failure-modes.md:132` [FORBID] — Generation is one stage in a pipeline. Don't try to make it the whole pipeline.
  - `visual-prompt-forge/references/failure-modes.md:16` [RECOMMEND] — - Add specific lens and aperture ("50mm prime, f/2.0")
  - `visual-prompt-forge/references/failure-modes.md:19` [FORBID] — - Verify brand-lock "never" list is being applied, if it includes "no AI uncanny", surface that into the prompt
  - `visual-prompt-forge/references/failure-modes.md:29` [REQUIRE] — - Series_lock character string paraphrased rather than verbatim
  - `visual-prompt-forge/references/failure-modes.md:35` [REQUIRE] — - Verify character string is verbatim across every prompt
  - `visual-prompt-forge/references/failure-modes.md:36` [RECOMMEND] — - Add 1–2 more specific features ("small scar above left eyebrow", "black wireframe glasses")
  - `visual-prompt-forge/references/failure-modes.md:65` [REQUIRE] — - Lighting language paraphrased rather than verbatim from series_lock
  - `visual-prompt-forge/references/failure-modes.md:70` [REQUIRE] — - Verify lighting string is verbatim across prompts
  - `visual-prompt-forge/references/failure-modes.md:72` [RECOMMEND] — - For reverse-angle shots, flag in rationale and update lighting language for that shot only
  - `visual-prompt-forge/references/failure-modes.md:83` [RECOMMEND] — - Generator interpreting "centered subject" by default
  - `visual-prompt-forge/references/failure-modes.md:86` [RECOMMEND] — - Add explicit composition note: "subject framed in left third, right two-thirds open for text overlay"
  - `visual-prompt-forge/references/prompt-anatomy.md:16` [FORBID] — - "Never" list (things this brand never does, e.g. "no stock photo aesthetic", "no AI uncanny", "no over-saturated", "no shouting copy")
  - `visual-prompt-forge/references/prompt-anatomy.md:20` [REQUIRE] — This layer answers: **what does the brand always look and feel like?**
  - `visual-prompt-forge/references/prompt-anatomy.md:64` [RECOMMEND] — 1. **Editability.** Composited text can be revised without re-generating images.
  - `visual-prompt-forge/references/prompt-anatomy.md:67` [RECOMMEND] — 4. **Brand control.** Composited text uses exact brand fonts and exact brand colors. Generated text approximates.
  - `visual-prompt-forge/references/prompt-anatomy.md:75` [RECOMMEND] — This is the only layer the skill *applies* (vs. reads). Layers 1–4 are inputs; Layer 5 is the renderer that turns inputs into a generator-specific str
  - `visual-prompt-forge/references/prompt-anatomy.md:98` [FORBID] — The adapter pulls from Layers 1–3 and produces a string. Layer 4 lives parallel and never enters the prompt.

## SIN REFERENCIA (TEXTO A IMAGEN) (`references.count = 0`) — 4 reglas propias

  - `brand-lock-extractor/brand-packs/README.md:36` [FORBID] — Don't hand-author from scratch if the brand already exists. The **`brand-lock-extractor`** skill (ships in this repo at `skills/brand-lock-extractor/`
  - `storyboard-architect/brand-packs/README.md:36` [FORBID] — Don't hand-author from scratch if the brand already exists. The **`brand-lock-extractor`** skill (ships in this repo at `skills/brand-lock-extractor/`
  - `visual-prompt-forge/SKILL.md:21` [PROCESS] — If the user wants to build a storyboard from scratch (no shots.json yet), use `storyboard-architect` first, then chain into this skill.
  - `visual-prompt-forge/adapters/nano-banana.md:87` [PROCESS] — - The text-to-image prompt (for first-pass generation)

### CON PERSONAS — 72 reglas propias

  - `ai-production-director/SKILL.md:52` [PROCESS] — | Narrativa | Un beat (hook→payoff) | Arco simple | Multi-escena, personajes |
  - `aurora-prompt-linter/SKILL.md:158` [RECOMMEND] — - **Sub-tags por categoría**: O.upper / O.lower / P.face / P.body no soportados — un ref tagueado como O cubre todo outfit. Si el ref solo muestra el 
  - `aurora-prompt-linter/references/README.md:97` [RECOMMEND] — 6. **Exenciones**: términos en contexto de motion/cámara o como anchor direccional (`away from her face`, `across the climbing wall`) NO se flaggean.
  - `brand-lock-extractor/SKILL.md:20` [PROCESS] — - Hands over a URL, a PDF, image files, or a written brand description and asks for a brand-lock
  - `brand-lock-extractor/references/extraction-rubric.md:59` [FORBID] — - Imagery: no stock-photo gloss? no people? no gradients? no clip-art icons? Each absence is a never.
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:64` [PROCESS] — - **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 
  - `image/references/creative-direction.md:34` [REQUIRE] — - Hasselblad — medium format, shallow DOF, fashion/portrait
  - `image/references/creative-direction.md:47` [RECOMMEND] — - "Waist-up portrait", "full body", "over-the-shoulder"
  - `image/references/golden-rules.md:16` [REQUIRE] — - ✅ "solo portrait" → ❌ "no other people"
  - `image/references/gpt-image.md:94` [RECOMMEND] — **Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows s
  - `image/references/multi-panel.md:210` [REQUIRE] — - Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
  - `image/references/multi-panel.md:294` [REQUIRE] — **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space) **Model:** GPT Image 2 `quality: high` (text-heavy — scene number
  - `image/references/multi-panel.md:308` [REQUIRE] — **Subject consistency:** Always include an explicit instruction: "same person / same character / same product across all panels." Repeat key identity 
  - `image/references/multi-panel.md:57` [RECOMMEND] — **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/patterns/character-design.md:106` [RECOMMEND] — **Key levers:** `{character_name}`, `{character_description_simplified}` (key outfit and hair only), `{face_markers}` (e.g. round glasses, scar on lef
  - `image/references/patterns/character-design.md:120` [RECOMMEND] — Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional con
  - `image/references/patterns/character-design.md:29` [RECOMMEND] — Use to produce a grid of 6–9 facial expressions for the same character — consistent head angle and art style, with emotion labels under each face.
  - `image/references/patterns/character-design.md:58` [RECOMMEND] — Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
  - `image/references/patterns/fashion-editorial.md:33` [RECOMMEND] — Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
  - `image/references/patterns/portrait-cinema.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/patterns/portrait-cinema.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
  - `image/references/patterns/portrait-cinema.md:61` [RECOMMEND] — **Key levers:** `{person_description}`, `{direction}` (left, right), `{hair_detail}` (tight buzz cut showing skull contour, shoulder-length hair with 
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:83` [RECOMMEND] — Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elem
  - `image/references/patterns/portrait-cinema.md:9` [RECOMMEND] — Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
  - `image/references/patterns/portrait-cinema.md:97` [RECOMMEND] — **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)
  - `image/references/patterns/poster-illustration.md:117` [RECOMMEND] — **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/patterns/ui-social.md:116` [RECOMMEND] — Use to create a visual color analysis graphic from a portrait — seasonal palette classification, clothing color comparisons, and accessory recommendat
  - `image/references/patterns/ui-social.md:133` [REQUIRE] — **Key levers:** `{subject_description}` (age, skin tone, hair color, eye color — needed for accurate seasonal analysis), `{season_type}` (Warm Spring,
  - `image/references/prompt-framework.md:213` [RECOMMEND] — 2. **Micro-textures** — "visible pores on skin, individual hair strands catching backlight, fabric weave pattern on linen shirt, grain of weathered wo
  - `image/references/prompt-framework.md:218` [RECOMMEND] — 7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby si
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"
  - `image/references/vision-decomposer.md:36` [PROCESS] — - **Figure & ground (Arnheim):** degree of subject isolation, overlapping of forms, mass relationships. Use of reflections (mirrors, windows) to expan
  - `image/references/vision-decomposer.md:44` [PROCESS] — - **Broken light & reflexes (Zheleznyakov):** use of shadow masks (gobos), light through blinds / foliage, color reflexes from neighboring objects ont
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `learned/production-learnings.v3.2.json:3` [REQUIRE] — Preserve a sufficiently specific domain-native pose/technique label instead of expanding it into speculative anatomy. Expand only when the target adap
  - `learned/production-learnings.v3.2.json:8` [RECOMMEND] — For complex underwater human anatomy, physically justified bubbles/turbulence may obscure non-critical anatomical detail when the brief does not requi
  - `produccion-visual-sw30/SKILL.md:116` [GATE] — 1. Un solo trabajo por generación. Con dos personajes: un sujeto por generación, o técnica de colocación probada; nunca "a ver si sale".
  - `produccion-visual-sw30/SKILL.md:123` [GATE] — 5. Herencia mínima: "same face and clothes" + solo los deltas. Cero re-descripción de lo que la referencia ya muestra.
  - `produccion-visual-sw30/SKILL.md:130` [GATE] — 9. Contactos entre personas: "a natural high five" — la anatomía la fija el keyframe aprobado, nunca la asignación de manos por texto.
  - `produccion-visual-sw30/SKILL.md:35` [GATE] — 1. **CATALOGAR** — identificar el TIPO de prompt y leer qué reglas aplican a ese tipo en la matriz (production-package/RULES_MATRIX.md: 26 reglas × 5 
  - `produccion-visual-sw30/SKILL.md:39` [GATE] — 2. **DEFINIR SECCIONES** — antes de redactar, listar las secciones que ese tipo exige. Cada regla vive en UN bloque nombrado y compartido (optics_*, s
  - `storyboard-architect/SKILL.md:18` [PROCESS] — - Hands over a script, brief, or concept document expecting structured pre-production output
  - `storyboard-architect/SKILL.md:266` [GATE] — - [ ] `series_lock` anchors are specific enough to reproduce (not "a person in a room")
  - `storyboard-architect/references/beat-frameworks.md:33` [RECOMMEND] — Default for personal-brand video where a person speaks to camera. Five micro-beats:
  - `storyboard-architect/references/beat-frameworks.md:41` [RECOMMEND] — Use when: founder content, thought leadership, personal-brand pieces.
  - `storyboard-html-preview/SKILL.md:19` [PROCESS] — - Hands off `storyboard.md` + `shots.json` + asks for a deliverable for review
  - `visual-asset-critic/SKILL.md:102` [REQUIRE] — **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts: > "Hands are mangled. This is a known Fl
  - `visual-asset-critic/SKILL.md:224` [REQUIRE] — "Looks great" / "feels off" without specifics is not a critique. Every observation must reference something in the image (composition, color, anatomy,
  - `visual-asset-critic/SKILL.md:236` [FORBID] — Some failures (mangled hands, weird eye reflections, jewelry shimmer) are known generator weaknesses. Surface them as such, don't pretend a different 
  - `visual-asset-critic/SKILL.md:24` [GATE] — **Two artifacts from every review, always both:** a human-readable markdown critique (the primary surface) and a machine-readable critique JSON (so a 
  - `visual-asset-critic/SKILL.md:87` [PROCESS] — 5. **Technical**, skin texture, hands, eyes, anatomy, AI artifacts?
  - `visual-asset-critic/SKILL.md:96` [REQUIRE] — **Prompt-level fix**, change the prompt and re-roll. Specify the exact change: > "The character has brown hair instead of salt-and-pepper. Add 'salt-a
  - `visual-asset-critic/references/critique-rubric.md:111` [REQUIRE] — - **Distinguish prompt failure from generator failure**, if the prompt was fine and the generator produced garbage hands, that's "re-roll required", n
  - `visual-prompt-forge/SKILL.md:16` [PROCESS] — - Hands over a `shots.json` (or any structured shot list) and asks for prompts
  - `visual-prompt-forge/SKILL.md:186` [FORBID] — This is what `visual-asset-critic`'s structured output is for. When the user hands you `shots.json` plus one or more `critique.json` files (the machin
  - `visual-prompt-forge/SKILL.md:190` [RECOMMEND] — The user says "apply the critique", "revise the failed shots", "re-roll what didn't pass", or hands over an output tree containing `critiques/`.
  - `visual-prompt-forge/SKILL.md:215` [PROCESS] — 6. Re-apply the five-layer anatomy and the same adapter as the original run.
  - `visual-prompt-forge/SKILL.md:281` [REQUIRE] — `character` is a warning rather than an error, because a shot with no person in it can legitimately leave it out. When the shot has a person, it is ve
  - `visual-prompt-forge/SKILL.md:305` [REQUIRE] — - **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no
  - `visual-prompt-forge/adapters/flux.md:66` [REQUIRE] — The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.
  - `visual-prompt-forge/adapters/gpt-image.md:46` [RECOMMEND] — - "The subject's shoulders are angled 30 degrees toward the camera, face turned to look at the off-frame light source."
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/references/consistency-locks.md:113` [FORBID] — A few things people try that don't actually fix consistency:
  - `visual-prompt-forge/references/consistency-locks.md:115` [FORBID] — - **Adding "consistent character" or "same person" to the prompt**, generators don't read meta-instructions
  - `visual-prompt-forge/references/consistency-locks.md:70` [RECOMMEND] — **This is the most effective lock for character consistency** in 2026. Use it whenever the storyboard features the same person across multiple shots.
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)

#### UNA PERSONA — 1 reglas propias

  - `produccion-visual-sw30/SKILL.md:116` [GATE] — 1. Un solo trabajo por generación. Con dos personajes: un sujeto por generación, o técnica de colocación probada; nunca "a ver si sale".

##### 0 · personas · 1 → style.photography = `editorial` (editorial) — 16 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/multi-panel.md:57` [RECOMMEND] — **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:33` [RECOMMEND] — Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:9` [RECOMMEND] — Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 
  - `visual-asset-critic/SKILL.md:20` [PROCESS] — - Has a generated image and just wants editorial feedback (no storyboard reference)
  - `visual-asset-critic/SKILL.md:8` [FORBID] — You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structu
  - `visual-prompt-forge/adapters/nano-banana.md:82` [PROCESS] — 3. Get 4–8 variants of the same shot for editorial selection
  - `visual-prompt-forge/references/consistency-locks.md:109` [FORBID] — Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.
  - `visual-prompt-forge/references/failure-modes.md:130` [RECOMMEND] — 3. The image is 80% right and the gap is editorial → ship to post and let the editor finish
  - `visual-prompt-forge/references/failure-modes.md:3` [FORBID] — What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

##### 0 · personas · 1 → style.photography = `documental` (documental / fotoperiodismo) — 1 reglas

  - `produccion-visual-sw30/SKILL.md:73` [GATE] — | usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO

##### 0 · personas · 1 → style.photography = `natgeo` (documental de naturaleza (National Geographic)) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → style.photography = `moda` (moda) — 8 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/creative-direction.md:34` [REQUIRE] — - Hasselblad — medium format, shallow DOF, fashion/portrait
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/character-design.md:58` [RECOMMEND] — Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o

##### 0 · personas · 1 → style.photography = `producto` (producto / e-commerce) — 1 reglas

  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)

##### 0 · personas · 1 → style.photography = `cinematografico` (cinematográfico) — 9 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:67` [RECOMMEND] — The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site 
  - `image/SKILL.md:64` [PROCESS] — - **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 
  - `image/SKILL.md:69` [PROCESS] — - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - `image/SKILL.md:80` [PROCESS] — Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / stand
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/nano-banana.md:25` [RECOMMEND] — - Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `visual-asset-critic/references/critique-rubric.md:107` [FORBID] — - **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
  - `visual-prompt-forge/references/consistency-locks.md:96` [REQUIRE] — The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal s

##### 0 · personas · 1 → style.photography = `vintage` (vintage / analógico) — 6 reglas

  - `image/SKILL.md:76` [PROCESS] — Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise 
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `visual-prompt-forge/references/failure-modes.md:17` [RECOMMEND] — - Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")

##### 0 · personas · 1 → style.photography = `calle` (fotografía de calle) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → style.photography = `movil` (móvil / snapshot) — 3 reglas

  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `storyboard-html-preview/SKILL.md:238` [RECOMMEND] — Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
  - `storyboard-html-preview/SKILL.md:255` [GATE] — - [ ] Mobile viewport (375px) renders without horizontal scroll

##### 0 · personas · 1 → style.photography = `bellas_artes` (bellas artes / conceptual) — 1 reglas

  - `image/references/patterns/portrait-cinema.md:83` [RECOMMEND] — Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elem

##### 0 · personas · 1 → style.photography = `estudio` (retrato de estudio) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → lighting.setup = `estudio` (estudio (softbox, strobe, controlada)) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → lighting.setup = `natural_exterior` (natural exterior) — 1 reglas

  - `visual-prompt-forge/adapters/flux.md:56` [RECOMMEND] — - `Sony FX6, 35mm prime, natural light only`

##### 0 · personas · 1 → lighting.setup = `ventana` (luz entrando por ventana) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → lighting.setup = `golden_hour` (golden hour / atardecer) — 1 reglas

  - `image/references/prompt-framework.md:214` [RECOMMEND] — 3. **Atmospheric particles** — "dust motes suspended in light beam, steam wisps rising from coffee cup, pollen floating in golden hour air, fine rain 

##### 0 · personas · 1 → lighting.setup = `artificial_nocturna` (artificial nocturna) — 3 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/prompt-framework.md:218` [RECOMMEND] — 7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby si

##### 0 · personas · 1 → lighting.setup = `mixta` (mixta) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → composition.shot_size = `macro` (macro / detalle) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → composition.shot_size = `close_up` (close-up) — 3 reglas

  - `image/references/multi-panel.md:94` [RECOMMEND] — **When to use:** Hero shot + close-up + action for a campaign visual — horizontal or vertical triptych.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `storyboard-architect/references/shot-grammar.md:11` [RECOMMEND] — | `MCU` | Medium close-up | Head and shoulders |

##### 0 · personas · 1 → composition.shot_size = `plano_medio` (plano medio) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → composition.shot_size = `cuerpo_completo` (cuerpo completo) — 2 reglas

  - `image/references/creative-direction.md:47` [RECOMMEND] — - "Waist-up portrait", "full body", "over-the-shoulder"
  - `image/references/patterns/character-design.md:120` [RECOMMEND] — Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional con

##### 0 · personas · 1 → composition.shot_size = `plano_general` (plano general / amplio) — 2 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

##### 0 · personas · 1 → task.theme = `deportiva` (deportiva) — 6 reglas

  - `aurora-prompt-linter/SKILL.md:157` [RECOMMEND] — - **Sinónimos**: "tank top" en ref + "athletic shirt" en prompt no se detecta como redundante. Roadmap v1.1: tabla de sinónimos.
  - `aurora-prompt-linter/references/README.md:96` [RECOMMEND] — 5. **Sports broadcast**: si flag activo, requiere `60fps` y `broadcast realism` en MAIN (Regla 26 v6.0).
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:93` [RECOMMEND] — Use for forward-looking athletic or techwear editorials where abstract 3D forms create a surreal spatial environment around the model.
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 

##### 0 · personas · 1 → task.theme = `musical` (musical / concierto) — 2 reglas

  - `image/references/patterns/portrait-cinema.md:49` [RECOMMEND] — Use for edgy, tech-forward portraits — artist profiles, electronic music press, tech brand campaigns. High contrast black-and-white with selective red
  - `storyboard-architect/references/on-screen-text.md:10` [RECOMMEND] — 4. **Beat punctuation.** A single word or phrase that lands on a music hit.

##### 0 · personas · 1 → task.theme = `moda` (moda) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → task.theme = `gastronomica` (gastronómica) — 8 reglas

  - `image/SKILL.md:68` [PROCESS] — - Food & beverage advertising → [patterns/food-beverage.md](references/patterns/food-beverage.md)
  - `image/references/patterns/ecommerce.md:80` [RECOMMEND] — Use for food, beverage, or supplement products where suspended ingredients communicate freshness, flavor, or composition.
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:41` [RECOMMEND] — Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
  - `image/references/patterns/food-beverage.md:65` [RECOMMEND] — Use for hero food posters — restaurants, delivery apps, menu boards — where the food is the entire composition with fillable content slots.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"

##### 0 · personas · 1 → task.theme = `corporativa` (corporativa) — 3 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:52` [RECOMMEND] — Reject generic fillers ("professional, modern, clean"), they describe everything and constrain nothing. Push to contrast clauses that do work: "operat
  - `visual-prompt-forge/SKILL.md:269` [REQUIRE] — Verbatim means the whole string, unedited. Not "the same idea in better prose". The failure mode is specific and easy to walk into: you are writing fl
  - `visual-prompt-forge/SKILL.md:276` [REQUIRE] — Capitalising the first letter to start a sentence is fine, because the check is case-insensitive. "Minimalist home office, white walls, oak desk, sing

##### 0 · personas · 1 → task.theme = `medica` (médica / científica) — 3 reglas

  - `brand-lock-extractor/SKILL.md:114` [REQUIRE] — The output is a clinical specification. It models the standards the brand-lock enforces. No emojis anywhere. No marketing adjectives about the brand i
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `learned/production-learnings.v3.2.json:11` [REQUIRE] — Once an image is accepted and requested changes are local, perform a surgical image edit and preserve the approved pixels/locks outside the requested 

##### 0 · personas · 1 → task.theme = `viaje` (viaje / turismo) — 3 reglas

  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `visual-prompt-forge/SKILL.md:303` [REQUIRE] — - **The direction of travel.** Left to right, right to left, toward camera. Without it the generator picks, and consecutive shots stop matching.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 0 · personas · 1 → task.theme = `automotriz` (automotriz) — 1 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo

##### 0 · personas · 1 → task.theme = `otra` (otra) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → motion.action_complexity = `estatica` (estática) — 11 reglas

  - `brand-lock-extractor/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `storyboard-architect/SKILL.md:263` [GATE] — What the validator cannot check, and you still have to:
  - `storyboard-architect/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `visual-asset-critic/SKILL.md:170` [GATE] — The hashes are the point. Without `image_sha256`, a frame regenerated after this review still satisfies `image_ref`, and a stale ACCEPT sails through 
  - `visual-asset-critic/SKILL.md:215` [GATE] — Worked examples: `examples/critique.accept.json` and `examples/critique.revise.json` show the shape at version `1.0`, which is still valid and carries
  - `visual-prompt-forge/SKILL.md:299` [REQUIRE] — A prompt can be beautifully written and still be impossible to shoot. Every prompt declares, before anything else:
  - `visual-prompt-forge/SKILL.md:360` [GATE] — What it cannot check, and you still have to:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/references/prompt-anatomy.md:66` [RECOMMEND] — 3. **Animation.** Animated text needs After Effects / Remotion / CapCut. Static rendered text is dead-on-arrival for motion content.

##### 0 · personas · 1 → motion.action_complexity = `pose_dirigida` (pose dirigida) — 6 reglas

  - `image/references/gpt-image.md:94` [RECOMMEND] — **Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows s
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `learned/production-learnings.v3.2.json:3` [REQUIRE] — Preserve a sufficiently specific domain-native pose/technique label instead of expanding it into speculative anatomy. Expand only when the target adap
  - `learned/production-learnings.v3.2.json:4` [REQUIRE] — A reference may control only its declared role. Features explicitly excluded from that role must not be copied into subject identity, pose, camera, fr
  - `learned/production-learnings.v3.2.json:8` [RECOMMEND] — For complex underwater human anatomy, physically justified bubbles/turbulence may obscure non-critical anatomical detail when the brief does not requi
  - `produccion-visual-sw30/SKILL.md:125` [GATE] — 6. Swap de identidad = última operación, sola: "Replace X with Y — same position, same pose, same scale".

##### 0 · personas · 1 → motion.action_complexity = `accion_simple` (acción simple (un cuerpo)) — 5 reglas

  - `image/references/multi-panel.md:210` [REQUIRE] — - Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"
  - `learned/production-learnings.v3.2.json:10` [REQUIRE] — Do not declare a generated asset or model successful for a case before running the applicable QA. Separate deterministic/mechanical checks from semant
  - `visual-prompt-forge/SKILL.md:302` [REQUIRE] — - **The point of view.** Profile, frontal, side, rear. "A man walking" is not a shot.

##### 0 · personas · 1 → motion.action_complexity = `accion_compleja` (acción compleja (varios cuerpos, contacto, física)) — 4 reglas

  - `image/references/prompt-framework.md:217` [RECOMMEND] — 6. **Contact shadows** — "soft contact shadow where cup meets saucer, ambient occlusion in crevices of stone wall, dark line where book spine meets ta
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:305` [REQUIRE] — - **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 0 · personas · 1 → text.mode = `none` (sin texto) — **0 reglas · RAMA VACÍA**

##### 0 · personas · 1 → text.mode = `in_image` (texto dentro de la imagen) — 16 reglas

  - `brand-lock-extractor/SKILL.md:54` [PROCESS] — 3. **Typography** (display, body, optional mono, with weights)
  - `brand-lock-extractor/SKILL.md:82` [FORBID] — - All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion languag
  - `brand-lock-extractor/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `image/SKILL.md:56` [PROCESS] — - Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
  - `image/references/models.md:50` [PROCESS] — | Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/text-rendering.md:133` [RECOMMEND] — Describe typography style or name the font directly:
  - `produccion-visual-sw30/SKILL.md:132` [GATE] — 10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los cuerpos nunca tapan logo ni lettering en frames congelados.
  - `storyboard-architect/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `storyboard-architect/references/beat-frameworks.md:45` [RECOMMEND] — Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/on-screen-text.md:71` [REQUIRE] — Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the br
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 0 · personas · 1 → text.mode = `composite` (texto compuesto después) — 7 reglas

  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:105` [FORBID] — - **Don't include text content in image prompts**, composite separately; text rendering is mediocre
  - `visual-prompt-forge/adapters/nano-banana.md:83` [PROCESS] — 4. Composite text on the chosen variant
  - `visual-prompt-forge/adapters/seedream.md:82` [FORBID] — - **Don't include text content**, text rendering is poor; composite separately
  - `visual-prompt-forge/references/failure-modes.md:53` [FORBID] — - The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.

##### 0 · personas · 1 → generator.family = `nano_banana` (Nano Banana / Pro) — 38 reglas

  - `image/SKILL.md:100` [REQUIRE] — For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:40` [FORBID] — - **Nano Banana** → [nano-banana.md](references/nano-banana.md) Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mo
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:78` [REQUIRE] — - **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
  - `image/references/models.md:10` [PROCESS] — | Сложная сцена с физикой/композицией | **Nano Banana Pro** |
  - `image/references/models.md:11` [PROCESS] — | Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
  - `image/references/models.md:12` [PROCESS] — | Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
  - `image/references/models.md:17` [PROCESS] — | Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:9` [PROCESS] — | Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/nano-banana.md:55` [RECOMMEND] — Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены пл
  - `image/references/patterns/ecommerce.md:114` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for believable physical distortion
  - `image/references/patterns/fashion-editorial.md:107` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/food-beverage.md:110` [RECOMMEND] — **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
  - `image/references/patterns/food-beverage.md:124` [RECOMMEND] — **Recommended model:** NB2 — image grounding for real city landmarks + illustration style
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/portrait-cinema.md:97` [RECOMMEND] — **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)
  - `image/references/patterns/poster-illustration.md:117` [RECOMMEND] — **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species
  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
  - `image/references/prompt-framework.md:43` [REQUIRE] — > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
  - `image/references/prompt-framework.md:87` [PROCESS] — **3. Exclusions** - что исключить (опционально): > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:109` [FORBID] — That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the build when an adapter advertises more words than its ceiling
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/nano-banana.md:101` [FORBID] — - **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
  - `visual-prompt-forge/adapters/nano-banana.md:102` [FORBID] — - **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
  - `visual-prompt-forge/adapters/nano-banana.md:104` [REQUIRE] — - **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:81` [PROCESS] — 2. Feed that image to Nano Banana with variation prompts
  - `visual-prompt-forge/references/failure-modes.md:129` [RECOMMEND] — 2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-prod

##### 0 · personas · 1 → generator.family = `gpt_image` (GPT Image 2) — 65 reglas

  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:43` [REQUIRE] — - **GPT Image 2** → [gpt-image.md](references/gpt-image.md) 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop 
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:74` [REQUIRE] — > **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.
  - `image/references/golden-rules.md:93` [REQUIRE] — Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.
  - `image/references/gpt-image.md:117` [RECOMMEND] — GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не распи
  - `image/references/models.md:13` [PROCESS] — | Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
  - `image/references/models.md:14` [PROCESS] — | Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
  - `image/references/models.md:15` [PROCESS] — | Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
  - `image/references/models.md:16` [PROCESS] — | Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
  - `image/references/models.md:18` [PROCESS] — | Storyboard с фокусом на типографике | **GPT Image 2** |
  - `image/references/models.md:19` [PROCESS] — | Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:26` [REQUIRE] — - **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
  - `image/references/multi-panel.md:122` [RECOMMEND] — **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych) **Model:** GPT Image 2 `quality: medium` — if text overlay need
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:294` [REQUIRE] — **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space) **Model:** GPT Image 2 `quality: high` (text-heavy — scene number
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/patterns/character-design.md:108` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
  - `image/references/patterns/character-design.md:140` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering
  - `image/references/patterns/character-design.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
  - `image/references/patterns/character-design.md:3` [RECOMMEND] — Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}`
  - `image/references/patterns/character-design.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
  - `image/references/patterns/character-design.md:80` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
  - `image/references/patterns/ecommerce.md:74` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
  - `image/references/patterns/ecommerce.md:94` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
  - `image/references/patterns/fashion-editorial.md:27` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
  - `image/references/patterns/fashion-editorial.md:73` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:35` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
  - `image/references/patterns/food-beverage.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
  - `image/references/patterns/food-beverage.md:96` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
  - `image/references/patterns/portrait-cinema.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `image/references/patterns/portrait-cinema.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
  - `image/references/patterns/portrait-cinema.md:63` [RECOMMEND] — **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:3` [RECOMMEND] — Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. De
  - `image/references/patterns/poster-illustration.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
  - `image/references/patterns/poster-illustration.md:82` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
  - `image/references/patterns/ui-social.md:104` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements requir
  - `image/references/patterns/ui-social.md:135` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout
  - `image/references/patterns/ui-social.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
  - `image/references/patterns/ui-social.md:3` [RECOMMEND] — Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for c
  - `image/references/patterns/ui-social.md:49` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
  - `image/references/patterns/ui-social.md:75` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/gpt-image.md:38` [RECOMMEND] — GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:86` [FORBID] — - **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
  - `visual-prompt-forge/adapters/gpt-image.md:89` [FORBID] — - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:87` [RECOMMEND] — - For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 0 · personas · 1 → generator.family = `midjourney` (Midjourney) — 13 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:18` [PROCESS] — - Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
  - `visual-prompt-forge/SKILL.md:295` [REQUIRE] — If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. T
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
  - `visual-prompt-forge/references/consistency-locks.md:64` [RECOMMEND] — For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
  - `visual-prompt-forge/references/failure-modes.md:39` [RECOMMEND] — - For Midjourney, use `--cref` with `--cw 50`

##### 0 · personas · 1 → generator.family = `flux` (Flux) — 17 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-asset-critic/SKILL.md:102` [REQUIRE] — **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts: > "Hands are mangled. This is a known Fl
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/flux.md:66` [REQUIRE] — The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.
  - `visual-prompt-forge/adapters/flux.md:86` [RECOMMEND] — Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.
  - `visual-prompt-forge/adapters/flux.md:90` [FORBID] — - **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
  - `visual-prompt-forge/adapters/flux.md:91` [FORBID] — - **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:69` [RECOMMEND] — **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

##### 0 · personas · 1 → generator.family = `ideogram` (Ideogram) — 14 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:257` [REQUIRE] — If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:30` [REQUIRE] — The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/ideogram.md:92` [FORBID] — - **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
  - `visual-prompt-forge/adapters/ideogram.md:93` [FORBID] — - **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
  - `visual-prompt-forge/references/failure-modes.md:54` [REQUIRE] — - If text must be in-image (poster work), use Ideogram v3 with explicit override flag
  - `visual-prompt-forge/references/failure-modes.md:56` [RECOMMEND] — - Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
  - `visual-prompt-forge/references/prompt-anatomy.md:58` [FORBID] — **What:** on-screen text composited after generation. **Source:** `text-overlays.json`. **Never appears in image prompts** (except Ideogram Mode 2 wit
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 0 · personas · 1 → generator.family = `seedream` (Seedream) — 3 reglas

  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/seedream.md:80` [FORBID] — - **Don't write paragraphs**. Seedream wants comma-separated phrases
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output

#### GRUPO DE PERSONAS — 0 reglas propias


##### 0 · personas · grupo → style.photography = `editorial` (editorial) — 16 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/multi-panel.md:57` [RECOMMEND] — **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:33` [RECOMMEND] — Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:9` [RECOMMEND] — Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 
  - `visual-asset-critic/SKILL.md:20` [PROCESS] — - Has a generated image and just wants editorial feedback (no storyboard reference)
  - `visual-asset-critic/SKILL.md:8` [FORBID] — You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structu
  - `visual-prompt-forge/adapters/nano-banana.md:82` [PROCESS] — 3. Get 4–8 variants of the same shot for editorial selection
  - `visual-prompt-forge/references/consistency-locks.md:109` [FORBID] — Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.
  - `visual-prompt-forge/references/failure-modes.md:130` [RECOMMEND] — 3. The image is 80% right and the gap is editorial → ship to post and let the editor finish
  - `visual-prompt-forge/references/failure-modes.md:3` [FORBID] — What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

##### 0 · personas · grupo → style.photography = `documental` (documental / fotoperiodismo) — 1 reglas

  - `produccion-visual-sw30/SKILL.md:73` [GATE] — | usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO

##### 0 · personas · grupo → style.photography = `natgeo` (documental de naturaleza (National Geographic)) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → style.photography = `moda` (moda) — 8 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/creative-direction.md:34` [REQUIRE] — - Hasselblad — medium format, shallow DOF, fashion/portrait
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/character-design.md:58` [RECOMMEND] — Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o

##### 0 · personas · grupo → style.photography = `producto` (producto / e-commerce) — 1 reglas

  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)

##### 0 · personas · grupo → style.photography = `cinematografico` (cinematográfico) — 9 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:67` [RECOMMEND] — The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site 
  - `image/SKILL.md:64` [PROCESS] — - **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 
  - `image/SKILL.md:69` [PROCESS] — - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - `image/SKILL.md:80` [PROCESS] — Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / stand
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/nano-banana.md:25` [RECOMMEND] — - Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `visual-asset-critic/references/critique-rubric.md:107` [FORBID] — - **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
  - `visual-prompt-forge/references/consistency-locks.md:96` [REQUIRE] — The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal s

##### 0 · personas · grupo → style.photography = `vintage` (vintage / analógico) — 6 reglas

  - `image/SKILL.md:76` [PROCESS] — Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise 
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `visual-prompt-forge/references/failure-modes.md:17` [RECOMMEND] — - Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")

##### 0 · personas · grupo → style.photography = `calle` (fotografía de calle) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → style.photography = `movil` (móvil / snapshot) — 3 reglas

  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `storyboard-html-preview/SKILL.md:238` [RECOMMEND] — Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
  - `storyboard-html-preview/SKILL.md:255` [GATE] — - [ ] Mobile viewport (375px) renders without horizontal scroll

##### 0 · personas · grupo → style.photography = `bellas_artes` (bellas artes / conceptual) — 1 reglas

  - `image/references/patterns/portrait-cinema.md:83` [RECOMMEND] — Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elem

##### 0 · personas · grupo → style.photography = `estudio` (retrato de estudio) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → lighting.setup = `estudio` (estudio (softbox, strobe, controlada)) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → lighting.setup = `natural_exterior` (natural exterior) — 1 reglas

  - `visual-prompt-forge/adapters/flux.md:56` [RECOMMEND] — - `Sony FX6, 35mm prime, natural light only`

##### 0 · personas · grupo → lighting.setup = `ventana` (luz entrando por ventana) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → lighting.setup = `golden_hour` (golden hour / atardecer) — 1 reglas

  - `image/references/prompt-framework.md:214` [RECOMMEND] — 3. **Atmospheric particles** — "dust motes suspended in light beam, steam wisps rising from coffee cup, pollen floating in golden hour air, fine rain 

##### 0 · personas · grupo → lighting.setup = `artificial_nocturna` (artificial nocturna) — 3 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/prompt-framework.md:218` [RECOMMEND] — 7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby si

##### 0 · personas · grupo → lighting.setup = `mixta` (mixta) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → composition.shot_size = `macro` (macro / detalle) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → composition.shot_size = `close_up` (close-up) — 3 reglas

  - `image/references/multi-panel.md:94` [RECOMMEND] — **When to use:** Hero shot + close-up + action for a campaign visual — horizontal or vertical triptych.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `storyboard-architect/references/shot-grammar.md:11` [RECOMMEND] — | `MCU` | Medium close-up | Head and shoulders |

##### 0 · personas · grupo → composition.shot_size = `plano_medio` (plano medio) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → composition.shot_size = `cuerpo_completo` (cuerpo completo) — 2 reglas

  - `image/references/creative-direction.md:47` [RECOMMEND] — - "Waist-up portrait", "full body", "over-the-shoulder"
  - `image/references/patterns/character-design.md:120` [RECOMMEND] — Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional con

##### 0 · personas · grupo → composition.shot_size = `plano_general` (plano general / amplio) — 2 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

##### 0 · personas · grupo → task.theme = `deportiva` (deportiva) — 6 reglas

  - `aurora-prompt-linter/SKILL.md:157` [RECOMMEND] — - **Sinónimos**: "tank top" en ref + "athletic shirt" en prompt no se detecta como redundante. Roadmap v1.1: tabla de sinónimos.
  - `aurora-prompt-linter/references/README.md:96` [RECOMMEND] — 5. **Sports broadcast**: si flag activo, requiere `60fps` y `broadcast realism` en MAIN (Regla 26 v6.0).
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:93` [RECOMMEND] — Use for forward-looking athletic or techwear editorials where abstract 3D forms create a surreal spatial environment around the model.
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 

##### 0 · personas · grupo → task.theme = `musical` (musical / concierto) — 2 reglas

  - `image/references/patterns/portrait-cinema.md:49` [RECOMMEND] — Use for edgy, tech-forward portraits — artist profiles, electronic music press, tech brand campaigns. High contrast black-and-white with selective red
  - `storyboard-architect/references/on-screen-text.md:10` [RECOMMEND] — 4. **Beat punctuation.** A single word or phrase that lands on a music hit.

##### 0 · personas · grupo → task.theme = `moda` (moda) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → task.theme = `gastronomica` (gastronómica) — 8 reglas

  - `image/SKILL.md:68` [PROCESS] — - Food & beverage advertising → [patterns/food-beverage.md](references/patterns/food-beverage.md)
  - `image/references/patterns/ecommerce.md:80` [RECOMMEND] — Use for food, beverage, or supplement products where suspended ingredients communicate freshness, flavor, or composition.
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:41` [RECOMMEND] — Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
  - `image/references/patterns/food-beverage.md:65` [RECOMMEND] — Use for hero food posters — restaurants, delivery apps, menu boards — where the food is the entire composition with fillable content slots.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"

##### 0 · personas · grupo → task.theme = `corporativa` (corporativa) — 3 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:52` [RECOMMEND] — Reject generic fillers ("professional, modern, clean"), they describe everything and constrain nothing. Push to contrast clauses that do work: "operat
  - `visual-prompt-forge/SKILL.md:269` [REQUIRE] — Verbatim means the whole string, unedited. Not "the same idea in better prose". The failure mode is specific and easy to walk into: you are writing fl
  - `visual-prompt-forge/SKILL.md:276` [REQUIRE] — Capitalising the first letter to start a sentence is fine, because the check is case-insensitive. "Minimalist home office, white walls, oak desk, sing

##### 0 · personas · grupo → task.theme = `medica` (médica / científica) — 3 reglas

  - `brand-lock-extractor/SKILL.md:114` [REQUIRE] — The output is a clinical specification. It models the standards the brand-lock enforces. No emojis anywhere. No marketing adjectives about the brand i
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `learned/production-learnings.v3.2.json:11` [REQUIRE] — Once an image is accepted and requested changes are local, perform a surgical image edit and preserve the approved pixels/locks outside the requested 

##### 0 · personas · grupo → task.theme = `viaje` (viaje / turismo) — 3 reglas

  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `visual-prompt-forge/SKILL.md:303` [REQUIRE] — - **The direction of travel.** Left to right, right to left, toward camera. Without it the generator picks, and consecutive shots stop matching.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 0 · personas · grupo → task.theme = `automotriz` (automotriz) — 1 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo

##### 0 · personas · grupo → task.theme = `otra` (otra) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → motion.action_complexity = `estatica` (estática) — 11 reglas

  - `brand-lock-extractor/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `storyboard-architect/SKILL.md:263` [GATE] — What the validator cannot check, and you still have to:
  - `storyboard-architect/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `visual-asset-critic/SKILL.md:170` [GATE] — The hashes are the point. Without `image_sha256`, a frame regenerated after this review still satisfies `image_ref`, and a stale ACCEPT sails through 
  - `visual-asset-critic/SKILL.md:215` [GATE] — Worked examples: `examples/critique.accept.json` and `examples/critique.revise.json` show the shape at version `1.0`, which is still valid and carries
  - `visual-prompt-forge/SKILL.md:299` [REQUIRE] — A prompt can be beautifully written and still be impossible to shoot. Every prompt declares, before anything else:
  - `visual-prompt-forge/SKILL.md:360` [GATE] — What it cannot check, and you still have to:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/references/prompt-anatomy.md:66` [RECOMMEND] — 3. **Animation.** Animated text needs After Effects / Remotion / CapCut. Static rendered text is dead-on-arrival for motion content.

##### 0 · personas · grupo → motion.action_complexity = `pose_dirigida` (pose dirigida) — 6 reglas

  - `image/references/gpt-image.md:94` [RECOMMEND] — **Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows s
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `learned/production-learnings.v3.2.json:3` [REQUIRE] — Preserve a sufficiently specific domain-native pose/technique label instead of expanding it into speculative anatomy. Expand only when the target adap
  - `learned/production-learnings.v3.2.json:4` [REQUIRE] — A reference may control only its declared role. Features explicitly excluded from that role must not be copied into subject identity, pose, camera, fr
  - `learned/production-learnings.v3.2.json:8` [RECOMMEND] — For complex underwater human anatomy, physically justified bubbles/turbulence may obscure non-critical anatomical detail when the brief does not requi
  - `produccion-visual-sw30/SKILL.md:125` [GATE] — 6. Swap de identidad = última operación, sola: "Replace X with Y — same position, same pose, same scale".

##### 0 · personas · grupo → motion.action_complexity = `accion_simple` (acción simple (un cuerpo)) — 5 reglas

  - `image/references/multi-panel.md:210` [REQUIRE] — - Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"
  - `learned/production-learnings.v3.2.json:10` [REQUIRE] — Do not declare a generated asset or model successful for a case before running the applicable QA. Separate deterministic/mechanical checks from semant
  - `visual-prompt-forge/SKILL.md:302` [REQUIRE] — - **The point of view.** Profile, frontal, side, rear. "A man walking" is not a shot.

##### 0 · personas · grupo → motion.action_complexity = `accion_compleja` (acción compleja (varios cuerpos, contacto, física)) — 4 reglas

  - `image/references/prompt-framework.md:217` [RECOMMEND] — 6. **Contact shadows** — "soft contact shadow where cup meets saucer, ambient occlusion in crevices of stone wall, dark line where book spine meets ta
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:305` [REQUIRE] — - **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 0 · personas · grupo → text.mode = `none` (sin texto) — **0 reglas · RAMA VACÍA**

##### 0 · personas · grupo → text.mode = `in_image` (texto dentro de la imagen) — 16 reglas

  - `brand-lock-extractor/SKILL.md:54` [PROCESS] — 3. **Typography** (display, body, optional mono, with weights)
  - `brand-lock-extractor/SKILL.md:82` [FORBID] — - All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion languag
  - `brand-lock-extractor/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `image/SKILL.md:56` [PROCESS] — - Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
  - `image/references/models.md:50` [PROCESS] — | Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/text-rendering.md:133` [RECOMMEND] — Describe typography style or name the font directly:
  - `produccion-visual-sw30/SKILL.md:132` [GATE] — 10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los cuerpos nunca tapan logo ni lettering en frames congelados.
  - `storyboard-architect/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `storyboard-architect/references/beat-frameworks.md:45` [RECOMMEND] — Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/on-screen-text.md:71` [REQUIRE] — Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the br
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 0 · personas · grupo → text.mode = `composite` (texto compuesto después) — 7 reglas

  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:105` [FORBID] — - **Don't include text content in image prompts**, composite separately; text rendering is mediocre
  - `visual-prompt-forge/adapters/nano-banana.md:83` [PROCESS] — 4. Composite text on the chosen variant
  - `visual-prompt-forge/adapters/seedream.md:82` [FORBID] — - **Don't include text content**, text rendering is poor; composite separately
  - `visual-prompt-forge/references/failure-modes.md:53` [FORBID] — - The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.

##### 0 · personas · grupo → generator.family = `nano_banana` (Nano Banana / Pro) — 38 reglas

  - `image/SKILL.md:100` [REQUIRE] — For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:40` [FORBID] — - **Nano Banana** → [nano-banana.md](references/nano-banana.md) Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mo
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:78` [REQUIRE] — - **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
  - `image/references/models.md:10` [PROCESS] — | Сложная сцена с физикой/композицией | **Nano Banana Pro** |
  - `image/references/models.md:11` [PROCESS] — | Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
  - `image/references/models.md:12` [PROCESS] — | Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
  - `image/references/models.md:17` [PROCESS] — | Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:9` [PROCESS] — | Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/nano-banana.md:55` [RECOMMEND] — Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены пл
  - `image/references/patterns/ecommerce.md:114` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for believable physical distortion
  - `image/references/patterns/fashion-editorial.md:107` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/food-beverage.md:110` [RECOMMEND] — **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
  - `image/references/patterns/food-beverage.md:124` [RECOMMEND] — **Recommended model:** NB2 — image grounding for real city landmarks + illustration style
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/portrait-cinema.md:97` [RECOMMEND] — **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)
  - `image/references/patterns/poster-illustration.md:117` [RECOMMEND] — **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species
  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
  - `image/references/prompt-framework.md:43` [REQUIRE] — > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
  - `image/references/prompt-framework.md:87` [PROCESS] — **3. Exclusions** - что исключить (опционально): > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:109` [FORBID] — That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the build when an adapter advertises more words than its ceiling
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/nano-banana.md:101` [FORBID] — - **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
  - `visual-prompt-forge/adapters/nano-banana.md:102` [FORBID] — - **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
  - `visual-prompt-forge/adapters/nano-banana.md:104` [REQUIRE] — - **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:81` [PROCESS] — 2. Feed that image to Nano Banana with variation prompts
  - `visual-prompt-forge/references/failure-modes.md:129` [RECOMMEND] — 2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-prod

##### 0 · personas · grupo → generator.family = `gpt_image` (GPT Image 2) — 65 reglas

  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:43` [REQUIRE] — - **GPT Image 2** → [gpt-image.md](references/gpt-image.md) 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop 
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:74` [REQUIRE] — > **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.
  - `image/references/golden-rules.md:93` [REQUIRE] — Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.
  - `image/references/gpt-image.md:117` [RECOMMEND] — GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не распи
  - `image/references/models.md:13` [PROCESS] — | Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
  - `image/references/models.md:14` [PROCESS] — | Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
  - `image/references/models.md:15` [PROCESS] — | Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
  - `image/references/models.md:16` [PROCESS] — | Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
  - `image/references/models.md:18` [PROCESS] — | Storyboard с фокусом на типографике | **GPT Image 2** |
  - `image/references/models.md:19` [PROCESS] — | Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:26` [REQUIRE] — - **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
  - `image/references/multi-panel.md:122` [RECOMMEND] — **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych) **Model:** GPT Image 2 `quality: medium` — if text overlay need
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:294` [REQUIRE] — **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space) **Model:** GPT Image 2 `quality: high` (text-heavy — scene number
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/patterns/character-design.md:108` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
  - `image/references/patterns/character-design.md:140` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering
  - `image/references/patterns/character-design.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
  - `image/references/patterns/character-design.md:3` [RECOMMEND] — Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}`
  - `image/references/patterns/character-design.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
  - `image/references/patterns/character-design.md:80` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
  - `image/references/patterns/ecommerce.md:74` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
  - `image/references/patterns/ecommerce.md:94` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
  - `image/references/patterns/fashion-editorial.md:27` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
  - `image/references/patterns/fashion-editorial.md:73` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:35` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
  - `image/references/patterns/food-beverage.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
  - `image/references/patterns/food-beverage.md:96` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
  - `image/references/patterns/portrait-cinema.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `image/references/patterns/portrait-cinema.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
  - `image/references/patterns/portrait-cinema.md:63` [RECOMMEND] — **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:3` [RECOMMEND] — Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. De
  - `image/references/patterns/poster-illustration.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
  - `image/references/patterns/poster-illustration.md:82` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
  - `image/references/patterns/ui-social.md:104` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements requir
  - `image/references/patterns/ui-social.md:135` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout
  - `image/references/patterns/ui-social.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
  - `image/references/patterns/ui-social.md:3` [RECOMMEND] — Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for c
  - `image/references/patterns/ui-social.md:49` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
  - `image/references/patterns/ui-social.md:75` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/gpt-image.md:38` [RECOMMEND] — GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:86` [FORBID] — - **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
  - `visual-prompt-forge/adapters/gpt-image.md:89` [FORBID] — - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:87` [RECOMMEND] — - For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 0 · personas · grupo → generator.family = `midjourney` (Midjourney) — 13 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:18` [PROCESS] — - Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
  - `visual-prompt-forge/SKILL.md:295` [REQUIRE] — If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. T
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
  - `visual-prompt-forge/references/consistency-locks.md:64` [RECOMMEND] — For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
  - `visual-prompt-forge/references/failure-modes.md:39` [RECOMMEND] — - For Midjourney, use `--cref` with `--cw 50`

##### 0 · personas · grupo → generator.family = `flux` (Flux) — 17 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-asset-critic/SKILL.md:102` [REQUIRE] — **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts: > "Hands are mangled. This is a known Fl
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/flux.md:66` [REQUIRE] — The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.
  - `visual-prompt-forge/adapters/flux.md:86` [RECOMMEND] — Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.
  - `visual-prompt-forge/adapters/flux.md:90` [FORBID] — - **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
  - `visual-prompt-forge/adapters/flux.md:91` [FORBID] — - **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:69` [RECOMMEND] — **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

##### 0 · personas · grupo → generator.family = `ideogram` (Ideogram) — 14 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:257` [REQUIRE] — If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:30` [REQUIRE] — The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/ideogram.md:92` [FORBID] — - **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
  - `visual-prompt-forge/adapters/ideogram.md:93` [FORBID] — - **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
  - `visual-prompt-forge/references/failure-modes.md:54` [REQUIRE] — - If text must be in-image (poster work), use Ideogram v3 with explicit override flag
  - `visual-prompt-forge/references/failure-modes.md:56` [RECOMMEND] — - Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
  - `visual-prompt-forge/references/prompt-anatomy.md:58` [FORBID] — **What:** on-screen text composited after generation. **Source:** `text-overlays.json`. **Never appears in image prompts** (except Ideogram Mode 2 wit
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 0 · personas · grupo → generator.family = `seedream` (Seedream) — 3 reglas

  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/seedream.md:80` [FORBID] — - **Don't write paragraphs**. Seedream wants comma-separated phrases
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output

### SIN PERSONAS — 5 reglas propias

  - `brand-lock-extractor/references/extraction-rubric.md:59` [FORBID] — - Imagery: no stock-photo gloss? no people? no gradients? no clip-art icons? Each absence is a never.
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:57` [PROCESS] — - Edit existing image (object removal, lighting swap, colorization, restoration, localization) → [editing.md](references/editing.md)
  - `image/references/gpt-image.md:96` [FORBID] — **Object removal:** «Remove [X]. Do not change anything else. Use `input_fidelity: high` to maintain surrounding context» (только gpt-image-1.5/1, в g
  - `image/references/gpt-image.md:98` [RECOMMEND] — **Lighting/weather swap:** «Change ONLY environmental conditions: lighting direction/quality, shadows, atmosphere, precipitation. Preserve identity, g

#### 0 · sin personas → scene.category = `exterior` (exterior) — 3 reglas

  - `brand-lock-extractor/brand-packs/_template.md:15` [RECOMMEND] — Every hex value here is allowed. Anything outside this list is not.
  - `learned/production-learnings.v3.2.json:11` [REQUIRE] — Once an image is accepted and requested changes are local, perform a surgical image edit and preserve the approved pixels/locks outside the requested 
  - `learned/production-learnings.v3.4.json:4` [REQUIRE] — Prompt revisions may not be freely rewritten. Re-render the same immutable Prompt AST against the updated frozen brief; any AST/model/parameter/templa

#### 0 · sin personas → scene.category = `interior` (interior) — 13 reglas

  - `image/references/patterns/ui-social.md:55` [RECOMMEND] — Use to create a polished App Store or Google Play listing screenshot — device frame with app UI inside, feature headline, and clean gradient backgroun
  - `image/references/prompt-framework.md:215` [RECOMMEND] — 4. **Specular behavior** — "specular highlights on metal edges of watch, caustic reflections dancing inside glass bottle, wet surface sheen on cobbles
  - `storyboard-architect/SKILL.md:255` [GATE] — - every overlay's timing sits inside its shot window, and exit is after enter
  - `storyboard-architect/SKILL.md:259` [GATE] — It warns, rather than fails, on judgement calls worth a second look: overlay copy repeated inside a shot subject, a raw hex in a subject, shot ids out
  - `visual-asset-critic/SKILL.md:232` [FORBID] — If the brief was "founder at laptop, calm mood" and the generation delivered exactly that, don't note that "the room could be more visually interestin
  - `visual-prompt-forge/SKILL.md:104` [REQUIRE] — `max_prompt_words` is a ceiling. The range in an adapter `.md` is the recommended target and always sits inside that ceiling, so a `.md` saying "40 to
  - `visual-prompt-forge/adapters/flux.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/gpt-image.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/ideogram.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/nano-banana.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/seedream.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `

#### 0 · sin personas → scene.category = `animales` (animales / fauna) — 1 reglas

  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 

#### 0 · sin personas → scene.category = `arquitectonica` (arquitectónica / inmobiliaria) — 1 reglas

  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency

#### 0 · sin personas → scene.category = `paisaje_natural` (paisaje natural) — 4 reglas

  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa

#### 0 · sin personas → scene.category = `producto_objeto` (producto u objeto) — 21 reglas

  - `image/SKILL.md:57` [PROCESS] — - Edit existing image (object removal, lighting swap, colorization, restoration, localization) → [editing.md](references/editing.md)
  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)
  - `image/references/gpt-image.md:96` [FORBID] — **Object removal:** «Remove [X]. Do not change anything else. Use `input_fidelity: high` to maintain surrounding context» (только gpt-image-1.5/1, в g
  - `image/references/gpt-image.md:98` [RECOMMEND] — **Lighting/weather swap:** «Change ONLY environmental conditions: lighting direction/quality, shadows, atmosphere, precipitation. Preserve identity, g
  - `image/references/models.md:39` [PROCESS] — - Product shots на нейтральном фоне.
  - `image/references/multi-panel.md:216` [RECOMMEND] — **When to use:** Product transformation, makeover, time comparison, renovation — two states side by side.
  - `image/references/patterns/ecommerce.md:100` [RECOMMEND] — Use for disruptive, scroll-stopping social ads where the product packaging appears squeezed, inflated, or physically distorted as if made of soft rubb
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:29` [RECOMMEND] — Use for premium beauty or fragrance product photography — dark, moody, tactile surfaces with atmospheric effects.
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:51` [RECOMMEND] — Use to present a product commercial shot breakdown in a single image — pitch decks, creative presentations, client approvals.
  - `image/references/patterns/ecommerce.md:9` [RECOMMEND] — Use when you need a playful, attention-grabbing product visual where tiny workers interact with an oversized product — ideal for social media ads and 
  - `image/references/patterns/food-beverage.md:41` [RECOMMEND] — Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `image/references/patterns/ui-social.md:29` [RECOMMEND] — Use for square-format posts on Instagram or Facebook — quote cards, feature announcements, or product highlights with centered layout.
  - `image/references/patterns/ui-social.md:9` [RECOMMEND] — Use for vertical product or brand ads targeting Instagram Stories — hero product, bold headline, and swipe-up CTA zone at the bottom.
  - `storyboard-architect/references/beat-frameworks.md:20` [RECOMMEND] — Default for product films and brand films. Three beats:
  - `storyboard-architect/references/beat-frameworks.md:23` [RECOMMEND] — 2. **Hero**, the product/founder/methodology arrives. Show what it does, not what it is.
  - `storyboard-architect/references/beat-frameworks.md:29` [RECOMMEND] — Use when: product launches, brand films, anchor pieces.
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/shot-grammar.md:17` [RECOMMEND] — Default to MCU and MS for talking-head founder content. ECU and CU for product detail and emotion. WS and EWS for context-setting.

#### 0 · sin personas → scene.category = `urbana` (urbana / cityscape) — 2 reglas

  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 

#### 0 · sin personas → style.photography = `editorial` (editorial) — 11 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 
  - `visual-asset-critic/SKILL.md:20` [PROCESS] — - Has a generated image and just wants editorial feedback (no storyboard reference)
  - `visual-asset-critic/SKILL.md:8` [FORBID] — You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structu
  - `visual-prompt-forge/adapters/nano-banana.md:82` [PROCESS] — 3. Get 4–8 variants of the same shot for editorial selection
  - `visual-prompt-forge/references/consistency-locks.md:109` [FORBID] — Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.
  - `visual-prompt-forge/references/failure-modes.md:130` [RECOMMEND] — 3. The image is 80% right and the gap is editorial → ship to post and let the editor finish
  - `visual-prompt-forge/references/failure-modes.md:3` [FORBID] — What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

#### 0 · sin personas → style.photography = `documental` (documental / fotoperiodismo) — 1 reglas

  - `produccion-visual-sw30/SKILL.md:73` [GATE] — | usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO

#### 0 · sin personas → style.photography = `natgeo` (documental de naturaleza (National Geographic)) — **0 reglas · RAMA VACÍA**

#### 0 · sin personas → style.photography = `moda` (moda) — 5 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

#### 0 · sin personas → style.photography = `producto` (producto / e-commerce) — 1 reglas

  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)

#### 0 · sin personas → style.photography = `cinematografico` (cinematográfico) — 8 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:67` [RECOMMEND] — The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site 
  - `image/SKILL.md:69` [PROCESS] — - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - `image/SKILL.md:80` [PROCESS] — Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / stand
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/nano-banana.md:25` [RECOMMEND] — - Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `visual-asset-critic/references/critique-rubric.md:107` [FORBID] — - **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
  - `visual-prompt-forge/references/consistency-locks.md:96` [REQUIRE] — The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal s

#### 0 · sin personas → style.photography = `vintage` (vintage / analógico) — 5 reglas

  - `image/SKILL.md:76` [PROCESS] — Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise 
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `visual-prompt-forge/references/failure-modes.md:17` [RECOMMEND] — - Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")

#### 0 · sin personas → style.photography = `calle` (fotografía de calle) — **0 reglas · RAMA VACÍA**

#### 0 · sin personas → style.photography = `movil` (móvil / snapshot) — 3 reglas

  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `storyboard-html-preview/SKILL.md:238` [RECOMMEND] — Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
  - `storyboard-html-preview/SKILL.md:255` [GATE] — - [ ] Mobile viewport (375px) renders without horizontal scroll

#### 0 · sin personas → style.photography = `bellas_artes` (bellas artes / conceptual) — **0 reglas · RAMA VACÍA**

#### 0 · sin personas → style.photography = `estudio` (retrato de estudio) — **0 reglas · RAMA VACÍA**

#### 0 · sin personas → text.mode = `none` (sin texto) — **0 reglas · RAMA VACÍA**

#### 0 · sin personas → text.mode = `in_image` (texto dentro de la imagen) — 14 reglas

  - `brand-lock-extractor/SKILL.md:54` [PROCESS] — 3. **Typography** (display, body, optional mono, with weights)
  - `brand-lock-extractor/SKILL.md:82` [FORBID] — - All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion languag
  - `brand-lock-extractor/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `image/SKILL.md:56` [PROCESS] — - Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
  - `image/references/models.md:50` [PROCESS] — | Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/text-rendering.md:133` [RECOMMEND] — Describe typography style or name the font directly:
  - `produccion-visual-sw30/SKILL.md:132` [GATE] — 10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los cuerpos nunca tapan logo ni lettering en frames congelados.
  - `storyboard-architect/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `storyboard-architect/references/beat-frameworks.md:45` [RECOMMEND] — Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/on-screen-text.md:71` [REQUIRE] — Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the br
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

#### 0 · sin personas → text.mode = `composite` (texto compuesto después) — 7 reglas

  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:105` [FORBID] — - **Don't include text content in image prompts**, composite separately; text rendering is mediocre
  - `visual-prompt-forge/adapters/nano-banana.md:83` [PROCESS] — 4. Composite text on the chosen variant
  - `visual-prompt-forge/adapters/seedream.md:82` [FORBID] — - **Don't include text content**, text rendering is poor; composite separately
  - `visual-prompt-forge/references/failure-modes.md:53` [FORBID] — - The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.

#### 0 · sin personas → generator.family = `nano_banana` (Nano Banana / Pro) — 34 reglas

  - `image/SKILL.md:100` [REQUIRE] — For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:40` [FORBID] — - **Nano Banana** → [nano-banana.md](references/nano-banana.md) Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mo
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:78` [REQUIRE] — - **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
  - `image/references/models.md:10` [PROCESS] — | Сложная сцена с физикой/композицией | **Nano Banana Pro** |
  - `image/references/models.md:11` [PROCESS] — | Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
  - `image/references/models.md:12` [PROCESS] — | Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
  - `image/references/models.md:17` [PROCESS] — | Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:9` [PROCESS] — | Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/nano-banana.md:55` [RECOMMEND] — Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены пл
  - `image/references/patterns/ecommerce.md:114` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for believable physical distortion
  - `image/references/patterns/fashion-editorial.md:107` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/food-beverage.md:110` [RECOMMEND] — **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
  - `image/references/patterns/food-beverage.md:124` [RECOMMEND] — **Recommended model:** NB2 — image grounding for real city landmarks + illustration style
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
  - `image/references/prompt-framework.md:43` [REQUIRE] — > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
  - `image/references/prompt-framework.md:87` [PROCESS] — **3. Exclusions** - что исключить (опционально): > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
  - `visual-prompt-forge/SKILL.md:109` [FORBID] — That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the build when an adapter advertises more words than its ceiling
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/nano-banana.md:101` [FORBID] — - **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
  - `visual-prompt-forge/adapters/nano-banana.md:102` [FORBID] — - **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
  - `visual-prompt-forge/adapters/nano-banana.md:104` [REQUIRE] — - **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:81` [PROCESS] — 2. Feed that image to Nano Banana with variation prompts
  - `visual-prompt-forge/references/failure-modes.md:129` [RECOMMEND] — 2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-prod

#### 0 · sin personas → generator.family = `gpt_image` (GPT Image 2) — 59 reglas

  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:43` [REQUIRE] — - **GPT Image 2** → [gpt-image.md](references/gpt-image.md) 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop 
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:74` [REQUIRE] — > **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.
  - `image/references/golden-rules.md:93` [REQUIRE] — Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.
  - `image/references/gpt-image.md:117` [RECOMMEND] — GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не распи
  - `image/references/models.md:13` [PROCESS] — | Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
  - `image/references/models.md:14` [PROCESS] — | Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
  - `image/references/models.md:15` [PROCESS] — | Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
  - `image/references/models.md:16` [PROCESS] — | Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
  - `image/references/models.md:18` [PROCESS] — | Storyboard с фокусом на типографике | **GPT Image 2** |
  - `image/references/models.md:19` [PROCESS] — | Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:26` [REQUIRE] — - **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
  - `image/references/multi-panel.md:122` [RECOMMEND] — **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych) **Model:** GPT Image 2 `quality: medium` — if text overlay need
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa
  - `image/references/patterns/character-design.md:108` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
  - `image/references/patterns/character-design.md:140` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering
  - `image/references/patterns/character-design.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
  - `image/references/patterns/character-design.md:3` [RECOMMEND] — Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}`
  - `image/references/patterns/character-design.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
  - `image/references/patterns/character-design.md:80` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
  - `image/references/patterns/ecommerce.md:74` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
  - `image/references/patterns/ecommerce.md:94` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
  - `image/references/patterns/fashion-editorial.md:27` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
  - `image/references/patterns/fashion-editorial.md:73` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:35` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
  - `image/references/patterns/food-beverage.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
  - `image/references/patterns/food-beverage.md:96` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `image/references/patterns/portrait-cinema.md:63` [RECOMMEND] — **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:3` [RECOMMEND] — Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. De
  - `image/references/patterns/poster-illustration.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
  - `image/references/patterns/poster-illustration.md:82` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
  - `image/references/patterns/ui-social.md:104` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements requir
  - `image/references/patterns/ui-social.md:135` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout
  - `image/references/patterns/ui-social.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
  - `image/references/patterns/ui-social.md:3` [RECOMMEND] — Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for c
  - `image/references/patterns/ui-social.md:49` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
  - `image/references/patterns/ui-social.md:75` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/gpt-image.md:38` [RECOMMEND] — GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:86` [FORBID] — - **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
  - `visual-prompt-forge/adapters/gpt-image.md:89` [FORBID] — - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
  - `visual-prompt-forge/references/failure-modes.md:87` [RECOMMEND] — - For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

#### 0 · sin personas → generator.family = `midjourney` (Midjourney) — 13 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:18` [PROCESS] — - Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
  - `visual-prompt-forge/SKILL.md:295` [REQUIRE] — If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. T
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
  - `visual-prompt-forge/references/consistency-locks.md:64` [RECOMMEND] — For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
  - `visual-prompt-forge/references/failure-modes.md:39` [RECOMMEND] — - For Midjourney, use `--cref` with `--cw 50`

#### 0 · sin personas → generator.family = `flux` (Flux) — 13 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/flux.md:86` [RECOMMEND] — Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.
  - `visual-prompt-forge/adapters/flux.md:90` [FORBID] — - **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
  - `visual-prompt-forge/adapters/flux.md:91` [FORBID] — - **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:69` [RECOMMEND] — **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

#### 0 · sin personas → generator.family = `ideogram` (Ideogram) — 14 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:257` [REQUIRE] — If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:30` [REQUIRE] — The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/ideogram.md:92` [FORBID] — - **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
  - `visual-prompt-forge/adapters/ideogram.md:93` [FORBID] — - **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
  - `visual-prompt-forge/references/failure-modes.md:54` [REQUIRE] — - If text must be in-image (poster work), use Ideogram v3 with explicit override flag
  - `visual-prompt-forge/references/failure-modes.md:56` [RECOMMEND] — - Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
  - `visual-prompt-forge/references/prompt-anatomy.md:58` [FORBID] — **What:** on-screen text composited after generation. **Source:** `text-overlays.json`. **Never appears in image prompts** (except Ideogram Mode 2 wit
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

#### 0 · sin personas → generator.family = `seedream` (Seedream) — 3 reglas

  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/seedream.md:80` [FORBID] — - **Don't write paragraphs**. Seedream wants comma-separated phrases
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output

## UNA REFERENCIA (`references.count = 1`) — 12 reglas propias

  - `image/SKILL.md:63` [PROCESS] — - **Vision analysis / image-to-prompt / style transfer from a reference image** → [vision-decomposer.md](references/vision-decomposer.md). Load this w
  - `image/references/characters.md:14` [REQUIRE] — Key phrase: "Keep facial features exactly the same as Image 1"
  - `image/references/golden-rules.md:105` [REQUIRE] — **Лицо/персонаж как референс:**
  - `image/references/golden-rules.md:112` [REQUIRE] — **Продукт/объект как референс:**
  - `image/references/golden-rules.md:119` [REQUIRE] — **Стиль как референс:**
  - `image/references/vision-decomposer.md:109` [FORBID] — Do NOT load this for: pure generation requests where no reference image is given. For those, use the standard model files.
  - `learned/production-learnings.v3.2.json:13` [REQUIRE] — When a user supplies an image only to follow or study its composition, first translate the visible composition into an abstract composition specificat
  - `produccion-visual-sw30/SKILL.md:127` [GATE] — 7. Mundos por dos pasos: placa vacía primero; insert con "use only the person from image N, ignore its setting" + "keep the world of image 1 untouched
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/consistency-locks.md:62` [REQUIRE] — 3. Each subsequent prompt has the verbatim character anchor PLUS the reference image link
  - `visual-prompt-forge/references/consistency-locks.md:74` [RECOMMEND] — When the storyboard has a distinctive visual style (specific film stock, specific lighting school, specific color theory), use a style reference image
  - `visual-prompt-forge/references/failure-modes.md:37` [RECOMMEND] — - Use reference image after the first successful shot

### CON PERSONAS — 74 reglas propias

  - `ai-production-director/SKILL.md:52` [PROCESS] — | Narrativa | Un beat (hook→payoff) | Arco simple | Multi-escena, personajes |
  - `aurora-prompt-linter/SKILL.md:158` [RECOMMEND] — - **Sub-tags por categoría**: O.upper / O.lower / P.face / P.body no soportados — un ref tagueado como O cubre todo outfit. Si el ref solo muestra el 
  - `aurora-prompt-linter/references/README.md:97` [RECOMMEND] — 6. **Exenciones**: términos en contexto de motion/cámara o como anchor direccional (`away from her face`, `across the climbing wall`) NO se flaggean.
  - `brand-lock-extractor/SKILL.md:20` [PROCESS] — - Hands over a URL, a PDF, image files, or a written brand description and asks for a brand-lock
  - `brand-lock-extractor/references/extraction-rubric.md:59` [FORBID] — - Imagery: no stock-photo gloss? no people? no gradients? no clip-art icons? Each absence is a never.
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:64` [PROCESS] — - **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 
  - `image/references/creative-direction.md:34` [REQUIRE] — - Hasselblad — medium format, shallow DOF, fashion/portrait
  - `image/references/creative-direction.md:47` [RECOMMEND] — - "Waist-up portrait", "full body", "over-the-shoulder"
  - `image/references/golden-rules.md:105` [REQUIRE] — **Лицо/персонаж как референс:**
  - `image/references/golden-rules.md:16` [REQUIRE] — - ✅ "solo portrait" → ❌ "no other people"
  - `image/references/gpt-image.md:94` [RECOMMEND] — **Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows s
  - `image/references/multi-panel.md:210` [REQUIRE] — - Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
  - `image/references/multi-panel.md:294` [REQUIRE] — **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space) **Model:** GPT Image 2 `quality: high` (text-heavy — scene number
  - `image/references/multi-panel.md:308` [REQUIRE] — **Subject consistency:** Always include an explicit instruction: "same person / same character / same product across all panels." Repeat key identity 
  - `image/references/multi-panel.md:57` [RECOMMEND] — **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/patterns/character-design.md:106` [RECOMMEND] — **Key levers:** `{character_name}`, `{character_description_simplified}` (key outfit and hair only), `{face_markers}` (e.g. round glasses, scar on lef
  - `image/references/patterns/character-design.md:120` [RECOMMEND] — Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional con
  - `image/references/patterns/character-design.md:29` [RECOMMEND] — Use to produce a grid of 6–9 facial expressions for the same character — consistent head angle and art style, with emotion labels under each face.
  - `image/references/patterns/character-design.md:58` [RECOMMEND] — Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
  - `image/references/patterns/fashion-editorial.md:33` [RECOMMEND] — Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
  - `image/references/patterns/portrait-cinema.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/patterns/portrait-cinema.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
  - `image/references/patterns/portrait-cinema.md:61` [RECOMMEND] — **Key levers:** `{person_description}`, `{direction}` (left, right), `{hair_detail}` (tight buzz cut showing skull contour, shoulder-length hair with 
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:83` [RECOMMEND] — Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elem
  - `image/references/patterns/portrait-cinema.md:9` [RECOMMEND] — Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
  - `image/references/patterns/portrait-cinema.md:97` [RECOMMEND] — **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)
  - `image/references/patterns/poster-illustration.md:117` [RECOMMEND] — **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/patterns/ui-social.md:116` [RECOMMEND] — Use to create a visual color analysis graphic from a portrait — seasonal palette classification, clothing color comparisons, and accessory recommendat
  - `image/references/patterns/ui-social.md:133` [REQUIRE] — **Key levers:** `{subject_description}` (age, skin tone, hair color, eye color — needed for accurate seasonal analysis), `{season_type}` (Warm Spring,
  - `image/references/prompt-framework.md:213` [RECOMMEND] — 2. **Micro-textures** — "visible pores on skin, individual hair strands catching backlight, fabric weave pattern on linen shirt, grain of weathered wo
  - `image/references/prompt-framework.md:218` [RECOMMEND] — 7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby si
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"
  - `image/references/vision-decomposer.md:36` [PROCESS] — - **Figure & ground (Arnheim):** degree of subject isolation, overlapping of forms, mass relationships. Use of reflections (mirrors, windows) to expan
  - `image/references/vision-decomposer.md:44` [PROCESS] — - **Broken light & reflexes (Zheleznyakov):** use of shadow masks (gobos), light through blinds / foliage, color reflexes from neighboring objects ont
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `learned/production-learnings.v3.2.json:3` [REQUIRE] — Preserve a sufficiently specific domain-native pose/technique label instead of expanding it into speculative anatomy. Expand only when the target adap
  - `learned/production-learnings.v3.2.json:8` [RECOMMEND] — For complex underwater human anatomy, physically justified bubbles/turbulence may obscure non-critical anatomical detail when the brief does not requi
  - `produccion-visual-sw30/SKILL.md:116` [GATE] — 1. Un solo trabajo por generación. Con dos personajes: un sujeto por generación, o técnica de colocación probada; nunca "a ver si sale".
  - `produccion-visual-sw30/SKILL.md:123` [GATE] — 5. Herencia mínima: "same face and clothes" + solo los deltas. Cero re-descripción de lo que la referencia ya muestra.
  - `produccion-visual-sw30/SKILL.md:127` [GATE] — 7. Mundos por dos pasos: placa vacía primero; insert con "use only the person from image N, ignore its setting" + "keep the world of image 1 untouched
  - `produccion-visual-sw30/SKILL.md:130` [GATE] — 9. Contactos entre personas: "a natural high five" — la anatomía la fija el keyframe aprobado, nunca la asignación de manos por texto.
  - `produccion-visual-sw30/SKILL.md:35` [GATE] — 1. **CATALOGAR** — identificar el TIPO de prompt y leer qué reglas aplican a ese tipo en la matriz (production-package/RULES_MATRIX.md: 26 reglas × 5 
  - `produccion-visual-sw30/SKILL.md:39` [GATE] — 2. **DEFINIR SECCIONES** — antes de redactar, listar las secciones que ese tipo exige. Cada regla vive en UN bloque nombrado y compartido (optics_*, s
  - `storyboard-architect/SKILL.md:18` [PROCESS] — - Hands over a script, brief, or concept document expecting structured pre-production output
  - `storyboard-architect/SKILL.md:266` [GATE] — - [ ] `series_lock` anchors are specific enough to reproduce (not "a person in a room")
  - `storyboard-architect/references/beat-frameworks.md:33` [RECOMMEND] — Default for personal-brand video where a person speaks to camera. Five micro-beats:
  - `storyboard-architect/references/beat-frameworks.md:41` [RECOMMEND] — Use when: founder content, thought leadership, personal-brand pieces.
  - `storyboard-html-preview/SKILL.md:19` [PROCESS] — - Hands off `storyboard.md` + `shots.json` + asks for a deliverable for review
  - `visual-asset-critic/SKILL.md:102` [REQUIRE] — **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts: > "Hands are mangled. This is a known Fl
  - `visual-asset-critic/SKILL.md:224` [REQUIRE] — "Looks great" / "feels off" without specifics is not a critique. Every observation must reference something in the image (composition, color, anatomy,
  - `visual-asset-critic/SKILL.md:236` [FORBID] — Some failures (mangled hands, weird eye reflections, jewelry shimmer) are known generator weaknesses. Surface them as such, don't pretend a different 
  - `visual-asset-critic/SKILL.md:24` [GATE] — **Two artifacts from every review, always both:** a human-readable markdown critique (the primary surface) and a machine-readable critique JSON (so a 
  - `visual-asset-critic/SKILL.md:87` [PROCESS] — 5. **Technical**, skin texture, hands, eyes, anatomy, AI artifacts?
  - `visual-asset-critic/SKILL.md:96` [REQUIRE] — **Prompt-level fix**, change the prompt and re-roll. Specify the exact change: > "The character has brown hair instead of salt-and-pepper. Add 'salt-a
  - `visual-asset-critic/references/critique-rubric.md:111` [REQUIRE] — - **Distinguish prompt failure from generator failure**, if the prompt was fine and the generator produced garbage hands, that's "re-roll required", n
  - `visual-prompt-forge/SKILL.md:16` [PROCESS] — - Hands over a `shots.json` (or any structured shot list) and asks for prompts
  - `visual-prompt-forge/SKILL.md:186` [FORBID] — This is what `visual-asset-critic`'s structured output is for. When the user hands you `shots.json` plus one or more `critique.json` files (the machin
  - `visual-prompt-forge/SKILL.md:190` [RECOMMEND] — The user says "apply the critique", "revise the failed shots", "re-roll what didn't pass", or hands over an output tree containing `critiques/`.
  - `visual-prompt-forge/SKILL.md:215` [PROCESS] — 6. Re-apply the five-layer anatomy and the same adapter as the original run.
  - `visual-prompt-forge/SKILL.md:281` [REQUIRE] — `character` is a warning rather than an error, because a shot with no person in it can legitimately leave it out. When the shot has a person, it is ve
  - `visual-prompt-forge/SKILL.md:305` [REQUIRE] — - **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no
  - `visual-prompt-forge/adapters/flux.md:66` [REQUIRE] — The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.
  - `visual-prompt-forge/adapters/gpt-image.md:46` [RECOMMEND] — - "The subject's shoulders are angled 30 degrees toward the camera, face turned to look at the off-frame light source."
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/references/consistency-locks.md:113` [FORBID] — A few things people try that don't actually fix consistency:
  - `visual-prompt-forge/references/consistency-locks.md:115` [FORBID] — - **Adding "consistent character" or "same person" to the prompt**, generators don't read meta-instructions
  - `visual-prompt-forge/references/consistency-locks.md:70` [RECOMMEND] — **This is the most effective lock for character consistency** in 2026. Use it whenever the storyboard features the same person across multiple shots.
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)

#### UNA PERSONA — 1 reglas propias

  - `produccion-visual-sw30/SKILL.md:116` [GATE] — 1. Un solo trabajo por generación. Con dos personajes: un sujeto por generación, o técnica de colocación probada; nunca "a ver si sale".

##### 1 · personas · 1 → style.photography = `editorial` (editorial) — 16 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/multi-panel.md:57` [RECOMMEND] — **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:33` [RECOMMEND] — Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:9` [RECOMMEND] — Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 
  - `visual-asset-critic/SKILL.md:20` [PROCESS] — - Has a generated image and just wants editorial feedback (no storyboard reference)
  - `visual-asset-critic/SKILL.md:8` [FORBID] — You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structu
  - `visual-prompt-forge/adapters/nano-banana.md:82` [PROCESS] — 3. Get 4–8 variants of the same shot for editorial selection
  - `visual-prompt-forge/references/consistency-locks.md:109` [FORBID] — Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.
  - `visual-prompt-forge/references/failure-modes.md:130` [RECOMMEND] — 3. The image is 80% right and the gap is editorial → ship to post and let the editor finish
  - `visual-prompt-forge/references/failure-modes.md:3` [FORBID] — What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

##### 1 · personas · 1 → style.photography = `documental` (documental / fotoperiodismo) — 1 reglas

  - `produccion-visual-sw30/SKILL.md:73` [GATE] — | usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO

##### 1 · personas · 1 → style.photography = `natgeo` (documental de naturaleza (National Geographic)) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → style.photography = `moda` (moda) — 8 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/creative-direction.md:34` [REQUIRE] — - Hasselblad — medium format, shallow DOF, fashion/portrait
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/character-design.md:58` [RECOMMEND] — Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o

##### 1 · personas · 1 → style.photography = `producto` (producto / e-commerce) — 1 reglas

  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)

##### 1 · personas · 1 → style.photography = `cinematografico` (cinematográfico) — 9 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:67` [RECOMMEND] — The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site 
  - `image/SKILL.md:64` [PROCESS] — - **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 
  - `image/SKILL.md:69` [PROCESS] — - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - `image/SKILL.md:80` [PROCESS] — Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / stand
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/nano-banana.md:25` [RECOMMEND] — - Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `visual-asset-critic/references/critique-rubric.md:107` [FORBID] — - **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
  - `visual-prompt-forge/references/consistency-locks.md:96` [REQUIRE] — The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal s

##### 1 · personas · 1 → style.photography = `vintage` (vintage / analógico) — 7 reglas

  - `image/SKILL.md:76` [PROCESS] — Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise 
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `visual-prompt-forge/references/consistency-locks.md:74` [RECOMMEND] — When the storyboard has a distinctive visual style (specific film stock, specific lighting school, specific color theory), use a style reference image
  - `visual-prompt-forge/references/failure-modes.md:17` [RECOMMEND] — - Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")

##### 1 · personas · 1 → style.photography = `calle` (fotografía de calle) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → style.photography = `movil` (móvil / snapshot) — 3 reglas

  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `storyboard-html-preview/SKILL.md:238` [RECOMMEND] — Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
  - `storyboard-html-preview/SKILL.md:255` [GATE] — - [ ] Mobile viewport (375px) renders without horizontal scroll

##### 1 · personas · 1 → style.photography = `bellas_artes` (bellas artes / conceptual) — 1 reglas

  - `image/references/patterns/portrait-cinema.md:83` [RECOMMEND] — Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elem

##### 1 · personas · 1 → style.photography = `estudio` (retrato de estudio) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → lighting.setup = `estudio` (estudio (softbox, strobe, controlada)) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → lighting.setup = `natural_exterior` (natural exterior) — 1 reglas

  - `visual-prompt-forge/adapters/flux.md:56` [RECOMMEND] — - `Sony FX6, 35mm prime, natural light only`

##### 1 · personas · 1 → lighting.setup = `ventana` (luz entrando por ventana) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → lighting.setup = `golden_hour` (golden hour / atardecer) — 1 reglas

  - `image/references/prompt-framework.md:214` [RECOMMEND] — 3. **Atmospheric particles** — "dust motes suspended in light beam, steam wisps rising from coffee cup, pollen floating in golden hour air, fine rain 

##### 1 · personas · 1 → lighting.setup = `artificial_nocturna` (artificial nocturna) — 3 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/prompt-framework.md:218` [RECOMMEND] — 7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby si

##### 1 · personas · 1 → lighting.setup = `mixta` (mixta) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → composition.shot_size = `macro` (macro / detalle) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → composition.shot_size = `close_up` (close-up) — 3 reglas

  - `image/references/multi-panel.md:94` [RECOMMEND] — **When to use:** Hero shot + close-up + action for a campaign visual — horizontal or vertical triptych.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `storyboard-architect/references/shot-grammar.md:11` [RECOMMEND] — | `MCU` | Medium close-up | Head and shoulders |

##### 1 · personas · 1 → composition.shot_size = `plano_medio` (plano medio) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → composition.shot_size = `cuerpo_completo` (cuerpo completo) — 2 reglas

  - `image/references/creative-direction.md:47` [RECOMMEND] — - "Waist-up portrait", "full body", "over-the-shoulder"
  - `image/references/patterns/character-design.md:120` [RECOMMEND] — Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional con

##### 1 · personas · 1 → composition.shot_size = `plano_general` (plano general / amplio) — 2 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

##### 1 · personas · 1 → task.theme = `deportiva` (deportiva) — 6 reglas

  - `aurora-prompt-linter/SKILL.md:157` [RECOMMEND] — - **Sinónimos**: "tank top" en ref + "athletic shirt" en prompt no se detecta como redundante. Roadmap v1.1: tabla de sinónimos.
  - `aurora-prompt-linter/references/README.md:96` [RECOMMEND] — 5. **Sports broadcast**: si flag activo, requiere `60fps` y `broadcast realism` en MAIN (Regla 26 v6.0).
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:93` [RECOMMEND] — Use for forward-looking athletic or techwear editorials where abstract 3D forms create a surreal spatial environment around the model.
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 

##### 1 · personas · 1 → task.theme = `musical` (musical / concierto) — 2 reglas

  - `image/references/patterns/portrait-cinema.md:49` [RECOMMEND] — Use for edgy, tech-forward portraits — artist profiles, electronic music press, tech brand campaigns. High contrast black-and-white with selective red
  - `storyboard-architect/references/on-screen-text.md:10` [RECOMMEND] — 4. **Beat punctuation.** A single word or phrase that lands on a music hit.

##### 1 · personas · 1 → task.theme = `moda` (moda) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → task.theme = `gastronomica` (gastronómica) — 8 reglas

  - `image/SKILL.md:68` [PROCESS] — - Food & beverage advertising → [patterns/food-beverage.md](references/patterns/food-beverage.md)
  - `image/references/patterns/ecommerce.md:80` [RECOMMEND] — Use for food, beverage, or supplement products where suspended ingredients communicate freshness, flavor, or composition.
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:41` [RECOMMEND] — Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
  - `image/references/patterns/food-beverage.md:65` [RECOMMEND] — Use for hero food posters — restaurants, delivery apps, menu boards — where the food is the entire composition with fillable content slots.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"

##### 1 · personas · 1 → task.theme = `corporativa` (corporativa) — 3 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:52` [RECOMMEND] — Reject generic fillers ("professional, modern, clean"), they describe everything and constrain nothing. Push to contrast clauses that do work: "operat
  - `visual-prompt-forge/SKILL.md:269` [REQUIRE] — Verbatim means the whole string, unedited. Not "the same idea in better prose". The failure mode is specific and easy to walk into: you are writing fl
  - `visual-prompt-forge/SKILL.md:276` [REQUIRE] — Capitalising the first letter to start a sentence is fine, because the check is case-insensitive. "Minimalist home office, white walls, oak desk, sing

##### 1 · personas · 1 → task.theme = `medica` (médica / científica) — 3 reglas

  - `brand-lock-extractor/SKILL.md:114` [REQUIRE] — The output is a clinical specification. It models the standards the brand-lock enforces. No emojis anywhere. No marketing adjectives about the brand i
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `learned/production-learnings.v3.2.json:11` [REQUIRE] — Once an image is accepted and requested changes are local, perform a surgical image edit and preserve the approved pixels/locks outside the requested 

##### 1 · personas · 1 → task.theme = `viaje` (viaje / turismo) — 3 reglas

  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `visual-prompt-forge/SKILL.md:303` [REQUIRE] — - **The direction of travel.** Left to right, right to left, toward camera. Without it the generator picks, and consecutive shots stop matching.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 1 · personas · 1 → task.theme = `automotriz` (automotriz) — 1 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo

##### 1 · personas · 1 → task.theme = `otra` (otra) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → motion.action_complexity = `estatica` (estática) — 11 reglas

  - `brand-lock-extractor/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `storyboard-architect/SKILL.md:263` [GATE] — What the validator cannot check, and you still have to:
  - `storyboard-architect/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `visual-asset-critic/SKILL.md:170` [GATE] — The hashes are the point. Without `image_sha256`, a frame regenerated after this review still satisfies `image_ref`, and a stale ACCEPT sails through 
  - `visual-asset-critic/SKILL.md:215` [GATE] — Worked examples: `examples/critique.accept.json` and `examples/critique.revise.json` show the shape at version `1.0`, which is still valid and carries
  - `visual-prompt-forge/SKILL.md:299` [REQUIRE] — A prompt can be beautifully written and still be impossible to shoot. Every prompt declares, before anything else:
  - `visual-prompt-forge/SKILL.md:360` [GATE] — What it cannot check, and you still have to:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/references/prompt-anatomy.md:66` [RECOMMEND] — 3. **Animation.** Animated text needs After Effects / Remotion / CapCut. Static rendered text is dead-on-arrival for motion content.

##### 1 · personas · 1 → motion.action_complexity = `pose_dirigida` (pose dirigida) — 6 reglas

  - `image/references/gpt-image.md:94` [RECOMMEND] — **Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows s
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `learned/production-learnings.v3.2.json:3` [REQUIRE] — Preserve a sufficiently specific domain-native pose/technique label instead of expanding it into speculative anatomy. Expand only when the target adap
  - `learned/production-learnings.v3.2.json:4` [REQUIRE] — A reference may control only its declared role. Features explicitly excluded from that role must not be copied into subject identity, pose, camera, fr
  - `learned/production-learnings.v3.2.json:8` [RECOMMEND] — For complex underwater human anatomy, physically justified bubbles/turbulence may obscure non-critical anatomical detail when the brief does not requi
  - `produccion-visual-sw30/SKILL.md:125` [GATE] — 6. Swap de identidad = última operación, sola: "Replace X with Y — same position, same pose, same scale".

##### 1 · personas · 1 → motion.action_complexity = `accion_simple` (acción simple (un cuerpo)) — 5 reglas

  - `image/references/multi-panel.md:210` [REQUIRE] — - Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"
  - `learned/production-learnings.v3.2.json:10` [REQUIRE] — Do not declare a generated asset or model successful for a case before running the applicable QA. Separate deterministic/mechanical checks from semant
  - `visual-prompt-forge/SKILL.md:302` [REQUIRE] — - **The point of view.** Profile, frontal, side, rear. "A man walking" is not a shot.

##### 1 · personas · 1 → motion.action_complexity = `accion_compleja` (acción compleja (varios cuerpos, contacto, física)) — 4 reglas

  - `image/references/prompt-framework.md:217` [RECOMMEND] — 6. **Contact shadows** — "soft contact shadow where cup meets saucer, ambient occlusion in crevices of stone wall, dark line where book spine meets ta
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:305` [REQUIRE] — - **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 1 · personas · 1 → text.mode = `none` (sin texto) — **0 reglas · RAMA VACÍA**

##### 1 · personas · 1 → text.mode = `in_image` (texto dentro de la imagen) — 16 reglas

  - `brand-lock-extractor/SKILL.md:54` [PROCESS] — 3. **Typography** (display, body, optional mono, with weights)
  - `brand-lock-extractor/SKILL.md:82` [FORBID] — - All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion languag
  - `brand-lock-extractor/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `image/SKILL.md:56` [PROCESS] — - Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
  - `image/references/models.md:50` [PROCESS] — | Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/text-rendering.md:133` [RECOMMEND] — Describe typography style or name the font directly:
  - `produccion-visual-sw30/SKILL.md:132` [GATE] — 10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los cuerpos nunca tapan logo ni lettering en frames congelados.
  - `storyboard-architect/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `storyboard-architect/references/beat-frameworks.md:45` [RECOMMEND] — Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/on-screen-text.md:71` [REQUIRE] — Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the br
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 1 · personas · 1 → text.mode = `composite` (texto compuesto después) — 7 reglas

  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:105` [FORBID] — - **Don't include text content in image prompts**, composite separately; text rendering is mediocre
  - `visual-prompt-forge/adapters/nano-banana.md:83` [PROCESS] — 4. Composite text on the chosen variant
  - `visual-prompt-forge/adapters/seedream.md:82` [FORBID] — - **Don't include text content**, text rendering is poor; composite separately
  - `visual-prompt-forge/references/failure-modes.md:53` [FORBID] — - The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.

##### 1 · personas · 1 → generator.family = `nano_banana` (Nano Banana / Pro) — 39 reglas

  - `image/SKILL.md:100` [REQUIRE] — For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:40` [FORBID] — - **Nano Banana** → [nano-banana.md](references/nano-banana.md) Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mo
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:78` [REQUIRE] — - **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
  - `image/references/models.md:10` [PROCESS] — | Сложная сцена с физикой/композицией | **Nano Banana Pro** |
  - `image/references/models.md:11` [PROCESS] — | Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
  - `image/references/models.md:12` [PROCESS] — | Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
  - `image/references/models.md:17` [PROCESS] — | Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:9` [PROCESS] — | Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/nano-banana.md:55` [RECOMMEND] — Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены пл
  - `image/references/patterns/ecommerce.md:114` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for believable physical distortion
  - `image/references/patterns/fashion-editorial.md:107` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/food-beverage.md:110` [RECOMMEND] — **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
  - `image/references/patterns/food-beverage.md:124` [RECOMMEND] — **Recommended model:** NB2 — image grounding for real city landmarks + illustration style
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/portrait-cinema.md:97` [RECOMMEND] — **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)
  - `image/references/patterns/poster-illustration.md:117` [RECOMMEND] — **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species
  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
  - `image/references/prompt-framework.md:43` [REQUIRE] — > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
  - `image/references/prompt-framework.md:87` [PROCESS] — **3. Exclusions** - что исключить (опционально): > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:109` [FORBID] — That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the build when an adapter advertises more words than its ceiling
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/nano-banana.md:101` [FORBID] — - **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
  - `visual-prompt-forge/adapters/nano-banana.md:102` [FORBID] — - **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
  - `visual-prompt-forge/adapters/nano-banana.md:104` [REQUIRE] — - **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:81` [PROCESS] — 2. Feed that image to Nano Banana with variation prompts
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/failure-modes.md:129` [RECOMMEND] — 2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-prod

##### 1 · personas · 1 → generator.family = `gpt_image` (GPT Image 2) — 65 reglas

  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:43` [REQUIRE] — - **GPT Image 2** → [gpt-image.md](references/gpt-image.md) 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop 
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:74` [REQUIRE] — > **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.
  - `image/references/golden-rules.md:93` [REQUIRE] — Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.
  - `image/references/gpt-image.md:117` [RECOMMEND] — GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не распи
  - `image/references/models.md:13` [PROCESS] — | Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
  - `image/references/models.md:14` [PROCESS] — | Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
  - `image/references/models.md:15` [PROCESS] — | Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
  - `image/references/models.md:16` [PROCESS] — | Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
  - `image/references/models.md:18` [PROCESS] — | Storyboard с фокусом на типографике | **GPT Image 2** |
  - `image/references/models.md:19` [PROCESS] — | Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:26` [REQUIRE] — - **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
  - `image/references/multi-panel.md:122` [RECOMMEND] — **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych) **Model:** GPT Image 2 `quality: medium` — if text overlay need
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:294` [REQUIRE] — **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space) **Model:** GPT Image 2 `quality: high` (text-heavy — scene number
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/patterns/character-design.md:108` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
  - `image/references/patterns/character-design.md:140` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering
  - `image/references/patterns/character-design.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
  - `image/references/patterns/character-design.md:3` [RECOMMEND] — Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}`
  - `image/references/patterns/character-design.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
  - `image/references/patterns/character-design.md:80` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
  - `image/references/patterns/ecommerce.md:74` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
  - `image/references/patterns/ecommerce.md:94` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
  - `image/references/patterns/fashion-editorial.md:27` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
  - `image/references/patterns/fashion-editorial.md:73` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:35` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
  - `image/references/patterns/food-beverage.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
  - `image/references/patterns/food-beverage.md:96` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
  - `image/references/patterns/portrait-cinema.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `image/references/patterns/portrait-cinema.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
  - `image/references/patterns/portrait-cinema.md:63` [RECOMMEND] — **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:3` [RECOMMEND] — Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. De
  - `image/references/patterns/poster-illustration.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
  - `image/references/patterns/poster-illustration.md:82` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
  - `image/references/patterns/ui-social.md:104` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements requir
  - `image/references/patterns/ui-social.md:135` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout
  - `image/references/patterns/ui-social.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
  - `image/references/patterns/ui-social.md:3` [RECOMMEND] — Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for c
  - `image/references/patterns/ui-social.md:49` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
  - `image/references/patterns/ui-social.md:75` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/gpt-image.md:38` [RECOMMEND] — GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:86` [FORBID] — - **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
  - `visual-prompt-forge/adapters/gpt-image.md:89` [FORBID] — - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:87` [RECOMMEND] — - For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 1 · personas · 1 → generator.family = `midjourney` (Midjourney) — 14 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:18` [PROCESS] — - Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
  - `visual-prompt-forge/SKILL.md:295` [REQUIRE] — If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. T
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/consistency-locks.md:64` [RECOMMEND] — For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
  - `visual-prompt-forge/references/failure-modes.md:39` [RECOMMEND] — - For Midjourney, use `--cref` with `--cw 50`

##### 1 · personas · 1 → generator.family = `flux` (Flux) — 17 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-asset-critic/SKILL.md:102` [REQUIRE] — **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts: > "Hands are mangled. This is a known Fl
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/flux.md:66` [REQUIRE] — The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.
  - `visual-prompt-forge/adapters/flux.md:86` [RECOMMEND] — Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.
  - `visual-prompt-forge/adapters/flux.md:90` [FORBID] — - **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
  - `visual-prompt-forge/adapters/flux.md:91` [FORBID] — - **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:69` [RECOMMEND] — **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

##### 1 · personas · 1 → generator.family = `ideogram` (Ideogram) — 15 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:257` [REQUIRE] — If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:30` [REQUIRE] — The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/ideogram.md:92` [FORBID] — - **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
  - `visual-prompt-forge/adapters/ideogram.md:93` [FORBID] — - **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/failure-modes.md:54` [REQUIRE] — - If text must be in-image (poster work), use Ideogram v3 with explicit override flag
  - `visual-prompt-forge/references/failure-modes.md:56` [RECOMMEND] — - Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
  - `visual-prompt-forge/references/prompt-anatomy.md:58` [FORBID] — **What:** on-screen text composited after generation. **Source:** `text-overlays.json`. **Never appears in image prompts** (except Ideogram Mode 2 wit
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 1 · personas · 1 → generator.family = `seedream` (Seedream) — 3 reglas

  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/seedream.md:80` [FORBID] — - **Don't write paragraphs**. Seedream wants comma-separated phrases
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output

#### GRUPO DE PERSONAS — 0 reglas propias


##### 1 · personas · grupo → style.photography = `editorial` (editorial) — 16 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/multi-panel.md:57` [RECOMMEND] — **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:33` [RECOMMEND] — Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:9` [RECOMMEND] — Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 
  - `visual-asset-critic/SKILL.md:20` [PROCESS] — - Has a generated image and just wants editorial feedback (no storyboard reference)
  - `visual-asset-critic/SKILL.md:8` [FORBID] — You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structu
  - `visual-prompt-forge/adapters/nano-banana.md:82` [PROCESS] — 3. Get 4–8 variants of the same shot for editorial selection
  - `visual-prompt-forge/references/consistency-locks.md:109` [FORBID] — Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.
  - `visual-prompt-forge/references/failure-modes.md:130` [RECOMMEND] — 3. The image is 80% right and the gap is editorial → ship to post and let the editor finish
  - `visual-prompt-forge/references/failure-modes.md:3` [FORBID] — What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

##### 1 · personas · grupo → style.photography = `documental` (documental / fotoperiodismo) — 1 reglas

  - `produccion-visual-sw30/SKILL.md:73` [GATE] — | usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO

##### 1 · personas · grupo → style.photography = `natgeo` (documental de naturaleza (National Geographic)) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → style.photography = `moda` (moda) — 8 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/creative-direction.md:34` [REQUIRE] — - Hasselblad — medium format, shallow DOF, fashion/portrait
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/character-design.md:58` [RECOMMEND] — Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o

##### 1 · personas · grupo → style.photography = `producto` (producto / e-commerce) — 1 reglas

  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)

##### 1 · personas · grupo → style.photography = `cinematografico` (cinematográfico) — 9 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:67` [RECOMMEND] — The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site 
  - `image/SKILL.md:64` [PROCESS] — - **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 
  - `image/SKILL.md:69` [PROCESS] — - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - `image/SKILL.md:80` [PROCESS] — Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / stand
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/nano-banana.md:25` [RECOMMEND] — - Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `visual-asset-critic/references/critique-rubric.md:107` [FORBID] — - **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
  - `visual-prompt-forge/references/consistency-locks.md:96` [REQUIRE] — The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal s

##### 1 · personas · grupo → style.photography = `vintage` (vintage / analógico) — 7 reglas

  - `image/SKILL.md:76` [PROCESS] — Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise 
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `visual-prompt-forge/references/consistency-locks.md:74` [RECOMMEND] — When the storyboard has a distinctive visual style (specific film stock, specific lighting school, specific color theory), use a style reference image
  - `visual-prompt-forge/references/failure-modes.md:17` [RECOMMEND] — - Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")

##### 1 · personas · grupo → style.photography = `calle` (fotografía de calle) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → style.photography = `movil` (móvil / snapshot) — 3 reglas

  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `storyboard-html-preview/SKILL.md:238` [RECOMMEND] — Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
  - `storyboard-html-preview/SKILL.md:255` [GATE] — - [ ] Mobile viewport (375px) renders without horizontal scroll

##### 1 · personas · grupo → style.photography = `bellas_artes` (bellas artes / conceptual) — 1 reglas

  - `image/references/patterns/portrait-cinema.md:83` [RECOMMEND] — Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elem

##### 1 · personas · grupo → style.photography = `estudio` (retrato de estudio) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → lighting.setup = `estudio` (estudio (softbox, strobe, controlada)) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → lighting.setup = `natural_exterior` (natural exterior) — 1 reglas

  - `visual-prompt-forge/adapters/flux.md:56` [RECOMMEND] — - `Sony FX6, 35mm prime, natural light only`

##### 1 · personas · grupo → lighting.setup = `ventana` (luz entrando por ventana) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → lighting.setup = `golden_hour` (golden hour / atardecer) — 1 reglas

  - `image/references/prompt-framework.md:214` [RECOMMEND] — 3. **Atmospheric particles** — "dust motes suspended in light beam, steam wisps rising from coffee cup, pollen floating in golden hour air, fine rain 

##### 1 · personas · grupo → lighting.setup = `artificial_nocturna` (artificial nocturna) — 3 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/prompt-framework.md:218` [RECOMMEND] — 7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby si

##### 1 · personas · grupo → lighting.setup = `mixta` (mixta) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → composition.shot_size = `macro` (macro / detalle) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → composition.shot_size = `close_up` (close-up) — 3 reglas

  - `image/references/multi-panel.md:94` [RECOMMEND] — **When to use:** Hero shot + close-up + action for a campaign visual — horizontal or vertical triptych.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `storyboard-architect/references/shot-grammar.md:11` [RECOMMEND] — | `MCU` | Medium close-up | Head and shoulders |

##### 1 · personas · grupo → composition.shot_size = `plano_medio` (plano medio) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → composition.shot_size = `cuerpo_completo` (cuerpo completo) — 2 reglas

  - `image/references/creative-direction.md:47` [RECOMMEND] — - "Waist-up portrait", "full body", "over-the-shoulder"
  - `image/references/patterns/character-design.md:120` [RECOMMEND] — Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional con

##### 1 · personas · grupo → composition.shot_size = `plano_general` (plano general / amplio) — 2 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

##### 1 · personas · grupo → task.theme = `deportiva` (deportiva) — 6 reglas

  - `aurora-prompt-linter/SKILL.md:157` [RECOMMEND] — - **Sinónimos**: "tank top" en ref + "athletic shirt" en prompt no se detecta como redundante. Roadmap v1.1: tabla de sinónimos.
  - `aurora-prompt-linter/references/README.md:96` [RECOMMEND] — 5. **Sports broadcast**: si flag activo, requiere `60fps` y `broadcast realism` en MAIN (Regla 26 v6.0).
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:93` [RECOMMEND] — Use for forward-looking athletic or techwear editorials where abstract 3D forms create a surreal spatial environment around the model.
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 

##### 1 · personas · grupo → task.theme = `musical` (musical / concierto) — 2 reglas

  - `image/references/patterns/portrait-cinema.md:49` [RECOMMEND] — Use for edgy, tech-forward portraits — artist profiles, electronic music press, tech brand campaigns. High contrast black-and-white with selective red
  - `storyboard-architect/references/on-screen-text.md:10` [RECOMMEND] — 4. **Beat punctuation.** A single word or phrase that lands on a music hit.

##### 1 · personas · grupo → task.theme = `moda` (moda) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → task.theme = `gastronomica` (gastronómica) — 8 reglas

  - `image/SKILL.md:68` [PROCESS] — - Food & beverage advertising → [patterns/food-beverage.md](references/patterns/food-beverage.md)
  - `image/references/patterns/ecommerce.md:80` [RECOMMEND] — Use for food, beverage, or supplement products where suspended ingredients communicate freshness, flavor, or composition.
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:41` [RECOMMEND] — Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
  - `image/references/patterns/food-beverage.md:65` [RECOMMEND] — Use for hero food posters — restaurants, delivery apps, menu boards — where the food is the entire composition with fillable content slots.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"

##### 1 · personas · grupo → task.theme = `corporativa` (corporativa) — 3 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:52` [RECOMMEND] — Reject generic fillers ("professional, modern, clean"), they describe everything and constrain nothing. Push to contrast clauses that do work: "operat
  - `visual-prompt-forge/SKILL.md:269` [REQUIRE] — Verbatim means the whole string, unedited. Not "the same idea in better prose". The failure mode is specific and easy to walk into: you are writing fl
  - `visual-prompt-forge/SKILL.md:276` [REQUIRE] — Capitalising the first letter to start a sentence is fine, because the check is case-insensitive. "Minimalist home office, white walls, oak desk, sing

##### 1 · personas · grupo → task.theme = `medica` (médica / científica) — 3 reglas

  - `brand-lock-extractor/SKILL.md:114` [REQUIRE] — The output is a clinical specification. It models the standards the brand-lock enforces. No emojis anywhere. No marketing adjectives about the brand i
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `learned/production-learnings.v3.2.json:11` [REQUIRE] — Once an image is accepted and requested changes are local, perform a surgical image edit and preserve the approved pixels/locks outside the requested 

##### 1 · personas · grupo → task.theme = `viaje` (viaje / turismo) — 3 reglas

  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `visual-prompt-forge/SKILL.md:303` [REQUIRE] — - **The direction of travel.** Left to right, right to left, toward camera. Without it the generator picks, and consecutive shots stop matching.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 1 · personas · grupo → task.theme = `automotriz` (automotriz) — 1 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo

##### 1 · personas · grupo → task.theme = `otra` (otra) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → motion.action_complexity = `estatica` (estática) — 11 reglas

  - `brand-lock-extractor/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `storyboard-architect/SKILL.md:263` [GATE] — What the validator cannot check, and you still have to:
  - `storyboard-architect/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `visual-asset-critic/SKILL.md:170` [GATE] — The hashes are the point. Without `image_sha256`, a frame regenerated after this review still satisfies `image_ref`, and a stale ACCEPT sails through 
  - `visual-asset-critic/SKILL.md:215` [GATE] — Worked examples: `examples/critique.accept.json` and `examples/critique.revise.json` show the shape at version `1.0`, which is still valid and carries
  - `visual-prompt-forge/SKILL.md:299` [REQUIRE] — A prompt can be beautifully written and still be impossible to shoot. Every prompt declares, before anything else:
  - `visual-prompt-forge/SKILL.md:360` [GATE] — What it cannot check, and you still have to:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/references/prompt-anatomy.md:66` [RECOMMEND] — 3. **Animation.** Animated text needs After Effects / Remotion / CapCut. Static rendered text is dead-on-arrival for motion content.

##### 1 · personas · grupo → motion.action_complexity = `pose_dirigida` (pose dirigida) — 6 reglas

  - `image/references/gpt-image.md:94` [RECOMMEND] — **Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows s
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `learned/production-learnings.v3.2.json:3` [REQUIRE] — Preserve a sufficiently specific domain-native pose/technique label instead of expanding it into speculative anatomy. Expand only when the target adap
  - `learned/production-learnings.v3.2.json:4` [REQUIRE] — A reference may control only its declared role. Features explicitly excluded from that role must not be copied into subject identity, pose, camera, fr
  - `learned/production-learnings.v3.2.json:8` [RECOMMEND] — For complex underwater human anatomy, physically justified bubbles/turbulence may obscure non-critical anatomical detail when the brief does not requi
  - `produccion-visual-sw30/SKILL.md:125` [GATE] — 6. Swap de identidad = última operación, sola: "Replace X with Y — same position, same pose, same scale".

##### 1 · personas · grupo → motion.action_complexity = `accion_simple` (acción simple (un cuerpo)) — 5 reglas

  - `image/references/multi-panel.md:210` [REQUIRE] — - Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"
  - `learned/production-learnings.v3.2.json:10` [REQUIRE] — Do not declare a generated asset or model successful for a case before running the applicable QA. Separate deterministic/mechanical checks from semant
  - `visual-prompt-forge/SKILL.md:302` [REQUIRE] — - **The point of view.** Profile, frontal, side, rear. "A man walking" is not a shot.

##### 1 · personas · grupo → motion.action_complexity = `accion_compleja` (acción compleja (varios cuerpos, contacto, física)) — 4 reglas

  - `image/references/prompt-framework.md:217` [RECOMMEND] — 6. **Contact shadows** — "soft contact shadow where cup meets saucer, ambient occlusion in crevices of stone wall, dark line where book spine meets ta
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:305` [REQUIRE] — - **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 1 · personas · grupo → text.mode = `none` (sin texto) — **0 reglas · RAMA VACÍA**

##### 1 · personas · grupo → text.mode = `in_image` (texto dentro de la imagen) — 16 reglas

  - `brand-lock-extractor/SKILL.md:54` [PROCESS] — 3. **Typography** (display, body, optional mono, with weights)
  - `brand-lock-extractor/SKILL.md:82` [FORBID] — - All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion languag
  - `brand-lock-extractor/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `image/SKILL.md:56` [PROCESS] — - Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
  - `image/references/models.md:50` [PROCESS] — | Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/text-rendering.md:133` [RECOMMEND] — Describe typography style or name the font directly:
  - `produccion-visual-sw30/SKILL.md:132` [GATE] — 10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los cuerpos nunca tapan logo ni lettering en frames congelados.
  - `storyboard-architect/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `storyboard-architect/references/beat-frameworks.md:45` [RECOMMEND] — Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/on-screen-text.md:71` [REQUIRE] — Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the br
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 1 · personas · grupo → text.mode = `composite` (texto compuesto después) — 7 reglas

  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:105` [FORBID] — - **Don't include text content in image prompts**, composite separately; text rendering is mediocre
  - `visual-prompt-forge/adapters/nano-banana.md:83` [PROCESS] — 4. Composite text on the chosen variant
  - `visual-prompt-forge/adapters/seedream.md:82` [FORBID] — - **Don't include text content**, text rendering is poor; composite separately
  - `visual-prompt-forge/references/failure-modes.md:53` [FORBID] — - The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.

##### 1 · personas · grupo → generator.family = `nano_banana` (Nano Banana / Pro) — 39 reglas

  - `image/SKILL.md:100` [REQUIRE] — For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:40` [FORBID] — - **Nano Banana** → [nano-banana.md](references/nano-banana.md) Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mo
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:78` [REQUIRE] — - **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
  - `image/references/models.md:10` [PROCESS] — | Сложная сцена с физикой/композицией | **Nano Banana Pro** |
  - `image/references/models.md:11` [PROCESS] — | Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
  - `image/references/models.md:12` [PROCESS] — | Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
  - `image/references/models.md:17` [PROCESS] — | Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:9` [PROCESS] — | Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/nano-banana.md:55` [RECOMMEND] — Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены пл
  - `image/references/patterns/ecommerce.md:114` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for believable physical distortion
  - `image/references/patterns/fashion-editorial.md:107` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/food-beverage.md:110` [RECOMMEND] — **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
  - `image/references/patterns/food-beverage.md:124` [RECOMMEND] — **Recommended model:** NB2 — image grounding for real city landmarks + illustration style
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/portrait-cinema.md:97` [RECOMMEND] — **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)
  - `image/references/patterns/poster-illustration.md:117` [RECOMMEND] — **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species
  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
  - `image/references/prompt-framework.md:43` [REQUIRE] — > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
  - `image/references/prompt-framework.md:87` [PROCESS] — **3. Exclusions** - что исключить (опционально): > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:109` [FORBID] — That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the build when an adapter advertises more words than its ceiling
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/nano-banana.md:101` [FORBID] — - **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
  - `visual-prompt-forge/adapters/nano-banana.md:102` [FORBID] — - **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
  - `visual-prompt-forge/adapters/nano-banana.md:104` [REQUIRE] — - **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:81` [PROCESS] — 2. Feed that image to Nano Banana with variation prompts
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/failure-modes.md:129` [RECOMMEND] — 2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-prod

##### 1 · personas · grupo → generator.family = `gpt_image` (GPT Image 2) — 65 reglas

  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:43` [REQUIRE] — - **GPT Image 2** → [gpt-image.md](references/gpt-image.md) 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop 
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:74` [REQUIRE] — > **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.
  - `image/references/golden-rules.md:93` [REQUIRE] — Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.
  - `image/references/gpt-image.md:117` [RECOMMEND] — GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не распи
  - `image/references/models.md:13` [PROCESS] — | Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
  - `image/references/models.md:14` [PROCESS] — | Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
  - `image/references/models.md:15` [PROCESS] — | Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
  - `image/references/models.md:16` [PROCESS] — | Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
  - `image/references/models.md:18` [PROCESS] — | Storyboard с фокусом на типографике | **GPT Image 2** |
  - `image/references/models.md:19` [PROCESS] — | Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:26` [REQUIRE] — - **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
  - `image/references/multi-panel.md:122` [RECOMMEND] — **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych) **Model:** GPT Image 2 `quality: medium` — if text overlay need
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:294` [REQUIRE] — **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space) **Model:** GPT Image 2 `quality: high` (text-heavy — scene number
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/patterns/character-design.md:108` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
  - `image/references/patterns/character-design.md:140` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering
  - `image/references/patterns/character-design.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
  - `image/references/patterns/character-design.md:3` [RECOMMEND] — Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}`
  - `image/references/patterns/character-design.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
  - `image/references/patterns/character-design.md:80` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
  - `image/references/patterns/ecommerce.md:74` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
  - `image/references/patterns/ecommerce.md:94` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
  - `image/references/patterns/fashion-editorial.md:27` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
  - `image/references/patterns/fashion-editorial.md:73` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:35` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
  - `image/references/patterns/food-beverage.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
  - `image/references/patterns/food-beverage.md:96` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
  - `image/references/patterns/portrait-cinema.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `image/references/patterns/portrait-cinema.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
  - `image/references/patterns/portrait-cinema.md:63` [RECOMMEND] — **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:3` [RECOMMEND] — Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. De
  - `image/references/patterns/poster-illustration.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
  - `image/references/patterns/poster-illustration.md:82` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
  - `image/references/patterns/ui-social.md:104` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements requir
  - `image/references/patterns/ui-social.md:135` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout
  - `image/references/patterns/ui-social.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
  - `image/references/patterns/ui-social.md:3` [RECOMMEND] — Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for c
  - `image/references/patterns/ui-social.md:49` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
  - `image/references/patterns/ui-social.md:75` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/gpt-image.md:38` [RECOMMEND] — GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:86` [FORBID] — - **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
  - `visual-prompt-forge/adapters/gpt-image.md:89` [FORBID] — - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:87` [RECOMMEND] — - For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 1 · personas · grupo → generator.family = `midjourney` (Midjourney) — 14 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:18` [PROCESS] — - Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
  - `visual-prompt-forge/SKILL.md:295` [REQUIRE] — If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. T
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/consistency-locks.md:64` [RECOMMEND] — For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
  - `visual-prompt-forge/references/failure-modes.md:39` [RECOMMEND] — - For Midjourney, use `--cref` with `--cw 50`

##### 1 · personas · grupo → generator.family = `flux` (Flux) — 17 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-asset-critic/SKILL.md:102` [REQUIRE] — **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts: > "Hands are mangled. This is a known Fl
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/flux.md:66` [REQUIRE] — The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.
  - `visual-prompt-forge/adapters/flux.md:86` [RECOMMEND] — Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.
  - `visual-prompt-forge/adapters/flux.md:90` [FORBID] — - **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
  - `visual-prompt-forge/adapters/flux.md:91` [FORBID] — - **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:69` [RECOMMEND] — **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

##### 1 · personas · grupo → generator.family = `ideogram` (Ideogram) — 15 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:257` [REQUIRE] — If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:30` [REQUIRE] — The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/ideogram.md:92` [FORBID] — - **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
  - `visual-prompt-forge/adapters/ideogram.md:93` [FORBID] — - **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/failure-modes.md:54` [REQUIRE] — - If text must be in-image (poster work), use Ideogram v3 with explicit override flag
  - `visual-prompt-forge/references/failure-modes.md:56` [RECOMMEND] — - Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
  - `visual-prompt-forge/references/prompt-anatomy.md:58` [FORBID] — **What:** on-screen text composited after generation. **Source:** `text-overlays.json`. **Never appears in image prompts** (except Ideogram Mode 2 wit
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 1 · personas · grupo → generator.family = `seedream` (Seedream) — 3 reglas

  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/seedream.md:80` [FORBID] — - **Don't write paragraphs**. Seedream wants comma-separated phrases
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output

### SIN PERSONAS — 5 reglas propias

  - `brand-lock-extractor/references/extraction-rubric.md:59` [FORBID] — - Imagery: no stock-photo gloss? no people? no gradients? no clip-art icons? Each absence is a never.
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:57` [PROCESS] — - Edit existing image (object removal, lighting swap, colorization, restoration, localization) → [editing.md](references/editing.md)
  - `image/references/gpt-image.md:96` [FORBID] — **Object removal:** «Remove [X]. Do not change anything else. Use `input_fidelity: high` to maintain surrounding context» (только gpt-image-1.5/1, в g
  - `image/references/gpt-image.md:98` [RECOMMEND] — **Lighting/weather swap:** «Change ONLY environmental conditions: lighting direction/quality, shadows, atmosphere, precipitation. Preserve identity, g

#### 1 · sin personas → scene.category = `exterior` (exterior) — 3 reglas

  - `brand-lock-extractor/brand-packs/_template.md:15` [RECOMMEND] — Every hex value here is allowed. Anything outside this list is not.
  - `learned/production-learnings.v3.2.json:11` [REQUIRE] — Once an image is accepted and requested changes are local, perform a surgical image edit and preserve the approved pixels/locks outside the requested 
  - `learned/production-learnings.v3.4.json:4` [REQUIRE] — Prompt revisions may not be freely rewritten. Re-render the same immutable Prompt AST against the updated frozen brief; any AST/model/parameter/templa

#### 1 · sin personas → scene.category = `interior` (interior) — 13 reglas

  - `image/references/patterns/ui-social.md:55` [RECOMMEND] — Use to create a polished App Store or Google Play listing screenshot — device frame with app UI inside, feature headline, and clean gradient backgroun
  - `image/references/prompt-framework.md:215` [RECOMMEND] — 4. **Specular behavior** — "specular highlights on metal edges of watch, caustic reflections dancing inside glass bottle, wet surface sheen on cobbles
  - `storyboard-architect/SKILL.md:255` [GATE] — - every overlay's timing sits inside its shot window, and exit is after enter
  - `storyboard-architect/SKILL.md:259` [GATE] — It warns, rather than fails, on judgement calls worth a second look: overlay copy repeated inside a shot subject, a raw hex in a subject, shot ids out
  - `visual-asset-critic/SKILL.md:232` [FORBID] — If the brief was "founder at laptop, calm mood" and the generation delivered exactly that, don't note that "the room could be more visually interestin
  - `visual-prompt-forge/SKILL.md:104` [REQUIRE] — `max_prompt_words` is a ceiling. The range in an adapter `.md` is the recommended target and always sits inside that ceiling, so a `.md` saying "40 to
  - `visual-prompt-forge/adapters/flux.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/gpt-image.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/ideogram.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/nano-banana.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/seedream.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `

#### 1 · sin personas → scene.category = `animales` (animales / fauna) — 1 reglas

  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 

#### 1 · sin personas → scene.category = `arquitectonica` (arquitectónica / inmobiliaria) — 1 reglas

  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency

#### 1 · sin personas → scene.category = `paisaje_natural` (paisaje natural) — 4 reglas

  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa

#### 1 · sin personas → scene.category = `producto_objeto` (producto u objeto) — 21 reglas

  - `image/SKILL.md:57` [PROCESS] — - Edit existing image (object removal, lighting swap, colorization, restoration, localization) → [editing.md](references/editing.md)
  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)
  - `image/references/gpt-image.md:96` [FORBID] — **Object removal:** «Remove [X]. Do not change anything else. Use `input_fidelity: high` to maintain surrounding context» (только gpt-image-1.5/1, в g
  - `image/references/gpt-image.md:98` [RECOMMEND] — **Lighting/weather swap:** «Change ONLY environmental conditions: lighting direction/quality, shadows, atmosphere, precipitation. Preserve identity, g
  - `image/references/models.md:39` [PROCESS] — - Product shots на нейтральном фоне.
  - `image/references/multi-panel.md:216` [RECOMMEND] — **When to use:** Product transformation, makeover, time comparison, renovation — two states side by side.
  - `image/references/patterns/ecommerce.md:100` [RECOMMEND] — Use for disruptive, scroll-stopping social ads where the product packaging appears squeezed, inflated, or physically distorted as if made of soft rubb
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:29` [RECOMMEND] — Use for premium beauty or fragrance product photography — dark, moody, tactile surfaces with atmospheric effects.
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:51` [RECOMMEND] — Use to present a product commercial shot breakdown in a single image — pitch decks, creative presentations, client approvals.
  - `image/references/patterns/ecommerce.md:9` [RECOMMEND] — Use when you need a playful, attention-grabbing product visual where tiny workers interact with an oversized product — ideal for social media ads and 
  - `image/references/patterns/food-beverage.md:41` [RECOMMEND] — Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `image/references/patterns/ui-social.md:29` [RECOMMEND] — Use for square-format posts on Instagram or Facebook — quote cards, feature announcements, or product highlights with centered layout.
  - `image/references/patterns/ui-social.md:9` [RECOMMEND] — Use for vertical product or brand ads targeting Instagram Stories — hero product, bold headline, and swipe-up CTA zone at the bottom.
  - `storyboard-architect/references/beat-frameworks.md:20` [RECOMMEND] — Default for product films and brand films. Three beats:
  - `storyboard-architect/references/beat-frameworks.md:23` [RECOMMEND] — 2. **Hero**, the product/founder/methodology arrives. Show what it does, not what it is.
  - `storyboard-architect/references/beat-frameworks.md:29` [RECOMMEND] — Use when: product launches, brand films, anchor pieces.
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/shot-grammar.md:17` [RECOMMEND] — Default to MCU and MS for talking-head founder content. ECU and CU for product detail and emotion. WS and EWS for context-setting.

#### 1 · sin personas → scene.category = `urbana` (urbana / cityscape) — 2 reglas

  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 

#### 1 · sin personas → style.photography = `editorial` (editorial) — 11 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 
  - `visual-asset-critic/SKILL.md:20` [PROCESS] — - Has a generated image and just wants editorial feedback (no storyboard reference)
  - `visual-asset-critic/SKILL.md:8` [FORBID] — You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structu
  - `visual-prompt-forge/adapters/nano-banana.md:82` [PROCESS] — 3. Get 4–8 variants of the same shot for editorial selection
  - `visual-prompt-forge/references/consistency-locks.md:109` [FORBID] — Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.
  - `visual-prompt-forge/references/failure-modes.md:130` [RECOMMEND] — 3. The image is 80% right and the gap is editorial → ship to post and let the editor finish
  - `visual-prompt-forge/references/failure-modes.md:3` [FORBID] — What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

#### 1 · sin personas → style.photography = `documental` (documental / fotoperiodismo) — 1 reglas

  - `produccion-visual-sw30/SKILL.md:73` [GATE] — | usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO

#### 1 · sin personas → style.photography = `natgeo` (documental de naturaleza (National Geographic)) — **0 reglas · RAMA VACÍA**

#### 1 · sin personas → style.photography = `moda` (moda) — 5 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

#### 1 · sin personas → style.photography = `producto` (producto / e-commerce) — 1 reglas

  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)

#### 1 · sin personas → style.photography = `cinematografico` (cinematográfico) — 8 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:67` [RECOMMEND] — The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site 
  - `image/SKILL.md:69` [PROCESS] — - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - `image/SKILL.md:80` [PROCESS] — Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / stand
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/nano-banana.md:25` [RECOMMEND] — - Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `visual-asset-critic/references/critique-rubric.md:107` [FORBID] — - **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
  - `visual-prompt-forge/references/consistency-locks.md:96` [REQUIRE] — The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal s

#### 1 · sin personas → style.photography = `vintage` (vintage / analógico) — 6 reglas

  - `image/SKILL.md:76` [PROCESS] — Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise 
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `visual-prompt-forge/references/consistency-locks.md:74` [RECOMMEND] — When the storyboard has a distinctive visual style (specific film stock, specific lighting school, specific color theory), use a style reference image
  - `visual-prompt-forge/references/failure-modes.md:17` [RECOMMEND] — - Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")

#### 1 · sin personas → style.photography = `calle` (fotografía de calle) — **0 reglas · RAMA VACÍA**

#### 1 · sin personas → style.photography = `movil` (móvil / snapshot) — 3 reglas

  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `storyboard-html-preview/SKILL.md:238` [RECOMMEND] — Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
  - `storyboard-html-preview/SKILL.md:255` [GATE] — - [ ] Mobile viewport (375px) renders without horizontal scroll

#### 1 · sin personas → style.photography = `bellas_artes` (bellas artes / conceptual) — **0 reglas · RAMA VACÍA**

#### 1 · sin personas → style.photography = `estudio` (retrato de estudio) — **0 reglas · RAMA VACÍA**

#### 1 · sin personas → text.mode = `none` (sin texto) — **0 reglas · RAMA VACÍA**

#### 1 · sin personas → text.mode = `in_image` (texto dentro de la imagen) — 14 reglas

  - `brand-lock-extractor/SKILL.md:54` [PROCESS] — 3. **Typography** (display, body, optional mono, with weights)
  - `brand-lock-extractor/SKILL.md:82` [FORBID] — - All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion languag
  - `brand-lock-extractor/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `image/SKILL.md:56` [PROCESS] — - Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
  - `image/references/models.md:50` [PROCESS] — | Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/text-rendering.md:133` [RECOMMEND] — Describe typography style or name the font directly:
  - `produccion-visual-sw30/SKILL.md:132` [GATE] — 10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los cuerpos nunca tapan logo ni lettering en frames congelados.
  - `storyboard-architect/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `storyboard-architect/references/beat-frameworks.md:45` [RECOMMEND] — Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/on-screen-text.md:71` [REQUIRE] — Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the br
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

#### 1 · sin personas → text.mode = `composite` (texto compuesto después) — 7 reglas

  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:105` [FORBID] — - **Don't include text content in image prompts**, composite separately; text rendering is mediocre
  - `visual-prompt-forge/adapters/nano-banana.md:83` [PROCESS] — 4. Composite text on the chosen variant
  - `visual-prompt-forge/adapters/seedream.md:82` [FORBID] — - **Don't include text content**, text rendering is poor; composite separately
  - `visual-prompt-forge/references/failure-modes.md:53` [FORBID] — - The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.

#### 1 · sin personas → generator.family = `nano_banana` (Nano Banana / Pro) — 35 reglas

  - `image/SKILL.md:100` [REQUIRE] — For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:40` [FORBID] — - **Nano Banana** → [nano-banana.md](references/nano-banana.md) Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mo
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:78` [REQUIRE] — - **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
  - `image/references/models.md:10` [PROCESS] — | Сложная сцена с физикой/композицией | **Nano Banana Pro** |
  - `image/references/models.md:11` [PROCESS] — | Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
  - `image/references/models.md:12` [PROCESS] — | Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
  - `image/references/models.md:17` [PROCESS] — | Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:9` [PROCESS] — | Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/nano-banana.md:55` [RECOMMEND] — Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены пл
  - `image/references/patterns/ecommerce.md:114` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for believable physical distortion
  - `image/references/patterns/fashion-editorial.md:107` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/food-beverage.md:110` [RECOMMEND] — **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
  - `image/references/patterns/food-beverage.md:124` [RECOMMEND] — **Recommended model:** NB2 — image grounding for real city landmarks + illustration style
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
  - `image/references/prompt-framework.md:43` [REQUIRE] — > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
  - `image/references/prompt-framework.md:87` [PROCESS] — **3. Exclusions** - что исключить (опционально): > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
  - `visual-prompt-forge/SKILL.md:109` [FORBID] — That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the build when an adapter advertises more words than its ceiling
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/nano-banana.md:101` [FORBID] — - **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
  - `visual-prompt-forge/adapters/nano-banana.md:102` [FORBID] — - **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
  - `visual-prompt-forge/adapters/nano-banana.md:104` [REQUIRE] — - **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:81` [PROCESS] — 2. Feed that image to Nano Banana with variation prompts
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/failure-modes.md:129` [RECOMMEND] — 2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-prod

#### 1 · sin personas → generator.family = `gpt_image` (GPT Image 2) — 59 reglas

  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:43` [REQUIRE] — - **GPT Image 2** → [gpt-image.md](references/gpt-image.md) 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop 
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:74` [REQUIRE] — > **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.
  - `image/references/golden-rules.md:93` [REQUIRE] — Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.
  - `image/references/gpt-image.md:117` [RECOMMEND] — GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не распи
  - `image/references/models.md:13` [PROCESS] — | Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
  - `image/references/models.md:14` [PROCESS] — | Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
  - `image/references/models.md:15` [PROCESS] — | Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
  - `image/references/models.md:16` [PROCESS] — | Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
  - `image/references/models.md:18` [PROCESS] — | Storyboard с фокусом на типографике | **GPT Image 2** |
  - `image/references/models.md:19` [PROCESS] — | Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:26` [REQUIRE] — - **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
  - `image/references/multi-panel.md:122` [RECOMMEND] — **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych) **Model:** GPT Image 2 `quality: medium` — if text overlay need
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa
  - `image/references/patterns/character-design.md:108` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
  - `image/references/patterns/character-design.md:140` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering
  - `image/references/patterns/character-design.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
  - `image/references/patterns/character-design.md:3` [RECOMMEND] — Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}`
  - `image/references/patterns/character-design.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
  - `image/references/patterns/character-design.md:80` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
  - `image/references/patterns/ecommerce.md:74` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
  - `image/references/patterns/ecommerce.md:94` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
  - `image/references/patterns/fashion-editorial.md:27` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
  - `image/references/patterns/fashion-editorial.md:73` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:35` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
  - `image/references/patterns/food-beverage.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
  - `image/references/patterns/food-beverage.md:96` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `image/references/patterns/portrait-cinema.md:63` [RECOMMEND] — **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:3` [RECOMMEND] — Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. De
  - `image/references/patterns/poster-illustration.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
  - `image/references/patterns/poster-illustration.md:82` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
  - `image/references/patterns/ui-social.md:104` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements requir
  - `image/references/patterns/ui-social.md:135` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout
  - `image/references/patterns/ui-social.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
  - `image/references/patterns/ui-social.md:3` [RECOMMEND] — Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for c
  - `image/references/patterns/ui-social.md:49` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
  - `image/references/patterns/ui-social.md:75` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/gpt-image.md:38` [RECOMMEND] — GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:86` [FORBID] — - **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
  - `visual-prompt-forge/adapters/gpt-image.md:89` [FORBID] — - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
  - `visual-prompt-forge/references/failure-modes.md:87` [RECOMMEND] — - For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

#### 1 · sin personas → generator.family = `midjourney` (Midjourney) — 14 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:18` [PROCESS] — - Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
  - `visual-prompt-forge/SKILL.md:295` [REQUIRE] — If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. T
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/consistency-locks.md:64` [RECOMMEND] — For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
  - `visual-prompt-forge/references/failure-modes.md:39` [RECOMMEND] — - For Midjourney, use `--cref` with `--cw 50`

#### 1 · sin personas → generator.family = `flux` (Flux) — 13 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/flux.md:86` [RECOMMEND] — Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.
  - `visual-prompt-forge/adapters/flux.md:90` [FORBID] — - **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
  - `visual-prompt-forge/adapters/flux.md:91` [FORBID] — - **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:69` [RECOMMEND] — **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

#### 1 · sin personas → generator.family = `ideogram` (Ideogram) — 15 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:257` [REQUIRE] — If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:30` [REQUIRE] — The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/ideogram.md:92` [FORBID] — - **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
  - `visual-prompt-forge/adapters/ideogram.md:93` [FORBID] — - **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
  - `visual-prompt-forge/references/consistency-locks.md:56` [RECOMMEND] — For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.
  - `visual-prompt-forge/references/failure-modes.md:54` [REQUIRE] — - If text must be in-image (poster work), use Ideogram v3 with explicit override flag
  - `visual-prompt-forge/references/failure-modes.md:56` [RECOMMEND] — - Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
  - `visual-prompt-forge/references/prompt-anatomy.md:58` [FORBID] — **What:** on-screen text composited after generation. **Source:** `text-overlays.json`. **Never appears in image prompts** (except Ideogram Mode 2 wit
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

#### 1 · sin personas → generator.family = `seedream` (Seedream) — 3 reglas

  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/seedream.md:80` [FORBID] — - **Don't write paragraphs**. Seedream wants comma-separated phrases
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output

## ANCLA CON 2 O MÁS REFERENCIAS (`references.count = 2+`) — 12 reglas propias

  - `ai-production-director/SKILL.md:90` [GATE] — - **Gate:** `tools/validate_shots.py` limpio + six-point dramaturgy check + auditoría de 3 detalles por shot (presión ambiental, micro-acción física, 
  - `image/references/golden-rules.md:136` [REQUIRE] — GPT Image 2 обладает глубокими знаниями о культуре, эпохах и визуальных стилях. Вместо описания каждой детали — дай модели культурный/временной/жанров
  - `image/references/golden-rules.md:158` [REQUIRE] — 1. **Используй как HIGH-LEVEL steering** — якорь задаёт настроение и эстетику, а не заменяет весь промпт
  - `image/references/golden-rules.md:159` [REQUIRE] — 2. **Комбинируй с конкретными визуальными деталями** — якорь устанавливает мир, детали устанавливают специфику
  - `image/references/golden-rules.md:79` [REQUIRE] — - **GPT Image 2:** прогон на `quality: low` → отбор → переген на `medium` или `high`.
  - `produccion-visual-sw30/SKILL.md:118` [GATE] — 2. Posición SIEMPRE por ancla legible de la propia imagen (letterforms del mundo: "his back level with the letter L of WORLD"). Prohibido "left half",
  - `visual-asset-critic/SKILL.md:228` [REQUIRE] — "Change the prompt" is not a fix. "Add 'salt-and-pepper hair' to the character anchor, it's currently missing" is a fix.
  - `visual-prompt-forge/SKILL.md:354` [GATE] — - **Rule 3**: `environment`, `lighting`, and `color_grade` appear verbatim, with the character anchor as a warning
  - `visual-prompt-forge/adapters/midjourney.md:24` [RECOMMEND] — | `--cref` | image URL | use when character anchor exists | Character reference. Pair with `--cw` |
  - `visual-prompt-forge/adapters/midjourney.md:26` [RECOMMEND] — | `--sref` | image URL | use when style anchor exists | Style reference |
  - `visual-prompt-forge/adapters/seedream.md:74` [REQUIRE] — - **Verbatim repeat** the character anchor string from series_lock in every prompt
  - `visual-prompt-forge/references/consistency-locks.md:62` [REQUIRE] — 3. Each subsequent prompt has the verbatim character anchor PLUS the reference image link

### CON PERSONAS — 73 reglas propias

  - `ai-production-director/SKILL.md:52` [PROCESS] — | Narrativa | Un beat (hook→payoff) | Arco simple | Multi-escena, personajes |
  - `aurora-prompt-linter/SKILL.md:158` [RECOMMEND] — - **Sub-tags por categoría**: O.upper / O.lower / P.face / P.body no soportados — un ref tagueado como O cubre todo outfit. Si el ref solo muestra el 
  - `aurora-prompt-linter/references/README.md:97` [RECOMMEND] — 6. **Exenciones**: términos en contexto de motion/cámara o como anchor direccional (`away from her face`, `across the climbing wall`) NO se flaggean.
  - `brand-lock-extractor/SKILL.md:20` [PROCESS] — - Hands over a URL, a PDF, image files, or a written brand description and asks for a brand-lock
  - `brand-lock-extractor/references/extraction-rubric.md:59` [FORBID] — - Imagery: no stock-photo gloss? no people? no gradients? no clip-art icons? Each absence is a never.
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:64` [PROCESS] — - **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 
  - `image/references/creative-direction.md:34` [REQUIRE] — - Hasselblad — medium format, shallow DOF, fashion/portrait
  - `image/references/creative-direction.md:47` [RECOMMEND] — - "Waist-up portrait", "full body", "over-the-shoulder"
  - `image/references/golden-rules.md:16` [REQUIRE] — - ✅ "solo portrait" → ❌ "no other people"
  - `image/references/gpt-image.md:94` [RECOMMEND] — **Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows s
  - `image/references/multi-panel.md:210` [REQUIRE] — - Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
  - `image/references/multi-panel.md:294` [REQUIRE] — **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space) **Model:** GPT Image 2 `quality: high` (text-heavy — scene number
  - `image/references/multi-panel.md:308` [REQUIRE] — **Subject consistency:** Always include an explicit instruction: "same person / same character / same product across all panels." Repeat key identity 
  - `image/references/multi-panel.md:57` [RECOMMEND] — **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/patterns/character-design.md:106` [RECOMMEND] — **Key levers:** `{character_name}`, `{character_description_simplified}` (key outfit and hair only), `{face_markers}` (e.g. round glasses, scar on lef
  - `image/references/patterns/character-design.md:120` [RECOMMEND] — Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional con
  - `image/references/patterns/character-design.md:29` [RECOMMEND] — Use to produce a grid of 6–9 facial expressions for the same character — consistent head angle and art style, with emotion labels under each face.
  - `image/references/patterns/character-design.md:58` [RECOMMEND] — Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
  - `image/references/patterns/fashion-editorial.md:33` [RECOMMEND] — Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
  - `image/references/patterns/portrait-cinema.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/patterns/portrait-cinema.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
  - `image/references/patterns/portrait-cinema.md:61` [RECOMMEND] — **Key levers:** `{person_description}`, `{direction}` (left, right), `{hair_detail}` (tight buzz cut showing skull contour, shoulder-length hair with 
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:83` [RECOMMEND] — Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elem
  - `image/references/patterns/portrait-cinema.md:9` [RECOMMEND] — Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
  - `image/references/patterns/portrait-cinema.md:97` [RECOMMEND] — **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)
  - `image/references/patterns/poster-illustration.md:117` [RECOMMEND] — **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/patterns/ui-social.md:116` [RECOMMEND] — Use to create a visual color analysis graphic from a portrait — seasonal palette classification, clothing color comparisons, and accessory recommendat
  - `image/references/patterns/ui-social.md:133` [REQUIRE] — **Key levers:** `{subject_description}` (age, skin tone, hair color, eye color — needed for accurate seasonal analysis), `{season_type}` (Warm Spring,
  - `image/references/prompt-framework.md:213` [RECOMMEND] — 2. **Micro-textures** — "visible pores on skin, individual hair strands catching backlight, fabric weave pattern on linen shirt, grain of weathered wo
  - `image/references/prompt-framework.md:218` [RECOMMEND] — 7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby si
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"
  - `image/references/vision-decomposer.md:36` [PROCESS] — - **Figure & ground (Arnheim):** degree of subject isolation, overlapping of forms, mass relationships. Use of reflections (mirrors, windows) to expan
  - `image/references/vision-decomposer.md:44` [PROCESS] — - **Broken light & reflexes (Zheleznyakov):** use of shadow masks (gobos), light through blinds / foliage, color reflexes from neighboring objects ont
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `learned/production-learnings.v3.2.json:3` [REQUIRE] — Preserve a sufficiently specific domain-native pose/technique label instead of expanding it into speculative anatomy. Expand only when the target adap
  - `learned/production-learnings.v3.2.json:8` [RECOMMEND] — For complex underwater human anatomy, physically justified bubbles/turbulence may obscure non-critical anatomical detail when the brief does not requi
  - `produccion-visual-sw30/SKILL.md:116` [GATE] — 1. Un solo trabajo por generación. Con dos personajes: un sujeto por generación, o técnica de colocación probada; nunca "a ver si sale".
  - `produccion-visual-sw30/SKILL.md:123` [GATE] — 5. Herencia mínima: "same face and clothes" + solo los deltas. Cero re-descripción de lo que la referencia ya muestra.
  - `produccion-visual-sw30/SKILL.md:130` [GATE] — 9. Contactos entre personas: "a natural high five" — la anatomía la fija el keyframe aprobado, nunca la asignación de manos por texto.
  - `produccion-visual-sw30/SKILL.md:35` [GATE] — 1. **CATALOGAR** — identificar el TIPO de prompt y leer qué reglas aplican a ese tipo en la matriz (production-package/RULES_MATRIX.md: 26 reglas × 5 
  - `produccion-visual-sw30/SKILL.md:39` [GATE] — 2. **DEFINIR SECCIONES** — antes de redactar, listar las secciones que ese tipo exige. Cada regla vive en UN bloque nombrado y compartido (optics_*, s
  - `storyboard-architect/SKILL.md:18` [PROCESS] — - Hands over a script, brief, or concept document expecting structured pre-production output
  - `storyboard-architect/SKILL.md:266` [GATE] — - [ ] `series_lock` anchors are specific enough to reproduce (not "a person in a room")
  - `storyboard-architect/references/beat-frameworks.md:33` [RECOMMEND] — Default for personal-brand video where a person speaks to camera. Five micro-beats:
  - `storyboard-architect/references/beat-frameworks.md:41` [RECOMMEND] — Use when: founder content, thought leadership, personal-brand pieces.
  - `storyboard-html-preview/SKILL.md:19` [PROCESS] — - Hands off `storyboard.md` + `shots.json` + asks for a deliverable for review
  - `visual-asset-critic/SKILL.md:102` [REQUIRE] — **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts: > "Hands are mangled. This is a known Fl
  - `visual-asset-critic/SKILL.md:224` [REQUIRE] — "Looks great" / "feels off" without specifics is not a critique. Every observation must reference something in the image (composition, color, anatomy,
  - `visual-asset-critic/SKILL.md:228` [REQUIRE] — "Change the prompt" is not a fix. "Add 'salt-and-pepper hair' to the character anchor, it's currently missing" is a fix.
  - `visual-asset-critic/SKILL.md:236` [FORBID] — Some failures (mangled hands, weird eye reflections, jewelry shimmer) are known generator weaknesses. Surface them as such, don't pretend a different 
  - `visual-asset-critic/SKILL.md:24` [GATE] — **Two artifacts from every review, always both:** a human-readable markdown critique (the primary surface) and a machine-readable critique JSON (so a 
  - `visual-asset-critic/SKILL.md:87` [PROCESS] — 5. **Technical**, skin texture, hands, eyes, anatomy, AI artifacts?
  - `visual-asset-critic/SKILL.md:96` [REQUIRE] — **Prompt-level fix**, change the prompt and re-roll. Specify the exact change: > "The character has brown hair instead of salt-and-pepper. Add 'salt-a
  - `visual-asset-critic/references/critique-rubric.md:111` [REQUIRE] — - **Distinguish prompt failure from generator failure**, if the prompt was fine and the generator produced garbage hands, that's "re-roll required", n
  - `visual-prompt-forge/SKILL.md:16` [PROCESS] — - Hands over a `shots.json` (or any structured shot list) and asks for prompts
  - `visual-prompt-forge/SKILL.md:186` [FORBID] — This is what `visual-asset-critic`'s structured output is for. When the user hands you `shots.json` plus one or more `critique.json` files (the machin
  - `visual-prompt-forge/SKILL.md:190` [RECOMMEND] — The user says "apply the critique", "revise the failed shots", "re-roll what didn't pass", or hands over an output tree containing `critiques/`.
  - `visual-prompt-forge/SKILL.md:215` [PROCESS] — 6. Re-apply the five-layer anatomy and the same adapter as the original run.
  - `visual-prompt-forge/SKILL.md:281` [REQUIRE] — `character` is a warning rather than an error, because a shot with no person in it can legitimately leave it out. When the shot has a person, it is ve
  - `visual-prompt-forge/SKILL.md:305` [REQUIRE] — - **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no
  - `visual-prompt-forge/adapters/flux.md:66` [REQUIRE] — The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.
  - `visual-prompt-forge/adapters/gpt-image.md:46` [RECOMMEND] — - "The subject's shoulders are angled 30 degrees toward the camera, face turned to look at the off-frame light source."
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/references/consistency-locks.md:113` [FORBID] — A few things people try that don't actually fix consistency:
  - `visual-prompt-forge/references/consistency-locks.md:115` [FORBID] — - **Adding "consistent character" or "same person" to the prompt**, generators don't read meta-instructions
  - `visual-prompt-forge/references/consistency-locks.md:70` [RECOMMEND] — **This is the most effective lock for character consistency** in 2026. Use it whenever the storyboard features the same person across multiple shots.
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)

#### UNA PERSONA — 1 reglas propias

  - `produccion-visual-sw30/SKILL.md:116` [GATE] — 1. Un solo trabajo por generación. Con dos personajes: un sujeto por generación, o técnica de colocación probada; nunca "a ver si sale".

##### 2+ · personas · 1 → style.photography = `editorial` (editorial) — 16 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/multi-panel.md:57` [RECOMMEND] — **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:33` [RECOMMEND] — Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:9` [RECOMMEND] — Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 
  - `visual-asset-critic/SKILL.md:20` [PROCESS] — - Has a generated image and just wants editorial feedback (no storyboard reference)
  - `visual-asset-critic/SKILL.md:8` [FORBID] — You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structu
  - `visual-prompt-forge/adapters/nano-banana.md:82` [PROCESS] — 3. Get 4–8 variants of the same shot for editorial selection
  - `visual-prompt-forge/references/consistency-locks.md:109` [FORBID] — Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.
  - `visual-prompt-forge/references/failure-modes.md:130` [RECOMMEND] — 3. The image is 80% right and the gap is editorial → ship to post and let the editor finish
  - `visual-prompt-forge/references/failure-modes.md:3` [FORBID] — What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

##### 2+ · personas · 1 → style.photography = `documental` (documental / fotoperiodismo) — 1 reglas

  - `produccion-visual-sw30/SKILL.md:73` [GATE] — | usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO

##### 2+ · personas · 1 → style.photography = `natgeo` (documental de naturaleza (National Geographic)) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → style.photography = `moda` (moda) — 8 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/creative-direction.md:34` [REQUIRE] — - Hasselblad — medium format, shallow DOF, fashion/portrait
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/character-design.md:58` [RECOMMEND] — Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o

##### 2+ · personas · 1 → style.photography = `producto` (producto / e-commerce) — 1 reglas

  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)

##### 2+ · personas · 1 → style.photography = `cinematografico` (cinematográfico) — 9 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:67` [RECOMMEND] — The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site 
  - `image/SKILL.md:64` [PROCESS] — - **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 
  - `image/SKILL.md:69` [PROCESS] — - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - `image/SKILL.md:80` [PROCESS] — Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / stand
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/nano-banana.md:25` [RECOMMEND] — - Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `visual-asset-critic/references/critique-rubric.md:107` [FORBID] — - **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
  - `visual-prompt-forge/references/consistency-locks.md:96` [REQUIRE] — The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal s

##### 2+ · personas · 1 → style.photography = `vintage` (vintage / analógico) — 6 reglas

  - `image/SKILL.md:76` [PROCESS] — Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise 
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `visual-prompt-forge/references/failure-modes.md:17` [RECOMMEND] — - Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")

##### 2+ · personas · 1 → style.photography = `calle` (fotografía de calle) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → style.photography = `movil` (móvil / snapshot) — 3 reglas

  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `storyboard-html-preview/SKILL.md:238` [RECOMMEND] — Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
  - `storyboard-html-preview/SKILL.md:255` [GATE] — - [ ] Mobile viewport (375px) renders without horizontal scroll

##### 2+ · personas · 1 → style.photography = `bellas_artes` (bellas artes / conceptual) — 1 reglas

  - `image/references/patterns/portrait-cinema.md:83` [RECOMMEND] — Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elem

##### 2+ · personas · 1 → style.photography = `estudio` (retrato de estudio) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → lighting.setup = `estudio` (estudio (softbox, strobe, controlada)) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → lighting.setup = `natural_exterior` (natural exterior) — 1 reglas

  - `visual-prompt-forge/adapters/flux.md:56` [RECOMMEND] — - `Sony FX6, 35mm prime, natural light only`

##### 2+ · personas · 1 → lighting.setup = `ventana` (luz entrando por ventana) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → lighting.setup = `golden_hour` (golden hour / atardecer) — 1 reglas

  - `image/references/prompt-framework.md:214` [RECOMMEND] — 3. **Atmospheric particles** — "dust motes suspended in light beam, steam wisps rising from coffee cup, pollen floating in golden hour air, fine rain 

##### 2+ · personas · 1 → lighting.setup = `artificial_nocturna` (artificial nocturna) — 3 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/prompt-framework.md:218` [RECOMMEND] — 7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby si

##### 2+ · personas · 1 → lighting.setup = `mixta` (mixta) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → composition.shot_size = `macro` (macro / detalle) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → composition.shot_size = `close_up` (close-up) — 3 reglas

  - `image/references/multi-panel.md:94` [RECOMMEND] — **When to use:** Hero shot + close-up + action for a campaign visual — horizontal or vertical triptych.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `storyboard-architect/references/shot-grammar.md:11` [RECOMMEND] — | `MCU` | Medium close-up | Head and shoulders |

##### 2+ · personas · 1 → composition.shot_size = `plano_medio` (plano medio) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → composition.shot_size = `cuerpo_completo` (cuerpo completo) — 2 reglas

  - `image/references/creative-direction.md:47` [RECOMMEND] — - "Waist-up portrait", "full body", "over-the-shoulder"
  - `image/references/patterns/character-design.md:120` [RECOMMEND] — Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional con

##### 2+ · personas · 1 → composition.shot_size = `plano_general` (plano general / amplio) — 2 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

##### 2+ · personas · 1 → task.theme = `deportiva` (deportiva) — 6 reglas

  - `aurora-prompt-linter/SKILL.md:157` [RECOMMEND] — - **Sinónimos**: "tank top" en ref + "athletic shirt" en prompt no se detecta como redundante. Roadmap v1.1: tabla de sinónimos.
  - `aurora-prompt-linter/references/README.md:96` [RECOMMEND] — 5. **Sports broadcast**: si flag activo, requiere `60fps` y `broadcast realism` en MAIN (Regla 26 v6.0).
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:93` [RECOMMEND] — Use for forward-looking athletic or techwear editorials where abstract 3D forms create a surreal spatial environment around the model.
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 

##### 2+ · personas · 1 → task.theme = `musical` (musical / concierto) — 2 reglas

  - `image/references/patterns/portrait-cinema.md:49` [RECOMMEND] — Use for edgy, tech-forward portraits — artist profiles, electronic music press, tech brand campaigns. High contrast black-and-white with selective red
  - `storyboard-architect/references/on-screen-text.md:10` [RECOMMEND] — 4. **Beat punctuation.** A single word or phrase that lands on a music hit.

##### 2+ · personas · 1 → task.theme = `moda` (moda) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → task.theme = `gastronomica` (gastronómica) — 8 reglas

  - `image/SKILL.md:68` [PROCESS] — - Food & beverage advertising → [patterns/food-beverage.md](references/patterns/food-beverage.md)
  - `image/references/patterns/ecommerce.md:80` [RECOMMEND] — Use for food, beverage, or supplement products where suspended ingredients communicate freshness, flavor, or composition.
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:41` [RECOMMEND] — Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
  - `image/references/patterns/food-beverage.md:65` [RECOMMEND] — Use for hero food posters — restaurants, delivery apps, menu boards — where the food is the entire composition with fillable content slots.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"

##### 2+ · personas · 1 → task.theme = `corporativa` (corporativa) — 3 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:52` [RECOMMEND] — Reject generic fillers ("professional, modern, clean"), they describe everything and constrain nothing. Push to contrast clauses that do work: "operat
  - `visual-prompt-forge/SKILL.md:269` [REQUIRE] — Verbatim means the whole string, unedited. Not "the same idea in better prose". The failure mode is specific and easy to walk into: you are writing fl
  - `visual-prompt-forge/SKILL.md:276` [REQUIRE] — Capitalising the first letter to start a sentence is fine, because the check is case-insensitive. "Minimalist home office, white walls, oak desk, sing

##### 2+ · personas · 1 → task.theme = `medica` (médica / científica) — 3 reglas

  - `brand-lock-extractor/SKILL.md:114` [REQUIRE] — The output is a clinical specification. It models the standards the brand-lock enforces. No emojis anywhere. No marketing adjectives about the brand i
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `learned/production-learnings.v3.2.json:11` [REQUIRE] — Once an image is accepted and requested changes are local, perform a surgical image edit and preserve the approved pixels/locks outside the requested 

##### 2+ · personas · 1 → task.theme = `viaje` (viaje / turismo) — 3 reglas

  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `visual-prompt-forge/SKILL.md:303` [REQUIRE] — - **The direction of travel.** Left to right, right to left, toward camera. Without it the generator picks, and consecutive shots stop matching.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 2+ · personas · 1 → task.theme = `automotriz` (automotriz) — 1 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo

##### 2+ · personas · 1 → task.theme = `otra` (otra) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → motion.action_complexity = `estatica` (estática) — 11 reglas

  - `brand-lock-extractor/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `storyboard-architect/SKILL.md:263` [GATE] — What the validator cannot check, and you still have to:
  - `storyboard-architect/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `visual-asset-critic/SKILL.md:170` [GATE] — The hashes are the point. Without `image_sha256`, a frame regenerated after this review still satisfies `image_ref`, and a stale ACCEPT sails through 
  - `visual-asset-critic/SKILL.md:215` [GATE] — Worked examples: `examples/critique.accept.json` and `examples/critique.revise.json` show the shape at version `1.0`, which is still valid and carries
  - `visual-prompt-forge/SKILL.md:299` [REQUIRE] — A prompt can be beautifully written and still be impossible to shoot. Every prompt declares, before anything else:
  - `visual-prompt-forge/SKILL.md:360` [GATE] — What it cannot check, and you still have to:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/references/prompt-anatomy.md:66` [RECOMMEND] — 3. **Animation.** Animated text needs After Effects / Remotion / CapCut. Static rendered text is dead-on-arrival for motion content.

##### 2+ · personas · 1 → motion.action_complexity = `pose_dirigida` (pose dirigida) — 6 reglas

  - `image/references/gpt-image.md:94` [RECOMMEND] — **Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows s
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `learned/production-learnings.v3.2.json:3` [REQUIRE] — Preserve a sufficiently specific domain-native pose/technique label instead of expanding it into speculative anatomy. Expand only when the target adap
  - `learned/production-learnings.v3.2.json:4` [REQUIRE] — A reference may control only its declared role. Features explicitly excluded from that role must not be copied into subject identity, pose, camera, fr
  - `learned/production-learnings.v3.2.json:8` [RECOMMEND] — For complex underwater human anatomy, physically justified bubbles/turbulence may obscure non-critical anatomical detail when the brief does not requi
  - `produccion-visual-sw30/SKILL.md:125` [GATE] — 6. Swap de identidad = última operación, sola: "Replace X with Y — same position, same pose, same scale".

##### 2+ · personas · 1 → motion.action_complexity = `accion_simple` (acción simple (un cuerpo)) — 5 reglas

  - `image/references/multi-panel.md:210` [REQUIRE] — - Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"
  - `learned/production-learnings.v3.2.json:10` [REQUIRE] — Do not declare a generated asset or model successful for a case before running the applicable QA. Separate deterministic/mechanical checks from semant
  - `visual-prompt-forge/SKILL.md:302` [REQUIRE] — - **The point of view.** Profile, frontal, side, rear. "A man walking" is not a shot.

##### 2+ · personas · 1 → motion.action_complexity = `accion_compleja` (acción compleja (varios cuerpos, contacto, física)) — 4 reglas

  - `image/references/prompt-framework.md:217` [RECOMMEND] — 6. **Contact shadows** — "soft contact shadow where cup meets saucer, ambient occlusion in crevices of stone wall, dark line where book spine meets ta
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:305` [REQUIRE] — - **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 2+ · personas · 1 → text.mode = `none` (sin texto) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · 1 → text.mode = `in_image` (texto dentro de la imagen) — 16 reglas

  - `brand-lock-extractor/SKILL.md:54` [PROCESS] — 3. **Typography** (display, body, optional mono, with weights)
  - `brand-lock-extractor/SKILL.md:82` [FORBID] — - All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion languag
  - `brand-lock-extractor/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `image/SKILL.md:56` [PROCESS] — - Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
  - `image/references/models.md:50` [PROCESS] — | Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/text-rendering.md:133` [RECOMMEND] — Describe typography style or name the font directly:
  - `produccion-visual-sw30/SKILL.md:132` [GATE] — 10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los cuerpos nunca tapan logo ni lettering en frames congelados.
  - `storyboard-architect/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `storyboard-architect/references/beat-frameworks.md:45` [RECOMMEND] — Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/on-screen-text.md:71` [REQUIRE] — Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the br
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 2+ · personas · 1 → text.mode = `composite` (texto compuesto después) — 7 reglas

  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:105` [FORBID] — - **Don't include text content in image prompts**, composite separately; text rendering is mediocre
  - `visual-prompt-forge/adapters/nano-banana.md:83` [PROCESS] — 4. Composite text on the chosen variant
  - `visual-prompt-forge/adapters/seedream.md:82` [FORBID] — - **Don't include text content**, text rendering is poor; composite separately
  - `visual-prompt-forge/references/failure-modes.md:53` [FORBID] — - The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.

##### 2+ · personas · 1 → generator.family = `nano_banana` (Nano Banana / Pro) — 38 reglas

  - `image/SKILL.md:100` [REQUIRE] — For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:40` [FORBID] — - **Nano Banana** → [nano-banana.md](references/nano-banana.md) Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mo
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:78` [REQUIRE] — - **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
  - `image/references/models.md:10` [PROCESS] — | Сложная сцена с физикой/композицией | **Nano Banana Pro** |
  - `image/references/models.md:11` [PROCESS] — | Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
  - `image/references/models.md:12` [PROCESS] — | Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
  - `image/references/models.md:17` [PROCESS] — | Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:9` [PROCESS] — | Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/nano-banana.md:55` [RECOMMEND] — Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены пл
  - `image/references/patterns/ecommerce.md:114` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for believable physical distortion
  - `image/references/patterns/fashion-editorial.md:107` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/food-beverage.md:110` [RECOMMEND] — **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
  - `image/references/patterns/food-beverage.md:124` [RECOMMEND] — **Recommended model:** NB2 — image grounding for real city landmarks + illustration style
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/portrait-cinema.md:97` [RECOMMEND] — **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)
  - `image/references/patterns/poster-illustration.md:117` [RECOMMEND] — **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species
  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
  - `image/references/prompt-framework.md:43` [REQUIRE] — > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
  - `image/references/prompt-framework.md:87` [PROCESS] — **3. Exclusions** - что исключить (опционально): > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:109` [FORBID] — That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the build when an adapter advertises more words than its ceiling
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/nano-banana.md:101` [FORBID] — - **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
  - `visual-prompt-forge/adapters/nano-banana.md:102` [FORBID] — - **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
  - `visual-prompt-forge/adapters/nano-banana.md:104` [REQUIRE] — - **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:81` [PROCESS] — 2. Feed that image to Nano Banana with variation prompts
  - `visual-prompt-forge/references/failure-modes.md:129` [RECOMMEND] — 2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-prod

##### 2+ · personas · 1 → generator.family = `gpt_image` (GPT Image 2) — 67 reglas

  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:43` [REQUIRE] — - **GPT Image 2** → [gpt-image.md](references/gpt-image.md) 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop 
  - `image/references/golden-rules.md:136` [REQUIRE] — GPT Image 2 обладает глубокими знаниями о культуре, эпохах и визуальных стилях. Вместо описания каждой детали — дай модели культурный/временной/жанров
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:74` [REQUIRE] — > **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.
  - `image/references/golden-rules.md:79` [REQUIRE] — - **GPT Image 2:** прогон на `quality: low` → отбор → переген на `medium` или `high`.
  - `image/references/golden-rules.md:93` [REQUIRE] — Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.
  - `image/references/gpt-image.md:117` [RECOMMEND] — GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не распи
  - `image/references/models.md:13` [PROCESS] — | Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
  - `image/references/models.md:14` [PROCESS] — | Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
  - `image/references/models.md:15` [PROCESS] — | Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
  - `image/references/models.md:16` [PROCESS] — | Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
  - `image/references/models.md:18` [PROCESS] — | Storyboard с фокусом на типографике | **GPT Image 2** |
  - `image/references/models.md:19` [PROCESS] — | Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:26` [REQUIRE] — - **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
  - `image/references/multi-panel.md:122` [RECOMMEND] — **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych) **Model:** GPT Image 2 `quality: medium` — if text overlay need
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:294` [REQUIRE] — **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space) **Model:** GPT Image 2 `quality: high` (text-heavy — scene number
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/patterns/character-design.md:108` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
  - `image/references/patterns/character-design.md:140` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering
  - `image/references/patterns/character-design.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
  - `image/references/patterns/character-design.md:3` [RECOMMEND] — Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}`
  - `image/references/patterns/character-design.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
  - `image/references/patterns/character-design.md:80` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
  - `image/references/patterns/ecommerce.md:74` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
  - `image/references/patterns/ecommerce.md:94` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
  - `image/references/patterns/fashion-editorial.md:27` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
  - `image/references/patterns/fashion-editorial.md:73` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:35` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
  - `image/references/patterns/food-beverage.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
  - `image/references/patterns/food-beverage.md:96` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
  - `image/references/patterns/portrait-cinema.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `image/references/patterns/portrait-cinema.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
  - `image/references/patterns/portrait-cinema.md:63` [RECOMMEND] — **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:3` [RECOMMEND] — Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. De
  - `image/references/patterns/poster-illustration.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
  - `image/references/patterns/poster-illustration.md:82` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
  - `image/references/patterns/ui-social.md:104` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements requir
  - `image/references/patterns/ui-social.md:135` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout
  - `image/references/patterns/ui-social.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
  - `image/references/patterns/ui-social.md:3` [RECOMMEND] — Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for c
  - `image/references/patterns/ui-social.md:49` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
  - `image/references/patterns/ui-social.md:75` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/gpt-image.md:38` [RECOMMEND] — GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:86` [FORBID] — - **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
  - `visual-prompt-forge/adapters/gpt-image.md:89` [FORBID] — - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:87` [RECOMMEND] — - For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 2+ · personas · 1 → generator.family = `midjourney` (Midjourney) — 13 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:18` [PROCESS] — - Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
  - `visual-prompt-forge/SKILL.md:295` [REQUIRE] — If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. T
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
  - `visual-prompt-forge/references/consistency-locks.md:64` [RECOMMEND] — For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
  - `visual-prompt-forge/references/failure-modes.md:39` [RECOMMEND] — - For Midjourney, use `--cref` with `--cw 50`

##### 2+ · personas · 1 → generator.family = `flux` (Flux) — 17 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-asset-critic/SKILL.md:102` [REQUIRE] — **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts: > "Hands are mangled. This is a known Fl
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/flux.md:66` [REQUIRE] — The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.
  - `visual-prompt-forge/adapters/flux.md:86` [RECOMMEND] — Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.
  - `visual-prompt-forge/adapters/flux.md:90` [FORBID] — - **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
  - `visual-prompt-forge/adapters/flux.md:91` [FORBID] — - **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:69` [RECOMMEND] — **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

##### 2+ · personas · 1 → generator.family = `ideogram` (Ideogram) — 14 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:257` [REQUIRE] — If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:30` [REQUIRE] — The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/ideogram.md:92` [FORBID] — - **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
  - `visual-prompt-forge/adapters/ideogram.md:93` [FORBID] — - **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
  - `visual-prompt-forge/references/failure-modes.md:54` [REQUIRE] — - If text must be in-image (poster work), use Ideogram v3 with explicit override flag
  - `visual-prompt-forge/references/failure-modes.md:56` [RECOMMEND] — - Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
  - `visual-prompt-forge/references/prompt-anatomy.md:58` [FORBID] — **What:** on-screen text composited after generation. **Source:** `text-overlays.json`. **Never appears in image prompts** (except Ideogram Mode 2 wit
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 2+ · personas · 1 → generator.family = `seedream` (Seedream) — 3 reglas

  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/seedream.md:80` [FORBID] — - **Don't write paragraphs**. Seedream wants comma-separated phrases
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output

#### GRUPO DE PERSONAS — 0 reglas propias


##### 2+ · personas · grupo → style.photography = `editorial` (editorial) — 16 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/multi-panel.md:57` [RECOMMEND] — **When to use:** Same person shown from 4 angles/crops in one image for an editorial or casting look.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:33` [RECOMMEND] — Use for model tests, casting cards, or editorial portfolio pages — four angles of the same person in a clean grid.
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:9` [RECOMMEND] — Use for warm, emotive street portraits with strong backlight flare — editorial, personal branding, album covers.
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 
  - `visual-asset-critic/SKILL.md:20` [PROCESS] — - Has a generated image and just wants editorial feedback (no storyboard reference)
  - `visual-asset-critic/SKILL.md:8` [FORBID] — You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structu
  - `visual-prompt-forge/adapters/nano-banana.md:82` [PROCESS] — 3. Get 4–8 variants of the same shot for editorial selection
  - `visual-prompt-forge/references/consistency-locks.md:109` [FORBID] — Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.
  - `visual-prompt-forge/references/failure-modes.md:130` [RECOMMEND] — 3. The image is 80% right and the gap is editorial → ship to post and let the editor finish
  - `visual-prompt-forge/references/failure-modes.md:3` [FORBID] — What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

##### 2+ · personas · grupo → style.photography = `documental` (documental / fotoperiodismo) — 1 reglas

  - `produccion-visual-sw30/SKILL.md:73` [GATE] — | usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO

##### 2+ · personas · grupo → style.photography = `natgeo` (documental de naturaleza (National Geographic)) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → style.photography = `moda` (moda) — 8 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/creative-direction.md:34` [REQUIRE] — - Hasselblad — medium format, shallow DOF, fashion/portrait
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/character-design.md:58` [RECOMMEND] — Use to show one character in multiple outfits or costumes — for fashion exploration, game skin concepts, or wardrobe design.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o

##### 2+ · personas · grupo → style.photography = `producto` (producto / e-commerce) — 1 reglas

  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)

##### 2+ · personas · grupo → style.photography = `cinematografico` (cinematográfico) — 9 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:67` [RECOMMEND] — The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site 
  - `image/SKILL.md:64` [PROCESS] — - **Multi-panel compositions** (grids, collages, storyboard sheets in ONE image) → [multi-panel.md](references/multi-panel.md). 9-cell TVC grids, 2x2 
  - `image/SKILL.md:69` [PROCESS] — - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - `image/SKILL.md:80` [PROCESS] — Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / stand
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/nano-banana.md:25` [RECOMMEND] — - Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `visual-asset-critic/references/critique-rubric.md:107` [FORBID] — - **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
  - `visual-prompt-forge/references/consistency-locks.md:96` [REQUIRE] — The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal s

##### 2+ · personas · grupo → style.photography = `vintage` (vintage / analógico) — 6 reglas

  - `image/SKILL.md:76` [PROCESS] — Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise 
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/portrait-cinema.md:69` [RECOMMEND] — Use for moody, atmospheric portraits with overexposed analog film qualities — muted colors, lifted shadows, and a feeling of faded memory. Ideal for e
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `visual-prompt-forge/references/failure-modes.md:17` [RECOMMEND] — - Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")

##### 2+ · personas · grupo → style.photography = `calle` (fotografía de calle) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → style.photography = `movil` (móvil / snapshot) — 3 reglas

  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `storyboard-html-preview/SKILL.md:238` [RECOMMEND] — Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
  - `storyboard-html-preview/SKILL.md:255` [GATE] — - [ ] Mobile viewport (375px) renders without horizontal scroll

##### 2+ · personas · grupo → style.photography = `bellas_artes` (bellas artes / conceptual) — 1 reglas

  - `image/references/patterns/portrait-cinema.md:83` [RECOMMEND] — Use for beauty campaigns, conceptual art, or album visuals — a portrait where the subject floats in clear water surrounded by translucent aquatic elem

##### 2+ · personas · grupo → style.photography = `estudio` (retrato de estudio) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → lighting.setup = `estudio` (estudio (softbox, strobe, controlada)) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → lighting.setup = `natural_exterior` (natural exterior) — 1 reglas

  - `visual-prompt-forge/adapters/flux.md:56` [RECOMMEND] — - `Sony FX6, 35mm prime, natural light only`

##### 2+ · personas · grupo → lighting.setup = `ventana` (luz entrando por ventana) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → lighting.setup = `golden_hour` (golden hour / atardecer) — 1 reglas

  - `image/references/prompt-framework.md:214` [RECOMMEND] — 3. **Atmospheric particles** — "dust motes suspended in light beam, steam wisps rising from coffee cup, pollen floating in golden hour air, fine rain 

##### 2+ · personas · grupo → lighting.setup = `artificial_nocturna` (artificial nocturna) — 3 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/prompt-framework.md:218` [RECOMMEND] — 7. **Environmental reflections** — "building reflections in wet pavement, sky gradient in chrome bumper surface, warm neon glow on skin from nearby si

##### 2+ · personas · grupo → lighting.setup = `mixta` (mixta) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → composition.shot_size = `macro` (macro / detalle) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → composition.shot_size = `close_up` (close-up) — 3 reglas

  - `image/references/multi-panel.md:94` [RECOMMEND] — **When to use:** Hero shot + close-up + action for a campaign visual — horizontal or vertical triptych.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `storyboard-architect/references/shot-grammar.md:11` [RECOMMEND] — | `MCU` | Medium close-up | Head and shoulders |

##### 2+ · personas · grupo → composition.shot_size = `plano_medio` (plano medio) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → composition.shot_size = `cuerpo_completo` (cuerpo completo) — 2 reglas

  - `image/references/creative-direction.md:47` [RECOMMEND] — - "Waist-up portrait", "full body", "over-the-shoulder"
  - `image/references/patterns/character-design.md:120` [RECOMMEND] — Use for a full character reference card with portrait, full body, key items, and color palette — organized on a white background in a professional con

##### 2+ · personas · grupo → composition.shot_size = `plano_general` (plano general / amplio) — 2 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

##### 2+ · personas · grupo → task.theme = `deportiva` (deportiva) — 6 reglas

  - `aurora-prompt-linter/SKILL.md:157` [RECOMMEND] — - **Sinónimos**: "tank top" en ref + "athletic shirt" en prompt no se detecta como redundante. Roadmap v1.1: tabla de sinónimos.
  - `aurora-prompt-linter/references/README.md:96` [RECOMMEND] — 5. **Sports broadcast**: si flag activo, requiere `60fps` y `broadcast realism` en MAIN (Regla 26 v6.0).
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/patterns/fashion-editorial.md:93` [RECOMMEND] — Use for forward-looking athletic or techwear editorials where abstract 3D forms create a surreal spatial environment around the model.
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 

##### 2+ · personas · grupo → task.theme = `musical` (musical / concierto) — 2 reglas

  - `image/references/patterns/portrait-cinema.md:49` [RECOMMEND] — Use for edgy, tech-forward portraits — artist profiles, electronic music press, tech brand campaigns. High contrast black-and-white with selective red
  - `storyboard-architect/references/on-screen-text.md:10` [RECOMMEND] — 4. **Beat punctuation.** A single word or phrase that lands on a music hit.

##### 2+ · personas · grupo → task.theme = `moda` (moda) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → task.theme = `gastronomica` (gastronómica) — 8 reglas

  - `image/SKILL.md:68` [PROCESS] — - Food & beverage advertising → [patterns/food-beverage.md](references/patterns/food-beverage.md)
  - `image/references/patterns/ecommerce.md:80` [RECOMMEND] — Use for food, beverage, or supplement products where suspended ingredients communicate freshness, flavor, or composition.
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:41` [RECOMMEND] — Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
  - `image/references/patterns/food-beverage.md:65` [RECOMMEND] — Use for hero food posters — restaurants, delivery apps, menu boards — where the food is the entire composition with fillable content slots.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"

##### 2+ · personas · grupo → task.theme = `corporativa` (corporativa) — 3 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:52` [RECOMMEND] — Reject generic fillers ("professional, modern, clean"), they describe everything and constrain nothing. Push to contrast clauses that do work: "operat
  - `visual-prompt-forge/SKILL.md:269` [REQUIRE] — Verbatim means the whole string, unedited. Not "the same idea in better prose". The failure mode is specific and easy to walk into: you are writing fl
  - `visual-prompt-forge/SKILL.md:276` [REQUIRE] — Capitalising the first letter to start a sentence is fine, because the check is case-insensitive. "Minimalist home office, white walls, oak desk, sing

##### 2+ · personas · grupo → task.theme = `medica` (médica / científica) — 3 reglas

  - `brand-lock-extractor/SKILL.md:114` [REQUIRE] — The output is a clinical specification. It models the standards the brand-lock enforces. No emojis anywhere. No marketing adjectives about the brand i
  - `image/references/patterns/food-beverage.md:102` [RECOMMEND] — Use for educational food content, ingredient features, or artisanal brand storytelling — the food item rendered as a scientific illustration in the st
  - `learned/production-learnings.v3.2.json:11` [REQUIRE] — Once an image is accepted and requested changes are local, perform a surgical image edit and preserve the approved pixels/locks outside the requested 

##### 2+ · personas · grupo → task.theme = `viaje` (viaje / turismo) — 3 reglas

  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 
  - `visual-prompt-forge/SKILL.md:303` [REQUIRE] — - **The direction of travel.** Left to right, right to left, toward camera. Without it the generator picks, and consecutive shots stop matching.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 2+ · personas · grupo → task.theme = `automotriz` (automotriz) — 1 reglas

  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo

##### 2+ · personas · grupo → task.theme = `otra` (otra) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → motion.action_complexity = `estatica` (estática) — 11 reglas

  - `brand-lock-extractor/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `storyboard-architect/SKILL.md:263` [GATE] — What the validator cannot check, and you still have to:
  - `storyboard-architect/brand-packs/README.md:44` [REQUIRE] — Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version th
  - `visual-asset-critic/SKILL.md:170` [GATE] — The hashes are the point. Without `image_sha256`, a frame regenerated after this review still satisfies `image_ref`, and a stale ACCEPT sails through 
  - `visual-asset-critic/SKILL.md:215` [GATE] — Worked examples: `examples/critique.accept.json` and `examples/critique.revise.json` show the shape at version `1.0`, which is still valid and carries
  - `visual-prompt-forge/SKILL.md:299` [REQUIRE] — A prompt can be beautifully written and still be impossible to shoot. Every prompt declares, before anything else:
  - `visual-prompt-forge/SKILL.md:360` [GATE] — What it cannot check, and you still have to:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/references/prompt-anatomy.md:66` [RECOMMEND] — 3. **Animation.** Animated text needs After Effects / Remotion / CapCut. Static rendered text is dead-on-arrival for motion content.

##### 2+ · personas · grupo → motion.action_complexity = `pose_dirigida` (pose dirigida) — 6 reglas

  - `image/references/gpt-image.md:94` [RECOMMEND] — **Virtual try-on:** «Change garments only. Preserve exact face, body shape, pose, hair, expression, background, camera angle. Match lighting/shadows s
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.
  - `learned/production-learnings.v3.2.json:3` [REQUIRE] — Preserve a sufficiently specific domain-native pose/technique label instead of expanding it into speculative anatomy. Expand only when the target adap
  - `learned/production-learnings.v3.2.json:4` [REQUIRE] — A reference may control only its declared role. Features explicitly excluded from that role must not be copied into subject identity, pose, camera, fr
  - `learned/production-learnings.v3.2.json:8` [RECOMMEND] — For complex underwater human anatomy, physically justified bubbles/turbulence may obscure non-critical anatomical detail when the brief does not requi
  - `produccion-visual-sw30/SKILL.md:125` [GATE] — 6. Swap de identidad = última operación, sola: "Replace X with Y — same position, same pose, same scale".

##### 2+ · personas · grupo → motion.action_complexity = `accion_simple` (acción simple (un cuerpo)) — 5 reglas

  - `image/references/multi-panel.md:210` [REQUIRE] — - Motion blur instruction must be specific ("blur on hands and feet") or the model applies blur everywhere
  - `image/references/patterns/poster-illustration.md:40` [RECOMMEND] — Use for sport and fitness brand campaigns — a dynamic 3-panel collage combining action, detail, and atmosphere around a boxing/combat sport theme.
  - `image/references/prompt-framework.md:219` [RECOMMEND] — 8. **Motion cues** — "slight motion blur on trailing hair strand, frozen splash droplet from espresso pour, wind-displaced fabric edge of scarf"
  - `learned/production-learnings.v3.2.json:10` [REQUIRE] — Do not declare a generated asset or model successful for a case before running the applicable QA. Separate deterministic/mechanical checks from semant
  - `visual-prompt-forge/SKILL.md:302` [REQUIRE] — - **The point of view.** Profile, frontal, side, rear. "A man walking" is not a shot.

##### 2+ · personas · grupo → motion.action_complexity = `accion_compleja` (acción compleja (varios cuerpos, contacto, física)) — 4 reglas

  - `image/references/prompt-framework.md:217` [RECOMMEND] — 6. **Contact shadows** — "soft contact shadow where cup meets saucer, ambient occlusion in crevices of stone wall, dark line where book spine meets ta
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:305` [REQUIRE] — - **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
  - `visual-prompt-forge/SKILL.md:356` [GATE] — - **Rule 6**: every shot states which third of the frame the body occupies, its point of view and its direction of travel; no scale contradictions, no

##### 2+ · personas · grupo → text.mode = `none` (sin texto) — **0 reglas · RAMA VACÍA**

##### 2+ · personas · grupo → text.mode = `in_image` (texto dentro de la imagen) — 16 reglas

  - `brand-lock-extractor/SKILL.md:54` [PROCESS] — 3. **Typography** (display, body, optional mono, with weights)
  - `brand-lock-extractor/SKILL.md:82` [FORBID] — - All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion languag
  - `brand-lock-extractor/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `image/SKILL.md:56` [PROCESS] — - Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
  - `image/references/models.md:50` [PROCESS] — | Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
  - `image/references/patterns/portrait-cinema.md:29` [RECOMMEND] — Use for urban night portraits with mixed artificial lighting — fluorescent overhead + colored neon signage creating a chromatic push-pull on the subje
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:88` [RECOMMEND] — Use for fashion drops, event announcements, or editorial magazine covers where bold typography and a street fashion figure share equal visual weight o
  - `image/references/text-rendering.md:133` [RECOMMEND] — Describe typography style or name the font directly:
  - `produccion-visual-sw30/SKILL.md:132` [GATE] — 10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los cuerpos nunca tapan logo ni lettering en frames congelados.
  - `storyboard-architect/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `storyboard-architect/references/beat-frameworks.md:45` [RECOMMEND] — Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/on-screen-text.md:71` [REQUIRE] — Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the br
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 2+ · personas · grupo → text.mode = `composite` (texto compuesto después) — 7 reglas

  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:105` [FORBID] — - **Don't include text content in image prompts**, composite separately; text rendering is mediocre
  - `visual-prompt-forge/adapters/nano-banana.md:83` [PROCESS] — 4. Composite text on the chosen variant
  - `visual-prompt-forge/adapters/seedream.md:82` [FORBID] — - **Don't include text content**, text rendering is poor; composite separately
  - `visual-prompt-forge/references/failure-modes.md:53` [FORBID] — - The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.

##### 2+ · personas · grupo → generator.family = `nano_banana` (Nano Banana / Pro) — 38 reglas

  - `image/SKILL.md:100` [REQUIRE] — For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:40` [FORBID] — - **Nano Banana** → [nano-banana.md](references/nano-banana.md) Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mo
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:78` [REQUIRE] — - **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
  - `image/references/models.md:10` [PROCESS] — | Сложная сцена с физикой/композицией | **Nano Banana Pro** |
  - `image/references/models.md:11` [PROCESS] — | Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
  - `image/references/models.md:12` [PROCESS] — | Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
  - `image/references/models.md:17` [PROCESS] — | Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:9` [PROCESS] — | Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/nano-banana.md:55` [RECOMMEND] — Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены пл
  - `image/references/patterns/ecommerce.md:114` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for believable physical distortion
  - `image/references/patterns/fashion-editorial.md:107` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/food-beverage.md:110` [RECOMMEND] — **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
  - `image/references/patterns/food-beverage.md:124` [RECOMMEND] — **Recommended model:** NB2 — image grounding for real city landmarks + illustration style
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/portrait-cinema.md:97` [RECOMMEND] — **Recommended model:** NBP — complex physics (floating hair, fabric, fish transparency, caustic light)
  - `image/references/patterns/poster-illustration.md:117` [RECOMMEND] — **Recommended model:** NB2 — image grounding for accurate peacock anatomy and botanical species
  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
  - `image/references/prompt-framework.md:43` [REQUIRE] — > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
  - `image/references/prompt-framework.md:87` [PROCESS] — **3. Exclusions** - что исключить (опционально): > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
  - `learned/production-learnings.v3.2.json:12` [RECOMMEND] — For complex split-level underwater images with a human in Olympic/platform diving or similarly extreme aquatic anatomy, prefer Nano Banana Pro as the 
  - `visual-prompt-forge/SKILL.md:109` [FORBID] — That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the build when an adapter advertises more words than its ceiling
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/nano-banana.md:101` [FORBID] — - **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
  - `visual-prompt-forge/adapters/nano-banana.md:102` [FORBID] — - **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
  - `visual-prompt-forge/adapters/nano-banana.md:104` [REQUIRE] — - **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:81` [PROCESS] — 2. Feed that image to Nano Banana with variation prompts
  - `visual-prompt-forge/references/failure-modes.md:129` [RECOMMEND] — 2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-prod

##### 2+ · personas · grupo → generator.family = `gpt_image` (GPT Image 2) — 67 reglas

  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:43` [REQUIRE] — - **GPT Image 2** → [gpt-image.md](references/gpt-image.md) 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop 
  - `image/references/golden-rules.md:136` [REQUIRE] — GPT Image 2 обладает глубокими знаниями о культуре, эпохах и визуальных стилях. Вместо описания каждой детали — дай модели культурный/временной/жанров
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:74` [REQUIRE] — > **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.
  - `image/references/golden-rules.md:79` [REQUIRE] — - **GPT Image 2:** прогон на `quality: low` → отбор → переген на `medium` или `high`.
  - `image/references/golden-rules.md:93` [REQUIRE] — Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.
  - `image/references/gpt-image.md:117` [RECOMMEND] — GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не распи
  - `image/references/models.md:13` [PROCESS] — | Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
  - `image/references/models.md:14` [PROCESS] — | Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
  - `image/references/models.md:15` [PROCESS] — | Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
  - `image/references/models.md:16` [PROCESS] — | Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
  - `image/references/models.md:18` [PROCESS] — | Storyboard с фокусом на типографике | **GPT Image 2** |
  - `image/references/models.md:19` [PROCESS] — | Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:26` [REQUIRE] — - **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
  - `image/references/multi-panel.md:122` [RECOMMEND] — **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych) **Model:** GPT Image 2 `quality: medium` — if text overlay need
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:294` [REQUIRE] — **Recommended size:** 1024x1536 (portrait — 3 columns x 4 rows needs vertical space) **Model:** GPT Image 2 `quality: high` (text-heavy — scene number
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa
  - `image/references/multi-panel.md:83` [RECOMMEND] — **Recommended size:** 1024x1024 (square) or 1024x1536 (vertical for portrait emphasis) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro (bo
  - `image/references/patterns/character-design.md:108` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
  - `image/references/patterns/character-design.md:140` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering
  - `image/references/patterns/character-design.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
  - `image/references/patterns/character-design.md:3` [RECOMMEND] — Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}`
  - `image/references/patterns/character-design.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
  - `image/references/patterns/character-design.md:80` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
  - `image/references/patterns/ecommerce.md:74` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
  - `image/references/patterns/ecommerce.md:94` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
  - `image/references/patterns/fashion-editorial.md:27` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
  - `image/references/patterns/fashion-editorial.md:73` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:35` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
  - `image/references/patterns/food-beverage.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
  - `image/references/patterns/food-beverage.md:96` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
  - `image/references/patterns/portrait-cinema.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 — backlight exposure control and skin rendering
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `image/references/patterns/portrait-cinema.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise dual-light color rendering on skin
  - `image/references/patterns/portrait-cinema.md:63` [RECOMMEND] — **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:3` [RECOMMEND] — Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. De
  - `image/references/patterns/poster-illustration.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
  - `image/references/patterns/poster-illustration.md:82` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
  - `image/references/patterns/ui-social.md:104` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements requir
  - `image/references/patterns/ui-social.md:135` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout
  - `image/references/patterns/ui-social.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
  - `image/references/patterns/ui-social.md:3` [RECOMMEND] — Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for c
  - `image/references/patterns/ui-social.md:49` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
  - `image/references/patterns/ui-social.md:75` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/gpt-image.md:38` [RECOMMEND] — GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:86` [FORBID] — - **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
  - `visual-prompt-forge/adapters/gpt-image.md:89` [FORBID] — - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:87` [RECOMMEND] — - For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 2+ · personas · grupo → generator.family = `midjourney` (Midjourney) — 13 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:18` [PROCESS] — - Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
  - `visual-prompt-forge/SKILL.md:295` [REQUIRE] — If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. T
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
  - `visual-prompt-forge/references/consistency-locks.md:64` [RECOMMEND] — For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
  - `visual-prompt-forge/references/failure-modes.md:39` [RECOMMEND] — - For Midjourney, use `--cref` with `--cw 50`

##### 2+ · personas · grupo → generator.family = `flux` (Flux) — 17 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-asset-critic/SKILL.md:102` [REQUIRE] — **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts: > "Hands are mangled. This is a known Fl
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/flux.md:66` [REQUIRE] — The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.
  - `visual-prompt-forge/adapters/flux.md:86` [RECOMMEND] — Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.
  - `visual-prompt-forge/adapters/flux.md:90` [FORBID] — - **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
  - `visual-prompt-forge/adapters/flux.md:91` [FORBID] — - **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/gpt-image.md:90` [REQUIRE] — - **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:69` [RECOMMEND] — **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/references/failure-modes.md:18` [RECOMMEND] — - Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

##### 2+ · personas · grupo → generator.family = `ideogram` (Ideogram) — 14 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:257` [REQUIRE] — If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:30` [REQUIRE] — The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/ideogram.md:92` [FORBID] — - **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
  - `visual-prompt-forge/adapters/ideogram.md:93` [FORBID] — - **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
  - `visual-prompt-forge/references/failure-modes.md:54` [REQUIRE] — - If text must be in-image (poster work), use Ideogram v3 with explicit override flag
  - `visual-prompt-forge/references/failure-modes.md:56` [RECOMMEND] — - Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
  - `visual-prompt-forge/references/prompt-anatomy.md:58` [FORBID] — **What:** on-screen text composited after generation. **Source:** `text-overlays.json`. **Never appears in image prompts** (except Ideogram Mode 2 wit
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

##### 2+ · personas · grupo → generator.family = `seedream` (Seedream) — 3 reglas

  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/seedream.md:80` [FORBID] — - **Don't write paragraphs**. Seedream wants comma-separated phrases
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output

### SIN PERSONAS — 5 reglas propias

  - `brand-lock-extractor/references/extraction-rubric.md:59` [FORBID] — - Imagery: no stock-photo gloss? no people? no gradients? no clip-art icons? Each absence is a never.
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:57` [PROCESS] — - Edit existing image (object removal, lighting swap, colorization, restoration, localization) → [editing.md](references/editing.md)
  - `image/references/gpt-image.md:96` [FORBID] — **Object removal:** «Remove [X]. Do not change anything else. Use `input_fidelity: high` to maintain surrounding context» (только gpt-image-1.5/1, в g
  - `image/references/gpt-image.md:98` [RECOMMEND] — **Lighting/weather swap:** «Change ONLY environmental conditions: lighting direction/quality, shadows, atmosphere, precipitation. Preserve identity, g

#### 2+ · sin personas → scene.category = `exterior` (exterior) — 3 reglas

  - `brand-lock-extractor/brand-packs/_template.md:15` [RECOMMEND] — Every hex value here is allowed. Anything outside this list is not.
  - `learned/production-learnings.v3.2.json:11` [REQUIRE] — Once an image is accepted and requested changes are local, perform a surgical image edit and preserve the approved pixels/locks outside the requested 
  - `learned/production-learnings.v3.4.json:4` [REQUIRE] — Prompt revisions may not be freely rewritten. Re-render the same immutable Prompt AST against the updated frozen brief; any AST/model/parameter/templa

#### 2+ · sin personas → scene.category = `interior` (interior) — 13 reglas

  - `image/references/patterns/ui-social.md:55` [RECOMMEND] — Use to create a polished App Store or Google Play listing screenshot — device frame with app UI inside, feature headline, and clean gradient backgroun
  - `image/references/prompt-framework.md:215` [RECOMMEND] — 4. **Specular behavior** — "specular highlights on metal edges of watch, caustic reflections dancing inside glass bottle, wet surface sheen on cobbles
  - `storyboard-architect/SKILL.md:255` [GATE] — - every overlay's timing sits inside its shot window, and exit is after enter
  - `storyboard-architect/SKILL.md:259` [GATE] — It warns, rather than fails, on judgement calls worth a second look: overlay copy repeated inside a shot subject, a raw hex in a subject, shot ids out
  - `visual-asset-critic/SKILL.md:232` [FORBID] — If the brief was "founder at laptop, calm mood" and the generation delivered exactly that, don't note that "the room could be more visually interestin
  - `visual-prompt-forge/SKILL.md:104` [REQUIRE] — `max_prompt_words` is a ceiling. The range in an adapter `.md` is the recommended target and always sits inside that ceiling, so a `.md` saying "40 to
  - `visual-prompt-forge/adapters/flux.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/gpt-image.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/ideogram.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/nano-banana.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `
  - `visual-prompt-forge/adapters/seedream.md:3` [RECOMMEND] — > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `

#### 2+ · sin personas → scene.category = `animales` (animales / fauna) — 1 reglas

  - `image/references/patterns/food-beverage.md:116` [RECOMMEND] — Use for restaurant guides, food festival materials, travel content, or local cuisine features — a bird's-eye illustrated map showing food specialties 

#### 2+ · sin personas → scene.category = `arquitectonica` (arquitectónica / inmobiliaria) — 1 reglas

  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency

#### 2+ · sin personas → scene.category = `paisaje_natural` (paisaje natural) — 4 reglas

  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa

#### 2+ · sin personas → scene.category = `producto_objeto` (producto u objeto) — 21 reglas

  - `image/SKILL.md:57` [PROCESS] — - Edit existing image (object removal, lighting swap, colorization, restoration, localization) → [editing.md](references/editing.md)
  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)
  - `image/references/gpt-image.md:96` [FORBID] — **Object removal:** «Remove [X]. Do not change anything else. Use `input_fidelity: high` to maintain surrounding context» (только gpt-image-1.5/1, в g
  - `image/references/gpt-image.md:98` [RECOMMEND] — **Lighting/weather swap:** «Change ONLY environmental conditions: lighting direction/quality, shadows, atmosphere, precipitation. Preserve identity, g
  - `image/references/models.md:39` [PROCESS] — - Product shots на нейтральном фоне.
  - `image/references/multi-panel.md:216` [RECOMMEND] — **When to use:** Product transformation, makeover, time comparison, renovation — two states side by side.
  - `image/references/patterns/ecommerce.md:100` [RECOMMEND] — Use for disruptive, scroll-stopping social ads where the product packaging appears squeezed, inflated, or physically distorted as if made of soft rubb
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:29` [RECOMMEND] — Use for premium beauty or fragrance product photography — dark, moody, tactile surfaces with atmospheric effects.
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:51` [RECOMMEND] — Use to present a product commercial shot breakdown in a single image — pitch decks, creative presentations, client approvals.
  - `image/references/patterns/ecommerce.md:9` [RECOMMEND] — Use when you need a playful, attention-grabbing product visual where tiny workers interact with an oversized product — ideal for social media ads and 
  - `image/references/patterns/food-beverage.md:41` [RECOMMEND] — Use for premium beverage brand campaigns that combine lifestyle and product in a structured board layout — model shot + hero product + product lineup.
  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `image/references/patterns/ui-social.md:29` [RECOMMEND] — Use for square-format posts on Instagram or Facebook — quote cards, feature announcements, or product highlights with centered layout.
  - `image/references/patterns/ui-social.md:9` [RECOMMEND] — Use for vertical product or brand ads targeting Instagram Stories — hero product, bold headline, and swipe-up CTA zone at the bottom.
  - `storyboard-architect/references/beat-frameworks.md:20` [RECOMMEND] — Default for product films and brand films. Three beats:
  - `storyboard-architect/references/beat-frameworks.md:23` [RECOMMEND] — 2. **Hero**, the product/founder/methodology arrives. Show what it does, not what it is.
  - `storyboard-architect/references/beat-frameworks.md:29` [RECOMMEND] — Use when: product launches, brand films, anchor pieces.
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/shot-grammar.md:17` [RECOMMEND] — Default to MCU and MS for talking-head founder content. ECU and CU for product detail and emotion. WS and EWS for context-setting.

#### 2+ · sin personas → scene.category = `urbana` (urbana / cityscape) — 2 reglas

  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 

#### 2+ · sin personas → style.photography = `editorial` (editorial) — 11 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `image/references/patterns/poster-illustration.md:9` [RECOMMEND] — Use for urban development campaigns, anniversary materials, cultural exhibitions, or editorial features — a single city view divided down the middle, 
  - `visual-asset-critic/SKILL.md:20` [PROCESS] — - Has a generated image and just wants editorial feedback (no storyboard reference)
  - `visual-asset-critic/SKILL.md:8` [FORBID] — You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structu
  - `visual-prompt-forge/adapters/nano-banana.md:82` [PROCESS] — 3. Get 4–8 variants of the same shot for editorial selection
  - `visual-prompt-forge/references/consistency-locks.md:109` [FORBID] — Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.
  - `visual-prompt-forge/references/failure-modes.md:130` [RECOMMEND] — 3. The image is 80% right and the gap is editorial → ship to post and let the editor finish
  - `visual-prompt-forge/references/failure-modes.md:3` [FORBID] — What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

#### 2+ · sin personas → style.photography = `documental` (documental / fotoperiodismo) — 1 reglas

  - `produccion-visual-sw30/SKILL.md:73` [GATE] — | usecase | `usecase_doc` | fotografía documental Kodak Tri-X de reportaje. Kodak Portra suaviza la piel por diseño y contradice los poros — PROHIBIDO

#### 2+ · sin personas → style.photography = `natgeo` (documental de naturaleza (National Geographic)) — **0 reglas · RAMA VACÍA**

#### 2+ · sin personas → style.photography = `moda` (moda) — 5 reglas

  - `image/SKILL.md:67` [PROCESS] — - Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
  - `image/references/multi-panel.md:173` [RECOMMEND] — **When to use:** Fashion editorial or film-style sequence — multiple camera angles of the same scene in one image.
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:58` [RECOMMEND] — Use for streetwear drops, limited edition launches, or urban fashion brand campaigns where bold type dominates the composition.
  - `image/references/patterns/fashion-editorial.md:9` [RECOMMEND] — Use for fashion brand campaign hero images — one wide shot combining hero pose, close-up detail, and action/movement in a triptych layout.

#### 2+ · sin personas → style.photography = `producto` (producto / e-commerce) — 1 reglas

  - `image/SKILL.md:66` [PROCESS] — - E-commerce product shots → [patterns/ecommerce.md](references/patterns/ecommerce.md)

#### 2+ · sin personas → style.photography = `cinematografico` (cinematográfico) — 8 reglas

  - `brand-lock-extractor/references/extraction-rubric.md:67` [RECOMMEND] — The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site 
  - `image/SKILL.md:69` [PROCESS] — - Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
  - `image/SKILL.md:80` [PROCESS] — Universal element checklist (subject, context, action, environment, camera, lighting, mood, materials, palette, format), detail modes (concise / stand
  - `image/references/golden-rules.md:27` [REQUIRE] — ❌ Bad: "Cool car, neon, city, night, 8k" ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. Neo
  - `image/references/nano-banana.md:25` [RECOMMEND] — - Tag-soup: «cool, modern, 4k, cinematic» — пишет связным предложением.
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `visual-asset-critic/references/critique-rubric.md:107` [FORBID] — - **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
  - `visual-prompt-forge/references/consistency-locks.md:96` [REQUIRE] — The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal s

#### 2+ · sin personas → style.photography = `vintage` (vintage / analógico) — 5 reglas

  - `image/SKILL.md:76` [PROCESS] — Studio-quality vocabulary for lighting design, camera and hardware, color grading and film stock, materiality and texture. Read when you need precise 
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:109` [RECOMMEND] — Use for decorative prints, packaging illustration, wallpaper design, or editorial art — a symmetrical composition combining a peacock with botanical e
  - `visual-prompt-forge/references/failure-modes.md:17` [RECOMMEND] — - Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")

#### 2+ · sin personas → style.photography = `calle` (fotografía de calle) — **0 reglas · RAMA VACÍA**

#### 2+ · sin personas → style.photography = `movil` (móvil / snapshot) — 3 reglas

  - `image/references/patterns/poster-illustration.md:65` [RECOMMEND] — Use for tech product launch visuals — clean, color-dominant hero shots where a smartphone (or similar device) floats against a monochromatic gradient 
  - `storyboard-html-preview/SKILL.md:238` [RECOMMEND] — Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
  - `storyboard-html-preview/SKILL.md:255` [GATE] — - [ ] Mobile viewport (375px) renders without horizontal scroll

#### 2+ · sin personas → style.photography = `bellas_artes` (bellas artes / conceptual) — **0 reglas · RAMA VACÍA**

#### 2+ · sin personas → style.photography = `estudio` (retrato de estudio) — **0 reglas · RAMA VACÍA**

#### 2+ · sin personas → text.mode = `none` (sin texto) — **0 reglas · RAMA VACÍA**

#### 2+ · sin personas → text.mode = `in_image` (texto dentro de la imagen) — 14 reglas

  - `brand-lock-extractor/SKILL.md:54` [PROCESS] — 3. **Typography** (display, body, optional mono, with weights)
  - `brand-lock-extractor/SKILL.md:82` [FORBID] — - All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion languag
  - `brand-lock-extractor/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `image/SKILL.md:56` [PROCESS] — - Text in image, infographic, diagram, multilingual rendering → [text-rendering.md](references/text-rendering.md)
  - `image/references/models.md:50` [PROCESS] — | Text in image | `"..."` в кавычках, font + position | `"..."` или ALL CAPS + «no extra words / no duplicate text» |
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/text-rendering.md:133` [RECOMMEND] — Describe typography style or name the font directly:
  - `produccion-visual-sw30/SKILL.md:132` [GATE] — 10. Logos solo heredados de asset aprobado o descripción canónica del brand-lock; los cuerpos nunca tapan logo ni lettering en frames congelados.
  - `storyboard-architect/brand-packs/README.md:3` [RECOMMEND] — A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. E
  - `storyboard-architect/references/beat-frameworks.md:45` [RECOMMEND] — Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:
  - `storyboard-architect/references/on-screen-text.md:17` [RECOMMEND] — 3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
  - `storyboard-architect/references/on-screen-text.md:71` [REQUIRE] — Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the br
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

#### 2+ · sin personas → text.mode = `composite` (texto compuesto después) — 7 reglas

  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:105` [FORBID] — - **Don't include text content in image prompts**, composite separately; text rendering is mediocre
  - `visual-prompt-forge/adapters/nano-banana.md:83` [PROCESS] — 4. Composite text on the chosen variant
  - `visual-prompt-forge/adapters/seedream.md:82` [FORBID] — - **Don't include text content**, text rendering is poor; composite separately
  - `visual-prompt-forge/references/failure-modes.md:53` [FORBID] — - The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.

#### 2+ · sin personas → generator.family = `nano_banana` (Nano Banana / Pro) — 34 reglas

  - `image/SKILL.md:100` [REQUIRE] — For edits, also include an explicit preserve-list (mandatory for gpt-image-2, recommended for nano-banana):
  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:40` [FORBID] — - **Nano Banana** → [nano-banana.md](references/nano-banana.md) Image grounding for real locations. Extreme aspect ratios (1:8, 8:1, 4:1). Thinking mo
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:78` [REQUIRE] — - **Nano Banana:** прогон вариантов на `0.5K` Flash → отбор → переген победителя на `2K`/`4K`.
  - `image/references/models.md:10` [PROCESS] — | Сложная сцена с физикой/композицией | **Nano Banana Pro** |
  - `image/references/models.md:11` [PROCESS] — | Длинные горизонтальные/вертикальные форматы (1:8, 8:1, 4:1) | **Nano Banana** (только NB поддерживает экстрим) |
  - `image/references/models.md:12` [PROCESS] — | Дешёвая массовая генерация | **Nano Banana 2 Lite** или **gpt-image-1-mini** |
  - `image/references/models.md:17` [PROCESS] — | Сториборды, комиксы (последовательность) | **Nano Banana** (extreme ratios + thinking) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:9` [PROCESS] — | Реальное место/объект (с грунтингом) | **Nano Banana** (NB2/NBP) |
  - `image/references/multi-panel.md:162` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) — gives each cell enough resolution **Model:** Nano Banana Pro (handles complex multi-element compositions
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/nano-banana.md:55` [RECOMMEND] — Включён по умолчанию; у NBP отключить нельзя (модель рисует до 2 «thought images» в бэкенде, они не тарифицируются как картинки, но thinking-токены пл
  - `image/references/patterns/ecommerce.md:114` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for believable physical distortion
  - `image/references/patterns/fashion-editorial.md:107` [RECOMMEND] — **Recommended model:** NBP — complex spatial reasoning for blob placement and reflections
  - `image/references/patterns/fashion-editorial.md:87` [RECOMMEND] — **Recommended model:** NB2 — natural movement, analog film grain, atmospheric grounding
  - `image/references/patterns/food-beverage.md:110` [RECOMMEND] — **Recommended model:** NB2 — naturalist illustration style, grounding on botanical plate aesthetics
  - `image/references/patterns/food-beverage.md:124` [RECOMMEND] — **Recommended model:** NB2 — image grounding for real city landmarks + illustration style
  - `image/references/patterns/portrait-cinema.md:77` [RECOMMEND] — **Recommended model:** NB2 — analog film grain emulation and atmospheric mood
  - `image/references/patterns/poster-illustration.md:28` [RECOMMEND] — **Recommended model:** NBP — spatial reasoning for architectural morphing and perspective consistency
  - `image/references/prompt-framework.md:43` [REQUIRE] — > - **Nano Banana** — игнорит числа, пиши описательно («shallow depth of field»)
  - `image/references/prompt-framework.md:87` [PROCESS] — **3. Exclusions** - что исключить (опционально): > Формулируй позитивно! NBP лучше понимает "clean background" чем "no clutter"
  - `visual-prompt-forge/SKILL.md:109` [FORBID] — That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the build when an adapter advertises more words than its ceiling
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/nano-banana.md:101` [FORBID] — - **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
  - `visual-prompt-forge/adapters/nano-banana.md:102` [FORBID] — - **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
  - `visual-prompt-forge/adapters/nano-banana.md:104` [REQUIRE] — - **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:81` [PROCESS] — 2. Feed that image to Nano Banana with variation prompts
  - `visual-prompt-forge/references/failure-modes.md:129` [RECOMMEND] — 2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-prod

#### 2+ · sin personas → generator.family = `gpt_image` (GPT Image 2) — 61 reglas

  - `image/SKILL.md:112` [RECOMMEND] — Prefer: ready-to-copy prompts, hex colors, concrete materials, named compositions, model-specific syntax (5-slot for GPT Image, natural prose for Nano
  - `image/SKILL.md:114` [FORBID] — Avoid: tag soup ("cool, modern, 4k"), vague praise ("stunning, epic, masterpiece" — actively hurts GPT Image 2), negative framing ("no people, no cars
  - `image/SKILL.md:34` [PROCESS] — Decide: Nano Banana (NB2 or NBP) or GPT Image 2. The choice changes the prompt syntax fundamentally — natural-language paragraphs vs. labeled 5-slot t
  - `image/SKILL.md:43` [REQUIRE] — - **GPT Image 2** → [gpt-image.md](references/gpt-image.md) 5-slot template (Scene / Subject / Important Details / Use Case / Constraints). Anti-slop 
  - `image/references/golden-rules.md:136` [REQUIRE] — GPT Image 2 обладает глубокими знаниями о культуре, эпохах и визуальных стилях. Вместо описания каждой детали — дай модели культурный/временной/жанров
  - `image/references/golden-rules.md:161` [REQUIRE] — 4. **Era/cultural anchors работают лучше с GPT Image 2** (world knowledge). С Nano Banana результат менее предсказуем — NB больше опирается на явные о
  - `image/references/golden-rules.md:3` [REQUIRE] — Универсальные принципы. Работают для **обеих** семей моделей (Nano Banana и GPT Image 2). Для модельной специфики см. [nano-banana.md](nano-banana.md)
  - `image/references/golden-rules.md:74` [REQUIRE] — > **Thinking Mode** (NB only), **`quality: low/medium/high`** (GPT Image 2 only) — см. соответствующие references.
  - `image/references/golden-rules.md:79` [REQUIRE] — - **GPT Image 2:** прогон на `quality: low` → отбор → переген на `medium` или `high`.
  - `image/references/golden-rules.md:93` [REQUIRE] — Multi-image вход: **NB до 14**, **GPT Image 2 до 16**. Индексируй с ролью каждой картинки.
  - `image/references/gpt-image.md:117` [RECOMMEND] — GPT Image 2 умеет домысливать контекст: «Bethel, NY, August 1969» → выведет Woodstock-эстетику. Используй: дай исторический/культурный анкер, не распи
  - `image/references/models.md:13` [PROCESS] — | Фотореализм с тонкой типографикой/UI | **GPT Image 2** |
  - `image/references/models.md:14` [PROCESS] — | Точное editing с preservation (try-on, swap, weather) | **GPT Image 2** (в editing у него лучшая identity-preservation) |
  - `image/references/models.md:15` [PROCESS] — | Маленький плотный текст в кадре | **GPT Image 2** (`quality: high`) |
  - `image/references/models.md:16` [PROCESS] — | Брендовая полиграфия / постеры с EXACT TEXT | **GPT Image 2** |
  - `image/references/models.md:18` [PROCESS] — | Storyboard с фокусом на типографике | **GPT Image 2** |
  - `image/references/models.md:19` [PROCESS] — | Style transfer без упоминаемых референс-картинок | **GPT Image 2** (concrete visual targets) |
  - `image/references/models.md:20` [PROCESS] — | Рендер из 14+ референсов | **Nano Banana Pro** (до 14) или **GPT Image 2** (до 16) |
  - `image/references/models.md:26` [REQUIRE] — - **Экстремальные пропорции.** 1:8, 8:1, 1:4, 4:1 — баннеры, скроллы, комикс-стрипы. У GPT Image 2 max 3:1.
  - `image/references/multi-panel.md:122` [RECOMMEND] — **Recommended size:** 1536x1024 (horizontal triptych) or 1024x1536 (vertical triptych) **Model:** GPT Image 2 `quality: medium` — if text overlay need
  - `image/references/multi-panel.md:205` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape, 3x2 grid) **Model:** GPT Image 2 `quality: medium` or Nano Banana Pro **Common pitfalls:**
  - `image/references/multi-panel.md:243` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape — gives each half a portrait-like proportion) **Model:** GPT Image 2 `quality: medium` — for text labels ("
  - `image/references/multi-panel.md:46` [RECOMMEND] — **Recommended size:** 1536x1024 (landscape) **Model:** GPT Image 2 `quality: high` (text-heavy — timestamps and titles need legibility) **Common pitfa
  - `image/references/patterns/character-design.md:108` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — smooth 3D vinyl surfaces render well at medium; `high` for marketing-ready close-ups
  - `image/references/patterns/character-design.md:140` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout with hex codes, labels, and stat block requires precise rendering
  - `image/references/patterns/character-design.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — height reference lines and color callout text require precise rendering
  - `image/references/patterns/character-design.md:3` [RECOMMEND] — Reusable prompt templates for character turnarounds, expression sheets, outfit variants, and collectible/card formats. Each pattern uses `{variables}`
  - `image/references/patterns/character-design.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text labels and consistent facial identity across 9 cells need precise control
  - `image/references/patterns/character-design.md:80` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: medium`) — character consistency is the priority; `high` only if outfit labels need fine legibility
  - `image/references/patterns/ecommerce.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — precise figurine detail and product label legibility
  - `image/references/patterns/ecommerce.md:3` [RECOMMEND] — Reusable prompt templates for product ads, packaging, and commercial visuals. Each pattern uses `{variables}` for customization. Default model: GPT Im
  - `image/references/patterns/ecommerce.md:43` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — surface materials and condensation detail
  - `image/references/patterns/ecommerce.md:74` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — grid precision and text in panel 9
  - `image/references/patterns/ecommerce.md:94` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — frozen detail precision and label legibility
  - `image/references/patterns/fashion-editorial.md:27` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency across panels and fabric texture detail
  - `image/references/patterns/fashion-editorial.md:3` [RECOMMEND] — Reusable prompt templates for fashion campaigns, lookbooks, and editorial shoots. Each pattern uses `{variables}` for customization. Default model: GP
  - `image/references/patterns/fashion-editorial.md:52` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — identity consistency critical across four frames
  - `image/references/patterns/fashion-editorial.md:73` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering and model-type depth interplay
  - `image/references/patterns/food-beverage.md:3` [RECOMMEND] — Reusable prompt templates for food photography, beverage campaigns, and culinary illustration. Each pattern uses `{variables}` for customization. Defa
  - `image/references/patterns/food-beverage.md:35` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — fracture detail and cocoa powder precision
  - `image/references/patterns/food-beverage.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — label legibility and panel consistency
  - `image/references/patterns/food-beverage.md:96` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — steam, condensation, and ingredient texture fidelity
  - `image/references/patterns/portrait-cinema.md:3` [RECOMMEND] — Reusable prompt templates for cinematic portraits, atmospheric character photography, and mood-driven portraiture. Each pattern uses `{variables}` for
  - `image/references/patterns/portrait-cinema.md:63` [RECOMMEND] — **Recommended model:** GPT Image 2 — high-contrast mono rendering and controlled glitch placement
  - `image/references/patterns/poster-illustration.md:103` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — typography rendering and figure-type layering
  - `image/references/patterns/poster-illustration.md:3` [RECOMMEND] — Reusable prompt templates for posters, art prints, campaign collages, and graphic illustrations. Each pattern uses `{variables}` for customization. De
  - `image/references/patterns/poster-illustration.md:59` [RECOMMEND] — **Recommended model:** GPT Image 2 — identity consistency across panels and sweat/texture detail
  - `image/references/patterns/poster-illustration.md:82` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text rendering, screen content legibility, device accuracy
  - `image/references/patterns/ui-social.md:104` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — dense text (labels, numbers, navigation), precise chart rendering, and small UI elements requir
  - `image/references/patterns/ui-social.md:135` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — color accuracy of palette swatches is critical, plus small text labels throughout
  - `image/references/patterns/ui-social.md:23` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — headline text legibility and glassmorphism transparency effects need precision
  - `image/references/patterns/ui-social.md:3` [RECOMMEND] — Reusable prompt templates for social media ads, app store assets, dashboard mockups, and visual analysis boards. Each pattern uses `{variables}` for c
  - `image/references/patterns/ui-social.md:49` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — text-heavy layout; legibility at small sizes is critical
  - `image/references/patterns/ui-social.md:75` [RECOMMEND] — **Recommended model:** GPT Image 2 (`quality: high`) — device bezel precision, small UI text, and headline legibility all demand high quality
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/gpt-image.md:38` [RECOMMEND] — GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:86` [FORBID] — - **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
  - `visual-prompt-forge/adapters/gpt-image.md:89` [FORBID] — - **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
  - `visual-prompt-forge/references/failure-modes.md:87` [RECOMMEND] — - For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

#### 2+ · sin personas → generator.family = `midjourney` (Midjourney) — 13 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:18` [PROCESS] — - Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
  - `visual-prompt-forge/SKILL.md:295` [REQUIRE] — If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. T
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/midjourney.md:105` [RECOMMEND] — Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Disc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
  - `visual-prompt-forge/references/consistency-locks.md:64` [RECOMMEND] — For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
  - `visual-prompt-forge/references/failure-modes.md:39` [RECOMMEND] — - For Midjourney, use `--cref` with `--cw 50`

#### 2+ · sin personas → generator.family = `flux` (Flux) — 13 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/flux.md:36` [FORBID] — Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
  - `visual-prompt-forge/adapters/flux.md:86` [RECOMMEND] — Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.
  - `visual-prompt-forge/adapters/flux.md:90` [FORBID] — - **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
  - `visual-prompt-forge/adapters/flux.md:91` [FORBID] — - **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
  - `visual-prompt-forge/adapters/flux.md:93` [FORBID] — - **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/nano-banana.md:5` [RECOMMEND] — Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano
  - `visual-prompt-forge/adapters/nano-banana.md:69` [RECOMMEND] — **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
  - `visual-prompt-forge/adapters/nano-banana.md:80` [PROCESS] — 1. Generate hero shot in Midjourney or Flux (one prompt → one image)
  - `visual-prompt-forge/references/failure-modes.md:20` [RECOMMEND] — - Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

#### 2+ · sin personas → generator.family = `ideogram` (Ideogram) — 14 reglas

  - `ai-production-director/SKILL.md:126` [REQUIRE] — `ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefa
  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/SKILL.md:257` [REQUIRE] — If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram
  - `visual-prompt-forge/adapters/gpt-image.md:75` [REQUIRE] — GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
  - `visual-prompt-forge/adapters/gpt-image.md:82` [RECOMMEND] — Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.
  - `visual-prompt-forge/adapters/ideogram.md:11` [RECOMMEND] — Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Synta
  - `visual-prompt-forge/adapters/ideogram.md:30` [REQUIRE] — The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
  - `visual-prompt-forge/adapters/ideogram.md:5` [RECOMMEND] — Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded soc
  - `visual-prompt-forge/adapters/ideogram.md:92` [FORBID] — - **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
  - `visual-prompt-forge/adapters/ideogram.md:93` [FORBID] — - **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
  - `visual-prompt-forge/references/failure-modes.md:54` [REQUIRE] — - If text must be in-image (poster work), use Ideogram v3 with explicit override flag
  - `visual-prompt-forge/references/failure-modes.md:56` [RECOMMEND] — - Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
  - `visual-prompt-forge/references/prompt-anatomy.md:58` [FORBID] — **What:** on-screen text composited after generation. **Source:** `text-overlays.json`. **Never appears in image prompts** (except Ideogram Mode 2 wit
  - `visual-prompt-forge/references/prompt-anatomy.md:65` [RECOMMEND] — 2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.

#### 2+ · sin personas → generator.family = `seedream` (Seedream) — 3 reglas

  - `visual-prompt-forge/SKILL.md:17` [PROCESS] — - Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
  - `visual-prompt-forge/adapters/seedream.md:80` [FORBID] — - **Don't write paragraphs**. Seedream wants comma-separated phrases
  - `visual-prompt-forge/adapters/seedream.md:83` [FORBID] — - **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output

## Reglas sin colocar — 0

Cero es la condición de que la división sea exhaustiva.

