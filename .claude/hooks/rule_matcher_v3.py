#!/usr/bin/env python3
"""Match every published rule against one validated Case Fingerprint.

Runtime exhaustivity = every published rule is evaluated. A rule is one of:
NA, APPLIES, SUPPRESSED, or UNRESOLVED. UNKNOWN never becomes NA silently.
Conflicting applicable rules require an explicit case-dependent conflict policy.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from rule_engine_v3 import eval_condition, match_rule, TRUE, FALSE, UNKNOWN, sha256_json


def incompatible(effects: set[str]) -> bool:
    hard = effects.intersection({"REQUIRE", "FORBID"})
    if hard == {"REQUIRE", "FORBID"}:
        return True
    if "FORBID" in effects and "RECOMMEND" in effects:
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Match APD ruleset to case fingerprint")
    ap.add_argument("--ruleset", required=True)
    ap.add_argument("--case", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    # Gate A: a Rule Match may never begin from an invalid Case Fingerprint.
    case_validator = Path(__file__).with_name("case_validate.py")
    cv = subprocess.run([sys.executable, str(case_validator), args.case, "--json"], capture_output=True, text=True)
    if cv.returncode != 0:
        print("RULE MATCH: FAIL — Case Fingerprint did not pass qualification gate")
        if cv.stdout.strip(): print(cv.stdout.strip())
        if cv.stderr.strip(): print(cv.stderr.strip())
        return 1

    rs = json.loads(Path(args.ruleset).read_text(encoding="utf-8"))
    case = json.loads(Path(args.case).read_text(encoding="utf-8"))
    if not rs.get("published"):
        print("RULE MATCH: FAIL — ruleset is not published")
        return 1

    records = []
    applies = []
    unresolved = []
    na = []
    nonnorm = []
    by_id = {}

    for item in rs["rules"]:
        rule, meta = item["rule"], item["metadata"]
        rid = rule["id"]
        by_id[rid] = item
        if meta["classification_status"] == "NON_NORMATIVE":
            rec = {"rule_id": rid, "status": "NA", "reason": "classified NON_NORMATIVE", "rule": rule, "metadata": meta}
            records.append(rec); nonnorm.append(rec); continue
        m = match_rule(case, rule, meta)
        rec = {"rule_id": rid, "status": m.status, "reason": m.reason, "rule": rule, "metadata": meta}
        records.append(rec)
        if m.status == "APPLIES": applies.append(rec)
        elif m.status == "UNRESOLVED": unresolved.append(rec)
        else: na.append(rec)

    # Explicit rule-to-rule supersession, only among rules that actually apply.
    active_ids = {r["rule_id"] for r in applies}
    suppressed = {}
    for r in applies:
        for loser in r["metadata"].get("supersedes", []):
            if loser in active_ids:
                suppressed[loser] = r["rule_id"]

    # Conditional conflict policies. They decide only after both rules match.
    conflicts = []
    groups = {}
    for r in applies:
        if r["rule_id"] in suppressed:
            continue
        key = r["metadata"].get("conflict_key")
        if key:
            groups.setdefault(key, []).append(r)

    for key, group in groups.items():
        effects = {r["metadata"]["effect"] for r in group}
        if not incompatible(effects):
            continue
        policy_matches = []
        policy_unknown = []
        for p in rs.get("conflict_policies", []):
            if p.get("conflict_key") != key:
                continue
            state = eval_condition(case, p.get("when", {}))
            if state == TRUE:
                policy_matches.append(p)
            elif state == UNKNOWN:
                policy_unknown.append(p)
        if len(policy_matches) != 1:
            conflicts.append({
                "conflict_key": key,
                "rule_ids": [r["rule_id"] for r in group],
                "effects": sorted(effects),
                "status": "UNRESOLVED",
                "reason": "expected exactly one matching conflict policy",
                "matching_policies": [p.get("id") for p in policy_matches],
                "unknown_policies": [p.get("id") for p in policy_unknown],
            })
            continue
        p = policy_matches[0]
        winner = p.get("winner_rule_id")
        if winner not in {r["rule_id"] for r in group}:
            conflicts.append({"conflict_key": key, "status": "UNRESOLVED", "reason": f"policy {p.get('id')} winner does not apply", "rule_ids": [r["rule_id"] for r in group]})
            continue
        for r in group:
            if r["rule_id"] != winner:
                suppressed[r["rule_id"]] = winner
        conflicts.append({"conflict_key": key, "status": "RESOLVED", "policy": p.get("id"), "winner_rule_id": winner, "rule_ids": [r["rule_id"] for r in group]})

    for rec in records:
        if rec["rule_id"] in suppressed and rec["status"] == "APPLIES":
            rec["status"] = "SUPPRESSED"
            rec["reason"] = f"suppressed by {suppressed[rec['rule_id']]}"

    active = [r for r in records if r["status"] == "APPLIES"]
    unresolved_conflicts = [c for c in conflicts if c["status"] == "UNRESOLVED"]
    status = "PASS" if not unresolved and not unresolved_conflicts else "FAIL"

    out = {
        "status": status,
        "case_id": case["case_id"],
        "case_sha256": sha256_json(case),
        "ruleset_version": rs["ruleset_version"],
        "ruleset_sha256": rs["ruleset_sha256"],
        "counts": {
            "rules_evaluated": len(records),
            "active": len(active),
            "na": sum(1 for r in records if r["status"] == "NA"),
            "suppressed": sum(1 for r in records if r["status"] == "SUPPRESSED"),
            "unresolved": len(unresolved),
            "unresolved_conflicts": len(unresolved_conflicts)
        },
        "conflicts": conflicts,
        "records": records,
        "active_rules": active,
    }
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"RULE MATCH: {status}")
    for k, v in out["counts"].items():
        print(f"  {k:22} {v}")
    if unresolved:
        print("  unresolved examples:")
        for r in unresolved[:8]:
            print(f"    {r['rule_id']} — {r['reason']} — {r['rule']['source_path']}")
    if unresolved_conflicts:
        print("  unresolved conflicts:")
        for c in unresolved_conflicts[:8]:
            print(f"    {c['conflict_key']}: {', '.join(c['rule_ids'])}")
    print(f"written: {args.out}")
    return 0 if status == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
