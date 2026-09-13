#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,hashlib
from datetime import datetime,timezone
from pathlib import Path
def canon(x): return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x): return hashlib.sha256(canon(x).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--base',required=True); ap.add_argument('--learned',required=True); ap.add_argument('--out',required=True); ap.add_argument('--version',default='3.4.0'); a=ap.parse_args()
 base=json.load(open(a.base,encoding='utf-8')); learned=json.load(open(a.learned,encoding='utf-8'))
 if not base.get('published'): raise SystemExit('base ruleset not published')
 ids={x['rule']['id'] for x in base['rules']}; add=[]
 for x in learned['rules']:
  rid=x['rule']['id']
  if rid in ids: raise SystemExit(f'duplicate learned rule id {rid}')
  add.append(x); ids.add(rid)
 out=dict(base); out['ruleset_version']=a.version; out['published_at']=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
 out['certification']='V3_3_2_DEPENDENCY_CLOSED_PLUS_V3_4_FROZEN_BRIEF_AUTHORIZED_DELTA'
 out['base_rule_count']=len(base['rules']); out['v34_learned_rule_count']=len(add); out['rule_count']=len(base['rules'])+len(add)
 out['v34_overlay']={'version':learned['version'],'provenance':learned['provenance'],'sha256':sha(learned)}
 out['rules']=base['rules']+add; out['ruleset_sha256']=sha({'base_ruleset_sha256':base.get('ruleset_sha256'),'v34':learned,'rules':out['rules'],'policies':out.get('conflict_policies',[])})
 Path(a.out).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
 print('RULESET OVERLAY V3.4: PASS'); print('base',out['base_rule_count'],'v34',out['v34_learned_rule_count'],'total',out['rule_count']); print('hash',out['ruleset_sha256'])
if __name__=='__main__': main()
