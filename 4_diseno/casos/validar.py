from pathlib import Path
import json,sqlite3,sys,collections
R=Path(__file__).resolve().parent
rows=json.loads((R/'catalogo_opciones.json').read_text()); ids={r['id']:r for r in rows}
assert len(ids)==len(rows),'IDs duplicados'
assert {i for i in ids if i.startswith('TRM-')}=={f'TRM-{i:04}' for i in range(1,1370)},'Cobertura TRM incompleta'
assert all(r['physical_paths'] and all(r['physical_paths']) for r in rows),'Destino vacío'
assert {f'F{i:02}' for i in range(1,32)}.issubset({r['facet'] for r in rows}),'Faceta perdida'
assert all(r['disposition'] not in ['NO APLICA','NO DETERMINADO','PENDIENTE'] for r in rows)
con=sqlite3.connect(R/'casos_opciones.sqlite'); assert con.execute('SELECT COUNT(*) FROM opciones').fetchone()[0]==len(rows)
schema=json.loads((R.parent/'templates'/'CONTRATO_IMAGEN_ORQUESTACION.schema.json').read_text())
def path_exists(path):
 s=schema
 for p in path.split('.'):
  arr=p.endswith('[]');k=p[:-2] if arr else p
  if k not in s.get('properties',{}):return False
  s=s['properties'][k]
  if arr:
   if s.get('type')!='array':return False
   s=s['items']
 return True
assert all(path_exists(p) for r in rows for p in r['physical_paths']),'Ruta fuera de schema'
assert all(r['definition'] not in ['', '—', '-'] for r in rows if r['disposition'] in ['VOCABULARIO_OPERATIVO','VALOR_AUTORIZADO']),'Definición operativa vacía'
result={'rutas_comprobadas_en_schema':sum(len(r['physical_paths']) for r in rows),'validacion_estructural':'PASA','registros':len(rows),'TRM':1369,'IDs_duplicados':0,'destinos_vacios':0,'facetas':31,'asociaciones_REG':0,'compatibilidad_semantica':'No medida: se requiere catálogo de reglas originales clasificado.'}
if len(sys.argv)>1:
 c=json.loads(Path(sys.argv[1]).read_text());errors=[]
 for k in ['case_id','taxonomy_sha256','brief_literal','campos','requisitos_de_completitud','aprobacion']:
  if k not in c:errors.append('Falta campo estructural '+k)
 if not c.get('requisitos_de_completitud'):errors.append('Falta contrato de requisitos del caso')
 if not c.get('campos'):errors.append('Faltan datos del brief')
 expected=json.loads((R/'manifest_fuentes.json').read_text())['taxonomy']['sha256']
 if c.get('taxonomy_sha256')!=expected:errors.append('Huella de taxonomía incorrecta')
 for f in c.get('campos',[]):
  if not path_exists(f.get('path','')):errors.append('Campo fuera del template: '+f.get('path',''))
  for oid in f.get('option_ids',[]):
   if oid not in ids:errors.append('Opción desconocida '+oid)
   elif not ids[oid]['case_selectable']:errors.append('Opción documental/control fuera del selector de atributos '+oid)
   elif not any(f.get('path','')==p or f.get('path','').startswith(p+'.') for p in ids[oid]['physical_paths']):errors.append('Opción fuera de su destino: '+oid)
  if not f.get('confirmado'):errors.append('Dato propuesto sin confirmar: '+f.get('path',''))
 if any(not r.get('resuelto') for r in c.get('requisitos_de_completitud',[])):errors.append('Brief incompleto')
 if not c.get('aprobacion',{}).get('aprobado') or not c.get('aprobacion',{}).get('evidencia'):errors.append('Falta aprobación comprobable')
 result['case_gate_errors']=errors;result['case_gate']='BLOQUEADO' if errors else 'ESTRUCTURA_COMPLETA; selección de reglas y validación semántica aún necesarias'
print(json.dumps(result,ensure_ascii=False,indent=2))
if len(sys.argv)==1:(R.parent.parent/'7_auditorias_y_verificaciones'/'casos'/'verificacion.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
