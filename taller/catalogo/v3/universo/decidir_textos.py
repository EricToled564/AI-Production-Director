"""decidir_textos.py: decisión por texto dentro de las secciones «dentro» que nombran un modelo.

    python3 -I decidir_textos.py   → lectura_textos_con_modelo.txt, decision_textos.json

Regla (Eric, 2026-10-24, DECISIONES_ERIC_20261024.md §1): entra todo texto de creación de imagen; sale solo el que es
relevante únicamente para modelos que no son GPT Image 2. Un texto que no nombra ningún modelo no puede ser «solo de
otro modelo» y entra. Por eso aquí se leen, uno por uno, los textos de secciones «dentro» que nombran un modelo
(regex MODELO, 217 textos), más la sección 1344, cuyo documento declara gpt-image-1.5.

Límite comprobado: INV-002054 («Up to 14 reference images (6 high-fidelity)», characters.md:3) no nombra ningún
modelo y su cifra es de Nano Banana. Un dato de un solo modelo puede ir sin el nombre del modelo, así que esta lectura
no cierra por sí sola el universo: faltan por leer los textos «dentro» de documentos que no declaran su modelo.

Criterio aplicado al leer:
- sale si el texto solo habla de otro modelo (Nano Banana, Flux, Midjourney, Ideogram, Seedream, Stable Diffusion,
  gpt-image-1.5/1/1-mini) o de un modelo de video (Kling, Veo, Seedance, Hailuo), o solo enlaza su archivo;
- entra si nombra GPT Image 2 o la familia GPT Image (1.5 / 2), si compara modelos incluido GPT Image, o si el modelo
  aparece solo como ejemplo de una regla o herramienta genérica.
"""
import json
import re
import sqlite3
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parents[1] / "corpus" / "BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite"
MODELO = re.compile(r"nano.?banana|\bNB2?\b|\bNBP\b|gpt.?image|dall.?e|\bflux\b|midjourney|\bMJ\b|ideogram|seedream|"
                    r"kling|\bveo\b|seedance|hailuo|stable diffusion|imagen", re.I)

SALE = {
    # flujos/flujo-anclas.html
    "INV-000017": "solo fuentes de keyframe para Nano Banana y modelos de video (Kling, Veo, Seedance)",
    "INV-000206": "EN.7: ensamble en video, Kling Elements y Seedance @Image",
    "INV-000221": "escena compleja: solo NBP",
    "INV-000223": "hero photoreal: solo Flux 2 Pro o Midjourney v7",
    "INV-000224": "variantes baratas: NB2 Lite o gpt-image-1-mini, ninguno es GPT Image 2",
    "INV-000265": "fila Kling 3.0 (imagen a video)",
    "INV-000266": "fila Veo 3.1 (imagen a video)",
    "INV-000267": "fila Seedance 2.5 (imagen a video)",
    # flujos/flujo-spot.html
    "INV-000439": "modelo de rostro: NB2 o NBP",
    "INV-000449": "arquitectura fiel: solo NB2",
    "INV-000453": "especie animal: NB2 con grounding",
    "INV-000454": "física compleja: NBP",
    "INV-000455": "límites de referencias de NB2 y NBP",
    "INV-000458": "distorsión física: NBP",
    "INV-000529": "etiqueta de diagrama: Nano Banana Pro o NB2",
    "INV-000542": "etiqueta de diagrama: Nano Banana 2 con Image Grounding",
    "INV-000543": "etiqueta de diagrama: nano-banana.md",
    "INV-000546": "«Leer nano-banana.md»",
    # skills/image
    "INV-002003": "enruta movimiento y clips (Seedance, Kling, Veo) al skill de video",
    "INV-002013": "enlace y capacidades de nano-banana.md",
    "INV-002196": "edición en Nano Banana",
    "INV-002227": "«NBP understands materials»",
    "INV-002276": "recorrido de costo en Nano Banana",
    "INV-002383": "input_fidelity: solo gpt-image-1.5/1; el propio texto dice que en gpt-image-2 ya es alto por defecto",
    "INV-002412": "gpt-image-1-mini",
    "INV-002531": "Borderless Grid: modelo NBP",
    "INV-002593": "sin texto y composición compleja: NBP",
    "INV-002755": "patrón Inflatable: recomendado NBP",
    "INV-002789": "patrón Roller Skating: recomendado NB2",
    "INV-002796": "patrón 3D Blob: recomendado NBP",
    "INV-002849": "patrón Naturalist: recomendado NB2",
    "INV-002856": "patrón City Food Map: recomendado NB2",
    "INV-002910": "patrón City Across Two Centuries: recomendado NBP",
    "INV-002940": "patrón Peacock: recomendado NB2",
    "INV-002990": "enlace a nano-banana.md",
    "INV-003296": "texto en imagen con Nano Banana",
    # skills/visual-prompt-forge/SKILL.md: lista de adaptadores
    "INV-011301": "adapters/midjourney.md",
    "INV-011302": "adapters/flux.md",
    "INV-011303": "adapters/ideogram.md",
    "INV-011305": "adapters/nano-banana.md",
    "INV-011306": "adapters/seedream.md",
    "INV-011307": "adapters/kling.md (video)",
    "INV-011308": "adapters/veo.md (video)",
    "INV-011309": "adapters/seedance.md (video)",
    "INV-011310": "adapters/hailuo.md (video)",
    # skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt (sección 1344): el documento declara
    # «Generator: gpt-image (1.5)» y «model=gpt-image-1.5»
    "INV-012202": "ejemplo generado para gpt-image-1.5 (cabecera del documento)",
    "INV-012203": "ejemplo generado para gpt-image-1.5",
    "INV-012204": "ejemplo generado para gpt-image-1.5",
    "INV-012205": "ejemplo generado para gpt-image-1.5",
    # references/consistency-locks.md
    "INV-012232": "seed lock: Flux, Seedream, Ideogram, Stable Diffusion",
    "INV-012236": "seeds en Midjourney, Veo y Seedance",
    "INV-012238": "referencia de imagen en Midjourney v7, Ideogram v3 y Nano Banana",
    "INV-012243": "Midjourney --cref",
    "INV-012244": "Ideogram omni-reference",
    "INV-012245": "Nano Banana referenceImages",
    "INV-012249": "Midjourney --sref",
    "INV-012250": "Ideogram style reference",
    "INV-012251": "Flux sin style reference",
    # references/failure-modes.md
    "INV-012291": "hero shots: Flux 2 Pro o Midjourney v7",
    "INV-012305": "Midjourney --cref --cw 50",
    "INV-012311": "Midjourney para trabajo con texto",
    "INV-012315": "texto en imagen: Ideogram v3",
    "INV-012318": "aceptar el resultado de Ideogram",
    # references/prompt-anatomy.md
    "INV-012411": "orden de palabras en Midjourney y Kling",
    "INV-012414": "fortalezas de Ideogram y Flux",
}

# Entran, pero con una nota para la clasificación: el modelo nombrado es solo ejemplo, o el texto lleva una cifra de
# otro modelo junto a contenido genérico.
NOTA = {
    "INV-000220": "entra porque fija el papel de GPT Image 2 (solo anclas de época, no geometría real)",
    "INV-000477": "la columna de modelo es de Nano Banana; entran el resto de la fila (auditar anatomía y pelaje)",
    "INV-000479": "«Cualquiera; NBP si…»: aplica a cualquier modelo",
    "INV-000605": "grounding es de NB2; la verificación contra la realidad es genérica",
    "INV-002054": "«Up to 14 reference images (6 high-fidelity)» es la cifra de Nano Banana (nano-banana.md:64); "
                  "para GPT Image 2 son 16 (gpt-image.md:102)",
    "INV-003035": "el imperativo «formula en positivo» es genérico; NBP es el ejemplo",
    "INV-003039": "dice qué solo hace Nano Banana, es decir, qué no pedirle a GPT Image 2",
    "INV-009814": "regla genérica de re-roll; Flux es el ejemplo",
    "INV-011314": "regla de validación de la herramienta; nano-banana es el ejemplo",
    "INV-011325": "plantilla de salida para cualquier generador; midjourney es el ejemplo",
    "INV-011336": "uso de copy-prompt.py; midjourney.txt es el ejemplo",
    "INV-011363": "regla genérica de texto compuesto aparte; Ideogram es la excepción",
    "INV-011375": "el adaptador manda sobre el entrenamiento; Midjourney es el ejemplo",
    "INV-011406": "uso de validate_prompts.py y copy-prompt.py; flux.txt es el ejemplo",
    "INV-012283": "las muletillas de Stable Diffusion se prohíben en los demás generadores, GPT Image incluido",
    "INV-012317": "fuentes simples para texto en imagen, en cualquier generador",
    "INV-012366": "rendimientos decrecientes del prompt; NB es una de las dos salidas, la otra es postproducción",
    "INV-012401": "el texto nunca va en el prompt; Ideogram es la excepción",
}


def main():
    dec = json.loads((AQUI / "decision_secciones.json").read_text(encoding="utf-8"))
    db = sqlite3.connect(f"file:{BASE}?mode=ro", uri=True)
    texto = dict(db.execute("SELECT id, texto FROM textos"))
    sec_de = {i: d for d in dec for i in d["ids"]}
    sec1344 = next(d for d in dec if d["n"] == 1344)
    assert sec1344["archivo"].endswith("one-shot-all-adapters/gpt-image.txt") and sec1344["estado"] == "dentro"
    leidos = [i for d in dec if d["estado"] == "dentro" for i in d["ids"]
              if MODELO.search(texto[i]) or d["n"] == 1344 or i in NOTA]
    assert set(SALE) <= set(leidos) and set(NOTA) <= set(leidos) and not set(SALE) & set(NOTA)
    lineas, filas = [], []
    for i in leidos:
        d = sec_de[i]
        estado = "sale" if i in SALE else "entra"
        motivo = SALE.get(i) or NOTA.get(i, "")
        filas.append({"id": i, "seccion": d["n"], "archivo": d["archivo"], "estado": estado, "motivo": motivo})
        lineas += [f"### {i} | sec {d['n']} | {d['archivo']} | {estado.upper()}" + (f" | {motivo}" if motivo else ""),
                   texto[i], ""]
    (AQUI / "lectura_textos_con_modelo.txt").write_text("\n".join(lineas), encoding="utf-8")
    (AQUI / "decision_textos.json").write_text(json.dumps(filas, ensure_ascii=False, indent=0), encoding="utf-8")
    print("leídos", len(leidos), "salen", len(SALE), "entran", len(leidos) - len(SALE), "con nota", len(NOTA))


if __name__ == "__main__":
    main()
