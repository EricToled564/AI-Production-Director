# SKILL: storyboard-html-preview

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: storyboard-html-preview/SKILL.md

---
name: storyboard-html-preview
description: Render a structured storyboard (storyboard.md, shots.json, text-overlays.json, brand-lock.snapshot.md) into a single-file HTML preview that is shareable, printable, and offline. Use when the user wants to share a storyboard, export for review, hand off to an editor, or print a hard copy. Triggers on "preview the storyboard", "share this", "export to HTML", "print version", or after a storyboard-architect run. Produces one self-contained .html file with no build or server.
---

# Storyboard HTML Preview

You are turning structured storyboard files into a single shareable HTML document. The output is what an editor, stakeholder, or client opens in a browser without thinking about it.

The constraint is non-negotiable: **single file, no build step, no server, works offline.** Any time the output requires "run this build command" or "host this somewhere," the skill has failed.

## When to use

Trigger when the user:

- Asks to preview, share, or export a storyboard
- Wants a printable version
- Says "what's the next step" after a storyboard-architect run
- Hands off `storyboard.md` + `shots.json` + asks for a deliverable for review

## What you produce

One file: `preview.html`. Self-contained. Inline CSS. No JavaScript dependencies (vanilla JS only, embedded). No external font files (uses system stack with brand-font fallbacks). No external images (placeholder slots; if generated images exist, embed as base64 OR reference relative paths).

```
output/
├── run.json                   # input, for the run id and date
├── storyboard.md              # input
├── shots.json                 # input
├── text-overlays.json         # input
├── brand-lock.snapshot.md     # input
├── frames/round-N/            # input, if generation has happened
├── critiques/round-N/         # input, for the verdict badges
└── preview.html               # ← what this skill produces
```

If the user has generated frames, the HTML references them via relative paths so the file
works when the whole `output/` folder is shared. Resolve a shot's frame in this order:

1. An entry in `shot.assets.generated` marked `accepted: true`
2. The newest entry in `shot.assets.generated`
3. `frames/round-{highest}/{shot_id}.{png,jpg,jpeg,webp}`
4. `generated/{shot_id}.{ext}`, the pre-3.0.0 flat layout

Data first, convention second. Reading the path convention first meant the page showed
whatever file happened to sit there, accepted or rejected, first draft or fifth re-roll.

If no frames exist yet, the HTML uses styled placeholder cards with the shot spec, still
useful for review and handoff.

## Workflow

### Step 1. Read inputs

Required:

- `shots.json`
- `text-overlays.json`
- `brand-lock.snapshot.md`

Optional:

- `run.json` (for the run id and date; without it the page says "not recorded")
- `storyboard.md` (for narrative context, surface the brief at the top)
- `frames/round-N/{shot_id}.{png,jpg,jpeg,webp}` (if generation has happened)
- `critiques/round-N/{shot_id}.critique.json` (for verdict badges)

Validate before rendering, and stop if it fails:

```bash
python tools/validate_shots.py output/
```

### Step 2. Extract brand parameters

From `brand-lock.snapshot.md`, extract:

- Palette (hex values), used for HTML accent colors
- Display font and body font names, used as font-family values with system fallbacks
- Brand voice / mood, used in subtle copy choices

The HTML preview should *feel* like the brand without going overboard. Quiet branding, not loud.

### Step 3. Generate the HTML

Use `templates/preview.html.tpl` as the structural template. Read it before generating.

The HTML structure:

```
<!DOCTYPE html>
<html>
<head>
  <meta>
  <title>{project title}</title>
  <style>
    /* All CSS inline. ~200 lines. Brand-aware. */
    /* Print stylesheet included. */
  </style>
</head>
<body>
  <header>
    <!-- Project title, duration, aspect, generated timestamp -->
  </header>

  <section class="brief">
    <!-- Brief summary if storyboard.md provides one -->
  </section>

  <section class="series-lock">
    <!-- Character / environment / lighting / color grade -->
  </section>

  <section class="shots">
    <!-- One card per shot -->
    <article class="shot" id="shot_01">
      <div class="shot-frame">
        <!-- generated image OR styled placeholder -->
      </div>
      <div class="shot-meta">
        <!-- timestamp, framing, angle, motion -->
      </div>
      <div class="shot-subject">
        <!-- subject description -->
      </div>
      <div class="shot-text-overlay">
        <!-- if on_screen_text exists, show overlay content with timing -->
      </div>
      <div class="shot-rationale">
        <!-- rationale text -->
      </div>
    </article>
    <!-- ... -->
  </section>

  <footer>
    <!-- audit trail: brand-lock snapshot reference, timestamp -->
  </footer>

  <script>
    /* Vanilla JS only. Optional: keyboard nav, jump-to-shot, expand/collapse. */
  </script>
</body>
</html>
```

### Step 4. Embed frames if available

Resolve each shot's frame by the order in "What you produce" above, then reference it by a
path relative to the output root:

```html
<img src="frames/round-2/shot_01.png" alt="shot_01: hook" loading="lazy" />
```

This works when the whole output folder is zipped and shared.

For hard-copy print (a single file with no folder structure), the skill can offer to inline
frames as base64. Ask the user which they prefer if frames are present.

If a shot's `assets.generated` entry carries a `sha256` and the file no longer matches it,
render the frame but say so on the page. That mismatch means the frame changed after it was
recorded, which is exactly the case where a preview quietly showing the new file is worse
than one that flags it.

If no frames exist, render styled placeholder cards showing the framing, subject, and shot
spec. These are still useful for stakeholder review at the storyboard stage.

**Template flag convention.** When composing the per-shot context for `preview.html.tpl`, set exactly one of:

- `has_image: true` and `image_path: "frames/round-2/shot_NN.png"`, when a frame exists
- `has_no_image: true`, when none does (renders the placeholder card)

The template uses two parallel `{{#if}}` blocks rather than `{{#if}}/{{else}}` to keep the rendering portable across template engines.

For text overlays, set `has_overlays: true` and an `overlays` array on the shot. Each entry
carries `id`, `content`, `font`, `weight`, `color`, `size`, `position_class`,
`position_label`, `enter_at`, `enter_animation`, `exit_at`, `exit_animation`. The template
iterates that array with `{{#each overlays}}`.

It is an array because `shots.json` lets a shot carry several overlays and
`text-overlays.json` always did. A single set of `overlay_*` fields could hold one, so the
second overlay on a shot rendered nowhere and nothing reported it.

For verdict badges, set `has_verdict`, `verdict`, `verdict_round`, and `verdict_class`
(the lowercased verdict) from the newest critique for that shot under `critiques/`. Omit
them when the shot has no critique.

**Escape everything.** Subjects, rationales, VO lines, and overlay copy are model-generated
prose that lands in both text and attribute contexts. One angle bracket in a rationale, or
one quote in an overlay font name, breaks the page a client is reading.
`tools/shots-to-html.py` escapes every substitution by default and reserves raw output for
the inlined CSS alone.

### Step 5. Render text overlays visually

For every shot with an `on_screen_text` reference, the HTML shows:

- The text content rendered in approximately the brand font (or visible fallback)
- The position indicated visually (lower-third, center, etc.)
- Timing info (enter/exit beats)

This gives the reviewer a sense of what the final composited frame will look like, even before final compositing happens.

### Step 6. Print stylesheet

Include `@media print` rules that:

- Hide nav, footer scripts, expand/collapse UI
- Force one shot per page (or two if compact)
- Ensure text overlays render legibly
- Use black-on-white where brand colors won't print well

The user should be able to hit Cmd-P / Ctrl-P and get a clean PDF.

## Hard rules

### Rule 1. Single file, no exceptions

The output is one `.html` file. If you find yourself wanting a separate stylesheet or JS file, inline it. If you find yourself wanting a build step, you're solving the wrong problem.

### Rule 2. No external dependencies at runtime

No CDN scripts. No Google Fonts. No external CSS frameworks. The file must work with no internet connection.

The exception: if the user explicitly opts in (e.g. "make it pretty, I'm online"), Tailwind via CDN is acceptable. Default is no.

### Rule 3. Print must work

Hit Cmd-P. The result should be a clean PDF. If layout breaks across page boundaries, the print stylesheet is broken.

### Rule 4. Brand-aware but quiet

Use brand colors as accents, not as full backgrounds. The reviewer's job is to read the storyboard, not admire the design. Subtle.

### Rule 5. Mobile-readable

Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.

## Templates

- `templates/preview.html.tpl`, the structural template
- `templates/styles.css.tpl`, the CSS to inline
- `templates/print.css.tpl`, the print rules

The skill reads all three and assembles them into a single `preview.html`.

## Quality bar

Before declaring done, verify:

- [ ] File opens in any browser (Chrome, Safari, Firefox) with no errors
- [ ] No external network requests fire on load
- [ ] Print preview produces a clean PDF
- [ ] Mobile viewport (375px) renders without horizontal scroll
- [ ] Brand colors and fonts come from the brand-lock, not from a fallback
- [ ] Every shot from `shots.json` is present
- [ ] Every overlay referenced by a shot is rendered, including second and third overlays
- [ ] `brand_lock_ref` from `shots.json` is what the footer links to, not a hardcoded name
- [ ] The run date and the render date are both shown, and labelled differently
- [ ] No `{{` remains anywhere in the output

The CLI renderer checks the mechanical half of that list against itself:

```bash
python tools/shots-to-html.py --selftest
```

## Two timestamps, not one

"Run" is when the storyboard was produced, read from `run.json`. "Rendered" is when the page
was written. They are separate lines in the footer and they must stay separate.

Collapsing them into a single "Generated" date meant re-rendering a preview six months later
restamped the run as today, and the footer went on asserting the page was built against a
brand-lock on a date that had nothing to do with the frames above it.

If the brand-lock on disk no longer hashes to what `run.json` recorded, say so on the page.
The reader is looking at frames built against a brand state they can no longer see.

## Examples

Generated `preview.html` files ship next to the storyboards that produced them:

- `../storyboard-architect/examples/30s-pain-proof-promise/preview.html`
- `../storyboard-architect/examples/60s-founder-explainer/preview.html`
- `../storyboard-architect/examples/shotkit-explainer/preview.html`, including the
  two-overlay shot
- `../visual-asset-critic/examples/worked-run/preview.html`, with frames and verdict badges

Open them in a browser to calibrate quality. All four are re-rendered in CI with pinned
timestamps and the build fails if the output moves, so they are also the regression test for
this skill's output.


---

## ARCHIVO: storyboard-html-preview/tools/README.md

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

