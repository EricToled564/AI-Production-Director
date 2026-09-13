#!/usr/bin/env python3
"""Validadores mecánicos: reglas del KB comprobadas por código en vez de por un auditor.

Por qué existe: el auditor es un modelo y falla. Sobre el mismo prompt, una tanda dio
cero fallas mientras otras dos encontraron ocho reales. Un validador corre igual
siempre, y puede correr ANTES de escribir el borrador, que es lo que produce
adherencia a la primera en vez de corrección por rondas.

Por qué no es peligroso: un validador mal escrito aprueba lo que debería fallar y no
duda. Contra eso, cada entrada trae casos de prueba —uno que debe pasar y uno que debe
fallar—, se autoprueba en cada corrida, y si su autoprueba no sale bien la regla vuelve
al auditor. Un validador roto no aprueba nada: se aparta.

El spec es declarativo a propósito. Eric tiene que poder leer qué comprueba cada regla
sin leer código.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / ".claude" / "rules" / "v3" / "validators"

UNRESOLVED = "UNRESOLVED"


def _target(art: dict, name: str):
    """Texto o estructura sobre la que se comprueba."""
    if name == "prompt":
        return art.get("prompt", "")
    if name == "prompt.main":                      # el cuerpo, sin el bloque Negative
        return re.split(r"(?im)^\s*negative\s*:", art.get("prompt", ""))[0]
    if name == "prompt.negative":
        parts = re.split(r"(?im)^\s*negative\s*:", art.get("prompt", ""))
        return parts[1] if len(parts) > 1 else ""
    if name == "notes":
        return art.get("notes", "")
    if name.startswith("slots."):
        cur = art.get("slots", {})
        for p in name.split(".")[1:]:
            cur = cur.get(p) if isinstance(cur, dict) else None
            if cur is None:
                return None
        return cur
    if name == "provenance":
        return json.dumps(art.get("provenance", {}), ensure_ascii=False)
    if name == "gates":                            # el informe de los gates mecánicos
        return json.dumps(art.get("gates", {}), ensure_ascii=False)
    if name == "stages":
        return art.get("stages", [])
    if name == "files":
        return art.get("files", [])
    return None


def _when(cond, art: dict) -> bool | None:
    """Precondición del caso; una lista son varias que deben cumplirse todas.
    None = no se puede decidir → UNRESOLVED."""
    if not cond:
        return True
    if isinstance(cond, list):
        res = [_when(c, art) for c in cond]
        if None in res:
            return None
        return all(res)
    cur = art.get("case", {})
    for p in cond["path"].split("."):
        cur = cur.get(p) if isinstance(cur, dict) else None
        if cur is None:
            return None
    if cur == "UNKNOWN":
        return None
    val = cond["value"]
    val = val if isinstance(val, list) else [val]
    return (cur in val) if cond.get("op", "in") == "in" else (cur not in val)


def evaluate(spec: dict, art: dict) -> tuple[str, str]:
    """(estado, razón). Estado UNRESOLVED cuando falta información: nunca PASS a ciegas."""
    ok = _when(spec.get("when"), art)
    if ok is None:
        w = spec["when"]
        rutas = ", ".join(c["path"] for c in w) if isinstance(w, list) else w["path"]
        return UNRESOLVED, f"el caso no declara {rutas}"
    if ok is False:
        return "NA", "no aplica a este caso por su precondición"

    op = spec["op"]
    if op in ("all", "any"):
        res = [evaluate(s, art) for s in spec["checks"]]
        estados = [r[0] for r in res]
        if UNRESOLVED in estados:
            return UNRESOLVED, "; ".join(r[1] for r in res if r[0] == UNRESOLVED)
        bien = [e in ("PASS", "NA") for e in estados]
        if (all(bien) if op == "all" else any(bien)):
            return "PASS", "; ".join(r[1] for r in res)[:300]
        return "FAIL", "; ".join(r[1] for r in res if r[0] == "FAIL")[:300]

    if op == "stage_pass":
        st = {s["name"]: s["status"] for s in _target(art, "stages")}
        if spec["stage"] not in st:
            return "FAIL", f"la etapa {spec['stage']} no se ejecutó"
        return ("PASS", f"etapa {spec['stage']} PASS") if st[spec["stage"]] == "PASS" else \
               ("FAIL", f"etapa {spec['stage']} en {st[spec['stage']]}")
    if op == "stages_ok":
        mal = [s["name"] for s in _target(art, "stages") if s["status"] not in ("PASS", "NA")]
        if not _target(art, "stages"):
            return UNRESOLVED, "el artefacto no trae etapas"
        return ("FAIL", f"etapas sin pasar: {', '.join(mal)}") if mal else \
               ("PASS", f"las {len(_target(art, 'stages'))} etapas del run pasaron o quedaron NA")
    if op == "file_exists":
        return ("PASS", f"{spec['file']} presente en el run") if spec["file"] in _target(art, "files") else \
               ("FAIL", f"falta {spec['file']} en el run")

    t = _target(art, spec["in"])
    if t is None:
        return UNRESOLVED, f"sin {spec['in']} en el artefacto"

    if op == "any_term":
        hit = [w for w in spec["terms"] if w.lower() in str(t).lower()]
        return ("PASS", f"{spec['in']} contiene {hit[0]!r}") if hit else \
               ("FAIL", f"{spec['in']} no contiene ninguno de: {', '.join(spec['terms'][:6])}")
    if op == "no_term":
        hit = [w for w in spec["terms"] if w.lower() in str(t).lower()]
        return ("FAIL", f"{spec['in']} contiene {hit[0]!r}, prohibido") if hit else \
               ("PASS", f"{spec['in']} sin términos prohibidos")
    if op == "regex":
        return ("PASS", f"{spec['in']} cumple /{spec['pattern']}/") if re.search(spec["pattern"], str(t), re.I | re.M) else \
               ("FAIL", spec.get("fail_reason") or f"{spec['in']} no cumple /{spec['pattern']}/")
    if op == "no_regex":
        m = re.search(spec["pattern"], str(t), re.I | re.M)
        return ("FAIL", (spec.get("fail_reason") or f"{spec['in']} coincide con /{spec['pattern']}/") + f": {m.group(0)!r}") if m else \
               ("PASS", f"{spec['in']} no coincide con /{spec['pattern']}/")
    return UNRESOLVED, f"operación desconocida: {op}"


def selftest(entry: dict) -> tuple[bool, str]:
    """Un validador sólo cuenta si demuestra que distingue. Sin los dos casos, no cuenta."""
    tests = entry.get("tests", {})
    if not tests.get("pass") or not tests.get("fail"):
        return False, "faltan casos de prueba (uno que pase y uno que falle)"
    for art in tests["pass"]:
        estado, razon = evaluate(entry["check"], art)
        if estado not in ("PASS", "NA"):
            return False, f"el caso que debía pasar dio {estado}: {razon}"
    for art in tests["fail"]:
        estado, razon = evaluate(entry["check"], art)
        if estado != "FAIL":
            return False, f"el caso que debía fallar dio {estado}: {razon}"
    return True, f"{len(tests['pass'])} pasan, {len(tests['fail'])} fallan, como debe ser"


def load(approved_only: bool = True) -> dict:
    """Validadores utilizables: aprobados por Eric y con autoprueba en verde."""
    out = {}
    for f in sorted(REGISTRY.glob("*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            e = json.loads(line)
            if approved_only and e.get("approved_by") != "user":
                continue
            ok, why = selftest(e)
            if ok:
                out[e["rule_id"]] = e
            else:
                e["_selftest_error"] = why
    return out


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="autoprueba del registro de validadores")
    ap.add_argument("--all", action="store_true", help="incluye los que Eric aún no aprueba")
    a = ap.parse_args()
    total = fallidos = 0
    for f in sorted(REGISTRY.glob("*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            e = json.loads(line)
            if not a.all and e.get("approved_by") != "user":
                continue
            total += 1
            ok, why = selftest(e)
            if not ok:
                fallidos += 1
                print(f"FAIL {e['rule_id']} ({e.get('source')}): {why}")
    print(f"validadores: {total}, autoprueba fallida: {fallidos}")
    return 1 if fallidos else 0


if __name__ == "__main__":
    raise SystemExit(main())
