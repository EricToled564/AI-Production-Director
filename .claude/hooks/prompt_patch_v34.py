#!/usr/bin/env python3
"""Patch a prompt revision without rewriting it: only advance brief_hash after an authorized brief delta.
AST structure, templates, model, rules and generation parameters remain byte-for-byte unchanged.
"""
from __future__ import annotations
import argparse,copy,hashlib,json
from pathlib import Path

def dh(d): return hashlib.sha256(json.dumps(d,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ast',required=True); ap.add_argument('--old-brief',required=True); ap.add_argument('--new-brief',required=True); ap.add_argument('--delta',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    ast=json.loads(Path(a.ast).read_text(encoding='utf-8')); old=json.loads(Path(a.old_brief).read_text(encoding='utf-8')); new=json.loads(Path(a.new_brief).read_text(encoding='utf-8')); d=json.loads(Path(a.delta).read_text(encoding='utf-8'))
    errs=[]
    if ast.get('brief_hash')!=old.get('brief_hash'): errs.append('AST does not target old brief')
    if d.get('base_brief_hash')!=old.get('brief_hash'): errs.append('delta does not target old brief')
    hist=new.get('delta_history',[])
    if not hist or hist[-1].get('delta_hash')!=dh(d): errs.append('new brief was not produced by supplied delta')
    if errs:
        print('PROMPT_PATCH: FAIL'); [print('  -',e) for e in errs]; raise SystemExit(1)
    out=copy.deepcopy(ast); out['brief_hash']=new['brief_hash']; out['prompt_revision']=int(ast.get('prompt_revision',1))+1
    Path(a.out).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'PROMPT_PATCH: PASS\n  revision: {out["prompt_revision"]}\n  new_brief_hash: {new["brief_hash"]}')
if __name__=='__main__': main()
