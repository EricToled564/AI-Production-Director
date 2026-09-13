---
name: aurora-prompt-linter
description: "Gate determinista que valida prompts de generación visual AI (imagen/video) antes de entregar. Detecta 3 capas: redundancia con refs por categoría P/O/L/PR/S, secciones requeridas por plataforma+caso (Kling 3.0/Veo 3.1/Sora 2/GPT Image 2/Nano Banana Pro/Midjourney), y estructura (word count, negative prompt, vocab baneado). USA ESTE SKILL antes de entregar cualquier prompt visual al usuario — gate obligatorio del skill prompt-production-protocol Step 5b. Override solo con sintaxis expresa OVERRIDE: término-o-categoría - razón, válido únicamente en turno actual."
---

# Aurora Prompt Linter

Gate determinista entre el drafting del prompt y la entrega al usuario. Mueve la regla "no redescribir lo que está en los refs" de memoria del agente a código ejecutable.

## Por qué existe

El agente olvida la regla v6.0 §5.4 ("menos descripción de lo que HAY, más de cómo EVOLUCIONA") bajo presión de iteración rápida. Documentado empíricamente en sesión 2026-05-27: 4 errores repetidos de over-description en el mismo flujo. La memoria del agente falla, el código no.

## Cuándo usarlo

**Obligatorio** para:
- Casos 3a/3b/3c (I2V con FF/LF refs) — donde la redundancia es la falla más común

**Recomendado** para:
- Caso 1 (Génesis text-to-image)
- Caso 2 (Ancla con refs parciales)
- Caso 4 (Video con diálogo)

**El agente lo invoca automáticamente** al final de Step 4 (drafting) del skill `prompt-production-protocol`, antes de Step 6 (delivery). Si la Regla 28 está activa en el system prompt, es bloqueante.

## Cómo invocarlo

Antes de entregar el prompt al usuario:

1. **Etiquetar los refs por categoría.** Cada ref carga 0 o más de: P (sujeto), O (outfit), L (locación), PR (prop), S (estilo). Mapea a IDs system v6.0 §7. Ejemplo de refs.yaml:
   ```yaml
   - file: "img_ciclista_ff.jpg"
     role: "FF"
     tags: ["P1", "O1", "L1", "PR1"]
   - file: "img_climbing_wall_lf.jpg"
     role: "LF"
     tags: ["L2", "PR1"]
   ```

2. **Escribir el draft del prompt** (incluyendo negative prompt) a un archivo de texto.

3. **Capturar el mensaje del usuario** del turno actual a un archivo de texto (para parsear OVERRIDEs).

4. **Ejecutar el linter:**
   ```bash
   python3 scripts/prompt_linter.py \
     --prompt /tmp/draft.txt \
     --refs /tmp/refs.yaml \
     --case 3b \
     --overrides /tmp/user_msg.txt \
     --sports-broadcast
   ```

5. **Interpretar el resultado:**
   - Exit 0 → STATUS=PASS → entregar al usuario + incluir reporte del linter en el output para trazabilidad.
   - Exit 1 → STATUS=FAIL → NO entregar. Iterar el draft basándose en las violaciones listadas. Repetir hasta PASS.

## Categorías que detecta

| Categoría | Qué cubre | Cuándo se banea en MAIN |
|---|---|---|
| **P** | Sujeto: cara, cuerpo, edad, build, cabello, expresión, identidad | Si ref carga P |
| **O** | Outfit: prendas, colores, accesorios | Si ref carga O |
| **L** | Locación: piso, paredes, ventanas, lighting, ambiente | Si ref carga L |
| **PR** | Prop: balón, objeto interactuado | Si ref carga PR |
| **S** | Estilo: render, paleta, aesthetic | Si ref carga S |
| **BANNED** | Cross-platform: `slow motion`, `cartoon`, `anime`, `3D render`, `perfume ad`, `dreamlike` | SIEMPRE en MAIN (deben ir en NEGATIVE) |
| **STRUCTURE** | Word count, presencia de negative prompt | Siempre |
| **REQUIRED** | `60fps`, `broadcast realism` (con flag --sports-broadcast) | Cuando aplica Regla 26 v6.0 |

## Exenciones automáticas

El linter NO flaggea cuando el término aparece en:

- **Contexto de motion/cámara**: `camera arcs through the studio` — "studio" exento porque sigue a "camera".
- **Anchor direccional**: `away from her face`, `across the climbing wall`, `over his head` — preposiciones direccionales (`away from`, `toward`, `off`, `over`, `behind`, `across`, `past`, `onto`, `into`, `above`, `below`, `beside`) seguidas opcionalmente de `her/his/the` exentan el término que sigue.

Esto distingue descriptor estático ("warm tungsten studio") de uso funcional ("ball passes through the studio").

## Mecanismo de override

Si una violación detectada es legítima en el caso actual, el usuario puede autorizarla **expresamente por escrito en el turno actual**.

Sintaxis válida:
```
OVERRIDE: <término-o-categoría> - <razón>
```

Ejemplos válidos:
- `OVERRIDE: red performance tank - necesito reforzar el color porque seeds previas lo pierden`
- `OVERRIDE: L - autorizo describir locación porque la ref está muy oscura`
- `OVERRIDE: slow motion - explícitamente quiero slow motion en este clip`

Frases que **NO** cuentan como override (genéricas, sin scope específico):
- "hazlo de todas formas"
- "ya sé que está en la ref, déjalo"
- "ready to copy paste"
- "dale"

**Reglas críticas del override:**
- Solo válido en el turno actual del usuario. Autorizaciones de turnos pasados NO persisten.
- Cada prompt nuevo arranca STRICT (sin overrides activos).
- Override de categoría completa (ej. `OVERRIDE: L`) cubre todos los términos de esa categoría.
- Override de término específico (ej. `OVERRIDE: red performance tank`) solo cubre ese término.

## Word count por caso

| Case | Budget | Comportamiento |
|---|---|---|
| 1, 2 | 75-130 palabras | Max es HARD FAIL. Min es WARN no-bloqueante. |
| 3a, 3b, 3c | 50-90 palabras | Max es HARD FAIL (Regla 10 v6.0). Min es WARN — compresión válida si intencional. |
| 4 | 75-130 palabras | Same as 1/2. |

El conteo se hace solo sobre MAIN (no incluye negative prompt block).

## Output esperado

Reporte de texto plano (o JSON con `--json`). Ejemplo de FAIL:

```
============================================================
AURORA PROMPT LINTER REPORT v1.0
============================================================
Case: 3b (I2V FF + LF)
Word count (MAIN): 127 / budget (50, 90)
Negative prompt: present
Categories covered by refs: ['L', 'O', 'P', 'PR']
Sports broadcast mode: on

VIOLATIONS (27):
  FAIL [L] 'studio' - Static descriptor of category L (covered by refs)
  FAIL [L] 'concrete walls' - Static descriptor of category L (covered by refs)
  ...
  FAIL [STRUCTURE] 'word_count=127' - Above HARD MAX 90 (Regla 10 v6.0)

OVERRIDES ACCEPTED (1):
  OK 'red performance tank' - necesito reforzar color por seeds previas

SUGGESTIONS:
  -> Strip from MAIN: [...] (category L already covered by refs)
  -> Move to NEGATIVE block: [...]
  -> Fix structure: ['word_count=127']

STATUS: FAIL
Delivery BLOCKED. Iterate or grant OVERRIDE in current turn.
============================================================
```

Ejemplo de PASS:
```
STATUS: PASS
Delivery PERMITTED.
```

## Limitaciones conocidas v1.0

- **Sinónimos**: "tank top" en ref + "athletic shirt" en prompt no se detecta como redundante. Roadmap v1.1: tabla de sinónimos.
- **Sub-tags por categoría**: O.upper / O.lower / P.face / P.body no soportados — un ref tagueado como O cubre todo outfit. Si el ref solo muestra el torso pero el clip va a mostrar zapatos, hay falso positivo en "white sneakers". Roadmap v1.2.
- **Vision check**: el linter no ve las imágenes, depende de los tags que el agente declara. Si tageo mal, falla en silencio. Mitigación: el agente debe re-verificar tags antes de invocar.
- **Vocabulary base**: las listas en `scripts/vocabularies.yaml` están calibradas para casos típicos de Aurora (cycling, soccer, fitness). Si el proyecto usa otros dominios (cocina, automotriz, etc.) hay que expandir las listas.

## Integración con system prompt v6.1

Si tu system prompt incluye Regla 28 (v6.1+), este linter es bloqueante — el agente NO entrega prompts sin pasar el linter o sin overrides válidos. Si tu system prompt es v6.0, el linter es opcional pero altamente recomendado.

Ver `references/skill_update_step5.md` para la edit al skill prompt-production-protocol.
Ver `references/system_prompt_v6_1_rule28.md` para el bundle de 9 cambios que actualizan v6.0 → v6.1.

## Archivos del paquete

```
aurora-prompt-linter/
├── SKILL.md                       (este archivo)
├── scripts/
│   ├── prompt_linter.py           (CLI ejecutable)
│   └── vocabularies.yaml          (vocabulary lists base)
└── references/
    ├── README.md                  (uso detallado + tests)
    ├── skill_update_step5.md      (edit al skill prompt-production-protocol)
    └── system_prompt_v6_1_rule28.md (9 edits propuestas a system prompt v6.0)
```

## Versión

v1.0 — 2026-05-27
Built by: Final Upgrade AI / Eric Toledano
Origen: Retrospectiva F7 sesión 2026-05-27
