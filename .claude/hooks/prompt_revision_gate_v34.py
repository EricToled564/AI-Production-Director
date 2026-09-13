#!/usr/bin/env python3
"""Prove that a revision changed nothing except the brief hash/revision counter.
The authorized delta affects rendered values through immutable AST bindings; the AST itself may not be rewritten.
"""
from __future__ import annotations
import argparse,copy,json
from pathlib import Path

def normalized(x):
    y=copy.deepcopy(x); y.pop('brief_hash',None); y.pop('prompt_revision',None); return y

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--before',required=True); ap.add_argument('--after',required=True); ap.add_argument('--old-brief',required=True); ap.add_argument('--new-brief',required=True); ap.add_argument('--delta',required=True); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    oldast=json.loads(Path(a.before).read_text(encoding='utf-8')); newast=json.loads(Path(a.after).read_text(encoding='utf-8')); oldb=json.loads(Path(a.old_brief).read_text(encoding='utf-8')); newb=json.loads(Path(a.new_brief).read_text(encoding='utf-8')); d=json.loads(Path(a.delta).read_text(encoding='utf-8'))
    errs=[]
    if oldast.get('brief_hash')!=oldb.get('brief_hash'): errs.append('before AST/brief mismatch')
    if newast.get('brief_hash')!=newb.get('brief_hash'): errs.append('after AST/brief mismatch')
    if d.get('base_brief_hash')!=oldb.get('brief_hash'): errs.append('delta base mismatch')
    if normalized(oldast)!=normalized(newast): errs.append('UNAUTHORIZED PROMPT DRIFT: AST content/model/parameters/templates changed')
    if int(newast.get('prompt_revision',1))!=int(oldast.get('prompt_revision',1))+1: errs.append('revision counter did not increment exactly once')
    out={'status':'FAIL' if errs else 'PASS','authorized_paths':[c['path'] for c in d.get('changes',[])],'errors':errs}
    print(json.dumps(out,ensure_ascii=False,indent=2) if a.json else ('PROMPT_REVISION_GATE: '+out['status']+'\n'+'\n'.join('  - '+x for x in errs)))
    raise SystemExit(1 if errs else 0)
if __name__=='__main__': main()
