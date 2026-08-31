# Reglas del skill: screenwriter

57 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## screenwriter/SKILL.md

- [fb3896038afa] Always use ALL CAPS for sluglines
- [4d9355018ad2] Use hyphens to separate elements
- [57e9c487ac74] Time should suggest lighting/mood
- [fa0199539554] **Show, Don't Tell:** Write what's visible, not internal thoughts
- [e10b5f7be709] **Sensory Details:** Include lighting, atmosphere, textures, colors
- [45f2e43f67e0] **Present Tense:** Always write in present tense
- [a93dbeef8737] **Active Voice:** Use strong, active verbs
- [10e5da2fcf9a] **Specific Props:** Name objects that matter visually
- [59d398f4c454] **Atmosphere:** Set mood through environmental details
- [671c49de0056] Avoid excessive detail—just enough for visual consistency
- [27e302d3a37e] Use dialogue ONLY when essential to story
- [5645bf344589] `CUT TO:` - Scene change (usually implied, use for emphasis)
- [68d5f2185557] **Modern Best Practice:** Most transitions are IMPLIED. Use sparingly, only for specific narrative effect.
- [c775d8acd13e] **Emotional beats:** Each scene should shift emotional state
- [8cc0ef448f33] **Consistent naming:** Use same character names throughout
- [bff5030b3380] **Lean prose:** Each word should serve the image
- [35abb8abc912] ❌ **Vague descriptions:** "A person walks" → ✅ "A weathered woman in her 50s trudges through snow"
- [df9b899dbc91] ❌ **Telling emotions:** "She feels sad" → ✅ "Tears streak her dusty cheeks"
- [de28e225dfa5] ❌ **Camera directions:** "CLOSE UP ON" → ✅ "The crack in the glass spreads"
- [aa1edc03619b] ❌ **Over-dialogue:** Short films need visual storytelling
- [0cf150e839a8] ❌ **Inconsistent character names:** Stick to ONE name per character

## screenwriter/references/advanced-techniques.md

- [90c5d5126758] [Camera Movement Hints (For Arch-V)](#camera-movement-hints-for-arch-v)
- [b7d064023d0d] [Dialogue Polish Techniques](#dialogue-polish-techniques)
- [1c4f7d2165c8] [Pacing Optimization](#pacing-optimization)
- [0f0193ec9566] [Advanced Visual Storytelling](#advanced-visual-storytelling)
- [206b86beff99] [Short Film Specific Techniques](#short-film-specific-techniques)
- [b6cf18f1ea26] While avoiding technical camera directions in action lines, you can *suggest* camera movement through visual description and scene structure.
- [5c5b85a079dc] **❌ On-the-nose:**
- [118e505786a4] **✅ Subtext:**
- [f1221744d7a1] Each character should have distinct speech patterns:
- [42187af933ee] Each scene should raise stakes or tension incrementally:
- [38b4028efe2f] Use color to track emotional/narrative arc:
- [5ea772208440] Every scene must serve multiple purposes:
- [3697579b1689] First 10-15 seconds must grip audience:

## screenwriter/references/pipeline-integration.md

- [9c577fb2318c] [Scene Metadata Standards](#scene-metadata-standards)
- [5b3dfb82edff] [Imagine-Ready Visual Descriptions](#imagine-ready-visual-descriptions)
- [4091766c17f1] [Character Consistency Tracking](#character-consistency-tracking)
- [5c45c9d37a0f] [Scene Numbering Conventions](#scene-numbering-conventions)
- [43640ae6f014] [Duration Estimation Guidelines](#duration-estimation-guidelines)
- [f781421a09f6] [Output Format Validation](#output-format-validation)
- [64821fb649fa] [Pipeline Handoff Checklist](#pipeline-handoff-checklist)
- [dcba7967bb86] Every scene MUST include all required metadata fields for reliable pipeline processing:
- [5a421a0a0c7f] **Required Fields:**
- [34d356cca129] Use 1-3 adjectives that guide visual tone:
- [06f7cfabe30d] Avoid: "the character feels anxious" (this describes internal state, not mood)
- [f02d8dcae6c2] The `key_visuals` array should contain discrete, image-generation-friendly descriptions:
- [9a04fd13f520] After first appearance, use consistent identifiers:
- [ee32154734ae] **Preferred Pattern:**
- [d58376dbc7f5] Use character name only: "Maya checks her phone"
- [33379bbc4b87] Option B: Use fractional numbering (1, 2, 2A, 3...)
- [8a33756b8cb8] For pipeline simplicity, prefer Option A (complete renumbering).
- [3172bdb34a71] Ensure valid XML structure:
- [f139664debd1] **❌ Missing closing tag:**
- [415ef4d14678] **✅ Properly closed:**
- [f034c18c96e4] **❌ Unescaped special characters:**
- [b18a910b547f] **✅ Properly escaped:**
- [47f320764950] [ ] No technical camera directions (use visual descriptions instead)