#!/usr/bin/env python3
"""Validate a deterministic prompt AST against a frozen brief.
Brief-template segments may bind only LOCKED fields. Rule/adapter segments require rule provenance.
Every prompt-required brief field must be represented by a binding.
"""
from __future__ import annotations
import argparse,json,re
from pathlib import Path

def placeholders(t): return set(re.findall(r'\{([A-Za-z_][A-Za-z0-9_]*)\}',t))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--brief',required=True); ap.add_argument('--ast',required=True); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    b=json.loads(Path(a.brief).read_text(encoding='utf-8')); ast=json.loads(Path(a.ast).read_text(encoding='utf-8'))
    errs=[]; used=[]; ids=set()
    if ast.get('schema_version')!='2.0': errs.append('prompt AST schema_version must be 2.0')
    if ast.get('brief_hash')!=b.get('brief_hash'): errs.append('prompt AST brief_hash mismatch')
    open_required=[p for p,s in b['field_states'].items() if s.get('prompt_required') and s.get('state')!='LOCKED']
    if open_required: errs.append('prompt-required fields are OPEN: '+', '.join(open_required))
    states=b['field_states']
    for block in ast.get('blocks',[]):
        if not block.get('segments'): errs.append(f'block {block.get("id")} has no segments')
        for seg in block.get('segments',[]):
            sid=f'{block.get("id")}.{seg.get("id")}'
            if sid in ids: errs.append(f'duplicate segment id {sid}')
            ids.add(sid); kind=seg.get('kind')
            if kind=='brief_template':
                template=seg.get('template',''); binds=seg.get('bindings',{})
                if placeholders(template)!=set(binds): errs.append(f'{sid} template placeholders do not match bindings')
                if not binds: errs.append(f'{sid} has no brief bindings')
                for _,p in binds.items():
                    used.append(p)
                    if p not in states: errs.append(f'{sid} references unknown brief path {p}')
                    elif states[p]['state']!='LOCKED': errs.append(f'{sid} binds OPEN brief field {p}')
            elif kind in ('rule_text','adapter_text'):
                if not seg.get('text'): errs.append(f'{sid} has empty text')
                if not seg.get('source_rules'): errs.append(f'{sid} lacks rule provenance')
                if seg.get('bindings'): errs.append(f'{sid} rule/adapter segment may not bind brief fields')
            else: errs.append(f'{sid} invalid kind {kind}')
    missing=[p for p,s in states.items() if s.get('prompt_required') and s['state']=='LOCKED' and p not in used]
    if missing: errs.append('locked prompt-required fields omitted: '+', '.join(missing))
    out={'status':'FAIL' if errs else 'PASS','brief_hash':b['brief_hash'],'segments':len(ids),'used_paths':sorted(set(used)),'missing_required':missing,'errors':errs}
    print(json.dumps(out,ensure_ascii=False,indent=2) if a.json else ('PROMPT_AST_GATE: '+out['status']+'\n'+'\n'.join('  - '+x for x in errs)))
    raise SystemExit(1 if errs else 0)
if __name__=='__main__': main()
