# Anatomía del frío — Etapa 5: génesis de anclas (Nano Banana Pro)

Modelo: **Nano Banana Pro** (`gemini-3-pro-image`), decisión ya tomada en `01-estrategia.md` y sostenida por `.claude/rules/regimenes/09-grupo-ensamble.md` (NBP sostiene hasta 5 identidades de personaje por pasada — exactamente el tamaño de este quinteto). Todos los prompts pasaron `.claude/hooks/aurora/prompt_linter.py` (copia parcheada v1.2-fupai) con `STATUS: PASS` — el comando exacto de cada uno está en `output/genesis/LINT_LOG.md`.

## Corrección 2026-09-25b (feedback de Eric)

Dos errores reales en la primera versión, no decisiones de dirección:

1. **Blanco y negro no pedido.** `produccion-visual-sw30/SKILL.md:73` fija `Kodak Tri-X` (una película histórica de blanco y negro) como el stock del bloque `usecase_doc` de todo T1. Se aplicó literal sin notar el choque con la propia paleta a color de `brand-lock.md` (ámbar cálido sobre negros neutros). Reemplazado en los 10 T1/T2 por **Kodak Vision3 500T**, negativo de cine a color balanceado a tungsteno — mismo espíritu documental sin retoque, pero a color y coherente con la luz de tungsteno ya establecida.
2. **Rostros poco favorecedores.** El template T1 de SW30 pide cara irregular para evitar el look plástico, y esta versión apiló demasiado encima (parches rojos, descamación, dientes torcidos, asimetría extra no canonizada) — el resultado leía a documental de prisión, no a músico de un video musical. Reescrito: se conservan solo los anclas de identidad que **ya están citados en `03-direccion.md` y en las rationale de `shots.json`** (la cicatriz y el caballete de la nariz de Vera, los lentes y la barba de Ilan, el aro y la trenza de Noor, el pelo blanco de Tomás, el tatuaje de Kai) y se pide explícitamente un elenco atractivo con piel real pero no dañada.

## Método (family 09, R1/R2/R7 — `.claude/rules/regimenes/09-grupo-ensamble.md`)

1. **T1 — maestro de rostro**, sin referencia, template SW30 adaptado (luz dura, piel real sin retoque, cara atractiva y simétrica con solo sus anclas de identidad ya canonizados), ~200-220 palabras. Uno por músico.
2. **T2 — maestro de cuerpo**, con el T1 aprobado como referencia de personaje ('Image 1'), cuerpo entero con el instrumento, mismo fondo neutro de estudio. Uno por músico.
3. **Placa vacía** del escenario, con las cinco marcas de cinta y los cinco atriles como anclas de posición legibles (R2), sin ninguna persona.
4. **Inserción secuencial** (R7): cada T2 aprobado se inserta uno a la vez sobre la placa acumulada, 'keep every person already placed in Image 1 untouched', hasta tener el quinteto completo — la **composición canónica**.
5. **Tres anclas por edición, no por regeneración** (SW30 R11/R12 'Edit, don't re-roll'): las tres imágenes de conjunto de `03-direccion.md` (apertura 0.0s, tormenta 52.0s ángulo bajo, acorde final 77.4s) se piden como ediciones de la composición canónica (`--ref-role ff`: no se repite ninguna descripción de personas, vestuario ni props — ya están fijados por la referencia), describiendo solo el delta de pose/cámara/estado del polvo de resina.

**Riesgo declarado (family 06 research, C-22/C-23):** un A/B fechado (2026-04-22) dio a NBP la ventaja en piel/poros/gotas en el aire pero a GPT Image 2 la tipografía; y `image/references/nano-banana.md` documenta que *"NBP a veces sostiene peor los rostros"* que NB2. Mitigación: cada T1 se generó pensado para NBP pero, si el rostro deriva entre T1 y T2 o entre pasos de inserción, el método SW30 (regla 13, máx. 2 intentos por método) manda cambiar a NB2 para ese T1/T2 puntual antes de re-intentar NBP.

---

## T1 — maestros de rostro (sin referencia)

### T1 · Vera (primer violín)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — generar primero a 1K para revisión, regenerar la toma aprobada a 2K

References:
- (ninguna — génesis desde texto)

Prompt:
Create a color documentary portrait of an attractive woman in her mid-thirties, a first violinist, frozen mid-breath a second before playing. Head and shoulders, three-quarter framing, eyes straight on the lens. Striking, symmetrical features, sharp cheekbones, very short black hair with a shaved nape. A thin pale scar through the left eyebrow and a small elegant bump on the nose bridge read as character, not damage. Skin is real, not airbrushed: fine visible pores, a light natural sheen of sweat at the hairline, a few individual fine hairs along the jaw, healthy even tone with subtle natural color variation, no makeup. Wearing a black linen shirt collar rolled to the throat. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, so skin texture reads at full size without looking harsh or unflattering. Background is a bare dark studio room, dropping to black with no detail. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: pores, collar weave, eyelashes. Format: 4:5.

Notes:
- Elenco atractivo a color (Kodak Vision3 500T); anclas de identidad solo las ya canonizadas.
- Sin luz suave/Portra: prohibido en rostros por el template SW30; piel real sin retoque, no dañada.
- Al aprobar: canonizar con hash como maestro T1 de Vera antes de generar su T2.
```

### T1 · Ilan (segundo violín)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — generar primero a 1K para revisión, regenerar la toma aprobada a 2K

References:
- (ninguna — génesis desde texto)

Prompt:
Create a color documentary portrait of a distinguished, good-looking man in his early forties, a second violinist, frozen mid-breath a second before playing. Head and shoulders, three-quarter framing, eyes straight on the lens through thin metal-rimmed glasses. A receding hairline, a well-groomed short grey beard, kind deep-set eyes, strong symmetrical bone structure. Skin is real, not airbrushed: fine visible pores, a light natural sheen of sweat on the upper lip, faint smile lines at the eyes, healthy even tone, individual grey hairs visible in the beard. Wearing a black jacket collar, no tie, top button open. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, catching two warm reflections in the lenses and giving the face natural dimension without looking harsh. Background is a bare dark studio room, dropping to black with no detail. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: pores, beard hair, lens reflections. Format: 4:5.

Notes:
- Elenco atractivo a color (Kodak Vision3 500T); anclas de identidad solo las ya canonizadas.
- Sin luz suave/Portra: prohibido en rostros por el template SW30; piel real sin retoque, no dañada.
- Al aprobar: canonizar con hash como maestro T1 de Ilan antes de generar su T2.
```

### T1 · Noor (viola)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — generar primero a 1K para revisión, regenerar la toma aprobada a 2K

References:
- (ninguna — génesis desde texto)

Prompt:
Create a color documentary portrait of a striking, good-looking woman in her late twenties, a violist, frozen mid-breath a second before playing. Head and shoulders, three-quarter framing, eyes straight on the lens. A small gold nose ring through the left nostril, a long dark braid pulled over the right shoulder with loose strands escaping at the temple, symmetrical features, full lips. Skin is real, not airbrushed: fine visible pores across the forehead, a light natural sheen of sweat at the brow, healthy even tone with subtle natural color variation, no makeup. Wearing a sleeveless black high-neck top at the collarbone. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, catching a bright specular point on the nose ring and giving the face natural dimension without looking harsh. Background is a bare dark studio room, dropping to black with no detail. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: pores, braid strands, nose ring. Format: 4:5.

Notes:
- Elenco atractivo a color (Kodak Vision3 500T); anclas de identidad solo las ya canonizadas.
- Sin luz suave/Portra: prohibido en rostros por el template SW30; piel real sin retoque, no dañada.
- Al aprobar: canonizar con hash como maestro T1 de Noor antes de generar su T2.
```

### T1 · Tomas (cello)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — generar primero a 1K para revisión, regenerar la toma aprobada a 2K

References:
- (ninguna — génesis desde texto)

Prompt:
Create a color documentary portrait of a distinguished, handsome man in his early fifties, a cellist, frozen mid-breath a second before playing. Head and shoulders, three-quarter framing, eyes straight on the lens. Long white hair tied back at the nape with loose strands at the temple, a strong jaw, kind eyes with a few natural creases at the corners, symmetrical weathered features that read as dignified. Skin is real, not airbrushed: fine visible pores, a light natural sheen of sweat on the forehead, neatly kept white stubble at the jawline, healthy even tone. Wearing an open black waistcoat collar over a black shirt. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, giving the face natural dimension and carving gentle definition without looking harsh. Background is a bare dark studio room, dropping to black with no detail. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: pores, stubble, fabric weave of the collar. Format: 4:5.

Notes:
- Elenco atractivo a color (Kodak Vision3 500T); anclas de identidad solo las ya canonizadas.
- Sin luz suave/Portra: prohibido en rostros por el template SW30; piel real sin retoque, no dañada.
- Al aprobar: canonizar con hash como maestro T1 de Tomas antes de generar su T2.
```

### T1 · Kai (contrabajo)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — generar primero a 1K para revisión, regenerar la toma aprobada a 2K

References:
- (ninguna — génesis desde texto)

Prompt:
Create a color documentary portrait of a striking, handsome man in his early thirties, a double bassist, frozen mid-breath a second before playing. Head and shoulders, three-quarter framing, eyes straight on the lens. A shaved head, strong symmetrical features, a sharp defined jawline, a light shadow of stubble. Skin is real, not airbrushed: fine visible pores across the forehead, a light natural sheen of sweat on the shaved scalp, healthy even tone. Wearing a fitted black t-shirt collar at the throat. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, giving the face natural dimension and a soft highlight along the scalp without looking harsh. Background is a bare dark studio room, dropping to black with no detail. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: pores, stubble, scalp texture. Format: 4:5.

Notes:
- Elenco atractivo a color (Kodak Vision3 500T); anclas de identidad solo las ya canonizadas.
- Sin luz suave/Portra: prohibido en rostros por el template SW30; piel real sin retoque, no dañada.
- Al aprobar: canonizar con hash como maestro T1 de Kai antes de generar su T2.
```

---

## T2 — maestros de cuerpo (referencia: T1 aprobado)

### T2 · Vera (primer violín, cuerpo completo)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — 1K revisión, 2K en la toma aprobada

References:
- Image 1 = T1 de Vera aprobado y canonizado (rol: character)

Prompt:
Image 1: character reference — keep the facial features exactly the same, ignore its plain background. Create a color documentary photograph of the same woman, full body, standing holding a violin under her chin and a bow raised in her right hand, frozen mid-breath a second before playing. Same face as Image 1: the elegant nose bridge bump, the thin scar through the left eyebrow, the shaved nape. Body is athletic and real, not airbrushed: defined forearms, a faint raised vein on the back of the right hand from the grip, confident straight posture. Wearing a black linen shirt rolled to the elbow and plain black trousers. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, a bright specular on the violin varnish and on the bow hair. Background is a bare dark studio room, dropping to black with no detail, a plain grey floor under her feet. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: forearm texture, varnish specular, fabric weave. Format: 4:5.

Notes:
- Herencia mínima (SW30 R5): solo se repite 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
- El fondo sigue siendo el estudio neutro del T1, no el escenario — la puesta en escena llega en la inserción.
```

### T2 · Ilan (segundo violín, cuerpo completo)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — 1K revisión, 2K en la toma aprobada

References:
- Image 1 = T1 de Ilan aprobado y canonizado (rol: character)

Prompt:
Image 1: character reference — keep the facial features exactly the same, ignore its plain background. Create a color documentary photograph of the same man, full body, standing holding a violin under his chin and a bow raised in his right hand, frozen mid-breath a second before playing. Same face as Image 1: the receding hairline, the short grey beard, the thin metal-rimmed glasses. Body is real, not airbrushed: an upright confident posture, a firm grip with the thumb pressing on the bow's frog, sparse chest hair visible above the open collar. Wearing a black jacket, no tie, top button open, plain black trousers. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, two warm reflections in the lenses and a bright specular on the violin varnish. Background is a bare dark studio room, dropping to black with no detail, a plain grey floor under his feet. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: lens reflections, varnish specular, fabric weave. Format: 4:5.

Notes:
- Herencia mínima (SW30 R5): solo se repite 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
- El fondo sigue siendo el estudio neutro del T1, no el escenario — la puesta en escena llega en la inserción.
```

### T2 · Noor (viola, cuerpo completo)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — 1K revisión, 2K en la toma aprobada

References:
- Image 1 = T1 de Noor aprobado y canonizado (rol: character)

Prompt:
Image 1: character reference — keep the facial features exactly the same, ignore its plain background. Create a color documentary photograph of the same woman, full body, standing holding a viola under her chin and a bow raised in her right hand, frozen mid-breath a second before playing. Same face as Image 1: the gold nose ring, the long dark braid over the right shoulder. Body is athletic and real, not airbrushed: a confident upright posture, wiry defined forearms, the braid slightly loosened at the tie. Wearing a sleeveless black high-neck dress and plain black shoes. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, a bright specular point on the nose ring and on the viola varnish. Background is a bare dark studio room, dropping to black with no detail, a plain grey floor under her feet. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: forearm texture, varnish specular, fabric weave. Format: 4:5.

Notes:
- Herencia mínima (SW30 R5): solo se repite 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
- El fondo sigue siendo el estudio neutro del T1, no el escenario — la puesta en escena llega en la inserción.
```

### T2 · Tomas (cello, cuerpo completo)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — 1K revisión, 2K en la toma aprobada

References:
- Image 1 = T1 de Tomas aprobado y canonizado (rol: character)

Prompt:
Image 1: character reference — keep the facial features exactly the same, ignore its plain background. Create a color documentary photograph of the same man, full body, seated with a cello between his knees, left hand gripping the neck and a bow raised in his right hand, frozen mid-breath a second before playing. Same face as Image 1: the long white hair tied at the nape, the strong jaw, the kind eyes. Body is real, not airbrushed: large capable hands with a firm grip on the cello neck, an upright dignified seated posture, a faint raised vein crossing the forearm. Wearing an open black waistcoat over a black shirt and plain black trousers. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, a bright specular on the cello's f-hole edge and on the bow hair. Background is a bare dark studio room, dropping to black with no detail, a plain grey floor under the chair. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: hand texture, cello varnish specular, fabric weave. Format: 4:5.

Notes:
- Herencia mínima (SW30 R5): solo se repite 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
- El fondo sigue siendo el estudio neutro del T1, no el escenario — la puesta en escena llega en la inserción.
```

### T2 · Kai (contrabajo, cuerpo completo)

```
Model: nano-banana-pro
Size / Ratio: 4:5 — 1K revisión, 2K en la toma aprobada

References:
- Image 1 = T1 de Kai aprobado y canonizado (rol: character)

Prompt:
Image 1: character reference — keep the facial features exactly the same, ignore its plain background. Create a color documentary photograph of the same man, full body, standing behind a double bass with his left hand on the neck and a bow raised in his right hand, frozen mid-breath a second before playing. Same face as Image 1: the shaved head, the sharp defined jawline. Body is athletic and real, not airbrushed: a fine-line geometric tattoo on the right forearm, broad confident shoulders, a light natural sheen of sweat on the shaved scalp. Wearing a fitted black t-shirt and plain black trousers. Hard light: one single hard warm tungsten source raking in from camera-left, no fill, a bright specular on the bass's varnish and on the tattoo's ink line. Background is a bare dark studio room, dropping to black with no detail, a plain grey floor under his feet. Kodak Vision3 500T color, tungsten-balanced documentary look, natural contrast, visible fine grain in the shadows, no HDR look, no black and white. Anti-beauty rules: no digital retouching, no skin smoothing, no plastic complexion, no soft fill light — the person is naturally good-looking, the skin is simply unretouched. Fine detail at 100 percent: tattoo linework, varnish specular, fabric weave. Format: 4:5.

Notes:
- Herencia mínima (SW30 R5): solo se repite 'same face as Image 1' + los deltas de cuerpo/vestuario/instrumento.
- El fondo sigue siendo el estudio neutro del T1, no el escenario — la puesta en escena llega en la inserción.
```

---

## Placa vacía del escenario

### Placa · escenario vacío con anclas de posición

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 1K revisión, 2K/4K en la toma aprobada (placa se reutiliza en las 5 inserciones)

References:
- (ninguna — génesis desde texto)

Prompt:
Create a documentary photograph of an indoor bare performance stage, the subject of the frame is the stage itself, empty and ready for five string players to take their marks. Bare black stage with no visible back wall, dark matte floor with white gaffer-tape marks at the feet of each of five black music stands set in an open arc: Vera front-left, Ilan front-right, Noor centre-back, Tomas seated back-left, Kai standing back-right. Rosin dust hangs in the air. Nothing else on stage, no audience. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide static composition, eye level, symmetry of the open arc reads clearly. Fine detail on the gaffer-tape marks and on the rosin haze. Kodak Tri-X reportage look, visible grain in the shadows. Format: 16:9.

Notes:
- Sin ninguna persona (R2/R3): los cinco atriles y las marcas de cinta blanca son las anclas de posición que fijan dónde entra cada músico en la inserción secuencial.
- environment/lighting/color_grade de `series_lock` van verbatim; ver LINT_LOG.md para el WARN esperado de 'character' (no aplica, la placa no tiene personas).
```

---

## Inserción secuencial (R7) — construye la composición canónica del quinteto

### Inserción 1 · +Vera (front-left)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa vacía (rol: location)
- Image 2 = T2 de Vera aprobado y canonizado (rol: character)

Prompt:
Image 1: the empty stage plate, keep the world of Image 1 untouched. Image 2: character reference of Vera, use only the person from Image 2, ignore its plain background. Place Vera standing at the white gaffer-tape mark front-left of Image 1, bow raised in her right hand, frozen mid-breath a second before playing, body oriented into the open arc. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, the four other stands and the rest of Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched' (R4/R7): ningún miembro ya insertado se vuelve a describir ni se re-genera.
- Salida de la Inserción 5 = **composición canónica del quinteto**, base de las tres anclas siguientes.
```

### Inserción 2 · +Ilan (front-right)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa con Vera ya colocada (rol: location)
- Image 2 = T2 de Ilan aprobado y canonizado (rol: character)

Prompt:
Image 1: the plate with Vera already placed, keep every person already placed in Image 1 untouched. Image 2: character reference of Ilan, use only the person from Image 2, ignore its plain background. Place Ilan standing at the white gaffer-tape mark front-right of Image 1, bow raised in his right hand, frozen mid-breath a second before playing, body oriented into the open arc, facing Vera across the arc. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, the three other stands and the rest of Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched' (R4/R7): ningún miembro ya insertado se vuelve a describir ni se re-genera.
- Salida de la Inserción 5 = **composición canónica del quinteto**, base de las tres anclas siguientes.
```

### Inserción 3 · +Noor (centre-back)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa con Vera e Ilan ya colocados (rol: location)
- Image 2 = T2 de Noor aprobado y canonizado (rol: character)

Prompt:
Image 1: the plate with Vera and Ilan already placed, keep every person already placed in Image 1 untouched. Image 2: character reference of Noor, use only the person from Image 2, ignore its plain background. Place Noor standing at the white gaffer-tape mark centre-back of Image 1, bow raised in her right hand, frozen mid-breath a second before playing, body oriented into the open arc, framed between Vera and Ilan. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, the two other stands and the rest of Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched' (R4/R7): ningún miembro ya insertado se vuelve a describir ni se re-genera.
- Salida de la Inserción 5 = **composición canónica del quinteto**, base de las tres anclas siguientes.
```

### Inserción 4 · +Tomas (back-left)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa con Vera, Ilan y Noor ya colocados (rol: location)
- Image 2 = T2 de Tomas aprobado y canonizado (rol: character)

Prompt:
Image 1: the plate with Vera, Ilan and Noor already placed, keep every person already placed in Image 1 untouched. Image 2: character reference of Tomas, use only the person from Image 2, ignore its plain background. Place Tomas seated at the white gaffer-tape mark back-left of Image 1, left hand gripping the neck of his instrument and bow raised in his right hand, frozen mid-breath a second before playing, body oriented into the open arc. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, the remaining stand and the rest of Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched' (R4/R7): ningún miembro ya insertado se vuelve a describir ni se re-genera.
- Salida de la Inserción 5 = **composición canónica del quinteto**, base de las tres anclas siguientes.
```

### Inserción 5 · +Kai (back-right)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K (esta imagen se reutiliza como Image 1 del siguiente paso)

References:
- Image 1 = la placa con Vera, Ilan, Noor y Tomas ya colocados (rol: location)
- Image 2 = T2 de Kai aprobado y canonizado (rol: character)

Prompt:
Image 1: the plate with Vera, Ilan, Noor and Tomas already placed, keep every person already placed in Image 1 untouched. Image 2: character reference of Kai, use only the person from Image 2, ignore its plain background. Place Kai standing at the white gaffer-tape mark back-right of Image 1, left hand on the neck of his instrument and bow raised in his right hand, frozen mid-breath a second before playing, body oriented into the open arc, closing the quintet. Keep facial features exactly the same as Image 2. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light. Wide shot, eye level, all four other players from Image 1 stay untouched. Format: 16:9.

Notes:
- 'Keep every person already placed in Image 1 untouched' (R4/R7): ningún miembro ya insertado se vuelve a describir ni se re-genera.
- Salida de la Inserción 5 = **composición canónica del quinteto**, base de las tres anclas siguientes.
```

---

## Tres anclas de conjunto (edición sobre la composición canónica, no regeneración)

### Ancla 1 · Apertura (0.0s)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K/4K directo (es una toma final del storyboard, no una variante de exploración)

References:
- Image 1 = composición canónica del quinteto (rol: ff — no se re-describe a nadie ni el vestuario)

Prompt:
Image 1: the canonical quintet composition, use only what Image 1 already shows, do not re-describe the five people, their wardrobe or the instruments. Five bows landing on the strings at once, frozen mid-impact, rosin bursting up from the strings. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation. Wide shot, eye level, static frame centred at the middle of the open arc, white gaffer-tape marks visible at their feet. Format: 16:9.

Notes:
- Por qué esta ancla: el golpe inicial del arranque, corona baja, arco a la vista (ver `03-direccion.md` y `output/shots.json` shot_01/shot_16/shot_27).
- 'dust' se evita como palabra suelta (colisiona con el vocabulario de redundancia del linter, ya cubierto por la referencia); el estado del polvo de resina se describe con 'rosin' + el verbo del beat.
```

### Ancla 2 · Tormenta (52.0s, ángulo bajo)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K/4K directo (es una toma final del storyboard, no una variante de exploración)

References:
- Image 1 = composición canónica del quinteto (rol: ff — no se re-describe a nadie ni el vestuario)

Prompt:
Image 1: the canonical quintet composition, use only what Image 1 already shows, do not re-describe the five people, their wardrobe or the instruments. Change camera to a low angle, looking up at the quintet. Five right arms at the same angle, frozen mid-stroke, five bows coming down together, rosin exploding into the beam so the light reads as a solid body. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation. Wide shot, low angle, static frame, in front of the arc looking up. Format: 16:9.

Notes:
- Por qué esta ancla: segundo plano de conjunto, la tormenta se abre (ver `03-direccion.md` y `output/shots.json` shot_01/shot_16/shot_27).
- 'dust' se evita como palabra suelta (colisiona con el vocabulario de redundancia del linter, ya cubierto por la referencia); el estado del polvo de resina se describe con 'rosin' + el verbo del beat.
```

### Ancla 3 · Acorde final (77.4s)

```
Model: nano-banana-pro
Size / Ratio: 16:9 — 2K/4K directo (es una toma final del storyboard, no una variante de exploración)

References:
- Image 1 = composición canónica del quinteto (rol: ff — no se re-describe a nadie ni el vestuario)

Prompt:
Image 1: the canonical quintet composition, use only what Image 1 already shows, do not re-describe the five people, their wardrobe or the instruments. Five bows stopped in the air at the same height after the last chord, frozen a beat after impact, five chests rising and falling together, all five faces legible. Rosin still falling through the beam. One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight. Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, no HDR look, no added saturation. Wide shot, eye level, static frame from the front, level with the middle of the open arc. Format: 16:9.

Notes:
- Por qué esta ancla: las cinco identidades deben leerse y verificarse contra sus maestros (ver `03-direccion.md` y `output/shots.json` shot_01/shot_16/shot_27).
- 'dust' se evita como palabra suelta (colisiona con el vocabulario de redundancia del linter, ya cubierto por la referencia); el estado del polvo de resina se describe con 'rosin' + el verbo del beat.
```
