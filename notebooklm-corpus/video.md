# SKILL: video

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: video/SKILL.md

---
name: video
license: CC-BY-4.0 (attribution required — Serge Shima, github.com/smixs/visual-skills)
description: Use this skill whenever the user asks to create, improve, audit, or split prompts for AI video generators (Seedance, Kling, Veo, Runway, Luma, Pika, Sora, any image-to-video system). The skill also covers storyboards, shot lists, director treatments, dynamic montage, multi-clip story structure, camera direction, lighting, blocking, pacing, character continuity, dialogue, and sound design. Trigger even when the user says things like "придумай сцену для видео", "разбей на склейки", "сделай раскадровку", "улучши промпт для Kling", "переведи сценарий в промпты", "как снять X в AI-видео", or shares a prompt and asks to fix it.
---

# AI Director, Screenwriter & Editor

Hybrid role. You direct (see frame, emotion, motivated camera), write (build beat, action, consequence, final image), and edit (cut rhythm, protect continuity, drive montage). Prompt engineering is fourth — it serves the first three.

A beautiful frame without dramaturgy is wallpaper. A dramaturgically clean prompt without details is mush. The whole craft of this skill lives in the reference files. The body of this SKILL.md is intentionally thin so you cannot fake a result by reading it alone.

## Route first — is this actually a video-prompt task?

- **No idea or script yet** (user wants a concept, a Big Idea, a campaign, an ad scenario — not a prompt): if the `creative-director` skill is installed, start there — it develops ideas and scripts for commercials and beyond ([github.com/smixs/creative-director-skill](https://github.com/smixs/creative-director-skill)). Come back here once there is a script to shoot.
- **Still keyframes, character sheets, animatic panels** to feed the video pipeline: use the sibling `image` skill, then return with the keyframes.
- **A script or scene exists and needs prompts** — this skill. Continue below.

---

# Mandatory reading order — DO NOT WRITE A PROMPT WITHOUT THIS

Past attempts to write prompts directly from this skill body produced lazy, mush-prone results. The fix is structural: the process lives only in the reference files, and you load them in this order before producing output. Skipping a step **silently** degrades the result — the model cannot tell that a shot is wallpaper, only the writer can, and only by applying the rules from these files.

For every video prompt request, load the files in this order:

### Step 1 — always read first → [dramaturgy.md](references/dramaturgy.md)

Scene formula. Details Law (the second core law, most violated). Murch Rule of Six. Three-jobs rule. Five anchors. Blocking, staging, environment as pressure. Three-layer storyboard. 14-field shot card. Rhythm ladder. Dramaturgy check.

You cannot decide whether a prompt is ready without running the dramaturgy check from this file.

### Step 2 — always read second → [universal-rules.md](references/universal-rules.md)

U1–U12 universal rules that apply to every video model: prompt skeleton, weight-at-start, show-don't-tell, lens language, character anchor, contradictions, duration discipline, final image rule, three-detail check.

### Step 3 — pick the model and read **one** model file

Use this short selector. The full reasoning is in the chosen file.

| Cue from the user / task | Read |
|---|---|
| Seedance, ByteDance, Doubao, Jimeng, multi-shot in one clip, `--resolution`, `--duration`, `--camerafixed`, "Cut to", `@img1`, fast multi-shot drama | [seedance.md](references/seedance.md) |
| **Seedance 2.5 production work**: 30s single-pass, 50-slot reference kits, video editing / partial re-render, extension, Ultra Long (30-180s), 3D blockout / green screen, `@Image N`, `{ }` dialogue markers | [seedance.md](references/seedance.md) **+** [seedance-25.md](references/seedance-25.md) |
| Kling, Kuaishou, Element Binding, Motion Brush, Motion Control, dedicated negative prompt field, **Kling 3.0 multi-shot with `[Character A: ...]` labels, native dialogue + lip-sync, 15s, Turbo (cheap lip-sync), Omni (references + editing, 4K)** | [kling.md](references/kling.md) |
| Veo, Google video, dialogue / lip-sync, JSON prompts, synchronized SFX, commercial polish with voiceover | [veo.md](references/veo.md) |

Default if nothing in the request hints at a model:
- Multi-shot narrative or fast montage drama → Seedance, or Kling 3.0 if dialogue is involved.
- Dialogue / commercial polish / synchronized SFX → Veo, or Kling 3.0 for multi-character dialogue scenes up to 15s.
- Character consistency across many social clips → Kling 2.6 Pro (cheaper) or Kling 3.0 (with in-prompt `[Character A: ...]` labels).
- 10-15s continuous narrative with audio → Kling 3.0.
- 15-30s continuous single-generation arc, heavy reference kits (up to 50 assets), editing or extending existing footage, 30-180s long-form → Seedance 2.5.
- Face-heavy drama → Seedance 2.5 (realistic humans + lip-sync are its headline feature), Kling, or Veo. On a 2.0-only pipeline route faces to 1.5 Pro (2.0 filters human faces aggressively).

For a more detailed comparison (max clip length, audio support, character lock methods, motion brush, etc.), read the model file you picked. Do not load all three.

### Step 4 — task-shaped reading (load only those that match)

- Storyboard / shot list / director treatment / "разбей на склейки" → [role-modes.md](references/role-modes.md). Determines whether you operate as Director, Screenwriter, or Editor for this turn.
- Storyboard keyframes / опорные кадры / аниматик / animatic / still panels / key visuals to pitch a sequence → [animatic-keyframes.md](references/animatic-keyframes.md). The general method for turning a beat sheet into still panels (and then image-gen prompts) that read as story, drama and emotion without motion or faces.
- Race / drift / drag / chase / speed / dynamic / kinetic montage, "гонщик", "раскадровка гонки", authentic-speed spot → [race-and-speed.md](references/race-and-speed.md). Specializes `animatic-keyframes.md` for the race domain — read that file first.
- Commercial, music video, drama, action, fashion, UGC, product film, escalation / anxiety / discovery / catastrophe / product-drama montage → [patterns-and-genres.md](references/patterns-and-genres.md).
- Multi-clip continuity, fixing a broken prompt, known failure modes (one-take, face drift, melted hands, dialogue too fast) → [fixes-and-skeletons.md](references/fixes-and-skeletons.md).
- Need precise framing / lens / movement / light / sound terms → [camera-lighting-vocabulary.md](references/camera-lighting-vocabulary.md).

If none match — proceed with steps 1-3 only.

### Step 5 — apply the dramaturgy check and the three-detail check

Before returning anything, run both checks:

- Dramaturgy check (`dramaturgy.md` §15): scene formula complete, three-detail check on every shot, three-jobs rule on every shot, motivated camera, readable geometry, five anchors named.
- Three-detail audit (`universal-rules.md` §13): each shot owns environmental pressure + physical micro-action + sound or visual motif.

If any shot fails, fix before sending. This is the step the user has had to enforce repeatedly. Do not skip it.

---

# Output

Choose the format the request actually asks for. Default to **A** if unclear.

- **A. Single prompt.** One ready-to-copy prompt for one generation. Lead with model name + parameters in a short header.
- **B. Multi-clip prompts.** Sequence of self-contained prompts, each repeating the full identity / style / continuity block (see `universal-rules.md` U7).
- **C. Storyboard.** Table — Time, Shot, Function, Action, Camera, Light, Sound, Emotion. Every row is a 14-field shot card from `dramaturgy.md` §11, compressed.
- **D. Prompt audit.** Given a user prompt, return: What works, What breaks generation, Missing direction, Continuity risks, Model-specific mismatches, Stronger version (rewritten prompt).
- **E. Director treatment.** Core idea, Emotional arc, Visual motif, Rhythm, Camera language, Lighting, Sound, Ending image. (Treatment ≠ prompt.)
- **F. JSON (Veo only).** Structured scene-by-scene continuity. See `veo.md`.

Default output language follows the user. The final AI prompt itself goes in English unless the user asks otherwise — Seedance, Kling, and Veo all perform better in English.

---

# Final response style

Prefer: ready-to-copy prompts, clear section labels, production language, motivated camera and light direction, strict continuity blocks, model-specific syntax, direct fixes.

Avoid: long theory unless asked, academic lectures, vague inspiration, decorative jargon, "cinematic masterpiece" filler, prompts without camera and light, prompts without continuity, stacking more than two director references, abstract emotions without physical translation.

When in doubt about a model-specific detail — re-read the model file before writing the final prompt. It costs nothing and prevents bad output.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/animatic-keyframes.md

# Keyframes for an animatic (opornye kadry)

This is the still-panel layer. A storyboard keyframe is not a frame grab of footage — it is a single drawn image that must carry one story-beat with **no motion and (usually) no face**. The animatic hangs off these panels. A panel that only looks good is wallpaper; a panel must report its story function, its drama, and the motion it cannot show, all frozen.

This file converts a beat sheet / treatment into **opornye kadry**, then into image-generation prompts. It sits on top of `dramaturgy.md` (§2 Details Law, §10 three-layer method, §11 shot card, §12 rhythm ladder, §15 check) and `universal-rules.md` (U1 skeleton, U11 final image). Pairs with `camera-lighting-vocabulary.md` for framing/lens/light tokens, `role-modes.md` §4 for the function taxonomy, `patterns-and-genres.md` (Action genre, Escalation pattern) for the spatial-clarity spine, and `seedance.md` / `kling.md` / `veo.md` to animate each locked frame. Output stays compatible with Storyboard format C: `Time | Shot | Function | Action | Camera | Light | Sound | Emotion`.

The running brief through every example below: drag/drift race spot, cold combative palette (steel blue, cyan, magenta, mercury-white; **red and green as accents only**; amber only as the start-tree's alien pulse or a toxic spill), faces absent or unusably fragmented. Swap subject as the task demands — the method holds.

## Contents

1. What an animatic keyframe must do
2. The keyframe card (a still extension of the shot card)
3. How many keyframes per beat (density ladder)
4. Composing a still that reads as MOTION
5. Emotion without faces in a still
6. The loaded frame for one panel
7. From keyframe to image-gen prompt
8. Worked keyframe board for a 30s race spot
9. Checklist: does this keyframe earn its place

---

## 1. What an animatic keyframe must do

In an animatic the **panel is the unit, not the shot.** A shot has duration, motion, and sound to carry its function across time. A keyframe has one frozen image and must carry the same function in a single glance. So every panel does four things at once, in one still:

- **One readable story-beat** — name it in one sentence before generating. If you cannot, the panel is not ready (`dramaturgy.md` §1).
- **One function tag** — Establish / Reveal / Power / Pressure / Detail / Reaction / Shift / Impact / Aftermath / Exit (`role-modes.md` §4). The tag is the question the panel answers. In a faceless spot **Reaction** is reassigned from a human face to the *machine's* face — the needle jumping, the slick wrinkling, the nose squatting. Treat gauges and rubber as the actor.
- **One emotion** — routed through metal, rubber, light, or anatomy, never named (`dramaturgy.md` §2). Mixed signals = no signal.
- **One implied motion** — the movement the still cannot perform, frozen as its physical residue (§4).

A panel that carries a beat, a function, an emotion, and an implied motion earns its place. A panel missing any of the four is a *fantik* — wrapper without candy (`dramaturgy.md` §3). The discipline of this whole file is: **you cannot prompt "motion" or "emotion" into a still — you prompt the physical consequence each leaves behind.**

---

## 2. The keyframe card

The shot card in `dramaturgy.md` §11 describes a moving shot. A keyframe needs a *still*-specific card: every field describes a frozen image, and three fields are new (implied camera, emotion-via-object, motion-rendered-as-still). Fill every field before generating. Empty fields reveal missing direction.

```text
KEYFRAME CARD
- Panel ID.            01, 02, 03
- Timecode.            on-screen life in the animatic (e.g. 0:10.5, HOLD 2s)
- Function tag.        Establish / Reveal / Power / Pressure / Detail /
                       Reaction / Shift / Impact / Aftermath / Exit
- Beat.                what changes in the story in this one still
- Framing + lens.      ECU / CU / MCU / wide / macro insert / POV + lens token
                       (24mm immersive ... 100mm macro — camera-lighting-vocabulary.md §3)
- Subject / anchor.    the ONE object or anatomy the eye lands on in 0.3s
- Depth layers.        FG job (frame / obstruct / put us inside)
                       MG job (the subject / the act)
                       BG job (stakes / context / rival)
- Implied camera.      the move this still is the first frame OF
                       (push-in, whip, bumper-POV, joust) — what it would do if it ran
- Light + palette.     one motivated source + direction + the surface it rims;
                       concrete colors, amber-ban repeated
- Emotion-via-object.  the feeling a face would show, mapped to an object's state (§5)
- Motion-as-still.     which frozen cue carries the missing movement (§4):
                       smear / partial blur / streak / vector / sharp-blur / held stillness
- Caption / label.     one word: setup / commitment / mistake / recovery /
                       proof-of-speed / result
- Sound.               what audio sits under the held frame, where the cut bites
                       (fill even though it is a still — dramaturgy.md §11)
- Production note.      prop, rig, continuity anchor
```

The card maps straight onto format C: `Function`, `Framing`, `Implied camera`, `Light`, `Sound`, `Emotion-via-object` become the table columns. The three still-specific fields — **implied camera, emotion-via-object, motion-as-still** — are the ones a normal shot card does not force you to name, and they are exactly the ones that keep a panel from going flat.

---

## 3. How many keyframes per beat — the density ladder

**Loudness in the audio = panel count in the board.** Silence gets one held panel; a bang gets a burst. This is the still-panel reading of `dramaturgy.md` §12 (rhythm ladder) and `role-modes.md` §3 (editor density: 3-4 beats/5s drama, 4-7 narrative, 6-9 fast montage). The full 30s beat map is the worked board in §8; split it per `patterns-and-genres.md` §3 (30s = 6×5s).

| Beat | Density | Panels | Why |
|---|---|---|---|
| **Ritual / staging** (quiet) | 1 hero panel, held | 1 panel living 1.5-2.5s | A silent beat is monolithic. Do not subdivide it — its power is that nothing moves while the world holds its breath. One symmetric "breath" frame, most negative space, least motion. |
| **Pressure climbing** (amber stagger) | escalating singles | 3 panels, collapsing length | The Sportsman tree fires three ambers 0.5s apart — three drawable panels, each tighter than the last, cut length collapsing toward the green. |
| **Launch / impact** (bang) | 3-panel micro-burst → up to 6-9 | 6-9 panels at 8fr → 4fr | The audio bang is rendered as panel *density*, not one big image. Hip-hop montage: bumper-POV smear, side wheelspin, tach flare, clutch hand, lane-stripe strobe. |
| **Contest** (sustained roar) | alternating | fragment-cluster ↔ one held detail | Never two bang-clusters back to back. Between every burst, one held quiet panel — loud only works next to quiet. |
| **Aftermath / exit** (cut to silence) | 1 hero panel, held | 1-2 panels, ~2s hold | End on consequence, not explanation. One held still: drifting smoke, hand unclenching, car nosing into dark. |

**Allocation rule.** A 30s spot lands at ~18-26 panels. Plot the board as a descending duration staircase (≈2.5s → 0.5s → 4fr), broken only by the one pre-launch pause and the one post-finish hold. The board should *read* as an accelerating tachometer even on mute. Give a beat a micro-burst only when the audio detonates; everywhere else, one panel that holds is stronger than three that scatter.

---

## 4. Composing a still that reads as MOTION

A keyframe cannot ramp, cut, or whip. Each missing move resolves into one of **six frozen cues**. Never write "motion" — write the artifact motion leaves behind. State the cue in the card's *Motion-as-still* field and again in the prompt's camera/light clause; models default to over-clean stabilization and will sand the speed off unless told (§7).

| Cue | What it is in a still | Renders the implied move |
|---|---|---|
| **Directional motion-blur smear** | Background streaked along the travel axis, subject sharp. Guardrail, lane stripes, tree lamps pulled into horizontal light-rods. | tracking pass, POV launch, the whip-pan aftermath |
| **Frozen partial blur** | One moving element blurred (tyre sidewall, smoke bloom, shift hand mid-throw) while the anchor stays crisp — proof of a single arrested instant. | speed-ramp peak, launch, shift |
| **Streak-frame (implied whip)** | The whole panel raked into motion-streaks with one readable shape surviving (a wheel arc, the shifter) — a "between two shots" blur panel. | whip pan, transition beat |
| **Posture / trajectory vector** | A body or car locked in a pose that can only resolve forward — wrist cocked over the shifter, front wheels lifting, weight slung onto the rear axle. The eye finishes the move. | charged pose, freeze frame, launch |
| **Sharp-subject / blurred-field separation** | Shallow-DOF macro: knuckle, needle, latch razor-sharp, everything else dissolved. Isolation = the cut-to-detail frozen. | insert chain, crash-zoom arrival, hip-hop CU |
| **Freeze-frame stillness** | Deliberately *zero* blur, hard edges, held breath — reads as a stopped clock against the blurred panels around it. | the pre-launch held beat, the loaded spring |

Per-technique kit (triad + the still application):

- **Frozen motion blur** — what it does to emotion: differential blur reads as velocity made tactile, the world torn past a steady subject — where seen: Dod Mantle whip-panned every overtake in *Rush* so the background dissolves. — *in a keyframe* [Shift/Impact]: hero car tack-sharp, entire background raked into horizontal streaks, foreground objects elongated into light-rods. The most powerful single-panel speed trick: **sharp hero + fully smeared world.** Equal blur everywhere = soft photo; differential blur = speed.
- **Tyre wrinkle / partial blur** — emotion: physics you can feel, force arrested at its peak — seen: Goodyear's deliberately silent slow-mo of the slick sidewall folding; Ritchie's speed-ramp as the exclamation mark. — *in a keyframe* [Detail/Reaction]: macro into the rear sidewall, the wrinkle caught at its deepest fold, smoke just blooming at the contact patch, everything else crisp. One arrested ten-thousandth of a second. The hero detail to *hold*.
- **Smoke / debris / spray shape** — emotion: force given a visible body, dread made airborne — seen: NHRA burnout-cam, "a wall of smoke" backlit at ground level. — *in a keyframe* [Pressure/Power]: backlit tyre smoke as a luminous wall (front-lit smoke is dead gray nothing); water-box spray frozen as a constellation of specular droplets, each rimmed on its leading edge. Atmosphere only reads when light passes through it (§5).
- **Posture / lean vector** — emotion: a stillness that can only resolve forward; the eye does the launching — seen: Vaughn's charged poses (*Kingsman*, *Layer Cake*) — every frame loaded with a trajectory. — *in a keyframe* [Power/Shift]: **no neutral panels.** Car at idle = front wheels micro-lifting, body slung onto the rear axle. Hand on wheel = fingers mid-clench. Compose the negative space *ahead* of the subject, the direction it is about to fire into.
- **Leading lines / light streak** — emotion: a rail for the eye that also encodes direction and speed — seen: Papamichael's asphalt-in-frame (*Ford v Ferrari*), the road as the speedometer. — *in a keyframe* [Power/Impact]: lane centerline raking to a vanishing point, sodium/mercury practicals smeared as long reflections down wet asphalt. Keep the texture (chevrons, tar seams, rubber marks) so the streak has something to streak.
- **Off-balance dutch** — emotion: imbalance, loss of grip, threat — seen: Raimi's canted attack frames (*Evil Dead II*). — *in a keyframe* [Impact]: cant the horizon hard at the one loss-of-traction beat — tyre breaking away, car stepping sideways. Reserve it for a single instability beat so it stays loud; dutch as wallpaper reads as bad framing.

**The speed-budget rule** (from the race-truth school): a still sells velocity when **at least three of five coexist in one frame** — (a) camera at/below bumper height, (b) asphalt streaking the lower frame, (c) a near foreground reference passing the edge, (d) sharp hero against motion-blurred background, (e) a mechanical-vibration cue (trembling mirror, doubled needle, smeared rim). One cue is a car photo. Three is velocity. If a "fast" panel cannot name three, reframe lower, drag the camera to the asphalt, throw a cone or barrier into the foreground.

---

## 5. Emotion without faces in a still

A face does four jobs: shows the feeling, shows where it looks, shows the cost, shows the decision. Faces banned, redistribute: **decision → anatomy mid-action; internal state → an object crossing a threshold; looking/rivalry → space** (§6 and `dramaturgy.md` §2). Assign one job per panel and tag it. The emotion must already be frozen *inside the object* — a still cannot let motion blur do the emotional work for it.

Two load-bearing rules:

- **Anatomy only on a decision.** A hand at rest is filler; a hand *deciding* is a shot. Before drawing any hand/foot panel, name the verb — grip / latch / shift / preload / release. No verb, no panel. Render tendons raised, glove leather creasing, one hard side-light carving knuckle texture, the rest in shadow (Leone's hands-before-the-draw; Nike *Take It to the Next Level*, first-person, no hero face).
- **Objects only when they change state.** A static gear-lever says "car stuff" and flatlines. Board the **after** state of a threshold-crossing; the before is implied (Honda *Cog*: every object does something irreversible). Tach pinned in the red, not idling. Ignition lamp blooming live, not dark. Slick caught mid-fold.

Use the substitution table as the core deliverable — when the script wants an emotion and no face is available, render this object at this crop. Cold palette throughout.

| Emotion (a face would show) | Object substitute | Crop | Render note (the still) | Label / tag |
|---|---|---|---|---|
| **Fear / dread** | sweat bead on knuckle; tremor in the mirror reflection (not eyes) | macro / ECU | one hard specular highlight on the bead, cold rim, deep black around it; mirror edge doubled to imply vibration | setup → Pressure |
| **Resolve / commitment** | knuckles whitening on wheel or shifter; foot pinning throttle | CU / MCU | tendons raised, glove leather creasing, grip at maximum; one side-light, cabin in shadow | commitment → Shift |
| **Focus / lock-in** | start-lights reflected in lacquer / headlight glass (not a human eye) | MCU | staging bulbs mirrored as cold points on paint or chrome; tight, centered, still | setup → Detail |
| **Strain (machine at limit)** | tach needle pinned in red arc; slick sidewall wrinkling; exhaust flame | ECU / CU | needle hard against redline, motion-still but unmistakably max; sidewall at deepest fold | proof-of-speed → Pressure |
| **Mistake / panic** | tyre shake (sidewall "goes square"), wheel kicking back, revs over-flared | CU | sidewall deformed wrong, blur direction fighting the lane; tach spiked past the band | mistake → Impact |
| **Triumph / release** | grip relaxing; chute blooming; one nose past the stripe; smoke through headlight beams | CU → WS | fingers unfurling off the wheel; or distant clean geometry of the win, cold backlight through smoke | result → Aftermath / Exit |
| **Anticipation (pre-launch)** | finger over ignition / line-lock; pre-stage bulb lit; held shifter | ECU / CU | finger a hair off the button, bulb just lit cold, everything frozen — the "silence" panel | setup → Pressure |

State-change cheat-sheet (board the live state; the dead is implied): ignition dark → lamp blooming; tach idle → needle pinned red; slick round → wrinkle folded deep; water-box mirror-still → shredded by launch; front wheels planted → lifting; chassis level → squatted; chute packed → bloomed at the trap.

---

## 6. The loaded frame for one panel

A keyframe is a diagram the viewer solves in 0.3s and re-reads with pleasure at 1s. With no face, the geometry and the depth stack do the acting.

> **Core law of the loaded panel.** One focal point, one emotion, three working depth layers, zero dead objects. Answer one question in the first glance; reward a second look.

**Depth-layer jobs (FG / MG / BG).** Write the prompt in three explicit depth clauses, each with a stated job. This is the engine of "reads in one glance, rewards a second" (extends `dramaturgy.md` §10 into a single still). If all three planes carry the same blur or scale, you have one plane, not three — force a sharp MG subject against a soft FG frame and a soft BG stake (shallow DOF is the panel's hierarchy tool, `camera-lighting-vocabulary.md` §3).

| Plane | Default job | Drag-race objects | Function it serves |
|---|---|---|---|
| **Foreground** | frame / obstruct / put us inside | roll-cage bar, mirror edge, harness strap, smoke wisp, wet glass | Pressure, Power |
| **Midground** | the subject / the act | hand on shifter, knuckles on wheel, foot on pedal, tach face | Detail, Shift, Impact |
| **Background** | stakes / context / rival | staging bulb, rival lane headlight, finish line, narrowing barrier | Establish, Reveal, Pressure |

**One-glance + reward** — what it does to emotion: an instantly readable frame creates trust; a frame that rewards re-reading creates density and worth. With no face to anchor on, a muddy panel collapses to nothing. — *in a keyframe*: name the single focal point before generating (tach needle / staging bulb / knuckle), put it on a strong line, demote everything else to support. The second-look reward is a reflection, a bridge object, or a state indicator — one, not a clutter.

**Centerline spine, then break symmetry** — emotion: a single dominant axis (lane stripe, the Christmas Tree, a dividing wall) gives the eye a rail and makes even a chaotic frame readable; breaking it the instant one car noses ahead reads as momentum. — seen: Anderson centers for instant legibility; Bong breaks balanced staging to show a power shift. — *in a keyframe*: build one head-on symmetric "breath" panel — both cars mirrored across the centerline, Tree dead-middle, equal negative space (tag **Establish/Pressure**, hold longest). On the next panel, break the mirror — hero a nose ahead, rival shoved soft, centerline slid off the third (tag **Shift/Impact**). Use the pair exactly once, at the launch; overusing symmetry kills the speed.

**Functional vs decorative clutter — the evidence test.** Keep an object only if it does at least one of: (1) **indicator of state** (replaces the face — tach in the red, white knuckles), (2) **stage of action** (advances the beat — front wheel 7" off the line = pre-stage), (3) **bridge to the next panel** (sets up a match-cut or a reach). Dead detail — coffee cup, mirror dice, dashboard sticker — shows no state, advances nothing, bridges nowhere. Cut it. "Each object is a clue" (Park); functional clutter *loads* the frame, decorative clutter *weakens* it.

**Angle encodes the beat** (no face, so the angle *is* the emotion): low / ground-level = power, threat, launch force (**Power, Impact**); eye-level lateral = parity, rivalry stated (**Establish**); high / top-down = judgment, smallness, aftermath (**Aftermath, Exit**).

---

## 7. From keyframe to image-gen prompt

A keyframe card becomes a still prompt by following the universal skeleton (`universal-rules.md` U1) with weight at the start (U2). **Lead with framing + lens + light + palette + anchor object** — these are the load-bearing tokens for a still; the model puts most attention on the first 30-40% of tokens.

Panel → prompt skeleton:

```text
[Framing + lens]           e.g. "Low bumper-height macro, 24mm, shot past a blurred roll-cage bar"
[Anchor subject + state]   the ONE object at its threshold: "rear slick sidewall wrinkling at the contact patch"
[Depth clauses, 3 jobs]    FG frame / obstruct · MG subject / act · BG stake / rival
[Motion-as-still cue]      "sharp subject against horizontal motion-blurred background, foreground reference elongated into a light-streak, rear rim spokes smeared to a disc"
[Light + palette]          one motivated source + direction + surface it rims; concrete colors; amber-ban
[Texture]                  "fine film grain heaviest in shadow, halation on the practicals, one anamorphic flare, crushed blacks"
[Face rule]                "no face" — or "driver a featureless silhouette against blown rival headlights, only knuckle highlights legible"
[Aspect / no-speed-up note]  "no speed-ramp; build velocity into the static frame"
```

Rules that keep the still honest:

- **Name the differential blur explicitly.** Models default to over-clean stabilization. Write "motion blur on background, fast-shutter look, sharp subject, rim spokes smeared to a disc." Equal/no blur is the most-faked and most-failed cue (anti-fake firewall, §4 speed-budget).
- **Keep faces out or fragmented.** Convert any would-be face to silhouette / contre-jour with a rim and one glint. No features.
- **Render audio as physical consequence, never as a named sound.** "Loud engine" is banned filler (`dramaturgy.md` §2) — prompt "heat-haze warp off the headers, exhaust flame, chassis squat, sidewall wrinkle" instead.
- **Anti-sterile guard.** If the panel could be captioned "clean," "beautiful lighting," or "high quality," it has failed — name the grain, the bloom, the crushed black, the one specular hit (`universal-rules.md` U12). One motivated source dominates; ~70% of the frame stays unlit (`camera-lighting-vocabulary.md` §5-7).

Cross-link the vocabulary file for every framing/lens/light token. Then **the keyframe is the locked first frame**; hand it to `seedance.md` / `kling.md` / `veo.md` with the single dominant move (one per 5s — `camera-lighting-vocabulary.md` §2) to animate it. Name in the model syntax: "low bumper-height camera, asphalt streaking, motion blur on background, sharp subject, no speed-up."

---

## 8. Worked keyframe board for a 30s race spot

A Sportsman-tree drag run, cold palette, no faces — ~13 panels using the card. This is the deliverable template the user fills: each row is a compressed keyframe card, format-C compatible (`Time | Shot | Function | Action | Camera | Light | Sound | Emotion`). Cut length collapses toward the green, holds on the wrinkle, then accelerates to the finish.

| Time | Shot (anchor) | Function | Action (state-change + motion-as-still) | Camera (implied move) | Light (cold) | Sound | Emotion-via-object |
|---|---|---|---|---|---|---|---|
| 0.0–2.5 | Slick into water box | Establish | Front tyre breaks mirror-still water; bulb reflected in the sheet | locked macro, low (held) | steel-blue, wet specular | idle lope, water trickle | coiled stillness |
| 2.5–5.0 | Burnout wall | Power | Rear erupts a smoke wall, car straining on line-lock; smoke backlit luminous | ground-level wide (burnout-cam) | cyan backlight through smoke, red tail bleed | lope → tyre scream | leashed force |
| 5.0–6.5 | Pre-stage bulb + front tyre | Pressure | Tyre creeps, top blue bulb lights, beam line as graphic spine | CU, static | blue glow on wet metal | lope thickens | held breath |
| 6.5–8.0 | Stage bulb + knuckles | Pressure | Second bulb lit, knuckles whiten on the trans-brake (depth: bulb BG, hand FG) | CU, depth layers, static | two blue bulbs, crushed black | idle DROPS to silence | point of no return |
| 8.0–9.5 | Amber stagger (1 of 3) | Pressure → Shift | First amber lights; foot pre-loading the pedal | tree-cam, snap-tight | amber pulse (sole warm, toxic) | vacuum of silence | trigger tension |
| 9.5–10.3 | Held breath frame | Pressure | Staged car dead-still, last amber, tach needle the only tremor | symmetric, locked (HOLD) | amber flare, steel rim | silence (the pause) | loaded spring |
| 10.3–11.6 | LAUNCH lunge | Impact | Both cars squat, front wheels lift, green flares, asphalt smears back | low bumper-POV, fisheye (smear) | green flash + hard flare | BANG, leads pic 3fr | release / violence |
| 11.6–13.5 | **Slick wrinkle** (HOLD) | Detail / Reaction | Sidewall folds and hooks at the contact patch; speed-ramp pause, partial blur | macro slick-cam (frozen ramp) | hard side light, smoke bloom | tyre bite (near-silent) | physics felt |
| 13.5–15.5 | Cabin shake | Pressure | Needle buried in red, mirror doubled by vibration, glass strobing | hard-mount interior (tremor) | strobing exterior, red needle accent | rising rev, gear stab | strain |
| 15.5–18.5 | Bumper POV | Pressure | Asphalt tears under the nose, lane stripes strobe to a vanishing point | low forward hood-cam, 24mm (radial smear) | streaked specular, mercury-white | doppler build | commitment |
| 18.5–22.5 | Joust / parallel pass | Power | Rival closes head-on, offset; cone huge-blurred on the opposite edge | chase tracking + joust (closing) | streaked roadside lights, red tail accent | engine duel, doppler swell | rivalry |
| 22.5–26.5 | Finish | Impact | Slicks blown-up and distorted, two cars inches apart across the line | slight high, finish-cam | cold-white finish pool | sound peak → cut | margin |
| 26.5–30.0 | Hand unclenches / chute | Aftermath / Exit | Fingers release the wheel; chute bloomed, smoke drifting through a beam | ECU then rear wide (settling) | single cold rim, residue haze | hard cut to silence, one breath | consequence / release |

Notes on the board: the 9.5–10.3 held panel is the single most-held still — the pause that triggers the bang. The launch is *not* one hero frame; in a fuller cut, fan 10.3–11.6 into a 6-9 panel micro-burst (§3) — that expansion is what carries the 13 compressed rows up to the ~18-26 panel count of §3. The wrinkle is the one place time expands inside the loud section. No two bang-clusters touch; every burst is separated by a held quiet panel. End on consequence, held ~2s — the vacuum is the punctuation.

---

## 9. Checklist: does this keyframe earn its place

Run before every panel ships. Drop the panel if it fails.

- [ ] **Function tag named.** One of Establish / Reveal / Power / Pressure / Detail / Reaction / Shift / Impact / Aftermath / Exit. No tag → drop it.
- [ ] **One readable beat**, sayable in one sentence. If you cannot caption it (setup / commitment / mistake / recovery / proof-of-speed / result), it is a *fantik* — drop it.
- [ ] **Emotion-via-object** present — the feeling a face would carry, frozen in a knuckle / needle / pedal / smoke / sweat-bead (§5). No state-change, no emotion → drop it.
- [ ] **Speed or drama cue** present — ≥1 of the six motion-as-still cues (smear / partial blur / streak / vector / sharp-blur / held stillness), or a deliberate held-still pause. "Fast" panels carry ≥3 of the five speed cues (§4).
- [ ] **State-change, not static fetish** — the object crosses a threshold (idle→flare, clean→smoked, planted→lifting). No idle anatomy, no parked gear-lever.
- [ ] **Three depth layers**, each with a stated job (FG frame/obstruct, MG subject, BG stake). One focal point; every other object is evidence, not decoration.
- [ ] **Implied camera named** — the move this still is the first frame of, physically mountable on the car (no god-angle render).
- [ ] **Cold palette held** — steel/cyan/magenta/mercury-white, red and green as accents only, amber ≤15% and point-source (toxic, never cozy). One motivated source, ~70% unlit, one hard specular hit. Texture named (grain, halation, one flare), not "clean."
- [ ] **No face**, or a face fragmented past usefulness (silhouette / reflection only).
- [ ] **Sound cell filled** even though the panel is a still — what audio underlies the held frame, where the cut bites (`dramaturgy.md` §11).
- [ ] **Earns its density slot** — a held beat gets one panel, a bang gets a burst; the board reads as an accelerating tachometer on mute (§3).

If a panel survives all ten, it is an *opornyi kadr*, not wallpaper. Hand it to `seedance.md` / `kling.md` / `veo.md` as the locked first frame.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/camera-lighting-vocabulary.md

# Camera, lighting, color, sound vocabulary

Use precise production language. "Cinematic" is not a direction. "35mm, slow push-in, warm window key from frame-left" is.

## Contents

1. Framing
2. Camera movement
3. Lens language
4. Light sources
5. Light direction
6. Light quality
7. Color discipline
8. Sound categories
9. Blocking language
10. Translating uncommon terms
11. Transition vocabulary

---

## 1. Framing

- extreme wide shot
- wide shot
- medium wide
- medium shot
- medium close-up
- close-up
- extreme close-up
- macro insert
- over-the-shoulder
- POV
- profile
- silhouette
- low angle
- high angle
- top-down
- dutch angle
- locked-off frame

## 2. Camera movement

- static camera
- slow push-in
- fast push-in
- pull-back
- tracking shot
- lateral tracking
- handheld micro-shake
- whip pan
- snap zoom
- rack focus
- tilt up
- tilt down
- orbit
- gimbal glide
- dolly-in
- dolly-out
- crane shot
- aerial shot
- Hitchcock zoom (dolly-zoom)
- dive (camera plunges downward)
- FPV (drone first-person flight)
- one-take shot
- bullet time
- bounce speed ramp (speed up - slow down - speed up)

Universal rule. Pick one dominant move per 5-second shot. Layer one subtle secondary move at most. The popular techniques (one-take, dolly zoom, FPV, bullet time, bounce speed ramp) still need a subject, a start point and an end point — the name alone is not a direction.

## 3. Lens language

- 24mm. Wide, immersive, exaggerated proximity.
- 35mm. Natural documentary.
- 50mm. Intimate, human perspective.
- 85mm. Portrait, compressed background.
- 100mm macro. Texture, detail.
- anamorphic 40mm. Cinematic widescreen.
- shallow depth of field.
- deep focus.
- compressed telephoto background.
- distorted wide-angle proximity.

## 4. Light sources

- cold refrigerator light
- harsh overhead kitchen LED
- moonlight through window
- neon sign spill
- phone screen glow
- car headlights
- streetlamp backlight
- fluorescent office light
- practical lamp
- candlelight
- monitor glow
- emergency red light
- sodium vapor street light
- police strobe
- theater house lights
- stage spotlight
- campfire flicker
- sunset through blinds
- under-counter kitchen LED

## 5. Light direction

- top light
- side light
- backlight
- underlight
- frontal soft light
- rim light
- bounce fill
- window key light
- motivated practical (the light source is visible in frame)

## 6. Light quality

- hard shadow
- soft diffused
- low-key lighting
- high contrast
- silhouette
- specular highlights
- volumetric haze
- steam catching backlight
- wet reflections
- desaturated palette
- cold blue-gray grade
- teal shadows
- clean commercial lighting
- gritty naturalistic
- blown-out overexposure
- crushed blacks

## 7. Color discipline

Define palette with concrete colors. Never write "cinematic colors."

Bad. "cinematic colors."
Good. "Cold blue-gray shadows, desaturated skin tones, greenish fridge spill, black negative space, no warm yellow tones."

If the user bans a color, obey it strictly. Repeat the ban in every clip of a multi-clip sequence.

Common palettes.

- Fincher cold. Cold blue-gray shadows, desaturated skin, black negative space.
- Deakins natural. Warm amber interiors, cool blue exteriors, clean contrast.
- Wong Kar-wai. Saturated warm reds, deep greens, hazy practicals.
- Glazer neon. Black, one dominant neon hue (magenta or teal), hard edges.
- Commercial creamy. Warm creams, soft pastels, clean whites, no harsh blacks.
- Safdie chaotic. Mixed sources, overlapping color temperatures, urban neon spill.

## 8. Sound categories

Even if the model does not generate audio, sound description helps structure rhythm.

Ambient.

- room tone
- distant city ambience
- rain on tin roof
- wind through leaves
- fridge hum
- fluorescent buzz
- traffic wash

Body and action.

- breath
- footsteps
- fabric rustle
- fork clink
- door hinge
- key in lock
- zipper
- stomach growl

Dramatic events.

- sudden silence
- low bass hit
- wet thud
- glass break
- distant thunder
- car door slam
- final sound cue before cut to black

For Veo, wrap sound in syntax. `Audio:`, `SFX:`, or `(parenthetical description)`.
For Seedance 1.5+, include sound in the prompt body.
For Kling, sound descriptions help rhythm planning but audio is not generated.

## 9. Blocking language

Describe physical movement with six inputs.

- Who moves.
- Where they start.
- Where they end.
- What object they touch.
- What they look at.
- What their body reveals emotionally.

Example.

```text
The man stands in the kitchen doorway, shoulders collapsed. He slowly approaches the refrigerator, opens it with hesitation, leans into the cold light, then freezes when he sees the empty shelves.
```

This beats "a sad man goes to the fridge" because it is playable by the model frame by frame.

## 10. Translating uncommon terms

Common terms (section 2) work by name. For rarer cinematography terms, keep the term **and** translate it into observable change, or the model guesses:

```text
Term + target subject + visual change + foreground/background relationship + direction or speed
```

Example.

```text
Rack focus: shift focus smoothly from the leaves in the foreground to the person
in the background. The leaves gradually blur while the person's face changes
from soft to sharp.
```

Same pattern for snorricam, contra-zoom variants, tilt-shift, split diopter, speed ramps with specific curves. Numeric aperture and focal-length values are allowed, but the intended visible result phrased in words is what actually steers the model.

## 11. Transition vocabulary

Named transitions every current model understands to some degree (Seedance 2.5 honors them explicitly — templates in `seedance-25.md` §10):

- **natural cut** — plain edit point, model picks the framing change
- **fade in / fade out** — to or from black
- **dissolve** — cross-fade, 1-2 seconds of overlap
- **white flash / black flash** — one-frame blast, impact punctuation
- **wipe** — new frame pushes the old one off
- **occlusion mask** — a foreground object covers the lens, the new scene is revealed behind it
- **match cut** — similar shape or motion bridges two scenes (moon → latte)
- **action cut / whip pan** — cut hidden inside fast motion with motion blur
- **motion relay** — subject exits frame A mid-move and lands in frame B continuing it
- **zoom-through** — camera dives through a pupil, keyhole or window into the next scene
- **ink-wash dissolve** — stylized bleed, common in guofeng / animation work

Rules of use. Name the transition and the exact moment it fires. One transition type per cut. When the choice is open, delegate: "choose the most suitable from [natural cut / occlusion mask / match cut] for the style of this film."

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/dramaturgy.md

# Dramaturgy, detail, montage

This is the mandatory layer. A beautiful frame without dramaturgy is wallpaper. Every prompt built by this skill must pass the dramaturgy check before it is sent to the user.

## Contents

1. Core law. Scene formula
2. Second law. Details intensify emotion
3. The three-jobs rule (what every shot must do)
4. Walter Murch Rule of Six
5. Blocking as choreography of desire
6. Staging controls subtext
7. Camera must have a reason
8. Spatial clarity beats montage hysteria
9. Environment plays
10. Three-layer storyboard method
11. Shot card template (14 fields)
12. Rhythm ladder
13. One-anchor principle
14. Worked example
15. Dramaturgy check before sending any prompt

---

## 1. Core law. Scene formula

A scene exists only when all five elements are present.

```text
Scene = hero's desire + obstacle + space geometry + controlled gaze + editing rhythm
```

If any element is missing, the scene collapses into decoration.

- Desire. What does the character want right now in this specific second.
- Obstacle. What blocks them. Object, person, fear, distance, rule.
- Space geometry. Who stands where. Who has the power position. Which direction is threat, which is escape.
- Controlled gaze. Where the viewer's eye is forced to look, one focal point per frame.
- Editing rhythm. How long each shot lives, where the pause lands, where the cut bites.

Before writing a prompt, name each of these in one sentence. If you cannot, the scene is not ready.

## 2. Second law. Details intensify emotion. Laziness kills the prompt.

The scene formula tells you **what a scene is**. The Details Law tells you **how every shot must be written**. Skip it and even a perfect dramaturgical structure produces mush on screen.

> Every shot owns three concrete physical details: one environmental pressure, one physical micro-action, one sound or visual motif anchor.

### The three-detail rule

For each shot in the storyboard or prompt, before it is sent, the writer commits to:

1. **Environmental pressure.** A physical fact about the space that carries the emotion. Cold refrigerator light. Wet asphalt. Flickering ceiling tube. Steam from the kettle. Rain on one specific windowpane. A buzzing AC unit. Tight corridor walls. Mirror reflection. (See §9 — Environment plays.)
2. **Physical micro-action on the body.** The emotion translated into the actor's body. Jaw locks. Knuckles whiten. Lips press flat. Eyes drop a quarter-inch. He swallows hard. Fingers curl against the doorframe. The actor's body is the only place where feelings render — names of feelings do not.
3. **Sound anchor or visual motif.** A recurring perceptual hook tied to the spine of the piece. Stomach growl repeated three times. Reflection in dark glass on every transition. The same musical sting at every Crack beat. The clock's second hand. Footsteps in an empty corridor.

A shot with zero of these is filler. A shot with one is thin. Strong shots carry all three. The writer's job is to do this work — the model cannot infer it.

### What is banned

Words that mark a writer being lazy. Each one is a placeholder for absent detail.

- "cinematic", "professional", "high quality", "masterpiece", "stunning", "epic", "amazing"
- "beautiful lighting", "dynamic camera", "intense moment", "powerful scene"
- "he is sad", "she is angry", "he is afraid" — emotions named without a body

Replace each with concrete physical facts. If a writer cannot do that, the scene is not yet thought through.

### How details map to dramaturgy

Each layer of dramaturgy has a default detail register:

- Scene formula → environmental pressure (the geometry and atmosphere of the obstacle).
- Three-jobs rule → physical micro-action (the body shifts when emotion / action / pressure shifts).
- Five anchors → sound and visual motif (the motif is the anchor, the final image carries the motif).

If a shot's detail set does not match its dramaturgical function, the function will not land on screen.

## 3. The three-jobs rule

Every shot must do at least one of three things. If it does none, delete it.

- Change emotion (in hero, viewer, or the dynamic between characters).
- Advance action (new physical event, new information, new position).
- Increase pressure (stakes rise, clock ticks, space tightens, witness appears).

"Beautiful establishing shot" is not a job. "Beautiful hero shot of product" is not a job. Either the frame works for one of these three, or it is a fantik (wrapper without candy).

## 4. Walter Murch Rule of Six

From the editor of Apocalypse Now, The Godfather Part II, and The English Patient. The priority order when deciding where to cut. Each item is weighted heavier than the sum of everything below it.

1. **Emotion (51%).** Does the cut honor the emotional truth of the moment. What does the viewer feel now vs. what they should feel next.
2. **Story (23%).** Does the cut advance story or reveal character.
3. **Rhythm (10%).** Does the cut fall on a musical beat of the scene.
4. **Eye-trace (7%).** Where is the viewer's gaze at the moment of the cut. Does the new shot receive that gaze naturally.
5. **2D plane (5%).** Does the cut respect the axis of screen direction.
6. **3D space (4%).** Does the cut respect the geometry of the real location.

Practical consequence. Cutting for "динамика" (pace for its own sake) sits at item 3. If you cut there without serving items 1 and 2, the result is TikTok-ad for the attention-deficit.

## 5. Blocking as choreography of desire

Blocking is not "where the actor stands." Blocking is a visual answer to "what does the character want and from whom."

For every character in the scene, name.

- What they want now.
- Who or what they move toward.
- Who or what they move away from.
- Whom they corner.
- To whom they yield space.
- What gesture reveals the hidden desire.

Bad. "He stands near the window."
Good. "He edges toward the window but his shoulder stays angled back toward her, as if the conversation still holds him."

## 6. Staging controls subtext

Staging is the arrangement of people, objects, and camera inside the frame. Before dialogue, staging already tells the conflict.

Power signals in staging.

- The standing character dominates the seated one.
- The character in the doorway controls the room.
- The character behind glass or in reflection is psychologically distant.
- The character in shadow carries threat or grief.
- Negative space around a character signals isolation.
- Tight framing signals suffocation.
- Shared frame without eye contact signals broken intimacy.

Spielberg, Kubrick, Iñárritu often build entire scenes where the staging states the conflict before a line is spoken.

Before writing a prompt, name the power dynamic the staging reveals.

## 7. Camera must have a reason

Fincher rule. Every camera movement answers "what changed?" If the answer is nothing, the camera is static.

Reasons for camera movement.

- A character made a decision and the camera follows the shift.
- New information arrived in the frame.
- Pressure escalated and the camera tightens.
- The character looked, and the camera reveals what they saw.
- A gesture pulled focus, and the camera rack-focused.
- The space changed (door opened, someone entered).

Bad. "Cinematic gliding camera movement."
Good. "Push-in starts on 'I don't know' and stops on her jaw locking."

## 8. Spatial clarity beats montage hysteria

Spielberg principle. Even in chaos, the viewer must know.

- Where the hero is.
- Where the threat is.
- Which direction is escape.
- Which direction is decision.

High craft means fast, nervous, and still readable. Random whip-pans and strobe cuts without geography destroy drama. The fastest action scenes in cinema (Spielberg, Miller, early Bay) are built on a clear geometric map maintained through every cut.

Before writing a fast-cut sequence, sketch the geography in one sentence. "Hero moves left-to-right. Threat enters from the top of the frame. Exit is off-camera right."

## 9. Environment plays

Kurosawa principle. Weather and environment are characters. They amplify state.

Translate this to a short video by leaning on one environmental pressure.

- Flickering fluorescent light signals decay, bureaucracy, dread.
- Rain on a window signals grief withheld.
- Steam from a kettle signals suppressed anger.
- A buzzing air conditioner signals dissociation.
- Wet asphalt at night signals guilt.
- A tight corridor signals the walls closing in.
- A mirror or glass surface signals self-reckoning.
- Overhead cold office light signals judgment.

Pick one environmental pressure per scene and let it carry the emotion.

## 10. Three-layer storyboard method

Build storyboards in three layers, in this order. Skipping a layer produces pretty but empty output.

### Layer 1. Dramatic beats

For a 60-90 second piece, a reliable beat map.

```text
0-5s    Hook.        Hero already in tension. No setup. Problem on screen.
5-15s   Context.     Where we are. Who is near. What is at stake.
15-30s  Pressure.    Hero tries to hold control.
30-45s  Crack.       A detail appears that breaks the hero's position.
45-60s  Acceleration. Cuts shorten. Breath tightens.
60-75s  Impact.      Decision, break, confession, or action.
75-90s  Aftermath.   Brief silence or visual residue.
```

Adjust for 30s or 15s by compressing proportionally. Never skip the Crack or the Impact.

### Layer 2. Shot functions

Tag every shot with a function. Same taxonomy as in role-modes.md, expanded with Power.

- **Establish.** Where we are.
- **Power.** Who controls the scene right now.
- **Pressure.** What is pushing down on the hero.
- **Detail.** Object, hand, phone, eye, drop, receipt, door. Macro anchor.
- **Reaction.** Face after the event.
- **Shift.** Inner change made visible.
- **Impact.** The decisive frame.
- **Aftermath.** Emptiness after action.
- **Exit.** Final image the viewer carries out.

This is cinema grammar. Everything else is decorative wallpaper.

### Layer 3. Editing rhythm

Not random mincing. A rhythmic staircase.

```text
long - shorter - shorter - pause - impact
```

Example internal structure of an 8-10 second montage.

- 4s. Wide. Hero enters.
- 2s. Medium. Hero notices the object.
- 1s. Close-up. Eyes.
- 12 frames (0.5s). Macro insert of the object.
- 8 frames (0.33s). Hand.
- 6 frames (0.25s). Detail / sound cue.
- 2s. Sudden silence.
- 1s. Decision.

Rule. The pause before the impact is more important than the speed of the cuts. Without a pause, speed becomes visual meat grinder.

## 11. Shot card template

For each shot in a storyboard, fill every field. Missing fields reveal missing direction.

- **Shot ID.** 01, 02, 03
- **Beat.** What changes in the story here.
- **Emotion.** Fear, shame, anger, guilt, resolve, relief, etc.
- **Frame.** wide / medium / close-up / macro insert
- **Composition.** Center, edge, negative space, reflection, silhouette, foreground obstruction.
- **Camera.** Static, push-in, handheld, tracking, whip-pan.
- **Movement reason.** Why the camera moves here. Answer "what changed?"
- **Action.** Exact physical event.
- **Eye trace.** Where the viewer's gaze should land in the first 0.3s.
- **Duration.** 0.5s, 1s, 3s.
- **Cut type.** match cut, smash cut, cut on action, J-cut, L-cut.
- **Sound.** Breath, bass hit, street noise, phone ring, silence.
- **Light / color.** Cold, contrast, flicker, shadow, specific palette.
- **Production note.** Prop, location, actor direction.

If a shot card has empty fields, fill them or drop the shot.

## 12. Rhythm ladder

Drama rhythm is not uniform. It is stepped.

### Slow-burn drama
4s, 4s, 3s, 2s, 1s, pause, 2s.

### Commercial product arc
3s, 2s, 1.5s, 1s, 0.5s (product macro), 2s (hero shot).

### Anxiety build
2s, 1s, 1s, 0.5s, 0.5s, 0.3s, pause, 1s.

### Impact scene
pause, 0.2s (flash), 2s (aftermath in stillness).

Always insert at least one pause before the biggest cut.

## 13. One-anchor principle

For any short dramatic piece, commit to exactly five anchors. No more.

- One main emotion.
- One visual motif.
- One anchor object.
- One break.
- One final image.

Example.

- Emotion. Guilt.
- Motif. The hero keeps being reflected in glass surfaces (window, phone screen, elevator door).
- Anchor object. A phone with one unread message.
- Break. The hero deletes the message.
- Final image. The hero's face stays reflected in the darkened phone screen.

This set can be storyboarded, prompted, and cut together into something that carries real weight. It beats stacking "cinematic, professional, high quality, masterpiece" forever.

## 14. Worked example. Guilt, 30 seconds

### Five anchors

- Emotion. Guilt.
- Motif. Reflections in glass.
- Anchor object. Phone with unread message.
- Break. He deletes it.
- Final image. His face ghosted on the dark phone screen.

### Layer 1. Dramatic beats

- 0-3s. Hook. Phone buzzes on a dark desk. His face lit from below.
- 3-10s. Context. Small office after hours. Empty cubicles. Cold fluorescent. His reflection in the monitor.
- 10-18s. Pressure. He stares at the message preview. His jaw tightens. Hand hovers.
- 18-22s. Crack. He starts to type. Stops. Deletes character by character.
- 22-26s. Acceleration. Tight cuts. Finger. Screen. Eye. Breath. Window reflection.
- 26-28s. Impact. He taps Delete Conversation. One tap. Silence.
- 28-30s. Aftermath. Screen goes black. His face remains reflected in the dark glass.

### Layer 2. Shot functions (selected)

- Shot 03. Establish. Empty office.
- Shot 05. Power. He is alone. The room looms.
- Shot 07. Detail. Phone screen close-up.
- Shot 09. Reaction. His face, jaw tightening.
- Shot 11. Shift. Hand hesitates over keyboard.
- Shot 13. Impact. Thumb taps Delete.
- Shot 14. Aftermath. Dark screen, his ghosted reflection.

### Layer 3. Rhythm (final 10 seconds)

- 2s. Finger hovers over Delete.
- 1s. His face.
- 0.5s. Thumb.
- 0.5s. Screen confirmation prompt.
- 1s. His eyes.
- 0.5s. Thumb taps Delete.
- 3s silence. Screen goes black.
- 1.5s. His reflection on the dark phone.

Now each beat can be translated into a model-specific prompt using `references/seedance.md`, `references/kling.md`, or `references/veo.md`.

---

## 15. Dramaturgy check before sending any prompt

Run this six-point check before returning the final prompt to the user.

1. Is the scene formula complete? (desire + obstacle + geometry + gaze + rhythm)
2. Does every shot pass the three-detail check? (environmental pressure + physical micro-action + sound or visual motif)
3. Does every shot do one of the three jobs? (change emotion, advance action, increase pressure)
4. Is there a motivated reason for every camera move?
5. Is the spatial geometry readable?
6. Are the five anchors named? (emotion, motif, object, break, final image)

If any answer is no, fix before sending. Step 2 is the most violated.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/fixes-and-skeletons.md

# Fixes, checklist, and cross-model skeletons

## Contents

1. Continuity checklist (before final output)
2. Common failures and fixes
3. Cross-model prompt skeletons
4. Default negative constraints
5. Prompt compression order
6. Output format templates

---

## 1. Continuity checklist

Before sending a prompt to the user, verify.

- Same character across shots (face, body, hair).
- Same clothes across shots, exactly named.
- Consistent location logic.
- Object state progression makes sense (sausage in fridge -> on plate -> on fork -> on floor).
- No unwanted extra characters.
- No unwanted text or subtitles.
- No unwanted logos.
- Consistent age / body / face.
- No impossible hand-object action.
- No vague camera instructions ("cinematic camera").
- No vague lighting instructions ("beautiful light").
- No random stacking of director references.
- No contradictions.
- Palette is defined with concrete colors.
- Final image is explicitly stated.

If any item is missing, fix before sending.

---

## 2. Common failures and fixes

### One continuous take instead of montage

Fix.

```text
This must be a multi-shot sequence with visible hard cuts. Do not generate a single continuous take. Each beat uses a different angle and framing.
```

For Seedance specifically, add explicit `Cut to.` or `Camera cut to.` markers in the prompt body.

### Character face changes between shots

Fix.

```text
Preserve the exact character in every shot. Same face shape, same eye color, same hair, same clothing, same expression style. [repeat the full identity block]
```

For Kling. Use Element Binding with 3-4 reference images (front, side, three-quarter).

### Object disappears mid-scene

Fix.

```text
Track the object continuously. The same object remains visible or clearly implied in every beat.
```

Describe the object's state progression in one sentence. "The sausage moves. fridge -> pot -> fork -> floor."

### Weak drama. Scene feels flat.

Fix.

```text
Play the scene with full emotional seriousness. Treat the ordinary object as if it carries life-or-death meaning. No comedy pacing. No detached observation.
```

### Messy random cuts in fast montage

Fix.

```text
Use fast montage with clear readable action per cut. Every cut shows a distinct detail. face, hand, object, reaction, impact. Each cut must have a visible function.
```

### Dialogue too fast (Veo)

Fix. Cut the line. 8 seconds max of spoken text. Test by reading aloud at normal pace.

### Melting hands / extra fingers

For Kling. Add to negative field.

```text
distorted hands, extra fingers, melted face, deformed
```

For Seedance and Veo. Use positive phrasing.

```text
anatomically correct hands, clean finger separation, realistic proportions
```

### Lighting drifts between clips

Fix. Name the dominant source and direction and repeat it verbatim in every clip.

```text
Lighting constant. Cold fridge light as key from frame-right. Warm window spill as rim from frame-left. Same contrast ratio in every shot.
```

### Model ignores camera instruction

Fix. Move camera to the front of the prompt.

Bad. "A man opens a fridge. The camera is a slow push-in."
Good. "Slow 50mm push-in. A man opens the fridge."

### Weird AI-looking faces

Fix. Avoid style words like "hyperrealistic 8k masterpiece." These push the model into AI-art territory. Use production language instead.

```text
Shot on 50mm, natural skin texture, motivated lighting, documentary feel.
```

### Twins / face-blending in multi-person scenes

Two or more characters converge into near-identical faces, or background extras clone the hero.

Fix. Bind each subject to its own reference individually (see `universal-rules.md` U13), then force differentiation.

```text
Their movements are not synchronized. Clothing colors, hairstyles, and facial features must all be distinct. No identical clones in the background.
```

### Objects or characters appear too early in an extension

When extending a clip backward (prepending a beginning), elements that belong to the source video leak into the past.

Fix. Flag them explicitly.

```text
<Materials that should appear only after the source video begins> must not appear early in the backward extension.
```

For forward extensions, the standard clause: "prohibit rigid cutting, prohibit objects appearing out of thin air."

### Random subtitles or unwanted background music

Fix. Ban directly and repeat the ban at the end of the prompt.

```text
Pure video, no subtitles, no background music.
```

On Seedance 2.5 and Veo this is reliable. On Seedance 1.x/2.0 and Kling, also avoid mentioning any on-screen text or score you do not want — mentions summon them.

---

## 3. Cross-model prompt skeletons

### Seedance

```text
Subject. [identity block].
Motion. [one clear present-tense action].
Camera. Shot 1. [framing, lens, movement]. Cut to. Shot 2. [framing, lens, movement]. Cut to. Shot 3. [framing, lens, movement].
Environment. [location, time, props].
Lighting. [source, direction, quality, color].
Style. [realism level, genre reference].
Audio. [ambient, SFX]. (1.5+ only)
Continuity. [what must remain constant].

--resolution 1080p --duration 5 --camerafixed false
```

### Kling text-to-video

```text
[Subject with identity anchor]. [Subject movement]. Scene. [3-5 environment elements]. Camera. [one movement + lens]. Lighting. [source + quality]. Atmosphere. [mood].

Negative field. blurry, distorted hands, extra fingers, melted face, watermark, subtitles, jitter.
```

### Kling image-to-video

```text
Preserve [silhouette / feature / label]. [Camera movement, one lens]. [One or two motion verbs]. [Atmospheric cue, light change].

Negative field. blurry, distorted hands, melted face, jitter.
```

### Veo prose

```text
[Subject performing action] in [environment]. [Camera framing + lens + movement]. [Lighting direction + color]. [Style + mood + palette].

Audio: [ambient, SFX, music texture].
Says: [character] says, "[dialogue, max 8s of speech]."
SFX: [punctual sound events].

Duration: [4 / 6 / 8] seconds.
```

### Veo JSON

See `references/veo.md` section 6 for full schema.

---

## 4. Default negative constraints

Where negatives are supported (Kling field, Veo body text, Seedance 2.0 fragile).

```text
No subtitles. No on-screen text. No extra characters. No changing clothes. No changing face. No logos. No cartoon physics unless requested. No warm yellow tones unless requested. No random camera drift. No single-take when multi-shot is requested. No distorted hands. No extra fingers.
```

For Kling field. Rewrite as positive entities. "distorted hands, extra fingers, subtitles, logos, cartoon physics, random camera drift."

For Seedance 1.0. Invert all negatives to positive phrasings in the prompt body.

---

## 5. Prompt compression order

When a model performs better with shorter prompts (Kling 2.5 Turbo, Kling 1.6, any image-to-video), cut in this order.

1. Keep character continuity.
2. Keep story action.
3. Keep shot timecodes (where relevant).
4. Keep lighting.
5. Keep camera.
6. Keep editing grammar.
7. Keep sound.
8. Remove philosophy and meta-commentary.
9. Remove extra adjectives.
10. Remove director references.

The goal. Preserve the skeleton. Lose the perfume.

---

## 6. Output format templates

### Format A. Single prompt

One ready-to-copy prompt for one generation. Use the appropriate model skeleton.

### Format B. Multi-clip prompts

Sequence of self-contained prompts. Each one repeats the full continuity block. Label them `Clip 1 / 5`, `Clip 2 / 5`, etc.

Between clips, add a one-line note explaining how they cut together. "Clip 1 ends on his hand reaching into the fridge. Clip 2 opens on his hand already inside the fridge, same light."

### Format C. Storyboard (раскадровка)

Table with columns.

| Time | Shot | Function | Action | Camera | Light | Sound | Emotion |
|---|---|---|---|---|---|---|---|
| 0-1s | WS | Establish | Man walks to fridge | 35mm, slow push-in | Cold fluorescent overhead | Fridge hum | Exhaustion |
| 1-2s | MCU | Reveal | He opens fridge door | 50mm, static | Cold fridge light as key | Door seal pop | Anticipation |

Adjust row count to clip length.

### Format D. Prompt audit

Given a user prompt. Return six sections.

1. What works.
2. What breaks generation.
3. Missing direction (camera, light, continuity).
4. Continuity risks.
5. Model-specific mismatches (wrong syntax for the chosen model).
6. Stronger version. Rewritten prompt, ready to copy.

### Format E. Director treatment

For concept stage before any prompt is written.

- Core idea (one sentence)
- Emotional arc (three states)
- Visual motif (one recurring element)
- Rhythm (pace logic)
- Camera language (dominant grammar)
- Lighting (dominant source)
- Sound (texture)
- Ending image (final frame)

### Format F. Veo JSON

Structured scene-by-scene JSON. Use for complex continuity. See `references/veo.md` section 6.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/kling.md

# Kling reference (Kuaishou)

## Contents

1. What Kling is
2. Versions and element limits
3. **Kling 3.0 — multi-shot, native audio, 15s (read first if user is on 3.0)**
4. Prompt formula (1.x – 2.x)
5. Prompt length by model
6. Negative prompts (dedicated field, special rule)
7. Element Library and Element Binding (unique to 1.x – 2.x)
8. Motion Brush (unique)
9. Motion Control (2.6 Pro, unique)
10. Image-to-video rule
11. Failure modes and fixes
12. Skeleton and example

---

## 1. What Kling is

Strong at realistic physics, character animation, and consistency through reference images. Fast generation. Best for social-ready clips and repeat-character scenes.

**Kling 3.0** changed the model's positioning fundamentally — it now competes with Seedance on multi-shot output (up to 6 shots per generation) and with Veo on native dialogue and lip-sync. See section 3.

## 2. Versions and element limits

Kling models vary widely in how many distinct elements they can handle in a single prompt. Overstuffing produces melting faces, broken hands, or static motion.

- **Kling 1.6.** Simplified prompts. Keep it very simple.
- **Kling 2.1 Pro.** 1080p at 30fps. Motion Brush. End frame control.
- **Kling 2.5 Turbo Pro.** Maximum 3-4 distinct elements.
- **Kling 2.6 Pro.** 5-7 elements. Motion Control. Element Binding for character consistency.
- **Kling 3.0.** Multi-shot in one generation (up to 6 shots). Native audio with dialogue and lip-sync. 15s continuous output. Native 4K, up to 60 fps. Strongest character and scene consistency. Two tiers: v3/pro and v3/standard.
- **Kling 3.0 Turbo** (June 2026). Speed/price tier: audio included in base cost, noticeably better lip-sync on talking heads, 3-15s, but capped at 1080p — no 4K.
- **Kling 3.0 Omni** (June 2026). The reference-and-editing flagship (API alias `o3`): strongest input understanding, editing pipeline at 3-15s with 4K in/out, Elements 3.0 with voice binding (see section 7).

If in doubt about the user's version, ask. The prompting protocol differs between 1.x – 2.x (sections 4-9) and 3.0 (section 3).

## 3. Kling 3.0 — multi-shot, native audio, 15s

Kling 3.0 is a different beast. It understands cinematic intent, not just visual descriptions. Prompts read like scene directions, not object lists.

### What changed vs 2.x

| Capability | 1.x – 2.6 | **3.0** |
|---|---|---|
| Multi-shot in one generation | No (one continuous take) | **Yes — up to 6 shots** |
| Native audio | Limited / off | **Yes — dialogue, ambient, voice tone** |
| Lip-sync | No | **Yes — coherent across multi-character scenes** |
| Max duration | 5-10s | **Up to 15s** |
| Character labeling | Via Element Library + reference images | **Via in-prompt `[Character A: ...]` tags** (still supports references) |
| Cinematic language understanding | Partial | **Full — reads "shot-reverse-shot", "POV", "tracking shot", "macro close-up"** |

### Five-layer prompt structure

```text
Scene  →  Characters  →  Action  →  Camera  →  Audio
```

Write each layer as flowing prose with explicit labels.

### Anchor subjects early

Introduce every character and key object at the **start** of the prompt, before any shot description. Use unique consistent identifiers — the same label survives across all shots:

```text
[Character A: Exhausted Partner — late 40s, gray-streaked beard, navy peacoat, hollow eyes]
[Character B: Female Investor — early 30s, sharp blazer, calm posture]
```

Then refer to them as "Character A" / "Character B" inside shot descriptions. This locks identity better than re-describing the character each shot.

### Multi-shot syntax (think in shots, not clips)

```text
[Character A: ...]
[Character B: ...]

Master intent: tense negotiation in a glass-walled office at dusk.

Shot 1 (0-3s). Wide tracking shot. Character A enters frame from left, crosses to the table.
Shot 2 (3-6s). Profile close-up on Character A. He sets down a brown leather folder.
Shot 3 (6-9s). Shot-reverse-shot. Cut to Character B's face. She does not blink.
Shot 4 (9-12s). Macro insert on her hand tightening around a fountain pen.
Shot 5 (12-15s). Two-shot, low angle, both reflected in the glass wall behind them.

Camera. Slow, deliberate. Sony FX6 feel, 35mm and 85mm.
Lighting. Cold blue dusk through floor-to-ceiling windows. Single amber desk lamp.
Audio. Distant city ambience. No music. Footsteps on hardwood. Pen clicks on paper.
```

Each shot must answer: **framing + subject + motion**. Empty shot descriptions ("static frame, ambient mood") collapse into one continuous take.

### Dialogue protocol (P1-P4)

For any speaking scene, follow these four rules. The fal.ai guide calls them P1, P2, P3, P4.

**P1. Structured naming.** Use unique identifiers per character.
- ✓ `[Character A: Black-suited Agent]` and `[Character B: Female Assistant]`
- ✗ "[Agent] says... Then, he says..."

**P2. Visual anchoring before dialogue.** Bind dialogue to a unique action first.
- ✓ "Character A pulls a folded note from his pocket and reads aloud: 'It's not what you think.'"
- ✗ "Character A says 'It's not what you think.'" (no visual anchor → lip-sync drifts)

**P3. Voice tone in the tag.** Assign emotion / texture inline.
- ✓ `[Character A, raspy deep voice]: "We're out of time."`
- ✓ `[Character B, clear fearful voice]: "Don't open it."`
- ✗ `[Man]: "We're out of time."` (vague — model picks a generic voice)

**P4. Temporal control between lines.** Use linking words to prevent dialogue from merging.
- ✓ "Character A: 'I won't ask again.' **Immediately,** Character B: 'You don't have to.'"
- ✗ Two consecutive `[Character X]: "..."` lines with no transition (model overlaps them)

### Image-to-video on 3.0 — lock first, then move

The input image serves as the anchor for identity, layout, and on-image text. Keep the prompt short and motion-focused. Describe **how the scene evolves from the image**, not what is in the image.

```text
Preserve identity, wardrobe, and the storefront sign exactly.
[Character A: same person from the image]
Shot 1 (0-2s). She turns her head toward camera, exhales.
Shot 2 (2-5s). Slow push-in to a tight close-up. Wind catches her hair.
Audio. Distant traffic, wind through awnings, a soft bell from inside the shop.
```

### Cinematic vocabulary that 3.0 actually understands

Use these terms directly — the model treats them as instructions, not flavor:

- Framing: profile shot, three-quarter, macro insert, two-shot, OTS, POV, low angle, high angle, Dutch
- Edits: shot-reverse-shot, match cut, smash cut, J-cut, L-cut
- Camera moves: tracking, dolly, push-in, pull-out, whip pan, crane, handheld, orbital / 360 spin, Steadicam, drone-like aerial. Composites work: "pan right while tilting up".
- Lens feel: 35mm, 50mm, 85mm, 100mm macro, anamorphic 40mm
- Tempo words the model obeys: "ultra-slow motion" (2-3s feel), "slow and deliberate" (5-8s), "moderate" (3-5s), "quick snap" (1-2s); exact timing works too ("5-second dolly zoom").
- Angle carries emotion: low angle = dominance, high angle = vulnerability, eye-level = neutral. Pick per the power dynamic from `dramaturgy.md` §6, not at random.
- In the Kling app, Master Shot presets ("Move Forward and Zoom Up" etc.) are more stable than hand-written camera prose and save credits — prefer them for standard moves, prose for motivated ones.

### Default model choice

If the task hits any of these — **use Kling 3.0 over earlier Kling**:
- Multi-shot dialogue scenes
- 10-15s continuous narrative
- Lip-sync required
- Multi-character with distinct voices
- Image-to-video where text on the image must stay legible

Within the 3.0 family: talking heads and dialogue on a budget → **Turbo** (best lip-sync per dollar, audio included, 1080p cap); reference-heavy or editing work, 4K delivery → **Omni**; everything else → base 3.0.

For everything else (single clip, no dialogue, < 10s, character lock via reference images, Motion Brush) — older versions still work and are cheaper.

### API parameters (3.0, fal/official)

- `cfg_scale` 0-1, default 0.5. 0.3-0.4 = creative freedom, 0.7-1.0 = strict prompt adherence (product / explainer work).
- `duration` — per-shot durations must sum to ≤ 15s.
- `aspect_ratio` — 16:9 / 9:16 / 1:1.
- `generate_audio` — bool. There is no "no music" toggle: the model lays music even against a negative prompt. If you need clean audio, generate with audio off or strip the track in post.

## 4. Prompt formula (1.x – 2.x)

For 1.6, 2.1 Pro, 2.5 Turbo Pro, 2.6 Pro:

```text
Subject (with specific details)
+ Subject Movement (one clean verb phrase)
+ Scene (3-5 elements max)
+ Camera Language
+ Lighting
+ Atmosphere
```

Write as flowing prose. Kling 1.x – 2.x dislikes fragmented tag-style inputs.

For Kling 3.0, use the multi-shot structure from section 3 instead.

## 5. Prompt length by model

- 1.6. Keep it simple, minimal.
- 2.5 Turbo Pro. 3-4 elements max. 50-80 words.
- 2.6 Pro. 5-7 elements. 50-80 words.
- 3.0. Longer prompts welcome — multi-shot needs explicit structure (see section 3). Plan ~30-60 words per shot.
- Image-to-video (any version). 20-40 words. Shorter, motion-focused.

Long prompts on 1.x – 2.x = melted outputs. Compress ruthlessly. On 3.0, structure beats length.

## 6. Negative prompts (critical rule)

Kling has a dedicated negative prompts field. The field auto-interprets input as exclusion. Do not write "no X". Write the thing itself.

Bad. "no robots"
Good. "robots"

Bad. "no blurry faces, no distorted hands"
Good. "blurry faces, distorted hands, melted features"

Common effective negatives.

```text
low resolution, blurry, distorted hands, extra fingers, melted face, watermark, subtitles, logo, text overlay, jitter, shaking camera, deformed
```

Keep the list short. Long negative stacks reduce motion and detail.

## 7. Element Library and Element Binding (1.x – 2.x)

For character consistency across generations, Kling has an Element Library. Upload 3-4 reference images of the character from different angles.

Required angles.

- Front
- Side (profile)
- Three-quarter

Then in Image-to-Video settings, enable "Bind Elements" to lock features. This gives the AI a visual anchor that survives camera pans and light changes.

Source image rules.

- 1080p or higher.
- Even lighting. Avoid hard shadows. The AI can mistake them for permanent facial features.
- No text or watermarks.
- Clean uncluttered background.
- Centered subject.
- Well-contrasted.

For Kling 3.0 — Element Library still works, but the in-prompt `[Character A: ...]` labels (see section 3) are usually enough on their own.

### Elements 3.0 (Omni)

On 3.0 Omni the element system got deeper:

- A character element takes either a **3-8s video** (the model extracts both appearance and voice) or up to **4 multi-angle stills** (front, three-quarter, profile, back), plus optional **voice binding** (5-30s audio clip). Once bound, the voice belongs to the subject — do not re-describe it in the prompt.
- Define a character / product / location **once** as an element, then tag it in prose: `@Grace picks up the folder`. The prompt carries only action and camera; identity lives in the element.
- Holds 3+ distinct characters in frame without feature blending — but only if **each** has its own element.
- Cost of the feature: several practitioners report visible image-quality degradation the moment elements/references are enabled. Use elements only when consistency actually matters; for one-off clips, in-prompt labels are cleaner.

## 8. Motion Brush (unique)

Animate up to 6 regions of a single image independently. Each region gets its own motion path.

Critical rule. The text prompt MUST match the brush motion. If you brush a river flowing and write "stagnant pond" the model tears itself apart. Align prompt verbs with brush directions.

## 9. Motion Control (2.6 Pro, unique)

Copy motion from a reference video. Use when you need specific performance or choreography (dance, martial arts, specific gait). The prompt then focuses on subject description only, the reference handles motion.

## 10. Image-to-video rule

Keep the prompt short (20-40 words). Focus only on motion. Do not re-describe static elements the model already sees.

Include explicit continuity cues. Kling responds well to "preserve X" instructions.

Example.

```text
Preserve silhouette and label text. Slow tracking shot from the side. She turns her head toward camera. Wind catches her hair. 35mm, golden hour rim light.
```

For Kling 3.0 image-to-video — see section 3 ("Image-to-video on 3.0 — lock first, then move").

## 11. Failure modes and fixes

### Random camera drift in static scenes

Fix. Say "locked static frame" or "camera fixed, no movement."

### Prompt exceeds model capacity, output melts

Fix. Cut to model-appropriate element count. 3-4 for Turbo, 5-7 for 2.6 Pro.

### Character face changes between generations

Fix. Upload 3-4 reference images to Element Library. Use Bind Elements in the settings.

### Negative prompts ignored

Fix. Rewrite "no X" as "X" in the negative field.

### Motion Brush artifact

Fix. Check that the text prompt verbs match the brush direction. Rewrite the text if it contradicts the motion.

### Element overload melts hands

Fix. Simplify. Combine elements where possible. Cut secondary descriptions.

### Kling 3.0 collapses multi-shot into one continuous take

Fix. Make shot boundaries explicit: `Shot 1 (0-3s). ... Shot 2 (3-6s). ...`. Each shot description must include a different framing or camera angle. If two adjacent shots share both framing and angle, the model merges them.

### Kling 3.0 dialogue lip-sync drifts

Fix. Apply P2 — bind dialogue to a unique visual action ("Character A pulls a folded note from his pocket and reads aloud:") before the line itself. Then add P4 linking words ("Immediately,") between consecutive lines.

### Kling 3.0 picks the wrong voice

Fix. Apply P3 — put voice tone inside the speaker tag: `[Character A, raspy deep voice]:`. Generic `[Man]:` / `[Woman]:` tags get a generic voice.

### Image quality drops when Elements / references are enabled

Fix. Strip references to the essential ones only; for one-off clips prefer in-prompt `[Character A: ...]` labels over elements. Accept the trade: elements buy consistency, not fidelity.

### Two similar characters blend features in one frame

Fix. Give each character its own element (or its own labeled identity block). Never let two speaking characters share one visual description.

### Morphing artifacts on fast motion

Fix. Generate the action in slow motion and speed it up in post — the model holds geometry at slower internal motion.

### Music appears even though the prompt says "no music"

Fix. Negative-prompting music is unreliable. Generate with `generate_audio` off and add sound in post, or strip the music track.

## 12. Skeleton

### Text-to-video (1.x – 2.x)

```text
[Subject with identity anchor]. [Subject movement in one clean verb phrase]. Scene. [3-5 environment elements]. Camera. [one movement + lens]. Lighting. [source + quality]. Atmosphere. [mood].

Negative field. blurry, distorted hands, extra fingers, melted face, watermark, subtitles, jitter.
```

### Image-to-video

```text
Preserve [silhouette / label / specific feature]. [Camera movement, one lens]. [One or two motion verbs]. [Atmospheric cue, light change].

Negative field. blurry, distorted hands, melted face, jitter.
```

### Worked example. Fashion, image-to-video (2.6 Pro)

```text
Preserve silhouette and fabric texture. Slow lateral tracking, 85mm. She turns her head toward camera, exhales through her nose, hair catches golden hour wind. Warm rim light. Confident stillness.

Negative field. blurry, distorted hands, extra fingers, melted face, watermark, motion blur, jitter.
```

### Multi-shot with dialogue (Kling 3.0)

```text
[Character A: Investigator — late 30s, navy raincoat, tired blue eyes, three-day stubble]
[Character B: Witness — early 20s, oversized hoodie, hands wrapped around a paper cup, eyes red from crying]

Master intent: a 12-second interrogation in a fluorescent-lit precinct break room at 2am. The investigator holds back, the witness breaks.

Shot 1 (0-3s). Two-shot, eye level, 35mm. Character A sits across from Character B. Static frame.
Shot 2 (3-6s). OTS over Character A's shoulder. Character B's hands tighten on the paper cup.
Shot 3 (6-9s). Profile close-up on Character A. He slides a photo across the table.
[Character A, low even voice]: "You were there."
Shot 4 (9-12s). Reverse — close-up on Character B. She does not look up.
Immediately, [Character B, fragile broken voice]: "I didn't see anything."

Camera. Locked frames, no movement except the slide of the photo. Sony FX6 feel.
Lighting. Cold overhead fluorescent, slight flicker. Pale skin, hard shadows under the eyes.
Audio. Distant police radio chatter, the buzz of the fluorescent tube, a vending machine humming in the corridor. No music.

Negative field. blurry, distorted hands, extra fingers, melted face, watermark, subtitles, jitter, dialogue overlap.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/patterns-and-genres.md

# Montage patterns and genre modules

## Contents

1. Montage patterns (6 ready structures)
2. Genre modules (7 archetypes)
3. Multi-clip story structure

---

## 1. Montage patterns

These are pre-built structures that solve common scene types. Pick one, fill with your specifics.

### Pattern 1. Escalation

Use for tension builds, reveals, dramatic emphasis.

```text
wide -> medium -> close-up -> macro -> reaction close-up -> impact
```

### Pattern 2. Anxiety

Use for psychological pressure, internal conflict, impending bad news.

```text
face -> object -> hand -> face -> object closer -> sound cue -> sudden stillness
```

### Pattern 3. Discovery

Use for revealing a hidden element, exploration, search.

```text
POV -> empty space -> searching hand -> hidden object -> rack focus -> emotional reaction
```

### Pattern 4. Catastrophe

Use for comedic or dramatic disaster. Tiny object failures play bigger than explosions.

```text
anticipation -> object instability -> reaction -> object falling -> impact -> silence -> emotional collapse
```

### Pattern 5. Commercial product drama

Use for ads with a hero product.

```text
lifestyle setup -> product reveal -> macro texture -> human reaction -> use moment -> hero product shot
```

### Pattern 6. Music video loop

Use for rhythmic repetition, transformation, performance.

```text
gesture A -> cut -> gesture A from new angle -> cut -> transformation -> repeat gesture A -> release
```

---

## 2. Genre modules

Each genre has a distinct visual grammar. Match style and rhythm to the genre.

### Domestic tragedy

Ordinary objects treated with extreme seriousness. Tiny event as cosmic disaster.

- Style. Cold night interior. Mundane location. Dramatic close-ups. Slow push-ins. Macro inserts. Sudden silence.
- Tone. Tragicomic. Absurd sincerity.
- Pace. Slow build, longer reaction shots.
- Example. A man discovering his fridge is empty, played like a Greek tragedy.

### Music video

Rhythm. Repetition. Visual motif. Transformation.

- Style. Repeated gestures. Match cuts. Performance fragments. Visual loops. Color-coded sections. Aggressive lens changes.
- Tone. Emotional intensity. Sensory overload with readable structure.
- Pace. Fast, beat-driven.

### Commercial

Clarity. Product logic. Sensory detail.

- Style. Clean lighting. Intentional macro. Clear product visibility. Controlled movement. Readable final hero shot.
- Tone. Desire. Transformation. Benefit shown through action.
- Pace. Medium, building to hero shot.

### Psychological drama

Pressure. Stillness. Negative space.

- Style. Locked frames. Long close-ups. Reflections. Obstructed framing. Quiet sound design.
- Tone. Internal conflict. Hidden tension. Emotional compression.
- Pace. Slow, sustained.

### Action

Spatial clarity above all else.

- Style. Establishing geography. Clear direction of movement. Impact inserts. Wide shots between close-ups. Strong eyeline continuity.
- Tone. Urgency. Force. Readable chaos.
- Pace. Fast but geometrically clear.

### Race / speed

Authentic velocity. Faceless detail-as-emotion. Cold combative palette.

- Style. Low bumper-height. Asphalt streaking in frame. Foreground reference objects passing. Hard light on metal/rubber/sweat. Beat-locked cutting that collapses toward the launch.
- Tone. Threat, not glamour. Force transmission over shiny bodywork.
- Pace. Silence-then-bang. Held ritual, exploding launch, dense contest, one held aftermath.
- For the full grammar (schools, start-line ritual, 5 shot families, drift adaptation, anti-fake guard) load `race-and-speed.md`; for turning it into still panels load `animatic-keyframes.md`.

### Fashion

Symmetric framing. Controlled palette. Repeated silhouettes.

- Style. Slow motion micro-beats. Macro fabric detail. Confident stillness. Rim light.
- Tone. Assured. Sensual.
- Pace. Slow, intentional.

### UGC / Social

Authentic. Vertical. Quick.

- Style. Handheld. Natural light. 9:16. Vertical compositions. Direct-to-camera gestures. Quick beats.
- Tone. Immediate. Casual. Urgent relevance.
- Pace. Rapid, thumbnail-readable.

---

## 3. Multi-clip story structure

AI video generators have no memory between generations. Longer videos live in multiple clips stitched in the edit.

### Default splits

- 10s. 2 clips x 5s
- 15s. 3 clips x 5s
- 30s. 6 clips x 5s
- 45s. 9 clips x 5s
- 60s. 12 clips x 5s

Exception. Seedance multi-shot can pack 2-3 shots into a single 5-10s clip.

### What every clip must repeat

Every clip is self-contained. The model has no memory. Repeat this block in every clip.

- Character identity (face, hair, clothing, distinguishing marks)
- Clothing items, exactly named
- Location description
- Visual style (palette, grade, reference)
- Camera language (dominant grammar of the whole piece)
- Lighting logic (dominant source and direction)
- Continuity rules (what must remain constant)
- Color palette with specific colors

Yes, every single clip. Yes, even if it feels repetitive. That repetition is the only thing keeping the output consistent.

### Timecoded internal beats

Inside each 5-second prompt, use timecodes.

```text
0.0-0.8. [action / camera / light]
0.8-1.6. [action / camera / light]
1.6-2.5. [action / camera / light]
2.5-3.7. [action / camera / light]
3.7-5.0. [action / camera / light]
```

Density by genre.

- Emotional drama. 3-4 beats per 5s. Longer reactions.
- Standard narrative. 4-7 beats per 5s.
- Fast montage / music video. 6-9 beats per 5s.

Use timecoded structure for Seedance and Veo. Kling prefers flowing prose.

### Continuity across clips

When moving from clip N to clip N+1, the first beat of the new clip should match the final beat of the previous clip. Character in same pose. Same light. Same color temperature. This is what makes them cut together cleanly in the editor.

Example. Clip 1 ends on him reaching into the fridge. Clip 2 opens on his hand inside the fridge at the same height and light.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/race-and-speed.md

# Race, speed and faceless kinetic montage

Domain grammar for dynamic race spots — drag, drift, chase, drag-strip, kinetic montage. The brief is brutal: faces are banned, the deliverable is **still keyframes (opornye kadry)** for an animatic, and a frozen panel must read as lethal velocity at a glance. Speed is not a post effect — it is a photographic fact built from spatial cues that imply the missing motion. Emotion does not live on a face; it rides on metal, rubber, road, gauges and light. Load this file when the task involves racing, drift, drag, chase, speed, dynamic or kinetic montage, "гонщик", or "раскадровка гонки".

This file **specializes `animatic-keyframes.md` for the race domain.** That file owns the general still-panel method and is the prerequisite read: the keyframe card, the **six motion-as-still cues** (§4), the **5-cue speed budget** (§4), the **EMOTION→OBJECT substitution table** and state-change cheat-sheet (§5), the loaded-frame depth method (§6), the **density ladder** (§3), the **keyframe→image-gen prompt skeleton** (§7), the worked 30s board (§8), and the **master per-panel checklist** (§9). This file does **not** repeat them — it adds the race grammar on top: the schools, the start-line liturgy, the shot families, the drift ritual, the Christmas-Tree light logic, and the cold-combat palette. Where the method is general, this file points; where it is race-specific, it teaches.

Sits on top of `dramaturgy.md` (§2 Details Law, §3 fantik, §9 environment, §11 shot card, §12 rhythm ladder, §15 check), `universal-rules.md` (U1–U12), `role-modes.md` §4 (shot-function taxonomy). Pairs with `camera-lighting-vocabulary.md` for framing/lens/light tokens, `patterns-and-genres.md` for the action/escalation arc, and `seedance.md` / `kling.md` / `veo.md` to animate each locked keyframe.

## Contents

1. Core laws (the non-negotiables)
2. Four schools worth stealing
3. Selling speed in a single frame
4. Storytelling without faces — the race captioning system
5. The race ritual (liturgy) + the 5 shot families
6. Camera grammar for speed
7. Light & color for speed without faces
8. Sound & rhythm
9. 30-second structure (beat map)
10. Anti-fake guard

---

## 1. Core laws (the non-negotiables)

Six laws govern every race panel. Break one and the spot collapses to a car commercial.

1. **Authentic speed, never CGI-clean or sped-up.** Build velocity into the static composition (§3); never lean on a ramp to rescue a dead frame. Over-crank, glass-smooth stabilization and post speed-ramps read subconsciously as "ad-speed" and drain all threat. Squat, lifted nose, slick wrinkle, smeared rim — the physics has to be visible in the still.
2. **Detail is the emotion.** Faces banned, feeling renders only on a knuckle, a needle, a pedal, smoke, or a sweat bead (`dramaturgy.md` §2; the full substitution method is `animatic-keyframes.md` §5). A hand mid-grip is the no-face equivalent of a close-up on the eyes. No abstract "motion", no named feeling.
3. **One governing visual promise per piece.** A 30s cut earns cohesion from a single conceit: everything through reflections in painted metal, or everything through circles (tach → headlight → bulb → wheel), or everything as machine-talks / no-music. Kon's "one visual principle". Name it before boarding.
4. **Beat-locked cutting.** Loudness in the audio = shot count on the board (§8; the density ladder itself is `animatic-keyframes.md` §3). Silence = one held panel. Bang = a burst of 4–8-frame micro-panels. Cut length is engine RPM made visual: idle = long panels, redline = collapsing panels toward the green.
5. **Cold combative palette** (§7). Steel blue, cyan, magenta, dirty mercury-white; **red as danger accent only** (brake glow, redline, tail-lights, the Tree's bulbs). No warm cozy amber wash — warmth appears only as toxin. Steal Tony Scott's grain, contrast and overexposure; **discard his warm grade.**
6. **Every insert is load-bearing.** Each detail panel must be captionable with one race label — *setup / commitment / mistake / recovery / proof-of-speed / result* (§4). If you cannot label it, it is a *fantik* (`dramaturgy.md` §3) — drop it. A board that is all proof-of-speed with no commitment/mistake/recovery is a reel, not a story.

---

## 2. Four schools worth stealing

Four traditions, compressed. Each ends in its one transferable rule.

**Kinetic montage (Wright, Ritchie, Boyle, Scott, Vaughn, Raimi, Aronofsky).** Time is elastic, every prop is a trigger, prep is an event. A keyframe cannot ramp or whip — so each moving trick compresses into one frozen cue (the six cues are catalogued in `animatic-keyframes.md` §4). Aronofsky's hip-hop montage is the single most transferable engine for prep-without-faces: a 6–9-panel ultra-CU strip of the start ritual, each panel one beat with a locked sound cue, the cluster **repeated two-to-three times with escalation** (calm → strained → violent). Repetition is memory; memory is emotion.
→ **Rule:** never write "motion" — write the artifact motion leaves behind, and never board a neutral panel (every frame carries a forward vector, negative space ahead of the subject).

**Race-truth (Frankenheimer, Lelouch, Mangold/Papamichael, Howard/Dod Mantle, Refn).** Speed is a fact you earn by putting the camera where a real rig could bolt — bumper, hood lip, hostess-tray, axle, cabin. Low, wide and close, hard-mounted without vibration isolation so "cheeks shake", asphalt streaking in frame as the speedometer, mini-cams next to pistons and swelling tires for "an electron-microscope view of the car at its limit". Refn's cocoon: silence and stillness inside the shell, chaos outside, so the launch detonates. Refuse the crank — *Grand Prix* oiled tires for real smoke rather than fake the burnout.
→ **Rule:** if the implied camera could not physically mount on the car, the panel reads as render — drop it to bumper height and bolt it on.

**Loaded composition (Bong, Park, Anderson, Kon).** With no faces, geometry and the depth stack do the acting (the FG/MG/BG depth method is `animatic-keyframes.md` §6). One geometric spine (centerline or Christmas Tree as the axis); every object an evidence (Park: "each object is a clue") or it is cut. Symmetry is handwriting — one held symmetric "breath" frame says balanced rivalry; break it the instant one car noses ahead. Kon's graphic-match pairs compress time across two adjacent keyframes sharing a shape at the same size and screen position.
→ **Rule:** a panel answers one question in the first glance and rewards a second look — one focal point, one emotion, three depth layers, zero dead objects.

**Rule-based ad (Honda *Cog*, Audi Quattro, Nike/Ritchie, Goodyear).** The drama is pure mechanism: every object does something irreversible, "let the machine talk" (no music), the entire spot first-person with no hero face. Tension is "will it fire". A static fetish shot of a gear lever flatlines; an object crossing a threshold says a decision just happened.
→ **Rule:** objects carry feeling only when they visibly **change state** — board the "after" (needle pinned in the red, ignition lamp blooming live, slick caught mid-fold), the "before" is implied.

---

## 3. Selling speed in a single frame

A still has no engine note and zero motion. It sells velocity through the **speed-budget rule** — a frame reads fast only when **≥3 of five cues coexist** (camera at/below bumper height · asphalt streaking the lower frame · a near foreground reference passing the edge · sharp hero against motion-blurred background · a mechanical-vibration cue). The full rule, with the anti-fake firewall, lives in `animatic-keyframes.md` §4; do not re-derive it. One cue is a car photo; three is velocity; five and even a parked car reads dangerous. If a "fast" panel can't name three, reframe lower, drag the camera to the asphalt, throw a barrier into the foreground.

Two race-domain extensions the general file does not carry:

**The foreground reference catalog** (cue *c*, the cheapest and strongest speed multiplier). Place the reference *near the lens* (so it smears most) and *passing the edge* (so it reads as transiting, not parked). Keep one near object tack-sharp so the brain measures the smear against it.

| Reference object | Where to place it | Speed it implies |
|---|---|---|
| Cone / timing block | near edge, elongated/smeared | lane-level rush |
| Armco barrier / wall | scraping the near side, streaked | proximity + velocity |
| Lane stripe / chevron | lower frame, smeared toward bottom | ground speed |
| Christmas-Tree pylon | foreground, sharp anchor; car blurred | launch reference + timer |
| Tree / lamp post / grandstand | whipping past, motion-rod | open-road pace |
| Tire smoke / spray | raked by backlight across frame | force + air movement |
| Marshal / crowd at periphery | blurred, fragmented | scale + danger |

**Long-lens compression** — the second speed register and the antidote to "only blur sells speed". Frankenheimer's 1000mm stacked distant cars onto the hero so closing distance reads as collapse. Pair compression panels with low-wide panels in the cut; never board the whole spot on one lens. In `seedance.md`/`veo.md` syntax name "motion blur, fast-shutter look on background, sharp subject" explicitly — models default to over-clean stabilization (the prompt skeleton is `animatic-keyframes.md` §7).

(The full "what kills the speed" audit lives once, in §10.)

---

## 4. Storytelling without faces — the race captioning system

A face does four jobs: internal state, where it looks, the cost, the decision. Banned, those jobs redistribute — **decision → anatomy mid-action; internal state → an object crossing a threshold; looking/rivalry → space.** The mechanism, the EMOTION→OBJECT substitution table and the state-change cheat-sheet are owned by `animatic-keyframes.md` §5; do not duplicate them. Two filters before you draw: name the **verb** on any hand/foot panel (grip / latch / shift / preload / release — no verb, no panel), and board only the **after** state of any object threshold (Honda *Cog*). Pick ONE hero object and board it three times at rising intensity — beats twelve unrelated inserts (`dramaturgy.md` §13).

What this file owns is the **race captioning system** — the margin label that proves an insert is load-bearing (Law 6). Every detail keyframe gets exactly one. If you cannot assign one, drop the panel.

| Label | Story job | Typical object / crop | Skill tag (`role-modes.md` §4) |
|---|---|---|---|
| **setup** | establishes capability / readiness | glove pull, harness latch, ignition dead | Establish / Detail |
| **commitment** | point of no return chosen | foot pins throttle, shifter rammed home, ignition live | Shift / Impact |
| **mistake** | something slips / over-limit | tire shake, wheel fights back, revs flare wrong | Pressure / Impact |
| **recovery** | control reclaimed | hand catches the correction, tach settles back into band | Shift |
| **proof-of-speed** | force is real, not staged | chassis squat, slick wrinkle, exhaust flame, asphalt streak | Power / Pressure |
| **result** | who won the inch | finish stripe, slicks ballooned at trap, one nose ahead, chute bloom | Impact / Aftermath |

(Banned panels are consolidated in §10.)

---

## 5. The race ritual (liturgy) + the 5 shot families

The race is not a chase, it is a *liturgy*. Every phase is a legible, irreversible state-change a knowing viewer reads instantly — muddle the order and the spot dies. The countdown *tightens cut length toward the green*, then explodes: the drag-specific instance of the `dramaturgy.md` §12 rhythm staircase. Draw one anchor keyframe per beat. In a faceless spot **Reaction** is reassigned from a human face to the *machine's* face — the needle jumping, the slick wrinkling, the nose squatting. Gauges and rubber are the actor.

| # | Ritual beat | Function | Keyframe to draw (still) | Light (cold) | Emotion |
|---|---|---|---|---|---|
| 1 | Water box entry | Establish | Front slick easing into mirror-still water, chalk/box edge in frame, bulbs reflected in the sheet | Steel-blue dusk, wet specular | coiled stillness |
| 2 | Burnout (white→blue) | Power | Ground-level wall of smoke off the rear, plume backlit; car straining on line-lock | Hard cyan backlight through smoke | barely-leashed force |
| 3 | Reverse settle | Pressure | Rear rolling back through its own drifting smoke toward the beams, tail-lights bleeding red into haze | Smoke haze, low key, red tail wash | deliberate menace |
| 4 | Pre-stage bulb | Pressure | Front tyre creeping, top blue bulb lit as anchor, beam line as a graphic spine on asphalt | Blue bulb glow on wet metal | held breath |
| 5 | Stage bulb | Pressure | Second blue bulb lit, tyre on the line, knuckles whitening on wheel/trans-brake (depth: bulb BG, hand FG) | Two blue bulbs, deep black | point of no return |
| 6 | Amber countdown | Pressure→Shift | The Tree as timer — three ambers, sequential (see below) | Amber pulse (the only narrative warm light) | trigger tension |
| 7 | Green / launch | Impact | Both cars squatting on rear suspension, front wheels lifting, asphalt streaking back | Green flash + hard flare | release / violence |
| 8 | Slick wrinkle (hero) | Detail/Reaction | Macro into rear sidewall folding/wrinkling as it hooks — *the* hero detail, the held/ramp beat | Hard side light, smoke bloom | physics made visible |
| 9 | Shift / exhaust flame | Detail | Hand slamming shifter with chassis twist, OR header pipe spitting flame | Flame as warm spark in cold frame | escalation |
| 10 | The pass | Power | Joust / parallel tracking, asphalt streaking, rival lane in frame | Streaked specular, motion-rod lights | duel |
| 11 | Finish | Impact | Top-end: slicks "blown up"/distorted, cars inches apart crossing the line, one nose ahead | Cold-white finish pool | margin |
| 12 | Chutes / aftermath | Aftermath/Exit | Parachutes blooming, smoke drifting through headlight beams, OR hand unclenching off the wheel | Falling light, residue haze | consequence |

**Amber logic (decision point).** Choose the **Sportsman / full tree** for an ad: three ambers fire *sequentially 0.5s apart* — three drawable keyframes, a stretched drum-roll of dread with cut length collapsing toward the green. The Pro tree fires all three at once — one panel, brutal but no build. Draw the Sportsman stagger. Always leave on the **last amber, not the green** (holeshot): the launch keyframe precedes the green-lit panel by a frame, which makes it read as *anticipation*, not reaction.

**Drift adaptation — the slip-angle liturgy.** Drift swaps the countdown for a *continuous angle ritual*: **approach → entry → clutch-kick initiation → counter-steer hold → clipping point (wall proximity) → smoke wall → transition (flick) → exit.** The **counter-steer** replaces the slick-wrinkle as the "physics made visible" anchor — ECU/CU of hands wound into opposite lock, forearms crossed, wheel at full angle, cold side-light on knuckles, the steering angle drawn large and unmistakable. **Wall proximity** is danger without a face: barrier hard and sharp in the foreground layer, car door a hand's-width away, motion-streak on the wall texture — the gap *is* the emotion. The **transition flick** is yawed mid-switch, smoke crossing the frame diagonally, both exit directions readable.

### The 5 shot families

Rotate among all five across the 30s — speed reads through *changing perspective*, not long takes. Each family has one job and a default composition.

| # | Family | Job (function) | Put in the still panel | Authenticity tell |
|---|---|---|---|---|
| 1 | **Hostess-tray side profile** | Detail / Power | Side-mounted outside the door: hand on wheel/shifter, or rear-quarter wheel filling frame; asphalt streaking behind | door/window line anchors scale; rubber works in frame |
| 2 | **Hood / bumper low forward POV** | Pressure / Impact | Predatory low forward look: asphalt rushing under the nose, cones/Tree/markers growing fast, lane stripe strobing; fisheye edge optional | road texture under the car = velocity |
| 3 | **Hard-mounted cabin shake** | Pressure / Reaction | Rigid interior mount: dash/needle/hands vibrating, mirror trembling, world shuddering through glass | visible micro-vibration; never perfectly stable |
| 4 | **Tracking / chase parallel + joust** | Power / Reveal | Camera car alongside (parallel) or closing head-on offset (joust); rival lane in frame, roadside lights as streaks | closing distance + streaked surroundings |
| 5 | **Distant proof shot** | Establish / Aftermath | Long locked lens: two cars as small hard shapes crossing huge space, smoke trail, barriers narrowing perspective | space covered brutally fast; one breath of stillness |

---

## 6. Camera grammar for speed

The **six motion-as-still cues** (smear / partial blur / streak / vector / sharp-blur separation / held stillness) are catalogued in `animatic-keyframes.md` §4. This table is the complementary layer: the camera *move* the user names, resolved into one still composition. Format: technique — what it does to emotion — application in a keyframe/panel.

| Technique | What it does to emotion | Keyframe application (the still) | Tag |
|---|---|---|---|
| **Whip pan** | instant transfer of attention, reads as motion not a cut | Streak-frame between two clean panels: whole frame raked into horizontal streaks (Tree lamps, guardrail, lane stripes smeared), one shape barely surviving (a wheel arc, the shifter) | Shift |
| **Crash / snap zoom** | shock-shove into a detail; discovery, alarm | Aggressively tight macro of the trigger detail (needle slamming red, last amber bulb), faint radial/zoom-blur ring at edges, subject oversized dead-center | Detail / Impact |
| **Speed ramp** | punctuation: ramp = the breakout, freeze = exclamation mark | Frozen partial blur at the peak — sidewall wrinkle caught mid-deformation, smoke just blooming, everything else tack-sharp; one arrested ten-thousandth of a second | Impact |
| **Freeze frame** | a held breath / a one-frame dossier on an object | Deliberately blur-free locked macro, hard edges, margin caption (knuckles whitening, *committed*); the symmetrical "exhale" amid kinetic panels | Detail / Pressure |
| **POV (cockpit / impossible mount)** | identification; the viewer *is* in the car | Hands + wheel rim in hard foreground, cluster mid-ground, Tree/rival in blurred deep ground; 24mm exaggerated proximity; or genuinely impossible mount (wheel arch, exhaust mouth) | POV / Pressure |
| **Joust** | closing-distance rate spikes the sense of speed | Near head-on, car offset to one side, a cone/marker huge and blurred on the opposite edge to mark the closing gap; reserve for the climax pass | Impact |
| **Low macro (aggressor cam)** | the lens is a predator, the track attacks the frame | Bumper/grille-level skimming the asphalt, fisheye curvature at the edges, road lunging into the lens; or extreme CU under hard cold side-light — a knuckle becomes a ridge, the lever a weapon | Impact / POV / Detail |
| **Restless / handheld cam** | the frame never settles; constant threat, physiological unease | Never a perfectly level, perfectly clean panel — bake in a 1–3° drift, edge smear, off-true horizon, a faint micro-shake artifact even in a "static" cockpit | Pressure |
| **Dutch angle** | imbalance, loss of grip | Cant the horizon hard at the one loss-of-traction beat only (tyre breaking away, car stepping sideways) — reserve it so it stays loud | Impact |

Ration aggression: one bumper-fisheye lunge, one crash-zoom, one dutch — at commitment beats, not as wallpaper. Per `camera-lighting-vocabulary.md` §2, the animatic prompt supplies one dominant move per clip; the keyframe is the locked first frame.

---

## 7. Light & color for speed without faces

Faces are banned, so light is the only actor left. It does not "set a mood" — it **rims a material** so a piece of metal, rubber or skin reports the emotion a face would. General light grammar (sources, direction, quality) is `camera-lighting-vocabulary.md` §4–7; the anti-sterile firewall is `animatic-keyframes.md` §7 + `universal-rules.md` U12. The race-specific governing law: *embrace the dark* (crush blacks, ~70% of the frame unlit), *one motivated practical per panel* (Tree lamp, headlight, sodium lamp, brake glow), *light is specular not ambient* (every panel needs ≥1 hard specular hit — no specular, no information).

### The cold combative palette

| Color | Emotional job | Where it lives in the keyframe |
|---|---|---|
| Hard white / dirty mercury white | clinical pressure, the white-hot edge of commitment | top/side key on knuckles, metal lip; blown highlight on chrome |
| Cyan / electric teal | cold adrenaline, machine-alive | backlight through burnout smoke; spill on wet asphalt; rim on rear-quarter |
| Steel blue | night base, isolation, the void | negative space, deep shadow body, the unlit 70% |
| Magenta / cold violet | aggression, neon menace | practical sign spill on roofline; reflection ribbon down wet lane |
| **Red (accent only)** | danger, redline, point of no return | brake disc glow, tail-lights, Tree bulbs in lacquer, tach needle in the red |
| Green (accent only) | release, GO | the Tree's green bulb, its single reflection in a headlight lens or paint |
| Toxic amber/sodium (rationed) | temporary, contaminated, alien — never cozy | sodium lamp as a passing smear; spilled fluid catching one lamp; the Tree's three ambers as countdown only |

**Warmth as toxin** is the only permitted heat: brake-disc/exhaust glow (the machine at its thermal limit), a header flame stab gone in a frame, the Tree's alien ambers, a sickly sodium smear. Any warm element must be **point-source and surrounded by cold**. If amber fills more than ~15% of the frame it has become a wash — kill it.

### Concrete lighting recipes (drop-in for the format-C Light column: source · direction · quality · what it rims)

- **Hard key on the working hand** [Detail/Pressure]: single hard source 45° camera-side onto knuckles on the shifter — finger shadows rake the skin, sweat reads as discrete specular dots, veins as ridges, background crushed. The whitening knuckle IS the fear.
- **Backlight / rim on metal edge** [Power]: hard white or cyan source behind/above at low angle drawing one bright line down the roof gutter, mirror housing or wing edge; body in shadow, only the contour glows, against black sky.
- **Backlit smoke** [Pressure/Establish]: hard cyan or mercury-white punching *through* tire smoke from behind; volumetric shafts, the car a dark mass dissolving into glowing haze, red tail-light bleed inside the smoke for the danger accent. Front-lit smoke is dead gray nothing — always rim it from behind.
- **Brake-disc glow** [Detail/Impact]: macro on the wheel, glowing orange-red rotor through the spokes as the *only* warm element (toxic heat), rim the caliper and spokes with that glow, everything else steel blue — the one ember in a cold frame.
- **Specular on wet asphalt — the mirror** [Establish/Shift]: low bumper-height, lane stretching away, practicals (Tree, sodium lamps, headlights) reflected as long vertical smears down the wet surface as the composition's spine; pull the real lamps half out of frame, keep the mirror. Wet asphalt at night = `dramaturgy.md` §9 guilt/threat, and the cheapest way to put more cold light in frame without lifting blacks.
- **Silhouette / contre-jour** [Power/Pressure]: helmet/shoulder as pure black shape against a blown headlight or the Tree's amber bank, one thin rim defining the form plus one glint on the visor edge, no features. The brain fills the dark with something worse than any face.
- **The Christmas Tree as the scene's lamp and clock** [Pressure→Impact]: put the Tree bank in frame as the dominant practical — its glow the only key. Stage 1: two blue bulbs as cold points in the lacquer. Stage 2: three ambers blazing, amber-as-toxin spill on wet asphalt, held. Stage 3: green pops, a single green reflection streaks the hood. Match-cut the round bulb → round headlight → round tach.

**Texture and atmosphere.** Name the grain, never "clean": fine-to-medium film grain (heaviest in shadow), halation/bloom on hard practicals (soft glow ring + hard hot core), one anamorphic flare off the dominant source, slight chromatic fringe on the hottest edges (anti-sterile test in `animatic-keyframes.md` §7). One atmospheric pressure per panel (`dramaturgy.md` §9, Kurosawa) — backlit tire smoke, frozen launch grit lit on its leading edge, heat-haze warping the rimmed edge, wet asphalt as the mirror. Don't stack smoke + haze + spray in one still or it turns to mud. Keep Tony Scott's restlessness and grain; discard his warm grade.

---

## 8. Sound & rhythm

You storyboard the **sound first**; the keyframes hang off it. The general law — **loudness in the audio = panel count** — and the descending duration staircase are the density ladder in `animatic-keyframes.md` §3, sitting on the `dramaturgy.md` §12 rhythm staircase. Do not re-derive them. The race-specific rhythm rules:

- **Engine as metronome.** Tie panel *duration* to RPM: idle = ~2s panels, redline = panels collapsing 2s → 1s → 0.5s → 8fr → 4fr toward the green. The board should read as an accelerating tachometer on mute. Annotate each panel with its on-screen life.
- **Amber collapse.** The Sportsman stagger (§5) is the audible drum-roll: idle drops out on the ambers, each amber a tighter panel, the green detonates.
- **The wrinkle is the one time-expansion.** Dedicate 2–3 sequential panels to the slick folding (clean → wrinkled → gripping), marked "RAMP — hold", sound dropped (the Goodyear move) — the only place time *expands* inside the loud section.
- **Pull-to-intimate at the peak.** At the contest's tensest point, cut from a wide loud pass to an ECU of glove-on-shifter / breath-fog, shallow focus, void around it — engines stripped to breath only. The *quiet* panel goes *tight*; the loud panel goes wide.
- **Machine talks (the governing anchor).** Strip music; the `Sound` cell reads "engine + tire only" (Audi Quattro 1984).
- **Sound leads picture by 2–3fr** (J-cuts). Annotate the offset at every hard mechanical event so the incoming panel opens mid-action (shifter already moving).

Every panel inherits a `Sound` cell even though it is a still (`dramaturgy.md` §11) — prompt the *physical consequence* of the sound (deformation, particulate, smear, heat-haze, isolation-in-void), never a named sound. Fill it.

---

## 9. 30-second structure (beat map)

Five phases: **ritual → staging → launch → contest → release.** Cut length escalates toward the green, the contest stays dense, one held aftermath. ~20–26 panels. Function tags from `role-modes.md` §4. This is the structural skeleton; for a fully worked, panel-by-panel deliverable board of this exact structure (format C, ~13 rows), use `animatic-keyframes.md` §8 — do not draw a second worked board here.

| Time | Phase | Function tags | # keyframes | Panel life | Framing | Sound | Render note |
|---|---|---|---|---|---|---|---|
| 0:00–0:06 | **Ritual** | Establish, Detail, Pressure | 3–4 | 1.5–2s | Macro / ECU, locked | Idle lope, metal ticks, near-silence, music off | Held low-motion inserts: slick into water box, harness latch, finger over ignition, condensation on glass. Belief is won here. |
| 0:06–0:11 | **Staging** | Pressure, Power | 3–4 | 1s → held | Symmetric MS, Tree centered, static | Idle drops to silence on ambers; Tree relay click | Pre-stage/stage bulbs; one long *held* symmetric Tree panel = the pause. Tach trembling = the only motion. |
| 0:11–0:19 | **Launch** | Impact | 6–9 | 8fr → 4fr (burst) | Low bumper-POV, side-rig, ECU tach | BANG: tire chirp + roar, J-cut 2–3fr ahead | Hip-hop burst cluster: bumper smear, side wheelspin, tach flare, clutch hand, lane-stripe strobe. Asphalt in frame. One speed-ramp on the wrinkle. |
| 0:19–0:27 | **Contest** | Power, Shift, Reaction | 6–8 | 0.5–1s | Mirror two-shot, joust, parallel pass | Layered roar; **one pull-to-intimate / in-the-head panel** | Mirrored compositions, joust, parallel pass, one medium-wide proving ground-speed. Alternate fragment-cluster ↔ one quiet detail panel. |
| 0:27–0:30 | **Release / Aftermath** | Impact, Aftermath, Exit | 2–3 | 0.5s, then 2s hold | Wide-to-detail, smoke in beam | Hard cut to silence / one tick | Finish marker + microscopic edge, OR skip the result → engine drop, smoke through headlight beam, car nosing into dark. End on consequence, not explanation. |

Allocation: plot the board as a descending duration staircase, broken only by the one pre-launch held panel (the single most-held still, most negative space) and the one post-finish hold. The launch is *never* one hero frame — fan it into the 6–9-panel micro-burst. No two bang-clusters touch; every burst is separated by a held quiet panel.

---

## 10. Anti-fake guard

The race-specific list of panels that kill credibility — do not draw. (The general per-panel earns-its-place checklist is `animatic-keyframes.md` §9; run that on every panel as well.)

- [ ] No high, clean, "beauty" god-angle for action beats — drop to bumper height; low/wide/close beats polish.
- [ ] No perfectly stable cabin — render visible vibration (trembling mirror, doubled needle, smeared rim); tilt 1–3°.
- [ ] No long-lens speed panel without road texture or a passing reference object.
- [ ] No panel that only works "when sped up" — build the speed into the static composition (squat, lifted nose, slick wrinkle).
- [ ] No air around the car on a speed beat — crowd the near edge with barrier/rival/wall.
- [ ] No sharp wheel rim on a moving car — smear the spokes into a disc.
- [ ] No shiny-bodywork beauty pass — shoot force transmission (tire load, chassis squat, exhaust flame).
- [ ] No ritual beat out of order or skipped (§5) — a knowing viewer reads the fake instantly.
- [ ] No warm cozy grade — cold palette, red as danger accent only, amber ≤15% and toxic (§7).
- [ ] No banned panel: static fetish insert (lever/badge/wheel with no verb, no state-change); anatomy at rest; a detail you cannot caption with a §4 label; all-proof-of-speed board with no commitment/mistake/recovery; decorative dashboard clutter (keyring, dice, coffee cup — "each object is a clue"); warm wash without narrative function.

Before sending the board, run `animatic-keyframes.md` §9 (per-panel master checklist), `dramaturgy.md` §15 and `universal-rules.md` §13 over it. The most-violated step is the three-detail check — do not skip it.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/role-modes.md

# Role modes

This skill fuses three mindsets. Switch role based on the task stage. The dramaturgy layer sits underneath all three roles. For the full dramaturgy method (scene formula, Murch Rule of Six, blocking as choreography of desire, staging and subtext, three-layer storyboard, shot card template, rhythm ladder), load `references/dramaturgy.md`. Director mode leans heaviest on that file.

## Contents

1. Director mode
2. Screenwriter mode
3. Editor mode
4. Shot function taxonomy

---

## 1. Director mode

### Trigger

User asks to "придумать сцену", "разработать концепцию", "визуализировать идею", "сделай как Финчер", "предложи трактовку", "какой вайб", or shares a raw idea without structure.

### Mindset

Every shot must answer at least one of these questions. If a shot answers none, delete it.

- What changes emotionally?
- What new information appears?
- What action moves the story?
- What pressure increases?
- What does the viewer need to notice?
- Why does the camera move?
- Why does the cut happen here?

### Output format. Director treatment

```text
Core idea. [one sentence, the point of the piece]
Emotional arc. [start -> middle -> end, three emotion states]
Visual motif. [one recurring visual element]
Rhythm. [pace logic. slow build, rapid montage, still + sudden burst]
Camera language. [dominant grammar. handheld intimacy, locked precision, gliding observer]
Lighting. [dominant source and direction]
Sound. [texture. ambient layers, music role, silence moments]
Ending image. [final frame in one sentence]
```

### Style references

Use one dominant director reference per scene. Translate into concrete camera, light, rhythm, blocking. Never stack three or more references.

- Fincher. Precise motivated camera. No handheld drift. Cold palette.
- Kurosawa. Weather as emotional pressure. Rain, wind, heat.
- Spielberg. Readable staging. Clear geography. Emotional wide shots.
- Edgar Wright. Sound-driven montage. Match cuts on sound events.
- Jonathan Glazer. Music-video visual idea translated to drama.
- Wong Kar-wai. Longing. Reflections. Slow emotional drift.
- Safdie. Anxiety. Handheld pressure. Overlapping sound.
- Wes Anderson. Symmetry. Controlled blocking. Color blocks.

---

## 2. Screenwriter mode

### Trigger

User asks to "напиши сценарий", "разбей на биты", "придумай диалог", "адаптируй историю в видео", "нужен story arc."

### Mindset

Translate every beat into physical action the camera can see. Tag each beat with a shot function (see section 4). Every beat must have subtext.

### Output format. Beat breakdown

```text
Beat 1. [function] - [physical action]. Subtext. [what it means].
Beat 2. [function] - [physical action]. Subtext. [what it means].
...
Final image. [what the viewer takes with them].
```

### Dialogue format (for Veo specifically)

Write spoken lines in ready-to-paste Veo syntax.

```text
He says, in a flat exhausted voice, "We are fine. We are fine."
```

Cut lines until they fit 8 seconds of natural speech.

### Internal monologue rule

Veo cannot render internal monologue. Translate into visible bodily signal.

Bad. "He is thinking about his father."
Good. "He stops mid-motion. His eyes drift off-axis. He swallows. He resumes."

---

## 3. Editor mode

### Trigger

User asks to "собери монтаж", "задай ритм", "сделай динамично", "разбей на склейки", "как смонтировать", "сколько кадров в 5 секундах."

### Mindset

Dynamic montage is built through structure, not speed. Random fast cuts create visual soup. Readable fast cuts create propulsion.

### Rules

- Clear shot function per cut.
- Escalating frame tightness (wide -> medium -> close).
- Different camera angles per cut.
- Motivated cuts (sound event, action beat, emotional shift).
- Contrast speed and pause.
- Sound-driven transitions.
- One silence or stillness moment before a major impact.

### Output format. Timecoded beat sheet

```text
00.0-00.8. [shot function] - [framing] - [camera] - [sound cue]
00.8-01.6. [shot function] - [framing] - [camera] - [sound cue]
...
```

### Density

- Emotional drama. 3-4 beats per 5s.
- Standard narrative. 4-7 beats per 5s.
- Fast montage. 6-9 beats per 5s.

More than 9 beats in 5s creates incoherent motion regardless of model.

---

## 4. Shot function taxonomy

Every beat should carry at least one function tag. This is the editor's grammar.

- **Establish.** Where we are. Wide or master shot. Sets geography.
- **Reveal.** What appears. New information enters frame.
- **Power.** Who controls the scene right now. Staging reveals the hierarchy before dialogue does.
- **Pressure.** Tension builds. Movement toward threat or decision. Environment can carry this (flickering light, rain, steam, a tight corridor).
- **Detail.** Important object, hand, eye, texture, gesture. Macro or close-up. The anchor object often lives here.
- **Reaction.** Emotional consequence. Face response to a beat.
- **Shift.** Inner change. Body language turning point. The moment before the decision becomes visible.
- **Impact.** Decisive visual event. The drop. The hit. The break.
- **Aftermath.** Emotional residue. Stillness after impact.
- **Exit.** Final state. The image the viewer leaves with.

A full scene usually moves. Establish -> Power -> Pressure -> Detail -> Reaction -> Shift -> Impact -> Aftermath -> Exit.

A montage sequence can compress or loop. Use function tags to keep the structure readable even at high speed.

Each tag is also a question the shot must answer. Establish. Where. Power. Who commands. Pressure. What pushes. Detail. What to notice. Reaction. What it cost. Shift. What changed inside. Impact. The moment. Aftermath. The residue. Exit. The image carried out.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/seedance-25.md

# Seedance 2.5 — production reference (ByteDance, official guides of 2026-07-31)

Read `seedance.md` first for the family basics (Details Law, multi-shot syntax, 11-block skeleton). This file covers what 2.5 adds: the official prompt formulas, the 50-slot reference system, video editing, extension, ultra-long mode, and the blockout pipeline. Sources: the official Dreamina/Jimeng User Guide and Prompt Guide (both published 2026-07-31), verified against practitioner tests from the first launch week.

## Contents

1. What 2.5 changes
2. Specs and hard limits
3. Official prompt formula
4. Syntax markers for audio, dialogue and text
5. Reference discipline (the 50-slot system)
6. The 30-second structure: stages and end states
7. The anti-collapse skeleton (3 modules)
8. Realistic human formula (anti-AI-face)
9. Camera language
10. Transitions
11. Physics through consequences and triggers
12. Video editing (partial re-render)
13. Video extension
14. Ultra Long mode (30-180s)
15. Blockout and green screen
16. Storyboard grids and keyframes
17. Failure modes and fixes
18. Economics and model choice
19. Worked examples (official, verbatim)

---

## 1. What 2.5 changes

- **30-second native single-pass clip.** One generation, one continuous arc, no stitching. Extension pushes it to 60s; a separate Ultra Long mode goes to 180s (see sections 13-14).
- **50 multimodal references** (30 images + 10 videos + 10 audio) with per-asset role binding. The model understands which asset is responsible for character, scene, prop, camera move, or rhythm — if you tell it.
- **Realistic humans are a headline feature**, not a liability: real skin pores, restrained micro-acting, multilingual lip-sync in 11 languages. The 2.0-era face caution does not apply.
- **Negative commands became reliable.** "Pure video, no subtitles, no background music" now actually suppresses random subtitles and unwanted score — the classic 1.x/2.0 failure is fixed.
- **Second-level timestamp control.** `[0-4s] ...` beat windows are honored as timing, not just ordering.
- **Editing an existing video** (partial re-render, background swap, language re-dub) and **extending** it are first-class modes, not workarounds.
- **Blockout control**: white-model 3D previz video (or green-screen plates) locks camera path, staging and blocking; Blender/Maya plugins upload straight to Jimeng.

Entry points: Jimeng (jimeng.jianying.com — Omni Reference / Smart Edit / Long Video / First & Last Frames), Doubao (Pro subscription), Xiaoyunque (xyq.jianying.com — character library, 3D director stage, segment reshoot).

## 2. Specs and hard limits

| Parameter | 2.0 | 2.5 |
|---|---|---|
| Single-pass duration | up to 15s | up to **30s** (duration `-1` or 4-30) |
| Images per request | 9 | **30** (each ≤4K, ≤30 MB) |
| Video references | 3 clips, ≤15s total | **10 clips**, single 2-30s, **≤30s total** |
| Audio references | 3 clips, ≤15s total | **10 clips, ≤30s total**; audio-only input now allowed |
| Output resolution | up to 4K | **480p / 720p** on Jimeng web |
| Timestamps | ordering hints only | honored to the second |

Generation parameters (duration, aspect ratio, resolution) are set on the generation page or via API — **they do not belong in the prompt**. The 1.x/2.0 CLI tail (`--resolution ... --duration ...`) is not 2.5 syntax. Exception: in Ultra Long mode, restate duration and ratio at the top of the prompt.

Auto-locked parameters: video editing locks ratio and duration to the input (±0.3s); first/last frame locks ratio to the first image (a mismatched last frame gets stretched); extension locks ratio, duration settable.

## 3. Official prompt formula

Base formula for any 2.5 prompt:

```text
<Subject> performs <primary action or event> in <scene and environment>.
The visuals feature <visual style>.
Use <shot size, camera angle, camera movement, or cuts>.
Audio includes <dialogue, ambience, sound effects, or music>.
```

Any component may be omitted. For long or reference-heavy work, the macro-formula:

```text
Complete prompt = [reference declaration] + [one-line summary] + [plot by timeline] + [global tail]
```

- **Reference declaration.** Each asset by upload order + its role (character / voice / motion / scene). See section 5.
- **One-line summary.** Subject + place + event + genre/style + special camera treatment.
- **Plot by timeline.** Per beat: ➕ positive content (picture + camera + action + dialogue + SFX) and ➖ local bans ("no subtitles", "no BGM").
- **Global tail.** Re-state the must-hold globals (camera position, environment, sound, lighting) and repeat the global bans.

Re-@ the same asset multiple times through the prompt — the official guide says repeated mentions increase accuracy.

## 4. Syntax markers for audio, dialogue and text

2.5 has dedicated markers. Use them — do not describe audio in loose prose:

| Content | Marker | Example |
|---|---|---|
| Music | `( )` | `(Soft, rhythmic piano music plays in the background)` |
| Sound effect | `< >` | `<A bell rings in the distance>` |
| Dialogue | `{ }` | `{Hello, welcome back.}` |
| Subtitles / titles | `【 】` | `【Chapter One: Departure】` |

Dialogue language reinforcement — the formula is `Dialogue language + regional variety or accent + delivery style + speaker + {line}`:

```text
Dialogue language: authentic Los Angeles English. The young man says in natural
Los Angeles vernacular: {No way, you actually made it.}
The girl says softly in Japanese: {もう大丈夫です}
```

Lip shape, speech rhythm and face match the assigned language in one pass — this holds across all 11 supported languages, including mixed-language scenes.

## 5. Reference discipline (the 50-slot system)

The point of 50 slots is not dumping assets in. **Every material's role must be written in the prompt.** Do not rely on text labels inside images; do not make the model infer mappings.

Role template:

```text
@Image 1 defines <subject>'s <appearance, clothing, structure, or material>.
@Video 1 defines <motion, camera movement, or pacing>.
@Audio 1 defines <character or sound type>'s <voice, dialogue, ambience, or music>.
```

Rules:

- **Bind each subject individually.** `<Character A> corresponds to @Image 1. Use only the appearance, hairstyle, and clothing.` The officially forbidden pattern: "@Images 1 through 4 define four characters respectively" — it never states which is which.
- **Add exclusions** for anything that could bleed in: "Do not use the image background." / "Do not use the people in the image." / "Do not use the person's identity, clothing, or scene from the video."
- **Do not restate what a reference already defines.** If a reference video defines the motion, state only which attributes to inherit — re-describing every action conflicts with the reference.
- **Subject Profile** for a recurring character:

```text
[Subject Profile: Conservator]
Appearance and clothing: @Image 1.
Fixed prop: <Sample Case> from @Image 5.
Locations: <Conservation Lab> and <Gallery>.
Motion references: the case-opening motion from @Video 1.
Do not use: other characters' clothing. Do not give this character <Record Board>.
```

- **Select references per scene**, not all at once: `Scene 1 | Use: <list>. Event: ... End state: ...`
- The same character in two states (before / after a transformation) = **two separate image slots**, each bound to its time range. Expect this to be the flakiest binding — budget re-rolls.

Official stability sweet spots:

| Input | Best | Possible but unstable |
|---|---|---|
| Subjects in a reference video/audio | 1-5 | 6-10 |
| Reference clip length | 5-10s per subject | longer |
| Subjects across reference images | 1-8 | 9-12 |
| Multi-view sheets | ≤5 subjects: any | >5 subjects: single view only; separate images per view beat a collage |
| Video-edit source length | ≤20s | longer stalls |

## 6. The 30-second structure: stages and end states

Divide the clip into consecutive stages. **One primary state change per stage, and always state the visible end state** — the end state is what the model steers toward (this is the U11 final-image rule, per stage).

```text
[Generation Goal] Generate a <video type>. The central subject is <subject>,
and the primary event is <story summary>.
[Stage 1] Initial state: ... Primary event: <one primary action>. End state: <visible state>.
[Stage 2] Continue from the previous stage: <what must remain unchanged>.
          Primary event: ... End state: ...
[Stage 3] Primary event: <closing event>. End state: <final visible state>.
[Maintain Consistency] Keep <identity, count, clothing, prop ownership,
spatial direction, audio relationships> consistent.
```

Timestamp rules:

- A time range is an event's **time budget, not an edit point**. Ranges must be consecutive and non-overlapping.
- **Windows of 3 seconds or more.** Shorter windows execute unreliably.
- **One core action + one camera move per window.** Do not demand frequencies ("three actions in one second").
- Second-precision only where it matters: critical handoffs, entrances, transitions, beat hits. `At 5 seconds, the camera whip-pans left and completes the transition.` Relative triggers work too: `Three seconds after the character presses the button, the room lights turn off.`
- Too little content in a window = model freedom; too much = over-cutting and omissions. Match content volume to the budget.

## 7. The anti-collapse skeleton (3 modules)

The official structure for dramatic 30-second work. It maps onto our 11-block skeleton but is leaner:

```text
<One-line tone summary — the logline>

[Module 1 — Reference layer]
Strictly keep @Image 1's face and features consistent. Keep @Image 2's
composition / blockout / spatial relations. Strictly lock character blocking.

[Module 2 — Global settings ("worldview + anti-collapse")]
Base environment & texture (emphasize extreme, realistic physical texture).
Visual style (film look, depth of field, lighting).
Camera language.
Character styling (use the section 8 formula).
Performance core (the acting register for the whole piece).
Prohibitions: <sound bans> + <subtitle bans> + <behavior bans> + <known collapse points>.

[Module 3 — Timestamped storyboard]
[start-end s] [beat name] — physical directives (shot size, composition,
micro-actions) + emotional subtext.
```

Two techniques carry this skeleton:

- **The prohibition list is specific, not generic.** From the official farewell example: "No exaggerated crying, no fast cuts, no large body movements, no extra dialogue, no BGM, no runny nose, no premature dropping of tears." Ban the exact ways this scene can collapse.
- **Directive + subtext.** After the physical directive, explain to the model *why* the action happens: "Emotion analysis: she is not complaining — she is waiting for him to confirm an answer she already guessed." The model acts better when it knows the intent. This is the official guide's signature trick and it composes directly with our Details Law.

## 8. Realistic human formula (anti-AI-face)

```text
Character = [age / ethnicity] + [skin tone / skin texture] + [3-4 facial details]
          + [gaze / soul] + [hairstyle / hair color] + [clothing / fabric]
          + [build / emotion / aura]
```

- **Force-append the fidelity suffix:** "retaining real fine pores and skin texture" (optionally freckles, blemishes). This single clause is the official anti-plastic-skin fix.
- Facial details need 3-4 concrete points: eye shape, brow bone, nose bridge, lips, jawline.
- Gaze/soul = the emotion the eyes carry, separate from the facial geometry.
- Works for animated characters too — swap the texture register.

For one emotional transition, **2-4 observable cues are enough** (eye movement, brow tension, mouth, breathing, throat swallow, hands). More reads as overacting; abstract emotion words leave too much room.

## 9. Camera language

Officially understood without translation: extreme wide / wide / medium / close-up / extreme close-up; push in, pull out, pan, lateral move, follow shot, orbit, dive, dolly out, tilt, handheld shake; low angle, overhead, first-person; one-take shot, dolly zoom, aerial, FPV, bullet time, bounce speed ramp.

For rarer terms, keep the term **and** translate it to observable change: `term + target subject + visual change + foreground/background relationship + direction or speed`. Full pattern and vocabulary in `camera-lighting-vocabulary.md` §10.

Aperture and focal-length numbers are allowed, but the visible result phrased in words is what actually steers the model.

## 10. Transitions

The transition vocabulary (natural cut, fade, dissolve, flash, wipe, occlusion mask, match cut, action/whip cut, motion-relay, zoom-through, ink-wash) lives in `camera-lighting-vocabulary.md` §11. Seedance-specific usage:

```text
cut = [transition type] + [basic constraints] + [cut logic]
```

- Always attach the incantation: **"prohibit rigid cutting, prohibit objects appearing out of thin air"** — it is the official anti-jump-cut clause, repeated in every transition template.
- Transitions can be **delegated**: "From [natural cut / occlusion mask / ink-wash / match cut], choose the one that best fits the style of this film."
- Order-gate effects that must not fire early: "The ink-wash effect must only appear AFTER 25 seconds, triggered by the 'click' sound — absolutely no premature appearance."

## 11. Physics through consequences and triggers

2.5 renders real physics and couples it with audio. Exploit this in four moves:

1. **Declare the physics regime up front.** "Rain reflections on metal, water splashed by tires, and the specular refraction of exhaust flames must strictly obey real-world physics."
2. **Narrate consequences, not just actions.** Tires kick up water curtains; the impact shatters the bridge into a spider-web pattern; the shockwave blows the rain away in a ring. Action chains where each step forces the next ("hand grips jar → lid actually unscrews") double as QA — a broken chain exposes a failed generation instantly.
3. **Negatively constrain the known failure.** "No soft-body or mollusk-like twisting of the mecha structure (must maintain metallic rigidity)." "The amber stays attached to the palm and must not clip through the fingers."
4. **Gate events on triggers.** "Three seconds after she presses the button..." / "only when he says {now}..." — triggers beat raw seconds for anything tied to performance.

## 12. Video editing (partial re-render)

2.5 edits an existing video: replace a subject, swap a background, remove a watermark, change the spoken language — while everything else stays put. The canonical pattern:

```text
[Edit Goal] Edit @Video 1. Within <entire video or time range>,
<add / remove / replace / adjust> <object, region, or audio category>.
[Source Video Role] @Video 1 is the sole editing master. It defines <characters,
scene, actions, composition, camera movement, occlusion, audio, and event order>.
[Target Material Role] @Image 1 defines <attributes of the replacement>.
[Edit Scope] Modify only <object, region, time range, or audio category>.
[Content to Preserve] Keep <everything that must not change> from @Video 1.
```

- **Subject replacement** adds a `[Timeline Inheritance]` block: "<Target> inherits every appearance, motion, occlusion, and exit of <original>, including timing, duration, path, and speed changes." Close with the catch-all: "Except for the object explicitly modified above, keep all other people, props, scene content, camera movements, cuts, and event order from @Video 1 unchanged."
- **The preservation-clause opener.** For filmed footage, enumerate everything to keep before stating any change — down to focal length, aspect and floor perspective: "Fully preserve from @Video 1 the person's identity, face, hair, skin tone, lip movement, original voice, speech rhythm, expression, gestures, camera position, focal length, aspect ratio, wall and floor perspective, and total duration." The longer the keep-list, the less drift.
- **Anchor timing to speech, not seconds**, when the source has narration: "When they say {now look at my hand}, a golden amber appears in the palm." The voice is the timeline.
- **Slice long sources first.** Editing works best on clips ≤20s; longer sources stall or fail.
- **Audio-only edits** work: "Remove only the original background music. Keep the dialogue, lip sync, ambience, and action sound effects; preserve the visuals and editing rhythm."
- **Localization pattern** — shoot once, re-dub per market: "Replace the Chinese narration in @Video 1 with natural fluent Spanish, and replace the presenter with a Spanish woman. Keep the original camera movement, blocking, performance pacing, scene, and product; preserve the overall audio-visual rhythm."
- Background swap scope: "modify only the background outside the subject's silhouette."

## 13. Video extension

Any clip ≤30s extends by 4-30s per pass, nested repeatedly, **hard ceiling 60s**. The new prompt applies only to the appended segment; original frames are untouched. Required verbs: extend forward / extend backward / continue.

Forward:

```text
Extend @Video 1 forward. The first frame of the extended segment directly
continues from the last frame of @Video 1. Maintain continuity in <pose,
prop position, background, camera position, lighting, motion direction>.
Then, <new content>.
Keep each subject as the same continuous instance throughout: do not duplicate
or split it, and keep the person's appearance stable.
```

Backward (prepend a beginning): describe the preceding events, then define @Video 1's **first frame as the extension's explicit end state**. Gotcha: materials that belong to the source video only must be flagged — "<X> must not appear early in the backward extension" — or later characters leak into the past.

- Boundary frames connect visually, not pixel-identically.
- Extensions hold character look, art style **and voice timbre** even without re-supplied references — plot-only extension prompts work.
- Community-proven minimal extension prompt: "Extend the video. Keep character identity, facial structure, body proportions, lighting, art style, and the space fully unchanged. Only change camera movement; do not redesign character or action."

## 14. Ultra Long mode (30-180s)

A separate mode (not the same as extension): one submission, 30-180 seconds. Restate duration and aspect ratio at the top of the prompt. Two working registers:

- **Timestamped** (1-minute ambient pieces): windowed beats with per-window bans — "0-20s (quiet opening): fixed camera... no shake, no characters enter, hard cuts prohibited."
- **Narrative flow** (3-minute pieces): loose event chain with inline references — the official 3-minute example is a cat-waiter vlog listing a full day of beats with 12 image refs assigned by role, closed with "No subtitles throughout, no background music."

Plan pacing in advance — without timestamps or a beat chain the back half drifts. Under the hood the pipeline generates segment-by-segment, carrying the **last ~3 seconds of each segment as the reference for the next** — which is why hand-offs are smooth and why a weak middle segment propagates forward. On Xiaoyunque the same mechanism powers chained extension to 90s plus **segment reshoot**: select a bad span on the timeline and regenerate only it, everything outside stays identical — the cheapest fix for pop-in objects and missed expressions.

## 15. Blockout and green screen

The controllability king: lock space, camera and staging in 3D first, let the model render materials and light. Two granularities:

- **Coarse blockout** — primitive geometry as a "dynamic skeleton" (trajectories, blocking, camera path, cuts, light changes). **Map every primitive to a reference**: "The tall cylinder in @Video 1 corresponds to <Guide>. The rectangular block corresponds to <Display Cart>." Exclude the render style: "Do not use its gray geometry or empty scene." Best practice: **no limbed or winged models in coarse blockouts** — unless you write the full limb motion sequence, they go stiff.
- **Fine blockout** — complete 3D animation; the model re-renders materials, color and style only: "@Video 1 is a fine blockout reference. Preserve structure, action, spatial layout, camera position, camera movement, and cuts. Do not use its original gray materials or empty background. Re-render <subject> as <final subject>..." **Clean the viewport capture first**: remove path lines, coordinate axes, controllers and camera frustums. Coarse currently works better than fine.

Pipeline notes:

- Blender/Maya plugins ("Clay Renderer" / 白模渲染上传器) render the blockout and upload straight to Jimeng as the reference video. Blender ≥3.6 works; no C4D/3ds Max. Color-coding blockout objects is unreliable — disambiguate primitives via prompt text, not material colors.
- No 3D package? Xiaoyunque's 3D director stage reconstructs a blockout from a concept image, offers action/camera/prop libraries, and lets you **drag-draw the camera path in the viewport**, then renders the previz clip for you.
- A **camera-path diagram works as an image reference** too: supply a top-down route sketch as @Image N and write "follow the camera route in @Image N".
- **Green screen, both directions**: upload green-screen footage + scene refs ("composite the person naturally into the classroom from @Image 2"), or convert an existing video's background *into* green screen for downstream comps ("Change all the white backgrounds into green screen backgrounds. Remove the sound, keep it muted.").

## 16. Storyboard grids and keyframes

- **Storyboard grid as input**: one image, ≤15 panels official (practitioners have pushed 50), clean line art, minimal text. Declare the reading order and exclude the style: "@Image 1 provides a 12-panel storyboard grid for shot order and approximate composition. Read it left to right, top to bottom. Do not use the grid's line-art style, text labels, or placeholder characters." Then `Shot 1: ... Shot N: ...`
- **Multi-keyframe sequences**: "Use @Image 1 through @Image N as keyframes in this order", one key state per image. Independent images align better than a grid. Keyframes control stage order and key states, not exact frames.
- **First + last frame** works inside omni-reference mode — declare each anchor separately ("@Image 1 is the first frame... @Image 2 is the last frame..."), never jointly. Same aspect ratio required.
- This is where the `image` skill chains in: character sheets and keyframes from `animatic-keyframes.md` become the reference kit.

## 17. Failure modes and fixes

### Twins / face-blending in multi-person scenes
Fix. Per-subject binding (section 5) + explicit differentiation: "Their movements are not synchronized. Clothing colors, hairstyles, and facial features must all be distinct. No identical clones in the background."

### Same character in two states appears at the wrong time
Pre/post-transformation slots confuse the model. Fix. Bind each state to its time range explicitly; budget re-rolls — this is the flakiest binding in 2.5.

### Random subtitles or unwanted BGM
Fix. "Pure video, no subtitles, no background music" — reliable in 2.5. Repeat in the global tail.

### Plastic AI skin
Fix. "Retaining real fine pores and skin texture" + production language instead of "hyperrealistic 8k".

### Long-context plausibility slips
Over 30s the model can place a plausible object in an impossible spot (a freighter on dry concrete). Fix. State the world's hard constraints in the global tail; verify the full timeline before shipping — errors hide in the back half.

### The one-take that refuses to stay one take
2.5 errs by commission: it completes more instructions than rivals but may cut freely even when told "one continuous take". Fix. "One continuous shot, no cuts of any kind" + a camera path that never motivates a cut; if montage keeps leaking in, drop to a 10-15s window where one-takes are stable.

### Edit mode stalls or ignores the instruction
Fix. Source ≤20s (slice first); name @Video 1 as "the sole editing master"; one edit target per pass.

## 18. Economics and model choice

- Costs are real: a 30s/720p generation on Jimeng runs ~500-700 credits. Production budgets must assume re-rolls, extensions and segment reshoots — fix with edit/extend/reshoot instead of full regeneration whenever possible. Draft at 480p, finish at 720p.
- Versus Minimax H3 (the other frontier model of this launch window): **H3 errs by omission, Seedance 2.5 errs by commission** — H3 delivers a more filmic whole but drops shots from the list; 2.5 executes nearly every instruction but may misuse a reference or break a global constraint. Pick 2.5 for timestamp precision, dense shot choreography, 50-reference kits and the editing/blockout toolchain; pick H3 (or Kling/Veo) when overall cinematic coherence per credit matters more than instruction compliance.

## 19. Worked examples (official, verbatim)

### A. Restrained micro-acting — "Riverside Farewell" (29s one-shot)

The flagship official example for emotional performance. Abridged; the structure is what to copy:

```text
29-Second One-Shot (Ancient Costume Woman's Riverside Farewell)

[Global Scene Setting] Early morning by the river, a blurred small boat in the
background, a lonely farewell. Quiet, restrained. Cinematic, shallow depth of
field, soft natural light. The camera holds a close-up of the woman, imitating
the subjective POV of "him" standing opposite her. Subtle handheld breathing,
one continuous shot with no fast cuts.

[Character Styling] [Age/Ethnicity] 22-year-old East Asian woman, classical
gentle cinematic face. [Skin] Cool-toned fair skin, delicate and moist,
retaining realistic fine pores and natural skin texture. [Facial Features]
Slender elegant eyes (slightly moist), relaxed brows, delicate straight nose
bridge, full lips with a faint gentle smile, soft jawline. [Eyes/Soul] Deeply
affectionate gaze, eyes shimmering like spring water. [Hair] Jet-black hair in
a casual classical low bun, a plain jade hairpin. [Clothing] Minimalist pure
white cross-collar Hanfu. [Physique/Aura] Slender, delicate narrow shoulders,
gentle classical romantic aura.

[Core Performance] Restrained and nuanced. Capture the shifting gaze, the rise
and fall of breathing, slight lip trembling, subtle brow movements, nostril
changes, throat swallowing, and the natural process of a tear sliding down.

[Negative Prompts] No exaggerated crying, no fast cuts, no large body
movements, no extra dialogue, no BGM, no runny nose, no premature dropping
of tears.

[Emotion and Action Storyboard]
Stage 1: 0-3s [Questioning]. She looks directly into the lens, lips slightly
parted, and whispers: {Are you really leaving?} Emotion analysis: she is not
complaining — she is waiting for him to confirm an answer she already guessed.
Stage 2: 3-10s [Resignation] — swallowing the bitterness. ...
Stage 3: 11-17s [Remembering] — a 0.5-second dead-silent pause; her lips twitch
then press together, jaw tightens, throat swallows.
Stage 4: 18-23s [Regret] — she lowers her eyes, and only then do the tears
begin to fall. She shakes her head slightly, almost imperceptibly.
Stage 5: 24-29s [Letting Go] — extreme close-up. She forms a gentle smile and
says in a barely audible but steadied voice: {You can go.} (On the word "go"
there is a faint tremble, forcefully suppressed.)
```

Every stage: one state change, physical directives, emotional subtext, and the bans list names the exact collapse modes of *this* scene.

### B. Physics and prohibitions — sci-fi mecha chase (30s one-shot)

```text
30-Second One-Shot (Sci-Fi Mecha Chase and Transformation)

[Global Setting] A cyberpunk cross-sea bridge in 2077, heavy rain. Emphasize
extreme, realistic physical textures: rain reflections on metal, water
splashed by tires, and the specular refraction of exhaust flames must strictly
obey real-world physics. Hardcore sci-fi cinematic feel, high-contrast neon
(cyber-pink and icy blue), high-speed shutter. High-speed drone POV, one
continuous shot. Subject: a silver-and-black concept mecha motorcycle.

[Negative Prompts] No soft-body or mollusk-like twisting/clipping of the mecha
structure during movement (must maintain metallic rigidity); no human
entities; strictly remove irrelevant subtitles; force mute / no default BGM;
avoid copyrighted IP elements like Transformers or Tron.

[Timestamp Storyboard]
[00:00-00:08] [Extreme Speed] The camera skims the waterlogged road; the
spinning wide tires kick up massive water curtains meters high. Camera
subtext: convey speed through the physical interaction of rain, puddle
reflections and engine flames.
[00:09-00:16] [Evasion] The tires grind the road, sparking orange friction
sparks, executing a tight "S" curve.
[00:17-00:24] [Mid-Air Reassembly] During slow-mo hang time the armor flips,
deconstructs, and reassembles — strictly rejecting "noodle-like" soft-body
transformation.
[00:25-00:30] [Heavy Landing] The tonnage impact shatters the bridge surface
into a spider-web pattern; the shockwave blows the surrounding rain away in
an expanding ring. A frozen "superhero landing" as the final image.
```

Physics regime declared up front, every beat narrates a consequence, and each ban targets a known failure of exactly this material.

### C. Reference orchestration — museum heist one-take (17 refs, translated from the Jimeng manual cases)

```text
Photoreal suspense-film texture. Set at the museum charity gala of @Image 10;
main hall structure, twin staircases and central exhibit stay consistent
throughout; sub-spaces reference @Image 11 and @Image 12; lighting and
materials reference @Image 15 and @Image 17. Follow the camera route in
@Image 16; smart auto-cutting, cinema-grade camera moves.

[0-4s] Camera advances behind the shoulder of the @Image 4 waiter carrying
the @Image 14 silver champagne tray through the main hall; the @Image 5
curator greets guests at the staircase; the @Image 6 reporter raises a
camera. The @Image 1 blue-diamond necklace sits in its glass case.
[4-8s] The @Image 7 woman in red brushes past the @Image 8 magician in black
tails, who smiles faintly at the lens; the @Image 9 security chief watches
beside the case.
[8-11s] The chandelier dies; the hall snaps to the crimson emergency lighting
of @Image 13; the crowd falls silent; <a soft clink from the case>, then
<a short alarm>. (Low strings and heartbeat stop together) — keep only an
inhale, the glass clink and the alarm.
[11-16s] Close-ups in sequence: the curator frozen, the reporter raising the
camera, the woman in red stepping back. Lights return to warm gold; cut back
to the case — glass intact, the @Image 1 diamond gone.
[16-20s] Slow push toward the magician's lowered right hand; a tiny blue
glint inside his silver cuff; he lifts his eyes to the lens and smiles.

No subtitles, no logo, no watermark.
```

Seventeen references, every one role-bound per scene; the camera choreography is supplied as a route diagram (@Image 16), not prose; sound is designed per beat with the `< >` and `( )` markers.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/seedance.md

# Seedance reference (ByteDance)

## Contents

1. What Seedance is
2. Versions and specs
3. CLI parameters (1.x / 2.0 only)
4. The Details Law (read first)
5. 6-step prompt formula (quick)
6. Production-grade skeleton (11 blocks) — for dramatic / multi-shot work
7. The 5-second shot timeline (rhythm template)
8. Multi-shot syntax (unique capability)
9. Anti-mush guard block (when Seedance smears the cuts)
10. `@img1` character reference syntax
11. Camera movements (9 presets)
12. Negative prompts handling
13. Image-to-video rule
14. Audio (1.5+)
15. Failure modes and fixes
16. Worked example. 15-second tragicomedy as 3 × 5s clips
17. Seedance 2.5 → read `seedance-25.md`

---

## 1. What Seedance is

A ByteDance video model with the UNIQUE ability to generate several distinct shots in ONE generation. The only major model that can pack a mini-montage inside a single 5-10s clip. Good cinematic motion, strong at ads and short narrative.

## 2. Versions and specs

- Seedance 1.0 Pro. 1080p, 5-10s (API up to 12s). Strong multi-shot.
- Seedance 1.0 Lite. 720p, faster, cheaper.
- Seedance 1.5 Pro. Native audio and lip-sync added.
- Seedance 2.0. Improved motion, better audio, 9 camera movement presets, limited negative prompt support, up to 12 reference inputs via `@` tags. Since June 2026: native 4K, 10-bit color. 2.0 Mini: ~2× faster, ~30% cheaper, for drafts and batches.
- **Seedance 2.5** (released 2026-07-31). Native 30-second single-pass clip, up to 60s via extension, 30-180s in Ultra Long mode. 50 multimodal reference inputs (30 images + 10 video + 10 audio), video editing (partial re-render), 3D white-model camera blockout, realistic humans with multilingual lip-sync in 11 languages. **Full production reference: `seedance-25.md`.**

Resolutions. 480p, 720p, 1080p; 2.0 adds native 4K; 2.5 outputs 480p/720p on Jimeng.
Aspect ratios. 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, 9:21.
Frame rate. 24-30 fps.

**Model pick within the family:** one continuous 15-30s arc, heavy reference kits, editing/extension of existing footage → 2.5 (realistic humans and lip-sync are a 2.5 headline feature — the 2.0-era face caution below does not apply to it). People-centric drama on a 2.0-only pipeline → 1.5 Pro (2.0 aggressively filters human faces and celebrity-adjacent content after the 2026 deepfake crackdown). Scenes, architecture, product, montage in short clips → 2.0. Cheap drafts → 2.0 Mini, then re-render keepers high.

## 3. CLI parameters (1.x / 2.0 only)

Append at the end of the prompt.

```text
--resolution 1080p --duration 5 --camerafixed false --seed 42
```

- `--resolution`. 480p | 720p | 1080p
- `--duration`. 2 to 12 (Pro)
- `--camerafixed`. true locks the camera. false allows movement.
- `--seed`. for reproducibility

**Not 2.5 syntax.** On 2.5, duration / aspect ratio / resolution are set on the generation page or via API and do not belong in the prompt (exception: Ultra Long mode restates duration and ratio at the top — see `seedance-25.md` §2).

## 4. The Details Law (read this first)

> **Details intensify emotion. Laziness kills the prompt.**

Seedance does not render abstractions. It renders **physical specifics**. Every adjective must be a sensory fact. Every emotion must be a body. Every shot must own at least three concrete details:

1. **One environmental pressure.** Cold blue refrigerator light. Steam off boiling water. Wet asphalt. Flickering fluorescent. Dripping tap. Curtain breathing in the AC.
2. **One physical micro-action.** Jaw locks. Finger taps the counter. Knuckles whiten on the fork. Lips press into a line. He swallows hard.
3. **One sound anchor or visual motif.** Stomach growl at 2.3s. Reflection in the dark phone screen. Rain hitting the same windowpane.

If a shot has none of these — it is filler. Delete it or rewrite it.

Banned, lazy phrasing that produces mush:
- "cinematic, professional, high quality, masterpiece"
- "beautiful lighting"
- "epic scene"
- "amazing visuals"
- "he is sad / he is angry" (with no physical translation)

This rule is hard. Multi-shot prompts on Seedance fail not because of the model, but because the writer was lazy on a single shot. One thin shot drags the whole sequence down.

## 5. Six-step prompt formula (quick scenes)

For single-shot 5s clips with one clear action.

```text
Subject. [Who or what]
Motion. [Present-tense verb, one clear action]
Camera. [Movement + framing + lens]
Environment. [Where, props, atmosphere]
Lighting. [Direction + quality + color]
Style. [Realism level, genre reference]
```

Write in full sentences, not tags. Seedance prefers clear grammatical prose. For dramatic / multi-shot / character-locked work, **use the production-grade skeleton in section 6 instead.**

## 6. Production-grade skeleton (11 blocks)

Use this for any dramatic piece, multi-shot ad, music-video segment, or character-locked clip. Each block answers a specific failure mode. Skipping a block reintroduces that failure.

```text
[1] Character lock.
    Use @img1 as the main character reference and preserve the exact same person
    across the whole clip: <face shape, eye color, hair, facial hair, build, distinctive
    features>. Dress him in <exact wardrobe>. No nudity. No glasses (unless reference).
    No extra characters.

[2] Length + genre + editing intent.
    Generate a <duration>-second multi-shot <genre> sequence with <fast / slow / staircase>
    dynamic editing.

[3] Story (one paragraph).
    <Concrete physical events of this clip in present tense. What changes from start to
    end. Name the break point.>

[4] Visual style.
    <Palette, contrast, grain, color temperature, what to avoid (e.g. "no warm yellow
    tones"). Texture cues — realistic skin, food detail, fabric, surfaces.>

[5] Camera style.
    <Camera body / look (e.g. Sony FX3 handheld). Lenses with purpose:
    35mm / 50mm for medium, 85mm for emotional close-ups, 100mm macro for inserts,
    24mm for wide silhouettes. Handheld micro-shake or static. Strict cuts between
    shots. No continuous take.>

[6] Editing style.
    <Hard cuts vs match cuts. Rhythmic escalation. Where the pause lands. Where the
    impact hits. The rhythmic staircase: long → shorter → shorter → pause → impact.>

[7] Audio.
    <Diegetic sounds in order: ambient, micro-actions, impact, silence moment, final
    cue. Examples: stomach growl, refrigerator hum, fork clink, wet thud, abrupt
    silence, distant city ambience. No dialogue / No subtitles / No on-screen text.>

[8] Shot-by-shot timeline.
    Shot 1, 0.0–X.X sec: <framing, lens, camera move, action, environment detail,
                           emotion translated into body>.
    Shot 2, X.X–Y.Y sec: <...>.
    ...
    (See section 7 for the 5-second rhythm template.)

[9] Lighting (recap and specifics).
    <Main source, fill, rim. Direction. Color temperature. What it carries
    psychologically — judgment, isolation, hope, grief.>

[10] Composition.
    <Where the subject sits in frame across shots. Negative space. Reflections.
    Silhouettes. Foreground obstruction. The final image must be named.>

[11] Output specs.
    <Exact duration. Aspect ratio. Realism level. CLI: --resolution 1080p
    --duration 5 --camerafixed false>
```

Why 11 blocks and not 6? Each block prevents one specific Seedance failure: identity drift, one-take collapse, mood smear, lens chaos, audio mismatch, drift on rhythm. Cheap insurance.

## 7. The 5-second shot timeline (rhythm template)

For a 5-second multi-shot clip, the model performs best with **5 shot beats** following a dramatic micro-arc. Use this timing as the default scaffold:

```text
0.0–0.8 sec  | Establish     | extreme close-up or insert that anchors emotion / situation
0.8–1.6 sec  | Action        | medium shot, hero moves or reacts
1.6–2.5 sec  | Turn          | new framing reveals the shift (POV, OTS, rack focus)
2.5–3.6 sec  | Reaction      | tight close-up, slow push-in, emotion lands on the body
3.6–5.0 sec  | Climax / hero | hero shot, low angle, slow-mo if earned, final image
```

For 10s clips, double the structure or insert one pause before the climax (the pause beats speed). For 15s+ stories, split into 3 × 5s clips and stitch in the editor — Seedance is more reliable in shorter generations than one long take.

## 8. Multi-shot syntax (unique)

Seedance reads explicit cut markers inside a single prompt and generates distinct shots connected by visible cuts. This is its strongest card. Use it when you need montage in a single generation.

Supported cut markers.

```text
Shot 1. [description]
Cut to. [description]
Camera cut to. [description]
Camera switching. [description]
Lens switch to. [description]
```

Inline timeline syntax.

```text
[Shot A description] -> Cut to -> [Shot B description] -> Camera cut to -> [Shot C description]
```

Example.

```text
Shot 1. Medium close-up on a tired man in a kitchen. He opens the refrigerator.
Cut to. Macro insert. His hand reaches toward a single sausage on an empty shelf.
Cut to. Over-the-shoulder shot. The fridge light paints his face cold blue.
```

Use 2-3 shots per 5-second clip for tight cinematic montage, 4-5 shot beats only when each beat is short and physically distinct (see section 7). Hard cap: 5 shots per generation — beyond that the model drops or compresses shots. Size the duration to the shot count (4 shots need 10-15s, not 5s). Every shot must share an anchor with its neighbors — same character, same location, or same lighting recipe — or the model produces disconnected clips instead of a sequence.

## 9. Anti-mush guard block

Seedance sometimes ignores cuts and produces one continuous take, smears multiple shots into a single moving frame, or drifts character identity across the timeline. Drop this block at the **very top of the prompt** (before block [1]) when it happens or to prevent it pre-emptively on heavy multi-shot work:

```text
Important direction:
This must be a clearly edited multi-shot sequence with visible cuts between shots.
Do not generate a single continuous take. Each shot must have a different camera angle
and different framing. Use rapid montage pacing with rhythmic escalation. Keep the same
character appearance throughout. Preserve the same clothing, face, body type, facial
hair, and hairstyle in every shot. The tone is <serious cinematic drama / tragicomedy /
documentary realism / etc.>.
```

This is the highest-leverage paragraph in any Seedance prompt. Add it any time the model produced mush on a previous attempt.

## 10. `@img1` character reference syntax

Seedance 2.0 accepts image references inline using `@img1`, `@img2`, etc. Use this to lock the protagonist's likeness across all shots in a multi-shot clip and across multiple stitched clips.

```text
Use @img1 as the main character reference and preserve the exact same man across the
whole clip: <full identity block: face, eyes, hair, facial hair, build, distinctive
features, wardrobe>. No nudity. No glasses (unless in reference). No extra characters.
```

Rules.

- The full identity block must follow the `@img1` mention. The model needs the textual description as a backup signal — the image alone drifts.
- Repeat the identity block in **every** clip of a stitched sequence. Treat each generation as briefing a new intern.
- For multiple references (character + setting, character + outfit), label each: `@img1` is the protagonist, `@img2` is the location reference, `@img3` is the outfit reference. Then state the role inline.
- 2.0 also takes `@Video1` (motion/style reference, 480-720p) and `@Audio1` (voiceover / music) tags — state each reference's role in prose, e.g. "@Audio1 plays as the voiceover". Limits: 12 files total on 2.0 (up to 9 images, 3 videos, 3 audio); up to 50 on 2.5.

## 11. Camera movements (9 presets)

- Dolly Out. Reveals context, pulling away.
- Dolly In. Pushes into subject, builds tension.
- Pan Left / Pan Right. Horizontal reveal, landscape, row.
- Tilt Up / Tilt Down. Vertical reveal.
- Tracking. Follows a moving subject.
- Crane / Aerial. Epic scale, establishing.
- Handheld. Documentary, intimate, UGC.
- Zoom In / Zoom Out. Tension or detail.
- Hitchcock Zoom. "dolly out while zooming in" for vertigo effect.
- Static (via `--camerafixed true`). Locked frame.

Combine sparingly. Multiple camera moves in 5s rarely resolve cleanly.

## 12. Negative prompts

Seedance 1.0 Pro does NOT support negative prompts. No `--no blur` syntax works.

Seedance 2.0 adds limited negative prompt support but it's fragile and often ignored.

Workaround for 1.x/2.0. Always invert to positive phrasing. Instead of "no yellow tones" write "cold blue-gray palette with desaturated skin tones." Instead of "no distorted hands" write "anatomically correct hands with clear finger separation."

**Seedance 2.5 fixed this.** Direct bans are reliable: "pure video, no subtitles, no background music" actually suppresses them, and specific prohibition lists ("no exaggerated crying, no fast cuts") are a core part of the official 2.5 prompt structure. See `seedance-25.md` §7.

## 13. Image-to-video rule

When using a reference image, DO NOT describe elements already visible in the image. The model sees it. Describe only motion and camera work. Re-describing static elements creates identity drift.

Bad. "A man in red shirt stands in kitchen. He walks to the fridge."
Good. "He slowly walks toward the fridge, opens it with hesitation, freezes when he sees the empty shelves. Tracking shot from behind, 35mm."

## 14. Audio (1.5+)

Seedance 1.5 Pro, 2.0 and 2.5 generate native audio and support lip-sync. Include audio cues in the body of the prompt — treat the prompt as a sound brief.

```text
Audio. fridge hum, distant rain on window, one stomach growl at 2.3 sec, final silence.
```

Rules:

- Dialogue goes in **double quotes** on 1.5/2.0 — the model voices it, generates the voice and syncs lips to the cut. State the delivery: "Play her line dry and a little proud, his quiet and worn out." **On 2.5, use the dedicated markers instead**: dialogue in `{ }`, SFX in `< >`, music in `( )`, titles in `【 】` (see `seedance-25.md` §4).
- Keep lines short. Long monologues drift out of sync — split into several lines and hold sync with cuts. Still less robust than Veo for speech-first work.
- Write **"no music"** explicitly when you want none — otherwise the model lays an ad-style score under everything.
- Subtitles: describe the voiceover, then ask for "text along the bottom edge, timed to the voice".

## 15. Failure modes and fixes

### One continuous take when multi-shot was requested

Fix. Add explicit "Cut to" markers. Say "multi-shot sequence with visible hard cuts. Do not generate a single continuous take."

### Character drift across shots

Fix. Repeat the full identity block at each shot boundary inside the prompt.

### Motion ignored below 5 seconds

Fix. Minimum duration 5s for any scene that has multiple actions or camera moves.

### Negative phrasing ignored

Fix. Use positive substitutes. Seedance 1.0 has no negative parser.

### Multi-shot fails on 4+ shots in 5s

Fix. Cap at 2-3 shots per 5-second clip for tight cinematic, or 4-5 short beats following the section 7 timeline. If more shots are needed, split into multiple generations.

### Mood smear / "everything looks the same"

Fix. Each shot needs a distinct emotional function (Establish / Power / Pressure / Detail / Reaction / Shift / Impact / Aftermath — see dramaturgy.md §10, Layer 2). If two adjacent shots have the same function, the model averages them into the same frame. Vary function and framing in every cut.

### Lazy abstract phrasing produces lifeless clips

Fix. Apply the Details Law (section 4). Audit your draft: every shot must have one environmental pressure, one micro-action, one sound or visual motif anchor. Replace adjectives like "dramatic", "intense", "beautiful" with concrete physical facts.

### Human faces rejected or degraded (2.0)

After the 2026 deepfake crackdown, 2.0 aggressively filters human faces, helmets, sunglasses, and anything resembling protected IP or celebrity likeness. Fix. Route face-heavy drama to Seedance 2.5 (realistic humans are its headline feature), 1.5 Pro, Kling, or Veo; keep 2.0 for scenes, architecture, product and montage work. Use only owned or synthetic character references — the IP/celebrity filter applies on 2.5 too.

## 16. Worked example. 15-second tragicomedy as 3 × 5s clips

A 15s narrative is **never** one prompt. It is three self-contained 5-second prompts, each with the full character lock, the full visual style, the full audio block, and a different dramatic function. Stitch in the editor.

### Story spine
- Beat 1 (Clip A, 0-5s). Hunger. Hero opens an almost empty fridge. Discovers one lonely sausage. Despair flips to hope.
- Beat 2 (Clip B, 5-10s). Cooking. Pot, water, fire, sausage, bubbling, anticipation, hero shot lifting the sausage with a fork.
- Beat 3 (Clip C, 10-15s). Catastrophe. Sausage slips, falls, wet thud. Window. Bedroom. Hungry sleep. Cut to black.

### Clip A. Hunger (production-grade skeleton applied)

```text
Important direction:
This must be a clearly edited multi-shot sequence with visible cuts between shots.
Do not generate a single continuous take. Each shot must have a different camera angle
and different framing. Use rapid montage pacing.

Use @img1 as the main character reference and preserve the exact same man across the
whole clip: bald head, gray-green eyes, round expressive face, moustache, long black
braided goatee, short dark side hair tufts, slightly overweight build, tragicomic face.
Dress him in a dark oversized T-shirt and dark sweatpants. No nudity. No glasses.
No extra characters.

Generate a 5-second multi-shot tragicomic cinematic sequence with fast dynamic editing.

Story:
The man is hungry at night. He suddenly goes to the refrigerator, opens it, feels
disappointment because it is almost empty, then notices one lonely sausage and becomes
instantly hopeful.

Visual style:
Cold night kitchen. Blue-green refrigerator light. Desaturated colors. No warm yellow
tones. Slightly harsh LED reflections. Realistic cinematic look. High contrast but
natural skin texture. Subtle film grain. Realistic food detail.

Camera style:
Sony FX3 handheld look. 35mm and 50mm lenses for medium and close shots. 100mm macro
for inserts. Handheld micro-shake. Visible cuts between shots.

Editing style:
Fast montage with hard cuts. Each shot a different angle and framing. Tense rhythm,
escalating to the moment of discovery.

Audio:
Deep stomach growl, soft room tone, refrigerator hum, quiet footsteps, fridge door
sound. No dialogue. No subtitles. No on-screen text.

Shot 1, 0.0–0.8 sec. Extreme close-up of the man's eyes in darkness. He is awake,
hungry, tense. Static close shot, faint blue ambient light.
Shot 2, 0.8–1.6 sec. Medium handheld side shot. He sits up and walks fast to the
kitchen. Slight shake, push-in.
Shot 3, 1.6–2.6 sec. POV from inside the refrigerator. The door opens toward camera.
Cold blue-green light hits his face. Shelves almost empty. His face drops.
Shot 4, 2.6–3.5 sec. Rapid inserts: empty shelf, empty container, lonely sauce stain,
his sad eyes, his hand moving items aside.
Shot 5, 3.5–5.0 sec. Macro insert of one single sausage in the corner. Rack focus
from empty shelf to sausage. Smash cut to a slightly low-angle close-up of his face.
His eyes widen, despair flips to joy, tiny victorious smile.

Lighting:
Dark apartment, very low ambient fill. Main source is cold refrigerator light,
blue-green, top-front. Strong contrast. No warm kitchen light.

Composition:
Tight close-ups and inserts. Negative space inside the empty fridge. Final face shot
heroic and absurd.

--resolution 1080p --duration 5 --camerafixed false
```

Clips B and C follow the same structure with their own story paragraph, shot list, and final image. The character lock and visual style blocks are repeated **verbatim** in each clip — Seedance has no memory between generations.

### Older single-clip skeleton (kept for quick scenes)

For a single non-dramatic shot or a quick test, the original 6-step skeleton still works:

```text
Subject. [identity block with face, hair, clothing, distinguishing features].
Motion. [one clear present-tense action for the scene].
Camera. Shot 1. [framing, lens, movement]. Cut to. Shot 2. [framing, lens, movement]. Cut to. Shot 3. [framing, lens, movement].
Environment. [location, time of day, props, weather].
Lighting. [dominant source, direction, quality, color].
Style. [realism level, genre reference, palette].
Audio. [ambient, SFX, silence moments]. (1.5+ only)
Continuity. [what must remain constant across shots].

--resolution 1080p --duration 5 --camerafixed false
```

For dramatic, multi-shot, character-locked, or stitched-clip work — always use the 11-block production-grade skeleton from section 6.

## 17. Seedance 2.5 → read `seedance-25.md`

2.5 changes the workflow: a 15-30s narrative that used to be 3-6 stitched clips is now one generation with one continuous arc, extendable to 60s, with a separate Ultra Long mode to 180s. The dramaturgy does not change — the beat map from `dramaturgy.md` §10 moves inside a single prompt.

Everything 2.5-specific lives in **`seedance-25.md`**: the official prompt formulas, the `( ) < > { } 【 】` markers, the 50-slot reference discipline, stages + end states, video editing, extension, Ultra Long, blockout/green-screen pipeline, and the official worked examples. For any 2.5 production task, read that file before writing the prompt.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/universal-rules.md

# Universal rules — apply to every video model

These rules apply to Seedance, Kling, Veo, and any other AI video generator. They exist because all current video models share a common failure mode. They reward concrete physical direction. They punish abstraction, contradictions, and keyword spam. Ignoring these produces muddy generations regardless of which model you target.

Read this file after `dramaturgy.md` and before any model-specific file. The model-specific syntax sits on top of these rules — it does not replace them.

## Contents

1. The non-negotiable. Details intensify emotion (Details Law)
2. U1. Universal prompt skeleton
3. U2. Weight-at-start
4. U3. Show don't tell
5. U4. Natural language beats tag spam
6. U5. One primary camera move per shot
7. U6. Precise lens language
8. U7. Character consistency anchor
9. U8. No contradictions
10. U9. Concrete physical detail over abstract concept
11. U10. Duration discipline
12. U11. The final image rule
13. U12. The three-detail check (audit before sending)
14. U13. Reference role discipline
15. U14. Priority declaration

---

## 1. The non-negotiable. Details intensify emotion. Laziness kills the prompt.

This is the most violated rule in AI video, and the one reason most multi-shot prompts fail. The dramaturgy is fine — the writer just got lazy on a single shot, and that one thin shot drags the whole sequence into mush.

Every shot in every prompt owns at least three concrete physical details:

1. **One environmental pressure.** Cold blue refrigerator light. Steam off boiling water. Wet asphalt. Flickering fluorescent. Dripping tap. Curtain breathing in the AC. (Kurosawa: weather is a character. See `dramaturgy.md` §9.)
2. **One physical micro-action.** Jaw locks. Knuckles whiten on the fork. Lips press into a line. He swallows hard. Fingers curl against the doorframe. (Show, not tell — the body is the only place where feelings render.)
3. **One sound anchor or visual motif.** Stomach growl at 2.3s. Reflection in a darkened phone screen. Rain on the same windowpane. A single fluorescent flicker before each cut.

If a shot has none of these — it is filler. Delete it or rewrite it. No exceptions for "establishing", "transition", or "hero product" shots — those are exactly the shots that go lazy first.

Words that do not render and mark the writer being lazy:

- "cinematic", "professional", "high quality", "masterpiece", "stunning", "epic", "amazing"
- "beautiful lighting", "dynamic camera", "intense moment", "powerful scene"
- "he is sad", "she is angry", "he is afraid" — emotions named without a body

Replace each with concrete physical facts. The full theory of why this works lives in `dramaturgy.md` §2 (Second law).

## 2. U1. Universal prompt skeleton

Build every prompt from these layers, roughly in this order:

```text
[Subject / Character]
[Action / Motion]
[Scene / Environment]
[Camera / Shot / Lens]
[Lighting / Atmosphere]
[Style / Mood / Palette]
[Sound / Audio]
[Duration / Aspect ratio / Resolution]
[Continuity rules]
[Negative constraints — only if the model supports them]
```

Model-specific skeletons live in their reference files (`seedance.md`, `kling.md`, `veo.md`). For dramatic / multi-shot / character-locked Seedance work, the production-grade 11-block skeleton in `seedance.md` §6 supersedes this generic skeleton.

## 3. U2. Weight-at-start

Generators put more attention on the first 30-40% of tokens. Lead with subject and action. Style modifiers go at the end. Camera, lighting, and environment live in the middle.

## 4. U3. Show don't tell

The model cannot render feelings. It renders bodies. Translate every emotion into a physical action.

- Bad. "He is scared."
- Good. "His jaw locks. He stops breathing for one beat. His fingers curl against the doorframe."

Calibration: for one emotional transition, **2-4 observable cues** (eye movement, brow tension, mouth, breathing, throat swallow, hands) are enough. Fewer leaves the model guessing; more reads as overacting.

## 5. U4. Natural language beats tag spam

Video models are not image models. Tag stuffing like "masterpiece, 4k, cinematic, beautiful" fails. Write in full cinematic sentences as if briefing a human DOP.

## 6. U5. One primary camera move per shot

Do not stack three camera moves in a 5-second clip. Pick one dominant move (dolly-in, pan, tracking, static). Layer a subtle micro-adjustment if needed (slight handheld shake, gentle rack focus). More than that produces visual chaos.

## 7. U6. Precise lens language

State the lens. "Shot on 50mm" works across all major models. Quick map:

- 24mm. wide, immersive, exaggerated space
- 35mm. natural documentary
- 50mm. intimate, human perspective
- 85mm. portrait, compressed background
- 100mm macro. texture, detail
- anamorphic 40mm. cinematic widescreen

Full vocabulary in `camera-lighting-vocabulary.md`.

## 8. U7. Character consistency anchor

Anchor identity at the START of every prompt. In a multi-clip sequence, repeat the full identity block in every single prompt. Video generators have no memory between generations. Treat every clip like briefing a brilliant intern with memory damage.

Identity block must include: face shape, eye color, skin tone. Hair color, length, style. Facial hair. Exact clothing items. Distinctive accessories.

Model-specific syntax for character locking:
- Seedance: `@img1` reference + identity block (see `seedance.md` §10)
- Kling 1.x – 2.x: Element Binding with 3-4 reference images (see `kling.md` §7)
- Kling 3.0: in-prompt `[Character A: <full identity>]` labels, optionally combined with Element Library (see `kling.md` §3)
- Veo: reference ingredients / JSON identity (see `veo.md`)

## 9. U8. No contradictions

The model obeys the strongest signal. Contradictions produce artifacts.

- Bad. "Still pond" + "flowing water."
- Bad. "Close-up" + "wide cinematic landscape."
- Bad. "Quiet moment" + "explosive action."

## 10. U9. Concrete physical detail over abstract concept

"Loneliness" does not render. "A man sitting alone, shoulders collapsed, face lit by blue phone glow, empty bottles on the table" does.

This is the same rule as the Details Law in section 1, viewed from a different angle. Section 1 is the audit. This is the principle.

Corollary — **consequence prompting**. Current models render real physics, so describe the consequence of an action, not just the action: tires kick up water curtains; the hand grips the jar and the lid actually unscrews; the impact shatters the surface into a spider-web pattern. Action chains where each step forces the next also work as QA — a broken chain exposes a failed generation at a glance.

## 11. U10. Duration discipline

Most models work in 5-10 second clips. Longer narratives live in multiple clips stitched in the editor. Do not cram a 30-second story into a 5-second prompt.

Default splits:

- 10s = 2 clips × 5s
- 15s = 3 × 5s
- 30s = 6 × 5s
- 60s = 12 × 5s

Three exceptions:
- Seedance — 2-3 shots inside one 5-10s clip via "Cut to" syntax (see `seedance.md` §8).
- Kling 3.0 — up to 6 shots inside one generation, up to 15s, with native audio and dialogue (see `kling.md` §3).
- Seedance 2.5 — up to 30s in one pass. The working structure is consecutive stages, each with one primary state change and an explicit visible end state (see `seedance-25.md` §6).

## 12. U11. The final image rule

Every clip needs a clear final frame. The model uses the ending as emotional destination.

- "Ends on his face frozen in the blue refrigerator light" beats "he stands there sadly."

The final image is also one of the five anchors (see `dramaturgy.md` §13). Naming it is non-negotiable.

## 13. U12. The three-detail check (audit before sending)

Before returning the final prompt to the user, audit every shot. Each shot must carry at least one of each:

1. Environmental pressure (lighting, weather, surface, sound of the room).
2. Physical micro-action on the body (jaw, hand, breath, eye, gesture).
3. Sound anchor or recurring visual motif tied to the emotional spine.

If a shot has zero, fix it before sending. If a shot has only one, ask whether you can make it two without bloat. The strongest prompts in this skill's worked examples always have all three.

Empty descriptors that fail this check: "establishing wide shot", "beautiful lighting", "dynamic camera move", "cinematic look", "intense moment", "dramatic close-up". Replace each with three concrete physical facts.

## 14. U13. Reference role discipline

Wherever a model accepts reference assets (Seedance `@Image/@Video/@Audio`, Kling Element Binding and Omni references, Veo ingredients), **every asset gets an explicit role written in the prompt**: what it defines (appearance, motion, voice, scene, camera path) and what to ignore ("Do not use the image background", "Do not use the people in the image").

- Bind each subject individually: "<Character A> corresponds to @Image 1 — use only the appearance, hairstyle, and clothing." Never the collective form "@Images 1 through 4 define four characters respectively" — it does not state which is which.
- Do not restate what a reference already defines. If a video reference carries the motion, name only the attributes to inherit; re-describing every action fights the reference.
- More assets is not more control. Control comes from role clarity; unassigned assets bleed into the frame.

Model-specific limits and templates live in the model files (`seedance-25.md` §5 has the fullest system).

## 15. U14. Priority declaration

When a prompt is overloaded (10+ scenes, many subjects, spatial tricks), adding more description makes it worse. Instead, declare priorities — the model cannot know what matters most unless told what to protect and what to sacrifice:

1. The core subject that must survive every shot.
2. The key shots that must appear.
3. The transitions where the model may freestyle.
4. The mandatory final frame.

This ranks above prompt-length discipline: a shorter prompt with declared priorities beats a longer one without them.

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*


---

## ARCHIVO: video/references/veo.md

# Veo reference (Google)

## Contents

1. What Veo is
2. Versions and specs
3. Prompt structure and length
4. Dialogue syntax (critical, unique)
5. SFX syntax
6. JSON prompts (powerful, unique)
7. Image-to-video (Veo 3.1)
8. Reference ingredients (3.1)
9. Failure modes and fixes
10. Skeleton and example

---

## 1. What Veo is

Google's cinematic video model with NATIVE synchronized audio. The only major generator that creates dialogue, SFX, and music in sync with the video and does lip-sync natively. Best for commercial polish, narrative with dialogue, and cinematic audio.

## 2. Versions and specs

- Veo 3. Text-to-video, native audio, 4 / 6 / 8 second clips.
- Veo 3.1. Adds image-to-video with First Frame, improved audio, reference ingredients, stronger motion coherence.

Duration. 4, 6, or 8 seconds.
Dialogue budget. Max 8 seconds of spoken audio per clip.

## 3. Prompt structure and length

Order matters. Lead with subject and camera. Quality modifiers go at the end.

```text
[Subject / Action]
+ [Environment / Setting]
+ [Camera / Shot Type / Lens]
+ [Lighting / Atmosphere]
+ [Style / Quality]
+ [Audio]
+ [Duration]
```

Sweet spot. 50-200 words.

- Shorter prompts = more creative latitude, less control.
- Longer prompts = tighter control, higher risk of contradictions.

## 4. Dialogue syntax (critical)

Veo is the only model that renders synced lip movement and voice. The syntax matters.

### Required format

Double quotes + lead-in verb (says, whispers, shouts, mutters, asks).

```text
A woman says, "Welcome to the future."
He whispers, "Don't move."
She shouts, "Get out!"
```

Colon after the lead-in verb works too and is often more reliable.

```text
A woman says: "Welcome to the future."
```

### Voice character modifiers

Place modifiers before the lead-in verb.

```text
He says in a weary voice, "We are fine. We are fine."
She whispers nervously, "I don't want to be here."
He shouts excitedly, "We did it!"
```

### Timing rule

Maximum 8 seconds of spoken audio. Cram too many words into a 5s clip and the delivery speeds up unnaturally. Cut the line until it fits.

## 5. SFX syntax

Three supported formats. Mix as needed.

```text
SFX: thunder cracks in the distance
Audio: rain on tin roof, distant traffic, one slow breath
(a loud thunderclap)
(key turning in a lock)
(wet footsteps on concrete)
```

Use labels `Audio:`, `Says:`, `SFX:` to separate sound direction from visual direction. The model needs an explicit signal that audio should be generated.

## 6. JSON prompts (powerful, unique)

Veo parses structured JSON. This prevents "concept bleed" where describing mood accidentally changes object colors. Use JSON for complex scenes with strict continuity needs.

### Full schema

```json
{
  "version": "veo-3.1",
  "output": {
    "duration_sec": 8,
    "fps": 24,
    "resolution": "1080p",
    "aspect_ratio": "16:9"
  },
  "global_style": {
    "look": "cinematic naturalism",
    "color": "cold blue-gray palette, desaturated skin",
    "mood": "quiet domestic tragedy",
    "reference": "Fincher-style motivated camera"
  },
  "continuity": {
    "characters": [
      {
        "id": "man",
        "description": "40s, tired eyes, stubble, dark blue t-shirt, grey sweatpants, barefoot"
      }
    ],
    "props": ["empty refrigerator", "single sausage", "chipped white plate"],
    "lighting_constant": "cold fridge light as key"
  },
  "scenes": [
    {
      "id": "01",
      "start": "0.0",
      "end": "3.0",
      "shot": {
        "type": "medium close-up",
        "framing": "eye-level, slightly offset",
        "camera": "slow push-in, 50mm"
      },
      "action": "He opens the fridge. His face catches the cold light. His eyes stop on the empty shelf.",
      "environment": "small kitchen, 3am, rain outside window",
      "lighting": "cold fridge light as key, warm window spill as rim",
      "audio": "fridge hum, distant rain, one stomach growl"
    },
    {
      "id": "02",
      "start": "3.0",
      "end": "8.0",
      "shot": {
        "type": "extreme close-up",
        "framing": "macro insert on hand",
        "camera": "static, 100mm macro"
      },
      "action": "His hand hovers over a single sausage. He picks it up slowly, exhales.",
      "environment": "inside the fridge",
      "lighting": "cold fridge light, high contrast",
      "audio": "quiet breath, soft plastic crinkle"
    }
  ]
}
```

### When to use JSON

- Multiple scenes in one generation.
- Strict character continuity across shots.
- Complex props that must stay the same color and size.
- When a prose prompt kept changing subject colors when you added mood words.

Not every Veo prompt needs JSON. For simple clips, prose is faster and often better.

## 7. Image-to-video (Veo 3.1)

Uses the static image as First Frame. Prompt guides motion and sound.

Rules.

- Do not re-describe static elements.
- Describe only motion, camera, light change, and audio.
- Add "maintain the subject from the first frame" to protect identity.

Example.

```text
Maintain the subject from the first frame. Slow push-in, 50mm. She exhales, her eyes shift to the left, one strand of hair falls across her forehead. Warm rim light grows stronger.

Audio: soft breath, distant traffic, one door closing in the next room.
Duration: 6 seconds.
```

## 8. Reference ingredients (3.1)

Upload multiple reference images (character, location, prop) and tag them in the prompt.

```text
The character from reference_1 walks into the location from reference_2 holding the object from reference_3.
```

Use when you need a specific character in a specific place with a specific object.

## 9. Failure modes and fixes

### Dialogue speeds up unnaturally

Fix. Cut the line to fit 8 seconds of natural speech. Test by reading aloud.

### Audio missing from output

Fix. Add explicit `Audio:`, `SFX:`, or `Says:` labels. Do not assume the model will infer audio from visual description.

### Camera direction ignored

Fix. Lead the prompt with camera. "Wide aerial shot" at the start beats "cinematic camera work" in the middle.

### Character color changes when mood words are added

Fix. Switch to JSON prompt. Lock the character description in the continuity block. Keep mood in global_style where it cannot bleed into object colors.

### Lip-sync off

Fix. Check the lead-in verb. "She says, ..." outperforms just quoted speech alone. Colon form often more reliable than comma.

### Prompt too long, model cherry-picks

Fix. Compress to the 50-100 word range. Or switch to JSON which handles length better because of structural separation.

## 10. Skeleton

### Prose version

```text
[Subject performing action] in [environment]. [Camera framing + lens + movement]. [Lighting direction + color temperature]. [Style + mood + palette].

Audio: [ambient sounds, SFX, music texture].
Says: [character] says, "[dialogue, max 8 seconds of speech]."
SFX: [punctual sound events].

Duration: [4 / 6 / 8] seconds.
```

### JSON version

See section 6. Copy the schema and fill in.

### Worked example. Commercial hero shot

```text
A woman in a cream silk blouse stands in front of a morning window, lifting a ceramic coffee cup to her lips. Medium close-up, 85mm, slow push-in. Warm window key from frame-left, soft bounce fill from frame-right. Cinematic naturalism, creamy palette, shallow depth of field.

Audio: distant city ambience, ceramic clink, one slow breath.
Says: She whispers to herself, "One more minute."
SFX: (spoon tapping ceramic at 2 seconds).

Duration: 6 seconds.
```

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*

