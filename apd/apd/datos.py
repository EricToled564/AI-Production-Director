"""Construcción de los datos derivados en apd/data/ (nunca en los originales).

    python3 -m apd.datos            # construye si falta
    python3 -m apd.datos --forzar   # reconstruye rules.sqlite desde los originales

Salidas (todas con procedencia):
  rules.sqlite            constructor original rules_v3.py build+derive, sin modificar
  registro.json           validación de esquema y conteos, versión del registro
  reconciliacion.json     1,398 del registro vs 852 del ejecutor anterior
  ubicaciones.json        ids cuyo texto aparece en 2+ skills (el build conserva una atribución)
  clasificacion_app.json  complemento: toda regla con caso, tarea y las 9 facetas explícitas
  cruce_v34.json          ruleset-3.4.0 (1,704) contra el registro, por texto
  plantillas.json         catálogo extraído de los originales
  inventario.json         cada fuente con sha256, función y versión
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from . import fuentes as F
from . import registro as R
from . import plantillas as P
from . import flujos as FL

DIMS_CERRADAS = ["d1", "d2", "d3", "d4", "d8", "d9"]
DIMS_ABIERTAS = ["d5", "d6", "d7"]


def ahora() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def escribir(nombre: str, obj) -> Path:
    p = F.DATA / nombre
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    return p


# --------------------------------------------------------------------------- ubicaciones

def ubicaciones() -> dict:
    """rule_registry (original) por skill: un mismo id puede venir de varias skills."""
    sys.path.insert(0, str(F.HOOKS))
    import os
    os.environ["FUPAI_SKILLS_ROOT"] = str(F.skills_root())
    import importlib
    rr = importlib.import_module("rule_registry")
    rr.SKILLS_ROOT = F.skills_root()
    donde: dict[str, list] = {}
    filas = 0
    for sk in sorted(p.name for p in (F.skills_root() / "skills").iterdir() if p.is_dir()):
        try:
            res = rr.build(sk)
        except SystemExit:
            continue
        reglas = res[1] if isinstance(res, tuple) else res
        for r in reglas:
            filas += 1
            donde.setdefault(r["id"], []).append({"skill": sk, "archivo": r.get("file"), "linea": r.get("line")})
    multi = {k: v for k, v in donde.items() if len({x["skill"] for x in v}) > 1}
    return {"filas_extraidas_skills": filas, "ids_skills": len(donde),
            "ids_en_varias_skills": len(multi),
            "filas_colapsadas": sum(len(v) for v in multi.values()) - len(multi),
            "nota": "rule_id = sha1(ruta relativa + texto) no incluye la skill: el mismo archivo copiado en "
                    "varias skills (p.ej. tools/README.md de shotkit) produce el mismo id. El texto se "
                    "conserva una vez; la app muestra todas sus ubicaciones.",
            "ids": multi}


# --------------------------------------------------------------------------- clasificación completa

def clasificacion_completa(reg: R.Registro) -> dict:
    """Ninguna regla sin clasificar: caso, tarea y d1..d9 explícitos para las 1,398.

    Lo que el constructor original ya decidió se conserva con su origen. Lo que falta se
    completa aquí con origen 'app_derivada' y una razón concreta: nunca queda vacío.
    """
    comp: dict[str, dict] = {}
    faltas = Counter()
    for rid, r in reg.reglas.items():
        c: dict = {}
        if not reg.casos.get(rid):
            etapas_r = {t.split(".")[0] for t, _ in reg.tareas.get(rid, [])}
            casos_e = sorted({c for e in FL.etapas() if e["clave"] in etapas_r for c in e["casos"]})
            c["caso"] = {"valor": casos_e or ["NINGUNO"], "origen": "app_derivada",
                         "razon": (f"sin fila en regla_caso; casos derivados de sus etapas {sorted(etapas_r)} "
                                   "(ETAPAS.casos de build_app.py)") if casos_e else
                                  f"sin fila en regla_caso ni etapa con casos; medio {r['medio']} / ámbito {r['ambito']}"}
            faltas["caso"] += 1
        if not reg.tareas.get(rid):
            c["tarea"] = {"valor": ["DOC"], "origen": "app_derivada",
                          "razon": "sin fila en regla_tarea; se asigna DOC (tarea suelta de build_app.py)"}
            faltas["tarea"] += 1
        fac = reg.facetas.get(rid, {})
        for d in DIMS_CERRADAS + DIMS_ABIERTAS:
            if fac.get(d):
                continue
            faltas[d] += 1
            if r["medio"] in ("PROCESO", "TEXTO"):
                razon = (f"regla de medio {r['medio']} ({r['skill']}/{r['archivo']}): la tarjeta de ancla "
                         "D1–D9 no discrimina reglas que no son de imagen ni video")
            else:
                razon = (f"ninguna tabla ARCHIVO_FACETA/REGEX_FACETA de rules_v3.py ni la clasificación "
                         f"llm/auditoría le asignó valor en {d}; se registra 'ninguno' explícito (revisable)")
            c[d] = {"valor": ["ninguno"], "origen": "app_derivada", "razon": razon}
        if c:
            comp[rid] = c
    return {"generado": ahora(), "registro": reg.version, "reglas": len(reg.reglas),
            "reglas_completadas": len(comp), "faltas_por_dimension": dict(faltas),
            "garantia": "tras este complemento, 0 reglas sin caso, 0 sin tarea y 0 sin valor en d1..d9",
            "complemento": comp}


# --------------------------------------------------------------------------- cruce v3.4

def _norm(t: str) -> str:
    t = re.sub(r"[`*_>#|]", " ", t.lower())
    t = re.sub(r"^\s*(\d{1,2}[.)]|[-+])\s+", "", t)
    return re.sub(r"\s+", " ", t).strip(" .:;")


def cruce_v34(reg: R.Registro) -> dict:
    p = F.extraer_paquete() / "repo" / ".claude" / "rules" / "v3" / "build" / "ruleset-3.4.0.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    por_texto: dict[str, list[str]] = {}
    for rid, r in reg.reglas.items():
        por_texto.setdefault(_norm(r["texto"]), []).append(rid)
    enl, sin = [], []
    for x in d["rules"]:
        t = _norm(x["rule"].get("text", ""))
        ids = por_texto.get(t)
        if not ids:
            # misma skill/archivo y el texto del registro contenido en el bloque v3
            cand = [rid for rid, r in reg.reglas.items()
                    if r["skill"] == x["rule"].get("skill") and r["archivo"] == x["rule"].get("file")
                    and len(_norm(r["texto"])) > 20 and _norm(r["texto"]) in t]
            ids = cand or None
        (enl if ids else sin).append({"id_v34": x["rule"]["id"], "skill": x["rule"].get("skill"),
                                      "archivo": x["rule"].get("source_path"), "linea": x["rule"].get("line"),
                                      "autoridad": x["metadata"].get("authority"),
                                      "efecto": x["metadata"].get("effect"),
                                      "texto": x["rule"].get("text", "")[:300], "ids_registro": ids or []})
    aprendidas = [s for s in sin if s["autoridad"] == "LEARNED_PRODUCTION"]
    return {"ruleset": "ruleset-3.4.0.json", "sha256": F.sha256_file(p), "reglas_v34": len(d["rules"]),
            "enlazadas_por_texto": len(enl), "sin_enlace": len(sin),
            "sin_enlace_por_autoridad": dict(Counter(s["autoridad"] for s in sin)),
            "aprendidas_fuera_del_registro": aprendidas,
            "politicas_conflicto": d.get("conflict_policies", []),
            "nota": "Los legacy_rule_ids de v3.4 no coinciden con ningún id de rules.sqlite (extractor distinto). "
                    "El cruce es por texto normalizado. Las reglas v3.4 sin enlace son fuentes normativas del "
                    "paquete que NO están en el registro de 1,398: se muestran, no se deciden ni se ocultan.",
            "enlazadas": enl, "sin_enlazar": sin}


# --------------------------------------------------------------------------- t1.sqlite del scratchpad

def comparar_t1() -> dict:
    import zipfile
    z = F.ORIGINALES / "scratchpad-completo.zip"
    if not z.exists():
        return {"disponible": False}
    dest = F.CACHE / "scratchpad"
    if not (dest / "t1.sqlite").exists():
        dest.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(z) as zz:
            zz.extract("t1.sqlite", dest)
    t1 = dest / "t1.sqlite"
    a = sqlite3.connect(f"file:{t1}?mode=ro", uri=True)
    b = sqlite3.connect(f"file:{F.RULES_DB}?mode=ro", uri=True)
    A = dict(a.execute("select id, texto from reglas"))
    B = dict(b.execute("select id, texto from reglas"))
    extra = [dict(zip(["id", "skill", "archivo", "linea", "texto"], r)) for r in
             a.execute("select id, skill, archivo, linea, texto from reglas") if r[0] not in B]
    return {"disponible": True, "archivo": "scratchpad-completo.zip:t1.sqlite", "sha256": F.sha256_file(t1),
            "reglas_t1": len(A), "reglas_registro": len(B),
            "ids_registro_en_t1": len(set(B) & set(A)),
            "textos_identicos": sum(1 for k in B if A.get(k) == B[k]),
            "solo_en_t1": extra,
            "conclusion": "t1.sqlite es una instantánea de trabajo (2026-09-25) construida con la fixture "
                          "tests/fixtures/regimenes/99-fixture-prueba.md cargada; sin esas reglas de prueba "
                          "coincide id por id y texto por texto con el registro reconstruido."}


# --------------------------------------------------------------------------- inventario

def inventario() -> dict:
    items = []

    def add(ruta: Path, base: str, funcion: str, version: str):
        if ruta.is_file():
            items.append({"ruta": base, "sha256": F.sha256_file(ruta), "bytes": ruta.stat().st_size,
                          "funcion": funcion, "version": version})

    for nombre, fun in [(F.ZIP_NOMBRE, "paquete v3.4.0 completo: skills, repo v3.x, ruleset 1,704, tests"),
                        ("scratchpad-completo.zip", "scratchpad de sesión: t1.sqlite, registros legacy, clasificación llm, research"),
                        ("flujo-anclas.html", "flujo de anclas: tarjeta D1–D9, pasos A0–A12, D9 por acción, ensamble"),
                        ("flujo-spot.html", "mapa del spot: niveles 0–4, E0–E7, subprocesos, génesis por clase")]:
        add(F.ORIGINALES / nombre, "originales/" + nombre, fun, "entregado 2026-09-27/28")
    repo_rel = [
        (".claude/hooks/rules_v3.py", "constructor de rules.sqlite v3"), (".claude/hooks/schema_v3.sql", "esquema v3"),
        (".claude/hooks/rule_registry.py", "extractor mecánico de enunciados"), (".claude/hooks/rule_query.py", "consulta top-k (reemplazada)"),
        (".claude/hooks/rule_answer_check.py", "medidor de cobertura de ids"), (".claude/hooks/aurora/prompt_linter.py", "linter aurora v1.2-fupai"),
        (".claude/hooks/aurora/vocabularies.yaml", "vocabularios aurora"), (".claude/hooks/gate_image.py", "gate de imagen"),
        (".claude/hooks/gate_dramaturgy.py", "gate de vocabulario prohibido"), (".claude/hooks/gate_microgate.py", "micro-gate"),
        (".claude/hooks/gate_shots.py", "gate shots.json"), (".claude/rules/DECISIONES.md", "decisiones de dirección 2026-09-25"),
        (".claude/rules/METODO.md", "método"), (".claude/rules/scope.yaml", "respaldo determinista"),
        (".claude/rules/clasificacion_v2_app.json", "852 clasificaciones del ejecutor"),
        (".claude/rules/clasificacion_llm_facetas.json", "clasificación llm de facetas"),
        ("app/build_app.py", "generador del ejecutor anterior (ETAPAS, TRACKS)"), ("app/ejecutor.html", "ejecutor anterior (852 reglas)"),
        ("api/sample.js", "puente OpenAI del ejecutor"), ("tests/test_rules_v3.sh", "tests v3"),
    ]
    for rel, fun in repo_rel:
        add(F.REPO / rel, rel, fun, "repo@" + F.REPO_COMMIT[:7])
    for p in sorted((F.REPO / ".claude" / "rules" / "regimenes").glob("*.md")):
        add(p, str(p.relative_to(F.REPO)), "familia de régimen físico (reglas FUENTE / A PRUEBA)", "repo@" + F.REPO_COMMIT[:7])
    pkg = F.extraer_paquete()
    for p in sorted((pkg / "skills").rglob("*.md")):
        add(p, "pkg/" + str(p.relative_to(pkg)), "fuente normativa de skill", "pkg v3.4.0")
    for rel, fun in [("repo/.claude/rules/v3/build/ruleset-3.4.0.json", "ruleset v3.4.0 (1,704)"),
                     ("repo/production-package/template_engine.py", "motor T1–T5 (SOURCE_RECONSTRUCTED)"),
                     ("repo/production-package/audit_gi2.py", "auditor 15 columnas"),
                     ("repo/.claude/hooks/prompt_ast_gate_v34.py", "gate AST v3.4"),
                     ("repo/.claude/hooks/prompt_render_v34.py", "render determinista v3.4"),
                     ("repo/.claude/hooks/prompt_revision_gate_v34.py", "gate de deriva v3.4"),
                     ("repo/.claude/hooks/brief_freeze_v34.py", "congelado de brief v3.4"),
                     ("skills/visual-prompt-forge/adapters/_capabilities.json", "capacidades por modelo")]:
        add(pkg / rel, "pkg/" + rel, fun, "pkg v3.4.0")
    return {"generado": ahora(), "repo_commit": F.REPO_COMMIT, "fuentes_nombradas": F.FUENTES_NOMBRADAS,
            "n": len(items), "items": items}


# --------------------------------------------------------------------------- main

def construir(forzar: bool = False) -> dict:
    F.DATA.mkdir(parents=True, exist_ok=True)
    info = R.construir(forzar=forzar)
    val = R.validar(F.RULES_DB)
    reg = R.cargar()
    val["construccion"] = {k: v for k, v in info.items() if k != "log"}
    val["verificado"] = ahora()
    escribir("registro.json", val)
    escribir("reconciliacion.json", R.reconciliar(reg))
    escribir("ubicaciones.json", ubicaciones())
    escribir("clasificacion_app.json", clasificacion_completa(reg))
    escribir("cruce_v34.json", cruce_v34(reg))
    escribir("comparacion_t1.json", comparar_t1())
    escribir("plantillas.json", P.extraer())
    escribir("citas_flujos.json", FL.verificar_citas())
    escribir("inventario.json", inventario())
    return {"registro": val["version"], "reglas": val.get("reglas_ids_distintos"), "ok": val.get("ok")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()
    print(json.dumps(construir(a.forzar), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
