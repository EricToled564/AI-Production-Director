"""Auditoría posterior a la composición y estado de liberación.

Cuatro niveles que la interfaz muestra por separado — nunca como una garantía única:
  1. cobertura     cada id del registro vigente tiene decisión válida (mecánico)
  2. semántica     un revisor independiente (modelo o humano) juzgó regla ↔ texto
  3. redacción     el usuario aprobó ESTE texto (hash)
  4. visual        resultado del generador: fuera de la auditoría textual; sólo se
                   registra si el usuario adjunta el render

Los controles deterministas ejecutan los gates ORIGINALES como subprocesos, sin
modificarlos: gate_image.py, gate_dramaturgy.py, aurora/prompt_linter.py (repo) y
prompt_ast_gate_v34.py / prompt_render_v34.py (paquete v3.4).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from . import fuentes as F
from . import ledger as L

PY = sys.executable
AURORA_PLAT = {"gpt-image-2": "gpt_image_2", "nano-banana-pro": "nano_banana_pro", "nano-banana-2": "nano_banana_2",
               "kling": "kling_3.0", "veo": "veo_3.1", "seedance": "seedance_2.5", "midjourney": "midjourney",
               "flux": "flux", "hailuo": "hailuo"}
MODELO_NOMBRE = {"gpt-image-2": "GPT Image 2 (gpt-image-2)", "nano-banana-pro": "Nano Banana Pro", "nano-banana-2": "Nano Banana 2",
                 "kling": "Kling 3.0", "veo": "Veo 3.1", "seedance": "Seedance 2.5"}
META_RE = re.compile(r"(?im)^\s*(?:model|quality|size|aspect\s*ratio|size\s*/\s*ratio)\s*:\s*|\b--ar\b")
CONTRADICCIONES = [
    (re.compile(r"head[- ]and[- ]shoulders|shoulders up|from the shoulders", re.I), re.compile(r"full[- ]body|head to feet|full length", re.I),
     "encuadre contradictorio: hombros hacia arriba y cuerpo entero en el mismo prompt"),
    (re.compile(r"black[- ]and[- ]white|monochrome|tri-x", re.I), re.compile(r"natural colou?r|full colou?r|colou?r photograph", re.I),
     "color contradictorio: blanco y negro y color natural"),
    (re.compile(r"hard (?:grazing |directional )?light|no fill", re.I), re.compile(r"soft even|no hard shadows|gradual shadow transitions", re.I),
     "luz contradictoria: dura sin relleno y suave pareja"),
]


NEG = re.compile(r"\b(?:not|no|without|never|sin|nunca)\b[\w\s,-]{0,25}$", re.I)


def afirmado(rx: re.Pattern, t: str) -> bool:
    """Hay al menos una mención NO negada ('not black and white' no afirma blanco y negro)."""
    return any(not NEG.search(t[max(0, m.start() - 40):m.start()]) for m in rx.finditer(t))


def _run(args, entrada=None, env=None, timeout=120):
    r = subprocess.run(args, input=entrada, capture_output=True, text=True, env=env, timeout=timeout, cwd=str(F.REPO))
    return r.returncode, r.stdout, r.stderr


def gate_hook(nombre: str, texto: str, modelo: str) -> dict:
    """Ejecuta un gate Stop original con un mensaje de entrega real (modelo nombrado + bloque cercado)."""
    msg = f"Modelo: {MODELO_NOMBRE.get(modelo, modelo)}\n\n```\n{texto.strip()}\n```\n"
    env = dict(os.environ, FUPAI_SKILLS_ROOT=str(F.skills_root()), TMPDIR=tempfile.gettempdir())
    payload = json.dumps({"last_assistant_message": msg, "session_id": f"apd-{os.getpid()}-{nombre}-{F.sha256_text(texto)[:8]}"})
    code, out, err = _run([PY, str(F.HOOKS / f"{nombre}.py")], payload, env)
    return {"gate": nombre, "exit": code, "estado": "PASS" if code == 0 else ("BLOCK" if code == 2 else "ERROR"),
            "salida": (out + err).strip()[-2500:], "original": f".claude/hooks/{nombre}.py"}


def aurora(texto: str, modelo: str, caso: str, refs: list, tratamiento: str | None) -> dict:
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "prompt.txt"
        p.write_text(texto, encoding="utf-8")
        rf = Path(d) / "refs.yaml"
        if refs:
            rf.write_text("\n".join(f'- file: "{r.get("nombre")}"\n  role: "{(r.get("rol") or "").upper()}"' for r in refs) + "\n")
        else:
            rf.write_text("# sin referencias\n[]\n")
        args = [PY, str(F.HOOKS / "aurora" / "prompt_linter.py"), "--prompt", str(p), "--refs", str(rf),
                "--case", caso, "--json"]
        if modelo in AURORA_PLAT:
            args += ["--platform", AURORA_PLAT[modelo]]
        if tratamiento in ("race",):
            args += ["--treatment", "race"]
        code, out, err = _run(args)
    try:
        j = json.loads(out)
    except Exception:
        j = {"raw": (out + err)[-2000:]}
    return {"gate": "aurora", "exit": code, "estado": "PASS" if code == 0 else "FAIL", "detalle": j,
            "original": ".claude/hooks/aurora/prompt_linter.py (v1.2-fupai)"}


def gates_v34(compilado: dict) -> dict:
    """AST gate y render del paquete v3.4, ejecutados tal cual sobre los artefactos de la app."""
    hooks = F.extraer_paquete() / "repo" / ".claude" / "hooks"
    with tempfile.TemporaryDirectory() as d:
        b = Path(d) / "brief.json"
        a = Path(d) / "ast.json"
        o = Path(d) / "render.txt"
        b.write_text(json.dumps(compilado["brief"], ensure_ascii=False))
        a.write_text(json.dumps(compilado["ast"], ensure_ascii=False))
        c1, out1, err1 = _run([PY, str(hooks / "prompt_ast_gate_v34.py"), "--brief", str(b), "--ast", str(a), "--json"])
        c2, out2, err2 = _run([PY, str(hooks / "prompt_render_v34.py"), "--ast", str(a), "--brief", str(b), "--out", str(o)])
        rend = o.read_text(encoding="utf-8") if o.exists() else ""
    try:
        j1 = json.loads(out1)
    except Exception:
        j1 = {"raw": out1 + err1}
    prosa = compilado["ast"].get("formato") in ("nano-banana", "veo", "seedance")
    esperado = rend if not prosa else " ".join(p for p in rend.strip().split("\n\n")) + "\n"
    return {"ast_gate": {"exit": c1, "estado": j1.get("status", "ERROR"), "detalle": j1,
                         "original": "pkg repo/.claude/hooks/prompt_ast_gate_v34.py"},
            "render_original": {"exit": c2, "igual": esperado == compilado["texto"],
                                "hash_render_original": F.sha256_text(esperado), "hash_app": compilado["hash"],
                                "original": "pkg repo/.claude/hooks/prompt_render_v34.py",
                                "nota": "en formato prosa los bloques se unen con espacio en vez de línea en blanco"
                                        if prosa else ""}}


def limites_longitud(compilado: dict, spec: dict):
    """Rango de palabras establecido por la fuente para el modelo destino (matriz de sintaxis)."""
    from . import sintaxis as SX
    m = SX.MODELO_SX.get(spec["comunes"]["modelo"]["valor"] or "")
    lon = (SX.catalogo()["modelos"].get(m) or {}).get("longitud") or {}
    if lon.get("max"):
        c = lon.get("cita") or {}
        return lon.get("min"), lon["max"], f"{c.get('archivo')}:{c.get('linea_ini')} «{c.get('texto', '')[:90]}»"
    return None, None, "sin límite de longitud documentado para este modelo"


def add_longitud(add, texto, compilado, spec):
    from . import politicas as PO
    n = len(re.findall(r"\S+", texto))
    lo, hi, fuente = limites_longitud(compilado, spec)
    if not hi:
        add("longitud", True, f"{n} palabras · {fuente}", obligatorio=False, fuente=PO.LONGITUD["id"])
        return
    tope = int(hi * PO.LONGITUD["factor_bloqueo"])
    if n > tope:
        add("longitud", False, f"{n} palabras > {tope} (2× el máximo {hi} de {fuente}): bloquea — regenerar acortando bloques",
            obligatorio=True, fuente=PO.LONGITUD["id"] + " · " + PO.LONGITUD["regla"])
    else:
        aviso = "" if (lo or 0) <= n <= hi else f" — fuera del rango aspiracional {lo}–{hi} (aviso, no bloquea)"
        add("longitud", True, f"{n} palabras · rango de la fuente {lo}–{hi}{aviso}", obligatorio=False,
            fuente=PO.LONGITUD["id"] + " · " + fuente)


def controles(compilado: dict, spec: dict, ent: dict, dec: dict, reg, perfil: dict, anclas: set, semantica: dict | None = None) -> list[dict]:
    t = compilado["texto"]
    fmt = compilado["formato"]
    out = []

    def add(id_, ok, detalle, obligatorio=True, fuente=""):
        out.append({"id": id_, "ok": bool(ok), "detalle": detalle, "obligatorio": obligatorio, "fuente": fuente})

    g = L.gate_mecanico(reg, dec, anclas)
    add_longitud(add, t, compilado, spec)
    add("cobertura_ids", g["ok"], "; ".join(g["bloqueos"]) or f"{g['decididas']}/{g['total_registro']} ids con decisión válida",
        fuente="A3 del encargo · METODO.md Paso 3")
    # secciones del formato
    from .compilador import FORMATOS
    etiquetas = [s["etiqueta"] for s in FORMATOS[fmt]["secciones"] if s["etiqueta"] and not s.get("solo_si")]
    faltan = [e for e in etiquetas if e not in t]
    dup = [e for e in etiquetas if t.count(e) > 1]
    orden = [t.find(e) for e in etiquetas if e in t]
    add("secciones", not faltan and not dup and orden == sorted(orden),
        f"faltan {faltan} · duplicadas {dup}" if (faltan or dup) else ("orden incorrecto" if orden != sorted(orden) else f"{len(etiquetas)} secciones en orden"),
        fuente=FORMATOS[fmt]["fuente"])
    add("metadatos_fuera", not META_RE.search(t), "Model/Quality/Size/Aspect ratio fuera del cuerpo",
        fuente="SW30 motor de plantillas: 'se cuela un metadato … dentro del cuerpo' → TemplateViolation")
    if fmt == "nano-banana":
        m = re.search(r"\b\d{2,3}\s?mm\b|f/\d|\biso\s?\d", t, re.I)
        add("nb_sin_numeros_lente", not m, f"encontrado {m.group(0)!r}" if m else "sin parámetros numéricos de lente",
            fuente="image/references/nano-banana.md:22-24")
    if fmt == "kling":
        neg = (spec["comunes"].get("negativos") or {}).get("valor") or ""
        add("kling_negativos", not re.search(r"\bno\s+\w", str(neg), re.I) and len([x for x in str(neg).split(",") if x.strip()]) <= 8,
            "negativos sin 'no X' y ≤8 ítems", fuente="kling.md:187-204 · SW30 R16")
    for a, b, desc in CONTRADICCIONES:
        if afirmado(a, t) and afirmado(b, t):
            add("contradiccion", False, desc, fuente="universal-rules U8 (no contradicciones) · caso Vivaldi T2")
            break
    else:
        add("contradiccion", True, "sin pares contradictorios conocidos")
    # restricciones del brief conservadas: cada hecho prompt_required aparece literal
    faltan_h = []
    for k, s in compilado["brief"]["field_states"].items():
        v = compilado["brief"]["facts"].get(k)
        if s["prompt_required"] and isinstance(v, (str, int)) and str(v) not in t:
            faltan_h.append(k)
    add("restricciones_conservadas", not faltan_h, f"campos no presentes literalmente: {faltan_h}" if faltan_h else
        "todos los campos requeridos del brief congelado aparecen literalmente", fuente="v3.4 brief freeze · A4")
    # parámetros requeridos
    pnulos = [p["nombre"] for p in compilado["parametros"] if p["nombre"] in ("model", "size", "quality", "aspectRatio", "image_size",
                                                                            "aspect_ratio", "duration") and not p["valor"]]
    add("parametros", not pnulos, f"sin valor: {pnulos}" if pnulos else "parámetros externos completos",
        fuente="A4: parámetros de la herramienta separados del texto")
    # evidencia de cada APLICA
    sin = []
    cuerpo = {r for b in compilado["bloques"] for r in b["satisface"]}
    ver = (semantica or {}).get("veredictos", {}) if (semantica or {}).get("texto_hash") == compilado["hash"] else {}
    for k, v in dec.items():
        if v["estado"] == "APLICA" and k not in cuerpo and k not in compilado["evidencia_fuera_del_cuerpo"]:
            sv = ver.get(k)
            if sv and sv.get("veredicto") in ("CUMPLE", "NO_EVALUABLE_EN_TEXTO") and (sv.get("bloque") or sv.get("evidencia")):
                continue  # el revisor semántico localizó la evidencia
            sin.append(k)
    add("evidencia_aplica", not sin, f"{len(sin)} reglas APLICA sin bloque ni parámetro/nota asignado" if sin
        else "cada APLICA tiene bloque, parámetro o nota de proceso asignado", fuente="A5.1 del encargo")
    out[-1]["ids"] = sin
    return out


def auditar(compilado, spec, ent, dec, reg, perfil, caso_aurora: str, correr_originales=True, semantica=None) -> dict:
    anclas = L.anclas_brief(perfil, spec)
    res = {"texto_hash": compilado["hash"], "ledger_hash": F.sha256_text(F.canon_json({k: v["estado"] for k, v in dec.items()})),
           "registro": reg.version, "controles": controles(compilado, spec, ent, dec, reg, perfil, anclas, semantica)}
    if correr_originales:
        mod = spec["comunes"]["modelo"]["valor"]
        res["originales"] = {
            "gate_image": gate_hook("gate_image", compilado["texto"], mod),
            "gate_dramaturgy": gate_hook("gate_dramaturgy", compilado["texto"], mod),
            "aurora": aurora(compilado["texto"], mod, caso_aurora, spec["comunes"]["referencias"]["valor"] or [],
                             spec["comunes"]["tratamiento"]["valor"]) if caso_aurora else
                      {"gate": "aurora", "estado": "NO_APLICA", "exit": None, "original": ".claude/hooks/aurora/prompt_linter.py",
                       "detalle": {"motivo": "el linter no tiene caso para texto-a-video: sus casos de video son I2V (3a/3b/3c) y diálogo (4); "
                                             "prompt_linter.py:195 mapea CLIP→3a (I2V)"}},
            **gates_v34(compilado),
        }
    res["recibo"] = L.recibo(reg, dec, perfil.get("_conflictos", []))
    return res


# Qué gates originales bloquean y cuáles informan. Autoridad: DECISIONES.md #2 (longitud nunca bloquea).
BLOQUEANTES_ORIGINALES = {"gate_dramaturgy", "ast_gate", "render_original"}


def estado_liberacion(auditoria: dict | None, texto_actual_hash: str, semantica: dict | None, aprobacion: dict | None,
                      visual: list | None, excepciones: dict | None = None) -> dict:
    excepciones = excepciones or {}
    bloqueos = []
    if not auditoria:
        return {"liberable": False, "bloqueos": ["sin auditoría"], "niveles": _niveles(None, semantica, aprobacion, visual)}
    if auditoria["texto_hash"] != texto_actual_hash:
        bloqueos.append("el texto cambió después de auditarse (hash distinto): reauditar")
    for c in auditoria["controles"]:
        if c["obligatorio"] and not c["ok"] and c["id"] not in excepciones:
            bloqueos.append(f"control {c['id']}: {c['detalle']}")
    org = auditoria.get("originales", {})
    for k in BLOQUEANTES_ORIGINALES:
        g = org.get(k)
        if not g:
            continue
        ok = g.get("igual") if k == "render_original" else g.get("estado") == "PASS"
        if not ok and k not in excepciones:
            bloqueos.append(f"gate original {k} no pasa")
    au = org.get("aurora")
    if au and au["estado"] not in ("PASS", "NO_APLICA") and "aurora" not in excepciones:
        bloqueos.append("aurora-prompt-linter FAIL (ver detalle; la longitud sola no bloquea: DECISIONES #2)")
    gi = org.get("gate_image")
    if gi and gi["estado"] != "PASS" and "gate_image" not in excepciones:
        bloqueos.append("gate_image no pasa (ver detalle o registrar excepción con autoridad)")
    sem_ok = bool(semantica) and semantica.get("completo") and semantica.get("texto_hash") == texto_actual_hash \
        and not semantica.get("no_cumple_abiertos")
    if not sem_ok:
        if semantica and semantica.get("texto_hash") == texto_actual_hash and semantica.get("pendientes"):
            bloqueos.append(f"revisión semántica: {len(semantica['pendientes'])} reglas de los bloques cambiados pendientes "
                            f"({', '.join((semantica.get('heredada') or {}).get('bloques', []))}); el resto se heredó")
        elif semantica and semantica.get("texto_hash") == texto_actual_hash and semantica.get("no_cumple_abiertos"):
            bloqueos.append(f"revisión semántica: {len(semantica['no_cumple_abiertos'])} NO_CUMPLE abiertos — corregir el bloque fuente "
                            "o disputar con autoridad documentada")
        else:
            bloqueos.append("interpretación semántica no revisada para este texto (modelo o revisión humana)")
    if not aprobacion or aprobacion.get("texto_hash") != texto_actual_hash:
        bloqueos.append("redacción pendiente de aprobación humana para este texto")
    return {"liberable": not bloqueos, "bloqueos": bloqueos, "niveles": _niveles(auditoria, semantica, aprobacion, visual,
                                                                                 texto_actual_hash)}


def _niveles(aud, sem, apr, vis, h=None):
    cob = next((c for c in (aud or {}).get("controles", []) if c["id"] == "cobertura_ids"), None)
    return {
        "cobertura": {"estado": "COMPROBADA" if cob and cob["ok"] else "INCOMPLETA", "detalle": cob["detalle"] if cob else "sin auditoría",
                      "significa": "cada id del registro tiene una decisión válida; no prueba que cada decisión sea correcta"},
        "semantica": {"estado": (("REVISADA_" + sem.get("revisor", "MODELO").split(":")[0].upper())
                                 + (f"_CON_{len(sem['no_cumple_abiertos'])}_NO_CUMPLE" if sem.get("no_cumple_abiertos") else ""))
                      if sem and sem.get("completo") and sem.get("texto_hash") == h else "NO_REVISADA",
                      "detalle": (sem or {}).get("resumen", ""),
                      "significa": "un revisor independiente contrastó reglas aplicables con el texto"},
        "redaccion": {"estado": "APROBADA" if apr and apr.get("texto_hash") == h else "PENDIENTE_APROBACION_HUMANA",
                      "significa": "el director aprobó este texto exacto (hash)"},
        "visual": {"estado": "EVALUADO_CON_DEFECTOS" if vis and any(v.get("defectos") for v in vis) else
                   ("EVALUADO_SIN_DEFECTOS_REGISTRADOS" if vis else "NO_EVALUADO"),
                   "significa": "la auditoría textual no certifica la imagen o el video generados"},
    }
