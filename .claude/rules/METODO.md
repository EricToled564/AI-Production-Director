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

**Decisión 9 del 2026-09-25: NotebookLM queda fuera del flujo por completo.** El criterio
no vuelve al agente: se reparte entre dos capas deterministas y la auditoría de Eric.

1. **Capa determinista.** Tablas de patrón de ruta y expresiones regulares dentro de
   `.claude/hooks/rules_v3.py` (`ARCHIVO_CASO`, `ARCHIVO_TAREA`, `ARCHIVO_FACETA`,
   `REGEX_FACETA`), más el frontmatter de cada archivo de `regimenes/`, con la misma
   disciplina que `scope.yaml`: cada entrada dice qué toca, qué valor asigna y por qué, y
   gana la primera que hace match. La ejecuta `derive`. Se discute línea por línea, en Python,
   por PR.
2. **Capa vectorial.** El subcomando `classify`. Para lo que la capa 1 no decide, la
   similitud del embedding de la regla (`intfloat/multilingual-e5-large`, tabla `embeddings`)
   contra el prototipo de cada valor de faceta o caso (tabla `prototipos`, un centroide por
   descripción, construido por `embed`) asigna el valor con `origen='vector'` si supera
   `--umbral` (0.80 por defecto), y guarda la confianza. Es una sugerencia con número, nunca
   una decisión editorial; las facetas D1-D9 solo se auditan en reglas de imagen o video.
3. **Auditoría.** `audit-export` vuelca a una hoja xlsx, una pestaña por dimensión y otra
   para `caso`, todo lo que sigue sin valor tras las capas 1 y 2, con la mejor sugerencia y su
   confianza aunque no llegara al umbral. Eric llena `valor_corregido` y `razon`; `audit-import`
   relee esa hoja y aplica cada corrección con `origen='auditoria'`, que manda sobre las otras
   dos capas sin importar la confianza que tuvieran, y queda registrada en `auditorias` con
   fecha. Así el sistema aprende de su detector más confiable.

```bash
python3 .claude/hooks/rules_v3.py --db rules.sqlite build
python3 .claude/hooks/rules_v3.py --db rules.sqlite derive
python3 .claude/hooks/rules_v3.py --db rules.sqlite embed         # requiere fastembed + numpy
python3 .claude/hooks/rules_v3.py --db rules.sqlite classify
python3 .claude/hooks/rules_v3.py --db rules.sqlite audit-export --xlsx auditoria.xlsx
# Eric revisa auditoria.xlsx, llena valor_corregido y razon donde corresponde
python3 .claude/hooks/rules_v3.py --db rules.sqlite audit-import --xlsx auditoria.xlsx
python3 .claude/hooks/rules_v3.py --db rules.sqlite check         # exit 1 si algo quedó sin caso ni tarea
```

`scope.yaml` sigue siendo válido como capa determinista para los casos `imagen` y `video`
fuera de la base v3. Para extraer las reglas que aplican a un brief concreto una vez
poblada `rules.sqlite`, el código de selección es `rule_query.py` (brief → facetas
detectadas por regex y por similitud → filtro SQL duro → ranking híbrido BM25+coseno):

```bash
python3 .claude/hooks/rule_query.py --db rules.sqlite --brief "maestro de rostro T1 para Nano Banana Pro, documental"
```

## Paso 3 — Medir que la selección fue exhaustiva

```bash
python3 .claude/hooks/rule_answer_check.py \
  --registry reg_image.json --respuesta respuesta.txt --faltantes faltan.txt
```

No juzga si la selección fue acertada — eso es criterio, y el criterio es de las capas
deterministas y de la auditoría, no del agente. Mide cobertura y detecta tres cosas:

- **SIN MENCIONAR** — reglas del registro que la respuesta no clasificó.
- **Ids inexistentes** — ids citados que no están en el registro.
- **Contradictorias** — la misma regla clasificada `APLICA` y `NO APLICA`.

Sale con código 1 si aparece cualquiera de las tres. Con `0 sin mencionar`, la
exhaustividad queda **demostrada** en vez de supuesta, y ya nadie tiene que
creerle a nadie.

## Por qué el paso 3 existe

Sin él, "fue exhaustivo" es una
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

## Paso 0 — Las reglas que los skills no tienen

Medido el 2026-09-25: los skills instalados no cubren instante pico, fenómenos de luz y clima,
multitudes anónimas ni grupos con identidades. Esas reglas se escriben en el repo, en
`.claude/rules/regimenes/`, como nueve familias por régimen físico con el mismo esqueleto
que `race-and-speed.md`. Cada línea normativa lleva etiqueta de origen: `[FUENTE: …]` si está
en un skill, `[A PRUEBA]` si es inferencia. Una inferencia nunca bloquea un gate. Pasa a
`[CAMPO: url]` cuando la investigación en foros y tutoriales la confirma, y a `[CANONICA fecha]`
cuando un ejercicio real la valida. `rule_registry.py` lee esa carpeta igual que los skills, así
que el Paso 1 las incluye sin que nadie tenga que recordarlas. Las ocho decisiones que gobiernan
esto están en `DECISIONES.md`.
