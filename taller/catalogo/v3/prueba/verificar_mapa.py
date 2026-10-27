"""verificar_mapa.py: control de la tarea 2 del plan (PLAN_FINAL_PRUEBA.md §5).

    python3 -I taller/catalogo/v3/prueba/verificar_mapa.py

Comprueba mapa_tipos.json y casos.json contra sus fuentes y sale con código 1 si algo no cuadra:
- una fila por operación del schema (CONTRATO_IMAGEN_ORQUESTACION.schema.json, entrada.operacion);
- campos propios y mínimo de referencias iguales a CONTRATOS_OPERACION_MODELO.json (operation_contracts);
- adaptador igual a model_adapters (GPT2-GEN / GPT2-EDIT);
- cada INV o ADD citado existe en el universo (universo_prueba_textos.jsonl) o en la adenda (veredicto «entra»);
- cada valor de faceta de los casos existe en v2/esquema_taxonomia.json;
- la operación de cada caso corresponde a su F10, y sus entradas existen;
- cobertura: todos los valores de F15, F32, F11, F13 y F14, los valores de imagen de F10 y los F04 fotográficos
  aprobados (26 §16) aparecen al menos en un caso;
- quality high donde el plan lo exige (§2): retrato, texto extenso o pequeño, F15 persona en composición, edición o
  ancla con identidad.
"""
import json
import re
import sys
from pathlib import Path

V3 = Path(__file__).resolve().parent.parent
CAT = V3.parent
TPL = CAT / "fuentes_20261019/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates"

mapa = json.loads((V3 / "prueba/mapa_tipos.json").read_text(encoding="utf-8"))
casos = json.loads((V3 / "prueba/casos.json").read_text(encoding="utf-8"))
schema = json.loads((TPL / "CONTRATO_IMAGEN_ORQUESTACION.schema.json").read_text(encoding="utf-8"))
contratos = json.loads((TPL / "CONTRATOS_OPERACION_MODELO.json").read_text(encoding="utf-8"))
esquema = json.loads((CAT / "v2/esquema_taxonomia.json").read_text(encoding="utf-8"))
universo = {json.loads(l)["id"] for l in open(V3 / "universo/universo_prueba_textos.jsonl", encoding="utf-8")}
adenda = {d["id"] for d in map(json.loads, open(V3 / "universo/adenda/adenda_universo.jsonl", encoding="utf-8"))
          if d["veredicto"] == "entra"}

fallas = []

# 1. Mapa contra schema y contratos
operaciones = schema["properties"]["entrada"]["properties"]["operacion"]["enum"]
contrato = {o["operacion"]: o for o in contratos["operation_contracts"]}
adaptador = {op: a["id"] for a in contratos["model_adapters"] if "GPT Image 2" in a["models"] for op in a["operations"]}
comunes = mapa["comunes"]
if set(comunes) != set(contrato["genesis"]["required_fields"][:12]):
    fallas.append("mapa: los 12 campos comunes no son los de CONTRATOS")
filas_por_op = {}
for f in mapa["filas"]:
    filas_por_op.setdefault(f["operacion"], []).append(f)
for op in operaciones:
    if op not in filas_por_op:
        fallas.append(f"mapa: falta la operación {op}")
for op, filas in filas_por_op.items():
    if op not in operaciones:
        fallas.append(f"mapa: operación {op} no está en el schema")
        continue
    c = contrato[op]
    for f in filas:
        if f["campos_propios"] != c["required_fields"][12:]:
            fallas.append(f"mapa {f['tipo']}: campos propios {f['campos_propios']} ≠ {c['required_fields'][12:]}")
        if f["referencias_min"] != c["references_min"]:
            fallas.append(f"mapa {f['tipo']}: referencias_min {f['referencias_min']} ≠ {c['references_min']}")
        if f["template"] != c["template_id"]:
            fallas.append(f"mapa {f['tipo']}: template {f['template']} ≠ {c['template_id']}")
        if f["adaptador"] != adaptador.get(op):
            fallas.append(f"mapa {f['tipo']}: adaptador {f['adaptador']} ≠ {adaptador.get(op)}")

# 2. Ids citados
citados = set()
for f in mapa["filas"]:
    citados |= set(f["gobierna"])
for c in casos["casos"]:
    citados |= set(re.findall(r"(?:INV-\d{6}|ADD-\d{4})", c["plantilla"]))
for i in sorted(citados):
    if i not in universo and i not in adenda:
        fallas.append(f"id citado que no está en el universo ni en la adenda: {i}")

# 3. Valores de faceta, operación, entradas
valores = {k: {v["valor"] if isinstance(v, dict) else v for v in f["valores"]} for k, f in esquema["facetas"].items()}
F10_OP = {"génesis sin referencias (caso 1, T1)": {"genesis"}, "análisis de imagen a prompt": {"genesis"},
          "composición de varias referencias": {"composicion_referencias"},
          "ancla con referencias (caso 2, T2 a T4)": {"ancla_referencia", "ancla_ff", "ancla_lf"},
          "transferencia de estilo": {"transferencia_estilo"}, "boceto o wireframe a final": {"boceto_a_final"}}
F10_IMAGEN = set(F10_OP) | {"edición de imagen existente (T5)"} | {v for v in valores["F10"] if v.startswith("edición: ")}
ids_casos = {c["id"] for c in casos["casos"]}
ids_entradas = {e["id"] for e in casos["entradas"]}
DE_LA_FOTO = "de_la_foto"
for c in casos["casos"]:
    for fac in ("F04", "F10", "F11", "F13", "F14", "F15", "F32"):
        v = c[fac]
        if v is None or v == DE_LA_FOTO:
            continue
        if v not in valores[fac]:
            fallas.append(f"{c['id']}: {fac} «{v}» no está en el esquema")
    ops = F10_OP.get(c["F10"], {"edicion"} if c["F10"] in F10_IMAGEN else set())
    if c["operacion"] not in ops:
        fallas.append(f"{c['id']}: operación {c['operacion']} no corresponde a F10 «{c['F10']}»")
    minimo = contrato[c["operacion"]]["references_min"]
    if len(c["entradas"]) < minimo:
        fallas.append(f"{c['id']}: {len(c['entradas'])} entradas, el contrato pide al menos {minimo}")
    for e in c["entradas"]:
        if e not in ids_casos and e not in ids_entradas:
            fallas.append(f"{c['id']}: entrada {e} no existe")
    if c["F10"] == "análisis de imagen a prompt" and c["entradas"] != ["E7"]:
        fallas.append(f"{c['id']}: la descripción usa la foto E7 y nada más (26 §14)")

# 4. Cobertura
def cubiertos(fac):
    return {c[fac] for c in casos["casos"]}
requeridos = {"F15": valores["F15"], "F32": valores["F32"], "F11": valores["F11"], "F13": valores["F13"],
              "F14": valores["F14"], "F10": F10_IMAGEN, "F04": set(casos["F04_fotograficos"])}
for fac, req in requeridos.items():
    faltan = sorted(req - cubiertos(fac))
    if faltan:
        fallas.append(f"cobertura {fac}: sin caso para {faltan}")
for v in casos["F04_fotograficos"]:
    if v not in valores["F04"]:
        fallas.append(f"F04 fotográfico «{v}» no está en el esquema")

# 5. Quality high obligatoria (§2 del plan)
for c in casos["casos"]:
    identidad = c["F15"] == "persona" and c["operacion"] in ("composicion_referencias", "edicion", "ancla_referencia")
    obligado = c["F04"] == "retrato" or c["F32"] == "texto extenso o pequeño" or identidad
    if obligado and c["quality"] != "high":
        fallas.append(f"{c['id']}: quality debe ser high (§2 del plan)")

print(f"operaciones {len(operaciones)} · filas del mapa {len(mapa['filas'])} · casos {len(casos['casos'])} · "
      f"entradas {len(casos['entradas'])} · ids citados {len(citados)}")
for f in fallas:
    print("  FALLA", f)
print("OK" if not fallas else f"{len(fallas)} fallas")
sys.exit(1 if fallas else 0)
