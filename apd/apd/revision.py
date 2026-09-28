"""Procesamiento por lotes con el modelo: revisión de decisiones por regla y revisión
semántica del prompt final. Reanudable (cada lote se guarda), validado (ids exactos) y
con consumo registrado. Nunca reduce el universo: todos los ids del registro entran
en algún lote; un lote que no se valida tras los reintentos bloquea la entrega.
"""

from __future__ import annotations

import json
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from . import ledger as L
from . import llm
from . import store as ST

LOTE = 60
REINTENTOS = 2

SIS_DECISION = """Eres el revisor de aplicabilidad de reglas de producción visual. Para CADA id recibido decides
un estado: APLICA, NO_APLICA, CONDICIONAL o CONFLICTO, respecto de ESTA entrega concreta.
- La propuesta determinista y la clasificación de la base son evidencia, no veto: corrígelas si el texto de la regla lo exige.
- NO_APLICA exige una razón que cite un dato concreto de la entrega (caso, modelo, medio, encuadre, tratamiento, etapa…).
  Prohibidas razones genéricas como "no aplica" o "no relevante".
- CONDICIONAL sólo si la condición de la regla depende de un dato que la entrega no fija; di cuál.
- No inventes ids, no omitas ninguno, no repitas ninguno.
- "destino": dónde debe verse la regla si APLICA: uno o más de identidad, encuadre, camara, luz, fondo, textura, color,
  restricciones, vocabulario, parametros, referencias, estructura, longitud, proceso, movimiento, audio.
Responde SOLO JSON: {"decisiones":[{"id":"...","estado":"...","razon":"...","destino":["..."]}]}"""

SIS_SEMANTICA = """Eres un auditor independiente. Recibes el TEXTO FINAL de un prompt, su mapa de bloques y un lote de
reglas que se decidió que APLICAN. Para CADA id juzga si el texto (o el parámetro externo indicado) la cumple.
Puedes cuestionar la decisión inicial: si la regla en realidad no aplica, dilo con razón concreta.
Veredictos: CUMPLE, NO_CUMPLE, NO_EVALUABLE_EN_TEXTO (p.ej. reglas de proceso o de resultado visual), NO_APLICA_REALMENTE.
Para NO_CUMPLE indica el bloque fuente a corregir y la corrección concreta. No reescribas el prompt.
Responde SOLO JSON: {"veredictos":[{"id":"...","veredicto":"...","bloque":"...","evidencia":"...","correccion":"..."}]}"""


def _resumen_perfil(spec: dict, perfil: dict, entrega: dict | None) -> str:
    c = spec["comunes"]
    campos = {k: v["valor"] for k, v in c.items() if v["estado"] == "LOCKED" and k != "objetivo"}
    if entrega:
        campos.update({f"{entrega['id']}.{k}": v["valor"] for k, v in entrega["campos"].items() if v["estado"] == "LOCKED"})
    return json.dumps({"perfil": L.etiqueta(perfil), "recorrido": perfil["recorrido"],
                       "subprocesos": sorted(perfil["tareas"]), "campos": campos,
                       "brief": c["objetivo"]["valor"]}, ensure_ascii=False)


def partir(ids: list[str], n: int = LOTE) -> list[list[str]]:
    return [ids[i:i + n] for i in range(0, len(ids), n)]


def estimar(reg, n_lotes: int, chars_por_regla=420, n_reglas: int | None = None) -> dict:
    total = len(reg.reglas) if n_reglas is None else n_reglas
    return {"reglas": total, "lotes": n_lotes, "tokens_entrada_estimados": int(total * chars_por_regla / 4 + n_lotes * 700),
            "tokens_salida_estimados": int(total * 45)}


def modo_revision() -> str:
    """APD_REVISION=abiertas (por defecto): el modelo sólo ve lo que la selección mecánica dejó abierto
    (DECISIONES #9: el criterio no vuelve al agente). APD_REVISION=todas: re-revisa todo el medio, como antes."""
    return "todas" if os.environ.get("APD_REVISION", "").strip().lower() == "todas" else "abiertas"


def abierta(d: dict) -> bool:
    """Lo que la capa determinista no pudo cerrar sola: CONDICIONAL, CONFLICTO, PENDIENTE, APLICA con evidencia débil
    en contra, o un lote anterior fallido. Todo lo demás ya está decidido con evidencia y no pasa por el modelo."""
    return (d["estado"] in ("CONDICIONAL", "CONFLICTO", "PENDIENTE") or bool((d.get("evidencia") or {}).get("en_contra_debil"))
            or bool(d.get("lote_fallido")))


def construir_lotes(reg, spec, perfil, entrega, dec, lote_n=LOTE, excluir=frozenset(), modo=None) -> list[tuple[list[str], str]]:
    """Ids a revisar, primero lo abierto. `excluir`: reglas del otro medio (nivel 0 fijo, U-2026-09-28-CAMBIO-QUIRURGICO),
    que conservan su NO_APLICA determinista. En modo «abiertas» sólo entran las decisiones abiertas (ver `abierta`)."""
    prio = {"CONFLICTO": 0, "CONDICIONAL": 1, "APLICA": 2, "NO_APLICA": 3, "PENDIENTE": 0}
    solo_abiertas = (modo or modo_revision()) == "abiertas"
    ids = sorted((k for k in reg.reglas if k not in excluir and (not solo_abiertas or abierta(dec[k]))),
                 key=lambda k: (prio[dec[k]["estado"]], k))
    contexto = _resumen_perfil(spec, perfil, entrega)
    out = []
    for grupo in partir(ids, lote_n):
        reglas_txt = "\n".join(json.dumps({"id": rid, "texto": reg.reglas[rid]["texto"],
                                           "fuente": f"{reg.reglas[rid]['skill']}/{reg.reglas[rid]['archivo']}:{reg.reglas[rid]['linea']}",
                                           "seccion": reg.reglas[rid].get("seccion", ""),
                                           "estado_fuente": reg.reglas[rid].get("estado"),
                                           "propuesta": dec[rid]["estado"], "razon_propuesta": dec[rid]["razon"]},
                                          ensure_ascii=False) for rid in grupo)
        out.append((grupo, f"ENTREGA:\n{contexto}\n\nIDS DE ESTE LOTE ({len(grupo)}): {', '.join(grupo)}\n\nREGLAS:\n{reglas_txt}"))
    return out


def aplicar_respuestas(reg, spec, perfil, dec, lotes: list[tuple[list[str], str]], respuestas: dict[int, object], capa: str) -> dict:
    """Valida respuestas externas lote por lote con las mismas reglas que las del modelo del servidor."""
    anclas = L.anclas_brief(perfil, spec)
    informe = {"ok": [], "rechazados": {}, "faltan_lotes": []}
    for i, (grupo, _) in enumerate(lotes):
        if i not in respuestas:
            informe["faltan_lotes"].append(i)
            continue
        v = L.validar_lote(grupo, respuestas[i], anclas)
        if not v["ok"]:
            informe["rechazados"][i] = v
            continue
        for x in respuestas[i]["decisiones"]:
            dec[x["id"]] = dict(_desde_modelo(dec[x["id"]], x), capa=capa)
        informe["ok"].append(i)
    informe["completo"] = not informe["rechazados"] and not informe["faltan_lotes"]
    return informe


def revisar_ledger(reg, spec, perfil, entrega, dec: dict[str, dict], clave: str, pid=None, progreso=None,
                   lote_n: int = LOTE, reintentos: int = REINTENTOS, excluir=frozenset()) -> dict:
    """Revisa TODOS los ids. Reanuda: los lotes ya validados no se repiten."""
    p = llm.proveedor()
    if not p.disponible():
        raise llm.SinModelo(llm.estado()["motivo"])
    # orden de trabajo: primero lo que la capa determinista dejó abierto o con evidencia débil
    construidos = construir_lotes(reg, spec, perfil, entrega, dec, lote_n, excluir)
    grupos = [g for g, _ in construidos]
    mensajes = [m for _, m in construidos]
    previos = {l["indice"]: l for l in ST.lotes(clave, "decision")}
    anclas = L.anclas_brief(perfil, spec)
    uso_total = {"entrada": 0, "salida": 0, "segundos": 0.0, "llamadas": 0, "reintentos": 0}
    fallidos = []
    pendientes = []
    for i, grupo in enumerate(grupos):
        prev = previos.get(i)
        if prev and prev["estado"] == "OK" and prev["ids"] == grupo:
            for x in prev["respuesta"]["decisiones"]:
                dec[x["id"]] = _desde_modelo(dec[x["id"]], x)
        else:
            pendientes.append(i)
    mu = threading.Lock()

    def uno(i: int) -> tuple[int, dict, dict | None]:
        """Un lote con sus reintentos. No toca `dec`: devuelve la respuesta validada (o None)."""
        grupo, usuario = grupos[i], mensajes[i]
        lote = {"id": f"{clave}-d-{i}", "proyecto_id": pid, "clave": clave, "tipo": "decision", "indice": i,
                "ids": grupo, "estado": "EN_CURSO", "intentos": 0, "errores": []}
        for intento in range(reintentos + 1):
            lote["intentos"] = intento + 1
            try:
                r = p.completar(SIS_DECISION, usuario)
                with mu:
                    for k in ("entrada", "salida", "segundos"):
                        uso_total[k] += r["uso"].get(k, 0)
                    uso_total["llamadas"] += 1
                resp = llm.extraer_json(r["texto"])
                v = L.validar_lote(grupo, resp, anclas)
            except Exception as ex:  # respuesta no JSON, HTTP, etc.
                v = {"ok": False, "errores": [f"{type(ex).__name__}: {str(ex)[:200]}"]}
                resp = None
            if v["ok"]:
                lote.update(estado="OK", respuesta=resp, uso=r["uso"])
                ST.lote_put(lote)
                return i, lote, resp
            lote["errores"].append(v["errores"] + [str(v.get("invalidos", ""))[:300]])
            with mu:
                uso_total["reintentos"] += 1
            usuario += ("\n\nTU RESPUESTA ANTERIOR FUE RECHAZADA: " + "; ".join(v["errores"]) +
                        (f". Faltaban: {v.get('faltan')}" if v.get("faltan") else "") +
                        (f". Inválidas: {v.get('invalidos')}" if v.get("invalidos") else "") + ". Corrige y responde de nuevo.")
        lote["estado"] = "FALLIDO"
        ST.lote_put(lote)
        return i, lote, None

    hechos = len(grupos) - len(pendientes)
    for i, lote, resp in _en_paralelo(uno, pendientes):
        # las decisiones se aplican en este hilo: cada lote tiene ids disjuntos y `dec` no se toca en paralelo
        if resp is None:
            fallidos.append(i)
            for rid in grupos[i]:
                dec[rid] = dict(dec[rid], lote_fallido=True)
        else:
            for x in resp["decisiones"]:
                dec[x["id"]] = _desde_modelo(dec[x["id"]], x)
        hechos += 1
        if progreso:
            progreso({"lote": hechos, "de": len(grupos), "fallidos": len(fallidos), "uso": uso_total})
    return {"lotes": len(grupos), "fallidos": sorted(fallidos), "uso": uso_total, "completo": not fallidos}


def paralelo() -> int:
    """Lotes simultáneos al modelo (APD_LLM_PARALELO, 6 por defecto). Todas las reglas se siguen revisando: sólo
    cambia cuántas llamadas van a la vez. 1 = secuencial, como antes."""
    try:
        return max(1, int(os.environ.get("APD_LLM_PARALELO", "6")))
    except ValueError:
        return 6


def _en_paralelo(fn, indices):
    """Ejecuta fn(i) con hasta paralelo() hilos y entrega los resultados en orden de término."""
    if paralelo() == 1 or len(indices) <= 1:
        for i in indices:
            yield fn(i)
        return
    with ThreadPoolExecutor(max_workers=min(paralelo(), len(indices))) as ex:
        for f in as_completed([ex.submit(fn, i) for i in indices]):
            yield f.result()


def _desde_modelo(prev: dict, x: dict) -> dict:
    d = dict(prev)
    if x["estado"] != prev["estado"]:
        d["discrepancia"] = {"determinista": prev["estado"], "razon_determinista": prev["razon"]}
    d.update(estado=x["estado"], razon=x.get("razon", ""), capa="modelo", revisada=True, lote_fallido=False)
    if x.get("destino"):
        d["destino"] = x["destino"]
    return d


def revisar_semantica(reg, texto: str, mapa_bloques: list[dict], aplicables: list[str], clave: str, pid=None,
                      progreso=None, lote_n: int = 40, reintentos: int = REINTENTOS) -> dict:
    p = llm.proveedor()
    if not p.disponible():
        raise llm.SinModelo(llm.estado()["motivo"])
    grupos = partir(sorted(aplicables), lote_n)
    veredictos, fallidos = {}, []
    uso = {"entrada": 0, "salida": 0, "segundos": 0.0, "llamadas": 0}
    mapa = json.dumps(mapa_bloques, ensure_ascii=False)
    mu = threading.Lock()

    def uno(i: int) -> tuple[int, list | None]:
        g = grupos[i]
        reglas_txt = "\n".join(json.dumps({"id": rid, "texto": reg.reglas[rid]["texto"]}, ensure_ascii=False) for rid in g)
        usuario = f"TEXTO FINAL:\n<<<\n{texto}\n>>>\n\nMAPA DE BLOQUES:\n{mapa}\n\nIDS ({len(g)}): {', '.join(g)}\n\nREGLAS:\n{reglas_txt}"
        items_ok = None
        for intento in range(reintentos + 1):
            try:
                r = p.completar(SIS_SEMANTICA, usuario)
                with mu:
                    for k in ("entrada", "salida", "segundos"):
                        uso[k] += r["uso"].get(k, 0)
                    uso["llamadas"] += 1
                resp = llm.extraer_json(r["texto"])
                items = resp.get("veredictos", [])
                got = [str(x.get("id")) for x in items]
                if sorted(got) == sorted(g) and len(set(got)) == len(got) and all(
                        x.get("veredicto") in ("CUMPLE", "NO_CUMPLE", "NO_EVALUABLE_EN_TEXTO", "NO_APLICA_REALMENTE") for x in items):
                    items_ok = items
                    break
                usuario += f"\n\nRECHAZADA: ids o veredictos inválidos (esperados exactamente {len(g)} ids). Corrige."
            except Exception as ex:
                usuario += f"\n\nRECHAZADA: {type(ex).__name__}. Responde sólo JSON válido."
        ST.lote_put({"id": f"{clave}-s-{i}", "proyecto_id": pid, "clave": clave, "tipo": "semantica", "indice": i,
                     "ids": g, "estado": "OK" if items_ok is not None else "FALLIDO", "intentos": intento + 1, "uso": dict(uso)})
        return i, items_ok

    hechos = 0
    for i, items in _en_paralelo(uno, list(range(len(grupos)))):
        if items is None:
            fallidos.append(i)
        else:
            for x in items:
                veredictos[x["id"]] = x
        hechos += 1
        if progreso:
            progreso({"lote": hechos, "de": len(grupos), "fallidos": len(fallidos), "uso": uso})
    return {"veredictos": veredictos, "fallidos": sorted(fallidos), "uso": uso, "completo": not fallidos,
            "modelo": f"{p.nombre}:{p.modelo}", "fecha": ST.ahora()}


SIS_SPEC = """Extrae de un brief de producción visual una especificación JSON. No inventes restricciones: si el brief no
lo dice, deja null. Separa lo que el brief DICE de lo que tú PROPONES como decisión creativa (campo "propuestas").
Valores del prompt en inglés; conserva la frase original en "valor_brief".
Formato: {"comunes":{"<campo>":{"valor":...,"valor_brief":"..."}}, "entregas":[{"id":"E1","campos":{...}}],
"propuestas":{"<ruta>":{"valor":...,"porque":"..."}}}"""

SIS_CREATIVO = """Eres director de casting/fotografía. Propón valores para los campos abiertos de cada entrega respetando
TODAS las restricciones del brief (edades, sexos, fondo, encuadre, etc.). Cada entrega debe ser claramente distinta de las
demás (sin variantes genéricas). Valores en inglés, concretos y visibles en la imagen. No uses vocabulario prohibido
(stunning, epic, masterpiece, cinematic, beautiful lighting, professional, high quality).
Responde SOLO JSON: {"propuestas":[{"ruta":"E1.origen","valor":"..."}, ...]}"""


def proponer_creativo(spec: dict, abiertos: list[str]) -> list[dict]:
    p = llm.proveedor()
    if not p.disponible():
        raise llm.SinModelo(llm.estado()["motivo"])
    usuario = json.dumps({"brief": spec["comunes"]["objetivo"]["valor"],
                          "comunes": {k: v["valor"] for k, v in spec["comunes"].items() if v["estado"] == "LOCKED"},
                          "entregas": {e["id"]: {k: v for k, v in e["campos"].items()} for e in spec["entregas"]},
                          "abiertos": abiertos}, ensure_ascii=False)
    r = p.completar(SIS_CREATIVO, usuario)
    out = llm.extraer_json(r["texto"]).get("propuestas", [])
    return [x for x in out if x.get("ruta") in abiertos]
