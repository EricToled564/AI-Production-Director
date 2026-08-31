#!/usr/bin/env python3
"""PostToolUse hook: runs the shotkit validator whenever shots.json is written.

Authority chain (ai-production-director SKILL.md, Etapa 4):
    "Gate: `tools/validate_shots.py` limpio"

Two packaging defects stop that gate from ever running in a synced-skill
install, and this hook repairs both before delegating:

  1. `jsonschema` missing -> the validator exits 1 for the wrong reason.
     Detected and reported, never silently swallowed.
  2. `_shotkit.py` sets REPO_ROOT to the skill directory and then appends
     `skills/storyboard-architect/...`, a repo layout that a synced install
     does not have. An additive symlink shim is recreated on every run, so a
     skill re-sync cannot leave the gate permanently broken.

Nothing in the skill's own content is modified.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

SKILLS_ROOT = Path(
    os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude" / "skills" / "synced")
)
WATCHED = {"shots.json", "text-overlays.json"}


def find_architect() -> Path | None:
    for pattern in ("*/storyboard-architect", "*/*/storyboard-architect"):
        for candidate in SKILLS_ROOT.glob(pattern):
            if (candidate / "tools" / "validate_shots.py").is_file():
                return candidate
    return None


def heal_shim(architect: Path) -> None:
    """Recreate the layout _shotkit.py expects. Idempotent and additive."""
    shim = architect / "skills"
    shim.mkdir(exist_ok=True)
    links = {
        shim / "storyboard-architect": Path(".."),
        shim / "visual-prompt-forge": Path("../../visual-prompt-forge"),
    }
    for link, target in links.items():
        if link.is_symlink() and os.readlink(link) == str(target):
            continue
        if link.is_symlink() or link.exists():
            link.unlink()
        link.symlink_to(target)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as exc:
        print(f"gate_shots: unreadable hook payload: {exc}", file=sys.stderr)
        return 1

    tool_input = payload.get("tool_input") or {}
    written = tool_input.get("file_path") or tool_input.get("path") or ""
    if Path(written).name not in WATCHED:
        return 0

    target_dir = Path(written).parent
    if not (target_dir / "shots.json").is_file():
        return 0  # the set is not complete yet; nothing to validate

    architect = find_architect()
    if architect is None:
        print(
            f"gate_shots: storyboard-architect not found under {SKILLS_ROOT}. "
            "Etapa 4 gate did NOT run — shots.json is unvalidated.",
            file=sys.stderr,
        )
        return 1

    try:
        import jsonschema  # noqa: F401
    except ImportError:
        print(
            "gate_shots: jsonschema is not installed, so validate_shots.py cannot "
            "run and the Etapa 4 gate did NOT execute. Fix with:\n"
            "  pip install pyyaml jsonschema --break-system-packages",
            file=sys.stderr,
        )
        return 1

    try:
        heal_shim(architect)
    except OSError as exc:
        print(f"gate_shots: could not repair the shotkit path shim: {exc}", file=sys.stderr)
        return 1

    proc = subprocess.run(
        [sys.executable, str(architect / "tools" / "validate_shots.py"), str(target_dir)],
        capture_output=True,
        text=True,
        cwd=str(architect),
    )
    if proc.returncode == 0:
        return 0

    print(
        "ETAPA 4 GATE FAILED — shots.json is not the source of truth yet.\n"
        "ai-production-director: 'El gate se verifica ANTES de avanzar. Si falla, "
        "se corrige en la etapa actual — nunca se \"arregla despues\".'\n"
        "Do not write prompts against this shot list.\n\n"
        + (proc.stdout or "")
        + (proc.stderr or ""),
        file=sys.stderr,
    )
    return 2  # blocking: Claude sees stderr and must fix before continuing


if __name__ == "__main__":
    sys.exit(main())
