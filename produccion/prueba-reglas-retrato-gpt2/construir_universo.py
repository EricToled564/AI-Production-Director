"""Universo de textos de la prueba de retratos GPT Image 2 y lotes de revisión.

Universo = los 1,511 textos de la decisión 1 (DECISIONES_ERIC_20261023.md, `taller/catalogo/universo_ids.json`,
con su id INV original) + los documentos del bloque del piloto (PILOTO_V5_INSTRUCCIONES §4.1) que no están en
`skills/image/**` + `produccion-visual-sw30/SKILL.md` (template T1 de rostros). Los documentos extra se parten con
la misma unidad que la base original: una línea no vacía = un texto.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
AQUI = Path(__file__).resolve().parent
PKG = RAIZ / "apd/.cache/pkg/AI_Production_Director_v3.4.0_COMPLETE"

EXTRA = [
    "skills/visual-prompt-forge/SKILL.md",
    "skills/visual-prompt-forge/adapters/_capabilities.json",
    "skills/visual-prompt-forge/references/prompt-anatomy.md",
    "skills/visual-prompt-forge/references/failure-modes.md",
    "skills/ai-production-director/SKILL.md",
    "skills/visual-asset-critic/SKILL.md",
    "skills/visual-asset-critic/references/critique-rubric.md",
    "skills/produccion-visual-sw30/SKILL.md",
]

# Lotes por archivo, de tamaño parecido; un archivo nunca se parte (el revisor lee el documento entero).
LOTES = {
    "01": ["skills/image/SKILL.md", "skills/image/references/gpt-image.md", "skills/image/references/models.md",
           "skills/visual-prompt-forge/adapters/gpt-image.md",
           "skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt"],
    "02": ["skills/image/references/golden-rules.md", "skills/image/references/prompt-framework.md",
           "skills/image/references/patterns/portrait-cinema.md"],
    "03": ["skills/image/references/creative-direction.md", "skills/image/references/characters.md",
           "skills/image/references/patterns/fashion-editorial.md", "skills/image/references/patterns/character-design.md",
           "skills/image/references/vision-decomposer.md"],
    "04": ["skills/image/references/text-rendering.md", "skills/image/references/nano-banana.md",
           "skills/image/references/editing.md", "skills/image/references/patterns/poster-illustration.md",
           "skills/image/references/structural.md", "skills/image/references/dimensional.md"],
    "05": ["skills/image/references/slides.md", "skills/image/references/multi-panel.md",
           "skills/image/references/storyboards.md", "skills/image/references/patterns/food-beverage.md",
           "skills/image/references/patterns/ecommerce.md", "skills/image/references/patterns/ui-social.md"],
    "06": EXTRA[:4],
    "07": EXTRA[4:],
}


def extra_unidades(rel):
    lineas = (PKG / rel).read_text(encoding="utf-8").splitlines()
    pila, out = [], []
    corto = rel.split("/")[1] + "/" + rel.split("/")[-1]
    for n, l in enumerate(lineas, 1):
        if not l.strip():
            continue
        if l.startswith("#"):
            nivel = len(l) - len(l.lstrip("#"))
            pila = pila[:nivel - 1] + [l.lstrip("#").strip()]
        out.append({"id": f"EXT-{corto}-{n:04d}", "archivo": rel, "linea": str(n),
                    "encabezado": " › ".join(pila), "texto": l})
    return out


def main():
    cat = json.loads((RAIZ / "taller/catalogo/catalogo_imagen_gpt2.json").read_text(encoding="utf-8"))
    univ = [{k: x[k] for k in ("id", "archivo", "linea", "encabezado", "texto")} for x in cat]
    for rel in EXTRA:
        univ += extra_unidades(rel)
    ids = [u["id"] for u in univ]
    assert len(ids) == len(set(ids)), "ids duplicados"
    por_archivo = {}
    for u in univ:
        por_archivo.setdefault(u["archivo"], []).append(u)
    asignados = [a for v in LOTES.values() for a in v]
    assert sorted(asignados) == sorted(por_archivo), set(por_archivo) ^ set(asignados)
    (AQUI / "universo.json").write_text(json.dumps(univ, ensure_ascii=False, indent=0), encoding="utf-8")
    (AQUI / "lotes").mkdir(exist_ok=True)
    for k, archivos in LOTES.items():
        unidades = [u for a in archivos for u in por_archivo[a]]
        (AQUI / f"lotes/lote_{k}.json").write_text(json.dumps(unidades, ensure_ascii=False, indent=0), encoding="utf-8")
        print(k, len(unidades), sum(len(u["texto"]) for u in unidades))
    print("universo", len(univ))


if __name__ == "__main__":
    main()
