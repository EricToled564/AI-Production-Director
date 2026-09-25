#!/usr/bin/env bash
# Prueba end-to-end de la base de reglas v3. Sale 0 sólo si todo lo afirmado se cumple.
#
#   bash tests/test_rules_v3.sh
#
# Construye la base en un directorio temporal (con el fixture de régimen de tests/),
# verifica la importación de la clasificación v2 (852 contabilizadas: importadas +
# huérfanas visibles), verifica que ninguna regla queda sin caso NI tarea, y corre
# tres briefs mostrando total / incluidas / sin faceta de cada uno.
#
# Intérpretes: los pasos deterministas corren con python3 del sistema. `embed` y el
# coseno del ranking necesitan fastembed + numpy; se buscan en $RULES_V3_PY, luego en
# .venv del repo, luego en el venv del scratchpad de la sesión. Si no hay ninguno, el
# embed se omite (se dice) y los briefs corren sólo con BM25: la prueba sigue siendo
# válida porque nada de lo afirmado depende del vector.

set -uo pipefail
bash -n "${BASH_SOURCE[0]}" || { echo "test_rules_v3.sh tiene un error de sintaxis"; exit 2; }

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOKS="$REPO/.claude/hooks"
FIXTURE="$REPO/tests/fixtures/regimenes"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
DB="$TMP/rules.sqlite"
PASS=0
FAIL=0

check() { # check <nombre> <esperado> <obtenido>
  if [[ "$2" == "$3" ]]; then
    printf '  \033[32mPASS\033[0m  %-58s %s\n' "$1" "$3"; PASS=$((PASS + 1))
  else
    printf '  \033[31mFAIL\033[0m  %-58s %s (esperado %s)\n' "$1" "$3" "$2"; FAIL=$((FAIL + 1))
  fi
}
ge() { # ge <nombre> <minimo> <obtenido>
  if [[ "$3" -ge "$2" ]]; then
    printf '  \033[32mPASS\033[0m  %-58s %s\n' "$1" "$3"; PASS=$((PASS + 1))
  else
    printf '  \033[31mFAIL\033[0m  %-58s %s (esperado >= %s)\n' "$1" "$3" "$2"; FAIL=$((FAIL + 1))
  fi
}
q() { python3 -c 'import sqlite3,sys; print(sqlite3.connect(sys.argv[1]).execute(sys.argv[2]).fetchone()[0])' "$DB" "$1"; }

# intérprete con fastembed + numpy, si lo hay
PYV="${RULES_V3_PY:-}"
if [[ -z "$PYV" && -x "$REPO/.venv/bin/python" ]]; then PYV="$REPO/.venv/bin/python"; fi
if [[ -z "$PYV" ]]; then
  for cand in /tmp/claude-0/*/*/scratchpad/venv/bin/python; do
    [[ -x "$cand" ]] && PYV="$cand" && break
  done
fi
if [[ -z "$PYV" ]] && python3 -c 'import fastembed, numpy' 2>/dev/null; then PYV="python3"; fi
if [[ -n "$PYV" ]] && ! "$PYV" -c 'import fastembed, numpy' 2>/dev/null; then PYV=""; fi
if [[ -z "$PYV" ]]; then
  echo "aviso: sin intérprete con fastembed+numpy; embed omitido, ranking sólo BM25"
fi

echo
echo "=== 1. build (13 skills + regímenes + fixture) ==="
python3 "$HOOKS/rules_v3.py" --db "$DB" build --root "$FIXTURE" >"$TMP/build.log" 2>&1
check "build sale 0" 0 $?
sed 's/^/      /' "$TMP/build.log" | grep -E 'reglas:|import-app|huérfana|fts:' | head -8
TOTAL=$(q 'SELECT COUNT(*) FROM reglas')
ge "reglas en la base" 1000 "$TOTAL"
check "13 skills + regimenes registrados" 14 "$(q 'SELECT COUNT(*) FROM skills')"
check "22 casos" 22 "$(q 'SELECT COUNT(*) FROM casos')"
check "50 tareas (45 subprocesos + 5 sueltas)" 50 "$(q 'SELECT COUNT(*) FROM tareas')"
check "reglas_fts tiene todas las reglas" "$TOTAL" "$(q 'SELECT COUNT(*) FROM reglas_fts')"
check "descartes registrados (índices, cabeceras, sin etiqueta)" 1 "$(q 'SELECT COUNT(*) > 0 FROM descartes')"

echo
echo "=== 2. importación de la clasificación v2 (852 reglas) ==="
IMPORTADAS=$(q "SELECT COUNT(DISTINCT regla_id) FROM regla_caso WHERE auditor='app_v2'")
HUERFANAS=$(q "SELECT COUNT(DISTINCT regla_id) FROM importacion_huerfana")
check "852/852 contabilizadas (importadas + huérfanas visibles)" 852 $((IMPORTADAS + HUERFANAS))
check "huérfanas: sólo las 2 líneas de índice excluidas por diseño" 2 "$HUERFANAS"
check "huérfanas con razón id_no_en_registro" 2 "$(q "SELECT COUNT(*) FROM importacion_huerfana WHERE razon='id_no_en_registro'")"
check "origen conservado: archivo/regla/auditoria presentes" 3 "$(q "SELECT COUNT(DISTINCT origen) FROM regla_caso WHERE auditor='app_v2'")"

echo
echo "=== 3. fixture de régimen (tests/fixtures/regimenes) ==="
FX="archivo='99-fixture-prueba.md'"
check "reglas del fixture extraídas" 7 "$(q "SELECT COUNT(*) FROM reglas WHERE skill='regimenes' AND $FX")"
check "estado A_PRUEBA" 3 "$(q "SELECT COUNT(*) FROM reglas WHERE $FX AND estado='A_PRUEBA'")"
check "estado CAMPO" 1 "$(q "SELECT COUNT(*) FROM reglas WHERE $FX AND estado='CAMPO'")"
check "estado CANONICA (prioridad 1)" 1 "$(q "SELECT COUNT(*) FROM reglas WHERE $FX AND estado='CANONICA' AND prioridad=1")"
check "estado REFUTADA (prioridad 5)" 1 "$(q "SELECT COUNT(*) FROM reglas WHERE $FX AND estado='REFUTADA' AND prioridad=5")"
check "FUENTE -> CANONICA_SKILL con fuente guardada" 1 "$(q "SELECT COUNT(*) FROM reglas WHERE $FX AND estado='CANONICA_SKILL' AND fuente LIKE 'FUENTE:%'")"
check "línea sin etiqueta descartada y contada" 1 "$(q "SELECT COUNT(*) FROM descartes WHERE $FX AND razon='sin_etiqueta'")"
check "línea de índice descartada y contada" 1 "$(q "SELECT COUNT(*) FROM descartes WHERE $FX AND razon='indice'")"
check "cabecera de tabla descartada y contada" 1 "$(q "SELECT COUNT(*) FROM descartes WHERE $FX AND razon='cabecera_tabla'")"
CANON=$(q "SELECT id FROM reglas WHERE $FX AND estado='CANONICA'")
check "faceta heredada del frontmatter (d2=C_movimiento, origen archivo)" 1 "$(q "SELECT COUNT(*) FROM regla_faceta WHERE regla_id='$CANON' AND dimension='d2' AND valor='C_movimiento' AND origen='archivo'")"
check "prefijo {d9: high} sobrescribe d9 (origen manual)" "high" "$(q "SELECT GROUP_CONCAT(valor) FROM regla_faceta WHERE regla_id='$CANON' AND dimension='d9'")"
check "casos del frontmatter aplicados (T3, OBJ)" 2 "$(q "SELECT COUNT(*) FROM regla_caso WHERE regla_id='$CANON' AND caso IN ('T3','OBJ')")"
check "tareas del frontmatter aplicadas (E5.2, E6.2), origen directa" 2 "$(q "SELECT COUNT(*) FROM regla_tarea WHERE regla_id='$CANON' AND origen='directa'")"
# el id no depende de la etiqueta ni del prefijo de facetas
IDCALC=$(python3 - "$HOOKS" <<'PY'
import sys; sys.path.insert(0, sys.argv[1]); import rule_registry as rr
print(rr.rule_id("99-fixture-prueba.md", "Desde arriba, el spray debe leerse como un abanico, nunca como niebla."))
PY
)
check "id calculado sin etiqueta ni prefijo coincide" "$CANON" "$IDCALC"

echo
echo "=== 4. derive + check ==="
python3 "$HOOKS/rules_v3.py" --db "$DB" derive >"$TMP/derive.log" 2>&1
check "derive sale 0" 0 $?
grep -E '^derive:' "$TMP/derive.log" | sed 's/^/      /'
python3 "$HOOKS/rules_v3.py" --db "$DB" check >"$TMP/check.log" 2>&1
check "check sale 0 (0 reglas sin caso NI tarea)" 0 $?
check "v_sin_caso_ni_tarea vacía" 0 "$(q 'SELECT COUNT(*) FROM v_sin_caso_ni_tarea')"
check "toda regla tiene tarea" "$TOTAL" "$(q 'SELECT COUNT(DISTINCT regla_id) FROM regla_tarea')"
check "kling.md -> d8 kling por ruta" 1 "$(q "SELECT COUNT(*) > 0 FROM regla_faceta rf JOIN reglas r ON r.id=rf.regla_id WHERE r.skill='video' AND r.archivo='references/kling.md' AND rf.dimension='d8' AND rf.valor='kling' AND rf.origen='archivo'")"
check "race-and-speed.md -> d4 race + d2 C_movimiento" 2 "$(q "SELECT COUNT(DISTINCT rf.dimension) FROM regla_faceta rf JOIN reglas r ON r.id=rf.regla_id WHERE r.archivo='references/race-and-speed.md' AND ((rf.dimension='d4' AND rf.valor='race') OR (rf.dimension='d2' AND rf.valor='C_movimiento'))")"
check "ecommerce.md -> PROD" 1 "$(q "SELECT COUNT(*) > 0 FROM regla_caso rc JOIN reglas r ON r.id=rc.regla_id WHERE r.archivo='references/patterns/ecommerce.md' AND rc.caso='PROD'")"
check "v_sin_faceta reporta por skill (nada se calla)" 1 "$(q 'SELECT COUNT(*) > 0 FROM v_sin_faceta')"
sed -n '/v_sin_faceta por skill/,/total en v_sin_faceta/p' "$TMP/check.log" | sed 's/^/      /'

echo
echo "=== 5. embed ==="
if [[ -n "$PYV" ]]; then
  "$PYV" "$HOOKS/rules_v3.py" --db "$DB" embed >"$TMP/embed.log" 2>&1
  check "embed sale 0" 0 $?
  grep -E '^embed:' "$TMP/embed.log" | sed 's/^/      /'
  check "una regla, un vector" "$TOTAL" "$(q 'SELECT COUNT(*) FROM embeddings')"
  check "dim 1024, float32 normalizado" 1 "$(q 'SELECT dim=1024 AND LENGTH(vector)=4096 FROM embeddings LIMIT 1')"
  ge "prototipos (casos + tareas + valores de faceta)" 100 "$(q 'SELECT COUNT(*) FROM prototipos')"
  QPY="$PYV"
else
  echo "  SKIP  embed (sin fastembed)"
  QPY=python3
fi

echo
echo "=== 5b. classify + auditoría (capas 2 y 3, decisión 9) ==="
if [[ -n "$PYV" ]]; then
  ANTES_CASO=$(q 'SELECT COUNT(DISTINCT regla_id) FROM regla_caso')
  ANTES_FACETA=$(q 'SELECT COUNT(DISTINCT regla_id||dimension) FROM regla_faceta')
  "$PYV" "$HOOKS/rules_v3.py" --db "$DB" classify >"$TMP/classify.log" 2>&1
  check "classify sale 0" 0 $?
  grep -E '^classify:|regla_caso|regla_faceta' "$TMP/classify.log" | sed 's/^/      /'
  DESPUES_CASO=$(q 'SELECT COUNT(DISTINCT regla_id) FROM regla_caso')
  DESPUES_FACETA=$(q 'SELECT COUNT(DISTINCT regla_id||dimension) FROM regla_faceta')
  check "classify solo suma (nunca quita) filas de regla_caso" 1 "$((DESPUES_CASO >= ANTES_CASO))"
  check "classify solo suma (nunca quita) filas de regla_faceta" 1 "$((DESPUES_FACETA >= ANTES_FACETA))"
  check "0 filas de vector con confianza por debajo del umbral 0.80" 0 "$(q "SELECT COUNT(*) FROM regla_caso WHERE origen='vector' AND confianza<0.80")"

  XLSX="$TMP/auditoria.xlsx"
  "$PYV" "$HOOKS/rules_v3.py" --db "$DB" audit-export --xlsx "$XLSX" >"$TMP/audit_export.log" 2>&1
  check "audit-export sale 0" 0 $?
  check "auditoria.xlsx escrito" 1 "$([[ -f "$XLSX" ]] && echo 1 || echo 0)"
  check "audit-export tiene hoja 'caso' + una por faceta cerrada (d1,d2,d3,d4,d8,d9)" 7 \
    "$("$PYV" -c "import openpyxl; print(len(openpyxl.load_workbook('$XLSX', read_only=True).sheetnames))")"

  # round-trip: corrige a mano una fila de la hoja 'caso' y reimporta
  RID_PRUEBA=$("$PYV" -c "
import openpyxl
wb = openpyxl.load_workbook('$XLSX')
ws = wb['caso']
row = next(ws.iter_rows(min_row=2, max_row=2), None)
if row is None:
    print('')
else:
    row[8].value = 'NINGUNO'
    row[9].value = 'prueba automatica test_rules_v3.sh'
    wb.save('$XLSX')
    print(row[0].value)
")
  if [[ -n "$RID_PRUEBA" ]]; then
    "$PYV" "$HOOKS/rules_v3.py" --db "$DB" audit-import --xlsx "$XLSX" --auditor test_ci >"$TMP/audit_import.log" 2>&1
    check "audit-import sale 0" 0 $?
    check "la corrección queda con origen=auditoria" 1 \
      "$(q "SELECT COUNT(*) FROM regla_caso WHERE regla_id='$RID_PRUEBA' AND caso='NINGUNO' AND origen='auditoria' AND auditor='test_ci'")"
    check "la corrección queda registrada en auditorias" 1 \
      "$(q "SELECT COUNT(*) > 0 FROM auditorias WHERE regla_id='$RID_PRUEBA' AND auditor='test_ci'")"
  else
    echo "  SKIP  round-trip de audit-import (hoja 'caso' vacía: nada pendiente de auditar)"
  fi
else
  echo "  SKIP  classify + auditoría (sin fastembed: classify necesita embeddings y prototipos)"
fi

echo
echo "=== 6. tres briefs ==="
BRIEFS=(
  "maestro de rostro T1 para Nano Banana Pro, documental"
  "clip Kling 3.0 de un auto de carreras, keyframe de inicio"
  "dos personas conversando en un café, cuadro con referencias, GPT Image 2"
)
ESPERADO_CASO=("T1" "CLIP" "T4")
ESPERADO_D8=("nano-banana-pro" "kling" "gpt-image-2")
for i in 0 1 2; do
  b="${BRIEFS[$i]}"
  "$QPY" "$HOOKS/rule_query.py" --db "$DB" --brief "$b" --json >"$TMP/q$i.json" 2>"$TMP/q$i.err"
  rc=$?
  check "brief $((i + 1)) sale 0" 0 "$rc"
  python3 - "$TMP/q$i.json" "${ESPERADO_CASO[$i]}" "${ESPERADO_D8[$i]}" <<'PY'
import json, sys
r = json.load(open(sys.argv[1]))
fc = r["facetas_confirmadas"]
ok_caso = sys.argv[2] in fc.get("caso", [])
ok_d8 = sys.argv[3] in fc.get("d8", [])
print(f"      brief: {r['brief']}")
print(f"      facetas: " + " · ".join(f"{k}={','.join(v)}" for k, v in fc.items()))
print(f"      total del filtro: {r['total_filtro']} · incluidas: {r['incluidas']} · fuera por presupuesto: {r['fuera_presupuesto']} · sin faceta: {r['sin_faceta_total']} · ranking {'híbrido' if r['vectorial'] else 'BM25'}")
sys.exit(0 if (ok_caso and ok_d8 and r["total_filtro"] > 0 and r["incluidas"] > 0) else 1)
PY
  check "brief $((i + 1)): caso ${ESPERADO_CASO[$i]} y d8 ${ESPERADO_D8[$i]} detectados, resultado no vacío" 0 $?
done
check "consultas registradas en briefs" 3 "$(q 'SELECT COUNT(*) FROM briefs')"
ge "brief_regla con filas" 100 "$(q 'SELECT COUNT(*) FROM brief_regla')"

echo
echo "=== 7. stats ==="
python3 "$HOOKS/rules_v3.py" --db "$DB" stats >"$TMP/stats.log" 2>&1
check "stats sale 0" 0 $?
head -8 "$TMP/stats.log" | sed 's/^/      /'

echo
echo "PASS $PASS · FAIL $FAIL"
[[ "$FAIL" -eq 0 ]]
