#!/usr/bin/env python3
"""Verifica cada cita de sintaxis_fuente.json: archivo existe y texto (espacios colapsados)
es substring de linea_ini..linea_fin (1-based) unidas y colapsadas."""
import json, os, re, sys

J = sys.argv[1] if len(sys.argv) > 1 else "/home/user/AI-Production-Director/apd/data/sintaxis_fuente.json"
data = json.load(open(J, encoding="utf-8"))
import pathlib as _p, sys as _s
_s.path.insert(0, str(_p.Path(__file__).resolve().parents[1]))
from apd import fuentes as _F
PKG = str(_F.extraer_paquete() / "skills")
REPO = str(_F.REPO)


def resolve(a):
    return os.path.join(PKG, a[len("skills/"):]) if a.startswith("skills/") else os.path.join(REPO, a)


def col(s):
    return re.sub(r"\s+", " ", s).strip()


cache = {}
ok, bad = 0, []


def walk(o, path):
    global ok
    if isinstance(o, dict):
        if "archivo" in o and "texto" in o:
            f = resolve(o["archivo"])
            if not os.path.isfile(f):
                bad.append((path, "no existe", o)); return
            if f not in cache:
                cache[f] = open(f, encoding="utf-8").read().split("\n")
            lines = cache[f]
            a, b = o["linea_ini"], o["linea_fin"]
            if not (1 <= a <= b <= len(lines)):
                bad.append((path, "rango inválido", o)); return
            hay = col(" ".join(lines[a - 1:b]))
            if col(o["texto"]) in hay and col(o["texto"]):
                ok += 1
            else:
                bad.append((path, "texto no encontrado", o))
            return
        for k, v in o.items():
            walk(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f"{path}[{i}]")


walk(data, "$")
print(f"verificadas={ok} fallidas={len(bad)}")
for p, why, o in bad:
    print(f"FAIL {why}: {p} -> {o['archivo']}:{o['linea_ini']}-{o['linea_fin']} :: {o['texto']!r}")
sys.exit(1 if bad else 0)
