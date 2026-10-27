"""Control de 05_lectura_universo.md: cada texto del universo y cada texto de la adenda que entra tiene exactamente un
veredicto. Sale con código 1 si falta alguno o alguno tiene dos.

python3 -I taller/catalogo/v3/revision/verificar_lectura.py
"""
import collections
import json
import re
import sys
from pathlib import Path

V3 = Path(__file__).resolve().parent.parent
U = [json.loads(l)["id"] for l in open(V3 / "universo/universo_prueba_textos.jsonl", encoding="utf-8")]
A = [d["id"] for d in map(json.loads, open(V3 / "universo/adenda/adenda_universo.jsonl", encoding="utf-8"))
     if d["veredicto"] == "entra"]
cov = collections.Counter()
for line in (V3 / "revision/05_lectura_universo.md").read_text(encoding="utf-8").split("\n"):
    if not line.startswith("| ") or line.startswith("| Ids"):
        continue
    cell = line.split("|")[1]
    for a, b in re.findall(r"(\d{6})–(\d{6})", cell):
        for n in range(int(a), int(b) + 1):
            cov["INV-%06d" % n] += 1
    for a in re.findall(r"\b(\d{6})\b", re.sub(r"\d{6}–\d{6}", "", cell)):
        cov["INV-" + a] += 1
    for a, b in re.findall(r"ADD-(\d{4})–ADD-(\d{4})", cell):
        for n in range(int(a), int(b) + 1):
            cov["ADD-%04d" % n] += 1
    for a in re.findall(r"ADD-(\d{4})", re.sub(r"ADD-\d{4}–ADD-\d{4}", "", cell)):
        cov["ADD-" + a] += 1
falta = [x for x in U + A if cov[x] == 0]
doble = [x for x in U + A if cov[x] > 1]
print(f"textos {len(U) + len(A)} · sin veredicto {len(falta)} · con dos o más {len(doble)}")
sys.exit(1 if falta or doble else 0)
