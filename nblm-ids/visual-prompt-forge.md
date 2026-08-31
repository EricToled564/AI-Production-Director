# Reglas del skill: visual-prompt-forge

172 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## visual-prompt-forge/SKILL.md

- [73fe57cd2392] If the user wants to build a storyboard from scratch (no shots.json yet), use `storyboard-architect` first, then chain into this skill.
- [30bbbcefca75] **Brand Lock**, palette, type, mood, "never" list (constant across project)
- [3a6fba22ac13] **Series Lock**, character/environment/lighting anchors (constant across storyboard)
- [ea1a9a227c90] **Shot Spec**, framing, angle, motion, subject (per shot)
- [d584b5f6dd31] **Text Layer**, **never in the prompt**, composited separately
- [2ad7d2bd5837] **Generator Adapter**, model-specific syntax wrapper
- [676d83318ba4] `shots.json` (required), the structured shot list
- [15c8b7599336] `brand-lock.snapshot.md` (required), referenced from shots.json
- [2266a36b9924] Target generators (required), ask if not specified
- [ceadbe55c7f7] Don't try to forge prompts from incomplete data.
- [f5780b83a7fd] relative path only resolves when the skills sit side by side; when they don't, ask the
- [409086978069] Each adapter file documents the prompting style, parameter syntax, and known pitfalls for that generator. You **must** read the adapter before writing prompts for it. Don't guess from training data, image-gen syntax has churned multiple times.
- [dc64b62d7b53] **`adapters/_capabilities.json` is the single source of truth for per-generator limits** (`max_prompt_words`, `supports_text_render`, `supports_motion`, `aspect_param`, and so on). Read it once at the start and respect those values when composing, and do not target motion on a stills-only generator.
- [c8ca9f7ecf45] `max_prompt_words` is a ceiling. The range in an adapter `.md` is the recommended target
- [f839d2e13059] and always sits inside that ceiling, so a `.md` saying "40 to 70 words" under a ceiling of
- [926849d6c818] build when an adapter advertises more words than its ceiling, or when an adapter never
- [f5131460c877] Pull brand-lock palette, mood, "never" list
- [7405b4323a06] Pull series_lock character/environment/lighting
- [31c852fadeeb] Pull shot framing/angle/motion/subject
- [a8d68a296084] **Strip any on_screen_text reference**, text never goes in the prompt
- [2b9195a30710] Apply the generator adapter's syntax wrapper
- [2b8a535c5cf5] Append generator-specific parameters (aspect ratio, style flags, seed if applicable)
- [5d8272012767] > "Want me to QA the generated images against the storyboard? Use `visual-asset-critic` once you have the renders."
- [f40b417305f5] This is what `visual-asset-critic`'s structured output is for. When the user hands you `shots.json` plus one or more `critique.json` files (the machine-readable verdict the critic writes), don't re-forge the whole storyboard, re-emit prompts for **only the shots that failed**, with the fix already applied.
- [f967955038f5] Read every critique under `output/critiques/round-{N}/`, where N is the highest round
- [8094567ba7ff] Skip any with `verdict: ACCEPT`. Those are done.
- [da7ec8955918] **Stop on `REJECT`.** A REJECT means the critic found a blocking issue, or three or more
- [5854e254d91b] For every `REVISE` shot, walk its `issues[]` and branch on `fix_type`:
- [1bd4b3b2da0d] A shot whose issues are all `post-level` needs no new prompt. Leave it out of the
- [67742a174a9f] Saying it in chat is not recording it: that obligation has to exist on disk or the
- [a3656615b59b] Re-apply the five-layer anatomy and the same adapter as the original run.
- [faee36ed7238] Given the same `shots.json`, the same brand-lock, and the same critique, this should
- [24d0e917035e] Colors come from the series_lock color_grade and the brand_lock palette. They get rendered into the prompt by the adapter. Don't write "deep navy blazer" in the shot subject if "deep navy" is already in the palette, that's a duplicated description and produces oversaturation.
- [80fc570bbe52] side-by-side: the six stills generators plus Kling. Use it to calibrate output quality.

## visual-prompt-forge/adapters/flux.md

- [07934feae2b7] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [4a9a9f1d1b5a] Flux handles **80–150 words** comfortably. Don't pad, but you have headroom Midjourney doesn't.
- [cf6ea7ae4157] `shallow DOF` | `Shot at f/1.8 with shallow depth of field, background softly out of focus.`
- [90c1b290af77] **Don't write "highly detailed, 4k, masterpiece"**, these are Stable Diffusion crutches. Flux ignores them and the line burns tokens
- [c55494cbbad4] **Don't use weight syntax `(thing:1.4)`**. Flux 2 doesn't support it; Flux 1.1 partially does. Stick to natural language
- [0447e389826e] **Don't enable prompt upsampling for series work**, fal.ai's auto-rewrite produces inconsistent shots
- [d070363f06ff] **Don't include text content**, even if Flux 2 handles text better than Flux 1.1, composite separately for editability
- [bc7cb8df5ee2] **Don't omit the photoreal closing line**, the "no AI artifacts" anchor measurably reduces the AI-look

## visual-prompt-forge/adapters/gpt-image.md

- [b107310048f9] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [3e22b4c62b1b] GPT Image handles **150–300 words** comfortably. Longer than other generators. Use the headroom for explicit spatial descriptions.
- [4e37b6108b10] "The subject's shoulders are angled 30 degrees toward the camera, face turned to look at the off-frame light source."
- [20ebea9d8a54] Use this when the shot's composition is load-bearing.
- [226a236b4dcc] GPT Image handles text-in-image at roughly 95% accuracy, second only to Ideogram. When text is required:
- [fd93590ae5d9] **Don't write Midjourney-style comma stacks**. GPT Image parses them as a list of disconnected concepts
- [b5fa2fb924bd] **Don't omit spatial language when the shot has specific composition**, you're paying for the model's strength; use it
- [e1f3ed8e587b] **Don't pile too many objects**, five or fewer distinct elements per scene; more degrades fidelity
- [a6bec722c41f] **Don't include `--ar` flags or weight syntax**. GPT Image ignores them
- [d4f119799fc1] **Don't forget that GPT Image's "AI look" is real**, the closing "natural skin texture, no AI rendering artifacts" line meaningfully helps but isn't a complete fix. For pure photoreal, Flux is still stronger

## visual-prompt-forge/adapters/hailuo.md

- [06dd78348fae] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [c72b6be12f5a] Hailuo 02 Pro is the cheap, fast iteration model. Strong motion response and prompt-following for the price, on fal.ai. Use it to **find the shot**, block out camera move, framing, and timing across many quick drafts, then re-generate the keeper on Kling (motion finals), Veo (dialogue), or Seedance (sequences). Treat Hailuo output as a working draft, not a final asset.
- [19e3c8f16aab] Draft the shot on Hailuo with `prompt_optimizer=false`. Cheap, fast.
- [135bf9bbfea0] Lock the camera move, framing, and timing that read best.
- [71c8ecef7358] Re-generate the keeper on the right final-tier model: **Kling** for motion finals, **Veo** for dialogue/lipsync, **Seedance** for multi-shot sequences.
- [e78a9329a596] Carry the exact prompt forward, the adapters share the same five-layer anatomy, so the prompt body ports with only parameter changes.
- [2331185c4bd4] **Don't ship Hailuo drafts as finals.** Re-roll the keeper on a final-tier model.
- [a5926981e848] **Don't enable the prompt optimizer for series work.** Auto-rewrite breaks shot-to-shot consistency.
- [c52dc68d0daf] **Don't stack two camera moves.** One move per shot.
- [4755505de7d6] **Don't include text content.** Composite captions in post.
- [cfc2cee4d758] **Don't over-polish the draft prompt.** Spend words on motion and framing; save the photographic detail for the final-tier re-roll.

## visual-prompt-forge/adapters/ideogram.md

- [62285c31f534] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [fdc0e542eefc] Ideogram is the only generator that reliably renders text inside images. Use it for cases where text-as-image is the deliverable, posters, branded social tiles, signage, packaging mockups. For everything else, default to Flux or Midjourney and composite text separately.
- [580aeac4bce0] Same as Flux, generate the image clean, composite text in post. Use when Ideogram is being chosen for general image quality, not text rendering. Syntax matches Flux conventions.
- [88ac8d8506e0] Use when the on-screen text is meant to appear as part of the image itself, a poster headline, a sign in the scene, a packaging label. This is the only case where a generator prompt contains the text content.
- [6fe6a8f5491e] **To trigger Mode 2, the shot must have an explicit override flag in rationale**, e.g.:
- [8601bfd0e280] If you don't see that override flag, default to Mode 1.
- [73aaed94b890] The exact text must be in straight double-quotes. Ideogram parses these as the text-render target.
- [997a8c1f12f1] **Don't use Mode 2 without the rationale override**, defaults to text-in-image cause double-text (composited + generated) which destroys the comp
- [8ad2673a7cf6] **Don't trust magic_prompt**, it auto-rewrites and produces inconsistent shots across a series
- [83c574fc9ce5] **Don't pile multiple text elements in one prompt**. Ideogram handles one text element well, two becomes lottery, three is broken
- [e0e022e50a9e] **Don't use cursive/decorative fonts**, even Ideogram fails on these. Sans-serif and clean serif are reliable
- [22d09b130cbd] **Don't forget seed**, for any series work, lock the seed at the storyboard level

## visual-prompt-forge/adapters/kling.md

- [278af9f8d903] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [0df53c838f6c] With video the **camera motion becomes load-bearing** instead of optional. The same shot generates differently when `motion` is `static` versus `push` versus `handheld`. Use this adapter when the storyboard is destined for video generation rather than still-frame compositing.
- [34c9774072b9] Camera motion goes **first**. This is the inverse of image generators where camera is implied. With video the camera's behaviour is the first thing the model must understand.
- [a96d5275630a] `negative_prompt` | per series | Supported. Use to suppress drift, e.g. `extra fingers, warped face`
- [c05a37e6c694] Kling handles **80–150 words** comfortably. Motion description adds a beat over a still prompt; do not pad past it.
- [dd11b5da1036] Use `start_image` from the previous shot's accepted final frame to chain a sequence.
- [1e43dbde9ec3] Do not flip lighting direction between consecutive shots (window-left stays window-left).
- [5996725c4119] **Don't put camera motion at the end.** Kling parses motion best as the leading instruction.
- [28b092664be0] **Don't request multiple camera moves in one shot.** Pick one; compound moves break.
- [9d51ba168710] **Don't describe motion faster than the duration allows.** A slow dolly over 5s is plausible; over 1s it is jitter.
- [3d67beea0470] **Don't include text content.** Video text rendering is unreliable; composite or animate text in post.
- [cbb479ac1517] **Don't expect frame-perfect character match between clips.** Budget editorial cleanup.

## visual-prompt-forge/adapters/midjourney.md

- [397cf2e63aa9] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [6d613697ccf2] Param | Values | Default to use | Notes
- [7fb6a50cd854] `--c` | 0–100 | omit | Chaos. Use only when exploring variations
- [d32ed6a243e7] `--cref` | image URL | use when character anchor exists | Character reference. Pair with `--cw`
- [211d04720fee] `--sref` | image URL | use when style anchor exists | Style reference
- [35ad63b182a1] `shallow DOF` | `shallow depth of field, f/1.8, bokeh background`
- [c51e98883ae8] **Don't use "AI" or "rendered"**, produces stylized outputs that look generated
- [e6bae7347048] **Don't over-stack adjectives**, three adjectives per noun phrase max
- [f85b78ac44b0] **Don't include text content**, even if the shot has `on_screen_text`, leave it out. Composited separately.
- [8452bcb3abe4] **Don't use `--c` for series work**, chaos kills consistency
- [3ac7c1186c62] **Don't change `--seed` mid-storyboard**, set once at series_lock level
- [bae5480432cd] Midjourney still has limited API access as of Q2 2026. For programmatic workflows, the prompts in `midjourney.txt` are designed to be pasted into Discord or the web UI. Some teams use third-party wrappers (PiAPI, Useapi.net), those generally accept the same prompt syntax.

## visual-prompt-forge/adapters/nano-banana.md

- [d19b5afba806] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [512c6518fda5] Google's Nano Banana model (`gemini-2.5-flash-image`) is the edit-and-iterate champion. Where other generators are best for first-frame creation, Nano Banana excels at variations, inpainting, and reference-based modification. The 2026 production pattern is to generate hero frames in Midjourney or Flux, then use Nano Banana for variants.
- [f3de59067b61] **Use case:** generated `shot_03` in Flux, want a variant where the founder is looking directly at camera
- [143dc2890227] Generate hero shot in Midjourney or Flux (one prompt → one image)
- [d5bfa09e50d2] Feed that image to Nano Banana with variation prompts
- [cc8441e81dd6] Get 4–8 variants of the same shot for editorial selection
- [90a27f197867] Composite text on the chosen variant
- [2b0600ce9bc0] A modification template comment showing how to use the result for variants:
- [43331142e7ea] **Don't use Midjourney-style flag syntax**. Nano Banana ignores `--ar`, expects `aspectRatio` parameter
- [c169c881a0e6] **Don't expect Midjourney-level aesthetic by default**. Nano Banana is a workhorse, not a stylist. Stack mood adjectives explicitly
- [03aa46d144b5] **Don't pile multiple modifications in one image-to-image prompt**, one change per pass produces cleaner results
- [c4812cc96bc2] **Don't forget the "preserve" clause in image-to-image**, without it, Nano Banana treats the reference as loose inspiration and drifts
- [5fc1cc954fb0] **Don't include text content in image prompts**, composite separately; text rendering is mediocre

## visual-prompt-forge/adapters/seedance.md

- [6930bdd3fefe] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [941f9d967144] One beat, one frame | Single shot (or use Kling)
- [07771e486a77] **Don't force unrelated beats into one sequence.** Multi-shot is for shots that genuinely belong to one take.
- [cee8c4cd6183] **Don't write more than ~4 cuts per generation.** Consistency degrades past that; split and assemble in edit.
- [e84b5c0448b9] **Don't vary the character anchor between cuts.** Restate it once for the whole sequence, verbatim.
- [98d91e461feb] **Don't include text content.** Composite captions from `text-overlays.json` in post.
- [750cf06a6b5c] **Don't stack two camera moves inside one cut.** One move per cut.

## visual-prompt-forge/adapters/seedream.md

- [033510e42dcb] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [5c181b49f9d4] **40–70 words per prompt**. Shorter than most. Don't pad.
- [b58550816f3f] **Don't vary** the lighting language between shots, series_lock string in, no paraphrasing
- [735b1edeccc3] **Don't write paragraphs**. Seedream wants comma-separated phrases
- [8c221aa40298] **Don't use `--ar` syntax**, pass aspect_ratio as a parameter
- [679f8c322dba] **Don't include text content**, text rendering is poor; composite separately
- [3de5ebeb511c] **Don't expect Midjourney aesthetic**. Seedream produces clean but less art-directed output
- [14306fa1f1c7] **Don't skip the seed lock for series work**, without it, character consistency breaks

## visual-prompt-forge/adapters/veo.md

- [d992a5044ff9] > Capability data (length ceiling, text/motion support, aspect param) is canonical in `_capabilities.json`. This file is the how-to-prompt guidance. `max_prompt_words` there is a ceiling; the range below is the recommended target and has to sit inside it. Where a fact here and a fact in the JSON disagree, the JSON wins, and `tools/validate_capabilities.py` fails the build instead of letting the tw
- [05691c5685fb] **Don't use Veo for silent B-roll.** You are paying for an audio engine you turned off; use Kling.
- [c962c96606da] **Don't overrun the duration with dialogue.** A line that needs 12s of speech will clip or rush at 8s.
- [1087e186fed5] **Don't put on-screen text in the prompt.** Spoken lines are fine; rendered captions still come from `text-overlays.json` in post.
- [0acb882ac4aa] **Don't stack two camera moves.** One move per shot.
- [561e4601866e] **Don't let Veo's auto-audio fight a post audio bed.** Pick one owner of sound per shot.
- [93e1dbd6d5ab] Veo clips arrive with audio attached. They still need: editorial assembly to timing, on-screen text compositing from `text-overlays.json`, a color-grade pass, and an audio decision, keep Veo's native track, or mute it and use the storyboard's recorded VO and music. State which in handoff.

## visual-prompt-forge/examples/one-shot-all-adapters/README.md

- [4227374e4dd2] This example takes a single shot from the WhyStrohm 30-second pitch and renders it through the generator adapters in the pack. Use it as a calibration reference: same intent, same data, different prompt syntaxes. Six stills adapters are shown, plus the default motion adapter (Kling) standing in for the motion video lane.
- [4f3b139befa2] The on-screen text content. Even though shot_04 has an on-screen text overlay (`text_03`, "You don't have a content problem. You have an infrastructure problem."), none of the prompts contain that text. It's composited separately per the five-layer model.

## visual-prompt-forge/references/consistency-locks.md

- [00ad95b7807d] Same principle for `series_lock.lighting`. Lighting direction in particular is critical, flipping window-left to window-right between shots produces obvious cuts where there shouldn't be any.
- [199cfb9ab91d] Generate the hero shot first (any shot, usually `shot_01` or whichever is most defining)
- [b2e806d6105a] Use that image as the reference for every subsequent shot
- [14c534d5e7f2] Each subsequent prompt has the verbatim character anchor PLUS the reference image link
- [926508430703] **This is the most effective lock for character consistency** in 2026. Use it whenever the storyboard features the same person across multiple shots.
- [a0d393395e3a] When the storyboard has a distinctive visual style (specific film stock, specific lighting school, specific color theory), use a style reference image:
- [4140ed69949c] A subtle one that breaks scenes when violated. If `series_lock.lighting` says "soft natural side-light, large window LEFT", then every shot's lighting must respect that direction.
- [20b3434a9a5d] When a shot reverses character orientation (e.g., over-the-shoulder reverse), update the rationale to acknowledge the lighting flip:
- [3b984b2349a3] A few things people try that don't actually fix consistency:
- [0f136ad02a4a] **Adding "consistent character" or "same person" to the prompt**, generators don't read meta-instructions
- [985e93f22844] **Numbering shots in the prompt** ("shot 3 of 7, same as before"), generators don't have memory across calls
- [dd6e04a7a56e] **Asking for "exactly the same"**, there is no such thing in stateless image gen; you reduce drift, you don't eliminate it
- [bfb6f1d9e6b2] Accept that some shots will need re-rolls. Budget for it. The locks reduce the failure rate; they don't eliminate it.

## visual-prompt-forge/references/failure-modes.md

- [3613e7f4cf02] What goes wrong when generated images don't match the storyboard, and what to fix at the prompt level vs. accept as editorial work.
- [b70a07474b42] No "never" list applied from brand-lock
- [2757ce63d7e2] Verify brand-lock "never" list is being applied, if it includes "no AI uncanny", surface that into the prompt
- [8f8dc623566a] Use Flux 2 Pro or Midjourney v7 instead of cheaper models for hero shots
- [b826ad9667a2] Use reference image after the first successful shot
- [717c03da642d] For Midjourney, use `--cref` with `--cw 50`
- [6447bec15b56] The right answer is almost always: **don't put text in the prompt**. Composite separately from `text-overlays.json`.
- [359736f73561] If text must be in-image (poster work), use Ideogram v3 with explicit override flag
- [5945d25c9b90] Use simple fonts (sans-serif, clean serif), cursive and decorative fonts fail even on Ideogram
- [ecb6a8e221f1] For GPT Image (best at spatial reasoning), use percentage references: "subject at left 30% of frame"
- [982752f60d62] **Accept editorially when:** generation is close enough that retouching gets there. Don't burn API credits chasing perfect on-prompt.
- [1f983ff0ee18] You've re-rolled the same shot 5+ times with no improvement → the prompt is fine; the model can't render this concept; pick a different shot or different generator
- [12009aa60167] You're tweaking single words and hoping → you've hit prompt-level diminishing returns; move to image-to-image refinement (Nano Banana) or post-production
- [4be94337bb02] The image is 80% right and the gap is editorial → ship to post and let the editor finish
- [33fc833724e0] Generation is one stage in a pipeline. Don't try to make it the whole pipeline.

## visual-prompt-forge/references/prompt-anatomy.md

- [bcaac139f9b7] "Never" list (things this brand never does, e.g. "no stock photo aesthetic", "no AI uncanny", "no over-saturated", "no shouting copy")
- [e95be207e462] This layer answers: **what does the brand always look and feel like?**
- [67037c4b307e] **Never appears in image prompts** (except Ideogram Mode 2 with explicit override).
- [e177c4f10a04] **Editability.** Composited text can be revised without re-generating images.
- [4c22b71ebf0a] **Quality.** Even Ideogram and GPT Image (the best at text) produce typography that lags professional design tools.
- [5f5e6ee4ad91] **Animation.** Animated text needs After Effects / Remotion / CapCut. Static rendered text is dead-on-arrival for motion content.
- [05efedce58b5] **Brand control.** Composited text uses exact brand fonts and exact brand colors. Generated text approximates.
- [c8d6aa0aff0b] The adapter pulls from Layers 1–3 and produces a string. Layer 4 lives parallel and never enters the prompt.