"""probar_verificar_templates.py: verificar_templates.validate_instance con las formas que el plan necesita.

    python3 -I taller/catalogo/v3/prueba/probar_verificar_templates.py

Parte del fixture de `probar_contratos.py` (génesis aprobada con 5 slots) y prueba lo que el plan pide y ese archivo
no cubre: descripción de imagen con procedencia por inferencia (26 §14), F32 en selecciones_taxonomicas, texto_marca,
texto literal entre comillas dentro de un slot, ancla con la tarjeta D1–D9, LF, y los rechazos esperados. Sale con
código 1 si un resultado no es el esperado.
"""
import copy
import hashlib
import json
import sys
from pathlib import Path

TPL = Path(__file__).resolve().parents[2] / "fuentes_20261019/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates"
sys.path.insert(0, str(TPL))
from verificar_templates import C, R, validate_instance  # noqa: E402

TIPOS = {f["path"]: f["type"] for f in R["fields"]}
CONTRATO = {o["operacion"]: o for o in C["operation_contracts"]}
FOTO = "a" * 64


def put(x, path, v):
    bits = path.split(".")
    node = x
    for bit in bits[:-1]:
        node = node.setdefault(bit, {})
    node[bits[-1]] = v


def procedencia(x, path, origen="usuario", fuente="BRIEF"):
    x["procedencia_campos"].append({"path": path, "origen": origen, "fuente": fuente,
                                    "valor_sha256": "0" * 64, "aprobacion_id": "MSG"})


def base(operacion):
    x = {"contrato_id": "prueba", "version": "20261019", "procedencia_campos": []}
    for p in CONTRATO[operacion]["required_fields"]:
        t = TIPOS.get(p, "object")
        put(x, p, [] if t.startswith("array") else 0 if t == "integer" else {} if t == "object" else "valor")
        procedencia(x, p)
    e = x["entrada"]
    e["operacion"] = operacion
    e["ruta"]["flujo"] = "FL04"
    e["modelo"].update(nombre="GPT Image 2", version="2", interfaz="App de ChatGPT para escritorio")
    e["formato"]["ratio"] = "4:5"
    e["idioma_prompt"] = "en"
    e["selecciones_taxonomicas"] = ["F10: génesis sin referencias (caso 1, T1)", "F32: sin texto"]
    return x


def aprobar(x):
    x["aprobacion_brief"] = {"aprobado": True, "mensaje_id": "MSG", "brief_sha256": hashlib.sha256(
        json.dumps(x["entrada"], ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()}
    return x


GEN = ("Scene: A vertical 4:5 photograph of a quiet street cafe at dusk.\nSubject: A hand-painted wooden sign.\n"
       "Important Details: The sign reads \"Florista\" in white serif letters.\nUse Case: Editorial thumbnail.\n"
       "Constraints: No extra words, no duplicate text, no watermarks.")
resultados = []


def run(nombre, x, etapa, rechazo):
    err = validate_instance(x, etapa)
    ok = bool(err) == rechazo
    resultados.append((nombre, ok, err))


# Génesis con texto del mundo (K08): F32 en selecciones_taxonomicas, texto_marca, literal entre comillas en un slot
g = base("genesis")
g["entrada"]["selecciones_taxonomicas"] = ["F10: génesis sin referencias (caso 1, T1)", "F32: texto corto"]
g["entrada"]["texto_marca"] = {"literales": ["Florista"], "posicion": "letrero sobre la puerta", "tipografia": "serif blanca"}
g["salida"] = {"prompt": GEN}
run("K08 génesis con texto del mundo, salida válida", aprobar(g), "salida", False)
y = copy.deepcopy(g)
y["salida"]["prompt"] = GEN.replace("\"Florista\"", "\"Florista...\"")
run("literal con elipsis: rechazado (L59)", y, "salida", True)
y = copy.deepcopy(g)
y["entrada"]["texto_marca"]["color"] = "blanco"
run("texto_marca con campo fuera del schema: rechazado", aprobar(y), "salida", True)
y = copy.deepcopy(g)
y["entrada"]["modelo"]["nombre"] = "GPT Image 2 "
y = aprobar(y)
y["salida"]["prompt"] = "Create " + GEN
run("nombre de modelo distinto de «GPT Image 2»: el control de slots no corre (no rechaza)", y, "salida", False)

# Descripción de imagen (K32): génesis, sin referencias, valores con origen inferencia_para_aprobacion y la foto como fuente
d = base("genesis")
d["procedencia_campos"] = [p for p in d["procedencia_campos"] if p["path"] not in ("entrada.sujetos", "entrada.escena")]
procedencia(d, "entrada.sujetos", "inferencia_para_aprobacion", "E7 sha256:" + FOTO)
procedencia(d, "entrada.escena", "inferencia_para_aprobacion", "E7 sha256:" + FOTO)
d["salida"] = {"prompt": GEN}
run("K32 descripción con procedencia por inferencia: válida", aprobar(d), "salida", False)
y = copy.deepcopy(d)
y["entrada"]["referencias"] = [{"archivo": "E7.png", "sha256": FOTO, "medio": "imagen", "rol": "foto", "indice": 1}]
run("K32 con la foto adjunta: rechazado (26 §14)", aprobar(y), "salida", True)
y = copy.deepcopy(d)
y["procedencia_campos"][-1]["origen"] = "deducido"
run("origen fuera del schema: rechazado", aprobar(y), "salida", True)

# Ancla con referencia (K33): tarjeta D1–D9 obligatoria
a = base("ancla_referencia")
for k in ("estilo", "color_material", "camara", "luz", "accion", "sujetos"):
    a["entrada"].setdefault(k, {})
run("ancla sin tarjeta D1–D9 llena: rechazada", aprobar(copy.deepcopy(a)), "brief", True)

# LF (K36): campos propios de T-ANCLA-LF
lf = base("ancla_lf")
del lf["entrada"]["ancla"]["estado_final"]
run("LF sin estado final: rechazado", aprobar(lf), "brief", True)

# Edición (K14): GPT2-EDIT en su orden
e = base("edicion")
e["entrada"]["edicion"] = {"cambio": "Remove the bicycle", "preservar": ["geometry", "light"]}
e["entrada"]["referencias"] = [{"archivo": "K02.png", "sha256": FOTO, "medio": "imagen", "rol": "base", "indice": 1}]
e["salida"] = {"prompt": "Change: Remove the bicycle. Do not change anything else.\nPreserve: Geometry, light.\nConstraints: One change."}
run("K14 edición válida", aprobar(e), "salida", False)
y = copy.deepcopy(e)
y["salida"]["prompt"] = "Preserve: Geometry.\nChange: Remove the bicycle.\nConstraints: One change."
run("edición con slots fuera de orden: rechazada", y, "salida", True)

# Aprobación ligada al hash
y = copy.deepcopy(g)
y["entrada"]["pieza"]["objetivo"] = "otro"
run("brief cambiado tras aprobar: rechazado", y, "seleccion", True)

fallos = 0
for nombre, ok, err in resultados:
    print(("  ok    " if ok else "  FALLA ") + nombre + ("" if ok else f" -> {err}"))
    fallos += not ok
print(f"{len(resultados) - fallos}/{len(resultados)} como se esperaba")
sys.exit(1 if fallos else 0)
