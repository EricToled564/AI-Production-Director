#!/usr/bin/env python3
import json,subprocess,tempfile,unittest,copy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; H=ROOT/'.claude/hooks'
class V34(unittest.TestCase):
 def cmd(self,*args,ok=True):
  p=subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True)
  if ok and p.returncode: self.fail(p.stdout+p.stderr)
  return p
 def fixture(self,td):
  d=Path(td); facts={'deliverable':'editorial sports photograph','aspect_ratio':'16:9','model':'Nano Banana Pro','reference_mode':'none','subject':{'sex':'male','age_range':None,'sport':'tennis'},'composition':{'camera':'low side-on camera close to the player','perspective':'compressed moderate telephoto perspective','player_position':'large in frame, center-right','action':'deep lateral two-handed backhand stretch toward camera-left','racket_ball':'racket and yellow ball in the left third, just before contact','legs':'one leg bent and planted; opposite leg extends strongly toward the right','court_depth':'only a narrow strip of clay behind the player before the courtside wall','net_visibility':'no visible tennis net'},'environment':{'location':'Roland-Garros','surface':'red clay','wall_relation':'courtside wall sits immediately behind the player','stands':'packed spectator stands rise directly above the wall','crowd_focus':'softly out of focus'},'look':{'expression':'natural controlled expression','anatomy':'realistic anatomy','clay':'restrained clay spray','photography':'live-match editorial photography'}}
  (d/'facts.json').write_text(json.dumps(facts)); return d
 def freeze(self,d):
  self.cmd(H/'brief_freeze_v34.py','--input',d/'facts.json','--brief-id','t','--prompt-optional-prefix','model','--prompt-optional-prefix','aspect_ratio','--prompt-optional-prefix','reference_mode','--prompt-required-prefix','subject.age_range','--out',d/'b1.json'); return json.load(open(d/'b1.json'))
 def test_01_unresolved_required_blocks(self):
  with tempfile.TemporaryDirectory() as td:
   d=self.fixture(td); self.freeze(d); p=self.cmd(H/'brief_preflight_v34.py','--brief',d/'b1.json',ok=False); self.assertNotEqual(p.returncode,0); self.assertIn('subject.age_range',p.stdout)
 def test_02_authorized_delta_resolves(self):
  with tempfile.TemporaryDirectory() as td:
   d=self.fixture(td); b=self.freeze(d); delta={'schema_version':'1.1','base_brief_hash':b['brief_hash'],'authorized_by':'user','reason':'resolve age','changes':[{'path':'subject.age_range','op':'replace','value':'30–35'}]}; (d/'delta.json').write_text(json.dumps(delta)); self.cmd(H/'brief_apply_delta_v34.py','--brief',d/'b1.json','--delta',d/'delta.json','--out',d/'b2.json'); p=self.cmd(H/'brief_preflight_v34.py','--brief',d/'b2.json'); self.assertIn('PASS',p.stdout)
 def test_03_wrong_base_hash_blocks(self):
  with tempfile.TemporaryDirectory() as td:
   d=self.fixture(td); self.freeze(d); delta={'schema_version':'1.1','base_brief_hash':'0'*64,'authorized_by':'user','reason':'x','changes':[{'path':'subject.age_range','op':'replace','value':'30–35'}]}; (d/'delta.json').write_text(json.dumps(delta)); p=self.cmd(H/'brief_apply_delta_v34.py','--brief',d/'b1.json','--delta',d/'delta.json','--out',d/'b2.json',ok=False); self.assertNotEqual(p.returncode,0)
 def test_04_tennis_fixture_drift_is_blocked(self):
  ex=ROOT/'examples/v3.4/tennis'; p=self.cmd(H/'prompt_revision_gate_v34.py','--before',ex/'prompt_v1.ast.json','--after',ex/'prompt_v2_drifted.ast.json','--old-brief',ex/'brief_v2.lock.json','--new-brief',ex/'brief_v3.lock.json','--delta',ex/'delta_age_only_revision.json',ok=False); self.assertNotEqual(p.returncode,0); self.assertIn('UNAUTHORIZED PROMPT DRIFT',p.stdout)
 def test_05_tennis_fixture_age_only_passes(self):
  ex=ROOT/'examples/v3.4/tennis'; p=self.cmd(H/'prompt_revision_gate_v34.py','--before',ex/'prompt_v1.ast.json','--after',ex/'prompt_v2.ast.json','--old-brief',ex/'brief_v2.lock.json','--new-brief',ex/'brief_v3.lock.json','--delta',ex/'delta_age_only_revision.json'); self.assertIn('PASS',p.stdout)
 def test_06_age_only_render_changes_only_age(self):
  ex=ROOT/'examples/v3.4/tennis'; a=(ex/'prompt_v1.txt').read_text(); b=(ex/'prompt_v2.txt').read_text(); self.assertEqual(a.replace('30–35','31–35'),b)
 def test_07_parameter_drift_blocks(self):
  ex=ROOT/'examples/v3.4/tennis'; x=json.load(open(ex/'prompt_v2.ast.json')); x['parameters']['aspectRatio']='1:1'; tmp=ex/'_tmp_param_drift.json'; tmp.write_text(json.dumps(x)); p=self.cmd(H/'prompt_revision_gate_v34.py','--before',ex/'prompt_v1.ast.json','--after',tmp,'--old-brief',ex/'brief_v2.lock.json','--new-brief',ex/'brief_v3.lock.json','--delta',ex/'delta_age_only_revision.json',ok=False); tmp.unlink(); self.assertNotEqual(p.returncode,0)
if __name__=='__main__': unittest.main(verbosity=2)
