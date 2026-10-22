"""Pruebas del taller con un modelo simulado (fixture). Comprueban compuertas, validadores y bucles.
No prueban la calidad semántica de un modelo real: eso exige correr un caso con un proveedor real.

    python -m unittest discover -s taller/tests -v
"""
import json
import os
import sys
import tempfile
import threading
import unittest
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import etapas as E  # noqa: E402
import llm  # noqa: E402
import proceso as P  # noqa: E402
from recursos import cargar, verificar_manifiesto  # noqa: E402

ORIGINAL = "quiero un retrato de una pescadora de 60 años en un muelle al amanecer, formato 16:9, sin texto"


class Modelo:
    """Responde por rol a partir de la carga recibida; lleva la cuenta de llamadas por rol."""

    def __init__(self):
        self.llamadas = {}
        self.fallar_corrector_una_vez = True
        self.nota_en_corrector = False
        self.borrador_con_slop = True
        self.duda_en_revision = True

    def __call__(self, rol, carga):
        self.llamadas[rol] = self.llamadas.get(rol, 0) + 1
        return getattr(self, rol)(carga)

    def desarrollador_brief(self, carga):
        rec = cargar()
        req = set(rec.contrato_genesis["required_fields"])
        campos = []
        for c in carga["campos_template"]:
            ruta = c["path"]
            base = {"path": ruta, "estado": "", "valor": None, "cita": "", "fundamento": "", "pregunta": "", "alternativas": []}
            if ruta == "entrada.formato.ratio":
                base.update(estado="proporcionado", valor="16:9", cita="formato 16:9")
            elif ruta == "entrada.restricciones":
                base.update(estado="proporcionado", valor=["sin texto"], cita="sin texto")
            elif ruta.startswith("entrada.camara.plano") or ruta.startswith("entrada.luz.direccion"):
                base.update(estado="propuesta", valor="plano medio corto, luz lateral baja", fundamento="Pieza fotográfica: hay que definir la toma.")
            elif ruta == "entrada.sujetos.items[].vestuario":
                base.update(estado="falta", pregunta="¿Qué ropa lleva la pescadora?")
            elif c["condicion"] == "siempre" or ruta in req or ruta.startswith(("entrada.sujetos", "entrada.escena")):
                base.update(estado="inferido", valor="valor deducido", fundamento="Se deduce del original.")
            else:
                base.update(estado="condicion_inactiva", fundamento=f"Condición «{c['condicion']}» no se cumple.")
            campos.append(base)
        return {"campos": campos, "resumen_creativo": "Retrato documental al amanecer.", "conflictos": []}

    def corrector_brief(self, carga):
        observaciones = []
        primero, ultimo = carga["brief"][0]["path"], carga["brief"][-1]["path"]
        if self.fallar_corrector_una_vez:
            self.fallar_corrector_una_vez = False
            observaciones.append({"path": primero, "estado": "FAIL", "comentario": "El flujo no corresponde a una génesis."})
        if self.nota_en_corrector:
            observaciones.append({"path": ultimo, "estado": "UNCERTAIN", "comentario": "Decisión del usuario.",
                                  "pregunta": "¿Confirmas el destino?"})
        return {"observaciones": observaciones, "observaciones_generales": ""}

    def selector(self, carga):
        decisiones = []
        for i, u in enumerate(carga["candidatas"]):
            if i < 3 and _primer_lote(carga):
                decisiones.append({"id": u["id"], "decision": "seleccionada", "bloque": "Important Details",
                                   "campo_brief": "entrada.formato.ratio", "cita_brief": "16:9", "razon": "Aplica al formato."})
            else:
                decisiones.append({"id": u["id"], "decision": "excluida", "razon": "No se activa en este caso."})
        return {"decisiones": decisiones}

    def revisor_seleccion(self, carga):
        return {"registros": [{"id": d["id"], "estado": "PASS", "comentario": "Correcto.", "pregunta": ""} for d in carga["decisiones"]]}

    def redactor(self, carga):
        detalles = "Low side light from the left, weathered skin texture."
        if self.borrador_con_slop:
            self.borrador_con_slop = False
            detalles = "Stunning light, weathered skin texture."
        slots = {"Scene": "Create a fishing pier at dawn with wet planks.", "Subject": "A 60-year-old fisherwoman, medium close-up.",
                 "Important Details": detalles, "Use Case": "Documentary portrait.", "Constraints": "No rendered text."}
        return {"slots": slots, "parametros": carga["parametros_fijados"], "aplicacion": [], "notas": []}

    def revisor_prompt(self, carga):
        registros = [{"regla_id": r["regla_id"], "estado": "PASS", "slot": "", "cita": "", "explicacion": "Cumple.", "pregunta": ""}
                     for r in carga["reglas"]]
        con_decision = any(r["notas_contextuales"] for r in carga["reglas"])
        if self.duda_en_revision and "Stunning" not in carga["prompt"] and not con_decision:
            registros[0] = dict(registros[0], estado="UNCERTAIN", cita="medium close-up", explicacion="¿Plano medio corto o primer plano?",
                                pregunta="¿Qué plano prefieres?")
        return {"registros": registros}


def _primer_lote(carga):
    return carga["candidatas"][0]["id"] == cargar().catalogo[0]["id"]


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.almacen = P.Almacen(Path(self.tmp.name) / "t.sqlite3")
        self.modelo = Modelo()
        self.proveedor = llm.Fixture(self.almacen, self.modelo)
        self.pr = P.Proceso(self.almacen, self.proveedor)

    def tearDown(self):
        self.tmp.cleanup()

    def decidir_todo(self, cid, pr=None):
        pr = pr or self.pr
        caso = pr.leer(cid)
        for c in caso["brief_actual"]:
            if c["estado_desarrollo"] == "propuesta":
                pr.decidir_campo(cid, c["path"], "aceptar")
            elif c["estado_desarrollo"] == "falta":
                pr.decidir_campo(cid, c["path"], "responder", "overol impermeable naranja")
        pr.marcar_revisado(cid, True)

    def hasta_brief_validado(self):
        cid = self.pr.crear_caso(ORIGINAL)["id"]
        self.pr.desarrollar_brief(cid)
        self.decidir_todo(cid)
        self.pr.corregir_brief(cid)          # el corrector devuelve una vez
        self.pr.marcar_revisado(cid, True)
        self.pr.corregir_brief(cid)
        return cid


class TestRecursos(unittest.TestCase):
    def test_manifiesto_intacto(self):
        self.assertEqual(verificar_manifiesto(), [])

    def test_doce_universales_con_literal_canonico(self):
        rec = cargar()
        self.assertEqual(len(rec.universales), 12)
        anti = next(u for u in rec.universales if u["regla_id"] == "U-ANTI-SLOP")
        literal = next(f for f in anti["fuentes"] if f["id"] == "INV-002343")["texto"]
        self.assertEqual(literal, rec.canonicos["INV-002343"]["texto"])
        self.assertIn("gorgeous", literal)

    def test_brief_tiene_109_campos_y_directivas(self):
        rec = cargar()
        self.assertEqual(len(rec.campos), 109)
        ids = [d["regla_id"] for d in rec.reglas_directivas()]
        self.assertIn("USER::ERIC-DELEGATION-TERMS", ids)
        self.assertIn("USER::ERIC-IDIOMA-PROMPT-INGLES", ids)
        self.assertNotIn("USER::ERIC-B1-PHOTOREALISTIC", ids, "La restricción del perfil B1 no se hereda a casos nuevos.")


class TestCompuertas(Base):
    def test_no_se_puede_saltar_ninguna_etapa(self):
        cid = self.pr.crear_caso(ORIGINAL)["id"]
        for op in (lambda: self.pr.corregir_brief(cid), lambda: self.pr.seleccionar(cid),
                   lambda: self.pr.confirmar_plantilla(cid, "high"), lambda: self.pr.redactar(cid),
                   lambda: self.pr.aprobar(cid), lambda: self.pr.exportar(cid)):
            with self.assertRaises(P.Compuerta):
                op()

    def test_corrector_exige_revision_y_decisiones(self):
        cid = self.pr.crear_caso(ORIGINAL)["id"]
        self.pr.desarrollar_brief(cid)
        with self.assertRaises(P.Compuerta):
            self.pr.corregir_brief(cid)                       # sin "revisé el brief"
        self.pr.marcar_revisado(cid, True)
        with self.assertRaises(P.Compuerta) as e:
            self.pr.corregir_brief(cid)                       # propuestas y faltas sin decidir
        self.assertIn("pendientes", str(e.exception))
        self.assertEqual(self.modelo.llamadas.get("corrector_brief"), None, "El corrector no se llama con pendientes.")

    def test_dejar_vacio_exige_explicacion(self):
        cid = self.pr.crear_caso(ORIGINAL)["id"]
        self.pr.desarrollar_brief(cid)
        with self.assertRaises(P.Compuerta):
            self.pr.decidir_campo(cid, "entrada.sujetos.items[].vestuario", "dejar_vacio", None, "")

    def test_brief_siempre_muestra_todos_los_campos(self):
        cid = self.pr.crear_caso(ORIGINAL)["id"]
        self.pr.desarrollar_brief(cid)
        caso = self.pr.leer(cid)
        self.assertEqual(len(caso["brief_actual"]), 109)

    def test_corrector_devuelve_al_usuario(self):
        cid = self.pr.crear_caso(ORIGINAL)["id"]
        self.pr.desarrollar_brief(cid)
        self.decidir_todo(cid)
        caso = self.pr.corregir_brief(cid)
        self.assertEqual(caso["etapa"], P.BRIEF_REVISION)
        self.assertFalse(caso["revision_completa"], "Tras una devolución el usuario debe revisar de nuevo.")
        self.assertEqual(len(caso["correccion"]["problemas"]), 1)
        with self.assertRaises(P.Compuerta):
            self.pr.seleccionar(cid)

    def test_nota_del_corrector_no_devuelve_el_brief(self):
        """Lo que solo el usuario puede decidir no es motivo de devolución (Eric, 2026-10-22)."""
        self.modelo.fallar_corrector_una_vez = False
        self.modelo.nota_en_corrector = True
        cid = self.pr.crear_caso(ORIGINAL)["id"]
        self.pr.desarrollar_brief(cid)
        self.decidir_todo(cid)
        caso = self.pr.corregir_brief(cid)
        self.assertEqual(caso["etapa"], P.BRIEF_VALIDADO)
        self.assertEqual(len(caso["correccion"]["notas"]), 1)
        self.assertEqual(caso["correccion"]["problemas"], [])

    def test_revision_del_brief_limitada_a_45_segundos(self):
        vistos = []

        def falso_post(url, cuerpo, cabeceras, segundos):
            vistos.append((segundos, cuerpo.get("max_tokens")))
            return {"content": [{"type": "text", "text": json.dumps({"observaciones": [], "observaciones_generales": ""})}]}

        original_post, clave = llm._post, os.environ.get("ANTHROPIC_API_KEY")
        os.environ["ANTHROPIC_API_KEY"] = "prueba"
        llm._post = falso_post
        try:
            pr = P.Proceso(self.almacen, llm.Anthropic(self.almacen))
            cid = pr.crear_caso(ORIGINAL)["id"]
            caso = self.almacen.leer_caso(cid)
            caso["desarrollo"] = self.modelo.desarrollador_brief(
                E.carga_desarrollo(pr.rec, ORIGINAL, [], []))
            caso["etapa"] = P.BRIEF_REVISION
            self.almacen.guardar_caso(caso)
            self.decidir_todo(cid, pr)
            caso = pr.corregir_brief(cid)
        finally:
            llm._post = original_post
            if clave is None:
                os.environ.pop("ANTHROPIC_API_KEY", None)
            else:
                os.environ["ANTHROPIC_API_KEY"] = clave
        self.assertEqual(caso["etapa"], P.BRIEF_VALIDADO)
        self.assertEqual(len(vistos), 1)
        self.assertLessEqual(vistos[0][0], 45)
        self.assertEqual(vistos[0][1], P.MAX_SALIDA_REVISION)

    def test_reabrir_invalida_lo_posterior(self):
        cid = self.hasta_brief_validado()
        self.pr.seleccionar(cid)
        caso = self.pr.reabrir_brief(cid)
        self.assertEqual(caso["etapa"], P.BRIEF_REVISION)
        self.assertIsNone(caso["seleccion"])
        self.assertIsNone(caso["brief_validado"])


class TestFlujoCompleto(Base):
    def test_recorrido_hasta_aprobar(self):
        cid = self.hasta_brief_validado()
        caso = self.pr.leer(cid)
        self.assertEqual(caso["etapa"], P.BRIEF_VALIDADO)

        caso = self.pr.seleccionar(cid)
        self.assertEqual(caso["etapa"], P.SELECCION_LISTA, "Más de dos por bloque avisa pero no bloquea.")
        self.assertEqual(caso["seleccion"]["conteos"]["Important Details"], 3)
        self.assertTrue(any(a["tipo"] == "mas_de_dos" for a in caso["seleccion"]["avisos"]))

        with self.assertRaises(P.Compuerta):
            self.pr.confirmar_plantilla(cid, "")             # quality no se inventa
        self.pr.confirmar_plantilla(cid, "high")

        caso = self.pr.redactar(cid)
        self.assertEqual(caso["revision_prompt"]["ronda"], 2, "La falla determinista (stunning) vuelve sola al redactor.")
        self.assertEqual(caso["etapa"], P.PROMPT_AMBIGUEDADES)
        with self.assertRaises(P.Compuerta):
            self.pr.redactar(cid)                             # ambigüedad sin decidir
        item = caso["ambiguedades"]["items"][0]
        self.pr.decidir_ambiguedad(cid, item["id"], "Plano medio corto, como dice el brief.", "solo_este_caso")
        caso = self.pr.redactar(cid)
        self.assertEqual(caso["etapa"], P.REVISION_FINAL)

        self.pr.comentar_final(cid, "Que el muelle sea de madera.")
        with self.assertRaises(P.Compuerta):
            self.pr.aprobar(cid)                              # comentario pendiente
        caso = self.pr.redactar(cid)
        self.assertEqual(caso["etapa"], P.REVISION_FINAL)
        caso = self.pr.aprobar(cid)
        self.assertEqual(caso["etapa"], P.APROBADO)

        doc = self.pr.exportar(cid)
        self.assertIn("Scene: Create a fishing pier", doc)
        self.assertIn(cargar().canonicos["INV-002343"]["texto"], doc, "La cabecera lleva el literal canónico.")
        self.assertIn("Quality: high", doc)

    def test_notas_quedan_vinculadas_a_la_regla(self):
        cid = self.hasta_brief_validado()
        self.pr.seleccionar(cid)
        self.pr.confirmar_plantilla(cid, "high")
        caso = self.pr.redactar(cid)
        item = caso["ambiguedades"]["items"][0]
        self.pr.decidir_ambiguedad(cid, item["id"], "Plano medio corto.", "casos_similares")
        notas = self.almacen.notas_para("otro-caso")
        self.assertEqual(notas[0]["regla_id"], item["regla_id"])
        self.assertEqual(notas[0]["decision"], "Plano medio corto.")


class TestValidadores(unittest.TestCase):
    def setUp(self):
        self.rec = cargar()

    def respuesta(self):
        return Modelo().desarrollador_brief(E.carga_desarrollo(self.rec, ORIGINAL, [], []))

    def test_desarrollo_valido(self):
        E.validar_desarrollo(self.rec, ORIGINAL, [])(self.respuesta())

    def test_rechaza_campo_omitido(self):
        r = self.respuesta()
        r["campos"].pop(5)
        with self.assertRaises(llm.RespuestaInvalida):
            E.validar_desarrollo(self.rec, ORIGINAL, [])(r)

    def test_rechaza_cita_inventada(self):
        r = self.respuesta()
        r["campos"][0] = dict(r["campos"][0], estado="proporcionado", valor="x", cita="esto no lo dijo el usuario")
        with self.assertRaises(llm.RespuestaInvalida):
            E.validar_desarrollo(self.rec, ORIGINAL, [])(r)

    def test_rechaza_condicion_inactiva_en_campo_siempre(self):
        r = self.respuesta()
        i = next(i for i, c in enumerate(r["campos"]) if c["path"] == "entrada.idioma_prompt")
        r["campos"][i] = dict(r["campos"][i], estado="condicion_inactiva", valor=None, fundamento="x")
        with self.assertRaises(llm.RespuestaInvalida):
            E.validar_desarrollo(self.rec, ORIGINAL, [])(r)

    def test_selector_exige_cita_del_brief(self):
        brief = [{"path": "entrada.formato.ratio", "valor": "16:9"}]
        malo = {"decisiones": [{"id": "X", "decision": "seleccionada", "bloque": "Scene", "campo_brief": "entrada.formato.ratio",
                                "cita_brief": "4:5", "razon": "r"}]}
        with self.assertRaises(llm.RespuestaInvalida):
            E.validar_selector(["X"], brief)(malo)

    def test_revisor_exige_cita_literal_en_dudas(self):
        malo = {"registros": [{"regla_id": "U-LABELS", "estado": "UNCERTAIN", "cita": "no está", "explicacion": "e", "pregunta": "p"}]}
        with self.assertRaises(llm.RespuestaInvalida):
            E.validar_revisor_prompt(["U-LABELS"], "Scene: Create a pier.")(malo)

    def test_deterministas(self):
        brief = [{"path": "entrada.formato.ratio", "valor": "16:9"}]
        slots = {s: "Create a scene." for s in E.SLOTS_GEN}
        slots["Important Details"] = 'A photorealistic and EPIC look, sign reading "EPIC SALE".'
        slots["Subject"] = "Una imagen fotorealista."
        r = E.comprobaciones_deterministas(slots, {"quality": "high", "tamano": "4:5"}, brief)
        reglas = [x["regla_id"] for x in r]
        self.assertEqual(reglas.count("USER::ERIC-DELEGATION-TERMS"), 2)
        self.assertEqual(reglas.count("U-ANTI-SLOP"), 1, "'EPIC' entre comillas es texto pedido, no elogio.")
        self.assertIn("U-TECHNICAL-ENVELOPE", reglas)
        ok = E.comprobaciones_deterministas({s: "Create a pier." for s in E.SLOTS_GEN}, {"quality": "high", "tamano": "1536x1024"}, brief)
        self.assertEqual(ok, [])


class TestManual(unittest.TestCase):
    def test_pegar_valida_y_continua(self):
        with tempfile.TemporaryDirectory() as d:
            almacen = P.Almacen(Path(d) / "m.sqlite3")
            pr = P.Proceso(almacen, llm.Manual(almacen))
            cid = pr.crear_caso(ORIGINAL)["id"]
            with self.assertRaises(llm.ManualPendiente) as m:
                pr.desarrollar_brief(cid)
            sol = m.exception.solicitud
            self.assertIn("texto_original", llm.texto_para_copiar(sol))
            pr.pegar_respuesta(sol["clave"], '{"campos": []}')
            with self.assertRaises(llm.RespuestaInvalida):
                pr.desarrollar_brief(cid, nueva=False)        # retomar con respuesta inválida: no avanza
            respuesta = Modelo().desarrollador_brief(sol["carga"])
            pr.pegar_respuesta(sol["clave"], "```json\n" + json.dumps(respuesta) + "\n```")
            caso = pr.desarrollar_brief(cid, nueva=False)
            self.assertEqual(caso["etapa"], P.BRIEF_REVISION)


class TestServidor(unittest.TestCase):
    def test_api_basica(self):
        import os
        import server
        with tempfile.TemporaryDirectory() as d:
            os.environ["TALLER_DB"] = str(Path(d) / "s.sqlite3")
            os.environ["TALLER_PROVEEDOR"] = "manual"
            server.ESTADO = server.Estado()
            srv = server.ThreadingHTTPServer(("127.0.0.1", 0), server.Manejador)
            hilo = threading.Thread(target=srv.serve_forever, daemon=True)
            hilo.start()
            base = f"http://127.0.0.1:{srv.server_port}"

            def post(ruta, cuerpo):
                req = urllib.request.Request(base + ruta, data=json.dumps(cuerpo).encode(), headers={"Content-Type": "application/json"})
                try:
                    with urllib.request.urlopen(req) as r:
                        return r.status, json.load(r)
                except urllib.error.HTTPError as e:
                    return e.code, json.load(e)

            estado = json.load(urllib.request.urlopen(base + "/api/estado"))
            self.assertEqual(estado["recursos_modificados"], [])
            codigo, caso = post("/api/casos", {"original": ORIGINAL})
            self.assertEqual(codigo, 200)
            codigo, error = post(f"/api/casos/{caso['id']}/plantilla", {"quality": "high"})
            self.assertEqual(codigo, 409)
            self.assertIn("no permitida", error["error"])
            html = urllib.request.urlopen(base + "/").read().decode()
            self.assertIn("Taller de prompts", html)
            srv.shutdown()


if __name__ == "__main__":
    unittest.main()
