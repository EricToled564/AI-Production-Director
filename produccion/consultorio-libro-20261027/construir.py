"""construir.py: los tres prompts GPT Image 2 de la escena del consultorio (BRIEF.md), armados por sección.

    python3 -I produccion/consultorio-libro-20261027/construir.py            → escribe PROMPTS.txt; código 1 si algo falla
    python3 -I produccion/consultorio-libro-20261027/construir.py --probar   → casos que deben fallar

Cada paso se instancia con `herramientas/template_engine.py` (SW30 §Motor de plantillas: T5 para la edición, T3 para
la inserción del hombre, T4 para la de la mujer porque el cuadro queda con dos personas, RULES_MATRIX.md:13), se audita
con `herramientas/audit_gi2.py` (SW30 §Verificación mecánica, 15 columnas) y pasa los controles de `verificar()`, que
comprueban por código las reglas que el auditor no cubre. Los tres pasos salen de flujo-anclas.html:384 (2 personas sin
contacto: placa → A → B), de la regla crítica 1 de `produccion-visual-sw30/SKILL.md` («un sujeto por generación», sin
técnica de colocación probada para dos personas) y de la 7 («mundos por dos pasos»). Ver LECTURA_CORPUS.md.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI / "herramientas"))
from template_engine import block, build  # noqa: E402
from audit_gi2 import audit  # noqa: E402

META = {"model": "gpt-image-2", "quality": "high", "size_or_ratio": "1536x1024 (3:2)"}
TECHO_PALABRAS = 300  # SW30: el prompt ronda 250 palabras; un slot de 300+ compite consigo mismo
# armar.py:20 (gpt-image.md:36–38 y prohibición de Eric) más SW30 regla 2 (posición vaga)
PROHIBIDAS = ["stunning", "incredible", "epic", "gorgeous", "masterpiece", "photorealistic", "photoreal", "minimalist",
              "brutalist", "luxury", "beautiful", "handsome", "cinematic", "professional", "high quality"]
POSICION_VAGA = [r"\bleft half\b", r"\bright half\b", r"\bcent(?:re|er)\b", r"\bcentral\b", r"\bjust left of\b",
                 r"\bjust right of\b"]
NARRATIVA_EDITOR = [r"\bagain\b", r"\bhas become\b"]  # SW30 regla 3
MOVIMIENTO = [r"\bmoving\b", r"\bmoves\b", r"\bwalking\b", r"\bin motion\b"]  # SW30 regla 8
TONOS = "charcoal #36383B, black #121212, pearl grey #D8D6D0"

PASOS = {
 "paso1": dict(
  tipo="T5", refs=["Image 1: placa vacía del consultorio (la Image 7 del texto de Eric)",
                   "Image 2: libro negro de lino cerrado (Image 6)", "Image 3: placa aprobada de la doctora (Image 5)"],
  jobs=1,
  change=("Image 1 is the empty office to edit. Image 2 is the doctor's closed black linen book. Image 3 is the "
          "doctor's approved plate: use only her right hand and the white cuff of her coat. Replace the open book "
          "lying on the marble desk in Image 1 with the closed book of Image 2, at the same size and in the same "
          "place, with the doctor's right hand from Image 3 resting flat on its lower corner, covering the gold "
          "name: a slender woman's hand with five fingers, only the hand and the white cuff entering at the bottom "
          "edge of the frame."),
  preserve=("the office of Image 1 exactly: its walls, the abstract painting, the open doorway, the two empty grey "
            "chairs where they stand, the marble desk, the camera position, the framing and the soft cool morning "
            "window light."),
  constraints=("the hand and cuff are the only additions; a soft contact shadow where the hand meets the book and "
               "where the book meets the marble; natural unretouched skin with visible pores; fine film grain."),
  notes="Paso 1 de 3: prepara el mundo antes de insertar personas (SW30 regla 7)."),
 "paso2": dict(
  tipo="T3", personas=1, refs=["Image 1: resultado aprobado del paso 1", "Image 2: primer plano del rostro del hombre (Image 1)",
                   "Image 3: placa aprobada de cuerpo entero del hombre (Image 2)"],
  jobs=1,
  scene=("Scene: Create a photograph in the office of Image 1, seen from the doctor's seat. Keep the world of Image "
         "1 untouched: this place, its camera position, its soft cool morning window light, the closed book and the "
         "doctor's hand exactly as they are."),
  subject=("Subject: Image 2 is a close-up of the man's face: copy this exact face. Image 3 is his approved "
           "full-length plate: use only the person from Images 2 and 3, ignore their setting, and take only his "
           "hair, glasses and build from Image 3. He sits in the grey chair below the abstract painting, far behind "
           "the marble desk, in a charcoal #36383B unstructured wool-cashmere jacket worn open over a black #121212 "
           "merino crewneck."),
  anatomy=("Important Details: His shoulders are as wide as the chair back and his head sits level with the bottom "
           "edge of the painting, so the whole desk lies between him and the camera; the desk top sits at the "
           "height of his elbows and his whole chest and upper arms rise above it. Frozen instant: he leans "
           "slightly forward, listening to the doctor with a quiet closed-lip smile, his eyes raised along the "
           "doctor's white sleeve toward her face just beyond the right side of the frame, his gaze passing the "
           "camera on its right."),
  idlock="Keep facial features exactly the same as Image 2.",  # characters.md:14
  optics=("Five fingers on each hand; natural unretouched skin with visible pores; visible wool weave on the open "
          "jacket; deep focus, natural contrast, fine film grain."),
  usecase=("Use Case: editorial documentary photograph that looks like a real photo; key frame of a film in which "
           "a doctor closes a woman's book while a couple listens."),
  constraints=("Constraints: his face clean and sharp, eyes clear; he is the only person added; the chair before "
               "the open doorway stays empty."),
  notes="Paso 2 de 3: un sujeto por generación (SW30 regla 1)."),
 "paso3": dict(
  tipo="T4", personas=2, refs=["Image 1: resultado aprobado del paso 2", "Image 2: primer plano del rostro de la mujer (Image 3)",
                   "Image 3: placa aprobada de cuerpo entero de la mujer (Image 4)"],
  jobs=1,
  scene=("Scene: Create a photograph in the office of Image 1, seen from the doctor's seat. Keep the world of Image "
         "1 untouched: this place, its camera position, its soft cool morning window light, the seated man, the "
         "closed book and the doctor's hand exactly as they are."),
  subject=("Subject: Image 2 is a close-up of the woman's face: copy this exact face. Image 3 is her approved "
           "full-length plate: use only the person from Images 2 and 3, ignore their setting, and take only her "
           "hair, earrings and build from Image 3. She sits in the grey chair before the open doorway, far behind "
           "the marble desk, in a pearl grey #D8D6D0 knit polo with an open collar."),
  anatomy=("Important Details: Her shoulders are as wide as the chair back and her head sits level with the bottom "
           "edge of the painting, so the whole desk lies between her and the camera; the desk top sits at the "
           "height of her elbows and her whole chest and upper arms rise above it. Frozen mid-reach: she leans "
           "forward, her left arm extended across the desk, fingers slightly open to take the book, eyes on the "
           "book, a quiet closed-lip smile."),
  contact=("Her left hand stops halfway to the closed book and touches nothing; only the doctor's hand rests on "
           "the book. The man and the woman do not touch."),
  idlock="Keep facial features exactly the same as Image 2.",  # characters.md:14
  optics=("Five fingers on each hand; natural unretouched skin with visible pores; deep focus, natural contrast, "
          "fine film grain."),
  usecase=("Use Case: editorial documentary photograph that looks like a real photo; key frame of a film in which "
           "a doctor closes a woman's book while a couple listens."),
  constraints=("Constraints: her face clean and sharp, eyes clear; only the couple and the doctor's hand in "
               "frame."),
  notes="Paso 3 de 3: un sujeto por generación (SW30 regla 1); T4 porque el cuadro queda con dos personas."),
}


def armar(d):
    if d["tipo"] == "T5":
        return build("T5", metadata=META, references=d["refs"], change=d["change"], preserve=d["preserve"],
                     constraints=d["constraints"], notes=d["notes"])
    extra = {"contact": block("contact", d["contact"])} if d["tipo"] == "T4" else {}
    return build(d["tipo"], metadata=META, references=d["refs"], scene=d["scene"], subject=d["subject"],
                 anatomy=block("anatomy", d["anatomy"]), idlock=block("idlock", d["idlock"]), **extra,
                 optics=block("optics_deep", d["optics"]),
                 usecase=d["usecase"], constraints=d["constraints"], notes=d["notes"])


def verificar(nombre, d, p):
    """Reglas que audit_gi2 no comprueba; cada una cita su fuente."""
    f, txt, low = [], p.prompt, p.prompt.lower()
    slots = ["Change", "Preserve", "Constraints"] if d["tipo"] == "T5" else \
        ["Scene", "Subject", "Important Details", "Use Case", "Constraints"]
    if re.findall(r"^(Scene|Subject|Important Details|Use Case|Constraints|Change|Preserve):", txt, re.M) != slots:
        f.append("slots GPT fuera de orden (gpt-image.md:9–15, :86–90; verificar_templates.py:61–65)")
    if not txt.startswith(slots[0] + ":"):
        f.append("el prompt no abre con su primer slot")
    for w in PROHIBIDAS:
        if re.search(rf"\b{w}\b", low):
            f.append(f"palabra prohibida: {w} (gpt-image.md:36–38; CLAUDE.md)")
    for pat in POSICION_VAGA:
        if re.search(pat, low):
            f.append(f"posición vaga «{pat}» (SW30 regla 2)")
    for pat in MOVIMIENTO:
        if re.search(pat, low):
            f.append(f"movimiento en un still «{pat}» (SW30 regla 8)")
    if "…" in txt or "..." in txt:
        f.append("elipsis en el prompt (verificar_templates.py:59)")
    usadas = {int(x) for t in re.findall(r"Images? (\d)(?: and (\d))?", txt) for x in t if x}
    if usadas and max(usadas) > len(d["refs"]):
        f.append(f"cita Image {max(usadas)} con {len(d['refs'])} referencias adjuntas (SW30 regla 4)")
    if d.get("personas", 0) >= 2 and d["tipo"] != "T4":
        f.append("cuadro con dos personas armado como " + d["tipo"] + "; debe ser T4 (RULES_MATRIX.md:13)")
    if not re.search(r"#[0-9A-Fa-f]{6}", txt) and d["tipo"] != "T5":
        f.append("colores nuevos sin hex (golden-rules.md, SKILL.md:50)")
    if d["tipo"] == "T5":
        if not re.search(r"\b(Replace|Add|Remove|Move|Swap)\b", txt):
            f.append("edición sin verbo operativo (SW30 regla 3)")
        for pat in NARRATIVA_EDITOR:
            if re.search(pat, low):
                f.append(f"narrativa en edición «{pat}» (SW30 regla 3)")
    else:
        for frase in ("use only the person from images 2 and 3, ignore their setting", "keep the world of image 1 untouched"):
            if frase not in low:
                f.append(f"falta «{frase}» (SW30 regla 7)")
        if "frozen" not in low:
            f.append("falta el instante congelado (SW30 regla 8)")
        if "create a photograph" not in low:
            f.append("falta el verbo dentro del slot Scene (golden-rules.md §1)")
    art = dict(p.to_dict(), audit_context={"max_prompt_words": TECHO_PALABRAS, "jobs": d["jobs"],
                                           "identity_required": d["tipo"] != "T5", "hands_required": True,
                                           "gaze_required": d["tipo"] != "T5", "colour_required": d["tipo"] != "T5"})
    cols = audit(art)
    f += [f"audit_gi2 {c.name}: {c.detail}" for c in cols if c.status == "FAIL"]
    return f, cols


def correr(pasos):
    fallas, salida = [], ["Model: gpt-image-2 · Quality: high · Size: 1536x1024 (3:2) · un chat nuevo por paso", ""]
    for nombre, d in pasos.items():
        try:
            p = armar(d)
        except Exception as e:  # TemplateViolation u otro error del motor
            fallas.append(f"{nombre}: {e}")
            continue
        f, cols = verificar(nombre, d, p)
        fallas += [f"{nombre}: {x}" for x in f]
        n = len(p.prompt.split())
        salida += [f"{nombre} · {n} palabras · referencias: " + " | ".join(p.references), "====", p.prompt, "====",
                   "audit_gi2: " + " · ".join(f"{c.name}={c.status}" for c in cols), ""]
    return fallas, salida


def main():
    if "--probar" in sys.argv:
        return probar()
    fallas, salida = correr(PASOS)
    for f in fallas:
        print("  FALLA", f)
    if not fallas:
        (AQUI / "PROMPTS.txt").write_text("\n".join(salida), encoding="utf-8")
    print(f"{len(PASOS)} pasos · " + ("OK" if not fallas else f"{len(fallas)} fallas"))
    return 1 if fallas else 0


def probar():
    """Cada caso cambia un dato y debe producir la falla nombrada; el lote tal cual debe pasar."""
    import copy
    casos = [("lote tal cual", None, None),
             ("palabra prohibida", ("paso2", "optics", "deep focus", "stunning deep focus"), "palabra prohibida: stunning"),
             ("posición vaga", ("paso3", "anatomy", "Frozen mid-reach", "In the centre, frozen mid-reach"), "posición vaga"),
             ("dos personas como T3", ("paso3", "tipo", None, "T3"), "debe ser T4"),
             ("sin frase de inserción", ("paso2", "subject", "use only the person from Images 2 and 3, ignore their "
                                         "setting, and ", ""), "SW30 regla 7"),
             ("imagen no adjunta", ("paso3", "scene", "office of Image 1,", "office of Image 4,"), "SW30 regla 4"),
             ("dos trabajos", ("paso2", "jobs", None, 2), "single_job"),
             ("sección obligatoria vacía", ("paso3", "usecase", None, ""), "missing required section"),
             ("edición con narrativa", ("paso1", "change", "Replace the open book", "Replace again the open book"),
              "narrativa en edición")]
    malos = 0
    for nombre, cambio, esperado in casos:
        pasos = copy.deepcopy(PASOS)
        if cambio:
            paso, campo, viejo, nuevo = cambio
            pasos[paso][campo] = nuevo if viejo is None else pasos[paso][campo].replace(viejo, nuevo)
        fallas, _ = correr(pasos)
        ok = (not fallas) if esperado is None else any(esperado in x for x in fallas)
        malos += not ok
        print(("  ok    " if ok else "  FALLA ") + nombre + ("" if ok else f": {fallas}"))
    print("todo como se esperaba" if not malos else f"{malos} resultados inesperados")
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())
