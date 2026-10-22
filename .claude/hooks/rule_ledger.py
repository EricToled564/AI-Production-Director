#!/usr/bin/env python3
"""Force an explicit disposition for every extracted rule. Fail on any PENDING.

Specified in produccion-visual-sw30/SKILL.md:

    `rule_ledger.py` — obliga a que CADA regla aplicable tenga disposición
    explícita: CHECK (existe verificación) o NA (con razón escrita y auditable).
    Sale con código 1 si queda una sola PENDING.

    GATE DE COBERTURA: el builder corre `rule_ledger.py` antes de emitir; si no
    cierra en 100% dispuesto, no hay archivo de prompts.

A rule is PENDING until somebody writes down what happens to it. Silence is not
a disposition. That is the whole mechanism: a number nobody can round up.

Dispositions live in a JSON file keyed by rule id:

    {
      "a1b2c3d4e5f6": {"status": "CHECK", "by": "gate_image.py::R1"},
      "0f1e2d3c4b5a": {"status": "NA", "reason": "aplica solo a slides, no a spots"}
    }

CHECK requires `by` (what verifies it). NA requires `reason`. Both are audited.
A disposition whose id is no longer in the registry is reported as STALE: the
source text changed underneath it, so the claim no longer covers anything.

Usage:
    python3 rule_ledger.py --registry reg.json [reg2.json ...] --dispositions d.json
    python3 rule_ledger.py --registry reg.json --dispositions d.json --pending 20
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

VALID = ("CHECK", "NA")


def load_registry(paths: list[str]) -> dict[str, dict]:
    rules: dict[str, dict] = {}
    for p in paths:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        for rule in data.get("rules", []):
            rule.setdefault("skill", data.get("skill", "?"))
            rules[rule["id"]] = rule
    return rules


def main() -> int:
    ap = argparse.ArgumentParser(description="Coverage gate over an extracted rule registry")
    ap.add_argument("--registry", nargs="+", required=True)
    ap.add_argument("--dispositions", required=True)
    ap.add_argument("--pending", type=int, default=10, help="cuantas PENDING listar")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rules = load_registry(args.registry)

    disp_path = Path(args.dispositions)
    dispositions: dict[str, dict] = {}
    if disp_path.is_file():
        dispositions = json.loads(disp_path.read_text(encoding="utf-8"))

    checked: list[str] = []
    na: list[str] = []
    malformed: list[tuple[str, str]] = []
    pending: list[str] = []

    for rid in rules:
        d = dispositions.get(rid)
        if d is None:
            pending.append(rid)
            continue
        status = (d.get("status") or "").upper()
        if status not in VALID:
            malformed.append((rid, f"status invalido: {d.get('status')!r}"))
        elif status == "CHECK" and not d.get("by"):
            malformed.append((rid, "CHECK sin campo 'by' (que lo verifica)"))
        elif status == "NA" and not (d.get("reason") or "").strip():
            malformed.append((rid, "NA sin razon escrita"))
        elif status == "CHECK":
            checked.append(rid)
        else:
            na.append(rid)

    stale = [rid for rid in dispositions if rid not in rules]

    total = len(rules)
    disposed = len(checked) + len(na)
    pct = (disposed / total * 100) if total else 0.0

    if args.json:
        print(json.dumps({
            "total": total, "check": len(checked), "na": len(na),
            "pending": len(pending), "malformed": len(malformed),
            "stale": len(stale), "disposed_pct": round(pct, 1),
        }, indent=2))
    else:
        print("=" * 63)
        print("RULE LEDGER — gate de cobertura")
        print("=" * 63)
        print(f"  reglas en el registro    {total}")
        print(f"  CHECK  (verificadas)     {len(checked)}")
        print(f"  NA     (excluidas)       {len(na)}")
        print(f"  PENDING (sin disponer)   {len(pending)}")
        print(f"  MALFORMED                {len(malformed)}")
        print(f"  STALE (id ya no existe)  {len(stale)}")
        print(f"  dispuesto                {pct:.1f}%")
        print()

        for rid, why in malformed[: args.pending]:
            r = rules[rid]
            print(f"  MALFORMED {rid}  {why}")
            print(f"            {r['skill']}/{r['file']}:{r['line']}")

        if stale:
            print(f"  STALE: {', '.join(stale[:8])}"
                  + (" …" if len(stale) > 8 else ""))
            print("         el texto de origen cambio; la disposicion ya no cubre nada.")
            print()

        if pending:
            print(f"  Primeras {min(args.pending, len(pending))} PENDING:")
            for rid in pending[: args.pending]:
                r = rules[rid]
                print(f"    {rid}  [{','.join(r['markers'])}]")
                print(f"      {r['skill']}/{r['file']}:{r['line']}")
                print(f"      {r['text'][:150]}")
            if len(pending) > args.pending:
                print(f"    … y {len(pending) - args.pending} mas")
            print()

        if pending or malformed:
            print("  GATE CERRADO. No se emite mientras quede una sola PENDING.")
            print(f"  Dispon cada una en {disp_path} con CHECK+by o NA+reason.")
        else:
            print("  GATE ABIERTO. 100% dispuesto.")
        print("=" * 63)

    return 1 if (pending or malformed) else 0


if __name__ == "__main__":
    sys.exit(main())
