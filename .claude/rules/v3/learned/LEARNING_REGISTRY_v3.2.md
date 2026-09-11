# AI Production Director — Learning Registry v3.2

These are versioned production learnings from the controlled Olympic 10 m platform-diving image trial. They do **not** rewrite the canonical KB extractor. Promotion path: production evidence → learned overlay → regression tests → versioned ruleset.

1. **Lock preservation on revision.** Do not reinterpret unaffected user/project locks.
2. **Small-delta revision.** Correct only failed elements when the rest of the asset/prompt is passing.
3. **Preserve domain-native pose terminology.** A precise phrase such as a standard Olympic 10 m platform diving entry position should not be expanded into speculative anatomical prose unless required or proven necessary.
4. **Reference-role isolation.** A water-physics reference controls water physics only; ignored dimensions must not leak into pose, framing, identity, environment, color, etc.
5. **Generation parameters are hard settings.** Aspect ratio/size must be passed as generator settings when possible and verified from output pixels.
6. **Aspect-ratio output policy.** Exact is preferred; <=1% deviation is minor/crop-fix; >1% is blocking unless explicitly accepted.
7. **No unspecified amplification.** Presence does not imply quantity/density. Audience present does not mean packed stands; packed stands require a lock.
8. **Physically justified occlusion.** In complex underwater anatomy, bubbles/turbulence may hide non-critical detail while preserving required silhouette, proportions, orientation and continuity.
9. **Camera-relative geometry.** Objects located behind the camera by the locked scene geometry must not appear in frame.
10. **QA before success claims.** Do not call an asset/model successful before applicable QA. Mechanical and semantic checks remain distinct; age/nationality/ethnicity are not visually certifiable from pixels alone.
11. **Surgical edit after acceptance.** Local requested changes to an accepted image use edit, not reroll; preserve approved pixels/locks outside the delta.
12. **Empirical model routing.** For complex split-level underwater human anatomy, especially Olympic/platform diving, Nano Banana Pro is the preferred default candidate based on this trial. An explicit user model lock wins; future benchmark evidence may supersede the preference.

## Trial-specific observations preserved as tests/evidence
- GPT Image 2 repeatedly produced strong water/stadium rendering but unstable extreme-entry pose/head/feet in this case.
- Nano Banana Pro produced an accepted frontal entry pose with coherent anatomy and complex water behavior.
- Verbose anatomical decompositions degraded the pose relative to the user's concise domain-native pose lock.
- A partial water reference was useful when its role and ignored dimensions were explicit.
- Background/crowd and camera-visible structures should be treated as independent small deltas rather than reasons to reroll an accepted subject/water solution.

13. **Composition-only sources are abstracted, not attached.** If a user asks to follow/study composition, convert the source into a composition spec and generate with zero source-image references unless reference use is explicitly requested.
14. **No cross-task attribute leakage.** A new task cannot inherit demographics, nationality, ethnicity, gender, wardrobe, brand, or other subject/content locks from a previous task unless explicitly inherited by the current brief.
