#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,sys
from pathlib import Path
from rule_engine_v3 import eval_condition, TRUE, UNKNOWN

def parse_ratio(s):
    if not s or ':' not in str(s): return None
    try:
        a,b=str(s).split(':',1); a=float(a); b=float(b); return a/b if a>0 and b>0 else None
    except Exception: return None

def derived_features(case):
    tags=set(case.get('task',{}).get('tags',[]) or [])
    phys=case.get('physics',{})
    pcount=sum(1 for k in ('water','splash','bubbles','turbulence','refraction','reflection','gravity','collision','deformation') if phys.get(k) is True)
    ratio=parse_ratio(case.get('deliverable',{}).get('aspect_ratio'))
    fam=case.get('task',{}).get('family')
    text=case.get('text',{})
    refs=case.get('references',{})
    purpose=case.get('deliverable',{}).get('purpose')
    brand=case.get('brand',{}).get('mode')
    op=case.get('operation')
    sid=case.get('subject',{}).get('identity_fidelity')
    product=case.get('subject',{}).get('product_fidelity')
    roles=refs.get('roles',[]) or []
    return {
      'requires_real_world_grounding': bool(tags & {'REAL_WORLD_GROUNDING','GROUNDING_REQUIRED'}),
      'complex_scene_physics_composition': case.get('composition',{}).get('load_bearing') is True and (pcount>=2 or bool(tags & {'COMPLEX_PHYSICS','PHYSICS_HEAVY'})),
      'extreme_aspect_ratio': ratio is not None and (ratio>3.0 or ratio<(1/3)),
      'bulk_low_cost': bool(tags & {'BULK_LOW_COST','MASS_GENERATION'}),
      'photographic_fine_typography_ui': case.get('realism',{}).get('mode') in {'photographic','strict_photographic'} and (fam=='ui_social' or (text.get('readable_text_required') is True and bool(tags & {'FINE_TYPOGRAPHY','UI'}))),
      'exact_edit_preservation': op=='image_edit' and (sid in {'consistent','exact'} or product in {'recognizable','exact'}),
      'dense_small_text': text.get('readable_text_required') is True and (fam=='text_rendering' or bool(tags & {'DENSE_SMALL_TEXT'})),
      'brand_print_exact_text': purpose=='poster' and brand in {'guided','locked','strict'} and text.get('readable_text_required') is True,
      'storyboard_sequence': fam in {'storyboard','multi_panel'} and text.get('readable_text_required') is not True,
      'storyboard_typography': fam in {'storyboard','multi_panel'} and text.get('readable_text_required') is True,
      'style_transfer_without_refs': bool(tags & {'STYLE_TRANSFER'}) and refs.get('mode')=='none',
      'many_references_14_plus': len(roles)>=14 or bool(tags & {'MANY_REFERENCES_14_PLUS'}),
      'photographic_portrait': fam=='portrait' and case.get('realism',{}).get('mode') in {'photographic','strict_photographic'},
      'neutral_product_shot': purpose=='product' and case.get('environment',{}).get('type') in {'neutral_studio','studio','neutral_background'},
      'minimalist_poster': purpose=='poster' and bool(tags & {'MINIMALIST'}),
      'editorial_photography': purpose=='editorial' and case.get('realism',{}).get('mode') in {'photographic','strict_photographic'},
      'physics_signal_count':pcount
    }

def validate_case(case_path,schema_path):
    import jsonschema
    case=json.load(open(case_path,encoding='utf-8')); schema=json.load(open(schema_path,encoding='utf-8'))
    errs=list(jsonschema.Draft202012Validator(schema).iter_errors(case))
    if errs:
        return case,[f"{'.'.join(map(str,e.path)) or '$'}: {e.message}" for e in errs]
    return case,[]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--case',required=True); ap.add_argument('--canonical',required=True); ap.add_argument('--learned'); ap.add_argument('--schema',required=True); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    case,errors=validate_case(a.case,a.schema)
    if errors:
        result={'status':'CASE_INVALID','errors':errors}; print(json.dumps(result,ensure_ascii=False,indent=2)); return 1
    current=case.get('generator',{})
    explicit=current.get('family') not in (None,'UNKNOWN','other') and current.get('model') not in (None,'UNKNOWN','')
    features=derived_features(case)
    canonical=json.load(open(a.canonical,encoding='utf-8'))
    candidates=[]; neutrals=[]
    for r in canonical.get('routes',[]):
        if features.get(r['feature']) is True:
            candidates.append({'source':'KB_CANONICAL','id':r['id'],'priority':r['priority'],'kind':r['kind'],'candidates':r['candidates'],'source_rule_id':r['source_rule_id'],'source_text':r['source_text'],'feature':r['feature']})
    for r in canonical.get('neutral_routes',[]):
        if features.get(r['feature']) is True:
            neutrals.append({'source':'KB_CANONICAL','id':r['id'],'priority':r['priority'],'kind':'NEUTRAL','candidates':r['candidates'],'source_rule_id':r['source_rule_id'],'source_text':r['source_text'],'feature':r['feature']})
    if a.learned:
        ld=json.load(open(a.learned,encoding='utf-8'))
        for r in ld.get('routes',[]):
            st=eval_condition(case,r.get('when',{}))
            if st==TRUE:
                candidates.append({'source':'LEARNED_PRODUCTION','id':r['id'],'priority':r.get('priority',0),'kind':'DECISIVE','candidates':[r['preferred']],'evidence':r.get('evidence')})
    candidates.sort(key=lambda x:x['priority'],reverse=True)
    if explicit:
        result={'status':'USER_MODEL_LOCK_PRESERVED','selected':current,'features':features,'matching_routes':candidates,'neutral_routes':neutrals}
    elif candidates:
        top=candidates[0]
        if top['kind']=='CHOICE' and len(top['candidates'])>1:
            result={'status':'MODEL_CHOICE_REQUIRED','selected':None,'choices':top['candidates'],'route':top,'features':features,'matching_routes':candidates,'neutral_routes':neutrals}
        else:
            result={'status':'ROUTED','selected':top['candidates'][0],'route':top,'features':features,'matching_routes':candidates,'neutral_routes':neutrals}
    elif neutrals:
        result={'status':'MODEL_TIE','selected':None,'choices':neutrals[0]['candidates'],'route':neutrals[0],'features':features,'matching_routes':[],'neutral_routes':neutrals}
    else:
        result={'status':'NO_CANONICAL_ROUTE','selected':None,'features':features,'matching_routes':[],'neutral_routes':[]}
    print(json.dumps(result,ensure_ascii=False,indent=2) if a.json else result)
    return 0 if result['status'] in {'ROUTED','USER_MODEL_LOCK_PRESERVED','MODEL_TIE','MODEL_CHOICE_REQUIRED','NO_CANONICAL_ROUTE'} else 1
if __name__=='__main__': raise SystemExit(main())
