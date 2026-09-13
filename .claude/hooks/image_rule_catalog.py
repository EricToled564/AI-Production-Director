#!/usr/bin/env python3
"""Cataloga cada regla del lado imagen dentro del árbol de image-taxonomy.

Instrucción de Eric: dividir las reglas de imagen por referencias (0 / 1 / 2+),
por personas (sí / no), las de personas por cantidad (una / grupo), y después por
estilo de fotografía, iluminación, toma, tema y complejidad de acción; las de sin
personas por exterior / interior / animales / arquitectónica / paisaje y estilo.
Hasta que el 100% de las reglas que se refieren a imágenes estén catalogadas.

Dos campos distintos por regla, y la distinción es la que impide matar reglas:

  tema[]    — de qué habla la regla. Sale de que su texto contenga un término del
              léxico de esa dimensión, y se guarda el fragmento literal.
  alcance   — dónde aplica. Por defecto TODAS las ramas. Sólo se propone una
              restricción cuando el texto de la regla enuncia la condición
              ("if/when/for/only ... <término>"), y la propuesta queda marcada
              como candidata: narrow de scope no se aplica sin revisión.

Una regla sin ningún término del léxico no es un hueco del catálogo: es una regla
que aplica a todo caso de imagen, y así queda registrada.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HOOKS = Path(__file__).resolve().parent
sys.path.insert(0, str(HOOKS))
import rule_engine_v3 as E  # noqa: E402

# Enunciados condicionales: el texto de la regla acota su propio alcance.
COND = re.compile(
    r"\b(if|when|whenever|only\s+for|only\s+when|only\s+if|unless|in\s+case\s+of|applies\s+only)\b"
    r"|\b(si|cuando|sólo\s+para|solo\s+para|únicamente|en\s+caso\s+de|aplica\s+sólo)\b"
    r"|\b(если|когда|только\s+для)\b",
    re.IGNORECASE,
)


def patron(termino: str) -> re.Pattern:
    """Frontera de palabra completa; un término con '*' final es prefijo.

    Sin esto `car` matchea dentro de `carga` y el catálogo se llena de basura.
    """
    t = termino[:-1] if termino.endswith("*") else termino
    fin = "" if termino.endswith("*") else r"(?![\w-])"
    return re.compile(r"(?<![\w-])" + re.escape(t) + fin, re.IGNORECASE | re.UNICODE)


def fragmento(texto: str, termino: str, ancho: int = 70) -> str:
    m = patron(termino).search(texto)
    i = m.start() if m else -1
    if i < 0:
        return ""
    a, b = max(0, i - ancho // 2), min(len(texto), i + len(termino) + ancho // 2)
    return ("…" if a else "") + " ".join(texto[a:b].split()) + ("…" if b < len(texto) else "")


def catalogar(regla: dict, taxonomia: dict) -> dict:
    texto = regla["rule"]["text"] or ""
    tema, candidatos = [], []
    for dim in taxonomia["dimensiones"]:
        if dim["id"] == "media":
            continue
        for val in dim["valores"]:
            for termino in val["lexico"]:
                if patron(termino).search(texto):
                    frag = fragmento(texto, termino)
                    tema.append({"dimension": dim["id"], "valor": val["id"],
                                 "termino": termino, "fragmento": frag})
                    if COND.search(frag):
                        candidatos.append({"dimension": dim["id"], "valor": val["id"],
                                           "evidencia": frag})
                    break
    dims = sorted({t["dimension"] for t in tema})
    return {
        "rule_id": regla["rule"]["id"],
        "fuente": f"{regla['rule'].get('source_path')}:{regla['rule'].get('line')}",
        "skill": regla["rule"].get("skill"),
        "effect": regla["metadata"].get("effect"),
        "texto": " ".join(texto.split())[:240],
        "media": "image",
        "tema": tema,
        "dimensiones": dims,
        "alcance": "TODAS" if not dims else "TODAS (restricción no aplicada)",
        "restriccion_candidata": candidatos,
        "catalogada": True,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Catálogo de reglas de imagen por rama")
    ap.add_argument("--ruleset", required=True)
    ap.add_argument("--taxonomy", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", default=None)
    a = ap.parse_args()

    rs = json.loads(Path(a.ruleset).read_text(encoding="utf-8"))["rules"]
    tax = json.loads(Path(a.taxonomy).read_text(encoding="utf-8"))

    img = [r for r in rs if E.eval_condition({"media": "image"}, r["metadata"].get("when") or {}) != "FALSE"]
    filas = [catalogar(r, tax) for r in img]
    Path(a.out).write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")

    por_dim, por_val = {}, {}
    for f in filas:
        for d in f["dimensiones"]:
            por_dim[d] = por_dim.get(d, 0) + 1
        for t in f["tema"]:
            k = f"{t['dimension']}={t['valor']}"
            por_val[k] = por_val.get(k, 0) + 1
    todas = [f for f in filas if not f["dimensiones"]]
    sin_atestiguar = [f"{d['id']}={v['id']}" for d in tax["dimensiones"] if d["id"] != "media"
                      for v in d["valores"] if f"{d['id']}={v['id']}" not in por_val]
    rep = {
        "taxonomy_version": tax["taxonomy_version"],
        "reglas_de_imagen": len(filas),
        "reglas_de_video_excluidas": len(rs) - len(filas),
        "catalogadas": sum(1 for f in filas if f["catalogada"]),
        "cobertura_pct": round(100.0 * sum(1 for f in filas if f["catalogada"]) / max(1, len(filas)), 2),
        "en_todas_las_ramas": len(todas),
        "con_al_menos_una_dimension": len(filas) - len(todas),
        "restricciones_candidatas": sum(len(f["restriccion_candidata"]) for f in filas),
        "por_dimension": dict(sorted(por_dim.items(), key=lambda x: -x[1])),
        "por_valor": dict(sorted(por_val.items(), key=lambda x: -x[1])),
        "valores_sin_ninguna_regla": sin_atestiguar,
    }
    if a.report:
        Path(a.report).write_text(json.dumps(rep, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"CATALOGO: {rep['catalogadas']}/{rep['reglas_de_imagen']} = {rep['cobertura_pct']}%")
    print(f"  en todas las ramas        {rep['en_todas_las_ramas']}")
    print(f"  con dimensión declarada   {rep['con_al_menos_una_dimension']}")
    print(f"  restricciones candidatas  {rep['restricciones_candidatas']}")
    print(f"  valores sin ninguna regla {len(sin_atestiguar)}: {sin_atestiguar}")
    return 0 if rep["cobertura_pct"] == 100.0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
