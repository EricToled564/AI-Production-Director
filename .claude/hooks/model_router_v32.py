#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from rule_engine_v3 import eval_condition, TRUE, UNKNOWN

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--case',required=True); ap.add_argument('--routes',required=True); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    case=json.load(open(a.case,encoding='utf-8')); routes=json.load(open(a.routes,encoding='utf-8'))['routes']
    current=case.get('generator',{})
    explicit=current.get('family') not in (None,'UNKNOWN','other') and current.get('model') not in (None,'UNKNOWN','')
    matches=[]; unknown=[]
    for r in routes:
        st=eval_condition(case,r.get('when',{}))
        if st==TRUE: matches.append(r)
        elif st==UNKNOWN: unknown.append(r['id'])
    matches.sort(key=lambda r:r.get('priority',0),reverse=True)
    if explicit:
        result={'status':'USER_MODEL_LOCK_PRESERVED','selected':current,'recommended':matches[0]['preferred'] if matches else None,'route_id':matches[0]['id'] if matches else None,'unknown_routes':unknown}
    elif matches:
        result={'status':'ROUTED','selected':matches[0]['preferred'],'route_id':matches[0]['id'],'confidence':matches[0].get('confidence'),'unknown_routes':unknown}
    else:
        result={'status':'NO_ROUTE','selected':current,'unknown_routes':unknown}
    print(json.dumps(result,ensure_ascii=False,indent=2) if a.json else result)
if __name__=='__main__': main()
