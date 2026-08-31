# Gates de producción — enforcement fuera del modelo

Seis hooks que hacen ejecutables reglas que los skills ya declaraban obligatorias.
La diferencia no es de redacción: una regla escrita en un SKILL.md es una decisión
que el modelo vuelve a tomar en cada turno; en un hook corre fuera del modelo y
devuelve `exit 2`, y el turno no cierra.

No se agrega ninguna herramienta externa. Todos delegan en material que ya vive
dentro del pipeline instalado.

## Qué hace cada gate

| Gate | Evento | Autoridad | Delega en |
|---|---|---|---|
| `gate_dramaturgy.py` | `Stop` | `ai-production-director` §6.1 | `video/references/dramaturgy.md`, sección *"What is banned"* |
| `gate_image.py` | `Stop` | `ai-production-director` Etapa 5 y §6.2 | `image/references/golden-rules.md` |
| `gate_shots.py` | `PostToolUse` (Write/Edit) | `ai-production-director` Etapa 4 | `storyboard-architect/tools/validate_shots.py` |
| `gate_microgate.py` | `Stop` | `produccion-visual-sw30` §MICRO-GATE | la cabecera de 3 líneas |
| `inject_rules.py` | `UserPromptSubmit` | `produccion-visual-sw30` §PREGUNTA DE AVANCE | inyecta las fuentes completas |

## El gate que importa más que los demás

Los otros cinco inspeccionan la salida. Ninguno toca la falla real: **qué se lee**.
Mientras leer sea una elección, se puede seguir eligiendo saltarse la parte que
importa — que es exactamente lo que pasó en la sesión donde se construyó esto:
`produccion-visual-sw30` estaba instalado desde el primer minuto, su descripción
dice "APLICAR ANTES de producir" y dispara con la palabra "gate", y no se abrió
hasta que el usuario lo señaló dos veces.

`inject_rules.py` quita la elección. En cualquier prompt que toque producción
visual inyecta las fuentes que gobiernan, **completas y verbatim** — el criterio
que el propio skill exige: *"leídos COMPLETOS todos los archivos del skill
aplicables al caso, no fragmentos ni grep"*. Hoy son 41,226 caracteres para un
caso de imagen: `produccion-visual-sw30`, `ai-production-director`, `image/SKILL.md`
y `golden-rules.md`. Lo que no quepa en presupuesto se nombra explícitamente en
la cabecera de la inyección, para que una omisión no pueda pasar en silencio.

`gate_microgate.py` hace efectiva la línea *"Entrega sin cabecera = inválida"*:
sin las 3 líneas `SKILL:` / `RIESGOS:` / `TÉCNICA:` el turno no cierra. Y `SKILL:`
tiene que nombrar un archivo `.md` que exista de verdad en los skills instalados,
así que una cabecera de relleno se rechaza igual que la ausencia de cabecera.

**`gate_image.py`** aplica las golden rules del skill `image` a prompts de imagen,
con los verbos parseados del archivo en tiempo de ejecución:

| Check | Regla | Efecto |
|---|---|---|
| R1 | *Start with a Verb* | bloquea |
| R4 | *Natural Language* (keyword soup) | bloquea |
| §6.2 | modelo destino declarado | bloquea |
| R2 | *Positive Framing* | **advierte** |

R2 no bloquea a propósito: el ejemplo aprobado del propio skill dice `no makeup`,
así que una detección estricta de negaciones rechazaría prompts que el skill
bendice. Se reporta como contexto, no como veto.

Si el mensaje nombra un modelo de video (Kling, Veo, Sora, Seedance…) y ninguno de
imagen, este gate no opina — ese prompt es de `gate_dramaturgy.py`.

**`gate_dramaturgy.py`** lee la lista prohibida del skill `video` **en tiempo de
ejecución**. No hay copia. Si editas `dramaturgy.md`, el gate cambia contigo.
Hoy extrae 11 términos: `cinematic`, `professional`, `high quality`, `masterpiece`,
`stunning`, `epic`, `amazing`, `beautiful lighting`, `dynamic camera`,
`intense moment`, `powerful scene`.

Sólo escanea **bloques de código cercados** del mensaje final. Explicar la regla en
prosa no dispara nada; entregar un prompt sí. Escape auditable, con la misma
sintaxis que el pipeline ya usa:

```
OVERRIDE: cinematic - el tagline on-screen del cliente lo exige
```

**`gate_shots.py`** corre `validate_shots.py` cada vez que se escribe un
`shots.json` o `text-overlays.json`, y repara antes dos defectos de empaquetado que
impedían que ese gate corriera **jamás** en una instalación synced:

1. `jsonschema` ausente — el validador salía `1` por la razón equivocada.
2. `_shotkit.py` fija `REPO_ROOT` al directorio del skill y luego le concatena
   `skills/storyboard-architect/…`, un layout que sólo existe si shotkit está
   instalado como repo. El hook recrea ese layout con symlinks aditivos en cada
   corrida, así que un re-sync del skill no deja el gate roto de forma permanente.

Ninguno de los dos modifica el contenido de tus skills.

## Verificación

No hace falta creerle a nadie:

```bash
bash .claude/hooks/verify.sh
```

34 casos, cada uno afirmando un exit code concreto — bloqueo, paso limpio,
override, anti-deadlock, auto-reparación del shim y supervivencia a payloads
corruptos. Si un gate deja de funcionar, esto falla en voz alta en vez de dejar
pasar prompts en silencio.

## Cobertura real — el número que ningún gate verde reemplaza

`produccion-visual-sw30/SKILL.md` §"Sistema de cobertura de reglas" documenta la
causa raíz: *"el catálogo de reglas salía de la memoria y cubría 26 de 209
enunciados de la fuente (12%)"*, y especifica la cadena que lo rompe
(`rule_registry.py`, `rule_ledger.py`, `audit_gi2.py`).

**Ninguno de esos scripts existía.** Ni `production-package/`, ni `RULES_MATRIX.md`.
El skill que dice *"la fuente manda, no la memoria"* era, él mismo, sólo memoria —
incluyendo su línea de estado *"124 reglas aplicables · 0 pendientes · 100%
dispuesto"*, que no podía ser cierta sin un ledger que la calculara.

`rule_registry.py` y `rule_ledger.py` se construyen aquí, según esa especificación.

### Medición

```
$ python3 .claude/hooks/rule_registry.py --skill image --stats
enunciados: 194          # el skill medía 209 con su propio extractor
```

Pipeline completo: **1,263 enunciados normativos** (1,213 únicos tras deduplicar
los repetidos entre skills), repartidos así:

| skill | reglas | | skill | reglas |
|---|---:|---|---|---:|
| `video` | 363 | | `brand-lock-extractor` | 90 |
| `image` | 194 | | `visual-asset-critic` | 64 |
| `visual-prompt-forge` | 181 | | `screenwriter` | 58 |
| `storyboard-architect` | 178 | | `produccion-visual-sw30` | 46 |
| `ai-video-storyboard` | 36 | | `ai-production-director` | 27 |
| `storyboard-html-preview` | 25 | | `visual-media` | 1 |

**Los gates de este repo verifican 26 controles = 2.1% de esa superficie.** Una
suite en 27/27 verde no cambia ese número, y presentarla sin él induce a error.

### Cómo se usa el ledger

```bash
python3 .claude/hooks/rule_registry.py --skill image --out reg.json --stats
python3 .claude/hooks/rule_ledger.py --registry reg.json --dispositions disp.json
```

Cada regla necesita disposición explícita o queda `PENDING`, y una sola `PENDING`
cierra el gate con `exit 1`. `CHECK` exige el campo `by` (qué la verifica), `NA`
exige `reason` escrita. Una disposición cuyo id ya no está en el registro se
reporta `STALE`: el texto de origen cambió y la afirmación dejó de cubrir algo.

Los ids son `sha1(ruta + texto normalizado)`, así que sobreviven a que se muevan
líneas y cambian cuando cambia la redacción. Esa es justo la propiedad que impide
heredar una cobertura vieja sobre un skill nuevo.

## Dos contradicciones encontradas en los skills

Salieron al calibrar el gate de imagen contra los ejemplos que el propio skill
marca con ✅. No las resuelve el gate — son cosas a decidir en los skills.

1. **El ejemplo ✅ de la Regla 4 de `image` viola la Regla 1 y §6.1.**
   `"A cinematic wide shot of a futuristic sports car…"` empieza con `A` en vez de
   un verbo, y usa `cinematic`, que §6.1 declara prohibido y que "gana siempre".
   El gate lo bloquea. Es coherente con el director; el ejemplo es el que está mal.

2. **El skill `image` no tiene lista de vocabulario prohibido propia.** Hereda la de
   `video`/dramaturgy vía §6.1, que está escrita para dramaturgia de movimiento.
   Funciona, pero conviene decidir si imagen necesita términos propios.

## Estado de verificación — honesto

**Probado en ejecución:**

- Los 34 casos de `verify.sh` pasan, y la suite es idempotente en corridas seguidas.
- `gate_dramaturgy.py` bloquea con `exit 2` un prompt con vocabulario prohibido y
  deja pasar uno limpio, prosa y overrides. Probado con prompts de imagen
  (Nano Banana Pro, GPT Image 2) además de video.
- `gate_image.py` bloquea keyword soup, falta de verbo inicial y prompts sin modelo
  destino; deja pasar los ejemplos aprobados del skill e ignora prompts de video.
- `gate_shots.py` bloquea con `exit 2` un `shots.json` con solape de timing y con
  hueco de timing, señalando el shot exacto.
- `validate_shots.py --selftest` pasa sus 12 checks, y los 3 ejemplos incluidos en
  el skill validan una vez aplicado el shim (antes fallaban los 3).

**NO probado:**

- Que Claude Code dispare los hooks automáticamente. En la sesión donde se
  construyeron, `.claude/` no existía al arrancar y los hooks de proyecto se cargan
  al inicio de sesión, así que el harness no los invocó. Los scripts se probaron
  alimentándoles el payload documentado por stdin, que es el mismo contrato.

Cómo cerrar ese hueco tú mismo, en una sesión **nueva** de Claude Code sobre este
repo: pide un prompt de video que incluya la palabra `cinematic`. Si el gate está
cargado, el turno no cierra y ves el reporte de bloqueo. Si cierra normalmente, los
hooks no se cargaron y no hay enforcement — mejor saberlo con una prueba de diez
segundos que en medio de una producción.

## Requisito

```bash
pip install pyyaml jsonschema --break-system-packages
```

Sin `jsonschema`, `gate_shots.py` lo dice y sale `1` (error visible, no bloqueo
silencioso). Nunca finge haber validado.

## Límites reales

- El gate de vocabulario es léxico. Atrapa `cinematic`; no atrapa un shot sin los
  tres detalles que exige `dramaturgy.md` §2 — eso es semántico y ningún gate
  determinista lo resuelve. Cubre el modo de fallo más frecuente, no todos.
- Un prompt entregado fuera de un bloque de código no se escanea. Es el precio de
  no tener falsos positivos sobre prosa.
- Los hooks son de Claude Code. En el chat de claude.ai no existen, y ahí estos
  gates no aplican.
