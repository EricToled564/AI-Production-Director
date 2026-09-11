#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[2]
HOOK=ROOT/'.claude/hooks'
RULE=ROOT/'.claude/rules/v3'

def run(cmd,ok=(0,)):
    p=subprocess.run(cmd,capture_output=True,text=True)
    if p.returncode not in ok:
        raise AssertionError(f"cmd failed {cmd}\nrc={p.returncode}\nOUT={p.stdout}\nERR={p.stderr}")
    return p

def main():
    rs=json.load(open(RULE/'build/ruleset-3.2.1.json'))
    assert rs['published'] is True
    assert rs['kb_rule_count']==1649
    assert rs['learned_rule_count']==14
    assert rs['rule_count']==1663
    ids={x['rule']['id'] for x in rs['rules']}
    required={
      'lrn32_lock_preservation','lrn32_small_delta_revision','lrn32_domain_pose_literal',
      'lrn32_reference_role_isolation','lrn32_generation_params_are_hard','lrn32_ratio_tolerance',
      'lrn32_no_unspecified_amplification','lrn32_physical_occlusion_strategy','lrn32_camera_geometry_visibility',
      'lrn32_qa_before_claim','lrn32_surgical_edit_after_accept','lrn32_nano_underwater_diving_route',
      'lrn321_composition_abstraction_no_ref','lrn321_no_cross_task_attribute_leak'}
    assert required <= ids

    nano=ROOT/'examples/cases/diver_nano_ref_case.json'
    gpt=ROOT/'examples/cases/diver_gpt2_ref_case.json'
    # Published overlay can match both known cases fail-closed with zero unresolved.
    for case in (nano,gpt):
        with tempfile.NamedTemporaryFile(suffix='.json') as f:
            p=run([sys.executable,str(HOOK/'rule_matcher_v3.py'),'--ruleset',str(RULE/'build/ruleset-3.2.1.json'),'--case',str(case),'--out',f.name])
            m=json.load(open(f.name)); assert m['counts']['rules_evaluated']==1663; assert m['counts']['unresolved']==0; assert m['counts']['unresolved_conflicts']==0

    routes=RULE/'learned/model-routing.v3.2.json'
    # Explicit user generator lock always wins.
    for case, fam in ((nano,'nano_banana'),(gpt,'gpt_image')):
        p=run([sys.executable,str(HOOK/'model_router_v32.py'),'--case',str(case),'--routes',str(routes),'--json'])
        r=json.loads(p.stdout); assert r['status']=='USER_MODEL_LOCK_PRESERVED'; assert r['selected']['family']==fam
    # Unknown generator routes this exact risk profile to Nano Banana Pro.
    d=json.load(open(nano)); d['generator']={'family':'UNKNOWN','model':None,'adapter_version':None}
    with tempfile.NamedTemporaryFile('w+',suffix='.json') as f:
        json.dump(d,f); f.flush()
        p=run([sys.executable,str(HOOK/'model_router_v32.py'),'--case',f.name,'--routes',str(routes),'--json'])
        r=json.loads(p.stdout); assert r['status']=='ROUTED'; assert r['selected']=={'family':'nano_banana','model':'nano-banana-pro'}

    # Ratio policy: exact, near (minor), and vertical fail.
    with tempfile.TemporaryDirectory() as td:
        td=Path(td); exact=td/'exact.png'; near=td/'near.png'; bad=td/'bad.png'
        Image.new('RGB',(1600,900)).save(exact); Image.new('RGB',(1024,572)).save(near); Image.new('RGB',(852,1024)).save(bad)
        p=run([sys.executable,str(HOOK/'output_geometry_check_v32.py'),'--image',str(exact),'--aspect','16:9','--json']); assert json.loads(p.stdout)['status']=='PASS'
        p=run([sys.executable,str(HOOK/'output_geometry_check_v32.py'),'--image',str(near),'--aspect','16:9','--json']); assert json.loads(p.stdout)['status']=='MINOR'
        p=run([sys.executable,str(HOOK/'output_geometry_check_v32.py'),'--image',str(bad),'--aspect','16:9','--json'],ok=(1,)); assert json.loads(p.stdout)['status']=='FAIL'

    # Learning registry/templates must exist.
    assert (RULE/'learned/LEARNING_REGISTRY_v3.2.md').exists()
    assert (ROOT/'templates/v3.2/underwater-human-reference-policy.md').exists()
    assert (ROOT/'templates/v3.2/surgical-image-edit.md').exists()
    assert (ROOT/'templates/v3.2/composition-only-source.md').exists()
    print('V3.2 LEARNING PATCH: PASS')
    print('checks: ruleset overlay, 14 learned rules, runtime exhaustivity, routing, explicit model lock, aspect QA, templates')
if __name__=='__main__': main()
