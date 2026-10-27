"""probar_validar_caso.py: casos/validar.py con las formas de caso que el plan necesita.

    python3 -I taller/catalogo/v3/prueba/probar_validar_caso.py

`validar.py` imprime `case_gate_errors` y sale con código 0 aunque haya errores; el control de la tarea 3 tiene que leer
esa lista. Este archivo lo corre sobre casos de prueba y comprueba el resultado por la lista, no por el código de salida:
- un caso con valores originales (option_ids del catálogo) y uno con un valor de extensión aprobada (F10 «edición:
  quitar objeto», sin id en el catálogo: option_ids vacío y la decisión como evidencia) pasan;
- sin confirmar, con un id desconocido, con requisito sin resolver o sin aprobación, el caso queda BLOQUEADO.
Sale con código 1 si un resultado no es el esperado.
"""
import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

CASOS = Path(__file__).resolve().parents[2] / "fuentes_20261019/CASOS_OPCIONES_TAXONOMIA_20261019/casos"
SHA_TAX = json.loads((CASOS / "manifest_fuentes.json").read_text(encoding="utf-8"))["taxonomy"]["sha256"]


def correr(caso):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(caso, f, ensure_ascii=False)
    p = subprocess.run([sys.executable, "-I", "-c",
                        f"import sys,runpy; sys.argv=['validar.py', {f.name!r}]; sys.path.insert(0, {str(CASOS)!r}); "
                        f"runpy.run_path({str(CASOS / 'validar.py')!r}, run_name='__main__')"],
                       capture_output=True, text=True)
    Path(f.name).unlink()
    if p.returncode != 0:
        return None, p.stderr[-400:], p.returncode
    out = json.loads(p.stdout)
    return out.get("case_gate_errors"), out.get("case_gate"), p.returncode


base = {"case_id": "K01", "taxonomy_sha256": SHA_TAX, "brief_literal": "rostro maestro",
        "campos": [{"path": "entrada.sujetos.items[].clase", "valor": "persona", "origen": "USUARIO",
                    "option_ids": ["OPT-PERSONA"], "evidencia": "brief", "confirmado": True}],
        "requisitos_de_completitud": [{"path": "entrada.sujetos", "motivo": "génesis", "resuelto": True}],
        "aprobacion": {"aprobado": True, "evidencia": "mensaje"}}
rows = json.loads((CASOS / "catalogo_opciones.json").read_text(encoding="utf-8"))
persona = next(r["id"] for r in rows if r["facet"] == "F15" and r["label"] == "persona" and r["case_selectable"])
base["campos"][0]["option_ids"] = [persona]

pruebas = [("valores originales con option_ids", base, False)]
ext = copy.deepcopy(base)
ext["case_id"] = "K14"
ext["campos"].append({"path": "entrada.operacion", "valor": "edición: quitar objeto", "origen": "USUARIO",
                      "option_ids": [], "evidencia": "extensión aprobada DECISIONES_ERIC_20261023 §4", "confirmado": True})
pruebas.append(("valor de extensión con option_ids vacío", ext, False))
for nombre, cambio in [
        ("dato sin confirmar", lambda c: c["campos"][0].update(confirmado=False)),
        ("id de opción desconocido", lambda c: c["campos"][0].update(option_ids=["TRM-9999"])),
        ("requisito sin resolver", lambda c: c["requisitos_de_completitud"][0].update(resuelto=False)),
        ("sin aprobación", lambda c: c.update(aprobacion={"aprobado": False, "evidencia": ""})),
        ("huella de taxonomía cambiada", lambda c: c.update(taxonomy_sha256="0" * 64)),
        ("ruta fuera del template", lambda c: c["campos"][0].update(path="entrada.inventado"))]:
    c = copy.deepcopy(base)
    cambio(c)
    pruebas.append((nombre, c, True))

fallos = 0
for nombre, caso, bloquear in pruebas:
    errores, gate, codigo = correr(caso)
    ok = errores is not None and bool(errores) == bloquear and codigo == 0
    fallos += not ok
    print(("  ok    " if ok else "  FALLA ") + f"{nombre}: código {codigo}, {gate}, errores {errores}")
print(f"{len(pruebas) - fallos}/{len(pruebas)} como se esperaba (código de salida de validar.py: siempre 0)")
sys.exit(1 if fallos else 0)
