# Decisión por sección — universo de creación de imágenes con GPT Image 2

Cada una de las 1,408 secciones (documento + ruta de encabezados, `secciones.txt`) leída y decidida en `decidir_secciones.py`.

| Estado | Secciones | Textos |
|---|---:|---:|
| dentro | 342 | 2,350 |
| mixta | 54 | 782 |
| otro_modelo | 85 | 408 |
| fuera | 927 | 9,465 |

## Secciones mixtas (se deciden leyendo cada texto)

| # | Documento | Sección | Textos |
|---:|---|---|---:|
| 11 | `flujos/flujo-spot.html` | (inicio del documento) | 8 |
| 12 | `flujos/flujo-spot.html` | Nivel 0 → 1 | 57 |
| 13 | `flujos/flujo-spot.html` | Nivel 2 | 58 |
| 16 | `flujos/flujo-spot.html` | Nivel 3b · cadena de dependencia | 42 |
| 34 | `skills/ai-production-director/SKILL.md` | AI Production Director › 6. Reglas de resolución de conflictos › 6.1 Vocabulario | 2 |
| 35 | `skills/ai-production-director/SKILL.md` | AI Production Director › 6. Reglas de resolución de conflictos › 6.2 Sintaxis de modelo | 2 |
| 37 | `skills/ai-production-director/SKILL.md` | AI Production Director › 6. Reglas de resolución de conflictos › 6.4 División forge ↔ smixs | 2 |
| 277 | `skills/image/references/models.md` | Model Selection — Nano Banana vs GPT Image 2 › TL;DR | 15 |
| 282 | `skills/image/references/models.md` | Model Selection — Nano Banana vs GPT Image 2 › Различия в синтаксисе промпта | 11 |
| 283 | `skills/image/references/models.md` | Model Selection — Nano Banana vs GPT Image 2 › Стоимость (ориентир) | 13 |
| 348 | `skills/image/references/patterns/portrait-cinema.md` | Portrait & Cinema Patterns › Japanese Negative Film Rooftop Portrait | 7 |
| 349 | `skills/image/references/patterns/portrait-cinema.md` | Portrait & Cinema Patterns › Dreamy Underwater Surreal Portrait | 6 |
| 667 | `skills/storyboard-architect/references/on-screen-text.md` | On-Screen Text › Composition rules › Negative-space-aware composition | 4 |
| 676 | `skills/storyboard-architect/references/shot-grammar.md` | Shot Grammar › Framing (subject size in frame) | 11 |
| 677 | `skills/storyboard-architect/references/shot-grammar.md` | Shot Grammar › Angle (camera vertical position) | 9 |
| 678 | `skills/storyboard-architect/references/shot-grammar.md` | Shot Grammar › Motion (camera movement) | 12 |
| 679 | `skills/storyboard-architect/references/shot-grammar.md` | Shot Grammar › Depth of field | 7 |
| 680 | `skills/storyboard-architect/references/shot-grammar.md` | Shot Grammar › Lighting style (referenced from series_lock) | 6 |
| 681 | `skills/storyboard-architect/references/shot-grammar.md` | Shot Grammar › Subject description | 8 |
| 682 | `skills/storyboard-architect/references/shot-grammar.md` | Shot Grammar › What goes in `subject` vs `series_lock` vs `brand_lock` | 6 |
| 804 | `skills/video/references/animatic-keyframes.md` | Keyframes for an animatic (opornye kadry) › 1. What an animatic keyframe must do | 8 |
| 805 | `skills/video/references/animatic-keyframes.md` | Keyframes for an animatic (opornye kadry) › 2. The keyframe card | 5 |
| 806 | `skills/video/references/animatic-keyframes.md` | Keyframes for an animatic (opornye kadry) › 3. How many keyframes per beat — the density ladder | 11 |
| 807 | `skills/video/references/animatic-keyframes.md` | Keyframes for an animatic (opornye kadry) › 4. Composing a still that reads as MOTION | 19 |
| 808 | `skills/video/references/animatic-keyframes.md` | Keyframes for an animatic (opornye kadry) › 5. Emotion without faces in a still | 17 |
| 809 | `skills/video/references/animatic-keyframes.md` | Keyframes for an animatic (opornye kadry) › 6. The loaded frame for one panel | 14 |
| 810 | `skills/video/references/animatic-keyframes.md` | Keyframes for an animatic (opornye kadry) › 7. From keyframe to image-gen prompt | 11 |
| 811 | `skills/video/references/animatic-keyframes.md` | Keyframes for an animatic (opornye kadry) › 8. Worked keyframe board for a 30s race spot | 19 |
| 812 | `skills/video/references/animatic-keyframes.md` | Keyframes for an animatic (opornye kadry) › 9. Checklist: does this keyframe earn its place | 16 |
| 815 | `skills/video/references/camera-lighting-vocabulary.md` | Camera, lighting, color, sound vocabulary › 1. Framing | 18 |
| 817 | `skills/video/references/camera-lighting-vocabulary.md` | Camera, lighting, color, sound vocabulary › 3. Lens language | 11 |
| 818 | `skills/video/references/camera-lighting-vocabulary.md` | Camera, lighting, color, sound vocabulary › 4. Light sources | 20 |
| 819 | `skills/video/references/camera-lighting-vocabulary.md` | Camera, lighting, color, sound vocabulary › 5. Light direction | 10 |
| 820 | `skills/video/references/camera-lighting-vocabulary.md` | Camera, lighting, color, sound vocabulary › 6. Light quality | 17 |
| 821 | `skills/video/references/camera-lighting-vocabulary.md` | Camera, lighting, color, sound vocabulary › 7. Color discipline | 11 |
| 867 | `skills/video/references/fixes-and-skeletons.md` | Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Melting hands / extra fingers | 5 |
| 870 | `skills/video/references/fixes-and-skeletons.md` | Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Weird AI-looking faces | 3 |
| 871 | `skills/video/references/fixes-and-skeletons.md` | Fixes, checklist, and cross-model skeletons › 2. Common failures and fixes › Twins / face-blending in multi-person scenes | 4 |
| 957 | `skills/video/references/race-and-speed.md` | Race, speed and faceless kinetic montage › 3. Selling speed in a single frame | 16 |
| 962 | `skills/video/references/race-and-speed.md` | Race, speed and faceless kinetic montage › 7. Light & color for speed without faces | 2 |
| 963 | `skills/video/references/race-and-speed.md` | Race, speed and faceless kinetic montage › 7. Light & color for speed without faces › The cold combative palette | 11 |
| 964 | `skills/video/references/race-and-speed.md` | Race, speed and faceless kinetic montage › 7. Light & color for speed without faces › Concrete lighting recipes (drop-in for the format-C Light column: source · direction · quality · what it rims) | 10 |
| 967 | `skills/video/references/race-and-speed.md` | Race, speed and faceless kinetic montage › 10. Anti-fake guard | 15 |
| 1183 | `skills/visual-media/SKILL.md` | Creación Visual — Visual Media › Fundamentos de fotografía › Triángulo de exposición | 2 |
| 1184 | `skills/visual-media/SKILL.md` | Creación Visual — Visual Media › Fundamentos de fotografía › Reglas de composición | 2 |
| 1185 | `skills/visual-media/SKILL.md` | Creación Visual — Visual Media › Fundamentos de fotografía › Uso de la luz | 9 |
| 1230 | `skills/visual-prompt-forge/SKILL.md` | Visual Prompt Forge › Adapters | 14 |
| 1233 | `skills/visual-prompt-forge/adapters/_capabilities.json` | (documento completo) | 167 |
| 1337 | `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` | One Shot, All Adapters | 2 |
| 1338 | `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` | One Shot, All Adapters › The source shot | 3 |
| 1339 | `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` | One Shot, All Adapters › Series lock context (constant across all adapters) | 2 |
| 1340 | `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` | One Shot, All Adapters › Brand mood | 2 |
| 1341 | `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` | One Shot, All Adapters › Outputs | 17 |
| 1342 | `skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md` | One Shot, All Adapters › What's not in any prompt | 3 |
