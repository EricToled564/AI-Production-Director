# Universo de la prueba — estado al 2026-10-26

Regla (Eric, 2026-10-24, `v2/decisiones/DECISIONES_ERIC_20261024.md` §1): entra todo texto relevante para crear
imágenes con cualquier modelo; sale solo el que es relevante únicamente para modelos que no son GPT Image 2.

## 1. Documento, líneas y encabezado de los 13,005 textos, contra los originales

`verificar_origen.py` localiza cada archivo del corpus en `apd/originales/` por su sha256 (no por el nombre) y
comprueba cada texto. Resultado en `verificacion_origen.json`:

| Prueba | Pasan | De |
|---|---:|---:|
| A. el archivo original existe con el sha256 de la base | 13,005 | 13,005 |
| B. el texto está literal en el original, en sus líneas (HTML: en el texto visible; filas de tabla, celda por celda) | 13,005 | 13,005 |
| C. el sha256 del texto coincide | 13,005 | 13,005 |
| D. el encabezado guardado es la ruta de títulos del original (.md y .md.tpl) | 6,890 | 6,952 |
| E. en los 6 HTML, el orden de los textos es el del documento (de ahí sale su sección) | 6 | 6 |

Los 62 fallos de D son un error de la base: en `skills/image/SKILL.md` (30) y `skills/video/SKILL.md` (32), los
títulos «### Step 2…» a «### Step 6…» quedaron anidados bajo «### Step 1…», que en el original es su hermano (mismo
nivel `###`, image/SKILL.md líneas 32, 38, 48, 52, 74, 78). `secciones.py` usa el encabezado reconstruido para esos 62.
La corrección es 1 a 1 y no choca con ningún otro encabezado: las 1,408 secciones y sus textos son los mismos; cambia el
nombre de 9 secciones (200–204 y 796–799).

## 2. Decisión por sección (`decidir_secciones.py`, sin cambios de criterio)

| Estado | Secciones | Textos |
|---|---:|---:|
| dentro | 342 | 2,350 |
| mixta | 54 | 782 |
| otro_modelo | 85 | 408 |
| fuera | 927 | 9,465 |

## 3. Decisión por texto dentro de «dentro» (`decidir_textos.py`)

Leídos uno por uno: los 217 textos de secciones «dentro» que nombran un modelo, los 4 de la sección 1344 (el documento
declara gpt-image-1.5) e INV-002054. Total: 222. Cada decisión y su motivo están en `decision_textos.json`, y el texto
completo en `lectura_textos_con_modelo.txt`.

| | Textos |
|---|---:|
| Salen (solo otro modelo o video) | 65 |
| Entran | 157 |
| …de ellos con nota para la clasificación | 18 |

Las secciones «dentro» quedan en **2,285** textos (2,350 − 65), pendientes de lo que dé el punto 4.

## 4. Lo que falta para cerrar la cifra

1. **Los textos «dentro» de documentos que no declaran su modelo y no lo nombran: 910.** INV-002054 («Up to 14
   reference images (6 high-fidelity)», `characters.md:3`) no nombra ningún modelo y su cifra es de Nano Banana
   (`nano-banana.md:64`). Por eso no basta con leer los que nombran un modelo. Los 910 se reparten así: characters 30,
   creative-direction 83, dimensional 27, multi-panel 114, slides 137, storyboards 30, structural 39,
   vision-decomposer 67, visual-asset-critic/SKILL 124, critique-rubric 75, consistency-locks 51, failure-modes 81 y
   prompt-anatomy 52.
2. **Los 782 textos de las 54 secciones mixtas**, uno por uno.

Universo = 2,285 − lo que salga del punto 4.1 + lo que entre del punto 4.2.
