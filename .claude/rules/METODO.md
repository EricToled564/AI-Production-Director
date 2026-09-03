# El método: seleccionar todas, después aplicar las que corresponden

El problema nunca fue no tener las reglas. Fue que la **selección** de qué reglas
aplican salía de la memoria del agente, y ahí siempre faltaban las mismas.

Son dos pasos y no se pueden fusionar.

## Paso 1 — Tenerlas TODAS

```bash
python3 .claude/hooks/rule_registry.py --skill image --out reg_image.json --stats
```

Extracción mecánica de cada enunciado normativo de los archivos del skill. Nadie
elige: una línea entra porque lleva un marcador deóntico (`never`, `must`,
`always`, `❌`, `✅`, regla numerada…), no porque alguien la recordara. Cada regla
recibe un id estable `sha1(ruta + texto)`, que sobrevive a que se muevan líneas y
cambia cuando cambia la redacción.

Estado medido hoy: **1,210 enunciados** en el pipeline visual completo.

| skill | reglas | | skill | reglas |
|---|---:|---|---|---:|
| `video` | 348 | | `brand-lock-extractor` | 89 |
| `visual-prompt-forge` | 180 | | `visual-asset-critic` | 63 |
| `storyboard-architect` | 177 | | `screenwriter` | 57 |
| `image` | 167 | | `produccion-visual-sw30` | 45 |
| `ai-video-storyboard` | 35 | | `ai-production-director` | 25 |
| `storyboard-html-preview` | 24 | | `visual-media` | 0 |

Reproducible: `for s in ...; do rule_registry.py --skill $s --stats; done`.

## Paso 2 — Decidir cuáles aplican a ESTE caso

**Lo hace NotebookLM, no el agente.** Decisión de dirección, y el razonamiento es
correcto: hay evidencia directa de que la selección del agente falla — en la sesión
donde se construyó esto se saltó dos veces un skill que estaba instalado desde el
primer minuto — y evidencia directa de que NotebookLM funciona.

```bash
python3 .claude/hooks/rule_export.py \
  --registry reg_image.json --out fuente.md --pregunta pregunta.txt \
  --caso "maestro de rostro T1, Nano Banana Pro"
```

Produce el documento a subir al notebook (todas las reglas, una por línea, con su
id) y la pregunta canónica: clasificar **cada** id como `APLICA` o `NO APLICA` con
razón. El servidor MCP está declarado en `.mcp.json`; requiere Chrome y una
autenticación inicial con pantalla.

`.claude/rules/scope.yaml` queda como respaldo determinista para cuando NotebookLM
no esté disponible. **No es la autoridad** — es el plan B, y su criterio es del
agente, por eso está escrito para poder discutirse línea por línea.

## Paso 3 — Medir que la selección fue exhaustiva

```bash
python3 .claude/hooks/rule_answer_check.py \
  --registry reg_image.json --respuesta respuesta.txt --faltantes faltan.txt
```

No juzga si la selección fue acertada — eso es criterio, y el criterio ya no es del
agente. Mide cobertura y detecta tres cosas:

- **SIN MENCIONAR** — reglas del registro que la respuesta no clasificó.
- **Ids inexistentes** — ids citados que no están en el registro.
- **Contradictorias** — la misma regla clasificada `APLICA` y `NO APLICA`.

Sale con código 1 si aparece cualquiera de las tres. Con `0 sin mencionar`, la
exhaustividad queda **demostrada** en vez de supuesta, y ya nadie tiene que
creerle a nadie.

## Por qué el paso 3 existe

No es desconfianza hacia NotebookLM. Es que sin él, "fue exhaustivo" es una
opinión, y este repo existe justamente porque las opiniones sobre cumplimiento no
resultaron confiables. El paso 3 cuesta un comando y convierte la afirmación en un
número. Si el número sale 100%, la objeción se muere con datos.

## Un caso real de por qué el paso 1 no lo puede hacer el agente

Durante esta sesión el agente afirmó que el skill `image` **no tenía lista de
vocabulario prohibido propia**. Sí la tiene:
`image/references/gpt-image.md:36` — *stunning, incredible, epic, gorgeous,
masterpiece*. Y `models.md:49` añade que en GPT Image 2 esas palabras **empeoran**
el resultado, mientras que Nano Banana simplemente las ignora.

La afirmación falsa salió de buscar encabezados con grep en vez de leer los
archivos. Es exactamente lo que el propio `image/SKILL.md:18` advierte:

> *"The body of this SKILL.md is intentionally thin so you cannot fake a result by
> reading it alone. The actual rules live only in the reference files."*

El paso 1 existe para que ese error sea imposible: la extracción no busca, lee todo.
