#!/usr/bin/env python3
"""Deterministically render Prompt AST v2 from a frozen brief. No semantic rewriting."""
from __future__ import annotations
import argparse,json
from pathlib import Path

def getp(d,path):
    cur=d
    for p in path.split('.'): cur=cur[p]
    return cur

def fmt(v):
    if isinstance(v,bool): return 'true' if v else 'false'
    if isinstance(v,list): return ', '.join(str(x) for x in v)
    return str(v)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ast',required=True); ap.add_argument('--brief',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    x=json.loads(Path(a.ast).read_text(encoding='utf-8')); b=json.loads(Path(a.brief).read_text(encoding='utf-8'))
    if x.get('brief_hash')!=b.get('brief_hash'): raise SystemExit('PROMPT_RENDER: FAIL brief_hash mismatch')
    blocks=[]
    for block in x['blocks']:
        segtexts=[]
        for s in block['segments']:
            if s['kind']=='brief_template':
                vals={name:fmt(getp(b['facts'],path)) for name,path in s['bindings'].items()}
                segtexts.append(s['template'].format(**vals).strip())
            else: segtexts.append(s['text'].strip())
        blocks.append(' '.join(t for t in segtexts if t))
    text='\n\n'.join(blocks)+'\n'; Path(a.out).write_text(text,encoding='utf-8')
    print(f'PROMPT_RENDER: PASS\n  blocks: {len(blocks)}\n  out: {a.out}')
if __name__=='__main__': main()
