"""indice_consulta.py: escribe ../CONSULTA.md, el índice que el agente consulta antes de preguntar a Eric o de afirmar
que algo no existe o no está decidido.

    python3 -I indice_consulta.py      (desde 6_mapa/herramientas)

El índice no repite el contenido de los archivos: dice qué hay y en qué línea. Todo sale mecánicamente de los archivos:
  1. cada archivo del repo, con sus secciones (Markdown), claves (JSON), tablas (SQLite) o descripción (Python);
  2. cada decisión e instrucción de Eric, con archivo y línea;
  3. cada pendiente;
  4. cada documento del corpus: textos, ids, utilidad y copias idénticas.
Se regenera cada vez que cambia una decisión o un archivo del repo.
"""
import ast
import collections
import json
import re
import sqlite3
import subprocess
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MAPA = AQUI.parent
REPO = MAPA.parent
DB = REPO / "2_corpus/BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite"


def corta(s, n=150):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


GUIA = """# Índice del repo (memoria del agente)

Se consulta **antes** de preguntarle algo a Eric y **antes** de decir que algo falta, no existe o no está decidido.
Dice qué hay y en qué línea; lo que vale es siempre el archivo señalado. Se regenera con
`6_mapa/herramientas/indice_consulta.py`.

| Duda | Dónde mirar |
|---|---|
| Instrucciones de trabajo | `CLAUDE.md`; `.claude/rules/DECISIONES.md` (§2 de este índice) |
| ¿Eric ya decidió esto? | §2: cada decisión con archivo y línea |
| Qué falta y quién lo resuelve | `PENDIENTES.md` (§3) |
| Texto original de una regla | `2_corpus/…sqlite`, tabla `textos`, por `id` (INV-xxxxxx). Secciones de un documento: `SELECT DISTINCT encabezado FROM textos WHERE archivo=?` |
| Qué documentos tiene el corpus | §4 |
| Taxonomía, templates, casos, validadores | §1, carpetas `3_taxonomia/` y `4_diseno/` |
| Algo borrado del repo | `git log --diff-filter=D --name-only`; se recupera desde el commit anterior al borrado |
"""


def secciones_md(f):
    out = []
    for i, l in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        m = re.match(r"^(#{1,4}) (.+)", l)
        if m:
            out.append(f"L{i} {corta(m.group(2), 70)}")
    return out


def describe(a):
    f = REPO / a
    suf = f.suffix.lower()
    try:
        if suf == ".md":
            s = secciones_md(f)
            n = f.read_text(encoding="utf-8").count("\n")
            return f"{n} líneas" + (": " + " · ".join(s) if s else "")
        if suf == ".json":
            d = json.loads(f.read_text(encoding="utf-8"))
            if isinstance(d, dict):
                return f"{len(d)} claves: " + ", ".join(corta(str(k), 40) for k in list(d)[:12]) + (" …" if len(d) > 12 else "")
            return f"lista de {len(d)} elementos"
        if suf == ".jsonl":
            return f"{sum(1 for _ in f.open(encoding='utf-8'))} líneas JSON"
        if suf == ".csv":
            lineas = f.read_text(encoding="utf-8").splitlines()
            return f"{len(lineas) - 1} filas; columnas: {corta(lineas[0], 100)}"
        if suf == ".py":
            doc = ast.get_docstring(ast.parse(f.read_text(encoding="utf-8"))) or ""
            return corta(doc.splitlines()[0], 120) if doc else "sin docstring"
        if suf == ".sqlite":
            c = sqlite3.connect(f)
            t = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
            return "tablas: " + ", ".join(f"{x} ({c.execute(f'SELECT COUNT(*) FROM {x}').fetchone()[0]} filas)" for x in t)
        if suf == ".zip":
            z = zipfile.ZipFile(f)
            arch = [i.filename for i in z.infolist() if not i.is_dir()]
            top = collections.Counter(x.split("/")[1] if x.count("/") > 1 else "(raíz)" for x in arch)
            return (f"{len(arch)} archivos: " + ", ".join(f"{k} {v}" for k, v in top.most_common()) +
                    ". Los de `skills/` son el corpus (§4); los demás no están en el corpus (PENDIENTES P-18). "
                    "Guías: `START_HERE.md`, `INDEX.md`, `repo/.claude/hooks/README.md`")
    except (ValueError, SyntaxError, sqlite3.Error) as e:
        return f"no se pudo leer ({type(e).__name__})"
    return f"{f.stat().st_size:,} bytes"


def archivos():
    lista = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True, text=True, check=True).stdout.split()
    o = [f"\n## 1. Archivos del repo ({len(lista)})\n"]
    carpeta = None
    for a in lista:
        c = str(Path(a).parent)
        if c != carpeta:
            o.append(f"\n**`{c}/`**\n")
            carpeta = c
        o.append(f"- `{Path(a).name}`: {describe(a)}")
    return o


def decisiones():
    o = ["\n## 2. Decisiones e instrucciones de Eric (archivo y línea)\n"]
    for f in [REPO / "CLAUDE.md", REPO / ".claude/rules/DECISIONES.md"] + sorted((REPO / "5_decisiones").glob("*.md")):
        lineas = f.read_text(encoding="utf-8").splitlines()
        o.append(f"\n**`{f.relative_to(REPO)}`**\n")
        for i, l in enumerate(lineas, 1):
            if re.match(r"^#{2,4} ", l):
                o.append(f"- L{i} **{corta(l.lstrip('# '), 90)}**")
            elif re.match(r"^\s{0,3}\d+\. ", l) or re.match(r"^\| \d+ \|", l) or re.match(r"^- \*\*", l):
                o.append(f"- L{i} {corta(l)}")
    for f in sorted((REPO / "5_decisiones/directivas_20261021").glob("*directiv*.json")):
        o.append(f"\n**`{f.relative_to(REPO)}`**\n")
        for d in json.loads(f.read_text(encoding="utf-8")):
            o.append(f"- `{d['constraint_id']}`: «{corta(d['literal'])}»")
    return o


def pendientes():
    o = ["\n## 3. Pendientes (`PENDIENTES.md`)\n"]
    for i, l in enumerate((REPO / "PENDIENTES.md").read_text(encoding="utf-8").splitlines(), 1):
        m = re.match(r"^\| (P-\d+) \| (.+?) \| (.+?) \| (.+?) \|", l)
        if m:
            o.append(f"- L{i} **{m.group(1)}** ({corta(m.group(3), 40)}; {corta(m.group(4), 50)}): {corta(m.group(2), 120)}")
    return o


def corpus():
    util = json.loads((AQUI / "utilidad_corpus.json").read_text(encoding="utf-8"))
    c = sqlite3.connect(DB)
    filas = c.execute("SELECT archivo, sha256_archivo, COUNT(*), MIN(id), MAX(id) FROM textos "
                      "GROUP BY archivo ORDER BY archivo").fetchall()
    por_sha = collections.defaultdict(list)
    for f in filas:
        por_sha[f[1]].append(f[0])
    o = [f"\n## 4. Corpus: {len(filas)} archivos, {len(por_sha)} contenidos distintos\n",
         "Utilidad: ALTA, dice qué va o no va en un prompt; MEDIA, regula el proceso; NULA, ninguna de las dos.\n",
         "| Documento | Textos | Ids | Utilidad | Copias idénticas |", "|---|---:|---|---|---|"]
    for arch, sha, n, a, b in filas:
        grupo = por_sha[sha]
        if arch != grupo[0]:
            continue
        o.append(f"| `{arch}` | {n} | {a}–{b} | {util.get(arch, '—')} | "
                 + (", ".join(f"`{x}`" for x in grupo[1:]) or "—") + " |")
    return o


texto = "\n".join([GUIA] + archivos() + decisiones() + pendientes() + corpus()) + "\n"
(MAPA / "CONSULTA.md").write_text(texto, encoding="utf-8")
print(f"CONSULTA.md: {texto.count(chr(10))} líneas, {len(texto):,} caracteres")
