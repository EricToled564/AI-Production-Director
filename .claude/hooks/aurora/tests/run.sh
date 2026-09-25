#!/usr/bin/env bash
# Pruebas del linter parcheado (.claude/hooks/aurora/prompt_linter.py).
#
# Cada prueba reproduce una contradicción detectada entre el linter original del skill
# aurora-prompt-linter y el resto del pipeline (video, image, visual-prompt-forge,
# produccion-visual-sw30, ai-production-director) y afirma el exit code y, donde aplica,
# la presencia o ausencia de un WARN o FAIL concreto en la salida.
#
# Uso:  bash .claude/hooks/aurora/tests/run.sh          (sale 0 si todo pasa, 1 si algo falla)
#       VERBOSE=1 bash .claude/hooks/aurora/tests/run.sh (imprime la salida de cada prueba)
#
# Regla: si una prueba falla se corrige el código, no la prueba.

set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LINTER="$HERE/../prompt_linter.py"
FX="$HERE/fixtures"
OUT="${TMPDIR:-/tmp}/aurora_linter_tests.$$"
mkdir -p "$OUT"
trap 'rm -rf "$OUT"' EXIT

PASS=0
FAIL=0
FALLIDAS=()
LAST_OUT=""
LAST_EXIT=0

# run <nombre> <exit esperado> <args del linter...>
run() {
  local name="$1" expected="$2"
  shift 2
  LAST_OUT="$OUT/$name.out"
  python3 "$LINTER" "$@" > "$LAST_OUT" 2>&1
  LAST_EXIT=$?
  if [ "${VERBOSE:-0}" = "1" ]; then
    sed 's/^/      | /' "$LAST_OUT"
  fi
  if [ "$LAST_EXIT" -ne "$expected" ]; then
    echo "    [FALLA] exit $LAST_EXIT, esperado $expected. Salida:"
    sed 's/^/      | /' "$LAST_OUT" | head -60
    return 1
  fi
  return 0
}
expect_has()   { grep -qF -- "$1" "$LAST_OUT" || { echo "    [FALLA] falta en la salida: $1"; return 1; }; }
expect_not()   { if grep -qF -- "$1" "$LAST_OUT"; then echo "    [FALLA] no debería aparecer: $1"; return 1; fi; }
expect_regex() { grep -qiE -- "$1" "$LAST_OUT" || { echo "    [FALLA] falta (regex): $1"; return 1; }; }
expect_no_regex() { if grep -qiE -- "$1" "$LAST_OUT"; then echo "    [FALLA] no debería aparecer (regex): $1"; grep -iE -- "$1" "$LAST_OUT" | sed 's/^/      | /'; return 1; fi; }
expect_count() {
  local n
  n=$(grep -cF -- "$1" "$LAST_OUT")
  [ "$n" -eq "$2" ] || { echo "    [FALLA] '$1' aparece $n veces, esperado $2"; return 1; }
}

# ---------------------------------------------------------------------------
# Pruebas. Cada función devuelve 0 si pasa.
# ---------------------------------------------------------------------------

t01() {
  echo "T01 Prompt T1 SW30 (~250 palabras) para nano_banana_pro caso 1 -> exit 0 con WARN de palabras (P1)"
  local ok=0
  run t01 0 --prompt "$FX/t1_nano_250.txt" --refs "$FX/refs_empty.yaml" --case 1 --platform nano_banana_pro || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_regex "WARN Word count [0-9]+ above platform budget max 120" || ok=1
  expect_not "FAIL [STRUCTURE] 'word_count" || ok=1
  return $ok
}

t02() {
  echo "T02 GPT Image 2 con 'Constraints:' y sin 'Negative:' caso 1 -> exit 0 (P2: el slot Constraints es el bloque negativo)"
  local ok=0
  run t02 0 --prompt "$FX/gpt_constraints.txt" --refs "$FX/refs_empty.yaml" --case 1 --platform gpt_image_2 || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_has "Negative block: present (policy optional, marker constraints)" || ok=1
  expect_has "PRESENT constraints_slot" || ok=1
  return $ok
}

t03() {
  echo "T03 Prompt Kling caso 3a sin bloque negativo -> exit 1 (P2: Kling tiene campo negativo dedicado)"
  local ok=0
  run t03 1 --prompt "$FX/kling_3a_no_negative.txt" --refs "$FX/refs_ff_location.yaml" --case 3a --platform kling_3.0 || ok=1
  expect_has "FAIL [STRUCTURE] 'negative_prompt'" || ok=1
  return $ok
}

t04() {
  echo "T04 Caso 2 con --ref-role character, identity block presente y descriptores P -> exit 0 (P3)"
  local ok=0
  run t04 0 --prompt "$FX/case2_character_identity.txt" --refs "$FX/refs_character.yaml" --case 2 --platform nano_banana_pro --ref-role character || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_not "FAIL [P]" || ok=1
  expect_not "identity block absent" || ok=1
  expect_has "P/O descriptors allowed" || ok=1
  return $ok
}

t04b() {
  echo "T04b Caso 2 con --ref-role character y SIN identity block -> exit 0 con WARN 'identity block absent' (P3, U7)"
  local ok=0
  run t04b 0 --prompt "$FX/case2_no_identity.txt" --refs "$FX/refs_character.yaml" --case 2 --platform nano_banana_2 --ref-role character --vocab "$HERE/../vocabularies.yaml" || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_has "WARN identity block absent" || ok=1
  expect_has "snapshot nano_banana_2__2" || ok=1
  return $ok
}

t05() {
  echo "T05 Caso 3a con --ref-role ff y descriptores P en MAIN -> exit 1 (P3: I2V no re-describe, kling.md §10)"
  local ok=0
  run t05 1 --prompt "$FX/kling_3a_p_descriptors.txt" --refs "$FX/refs_ff_person.yaml" --case 3a --platform kling_3.0 --ref-role ff || ok=1
  expect_has "FAIL [P] 'athletic woman'" || ok=1
  expect_has "FAIL [P] 'ponytail'" || ok=1
  return $ok
}

t06() {
  echo "T06 Caso 2 con --series-lock que contiene 'gym' y prompt con 'gym' verbatim -> exit 0 (P4, forge Rule 3)"
  local ok=0
  run t06 0 --prompt "$FX/case2_series_lock.txt" --refs "$FX/refs_character_location.yaml" --case 2 --platform nano_banana_pro --series-lock "$FX/series_lock.json" || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_not "FAIL [L]" || ok=1
  expect_not "series_lock.environment not found" || ok=1
  return $ok
}

t06b() {
  echo "T06b Control: el mismo prompt SIN --series-lock -> exit 1 con FAIL [L] 'gym' (demuestra que la exención hace el trabajo)"
  local ok=0
  run t06b 1 --prompt "$FX/case2_series_lock.txt" --refs "$FX/refs_character_location.yaml" --case 2 --platform nano_banana_pro || ok=1
  expect_has "FAIL [L] 'gym'" || ok=1
  return $ok
}

t07() {
  echo "T07 'her jaw locks, sweat beads' con ref P rol ff -> exit 0 por exención de micro-acción corporal (P5, dramaturgy §2)"
  local ok=0
  run t07 0 --prompt "$FX/kling_3a_body_micro.txt" --refs "$FX/refs_ff_person.yaml" --case 3a --platform kling_3.0 --ref-role ff || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_not "FAIL [P]" || ok=1
  return $ok
}

t08() {
  echo "T08 Prompt con 'cinematic' -> exit 1 (P6: director §6.1 gana siempre)"
  local ok=0
  run t08 1 --prompt "$FX/kling_3a_cinematic.txt" --refs "$FX/refs_ff_location.yaml" --case 3a --platform kling_3.0 || ok=1
  expect_has "FAIL [BANNED] 'cinematic'" || ok=1
  return $ok
}

t09() {
  echo "T09 Prompt ilustración con 'anime': --treatment ilustracion -> exit 0; fotorreal (default) -> exit 1 (P7)"
  local ok=0
  run t09a 0 --prompt "$FX/illustration_anime.txt" --refs "$FX/refs_empty.yaml" --case 1 --platform gpt_image_2 --treatment ilustracion || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_not "FAIL [BANNED] 'anime'" || ok=1
  run t09b 1 --prompt "$FX/illustration_anime.txt" --refs "$FX/refs_empty.yaml" --case 1 --platform gpt_image_2 || ok=1
  expect_has "FAIL [BANNED] 'anime'" || ok=1
  return $ok
}

t10() {
  echo "T10 'ultra-slow motion' Kling -> exit 0 sin WARN; 'slow motion' con --treatment race -> exit 1; fotorreal -> WARN (P7)"
  local ok=0
  run t10a 0 --prompt "$FX/kling_3a_ultra_slow.txt" --refs "$FX/refs_ff_location.yaml" --case 3a --platform kling_3.0 || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_no_regex "WARN.*slow motion" || ok=1
  run t10b 1 --prompt "$FX/kling_3a_slow.txt" --refs "$FX/refs_ff_location.yaml" --case 3a --platform kling_3.0 --treatment race || ok=1
  expect_has "FAIL [BANNED] 'slow motion'" || ok=1
  expect_has "race-and-speed" || ok=1
  run t10c 0 --prompt "$FX/kling_3a_slow.txt" --refs "$FX/refs_ff_location.yaml" --case 3a --platform kling_3.0 || ok=1
  expect_regex "WARN 'slow motion' in MAIN" || ok=1
  return $ok
}

t11() {
  echo "T11 --sports-broadcast en caso 1 -> exit 0 con WARN explicativo (P8)"
  local ok=0
  run t11 0 --prompt "$FX/t1_nano_250.txt" --refs "$FX/refs_empty.yaml" --case 1 --platform nano_banana_pro --sports-broadcast || ok=1
  expect_has "WARN --sports-broadcast ignored for case 1" || ok=1
  expect_not "FAIL [REQUIRED]" || ok=1
  expect_has "Sports broadcast mode: ignored" || ok=1
  return $ok
}

t12() {
  echo "T12 --case T1 se acepta y mapea a 1; también CLIP-FF -> 3a y CLIP-DIALOGO -> 4 (P9)"
  local ok=0
  run t12a 0 --prompt "$FX/t1_nano_250.txt" --refs "$FX/refs_empty.yaml" --case T1 --platform nano_banana_pro || ok=1
  expect_has "Case: 1 (Genesis (text-to-image)) [alias T1]" || ok=1
  run t12b 0 --prompt "$FX/kling_3a_clean.txt" --refs "$FX/refs_ff_location.yaml" --case CLIP-FF --platform kling_3.0 || ok=1
  expect_has "Case: 3a (I2V FF only) [alias CLIP-FF]" || ok=1
  run t12d 0 --prompt "$FX/kling_4_dialogue.txt" --refs "$FX/refs_empty.yaml" --case CLIP-DIALOGO --platform kling_3.0 || ok=1
  expect_has "Case: 4 (Video with dialogue) [alias CLIP-DIALOGO]" || ok=1
  expect_has "snapshot kling_3.0__4" || ok=1
  # Alias desconocido -> error de uso (exit 2), no un FAIL silencioso
  run t12c 2 --prompt "$FX/kling_3a_clean.txt" --refs "$FX/refs_ff_location.yaml" --case T9 --platform kling_3.0 || ok=1
  return $ok
}

t13() {
  echo "T13 Negativo Kling con 'no blur' y 10 ítems -> exit 0 con dos WARN R16 (P2, kling.md §6, SW30 R16)"
  local ok=0
  run t13 0 --prompt "$FX/prompt_GOOD_neg10.txt" --refs "$FX/refs_session.yaml" --case 3b --platform kling_3.0 --sports-broadcast || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_count "WARN R16" 2 || ok=1
  expect_has "10 items (> 8)" || ok=1
  expect_has "do not write 'no X'" || ok=1
  return $ok
}

t14() {
  echo "T14 El prompt GOOD del README del skill sigue pasando y el BAD sigue fallando (fixtures reconstruidos según references/README.md)"
  local ok=0
  run t14a 0 --prompt "$FX/prompt_GOOD.txt" --refs "$FX/refs_session.yaml" --case 3b --platform kling_3.0 --sports-broadcast || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_has "Delivery PERMITTED." || ok=1
  run t14b 1 --prompt "$FX/prompt_BAD.txt" --refs "$FX/refs_session.yaml" --case 3b --platform kling_3.0 --sports-broadcast --overrides "$FX/override_msg.txt" || ok=1
  expect_has "STATUS: FAIL" || ok=1
  expect_has "FAIL [P] 'athletic woman'" || ok=1
  expect_has "FAIL [O] 'white sneakers'" || ok=1
  expect_has "FAIL [PR] 'soccer ball'" || ok=1
  expect_has "FAIL [BANNED] 'cinematic'" || ok=1
  expect_has "FAIL [BANNED] '3D render'" || ok=1
  expect_has "FAIL [STRUCTURE] 'negative_prompt'" || ok=1
  expect_has "OK 'red performance tank'" || ok=1
  expect_has "OK 'L'" || ok=1
  expect_not "FAIL [L]" || ok=1
  # El conteo de palabras ya no bloquea (P1): el BAD falla por redundancia/vocabulario/estructura, no por longitud.
  expect_not "FAIL [STRUCTURE] 'word_count" || ok=1
  # También sin --platform (como lo invoca el SKILL.md original) el BAD sigue fallando y el GOOD pasando.
  run t14c 0 --prompt "$FX/prompt_GOOD.txt" --refs "$FX/refs_session.yaml" --case 3b --sports-broadcast || ok=1
  run t14d 1 --prompt "$FX/prompt_BAD.txt" --refs "$FX/refs_session.yaml" --case 3b --sports-broadcast || ok=1
  return $ok
}

t15() {
  echo "T15 --json intacto: la salida es JSON válido con las claves originales y linter_version"
  local ok=0
  run t15 0 --prompt "$FX/prompt_GOOD.txt" --refs "$FX/refs_session.yaml" --case 3b --platform kling_3.0 --sports-broadcast --json || ok=1
  python3 - "$LAST_OUT" <<'PY' || ok=1
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
orig = ["status","case_type","platform","word_count","word_budget","covered_categories",
        "sections_required","sections_present","sections_missing","violations",
        "overrides_accepted","warnings","suggestions"]
missing = [k for k in orig if k not in d]
assert not missing, f"faltan claves originales: {missing}"
assert d["status"] == "PASS", d["status"]
assert d["linter_version"].startswith("v1.2"), d["linter_version"]
assert d["ref_role"] == "ff", d["ref_role"]
print("    json ok:", len(d), "claves")
PY
  return $ok
}

t16() {
  echo "T16 Ref con S (estilo) y prompt sin palabras de estilo -> exit 0: la sección 'style' se dispensa (U13; antes S baneaba lo que la sección exigía)"
  local ok=0
  run t16a 0 --prompt "$FX/kling_3a_style_ref.txt" --refs "$FX/refs_ff_style.yaml" --case 3a --platform kling_3.0 || ok=1
  expect_has "STATUS: PASS" || ok=1
  expect_has "Section 'style' waived" || ok=1
  expect_not "MISSING style" || ok=1
  # Control: sin ref S el mismo prompt falla por la sección style ausente.
  run t16b 1 --prompt "$FX/kling_3a_style_ref.txt" --refs "$FX/refs_ff_location.yaml" --case 3a --platform kling_3.0 || ok=1
  expect_has "FAIL [SECTION] 'style'" || ok=1
  return $ok
}

# ---------------------------------------------------------------------------
TESTS=(t01 t02 t03 t04 t04b t05 t06 t06b t07 t08 t09 t10 t11 t12 t13 t14 t15 t16)
echo "Aurora linter parcheado — ${#TESTS[@]} pruebas"
echo "linter: $LINTER"
echo
for t in "${TESTS[@]}"; do
  if "$t"; then
    echo "    PASA"
    PASS=$((PASS + 1))
  else
    FAIL=$((FAIL + 1))
    FALLIDAS+=("$t")
  fi
done
echo
echo "Resultado: $PASS pasan, $FAIL fallan"
if [ "$FAIL" -gt 0 ]; then
  echo "Fallidas: ${FALLIDAS[*]}"
  exit 1
fi
exit 0
