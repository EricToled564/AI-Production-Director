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


APP = "App de ChatGPT para escritorio"  # interfaz de Eric: taller/demo/generar_desarrollo_spinning.py:47
INTERFACES = ("OpenAI API", "fal.ai", APP)


def acciones_de_dependencia(sel, caso):
    """Acción concreta de cada regla seleccionada que declara dependencia (TRM-0683 interfaz: «Diferencia de soporte
    entre API, aplicación o integración»; TRM-0684 versión: «Cambio de soporte entre versiones del mismo modelo»).

    La regla sigue seleccionada: la dependencia no veta la selección (taxonomía §Seleccionabilidad 2 y 5, §7.4). La
    versión ya la evalúa F29 (INV-002383 A3 solo vale para gpt-image-1.5/1 y nunca entra con GPT Image 2). Acciones:
    - interfaz ausente en el caso → dato faltante: T-BRIEF-IMG §3 exige entrada.modelo.interfaz siempre, y §2 «Ningún
      campo vacío o pregunta abierta habilita selección definitiva». La selección queda exploratoria.
    - INV-002374 (destino entrada.modelo.interfaz) → escribir en la traza el endpoint que da gpt-image.md:78 para esa
      interfaz.
    - INV-002380 (mask_image_url, gpt-image.md:90) → T-BRIEF-IMG §3 admite entrada.edicion.mascara «solo admitida por
      modelo/interfaz» y el corpus no dice qué interfaz la admite: preguntar al usuario; solo con «sí» se habilita.
    - INV-002383 A2 (versión: «no enviar input_fidelity a gpt-image-2») → validación bloqueante en validar().
    Devuelve (acciones, datos_faltantes)."""
    acciones, faltantes = [], []
    interfaz = caso.get("interfaz")
    if interfaz is not None and interfaz not in INTERFACES:
        raise SystemExit(f"{caso['id']}: interfaz «{interfaz}» fuera de {INTERFACES}")
    if interfaz is None:  # T-BRIEF-IMG L34: entrada.modelo.interfaz obligatoria «siempre», haya o no regla con dependencia
        faltantes.append("entrada.modelo.interfaz")
    for a in sel:
        dep = a.get("dependencia")
        if not dep:
            continue
        rid = a["id"] + a.get("sufijo", "")
        if dep == "Dependencia de interfaz" and interfaz is None:
            accion = "pedir al usuario la interfaz (OpenAI API o fal.ai) antes de la selección definitiva"
        elif rid == "INV-002374":
            accion = ("traza: endpoint «openai/gpt-image-2/edit»" if interfaz == "fal.ai"
                      else "traza: sin endpoint; la app no expone parámetros, tamaño y quality quedan como referencia "
                           "(taller/demo/PRUEBA_SPINNING_prompt_exportado.md:242)" if interfaz == APP
                      else "traza: endpoint images.edit de la API de OpenAI (developers.openai.com, referencia de images.edit)")
        elif rid == "INV-002380":
            if caso.get("mascara_admitida") is None:
                faltantes.append("confirmación de que la interfaz admite mask_image_url")
                accion = "preguntar al usuario si su interfaz admite mask_image_url; sin «sí» no se ofrece máscara"
            else:
                param = "mask (PNG con alfa, mismas dimensiones que la imagen)" if interfaz == "OpenAI API" else "mask_image_url"
                accion = (f"habilitar entrada.edicion.mascara con el parámetro {param} (opcional, ediciones puntuales)"
                          if caso["mascara_admitida"] else "no ofrecer máscara: la interfaz no la admite")
        elif rid == "INV-002383A2":
            accion = "validación bloqueante: el prompt y los parámetros no llevan input_fidelity"
        else:
            raise SystemExit(f"{rid}: dependencia «{dep}» sin acción concreta definida en correr.py")
        acciones.append({"id": rid, "dependencia": dep, "accion_concreta": accion})
    return acciones, faltantes


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
    if "input_fidelity" in bajo:  # INV-002383 A2: en gpt-image-2 la alta fidelidad es por defecto (gpt-image.md:96)
        fallas.append("parámetro prohibido en gpt-image-2: input_fidelity")
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
        acciones, faltantes = acciones_de_dependencia(sel, c)
        if "tamano" in c:  # tamaño propio del caso; validar() aplica los límites INV-002355..2359
            ancho, alto = (int(x) for x in c["tamano"].split("x"))
            w, h = (int(x) for x in c["facetas"]["F06"][0].split(":"))
            if ancho * h != alto * w:
                raise SystemExit(f"{c['id']}: tamaño {c['tamano']} no es {w}:{h}")
            origen_tam = c["origen_tamano"]
        else:
            (ancho, alto), origen_tam = tamano(c["facetas"]["F06"][0])
        # «Image N: rol» antes de los slots (gpt-image.md:104–109); el regex de slots no las cuenta porque llevan dígito
        prompt = "\n".join(c.get("referencias", []) + [f"{s}: {c['slots'][s]}" for s in SLOTS])
        fallas, palabras = validar(prompt, c["slots"], ancho, alto)
        if c.get("interfaz") == APP and c["facetas"]["F06"][0] not in prompt:
            # la app no fija el tamaño: el formato va escrito en el texto (PRUEBA_SPINNING_prompt_exportado.md:242)
            fallas.append(f"falta el formato {c['facetas']['F06'][0]} en el texto del prompt")
        t_caso = time.perf_counter() - t1
        bloqueantes = [f for f in fallas if not f.startswith("aviso")]
        traza.append({"brief": c["id"], "facetas": c["facetas"], "inferencias": c["inferencias"],
                      "seleccionadas": [{"id": a["id"], "uso": a["uso"], "accion": a["accion"], "destino": a["destino"],
                                         "valor": a["valor"]} for a in sel],
                      "acciones_dependencia": acciones,
                      "datos_faltantes": faltantes,
                      "seleccion": "exploratoria" if faltantes else "definitiva",
                      "tamano": [ancho, alto], "origen_tamano": origen_tam, "validacion": fallas or ["sin fallas"],
                      "palabras": palabras, "ms_seleccion_validacion": round(t_caso * 1000, 2)})
        salida += [f"## {c['id']} — {c['brief']}", "",
                   f"Uso: {c['uso']} · Formato {c['facetas']['F06'][0]}", "", "```text",
                   f"Model: gpt-image-2 ({c.get('interfaz') or 'interfaz sin definir'})",
                   "Quality: high" + (" (referencia: la app no lo fija)" if c.get("interfaz") == APP else ""),
                   f"Size: {ancho}x{alto}" + (" (referencia: la app no lo fija; el formato va en el texto)" if c.get("interfaz") == APP else ""), "", "Prompt:", prompt, "```", "",
                   f"Validación: {'; '.join(fallas) if fallas else 'sin fallas'} · {palabras} palabras · "
                   f"{len(sel)} reglas del piloto seleccionadas", ""]
        if acciones or faltantes:
            salida += [f"Selección {'exploratoria' if faltantes else 'definitiva'}. Datos que faltan: "
                       f"{', '.join(faltantes) or 'ninguno'}.", ""]
            salida += [f"- {x['id']} ({x['dependencia']}): {x['accion_concreta']}" for x in acciones] + [""]
        salida += ["Reglas aplicadas por lectura directa (sin clasificar todavía):", ""]
        salida += [f"- {f}" for f in c.get("fuentes_aplicadas", [])] + ["", "Inferencias mías, para tu aprobación:", ""]
        salida += [f"- {i}" for i in c["inferencias"]] + [""]
        if bloqueantes:
            raise SystemExit(f"{c['id']}: {bloqueantes}")
    (AQUI / "prompts.md").write_text("\n".join(salida), encoding="utf-8")
    (AQUI / "traza.json").write_text(json.dumps(traza, ensure_ascii=False, indent=1), encoding="utf-8")
    total = time.perf_counter() - t0
    print(f"carga del piloto {t_carga * 1000:.1f} ms · total determinista {total * 1000:.1f} ms")
    for t in traza:
        print(f"{t['brief']}: {len(t['seleccionadas'])} reglas · selección {t['seleccion']} "
              f"(faltan: {t['datos_faltantes'] or 'nada'}) · "
              f"{t['palabras']} palabras · {t['tamano']} · "
              f"{t['validacion']} · {t['ms_seleccion_validacion']} ms")


if __name__ == "__main__":
    main()
