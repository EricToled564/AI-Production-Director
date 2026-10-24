"""Corrida de punta a punta con los briefs B1–B5 de PILOTO_V5 §5 y las 61 aplicaciones aprobadas del piloto gpt-image.md.

python3 -I correr.py        → escribe prompts.md y traza.json junto a este archivo e imprime tiempos

Paso 1 (valores de faceta por brief) y paso 3 (redacción de los cinco slots) los escribió el agente; están en
casos.json como datos. Este programa hace lo determinista: selección por condición, parámetros, validación y
ensamblado. Solo selecciona entre las reglas de gpt-image.md: es el único archivo clasificado y aprobado.
"""
import importlib.util
import json
import re
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
PILOTO = RAIZ / "taller/catalogo/v2/piloto_gpt-image/clasificacion.py"
SLOTS = ["Scene", "Subject", "Important Details", "Use Case", "Constraints"]
# INV-002343, INV-002344, INV-002345 (gpt-image.md:36–38) y la prohibición de Eric de «photorealistic» (PILOTO_V5 §0.4)
PROHIBIDAS = ["stunning", "incredible", "epic", "gorgeous", "masterpiece", "photorealistic", "photoreal", "minimalist",
              "brutalist", "luxury", "apple"]
# INV-002361..2364 (gpt-image.md:60–63): tamaños de la fuente por ratio
TAMANOS = {"2:3": (1024, 1536), "3:2": (1536, 1024), "1:1": (1024, 1024)}


def cargar_piloto():
    spec = importlib.util.spec_from_file_location("piloto", PILOTO)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def aplica(a, facetas, paso):
    """Condición del piloto: F29 debe incluir el modelo; cada faceta de r exige al menos un valor común (TODAS de ALGUNA)."""
    if "GPT Image 2" not in a["f29"] or paso not in a["f02"]:
        return False
    return all(set(v) & set(facetas.get(f, [])) for f, v in a["r"].items())


def tamano(ratio):
    """Tamaño de la fuente si existe; si no, el menor múltiplo de 16 con lado corto 1024 que cumple 002355–002358."""
    if ratio in TAMANOS:
        return TAMANOS[ratio], "INV-002361..2364"
    w, h = (int(x) for x in ratio.split(":"))
    corto = 1024
    largo = round(corto * max(w, h) / min(w, h) / 16) * 16
    return ((corto, largo) if h > w else (largo, corto)), "calculado con INV-002355..2358"


def validar(prompt, slots, ancho, alto):
    fallas = []
    etiquetas = re.findall(r"^([A-Za-z ]+):", prompt, flags=re.M)
    if etiquetas != SLOTS:  # INV-002334, INV-002335, INV-002397
        fallas.append(f"slots {etiquetas} ≠ {SLOTS}")
    if not slots["Constraints"].strip():  # INV-002336
        fallas.append("Constraints vacío")
    bajo = prompt.lower()
    for p in PROHIBIDAS:  # INV-002340, INV-002343..2345, PILOTO_V5 §0.4
        if re.search(rf"\b{p}\b", bajo):
            fallas.append(f"palabra prohibida: {p}")
    if max(ancho, alto) >= 3840:  # INV-002355
        fallas.append("lado ≥ 3840")
    if ancho % 16 or alto % 16:  # INV-002356
        fallas.append("lado no múltiplo de 16")
    if max(ancho, alto) / min(ancho, alto) > 3:  # INV-002357
        fallas.append("ratio > 3:1")
    if not 655360 <= ancho * alto <= 8294400:  # INV-002358
        fallas.append("píxeles fuera de rango")
    if ancho > 2560 or alto > 2560:  # INV-002359, recomendación
        fallas.append("aviso: sobre el límite fiable 2560×1440")
    palabras = len(prompt.split())
    if palabras > 300:  # techo editorial GPT 2 (templates §6)
        fallas.append(f"aviso: {palabras} palabras > 300")
    return fallas, palabras


def main():
    t0 = time.perf_counter()
    m = cargar_piloto()
    casos = json.loads((AQUI / "casos.json").read_text(encoding="utf-8"))
    t_carga = time.perf_counter() - t0
    salida, traza = ["# Prompts GPT Image 2 — briefs B1–B5 (PILOTO_V5 §5)", ""], []
    for c in casos:
        t1 = time.perf_counter()
        sel = [a for a in m.APLICACIONES if aplica(a, c["facetas"], c["paso"])]
        (ancho, alto), origen_tam = tamano(c["facetas"]["F06"][0])
        prompt = "\n".join(f"{s}: {c['slots'][s]}" for s in SLOTS)
        fallas, palabras = validar(prompt, c["slots"], ancho, alto)
        t_caso = time.perf_counter() - t1
        bloqueantes = [f for f in fallas if not f.startswith("aviso")]
        traza.append({"brief": c["id"], "facetas": c["facetas"], "inferencias": c["inferencias"],
                      "seleccionadas": [{"id": a["id"], "uso": a["uso"], "accion": a["accion"], "destino": a["destino"],
                                         "valor": a["valor"]} for a in sel],
                      "tamano": [ancho, alto], "origen_tamano": origen_tam, "validacion": fallas or ["sin fallas"],
                      "palabras": palabras, "ms_seleccion_validacion": round(t_caso * 1000, 2)})
        salida += [f"## {c['id']} — {c['brief']}", "",
                   f"Uso: {c['uso']} · Formato {c['facetas']['F06'][0]}", "", "```text",
                   "Model: gpt-image-2 (OpenAI API o fal.ai openai/gpt-image-2)",
                   "Quality: high",
                   f"Size: {ancho}x{alto}", "", "Prompt:", prompt, "```", "",
                   f"Validación: {'; '.join(fallas) if fallas else 'sin fallas'} · {palabras} palabras · "
                   f"{len(sel)} reglas del piloto seleccionadas", "",
                   "Inferencias mías, para tu aprobación:", ""] + [f"- {i}" for i in c["inferencias"]] + [""]
        if bloqueantes:
            raise SystemExit(f"{c['id']}: {bloqueantes}")
    (AQUI / "prompts.md").write_text("\n".join(salida), encoding="utf-8")
    (AQUI / "traza.json").write_text(json.dumps(traza, ensure_ascii=False, indent=1), encoding="utf-8")
    total = time.perf_counter() - t0
    print(f"carga del piloto {t_carga * 1000:.1f} ms · total determinista {total * 1000:.1f} ms")
    for t in traza:
        print(f"{t['brief']}: {len(t['seleccionadas'])} reglas · {t['palabras']} palabras · {t['tamano']} · "
              f"{t['validacion']} · {t['ms_seleccion_validacion']} ms")


if __name__ == "__main__":
    main()
