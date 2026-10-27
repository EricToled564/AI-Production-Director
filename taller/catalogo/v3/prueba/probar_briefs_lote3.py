"""probar_briefs_lote3.py: prueba `briefs/construir_briefs_lote3.py` con casos que deben pasar y casos que deben fallar.

    python3 -I taller/catalogo/v3/prueba/probar_briefs_lote3.py

Igual que `probar_briefs_lote2.py`: copia los constructores a una carpeta temporal dentro de `prueba/` junto con los
contratos de las imágenes de entrada (de ahí sale el formato), cambia un dato por prueba y comprueba el código de salida
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
TMP = PRUEBA / "_tmp_probar_lote3"
ENTRADAS = ("K02", "K03", "K05", "K08", "K09", "K10")


def preparar(reemplazos=(), aprobaciones=None):
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir()
    for f in ["construir_briefs.py", "construir_briefs_lote2.py"] + [f"{k}.contrato.json" for k in ENTRADAS]:
        shutil.copy(ORIG / f, TMP / f)
    s = (ORIG / "construir_briefs_lote3.py").read_text(encoding="utf-8")
    for a, b in reemplazos:
        assert s.count(a) == 1, f"el texto a reemplazar no aparece una sola vez: {a}"
        s = s.replace(a, b)
    (TMP / "construir_briefs_lote3.py").write_text(s, encoding="utf-8")
    if aprobaciones is not None:
        (TMP / "aprobaciones.json").write_text(json.dumps(aprobaciones), encoding="utf-8")


def correr():
    p = subprocess.run([sys.executable, "-I", str(TMP / "construir_briefs_lote3.py")], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


casos = [
    ("lote tal cual", [], 0, "aprobados 0 · OK"),
    ("cambio de edición vacío", [('"dar a la banqueta del primer plano textura de adoquín de basalto gris, mate y rugosa"',
                                  '""')], 1, "Campo sin resolver: entrada.edicion.cambio"),
    ("selección de faceta fuera del esquema",
     [('motivo_requisitos="campo exigido por T-EDIT",', 'motivo_requisitos="campo exigido por T-EDIT", '
                                                         'estilo=["fotorrealista"],')],
     1, "F17 «fotorrealista» no está en el esquema"),
    ("imagen de entrada sin contrato", [('"K14": edicion("K14", "K02",', '"K14": edicion("K14", "K99",')],
     1, "K99.contrato.json"),
]
fallos = 0
for nombre, rep, codigo_esperado, texto in casos:
    preparar(rep)
    codigo, salida = correr()
    ok = codigo == codigo_esperado and texto in salida
    fallos += not ok
    print(("  ok    " if ok else "  FALLA ") + f"{nombre}: código {codigo}" + ("" if ok else f"\n        {salida[-600:]}"))

# Sin la referencia prevista, el contrato ya no da los errores esperados por referencia pendiente: debe fallar.
preparar([('referencias=[dict(indice=1, entrada=entrada, medio="imagen", rol="imagen a editar", preservar=preservar)])',
           'referencias_quitadas=True)')])
codigo, salida = correr()
ok = codigo == 1 and "Falta campo: entrada.referencias" in salida
fallos += not ok
print(("  ok    " if ok else "  FALLA ") + f"sin referencia prevista: código {codigo}" + ("" if ok else f"\n        {salida[-600:]}"))

# Aprobación ligada al sha256 del contenido.
preparar()
correr()
sys.path.insert(0, str(TMP))
l2 = importlib.import_module("construir_briefs_lote2")
x = json.loads((TMP / "K24.contrato.json").read_text(encoding="utf-8"))
refs = json.loads((TMP / "K24.referencias.json").read_text(encoding="utf-8"))
AP = {"mensaje_id": "prueba", "fecha": "2026-10-27T00:00:00Z", "texto": "ok", "documento": "prueba"}
for nombre, aps, esperado in [("aprobación con sha correcto", {"K24": dict(AP, contenido_sha256=l2.contenido_sha(x["entrada"], refs))},
                               "aprobados 1 · OK"),
                              ("aprobación con sha de otro brief", {"K24": dict(AP, contenido_sha256="0" * 64)},
                               "aviso K24: el brief cambió")]:
    preparar(aprobaciones=aps)
    codigo, salida = correr()
    ok = codigo == 0 and esperado in salida
    fallos += not ok
    print(("  ok    " if ok else "  FALLA ") + f"{nombre}: código {codigo}" + ("" if ok else f"\n        {salida[-600:]}"))
shutil.rmtree(TMP, ignore_errors=True)
print("todo como se esperaba" if not fallos else f"{fallos} resultados inesperados")
sys.exit(1 if fallos else 0)
