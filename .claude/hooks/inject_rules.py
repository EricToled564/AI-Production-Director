#!/usr/bin/env python3
"""UserPromptSubmit hook: put the mandatory rules in context before Claude chooses.

Every other gate in this directory inspects output. None of them touch the real
failure: which files get read. While reading is a choice the model makes, it can
keep choosing to skip the part that matters.

This hook removes the choice. On any prompt that touches visual production it
injects the governing files verbatim — not a summary, not a grep, which is what
produccion-visual-sw30/SKILL.md demands:

    "Exhaustiva" significa: leídos COMPLETOS todos los archivos del skill
    aplicables al caso (SKILL.md indica el orden obligatorio), no fragmentos ni grep.

The text is in context whether or not the model decided to look it up.

Injection is capped: MANDATORY files always go in whole; CONDITIONAL ones go in
whole only while the budget lasts, and anything dropped is named explicitly so a
silent omission is impossible.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

SKILLS_ROOT = Path(
    os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude" / "skills" / "synced")
)
BUDGET_CHARS = int(os.environ.get("FUPAI_INJECT_BUDGET", "60000"))

TRIGGERS = re.compile(
    r"\b(prompt|imagen|image|video|v[ií]deo|shot|storyboard|anchor|ancla|clip|"
    r"render|generar|genera|nano ?banana|nb2|nbp|gpt ?image|kling|veo|sora|"
    r"seedance|midjourney|flux|ideogram|higgsfield|cr[ée]dito|gate|micro-?gate|"
    r"producci[óo]n visual|spot|reel|campa[ñn]a)\b",
    re.IGNORECASE,
)

# Always injected: the rules that govern every visual delivery.
MANDATORY = [
    ("produccion-visual-sw30", "SKILL.md"),
    ("ai-production-director", "SKILL.md"),
]

# Injected when the prompt points at that medium.
CONDITIONAL = {
    re.compile(r"\b(imagen|image|nano ?banana|nb2|nbp|gpt ?image|midjourney|flux|ideogram|still|ancla|anchor)\b", re.I): [
        ("image", "SKILL.md"),
        ("image", "references/golden-rules.md"),
    ],
    re.compile(r"\b(video|v[ií]deo|kling|veo|sora|seedance|hailuo|clip|movimiento|motion)\b", re.I): [
        ("video", "references/dramaturgy.md"),
        ("video", "references/universal-rules.md"),
    ],
    re.compile(r"\b(shot|storyboard|shots\.json|escaleta)\b", re.I): [
        ("storyboard-architect", "SKILL.md"),
    ],
}


def resolve(skill: str, rel: str) -> Path | None:
    for pattern in (f"*/{skill}/{rel}", f"*/*/{skill}/{rel}"):
        for candidate in SKILLS_ROOT.glob(pattern):
            if candidate.is_file():
                return candidate
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as exc:
        print(f"inject_rules: unreadable hook payload: {exc}", file=sys.stderr)
        return 1

    prompt = payload.get("prompt") or ""
    if not TRIGGERS.search(prompt):
        return 0

    wanted: list[tuple[str, str]] = list(MANDATORY)
    for pattern, files in CONDITIONAL.items():
        if pattern.search(prompt):
            for f in files:
                if f not in wanted:
                    wanted.append(f)

    parts: list[str] = []
    injected: list[str] = []
    missing: list[str] = []
    dropped: list[str] = []
    used = 0

    for i, (skill, rel) in enumerate(wanted):
        path = resolve(skill, rel)
        label = f"{skill}/{rel}"
        if path is None:
            missing.append(label)
            continue
        text = path.read_text(encoding="utf-8")
        is_mandatory = i < len(MANDATORY)
        if not is_mandatory and used + len(text) > BUDGET_CHARS:
            dropped.append(f"{label} ({len(text)} chars)")
            continue
        used += len(text)
        injected.append(label)
        parts.append(f"\n===== FUENTE OBLIGATORIA: {label} =====\n{text}")

    if not parts and not missing:
        return 0

    header = [
        "REGLAS INYECTADAS POR HOOK — no son opcionales y no dependen de que alguien",
        "decidiera leerlas. Texto completo, verbatim, de la fuente instalada.",
        "",
        f"Inyectadas ({len(injected)}): " + ", ".join(injected),
    ]
    if missing:
        header += ["", f"NO ENCONTRADAS ({len(missing)}): " + ", ".join(missing),
                   "  Estas reglas NO estan en contexto. No afirmes haberlas aplicado."]
    if dropped:
        header += ["", f"OMITIDAS POR PRESUPUESTO ({len(dropped)}): " + ", ".join(dropped),
                   "  Leelas con Read antes de entregar, o declara que no aplican."]

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "\n".join(header) + "\n" + "\n".join(parts),
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
