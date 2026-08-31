#!/usr/bin/env bash
# Self-verification for the production gates. Run it yourself; trust the output,
# not a claim in a chat message.
#
#   bash .claude/hooks/verify.sh
#
# Every case below asserts an exit code. A gate that stops working fails loudly
# here instead of passing prompts through in silence.

set -uo pipefail

HOOKS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export HOOKS
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
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

BAD="$(msg brk 'Prompt:

```
cinematic epic masterpiece
```')"
for _ in 1 2 3; do fire gate_dramaturgy.py "$BAD" >/dev/null; done
check "libera el turno tras 3 bloqueos (anti-deadlock)" 1 \
  "$(fire gate_dramaturgy.py "$BAD")"

check "avisa fuerte si no encuentra el skill video" 1 \
  "$(FUPAI_SKILLS_ROOT=/no/existe fire gate_dramaturgy.py "$(msg v6 '```
cinematic
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
echo "=== payload corrupto (ningun gate debe morir en silencio) ==="
check "gate_dramaturgy sobrevive a JSON invalido" 1 "$(fire gate_dramaturgy.py 'no soy json')"
check "gate_shots sobrevive a JSON invalido"      1 "$(fire gate_shots.py 'no soy json')"

echo
echo "-------------------------------------------------------------------"
printf '  %s pasaron · %s fallaron\n' "$PASS" "$FAIL"
echo "-------------------------------------------------------------------"
echo
[[ "$FAIL" -eq 0 ]] || exit 1
