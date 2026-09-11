#!/usr/bin/env python3
"""Validate a Case Fingerprint before any rule matching.

This gate checks schema + deterministic cross-field invariants. It does not try
to infer the case from natural language. The LLM/UI may propose a fingerprint,
but this script decides whether the structured object is internally valid.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema required", file=sys.stderr)
    raise SystemExit(2)

DEFAULT_SCHEMA = Path(__file__).resolve().parent.parent / "rules" / "v3" / "case-fingerprint.schema.json"


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate APD case fingerprint")
    ap.add_argument("case")
    ap.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    case = json.loads(Path(args.case).read_text(encoding="utf-8"))
    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    errors = []
    warnings = []

    validator = jsonschema.Draft202012Validator(schema)
    for e in sorted(validator.iter_errors(case), key=lambda x: list(x.path)):
        path = ".".join(map(str, e.path)) or "$"
        errors.append(f"schema {path}: {e.message}")

    if not errors:
        bt = case["base_type"]
        subj = case["subject"]
        op = case["operation"]
        stage = case["stage"]
        comp = case["composition"]
        phys = case["physics"]
        refs = case["references"]
        brand = case["brand"]

        if bt == "T3" and not (subj["count"] == 1 and subj["human"] is True):
            errors.append("T3 requires subject.count=1 and subject.human=true")
        if bt == "T4" and not (isinstance(subj["count"], int) and subj["count"] >= 2 and subj["human"] is True):
            errors.append("T4 requires at least two human subjects")
        if bt == "T5" and op not in {"image_edit", "image_to_image"}:
            errors.append("T5 requires an image editing operation")
        if subj["human_contact"] is True and (not isinstance(subj["count"], int) or subj["count"] < 2):
            errors.append("human_contact=true requires at least two subjects")
        if subj["identity_fidelity"] == "exact" and refs["identity_reference"] is not True:
            errors.append("exact identity fidelity requires references.identity_reference=true")
        if brand["mode"] in {"locked", "strict"} and not brand["brand_lock_ref"]:
            errors.append("locked/strict brand mode requires brand_lock_ref")
        if comp["split_level"] is True:
            if phys["water"] is not True:
                errors.append("split_level=true requires physics.water=true")
            if comp["waterline_visible"] is not True:
                errors.append("split_level=true requires waterline_visible=true")
        if comp["waterline_visible"] is True and phys["water"] is not True:
            errors.append("waterline_visible=true requires physics.water=true")
        if case["motion"]["static_frame"] is True and op in {"text_to_video", "image_to_video", "video_edit"}:
            errors.append("video generation/edit cannot have motion.static_frame=true")
        if stage in {"prompt", "generation"} and case["generator"]["family"] == "UNKNOWN":
            errors.append("prompt/generation stage requires a known generator family")
        task = case["task"]
        audio = case["audio"]
        seq = case["sequence"]
        if audio["dialogue_required"] is True and case["media"] != "video":
            errors.append("dialogue_required=true requires media=video")
        if audio["lipsync"] is True and audio["dialogue_required"] is not True:
            errors.append("lipsync=true requires dialogue_required=true")
        if isinstance(audio["speaker_count"], int) and audio["speaker_count"] > 0 and audio["dialogue_required"] is not True:
            errors.append("speaker_count>0 requires dialogue_required=true")
        if seq["multi_shot"] is True and isinstance(seq["shot_count"], int) and seq["shot_count"] < 2:
            errors.append("multi_shot=true requires shot_count>=2")
        if seq["multi_shot"] is False and isinstance(seq["shot_count"], int) and seq["shot_count"] != 1:
            errors.append("multi_shot=false requires shot_count=1")
        if task["family"] == "race_speed" and case["media"] != "video":
            warnings.append("task.family=race_speed is normally video; confirm this is intentional")
        pc = case["prompt_case"]
        if stage in {"prompt", "generation"} and case["media"] in {"image", "video"} and pc == "NONE":
            errors.append("visual prompt/generation requires prompt_case classification")
        if pc == "1" and not (case["media"] == "image" and op == "text_to_image" and refs["mode"] == "none"):
            errors.append("prompt_case=1 requires image text_to_image with references.mode=none")
        if pc == "2" and not (case["media"] == "image" and refs["mode"] in {"partial", "full"}):
            errors.append("prompt_case=2 requires image with references")
        if pc == "3a" and not (case["media"] == "video" and op == "image_to_video" and seq["start_frame_ref"] is True and seq["end_frame_ref"] is False):
            errors.append("prompt_case=3a requires I2V with start frame only")
        if pc == "3b" and not (case["media"] == "video" and op == "image_to_video" and seq["start_frame_ref"] is True and seq["end_frame_ref"] is True):
            errors.append("prompt_case=3b requires I2V with start and end frames")
        if pc == "3c" and not (case["media"] == "video" and seq["motion_reference"] is True):
            errors.append("prompt_case=3c requires video with motion_reference=true")
        if pc == "4" and not (case["media"] == "video" and audio["dialogue_required"] is True):
            errors.append("prompt_case=4 requires video dialogue")

        declared_unknowns = {x["path"] for x in case.get("unknowns", [])}
        blocking_unknowns = [x for x in case.get("unknowns", []) if x["blocking"]]
        if blocking_unknowns:
            errors.append("blocking unknowns remain: " + ", ".join(x["path"] for x in blocking_unknowns))

        # Important delivery context can be intentionally unknown at early stages,
        # but at prompt/generation it must be resolved or explicitly defaulted.
        if stage in {"prompt", "generation"} and case["media"] == "image":
            if not case["deliverable"]["aspect_ratio"]:
                errors.append("image prompt/generation requires deliverable.aspect_ratio")
            if case["deliverable"]["purpose"] == "UNKNOWN":
                warnings.append("deliverable.purpose is UNKNOWN; prompt may be technically valid but under-directed")

        # Warn when explicit UNKNOWN values are not documented in unknowns.
        def walk(obj, prefix=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    p = f"{prefix}.{k}" if prefix else k
                    yield from walk(v, p)
            elif isinstance(obj, list):
                return
            else:
                if obj == "UNKNOWN":
                    yield prefix
        silent_unknowns = [p for p in walk(case) if p not in declared_unknowns]
        if silent_unknowns:
            warnings.append("UNKNOWN values not documented in unknowns[]: " + ", ".join(silent_unknowns))

    result = {"status": "PASS" if not errors else "FAIL", "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"CASE VALIDATION: {result['status']}")
        for x in errors:
            print(f"  ERROR: {x}")
        for x in warnings:
            print(f"  WARN:  {x}")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
