# SKILL: brand-lock-extractor

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: brand-lock-extractor/SKILL.md

---
name: brand-lock-extractor
description: Extract a production-ready brand-lock.md from a brand's existing assets. Point it at a website URL, a brand book PDF, screenshots, or a written description and it produces the nine-section brand-lock the rest of shotkit consumes, with a confidence and source noted for every value. Use when the user wants to onboard a brand, says "build a brand lock", "extract my brand", "make a brand pack from my site", or hands over brand assets. The cold-start killer that turns a blank brand-pack template into a filled, validate-ready file. Pairs with storyboard-architect downstream.
---

# Brand Lock Extractor

The blank `brand-packs/_template.md` is the single biggest point of friction in shotkit. Nobody wants to hand-author nine sections of brand parameters before they can produce a single storyboard. This skill removes that wall: hand it what you already have, get a filled brand-lock back.

The output is a `brand-lock.md` in the exact format `tools/validate_brand_lock.py` validates and every other skill consumes. Same file the pipeline reads, produced from your assets instead of from scratch.

This skill extracts. It does not invent. Every value is sampled from a real asset or flagged as an estimate the user must confirm. A confident-sounding wrong hex is worse than a flagged guess.

## When to use

Trigger when the user:

- Wants to onboard a brand into shotkit and has assets (a site, a brand book, screenshots)
- Says "extract my brand", "build a brand lock", "make a brand pack from my site/PDF"
- Hands over a URL, a PDF, image files, or a written brand description and asks for a brand-lock
- Has a brand-lock that is half-filled and wants the gaps extracted from assets

If the user has nothing but a vague idea (no assets, no description), they are not extracting, they are authoring. Point them at `brand-packs/_template.md` and help them fill it directly.

## Inputs

You can work from any one of these. More sources is a better extraction.

| Source | How you read it | Best for |
|---|---|---|
| Website URL | `WebFetch` homepage + about + one more page | Voice, positioning, palette, type |
| Brand book PDF | `Read` the PDF | Palette (exact hex), type, motion rules |
| Screenshots / image files | `Read` the images | Palette (sample pixels), mood, layout |
| Written description | Use directly | Identity, archetype, voice posture |

At minimum you need one source. If the user offers none, ask for the one they have: **"What can I work from, a website URL, a brand book PDF, screenshots, or a short description?"** One question.

## Workflow

### Step 1. Gather the source material

- **URL:** `WebFetch` the homepage, then try the about page (`/about`, `/about-us`, `/our-story`) and one more (`/services`, `/work`, recent blog). Skip pages that 404. The homepage is the floor.
- **PDF / images:** `Read` each file. Brand books carry exact hex and type; screenshots are for sampling color and reading mood.
- **Description:** take it as written.

Tell the user what you are pulling. Do not ask follow-ups yet, extract first, confirm gaps at the end.

### Step 2. Extract each section

Read `references/extraction-rubric.md`. It maps every brand-lock section to where the signal lives and how to read it. Work the nine sections in order:

1. **Identity** (brand, one-line description, archetype, voice posture)
2. **Palette** (sampled hex, by role)
3. **Typography** (display, body, optional mono, with weights)
4. **Mood adjectives** (3-5, specific, contrast clauses preferred)
5. **Never list** (what the brand avoids, inferred from consistency)
6. **Aspect ratios**
7. **Color grade direction** (one sentence)
8. **Motion language** (one paragraph)
9. **Voice rules** (copy-level constraints)

For every value, hold two things: the value, and where it came from (which asset, which quote, which sampled swatch). You will need the source for the confidence pass.

### Step 3. Assign confidence and flag estimates

Each value is one of:

- **extracted**, read directly from an asset (a hex in the brand book, a font in the CSS, a quote from the site). State it plainly.
- **inferred**, reasoned from evidence but not stated (archetype from positioning, never-list from consistency). Reasonable to ship, worth noting.
- **needs confirmation**, your best estimate where the assets were silent or ambiguous (a color sampled from a JPEG with compression, a font you could not identify). Fill it, then flag it.

### Step 4. Write the brand-lock

Use `templates/brand-lock.md.tpl`. Fill **every** required section, no placeholders left behind. Then append an `## Extraction notes` section that lists every `inferred` and `needs confirmation` value with its source and your reasoning. This section is the audit trail; it does not break validation (the validator checks the nine required sections are present, extra sections are fine).

Set the footer: `Last updated` to today, `Owner` to the user or "extracted", `Version: 1.0`.

### Step 5. Self-check, then hand off

Before you present it, confirm the file would pass validation:

- All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion language, Voice rules.
- Identity contains all four fields: Brand, One-line description, Archetype, Voice posture.
- Palette has at least one real `#RRGGBB` hex (not a placeholder).

Then hand off:

> "Here is your brand-lock. I sampled the palette and type from your assets and flagged N values that need your eyes (see Extraction notes). Drop it in `brand-packs/`, confirm the flagged values, and run `python tools/validate_brand_lock.py path/to/file.md` to verify. Then: `'30-second explainer. Use brand-packs/your-brand.md as the brand lock.'`"

## Hard rules

### Rule 1. Never invent a hex value

Colors are sampled, never guessed. Read them from a brand book, from CSS, or by sampling pixels in a screenshot. If you genuinely cannot determine a color, fill your closest estimate and mark it `needs confirmation` in Extraction notes. "Navy" is not a palette entry. `#0F1F3A` is. A wrong hex stated confidently corrupts every downstream prompt.

### Rule 2. Never fabricate a typeface

Identify fonts from the brand book, the site's CSS/font files, or clear visual match. If you cannot identify one, say so and flag it, do not name a plausible-sounding font you did not verify.

### Rule 3. Source everything

Every extracted value traces to an asset. Every inferred value traces to reasoning. This is the same audit-trail discipline as the brand-lock snapshot, applied at extraction time.

### Rule 4. The never-list is the highest-value section

It is also the hardest to extract, because brands document what they do, not what they avoid. Infer it from consistency: if every image avoids stock-photo gloss, that is a never. If copy never uses exclamation points, that is a never. Read `references/extraction-rubric.md` for the method. Do not ship an empty never-list.

### Rule 5. Mood adjectives must be specific

"Professional, modern, clean" describes every brand and constrains nothing. Extract contrast clauses that do work: "operator not creator", "warm not precious", "confident without volume". If the assets only support generic adjectives, that is a `needs confirmation` flag, not a license to ship filler.

### Rule 6. No emojis, no hype

The output is a clinical specification. It models the standards the brand-lock enforces. No emojis anywhere. No marketing adjectives about the brand in your own voice, report what the assets show.

## Reference

- `references/extraction-rubric.md`, section-by-section extraction method and confidence definitions.

## Example

`examples/` contains a worked extraction: the source material provided (`input-brief.md`) and the `brand-lock.md` produced from it, including the Extraction notes audit trail. Use it to calibrate the level of specificity and the confidence flagging.


---

## ARCHIVO: brand-lock-extractor/brand-packs/README.md

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

## ARCHIVO: brand-lock-extractor/brand-packs/_template.md

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

## ARCHIVO: brand-lock-extractor/brand-packs/examples/saas-clean.md

# Brand Lock: Acme SaaS (Example)

> Reference example for B2B SaaS brands. Restrained, professional, single-accent palette.

## Identity

**Brand:** Acme SaaS
**One-line description:** B2B platform that helps SaaS teams cut churn 40% in 90 days through customer health scoring and intervention workflows.
**Archetype:** Sage
**Voice posture:** Confident, data-driven, peer-to-peer (not vendor-to-buyer)

## Palette

| Role | Hex | Use |
|---|---|---|
| Background | `#FFFFFF` | Pure white, primary canvas |
| Ink | `#0F1F3A` | Deep navy, primary text |
| Accent | `#3B82F6` | Bright blue. CTAs, data highlights |
| Muted | `#64748B` | Slate, secondary text, captions |
| Rule | `#E2E8F0` | Light gray, borders, dividers |
| Success | `#10B981` | Emerald, positive metrics, gains |
| Warning | `#F59E0B` | Amber, alerts, attention items |

## Typography

**Display font:** `Inter Bold 700`
**Body font:** `Inter Regular 400`
**Mono font:** `JetBrains Mono Regular`, for data, code, dashboards

## Mood adjectives

- credible
- precise
- helpful
- restrained
- expert

## Never list

- never use stock photo aesthetic
- never use AI uncanny faces
- never use illustrations of people (real photography or abstract data viz only)
- never use gradients (flat color only)
- never use rounded corners larger than 8px
- never use exclamation points
- never use vague claims ("the best", "industry-leading", "cutting-edge")
- never use AI/ML buzzwords without specifics
- never default to dark mode in primary marketing
- never use animated icons or lottie illustrations

## Aspect ratios

- 16:9, primary for product demos and hero films
- 9:16, short-form social
- 1:1. LinkedIn carousels

## Color grade direction

Clean, neutral, slight cool bias. White points pure white, blacks deep but not crushed. Skin tones natural. No filmic grain. Reminiscent of Apple keynote photography, clean, evenly lit, technically perfect.

## Motion language

Minimal motion. UI elements appear with subtle 200ms fade. Cuts on logic beats, not on time. Data visualizations animate with linear easing, no bounce, no overshoot. Camera moves limited to slow push on hero shots. No handheld, no whip pans, no transitions beyond hard cuts.

## Voice rules

- no em dashes
- no exclamation points
- no hype words
- prefer specific numbers ("40% reduction in 90 days" not "significant improvement")
- prefer "we" and "you" over "the company" and "the user"
- prefer present-tense
- never start a sentence with "Just" or "Simply"
- avoid corporate hedge language ("seek to", "look to", "aim to")

## Reference materials

- Vercel marketing, design language reference
- Linear marketing, voice and pacing reference
- Stripe Press, typography and density reference

---

**Last updated:** 2026-05-07
**Owner:** Example
**Version:** 1.0


---

## ARCHIVO: brand-lock-extractor/examples/brand-lock.md

# Brand Lock: Northwind Coffee Roasters

## Identity

**Brand:** Northwind Coffee Roasters
**One-line description:** Small-batch coffee, roasted and shipped the same morning, with full origin transparency, for people who want real coffee and no subscription to babysit.
**Archetype:** Maker, with a Rebel edge against pretension (frames the category's problem as cheap beans hidden behind burnt roasts and luxury pricing).
**Voice posture:** Plainspoken and confident. Short declaratives, dry, no decoration.

## Palette

Every hex value here is allowed. Anything outside this list is not.

| Role | Hex | Use |
|---|---|---|
| Background | `#F4EFE6` | Paper cream, primary canvas |
| Ink | `#2B2018` | Espresso brown, primary text and dark elements |
| Accent | `#C5562B` | Ember, highlights and CTAs |
| Muted | `#8A8076` | Stone, secondary text and captions |
| Rule | `#DCD3C4` | Borders and dividers |

## Typography

**Display font:** `Tiempos Headline Semibold`, serif
**Body font:** `Söhne Regular`, sans-serif, Medium for emphasis

## Mood adjectives

- plainspoken, not precious
- warm, not cozy-cute
- honest about origin
- unhurried

## Never list

- never use stock smiles or posed lifestyle photography
- never use latte art as decoration
- never use the word "artisanal"
- never use exclamation points
- never shoot glossy product-on-white; matte and natural-light only
- never lean on burnt, dark-roast cliche imagery

## Aspect ratios

Default: 4:5 and 9:16 for social, 16:9 for the web hero.

## Color grade direction

> Matte, low contrast, natural window light, warm but restrained. Reminiscent of Kinfolk editorial photography. Never glossy commercial product lighting.

## Motion language

> Minimal and unhurried. Static or slow push only. Cuts land on action, not on a timer. Type sets in place, it does not bounce or wobble. No fast cuts, no whip pans.

## Voice rules

- no exclamation points, anywhere
- never the word "artisanal" (or "curated", "elevated")
- short declarative sentences; cut adjectives before nouns that do not need them
- prefer specific origin claims (farm, region, roast date) over vague quality words
- no hype words ("best", "premium", "game-changing")

## Extraction notes

Audit trail for this extraction. Values not listed here were read directly from an asset (`extracted`): the four palette hex from the site CSS, both font names from the CSS, the never-list lines from the brand sheet, and the aspect ratios from the brand sheet.

**Inferred** (reasoned from evidence, reasonable to ship):
- Archetype "Maker / Rebel", from "we are roasters, not a lifestyle brand. The coffee does the talking" and the framing of competitors as burnt-cheap or overpriced.
- Mood adjectives, from the plainspoken homepage copy and the matte, natural-light photography described on the brand sheet.
- Color grade direction, inferred from the brand sheet's photography notes (matte, low-contrast, window light); no graded footage was provided.

**Needs confirmation** (best estimate, please verify):
- Rule color `#DCD3C4`, no divider/border color was given; estimated as a darker tint of the paper background. Confirm or replace.
- Font weights (Tiempos Headline Semibold, Söhne Regular/Medium), fonts are confirmed from CSS, weights are estimated from visual weight. Confirm against the brand book.
- Motion language, no motion assets were provided; this is a conservative default consistent with the Plainspoken/Confident posture. Confirm against any existing video.

---

**Last updated:** 2026-06-18
**Owner:** extracted
**Version:** 1.0


---

## ARCHIVO: brand-lock-extractor/examples/input-brief.md

# Example input: what the user handed over

This is the raw source material for the worked extraction. The user provided a URL and a one-page brand sheet. The `brand-lock.md` in this folder is what the skill produced from it.

## Source 1: website (fetched)

**Homepage hero:**
> Northwind Coffee Roasters
> Small-batch coffee, roasted the morning it ships.
> No subscriptions to forget about. No bitter shortcuts. Just coffee that tastes like someone cared.

**About page excerpt:**
> We started Northwind in a one-car garage in Duluth because the coffee we could buy locally was either burnt to hide cheap beans or priced like a luxury good. We roast in small batches, ship the same day, and tell you exactly where the beans came from and who grew them. We are roasters, not a lifestyle brand. The coffee does the talking.

**CSS (from the page source):**
```
--paper: #F4EFE6;
--espresso: #2B2018;
--ember: #C5562B;
--stone: #8A8076;
font-family: "Tiempos Headline", Georgia, serif;   /* headings */
font-family: "Söhne", -apple-system, sans-serif;    /* body */
```

## Source 2: one-page brand sheet (read)

- Logo: wordmark only, espresso brown on paper cream. No icon.
- Photography: matte, low-contrast, natural window light. Beans, hands, kraft bags. Never glossy product-on-white.
- "We don't do: stock smiles, latte art as decoration, exclamation points, or the word 'artisanal'."
- Formats noted: Instagram (4:5 and 9:16), website hero (16:9).


---

## ARCHIVO: brand-lock-extractor/references/extraction-rubric.md

# Extraction rubric

How to read each brand-lock section out of real assets. For every section: where the signal lives, how to read it, and how to assign confidence.

## Confidence levels

Apply one to every value.

- **extracted**, read directly from an asset. A hex in the brand book PDF. A `font-family` in the site CSS. A verbatim quote from the homepage. Ship it plainly.
- **inferred**, reasoned from evidence, not stated. Archetype from how the brand frames problems. Never-list from what the assets consistently avoid. Ship it, note the reasoning.
- **needs confirmation**, a best estimate where assets were silent, compressed, or contradictory. A color sampled from a low-quality JPEG. A font you could not positively identify. Fill it so the file is complete, then flag it in Extraction notes.

## Identity

**Brand:** the name. Extracted from the logo, the title tag, or the description.

**One-line description:** what the brand does and who for. This is the load-bearing sentence; a generator implicitly references it on every prompt. Pull it from the hero headline plus the about page. Prefer concrete over abstract: "Managed bookkeeping for solo law firms" beats "Financial services for professionals." If the site only offers a vague tagline, sharpen it from the services/about copy and flag it `needs confirmation`.

**Archetype:** one word, Operator, Sage, Caregiver, Rebel, Creator, Jester, Ruler, Everyman, etc. Almost always `inferred`. Read it from how the brand frames the customer's problem:
- frames problems as systems to engineer -> Operator
- frames problems as questions to investigate -> Sage
- frames problems as people to support -> Caregiver
- frames problems as a status quo to break -> Rebel

**Voice posture:** Confident / Warm / Sharp / Quiet / Playful / Authoritative. Read from sentence length, punctuation, and word choice in the body copy. Short declaratives -> Sharp/Confident. Long, soft, second-person -> Warm. Cite a representative sentence.

## Palette

A table of `#RRGGBB` by role: Background, Ink, Accent, Muted, Rule, plus any brand-specific roles. Up to 8; past that the brand stops being recognizable.

How to get real hex:
- **Brand book PDF:** read the swatches directly. Highest confidence.
- **Website:** the CSS holds exact values (`background`, `color`, CSS custom properties like `--accent`). Highest confidence after a brand book.
- **Screenshots:** sample the dominant background, the text color, and the one or two accent colors. Compression shifts color slightly, so flag screenshot-sampled values `needs confirmation` unless they are clearly flat brand colors.

**Never guess a hex.** If you cannot read or sample one, estimate, label it `needs confirmation`, and tell the user exactly which role to verify. (See SKILL.md Rule 1.)

## Typography

Display font, body font, optional mono, each with weight (`Inter Black 900`, not `Inter Bold`).

- **Website:** `font-family` declarations and loaded font files (`fonts.googleapis.com`, `@font-face`, `.woff2` names) name the fonts exactly. Weights come from `font-weight`.
- **Brand book:** named directly.
- **Screenshots:** identify by eye only if confident; otherwise flag `needs confirmation`. Do not invent a plausible name (Rule 2).

Two fonts max; three only if one is mono for code/data.

## Mood adjectives

3-5 adjectives, specific, contrast clauses preferred. Read tone from the body copy and the imagery together.

Reject generic fillers ("professional, modern, clean"), they describe everything and constrain nothing. Push to contrast clauses that do work: "operator not creator", "warm not precious", "plainspoken not corporate". If the assets only support generic adjectives, flag `needs confirmation`. Cite the copy or image that supports each adjective.

## Never list

The hardest and most valuable section. Brands document what they do; you infer what they avoid from consistency across the assets.

Method, look for what is conspicuously absent:
- Imagery: no stock-photo gloss? no people? no gradients? no clip-art icons? Each absence is a never.
- Copy: no exclamation points? no hype words ("revolutionary", "game-changing")? no emojis? no questions in headlines? Each pattern is a never.
- Color/layout: never full-bleed photography? never more than one accent? never centered body text?

Turn each observed constraint into a `never` line. Be specific: "never use stock-photo aesthetic" beats "keep it authentic". Aim for 5+. Never ship an empty list (Rule 4).

## Aspect ratios

The ratios the brand renders for. Default to `9:16, 16:9, 1:1, 4:5`. If the assets reveal a bias (a vertical-only social brand, a cinematic 21:9 site hero), reflect it and note the evidence.

## Color grade direction

One sentence on how footage and generated images should be graded, with a reference point where possible (Kodak Portra 400, Apple keynote photography, A24 film grade). Infer from the existing photography's warmth, contrast, and saturation. If there is no photography to read, base it on the palette and flag `needs confirmation`.

## Motion language

One paragraph: camera moves, cut style, text animation, pacing. Read from any existing video or motion on the site; if there is none, infer a conservative default consistent with the voice posture (a Quiet/Authoritative brand -> minimal, slow, deliberate) and flag `needs confirmation`. Keep it to one coherent motion language, do not blend "minimal and deliberate" with "energetic whip pans".

## Voice rules

Copy-level constraints for VO and on-screen text. Many overlap the never-list but are phrased as authoring rules: "no em dashes", "sentences under 14 words", "prefer specific numbers over vague claims", "no exclamation points in headlines". Extract from observed copy patterns. These become prompt constraints downstream, so make them enforceable, not aspirational.


---

## ARCHIVO: brand-lock-extractor/tools/README.md

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

