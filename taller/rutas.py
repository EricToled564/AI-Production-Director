"""Rutas de la API compartidas por el servidor local (SQLite, hilos) y la función de Vercel (estado en el
navegador). Las compuertas viven en proceso.py; aquí solo se traduce HTTP a operaciones del proceso.

despachar(metodo, partes, cuerpo, proceso, ctx) devuelve (codigo, datos). El contexto `ctx` aporta lo que
cambia entre entornos: cómo se lanza una operación larga, el estado de la operación en curso y el
proveedor activo.
"""
import time
import traceback

import llm
import proceso as P
from recursos import verificar_manifiesto

OPERACIONES_LARGAS = {
    "desarrollar": lambda pr, cid, nueva: pr.desarrollar_brief(cid, nueva),
    "corregir": lambda pr, cid, nueva: pr.corregir_brief(cid, nueva),
    "seleccionar": lambda pr, cid, nueva: pr.seleccionar(cid, nueva),
    "redactar": lambda pr, cid, nueva: pr.redactar(cid, nueva),
}


def ejecutar_operacion(pr, cid, nombre, nueva, op):
    """Corre una operación larga y deja su resultado en `op` (en_curso, manual, error u ok)."""
    try:
        with pr.candado(cid):
            OPERACIONES_LARGAS[nombre](pr, cid, nueva)
        op.update(estado="ok", mensaje="Completado.")
    except llm.Continuar:
        op["pasos"] = op.get("pasos", 0) + 1
        op.update(estado="en_curso", mensaje=f"Llamadas al modelo completadas: {op['pasos']}. Sigue la siguiente.")
    except llm.ManualPendiente as m:
        s = m.solicitud
        op.update(estado="manual", mensaje="Copia la solicitud en ChatGPT o Claude y pega aquí la respuesta JSON.",
                  solicitud={"clave": s["clave"], "rol": s["rol"], "texto": llm.texto_para_copiar(s)})
    except (P.Compuerta, llm.ErrorModelo, llm.RespuestaInvalida) as e:
        op.update(estado="error", mensaje=str(e))
    except Exception as e:  # noqa: BLE001
        traceback.print_exc()
        op.update(estado="error", mensaje=f"Error interno: {e}")
    op["fin"] = time.time()
    if op["estado"] != "en_curso":
        pr.almacen.evento(cid, "operacion_" + op["estado"], {"nombre": nombre, "mensaje": op["mensaje"]})
    return op


def nueva_operacion(nombre):
    return {"nombre": nombre, "estado": "en_curso", "inicio": time.time(), "mensaje": "", "pasos": 0}


def estado_base(ctx):
    return {"proveedor": ctx.nombre_proveedor(), "aviso_proveedor": ctx.aviso_proveedor(),
            "recursos_modificados": verificar_manifiesto()}


def despachar(metodo, partes, b, pr, ctx):
    try:
        if metodo == "GET":
            return _get(partes, pr, ctx)
        return _post(partes, b or {}, pr, ctx)
    except KeyError:
        return 404, {"error": "Caso inexistente"}
    except (P.Compuerta, llm.RespuestaInvalida) as e:
        return 409, {"error": str(e)}


def _get(partes, pr, ctx):
    if partes == ["api", "estado"]:
        return 200, dict(estado_base(ctx), casos=pr.almacen.listar_casos())
    if len(partes) >= 3 and partes[:2] == ["api", "casos"]:
        cid = partes[2]
        if len(partes) == 3:
            caso = pr.leer(cid)
            caso["operacion_actual"] = ctx.operacion(cid)
            caso["eventos"] = pr.almacen.eventos(cid)[-60:]
            caso["especificas"] = pr.especificas(caso) if caso.get("seleccion") else []
            return 200, caso
        if partes[3] == "plantilla":
            return 200, pr.vista_plantilla(cid)
        if partes[3] == "exportar":
            return 200, {"_markdown": pr.exportar(cid), "_nombre": f"prompt_{cid}.md"}
    return 404, {"error": "No encontrado"}


def _post(partes, b, pr, ctx):
    if partes == ["api", "proveedor"]:
        ctx.cambiar_proveedor(b.get("nombre", "manual"))
        return 200, {"proveedor": ctx.nombre_proveedor(), "aviso": ctx.aviso_proveedor()}
    if partes == ["api", "casos"]:
        return 200, pr.crear_caso(b.get("original", ""))
    if len(partes) == 4 and partes[:2] == ["api", "casos"]:
        cid, accion = partes[2], partes[3]
        pr.almacen.leer_caso(cid)
        if accion in OPERACIONES_LARGAS:
            return ctx.lanzar(cid, accion, True)
        if accion == "manual":
            op = ctx.operacion(cid) or {}
            if op.get("estado") != "manual" or op["solicitud"]["clave"] != b.get("clave"):
                raise P.Compuerta("No hay una solicitud manual pendiente con esa clave.")
            pr.pegar_respuesta(b["clave"], b.get("texto", ""))
            return ctx.lanzar(cid, op["nombre"], False)
        if accion == "continuar":
            op = ctx.operacion(cid) or {}
            if op.get("estado") != "en_curso" or op.get("nombre") not in OPERACIONES_LARGAS:
                raise P.Compuerta("No hay una operación por continuar.")
            return ctx.continuar(cid, op["nombre"])
        acciones = {
            "aporte": lambda: pr.agregar_aporte(cid, b.get("texto", "")),
            "campo": lambda: pr.decidir_campo(cid, b.get("path"), b.get("decision"), b.get("valor"), b.get("comentario", "")),
            "revisado": lambda: pr.marcar_revisado(cid, b.get("revisado")),
            "reabrir": lambda: pr.reabrir_brief(cid),
            "duda": lambda: pr.resolver_duda_seleccion(cid, b.get("id"), b.get("incluir"), b.get("bloque", ""),
                                                       b.get("campo", ""), b.get("cita", ""), b.get("comentario", "")),
            "plantilla": lambda: pr.confirmar_plantilla(cid, b.get("quality")),
            "ambiguedad": lambda: pr.decidir_ambiguedad(cid, b.get("id"), b.get("decision", ""), b.get("alcance", "solo_este_caso")),
            "comentario": lambda: pr.comentar_final(cid, b.get("texto", "")),
            "aprobar": lambda: pr.aprobar(cid),
        }
        if accion in acciones:
            acciones[accion]()
            return 200, {"ok": True}
    return 404, {"error": "No encontrado"}
