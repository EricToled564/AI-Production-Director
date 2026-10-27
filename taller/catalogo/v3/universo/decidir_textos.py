"""decidir_textos.py: decisión por texto dentro de las secciones «dentro» que nombran un modelo.

    python3 -I decidir_textos.py   → lectura_textos_con_modelo.txt, decision_textos.json

Regla (Eric, 2026-10-24, DECISIONES_ERIC_20261024.md §1): entra todo texto de creación de imagen; sale solo el que es
relevante únicamente para modelos que no son GPT Image 2. Un texto que no nombra ningún modelo no puede ser «solo de
otro modelo» y entra. Por eso aquí se leen, uno por uno, los textos de secciones «dentro» que nombran un modelo
(regex MODELO, 217 textos), más la sección 1344, cuyo documento declara gpt-image-1.5.

INV-002054 («Up to 14 reference images (6 high-fidelity)», characters.md:3) no nombra ningún modelo. Su documento
no restringe modelo: image/SKILL.md lo carga en el Paso 4 (L52, L58), después de elegir modelo (Pasos 1 y 2). Sus
cifras son exactamente el desglose de NBP: 14 refs = 6 objetos de alta fidelidad + 5 character + 3 style
(nano-banana.md:64-66, :144; models.md:20, :62); para GPT Image 2 el corpus da 16 y alta fidelidad por defecto
(gpt-image.md:96, :102).
Un texto sin nombre de modelo puede no valer para GPT Image 2. Por eso también se leen todos los textos
«dentro» de los 13 documentos que no declaran a qué modelo aplican (SIN_DECLARACION). Los documentos que sí lo declaran
(golden-rules, prompt-framework, text-rendering, editing, image/SKILL, models: los dos modelos; gpt-image.md y los 7
patterns: GPT Image 2; adaptador forge: GPT Image 1.5/2; flujos y director) se rigen por su declaración.

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
    "INV-002412": "gpt-image-1-mini",
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
    # seed: el adaptador GPT Image no tiene parámetro seed (adapters/gpt-image.md:24-28, ni _capabilities.json) y
    # consistency-locks.md:37 limita el seed a Flux, Seedream, Ideogram y Stable Diffusion
    "INV-012231": "título «Lock 4. Seed locking»: seed no existe en GPT Image",
    "INV-012233": "seed en shots.json: no existe en GPT Image",
    "INV-012234": "ejemplo JSON de seed: no existe en GPT Image",
    "INV-012235": "el adaptador aplica el seed: no existe en GPT Image",
    "INV-012266": "fila «Seed | Random feature drift»: no existe en GPT Image",
    "INV-012298": "causa «Seed not locked»: no existe en GPT Image",
    "INV-012304": "arreglo «Lock seed at storyboard level»: no existe en GPT Image",
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
    "INV-002383": "entra (Eric, 2026-10-27, 26 §18): «Remove [X]. Do not change anything else.» es la plantilla de quitar "
                  "objeto de GPT Image 2; la cláusula input_fidelity es de gpt-image-1.5/1 y se quita en correcciones.json",
    "INV-002531": "entra (Eric, 2026-10-27, 26 §18): L162, el tamaño 1536x1024 de la plantilla 4x3, no depende del "
                  "modelo; L163 (NBP) y L164 (rótulo) se quitan en correcciones.json",
    "INV-000220": "entra porque fija el papel de GPT Image 2 (solo anclas de época, no geometría real)",
    "INV-000477": "la columna de modelo es de Nano Banana; entran el resto de la fila (auditar anatomía y pelaje)",
    "INV-000479": "«Cualquiera; NBP si…»: aplica a cualquier modelo",
    "INV-000605": "grounding es de NB2; la verificación contra la realidad es genérica",
    "INV-002054": "el documento no dice a qué modelo se refiere y image/SKILL.md lo carga en el Paso 4 (L58) sin "
                  "restringir modelo. «14 (6 high-fidelity)» es exactamente el desglose de NBP: hasta 14 refs "
                  "(models.md:20, :62) = 6 objetos de alta fidelidad + 5 character + 3 style (nano-banana.md:64-66, "
                  ":144). Para GPT Image 2 el corpus da hasta 16 con rol (SKILL.md:43, golden-rules.md:93, "
                  "gpt-image.md:102, models.md:20, :54) y alta fidelidad por defecto (gpt-image.md:96). Corregido a la "
                  "cifra de GPT Image 2 por decisión de Eric (correcciones.json, DECISIONES_ERIC_20261026.md §1)",
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
    # Leídos entre los 910 sin nombre de modelo: entran, con una tensión que la clasificación debe resolver
    "INV-002125": "lente: vale para los dos modelos, coherente con prompt-framework.md:42-44 (ver CONTRADICCIONES.md §2)",
    "INV-003433": "contradicción real con gpt-image.md:7 y golden-rules.md:25-28; decisión pendiente de Eric (CONTRADICCIONES.md §3)",
    "INV-012272": "no choca con multi-panel.md:308 (una sola imagen); queda abierta con storyboards.md (CONTRADICCIONES.md §4)",
    "INV-012287": "«50mm prime, f/2.0» es borrador del forge; en el prompt final de GPT Image 2 va como «50mm feel» (director §6.4; CONTRADICCIONES.md §2)",
}

def ids(a, b):
    """INV-a … INV-b, ambos incluidos."""
    return {f"INV-{n:06d}" for n in range(a, b + 1)}


# Secciones mixtas (decidir_secciones.py): cada texto leído. Por sección: estado por defecto y excepciones con motivo.
# «entra» = regula o describe la creación de una imagen fija con GPT Image 2 o con cualquier modelo.
FUERA_ETAPA = "otra etapa: no regula la creación de la imagen"
MIXTA = {
    11: ("sale", "título y leyenda del mapa del spot completo", {
        "INV-000297": "entra: presenta la taxonomía de génesis y el subflujo atómico que produce imágenes",
        "INV-000301": "entra: leyenda «génesis y lo que hereda de ella»"}),
    12: ("sale", "megaflujo: etapas de marca, estrategia, guion, dirección, storyboard, video y entrega",
         {i: "entra: Etapa 5, imágenes ancla y su gate de crítica" for i in ids(337, 342) | {"INV-000358"}}),
    13: ("sale", "subprocesos de etapas que no crean imagen",
         {i: "entra: subproceso E5 (imágenes ancla)" for i in ids(392, 401)}),
    16: ("entra", "", {
        **{i: "sale: herencia hacia el clip de video" for i in ("INV-000499", "INV-000500")},
        **{i: "sale: video, edición en NLE y spot final" for i in ids(518, 522)}}),
    34: ("entra", "vocabulario prohibido en todo prompt final", {}),
    35: ("entra", "todo prompt final en la sintaxis del modelo destino", {}),
    37: ("entra", "el borrador de forge se reescribe a la sintaxis del skill image", {}),
    277: ("entra", "", {
        "INV-002420": "sale: lugar real con grounding → Nano Banana",
        "INV-002421": "sale: escena compleja con física → Nano Banana Pro",
        "INV-002423": "sale: generación barata → NB2 Lite o gpt-image-1-mini",
        "INV-002428": "sale: storyboards y cómics → Nano Banana"}),
    282: ("entra", "tabla que compara la sintaxis de los dos modelos", {}),
    283: ("entra", "", {
        "INV-002463": "sale: costo de Nano Banana 2 Lite", "INV-002464": "sale: costo de Nano Banana 2",
        "INV-002465": "sale: costo de Nano Banana Pro", "INV-002469": "sale: costo de gpt-image-1-mini"}),
    348: ("entra", "", {"INV-002890": "sale: «Recommended model: NB2»"}),
    349: ("entra", "", {"INV-002897": "sale: «Recommended model: NBP»"}),
    667: ("entra", "composición que reserva espacio al texto", {
        "INV-005732": "sale: campo rationale de shots.json (storyboard)"}),
    676: ("entra", "tamaño del sujeto en el cuadro", {}),
    677: ("entra", "ángulo de cámara", {}),
    678: ("sale", "movimiento de cámara: video", {
        "INV-005805": "entra: en una imagen fija el movimiento es solo intención para el editor"}),
    679: ("entra", "profundidad de campo", {}),
    680: ("entra", "luz definida una vez en series_lock", {}),
    681: ("entra", "descripción del sujeto", {}),
    682: ("entra", "qué va en subject, series_lock y brand_lock", {}),
    804: ("entra", "lo que debe hacer una imagen fija clave", {}),
    805: ("entra", "tarjeta de la imagen fija clave", {}),
    806: ("sale", "cuántos paneles por beat: planificación del animatic", {}),
    807: ("entra", "movimiento compuesto en una imagen fija", {}),
    808: ("entra", "emoción sin rostro en una imagen fija", {}),
    809: ("entra", "el cuadro cargado: capas de profundidad y foco", {}),
    810: ("entra", "de la tarjeta al prompt de imagen", {}),
    811: ("sale", "tablero de animatic de 30 s (tiempo, sonido, densidad): storyboard", {}),
    812: ("entra", "checklist de la imagen fija", {
        "INV-008093": "sale: celda de sonido de la tarjeta (storyboard)",
        "INV-008094": "sale: densidad de paneles (storyboard)",
        "INV-008095": "sale: entrega al modelo de video como primer frame"}),
    815: ("entra", "vocabulario de encuadre", {"INV-008130": "sale: «locked-off frame», cámara fija de video"}),
    817: ("entra", "lenguaje de lente", {}),
    818: ("entra", "fuentes de luz", {}),
    819: ("entra", "dirección de luz", {}),
    820: ("entra", "calidad de luz", {}),
    821: ("entra", "paleta con colores concretos", {}),
    867: ("sale", "manos: negativos para Kling y frase positiva para Seedance y Veo", {}),
    870: ("entra", "caras con aspecto de IA: lenguaje de producción", {}),
    871: ("entra", "gemelos y caras fundidas en escenas con varias personas", {}),
    957: ("entra", "velocidad en un solo cuadro", {}),
    962: ("entra", "luz y color sin rostro", {}),
    963: ("entra", "paleta fría", {}),
    964: ("entra", "recetas de luz", {}),
    967: ("entra", "anti-fake del cuadro", {"INV-009107": "sale: orden de los beats rituales de la secuencia"}),
    1183: ("entra", "triángulo de exposición", {}),
    1184: ("entra", "reglas de composición", {}),
    1185: ("entra", "uso de la luz", {}),
    1230: ("entra", "", {
        **{i: "sale: fila de adaptador de otro modelo de imagen" for i in ids(11394, 11396) | {"INV-011398", "INV-011399"}},
        **{i: "sale: fila de adaptador de video" for i in ids(11400, 11403)}}),
    1233: ("entra", "", {
        **{i: "sale: entrada de Midjourney, Flux o Ideogram en la matriz" for i in ids(11431, 11478)},
        **{i: "sale: entrada de Nano Banana, Seedream o de un modelo de video en la matriz" for i in ids(11495, 11590)}}),
    1337: ("entra", "ejemplo de calibración entre adaptadores, GPT Image incluido", {}),
    1338: ("entra", "shot de origen del ejemplo", {}),
    1339: ("entra", "series_lock del ejemplo", {}),
    1340: ("entra", "brand mood del ejemplo", {}),
    1341: ("entra", "", {
        **{i: "sale: salida de otro modelo (o de gpt-image-1.5, ver sección 1344)" for i in ids(12182, 12188)},
        "INV-012189": "sale: adaptadores de video",
        "INV-012191": "sale: sintaxis de Midjourney", "INV-012192": "sale: sintaxis de Flux",
        "INV-012194": "sale: sintaxis de Seedream", "INV-012195": "sale: Kling y modelos de video"}),
    1342: ("entra", "el texto en pantalla no entra en ningún prompt", {}),
}
NOTA_MIXTA = {
    "INV-002422": "«solo NB soporta 1:8, 8:1, 4:1»: lo que no pedirle a GPT Image 2",
    "INV-008061": "la primera frase (vocabulario de encuadre, lente y luz) es de imagen; el resto entrega a video",
}

# Documentos cuyos textos «dentro» se leyeron todos, uno por uno, porque el documento no declara a qué modelo aplica:
# un dato de un solo modelo puede ir sin el nombre del modelo (INV-002054).
SIN_DECLARACION = (
    "skills/image/references/characters.md", "skills/image/references/creative-direction.md",
    "skills/image/references/dimensional.md", "skills/image/references/multi-panel.md",
    "skills/image/references/slides.md", "skills/image/references/storyboards.md",
    "skills/image/references/structural.md", "skills/image/references/vision-decomposer.md",
    "skills/visual-asset-critic/SKILL.md", "skills/visual-asset-critic/references/critique-rubric.md",
    "skills/visual-prompt-forge/references/consistency-locks.md",
    "skills/visual-prompt-forge/references/failure-modes.md",
    "skills/visual-prompt-forge/references/prompt-anatomy.md",
)


def main():
    dec = json.loads((AQUI / "decision_secciones.json").read_text(encoding="utf-8"))
    db = sqlite3.connect(f"file:{BASE}?mode=ro", uri=True)
    texto = dict(db.execute("SELECT id, texto FROM textos"))
    sec_de = {i: d for d in dec for i in d["ids"]}
    sec1344 = next(d for d in dec if d["n"] == 1344)
    assert sec1344["archivo"].endswith("one-shot-all-adapters/gpt-image.txt") and sec1344["estado"] == "dentro"
    leidos = [i for d in dec if d["estado"] == "dentro" for i in d["ids"]
              if MODELO.search(texto[i]) or d["n"] == 1344 or i in NOTA or d["archivo"] in SIN_DECLARACION]
    assert set(SALE) <= set(leidos) and set(NOTA) <= set(leidos) and not set(SALE) & set(NOTA)
    lineas, filas = [], []
    for i in leidos:
        d = sec_de[i]
        estado = "sale" if i in SALE else "entra"
        motivo = SALE.get(i) or NOTA.get(i, "")
        filas.append({"id": i, "seccion": d["n"], "archivo": d["archivo"], "estado": estado, "motivo": motivo})
        lineas += [f"### {i} | sec {d['n']} | {d['archivo']} | {estado.upper()}" + (f" | {motivo}" if motivo else ""),
                   texto[i], ""]
    mixtas = [d for d in dec if d["estado"] == "mixta"]
    assert {d["n"] for d in mixtas} == set(MIXTA), "cada sección mixta debe estar decidida"
    for d in mixtas:
        defecto, motivo_def, excep = MIXTA[d["n"]]
        assert set(excep) <= set(d["ids"]), f"excepción fuera de la sección {d['n']}"
        for i in d["ids"]:
            if i in excep:
                estado, motivo = excep[i].split(": ", 1)
            else:
                estado, motivo = defecto, motivo_def
            motivo = NOTA_MIXTA.get(i, motivo)
            filas.append({"id": i, "seccion": d["n"], "archivo": d["archivo"], "estado": estado, "motivo": motivo})
            lineas += [f"### {i} | sec {d['n']} | {d['archivo']} | MIXTA {estado.upper()}" + (f" | {motivo}" if motivo else ""),
                       texto[i], ""]
    (AQUI / "lectura_textos_con_modelo.txt").write_text("\n".join(lineas), encoding="utf-8")
    (AQUI / "decision_textos.json").write_text(json.dumps(filas, ensure_ascii=False, indent=0), encoding="utf-8")
    assert all(any(d["archivo"] == a for d in dec) for a in SIN_DECLARACION)
    # Universo de la prueba: textos de secciones «dentro» que no salen + textos de secciones mixtas que entran.
    sale = set(SALE) | {f["id"] for f in filas if f["estado"] == "sale"}
    universo = [i for d in dec if d["estado"] in ("dentro", "mixta") for i in d["ids"]
                if i not in sale and (d["estado"] == "dentro" or i in {f["id"] for f in filas if f["estado"] == "entra"})]
    (AQUI / "universo_prueba.json").write_text(json.dumps(universo, ensure_ascii=False, indent=0), encoding="utf-8")
    m = [f for f in filas if f["id"] in {i for d in mixtas for i in d["ids"]}]
    print("mixtas leídos", len(m), "entran", sum(f["estado"] == "entra" for f in m),
          "salen", sum(f["estado"] == "sale" for f in m))
    print("UNIVERSO", len(universo))
    print("leídos", len(leidos), "salen", len(SALE), "entran", len(leidos) - len(SALE), "con nota", len(NOTA))


if __name__ == "__main__":
    main()
