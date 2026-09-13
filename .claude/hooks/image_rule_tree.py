#!/usr/bin/env python3
"""Materializa el árbol de reglas de imagen en el orden que pidió Eric.

  imagen
    └ sin referencia / una referencia / ancla 2+ referencias
        └ con personas / sin personas
            con personas → una persona / grupo de personas
                → estilo de fotografía, iluminación, toma, tema,
                  complejidad de acción, y las demás categorías que
                  las reglas nombran (texto en imagen, modelo generador)
            sin personas → exterior, interior, animales, arquitectónica,
                  paisaje natural, producto/objeto, urbana
                → estilo de fotografía

No es una tabla de etiquetas: cada nodo lista las reglas que le pertenecen.

Colocación. Una regla pertenece a un nodo si, para cada dimensión del camino,
o no nombra ninguna rama de esa dimensión (entonces pertenece a todas) o nombra
precisamente ésa. Por eso las reglas que no nombran nada aparecen una sola vez
en la raíz, como lo que son: reglas de todas las ramas. Y por eso una regla que
nombra dos categorías aparece en las dos: no se le inventa una prioridad.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HOOKS = Path(__file__).resolve().parent
sys.path.insert(0, str(HOOKS))

RAMA_PERSONAS = ["style.photography", "lighting.setup", "composition.shot_size",
                 "task.theme", "motion.action_complexity", "text.mode", "generator.family"]
RAMA_SIN_PERSONAS = ["scene.category", "style.photography", "text.mode", "generator.family"]


def tags(fila: dict) -> dict[str, set[str]]:
    t: dict[str, set[str]] = {}
    for x in fila["tema"]:
        t.setdefault(x["dimension"], set()).add(x["valor"])
    return t


def compatible(t: dict[str, set[str]], camino: list[tuple[str, str]]) -> bool:
    """La regla cabe en el camino: en cada dimensión, o calla o dice ese valor."""
    return all(valor in t[dim] for dim, valor in camino if dim in t)


def especifica(t: dict[str, set[str]], dim: str, valor: str) -> bool:
    """La regla nombra esta rama — no la hereda por silencio."""
    return dim in t and valor in t[dim]


def etiqueta(tax: dict, dim: str, valor: str) -> str:
    for d in tax["dimensiones"]:
        if d["id"] == dim:
            for v in d["valores"]:
                if v["id"] == valor:
                    return v["etiqueta"]
    return valor


def valores(tax: dict, dim: str) -> list[str]:
    for d in tax["dimensiones"]:
        if d["id"] == dim:
            return [v["id"] for v in d["valores"]]
    return []


def linea(f: dict) -> str:
    return f"  - `{f['fuente']}` [{f['effect']}] — {f['texto'][:150]}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Árbol de reglas de imagen, con las reglas dentro")
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--taxonomy", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    filas = [json.loads(l) for l in Path(a.catalog).read_text(encoding="utf-8").splitlines() if l.strip()]
    tax = json.loads(Path(a.taxonomy).read_text(encoding="utf-8"))
    T = {f["rule_id"]: tags(f) for f in filas}
    byid = {f["rule_id"]: f for f in filas}
    colocadas: set[str] = set()
    L: list[str] = []

    L.append("# IMAGEN — todas las reglas, divididas rama por rama\n")
    L.append(f"**{len(filas)} reglas de imagen.** Las de video quedaron fuera por evaluación "
             "mecánica del `when` de cada regla con `media=image`.\n")

    raiz = [f for f in filas if not f["dimensiones"]]
    colocadas |= {f["rule_id"] for f in raiz}
    L.append(f"## TODAS LAS RAMAS — {len(raiz)} reglas\n")
    L.append("No nombran ninguna categoría: se aplican a cualquier imagen, con o sin referencia, "
             "con o sin personas. Se listan aquí una vez y **no se repiten abajo**; cada rama de "
             "abajo las lleva además de las suyas.\n")
    for f in sorted(raiz, key=lambda x: x["fuente"]):
        L.append(linea(f))
    L.append("")

    def hoja(titulo: str, camino: list[tuple[str, str]], dims: list[str], nivel: int) -> None:
        for dim in dims:
            for val in valores(tax, dim):
                sub = camino + [(dim, val)]
                rs = [byid[r] for r, t in T.items()
                      if especifica(t, dim, val) and compatible(t, sub)]
                cab = "#" * min(nivel, 6)
                if not rs:
                    L.append(f"{cab} {titulo} → {dim} = `{val}` ({etiqueta(tax, dim, val)}) — "
                             "**0 reglas · RAMA VACÍA**\n")
                    continue
                L.append(f"{cab} {titulo} → {dim} = `{val}` ({etiqueta(tax, dim, val)}) — "
                         f"{len(rs)} reglas\n")
                for f in sorted(rs, key=lambda x: x["fuente"]):
                    L.append(linea(f))
                    colocadas.add(f["rule_id"])
                L.append("")

    for ref in ["0", "1", "2+"]:
        cref = [("references.count", ref)]
        rs_ref = [byid[r] for r, t in T.items()
                  if especifica(t, "references.count", ref) and compatible(t, cref)]
        L.append(f"## {etiqueta(tax, 'references.count', ref).upper()} "
                 f"(`references.count = {ref}`) — {len(rs_ref)} reglas propias\n")
        for f in sorted(rs_ref, key=lambda x: x["fuente"]):
            L.append(linea(f))
            colocadas.add(f["rule_id"])
        L.append("")
        for hum, dims in (("true", RAMA_PERSONAS), ("false", RAMA_SIN_PERSONAS)):
            chum = cref + [("subject.human", hum)]
            rs_h = [byid[r] for r, t in T.items()
                    if especifica(t, "subject.human", hum) and compatible(t, chum)]
            L.append(f"### {etiqueta(tax, 'subject.human', hum).upper()} — {len(rs_h)} reglas propias\n")
            for f in sorted(rs_h, key=lambda x: x["fuente"]):
                L.append(linea(f))
                colocadas.add(f["rule_id"])
            L.append("")
            if hum == "true":
                for cnt in valores(tax, "subject.count_class"):
                    ccnt = chum + [("subject.count_class", cnt)]
                    rs_c = [byid[r] for r, t in T.items()
                            if especifica(t, "subject.count_class", cnt) and compatible(t, ccnt)]
                    L.append(f"#### {etiqueta(tax, 'subject.count_class', cnt).upper()} — "
                             f"{len(rs_c)} reglas propias\n")
                    for f in sorted(rs_c, key=lambda x: x["fuente"]):
                        L.append(linea(f))
                        colocadas.add(f["rule_id"])
                    L.append("")
                    hoja(f"{ref} · personas · {cnt}", ccnt, dims, 5)
            else:
                hoja(f"{ref} · sin personas", chum, dims, 4)

    faltan = [byid[r] for r in byid if r not in colocadas]
    L.append(f"## Reglas sin colocar — {len(faltan)}\n")
    L.append("Cero es la condición de que la división sea exhaustiva.\n" if not faltan
             else "Cada una es un hueco del árbol:\n")
    for f in sorted(faltan, key=lambda x: x["fuente"]):
        L.append(linea(f) + f"  ← nombra {f['dimensiones']}")

    Path(a.out).write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"ARBOL: {len(colocadas)}/{len(filas)} reglas colocadas; sin colocar {len(faltan)}")
    print(f"  raíz (todas las ramas) {len(raiz)}")
    print(f"  escrito {a.out}")
    return 0 if not faltan else 1


if __name__ == "__main__":
    raise SystemExit(main())
