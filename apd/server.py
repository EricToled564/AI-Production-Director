#!/usr/bin/env python3
"""Servidor local de la app (sólo biblioteca estándar).

    python3 apd/server.py                  # http://127.0.0.1:8765
    APD_PORT=9000 python3 apd/server.py

La clave del modelo se lee del entorno (ver apd/llm.py) y nunca se envía al navegador.
Escucha sólo en 127.0.0.1 salvo APD_HOST explícito. APP_PASSWORD (opcional) protege la API.
"""

from __future__ import annotations

import base64
import json
import os
import re
import sys
import traceback
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

from apd import datos, fuentes as F, ledger as L, llm, proyecto as P, registro as R, sintaxis as SX, store as ST  # noqa: E402

WEB = AQUI / "web"
# Desplegado en una liga pública (Vercel): la API exige APP_PASSWORD y los proyectos deben ir a Turso.
PUBLICO = bool(os.environ.get("VERCEL"))
TIPOS = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8",
         ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".mp4": "video/mp4",
         ".json": "application/json"}


def _json_file(nombre):
    return json.loads((F.DATA / nombre).read_text(encoding="utf-8"))


def resumen_fuentes():
    rec = _json_file("reconciliacion.json")
    cru = _json_file("cruce_v34.json")
    ubi = _json_file("ubicaciones.json")
    return {
        "registro": _json_file("registro.json"),
        "reconciliacion": {k: v for k, v in rec.items() if k != "solo_en_registro"} | {
            "solo_en_registro": {k: v["n"] for k, v in rec["solo_en_registro"]["por_motivo"].items()}},
        "cruce_v34": {k: v for k, v in cru.items() if k not in ("enlazadas", "sin_enlazar")},
        "comparacion_t1": _json_file("comparacion_t1.json"),
        "ubicaciones": {k: v for k, v in ubi.items() if k != "ids"},
        "clasificacion_app": {k: v for k, v in _json_file("clasificacion_app.json").items() if k != "complemento"},
        "citas_flujos": _json_file("citas_flujos.json"),
        "plantillas": [{k: v for k, v in x.items() if k != "texto"} for x in _json_file("plantillas.json")],
        "sintaxis": {"requisitos": len(SX.items()), "modelos": list(SX.catalogo()["modelos"]),
                     "conflictos": [{"id": f"CF-SX-{i + 1:02d}", "descripcion": c["descripcion"],
                                     "resolucion": (c.get("resolucion_documentada") or {}).get("tipo")}
                                    for i, c in enumerate(SX.catalogo()["conflictos_de_sintaxis"])],
                     "sin_fuente": SX.catalogo()["sin_fuente"]},
        "inventario": _json_file("inventario.json"),
    }


def vista_proyecto(pid, n=None):
    n, e = P.cargar(pid, n)
    vis = ST.visual_list(pid)
    entregas = {}
    for ent in e["spec"]["entregas"]:
        eid = ent["id"]
        info = e["entregas"][eid]
        comp = info.get("compilado")
        led = e["ledgers"][info["perfil"]]
        lib = P.liberacion(e, eid, [v for v in vis if v["entrega_id"] == eid])
        sx = info.get("sintaxis") or {}
        entregas[eid] = {
            "id": eid, "nombre": ent["nombre"], "casos": ent["casos"], "campos": ent["campos"], "vinculos": ent.get("vinculos", {}),
            "perfil": info["perfil"], "perfil_etiqueta": led["etiqueta"], "bloqueo": info.get("bloqueo"),
            "texto": comp["texto"] if comp else None, "hash": comp["hash"] if comp else None,
            "formato": comp["formato"] if comp else None, "fuente_formato": comp.get("fuente_formato") if comp else None,
            "parametros": comp["parametros"] if comp else [], "bloques": comp["bloques"] if comp else [],
            "notas": comp["notas"] if comp else None, "ast": comp["ast"] if comp else None,
            "auditoria": e["auditorias"].get(eid), "semantica": {k: v for k, v in (e["semantica"].get(eid) or {}).items() if k != "veredictos"},
            "semantica_veredictos": (e["semantica"].get(eid) or {}).get("veredictos"),
            "aprobacion": e["aprobaciones"].get(eid), "liberacion": lib,
            "sintaxis": {"gate": sx.get("gate"), "conflictos": sx.get("conflictos"), "controles": sx.get("controles"),
                         "aplica": sx.get("aplica")},
        }
    from apd import revision as RV, plantilla_brief as PB
    fmt0 = next(((i.get("compilado") or {}).get("formato") for i in e["entregas"].values() if i.get("compilado")), None)
    mod = e["spec"]["comunes"]["modelo"]["valor"] or ""
    plantilla = PB.vista(e["spec"], fmt0 or ("nano-banana" if mod.startswith("nano-banana") else mod))
    reg = P.registro()
    modo = RV.modo_revision()
    n_rev = max((sum(1 for d in led["decisiones"].values() if RV.abierta(d)) if modo == "abiertas" else len(reg.reglas))
                for led in e["_ledgers_completos"].values()) if e.get("_ledgers_completos") else len(reg.reglas)
    n_lotes = -(-n_rev // RV.LOTE)
    est = dict(RV.estimar(reg, n_lotes, n_reglas=n_rev), perfiles=len(e["ledgers"]), modo=modo,
               nota=(f"La selección mecánica ya decidió las {len(reg.reglas):,} reglas; el modelo sólo revisa las {n_rev} que quedaron "
                     f"abiertas, en {RV.paralelo()} llamadas simultáneas (APD_REVISION=todas para revisar todo el medio).")
               if modo == "abiertas" else "Se re-revisan TODAS las reglas del medio de cada perfil (APD_REVISION=todas).")
    return {"id": pid, "version": n, "estimacion": est, "plantilla": plantilla, "plantilla_info": e["spec"].get("plantilla_info"),
            "plan_aprobado": P.plan_aprobado(e), "aprobacion_plan": e.get("aprobacion_plan"), "brief": e["brief"], "spec": e["spec"], "plan": e["plan"], "preflight": e["preflight"],
            "ledgers": e["ledgers"], "entregas": entregas, "diferencias": e.get("diferencias"),
            "versiones": ST.versiones(pid), "etapas": e.get("etapas", {}), "visual": vis,
            "propuestas": P.PR.proponer(e["spec"]), "decisiones_humanas": e["decisiones_humanas"]}


def filtrar_reglas(pid, q):
    n, e = P.cargar(pid)
    reg = P.registro()
    clave = q.get("perfil") or next(iter(e["_ledgers_completos"]))
    dec = e["_ledgers_completos"][clave]["decisiones"]
    cl = L.Clasif(reg, P.complemento())
    filas = []
    texto_q = (q.get("q") or "").lower()
    sin_evidencia = set()
    for eid, a in e["auditorias"].items():
        if e["entregas"].get(eid, {}).get("perfil") == clave:
            for c in a["controles"]:
                if c["id"] == "evidencia_aplica" and not c["ok"]:
                    sin_evidencia |= set(c.get("ids", []))
    for rid in sorted(reg.reglas):
        r = reg.reglas[rid]
        d = dec[rid]
        if q.get("estado") and d["estado"] != q["estado"]:
            continue
        if q.get("skill") and r["skill"] != q["skill"]:
            continue
        if q.get("caso") and q["caso"] not in cl.casos(rid):
            continue
        if q.get("tarea") and q["tarea"] not in cl.tareas(rid):
            continue
        if q.get("faceta"):
            dim, _, val = q["faceta"].partition("=")
            vals, _ = cl.faceta(rid, dim)
            if val not in vals:
                continue
        if q.get("bloqueo") == "evidencia" and rid not in sin_evidencia:
            continue
        if q.get("bloqueo") == "abiertas" and d["estado"] not in ("CONDICIONAL", "CONFLICTO", "PENDIENTE"):
            continue
        if q.get("capa") and not d["capa"].startswith(q["capa"]):
            continue
        if q.get("motivo") and q["motivo"].lower() not in d.get("razon", "").lower():
            continue
        if texto_q and texto_q not in r["texto"].lower() and texto_q not in rid:
            continue
        filas.append({"id": rid, "skill": r["skill"], "archivo": r["archivo"], "linea": r["linea"], "texto": r["texto"][:220],
                      "estado": d["estado"], "capa": d["capa"], "razon": d.get("razon", ""), "destino": d.get("destino", []),
                      "inferencia": d.get("inferencia", False), "fuerza": r["fuerza"], "estado_fuente": r["estado"]})
    off, lim = int(q.get("offset", 0)), int(q.get("limit", 200))
    return {"perfil": clave, "total_registro": len(reg.reglas), "filtradas": len(filas), "filas": filas[off:off + lim]}


def ficha_regla(rid, pid=None, perfil=None):
    reg = P.registro()
    if rid not in reg.reglas:
        raise KeyError(rid)
    f = reg.ficha(rid)
    f["complemento_app"] = P.complemento().get(rid)
    ubi = _json_file("ubicaciones.json")["ids"].get(rid)
    f["ubicaciones"] = ubi
    f["hash_archivo_actual"] = reg.archivos.get(f"{f['skill']}/{f['archivo']}")
    if pid:
        n, e = P.cargar(pid)
        claves = [perfil] if perfil else list(e["_ledgers_completos"])
        f["decisiones"] = {c: e["_ledgers_completos"][c]["decisiones"][rid] for c in claves}
        historia = []
        for v in ST.versiones(pid):
            _, ev = P.cargar(pid, v["n"])
            for c, led in ev.get("_ledgers_completos", {}).items():
                d = led["decisiones"].get(rid)
                if d:
                    historia.append({"version": v["n"], "perfil": c, "estado": d["estado"], "capa": d["capa"]})
        f["historial"] = historia
        f["en_bloques"] = {eid: [b["id"] for b in (info.get("compilado") or {}).get("bloques", []) if rid in b["satisface"]]
                           for eid, info in e["entregas"].items()}
    return f


class H(BaseHTTPRequestHandler):
    server_version = "APD/1.0"

    def log_message(self, fmt, *args):
        if os.environ.get("APD_LOG"):
            super().log_message(fmt, *args)

    def _auth(self):
        clave = os.environ.get("APP_PASSWORD")
        if PUBLICO and not clave:
            return False  # liga pública sin contraseña: nadie puede gastar la clave del modelo
        return not clave or self.headers.get("x-app-password") == clave

    def _send(self, code, body, tipo="application/json; charset=utf-8", extra=None):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False, default=list).encode("utf-8")
        self.send_response(code)
        self.send_header("content-type", tipo)
        self.send_header("content-length", str(len(data)))
        self.send_header("cache-control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def _body(self):
        n = int(self.headers.get("content-length") or 0)
        return json.loads(self.rfile.read(n).decode("utf-8")) if n else {}

    def do_GET(self):
        self._route("GET")

    def do_POST(self):
        self._route("POST")

    def _route(self, metodo):
        u = urlparse(self.path)
        ruta = u.path
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        if q.get("__ruta"):  # despliegue: vercel.json reenvía toda ruta a api/index.py con la original en __ruta
            ruta = "/" + q.pop("__ruta").lstrip("/")
        try:
            if metodo == "GET" and (ruta == "/" or ruta.startswith("/web/")):
                p = WEB / ("index.html" if ruta == "/" else ruta[5:])
                if not p.resolve().is_relative_to(WEB.resolve()) or not p.is_file():
                    return self._send(404, {"error": "no existe"})
                return self._send(200, p.read_bytes(), TIPOS.get(p.suffix, "application/octet-stream"))
            if metodo == "GET" and ruta.startswith("/uploads/"):
                if not self._auth():
                    return self._send(401, {"error": "contraseña incorrecta"})
                data = ST.leer_archivo(ruta.split("/")[-1])
                if data is None:
                    return self._send(404, {"error": "no existe"})
                return self._send(200, data, TIPOS.get(Path(ruta).suffix, "application/octet-stream"))
            if not ruta.startswith("/api/"):
                return self._send(404, {"error": "ruta desconocida"})
            if ruta == "/api/config":
                return self._send(200, {"ia": llm.estado(), "clave": bool(os.environ.get("APP_PASSWORD")), "claveOk": self._auth(),
                                        "registro": _json_file("registro.json")["version"], "almacenamiento": ST.motor(),
                                        "publico": PUBLICO, "falta_clave_app": PUBLICO and not os.environ.get("APP_PASSWORD"),
                                        "almacenamiento_temporal": PUBLICO and ST.motor() != "turso"})
            if not self._auth():
                return self._send(401, {"error": "falta configurar APP_PASSWORD en el servidor" if PUBLICO and not os.environ.get("APP_PASSWORD")
                                        else "contraseña incorrecta"})
            return self._api(metodo, ruta, q)
        except PermissionError as ex:
            return self._send(409, {"error": "no liberable", "detalle": json.loads(str(ex)) if str(ex).startswith("{") else str(ex)})
        except (ValueError, KeyError) as ex:
            return self._send(400, {"error": f"{type(ex).__name__}: {ex}"})
        except llm.SinModelo as ex:
            return self._send(503, {"error": "sin modelo configurado", "detalle": str(ex)})
        except Exception as ex:
            traceback.print_exc()
            return self._send(500, {"error": f"{type(ex).__name__}: {ex}"})

    def _api(self, metodo, ruta, q):
        partes = ruta.strip("/").split("/")[1:]
        if metodo == "GET" and partes == ["estado"]:
            return self._send(200, {"ia": llm.estado(), "registro": _json_file("registro.json")})
        if metodo == "GET" and partes == ["fuentes"]:
            return self._send(200, resumen_fuentes())
        if metodo == "GET" and partes[:1] == ["plantillas"]:
            return self._send(200, _json_file("plantillas.json"))
        if metodo == "GET" and partes[:1] == ["sintaxis"]:
            return self._send(200, SX.catalogo())
        if metodo == "GET" and len(partes) == 2 and partes[0] == "reglas":
            return self._send(200, ficha_regla(partes[1], q.get("pid"), q.get("perfil")))
        if metodo == "POST" and partes == ["importar-rules-sqlite"]:
            b = self._body()
            tmp = Path(__import__("tempfile").gettempdir()) / "apd_importado_tmp.sqlite"
            tmp.write_bytes(base64.b64decode(b["data"]))
            rep = R.validar(tmp, esperado=b.get("esperado", R.CONTEO_DECLARADO))
            rep["comparacion_con_registro_vigente"] = comparar_import(tmp)
            return self._send(200, rep)
        if metodo == "GET" and partes == ["trabajos", *partes[1:]] and len(partes) == 2:
            return self._send(200, P.trabajo(partes[1]) or {"estado": "DESCONOCIDO"})
        if partes == ["proyectos"]:
            if metodo == "GET":
                return self._send(200, ST.listar())
            b = self._body()
            brief = b["brief"]
            for r in brief.get("referencias", []) or []:
                if r.get("data"):
                    info = ST.guardar_archivo(base64.b64decode(r.pop("data")), r.get("nombre", "ref"))
                    r["sha256"], r["ruta"] = info["sha256"], info["ruta"]
            pid = P.nuevo(brief, b.get("nombre"))
            return self._send(201, {"id": pid})
        if partes and partes[0] == "proyectos" and len(partes) >= 2:
            pid = partes[1]
            resto = partes[2:]
            if metodo == "GET" and not resto:
                return self._send(200, vista_proyecto(pid, int(q["v"]) if q.get("v") else None))
            if metodo == "GET" and resto == ["reglas"]:
                return self._send(200, filtrar_reglas(pid, q))
            if metodo == "GET" and resto == ["diff"]:
                _, a = P.cargar(pid, int(q["a"]))
                _, b = P.cargar(pid, int(q["b"]))
                return self._send(200, P.comparar(a, b))
            if metodo == "GET" and resto == ["exportar"]:
                aprobado = q.get("aprobado") == "1"
                data, man = P.exportar(pid, aprobado)
                nombre = f"apd-{pid}-v{man['version']}-{'aprobado' if aprobado else 'borrador'}.zip"
                return self._send(200, data, "application/zip", {"content-disposition": f'attachment; filename="{nombre}"'})
            if metodo == "GET" and resto == ["visual"]:
                return self._send(200, ST.visual_list(pid))
            if metodo == "GET" and resto == ["eventos"]:
                return self._send(200, ST.eventos(pid))
            if metodo == "GET" and resto == ["lotes-decision"]:
                return self._send(200, P.exportar_lotes_decision(pid))
            b = self._body() if metodo == "POST" else {}
            if metodo == "POST" and resto == ["campos"]:
                return self._send(200, P.cambiar_campos(pid, b["cambios"], b.get("autor", "usuario"), b.get("nota", "edición")))
            if metodo == "POST" and resto == ["propuestas"]:
                return self._send(200, P.aceptar_propuestas(pid, b.get("rutas")))
            if metodo == "POST" and resto == ["decisiones"]:
                return self._send(200, P.decidir_reglas(pid, b["perfil"], b["decisiones"], b.get("autor", "usuario")))
            if metodo == "POST" and resto == ["herencia"]:
                return self._send(200, P.confirmar_herencia(pid, b.get("perfil"), b.get("autor") or "", b.get("nota") or ""))
            if metodo == "POST" and resto == ["conflictos"]:
                return self._send(200, P.resolver_conflicto(pid, b["id"], b["gana"], b.get("razon", ""), b.get("autor", "usuario")))
            if metodo == "POST" and resto == ["gates"]:
                return self._send(200, P.aprobar_gate(pid, b["gate"], b.get("artefacto", ""), b.get("autor", "usuario")))
            if metodo == "POST" and resto == ["generar-etapa"]:
                return self._send(200, P.generar_etapa(pid, b["etapa"]))
            if metodo == "POST" and resto == ["shots"]:
                return self._send(200, P.cargar_shots(pid, b["shots"], b.get("modelo_imagen", "gpt-image-2"), b.get("modelo_video", "kling")))
            if metodo == "POST" and resto == ["revisar-modelo"]:
                return self._send(202, {"trabajo": P.revisar_con_modelo(pid)})
            if metodo == "POST" and resto == ["auditar"]:
                P.auditar(pid, originales=b.get("originales", True))
                return self._send(200, vista_proyecto(pid))
            if metodo == "POST" and resto == ["aprobar-plan"]:
                P.aprobar_plan(pid, b.get("autor") or "usuario")
                return self._send(200, vista_proyecto(pid))
            if metodo == "POST" and resto == ["feedback"]:
                return self._send(200, P.feedback(pid, b.get("entrega"), b["texto"]))
            if metodo == "POST" and resto == ["lotes-decision"]:
                return self._send(200, P.importar_lotes_decision(pid, b["perfil"], b["respuestas"], b.get("revisor", "externo")))
            if len(resto) >= 3 and resto[0] == "entregas":
                eid, accion = resto[1], resto[2]
                if metodo == "GET" and accion == "copiar":
                    r = P.copiar(pid, eid)
                    return self._send(200 if r["liberable"] else 409, r)
                if metodo == "GET" and accion == "lotes-semantica":
                    return self._send(200, P.exportar_lotes_semantica(pid, eid))
                if metodo == "POST" and accion == "lotes-semantica":
                    return self._send(200, P.importar_semantica(pid, eid, b["texto_hash"], b["veredictos"], b.get("revisor", "externo")))
                if metodo == "POST" and accion == "semantica-modelo":
                    return self._send(202, {"trabajo": P.semantica_modelo(pid, eid)})
                if metodo == "POST" and accion == "semantica-disputa":
                    return self._send(200, P.disputar_semantica(pid, eid, b.get("regla"), b.get("autoridad"), b.get("razon"), b.get("autor") or "usuario"))
                if metodo == "POST" and accion == "semantica-humana":
                    return self._send(200, P.semantica_humana(pid, eid, b.get("firmante", ""), b.get("nota", "")))
                if metodo == "POST" and accion == "regenerar-longitud":
                    return self._send(200, P.regenerar_por_longitud(pid, eid))
                if metodo == "POST" and accion == "aprobar":
                    return self._send(200, P.aprobar_redaccion(pid, eid, b["texto_hash"], b.get("autor", "usuario")))
                if metodo == "POST" and accion == "visual":
                    info = ST.guardar_archivo(base64.b64decode(b["data"]), b.get("nombre", "render"))
                    info["media_type"] = b.get("media_type")
                    return self._send(200, P.evaluar_visual(pid, eid, info, b.get("defectos", []), b["veredicto"], b.get("nota", "")))
        return self._send(404, {"error": f"{metodo} {ruta} no existe"})


def comparar_import(p: Path) -> dict:
    import sqlite3
    a = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
    ids = {r[0] for r in a.execute("select id from reglas")}
    vig = set(P.registro().reglas)
    return {"en_ambos": len(ids & vig), "solo_importado": sorted(ids - vig)[:50], "n_solo_importado": len(ids - vig),
            "solo_vigente": sorted(vig - ids)[:50], "n_solo_vigente": len(vig - ids)}


def main():
    if not F.RULES_DB.exists() or not (F.DATA / "registro.json").exists():
        print("construyendo datos derivados desde los originales…", flush=True)
        datos.construir()
    host = os.environ.get("APD_HOST", "127.0.0.1")
    port = int(os.environ.get("APD_PORT", "8765"))
    srv = ThreadingHTTPServer((host, port), H)
    ia = llm.estado()
    print(f"APD en http://{host}:{port}  ·  registro {_json_file('registro.json')['version']}  ·  modelo: "
          f"{ia['proveedor']}{' (' + ia['modelo'] + (', esfuerzo ' + ia['esfuerzo'] if ia['esfuerzo'] else '') + ')' if ia['disponible'] else ' — ' + ia['motivo']}",
          flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
