#!/usr/bin/env python3
"""Rinde el árbol de decisión de Eric con el TEXTO ÍNTEGRO de cada regla asignada.

Es el entregable que Eric pidió: «una lista con cada sección del árbol de decisión
con el texto íntegro de cada regla que le asignaste». No un resumen ni un conteo.

Orden del árbol, el que dio Eric y no otro:

  imagen → referencias (0 / 1 / 2+) → personas (sí / no)
    con personas → cantidad (una / grupo)
        → estilo de fotografía · iluminación · toma · tema · complejidad de acción
    sin personas → escena (exterior, interior, animales, arquitectónica, paisaje,
        producto, urbana) → estilo de fotografía
  y las demás categorías que las reglas nombran: texto en imagen, modelo generador.

Una regla aparece en cada rama que su propio texto nombra, con la cita literal que
lo justifica debajo. Las que su texto no acota van en TODAS LAS RAMAS, con el motivo
escrito. Nada queda sin sección.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DIMS = ["ref", "personas", "cantidad", "estilo", "luz", "toma", "tema", "accion",
        "escena", "texto", "modelo"]

TITULOS = {
    "ref": "REFERENCIAS",
    "personas": "PERSONAS",
    "cantidad": "CANTIDAD DE PERSONAS",
    "estilo": "ESTILO DE FOTOGRAFÍA",
    "luz": "ILUMINACIÓN",
    "toma": "TAMAÑO DE TOMA",
    "tema": "TEMA",
    "accion": "COMPLEJIDAD DE ACCIÓN",
    "escena": "ESCENA SIN PERSONAS",
    "texto": "TEXTO EN IMAGEN",
    "modelo": "MODELO GENERADOR",
}

ETIQUETAS = {
    "ref": {"0": "sin referencia (texto a imagen)", "1": "una referencia",
            "2+": "ancla con 2 o más referencias"},
    "personas": {"si": "con personas", "no": "sin personas"},
    "cantidad": {"1": "una persona", "grupo": "grupo de personas"},
    "escena": {"exterior": "exterior", "interior": "interior", "animales": "animales / fauna",
               "arquitectonica": "arquitectónica / inmobiliaria", "paisaje_natural": "paisaje natural",
               "producto_objeto": "producto u objeto", "urbana": "urbana / cityscape"},
    "luz": {"estudio": "estudio", "natural_exterior": "natural exterior", "ventana": "luz de ventana",
            "golden_hour": "golden hour / hora azul", "artificial_nocturna": "artificial nocturna",
            "mixta": "mixta"},
    "toma": {"macro": "macro / detalle", "close_up": "close-up", "plano_medio": "plano medio",
             "cuerpo_completo": "cuerpo completo", "plano_general": "plano general"},
    "accion": {"estatica": "estática", "pose_dirigida": "pose dirigida",
               "accion_simple": "acción simple", "accion_compleja": "acción compleja"},
    "texto": {"none": "sin texto", "in_image": "texto dentro de la imagen",
              "composite": "texto compuesto después"},
}


def bloque(fila: dict, unidad: dict, cita: str | None) -> list[str]:
    L = [f"**`{unidad['fuente']}:{unidad['linea']}`**", ""]
    L.append("> " + "\n> ".join(unidad["texto"].splitlines()))
    L.append("")
    L.append(f"*Qué dice:* {fila['resumen']}")
    if cita:
        L.append(f"*Cita que la coloca en esta rama:* «{cita}»")
    L.append("")
    return L


def main() -> int:
    ap = argparse.ArgumentParser(description="Rendir el árbol con el texto íntegro de cada regla")
    ap.add_argument("--units", required=True)
    ap.add_argument("--classification", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    unid = {u["id"]: u for u in (json.loads(l) for l in Path(a.units).read_text(encoding="utf-8").splitlines() if l.strip())}
    filas = [json.loads(l) for l in Path(a.classification).read_text(encoding="utf-8").splitlines() if l.strip()]
    porid = {f["rule_id"]: f for f in filas}

    video = [f for f in filas if f.get("media") == "video"]
    img = [f for f in filas if f.get("media") != "video"]
    universales = [f for f in img if all(f.get(d, "cualquiera") == "cualquiera" for d in DIMS)]
    noregla = [f for f in universales if str(f.get("motivo_universal", "")).startswith("No es regla")]
    uni_reales = [f for f in universales if f not in noregla]

    L: list[str] = []
    L.append("# IMAGEN — el árbol de decisión con el texto íntegro de cada regla\n")
    L.append(f"Fuente única: el paquete `AI_Production_Director_v3.4.0_COMPLETE` que entregó Eric, "
             f"con sus hashes en `.claude/rules/v4/SOURCE_SHA256.txt`.\n")
    L.append(f"**{len(filas)} unidades leídas una por una.** {len(video)} quedaron del lado video en el "
             f"nivel 1 del árbol. {len(img)} son del lado imagen.\n")
    L.append("Cada rama que se le asigna a una regla lleva la cita literal de esa misma regla que lo "
             "justifica, y `rule_class_verify.py` comprueba que la cita exista en su texto. Una regla "
             "aparece en todas las ramas que su texto nombra.\n")
    L.append("---\n")

    L.append("## NIVEL 1 — VIDEO (fuera del alcance de imagen)\n")
    L.append(f"{len(video)} unidades cuyo propio texto dice que son de video.\n")
    for f in video:
        L += bloque(f, unid[f["rule_id"]], (f.get("citas") or {}).get("media"))

    L.append("---\n")
    L.append(f"## TODAS LAS RAMAS — {len(uni_reales)} reglas\n")
    L.append("Reglas cuyo texto no acota ninguna rama: aplican a cualquier caso de imagen. "
             "Cada rama de abajo las lleva además de las suyas.\n")
    for f in uni_reales:
        L += bloque(f, unid[f["rule_id"]], None)
        L.append(f"*Por qué en todas las ramas:* {f.get('motivo_universal','')}\n")

    for dim in DIMS:
        vals: dict[str, list[dict]] = {}
        for f in img:
            v = f.get(dim, "cualquiera")
            if v == "cualquiera":
                continue
            for parte in str(v).split(","):
                vals.setdefault(parte.strip(), []).append(f)
        if not vals:
            continue
        L.append("---\n")
        L.append(f"# {TITULOS[dim]}\n")
        for val in sorted(vals, key=lambda x: (-len(vals[x]), x)):
            etq = ETIQUETAS.get(dim, {}).get(val, val)
            L.append(f"## {TITULOS[dim]} = `{val}` — {etq} — {len(vals[val])} reglas\n")
            for f in vals[val]:
                L += bloque(f, unid[f["rule_id"]], (f.get("citas") or {}).get(dim))

    L.append("---\n")
    L.append(f"## NO SON REGLAS — {len(noregla)} unidades\n")
    L.append("Separadores de maquetación, créditos de autoría, comentarios HTML con el concepto de "
             "origen, changelogs, contadores de versión, formularios de aprobación, inventarios de "
             "archivos y punteros cruzados. Quedan registradas con su razón, no borradas.\n")
    for f in noregla:
        u = unid[f["rule_id"]]
        L.append(f"- `{u['fuente']}:{u['linea']}` — {f.get('motivo_universal','')}")

    Path(a.out).write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"ÁRBOL RENDIDO: {a.out}")
    print(f"  unidades          {len(filas)}")
    print(f"  lado video        {len(video)}")
    print(f"  todas las ramas   {len(uni_reales)}")
    print(f"  no son reglas     {len(noregla)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
