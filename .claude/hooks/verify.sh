#!/usr/bin/env bash
# Self-verification for the production gates. Run it yourself; trust the output,
# not a claim in a chat message.
#
#   bash .claude/hooks/verify.sh
#
# Every case below asserts an exit code. A gate that stops working fails loudly
# here instead of passing prompts through in silence.

set -uo pipefail
# El propio verify.sh se valida antes de correr: un error de sintaxis aqui hace
# que la suite reporte verde sin haber corrido los ultimos casos.
bash -n "${BASH_SOURCE[0]}" || { echo "verify.sh tiene un error de sintaxis"; exit 2; }

HOOKS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export HOOKS
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
# El breaker cuenta bloqueos consecutivos por sesion. Sin esto, el estado de una
# corrida anterior hace que la suite se comporte distinto la segunda vez.
rm -rf "${TMPDIR:-/tmp}/fupai-gate"
PASS=0
FAIL=0

fire() { # fire <script> <json-payload> -> echoes exit code, captures stderr
  printf '%s' "$2" | python3 "$HOOKS/$1" 2>"$TMP/err" >/dev/null
  echo $?
}

check() { # check <name> <expected> <actual>
  if [[ "$2" == "$3" ]]; then
    printf '  \033[32mPASS\033[0m  %-52s exit=%s\n' "$1" "$3"
    PASS=$((PASS + 1))
  else
    printf '  \033[31mFAIL\033[0m  %-52s exit=%s (esperado %s)\n' "$1" "$3" "$2"
    sed 's/^/          /' "$TMP/err" | head -6
    FAIL=$((FAIL + 1))
  fi
}

msg() { python3 -c 'import json,sys;print(json.dumps({"session_id":sys.argv[1],"hook_event_name":"Stop","last_assistant_message":sys.argv[2]}))' "$1" "$2"; }
wrote() { python3 -c 'import json,sys;print(json.dumps({"session_id":"v","hook_event_name":"PostToolUse","tool_name":"Write","tool_input":{"file_path":sys.argv[1]}}))' "$1"; }

echo
echo "=== GATE 6.1 — vocabulario prohibido (fuente: video/references/dramaturgy.md) ==="

TERMS=$(python3 - <<'PY'
import importlib.util, os, sys
spec = importlib.util.spec_from_file_location("g", os.path.join(os.environ["HOOKS"], "gate_dramaturgy.py"))
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
p = g.find_dramaturgy()
if p is None:
    print("0"); sys.exit()
print(len(g.load_banned(p)))
PY
)
if [[ "${TERMS:-0}" -gt 0 ]]; then
  printf '  \033[32mPASS\033[0m  %-52s %s terminos\n' "lee la lista prohibida del skill video" "$TERMS"
  PASS=$((PASS + 1))
else
  printf '  \033[31mFAIL\033[0m  %-52s\n' "NO encuentra video/references/dramaturgy.md"
  FAIL=$((FAIL + 1))
fi

check "bloquea prompt con vocabulario prohibido" 2 \
  "$(fire gate_dramaturgy.py "$(msg v1 'Prompt:

```
Wide shot, cinematic lighting, epic and stunning, masterpiece.
```')")"

check "deja pasar prompt limpio" 0 \
  "$(fire gate_dramaturgy.py "$(msg v2 'Prompt:

```
Wide shot, 35mm. Wet asphalt throws a sodium-lamp streak. Knuckles whiten.
```')")"

check "no confunde prosa con entrega de prompt" 0 \
  "$(fire gate_dramaturgy.py "$(msg v3 'La palabra cinematic esta prohibida, igual que epic y masterpiece.')")"

check "respeta OVERRIDE explicito" 0 \
  "$(fire gate_dramaturgy.py "$(msg v4 'OVERRIDE: cinematic - el tagline on-screen lo exige

```
Wet asphalt, sodium lamp. On-screen text reads "cinematic".
```')")"

BAD="$(msg brk 'Prompt para Nano Banana Pro:

```
Create a shot with cinematic epic masterpiece lighting.
Format: 4:5
```')"
for _ in 1 2 3; do fire gate_dramaturgy.py "$BAD" >/dev/null; done
check "libera el turno tras 3 bloqueos (anti-deadlock)" 1 \
  "$(fire gate_dramaturgy.py "$BAD")"

check "avisa fuerte si no encuentra el skill video" 1 \
  "$(FUPAI_SKILLS_ROOT=/no/existe fire gate_dramaturgy.py "$(msg v6 'Prompt para Nano Banana:

```
Create a cinematic shot.
Format: 4:5
```')")"

echo
echo "=== INYECCION — la lectura deja de ser eleccion del modelo ==="

inj() { python3 -c 'import json,sys;print(json.dumps({"hook_event_name":"UserPromptSubmit","prompt":sys.argv[1]}))' "$1" \
  | python3 "$HOOKS/inject_rules.py" 2>/dev/null; }

CHARS=$(inj "dame un prompt de imagen para Nano Banana del ancla" \
  | python3 -c 'import json,sys;d=sys.stdin.read();print(len(json.loads(d)["hookSpecificOutput"]["additionalContext"]) if d.strip() else 0)')
if [[ "${CHARS:-0}" -gt 20000 ]]; then
  printf '  \033[32mPASS\033[0m  %-52s %s chars\n' "inyecta las fuentes obligatorias verbatim" "$CHARS"
  PASS=$((PASS + 1))
else
  printf '  \033[31mFAIL\033[0m  %-52s %s chars\n' "inyecta las fuentes obligatorias verbatim" "${CHARS:-0}"
  FAIL=$((FAIL + 1))
fi

NAMES=$(inj "dame un prompt de imagen para Nano Banana" \
  | python3 -c 'import json,sys;d=sys.stdin.read();print(json.loads(d)["hookSpecificOutput"]["additionalContext"].splitlines()[3] if d.strip() else "")')
if [[ "$NAMES" == *"produccion-visual-sw30"* && "$NAMES" == *"golden-rules"* ]]; then
  printf '  \033[32mPASS\033[0m  %-52s\n' "incluye sw30 + golden-rules en un caso de imagen"
  PASS=$((PASS + 1))
else
  printf '  \033[31mFAIL\033[0m  %-52s %s\n' "incluye sw30 + golden-rules" "$NAMES"
  FAIL=$((FAIL + 1))
fi

if [[ -z "$(inj 'que hora es')" ]]; then
  printf '  \033[32mPASS\033[0m  %-52s\n' "no inyecta en prompts ajenos a produccion"
  PASS=$((PASS + 1))
else
  printf '  \033[31mFAIL\033[0m  %-52s\n' "inyecta donde no debe"
  FAIL=$((FAIL + 1))
fi

echo
echo "=== MICRO-GATE — cabecera de 3 lineas (produccion-visual-sw30) ==="

check "bloquea entrega de prompt sin cabecera" 2 \
  "$(fire gate_microgate.py "$(msg m1 'Prompt para Nano Banana:

```
Create an editorial portrait of a runner. Format: 4:5
```')")"

check "acepta cabecera con archivo real y campos llenos" 0 \
  "$(fire gate_microgate.py "$(msg m2 'SKILL: image/references/golden-rules.md secciones 1-7
RIESGOS: look plastico por luz suave; lo mitiga la linea de luz dura rasante
TECNICA: template T1 de rostro, fuente produccion-visual-sw30/SKILL.md

Prompt para Nano Banana:

```
Create an editorial portrait of a runner. Format: 4:5
```')")"

check "rechaza cabecera de relleno (archivo inexistente)" 2 \
  "$(fire gate_microgate.py "$(msg m3 'SKILL: mis notas internas
RIESGOS: varios
TECNICA: ninguna

```
Create a portrait for Nano Banana. Format: 4:5
```')")"

check "no exige cabecera si no hay entrega visual" 0 \
  "$(fire gate_microgate.py "$(msg m4 'Te explico como funciona el micro-gate, sin entregar prompts.')")"

echo
echo "=== GATE IMAGEN — golden rules (fuente: image/references/golden-rules.md) ==="

VERBS=$(python3 - <<'PY'
import importlib.util, os, sys
spec = importlib.util.spec_from_file_location("g", os.path.join(os.environ["HOOKS"], "gate_image.py"))
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
p = g.find_golden_rules()
print(len(g.load_verbs(p)) if p else 0)
PY
)
if [[ "${VERBS:-0}" -gt 0 ]]; then
  printf '  \033[32mPASS\033[0m  %-52s %s verbos\n' "lee las golden rules del skill image" "$VERBS"
  PASS=$((PASS + 1))
else
  printf '  \033[31mFAIL\033[0m  %-52s\n' "NO encuentra image/references/golden-rules.md"
  FAIL=$((FAIL + 1))
fi

check "bloquea keyword soup (R4) y falta de verbo (R1)" 2 \
  "$(fire gate_image.py "$(msg i1 'Prompt para Nano Banana:

```
Cool shoe, neon, city, night, 8k
```')")"

check "bloquea prompt sin modelo destino declarado (6.2)" 2 \
  "$(fire gate_image.py "$(msg i2 'Anchor:

```
Create an editorial portrait of a runner in a stadium tunnel.
Format: 4:5
```')")"

check "deja pasar el ejemplo aprobado del skill (Havana)" 0 \
  "$(fire gate_image.py "$(msg i3 'Prompt para GPT Image 2:

```
Create an editorial portrait set in Havana, 1957.
Subject: jazz musician against a pastel colonial building, trumpet at his side.
Format: 3:4
```')")"

check "no bloquea por R2 (el skill aprueba \"no makeup\")" 0 \
  "$(fire gate_image.py "$(msg i4 'Prompt para Nano Banana Pro:

```
Create a fashion editorial portrait with Peter Lindbergh influence.
Subject: model in oversized blazer, no makeup, wind-tousled hair.
Format: 2:3
```')")"

check "no opina sobre un prompt de video (Kling)" 0 \
  "$(fire gate_image.py "$(msg i5 'Prompt para Kling 3.0:

```
Wide shot, 35mm. Wet asphalt throws a sodium-lamp streak. Knuckles whiten.
```')")"

check "respeta OVERRIDE de regla" 0 \
  "$(fire gate_image.py "$(msg i6 'OVERRIDE: R1 - el cliente entrega el prompt ya redactado

Prompt para Nano Banana:

```
A wide shot of wet asphalt under a sodium lamp.
```')")"

echo
echo "=== GATE ETAPA 4 — validate_shots.py (shotkit) ==="

ARCH=$(python3 - <<'PY'
import importlib.util, os
spec = importlib.util.spec_from_file_location("g", os.path.join(os.environ["HOOKS"], "gate_shots.py"))
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
print(g.find_architect() or "")
PY
)

if [[ -z "$ARCH" ]]; then
  printf '  \033[31mFAIL\033[0m  %-52s\n' "storyboard-architect no encontrado"
  FAIL=$((FAIL + 1))
elif ! python3 -c "import jsonschema" 2>/dev/null; then
  printf '  \033[31mFAIL\033[0m  %-52s\n' "falta jsonschema (pip install jsonschema)"
  FAIL=$((FAIL + 1))
else
  EX="$ARCH/examples/30s-pain-proof-promise"
  cp "$EX"/* "$TMP/" 2>/dev/null

  check "deja pasar un shot list valido" 0 "$(fire gate_shots.py "$(wrote "$TMP/shots.json")")"

  python3 - "$TMP/shots.json" <<'PY'
import json, sys
p = sys.argv[1]; d = json.load(open(p))
d["shots"][1]["start"] = 0.8          # solape con shot_01
json.dump(d, open(p, "w"), indent=2)
PY
  check "bloquea solape de timing entre shots" 2 "$(fire gate_shots.py "$(wrote "$TMP/shots.json")")"

  check "ignora archivos que no son del pipeline" 0 "$(fire gate_shots.py "$(wrote "$TMP/README.md")")"

  rm -rf "$ARCH/skills"
  check "repara solo el shim de rutas de shotkit" 2 "$(fire gate_shots.py "$(wrote "$TMP/shots.json")")"
  [[ -L "$ARCH/skills/storyboard-architect" ]] \
    && { printf '  \033[32mPASS\033[0m  %-52s\n' "shim recreado tras borrarlo"; PASS=$((PASS + 1)); } \
    || { printf '  \033[31mFAIL\033[0m  %-52s\n' "shim NO recreado"; FAIL=$((FAIL + 1)); }
fi

echo
echo "=== REGISTRY + LEDGER — cobertura sobre la fuente, no sobre la memoria ==="

python3 "$HOOKS/rule_registry.py" --skill image --out "$TMP/reg.json" --stats >"$TMP/reg.log" 2>&1
N=$(grep -oE 'enunciados:[[:space:]]+[0-9]+' "$TMP/reg.log" | grep -oE '[0-9]+')
if [[ "${N:-0}" -gt 100 ]]; then
  printf '  \033[32mPASS\033[0m  %-52s %s enunciados\n' "extrae reglas del skill image" "$N"
  PASS=$((PASS + 1))
else
  printf '  \033[31mFAIL\033[0m  %-52s %s\n' "extrae reglas del skill image" "${N:-0}"
  FAIL=$((FAIL + 1))
fi

echo '{}' > "$TMP/disp.json"
python3 "$HOOKS/rule_ledger.py" --registry "$TMP/reg.json" --dispositions "$TMP/disp.json" >/dev/null 2>&1
check "ledger cierra el gate con reglas sin disponer" 1 "$?"

FIRST=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['rules'][0]['id'])" "$TMP/reg.json")
python3 -c "
import json,sys
rid=sys.argv[1]
json.dump({rid:{'status':'CHECK'}}, open(sys.argv[2],'w'))
" "$FIRST" "$TMP/disp.json"
python3 "$HOOKS/rule_ledger.py" --registry "$TMP/reg.json" --dispositions "$TMP/disp.json" >/dev/null 2>&1
check "rechaza CHECK sin decir quien lo verifica" 1 "$?"

python3 -c "
import json,sys
reg=json.load(open(sys.argv[1]))
json.dump({r['id']:{'status':'NA','reason':'prueba'} for r in reg['rules']}, open(sys.argv[2],'w'))
" "$TMP/reg.json" "$TMP/disp.json"
python3 "$HOOKS/rule_ledger.py" --registry "$TMP/reg.json" --dispositions "$TMP/disp.json" >/dev/null 2>&1
check "abre el gate solo al 100% dispuesto" 0 "$?"

python3 -c "
import json,sys
d=json.load(open(sys.argv[1])); d['000000000000']={'status':'NA','reason':'huerfana'}
json.dump(d, open(sys.argv[1],'w'))
" "$TMP/disp.json"
STALE=$(python3 "$HOOKS/rule_ledger.py" --registry "$TMP/reg.json" --dispositions "$TMP/disp.json" --json 2>/dev/null | python3 -c 'import json,sys;print(json.load(sys.stdin)["stale"])')
check "detecta disposiciones huerfanas (STALE)" 1 "$STALE"

echo
echo "=== FALSOS POSITIVOS — un gate que bloquea texto tecnico se desactiva ==="

TECNICO='Donde para:

```
get_health  -> authenticated: false
```

```bash
python3 nblm_load.py --corpus notebooklm-corpus
```'
for g in gate_image gate_dramaturgy gate_microgate; do
  check "$g deja pasar salida de terminal y shell" 0 "$(fire $g.py "$(msg fp-$g "$TECNICO")")"
done

check "no bloquea shell aunque la prosa nombre el modelo" 0 \
  "$(fire gate_image.py "$(msg fp2 'Para generar con Nano Banana corre:

```bash
python3 gen.py --model nano-banana
```')")"

check "no bloquea terminal con palabras prohibidas dentro" 0 \
  "$(fire gate_dramaturgy.py "$(msg fp3 'Resultado:

```
  PASS  professional check   exit=0
  FAIL  high quality assert  exit=1
```')")"

check "no bloquea un bloque json etiquetado" 0 \
  "$(fire gate_dramaturgy.py "$(msg fp4 '```json
{"style": "cinematic", "q": "high quality"}
```')")"

echo
echo "=== payload corrupto (ningun gate debe morir en silencio) ==="
check "gate_dramaturgy sobrevive a JSON invalido" 1 "$(fire gate_dramaturgy.py 'no soy json')"
check "gate_image sobrevive a JSON invalido"      1 "$(fire gate_image.py 'no soy json')"
check "gate_shots sobrevive a JSON invalido"      1 "$(fire gate_shots.py 'no soy json')"

echo
echo "-------------------------------------------------------------------"
printf '  %s pasaron · %s fallaron\n' "$PASS" "$FAIL"
echo "-------------------------------------------------------------------"
echo
[[ "$FAIL" -eq 0 ]] || exit 1
