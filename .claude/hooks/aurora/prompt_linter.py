#!/usr/bin/env python3
"""Aurora Prompt Linter v1.2-fupai — copia parcheada del linter del skill
`aurora-prompt-linter` (v1.1, 2026-05-27) con vocabulario ampliado y las
contradicciones con el resto del pipeline resueltas a favor de la fuente.

Original (solo lectura, no se modifica):
  ~/.claude/skills/synced/<id>/aurora-prompt-linter/scripts/prompt_linter.py

Misma CLI que el original (--prompt --refs --case --platform --vocab --overrides
--sports-broadcast --json), mismos exit codes (0 PASS / 1 FAIL / 2 uso), más las
opciones nuevas --ref-role, --series-lock, --treatment.

CHANGELOG — cada parche cita la regla del skill que lo sustenta
================================================================
P1  Conteo de palabras: deja de ser HARD FAIL; pasa a WARN con el presupuesto por
    plataforma como referencia. Fuente: visual-prompt-forge/adapters/_capabilities.json
    (`max_prompt_words` es "a ceiling, not a target"), rangos de cada adaptador
    (kling 80-150, veo 80-150, gpt-image 150-300, nano-banana 60-120, midjourney
    40-80, flux 80-150, ideogram 60-120, seedream 40-70, hailuo 60-120, seedance
    80-150), kling.md §5/§10 (I2V 20-40), veo.md §3 (50-200) y §9 (comprimir a
    50-100), produccion-visual-sw30 "Template T1 ~250 palabras". El presupuesto
    original del caso (75-130 / 50-90) queda como referencia cuando la plataforma
    no está en la tabla.
P2  Bloque negativo obligatorio SOLO si la plataforma tiene campo negativo.
    Fuente: universal-rules U1 ("Negative constraints — only if the model supports
    them"), kling.md §6 (campo dedicado), seedance-25.md §7 y §19-A
    (`[Negative Prompts]`), seedance.md §12 (1.x/2.0 sin soporte fiable),
    veo.md §7 (positivo), image/golden-rules.md §2 (positive framing),
    image/gpt-image.md "5 slots" (Constraints: es el slot de exclusiones → cuenta
    como bloque negativo). Si el bloque existe se valida el formato SW30 R16:
    sin "no X" (kling.md §6 "Do not write 'no X'"), ≤8 ítems (kling.md §6 "Keep
    the list short", SW30 R16) → WARN.
P3  Identity block por rol de la referencia (--ref-role). La prohibición de
    descriptores P/O solo aplica con rol ff/lf (imagen a video: kling.md §3 y
    §10 "Do not re-describe static elements", veo.md §7, seedance.md §13,
    SW30 R5 y R16). Con rol character el identity block es obligatorio (U7
    "Anchor identity at the START of every prompt", seedance.md §10 "The full
    identity block must follow the @img1 mention", forge SKILL.md Rule 3 /
    consistency-locks Lock 1): si faltan ≥3 de {pelo, ojos/piel, prenda,
    accesorio, rasgo distintivo} → WARN "identity block absent".
P4  --series-lock: los términos del vocabulario que caen dentro de una cadena
    verbatim de series_lock (character/environment/lighting/color_grade) quedan
    exentos de la capa de redundancia. Fuente: forge SKILL.md Rule 3 ("flow into
    every prompt verbatim"), tools/validate_prompts.py (lo bloquea si NO están),
    consistency-locks.md Locks 1-3 y 8. Un linter que castiga lo que otro
    validador exige era una contradicción directa.
P5  Micro-acción corporal exenta de P: sweat, sweat bead, sweaty, jaw, jawline,
    knuckles, breath, exhale, swallow, tendon, vein, blink. Fuente: dramaturgy.md
    §2 ("Physical micro-action on the body. Jaw locks. Knuckles whiten..."),
    universal-rules U3 y §1 (Details Law), race-and-speed.md §1 ley 2 y §7
    ("sweat reads as discrete specular dots"). Salen de P y además existe
    BODY_MICRO_ACTION_EXEMPT que el código respeta aunque un vocab custom los
    vuelva a meter.
P6  "cinematic" sale de S y de TODOS los patrones de secciones requeridas y entra
    en BANNED, junto con professional, high quality, masterpiece, stunning,
    epic, amazing, beautiful lighting, dynamic camera, intense moment, powerful
    scene (dramaturgy.md §2 "What is banned", universal-rules §1) y la lista
    anti-slop de image/gpt-image.md (stunning, incredible, epic, gorgeous,
    masterpiece). Fuente de precedencia: ai-production-director §6.1 ("gana
    siempre").
P7  Bans de estilo condicionados al tratamiento (--treatment). anime / cartoon /
    3D render y similares solo se banean en fotorreal: image/references/patterns/
    character-design.md ("Anime-Style Character Card", "clean cel-shaded anime"),
    multi-panel.md ("Pixar-style 3D", "anime cel shading"), editing.md ("vibrant
    anime") los usan de forma legítima. "slow motion" deja de ser BANNED global:
    WARN en fotorreal (kling.md §11 lo recomienda como técnica anti-morphing;
    dramaturgy §7 exige razón), FAIL con --treatment race (race-and-speed.md §1
    ley 1 "never CGI-clean or sped-up... Over-crank... drain all threat"),
    permitido sin aviso con prefijo "ultra-" (kling.md §3 tempo words:
    "ultra-slow motion (2-3s feel)") o con OVERRIDE.
P8  --sports-broadcast solo aplica a casos de video (3a/3b/3c/4). En casos 1 y 2
    se ignora con WARN: la Regla 26 v6.0 del linter habla de "60fps" y
    "broadcast realism", que son parámetros de video (kling.md §2 "up to 60
    fps"); SW30 R8 prohíbe movimiento en stills ("frozen mid-stride").
P9  Casos del pipeline mapeados a los del linter: T1/T2/placa → 1; T3/T4/T5 con
    refs → 2; CLIP I2V → 3a/3b/3c; CLIP con diálogo → 4. Fuente: SW30
    "ARQUITECTURA POR SECCIONES" (tipos T1..T5), ai-production-director Etapa 5
    (casos de imagen) y Etapa 6 (clips). --case acepta ambos alfabetos.
P10 Vocabulario ampliado (L/PR/O para agua, automotriz, café/interior, clima,
    música) y snapshots de secciones para seedance_2.5, flux, ideogram, hailuo,
    seedream, nano_banana_2, kling 3.0 caso 4. Fuente: adaptadores de forge y
    archivos de modelo de `video` (kling.md §3, seedance-25.md §3-§7, veo.md §10).
    Reconoce también `Negative field.`, `[Negative Prompts]` y `Constraints:`.
P11 Mención negada no cuenta como violación de BANNED/estilo ("no cartoon", "not
    anime"): image/gpt-image.md ejemplo anti_style "no cartoon, no anime" vive en
    MAIN de forma legítima. Sigue siendo mala práctica en NB/GPT (golden-rules §2)
    pero eso lo cubre gate_image.py, no este linter.
P12 S vs secciones requeridas: si un ref carga S, el vocabulario de estilo queda
    prohibido en MAIN y a la vez la sección `style` lo exigía — imposible de
    satisfacer. Con S cubierto la sección `style` se dispensa y se reporta como
    WARN informativo. Fuente: universal-rules U13 ("Do not restate what a
    reference already defines"), seedance-25.md §5, consistency-locks Lock 6.
"""
import re
import sys
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Set, Tuple, Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml --break-system-packages", file=sys.stderr)
    sys.exit(2)

LINTER_VERSION = "v1.2-fupai"


@dataclass
class RefTag:
    file: str
    role: str
    tags: List[str]


@dataclass
class Override:
    term: str
    category: str
    reason: str
    source_text: str


@dataclass
class Violation:
    term: str
    category: str
    reason: str


@dataclass
class LinterResult:
    status: str
    case_type: str
    platform: str
    word_count: int
    word_budget: Tuple[int, int]
    covered_categories: List[str]
    sections_required: List[str]
    sections_present: List[str]
    sections_missing: List[str]
    violations: List[Violation]
    overrides_accepted: List[Override]
    warnings: List[str]
    suggestions: List[str]
    report: str
    # --- new in v1.2-fupai (added keys; original keys untouched) ---
    case_alias: str = ""
    treatment: str = "fotorreal"
    ref_role: str = ""
    ref_role_source: str = ""
    word_budget_source: str = ""
    negative_policy: str = ""
    negative_marker: str = ""
    series_lock_keys: List[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "status": self.status, "case_type": self.case_type, "platform": self.platform,
            "word_count": self.word_count, "word_budget": list(self.word_budget),
            "covered_categories": self.covered_categories,
            "sections_required": self.sections_required,
            "sections_present": self.sections_present,
            "sections_missing": self.sections_missing,
            "violations": [asdict(v) for v in self.violations],
            "overrides_accepted": [asdict(o) for o in self.overrides_accepted],
            "warnings": self.warnings, "suggestions": self.suggestions,
            "case_alias": self.case_alias, "treatment": self.treatment,
            "ref_role": self.ref_role, "ref_role_source": self.ref_role_source,
            "word_budget_source": self.word_budget_source,
            "negative_policy": self.negative_policy, "negative_marker": self.negative_marker,
            "series_lock_keys": self.series_lock_keys,
            "linter_version": LINTER_VERSION,
        }


# Original v1.1 budgets kept as the fallback reference (P1).
CASE_CONFIGS = {
    "1":  {"name": "Genesis (text-to-image)",  "budget": (75, 130)},
    "2":  {"name": "Anchor (image with refs)", "budget": (75, 130)},
    "3a": {"name": "I2V FF only",              "budget": (50, 90)},
    "3b": {"name": "I2V FF + LF",              "budget": (50, 90)},
    "3c": {"name": "I2V motion control",       "budget": (50, 90)},
    "4":  {"name": "Video with dialogue",      "budget": (75, 130)},
}
VIDEO_CASES = ("3a", "3b", "3c", "4")
I2V_CASES = ("3a", "3b", "3c")

# P9 — pipeline aliases → linter cases. Keys are upper-case with '-' separators.
CASE_ALIASES = {
    "1": "1", "T1": "1", "T2": "1", "PLACA": "1", "PLATE": "1", "GENESIS": "1", "T2I": "1",
    "2": "2", "T3": "2", "T4": "2", "T5": "2", "ANCLA": "2", "ANCHOR": "2",
    "3A": "3a", "CLIP": "3a", "CLIP-FF": "3a", "CLIP-I2V": "3a", "I2V": "3a", "FF": "3a",
    "3B": "3b", "CLIP-FF-LF": "3b", "CLIP-LF": "3b", "FF-LF": "3b", "CLIP-TAIL": "3b",
    "3C": "3c", "CLIP-MC": "3c", "CLIP-MOTION": "3c", "MOTION-CONTROL": "3c", "MC": "3c",
    "4": "4", "CLIP-DIALOGO": "4", "CLIP-DIALOG": "4", "CLIP-DIALOGUE": "4",
    "DIALOGO": "4", "DIALOGUE": "4", "CLIP-DIAL": "4",
}

TREATMENTS = ("fotorreal", "ilustracion", "animacion", "race")
REF_ROLES = ("ff", "lf", "character", "location", "prop", "style")

# P10 — platform families (forge _capabilities.json ids) and their default snapshot key.
FAMILY_PATTERNS = [
    ("nano-banana", r"^(nano_?banana|nbp\b|nb2\b)"),
    ("gpt-image",   r"^gpt_?image"),
    ("midjourney",  r"^(midjourney|mj\b)"),
    ("flux",        r"^flux"),
    ("ideogram",    r"^ideogram"),
    ("seedream",    r"^seedream"),
    ("kling",       r"^kling"),
    ("veo",         r"^veo"),
    ("seedance",    r"^seedance"),
    ("hailuo",      r"^hailuo"),
    ("sora",        r"^sora"),
]


def normalize_case(raw: str) -> Tuple[Optional[str], str]:
    """Return (linter case, alias as typed). None when unknown."""
    key = raw.strip().upper().replace("_", "-").replace(" ", "-")
    return CASE_ALIASES.get(key), raw.strip()


def normalize_tag(tag: str) -> str:
    m = re.match(r"^([A-Z]+)\d*$", str(tag).strip())
    return m.group(1) if m else str(tag)


def covered_categories(refs: List[RefTag]) -> Set[str]:
    cats = set()
    for ref in refs:
        for tag in ref.tags:
            cats.add(normalize_tag(tag))
    return cats


def normalize_platform_key(platform: str) -> str:
    p = platform.strip().lower().replace("-", "_").replace(" ", "_").replace(".", "_")
    p = re.sub(r"_(\d+)_(\d+)", r"_\1.\2", p)
    return p


def platform_info(platform: str) -> Dict[str, str]:
    norm = normalize_platform_key(platform) if platform else ""
    family = ""
    for fam, pat in FAMILY_PATTERNS:
        if norm and re.match(pat, norm):
            family = fam
            break
    ver_m = re.search(r"(\d+(?:\.\d+)?)", norm)
    version = ver_m.group(1) if ver_m else ""
    if family == "seedance":
        snapshot = "seedance_2.5" if version.startswith("2.5") else "seedance"
        budget_key = snapshot
    elif family == "nano-banana":
        snapshot = "nano_banana_2" if (re.search(r"(^|_)2(\b|_)", norm) and "pro" not in norm) else "nano_banana_pro"
        budget_key = family
    elif family == "kling":
        snapshot, budget_key = "kling_3.0", family
    elif family == "veo":
        snapshot, budget_key = "veo_3.1", family
    elif family == "gpt-image":
        snapshot, budget_key = "gpt_image_2", family
    elif family == "sora":
        snapshot, budget_key = "sora_2", family
    else:
        snapshot, budget_key = family.replace("-", "_"), family
    return {"normalized": norm, "family": family, "version": version,
            "snapshot": snapshot, "budget_key": budget_key}


def normalize_platform_case_key(platform: str, case_type: str) -> str:
    return f"{normalize_platform_key(platform)}__{case_type}"


# ----------------------------------------------------------------------------
# Prompt splitting (P2, P10): MAIN vs NEGATIVE block
# ----------------------------------------------------------------------------
NEGATIVE_MARKER = re.compile(
    r"(?i)(\[negative\s+prompts?\]|\bnegative(?:\s+(?:prompts?|field|constraints))?\s*[:.])")
CONSTRAINTS_MARKER = re.compile(r"(?im)^\s*constraints\s*:")


def split_main_and_negative(prompt: str, family: str = "") -> Tuple[str, str, str, str]:
    """Return (main, negative, marker_kind, marker_text). For the gpt-image family the
    `Constraints:` slot counts as the negative block (gpt-image.md, 5 slots). The marker
    text is returned so the required-sections check can still see the slot label."""
    candidates = []
    m = NEGATIVE_MARKER.search(prompt)
    if m:
        candidates.append((m.start(), m.end(), "negative"))
    if family == "gpt-image":
        c = CONSTRAINTS_MARKER.search(prompt)
        if c:
            candidates.append((c.start(), c.end(), "constraints"))
    if not candidates:
        return prompt, "", "", ""
    start, end, kind = min(candidates)
    return prompt[:start], prompt[end:], kind, prompt[start:end]


def word_count_of(text: str) -> int:
    return len(text.split())


def parse_negative_items(negative: str) -> List[str]:
    items = []
    for raw in re.split(r"[,;\n]", negative):
        it = raw.strip().strip("-•*").strip().rstrip(".")
        if it:
            items.append(it)
    return items


# ----------------------------------------------------------------------------
# Term matching helpers
# ----------------------------------------------------------------------------
def find_term_in_text(term: str, text: str) -> List[Tuple[int, int]]:
    text_lower, term_lower = text.lower(), term.lower()
    spans = []
    if " " in term_lower:
        start = 0
        while True:
            idx = text_lower.find(term_lower, start)
            if idx == -1:
                break
            spans.append((idx, idx + len(term_lower)))
            start = idx + 1
    else:
        for m in re.finditer(r"\b" + re.escape(term_lower) + r"\b", text_lower):
            spans.append((m.start(), m.end()))
    return spans


DIRECTIONAL_PREPOSITIONS = [
    "away from", "toward", "towards", "off", "over", "behind",
    "in front of", "across", "past", "from her", "from his",
    "onto", "into", "above", "below", "beside",
]


def is_in_motion_context(text: str, span: Tuple[int, int], motion_prefixes: List[str]) -> bool:
    start = max(0, span[0] - 60)
    window_full = text[start:span[1]].lower()
    window_before = text[start:span[0]].lower()
    for prefix in motion_prefixes:
        pat = r"\b" + re.escape(prefix.lower()) + r"\b[^.]{0,50}$"
        if re.search(pat, window_full):
            return True
    for prep in DIRECTIONAL_PREPOSITIONS:
        pat = r"\b" + re.escape(prep) + r"\s+(?:her\s+|his\s+|the\s+)?$"
        if re.search(pat, window_before):
            return True
    return False


NEGATION_BEFORE = re.compile(r"\b(no|not|never|avoid|without|non)[\s\-]+(?:\w+[\s\-]+){0,2}$")


def is_negated(text: str, span: Tuple[int, int]) -> bool:
    """P11 — 'no cartoon', 'not an anime look': a negated mention is not a delivery of the term."""
    before = text[max(0, span[0] - 40):span[0]].lower()
    return bool(NEGATION_BEFORE.search(before))


def in_any_span(span: Tuple[int, int], spans: List[Tuple[int, int]]) -> bool:
    return any(s <= span[0] and span[1] <= e for s, e in spans)


# ----------------------------------------------------------------------------
# Overrides (unchanged from v1.1)
# ----------------------------------------------------------------------------
OVERRIDE_PATTERN = re.compile(
    r"OVERRIDE\s*:\s*(?P<term>[^\-\n]+?)\s*[\-]+\s*(?P<reason>[^\n]+)",
    re.IGNORECASE
)


def parse_overrides(user_message: str) -> List[Override]:
    overrides = []
    for m in OVERRIDE_PATTERN.finditer(user_message):
        term = m.group("term").strip().strip('"\'')
        reason = m.group("reason").strip()
        is_cat = bool(re.match(r"^[A-Z]{1,2}\d*$", term))
        overrides.append(Override(term=term, category=normalize_tag(term) if is_cat else "",
                                  reason=reason, source_text=m.group(0)))
    return overrides


def override_matches(v: Violation, overrides: List[Override]) -> Optional[Override]:
    for ovr in overrides:
        if ovr.term.lower() == v.term.lower():
            return ovr
        if ovr.category and ovr.category == v.category:
            return ovr
    return None


# ----------------------------------------------------------------------------
# Series lock (P4)
# ----------------------------------------------------------------------------
SERIES_LOCK_KEYS = ("character", "environment", "lighting", "color_grade")


def load_series_lock(path: Optional[str]) -> Dict[str, str]:
    if not path:
        return {}
    raw = Path(path).read_text(encoding="utf-8")
    data = yaml.safe_load(raw)  # YAML is a superset of JSON
    if isinstance(data, dict) and isinstance(data.get("series_lock"), dict):
        data = data["series_lock"]
    out: Dict[str, str] = {}
    if isinstance(data, dict):
        for k in SERIES_LOCK_KEYS:
            v = data.get(k)
            if isinstance(v, str) and v.strip():
                out[k] = v.strip()
    return out


def series_lock_spans(main: str, series_lock: Dict[str, str]) -> Tuple[List[Tuple[int, int]], List[str]]:
    spans: List[Tuple[int, int]] = []
    missing: List[str] = []
    low = main.lower()
    for key, value in series_lock.items():
        v = value.lower()
        idx, found = 0, False
        while True:
            i = low.find(v, idx)
            if i == -1:
                break
            spans.append((i, i + len(v)))
            found = True
            idx = i + 1
        if not found:
            missing.append(key)
    return spans, missing


# ----------------------------------------------------------------------------
# Ref role (P3)
# ----------------------------------------------------------------------------
FF_ROLES = {"FF", "START", "FIRST", "FIRST_FRAME", "START_IMAGE"}
LF_ROLES = {"LF", "TAIL", "LAST", "LAST_FRAME", "TAIL_IMAGE", "END", "END_FRAME"}
CHAR_ROLES = {"CHARACTER", "CHAR", "ELEMENT", "IMG", "CREF", "REF", "OMNI", "IDENTITY", "@IMG"}


def person_refs(refs: List[RefTag]) -> List[RefTag]:
    return [r for r in refs if any(normalize_tag(t) in ("P", "O") for t in r.tags)]


def effective_ref_role(refs: List[RefTag], case_type: str, cli_role: str) -> Tuple[str, str]:
    if cli_role:
        return cli_role, "--ref-role"
    prefs = person_refs(refs)
    if not prefs:
        return "", "no person (P/O) refs"
    roles = {str(r.role).strip().upper() for r in prefs}
    if roles & FF_ROLES:
        return "ff", "refs.yaml role"
    if roles & LF_ROLES:
        return "lf", "refs.yaml role"
    if roles & CHAR_ROLES:
        return "character", "refs.yaml role"
    if case_type in VIDEO_CASES:
        return "ff", "default for video case (I2V)"
    return "character", "default for case 1/2 (refs @img / Elements)"


def identity_groups_present(main: str, groups: Dict[str, List[str]]) -> List[str]:
    present = []
    for name, terms in (groups or {}).items():
        for t in terms or []:
            if find_term_in_text(str(t), main):
                present.append(name)
                break
    return present


# ----------------------------------------------------------------------------
# Sections (P6, P7, P10)
# ----------------------------------------------------------------------------
def resolve_section_specs(platform: str, pinfo: Dict[str, str], case_type: str,
                          vocabs: Dict, treatment: str,
                          covered: Optional[Set[str]] = None) -> Tuple[Optional[Dict], str, List[str]]:
    """Return (section specs, snapshot key, waived section names).

    A section is waived when a reference already carries what it asks for: with an S
    (style) ref the `style` section is dropped, because the S vocabulary is banned in
    MAIN for that very reason (U13 "Do not restate what a reference already defines").
    """
    sections_db = vocabs.get("REQUIRED_SECTIONS_BY_PLATFORM_CASE", {}) or {}
    covered = covered or set()
    waived: List[str] = []
    candidates = []
    if pinfo["normalized"]:
        candidates.append(f"{pinfo['normalized']}__{case_type}")
    if pinfo["snapshot"]:
        candidates.append(f"{pinfo['snapshot']}__{case_type}")
    if pinfo["family"]:
        candidates.append(f"{pinfo['family'].replace('-', '_')}__{case_type}")
    for key in candidates:
        if key in sections_db and sections_db[key]:
            specs = dict(sections_db[key])
            overrides = (vocabs.get("TREATMENT_SECTION_OVERRIDES", {}) or {}).get(treatment, {}) or {}
            for name, pats in overrides.items():
                if name in specs:
                    if pats is None:
                        specs.pop(name)
                    else:
                        specs[name] = list(pats)
            if "S" in covered:
                for name in [n for n in specs if n == "style"]:
                    specs.pop(name)
                    waived.append(name)
            return specs, key, waived
    return None, (candidates[0] if candidates else normalize_platform_case_key(platform, case_type)), waived


def validate_sections(prompt_main: str, section_specs: Optional[Dict]) -> Tuple[List[str], List[str], List[str]]:
    if not section_specs:
        return [], [], []
    required, present, missing = list(section_specs.keys()), [], []
    main_lower = prompt_main.lower()
    for section_name, patterns in section_specs.items():
        if any(str(pat).lower() in main_lower for pat in (patterns or [])):
            present.append(section_name)
        else:
            missing.append(section_name)
    return required, present, missing


# ----------------------------------------------------------------------------
# Word budget (P1) and negative policy (P2)
# ----------------------------------------------------------------------------
def resolve_word_budget(pinfo: Dict[str, str], case_type: str, vocabs: Dict) -> Tuple[Tuple[int, int], str, Optional[int]]:
    table = vocabs.get("WORD_BUDGET_BY_PLATFORM", {}) or {}
    entry = None
    for key in (pinfo.get("snapshot"), pinfo.get("budget_key"), pinfo.get("family")):
        if key and key in table:
            entry = table[key]
            break
    if entry:
        rng = entry.get("default")
        if case_type in I2V_CASES and entry.get("i2v"):
            rng = entry["i2v"]
        lo, hi = int(rng[0]), int(rng[1])
        return (lo, hi), str(entry.get("source", "")), entry.get("ceiling")
    cfg = CASE_CONFIGS[case_type]["budget"]
    return cfg, "linter v1.1 case budget (platform not in WORD_BUDGET_BY_PLATFORM) — reference only", None


def resolve_negative_policy(pinfo: Dict[str, str], vocabs: Dict) -> str:
    table = vocabs.get("NEGATIVE_BLOCK_POLICY", {}) or {}
    for key in (pinfo.get("snapshot"), pinfo.get("budget_key"), pinfo.get("family")):
        if key and key in table:
            return str(table[key])
    return "legacy_required"


# ----------------------------------------------------------------------------
# Main validation
# ----------------------------------------------------------------------------
def validate(refs, prompt, case_type, platform, vocabs, overrides,
             require_sports_broadcast=False, treatment="fotorreal",
             ref_role="", series_lock=None, case_alias="") -> LinterResult:
    config = CASE_CONFIGS.get(case_type)
    if not config:
        return LinterResult(status="FAIL", case_type=case_type, platform=platform,
            word_count=0, word_budget=(0, 0), covered_categories=[],
            sections_required=[], sections_present=[], sections_missing=[],
            violations=[], overrides_accepted=[], warnings=[], suggestions=[],
            report=f"ERROR: Unknown case_type {case_type}")

    series_lock = series_lock or {}
    pinfo = platform_info(platform)
    main, negative, neg_marker, neg_marker_text = split_main_and_negative(prompt, pinfo["family"])
    # The Constraints: label is a required slot for gpt-image (gpt-image.md "5 slots"); it is
    # split off as the negative block, so the section check sees the label again here.
    section_text = main + ("\n" + neg_marker_text if neg_marker == "constraints" else "")
    cats = covered_categories(refs)
    motion_prefixes = vocabs.get("ALLOWED_MOTION_PREFIXES", []) or []
    body_exempt = {str(t).lower() for t in (vocabs.get("BODY_MICRO_ACTION_EXEMPT", []) or [])}

    violations: List[Violation] = []
    overrides_accepted: List[Override] = []
    overrides_used: Set[str] = set()
    warnings: List[str] = []

    def record(v: Violation):
        ovr = override_matches(v, overrides)
        if ovr:
            if ovr.source_text not in overrides_used:
                overrides_accepted.append(ovr)
                overrides_used.add(ovr.source_text)
        else:
            violations.append(v)

    # P8 — sports broadcast only for video cases
    sports_active = require_sports_broadcast
    if require_sports_broadcast and case_type not in VIDEO_CASES:
        sports_active = False
        warnings.append(
            f"--sports-broadcast ignored for case {case_type} (still image): '60fps' and "
            f"'broadcast realism' are video parameters (kling.md §2, Regla 26 v6.0); "
            f"SW30 R8 forbids motion in stills")

    # P3 — effective role of the person refs
    role, role_source = effective_ref_role(refs, case_type, ref_role)
    po_banned = role in ("ff", "lf")
    if role in ("location", "prop", "style") and person_refs(refs):
        warnings.append(
            f"--ref-role {role} but refs carry P/O tags; P/O redundancy not enforced for this role "
            f"(only ff/lf ban re-description: kling.md §10, veo.md §7, seedance.md §13)")

    # P4 — series_lock verbatim spans
    sl_spans, sl_missing = series_lock_spans(main, series_lock)
    for k in sl_missing:
        warnings.append(
            f"series_lock.{k} not found verbatim in MAIN (forge Rule 3; validate_prompts.py "
            f"{'blocks' if k != 'character' else 'warns on'} this)")

    # Layer 1: refs redundancy
    for cat in sorted(cats):
        if cat in ("P", "O") and not po_banned:
            continue
        for term in vocabs.get(cat, []) or []:
            term = str(term)
            if term.lower() in body_exempt:
                continue
            for span in find_term_in_text(term, main):
                if is_in_motion_context(main, span, motion_prefixes):
                    continue
                if in_any_span(span, sl_spans):
                    continue
                record(Violation(term=term, category=cat,
                                 reason=f"Static descriptor of category {cat} (covered by refs; role={role or 'n/a'})"))
                break
    if cats & {"P", "O"} and not po_banned and role:
        warnings.append(
            f"P/O descriptors allowed: person ref role is '{role}' ({role_source}); "
            f"re-description ban applies only to ff/lf (kling.md §10, veo.md §7, seedance.md §13, SW30 R16)")

    # P3 — identity block required when role is character
    if role == "character":
        groups = vocabs.get("IDENTITY_BLOCK_GROUPS", {}) or {}
        present = identity_groups_present(main, groups)
        need = int(vocabs.get("IDENTITY_BLOCK_MIN_GROUPS", 3) or 3)
        if len(present) < need:
            warnings.append(
                f"identity block absent or thin: {len(present)}/{len(groups)} groups present "
                f"{sorted(present)}; need >= {need} of {sorted(groups.keys())} "
                f"(U7, seedance.md §10, forge Rule 3 / consistency-locks Lock 1)")

    # Layer 2: required sections by platform+case (P6/P7/P10)
    section_specs, section_key, sec_waived = resolve_section_specs(
        platform, pinfo, case_type, vocabs, treatment, cats)
    sec_req, sec_pres, sec_miss = validate_sections(section_text, section_specs)
    for w in sec_waived:
        warnings.append(
            f"Section '{w}' waived: category S is covered by a ref, and its vocabulary is banned in MAIN "
            f"(U13 'Do not restate what a reference already defines')")
    if not sec_req and platform:
        warnings.append(
            f"No required-sections snapshot for platform '{platform}' + case '{case_type}'. "
            f"Update vocabularies.yaml REQUIRED_SECTIONS_BY_PLATFORM_CASE.{section_key}")
    for ms in sec_miss:
        record(Violation(term=ms, category="SECTION",
                         reason=f"Required section '{ms}' for platform '{platform}' case {case_type} "
                                f"(snapshot {section_key}, treatment {treatment}) not detected in MAIN"))

    # Layer 3: banned vocab in MAIN (P6, P11)
    for term in vocabs.get("BANNED", []) or []:
        term = str(term)
        spans = [s for s in find_term_in_text(term, main) if not is_negated(main, s)]
        if spans:
            record(Violation(term=term, category="BANNED",
                             reason="Banned vocab in main prompt (dramaturgy §2 / gpt-image anti-slop; director §6.1 wins)"))

    # Layer 3b: style bans conditioned on treatment (P7)
    if treatment in ("fotorreal", "race"):
        for term in vocabs.get("STYLE_BANNED_FOTORREAL", []) or []:
            term = str(term)
            spans = [s for s in find_term_in_text(term, main) if not is_negated(main, s)]
            if spans:
                record(Violation(term=term, category="BANNED",
                                 reason=f"Non-photoreal style term in MAIN under treatment '{treatment}' "
                                        f"(move to NEGATIVE or use --treatment ilustracion/animacion)"))

    # Layer 3c: slow motion (P7)
    slow_terms = vocabs.get("SLOW_MOTION_TERMS", []) or []
    slow_prefixes = [str(p).lower() for p in (vocabs.get("SLOW_MOTION_ALLOWED_PREFIXES", []) or [])]
    slow_hit = None
    for term in slow_terms:
        for span in find_term_in_text(str(term), main):
            before = main[max(0, span[0] - 12):span[0]].lower()
            if any(before.endswith(p) for p in slow_prefixes):
                continue  # kling.md §3 tempo word "ultra-slow motion"
            if is_negated(main, span):
                continue
            slow_hit = str(term)
            break
        if slow_hit:
            break
    if slow_hit:
        if treatment == "race":
            record(Violation(term=slow_hit, category="BANNED",
                             reason="slow motion under --treatment race (race-and-speed.md §1 law 1: "
                                    "never over-crank / sped-up; authentic speed only)"))
        else:
            v = Violation(term=slow_hit, category="BANNED", reason="")
            ovr = override_matches(v, overrides)
            if ovr:
                if ovr.source_text not in overrides_used:
                    overrides_accepted.append(ovr)
                    overrides_used.add(ovr.source_text)
            else:
                warnings.append(
                    f"'{slow_hit}' in MAIN: allowed as technique (kling.md §11 anti-morphing) but needs a "
                    f"declared reason (dramaturgy §7); use 'ultra-slow motion' (kling.md §3 tempo) or "
                    f"OVERRIDE: {slow_hit} - <reason>")

    # Word count (P1) — WARN only
    wc_main = word_count_of(main)
    budget, budget_source, ceiling = resolve_word_budget(pinfo, case_type, vocabs)
    if wc_main > budget[1]:
        warnings.append(
            f"Word count {wc_main} above platform budget max {budget[1]}"
            f"{f' (ceiling {ceiling})' if ceiling else ''} — reference only, not blocking. "
            f"Source: {budget_source}")
    elif wc_main < budget[0]:
        warnings.append(
            f"Word count {wc_main} below platform budget min {budget[0]} (compression OK if intentional). "
            f"Source: {budget_source}")

    # Negative block (P2)
    neg_policy = resolve_negative_policy(pinfo, vocabs)
    neg_present = bool(negative.strip())
    if neg_policy in ("required", "legacy_required") and not neg_present:
        reason = ("Negative prompt block required: platform has a dedicated negative field "
                  "(kling.md §6 / seedance-25.md §7)")
        if neg_policy == "legacy_required":
            reason = ("Negative prompt block required (v1.1 rule kept: platform unknown or not "
                      "specified, so U1 'only if the model supports them' cannot be resolved)")
            warnings.append("Platform not resolved: negative-block requirement falls back to v1.1 "
                            "behaviour (required). Pass --platform to apply U1.")
        record(Violation(term="negative_prompt", category="STRUCTURE", reason=reason))
    if neg_present:
        items = parse_negative_items(negative)
        max_items = int(vocabs.get("NEGATIVE_MAX_ITEMS", 8) or 8)
        if len(items) > max_items:
            warnings.append(
                f"R16: negative block has {len(items)} items (> {max_items}). kling.md §6 'Keep the list "
                f"short. Long negative stacks reduce motion and detail'; SW30 R16 '≤8 ítems'")
        if pinfo["family"] == "kling":
            bad = [it for it in items if re.match(r"^(no|not|without|never)\b", it.strip().lower())]
            if bad:
                warnings.append(
                    f"R16: Kling negative field auto-interprets input as exclusion — do not write 'no X' "
                    f"(kling.md §6, SW30 R16). Rewrite as the thing itself: {bad[:5]}")
        if neg_policy == "optional" and pinfo["family"] in ("nano-banana", "gpt-image", "veo", "flux"):
            if neg_marker == "negative":
                warnings.append(
                    f"Negative block present on '{pinfo['family']}' which has no dedicated negative field; "
                    f"prefer positive framing (golden-rules §2, veo.md §7) or the Constraints: slot (gpt-image.md)")

    # Sports broadcast (unchanged, video cases only — P8)
    if sports_active:
        for kw in vocabs.get("REQUIRED_SPORTS_BROADCAST", []) or []:
            if str(kw).lower() not in main.lower():
                violations.append(Violation(term=str(kw), category="REQUIRED",
                    reason="Required keyword for sports broadcast (Regla 26 v6.1)"))

    status = "PASS" if not violations else "FAIL"

    # -------------------- report --------------------
    L = [
        "=" * 64,
        f"AURORA PROMPT LINTER REPORT {LINTER_VERSION}",
        "=" * 64,
        f"Case: {case_type} ({config['name']})" + (f" [alias {case_alias}]" if case_alias and case_alias != case_type else ""),
        f"Platform: {platform if platform else '(none specified)'}"
        + (f" -> family {pinfo['family']}, snapshot {pinfo['snapshot']}" if pinfo['family'] else ""),
        f"Treatment: {treatment}",
        f"Word count (MAIN): {wc_main} / budget {budget} [WARN only] — {budget_source}",
        f"Negative block: {'present' if neg_present else 'MISSING'} "
        f"(policy {neg_policy}{', marker ' + neg_marker if neg_marker else ''})",
        f"Categories covered by refs: {sorted(cats) if cats else '(none)'}",
        f"Person-ref role: {role or '(none)'} ({role_source}) -> P/O re-description {'BANNED' if po_banned else 'allowed'}",
        f"Series lock: {sorted(series_lock.keys()) if series_lock else '(none)'}",
        f"Sports broadcast mode: {'on' if sports_active else ('ignored' if require_sports_broadcast else 'off')}",
        ""
    ]
    if sec_req:
        L.append(f"REQUIRED SECTIONS for {platform} case {case_type} (snapshot {section_key}):")
        for s in sec_req:
            L.append(f"  {'PRESENT' if s in sec_pres else 'MISSING'} {s}")
        L.append("")
    if violations:
        L.append(f"VIOLATIONS ({len(violations)}):")
        for v in violations:
            L.append(f"  FAIL [{v.category}] '{v.term}' - {v.reason}")
    else:
        L.append("VIOLATIONS: none")
    if warnings:
        L.append("")
        L.append(f"WARNINGS ({len(warnings)}) non-blocking:")
        for w in warnings:
            L.append(f"  WARN {w}")
    if overrides_accepted:
        L.append("")
        L.append(f"OVERRIDES ACCEPTED ({len(overrides_accepted)}):")
        for o in overrides_accepted:
            L.append(f"  OK '{o.term}' - {o.reason[:100]}")
    suggestions: List[str] = []
    if violations:
        cat_vio: Dict[str, List[str]] = {}
        for v in violations:
            cat_vio.setdefault(v.category, []).append(v.term)
        for cat, terms in cat_vio.items():
            if cat in ("P", "O", "L", "PR", "S"):
                suggestions.append(f"Strip from MAIN: {terms} (category {cat} already covered by refs)")
            elif cat == "SECTION":
                suggestions.append(f"Add sections to MAIN: {terms} (required by platform '{platform}' case {case_type})")
            elif cat == "BANNED":
                suggestions.append(f"Move to NEGATIVE block or replace with concrete physical facts: {terms}")
            elif cat == "STRUCTURE":
                suggestions.append(f"Fix structure: {terms}")
            elif cat == "REQUIRED":
                suggestions.append(f"Add to MAIN: {terms}")
        L.append("")
        L.append("SUGGESTIONS:")
        for s in suggestions:
            L.append(f"  -> {s}")
    L.append("")
    L.append(f"STATUS: {status}")
    L.append("Delivery BLOCKED. Iterate or grant OVERRIDE in current turn." if status == "FAIL" else "Delivery PERMITTED.")
    L.append("=" * 64)

    return LinterResult(status=status, case_type=case_type, platform=platform,
        word_count=wc_main, word_budget=budget,
        covered_categories=sorted(cats), sections_required=sec_req,
        sections_present=sec_pres, sections_missing=sec_miss,
        violations=violations, overrides_accepted=overrides_accepted,
        warnings=warnings, suggestions=suggestions, report="\n".join(L),
        case_alias=case_alias, treatment=treatment, ref_role=role, ref_role_source=role_source,
        word_budget_source=budget_source, negative_policy=neg_policy, negative_marker=neg_marker,
        series_lock_keys=sorted(series_lock.keys()))


def load_refs(path: str) -> List[RefTag]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or []
    if isinstance(data, dict) and isinstance(data.get("refs"), list):
        data = data["refs"]
    refs = []
    for r in data:
        if not isinstance(r, dict):
            continue
        refs.append(RefTag(file=str(r.get("file", "")), role=str(r.get("role", "")),
                           tags=[str(t) for t in (r.get("tags") or [])]))
    return refs


def main():
    p = argparse.ArgumentParser(description=f"Aurora Prompt Linter {LINTER_VERSION} (FUPAI patched copy)")
    p.add_argument("--prompt", required=True)
    p.add_argument("--refs", required=True)
    p.add_argument("--case", required=True,
        help="Linter case (1, 2, 3a, 3b, 3c, 4) or pipeline alias (T1/T2/placa -> 1; T3/T4/T5 -> 2; "
             "CLIP-FF/I2V -> 3a; CLIP-FF-LF -> 3b; CLIP-MC -> 3c; CLIP-DIALOGO -> 4)")
    p.add_argument("--platform", default="",
        help="Platform identifier (e.g., gpt_image_2, kling_3.0, veo_3.1, nano_banana_pro, nano_banana_2, "
             "seedance_2.5, flux, ideogram, hailuo, seedream, midjourney, sora_2)")
    p.add_argument("--vocab", default=None)
    p.add_argument("--overrides", default=None)
    p.add_argument("--sports-broadcast", action="store_true")
    p.add_argument("--json", action="store_true")
    # --- new options ---
    p.add_argument("--ref-role", default="", choices=list(REF_ROLES) + [""],
        help="Role of the person reference(s): ff/lf ban P/O re-description (I2V); character requires an identity block")
    p.add_argument("--series-lock", default=None,
        help="JSON or YAML with verbatim series_lock strings (character/environment/lighting/color_grade); "
             "vocab terms inside them are exempt (forge Rule 3)")
    p.add_argument("--treatment", default="fotorreal", choices=list(TREATMENTS),
        help="fotorreal (default) bans anime/cartoon/3D render and warns on slow motion; ilustracion/animacion "
             "lift the style bans; race turns slow motion into FAIL")
    args = p.parse_args()

    case_type, case_alias = normalize_case(args.case)
    if case_type is None:
        p.error(f"argument --case: unknown case '{args.case}'. Accepted: {sorted(CASE_ALIASES.keys())}")

    prompt = Path(args.prompt).read_text(encoding="utf-8")
    refs = load_refs(args.refs)
    vocab_path = Path(args.vocab) if args.vocab else Path(__file__).parent / "vocabularies.yaml"
    vocabs = yaml.safe_load(vocab_path.read_text(encoding="utf-8")) or {}
    overrides = []
    if args.overrides:
        overrides = parse_overrides(Path(args.overrides).read_text(encoding="utf-8"))
    series_lock = load_series_lock(args.series_lock)
    result = validate(refs, prompt, case_type, args.platform, vocabs, overrides,
                      require_sports_broadcast=args.sports_broadcast,
                      treatment=args.treatment, ref_role=args.ref_role,
                      series_lock=series_lock, case_alias=case_alias)
    if args.json:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(result.report)
    sys.exit(0 if result.status == "PASS" else 1)


if __name__ == "__main__":
    main()
