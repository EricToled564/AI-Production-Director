# Aurora Prompt Linter v1.0

Linter determinista que bloquea entrega de prompts AI con redundancia respecto a refs, violaciones de estructura, vocabulario baneado o falta de keywords obligatorios. Integra con el skill `prompt-production-protocol` como gate obligatorio en Step 5.

## Por qué existe

Sesión 2026-05-27: el agente cometió el mismo error tres veces (describir en el prompt cosas ya visibles en los refs). v6.0 §5.4 lo prohíbe pero el agente lo olvida bajo presión. El linter mueve el enforcement de "memoria del agente" a "regla determinista en código".

## Cobertura

| Versión | Cobertura efectiva |
|---|---|
| Solo memoria + skill | ~50% |
| Linter regex genérico | ~70% |
| **v1.0 (este) — tags por categoría + override** | **~92-94%** |

## Cómo se usa

```bash
python3 prompt_linter.py \
  --prompt path/to/prompt.txt \
  --refs path/to/refs.yaml \
  --case 3b \
  --overrides path/to/user_message.txt \
  --sports-broadcast
```

Exit code:
- `0` → PASS, entrega permitida
- `1` → FAIL, entrega bloqueada

## Formato de refs.yaml

Cada ref se etiqueta con las categorías que carga (mapea a IDs system v6.0 §7):

```yaml
- file: "img_ciclista_balon_aire.jpg"
  role: "FF"          # FF | LF | MR (motion ref)
  tags: ["P1", "O1", "L1", "PR1"]   # persona, outfit, locación, prop
- file: "img_climbing_wall.jpg"
  role: "LF"
  tags: ["L2", "PR1"]    # nueva locación + mismo prop
```

Categorías:
- **P** — Personaje / Sujeto
- **O** — Outfit
- **L** — Locación
- **PR** — Prop
- **S** — Estilo

Si una categoría tiene AL MENOS UN ref, sus descriptores estáticos quedan baneados en el MAIN prompt. Las categorías sin ref siguen siendo describibles.

## Casos soportados

| Case | Descripción | Word budget |
|---|---|---|
| 1 | Génesis text-to-image | 75-130 |
| 2 | Ancla image-with-refs | 75-130 |
| 3a | I2V FF only | 50-90 |
| 3b | I2V FF + LF | 50-90 |
| 3c | I2V motion control | 50-90 |
| 4 | Video con diálogo | 75-130 |

Word count: el MAX es HARD FAIL (Regla 10 v6.0). El MIN es WARN no-bloqueante (compresión válida si intencional).

## Override mechanism

Si una violación detectada es legítima en este caso, el usuario puede autorizarla por escrito en el turno actual. **Solo se acepta autorización expresa específica.**

Sintaxis:
```
OVERRIDE: <term-or-category> - <reason>
```

Ejemplos válidos:
```
OVERRIDE: red performance tank - necesito reforzar el color porque seeds previas lo pierden
OVERRIDE: L - autorizo describir locación porque la ref está muy oscura
OVERRIDE: slow motion - explícitamente quiero slow motion en este clip
```

Ejemplos NO válidos (genéricos, sin scope específico):
- "hazlo de todas formas"
- "ya sé que está en la ref, déjalo"
- "ready to copy paste"

El override solo es válido en el turno actual del usuario. Autorizaciones de turnos pasados NO persisten — cada prompt nuevo arranca STRICT.

## Reglas que aplica

1. **Redundancia por categoría**: si ref carga categoría X, no describir X en MAIN.
2. **Vocabulario baneado cross-platform**: `slow motion`, `cartoon`, `anime`, `3D render`, etc. solo en NEGATIVE block.
3. **Word count**: cap MAX duro = 90 (I2V) o 130 (T2I); MIN soft = 50/75.
4. **Negative prompt**: bloque obligatorio.
5. **Sports broadcast**: si flag activo, requiere `60fps` y `broadcast realism` en MAIN (Regla 26 v6.0).
6. **Exenciones**: términos en contexto de motion/cámara o como anchor direccional (`away from her face`, `across the climbing wall`) NO se flaggean.

## Limitaciones conocidas v1.0 (roadmap v1.1+)

- **Sinónimos**: "tank top" en ref + "athletic shirt" en prompt = no detectado. Solución v1.1: tabla de sinónimos en vocabularies.yaml.
- **Sub-tags por categoría**: O.upper / O.lower / P.face / P.body — para refs con coverage parcial. v1.2.
- **Embeddings semánticos**: para paráfrasis más sutiles. v2.0 si justifica el costo.
- **Auto-suggest rewrite**: hoy lista qué quitar; v1.1 podría generar versión limpia automática.
- **Vision check**: linter no ve las imágenes, depende de los tags. Si tageo mal, falla en silencio. Mitigación: review humano del tag antes de correr.

## Integración con skill

El linter NO corre solo. El skill `prompt-production-protocol` Step 5 debe invocarlo como item crítico. Ver `skill_update_step5.md` para la edit propuesta.

System prompt v6.1 (propuesta): nueva Regla 28 forzando llamada al linter antes de Step 6 delivery. Ver `system_prompt_v6_1_rule28.md`.

## Archivos del paquete

```
aurora-linter/
├── prompt_linter.py        # Script ejecutable
├── vocabularies.yaml       # Vocabulary lists por categoría
├── README.md               # Este archivo
├── skill_update_step5.md   # Edit propuesta al skill Step 5
├── system_prompt_v6_1_rule28.md  # Edit propuesta al system prompt
├── test_refs_session.yaml  # Test fixture
├── test_prompt_BAD.txt     # Test: prompt con 27 violaciones
├── test_prompt_GOOD.txt    # Test: prompt limpio
└── test_override_msg.txt   # Test: mensaje con overrides válidos
```

## Versión

v1.0 — 2026-05-27
Built by: Final Upgrade AI / Eric Toledano
Fuente: retrospectiva F7 sesión 2026-05-27
