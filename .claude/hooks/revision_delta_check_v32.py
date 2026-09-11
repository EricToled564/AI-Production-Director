#!/usr/bin/env python3
"""Fail closed when a revision changes locked JSON paths outside an allowed delta."""
from __future__ import annotations
import argparse, json

def get(d,path):
    cur=d
    for p in path.split('.'):
        if not isinstance(cur,dict) or p not in cur: return None
        cur=cur[p]
    return cur

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--before',required=True); ap.add_argument('--after',required=True); ap.add_argument('--locked',required=True,help='JSON file containing array of locked dot paths'); ap.add_argument('--allow-change',action='append',default=[]); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    before=json.load(open(a.before)); after=json.load(open(a.after)); locks=json.load(open(a.locked)); allowed=set(a.allow_change)
    changed=[]; violations=[]
    for path in locks:
        b=get(before,path); n=get(after,path)
        if b!=n:
            changed.append({'path':path,'before':b,'after':n})
            if path not in allowed: violations.append(path)
    out={'status':'FAIL' if violations else 'PASS','changed_locked_fields':changed,'unauthorized_changes':violations,'allowed_changes':sorted(allowed)}
    print(json.dumps(out,ensure_ascii=False,indent=2) if a.json else out)
    raise SystemExit(1 if violations else 0)
if __name__=='__main__': main()
