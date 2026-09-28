"""Utilidades de prueba: base de proyectos temporal y helpers para llevar un proyecto a liberable
actuando como el director humano (decisiones explícitas, firmadas como 'test-humano')."""

import os
import sys
import tempfile
from pathlib import Path

APD = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APD))
_tmp = tempfile.mkdtemp(prefix="apd-test-")
os.environ["APD_DB"] = str(Path(_tmp) / "proyectos.sqlite")
os.environ.setdefault("APD_LLM", "none")
# las pruebas de lotes verifican el modo exhaustivo (todo el medio); el modo por defecto «abiertas» tiene su propia prueba
os.environ.setdefault("APD_REVISION", "todas")

from apd import datos, fuentes as F, store as ST  # noqa: E402
if not F.RULES_DB.exists() or not (F.DATA / "registro.json").exists():
    datos.construir()  # clon recién descargado: mismo paso que hace server.py al arrancar
ST.DB = Path(os.environ["APD_DB"])
from apd import proyecto as P, llm  # noqa: E402

BRIEF_QUINTETO = ("Cinco retratos de casting de un quinteto de cuerdas: tres mujeres y dos hombres de 22–28 años, "
                  "orígenes diversos, hombros hacia arriba, fondo gris claro, personalidades distintas y rostros naturales.")


def proyecto_quinteto(nombre="quinteto"):
    pid = P.nuevo({"texto": BRIEF_QUINTETO}, nombre)
    P.aceptar_propuestas(pid)
    P.aceptar_propuestas(pid)
    return pid


def resolver_como_humano(pid, autor="test-humano"):
    """Decide CONDICIONAL/CONFLICTO y asigna destino a APLICA sin evidencia, con razones concretas."""
    P.auditar(pid, originales=False)
    n, e = P.cargar(pid)
    for clave, led in e["_ledgers_completos"].items():
        dec = {}
        et = led["etiqueta"]
        for rid, d in led["decisiones"].items():
            if d["estado"] in ("CONDICIONAL", "CONFLICTO"):
                dec[rid] = {"estado": "NO_APLICA", "razon": f"condición no se da en esta entrega ({et}): génesis T1 sin storyboard ni referencias"}
        sin = set()
        for eid, a in e["auditorias"].items():
            if e["entregas"][eid]["perfil"] == clave:
                for c in a["controles"]:
                    if c["id"] == "evidencia_aplica":
                        sin |= set(c.get("ids", []))
        for rid in sin:
            dec[rid] = {"estado": "APLICA", "razon": f"guía de redacción general cumplida por el texto completo ({et})", "destino": ["estructura"]}
        if dec:
            P.decidir_reglas(pid, clave, dec, autor)
    return P.cargar(pid)


def liberar(pid, eid, originales=False):
    P.auditar(pid, originales=originales)
    n, e = P.cargar(pid)
    P.semantica_humana(pid, eid, "test-humano", "revisé la correspondencia regla-texto de este hash")
    n, e = P.cargar(pid)
    P.aprobar_redaccion(pid, eid, e["entregas"][eid]["compilado"]["hash"])
    return P.cargar(pid)
