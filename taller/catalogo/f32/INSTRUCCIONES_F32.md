# Faceta nueva F32 — Texto en la imagen

Eric aprobó el 2026-10-23 una faceta nueva para el catálogo de textos de imagen y GPT Image 2:

**F32 · Texto en la imagen** — ¿la imagen final lleva texto renderizado y de qué tipo?
- `sin texto`: la imagen no lleva ninguna letra legible renderizada.
- `texto corto`: titular, logotipo con texto, etiqueta, rótulo o frase breve legible.
- `texto extenso o pequeño`: varios bloques, párrafos, listas, cifras, letra pequeña, infografía, menú, slide
  con contenido o UI con texto.

Para cada texto de tu lote decide su valor de F32, igual que las demás facetas del catálogo:
- `"TODOS"` si el texto (la regla, sintaxis, ejemplo o explicación) no depende de que la imagen lleve texto.
- O una lista con los valores en los que aplica. Ejemplos: "si no hay texto, añadir 'no text' en Constraints"
  → ["sin texto"]; "pon el texto literal entre comillas" → ["texto corto", "texto extenso o pequeño"];
  "quality high para letra pequeña" → ["texto extenso o pequeño"]; una plantilla de póster con titular →
  ["texto corto"]; una plantilla de infografía o de slide con contenido → ["texto extenso o pequeño"];
  "evita texto en la imagen" como regla general de una pieza → ["sin texto"] si solo vale cuando no se pide
  texto, o "TODOS" si es una restricción que vale siempre para ese tipo de pieza.
Lee el texto completo y su contexto (encabezado; archivo fuente en
`docs/d4ea0f84-BASE_TEXTOS_ORIGINALES_13005_20261019_055700_1/fuentes_originales/<archivo>` dentro de la carpeta
scratchpad). Los textos pueden estar en inglés, ruso o español. Ningún estado pendiente ni duda: cada texto se
resuelve.

Salida: lista JSON, un objeto por texto del lote, en el mismo orden: `{"id": "...", "F32": "TODOS" | [...],
"razon_f32": "15 palabras o menos; vacío si TODOS"}`. Escríbela con json.dump y verifica tú mismo que tiene
los mismos ids en el mismo orden y solo valores válidos.
