"""Conflictos conocidos entre reglas y su resolución con la autoridad documentada.

Cada entrada cita ambos lados (id del registro o archivo:línea cuando la fuente no
quedó en el registro) y la autoridad que la resuelve. Si la autoridad hace depender
la resolución de un dato del brief que falta, el estado es CONFLICTO y la entrega se
bloquea hasta que el usuario decida. Nada se fusiona: cada lado conserva su texto.
"""

from __future__ import annotations

CATALOGO = [
    {
        "id": "CF-VOCAB-61",
        "descripcion": "Cierre 'cinematic 1080p, synchronized audio' (ai-video-storyboard) vs vocabulario prohibido.",
        "a": ["f556f97c9939"], "b": ["097929817bc7"],
        "autoridad": "ai-production-director/SKILL.md §6.1 (línea 123): 'gana siempre … anula explícitamente la regla de ai-video-storyboard'; conflict-policies v3.4 POLICY_VIDEO_FINAL_VOCAB_001",
        "resolver": lambda p: ("a", "política §6.1: el vocabulario prohibido gana siempre"),
    },
    {
        "id": "CF-SINTAXIS-62",
        "descripcion": "Prompts model-agnostic (ai-video-storyboard) vs sintaxis del modelo destino (smixs).",
        "a": [], "b": ["60f13533c38e"],
        "autoridad": "ai-production-director/SKILL.md §6.2 (línea 126, no extraída al registro por falta de marcador): 'model-agnostic SOLO en artefactos intermedios … Todo prompt FINAL se escribe en la sintaxis del modelo destino'",
        "resolver": lambda p: ("a", "§6.2: esta entrega es un prompt FINAL; model-agnostic sólo en intermedios"),
    },
    {
        "id": "CF-LUZ-T1",
        "descripcion": "SW30 T1: luz dura rasante sin relleno obligatoria en rostros vs flujo-anclas D1 'Character ref: luz pareja, sin sombras duras que el modelo confunda con rasgos'.",
        "a": ["d5b415caa2cd", "98e61771053d"], "b": [],
        "b_fuente": "flujo-anclas.html Paso 0 'Roles posibles de un ancla' (Character ref) y D7 'Comercial: clean, pareja'",
        "autoridad": "flujo-anclas.html D7: 'Rostros documentales: luz dura rasante … Comercial: clean, pareja' — la resolución depende de D4 tratamiento",
        "aplica_si": lambda p: bool(p["casos"] & {"T1", "T2"}),
        "resolver": lambda p: (("a", "D4 = documental: SW30 T1 luz dura (flujo-anclas D7)") if p.get("d4") == "documental"
                               else ("b", f"D4 = {p['d4']}: luz pareja de character ref (flujo-anclas D1/D7)") if p.get("d4")
                               else None),
    },
    {
        "id": "CF-TRIX-COLOR",
        "descripcion": "SW30 usecase_doc 'fotografía documental Kodak Tri-X' (stock blanco y negro) vs brief a color.",
        "a": ["5a5348b20c81"], "b": [],
        "b_fuente": "brief: color",
        "autoridad": "flujo-anclas.html Paso 4 (Tri-X sólo en la fila Documental). Con D4 = documental y brief a color no hay autoridad: "
                     "requiere decisión. Antecedente: produccion/vivaldi-invierno/05-genesis-anclas.md corrección 1 (Tri-X produjo B/N no pedido).",
        "aplica_si": lambda p: bool(p["casos"] & {"T1"}),
        "resolver": lambda p: (("b", f"D4 = {p['d4']}: Kodak Tri-X es el stock de la fila Documental; la fila de {p['d4']} no lo usa "
                                     "(flujo-anclas.html Paso 4, tabla de tratamientos)") if p.get("d4") and p.get("d4") != "documental"
                               else ("a", "el brief pide blanco y negro: Tri-X es coherente") if p.get("color") == "bn"
                               else ("b", "decisión registrada: color natural; Tri-X se sustituye") if p.get("decision_trix") == "b"
                               else ("a", "decisión registrada: se conserva Tri-X") if p.get("decision_trix") == "a"
                               else None),
    },
    {
        "id": "CF-MOTOR-SW30",
        "descripcion": "SW30: todo prompt visual se INSTANCIA con production-package/template_engine.py build(tipo) (T1 = bloques "
                       "light_hard, skin_doc, usecase_doc, clean_doc) vs compilación por bloques de la app en los 5 slots de gpt-image.md "
                       "con luz pareja de character ref (flujo-anclas D1/D7, kling.md:220, regimenes/09:45).",
        "a": ["7ba769efe2d7", "c0bc3ce2b122", "ed3f4a2ab62f", "f75cfcf75330", "4a2eeac6c89d"], "b": [],
        "b_fuente": "image/references/gpt-image.md:5-15 (5 slots) · flujo-anclas.html D1/D7 · DECISIONES.md #2 ('los templates de SW30 "
                    "y los prompts de 5 slots de GPT Image pasan': ambos formatos existen, no dice cuál manda)",
        "autoridad": "apd/politicas.py U-2026-09-28-MOTOR (Eric, 2026-09-28, vale para todo brief): manda la compilación por bloques en el "
                     "formato documentado del modelo destino (5 slots en GPT Image); template_engine de SW30 no es obligatorio",
        "aplica_si": lambda p: p["medio"] != "VIDEO",
        "resolver": lambda p: ("b", "U-2026-09-28-MOTOR (director, todo brief): compilación por bloques en el formato del modelo destino"),
    },
    {
        "id": "CF-REROLL-SW30",
        "descripcion": "visual-asset-critic presupuesta 2–3 re-rolls ante un fallo técnico vs SW30 'Máximo 2 intentos por método … "
                       "Nunca tercera vuelta de lo mismo'.",
        "a": ["1e898f2c0308", "7eac9caa0ac8", "87d7e03eed3d"], "b": ["f9fee85351f3"],
        "autoridad": "apd/politicas.py U-2026-09-28-REROLL (Eric, 2026-09-28, vale para todo brief): máximo 2 intentos por método; "
                     "a la 2ª falla, cambio de método con causa declarada",
        "resolver": lambda p: ("b", "U-2026-09-28-REROLL (director, todo brief): máximo 2 intentos por método (SW30)"),
    },
    {
        "id": "CF-IDENTIDAD-ROL",
        "descripcion": "Bloque de identidad completo en cada prompt (U7) vs no re-describir lo que la imagen ya fija (Kling §10, SW30 R16).",
        "a": ["c1d814f8c059"], "b": ["36686df1386d", "2dddf6f48ba3"],
        "autoridad": "DECISIONES.md #3 (Eric, 2026-09-25): por rol de la referencia — FF/LF: no re-describir; referencia de personaje sin start frame o @img/Elements: bloque completo y verbatim",
        "aplica_si": lambda p: p["medio"] == "VIDEO",
        "resolver": lambda p: (("b", "rol frame inicial/final: no re-describir (DECISIONES #3)") if p["roles"] & {"frame_inicial", "frame_final"}
                               else ("a", "sin start frame: bloque de identidad completo y verbatim (DECISIONES #3)")),
    },
]


def evaluar(perfil: dict, estados: dict[str, str], conflicto_de: dict[str, str] | None = None) -> list[dict]:
    """Devuelve los conflictos activos para el perfil. `estados` = decisión actual por id; `conflicto_de` = id → conflicto
    que ya la suprimió (para seguir mostrando los conflictos resueltos, no sólo los abiertos)."""
    out = []
    cd = conflicto_de or {}
    for c in CATALOGO:
        if c.get("aplica_si") and not c["aplica_si"](perfil):
            continue
        vivo = lambda i: estados.get(i) in ("APLICA", "CONDICIONAL", "CONFLICTO") or cd.get(i) == c["id"]
        a = [i for i in c["a"] if vivo(i)]
        b = [i for i in c["b"] if vivo(i)]
        lado_externo = bool(c.get("b_fuente")) or not c["a"]
        if not (a or (not c["a"])) or not (b or lado_externo):
            continue
        auto = c["resolver"](perfil)
        manual = (perfil.get("decisiones") or {}).get(c["id"])
        # la decisión registrada del director manda y queda visible junto a lo que habría dicho la autoridad automática
        res = (manual, f"decisión registrada del director: gana {manual}"
                       + (f" (la autoridad automática decía {auto[0]}: {auto[1]})" if auto else "")) if manual in ("a", "b") else auto
        out.append({"id": c["id"], "descripcion": c["descripcion"], "a": c["a"], "b": c["b"],
                    "origen_resolucion": "director" if manual in ("a", "b") else ("autoridad" if auto else None),
                    "b_fuente": c.get("b_fuente"), "autoridad": c["autoridad"],
                    "resuelto": res is not None, "gana": res[0] if res else None,
                    "razon": res[1] if res else "falta un dato del brief o una decisión del usuario para aplicar la autoridad"})
    return out


def ids_conocidos() -> set[str]:
    s = set()
    for c in CATALOGO:
        s |= set(c["a"]) | set(c["b"])
    return s
