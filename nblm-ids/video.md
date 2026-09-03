# Reglas del skill: video

348 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## video/SKILL.md

- [2d5d435df3ef] **Still keyframes, character sheets, animatic panels** to feed the video pipeline: use the sibling `image` skill, then return with the keyframes.
- [bc478afe5b70] U1–U12 universal rules that apply to every video model: prompt skeleton, weight-at-start, show-don't-tell, lens language, character anchor, contradictions, duration discipline, final image rule, three-detail check.
- [534cc7500424] Use this short selector. The full reasoning is in the chosen file.
- [3eac07a0a838] For a more detailed comparison (max clip length, audio support, character lock methods, motion brush, etc.), read the model file you picked. Do not load all three.
- [f21bcfe2dfbc] If any shot fails, fix before sending. This is the step the user has had to enforce repeatedly. Do not skip it.
- [99b3186877c9] Prefer: ready-to-copy prompts, clear section labels, production language, motivated camera and light direction, strict continuity blocks, model-specific syntax, direct fixes.
- [54b8e873fa4e] Avoid: long theory unless asked, academic lectures, vague inspiration, decorative jargon, "cinematic masterpiece" filler, prompts without camera and light, prompts without continuity, stacking more than two director references, abstract emotions without physical translation.

## video/references/animatic-keyframes.md

- [1abf520d87fe] This is the still-panel layer. A storyboard keyframe is not a frame grab of footage — it is a single drawn image that must carry one story-beat with **no motion and (usually) no face**. The animatic hangs off these panels. A panel that only looks good is wallpaper; a panel must report its story function, its drama, and the motion it cannot show, all frozen.
- [b19568241a2e] What an animatic keyframe must do
- [08a797245f8c] The keyframe card (a still extension of the shot card)
- [423028c059a7] How many keyframes per beat (density ladder)
- [540c8325a473] Composing a still that reads as MOTION
- [9a75e498f8a5] Emotion without faces in a still
- [f112ae392b0f] The loaded frame for one panel
- [8a00af193f34] From keyframe to image-gen prompt
- [739f6cf3bb40] Worked keyframe board for a 30s race spot
- [0715fd2a94e1] Checklist: does this keyframe earn its place
- [24fe340cb58e] In an animatic the **panel is the unit, not the shot.** A shot has duration, motion, and sound to carry its function across time. A keyframe has one frozen image and must carry the same function in a single glance. So every panel does four things at once, in one still:
- [43a9c422d34f] **One emotion** — routed through metal, rubber, light, or anatomy, never named (`dramaturgy.md` §2). Mixed signals = no signal.
- [b9cd34ffcb70] **Ritual / staging** (quiet) | 1 hero panel, held | 1 panel living 1.5-2.5s | A silent beat is monolithic. Do not subdivide it — its power is that nothing moves while the world holds its breath. One symmetric "breath" frame, most negative space, least motion.
- [b04a79b44100] **Contest** (sustained roar) | alternating | fragment-cluster ↔ one held detail | Never two bang-clusters back to back. Between every burst, one held quiet panel — loud only works next to quiet.
- [6d32d7171722] **Allocation rule.** A 30s spot lands at ~18-26 panels. Plot the board as a descending duration staircase (≈2.5s → 0.5s → 4fr), broken only by the one pre-launch pause and the one post-finish hold. The board should *read* as an accelerating tachometer even on mute. Give a beat a micro-burst only when the audio detonates; everywhere else, one panel that holds is stronger than three that scatter.
- [0fb332eaeff4] A keyframe cannot ramp, cut, or whip. Each missing move resolves into one of **six frozen cues**. Never write "motion" — write the artifact motion leaves behind. State the cue in the card's *Motion-as-still* field and again in the prompt's camera/light clause; models default to over-clean stabilization and will sand the speed off unless told (§7).
- [84e4c557c5f1] **Sharp-subject / blurred-field separation** | Shallow-DOF macro: knuckle, needle, latch razor-sharp, everything else dissolved. Isolation = the cut-to-detail frozen. | insert chain, crash-zoom arrival, hip-hop CU
- [9116b6b7205f] A face does four jobs: shows the feeling, shows where it looks, shows the cost, shows the decision. Faces banned, redistribute: **decision → anatomy mid-action; internal state → an object crossing a threshold; looking/rivalry → space** (§6 and `dramaturgy.md` §2). Assign one job per panel and tag it. The emotion must already be frozen *inside the object* — a still cannot let motion blur do the emo
- [22aed852b261] Use the substitution table as the core deliverable — when the script wants an emotion and no face is available, render this object at this crop. Cold palette throughout.
- [5bea8ddfb87c] **Depth-layer jobs (FG / MG / BG).** Write the prompt in three explicit depth clauses, each with a stated job. This is the engine of "reads in one glance, rewards a second" (extends `dramaturgy.md` §10 into a single still). If all three planes carry the same blur or scale, you have one plane, not three — force a sharp MG subject against a soft FG frame and a soft BG stake (shallow DOF is the panel
- [c241a02cc037] **Centerline spine, then break symmetry** — emotion: a single dominant axis (lane stripe, the Christmas Tree, a dividing wall) gives the eye a rail and makes even a chaotic frame readable; breaking it the instant one car noses ahead reads as momentum. — seen: Anderson centers for instant legibility; Bong breaks balanced staging to show a power shift. — *in a keyframe*: build one head-on symmetric 
- [921f5446334f] **Render audio as physical consequence, never as a named sound.** "Loud engine" is banned filler (`dramaturgy.md` §2) — prompt "heat-haze warp off the headers, exhaust flame, chassis squat, sidewall wrinkle" instead.
- [d5feae1b60b8] [ ] **Cold palette held** — steel/cyan/magenta/mercury-white, red and green as accents only, amber ≤15% and point-source (toxic, never cozy). One motivated source, ~70% unlit, one hard specular hit. Texture named (grain, halation, one flare), not "clean."

## video/references/camera-lighting-vocabulary.md

- [6f5a79ae61af] Use precise production language. "Cinematic" is not a direction. "35mm, slow push-in, warm window key from frame-left" is.
- [a7a4a415739c] Camera movement
- [d2fdc95e0774] Lens language
- [452aeff5a606] Light sources
- [1fdefb1f03d2] Light direction
- [a7625f9fa01e] Light quality
- [26fe42ae15f1] Color discipline
- [a2b7cd269ef9] Sound categories
- [9fb5a7cc627c] Blocking language
- [5e6379d739b9] Translating uncommon terms
- [1a3ede808e84] Transition vocabulary
- [617b9596ef1d] over-the-shoulder
- [a3c2614e6e5e] shallow depth of field.
- [84e552ce62b9] Define palette with concrete colors. Never write "cinematic colors."
- [0278247a92b4] Rules of use. Name the transition and the exact moment it fires. One transition type per cut. When the choice is open, delegate: "choose the most suitable from [natural cut / occlusion mask / match cut] for the style of this film."

## video/references/dramaturgy.md

- [4594046fc713] This is the mandatory layer. A beautiful frame without dramaturgy is wallpaper. Every prompt built by this skill must pass the dramaturgy check before it is sent to the user.
- [95308d522567] Core law. Scene formula
- [3a40b663b7a0] Second law. Details intensify emotion
- [25b46aacc27f] The three-jobs rule (what every shot must do)
- [400ac520404a] Walter Murch Rule of Six
- [9ee967da1e9e] Blocking as choreography of desire
- [d77273af9f2d] Staging controls subtext
- [24f71a932bee] Camera must have a reason
- [9a6465045388] Spatial clarity beats montage hysteria
- [5c6aa86c10f3] Environment plays
- [c5709d6c31d8] Three-layer storyboard method
- [19420f877e9d] Shot card template (14 fields)
- [e41ee886f6b0] Rhythm ladder
- [1817511ea8d5] One-anchor principle
- [33dfbb40658d] Worked example
- [bea9522cf143] Dramaturgy check before sending any prompt
- [f2664fed4b35] The scene formula tells you **what a scene is**. The Details Law tells you **how every shot must be written**. Skip it and even a perfect dramaturgical structure produces mush on screen.
- [fe8ae4c731e8] **Environmental pressure.** A physical fact about the space that carries the emotion. Cold refrigerator light. Wet asphalt. Flickering ceiling tube. Steam from the kettle. Rain on one specific windowpane. A buzzing AC unit. Tight corridor walls. Mirror reflection. (See §9 — Environment plays.)
- [291a35a705ad] **Physical micro-action on the body.** The emotion translated into the actor's body. Jaw locks. Knuckles whiten. Lips press flat. Eyes drop a quarter-inch. He swallows hard. Fingers curl against the doorframe. The actor's body is the only place where feelings render — names of feelings do not.
- [adc3e3d51477] **Sound anchor or visual motif.** A recurring perceptual hook tied to the spine of the piece. Stomach growl repeated three times. Reflection in dark glass on every transition. The same musical sting at every Crack beat. The clock's second hand. Footsteps in an empty corridor.
- [435fff89e7d5] Every shot must do at least one of three things. If it does none, delete it.
- [dbb9069efcc9] **Emotion (51%).** Does the cut honor the emotional truth of the moment. What does the viewer feel now vs. what they should feel next.
- [5d494f11d5ec] **Story (23%).** Does the cut advance story or reveal character.
- [09ecf6f81ee5] **Rhythm (10%).** Does the cut fall on a musical beat of the scene.
- [94cb46e0cdd8] **Eye-trace (7%).** Where is the viewer's gaze at the moment of the cut. Does the new shot receive that gaze naturally.
- [0cf6378a2c57] **2D plane (5%).** Does the cut respect the axis of screen direction.
- [dd109f775c6c] **3D space (4%).** Does the cut respect the geometry of the real location.
- [5b4e8d3dcda1] Good. "He edges toward the window but his shoulder stays angled back toward her, as if the conversation still holds him."
- [2be8adc698a8] Good. "Push-in starts on 'I don't know' and stops on her jaw locking."
- [c7fa86763233] Spielberg principle. Even in chaos, the viewer must know.
- [f88d89dd2268] Adjust for 30s or 15s by compressing proportionally. Never skip the Crack or the Impact.
- [6be9ddc67dea] **Eye trace.** Where the viewer's gaze should land in the first 0.3s.
- [c2e0a3b45412] Always insert at least one pause before the biggest cut.
- [01d9db058ef3] Is the scene formula complete? (desire + obstacle + geometry + gaze + rhythm)
- [75eee4c9c72b] Does every shot pass the three-detail check? (environmental pressure + physical micro-action + sound or visual motif)
- [c52b9a2cbc96] Does every shot do one of the three jobs? (change emotion, advance action, increase pressure)
- [cd71da05d199] Is there a motivated reason for every camera move?
- [e51237770b8c] Is the spatial geometry readable?
- [eba7494935d3] Are the five anchors named? (emotion, motif, object, break, final image)

## video/references/fixes-and-skeletons.md

- [f1203c349d53] Continuity checklist (before final output)
- [14470e6ae37c] Common failures and fixes
- [43f2bc69865a] Cross-model prompt skeletons
- [a06a62cee7b4] Default negative constraints
- [8bc62af4ced4] Prompt compression order
- [db96b8a465b2] Output format templates
- [4ddd5b7aae62] For Kling. Use Element Binding with 3-4 reference images (front, side, three-quarter).
- [1df0239fdbc2] For Seedance and Veo. Use positive phrasing.
- [87d2484dd6cf] Fix. Avoid style words like "hyperrealistic 8k masterpiece." These push the model into AI-art territory. Use production language instead.
- [1863ac937570] For forward extensions, the standard clause: "prohibit rigid cutting, prohibit objects appearing out of thin air."
- [d98803cf48d0] On Seedance 2.5 and Veo this is reliable. On Seedance 1.x/2.0 and Kling, also avoid mentioning any on-screen text or score you do not want — mentions summon them.
- [8f83dc97e5ba] Keep character continuity.
- [8ea66f62d954] Keep story action.
- [13635ca633f1] Keep shot timecodes (where relevant).
- [508966ae84b9] Keep lighting.
- [7dabe8b7b479] Keep camera.
- [b755a79d8702] Keep editing grammar.
- [2d6cacf87d0d] Remove philosophy and meta-commentary.
- [c485717d92a0] Remove extra adjectives.
- [f1cf3ccb4d13] Remove director references.
- [a7febb0fdf00] One ready-to-copy prompt for one generation. Use the appropriate model skeleton.
- [0f1c2fb96c3b] What breaks generation.
- [61f2696d823a] Missing direction (camera, light, continuity).
- [2a25c3da0b7a] Continuity risks.
- [179286c8c088] Model-specific mismatches (wrong syntax for the chosen model).
- [c16f3957c655] Stronger version. Rewritten prompt, ready to copy.
- [a82de4fa4979] Structured scene-by-scene JSON. Use for complex continuity. See `references/veo.md` section 6.

## video/references/kling.md

- [406d3cf655f8] What Kling is
- [e32d756b9d44] Versions and element limits
- [d85e439effb2] **Kling 3.0 — multi-shot, native audio, 15s (read first if user is on 3.0)**
- [e5e68045785e] Prompt formula (1.x – 2.x)
- [6b227126404d] Prompt length by model
- [fe84285ad428] Negative prompts (dedicated field, special rule)
- [3ed6dc5cff5c] Element Library and Element Binding (unique to 1.x – 2.x)
- [c1683b579e07] Motion Brush (unique)
- [7861ecb7da9e] Motion Control (2.6 Pro, unique)
- [ea18941fcff5] Image-to-video rule
- [b3d6ee7d8633] Failure modes and fixes
- [351002a931a9] Skeleton and example
- [0809eafc4ffb] Introduce every character and key object at the **start** of the prompt, before any shot description. Use unique consistent identifiers — the same label survives across all shots:
- [bb25b6a212a2] Each shot must answer: **framing + subject + motion**. Empty shot descriptions ("static frame, ambient mood") collapse into one continuous take.
- [71e86bdfe510] **P1. Structured naming.** Use unique identifiers per character.
- [a4313d46162b] ✓ `[Character B, clear fearful voice]: "Don't open it."`
- [9e30b0899784] **P4. Temporal control between lines.** Use linking words to prevent dialogue from merging.
- [7d81fcd5ccc0] ✓ "Character A: 'I won't ask again.' **Immediately,** Character B: 'You don't have to.'"
- [21472873e0ca] Use these terms directly — the model treats them as instructions, not flavor:
- [c9b8d9532823] In the Kling app, Master Shot presets ("Move Forward and Zoom Up" etc.) are more stable than hand-written camera prose and save credits — prefer them for standard moves, prose for motivated ones.
- [4286109b9522] If the task hits any of these — **use Kling 3.0 over earlier Kling**:
- [2fed8a69d2f5] Lip-sync required
- [87d3fe34072e] Image-to-video where text on the image must stay legible
- [8b8795ac59fd] `duration` — per-shot durations must sum to ≤ 15s.
- [eeae0374284b] For Kling 3.0, use the multi-shot structure from section 3 instead.
- [5c7946d7fd9f] Kling has a dedicated negative prompts field. The field auto-interprets input as exclusion. Do not write "no X". Write the thing itself.
- [d5c7cfa8e640] Required angles.
- [15b3f8595289] Even lighting. Avoid hard shadows. The AI can mistake them for permanent facial features.
- [7a47e689454a] A character element takes either a **3-8s video** (the model extracts both appearance and voice) or up to **4 multi-angle stills** (front, three-quarter, profile, back), plus optional **voice binding** (5-30s audio clip). Once bound, the voice belongs to the subject — do not re-describe it in the prompt.
- [d94be792c74d] Cost of the feature: several practitioners report visible image-quality degradation the moment elements/references are enabled. Use elements only when consistency actually matters; for one-off clips, in-prompt labels are cleaner.
- [0db6e0a2de52] Critical rule. The text prompt MUST match the brush motion. If you brush a river flowing and write "stagnant pond" the model tears itself apart. Align prompt verbs with brush directions.
- [1e5d66901508] Copy motion from a reference video. Use when you need specific performance or choreography (dance, martial arts, specific gait). The prompt then focuses on subject description only, the reference handles motion.
- [36686df1386d] Keep the prompt short (20-40 words). Focus only on motion. Do not re-describe static elements the model already sees.
- [7d3ab7f4ba2a] Fix. Upload 3-4 reference images to Element Library. Use Bind Elements in the settings.
- [cf73cec68544] Fix. Make shot boundaries explicit: `Shot 1 (0-3s). ... Shot 2 (3-6s). ...`. Each shot description must include a different framing or camera angle. If two adjacent shots share both framing and angle, the model merges them.
- [85c33c12c479] Fix. Strip references to the essential ones only; for one-off clips prefer in-prompt `[Character A: ...]` labels over elements. Accept the trade: elements buy consistency, not fidelity.
- [4b9361768f1a] Fix. Give each character its own element (or its own labeled identity block). Never let two speaking characters share one visual description.

## video/references/patterns-and-genres.md

- [91af7aa3fb0b] Montage patterns (6 ready structures)
- [cb4a0202d81c] Genre modules (7 archetypes)
- [407248020546] Multi-clip story structure
- [f876e8f2e5cb] Use for tension builds, reveals, dramatic emphasis.
- [5a27254127bb] Use for psychological pressure, internal conflict, impending bad news.
- [5465eb46d054] Use for revealing a hidden element, exploration, search.
- [240a672f7a78] Use for comedic or dramatic disaster. Tiny object failures play bigger than explosions.
- [5eaea7d005f0] Use for ads with a hero product.
- [4c683ca1e1ef] Use for rhythmic repetition, transformation, performance.
- [3360e40d09e2] Continuity rules (what must remain constant)
- [fae5c2bff912] Inside each 5-second prompt, use timecodes.
- [de49559afcec] Use timecoded structure for Seedance and Veo. Kling prefers flowing prose.
- [94114b6c3c86] When moving from clip N to clip N+1, the first beat of the new clip should match the final beat of the previous clip. Character in same pose. Same light. Same color temperature. This is what makes them cut together cleanly in the editor.

## video/references/race-and-speed.md

- [329b4a6f2ea8] Domain grammar for dynamic race spots — drag, drift, chase, drag-strip, kinetic montage. The brief is brutal: faces are banned, the deliverable is **still keyframes (opornye kadry)** for an animatic, and a frozen panel must read as lethal velocity at a glance. Speed is not a post effect — it is a photographic fact built from spatial cues that imply the missing motion. Emotion does not live on a fa
- [7177643306c8] Core laws (the non-negotiables)
- [7f3de462ae7d] Four schools worth stealing
- [9d8b669b963a] Selling speed in a single frame
- [d0406d8416a6] Storytelling without faces — the race captioning system
- [04df341ef39d] The race ritual (liturgy) + the 5 shot families
- [02d619120a92] Camera grammar for speed
- [cb63fe4c6da0] Light & color for speed without faces
- [7e6ed8137a3c] Sound & rhythm
- [347ccea61bf2] 30-second structure (beat map)
- [5fdf491ab509] Anti-fake guard
- [00552d374a9c] **Authentic speed, never CGI-clean or sped-up.** Build velocity into the static composition (§3); never lean on a ramp to rescue a dead frame. Over-crank, glass-smooth stabilization and post speed-ramps read subconsciously as "ad-speed" and drain all threat. Squat, lifted nose, slick wrinkle, smeared rim — the physics has to be visible in the still.
- [47dd1d977a21] **Detail is the emotion.** Faces banned, feeling renders only on a knuckle, a needle, a pedal, smoke, or a sweat bead (`dramaturgy.md` §2; the full substitution method is `animatic-keyframes.md` §5). A hand mid-grip is the no-face equivalent of a close-up on the eyes. No abstract "motion", no named feeling.
- [a2680889ec7c] **One governing visual promise per piece.** A 30s cut earns cohesion from a single conceit: everything through reflections in painted metal, or everything through circles (tach → headlight → bulb → wheel), or everything as machine-talks / no-music. Kon's "one visual principle". Name it before boarding.
- [5e64b7c7d357] **Beat-locked cutting.** Loudness in the audio = shot count on the board (§8; the density ladder itself is `animatic-keyframes.md` §3). Silence = one held panel. Bang = a burst of 4–8-frame micro-panels. Cut length is engine RPM made visual: idle = long panels, redline = collapsing panels toward the green.
- [1f3f073247b7] **Cold combative palette** (§7). Steel blue, cyan, magenta, dirty mercury-white; **red as danger accent only** (brake glow, redline, tail-lights, the Tree's bulbs). No warm cozy amber wash — warmth appears only as toxin. Steal Tony Scott's grain, contrast and overexposure; **discard his warm grade.**
- [11ae3ea96fb0] **Every insert is load-bearing.** Each detail panel must be captionable with one race label — *setup / commitment / mistake / recovery / proof-of-speed / result* (§4). If you cannot label it, it is a *fantik* (`dramaturgy.md` §3) — drop it. A board that is all proof-of-speed with no commitment/mistake/recovery is a reel, not a story.
- [611f323d3615] → **Rule:** never write "motion" — write the artifact motion leaves behind, and never board a neutral panel (every frame carries a forward vector, negative space ahead of the subject).
- [ca87c9bb0cd3] A still has no engine note and zero motion. It sells velocity through the **speed-budget rule** — a frame reads fast only when **≥3 of five cues coexist** (camera at/below bumper height · asphalt streaking the lower frame · a near foreground reference passing the edge · sharp hero against motion-blurred background · a mechanical-vibration cue). The full rule, with the anti-fake firewall, lives in 
- [be25e9cc99a1] **Long-lens compression** — the second speed register and the antidote to "only blur sells speed". Frankenheimer's 1000mm stacked distant cars onto the hero so closing distance reads as collapse. Pair compression panels with low-wide panels in the cut; never board the whole spot on one lens. In `seedance.md`/`veo.md` syntax name "motion blur, fast-shutter look on background, sharp subject" explici
- [fc4a79f80ec2] A face does four jobs: internal state, where it looks, the cost, the decision. Banned, those jobs redistribute — **decision → anatomy mid-action; internal state → an object crossing a threshold; looking/rivalry → space.** The mechanism, the EMOTION→OBJECT substitution table and the state-change cheat-sheet are owned by `animatic-keyframes.md` §5; do not duplicate them. Two filters before you draw:
- [5d1c203cbde8] (Banned panels are consolidated in §10.)
- [7a8e1fc6b5e6] **Amber logic (decision point).** Choose the **Sportsman / full tree** for an ad: three ambers fire *sequentially 0.5s apart* — three drawable keyframes, a stretched drum-roll of dread with cut length collapsing toward the green. The Pro tree fires all three at once — one panel, brutal but no build. Draw the Sportsman stagger. Always leave on the **last amber, not the green** (holeshot): the launc
- [9bf2cbf9c271] 3 | **Hard-mounted cabin shake** | Pressure / Reaction | Rigid interior mount: dash/needle/hands vibrating, mirror trembling, world shuddering through glass | visible micro-vibration; never perfectly stable
- [0e9bacb2e8ad] **Restless / handheld cam** | the frame never settles; constant threat, physiological unease | Never a perfectly level, perfectly clean panel — bake in a 1–3° drift, edge smear, off-true horizon, a faint micro-shake artifact even in a "static" cockpit | Pressure
- [98ee930c9f7c] Faces are banned, so light is the only actor left. It does not "set a mood" — it **rims a material** so a piece of metal, rubber or skin reports the emotion a face would. General light grammar (sources, direction, quality) is `camera-lighting-vocabulary.md` §4–7; the anti-sterile firewall is `animatic-keyframes.md` §7 + `universal-rules.md` U12. The race-specific governing law: *embrace the dark* 
- [2be4bcd05090] Toxic amber/sodium (rationed) | temporary, contaminated, alien — never cozy | sodium lamp as a passing smear; spilled fluid catching one lamp; the Tree's three ambers as countdown only
- [8a862f876fa8] **Warmth as toxin** is the only permitted heat: brake-disc/exhaust glow (the machine at its thermal limit), a header flame stab gone in a frame, the Tree's alien ambers, a sickly sodium smear. Any warm element must be **point-source and surrounded by cold**. If amber fills more than ~15% of the frame it has become a wash — kill it.
- [f79825c8bfa6] **Backlit smoke** [Pressure/Establish]: hard cyan or mercury-white punching *through* tire smoke from behind; volumetric shafts, the car a dark mass dissolving into glowing haze, red tail-light bleed inside the smoke for the danger accent. Front-lit smoke is dead gray nothing — always rim it from behind.
- [784a21fb3fba] **Silhouette / contre-jour** [Power/Pressure]: helmet/shoulder as pure black shape against a blown headlight or the Tree's amber bank, one thin rim defining the form plus one glint on the visor edge, no features. The brain fills the dark with something worse than any face.
- [c50591694f2a] **Texture and atmosphere.** Name the grain, never "clean": fine-to-medium film grain (heaviest in shadow), halation/bloom on hard practicals (soft glow ring + hard hot core), one anamorphic flare off the dominant source, slight chromatic fringe on the hottest edges (anti-sterile test in `animatic-keyframes.md` §7). One atmospheric pressure per panel (`dramaturgy.md` §9, Kurosawa) — backlit tire sm
- [5f835d0eb35a] You storyboard the **sound first**; the keyframes hang off it. The general law — **loudness in the audio = panel count** — and the descending duration staircase are the density ladder in `animatic-keyframes.md` §3, sitting on the `dramaturgy.md` §12 rhythm staircase. Do not re-derive them. The race-specific rhythm rules:
- [a433636c2657] **Engine as metronome.** Tie panel *duration* to RPM: idle = ~2s panels, redline = panels collapsing 2s → 1s → 0.5s → 8fr → 4fr toward the green. The board should read as an accelerating tachometer on mute. Annotate each panel with its on-screen life.
- [2d91bbc13caa] **Pull-to-intimate at the peak.** At the contest's tensest point, cut from a wide loud pass to an ECU of glove-on-shifter / breath-fog, shallow focus, void around it — engines stripped to breath only. The *quiet* panel goes *tight*; the loud panel goes wide.
- [f5ef9ac105ef] Every panel inherits a `Sound` cell even though it is a still (`dramaturgy.md` §11) — prompt the *physical consequence* of the sound (deformation, particulate, smear, heat-haze, isolation-in-void), never a named sound. Fill it.
- [19ef2dbc9666] Five phases: **ritual → staging → launch → contest → release.** Cut length escalates toward the green, the contest stays dense, one held aftermath. ~20–26 panels. Function tags from `role-modes.md` §4. This is the structural skeleton; for a fully worked, panel-by-panel deliverable board of this exact structure (format C, ~13 rows), use `animatic-keyframes.md` §8 — do not draw a second worked board
- [de0ddf9ca295] Allocation: plot the board as a descending duration staircase, broken only by the one pre-launch held panel (the single most-held still, most negative space) and the one post-finish hold. The launch is *never* one hero frame — fan it into the 6–9-panel micro-burst. No two bang-clusters touch; every burst is separated by a held quiet panel.
- [b4e9fb037f88] The race-specific list of panels that kill credibility — do not draw. (The general per-panel earns-its-place checklist is `animatic-keyframes.md` §9; run that on every panel as well.)
- [54d1d74f3df8] [ ] No banned panel: static fetish insert (lever/badge/wheel with no verb, no state-change); anatomy at rest; a detail you cannot caption with a §4 label; all-proof-of-speed board with no commitment/mistake/recovery; decorative dashboard clutter (keyring, dice, coffee cup — "each object is a clue"); warm wash without narrative function.
- [1948fb0cd2ea] Before sending the board, run `animatic-keyframes.md` §9 (per-panel master checklist), `dramaturgy.md` §15 and `universal-rules.md` §13 over it. The most-violated step is the three-detail check — do not skip it.

## video/references/role-modes.md

- [0228eb6fc32a] Director mode
- [bc65d00b7648] Screenwriter mode
- [84f2cd5a378b] Shot function taxonomy
- [cedacf95ce49] Every shot must answer at least one of these questions. If a shot answers none, delete it.
- [5c79b70fbb5a] What does the viewer need to notice?
- [e47d5852520a] Use one dominant director reference per scene. Translate into concrete camera, light, rhythm, blocking. Never stack three or more references.
- [d92564e28fe4] Translate every beat into physical action the camera can see. Tag each beat with a shot function (see section 4). Every beat must have subtext.
- [9570d85c5b8a] Every beat should carry at least one function tag. This is the editor's grammar.
- [85f471342e23] A montage sequence can compress or loop. Use function tags to keep the structure readable even at high speed.
- [a84829cef94a] Each tag is also a question the shot must answer. Establish. Where. Power. Who commands. Pressure. What pushes. Detail. What to notice. Reaction. What it cost. Shift. What changed inside. Impact. The moment. Aftermath. The residue. Exit. The image carried out.

## video/references/seedance-25.md

- [16d0138b736d] What 2.5 changes
- [8b8c0d1dbc74] Specs and hard limits
- [30d2f5eff0ad] Official prompt formula
- [8313a9a24b34] Syntax markers for audio, dialogue and text
- [b8eee7f2f8e2] Reference discipline (the 50-slot system)
- [cbefd0f56511] The 30-second structure: stages and end states
- [b91733d06e56] The anti-collapse skeleton (3 modules)
- [c02c4d796066] Realistic human formula (anti-AI-face)
- [a7f7eaa6494a] Camera language
- [75c045746d55] Physics through consequences and triggers
- [6fc796f8b7ef] Video editing (partial re-render)
- [365c648ba098] Video extension
- [36dccaf6ebb2] Ultra Long mode (30-180s)
- [0d171a59aa6e] Blockout and green screen
- [0130710f74ef] Storyboard grids and keyframes
- [813d4456baa4] Failure modes and fixes
- [c9f0f1f54765] Economics and model choice
- [521bfa52222b] Worked examples (official, verbatim)
- [dc069aea561b] Generation parameters (duration, aspect ratio, resolution) are set on the generation page or via API — **they do not belong in the prompt**. The 1.x/2.0 CLI tail (`--resolution ... --duration ...`) is not 2.5 syntax. Exception: in Ultra Long mode, restate duration and ratio at the top of the prompt.
- [3c3a35bd5003] **Global tail.** Re-state the must-hold globals (camera position, environment, sound, lighting) and repeat the global bans.
- [fe2010e7cd1e] 2.5 has dedicated markers. Use them — do not describe audio in loose prose:
- [5090be9f2dcb] The point of 50 slots is not dumping assets in. **Every material's role must be written in the prompt.** Do not rely on text labels inside images; do not make the model infer mappings.
- [f4e68628a21b] **Bind each subject individually.** `<Character A> corresponds to @Image 1. Use only the appearance, hairstyle, and clothing.` The officially forbidden pattern: "@Images 1 through 4 define four characters respectively" — it never states which is which.
- [1a73cf483aab] **Add exclusions** for anything that could bleed in: "Do not use the image background." / "Do not use the people in the image." / "Do not use the person's identity, clothing, or scene from the video."
- [8acb235535b4] **Do not restate what a reference already defines.** If a reference video defines the motion, state only which attributes to inherit — re-describing every action conflicts with the reference.
- [9d8033a7fcbb] **Select references per scene**, not all at once: `Scene 1 | Use: <list>. Event: ... End state: ...`
- [58c03455aad2] Divide the clip into consecutive stages. **One primary state change per stage, and always state the visible end state** — the end state is what the model steers toward (this is the U11 final-image rule, per stage).
- [7e710b7de286] A time range is an event's **time budget, not an edit point**. Ranges must be consecutive and non-overlapping.
- [2976ffd881f1] **One core action + one camera move per window.** Do not demand frequencies ("three actions in one second").
- [83694d17ac4b] **The prohibition list is specific, not generic.** From the official farewell example: "No exaggerated crying, no fast cuts, no large body movements, no extra dialogue, no BGM, no runny nose, no premature dropping of tears." Ban the exact ways this scene can collapse.
- [4340f22ac789] Always attach the incantation: **"prohibit rigid cutting, prohibit objects appearing out of thin air"** — it is the official anti-jump-cut clause, repeated in every transition template.
- [b93895a69273] Order-gate effects that must not fire early: "The ink-wash effect must only appear AFTER 25 seconds, triggered by the 'click' sound — absolutely no premature appearance."
- [e56653bec670] **Declare the physics regime up front.** "Rain reflections on metal, water splashed by tires, and the specular refraction of exhaust flames must strictly obey real-world physics."
- [809f55027421] **Narrate consequences, not just actions.** Tires kick up water curtains; the impact shatters the bridge into a spider-web pattern; the shockwave blows the rain away in a ring. Action chains where each step forces the next ("hand grips jar → lid actually unscrews") double as QA — a broken chain exposes a failed generation instantly.
- [8870a91220dc] **Negatively constrain the known failure.** "No soft-body or mollusk-like twisting of the mecha structure (must maintain metallic rigidity)." "The amber stays attached to the palm and must not clip through the fingers."
- [5e9381b1532d] **Gate events on triggers.** "Three seconds after she presses the button..." / "only when he says {now}..." — triggers beat raw seconds for anything tied to performance.
- [8dd832a85896] Any clip ≤30s extends by 4-30s per pass, nested repeatedly, **hard ceiling 60s**. The new prompt applies only to the appended segment; original frames are untouched. Required verbs: extend forward / extend backward / continue.
- [324bcf02f62b] Backward (prepend a beginning): describe the preceding events, then define @Video 1's **first frame as the extension's explicit end state**. Gotcha: materials that belong to the source video only must be flagged — "<X> must not appear early in the backward extension" — or later characters leak into the past.
- [3cc2915d07c9] Community-proven minimal extension prompt: "Extend the video. Keep character identity, facial structure, body proportions, lighting, art style, and the space fully unchanged. Only change camera movement; do not redesign character or action."
- [f0315e2411a6] **Timestamped** (1-minute ambient pieces): windowed beats with per-window bans — "0-20s (quiet opening): fixed camera... no shake, no characters enter, hard cuts prohibited."
- [ed4fbf774ee8] **Coarse blockout** — primitive geometry as a "dynamic skeleton" (trajectories, blocking, camera path, cuts, light changes). **Map every primitive to a reference**: "The tall cylinder in @Video 1 corresponds to <Guide>. The rectangular block corresponds to <Display Cart>." Exclude the render style: "Do not use its gray geometry or empty scene." Best practice: **no limbed or winged models in coarse
- [7887bf99374c] **Fine blockout** — complete 3D animation; the model re-renders materials, color and style only: "@Video 1 is a fine blockout reference. Preserve structure, action, spatial layout, camera position, camera movement, and cuts. Do not use its original gray materials or empty background. Re-render <subject> as <final subject>..." **Clean the viewport capture first**: remove path lines, coordinate axes
- [c8f9182dab48] **Storyboard grid as input**: one image, ≤15 panels official (practitioners have pushed 50), clean line art, minimal text. Declare the reading order and exclude the style: "@Image 1 provides a 12-panel storyboard grid for shot order and approximate composition. Read it left to right, top to bottom. Do not use the grid's line-art style, text labels, or placeholder characters." Then `Shot 1: ... Sho
- [dbf4503191cb] **Multi-keyframe sequences**: "Use @Image 1 through @Image N as keyframes in this order", one key state per image. Independent images align better than a grid. Keyframes control stage order and key states, not exact frames.
- [884b4b40911e] **First + last frame** works inside omni-reference mode — declare each anchor separately ("@Image 1 is the first frame... @Image 2 is the last frame..."), never jointly. Same aspect ratio required.
- [877300b2ba56] Fix. Per-subject binding (section 5) + explicit differentiation: "Their movements are not synchronized. Clothing colors, hairstyles, and facial features must all be distinct. No identical clones in the background."
- [3b48069bb705] 2.5 errs by commission: it completes more instructions than rivals but may cut freely even when told "one continuous take". Fix. "One continuous shot, no cuts of any kind" + a camera path that never motivates a cut; if montage keeps leaking in, drop to a 10-15s window where one-takes are stable.
- [6eafd4ebaa95] Costs are real: a 30s/720p generation on Jimeng runs ~500-700 credits. Production budgets must assume re-rolls, extensions and segment reshoots — fix with edit/extend/reshoot instead of full regeneration whenever possible. Draft at 480p, finish at 720p.

## video/references/seedance.md

- [bf04722fb2d7] What Seedance is
- [379e62884da3] Versions and specs
- [72c2aed0f513] CLI parameters (1.x / 2.0 only)
- [9aaa76a80841] The Details Law (read first)
- [cf0aa2c21b81] 6-step prompt formula (quick)
- [a624dc423b7d] Production-grade skeleton (11 blocks) — for dramatic / multi-shot work
- [1c02614a3e4f] The 5-second shot timeline (rhythm template)
- [ba9e08cfe115] Multi-shot syntax (unique capability)
- [d2ca29dc370a] Anti-mush guard block (when Seedance smears the cuts)
- [aa26f1234c80] `@img1` character reference syntax
- [3830b43ea337] Camera movements (9 presets)
- [805acf614f43] Negative prompts handling
- [c0ec18d3a206] Image-to-video rule
- [f561578ec058] Audio (1.5+)
- [c1ff7a4810db] Failure modes and fixes
- [20840c83ede1] Worked example. 15-second tragicomedy as 3 × 5s clips
- [5e727274f86e] Seedance 2.5 → read `seedance-25.md`
- [0395ddb6bd06] **Not 2.5 syntax.** On 2.5, duration / aspect ratio / resolution are set on the generation page or via API and do not belong in the prompt (exception: Ultra Long mode restates duration and ratio at the top — see `seedance-25.md` §2).
- [73905921cedf] Seedance does not render abstractions. It renders **physical specifics**. Every adjective must be a sensory fact. Every emotion must be a body. Every shot must own at least three concrete details:
- [a78b8143dfae] **One environmental pressure.** Cold blue refrigerator light. Steam off boiling water. Wet asphalt. Flickering fluorescent. Dripping tap. Curtain breathing in the AC.
- [809fb4ebddce] **One physical micro-action.** Jaw locks. Finger taps the counter. Knuckles whiten on the fork. Lips press into a line. He swallows hard.
- [659a2eb38201] **One sound anchor or visual motif.** Stomach growl at 2.3s. Reflection in the dark phone screen. Rain hitting the same windowpane.
- [ae09790a4e9b] Banned, lazy phrasing that produces mush:
- [e30cec365a82] Write in full sentences, not tags. Seedance prefers clear grammatical prose. For dramatic / multi-shot / character-locked work, **use the production-grade skeleton in section 6 instead.**
- [2d5229cb5344] Use this for any dramatic piece, multi-shot ad, music-video segment, or character-locked clip. Each block answers a specific failure mode. Skipping a block reintroduces that failure.
- [b9c780304835] For a 5-second multi-shot clip, the model performs best with **5 shot beats** following a dramatic micro-arc. Use this timing as the default scaffold:
- [c6a20928bc70] Seedance reads explicit cut markers inside a single prompt and generates distinct shots connected by visible cuts. This is its strongest card. Use it when you need montage in a single generation.
- [c3c3d1047037] Use 2-3 shots per 5-second clip for tight cinematic montage, 4-5 shot beats only when each beat is short and physically distinct (see section 7). Hard cap: 5 shots per generation — beyond that the model drops or compresses shots. Size the duration to the shot count (4 shots need 10-15s, not 5s). Every shot must share an anchor with its neighbors — same character, same location, or same lighting re
- [d629ec5811b5] Seedance 2.0 accepts image references inline using `@img1`, `@img2`, etc. Use this to lock the protagonist's likeness across all shots in a multi-shot clip and across multiple stitched clips.
- [e57740e558ac] The full identity block must follow the `@img1` mention. The model needs the textual description as a backup signal — the image alone drifts.
- [80e69a894fcc] Workaround for 1.x/2.0. Always invert to positive phrasing. Instead of "no yellow tones" write "cold blue-gray palette with desaturated skin tones." Instead of "no distorted hands" write "anatomically correct hands with clear finger separation."
- [a75221469baa] **Seedance 2.5 fixed this.** Direct bans are reliable: "pure video, no subtitles, no background music" actually suppresses them, and specific prohibition lists ("no exaggerated crying, no fast cuts") are a core part of the official 2.5 prompt structure. See `seedance-25.md` §7.
- [71fec8821328] When using a reference image, DO NOT describe elements already visible in the image. The model sees it. Describe only motion and camera work. Re-describing static elements creates identity drift.
- [6b50e2278180] Dialogue goes in **double quotes** on 1.5/2.0 — the model voices it, generates the voice and syncs lips to the cut. State the delivery: "Play her line dry and a little proud, his quiet and worn out." **On 2.5, use the dedicated markers instead**: dialogue in `{ }`, SFX in `< >`, music in `( )`, titles in `【 】` (see `seedance-25.md` §4).
- [f1f0fcdff995] Fix. Add explicit "Cut to" markers. Say "multi-shot sequence with visible hard cuts. Do not generate a single continuous take."
- [27ee9fc25b00] Fix. Use positive substitutes. Seedance 1.0 has no negative parser.
- [f4c2c207fbb8] Fix. Apply the Details Law (section 4). Audit your draft: every shot must have one environmental pressure, one micro-action, one sound or visual motif anchor. Replace adjectives like "dramatic", "intense", "beautiful" with concrete physical facts.
- [e7caec8627aa] After the 2026 deepfake crackdown, 2.0 aggressively filters human faces, helmets, sunglasses, and anything resembling protected IP or celebrity likeness. Fix. Route face-heavy drama to Seedance 2.5 (realistic humans are its headline feature), 1.5 Pro, Kling, or Veo; keep 2.0 for scenes, architecture, product and montage work. Use only owned or synthetic character references — the IP/celebrity filt
- [31550b84c066] A 15s narrative is **never** one prompt. It is three self-contained 5-second prompts, each with the full character lock, the full visual style, the full audio block, and a different dramatic function. Stitch in the editor.
- [dd071e4f1adc] For dramatic, multi-shot, character-locked, or stitched-clip work — always use the 11-block production-grade skeleton from section 6.

## video/references/universal-rules.md

- [1eff4afae0c5] The non-negotiable. Details intensify emotion (Details Law)
- [f8bede714bb2] U1. Universal prompt skeleton
- [2aaa9e213f3c] U2. Weight-at-start
- [bc20f5aff1a0] U3. Show don't tell
- [4da3a01386c8] U4. Natural language beats tag spam
- [ea5fe60a475b] U5. One primary camera move per shot
- [bfd5925d781c] U6. Precise lens language
- [59e3586c0672] U7. Character consistency anchor
- [2dbc39baa120] U8. No contradictions
- [6fe216acd414] U9. Concrete physical detail over abstract concept
- [af2fe5419c45] U10. Duration discipline
- [f768d100f368] U11. The final image rule
- [8d89d14b9f2b] U12. The three-detail check (audit before sending)
- [c5205558e796] U13. Reference role discipline
- [a8c92c01fd2f] U14. Priority declaration
- [90c9d01c7da9] **One environmental pressure.** Cold blue refrigerator light. Steam off boiling water. Wet asphalt. Flickering fluorescent. Dripping tap. Curtain breathing in the AC. (Kurosawa: weather is a character. See `dramaturgy.md` §9.)
- [3da18291f908] **One physical micro-action.** Jaw locks. Knuckles whiten on the fork. Lips press into a line. He swallows hard. Fingers curl against the doorframe. (Show, not tell — the body is the only place where feelings render.)
- [01e778de1f4c] **One sound anchor or visual motif.** Stomach growl at 2.3s. Reflection in a darkened phone screen. Rain on the same windowpane. A single fluorescent flicker before each cut.
- [d9efc3ad4bfb] Words that do not render and mark the writer being lazy:
- [a4cd347f4b1e] Do not stack three camera moves in a 5-second clip. Pick one dominant move (dolly-in, pan, tracking, static). Layer a subtle micro-adjustment if needed (slight handheld shake, gentle rack focus). More than that produces visual chaos.
- [c1d814f8c059] Identity block must include: face shape, eye color, skin tone. Hair color, length, style. Facial hair. Exact clothing items. Distinctive accessories.
- [e24b10c311e9] "Loneliness" does not render. "A man sitting alone, shoulders collapsed, face lit by blue phone glow, empty bottles on the table" does.
- [9373adbe6c11] Most models work in 5-10 second clips. Longer narratives live in multiple clips stitched in the editor. Do not cram a 30-second story into a 5-second prompt.
- [adbe90385564] Before returning the final prompt to the user, audit every shot. Each shot must carry at least one of each:
- [75ec08f6c7e0] Environmental pressure (lighting, weather, surface, sound of the room).
- [6f2d9a2fd7ba] Physical micro-action on the body (jaw, hand, breath, eye, gesture).
- [e2b9c51c5ef7] Sound anchor or recurring visual motif tied to the emotional spine.
- [f7ff7d98a4a9] If a shot has zero, fix it before sending. If a shot has only one, ask whether you can make it two without bloat. The strongest prompts in this skill's worked examples always have all three.
- [51c07299485c] Wherever a model accepts reference assets (Seedance `@Image/@Video/@Audio`, Kling Element Binding and Omni references, Veo ingredients), **every asset gets an explicit role written in the prompt**: what it defines (appearance, motion, voice, scene, camera path) and what to ignore ("Do not use the image background", "Do not use the people in the image").
- [2e0a56484152] Bind each subject individually: "<Character A> corresponds to @Image 1 — use only the appearance, hairstyle, and clothing." Never the collective form "@Images 1 through 4 define four characters respectively" — it does not state which is which.
- [21023b368ec1] Do not restate what a reference already defines. If a video reference carries the motion, name only the attributes to inherit; re-describing every action fights the reference.
- [d1794addd647] The core subject that must survive every shot.
- [0196c3f7220c] The key shots that must appear.
- [da70b123efd4] The transitions where the model may freestyle.
- [e21763705dd8] The mandatory final frame.

## video/references/veo.md

- [f537cf5a3aea] Versions and specs
- [12a578676a61] Prompt structure and length
- [a60c5e0dfaba] Dialogue syntax (critical, unique)
- [8350ec6bf0fe] JSON prompts (powerful, unique)
- [8c412614e361] Image-to-video (Veo 3.1)
- [5b62ebcc0fbf] Reference ingredients (3.1)
- [8cd72c333780] Failure modes and fixes
- [60e1c0dd065d] Skeleton and example
- [dfcbb6dd0684] Use labels `Audio:`, `Says:`, `SFX:` to separate sound direction from visual direction. The model needs an explicit signal that audio should be generated.
- [a45ee38936f8] Veo parses structured JSON. This prevents "concept bleed" where describing mood accidentally changes object colors. Use JSON for complex scenes with strict continuity needs.
- [01a57763de37] Complex props that must stay the same color and size.
- [1c400db686fb] Do not re-describe static elements.
- [402a936cf3fe] Use when you need a specific character in a specific place with a specific object.
- [1a0831f5ce00] Fix. Add explicit `Audio:`, `SFX:`, or `Says:` labels. Do not assume the model will infer audio from visual description.