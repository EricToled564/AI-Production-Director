# SKILL: storyboard-architect

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: storyboard-architect/SKILL.md

---
name: storyboard-architect
description: Turn a creative brief into a production-grade storyboard with shot specs, timing, on-screen text, and per-shot rationale. Use when the user describes a video brief, plans a video, references shots or beats, scripts a social video, or hands over a creative concept to break into scenes. Produces run.json, storyboard.md, shots.json, text-overlays.json, and brand-lock.snapshot.md. Pairs with visual-prompt-forge, visual-asset-critic, storyboard-html-preview.
---

# Storyboard Architect

You are turning a creative brief into a deterministic storyboard. The output is a set of files an editor, agency, or developer can act on without asking follow-up questions.

This is not a creative-writing exercise. The output is a spec.

## When to use

Trigger this skill when the user:

- Describes a video they want to make ("30-second explainer for...", "TikTok ad about...")
- Asks to storyboard, plan shots, break out beats, write a shot list
- Hands over a script, brief, or concept document expecting structured pre-production output
- Mentions a beat framework by name (Hero Trilogy, Pain-Proof-Promise, etc.)
- References an existing brand-lock file or pack

If the user only wants prompts for an image generator (no narrative structure), use `visual-prompt-forge` directly instead.

## What you produce

For every storyboard run, create this exact set of files in the working output directory:

```
output/
├── run.json                   # Run identity + every input pinned by content hash
├── storyboard.md              # Human-readable, structured per shot
├── shots.json                 # Machine-readable, schema in templates/shots.schema.json
├── text-overlays.json         # On-screen text + timing
└── brand-lock.snapshot.md     # Frozen copy of the brand-lock used (audit trail)
```

`run.json` is what makes the rest of the tree auditable later. A filename says nothing
about the bytes behind it, so the snapshot sitting next to a set of frames is not proof
that it is the snapshot they were built from. The hashes in `run.json` are that proof.
Write it once, at the end of the run, and never edit it.

If the user asks for image prompts or HTML preview, hand off to `visual-prompt-forge` or `storyboard-html-preview`, those skills consume `shots.json` directly. Don't try to do their job here.

## Inputs

You need these. If any are missing, ask before drafting.

| Input | Required? | Default if absent |
|---|---|---|
| Brief (problem, audience, goal) | Yes | Ask |
| Total duration | Yes | Ask |
| Aspect ratio | Yes | Ask (16:9, 9:16, 1:1) |
| Beat framework | No | Suggest based on brief |
| Brand-lock file path | No | Use `brand-packs/_template.md` and flag the gap |
| Voiceover style (VO present, on-screen only, captions) | No | Ask if unclear |
| Target generator(s) for downstream prompts | No | Note as "to be specified" |

## Workflow

Follow this sequence. Don't skip steps even if the brief seems simple.

### Step 1. Read the brand-lock

If a brand-lock file path is provided, read it first. Extract:

- Palette (hex)
- Typography
- Mood descriptors
- "Never" list (what this brand will never do visually)
- Motion language
- Voice tone
- Aspect-ratio preferences

If no brand-lock is provided, copy `brand-packs/_template.md` into the output as `brand-lock.snapshot.md` with a note: `# UNCONFIGURED, using template defaults. Recommend providing a real brand-lock for production work.`

### Step 2. Pick the beat framework

Read `references/beat-frameworks.md`. Pick the one that matches the brief. Common cases:

- Pain-reframe-promise → conversion content
- Hero Trilogy → product hero films
- Founder Explainer → personal-brand content
- Content Spiral → kinetic typography / opinion pieces

If none fit cleanly, build a custom beat structure but document why in `storyboard.md` rationale section.

### Step 3. Block out timing

Read `references/timing-rules.md` for the math. Default cadence:

- Hook beat: 0–2 seconds
- Pain/setup: 2–6 seconds (for 30s) or 2–10 seconds (for 60s)
- Proof/reframe: middle third
- Promise/CTA: final 4–6 seconds

Don't fight the framework. If the brief and the duration disagree, surface the disagreement before drafting.

### Step 4. Draft the shot list

Read `references/shot-grammar.md` for controlled vocabulary. The field names below are
the schema's field names. `templates/shots.schema.json` sets `additionalProperties:
false`, so a near-miss like `environment` instead of `environment_ref` is a validation
failure, not a synonym.

- `id`, sequential, zero-padded (`shot_01`, `shot_02`...)
- `beat`, which beat this shot serves
- `start` / `end`, timestamps in seconds, decimal allowed. `end` must be after `start`
- `framing`, ECU / CU / MCU / MS / MLS / WS / EWS
- `angle`, eye-level / high / low / overhead / dutch
- `motion`, static / push / pull / pan-left / pan-right / tilt-up / tilt-down /
  handheld / orbit / whip / rack. All eleven are legal; the schema enum is the
  authority and `references/shot-grammar.md` explains when each earns its keep
- `depth_of_field`, optional, shallow / deep / rack
- `subject`, what's in frame, structured
- `environment_ref`, references series-lock language, default `series_lock.environment`
- `lighting_ref`, references series-lock language, default `series_lock.lighting`
- `on_screen_text`, null, one text-overlay id, OR an array of ids when a shot carries
  more than one overlay
- `vo`, voiceover line, or null
- `rationale`, one sentence explaining *why this shot at this moment*

Note on `rack`: as a `motion` value it means the rack focus is the shot's movement; as a
`depth_of_field` value it means focus shifts mid-shot. Same word, two fields, two
meanings.

### Step 5. Separate the text layer

Every piece of on-screen text becomes an entry in `text-overlays.json`. Never bake text into the visual description. Each overlay has:

- `id`, `text_01`, `text_02`...
- `shot_id`, which shot this overlays on
- `content`, the actual text
- `font`, references brand-lock typography
- `position`, `center`, `lower-third`, `upper-third`, `left-third`, `right-third`, or `{x, y}` percentages
- `size`, `display`, `headline`, `body`, `caption`
- `weight`, `regular`, `medium`, `bold`, `black`
- `color`, hex (must come from brand-lock palette)
- `enter`, `{ at: seconds, animation: fade-in | slide-up | slide-down | type-on | hard-cut }`
- `exit`, `{ at: seconds, animation: fade-out | slide-up | slide-down | hard-cut }`

Enter and exit have different animation vocabularies, and `templates/text-overlays.schema.json`
is the authority on both. A shot may carry more than one overlay; list every id in that
shot's `on_screen_text` array, or the extra overlays render nowhere.

### Step 6. Lock the series

Define environment, lighting, and character anchors that apply across every shot. These go at the top of `shots.json` under `series_lock`. Without these, image generation will produce incoherent frames.

### Step 7. Write rationale

Every shot has a one-sentence rationale. Why this beat. Why this framing. Why this on-screen text. This is the audit trail. Do not skip it.

### Step 8. Snapshot the brand-lock

Copy the brand-lock file (or template) into the output as `brand-lock.snapshot.md`. Add
these two comments at the very top, in this order:

```
<!-- snapshot taken: 2026-05-07T14:23:00Z -->
<!-- source: brand-packs/whystrohm.md -->
```

The timestamp is a full UTC instant, `YYYY-MM-DDThh:mm:ssZ`. A bare date cannot
distinguish two runs made on the same day, which is the case that matters. The source is
the path it was copied from, or the literal string `template default` for an
unconfigured run. Extra comments after these two are fine.

`tools/validate_brand_lock.py --snapshot <path>` checks both lines. Run it.

### Step 9. Write run.json

Last step, after the other four files are final. Fill in
`templates/run.schema.json`: a `run_id`, the `created_at` instant, and the SHA-256 of
`shots.json`, `text-overlays.json`, and `brand-lock.snapshot.md` as written.

```bash
shasum -a 256 output/shots.json output/text-overlays.json output/brand-lock.snapshot.md
```

`run_id` is the compact UTC timestamp, a dash, then 8 hex characters, e.g.
`20260730T142300Z-9f2c1ab4`. The hex suffix is what keeps two operators starting a run
in the same second from colliding. Set `brand_lock_configured: false` when the snapshot
is an unfilled template.

Leave `rounds` empty. `visual-prompt-forge` appends a round entry when it writes
prompts.

## Output formats

### `storyboard.md`

Use the template at `templates/storyboard.md.tpl`. Read it before writing.

### `shots.json`

Must validate against `templates/shots.schema.json`. Read it before writing. The structure is:

```json
{
  "version": "1.2",
  "project": { "title": "...", "duration_s": 30, "aspect": "9:16", "framework": "..." },
  "brand_lock_ref": "brand-lock.snapshot.md",
  "series_lock": {
    "character": "...",
    "environment": "...",
    "lighting": "...",
    "color_grade": "..."
  },
  "shots": [
    {
      "id": "shot_01",
      "beat": "hook",
      "start": 0.0,
      "end": 2.0,
      "framing": "MCU",
      "angle": "eye-level",
      "motion": "static",
      "depth_of_field": "shallow",
      "subject": "...",
      "environment_ref": "series_lock.environment",
      "lighting_ref": "series_lock.lighting",
      "on_screen_text": "text_01",
      "vo": null,
      "rationale": "..."
    }
  ]
}
```

Write `1.2` for new storyboards. `1.0` and `1.1` files stay valid; the array form of
`on_screen_text` and the hashed `assets` block need `1.2`.

### `text-overlays.json`

Must validate against `templates/text-overlays.schema.json`. Read it before writing.

## Quality bar

Run the validator. Do not eyeball this list.

```bash
python tools/validate_shots.py output/
python tools/validate_brand_lock.py --snapshot output/brand-lock.snapshot.md
python tools/validate_provenance.py output/
```

`validate_shots.py` checks every mechanical rule that used to live here as a checkbox,
because a checkbox is a rule enforced by remembering to look:

- shots.json and text-overlays.json validate against their schemas
- `end` is after `start`, no duplicate ids, no gaps, no overlaps, and the covered span
  matches `project.duration_s` within 0.1s
- every `on_screen_text` resolves to an overlay, every `overlay.shot_id` resolves to a
  shot, and every overlay is reachable from at least one shot
- every overlay's timing sits inside its shot window, and exit is after enter
- every overlay color appears in the brand-lock palette
- `brand_lock_ref` resolves on disk

It warns, rather than fails, on judgement calls worth a second look: overlay copy
repeated inside a shot subject, a raw hex in a subject, shot ids out of chronological
order, an overlay font the brand-lock does not declare.

What the validator cannot check, and you still have to:

- [ ] Every rationale says *why this shot at this moment*, not what the shot contains
- [ ] `series_lock` anchors are specific enough to reproduce (not "a person in a room")
- [ ] The beat structure actually matches the brief's argument
- [ ] `run.json` is written and its hashes are the files as shipped

If the validator fails, fix it before declaring done. A green validator plus an unread
rationale is not a finished storyboard.

## Reference files

Load these as needed:

- `references/beat-frameworks.md`, the beat structures
- `references/shot-grammar.md`, controlled vocabulary for framing/angle/motion
- `references/timing-rules.md`, pacing math
- `references/on-screen-text.md`, when on-screen text earns its keep

## Examples

- `examples/30s-pain-proof-promise/`, full output set for a 30-second conversion ad
- `examples/60s-founder-explainer/`, full output set for a founder explainer
- `examples/shotkit-explainer/`, the 90-second explainer, including a shot that carries
  two overlays

Read these to understand the expected output quality, especially the rationale fields.
All three validate clean under `tools/validate_shots.py --examples`, so they are also
the reference for what a passing file looks like.

For what the output tree looks like after generation and review, see
`../visual-asset-critic/examples/worked-run/`: two shots through two rounds, with real
hashes, per-round prompts and frames, and one critique per shot per round.

## Handoff

After producing the five files, tell the user what's in `output/` and offer the obvious next steps:

- "Want image prompts? I'll run `visual-prompt-forge` on `shots.json`."
- "Want a shareable HTML preview? I'll run `storyboard-html-preview`."
- "Want to QA a generated image against this storyboard? I'll run `visual-asset-critic`."

Don't run those automatically. The user picks.


---

## ARCHIVO: storyboard-architect/brand-packs/README.md

# Brand Packs

A brand pack is a single Markdown file that locks in palette, typography, voice, and visual rules for a project. The skills in this pack consume it. Every storyboard, every prompt, every generated frame inherits from it.

## How to use

1. Copy `_template.md` to a new file (e.g. `acme.md`)
2. Fill in every field. No placeholders left behind.
3. Reference it from your storyboard requests:

   > "30-second founder explainer. Use `brand-packs/acme.md` as the brand lock."

4. The skill reads it, snapshots it into the output as `brand-lock.snapshot.md`, and applies it through the pipeline.

## How to write a good one

The template is a checklist, not a creative-writing exercise. Three rules:

**Be specific.** "Modern, clean, professional" is not a brand. "Calm, considered, operator energy, confident without shouting" is.

**Be exclusive.** The "never" list is more valuable than the "always" list. Listing what the brand will not do narrows the generator's space and produces tighter output.

**Be hex-precise.** Every color is a hex value. Every font is named. The skills consume structured data; vagueness here cascades into bad prompts later.

## Examples

The pack ships with two reference brand packs:

- **`whystrohm.md`** (flagship). The actual brand pack WhyStrohm uses on its own content. Real palette, real voice rules, real "never" list. Use this as the reference for the level of specificity production work requires.
- **`examples/saas-clean.md`**. B2B SaaS, restrained, professional. Light backgrounds, single accent. Inter type stack. A neutral counterpoint to the WhyStrohm flagship.

More example brand packs will land in v2.0.0. PRs welcome.

## Generating a brand pack from existing assets

Don't hand-author from scratch if the brand already exists. The **`brand-lock-extractor`** skill (ships in this repo at `skills/brand-lock-extractor/`) takes a website URL, a brand book PDF, screenshots, or a written description and produces a `brand-lock.md` in this exact format, with a confidence and source noted for every value:

> "Extract a brand-lock from acme.com" or "build a brand pack from this brand book PDF."

For bulk or programmatic extraction across many URLs, [media-tsunami](https://github.com/whystrohm/media-tsunami) (WhyStrohm's open-source brand voice extractor) scrapes URLs and produces a `brand-lock.md` in the same format.

## Versioning

Every storyboard run snapshots the brand pack it was built against. If you update `acme.md` later, previous storyboards still reference the version they were built on. This is intentional, the audit trail tells you exactly what brand state any given piece of content was built against.

When you make a brand-pack revision that materially changes look or voice, bump the `Version:` field at the bottom and note the change. e.g.:

```
Version: 1.1 (2026-05-12: switched accent from #D94F3A coral to #C44233 deeper coral)
```

## Contributing examples

PRs welcome for new brand-pack examples that fill gaps in the current set. Open an issue with the `brand-pack-request` template before submitting.


---

## ARCHIVO: storyboard-architect/brand-packs/_template.md

# Brand Lock: {{BRAND_NAME}}

> Replace placeholders. Delete this blockquote when you're done.
> Every field below feeds into the storyboard pipeline. Be specific.

## Identity

**Brand:** {{BRAND_NAME}}
**One-line description:** What this brand actually does, who for.
**Archetype:** Operator / Creator / Sage / Rebel / Caregiver / Other
**Voice posture:** Confident / Warm / Sharp / Quiet / Playful / Authoritative

## Palette

Every hex value here is allowed. Anything outside this list is not.

| Role | Hex | Use |
|---|---|---|
| Background | `#______` | Primary canvas |
| Ink | `#______` | Primary text, dark elements |
| Accent | `#______` | Highlights, CTAs, brand pop |
| Muted | `#______` | Secondary text, captions |
| Rule | `#______` | Borders, dividers, subtle UI |

Add more rows if the brand has more named colors. Don't add more than 8, past that, the brand stops being recognizable.

## Typography

**Display font:** `______`
**Body font:** `______`
**Mono font (optional):** `______`

Put the font name and weight in backticks immediately after the label, e.g.
`` **Display font:** `Inter Black 900`, headlines and hooks ``. The HTML preview and
the overlay-font check read that backticked value; anything before it is prose.

Two fonts max for production work. Three only if one is reserved for code/data.

## Mood adjectives

Pick 3–5. These flow into prompts as the brand's emotional posture.

- adjective_1
- adjective_2
- adjective_3

## Never list

What this brand never does, visually or tonally. Be specific.

- never use stock photo aesthetic
- never use AI uncanny faces
- never over-saturate
- never shout in copy
- never use clip-art icons
- (add more, the more specific, the better)

## Aspect ratios

Default: 16:9 / 9:16 / 1:1 / 4:5 / other

## Color grade direction

How footage and generated images should be graded. One sentence.

> e.g. "Warm filmic, muted teal shadows, slight grain. Reminiscent of Kodak Portra 400."

## Motion language

How motion behaves in this brand's content. One paragraph.

> e.g. "Camera moves are minimal and deliberate. Static or slow-push. Cuts on action, not on time. Type-on for emphasis, never bouncing or wobbling text."

## Voice rules

Copy-level rules that apply to VO and on-screen text.

- e.g. no em dashes
- no emojis in body copy
- no exclamation points in headlines
- no clichéd metaphors ("game-changing", "revolutionary", "next-level")
- no hype words

## Reference materials

Optional. Links to past work, mood boards, or style guides that further define the brand.

- Link to brand guide
- Link to past hero film
- Link to mood board

---

**Last updated:** YYYY-MM-DD
**Owner:** name / role
**Version:** 1.0


---

## ARCHIVO: storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md

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

## ARCHIVO: storyboard-architect/examples/30s-pain-proof-promise/storyboard.md

# WhyStrohm. The Content Infrastructure Pitch

| | |
|---|---|
| **Duration** | 30s |
| **Aspect** | 9:16 |
| **Beat framework** | Pain-Reframe-Promise |
| **Brand lock** | [`brand-lock.snapshot.md`](./brand-lock.snapshot.md) |
| **Generated** | 2026-05-07 14:23 UTC |

---

## Brief

A 30-second founder explainer aimed at founders running content marketing themselves. The audience knows their content output is uneven and they're tired of the treadmill. The reframe is the WhyStrohm thesis: it's not a content problem, it's an infrastructure problem. The promise is the offer, 30 min/week of founder time, 48-hour cycle. The CTA is the free /scan diagnostic.

## Beat framework: Pain-Reframe-Promise

Standard PRP for conversion content. Three beats with hook and CTA bookending.

- 0–2s. Hook
- 2–11s. Pain (extended for 30s, gives the problem space to breathe)
- 11–20s. Reframe + Proof (the WhyStrohm thesis lands, then is shown)
- 20–26s. Promise (specific, time-bound)
- 26–30s. CTA

## Series lock

| | |
|---|---|
| **Character anchor** | founder, mid-thirties, salt-and-pepper hair, navy crewneck, calm posture, working at laptop |
| **Environment** | minimalist home office, white walls, oak desk, single houseplant, no decor clutter |
| **Lighting** | soft natural side-light, large window camera-left, warm afternoon golden hour, gentle shadow rolloff |
| **Color grade** | warm filmic, muted teal shadows, slight grain, cream highlights, deep navy shadows never crushed |

---

## Shots

### shot_01 · 0.0–2.0s · MCU · static

**Beat:** hook

**Subject:** founder, mid-thirties, salt-and-pepper hair, navy crewneck, looking directly into camera, neutral expression, slightly tired

**On-screen text:** "Your content feels random." (Inter Black 900, lower-third, hard cut at 0.4s)

**Rationale:** Cold open, direct eye contact establishes parasocial trust. Static framing keeps the hook simple, text does the work.

---

### shot_02 · 2.0–7.0s · MS · static

**Beat:** pain

**Subject:** founder at laptop, scrolling social feed, content tiles glowing on screen, slight slump in shoulders, mug of coffee mid-distance

**On-screen text:** "Posting more isn't fixing it." (Inter Black 900, right-third, fade-in at 2.4s)

**Rationale:** High angle subtly diminishes the subject, pain beat. Deep DOF keeps the messy social feed legible. Subject left-weighted, text reserves right two-thirds.

---

### shot_03 · 7.0–11.0s · ECU · static

**Beat:** pain

**Subject:** close on founder's hand hovering over laptop trackpad, frozen, not moving

**On-screen text:** none

**Rationale:** Hand frozen above trackpad is the visual symbol of decision paralysis. Wordless beat, let the image carry the pain before the reframe.

---

### shot_04 · 11.0–16.0s · MCU · push

**Beat:** reframe

**Subject:** founder, same posture, looking at camera, expression shifts from tired to clear, small almost-smile

**On-screen text:** "You don't have a content problem. / You have an infrastructure problem." (Inter Black 900, coral, center, type-on at 11.5s)

**Rationale:** Slow push as the reframe lands. Same character, same environment, only the expression changes. The change is the point.

---

### shot_05 · 16.0–20.0s · MS · static

**Beat:** proof

**Subject:** founder gestures toward laptop screen, kanban-style content pipeline visible, organized columns, clean structure

**On-screen text:** "Voice extracted. Brand locked. System runs." (Inter Medium 500, upper-third, slide-up at 16.4s)

**Rationale:** Proof beat, show the system, not the result. The kanban metaphor is recognizable to operators. Subject right-weighted, text upper-third.

---

### shot_06 · 20.0–26.0s · MCU · static

**Beat:** promise

**Subject:** founder, calm composed posture, fully present, slight smile, hands folded on desk

**On-screen text:** "30 minutes a week. / 48-hour content cycles." (Inter Black 900, lower-third, type-on at 20.5s)

**Rationale:** Promise beat, the after-state is the same person, just calmer. Static frame holds the moment. Text carries the specific commitment.

---

### shot_07 · 26.0–30.0s · MS · static

**Beat:** cta

**Subject:** founder, neutral posture, room visible behind, calm presence, gentle eye contact with camera

**On-screen text:** "whystrohm.com/scan" (Inter Black 900, coral, lower-third, type-on at 26.4s)

**Rationale:** CTA beat. Pulled out to MS to give text the breathing room. Subject centered, text lower-third with URL. No motion, let it land.

---

## Handoff notes

- **For image generation:** run `visual-prompt-forge` against `shots.json`
- **For HTML preview:** run `storyboard-html-preview` against this folder
- **For QA on generated frames:** run `visual-asset-critic` with the generated image and the shot ID

## Audit trail

This storyboard was generated against `brand-lock.snapshot.md` (frozen at 2026-05-07T14:23:00Z, source `brand-packs/whystrohm.md`). If the brand-lock changes after this date, re-run to pick up the new state.


---

## ARCHIVO: storyboard-architect/examples/60s-founder-explainer/brand-lock.snapshot.md

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

## ARCHIVO: storyboard-architect/examples/60s-founder-explainer/storyboard.md

# WhyStrohm. How The System Actually Works

| | |
|---|---|
| **Duration** | 60s |
| **Aspect** | 9:16 |
| **Beat framework** | Founder Explainer |
| **Brand lock** | [`brand-lock.snapshot.md`](./brand-lock.snapshot.md) |
| **Generated** | 2026-05-07 14:31 UTC |

---

## Brief

A 60-second founder explainer for WhyStrohm. The audience is operators and founders who already know they need a content system but haven't seen the WhyStrohm thesis articulated. The narrative arc moves through five micro-beats: hook, stakes, insight, proof, and CTA. Voice carries the explanation; on-screen text reinforces the key turns.

## Beat framework: Founder Explainer

Five micro-beats:

- 0–2s. Hook (provocation)
- 2–14s. Stakes (why it matters)
- 14–32s. Insight (the actual point, extended for 60s to give the thesis room)
- 32–42s. Proof (the numbers)
- 42–60s. Insight wrap + CTA

## Series lock

| | |
|---|---|
| **Character anchor** | founder, mid-thirties, salt-and-pepper hair, navy crewneck, speaking directly to camera, calm authoritative posture |
| **Environment** | minimalist home office, white walls, oak desk, single houseplant, late afternoon |
| **Lighting** | soft natural side-light, large window camera-left, warm afternoon golden hour, gentle shadow rolloff |
| **Color grade** | warm filmic, muted teal shadows, slight grain, cream highlights, deep navy shadows never crushed |

---

## Shots

### shot_01 · 0.0–2.0s · MCU · static

**Beat:** hook · **VO:** "Most founders treat content like a hobby."
**Subject:** founder, looking directly into camera, slight knowing smile, mid-statement.
**On-screen text:** "Most founders treat content like a hobby." (lower-third, hard-cut)
**Rationale:** Hook is provocative but calm, voice carries the bite. Direct eye contact, MCU lock-in.

### shot_02 · 2.0–8.0s · MS · static

**Beat:** stakes · **VO:** "Then they wonder why every post feels like starting over. New idea, new angle, no compounding."
**Subject:** founder, gesturing slightly with one hand, explaining, eye contact maintained.
**Rationale:** Stakes beat. Pulled out to MS to let the gesture read. VO does the work, no on-screen text needed.

### shot_03 · 8.0–14.0s · ECU · static

**Beat:** stakes · **VO:** "It's not creativity. It's missing infrastructure."
**Subject:** close on founder's eyes, considered expression, slight head tilt.
**On-screen text:** "It's missing infrastructure." (coral, lower-third, type-on)
**Rationale:** ECU pulls the audience into the realization moment. Text reinforces the line that needs to land.

### shot_04 · 14.0–24.0s · MCU · push

**Beat:** insight · **VO:** "Every brand has a voice. Most founders never extract it. So every post starts from scratch."
**Subject:** founder, leaning slightly forward, more energy in delivery, hands resting on desk.
**Rationale:** Slow push as the thesis builds. VO is the load-bearing element here.

### shot_05 · 24.0–32.0s · MS · static

**Beat:** insight · **VO:** "Extract it once. Lock it in code. Now every post compounds."
**Subject:** founder gestures toward laptop screen, kanban content pipeline, voice extraction interface, brand-lock file open in editor.
**On-screen text:** "Extract. Lock. Compound." (upper-third, slide-up)
**Rationale:** Show the artifact. Text reinforces the three-step pattern. Deep DOF keeps the screen legible.

### shot_06 · 32.0–42.0s · MCU · static

**Beat:** proof · **VO:** "Hundreds of videos rendered from code. 48-hour content cycles. One operator."
**Subject:** founder, calm steady delivery, eye contact, hands folded.
**On-screen text:** "hundreds of videos · 48hr cycles · 1 operator" (upper-third, fade)
**Rationale:** Proof beat, concrete numbers. Stat callout lets viewer absorb visually while VO confirms.

### shot_07 · 42.0–50.0s · MS · pull

**Beat:** insight · **VO:** "Not because we work harder. Because the system runs."
**Subject:** founder, slight smile, settled into the explanation, room visible around him.
**Rationale:** Slow pull releases tension. The thesis lands. VO carries, text would dilute.

### shot_08 · 50.0–60.0s · MCU · static

**Beat:** cta · **VO:** "If this sounds like the version of content you actually want, run a free scan."
**Subject:** founder, calm, looks directly into camera one more time, almost-smile, settled.
**On-screen text:** "whystrohm.com/scan" (coral, lower-third, type-on)
**Rationale:** CTA beat. Static MCU brings it home. URL holds in lower-third for full read-twice duration.

---

## Handoff notes

- **For image generation:** run `visual-prompt-forge` against `shots.json`
- **For HTML preview:** run `storyboard-html-preview` against this folder
- **For QA:** run `visual-asset-critic` per shot

## Audit trail

Generated against `brand-lock.snapshot.md` (frozen at 2026-05-07T14:31:00Z, source `brand-packs/whystrohm.md`).


---

## ARCHIVO: storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md

<!-- snapshot taken: 2026-05-08T14:34:24Z -->
<!-- source: brand-packs/whystrohm.md -->
<!-- storyboard: shotkit-explainer -->

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

Two-font stack for production. Mono only for technical content.

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
- never use em dashes in copy (only periods, commas, semicolons)
- never use emojis in body copy
- never use bullet points in narrative copy
- never use clip-art or generic icon sets
- never use hype words ("game-changing", "revolutionary", "next-level", "comprehensive")
- never use exclamation points in headlines
- never default to dark mode, light mode hybrid is the brand
- never animate text with bouncing or wobbling, type-on, fade, or hard cut only
- never break the eye line between subject and the implied "operator perspective"

## Aspect ratios

- 9:16, primary for short-form social
- 16:9, long-form, hero films, web embeds
- 1:1, feed posts, podcast covers
- 4:5. Instagram feed alternative

## Color grade direction

Warm filmic, muted teal shadows. Slight grain. Cream highlights, deep navy/charcoal shadows, never crushed. Reminiscent of Kodak Portra 400 with a slight digital cleanup. Skin tones warm but not orange. Greens kept slightly desaturated to push focus to subject.

## Motion language

Camera moves are minimal and deliberate. Default to static. When motion is used, slow push or slow pull only. Cuts on action, not on time. Type-on for emphasis, never bouncing or wobbling. Coral periods animate as a hard pop on signature beats. Transitions are hard cuts or 6-frame dissolves only, no fancy wipes, no zooms.

For kinetic typography content (the Content Spiral pattern): pacing accelerates inward, each zoom 1.5–2x faster than the previous. Snap-back to wide claim is a hard cut.

## Voice rules

- no em dashes
- no emojis in body copy
- no exclamation points in headlines
- no hype words ("game-changing", "revolutionary", "comprehensive", "next-level", "leverage")
- no clichéd business metaphors ("move the needle", "drink the kool-aid", "low-hanging fruit")
- no qualifiers in declarative copy ("perhaps", "maybe", "kind of")
- prefer specific numbers over vague claims ("48 hours" not "fast", "30 minutes a week" not "a little time")
- prefer present-tense over future-tense
- prefer "operator" over "creator", "infrastructure" over "agency", "system" over "service"
- coral period (`.`) on signature lines is a typography choice, not punctuation, apply at end of hero phrases only

## Reference materials

- Site: https://whystrohm.com
- Brand voice extractor: https://github.com/whystrohm/media-tsunami
- Past hero films: see `/results` page
- Content Spiral pattern: documented in WhyStrohm production bible v3 (internal)

---

**Last updated:** 2026-05-07
**Owner:** Yuri Strohm
**Version:** 1.0


---

## ARCHIVO: storyboard-architect/examples/shotkit-explainer/storyboard.md

# shotkit. The Explainer.

**Project:** shotkit explainer film
**Duration:** 90 seconds
**Aspect:** 16:9 (1280x720 hero render, 1080x1920 vertical cut for socials)
**Framework:** founder-explainer
**Brand-lock:** [brand-lock.snapshot.md](./brand-lock.snapshot.md) snapshotted 2026-05-08T14:34:24Z
**Generated:** 2026-05-08

> This storyboard is the record of the v0.1.0 explainer film as it was actually rendered, so
> shot_05 still names seven adapters including Runway/Sora. Sora was discontinued and the
> motion lane moved to Kling, Veo, Seedance, and Hailuo. The storyboard is deliberately left
> matching the artifact it produced: editing it to describe a video that was never made is
> exactly the kind of drift this repo exists to prevent. See `CHANGELOG.md` for the adapter
> change.

## Brief

90-second explainer for shotkit. Targets founder-led brands at $500K to $5M ARR who run their own content and feel the prompt-engineering tax. Walks through the diagnosis (vague brief plus model-roulette equals brand drift), the methodology (five-layer prompt anatomy), the build moment (brief in, files out), the proof (rendered preview from a real shotkit run), and the install command. Lives at the top of the shotkit blog post on whystrohm.com.

## Series lock

| Field | Value |
|---|---|
| **Character** | No human subject. Typography-driven explainer with document-control aesthetic. |
| **Environment** | Operator-grade dashboard. Cream canvas, JetBrains Mono headers, Inter body, single coral accent per beat. |
| **Lighting** | Even diffuse. No shadow rolloff. Flat operator-doc grading throughout. |
| **Color grade** | Cream highlights (#F5F0E8), ink shadows (#2A2A32), coral (#D94F3A) reserved for signature beats. No saturation drift. |

## Shots

### shot_01: 0.0 to 12.0s. WS. eye-level. static.

**Beat:** pain. **Subject:** vague founder brief types into the left panel in JetBrains Mono. Cursor blinks. Then a chaos cut shows four image generators producing slightly off-brand outputs in a 2x2 grid. Each tile renders the same shot with a different palette, framing, font.
**On-screen text:** "You don't have a content problem. You have a pre-production problem." (Inter Black 900, center, fade)
**Rationale:** Cold open names the failure mode every founder recognizes. Vague brief plus model-roulette equals brand drift. The 2x2 grid does the work text cannot.

### shot_02: 12.0 to 30.0s. MS. eye-level. static.

**Beat:** reframe. **Subject:** Five horizontal layers stack from top to bottom. Each labeled in JetBrains Mono caps with 0.08em letter-spacing: brand lock, series lock, shot spec, text layer, generator adapter. Each layer slides in from below on a 6-frame stagger. Coral dot lands on brand lock as it appears.
**On-screen text:** "Five layers. Locked top to bottom." (Inter Black 900, upper-third, type-on)
**Rationale:** Architecture beat. The reader needs to see the layers exist before any claim about composability lands. Stack layout is the diagram doing the explanation.

### shot_03: 30.0 to 50.0s. MS. eye-level. push.

**Beat:** proof-1. **Subject:** Split panel. Left BRIEF column types out a brief slowly. Right OUTPUT column starts empty with a pulsing waiting dot, then file tree assembles row by row in JetBrains Mono Regular 16pt. storyboard.md, shots.json, text-overlays.json, brand-lock.snapshot.md, prompts/ directory with seven adapter files, preview.html. Coral dot lands on preview.html on completion.
**On-screen text:** "Brief in. Storyboard out. Audit trail included." (Inter Medium 500, upper-third, fade)
**Rationale:** The build moment is the centerpiece. Brief in, structured files out. Same animation language as the social demo so brand consistency reads across both surfaces.

### shot_04: 50.0 to 65.0s. MCU. eye-level. push.

**Beat:** proof-2. **Subject:** Coral wipe expands radially from the preview.html dot. Wipe reveals the rendered preview iframe scrolling vertically. The reader sees actual shot cards from the 30-second example pass through frame, including framing, angle, motion, color-grade rows. Subtle 10% vignette on edges.
**On-screen text:** "Files. Not panels. Not a SaaS dashboard." (Inter Black 900, lower-third, type-on)
**Rationale:** Reveal beat. The reader has now seen the methodology and the file outputs. The iframe shows the actual deliverable, not a mock.

### shot_05: 65.0 to 80.0s. MS. eye-level. static.

**Beat:** proof-3. **Subject:** Single shot description card sits center-frame. Seven generator adapter labels fan out radially around it. Midjourney, Flux, Ideogram, GPT Image, Nano Banana, Seedream, Runway/Sora. Lines connect center card to each adapter in 1px ink. Each adapter shows its prompt syntax appearing as a typewriter pass running simultaneously.
**On-screen text:** "One shot. Seven generators. One spec." (Inter Black 900, upper-third, fade)
**Rationale:** Cross-generator demonstration. Same shot description compiles to seven different prompt syntaxes simultaneously. The visual proves model-agnosticism is structural, not aspirational.

### shot_06: 80.0 to 90.0s. WS. eye-level. static.

**Beat:** promise. **Subject:** Full-frame typography. Install command appears via type-on in JetBrains Mono Regular at 22pt. Below it the project tagline in Inter italic 500 18pt, color muted. Coral period on the signature beat. Standard footer chrome holds.
**On-screen text:** "git clone github.com/whystrohm/shotkit / cd shotkit && ./install.sh" (JetBrains Mono, center, type-on) plus tagline "Pre-production for founder-led video at scale." (Inter italic 500, lower-third, fade).
**Rationale:** Promise beat. The viewer has the diagnosis, the architecture, the artifact, and the proof. The CTA is one paste-into-terminal command. No friction surface.

## Audit trail

- Brief, this document, scoped from the shotkit blog launch sequence.
- Brand-lock snapshotted from `brand-packs/whystrohm.md` on 2026-05-08.
- Shot list designed to compose with the existing ShotkitDemo composition (same chrome, complementary content, longer arc).
- Render shipped at [whystrohm.com/blog/you-dont-have-a-content-problem](https://whystrohm.com/blog/you-dont-have-a-content-problem) as the "we used shotkit to make this video" dogfood reveal.
- Landscape MP4 served from the blog: `/media/shotkit-explainer/shotkit-explainer.mp4`.


---

## ARCHIVO: storyboard-architect/references/beat-frameworks.md

# Beat Frameworks

Pick one. Don't invent a new one unless the brief genuinely doesn't fit. Document the choice in `storyboard.md`.

## Pain-Reframe-Promise (PRP)

Default for conversion content. Three beats:

1. **Pain**, name the audience's actual problem in their actual language. Concrete, not abstract. "Your content feels random" not "marketing inefficiency."
2. **Reframe**, flip the problem on its head. The point is *not* what they thought it was. "You don't have a content problem. You have an infrastructure problem."
3. **Promise**, what life looks like on the other side. Specific, verifiable, time-bound when possible.

Timing for 30s: 0–8 / 8–22 / 22–30.
Timing for 60s: 0–15 / 15–45 / 45–60.

Use when: ad creative, landing-page hero video, conversion-focused social.

## Hero Trilogy

Default for product films and brand films. Three beats:

1. **World**, set the context. Who lives in this world. What's broken about it.
2. **Hero**, the product/founder/methodology arrives. Show what it does, not what it is.
3. **Transformation**, the world changes. Show before/after at scale.

Timing for 60s: 0–20 / 20–40 / 40–60.
Timing for 90s: 0–30 / 30–60 / 60–90.

Use when: product launches, brand films, anchor pieces.

## Founder Explainer

Default for personal-brand video where a person speaks to camera. Five micro-beats:

1. **Hook**, a one-line provocation (0–2s)
2. **Stakes**, why this matters (2–8s)
3. **Insight**, the actual point (8–20s for 30s, 8–40s for 60s)
4. **Proof**, one concrete example or data point
5. **CTA**, what to do next, narrow and specific

Use when: founder content, thought leadership, personal-brand pieces.

## Content Spiral

Default for kinetic typography or opinion content. The structure is recursive, each beat zooms in tighter:

1. **Wide claim**, the headline take
2. **Zoom 1**, one layer of nuance
3. **Zoom 2**, the layer underneath that
4. **Snap-back**, return to the wide claim, now reframed by the zooms

Each zoom is 1.5–2x faster than the previous. Pacing accelerates inward.

Use when: opinion videos, kinetic-type pieces, social-native commentary.

## Educational Demo

Default for how-to content. Four beats:

1. **Problem state**, what someone is stuck on
2. **Reveal**, the technique or trick
3. **Walk-through**, apply it step by step
4. **Result**, the after-state, side-by-side with before

Use when: tutorials, demo videos, training content.

## Custom

If the brief doesn't fit, build a custom beat structure. Document in `storyboard.md`:

```markdown
## Beat framework: Custom

**Why custom:** [one sentence, what made the standard frameworks insufficient]

**Beats:**
1. [name], [purpose], [duration]
2. ...
```

Custom is a last resort, not a first move. The standard frameworks exist because they work.


---

## ARCHIVO: storyboard-architect/references/on-screen-text.md

# On-Screen Text

Text on screen is a load-bearing decision. Most storyboards over-text. The default should be: **does this shot need text to land?** If the visual carries the meaning, text dilutes.

## When on-screen text earns its keep

1. **Auto-play-mute environments.** Social feeds. Text replaces VO.
2. **Concept compression.** A short phrase lands harder than 4 seconds of narration.
3. **Stat or proof point.** Numbers stick visually in a way they don't audibly.
4. **Beat punctuation.** A single word or phrase that lands on a music hit.
5. **CTA.** The action you want the viewer to take.

## When on-screen text doesn't earn its keep

1. **Restating the VO.** If the voice says it, the text is noise.
2. **Decorative copy.** "Moments matter" floating over b-roll. Cut it.
3. **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
4. **Filler beats.** If the shot doesn't need text, leave it clean.

## Composition rules

These flow into the `position` field of each text overlay.

### Negative-space-aware composition

When a shot has on-screen text, the **shot subject must reserve space for it**. This is enforced at storyboard time, not generation time.

If text is in the right third → subject composition leaves the right third clear.
If text is lower third → subject upper two-thirds.
If text is centered → subject framed to negative space around center.

This goes into the shot's rationale: "MCU left-third subject, reserves right-third for `text_03`."

### Positions

| Position | Use when |
|---|---|
| `center` | Display headline, single concept, hard cut in/out |
| `lower-third` | Caption / VO substitute, persistent across shots |
| `upper-third` | Stat callout, secondary information |
| `left-third` | Subject is right-weighted in frame |
| `right-third` | Subject is left-weighted in frame |
| `{x: %, y: %}` | Custom, only when the standard positions don't fit |

### Sizes

| Size | Pixel approx (1080p) | Use for |
|---|---|---|
| `display` | 96–144 px | Hero/hook beats |
| `headline` | 56–80 px | Reframe beats |
| `body` | 32–48 px | Caption-style, persistent |
| `caption` | 20–28 px | Disclaimers, attribution |

### Animation

Default to clean, not flashy:

- Hook beats → `hard-cut` in, `hard-cut` out (no fade)
- Reframe beats → `fade-in` 0.2s, `fade-out` 0.2s
- Persistent captions → `slide-up` in, `slide-down` out
- CTA → `type-on` for a typewriter effect, or `slide-up`

Avoid stacking animations. Pick one per overlay.

## Color rules

The `color` field of every text overlay must be a hex value that exists in the brand-lock palette. If you find yourself wanting a color that's not in the palette, the answer is not to add it, the answer is to pick a different overlay style or shot composition.

## Typography rules

Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the brand stops being recognizable.

## The "read twice" rule

Already covered in timing-rules.md but worth repeating: text needs to be on screen long enough for someone to read it twice. Calculate, then verify. Don't eyeball.

## Stacking text across shots

Text can persist across consecutive shots. This is useful when:

- The text takes longer to read than a single shot's duration
- You want text to feel anchored while visuals change underneath

To stack, both shots reference the same `on_screen_text` ID. The overlay's `enter.at` aligns to the first shot's start, `exit.at` aligns to the second shot's end.

In `shots.json`:

```json
{ "id": "shot_03", "on_screen_text": "text_02", ... },
{ "id": "shot_04", "on_screen_text": "text_02", ... }
```

In `text-overlays.json`:

```json
{
  "id": "text_02",
  "shot_id": ["shot_03", "shot_04"],
  ...
}
```

Document this in rationale: "text persists across shot 3-4 to give 4.8s read-time for 16-word reframe."


---

## ARCHIVO: storyboard-architect/references/shot-grammar.md

# Shot Grammar

Controlled vocabulary. Use these exact terms in `shots.json`. Generators interpret loose language inconsistently, locked vocabulary survives translation.

## Framing (subject size in frame)

| Code | Name | What it shows |
|---|---|---|
| `ECU` | Extreme close-up | Eyes, hands, single detail |
| `CU` | Close-up | Head, or full hand-on-object |
| `MCU` | Medium close-up | Head and shoulders |
| `MS` | Medium shot | Waist up |
| `MLS` | Medium long shot | Full body, environment minimal |
| `WS` | Wide shot | Full body, environment present |
| `EWS` | Extreme wide shot | Subject small in environment |

Default to MCU and MS for talking-head founder content. ECU and CU for product detail and emotion. WS and EWS for context-setting.

## Angle (camera vertical position)

| Code | Effect |
|---|---|
| `eye-level` | Neutral, default |
| `high` | Subject feels smaller, vulnerable |
| `low` | Subject feels powerful, dominant |
| `overhead` | Detached, schematic, instructional |
| `dutch` | Tilted, tension, unease |

Default to eye-level. Use the others deliberately, not for variety.

## Motion (camera movement)

| Code | Effect | Use when |
|---|---|---|
| `static` | No movement | Default. Static is not boring. |
| `push` | Camera moves toward subject | Building intensity, revealing |
| `pull` | Camera moves away | Releasing, contextualizing |
| `pan-left` / `pan-right` | Camera rotates horizontally | Surveying environment |
| `tilt-up` / `tilt-down` | Camera rotates vertically | Reveal scale or detail |
| `handheld` | Subtle organic shake | Documentary feel, urgency |
| `orbit` | Camera circles subject | Hero shots, product reveal |
| `whip` | Fast pan as transition | Beat-cuts in fast-paced content |

For AI-generated still frames, motion is mostly intent for the editor. For motion-video prompts (Kling, Veo, Seedance, Hailuo), motion translates directly.

## Depth of field

| Code | Effect |
|---|---|
| `shallow` | Subject sharp, background blurred |
| `deep` | Everything in focus |
| `rack` | Focus shifts mid-shot |

Default to shallow for talking-head, deep for environmental and schematic.

## Lighting style (referenced from series_lock)

Don't redefine per shot. Define once in `series_lock.lighting`. Examples:

- `soft natural side-light, large window left, warm afternoon`
- `hard top-light, single source, deep shadows, studio black`
- `practical mixed sources, neon accents, urban night`

The series_lock string flows into every prompt automatically.

## Subject description

Structured, not poetic. Pattern:

```
[who/what], [doing what], [emotional or compositional note]
```

Good:
```
"Founder, mid-thirties, leaning forward at laptop, face partially turned to window light"
```

Bad:
```
"A determined entrepreneur conquering the digital frontier with passion"
```

Generators reward precision. Adjectives describing emotion ("determined", "passionate") produce stock-photo aesthetics. Describe what the camera actually sees.

## What goes in `subject` vs `series_lock` vs `brand_lock`

This trips people up. The rule:

- **brand_lock**, locked across the entire project. Palette, type, "never" list.
- **series_lock**, locked across this storyboard. Character anchor, environment, lighting style, color grade.
- **subject (per shot)**, what's different about *this* shot. Action, expression, framing-specific composition notes.

If you find yourself repeating the same lighting description across shots, it belongs in series_lock. If you find yourself repeating the same color description across storyboards, it belongs in brand_lock.


---

## ARCHIVO: storyboard-architect/references/timing-rules.md

# Timing Rules

Pacing is math, not feel. Use these as defaults. Override only with reason documented in rationale.

## Shot duration baselines

| Content type | Default shot duration | Range |
|---|---|---|
| Kinetic typography / opinion | 1.0–1.5s | 0.5–2.0s |
| Founder talking-head | 2.5–4.0s | 2.0–6.0s |
| Product/lifestyle b-roll | 1.5–2.5s | 1.0–3.5s |
| Demo / how-to | 3.0–5.0s | 2.0–7.0s |
| Cinematic brand film | 3.5–6.0s | 2.0–10.0s |

If a single shot is longer than 7 seconds in a 30-second piece, justify it in rationale. Long shots are not bad. Unjustified long shots are.

## Hook timing (the first beat)

The hook is 0–2s. Always. There are no exceptions in short-form content. Specifically:

- 9:16 social: first frame must telegraph the topic. Auto-play on mute means the first half-second is fighting a swipe.
- 16:9 in-feed: first 2s decides watch-time.

The hook shot framing should be high-contrast against the shots that follow. If shot 2 is MS, shot 1 should not be MS. Visual contrast = retention.

## CTA timing (the final beat)

The CTA is the final 4–6s for 30s content, 6–10s for 60s content. Specifically:

- Last shot should hold long enough for someone to read the CTA text and act
- Don't put motion on the CTA shot, let the text breathe
- If there's a logo lockup, it lives in the final 2s, not earlier

## On-screen text duration math

A text overlay needs to be on screen long enough to be **read twice**. Not once, twice. Why: viewers are skimming, eyes don't always lock on first frame.

Reading speed reference (assume average viewer):
- 1 short word (≤5 chars): 0.6s minimum read
- Short phrase (≤6 words): 1.2s
- Sentence (≤14 words): 2.4s
- Long sentence (15–25 words): 4.0s

Multiply by 2 for the "read twice" rule. So a 6-word phrase needs **2.4s on screen minimum**.

If a shot is 2 seconds and you need a 14-word sentence, you have a problem. Either:
1. Shorten the copy
2. Carry the text across two consecutive shots (text persists during cut)
3. Lengthen the shot

Do not under-time text. It's the most common storyboard failure.

## Pacing curve

For 30-second content, the natural energy curve:

```
0s ─────────────────────────────────── 30s

Energy
  ▲     ╱╲
  │    ╱  ╲___
  │   ╱       ╲___
  │  ╱            ╲___
  │ ╱                 ╲___
  └─────────────────────────►
   hook  build  apex  release  CTA
   0-2   2-12   12-20  20-26   26-30
```

The apex is two-thirds in, not at the end. The CTA is a release, not a peak.

For 60-second content, scale the same curve. Apex around 0:40, CTA from 0:50.

## Validating timing

Before declaring done, check:

1. Sum of `(end - start)` across all shots equals project duration ±0.1s
2. No shot has `start >= end`
3. No two shots overlap
4. First shot starts at 0.0
5. Last shot ends at project duration
6. Every text overlay's `enter.at` is ≥ its shot's `start`
7. Every text overlay's `exit.at` is ≤ its shot's `end` (or carries to a flagged successor shot)
8. Every text overlay's on-screen duration ≥ read-twice threshold


---

## ARCHIVO: storyboard-architect/tools/README.md

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

