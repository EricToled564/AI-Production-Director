# Reglas del skill: storyboard-architect

152 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## storyboard-architect/SKILL.md

- [364c86aacbd6] If the user only wants prompts for an image generator (no narrative structure), use `visual-prompt-forge` directly instead.
- [7696a03e6c31] Write it once, at the end of the run, and never edit it.
- [8f9cad0e2224] If the user asks for image prompts or HTML preview, hand off to `visual-prompt-forge` or `storyboard-html-preview`, those skills consume `shots.json` directly. Don't try to do their job here.
- [6c9cf5270a4d] Input | Required? | Default if absent
- [8d21f65f4329] Brand-lock file path | No | Use `brand-packs/_template.md` and flag the gap
- [0a6768420027] Follow this sequence. Don't skip steps even if the brief seems simple.
- [c7861b2bb543] "Never" list (what this brand will never do visually)
- [8b27a216f395] Aspect-ratio preferences
- [5b7b1c8fb6ae] If no brand-lock is provided, copy `brand-packs/_template.md` into the output as `brand-lock.snapshot.md` with a note: `# UNCONFIGURED, using template defaults. Recommend providing a real brand-lock for production work.`
- [0b4182e7f0fc] Don't fight the framework. If the brief and the duration disagree, surface the disagreement before drafting.
- [37204f4e9d9d] `start` / `end`, timestamps in seconds, decimal allowed. `end` must be after `start`
- [bbcf9882e50b] `depth_of_field`, optional, shallow / deep / rack
- [5942ba44f22f] Every piece of on-screen text becomes an entry in `text-overlays.json`. Never bake text into the visual description. Each overlay has:
- [1cec4673e7f2] `color`, hex (must come from brand-lock palette)
- [abc02ebdb6a8] Every shot has a one-sentence rationale. Why this beat. Why this framing. Why this on-screen text. This is the audit trail. Do not skip it.
- [38de07452a46] Use the template at `templates/storyboard.md.tpl`. Read it before writing.
- [16f6bf46f67c] Must validate against `templates/shots.schema.json`. Read it before writing. The structure is:
- [85e3ed23b8ae] Must validate against `templates/text-overlays.schema.json`. Read it before writing.
- [953b9b11b0eb] Run the validator. Do not eyeball this list.
- [4c1f6d0ef267] Don't run those automatically. The user picks.

## storyboard-architect/examples/30s-pain-proof-promise/brand-lock.snapshot.md

- [d57bd1da3f85] Role | Hex | Use
- [25d9cd499896] never use stock photo aesthetic
- [e815875bfd9e] never use AI uncanny faces
- [dd6e8d6008ac] never over-saturate the cream background
- [333c20110ff3] never use coral as a flood color (only as accent or signature periods)
- [5aecc4ca21d4] never use em dashes in copy
- [dac6a52ee58c] never use emojis in body copy
- [c95b248c14c2] never use bullet points in narrative copy
- [c906d8795790] never use clip-art or generic icon sets
- [ba0238372a4c] never use hype words ("game-changing", "revolutionary", "next-level", "comprehensive")
- [03c4f6662db6] never use exclamation points in headlines
- [91020f8aff04] never default to dark mode, light mode hybrid is the brand
- [26257934361a] never animate text with bouncing or wobbling, type-on, fade, or hard cut only
- [65805ba83e7e] Warm filmic, muted teal shadows. Slight grain. Cream highlights, deep navy/charcoal shadows, never crushed. Reminiscent of Kodak Portra 400 with a slight digital cleanup.
- [19abf8cb5067] Camera moves are minimal and deliberate. Default to static. When motion is used, slow push or slow pull only. Cuts on action, not on time. Type-on for emphasis, never bouncing or wobbling. Coral periods animate as a hard pop on signature beats. Transitions are hard cuts or 6-frame dissolves only.
- [d81969febc9e] prefer specific numbers over vague claims
- [e1559d443197] prefer present-tense over future-tense
- [f380cff82f61] prefer "operator" over "creator", "infrastructure" over "agency"

## storyboard-architect/examples/30s-pain-proof-promise/storyboard.md

- [cb070662db9b] **Color grade** | warm filmic, muted teal shadows, slight grain, cream highlights, deep navy shadows never crushed
- [3361115a3c24] **Subject:** founder at laptop, scrolling social feed, content tiles glowing on screen, slight slump in shoulders, mug of coffee mid-distance
- [f3a0d5dd594d] **On-screen text:** "You don't have a content problem. / You have an infrastructure problem." (Inter Black 900, coral, center, type-on at 11.5s)

## storyboard-architect/examples/60s-founder-explainer/brand-lock.snapshot.md

- [905efed35c14] Role | Hex | Use
- [e10409cde634] never use stock photo aesthetic
- [5c3ec0c8cf75] never use AI uncanny faces
- [fef9fe44ef96] never over-saturate the cream background
- [4590b5aee804] never use coral as a flood color (only as accent or signature periods)
- [d40b84764301] never use em dashes in copy
- [478143da99e2] never use emojis in body copy
- [1bbba41d8f5e] never use bullet points in narrative copy
- [1249aae4215a] never use clip-art or generic icon sets
- [621b3df6eb6a] never use hype words ("game-changing", "revolutionary", "next-level", "comprehensive")
- [d9e264405291] never use exclamation points in headlines
- [64c7eedde7cc] never default to dark mode, light mode hybrid is the brand
- [38c7b73cec5b] never animate text with bouncing or wobbling, type-on, fade, or hard cut only
- [4b55ac47f0e7] Warm filmic, muted teal shadows. Slight grain. Cream highlights, deep navy/charcoal shadows, never crushed. Reminiscent of Kodak Portra 400 with a slight digital cleanup.
- [ff35cc7d69fd] Camera moves are minimal and deliberate. Default to static. When motion is used, slow push or slow pull only. Cuts on action, not on time. Type-on for emphasis, never bouncing or wobbling. Coral periods animate as a hard pop on signature beats. Transitions are hard cuts or 6-frame dissolves only.
- [995296a29fb4] prefer specific numbers over vague claims
- [db692e54505e] prefer present-tense over future-tense
- [5e4a95ec4d8c] prefer "operator" over "creator", "infrastructure" over "agency"

## storyboard-architect/examples/60s-founder-explainer/storyboard.md

- [d7aa7bcd6517] **Color grade** | warm filmic, muted teal shadows, slight grain, cream highlights, deep navy shadows never crushed
- [cab7b8309e7a] **Beat:** insight · **VO:** "Every brand has a voice. Most founders never extract it. So every post starts from scratch."

## storyboard-architect/examples/shotkit-explainer/brand-lock.snapshot.md

- [5566ff43eca7] Role | Hex | Use
- [929d3e62f0b7] never use stock photo aesthetic
- [c5761942f155] never use AI uncanny faces
- [f28e4507d045] never over-saturate the cream background
- [3751f321730f] never use coral as a flood color (only as accent or signature periods)
- [9132e55fcf5d] never use em dashes in copy (only periods, commas, semicolons)
- [0f628683c6b8] never use emojis in body copy
- [eff9c8392083] never use bullet points in narrative copy
- [b700cf8f4dcb] never use clip-art or generic icon sets
- [45e257d77c42] never use hype words ("game-changing", "revolutionary", "next-level", "comprehensive")
- [ddb048e79808] never use exclamation points in headlines
- [eb006504840c] never default to dark mode, light mode hybrid is the brand
- [783ff683393c] never animate text with bouncing or wobbling, type-on, fade, or hard cut only
- [8cea74bc14b1] never break the eye line between subject and the implied "operator perspective"
- [f6abdd226436] Warm filmic, muted teal shadows. Slight grain. Cream highlights, deep navy/charcoal shadows, never crushed. Reminiscent of Kodak Portra 400 with a slight digital cleanup. Skin tones warm but not orange. Greens kept slightly desaturated to push focus to subject.
- [d8a47abf50ca] Camera moves are minimal and deliberate. Default to static. When motion is used, slow push or slow pull only. Cuts on action, not on time. Type-on for emphasis, never bouncing or wobbling. Coral periods animate as a hard pop on signature beats. Transitions are hard cuts or 6-frame dissolves only, no fancy wipes, no zooms.
- [e9560a0de1ac] prefer specific numbers over vague claims ("48 hours" not "fast", "30 minutes a week" not "a little time")
- [cc0c55fe6755] prefer present-tense over future-tense
- [c1a8c5479b88] prefer "operator" over "creator", "infrastructure" over "agency", "system" over "service"

## storyboard-architect/examples/shotkit-explainer/storyboard.md

- [d14865cb6d2f] > matching the artifact it produced: editing it to describe a video that was never made is
- [35a8d9d8702e] **On-screen text:** "You don't have a content problem. You have a pre-production problem." (Inter Black 900, center, fade)

## storyboard-architect/references/beat-frameworks.md

- [7e5f2e473cd3] Pick one. Don't invent a new one unless the brief genuinely doesn't fit. Document the choice in `storyboard.md`.
- [f32c786bfbff] **Pain**, name the audience's actual problem in their actual language. Concrete, not abstract. "Your content feels random" not "marketing inefficiency."
- [d329c7d38124] **Reframe**, flip the problem on its head. The point is *not* what they thought it was. "You don't have a content problem. You have an infrastructure problem."
- [b55cf418fc3a] **Promise**, what life looks like on the other side. Specific, verifiable, time-bound when possible.
- [e5235864c6bb] Use when: ad creative, landing-page hero video, conversion-focused social.
- [0206d6df0cc3] **World**, set the context. Who lives in this world. What's broken about it.
- [9b3fba335e1b] **Hero**, the product/founder/methodology arrives. Show what it does, not what it is.
- [e4b20db35b44] **Transformation**, the world changes. Show before/after at scale.
- [cfaecb7f5fa7] Use when: product launches, brand films, anchor pieces.
- [39b17554140c] **Hook**, a one-line provocation (0–2s)
- [ec4f8b7428c7] **Stakes**, why this matters (2–8s)
- [3bdf77c5a1e7] **Insight**, the actual point (8–20s for 30s, 8–40s for 60s)
- [6154ed831bf3] **Proof**, one concrete example or data point
- [6be1e3549be6] **CTA**, what to do next, narrow and specific
- [ca19a04f7f16] Use when: founder content, thought leadership, personal-brand pieces.
- [e707043ad741] **Wide claim**, the headline take
- [61117f1e1435] **Zoom 1**, one layer of nuance
- [bcd48bb1ab67] **Zoom 2**, the layer underneath that
- [409a346f14c6] **Snap-back**, return to the wide claim, now reframed by the zooms
- [e4456cb5dc55] Use when: opinion videos, kinetic-type pieces, social-native commentary.
- [86733dae8e0e] **Problem state**, what someone is stuck on
- [4b795000d239] **Reveal**, the technique or trick
- [a68a06f84fe6] **Walk-through**, apply it step by step
- [0357fe063806] **Result**, the after-state, side-by-side with before
- [08af446ba369] Use when: tutorials, demo videos, training content.

## storyboard-architect/references/on-screen-text.md

- [428f5eebff7b] Text on screen is a load-bearing decision. Most storyboards over-text. The default should be: **does this shot need text to land?** If the visual carries the meaning, text dilutes.
- [a268ba75d0b5] **Auto-play-mute environments.** Social feeds. Text replaces VO.
- [efdeec778e0f] **Concept compression.** A short phrase lands harder than 4 seconds of narration.
- [90221fe5fe0f] **Stat or proof point.** Numbers stick visually in a way they don't audibly.
- [48c59084ee78] **Beat punctuation.** A single word or phrase that lands on a music hit.
- [9f529931cccc] **CTA.** The action you want the viewer to take.
- [c1fb4192e05a] **Restating the VO.** If the voice says it, the text is noise.
- [84655e935767] **Decorative copy.** "Moments matter" floating over b-roll. Cut it.
- [84f1791a022e] **Brand vibing.** Product names everywhere. Logo lockup in the CTA covers this.
- [67f2beaeb3ef] **Filler beats.** If the shot doesn't need text, leave it clean.
- [4ff066eab26b] When a shot has on-screen text, the **shot subject must reserve space for it**. This is enforced at storyboard time, not generation time.
- [a526c207e3dc] Position | Use when
- [7a7cb7a4a5e8] `{x: %, y: %}` | Custom, only when the standard positions don't fit
- [4a432ad00196] Size | Pixel approx (1080p) | Use for
- [9f4f78bc99a2] Avoid stacking animations. Pick one per overlay.
- [4cbacbc0b8fa] The `color` field of every text overlay must be a hex value that exists in the brand-lock palette. If you find yourself wanting a color that's not in the palette, the answer is not to add it, the answer is to pick a different overlay style or shot composition.
- [d7940c08b552] Same: every `font` field must reference a font defined in brand-lock typography. Two fonts max per project (display + body). More than that and the brand stops being recognizable.
- [717463d29f8f] Already covered in timing-rules.md but worth repeating: text needs to be on screen long enough for someone to read it twice. Calculate, then verify. Don't eyeball.

## storyboard-architect/references/shot-grammar.md

- [7268a7328d89] Controlled vocabulary. Use these exact terms in `shots.json`. Generators interpret loose language inconsistently, locked vocabulary survives translation.
- [74926ea5bff7] `MCU` | Medium close-up | Head and shoulders
- [6b3fa7bb2923] Default to eye-level. Use the others deliberately, not for variety.
- [7faa95961da0] Code | Effect | Use when
- [5528555145f9] `shallow` | Subject sharp, background blurred
- [e4e41d7c48e9] Default to shallow for talking-head, deep for environmental and schematic.
- [03a00602482e] Don't redefine per shot. Define once in `series_lock.lighting`. Examples:
- [05f30ccb87c3] **brand_lock**, locked across the entire project. Palette, type, "never" list.

## storyboard-architect/references/timing-rules.md

- [22f6035ce704] Pacing is math, not feel. Use these as defaults. Override only with reason documented in rationale.
- [32344b412ad5] The hook is 0–2s. Always. There are no exceptions in short-form content. Specifically:
- [e67edc98e31f] 9:16 social: first frame must telegraph the topic. Auto-play on mute means the first half-second is fighting a swipe.
- [5e8113658ff6] The hook shot framing should be high-contrast against the shots that follow. If shot 2 is MS, shot 1 should not be MS. Visual contrast = retention.
- [7e40e9d57114] Last shot should hold long enough for someone to read the CTA text and act
- [5acc0a53e64b] Don't put motion on the CTA shot, let the text breathe
- [8499e1ad407c] A text overlay needs to be on screen long enough to be **read twice**. Not once, twice. Why: viewers are skimming, eyes don't always lock on first frame.
- [8a7cde5fbf44] Shorten the copy
- [1740a84f47a3] Carry the text across two consecutive shots (text persists during cut)
- [6c398f45603b] Lengthen the shot
- [6c97051eb055] Do not under-time text. It's the most common storyboard failure.
- [e7f6806c93e3] Sum of `(end - start)` across all shots equals project duration ±0.1s
- [35389a2e7e9a] No shot has `start >= end`
- [993e2cd1eec5] No two shots overlap
- [40867e840a40] First shot starts at 0.0
- [e620d729b974] Last shot ends at project duration
- [0678f6cbf749] Every text overlay's `enter.at` is ≥ its shot's `start`
- [5d267e42e94d] Every text overlay's `exit.at` is ≤ its shot's `end` (or carries to a flagged successor shot)
- [18b6449fb38c] Every text overlay's on-screen duration ≥ read-twice threshold