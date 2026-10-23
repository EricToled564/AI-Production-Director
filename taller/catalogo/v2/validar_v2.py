"""validar_v2.py <lote.json> <salida.json>: estructura del registro §7.1, cobertura del lote y coincidencia
exacta de cada etiqueta con esquema_taxonomia.json (extraído de la taxonomía original + extensiones aprobadas).

Imprime OK solo si no hay ningún error. Uso desde la carpeta v2.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
E = json.loads((AQUI / "esquema_taxonomia.json").read_text())
FAC_APLIC = ["P01"] + [f"F{i:02d}" for i in range(1, 30)] + ["P04", "F32", "F33", "F34"]
VALORES = {f: {v["valor"] for v in d["valores"]} for f, d in E["facetas"].items()}
CAMPOS = {c: {v["valor"] for v in vals} for c, vals in E["campos"].items()}
TERMINOS = {t["id"] for t in E["terminos"]}
DESTINOS = set(E["destinos"])
PROHIBIDAS = re.compile(r"\b(no aplica|pendiente|propuesta|duda|desconocido|no determinado|en proceso|tbd|n/a)\b", re.I)


def validar(lote, salida):
    err = []
    ids_lote = [u["id"] for u in lote]
    vistos = []
    for r in salida:
        rid = r.get("id", "?")
        vistos += r.get("unidades", [])
        if rid not in r.get("unidades", []):
            err.append(f"{rid}: el id debe ser una de sus unidades")
        tipo = r.get("tipo_registro")
        if tipo == "conciliacion":
            if set(r) != {"id", "tipo_registro", "unidades", "tipo_conciliacion", "justificacion", "remite_a"}:
                err.append(f"{rid}: claves de conciliación {sorted(r)}")
                continue
            if r["tipo_conciliacion"] not in CAMPOS["tipo_conciliacion"]:
                err.append(f"{rid}: tipo_conciliacion no está en la taxonomía: {r['tipo_conciliacion']}")
            if len((r["justificacion"] or "").split()) < 3:
                err.append(f"{rid}: la conciliación exige justificación explícita")
            if r["tipo_conciliacion"] == "duplicado referenciado" and not r["remite_a"]:
                err.append(f"{rid}: un duplicado referenciado debe remitir a la regla")
            continue
        if tipo != "regla":
            err.append(f"{rid}: tipo_registro debe ser regla o conciliacion")
            continue
        if set(r) != {"id", "tipo_registro", "unidades", "contexto", "bloque_E", "bloque_D", "aplicaciones"}:
            err.append(f"{rid}: claves de regla {sorted(r)}")
            continue
        be = r["bloque_E"]
        claves_e = {"idioma", "objeto_regulado", "medio", "unidad", "tipo_enunciado", "fuerza_normativa",
                    "origen_evidencia", "evidencia_afirmacion_fuente", "adopcion_canonica", "estado_modelo_citado",
                    "estado_evidencia", "dependencia", "autoridad", "precedencia"}
        if set(be) != claves_e:
            err.append(f"{rid}: claves de bloque_E {sorted(set(be) ^ claves_e)}")
            continue
        for c in ("idioma", "objeto_regulado", "unidad", "tipo_enunciado", "fuerza_normativa", "origen_evidencia",
                  "evidencia_afirmacion_fuente", "adopcion_canonica"):
            if be[c] not in CAMPOS[c]:
                err.append(f"{rid}: bloque_E.{c} no está en la taxonomía: {be[c]!r}")
        if (be["objeto_regulado"] == "activo visual o sonoro") != (be["medio"] is not None):
            err.append(f"{rid}: medio va solo y siempre en la rama «activo visual o sonoro» (§1.3)")
        if be["medio"] is not None and be["medio"] not in CAMPOS["medio"]:
            err.append(f"{rid}: medio no está en la taxonomía: {be['medio']!r}")
        for c in ("estado_evidencia", "dependencia"):
            if be[c] is not None and be[c] not in CAMPOS[c]:
                err.append(f"{rid}: bloque_E.{c} no está en la taxonomía: {be[c]!r}")
        emc = be["estado_modelo_citado"]
        if emc is not None:
            if not isinstance(emc, dict) or set(emc) != {"estado", "modelo", "version", "fecha"}:
                err.append(f"{rid}: estado_modelo_citado = {{estado, modelo, version, fecha}} o null")
            elif emc["estado"] not in CAMPOS["estado_modelo_citado"] or emc["modelo"] not in VALORES["F29"]:
                err.append(f"{rid}: estado_modelo_citado con estado o modelo fuera de la taxonomía")
        bd = r["bloque_D"]
        if set(bd) != {"F30", "F31", "terminos", "ambito_funcional"}:
            err.append(f"{rid}: claves de bloque_D {sorted(bd)}")
            continue
        for f in ("F30", "F31"):
            faceta(err, rid, f, bd[f])
        if bd["F30"].get("estado") != "VALOR":
            err.append(f"{rid}: F30 es la materia de la regla: siempre VALOR")
        if bd["F31"].get("estado") != "VALOR" or len(bd["F31"].get("valores", [])) != 1:
            err.append(f"{rid}: F31 lleva exactamente un valor")
        for t in bd["terminos"]:
            if t not in TERMINOS:
                err.append(f"{rid}: término fuera del vocabulario operativo: {t}")
        if not bd["ambito_funcional"] or any(a not in CAMPOS["ambito_funcional"] for a in bd["ambito_funcional"]):
            err.append(f"{rid}: ambito_funcional vacío o fuera de la taxonomía: {bd['ambito_funcional']}")
        if not r["aplicaciones"]:
            err.append(f"{rid}: una regla tiene al menos una aplicación")
        for a in r["aplicaciones"]:
            aid = f"{rid}/{a.get('aplicacion_id')}"
            claves_a = {"aplicacion_id", "ruta", "uso_operativo", "destinos", "condicion", "adopcion", "facetas"}
            if set(a) != claves_a:
                err.append(f"{aid}: claves de aplicación {sorted(set(a) ^ claves_a)}")
                continue
            ruta = a["ruta"]
            if not isinstance(ruta, dict) or set(ruta) != {"flujo", "seccion", "paso", "condicion"}:
                err.append(f"{aid}: ruta = {{flujo, seccion, paso, condicion}} (§1.7)")
            else:
                if ruta["flujo"] not in VALORES["P01"]:
                    err.append(f"{aid}: ruta.flujo no está en P-01: {ruta['flujo']!r}")
                if ruta["paso"] not in VALORES["F02"]:
                    err.append(f"{aid}: ruta.paso no está en F02: {ruta['paso']!r}")
            if a["uso_operativo"] not in CAMPOS["uso_operativo"]:
                err.append(f"{aid}: uso_operativo no está en la taxonomía: {a['uso_operativo']!r}")
            if not a["destinos"] or any(d not in DESTINOS for d in a["destinos"]):
                err.append(f"{aid}: destinos vacíos o inexistentes en el contrato de templates: {a['destinos']}")
            if a["adopcion"] not in CAMPOS["adopcion_canonica"]:
                err.append(f"{aid}: adopcion no está en la taxonomía: {a['adopcion']!r}")
            if a["condicion"] is not None:
                condicion(err, aid, a["condicion"])
            fac = a["facetas"]
            if sorted(fac) != sorted(FAC_APLIC):
                err.append(f"{aid}: faltan o sobran facetas {sorted(set(FAC_APLIC) ^ set(fac))}")
                continue
            for f in FAC_APLIC:
                faceta(err, aid, f, fac[f])
        texto = json.dumps(r, ensure_ascii=False)
        for clave in ("estado", "valores", "valor", "uso_operativo", "adopcion"):
            for m in re.finditer(rf'"{clave}": (\[[^\]]*\]|"[^"]*")', texto):
                if PROHIBIDAS.search(m.group(1)):
                    err.append(f"{rid}: estado de diferimiento prohibido: {m.group(1)[:60]}")
    if sorted(vistos) != sorted(ids_lote):
        faltan = sorted(set(ids_lote) - set(vistos))
        sobran = sorted(set(vistos) - set(ids_lote))
        rep = sorted({i for i in vistos if vistos.count(i) > 1})
        err.append(f"cobertura: faltan {faltan[:10]} · sobran {sobran[:10]} · repetidas {rep[:10]}")
    return err


def faceta(err, donde, f, v):
    if not isinstance(v, dict) or set(v) != {"estado", "valores", "evidencia"}:
        err.append(f"{donde}: {f} = {{estado, valores, evidencia}}")
        return
    if v["estado"] not in CAMPOS["estado_faceta"]:
        err.append(f"{donde}: {f}.estado debe ser VALOR o UNIVERSAL: {v['estado']!r}")
    if v["estado"] == "VALOR":
        if not v["valores"]:
            err.append(f"{donde}: {f} VALOR sin valores")
        for x in v["valores"]:
            if x not in VALORES[f]:
                err.append(f"{donde}: {f} valor fuera de la taxonomía: {x!r}")
    elif v["valores"]:
        err.append(f"{donde}: {f} UNIVERSAL no lleva valores")
    if len((v["evidencia"] or "").split()) < 2:
        err.append(f"{donde}: {f} sin evidencia contextual (§1.12 punto 4 y 6)")


def condicion(err, donde, g):
    if not isinstance(g, dict) or set(g) != {"grupo", "miembros"} or g["grupo"] not in CAMPOS["grupo_condicion"] \
            or not g["miembros"]:
        err.append(f"{donde}: condición = {{grupo: TODAS|ALGUNA|NINGUNA, miembros: [...]}} (§7.2)")
        return
    for m in g["miembros"]:
        if isinstance(m, dict) and "grupo" in m:
            condicion(err, donde, m)
            continue
        if not isinstance(m, dict) or set(m) - {"campo", "operador", "valor", "unidad"} or \
                not {"campo", "operador", "valor"} <= set(m):
            err.append(f"{donde}: átomo = {{campo, operador, valor, unidad?}} (§7.2)")
            continue
        if m["operador"] not in CAMPOS["operador_atomo"]:
            err.append(f"{donde}: operador de átomo fuera de §7.2: {m['operador']!r}")
        if m["campo"] in VALORES and m["operador"] in ("=", "≠", "∈", "∉"):
            vals = m["valor"] if isinstance(m["valor"], list) else [m["valor"]]
            for x in vals:
                if x not in VALORES[m["campo"]]:
                    err.append(f"{donde}: valor de condición fuera de {m['campo']}: {x!r}")
        elif m["campo"] not in VALORES and m["campo"] not in DESTINOS and m["campo"] not in CAMPOS:
            err.append(f"{donde}: campo de condición desconocido (faceta o ruta del contrato): {m['campo']!r}")


if __name__ == "__main__":
    lote = json.loads(Path(sys.argv[1]).read_text())
    salida = json.loads(Path(sys.argv[2]).read_text())
    e = validar(lote, salida)
    print("OK" if not e else f"ERRORES ({len(e)}):\n" + "\n".join(e[:80]))
