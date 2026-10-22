"""Máquina de etapas del taller. Cada operación verifica su compuerta antes de actuar.

Etapas (en orden):
  original -> brief_revision -> brief_validado -> seleccion_dudas | seleccion_lista -> plantilla_vista
  -> prompt_ambiguedades | prompt_detenido | revision_final -> aprobado

Ninguna operación puede saltar una etapa: el brief precede y determina el prompt.
Cambiar el brief después de validarlo invalida la selección, la plantilla vista y el prompt.
"""
import json
import sqlite3
import threading
import time
import uuid
from pathlib import Path

import etapas as E
import llm
from recursos import SLOTS_GEN, cargar, huella

ORIGINAL = "original"
BRIEF_REVISION = "brief_revision"
BRIEF_VALIDADO = "brief_validado"
SELECCION_DUDAS = "seleccion_dudas"
SELECCION_LISTA = "seleccion_lista"
PLANTILLA_VISTA = "plantilla_vista"
PROMPT_AMBIGUEDADES = "prompt_ambiguedades"
PROMPT_DETENIDO = "prompt_detenido"
REVISION_FINAL = "revision_final"
APROBADO = "aprobado"

ORDEN = [ORIGINAL, BRIEF_REVISION, BRIEF_VALIDADO, SELECCION_DUDAS, SELECCION_LISTA, PLANTILLA_VISTA,
         PROMPT_AMBIGUEDADES, PROMPT_DETENIDO, REVISION_FINAL, APROBADO]
RONDAS_AUTOMATICAS = 3
LIMITE_REVISION_S = 45      # tiempo máximo de la revisión del brief por API (decisión de Eric, 2026-10-22)
MAX_SALIDA_REVISION = 4000  # tokens de salida: la respuesta solo lista excepciones
REINTENTOS_SELECCION = 2

DECISIONES_POR_ESTADO = {
    "proporcionado": {"aceptar", "modificar"},
    "inferido": {"aceptar", "modificar"},
    "propuesta": {"aceptar", "modificar", "rechazar"},
    "falta": {"responder", "dejar_vacio"},
    "condicion_inactiva": {"aceptar", "activar"},
}


class Compuerta(Exception):
    """La operación no está permitida en la etapa actual o falta una condición previa."""


class Almacen:
    def __init__(self, ruta):
        Path(ruta).parent.mkdir(parents=True, exist_ok=True)
        self.ruta = str(ruta)
        self._local = threading.local()
        with self._con() as c:
            c.executescript("""
            CREATE TABLE IF NOT EXISTS casos (id TEXT PRIMARY KEY, creado REAL, actualizado REAL, etapa TEXT, datos TEXT);
            CREATE TABLE IF NOT EXISTS eventos (id INTEGER PRIMARY KEY AUTOINCREMENT, caso_id TEXT, ts REAL, tipo TEXT, detalle TEXT);
            CREATE TABLE IF NOT EXISTS respuestas (clave TEXT PRIMARY KEY, rol TEXT, proveedor TEXT, valor TEXT, ts REAL);
            CREATE TABLE IF NOT EXISTS pegados (clave TEXT PRIMARY KEY, valor TEXT);
            CREATE TABLE IF NOT EXISTS notas (id TEXT PRIMARY KEY, regla_id TEXT, caso_id TEXT, decision TEXT, contexto TEXT, alcance TEXT, ts REAL);
            """)

    def _con(self):
        con = getattr(self._local, "con", None)
        if con is None:
            con = sqlite3.connect(self.ruta, timeout=30)
            con.row_factory = sqlite3.Row
            self._local.con = con
        return con

    # caché de respuestas de modelo
    def leer_respuesta(self, clave):
        fila = self._con().execute("SELECT valor FROM respuestas WHERE clave=?", (clave,)).fetchone()
        return json.loads(fila["valor"]) if fila else None

    def guardar_respuesta(self, clave, rol, proveedor, valor):
        with self._con() as c:
            c.execute("INSERT OR REPLACE INTO respuestas VALUES (?,?,?,?,?)",
                      (clave, rol, proveedor, json.dumps(valor, ensure_ascii=False), time.time()))

    def leer_pegado(self, clave):
        fila = self._con().execute("SELECT valor FROM pegados WHERE clave=?", (clave,)).fetchone()
        return json.loads(fila["valor"]) if fila else None

    def guardar_pegado(self, clave, valor):
        with self._con() as c:
            c.execute("INSERT OR REPLACE INTO pegados VALUES (?,?)", (clave, json.dumps(valor, ensure_ascii=False)))

    def borrar_pegado(self, clave):
        with self._con() as c:
            c.execute("DELETE FROM pegados WHERE clave=?", (clave,))

    # casos
    def guardar_caso(self, caso):
        caso["actualizado"] = time.time()
        with self._con() as c:
            c.execute("INSERT OR REPLACE INTO casos VALUES (?,?,?,?,?)",
                      (caso["id"], caso["creado"], caso["actualizado"], caso["etapa"], json.dumps(caso, ensure_ascii=False)))

    def leer_caso(self, caso_id):
        fila = self._con().execute("SELECT datos FROM casos WHERE id=?", (caso_id,)).fetchone()
        if not fila:
            raise KeyError(caso_id)
        return json.loads(fila["datos"])

    def listar_casos(self):
        filas = self._con().execute("SELECT id, creado, actualizado, etapa, datos FROM casos ORDER BY actualizado DESC").fetchall()
        return [{"id": f["id"], "creado": f["creado"], "actualizado": f["actualizado"], "etapa": f["etapa"],
                 "titulo": json.loads(f["datos"])["original"][:90]} for f in filas]

    def evento(self, caso_id, tipo, detalle):
        with self._con() as c:
            c.execute("INSERT INTO eventos (caso_id, ts, tipo, detalle) VALUES (?,?,?,?)",
                      (caso_id, time.time(), tipo, json.dumps(detalle, ensure_ascii=False)))

    def eventos(self, caso_id):
        filas = self._con().execute("SELECT ts, tipo, detalle FROM eventos WHERE caso_id=? ORDER BY id", (caso_id,)).fetchall()
        return [{"ts": f["ts"], "tipo": f["tipo"], "detalle": json.loads(f["detalle"])} for f in filas]

    # notas contextuales vinculadas a reglas (no modifican el texto canónico)
    def guardar_nota(self, regla_id, caso_id, decision, contexto, alcance):
        nota_id = uuid.uuid4().hex
        with self._con() as c:
            c.execute("INSERT INTO notas VALUES (?,?,?,?,?,?,?)",
                      (nota_id, regla_id, caso_id, decision, json.dumps(contexto, ensure_ascii=False), alcance, time.time()))
        return nota_id

    def notas_para(self, caso_id):
        filas = self._con().execute(
            "SELECT * FROM notas WHERE caso_id=? OR alcance='casos_similares' ORDER BY ts", (caso_id,)).fetchall()
        return [{"id": f["id"], "regla_id": f["regla_id"], "caso_id": f["caso_id"], "decision": f["decision"],
                 "contexto": json.loads(f["contexto"]), "alcance": f["alcance"]} for f in filas]


class Proceso:
    def __init__(self, almacen, proveedor):
        self.almacen = almacen
        self.proveedor = proveedor
        self.rec = cargar()
        self._candados = {}

    def candado(self, caso_id):
        return self._candados.setdefault(caso_id, threading.Lock())

    # ------------------------------------------------------------ utilidades
    def _exigir_etapa(self, caso, *permitidas):
        if caso["etapa"] not in permitidas:
            raise Compuerta(f"Operación no permitida en la etapa '{caso['etapa']}'. Etapas permitidas: {', '.join(permitidas)}.")

    def _guardar(self, caso, tipo, detalle=None):
        self.almacen.guardar_caso(caso)
        self.almacen.evento(caso["id"], tipo, dict(detalle or {}, etapa=caso["etapa"]))

    def _invalidar_desde_brief(self, caso, motivo):
        if any(caso.get(k) for k in ("brief_validado", "seleccion", "plantilla", "prompt")):
            self.almacen.evento(caso["id"], "invalidacion", {"motivo": motivo,
                                                              "brief_hash": caso.get("brief_hash"),
                                                              "prompt_hash": (caso.get("prompt") or {}).get("hash")})
        for k in ("brief_validado", "brief_hash", "seleccion", "plantilla", "prompt", "revision_prompt",
                  "ambiguedades", "aprobacion"):
            caso[k] = None
        caso["revision_completa"] = False

    def _ronda(self, caso, operacion, nueva):
        """Cada ejecución pedida por el usuario abre una ronda nueva (respuesta fresca del modelo);
        retomar una operación manual conserva la ronda para reutilizar lo ya respondido."""
        rondas = caso.setdefault("rondas", {})
        if nueva or operacion not in rondas:
            rondas[operacion] = rondas.get(operacion, 0) + 1
            self.almacen.guardar_caso(caso)
        return rondas[operacion]

    def leer(self, caso_id):
        caso = self.almacen.leer_caso(caso_id)
        caso["brief_actual"] = self.brief_final(caso) if caso.get("desarrollo") else None
        caso["pendientes_brief"] = self.pendientes_brief(caso) if caso.get("desarrollo") else []
        return caso

    # ------------------------------------------------------------ 1. Original
    def crear_caso(self, original):
        if not original or not original.strip():
            raise Compuerta("El texto original no puede estar vacío.")
        caso = {"id": uuid.uuid4().hex[:12], "creado": time.time(), "etapa": ORIGINAL,
                "original": original, "original_sha256": huella(original), "aportes": [], "desarrollo": None,
                "decisiones": {}, "revision_completa": False, "correccion": None, "brief_validado": None,
                "brief_hash": None, "seleccion": None, "plantilla": None, "prompt": None, "revision_prompt": None,
                "ambiguedades": None, "comentario_final": None, "aprobacion": None, "operacion": None}
        self._guardar(caso, "original_guardado", {"original_sha256": caso["original_sha256"]})
        return caso

    def agregar_aporte(self, caso_id, texto):
        caso = self.almacen.leer_caso(caso_id)
        if not texto.strip():
            raise Compuerta("El aporte está vacío.")
        if caso["etapa"] == APROBADO:
            raise Compuerta("El caso ya fue aprobado.")
        caso["aportes"].append({"id": len(caso["aportes"]) + 1, "texto": texto, "ts": time.time()})
        if caso["etapa"] not in (ORIGINAL, BRIEF_REVISION):
            self._invalidar_desde_brief(caso, "nuevo aporte del usuario")
            caso["etapa"] = BRIEF_REVISION
        self._guardar(caso, "aporte_usuario", {"texto": texto})
        return caso

    # ------------------------------------------------------------ 2. Desarrollo del brief
    def desarrollar_brief(self, caso_id, nueva=True):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, ORIGINAL, BRIEF_REVISION)
        decisiones = [dict(v, path=k) for k, v in caso["decisiones"].items()]
        carga = E.carga_desarrollo(self.rec, caso["original"], caso["aportes"], decisiones)
        carga["ronda_operacion"] = self._ronda(caso, "desarrollar", nueva)
        valor = self.proveedor.llamar("desarrollador_brief", E.SISTEMA_DESARROLLO, carga,
                                      E.validar_desarrollo(self.rec, caso["original"], caso["aportes"]))
        caso["desarrollo"] = valor
        # Las decisiones del usuario se conservan solo si el campo sigue en un estado compatible.
        estados = {c["path"]: c["estado"] for c in valor["campos"]}
        caso["decisiones"] = {p: d for p, d in caso["decisiones"].items()
                              if d["decision"] in DECISIONES_POR_ESTADO.get(estados.get(p), set())}
        caso["revision_completa"] = False
        caso["correccion"] = None
        caso["etapa"] = BRIEF_REVISION
        self._guardar(caso, "brief_desarrollado", {"proveedor": self.proveedor.descripcion(),
                                                   "conteo_estados": _contar(estados.values())})
        return caso

    # ------------------------------------------------------------ 3. Revisión del usuario
    def decidir_campo(self, caso_id, ruta, decision, valor=None, comentario=""):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, BRIEF_REVISION)
        entrada = next((c for c in caso["desarrollo"]["campos"] if c["path"] == ruta), None)
        if entrada is None:
            raise Compuerta(f"Campo inexistente: {ruta}")
        if decision == "deshacer":
            caso["decisiones"].pop(ruta, None)
        else:
            if decision not in DECISIONES_POR_ESTADO[entrada["estado"]]:
                raise Compuerta(f"La decisión '{decision}' no corresponde a un campo en estado '{entrada['estado']}'.")
            if decision in ("modificar", "responder", "activar") and E.vacio(valor):
                raise Compuerta("Esta decisión exige un valor.")
            if decision == "dejar_vacio" and not comentario.strip():
                raise Compuerta("Dejar un campo vacío exige explicar por qué: no se admiten vacíos silenciosos.")
            caso["decisiones"][ruta] = {"decision": decision, "valor": _tipar(valor), "comentario": comentario,
                                        "ts": time.time()}
        caso["revision_completa"] = False
        self._guardar(caso, "decision_campo", {"path": ruta, "decision": decision})
        return caso

    def marcar_revisado(self, caso_id, revisado):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, BRIEF_REVISION)
        caso["revision_completa"] = bool(revisado)
        self._guardar(caso, "brief_revisado_por_usuario", {"revisado": bool(revisado)})
        return caso

    def brief_final(self, caso):
        campos = []
        for c in caso["desarrollo"]["campos"]:
            d = caso["decisiones"].get(c["path"])
            valor, origen = c.get("valor"), c["estado"]
            if d:
                if d["decision"] in ("modificar", "responder", "activar"):
                    valor, origen = d["valor"], "usuario"
                elif d["decision"] == "rechazar":
                    valor, origen = None, "propuesta_rechazada"
                elif d["decision"] == "dejar_vacio":
                    valor, origen = None, "vacio_explicado_por_usuario"
                elif d["decision"] == "aceptar" and c["estado"] == "propuesta":
                    origen = "propuesta_aceptada"
            campos.append({"path": c["path"], "condicion": self.rec.campo_por_ruta[c["path"]]["condition"],
                           "estado_desarrollo": c["estado"], "origen": origen, "valor": valor,
                           "cita": c.get("cita", ""), "fundamento": c.get("fundamento", ""),
                           "pregunta": c.get("pregunta", ""), "alternativas": c.get("alternativas") or [],
                           "decision_usuario": d["decision"] if d else None,
                           "comentario_usuario": d["comentario"] if d else ""})
        return campos

    def _requeridos(self):
        req = set(self.rec.contrato_genesis["required_fields"])
        req |= {c["path"] for c in self.rec.campos if c["condition"] == "siempre"}
        return req

    def pendientes_brief(self, caso):
        pendientes = []
        final = self.brief_final(caso)
        for c in final:
            if c["estado_desarrollo"] == "propuesta" and not c["decision_usuario"]:
                pendientes.append({"path": c["path"], "motivo": "Propuesta sin decidir"})
            if c["estado_desarrollo"] == "falta" and not c["decision_usuario"]:
                pendientes.append({"path": c["path"], "motivo": "Pregunta sin responder"})
        for req in sorted(self._requeridos()):
            subcampos = [c for c in final if c["path"] == req or c["path"].startswith(req + ".")]
            if req == "entrada.restricciones":
                completo = bool(subcampos) and isinstance(subcampos[0]["valor"], list)
            else:
                completo = any(not E.vacio(c["valor"]) for c in subcampos)
            if not completo:
                pendientes.append({"path": req, "motivo": "Campo requerido vacío"})
        return pendientes

    # ------------------------------------------------------------ 4. Corrector del brief
    def corregir_brief(self, caso_id, nueva=True):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, BRIEF_REVISION)
        if not caso["desarrollo"]:
            raise Compuerta("Primero hay que desarrollar el brief.")
        if not caso["revision_completa"]:
            raise Compuerta("El usuario debe revisar el brief completo y confirmarlo antes del corrector.")
        pendientes = self.pendientes_brief(caso)
        if pendientes:
            raise Compuerta("Quedan decisiones pendientes en el brief: " + "; ".join(f"{p['path']} ({p['motivo']})" for p in pendientes[:6]))
        final = self.brief_final(caso)
        carga = E.carga_corrector(self.rec, caso["original"], caso["aportes"], final)
        carga["ronda_operacion"] = self._ronda(caso, "corregir", nueva)
        inicio = time.monotonic()
        valor = self.proveedor.llamar("corrector_brief", E.SISTEMA_CORRECTOR_BRIEF, carga,
                                      E.validar_corrector(self.rec.rutas),
                                      limite_s=LIMITE_REVISION_S, max_salida=MAX_SALIDA_REVISION)
        segundos = round(time.monotonic() - inicio, 1)
        # Solo un FAIL devuelve el brief. UNCERTAIN es una nota para el usuario: lo que solo el usuario
        # puede decidir no es motivo de devolución.
        observaciones = valor["observaciones"]
        problemas = [r for r in observaciones if r["estado"] == "FAIL"]
        notas = [r for r in observaciones if r["estado"] == "UNCERTAIN"]
        caso["correccion"] = {"registros": observaciones, "observaciones": valor.get("observaciones_generales", ""),
                              "problemas": problemas, "notas": notas, "aprobados": len(final) - len(observaciones),
                              "segundos": segundos, "brief_hash": huella(final), "ts": time.time()}
        if problemas:
            caso["revision_completa"] = False
            self._guardar(caso, "brief_devuelto_por_corrector", {"problemas": len(problemas), "notas": len(notas),
                                                                 "segundos": segundos})
        else:
            caso["brief_validado"] = final
            caso["brief_hash"] = huella(final)
            caso["etapa"] = BRIEF_VALIDADO
            self._guardar(caso, "brief_validado", {"brief_hash": caso["brief_hash"], "notas": len(notas),
                                                   "segundos": segundos})
        return caso

    def reabrir_brief(self, caso_id, motivo="El usuario reabrió el brief"):
        caso = self.almacen.leer_caso(caso_id)
        if ORDEN.index(caso["etapa"]) < ORDEN.index(BRIEF_VALIDADO):
            raise Compuerta("El brief todavía no está validado.")
        self._invalidar_desde_brief(caso, motivo)
        caso["etapa"] = BRIEF_REVISION
        self._guardar(caso, "brief_reabierto", {"motivo": motivo})
        return caso

    # ------------------------------------------------------------ 5. Selección de reglas específicas
    def seleccionar(self, caso_id, nueva=True):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, BRIEF_VALIDADO)
        brief = caso["brief_validado"]
        ronda_op = self._ronda(caso, "seleccionar", nueva)
        lote = self.proveedor.lote_seleccion
        unidades = self.rec.catalogo
        decisiones, revisiones = {}, {}
        lotes = [unidades[i:i + lote] for i in range(0, len(unidades), lote)]
        for grupo in lotes:
            ids = [u["id"] for u in grupo]
            valor = self.proveedor.llamar("selector", E.SISTEMA_SELECTOR, dict(E.carga_selector(self.rec, brief, grupo), ronda_operacion=ronda_op),
                                          E.validar_selector(ids, brief))
            for d in valor["decisiones"]:
                decisiones[d["id"]] = d
        # Todos los revisores ven el mismo conteo, el de la primera pasada: así cada lote se revisa de forma
        # independiente (se puede paralelizar y el reintento de un lote no invalida la revisión de los demás).
        conteos_revision = _conteos(decisiones.values())
        for grupo in lotes:
            ids = [u["id"] for u in grupo]
            for intento in range(REINTENTOS_SELECCION + 1):
                propias = [decisiones[i] for i in ids]
                rev = self.proveedor.llamar("revisor_seleccion", E.SISTEMA_REVISOR_SELECCION,
                                            dict(E.carga_revisor_seleccion(self.rec, brief, grupo, propias, conteos_revision), ronda_operacion=ronda_op),
                                            E.validar_registros(ids, clave="id"))
                fallas = [r for r in rev["registros"] if r["estado"] == "FAIL"]
                for r in rev["registros"]:
                    revisiones[r["id"]] = r
                if not fallas or intento == REINTENTOS_SELECCION:
                    break
                retro = [{"id": r["id"], "comentario": r["comentario"]} for r in fallas]
                nuevo = self.proveedor.llamar("selector", E.SISTEMA_SELECTOR,
                                              dict(E.carga_selector(self.rec, brief, grupo, retro), ronda_operacion=ronda_op),
                                              E.validar_selector(ids, brief))
                for d in nuevo["decisiones"]:
                    decisiones[d["id"]] = d
        dudas = []
        for i, d in decisiones.items():
            r = revisiones.get(i, {})
            if d["decision"] == "duda":
                dudas.append({"id": i, "origen": "selector", "pregunta": d.get("pregunta", ""), "decision_selector": d,
                              "texto": self.rec.catalogo_por_id[i]["source"]["texto"]})
            elif r.get("estado") in ("FAIL", "UNCERTAIN"):
                dudas.append({"id": i, "origen": "revisor_" + r["estado"].lower(),
                              "pregunta": r.get("pregunta") or r.get("comentario", ""), "decision_selector": d,
                              "texto": self.rec.catalogo_por_id[i]["source"]["texto"]})
        conteos = _conteos(decisiones.values())
        caso["seleccion"] = {"decisiones": list(decisiones.values()), "revisiones": list(revisiones.values()),
                             "dudas": dudas, "respuestas_usuario": {}, "conteos": conteos,
                             "avisos": _avisos(conteos), "brief_hash": caso["brief_hash"], "lotes": len(lotes)}
        caso["etapa"] = SELECCION_DUDAS if dudas else SELECCION_LISTA
        self._guardar(caso, "seleccion_completada", {"seleccionadas": sum(conteos.values()), "dudas": len(dudas),
                                                     "avisos": caso["seleccion"]["avisos"]})
        return caso

    def resolver_duda_seleccion(self, caso_id, unidad_id, incluir, bloque="", campo="", cita="", comentario=""):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, SELECCION_DUDAS)
        sel = caso["seleccion"]
        if unidad_id not in {d["id"] for d in sel["dudas"]}:
            raise Compuerta("Esa regla no tiene una duda pendiente.")
        if incluir and bloque not in E.BLOQUES:
            raise Compuerta("Para incluir la regla hay que indicar el bloque del prompt.")
        sel["respuestas_usuario"][unidad_id] = {"incluir": bool(incluir), "bloque": bloque, "campo_brief": campo,
                                                "cita_brief": cita, "comentario": comentario, "ts": time.time()}
        if all(d["id"] in sel["respuestas_usuario"] for d in sel["dudas"]):
            sel["conteos"] = _conteos(self._especificas_raw(caso))
            sel["avisos"] = _avisos(sel["conteos"])
            caso["etapa"] = SELECCION_LISTA
        self._guardar(caso, "duda_seleccion_resuelta", {"id": unidad_id, "incluir": bool(incluir)})
        return caso

    def _especificas_raw(self, caso):
        sel = caso["seleccion"]
        dudosas = {d["id"] for d in sel["dudas"]}
        salida = []
        for d in sel["decisiones"]:
            if d["id"] in dudosas:
                r = sel["respuestas_usuario"].get(d["id"])
                if r and r["incluir"]:
                    salida.append({"id": d["id"], "decision": "seleccionada", "bloque": r["bloque"],
                                   "campo_brief": r["campo_brief"] or d.get("campo_brief", ""),
                                   "cita_brief": r["cita_brief"] or d.get("cita_brief", ""),
                                   "razon": "Incluida por decisión del usuario. " + r["comentario"]})
            elif d["decision"] == "seleccionada":
                salida.append(d)
        return salida

    def especificas(self, caso):
        salida = []
        for d in self._especificas_raw(caso):
            u = self.rec.catalogo_por_id[d["id"]]
            salida.append({"regla_id": "SPEC::" + d["id"], "fuente_id": d["id"], "literal": u["source"]["texto"],
                           "archivo": u["source"]["archivo"], "encabezado": u["source"]["encabezado"],
                           "bloque": d["bloque"], "activacion": {"campo": d.get("campo_brief", ""), "cita": d.get("cita_brief", "")},
                           "razon": d.get("razon", "")})
        return salida

    # ------------------------------------------------------------ 6. Plantilla e instrucciones
    def vista_plantilla(self, caso_id):
        caso = self.almacen.leer_caso(caso_id)
        if ORDEN.index(caso["etapa"]) < ORDEN.index(SELECCION_LISTA):
            raise Compuerta("La plantilla se muestra después de validar el brief y seleccionar las reglas.")
        ratio = next((c["valor"] for c in caso["brief_validado"] if c["path"] == "entrada.formato.ratio"), "")
        return {"adapter": self.rec.llenado["template"], "fuente_adapter": self.rec.llenado["fuente_adapter"],
                "instrucciones_llenado": self.rec.instrucciones_slots(), "parametros": self.rec.llenado["parametros"],
                "universales": self.rec.universales, "pack_operacion": self.rec.pack_gen(),
                "directivas": self.rec.reglas_directivas(), "especificas": self.especificas(caso),
                "avisos_seleccion": caso["seleccion"]["avisos"], "tamano": ratio}

    def confirmar_plantilla(self, caso_id, quality):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, SELECCION_LISTA)
        if quality not in ("low", "medium", "high"):
            raise Compuerta("Elige quality: low, medium o high. La app no inventa un valor por defecto.")
        vista = self.vista_plantilla(caso_id)
        caso["plantilla"] = {"hash": huella(vista), "parametros": {"quality": quality, "tamano": vista["tamano"]},
                             "ts": time.time()}
        caso["etapa"] = PLANTILLA_VISTA
        self._guardar(caso, "plantilla_vista_confirmada", {"hash": caso["plantilla"]["hash"], "quality": quality})
        return caso

    # ------------------------------------------------------------ 7-8. Redacción y corrección del prompt
    def redactar(self, caso_id, nueva=True):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, PLANTILLA_VISTA, PROMPT_DETENIDO, PROMPT_AMBIGUEDADES, REVISION_FINAL)
        if caso["etapa"] == PROMPT_AMBIGUEDADES:
            pendientes = [a for a in caso["ambiguedades"]["items"] if not a.get("decision")]
            if pendientes:
                raise Compuerta(f"Quedan {len(pendientes)} ambigüedades por decidir.")
        if caso["etapa"] == REVISION_FINAL and not caso.get("comentario_final"):
            raise Compuerta("En la revisión final se redacta de nuevo solo si hay un comentario del usuario.")
        brief = caso["brief_validado"]
        especificas = self.especificas(caso)
        parametros = caso["plantilla"]["parametros"]
        notas = self.almacen.notas_para(caso_id)
        reglas = E.reglas_para_revision(self.rec, especificas, notas)
        ids = [r["regla_id"] for r in reglas]
        previo = caso["prompt"]
        observaciones = (caso.get("revision_prompt") or {}).get("problemas", [])
        decisiones = [{"regla_id": a["regla_id"], "cita": a["cita"], "pregunta": a["pregunta"], "decision": a["decision"]}
                      for a in ((caso.get("ambiguedades") or {}).get("items") or []) if a.get("decision")]
        comentario = caso.get("comentario_final")
        ronda_op = self._ronda(caso, "redactar", nueva)
        for ronda in range(1, RONDAS_AUTOMATICAS + 1):
            carga = E.carga_redactor(self.rec, brief, especificas, parametros,
                                     previo={"slots": previo["slots"]} if previo else None,
                                     observaciones=observaciones, decisiones=decisiones, comentario=comentario)
            carga["ronda_operacion"] = [ronda_op, ronda]
            borrador = self.proveedor.llamar("redactor", E.SISTEMA_REDACTOR, carga, E.validar_redactor(parametros))
            slots = {s: borrador["slots"][s].strip() for s in SLOTS_GEN}
            cuerpo = E.cuerpo_prompt(slots)
            prompt = {"slots": slots, "cuerpo": cuerpo, "parametros": dict(parametros),
                      "aplicacion": borrador.get("aplicacion", []), "notas": borrador.get("notas", []),
                      "hash": huella({"cuerpo": cuerpo, "parametros": parametros}), "ronda": ronda}
            if borrador.get("parametros") != parametros:
                prompt["notas"].append("El redactor devolvió parámetros distintos; se conservan los fijados por el usuario.")
            deterministas = E.comprobaciones_deterministas(slots, parametros, brief)
            entrega = E.paquete_entrega(parametros, brief)
            rev = self.proveedor.llamar("revisor_prompt", E.SISTEMA_REVISOR_PROMPT,
                                        {"brief_validado": brief, "prompt": cuerpo, "parametros": parametros,
                                         "entrega": entrega, "reglas": reglas, "texto_original": caso["original"],
                                         "ronda_operacion": [ronda_op, ronda]},
                                        E.validar_revisor_prompt(ids, cuerpo, entrega))
            registros = rev["registros"] + deterministas
            problemas = [r for r in registros if r["estado"] != "PASS"]
            fallas = [r for r in problemas if r["estado"] == "FAIL"]
            dudas = [r for r in problemas if r["estado"] == "UNCERTAIN"]
            caso["prompt"] = prompt
            caso["revision_prompt"] = {"registros": registros, "problemas": problemas, "ronda": ronda,
                                       "estado": "FAIL" if fallas else "UNCERTAIN" if dudas else "PASS"}
            self.almacen.evento(caso_id, "prompt_revisado", {"ronda": ronda, "fallas": len(fallas), "dudas": len(dudas),
                                                             "prompt_hash": prompt["hash"]})
            if fallas and ronda < RONDAS_AUTOMATICAS:
                previo, observaciones, comentario = prompt, fallas, comentario
                continue
            break
        caso["comentario_final"] = None
        estado = caso["revision_prompt"]["estado"]
        if estado == "FAIL":
            caso["etapa"] = PROMPT_DETENIDO
        elif estado == "UNCERTAIN":
            items = []
            for r in caso["revision_prompt"]["problemas"]:
                if r["estado"] == "UNCERTAIN":
                    items.append({"id": huella([r["regla_id"], r.get("cita"), r.get("explicacion")])[:16],
                                  "regla_id": r["regla_id"], "cita": r.get("cita", ""), "slot": r.get("slot", ""),
                                  "explicacion": r.get("explicacion", ""), "pregunta": r.get("pregunta", ""),
                                  "decision": None, "alcance": None})
            caso["ambiguedades"] = {"items": items, "prompt_hash": caso["prompt"]["hash"]}
            caso["etapa"] = PROMPT_AMBIGUEDADES
        else:
            caso["etapa"] = REVISION_FINAL
        self._guardar(caso, "prompt_redactado", {"estado_revision": estado, "prompt_hash": caso["prompt"]["hash"]})
        return caso

    # ------------------------------------------------------------ 9. Ambigüedades
    def decidir_ambiguedad(self, caso_id, item_id, decision, alcance="solo_este_caso"):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, PROMPT_AMBIGUEDADES)
        if not decision.strip():
            raise Compuerta("La decisión no puede estar vacía.")
        if alcance not in ("solo_este_caso", "casos_similares"):
            raise Compuerta("Alcance inválido.")
        item = next((a for a in caso["ambiguedades"]["items"] if a["id"] == item_id), None)
        if item is None:
            raise Compuerta("Ambigüedad inexistente.")
        item["decision"], item["alcance"] = decision, alcance
        item["nota_id"] = self.almacen.guardar_nota(item["regla_id"], caso_id, decision,
                                                    {"cita": item["cita"], "pregunta": item["pregunta"],
                                                     "explicacion": item["explicacion"], "prompt_hash": caso["prompt"]["hash"]},
                                                    alcance)
        self._guardar(caso, "ambiguedad_decidida", {"regla_id": item["regla_id"], "alcance": alcance})
        return caso

    # ------------------------------------------------------------ 10. Revisión final y aprobación
    def comentar_final(self, caso_id, texto):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, REVISION_FINAL, PROMPT_DETENIDO)
        if not texto.strip():
            raise Compuerta("El comentario está vacío.")
        caso["comentario_final"] = texto
        self._guardar(caso, "comentario_final", {"texto": texto})
        return caso

    def aprobar(self, caso_id):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, REVISION_FINAL)
        if (caso.get("revision_prompt") or {}).get("estado") != "PASS":
            raise Compuerta("Solo se aprueba un prompt que pasó la corrección semántica.")
        if caso.get("comentario_final"):
            raise Compuerta("Hay un comentario pendiente: primero se corrige y verifica.")
        caso["aprobacion"] = {"prompt_hash": caso["prompt"]["hash"], "brief_hash": caso["brief_hash"], "ts": time.time()}
        caso["etapa"] = APROBADO
        self._guardar(caso, "prompt_aprobado_por_usuario", caso["aprobacion"])
        return caso

    def exportar(self, caso_id):
        caso = self.almacen.leer_caso(caso_id)
        self._exigir_etapa(caso, APROBADO)
        return documento_prompt(self.rec, caso, self.especificas(caso))

    # ------------------------------------------------------------ manual
    def pegar_respuesta(self, clave, texto):
        valor = llm.extraer_json(texto)
        self.almacen.guardar_pegado(clave, valor)


def _tipar(valor):
    if isinstance(valor, str):
        t = valor.strip()
        if t[:1] in "[{" or t in ("true", "false", "null") or _es_numero(t):
            try:
                return json.loads(t)
            except json.JSONDecodeError:
                return valor
    return valor


def _es_numero(t):
    try:
        float(t)
        return True
    except ValueError:
        return False


def _contar(valores):
    salida = {}
    for v in valores:
        salida[v] = salida.get(v, 0) + 1
    return salida


def _conteos(decisiones):
    conteos = {b: 0 for b in E.BLOQUES}
    for d in decisiones:
        if d.get("decision") == "seleccionada" and d.get("bloque") in conteos:
            conteos[d["bloque"]] += 1
    return conteos


def _avisos(conteos):
    avisos = []
    for b in SLOTS_GEN:
        if conteos[b] > 2:
            avisos.append({"bloque": b, "tipo": "mas_de_dos",
                           "texto": f"{conteos[b]} reglas específicas en {b}: revisar los filtros. No bloquea ni excluye reglas válidas."})
        elif conteos[b] == 0:
            avisos.append({"bloque": b, "tipo": "sin_especificas",
                           "texto": f"Ninguna regla específica en {b}: confirmar que la cobertura es correcta."})
    return avisos


def documento_prompt(rec, caso, especificas):
    p = caso["prompt"]
    lineas = ["# Prompt aprobado — GPT Image 2", "",
              f"Brief: {caso['brief_hash']} · Prompt: {p['hash']} · Aprobado: {time.strftime('%Y-%m-%d %H:%M', time.localtime(caso['aprobacion']['ts']))}", "",
              "## Instrucciones y reglas aplicadas (texto canónico sin alterar)", "", "### 12 reglas universales de redacción", ""]
    for u in rec.universales:
        lineas.append(f"- **{u['regla_id']}**: " + " | ".join(f"{f['id']} ({f['archivo']}:{f['lineas']}): {f['texto']}" for f in u["fuentes"]))
    lineas += ["", "### Directivas del usuario", ""]
    for d in rec.reglas_directivas():
        lineas.append(f"- **{d['regla_id']}**: {d['literal']}")
    lineas += ["", "### Reglas específicas seleccionadas desde el brief", ""]
    for e in especificas:
        lineas.append(f"- **{e['regla_id']}** → {e['bloque']} · activa: {e['activacion']['campo']} «{e['activacion']['cita']}» · {e['archivo']}: {e['literal']}")
    lineas += ["", "## Salida", "", "```text", "Model: GPT Image 2", f"Quality: {p['parametros']['quality']}",
               f"Size / Ratio: {p['parametros']['tamano']}", "", "Prompt:", p["cuerpo"], "```", "",
               "## Texto para copiar en el generador", "", "```text", p["cuerpo"], "```", ""]
    inferencias = E.paquete_entrega(p["parametros"], caso["brief_validado"])["inferencias_y_supuestos"]
    if inferencias:
        lineas += ["## Inferencias y supuestos (fuera del texto visual)", ""] + [f"- {n}" for n in inferencias] + [""]
    if p.get("notas"):
        lineas += ["## Notas del redactor", ""] + [f"- {n}" for n in p["notas"]] + [""]
    lineas += ["## Trazabilidad de la verificación", ""]
    for r in caso["revision_prompt"]["registros"]:
        lineas.append(f"- {r['regla_id']}: {r['estado']} — {r.get('explicacion') or r.get('comentario', '')}")
    return "\n".join(lineas) + "\n"
