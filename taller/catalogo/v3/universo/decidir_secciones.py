"""decidir_secciones.py: decisión por sección leída (número de sección de secciones.txt).

    python3 -I decidir_secciones.py   → decision_secciones.json y DECISION_SECCIONES.md

Estados:
- dentro: la sección trata de crear una imagen fija y aplica a GPT Image 2 o a cualquier modelo.
- otro_modelo: crea imagen pero solo para otro modelo (Nano Banana, Flux, Midjourney, Ideogram, Seedream).
- fuera: otra etapa o contenido que no regula la creación de imágenes (video, guion, storyboard, marca, vista HTML,
  código, licencia, paquete de entrega).
- mixta: el encabezado no basta; se decide leyendo cada texto (por ejemplo, vocabulario de cámara dentro del skill
  de video, o una tabla que compara modelos).
Toda sección no listada en DENTRO, OTRO o MIXTA queda fuera; la causa sale del documento.
"""
import collections
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def r(a, b):
    return set(range(a, b + 1))


DENTRO = (
    r(1, 10)                      # flujo-anclas: todo el documento es la etapa 5, anclas de imagen
    | {14, 15, 17}                # flujo-spot: niveles 3 (génesis) y 4 (subflujo atómico)
    | {28}                        # ai-production-director › Etapa 5 — Anchor Images
    | r(195, 206)                 # image/SKILL.md
    | r(207, 275)                 # characters, creative-direction, dimensional, editing, golden-rules, gpt-image
    | {276, 278, 280, 281}        # models.md: título, «GPT Image 2 выигрывает», «обе одинаково хороши»
    | r(284, 299)                 # multi-panel
    | r(315, 319) | {321}         # character-design (sin «Nano Banana version»)
    | r(323, 328)                 # ecommerce
    | r(330, 335)                 # fashion-editorial
    | r(337, 342)                 # food-beverage
    | r(344, 347)                 # portrait-cinema (5-slot)
    | r(351, 352) | r(354, 357)   # poster-illustration
    | r(359, 363) | {365}         # ui-social
    | r(367, 455)                 # prompt-framework, slides, storyboards, structural, text-rendering, vision-decomposer
    | r(1093, 1114)               # visual-asset-critic/SKILL.md: crítica del render
    | r(1137, 1146)               # critique-rubric
    | r(1205, 1229) | r(1231, 1232)  # visual-prompt-forge/SKILL.md
    | r(1246, 1255)               # adaptador GPT Image
    | {1344}                      # ejemplo gpt-image.txt
    | r(1350, 1377)               # consistency-locks, failure-modes, prompt-anatomy
)
OTRO = (
    {279}                         # models.md › Nano Banana выигрывает в
    | r(300, 314)                 # nano-banana.md
    | {320, 322, 329, 336, 343, 350, 353, 358, 364, 366}  # «Nano Banana version:»
    | r(1235, 1245) | r(1265, 1275) | r(1286, 1306) | r(1316, 1326)  # adaptadores Flux, Ideogram, Midjourney, NB, Seedream
    | {1343, 1345, 1347, 1348, 1349}  # ejemplos Flux, Ideogram, Midjourney, NB, Seedream
)
MIXTA = (
    {11, 12, 13, 16}              # flujo-spot: inicio, nivel 0→1, nivel 2 (filas E0–E7), nivel 3b (incluye clips)
    | {34, 35, 37}                # ai-production-director 6.1 vocabulario, 6.2 sintaxis, 6.4 forge↔smixs
    | {277, 282, 283}             # models.md: TL;DR, diferencias de sintaxis, costo (comparan los dos modelos)
    | {348, 349}                  # portrait-cinema: patrones recomendados para NB2 / NBP
    | r(676, 682)                 # storyboard-architect/shot-grammar: encuadre, ángulo, DOF, luz, sujeto
    | {667}                       # on-screen-text › composición que reserva espacio
    | r(804, 812)                 # video/animatic-keyframes: stills de keyframe y su prompt de imagen
    | {815, 817, 818, 819, 820, 821}  # camera-lighting-vocabulary: encuadre, lente, luz, color
    | {867, 870, 871}             # fixes-and-skeletons: manos, caras de IA, gemelos
    | {957, 962, 963, 964, 967}   # race-and-speed: velocidad en un solo cuadro, luz y color, anti-fake
    | r(1183, 1185)               # visual-media › fundamentos de fotografía
    | {1230, 1337, 1338, 1339, 1340, 1341, 1342}  # forge: tabla de adaptadores y README del ejemplo
    | {1233}                      # _capabilities.json (solo la entrada de GPT Image)
)


def main():
    secs = json.loads((AQUI / "secciones.json").read_text(encoding="utf-8"))
    assert not (DENTRO & OTRO or DENTRO & MIXTA or OTRO & MIXTA), "una sección en dos estados"
    assert max(DENTRO | OTRO | MIXTA) <= len(secs)
    out, cuenta = [], collections.Counter()
    for n, s in enumerate(secs, 1):
        e = "dentro" if n in DENTRO else "otro_modelo" if n in OTRO else "mixta" if n in MIXTA else "fuera"
        out.append({"n": n, "archivo": s["archivo"], "seccion": s["seccion"], "estado": e, "ids": s["ids"]})
        cuenta[e] += len(s["ids"])
    assert sum(cuenta.values()) == 13005
    (AQUI / "decision_secciones.json").write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    md = ["# Decisión por sección — universo de creación de imágenes con GPT Image 2", "",
          "Cada una de las 1,408 secciones (documento + ruta de encabezados, `secciones.txt`) leída y decidida en "
          "`decidir_secciones.py`.", "", "| Estado | Secciones | Textos |", "|---|---:|---:|"]
    ns = collections.Counter(d["estado"] for d in out)
    for e in ("dentro", "mixta", "otro_modelo", "fuera"):
        md.append(f"| {e} | {ns[e]} | {cuenta[e]:,} |")
    md += ["", "## Secciones mixtas (se deciden leyendo cada texto)", "", "| # | Documento | Sección | Textos |", "|---:|---|---|---:|"]
    md += [f"| {d['n']} | `{d['archivo']}` | {d['seccion']} | {len(d['ids'])} |" for d in out if d["estado"] == "mixta"]
    (AQUI / "DECISION_SECCIONES.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(dict(ns), dict(cuenta))


if __name__ == "__main__":
    main()
