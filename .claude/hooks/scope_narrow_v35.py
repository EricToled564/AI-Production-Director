#!/usr/bin/env python3
"""Reclasificacion de scope 3.4.0 -> 3.5.0.

Corrige el defecto medido en produccion: reglas que presuponen un pipeline de
storyboard (shots.json, brand-lock.snapshot.md, rondas, critiques) se activaban
para un brief de una sola imagen, donde ninguno de esos artefactos existe.

El estrechamiento se deriva de la seccion declarada de cada regla (skill, file,
headings), nunca de buscar palabras en el cuerpo: eso es lo que
.claude/rules/v3/README.md prohibe por producir falsos NA.

La condicion se une con "all" a la que la regla ya tenia, asi que solo puede
reducir el conjunto activo. UNKNOWN devuelve UNRESOLVED (logica ternaria), no NA.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / ".claude" / "rules" / "v3" / "build"
SRC = BUILD / "ruleset-3.4.0.json"
OUT = BUILD / "ruleset-3.5.0.json"

PIPELINE = {"op": "not_in", "path": "pipeline_track", "value": ["NONE"]}
SERIES = {"op": "eq", "path": "sequence.multi_shot", "value": True}
BRAND = {"op": "not_in", "path": "brand.mode", "value": ["none"]}
TEXT = {"op": "not_in", "path": "text.mode", "value": ["none"]}
NOT_NANO = {"op": "not_in", "path": "generator.family", "value": ["nano_banana"]}

TABLE = [
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > When to use",
     PIPELINE, "enumera los disparadores del skill, todos con shots.json o storyboard"),
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > What you produce",
     PIPELINE, "describe el arbol output/prompts/round-N del pipeline"),
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > Workflow > Step 1. Read inputs",
     PIPELINE, "exige shots.json y brand-lock.snapshot.md como entradas obligatorias"),
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > Workflow > Step 3. Compose per shot",
     PIPELINE, "compone desde brand-lock, series_lock y el registro del shot"),
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > Workflow > Step 4",
     PIPELINE, "escribe la ronda en el run.json del architect"),
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > Workflow > Step 5. Hand off",
     PIPELINE, "entrega el arbol de salida y ofrece el QA contra el storyboard"),
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > Revision mode",
     PIPELINE, "consume critiques por ronda producidos por visual-asset-critic"),
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > Quality bar",
     PIPELINE, "valida el archivo de prompts por shot, sus cabeceras y sus rondas"),
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > Hard rules > Rule 2. Brand colors",
     BRAND, "opera sobre la paleta del brand-lock"),
    ("visual-prompt-forge", "SKILL.md", "Visual Prompt Forge > Hard rules > Rule 3. Series_lock",
     SERIES, "los anchors de series_lock solo existen en una serie de shots"),
    ("visual-prompt-forge", "references/prompt-anatomy.md", "Prompt Anatomy: The Five Layers > Layer 1. Brand Lock",
     BRAND, "la capa 1 es el brand-lock"),
    ("visual-prompt-forge", "references/prompt-anatomy.md", "Prompt Anatomy: The Five Layers > Layer 4. Text Layer",
     TEXT, "la capa 4 es el texto en imagen"),
    ("visual-prompt-forge", "references/failure-modes.md", "Failure Modes > Failure 2. Character drift across shots",
     SERIES, "la deriva entre shots requiere varios shots"),
    ("visual-prompt-forge", "references/failure-modes.md", "Failure Modes > Failure 3. Text in image",
     TEXT, "trata el texto renderizado en la imagen"),
    ("visual-prompt-forge", "references/failure-modes.md", "Failure Modes > Failure 5. Composition doesn't reserve space",
     TEXT, "reserva espacio para el texto de la pieza"),
    ("visual-prompt-forge", "references/failure-modes.md", "Failure Modes > Failure 6. Series feels",
     SERIES, "compara shots de una misma serie"),
    ("visual-prompt-forge", "adapters/nano-banana.md", "Adapter: Nano Banana (Gemini 2.5 Flash Image) > Variant-generation",
     PIPELINE, "produce el set de variantes de un shot del pipeline"),
    ("visual-prompt-forge", "references/failure-modes.md", 'Failure Modes > Failure 1. The "AI look"',
     NOT_NANO, "APD 6.2: manda la sintaxis del modelo; image/references/nano-banana.md:24 y models.md:49 "
               "documentan que Nano Banana ignora lente y diafragma numericos"),
    ("ai-production-director", "SKILL.md", "AI Production Director > 2. Selección de track",
     PIPELINE, "elige el track de un proyecto audiovisual completo"),
    ("ai-production-director", "SKILL.md", "AI Production Director > 3. Las etapas",
     PIPELINE, "define las etapas del pipeline y sus gates"),
    ("ai-production-director", "SKILL.md", "AI Production Director > 4. Interacción con el usuario entre etapas",
     PIPELINE, "regula la entrega entre etapas del pipeline"),
    ("ai-production-director", "SKILL.md", "AI Production Director > 6. Reglas de resolución de conflictos > 6.3",
     PIPELINE, "fuente de verdad estructural de la Etapa 4 en adelante"),
    ("ai-production-director", "SKILL.md", "AI Production Director > 6. Reglas de resolución de conflictos > 6.4",
     PIPELINE, "reparto de duenos del flujo shots.json -> critique.json"),
]

BY_LINE = [
    ("produccion-visual-sw30", "SKILL.md", 142, PIPELINE,
     "R15: shots.json como fuente de verdad presupone un storyboard"),
]


def heading_of(rule):
    return " > ".join(rule.get("headings") or [])


def narrow(when, cond):
    if not when:
        return dict(cond)
    if isinstance(when, dict) and list(when.keys()) == ["all"]:
        return {"all": list(when["all"]) + [cond]}
    return {"all": [when, cond]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = json.loads(SRC.read_text(encoding="utf-8"))
    changes, unmatched = [], []

    for skill, file, head, cond, reason in TABLE:
        hit = 0
        for entry in data["rules"]:
            r = entry["rule"]
            if r["skill"] == skill and r["file"] == file and heading_of(r).startswith(head):
                entry["metadata"]["when"] = narrow(entry["metadata"].get("when"), cond)
                changes.append({"rule_id": r["id"], "section": skill + "/" + file + " :: " + head,
                                "condition": cond, "reason": reason})
                hit += 1
        if hit == 0:
            unmatched.append(skill + "/" + file + " :: " + head)

    for skill, file, line, cond, reason in BY_LINE:
        hit = 0
        for entry in data["rules"]:
            r = entry["rule"]
            if r["skill"] == skill and r["file"] == file and r["line"] == line:
                if any(c["rule_id"] == r["id"] for c in changes):
                    hit += 1
                    continue
                entry["metadata"]["when"] = narrow(entry["metadata"].get("when"), cond)
                changes.append({"rule_id": r["id"], "section": "%s/%s:%d" % (skill, file, line),
                                "condition": cond, "reason": reason})
                hit += 1
        if hit == 0:
            unmatched.append("%s/%s:%d" % (skill, file, line))

    print("reglas estrechadas: %d de %d" % (len(changes), len(data["rules"])))
    by_section = {}
    for c in changes:
        by_section[c["section"]] = by_section.get(c["section"], 0) + 1
    for sec, n in sorted(by_section.items(), key=lambda kv: -kv[1]):
        print("  %3d  %s" % (n, sec))
    if unmatched:
        print("SIN COINCIDENCIA (la tabla no corresponde al ruleset):")
        for u in unmatched:
            print("  " + u)
        return 1
    if args.dry_run:
        return 0

    data["ruleset_version"] = "3.5.0"
    data["scope_narrowing"] = {
        "base_version": "3.4.0",
        "base_ruleset_sha256": data.get("ruleset_sha256"),
        "authorized_by": "user",
        "reason": "brief de una sola imagen: las reglas del pipeline de storyboard no aplican",
        "generator": ".claude/hooks/scope_narrow_v35.py",
        "changes": changes,
    }
    data.pop("ruleset_sha256", None)
    payload = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    data["ruleset_sha256"] = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("escrito %s  sha256 %s" % (OUT.relative_to(ROOT), data["ruleset_sha256"][:16]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
