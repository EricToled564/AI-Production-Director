# Texto en la imagen con GPT Image 2 — verificación (2026-10-27)

Pregunta: ¿una imagen fotográfica de la prueba puede llevar texto pedido en el prompt (F32 «texto corto», «texto
extenso o pequeño»)? El plan anterior decía que todos los casos llevan F32 «sin texto». Eso fue un error: mezcló dos cosas
distintas que el corpus separa.

Leídos completos en los originales (`apd/originales/AI_Production_Director_v3.4.0_COMPLETE.zip`, idénticos a los skills
instalados: `diff -rq` sin diferencias en `image/`): `image/references/gpt-image.md` (190 l), `text-rendering.md`
(175 l), `vision-decomposer.md` (113 l), `image/SKILL.md` (118 l). Leídos además los 149 textos del universo que tratan
de texto, letrero, tipografía o lettering. Esta verificación es parcial respecto del universo: la relectura completa
(`02_lectura_universo.md`) la confirma o la corrige.

## 1. Texto superpuesto (overlay): nunca en el prompt

Texto en pantalla que se compone después, en post o en video. Fuente de los textos: `text-overlays.json`.

- `flujo-anclas.html:48` (INV-000026) y `flujo-spot.html:634` (INV-000612): «Texto en pantalla: capa separada,
  text-overlays.json».
- forge `SKILL.md:255–257` Rule 1 (INV-011362–011363): el shot con `on_screen_text` no lleva ese texto en el prompt.
- forge `prompt-anatomy.md:56–67` Layer 4 (INV-012400–012406), `failure-modes.md:43–55` (INV-012307–012316),
  `examples/one-shot-all-adapters/README.md:63–65` (INV-012198–012199).

## 2. Texto dentro del mundo de la imagen: GPT Image 2 lo hace y el corpus dice cómo

Letrero, etiqueta, póster, pantalla, todo lo que forma parte de lo fotografiado.

- `gpt-image.md:67–74` «Text in Image» (INV-002366–002370…): texto literal entre comillas o en mayúsculas; fuente,
  tamaño, color y posición explícitos; deletrear palabras difíciles; «no extra words, no duplicate text, no
  watermarks»; texto pequeño o denso → `quality: high`.
- `gpt-image.md:21–27` (INV-002338): el ejemplo mínimo es una fotografía editorial con el letrero «"Florista"
  hand-painted sign» y «no text other than the sign».
- `image/SKILL.md:34` (INV-002010): «EXACT TEXT discipline only on GPT Image»; `:56` (INV-002020) carga
  `text-rendering.md` para texto en imagen.
- `models.md:16` (INV-002427) y `:50` (INV-002455); `golden-rules.md:46–49` (INV-002266–002268) «Quote Text Exactly».
- `flujo-anclas.html:440` (INV-000222): «Etiqueta de producto, UI, texto pequeño legible → GPT Image 2 quality high»;
  `:24` (INV-000014): el keyframe FF «fija identidad, layout y texto en imagen».
- forge `adapters/gpt-image.md:73–82` (INV-011748–011754): «GPT Image handles text-in-image at roughly 95% accuracy…
  Put the exact text in straight double-quotes… Limit to one text element per prompt»; «Default for storyboard work is
  still composited text»: la composición posterior es el default solo para storyboard.

## 3. Lo que sigue prohibido

- Logos y lettering de marca real generados desde texto: solo heredados de asset aprobado o compuestos en post
  (`flujo-anclas.html:50`, INV-000027; `flujo-spot.html:354`, INV-000472; SW30 R10, ADD-0027; forge `SKILL.md:306`,
  INV-011383).

## Conclusión

F32 «texto corto» y «texto extenso o pequeño» son tipos de imagen fotográfica válidos para GPT Image 2 cuando el texto
pertenece al mundo fotografiado y no es una marca real. Entran a la prueba con caso propio. El texto superpuesto no es un
tipo de imagen: se compone aparte y no entra.
