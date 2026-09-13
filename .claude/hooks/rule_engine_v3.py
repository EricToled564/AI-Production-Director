#!/usr/bin/env python3
"""Shared primitives for APD Rule Engine v3.

Design goals:
- KB exhaustivity is an OFFLINE property of a published ruleset.
- Runtime exhaustivity means every rule that MATCHES a validated case fingerprint
  is accounted for. No silent omission.
- Applicability uses three-valued logic: TRUE / FALSE / UNKNOWN. UNKNOWN closes
  the gate instead of being silently treated as FALSE.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

TRUE = "TRUE"
FALSE = "FALSE"
UNKNOWN = "UNKNOWN"
UNKNOWN_VALUES = {None, "UNKNOWN", "UNSPECIFIED", "OPEN", "TBD"}


def canonical_json(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_json(obj: Any) -> str:
    return hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def get_path(data: Any, path: str) -> tuple[bool, Any]:
    cur = data
    for part in path.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return False, None
    return True, cur


def is_unknown(v: Any) -> bool:
    if v is None:
        return True
    if isinstance(v, str):
        return v.strip().upper() in UNKNOWN_VALUES
    return False


def tri_not(v: str) -> str:
    return {TRUE: FALSE, FALSE: TRUE, UNKNOWN: UNKNOWN}[v]


def tri_all(vals: Iterable[str]) -> str:
    vals = list(vals)
    if any(v == FALSE for v in vals):
        return FALSE
    if any(v == UNKNOWN for v in vals):
        return UNKNOWN
    return TRUE


def tri_any(vals: Iterable[str]) -> str:
    vals = list(vals)
    if any(v == TRUE for v in vals):
        return TRUE
    if any(v == UNKNOWN for v in vals):
        return UNKNOWN
    return FALSE


def eval_leaf(case: dict[str, Any], leaf: dict[str, Any]) -> str:
    path = leaf.get("path")
    op = leaf.get("op", "eq")
    expected = leaf.get("value")
    exists, actual = get_path(case, path)

    if op == "exists":
        return TRUE if exists else FALSE
    if not exists or is_unknown(actual):
        return UNKNOWN

    if op == "eq":
        return TRUE if actual == expected else FALSE
    if op == "neq":
        return TRUE if actual != expected else FALSE
    if op == "in":
        if not isinstance(expected, list):
            raise ValueError("op=in requires list value")
        return TRUE if actual in expected else FALSE
    if op == "not_in":
        if not isinstance(expected, list):
            raise ValueError("op=not_in requires list value")
        return TRUE if actual not in expected else FALSE
    if op == "contains":
        if isinstance(actual, (list, tuple, set, str)):
            return TRUE if expected in actual else FALSE
        return FALSE
    if op == "intersects":
        if not isinstance(expected, list):
            raise ValueError("op=intersects requires list value")
        if not isinstance(actual, (list, tuple, set)):
            return FALSE
        return TRUE if set(actual).intersection(expected) else FALSE
    if op == "truthy":
        return TRUE if bool(actual) else FALSE
    if op == "falsy":
        return TRUE if not bool(actual) else FALSE
    if op == "regex":
        return TRUE if re.search(str(expected), str(actual), re.IGNORECASE) else FALSE
    if op in {"gt", "gte", "lt", "lte"}:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return FALSE
        if not isinstance(expected, (int, float)) or isinstance(expected, bool):
            raise ValueError(f"op={op} requires numeric value")
        if op == "gt": return TRUE if actual > expected else FALSE
        if op == "gte": return TRUE if actual >= expected else FALSE
        if op == "lt": return TRUE if actual < expected else FALSE
        return TRUE if actual <= expected else FALSE
    raise ValueError(f"unsupported condition op: {op}")


def eval_condition(case: dict[str, Any], cond: dict[str, Any] | None) -> str:
    if cond is None or cond == {}:
        return TRUE
    if "all" in cond:
        return tri_all(eval_condition(case, c) for c in cond["all"])
    if "any" in cond:
        return tri_any(eval_condition(case, c) for c in cond["any"])
    if "not" in cond:
        return tri_not(eval_condition(case, cond["not"]))
    if "path" in cond:
        return eval_leaf(case, cond)
    raise ValueError(f"invalid condition node: {cond}")


def condition_paths(cond: dict[str, Any] | None) -> set[str]:
    if not cond:
        return set()
    if "path" in cond:
        return {cond["path"]}
    out: set[str] = set()
    for key in ("all", "any"):
        for c in cond.get(key, []) or []:
            out |= condition_paths(c)
    if "not" in cond:
        out |= condition_paths(cond["not"])
    return out


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    out = []
    if not path.exists():
        return out
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError as e:
            raise ValueError(f"{path}:{n}: invalid JSONL: {e}") from e
    return out


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def flatten_rules(registries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for reg in registries:
        skill = reg.get("skill", "?")
        for r in reg.get("rules", []):
            rid = r["id"]
            if rid in seen:
                continue
            seen.add(rid)
            x = dict(r)
            x["skill"] = skill
            x["source_path"] = f"{skill}/{r['file']}"
            out.append(x)
    return out


def effective_rank(meta: dict[str, Any]) -> tuple[int, int]:
    """Higher wins only as a tie-breaker AFTER conditional matching.

    Explicit supersedes/conflict policies are preferred. Rank is intentionally
    simple and auditable; it must never make an UNKNOWN applicability disappear.
    """
    authority_rank = {
        "GLOBAL_HARD": 700,
        "PROJECT_LOCK": 650,
        "PIPELINE": 600,
        "SKILL": 500,
        "LEARNED_PRODUCTION": 475,
        "MODEL_ADAPTER": 450,
        "GUIDELINE": 300,
        "EXAMPLE": 100,
        "LEGACY": 0,
    }.get(meta.get("authority", "SKILL"), 400)
    return (int(meta.get("priority", 0)), authority_rank)


@dataclass
class MatchRecord:
    rule_id: str
    status: str  # APPLIES | NA | UNRESOLVED
    reason: str
    rule: dict[str, Any]
    metadata: dict[str, Any]


def match_rule(case: dict[str, Any], rule: dict[str, Any], meta: dict[str, Any]) -> MatchRecord:
    state = eval_condition(case, meta.get("when"))
    if state == TRUE:
        return MatchRecord(rule["id"], "APPLIES", "condition matched", rule, meta)
    if state == FALSE:
        return MatchRecord(rule["id"], "NA", "condition evaluated false", rule, meta)
    paths = sorted(condition_paths(meta.get("when")))
    unknown = []
    for p in paths:
        exists, v = get_path(case, p)
        if not exists or is_unknown(v):
            unknown.append(p)
    reason = "unknown case fields: " + ", ".join(unknown or paths)
    return MatchRecord(rule["id"], "UNRESOLVED", reason, rule, meta)
