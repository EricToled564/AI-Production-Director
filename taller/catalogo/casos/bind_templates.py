from pathlib import Path
import json,sqlite3,csv
R=Path(__file__).resolve().parent; T=R.parent/'templates'; reg=json.loads((T/'REGISTRO_DESTINOS_TEMPLATE.json').read_text())
m={'orquestación y control de flujo':['orquestacion'],'estrategia y concepto':['entrada.pieza.objetivo'],'estructura narrativa y diálogo':['entrada.contexto_narrativo'],'dramaturgia':['entrada.accion','entrada.sujetos.items[].expresion'],'encuadre y lente':['entrada.camara'],'ángulo':['entrada.camara.angulo'],'movimiento de cámara':['entrada.ancla.contexto_clip.camara'],'luz':['entrada.luz'],'color, grade y textura':['entrada.color_material'],'composición':['entrada.composicion'],'identidad y consistencia':['entrada.identidad'],'anatomía, rostro y piel':['entrada.sujetos.items[].rasgos','entrada.rostro'],'física y movimiento congelado':['entrada.fisica','entrada.accion'],'texto en pantalla':['entrada.texto_marca'],'marca y logos':['entrada.texto_marca.logos_aprobados'],'estructura y sintaxis del prompt':['salida.slots','salida.validaciones'],'parámetros técnicos':['salida.parametros'],'audio':['entrada.ancla.contexto_clip.audio'],'continuidad entre clips':['entrada.ancla'],'crítica y revisión':['salida.validaciones','salida.aceptacion'],'trazabilidad y entrega':['salida.traza','salida.handoff'],'materialidad y superficie':['entrada.color_material.materiales','entrada.color_material.texturas','entrada.color_material.acabado'],'puesta en escena y blocking':['entrada.blocking','entrada.sujetos.items[].posicion'],'animación':['entrada.ancla.contexto_clip.animacion']}
m=reg['f30_destinations']
rows=json.loads((R/'catalogo_opciones.json').read_text());schema=json.loads((T/'CONTRATO_IMAGEN_ORQUESTACION.schema.json').read_text())
def exists(path):
 s=schema
 for p in path.split('.'):
  arr=p.endswith('[]'); k=p[:-2] if arr else p
  if k not in s.get('properties',{}):return False
  s=s['properties'][k]
  if arr:
   if s.get('type')!='array':return False
   s=s['items']
 return True
for r in rows:
 if r['disposition'] in ['INDICE_DOCUMENTAL','CONCILIACION_HISTORICA','TRACK_HISTORICO_DEC22']:p=['salida.traza.procedencia']
 elif r['facet']=='F30':
  p=m[r['subject']];r['destination_inherited_from']='F30 / '+r['subject'];r['case_selectable']=r['kind']=='TERMINO' and r['subject'] not in ['estructura y sintaxis del prompt','crítica y revisión','trazabilidad y entrega','orquestación y control de flujo','parámetros técnicos']
 elif r['facet']=='AMBITO' and r['label'] in reg['scope_destinations']:p=reg['scope_destinations'][r['label']]
 else:p=[reg['facet_destinations'].get({'PUBLICACION':'P-04','FLUJO':'P-01','METADATOS':'E','AMBITO':'P-05'}.get(r['facet'],r['facet']))]
 assert all(p) and all(exists(x) for x in p),(r['id'],p)
 r['physical_paths']=p;r['template_schema']='../templates/CONTRATO_IMAGEN_ORQUESTACION.schema.json';r['path_check']='EXISTE_EN_SCHEMA'
(R/'catalogo_opciones.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(R/'mapa_materias_f30_paths.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
with (R/'catalogo_opciones.csv').open('w') as f:
 fields=['id','kind','facet','subject','label','definition','disposition','case_selectable','physical_paths','destination_inherited_from','effect_contract','section','line','source_sha256','citation','path_check'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in rows:w.writerow({k:json.dumps(r.get(k,''),ensure_ascii=False) if isinstance(r.get(k,''),(dict,list)) else r.get(k,'') for k in fields})
con=sqlite3.connect(R/'casos_opciones.sqlite')
for r in rows:con.execute('UPDATE opciones SET case_selectable=?,record_json=? WHERE id=?',(int(r['case_selectable']),json.dumps(r,ensure_ascii=False),r['id']))
con.commit();con.close()
c=json.loads((R/'conteos.json').read_text());c['case_selectable']=sum(r['case_selectable'] for r in rows);c['schema_paths_checked']=sum(len(r['physical_paths']) for r in rows);c['schema_path_errors']=0;(R/'conteos.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print(c)
