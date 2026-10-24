"""Cruce de las dos pasadas independientes y control de la traza final.

python3 cruzar.py cruce         → escribe desacuerdos.json (texto × caso donde las pasadas difieren) y resumen
python3 cruzar.py consolidar    → aplica adjudicacion.json sobre el acuerdo y escribe seleccion.json
python3 cruzar.py traza         → comprueba que cada (texto, caso) seleccionado tiene destino en traza_<caso>.json
                                  y que ningún destino cita un texto no seleccionado; exit 1 si falla

Acuerdo: si ambas pasadas dicen lo mismo para un texto y caso, ese es el veredicto. Si difieren (tipo distinto o
aplica en una y fuera en la otra), el par va a desacuerdos.json y lo resuelve la adjudicación leyendo la fuente.
"""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CASOS = ["B1", "B2", "B3", "B4", "B5"]


# Lotes revisados en una sola pasada (los revisores del lote 07 se detuvieron por presupuesto a pedido de Eric):
# la pasada 2 toma el veredicto de la pasada 1, sin desacuerdos posibles, y el resumen los cuenta aparte.
PASADA_UNICA = {"lote_07"}


def cargar(pasada):
    out = {}
    for lote in sorted((AQUI / "lotes").glob("lote_*.json")):
        f = AQUI / "veredictos" / pasada / lote.name
        if not f.exists() and lote.stem in PASADA_UNICA:
            f = AQUI / "veredictos" / "pasada_1" / lote.name
        if not f.exists():
            continue
        for r in json.loads(f.read_text(encoding="utf-8")):
            out[r["id"]] = r
    return out


def estado(r, c):
    if r["tipo"] != "normativo":
        return "sin contenido"
    return "aplica" if c in r.get("aplica", []) else "fuera"


def efecto(r, c):
    return (r.get("efecto_por_caso") or {}).get(c) or r.get("efecto", "")


def cruce():
    univ = json.loads((AQUI / "universo.json").read_text(encoding="utf-8"))
    p1, p2 = cargar("pasada_1"), cargar("pasada_2")
    faltan = [u["id"] for u in univ if u["id"] not in p1 or u["id"] not in p2]
    if faltan:
        sys.exit(f"faltan veredictos para {len(faltan)} textos, p. ej. {faltan[:5]}")
    desac, acuerdo = [], {}
    for u in univ:
        a, b = p1[u["id"]], p2[u["id"]]
        for c in CASOS:
            ea, eb = estado(a, c), estado(b, c)
            if ea == eb:
                acuerdo[(u["id"], c)] = ea
            else:
                desac.append({"id": u["id"], "caso": c, "archivo": u["archivo"], "linea": u["linea"],
                              "encabezado": u["encabezado"], "texto": u["texto"],
                              "pasada_1": {"estado": ea, "efecto": efecto(a, c), "motivo": (a.get("fuera") or {}).get(c, a.get("motivo", ""))},
                              "pasada_2": {"estado": eb, "efecto": efecto(b, c), "motivo": (b.get("fuera") or {}).get(c, b.get("motivo", ""))}})
    (AQUI / "desacuerdos.json").write_text(json.dumps(desac, ensure_ascii=False, indent=1), encoding="utf-8")
    pares = len(univ) * len(CASOS)
    print(f"textos {len(univ)} · pares texto×caso {pares} · acuerdo {len(acuerdo)} ({100 * len(acuerdo) / pares:.1f} %)"
          f" · desacuerdos {len(desac)}")
    unica = sum(len(json.loads((AQUI / "lotes" / f"{l}.json").read_text(encoding="utf-8"))) for l in PASADA_UNICA)
    print(f"  de ellos en pasada única (sin segunda revisión): {unica} textos ({', '.join(sorted(PASADA_UNICA))})")
    for c in CASOS:
        n = sum(1 for (i, cc), e in acuerdo.items() if cc == c and e == "aplica")
        d = sum(1 for x in desac if x["caso"] == c)
        print(f"  {c}: aplica por acuerdo {n} · en desacuerdo {d}")


def consolidar():
    univ = json.loads((AQUI / "universo.json").read_text(encoding="utf-8"))
    p1, p2 = cargar("pasada_1"), cargar("pasada_2")
    desac = json.loads((AQUI / "desacuerdos.json").read_text(encoding="utf-8"))
    adj = {(x["id"], x["caso"]): x for x in json.loads((AQUI / "adjudicacion.json").read_text(encoding="utf-8"))}
    pend = [(x["id"], x["caso"]) for x in desac if (x["id"], x["caso"]) not in adj]
    if pend:
        sys.exit(f"{len(pend)} desacuerdos sin adjudicar, p. ej. {pend[:5]}")
    sel = {c: [] for c in CASOS}
    texto = {u["id"]: u for u in univ}
    for u in univ:
        for c in CASOS:
            k = (u["id"], c)
            if k in adj:
                if adj[k]["estado"] != "aplica":
                    continue
                ef = adj[k]["efecto"]
            elif estado(p1[u["id"]], c) == "aplica":
                e1, e2 = efecto(p1[u["id"]], c), efecto(p2[u["id"]], c)
                ef = e1 if e1 == e2 else e1 + " ‖ " + e2
            else:
                continue
            sel[c].append({"id": u["id"], "archivo": u["archivo"], "linea": u["linea"], "texto": texto[u["id"]]["texto"],
                           "efecto": ef})
    (AQUI / "seleccion.json").write_text(json.dumps(sel, ensure_ascii=False, indent=1), encoding="utf-8")
    for c in CASOS:
        print(f"{c}: {len(sel[c])} textos aplican")


def traza():
    sel = json.loads((AQUI / "seleccion.json").read_text(encoding="utf-8"))
    total = 0
    for c in CASOS:
        t = json.loads((AQUI / f"traza_{c}.json").read_text(encoding="utf-8"))
        mapeados = {}
        for destino, ids in t["destinos"].items():
            for i in ids:
                mapeados.setdefault(i, []).append(destino)
        esperados = {x["id"] for x in sel[c]}
        sin = sorted(esperados - set(mapeados))
        sobran = sorted(set(mapeados) - esperados)
        print(f"{c}: seleccionados {len(esperados)} · con destino {len(esperados & set(mapeados))} · "
              f"sin destino {len(sin)} · citados sin selección {len(sobran)}")
        for i in sin[:10]:
            print("    sin destino:", i)
        for i in sobran[:10]:
            print("    no seleccionado:", i)
        total += len(sin) + len(sobran)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    {"cruce": cruce, "consolidar": consolidar, "traza": traza}[sys.argv[1]]()
