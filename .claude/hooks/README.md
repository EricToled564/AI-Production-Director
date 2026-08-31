# Gates de producción — enforcement fuera del modelo

Dos gates que el skill `ai-production-director` declara como obligatorios, movidos
de texto a código. La diferencia no es de redacción: un gate escrito en un SKILL.md
es una decisión que el modelo vuelve a tomar en cada turno; un gate en un hook corre
fuera del modelo y devuelve `exit 2`, y el turno no cierra.

No se agrega ninguna herramienta nueva. Ambos gates delegan en material que ya
vive dentro del pipeline.

## Qué hace cada gate

| Gate | Evento | Autoridad | Delega en |
|---|---|---|---|
| `gate_dramaturgy.py` | `Stop` | `ai-production-director` §6.1 | `video/references/dramaturgy.md`, sección *"What is banned"* |
| `gate_shots.py` | `PostToolUse` (Write/Edit) | `ai-production-director` Etapa 4 | `storyboard-architect/tools/validate_shots.py` |

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

14 casos, cada uno afirmando un exit code concreto — bloqueo, paso limpio,
override, anti-deadlock, auto-reparación del shim y supervivencia a payloads
corruptos. Si un gate deja de funcionar, esto falla en voz alta en vez de dejar
pasar prompts en silencio.

## Estado de verificación — honesto

**Probado en ejecución:**

- Los 14 casos de `verify.sh` pasan.
- `gate_dramaturgy.py` bloquea con `exit 2` un prompt con vocabulario prohibido y
  deja pasar uno limpio, prosa y overrides.
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
