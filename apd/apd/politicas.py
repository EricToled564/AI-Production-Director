"""Decisiones del usuario tomadas durante la construcción de la app (no forman parte de los originales;
DECISIONES.md del repo no se modifica). Cada una con fecha y texto literal de la instrucción."""

LONGITUD = {
    "id": "U-2026-09-28-LONGITUD",
    "fecha": "2026-09-28",
    "instruccion": ("quiero que no hags la restrccion en elumero de plabras de lols prompts bloqueante sino mas bien spiracional "
                    "y que solo si excede al doble del numeor d epalaras establecido por el cidgo entonces si se bkliqueee u se regenere"),
    "regla": "La longitud es aspiracional: fuera del rango de la fuente sólo avisa. Bloquea y exige regenerar si supera 2× el máximo.",
    "factor_bloqueo": 2.0,
    "compatible_con": "DECISIONES.md #2 (el conteo de palabras nunca bloquea: advertencia con el presupuesto como referencia)",
}

MOTOR = {
    "id": "U-2026-09-28-MOTOR",
    "fecha": "2026-09-28",
    "instruccion": "Decisión 1: «5 slots GPT Image» — y después: «my decision stands for any brief»",
    "regla": "En todo brief manda la compilación por bloques en el formato documentado del modelo destino (5 slots en GPT Image); "
             "template_engine de SW30 no es obligatorio (CF-MOTOR-SW30 gana b).",
}

REROLL = {
    "id": "U-2026-09-28-REROLL",
    "fecha": "2026-09-28",
    "instruccion": "Decisión 2: «SW30: máximo 2» — y después: «my decision stands for any brief»",
    "regla": "En todo brief: máximo 2 intentos por método; a la 2ª falla, cambio de método con causa declarada (CF-REROLL-SW30 gana b).",
}

CAMBIO_QUIRURGICO = {
    "id": "U-2026-09-28-CAMBIO-QUIRURGICO",
    "fecha": "2026-09-28",
    "instruccion": ("si te digo cambiale la edad a la modelo no quiero que cierres el proceso desde el inicio; quiero que se "
                    "identifique quirúrgicamente qué parte del prompt tiene que cambiar y dejar el resto como está; sólo si el "
                    "cambio es muy dramático (en lugar de una mujer de 28 años un hombre de 65) hay que revisar la redacción del "
                    "prompt, pero no es necesario en ningún caso revisar desde el inicio; las preguntas de los niveles anteriores "
                    "no se tocan y quedan fijas"),
    "regla": ("Un cambio de campo recompila sólo los bloques afectados. Las decisiones de niveles anteriores (clasificación de "
              "las 1,398 reglas, conflictos, decisiones del director) quedan fijas: nunca se re-revisan desde el inicio. "
              "Cambio MENOR: la revisión semántica y la aprobación de redacción pasan al texto nuevo (con registro de qué "
              "bloque cambió); sólo un NO_CUMPLE abierto en el bloque cambiado vuelve a revisarse. Cambio DRAMÁTICO: se "
              "revisa la redacción sólo de las reglas de los bloques cambiados y se pide aprobar la redacción de nuevo. "
              "La auditoría determinista (gates, hash) siempre se repite: es mecánica y no reabre decisiones."),
    "dramatico_si": "cambia el sexo o el origen, la edad cambia de franja (<30, 30–49, ≥50) o en 15 años o más, "
                    "o un bloque se reescribe en más de la mitad de sus palabras",
}


def _franja(edad):
    try:
        e = int(edad)
    except (TypeError, ValueError):
        return None
    return 0 if e < 30 else 1 if e < 50 else 2


def _palabras(t):
    import re
    return set(re.findall(r"[a-záéíóúñ0-9#]+", (t or "").lower()))


def clasificar_cambio(campos_antes: dict, campos_despues: dict, bloques_antes: dict, bloques_despues: dict) -> dict:
    """campos_*: valores de la entrega (comunes + propios); bloques_*: {id: texto}. Criterio de CAMBIO_QUIRURGICO."""
    cambiados = sorted(k for k in set(bloques_antes) | set(bloques_despues) if bloques_antes.get(k) != bloques_despues.get(k))
    motivos = []
    for k in ("sexo", "origen"):
        if campos_antes.get(k) != campos_despues.get(k):
            motivos.append(f"{k}: {campos_antes.get(k)} → {campos_despues.get(k)}")
    ea, ed = campos_antes.get("edad"), campos_despues.get("edad")
    if ea != ed and ea is not None and ed is not None:
        try:
            if _franja(ea) != _franja(ed) or abs(int(ea) - int(ed)) >= 15:
                motivos.append(f"edad: {ea} → {ed}")
        except (TypeError, ValueError):
            motivos.append(f"edad: {ea} → {ed}")
    for b in cambiados:
        pa, pd = _palabras(bloques_antes.get(b)), _palabras(bloques_despues.get(b))
        if pa and pd and len(pa & pd) / len(pa | pd) < 0.5:
            motivos.append(f"bloque {b} reescrito en más de la mitad")
    return {"tipo": "dramatico" if motivos else "menor", "motivos": motivos, "bloques": cambiados,
            "politica": CAMBIO_QUIRURGICO["id"]}
