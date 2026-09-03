# Reglas del skill: ai-video-storyboard

35 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## ai-video-storyboard/SKILL.md

- [eb02f32299e5] **Core insight:** Visual consistency across shots matters more than any single shot being perfect. A mediocre but consistent set of shots edits together; six gorgeous but mismatched shots do not.
- [962fd158c1b1] **Do NOT use for:**
- [fe59b8611a5b] **Goal platform and duration?** (TikTok 30s / Reel 15-60s / YouTube Short / Instagram Ad / explainer)
- [4a161f379427] **What is the video about?** (subject, story, product)
- [53a3fb486be4] **Brand vibe / tone?** (cozy, energetic, premium, minimalist, playful, cinematic, etc.)
- [0a4395028757] **Call to action at the end?** (visit website, buy product, follow channel, etc.)
- [375413fbe1a3] **Any hard constraints?** (must include logo, specific colors, locations, etc.)
- [658b20f679d9] **Lens character** (shallow DOF / deep focus / wide angle distortion / macro)
- [ce8831e8984c] Write these as a **Visual Theme** block at the top of the output. Every shot's prompt must respect this block.
- [68f234798bd5] **Always specify the shared visual language** in every prompt (color palette, lighting, lens character, film look). This is how you enforce consistency.
- [87680002b885] **Specify exact duration** (4s / 5s / 8s) and **aspect ratio** (9:16 for TikTok/Reels, 16:9 for YouTube landscape, 1:1 for feed posts).
- [097929817bc7] **Always end with "cinematic 1080p, synchronized audio"** — this signals professional-grade quality and works with modern video models that support both.
- [79369bcf16d4] **Use cinematography vocabulary**: ECU (extreme close-up), CU, MS (medium shot), WS (wide shot), OTS (over-the-shoulder), POV, Dutch angle, low angle, high angle, bird's eye, dolly in, dolly out, tracking, handheld, rack focus, etc.
- [3dde58c707c6] **Don't write abstract prompts** — be concrete. "A woman" → "A barista in her late 20s with wavy auburn hair, wearing a denim apron".
- [60f13533c38e] **No model-specific hacks** — don't write prompts tuned to specific model quirks. Write model-agnostic cinematic prompts that work anywhere.
- [c04789da6e17] The sequence of shots must have a **story arc**, not a random list. Use one of these patterns:
- [f136c00c3d59] **Header** — Title, duration, shot count, aspect ratio
- [f44cf9ff7226] **Visual Theme** — Shared palette, lighting, lens, film look, motion
- [5598ee94689f] **Shot List** — N shots, each following the structure in Step 4
- [b08dd9e82d1c] **Post-Production Checklist**
- [ab3cc98cbe7f] **Why This Works** — creative rationale
- [8a413ce6fe28] MIT — use freely, commercial or personal.

## ai-video-storyboard/examples/tiktok-reel-30s-coffee.md

- [39512433dfc7] **Lens character:** Shallow depth of field, gentle bokeh, 35mm full-frame look
- [ca2cb60ffbf7] > Extreme close-up overhead shot of hot water pouring from a brass gooseneck kettle into a white ceramic V60 dripper filled with dark coffee grounds, the grounds blooming and rising in slow motion, warm golden backlight with visible steam curling upward, shallow depth of field, 35mm full-frame look, subtle 16mm film grain, deep espresso brown and cream color palette, muted saturation, cinematic 10
- [017d7bcfc4cf] > Medium wide shot slow dolly forward into a cozy specialty coffee shop interior, warm morning sunlight streaming through large windows on the left, reclaimed dark wood counter in sharp focus with shelves of handmade ceramic mugs blurred in background, dust motes visible in sun rays, muted sage green wall accents, shallow depth of field, 35mm full-frame look, subtle film grain, warm 3200K color te
- [7dc3223937b9] > Medium close-up slightly low angle of a female barista in her late twenties with wavy auburn hair tied back, wearing a denim apron over cream linen shirt, standing behind a dark wood café counter, soft window light from the left creating warm rim light on her hair, she looks down at a pour-over coffee in her hands then slowly looks up at camera with a genuine small smile, shallow depth of field,
- [b8d91aaa1e04] > Macro extreme close-up of a hand scooping whole dark roasted coffee beans from a burlap sack into a small wooden measuring cup, slow motion cascade of beans spilling out as the hand tips the scoop, warm directional window light from upper right creating strong shadow depth, individual beans visible in sharp detail, shallow depth of field, deep espresso brown and burlap cream palette, subtle 16mm
- [69193134c05e] **Purpose:** Show the space in use. Aspirational — "this could be you."
- [92efe93b2278] **Composition:** Medium shot (MS), over-the-shoulder angle (OTS)
- [498de0013578] > Over-the-shoulder medium shot of a young female customer sitting at a wooden window counter inside a coffee shop, her laptop open in soft focus, a handmade ceramic coffee cup in her hand, warm window backlight creating gentle rim light on her silhouette, amber interior lamps in background blur, she slowly takes a sip of coffee and briefly closes her eyes in appreciation, slow pedestal camera mov
- [556cbcfe637d] > Medium wide locked-off shot of a hand-painted wooden shop sign above a dark-framed café door, below it a small chalkboard reading "Opening Saturday", a hand reaches in frame to hang a wooden "OPEN" sign on the door handle, soft even morning light, sage green accent wall visible, warm muted palette, shallow depth of field on the door, 35mm full-frame look, subtle film grain, cinematic 1080p, sync
- [81a8cfa35760] [ ] Generate all 6 shots with your preferred AI video tool
- [ab185f56879d] [ ] Add 0.3-0.4s **dissolve transitions** between Shots 1→2, 2→3, 4→5. Use a **hard cut** for Shot 3→4 (energy shift) and Shot 5→6 (CTA impact)
- [b8cf8ac90edc] **Visual consistency:** Every shot shares the same color palette (espresso/cream/amber/sage), the same lighting temperature (warm 3200K with motivated window light), the same lens character (shallow DOF, 35mm), and the same film look (subtle 16mm grain). Even if the 6 shots are generated in separate runs, they will edit together as if shot by the same cinematographer in the same session.
- [ac436694e34e] **Why the prompts work:** They lean heavily on concrete cinematic vocabulary (shallow DOF, rim light, warm backlight, film grain) — specifics that modern AI video models can actually execute. The synchronized audio direction means each shot arrives with ambient café sounds pre-baked, dramatically reducing post-production sound design time.