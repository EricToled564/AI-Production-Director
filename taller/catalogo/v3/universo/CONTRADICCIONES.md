# Supuestas contradicciones — lectura exhaustiva y veredicto (2026-10-26)

Regla: `v2/decisiones/DECISIONES_ERIC_20261026.md` §3. Cada caso se leyó completo en los originales de
`apd/originales/`, con su sección y su jerarquía de carga. Regla de autoridad entre skills, escrita en la fuente:
`ai-production-director/SKILL.md:126` (§6.2) «Todo prompt FINAL se escribe en la sintaxis del modelo destino según el
archivo smixs correspondiente. Si el modelo no tiene archivo smixs (p.ej. Flux, Midjourney, Ideogram), la autoridad es el
adaptador de visual-prompt-forge» y `:132` (§6.4) «video/image smixs son dueños del texto final del prompt. El borrador
del forge se reescribe a sintaxis smixs; nunca al revés». GPT Image 2 tiene archivo smixs: `image/references/gpt-image.md`.

## 1. Referencia de estilo en GPT Image — discrepancia real entre skills, resuelta por la jerarquía escrita

- forge `adapters/_capabilities.json:54-69`: GPT Image («1.5/2», verificado 2026-05-08) `"supports_style_ref": false`.
  `capabilities.schema.json:50` solo define el tipo (boolean), no qué significa; ningún archivo de `tools/` lo usa; el
  adaptador `adapters/gpt-image.md` (94 líneas) no trata referencias de imagen.
- image: `golden-rules.md:91-124` (los dos modelos, `:3`) «Стиль как референс: [Attach style reference] Create [NEW
  CONTENT] in this exact visual style»; `gpt-image.md:102-109` referencias con rol, incluida «Image 3: lighting reference
  (apply golden-hour quality from Image 3)»; `gpt-image.md:111-113` Style Transfer: nombrar las propiedades concretas del
  referente; `prompt-framework.md:20` Style Transfer = «Референс + новый контент».
- Veredicto: para el texto final de un prompt de GPT Image 2 manda image (§6.2, §6.4): la referencia de estilo como
  imagen adjunta con rol vale. El dato del forge no se usa para GPT Image 2.

## 2. Números de lente — no es contradicción dentro de image; discrepancia del forge resuelta por la jerarquía

- image, consistente en todos sus textos: Nano Banana ignora los números (`nano-banana.md:24`, `models.md:48`,
  `SKILL.md:41`, `:114`); GPT Image 2 los admite como look, «50mm feel», no como simulación física
  (`prompt-framework.md:42-44`, `models.md:48`, `gpt-image.md:24`, `:36`; plantillas con `{lens_feel}`,
  `prompt-framework.md:166`, `:183`, `:192`). `creative-direction.md:55-56` («Named lens parameters (50mm, f/2.8) are
  less reliable than descriptive terms») dice lo mismo para los dos modelos.
- forge: `references/failure-modes.md:16` «Add specific lens and aperture ("50mm prime, f/2.0")» y el ejemplo de
  `adapters/gpt-image.md:70` «Shot on a 50mm prime lens at f/2.0».
- Veredicto: el borrador del forge se reescribe a la sintaxis de image (§6.4). En el prompt final de GPT Image 2 la lente
  va como look («50mm feel»), no como apertura numérica. Mi nota anterior sobre INV-002125 («regla de Nano Banana») era
  incorrecta: el texto vale para los dos modelos.

## 3. «Solo keywords separadas por comas» — contradicción real dentro de image, sin regla de precedencia explícita

- `vision-decomposer.md:61` (Paso 4 de `SKILL.md`, `:63`): «Write only keywords separated by commas, in English», con la
  fórmula de 6 segmentos (`:66`) y la cabecera Model / Quality / Size al final (`:97`).
- Contra: `gpt-image.md:7` «Пиши лейблами, не сплошным текстом» (5 slots, `:9-15`); `golden-rules.md:25-28` (los dos
  modelos) «❌ Bad: "Cool car, neon, city, night, 8k"»; forge `adapters/gpt-image.md:86` «Don't write Midjourney-style
  comma stacks».
- Lo que sí dice la fuente sobre el orden: `SKILL.md:46` «The model file is non-negotiable»; `SKILL.md:112` «Prefer …
  model-specific syntax (5-slot for GPT Image)»; `SKILL.md:30` «common rules collapse into mush when applied without
  model-specific syntax». Ningún texto dice explícitamente que el archivo de modelo mande sobre vision-decomposer.
- Veredicto: contradicción real. Decisión pendiente de Eric: para GPT Image 2, ¿el resultado de vision-decomposer se
  reescribe a 5 slots (como piden `SKILL.md:46` y `:112`) o se entrega como keywords?

## 4. «Same person» — no es contradicción con multi-panel; sí queda abierta con storyboards

- forge `references/consistency-locks.md:111-118` «What doesn't work: Adding "consistent character" or "same person" to
  the prompt, generators don't read meta-instructions … generators don't have memory across calls», bajo la premisa de
  `:3` «Generators are stateless, every prompt is interpreted fresh»: se refiere a prompts de shots distintos.
- `multi-panel.md:308` «Always include … "same person … across all panels"»: dentro de una sola imagen («these patterns
  produce one image with all panels baked in», `:3`). Alcance distinto: no hay contradicción.
- `storyboards.md:7-15`, `:78-82`, `:93-95` y `characters.md:33-41`: varias imágenes «one at a time» con «Identity must
  stay consistent throughout». Si cada imagen es una llamada sin memoria, choca con `consistency-locks.md:115-116`. El
  corpus no dice si GPT Image 2 conserva contexto entre imágenes de una misma conversación (`adapters/gpt-image.md:94`
  solo dice «Standard images.generate endpoint … ChatGPT Plus and above gives UI access»).
- Veredicto: abierta; el corpus no tiene el dato que la decide.
