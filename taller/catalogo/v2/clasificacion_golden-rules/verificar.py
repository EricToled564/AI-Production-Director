"""verificar.py: corre el verificador del piloto (piloto_gpt-image/construir.py:verificar) sobre los lotes hechos.

    python3 -I verificar.py <última línea clasificada>

Comprueba forma, no acierto: cada texto hasta esa línea está en exactamente una aplicación o conciliación, todo valor
existe en la taxonomía, cada grupo obligatorio tiene valor y toda restricción lleva fundamento.
"""
import importlib.util
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
V2 = AQUI.parent
RAIZ = V2.parents[2]
sys.path.insert(0, str(V2))


def cargar(nombre, ruta):
    s = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


hasta = int(sys.argv[1])
B = cargar("construir_piloto", V2 / "piloto_gpt-image" / "construir.py")
B.C = cargar("clasificacion_gr", AQUI / "clasificacion.py")
cat = json.loads((RAIZ / "taller/catalogo/catalogo_imagen_gpt2.json").read_text(encoding="utf-8"))
unidades = [u for u in cat if u["archivo"] == "skills/image/references/golden-rules.md" and int(u["linea"]) <= hasta]
err = B.verificar(unidades, B.columnas())
print(f"textos hasta L{hasta}: {len(unidades)} · conciliaciones {len(B.C.CONCILIACIONES)} · aplicaciones "
      f"{len(B.C.APLICACIONES)} · " + ("VERIFICACIÓN DE FORMA: sin errores" if not err else f"{len(err)} ERRORES"))
print("\n".join(err))
sys.exit(1 if err else 0)
