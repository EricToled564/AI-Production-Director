"""Exporta la tabla de catalogación: columna A = registro completo; columnas siguientes = etiquetas del
catálogo (vacías); al final, la ubicación exacta en la fuente para corregir a mano.

Lee las tablas registros / registros_fuente / registros_exclusion que escribe extraer_registros.py.
Uso: python3 tools/exportar_catalogo.py --xlsx salida.xlsx [--db data/rules.sqlite]
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

APD = Path(__file__).resolve().parents[1]

TAXONOMIA = APD.parent / ".claude/rules/TAXONOMIA.md"


def leer_taxonomia(ruta=TAXONOMIA):
    """Facetas aprobadas (decisión 10): [("N. Nombre", "valor · valor · ...")], leídas de TAXONOMIA.md."""
    import re
    t = ruta.read_text(encoding="utf-8")
    out = []
    for b in re.split(r"\n### ", t)[1:]:
        b = b.split("\n## ")[0]
        cab = b.split("\n", 1)[0]
        nombre = cab.split(" — ")[0].split(" (")[0].strip()
        filas = [l for l in b.split("\n") if l.startswith("|") and not l.startswith("|---")]
        hdr = [c.strip() for c in filas[0].strip("|").split("|")] if filas else []
        vals = []
        for f in filas[1:]:
            cel = [c.strip() for c in f.strip("|").split("|")]
            if hdr[:2] == ["Rama", "Valores"] or hdr[0] == "Etapa":
                vals += [x.strip() for x in cel[1].split("·")]
            elif hdr[0] == "Rama":
                vals.append(cel[1])
            else:
                vals.append(cel[0])
        out.append((nombre, " · ".join(dict.fromkeys(vals))))
    return out


CATALOGO = leer_taxonomia()

UBICACION = ["Documento", "Página / sección", "Párrafo nº (de N)", "Líneas", "ID registro"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(APD / "data/rules.sqlite"))
    ap.add_argument("--xlsx", required=True)
    ap.add_argument("--sin-duplicados", action="store_true",
                    help="una fila por regla: cada grupo de duplicados sale como su registro fusionado y verificado")
    a = ap.parse_args()
    con = sqlite3.connect(a.db)
    regs = con.execute("select id, orden, texto from registros order by orden").fetchall()
    fuentes: dict[str, list] = {}
    for rid, arch, li, lf, sec, par, tot in con.execute(
            "select registro_id, archivo, linea_ini, linea_fin, seccion, parrafo, parrafos_en_documento from registros_fuente"):
        fuentes.setdefault(rid, []).append((arch, li, lf, sec, par, tot))
    fusiones = []
    if a.sin_duplicados:
        fusiones = con.execute("select grupo, texto, miembros, verificado from registros_fusion order by grupo").fetchall()
        malos = [g for g, _, _, v in fusiones if v != 1]
        if malos:
            raise SystemExit(f"{len(malos)} fusiones sin verificar: {malos[:5]}")
        orden = {rid: o for rid, o, _ in regs}
        texto_de = {rid: t for rid, _, t in regs}
        absorbidos = set()
        nuevas = []
        for g, t, miembros, _ in fusiones:
            ids = json.loads(miembros)
            absorbidos.update(ids)
            fuentes[g] = [f for i in ids for f in fuentes.get(i, [])]
            nuevas.append((g, min(orden[i] for i in ids), t))
        regs = sorted([r for r in regs if r[0] not in absorbidos] + nuevas, key=lambda r: r[1])

    wb = Workbook()
    ws = wb.active
    ws.title = "Registros"
    cab = ["Registro (regla o punto de sintaxis completo)"] + [c for c, _ in CATALOGO] + UBICACION
    ws.append(cab)
    for rid, orden, texto in regs:
        fs = fuentes.get(rid, [])
        doc = " | ".join(f[0] for f in fs)
        sec = " | ".join(f[3] or "" for f in fs)
        par = " | ".join(f"{f[4]} de {f[5]}" for f in fs)
        lin = " | ".join((f"{f[1]}–{f[2]}" if f[1] and f[2] != f[1] else str(f[1])) if f[1] else "objeto JSON/Python" for f in fs)
        ws.append([texto] + [""] * len(CATALOGO) + [doc, sec, par, lin, rid])
    bold = Font(bold=True)
    fill_cat = PatternFill("solid", fgColor="FFF2CC")
    fill_ubi = PatternFill("solid", fgColor="DDEBF7")
    for col in range(1, len(cab) + 1):
        c = ws.cell(row=1, column=col)
        c.font = bold
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if 2 <= col <= 1 + len(CATALOGO):
            c.fill = fill_cat
        elif col > 1 + len(CATALOGO):
            c.fill = fill_ubi
    ws.column_dimensions["A"].width = 110
    for col in range(2, 2 + len(CATALOGO)):
        ws.column_dimensions[get_column_letter(col)].width = 16
    for i, w in enumerate([48, 48, 14, 12, 14]):
        ws.column_dimensions[get_column_letter(2 + len(CATALOGO) + i)].width = w
    for row in ws.iter_rows(min_row=2, max_col=1):
        row[0].alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(cab))}{ws.max_row}"

    if fusiones:
        wd = wb.create_sheet("Fusiones")
        wd.append(["Grupo", "Registro fusionado", "ID original", "Texto original", "Documento", "Página / sección", "Líneas"])
        for g, t, miembros, _ in fusiones:
            for i in json.loads(miembros):
                for f in fuentes.get(i, [])[:1] or [("", "", "", "", "", "")]:
                    wd.append([g, t, i, texto_de[i], " | ".join(x[0] for x in fuentes.get(i, [])),
                               " | ".join(x[3] or "" for x in fuentes.get(i, [])), f"{f[1]}–{f[2]}" if f[1] else ""])
        for col, w in zip("ABCDEFG", (12, 70, 14, 70, 40, 40, 12)):
            wd.column_dimensions[col].width = w
        for row in wd.iter_rows(min_row=2):
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical="top")
        wd.freeze_panes = "A2"
        wd.auto_filter.ref = f"A1:G{wd.max_row}"

    wc = wb.create_sheet("Taxonomía")
    wc.append(["Faceta (TAXONOMIA.md, decisión 10)", "Valores aprobados"])
    for c, v in CATALOGO:
        wc.append([c, v])
    wc.column_dimensions["A"].width = 30
    wc.column_dimensions["B"].width = 140
    for r in wc.iter_rows(min_row=1):
        for c in r:
            c.alignment = Alignment(wrap_text=True, vertical="top")
        r[0].font = bold

    we = wb.create_sheet("Líneas excluidas")
    we.append(["Documento", "Línea", "Texto de la línea", "Motivo de exclusión"])
    for arch, ln, tx, mot in con.execute("select archivo, linea, texto, motivo from registros_exclusion order by archivo, linea"):
        we.append([arch, ln, tx, mot])
    for col, w in zip("ABCD", (60, 8, 90, 70)):
        we.column_dimensions[col].width = w
    we.freeze_panes = "A2"
    we.auto_filter.ref = f"A1:D{we.max_row}"

    wf = wb.create_sheet("Fuentes")
    wf.append(["Documento", "Registros", "Párrafos extraídos", "Líneas excluidas con motivo"])
    por_doc = {}
    for rid, fs in fuentes.items():
        for f in fs:
            d = por_doc.setdefault(f[0], {"regs": set(), "tot": f[5]})
            d["regs"].add(rid)
    exc = dict(con.execute("select archivo, count(*) from registros_exclusion group by archivo").fetchall())
    for doc in sorted(set(por_doc) | set(exc)):
        d = por_doc.get(doc, {"regs": set(), "tot": 0})
        wf.append([doc, len(d["regs"]), d["tot"], exc.get(doc, 0)])
    wf.append([])
    wf.append(["Fuentes NO incluidas", "Motivo"])
    import importlib.util
    spec = importlib.util.spec_from_file_location("ext", APD / "tools/extraer_registros.py")
    ext = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ext)
    for f, m in ext.EXCLUIDAS:
        wf.append([f, m])
    wf.column_dimensions["A"].width = 80
    wf.column_dimensions["B"].width = 90
    wb.save(a.xlsx)
    print(f"{len(regs)} registros · {len(fusiones)} fusiones · {len(CATALOGO)} columnas de catálogo · {a.xlsx}")


if __name__ == "__main__":
    main()
