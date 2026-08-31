# Reglas del skill: storyboard-html-preview

17 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## storyboard-html-preview/SKILL.md

- [090ccfb96455] The constraint is non-negotiable: **single file, no build step, no server, works offline.** Any time the output requires "run this build command" or "host this somewhere," the skill has failed.
- [629bb2d205d3] An entry in `shot.assets.generated` marked `accepted: true`
- [b9f0e777f95a] The newest entry in `shot.assets.generated`
- [b86cdec0bdb7] `frames/round-{highest}/{shot_id}.{png,jpg,jpeg,webp}`
- [ed9eefdf08c5] `generated/{shot_id}.{ext}`, the pre-3.0.0 flat layout
- [09e4367e3b97] The HTML preview should *feel* like the brand without going overboard. Quiet branding, not loud.
- [8a2c11a5fc35] Use `templates/preview.html.tpl` as the structural template. Read it before generating.
- [410599a6e6d1] frames as base64. Ask the user which they prefer if frames are present.
- [0c58d39b58a3] `text-overlays.json` always did. A single set of `overlay_*` fields could hold one, so the
- [e3ddb1d823f5] Ensure text overlays render legibly
- [32701372f5d1] Use black-on-white where brand colors won't print well
- [6975e2ff7171] The user should be able to hit Cmd-P / Ctrl-P and get a clean PDF.
- [77570da551dd] No CDN scripts. No Google Fonts. No external CSS frameworks. The file must work with no internet connection.
- [d86f1629a7f6] Hit Cmd-P. The result should be a clean PDF. If layout breaks across page boundaries, the print stylesheet is broken.
- [90b1a187484f] Use brand colors as accents, not as full backgrounds. The reviewer's job is to read the storyboard, not admire the design. Subtle.
- [9f76efb872f5] Stakeholders open links on phones. The HTML should be readable on mobile without horizontal scroll. Simple responsive CSS.
- [3c8013b57f39] was written. They are separate lines in the footer and they must stay separate.