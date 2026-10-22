"""Carga el caso real de spinning en la base del taller y deja el brief listo para la revisión de Eric.

Pasos que ejecuta, por las mismas compuertas que la interfaz:
  1. guarda el texto original sin modificar y la respuesta previa de Eric como aporte;
  2. pide el desarrollo del brief en modo manual y pega desarrollo_spinning.json (respuesta del rol
     desarrollador_brief producida por Claude); la app la valida antes de aceptarla.
Se detiene en el paso 3: la revisión del brief es de Eric.

    python taller/demo/cargar_demo.py [ruta_db]
"""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))

import llm  # noqa: E402
import proceso as P  # noqa: E402
from generar_desarrollo_spinning import construir  # noqa: E402


def main():
    ruta_db = sys.argv[1] if len(sys.argv) > 1 else str(AQUI.parent / "datos" / "taller.sqlite3")
    almacen = P.Almacen(ruta_db)
    pr = P.Proceso(almacen, llm.Manual(almacen))
    original = (AQUI / "ORIGINAL_SPINNING.txt").read_text(encoding="utf-8")
    caso = pr.crear_caso(original)
    pr.agregar_aporte(caso["id"], (AQUI / "RESPUESTA_USUARIO_PREVIA.txt").read_text(encoding="utf-8"))
    try:
        pr.desarrollar_brief(caso["id"])
    except llm.ManualPendiente as m:
        pr.pegar_respuesta(m.solicitud["clave"], json.dumps(construir(), ensure_ascii=False))
    caso = pr.desarrollar_brief(caso["id"], nueva=False)
    leido = pr.leer(caso["id"])
    conteo = {}
    for c in leido["brief_actual"]:
        conteo[c["estado_desarrollo"]] = conteo.get(c["estado_desarrollo"], 0) + 1
    print("caso:", caso["id"], "etapa:", caso["etapa"])
    print("estados:", conteo)
    print("pendientes para Eric:", len(leido["pendientes_brief"]))


if __name__ == "__main__":
    main()
