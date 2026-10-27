# Prompts GPT Image 2 — briefs B1–B5 (PILOTO_V5 §5)

## B1 — Pescadora de unos 60 años en un muelle al amanecer, sol bajo lateral, piel curtida, plano medio corto, mirada fuera de cámara

Uso: Portada de reportaje · Formato 4:5

```text
Model: gpt-image-2 (OpenAI API)
Quality: high
Size: 1024x1280

Prompt:
Scene: Create a photograph on a weathered wooden fishing pier at dawn on an open sea coast; the sun sits just above the horizon at camera left and rakes low across wet, salt-bleached planks with nail heads and frayed coiled rope, a stacked blue plastic fish crate behind her; sea and pale sky fall soft and out of focus, with fine sea mist hanging in the low light.
Subject: A fisherwoman of about 60, framed from mid-chest up (medium close-up), body turned three-quarters to camera, looking off-frame to the right toward the water; deep-set eyes, weathered sun-damaged skin with deep expression lines, grey hair tied back with loose strands lifted by the wind, a faded orange oilskin jacket with cracked coating at the seams and dried salt marks.
Important Details: Hard low side light from camera left grazes her face so wrinkles, pores, sunspots and dry lips cast small shadows; the shadow side stays one to two stops darker and unlit. Individual grey hair strands catch the sunlight; the oilskin shows creases at the elbow and a wet sheen with fine spray droplets on the shoulders. Eye-level camera, 85mm feel, shallow depth of field. Natural skin color with redness on the cheeks and nose. Palette of slate blue #4A5A6A, wet brown wood #5B4636 and faded orange #D9822B.
Use Case: editorial photograph for the cover of a print reportage, looks like a real photo
Constraints: Solo portrait of her alone with natural skin texture and no AI rendering artifacts; the frame stays free of text and watermarks, with no glamorization, heavy retouching or studio gloss.
```

Validación: sin fallas · 264 palabras · 21 reglas del piloto seleccionadas

Reglas aplicadas por lectura directa (sin clasificar todavía):

- natural skin texture, no AI rendering artifacts → visual-prompt-forge/adapters/gpt-image.md:57, :90
- microdetalle (texturas, mechones a la luz, sombras de contacto, especulares, partículas, caída de tela) → image/references/prompt-framework.md:208–219
- material nombrado por su textura → image/references/creative-direction.md:78–92
- colores con hex → image/references/golden-rules.md:36; image/SKILL.md:112
- quality high para fotorrealismo → image/references/models.md:65

Inferencias mías, para tu aprobación:

- F04 añade «editorial» a «retrato» (PILOTO §2 fija retrato): portada de reportaje = imagen con lenguaje de revista (definición de F04 editorial, taxonomía L490). Activa la plantilla INV-002400.
- F17 documental, por reportaje y piel curtida.
- Sol a la izquierda de cámara, mirada hacia la derecha, hacia el agua.
- Vestuario: chaqueta impermeable naranja desteñida; pelo gris recogido. El brief no los fija.
- Tamaño 1024x1280: no hay tamaño 4:5 en la fuente; calculado dentro de los límites INV-002355..2358.

## B2 — Ejecutivo de unos 40 años en una oficina con ventanal, luz suave de ventana, plano medio, mirando a cámara

Uso: Página «equipo» de un sitio web corporativo · Formato 3:2

```text
Model: gpt-image-2 (OpenAI API)
Quality: high
Size: 1536x1024

Prompt:
Scene: Create a photograph in a modern office interior in daytime with a floor-to-ceiling window at camera left; city buildings outside fall soft and slightly overexposed; the edge of a light oak desk with visible grain and a potted fiddle-leaf fig sit in the soft background.
Subject: A man of about 40, framed from the waist up (medium shot), standing slightly angled to camera with relaxed shoulders, looking straight into the lens with a calm closed-mouth half smile; short dark hair with grey at the temples, light stubble, a navy unstructured wool blazer with visible weave over a white cotton open-collar shirt.
Important Details: Soft diffused daylight from the large window at camera left with a gentle falloff across the right side of his face and a faint natural bounce from the white walls; low contrast. Natural fabric folds at the blazer elbows and collar, a soft window catchlight in both eyes. Eye-level camera, 50mm feel, moderate depth of field so the office reads but stays soft. Real skin texture with visible pores and slight shadows under the eyes. Palette of off-white #F2F0EB, light oak #C8A97E, navy #1F2A44 and glass grey #A9B4BC.
Use Case: team page portrait for a corporate website, looks like a real photo taken on location
Constraints: Solo portrait of him alone in a real office with natural skin texture and no AI rendering artifacts; the frame stays free of text, logos and watermarks, without heavy retouching or a studio backdrop.
```

Validación: sin fallas · 244 palabras · 21 reglas del piloto seleccionadas

Reglas aplicadas por lectura directa (sin clasificar todavía):

- natural skin texture, no AI rendering artifacts → visual-prompt-forge/adapters/gpt-image.md:57, :90
- microdetalle (texturas, mechones a la luz, sombras de contacto, especulares, partículas, caída de tela) → image/references/prompt-framework.md:208–219
- material nombrado por su textura → image/references/creative-direction.md:78–92
- colores con hex → image/references/golden-rules.md:36; image/SKILL.md:112
- quality high para fotorrealismo → image/references/models.md:65

Inferencias mías, para tu aprobación:

- F17 comercial pulido, por uso corporativo y luz suave.
- Ventanal a la izquierda de cámara; ciudad desenfocada afuera.
- Vestuario: blazer azul marino sin estructura y camisa blanca abierta; pelo oscuro con canas en las sienes, barba de un día. El brief no los fija.
- Expresión: media sonrisa con la boca cerrada.

## B3 — Atleta de unos 25 años justo después de entrenar en un gimnasio, sudor visible, luz dura cenital del gimnasio, primer plano

Uso: Campaña de un club deportivo · Formato 4:5

```text
Model: gpt-image-2 (OpenAI API)
Quality: high
Size: 1024x1280

Prompt:
Scene: Create a photograph in a training gym right after a session; worn black rubber flooring with chalk dust and steel weight racks blur behind her; a single row of industrial lights hangs directly overhead.
Subject: A female athlete of about 25, close-up from the collarbones up, head slightly lowered with her eyes raised to the lens, breathing through parted lips; hair pulled back with damp strands stuck to the temples, a grey sleeveless cotton-blend training top darkened with sweat at the neckline.
Important Details: Hard top light straight from above puts bright highlights on the forehead, cheekbones and shoulders and deep shadows under the brows, nose and chin. Individual sweat beads with small specular highlights on the forehead and upper lip, a wet sheen along the neck and collarbones, flushed skin with visible pores and fine veins at the temples, damp hair strands catching the overhead light. Eye-level camera, 85mm feel, shallow depth of field. Palette of charcoal #2B2B2B, steel grey #7A7F85 and warm skin tones.
Use Case: campaign image for a sports club, looks like a real photo taken right after training
Constraints: Solo portrait of her alone with natural skin texture and no AI rendering artifacts; the frame stays free of text, logos and watermarks, and her skin stays wet and textured, with no glamorization, heavy retouching or airbrushing.
```

Validación: sin fallas · 222 palabras · 20 reglas del piloto seleccionadas

Reglas aplicadas por lectura directa (sin clasificar todavía):

- natural skin texture, no AI rendering artifacts → visual-prompt-forge/adapters/gpt-image.md:57, :90
- microdetalle (texturas, mechones a la luz, sombras de contacto, especulares, partículas, caída de tela) → image/references/prompt-framework.md:208–219
- material nombrado por su textura → image/references/creative-direction.md:78–92
- colores con hex → image/references/golden-rules.md:36; image/SKILL.md:112
- quality high para fotorrealismo → image/references/models.md:65

Inferencias mías, para tu aprobación:

- Mujer: «atleta» no fija género; si prefieres hombre, cambia solo el sujeto.
- F17 documental, por sudor visible y luz dura, aunque el uso es campaña.
- Vestuario: top deportivo gris sin mangas oscurecido por el sudor; pelo recogido con mechones húmedos.
- Cabeza ligeramente baja y ojos a cámara, respirando por la boca entreabierta.
- Tamaño 1024x1280, calculado como en B1.

## B4 — Mujer de unos 30 años en una cocina doméstica de noche, una lámpara cálida como única fuente, sostiene una taza con ambas manos visibles, plano medio

Uso: Ilustración de artículo de estilo de vida · Formato 3:2

```text
Model: gpt-image-2 (OpenAI API)
Quality: high
Size: 1536x1024

Prompt:
Scene: Create a photograph in a small home kitchen at night; behind her a window shows only black glass with a faint reflection of the lamp; a worn wooden counter and a single warm pendant lamp hanging over the counter as the only light in the room.
Subject: A woman of about 30, framed from the waist up (medium shot), leaning back against the counter and holding a matte glazed ceramic mug of tea at chest height with both hands fully visible and wrapped around it, looking down at the rising steam; shoulder-length brown hair, an oversized grey chunky-knit sweater.
Important Details: One warm tungsten-colored pool of light from the pendant above and slightly in front of her; the rest of the kitchen falls into deep unlit shadow. Warm highlights on her cheek, knuckles and the rim of the mug, thin steam wisps catching the lamp light, a soft contact shadow where her fingers wrap the mug, loose fibers at the sweater cuffs. Eye-level camera, 35mm feel, the counter edge leading into the frame. Real skin texture with visible pores. Palette of amber #E0A04A, dark wood brown #4A3426 and charcoal shadow #1E1E1E.
Use Case: editorial photograph illustrating a lifestyle article, looks like a real photo
Constraints: Solo portrait of her alone with exactly two hands, lit only by the pendant lamp, with natural skin texture and no AI rendering artifacts; the frame stays free of text and watermarks, with no glamorization, heavy retouching or studio gloss.
```

Validación: sin fallas · 246 palabras · 22 reglas del piloto seleccionadas

Reglas aplicadas por lectura directa (sin clasificar todavía):

- natural skin texture, no AI rendering artifacts → visual-prompt-forge/adapters/gpt-image.md:57, :90
- microdetalle (texturas, mechones a la luz, sombras de contacto, especulares, partículas, caída de tela) → image/references/prompt-framework.md:208–219
- material nombrado por su textura → image/references/creative-direction.md:78–92
- colores con hex → image/references/golden-rules.md:36; image/SKILL.md:112
- quality high para fotorrealismo → image/references/models.md:65

Inferencias mías, para tu aprobación:

- F04 añade «editorial»: imagen para artículo de revista de estilo de vida. Activa INV-002400.
- F17 narrativo cinematográfico: una fuente domina y el resto en sombra (definición de F17).
- Lámpara colgante sobre la encimera, ligeramente delante de ella.
- Vestuario: suéter gris de punto holgado; pelo castaño a los hombros; té con vapor visible.
- Mirada baja hacia el vapor.

## B5 — Músico de unos 70 años de perfil, contraluz de escenario, ángulo bajo, fondo oscuro

Uso: Póster de concierto (sin texto en la imagen) · Formato 2:3

```text
Model: gpt-image-2 (OpenAI API)
Quality: high
Size: 1024x1536

Prompt:
Scene: Create a photograph on a concert stage at night; a black background with faint haze and suspended dust; one strong stage light hidden behind the back of his head spills a glow into the haze around his silhouette.
Subject: A musician of about 70 in strict profile facing the left edge of the frame, head and shoulders to mid-chest, gazing ahead; short white hair, a short white beard, a deeply lined neck, a dark cotton collarless shirt.
Important Details: Hard backlight from behind and above draws a bright rim along his forehead, nose, lips, individual beard hairs and shoulders while the side of his face toward camera stays mostly in shadow; the haze and dust glow around the rim. Low camera angle looking slightly up at him, 85mm feel. Deep black background fills the upper half of the frame above his head. Palette of black #0A0A0A, warm white rim #F5E6C8 and faint amber haze #B87333.
Use Case: concert poster image with empty dark space above the head for type added later, looks like a real live photo
Constraints: Solo portrait of him alone against plain darkness with natural skin texture and no AI rendering artifacts; the frame stays free of text, letters, logos, watermarks and stage equipment.
```

Validación: sin fallas · 208 palabras · 21 reglas del piloto seleccionadas

Reglas aplicadas por lectura directa (sin clasificar todavía):

- natural skin texture, no AI rendering artifacts → visual-prompt-forge/adapters/gpt-image.md:57, :90
- microdetalle (texturas, mechones a la luz, sombras de contacto, especulares, partículas, caída de tela) → image/references/prompt-framework.md:208–219
- material nombrado por su textura → image/references/creative-direction.md:78–92
- colores con hex → image/references/golden-rules.md:36; image/SKILL.md:112
- quality high para fotorrealismo → image/references/models.md:65

Inferencias mías, para tu aprobación:

- Hombre: «músico» en masculino en el brief.
- Perfil mirando a la izquierda del cuadro; pelo blanco corto y barba corta; sin instrumento, porque el brief no lo nombra.
- Espacio oscuro libre sobre la cabeza para el texto del póster, que se compone después (sin texto en la imagen).
- Bruma leve de escenario para que el contraluz se lea.
- F04 no añade «póster o key art»: sin texto en la imagen, las plantillas de póster del piloto (INV-002406) exigen F32 texto corto y no aplican.

## B6-T1 — Hombre mediterráneo bien parecido de 25 años, pelo castaño oscuro y barba salt and pepper, lentes de armazón negro, camisa blanca italiana, zapatos Armani negros, pantalón de vestir gris claro, cinturón negro; retrato de cuerpo entero sobre fondo gris claro, iluminación cálida a 45 grados

Uso: Maestro de rostro para el retrato de cuerpo entero B6-T2 (uso final no indicado) · Formato 4:5

```text
Model: gpt-image-2 (OpenAI API)
Quality: high
Size: 1024x1280

Prompt:
Scene: Create a photograph in a studio against a seamless light grey backdrop #C9C9C7.
Subject: A Mediterranean man of 25, head and shoulders (close-up), body turned slightly toward camera, looking into the lens with a relaxed closed-mouth expression; olive skin, dark brown eyes, a strong jaw, dark brown hair with premature salt-and-pepper grey combed back, a matching short salt-and-pepper beard, black acetate rectangular glasses, the spread collar of a white Italian cotton dress shirt.
Important Details: One warm key light at 45 degrees from camera left and slightly above models the face, with soft falloff into gentle shadow on his right cheek and a faint low fill. Small catchlights in both eyes behind the lenses, individual beard hairs and grey strands visible, visible cotton weave on the collar. Eye-level camera, 85mm feel, shallow depth of field. Real skin texture with visible pores. Palette of light grey #C9C9C7, white #F7F7F5 and black #111111.
Use Case: face master for a menswear lookbook, in a studio, looks like a real photo
Constraints: Solo portrait of him alone, with natural skin texture and no AI rendering artifacts; the frame stays free of text, logos and brand marks.
```

Validación: sin fallas · 193 palabras · 20 reglas del piloto seleccionadas

Reglas aplicadas por lectura directa (sin clasificar todavía):

- «Armani» → hechos visuales del zapato, sin marca → image/references/gpt-image.md:38
- «bien parecido» → rasgos concretos, sin elogio vago → image/references/gpt-image.md:32, :36
- luz clave única con dirección declarada → image/references/creative-direction.md:7, :11
- natural skin texture, no AI rendering artifacts → visual-prompt-forge/adapters/gpt-image.md:57, :90
- microdetalle de tela, especulares y caída → image/references/prompt-framework.md:212–216
- encuadre positivo («solo portrait») → image/references/golden-rules.md:16
- fondo con hex → image/references/golden-rules.md:36

Inferencias mías, para tu aprobación:

- Luz cálida a 45° desde la izquierda de cámara y un poco arriba; el brief no dice el lado.
- «Salt and pepper» a los 25 años = canas prematuras; lo declaro así para que el modelo no lo envejezca.
- Zapatos: oxford de piel negra pulida, sin marca visible (sustituye «Armani»).
- Uso: lookbook de moda masculina; el brief no lo dice. Cámbialo si es otro.
- Rasgos: piel oliva, ojos castaño oscuro, mandíbula marcada (traducción de «bien parecido»).
- F20 «todas»: su rostro debe reconocerse. La taxonomía separa reconocimiento de cantidad (L1210) y define «todas» como cada persona del cuadro con rostro reconocible, sin figuras anónimas (TRM-0175, L1220).
- Sin F34: GPT Image 2 usa tamaño en píxeles, no resolución nominal (T-BRIEF-IMG L40–42; CONTRATOS_OPERACION_MODELO.json:750–752).
- Dos pasos por TRM-0130 (flujos/flujo-spot.html:358, INV-000474): «primero el retrato de rostro T1 sin referencia, se canoniza con hash; después el cuerpo entero T2 con el rostro adjunto como Image 1 […]. Nunca cuerpo entero de un solo tiro»; DECISIONES.md:20. Textos tomados de produccion/template-retrato-gpt2/b6-corregido/PROMPTS.txt.
- Formato 4:5 (1024x1280) para el maestro de rostro, igual que b6-corregido; F24 «CU close-up» por «head and shoulders (close-up)»; F22 «≥20%».

## B6-T2 — Hombre mediterráneo bien parecido de 25 años, pelo castaño oscuro y barba salt and pepper, lentes de armazón negro, camisa blanca italiana, zapatos Armani negros, pantalón de vestir gris claro, cinturón negro; retrato de cuerpo entero sobre fondo gris claro, iluminación cálida a 45 grados — paso 2: cuerpo entero con el maestro B6-T1 adjunto como Image 1

Uso: Retrato de cuerpo entero (uso final no indicado) · Formato 2:3

```text
Model: gpt-image-2 (OpenAI API)
Quality: high
Size: 1440x2160

Prompt:
Image 1: face reference; use only his face, hair, beard and glasses, keep them exactly the same, and ignore its framing and background.
Scene: Create a photograph as a full-length studio portrait against a seamless light grey backdrop #C9C9C7 that curves smoothly into the floor; his soft shadow falls on the floor behind him to the right.
Subject: The man from Image 1, standing full body from head to shoes in the center of the frame, weight on his left leg, body turned slightly toward camera, looking into the lens with a relaxed closed-mouth expression. He wears a white Italian cotton dress shirt with a spread collar tucked into light grey tailored wool dress trousers with a sharp crease, a black leather belt with a plain silver buckle, and polished black leather oxford shoes.
Important Details: One warm key light at 45 degrees from camera left and slightly above his head models the face and the shirt folds, with soft falloff into gentle shadow on his right side and a faint low fill. His face keeps the detail of Image 1: clear eyes behind the lenses, individual beard hairs. Natural fabric folds at the elbows and waist, visible cotton weave, fine wool texture on the trousers, small specular highlights on the shoe toes. Camera at waist height, 85mm feel, the whole body sharp from hair to shoes. Real skin texture with visible pores. Palette of light grey #C9C9C7, white #F7F7F5 and black #111111.
Use Case: full-length portrait for a menswear lookbook, in a studio, looks like a real photo
Constraints: Solo portrait of him alone, with the full body from head to shoes inside the frame, with natural skin texture and no AI rendering artifacts; the frame stays free of text, logos and brand marks.
```

Validación: sin fallas · 295 palabras · 23 reglas del piloto seleccionadas

Reglas aplicadas por lectura directa (sin clasificar todavía):

- «Armani» → hechos visuales del zapato, sin marca → image/references/gpt-image.md:38
- «bien parecido» → rasgos concretos, sin elogio vago → image/references/gpt-image.md:32, :36
- luz clave única con dirección declarada → image/references/creative-direction.md:7, :11
- natural skin texture, no AI rendering artifacts → visual-prompt-forge/adapters/gpt-image.md:57, :90
- microdetalle de tela, especulares y caída → image/references/prompt-framework.md:212–216
- encuadre positivo («solo portrait») → image/references/golden-rules.md:16
- fondo con hex → image/references/golden-rules.md:36

Inferencias mías, para tu aprobación:

- Formato 2:3 vertical (1024x1536), porque es cuerpo entero; el brief no fija formato.
- Luz cálida a 45° desde la izquierda de cámara y un poco arriba; el brief no dice el lado.
- «Salt and pepper» a los 25 años = canas prematuras; lo declaro así para que el modelo no lo envejezca.
- Zapatos: oxford de piel negra pulida, sin marca visible (sustituye «Armani»).
- Uso: lookbook de moda masculina; el brief no lo dice. Cámbialo si es otro.
- Rasgos: piel oliva, ojos castaño oscuro, mandíbula marcada (traducción de «bien parecido»).
- F20 «todas»: su rostro debe reconocerse. La taxonomía separa reconocimiento de cantidad (L1210) y define «todas» como cada persona del cuadro con rostro reconocible, sin figuras anónimas (TRM-0175, L1220).
- Sin F34: GPT Image 2 usa tamaño en píxeles, no resolución nominal (T-BRIEF-IMG L40–42; CONTRATOS_OPERACION_MODELO.json:750–752).
- Dos pasos por TRM-0130 (flujos/flujo-spot.html:358, INV-000474): «primero el retrato de rostro T1 sin referencia, se canoniza con hash; después el cuerpo entero T2 con el rostro adjunto como Image 1 […]. Nunca cuerpo entero de un solo tiro»; DECISIONES.md:20. Textos tomados de produccion/template-retrato-gpt2/b6-corregido/PROMPTS.txt.
- F23 «persona»: el maestro de rostro B6-T1 aprobado entra como Image 1.
