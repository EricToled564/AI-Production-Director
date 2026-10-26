"""clasificacion_misma_posicion.py: clasificación aumentada de los textos del universo que están en la misma posición
que INV-002054, es decir, colgados directamente del título principal de su documento (o antes de él), sin ninguna
subsección.

    python3 -I clasificacion_misma_posicion.py   → CLASIFICACION_MISMA_POSICION.md

Clasificación aumentada = la ruta de encabezados del documento, más la cadena de documentos que lo cargan hasta arriba
(con la línea exacta que lo carga) y el modelo que declara cada nivel. Cada cadena se leyó en los originales de
apd/originales/; las líneas citadas son de esos archivos.
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent

DIRECTOR_IMAGE = ("ai-production-director/SKILL.md:34 (§1 Mapa de sub-skills) «image (smixs) | 5 · Anchors | Sintaxis "
                  "por modelo de imagen (Nano Banana, GPT Image 2)» y :94 (§3 Etapa 5 — Anchor Images)")
DIRECTOR_FORGE = ("ai-production-director/SKILL.md:35 (§1) «visual-prompt-forge | 5–6 · Prompts» y :94 (Etapa 5: forge "
                  "genera borradores, image es la autoridad de sintaxis final)")
DIRECTOR_CRITIC = "ai-production-director/SKILL.md:36 (§1) «visual-asset-critic | 5 · QA» y :94 (Etapa 5)"
IMAGE_SKILL = "image/SKILL.md:5 (frontmatter) «Image prompting skill for Nano Banana (NBP/NB2) and GPT Image 2»"
PASO = "image/SKILL.md:28 «Mandatory reading order» › "
FORGE_SKILL = ("visual-prompt-forge/SKILL.md:3 (frontmatter) «stills (Midjourney, Flux, Ideogram, GPT Image, Nano "
               "Banana, Seedream) and motion video»")
CRITIC_SKILL = "visual-asset-critic/SKILL.md:3 (frontmatter): no nombra modelo; critica cualquier imagen generada"

# documento → (cadena de carga de arriba abajo, modelo que resulta para el documento)
CARGA = {
    "skills/image/SKILL.md": ([DIRECTOR_IMAGE, IMAGE_SKILL], "los dos: Nano Banana y GPT Image 2"),
    "skills/image/references/models.md": ([DIRECTOR_IMAGE, IMAGE_SKILL, PASO + ":32 Step 1 «always read first → models.md» "
        "(«Decide: Nano Banana (NB2 or NBP) or GPT Image 2», :34)"], "los dos; sirve para elegir modelo"),
    "skills/image/references/gpt-image.md": ([DIRECTOR_IMAGE, IMAGE_SKILL, PASO + ":38 Step 2 «read one model file» › "
        ":43 «GPT Image 2 → gpt-image.md»"], "solo GPT Image 2"),
    "skills/image/references/golden-rules.md": ([DIRECTOR_IMAGE, IMAGE_SKILL, PASO + ":48 Step 3 «always read after the "
        "model file» («Universal rules that apply to both models», :50)"], "los dos"),
    "skills/image/references/creative-direction.md": ([DIRECTOR_IMAGE, IMAGE_SKILL, PASO + ":74 Step 5 «read for "
        "production language»"], "el modelo elegido; el paso no restringe"),
    "skills/image/references/prompt-framework.md": ([DIRECTOR_IMAGE, IMAGE_SKILL, PASO + ":78 Step 6 «read if "
        "structuring a complex prompt»"], "el modelo elegido; el paso no restringe"),
}
PASO4 = PASO + ":52 Step 4 «task-shaped reading (load only what matches the request)» › "
for doc, linea, cuando in [
        ("text-rendering.md", 56, "Text in image, infographic, diagram, multilingual rendering"),
        ("editing.md", 57, "Edit existing image"),
        ("characters.md", 58, "Character continuity across multiple images / panels"),
        ("slides.md", 59, "Presentation slides"),
        ("storyboards.md", 60, "Sequential narrative (storyboard, comic, panel sequence)"),
        ("structural.md", 61, "Sketch → final, wireframes, structural input"),
        ("dimensional.md", 62, "2D → 3D, floor plans, isometric"),
        ("vision-decomposer.md", 63, "Vision analysis / image-to-prompt / style transfer from a reference image"),
        ("multi-panel.md", 64, "Multi-panel compositions"),
        ("patterns/ecommerce.md", 66, "E-commerce product shots"),
        ("patterns/fashion-editorial.md", 67, "Fashion editorial campaigns"),
        ("patterns/food-beverage.md", 68, "Food & beverage advertising"),
        ("patterns/portrait-cinema.md", 69, "Cinematic portraits"),
        ("patterns/poster-illustration.md", 70, "Posters & illustration"),
        ("patterns/character-design.md", 71, "Character design"),
        ("patterns/ui-social.md", 72, "UI mockups & social media formats")]:
    CARGA["skills/image/references/" + doc] = (
        [DIRECTOR_IMAGE, IMAGE_SKILL, PASO4 + f":{linea} «{cuando}»"], "el modelo elegido; el Paso 4 no restringe")
for doc in ("patterns/ecommerce.md", "patterns/fashion-editorial.md", "patterns/food-beverage.md",
            "patterns/portrait-cinema.md", "patterns/poster-illustration.md", "patterns/character-design.md",
            "patterns/ui-social.md"):
    c, _ = CARGA["skills/image/references/" + doc]
    CARGA["skills/image/references/" + doc] = (c, "GPT Image 2 por defecto («Default model: GPT Image 2 (5-slot "
                                                   "format) unless noted», línea 3 del propio documento)")
for doc in ("text-rendering.md", "editing.md"):
    c, _ = CARGA["skills/image/references/" + doc]
    CARGA["skills/image/references/" + doc] = (c, "los dos, con diferencias por modelo (línea 3 del propio documento)")
CARGA.update({
    "skills/visual-asset-critic/SKILL.md": ([DIRECTOR_CRITIC, CRITIC_SKILL], "cualquier modelo de imagen"),
    "skills/visual-asset-critic/references/critique-rubric.md": ([DIRECTOR_CRITIC, CRITIC_SKILL,
        "visual-asset-critic/SKILL.md:79 «Workflow › Step 2. Critique by layer» :81 «Read references/critique-rubric.md "
        "for the full rubric» y :244 «Reference»"], "cualquier modelo de imagen"),
    "skills/visual-prompt-forge/SKILL.md": ([DIRECTOR_FORGE, FORGE_SKILL], "varios generadores, GPT Image incluido"),
    "skills/visual-prompt-forge/adapters/gpt-image.md": ([DIRECTOR_FORGE, FORGE_SKILL,
        "visual-prompt-forge/SKILL.md:85 «Workflow › Step 2. Pick the adapters» :87 «For each target generator, read the "
        "matching adapter file» :92 «adapters/gpt-image.md»; :327 tabla «GPT Image 1.5 / 2»"], "GPT Image 1.5 y 2"),
    "skills/visual-prompt-forge/references/prompt-anatomy.md": ([DIRECTOR_FORGE, FORGE_SKILL,
        "visual-prompt-forge/SKILL.md:51 «The five-layer prompt anatomy» y :312 «Reference files» :314"],
        "cualquier generador"),
    "skills/visual-prompt-forge/references/consistency-locks.md": ([DIRECTOR_FORGE, FORGE_SKILL,
        "visual-prompt-forge/SKILL.md:312 «Reference files» :315"], "cualquier generador; cada lock nombra los suyos"),
    "skills/visual-prompt-forge/references/failure-modes.md": ([DIRECTOR_FORGE, FORGE_SKILL,
        "visual-prompt-forge/SKILL.md:312 «Reference files» :316"], "cualquier generador; cada arreglo nombra los suyos"),
    "skills/visual-prompt-forge/examples/one-shot-all-adapters/README.md": ([DIRECTOR_FORGE, FORGE_SKILL,
        "visual-prompt-forge/SKILL.md:369 «Examples» :371 «one-shot-all-adapters … Use it to calibrate output quality»"],
        "todos los adaptadores; su salida GPT Image es 1.5 (README.md:44)"),
})

# Dictamen de cada texto, leído uno por uno. Sin entrada: título, separador o línea de autor sin contenido normativo.
DICTAMEN = {
    "INV-001998": "declara los dos modelos (NB y GPT Image 2) y excluye video, 3D y audio",
    "INV-002000": "la salida es modelo + quality/size/ratio + prompt; vale para GPT Image 2",
    "INV-002001": "las reglas viven en los archivos de referencia; obliga a leerlos",
    "INV-002008": "obliga al orden de lectura antes de escribir cualquier prompt",
    "INV-002043": "introduce la cabecera de salida",
    "INV-002044": "cabecera: Model, Quality (solo gpt-image-2), Size/Ratio, Prompt, Notes; vale para GPT Image 2",
    "INV-002045": "lista preserve obligatoria en ediciones con gpt-image-2",
    "INV-002046": "bloque Change / Preserve / Constraints de edición",
    "INV-002049": "preferir sintaxis del modelo: 5-slot para GPT Image",
    "INV-002050": "el elogio vago daña a GPT Image 2; la parte de lente numérica es solo de Nano Banana y no aplica a "
                  "GPT Image 2 (que admite «50mm feel» como look, prompt-framework.md:42)",
    "INV-002054": "CORREGIDO (correcciones.json): el original daba el desglose de NBP (14 = 6+5+3, nano-banana.md:64-66, "
                  ":144); ahora da la cifra de GPT Image 2 (16 con rol, alta fidelidad por defecto)",
    "INV-002085": "alcance del documento: luz, cámara, color y materialidad; sin cifra de modelo",
    "INV-002168": "alcance: conversiones 2D↔3D; sin cifra de modelo",
    "INV-002195": "el edit difiere por modelo; las dos líneas siguientes lo desglosan (la de NB, INV-002196, salió)",
    "INV-002197": "edición en GPT Image 2: Change / Preserve / Constraints, preserve en cada iteración",
    "INV-002198": "un edit por iteración, para cualquier modelo",
    "INV-002239": "declara el documento universal para los dos modelos",
    "INV-002332": "gpt-image-2 es el default; 1.5 y 1 solo migración; 1-mini presupuesto",
    "INV-002416": "el skill escribe para dos familias y el modelo cambia la estructura del prompt",
    "INV-002474": "una sola imagen con todos los paneles, a diferencia de storyboards.md",
    "INV-002475": "numerar y describir cada panel; sin cifra de modelo",
    "INV-002676": "plantillas con GPT Image 2 (5-slot) por defecto salvo nota",
    "INV-002719": "plantillas con GPT Image 2 (5-slot) por defecto salvo nota",
    "INV-002761": "plantillas con GPT Image 2 (5-slot) por defecto salvo nota",
    "INV-002802": "plantillas con GPT Image 2 (5-slot) por defecto salvo nota",
    "INV-002862": "plantillas con GPT Image 2 (5-slot) por defecto salvo nota",
    "INV-002903": "plantillas con GPT Image 2 (5-slot) por defecto salvo nota",
    "INV-002946": "plantillas con GPT Image 2 (5-slot) por defecto salvo nota",
    "INV-002989": "checklist universal para los dos modelos",
    "INV-002991": "enlace a gpt-image.md (5-slot, anti-slop, quality)",
    "INV-002992": "enlace a models.md para elegir modelo",
    "INV-003089": "alcance: diapositivas; sin cifra de modelo",
    "INV-003226": "alcance: secuencias y concept art; sin cifra de modelo",
    "INV-003256": "alcance: imágenes de entrada controlan la composición; sin cifra de modelo",
    "INV-003295": "universal para los dos modelos, con detalles de render distintos",
    "INV-003297": "texto en GPT Image 2: EXACT TEXT entre comillas o ALL CAPS, quality high para texto pequeño",
    "INV-003394": "cuándo usar el documento: análisis de imagen a prompt",
    "INV-003395": "rol de Vision Agent; sin cifra de modelo",
    "INV-003396": "dos pasos estrictos; el Paso 2 (INV-003433, con nota) pide keywords con comas, que choca con "
                  "adapters/gpt-image.md:86",
    "INV-009765": "crítica de cualquier imagen generada; no nombra modelo",
    "INV-009767": "rol de revisión editorial; sin cifra de modelo",
    "INV-009768": "la salida son arreglos concretos de prompt o de post",
    "INV-010314": "checklist por capas para revisar una imagen generada",
    "INV-011265": "GPT Image es uno de los generadores de imagen fija del skill",
    "INV-011267": "cada generador premia un estilo: párrafo para GPT Image",
    "INV-011268": "mismo shot, distinta sintaxis",
    "INV-011719": "manda _capabilities.json sobre el adaptador; la entrada GPT Image (_capabilities.json:54-69) da "
                  "300 palabras máximo, aspect_param size, sin style ref ni negative prompt",
    "INV-011720": "GPT Image: párrafos, razonamiento espacial explícito, texto preciso",
    "INV-012172": "ejemplo de calibración con 6 adaptadores de imagen y Kling; su salida GPT Image es 1.5 y salió "
                  "(sección 1344)",
    "INV-012218": "los generadores no tienen estado; sin locks hay deriva; sin cifra de modelo",
    "INV-012219": "técnicas vigentes en 2026; sin cifra de modelo",
    "INV-012278": "qué falla y qué se arregla en el prompt o en edición; sin cifra de modelo",
    "INV-012370": "cinco capas por prompt; sin cifra de modelo",
}


def main():
    filas = [json.loads(l) for l in (AQUI / "universo_prueba_textos.jsonl").read_text(encoding="utf-8").splitlines()]
    sel = [f for f in filas if f["archivo"].endswith((".md", ".md.tpl"))
           and (not f["encabezado"] or " › " not in f["encabezado"])]
    faltan = {f["archivo"] for f in sel} - set(CARGA)
    assert not faltan, f"documentos sin cadena de carga: {faltan}"
    assert set(DICTAMEN) <= {f["id"] for f in sel}
    md = ["# Clasificación aumentada — textos en la misma posición que INV-002054", "",
          f"{len(sel)} textos del universo cuelgan directamente del título principal de su documento (o están antes "
          "de él, en el frontmatter), sin subsección. Para cada documento: la cadena que lo carga, de arriba abajo, con "
          "la línea exacta, y el modelo que resulta. Para cada texto: su ruta y el dictamen de la lectura.", ""]
    por_doc = {}
    for f in sel:
        por_doc.setdefault(f["archivo"], []).append(f)
    for doc, textos in por_doc.items():
        cadena, modelo = CARGA[doc]
        md += [f"## `{doc}`", "", "Cadena de carga:", ""]
        md += [f"{n}. {paso}" for n, paso in enumerate(cadena, 1)]
        md += ["", f"Modelo que resulta: **{modelo}**", "", "| Id | Línea | Ruta aumentada | Texto | Dictamen |",
               "|---|---:|---|---|---|"]
        for f in textos:
            ruta = " › ".join(p.split(" (")[0].split(" «")[0] for p in cadena) + f" › {doc.split('/')[-1]}"
            ruta += f" › {f['encabezado']}" if f["encabezado"] else " › (frontmatter)"
            texto = f["texto"].replace("\n", " ").replace("|", "\\|")
            texto = texto if len(texto) <= 160 else texto[:157] + "…"
            dictamen = DICTAMEN.get(f["id"], "título, separador o autor; sin contenido normativo")
            md.append(f"| {f['id']} | {f['linea_inicial']} | {ruta} | {texto} | {dictamen} |")
        md.append("")
    (AQUI / "CLASIFICACION_MISMA_POSICION.md").write_text("\n".join(md), encoding="utf-8")
    print("textos", len(sel), "documentos", len(por_doc), "con dictamen", len(DICTAMEN))


if __name__ == "__main__":
    main()
