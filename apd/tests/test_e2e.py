"""Extremo a extremo: regresión del quinteto, hashes visible/copiado/exportado, invalidación selectiva,
recorridos (imagen, referencia, edición, clip, ancla, spot por track), feedback y evaluación visual."""

import io
import json
import re
import unittest
import zipfile

import util
from apd import fuentes as F, proyecto as P, store as ST

PKG = F.extraer_paquete()


def palabras(t):
    return set(re.findall(r"[a-z]{4,}", t.lower()))


class TestRegresionQuinteto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pid = util.proyecto_quinteto("regresion")
        cls.aud = P.auditar(cls.pid, originales=True)
        cls.n, cls.e = P.cargar(cls.pid)
        cls.textos = {k: v["compilado"]["texto"] for k, v in cls.e["entregas"].items()}

    def test_cinco_prompts(self):
        self.assertEqual(sorted(self.textos), ["E1", "E2", "E3", "E4", "E5"])

    def test_restricciones_del_brief_en_los_cinco(self):
        sexos = ["woman", "woman", "woman", "man", "man"]
        for (eid, t), sx in zip(sorted(self.textos.items()), sexos):
            self.assertIn("light grey", t, eid)
            self.assertRegex(t, r"(?i)head-and-shoulders|from the shoulders up", eid)
            self.assertRegex(t, r"(?i)natural faces|real skin texture|visible pores", eid)
            self.assertRegex(t, rf"\bA {sx}\b", eid)
            edad = int(re.search(r"(\d{2}) years old", t).group(1))
            self.assertTrue(22 <= edad <= 28, (eid, edad))
            self.assertNotIn("string quintet", t, eid)  # contexto del casting: en notas, no en el cuerpo (lean prose)
            notas = self.e["entregas"][eid]["compilado"]["notas"]["micro_gate"]["RIESGOS"]
            self.assertIn("string quintet", notas, eid)
            self.assertIn("Expression and posture:", t, eid)

    def test_camara_y_angulo_especificados(self):
        for eid, t in self.textos.items():
            self.assertIn("eye-level camera", t, eid)
            self.assertRegex(t, r"\d{2}mm|lens", eid)
            self.assertIn("Both eyes in sharp focus", t, eid)

    def test_no_son_variantes_genericas(self):
        origenes = {re.search(r"years old, (of [^.]+)\.", t).group(1) for t in self.textos.values()}
        self.assertEqual(len(origenes), 5, origenes)
        pers = {re.search(r"posture: ([^.]+)\.", t).group(1) for t in self.textos.values()}
        self.assertEqual(len(pers), 5)
        # Lo compartido (fondo, encuadre, cámara, luz) es restricción del brief y debe ser idéntico; lo que
        # distingue a cada persona son los segmentos ligados a sus campos propios. Ésos no pueden repetirse.
        variable = {}
        for eid, info in self.e["entregas"].items():
            b = {x["id"]: x for x in info["compilado"]["bloques"]}
            txt = " ".join(re.findall(r"(?:years old, [^.]+|posture: [^.]+|Distinct features: [^.]+)", b["subject"]["texto"] + " " + b["details"]["texto"]))
            variable[eid] = palabras(txt)
        ks = sorted(variable)
        for i, a in enumerate(ks):
            for b in ks[i + 1:]:
                inter = len(variable[a] & variable[b]) / len(variable[a] | variable[b])
                self.assertLess(inter, 0.25, (a, b, round(inter, 2)))
        for eid, t in self.textos.items():
            otros = set().union(*(palabras(x) for k, x in self.textos.items() if k != eid))
            self.assertGreaterEqual(len(palabras(t) - otros), 12, eid)  # palabras propias de esa persona

    def test_gates_originales_pasan(self):
        for eid, a in self.aud.items():
            o = a["originales"]
            self.assertEqual(o["gate_image"]["estado"], "PASS", eid)
            self.assertEqual(o["gate_dramaturgy"]["estado"], "PASS", eid)
            self.assertEqual(o["aurora"]["estado"], "PASS", eid)
            self.assertEqual(o["ast_gate"]["estado"], "PASS", eid)
            self.assertTrue(o["render_original"]["igual"], eid)

    def test_no_promete_alinear_ojos(self):
        notas = self.e["entregas"]["E1"]["compilado"]["notas"]["advertencia"]
        self.assertIn("no controlan físicamente el generador", notas)


class TestHashesEInvalidacion(unittest.TestCase):
    def test_visible_copiado_exportado_mismo_hash(self):
        pid = util.proyecto_quinteto("hash")
        util.resolver_como_humano(pid)
        for eid in ["E1", "E2", "E3", "E4", "E5"]:
            util.liberar(pid, eid)
        n, e = P.cargar(pid)
        for eid in e["entregas"]:
            h = e["entregas"][eid]["compilado"]["hash"]
            c = P.copiar(pid, eid)
            self.assertTrue(c["liberable"], c["bloqueos"])
            self.assertEqual(F.sha256_text(c["texto"]), h)
            self.assertEqual(c["hash_auditado"], h)
        data, man = P.exportar(pid, como_aprobado=True)
        z = zipfile.ZipFile(io.BytesIO(data))
        for eid in e["entregas"]:
            t = z.read(f"entregas/{eid}/prompt.txt").decode()
            self.assertEqual(F.sha256_text(t), e["entregas"][eid]["compilado"]["hash"])
        self.assertIn("ledger/" + e["entregas"]["E1"]["perfil"] + ".tsv", z.namelist())
        filas = z.read("ledger/" + e["entregas"]["E1"]["perfil"] + ".tsv").decode().strip().split("\n")
        self.assertEqual(len(filas) - 1, 1398)

        # cambiar sólo la edad de E2: E2 se regenera y pierde aprobación; E1, E3–E5 intactas
        r = P.cambiar_campos(pid, [{"ruta": "E2.edad", "valor": 26}])
        d = r["diferencias"]
        self.assertEqual(list(d["textos_cambiados"]), ["E2"])
        self.assertEqual(d["entregas_intactas"], ["E1", "E3", "E4", "E5"])
        self.assertEqual(d["bloques_regenerados"]["E2"], ["subject"])
        self.assertEqual(d["perfiles_cambiados"], [])
        self.assertFalse(P.copiar(pid, "E2")["liberable"])
        self.assertTrue(P.copiar(pid, "E1")["liberable"])
        with self.assertRaises(PermissionError):
            P.exportar(pid, como_aprobado=True)

    def test_cambio_de_modelo_invalida_todo_el_perfil(self):
        pid = util.proyecto_quinteto("modelo")
        r = P.cambiar_campos(pid, [{"ruta": "comunes.modelo", "valor": "nano-banana-pro"},
                                   {"ruta": "comunes.camara", "valor": "Portrait lens perspective, shallow depth of field"},
                                   {"ruta": "comunes.restricciones", "valor": "A single real photograph with no text, watermark or logo"}])
        d = r["diferencias"]
        self.assertEqual(sorted(d["perfiles_cambiados"]), ["E1", "E2", "E3", "E4", "E5"])
        self.assertTrue(d["reglas_con_estado_distinto"])
        n, e = P.cargar(pid)
        self.assertEqual(e["entregas"]["E1"]["compilado"]["formato"], "nano-banana")
        self.assertNotRegex(e["entregas"]["E1"]["compilado"]["texto"], r"\d{2}mm")

    def test_cambio_de_bloque_sin_cambio_de_reglas(self):
        pid = util.proyecto_quinteto("bloque")
        r = P.cambiar_campos(pid, [{"ruta": "comunes.fondo", "valor": "Plain seamless mid grey studio background"}])
        d = r["diferencias"]
        self.assertEqual(sorted(d["textos_cambiados"]), ["E1", "E2", "E3", "E4", "E5"])
        self.assertEqual(d["perfiles_cambiados"], [])
        self.assertTrue(all(v == ["scene"] for v in d["bloques_regenerados"].values()))

    def test_cambio_de_plantilla_invalida(self):
        from apd import compilador as C
        pid = util.proyecto_quinteto("plantilla")
        orig = C.FRASES["fondo"]
        try:
            C.FRASES["fondo"] = "Background: {fondo}."
            r = P.nueva_version(pid, lambda est: None, "test", "plantilla cambiada")
            self.assertEqual(sorted(r["diferencias"]["textos_cambiados"]), ["E1", "E2", "E3", "E4", "E5"])
        finally:
            C.FRASES["fondo"] = orig

    def test_referencia_cambia_recorrido(self):
        pid = util.proyecto_quinteto("ref")
        r = P.cambiar_campos(pid, [{"ruta": "comunes.referencias", "valor": [{"nombre": "look.png", "rol": "estilo"}]}])
        n, e = P.cargar(pid)
        self.assertTrue(r["diferencias"]["perfiles_cambiados"])
        self.assertIn("Image 1 (look.png) is a style reference", e["entregas"]["E1"]["compilado"]["texto"])


def correr(nombre, brief, cambios=(), gates=()):
    pid = P.nuevo(brief, nombre)
    P.aceptar_propuestas(pid)
    if cambios:
        P.cambiar_campos(pid, list(cambios))
    P.aceptar_propuestas(pid)
    for g in gates:
        P.aprobar_gate(pid, g, "aprobado en prueba")
    a = P.auditar(pid)
    return pid, a, P.cargar(pid)[1]


class TestRecorridos(unittest.TestCase):
    def test_clip_texto_a_video(self):
        pid, a, e = correr("clip", {"texto": "Clip de video de 5 segundos en Kling: una violinista toca de pie en un escenario oscuro.", "formato": "9:16"}, [
            {"ruta": "comunes.sujeto", "valor": "a violinist in her mid-twenties, black linen shirt"},
            {"ruta": "comunes.accion_video", "valor": "She draws the bow in one long slow stroke, eyes closed"},
            {"ruta": "comunes.movimiento", "valor": "Slow push-in"}, {"ruta": "comunes.angulo", "valor": "eye-level"},
            {"ruta": "comunes.luz", "valor": "One hard warm top light"}, {"ruta": "comunes.fondo", "valor": "Bare black stage"},
            {"ruta": "comunes.audio", "valor": "Solo violin note, no dialogue."}, {"ruta": "comunes.tratamiento", "valor": "narrativo"}])
        self.assertEqual(e["plan"]["recorrido"], "CLIP")
        t = e["entregas"]["E1"]["compilado"]["texto"]
        for etiqueta in ["[Character A:", "Scene.", "Action.", "Camera.", "Lighting.", "Audio.", "Negative field."]:
            self.assertIn(etiqueta, t)
        o = a["E1"]["originales"]
        self.assertEqual(o["ast_gate"]["estado"], "PASS")
        self.assertEqual(o["aurora"]["estado"], "NO_APLICA")  # el linter no tiene caso T2V
        led = e["ledgers"][e["entregas"]["E1"]["perfil"]]
        self.assertEqual(led["gate"]["decididas"], 1398)

    def test_imagen_con_referencia(self):
        pid, a, e = correr("ref", {"texto": "Retrato de cuerpo completo de la violinista usando su retrato aprobado como referencia de personaje, fondo gris claro.",
                                   "modelo": "gpt-image-2", "referencias": [{"nombre": "T1_vera.png", "rol": "personaje"}]}, [
            {"ruta": "comunes.sujeto", "valor": "The same violinist, standing, violin under her chin, bow raised"},
            {"ruta": "comunes.identidad", "valor": None, "estado": "NO_APLICA", "motivo": "la fija Image 1 (herencia mínima SW30 R5)"},
            {"ruta": "comunes.angulo", "valor": "eye-level"}, {"ruta": "comunes.camara", "valor": "50mm lens feel"},
            {"ruta": "comunes.luz", "valor": "Soft even frontal light"}, {"ruta": "comunes.textura", "valor": "Natural skin texture"},
            {"ruta": "E1.rasgos", "valor": "black linen shirt"}, {"ruta": "comunes.tratamiento", "valor": "comercial"},
            {"ruta": "comunes.encuadre", "valor": "Full-body framing, head to feet"}])
        self.assertEqual(e["plan"]["subtipo"], "con_referencia")
        self.assertEqual({t["codigo"] for t in e["plan"]["tareas"]} & {"E5.3", "E5.4"}, {"E5.3", "E5.4"})
        t = e["entregas"]["E1"]["compilado"]["texto"]
        self.assertIn("Image 1 (T1_vera.png) is the approved character reference — same face and clothes", t)
        self.assertEqual(a["E1"]["originales"]["gate_image"]["estado"], "PASS")

    def test_edicion(self):
        pid, a, e = correr("edicion", {"texto": "Edición quirúrgica: corregir los ojos del retrato aprobado, mantener todo lo demás igual.",
                                       "modelo": "gpt-image-2", "referencias": [{"nombre": "render.png", "rol": "edicion"}]},
                           [{"ruta": "comunes.cambio", "valor": "Both eyes looking together straight into the lens, pupils aligned"},
                            {"ruta": "comunes.formato", "valor": "2:3"}])
        t = e["entregas"]["E1"]["compilado"]["texto"]
        self.assertTrue(t.startswith("Edit Image 1"))
        self.assertIn("Change:", t)
        self.assertIn("Preserve:", t)
        for g in ("gate_image", "gate_dramaturgy", "aurora", "ast_gate"):
            self.assertEqual(a["E1"]["originales"][g]["estado"], "PASS", g)

    def test_ancla_tarjeta_y_gate_de_dependencias(self):
        brief = {"texto": "Ancla keyframe first frame para Kling: una clavadista entrando al agua, documental, un sujeto, instante pico.", "modelo": "nano-banana-pro"}
        pid = P.nuevo(brief, "ancla")
        n, e = P.cargar(pid)
        self.assertEqual(e["plan"]["recorrido"], "ANCLA")
        self.assertIn("comunes.tarjeta_d9", e["preflight"]["faltan"])  # flujo-anclas A1: no se genera con campos vacíos
        tarjeta = [{"ruta": f"comunes.tarjeta_{d}", "valor": v} for d, v in
                   {"d1": "keyframe_ff", "d2": "B_pico", "d3": "1", "d4": "documental", "d5": "deep teal water",
                    "d6": "MS, deep DOF", "d7": "hard midday sunlight", "d8": "nano-banana-pro", "d9": "low at water level"}.items()]
        campos = tarjeta + [
            {"ruta": "comunes.accion", "valor": "B_pico"}, {"ruta": "comunes.angulo", "valor": "low"},
            {"ruta": "E1.rasgos", "valor": "athletic woman diver, black one-piece swimsuit"},
            {"ruta": "comunes.sujeto", "valor": "A woman diver frozen mid-entry, hands first"},
            {"ruta": "comunes.identidad", "valor": None, "estado": "NO_APLICA", "motivo": "ancla sin maestro"},
            {"ruta": "comunes.encuadre", "valor": "Medium shot at the water surface"},
            {"ruta": "comunes.fondo", "valor": "Outdoor dive pool"}, {"ruta": "comunes.textura", "valor": "Skin texture with droplets"},
            {"ruta": "comunes.formato", "valor": "9:16"}, {"ruta": "comunes.color", "valor": "Natural colour photograph"},
            {"ruta": "comunes.camara", "valor": "Camera at water level"}, {"ruta": "comunes.luz", "valor": "Hard midday sunlight from above"}]
        P.aceptar_propuestas(pid)
        P.cambiar_campos(pid, campos)
        n, e = P.cargar(pid)
        self.assertIn("ANCLA_A2", e["entregas"]["E1"]["bloqueo"])  # dependencias canonizadas: OK humano
        P.aprobar_gate(pid, "A2", "no requiere génesis previa")
        a = P.auditar(pid)
        n, e = P.cargar(pid)
        self.assertIsNotNone(e["entregas"]["E1"]["compilado"])
        self.assertNotRegex(e["entregas"]["E1"]["compilado"]["texto"], r"\d{2}mm")
        self.assertEqual(a["E1"]["originales"]["aurora"]["estado"], "PASS", a["E1"]["originales"]["aurora"]["detalle"])

    def _spot(self, texto, esperado_track, esperadas):
        pid = P.nuevo({"texto": texto}, "spot " + esperado_track)
        n, e = P.cargar(pid)
        self.assertEqual(e["plan"]["track"], esperado_track)
        activas = [x["clave"] for x in e["plan"]["etapas"] if x["aplica"]]
        self.assertEqual(activas, esperadas)
        self.assertEqual(e["entregas"], {})
        shots = json.loads((PKG / "skills/storyboard-architect/examples/30s-pain-proof-promise/shots.json").read_text())
        P.cargar_shots(pid, shots)
        n, e = P.cargar(pid)
        self.assertEqual(len(e["entregas"]), 2 * len(shots["shots"]))
        bloqueadas = [k for k, v in e["entregas"].items() if v.get("bloqueo") and "gates" in v["bloqueo"]]
        return pid, e, bloqueadas

    def test_spot_express(self):
        pid, e, bloq = self._spot("Spot de 20 segundos para redes, un solo beat.", "EXPRESS", ["E4", "E5", "E6"])
        self.assertTrue(bloq)  # E4 requiere OK antes de producir prompts
        P.aprobar_gate(pid, "E4", "storyboard aprobado")
        n, e = P.cargar(pid)
        self.assertIn("series_lock.character", json.dumps(e["spec"]["entregas"][0]["campos"]["identidad"]))
        ff = e["entregas"]["shot_01-FF"]
        self.assertIsNotNone(ff["compilado"], ff.get("bloqueo"))
        v = ff["vinculos"]
        self.assertEqual(v["shot_id"], "shot_01")
        self.assertIn("shots_sha256", v)
        self.assertIn("E4", e["etapas"])
        self.assertIn("series_lock", json.dumps(e["spec"]["shots"]))

    def test_spot_standard(self):
        pid, e, bloq = self._spot("Spot de 60 segundos para una marca de café.", "STANDARD", ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"])
        self.assertEqual(set(e["plan"]["bloqueado_por_gates"]), {"OK_E0", "OK_E1", "OK_E2", "OK_E4"})

    def test_spot_film(self):
        pid, e, bloq = self._spot("Cortometraje brand film de 3 minutos para una marca.", "STANDARD" if False else "FILM",
                                  ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"])

    def test_shots_invalido_rechazado(self):
        pid = P.nuevo({"texto": "Spot de 20 segundos."}, "spot malo")
        with self.assertRaises(ValueError):
            P.cargar_shots(pid, {"version": "1.2", "shots": []})


class TestLongitud(unittest.TestCase):
    """Decisión del usuario 2026-09-28: longitud aspiracional; bloquea sólo por encima de 2× el máximo."""

    def test_corto_avisa_no_bloquea(self):
        pid = util.proyecto_quinteto("longitud")
        a = P.auditar(pid, originales=False)
        c = next(x for x in a["E1"]["controles"] if x["id"] == "longitud")
        self.assertTrue(c["ok"])
        self.assertFalse(c["obligatorio"])

    def test_mas_del_doble_bloquea_y_pide_regenerar(self):
        pid = util.proyecto_quinteto("longitud2")
        largo = ", ".join(["a small silver ring on the left index finger"] * 80)
        P.cambiar_campos(pid, [{"ruta": "E1.rasgos", "valor": largo}])
        a = P.auditar(pid, originales=False)
        c = next(x for x in a["E1"]["controles"] if x["id"] == "longitud")
        self.assertFalse(c["ok"])
        self.assertTrue(c["obligatorio"])
        self.assertIn("regenerar", c["detalle"])
        n, e = P.cargar(pid)
        self.assertTrue(any("longitud" in b for b in P.liberacion(e, "E1")["bloqueos"]))
        r = P.regenerar_por_longitud(pid, "E1")  # sin modelo: no finge, señala los bloques
        self.assertFalse(r["regenerado"])
        self.assertEqual(r["bloques_mas_largos"][0]["bloque"], "details")


class TestFeedbackYVisual(unittest.TestCase):
    def test_parece_render_y_ojos_con_imagen(self):
        pid = util.proyecto_quinteto("visual")
        n, e0 = P.cargar(pid)
        cob0 = e0["ledgers"][e0["entregas"]["E1"]["perfil"]]["gate"]
        fb = P.feedback(pid, "E1", "parece render")
        self.assertEqual(fb["primer_contrato"], "comunes.tratamiento")
        self.assertIn("comunes.textura", fb["contratos_en_orden"])
        fb2 = P.feedback(pid, "E1", "ojos desalineados")
        self.assertIn(fb2["primer_contrato"], ("comunes.angulo", "comunes.encuadre", "comunes.camara", "comunes.foco"))
        self.assertTrue(any("edición T5" in l for l in fb2["limites"]))
        img = (PKG / "skills/visual-asset-critic/examples/worked-run/frames/round-1/shot_01.png").read_bytes()
        arch = ST.guardar_archivo(img, "render_E1.png")
        arch["media_type"] = "image/png"
        v = P.evaluar_visual(pid, "E1", arch, [{"tipo": "apariencia_render", "nota": "piel cerosa"},
                                               {"tipo": "ojos_desalineados", "nota": "ojo izquierdo desviado"}], "REVISE")
        self.assertEqual({d["tipo"] for d in v["defectos"]}, {"apariencia_render", "ojos_desalineados"})
        self.assertTrue(all(d["contrato"] for d in v["defectos"]))
        n, e = P.cargar(pid)
        # el veredicto visual va aparte: la cobertura de reglas no cambia
        self.assertEqual(e["ledgers"][e["entregas"]["E1"]["perfil"]]["gate"], cob0)
        lib = P.liberacion(e, "E1", ST.visual_list(pid))
        self.assertEqual(lib["niveles"]["visual"]["estado"], "EVALUADO_CON_DEFECTOS")
        self.assertIn("no certifica", lib["niveles"]["visual"]["significa"])
        # aplicar la sugerencia recompila sólo lo dependiente del contrato
        r = P.cambiar_campos(pid, [{"ruta": "comunes.textura", "valor": fb["sugerencias"]["comunes.textura"]}])
        self.assertEqual(sorted(r["diferencias"]["textos_cambiados"]), ["E1", "E2", "E3", "E4", "E5"])
        self.assertTrue(all(b == ["details"] for b in r["diferencias"]["bloques_regenerados"].values()))


if __name__ == "__main__":
    unittest.main()
