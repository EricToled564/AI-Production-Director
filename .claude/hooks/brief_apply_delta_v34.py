#!/usr/bin/env python3
"""Apply only an explicit authorized delta to a frozen brief."""
from __future__ import annotations
import argparse, copy, hashlib, json
from pathlib import Path
from brief_freeze_v34 import canon_hash

def setp(d,path,value,op):
    ps=path.split('.'); cur=d
    for p in ps[:-1]:
        if p not in cur or not isinstance(cur[p],dict):
            if op=='add': cur[p]={}
            else: raise KeyError(path)
        cur=cur[p]
    k=ps[-1]
    if op=='replace' and k not in cur: raise KeyError(path)
    if op=='remove':
        if k not in cur: raise KeyError(path)
        cur[k]=None
    else: cur[k]=value

def delta_hash(d):
    return hashlib.sha256(json.dumps(d,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--brief',required=True); ap.add_argument('--delta',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    b=json.loads(Path(a.brief).read_text(encoding='utf-8')); d=json.loads(Path(a.delta).read_text(encoding='utf-8'))
    errors=[]
    if d.get('base_brief_hash')!=b.get('brief_hash'): errors.append('delta base_brief_hash does not match frozen brief')
    facts=copy.deepcopy(b['facts']); states=copy.deepcopy(b['field_states'])
    seen=set()
    for c in d.get('changes',[]):
        p=c['path']; op=c['op']
        if p in seen: errors.append(f'duplicate delta path: {p}'); continue
        seen.add(p)
        old_state=states.get(p,{'prompt_required':True})
        try: setp(facts,p,c.get('value'),op)
        except KeyError: errors.append(f'unknown path for {op}: {p}'); continue
        states[p]={
            'state':'OPEN' if op=='remove' else 'LOCKED',
            'source_type':'user', 'source_id':d['authorized_by'],
            'prompt_required':bool(old_state.get('prompt_required',True))
        }
    if errors:
        print('BRIEF_DELTA: FAIL'); [print('  -',e) for e in errors]; raise SystemExit(1)
    version=b['brief_version']+1; h=canon_hash(b['brief_id'],version,facts,states)
    history=list(b.get('delta_history',[])); history.append({'delta_hash':delta_hash(d),'authorized_by':d['authorized_by'],'reason':d.get('reason',''),'paths':sorted(seen)})
    out={'schema_version':'1.1','brief_id':b['brief_id'],'brief_version':version,'status':'FROZEN','facts':facts,'field_states':states,'brief_hash':h,'delta_history':history}
    Path(a.out).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'BRIEF_DELTA: PASS\n  changes: {len(seen)}\n  new_version: {version}\n  hash: {h}')
if __name__=='__main__': main()
