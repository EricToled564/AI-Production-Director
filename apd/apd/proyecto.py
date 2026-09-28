"""Orquestación de un proyecto: versiones inmutables, recálculo por dependencias,
decisiones humanas, revisión con modelo, auditoría, aprobaciones, feedback dirigido,
evaluación visual y exportación.

Invalidación: cada artefacto lleva el hash de sus entradas. Una versión nueva recalcula
todo, pero sólo cambia (y sólo invalida) lo que cambió de hash: si se edita la edad de
E2, E1/E3/E4/E5 conservan texto, hash, auditoría y aprobación.
"""

from __future__ import annotations

import copy
import io
import json
import re
import threading
import uuid
import zipfile
from functools import lru_cache

from . import auditoria as A
from . import compilador as C
from . import conflictos as CF
from . import politicas as POL
from . import plantilla_brief as PB
from . import flujos as FL
from . import fuentes as F
from . import ledger as L
from . import llm
from . import plan as PL
from . import propuestas as PR
from . import registro as R
from . import revision as RV
from . import spec as S
from . import sintaxis as SX
from . import store as ST

OVERRIDES_ENTREGA = {"medio", "modelo", "referencias", "tipo_tarea", "formato", "calidad", "duracion", "tratamiento",
                     "accion", "angulo", "negativos", "audio", "d1", "d3"}
CASO_AURORA = {"T1": "T1", "T2": "T2", "T3": "T3", "T4": "T4", "T5": "T5", "PROD": "1", "GRAF": "1", "MULTI": "1",
               "LUGAR": "1", "CLIP": "3a"}


_locks: dict[str, threading.RLock] = {}
_locks_guard = threading.Lock()


def _lock(pid: str) -> threading.RLock:
    with _locks_guard:
        return _locks.setdefault(pid, threading.RLock())


def serializado(fn):
    """Leer-modificar-guardar de un proyecto en exclusión mutua: sin esto, una auditoría larga que termina
    después de una firma o una aprobación reescribe la versión y borra lo que se hizo mientras corría
    (lo detectó la prueba de interfaz: firmar durante una auditoría perdía la firma)."""
    import functools

    @functools.wraps(fn)
    def w(pid, *a, **k):
        with _lock(pid):
            return fn(pid, *a, **k)
    return w


@lru_cache(maxsize=1)
def registro() -> R.Registro:
    return R.cargar()


@lru_cache(maxsize=1)
def complemento() -> dict:
    return json.loads((F.DATA / "clasificacion_app.json").read_text(encoding="utf-8"))["complemento"]


def spec_de_entrega(spec: dict, ent: dict) -> dict:
    s = copy.deepcopy(spec)
    for k in OVERRIDES_ENTREGA:
        if k in ent["campos"]:
            s["comunes"][k] = ent["campos"][k]
    return s


# --------------------------------------------------------------------------- creación y recálculo

def nuevo(brief: dict, nombre: str | None = None) -> str:
    spec = S.analizar_determinista(brief)
    # plantilla de brief: el modelo (si hay) y la app infieren cámara, luz, lugar, ángulo… sin preguntar al usuario
    spec, spec["plantilla_info"] = PB.completar(spec, brief, llm.proveedor().disponible())
    estado = {"brief": brief, "brief_hash": F.sha256_text(F.canon_json(brief)), "spec": spec,
              "decisiones_humanas": {}, "aprobaciones": {}, "semantica": {}, "auditorias": {}, "etapas": {},
              "excepciones": {}, "historial_feedback": []}
    estado = recalcular(estado)
    # persistible: sin esto la versión 1 guardaba los resúmenes del ledger pero no las 1,398 decisiones
    return ST.crear_proyecto(nombre or (brief.get("titulo") or brief.get("texto", "")[:60]), persistible(estado))


def recalcular(estado: dict, previo: dict | None = None) -> dict:
    reg, compl = registro(), complemento()
    spec = estado["spec"]
    spec["ambiguedades"] = S.ambiguedades(spec)
    plan = PL.construir(spec, {k: v for k, v in estado.get("etapas", {}).items() if v.get("aprobada")})
    estado["plan"] = plan
    estado["preflight"] = S.preflight(spec)
    gates_abiertos = plan["bloqueado_por_gates"]
    ledgers, entregas = {}, {}
    for ent in spec["entregas"]:
        se = spec_de_entrega(spec, ent)
        perfil = L.perfil_de(se, plan, ent)
        clave = L.clave_perfil(perfil)
        if clave not in ledgers:
            dec = L.decidir_todas(reg, compl, perfil)
            ck = clave_revision(se, perfil, clave)
            cache_modelo = ST.ledger_get(ck, reg.version, "modelo")
            herencia = None
            if cache_modelo:
                for rid, x in cache_modelo.items():
                    if rid in dec:
                        dec[rid] = x
            elif previo:
                herencia = _heredar_revision(previo, ent, se, perfil, ck, dec, estado)
            if cache_modelo or herencia:
                # el catálogo de conflictos (autoridad documentada o decisión del director) se aplica también sobre
                # decisiones revisadas por modelo/externo/heredadas; sin esto una revisión lo saltaba en silencio
                L.aplicar_conflictos(dec, dict(perfil, _conflictos=None))
            if clave not in estado["decisiones_humanas"] and previo:
                # la clave del perfil cambió sin cambiar el perfil (p.ej. formato de clave): las decisiones del director
                # se migran; nunca se pierden en silencio
                pa = (previo.get("entregas", {}).get(ent["id"]) or {}).get("perfil")
                pl = (previo.get("_ledgers_completos") or {}).get(pa)
                norm = lambda d: {k: (sorted(v) if isinstance(v, (set, list)) else v) for k, v in d.items() if k not in L.FUERA_DE_CLAVE}
                if pa in estado["decisiones_humanas"] and pl and norm(pl["perfil"]) == norm({k: v for k, v in perfil.items() if k != "decisiones"}):
                    estado["decisiones_humanas"][clave] = estado["decisiones_humanas"][pa]
            for rid, h in (estado["decisiones_humanas"].get(clave) or {}).items():
                if rid in dec:
                    prev = dec[rid]
                    dec[rid] = dict(prev, **h, capa="humano",
                                    discrepancia={"antes": prev["estado"], "capa_antes": prev["capa"]} if h["estado"] != prev["estado"] else None)
            conflictos = CF.evaluar(perfil, {k: v["estado"] for k, v in dec.items()},
                                    {k: v["conflicto"] for k, v in dec.items() if v.get("conflicto")})
            anclas = L.anclas_brief(perfil, se)
            ledgers[clave] = {"perfil": {k: (sorted(v) if isinstance(v, set) else v) for k, v in perfil.items() if k != "decisiones"},
                              "etiqueta": L.etiqueta(perfil), "decisiones": dec, "conflictos": conflictos,
                              "gate": L.gate_mecanico(reg, dec, anclas),
                              "hash": F.sha256_text(F.canon_json({k: [v["estado"], v.get("razon", "")] for k, v in dec.items()})),
                              "revision_modelo": bool(cache_modelo), "clave_revision": ck, "herencia": herencia,
                              "recibo": L.recibo(reg, dec, conflictos)}
        info = {"perfil": clave, "casos": ent["casos"], "vinculos": ent.get("vinculos", {})}
        faltan = S.preflight_entrega(spec, ent)["faltan"]
        if gates_abiertos:
            info["compilado"] = None
            info["bloqueo"] = "gates del recorrido sin aprobar: " + ", ".join(gates_abiertos)
        elif faltan:
            info["compilado"] = None
            info["bloqueo"] = "preflight: faltan " + ", ".join(faltan)
        else:
            comp = C.compilar(se, ent, ledgers[clave]["decisiones"], reg, f"{ent['id']}")
            info["compilado"] = comp
        info["sintaxis"] = sintaxis_entrega(spec, se, plan, ent, (info.get("compilado") or {}).get("texto"))
        entregas[ent["id"]] = info
    estado["ledgers"] = {k: _ledger_ligero(v) for k, v in ledgers.items()}
    estado["_ledgers_completos"] = ledgers
    estado["entregas"] = entregas
    if previo:
        estado["diferencias"] = comparar(previo, estado)
    return estado


def _heredar_revision(previo, ent, se, perfil, ck, dec, estado):
    """El contexto del brief cambió y ya no hay revisión (modelo/externa) para la clave nueva. En vez de caer en
    silencio a la capa determinista, se arrastran las decisiones revisadas de la versión anterior marcadas como
    heredadas, y la entrega queda bloqueada hasta que alguien vuelva a revisar o el director confirme que los
    campos cambiados no alteran la aplicabilidad de las reglas."""
    previos = previo.get("_ledgers_completos") or {}
    pl = previos.get(L.clave_perfil(perfil))
    if pl is None:  # misma entrega con perfil equivalente salvo decisiones de conflicto (o clave de una versión anterior)
        pa = previos.get((previo.get("entregas", {}).get(ent["id"]) or {}).get("perfil"))
        norm = lambda d: {k: (sorted(v) if isinstance(v, (set, list)) else v) for k, v in d.items() if k not in L.FUERA_DE_CLAVE}
        if pa and norm(pa["perfil"]) == norm({k: v for k, v in perfil.items() if k != "decisiones"}):
            pl = pa
    if pl is None:
        return None
    revisadas = {k: v for k, v in pl["decisiones"].items() if str(v.get("capa", "")).split("+")[0].split(":")[0] in ("modelo", "externo")}
    if not revisadas:
        return None
    ent_prev = next((x for x in previo["spec"]["entregas"] if x["id"] == ent["id"]), None)
    ctx = lambda s: json.loads(RV._resumen_perfil(s, perfil, None))["campos"]
    antes = ctx(spec_de_entrega(previo["spec"], ent_prev)) if ent_prev else {}
    ahora = ctx(se)
    cambiados = sorted(k for k in set(antes) | set(ahora) if antes.get(k) != ahora.get(k))
    origen = (pl.get("herencia") or {}).get("origen") or pl.get("clave_revision")
    for rid, x in revisadas.items():
        if rid in dec:
            dec[rid] = dict(x, capa=x["capa"] if x["capa"].endswith("+heredada") else x["capa"] + "+heredada")
    ph = pl.get("herencia") or {}
    if ph and not ph.get("confirmada"):  # herencia previa sin confirmar: sus cambios de contexto siguen pendientes
        cambiados = sorted(set(cambiados) | set(ph.get("campos_cambiados") or []))
    conf = (estado.get("herencias_confirmadas") or {}).get(ck)
    if not conf:  # U-2026-09-28-CAMBIO-QUIRURGICO: las decisiones de niveles anteriores quedan fijas, no se re-revisan
        conf = {"autor": POL.CAMBIO_QUIRURGICO["id"], "fecha": ST.ahora(),
                "nota": "niveles anteriores fijos (director): la clasificación de reglas se hereda; cambiaron "
                        + (", ".join(cambiados) or "sólo la clave del perfil")}
    if not cambiados and not conf:  # contexto idéntico: la revisión sigue valiendo tal cual
        conf = {"autor": "app", "nota": "contexto del brief idéntico; sólo cambió la clave del perfil o una decisión de conflicto "
                                        "(que se aplica encima de la revisión)", "fecha": ST.ahora()}
    if (pl.get("herencia") or {}).get("confirmada") and not cambiados:
        conf = pl["herencia"]["confirmada"]
    return {"origen": origen, "clave_actual": ck, "decisiones": len(revisadas), "campos_cambiados": cambiados,
            "confirmada": conf}


@serializado
def confirmar_herencia(pid, perfil: str, autor: str, nota: str) -> dict:
    """El director confirma que los campos cambiados no alteran qué reglas aplican: la revisión heredada vale."""
    if not (autor or "").strip() or len((nota or "").strip()) < 20:
        raise ValueError("confirmar la herencia exige autor y una nota de al menos 20 caracteres sobre los campos cambiados")
    n, e = cargar(pid)
    led = e["_ledgers_completos"].get(perfil)
    if not led or not led.get("herencia"):
        raise ValueError("este perfil no tiene una revisión heredada pendiente")
    h = led["herencia"]

    def mutar(est):
        est.setdefault("herencias_confirmadas", {})[h["clave_actual"]] = {
            "autor": autor, "nota": nota, "fecha": ST.ahora(), "origen": h["origen"], "campos_cambiados": h["campos_cambiados"]}
    return nueva_version(pid, mutar, autor, f"confirma revisión heredada ({len(h['campos_cambiados'])} campos de contexto)")


def sintaxis_entrega(spec, se, plan, ent, texto):
    perfil = L.perfil_de(se, plan, ent)
    roles = perfil["roles"]
    d = SX.decidir(perfil, i2v=bool(roles & {"frame_inicial"}), multi_shot=bool(ent["campos"].get("multi_shot")))
    for sid, h in ((spec.get("decisiones_sintaxis") or {}).get(ent["id"]) or {}).items():
        if sid in d:
            d[sid] = dict(h, capa="humano")
    cf = SX.conflictos(d, perfil, spec.get("decisiones"), texto)
    return {"decisiones": d, "conflictos": cf, "gate": SX.gate(d, cf),
            "controles": SX.controles_texto(texto, d) if texto else [],
            "aplica": [dict(id=it["id"], grupo=it["grupo"], clave=list(it["clave"]), texto=it["texto"], cita=it["cita"])
                       for it in SX.items() if d[it["id"]]["estado"] == "APLICA"]}


def clave_revision(se, perfil, clave) -> str:
    """Una revisión (modelo o externa) vale para este perfil Y este contexto de brief: nunca se reutiliza
    entre proyectos con otro brief aunque el perfil coincida."""
    return f"{clave}:{F.sha256_text(RV._resumen_perfil(se, perfil, None))[:12]}"


def _ledger_ligero(l):
    return {k: v for k, v in l.items() if k != "decisiones"} | {"n": len(l["decisiones"])}


def persistible(estado: dict) -> dict:
    e = dict(estado)
    completos = e.pop("_ledgers_completos", None)
    if completos:
        e["ledgers_decisiones"] = {k: v["decisiones"] for k, v in completos.items()}
    return e


def cargar(pid: str, n: int | None = None) -> tuple[int, dict]:
    n, e = ST.version(pid, n)
    dec = e.pop("ledgers_decisiones", {})
    e["_ledgers_completos"] = {k: dict(e["ledgers"][k], decisiones=v) for k, v in dec.items() if k in e["ledgers"]}
    return n, e


def guardar(pid: str, estado: dict, autor: str, nota: str) -> int:
    return ST.guardar_version(pid, persistible(estado), autor, nota)


@serializado
def nueva_version(pid: str, mutar, autor: str, nota: str) -> dict:
    n, prev = cargar(pid)
    est = copy.deepcopy(prev)
    est.pop("diferencias", None)
    mutar(est)
    est = recalcular(est, previo=prev)
    # U-2026-09-28-CAMBIO-QUIRURGICO: la auditoría determinista se repite siempre; la revisión semántica y la aprobación
    # de redacción se heredan en un cambio menor y sólo se reabren en lo que tocó un cambio dramático
    cambios = {}
    for eid, info in est["entregas"].items():
        h = (info.get("compilado") or {}).get("hash")
        pinfo = (prev["entregas"].get(eid) or {})
        ph = (pinfo.get("compilado") or {}).get("hash")
        cambio = None
        if h and ph and h != ph:
            cambio = POL.clasificar_cambio(_campos_entrega(prev["spec"], eid), _campos_entrega(est["spec"], eid),
                                           {b["id"]: b.get("texto") for b in pinfo["compilado"]["bloques"]},
                                           {b["id"]: b.get("texto") for b in info["compilado"]["bloques"]})
            cambios[eid] = cambio
        for campo in ("auditorias", "semantica", "aprobaciones"):
            x = est[campo].get(eid)
            if not x or x.get("texto_hash") == h:
                continue
            heredable = cambio and x.get("texto_hash") == ph and not x.get("invalidada")
            if campo == "semantica" and heredable:
                est[campo][eid] = _heredar_semantica(x, h, ph, cambio, info["compilado"], n + 1)
            elif campo == "aprobaciones" and heredable and cambio["tipo"] == "menor":
                est[campo][eid] = dict(x, texto_hash=h, heredada={"de": ph, "version": n + 1, "bloques": cambio["bloques"],
                                                                  "politica": cambio["politica"]})
            else:
                est[campo][eid] = dict(x, invalidada=True, invalidada_en=n + 1)
    if est.get("diferencias") is not None:
        est["diferencias"]["cambios"] = cambios
    nn = guardar(pid, est, autor, nota)
    return {"version": nn, "diferencias": est.get("diferencias")}


def _campos_entrega(spec: dict, eid: str) -> dict:
    ent = next((x for x in spec["entregas"] if x["id"] == eid), None) or {"campos": {}}
    out = {k: v.get("valor") for k, v in spec["comunes"].items()}
    out.update({k: v.get("valor") for k, v in ent["campos"].items()})
    return out


def _heredar_semantica(x: dict, h: str, ph: str, cambio: dict, comp: dict, version: int) -> dict:
    """Pasa la revisión semántica al texto nuevo. Pendientes: los NO_CUMPLE abiertos del bloque cambiado (la corrección
    se verifica) y, si el cambio es dramático, todas las reglas que satisfacen los bloques cambiados."""
    cambiados = set(cambio["bloques"])
    en_cambio = lambda v: any(b in str((v or {}).get("bloque", "")) for b in cambiados)
    ver = dict(x.get("veredictos") or {})
    pend = {k for k in x.get("no_cumple_abiertos", []) if en_cambio(ver.get(k))}
    if cambio["tipo"] == "dramatico":
        pend |= {r for b in comp["bloques"] if b["id"] in cambiados for r in b.get("satisface", [])}
    for k in pend:
        ver.pop(k, None)
    return dict(x, texto_hash=h, veredictos=ver, completo=not pend, pendientes=sorted(pend),
                no_cumple_abiertos=[k for k in x.get("no_cumple_abiertos", []) if k not in pend],
                heredada={"de": ph, "version": version, "tipo": cambio["tipo"], "bloques": cambio["bloques"],
                          "motivos": cambio["motivos"], "politica": cambio["politica"]},
                resumen=(x.get("resumen", "") + f" · heredada ({cambio['tipo']}, bloques {', '.join(cambio['bloques'])})"
                         + (f" · {len(pend)} reglas pendientes de revisar" if pend else "")))


def comparar(a: dict, b: dict) -> dict:
    """Antes/después: campos, reglas con estado distinto, bloques regenerados, aprobaciones invalidadas."""
    def campos(s):
        out = {f"comunes.{k}": v.get("valor") for k, v in s["spec"]["comunes"].items()}
        for e in s["spec"]["entregas"]:
            out |= {f"{e['id']}.{k}": v.get("valor") for k, v in e["campos"].items()}
        return out
    ca, cb = campos(a), campos(b)
    cambios_campos = sorted(k for k in set(ca) | set(cb) if ca.get(k) != cb.get(k))
    reglas = {}
    la, lb = a.get("_ledgers_completos", {}), b.get("_ledgers_completos", {})
    for eid, info in b["entregas"].items():
        pa = (a["entregas"].get(eid) or {}).get("perfil")
        pb = info["perfil"]
        if pa in la and pb in lb:
            da, db = la[pa]["decisiones"], lb[pb]["decisiones"]
            ch = [{"id": k, "antes": da[k]["estado"], "despues": db[k]["estado"]} for k in db if k in da and da[k]["estado"] != db[k]["estado"]]
            if ch:
                reglas[eid] = ch
    bloques, textos = {}, {}
    for eid, info in b["entregas"].items():
        ta = ((a["entregas"].get(eid) or {}).get("compilado") or {})
        tb = info.get("compilado") or {}
        if ta.get("hash") != tb.get("hash"):
            textos[eid] = {"antes": ta.get("hash"), "despues": tb.get("hash")}
            ba = {x["id"]: x.get("texto") for x in ta.get("bloques", [])}
            bb = {x["id"]: x.get("texto") for x in tb.get("bloques", [])}
            bloques[eid] = sorted(k for k in set(ba) | set(bb) if ba.get(k) != bb.get(k))
    invalidadas = [eid for eid, x in b.get("aprobaciones", {}).items() if x.get("invalidada")]
    heredadas = {k: {kk: vv for kk, vv in v["herencia"].items()} for k, v in lb.items() if v.get("herencia")}
    return {"campos": cambios_campos, "perfiles_cambiados": sorted(eid for eid in b["entregas"] if (a["entregas"].get(eid) or {}).get("perfil") != b["entregas"][eid]["perfil"]),
            "reglas_con_estado_distinto": reglas, "textos_cambiados": textos, "bloques_regenerados": bloques,
            "aprobaciones_invalidadas": invalidadas, "revisiones_heredadas": heredadas,
            "entregas_intactas": sorted(eid for eid in b["entregas"] if eid not in textos)}


def _texto_bloque(b):
    return json.dumps(b["segments"], sort_keys=True, ensure_ascii=False)


# --------------------------------------------------------------------------- ediciones

def cambiar_campos(pid, cambios, autor="usuario", nota="edición de campos"):
    def m(e):
        e["spec"], _ = S.aplicar_cambios(e["spec"], cambios, autor)
    return nueva_version(pid, m, autor, nota)


def aceptar_propuestas(pid, rutas: list[str] | None = None, autor="usuario"):
    n, e = cargar(pid)
    props = PR.proponer(e["spec"])
    if rutas is not None:
        props = [p for p in props if p["ruta"] in rutas]

    def m(est):
        est["spec"], _ = PR.aceptar(est["spec"], props, autor)
    return nueva_version(pid, m, autor, f"aceptar {len(props)} propuestas")


def decidir_reglas(pid, clave: str, decisiones: dict[str, dict], autor="usuario"):
    """Decisión humana sobre reglas de un perfil: {rid: {estado, razon, destino?}}."""
    n, e = cargar(pid)
    reg = registro()
    perfil_spec = e["ledgers"][clave]["perfil"]
    anclas = L.anclas_brief({**perfil_spec, "casos": set(perfil_spec["casos"]), "tareas": set(perfil_spec["tareas"])}, e["spec"])
    for rid, d in decisiones.items():
        if rid not in reg.reglas:
            raise ValueError(f"id inexistente: {rid}")
        if d["estado"] not in L.ESTADOS or d["estado"] == "PENDIENTE":
            raise ValueError(f"{rid}: estado inválido")
        if d["estado"] == "NO_APLICA":
            ok, why = L.razon_especifica(d.get("razon", ""), anclas)
            if not ok:
                raise ValueError(f"{rid}: NO_APLICA sin razón específica ({why})")

    def m(est):
        hum = est["decisiones_humanas"].setdefault(clave, {})
        for rid, d in decisiones.items():
            hum[rid] = {"estado": d["estado"], "razon": d.get("razon", ""), "destino": d.get("destino") or [],
                        "autor": autor, "fecha": ST.ahora()}
    return nueva_version(pid, m, autor, f"{len(decisiones)} decisiones humanas de reglas")


def resolver_conflicto(pid, cid: str, gana: str, razon: str, autor="usuario"):
    if gana not in ("a", "b"):
        raise ValueError("gana debe ser 'a' o 'b'")
    if len((razon or "").strip()) < 15:
        raise ValueError("resolver un conflicto exige una razón concreta (≥15 caracteres) que queda registrada")
    if cid not in {c["id"] for c in CF.CATALOGO}:
        raise ValueError(f"conflicto desconocido: {cid}")

    def m(est):
        est["spec"].setdefault("decisiones", {})[cid] = gana
        est["spec"].setdefault("decisiones_razon", {})[cid] = {"razon": razon, "autor": autor, "fecha": ST.ahora()}
    return nueva_version(pid, m, autor, f"resolver {cid} → {gana}")


def aprobar_gate(pid, gate: str, artefacto: str = "", autor="usuario"):
    def m(est):
        est.setdefault("etapas", {})[gate] = {"aprobada": True, "autor": autor, "fecha": ST.ahora(),
                                              "artefacto_hash": F.sha256_text(artefacto) if artefacto else None,
                                              "artefacto": artefacto[:20000]}
    return nueva_version(pid, m, autor, f"OK de etapa {gate}")


# --------------------------------------------------------------------------- modelo: revisión por lotes

_trabajos: dict[str, dict] = {}


def trabajo(tid):
    return _trabajos.get(tid)


def revisar_con_modelo(pid, en_hilo=True) -> str:
    """Revisa con el modelo los ids que la selección mecánica dejó abiertos (APD_REVISION=todas: todos los del medio).
    Reanudable: los lotes válidos no se repiten."""
    if not llm.proveedor().disponible():
        raise llm.SinModelo(llm.estado()["motivo"])
    tid = uuid.uuid4().hex[:8]
    _trabajos[tid] = {"estado": "EN_CURSO", "progreso": [], "pid": pid}

    def run():
        try:
            n, e = cargar(pid)
            reg = registro()
            res = {}
            for clave, led in e["_ledgers_completos"].items():
                ent = next(x for x in e["spec"]["entregas"] if e["entregas"][x["id"]]["perfil"] == clave)
                se = spec_de_entrega(e["spec"], ent)
                perfil = L.perfil_de(se, e["plan"], ent)
                dec = copy.deepcopy(led["decisiones"])
                ck = clave_revision(se, perfil, clave)
                prov = llm.proveedor()
                r = RV.revisar_ledger(reg, se, perfil, ent, dec, f"{ck}:{prov.nombre}:{prov.modelo}", pid,
                                      progreso=lambda p, c=clave: _trabajos[tid]["progreso"].append({"perfil": c, **p}), excluir=excluidas_por_medio(perfil))
                res[clave] = r
                if r["completo"]:
                    ST.ledger_put(ck, reg.version, "modelo", {k: v for k, v in dec.items() if v.get("capa") == "modelo"})
            _trabajos[tid]["resultado"] = res
            nueva_version(pid, lambda est: None, "modelo", "revisión de reglas por lotes")
            _trabajos[tid]["estado"] = "COMPLETO" if all(r["completo"] for r in res.values()) else "INCOMPLETO"
        except Exception as ex:
            _trabajos[tid].update(estado="ERROR", error=f"{type(ex).__name__}: {ex}")
    if en_hilo:
        threading.Thread(target=run, daemon=True).start()
    else:
        run()
    return tid


# --------------------------------------------------------------------------- auditoría

@serializado
def auditar(pid, originales=True) -> dict:
    n, e = cargar(pid)
    reg = registro()
    out = {}
    for ent in e["spec"]["entregas"]:
        info = e["entregas"][ent["id"]]
        comp = info.get("compilado")
        if not comp:
            out[ent["id"]] = {"bloqueo": info.get("bloqueo")}
            continue
        se = spec_de_entrega(e["spec"], ent)
        perfil = L.perfil_de(se, e["plan"], ent)
        perfil["_conflictos"] = e["ledgers"][info["perfil"]]["conflictos"]
        dec = e["_ledgers_completos"][info["perfil"]]["decisiones"]
        caso = CASO_AURORA.get(ent["casos"][0], "1")
        roles_c = {(r or {}).get("rol") for r in (se["comunes"]["referencias"]["valor"] or [])}
        if se["comunes"]["medio"]["valor"] == "imagen" and not (roles_c - {None, "genesis"}):
            caso = "1"  # génesis sin referencias: flujo-anclas A7 'aurora caso 1 génesis o caso 2 ancla con refs'
        if ent["casos"][0] == "CLIP":
            caso = "3b" if "frame_final" in roles_c else ("3a" if "frame_inicial" in roles_c else None)
        a = A.auditar(comp, se, ent, dec, reg, perfil, caso, correr_originales=originales, semantica=e["semantica"].get(ent["id"]))
        sx = info.get("sintaxis") or {}
        a["controles"].append({"id": "sintaxis_ledger", "ok": sx.get("gate", {}).get("ok", False),
                               "detalle": "; ".join(sx.get("gate", {}).get("bloqueos", [])) or
                               f"{sx.get('gate', {}).get('total')} requisitos de sintaxis decididos ({sx.get('gate', {}).get('por_estado')})",
                               "obligatorio": True, "fuente": "data/sintaxis_fuente.json (citas verificadas)"})
        malos = [c for c in sx.get("controles", []) if not c["ok"]]
        a["controles"].append({"id": "sintaxis_texto", "ok": not malos, "obligatorio": True,
                               "detalle": "; ".join(f"{c['tipo']} {c['detalle']} ({c['cita']})" for c in malos) or
                               f"{len(sx.get('controles', []))} verificaciones de sintaxis mecánicas pasan",
                               "fuente": "secciones obligatorias y términos prohibidos del modelo destino"})
        a["fecha"] = ST.ahora()
        a["version"] = n
        out[ent["id"]] = a
        e["auditorias"][ent["id"]] = a
    ST.reemplazar_version(pid, n, persistible(e))
    ST.evento(pid, "auditoria", {"version": n, "entregas": list(out)})
    return out


def semantica_modelo(pid, eid, en_hilo=True) -> str:
    if not llm.proveedor().disponible():
        raise llm.SinModelo(llm.estado()["motivo"])
    tid = uuid.uuid4().hex[:8]
    _trabajos[tid] = {"estado": "EN_CURSO", "progreso": [], "pid": pid}

    def run():
        try:
            n, e = cargar(pid)
            info = e["entregas"][eid]
            comp = info["compilado"]
            dec = e["_ledgers_completos"][info["perfil"]]["decisiones"]
            aplic = [k for k, v in dec.items() if v["estado"] == "APLICA"]
            mapa = [{"bloque": b["id"], "slot": b["slot"], "campos": b["campos"], "satisface": b["satisface"][:80]} for b in comp["bloques"]]
            r = RV.revisar_semantica(registro(), comp["texto"], mapa, aplic, f"{pid}-{eid}-{comp['hash'][:10]}", pid,
                                     progreso=lambda p: _trabajos[tid]["progreso"].append(p))
            nc = [k for k, v in r["veredictos"].items() if v["veredicto"] == "NO_CUMPLE"]
            na = [k for k, v in r["veredictos"].items() if v["veredicto"] == "NO_APLICA_REALMENTE"]
            with _lock(pid):
                n2, e2 = cargar(pid)
                e2["semantica"][eid] = {"revisor": "modelo", "modelo": r["modelo"], "texto_hash": comp["hash"], "completo": r["completo"],
                                        "veredictos": r["veredictos"], "no_cumple_abiertos": nc, "cuestionadas": na, "uso": r["uso"],
                                        "resumen": f"{len(r['veredictos'])} reglas revisadas · {len(nc)} NO_CUMPLE · {len(na)} cuestionadas"}
                ST.reemplazar_version(pid, n2, persistible(e2))
            _trabajos[tid]["estado"] = "COMPLETO"
        except Exception as ex:
            _trabajos[tid].update(estado="ERROR", error=f"{type(ex).__name__}: {ex}")
    if en_hilo:
        threading.Thread(target=run, daemon=True).start()
    else:
        run()
    return tid


@serializado
def semantica_humana(pid, eid, firmante: str, nota: str) -> dict:
    """El director firma que revisó la correspondencia regla ↔ texto de este hash. Queda como
    'REVISADA_HUMANO', distinto de la revisión por modelo."""
    if not firmante.strip() or len(nota.strip()) < 10:
        raise ValueError("la revisión humana exige nombre y una nota de al menos 10 caracteres")
    n, e = cargar(pid)
    comp = e["entregas"][eid]["compilado"]
    previa = e["semantica"].get(eid)
    abiertos = previa.get("no_cumple_abiertos", []) if previa and previa.get("texto_hash") == comp["hash"] else []
    e["semantica"][eid] = {"revisor": "humano", "firmante": firmante, "nota": nota, "texto_hash": comp["hash"], "completo": True,
                           # la firma no borra hallazgos de otro revisor sobre el mismo texto: siguen abiertos
                           "no_cumple_abiertos": abiertos, "previa": previa if abiertos else None,
                           "veredictos": (previa or {}).get("veredictos") if abiertos else None,
                           "disputados": (previa or {}).get("disputados", {}) if abiertos else {},
                           "fecha": ST.ahora(), "resumen": f"revisión humana de {firmante}"
                           + (f" · {len(abiertos)} NO_CUMPLE de {previa['revisor']} siguen abiertos" if abiertos else "")}
    ST.reemplazar_version(pid, n, persistible(e))
    ST.evento(pid, "semantica_humana", {"entrega": eid, "firmante": firmante, "hash": comp["hash"]})
    return e["semantica"][eid]


@serializado
def aprobar_redaccion(pid, eid, texto_hash: str, autor="usuario") -> dict:
    n, e = cargar(pid)
    comp = e["entregas"][eid]["compilado"]
    if not comp or comp["hash"] != texto_hash:
        raise ValueError("el hash no corresponde al texto vigente: no se aprueba un texto distinto al mostrado")
    e["aprobaciones"][eid] = {"texto_hash": texto_hash, "autor": autor, "fecha": ST.ahora(), "version": n}
    ST.reemplazar_version(pid, n, persistible(e))
    ST.evento(pid, "aprobacion", {"entrega": eid, "hash": texto_hash})
    return e["aprobaciones"][eid]


def liberacion(e: dict, eid: str, visual=None) -> dict:
    comp = e["entregas"][eid].get("compilado")
    if not comp:
        return {"liberable": False, "bloqueos": [e["entregas"][eid].get("bloqueo", "sin compilar")], "niveles": A._niveles(None, None, None, visual)}
    lib = A.estado_liberacion(e["auditorias"].get(eid) if not (e["auditorias"].get(eid) or {}).get("invalidada") else None,
                              comp["hash"], e["semantica"].get(eid), e["aprobaciones"].get(eid), visual,
                              e.get("excepciones", {}).get(eid))
    h = (e["_ledgers_completos"].get(e["entregas"][eid]["perfil"]) or {}).get("herencia") if e.get("_ledgers_completos") else \
        (e["ledgers"].get(e["entregas"][eid]["perfil"]) or {}).get("herencia")
    if h and not h.get("confirmada"):
        lib["liberable"] = False
        lib["bloqueos"].insert(0, f"revisión de reglas heredada de otro contexto ({h['decisiones']} decisiones; cambiaron "
                                  f"{', '.join(h['campos_cambiados']) or 'campos'}): volver a revisar o confirmar que no altera la aplicabilidad")
        lib["niveles"]["cobertura"]["estado"] = "HEREDADA_SIN_CONFIRMAR"
    return lib


def copiar(pid, eid) -> dict:
    n, e = cargar(pid)
    vis = [v for v in ST.visual_list(pid) if v["entrega_id"] == eid]
    lib = liberacion(e, eid, vis)
    comp = e["entregas"][eid].get("compilado") or {}
    return {"liberable": lib["liberable"], "bloqueos": lib["bloqueos"], "texto": comp.get("texto") if lib["liberable"] else None,
            "hash": comp.get("hash"), "hash_auditado": (e["auditorias"].get(eid) or {}).get("texto_hash")}


def regenerar_por_longitud(pid, eid) -> dict:
    """Política U-2026-09-28-LONGITUD: si el texto supera 2× el máximo, se regenera acortando los campos
    creativos (con modelo) o se señalan los bloques más largos para editarlos (sin modelo). Nunca se recorta
    el texto final a mano."""
    n, e = cargar(pid)
    comp = e["entregas"][eid]["compilado"]
    bloques = sorted(({"bloque": b["id"], "palabras": len(b["texto"].split()), "campos": b["campos"]} for b in comp["bloques"]),
                     key=lambda x: -x["palabras"])
    if not llm.proveedor().disponible():
        return {"regenerado": False, "motivo": llm.estado()["motivo"], "bloques_mas_largos": bloques[:3],
                "accion": "edite los campos de esos bloques en Especificación; la app recompila y reaudita"}
    ent = next(x for x in e["spec"]["entregas"] if x["id"] == eid)
    abiertos = [f"{eid}.{k}" for k, f in ent["campos"].items() if f.get("origen", "").startswith(("modelo", "propuesta_creativa"))]
    props = RV.proponer_creativo(e["spec"], abiertos)
    r = cambiar_campos(pid, [{"ruta": p["ruta"], "valor": p["valor"], "origen": "modelo:acortar"} for p in props], "modelo", "regenerar por longitud")
    return {"regenerado": True, "cambios": props, "diferencias": r["diferencias"]}


# --------------------------------------------------------------------------- feedback dirigido

FEEDBACK = [
    {"id": "render", "re": r"render|pl[aá]stic|cgi|\b3d\b|artificial|ia\b|ai[- ]look|parece (?:de )?ia|maniqu|mu[ñn]eco|piel perfecta|retocad",
     "contratos": ["comunes.tratamiento", "comunes.luz", "comunes.textura", "comunes.restricciones"],
     "reglas_re": r"skin|piel|plastic|pl[aá]stic|retouch|render|masterpiece|8k|hyperreal|texture|poro",
     "sugerencia": {"comunes.textura": "Natural skin texture with visible pores, fine vellus hair and slight tone variation; no retouching, no skin smoothing",
                    "comunes.restricciones_extra": "no glamorization, no heavy retouching, no studio gloss"},
     "fuentes": ["video/references/fixes-and-skeletons.md:119-125 'Weird AI-looking faces … Use production language … natural skin texture'",
                 "image/references/gpt-image.md:128-133 Photoreal Editorial: 'Constraints: no glamorization, no heavy retouching, no studio gloss'",
                 "produccion-visual-sw30 T1: light_hard/skin_doc (sólo si D4 = documental)"]},
    {"id": "ojos", "re": r"ojos?|mirada|estrabism|bizco|eyes?|gaze|pupil",
     "contratos": ["comunes.foco", "comunes.angulo", "comunes.encuadre", "comunes.camara"],
     "reglas_re": r"eye|ojo|gaze|mirada|face|rostro",
     "sugerencia": {"comunes.foco": "Both eyes in sharp focus, looking together straight into the lens"},
     "fuentes": ["SW30 R12 'Edit, don't re-roll': si el render es ≥80% correcto, corregir los ojos con una edición T5 puntual",
                 "SW30 R14: inspección al 100% de rostros antes de presentar"],
     "limite": "El texto no controla físicamente la alineación de los ojos: la corrección fiable es una edición T5 sobre el render (Change: eyes / Preserve: todo lo demás)."},
    {"id": "identidad", "re": r"identidad|no se parece|otra persona|cambi[oó] (?:la )?cara|continuidad|consisten",
     "contratos": ["comunes.referencias", "E*.rasgos"], "reglas_re": r"identity|identidad|same face|reference|referencia",
     "sugerencia": {}, "fuentes": ["DECISIONES.md #3 (identidad por rol de referencia)", "SW30 R5 herencia mínima"]},
    {"id": "fondo", "re": r"fondo|background", "contratos": ["comunes.fondo"], "reglas_re": r"background|fondo", "sugerencia": {}, "fuentes": []},
    {"id": "encuadre", "re": r"encuadre|recort|framing|crop|plano", "contratos": ["comunes.encuadre", "comunes.formato"],
     "reglas_re": r"framing|encuadre|crop", "sugerencia": {}, "fuentes": []},
    {"id": "luz", "re": r"\bluz\b|iluminaci|sombra|light", "contratos": ["comunes.tratamiento", "comunes.luz"],
     "reglas_re": r"light|luz|shadow|sombra", "sugerencia": {}, "fuentes": ["flujo-anclas D7"]},
    {"id": "color", "re": r"blanco y negro|b/n|color|colour|monocrom", "contratos": ["comunes.color"], "reglas_re": r"tri-x|colou?r|monochrome",
     "sugerencia": {}, "fuentes": ["CF-TRIX-COLOR"]},
]
ORDEN_CONTRATOS = ["comunes.modelo", "comunes.tratamiento", "comunes.referencias", "comunes.encuadre", "comunes.angulo", "comunes.camara",
                   "comunes.fondo", "comunes.luz", "comunes.color", "comunes.textura", "comunes.foco", "comunes.restricciones", "E*.rasgos"]


def feedback(pid, eid: str | None, texto: str) -> dict:
    """Localiza el PRIMER contrato afectado (orden de dependencias) y las entregas que dependen de él.
    No toca el texto final: propone cambios de campo/bloque que recompilan sólo lo afectado."""
    n, e = cargar(pid)
    reg = registro()
    tipos = [f for f in FEEDBACK if re.search(f["re"], texto, re.I)]
    if not tipos:
        return {"tipos": [], "mensaje": "No se reconoció el problema; indique el bloque (Scene/Subject/…) o el campo afectado."}
    contratos = []
    for f in tipos:
        contratos += f["contratos"]
    contratos = sorted(set(contratos), key=lambda c: ORDEN_CONTRATOS.index(c) if c in ORDEN_CONTRATOS else 99)
    primero = contratos[0]
    afectadas = []
    campo = primero.split(".", 1)[1]
    for ent in e["spec"]["entregas"]:
        comp = e["entregas"][ent["id"]].get("compilado") or {}
        usa = any(campo in b.get("campos", []) for b in comp.get("bloques", [])) or campo in ("tratamiento", "modelo", "referencias")
        if primero.startswith("comunes.") and campo not in ent["campos"] and usa:
            afectadas.append(ent["id"])
    if eid and primero.startswith("E*"):
        afectadas = [eid]
    reglas = []
    info = e["entregas"].get(eid or e["spec"]["entregas"][0]["id"])
    dec = e["_ledgers_completos"][info["perfil"]]["decisiones"]
    for f in tipos:
        rx = re.compile(f["reglas_re"], re.I)
        reglas += [{"id": k, "estado": v["estado"], "texto": reg.reglas[k]["texto"][:160]} for k, v in dec.items() if rx.search(reg.reglas[k]["texto"])][:25]
    sug = {}
    for f in tipos:
        sug |= f["sugerencia"]
    res = {"tipos": [f["id"] for f in tipos], "contratos_en_orden": contratos, "primer_contrato": primero,
           "entregas_dependientes": afectadas, "entregas_independientes": [x["id"] for x in e["spec"]["entregas"] if x["id"] not in afectadas],
           "reglas_relacionadas": reglas, "sugerencias": sug, "fuentes": [s for f in tipos for s in f["fuentes"]],
           "limites": [f["limite"] for f in tipos if f.get("limite")],
           "nota": "Se edita el campo o bloque fuente y se recompila; nunca se parchea el texto final. Las entregas independientes conservan hash y aprobaciones."}
    ST.evento(pid, "feedback", {"entrega": eid, "texto": texto, "primer_contrato": primero})
    return res


# --------------------------------------------------------------------------- evaluación visual

DEFECTOS = {
    "apariencia_render": "Apariencia de render / CGI / piel plástica",
    "ojos_desalineados": "Ojos desalineados o mirada divergente",
    "identidad": "Identidad no coincide con el maestro / referencia",
    "continuidad": "Continuidad rota (vestuario, luz, entorno) entre piezas",
    "manos_anatomia": "Manos o anatomía incorrectas",
    "texto_logo": "Texto o logo no pedido",
    "encuadre": "Encuadre distinto al especificado",
    "fondo": "Fondo distinto al especificado",
    "color": "Color/B-N distinto al especificado",
}


@serializado
def evaluar_visual(pid, eid, archivo: dict, defectos: list[dict], veredicto: str, nota: str = "") -> dict:
    """Registra defectos observables del render y los liga a bloques/campos. El veredicto visual
    (ACCEPT/REVISE/REJECT, vocabulario de visual-asset-critic) va aparte de la cobertura de reglas."""
    if veredicto not in ("ACCEPT", "REVISE", "REJECT"):
        raise ValueError("veredicto ACCEPT | REVISE | REJECT")
    n, e = cargar(pid)
    comp = e["entregas"][eid].get("compilado") or {}
    ligados = []
    for d in defectos:
        if d["tipo"] not in DEFECTOS:
            raise ValueError(f"defecto desconocido {d['tipo']}")
        fb = feedback(pid, eid, DEFECTOS[d["tipo"]] + " " + d.get("nota", ""))
        ligados.append(dict(d, contrato=fb.get("primer_contrato"), bloques=[b["id"] for b in comp.get("bloques", [])
                                                                           if fb.get("primer_contrato", "").split(".")[-1] in b.get("campos", [])],
                            limites=fb.get("limites", [])))
    v = {"id": uuid.uuid4().hex[:10], "proyecto_id": pid, "version": n, "entrega_id": eid, "archivo": archivo["ruta"],
         "sha256": archivo["sha256"], "media_type": archivo.get("media_type"), "prompt_hash": comp.get("hash"),
         "defectos": ligados, "veredicto": veredicto, "nota": nota}
    ST.visual_put(v)
    ST.evento(pid, "evaluacion_visual", {"entrega": eid, "veredicto": veredicto, "defectos": [d["tipo"] for d in defectos]})
    return v


# --------------------------------------------------------------------------- exportación

def exportar(pid, como_aprobado: bool) -> tuple[bytes, dict]:
    n, e = cargar(pid)
    reg = registro()
    vis = ST.visual_list(pid)
    estados = {eid: liberacion(e, eid, [v for v in vis if v["entrega_id"] == eid]) for eid in e["entregas"]}
    if como_aprobado:
        no = {k: v["bloqueos"] for k, v in estados.items() if not v["liberable"]}
        if no:
            raise PermissionError(json.dumps(no, ensure_ascii=False))
    buf = io.BytesIO()
    manifiesto = {"proyecto": pid, "version": n, "registro": reg.version, "exportado": ST.ahora(),
                  "tipo": "APROBADO" if como_aprobado else "BORRADOR (no liberado)", "archivos": {}}
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        def put(nombre, contenido):
            data = contenido if isinstance(contenido, bytes) else (contenido if isinstance(contenido, str) else
                                                                  json.dumps(contenido, ensure_ascii=False, indent=1)).encode("utf-8")
            z.writestr(nombre, data)
            manifiesto["archivos"][nombre] = __import__("hashlib").sha256(data).hexdigest()
        put("brief.json", e["brief"])
        put("especificacion.json", e["spec"])
        put("plan.json", e["plan"])
        for eid, info in e["entregas"].items():
            comp = info.get("compilado")
            if comp:
                put(f"entregas/{eid}/prompt.txt", comp["texto"])
                put(f"entregas/{eid}/parametros.json", comp["parametros"])
                put(f"entregas/{eid}/ast.json", comp["ast"])
                put(f"entregas/{eid}/brief_congelado.json", comp["brief"])
                put(f"entregas/{eid}/bloques.json", comp["bloques"])
                put(f"entregas/{eid}/notas.json", comp["notas"])
            put(f"entregas/{eid}/liberacion.json", estados[eid])
            if e["auditorias"].get(eid):
                put(f"entregas/{eid}/auditoria.json", e["auditorias"][eid])
            if e["semantica"].get(eid):
                put(f"entregas/{eid}/semantica.json", e["semantica"][eid])
        for clave, led in e["_ledgers_completos"].items():
            filas = ["id\testado\tcapa\tskill\tarchivo\tlinea\trazon\tdestino"]
            for rid in sorted(led["decisiones"]):
                d = led["decisiones"][rid]
                r = reg.reglas[rid]
                filas.append("\t".join([rid, d["estado"], d["capa"], r["skill"], r["archivo"], str(r["linea"]),
                                        d.get("razon", "").replace("\t", " ").replace("\n", " "), ",".join(d.get("destino") or [])]))
            put(f"ledger/{clave}.tsv", "\n".join(filas) + "\n")
            put(f"ledger/{clave}.recibo.json", e["ledgers"][clave]["recibo"])
        put("plantillas_snapshot.json", json.loads((F.DATA / "plantillas.json").read_text(encoding="utf-8")))
        put("aprobaciones.json", {"redaccion": e["aprobaciones"], "etapas": e.get("etapas", {})})
        put("evaluaciones_visuales.json", vis)
        put("versiones.json", ST.versiones(pid))
        put("eventos.json", ST.eventos(pid))
        put("registro.json", json.loads((F.DATA / "registro.json").read_text(encoding="utf-8")))
        put("inventario_fuentes.json", json.loads((F.DATA / "inventario.json").read_text(encoding="utf-8")))
        z.writestr("MANIFIESTO.json", json.dumps(manifiesto, ensure_ascii=False, indent=1))
    ST.evento(pid, "exportar", {"aprobado": como_aprobado, "version": n})
    return buf.getvalue(), manifiesto


# --------------------------------------------------------------------------- revisor externo (sin clave de API)

def excluidas_por_medio(perfil: dict) -> frozenset:
    reg, cl = registro(), L.Clasif(registro(), complemento())
    return frozenset(k for k, r in reg.reglas.items() if L.fuera_de_medio(r, cl, perfil))


def exportar_lotes_decision(pid) -> dict:
    n, e = cargar(pid)
    reg = registro()
    out = {"proyecto": pid, "version": n, "registro": reg.version, "sistema": RV.SIS_DECISION, "perfiles": {}}
    for clave, led in e["_ledgers_completos"].items():
        ent = next(x for x in e["spec"]["entregas"] if e["entregas"][x["id"]]["perfil"] == clave)
        se = spec_de_entrega(e["spec"], ent)
        perfil = L.perfil_de(se, e["plan"], ent)
        lotes = RV.construir_lotes(reg, se, perfil, ent, led["decisiones"], excluir=excluidas_por_medio(perfil))
        out["perfiles"][clave] = {"etiqueta": led["etiqueta"], "lotes": [{"indice": i, "ids": g, "usuario": m} for i, (g, m) in enumerate(lotes)]}
    return out


@serializado
def importar_lotes_decision(pid, clave: str, respuestas: dict, revisor: str) -> dict:
    """respuestas: {indice: {"decisiones": [...]}}. Mismo validador que el modelo del servidor.
    Si todos los lotes validan, las decisiones quedan como capa 'externo:<revisor>'."""
    n, e = cargar(pid)
    reg = registro()
    led = e["_ledgers_completos"][clave]
    ent = next(x for x in e["spec"]["entregas"] if e["entregas"][x["id"]]["perfil"] == clave)
    se = spec_de_entrega(e["spec"], ent)
    perfil = L.perfil_de(se, e["plan"], ent)
    dec = copy.deepcopy(led["decisiones"])
    lotes = RV.construir_lotes(reg, se, perfil, ent, dec, excluir=excluidas_por_medio(perfil))
    inf = RV.aplicar_respuestas(reg, se, perfil, dec, lotes, {int(k): v for k, v in respuestas.items()}, f"externo:{revisor}")
    if inf["completo"]:
        ST.ledger_put(clave_revision(se, perfil, clave), reg.version, "modelo",
                      {k: v for k, v in dec.items() if str(v.get("capa", "")).startswith("externo")})
        nueva_version(pid, lambda est: None, f"externo:{revisor}", "revisión externa de reglas por lotes")
    ST.evento(pid, "importar_lotes", {"perfil": clave, "revisor": revisor, "ok": inf["ok"],
                                      "rechazados": list(inf["rechazados"]), "faltan": inf["faltan_lotes"]})
    return inf


def exportar_lotes_semantica(pid, eid, lote_n=40) -> dict:
    n, e = cargar(pid)
    info = e["entregas"][eid]
    comp = info["compilado"]
    dec = e["_ledgers_completos"][info["perfil"]]["decisiones"]
    aplic = sorted(k for k, v in dec.items() if v["estado"] == "APLICA")
    sem = e["semantica"].get(eid) or {}
    if sem.get("texto_hash") == comp["hash"] and sem.get("pendientes"):
        aplic = sorted(set(aplic) & set(sem["pendientes"]))  # cambio quirúrgico: sólo lo que tocó el cambio
    mapa = [{"bloque": b["id"], "slot": b["slot"], "texto": b.get("texto")} for b in comp["bloques"]]
    reg = registro()
    return {"proyecto": pid, "entrega": eid, "texto_hash": comp["hash"], "sistema": RV.SIS_SEMANTICA, "texto": comp["texto"],
            "mapa": mapa, "parametros": comp["parametros"],
            "lotes": [{"indice": i, "ids": g, "reglas": [{"id": r, "texto": reg.reglas[r]["texto"]} for r in g]}
                      for i, g in enumerate(RV.partir(aplic, lote_n))]}


@serializado
def importar_semantica(pid, eid, texto_hash: str, veredictos: list[dict], revisor: str) -> dict:
    n, e = cargar(pid)
    comp = e["entregas"][eid]["compilado"]
    if comp["hash"] != texto_hash:
        raise ValueError("la revisión corresponde a otro texto (hash distinto)")
    dec = e["_ledgers_completos"][e["entregas"][eid]["perfil"]]["decisiones"]
    aplic = {k for k, v in dec.items() if v["estado"] == "APLICA"}
    previa = e["semantica"].get(eid) or {}
    parcial = previa.get("texto_hash") == texto_hash and bool(previa.get("pendientes"))
    if parcial:
        aplic &= set(previa["pendientes"])
    ids = [str(v.get("id")) for v in veredictos]
    faltan, sobran = sorted(aplic - set(ids)), sorted(set(ids) - aplic)
    dup = sorted({i for i in ids if ids.count(i) > 1})
    malos = [v for v in veredictos if v.get("veredicto") not in ("CUMPLE", "NO_CUMPLE", "NO_EVALUABLE_EN_TEXTO", "NO_APLICA_REALMENTE")]
    if faltan or sobran or dup or malos:
        return {"ok": False, "faltan": faltan, "inventados": sobran, "duplicados": dup, "invalidos": len(malos)}
    vv = {v["id"]: v for v in veredictos}
    if parcial:  # se fusiona con lo heredado: sólo se revisó lo que tocó el cambio
        vv = {**(previa.get("veredictos") or {}), **vv}
    nc = [k for k, v in vv.items() if v["veredicto"] == "NO_CUMPLE" and k not in (previa.get("disputados") or {} if parcial else {})]
    e["semantica"][eid] = {"revisor": f"externo:{revisor}", "texto_hash": texto_hash, "completo": True, "veredictos": vv,
                           "pendientes": [], "heredada": previa.get("heredada") if parcial else None,
                           "disputados": (previa.get("disputados") or {}) if parcial else {},
                           "no_cumple_abiertos": nc, "cuestionadas": [k for k, v in vv.items() if v["veredicto"] == "NO_APLICA_REALMENTE"],
                           "resumen": f"{len(vv)} reglas revisadas por {revisor} · {len(nc)} NO_CUMPLE", "fecha": ST.ahora()}
    ST.reemplazar_version(pid, n, persistible(e))
    ST.evento(pid, "semantica_externa", {"entrega": eid, "revisor": revisor, "no_cumple": nc})
    return {"ok": True, "no_cumple": nc}


AUTORIDAD_RE = re.compile(r"[\w./-]+\.(?:md|py|json|yaml|html)(?::\d+)?|DECISIONES\s*#\d+|U-\d{4}-\d{2}-\d{2}-[A-Z]+")


@serializado
def disputar_semantica(pid, eid, rid: str, autoridad: str, razon: str, autor: str) -> dict:
    """Un NO_CUMPLE del revisor semántico sólo sale de 'abiertos' corrigiendo el bloque (texto nuevo, revisión nueva)
    o con autoridad documentada citada (archivo:línea, DECISIONES #n o decisión U-…). Queda registrado y visible."""
    n, e = cargar(pid)
    sem = e["semantica"].get(eid)
    comp = e["entregas"][eid]["compilado"]
    if not sem or sem.get("texto_hash") != comp["hash"]:
        raise ValueError("no hay revisión semántica vigente para este texto")
    if rid not in sem.get("no_cumple_abiertos", []):
        raise ValueError(f"{rid} no es un NO_CUMPLE abierto de esta revisión")
    if not AUTORIDAD_RE.search(autoridad or ""):
        raise ValueError("la autoridad debe citar una fuente verificable (archivo:línea, DECISIONES #n o U-AAAA-MM-DD-…)")
    if len((razon or "").strip()) < 20:
        raise ValueError("la razón debe explicar por qué la autoridad prevalece sobre el veredicto (≥20 caracteres)")
    sem["no_cumple_abiertos"] = [x for x in sem["no_cumple_abiertos"] if x != rid]
    sem.setdefault("disputados", {})[rid] = {"autoridad": autoridad, "razon": razon, "autor": autor, "fecha": ST.ahora(),
                                             "veredicto_revisor": sem["veredictos"][rid]}
    nd = len(sem["disputados"])
    sem["resumen"] = re.sub(r" · \d+ disputados con autoridad", "", sem.get("resumen", "")) + f" · {nd} disputados con autoridad"
    ST.reemplazar_version(pid, n, persistible(e))
    ST.evento(pid, "semantica_disputada", {"entrega": eid, "regla": rid, "autoridad": autoridad, "autor": autor})
    return {"ok": True, "abiertos": sem["no_cumple_abiertos"]}


# --------------------------------------------------------------------------- spot: shots.json → entregas ancla + clip

ENCUADRE_SHOT = {"ECU": "extreme close-up", "CU": "close-up", "MCU": "medium close-up, head and shoulders",
                 "MS": "medium shot, waist up", "MLS": "medium long shot, knees up", "WS": "wide shot, full body in its setting",
                 "EWS": "extreme wide shot"}
MOV_SHOT = {"static": "Locked-off static camera", "push": "Slow push-in", "pull": "Slow pull-out", "pan-left": "Pan left",
            "pan-right": "Pan right", "tilt-up": "Tilt up", "tilt-down": "Tilt down", "handheld": "Handheld camera",
            "orbit": "Orbit around the subject", "whip": "Whip pan", "rack": "Rack focus"}


def validar_shots(shots: dict) -> list[str]:
    import jsonschema
    esquema = json.loads((F.extraer_paquete() / "skills" / "storyboard-architect" / "templates" / "shots.schema.json").read_text())
    v = jsonschema.Draft202012Validator(esquema)
    return [f"{'/'.join(str(p) for p in e.path)}: {e.message}" for e in v.iter_errors(shots)]


def cargar_shots(pid, shots: dict, modelo_imagen="gpt-image-2", modelo_video="kling", autor="usuario"):
    errores = validar_shots(shots)
    if errores:
        raise ValueError("shots.json no valida contra shots.schema.json (original): " + "; ".join(errores[:8]))
    h = F.sha256_text(F.canon_json(shots))
    sl = shots["series_lock"]

    def m(est):
        sp = est["spec"]
        sp["shots"] = {"sha256": h, "proyecto": shots["project"], "series_lock": sl}
        sp["comunes"]["formato"] = S.campo(shots["project"]["aspect"], origen="shots.json", prompt_required=False)
        entregas = []
        for sh in shots["shots"]:
            vinc = {"brief_hash": est["brief_hash"], "shots_sha256": h, "shot_id": sh["id"], "beat": sh["beat"],
                    "rationale": sh["rationale"], "aprobaciones_previas": sorted(k for k, v in est.get("etapas", {}).items() if v.get("aprobada"))}
            persona = not re.search(r"\b(empty|vac[ií]a|no people|product|producto|logo|screen|pantalla)\b", sh["subject"], re.I)
            caso = "T3" if persona else "LUGAR"
            base = {"medio": S.campo("imagen", origen="derivado", prompt_required=False),
                    "modelo": S.campo(modelo_imagen, origen="usuario", prompt_required=False),
                    "tipo_tarea": S.campo([caso], origen="derivado", prompt_required=False),
                    "encuadre": S.campo(ENCUADRE_SHOT[sh["framing"]], origen="shots.json"),
                    "angulo": S.campo(sh["angle"], origen="shots.json"),
                    "sujeto": S.campo(sh["subject"], origen="shots.json"),
                    "fondo": S.campo(sl["environment"], origen="shots.json series_lock (verbatim, forge Rule 3)"),
                    "luz": S.campo(sl["lighting"], origen="shots.json series_lock (verbatim)"),
                    "color": S.campo(sl["color_grade"], origen="shots.json series_lock (verbatim)"),
                    "uso": S.campo(f"Keyframe first frame for {sh['id']} ({sh['beat']}), to be animated", origen="derivado"),
                    "identidad": S.campo(sl["character"], origen="shots.json series_lock.character (verbatim, forge Rule 3)"),
                    "camara": S.campo(f"{sh.get('depth_of_field', 'natural')} depth of field".capitalize(), origen="shots.json depth_of_field")
                    if sh.get("depth_of_field") else S.campo(None, estado="OPEN", motivo="lente/DOF no definidos en el shot"),
                    "textura": S.campo(None, estado="NO_APLICA", prompt_required=False, origen="derivado",
                                       motivo="shots.json no define textura; el series_lock (grade) la gobierna"),
                    "restricciones": S.campo("no text, no watermark, no logo", origen="derivado",
                                             fuente="gpt-image.md:13 Constraints · storyboard-architect: texto en capa separada (text-overlays.json)"),
                    "d1": S.campo("keyframe_ff", origen="derivado", prompt_required=False),
                    "accion": S.campo("A_pose", origen="derivado", prompt_required=False)}
            entregas.append({"id": f"{sh['id']}-FF", "nombre": f"Ancla FF {sh['id']}", "casos": [caso], "campos": base,
                             "vinculos": vinc | {"rol": "ancla"}})
            clip = {"medio": S.campo("video", origen="derivado", prompt_required=False),
                    "modelo": S.campo(modelo_video, origen="usuario", prompt_required=False),
                    "tipo_tarea": S.campo(["CLIP"], origen="derivado", prompt_required=False),
                    "referencias": S.campo([{"nombre": f"{sh['id']}-FF (canonizada)", "rol": "frame_inicial"}], origen="derivado"),
                    "preservar": S.campo("Preserve identity, wardrobe and setting from the start image exactly.", origen="derivado",
                                         fuente="video/references/kling.md:121 (I2V 'Preserve identity, wardrobe … exactly')"),
                    "movimiento": S.campo(MOV_SHOT[sh["motion"]], origen="shots.json"),
                    "accion_video": S.campo(None, estado="OPEN", motivo="qué cambia en el clip (la imagen ya fija sujeto y lugar)"),
                    "audio": S.campo(None, estado="OPEN", motivo="audio del clip (Kling 3.0: capa Audio)"),
                    "duracion": S.campo(f"{round(sh['end'] - sh['start'], 2)}s", origen="shots.json", prompt_required=False),
                    "luz": S.campo(sl["lighting"], origen="shots.json series_lock"),
                    "sujeto": S.campo(None, estado="NO_APLICA", motivo="I2V: no re-describir lo que el frame inicial fija (DECISIONES #3)"),
                    "identidad": S.campo(None, estado="NO_APLICA", motivo="I2V: el frame inicial fija la identidad (DECISIONES #3)"),
                    "angulo": S.campo(sh["angle"], origen="shots.json"),
                    "camara": S.campo(None, estado="NO_APLICA", motivo="el movimiento de cámara va en 'movimiento'"),
                    "restricciones": S.campo(None, estado="NO_APLICA", motivo="Kling: negativos en campo aparte (kling.md §6)")}
            entregas.append({"id": f"{sh['id']}-CLIP", "nombre": f"Clip {sh['id']}", "casos": ["CLIP"], "campos": clip,
                             "vinculos": vinc | {"rol": "clip", "ancla": f"{sh['id']}-FF"}})
        sp["entregas"] = entregas
    return nueva_version(pid, m, autor, f"shots.json ({len(shots['shots'])} shots) → {2 * len(shots['shots'])} entregas")


# --------------------------------------------------------------------------- etapas E0–E4 con modelo (función del ejecutor anterior, sin recorte)

SIS_ETAPA = """Eres el ejecutor de la etapa {clave} · {nombre} del pipeline de producción audiovisual.
Entra: {entra}
Sale: {sale}
Gate de la etapa: {gate}
Cumple TODAS las reglas listadas (son todas las del registro para los subprocesos de esta etapa; ninguna fue recortada).
No inventes datos de marca. Si falta algo decisivo, dilo en "preguntas".
{formato}"""

FORMATO_ETAPA = {
    "E4": 'Responde SOLO JSON: {"shots_json": <objeto que valide contra shots.schema.json v1.2>, "notas": "...", "preguntas": []}',
}


def reglas_de_etapa(clave_etapa: str) -> list[str]:
    reg = registro()
    cl = L.Clasif(reg, complemento())
    subs = {t["codigo"] for t in FL.tareas() if t["etapa"] == clave_etapa}
    return sorted(rid for rid in reg.reglas if subs & set(cl.tareas(rid)))


def generar_etapa(pid, clave_etapa: str) -> dict:
    """Genera el entregable de una etapa con el modelo. El resultado queda PENDIENTE de OK humano
    (los gates 0, 1, 2 y 4 lo exigen); nunca se aprueba solo."""
    if not llm.proveedor().disponible():
        raise llm.SinModelo(llm.estado()["motivo"])
    n, e = cargar(pid)
    et = next(x for x in FL.etapas() if x["clave"] == clave_etapa)
    previas = {k: v.get("artefacto") for k, v in e.get("etapas", {}).items() if v.get("aprobada")}
    faltan = [d for d in FL.DEPENDENCIAS[clave_etapa] if d in [x["clave"] for x in e["plan"]["etapas"] if x["aplica"]] and d not in previas]
    if faltan:
        raise ValueError(f"{clave_etapa} depende de etapas sin aprobar: {faltan}")
    reg = registro()
    ids = reglas_de_etapa(clave_etapa)
    reglas_txt = "\n".join(f"[{rid}] {reg.reglas[rid]['texto']}" for rid in ids)
    sistema = SIS_ETAPA.format(clave=et["clave"], nombre=et["nombre"], entra=et["entra"], sale=et["sale"], gate=et["gate"],
                               formato=FORMATO_ETAPA.get(clave_etapa, 'Responde SOLO JSON: {"documento": "markdown", "preguntas": []}'))
    usuario = json.dumps({"brief": e["brief"].get("texto"), "etapas_aprobadas": previas, "reglas": f"{len(ids)} reglas"}, ensure_ascii=False) + \
        "\n\nREGLAS DE LA ETAPA (" + str(len(ids)) + "):\n" + reglas_txt
    r = llm.proveedor().completar(sistema, usuario)
    out = llm.extraer_json(r["texto"])
    art = json.dumps(out.get("shots_json") if clave_etapa == "E4" else out.get("documento"), ensure_ascii=False)
    errores = validar_shots(out["shots_json"]) if clave_etapa == "E4" and out.get("shots_json") else []

    def m(est):
        est.setdefault("etapas", {})[clave_etapa] = {"aprobada": False, "generado_por": f"{llm.proveedor().nombre}:{llm.proveedor().modelo}",
                                                     "artefacto": art, "artefacto_hash": F.sha256_text(art), "errores": errores,
                                                     "preguntas": out.get("preguntas", []), "reglas_enviadas": len(ids), "uso": r["uso"],
                                                     "fecha": ST.ahora()}
    res = nueva_version(pid, m, "modelo", f"generar {clave_etapa} ({len(ids)} reglas enviadas completas)")
    return {"version": res["version"], "reglas_enviadas": len(ids), "errores": errores, "preguntas": out.get("preguntas", []),
            "uso": r["uso"], "pendiente_ok": True}
