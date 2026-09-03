#!/usr/bin/env python3
"""Stop hook: enforces the image skill's own golden rules on delivered prompts.

Authority chain:
  ai-production-director, Etapa 5 -> "`image` (smixs) es la autoridad de sintaxis
  final por modelo", and section 6.2 -> "Todo prompt FINAL se escribe en la
  sintaxis del modelo destino segun el archivo smixs correspondiente."

Checks, each one traced to a rule in image/references/golden-rules.md:

  R1  Start with a Verb   blocking   verbs parsed from the file at runtime
  R4  Natural Language    blocking   keyword soup ("Cool car, neon, city, 8k")
  6.2 Target model named  blocking   a final prompt with no declared model
  R2  Positive Framing    warning    see the note below

R2 is deliberately non-blocking. The skill's own approved example carries
"no makeup", so a strict negation check would reject prompts the skill blesses.
It is reported as context instead of a veto.

Runs alongside gate_dramaturgy.py, which owns the section 6.1 vocabulary.
"""

import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompt_detect import visual_blocks, IMAGE_MODELS, VIDEO_MODELS  # noqa: E402

SKILLS_ROOT = Path(
    os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude" / "skills" / "synced")
)
MAX_CONSECUTIVE_BLOCKS = 3

FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)
QUOTED_RE = re.compile(r'"([A-Za-z][A-Za-z ]{1,20})"')
OVERRIDE_RE = re.compile(r"^\s*OVERRIDE:\s*(.+?)\s+-\s+(.+?)\s*$", re.MULTILINE)

# Model ids the pipeline knows. Sources: image/SKILL.md (Nano Banana, GPT Image 2)
# and ai-production-director 6.2 (Flux, Midjourney, Ideogram via forge adapters).
IMAGE_MODELS = (
    "nano banana", "nano-banana", "nanobanana", "nbp", "nb2",
    "gpt image", "gpt-image", "seedream", "midjourney", "flux", "ideogram",
)
# Naming any of these means the block is a motion prompt; the image rules do not apply.
VIDEO_MODELS = ("kling", "veo", "sora", "seedance", "hailuo", "runway", "luma", "pika")

NEGATION_RE = re.compile(r"\b(?:no|without|not)\s+[a-z]", re.IGNORECASE)


def find_golden_rules() -> Path | None:
    for pattern in ("*/image/references/golden-rules.md",
                    "*/*/image/references/golden-rules.md"):
        for candidate in SKILLS_ROOT.glob(pattern):
            return candidate
    return None


def load_verbs(path: Path) -> list[str]:
    """Parse the approved opening verbs from the '## 1. Start with a Verb' rule."""
    text = path.read_text(encoding="utf-8")
    start = text.find("## 1. Start with a Verb")
    if start == -1:
        return []
    rest = text[start:]
    end = rest.find("\n## ")
    section = rest if end == -1 else rest[:end]
    verbs = {v.strip().lower() for v in QUOTED_RE.findall(section) if v.strip()}
    return sorted(verbs)


def is_keyword_soup(line: str) -> bool:
    """Rule 4: 'Cool car, neon, city, night, 8k' — fragments, no sentence."""
    parts = [p.strip() for p in line.split(",") if p.strip()]
    if len(parts) < 4:
        return False
    if line.rstrip().endswith("."):
        return False
    # A real sentence carries a finite verb; fragments are 1-3 bare words.
    return all(len(p.split()) <= 3 for p in parts)


def state_path(session_id: str) -> Path:
    d = Path(os.environ.get("TMPDIR", "/tmp")) / "fupai-gate"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"img-{re.sub(r'[^A-Za-z0-9_-]', '_', session_id)}.count"


STATE_TTL_S = 3600


def read_count(p: Path) -> int:
    """Consecutive blocks, ignoring state left over from an older session."""
    try:
        count, stamp = p.read_text().split(":")
        if time.time() - float(stamp) > STATE_TTL_S:
            return 0
        return int(count)
    except Exception:
        return 0


def write_count(p: Path, n: int) -> None:
    try:
        p.write_text(f"{n}:{time.time()}")
    except OSError:
        pass


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as exc:
        print(f"gate_image: unreadable hook payload: {exc}", file=sys.stderr)
        return 1

    message = payload.get("last_assistant_message") or ""
    counter = state_path(payload.get("session_id") or "nosession")

    low_msg = message.lower()
    blocks = visual_blocks(message)
    if not blocks:
        write_count(counter, 0)
        return 0  # nada que sea entrega de prompt visual

    if any(m in low_msg for m in VIDEO_MODELS) and not any(m in low_msg for m in IMAGE_MODELS):
        write_count(counter, 0)
        return 0  # motion prompt; gate_dramaturgy still applies

    rules = find_golden_rules()
    if rules is None:
        print(
            f"gate_image: image/references/golden-rules.md not found under "
            f"{SKILLS_ROOT}. Gate could not run — image rules were NOT checked.",
            file=sys.stderr,
        )
        return 1

    verbs = load_verbs(rules)
    if not verbs:
        print(
            f"gate_image: no opening verbs parsed from {rules}. "
            "Gate could not run — image rules were NOT checked.",
            file=sys.stderr,
        )
        return 1

    overridden = {m.group(1).strip().lower() for m in OVERRIDE_RE.finditer(message)}
    model_named = any(m in low_msg for m in IMAGE_MODELS)

    def waived(rule: str) -> bool:
        return rule.lower() in overridden

    fails: list[str] = []
    warns: list[str] = []

    for idx, block in blocks:
        lines = [l for l in block.splitlines() if l.strip()]
        if not lines:
            continue

        first = lines[0].strip()
        if not waived("R1") and not any(
            first.lower().startswith(v) for v in verbs
        ):
            fails.append(
                f'  FAIL  block #{idx}  R1 Start with a Verb\n'
                f'        first line: "{first[:80]}"\n'
                f"        expected one of: {', '.join(verbs)}"
            )

        if not waived("R4"):
            for line in lines:
                if is_keyword_soup(line):
                    fails.append(
                        f"  FAIL  block #{idx}  R4 Natural Language (keyword soup)\n"
                        f'        -> "{line.strip()[:80]}"'
                    )
                    break

        if not waived("6.2") and not model_named:
            fails.append(
                f"  FAIL  block #{idx}  6.2 no target model declared\n"
                f"        name one of: {', '.join(IMAGE_MODELS[:6])}…"
            )

        for line in lines:
            if NEGATION_RE.search(line):
                warns.append(f'  WARN  block #{idx}  R2 Positive Framing -> "{line.strip()[:70]}"')
                break

    if not fails:
        write_count(counter, 0)
        if warns:
            # Non-blocking: exit 0 stdout is added as context Claude can see.
            print(
                "gate_image — advertencias (no bloquean):\n"
                + "\n".join(warns)
                + "\n  R2 pide describir lo que SI quieres. Revisa si aplica."
            )
        return 0

    seen = read_count(counter)
    if seen >= MAX_CONSECUTIVE_BLOCKS:
        write_count(counter, 0)
        print(
            f"gate_image: {len(fails)} violation(s) still present after {seen} blocked "
            "attempts. Releasing the turn so the session does not deadlock. "
            "THE PROMPT IS NOT CLEARED — do not spend credits on it.",
            file=sys.stderr,
        )
        return 1

    write_count(counter, seen + 1)
    report = [
        "DELIVERY BLOCKED — image golden rules.",
        f"Authority: {rules}",
        "",
        *fails,
    ]
    if warns:
        report += ["", *warns]
    report += [
        "",
        "Override with a line: OVERRIDE: R1 - <reason>  (R1 | R4 | 6.2)",
        f"(attempt {seen + 1} of {MAX_CONSECUTIVE_BLOCKS})",
    ]
    print("\n".join(report), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
