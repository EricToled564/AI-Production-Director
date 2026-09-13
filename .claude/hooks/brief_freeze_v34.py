#!/usr/bin/env python3
"""Freeze a production brief into immutable facts + field states.
Non-null leaves are LOCKED. Null leaves are OPEN. A caller may mark OPEN fields
as prompt-required; those must be resolved before prompt compilation.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def leaves(v, prefix=''):
    if isinstance(v, dict):
        for k in sorted(v):
            p=f'{prefix}.{k}' if prefix else k
            yield from leaves(v[k],p)
    elif isinstance(v, list):
        yield prefix,v
    else:
        yield prefix,v

def under(path, prefixes):
    return any(path==x or path.startswith(x+'.') for x in prefixes)

def canon_hash(brief_id, version, facts, states):
    payload={'brief_id':brief_id,'brief_version':version,'facts':facts,'field_states':states}
    raw=json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',required=True); ap.add_argument('--brief-id',required=True)
    ap.add_argument('--source-id',default='user-brief'); ap.add_argument('--derived-prefix',action='append',default=[])
    ap.add_argument('--prompt-optional-prefix',action='append',default=[])
    ap.add_argument('--prompt-required-prefix',action='append',default=[])
    ap.add_argument('--out',required=True); a=ap.parse_args()
    facts=json.loads(Path(a.input).read_text(encoding='utf-8')); states={}
    for p,val in leaves(facts):
        derived=under(p,a.derived_prefix); optional=under(p,a.prompt_optional_prefix); explicitly_required=under(p,a.prompt_required_prefix)
        states[p]={
            'state':'OPEN' if val is None else 'LOCKED',
            'source_type':'derived' if derived else 'user',
            'source_id':a.source_id,
            'prompt_required': bool(explicitly_required or (val is not None and not optional)),
        }
    h=canon_hash(a.brief_id,1,facts,states)
    out={'schema_version':'1.1','brief_id':a.brief_id,'brief_version':1,'status':'FROZEN','facts':facts,'field_states':states,'brief_hash':h}
    Path(a.out).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
    unresolved=[p for p,s in states.items() if s['state']=='OPEN' and s['prompt_required']]
    print(f'BRIEF_FREEZE: PASS\n  fields: {len(states)}\n  unresolved_required: {len(unresolved)}\n  hash: {h}\n  out: {a.out}')
if __name__=='__main__': main()
