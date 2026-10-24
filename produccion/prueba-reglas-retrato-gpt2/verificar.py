"""Verificación mecánica de los veredictos por texto y caso.

Uso: python3 verificar.py <carpeta_de_veredictos> [lote_XX]   (p. ej. veredictos/pasada_1 lote_03)
Comprueba, por lote: cada id del lote aparece exactamente una vez, ningún id ajeno, tipo válido, y en los textos
normativos los cinco casos quedan cubiertos exactamente una vez (en `aplica` o en `fuera`, con motivo no vacío y
efecto no vacío si aplica a algún caso). Sale con código 1 si algo falla.
"""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CASOS = {"B1", "B2", "B3", "B4", "B5"}
TIPOS = {"normativo", "sin contenido normativo"}


def verificar_lote(lote, salida):
    errores = []
    ids = [u["id"] for u in json.loads(lote.read_text(encoding="utf-8"))]
    if not salida.exists():
        return [f"falta {salida.name}"]
    filas = json.loads(salida.read_text(encoding="utf-8"))
    vistos = {}
    for f in filas:
        vistos[f.get("id")] = vistos.get(f.get("id"), 0) + 1
    for i in ids:
        if vistos.get(i, 0) != 1:
            errores.append(f"{i}: aparece {vistos.get(i, 0)} veces")
    for i in set(vistos) - set(ids):
        errores.append(f"{i}: id ajeno al lote")
    for f in filas:
        i, t = f.get("id"), f.get("tipo")
        if t not in TIPOS:
            errores.append(f"{i}: tipo inválido {t!r}")
            continue
        if not str(f.get("motivo", "")).strip() and t == "sin contenido normativo":
            errores.append(f"{i}: sin contenido normativo sin motivo")
        if t != "normativo":
            continue
        aplica = f.get("aplica", [])
        fuera = f.get("fuera", {})
        if not isinstance(aplica, list) or not isinstance(fuera, dict):
            errores.append(f"{i}: aplica/fuera con forma inválida")
            continue
        if set(aplica) & set(fuera):
            errores.append(f"{i}: caso en aplica y en fuera {set(aplica) & set(fuera)}")
        if set(aplica) | set(fuera) != CASOS or len(aplica) != len(set(aplica)):
            errores.append(f"{i}: casos cubiertos {sorted(set(aplica) | set(fuera))}")
        for c, m in fuera.items():
            if not str(m).strip():
                errores.append(f"{i}: {c} fuera sin motivo")
        if aplica and not str(f.get("efecto", "")).strip():
            errores.append(f"{i}: aplica sin efecto")
    return errores


def main():
    carpeta = Path(sys.argv[1])
    solo = sys.argv[2] if len(sys.argv) > 2 else None
    total_err, total = 0, 0
    for lote in sorted((AQUI / "lotes").glob("lote_*.json")):
        if solo and lote.stem != solo:
            continue
        err = verificar_lote(lote, carpeta / lote.name)
        n = len(json.loads(lote.read_text(encoding="utf-8")))
        total += n
        total_err += len(err)
        print(f"{lote.stem}: {n} textos · {'OK' if not err else f'{len(err)} ERRORES'}")
        for e in err[:15]:
            print("   ", e)
    print(f"TOTAL {total} textos · errores {total_err}")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
