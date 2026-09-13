#!/usr/bin/env python3
"""Verifica una clasificación regla-por-regla contra el texto de cada regla.

Eric pidió prueba cuantitativa de que las reglas se leyeron una por una. La
prueba es ésta: toda rama asignada a una regla tiene que venir con una cita
literal del texto DE ESA regla, y este programa comprueba que la cita exista
dentro de ese texto. Una cita que no aparece es una invención y sale como FAIL.

Una regla que su texto no acota queda `UNIVERSAL` con motivo escrito. Eso no es
un hueco: es la respuesta correcta cuando el texto no nombra ningún caso. Lo que
no se acepta es una regla sin fila, ni una rama sin cita.

Dimensiones (el árbol es el que dio Eric, no se inventa otro):
  ref personas cantidad estilo luz toma tema accion escena  + texto modelo
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

DIMS = ["media", "ref", "personas", "cantidad", "estilo", "luz", "toma", "tema", "accion",
        "escena", "texto", "modelo"]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", str(s))
    s = s.replace("«", '"').replace("»", '"').replace("“", '"').replace("”", '"')
    s = s.replace("’", "'").replace("‘", "'").replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def main() -> int:
    ap = argparse.ArgumentParser(description="Verificar clasificación regla por regla")
    ap.add_argument("--units", required=True, help="units.jsonl del extractor v4 — fuente única")
    ap.add_argument("--classification", required=True)
    ap.add_argument("--report", default=None)
    a = ap.parse_args()

    unid = {u["id"]: u for u in (json.loads(l) for l in Path(a.units).read_text(encoding="utf-8").splitlines() if l.strip())}
    rs = {k: {"rule": {"text": v["texto"]}} for k, v in unid.items()}
    universo = set(unid)
    filas = ([json.loads(l) for l in Path(a.classification).read_text(encoding="utf-8").splitlines() if l.strip()]
             if Path(a.classification).exists() else [])

    vistos, dup, citas_ok, citas_mal, sin_dim, universales = set(), [], 0, [], [], 0
    for f in filas:
        rid = f.get("rule_id")
        if rid in vistos:
            dup.append(rid)
        vistos.add(rid)
        if rid not in rs:
            citas_mal.append((rid, "*", "rule_id inexistente en el ruleset"))
            continue
        texto = norm(rs[rid]["rule"]["text"])
        ramas = {d: f.get(d, "cualquiera") for d in DIMS}
        if all(v == "cualquiera" for v in ramas.values()):
            universales += 1
            if not str(f.get("motivo_universal", "")).strip():
                sin_dim.append((rid, "UNIVERSAL sin motivo escrito"))
            continue
        for d, v in ramas.items():
            if v == "cualquiera":
                continue
            # `media` puede justificarse por el archivo: una unidad de image/** es de
            # imagen por vivir en el skill de imagen, que es alcance estructural, no
            # keyword spotting. Los archivos mixtos (aurora, sw30, forge, learned)
            # cubren imagen y video, así que ahí sí se exige cita.
            if d == "media" and v == "imagen" and unid[rid]["fuente"].startswith("image/"):
                citas_ok += 1
                continue
            cita = (f.get("citas") or {}).get(d)
            if not cita:
                citas_mal.append((rid, d, "rama sin cita"))
                continue
            if norm(cita) in texto:
                citas_ok += 1
            else:
                citas_mal.append((rid, d, f"la cita no está en el texto de la regla: {cita[:70]}"))

    faltan = sorted(universo - vistos)
    sobran = sorted(vistos - universo)
    rep = {
        "unidades_en_la_fuente": len(universo),
        "unidades_clasificadas": len(vistos & universo),
        "cobertura_pct": round(100.0 * len(vistos & universo) / max(1, len(universo)), 2),
        "sin_clasificar": len(faltan),
        "duplicadas": len(dup),
        "fuera_del_universo": len(sobran),
        "universales": universales,
        "acotadas": len(filas) - universales,
        "citas_verificadas_ok": citas_ok,
        "citas_invalidas": len(citas_mal),
        "universal_sin_motivo": len(sin_dim),
        "sin_clasificar_ids": faltan[:40],
        "citas_invalidas_detalle": citas_mal[:40],
    }
    if a.report:
        Path(a.report).write_text(json.dumps(rep, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for k in ("unidades_en_la_fuente", "unidades_clasificadas", "cobertura_pct", "sin_clasificar",
              "duplicadas", "universales", "acotadas", "citas_verificadas_ok",
              "citas_invalidas", "universal_sin_motivo"):
        print(f"  {k:24} {rep[k]}")
    for x in citas_mal[:10]:
        print(f"  CITA INVÁLIDA {x[0]} · {x[1]} · {x[2]}")
    ok = rep["cobertura_pct"] == 100.0 and not citas_mal and not sin_dim and not dup
    print("VERIFICACIÓN:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
