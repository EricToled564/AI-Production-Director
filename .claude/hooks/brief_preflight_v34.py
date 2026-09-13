#!/usr/bin/env python3
"""Block prompt compilation if any prompt-required brief field is OPEN."""
import argparse,json
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('--brief',required=True); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
b=json.loads(Path(a.brief).read_text(encoding='utf-8'))
missing=[p for p,s in b['field_states'].items() if s.get('prompt_required') and s.get('state')!='LOCKED']
out={'status':'FAIL' if missing else 'PASS','brief_hash':b['brief_hash'],'missing_required':missing}
print(json.dumps(out,ensure_ascii=False,indent=2) if a.json else 'BRIEF_PREFLIGHT: '+out['status'] + (('\n  - '+'\n  - '.join(missing)) if missing else ''))
raise SystemExit(1 if missing else 0)
