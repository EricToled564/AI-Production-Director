#!/usr/bin/env python3
"""Exporta el registro de reglas como fuente para NotebookLM, y la pregunta canónica.

Método acordado:

    Paso 1  rule_registry.py  — tener TODAS. Extracción mecánica, nadie elige.
    Paso 2  NotebookLM        — decidir cuáles aplican al caso. Criterio externo.
    Paso 3  rule_answer_check.py — medir si la respuesta cubrió las TODAS.

Este script hace el 1->2: convierte el registro en un documento subible, con un id
estable por regla, y emite la pregunta a hacerle. Los ids son lo que permite el
paso 3: sin ellos la respuesta no es verificable, sólo creíble.

Uso:
    python3 rule_export.py --registry reg_*.json --out fuente.md --caso "maestro de rostro, Nano Banana Pro"
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load(paths: list[str]) -> list[dict]:
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
            rules.append(r)
    return rules


QUESTION = """Tengo abajo el catálogo completo y numerado de reglas de producción visual.
Cada regla tiene un id de 12 caracteres entre corchetes.

CASO: {caso}

Devuélveme, para ESTE caso, la clasificación de CADA UNA de las {n} reglas.
Formato exacto, una línea por regla, sin texto adicional:

    [id] APLICA
    [id] NO APLICA — <razón breve>

Requisitos:
- Deben aparecer las {n} reglas. Ninguna puede quedar fuera de la lista.
- No resumas ni agrupes. Una línea por id.
- Si una regla es ambigua para este caso, clasifícala APLICA y anota la duda.
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Exporta el registro como fuente para NotebookLM")
    ap.add_argument("--registry", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--caso", required=True)
    ap.add_argument("--pregunta", help="archivo donde escribir la pregunta canónica")
    args = ap.parse_args()

    rules = load(args.registry)
    if not rules:
        print("rule_export: el registro está vacío", file=sys.stderr)
        return 1

    lines = [
        "# Catálogo de reglas de producción visual",
        "",
        f"{len(rules)} reglas extraídas mecánicamente de los skills instalados.",
        "El id entre corchetes es estable y es la referencia para clasificar.",
        "",
    ]
    por_archivo: dict[str, list[dict]] = {}
    for r in rules:
        por_archivo.setdefault(f"{r['skill']}/{r['file']}", []).append(r)

    for path, rs in sorted(por_archivo.items()):
        lines += [f"## {path}", ""]
        for r in rs:
            lines.append(f"- [{r['id']}] (línea {r['line']}) {r['text']}")
        lines.append("")

    Path(args.out).write_text("\n".join(lines), encoding="utf-8")

    pregunta = QUESTION.format(caso=args.caso, n=len(rules))
    if args.pregunta:
        Path(args.pregunta).write_text(pregunta, encoding="utf-8")

    print(f"fuente:   {args.out}  ({len(rules)} reglas, {len(por_archivo)} archivos)")
    print(f"pregunta: {args.pregunta or '(abajo)'}")
    if not args.pregunta:
        print()
        print(pregunta)
    return 0


if __name__ == "__main__":
    sys.exit(main())
