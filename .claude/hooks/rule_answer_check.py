#!/usr/bin/env python3
"""Paso 3: medir si la selección externa cubrió TODAS las reglas.

No juzga si la selección fue acertada — eso es criterio, y el criterio ya no es mío.
Sólo mide cobertura: de las N reglas del registro, cuántas fueron clasificadas y
cuáles quedaron sin mencionar.

Es la pieza que convierte "confío en que es exhaustivo" en un número. Si sale
0 sin mencionar, la exhaustividad queda demostrada y deja de ser una opinión.
Si sale distinto de 0, las que faltan se listan por id y se vuelven a preguntar.

Uso:
    python3 rule_answer_check.py --registry reg_*.json --respuesta respuesta.txt
    python3 rule_answer_check.py --registry reg_*.json --respuesta r.txt --faltantes f.txt
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

LINE_RE = re.compile(
    r"\[?(?P<id>[0-9a-f]{12})\]?\s*[-—:]?\s*(?P<verdict>NO\s+APLICA|APLICA)\s*(?:[-—:]\s*(?P<reason>.*))?",
    re.IGNORECASE,
)


def load(paths: list[str]) -> dict[str, dict]:
    rules: dict[str, dict] = {}
    for p in paths:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        skill = data.get("skill", "?")
        for r in data.get("rules", []):
            r["skill"] = skill
            rules.setdefault(r["id"], r)
    return rules


def main() -> int:
    ap = argparse.ArgumentParser(description="Cobertura de una clasificación externa")
    ap.add_argument("--registry", nargs="+", required=True)
    ap.add_argument("--respuesta", required=True)
    ap.add_argument("--faltantes", help="archivo donde escribir los ids no mencionados")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rules = load(args.registry)
    text = Path(args.respuesta).read_text(encoding="utf-8")

    aplica: set[str] = set()
    no_aplica: set[str] = set()
    for m in LINE_RE.finditer(text):
        rid = m.group("id").lower()
        if m.group("verdict").upper().startswith("NO"):
            no_aplica.add(rid)
        else:
            aplica.add(rid)

    clasificadas = aplica | no_aplica
    faltantes = [r for rid, r in rules.items() if rid not in clasificadas]
    inventadas = sorted(clasificadas - set(rules))
    duplicadas = sorted(aplica & no_aplica)

    total = len(rules)
    cubiertas = total - len(faltantes)
    pct = (cubiertas / total * 100) if total else 0.0

    if args.json:
        print(json.dumps({
            "total": total, "aplica": len(aplica), "no_aplica": len(no_aplica),
            "sin_mencionar": len(faltantes), "ids_inexistentes": len(inventadas),
            "contradictorias": len(duplicadas), "cobertura_pct": round(pct, 1),
        }, indent=2))
    else:
        print("=" * 68)
        print("COBERTURA DE LA CLASIFICACION EXTERNA")
        print("=" * 68)
        print(f"  reglas en el registro       {total}")
        print(f"  clasificadas APLICA         {len(aplica)}")
        print(f"  clasificadas NO APLICA      {len(no_aplica)}")
        print(f"  SIN MENCIONAR               {len(faltantes)}")
        print(f"  ids que no existen          {len(inventadas)}")
        print(f"  clasificadas dos veces      {len(duplicadas)}")
        print(f"  cobertura                   {pct:.1f}%")
        print()
        if inventadas:
            print(f"  Ids inexistentes: {', '.join(inventadas[:8])}")
            print("    Vinieron en la respuesta pero no estan en el registro.")
            print()
        if duplicadas:
            print(f"  Contradictorias: {', '.join(duplicadas[:8])}")
            print("    Clasificadas como APLICA y NO APLICA a la vez.")
            print()
        if faltantes:
            print(f"  {len(faltantes)} reglas quedaron sin clasificar. Vuelve a preguntar")
            print("  por estos ids explicitamente:")
            for r in faltantes[:10]:
                print(f"    [{r['id']}] {r['skill']}/{r['file']}:{r['line']}")
                print(f"      {r['text'][:110]}")
            if len(faltantes) > 10:
                print(f"    … y {len(faltantes) - 10} mas")
        else:
            print("  100% clasificado. Exhaustividad demostrada, no supuesta.")
        print("=" * 68)

    if args.faltantes:
        Path(args.faltantes).write_text(
            "\n".join(f"[{r['id']}] {r['skill']}/{r['file']}:{r['line']} — {r['text']}"
                      for r in faltantes),
            encoding="utf-8",
        )
        print(f"\nfaltantes escritos en {args.faltantes}")

    return 1 if (faltantes or inventadas or duplicadas) else 0


if __name__ == "__main__":
    sys.exit(main())
