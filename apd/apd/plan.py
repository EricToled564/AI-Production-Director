"""Plan visual: recorrido, etapas que aplican y que no (con razón), dependencias,
entregables, subprocesos (tareas de la base) y aprobaciones que el recorrido exige.

Fuentes: app/build_app.py (ETAPAS con `ok`, TRACKS), rules_v3.py (TAREAS de
flujo-spot.html Nivel 2), flujo-anclas.html (A0–A12) y ai-production-director/SKILL.md
(descripción: "NO aplicar a piezas sueltas — un solo prompt (usar image/video)").
"""

from __future__ import annotations

from . import flujos as FL

CITA_SUELTAS = ("ai-production-director/SKILL.md (description): NO aplicar a piezas sueltas — un solo prompt "
                "(usar image/video), un storyboard aislado (usar storyboard-architect)")

# Subprocesos por recorrido de pieza suelta. Motivo citado por cada uno.
TAREAS_SUELTAS = {
    ("IMAGEN", "genesis"): [
        ("PROMPT_IMAGEN", "etapa suelta de build_app.py para un brief de una sola imagen"),
        ("E5.2", "génesis sin referencias (flujo-spot Nivel 4: 'Génesis sin referencias, paso a paso')"),
        ("E6.5", "lints mecánicos antes de entregar (flujo-spot Nivel 4 'Lints mecánicos'; flujo-anclas A7 'aurora caso 1 génesis')"),
        ("E6.6", "micro-gate de 3 líneas antes de entregar cualquier prompt visual (produccion-visual-sw30 MICRO-GATE)"),
    ],
    ("IMAGEN", "con_referencia"): [
        ("PROMPT_IMAGEN", "etapa suelta de build_app.py"),
        ("E5.3", "maestros derivados con referencia (flujo-spot E5.3)"),
        ("E5.4", "cuadros con referencias (flujo-spot E5.4)"),
        ("E6.5", "lints mecánicos"), ("E6.6", "micro-gate"),
    ],
    ("IMAGEN", "edicion"): [
        ("PROMPT_IMAGEN", "etapa suelta de build_app.py"),
        ("E5.5", "edición quirúrgica (flujo-spot E5.5)"), ("E6.5", "lints mecánicos"), ("E6.6", "micro-gate"),
    ],
    ("ANCLA", None): [
        ("E5.1", "plan de anchors y tarjeta D1–D9 (flujo-anclas A0–A2)"),
        ("E5.2", "génesis de lo que el ancla necesita y no existe (flujo-anclas A2)"),
        ("E5.4", "cuadro/keyframe con referencias canonizadas (flujo-anclas A3–A6)"),
        ("E6.5", "lints (flujo-anclas A7)"), ("E6.6", "micro-gate (flujo-anclas A8)"),
    ],
    ("CLIP", None): [
        ("PROMPT_VIDEO", "etapa suelta de build_app.py para un brief de un solo clip"),
        ("E6.1", "motion draft (flujo-spot E6.1)"), ("E6.2", "reescritura a sintaxis del modelo (E6.2)"),
        ("E6.3", "bloques de continuidad (E6.3)"), ("E6.4", "dramaturgy check + 3 detalles (E6.4)"),
        ("E6.5", "linter determinista (E6.5)"), ("E6.6", "micro-gate y entrega (E6.6)"),
    ],
}
POSTERIORES = [("E5.7", "crítica por capas del render (evaluación visual, después de generar)"),
               ("E5.8", "revisión selectiva tras la crítica"),
               ("E5.9", "canonizar con hash el render aprobado")]


def _etapa(cl: str) -> dict:
    return next(e for e in FL.etapas() if e["clave"] == cl)


def construir(spec: dict, aprobaciones: dict | None = None) -> dict:
    aprobaciones = aprobaciones or {}
    rec = spec["recorrido"]
    r = rec["recorrido"]
    etapas = []
    tareas = []
    gates = []
    if r == "SPOT":
        track = rec.get("track")
        activas = FL.ETAPAS_POR_TRACK.get(track or "", [])
        for cl in ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"]:
            e = _etapa(cl)
            aplica = cl in activas
            razon = ""
            if not track:
                razon = "track pendiente: el brief no fija duración/marca"
                aplica = None
            elif not aplica:
                razon = f"track {track}: {FL.NOTA_TRACK[track]}"
            elif cl == "E0" and not spec["comunes"].get("marca", {}).get("valor"):
                razon = "E0 solo si hay marca o cliente (build_app ETAPAS.cond); confirmar si hay marca"
            etapas.append({"clave": cl, "nombre": e["nombre"], "aplica": aplica, "razon": razon,
                           "entra": e["entra"], "sale": e["sale"], "gate": e["gate"],
                           "requiere_ok": bool(e["ok"]) and cl in FL.GATES_OK,
                           "depende_de": [d for d in FL.DEPENDENCIAS[cl] if d in activas],
                           "aprobada": aprobaciones.get(cl)})
            if aplica:
                tareas += [(t["codigo"], f"subproceso de {cl} (flujo-spot Nivel 2)") for t in FL.tareas() if t["etapa"] == cl]
                if e["ok"] and cl in FL.GATES_OK:
                    gates.append({"id": f"OK_{cl}", "etapa": cl, "texto": e["gate"], "fuente": FL.CITA_GATES_OK,
                                  "aprobada": bool(aprobaciones.get(cl))})
    else:
        clave = (r, rec.get("subtipo")) if r == "IMAGEN" else (r, None)
        tareas = list(TAREAS_SUELTAS[clave])
        for cl in ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"]:
            e = _etapa(cl)
            usa = any(t.startswith(cl + ".") for t, _ in tareas)
            etapas.append({"clave": cl, "nombre": e["nombre"], "aplica": usa,
                           "razon": ("sólo los subprocesos " + ", ".join(t for t, _ in tareas if t.startswith(cl + "."))
                                     if usa else f"pieza suelta ({r.lower()}): {CITA_SUELTAS}"),
                           "entra": e["entra"], "sale": e["sale"], "gate": e["gate"], "requiere_ok": False,
                           "depende_de": [], "aprobada": None})
        if r == "ANCLA":
            momento = {"A1": ("preflight", "la verifica el preflight: los 9 campos de la tarjeta deben estar fijados"),
                       "A2": ("antes_de_compilar", "OK humano: existen canonizados persona/placa/producto que el ancla necesita"),
                       "A7": ("auditoria", "la verifica la auditoría (gates originales)"),
                       "A10": ("posterior", "después de generar: Evaluación visual")}
            for cod, nom, det, gate in FL.PASOS_ANCLA:
                if gate:
                    m, como = momento.get(cod, ("antes_de_compilar", ""))
                    gates.append({"id": f"ANCLA_{cod}", "etapa": cod, "texto": f"{nom}: {gate}", "momento": m, "como": como,
                                  "fuente": "flujo-anclas.html Paso 2",
                                  "aprobada": bool(aprobaciones.get(cod)) if m == "antes_de_compilar" else None})
    sueltas = {t["codigo"]: t for t in FL.tareas()}
    return {
        "recorrido": r, "subtipo": rec.get("subtipo"), "track": rec.get("track"), "motivo": rec.get("motivo"),
        "etapas": etapas,
        "tareas": [{"codigo": c, "motivo": m, "nombre": sueltas.get(c, {}).get("nombre", c),
                    "gate": sueltas.get(c, {}).get("gate", "")} for c, m in tareas],
        "posteriores": [{"codigo": c, "motivo": m} for c, m in POSTERIORES],
        "gates": gates,
        "entregables": [{"id": e["id"], "nombre": e["nombre"], "casos": e["casos"]} for e in spec["entregas"]],
        "bloqueado_por_gates": [g["id"] for g in gates if g.get("momento", "antes_de_compilar") == "antes_de_compilar" and not g["aprobada"]],
    }


def codigos_tareas(plan: dict) -> set[str]:
    return {t["codigo"] for t in plan["tareas"]}
