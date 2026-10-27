"""probar_briefs_lote2.py: prueba `briefs/construir_briefs_lote2.py` con casos que deben pasar y casos que deben fallar.

    python3 -I taller/catalogo/v3/prueba/probar_briefs_lote2.py

Copia los dos constructores a una carpeta temporal dentro de `prueba/` (así resuelven las mismas rutas), cambia un dato
por prueba y comprueba el código de salida y el mensaje. Borra la carpeta al terminar. Sale con código 1 si un
resultado no es el esperado.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

PRUEBA = Path(__file__).resolve().parent
ORIG = PRUEBA / "briefs"
TMP = PRUEBA / "_tmp_probar_lote2"


def preparar(reemplazos=(), aprobaciones=None):
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir()
    shutil.copy(ORIG / "construir_briefs.py", TMP / "construir_briefs.py")
    s = (ORIG / "construir_briefs_lote2.py").read_text(encoding="utf-8")
    for a, b in reemplazos:
        assert s.count(a) == 1, f"el texto a reemplazar no aparece una sola vez: {a}"
        s = s.replace(a, b)
    (TMP / "construir_briefs_lote2.py").write_text(s, encoding="utf-8")
    if aprobaciones is not None:
        (TMP / "aprobaciones.json").write_text(json.dumps(aprobaciones), encoding="utf-8")


def correr():
    p = subprocess.run([sys.executable, "-I", str(TMP / "construir_briefs_lote2.py")], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def sha_de(kid, clave):
    x = json.loads((TMP / f"{kid}.contrato.json").read_text(encoding="utf-8"))
    sys.path.insert(0, str(TMP))
    import importlib
    l2 = importlib.import_module("construir_briefs_lote2")
    if clave == "brief_sha256":
        return l2.cb.brief_sha(x)
    return l2.contenido_sha(x["entrada"], json.loads((TMP / f"{kid}.referencias.json").read_text(encoding="utf-8")))


AP = {"mensaje_id": "prueba", "fecha": "2026-10-27T00:00:00Z", "texto": "ok", "documento": "prueba"}
casos = [
    ("lote tal cual", [], None, 0, "aprobados 0 · OK"),
    ("F24 con etiqueta fuera del esquema", [('plano="WS wide", angulo="low", altura="a la altura de la cadera',
                                             'plano="full body", angulo="low", altura="a la altura de la cadera')],
     None, 1, "F24 «full body» no está en el esquema"),
    ("composición sin el error esperado de referencia", [('ESPERADOS_CONTRATO = {"Falta campo: entrada.referencias", '
                                                          '"Operación requiere referencia real"}',
                                                          'ESPERADOS_CONTRATO = {"Falta campo: entrada.referencias", '
                                                          '"Operación requiere referencia real", "error inventado"}')],
     None, 1, "no aparecen los errores esperados"),
    ("campo del módulo fotografía vacío", [('contraste="medio"),\n   rostro=dict(ocupacion=0.02, detalles=["tres',
                                             'contraste=""),\n   rostro=dict(ocupacion=0.02, detalles=["tres')],
     None, 1, "Módulo incompleto: entrada.luz.contraste"),
    ("brief de armar.py con elogio vago", [('microdetalle="Individual stubble hairs', 'microdetalle="Stunning stubble hairs')],
     None, 1, "G1 armar.py"),
]
fallos = 0
for nombre, rep, aps, codigo_esperado, texto in casos:
    preparar(rep, aps)
    codigo, salida = correr()
    ok = codigo == codigo_esperado and texto in salida
    fallos += not ok
    print(("  ok    " if ok else "  FALLA ") + f"{nombre}: código {codigo}" + ("" if ok else f"\n        {salida[-600:]}"))

# Aprobación: con el sha correcto el caso queda aprobado; con otro, invalidada.
preparar()
correr()
buenos = {"G1": dict(AP, brief_sha256=sha_de("G1", "brief_sha256")),
          "K10": dict(AP, contenido_sha256=sha_de("K10", "contenido_sha256"))}
for nombre, aps, esperado in [("aprobación con sha correcto", buenos, "aprobados 2 · OK"),
                              ("aprobación con sha de otro brief", {"G1": dict(AP, brief_sha256="0" * 64)},
                               "aviso G1: el brief cambió")]:
    preparar(aprobaciones=aps)
    codigo, salida = correr()
    ok = codigo == 0 and esperado in salida
    if ok and "correcto" in nombre:
        g1 = json.loads((TMP / "G1.contrato.json").read_text(encoding="utf-8"))
        k10 = json.loads((TMP / "K10.caso.json").read_text(encoding="utf-8"))
        ok = g1.get("aprobacion_brief", {}).get("aprobado") is True and k10["aprobacion"]["aprobado"] is True
    fallos += not ok
    print(("  ok    " if ok else "  FALLA ") + f"{nombre}: código {codigo}" + ("" if ok else f"\n        {salida[-600:]}"))
shutil.rmtree(TMP, ignore_errors=True)
print("todo como se esperaba" if not fallos else f"{fallos} resultados inesperados")
sys.exit(1 if fallos else 0)
