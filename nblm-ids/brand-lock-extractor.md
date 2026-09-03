# Reglas del skill: brand-lock-extractor

89 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## brand-lock-extractor/SKILL.md

- [ebc1422e5d22] This skill extracts. It does not invent. Every value is sampled from a real asset or flagged as an estimate the user must confirm. A confident-sounding wrong hex is worse than a flagged guess.
- [fcc9a56efa31] Written description | Use directly | Identity, archetype, voice posture
- [96e709999be1] Tell the user what you are pulling. Do not ask follow-ups yet, extract first, confirm gaps at the end.
- [5fe217339055] **Identity** (brand, one-line description, archetype, voice posture)
- [0dae3fdc0ace] **Palette** (sampled hex, by role)
- [39e68cb30388] **Typography** (display, body, optional mono, with weights)
- [c183542f6090] **Mood adjectives** (3-5, specific, contrast clauses preferred)
- [6257a4f1fd42] **Never list** (what the brand avoids, inferred from consistency)
- [89c96fc0932b] **Aspect ratios**
- [ddd43db015c9] **Color grade direction** (one sentence)
- [4075284680a4] **Motion language** (one paragraph)
- [086086b8d7f3] **Voice rules** (copy-level constraints)
- [c9c3a9312a4c] **inferred**, reasoned from evidence but not stated (archetype from positioning, never-list from consistency). Reasonable to ship, worth noting.
- [cd4c7a7c3646] Use `templates/brand-lock.md.tpl`. Fill **every** required section, no placeholders left behind. Then append an `## Extraction notes` section that lists every `inferred` and `needs confirmation` value with its source and your reasoning. This section is the audit trail; it does not break validation (the validator checks the nine required sections are present, extra sections are fine).
- [49fd83a4b509] All nine required sections present: Identity, Palette, Typography, Mood adjectives, Never list, Aspect ratios, Color grade direction, Motion language, Voice rules.
- [06963ad7d543] > "Here is your brand-lock. I sampled the palette and type from your assets and flagged N values that need your eyes (see Extraction notes). Drop it in `brand-packs/`, confirm the flagged values, and run `python tools/validate_brand_lock.py path/to/file.md` to verify. Then: `'30-second explainer. Use brand-packs/your-brand.md as the brand lock.'`"
- [afdb75007c72] Colors are sampled, never guessed. Read them from a brand book, from CSS, or by sampling pixels in a screenshot. If you genuinely cannot determine a color, fill your closest estimate and mark it `needs confirmation` in Extraction notes. "Navy" is not a palette entry. `#0F1F3A` is. A wrong hex stated confidently corrupts every downstream prompt.
- [6eb4f8ba4dbc] Identify fonts from the brand book, the site's CSS/font files, or clear visual match. If you cannot identify one, say so and flag it, do not name a plausible-sounding font you did not verify.
- [03ede5f175d7] It is also the hardest to extract, because brands document what they do, not what they avoid. Infer it from consistency: if every image avoids stock-photo gloss, that is a never. If copy never uses exclamation points, that is a never. Read `references/extraction-rubric.md` for the method. Do not ship an empty never-list.
- [165991e88830] `examples/` contains a worked extraction: the source material provided (`input-brief.md`) and the `brand-lock.md` produced from it, including the Extraction notes audit trail. Use it to calibrate the level of specificity and the confidence flagging.

## brand-lock-extractor/brand-packs/README.md

- [5cff35ce456c] Copy `_template.md` to a new file (e.g. `acme.md`)
- [e49a82b5336a] Fill in every field. No placeholders left behind.
- [3e5b03db5bd2] Reference it from your storyboard requests:
- [242353d6abcd] > "30-second founder explainer. Use `brand-packs/acme.md` as the brand lock."
- [ab8ee2cc3cfb] The skill reads it, snapshots it into the output as `brand-lock.snapshot.md`, and applies it through the pipeline.
- [3f9aad2c4e2c] **Be exclusive.** The "never" list is more valuable than the "always" list. Listing what the brand will not do narrows the generator's space and produces tighter output.
- [db7addc154a9] **`whystrohm.md`** (flagship). The actual brand pack WhyStrohm uses on its own content. Real palette, real voice rules, real "never" list. Use this as the reference for the level of specificity production work requires.
- [df43eb92b1b2] Don't hand-author from scratch if the brand already exists. The **`brand-lock-extractor`** skill (ships in this repo at `skills/brand-lock-extractor/`) takes a website URL, a brand book PDF, screenshots, or a written description and produces a `brand-lock.md` in this exact format, with a confidence and source noted for every value:

## brand-lock-extractor/brand-packs/_template.md

- [18cee24eb65b] Role | Hex | Use
- [c5e62839e1ee] Add more rows if the brand has more named colors. Don't add more than 8, past that, the brand stops being recognizable.
- [2f545717c91e] What this brand never does, visually or tonally. Be specific.
- [e03457ae7069] never use stock photo aesthetic
- [25f0ecf00da8] never use AI uncanny faces
- [1acd5803bd0f] never over-saturate
- [3214012dc24d] never shout in copy
- [250eda4c5849] never use clip-art icons
- [5ada3d9e3057] How footage and generated images should be graded. One sentence.
- [74acfc03835c] > e.g. "Camera moves are minimal and deliberate. Static or slow-push. Cuts on action, not on time. Type-on for emphasis, never bouncing or wobbling text."

## brand-lock-extractor/brand-packs/examples/saas-clean.md

- [073359ebd4a2] Role | Hex | Use
- [3d50d9dc8cee] never use stock photo aesthetic
- [2b77fe0ab77d] never use AI uncanny faces
- [528f3aca58d3] never use illustrations of people (real photography or abstract data viz only)
- [34f304b45ae2] never use gradients (flat color only)
- [70f50258fc9f] never use rounded corners larger than 8px
- [a61acb519eac] never use exclamation points
- [39f21f0bd621] never use vague claims ("the best", "industry-leading", "cutting-edge")
- [bdeeca395947] never use AI/ML buzzwords without specifics
- [21f3127a222e] never default to dark mode in primary marketing
- [289646ec1639] never use animated icons or lottie illustrations
- [5108ce119398] prefer specific numbers ("40% reduction in 90 days" not "significant improvement")
- [98944bc5d597] prefer "we" and "you" over "the company" and "the user"
- [5e5cfb4ec221] prefer present-tense
- [cc15db8a3ce1] never start a sentence with "Just" or "Simply"
- [f861a19be4ca] avoid corporate hedge language ("seek to", "look to", "aim to")

## brand-lock-extractor/examples/brand-lock.md

- [16a2f6133356] Role | Hex | Use
- [42b960dda0f5] never use stock smiles or posed lifestyle photography
- [e320951a2f69] never use latte art as decoration
- [deff6acf6ba6] never use the word "artisanal"
- [995266039bd6] never use exclamation points
- [9c0afb7d325a] never shoot glossy product-on-white; matte and natural-light only
- [00c5d773e8d3] never lean on burnt, dark-roast cliche imagery
- [a9ed618bb40b] > Matte, low contrast, natural window light, warm but restrained. Reminiscent of Kinfolk editorial photography. Never glossy commercial product lighting.
- [2d715d9073e7] never the word "artisanal" (or "curated", "elevated")
- [b5797c1841f0] short declarative sentences; cut adjectives before nouns that do not need them
- [fb243b53c635] prefer specific origin claims (farm, region, roast date) over vague quality words
- [007361a9a9c7] Audit trail for this extraction. Values not listed here were read directly from an asset (`extracted`): the four palette hex from the site CSS, both font names from the CSS, the never-list lines from the brand sheet, and the aspect ratios from the brand sheet.

## brand-lock-extractor/examples/input-brief.md

- [b10928de456e] Photography: matte, low-contrast, natural window light. Beans, hands, kraft bags. Never glossy product-on-white.
- [4f015f7fb337] "We don't do: stock smiles, latte art as decoration, exclamation points, or the word 'artisanal'."

## brand-lock-extractor/references/extraction-rubric.md

- [daf6cf4dbcb9] **inferred**, reasoned from evidence, not stated. Archetype from how the brand frames problems. Never-list from what the assets consistently avoid. Ship it, note the reasoning.
- [d446778cd38a] **One-line description:** what the brand does and who for. This is the load-bearing sentence; a generator implicitly references it on every prompt. Pull it from the hero headline plus the about page. Prefer concrete over abstract: "Managed bookkeeping for solo law firms" beats "Financial services for professionals." If the site only offers a vague tagline, sharpen it from the services/about copy a
- [b4fbf43a4a92] **Archetype:** one word, Operator, Sage, Caregiver, Rebel, Creator, Jester, Ruler, Everyman, etc. Almost always `inferred`. Read it from how the brand frames the customer's problem:
- [04363c882bf7] **Never guess a hex.** If you cannot read or sample one, estimate, label it `needs confirmation`, and tell the user exactly which role to verify. (See SKILL.md Rule 1.)
- [a69c36bdec51] **Screenshots:** identify by eye only if confident; otherwise flag `needs confirmation`. Do not invent a plausible name (Rule 2).
- [a1ad2f291171] 3-5 adjectives, specific, contrast clauses preferred. Read tone from the body copy and the imagery together.
- [775e72423ee9] The hardest and most valuable section. Brands document what they do; you infer what they avoid from consistency across the assets.
- [3f18cfa9b5e8] Imagery: no stock-photo gloss? no people? no gradients? no clip-art icons? Each absence is a never.
- [a86e2eb18131] Copy: no exclamation points? no hype words ("revolutionary", "game-changing")? no emojis? no questions in headlines? Each pattern is a never.
- [451be222e3f4] Color/layout: never full-bleed photography? never more than one accent? never centered body text?
- [f419380942de] Turn each observed constraint into a `never` line. Be specific: "never use stock-photo aesthetic" beats "keep it authentic". Aim for 5+. Never ship an empty list (Rule 4).
- [dd519aa232b4] One sentence on how footage and generated images should be graded, with a reference point where possible (Kodak Portra 400, Apple keynote photography, A24 film grade). Infer from the existing photography's warmth, contrast, and saturation. If there is no photography to read, base it on the palette and flag `needs confirmation`.
- [5a0a397f54c1] One paragraph: camera moves, cut style, text animation, pacing. Read from any existing video or motion on the site; if there is none, infer a conservative default consistent with the voice posture (a Quiet/Authoritative brand -> minimal, slow, deliberate) and flag `needs confirmation`. Keep it to one coherent motion language, do not blend "minimal and deliberate" with "energetic whip pans".
- [f3fad8754516] Copy-level constraints for VO and on-screen text. Many overlap the never-list but are phrased as authoring rules: "no em dashes", "sentences under 14 words", "prefer specific numbers over vague claims", "no exclamation points in headlines". Extract from observed copy patterns. These become prompt constraints downstream, so make them enforceable, not aspirational.

## brand-lock-extractor/tools/README.md

- [697ee94e32d3] Checks every `SKILL.md` in `skills/` has the required YAML frontmatter, a `name` that matches
- [c9c4d69a1e9d] Checks a brand-lock has all required sections and Identity fields, that its palette declares
- [4f5a12623761] `<!-- source: ... -->` header, with a full UTC instant preferred over a bare date.
- [d06f5a7d29d6] to be identified, and a named generator has to exist in the capability matrix.
- [43590512414d] a frame on disk with no critique for its round, never reviewed at all
- [4833d679d27e] template the skill uses, through the small engine in `_template.py`. It did not always: the
- [540c0d3d82a5] never land in the clipboard, so a revision file's `# fix [...]` notes are shown but not