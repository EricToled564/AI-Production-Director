#!/usr/bin/env python3
"""Canonical visual prompt template engine reconstructed from SW30 source.

Source requirements implemented:
- T1..T5 typed templates with ordered required sections.
- Creation uses section assembly; T5 uses Change/Preserve/Constraints semantics.
- T1 canonical four blocks are identity-locked: light_hard, skin_doc,
  usecase_doc, clean_doc.
- Unknown sections, missing sections, loose text where a named block is required,
  missing Notes, or metadata inside the prompt body raise TemplateViolation.
- Running this file with no args executes the required self-test.

This is SOURCE_RECONSTRUCTED, not a claim to reproduce a missing historical file.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Mapping


class TemplateViolation(ValueError):
    pass


@dataclass(frozen=True)
class Block:
    name: str
    text: str


@dataclass
class BuiltPrompt:
    type: str
    sections: dict[str, str]
    block_ids: dict[str, str]
    metadata: dict[str, Any]
    references: list[str]
    prompt: str
    notes: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def delivery_text(self) -> str:
        m = self.metadata
        header = [
            f"Model: {m.get('model', '')}",
            f"Quality: {m.get('quality', '')}",
            f"Size / Ratio: {m.get('size_or_ratio', '')}",
            "References: " + (", ".join(self.references) if self.references else "none"),
            "Prompt:",
            self.prompt,
            "Notes:",
            self.notes,
        ]
        return "\n".join(header).rstrip() + "\n"


# Only canonical literal content explicitly specified by the original SW30 source
# is supplied as defaults. Project/case-specific blocks must be passed explicitly.
BLOCKS: dict[str, Block] = {
    "light_hard": Block(
        "light_hard",
        "Hard grazing light with no fill; surface microtexture casts visible local shadow. No softbox flattening.",
    ),
    "skin_doc": Block(
        "skin_doc",
        "Concrete documentary skin detail: uneven pigment, redness, dry patches, sweat, individual facial hairs and naturally chapped lip texture where visible.",
    ),
    "usecase_doc": Block(
        "usecase_doc",
        "Documentary reportage photograph with Kodak Tri-X character; avoid beauty-oriented skin softening.",
    ),
    "clean_doc": Block(
        "clean_doc",
        "No beauty retouching, no skin smoothing, no even complexion, no soft fill light.",
    ),
}


@dataclass(frozen=True)
class TemplateSpec:
    required: tuple[str, ...]
    optional: tuple[str, ...]
    block_required: Mapping[str, str | None]

    @property
    def allowed(self) -> set[str]:
        return set(self.required) | set(self.optional)


TEMPLATES: dict[str, TemplateSpec] = {
    "T1": TemplateSpec(
        required=("scene", "subject", "light", "skin", "usecase", "clean", "notes"),
        optional=("anatomy", "idlock", "optics", "colour", "hair", "fabric", "mood", "constraints", "references"),
        block_required={"light": "light_hard", "skin": "skin_doc", "usecase": "usecase_doc", "clean": "clean_doc"},
    ),
    "T2": TemplateSpec(
        required=("scene", "subject", "anatomy", "usecase", "notes"),
        optional=("idlock", "optics", "skin", "colour", "hair", "fabric", "mood", "clean", "constraints", "references"),
        block_required={"anatomy": None},
    ),
    "T3": TemplateSpec(
        required=("scene", "subject", "anatomy", "usecase", "notes"),
        optional=("idlock", "optics", "skin", "colour", "hair", "fabric", "mood", "clean", "constraints", "references"),
        block_required={"anatomy": None},
    ),
    "T4": TemplateSpec(
        required=("scene", "subject", "anatomy", "contact", "usecase", "notes"),
        optional=("idlock", "optics", "skin", "colour", "hair", "fabric", "mood", "clean", "constraints", "references"),
        block_required={"anatomy": None, "contact": None},
    ),
    "T5": TemplateSpec(
        required=("change", "preserve", "notes"),
        optional=("constraints", "idlock", "text_lock", "autocontain", "references"),
        block_required={},
    ),
}

BLOCK_FAMILIES = {
    "optics": ("optics_",),
    "skin": ("skin_",),
    "anatomy": ("anatomy", "anatomy_"),
    "idlock": ("idlock", "idlock_"),
    "text_lock": ("text_lock", "text_lock_"),
    "contact": ("contact_", "contact"),
    "unique": ("unique", "unique_"),
    "colour": ("colour", "colour_", "color", "color_"),
    "hair": ("hair", "hair_"),
    "fabric": ("fabric", "fabric_"),
    "clean": ("clean_",),
    "autocontain": ("autocontain_", "autocontain"),
}

META_RE = re.compile(
    r"(?im)^\s*(?:model|quality|size|aspect\s*ratio|size\s*/\s*ratio)\s*:\s*|\b--ar\b"
)


def block(name: str, text: str | None = None) -> Block:
    if name in BLOCKS and text is None:
        return BLOCKS[name]
    if not text or not text.strip():
        raise TemplateViolation(f"Block {name!r} requires non-empty text")
    return Block(name=name, text=text.strip())


def _block_name_allowed(section: str, name: str) -> bool:
    prefixes = BLOCK_FAMILIES.get(section)
    if not prefixes:
        return True
    return any(name == p or name.startswith(p) for p in prefixes)


def _render_creation(values: dict[str, str]) -> str:
    order = ["scene", "subject", "anatomy", "contact", "idlock", "optics", "light", "skin", "colour", "hair", "fabric", "mood", "usecase", "clean", "constraints", "autocontain", "text_lock"]
    return "\n\n".join(values[k].strip() for k in order if values.get(k, "").strip())


def _render_edit(values: dict[str, str]) -> str:
    chunks = [f"Change: {values['change'].strip()}", f"Preserve: {values['preserve'].strip()}"]
    if values.get("constraints", "").strip():
        chunks.append(f"Constraints: {values['constraints'].strip()}")
    for k in ("idlock", "text_lock", "autocontain"):
        if values.get(k, "").strip():
            chunks.append(values[k].strip())
    return "\n".join(chunks)


def build(
    tipo: str,
    *,
    metadata: Mapping[str, Any] | None = None,
    references: list[str] | None = None,
    **sections: str | Block | list[str],
) -> BuiltPrompt:
    tipo = tipo.upper()
    if tipo not in TEMPLATES:
        raise TemplateViolation(f"Unknown template type {tipo!r}; expected one of {sorted(TEMPLATES)}")
    spec = TEMPLATES[tipo]

    supplied = set(sections)
    unknown = supplied - spec.allowed
    if unknown:
        raise TemplateViolation(f"{tipo}: undeclared section(s): {', '.join(sorted(unknown))}")
    missing = [s for s in spec.required if s not in sections or sections[s] in (None, "", [])]
    if missing:
        raise TemplateViolation(f"{tipo}: missing required section(s): {', '.join(missing)}")

    refs = list(references or [])
    if "references" in sections:
        r = sections.pop("references")
        if isinstance(r, list):
            refs.extend(str(x) for x in r)
        elif isinstance(r, str) and r.strip():
            refs.append(r.strip())
        else:
            raise TemplateViolation("references must be a string or list of strings")

    values: dict[str, str] = {}
    block_ids: dict[str, str] = {}
    for section, value in sections.items():
        if section == "notes":
            if isinstance(value, Block):
                raise TemplateViolation("Notes is delivery metadata and must be plain text, not a prompt block")
            values[section] = str(value).strip()
            continue
        required_block = spec.block_required.get(section, "__not_block_required__")
        if required_block != "__not_block_required__":
            if not isinstance(value, Block):
                target = required_block or f"{section} block"
                raise TemplateViolation(
                    f"{tipo}.{section} must come from BLOCKS/a named Block ({target}); edit the shared block instead of patching loose text"
                )
            if required_block and value.name != required_block:
                raise TemplateViolation(f"{tipo}.{section} requires block {required_block!r}, got {value.name!r}")
            if not required_block and not _block_name_allowed(section, value.name):
                raise TemplateViolation(f"{tipo}.{section}: block {value.name!r} does not belong to section family {section!r}")
            block_ids[section] = value.name
            values[section] = value.text.strip()
        else:
            if isinstance(value, Block):
                if not _block_name_allowed(section, value.name):
                    raise TemplateViolation(f"{tipo}.{section}: invalid block {value.name!r}")
                block_ids[section] = value.name
                values[section] = value.text.strip()
            else:
                values[section] = str(value).strip()

    notes = values.pop("notes").strip()
    if not notes:
        raise TemplateViolation(f"{tipo}: Notes block is mandatory")

    body = _render_edit(values) if tipo == "T5" else _render_creation(values)
    if META_RE.search(body):
        raise TemplateViolation("Model/Quality/Size/Aspect ratio metadata must stay outside the prompt body")

    meta = dict(metadata or {})
    return BuiltPrompt(tipo, values, block_ids, meta, refs, body, notes)


def _from_json(path: Path) -> BuiltPrompt:
    data = json.loads(path.read_text(encoding="utf-8"))
    tipo = data.pop("type")
    metadata = data.pop("metadata", {})
    references = data.pop("references", [])
    blocks = data.pop("blocks", {})
    sections = data.pop("sections", {})
    if data:
        raise TemplateViolation(f"Unknown top-level JSON keys: {sorted(data)}")
    for section, spec in blocks.items():
        if isinstance(spec, str):
            sections[section] = block(spec)
        else:
            sections[section] = block(spec["name"], spec.get("text"))
    return build(tipo, metadata=metadata, references=references, **sections)


def selftest() -> int:
    passed = 0
    def expect_fail(label: str, fn):
        nonlocal passed
        try:
            fn()
        except TemplateViolation:
            passed += 1
            print(f"ok  {label}")
        else:
            print(f"FAIL {label}: expected TemplateViolation")
            raise AssertionError(label)

    expect_fail("unknown type rejected", lambda: build("T9", scene="x"))
    expect_fail("missing section rejected", lambda: build("T3", scene="x", subject="y", notes="n"))
    expect_fail(
        "loose anatomy rejected",
        lambda: build("T3", scene="x", subject="y", anatomy="loose", usecase="editorial", notes="n"),
    )
    expect_fail(
        "T1 canonical block cannot be substituted",
        lambda: build("T1", scene="x", subject="y", light=block("light_soft", "soft"), skin=block("skin_doc"), usecase=block("usecase_doc"), clean=block("clean_doc"), notes="n"),
    )
    expect_fail(
        "metadata in body rejected",
        lambda: build("T3", scene="Aspect Ratio: 16:9", subject="y", anatomy=block("anatomy", "coherent"), usecase="editorial", notes="n"),
    )
    good = build(
        "T3",
        metadata={"model": "nano-banana-pro", "quality": "high", "size_or_ratio": "16:9"},
        scene="Clay court, low camera.",
        subject="One male professional tennis player.",
        anatomy=block("anatomy", "Natural human proportions and coherent joints."),
        usecase="Editorial sports photograph.",
        notes="No visual reference sent to generator.",
    )
    assert "Aspect Ratio:" not in good.prompt
    assert good.notes
    passed += 1
    print("ok  valid T3 builds")
    print(f"SELFTEST PASS — {passed}/6")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", type=Path, help="JSON build spec")
    ap.add_argument("--json", action="store_true", help="emit artifact JSON")
    args = ap.parse_args()
    if not args.build:
        return selftest()
    try:
        artifact = _from_json(args.build)
    except (TemplateViolation, KeyError, json.JSONDecodeError) as e:
        print(f"TemplateViolation: {e}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(artifact.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(artifact.delivery_text(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
