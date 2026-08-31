# Reglas del skill: visual-asset-critic

55 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## visual-asset-critic/SKILL.md

- [a9db0e982fb0] You are the editorial second-eye on AI-generated images. Most teams don't have one, they generate, glance, accept, and ship. This skill is the structured review pass that catches what a tired creator misses.
- [6692ef7502cf] Says "review this render", "is this on-brand", "what should I change"
- [1dc7c87def16] **Two artifacts from every review, always both:** a human-readable markdown critique (the primary surface) and a machine-readable critique JSON (so a pipeline can gate on the verdict instead of parsing prose). The JSON is detailed in Step 6; it never replaces the markdown.
- [331ea8b0b15b] per round, never a shared filename. A 12-shot project reviewed over three rounds writes 36
- [c174e00adaac] Shot ID + shots.json | Recommended | If absent, ask for shot intent in a sentence
- [92d3adf53086] brand-lock.snapshot.md | Recommended | If absent, critique only on technical merits
- [c8195d96aaff] If you can't establish intent in one sentence, ask. Don't critique blind.
- [0aebfb67e4fd] **Brand Lock**, does it respect palette, mood, "never" list?
- [3236a31aecea] **Series Lock**, does it match character/environment/lighting anchors?
- [79f9fd6178a0] **Shot Spec**, does framing/angle/composition match the spec?
- [024638f7f93d] **Composition**, does it reserve space for on-screen text if applicable?
- [d0476aaa14d5] **Technical**, skin texture, hands, eyes, anatomy, AI artifacts?
- [4254cbeb01a9] **Continuity**, if previous shots in the series are available, does it match?
- [4dabd7bdc618] For every "not working" point, the critique must say what to do about it. Three buckets:
- [c6c6b48f5a57] > "Color grade is slightly cool, push warmth +5 in post, no need to re-generate."
- [7eac9caa0ac8] **Re-roll required**, no prompt fix will help; the generator just produced a bad sample. Budget 2–3 attempts:
- [c24705b39ede] **Provenance, all of it required at 1.1.** A verdict is a claim about specific bytes. Name
- [110d5c828282] Every one of those fields is required, and every one is nullable. That combination is
- [e182afdf2371] your confidence to MEDIUM. Do not omit the key.
- [fd33b1fe4a83] **Gating rule, the verdict is derived from severities, not chosen freely.** This guarantees the markdown verdict and the JSON verdict always agree:
- [c7b224344104] fixtures that ship in the repo and never once against a real client's critique.
- [583d5f400a46] "Looks great" / "feels off" without specifics is not a critique. Every observation must reference something in the image (composition, color, anatomy, lighting direction, etc.).
- [0cde22e1a93c] If the brief was "founder at laptop, calm mood" and the generation delivered exactly that, don't note that "the room could be more visually interesting." That's scope creep, not critique.
- [5b837820df26] Some failures (mangled hands, weird eye reflections, jewelry shimmer) are known generator weaknesses. Surface them as such, don't pretend a different prompt will fix them. Recommend re-roll or post.
- [a221a716e952] Generation is one stage in a pipeline. If the image is 80% right and the gap is fixable in post, that's an ACCEPT with post notes. Don't send the user back to re-generate when an editor would handle it in 90 seconds.
- [87d7e03eed3d] > - **Hand:** Re-roll required. Generate 2–3 more times with same prompt and pick a clean one.
- [65ab63f3291c] If the verdict is REJECT, do not offer that. REJECT means a blocking issue or three or more
- [c7b95c733b7f] Don't auto-revise. The user picks. The critique you just wrote is exactly what closes that

## visual-asset-critic/examples/worked-run/brand-lock.snapshot.md

- [0ab5724633a2] Role | Hex | Use
- [147b5d10f118] never use stock photo aesthetic
- [edb34335baee] never use AI uncanny faces
- [36f326b4fa1b] never over-saturate the cream background
- [6fcfbe5ad699] never use coral as a flood color (only as accent or signature periods)
- [e3d69437c2f6] never use em dashes in copy
- [ff2826465af1] never use emojis in body copy
- [bd1590a213fe] never use bullet points in narrative copy
- [cf3ce4e1adaf] never use clip-art or generic icon sets
- [2ef7c79850da] never use hype words ("game-changing", "revolutionary", "next-level", "comprehensive")
- [5d8f1227d198] never use exclamation points in headlines
- [b1bf8c0bd438] never default to dark mode, light mode hybrid is the brand
- [2306baa11deb] never animate text with bouncing or wobbling, type-on, fade, or hard cut only
- [c2fbf1d46956] Warm filmic, muted teal shadows. Slight grain. Cream highlights, deep navy/charcoal shadows, never crushed. Reminiscent of Kodak Portra 400 with a slight digital cleanup.
- [8cb896ae3ca7] Camera moves are minimal and deliberate. Default to static. When motion is used, slow push or slow pull only. Cuts on action, not on time. Type-on for emphasis, never bouncing or wobbling. Coral periods animate as a hard pop on signature beats. Transitions are hard cuts or 6-frame dissolves only.
- [a3fa0f352d46] prefer specific numbers over vague claims
- [c1ee0d0b5a80] prefer present-tense over future-tense
- [650d25a8d091] prefer "operator" over "creator", "infrastructure" over "agency"

## visual-asset-critic/references/critique-rubric.md

- [00c742ccd1e6] The structured layer-by-layer pass. Use this as the checklist when reviewing a generated image.
- [bf46e2f0044e] "Never" list | None of the items in the never list are present | One item in the never list shows softly | Multiple never-list violations
- [7713f2e95b09] Depth of field | Matches if specified | Slight DOF variation | Deep when shallow was specified
- [1e898f2c0308] Technical hard fails are almost always **re-roll required**. The prompt was probably fine; the generator just produced a bad sample. Budget 2–3 re-rolls.
- [31afcb61a699] Soft fails are noted but don't change the verdict on their own. If you have three or more of
- [788f1a8f5595] **Don't critique what wasn't asked**, if the spec didn't call for cinematic mood, don't say "could be more cinematic"
- [8014a721e61b] **Don't pile-on once verdict is set**, if you're rejecting, list the issues that drive the rejection; don't list every cosmetic concern
- [9b616f961fba] **Be specific, always**, "lighting is off" is not a critique; "key light is camera-right but series_lock says camera-left" is
- [b1bf47b129ef] **Distinguish prompt failure from generator failure**, if the prompt was fine and the generator produced garbage hands, that's "re-roll required", not "fix the prompt"