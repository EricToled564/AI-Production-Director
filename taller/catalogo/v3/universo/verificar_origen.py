"""Verifica, contra los documentos originales, el archivo, las líneas y el encabezado de cada uno de los 13,005 textos.

Uso: python3 -I verificar_origen.py <carpeta_extraida>
<carpeta_extraida> tiene descomprimidos apd/originales/*.zip y copiados los dos flujo-*.html (los originales viven en
apd/originales/, SHA256SUMS). Cada archivo del corpus se localiza por su sha256_archivo, no por su nombre.

Comprobaciones por texto:
  A. el sha256 del archivo original coincide con sha256_archivo;
  B. el texto está literalmente en el original en las líneas linea_inicial..linea_final (HTML: en el texto visible,
     ver texto_html);
  C. sha256 del texto coincide con sha256_unidad;
  D. en Markdown (.md y .md.tpl), el encabezado guardado es igual a la ruta de títulos # reconstruida desde el original;
  E. en HTML, que no trae encabezado ni línea del fuente, los textos ordenados por linea_inicial aparecen en ese mismo
     orden en el texto visible del original (de ese orden sale la sección en secciones.py).
Los fallos D se guardan con el encabezado reconstruido; secciones.py usa ese en lugar del guardado.
Sale con código 1 si falla A, B, C o E; D es un error conocido del encabezado de la base y se corrige aguas abajo. Escribe verificacion_origen.json junto a este script.
"""
import hashlib, html, json, re, sqlite3, sys
from html.parser import HTMLParser
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parents[1] / "corpus" / "BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite"
SHA_BASE = "c991437028d9d731bf46e516efa315f08d9da71bd596495c119fa41d30f6c8d9"


class Visible(HTMLParser):
    """Nodos de texto visible de un HTML, sin style ni script, y las filas de tabla celda por celda."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.partes, self.saltar, self.filas, self.fila, self.celda = [], 0, [], None, None
    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script"):
            self.saltar += 1
        elif tag == "tr":
            self.fila = []
        elif tag in ("td", "th") and self.fila is not None:
            self.celda = []
    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self.saltar -= 1
        elif tag in ("td", "th") and self.celda is not None:
            self.fila.append(norm("".join(self.celda))); self.celda = None
        elif tag == "tr" and self.fila is not None:
            self.filas.append(tuple(self.fila)); self.fila = None
    def handle_data(self, d):
        if not self.saltar:
            self.partes.append(d)
            if self.celda is not None:
                self.celda.append(d)


def norm(s):
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def texto_html(texto, visible):
    """El texto está en el HTML: igual a un nodo de texto, contenido en el texto visible (etiquetas en línea), o, si es
    una fila de tabla '| a | b |', igual celda por celda a una fila <tr> del original."""
    nodos, filas, espacio, pegado = visible
    t = norm(texto)
    if t in nodos or t in espacio or t in pegado:
        return True
    if t.startswith("|"):
        celdas = tuple(norm(c) for c in t.strip().strip("|").split(" | "))
        return celdas in filas
    return False


def rutas_md(lineas):
    """Ruta de títulos vigente en cada línea (1-indexada), ignorando frontmatter y bloques de código."""
    ruta, pila, cerco, fm = {}, [], None, False
    for i, l in enumerate(lineas, 1):
        if i == 1 and l.strip() == "---":
            fm = True
        elif fm:
            if l.strip() == "---":
                fm = False
        else:
            m = re.match(r"^\s{0,3}(`{3,}|~{3,})", l)
            if m:
                if cerco is None:
                    cerco = m.group(1)[0]
                elif m.group(1)[0] == cerco:
                    cerco = None
            elif cerco is None:
                h = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", l)
                if h:
                    n = len(h.group(1))
                    pila = [p for p in pila if p[0] < n] + [(n, h.group(2).strip())]
        ruta[i] = " › ".join(t for _, t in pila)
    return ruta


def main():
    if hashlib.sha256(BASE.read_bytes()).hexdigest() != SHA_BASE:
        raise SystemExit("la base no coincide con su sha256 autorizado")
    raiz = Path(sys.argv[1])
    por_sha = {}
    for p in raiz.rglob("*"):
        if p.is_file():
            por_sha.setdefault(hashlib.sha256(p.read_bytes()).hexdigest(), p)
    db = sqlite3.connect(BASE)
    filas = db.execute("select id, archivo, sha256_archivo, linea_inicial, linea_final, tipo_unidad, encabezado, texto,"
                       " sha256_unidad from textos").fetchall()
    cache, fallos, cuentas = {}, [], {"A": 0, "B": 0, "C": 0, "D": 0, "D_aplica": 0}
    for id_, archivo, sha_a, li, lf, tipo, enc, texto, sha_u in filas:
        p = por_sha.get(sha_a)
        if p is None:
            fallos.append({"id": id_, "prueba": "A", "archivo": archivo}); continue
        cuentas["A"] += 1
        if sha_a not in cache:
            crudo = p.read_bytes().decode("utf-8")
            lineas = crudo.split("\n")
            visible = None
            if archivo.endswith(".html"):
                v = Visible(); v.feed(crudo)
                trozos = [norm(x) for x in v.partes]
                trozos = [x for x in trozos if x]
                visible = (set(trozos), set(v.filas), norm(" ".join(trozos)), norm("".join(v.partes)))
            cache[sha_a] = (lineas, visible, rutas_md(lineas) if archivo.endswith((".md", ".md.tpl")) else None)
        lineas, visible, rutas = cache[sha_a]
        li, lf = int(li), int(lf)
        if visible is not None:
            ok = texto_html(texto, visible)
        else:
            tramo = "\n".join(lineas[li - 1:lf])
            ok = tramo == texto or tramo.strip() == texto.strip()
        if ok:
            cuentas["B"] += 1
        else:
            fallos.append({"id": id_, "prueba": "B", "archivo": archivo, "lineas": [li, lf]})
        calc = hashlib.sha256(texto.encode("utf-8")).hexdigest()
        if calc == sha_u:
            cuentas["C"] += 1
        else:
            fallos.append({"id": id_, "prueba": "C", "archivo": archivo})
        if rutas is not None:
            cuentas["D_aplica"] += 1
            if (enc or "") == rutas[li]:
                cuentas["D"] += 1
            else:
                fallos.append({"id": id_, "prueba": "D", "archivo": archivo, "linea": li,
                               "guardado": enc, "reconstruido": rutas[li]})
    cuentas["E_archivos_html"], cuentas["E"] = 0, 0
    por_archivo = {}
    for id_, archivo, sha_a, li, *_ in filas:
        if archivo.endswith(".html"):
            por_archivo.setdefault((archivo, sha_a), []).append((int(li), id_))
    textos = {f[0]: f[7] for f in filas}
    for (archivo, sha_a), lista in por_archivo.items():
        cuentas["E_archivos_html"] += 1
        v = Visible(); v.feed(por_sha[sha_a].read_bytes().decode("utf-8"))
        flujo, pos = re.sub(r"\s+", "", "".join(v.partes)), 0
        for li, id_ in sorted(lista):
            t = html.unescape(textos[id_]).strip()
            clave = re.sub(r"\s+", "", t.strip("|").split(" | ")[0] if t.startswith("|") else t)
            k = flujo.find(clave, pos)
            if k < 0:
                fallos.append({"id": id_, "prueba": "E", "archivo": archivo, "linea": li})
            else:
                pos = k + 1
        if not any(f["prueba"] == "E" and f["archivo"] == archivo for f in fallos):
            cuentas["E"] += 1
    salida = {"textos": len(filas), "pasan": cuentas, "fallos": fallos}
    (AQUI / "verificacion_origen.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"textos": len(filas), "pasan": cuentas, "fallos": len(fallos)}, ensure_ascii=False))
    from collections import Counter
    print(Counter(f["prueba"] for f in fallos))
    sys.exit(1 if [f for f in fallos if f["prueba"] != "D"] else 0)


if __name__ == "__main__":
    main()
