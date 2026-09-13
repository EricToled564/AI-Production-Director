# -*- coding: utf-8 -*-
"""Genera apd/brief/TEMPLATE.md desde el schema del Case Fingerprint.

Se genera, no se escribe a mano: si el schema gana una dimensión, el template gana su
pregunta en la siguiente corrida. Así no puede desfasarse, que es cómo se murieron las
41 reglas del lado imagen.

Dos columnas que mandan:
  QUIÉN DECIDE  — user (Eric) · asset (la imagen adjunta) · regla (lo fija el skill)
  BLOQUEA       — si falta y es de Eric, el run no arranca: se pregunta.
"""
import json
from pathlib import Path

ROOT = Path("/home/user/AI-Production-Director")
S = json.loads((ROOT / ".claude/rules/v3/case-fingerprint.schema.json").read_text())

# Quién decide cada dimensión, y si su ausencia bloquea. Nada de esto es criterio libre:
# 'user' = dirección creativa que sólo Eric puede dar; 'asset' = se lee de la imagen
# adjunta cuando hay una; 'regla' = lo fija un archivo del skill; 'run' = lo pone el motor.
DECIDE = {
    "schema_version": ("run", False), "case_id": ("run", False), "project_id": ("user", False),
    "scene_id": ("user", False), "shot_id": ("user", False), "asset_id": ("run", False),
    "stage": ("run", True), "media": ("user", True), "operation": ("user", True),
    "base_type": ("regla", True), "track": ("user", False),
    "generator.family": ("regla", True), "generator.model": ("user", True),
    "generator.adapter_version": ("run", False),
    "deliverable.purpose": ("user", True), "deliverable.aspect_ratio": ("user", True),
    "deliverable.channel": ("user", False), "deliverable.approval_level": ("user", False),
    "subject.count": ("user|asset", True), "subject.kinds": ("user|asset", True),
    "subject.human": ("user|asset", True), "subject.identity_fidelity": ("user", True),
    "subject.recurring_character": ("user", True), "subject.product_present": ("user|asset", False),
    "subject.product_fidelity": ("user", False), "subject.body_visibility": ("user", True),
    "subject.hands_visible": ("user|asset", True), "subject.feet_visible": ("user|asset", True),
    "subject.human_contact": ("user|asset", True),
    "environment.type": ("user|asset", True), "environment.continuity": ("user", False),
    "environment.crowd": ("user|asset", True), "environment.indoor_outdoor": ("user|asset", True),
    "environment.time_of_day": ("user|asset", True),
    "composition.load_bearing": ("user", True), "composition.viewpoint": ("user|asset", True),
    "composition.split_level": ("user|asset", False), "composition.waterline_visible": ("user|asset", False),
    "composition.background_dof": ("user", True), "composition.spatial_invariants": ("user|asset", True),
    "realism.mode": ("user", True), "realism.skin_texture": ("regla", False),
    "realism.materiality": ("regla", False), "realism.optical_physics": ("regla", False),
    "motion.static_frame": ("regla", True), "motion.frozen_action": ("user|asset", True),
    "motion.camera_motion": ("user", False), "motion.subject_motion": ("user|asset", True),
    "motion.final_state_required": ("user", False),
    "physics.water": ("user|asset", False), "physics.splash": ("user|asset", False),
    "physics.bubbles": ("user|asset", False), "physics.turbulence": ("user|asset", False),
    "physics.refraction": ("user|asset", False), "physics.reflection": ("user|asset", False),
    "physics.gravity": ("regla", False), "physics.collision": ("user|asset", False),
    "physics.deformation": ("user|asset", False),
    "continuity.level": ("user", True), "continuity.dimensions": ("user", False),
    "brand.mode": ("user", True), "brand.brand_lock_ref": ("user", True),
    "text.mode": ("user", True), "text.readable_text_required": ("user", True),
    "references.mode": ("user", True), "references.roles": ("user", True),
    "references.style_reference": ("user", False), "references.identity_reference": ("user", False),
    "references.environment_reference": ("user", False),
    "risk_flags": ("regla", False), "unknowns": ("run", False), "provenance": ("run", False),
    "task.family": ("user", True), "task.tags": ("user", False), "task.genre": ("user", True),
    "audio.mode": ("user", False), "audio.dialogue_required": ("user", False),
    "audio.lipsync": ("user", False), "audio.speaker_count": ("user", False),
    "audio.language": ("user", False),
    "sequence.multi_shot": ("user", True), "sequence.shot_count": ("user", True),
    "sequence.start_frame_ref": ("user", False), "sequence.end_frame_ref": ("user", False),
    "sequence.motion_reference": ("user", False),
    "pipeline_track": ("user", True), "prompt_case": ("regla", True),
}

# Dimensiones que el gate de vida reclama y el schema todavía NO tiene. Cada una lleva
# las reglas que hoy están muertas por su ausencia: no son mi criterio, son consecuencia.
PROPUESTAS = [
    ("lighting.setup", ["studio", "natural_window", "open_shade", "direct_sun", "overcast",
                        "practical_ambient", "stadium_floodlight", "mixed", "UNKNOWN"], "user|asset", True,
     "visual-prompt-forge/SKILL.md:265-290 (el lock de iluminación entra verbatim); "
     "vision-decomposer.md:44 (luz quebrada, gobos, luz por persianas)"),
    ("lighting.quality", ["hard", "soft", "diffused", "high_contrast", "flat", "UNKNOWN"], "user|asset", True,
     "creative-direction.md sección de diseño de luz; image/references/photography.md"),
    ("lighting.direction", ["frontal", "side", "back", "top", "grazing", "mixed", "UNKNOWN"], "user|asset", True,
     "los bloques canónicos T1 (light_hard: 'hard grazing light with no fill')"),
    ("treatment.register", ["editorial", "documentary", "advertising", "fine_art", "snapshot_mobile",
                            "vintage_analog", "cinematic", "UNKNOWN"], "user", True,
     "el registro que Eric nombró: editorial ≠ documental ≠ imagen de móvil ≠ vintage"),
    ("treatment.era", ["contemporary", "1970s", "1980s", "1990s", "period_pre1960", "UNKNOWN"], "user", False,
     "golden-rules.md:140-161 (era anchors, cultural anchors)"),
    ("treatment.capture_device", ["pro_camera", "mobile_phone", "instant_film", "film_35mm",
                                  "medium_format", "action_cam", "UNKNOWN"], "user", True,
     "creative-direction.md:28-34 (GoPro, Fujifilm, desechable, Hasselblad, iPhone, Polaroid)"),
    ("composition.shot_size", ["extreme_close_up", "close_up", "medium_close_up", "medium",
                               "medium_full", "full", "wide", "extreme_wide", "UNKNOWN"], "user", True,
     "creative-direction.md:47 (encuadres nombrados); lo que Eric nombró: close-up de rostro ≠ cuerpo completo"),
    ("source_analysis.mode", ["none", "composition_only", "full_decomposition", "UNKNOWN"], "user", True,
     "image/references/vision-decomposer.md completo — 12 reglas muertas hoy; "
     "learned v3.2:13 (fuentes de composición se abstraen, no se adjuntan)"),
    ("series_lock.mode", ["none", "environment", "lighting", "color_grade", "character", "full", "UNKNOWN"],
     "user", True,
     "visual-prompt-forge/SKILL.md:265-290 y failure-modes.md:29-39 — 12 reglas muertas hoy"),
    ("structural_input.mode", ["none", "sketch", "wireframe", "floor_plan", "line_art", "UNKNOWN"], "user", True,
     "image/references/structural.md — 3 reglas muertas hoy"),
    ("environment.time_of_day", ["dawn", "morning", "midday", "golden_hour", "blue_hour", "night",
                                 "overcast_day", "UNKNOWN"], "user|asset", True,
     "hoy es string libre: ningún validador puede condicionar sobre la hora del día"),
    ("task.genre", ["CERRAR A ENUM — hoy string libre"], "user", True,
     "hoy es string libre; este run guardó 'sports_editorial' y ningún validador puede leerlo"),
    ("composition.viewpoint", ["CERRAR A ENUM — hoy string libre"], "user|asset", True,
     "hoy es string libre; el punto de vista gobierna reglas de geometría de cámara"),
    ("environment.type", ["CERRAR A ENUM — hoy string libre"], "user|asset", True,
     "hoy es string libre; gobierna reglas de entorno y de continuidad"),
]


def walk(node, pre=""):
    out = []
    for k, v in (node.get("properties") or {}).items():
        p = f"{pre}.{k}" if pre else k
        if "enum" in v:
            out.append((p, [x for x in v["enum"]]))
        elif v.get("type") == "object" or "properties" in v:
            out += walk(v, p)
        elif v.get("type") == "array":
            out.append((p, None))
        else:
            out.append((p, "LIBRE"))
    return out


# Alcance: SÓLO IMAGEN. Decisión de Eric, 2026-09-13: "ENFÓCATE SOLO EN IMAGEN POR AHORA,
# HACEMOS VIDEO DESPUÉS". Las dimensiones que sólo gobiernan video quedan fuera del template
# hasta entonces; siguen en el schema, nadie las borra.
FUERA_DE_ALCANCE = ("audio.", "sequence.", "motion.camera_motion", "motion.final_state_required")
campos = [c for c in walk(S) if not c[0].startswith(FUERA_DE_ALCANCE)]
L = []
w = L.append
w("# Brief template de imagen — el mismo para crear y para extraer de una imagen")
w("")
w("> Generado por `apd/brief/gen_template.py` desde `.claude/rules/v3/case-fingerprint.schema.json`.")
w("> No se edita a mano: si el schema gana una dimensión, este archivo gana su pregunta en la")
w("> siguiente corrida. Se desfasó una vez y costó 41 reglas muertas del lado imagen.")
w("")
w("> **APROBADO por Eric, 2026-09-13: \"EL TEMPLATE ESTA APROBADO\".** Las 14 dimensiones de la")
w("> parte 2 quedan autorizadas a entrar al schema; eso obliga a republicar el ruleset.")
w("")
w("> **Alcance: sólo imagen.** Video queda para después, por decisión de Eric. Las dimensiones")
w("> de audio, secuencia y movimiento de cámara no se preguntan todavía; siguen en el schema.")
w("")
w("## Cómo se usa")
w("")
w("1. Eric pide una imagen — desde cero, o a partir de una que adjunta. **Siempre se llena este")
w("   mismo template**, entero. La ruta cambia de dónde sale cada dato, no qué datos hacen falta.")
w("2. Toda línea `QUIÉN: user` que quede sin valor y esté marcada `BLOQUEA` **se pregunta a Eric")
w("   antes de armar el brief**. No se rellena por criterio del asistente: esa fuente no existe.")
w("3. Con una imagen adjunta, las líneas `QUIÉN: user|asset` se leen de la imagen y se declara")
w("   `source_analysis.mode`. Lo que la imagen no muestre sigue siendo pregunta para Eric.")
w("4. El template lleno se le da a Eric **para aprobación**. Aprobado, se congela como brief y")
w("   de ahí sale el `case.json`. Sin aprobación no hay run.")
w("")
w("## Leyenda")
w("")
w("| columna | qué significa |")
w("|---|---|")
w("| **QUIÉN** | `user` sólo Eric · `asset` se lee de la imagen adjunta · `regla` lo fija un archivo del skill · `run` lo pone el motor |")
w("| **BLOQUEA** | si falta y es de Eric, se pregunta y el run no arranca |")
w("| **VALORES** | los únicos admitidos. `LIBRE` = hoy es texto libre y **ningún validador puede condicionar sobre él** |")
w("")
w("---")
w("")
w(f"## Parte 1 — las {len(campos)} dimensiones de imagen que el fingerprint ya tiene")
w("")
w("| dimensión | QUIÉN | BLOQUEA | VALORES |")
w("|---|---|:-:|---|")
for p, vals in campos:
    quien, bloquea = DECIDE.get(p, ("user", False))
    if vals is None:
        v = "lista"
    elif vals == "LIBRE":
        v = "**LIBRE** ⚠️"
    else:
        v = " · ".join(f"`{x}`" for x in vals)
    w(f"| `{p}` | {quien} | {'**SÍ**' if bloquea else '—'} | {v} |")
w("")
w("---")
w("")
w("## Parte 2 — dimensiones que el gate de vida reclama y el schema no tiene")
w("")
w("Cada una sale de reglas que **hoy están muertas** porque no hay dónde expresar su condición.")
w("No son propuesta de criterio: son la causa medida de que esas reglas no puedan activarse.")
w("")
w("| dimensión nueva | QUIÉN | BLOQUEA | VALORES | reglas que revive |")
w("|---|---|:-:|---|---|")
for p, vals, quien, bloquea, porque in PROPUESTAS:
    w(f"| `{p}` | {quien} | {'**SÍ**' if bloquea else '—'} | {' · '.join(f'`{x}`' for x in vals)} | {porque} |")
w("")
w("---")
w("")
w("## Parte 3 — lo que el template pregunta y el fingerprint no guarda")
w("")
w("Datos que Eric da, que no son dimensiones de clasificación pero sin los cuales no hay prompt:")
w("")
w("| pregunta | QUIÉN | BLOQUEA |")
w("|---|---|:-:|")
for q in ["¿Qué se ve en la imagen? (sujeto, acción, entorno, en las palabras de Eric)",
          "¿Qué NO debe aparecer? (va al bloque Negative, no al cuerpo)",
          "Colores obligados (hex si los hay: marca, uniforme, producto)",
          "Texto que debe leerse en la imagen, literal y entre comillas",
          "Materiales que deben verse (tela, metal, piel, superficie)",
          "Qué se ancla a un elemento legible de la escena (sw30:118 prohíbe «centre», «left half»)",
          "Formato exacto y si es negociable",
          "Es exploración o es el visual final (cambia el modo de detalle y el costo)",
          "Si hay imagen adjunta: ¿se adjunta al generador, o sólo se estudia y se describe?"]:
    w(f"| {q} | user | **SÍ** |")
w("")
w("---")
w("")
w(f"Dimensiones en la parte 1: **{len(campos)}** · propuestas en la parte 2: **{len(PROPUESTAS)}** · "
  f"preguntas en la parte 3: **9**")
w(f"Campos `LIBRE` hoy (nadie puede condicionar sobre ellos): "
  f"**{sum(1 for _, v in campos if v == 'LIBRE')}**")

out = ROOT / "apd/brief/TEMPLATE.md"
out.write_text("\n".join(L) + "\n", encoding="utf-8")
falta = [p for p, _ in campos if p not in DECIDE]
print(f"escrito {out}  ({len(L)} líneas)")
print(f"dimensiones sin QUIÉN asignado: {falta or 'ninguna'}")
