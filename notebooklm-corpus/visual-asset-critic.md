# SKILL: visual-asset-critic

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: visual-asset-critic/SKILL.md

---
name: visual-asset-critic
description: Critique a generated image against its source storyboard shot and prompt, producing revision notes. Use when the user has generated an image and wants feedback before committing. Triggers on "does this match the brief", "review this render", "is this on-brand", "what should I change", or uploading an image alongside a shot ID. The QA loop for AI visuals. Works even without a storyboard-architect run. Pairs with storyboard-architect upstream, visual-prompt-forge sibling.
---

# Visual Asset Critic

You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structured review pass that catches what a tired creator misses.

The output is a critique with concrete, actionable revision notes. Not vibes. Not "looks good." Specific, prompt-level or post-level fixes.

## When to use

Trigger when the user:

- Uploads or links a generated image with a question about quality
- Asks "does this match the storyboard"
- Says "review this render", "is this on-brand", "what should I change"
- Has a generated image and a `shots.json` shot reference and wants QA
- Has a generated image and just wants editorial feedback (no storyboard reference)

## What you produce

**Two artifacts from every review, always both:** a human-readable markdown critique (the primary surface) and a machine-readable critique JSON (so a pipeline can gate on the verdict instead of parsing prose). The JSON is detailed in Step 6; it never replaces the markdown.

The JSON goes to `output/critiques/round-{N}/{shot_id}.critique.json`. One file per shot
per round, never a shared filename. A 12-shot project reviewed over three rounds writes 36
critiques; when they all went to `output/critique.json` it kept one, and which one depended
on review order.

The markdown critique uses these sections:

```
## Verdict
ACCEPT / REVISE / REJECT, one line

## What's working
2–4 specific positives. Concrete observations, not flattery.

## What's not working
2–5 specific issues. Each one cites a layer. Brand Lock, Series Lock, Shot Spec, Composition, Technical, or Continuity.

## Revision plan
For each issue, the fix:
- Prompt-level (re-roll with this change to the prompt)
- Post-level (acceptable to address in editing/compositing)
- Re-roll required (no prompt fix; budget 2–3 attempts)

## Confidence
HIGH / MEDIUM / LOW, how sure you are about the verdict
```

## Inputs

You need:

| Input | Required? | Default if absent |
|---|---|---|
| The generated image | Yes | Cannot critique without it |
| Shot ID + shots.json | Recommended | If absent, ask for shot intent in a sentence |
| brand-lock.snapshot.md | Recommended | If absent, critique only on technical merits |
| The original prompt used | Helpful | If absent, infer from intent |

If only the image is provided with no context, ask for one piece of information: **what was this shot supposed to be?** A single sentence is enough to anchor the critique.

## Workflow

### Step 1. Establish intent

What was this shot supposed to do? Pull from:

- Shot's `rationale` field (if shots.json provided)
- Shot's `subject`, `framing`, `angle`, `motion` fields
- User's stated intent (if no shots.json)
- The beat this shot serves

If you can't establish intent in one sentence, ask. Don't critique blind.

### Step 2. Critique by layer

Read `references/critique-rubric.md` for the full rubric. Quick version, check the image against:

1. **Brand Lock**, does it respect palette, mood, "never" list?
2. **Series Lock**, does it match character/environment/lighting anchors?
3. **Shot Spec**, does framing/angle/composition match the spec?
4. **Composition**, does it reserve space for on-screen text if applicable?
5. **Technical**, skin texture, hands, eyes, anatomy, AI artifacts?
6. **Continuity**, if previous shots in the series are available, does it match?

For each layer, note: pass / soft fail / hard fail. The verdict aggregates these.

### Step 3. Map issues to fixes

For every "not working" point, the critique must say what to do about it. Three buckets:

**Prompt-level fix**, change the prompt and re-roll. Specify the exact change:
> "The character has brown hair instead of salt-and-pepper. Add 'salt-and-pepper hair' verbatim from series_lock to the prompt, it's missing in the current prompt."

**Post-level fix**, acceptable to address in compositing. Specify what:
> "Color grade is slightly cool, push warmth +5 in post, no need to re-generate."

**Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts:
> "Hands are mangled. This is a known Flux failure mode; re-roll 2–3 times with same prompt and pick the best."

### Step 4. Verdict

| Verdict | When |
|---|---|
| ACCEPT | All layers pass or soft-fail in ways post can fix |
| REVISE | One or two layers hard-fail; clear fix path |
| REJECT | Three+ layers fail or one critical layer (Brand Lock, Series Lock) hard-fails with no clear fix |

### Step 5. Confidence

Be honest about uncertainty:

| Confidence | When |
|---|---|
| HIGH | Storyboard reference + brand-lock + prompt all available, clear assessment |
| MEDIUM | Some references missing but core intent is clear |
| LOW | Only the image, intent is inferred; verdict is your best guess |

HIGH is a factual claim about what you had, not a mood. `tools/validate_critique.py`
rejects a `1.1` critique that claims HIGH while `shot_id`, `brand_lock_ref`, or
`prompt_ref` is null, because that combination says the three inputs HIGH depends on were
not there.

### Step 6. Emit structured output (critique JSON)

After writing the markdown critique, **also** write
`output/critiques/round-{N}/{shot_id}.critique.json` conforming to
`templates/critique.schema.json` at version `1.1`. Same review, two surfaces. The markdown
is for the human; the JSON is so an automated QA loop (e.g. `visual-prompt-forge` revision
mode) can act on the verdict without parsing prose.

**Map the markdown to the schema, section for section:**

| Markdown | JSON field |
|---|---|
| `## Verdict` | `verdict` (`ACCEPT` / `REVISE` / `REJECT`) |
| `## What's working` bullets | `working[]` (one string each) |
| `## What's not working` + `## Revision plan` | `issues[]`, merge them: each issue carries its layer/note from "what's not working" and its `fix_type`/`fix` from the matching revision-plan line |
| `## Confidence` | `confidence` (`HIGH` / `MEDIUM` / `LOW`) |

**Provenance, all of it required at 1.1.** A verdict is a claim about specific bytes. Name
them, and hash them:

| Field | Value |
|---|---|
| `run_id`, `round` | from `run.json` and the round directory you are writing into |
| `created_at` | UTC instant, `YYYY-MM-DDThh:mm:ssZ` |
| `shot_id` | the shot, or `null` for a standalone image with no storyboard |
| `image_ref`, `image_sha256` | the frame you reviewed, and its SHA-256 |
| `prompt_ref`, `prompt_sha256` | the prompt file it came from, and its SHA-256 |
| `brand_lock_ref`, `brand_lock_sha256` | the snapshot you judged against, and its SHA-256 |
| `generator`, `model_version` | the generator id from `_capabilities.json`, and its model version |
| `seed` | if the generator exposes one, else `null` |

```bash
shasum -a 256 output/frames/round-1/shot_03.png \
              output/prompts/round-1/flux.txt \
              output/brand-lock.snapshot.md
```

Every one of those fields is required, and every one is nullable. That combination is
deliberate: `null` records that an input genuinely was not available, while a missing field
records nothing at all. If you did not have the prompt, write `prompt_ref: null` and drop
your confidence to MEDIUM. Do not omit the key.

The hashes are the point. Without `image_sha256`, a frame regenerated after this review
still satisfies `image_ref`, and a stale ACCEPT sails through the gate attached to a file
nobody looked at.

**Severity, assign one per issue.** This is the field the gate runs on, so map it from the layer rubric deterministically:

| Severity | Means | Maps from |
|---|---|---|
| `minor` | soft-fail, fixable in post | a soft-fail on any layer; `fix_type: post-level` |
| `major` | hard-fail **with** a clear fix path | a hard-fail that a prompt change or re-roll fixes |
| `blocking` | hard-fail on a critical layer (Brand Lock / Series Lock) with **no** clear fix, or a defect that makes the asset unusable | an unrecoverable hard-fail |

**Gating rule, the verdict is derived from severities, not chosen freely.** This guarantees the markdown verdict and the JSON verdict always agree:

- Any `blocking` issue ⇒ verdict is `REJECT`.
- Three or more `major` issues ⇒ verdict is `REJECT`.
- One or two `major` issues (and no blocking) ⇒ verdict is `REVISE`.
- Only `minor` issues, or none ⇒ verdict is `ACCEPT` (with post notes).

The three-major rule used to read "escalate to REJECT at your discretion." Discretion in a
gate is not a gate, and it disagreed with `references/critique-rubric.md`, which called
three hard fails a REJECT outright. It is now a threshold, and the validator enforces it.

Pick the markdown `## Verdict` by this same rule.

### Step 7. Run the gate

Writing a schema-valid critique is not the same as passing the gate. Run it:

```bash
python tools/validate_critique.py output/critiques/round-1/shot_03.critique.json
```

Or check the whole tree at once, which also recomputes every hash against the files on
disk:

```bash
python tools/validate_provenance.py output/
```

This step is not optional and it is not someone else's job. A critique that says `ACCEPT`
while carrying a `major` issue is a bug, and the only reason to write a validator for that
bug is to actually run it. Before this step existed, the gate ran in CI against two
fixtures that ship in the repo and never once against a real client's critique.

Worked examples: `examples/critique.accept.json` and `examples/critique.revise.json` show
the shape at version `1.0`, which is still valid and carries no provenance.
`examples/worked-run/critiques/` shows version `1.1` with real hashes, two shots across two
rounds.

## Hard rules

### Rule 1. No vibes-based critique

"Looks great" / "feels off" without specifics is not a critique. Every observation must reference something in the image (composition, color, anatomy, lighting direction, etc.).

### Rule 2. Prompt-level fixes must be specific

"Change the prompt" is not a fix. "Add 'salt-and-pepper hair' to the character anchor, it's currently missing" is a fix.

### Rule 3. Don't critique what wasn't asked

If the brief was "founder at laptop, calm mood" and the generation delivered exactly that, don't note that "the room could be more visually interesting." That's scope creep, not critique.

### Rule 4. Be honest about generator limits

Some failures (mangled hands, weird eye reflections, jewelry shimmer) are known generator weaknesses. Surface them as such, don't pretend a different prompt will fix them. Recommend re-roll or post.

### Rule 5. When in doubt, ACCEPT and recommend post

Generation is one stage in a pipeline. If the image is 80% right and the gap is fixable in post, that's an ACCEPT with post notes. Don't send the user back to re-generate when an editor would handle it in 90 seconds.

## Reference

- `references/critique-rubric.md`, the full layer-by-layer rubric

## Example output

> ## Verdict
> REVISE
>
> ## What's working
> - Composition correctly reserves the right two-thirds for text overlay (matches shot_03 rationale)
> - Lighting direction matches series_lock (window-left, warm afternoon)
> - Mood reads as calm/considered, on-brand
>
> ## What's not working
> - **Series Lock, character mismatch.** The character has brown hair, but series_lock specifies "salt-and-pepper." This is a verbatim-anchor failure.
> - **Technical, left hand.** Hand on the laptop has six fingers (Flux known failure mode).
> - **Shot Spec, framing.** Generated as MS but spec called for MCU. Subject is too small in frame.
>
> ## Revision plan
> - **Hair:** Prompt-level. Add "salt-and-pepper hair" to the character anchor in the prompt, currently missing. Re-roll.
> - **Hand:** Re-roll required. Generate 2–3 more times with same prompt and pick a clean one.
> - **Framing:** Prompt-level. Change "medium shot" to "medium close-up" in the prompt. Re-roll.
>
> ## Confidence
> HIGH

## Handoff

After delivering the critique, if the verdict is REVISE, offer:

> "Want me to draft the revised prompt? Point `visual-prompt-forge` at this output tree in
> revision mode and it will re-emit prompts for just the shots that need them."

If the verdict is REJECT, do not offer that. REJECT means a blocking issue or three or more
major ones, which is a failure with no clear fix path, and revision mode is built to stop
there and ask. Say what blocked it and what decision it needs: a changed shot spec, a
changed brand-lock, or a different generator.

Don't auto-revise. The user picks. The critique you just wrote is exactly what closes that
loop.


---

## ARCHIVO: visual-asset-critic/examples/worked-run/brand-lock.snapshot.md

<!-- snapshot taken: 2026-05-07T14:23:00Z -->
<!-- source: brand-packs/whystrohm.md -->

# Brand Lock: WhyStrohm

## Identity

**Brand:** WhyStrohm
**One-line description:** Managed content infrastructure for founder-led brands. Voice extraction, brand guardrails encoded in code, programmatic video, automated publishing. 30 minutes a week of founder time, 48-hour content cycles.
**Archetype:** Operator
**Voice posture:** Calm, considered, confident without shouting

## Palette

| Role | Hex | Use |
|---|---|---|
| Background | `#F5F0E8` | Cream, primary canvas |
| Ink | `#2A2A32` | Near-black, primary text and dark elements |
| Accent (warm) | `#D94F3A` | Coral, emphasis, periods on signature beats |
| Accent (cool) | `#C9BBE0` | Pale lavender, secondary highlights |
| Muted | `#7A7580` | Secondary text, captions |
| Rule | `#E8E1D4` | Subtle borders, dividers, card backgrounds |

## Typography

**Display font:** `Inter Black 900`, headline weight, hooks, on-screen text
**Body font:** `Inter Medium 500`, body copy, captions, UI
**Mono font:** `JetBrains Mono Regular`, code, data, technical references

## Mood adjectives

- operator (not creator)
- considered (not reactive)
- deterministic (not vibes-based)
- confident (without volume)
- defense-grade (not fragile)

## Never list

- never use stock photo aesthetic
- never use AI uncanny faces
- never over-saturate the cream background
- never use coral as a flood color (only as accent or signature periods)
- never use em dashes in copy
- never use emojis in body copy
- never use bullet points in narrative copy
- never use clip-art or generic icon sets
- never use hype words ("game-changing", "revolutionary", "next-level", "comprehensive")
- never use exclamation points in headlines
- never default to dark mode, light mode hybrid is the brand
- never animate text with bouncing or wobbling, type-on, fade, or hard cut only

## Aspect ratios

- 9:16, primary for short-form social
- 16:9, long-form, hero films, web embeds
- 1:1, feed posts, podcast covers
- 4:5. Instagram feed alternative

## Color grade direction

Warm filmic, muted teal shadows. Slight grain. Cream highlights, deep navy/charcoal shadows, never crushed. Reminiscent of Kodak Portra 400 with a slight digital cleanup.

## Motion language

Camera moves are minimal and deliberate. Default to static. When motion is used, slow push or slow pull only. Cuts on action, not on time. Type-on for emphasis, never bouncing or wobbling. Coral periods animate as a hard pop on signature beats. Transitions are hard cuts or 6-frame dissolves only.

## Voice rules

- no em dashes
- no emojis in body copy
- no exclamation points in headlines
- no hype words
- prefer specific numbers over vague claims
- prefer present-tense over future-tense
- prefer "operator" over "creator", "infrastructure" over "agency"

---

**Last updated:** 2026-05-07
**Owner:** Yuri Strohm
**Version:** 1.0


---

## ARCHIVO: visual-asset-critic/references/critique-rubric.md

# Critique Rubric

The structured layer-by-layer pass. Use this as the checklist when reviewing a generated image.

## Layer 1. Brand Lock check

| Check | Pass | Soft fail | Hard fail |
|---|---|---|---|
| Palette | Image colors come from brand-lock palette | Colors close but slightly off | Colors not in palette at all |
| Mood adjectives | Image reads as the brand mood | Mood reads as adjacent (e.g. "calm" vs "neutral") | Image reads as a different mood (e.g. "energetic" when brief was "calm") |
| "Never" list | None of the items in the never list are present | One item in the never list shows softly | Multiple never-list violations |
| Aspect ratio | Matches `project.aspect` | Within a crop of the spec | Wrong aspect |

Hard fail on Brand Lock = REJECT or REVISE depending on whether prompt fix exists.

## Layer 2. Series Lock check

| Check | Pass | Soft fail | Hard fail |
|---|---|---|---|
| Character anchor | All described features visible | One minor feature off (e.g. wrong shirt color) | Wrong person (different age/race/build than anchor) |
| Environment | Matches series_lock | Slight environment drift | Different environment entirely |
| Lighting direction | Matches series_lock | Lighting is right but slightly different angle | Lighting from wrong direction (continuity break) |
| Color grade | Matches series_lock | Slight tonal drift | Different color grade |

Hard fail on Series Lock = REJECT (continuity break) or REVISE if specific fix available.

## Layer 3. Shot Spec check

| Check | Pass | Soft fail | Hard fail |
|---|---|---|---|
| Framing | Matches spec (ECU/CU/MS/etc.) | One step off (e.g. MS instead of MCU) | Two+ steps off |
| Angle | Matches spec | Slight angle variation | Wrong angle (low when spec was eye-level) |
| Subject action | Matches `subject` description | Subject doing similar but slightly different action | Subject doing wrong action |
| Depth of field | Matches if specified | Slight DOF variation | Deep when shallow was specified |

Soft fail = post-level fix or accept. Hard fail = revise.

## Layer 4. Composition check

| Check | Pass | Soft fail | Hard fail |
|---|---|---|---|
| Negative space for text | Reserved per spec | Reserved but tight | No reserved space, overlay won't fit |
| Subject placement | Matches rationale | Slightly off (subject in left-third vs right-third) | Subject blocks where text was meant to go |
| Eye-line | Looks where intended | Slight gaze direction off | Looking the wrong way |
| Headroom | Appropriate | Slightly tight or loose | Cropped at hairline / huge headroom |

Composition fails are usually prompt-level fixable. Re-roll with explicit composition language.

## Layer 5. Technical check

| Check | Pass | Soft fail | Hard fail |
|---|---|---|---|
| Hands | Anatomically correct | Slight finger weirdness | Six fingers, fused fingers, wrong joints |
| Eyes | Symmetrical, focused | Slight asymmetry | Wonky eyes, wrong reflections |
| Skin texture | Natural | Slightly plastic | Heavy AI plastic |
| Anatomy | Correct | Minor weirdness | Major anatomy errors |
| Background artifacts | Clean | Minor weirdness | Distorted text, melted objects, impossible geometry |

Technical hard fails are almost always **re-roll required**. The prompt was probably fine; the generator just produced a bad sample. Budget 2–3 re-rolls.

## Layer 6. Continuity check (if previous shots available)

| Check | Pass | Soft fail | Hard fail |
|---|---|---|---|
| Character match | Same person, same look | Slight drift | Clearly different person |
| Lighting continuity | Same direction, time of day | Subtle shift | Direction reversed, time of day jumped |
| Environment continuity | Same space | Slight environment drift | Different space |
| Color grade match | Identical | Subtle shift | Visibly different |

Continuity hard fails break the storyboard. REVISE with verbatim-anchor checks on the prompt.

## From pass/fail to severity

The tables above grade each check as pass, soft fail, or hard fail. The JSON critique
records a severity instead, and the verdict is derived from those severities. Map them
this way, and only this way:

| Rubric result | Severity | Why |
|---|---|---|
| Soft fail on any layer | `minor` | Post can absorb it. `fix_type` is usually `post-level` |
| Hard fail **with** a clear fix path | `major` | A prompt change or a re-roll resolves it |
| Hard fail on Brand Lock or Series Lock **with no** fix path | `blocking` | Nothing downstream recovers this |
| Any defect that makes the asset unusable | `blocking` | Same, regardless of layer |

## Aggregating verdict

The verdict follows from the severities. It is not a separate judgement:

| Severities present | Verdict |
|---|---|
| any `blocking` | REJECT |
| three or more `major` | REJECT |
| one or two `major` | REVISE |
| only `minor`, or none | ACCEPT (with post notes) |

`tools/validate_critique.py` enforces exactly this table, so a critique that disagrees with
it fails rather than shipping. Earlier versions of this file counted hard fails and called
3+ a REJECT while the skill said "escalate at your discretion." Those two rules disagreed,
and the disagreement is the reason the threshold is now a number.

Soft fails are noted but don't change the verdict on their own. If you have three or more of
them, look again: a cluster of soft fails usually means one of them is really a hard fail
you talked yourself out of.

## Speed bumps to remember

- **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
- **Don't pile-on once verdict is set**, if you're rejecting, list the issues that drive the rejection; don't list every cosmetic concern
- **Be specific, always**, "lighting is off" is not a critique; "key light is camera-right but series_lock says camera-left" is
- **Cite the layer**, every issue gets tagged with which layer it falls under. This makes the fix path obvious
- **Distinguish prompt failure from generator failure**, if the prompt was fine and the generator produced garbage hands, that's "re-roll required", not "fix the prompt"


---

## ARCHIVO: visual-asset-critic/tools/README.md

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

