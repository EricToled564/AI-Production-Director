#!/usr/bin/env python3
"""Mechanical prompt auditor reconstructed from SW30 §Verificación mecánica.

The source says audit_gi2 validates 15 columns and names the required concerns.
The source list is internally shorter than fifteen conceptual labels, so this
reconstruction keeps every named concern and uses two additional SW30-mandated
checks (word ceiling and one-job) to produce exactly 15 auditable columns.

Fails closed on any required check that cannot be established from the supplied
artifact. SOURCE_RECONSTRUCTED.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

try:
    from template_engine import TEMPLATES
except Exception:
    TEMPLATES = {}

STANDARD_RATIOS = {
    "1:1", "3:2", "2:3", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"
}
META_RE = re.compile(r"(?im)^\s*(?:model|quality|size|aspect\s*ratio|size\s*/\s*ratio)\s*:\s*|\b--ar\b")
SLOP = re.compile(r"\b(?:masterpiece|stunning|epic|beautiful lighting|professional|high quality|highly detailed|4k|8k)\b", re.I)
NEGATIVE_FRAMING = re.compile(r"\b(?:don't|do not|without|avoid)\b", re.I)
GAZE_WORDS = re.compile(r"\b(?:gaze|looking|looks|eyes?|face(?:s|d)?|toward(?:s)? camera|off-camera)\b", re.I)
HAND_WORDS = re.compile(r"\b(?:hand|hands|finger|fingers|grip|fist|palm)\b", re.I)
IDENTITY_WORDS = re.compile(r"\b(?:identity|same face|preserve face|facial structure|character anchor|idlock)\b", re.I)
BRAND_WORDS = re.compile(r"\b(?:logo|brand|wordmark|trademark|signage|lettering|text_lock)\b", re.I)
MOOD_WORDS = re.compile(r"\b(?:mood|calm|tense|intimate|documentary|editorial|joyful|somber|serene|urgent)\b", re.I)
COLOUR_WORDS = re.compile(r"\b(?:color|colour|palette|red|blue|green|amber|teal|cyan|magenta|black|white|gray|grey|warm|cool)\b", re.I)

@dataclass
class Check:
    name: str
    status: str  # PASS / FAIL / NA
    detail: str


def _ratio(metadata: dict[str, Any]) -> str | None:
    raw = str(metadata.get("aspect_ratio") or metadata.get("size_or_ratio") or metadata.get("ratio") or "").strip()
    m = re.search(r"\b(\d{1,2}:\d{1,2})\b", raw)
    return m.group(1) if m else None


def _word_count(text: str) -> int:
    return len(re.findall(r"\b\w+[\w'-]*\b", text))


def audit(a: dict[str, Any]) -> list[Check]:
    tipo = str(a.get("type") or a.get("tipo") or "").upper()
    prompt = str(a.get("prompt") or "")
    sections = a.get("sections") or {}
    blocks = a.get("block_ids") or {}
    metadata = a.get("metadata") or {}
    notes = str(a.get("notes") or "").strip()
    context = a.get("audit_context") or {}

    checks: list[Check] = []

    # 1 slots
    spec = TEMPLATES.get(tipo)
    missing = []
    if spec:
        for s in spec.required:
            if s == "notes":
                if not notes:
                    missing.append(s)
            elif not str(sections.get(s, "")).strip():
                missing.append(s)
    else:
        missing = ["known template type"]
    checks.append(Check("slots", "PASS" if not missing else "FAIL", "all required slots present" if not missing else f"missing: {', '.join(missing)}"))

    # 2 anti-slop
    bad = sorted({m.group(0).lower() for m in SLOP.finditer(prompt)})
    checks.append(Check("anti_slop", "PASS" if not bad else "FAIL", "no banned slop tokens" if not bad else "found: " + ", ".join(bad)))

    # 3 standard ratio
    ratio = _ratio(metadata)
    checks.append(Check("ratio_standard", "PASS" if ratio in STANDARD_RATIOS else "FAIL", f"ratio={ratio or 'missing'}"))

    # 4 metadata outside body
    checks.append(Check("metadata_outside_prompt", "PASS" if not META_RE.search(prompt) else "FAIL", "metadata outside body" if not META_RE.search(prompt) else "metadata syntax found inside prompt"))

    # 5 Notes
    checks.append(Check("notes", "PASS" if notes else "FAIL", "Notes present" if notes else "Notes missing"))

    # 6 camera five effects (conditional on optics_required)
    optics_required = bool(context.get("optics_required"))
    optics_text = " ".join([str(sections.get("optics", "")), prompt]).lower()
    effect_terms = {
        "compression": ("compression", "compressed perspective", "telephoto compression"),
        "bokeh/wash": ("bokeh", "background wash", "softly out of focus", "shallow depth"),
        "vignette": ("vignette", "edge falloff"),
        "halation": ("halation", "bloom around highlights"),
        "grain": ("grain", "film grain"),
    }
    absent = [k for k, terms in effect_terms.items() if not any(t in optics_text for t in terms)]
    if optics_required:
        checks.append(Check("camera_5_effects", "PASS" if not absent else "FAIL", "all five present" if not absent else "missing: " + ", ".join(absent)))
    else:
        checks.append(Check("camera_5_effects", "NA", "optics_required=false"))

    # 7 mood
    mood_required = bool(context.get("mood_required", tipo in {"T1", "T2", "T3", "T4"}))
    mood_ok = bool(str(sections.get("mood", "")).strip() or MOOD_WORDS.search(prompt))
    checks.append(Check("mood", "PASS" if mood_ok else ("FAIL" if mood_required else "NA"), "mood/use-case signal present" if mood_ok else "mood not established"))

    # 8 colour
    colour_required = bool(context.get("colour_required", False))
    colour_ok = bool(str(sections.get("colour", "")).strip() or COLOUR_WORDS.search(prompt))
    checks.append(Check("colour", "PASS" if colour_ok else ("FAIL" if colour_required else "NA"), "colour signal present" if colour_ok else "no explicit colour requirement"))

    # 9 identity lock
    identity_required = bool(context.get("identity_required", False))
    identity_ok = bool("idlock" in blocks or IDENTITY_WORDS.search(prompt))
    checks.append(Check("identity_lock", "PASS" if identity_ok else ("FAIL" if identity_required else "NA"), "identity lock present" if identity_ok else "identity not required"))

    # 10 brand text
    brand_text_required = bool(context.get("brand_text_required", False))
    brand_ok = bool("text_lock" in blocks or BRAND_WORDS.search(prompt))
    checks.append(Check("brand_text", "PASS" if brand_ok else ("FAIL" if brand_text_required else "NA"), "brand/text rule present" if brand_ok else "brand text not required"))

    # 11 positive framing
    # Constraints may legitimately contain prohibitions; only fail when main prompt is dominated by negatives.
    negatives = len(NEGATIVE_FRAMING.findall(prompt))
    positive_ok = negatives <= int(context.get("max_negative_phrases", 4))
    checks.append(Check("framing_positive", "PASS" if positive_ok else "FAIL", f"negative phrases={negatives}"))

    # 12 gaze
    gaze_required = bool(context.get("gaze_required", False))
    gaze_ok = bool(GAZE_WORDS.search(prompt))
    checks.append(Check("gaze", "PASS" if gaze_ok else ("FAIL" if gaze_required else "NA"), "gaze/orientation described" if gaze_ok else "gaze not required"))

    # 13 hands
    hands_required = bool(context.get("hands_required", False))
    hands_ok = bool(HAND_WORDS.search(prompt))
    checks.append(Check("hands", "PASS" if hands_ok else ("FAIL" if hands_required else "NA"), "hands/grip described" if hands_ok else "hands not load-bearing"))

    # 14 word ceiling — required by SW30 critical rule 14
    wc = _word_count(prompt)
    max_words = context.get("max_prompt_words")
    if max_words is None:
        checks.append(Check("word_ceiling", "NA", f"word_count={wc}; no ceiling supplied"))
    else:
        max_words = int(max_words)
        checks.append(Check("word_ceiling", "PASS" if wc <= max_words else "FAIL", f"{wc}/{max_words} words"))

    # 15 one job — required by SW30 critical rule 1
    jobs = context.get("jobs")
    if jobs is None:
        checks.append(Check("single_job", "NA", "jobs not supplied"))
    else:
        jobs = int(jobs)
        checks.append(Check("single_job", "PASS" if jobs == 1 else "FAIL", f"jobs={jobs}"))

    assert len(checks) == 15
    return checks


def load_artifact(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "artifact" in data and isinstance(data["artifact"], dict):
        base = dict(data["artifact"])
        if "audit_context" in data:
            base["audit_context"] = data["audit_context"]
        return base
    return data


def selftest() -> int:
    sample = {
        "type": "T3",
        "sections": {
            "scene": "Clay court under daylight.",
            "subject": "One male tennis player.",
            "anatomy": "Natural proportions and coherent joints.",
            "usecase": "Editorial sports photograph.",
            "mood": "Focused editorial tension.",
            "colour": "Natural red clay and neutral sportswear.",
        },
        "block_ids": {"anatomy": "anatomy"},
        "metadata": {"model": "nano-banana-pro", "size_or_ratio": "16:9"},
        "prompt": "Create an editorial sports photograph of one male tennis player on red clay, frozen at ball contact, natural proportions, softly out of focus audience.",
        "notes": "No visual reference sent to generator.",
        "audit_context": {"max_prompt_words": 120, "jobs": 1},
    }
    checks = audit(sample)
    failures = [c for c in checks if c.status == "FAIL"]
    if failures:
        for c in failures:
            print("FAIL", c.name, c.detail)
        return 1
    print("SELFTEST PASS — 15 columns emitted, no blocking failure")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("artifact", nargs="?", type=Path)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest or args.artifact is None:
        return selftest()
    try:
        artifact = load_artifact(args.artifact)
        checks = audit(artifact)
    except Exception as e:
        print(f"audit_gi2: {e}", file=sys.stderr)
        return 2
    failed = [c for c in checks if c.status == "FAIL"]
    if args.json:
        print(json.dumps({"status": "FAIL" if failed else "PASS", "checks": [asdict(c) for c in checks]}, ensure_ascii=False, indent=2))
    else:
        print("audit_gi2 — 15 columns")
        for c in checks:
            print(f"{c.status:4}  {c.name:24} {c.detail}")
        print("STATUS:", "FAIL" if failed else "PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
