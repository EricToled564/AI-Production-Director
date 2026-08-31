# SKILL: screenwriter

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: screenwriter/SKILL.md

---
name: screenwriter
description: >
  Transform creative ideas into professional, production-ready screenplays optimized for AI video generation pipelines. Converts raw concepts into structured scene-by-scene narratives with rich visual descriptions, proper screenplay formatting, and XML-tagged output for seamless integration with image/video generation tools (imagine, arch-v).
  
  USE WHEN: Converting story ideas into screenplay format, preparing content for AI video pipelines, structuring narratives for 5-10 minute short films, generating visual-rich scene descriptions for image generation. Use this even when the user doesn't say "screenplay" explicitly — e.g. "break this idea into scenes" or "write the script for this short film."
  
  WORKFLOW: Raw idea → Scene breakdown → Visual enhancement → Professional formatting → XML-tagged markdown output
  
  OUTPUT: Markdown document with XML-wrapped scenes, rich visual descriptions, proper screenplay elements (sluglines, action, dialogue), and metadata for pipeline processing.
---

# Screenwriter Skill

## Overview

This skill transforms creative concepts into professional screenplay documents optimized for AI-powered video production pipelines. It bridges the gap between raw story ideas and production-ready scripts by generating structured, visual-rich narratives in industry-standard screenplay format.

**Pipeline Position:** `diverse-content-gen` → **screenwriter** → `imagine` → `arch-v`

**Key Capabilities:**
- Convert raw ideas into structured scene-by-scene narratives
- Generate rich visual descriptions optimized for image generation
- Apply professional screenplay formatting (sluglines, action lines, dialogue)
- Output XML-tagged markdown for easy parsing
- Optimize pacing for 5-10 minute short films (8-15 scenes typical)

---

## Core Workflow

### 1. Analyze Input Concept
- Extract key story beats from raw ideas
- Identify characters, locations, emotional arc
- Determine story structure (beginning, middle, end)

### 2. Generate Scene Breakdown
- Convert story beats into discrete scenes
- Establish scene count (aim for 8-15 scenes for 5-10 min films)
- Define scene purpose and emotional progression

### 3. Write Professional Screenplay
- Apply industry-standard formatting
- Write visual-rich action lines
- Include dialogue when narratively essential
- Maintain consistent character descriptions

### 4. Output XML-Tagged Markdown
- Wrap each scene in XML tags with metadata
- Include scene numbers, locations, key visuals
- Format for easy pipeline parsing

---

## Screenplay Format Standards

### Scene Structure (Master Scene Heading)

**Slugline Format:**
```
INT/EXT. LOCATION - TIME
```

**Components:**
- **INT/EXT:** Interior or Exterior
- **LOCATION:** Specific place (be descriptive but concise)
- **TIME:** DAY, NIGHT, DAWN, DUSK, CONTINUOUS

**Examples:**
```
EXT. WASTELAND - DAWN
INT. ABANDONED SUBWAY STATION - NIGHT
EXT. ROOFTOP GARDEN - GOLDEN HOUR
```

**Guidelines:**
- Always use ALL CAPS for sluglines
- Use hyphens to separate elements
- Be specific with locations (aids visual generation)
- Time should suggest lighting/mood

### Action Lines (Visual Description)

**Purpose:** Describe what the audience sees on screen. This is CRITICAL for image generation.

**Visual-Rich Writing Principles:**
1. **Show, Don't Tell:** Write what's visible, not internal thoughts
2. **Sensory Details:** Include lighting, atmosphere, textures, colors
3. **Present Tense:** Always write in present tense
4. **Active Voice:** Use strong, active verbs
5. **Specific Props:** Name objects that matter visually
6. **Atmosphere:** Set mood through environmental details

**Example - Weak:**
```
A robot walks through the city. It's sad.
```

**Example - Strong:**
```
A BOXY ROBOT (Unit-7, weathered chrome with a single blue optical sensor) rolls through fog-shrouded streets. Neon signs flicker overhead, casting pink and cyan reflections on wet pavement. The robot's movements are slow, deliberate—almost hesitant.
```

**Visual Enhancement Checklist:**
- [ ] Lighting described (natural/artificial, quality, color)
- [ ] Atmosphere/mood established (fog, rain, dust, clarity)
- [ ] Character appearance detailed (first appearance only)
- [ ] Props/objects specified (important visual elements)
- [ ] Composition suggested (without technical camera direction)
- [ ] Colors/textures mentioned when relevant

### Character Introduction

**First Appearance - Detailed:**
```
SARAH (28, sharp eyes, wearing a weathered leather jacket over faded jeans) enters the frame. Her dark hair is pulled back, revealing a small scar above her left eyebrow.
```

**Subsequent Appearances - Brief:**
```
Sarah checks her watch.
```

**Guidelines:**
- Character names in ALL CAPS on first appearance only
- Include: age (if relevant), key physical traits, wardrobe
- Focus on visual identifiers for consistent image generation
- Avoid excessive detail—just enough for visual consistency

### Dialogue (Use Sparingly)

**Format:**
```
CHARACTER NAME
(parenthetical - optional)
Dialogue goes here.
```

**Guidelines for Short Films:**
- Use dialogue ONLY when essential to story
- Favor visual storytelling over talking
- Keep lines concise (max 3-4 lines per block)
- Parentheticals only for critical tone/action
- Character names centered, ALL CAPS

**Example:**
```
UNIT-7 (robotic voice, soft)
Organic life form detected.
Probability of survival: low.
```

### Transitions (Minimal Use)

**Common Transitions:**
- `FADE IN:` - Opening of screenplay only
- `CUT TO:` - Scene change (usually implied, use for emphasis)
- `SMASH CUT TO:` - Abrupt, jarring transition
- `DISSOLVE TO:` - Passage of time
- `FADE OUT.` - End of screenplay

**Modern Best Practice:** Most transitions are IMPLIED. Use sparingly, only for specific narrative effect.

---

## XML Output Format

### Scene Tag Structure

Each scene wrapped in XML with metadata for pipeline processing:

```xml
<scene number="1" duration="30-45s">
  <slugline>EXT. WASTELAND - DAWN</slugline>
  <location>Wasteland</location>
  <time>Dawn</time>
  <characters>Unit-7</characters>
  <mood>desolate, lonely</mood>
  <key_visuals>
    <visual>post-apocalyptic wasteland with ruined skyscrapers</visual>
    <visual>boxy robot with single blue optical sensor</visual>
    <visual>dust and smog atmosphere, weak pale sun</visual>
  </key_visuals>
  <action>
Gray dust covers everything. Skeletal remains of skyscrapers pierce the horizon. The sun, pale and weak, struggles through thick smog.

A ROBOT (Unit-7, boxy frame with single blue optical sensor) rolls across cracked asphalt. Its treads leave marks in the dust—the only sign of life.

The robot stops at a pile of rubble, extending a mechanical arm to sort through debris. Methodical. Purposeful. Lonely.
  </action>
</scene>
```

### Metadata Fields

- `number`: Scene sequence number (1, 2, 3...)
- `duration`: Estimated screen time (for 5-10 min total)
- `slugline`: Master scene heading
- `location`: Extracted location name
- `time`: Time of day
- `characters`: Comma-separated character list
- `mood`: Emotional tone/atmosphere
- `key_visuals`: Array of specific visual elements for image generation
- `action`: The full action/description text
- `dialogue` (optional): Character dialogue if present

---

## Short Film Structure (5-10 Minutes)

### Scene Count Guidelines
- **5 minutes:** 6-10 scenes
- **7 minutes:** 10-12 scenes
- **10 minutes:** 12-15 scenes

**Average:** ~30-60 seconds per scene

### Three-Act Structure (Compressed)

**Act 1 - Setup (20-25%):** 2-3 scenes
- Establish world, character, situation
- Inciting incident

**Act 2 - Confrontation (50-60%):** 4-8 scenes
- Development, obstacles, rising tension
- Midpoint twist or escalation

**Act 3 - Resolution (20-25%):** 2-3 scenes
- Climax and resolution
- Emotional payoff

### Pacing Tips
- **Open strong:** Hook audience in first 10-15 seconds
- **Visual variety:** Alternate between wide/close, action/stillness
- **Emotional beats:** Each scene should shift emotional state
- **Build tension:** Escalate stakes scene-by-scene
- **Satisfying end:** Clear resolution, even if bittersweet

---

## Best Practices

### For Pipeline Integration
- **Consistent naming:** Use same character names throughout
- **Rich visuals:** Every scene needs 3-5 key_visuals for image generation
- **Parseable format:** Maintain strict XML structure
- **Duration estimates:** Help pipeline plan total video length

### For Quality Output
- **Visual storytelling:** Show emotions through actions, not dialogue
- **Specific details:** "weathered chrome" beats "old metal"
- **Atmospheric writing:** Set mood through environment
- **Lean prose:** Each word should serve the image

### Common Pitfalls to Avoid
- ❌ **Vague descriptions:** "A person walks" → ✅ "A weathered woman in her 50s trudges through snow"
- ❌ **Telling emotions:** "She feels sad" → ✅ "Tears streak her dusty cheeks"
- ❌ **Camera directions:** "CLOSE UP ON" → ✅ "The crack in the glass spreads"
- ❌ **Over-dialogue:** Short films need visual storytelling
- ❌ **Inconsistent character names:** Stick to ONE name per character

---

## Additional Resources

### Pipeline Integration Guide
For detailed guidance on metadata standards, visual optimization, and integration with imagine/arch-v:
- [references/pipeline-integration.md](references/pipeline-integration.md)

### Advanced Techniques
For sophisticated screenwriting techniques, camera movement hints, and pacing optimization:
- [references/advanced-techniques.md](references/advanced-techniques.md)


---

## ARCHIVO: screenwriter/references/advanced-techniques.md

# Advanced Screenwriting Techniques

This reference covers sophisticated techniques for elevating screenplay quality and preparing for downstream video generation (arch-v integration).

## Table of Contents
1. [Camera Movement Hints (For Arch-V)](#camera-movement-hints-for-arch-v)
2. [Dialogue Polish Techniques](#dialogue-polish-techniques)
3. [Pacing Optimization](#pacing-optimization)
4. [Advanced Visual Storytelling](#advanced-visual-storytelling)
5. [Short Film Specific Techniques](#short-film-specific-techniques)

---

## Camera Movement Hints (For Arch-V)

While avoiding technical camera directions in action lines, you can *suggest* camera movement through visual description and scene structure.

### Suggesting Camera Movement Through Description

**Wide Establishing → Close Detail:**
```
The city sprawls below—a concrete jungle of steel and glass.

At street level, a single red balloon floats past graffitied walls.
```
*Implies: Wide establishing shot → close-up detail*

**Following Movement:**
```
Maya runs down the alley, her footsteps echoing off brick walls. Trash cans blur past. The exit ahead grows larger.
```
*Implies: Tracking shot following character*

**Revealing Information:**
```
The desk is empty. Coffee still steaming. Papers scattered.

The door stands ajar, revealing darkness beyond.
```
*Implies: Pan from desk to door, revealing new information*

### Scene Structure for Camera Flow

**Short Paragraphs = Multiple Shots:**
Breaking action into short paragraphs suggests multiple camera setups:

```
The warehouse is silent.

A shadow moves across the floor.

Sarah freezes, hand on her weapon.

The shadow stops.
```

**Continuous Paragraph = Single Shot:**
One paragraph suggests continuous camera movement:

```
Sarah enters the warehouse, weapon drawn. She moves along the wall, checking corners. The shadow crosses her path. She spins, aiming into darkness.
```

---

## Dialogue Polish Techniques

### Subtext Over Direct Statement

**❌ On-the-nose:**
```
JOHN
I'm angry at you for lying to me.
```

**✅ Subtext:**
```
JOHN
(barely looking at her)
Coffee's cold.
```

### Character Voice Consistency

Each character should have distinct speech patterns:

**Marcus (technical, precise):**
```
MARCUS
Probability of success: 47 percent.
Margin of error: plus or minus 3.
```

**Sarah (emotional, intuitive):**
```
SARAH
We'll make it work. We always do.
```

### Dialogue Rhythm

Vary sentence length for natural flow:

```
ELENA
Three years. That's how long I waited.
For what? This?
```

---

## Pacing Optimization

### Scene Length Variation

Alternate between long and short scenes for rhythm:

**Pattern Example:**
- Scene 1: 60s (long, establishing)
- Scene 2: 30s (short, tense)
- Scene 3: 45s (medium, development)
- Scene 4: 30s (short, action)
- Scene 5: 90s (long, climax)

### Tension Escalation

Each scene should raise stakes or tension incrementally:

**Scene 1:** Character wants something
**Scene 2:** Obstacle appears
**Scene 3:** Obstacle worsens
**Scene 4:** New complications
**Scene 5:** Crisis point
**Scene 6:** Resolution

### Visual Momentum

Alternate visual energy levels:

```
Scene A: Still, contemplative (character alone, quiet)
Scene B: Dynamic, energetic (chase, conflict, movement)
Scene C: Medium tempo (conversation, planning)
```

---

## Advanced Visual Storytelling

### Using Objects as Story Beats

Let objects carry narrative weight:

**The Flower Example:**
- Scene 1: Flower is vibrant, yellow
- Scene 3: Flower petals drooping
- Scene 5: Single petal falls
- Scene 7: Flower completely wilted

### Environmental Storytelling

Show passage of time or change through environment:

```
Scene 1: "Sunlight streams through clean windows"
Scene 5: "Dust motes drift through afternoon light"
Scene 10: "Shadows lengthen across abandoned chairs"
```

### Color Progression

Use color to track emotional/narrative arc:

**Beginning:** Warm, golden tones (hope)
**Middle:** Desaturated, gray (struggle)
**End:** Cool blue light (resolution/melancholy)

---

## Short Film Specific Techniques

### Economy of Storytelling

Every scene must serve multiple purposes:
- Advance plot
- Reveal character
- Build world
- Create emotion

**Example Scene Serving 4 Purposes:**
```
Scene: Robot discovers flower

Purpose 1 (Plot): Introduces story catalyst
Purpose 2 (Character): Shows robot's capacity for wonder
Purpose 3 (World): Reveals post-apocalyptic setting
Purpose 4 (Emotion): Creates hope/fragility contrast
```

### Opening Hook Strategies

First 10-15 seconds must grip audience:

**Visual Hook:** Striking, unusual image
**Question Hook:** Raise mystery to be solved
**Action Hook:** Start mid-event
**Emotion Hook:** Immediate emotional connection

### Ending Impact

Strong endings for short films:

**Circular:** Return to opening image, transformed
**Revelation:** Final scene reveals new understanding
**Resonance:** Emotionally satisfying moment
**Question:** Leave audience pondering


---

## ARCHIVO: screenwriter/references/pipeline-integration.md

# Pipeline Integration Guide

This reference provides detailed guidance for integrating screenwriter output with downstream AI tools (imagine, arch-v) in video generation pipelines.

## Table of Contents
1. [Scene Metadata Standards](#scene-metadata-standards)
2. [Imagine-Ready Visual Descriptions](#imagine-ready-visual-descriptions)
3. [Character Consistency Tracking](#character-consistency-tracking)
4. [Scene Numbering Conventions](#scene-numbering-conventions)
5. [Duration Estimation Guidelines](#duration-estimation-guidelines)
6. [Output Format Validation](#output-format-validation)
7. [Pipeline Handoff Checklist](#pipeline-handoff-checklist)

---

## Scene Metadata Standards

### Metadata Completeness

Every scene MUST include all required metadata fields for reliable pipeline processing:

**Required Fields:**
- `number`: Integer, sequential scene numbering
- `slugline`: Full scene heading (INT/EXT. LOCATION - TIME)
- `location`: Extracted location name for tracking
- `time`: Time of day (affects lighting in image generation)
- `characters`: All characters present in scene
- `mood`: Emotional tone/atmosphere descriptor
- `key_visuals`: 3-5 specific visual elements
- `action`: Full action/description text

**Optional Fields:**
- `dialogue`: Include only if dialogue exists
- `duration`: Scene duration estimate (helpful for pacing)

### Metadata Quality Guidelines

**Location Specificity:**
```xml
<!-- ❌ Too vague -->
<location>Building</location>

<!-- ✅ Specific and descriptive -->
<location>Abandoned Subway Station</location>
```

**Mood Descriptors:**
Use 1-3 adjectives that guide visual tone:
- Good: "tense, claustrophobic"
- Good: "serene, hopeful"
- Avoid: "the character feels anxious" (this describes internal state, not mood)

**Character Lists:**
```xml
<!-- Single character -->
<characters>Unit-7</characters>

<!-- Multiple characters -->
<characters>Sarah, Marcus, Tech-Bot</characters>
```

---

## Imagine-Ready Visual Descriptions

### Visual Element Extraction

The `key_visuals` array should contain discrete, image-generation-friendly descriptions:

**Example Scene Action:**
```
A BOXY ROBOT (Unit-7, weathered chrome with a single blue optical sensor) rolls through fog-shrouded streets. Neon signs flicker overhead, casting pink and cyan reflections on wet pavement.
```

**Extracted key_visuals:**
```xml
<key_visuals>
  <visual>boxy robot with weathered chrome body and single blue optical sensor</visual>
  <visual>fog-shrouded cyberpunk street with flickering neon signs</visual>
  <visual>pink and cyan neon reflections on wet pavement</visual>
</key_visuals>
```

### Visual Description Best Practices

**Composition Elements:**
- Subject: Main focus (character, object)
- Setting: Environment and background
- Lighting: Light quality, direction, color
- Atmosphere: Weather, air quality, mood
- Details: Significant props or textures

**Example - Layered Visual:**
```
Subject: "weathered robot with blue optical sensor"
Setting: "abandoned industrial warehouse, broken windows"
Lighting: "harsh afternoon sunlight streaming through gaps"
Atmosphere: "dust particles floating in light beams"
Details: "rusted machinery, scattered tools"
```

### Color and Lighting Vocabulary

**Color Descriptors:**
- Warm: amber, golden, crimson, burnt orange
- Cool: azure, ice blue, slate gray, mint
- Neon: electric pink, cyan, magenta, lime
- Natural: earth tones, moss green, sand, clay

**Lighting Descriptors:**
- Quality: soft, harsh, diffused, dappled, dramatic
- Direction: overhead, backlighting, side-lit, rim light
- Color: warm glow, cool blue, golden hour, neon-lit
- Intensity: dim, bright, shadowy, high-contrast

---

## Character Consistency Tracking

### First Appearance Template

Establish complete visual identity on first appearance:

```
CHARACTER NAME (age if relevant, defining physical trait, primary wardrobe)
```

**Examples:**
```
MAYA (early 30s, kind eyes, wearing a faded denim jacket and cargo pants)
COMMANDER REED (50s, grizzled with close-cropped gray hair, military uniform with rank insignia)
THE STRANGER (tall figure in a long black coat, face obscured by wide-brimmed hat)
```

### Subsequent References

After first appearance, use consistent identifiers:

**Preferred Pattern:**
- Use character name only: "Maya checks her phone"
- Add action-relevant details: "Maya pulls her jacket tighter against the wind"

**Avoid:**
- Re-describing appearance: "Maya, the woman in the denim jacket..."
- Changing character names: "Maya" → "the woman" → "she"

### Character Tracking Checklist

For each character, track:
- [ ] Full name and any aliases
- [ ] Age or age range
- [ ] Key physical identifiers (height, build, distinctive features)
- [ ] Primary wardrobe (consistent across scenes unless story requires change)
- [ ] Unique mannerisms or movement style

---

## Scene Numbering Conventions

### Sequential Numbering

Number scenes sequentially from 1 to N:
```xml
<scene number="1" ...>
<scene number="2" ...>
<scene number="3" ...>
```

**No Scene 0:** Start at 1, not 0 (industry standard)

### Scene Splits and Inserts

If a scene needs to be split or inserted during revision:
- Option A: Renumber all subsequent scenes
- Option B: Use fractional numbering (1, 2, 2A, 3...)

For pipeline simplicity, prefer Option A (complete renumbering).

---

## Duration Estimation Guidelines

### Per-Scene Duration

Estimate based on scene complexity:

**30-45 seconds:** Simple scenes
- Single action
- Minimal dialogue
- One primary visual

**45-60 seconds:** Standard scenes
- Multiple actions or dialogue exchanges
- 2-3 visual beats
- Character interaction

**60-90 seconds:** Complex scenes
- Extended dialogue
- Multiple visual beats
- Scene climax or key moment

### Total Film Duration

Track cumulative duration across all scenes:

```
Scene 1: 30s
Scene 2: 45s
Scene 3: 40s
...
Total: 8 minutes 20 seconds
```

Adjust scene count or duration to hit target length (5-10 min).

---

## Output Format Validation

### XML Well-Formedness

Ensure valid XML structure:
- All opening tags have closing tags
- Proper nesting (no overlapping tags)
- Special characters escaped (&lt; &gt; &amp;)

### Common XML Errors

**❌ Missing closing tag:**
```xml
<scene number="1">
  <action>Text here
</scene>
```

**✅ Properly closed:**
```xml
<scene number="1">
  <action>Text here</action>
</scene>
```

**❌ Unescaped special characters:**
```xml
<action>She thinks: "I'm < 10 years old"</action>
```

**✅ Properly escaped:**
```xml
<action>She thinks: "I'm &lt; 10 years old"</action>
```

---

## Pipeline Handoff Checklist

Before passing screenplay to next pipeline stage:

- [ ] All scenes have complete metadata
- [ ] key_visuals array populated (3-5 per scene)
- [ ] Character names consistent throughout
- [ ] XML well-formed and parseable
- [ ] Total duration within target range (5-10 min)
- [ ] Scene numbers sequential with no gaps
- [ ] Visual descriptions rich and specific
- [ ] No technical camera directions (use visual descriptions instead)

