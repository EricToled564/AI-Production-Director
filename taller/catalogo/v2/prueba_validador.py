"""prueba_validador.py: cada caso incorrecto DEBE ser rechazado por validar_v2; el correcto DEBE pasar."""
import copy, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validar_v2 import validar
E = json.load(open("esquema_taxonomia.json"))
F = ["P01"] + [f"F{i:02d}" for i in range(1, 30)] + ["P04", "F32", "F33", "F34"]
u = {"estado": "UNIVERSAL", "valores": [], "evidencia": "sin restricción en cuerpo"}
lote = [{"id": "INV-1"}]
base = {"id": "INV-1", "tipo_registro": "regla", "unidades": ["INV-1"], "contexto": "x",
 "bloque_E": {"idioma": "en", "objeto_regulado": "activo visual o sonoro", "medio": "Imagen fija", "unidad": "Fotograma",
   "tipo_enunciado": "Prescripción", "fuerza_normativa": "Obligación", "origen_evidencia": "Evidencia directa",
   "evidencia_afirmacion_fuente": "Afirmación fuente por contrastar", "adopcion_canonica": "adopción documental",
   "estado_modelo_citado": None, "estado_evidencia": None, "dependencia": None, "autoridad": None, "precedencia": None},
 "bloque_D": {"F30": {"estado": "VALOR", "valores": ["luz"], "evidencia": "habla de luz"},
   "F31": {"estado": "VALOR", "valores": ["no"], "evidencia": "no bloquea"}, "terminos": [], "ambito_funcional": ["Creación de imagen"]},
 "aplicaciones": [{"aplicacion_id": "A1", "ruta": {"flujo": "FL02 Génesis sin referencia", "seccion": "s",
   "paso": "E5.2 génesis sin referencias", "condicion": "c"}, "uso_operativo": "ACTIVO EN SELECCIÓN",
   "destinos": ["salida.slots.Scene"], "condicion": {"grupo": "TODAS", "miembros": [{"campo": "F32", "operador": "∈", "valor": ["texto corto"]}]},
   "adopcion": "adopción documental", "facetas": {f: dict(u) for f in F}}]}
def con(fn):
    r = copy.deepcopy(base); fn(r); return r
casos = {
 "condición con texto libre en ruta del contrato": con(lambda r: r["aplicaciones"][0]["condicion"]["miembros"].append(
     {"campo": "entrada.modulos_activos", "operador": "∈", "valor": ["trabajo por lotes (batch)"]})),
 "valor inventado en faceta": con(lambda r: r["aplicaciones"][0]["facetas"].update(F17={"estado": "VALOR", "valores": ["cyberpunk"], "evidencia": "dice cyberpunk"})),
 "valor inventado en condición de faceta": con(lambda r: r["aplicaciones"][0]["condicion"]["miembros"].append({"campo": "F04", "operador": "∈", "valor": ["infografía"]})),
 "valor inventado en campo tipado": con(lambda r: r["bloque_E"].update(objeto_regulado="imagen")),
 "faceta faltante": con(lambda r: r["aplicaciones"][0]["facetas"].pop("F25")),
 "estado NO APLICA": con(lambda r: r["aplicaciones"][0]["facetas"].update(F26={"estado": "NO APLICA", "valores": [], "evidencia": "es imagen fija"})),
 "valor pendiente": con(lambda r: r["aplicaciones"][0]["facetas"].update(F04={"estado": "VALOR", "valores": ["pendiente"], "evidencia": "no se sabe"})),
 "UNIVERSAL sin evidencia": con(lambda r: r["aplicaciones"][0]["facetas"].update(F05={"estado": "UNIVERSAL", "valores": [], "evidencia": ""})),
 "medio en rama documento": con(lambda r: r["bloque_E"].update(objeto_regulado="documento")),
 "destino inexistente": con(lambda r: r["aplicaciones"][0].update(destinos=["salida.slots.Mood"])),
 "término TRM inexistente": con(lambda r: r["bloque_D"].update(terminos=["TRM-9999"])),
 "unidad sin cubrir": con(lambda r: r.update(unidades=["INV-2"], id="INV-2")),
 "operador de rango sobre faceta cerrada": con(lambda r: r["aplicaciones"][0]["condicion"]["miembros"].append({"campo": "F19", "operador": ">", "valor": "2"})),
}
fallos = 0
print("correcto pasa:", "SÍ" if not validar(lote, [base]) else "NO  " + str(validar(lote, [base])[:2]))
fallos += bool(validar(lote, [base]))
for nombre, r in casos.items():
    e = validar(lote, [r])
    print(("RECHAZA  " if e else "¡ACEPTA! ") + nombre + ("" if not e else "  → " + e[0][:90]))
    fallos += not e
print("RESULTADO:", "todas las pruebas correctas" if not fallos else f"{fallos} pruebas fallan")
