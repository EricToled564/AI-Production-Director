# Anatomía del frío — Etapa 5: génesis de anclas

Dos modelos, cada uno donde la base de reglas lo sostiene:

- **T1 (rostro) y T2 (cuerpo) → GPT Image 2.** Consulté `rule_query.py` de nuevo con el brief corregido ('retrato cinemático elegante de un músico atractivo... no documental duro') y la base señaló `image/references/patterns/portrait-cinema.md`: para retratos cálidos/editoriales con piel bien renderizada, ese archivo recomienda **GPT Image 2**, no Nano Banana Pro. La v1 de este documento aplicó el template T1 de `produccion-visual-sw30/SKILL.md` (calibrado para documental deportivo duro de Sports World) sin cruzarlo contra el registro real de este proyecto — error mío, no de la base de reglas; corregido aquí.
- **Placa vacía, inserción secuencial y las 3 anclas de conjunto → Nano Banana Pro.** Aquí sí aplica de lleno `.claude/rules/regimenes/09-grupo-ensamble.md`: NBP sostiene hasta 5 identidades de personaje por pasada, exactamente el tamaño del quinteto, y las referencias cruzadas entre pasos (T2 exportado como imagen) funcionan igual de bien viniendo de GPT Image 2.

Todos los prompts pasaron `.claude/hooks/aurora/prompt_linter.py` (copia parcheada v1.2-fupai) con `STATUS: PASS` — comando exacto de cada uno en `output/genesis/LINT_LOG.md`.

## Historial de correcciones (feedback de Eric, 2026-09-25)

1. **Blanco y negro no pedido.** Causa: `produccion-visual-sw30/SKILL.md:73` fija 'Kodak Tri-X' (stock B/N) para todo T1. Corregido en la revisión b.
2. **Rostros poco favorecedores** ('parece un prisionero de guerra'). Causa: se apiló daño documental (parches, descamación, dientes torcidos) no canonizado encima del template de piel real de SW30. Corregido en la revisión b (piel real pero elenco atractivo).
3. **Sigue leyendo ambiguo/no claramente atractivo** incluso a color. Causa raíz real: el propio template SW30 no es el registro correcto para este proyecto — está calibrado para documental deportivo, no para un video musical cinematográfico. Corregido en esta revisión c: T1/T2 se reescriben en el formato de 5 slots de GPT Image 2 siguiendo `portrait-cinema.md`, no el molde de SW30. Se conservan los anclas de identidad ya citados en `02-guion.md`/`shots.json` (cicatriz y caballete de Vera, lentes de Ilan, aro de Noor, pelo blanco de Tomás, tatuaje de Kai) porque tocarlos de verdad revisaría contenido de un gate ya aprobado — pendiente de decisión de Eric si el corte de pelo específico de Vera sigue leyendo ambiguo en la imagen generada.

---

## T1 — maestros de rostro (GPT Image 2, sin referencia)

### T1 · Vera (primer violín)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- (ninguna — génesis desde texto)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Vera, a beautiful woman in her mid-thirties, a first violinist, frozen mid-breath a second before playing, head and shoulders, three-quarter framing, eyes straight on the lens.
Important Details: delicate symmetrical features, soft full lips, elegant cheekbones, naturally arched eyebrows, long dark lashes, a thin pale scar through the left eyebrow and a small elegant bump on the nose bridge read as character. Very short black hair styled as a fashion-forward undercut with a soft side-swept fringe on top and a clean shaved nape. Skin rendered naturally with warm undertones — no heavy smoothing, visible pores, a light natural sheen at the hairline, a light touch of makeup on the brows and lips. Wearing a black linen shirt with the top buttons open at the throat. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized character face reference for a music video, to be reused across every later shot of this person.
Constraints: face must be clearly visible and well-exposed, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Formato de 5 slots (Scene/Subject/Important Details/Use Case/Constraints) por portrait-cinema.md.
- Al aprobar: canonizar con hash como maestro T1 de Vera antes de generar su T2.
```

### T1 · Ilan (segundo violín)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- (ninguna — génesis desde texto)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Ilan, a distinguished, good-looking man in his early forties, a second violinist, frozen mid-breath a second before playing, head and shoulders, three-quarter framing, eyes straight on the lens through thin metal-rimmed glasses.
Important Details: a receding hairline, a well-groomed short grey beard, kind deep-set eyes, strong symmetrical bone structure. Skin rendered naturally with warm undertones — no heavy smoothing, visible pores, a light natural sheen on the upper lip, faint smile lines, individual grey hairs visible in the beard. Wearing a black jacket collar, no tie, top button open. Two warm reflections catch in the lenses. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized character face reference for a music video, to be reused across every later shot of this person.
Constraints: face must be clearly visible and well-exposed, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Formato de 5 slots (Scene/Subject/Important Details/Use Case/Constraints) por portrait-cinema.md.
- Al aprobar: canonizar con hash como maestro T1 de Ilan antes de generar su T2.
```

### T1 · Noor (viola)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- (ninguna — génesis desde texto)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Noor, a beautiful woman in her late twenties, a violist, frozen mid-breath a second before playing, head and shoulders, three-quarter framing, eyes straight on the lens.
Important Details: a small gold nose ring through the left nostril, a long dark braid pulled over the right shoulder with loose strands escaping at the temple, delicate symmetrical features, full lips, naturally arched eyebrows, long lashes. Skin rendered naturally with warm undertones — no heavy smoothing, visible pores, a light natural sheen at the brow, a light touch of makeup on the brows and lips. Wearing a sleeveless black high-neck top at the collarbone. A bright specular point catches the nose ring. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized character face reference for a music video, to be reused across every later shot of this person.
Constraints: face must be clearly visible and well-exposed, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Formato de 5 slots (Scene/Subject/Important Details/Use Case/Constraints) por portrait-cinema.md.
- Al aprobar: canonizar con hash como maestro T1 de Noor antes de generar su T2.
```

### T1 · Tomas (cello)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- (ninguna — génesis desde texto)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Tomas, a distinguished, handsome man in his early fifties, a cellist, frozen mid-breath a second before playing, head and shoulders, three-quarter framing, eyes straight on the lens.
Important Details: long white hair tied back at the nape with loose strands at the temple, a strong jaw, kind eyes with a few natural creases at the corners, symmetrical weathered features that read as dignified. Skin rendered naturally with warm undertones — no heavy smoothing, visible pores, a light natural sheen on the forehead, neatly kept white stubble at the jawline. Wearing an open black waistcoat collar over a black shirt. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized character face reference for a music video, to be reused across every later shot of this person.
Constraints: face must be clearly visible and well-exposed, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Formato de 5 slots (Scene/Subject/Important Details/Use Case/Constraints) por portrait-cinema.md.
- Al aprobar: canonizar con hash como maestro T1 de Tomas antes de generar su T2.
```

### T1 · Kai (contrabajo)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- (ninguna — génesis desde texto)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Kai, a striking, handsome man in his early thirties, a double bassist, frozen mid-breath a second before playing, head and shoulders, three-quarter framing, eyes straight on the lens.
Important Details: a shaved head, strong symmetrical features, a sharp defined jawline, a light shadow of stubble. Skin rendered naturally with warm undertones — no heavy smoothing, visible pores, a light natural sheen on the shaved scalp. Wearing a fitted black t-shirt collar at the throat. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized character face reference for a music video, to be reused across every later shot of this person.
Constraints: face must be clearly visible and well-exposed, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Formato de 5 slots (Scene/Subject/Important Details/Use Case/Constraints) por portrait-cinema.md.
- Al aprobar: canonizar con hash como maestro T1 de Kai antes de generar su T2.
```

---

## T2 — maestros de cuerpo (GPT Image 2, referencia: T1 aprobado)

### T2 · Vera (primer violín, cuerpo completo)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- Image 1 = T1 de Vera aprobado y canonizado (rol: character)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, a plain grey floor, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Image 1 is the approved character reference of Vera — keep the facial features exactly the same, ignore its plain background. Full body, standing, holding a violin under her chin and a bow raised in her right hand, frozen mid-breath a second before playing.
Important Details: same face as Image 1, the elegant nose bridge bump, the thin scar through the left eyebrow, the shaved nape. Athletic, confident straight posture, defined forearms with a faint raised vein from the grip. Wearing a black linen shirt rolled to the elbow and plain black trousers. A bright specular highlights the violin varnish and the bow hair. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized full-body character reference for a music video, to be reused across every later shot of this person.
Constraints: keep the face identical to Image 1, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Herencia mínima (SW30 R5): 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
```

### T2 · Ilan (segundo violín, cuerpo completo)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- Image 1 = T1 de Ilan aprobado y canonizado (rol: character)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, a plain grey floor, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Image 1 is the approved character reference of Ilan — keep the facial features exactly the same, ignore its plain background. Full body, standing, holding a violin under his chin and a bow raised in his right hand, frozen mid-breath a second before playing.
Important Details: same face as Image 1, the receding hairline, the short grey beard, the thin metal-rimmed glasses. Upright confident posture, a firm grip with the thumb pressing on the bow's frog. Wearing a black jacket, no tie, top button open, plain black trousers. Two warm reflections catch in the lenses; a bright specular highlights the violin varnish. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized full-body character reference for a music video, to be reused across every later shot of this person.
Constraints: keep the face identical to Image 1, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Herencia mínima (SW30 R5): 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
```

### T2 · Noor (viola, cuerpo completo)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- Image 1 = T1 de Noor aprobado y canonizado (rol: character)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, a plain grey floor, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Image 1 is the approved character reference of Noor — keep the facial features exactly the same, ignore its plain background. Full body, standing, holding a viola under her chin and a bow raised in her right hand, frozen mid-breath a second before playing.
Important Details: same face as Image 1, the gold nose ring, the long dark braid over the right shoulder. Confident upright posture, wiry defined forearms, the braid slightly loosened at the tie. Wearing a sleeveless black high-neck dress and plain black shoes. A bright specular highlights the nose ring and the viola varnish. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized full-body character reference for a music video, to be reused across every later shot of this person.
Constraints: keep the face identical to Image 1, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Herencia mínima (SW30 R5): 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
```

### T2 · Tomas (cello, cuerpo completo)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- Image 1 = T1 de Tomas aprobado y canonizado (rol: character)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, a plain grey floor, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Image 1 is the approved character reference of Tomas — keep the facial features exactly the same, ignore its plain background. Full body, seated, with a cello between his knees, left hand gripping the neck and a bow raised in his right hand, frozen mid-breath a second before playing.
Important Details: same face as Image 1, the long white hair tied at the nape, the strong jaw, the kind eyes. Large capable hands with a firm grip on the cello neck, an upright dignified seated posture, a faint raised vein crossing the forearm. Wearing an open black waistcoat over a black shirt and plain black trousers. A bright specular highlights the cello's f-hole edge and the bow hair. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized full-body character reference for a music video, to be reused across every later shot of this person.
Constraints: keep the face identical to Image 1, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Herencia mínima (SW30 R5): 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
```

### T2 · Kai (contrabajo, cuerpo completo)

```
Model: gpt-image-2 — quality: high
Size / Ratio: 4:5

References:
- Image 1 = T1 de Kai aprobado y canonizado (rol: character)

Prompt:
Scene: bare dark studio room, dropping to black with no detail, a plain grey floor, one single hard warm tungsten light source raking in from camera-left, no fill.
Subject: Image 1 is the approved character reference of Kai — keep the facial features exactly the same, ignore its plain background. Full body, standing behind a double bass with his left hand on the neck and a bow raised in his right hand, frozen mid-breath a second before playing.
Important Details: same face as Image 1, the shaved head, the sharp defined jawline. A fine-line geometric tattoo on the right forearm, broad confident shoulders, a light natural sheen on the shaved scalp. Wearing a fitted black t-shirt and plain black trousers. A bright specular highlights the bass's varnish and the tattoo's ink line. A real documentary photograph, photoreal skin texture, not an illustration. Warm tungsten color temperature, natural contrast, no HDR look.
Use Case: canonized full-body character reference for a music video, to be reused across every later shot of this person.
Constraints: keep the face identical to Image 1, natural color photograph, not black and white, no beauty retouching or plastic complexion, no cartoon or 3D render, no extra people, no text or logos.

Notes:
- Herencia mínima (SW30 R5): 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
```

---

## Placa vacía del escenario (Nano Banana Pro)

### Placa · escenario vacío con anclas de posición

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 1K revisión, 2K/4K en la toma aprobada (placa se reutiliza en las 5 inserciones)

References:
- (ninguna — génesis desde texto)

Prompt:
Create a documentary photograph of an indoor bare performance stage, the subject of the frame is the stage itself, empty and ready for five string players to take their marks. Bare black stage with no visible back wall, dark matte floor with white gaffer-tape marks at the feet of each of five black music stands set in an open arc: Vera front-left, Ilan front-right, Noor centre-back, Tomas seated back-left, Kai standing back-right. Rosin dust hangs in the air. Nothing else on stage, no audience. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide static composition, eye level, symmetry of the open arc reads clearly. Fine detail on the gaffer-tape marks and on the rosin haze. Kodak Tri-X reportage look, visible grain in the shadows. Format: 16:9.

Notes:
- Sin ninguna persona (R2/R3): los cinco atriles y las marcas de cinta blanca son las anclas de posición.
- environment/lighting/color_grade de series_lock van verbatim.
```

---

## Inserción secuencial (Nano Banana Pro) — construye la composición canónica

### Inserción 1 · +Vera (front-left)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa vacía (rol: location)
- Image 2 = T2 de Vera, exportado de GPT Image 2 y aprobado (rol: character)

Prompt:
Image 1: the empty stage plate, keep the world of Image 1 untouched. Image 2: character reference of Vera, use only the person from Image 2, ignore its plain background. Place Vera standing at the white gaffer-tape mark front-left of Image 1, bow raised in her right hand, frozen mid-breath a second before playing, body oriented into the open arc. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, the four other stands and the rest of Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched': ningún miembro ya insertado se re-describe.
- Salida de la Inserción 5 = composición canónica del quinteto.
```

### Inserción 2 · +Ilan (front-right)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa con Vera ya colocada (rol: location)
- Image 2 = T2 de Ilan, exportado de GPT Image 2 y aprobado (rol: character)

Prompt:
Image 1: the plate with Vera already placed, keep every person already placed in Image 1 untouched. Image 2: character reference of Ilan, use only the person from Image 2, ignore its plain background. Place Ilan standing at the white gaffer-tape mark front-right of Image 1, bow raised in his right hand, frozen mid-breath a second before playing, body oriented into the open arc, facing Vera across the arc. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, the three other stands and the rest of Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched': ningún miembro ya insertado se re-describe.
- Salida de la Inserción 5 = composición canónica del quinteto.
```

### Inserción 3 · +Noor (centre-back)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa con Vera e Ilan ya colocados (rol: location)
- Image 2 = T2 de Noor, exportado de GPT Image 2 y aprobado (rol: character)

Prompt:
Image 1: the plate with Vera and Ilan already placed, keep every person already placed in Image 1 untouched. Image 2: character reference of Noor, use only the person from Image 2, ignore its plain background. Place Noor standing at the white gaffer-tape mark centre-back of Image 1, bow raised in her right hand, frozen mid-breath a second before playing, body oriented into the open arc, framed between Vera and Ilan. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, the two other stands and the rest of Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched': ningún miembro ya insertado se re-describe.
- Salida de la Inserción 5 = composición canónica del quinteto.
```

### Inserción 4 · +Tomas (back-left)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa con Vera, Ilan y Noor ya colocados (rol: location)
- Image 2 = T2 de Tomas, exportado de GPT Image 2 y aprobado (rol: character)

Prompt:
Image 1: the plate with Vera, Ilan and Noor already placed, keep every person already placed in Image 1 untouched. Image 2: character reference of Tomas, use only the person from Image 2, ignore its plain background. Place Tomas seated at the white gaffer-tape mark back-left of Image 1, left hand gripping the neck of his instrument and bow raised in his right hand, frozen mid-breath a second before playing, body oriented into the open arc. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, the remaining stand and the rest of Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched': ningún miembro ya insertado se re-describe.
- Salida de la Inserción 5 = composición canónica del quinteto.
```

### Inserción 5 · +Kai (back-right)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa con Vera, Ilan, Noor y Tomas ya colocados (rol: location)
- Image 2 = T2 de Kai, exportado de GPT Image 2 y aprobado (rol: character)

Prompt:
Image 1: the plate with Vera, Ilan, Noor and Tomas already placed, keep every person already placed in Image 1 untouched. Image 2: character reference of Kai, use only the person from Image 2, ignore its plain background. Place Kai standing at the white gaffer-tape mark back-right of Image 1, left hand on the neck of his instrument and bow raised in his right hand, frozen mid-breath a second before playing, body oriented into the open arc, closing the quintet. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, all four other players from Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched': ningún miembro ya insertado se re-describe.
- Salida de la Inserción 5 = composición canónica del quinteto.
```

---

## Tres anclas de conjunto (Nano Banana Pro) — edición sobre la composición canónica

### Ancla 1 · Apertura (0.0s)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K/4K directo

References:
- Image 1 = composición canónica del quinteto (rol: ff)

Prompt:
Image 1: the canonical quintet composition, use only what Image 1 already shows, do not re-describe the five people, their wardrobe or the instruments. Five bows landing on the strings at once, frozen mid-impact, rosin bursting up from the strings. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation. Wide shot, eye level, static frame centred at the middle of the open arc, white gaffer-tape marks visible at their feet. Format: 16:9.

Notes:
- Por qué esta ancla: el golpe inicial, corona baja (ver 03-direccion.md y shots.json).
```

### Ancla 2 · Tormenta (52.0s, ángulo bajo)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K/4K directo

References:
- Image 1 = composición canónica del quinteto (rol: ff)

Prompt:
Image 1: the canonical quintet composition, use only what Image 1 already shows, do not re-describe the five people, their wardrobe or the instruments. Change camera to a low angle, looking up at the quintet. Five right arms at the same angle, frozen mid-stroke, five bows coming down together, rosin exploding into the beam so the light reads as a solid body. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation. Wide shot, low angle, static frame, in front of the arc looking up. Format: 16:9.

Notes:
- Por qué esta ancla: segundo plano de conjunto (ver 03-direccion.md y shots.json).
```

### Ancla 3 · Acorde final (77.4s)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K/4K directo

References:
- Image 1 = composición canónica del quinteto (rol: ff)

Prompt:
Image 1: the canonical quintet composition, use only what Image 1 already shows, do not re-describe the five people, their wardrobe or the instruments. Five bows stopped in the air at the same height after the last chord, frozen a beat after impact, five chests rising and falling together, all five faces legible. Rosin still falling through the beam. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation. Wide shot, eye level, static frame from the front, level with the middle of the open arc. Format: 16:9.

Notes:
- Por qué esta ancla: las cinco identidades deben verificarse (ver 03-direccion.md y shots.json).
```
