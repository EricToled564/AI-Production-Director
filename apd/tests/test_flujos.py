"""Recorridos y flujos que no cubren test_e2e/test_gates: casos de imagen T2–T4, PROD, GRAF, MULTI;
ancla (D9 por acción y número de sujetos, inferencias A PRUEBA); ancla → clip con transferencia al motion
brief; evidencia débil como evidencia y no como veto; conflictos con autoridad; plantillas NUEVA etiquetadas;
campos que no aplican al medio."""

import json
import unittest

import util
from apd import fuentes as F, ledger as L, proyecto as P, propuestas as PR, spec as S

PKG = F.extraer_paquete()

# Lo que un usuario escribiría en Especificación para cerrar el preflight de cada caso (valores de prueba).
RELLENO = {
    "sujeto": "A person described in the brief", "identidad": "short dark hair, oval face, olive skin, brown eyes",
    "encuadre": "Medium shot, waist up", "angulo": "eye-level", "camara": "50mm lens feel, moderate depth of field",
    "luz": "Soft window light from camera left", "fondo": "Plain warm grey wall", "textura": "Natural skin texture",
    "color": "Natural colour", "restricciones": "no text, no watermark, no logo", "foco": "sharp focus on the subject",
    "uso": "reference image", "formato": "4:5", "tratamiento": "comercial", "producto": "a glass perfume bottle",
    "texto_en_imagen": "JAZZ 2026", "paneles": "three panels side by side", "accion": "A_pose",
}


def cerrar_preflight(pid):
    for _ in range(4):
        n, e = P.cargar(pid)
        faltan = [f for f in e["preflight"]["faltan"]]
        for info in e["entregas"].values():
            if info.get("bloqueo", "").startswith("preflight: faltan "):
                faltan += info["bloqueo"][len("preflight: faltan "):].split(", ")
        faltan = sorted(set(faltan))
        if not faltan:
            return e
        cambios = []
        for ruta in faltan:
            k = ruta.split(".", 1)[1]
            cambios.append({"ruta": ruta, "valor": RELLENO.get(k, f"valor de prueba para {k}")})
        P.cambiar_campos(pid, cambios)
    return P.cargar(pid)[1]


class TestCasosImagen(unittest.TestCase):
    BRIEFS = {
        "T2": "Retrato de cuerpo entero de una bailarina de flamenco, fondo negro, para GPT Image 2.",
        "T3": "Una mujer leyendo en un café junto a la ventana, luz de tarde, GPT Image 2.",
        "T4": "Dos hombres jugando ajedrez en un parque, conversación tensa, GPT Image 2.",
        "PROD": "Foto de producto: botella de perfume de vidrio sobre mármol blanco, sin persona, GPT Image 2.",
        "GRAF": "Póster gráfico tipográfico para un festival de jazz con el texto 'JAZZ 2026', GPT Image 2.",
        "MULTI": "Tríptico multi-panel de tres paneles con la misma modelo en tres poses, GPT Image 2.",
    }

    def test_detecta_caso_y_compila_con_gates_originales(self):
        for caso, texto in self.BRIEFS.items():
            with self.subTest(caso=caso):
                pid = P.nuevo({"texto": texto}, "caso " + caso)
                P.aceptar_propuestas(pid)
                n, e = P.cargar(pid)
                self.assertEqual([x["casos"] for x in e["spec"]["entregas"]], [[caso]], texto)
                e = cerrar_preflight(pid)
                comp = e["entregas"]["E1"].get("compilado")
                self.assertIsNotNone(comp, e["entregas"]["E1"].get("bloqueo"))
                a = P.auditar(pid)["E1"]["originales"]
                for g in ("gate_image", "gate_dramaturgy", "ast_gate"):
                    self.assertEqual(a[g]["estado"], "PASS", (caso, g, a[g].get("salida") or a[g].get("detalle")))
                self.assertTrue(a["render_original"]["igual"], caso)

    def test_dos_personas_en_un_cuadro_no_son_dos_entregas(self):
        sp = S.analizar_determinista({"texto": self.BRIEFS["T4"]})
        self.assertEqual(len(sp["entregas"]), 1)
        self.assertEqual(sp["comunes"]["tipo_tarea"]["valor"], ["T4"])
        # los retratos nombrados sí son entregas: regresión del quinteto
        self.assertEqual(len(S.analizar_determinista({"texto": util.BRIEF_QUINTETO})["entregas"]), 5)


class TestAncla(unittest.TestCase):
    def props_d9(self, texto):
        sp = S.analizar_determinista({"texto": texto})
        return sp, [p for p in PR.proponer(sp) if p["ruta"] == "comunes.tarjeta_d9"]

    def test_d9_por_accion_inferencia_a_prueba(self):
        sp, p = self.props_d9("Ancla keyframe para Kling: una clavadista, instante pico, un sujeto.")
        self.assertEqual(sp["comunes"]["tarjeta_d2"]["valor"], "B_pico")
        self.assertEqual([(x["valor"], x["clase"]) for x in p], [("low", "inferencia_a_prueba")])
        self.assertIn("A PRUEBA", p[0]["fuente"])
        self.assertIn("flujo-anclas.html", p[0]["fuente"])

    def test_d9_por_numero_de_sujetos_ensamble(self):
        sp, p = self.props_d9("Ancla keyframe para Kling: foto de equipo, grupo de cinco remeros, comercial.")
        self.assertEqual(sp["comunes"]["tarjeta_d3"]["valor"], "ensamble")
        self.assertEqual([(x["valor"], x["clase"]) for x in p], [("eye-level", "fuente")])

    def test_d9_explicito_del_brief_y_defecto_del_regex_original(self):
        # rules_v3.REGEX_FACETA d9 'high' contiene 'picado' sin límite de palabra: 'contrapicado' caería en high.
        from apd.flujos import rules_v3
        alto = next(p for d, v, p in rules_v3().REGEX_FACETA if d == "d9" and v == "high")
        self.assertTrue(alto.search("contrapicado"))  # el defecto existe en el original (no se modifica)
        sp, p = self.props_d9("Ancla keyframe para Kling: piloto derrapando, contrapicado, velocidad.")
        self.assertEqual(sp["comunes"]["tarjeta_d9"]["valor"], "low")
        self.assertEqual(p, [])  # ya decidido por el brief: no se propone

    def test_ancla_a_clip_transferencia_motion_brief(self):
        pid = P.nuevo({"texto": "Spot de 20 segundos para redes, un solo beat."}, "ancla-clip")
        shots = json.loads((PKG / "skills/storyboard-architect/examples/30s-pain-proof-promise/shots.json").read_text())
        P.cargar_shots(pid, shots)
        n, e = P.cargar(pid)
        for g in e["plan"]["bloqueado_por_gates"]:
            P.aprobar_gate(pid, g.replace("OK_", ""), "aprobado en prueba")
        n, e = P.cargar(pid)
        sh = shots["shots"][0]["id"]
        clip, ff = e["entregas"][f"{sh}-CLIP"], e["entregas"][f"{sh}-FF"]
        self.assertEqual(clip["vinculos"]["ancla"], f"{sh}-FF")
        self.assertEqual(clip["vinculos"]["shot_id"], ff["vinculos"]["shot_id"])
        campos = next(x for x in e["spec"]["entregas"] if x["id"] == f"{sh}-CLIP")["campos"]
        self.assertEqual(campos["referencias"]["valor"][0]["rol"], "frame_inicial")
        self.assertEqual(campos["identidad"]["estado"], "NO_APLICA")  # DECISIONES #3: el frame fija la identidad
        t = (clip.get("compilado") or {}).get("texto") or ""
        if t:
            self.assertTrue(t.startswith("Preserve identity"), t[:80])  # motion brief Kling: preserve-cue primero
            self.assertNotIn("Scene.", t)  # I2V: no re-describir la escena del frame


class TestEvidenciaYConflictos(unittest.TestCase):
    def test_evidencia_debil_no_descarta(self):
        pid = util.proyecto_quinteto("debil")
        n, e = P.cargar(pid)
        dec = e["_ledgers_completos"][e["entregas"]["E1"]["perfil"]]["decisiones"]
        debiles = [k for k, v in dec.items() if (v.get("evidencia") or {}).get("en_contra_debil")]
        self.assertTrue(debiles)
        for k in debiles:  # la faceta débil nunca es la causa del descarte (otra autoridad sí puede serlo)
            self.assertFalse(dec[k]["estado"] == "NO_APLICA" and dec[k]["razon"].startswith("faceta"), (k, dec[k]["razon"]))
        self.assertGreater(sum(1 for k in debiles if dec[k]["estado"] == "APLICA"), len(debiles) // 2)
        fuertes = [k for k, v in dec.items() if v["estado"] == "NO_APLICA" and "faceta" in v.get("razon", "")]
        for k in fuertes:  # descarte por faceta: origen fuerte, o d8 (modelo destino), la excepción documentada
            self.assertRegex(dec[k]["razon"], r"origen [^)]*(archivo|auditoria|manual)|faceta d8", k)

    def test_conflicto_se_resuelve_por_autoridad_o_por_decision_registrada(self):
        pid = P.nuevo({"texto": util.BRIEF_QUINTETO}, "conflicto")
        P.cambiar_campos(pid, [{"ruta": "comunes.tratamiento", "valor": None}])  # tratamiento sin decidir
        n, e = P.cargar(pid)
        cf = {c["id"]: c for led in e["ledgers"].values() for c in led["conflictos"]}
        self.assertIn("CF-LUZ-T1", cf)
        self.assertFalse(cf["CF-LUZ-T1"]["resuelto"])  # sin D4 no hay autoridad aplicable: queda abierto
        with self.assertRaises(ValueError):
            P.resolver_conflicto(pid, "CF-LUZ-T1", "b", "")
        with self.assertRaises(ValueError):
            P.resolver_conflicto(pid, "CF-LUZ-T1", "c", "una razón concreta y suficiente")
        self.assertIn("flujo-anclas", cf["CF-LUZ-T1"]["autoridad"])
        # decisión del director, registrada con autor y razón, sobre el conflicto abierto
        P.resolver_conflicto(pid, "CF-LUZ-T1", "a", "el director quiere luz documental dura en el casting", autor="director")
        n, e = P.cargar(pid)
        self.assertEqual(e["spec"]["decisiones_razon"]["CF-LUZ-T1"]["autor"], "director")
        c = next((c for led in e["ledgers"].values() for c in led["conflictos"] if c["id"] == "CF-LUZ-T1"), None)
        self.assertTrue(c is None or (c["resuelto"] and c["gana"] == "a" and c["origen_resolucion"] == "director"), c)
        # con el dato del brief (D4 = comercial) la autoridad documentada decide sola en otro proyecto
        pid2 = util.proyecto_quinteto("conflicto-autoridad")
        n, e = P.cargar(pid2)
        c = next((c for led in e["ledgers"].values() for c in led["conflictos"] if c["id"] == "CF-LUZ-T1"), None)
        self.assertTrue(c is None or (c["resuelto"] and c["gana"] == "b"), c)


class TestPlantillasYCampos(unittest.TestCase):
    def test_plantillas_originales_citadas_y_nuevas_etiquetadas(self):
        pl = json.loads((F.DATA / "plantillas.json").read_text())
        items = pl["plantillas"] if isinstance(pl, dict) else pl
        estados = {x["estado"] for x in items}
        self.assertTrue({"ORIGINAL", "NUEVA"} <= estados, estados)
        for x in items:
            if x["estado"] == "NUEVA":  # etiquetada como nueva y con nota que dice qué parte es original y cuál no
                self.assertTrue(len(x.get("nota", "")) > 40, x["id"])
            if x["estado"] in ("ORIGINAL", "SOURCE_RECONSTRUCTED"):
                self.assertTrue(x.get("archivo"), x["id"])
            for t in __import__("re").findall(r"tests/(test_\w+\.py)", x.get("nota", "")):
                self.assertTrue((util.APD / "tests" / t).exists(), f"{x['id']} cita {t}, que no existe")

    def test_campos_que_no_aplican_al_medio(self):
        clip = S.analizar_determinista({"texto": "Clip de video de 5 segundos para Kling: una ola rompiendo al atardecer."})
        img = S.analizar_determinista({"texto": util.BRIEF_QUINTETO})
        self.assertEqual(clip["comunes"]["medio"]["valor"], "video")
        req_clip, req_img = set(S.requeridos(clip)), set(S.requeridos(img))
        self.assertIn("movimiento", req_clip)
        self.assertNotIn("movimiento", req_img)
        self.assertNotIn("textura", req_clip)
        for k in ("cambio", "preservar"):
            self.assertEqual(img["comunes"][k]["estado"], "NO_APLICA")
            self.assertTrue(img["comunes"][k]["motivo"])



class TestCambioQuirurgico(unittest.TestCase):
    """U-2026-09-28-CAMBIO-QUIRURGICO: nivel 0 (medio) fijo, nivel 1 (perfil) re-revisa sólo reglas del medio, nivel 2
    (campo) toca sólo el bloque; un cambio menor hereda semántica y aprobación, uno dramático reabre sólo lo cambiado."""

    def _liberado(self):
        pid = util.proyecto_quinteto("quirurgico")
        util.resolver_como_humano(pid)
        util.liberar(pid, "E2")
        return pid

    def test_cambio_menor_hereda_semantica_y_aprobacion(self):
        pid = self._liberado()
        n, e = P.cargar(pid)
        edad = e["spec"]["entregas"][1]["campos"]["edad"]["valor"]
        r = P.cambiar_campos(pid, [{"ruta": "E2.edad", "valor": edad + 1}])
        self.assertEqual(r["diferencias"]["cambios"]["E2"]["tipo"], "menor")
        self.assertEqual(r["diferencias"]["bloques_regenerados"]["E2"], ["subject"])
        n, e = P.cargar(pid)
        self.assertTrue(e["semantica"]["E2"]["completo"])
        self.assertEqual(e["semantica"]["E2"]["texto_hash"], e["entregas"]["E2"]["compilado"]["hash"])
        self.assertEqual(e["aprobaciones"]["E2"]["texto_hash"], e["entregas"]["E2"]["compilado"]["hash"])
        P.auditar(pid, originales=False)  # la auditoría mecánica sí se repite
        n, e = P.cargar(pid)
        self.assertTrue(P.liberacion(e, "E2")["liberable"], P.liberacion(e, "E2")["bloqueos"])

    def test_cambio_dramatico_reabre_solo_lo_cambiado(self):
        pid = self._liberado()
        x0 = P.exportar_lotes_semantica(pid, "E2")  # revisión por regla completa del texto original
        todos = [i for l in x0["lotes"] for i in l["ids"]]
        P.importar_semantica(pid, "E2", x0["texto_hash"], [{"id": i, "veredicto": "CUMPLE", "bloque": "details"} for i in todos], "prueba")
        r = P.cambiar_campos(pid, [{"ruta": "E2.sexo", "valor": "man"}, {"ruta": "E2.edad", "valor": 65}])
        c = r["diferencias"]["cambios"]["E2"]
        self.assertEqual(c["tipo"], "dramatico")
        n, e = P.cargar(pid)
        sem = e["semantica"]["E2"]
        self.assertFalse(sem["completo"])
        self.assertTrue(sem["pendientes"])
        self.assertTrue(e["aprobaciones"]["E2"].get("invalidada"))
        x = P.exportar_lotes_semantica(pid, "E2")
        ids = [i for l in x["lotes"] for i in l["ids"]]
        self.assertEqual(sorted(ids), sorted(sem["pendientes"]))  # sólo lo que tocó el cambio
        vs = [{"id": i, "veredicto": "CUMPLE", "bloque": "subject", "evidencia": "revisado"} for i in ids]
        self.assertTrue(P.importar_semantica(pid, "E2", x["texto_hash"], vs, "prueba")["ok"])
        n, e = P.cargar(pid)
        self.assertTrue(e["semantica"]["E2"]["completo"])
        self.assertGreater(len(e["semantica"]["E2"]["veredictos"]), len(ids))  # lo heredado se conserva

    def test_nivel_0_otro_medio_no_se_re_revisa(self):
        pid = util.proyecto_quinteto("nivel0")
        lotes = P.exportar_lotes_decision(pid)
        ids = {i for per in lotes["perfiles"].values() for l in per["lotes"] for i in l["ids"]}
        reg = P.registro()
        self.assertFalse(any(reg.reglas[i]["medio"] == "VIDEO" for i in ids))
        self.assertEqual(len(ids), 1398 - sum(1 for r in reg.reglas.values() if r["medio"] == "VIDEO"))


class TestPlantillaBrief(unittest.TestCase):
    """Plantilla de brief: bloques = facetas de la base + bloques del prompt; cámara, luz, lugar y ángulo nunca se
    preguntan, se infieren; lo que dijo el usuario gana a cualquier inferencia; con modelo, el modelo la llena."""

    def test_camara_luz_lugar_angulo_nunca_se_preguntan(self):
        from apd import plantilla_brief as PB
        for texto in (util.BRIEF_QUINTETO, "Una mujer leyendo en un café junto a la ventana, luz de tarde, GPT Image 2.",
                      "Foto de producto: botella de perfume de vidrio sobre mármol blanco, sin persona.",
                      "Retrato de cuerpo entero de una bailarina de flamenco para GPT Image 2."):
            pid = P.nuevo({"texto": texto}, "plantilla")
            n, e = P.cargar(pid)
            preguntas = {a["campo"] for a in e["spec"]["ambiguedades"]}
            self.assertFalse(preguntas & PB.NUNCA_PREGUNTAR, (texto, preguntas & PB.NUNCA_PREGUNTAR))
            c = e["spec"]["comunes"]
            for k in ("camara", "luz", "angulo", "encuadre"):
                self.assertEqual(c[k]["estado"], "LOCKED", (texto, k))

    def test_lo_que_dijo_el_usuario_gana(self):
        pid = P.nuevo({"texto": "Una mujer leyendo en un café junto a la ventana, luz de tarde, GPT Image 2."}, "usuario-gana")
        n, e = P.cargar(pid)
        c = e["spec"]["comunes"]
        self.assertEqual(c["luz"]["origen"], "brief")
        self.assertIn("afternoon", c["luz"]["valor"])
        self.assertEqual(c["fondo"]["valor"], "a café interior")
        self.assertEqual(c["camara"]["origen"], "inferido_app")

    def test_bloques_alineados_con_facetas_y_prompt(self):
        from apd import plantilla_brief as PB
        from apd.flujos import rules_v3
        dims = set(rules_v3().FACETAS)
        for b in PB.BLOQUES:
            self.assertTrue(b["faceta"] in dims | {"caso", "medio", None}, b)
        pid = util.proyecto_quinteto("plantilla-slots")
        n, e = P.cargar(pid)
        filas = {f["bloque"]: f for f in PB.vista(e["spec"], "gpt-image-2")}
        slot = lambda b, k: next(x["slot"] for x in filas[b]["campos"] if x["campo"] == k)
        self.assertIn("Important Details:", slot("luz", "luz"))
        self.assertIn("Scene:", slot("lugar", "fondo"))

    def test_con_modelo_la_plantilla_la_llena_el_modelo(self):
        from apd import llm
        def fn(sistema, usuario):
            self.assertIn("PLANTILLA DE BRIEF", sistema)
            return json.dumps({"comunes": {"sujeto": {"valor": "a young woman reading a paperback", "origen": "inferido",
                                                      "porque": "el brief dice 'una mujer leyendo'"},
                                           "fondo": {"valor": "a small corner café with a wooden table", "origen": "inferido",
                                                     "porque": "el brief dice 'en un café'"}}, "entregas": []})
        llm.fijar(llm.Falso(fn))
        try:
            pid = P.nuevo({"texto": "Una mujer leyendo en un café, GPT Image 2."}, "plantilla-modelo")
        finally:
            llm.fijar(None)
        n, e = P.cargar(pid)
        c = e["spec"]["comunes"]
        self.assertEqual(c["sujeto"]["origen"], "inferido_modelo")
        self.assertIn("el brief dice", c["sujeto"]["fuente"])
        self.assertEqual(c["fondo"]["origen"], "brief")  # lo LOCKED del brief no lo pisa el modelo
        self.assertTrue(e["spec"]["plantilla_info"]["modelo"]["campos"])

if __name__ == "__main__":
    unittest.main()
