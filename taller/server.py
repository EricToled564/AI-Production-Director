"""Servidor local del taller: http://127.0.0.1:8770

Uso:  python taller/server.py            (proveedor según TALLER_PROVEEDOR; por defecto manual)
      TALLER_PROVEEDOR=openai python taller/server.py
"""
import json
import os
import sys
import threading
import time
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))

import llm  # noqa: E402
import proceso as P  # noqa: E402
from recursos import verificar_manifiesto  # noqa: E402

AQUI = Path(__file__).resolve().parent
ESTATICO = AQUI / "static"
TIPOS = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8"}


class Estado:
    def __init__(self):
        self.almacen = P.Almacen(os.environ.get("TALLER_DB", str(AQUI / "datos" / "taller.sqlite3")))
        self.operaciones = {}
        self.nombre_proveedor = os.environ.get("TALLER_PROVEEDOR", "manual")
        self.proceso = None
        self.error_proveedor = ""
        self.cambiar_proveedor(self.nombre_proveedor)

    def cambiar_proveedor(self, nombre):
        try:
            prov = llm.crear(nombre, self.almacen)
            self.error_proveedor = ""
        except llm.ErrorModelo as e:
            prov = llm.crear("manual", self.almacen)
            self.error_proveedor = f"{e} Se usa el modo manual."
        self.nombre_proveedor = prov.nombre
        self.proceso = P.Proceso(self.almacen, prov)

    def lanzar(self, caso_id, nombre, funcion):
        actual = self.operaciones.get(caso_id)
        if actual and actual["estado"] == "en_curso":
            raise P.Compuerta(f"Ya hay una operación en curso: {actual['nombre']}.")
        self.operaciones[caso_id] = {"nombre": nombre, "estado": "en_curso", "inicio": time.time(), "mensaje": ""}

        def correr():
            op = self.operaciones[caso_id]
            try:
                with self.proceso.candado(caso_id):
                    funcion()
                op.update(estado="ok", mensaje="Completado.")
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
            self.almacen.evento(caso_id, "operacion_" + op["estado"], {"nombre": nombre, "mensaje": op["mensaje"]})

        threading.Thread(target=correr, daemon=True).start()


ESTADO = None

OPERACIONES_LARGAS = {
    "desarrollar": lambda pr, cid, nueva: pr.desarrollar_brief(cid, nueva),
    "corregir": lambda pr, cid, nueva: pr.corregir_brief(cid, nueva),
    "seleccionar": lambda pr, cid, nueva: pr.seleccionar(cid, nueva),
    "redactar": lambda pr, cid, nueva: pr.redactar(cid, nueva),
}


class Manejador(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def _json(self, codigo, datos):
        cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def _cuerpo(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}") if n else {}

    def do_GET(self):
        ruta = urlparse(self.path).path
        try:
            if ruta in ("/", "/index.html"):
                return self._archivo(ESTATICO / "index.html")
            if ruta.startswith("/static/"):
                return self._archivo(ESTATICO / Path(ruta).name)
            partes = [p for p in ruta.split("/") if p]
            if partes == ["api", "estado"]:
                return self._json(200, {"proveedor": ESTADO.nombre_proveedor, "aviso_proveedor": ESTADO.error_proveedor,
                                        "recursos_modificados": verificar_manifiesto(),
                                        "casos": ESTADO.almacen.listar_casos()})
            if len(partes) >= 3 and partes[:2] == ["api", "casos"]:
                cid = partes[2]
                pr = ESTADO.proceso
                if len(partes) == 3:
                    caso = pr.leer(cid)
                    caso["operacion_actual"] = ESTADO.operaciones.get(cid)
                    caso["eventos"] = ESTADO.almacen.eventos(cid)[-60:]
                    caso["especificas"] = pr.especificas(caso) if caso.get("seleccion") else []
                    return self._json(200, caso)
                if partes[3] == "plantilla":
                    return self._json(200, pr.vista_plantilla(cid))
                if partes[3] == "exportar":
                    texto = pr.exportar(cid).encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "text/markdown; charset=utf-8")
                    self.send_header("Content-Disposition", f'attachment; filename="prompt_{cid}.md"')
                    self.end_headers()
                    return self.wfile.write(texto)
            self._json(404, {"error": "No encontrado"})
        except KeyError:
            self._json(404, {"error": "Caso inexistente"})
        except P.Compuerta as e:
            self._json(409, {"error": str(e)})

    def do_POST(self):
        partes = [p for p in urlparse(self.path).path.split("/") if p]
        try:
            b = self._cuerpo()
            pr = ESTADO.proceso
            if partes == ["api", "proveedor"]:
                ESTADO.cambiar_proveedor(b.get("nombre", "manual"))
                return self._json(200, {"proveedor": ESTADO.nombre_proveedor, "aviso": ESTADO.error_proveedor})
            if partes == ["api", "casos"]:
                return self._json(200, pr.crear_caso(b.get("original", "")))
            if len(partes) == 4 and partes[:2] == ["api", "casos"]:
                cid, accion = partes[2], partes[3]
                pr.almacen.leer_caso(cid)
                if accion in OPERACIONES_LARGAS:
                    ESTADO.lanzar(cid, accion, lambda: OPERACIONES_LARGAS[accion](pr, cid, True))
                    return self._json(202, {"operacion": accion})
                if accion == "manual":
                    op = ESTADO.operaciones.get(cid) or {}
                    if op.get("estado") != "manual" or op["solicitud"]["clave"] != b.get("clave"):
                        raise P.Compuerta("No hay una solicitud manual pendiente con esa clave.")
                    pr.pegar_respuesta(b["clave"], b.get("texto", ""))
                    nombre = op["nombre"]
                    ESTADO.lanzar(cid, nombre, lambda: OPERACIONES_LARGAS[nombre](pr, cid, False))
                    return self._json(202, {"operacion": nombre})
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
                    return self._json(200, {"ok": True})
            self._json(404, {"error": "No encontrado"})
        except KeyError:
            self._json(404, {"error": "Caso inexistente"})
        except (P.Compuerta, llm.RespuestaInvalida) as e:
            self._json(409, {"error": str(e)})
        except json.JSONDecodeError:
            self._json(400, {"error": "JSON inválido"})

    def _archivo(self, ruta):
        if not ruta.exists():
            return self._json(404, {"error": "No encontrado"})
        datos = ruta.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", TIPOS.get(ruta.suffix, "application/octet-stream"))
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)


def main():
    global ESTADO
    ESTADO = Estado()
    puerto = int(os.environ.get("TALLER_PUERTO", "8770"))
    servidor = ThreadingHTTPServer(("127.0.0.1", puerto), Manejador)
    print(f"Taller de prompts en http://127.0.0.1:{puerto}  (proveedor: {ESTADO.nombre_proveedor})")
    if ESTADO.error_proveedor:
        print("Aviso:", ESTADO.error_proveedor)
    servidor.serve_forever()


if __name__ == "__main__":
    main()
