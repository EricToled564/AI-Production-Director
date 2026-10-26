"""construir_universo.py: universo de textos para la prueba, sobre la base original de 13,005 textos.

    python3 -I construir_universo.py   → universo.json, excluidos.json y UNIVERSO.md junto a este archivo

Alcance (v2/decisiones/DECISIONES_ERIC_20261023.md §1 y DECISIONES_ERIC_20261024.md §1): solo la creación de
imágenes fijas (etapa 5: génesis, maestros, cuadros, edición, borrador de prompt, crítica y canonización) con GPT
Image 2 o sin modelo específico. Las demás etapas (marca, estrategia, guion, dirección, storyboard, video, paquete) y
los textos que solo aplican a otros modelos quedan fuera.

Criterio de INCLUSIÓN: un texto entra solo si su archivo, o el tramo de líneas indicado, está en INCLUSIONES; todo lo
demás queda fuera con su causa. Dentro de lo incluido, la decisión texto por texto (por ejemplo, una línea que solo
vale para Nano Banana) la toma el filtro por caso del paso 2.
"""
import collections
import fnmatch
import json
import sqlite3
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parents[1] / "corpus" / "BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite"

# (patrón de archivo, (línea desde, línea hasta) o None para el archivo completo, por qué entra)
INCLUSIONES = [
    ("skills/image/SKILL.md", None, "skill de prompts de imagen (Nano Banana y GPT Image 2)"),
    ("skills/image/references/*", None, "referencias del skill de imagen; lo que solo aplica a Nano Banana sale en el paso 2"),
    ("skills/visual-prompt-forge/adapters/gpt-image.md", None, "adaptador de GPT Image"),
    ("skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt", None, "ejemplo de prompt GPT Image"),
    ("skills/visual-prompt-forge/SKILL.md", None, "borrador de prompts por adaptador (E5.6); lo de video sale en el paso 2"),
    ("skills/visual-prompt-forge/references/*", None, "anatomía del prompt, locks de consistencia y modos de falla"),
    ("skills/visual-prompt-forge/adapters/_capabilities.json", None, "capacidades por modelo; solo la entrada de GPT Image pasa el paso 2"),
    ("skills/visual-asset-critic/SKILL.md", None, "crítica del render contra el shot (E5.7)"),
    ("skills/visual-asset-critic/references/critique-rubric.md", None, "rúbrica de crítica (E5.7)"),
    ("flujos/flujo-anclas.html", None, "etapa 5: anclas de imagen"),
    ("flujos/flujo-spot.html", (194, 212), "filas E5.1–E5.9 del pipeline: producción de imágenes"),
    ("flujos/flujo-spot.html", (244, 99999), "niveles 3, 3b y 4: taxonomía de génesis, cadena de dependencia y subflujo atómico"),
]

CAUSAS_FUERA = [
    ("*/LICENSE", "licencia"), ("*/NOTICE", "aviso de atribución"),
    ("skills/video/*", "video (etapa 6) o dirección (etapa 3)"),
    ("skills/visual-prompt-forge/adapters/*", "adaptador de otro modelo"),
    ("skills/visual-prompt-forge/examples/*", "ejemplo de otro modelo"),
    ("skills/visual-prompt-forge/tools/*", "código del kit"),
    ("skills/visual-asset-critic/*", "ejemplos, esquemas o código del crítico"),
    ("skills/storyboard-architect/*", "storyboard (etapa 4)"), ("skills/ai-video-storyboard/*", "storyboard de video (etapa 4)"),
    ("skills/screenwriter/*", "guion (etapa 2)"), ("skills/storyboard-html-preview/*", "vista HTML (etapa 7)"),
    ("skills/brand-lock-extractor/*", "marca (etapa 0)"), ("skills/ai-production-director/*", "orquestación de todas las etapas"),
    ("skills/visual-media/*", "animación y glosario"), ("flujos/flujo-spot.html", "etapas 0–4, 6, 7 y POST del pipeline"),
]


def incluye(archivo, linea):
    for patron, tramo, porque in INCLUSIONES:
        if fnmatch.fnmatch(archivo, patron) and (tramo is None or tramo[0] <= linea <= tramo[1]):
            return porque
    return None


def causa_fuera(archivo):
    return next((c for p, c in CAUSAS_FUERA if fnmatch.fnmatch(archivo, p)), "sin regla de inclusión")


def main():
    db = sqlite3.connect(f"file:{BASE}?mode=ro", uri=True)
    filas = db.execute("SELECT id, archivo, CAST(linea_inicial AS INTEGER) FROM textos ORDER BY archivo, 3, id").fetchall()
    universo, excluidos = [], []
    tabla = collections.OrderedDict()
    for i, a, l in filas:
        porque = incluye(a, l)
        reg = {"id": i, "archivo": a, "linea": l, "estado": "dentro" if porque else "fuera",
               "causa": porque or causa_fuera(a)}
        (universo if porque else excluidos).append(reg)
        t = tabla.setdefault(a, collections.Counter())
        t[reg["estado"]] += 1
    assert len(universo) + len(excluidos) == 13005
    (AQUI / "universo.json").write_text(json.dumps(universo, ensure_ascii=False, indent=0), encoding="utf-8")
    (AQUI / "excluidos.json").write_text(json.dumps(excluidos, ensure_ascii=False, indent=0), encoding="utf-8")
    md = ["# Universo de la prueba — creación de imágenes fijas con GPT Image 2", "",
          "Generado por `construir_universo.py` (criterio de inclusión) desde la base original de 13,005 textos.", "",
          f"Dentro: **{len(universo):,}** textos · fuera: {len(excluidos):,}", "",
          "| Archivo | Dentro | Fuera | Por qué entra |", "|---|---:|---:|---|"]
    for a, c in tabla.items():
        if c["dentro"]:
            md.append(f"| `{a}` | {c['dentro']} | {c['fuera']} | {incluye(a, next(r['linea'] for r in universo if r['archivo'] == a))} |")
    fuera = collections.Counter(r["causa"] for r in excluidos)
    md += ["", "| Fuera por | Textos |", "|---|---:|"] + [f"| {c} | {n:,} |" for c, n in fuera.most_common()]
    (AQUI / "UNIVERSO.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("dentro", len(universo), "fuera", len(excluidos))


if __name__ == "__main__":
    main()
