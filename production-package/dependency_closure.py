#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
REQUIRED={
 'RULES_MATRIX.md': HERE/'RULES_MATRIX.md',
 'template_engine.py': HERE/'template_engine.py',
 'audit_gi2.py': HERE/'audit_gi2.py',
 'RECONSTRUCTION_MANIFEST.json': HERE/'RECONSTRUCTION_MANIFEST.json',
}

def sha(p:Path)->str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    errors=[]; checks=[]
    for name,p in REQUIRED.items():
        ok=p.is_file(); checks.append({'name':name,'exists':ok,'sha256':sha(p) if ok else None})
        if not ok: errors.append(f'missing {name}')
    if not errors:
        # matrix exact 26 rules x 5 type columns
        lines=(HERE/'RULES_MATRIX.md').read_text(encoding='utf-8').splitlines()
        rows=[x for x in lines if x.startswith('| PP') or x.startswith('| R')]
        if len(rows)!=26: errors.append(f'RULES_MATRIX rows={len(rows)} expected 26')
        for i,r in enumerate(rows,1):
            cells=[c.strip() for c in r.strip('|').split('|')]
            if len(cells)!=9: errors.append(f'RULES_MATRIX row {i} has {len(cells)} cells expected 9')
        checks.append({'name':'matrix_26x5','pass':not any('RULES_MATRIX' in e for e in errors),'rows':len(rows)})
        for tool,args in [('template_engine.py',[]),('audit_gi2.py',['--selftest'])]:
            p=subprocess.run([sys.executable,str(HERE/tool),*args],capture_output=True,text=True)
            checks.append({'name':tool+'_selftest','pass':p.returncode==0,'stdout':p.stdout.strip(),'stderr':p.stderr.strip()})
            if p.returncode!=0: errors.append(f'{tool} selftest failed')
    out={'status':'FAIL' if errors else 'PASS','required_count':len(REQUIRED),'errors':errors,'checks':checks}
    if a.json: print(json.dumps(out,ensure_ascii=False,indent=2))
    else:
        print('DEPENDENCY CLOSURE:',out['status'])
        for c in checks: print(' ',c['name'], 'PASS' if c.get('pass',c.get('exists')) else 'FAIL')
        for e in errors: print(' -',e)
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
