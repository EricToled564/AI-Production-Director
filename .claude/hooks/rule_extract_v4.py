#!/usr/bin/env python3
"""Extrae las reglas de creación de imagen del paquete v3.4.0 como UNIDADES COMPLETAS.

Fuente única: .claude/rules/v4/source (copiada del zip que entregó Eric, con sus
hashes en SOURCE_SHA256.txt). El ruleset 3.5.0 no se usa.

Por qué existe. El compilador anterior partía por líneas y producía "reglas" como
`Document:` o `- Labels: "[Revenue Growth]"`, dejando fuera el bloque de código que
llevaba la instrucción real. Una unidad aquí es un enunciado con TODO lo que le
pertenece pegado:

  - la línea de entrada más su bloque ``` de código;
  - la línea de entrada terminada en ':' más su lista o su tabla completa;
  - una tabla con su encabezado y todas sus filas;
  - una cita en bloque con todas sus líneas.

Nada se trunca y nada se descarta: los créditos, los encabezados de lista y la
prosa descriptiva también salen como unidades, para que la clasificación pueda
decir "no es regla" con el texto delante en vez de que desaparezcan en silencio.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

LISTA = re.compile(r"^\s{0,3}([-*+]|\d{1,2}[.)])\s")
TABLA = re.compile(r"^\s*\|")
CITA = re.compile(r"^\s*>")
FENCE = re.compile(r"^\s*(```|~~~)")
HEAD = re.compile(r"^(#{1,6})\s+(.*)$")


def unidades(lineas: list[str]) -> list[dict]:
    """Recorre el archivo y agrupa cada enunciado con su carga."""
    out: list[dict] = []
    pila: list[str] = []
    i, n = 0, len(lineas)
    if lineas[:1] == ["---"]:  # front matter YAML
        j = 1
        while j < n and lineas[j].strip() != "---":
            j += 1
        out.append({"linea": 1, "fin": j + 1, "seccion": [], "tipo": "front_matter",
                    "texto": "\n".join(lineas[:j + 1])})
        i = j + 1
    while i < n:
        ln = lineas[i]
        if not ln.strip():
            i += 1
            continue
        m = HEAD.match(ln)
        if m:
            nivel = len(m.group(1))
            pila = pila[: nivel - 1] + [m.group(2).strip()]
            i += 1
            continue
        ini = i
        if FENCE.match(ln):  # bloque de código sin entrada previa
            cierre = FENCE.match(ln).group(1)
            j = i + 1
            while j < n and not lineas[j].strip().startswith(cierre):
                j += 1
            i = min(j + 1, n)
            out.append({"linea": ini + 1, "fin": i, "seccion": list(pila), "tipo": "codigo",
                        "texto": "\n".join(lineas[ini:i])})
            continue
        if TABLA.match(ln):
            j = i
            while j < n and TABLA.match(lineas[j]):
                j += 1
            i = j
            out.append({"linea": ini + 1, "fin": i, "seccion": list(pila), "tipo": "tabla",
                        "texto": "\n".join(lineas[ini:i])})
            continue
        if CITA.match(ln):
            j = i
            while j < n and (CITA.match(lineas[j]) or (lineas[j].strip() and not HEAD.match(lineas[j]))):
                j += 1
            i = j
            out.append({"linea": ini + 1, "fin": i, "seccion": list(pila), "tipo": "cita",
                        "texto": "\n".join(lineas[ini:i])})
            continue
        if LISTA.match(ln):
            j = i
            while j < n and (LISTA.match(lineas[j]) or lineas[j].startswith(("  ", "\t"))
                             or (not lineas[j].strip() and j + 1 < n and LISTA.match(lineas[j + 1]))):
                if FENCE.match(lineas[j]):
                    cierre = FENCE.match(lineas[j]).group(1)
                    j += 1
                    while j < n and not lineas[j].strip().startswith(cierre):
                        j += 1
                j += 1
            i = j
            out.append({"linea": ini + 1, "fin": i, "seccion": list(pila), "tipo": "lista",
                        "texto": "\n".join(lineas[ini:i]).rstrip()})
            continue
        # párrafo: hasta línea en blanco; si le sigue código/lista/tabla/cita, se pega
        j = i
        while j < n and lineas[j].strip() and not HEAD.match(lineas[j]) \
                and not LISTA.match(lineas[j]) and not TABLA.match(lineas[j]) and not FENCE.match(lineas[j]):
            j += 1
        fin = j
        k = j
        while k < n and not lineas[k].strip():
            k += 1
        if k < n and (FENCE.match(lineas[k]) or LISTA.match(lineas[k]) or TABLA.match(lineas[k]) or CITA.match(lineas[k])):
            if FENCE.match(lineas[k]):
                cierre = FENCE.match(lineas[k]).group(1)
                z = k + 1
                while z < n and not lineas[z].strip().startswith(cierre):
                    z += 1
                fin = min(z + 1, n)
            else:
                z = k
                while z < n and lineas[z].strip() and not HEAD.match(lineas[z]):
                    if FENCE.match(lineas[z]):
                        cierre = FENCE.match(lineas[z]).group(1)
                        z += 1
                        while z < n and not lineas[z].strip().startswith(cierre):
                            z += 1
                    z += 1
                fin = z
        i = max(fin, j)
        out.append({"linea": ini + 1, "fin": fin, "seccion": list(pila), "tipo": "parrafo",
                    "texto": "\n".join(lineas[ini:fin]).rstrip()})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Extraer unidades de regla del paquete")
    ap.add_argument("--source", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    raiz = Path(a.source)
    filas: list[dict] = []
    for p in sorted(raiz.rglob("*")):
        if not p.is_file():
            continue
        rel = str(p.relative_to(raiz))
        if p.suffix == ".json":
            data = json.loads(p.read_text(encoding="utf-8"))
            items = data if isinstance(data, list) else data.get("learnings") or data.get("rules") or [data]
            for k, it in enumerate(items, 1):
                txt = json.dumps(it, ensure_ascii=False, indent=1)
                filas.append({"fuente": rel, "linea": k, "fin": k, "seccion": ["learned"],
                              "tipo": "json", "texto": txt})
            continue
        if p.suffix != ".md":
            continue
        for u in unidades(p.read_text(encoding="utf-8").splitlines()):
            u["fuente"] = rel
            filas.append(u)
    for f in filas:
        f["id"] = hashlib.sha1(f"{f['fuente']}|{f['linea']}|{f['texto']}".encode()).hexdigest()[:12]
        f["palabras"] = len(f["texto"].split())
    Path(a.out).write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")
    print(f"UNIDADES: {len(filas)}")
    import collections
    for k, v in collections.Counter(f["tipo"] for f in filas).most_common():
        print(f"  {k:14} {v}")
    print(f"  palabras totales {sum(f['palabras'] for f in filas):,}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
