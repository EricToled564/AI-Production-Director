#!/usr/bin/env python3
"""Extract every normative statement from a skill, mechanically.

Specified in produccion-visual-sw30/SKILL.md:

    `rule_registry.py` — relee los N archivos del skill y EXTRAE mecánicamente
    cada enunciado normativo. Si el skill cambia, el registro cambia solo.
    Mi interpretación deja de ser etapa.

The point is that no model decides what counts as a rule. A line is normative
because it carries a deontic marker, not because someone remembered it. The
markers are declared below and are auditable.

Ids are sha1(relative path + normalised text), so a rule keeps its id when
lines move around it, and changes id when its wording changes — which is the
behaviour a ledger needs.

Usage:
    python3 rule_registry.py --skill image --out registry.json
    python3 rule_registry.py --skill image --stats
    python3 rule_registry.py --list-skills
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

SKILLS_ROOT = Path(
    os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude" / "skills" / "synced")
)

# Deontic markers. Each one is a reason a line is normative; the marker is
# recorded on the rule so a reviewer can argue with the classification.
MARKERS: dict[str, re.Pattern] = {
    "prohibition": re.compile(
        r"\b(never|do not|don't|avoid|prohibit(?:ed|s)?|banned|forbidden|"
        r"no se|prohibido|nunca|jam[áa]s|"
        r"нельзя|не используй|никогда|запрещ)\w*\b",
        re.IGNORECASE,
    ),
    "obligation": re.compile(
        r"\b(must|shall|always|required|mandatory|ensure|has to|need to|"
        r"siempre|obligatorio|se debe|hay que|"
        r"должен|обязательн|всегда)\w*\b",
        re.IGNORECASE,
    ),
    "recommendation": re.compile(
        r"\b(should|prefer|recommend(?:ed)?|better to|use\b|"
        r"conviene|se recomienda|"
        r"лучше|используй|рекомендуется)\w*",
        re.IGNORECASE,
    ),
    "good_example": re.compile(r"✅"),
    "bad_example": re.compile(r"❌"),
    "numbered_rule": re.compile(r"^\s{0,3}\d{1,2}[.)]\s+\S"),
}

# Lines that are structure, not rules.
SKIP = (
    re.compile(r"^\s*$"),
    re.compile(r"^\s*(#{1,6})\s"),          # headings
    re.compile(r"^\s*[-*_]{3,}\s*$"),       # rules/hr
    re.compile(r"^\s*\|[\s:|-]+\|\s*$"),    # table separators
    re.compile(r"^\s*>\s*\*?Author"),       # attribution footers
    re.compile(r"^\s*\[!\["),               # badges
)

FENCE = re.compile(r"^\s*```")
FRONTMATTER = re.compile(r"^---\s*$")
# Metadatos del paquete, no enunciados normativos.
META = re.compile(
    r"^\s*(license|name|description|version|author|metadata|pipeline|allowed-tools|"
    r"compatibility)\s*:",
    re.IGNORECASE,
)
ATTRIBUTION = re.compile(r"(CC[ -]BY|attribution required|Serge Shima|t\.me/|©)", re.IGNORECASE)


def normalise(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^[-*+]\s+", "", text)
    text = re.sub(r"^\s*\d{1,2}[.)]\s+", "", text)
    return text.strip(" |")


def rule_id(rel: str, text: str) -> str:
    return hashlib.sha1(f"{rel}\x00{normalise(text).lower()}".encode()).hexdigest()[:12]


def extract_file(path: Path, root: Path) -> list[dict]:
    rel = str(path.relative_to(root))
    rules: list[dict] = []
    in_fence = False
    in_frontmatter = False

    lines = path.read_text(encoding="utf-8").splitlines()
    for lineno, raw in enumerate(lines, 1):
        # YAML frontmatter: metadata about the skill, not rules inside it.
        if lineno == 1 and FRONTMATTER.match(raw):
            in_frontmatter = True
            continue
        if in_frontmatter:
            if FRONTMATTER.match(raw):
                in_frontmatter = False
            continue

        if FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue  # prompt templates are examples, not statements about rules
        if any(p.match(raw) for p in SKIP):
            continue
        if META.match(raw) or ATTRIBUTION.search(raw):
            continue

        text = normalise(raw)
        if len(text) < 12:
            continue

        hits = [name for name, pat in MARKERS.items() if pat.search(raw)]
        if not hits:
            continue

        rules.append(
            {
                "id": rule_id(rel, text),
                "file": rel,
                "line": lineno,
                "markers": hits,
                "text": text[:400],
            }
        )
    return rules


def build(skill: str) -> tuple[Path, list[dict]]:
    roots = sorted(SKILLS_ROOT.glob(f"*/{skill}")) + sorted(
        SKILLS_ROOT.glob(f"*/*/{skill}")
    )
    roots = [r for r in roots if r.is_dir()]
    if not roots:
        raise SystemExit(f"rule_registry: skill '{skill}' not found under {SKILLS_ROOT}")
    root = roots[0]

    rules: list[dict] = []
    seen: set[str] = set()
    for md in sorted(root.rglob("*.md")):
        for rule in extract_file(md, root):
            if rule["id"] in seen:
                continue
            seen.add(rule["id"])
            rules.append(rule)
    return root, rules


def main() -> int:
    ap = argparse.ArgumentParser(description="Mechanical extraction of normative statements")
    ap.add_argument("--skill", default="image")
    ap.add_argument("--out")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--list-skills", action="store_true")
    args = ap.parse_args()

    if args.list_skills:
        for d in sorted(SKILLS_ROOT.glob("*/*")):
            if d.is_dir() and (d / "SKILL.md").is_file():
                print(d.name)
        return 0

    root, rules = build(args.skill)

    if args.out:
        Path(args.out).write_text(
            json.dumps(
                {"skill": args.skill, "root": str(root), "count": len(rules), "rules": rules},
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    if args.stats or not args.out:
        files = sorted({r["file"] for r in rules})
        by_marker: dict[str, int] = {}
        for r in rules:
            for m in r["markers"]:
                by_marker[m] = by_marker.get(m, 0) + 1
        print(f"skill:      {args.skill}")
        print(f"root:       {root}")
        print(f"archivos:   {len(list(root.rglob('*.md')))} .md leidos, {len(files)} con reglas")
        print(f"enunciados: {len(rules)}")
        print("por marcador:")
        for m, n in sorted(by_marker.items(), key=lambda kv: -kv[1]):
            print(f"  {m:16} {n}")
        if args.out:
            print(f"\nescrito en {args.out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
