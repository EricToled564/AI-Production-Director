#!/usr/bin/env python3
from __future__ import annotations
import json,subprocess,sys,tempfile,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HOOK=ROOT/'.claude/hooks'; RULE=ROOT/'.claude/rules/v3'

def run(cmd,ok=(0,)):
    p=subprocess.run(cmd,capture_output=True,text=True)
    if p.returncode not in ok: raise AssertionError(f'FAIL {cmd}\n{p.stdout}\n{p.stderr}')
    return p

def main():
    base=json.load(open(RULE/'build/ruleset-3.3.0.json')); rs=json.load(open(RULE/'build/ruleset-3.3.1.json'))
    assert base['published'] is True and base['rule_count']==1686
    assert base['certification']=='EXHAUSTIVE_RELATIVE_TO_KB_SOURCE_UNIVERSE_V3_3_DECISION_TABLE_REAUDIT'
    assert rs['kb_rule_count']==1686 and rs['learned_rule_count']==14 and rs['rule_count']==1700
    routing=json.load(open(RULE/'build/model-routing.canonical-v3.3.json'))
    assert routing['runtime_source_reads_forbidden'] is True
    assert len(routing['routes'])==12 and len(routing['neutral_routes'])==4
    # The formerly lost complex-scene row is now canonical and compiled.
    route=next(x for x in routing['routes'] if x['feature']=='complex_scene_physics_composition')
    assert route['source_block_id']=='e8b13f2f6cc8387b' and route['source_rule_id']=='8c832fc25405'
    pre=ROOT/'examples/cases/tennis_editorial_composition_only_pre_route.json'
    p=run([sys.executable,str(HOOK/'model_router_v33.py'),'--case',str(pre),'--canonical',str(RULE/'build/model-routing.canonical-v3.3.json'),'--learned',str(RULE/'learned/model-routing.v3.2.json'),'--schema',str(RULE/'case-fingerprint.schema.json'),'--json'])
    out=json.loads(p.stdout); assert out['status']=='ROUTED'; assert out['selected']=={'family':'nano_banana','model':'nano-banana-pro'}
    assert out['route']['source']=='KB_CANONICAL'; assert out['route']['source_rule_id']=='8c832fc25405'; assert out['features']['complex_scene_physics_composition'] is True
    prompt=ROOT/'examples/cases/tennis_editorial_nano_pro_prompt.json'
    with tempfile.NamedTemporaryFile(suffix='.json') as f:
        run([sys.executable,str(HOOK/'rule_matcher_v3.py'),'--ruleset',str(RULE/'build/ruleset-3.3.1.json'),'--case',str(prompt),'--out',f.name])
        m=json.load(open(f.name)); assert m['counts']['rules_evaluated']==1700; assert m['counts']['unresolved']==0; assert m['counts']['unresolved_conflicts']==0
        rb={r['rule_id']:r['status'] for r in m['records']}
        # model selection was already consumed in routing stage, so it must not contaminate prompt ledger
        assert rb['8c832fc25405']=='NA'
        # syntax decision table is active at prompt stage
        assert rb['23b761292838']=='APPLIES'
    audit=json.load(open(RULE/'build/decision-table-audit-v3.3.json'))
    assert audit['promoted']==37 and audit['represented']==6
    print('V3.3 DECISION ROUTING: PASS')
    print('checks: decision-table reaudit, canonical model routing, no runtime source read, tennis routes to NBP, full matcher 1700/0 unresolved')
if __name__=='__main__': main()
