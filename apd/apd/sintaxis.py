"""Ledger de sintaxis: qué requisitos de escritura de secciones aplican a ESTA entrega según
salida (imagen/video), modelo, composición de la imagen (caso, sujetos) o acción del video
(D2, I2V, multi-shot) y rol de las referencias.

Fuente: data/sintaxis_fuente.json — cada requisito con cita literal archivo:línea verificada
(tools/check_citas.py). Muchos de estos requisitos NO están en el registro de 1,398 (el
extractor legacy salta los bloques de código donde viven las plantillas), por eso se
deciden en un ledger propio con el mismo gate: todos decididos, conflictos resueltos.
"""

from __future__ import annotations

import hashlib
import json
import re
from functools import lru_cache

from . import fuentes as F

ARCHIVO = F.DATA / "sintaxis_fuente.json"
MODELO_SX = {"gpt-image-2": "gpt-image-2", "nano-banana-pro": "nano-banana-pro", "nano-banana-2": "nano-banana-2",
             "midjourney": "midjourney", "flux": "flux", "kling": "kling-3", "veo": "veo-3.1", "seedance": "seedance-2.5",
             "hailuo": "hailuo"}
CASO_SX = {"T1": "T1_genesis_rostro", "T2": "T2_cuerpo_con_ref", "T3": "T3_1_persona", "T4": "T4_2_personas_contacto",
           "T5": "T5_edicion", "PROD": "PROD", "GRAF": "GRAF_texto", "MULTI": "MULTI_panel", "LUGAR": "LUGAR_placa",
           "ENSAMBLE": "ENSAMBLE", "MULTITUD": "MULTITUD"}
ACCION_SX = {"A_pose": "A_pose", "B_pico": "B_pico", "C_movimiento": "C_movimiento", "D_luz_clima": "D_luz_clima",
             "E_interaccion": "E_interaccion_dialogo", "F_multitud": "F_multitud"}


@lru_cache(maxsize=1)
def catalogo() -> dict:
    return json.loads(ARCHIVO.read_text(encoding="utf-8"))


def _id(*partes) -> str:
    return "SX-" + hashlib.sha1("\x00".join(str(p) for p in partes).encode()).hexdigest()[:10]


def items() -> list[dict]:
    """Aplana el catálogo en requisitos con id estable."""
    d = catalogo()
    out = []
    for m, spec in d["modelos"].items():
        for grupo in ("secciones", "literales_obligatorios", "prohibido"):
            for i, x in enumerate(spec.get(grupo) or []):
                cita = x.get("cita") or {}
                out.append({"id": _id("modelo", m, grupo, i, cita.get("texto")), "clave": ("modelo", m), "grupo": grupo,
                            "texto": x.get("etiqueta_literal") or x.get("texto") or x.get("contenido"),
                            "detalle": x, "cita": cita, "cuando": x.get("cuando")})
        for grupo in ("negativos", "longitud", "referencias"):
            x = spec.get(grupo)
            if x:
                cita = x.get("cita") or {}
                out.append({"id": _id("modelo", m, grupo, cita.get("texto")), "clave": ("modelo", m), "grupo": grupo,
                            "texto": json.dumps({k: v for k, v in x.items() if k not in ("cita", "citas_adicionales")}, ensure_ascii=False),
                            "detalle": x, "cita": cita})
        for i, x in enumerate(spec.get("parametros_externos") or []):
            cita = x.get("cita") or {}
            out.append({"id": _id("modelo", m, "param", i, x.get("nombre")), "clave": ("modelo", m), "grupo": "parametros_externos",
                        "texto": f"{x.get('nombre')}: {x.get('valores')}", "detalle": x, "cita": cita})
    for sec, clave in (("por_caso_imagen", "caso"), ("por_accion_video", "accion"), ("por_rol_referencia", "rol")):
        for k, lista in d[sec].items():
            for i, x in enumerate(lista):
                cita = x.get("cita") or {}
                out.append({"id": _id(sec, k, i, cita.get("texto")), "clave": (clave, k), "grupo": sec,
                            "texto": x.get("requisito"), "detalle": x, "cita": cita, "origen": x.get("origen")})
    return out


def _cita_txt(c: dict) -> str:
    return (f"{c.get('archivo')}:{c.get('linea_ini')}" if c.get("linea_ini") else str(c.get("archivo"))) if c else "—"


def decidir(perfil: dict, i2v: bool = False, multi_shot: bool = False) -> dict[str, dict]:
    modelo = MODELO_SX.get(perfil.get("modelo") or "", perfil.get("modelo"))
    casos = {CASO_SX[c] for c in perfil["casos"] if c in CASO_SX}
    acc = ACCION_SX.get(perfil.get("d2") or "")
    roles = set(perfil.get("roles") or set())
    medio = "imagen" if perfil["medio"] == "IMAGEN" else "video"
    et = f"{'/'.join(sorted(perfil['casos']))} · {perfil.get('modelo') or 'modelo sin decidir'} · {medio}"
    dec = {}
    for it in items():
        tipo, k = it["clave"]
        if tipo == "modelo":
            ok = k == modelo
            et_lit = ((it["detalle"] or {}).get("etiqueta_literal") or "") if it["grupo"] == "secciones" else ""
            if ok and re.match(r"^Shot \d", et_lit) and not multi_shot:
                dec[it["id"]] = {"estado": "NO_APLICA", "razon": f"sintaxis multi-shot; esta entrega es un solo shot ({et})"}
                continue
            if ok and it["grupo"] == "secciones" and "T5" in perfil["casos"] and et_lit and et_lit not in ("Constraints:",):
                dec[it["id"]] = {"estado": "NO_APLICA", "razon": f"sección de creación {et_lit}; esta entrega es edición T5 "
                                                                 "(Change/Preserve/Constraints, gpt-image.md Editing)"}
                continue
            razon = (f"sintaxis de {k}; esta entrega usa {perfil.get('modelo')}" if not ok else f"modelo destino {k}")
            if ok and it.get("cuando"):
                r = resolver_cuando(it["cuando"], perfil)
                if r is None:
                    dec[it["id"]] = {"estado": "CONDICIONAL", "razon": f"aplica cuando «{it['cuando']}» — resolver para {et}"}
                else:
                    dec[it["id"]] = {"estado": "APLICA" if r[0] else "NO_APLICA", "razon": f"condición «{it['cuando']}»: {r[1]} ({et})"}
                continue
        elif tipo == "caso":
            ok = k in casos and medio == "imagen"
            razon = f"composición {k}; esta entrega es {et}" if not ok else f"composición {k} de esta entrega"
        elif tipo == "accion":
            if k == "i2v_frame_inicial":
                ok = medio == "video" and ("frame_inicial" in roles or i2v)
            elif k == "i2v_frame_final":
                ok = medio == "video" and "frame_final" in roles
            elif k == "multi_shot":
                ok = medio == "video" and multi_shot
            else:
                ok = medio == "video" and k == acc
            razon = f"acción de video {k}; esta entrega es {et}" + (f" (acción {acc})" if acc else "") if not ok else f"acción {k}"
        else:  # rol
            ok = k in roles
            razon = f"rol de referencia {k}; roles de esta entrega: {', '.join(sorted(roles)) or 'ninguno'} ({et})" if not ok else f"rol {k}"
        dec[it["id"]] = {"estado": "APLICA" if ok else "NO_APLICA", "razon": razon}
    return dec


def resolver_cuando(cuando: str, perfil: dict):
    """Condiciones del catálogo que se resuelven con datos de la entrega. None = no resoluble aquí."""
    c = cuando.lower()
    casos = perfil["casos"]
    nref = len(perfil.get("roles") or set() - {"genesis"})
    if re.search(r"edici", c):
        return ("T5" in casos, "la entrega es edición T5" if "T5" in casos else f"la entrega es {'/'.join(sorted(casos))}, no edición")
    if re.search(r"texto", c):
        hay = "GRAF" in casos or bool(perfil.get("texto_en_imagen"))
        return (hay, "hay texto en la imagen" if hay else "no hay texto en la imagen (restricción 'no text')")
    if re.search(r"multi-imagen|refs?\b|referencia", c):
        return (nref > 1, f"{nref} referencias con rol")
    return None


# Conflictos que la entrega puede satisfacer a la vez (ambos lados cumplidos) o cuya autoridad
# depende de un dato de la entrega. Cada uno declara su predicado y su autoridad.
RESOLUCION_ENTREGA = {
    "CF-SX-07": {"si": lambda p, t: "constraints:" in (t or "").lower(),
                 "autoridad": "satisfacción conjunta: el prompt incluye Constraints (obligatorio en gpt-image.md) y P() de SW30 lo admite como opcional"},
    "CF-SX-29": {"si": lambda p, t: bool(p.get("d4")),
                 "autoridad": "flujo-anclas.html D7: 'Rostros documentales: luz dura rasante … Comercial: clean, pareja' — decide D4"},
    "CF-SX-33": {"aplica": lambda p: "T2" in p["casos"]},
}


def conflictos(dec: dict[str, dict], perfil: dict, spec_decisiones: dict | None = None, texto: str | None = None) -> list[dict]:
    """Conflictos del catálogo con ambos lados activos para esta entrega."""
    spec_decisiones = spec_decisiones or {}
    activos_arch = {}
    for it in items():
        if dec.get(it["id"], {}).get("estado") == "APLICA" and it.get("cita"):
            activos_arch.setdefault(it["cita"].get("archivo"), []).append(it["cita"].get("linea_ini"))

    def lado_activo(lado):
        c = (lado or {}).get("cita") or {}
        lineas = activos_arch.get(c.get("archivo"))
        return bool(lineas) and any(abs((l or 0) - (c.get("linea_ini") or 0)) <= 3 for l in lineas)

    out = []
    for i, c in enumerate(catalogo()["conflictos_de_sintaxis"]):
        if not (lado_activo(c.get("lado_a")) and lado_activo(c.get("lado_b"))):
            continue
        cid = f"CF-SX-{i + 1:02d}"
        regla = RESOLUCION_ENTREGA.get(cid, {})
        if regla.get("aplica") and not regla["aplica"](perfil):
            continue
        res = c.get("resolucion_documentada")
        if not res and regla.get("si") and regla["si"](perfil, texto):
            res = {"cita": {"archivo": "apd", "linea_ini": None, "texto": regla["autoridad"]}, "tipo": "entrega"}
        dec_u = spec_decisiones.get(cid)
        out.append({"id": cid, "descripcion": c["descripcion"], "a": _cita_txt((c.get("lado_a") or {}).get("cita")),
                    "b": _cita_txt((c.get("lado_b") or {}).get("cita")),
                    "resuelto": bool(res) or bool(dec_u),
                    "autoridad": (_cita_txt(res.get("cita")) + f" [{res.get('tipo')}] «{(res.get('cita') or {}).get('texto', '')[:160]}»") if res
                    else ("decisión del usuario: " + str(dec_u) if dec_u else "sin resolución documentada: requiere decisión")})
    return out


def gate(dec: dict[str, dict], confl: list[dict]) -> dict:
    from collections import Counter
    c = Counter(v["estado"] for v in dec.values())
    bloqueos = []
    if len(dec) != len(items()):
        bloqueos.append("requisitos de sintaxis sin decisión")
    if c.get("CONDICIONAL"):
        bloqueos.append(f"{c['CONDICIONAL']} requisitos de sintaxis CONDICIONAL sin resolver")
    abiertos = [x["id"] for x in confl if not x["resuelto"]]
    if abiertos:
        bloqueos.append(f"conflictos de sintaxis sin resolver: {', '.join(abiertos)}")
    return {"total": len(items()), "por_estado": dict(c), "ok": not bloqueos, "bloqueos": bloqueos}


def controles_texto(texto: str, dec: dict[str, dict]) -> list[dict]:
    """Verificación mecánica de lo que es mecanizable: etiquetas de sección obligatorias y términos prohibidos."""
    out = []
    low = texto.lower()
    for it in items():
        if dec.get(it["id"], {}).get("estado") != "APLICA":
            continue
        d = it["detalle"]
        if it["grupo"] == "secciones" and d.get("etiqueta_literal") and d.get("obligatoria"):
            clave = re.split(r"\.\.\.|…|\[[a-z_ ]+\]", d["etiqueta_literal"])[0].strip().lower()
            ok = clave in low
            out.append({"id": it["id"], "tipo": "seccion", "ok": ok, "detalle": f"etiqueta {d['etiqueta_literal']!r}",
                        "cita": _cita_txt(it["cita"])})
        if it["grupo"] == "prohibido":
            terminos = [t.strip().strip('"«»').lower() for t in re.split(r",|/", (it["cita"] or {}).get("texto", "")) if 3 <= len(t.strip()) <= 30]
            hallados = [t for t in terminos if re.search(r"\b" + re.escape(t) + r"\b", low)]
            if terminos:
                out.append({"id": it["id"], "tipo": "prohibido", "ok": not hallados, "detalle": f"términos {terminos[:6]} · hallados {hallados}",
                            "cita": _cita_txt(it["cita"])})
    return out
