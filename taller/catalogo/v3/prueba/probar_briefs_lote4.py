"""probar_briefs_lote4.py: prueba `briefs/construir_briefs_lote4.py` con casos que deben pasar y casos que deben fallar.

    python3 -I taller/catalogo/v3/prueba/probar_briefs_lote4.py

Igual que `probar_briefs_lote3.py`: copia los constructores a una carpeta temporal dentro de `prueba/`, cambia un dato por prueba y comprueba el código de salida
y el mensaje. Sale con código 1 si un resultado no es el esperado.
"""
import importlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

PRUEBA = Path(__file__).resolve().parent
ORIG = PRUEBA / "briefs"
TMP = PRUEBA / "_tmp_probar_lote4"
ENTRADAS = ()


def preparar(reemplazos=(), aprobaciones=None):
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir()
    for f in ["construir_briefs.py", "construir_briefs_lote2.py"] + [f"{k}.contrato.json" for k in ENTRADAS]:
        shutil.copy(ORIG / f, TMP / f)
    s = (ORIG / "construir_briefs_lote4.py").read_text(encoding="utf-8")
    for a, b in reemplazos:
        assert s.count(a) == 1, f"el texto a reemplazar no aparece una sola vez: {a}"
        s = s.replace(a, b)
    (TMP / "construir_briefs_lote4.py").write_text(s, encoding="utf-8")
    if aprobaciones is not None:
        (TMP / "aprobaciones.json").write_text(json.dumps(aprobaciones), encoding="utf-8")


def correr():
    p = subprocess.run([sys.executable, "-I", str(TMP / "construir_briefs_lote4.py")], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


casos = [
    ("lote tal cual", [], 0, "aprobados 0 · OK"),
    ("propiedades de estilo vacías", [('transferencia=dict(propiedades=["paleta de la imagen 2', 'transferencia=dict(propiedades=[], no_usado=["paleta de la imagen 2'),
                                      ('def edicion(entrada,', 'def _quitar(d):\n    d["transferencia"].pop("no_usado")\n    return d\n\n\ndef edicion(entrada,'),
                                      ('LOTE_4 = {k: LOTE_4[k] for k', '_quitar(LOTE_4["K26"])\nLOTE_4 = {k: LOTE_4[k] for k')],
     1, "Lista vacía en campo exigido: entrada.transferencia.propiedades"),
    ("estilo fuera del esquema", [('estilo=["comercial pulido"], representacion=["fotorrealista"],\n   motivo_ref="T-STYLE',
                                   'estilo=["cinematic"], representacion=["fotorrealista"],\n   motivo_ref="T-STYLE')],
     1, "F17 «cinematic» no está en el esquema"),
    ("brief de armar.py con palabra prohibida", [('the wool weave and the tie', 'the gorgeous wool weave and the tie')],
     1, "E5 armar.py"),
    ("edición sin cambio", [('"colorear la foto en blanco y negro con colores propios de los años cincuenta y tonos de piel naturales"', '""')],
     1, "Campo sin resolver: entrada.edicion.cambio"),
]
fallos = 0
for nombre, rep, codigo_esperado, texto in casos:
    preparar(rep)
    codigo, salida = correr()
    ok = codigo == codigo_esperado and texto in salida
    fallos += not ok
    print(("  ok    " if ok else "  FALLA ") + f"{nombre}: código {codigo}" + ("" if ok else f"\n        {salida[-600:]}"))

# Aprobación ligada al sha256 del contenido.
preparar()
correr()
sys.path.insert(0, str(TMP))
l2 = importlib.import_module("construir_briefs_lote2")
x = json.loads((TMP / "K17.contrato.json").read_text(encoding="utf-8"))
refs = json.loads((TMP / "K17.referencias.json").read_text(encoding="utf-8"))
AP = {"mensaje_id": "prueba", "fecha": "2026-10-27T00:00:00Z", "texto": "ok", "documento": "prueba"}
for nombre, aps, esperado in [("aprobación con sha correcto", {"K17": dict(AP, contenido_sha256=l2.contenido_sha(x["entrada"], refs))},
                               "aprobados 1 · OK"),
                              ("aprobación con sha de otro brief", {"K17": dict(AP, contenido_sha256="0" * 64)},
                               "aviso K17: el brief cambió")]:
    preparar(aprobaciones=aps)
    codigo, salida = correr()
    ok = codigo == 0 and esperado in salida
    fallos += not ok
    print(("  ok    " if ok else "  FALLA ") + f"{nombre}: código {codigo}" + ("" if ok else f"\n        {salida[-600:]}"))
shutil.rmtree(TMP, ignore_errors=True)
print("todo como se esperaba" if not fallos else f"{fallos} resultados inesperados")
sys.exit(1 if fallos else 0)
