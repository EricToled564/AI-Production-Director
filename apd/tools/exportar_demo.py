"""Exporta el proyecto demo: zip borrador (el demo no es liberable: quedan decisiones del director), un .txt por
prompt con su sha256, la auditoría de cada entrega y un resumen de estado. Uso:
    APD_DB=apd/demo/demo.sqlite python3 apd/tools/exportar_demo.py <pid>"""

import json
import sys
from collections import Counter
from pathlib import Path

APD = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APD))
from apd import fuentes as F, proyecto as P, store as ST  # noqa: E402


def main(pid: str) -> int:
    out = APD / "demo"
    (out / "prompts").mkdir(parents=True, exist_ok=True)
    (out / "auditorias").mkdir(parents=True, exist_ok=True)
    n, e = P.cargar(pid)
    data, man = P.exportar(pid, como_aprobado=False)
    (out / "export_borrador.zip").write_bytes(data)
    resumen = {"proyecto": pid, "version": n, "registro": P.registro().version, "brief": e["brief"]["texto"],
               "exportacion": {"archivo": "export_borrador.zip", "sha256": F.sha256_file(out / "export_borrador.zip"),
                               "tipo": man["tipo"]}, "entregas": {}}
    for clave, led in e["_ledgers_completos"].items():
        resumen["ledger"] = {"perfil": led["etiqueta"], "por_estado": dict(Counter(d["estado"] for d in led["decisiones"].values())),
                             "por_capa": dict(Counter(d["capa"].split(":")[0].split("+")[0] for d in led["decisiones"].values())),
                             "conflictos": [{k: c[k] for k in ("id", "resuelto", "gana", "razon")} for c in led["conflictos"]],
                             "herencia": led.get("herencia")}
    for eid, info in e["entregas"].items():
        comp = info["compilado"]
        (out / "prompts" / f"{eid}.txt").write_text(comp["texto"], encoding="utf-8")
        a = e["auditorias"].get(eid) or {}
        (out / "auditorias" / f"{eid}.json").write_text(json.dumps(a, ensure_ascii=False, indent=1), encoding="utf-8")
        lib = P.liberacion(e, eid, [v for v in ST.visual_list(pid) if v["entrega_id"] == eid])
        sem = e["semantica"].get(eid) or {}
        resumen["entregas"][eid] = {
            "sha256": comp["hash"], "palabras": len(comp["texto"].split()),
            "gates_originales": {k: (v.get("estado") or ("PASS" if v.get("igual") else "DISTINTO")) for k, v in a.get("originales", {}).items()},
            "niveles": {k: v["estado"] for k, v in lib["niveles"].items()},
            "semantica": {"revisor": sem.get("revisor"), "resumen": sem.get("resumen"),
                          "no_cumple_abiertos": sem.get("no_cumple_abiertos"), "disputados": sorted(sem.get("disputados", {}))},
            "liberable": lib["liberable"], "bloqueos": lib["bloqueos"]}
    (out / "estado_demo.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in resumen.items() if k != "entregas"}, ensure_ascii=False)[:600])
    for eid, x in resumen["entregas"].items():
        print(eid, x["sha256"][:12], x["niveles"], "liberable" if x["liberable"] else f"bloqueada ({len(x['bloqueos'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
