#!/usr/bin/env python3
"""Paso 2 del método: decidir qué reglas aplican a ESTE caso.

    Paso 1  rule_registry.py  — tener TODAS. Extracción mecánica, nadie elige.
    Paso 2  rule_scope.py     — filtrar por caso. Escrito y auditable.
    Paso 3  auditoría externa — pedir a un segundo criterio qué se excluyó mal.

La propiedad que hace útil al paso 2 no es que acierte: es que **no puede callar**.
Una regla que ninguna línea de scope.yaml toca queda SIN DECIDIR, y una sola sin
decidir cierra el gate. El filtro no puede omitir por descuido, solo por escrito.

Eso es también lo que separa este paso de preguntarle a un modelo cuáles aplican:
un modelo devuelve una selección y no sabe decirte qué se le olvidó.

Uso:
    python3 rule_scope.py --caso imagen --registry reg_*.json
    python3 rule_scope.py --caso imagen --tipo T1 --registry reg_*.json --exclusiones out.md
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: falta pyyaml. pip install pyyaml --break-system-packages", file=sys.stderr)
    sys.exit(2)

DEFAULT_SCOPE = Path(__file__).resolve().parent.parent / "rules" / "scope.yaml"


def load_registry(paths: list[str]) -> list[dict]:
    rules: list[dict] = []
    seen: set[str] = set()
    for p in paths:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        skill = data.get("skill", "?")
        for r in data.get("rules", []):
            if r["id"] in seen:
                continue
            seen.add(r["id"])
            r["skill"] = skill
            r["path"] = f"{skill}/{r['file']}"
            rules.append(r)
    return rules


def matches(rule: dict, m: dict) -> bool:
    if "file" in m and not fnmatch.fnmatch(rule["path"], m["file"]):
        return False
    if "text" in m and not re.search(m["text"], rule["text"]):
        return False
    if "marker" in m and m["marker"] not in rule["markers"]:
        return False
    return bool(m)


def main() -> int:
    ap = argparse.ArgumentParser(description="Filtro de alcance por caso")
    ap.add_argument("--caso", required=True)
    ap.add_argument("--tipo")
    ap.add_argument("--registry", nargs="+", required=True)
    ap.add_argument("--scope", default=str(DEFAULT_SCOPE))
    ap.add_argument("--exclusiones", help="escribe el informe de exclusiones para auditar")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.scope).read_text(encoding="utf-8"))
    caso = args.caso

    if args.tipo:
        tipo = (cfg.get("tipos") or {}).get(args.tipo)
        if not tipo:
            print(f"rule_scope: tipo desconocido {args.tipo!r}", file=sys.stderr)
            return 2
        caso = tipo["caso"]

    spec = (cfg.get("casos") or {}).get(caso)
    if not spec:
        disponibles = ", ".join((cfg.get("casos") or {}).keys())
        print(f"rule_scope: caso {caso!r} no definido. Hay: {disponibles}", file=sys.stderr)
        return 2

    rules = load_registry(args.registry)
    entries = spec.get("reglas") or []

    aplican: list[dict] = []
    na: list[tuple[dict, str]] = []
    sin_decidir: list[dict] = []

    for rule in rules:
        hit = next((e for e in entries if matches(rule, e.get("match") or {})), None)
        if hit is None:
            sin_decidir.append(rule)
        elif (hit.get("status") or "").upper() == "APLICA":
            aplican.append(rule)
        else:
            na.append((rule, " ".join((hit.get("reason") or "sin razon").split())))

    por_razon: dict[str, int] = {}
    for _, reason in na:
        por_razon[reason] = por_razon.get(reason, 0) + 1

    if args.json:
        print(json.dumps({
            "caso": caso, "tipo": args.tipo, "total": len(rules),
            "aplican": len(aplican), "na": len(na), "sin_decidir": len(sin_decidir),
        }, ensure_ascii=False, indent=2))
    else:
        print("=" * 70)
        print(f"ALCANCE DEL CASO: {caso}" + (f" / {args.tipo}" if args.tipo else ""))
        print(f"  {spec.get('descripcion', '')}")
        print("=" * 70)
        print(f"  Paso 1 · reglas extraidas de la fuente   {len(rules)}")
        print(f"  Paso 2 · APLICAN a este caso             {len(aplican)}")
        print(f"           NO APLICAN (con razon escrita)  {len(na)}")
        print(f"           SIN DECIDIR                     {len(sin_decidir)}")
        print()
        print("  APLICAN, por archivo:")
        por_archivo: dict[str, int] = {}
        for r in aplican:
            por_archivo[r["path"]] = por_archivo.get(r["path"], 0) + 1
        for path, n in sorted(por_archivo.items(), key=lambda kv: -kv[1])[:12]:
            print(f"    {n:>4}  {path}")
        if len(por_archivo) > 12:
            print(f"          … y {len(por_archivo) - 12} archivos mas")
        print()
        print("  EXCLUIDAS, por razon (esto es lo que se audita):")
        for reason, n in sorted(por_razon.items(), key=lambda kv: -kv[1]):
            print(f"    {n:>4}  {reason[:110]}")
        print()
        if sin_decidir:
            print(f"  GATE CERRADO — {len(sin_decidir)} reglas sin decidir.")
            print("  Ninguna linea de scope.yaml las toca. Agrega la linea que")
            print("  las incluya o las excluya con razon. No se entrega asi.")
            for r in sin_decidir[:6]:
                print(f"    {r['id']}  {r['path']}:{r['line']}")
                print(f"      {r['text'][:110]}")
            if len(sin_decidir) > 6:
                print(f"    … y {len(sin_decidir) - 6} mas")
        else:
            print("  GATE ABIERTO — 0 sin decidir. Cada regla tiene disposicion escrita.")
        print("=" * 70)

    if args.exclusiones:
        out = [
            f"# Exclusiones del caso `{caso}`" + (f" / `{args.tipo}`" if args.tipo else ""),
            "",
            "Lista para auditar con un segundo criterio (paso 3). La pregunta es:",
            "**de estas reglas excluidas, ¿cuál debería aplicar a este caso?**",
            "",
            f"- Reglas totales en la fuente: {len(rules)}",
            f"- Aplican: {len(aplican)} · Excluidas: {len(na)} · Sin decidir: {len(sin_decidir)}",
            "",
        ]
        for reason, n in sorted(por_razon.items(), key=lambda kv: -kv[1]):
            out += [f"## Excluidas por: {reason}", f"", f"{n} reglas.", ""]
            for rule, rsn in na:
                if rsn == reason:
                    out.append(f"- `{rule['path']}:{rule['line']}` — {rule['text'][:180]}")
            out.append("")
        Path(args.exclusiones).write_text("\n".join(out), encoding="utf-8")
        print(f"\ninforme de exclusiones escrito en {args.exclusiones}")

    return 1 if sin_decidir else 0


if __name__ == "__main__":
    sys.exit(main())
