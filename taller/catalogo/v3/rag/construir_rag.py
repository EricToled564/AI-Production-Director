"""Índice de consulta de las clasificaciones maestras (taxonomías, decisiones, piloto aprobado y textos fuente).

python3 -I construir_rag.py        → escribe rag.sqlite junto a este archivo

Cada fragmento guarda: fuente, ruta exacta y línea, tipo de fragmento, estado de autoridad de la fuente y texto
literal. La búsqueda es BM25 (SQLite FTS5) sobre texto sin tildes; no hay vectores: no se necesita descargar modelos
y el resultado es determinista. Nada se reescribe: el texto de cada fragmento es copia literal de su fuente.
"""
import importlib.util
import json
import sqlite3
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[3]
V2 = RAIZ / "taller/catalogo/v2"
V3F = RAIZ / "taller/catalogo/v3/fuentes"

# Estado de autoridad de cada fuente, con su motivo verificable.
ESTADO = {
    "taxonomia-1019-extracto": ("VIGENTE (extracto)", "PILOTO_V5_INSTRUCCIONES_20261019 §3: entrada autorizada; solo 4 tramos literales"),
    "taxonomia-1019-esquema": ("VIGENTE (extraído)", "esquema_taxonomia.json, construido de la taxonomía 00688 con número de línea"),
    "decisiones-eric-1023": ("VIGENTE", "DECISIONES_ERIC_20261023.md; manda sobre las anteriores en lo que trata"),
    "decisiones-1011": ("VIGENTE", "registro de decisiones del usuario DEC-000001..027 y decisión 16:56:54"),
    "decisiones-repo-0925": ("VIGENTE", ".claude/rules/DECISIONES.md"),
    "templates-1019": ("VIGENTE (contrato documental)", "TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md"),
    "guia-v2": ("VIGENTE (instrucción operativa)", "GUIA_CLASIFICACION.md de v2"),
    "piloto-gpt-image": ("APROBADO POR ERIC (piloto)", "clasificacion.py; consultas U1, C1, C2, C3 resueltas por Eric"),
    "taxonomia-0928": ("VERSIÓN ANTERIOR", "aprobada 2026-09-28; la entrada autorizada del piloto es la del 2026-10-19"),
    "arbol-0913": ("HISTÓRICO, NO USAR COMO RESPUESTA", "clasificación por léxico; contradice taxonomía §1.6 y §1.12.4 y DEC-000023"),
    "universales-candidatas": ("CANDIDATO NO ACEPTADO", "universal_rules.json status IMPLEMENTATION_CANDIDATE_NOT_USER_ACCEPTED"),
    "texto-fuente": ("TEXTO ORIGINAL", "unidad de la base de 13,005 textos (universo de la decisión 1); sin clasificación"),
    "documento-fuente": ("DOCUMENTO ORIGINAL COMPLETO", "copia literal con hash en fuentes/documentos/PROCEDENCIA.md"),
}


def documentos():
    """Cada línea no vacía de los documentos fuente copiados, con su encabezado vigente."""
    out = []
    base = V3F / "documentos"
    for p in sorted(base.rglob("*.md")):
        if p.name == "PROCEDENCIA.md":
            continue
        rel = str(p.relative_to(RAIZ))
        enc = ""
        for n, l in enumerate(lineas(p), 1):
            if l.strip().startswith("#"):
                enc = l.strip().lstrip("#").strip()
            if l.strip():
                out.append(("documento-fuente", rel, n, enc, "línea de documento", l.strip()))
    return out


def lineas(p):
    return p.read_text(encoding="utf-8").splitlines()


def parrafos(ruta, rel, fuente, tipo="párrafo"):
    """Un fragmento por bloque de líneas no vacías; las filas de tabla y los ítems de lista van uno por uno."""
    out, buf, ini = [], [], None
    enc = ""
    for n, l in enumerate(lineas(ruta), 1):
        s = l.strip()
        if s.startswith("#"):
            if buf:
                out.append((fuente, rel, ini, enc, tipo, "\n".join(buf)))
                buf = []
            enc = s.lstrip("#").strip()
            out.append((fuente, rel, n, enc, "encabezado", s))
            continue
        if not s or s.startswith("|---") or s.startswith("|-"):
            if buf:
                out.append((fuente, rel, ini, enc, tipo, "\n".join(buf)))
                buf = []
            continue
        if s.startswith("|") or s.startswith("- ") or s[:3].rstrip(".").isdigit():
            if buf:
                out.append((fuente, rel, ini, enc, tipo, "\n".join(buf)))
                buf = []
            out.append((fuente, rel, n, enc, "fila o ítem", s))
            continue
        if not buf:
            ini = n
        buf.append(s)
    if buf:
        out.append((fuente, rel, ini, enc, tipo, "\n".join(buf)))
    return out


def esquema():
    rel = "taller/catalogo/v2/esquema_taxonomia.json"
    s = json.loads((RAIZ / rel).read_text(encoding="utf-8"))
    out = []
    for f, d in s["facetas"].items():
        for v in d["valores"]:
            ln = v.get("linea")
            out.append(("taxonomia-1019-esquema", rel, ln, f"{f} {d['nombre']}", "valor de faceta",
                        f"{f} {d['nombre']} = {v['valor']} · origen {v['origen']}"
                        + (f" · {v['id']}" if v.get("id") else "") + (f" · {v['definicion']}" if v.get("definicion") else "")
                        + (f" · línea de la taxonomía {ln}" if ln else "")))
    for c, vals in s["campos"].items():
        for v in vals:
            out.append(("taxonomia-1019-esquema", rel, v.get("linea"), f"campo {c}", "valor de campo",
                        f"campo {c} = {v['valor']} · origen {v['origen']}" + (f" · {v['id']}" if v.get("id") else "")
                        + (f" · {v['definicion']}" if v.get("definicion") else "")
                        + (f" · línea de la taxonomía {v['linea']}" if v.get("linea") else "")))
    for t in s["terminos"]:
        out.append(("taxonomia-1019-esquema", rel, t.get("linea"), f"término {t['faceta']} {t.get('materia', '')}".strip(),
                    "término TRM", f"{t['id']} «{t['termino']}» · faceta {t['faceta']}"
                    + (f" · materia {t['materia']}" if t.get("materia") else "") + f" · {t['definicion']}"))
    for d in s["destinos"]:
        txt = d if isinstance(d, str) else json.dumps(d, ensure_ascii=False)
        out.append(("taxonomia-1019-esquema", rel, None, "destinos del contrato de templates", "destino", txt))
    for e in s["extensiones"]:
        dim = f"faceta {e['faceta']}" if "faceta" in e else f"campo {e['campo']}"
        out.append(("taxonomia-1019-esquema", rel, None, "extensiones aprobadas 2026-10-23", "extensión",
                    f"extensión aprobada 2026-10-23 · {dim} = {e['valor']}"))
    for c, x in s["citas_de_listas"].items():
        out.append(("taxonomia-1019-esquema", rel, x["linea"], f"cita de lista {c}", "cita de lista",
                    f"cita de la lista del campo {c} · línea de la taxonomía {x['linea']} · {x['texto']}"))
    return out


def arbol():
    out = []
    rel = "taller/catalogo/v3/fuentes/arbol-0913_image-taxonomy.v1.json"
    d = json.loads((RAIZ / rel).read_text(encoding="utf-8"))
    for k in ("construida_por", "regla_de_oro", "nota_lexico"):
        out.append(("arbol-0913", rel, None, "árbol imagen v1", "principio", f"{k}: {d[k]}"))
    for x in d["dimensiones"]:
        padre = f"{x['padre']['dimension']}={x['padre']['valor']}" if x["padre"] else "raíz"
        for v in x["valores"]:
            out.append(("arbol-0913", rel, None, f"nivel {x['nivel']} {x['id']}", "rama",
                        f"nivel {x['nivel']} · {x['id']} (cuelga de {padre}) · {x['pregunta']} · rama {v['id']} = "
                        f"{v['etiqueta']} · léxico: {', '.join(v.get('lexico', []))}"))
    out += parrafos(V3F / "arbol-0913_CATALOGO-IMAGEN.md", "taller/catalogo/v3/fuentes/arbol-0913_CATALOGO-IMAGEN.md", "arbol-0913")
    out += parrafos(V3F / "arbol-0913_ARBOL-IMAGEN.md", "taller/catalogo/v3/fuentes/arbol-0913_ARBOL-IMAGEN.md", "arbol-0913",
                    "regla en rama")
    return out


def piloto():
    rel = "taller/catalogo/v2/piloto_gpt-image/clasificacion.py"
    spec = importlib.util.spec_from_file_location("piloto", RAIZ / rel)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    cat = {x["id"]: x for x in json.loads((RAIZ / "taller/catalogo/catalogo_imagen_gpt2.json").read_text(encoding="utf-8"))}
    out = []
    for a in m.APLICACIONES:
        u = cat[a["id"]]
        # F29 (modelo) va aparte de r en el piloto; sin él una aplicación de gpt-image-1-mini parece de GPT Image 2
        cond = (f"F29 {', '.join(a['f29'])} · " + (f"además {json.dumps(a['r'], ensure_ascii=False)}" if a["r"]
                                                    else "sin otra restricción de faceta"))
        pasos = "todos los pasos de prompt" if a["f02"] == m.PASOS_PROMPT else ", ".join(a["f02"])
        out.append(("piloto-gpt-image", f"{u['archivo']}", int(u["linea"]), u["encabezado"], "aplicación aprobada",
                    f"{a['id']} · tipo {a.get('t61')} / {', '.join(a.get('t112', []))} · fuerza {', '.join(a['fuerza'])} · "
                    f"uso {a['uso']} · ámbito {', '.join(a['ambito'])} · objeto {a['objeto']} · F30 "
                    f"{', '.join(a.get('f30', []))} · F31 {a['f31']} · condición {cond} · pasos {pasos} · acción "
                    f"{', '.join(a['accion'])} · destino "
                    f"{', '.join(a['destino'])} · valor: {a['valor']} · fundamento: {a['fund']} · TEXTO: {u['texto']}"))
    for i, (tipo, just) in m.CONCILIACIONES.items():
        u = cat[i]
        out.append(("piloto-gpt-image", u["archivo"], int(u["linea"]), u["encabezado"], "conciliación aprobada",
                    f"{i} · {tipo} · {just} · TEXTO: {u['texto']}"))
    return out


def universales():
    rel = "taller/recursos/universal_rules.json"
    d = json.loads((RAIZ / rel).read_text(encoding="utf-8"))
    return [("universales-candidatas", rel, None, r["rule_id"], "regla universal candidata",
             f"{r['rule_id']} · fuentes {', '.join(r.get('source_ids', []))} · {r.get('intent', '')} · falla si: "
             f"{r.get('failure_criteria', '')}") for r in d["rules"]]


def textos():
    cat = json.loads((RAIZ / "taller/catalogo/catalogo_imagen_gpt2.json").read_text(encoding="utf-8"))
    return [("texto-fuente", x["archivo"], int(x["linea"]), x["encabezado"], "texto original", f"{x['id']} · {x['texto']}")
            for x in cat]


def main():
    frag = []
    frag += parrafos(V2 / "taxonomia_extracto.md", "taller/catalogo/v2/taxonomia_extracto.md", "taxonomia-1019-extracto")
    frag += esquema()
    frag += parrafos(V2 / "decisiones/DECISIONES_ERIC_20261023.md", "taller/catalogo/v2/decisiones/DECISIONES_ERIC_20261023.md",
                     "decisiones-eric-1023")
    for f in ("01021_DECISIONES_APLICADAS_20261011_224300.md", "01022_DELTA_DECISIONES_CONSOLIDADO_20261011_224300.md",
              "01062_registro_decisiones_DOC01.md"):
        frag += parrafos(V2 / "decisiones" / f, f"taller/catalogo/v2/decisiones/{f}", "decisiones-1011")
    frag += parrafos(RAIZ / ".claude/rules/DECISIONES.md", ".claude/rules/DECISIONES.md", "decisiones-repo-0925")
    frag += parrafos(V2 / "decisiones/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md",
                     "taller/catalogo/v2/decisiones/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md", "templates-1019")
    frag += parrafos(V2 / "GUIA_CLASIFICACION.md", "taller/catalogo/v2/GUIA_CLASIFICACION.md", "guia-v2")
    frag += piloto()
    frag += parrafos(V3F / "taxonomia-0928_TAXONOMIA.md", "taller/catalogo/v3/fuentes/taxonomia-0928_TAXONOMIA.md", "taxonomia-0928")
    frag += arbol()
    frag += universales()
    frag += textos()
    frag += documentos()

    db = AQUI / "rag.sqlite"
    previas = []  # el registro de lecturas no se pierde al reconstruir el índice
    if db.exists():
        v = sqlite3.connect(db)
        if v.execute("select 1 from sqlite_master where name='lecturas'").fetchone():
            previas = v.execute("select fecha, ruta, desde, hasta, unidades, indexadas from lecturas order by id").fetchall()
        v.close()
    db.unlink(missing_ok=True)
    c = sqlite3.connect(db)
    c.execute("create table lecturas(id integer primary key, fecha text, ruta text, desde integer,"
              " hasta integer, unidades integer, indexadas integer)")
    c.executemany("insert into lecturas(fecha,ruta,desde,hasta,unidades,indexadas) values(?,?,?,?,?,?)", previas)
    c.execute("create table fragmentos(id integer primary key, fuente text, ruta text, linea integer, encabezado text,"
              " tipo text, estado text, motivo_estado text, texto text)")
    c.execute("create virtual table fts using fts5(texto, encabezado, content='fragmentos', content_rowid='id',"
              " tokenize='unicode61 remove_diacritics 2')")
    for f in frag:
        est, mot = ESTADO[f[0]]
        cur = c.execute("insert into fragmentos(fuente,ruta,linea,encabezado,tipo,estado,motivo_estado,texto)"
                        " values(?,?,?,?,?,?,?,?)", (f[0], f[1], f[2], f[3], f[4], est, mot, f[5]))
        c.execute("insert into fts(rowid,texto,encabezado) values(?,?,?)", (cur.lastrowid, f[5], f[3] or ""))
    c.commit()
    for (fuente, n) in c.execute("select fuente, count(*) from fragmentos group by fuente order by 2 desc"):
        print(f"{fuente:26} {n}")
    print("total", c.execute("select count(*) from fragmentos").fetchone()[0])


if __name__ == "__main__":
    main()
