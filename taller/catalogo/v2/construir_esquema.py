"""construir_esquema.py: esquema de clasificación extraído de la taxonomía original del 2026-10-19.

Nada se escribe a mano salvo la cita de las líneas de la taxonomía de donde sale cada lista de §6/§7 que no
está tabulada con ID, y las extensiones aprobadas por Eric el 2026-10-23, que quedan marcadas aparte con
origen "extension_aprobada" para que el control de coincidencia las cuente por separado.

    python3 construir_esquema.py <carpeta_docs>
"""
import csv
import hashlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
DOCS = Path(sys.argv[1])
TAX = DOCS / "p2/ARCHIVOS/00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md"
CASOS = DOCS / "59239886-CASOS_OPCIONES_TAXONOMIA_20261019/casos"
TPL = DOCS / "08fe4a51-TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates"
lineas = TAX.read_text().splitlines()
cat = json.loads((CASOS / "catalogo_opciones.json").read_text())
mapa = json.loads((CASOS / "mapa_facetas_v5.json").read_text())


def cita(n):
    """Devuelve la línea n de la taxonomía para dejar constancia literal de dónde sale una lista."""
    return {"linea": n, "texto": lineas[n - 1][:400]}


def valor(label, origen, id_=None, definicion="", linea=None):
    return {"valor": label, "origen": origen, "id": id_, "definicion": definicion, "linea": linea}


esquema = {"taxonomia": TAX.name, "taxonomia_sha256": hashlib.sha256(TAX.read_bytes()).hexdigest(),
           "facetas": {}, "campos": {}, "terminos": [], "destinos": [], "extensiones": []}

# Facetas F01–F31 y subcategorías P-01 (flujo) y P-04 (lugar de publicación): valores autorizados con ID.
for r in cat:
    if r["disposition"] != "VALOR_AUTORIZADO":
        continue
    clave = {"FLUJO": "P01", "PUBLICACION": "P04"}.get(r["facet"], r["facet"])
    if clave == "AMBITO":
        continue
    esquema["facetas"].setdefault(clave, {"nombre": mapa.get(clave, {}).get("label", clave), "valores": []})
    esquema["facetas"][clave]["valores"].append(valor(r["label"], "taxonomia_original", r["id"], r["definition"], r["line"]))
esquema["facetas"]["P01"]["nombre"] = "Flujo (P-01)"
esquema["facetas"]["P04"]["nombre"] = "Lugar de publicación (P-04, dentro de F04)"
ambito = [r for r in cat if r["facet"] == "AMBITO" and r["disposition"] == "VALOR_AUTORIZADO"]
esquema["campos"]["ambito_funcional"] = [valor(r["label"], "taxonomia_original", r["id"], r["definition"], r["line"])
                                         for r in ambito[:8]]
esquema["campos"]["uso_operativo"] = [valor(r["label"], "taxonomia_original", r["id"], r["definition"], r["line"])
                                      for r in ambito[8:]]

# Campos de §6.1 con término TRM.
por_campo = {}
for r in cat:
    if r["facet"] == "METADATOS" and r["disposition"] in ("VOCABULARIO_OPERATIVO", "INDICE_DOCUMENTAL"):
        por_campo.setdefault(r["subject"], []).append(valor(r["label"], "taxonomia_original", r["id"], r["definition"], r["line"]))
esquema["campos"]["medio"] = por_campo["medio"]
esquema["campos"]["tipo_enunciado"] = por_campo["tipo de enunciado"]
esquema["campos"]["operador_condicion"] = por_campo["operador de condición"]
esquema["campos"]["estado_evidencia"] = por_campo["estado de evidencia"]
esquema["campos"]["dependencia"] = por_campo["dependencia"]
esquema["campos"]["evidencia_afirmacion_fuente"] = por_campo["evidencia de la afirmación fuente"]

# Campos de §6.0/§6.1 cuyos valores la taxonomía da en texto (se cita la línea exacta).
TEXTO = {
    "unidad": ("| unidad |", por_campo["unidad"] + [valor(v, "taxonomia_original", None, "valor C16 de §6.0", None)
                                         for v in ("documento", "archivo", "paquete de entrega", "registro (run)", "campo o esquema")]),
    "objeto_regulado": ("| objeto regulado |", [valor(v, "taxonomia_original", None, "§6.0", None) for v in
                               ("activo visual o sonoro", "documento", "archivo", "paquete de entrega",
                                "registro de ejecución (run)", "campo o esquema")]),
    "idioma": ("| idioma del enunciado |", [valor(v, "taxonomia_original", None, "§6.0", None) for v in ("en", "es", "ru")]),
    "fuerza_normativa": ("«Sin fuerza normativa» codifica", por_campo["fuerza normativa"] + [valor("Sin fuerza normativa", "taxonomia_original", None,
                                                                      "estado no normativo de §6.1", None)]),
    "origen_evidencia": ("Valor añadido: «Decisión del usuario»", [v for v in por_campo["origen de evidencia"] if v["id"] != "TRM-1330"]
                         + [valor("Decisión del usuario", "taxonomia_original", None, "delta DOC01 de §6.1", None)]),
    "adopcion_canonica": ("| adopción canónica |", por_campo["adopción canónica"] + [valor(v, "taxonomia_original", None, "§6.0", None) for v in
                                                                ("adopción documental", "excluida por decisión del usuario",
                                                                 "refutada", "histórica")]),
    "estado_modelo_citado": ("| estado del modelo citado |", [valor(v, "taxonomia_original", None, "§6.0", None) for v in ("vigente", "histórico")]),
    "estado_faceta": ("1.2 Dos formas de alcance", [valor(v, "taxonomia_original", None, "§1.2", None) for v in ("VALOR", "UNIVERSAL")]),
    "grupo_condicion": ("Una condición es un grupo con operador", [valor(v, "taxonomia_original", None, "§7.2", None) for v in ("TODAS", "ALGUNA", "NINGUNA")]),
    "operador_atomo": ("Una condición es un grupo con operador", [valor(v, "taxonomia_original", None, "§7.2", None) for v in
                              ("=", "≠", "∈", "∉", "<", "≤", ">", "≥", "entre", "existe", "no existe")]),
    "tipo_conciliacion": ("1. Cero reglas o puntos pertinentes", [valor(v, "taxonomia_original", None, "Gate final §1", None) for v in
                                 ("estructura", "código auxiliar", "duplicado referenciado", "otro contenido no normativo")]),
}
for campo, (clave, vals) in TEXTO.items():
    n = next(i for i, l in enumerate(lineas, 1) if clave in l)
    for v in vals:
        v["linea"] = v["linea"] or n
        if v["id"] is None:  # un valor tomado del texto debe aparecer literal en su línea
            assert v["valor"] in lineas[n - 1], f"{campo}: «{v['valor']}» no está en la línea {n}"
    esquema["campos"][campo] = vals
    esquema.setdefault("citas_de_listas", {})[campo] = cita(n)

# Términos del tesauro: solo vocabulario operativo (§0.6: los índices documentales no activan categorías).
esquema["terminos"] = [{"id": r["id"], "termino": r["label"], "faceta": r["facet"], "materia": r.get("subject", ""),
                        "definicion": r["definition"]} for r in cat if r["disposition"] == "VOCABULARIO_OPERATIVO"]

# Destinos: rutas existentes del contrato de templates.
schema = json.loads((TPL / "CONTRATO_IMAGEN_ORQUESTACION.schema.json").read_text())
rutas = []


def recorrer(n, p):
    if isinstance(n, dict):
        for k, v in n.get("properties", {}).items():
            rutas.append(p + k)
            recorrer(v, p + k + ".")
        if "items" in n:
            recorrer(n["items"], p[:-1] + "[]." if p else "")
        for k in ("allOf", "anyOf", "oneOf"):
            for x in n.get(k, []):
                recorrer(x, p)


recorrer(schema, "")
esquema["destinos"] = sorted(set(rutas))

# Extensiones aprobadas por Eric el 2026-10-23 (no son taxonomía original; se cuentan aparte).
EXT = {"F04": ["infografía o diagrama", "concept art", "pieza de portafolio"],
       "F05": ["finanzas y banca", "sector público"], "F06": ["3:2"],
       "F10": ["edición: quitar objeto", "edición: añadir objeto", "edición: cambiar luz o clima", "edición: colorizar",
               "edición: restaurar", "edición: traducir texto", "análisis de imagen a prompt"],
       "F17": ["anclado en época, cultura o autor", "brutalista", "futurista"]}
for f, vals in EXT.items():
    for v in vals:
        esquema["facetas"][f]["valores"].append(valor(v, "extension_aprobada_2026-10-23", None,
                                                      "hijo de edición (T5)" if v.startswith("edición:") else ""))
        esquema["extensiones"].append({"faceta": f, "valor": v})
for f, nombre, vals in (("F32", "Texto en la imagen", ["sin texto", "texto corto", "texto extenso o pequeño"]),
                        ("F33", "Complejidad de escena", ["simple", "compleja (5 o más elementos)"]),
                        ("F34", "Resolución", ["1K", "2K", "4K"])):
    esquema["facetas"][f] = {"nombre": nombre, "valores": [valor(v, "extension_aprobada_2026-10-23") for v in vals]}
    esquema["extensiones"] += [{"faceta": f, "valor": v} for v in vals]

(AQUI / "esquema_taxonomia.json").write_text(json.dumps(esquema, ensure_ascii=False, indent=1))
print("facetas", {k: len(v["valores"]) for k, v in sorted(esquema["facetas"].items())})
print("campos", {k: len(v) for k, v in esquema["campos"].items()})
print("términos", len(esquema["terminos"]), "· destinos", len(esquema["destinos"]),
      "· extensiones", len(esquema["extensiones"]))
for campo, c in esquema["citas_de_listas"].items():
    print(f"  {campo} ← línea {c['linea']}: {c['texto'][:110]}")
