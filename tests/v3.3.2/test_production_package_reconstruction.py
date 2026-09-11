#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PKG=ROOT/'production-package'

def run(cmd,ok=(0,)):
    p=subprocess.run(cmd,capture_output=True,text=True)
    if p.returncode not in ok:
        raise AssertionError(f'FAIL {cmd}\n{p.stdout}\n{p.stderr}')
    return p

def main():
    closure=json.loads(run([sys.executable,str(PKG/'dependency_closure.py'),'--json']).stdout)
    assert closure['status']=='PASS'
    # Real regression: 121-word tennis candidate must fail word ceiling; 120 must pass.
    prompt121='Create a wide sports editorial photograph of one male competitive tennis player on a clay court. Shoot from very low court level, with the athlete spanning the middle-to-right region in a deep lateral two-handed backhand reach toward camera-left. Freeze the instant with the ball a few centimeters in front of the racket strings in the left third. One leg is deeply bent and planted while the opposite leg extends wide across the clay. Show restrained irregular clay spray, compressed shoe contact and slide marks. Use a new muted slate-blue perimeter wall as a clean horizontal background band, with spectators softly out of focus beyond it. Natural daytime light, shallow background depth, visible sweat, fabric folds, skin texture and balanced human proportions.'
    base={'type':'T3','sections':{'scene':'Clay court.','subject':'One male tennis player.','anatomy':'Balanced human proportions.','usecase':'Editorial sports photograph.','mood':'Focused competition.','colour':'Natural red clay.'},'block_ids':{'anatomy':'anatomy'},'metadata':{'model':'nano-banana-pro','size_or_ratio':'16:9'},'notes':'No reference image sent.','audit_context':{'max_prompt_words':120,'jobs':1},'prompt':prompt121}
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'a.json'; p.write_text(json.dumps(base),encoding='utf-8')
        out=run([sys.executable,str(PKG/'audit_gi2.py'),str(p),'--json'],ok=(1,))
        d=json.loads(out.stdout); assert d['status']=='FAIL'
        wc=next(x for x in d['checks'] if x['name']=='word_ceiling'); assert wc['status']=='FAIL' and '121/120' in wc['detail']
        base['prompt']=prompt121.replace('male competitive tennis player','male tennis player',1)
        p.write_text(json.dumps(base),encoding='utf-8')
        d=json.loads(run([sys.executable,str(PKG/'audit_gi2.py'),str(p),'--json']).stdout); assert d['status']=='PASS'
    print('V3.3.2 PRODUCTION PACKAGE RECONSTRUCTION: PASS')
    print('checks: dependency closure, template/audit selftests, matrix 26x5, tennis 121->FAIL / 120->PASS')
if __name__=='__main__': main()
