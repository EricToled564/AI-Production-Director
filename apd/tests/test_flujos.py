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


if __name__ == "__main__":
    unittest.main()
