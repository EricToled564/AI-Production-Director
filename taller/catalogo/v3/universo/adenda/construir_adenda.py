"""Adenda del universo de la prueba (tarea 1 de PLAN_FINAL_PRUEBA.md).

Lee del zip original del repo los textos que quedaron fuera de la base de 13,005: SW30 SKILL.md, las reglas
aprendidas (learned/), los 30 archivos de la raíz del paquete y los 33 ejemplos de repo/examples. Cada texto lleva
veredicto (entra/sale) y motivo. Entra lo que es regla original de generación de imágenes dentro del alcance (decisión
24 §1); sale lo derivado, lo duplicado, lo de video y lo que no es regla.

Uso: python3 -I construir_adenda.py  → escribe adenda_universo.jsonl; sale con código 1 si un archivo del alcance
queda sin veredicto, una línea no vacía de SW30 queda sin segmento, hay solapes o falta un motivo.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[4]
ZIP = REPO / "apd/originales/AI_Production_Director_v3.4.0_COMPLETE.zip"
RAIZ = "AI_Production_Director_v3.4.0_COMPLETE/"
SW30 = RAIZ + "skills/produccion-visual-sw30/SKILL.md"
LEARNED = RAIZ + "repo/.claude/rules/v3/learned/"
EJEMPLOS = RAIZ + "repo/examples/"

SALE_PROCESO = "proceso de entrega o conducta del agente, no regla de generación de imagen"

# (archivo, linea_inicial, linea_final, veredicto, motivo)
SEGMENTOS = [
    (SW30, 1, 4, "sale", "frontmatter: nombre y disparadores de la skill"),
    (SW30, 6, 9, "sale", "objetivo del proyecto SW30, no regla de generación de imagen"),
    (SW30, 11, 30, "sale", SALE_PROCESO + " (pregunta de avance)"),
    (SW30, 32, 45, "entra", "arquitectura del prompt de imagen: tipo T1–T5, bloques nombrados, P(scene, subject, details, mood, usecase, constraints) y E(change, preserve, constraints), metadatos fuera del cuerpo"),
    (SW30, 47, 63, "sale", "sistema de cobertura (rule_registry, rule_ledger, audit_gi2): herramienta de proceso, no regla de imagen"),
    (SW30, 65, 74, "entra", "plantilla T1 de maestro de rostro: light_hard, skin_doc, usecase_doc, clean_doc"),
    (SW30, 76, 77, "entra", "cara irregular en el slot de rasgos"),
    (SW30, 79, 80, "entra", "longitud ~250 palabras; slot de 300+ compite consigo mismo en gpt-image-2"),
    (SW30, 82, 88, "sale", "motor de plantillas del paquete SW30: herramienta, no regla de contenido"),
    (SW30, 89, 89, "entra", "bloque Notes obligatorio en la salida"),
    (SW30, 90, 90, "entra", "Model/Quality/Size/Aspect ratio fuera del cuerpo del prompt"),
    (SW30, 91, 92, "sale", "autotest del motor"),
    (SW30, 94, 98, "sale", "mantenimiento de prompts (editar bloque, no brief): proceso"),
    (SW30, 100, 103, "entra", "columnas que el auditor exige al prompt de gpt-image-2: slots, anti-slop, ratio estándar, metadatos fuera, Notes, cinco efectos ópticos, mood, color, identity-lock, texto de marca, framing positivo, mirada, manos"),
    (SW30, 104, 104, "sale", "lint del builder: herramienta"),
    (SW30, 106, 113, "sale", SALE_PROCESO + " (micro-gate)"),
    (SW30, 115, 115, "sale", "encabezado"),
    (SW30, 116, 117, "entra", "R1 un solo trabajo por generación"),
    (SW30, 118, 119, "entra", "R2 posición por ancla legible de la imagen"),
    (SW30, 120, 121, "entra", "R3 editor sin memoria: verbos operativos"),
    (SW30, 122, 122, "entra", "R4 autocontención de comparaciones"),
    (SW30, 123, 124, "entra", "R5 herencia mínima"),
    (SW30, 125, 126, "entra", "R6 swap de identidad como última operación"),
    (SW30, 127, 128, "entra", "R7 mundos por dos pasos"),
    (SW30, 129, 129, "entra", "R8 still en instante congelado"),
    (SW30, 130, 131, "entra", "R9 contactos entre personas"),
    (SW30, 132, 133, "entra", "R10 logos heredados de asset aprobado"),
    (SW30, 134, 134, "entra", "R11 canonizar con hash y editar desde ahí"),
    (SW30, 135, 136, "entra", "R12 edit, don't re-roll"),
    (SW30, 137, 138, "entra", "R13 máximo 2 intentos por método"),
    (SW30, 139, 141, "entra", "R14 validadores, techos de palabras e inspección al 100 % de rostros y manos"),
    (SW30, 142, 142, "sale", "R15 shots.json: pipeline de storyboard, no imagen suelta"),
    (SW30, 143, 144, "sale", "R16 clips: video, fuera del alcance"),
    (SW30, 145, 146, "sale", "R17 " + SALE_PROCESO),
    (SW30, 147, 148, "sale", "R18 " + SALE_PROCESO),
    (SW30, 149, 150, "sale", "R19 " + SALE_PROCESO),
    (SW30, 151, 152, "sale", "R20 uso de otras skills: " + SALE_PROCESO),
]

V32 = LEARNED + "production-learnings.v3.2.json"
V34 = LEARNED + "production-learnings.v3.4.json"
REGISTRO = LEARNED + "LEARNING_REGISTRY_v3.2.md"
for linea, rid in [(16, "lrn32_lock_preservation"), (53, "lrn32_small_delta_revision"),
                   (90, "lrn32_domain_pose_literal"), (132, "lrn32_reference_role_isolation"),
                   (167, "lrn32_generation_params_are_hard"), (214, "lrn32_ratio_tolerance"),
                   (259, "lrn32_no_unspecified_amplification"), (295, "lrn32_physical_occlusion_strategy"),
                   (347, "lrn32_camera_geometry_visibility"), (389, "lrn32_qa_before_claim"),
                   (425, "lrn32_surgical_edit_after_accept"), (458, "lrn32_nano_underwater_diving_route"),
                   (520, "lrn321_composition_abstraction_no_ref"), (566, "lrn321_no_cross_task_attribute_leak")]:
    SEGMENTOS.append((V32, linea, linea, "entra", f"regla aprendida {rid}, fuera de la base de 13,005"))
for linea, rid in [(16, "lrn34_frozen_brief"), (53, "lrn34_required_fields_resolved"),
                   (90, "lrn34_authorized_delta_only"), (126, "lrn34_immutable_prompt_ast")]:
    SEGMENTOS.append((V34, linea, linea, "entra", f"regla aprendida {rid}, fuera de la base de 13,005"))
SEGMENTOS += [
    (REGISTRO, 1, 3, "sale", "encabezado y política de promoción"),
    (REGISTRO, 5, 16, "sale", "duplicado en prosa de lrn32 1–12 (production-learnings.v3.2.json)"),
    (REGISTRO, 18, 23, "sale", "observaciones del ensayo: evidencia de lrn32_domain_pose_literal, lrn32_reference_role_isolation, lrn32_surgical_edit_after_accept y lrn32_nano_underwater_diving_route, no reglas"),
    (REGISTRO, 25, 26, "sale", "duplicado en prosa de lrn321 13–14"),
    (LEARNED + "model-routing.v3.2.json", 1, 23, "sale", "duplicado de lrn32_nano_underwater_diving_route como config de ruteo"),
]

MOTIVO_RAIZ = {
    "EXHAUSTIVE_CLASSIFICATION_REPORT.md": "reporte de clasificación del ruleset 3.1; no contiene reglas propias",
    "INDEX.md": "inventario de archivos del paquete",
    "START_HERE.md": "instrucciones de instalación y verificación del paquete",
    "V3_2_LEARNING_PATCH_REPORT.md": "reporte que repite las 14 reglas aprendidas v3.2 (entran desde el JSON)",
    "V3_3_2_DEPENDENCY_RECONSTRUCTION_REPORT.md": "reporte de reconstrucción de herramientas SW30; repite obligaciones de SW30",
    "V3_3_DECISION_ROUTING_REPORT.md": "reporte de ruteo de modelos; cita models.md, que ya está en la base",
    "V3_4_BRIEF_FREEZE_REPORT.md": "reporte que repite las 4 reglas aprendidas v3.4 (entran desde el JSON)",
    "MANIFEST_SHA256.txt": "749 líneas hash+ruta, verificadas todas con expresión regular",
    "VERIFY_COMPLETE_PACKAGE.py": "verificador de integridad del paquete",
    "DEPENDENCY_CLOSURE_V3_3_2.json": "resultado de verificación",
    "PACKAGE_METADATA.json": "metadatos del paquete",
    "skills-manifest.json": "descripciones de las 13 skills; las reglas viven en las skills",
    "requirements.txt": "dependencias Python",
}
MOTIVO_EJEMPLO = "ejemplo o fixture de caso, brief o prompt: datos de un caso, sin enunciado normativo propio"
EXCEPCIONES_EJEMPLO = [
    (EJEMPLOS + "briefs/diver_editorial_brief_v1.json", 140, 140, "entra",
     "enunciado normativo de generación de personas dentro del brief de ejemplo: la nacionalidad no se expande a rasgos étnicos estereotipados"),
]


def main():
    z = zipfile.ZipFile(ZIP)
    nombres = [n for n in z.namelist() if not n.endswith("/")]
    raiz = sorted(n for n in nombres if n.count("/") == 1)
    ejemplos = sorted(n for n in nombres if n.startswith(EJEMPLOS))
    learned = sorted(n for n in nombres if n.startswith(LEARNED))
    errores = []
    if len(raiz) != 30:
        errores.append(f"raíz: {len(raiz)} archivos, se esperaban 30")
    if len(ejemplos) != 33:
        errores.append(f"ejemplos: {len(ejemplos)} archivos, se esperaban 33")

    segs = list(SEGMENTOS)
    for n in raiz:
        base = n.split("/", 1)[1]
        motivo = MOTIVO_RAIZ.get(base) or ("salida de verificación o hash" if base.startswith(("V3_", "VERIFICATION")) else None)
        if motivo is None:
            errores.append(f"sin motivo: {n}")
            continue
        total = len(z.read(n).decode("utf-8").splitlines()) or 1
        segs.append((n, 1, total, "sale", motivo))
    for n in ejemplos:
        total = len(z.read(n).decode("utf-8").splitlines())
        exc = [e for e in EXCEPCIONES_EJEMPLO if e[0] == n]
        corte = 1
        for _, a, b, v, m in exc:
            if a > corte:
                segs.append((n, corte, a - 1, "sale", MOTIVO_EJEMPLO))
            segs.append((n, a, b, v, m))
            corte = b + 1
        if corte <= total:
            segs.append((n, corte, total, "sale", MOTIVO_EJEMPLO))

    salida = []
    cubiertas = {}
    for i, (arch, a, b, ver, mot) in enumerate(segs, 1):
        crudo = z.read(arch)
        lineas = crudo.decode("utf-8").splitlines()
        if not mot or ver not in ("entra", "sale"):
            errores.append(f"veredicto o motivo vacío: {arch}:{a}")
        if b > max(len(lineas), 1):
            errores.append(f"rango fuera del archivo: {arch}:{a}-{b}")
        for l in range(a, b + 1):
            if (arch, l) in cubiertas:
                errores.append(f"solape: {arch}:{l}")
            cubiertas[(arch, l)] = True
        texto = "\n".join(lineas[a - 1:b])
        salida.append({"id": f"ADD-{i:04d}", "archivo": arch.split("/", 1)[1], "linea_inicial": a, "linea_final": b,
                       "sha256_archivo": hashlib.sha256(crudo).hexdigest(), "veredicto": ver, "motivo": mot,
                       "texto": texto})

    # En las reglas aprendidas la condición y la fuerza viven en "metadata"; viajan con el texto.
    for arch in (V32, V34):
        reglas = {r["rule"]["text"]: r["metadata"] for r in json.loads(z.read(arch))["rules"]}
        for r in salida:
            if RAIZ + r["archivo"] == arch:
                md = reglas[json.loads("{" + r["texto"].strip().rstrip(",") + "}")["text"]]
                r["efecto"], r["condicion"] = md["effect"], md["when"]
    for arch in [SW30] + learned:
        for l, t in enumerate(z.read(arch).decode("utf-8").splitlines(), 1):
            if t.strip() and (arch, l) not in cubiertas and arch != V32 and arch != V34:
                errores.append(f"línea no vacía sin segmento: {arch}:{l}")
    for arch in learned:
        if not any(s[0] == arch for s in segs):
            errores.append(f"archivo learned sin veredicto: {arch}")

    with open(AQUI / "adenda_universo.jsonl", "w", encoding="utf-8") as f:
        for r in salida:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    entra = sum(r["veredicto"] == "entra" for r in salida)
    print(f"{len(salida)} textos · entra {entra} · sale {len(salida) - entra} · archivos {len({r['archivo'] for r in salida})}")
    for e in errores:
        print("ERROR", e)
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
