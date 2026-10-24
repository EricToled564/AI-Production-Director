"""Registra en rag.sqlite una sección leída completa, solo si cada una de sus unidades está en el índice.

python3 -I registrar_lectura.py lineas <ruta> <desde> <hasta>     → cada línea no vacía del archivo en ese rango
python3 -I registrar_lectura.py terminos <desde> <hasta>          → términos TRM del esquema, por posición 1..1197
python3 -I registrar_lectura.py esquema facetas|campos|destinos|extensiones|citas  → la sección completa del esquema
python3 -I registrar_lectura.py --ver                             → secciones registradas

Una línea cuenta como indexada si su texto (sin marcas de tabla ni de lista) aparece dentro de algún fragmento de la
misma ruta. Si falta una sola, no se registra y sale con código 1.
"""
import datetime
import json
import sqlite3
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[3]
DB = AQUI / "rag.sqlite"


def limpio(s):
    s = unicodedata.normalize("NFC", s).strip()
    return s.lstrip("#").strip()


def main():
    c = sqlite3.connect(DB)
    c.execute("create table if not exists lecturas(id integer primary key, fecha text, ruta text, desde integer,"
              " hasta integer, unidades integer, indexadas integer)")
    if sys.argv[1] == "--ver":
        for r in c.execute("select fecha, ruta, desde, hasta, unidades, indexadas from lecturas order by id"):
            print(f"{r[0]}  {r[1]}  {r[2]}–{r[3]}  {r[5]}/{r[4]} unidades en el índice")
        return
    if sys.argv[1] == "terminos":
        ruta = "taller/catalogo/v2/esquema_taxonomia.json#terminos"
        desde, hasta = int(sys.argv[2]), int(sys.argv[3])
        ts = json.loads((RAIZ / "taller/catalogo/v2/esquema_taxonomia.json").read_text(encoding="utf-8"))["terminos"]
        unidades = [t["id"] for t in ts[desde - 1:hasta]]
        textos = [r[0] for r in c.execute("select texto from fragmentos where tipo='término TRM'")]
        faltan = [u for u in unidades if not any(x.startswith(u + " ") for x in textos)]
    elif sys.argv[1] == "esquema":
        sec = sys.argv[2]
        ruta = f"taller/catalogo/v2/esquema_taxonomia.json#{sec}"
        s = json.loads((RAIZ / "taller/catalogo/v2/esquema_taxonomia.json").read_text(encoding="utf-8"))
        tipo, unidades = {
            "facetas": ("valor de faceta", [f"{f} {d['nombre']} = {v['valor']} · " for f, d in s["facetas"].items()
                                            for v in d["valores"]]),
            "campos": ("valor de campo", [f"campo {c} = {v['valor']} · " for c, vs in s["campos"].items() for v in vs]),
            "destinos": ("destino", [d if isinstance(d, str) else json.dumps(d, ensure_ascii=False) for d in s["destinos"]]),
            "extensiones": ("extensión", [f"extensión aprobada 2026-10-23 · "
                                          + (f"faceta {e['faceta']}" if "faceta" in e else f"campo {e['campo']}")
                                          + f" = {e['valor']}" for e in s["extensiones"]]),
            "citas": ("cita de lista", [f"cita de la lista del campo {c} · línea de la taxonomía {x['linea']} · {x['texto']}"
                                        for c, x in s["citas_de_listas"].items()]),
        }[sec]
        desde, hasta = 1, len(unidades)
        textos = [r[0] for r in c.execute("select texto from fragmentos where tipo=?", (tipo,))]
        faltan = [u for u in unidades if not any(x.startswith(u) for x in textos)]
    else:
        ruta, desde, hasta = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
        lineas = (RAIZ / ruta).read_text(encoding="utf-8").splitlines()[desde - 1:hasta]
        textos = [limpio(r[0]) for r in c.execute("select texto from fragmentos where ruta=?", (ruta,))]
        blob = "\n".join(textos)
        unidades = [limpio(l) for l in lineas if l.strip() and not l.strip().startswith(("|---", "|-"))]
        faltan = [u for u in unidades if u and u not in blob]
    if faltan:
        print(f"NO REGISTRADA: {len(faltan)} de {len(unidades)} unidades no están en el índice, p. ej.:")
        for f in faltan[:5]:
            print("   ", f[:120])
        sys.exit(1)
    c.execute("insert into lecturas(fecha,ruta,desde,hasta,unidades,indexadas) values(?,?,?,?,?,?)",
              (datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), ruta, desde, hasta,
               len(unidades), len(unidades)))
    c.commit()
    print(f"registrada: {ruta} {desde}–{hasta} · {len(unidades)}/{len(unidades)} unidades en el índice")


if __name__ == "__main__":
    main()
