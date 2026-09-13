#!/usr/bin/env python3
"""Genera apd/artifact/data.js: todo lo que la página necesita, extraído mecánicamente
del repo y de los skills instalados. Nada se transcribe a mano.

    python3 apd/artifact/build_data.py            # escribe apd/artifact/data.js

Contenido:
  ruleset (3.4.0, recortado a lo que usa el matcher), políticas de conflicto,
  routing canónico + overlay aprendido, schemas (case, facts, delta), topes de
  palabras de _capabilities.json, verbos iniciales (golden-rules.md), vocabulario
  prohibido (dramaturgy.md + Anti-Slop de gpt-image.md), bloques canónicos T1 y
  contratos T1..T5 (template_engine), manifiesto de archivos de skill (líneas) para
  verificar procedencias, fuentes de skill que la página entrega al extractor de
  hechos y AUDITOR.md.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HOOKS = REPO / ".claude" / "hooks"
RULES = REPO / ".claude" / "rules"
PKG = REPO / "production-package"
OUT = Path(__file__).resolve().parent / "data.js"
SKILLS_ROOT = Path(os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude" / "skills" / "synced"))

sys.path.insert(0, str(HOOKS))
sys.path.insert(0, str(PKG))
import gate_dramaturgy  # noqa: E402
import gate_image  # noqa: E402
import template_engine  # noqa: E402

# Archivos que el extractor de hechos recibe íntegros (inject_rules.py hace lo mismo
# con SKILL.md de sw30 y del director; aquí van además las referencias del skill image).
SOURCE_FILES = [
    "produccion-visual-sw30/SKILL.md",
    "image/SKILL.md",
    "image/references/golden-rules.md",
    "image/references/gpt-image.md",
    "image/references/nano-banana.md",
    "image/references/prompt-framework.md",
    "image/references/creative-direction.md",
    "image/references/models.md",
]


def skill_root() -> Path:
    for cand in SKILLS_ROOT.glob("*/image/SKILL.md"):
        return cand.parents[1]
    for cand in SKILLS_ROOT.glob("*/*/image/SKILL.md"):
        return cand.parents[1]
    raise SystemExit(f"skills no instalados bajo {SKILLS_ROOT}")


def main() -> int:
    root = skill_root()
    rs = json.loads((RULES / "v3" / "build" / "ruleset-3.5.0.json").read_text(encoding="utf-8"))
    rules = []
    for item in rs["rules"]:
        r, m = item["rule"], item["metadata"]
        rules.append({
            "rule": {k: r.get(k) for k in ("id", "skill", "source_path", "line", "text")},
            "metadata": {k: m.get(k) for k in ("when", "effect", "validator", "supersedes", "conflict_key", "priority", "authority", "classification_status")},
        })
    manifest = {}
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in {".md", ".json", ".yaml", ".yml"}:
            manifest[str(p.relative_to(root))] = len(p.read_text(encoding="utf-8", errors="replace").splitlines())
    sources = {f: (root / f).read_text(encoding="utf-8") for f in SOURCE_FILES if (root / f).exists()}
    caps = json.loads((root / "visual-prompt-forge" / "adapters" / "_capabilities.json").read_text(encoding="utf-8"))
    ceilings = {g["id"]: int(g["max_prompt_words"]) for g in caps["generators"]}
    dram, anti = gate_dramaturgy.find_dramaturgy(), gate_dramaturgy.find_antislop()
    banned = sorted(set((gate_dramaturgy.load_banned(dram) if dram else []) + (gate_dramaturgy.load_antislop(anti) if anti else [])))
    golden = gate_image.find_golden_rules()
    verbs = gate_image.load_verbs(golden) if golden else []
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=str(REPO)).stdout.strip()
    except Exception:
        commit = ""
    data = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo_commit": commit,
        "ruleset": {"ruleset_version": rs["ruleset_version"], "ruleset_sha256": rs["ruleset_sha256"], "published": rs["published"],
                    "rules": rules, "conflict_policies": rs.get("conflict_policies", [])},
        "routing": {"canonical": json.loads((RULES / "v3" / "build" / "model-routing.canonical-v3.3.json").read_text(encoding="utf-8")),
                    "learned": json.loads((RULES / "v3" / "learned" / "model-routing.v3.2.json").read_text(encoding="utf-8"))},
        "case_schema": json.loads((RULES / "v3" / "case-fingerprint.schema.json").read_text(encoding="utf-8")),
        "facts_schema": json.loads((REPO / "apd" / "facts.schema.json").read_text(encoding="utf-8")),
        "delta_schema": json.loads((RULES / "v3.4" / "authorized-delta.schema.json").read_text(encoding="utf-8")),
        "ceilings": ceilings,
        "verbs": verbs,
        "banned": banned,
        "blocks": {k: v.text for k, v in template_engine.BLOCKS.items()},
        "templates": {k: {"required": list(v.required), "optional": list(v.optional), "block_required": dict(v.block_required)} for k, v in template_engine.TEMPLATES.items()},
        "block_families": {k: list(v) for k, v in template_engine.BLOCK_FAMILIES.items()},
        "skill_manifest": manifest,
        "skill_sources": sources,
        "auditor_md": (REPO / "apd" / "AUDITOR.md").read_text(encoding="utf-8"),
        # Validadores aprobados por Eric: el artefacto comprueba las mismas reglas
        # por código que la línea de comandos, o la paridad sería una mentira.
        "validators": [json.loads(l) for f in sorted((RULES / "v3" / "validators").glob("*.jsonl"))
                       for l in f.read_text(encoding="utf-8").splitlines() if l.strip()
                       and json.loads(l).get("approved_by") == "user"],
        "sources_of_truth": {
            "verbs": str(golden.relative_to(root)) if golden else None,
            "banned": [str(p.relative_to(root)) for p in (dram, anti) if p],
            "ceilings": "visual-prompt-forge/adapters/_capabilities.json",
        },
    }
    OUT.write_text("window.APD_DATA = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(f"data.js: {OUT.stat().st_size/1e6:.1f} MB · {len(rules)} reglas · {len(manifest)} archivos de skill · {len(verbs)} verbos · {len(banned)} términos prohibidos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
