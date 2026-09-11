#!/usr/bin/env python3
"""Stop hook: un prompt de imagen sólo se entrega si lo produjo apd_run.py.

Cierra el hueco que ningún otro gate cubría: los gates léxicos verifican cómo está
escrito un prompt, no quién lo escribió. Aquí el bloque cercado que se entrega
tiene que coincidir, byte a byte salvo espacios, con el `DELIVERABLE.txt` (o su
sección Prompt) de un run en estado DELIVERED bajo `apd/runs/`. Un prompt
redactado a mano — aunque cumpla todos los demás gates — no sale.

Aplica a bloques que prompt_detect reconoce como prompt visual de imagen. Los
prompts de video no pasan por apd_run todavía y no se bloquean aquí.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompt_detect import visual_blocks, IMAGE_MODELS, VIDEO_MODELS  # noqa: E402

PROJECT = Path(os.environ.get("CLAUDE_PROJECT_DIR", Path(__file__).resolve().parents[2]))
RUNS = Path(os.environ.get("APD_RUNS_DIR", PROJECT / "apd" / "runs"))
OVERRIDE_RE = re.compile(r"^\s*OVERRIDE:\s*APD\s+-\s+(.+?)\s*$", re.MULTILINE)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def delivered_texts() -> dict[str, str]:
    """{sha256(normalizado): run} para cada DELIVERABLE.txt de un run DELIVERED."""
    out: dict[str, str] = {}
    if not RUNS.exists():
        return out
    for state in RUNS.glob("*/run.json"):
        try:
            s = json.loads(state.read_text(encoding="utf-8"))
        except Exception:
            continue
        if s.get("status") != "DELIVERED":
            continue
        d = state.parent / "DELIVERABLE.txt"
        if not d.exists():
            continue
        full = d.read_text(encoding="utf-8")
        m = re.search(r"^Prompt:\n(.*?)\nNotes:\n", full, re.DOTALL | re.MULTILINE)
        for cand in (full, m.group(1) if m else None):
            if cand:
                out[hashlib.sha256(norm(cand).encode()).hexdigest()] = state.parent.name
    return out


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as exc:
        print(f"gate_apd_delivery: unreadable hook payload: {exc}", file=sys.stderr)
        return 1
    message = payload.get("last_assistant_message") or ""
    blocks = visual_blocks(message)
    if not blocks:
        return 0
    low = message.lower()
    if any(m in low for m in VIDEO_MODELS) and not any(m in low for m in IMAGE_MODELS):
        return 0
    if OVERRIDE_RE.search(message):
        # Sólo Eric puede pedirlo; la línea queda en la respuesta como registro.
        return 0

    known = delivered_texts()
    fails = []
    for idx, block in blocks:
        h = hashlib.sha256(norm(block).encode()).hexdigest()
        if h not in known:
            first = next((l.strip() for l in block.splitlines() if l.strip()), "")
            fails.append(f'  FAIL  block #{idx}  no es DELIVERABLE.txt de ningún run DELIVERED\n        primera línea: "{first[:80]}"\n        sha256(normalizado): {h[:16]}…')
    if not fails:
        return 0
    print(
        "gate_apd_delivery — ENTREGA BLOQUEADA\n"
        + "\n".join(fails)
        + f"\n\nRuns DELIVERED conocidos bajo {RUNS}: {sorted(set(known.values())) or 'ninguno'}.\n"
        "Un prompt de imagen sólo se entrega pegando íntegro el DELIVERABLE.txt (o su\n"
        "sección Prompt) de un run que terminó en DELIVERED con\n"
        "  python3 apd/apd_run.py new / audit-pack / ledger.\n"
        "No redactes ni corrijas el prompt a mano: si algo debe cambiar, escribe un\n"
        "delta autorizado y corre `apd_run.py revise`.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
