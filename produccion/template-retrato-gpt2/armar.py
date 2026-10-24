"""Template fijo de retrato para GPT Image 2, congelado de los prompts B1–B6 que Eric aprobó el 2026-10-24.

python3 -I armar.py briefs.json            → escribe PROMPTS.txt y sale con 1 si un prompt no pasa la validación

Lo que el agente escribe por caso son solo los campos del brief (escena, sujeto, luz, detalles, paleta…). Todo lo que
funcionó y no cambia entre casos lo pone este programa: el verbo, la estructura de cinco slots, la línea anti-IA,
«solo portrait», «looks like a real photo», la piel con poros, el tamaño. El validador comprueba cada regla en cada
prompt, así que no depende de que el agente las recuerde.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SLOTS = ["Scene", "Subject", "Important Details", "Use Case", "Constraints"]
# gpt-image.md:60–63 (2:3, 3:2, 1:1); 4:5 calculado dentro de gpt-image.md:53–56
TAMANOS = {"2:3": "1024x1536", "3:2": "1536x1024", "1:1": "1024x1024", "4:5": "1024x1280", "16:9": "2560x1440"}
# gpt-image.md:36–38 y prohibición de Eric (PILOTO_V5 §0.4)
PROHIBIDAS = ["stunning", "incredible", "epic", "gorgeous", "masterpiece", "photorealistic", "photoreal", "minimalist",
              "brutalist", "luxury", "beautiful", "handsome", "armani", "gucci", "prada", "nike", "adidas", "apple"]
REQUERIDOS = {  # texto fijo que todo prompt debe contener, con su fuente
    "Scene: Create a photograph": "golden-rules.md:6–8 dentro del slot (templates §1)",
    "natural skin texture and no AI rendering artifacts": "forge gpt-image.md:57, :90",
    "Solo portrait": "golden-rules.md:16",
    "looks like a real photo": "piloto INV-002400 (gpt-image.md:128–135)",
    "Real skin texture with visible pores": "prompt-framework.md:213",
}


def armar(b):
    escena = f"Create a photograph {b['escena']}"
    refs = "".join(r + "\n" for r in b.get("referencias", []))  # gpt-image.md:104–109: cada imagen con su rol
    detalles = (f"{b['luz']} {b['microdetalle']} {b['camara']}. Real skin texture with visible pores. Palette of "
                + ", ".join(f"{n} {h}" for n, h in b["paleta"][:-1]) + f" and {b['paleta'][-1][0]} {b['paleta'][-1][1]}.")
    restr = (f"Solo portrait of {b['pronombre']} alone{(', ' + b['restriccion_extra']) if b.get('restriccion_extra') else ''}"
             f", with natural skin texture and no AI rendering artifacts; the frame stays free of {b['libre_de']}.")
    slots = {"Scene": escena, "Subject": b["sujeto"], "Important Details": detalles,
             "Use Case": f"{b['uso']}, looks like a real photo", "Constraints": restr}
    return refs + "\n".join(f"{s}: {slots[s]}" for s in SLOTS)


def tamano(b):
    """Tamaño fijo por ratio, o uno declarado que cumpla gpt-image.md:53–57 (lados <3840, múltiplos de 16, ≤3:1,
    655 360–8 294 400 px) sin pasar el límite fiable de 2560 px (gpt-image.md:57)."""
    if "tamano" not in b:
        return TAMANOS.get(b["ratio"])
    w, h = (int(x) for x in b["tamano"].split("x"))
    ok = (max(w, h) <= 2560 and w % 16 == 0 and h % 16 == 0 and max(w, h) / min(w, h) <= 3
          and 655360 <= w * h <= 8294400)
    return b["tamano"] if ok else None


def validar(b, prompt):
    f = []
    # DECISIONES.md:20 y taxonomía F15 persona (L1064): rostro T1 antes que cuerpo T2. Un rostro de menos del 20 %
    # del cuadro (F22) no se resuelve en una génesis: primero el maestro de rostro, después el cuerpo con referencia.
    if b.get("rostro_menor_20") is None:
        f.append("declara rostro_menor_20 (F22) true o false")
    elif b["rostro_menor_20"] and b.get("operacion", "genesis") == "genesis":
        f.append("rostro <20% en génesis: haz primero el maestro de rostro y el cuerpo con referencia (DECISIONES.md:20)")
    if b.get("operacion") == "ancla_referencia" and not b.get("referencias"):
        f.append("ancla con referencia sin «Image N: rol» (gpt-image.md:104–109)")
    if tamano(b) is None:
        f.append("tamaño fuera de los límites (gpt-image.md:53–57)")
    for txt, fuente in REQUERIDOS.items():
        if txt.lower() not in prompt.lower():
            f.append(f"falta «{txt}» ({fuente})")
    if re.findall(r"^([A-Za-z ]+):", prompt, flags=re.M) != SLOTS:  # «Image 1:» no cuenta: lleva dígito
        f.append("los cinco slots no están en orden (gpt-image.md:9–15)")
    for p in PROHIBIDAS:
        if re.search(rf"\b{p}\b", prompt.lower()):
            f.append(f"palabra prohibida o marca: {p} (gpt-image.md:36–38)")
    if not re.search(r"#[0-9A-Fa-f]{6}", prompt):
        f.append("paleta sin hex (golden-rules.md:36)")
    if not re.search(r"\bfrom (camera (left|right)|above|behind|the [a-z ]+(window|lamp|lights?))|overhead|backlight",
                     b["luz"], flags=re.I):
        f.append("la luz no declara fuente o dirección (creative-direction.md:7)")
    if not re.search(r"\d+mm feel", b["camara"]):
        f.append("cámara sin «Nmm feel» (prompt-framework.md:44)")
    if len(b.get("elementos", [])) > 5 or not b.get("elementos"):
        f.append("declara de 1 a 5 elementos distintos de escena (forge gpt-image.md:88)")
    n = len(prompt.split())
    if n > 300:
        f.append(f"{n} palabras > 300 (templates §6)")
    return f, n


def main():
    briefs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out, mal = ["Model: gpt-image-2 · Quality: high · copiar solo el texto entre ====", ""], 0
    for b in briefs:
        p = armar(b)
        fallas, n = validar(b, p)
        estado = "OK" if not fallas else "RECHAZADO: " + "; ".join(fallas)
        mal += bool(fallas)
        print(f"{b['id']}: {n} palabras · {estado}")
        out += [f"{b['id']} · Size: {tamano(b) or '?'}", "====", p, "====", ""]
    (Path(sys.argv[1]).parent / "PROMPTS.txt").write_text("\n".join(out), encoding="utf-8")
    sys.exit(1 if mal else 0)


if __name__ == "__main__":
    main()
