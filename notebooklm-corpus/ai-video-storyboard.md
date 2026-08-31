# SKILL: ai-video-storyboard

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: ai-video-storyboard/SKILL.md

---
name: ai-video-storyboard
description: Use when planning a multi-shot AI video (TikTok Reel, Instagram Ad, YouTube Shorts, product explainer) where the target duration exceeds what a single AI generation can produce (over 15 seconds), and you need a coordinated shot list with visually consistent prompts for each segment
---

# AI Video Storyboard Generator

## Overview

AI video generators produce 5–15 second clips. Real-world videos are longer: 30s TikToks, 60s ads, 90s explainers. This skill bridges that gap by producing a complete **shot-list storyboard** — a coordinated sequence of per-shot prompts with shared visual language, so the assembled final video looks like one intentional piece of work rather than six disconnected clips.

**Core insight:** Visual consistency across shots matters more than any single shot being perfect. A mediocre but consistent set of shots edits together; six gorgeous but mismatched shots do not.

## When to Use

- User wants a video longer than 15 seconds
- User wants a TikTok / Reel / Short / ad / explainer / B-roll sequence
- User says "help me make a video about X" and has no shot list
- User is about to generate multiple clips and needs a plan

**Do NOT use for:**
- Single-shot generation (just help with one prompt instead)
- Static image generation
- Video editing advice after clips are generated (that's a separate concern)

## Workflow

### Step 1 — Brief Intake

Ask the user these questions in a single message. Accept short answers:

1. **Goal platform and duration?** (TikTok 30s / Reel 15-60s / YouTube Short / Instagram Ad / explainer)
2. **What is the video about?** (subject, story, product)
3. **Brand vibe / tone?** (cozy, energetic, premium, minimalist, playful, cinematic, etc.)
4. **Call to action at the end?** (visit website, buy product, follow channel, etc.)
5. **Any hard constraints?** (must include logo, specific colors, locations, etc.)

If user already provided some of these, skip those questions and confirm the rest.

### Step 2 — Infer Structure

Based on duration and platform, divide the timeline into shots of ~5 seconds each (the sweet spot for AI video generators).

**Standard cadences:**

| Platform | Duration | Shots | Pacing |
|---|---|---|---|
| TikTok Hook | 15s | 3 | Fast cuts, single idea |
| TikTok Reel | 30s | 6 | Hook → Build → Payoff → CTA |
| Instagram Ad | 15s | 3 | Hook → Product → CTA |
| Instagram Ad | 30s | 6 | Hook → Problem → Product → Benefit → Social proof → CTA |
| YouTube Short | 60s | 12 | Hook → 3-act structure → CTA |
| Product Explainer | 90s | 18 | Problem → Solution → How it works → Results → CTA |
| Brand Story | 60s | 10-12 | Atmosphere-driven, longer shot holds |

### Step 3 — Establish Visual Consistency Layer

Before writing any shot, lock in the shared visual language. This is what makes shots edit together:

- **Color palette** (3-5 specific hex values or named colors)
- **Lighting style** (golden hour / neon / overcast / motivated / cinematic rim light)
- **Lens character** (shallow DOF / deep focus / wide angle distortion / macro)
- **Film look** (clean digital / 16mm grain / anamorphic / VHS / 35mm)
- **Motion language** (handheld / locked off / dolly only / gimbal smooth)

Write these as a **Visual Theme** block at the top of the output. Every shot's prompt must respect this block.

### Step 4 — Write Each Shot

For each shot, produce this structure:

```
## Shot N (START-ENDs) — [Purpose label: Hook / Setting / Action / Detail / Reveal / CTA]

**Composition:** [shot type + angle, e.g., "Extreme close-up, overhead"]
**Camera move:** [locked / slow dolly in / tracking / crane up / etc.]
**Lighting:** [from the Visual Theme, applied to this scene]
**Subject:** [what is in frame]
**Action:** [what is happening]

**Prompt to copy:**
> [Complete, cinematic-quality prompt, 40-80 words, including: subject + action + environment + camera + lighting + style + technical spec (duration, aspect ratio, resolution). Always ends with "cinematic 1080p, synchronized audio"]

**Audio direction:** [what the synchronized audio should sound like — ambient sounds, music beat position, voice-over line]
```

**Critical rules for shot prompts:**

1. **Always specify the shared visual language** in every prompt (color palette, lighting, lens character, film look). This is how you enforce consistency.
2. **Specify exact duration** (4s / 5s / 8s) and **aspect ratio** (9:16 for TikTok/Reels, 16:9 for YouTube landscape, 1:1 for feed posts).
3. **Always end with "cinematic 1080p, synchronized audio"** — this signals professional-grade quality and works with modern video models that support both.
4. **Use cinematography vocabulary**: ECU (extreme close-up), CU, MS (medium shot), WS (wide shot), OTS (over-the-shoulder), POV, Dutch angle, low angle, high angle, bird's eye, dolly in, dolly out, tracking, handheld, rack focus, etc.
5. **Don't write abstract prompts** — be concrete. "A woman" → "A barista in her late 20s with wavy auburn hair, wearing a denim apron".
6. **No model-specific hacks** — don't write prompts tuned to specific model quirks. Write model-agnostic cinematic prompts that work anywhere.

### Step 5 — Add Narrative Structure

The sequence of shots must have a **story arc**, not a random list. Use one of these patterns:

**Pattern A — Hook / Build / Payoff / CTA (TikTok default)**
- Shot 1: Visual hook (stop the scroll)
- Shot 2-3: Build context / intrigue
- Shot 4-5: Main content / payoff
- Shot 6: CTA

**Pattern B — Problem / Solution / Proof / CTA (Ad default)**
- Shots 1-2: Relatable problem
- Shot 3: Your product as solution
- Shots 4-5: Benefits / results
- Shot 6: CTA

**Pattern C — Atmosphere → Climax (Brand story)**
- Longer atmospheric shots
- Slow reveal
- Emotional climax
- Logo reveal

### Step 6 — Add Post-Production Checklist

Close with actionable post-production notes:

```
## Post-Production Checklist
- [ ] Generate all N shots with your preferred AI video tool
- [ ] Stitch in [CapCut / Descript / DaVinci Resolve / Premiere]
- [ ] Apply [specific LUT or color grade] for consistency
- [ ] Add [transition type and duration] between shots
- [ ] Layer BGM: [genre / BPM / mood]
- [ ] Add text overlays for [hook / CTA / captions]
- [ ] Export [platform spec: 9:16 1080x1920 30fps for TikTok, etc.]
```

### Step 7 — Explain Why It Works

Close with a "Why this works" block explaining the creative decisions. This educates the user and differentiates your output from generic prompt lists. Reference:

- The hook rule (first second determines watch-through)
- Pacing cadence (average scroll time)
- Story structure (why the shot order matters)
- Platform-specific conventions

## Output Format

The final output is a single Markdown document containing:

1. **Header** — Title, duration, shot count, aspect ratio
2. **Visual Theme** — Shared palette, lighting, lens, film look, motion
3. **Shot List** — N shots, each following the structure in Step 4
4. **Post-Production Checklist**
5. **Why This Works** — creative rationale

See `examples/tiktok-reel-30s-coffee.md` for a complete worked sample output (coffee shop opening TikTok, 30s / 6 shots).

## License

MIT — use freely, commercial or personal.


---

## ARCHIVO: ai-video-storyboard/examples/tiktok-reel-30s-coffee.md

# 30s TikTok Reel — Coffee Shop Opening

**Brief:** Small specialty coffee shop launching next week. Want a TikTok Reel to build anticipation and drive foot traffic on opening day.

- **Platform:** TikTok
- **Duration:** 30 seconds
- **Shots:** 6 × 5s
- **Aspect:** 9:16
- **CTA:** "Visit us. Opening next Saturday."
- **Brand vibe:** Warm, analog, hand-crafted, for slow-morning coffee lovers

---

## Visual Theme (applied to every shot)

- **Color palette:** Deep espresso brown `#3B2416`, cream `#F5E6D3`, muted amber `#D4A574`, soft sage green `#8FA88C`, black coffee `#1A1210`
- **Lighting style:** Warm golden backlight with motivated window light, soft shadows, no harsh fluorescents
- **Lens character:** Shallow depth of field, gentle bokeh, 35mm full-frame look
- **Film look:** Subtle 16mm film grain, slightly muted saturation, warm color temperature (around 3200K)
- **Motion language:** Locked-off or very slow push-ins, no handheld shake

---

## Shot 1 (0-5s) — Hook: The Pour

**Purpose:** Instant visual hook to stop the scroll. Universal sensory trigger.

**Composition:** Extreme close-up (ECU), slight overhead angle (~20° down)
**Camera move:** Locked off with micro push-in
**Lighting:** Strong warm backlight behind the cup, light rim-lighting the steam
**Subject:** Gooseneck kettle pouring hot water into a white ceramic V60 dripper
**Action:** Slow bloom of coffee grounds rising as water hits them

**Prompt to copy:**

> Extreme close-up overhead shot of hot water pouring from a brass gooseneck kettle into a white ceramic V60 dripper filled with dark coffee grounds, the grounds blooming and rising in slow motion, warm golden backlight with visible steam curling upward, shallow depth of field, 35mm full-frame look, subtle 16mm film grain, deep espresso brown and cream color palette, muted saturation, cinematic 1080p, synchronized audio, 5 seconds, 9:16 vertical

**Audio direction:** Intimate sound of pouring water, bloom of hot coffee crema, distant café ambience fading in. First acoustic guitar note plays at 4.8s to bridge into Shot 2.

---

## Shot 2 (5-10s) — Setting: The Space

**Purpose:** Establish the space. Show it's real, it's cozy, it exists.

**Composition:** Medium wide shot (MWS), waist-high eye level
**Camera move:** Very slow dolly forward (~0.5x speed feeling)
**Lighting:** Large window on camera-left, warm amber streetlamp glow from deep background
**Subject:** Empty wooden café interior, reclaimed wood counter in focus, shelves of mugs blurred in background
**Action:** Morning sun rays cut through the space, dust motes floating

**Prompt to copy:**

> Medium wide shot slow dolly forward into a cozy specialty coffee shop interior, warm morning sunlight streaming through large windows on the left, reclaimed dark wood counter in sharp focus with shelves of handmade ceramic mugs blurred in background, dust motes visible in sun rays, muted sage green wall accents, shallow depth of field, 35mm full-frame look, subtle film grain, warm 3200K color temperature, cinematic 1080p, synchronized audio, 5 seconds, 9:16 vertical

**Audio direction:** Acoustic guitar strum begins, layered with distant morning street sounds (birds, footsteps).

---

## Shot 3 (10-15s) — Human: The Barista

**Purpose:** Add a human face. Empathy trigger. This is the emotional center.

**Composition:** Medium close-up (MCU), slightly low angle (~10° up)
**Camera move:** Locked off
**Lighting:** Window light as key from camera-left, warm practical from counter lamp as fill
**Subject:** A female barista in her late 20s, wavy auburn hair tied back loosely, wearing a denim apron over a cream linen shirt
**Action:** She looks down at a pour-over in her hands, then looks up toward camera with a small, genuine smile

**Prompt to copy:**

> Medium close-up slightly low angle of a female barista in her late twenties with wavy auburn hair tied back, wearing a denim apron over cream linen shirt, standing behind a dark wood café counter, soft window light from the left creating warm rim light on her hair, she looks down at a pour-over coffee in her hands then slowly looks up at camera with a genuine small smile, shallow depth of field, 35mm full-frame look, subtle 16mm film grain, warm color temperature, cinematic 1080p, synchronized audio, 5 seconds, 9:16 vertical

**Audio direction:** Guitar melody crescendo, ambient café sounds swell subtly. No voice-over needed — her expression carries the emotion.

---

## Shot 4 (15-20s) — Detail: The Beans

**Purpose:** Tactile close-up. Signals craft and quality.

**Composition:** Extreme close-up (ECU), macro-style
**Camera move:** Micro zoom in
**Lighting:** Warm directional light from upper right, strong shadows
**Subject:** Hand scooping whole coffee beans from a burlap sack into a wooden measuring cup
**Action:** Slow-motion bean cascade as hand tips the scoop

**Prompt to copy:**

> Macro extreme close-up of a hand scooping whole dark roasted coffee beans from a burlap sack into a small wooden measuring cup, slow motion cascade of beans spilling out as the hand tips the scoop, warm directional window light from upper right creating strong shadow depth, individual beans visible in sharp detail, shallow depth of field, deep espresso brown and burlap cream palette, subtle 16mm film grain, cinematic 1080p, synchronized audio, 5 seconds, 9:16 vertical

**Audio direction:** Sound of beans tumbling, slightly rhythmic, quantized to the guitar beat. Guitar is now in full swing.

---

## Shot 5 (20-25s) — Atmosphere: The Customer Moment

**Purpose:** Show the space in use. Aspirational — "this could be you."

**Composition:** Medium shot (MS), over-the-shoulder angle (OTS)
**Camera move:** Slow pedestal down (~0.5x speed feeling)
**Lighting:** Window backlight creating gentle rim on the customer, warm amber spill from interior
**Subject:** A young customer sitting at a wooden window counter, laptop open, ceramic cup in hand
**Action:** She takes a slow sip, closes eyes briefly, sets cup down

**Prompt to copy:**

> Over-the-shoulder medium shot of a young female customer sitting at a wooden window counter inside a coffee shop, her laptop open in soft focus, a handmade ceramic coffee cup in her hand, warm window backlight creating gentle rim light on her silhouette, amber interior lamps in background blur, she slowly takes a sip of coffee and briefly closes her eyes in appreciation, slow pedestal camera move downward, shallow depth of field, 35mm full-frame look, subtle film grain, warm 3200K color temperature, cinematic 1080p, synchronized audio, 5 seconds, 9:16 vertical

**Audio direction:** Guitar continues, ambient café sounds (gentle chatter, page turning), the soft clink of cup on saucer at the end.

---

## Shot 6 (25-30s) — CTA: Opening Reveal

**Purpose:** Clear, confident call to action. Brand reveal.

**Composition:** Medium wide shot (MWS), straight-on eye level
**Camera move:** Locked off, zero movement (intentional stop to read text)
**Lighting:** Soft even morning light
**Subject:** The café's hand-painted wooden sign on the front door, "Opening Saturday" chalk text visible below
**Action:** Minimal — a hand hanging an "OPEN" wooden sign on the door handle

**Prompt to copy:**

> Medium wide locked-off shot of a hand-painted wooden shop sign above a dark-framed café door, below it a small chalkboard reading "Opening Saturday", a hand reaches in frame to hang a wooden "OPEN" sign on the door handle, soft even morning light, sage green accent wall visible, warm muted palette, shallow depth of field on the door, 35mm full-frame look, subtle film grain, cinematic 1080p, synchronized audio, 5 seconds, 9:16 vertical

**Audio direction:** Guitar resolves to final note, café ambience fades down. Sound of the wooden sign clacking against the door.

---

## Post-Production Checklist

- [ ] Generate all 6 shots with your preferred AI video tool
- [ ] Stitch in **CapCut** or **Descript** (simplest for TikTok workflow)
- [ ] Apply a consistent warm LUT — **Kodak Portra 400** emulation or **"Teal & Orange: Warm"** works well
- [ ] Add 0.3-0.4s **dissolve transitions** between Shots 1→2, 2→3, 4→5. Use a **hard cut** for Shot 3→4 (energy shift) and Shot 5→6 (CTA impact)
- [ ] Layer **BGM**: single acoustic guitar track at ~85 BPM, free from Artlist/Epidemic Sound. Something like "Morning Coffee" or "Slow Brew" genre keywords
- [ ] Add **text overlays**:
  - 0-1s: "Slow morning ☕️" (bottom center)
  - 25-30s: "Opening Saturday · @yourshop" (bold, centered)
- [ ] Export: **9:16, 1080×1920, 30fps, H.264, target bitrate 12 Mbps**
- [ ] Upload to TikTok with hashtags: `#coffeeshop #specialtycoffee #openingsoon #grandopening #coffeelover`

---

## Why This Works

**Structure:** Hook (1) → Setting (2) → Human (3) → Detail (4) → Atmosphere (5) → CTA (6). This is the classic TikTok cadence adapted for brand storytelling: a sensory hook to stop the scroll, a human face to build empathy, craft details to signal quality, an aspirational moment, then a clean CTA. No shot is wasted.

**Visual consistency:** Every shot shares the same color palette (espresso/cream/amber/sage), the same lighting temperature (warm 3200K with motivated window light), the same lens character (shallow DOF, 35mm), and the same film look (subtle 16mm grain). Even if the 6 shots are generated in separate runs, they will edit together as if shot by the same cinematographer in the same session.

**Pacing:** 5 seconds per shot matches the average scroll-dwell time on TikTok. Long enough to land the idea, short enough to maintain momentum. The 30s total is the sweet spot for completion-rate-optimized Reels.

**Emotion arc:** Shot 1 is sensory (hot water, steam), Shot 3 is emotional (barista's smile), Shot 5 is aspirational (customer enjoying the moment). This gives the viewer a reason to care beyond "coffee exists here".

**Why the prompts work:** They lean heavily on concrete cinematic vocabulary (shallow DOF, rim light, warm backlight, film grain) — specifics that modern AI video models can actually execute. The synchronized audio direction means each shot arrives with ambient café sounds pre-baked, dramatically reducing post-production sound design time.

