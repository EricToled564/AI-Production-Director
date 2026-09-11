#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from PIL import Image

def ratio(s):
    a,b=s.split(':',1); return float(a)/float(b)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--image',required=True); ap.add_argument('--aspect',required=True); ap.add_argument('--minor-tolerance-pct',type=float,default=1.0); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    im=Image.open(a.image); w,h=im.size; target=ratio(a.aspect); actual=w/h; dev=abs(actual-target)/target*100
    if dev < 1e-9: status='PASS'
    elif dev <= a.minor_tolerance_pct: status='MINOR'
    else: status='FAIL'
    out={'status':status,'width':w,'height':h,'requested_aspect':a.aspect,'target_ratio':target,'actual_ratio':actual,'deviation_pct':dev,'policy':'exact preferred; <=1% minor; >1% blocking unless user accepts'}
    print(json.dumps(out,indent=2) if a.json else out)
    raise SystemExit(1 if status=='FAIL' else 0)
if __name__=='__main__': main()
