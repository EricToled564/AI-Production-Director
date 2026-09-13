#!/usr/bin/env python3
"""Runtime exhaustivity gate over an already-resolved effective ruleset.

Every ACTIVE rule must have PASS, FAIL, or an explicit authorized OVERRIDE.
There is no N/A here: N/A belongs to matching, before the effective ruleset.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

VALID = {"PASS", "FAIL", "OVERRIDE"}


def main() -> int:
    ap = argparse.ArgumentParser(description="Runtime APD rule compliance ledger")
    ap.add_argument("--matched", required=True)
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    matched = json.loads(Path(args.matched).read_text(encoding="utf-8"))
    if matched.get("status") != "PASS":
        print("RUNTIME LEDGER: FAIL — rule matching is not PASS")
        return 1
    evidence = json.loads(Path(args.evidence).read_text(encoding="utf-8")) if Path(args.evidence).exists() else {}
    active = {r["rule_id"]: r for r in matched.get("active_rules", [])}

    pending, failed, malformed, passed, overridden = [], [], [], [], []
    for rid, rule in active.items():
        e = evidence.get(rid)
        if not e:
            pending.append(rid); continue
        st = str(e.get("status", "")).upper()
        if st not in VALID:
            malformed.append((rid, "invalid status")); continue
        if st == "PASS":
            if not e.get("by"):
                malformed.append((rid, "PASS requires by")); continue
            passed.append(rid)
        elif st == "FAIL":
            if not e.get("reason"):
                malformed.append((rid, "FAIL requires reason")); continue
            failed.append(rid)
        elif st == "OVERRIDE":
            if not e.get("reason") or not e.get("authorized_by"):
                malformed.append((rid, "OVERRIDE requires reason + authorized_by")); continue
            overridden.append(rid)

    stale = sorted(set(evidence) - set(active))
    status = "PASS" if not pending and not failed and not malformed else "FAIL"
    result = {
        "status": status,
        "active_rules": len(active),
        "pass": len(passed),
        "override": len(overridden),
        "fail": len(failed),
        "pending": len(pending),
        "malformed": len(malformed),
        "stale_evidence": len(stale),
        "pending_ids": pending,
        "failed_ids": failed,
        "malformed_items": malformed,
        "stale_ids": stale,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"RUNTIME LEDGER: {status}")
        for k in ("active_rules", "pass", "override", "fail", "pending", "malformed", "stale_evidence"):
            print(f"  {k:16} {result[k]}")
        for rid in pending[:8]:
            print(f"  PENDING {rid} — {active[rid]['rule']['text'][:120]}")
        for rid in failed[:8]:
            print(f"  FAIL    {rid} — {evidence[rid].get('reason','')}")
    return 0 if status == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
