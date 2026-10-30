from pathlib import Path
import re,json,csv,hashlib,sqlite3,collections
ROOT=Path(__file__).resolve().parent
SRC=next((ROOT.parent.parent/'3_taxonomia').glob('00688_*.md'))
lines=SRC.read_text().splitlines()
def cells(s):return [x.strip().replace('\\|','|') for x in re.split(r'(?<!\\)\|',s.strip())[1:-1]]
def save(n,x): (ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def csvout(n,rows):
 if not rows:return
 with (ROOT/n).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader()
  for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})
# Destinos de cada faceta y contratos de efecto de F30: datos fijos de este paquete.
facets=json.loads((ROOT/'mapa_facetas.json').read_text()); f30=json.loads((ROOT/'mapa_materias_f30.json').read_text())
terms={};defs={};section='';facet=None;subject='';header=[];branch='';table_idx=0;values=[]
for i,l in enumerate(lines):
 if l.startswith('## Anexo 1'):break
 if l.startswith('#'):
  section=l.lstrip('# ').strip();header=[];branch=''
  m=re.search(r'Faceta (\d+)\.',l)
  if m:facet='F'+m[1].zfill(2);subject=''
  if 'P-01' in l:facet='FLUJO'
  if 'P-04' in l:facet='PUBLICACION'
  if 'P-05' in l:facet='AMBITO'
  if l.startswith('## 6.'):facet='METADATOS'
  if l.startswith('#### «'):subject=re.search('«(.*?)»',l)[1]
  if l.startswith('#### Campo'):subject=re.search('«(.*?)»',l)[1]
 if l.startswith('**Rama'):branch=l.strip('*')
 if not l.startswith('|'):continue
 c=cells(l)
 if i+1<len(lines) and lines[i+1].startswith('|---'):header=c;table_idx+=1;continue
 if not c or c[0].startswith('---'):continue
 if c[0].startswith('TRM-') and len(c)>=9:
  defs[c[0]]={'definition':c[3],'facet':facet,'subject':subject,'section':section,'line':i+1,'definition_support':c[6],'citation':c[8]}
 elif header in [['Etapa','Pasos'],['Rama','Valores']]:
  for val in c[1].split(' · '):
   fid='F02' if header[0]=='Etapa' else 'F29'
   vid='OPT-'+hashlib.sha256((fid+'|'+c[0]+'|'+val).encode()).hexdigest()[:12]
   values.append({'id':vid,'facet':fid,'label':val,'definition':val if fid=='F02' else 'Modelo documentado de rama '+c[0]+'. Capacidades sujetas al contrato específico de fuente.','branch':c[0],'section':section,'line':i+1,'source_cells':dict(zip(header,c))})
 elif header and facet and ('Valor' in header or 'Valor aprobado' in header or header[0] in ['ID conservado','Ámbito funcional']) and not section.startswith('7.'):
  j=header.index('Valor') if 'Valor'in header else 0
  label=c[j]; vid=(c[0] if header[0]=='ID conservado' else 'OPT-'+hashlib.sha256((facet+'|'+branch+'|'+label).encode()).hexdigest()[:12])
  values.append({'id':vid,'facet':facet,'label':label if header[0]!='ID conservado' else c[1],'definition': c[header.index('Definición')] if 'Definición' in header else c[header.index('Definición de diseño aprobada')] if 'Definición de diseño aprobada' in header else c[j+1] if len(c)>j+1 else '', 'branch':c[0] if header[0]=='Rama' else branch,'section':section,'line':i+1,'source_cells':dict(zip(header,c))})
# Canonical concordance, never first arbitrary occurrence
inside=False
for i,l in enumerate(lines):
 if l.startswith('## Anexo 2'):inside=True;continue
 if l.startswith('## Anexo 3'):break
 if not inside or not l.startswith('| TRM-'):continue
 c=cells(l);tid=c[0];d=defs.get(tid,{})
 fm=re.search(r'faceta (\d+)',c[5],re.I); fid='F'+fm[1].zfill(2) if fm else d.get('facet','METADATOS')
 # Current source contract overrides historical concordance
 if tid in ['TRM-0178','TRM-0179']:fid='F14'
 if tid=='TRM-0249':fid='F31'
 if tid=='TRM-1369':fid='PUBLICACION'
 support=c[8]; disposition='VOCABULARIO_OPERATIVO' if support=='COMPLETO' else 'INDICE_DOCUMENTAL' if support=='PRESENCIA' else 'CONCILIACION_HISTORICA'
 if tid in ['TRM-0001','TRM-0002','TRM-0003']:disposition='TRACK_HISTORICO_DEC22'
 terms[tid]={'id':tid,'label':c[2],'alias':c[3],'definition':d.get('definition',c[9]),'facet':fid,'subject':d.get('subject',''),'canonical_destination':c[5],'secondary_destination':c[6],'relation_literal':c[7],'support':support,'disposition':disposition,'citation':c[10],'note':c[11],'section':d.get('section','Anexo 2'),'line':d.get('line',i+1),'concordance_line':i+1}
assert len(terms)==1369,len(terms)
# Facet values are governed options, term records are vocabulary, neither represents a source rule.
extras={'FLUJO':['entrada.ruta.flujo'],'PUBLICACION':['entrada.publicacion'],'AMBITO':['orquestacion.accion'],'METADATOS':['salida.traza.procedencia']}
def paths(fid):return facets[fid]['paths'] if fid in facets else extras.get(fid,['salida.traza.metadatos'])
rows=[]
for r in list(terms.values())+values:
 r=dict(r);r['kind']='TERMINO' if r['id'].startswith('TRM-') else 'VALOR';r.setdefault('disposition','VALOR_AUTORIZADO');r.setdefault('subject','')
 r['logical_paths']=paths(r['facet']);r['physical_paths']=[p.replace('entrada.sujetos[].clase','entrada.sujetos.items[].clase') for p in r['logical_paths']]
 r['destination_inherited_from']=r['facet'];r['activation']='REQUIERE_REGLA_ORIGINAL_CATALOGADA';r['source_sha256']=hashlib.sha256(SRC.read_bytes()).hexdigest()
 if r['disposition'] in ['INDICE_DOCUMENTAL','CONCILIACION_HISTORICA','TRACK_HISTORICO_DEC22']:
  r['physical_paths']=['salida.traza.procedencia'];r['destination_inherited_from']='Contrato §0.6 / DEC22';r['case_selectable']=False
 else:r['case_selectable']=r['facet'] not in ['METADATOS','F30','F31','AMBITO','F01','F02']
 if r['facet']=='F30':r['effect_contract']=f30.get(r.get('subject','') or r['label'],'Destino específico depende de la materia documentada; conservar traza del término.')
 rows.append(r)
# F30 registered values own exact material labels as subject
for r in rows:
 if r['facet']=='F30' and r['kind']=='VALOR':r['subject']=r['label'];r['effect_contract']=f30.get(r['label'],r.get('effect_contract',''))
save('catalogo_opciones.json',rows)
flat=[{'id':r['id'],'kind':r['kind'],'facet':r['facet'],'materia':r['subject'],'label':r['label'],'definition':r['definition'],'disposition':r['disposition'],'case_selectable':r['case_selectable'],'destination_paths':r['physical_paths'],'destination_inherited_from':r['destination_inherited_from'],'effect_contract':r.get('effect_contract',''),'source_section':r['section'],'source_line':r['line'],'source_sha256':r['source_sha256'],'citation':r.get('citation',r.get('source_cells',{}))} for r in rows]
csvout('catalogo_opciones.csv',flat)
ids=collections.Counter(r['id'] for r in rows);assert max(ids.values())==1,[k for k,v in ids.items() if v>1]
save('manifest_fuentes.json',{'taxonomy':{'file':str(SRC.relative_to(ROOT.parent.parent)),'sha256':hashlib.sha256(SRC.read_bytes()).hexdigest()},'limitations':['No se clasificó el corpus de reglas.','No hay asociaciones REG ni pruebas semánticas de activación.','No se afirma exhaustividad de posibles imágenes del mundo.','El inventario contiene valores y vocabulario completos, no combinaciones cartesianas materializadas.']})
save('conteos.json',{'total_records':len(rows),'terms':len(terms),'facet_values':len(values),'facets':len(facets),'by_disposition':dict(collections.Counter(r['disposition'] for r in rows)),'by_facet':dict(collections.Counter(r['facet'] for r in rows)),'case_selectable':sum(r['case_selectable'] for r in rows),'missing_paths':sum(not r['physical_paths'] for r in rows)})
con=sqlite3.connect(ROOT/'casos_opciones.sqlite');con.execute('DROP TABLE IF EXISTS opciones');con.execute('CREATE TABLE opciones (id TEXT PRIMARY KEY, facet TEXT, label TEXT, kind TEXT, case_selectable INTEGER, disposition TEXT, definition TEXT, record_json TEXT)');con.executemany('INSERT INTO opciones VALUES (?,?,?,?,?,?,?,?)',[(r['id'],r['facet'],r['label'],r['kind'],int(r['case_selectable']),r['disposition'],r['definition'],json.dumps(r,ensure_ascii=False)) for r in rows]);con.execute('CREATE INDEX IF NOT EXISTS idx_facet ON opciones(facet)');con.commit();con.close()
print((ROOT/'conteos.json').read_text())
