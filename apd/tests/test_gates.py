"""Gates de liberación: omisión, duplicado, id inexistente, lote incompleto, NO_APLICA genérico,
auditoría caducada, y procesamiento por lotes con un proveedor simulado (reintento y bloqueo)."""

import copy
import json
import unittest

import util
from apd import auditoria as A, ledger as L, llm, proyecto as P, revision as RV, spec as S, plan as PL


def contexto():
    pid = util.proyecto_quinteto("gates")
    n, e = P.cargar(pid)
    clave = e["entregas"]["E1"]["perfil"]
    ent = e["spec"]["entregas"][0]
    se = P.spec_de_entrega(e["spec"], ent)
    perfil = L.perfil_de(se, e["plan"], ent)
    return pid, e, clave, ent, se, perfil


class TestValidacionLote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pid, cls.e, cls.clave, cls.ent, cls.se, cls.perfil = contexto()
        cls.anclas = L.anclas_brief(cls.perfil, cls.se)
        cls.ids = sorted(P.registro().reglas)[:10]

    def resp(self, ids, estado="APLICA", razon="comparte caso T1 y subproceso E5.2 con la entrega T1 gpt-image-2"):
        return {"decisiones": [{"id": i, "estado": estado, "razon": razon} for i in ids]}

    def test_lote_correcto(self):
        self.assertTrue(L.validar_lote(self.ids, self.resp(self.ids), self.anclas)["ok"])

    def test_regla_omitida(self):
        v = L.validar_lote(self.ids, self.resp(self.ids[:-1]), self.anclas)
        self.assertFalse(v["ok"])
        self.assertEqual(v["faltan"], [self.ids[-1]])

    def test_decision_duplicada(self):
        r = self.resp(self.ids)
        r["decisiones"].append(dict(r["decisiones"][0]))
        v = L.validar_lote(self.ids, r, self.anclas)
        self.assertFalse(v["ok"])
        self.assertEqual(v["duplicados"], [self.ids[0]])

    def test_id_inexistente(self):
        v = L.validar_lote(self.ids, self.resp(self.ids + ["deadbeef0000"]), self.anclas)
        self.assertFalse(v["ok"])
        self.assertEqual(v["inventados"], ["deadbeef0000"])

    def test_no_aplica_sin_razon_especifica(self):
        for razon in ["no aplica", "N/A", "No relevante.", "irrelevant", "no corresponde a esto"]:
            v = L.validar_lote(self.ids, self.resp(self.ids, "NO_APLICA", razon), self.anclas)
            self.assertFalse(v["ok"], razon)
        ok = L.validar_lote(self.ids, self.resp(self.ids, "NO_APLICA", "regla de medio VIDEO; esta entrega es imagen fija T1"), self.anclas)
        self.assertTrue(ok["ok"])

    def test_gate_mecanico_bloquea_faltante_y_ajeno(self):
        dec = copy.deepcopy(self.e["_ledgers_completos"][self.clave]["decisiones"])
        quitado = next(iter(dec))
        dec.pop(quitado)
        dec["deadbeef0000"] = {"estado": "APLICA", "razon": "x", "capa": "x"}
        g = L.gate_mecanico(P.registro(), dec, self.anclas)
        self.assertFalse(g["ok"])
        self.assertIn(quitado, g["faltan"])
        self.assertIn("deadbeef0000", g["ajenos"])

    def test_humano_no_puede_no_aplica_generico(self):
        rid = self.ids[0]
        with self.assertRaises(ValueError):
            P.decidir_reglas(self.pid, self.clave, {rid: {"estado": "NO_APLICA", "razon": "no aplica"}})
        with self.assertRaises(ValueError):
            P.decidir_reglas(self.pid, self.clave, {"deadbeef0000": {"estado": "APLICA", "razon": "x"}})


class TestLotesConModeloSimulado(unittest.TestCase):
    """El flujo automático completo con un proveedor falso: todos los ids, validación, reintento, bloqueo."""

    @classmethod
    def setUpClass(cls):
        cls.pid, cls.e, cls.clave, cls.ent, cls.se, cls.perfil = contexto()

    def tearDown(self):
        llm.fijar(None)

    def _prov(self, modo):
        estado = {"llamadas": 0}

        def fn(sistema, usuario):
            estado["llamadas"] += 1
            ids = usuario.split("IDS DE ESTE LOTE (")[1].split("): ", 1)[1].split("\n")[0].split(", ")
            ds = [{"id": i, "estado": "NO_APLICA", "razon": "regla revisada: no gobierna esta entrega T1 gpt-image-2 imagen fija"} for i in ids]
            if modo == "omite_siempre" or (modo == "omite_una_vez" and "RECHAZADA" not in usuario):
                ds = ds[:-1]
            if modo == "inventa":
                ds.append({"id": "deadbeef0000", "estado": "APLICA", "razon": "x"})
            return json.dumps({"decisiones": ds})
        p = llm.Falso(fn)
        p.estado = estado
        llm.fijar(p)
        return p

    def _run(self, modo, clave):
        p = self._prov(modo)
        dec = copy.deepcopy(self.e["_ledgers_completos"][self.clave]["decisiones"])
        r = RV.revisar_ledger(P.registro(), self.se, self.perfil, self.ent, dec, clave, self.pid, lote_n=200)
        return r, dec, p

    def test_todos_los_ids_revisados(self):
        r, dec, p = self._run("ok", "prueba-ok")
        self.assertTrue(r["completo"])
        self.assertEqual(r["lotes"], 7)  # 1,398 / 200 → 7 lotes; nunca se reduce el universo
        self.assertEqual(sum(1 for v in dec.values() if v.get("capa") == "modelo"), 1398)
        self.assertGreater(r["uso"]["entrada"], 0)

    def test_reintento_recupera_lote(self):
        r, dec, p = self._run("omite_una_vez", "prueba-reintento")
        self.assertTrue(r["completo"])
        self.assertEqual(r["uso"]["reintentos"], 7)

    def test_lote_incompleto_bloquea(self):
        r, dec, p = self._run("omite_siempre", "prueba-falla")
        self.assertFalse(r["completo"])
        self.assertEqual(len(r["fallidos"]), 7)
        g = L.gate_mecanico(P.registro(), dec, L.anclas_brief(self.perfil, self.se))
        self.assertFalse(g["ok"])
        self.assertTrue(any("lotes que no validaron" in b for b in g["bloqueos"]))

    def test_id_inventado_rechaza_lote(self):
        r, dec, p = self._run("inventa", "prueba-inventa")
        self.assertFalse(r["completo"])

    def test_reanudable(self):
        self._run("ok", "prueba-reanuda")
        p = self._prov("ok")
        dec = copy.deepcopy(self.e["_ledgers_completos"][self.clave]["decisiones"])
        r = RV.revisar_ledger(P.registro(), self.se, self.perfil, self.ent, dec, "prueba-reanuda", self.pid, lote_n=200)
        self.assertTrue(r["completo"])
        self.assertEqual(p.estado["llamadas"], 0)  # lotes ya validados no se repiten

    def test_sin_modelo_no_finge(self):
        llm.fijar(llm.Ninguno())
        with self.assertRaises(llm.SinModelo):
            P.revisar_con_modelo(self.pid, en_hilo=False)


class TestAuditoriaCaducada(unittest.TestCase):
    def test_texto_cambiado_invalida_liberacion(self):
        pid = util.proyecto_quinteto("caducada")
        util.resolver_como_humano(pid)
        n, e = util.liberar(pid, "E1")
        self.assertTrue(P.liberacion(e, "E1")["liberable"], P.liberacion(e, "E1")["bloqueos"])
        # hash distinto al auditado → bloqueo aunque todo lo demás esté bien
        lib = A.estado_liberacion(e["auditorias"]["E1"], "0" * 64, e["semantica"]["E1"], e["aprobaciones"]["E1"], [])
        self.assertFalse(lib["liberable"])
        self.assertTrue(any("cambió después de auditarse" in b for b in lib["bloqueos"]))



class TestSemanticaDisputaYHerencia(unittest.TestCase):
    """Un NO_CUMPLE semántico sólo se cierra corrigiendo el bloque o con autoridad citada; una firma humana no borra
    hallazgos de otro revisor; editar el contexto hereda la revisión de reglas visiblemente y bloquea hasta confirmar."""

    def _semantica_externa(self, pid, eid, nc):
        x = P.exportar_lotes_semantica(pid, eid)
        ids = [i for l in x["lotes"] for i in l["ids"]]
        vs = [{"id": i, "veredicto": "NO_CUMPLE" if i in nc else "CUMPLE", "bloque": "details", "evidencia": "prueba",
               "correccion": "corregir en el bloque fuente" if i in nc else ""} for i in ids]
        return x["texto_hash"], ids, P.importar_semantica(pid, eid, x["texto_hash"], vs, "revisor-prueba")

    def test_disputa_exige_autoridad_y_firma_no_borra(self):
        pid = util.proyecto_quinteto("disputa")
        util.resolver_como_humano(pid)
        P.auditar(pid, originales=False)
        h, ids, r = self._semantica_externa(pid, "E1", set())
        nc = ids[:2]
        h, ids, r = self._semantica_externa(pid, "E1", set(nc))
        self.assertTrue(r["ok"])
        n, e = P.cargar(pid)
        lib = P.liberacion(e, "E1")
        self.assertTrue(any("2 NO_CUMPLE abiertos" in b for b in lib["bloqueos"]), lib["bloqueos"])
        self.assertIn("_CON_2_NO_CUMPLE", lib["niveles"]["semantica"]["estado"])
        # la firma humana no cierra los hallazgos del otro revisor
        P.semantica_humana(pid, "E1", "director", "revisé el texto completo de E1")
        n, e = P.cargar(pid)
        self.assertEqual(e["semantica"]["E1"]["no_cumple_abiertos"], nc)
        # disputa sin autoridad verificable o sin razón: rechazada
        with self.assertRaises(ValueError):
            P.disputar_semantica(pid, "E1", nc[0], "porque sí", "una razón suficientemente larga para pasar", "director")
        with self.assertRaises(ValueError):
            P.disputar_semantica(pid, "E1", nc[0], ".claude/rules/DECISIONES.md:9", "corta", "director")
        for rid in nc:
            P.disputar_semantica(pid, "E1", rid, ".claude/rules/DECISIONES.md:9 (DECISIONES #2)",
                                 "el linter vigente v1.2-fupai da PASS sobre este mismo hash", "director")
        n, e = P.cargar(pid)
        self.assertEqual(e["semantica"]["E1"]["no_cumple_abiertos"], [])
        self.assertEqual(sorted(e["semantica"]["E1"]["disputados"]), sorted(nc))
        self.assertFalse(any("NO_CUMPLE" in b for b in P.liberacion(e, "E1")["bloqueos"]))

    def test_cambio_de_contexto_hereda_revision_y_bloquea_hasta_confirmar(self):
        # brief propio: la caché de revisión se comparte entre proyectos con brief y perfil idénticos (por diseño)
        pid = P.nuevo({"texto": util.BRIEF_QUINTETO + " Serie interna de prueba de herencia."}, "herencia")
        P.aceptar_propuestas(pid)
        P.aceptar_propuestas(pid)
        lotes = P.exportar_lotes_decision(pid)
        clave, per = next(iter(lotes["perfiles"].items()))
        resp = {str(l["indice"]): {"decisiones": [{"id": i, "estado": "NO_APLICA", "razon": "revisada para esta entrega T1 gpt-image-2 imagen fija"}
                                                  for i in l["ids"]]} for l in per["lotes"]}
        self.assertTrue(P.importar_lotes_decision(pid, clave, resp, "externo-prueba")["completo"])
        n, e = P.cargar(pid)
        self.assertTrue(all(d["capa"].startswith("externo") for d in e["_ledgers_completos"][clave]["decisiones"].values()
                            if d["capa"] != "humano"))
        r = P.cambiar_campos(pid, [{"ruta": "comunes.fondo", "valor": "plain seamless light grey (#D0D0D0) studio background"}])
        her = r["diferencias"]["revisiones_heredadas"][clave]
        self.assertEqual(her["campos_cambiados"], ["fondo"])
        self.assertIsNone(her["confirmada"])
        n, e = P.cargar(pid)
        led = e["_ledgers_completos"][clave]
        self.assertTrue(all(d["capa"].endswith("+heredada") for d in led["decisiones"].values() if d["capa"].startswith("externo")))
        self.assertGreater(sum(1 for d in led["decisiones"].values() if d["capa"].startswith("externo")), 1300)
        lib = P.liberacion(e, "E1")
        self.assertEqual(lib["niveles"]["cobertura"]["estado"], "HEREDADA_SIN_CONFIRMAR")
        self.assertTrue(lib["bloqueos"][0].startswith("revisión de reglas heredada"))
        P.nueva_version(pid, lambda est: None, "prueba", "versión sin cambio de contexto")
        n, e = P.cargar(pid)
        self.assertIsNone(e["_ledgers_completos"][clave]["herencia"]["confirmada"])  # no se auto-confirma
        self.assertEqual(e["_ledgers_completos"][clave]["herencia"]["campos_cambiados"], ["fondo"])
        with self.assertRaises(ValueError):
            P.confirmar_herencia(pid, clave, "director", "corta")
        P.confirmar_herencia(pid, clave, "director", "el valor hex del fondo no cambia qué reglas aplican a un retrato T1")
        n, e = P.cargar(pid)
        self.assertEqual(e["_ledgers_completos"][clave]["herencia"]["confirmada"]["autor"], "director")
        self.assertFalse(any("heredada" in b for b in P.liberacion(e, "E1")["bloqueos"]))
        # (antes de confirmar) una versión sin cambios de contexto no confirma sola la herencia pendiente: probado abajo
        # un cambio posterior del contexto exige una confirmación nueva
        P.cambiar_campos(pid, [{"ruta": "comunes.luz", "valor": "soft even frontal key light with gentle fill"}])
        n, e = P.cargar(pid)
        self.assertIsNone(e["_ledgers_completos"][clave]["herencia"]["confirmada"])


class TestConflictosSobreRevision(unittest.TestCase):
    def test_revision_externa_no_salta_el_catalogo_de_conflictos(self):
        pid = P.nuevo({"texto": util.BRIEF_QUINTETO + " Serie interna de prueba de conflictos."}, "cf-sobre-revision")
        P.aceptar_propuestas(pid)
        P.aceptar_propuestas(pid)
        lotes = P.exportar_lotes_decision(pid)
        clave, per = next(iter(lotes["perfiles"].items()))
        motor = {"7ba769efe2d7", "c0bc3ce2b122", "ed3f4a2ab62f", "f75cfcf75330", "4a2eeac6c89d"}
        resp = {str(l["indice"]): {"decisiones": [
            {"id": i, "estado": "APLICA" if i in motor else "NO_APLICA",
             "razon": "revisada para esta entrega T1 gpt-image-2 imagen fija"} for i in l["ids"]]} for l in per["lotes"]}
        self.assertTrue(P.importar_lotes_decision(pid, clave, resp, "externo-prueba")["completo"])
        n, e = P.cargar(pid)
        led = e["_ledgers_completos"][clave]
        for rid in motor:  # el revisor dijo APLICA, pero CF-MOTOR-SW30 está abierto: queda en CONFLICTO
            self.assertEqual(led["decisiones"][rid]["estado"], "CONFLICTO", rid)
        self.assertTrue(any("CONFLICTO" in b for b in led["gate"]["bloqueos"]))
        P.resolver_conflicto(pid, "CF-MOTOR-SW30", "b", "el director elige los 5 slots de GPT Image para castings", autor="director")
        n, e = P.cargar(pid)
        for rid in motor:
            self.assertEqual(e["_ledgers_completos"][clave]["decisiones"][rid]["estado"], "NO_APLICA", rid)


class TestMigracionClave(unittest.TestCase):
    def test_decisiones_del_director_sobreviven_a_un_cambio_de_clave(self):
        import copy
        pid = util.proyecto_quinteto("migracion")
        n, e = P.cargar(pid)
        clave = e["entregas"]["E1"]["perfil"]
        rid = next(k for k, v in e["_ledgers_completos"][clave]["decisiones"].items() if v["estado"] == "CONDICIONAL")
        P.decidir_reglas(pid, clave, {rid: {"estado": "NO_APLICA", "razon": "condición no se da en este casting T1 del quinteto"}}, "director")
        n, e = P.cargar(pid)
        # simular datos de una versión con otro formato de clave para el mismo perfil
        viejo = copy.deepcopy(e)
        viejo["decisiones_humanas"] = {"clave-antigua": viejo["decisiones_humanas"][clave]}
        viejo["_ledgers_completos"] = {"clave-antigua": viejo["_ledgers_completos"][clave]}
        for info in viejo["entregas"].values():
            info["perfil"] = "clave-antigua"
        est = copy.deepcopy(viejo)
        est = P.recalcular(est, previo=viejo)
        d = est["_ledgers_completos"][clave]["decisiones"][rid]
        self.assertEqual((d["estado"], d["capa"]), ("NO_APLICA", "humano"))


class TestConcurrencia(unittest.TestCase):
    def test_firma_durante_auditoria_no_se_pierde(self):
        import threading
        import time
        pid = util.proyecto_quinteto("carrera")
        t = threading.Thread(target=P.auditar, args=(pid,), kwargs={"originales": True})
        t.start()
        time.sleep(0.3)  # la auditoría con gates originales tarda segundos: la firma llega mientras corre
        P.semantica_humana(pid, "E1", "director", "firma enviada durante la auditoría")
        t.join()
        n, e = P.cargar(pid)
        self.assertEqual(e["semantica"]["E1"]["firmante"], "director")
        self.assertIn("E1", e["auditorias"])

if __name__ == "__main__":
    unittest.main()
