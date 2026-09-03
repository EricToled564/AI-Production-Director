#!/usr/bin/env python3
"""Stop hook: enforce the 3-line micro-gate header on any visual delivery.

produccion-visual-sw30/SKILL.md:

    Antes de (a) cualquier generación que gaste créditos y (b) entregar cualquier
    prompt visual, la respuesta abre con exactamente 3 líneas:
      SKILL: <archivo y sección leídos EN ESTE turno>
      RIESGOS: <qué puede fallar y qué línea del prompt lo mitiga>
      TÉCNICA: <técnica probada encontrada y fuente, o "no encontrada">
    Entrega sin cabecera = inválida; Eric la rechaza sin leerla.

That rule is already unambiguous and already has a stated consequence. It was
still being skipped, because "invalid" was enforced by the reader noticing.
Here the turn does not close without the header.

Placeholder headers do not count: SKILL must name a real file that exists in the
installed skills, since the field asserts what was read this turn.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompt_detect import visual_blocks  # noqa: E402

SKILLS_ROOT = Path(
    os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude" / "skills" / "synced")
)
MAX_CONSECUTIVE_BLOCKS = 3
STATE_TTL_S = 3600

FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)
# A fenced block counts as a visual prompt when it names a target model or reads
# like a generation brief. Prose about prompts is not a delivery.
VISUAL_RE = re.compile(
    r"\b(nano ?banana|nb2|nbp|gpt ?image|midjourney|flux|ideogram|seedream|"
    r"kling|veo|sora|seedance|hailuo|runway|luma|pika)\b",
    re.IGNORECASE,
)
PROMPTISH_RE = re.compile(
    r"^\s*(create|generate|design|transform|convert|edit|wide shot|close-?up|"
    r"medium shot|mcu|ecu)\b|^\s*(format|aspect ratio|negative prompt)\s*:",
    re.IGNORECASE | re.MULTILINE,
)

HEADER_RE = re.compile(
    r"^\s*SKILL\s*:\s*(?P<skill>.+?)\s*\n"
    r"\s*RIESGOS\s*:\s*(?P<riesgos>.+?)\s*\n"
    r"\s*T[EÉ]CNICA\s*:\s*(?P<tecnica>.+?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)

FILE_TOKEN_RE = re.compile(r"[\w./-]+\.md")


def state_path(session_id: str) -> Path:
    d = Path(os.environ.get("TMPDIR", "/tmp")) / "fupai-gate"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"mg-{re.sub(r'[^A-Za-z0-9_-]', '_', session_id)}.count"


def read_count(p: Path) -> int:
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


def skill_file_exists(token: str) -> bool:
    name = token.strip().lstrip("`").rstrip("`,.;")
    for pattern in (f"*/**/{name}", f"*/{name}"):
        for _ in SKILLS_ROOT.glob(pattern):
            return True
    return any(SKILLS_ROOT.glob(f"*/*/{Path(name).name}")) or any(
        SKILLS_ROOT.glob(f"*/*/*/{Path(name).name}")
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as exc:
        print(f"gate_microgate: unreadable hook payload: {exc}", file=sys.stderr)
        return 1

    message = payload.get("last_assistant_message") or ""
    counter = state_path(payload.get("session_id") or "nosession")

    delivers = visual_blocks(message)
    if not delivers:
        write_count(counter, 0)
        return 0

    match = HEADER_RE.search(message)
    problems: list[str] = []

    if match is None:
        problems.append(
            "  FAIL  falta la cabecera de 3 lineas. La respuesta debe ABRIR con:\n"
            "          SKILL: <archivo y seccion leidos EN ESTE turno>\n"
            "          RIESGOS: <que puede fallar y que linea del prompt lo mitiga>\n"
            "          TECNICA: <tecnica probada y fuente, o \"no encontrada\">"
        )
    else:
        skill_field = match.group("skill")
        tokens = FILE_TOKEN_RE.findall(skill_field)
        if not tokens:
            problems.append(
                f'  FAIL  SKILL: no nombra ningun archivo .md -> "{skill_field[:70]}"'
            )
        else:
            unknown = [t for t in tokens if not skill_file_exists(t)]
            if unknown:
                problems.append(
                    "  FAIL  SKILL: nombra archivos que no existen en los skills "
                    f"instalados: {', '.join(unknown)}"
                )
        for field in ("riesgos", "tecnica"):
            if len(match.group(field).strip()) < 12:
                problems.append(f"  FAIL  {field.upper()}: vacio o de relleno")

    if not problems:
        write_count(counter, 0)
        return 0

    seen = read_count(counter)
    if seen >= MAX_CONSECUTIVE_BLOCKS:
        write_count(counter, 0)
        print(
            f"gate_microgate: cabecera aun invalida tras {seen} bloqueos. Se libera el "
            "turno para no trabar la sesion. LA ENTREGA SIGUE SIENDO INVALIDA segun "
            "produccion-visual-sw30 — no gastes creditos con ella.",
            file=sys.stderr,
        )
        return 1

    write_count(counter, seen + 1)
    print(
        "\n".join(
            [
                "DELIVERY BLOCKED — micro-gate ausente o invalido.",
                "Autoridad: produccion-visual-sw30/SKILL.md, seccion MICRO-GATE",
                '"Entrega sin cabecera = invalida; Eric la rechaza sin leerla."',
                "",
                *problems,
                "",
                f"(intento {seen + 1} de {MAX_CONSECUTIVE_BLOCKS})",
            ]
        ),
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
