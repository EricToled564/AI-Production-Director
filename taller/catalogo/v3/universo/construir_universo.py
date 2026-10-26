"""construir_universo.py: universo de textos según el alcance de Eric del 2026-10-24
(v2/decisiones/DECISIONES_ERIC_20261024.md §1), sobre la base original de 13,005 textos.

    python3 -I construir_universo.py   → universo.json, excluidos.json y UNIVERSO.md junto a este archivo

Regla de este paso: un archivo se excluye entero solo si TODO su contenido queda fuera del alcance; la causa va
escrita en EXCLUSIONES. Todo lo demás entra completo, y la decisión texto por texto (incluido «solo aplica a otro
modelo») la toma el filtro por caso del paso 2. Un archivo idéntico (mismo sha256_archivo) a otro ya incluido entra
una sola vez; las copias quedan registradas como duplicado.
"""
import collections
import fnmatch
import json
import sqlite3
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parents[1] / "corpus" / "BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite"

# (patrón de archivo, causa). Primera coincidencia gana.
EXCLUSIONES = [
    ("*/LICENSE", "licencia: no regula la creación de imágenes"),
    ("*/NOTICE", "aviso de atribución: no regula la creación de imágenes"),
    ("skills/visual-prompt-forge/adapters/flux.md", "solo Flux (otro modelo de imagen)"),
    ("skills/visual-prompt-forge/adapters/midjourney.md", "solo Midjourney (otro modelo de imagen)"),
    ("skills/visual-prompt-forge/adapters/ideogram.md", "solo Ideogram (otro modelo de imagen)"),
    ("skills/visual-prompt-forge/adapters/seedream.md", "solo Seedream (otro modelo de imagen)"),
    ("skills/visual-prompt-forge/adapters/nano-banana.md", "solo Nano Banana (otro modelo de imagen)"),
    ("skills/visual-prompt-forge/adapters/kling.md", "solo Kling (video)"),
    ("skills/visual-prompt-forge/adapters/veo.md", "solo Veo (video)"),
    ("skills/visual-prompt-forge/adapters/seedance.md", "solo Seedance (video)"),
    ("skills/visual-prompt-forge/adapters/hailuo.md", "solo Hailuo (video)"),
    ("skills/visual-prompt-forge/examples/one-shot-all-adapters/flux.txt", "ejemplo solo Flux"),
    ("skills/visual-prompt-forge/examples/one-shot-all-adapters/midjourney.txt", "ejemplo solo Midjourney"),
    ("skills/visual-prompt-forge/examples/one-shot-all-adapters/ideogram.txt", "ejemplo solo Ideogram"),
    ("skills/visual-prompt-forge/examples/one-shot-all-adapters/seedream.txt", "ejemplo solo Seedream"),
    ("skills/visual-prompt-forge/examples/one-shot-all-adapters/nano-banana.txt", "ejemplo solo Nano Banana"),
    ("skills/visual-prompt-forge/examples/one-shot-all-adapters/kling.txt", "ejemplo solo Kling (video)"),
    ("skills/video/references/kling.md", "solo Kling (video)"),
    ("skills/video/references/veo.md", "solo Veo (video)"),
    ("skills/video/references/seedance.md", "solo Seedance (video)"),
    ("skills/video/references/seedance-25.md", "solo Seedance 2.5 (video)"),
    ("skills/storyboard-html-preview/*", "vista HTML del storyboard: maquetación de la entrega, no creación de imágenes"),
    ("skills/screenwriter/*", "guion: texto narrativo, no creación de imágenes"),
    ("skills/*/tools/_shotkit.py", "código auxiliar del kit (rutas y carga de archivos)"),
    ("skills/*/tools/_template.py", "código auxiliar del kit"),
    ("skills/*/tools/check.sh", "código auxiliar del kit"),
    ("skills/*/tools/shots-to-html.py", "genera la vista HTML, no prompts"),
    ("skills/*/tools/copy-prompt.py", "copia prompts al portapapeles"),
    ("skills/*/tools/validate_schemas.py", "valida esquemas JSON del kit"),
    ("skills/*/tools/validate_skills.py", "valida la estructura de los skills"),
]


def causa(archivo):
    for patron, c in EXCLUSIONES:
        if fnmatch.fnmatch(archivo, patron):
            return c
    return None


def main():
    db = sqlite3.connect(f"file:{BASE}?mode=ro", uri=True)
    filas = db.execute("SELECT id, archivo, linea_inicial, sha256_archivo, texto FROM textos "
                       "ORDER BY archivo, CAST(linea_inicial AS INTEGER), id").fetchall()
    por_archivo = collections.OrderedDict()
    for i, a, l, h, t in filas:
        por_archivo.setdefault(a, {"sha": h, "ids": []})["ids"].append(i)
    vistos, universo, excluidos, tabla = {}, [], [], []
    for a, d in por_archivo.items():
        c = causa(a)
        if c:
            estado = "fuera"
        elif d["sha"] in vistos:
            estado, c = "duplicado", f"idéntico a {vistos[d['sha']]}"
        else:
            estado, c = "dentro", ""
            vistos[d["sha"]] = a
        (universo if estado == "dentro" else excluidos).extend(
            {"id": i, "archivo": a, "estado": estado, "causa": c} for i in d["ids"])
        tabla.append((a, len(d["ids"]), estado, c))
    (AQUI / "universo.json").write_text(json.dumps(universo, ensure_ascii=False, indent=0), encoding="utf-8")
    (AQUI / "excluidos.json").write_text(json.dumps(excluidos, ensure_ascii=False, indent=0), encoding="utf-8")
    tot = collections.Counter()
    for _, n, e, _c in tabla:
        tot[e] += n
    assert sum(tot.values()) == 13005 == len(filas)
    md = ["# Universo propuesto — alcance del 2026-10-24", "",
          "Generado por `construir_universo.py` desde la base original de 13,005 textos. Propuesta para revisión de Eric.", "",
          f"| Estado | Textos |", "|---|---:|"] + [f"| {e} | {tot[e]:,} |" for e in ("dentro", "fuera", "duplicado")] + \
         [f"| total | {sum(tot.values()):,} |", "", "| Archivo | Textos | Estado | Causa |", "|---|---:|---|---|"] + \
         [f"| `{a}` | {n} | {e} | {c} |" for a, n, e, c in tabla]
    (AQUI / "UNIVERSO.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(dict(tot), "archivos:", collections.Counter(e for _, _, e, _ in tabla))


if __name__ == "__main__":
    main()
