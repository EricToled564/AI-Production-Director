#!/usr/bin/env python3
"""Devuelve a cada regla el contenido que el compilador de bloques le cortó.

El compilador guardó la línea-etiqueta de cada bloque ("**Лицо/персонаж как
референс:**") y dejó fuera el bloque de código o la lista que venía justo
después — que es donde está la plantilla de prompt. La regla quedó sin nada que
aplicar.

Esto no reescribe reglas: relee el archivo fuente instalado y adjunta, verbatim,
las líneas que siguen al bloque hasta cerrar la cerca ``` o hasta que termina la
lista. El texto original se conserva en `text_original`; el añadido va en
`payload`, con su rango de líneas, para que se pueda auditar contra el archivo.
"""
from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

SKILLS = "/root/.claude/skills/synced"


def fuente(source_path: str) -> list[str] | None:
    hits = glob.glob(f"{SKILLS}/*/{source_path}")
    if not hits:
        return None
    return Path(hits[0]).read_text(encoding="utf-8").splitlines()


def payload(lineas: list[str], fin: int) -> tuple[str, int, int]:
    """Contenido que sigue al bloque: cerca de código completa, o lista contigua."""
    i = fin  # fin es 1-based inclusive → lineas[fin] es la siguiente
    while i < len(lineas) and not lineas[i].strip():
        i += 1
    if i >= len(lineas):
        return "", 0, 0
    ini = i
    if lineas[i].strip().startswith("```"):
        j = i + 1
        while j < len(lineas) and not lineas[j].strip().startswith("```"):
            j += 1
        return "\n".join(lineas[ini:min(j + 1, len(lineas))]), ini + 1, min(j + 1, len(lineas))
    if lineas[i].lstrip().startswith(("-", "*", "|")) or lineas[i].lstrip()[:2].rstrip(".").isdigit():
        j = i
        while j < len(lineas) and lineas[j].strip() and not lineas[j].startswith("#"):
            j += 1
        return "\n".join(lineas[ini:j]), ini + 1, j
    return "", 0, 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Reparar el texto truncado de las reglas")
    ap.add_argument("--ruleset", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--only", default=None, help="limitar a un source_path")
    a = ap.parse_args()

    rs = json.loads(Path(a.ruleset).read_text(encoding="utf-8"))["rules"]
    cache: dict[str, list[str] | None] = {}
    filas, sin_archivo = [], set()
    for r in rs:
        q = r["rule"]
        sp = q["source_path"]
        if a.only and sp != a.only:
            continue
        texto = " ".join(str(q["text"]).split())
        # Sólo reglas-etiqueta. Una que ya es un ítem de lista está completa: pegarle
        # los ítems hermanos la duplicaría con las reglas que ya son esos hermanos.
        es_item = texto.lstrip().startswith(("-", "*", "✅", "❌", "|")) or texto.lstrip()[:2].rstrip(".").isdigit()
        if es_item or not (texto.endswith(":") or len(texto) < 45):
            continue
        if sp not in cache:
            cache[sp] = fuente(sp)
        L = cache[sp]
        if L is None:
            sin_archivo.add(sp)
            continue
        pl, d, h = payload(L, q.get("end_line") or q["line"])
        if not pl.strip():
            continue
        filas.append({
            "rule_id": q["id"], "source_path": sp, "line": q["line"],
            "text_original": str(q["text"]), "payload": pl,
            "payload_lines": [d, h],
            "text_reparado": str(q["text"]).rstrip() + "\n" + pl,
        })
    Path(a.out).write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")
    print(f"REPARADAS: {len(filas)} reglas recuperaron su contenido")
    if sin_archivo:
        print(f"  archivos fuente no encontrados: {len(sin_archivo)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
