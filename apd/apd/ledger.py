"""Decisión exhaustiva por regla: un estado por cada id del registro vigente.

Estados: APLICA · NO_APLICA · CONDICIONAL · CONFLICTO · PENDIENTE.

Capas (la decisión guarda cuál decidió):
  determinista  propuesta con evidencia de la base (medio, tareas, casos, facetas, fase)
                y razón que cita el dato concreto del brief. Nunca descarta sin razón.
  modelo        revisión por lotes (llm.py); cada lote se valida: ids exactos, sin
                duplicados, sin inventados, NO_APLICA con razón específica.
  humano        el usuario decide un conflicto o corrige una decisión.

Las clasificaciones de la base (caso/tarea/faceta) son evidencia, no veto: se citan
en la razón y el modelo o el usuario pueden revertirlas.
"""

from __future__ import annotations

import json
import re
from collections import Counter

from . import conflictos as CF
from . import fuentes as F

FUERTES = {"archivo", "auditoria", "manual"}   # orígenes de faceta que pueden descartar solos
ESTADOS = ("APLICA", "NO_APLICA", "CONDICIONAL", "CONFLICTO", "PENDIENTE")

MEDIO_D8 = {"gpt-image-2": "gpt-image-2", "nano-banana-pro": "nano-banana-pro", "nano-banana-2": "nano-banana-2",
            "midjourney": "midjourney", "flux": "flux", "kling": "kling", "veo": "veo", "seedance": "seedance",
            "hailuo": "hailuo"}
D3_DE_CASO = {"T1": "1", "T2": "1", "T3": "1", "T4": "2_contacto", "PROD": "0", "LUGAR": "0", "EDIF": "0",
              "OBJ": "0", "MULTITUD": "multitud", "ENSAMBLE": "ensamble"}
D1_DE_CASO = {"T1": "character_ref", "T2": "character_ref", "LUGAR": "environment_ref"}

GENERICAS = re.compile(r"^\W*(n/?a|no aplica|no aplica a este caso|no relevante|not applicable|irrelevant|"
                       r"does not apply|no corresponde|no procede|sin relaci[oó]n|fuera de alcance)\W*$", re.I)
COND = re.compile(r"^\s*(\*\*)?(if|when|for\s|unless|si\s|cuando|en caso|solo si|sólo si|если|когда)", re.I)

# destino de evidencia por palabras clave (ES/EN/RU). Orden = prioridad.
DESTINOS = [
    ("vocabulario", r"stunning|epic|masterpiece|cinematic|vague praise|tag[- ]soup|vocabulario prohibido|banned|"
                    r"prohibid[oa]s?\s+(?:las\s+)?palabras|beautiful lighting|high quality|слоп|anti-slop|lazy phrasing"),
    ("parametros", r"quality:|aspect[ _]?ratio|\bratio\b|resoluci|resolution|\bsize\b|\b[124]k\b|--ar|image_size|"
                   r"aspectratio|duration|duraci[oó]n|cfg|seed\b|тариф|\bpx\b|1024|1536"),
    ("referencias", r"reference|referencia|image \d|@image|attach|adjunt|\brefs?\b|element"),
    ("proceso", r"canoniz|\bhash|critique|cr[ií]tica|re-?roll|generaci[oó]n|generate|cr[eé]ditos|credits|"
                r"approv|aprob|iteraci|iterat|\bround|ronda|variant|draft|borrador|preflight|micro-?gate|inspecci|"
                r"zoom|valida|lint|checklist|entrega|deliver|shots\.json|storyboard"),
    ("luz", r"\blight|\bluz\b|lighting|ilumin|shadow|sombra|softbox|\brim\b|backlight|contraluz|specular|освещ|свет"),
    ("textura", r"skin|piel|pore|poro|texture|textura|retouch|retoque|pl[aá]stic|grain|grano|film stock|tri-x|"
                r"portra|halaci|halation|кожа|текстур"),
    ("camara", r"camera|c[aá]mara|\blens|lente|\d+\s?mm\b|angle|[aá]ngulo|eye-level|focal|\bdof\b|depth of field|"
               r"bokeh|framing|encuadre|close-up|plano|shot type|perspective|perspectiva|ракурс|камер"),
    ("fondo", r"background|fondo|\bscene\b|escena|environment|entorno|placa|setting|location|locaci"),
    ("identidad", r"\bface|rostro|\bcara\b|identity|identidad|character|personaje|subject|sujeto|expression|"
                  r"expresi|\bhair|pelo|\beyes?\b|ojos|wardrobe|vestuario|clothes|ropa|person|persona|лиц"),
    ("color", r"colou?r|\bhex\b|palette|paleta|\bgrade\b|saturat|monochrom|blanco y negro|b/n|цвет"),
    ("restricciones", r"constraint|negative|negativ|no text|sin texto|watermark|\blogo|must not|avoid|evita|never|nunca"),
    ("movimiento", r"motion|movimiento|dolly|\bpan\b|tracking|push-?in|timecode|\bshot \d|segundos|seconds|"
                   r"frozen|congelad|blur|barrid"),
    ("audio", r"audio|sound|sonido|dialog|di[aá]logo|music|m[uú]sica|voice|\bvoz\b"),
    ("longitud", r"\bwords?\b|palabras|length|longitud|token|слов"),
    ("estructura", r"slot|section|secci[oó]n|label|structure|estructura|\border\b|orden|verb|verbo|positive|json|"
                   r"prose|prosa|format|prompt"),
]
DESTINOS_RE = [(k, re.compile(p, re.I)) for k, p in DESTINOS]


def destinos(texto: str) -> list[str]:
    return [k for k, rx in DESTINOS_RE if rx.search(texto)]


def perfil_de(spec: dict, plan: dict, entrega: dict) -> dict:
    c = spec["comunes"]
    casos = set(entrega["casos"])
    medio = "VIDEO" if c["medio"]["valor"] == "video" else "IMAGEN"
    roles = {r.get("rol") for r in (c["referencias"]["valor"] or []) if isinstance(r, dict)}
    if not roles and medio == "IMAGEN" and plan.get("subtipo") == "genesis":
        roles = {"genesis"}
    color = c.get("color", {}).get("valor") or ""
    col = "bn" if "black-and-white" in str(color) else ("color" if color else None)
    caso0 = sorted(casos)[0] if casos else None
    d3 = spec["comunes"].get("d3", {}).get("valor") or D3_DE_CASO.get(caso0)
    def tarjeta(d):
        f = c.get(f"tarjeta_{d}") or {}
        return f.get("valor") if f.get("estado") == "LOCKED" else None
    perf = {
        "medio": medio, "casos": casos, "tareas": {t["codigo"] for t in plan["tareas"]},
        "modelo": MEDIO_D8.get(c["modelo"]["valor"]) if c["modelo"]["estado"] == "LOCKED" else None,
        "d1": c.get("d1", {}).get("valor") or D1_DE_CASO.get(caso0),
        "d2": c["accion"]["valor"] if c["accion"]["estado"] == "LOCKED" else None,
        "d3": d3,
        "d4": c["tratamiento"]["valor"] if c["tratamiento"]["estado"] == "LOCKED" else None,
        "d9": c["angulo"]["valor"] if c["angulo"]["estado"] == "LOCKED" else None,
        "roles": roles, "recorrido": plan["recorrido"], "color": col,
        "decision_trix": (spec.get("decisiones") or {}).get("CF-TRIX-COLOR"),
        "decisiones": spec.get("decisiones") or {},
    }
    # recorrido ANCLA: la tarjeta D1–D4 (flujo-anclas Paso 1) manda sobre lo inferido del brief
    for d in ("d1", "d2", "d3", "d4"):
        if tarjeta(d):
            perf[d] = tarjeta(d)
    return perf


FUERA_DE_CLAVE = {"decisiones", "decision_trix", "_conflictos"}  # decisiones de conflicto: se aplican encima de la revisión


def clave_perfil(p: dict) -> str:
    q = {k: (sorted(v) if isinstance(v, set) else v) for k, v in p.items() if k not in FUERA_DE_CLAVE}
    return F.sha256_text(F.canon_json(q))[:16]


def etiqueta(p: dict) -> str:
    partes = ["/".join(sorted(p["casos"])) or "?", p["modelo"] or "modelo sin decidir",
              "imagen fija" if p["medio"] == "IMAGEN" else "video"]
    if p["d3"]:
        partes.append(f"sujetos={p['d3']}")
    if p["d2"]:
        partes.append(f"acción={p['d2']}")
    if p["d4"]:
        partes.append(f"tratamiento={p['d4']}")
    return " · ".join(partes)


class Clasif:
    """Vista de la clasificación de la base + complemento de la app para una regla."""

    def __init__(self, reg, compl: dict):
        self.reg = reg
        self.compl = compl

    def casos(self, rid):
        v = [c for c, _ in self.reg.casos.get(rid, [])]
        return v or self.compl.get(rid, {}).get("caso", {}).get("valor", [])

    def origen_casos(self, rid):
        v = {o for _, o in self.reg.casos.get(rid, [])}
        return v or ({"app_derivada"} if rid in self.compl and "caso" in self.compl[rid] else set())

    def tareas(self, rid):
        v = [t for t, _ in self.reg.tareas.get(rid, [])]
        return v or self.compl.get(rid, {}).get("tarea", {}).get("valor", [])

    def faceta(self, rid, d):
        vals = self.reg.facetas.get(rid, {}).get(d)
        if vals:
            return [v for v, _ in vals], sorted({o for _, o in vals})
        c = self.compl.get(rid, {}).get(d)
        return (c["valor"], ["app_derivada"]) if c else ([], [])


def _dec(estado, razon, capa="determinista", evidencia=None, campos=None, destino=None, inferencia=False):
    return {"estado": estado, "razon": razon, "capa": capa, "evidencia": evidencia or {},
            "campos": campos or [], "destino": destino or [], "inferencia": inferencia}


def decidir_regla(r: dict, cl: Clasif, p: dict) -> dict:
    rid = r["id"]
    et = etiqueta(p)
    casos = [c for c in cl.casos(rid) if c != "NINGUNO"]
    tareas = cl.tareas(rid)
    ev = {"medio": r["medio"], "fase": r["fase"], "ambito": r["ambito"], "casos": cl.casos(rid), "tareas": tareas}
    inferencia = r.get("estado") == "A_PRUEBA"
    if r.get("estado") == "REFUTADA":
        return _dec("NO_APLICA", f"regla REFUTADA en su fuente; no se sirve a {et}", evidencia=ev)
    if r["ambito"] == "META":
        return _dec("NO_APLICA", f"metadato del archivo {r['archivo']} (licencia/README), no instrucción de producción para {et}", evidencia=ev)
    if r["medio"] == "VIDEO" and p["medio"] == "IMAGEN":
        return _dec("NO_APLICA", f"regla de medio VIDEO ({r['skill']}/{r['archivo']}); esta entrega es imagen fija ({et}) sin clip",
                    evidencia=ev, campos=["medio"])
    if r["medio"] == "IMAGEN" and p["medio"] == "VIDEO" and not (set(tareas) & p["tareas"]):
        return _dec("NO_APLICA", f"regla de imagen fija ({r['archivo']}); esta entrega es un prompt de video ({et})",
                    evidencia=ev, campos=["medio"])
    comunes_t = set(tareas) & p["tareas"]
    if not comunes_t:
        return _dec("NO_APLICA", f"subprocesos de la regla {', '.join(tareas[:6]) or '—'}; el recorrido {p['recorrido']} de esta "
                                 f"entrega sólo usa {', '.join(sorted(p['tareas']))} ({et})", evidencia=ev, campos=["recorrido"])
    if casos and not (set(casos) & p["casos"]) and not (set(casos) & {"SHOT", "QA", "ENTREGA"} and p["recorrido"] in ("SPOT",)):
        return _dec("NO_APLICA", f"casos de la regla {', '.join(casos)}; esta entrega es {'/'.join(sorted(p['casos']))} ({et})",
                    evidencia=ev, campos=["tipo_tarea"])
    fuertes_caso = cl.origen_casos(rid) & {"regla", "auditoria"}
    if not casos and not fuertes_caso:
        return _dec("CONDICIONAL", f"la base sólo la clasifica NINGUNO por {'/'.join(sorted(cl.origen_casos(rid))) or '—'} "
                                   f"(evidencia débil) y comparte subproceso {', '.join(sorted(comunes_t))} con {et}: revisar",
                    evidencia=ev, destino=destinos(r["texto"]), campos=["tipo_tarea"])
    if not casos:
        return _dec("NO_APLICA", f"la base la clasifica NINGUNO (no gobierna un caso de producción); comparte subproceso "
                                 f"{', '.join(sorted(comunes_t))} pero no el caso {'/'.join(sorted(p['casos']))} de esta entrega",
                    evidencia=ev, campos=["tipo_tarea"])
    # modelo
    d8, o8 = cl.faceta(rid, "d8")
    d8 = [v for v in d8 if v != "ninguno"]
    ev["d8"] = {"valores": d8, "origen": o8}
    if d8 and "agnostico" not in d8:
        if p["modelo"] is None:
            return _dec("CONDICIONAL", f"específica de {', '.join(d8)}; el modelo destino aún no está decidido", evidencia=ev,
                        campos=["modelo"])
        if p["modelo"] not in d8:
            return _dec("NO_APLICA", f"específica de {', '.join(d8)} (faceta d8, origen {'/'.join(o8)}); modelo destino "
                                     f"de esta entrega: {p['modelo']}", evidencia=ev, campos=["modelo"])
    # facetas cerradas
    for d, campo_spec in (("d3", "sujetos"), ("d2", "accion"), ("d4", "tratamiento"), ("d1", "rol"), ("d9", "angulo")):
        vals, orig = cl.faceta(rid, d)
        vals = [v for v in vals if v != "ninguno"]
        if not vals:
            continue
        ev[d] = {"valores": vals, "origen": orig}
        pv = p.get(d)
        if pv is None:
            if d in ("d4", "d9"):
                return _dec("CONDICIONAL", f"la regla trata {d}={', '.join(vals)}; el {campo_spec} de esta entrega no está decidido",
                            evidencia=ev, campos=[campo_spec])
            continue
        if d == "d9" and len(vals) > 1:
            continue  # reglas de ángulo en general (varios valores): aplican a cualquier decisión de ángulo
        if pv not in vals:
            if not set(orig) & FUERTES:
                ev.setdefault("en_contra_debil", []).append(f"{d}={','.join(vals)} ({'/'.join(orig)})")
                continue
            return _dec("NO_APLICA", f"faceta {d} ({campo_spec}) de la regla: {', '.join(vals)} (origen {'/'.join(orig)}); "
                                     f"esta entrega: {pv} ({et})", evidencia=ev, campos=[campo_spec])
    if r["fase"] == "QA_RENDER":
        return _dec("NO_APLICA", f"fase QA_RENDER: gobierna la crítica del render de {et}, no el texto del prompt; "
                                 "se aplica en Evaluación visual", evidencia=ev, campos=["fase"])
    if r["fase"] == "PLANEACION" and p["recorrido"] in ("IMAGEN", "CLIP") and r["medio"] in ("TEXTO", "PROCESO"):
        return _dec("NO_APLICA", f"planeación de pieza completa ({r['archivo']}); esta entrega es pieza suelta {p['recorrido']} ({et})",
                    evidencia=ev, campos=["recorrido"])
    dest = destinos(r["texto"])
    if COND.search(r["texto"]):
        return _dec("CONDICIONAL", f"regla condicional: «{r['texto'][:140]}» — resolver contra los datos de {et}",
                    evidencia=ev, destino=dest, inferencia=inferencia)
    if ev.get("en_contra_debil"):
        return _dec("APLICA", f"comparte subproceso {', '.join(sorted(comunes_t))} y caso "
                              f"{'/'.join(sorted(set(casos) & p['casos']))} con {et}; evidencia débil en contra "
                              f"({'; '.join(ev['en_contra_debil'])}) no la descarta: prioridad de revisión semántica",
                    evidencia=ev, destino=dest, inferencia=inferencia)
    razon = f"comparte subproceso {', '.join(sorted(comunes_t))} y caso {'/'.join(sorted(set(casos) & p['casos']))} con {et}"
    if inferencia:
        razon += " · inferencia [A PRUEBA]: no bloquea ni modifica reglas canónicas"
    return _dec("APLICA", razon, evidencia=ev, destino=dest, inferencia=inferencia)


def decidir_todas(reg, compl: dict, perfil: dict) -> dict[str, dict]:
    cl = Clasif(reg, compl)
    dec = {rid: decidir_regla(r, cl, perfil) for rid, r in reg.reglas.items()}
    aplicar_conflictos(dec, perfil)
    return dec


def aplicar_conflictos(dec: dict[str, dict], perfil: dict) -> list[dict]:
    estados = {k: v["estado"] for k, v in dec.items()}
    activos = CF.evaluar(perfil, estados)
    for c in activos:
        lados = {"a": c["a"], "b": c["b"]}
        if not c["resuelto"]:
            for rid in c["a"] + c["b"]:
                if rid in dec and dec[rid]["estado"] in ("APLICA", "CONDICIONAL"):
                    dec[rid] = dict(dec[rid], estado="CONFLICTO", conflicto=c["id"],
                                    razon=f"{c['id']}: {c['descripcion']} Autoridad: {c['autoridad']}. {c['razon']} (entrega: {etiqueta(perfil)})")
            continue
        perdedor = "b" if c["gana"] == "a" else "a"
        for rid in lados[perdedor]:
            if rid in dec and dec[rid]["estado"] in ("APLICA", "CONDICIONAL", "CONFLICTO"):
                dec[rid] = dict(dec[rid], estado="NO_APLICA", conflicto=c["id"], capa=dec[rid]["capa"] + "+conflicto",
                                razon=f"suprimida por {c['id']}: {c['razon']} (autoridad: {c['autoridad']}; entrega: {etiqueta(perfil)})")
        for rid in lados[c["gana"]]:
            if rid in dec and dec[rid]["estado"] == "CONFLICTO":
                dec[rid] = dict(dec[rid], estado="APLICA", conflicto=c["id"], razon=dec[rid]["razon"] + f" · gana en {c['id']}")
    return activos


# --------------------------------------------------------------------------- validación

def anclas_brief(perfil: dict, spec: dict) -> set[str]:
    s = {x.lower() for x in perfil["casos"]} | {"imagen", "video", "still", "clip", "entrega", "brief", "modelo",
                                                  "caso", "recorrido", "fondo", "encuadre", "tratamiento", "sujetos",
                                                  "etapa", "faceta", "pieza", "retrato", "prompt"}
    if perfil.get("modelo"):
        s.add(perfil["modelo"].lower())
    s |= {f"d{i}" for i in range(1, 10)}
    s |= {t.lower() for t in perfil["tareas"]}
    for f in spec["comunes"].values():
        v = f.get("valor")
        if isinstance(v, str) and len(v) < 120:
            s |= {w for w in re.findall(r"[a-záéíóúñ0-9\-]{4,}", v.lower())}
    # palabras del propio brief (≥5 letras) y hechos por AUSENCIA verificables en el brief
    brief = str((spec["comunes"].get("objetivo") or {}).get("valor") or "").lower()
    s |= {w for w in re.findall(r"[a-záéíóúñ]{5,}", brief)}
    if not (spec["comunes"].get("marca") or {}).get("valor"):
        s |= {"sin marca", "no brand", "no hay marca", "marca"}
    if not (spec["comunes"].get("referencias") or {}).get("valor"):
        s |= {"sin referencia", "no reference", "referencias"}
    if not re.search(r"texto|text|logo|tipograf", brief):
        s |= {"sin texto", "no text", "sin copy", "sin logo", "copy"}
    return s


def razon_especifica(razon: str, anclas: set[str]) -> tuple[bool, str]:
    r = (razon or "").strip()
    if len(r) < 20:
        return False, "razón demasiado corta"
    if GENERICAS.match(r):
        return False, "razón genérica"
    low = r.lower()
    if not any(a in low for a in anclas):
        return False, "la razón no cita ningún dato del brief ni del recorrido"
    return True, ""


def validar_lote(solicitados: list[str], respuesta, anclas: set[str]) -> dict:
    """Exactamente los ids pedidos, sin duplicados ni inventados, estados válidos, NO_APLICA con razón específica."""
    errores = []
    items = respuesta.get("decisiones") if isinstance(respuesta, dict) else respuesta
    if not isinstance(items, list):
        return {"ok": False, "errores": ["la respuesta no trae una lista 'decisiones'"], "faltan": list(solicitados),
                "duplicados": [], "inventados": [], "invalidos": []}
    vistos = Counter(str(x.get("id")) for x in items if isinstance(x, dict))
    pedidos = set(solicitados)
    dup = sorted(k for k, n in vistos.items() if n > 1)
    inv = sorted(k for k in vistos if k not in pedidos)
    faltan = sorted(pedidos - set(vistos))
    malos = []
    for x in items:
        if not isinstance(x, dict) or str(x.get("id")) not in pedidos:
            continue
        est = x.get("estado")
        if est not in ESTADOS or est == "PENDIENTE":
            malos.append({"id": x.get("id"), "error": f"estado inválido {est!r}"})
            continue
        if est == "NO_APLICA":
            ok, why = razon_especifica(x.get("razon", ""), anclas)
            if not ok:
                malos.append({"id": x.get("id"), "error": f"NO_APLICA sin razón específica: {why}"})
    if dup:
        errores.append(f"{len(dup)} ids duplicados")
    if inv:
        errores.append(f"{len(inv)} ids inexistentes")
    if faltan:
        errores.append(f"{len(faltan)} ids faltantes")
    if malos:
        errores.append(f"{len(malos)} decisiones inválidas")
    return {"ok": not errores, "errores": errores, "faltan": faltan, "duplicados": dup, "inventados": inv, "invalidos": malos}


def gate_mecanico(reg, dec: dict[str, dict], anclas: set[str]) -> dict:
    """Una decisión por cada id vigente, sin ids ajenos, sin PENDIENTE, sin CONFLICTO abierto,
    CONDICIONAL resuelta, y NO_APLICA con razón específica."""
    ids = set(reg.reglas)
    faltan = sorted(ids - set(dec))
    ajenos = sorted(set(dec) - ids)
    cuenta = Counter(v["estado"] for k, v in dec.items() if k in ids)
    malos_na = [k for k, v in dec.items() if v["estado"] == "NO_APLICA" and not razon_especifica(v.get("razon", ""), anclas)[0]]
    bloqueos = []
    if faltan:
        bloqueos.append(f"{len(faltan)} reglas sin decisión")
    if ajenos:
        bloqueos.append(f"{len(ajenos)} ids que no están en el registro")
    if cuenta.get("PENDIENTE"):
        bloqueos.append(f"{cuenta['PENDIENTE']} PENDIENTE")
    if cuenta.get("CONFLICTO"):
        bloqueos.append(f"{cuenta['CONFLICTO']} en CONFLICTO sin resolver")
    if cuenta.get("CONDICIONAL"):
        bloqueos.append(f"{cuenta['CONDICIONAL']} CONDICIONAL sin resolver")
    if malos_na:
        bloqueos.append(f"{len(malos_na)} NO_APLICA sin razón específica")
    fallidas = [k for k, v in dec.items() if v.get("lote_fallido")]
    if fallidas:
        bloqueos.append(f"{len(fallidas)} reglas en lotes que no validaron (revisión incompleta)")
    return {"total_registro": len(ids), "decididas": len(ids) - len(faltan), "por_estado": dict(cuenta),
            "faltan": faltan[:50], "ajenos": ajenos[:50], "no_aplica_genericas": malos_na[:50],
            "ok": not bloqueos, "bloqueos": bloqueos}


def recibo(reg, dec: dict[str, dict], conflictos: list[dict], extra: dict | None = None) -> dict:
    cuenta = Counter(v["estado"] for v in dec.values())
    motivos = Counter()
    for v in dec.values():
        if v["estado"] == "NO_APLICA":
            r = v["razon"]
            tipo = ("medio" if "de medio" in r else "modelo (d8)" if "específica de" in r else
                    "subproceso/recorrido" if "subprocesos" in r or "planeación" in r else "caso" if "casos de la regla" in r
                    else "NINGUNO" if "NINGUNO" in r else "faceta" if "faceta" in r else "fase QA_RENDER" if "QA_RENDER" in r
                    else "conflicto" if "suprimida" in r else "meta" if "metadato" in r else "otro")
            motivos[tipo] += 1
    obsoletas = [rid for rid, r in reg.reglas.items() if reg.archivos.get(f"{r['skill']}/{r['archivo']}")
                 and reg.archivos.get(f"{r['skill']}/{r['archivo']}") != r.get("sha_archivo")]
    capas = Counter(v["capa"] for v in dec.values())
    return {"registro": reg.version, "total_ids": len(reg.reglas), "decididos": len(dec),
            "por_estado": {e: cuenta.get(e, 0) for e in ESTADOS}, "motivos_descarte": dict(motivos),
            "por_capa": dict(capas), "inferencias_a_prueba": sum(1 for v in dec.values() if v.get("inferencia")),
            "conflictos": conflictos,
            "pendientes": [k for k, v in dec.items() if v["estado"] == "PENDIENTE"][:100],
            "extraccion_no_verificable": obsoletas, **(extra or {})}
