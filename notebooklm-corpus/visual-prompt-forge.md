# SKILL: visual-prompt-forge

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: visual-prompt-forge/SKILL.md

---
name: visual-prompt-forge
description: Generate model-specific prompts from shots.json. Outputs copy-paste-ready prompts for stills (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream) and motion video (Kling, Veo, Seedance, Hailuo). Also runs a revision mode that reads a critique.json and re-emits prompts for only the failed shots, closing the QA loop. Use when the user asks for image or video prompts, mentions any of those generators, wants AI-generated frames for a storyboard, or hands over shots.json. The prompt half of the pipeline. Composes with storyboard-architect upstream, visual-asset-critic downstream.
---

# Visual Prompt Forge

You are turning structured shot data into prompts that work in production. Each image generator rewards a different prompting style, short and high-signal for Midjourney, natural-language for Flux, paragraph-form for GPT Image, text-aware for Ideogram. A prompt that crushes in one will produce slop in another.

This skill adapts. Same shot, different syntax.

## When to use

Trigger when the user:

- Hands over a `shots.json` (or any structured shot list) and asks for prompts
- Names a specific generator (Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Kling, Veo, Seedance, Hailuo)
- Asks for "image prompts," "Midjourney prompts," "AI prompts," "generation prompts" for a storyboard
- Wants the same shot adapted to multiple generators

If the user wants to build a storyboard from scratch (no shots.json yet), use `storyboard-architect` first, then chain into this skill.

## What you produce

For a given `shots.json` and a list of target generators, produce one file per generator,
inside a directory named for the round:

```
output/prompts/round-1/
├── midjourney.txt          # If targeted
├── flux.txt
├── ideogram.txt
├── gpt-image.txt
├── nano-banana.txt
├── seedream.txt
├── kling.txt               # Motion-aware video, default
├── veo.txt                 # Motion, dialogue/lipsync + native audio
├── seedance.txt            # Motion, multi-shot sequences
└── hailuo.txt              # Motion, budget iteration
```

Round 1 is the first pass. Revision mode writes `output/prompts/round-2/`, and so on.
The round in the path is not decoration: prompt files used to be written to one fixed
path per generator, so round 2 destroyed round 1 and the prompt that actually produced
most of the surviving frames was gone.

Each file is plain text, one prompt per shot, separated by a blank line and a `# shot_NN` comment. Designed for copy-paste workflows, drop into the generator's UI or pipe into an API.

## The five-layer prompt anatomy

Every prompt is composed from these layers. Read `references/prompt-anatomy.md` for the full theory. Quick version:

1. **Brand Lock**, palette, type, mood, "never" list (constant across project)
2. **Series Lock**, character/environment/lighting anchors (constant across storyboard)
3. **Shot Spec**, framing, angle, motion, subject (per shot)
4. **Text Layer**, **never in the prompt**, composited separately
5. **Generator Adapter**, model-specific syntax wrapper

The first four come from `shots.json` and the brand-lock. The fifth is what this skill applies.

## Workflow

### Step 1. Read inputs

You need:

- `shots.json` (required), the structured shot list
- `brand-lock.snapshot.md` (required), referenced from shots.json
- Target generators (required), ask if not specified

Validate before composing:

```bash
python tools/validate_shots.py output/
```

If the brand-lock is missing or `shots.json` does not validate, stop and tell the user.
Don't try to forge prompts from incomplete data.

If `tools/` is not on hand (a Claude.ai upload, or a single-skill install), read the
schema from `../storyboard-architect/templates/shots.schema.json` and check by hand. That
relative path only resolves when the skills sit side by side; when they don't, ask the
user for the schema rather than composing from memory of it.

### Step 2. Pick the adapters

For each target generator, read the matching adapter file:

- `adapters/midjourney.md`
- `adapters/flux.md`
- `adapters/ideogram.md`
- `adapters/gpt-image.md`
- `adapters/nano-banana.md`
- `adapters/seedream.md`
- `adapters/kling.md`      (motion video, default)
- `adapters/veo.md`        (motion video, dialogue/lipsync + native audio)
- `adapters/seedance.md`   (motion video, multi-shot sequences)
- `adapters/hailuo.md`     (motion video, budget iteration)

Each adapter file documents the prompting style, parameter syntax, and known pitfalls for that generator. You **must** read the adapter before writing prompts for it. Don't guess from training data, image-gen syntax has churned multiple times.

**`adapters/_capabilities.json` is the single source of truth for per-generator limits** (`max_prompt_words`, `supports_text_render`, `supports_motion`, `aspect_param`, and so on). Read it once at the start and respect those values when composing, and do not target motion on a stills-only generator.

`max_prompt_words` is a ceiling. The range in an adapter `.md` is the recommended target
and always sits inside that ceiling, so a `.md` saying "40 to 70 words" under a ceiling of
120 is guidance, not a conflict. Where a fact in a `.md` and a fact in the JSON genuinely
disagree, **the JSON wins**.

That rule is now enforced rather than trusted. `tools/validate_capabilities.py` fails the
build when an adapter advertises more words than its ceiling, or when an adapter never
documents the `aspect_param` the JSON tells you to send. The second check exists because
nano-banana's matrix entry said `aspect_ratio` while its adapter said the API expects
`aspectRatio`; the precedence rule meant the wrong one won, silently, on every prompt.

### Step 3. Compose per shot

For each shot in `shots.json`, for each target generator:

1. Pull brand-lock palette, mood, "never" list
2. Pull series_lock character/environment/lighting
3. Pull shot framing/angle/motion/subject
4. **Strip any on_screen_text reference**, text never goes in the prompt
5. Apply the generator adapter's syntax wrapper
6. Append generator-specific parameters (aspect ratio, style flags, seed if applicable)

### Step 4. Write output files

One file per generator, into `output/prompts/round-{N}/`. Format:

```
# Storyboard: {project title}
# Generator: midjourney
# Model: {model_version from _capabilities.json}
# Aspect: 9:16
# Brand-lock: brand-lock.snapshot.md
# Run: {run_id from run.json}
# Round: 1

# shot_01, hook, 0.0-2.0s, MCU eye-level static
{the prompt}

# shot_02, pain, 2.0-6.0s, MS eye-level push
{the prompt}

...
```

The `#` lines are comments; the user copies just the prompt body. `tools/copy-prompt.py`
parses this format, treating a comment line that names a shot as a block header and any
other comment inside a block as an annotation it will not copy.

Record the run and round in the header, not a wall-clock "Generated" line. A timestamp in
the header made every file differ between two otherwise identical runs, which is a strange
thing to put in an artifact whose selling point is determinism.

### Step 4b. Append the round to run.json

After writing the files, append an entry to `run.json`'s `rounds` array: the round number,
`started_at`, a `reason`, and for each file its generator, path, SHA-256, and the shot ids
it covers.

```bash
shasum -a 256 output/prompts/round-1/*.txt
```

This is the only writeable part of `run.json`. Everything else was fixed when the
architect wrote it.

### Step 5. Hand off

Tell the user where the files are. Offer the next step:

> "Want me to QA the generated images against the storyboard? Use `visual-asset-critic` once you have the renders."

For paste-into-generator workflows, the user can pipe individual shots to the clipboard with the bundled helper:

```bash
python tools/copy-prompt.py output/prompts/round-1/midjourney.txt
python tools/copy-prompt.py output/prompts/round-2/revised-midjourney.txt --shot shot_03
```

This is optional. The `.txt` files are also directly readable, and the user can copy any block by hand. The helper exists for the case where the operator is bouncing between the terminal and a generator UI repeatedly.

## Revision mode (closing the QA loop)

This is what `visual-asset-critic`'s structured output is for. When the user hands you `shots.json` plus one or more `critique.json` files (the machine-readable verdict the critic writes), don't re-forge the whole storyboard, re-emit prompts for **only the shots that failed**, with the fix already applied.

### Trigger

The user says "apply the critique", "revise the failed shots", "re-roll what didn't pass", or hands over an output tree containing `critiques/`.

### Workflow

1. Read every critique under `output/critiques/round-{N}/`, where N is the highest round
   present. Each file is one shot's verdict (`shot_id`, `verdict`, `issues[]`).
2. Skip any with `verdict: ACCEPT`. Those are done.
3. **Stop on `REJECT`.** A REJECT means the critic found a blocking issue, or three or more
   major ones: a failure with no clear fix path. Re-emitting a prompt for it pretends
   otherwise. List the rejected shots, say what the critic said about them, and ask the
   user how to proceed. Common answers are a change to the shot spec, a change to the
   brand-lock, or a different generator, and all three are decisions above this skill's
   pay grade.
4. For every `REVISE` shot, walk its `issues[]` and branch on `fix_type`:
   - **`prompt-level`**, recompose that shot's prompt with the change in `fix` applied
     (e.g. add the missing series_lock anchor). Re-emit it.
   - **`re-roll`**, keep the prompt identical; the generation was just a bad sample.
     Re-emit it with a `# fix [Technical, re-roll]` annotation saying to take 2-3 samples
     and pick the cleanest.
   - **`post-level`**, do **not** re-emit. The fix happens in compositing, not a new
     generation.
5. A shot whose issues are all `post-level` needs no new prompt. Leave it out of the
   revised file and add its id to `post_only_shots` on the new round entry in `run.json`.
   Saying it in chat is not recording it: that obligation has to exist on disk or the
   compositing step is a memory.
6. Re-apply the five-layer anatomy and the same adapter as the original run.

### Output

Write `output/prompts/round-{N+1}/revised-{generator}.txt` containing only the revised
shots, then append the round to `run.json`. Annotate each shot with what changed and why,
citing the issue:

```
# shot_03, reframe, 11.0-16.0s, MCU eye-level push, revision (was REVISE)
# fix [Series Lock, major]: added 'salt-and-pepper hair' to the character anchor (was missing)
# fix [Shot Spec, minor]: medium shot -> medium close-up
{the revised prompt}
```

The block header leads with the shot id, same as a full pass. `tools/copy-prompt.py`
identifies a block by the shot id near the start of the line, so a header that led with
"Revision of" produced a file the paste helper could not read at all, which is
inconvenient in the one file the operator is about to paste from repeatedly.

Tell the user which shots were revised, which need only post work, which were rejected,
and which were already ACCEPT. Then they generate the revised shots and run
`visual-asset-critic` again.

### Determinism, and its limits

Given the same `shots.json`, the same brand-lock, and the same critique, this should
produce the same revised prompt. Nothing in the file format fights that any more: no
wall-clock stamps, no random ordering.

What the format cannot guarantee is the judgement in between. Applying a `fix` field means
reading a sentence of English and editing prose, so hold yourself to the narrowest edit
that satisfies the fix and leave every other layer byte-identical. If you find yourself
rewriting a prompt the critique did not ask you to touch, stop: that is drift, and it will
read as a mystery six shots later.

## Hard rules

These are non-negotiable. Violating them produces broken output even if the prompt looks fine.

### Rule 1. Text is never in the prompt

If the shot has `on_screen_text: "text_03"`, the prompt does NOT contain the text content. Text is composited separately. The only exception: Ideogram, where text-in-image is the reason you'd choose it, but even then, treat it as an explicit override flagged in rationale.

### Rule 2. Brand colors never in shot subject prose

Colors come from the series_lock color_grade and the brand_lock palette. They get rendered into the prompt by the adapter. Don't write "deep navy blazer" in the shot subject if "deep navy" is already in the palette, that's a duplicated description and produces oversaturation.

### Rule 3. Series_lock anchors are verbatim

The series_lock `environment`, `lighting`, and `color_grade` strings flow into every
prompt **verbatim**. This is what produces visual consistency across shots. If you
paraphrase or vary, shots stop matching each other.

Verbatim means the whole string, unedited. Not "the same idea in better prose". The
failure mode is specific and easy to walk into: you are writing fluent descriptive
English, `environment` is "minimalist home office, white walls, oak desk, single
houseplant", and it reads more naturally as "a minimal home office with white walls and
an oak desk". That is drift. The frames stop matching, and it stays invisible until you
line up six shots and see six different rooms.

Capitalising the first letter to start a sentence is fine, because the check is
case-insensitive. "Minimalist home office, white walls, oak desk, single houseplant."
satisfies the rule and reads like a sentence. Nothing else may change: no reordering, no
dropped clause, no synonym, no inserted adjective.

`character` is a warning rather than an error, because a shot with no person in it can
legitimately leave it out. When the shot has a person, it is verbatim too.

This rule is enforced now, not trusted:

```bash
python tools/validate_prompts.py output/
```

It exists because a careful authoring pass over a seven-shot storyboard drifted on these
anchors in all seven shots while every other validator stayed green.

### Rule 4. Adapters are the source of truth on syntax

If your training data says Midjourney uses `--style 4a` and the adapter file says `--style raw`, the adapter wins. Image-gen syntax changes monthly. The adapter is current; your training is not.

### Rule 6. Shot logic before shot poetry

A prompt can be beautifully written and still be impossible to shoot. Every prompt declares, before anything else:

- **Where the body sits in frame.** Which third it occupies. On a piece that composites two eras with a vertical mask, a body sitting on the centre line gets split in half and no amount of post fixes it. This is the single most expensive failure in the kit, and it is invisible until the mask goes on.
- **The point of view.** Profile, frontal, side, rear. "A man walking" is not a shot.
- **The direction of travel.** Left to right, right to left, toward camera. Without it the generator picks, and consecutive shots stop matching.
- **Nothing that contradicts the camera.** A subject who walks away from camera cannot also keep the same size in frame.
- **Handedness in any two-person contact.** If one raises a hand, name which one, or you get two right hands meeting.
- **No brand marks.** Logos and lettering are composited in post. Generators deform them.

### Rule 5. Prompts must be reproducible

Every prompt is composed from the same inputs the same way. If two consecutive runs produce different prompts for the same shot, the skill is broken. Determinism is the whole point.

## Reference files

- `references/prompt-anatomy.md`, the five-layer model in depth
- `references/consistency-locks.md`, how series_lock prevents shot drift
- `references/failure-modes.md`, common image-gen failures and their prompt-side fixes

## Adapters

One file per generator. Read these on demand, only for the generators being targeted.

| File | Generator | Strength |
|---|---|---|
| `adapters/midjourney.md` | Midjourney v7+ | Aesthetic, cinematic |
| `adapters/flux.md` | Flux 2 / Flux 1.1 Pro | Photorealism |
| `adapters/ideogram.md` | Ideogram v3 | Text in image (override only) |
| `adapters/gpt-image.md` | GPT Image 1.5 / 2 | Prompt accuracy, spatial reasoning |
| `adapters/nano-banana.md` | Gemini 2.5 Flash Image | Edit fidelity, inpainting |
| `adapters/seedream.md` | Seedream 4.5 | High-volume, cost-efficient |
| `adapters/kling.md` | Kling 3.0 | Motion video, default (best camera motion per dollar) |
| `adapters/veo.md` | Veo 3 | Motion video, dialogue/lipsync + native audio |
| `adapters/seedance.md` | Seedance 2.0 | Motion video, multi-shot sequences |
| `adapters/hailuo.md` | Hailuo 02 Pro | Motion video, budget iteration |

## Quality bar

Run the validator. Do not eyeball this list.

```bash
python tools/validate_prompts.py output/
python tools/copy-prompt.py output/prompts/round-1/flux.txt --list
```

`validate_prompts.py` checks the mechanical half, which is everything that used to be a
checkbox here:

- the header names the storyboard, generator, aspect, brand-lock, run, and round
- the generator is a real id in `_capabilities.json`
- the header aspect matches `project.aspect`
- no prompt exceeds that generator's `max_prompt_words` ceiling
- a full pass covers every shot; a revision file covers a subset of real shots
- no shot block is duplicated, and none has a header with no body
- **Rule 1**: no on-screen text copy appears in any prompt
- **Rule 3**: `environment`, `lighting`, and `color_grade` appear verbatim, with the
  character anchor as a warning
- **Rule 6**: every shot states which third of the frame the body occupies, its point of
  view and its direction of travel; no scale contradictions, no two people at the same
  frame edge, no unnamed handedness in a two-person contact, no brand marks in frame

What it cannot check, and you still have to:

- [ ] One output file per requested generator
- [ ] On a revision pass, the shots you left out are accounted for as ACCEPT, post-only,
      or rejected, and you said which is which
- [ ] Generator-specific parameters are right for the surface the user will paste into
- [ ] The round is appended to `run.json` with a hash per prompt file
- [ ] The prompt actually describes the shot, which is the part no validator will ever do

## Examples

`examples/one-shot-all-adapters/` contains a single shot rendered across seven adapters
side-by-side: the six stills generators plus Kling. Use it to calibrate output quality.
The three remaining motion adapters (Veo, Seedance, Hailuo) have no worked example yet;
their `.md` files carry a worked prompt each in the meantime.

For a complete two-round output tree, prompts and frames and critiques together, see
`../visual-asset-critic/examples/worked-run/`.


---

## ARCHIVO: visual-prompt-forge/adapters/flux.md

# Adapter: Flux (Flux 2 Pro / Flux 1.1 Pro / Flux Dev)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

Flux rewards natural-language prompts that read like a competent photographer briefing themselves. It interprets full sentences accurately and handles spatial relationships better than Midjourney. It's the photorealism leader as of Q2 2026, choose Flux over Midjourney when the brief calls for "looks like a real photograph" rather than "looks designed."

## Syntax pattern

```
{One or two natural-language sentences describing the subject and action}. {Sentence describing environment and lighting}. {Sentence describing technical/photographic specs}. {Brand mood line.}
```

Periods separate beats. Each sentence does one job. No bracket weights, no `--` flags. Flux is parameterless on most APIs (fal.ai, Replicate, BFL direct).

## Where parameters go

Flux parameters are typically passed alongside the prompt, not inside it:

| Parameter | Where | Default |
|---|---|---|
| `aspect_ratio` | API call field | from `project.aspect` |
| `output_format` | API call field | `png` for compositing |
| `safety_tolerance` | API call field | `2` (default) |
| `prompt_upsampling` | API call field | `false` for series work, auto-rewrites kill consistency |
| `seed` | API call field | set per-storyboard for series consistency |

In the `flux.txt` output, document parameters as a comment line above each prompt:

```
# shot_01, params: ar=9:16, seed=2840193, upsampling=false
{prompt}
```

## Length

Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.

## Composition mapping

Translate shot grammar into descriptive language:

| shot_grammar | Flux phrasing |
|---|---|
| `MCU eye-level` | `Medium close-up framing, camera at eye level.` |
| `WS overhead` | `Wide overhead shot, looking straight down.` |
| `push` | `Camera pushing slowly toward the subject.` |
| `handheld` | `Handheld camera with slight natural movement.` |
| `shallow DOF` | `Shot at f/1.8 with shallow depth of field, background softly out of focus.` |
| `deep DOF` | `Shot at f/8, everything in sharp focus front to back.` |

## Photographic specifics

Flux rewards camera/lens vocabulary. Add when relevant:

- `Shot on Hasselblad, 80mm lens, f/2.8`
- `Sony FX6, 35mm prime, natural light only`
- `Documentary 16mm film aesthetic, slight grain`
- `Editorial fashion lighting, large softbox key`

## Composition pattern

```
{Framing description with character anchor and action}. {Environment description from series_lock}. {Lighting sentence from series_lock}. {Photographic spec, camera, lens, depth of field}. {Color grade and mood from brand_lock}. Photorealistic, natural skin texture, no AI artifacts.
```

The closing "Photorealistic, natural skin texture, no AI artifacts" line meaningfully reduces the AI-look in Flux output. Include in every prompt.

## Example

**Same shot data as Midjourney example.**

**Output prompt:**
```
Medium shot of a founder in his mid-thirties with salt-and-pepper hair, wearing a navy crewneck, leaning forward at his laptop with his face partially turned toward window light. Composition leaves negative space on the right side of the frame. The setting is a minimalist home office with white walls and an oak desk. Soft natural side-light from a large window on the left, warm afternoon golden hour. Shot on a 50mm prime at f/2.0, shallow depth of field. Warm filmic color grade with muted teal shadows. Calm, considered mood, operator, not creator. Photorealistic, natural skin texture, no AI artifacts.
```

## Flux variant selection

| Variant | When | Cost ratio |
|---|---|---|
| Flux 2 Pro | Hero shots, final assets | 1× (highest) |
| Flux 1.1 Pro | Series work, balanced | ~0.6× |
| Flux Schnell | Quick iteration, drafts | ~0.1× |
| Flux Dev | Self-hosted, scale | ~0× per image, GPU cost |

Default to Flux 2 Pro for storyboard previews. The `flux.txt` file works for any variant, same prompt syntax.

## Pitfalls to avoid

- **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
- **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
- **Don't enable prompt upsampling for series work**, fal.ai's auto-rewrite produces inconsistent shots
- **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
- **Don't omit the photoreal closing line**, the "no AI artifacts" anchor measurably reduces the AI-look

## API access

Flux has multiple API surfaces:

- **fal.ai**, fastest, most stable, supports all variants
- **Replicate**, broader model selection, slightly slower
- **BFL direct API**, official, requires their key
- **WaveSpeedAI**, unified interface across many models

Same prompt syntax across all four. The `flux.txt` file is portable.


---

## ARCHIVO: visual-prompt-forge/adapters/gpt-image.md

# Adapter: GPT Image (1.5 / 2)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

GPT Image rewards paragraph-form prompts with explicit spatial reasoning and complex composition descriptions. It interprets relational language ("to the left of", "behind", "in the foreground") more accurately than any other generator. Choose GPT Image when the brief requires precise scene composition, multiple objects, or accurate text rendering.

## Syntax pattern

```
{Paragraph 1: subject, action, spatial composition}

{Paragraph 2: environment and contextual details}

{Paragraph 3: lighting, photographic specs, mood}
```

Paragraph breaks help GPT Image parse separate beats. One long monolithic paragraph underperforms, the model loses track of which detail applies where.

## Parameters

GPT Image is API-driven through OpenAI:

| Parameter | Default for storyboard work | Notes |
|---|---|---|
| `size` | `1024x1792` for 9:16, `1792x1024` for 16:9, `1024x1024` for 1:1 | Native aspect ratios |
| `quality` | `high` for hero shots, `medium` for series | |
| `style` | `natural` for photoreal, `vivid` for stylized | |
| `model` | `gpt-image-1.5` (or `gpt-image-2` if available) | |

Document in comment:
```
# shot_01, params: size=1024x1792, quality=high, style=natural, model=gpt-image-1.5
{prompt}
```

## Length

GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.

## Spatial language strength

GPT Image's distinctive capability, describe spatial relationships explicitly:

- "The founder is positioned in the left third of the frame, leaving the right two-thirds open."
- "A laptop sits on the desk in the foreground, a window with afternoon light is visible in the background."
- "The subject's shoulders are angled 30 degrees toward the camera, face turned to look at the off-frame light source."

Use this when the shot's composition is load-bearing.

## Composition pattern

```
{Subject paragraph: who is in the frame, what they're doing, where they are positioned in the composition. Reference series_lock character anchor verbatim.}

{Environment paragraph: setting, props, contextual elements. Pull from series_lock environment.}

{Technical paragraph: lighting from series_lock, photographic spec, color grade from brand_lock, mood. Close with "natural skin texture, no AI rendering artifacts" if photoreal.}
```

## Example

**Same shot data as previous examples.**

**Output prompt:**
```
A founder in his mid-thirties with salt-and-pepper hair, wearing a navy crewneck sweater, leans forward at his laptop. He is positioned in the left third of the frame, his face turned partially toward the window light off-camera left. The composition deliberately reserves the right two-thirds of the frame as negative space.

The setting is a minimalist home office. White walls, an oak desk in the immediate foreground, the laptop screen partially visible. A large window is implied off-frame to the left, source of the natural light. No clutter, no decorative objects.

Soft natural side-light from the window left, warm afternoon golden hour temperature, gentle shadow rolloff. Shot on a 50mm prime lens at f/2.0, shallow depth of field with the background softly out of focus. Warm filmic color grade with muted teal shadows. The mood is calm and considered, operator energy, not creator energy. Natural skin texture, no AI rendering artifacts.
```

## Text rendering

GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:

- Put the exact text in straight double-quotes within the prompt
- Specify position explicitly ("centered in the lower third")
- Specify approximate typeface character ("bold sans-serif", "elegant serif")
- Limit to one text element per prompt for reliability

Default for storyboard work is still composited text, keep the override flag pattern from the Ideogram adapter.

## Pitfalls to avoid

- **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
- **Don't omit spatial language when the shot has specific composition**, you're paying for the model's strength; use it
- **Don't pile too many objects**, five or fewer distinct elements per scene; more degrades fidelity
- **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
- **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't a complete fix. For pure photoreal, Flux is still stronger

## API access

GPT Image is OpenAI-only as of Q2 2026. Standard `images.generate` endpoint. Pricing roughly $0.04–0.08 per image depending on size and quality. ChatGPT Plus and above gives UI access.


---

## ARCHIVO: visual-prompt-forge/adapters/hailuo.md

# Adapter: Hailuo 02 Pro (motion-aware video, budget iteration)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

Hailuo 02 Pro is the cheap, fast iteration model. Strong motion response and prompt-following for the price, on fal.ai. Use it to **find the shot**, block out camera move, framing, and timing across many quick drafts, then re-generate the keeper on Kling (motion finals), Veo (dialogue), or Seedance (sequences). Treat Hailuo output as a working draft, not a final asset.

With video the **camera motion is load-bearing**. The prompt anatomy matches Kling; the difference is cost and intent: iterate freely here.

## Syntax pattern

```
{Camera motion sentence, leading.} {Subject and action over the duration.} {Environment and lighting from series_lock.} {Color grade and mood from brand_lock.}
```

## Parameters

| Parameter | Default | Notes |
|---|---|---|
| `duration` | `6s` | Check the current fal.ai ceiling for the Pro tier |
| `aspect_ratio` | from `project.aspect` | |
| `start_image` | optional | Image-to-video from an accepted still |
| `prompt_optimizer` | `false` for series | Auto-rewrite helps one-offs but breaks shot-to-shot consistency |

```
# shot_01 (draft). Hailuo 02 Pro: duration=6s, ar=9:16, optimizer=false
{prompt}
```

## Length

Hailuo handles **60–120 words** efficiently. Shorter than Kling/Veo. Keep drafts lean, you are testing motion and framing, not final polish.

## Motion vocabulary

The shot grammar `motion` field maps directly. One move per shot.

| `motion` | Video prompt phrase |
|---|---|
| `static` | "Static camera, locked off." |
| `push` / `pull` | "Camera dollies forward / backward slowly." |
| `pan-left` / `pan-right` | "Camera pans smoothly left / right." |
| `tilt-up` / `tilt-down` | "Camera tilts up / down." |
| `handheld` | "Handheld camera, subtle organic movement." |
| `orbit` | "Camera orbits the subject slowly." |
| `whip` | "Fast whip pan with motion blur." |
| `rack` | "Rack focus from foreground to background." |

## Iteration workflow

1. Draft the shot on Hailuo with `prompt_optimizer=false`. Cheap, fast.
2. Lock the camera move, framing, and timing that read best.
3. Re-generate the keeper on the right final-tier model: **Kling** for motion finals, **Veo** for dialogue/lipsync, **Seedance** for multi-shot sequences.
4. Carry the exact prompt forward, the adapters share the same five-layer anatomy, so the prompt body ports with only parameter changes.

## Example

**Draft of the `motion = "push"` shot.**

```
Camera dollies forward slowly at a steady pace. A founder in his mid-thirties with salt-and-pepper hair in a navy crewneck sits at his laptop in a minimalist home office and leans slightly forward toward window light off-camera left. Soft natural side-light, warm afternoon. Warm filmic color grade, muted teal shadows. Calm operator mood.
```

## Pitfalls to avoid

- **Don't ship Hailuo drafts as finals.** Re-roll the keeper on a final-tier model.
- **Don't enable the prompt optimizer for series work.** Auto-rewrite breaks shot-to-shot consistency.
- **Don't stack two camera moves.** One move per shot.
- **Don't include text content.** Composite captions in post.
- **Don't over-polish the draft prompt.** Spend words on motion and framing; save the photographic detail for the final-tier re-roll.

## Output handoff

Hailuo output is a draft used to choose the shot. The deliverable comes from the final-tier re-roll. If a Hailuo take is genuinely good enough to keep, treat it like any other clip: editorial assembly, text-overlay compositing, color grade, audio.


---

## ARCHIVO: visual-prompt-forge/adapters/ideogram.md

# Adapter: Ideogram (v3)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded social tiles, signage, packaging mockups. For everything else, default to Flux or Midjourney and composite text separately.

This adapter has **two modes**: composited (default) and text-in-image (override).

## Mode 1: Composited (default)

Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Syntax matches Flux conventions.

## Mode 2: Text-in-image (override)

Use when the on-screen text is meant to appear as part of the image itself, a poster headline, a sign in the scene, a packaging label. This is the only case where a generator prompt contains the text content.

**To trigger Mode 2, the shot must have an explicit override flag in rationale**, e.g.:
```
"rationale": "Text-in-image override: poster shot, headline must render as part of composition"
```

If you don't see that override flag, default to Mode 1.

## Syntax pattern (Mode 2)

```
{Subject and composition}. {Environment and lighting}. The text "{exact text}" appears {position description}, in {font style description}. {Brand mood and color closing.}
```

The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.

## Parameters

| Parameter | Where | Default |
|---|---|---|
| `aspect_ratio` | API field | from `project.aspect` |
| `model` | API field | `V_3` |
| `magic_prompt` | API field | `OFF` for series work, kills consistency |
| `style_type` | API field | `DESIGN` for posters, `REALISTIC` for scenes |
| `seed` | API field | set per-storyboard |

Document in comment block:
```
# shot_01, params: ar=9:16, model=V_3, magic_prompt=OFF, style=DESIGN, seed=2840193
{prompt}
```

## Length

Ideogram handles **60–120 words** comfortably. Text-bearing prompts run shorter still:
the more scene description you stack around a text instruction, the more likely the
render drops or garbles the copy.

## Composition pattern (Mode 1, composited)

Same as Flux pattern, no text in prompt:

```
{Framing description with character and action}. {Environment from series_lock}. {Lighting from series_lock}. {Photographic spec}. {Brand mood and color}. Clean composition with negative space for text overlay placement.
```

## Composition pattern (Mode 2, text-in-image)

```
{Subject/composition sentence}. {Environment/lighting sentence}. The text "{exact content}" appears {center / top-third / bottom-third / etc.}, in {font style, bold sans-serif / elegant serif / handwritten script / etc.}, color {hex or named color from brand-lock}. {Brand mood closing}.
```

## Example (Mode 2)

**Shot:** poster-style hero frame, brand launch
**Brand-lock:** display font is `Inter Black`, headline color `#0F1F3A` on `#F5F0E8` cream background
**Text content:** `built different`

**Output prompt:**
```
Editorial poster composition, dense cream background, single bold composition. Minimalist studio environment, even diffused lighting. The text "built different" appears center of the frame, in heavy sans-serif typography (Inter Black style), color deep navy #0F1F3A on cream #F5F0E8 background. Calm, considered, operator brand mood, confident without shouting.
```

## When NOT to use Ideogram

- **Photorealistic scenes with people**. Flux is better
- **Cinematic mood/aesthetic**. Midjourney is better
- **Product photography**. Flux 2 Pro is better
- **Series work where consistency matters**. Midjourney with `--cref` or Flux with seed-locking handles consistency better

Ideogram's specialty is text. If the brief doesn't need text-in-image, picking Ideogram is choosing the wrong tool.

## Pitfalls to avoid

- **Don't use Mode 2 without the rationale override**, defaults to text-in-image cause double-text (composited + generated) which destroys the comp
- **Don't trust magic_prompt**, it auto-rewrites and produces inconsistent shots across a series
- **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
- **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
- **Don't forget seed**, for any series work, lock the seed at the storyboard level


---

## ARCHIVO: visual-prompt-forge/adapters/kling.md

# Adapter: Kling 3.0 (motion-aware video)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

Kling 3.0 generates short video clips, not still frames. It is the default motion model: the best camera-motion realism per dollar on fal.ai, and the strongest image-to-video of the four. Reach for it first. Escalate to Veo (dialogue/lipsync), Seedance (multi-shot), or Hailuo (cheap iteration) only when the shot needs what Kling does not do.

With video the **camera motion becomes load-bearing** instead of optional. The same shot generates differently when `motion` is `static` versus `push` versus `handheld`. Use this adapter when the storyboard is destined for video generation rather than still-frame compositing.

## Syntax pattern

```
{Camera motion sentence, explicit, leading.} {Subject and action over the duration.} {Environment and lighting from series_lock.} {Photographic spec.} {Color grade and mood from brand_lock.}
```

Camera motion goes **first**. This is the inverse of image generators where camera is implied. With video the camera's behaviour is the first thing the model must understand.

## Parameters

| Parameter | Default | Notes |
|---|---|---|
| `duration` | `5s` for shots, `10s` for hero | 5s and 10s are the supported lengths |
| `aspect_ratio` | from `project.aspect` | |
| `cfg_scale` | `0.5` | Lower = looser/more dynamic, higher = closer to prompt |
| `start_image` | optional | Image-to-video. Pass an accepted still from `shots.json` assets to lock the opening frame |
| `tail_image` | optional | End-frame target for controlled moves |
| `negative_prompt` | per series | Supported. Use to suppress drift, e.g. `extra fingers, warped face` |

Document parameters as a comment line above each prompt:

```
# shot_01. Kling 3.0: duration=5s, ar=9:16, cfg=0.5, start_image=frames/round-1/shot_01.png
{prompt}
```

## Length

Kling handles **80–150 words** comfortably. Motion description adds a beat over a still prompt; do not pad past it.

## Motion vocabulary

The shot grammar `motion` field maps directly. One move per shot.

| `motion` | Video prompt phrase |
|---|---|
| `static` | "Static camera, locked off." |
| `push` | "Camera dollies forward slowly at a steady pace." |
| `pull` | "Camera dollies backward, pulling away from the subject." |
| `pan-left` / `pan-right` | "Camera pans smoothly to the left / right." |
| `tilt-up` / `tilt-down` | "Camera tilts upward / downward." |
| `handheld` | "Handheld camera, subtle organic movement, documentary feel." |
| `orbit` | "Camera orbits the subject in a slow circle." |
| `whip` | "Fast whip pan with motion blur." |
| `rack` | "Rack focus shifts from foreground to background mid-shot." |

## Subject motion

Beyond the camera, describe what the subject does over the duration:

> "Over the course of the shot the founder leans slightly forward and turns his face toward the window light off-camera left."

Static composition is not enough for video. This is what separates a video prompt from an image prompt.

## Example

**Same shot data as the image-adapter examples, with `motion = "push"`.**

```
Camera dollies forward slowly into the scene at a steady pace. A founder in his mid-thirties with salt-and-pepper hair, wearing a navy crewneck, sits at his laptop in a minimalist home office; over the shot he leans slightly forward and his face turns toward window light off-camera left, holding negative space on the right of frame throughout. Soft natural side-light from a large window, warm afternoon golden hour. Shot on a 50mm prime equivalent, shallow depth of field. Warm filmic color grade with muted teal shadows. Calm, considered, operator mood.
```

## Continuity across shots

- Use `start_image` from the previous shot's accepted final frame to chain a sequence.
- Repeat the series_lock character anchor verbatim in every prompt.
- Do not flip lighting direction between consecutive shots (window-left stays window-left).
- Even with start-frame locking, each clip is a fresh generation. Plan for an editorial pass.

## Pitfalls to avoid

- **Don't put camera motion at the end.** Kling parses motion best as the leading instruction.
- **Don't request multiple camera moves in one shot.** Pick one; compound moves break.
- **Don't describe motion faster than the duration allows.** A slow dolly over 5s is plausible; over 1s it is jitter.
- **Don't include text content.** Video text rendering is unreliable; composite or animate text in post.
- **Don't expect frame-perfect character match between clips.** Budget editorial cleanup.

## Output handoff

Generated clips are raw material, not deliverable. After generation they still need: editorial assembly to storyboard timing, text-overlay compositing from `text-overlays.json`, a color-grade pass, and audio (VO, music, sound design). Say this in handoff.


---

## ARCHIVO: visual-prompt-forge/adapters/midjourney.md

# Adapter: Midjourney (v7)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

Midjourney rewards short, high-signal prompts with strong adjective stacking and cinematic vocabulary. Long descriptive paragraphs underperform, the model interprets them as competing weights and produces muddled output.

## Syntax pattern

```
{subject}, {action}, {composition}, {environment}, {lighting}, {color/mood}, {style modifiers} --ar {ratio} --style {style} --s {stylize} {extras}
```

Comma-separated phrases. No full sentences. No connective words ("the", "with", "and") unless they're load-bearing.

## Parameter reference (current as of Q2 2026)

| Param | Values | Default to use | Notes |
|---|---|---|---|
| `--ar` | aspect ratio | from `project.aspect` | `--ar 9:16`, `--ar 16:9`, `--ar 1:1` |
| `--style` | `raw` / `4a` / `4b` / `4c` | `raw` | `raw` for photorealistic, omit for default Midjourney aesthetic |
| `--s` | 0–1000 | `50` for branded, `250` for artistic | Stylization weight. Lower = closer to prompt, higher = more MJ aesthetic |
| `--c` | 0–100 | omit | Chaos. Use only when exploring variations |
| `--seed` | integer | omit unless reproducing | For series consistency, set per-storyboard |
| `--cref` | image URL | use when character anchor exists | Character reference. Pair with `--cw` |
| `--cw` | 0–100 | `50` | Character weight. 100 = strict character match, 0 = clothing only |
| `--sref` | image URL | use when style anchor exists | Style reference |

## Length

Aim for **40–80 words per prompt** including parameters. Anything over 100 words underperforms.

## Composition mapping

Translate shot grammar into Midjourney-friendly phrases:

| shot_grammar | Midjourney phrase |
|---|---|
| `MCU eye-level` | `medium close-up, eye level` |
| `WS overhead` | `wide shot, overhead view, top-down` |
| `static` | (omit, static is default) |
| `push` | `dolly in, pushing forward` |
| `handheld` | `handheld documentary feel, slight motion blur` |
| `shallow DOF` | `shallow depth of field, f/1.8, bokeh background` |
| `deep DOF` | `deep focus, everything sharp, f/8` |

## Lighting language

Midjourney rewards specific lighting vocabulary:

- `soft natural light, large window left, warm afternoon golden hour`
- `hard top-light, single key, deep shadows, studio black backdrop`
- `practical mixed sources, neon accents, urban night, atmospheric haze`
- `volumetric backlight, rim light separating subject, cinematic haze`
- `chiaroscuro, dramatic side-light, painterly`

Pull verbatim from `series_lock.lighting`.

## Composition pattern

```
{framing} of {subject character_anchor}, {action}, {compositional note}, {environment from series_lock}, {lighting from series_lock}, {color_grade}, cinematic photography, {brand mood adjectives} --ar {aspect} --style raw --s 50
```

## Example

**Shot data:**
```json
{
  "id": "shot_03",
  "framing": "MS",
  "angle": "eye-level",
  "motion": "static",
  "subject": "Founder mid-thirties, leaning forward at laptop, face partially turned to window",
  "rationale": "MS framing leaves negative space right for text overlay"
}
```

**Series lock:**
```
character: founder, mid-thirties, salt-and-pepper hair, navy crewneck
environment: minimalist home office, white walls, oak desk
lighting: soft natural side-light, large window left, warm afternoon
color_grade: warm filmic, muted teal shadows
```

**Brand lock palette:** `#0F1F3A navy`, `#F5F0E8 cream`, `#D94F3A coral`

**Brand mood:** `calm, considered, operator, not creator`

**Output prompt:**
```
medium shot of founder mid-thirties, salt-and-pepper hair, navy crewneck, leaning forward at laptop, face partially turned to window light, negative space right of frame, minimalist home office, white walls, oak desk, soft natural side-light large window left, warm afternoon golden hour, warm filmic color grade, muted teal shadows, cinematic photography, calm considered operator mood --ar 9:16 --style raw --s 50
```

## Pitfalls to avoid

- **Don't use "AI" or "rendered"**, produces stylized outputs that look generated
- **Don't over-stack adjectives**, three adjectives per noun phrase max
- **Don't include text content**, even if the shot has `on_screen_text`, leave it out. Composited separately.
- **Don't use `--c` for series work**, chaos kills consistency
- **Don't change `--seed` mid-storyboard**, set once at series_lock level

## API access note

Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Discord or the web UI. Some teams use third-party wrappers (PiAPI, Useapi.net), those generally accept the same prompt syntax.


---

## ARCHIVO: visual-prompt-forge/adapters/nano-banana.md

# Adapter: Nano Banana (Gemini 2.5 Flash Image)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano Banana excels at variations, inpainting, and reference-based modification. The 2026 production pattern is to generate hero frames in Midjourney or Flux, then use Nano Banana for variants.

For storyboard work, Nano Banana is the right choice when you need **many variations of a single concept** or you're feeding generated images back through for refinement.

## Syntax pattern

Nano Banana takes natural-language prompts plus optional reference images. For text-to-image:

```
{Subject and action}. {Environment and lighting}. {Photographic specs and mood}.
```

For image-to-image (the strength), the prompt describes the modification:

```
{Modification description}. Keep {what to preserve}. Change {what to vary}.
```

## Parameters

Nano Banana goes through the Gemini API:

| Parameter | Default | Notes |
|---|---|---|
| `model` | `gemini-2.5-flash-image` | |
| `aspectRatio` | from `project.aspect` | Native support for `9:16`, `16:9`, `1:1`, `4:5`, `3:4`, `21:9` |
| `numberOfImages` | `1` for series, `4` for variant exploration | |
| `referenceImages` | array of base64 images | Optional |

Document:
```
# shot_01, params: ar=9:16, n=1, ref=none (or list of refs)
{prompt}
```

## Length

Nano Banana handles **60–120 words** efficiently. Shorter than GPT Image, longer than Midjourney.

## Composition pattern (text-to-image)

```
{Framing and subject sentence with character anchor}. {Environment and lighting from series_lock}. {Photographic spec, lens, depth of field, mood}. {Brand color grade closing}.
```

## Composition pattern (image-to-image, the strength)

When refining a hero shot generated elsewhere:

```
Reference: {description of input image}. Modify the image to {specific change}. Preserve the character's {face/clothing/pose}, the {environment elements}, and the lighting direction. Change {specific element} to {target state}.
```

## Example (text-to-image)

**Same shot data as previous examples.**

**Output prompt:**
```
Medium shot of a founder, mid-thirties, salt-and-pepper hair, navy crewneck sweater, leaning forward at his laptop with face turned partially toward window light. Composition leaves negative space on the right side. Minimalist home office, white walls, oak desk. Soft natural side-light from large window left, warm afternoon golden hour. Shot on 50mm prime, f/2.0, shallow depth of field, warm filmic color grade with muted teal shadows. Calm, considered, operator mood.
```

## Example (image-to-image variant)

**Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera

**Output prompt:**
```
Reference: medium shot of founder at laptop in home office, leaning forward, face partially turned to window. Modify the image so the founder looks directly into the camera lens with a calm, neutral expression. Preserve the character's face, salt-and-pepper hair, navy crewneck, body posture, the home office environment, the desk and laptop, and the warm afternoon side-lighting. Change only the head angle and gaze direction.
```

## Variant-generation workflow

The pattern Nano Banana enables, and the reason it's worth including in storyboard work:

1. Generate hero shot in Midjourney or Flux (one prompt → one image)
2. Feed that image to Nano Banana with variation prompts
3. Get 4–8 variants of the same shot for editorial selection
4. Composite text on the chosen variant

When generating prompts for Nano Banana in `nano-banana.txt`, include both:

- The text-to-image prompt (for first-pass generation)
- A modification template comment showing how to use the result for variants:

```
# shot_01, text-to-image prompt:
{prompt}

# shot_01, variant template (after generating once):
# Reference: [the generated image]. Modify the image to {your change}.
# Preserve {anchors}. Change {target}.
```

## Pitfalls to avoid

- **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
- **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
- **Don't pile multiple modifications in one image-to-image prompt**, one change per pass produces cleaner results
- **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
- **Don't include text content in image prompts**, composite separately; text rendering is mediocre

## API access

Through Google Gemini API (`gemini-2.5-flash-image` model endpoint). Available via:

- Gemini API direct
- Vertex AI
- Replicate
- fal.ai (under "google/nano-banana")

Same prompt syntax across all four.


---

## ARCHIVO: visual-prompt-forge/adapters/seedance.md

# Adapter: Seedance 2.0 (motion-aware video, multi-shot)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

Seedance 2.0 is the multi-shot model. It can generate a **short sequence of cuts in a single generation** while holding subject and environment consistency across them. Reach for it when several consecutive storyboard beats share one subject and you want them to feel like one continuous take, it beats stitching four independent Kling clips that drift apart. For a single isolated shot, Kling is the simpler default.

With video the **camera motion is load-bearing**, and with Seedance the **cut structure is also load-bearing**, you describe the sequence of shots, not just one frame.

## Syntax pattern

Single shot:
```
{Camera motion sentence, leading.} {Subject and action.} {Environment and lighting from series_lock.} {Color grade and mood from brand_lock.}
```

Multi-shot sequence (Seedance's strength):
```
Shot 1: {camera + action}. Shot 2: {camera + action}. Shot 3: {camera + action}. Consistent subject throughout: {series_lock character anchor, verbatim}. {Environment and lighting from series_lock.} {Color grade and mood from brand_lock.}
```

## Parameters

| Parameter | Default | Notes |
|---|---|---|
| `duration` | `5s` per shot block | Multi-shot sequences run longer; check the current fal.ai ceiling |
| `aspect_ratio` | from `project.aspect` | |
| `start_image` | optional | Image-to-video reference for the opening frame |
| `shots` | 1 | Number of cuts in the sequence when using multi-shot mode |

```
# shot_02-shot_04. Seedance 2.0: ar=9:16, shots=3, multi-shot sequence
{prompt}
```

## Length

Seedance handles **80–150 words**. In multi-shot mode, keep each shot clause short, one camera move and one action per cut.

## When to use multi-shot vs single

| Situation | Mode |
|---|---|
| One beat, one frame | Single shot (or use Kling) |
| 2–4 consecutive beats, same subject, want continuity | Multi-shot sequence |
| Beats with different subjects/locations | Separate generations, assemble in edit |

Map consecutive `shots.json` entries that share a subject into one Seedance multi-shot prompt; reference them by id range in the comment.

## Motion vocabulary

The shot grammar `motion` field maps directly. One move per cut.

| `motion` | Video prompt phrase |
|---|---|
| `static` | "Static camera, locked off." |
| `push` / `pull` | "Camera dollies forward / backward slowly." |
| `pan-left` / `pan-right` | "Camera pans smoothly left / right." |
| `tilt-up` / `tilt-down` | "Camera tilts up / down." |
| `handheld` | "Handheld camera, subtle organic movement." |
| `orbit` | "Camera orbits the subject slowly." |
| `whip` | "Fast whip pan with motion blur." |
| `rack` | "Rack focus from foreground to background." |

## Example

**Three consecutive beats of the same founder, mapped to one sequence.**

```
Shot 1: static eye-level, the founder closes his laptop and exhales. Shot 2: slow push toward his face as he looks toward the window. Shot 3: handheld over-the-shoulder as he stands and crosses the room. Consistent subject throughout: a founder in his mid-thirties with salt-and-pepper hair, navy crewneck. Minimalist home office, white walls, oak desk, soft natural side-light from a large window on the left, warm afternoon golden hour. Warm filmic color grade with muted teal shadows. Calm, considered, operator mood.
```

## Pitfalls to avoid

- **Don't force unrelated beats into one sequence.** Multi-shot is for shots that genuinely belong to one take.
- **Don't write more than ~4 cuts per generation.** Consistency degrades past that; split and assemble in edit.
- **Don't vary the character anchor between cuts.** Restate it once for the whole sequence, verbatim.
- **Don't include text content.** Composite captions from `text-overlays.json` in post.
- **Don't stack two camera moves inside one cut.** One move per cut.

## Output handoff

Seedance returns a sequence as a single clip (or a small set). It still needs: editorial trimming to exact storyboard timing, text-overlay compositing, a color-grade pass, and audio. Multi-shot output usually needs *less* assembly than stitched single clips, which is the point. Say so in handoff.


---

## ARCHIVO: visual-prompt-forge/adapters/seedream.md

# Adapter: Seedream (4.5 / 4.0)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

ByteDance's Seedream models are the high-volume cost-efficient choice. Quality is below Flux 2 Pro and Midjourney v7 but above older mid-tier models, and the cost-per-image is roughly 5–10× lower. Choose Seedream when you're producing **many variations or doing rapid concept iteration**, not for hero/final assets.

For storyboard work, Seedream is useful for the storyboard preview pass: render every shot quickly to validate composition before committing to higher-cost generation for finals.

## Syntax pattern

Seedream rewards **short, precise prompts**. Long descriptive prompts underperform, the model interprets them as competing weights and produces mush. Closer to Midjourney's style than Flux's.

```
{Subject phrase}, {action}, {environment}, {lighting}, {mood/style}, {aspect note}
```

Comma-separated, no full sentences.

## Parameters

Seedream is API-driven through fal.ai, Replicate, or BytePlus direct:

| Parameter | Default | Notes |
|---|---|---|
| `aspect_ratio` | from `project.aspect` | |
| `seed` | per-storyboard | Critical for series consistency |
| `guidance_scale` | `4.5` | Lower = more creative, higher = more literal |
| `steps` | `28` | Default. Increase to 50 for higher quality at cost |

Document:
```
# shot_01, params: ar=9:16, seed=2840193, guidance=4.5, steps=28
{prompt}
```

## Length

**40–70 words per prompt**. Shorter than most. Don't pad.

## Composition pattern

```
{Framing} of {character anchor}, {action}, {environment from series_lock}, {lighting from series_lock}, {color grade from brand_lock}, {one mood adjective}, photorealistic
```

## Example

**Same shot data as previous examples.**

**Output prompt:**
```
Medium shot of founder mid-thirties, salt-and-pepper hair, navy crewneck, leaning forward at laptop, face turned to window light, minimalist home office, oak desk, soft natural side-light from large window, warm afternoon, warm filmic color grade, muted teal shadows, calm operator mood, photorealistic
```

## When Seedream is the right choice

- **Storyboard preview pass**, render all shots quickly at low cost to validate composition before final pass
- **High-volume social content**, when you need 50+ images per day and the quality bar allows it
- **Concept exploration**, quick iteration on shot ideas before committing to a final generator
- **Placeholder content**, assets that will be replaced once the brand-lock is finalized

## When Seedream is the wrong choice

- **Hero shots / final deliverables**. Flux 2 Pro or Midjourney v7 produce noticeably better output
- **Photorealistic product shots**. Flux is meaningfully better for product fidelity
- **Text-heavy designs**. Ideogram or GPT Image
- **Cinematic mood pieces**. Midjourney is the move

## Series consistency

Seedream's character consistency is weaker than Midjourney `--cref` or Ideogram omni-reference. To compensate:

- **Lock the seed** at the storyboard level (same seed across all shots in a series)
- **Verbatim repeat** the character anchor string from series_lock in every prompt
- **Don't vary** the lighting language between shots, series_lock string in, no paraphrasing
- **Accept** that some shots will need re-rolls; budget for it

## Pitfalls to avoid

- **Don't write paragraphs**. Seedream wants comma-separated phrases
- **Don't use `--ar` syntax**, pass aspect_ratio as a parameter
- **Don't include text content**, text rendering is poor; composite separately
- **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
- **Don't skip the seed lock for series work**, without it, character consistency breaks

## API access

- **fal.ai**, `bytedance/seedream-4.5` and `bytedance/seedream-4.0`
- **Replicate**, `bytedance/seedream-4.5`
- **BytePlus**, direct API, requires their account

Same prompt syntax across surfaces.


---

## ARCHIVO: visual-prompt-forge/adapters/veo.md

# Adapter: Veo 3 (motion-aware video, native audio)

> Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the two drift.

Veo 3 is the dialogue and lipsync model. It is the only adapter that generates **synchronised native audio**, speech, ambience, and sound effects, in the same pass as the video. It also has the strongest prompt adherence and physical realism of the four motion models. It is the most expensive, so reserve it for shots that actually need spoken dialogue, lipsync, or audio baked in. For silent B-roll and camera moves, Kling is the cheaper default.

With video the **camera motion is load-bearing**. When the shot has dialogue, the **spoken line is also load-bearing** and is written into the prompt (this is the one place where text belongs in a prompt, it is audio, not on-screen text).

## Syntax pattern

```
{Camera motion sentence, leading.} {Subject and action over the duration.} {Dialogue line, in quotes, if any.} {Environment and lighting from series_lock.} {Audio direction.} {Color grade and mood from brand_lock.}
```

## Parameters

| Parameter | Default | Notes |
|---|---|---|
| `duration` | `8s` | Veo's native clip length |
| `aspect_ratio` | from `project.aspect` | |
| `generate_audio` | `true` | The reason to choose Veo. Set `false` only for silent shots |
| `start_image` | optional | Image-to-video from an accepted still |

```
# shot_04. Veo 3: duration=8s, ar=9:16, generate_audio=true
{prompt}
```

## Length

Veo handles **80–150 words**. Spend the headroom on action timing and audio direction, not adjective stacks.

## Dialogue and lipsync

When the shot calls for the subject to speak, put the exact line in quotes:

> The founder looks directly into the lens and says, "I built the system once, and it runs without me."

Keep spoken lines to what fits the duration, roughly 12–18 words for an 8s clip. Direct the delivery ("calm, unhurried"). Veo lipsyncs the quoted line.

## Motion vocabulary

The shot grammar `motion` field maps directly. One move per shot.

| `motion` | Video prompt phrase |
|---|---|
| `static` | "Static camera, locked off." |
| `push` / `pull` | "Camera dollies forward / backward slowly." |
| `pan-left` / `pan-right` | "Camera pans smoothly left / right." |
| `tilt-up` / `tilt-down` | "Camera tilts up / down." |
| `handheld` | "Handheld camera, subtle organic movement." |
| `orbit` | "Camera orbits the subject slowly." |
| `whip` | "Fast whip pan with motion blur." |
| `rack` | "Rack focus from foreground to background." |

## Audio direction

Even on silent shots Veo can place ambience. Be explicit and brief:

- "Audio: quiet room tone, faint keyboard, no music."
- "Audio: soft afternoon ambience, distant street."

If the brand-lock or storyboard owns the audio bed (VO recorded separately, music added in post), set `generate_audio=false` and skip this section so Veo does not invent a competing track.

## Example

**Shot with `motion = "static"` and a spoken line.**

```
Static camera, locked off, eye level. A founder in his mid-thirties with salt-and-pepper hair in a navy crewneck sits at his laptop in a minimalist home office and looks directly into the lens. He says, "I built the system once, and it runs without me," calm and unhurried. Soft natural side-light from a large window on the left, warm afternoon golden hour. Audio: quiet room tone, faint keyboard, no music. Warm filmic color grade with muted teal shadows. Calm, considered, operator mood.
```

## Pitfalls to avoid

- **Don't use Veo for silent B-roll.** You are paying for an audio engine you turned off; use Kling.
- **Don't overrun the duration with dialogue.** A line that needs 12s of speech will clip or rush at 8s.
- **Don't put on-screen text in the prompt.** Spoken lines are fine; rendered captions still come from `text-overlays.json` in post.
- **Don't stack two camera moves.** One move per shot.
- **Don't let Veo's auto-audio fight a post audio bed.** Pick one owner of sound per shot.

## Output handoff

Veo clips arrive with audio attached. They still need: editorial assembly to timing, on-screen text compositing from `text-overlays.json`, a color-grade pass, and an audio decision, keep Veo's native track, or mute it and use the storyboard's recorded VO and music. State which in handoff.


---

## ARCHIVO: visual-prompt-forge/examples/one-shot-all-adapters/README.md

# One Shot, All Adapters

This example takes a single shot from the WhyStrohm 30-second pitch and renders it through the generator adapters in the pack. Use it as a calibration reference: same intent, same data, different prompt syntaxes. Six stills adapters are shown, plus the default motion adapter (Kling) standing in for the motion video lane.

## The source shot

From `examples/30s-pain-proof-promise/shots.json`:

```json
{
  "id": "shot_04",
  "beat": "reframe",
  "start": 11.0,
  "end": 16.0,
  "framing": "MCU",
  "angle": "eye-level",
  "motion": "push",
  "depth_of_field": "shallow",
  "subject": "founder, same posture, looking at camera, expression shifts from tired to clear, small almost-smile",
  "rationale": "Slow push as the reframe lands. Same character, same environment, only the expression changes. The change is the point."
}
```

## Series lock context (constant across all adapters)

```
character: founder, mid-thirties, salt-and-pepper hair, navy crewneck, calm posture
environment: minimalist home office, white walls, oak desk, single houseplant
lighting: soft natural side-light, large window camera-left, warm afternoon golden hour
color_grade: warm filmic, muted teal shadows, slight grain
```

## Brand mood

`calm, considered, operator (not creator), confident without volume`

## Outputs

Each `.txt` file in this directory is the prompt for one adapter:

- `midjourney.txt`. Midjourney v7
- `flux.txt`. Flux 2 Pro
- `ideogram.txt`. Ideogram v3 (composited mode)
- `gpt-image.txt`. GPT Image 1.5
- `nano-banana.txt`. Gemini 2.5 Flash Image
- `seedream.txt`. Seedream 4.5
- `kling.txt`. Kling 3.0 (motion video, the default motion adapter)

The other three motion adapters (`veo` for dialogue/lipsync, `seedance` for multi-shot sequences, `hailuo` for budget iteration) follow the same five-layer anatomy as Kling and are chosen by need; see their files in `adapters/`. This single silent push shot doesn't exercise dialogue or a sequence, so Kling is the representative motion example here.

Note the differences:

- **Midjourney** is a comma-separated stack with `--ar`, `--style raw`, `--s 50` flags
- **Flux** is natural-language paragraphs with no flags, parameters live in the API call
- **GPT Image** uses paragraph breaks and explicit spatial language
- **Seedream** is the shortest, comma stack like Midjourney but no flags
- **Kling** (and every motion adapter) leads with camera motion (the stills adapters let it be implicit)

Same intent. Different syntax. Same brand-lock and series-lock anchors flowing through all of them.

## What's not in any prompt

The on-screen text content. Even though shot_04 has an on-screen text overlay (`text_03`, "You don't have a content problem. You have an infrastructure problem."), none of the prompts contain that text. It's composited separately per the five-layer model.

This is the discipline: the image generator handles the image, the compositor handles the text, neither tries to do the other's job.


---

## ARCHIVO: visual-prompt-forge/references/consistency-locks.md

# Consistency Locks

Visual consistency across a storyboard is the hardest problem in AI image generation. Generators are stateless, every prompt is interpreted fresh. Without consistency locks, shot 1 and shot 7 will look like different productions.

This document covers the techniques that actually work in 2026.

## Lock 1. Verbatim character anchors

The most effective single technique. The character is described in `series_lock.character` once, and that exact string appears in every shot's prompt verbatim. No paraphrasing, no synonyms, no "improvement."

**Good (consistent):**
```
shot_01: "founder, mid-thirties, salt-and-pepper hair, navy crewneck, stubble"
shot_02: "founder, mid-thirties, salt-and-pepper hair, navy crewneck, stubble"
shot_07: "founder, mid-thirties, salt-and-pepper hair, navy crewneck, stubble"
```

**Bad (inconsistent):**
```
shot_01: "a thoughtful entrepreneur in his thirties, dark hair, casual sweater"
shot_02: "founder, 35 years old, salt-pepper hair, blue knit top"
shot_07: "the man in the home office, navy shirt"
```

Even small variations compound. Lock the string. Repeat verbatim.

## Lock 2. Verbatim environment anchors

Same principle for `series_lock.environment`. The environment string is identical in every shot prompt. The shot's individual subject describes what changes within the environment, not the environment itself.

## Lock 3. Verbatim lighting anchors

Same principle for `series_lock.lighting`. Lighting direction in particular is critical, flipping window-left to window-right between shots produces obvious cuts where there shouldn't be any.

## Lock 4. Seed locking

For generators that support seeds (Flux, Seedream, Ideogram, Stable Diffusion), set the seed at the storyboard level. Same seed across every shot. This anchors the generator's randomness so character features carry.

In `shots.json`, you can document the seed at the project level:

```json
{
  "project": {
    "title": "...",
    "seed": 2840193
  }
}
```

The adapter reads this and applies to every prompt.

**Caveat:** Midjourney and some motion models (Veo, Seedance) handle seeds differently, or not at all. Document seed-locking as best-effort, not guaranteed.

## Lock 5. Reference images (`--cref`, omni-reference, image-to-image)

For Midjourney v7, Ideogram v3, and Nano Banana, you can pass a reference image alongside the prompt to anchor character or style.

**Workflow:**

1. Generate the hero shot first (any shot, usually `shot_01` or whichever is most defining)
2. Use that image as the reference for every subsequent shot
3. Each subsequent prompt has the verbatim character anchor PLUS the reference image link

For Midjourney: `--cref {url} --cw 50` (character weight 50 = features only, not clothing).

For Ideogram: `omni-reference` parameter with the image.

For Nano Banana: `referenceImages` array.

**This is the most effective lock for character consistency** in 2026. Use it whenever the storyboard features the same person across multiple shots.

## Lock 6. Style references

When the storyboard has a distinctive visual style (specific film stock, specific lighting school, specific color theory), use a style reference image:

- Midjourney: `--sref {url}`
- Ideogram: style reference parameter
- Flux: not directly supported; bake style language into prompt instead

A consistent style reference across all shots produces aesthetic continuity even when characters or environments shift.

## Lock 7. Lighting direction continuity

A subtle one that breaks scenes when violated. If `series_lock.lighting` says "soft natural side-light, large window LEFT", then every shot's lighting must respect that direction.

When a shot reverses character orientation (e.g., over-the-shoulder reverse), update the rationale to acknowledge the lighting flip:

```
"rationale": "OTS reverse, light source now camera-right (matching scene continuity from window-left in master)"
```

If you find yourself flipping light direction without rationale, you're producing visual jump cuts.

## Lock 8. Color grade flow-through

The `series_lock.color_grade` string flows into every prompt verbatim. Same as character/environment/lighting. If shot 1 is "warm filmic, muted teal shadows" and shot 7 is "cinematic teal and orange", the audience will read it as different scenes.

## Failure modes when locks are missing

| Missing lock | Failure mode |
|---|---|
| Character | Different person every shot |
| Environment | Scene jumps |
| Lighting | Time-of-day jumps, eye-line breaks |
| Seed | Random feature drift |
| Reference image | Loose character interpretation |
| Color grade | Tonal whiplash |

Every one of these is a production problem editorial cannot fully fix. Lock at the prompt level. Save the editor's time.

## What doesn't work

A few things people try that don't actually fix consistency:

- **Adding "consistent character" or "same person" to the prompt**, generators don't read meta-instructions
- **Numbering shots in the prompt** ("shot 3 of 7, same as before"), generators don't have memory across calls
- **Long descriptive paragraphs of the character**, past 4–5 features, the generator starts dropping details randomly
- **Asking for "exactly the same"**, there is no such thing in stateless image gen; you reduce drift, you don't eliminate it

Accept that some shots will need re-rolls. Budget for it. The locks reduce the failure rate; they don't eliminate it.


---

## ARCHIVO: visual-prompt-forge/references/failure-modes.md

# Failure Modes

What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.

## Failure 1. The "AI look"

**Symptoms:** plastic skin, oversaturated colors, eyes too symmetrical, hands wrong, generic stock-photo composition, lighting that's too even, "rendered" feel.

**Causes:**
- Generic mood adjectives ("beautiful", "stunning", "amazing")
- Stable Diffusion crutches ("4k", "highly detailed", "masterpiece") in non-SD generators
- Missing photographic specifics
- No "never" list applied from brand-lock

**Prompt-level fixes:**
- Add specific lens and aperture ("50mm prime, f/2.0")
- Add film stock or camera reference ("Sony FX6", "Kodak Portra 400 film stock")
- Add "natural skin texture, no AI rendering artifacts" closing line (Flux, GPT Image)
- Verify brand-lock "never" list is being applied, if it includes "no AI uncanny", surface that into the prompt
- Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots

**Accept editorially when:** the brief is for stylized content where realism isn't the goal.

## Failure 2. Character drift across shots

**Symptoms:** same person looks different in shot 1 vs shot 5; clothing changes; hair color shifts; age perceived differently.

**Causes:**
- Series_lock character string paraphrased rather than verbatim
- No reference image passed (`--cref`, omni-reference)
- Seed not locked
- Too few features described in character anchor (gives generator too much room)

**Prompt-level fixes:**
- Verify character string is verbatim across every prompt
- Add 1–2 more specific features ("small scar above left eyebrow", "black wireframe glasses")
- Use reference image after the first successful shot
- Lock seed at storyboard level
- For Midjourney, use `--cref` with `--cw 50`

**Accept editorially when:** character consistency is genuinely impossible to lock. Budget re-rolls, typically 2–3× per problematic shot.

## Failure 3. Text in image looks bad

**Symptoms:** text is misspelled, kerning is off, font is wrong, multiple text elements compete.

**Causes:**
- Text was put in the image prompt instead of being composited
- Wrong generator chosen (using Midjourney for text-heavy work)
- Multiple text elements in one prompt

**Prompt-level fixes:**
- The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.
- If text must be in-image (poster work), use Ideogram v3 with explicit override flag
- Limit to one text element per prompt
- Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram

**Accept editorially when:** the deliverable genuinely requires baked-in text and Ideogram's output is close enough to retouch.

## Failure 4. Lighting direction inconsistency

**Symptoms:** shot 3 has light from window-left, shot 4 has light from window-right, they cut together as a continuity error.

**Causes:**
- Lighting language paraphrased rather than verbatim from series_lock
- Reverse-angle shots not flagged in rationale
- Generator interpreting lighting ambiguously

**Prompt-level fixes:**
- Verify lighting string is verbatim across prompts
- Be explicit about direction: "from camera-left" not "from one side"
- For reverse-angle shots, flag in rationale and update lighting language for that shot only
- For Flux and GPT Image, add the photographic spec ("key light camera-left at 45 degrees")

**Accept editorially when:** lighting drift is subtle enough that color grading will fix it.

## Failure 5. Composition doesn't reserve space for text overlay

**Symptoms:** the storyboard says text goes in the right third, but the generated image has the subject filling the right third.

**Causes:**
- Shot subject didn't include negative-space note
- Generator interpreting "centered subject" by default

**Prompt-level fixes:**
- Add explicit composition note: "subject framed in left third, right two-thirds open for text overlay"
- For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
- Re-roll with explicit composition prompt, this often fixes on second try

**Accept editorially when:** image is otherwise great. Reposition text overlay to fit the actual composition.

## Failure 6. Series feels "different" even with locks applied

**Symptoms:** all locks are in place, prompts look right, but the storyboard feels disjointed when viewed end-to-end.

**Causes:**
- Color grade language drifting between shots (one says "warm filmic", another says "cinematic")
- Aspect ratio drift (some 9:16 generations are taller than others)
- Mood adjectives shifting ("calm" in shot 1 vs "energetic" in shot 5 even though brief was uniform)

**Prompt-level fixes:**
- Audit every prompt against series_lock and brand-lock, verbatim check
- Verify aspect ratio is identical across all prompts
- Lock the brand mood adjectives, same set in every prompt

**Accept editorially when:** the disjoint feel is below the noise floor for the medium (e.g. fast-cut social where each shot is on screen <2s).

## Failure 7, "Looks fine but doesn't match the brief"

**Symptoms:** image is technically good but doesn't capture what the brief was actually about.

**Causes:**
- The shot subject in `shots.json` was vague
- The brief context wasn't surfaced into the prompt
- The generator is producing competent generic output rather than specific intent

**Prompt-level fixes:**
- Tighten the shot's subject field, what specifically is the audience meant to feel or notice
- Include a one-phrase intent at the end ("the moment of recognition", "the calm before the decision")
- For complex scenes, add a "what this shot conveys" line

**Accept editorially when:** generation is close enough that retouching gets there. Don't burn API credits chasing perfect on-prompt.

## When to stop iterating prompts

Three signs:

1. You've re-rolled the same shot 5+ times with no improvement → the prompt is fine; the model can't render this concept; pick a different shot or different generator
2. You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-production
3. The image is 80% right and the gap is editorial → ship to post and let the editor finish

Generation is one stage in a pipeline. Don't try to make it the whole pipeline.


---

## ARCHIVO: visual-prompt-forge/references/prompt-anatomy.md

# Prompt Anatomy: The Five Layers

Every image prompt this skill produces is composed from five layers. Four are inputs, one is applied at compose-time. Understanding the layers is the difference between bulletproof prompts and lottery tickets.

## Layer 1. Brand Lock

**What:** the locked brand parameters for the entire project.
**Source:** `brand-lock.snapshot.md` referenced in `shots.json`.
**Constant across:** every storyboard, every shot.

Contains:

- Palette (hex values)
- Typography (font names, weights)
- Mood descriptors (3–5 adjectives that describe the brand's emotional posture)
- "Never" list (things this brand never does, e.g. "no stock photo aesthetic", "no AI uncanny", "no over-saturated", "no shouting copy")
- Aspect ratios used
- Color grade direction

This layer answers: **what does the brand always look and feel like?**

## Layer 2. Series Lock

**What:** the locked anchors for this specific storyboard.
**Source:** `shots.json` → `series_lock`.
**Constant across:** every shot in this one storyboard.

Contains:

- Character anchor (who's in frame, described identically every shot)
- Environment description (where the action takes place, identical every shot)
- Lighting setup (direction, source, color temperature, identical every shot)
- Color grade (filmic look, identical every shot)

This layer answers: **what stays the same across this storyboard?**

The series_lock is what makes shot 1 and shot 7 feel like the same piece. Without it, every generated frame looks like a different production.

## Layer 3. Shot Spec

**What:** the per-shot variables.
**Source:** `shots.json` → `shots[i]`.
**Variable across:** every shot.

Contains:

- Framing (ECU, CU, MS, etc.)
- Angle (eye-level, high, low, etc.)
- Motion (static, push, pull, etc.)
- Subject (what's happening in this specific shot)
- Depth of field
- Rationale (audit trail, why this shot, this beat, this moment)

This layer answers: **what's different about this specific shot?**

## Layer 4. Text Layer

**What:** on-screen text composited after generation.
**Source:** `text-overlays.json`.
**Never appears in image prompts** (except Ideogram Mode 2 with explicit override).

Why text is a separate layer:

1. **Editability.** Composited text can be revised without re-generating images.
2. **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.
3. **Animation.** Animated text needs After Effects / Remotion / CapCut. Static rendered text is dead-on-arrival for motion content.
4. **Brand control.** Composited text uses exact brand fonts and exact brand colors. Generated text approximates.

## Layer 5. Generator Adapter

**What:** model-specific syntax wrapper.
**Source:** the relevant `adapters/{generator}.md` file.
**Variable across:** every target generator.

This is the only layer the skill *applies* (vs. reads). Layers 1–4 are inputs; Layer 5 is the renderer that turns inputs into a generator-specific string.

The adapter handles:

- Word order (Midjourney leads with subject; motion adapters like Kling lead with camera motion)
- Length conventions (Seedream short, GPT Image long)
- Parameter syntax (`--ar 9:16` vs `aspect_ratio: "9:16"`)
- Idiosyncratic strengths (Ideogram for text, Flux for photoreal, etc.)

## How layers compose

For a single shot's prompt:

```
Layer 1 (brand) ───┐
                   │
Layer 2 (series) ──┼──> Layer 5 (adapter) ──> {generator-specific prompt}
                   │
Layer 3 (shot) ────┘

Layer 4 (text) ────> separate compositing pipeline
```

The adapter pulls from Layers 1–3 and produces a string. Layer 4 lives parallel and never enters the prompt.

## Why this matters operationally

**Change the brand color** → edit brand-lock.md. Every prompt across every storyboard updates. No find-and-replace across files.

**Change the character** → edit series_lock in shots.json. Every shot in this storyboard updates. Other storyboards untouched.

**Change one shot** → edit just that shot's spec. Other shots unaffected.

**Change the generator** → swap adapters. Same shot data, different output file. Zero edits to brand-lock or series_lock.

**Audit a render** → check brand-lock.snapshot.md to see what version the storyboard was built against.

This is why guardrails-in-code beat guardrails-in-vibes. Each layer has one job. Changes are surgical. Outputs are reproducible.


---

## ARCHIVO: visual-prompt-forge/tools/README.md

# Tools

Python helpers that keep the repo honest, gate a real project's output, and render previews
without invoking Claude.

## Requirements

```bash
pip install pyyaml jsonschema
```

Standard library otherwise. No pandas, no numpy.

## Run everything

```bash
./tools/check.sh            # every check, with output
./tools/check.sh --quiet    # pass/fail lines only
PYTHON=python3.12 ./tools/check.sh
```

This is exactly what CI runs, so a green local run means a green PR.

Every validator below also ships a `--selftest` that constructs failing fixtures and fails if
the check does not catch them. A validator that silently stops catching things is worse than
no validator, and the selftests are how that gets noticed.

## Repo checks

### `validate_skills.py`

Checks every `SKILL.md` in `skills/` has the required YAML frontmatter, a `name` that matches
its directory and a substantive `description`.

```bash
python tools/validate_skills.py
```

### `validate_schemas.py`

Checks every `*.schema.json` file is itself valid JSON Schema (Draft 2020-12) and carries
`$id`, `title`, and `description`.

```bash
python tools/validate_schemas.py
```

It validates schemas, not instances. For instances, see `validate_shots.py`.

### `validate_capabilities.py`

Checks the generator capability matrix
(`skills/visual-prompt-forge/adapters/_capabilities.json`) against
`capabilities.schema.json`, then checks it against the adapter prose that defers to it:

- every generator id has an adapter `.md` and every adapter `.md` has an entry
- no adapter advertises more words than its own `max_prompt_words` ceiling
- every adapter documents the `aspect_param` the matrix says to send
- no `notes` field cites a word count above its own ceiling
- warns when the matrix or an entry is past its 120-day freshness window

```bash
python tools/validate_capabilities.py
python tools/validate_capabilities.py --selftest
```

The prose checks exist because the matrix and the adapters had drifted in three places while
every file repeated the rule that the JSON wins.

### `validate_brand_lock.py`

Checks a brand-lock has all required sections and Identity fields, that its palette declares
the five roles the HTML preview maps onto CSS variables, and that its fonts are in the
backticked form the tools read.

```bash
python tools/validate_brand_lock.py brand-packs/whystrohm.md
python tools/validate_brand_lock.py --require-configured brand-packs/whystrohm.md
python tools/validate_brand_lock.py --snapshot output/brand-lock.snapshot.md
python tools/validate_brand_lock.py --snapshots     # every snapshot in the repo
python tools/validate_brand_lock.py --selftest
```

A brand-pack may be an unfilled template; that is what a template is. A snapshot may not, and
`--snapshot` additionally requires the `<!-- snapshot taken: ... -->` and
`<!-- source: ... -->` header, with a full UTC instant preferred over a bare date.

## Project checks

These run against a project's output directory, not the repo.

### `validate_shots.py`

Validates `shots.json` and `text-overlays.json` as instances, plus every cross-field and
cross-file rule JSON Schema cannot express: `end` after `start`, no gaps or overlaps, span
matching `project.duration_s`, overlay references resolving in both directions, every overlay
reachable from some shot, overlay timing inside its shot window, and every overlay color
present in the brand-lock palette.

```bash
python tools/validate_shots.py output/
python tools/validate_shots.py path/to/shots.json
python tools/validate_shots.py --examples     # every bundled example
python tools/validate_shots.py --selftest
```

Warnings cover the judgement calls: overlay copy repeated in a shot subject, a raw hex in a
subject, shot ids out of chronological order, a font the brand-lock does not declare.

### `validate_prompts.py`

Validates the prompt files `visual-prompt-forge` writes, against `shots.json` and the
capability matrix. Header completeness, generator id, aspect agreement, the
`max_prompt_words` ceiling, shot coverage, duplicate blocks, and the forge's two hard
rules: no on-screen text copy inside a prompt, and `environment` / `lighting` /
`color_grade` appearing verbatim.

```bash
python tools/validate_prompts.py output/
python tools/validate_prompts.py output/prompts/round-1/flux.txt
python tools/validate_prompts.py --examples
python tools/validate_prompts.py --selftest
```

The verbatim check is the reason this file exists. Series consistency depends on the
series_lock anchors landing unedited in every prompt, and that is the single easiest rule
in the kit to break, because paraphrasing an anchor is what writing good prose feels like.
A careful authoring pass over a seven-shot storyboard drifted on it seven times out of
seven with every other validator green, and so did the worked-run fixture in this repo.

The character anchor is a warning rather than an error: a shot with no person in it can
legitimately omit it, and the message says so, so you can confirm rather than guess.

### `validate_critique.py`

Validates a critique against `critique.schema.json` **and** the two invariants the schema
cannot hold.

The gate: any `blocking` issue forces `REJECT`, three or more `major` issues force `REJECT`,
one or two `major` forbid `ACCEPT`.

The provenance rules, from schema version `1.1`: a hash without its path is not a reference,
`image_ref` may not be null, `HIGH` confidence requires the shot, brand-lock, and prompt all
to be identified, and a named generator has to exist in the capability matrix.

```bash
python tools/validate_critique.py output/critiques/round-1/shot_03.critique.json
python tools/validate_critique.py output/          # every critique in the tree
python tools/validate_critique.py --examples
python tools/validate_critique.py --selftest
```

Version `1.0` critiques still pass, with a warning: they carry a verdict and no way to tie it
to the bytes it reviewed.

### `validate_provenance.py`

Walks an output tree and recomputes every recorded hash. This is the tool that answers "does
this verdict still describe the file it reviewed."

```bash
python tools/validate_provenance.py output/
python tools/validate_provenance.py output/ --require-accept
python tools/validate_provenance.py output/ --json
python tools/validate_provenance.py --selftest
```

It catches, with a selftest for each:

- a frame regenerated after its critique (`image_sha256` no longer matches)
- a brand-lock edited mid-project (`brand_lock_sha256` no longer matches `run.json`)
- a frame on disk with no critique for its round, never reviewed at all
- two critiques for the same shot in the same round, two operators colliding
- rounds that skip a number, or a critique whose `run_id` belongs to another run

`--require-accept` makes it the pipeline stop condition: exit 0 only when the chain is intact
*and* every shot's latest verdict is ACCEPT.

## Rendering

### `shots-to-html.py`

Renders an output folder into a single `preview.html`.

```bash
python tools/shots-to-html.py output/
python tools/shots-to-html.py output/ --inline-images
python tools/shots-to-html.py output/ --out review.html
python tools/shots-to-html.py output/ --rendered-at 2026-07-30T00:00:00Z
python tools/shots-to-html.py --selftest
```

It renders `skills/storyboard-html-preview/templates/preview.html.tpl`, the same structural
template the skill uses, through the small engine in `_template.py`. It did not always: the
CLI used to build its HTML inline while claiming to share the template, so the two could and
did diverge.

Everything interpolated is HTML-escaped. Shot subjects and rationales are model-generated
prose, and one angle bracket used to be enough to break the page.

`--rendered-at` pins the render timestamp, which makes output reproducible. CI re-renders
every bundled preview with a pinned value and fails if a byte moves.

The page shows two dates, deliberately: the **run** date from `run.json`, and the **render**
date. A single "Generated" date meant re-rendering a preview restamped the run as today.

### `copy-prompt.py`

Pipes one shot's prompt to the clipboard so you can paste into a generator UI without hunting
through the file.

```bash
python tools/copy-prompt.py output/prompts/round-1/flux.txt
python tools/copy-prompt.py output/prompts/round-2/revised-flux.txt --shot shot_02
python tools/copy-prompt.py output/prompts/round-1/flux.txt --list
python tools/copy-prompt.py --selftest
```

Reads both file shapes the forge writes. Comment lines inside a shot block are annotations and
never land in the clipboard, so a revision file's `# fix [...]` notes are shown but not
copied. Revision files used to be unreadable to this tool entirely, which was awkward given
they are the files an operator pastes from most.

Pure standard library. `pbcopy` on macOS, `xclip` or `xsel` on Linux, `clip` on Windows.

## Internal modules

Not entry points. Imported by the tools above.

- `_shotkit.py`, hashing, run ids, brand-lock parsing, and the output-tree path conventions.
  One copy, so no two tools can disagree about what a palette or a frame path is.
- `_template.py`, the template engine: `{{var}}`, `{{{raw}}}`, `{{#each}}`, `{{#if}}`. Only
  the subset `preview.html.tpl` uses, deliberately.

## Adding new tools

- Make it executable (`chmod +x`)
- Add a usage docstring at the top of the file
- Give it a `--selftest` that proves the check fires
- Document it in this README
- Wire it into `tools/check.sh`, which is what CI calls

Keep tools dependency-light. PyYAML, jsonschema, and the standard library are the baseline.

