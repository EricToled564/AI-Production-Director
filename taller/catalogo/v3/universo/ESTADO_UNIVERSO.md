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

## 3. Decisión por texto (`decidir_textos.py`)

Leídos uno por uno 1,914 textos. Cada decisión y su motivo están en `decision_textos.json`, y el texto completo en
`lectura_textos_con_modelo.txt`.

| Grupo leído | Textos | Entran | Salen |
|---|---:|---:|---:|
| Secciones «dentro» que nombran un modelo, sección 1344 (gpt-image-1.5) e INV-002054 | 222 | 157 | 65 |
| Secciones «dentro» de los 13 documentos que no declaran su modelo | 910 | 903 | 7 |
| Secciones mixtas (54) | 782 | 444 | 338 |

- Los 7 de los 910 son seed (`consistency-locks.md` Lock 4 y sus menciones en `failure-modes.md`). El adaptador GPT
  Image no tiene seed (`adapters/gpt-image.md:24-28`, `_capabilities.json`), y `consistency-locks.md:37` lo limita a
  Flux, Seedream, Ideogram y Stable Diffusion.
- 22 textos entran con una nota para la clasificación. Dos son de lente (INV-002125 e INV-012287): «50mm, f/2.8» es
  regla de Nano Banana, mientras que GPT Image 2 admite «50mm feel» como look (`prompt-framework.md:42`). Otra es
  INV-003433: «solo keywords separadas por comas» choca con el adaptador GPT Image (`adapters/gpt-image.md:86`).

## 4. Universo de la prueba

**2,722 textos** = 2,350 de secciones «dentro» − 72 que salen + 444 de secciones mixtas que entran.
La lista de ids está en `universo_prueba.json`.

| Origen | Textos |
|---|---:|
| skills/image | 1,314 |
| flujos (anclas y spot) | 485 |
| skills/visual-prompt-forge | 414 |
| skills/video (imagen fija clave, vocabulario de cámara y luz, velocidad en un cuadro) | 233 |
| skills/visual-asset-critic | 202 |
| skills/storyboard-architect (gramática de plano) | 51 |
| skills/visual-media (fotografía) | 13 |
| skills/ai-production-director (Etapa 5 y reglas de conflicto) | 10 |

## 5. Lo que no se leyó texto por texto

- **Secciones «otro_modelo» (85, 408 textos)** y **«fuera» (927, 9,465 textos)**: se decidieron por sección, leyendo el
  documento y el encabezado (`decidir_secciones.py`), no texto por texto.
- **Documentos que declaran su modelo**: golden-rules, prompt-framework, text-rendering, editing, image/SKILL y models
  (los dos modelos); gpt-image.md y los 7 patterns (GPT Image 2); el adaptador forge (GPT Image 1.5/2). En ellos solo
  se leyeron los textos que nombran un modelo, porque el resto queda cubierto por la declaración del documento.
