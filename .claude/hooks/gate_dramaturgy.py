#!/usr/bin/env python3
"""Stop hook: blocks delivery of visual prompts that carry banned vocabulary.

Authority chain (ai-production-director SKILL.md section 6.1):
    "El vocabulario prohibido de `video`/dramaturgy ... gana siempre"

The banned list is read at runtime from the `video` skill itself
(references/dramaturgy.md, section "What is banned"), so editing the skill
updates the gate. Nothing is hardcoded and nothing is copied.

Scope rule: only fenced code blocks in the final assistant message are
scanned. Prose that merely discusses a banned word is not a delivery.

Escape hatch: a line matching `OVERRIDE: <term> - <reason>` anywhere in the
message clears that term for the current turn, and stays visible in the
transcript for audit.
"""

import json
import os
import re
import sys
import time
from pathlib import Path

SKILLS_ROOT = Path(
    os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude" / "skills" / "synced")
)
MAX_CONSECUTIVE_BLOCKS = 3

FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)
OVERRIDE_RE = re.compile(r"^\s*OVERRIDE:\s*(.+?)\s+-\s+(.+?)\s*$", re.MULTILINE)
# Terms inside the "What is banned" section are quoted: - "cinematic", "epic"
QUOTED_RE = re.compile(r'"([^"]{2,40})"')


def find_dramaturgy() -> Path | None:
    """Locate video/references/dramaturgy.md under any synced skill root."""
    for candidate in SKILLS_ROOT.glob("*/video/references/dramaturgy.md"):
        return candidate
    for candidate in SKILLS_ROOT.glob("*/*/video/references/dramaturgy.md"):
        return candidate
    return None


def load_banned(path: Path) -> list[str]:
    """Extract the quoted terms under the '### What is banned' heading."""
    text = path.read_text(encoding="utf-8")
    start = text.find("### What is banned")
    if start == -1:
        return []
    rest = text[start + len("### What is banned"):]
    end = rest.find("\n### ")
    section = rest if end == -1 else rest[:end]

    terms: list[str] = []
    for raw in QUOTED_RE.findall(section):
        term = raw.strip().lower()
        # Split compound entries such as "cinematic, professional, high quality"
        for part in term.split(","):
            part = part.strip()
            # Drop the illustrative emotion examples, which are patterns not terms
            if part and not part.startswith(("he is", "she is")):
                terms.append(part)
    return sorted(set(terms), key=len, reverse=True)


def state_path(session_id: str) -> Path:
    d = Path(os.environ.get("TMPDIR", "/tmp")) / "fupai-gate"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{re.sub(r'[^A-Za-z0-9_-]', '_', session_id)}.count"


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
        print(f"gate_dramaturgy: unreadable hook payload: {exc}", file=sys.stderr)
        return 1  # non-blocking error, visible in transcript

    message = payload.get("last_assistant_message") or ""
    session_id = payload.get("session_id") or "nosession"
    counter = state_path(session_id)

    blocks = FENCE_RE.findall(message)
    if not blocks:
        write_count(counter, 0)
        return 0

    dramaturgy = find_dramaturgy()
    if dramaturgy is None:
        print(
            "gate_dramaturgy: video/references/dramaturgy.md not found under "
            f"{SKILLS_ROOT}. Gate could not run — vocabulary was NOT checked.",
            file=sys.stderr,
        )
        return 1  # fail loud, never silently pass as if checked

    banned = load_banned(dramaturgy)
    if not banned:
        print(
            f"gate_dramaturgy: no banned terms parsed from {dramaturgy}. "
            "Gate could not run — vocabulary was NOT checked.",
            file=sys.stderr,
        )
        return 1

    overridden = {m.group(1).strip().lower() for m in OVERRIDE_RE.finditer(message)}

    violations: list[tuple[int, str, str]] = []
    for idx, block in enumerate(blocks, start=1):
        low = block.lower()
        for term in banned:
            if term in overridden:
                continue
            if re.search(rf"(?<![a-z]){re.escape(term)}(?![a-z])", low):
                line = next(
                    (l.strip() for l in block.splitlines() if term in l.lower()), ""
                )
                violations.append((idx, term, line[:110]))

    if not violations:
        write_count(counter, 0)
        return 0

    seen = read_count(counter)
    if seen >= MAX_CONSECUTIVE_BLOCKS:
        write_count(counter, 0)
        print(
            f"gate_dramaturgy: {len(violations)} violation(s) still present after "
            f"{seen} blocked attempts. Releasing the turn so the session does not "
            "deadlock. THE PROMPT BELOW IS NOT CLEARED — do not spend credits on it.",
            file=sys.stderr,
        )
        return 1

    write_count(counter, seen + 1)

    report = [
        "DELIVERY BLOCKED — banned vocabulary (ai-production-director 6.1).",
        f"Authority: {dramaturgy}",
        "",
    ]
    for idx, term, line in violations:
        report.append(f'  FAIL  block #{idx}  "{term}"')
        if line:
            report.append(f"        -> {line}")
    report += [
        "",
        "Each banned word is a placeholder for absent detail. Replace it with the",
        "three details dramaturgy.md requires: environmental pressure, physical",
        "micro-action, sound/visual anchor. Then deliver again.",
        "",
        "If a term is deliberate, add a line: OVERRIDE: <term> - <reason>",
        f"(attempt {seen + 1} of {MAX_CONSECUTIVE_BLOCKS})",
    ]
    print("\n".join(report), file=sys.stderr)
    return 2  # blocking: Claude does not stop, sees stderr, must fix


if __name__ == "__main__":
    sys.exit(main())
