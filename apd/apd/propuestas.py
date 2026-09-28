"""Propuestas para campos abiertos cuando no hay modelo, o como punto de partida.

Dos clases, y la app las etiqueta distinto:
  * derivadas de fuente: el valor sale literalmente de una tabla de flujo o skill
    (se cita). Ej.: D9 eye-level para maestros de identidad (flujo-anclas).
  * creativas de la app: casting de ejemplo, determinista y editable. NO vienen de
    ninguna regla; existen para que el flujo sin modelo no quede vacío y para la
    prueba de regresión. Se muestran como 'propuesta creativa (app)'.
Ninguna propuesta queda LOCKED sin que el usuario la acepte (o un test la acepte).
"""

from __future__ import annotations

from . import spec as S

LUZ_POR_TRATAMIENTO = {
    "documental": ("Hard grazing light with no fill; surface microtexture casts visible local shadow. No softbox flattening",
                   "produccion-visual-sw30 template T1 light_hard (texto de template_engine.py, SOURCE_RECONSTRUCTED) · flujo-anclas D7"),
    "comercial": ("soft even frontal key light with gentle fill and soft, gradual shadow transitions across the face",
                  "flujo-anclas.html D1 'Character ref: luz pareja, sin sombras duras que el modelo confunda con rasgos' · D7 'Comercial: clean, pareja'"),
    "narrativo": ("one motivated key light from camera-left dominating the face, the far side falling into shadow, a single specular highlight",
                  "flujo-anclas.html Paso 4 fila Narrativo: 'Una fuente motivada domina … un specular duro'"),
}
CAMARA_T1 = ("85mm portrait lens feel from about 1.5 metres, shallow depth of field",
             "flujo-anclas D6 (lente 85 entre los valores de la tarjeta) — la elección de 85 es propuesta de la app; "
             "la altura de cámara la fija el ángulo (eye-level, storyboard-architect/references/shot-grammar.md:29) en Subject")
CAMARA_T1_NB = ("portrait lens perspective with gentle background separation, shallow depth of field",
                "nano-banana.md:22-24: sin números de lente, usar descripción ('shallow depth of field')")
FOCO_T1 = ("both eyes in sharp focus", "propuesta de la app (retrato de identidad: la mirada es lo que se juzga)")

CASTING_EJEMPLO = {
    "woman": [
        {"edad": 23, "origen": "of Nigerian Yoruba descent",
         "personalidad": "steady direct gaze, lips closed, chin slightly lowered",
         "rasgos": "oval face with high cheekbones, deep brown skin, dark brown eyes, close-cropped natural black hair, a small scar through the left eyebrow, small gold stud earrings, black cotton crew-neck top",
         "instrumento": "first violin"},
        {"edad": 27, "origen": "of Korean descent",
         "personalidad": "soft half-smile, relaxed shoulders, head tilted slightly",
         "rasgos": "round face, light warm-beige skin, dark brown eyes behind round tortoiseshell glasses, shoulder-length straight black hair tucked behind one ear, light freckles across the nose, one ear set slightly higher than the other, charcoal wool knit sweater",
         "instrumento": "viola"},
        {"edad": 25, "origen": "of Mexican mestiza descent",
         "personalidad": "one eyebrow slightly raised, a hint of a grin at one corner of the mouth",
         "rasgos": "heart-shaped face, medium olive-brown skin, hazel eyes, long dark wavy hair gathered in a loose low bun, a small mole above the upper lip, silver hoop earrings, deep green silk blouse collar",
         "instrumento": "cello"},
    ],
    "man": [
        {"edad": 28, "origen": "of Punjabi Indian descent",
         "personalidad": "calm neutral mouth, shoulders squared, chin level",
         "rasgos": "square jaw, medium brown skin, dark brown eyes, short neat black beard, thick eyebrows, short side-parted black hair, a nose bridge with a slight bend to the right, navy cotton shirt collar",
         "instrumento": "second violin"},
        {"edad": 22, "origen": "of Norwegian descent",
         "personalidad": "broad toothy smile, crinkled eyes, head cocked back a little",
         "rasgos": "long narrow face, fair pinkish skin, pale blue eyes, tousled short ash-blond hair, light stubble, a slightly crooked front tooth, grey cotton henley collar",
         "instrumento": "double bass"},
    ],
}


def proponer(spec: dict) -> list[dict]:
    """Lista de propuestas {ruta, valor, clase, fuente}. No modifica la spec."""
    c = spec["comunes"]
    out = []
    casos = c["tipo_tarea"]["valor"] or []
    modelo = c["modelo"]["valor"]
    # Ancla: D9 (ángulo) por tipo de acción y número de sujetos — flujo-anclas.html tabla "D9 por tipo de acción".
    # Las filas que el propio flujo marca como inferencia se proponen como INFERENCIA A PRUEBA, no como regla.
    d9 = c.get("tarjeta_d9")
    if d9 and d9["estado"] == "OPEN":
        from .flujos import D9_POR_ACCION
        accion = (c.get("tarjeta_d2") or {}).get("valor") or (c.get("accion") or {}).get("valor")
        d3v = str((c.get("tarjeta_d3") or {}).get("valor") or (c.get("d3") or {}).get("valor") or "1")
        sujetos = {"ensamble": 3, "multitud": 99}.get(d3v) or (int(d3v[0]) if d3v[:1].isdigit() else 1)
        fila = "F_multitud" if d3v == "multitud" else "ensamble" if sujetos >= 3 else accion
        if fila in D9_POR_ACCION:
            x = D9_POR_ACCION[fila]
            out.append({"ruta": "comunes.tarjeta_d9", "valor": x["defecto"],
                        "clase": "inferencia_a_prueba" if x["inferencia"] else "fuente",
                        "fuente": f"flujo-anclas.html 'D9 por tipo de acción' fila {fila}"
                                  f"{' (≥3 sujetos → técnica de ensamble)' if fila == 'ensamble' else ''}: '{x['texto']}' — {x['porque']} ({x['fuente']})"
                                  + (" · el flujo la marca como inferencia: A PRUEBA, no regla canónica" if x["inferencia"] else "")})
    trat = c["tratamiento"]["valor"]
    if c["modelo"]["estado"] == "OPEN" and "T1" in casos:
        out.append({"ruta": "comunes.modelo", "valor": "gpt-image-2", "clase": "fuente",
                    "fuente": "flujo-anclas D8: 'Rostro humano, maestro … GPT Image 2 quality high para piel e identidad'; "
                              "image/references/patterns/portrait-cinema.md: 'Default model: GPT Image 2 (5-slot format)'"})
    if c["calidad"]["estado"] == "OPEN":
        if (modelo or "gpt-image-2") == "gpt-image-2":
            out.append({"ruta": "comunes.calidad", "valor": "high", "clase": "fuente",
                        "fuente": "gpt-image.md:47 '`quality: high` | … портреты, identity-sensitive edits'"})
        else:
            out.append({"ruta": "comunes.calidad", "valor": "2K", "clase": "fuente",
                        "fuente": "nano-banana.md:117 '2K | Финальный отбор'"})
    if c["formato"]["estado"] == "OPEN" and "T1" in casos:
        out.append({"ruta": "comunes.formato", "valor": "2:3", "clase": "creativa",
                    "fuente": "propuesta de la app: vertical de retrato; gpt-image.md:61 lista 'Portrait 1024×1536'"})
    if c["medio"]["valor"] == "video" and (modelo or "") == "kling" and not (c.get("negativos") or {}).get("valor"):
        out.append({"ruta": "comunes.negativos", "valor": "distorted hands, extra fingers, subtitles, logos, cartoon physics, random camera drift",
                    "clase": "fuente", "fuente": "video/references/fixes-and-skeletons.md:222 'For Kling field. Rewrite as positive entities.'"})
    if c["color"]["estado"] == "OPEN" and c["medio"]["valor"] == "imagen":
        out.append({"ruta": "comunes.color", "valor": "natural colour", "clase": "creativa",
                    "fuente": "propuesta de la app: casting a color; resuelve la ambigüedad Tri-X (ver CF-TRIX-COLOR)"})
    if c["tratamiento"]["estado"] == "OPEN" and "T1" in casos:
        out.append({"ruta": "comunes.tratamiento", "valor": "comercial", "clase": "creativa",
                    "fuente": "propuesta de la app: un retrato de casting es referencia de personaje (flujo-anclas D1 Character ref); "
                              "la alternativa 'documental' activa el template SW30 T1 (luz dura, Tri-X)"})
        trat = trat or "comercial"
    if c["luz"]["estado"] == "OPEN" and trat in LUZ_POR_TRATAMIENTO:
        v, f = LUZ_POR_TRATAMIENTO[trat]
        out.append({"ruta": "comunes.luz", "valor": v, "clase": "fuente", "fuente": f})
    if c["camara"]["estado"] == "OPEN" and "T1" in casos:
        v, f = CAMARA_T1_NB if (modelo or "").startswith("nano-banana") else CAMARA_T1
        out.append({"ruta": "comunes.camara", "valor": v, "clase": "creativa" if "propuesta" in f else "fuente", "fuente": f})
    if c["foco"]["estado"] == "OPEN" and "T1" in casos:
        out.append({"ruta": "comunes.foco", "valor": FOCO_T1[0], "clase": "creativa", "fuente": FOCO_T1[1]})
    if c["restricciones"]["estado"] == "OPEN" and "T5" not in casos and c["medio"]["valor"] == "imagen" and (modelo or "").startswith("nano-banana"):
        out.append({"ruta": "comunes.restricciones", "valor": "A single real photograph with no text, watermark or logo",
                    "clase": "fuente", "fuente": "nano-banana.md:11-25 prosa natural · golden-rules R2 positive framing · aurora: términos de estilo "
                                                  "no fotorreal fuera del MAIN (no hay campo negativo en Nano Banana)"})
    if c["restricciones"]["estado"] == "OPEN" and "T5" not in casos and c["medio"]["valor"] == "imagen" and not (modelo or "").startswith("nano-banana"):
        out.append({"ruta": "comunes.restricciones",
                    "valor": "one person only, no text, no watermark, no logo, no retouched plastic skin, not an illustration or 3D render",
                    "clase": "fuente",
                    "fuente": "gpt-image.md:13 'Constraints: what must NOT change/appear (no watermarks, … no extra text)' · "
                              "flujo-anclas 'Lo que un ancla nunca lleva' · golden-rules ✅ 'solo portrait'"})
    if c["sujeto"]["estado"] == "OPEN" and "T1" in casos:
        out.append({"ruta": "comunes.sujeto", "valor": None, "clase": "fuente", "estado": "NO_APLICA",
                    "motivo": "el sujeto de cada retrato se define por entrega (sexo, edad, origen)"})
    if c["identidad"]["estado"] == "OPEN" and "T1" in casos:
        out.append({"ruta": "comunes.identidad", "valor": None, "clase": "fuente", "estado": "NO_APLICA",
                    "motivo": "la identidad es por entrega (rasgos); génesis sin referencia: se escribe completa en texto"})
    if (c.get("preservar") or {}).get("estado") == "OPEN" or ("T5" in casos and not (c.get("preservar") or {}).get("valor")):
        out.append({"ruta": "comunes.preservar",
                    "valor": "Keep the face, identity, pose, lighting, framing, background, geometry, text and layout exactly as they are.",
                    "clase": "fuente", "fuente": "image/references/gpt-image.md:82 (lista Preserve literal) escrita como oración para cumplir "
                                                "golden-rules R4 'Natural Language' (gate_image R4 bloquea la lista suelta)"})
    if "T5" in casos and c["restricciones"]["estado"] == "OPEN":
        out.append({"ruta": "comunes.restricciones", "valor": "no extra objects, no redesign, no drift", "clase": "fuente",
                    "fuente": "image/references/gpt-image.md:83 'Constraints: no extra objects, no redesign, no drift'"})
    usados = {"woman": 0, "man": 0}
    for e in spec["entregas"]:
        sexo = (e["campos"].get("sexo") or {}).get("valor")
        if sexo not in CASTING_EJEMPLO:
            continue
        lista = CASTING_EJEMPLO[sexo]
        base = lista[usados[sexo] % len(lista)]
        usados[sexo] += 1
        for k in ("edad", "origen", "personalidad", "rasgos", "instrumento"):
            f = e["campos"].get(k)
            if f and f["estado"] == "OPEN":
                v = base[k]
                if k == "edad" and f.get("rango"):
                    lo, hi = f["rango"]
                    v = min(max(v, lo), hi)
                out.append({"ruta": f"{e['id']}.{k}", "valor": v, "clase": "creativa",
                            "fuente": "propuesta creativa determinista de la app (no es regla); editable"})
    return out


def aceptar(spec: dict, props: list[dict], autor="usuario") -> tuple[dict, list[str]]:
    cambios = []
    for p in props:
        c = {"ruta": p["ruta"], "valor": p.get("valor"), "origen": f"propuesta_{p['clase']}_aceptada",
             "fuente": p.get("fuente", "")}
        if p.get("estado"):
            c["estado"] = p["estado"]
            c["motivo"] = p.get("motivo", "")
        cambios.append(c)
    return S.aplicar_cambios(spec, cambios, autor)
