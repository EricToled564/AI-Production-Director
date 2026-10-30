#!/usr/bin/env python3
"""Structural checks plus instance checks. No claim of corpus semantic review."""
import json,re,pathlib,hashlib
P=pathlib.Path(__file__).resolve().parents[2]/'4_diseno'/'templates'  # templates que se verifican
OUT=pathlib.Path(__file__).resolve().parent
S=json.loads((P/'CONTRATO_IMAGEN_ORQUESTACION.schema.json').read_text())
R=json.loads((P/'REGISTRO_DESTINOS_TEMPLATE.json').read_text())
C=json.loads((P/'CONTRATOS_OPERACION_MODELO.json').read_text())
def schema_path(path):
 node=S
 for token in path.split('.'):
  arr=token.endswith('[]'); key=token[:-2] if arr else token
  node=node['properties'][key]
  if arr:node=node['items']
 return node

def get(obj,path):
 v=obj
 for part in path.split('.'):
  if part.endswith('[]'): return v[part[:-2]]
  v=v[part]
 return v

def validate_instance(x,stage='brief'):
 import jsonschema
 errors=[e.message for e in jsonschema.Draft202012Validator(S).iter_errors(x)]
 ent=x.get('entrada',{}); operation=ent.get('operacion'); contract=next((o for o in C['operation_contracts'] if o['operacion']==operation),None)
 if not contract:errors.append('Operación sin contrato')
 else:
  for path in contract['required_fields']:
   try:
    value=get(x,path)
    if value=='' or value is None:errors.append('Campo sin resolver: '+path)
   except (KeyError,TypeError):errors.append('Falta campo: '+path)
 for module in C.get('conditional_modules',[]):
  if module['id'] in ent.get('modulos_activos',[]):
   for path in module['required_fields']:
    try:
     if get(x,path) in ['',None]:errors.append('Módulo incompleto: '+path)
    except (KeyError,TypeError):errors.append('Módulo incompleto: '+path)
 refs=ent.get('referencias',[])
 if operation=='genesis' and refs:errors.append('Génesis sin referencia contiene referencias')
 if operation in ['composicion_referencias','edicion','transferencia_estilo','boceto_a_final'] and not refs:errors.append('Operación requiere referencia real')
 if operation and operation.startswith('ancla'):
  for key in ['estilo','color_material','camara','luz','modelo','formato','accion','sujetos']:
   if not ent.get(key):errors.append('Tarjeta D1–D9 incompleta: '+key)
 if ent.get('sujetos',{}).get('cantidad',0)<0:errors.append('Cantidad negativa')
 face=ent.get('rostro',{}).get('ocupacion',0)
 if not 0<=face<=1:errors.append('Ocupación facial fuera de 0..1')
 if stage in ['seleccion','salida']:
  approval=x.get('aprobacion_brief',{})
  digest=hashlib.sha256(json.dumps(ent,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  if approval.get('aprobado') is not True or approval.get('brief_sha256')!=digest or not approval.get('mensaje_id'):errors.append('Aprobación ausente o hash del brief cambiado')
  provenance={p['path']:p for p in x.get('procedencia_campos',[])}
  for p in contract['required_fields'] if contract else []:
   if p not in provenance or not provenance[p].get('aprobacion_id'):errors.append('Sin procedencia/aprobación de campo: '+p)
 if stage=='salida':
  out=x.get('salida',{});prompt=out.get('prompt','');model=ent.get('modelo',{}).get('nombre','')
  if not prompt:errors.append('Prompt vacío')
  if re.search(r'\{\{|\}\}|…|\.\.\.',prompt):errors.append('Prompt conserva variables o elipsis')
  if re.search(r'photorealistic|fotorealista',prompt,re.I):errors.append('Vocabulario prohibido por decisión del usuario')
  if model=='GPT Image 2':
   slots=['Change','Preserve','Constraints'] if operation=='edicion' else ['Scene','Subject','Important Details','Use Case','Constraints']
   actual=re.findall(r'^(Scene|Subject|Important Details|Use Case|Constraints|Change|Preserve):',prompt,re.M)
   if actual!=slots:errors.append('Orden o presencia de slots GPT incorrecto')
   if not prompt.startswith(slots[0]+':'):errors.append('Prefijo fuera de estructura GPT')
  if model.startswith('Nano Banana') and re.search(r'\b\d+\s*mm\b|f/\d|\bISO\s*\d',prompt,re.I):errors.append('Óptica numérica en Nano Banana')
  if model=='Ideogram' and ent.get('texto_integrado_override',{}).get('habilitado') and not ent.get('texto_integrado_override',{}).get('rationale'):errors.append('Ideogram integrado sin rationale')
  if model=='Nano Banana 2 Lite' and out.get('parametros',{}).get('image_size')!='1K':errors.append('Lite fuera de 1K según fuente suministrada')
 return errors

def main():
 paths=list(R['facet_destinations'].values())+[p for v in R['f30_destinations'].values() for p in v]+[f['path'] for f in R['fields']]
 paths += [p for c in C['operation_contracts'] for p in c['required_fields']]
 failures=[]
 for path in paths:
  try:schema_path(path)
  except Exception:failures.append(path)
 import jsonschema
 jsonschema.Draft202012Validator.check_schema(S)
 result={'schema_valid':True,'facets':len([k for k in R['facet_destinations'] if re.fullmatch(r'F\d\d',k)]),'f30_materials':len(R['f30_destinations']),'typed_fields':len(R['fields']),'operation_contracts':len(C['operation_contracts']),'model_adapter_contracts':len(C['model_adapters']),'path_occurrences_checked':len(paths),'invalid_paths':failures,'scope':'Integridad estructural. No certifica enlaces REG, lectura semántica ni selección de corpus.'}
 (OUT/'VERIFICACION_ESTRUCTURAL.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result,ensure_ascii=False))
 assert not failures
if __name__=='__main__': main()
