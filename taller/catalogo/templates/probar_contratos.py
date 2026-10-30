"""Fixtures sintéticos de estructura: no son testigos semánticos de reglas."""
import copy,json,hashlib,pathlib
from verificar_templates import validate_instance,C,R
P=pathlib.Path(__file__).parent
def put(x,path,v):
 bits=path.split('.');node=x
 for bit in bits[:-1]:node=node.setdefault(bit,{})
 node.setdefault(bits[-1],v)
c=next(o for o in C['operation_contracts'] if o['operacion']=='genesis')
x={'contrato_id':'T-GENESIS+GPT2-GEN','version':'20261019','procedencia_campos':[]}
types={f['path']:f['type'] for f in R['fields']}
for p in c['required_fields']:
 t=types.get(p,'object');v=[] if t.startswith('array') else 0 if t=='integer' else {} if t=='object' else 'valor sintético'
 put(x,p,v)
 x['procedencia_campos'].append({'path':p,'origen':'usuario','fuente':'FIXTURE-ESTRUCTURAL','valor_sha256':'fixture','aprobacion_id':'FIXTURE-APPROVAL'})
x['entrada']['operacion']='genesis';x['entrada']['ruta']['flujo']='FL02';x['entrada']['modelo']['nombre']='GPT Image 2';x['entrada']['formato']['ratio']='1:1'
x['salida']={'prompt':'Scene: Fondo blanco.\nSubject: Cubo.\nImportant Details: Luz lateral suave.\nUse Case: Estudio geométrico.\nConstraints: Un solo cubo.'}
def approve(x):x['aprobacion_brief']={'aprobado':True,'mensaje_id':'FIXTURE-APPROVAL','brief_sha256':hashlib.sha256(json.dumps(x['entrada'],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()}
approve(x); tests=[]
def run(name,obj,want,stage='salida'):
 errors=validate_instance(obj,stage);good=(bool(errors)==want);tests.append({'test':name,'expected_rejection':want,'passed':good,'errors':errors});assert good,(name,errors)
run('brief_aprobado_y_cinco_slots',x,False)
y=copy.deepcopy(x);del y['aprobacion_brief'];run('sin_aprobacion',y,True)
y=copy.deepcopy(x);y['entrada']['pieza']['objetivo']='cambio';run('aprobacion_invalidada_por_cambio',y,True)
y=copy.deepcopy(x);y['salida']['prompt']='Create '+y['salida']['prompt'];run('prefijo_fuera_slots',y,True)
y=copy.deepcopy(x);y['salida']['prompt']=y['salida']['prompt'].replace('Constraints: Un solo cubo.','');run('slot_omitido',y,True)
y=copy.deepcopy(x);y['salida']['prompt']+=' {{luz}}';run('variable_sin_sustituir',y,True)
y=copy.deepcopy(x);y['salida']['prompt']+=' photorealistic';run('lexico_prohibido',y,True)
y=copy.deepcopy(x);y['entrada']['referencias']=[{'archivo':'fixture.png'}];approve(y);run('genesis_con_referencia',y,True)
y=copy.deepcopy(x);y['entrada']['operacion']='edicion';approve(y);run('edicion_sin_preserve_ni_ref',y,True)
y=copy.deepcopy(x);y['entrada']['rostro']={'ocupacion':1.2};approve(y);run('proporcion_fuera_dominio',y,True)
y=copy.deepcopy(x);y['entrada']['modelo']['nombre']='Nano Banana 2';approve(y);y['salida']['prompt']='Subject at 50mm and f/2.8.';run('optica_numerica_NB',y,True)
y=copy.deepcopy(x);y['entrada']['modulos_activos']=['fotografia'];approve(y);run('fotografia_sin_luz_camara',y,True)
y=copy.deepcopy(x);y['entrada']['operacion']='edicion';y['entrada']['edicion']={'cambio':'Cambiar cubo a azul','preservar':['geometría','luz']};y['entrada']['referencias']=[{'archivo':'fixture.png','sha256':'0'*64,'medio':'imagen','rol':'base','indice':1}]
for p in ['entrada.edicion.cambio','entrada.edicion.preservar','entrada.referencias']:y['procedencia_campos'].append({'path':p,'origen':'usuario','fuente':'FIXTURE','valor_sha256':'fixture','aprobacion_id':'FIXTURE-APPROVAL'})
approve(y);y['salida']['prompt']='Change: Cubo azul.\nPreserve: Geometría y luz.\nConstraints: Solo cambiar color.';run('edicion_valida_sin_redefinir_luz_camara',y,False)
y=copy.deepcopy(y);y['entrada']['referencias']=[];approve(y);run('edicion_con_referencias_vacias',y,True)
(P/'RESULTADOS_PRUEBAS_ESTRUCTURALES.json').write_text(json.dumps({'scope':'Pruebas sintéticas del contrato. No acreditan selección de reglas ni calidad de imagen.','tests':tests,'passed':sum(t['passed'] for t in tests),'total':len(tests)},ensure_ascii=False,indent=2)+'\n')
print('Passed',len(tests),'synthetic structural checks')
