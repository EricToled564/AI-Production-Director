"""match_taxonomia.py: coincidencia de TODAS las etiquetas usadas en la catalogación con la taxonomía original.

Recorre salidas/*.json, extrae cada etiqueta (valores de faceta, campos de §6, términos TRM, destinos, operadores) y
la busca en esquema_taxonomia.json. Informa el porcentaje de coincidencia exacta, cuántas usan extensiones
aprobadas el 2026-10-23 y la cobertura inversa (valores de la taxonomía con y sin reglas). Sale con código 1 si
la coincidencia no es 100%.
"""
import collections
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
E = json.loads((AQUI / "esquema_taxonomia.json").read_text())
origen = {}
for f, d in E["facetas"].items():
    for v in d["valores"]:
        origen[("faceta", f, v["valor"])] = v["origen"]
for c, vals in E["campos"].items():
    for v in vals:
        origen[("campo", c, v["valor"])] = v["origen"]
for t in E["terminos"]:
    origen[("termino", "TRM", t["id"])] = "taxonomia_original"
for d in E["destinos"]:
    origen[("destino", "contrato", d)] = "contrato_templates"

usadas = collections.Counter()


def usar(*clave):
    usadas[clave] += 1


def faceta(f, v):
    usar("campo", "estado_faceta", v["estado"])
    for x in v["valores"]:
        usar("faceta", f, x)


def cond(g):
    usar("campo", "grupo_condicion", g["grupo"])
    for m in g["miembros"]:
        if "grupo" in m:
            cond(m)
        else:
            usar("campo", "operador_atomo", m["operador"])
            if ("faceta", m["campo"], "") and m["campo"] in E["facetas"] and m["operador"] in ("=", "≠", "∈", "∉"):
                for x in (m["valor"] if isinstance(m["valor"], list) else [m["valor"]]):
                    usar("faceta", m["campo"], x)


reglas = conciliaciones = 0
for s in sorted((AQUI / "salidas").glob("salida_*.json")):
    for r in json.loads(s.read_text()):
        if r["tipo_registro"] == "conciliacion":
            conciliaciones += 1
            usar("campo", "tipo_conciliacion", r["tipo_conciliacion"])
            continue
        reglas += 1
        be = r["bloque_E"]
        for c in ("idioma", "objeto_regulado", "unidad", "tipo_enunciado", "fuerza_normativa", "origen_evidencia",
                  "evidencia_afirmacion_fuente", "adopcion_canonica", "medio", "estado_evidencia", "dependencia"):
            if be[c] is not None:
                usar("campo", c, be[c])
        if be["estado_modelo_citado"]:
            usar("campo", "estado_modelo_citado", be["estado_modelo_citado"]["estado"])
            usar("faceta", "F29", be["estado_modelo_citado"]["modelo"])
        faceta("F30", r["bloque_D"]["F30"])
        faceta("F31", r["bloque_D"]["F31"])
        for t in r["bloque_D"]["terminos"]:
            usar("termino", "TRM", t)
        for a in r["bloque_D"]["ambito_funcional"]:
            usar("campo", "ambito_funcional", a)
        for ap in r["aplicaciones"]:
            usar("faceta", "P01", ap["ruta"]["flujo"])
            usar("faceta", "F02", ap["ruta"]["paso"])
            usar("campo", "uso_operativo", ap["uso_operativo"])
            usar("campo", "adopcion_canonica", ap["adopcion"])
            for d in ap["destinos"]:
                usar("destino", "contrato", d)
            if ap["condicion"]:
                cond(ap["condicion"])
            for f, v in ap["facetas"].items():
                faceta(f, v)

total = sum(usadas.values())
fuera = {k: n for k, n in usadas.items() if k not in origen}
ext = sum(n for k, n in usadas.items() if origen.get(k, "").startswith("extension_aprobada"))
ok = total - sum(fuera.values())
print(f"reglas {reglas} · conciliaciones {conciliaciones} · etiquetas usadas {total} (distintas {len(usadas)})")
print(f"coincidencia exacta con la taxonomía: {ok}/{total} = {100 * ok / max(total, 1):.2f}%"
      f" · de ellas con extensiones aprobadas 2026-10-23: {ext}")
for k, n in sorted(fuera.items(), key=lambda kv: -kv[1])[:50]:
    print("  NO COINCIDE:", k, n)
sin_uso = [k for k in origen if k[0] == "faceta" and k not in usadas]
print(f"cobertura inversa: valores de faceta usados {sum(1 for k in origen if k[0] == 'faceta' and k in usadas)}"
      f" · sin ninguna regla en este alcance {len(sin_uso)}")
if "--sin-uso" in sys.argv:
    for k in sin_uso:
        print("  sin reglas:", k[1], k[2])
sys.exit(0 if not fuera and total else 1)
