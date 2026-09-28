"""Extrae TODOS los registros a catalogar (reglas enteras + puntos de sintaxis) de las fuentes.

Unidad = bloque completo de la fuente, nunca una línea suelta:
  párrafo · viñeta con sus sub-viñetas y continuaciones · fila de tabla con sus encabezados ·
  bloque de código entero (plantilla/sintaxis) · cita · descripción del frontmatter ·
  clave YAML · generador de _capabilities.json · propiedad de esquema JSON · política/aprendizaje.
Cada unidad lleva delante la ruta de encabezados de su sección y, si la precede una frase
introductoria ("Rules:", "Fix."), esa frase: así la regla se lee entera sin abrir el archivo.

Cobertura (sale con código 1 si falla cualquiera):
  1. cada línea no vacía de cada fuente incluida cae en una unidad o en una exclusión con motivo;
  2. cada una de las reglas de rules.sqlite (tabla reglas) cae dentro de una unidad;
  3. cada punto de sintaxis de data/sintaxis_fuente.json cae dentro de una unidad.

Uso: python3 tools/extraer_registros.py [--db data/rules.sqlite] [--xlsx salida.xlsx]
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sqlite3
import sys
from pathlib import Path

APD = Path(__file__).resolve().parents[1]
REPO = APD.parent
PKG = APD / ".cache/pkg/AI_Production_Director_v3.4.0_COMPLETE"
SKILLS = PKG / "skills"
PKG_REPO = PKG / "repo"

RX_HEAD = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
RX_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
RX_FENCE = re.compile(r"^\s*(```|~~~)")
RX_HR = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
RX_TSEP = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
RX_FOOTER = re.compile(r"^\s*\*?\s*Author:\s*Serge Shima", re.I)
TOC = {"contents", "table of contents", "содержание", "índice", "indice"}


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip().lower()


def palabras(t: str) -> int:
    return len(re.findall(r"\S+", t))


class Doc:
    """Unidades y exclusiones de un archivo."""

    def __init__(self, ruta: str, lineas: list[str]):
        self.ruta = ruta
        self.lineas = lineas
        self.unidades: list[dict] = []
        self.excl: dict[int, str] = {}  # línea 1-based -> motivo

    def unidad(self, tipo, ini, fin, seccion, texto, lead=None):
        cuerpo = texto.strip("\n")
        if lead:
            cuerpo = f"{lead.strip()}\n{cuerpo}"
        pref = f"[{seccion}] " if seccion else ""
        self.unidades.append({"tipo": tipo, "ini": ini, "fin": fin, "seccion": seccion,
                              "texto": pref + cuerpo, "contenido": cuerpo})

    def excluir(self, ini, fin, motivo):
        for n in range(ini, fin + 1):
            if self.lineas[n - 1].strip():
                self.excl.setdefault(n, motivo)


# ---------------------------------------------------------------- markdown

def split_celdas(linea: str) -> list[str]:
    s = linea.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    celdas, cur, tick = [], "", False
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "|"
            i += 2
            continue
        if ch == "`":
            tick = not tick
        if ch == "|" and not tick:
            celdas.append(cur.strip())
            cur = ""
        else:
            cur += ch
        i += 1
    celdas.append(cur.strip())
    return celdas


def parse_md(doc: Doc, solo_secciones: re.Pattern | None = None):
    L = doc.lineas
    n = len(L)
    i = 0
    pila: list[tuple[int, str]] = []
    heads: list[dict] = []  # para detectar encabezados sin cuerpo
    bloques: list[dict] = []  # en orden, antes de resolver frases introductorias

    def seccion():
        return " › ".join(t for _, t in pila)

    # frontmatter
    if n and L[0].strip() == "---":
        j = 1
        while j < n and L[j].strip() != "---":
            j += 1
        fm_fin = j + 1  # línea del cierre, 1-based
        k = 1
        while k < j:
            m = re.match(r"^(\w[\w-]*):\s*(.*)$", L[k])
            if m and m.group(1) == "description":
                ini = k + 1
                partes = [m.group(2)] if m.group(2) not in (">", "|", ">-", "|-") else []
                k += 1
                while k < j and (L[k].startswith((" ", "\t")) or not L[k].strip()):
                    partes.append(L[k].strip())
                    k += 1
                txt = "\n".join(p for p in partes).strip()
                bloques.append({"tipo": "descripcion", "ini": ini, "fin": k, "sec": "frontmatter › description",
                                "txt": txt})
                continue
            k += 1
        doc.excluir(1, fm_fin, "frontmatter: metadatos (nombre, licencia, versión); la descripción se extrae aparte")
        # la descripción no se excluye
        for b in bloques:
            for x in range(b["ini"], b["fin"] + 1):
                doc.excl.pop(x, None)
        i = fm_fin

    while i < n:
        raw = L[i]
        s = raw.strip()
        ln = i + 1
        if not s:
            i += 1
            continue
        # comentario HTML (una o varias líneas)
        if s.startswith("<!--"):
            j = i
            while j < n and "-->" not in L[j]:
                j += 1
            doc.excluir(ln, j + 1, "comentario HTML (metadato de autoría/snapshot, no normativo)")
            i = j + 1
            continue
        if RX_FOOTER.match(s):
            doc.excluir(ln, ln, "pie de atribución de licencia CC BY 4.0")
            i += 1
            continue
        m = RX_HEAD.match(raw)
        if m and not raw.startswith((" ", "\t")):
            nivel = len(m.group(1))
            while pila and pila[-1][0] >= nivel:
                pila.pop()
            pila.append((nivel, m.group(2).strip()))
            heads.append({"ln": ln, "nivel": nivel, "sec": seccion(), "n_bloques": len(bloques)})
            doc.excluir(ln, ln, "encabezado: su texto va dentro de cada registro de la sección")
            i += 1
            continue
        if RX_HR.match(s):
            doc.excluir(ln, ln, "separador horizontal")
            i += 1
            continue
        if RX_FENCE.match(raw):
            marca = RX_FENCE.match(raw).group(1)
            j = i + 1
            while j < n and not L[j].strip().startswith(marca):
                j += 1
            cuerpo = "\n".join(L[i + 1:j])
            bloques.append({"tipo": "codigo", "ini": ln, "fin": min(j + 1, n), "sec": seccion(), "txt": cuerpo})
            i = j + 1
            continue
        if s.startswith("|") and i + 1 < n and RX_TSEP.match(L[i + 1]):
            cab = split_celdas(L[i])
            j = i + 2
            filas = []
            while j < n and L[j].strip().startswith("|"):
                filas.append((j + 1, split_celdas(L[j])))
                j += 1
            bloques.append({"tipo": "tabla", "ini": ln, "fin": j, "sec": seccion(), "cab": cab, "filas": filas})
            i = j
            continue
        if s.startswith(">"):
            j = i
            while j < n and L[j].strip().startswith(">"):
                j += 1
            txt = "\n".join(re.sub(r"^\s*>\s?", "", x) for x in L[i:j])
            bloques.append({"tipo": "cita", "ini": ln, "fin": j, "sec": seccion(), "txt": txt})
            i = j
            continue
        mi = RX_ITEM.match(raw)
        if mi and len(mi.group(1)) <= 3:
            base = len(mi.group(1))
            items = []
            j = i
            while j < n:
                mj = RX_ITEM.match(L[j])
                if mj and len(mj.group(1)) == base:
                    items.append({"ini": j + 1, "lineas": [L[j]]})
                    j += 1
                    continue
                t = L[j]
                if not t.strip():
                    # ¿sigue la lista después del hueco?
                    k = j
                    while k < n and not L[k].strip():
                        k += 1
                    if k < n and ((RX_ITEM.match(L[k]) and len(RX_ITEM.match(L[k]).group(1)) >= base)
                                  or (len(L[k]) - len(L[k].lstrip()) > base and not RX_HEAD.match(L[k]))):
                        items[-1]["lineas"].extend(L[j:k])
                        j = k
                        continue
                    break
                ind = len(t) - len(t.lstrip())
                if ind > base or (not RX_HEAD.match(t) and not t.strip().startswith(("|", ">")) and not RX_FENCE.match(t)
                                  and not RX_ITEM.match(t)):
                    # continuación (sangrada, sub-viñeta o perezosa); los bloques de código sangrados van enteros
                    if RX_FENCE.match(t):
                        marca = RX_FENCE.match(t).group(1)
                        k = j + 1
                        while k < n and not L[k].strip().startswith(marca):
                            k += 1
                        items[-1]["lineas"].extend(L[j:k + 1])
                        j = k + 1
                        continue
                    items[-1]["lineas"].append(t)
                    j += 1
                    continue
                break
            for it in items:
                it["fin"] = it["ini"] + len(it["lineas"]) - 1
                it["txt"] = "\n".join(x.rstrip() for x in it["lineas"]).strip()
                it["sub"] = any(RX_ITEM.match(x) and len(RX_ITEM.match(x).group(1)) > base for x in it["lineas"][1:])
            bloques.append({"tipo": "lista", "ini": ln, "fin": j, "sec": seccion(), "items": items})
            i = j
            continue
        # párrafo
        j = i
        while j < n and L[j].strip() and not RX_HEAD.match(L[j]) and not RX_FENCE.match(L[j]) \
                and not (L[j].strip().startswith("|") and j + 1 < n and RX_TSEP.match(L[j + 1])) \
                and not (RX_ITEM.match(L[j]) and len(RX_ITEM.match(L[j]).group(1)) <= 3 and j > i) \
                and not L[j].strip().startswith("<!--") and not RX_HR.match(L[j].strip()):
            j += 1
        if j == i:
            j = i + 1
        bloques.append({"tipo": "parrafo", "ini": ln, "fin": j, "sec": seccion(), "txt": "\n".join(L[i:j]).strip()})
        i = j

    # fusionar párrafos-etiqueta consecutivos de la misma sección ('**Beat:** hook', '**Subject:** ...')
    RX_ETQ = re.compile(r"^\*\*[^*]{1,40}:\*\*|^\*\*[^*]{1,40}\*\*:")
    fusion = []
    for b in bloques:
        if fusion and b["tipo"] == "parrafo" and fusion[-1]["tipo"] == "parrafo" and b["sec"] == fusion[-1]["sec"] \
                and RX_ETQ.match(b["txt"]) and RX_ETQ.match(fusion[-1]["txt"].split("\n")[-1] if fusion[-1].get("etq") else fusion[-1]["txt"]):
            fusion[-1]["txt"] += "\n" + b["txt"]
            fusion[-1]["fin"] = b["fin"]
            fusion[-1]["etq"] = True
            continue
        fusion.append(dict(b))
    bloques = fusion
    # frase introductoria que termina en ':' seguida de párrafo o cita: se unen
    unidos = []
    for b in bloques:
        if unidos and b["tipo"] in ("parrafo", "cita") and unidos[-1]["tipo"] == "parrafo" \
                and unidos[-1]["sec"] == b["sec"] and unidos[-1]["txt"].rstrip().rstrip("*_").rstrip().endswith(":"):
            unidos[-1]["txt"] += "\n" + b["txt"]
            unidos[-1]["fin"] = b["fin"]
            continue
        unidos.append(b)
    bloques = unidos
    # resolver frases introductorias y emitir
    k = 0
    while k < len(bloques):
        b = bloques[k]
        lead = None
        if b["tipo"] == "parrafo" and k + 1 < len(bloques):
            sig = bloques[k + 1]
            t = b["txt"]
            if sig["tipo"] in ("lista", "tabla", "codigo") and sig["sec"] == b["sec"] \
                    and (t.rstrip().rstrip("*_").rstrip().endswith(":") or palabras(t) <= 8):
                lead = t
                n0 = len(doc.unidades)
                emitir(doc, sig, lead)
                for u in doc.unidades[n0:]:
                    u["ini"] = b["ini"]
                k += 2
                continue
        if b["tipo"] == "lista" and b["sec"].split(" › ")[-1].strip().lower() in TOC:
            doc.excluir(b["ini"], b["fin"], "índice del archivo (lista de secciones)")
            k += 1
            continue
        emitir(doc, b, None)
        k += 1

    # encabezados sin ningún cuerpo (sección vacía que no es padre de otra)
    for idx, h in enumerate(heads):
        sig_ln = heads[idx + 1]["ln"] if idx + 1 < len(heads) else n + 1
        hijo = idx + 1 < len(heads) and heads[idx + 1]["nivel"] > h["nivel"]
        tiene = any(L[x - 1].strip() for x in range(h["ln"] + 1, sig_ln))
        if not tiene and not hijo:
            doc.excl.pop(h["ln"], None)
            doc.unidad("encabezado", h["ln"], h["ln"], h["sec"], L[h["ln"] - 1].lstrip("#").strip())

    if solo_secciones is not None:
        fuera = [u for u in doc.unidades if not solo_secciones.search(u["seccion"])]
        doc.unidades = [u for u in doc.unidades if solo_secciones.search(u["seccion"])]
        for u in fuera:
            doc.excluir(u["ini"], u["fin"], "research: sólo se extraen las reglas candidatas (hallazgos nuevos); "
                                            "el resto es bitácora, citas y veredictos")


def emitir(doc: Doc, b: dict, lead: str | None):
    t = b["tipo"]
    if t == "parrafo" or t == "cita" or t == "descripcion":
        doc.unidad(t, b["ini"], b["fin"], b["sec"], b["txt"], lead)
    elif t == "codigo":
        doc.unidad("codigo", b["ini"], b["fin"], b["sec"], b["txt"], lead)
        doc.excluir(b["ini"], b["ini"], "marca de apertura de bloque de código")
        doc.excluir(b["fin"], b["fin"], "marca de cierre de bloque de código")
        # las marcas están dentro del intervalo de la unidad; se cuentan como cubiertas por ella
        doc.excl.pop(b["ini"], None)
        doc.excl.pop(b["fin"], None)
    elif t == "tabla":
        cab = b["cab"]
        for ln, celdas in b["filas"]:
            partes = []
            if not any(cab):
                vals = [c for c in celdas if c]
                partes = [f"{vals[0]}: {' · '.join(vals[1:])}"] if len(vals) > 1 else vals
            for c_i, c in enumerate(celdas if any(cab) else []):
                if not c:
                    continue
                h = cab[c_i] if c_i < len(cab) and cab[c_i] else f"col{c_i + 1}"
                partes.append(f"{h}: {c}")
            doc.unidad("fila_tabla", ln, ln, b["sec"], " · ".join(partes), lead)
        if not b["filas"]:
            doc.unidad("tabla_plantilla", b["ini"], b["ini"] + 1, b["sec"],
                       "Tabla a llenar con columnas: " + " · ".join(c for c in cab if c), lead)
        else:
            doc.excluir(b["ini"], b["ini"] + 1, "encabezado de tabla: repetido dentro de cada fila")
    elif t == "lista":
        items = b["items"]
        simples = all(not it["sub"] and "\n" not in it["txt"] for it in items)
        n_cortos = sum(1 for it in items if palabras(it["txt"]) <= 7)
        cortos = simples and ((len(items) >= 2 and n_cortos == len(items)) or (len(items) >= 3 and n_cortos >= 0.75 * len(items)))
        if cortos:
            txt = "; ".join(re.sub(r"^\s*([-*+]|\d+[.)])\s+", "", it["txt"]) for it in items)
            doc.unidad("lista_vocabulario", items[0]["ini"], items[-1]["fin"], b["sec"], txt, lead)
        else:
            for it in items:
                doc.unidad("item", it["ini"], it["fin"], b["sec"], it["txt"], lead)


# ---------------------------------------------------------------- fuentes no markdown

def parse_yaml_toplevel(doc: Doc):
    L = doc.lineas
    ini = None
    clave = None
    pend_coment: list[int] = []
    for idx, t in enumerate(L + ["__FIN__:"]):
        m = re.match(r"^([A-Za-z_][\w-]*):", t)
        if m or idx == len(L):
            if clave is not None:
                fin = idx
                while fin > ini and not L[fin - 1].strip():
                    fin -= 1
                subs = [j for j in range(ini, fin) if re.match(r"^  [A-Za-z0-9_.\"'-][^:]*:", L[j])]
                if fin - ini > 60 and len(subs) >= 2:
                    cab_fin = subs[0]
                    for a_, j in enumerate(subs):
                        f_ = subs[a_ + 1] if a_ + 1 < len(subs) else fin
                        sub = L[j].split(":")[0].strip()
                        cuerpo = "\n".join(L[ini - 1:cab_fin]) + "\n" + "\n".join(L[j:f_])
                        doc.unidad("yaml", ini if a_ == 0 else j + 1, f_, f"{doc.ruta} › {clave} › {sub}", cuerpo)
                    clave, ini = (m.group(1), idx + 1) if m else (None, None)
                    if pend_coment and clave:
                        ini = pend_coment[0]
                    pend_coment = []
                    continue
                doc.unidad("yaml", ini, fin, f"{doc.ruta.split('/')[-3] if doc.ruta.startswith('.claude') else 'aurora skill'} vocabularies.yaml › {clave}", "\n".join(L[ini - 1:fin]))
            clave, ini = (m.group(1), idx + 1) if m else (None, None)
            if pend_coment and clave:
                ini = pend_coment[0]
            pend_coment = []
        elif clave is None and t.strip().startswith("#"):
            pend_coment.append(idx + 1)
        elif clave is None and t.strip():
            doc.excluir(idx + 1, idx + 1, "cabecera YAML")
    # comentarios de cabecera antes de la primera clave que quedaron fuera
    cubiertas = {x for u in doc.unidades for x in range(u["ini"], u["fin"] + 1)}
    for n_, t in enumerate(L, 1):
        if t.strip() and n_ not in cubiertas:
            doc.excluir(n_, n_, "comentario de cabecera YAML")


def json_units_capabilities(doc: Doc, data: dict):
    L = doc.lineas
    usados = set()
    for g in data.get("generators", []):
        pares = [f"{k}={json.dumps(v, ensure_ascii=False)}" for k, v in g.items() if k not in ("id",)]
        # intervalo de líneas del objeto: desde la '{' que lo abre hasta la '}' que lo cierra
        i_id = next(i for i, t in enumerate(L) if re.search(r'"id"\s*:\s*"%s"' % re.escape(g["id"]), t))
        ini = i_id
        while ini > 0 and not L[ini].strip().startswith("{"):
            ini -= 1
        ind = len(L[ini]) - len(L[ini].lstrip())
        fin = i_id
        while fin < len(L) - 1 and not (L[fin].strip().startswith("}") and len(L[fin]) - len(L[fin].lstrip()) == ind):
            fin += 1
        usados.update(range(ini + 1, fin + 2))
        doc.unidad("json", ini + 1, fin + 1, f"_capabilities.json › {g.get('id')}", f"{g.get('id')}: " + "; ".join(pares))
    meta = {k: v for k, v in data.items() if k != "generators"}
    lineas_meta = [i + 1 for i, t in enumerate(L) if i + 1 not in usados and t.strip() and t.strip() not in ("{", "}", "[", "]", "],", '"generators": [')]
    doc.unidad("json", min(lineas_meta), max(lineas_meta) if lineas_meta else 0, "_capabilities.json › meta",
               json.dumps(meta, ensure_ascii=False))
    for i, t in enumerate(L, 1):
        if t.strip() in ("{", "}", "[", "]", "],", '"generators": [') and i not in usados:
            doc.excluir(i, i, "llave/corchete de estructura JSON")


def json_units_schema(doc: Doc, data: dict, nombre: str):
    def walk(nodo, ruta, requeridos):
        if not isinstance(nodo, dict):
            return
        props = nodo.get("properties", {})
        req = set(nodo.get("required", []))
        for k, v in props.items():
            p = f"{ruta}.{k}" if ruta else k
            info = []
            for clave in ("type", "enum", "const", "pattern", "format", "minimum", "maximum", "minLength", "maxLength",
                          "minItems", "maxItems", "default", "description"):
                if isinstance(v, dict) and clave in v:
                    info.append(f"{clave}={json.dumps(v[clave], ensure_ascii=False)}")
            if isinstance(v, dict) and "oneOf" in v:
                info.append("oneOf=" + json.dumps(v["oneOf"], ensure_ascii=False)[:2000])
            info.append("requerido" if k in req else "opcional")
            doc.unidad("esquema", 0, 0, f"{nombre} › {p}", f"{p}: " + "; ".join(info))
            if isinstance(v, dict):
                walk(v, p, req)
                if isinstance(v.get("items"), dict):
                    walk(v["items"], p + "[]", req)
        for dk, dv in nodo.get("$defs", {}).items():
            walk(dv, f"$defs.{dk}", set())
        extra = nodo.get("additionalProperties")
        if extra is False and props:
            doc.unidad("esquema", 0, 0, f"{nombre} › {ruta or '(raíz)'}",
                       f"{ruta or '(raíz)'}: additionalProperties=false (ningún campo fuera de: {', '.join(props)})")
    top = [f"{k}={json.dumps(data[k], ensure_ascii=False)}" for k in ("title", "description") if k in data]
    if top:
        doc.unidad("esquema", 0, 0, f"{nombre} › (raíz)", "; ".join(top))
    walk(data, "", set(data.get("required", [])))


# ---------------------------------------------------------------- HTML (flujos del usuario) y linter parcheado

from html.parser import HTMLParser


class _HTMLSeg(HTMLParser):
    """Segmenta un flujo HTML: p, li, filas de tabla con sus encabezados, texto suelto, y cada diagrama
    (SVG de mermaid) reconstruido como lista de pasos y conexiones con sus etiquetas."""

    BLOQUE = {"p", "li"}

    def __init__(self, doc: Doc):
        super().__init__(convert_charrefs=True)
        self.doc = doc
        self.pila_sec: dict[int, str] = {}
        self.eyebrow = ""
        self.skip = 0          # style/script/head
        self.cap = None        # bloque capturando {tag, ini, partes, prof}
        self.tabla = None      # {cab:[], fila:None}
        self.svg = None        # {ini, nodos:{id:[texto]}, orden:[], aristas:[], elabels:[], ctx}
        self.stack: list[tuple[str, dict]] = []
        self.src = 0
        self.titulo_tag = None
        self.suelto = None     # texto suelto acumulado dentro de un mismo elemento padre

    def _flush(self, ln=None):
        sl = self.suelto
        if sl:
            t = re.sub(r"\s+", " ", "".join(sl["partes"])).strip()
            if t:
                self.doc.unidad("html_texto", sl["ini"], max(sl["fin"], sl["ini"]), sl["sec"], t)
        self.suelto = None

    def sec(self):
        return " › ".join(v for k, v in sorted(self.pila_sec.items()) if v)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        ln = self.getpos()[0]
        cls = a.get("class", "") or ""
        if self.suelto and tag not in ("span", "strong", "em", "i", "b", "code", "a", "br", "small", "sup", "sub"):
            self._flush()
        self.stack.append((tag, a))
        if tag in ("style", "script", "head", "title"):
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "svg" and self.svg is None:
            self.svg = {"ini": ln, "nodos": {}, "orden": [], "aristas": [], "elabels": [], "ctx": None, "prof": len(self.stack)}
            return
        if self.svg is not None:
            if tag == "g" and "node" in cls.split() and a.get("data-id"):
                self.svg["ctx"] = ("nodo", a["data-id"], len(self.stack))
                self.svg["nodos"].setdefault(a["data-id"], [])
                self.svg["orden"].append(a["data-id"])
            elif tag == "g" and "edgeLabel" in cls.split():
                self.svg["elabels"].append([])
                self.svg["ctx"] = ("elabel", len(self.svg["elabels"]) - 1, len(self.stack))
            elif tag == "path" and (a.get("id") or "").startswith("L-"):
                partes = a["id"][2:].rsplit("-", 1)[0]
                self.svg["aristas"].append(partes)
            return
        if tag in ("h1", "h2", "h3"):
            self.titulo_tag = (tag, [])
            return
        if tag == "div" and "eyebrow" in cls:
            self.titulo_tag = ("eyebrow", [])
            return
        if tag == "div" and cls.split() and cls.split()[0] == "n":
            self.titulo_tag = ("n", [])
            return
        if tag == "div" and "src" in cls.split():
            self.src += 1
            self.cap_src_ini = ln
            return
        if tag == "table":
            self.tabla = {"cab": [], "fila": None, "en_thead": False}
            return
        if self.tabla is not None:
            if tag == "thead":
                self.tabla["en_thead"] = True
            elif tag == "tr":
                self.tabla["fila"] = {"ini": ln, "celdas": [], "cel": None}
            elif tag in ("td", "th") and self.tabla["fila"] is not None:
                self.tabla["fila"]["cel"] = []
            return
        if tag in self.BLOQUE and self.cap is None:
            self.cap = {"tag": tag, "ini": ln, "partes": []}

    def handle_endtag(self, tag):
        ln = self.getpos()[0]
        if self.stack:
            # desapilar hasta el tag correspondiente
            for k in range(len(self.stack) - 1, -1, -1):
                if self.stack[k][0] == tag:
                    del self.stack[k:]
                    break
        if self.suelto and len(self.stack) < self.suelto["prof"]:
            self._flush()
        if tag in ("style", "script", "head", "title"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if self.svg is not None:
            ctx = self.svg["ctx"]
            if ctx and len(self.stack) < ctx[2]:
                self.svg["ctx"] = None
            if tag == "svg" and len(self.stack) < self.svg["prof"]:
                self._cerrar_svg(ln)
            return
        if self.titulo_tag and tag in ("h1", "h2", "h3", "div") and (tag == self.titulo_tag[0] or tag == "div"):
            kind, partes = self.titulo_tag
            t = re.sub(r"\s+", " ", "".join(partes)).strip()
            if kind == "eyebrow":
                self.eyebrow = t
            elif kind == "n":
                self.pila_sec[3] = t
            else:
                niv = int(kind[1])
                if niv <= 2:
                    self.pila_sec[1] = self.pila_sec.get(1) if niv == 2 else t
                    self.pila_sec[2] = (f"{self.eyebrow}: {t}" if self.eyebrow else t) if niv == 2 else ""
                    self.pila_sec[3] = ""
                    self.eyebrow = ""
                else:
                    self.pila_sec[3] = t
            self.titulo_tag = None
            return
        if tag == "div" and self.src:
            self.src -= 1
            self.doc.excluir(self.cap_src_ini, ln, "línea de fuentes citadas por la tarjeta del flujo")
            return
        if self.tabla is not None:
            f = self.tabla["fila"]
            if tag in ("td", "th") and f is not None and f["cel"] is not None:
                f["celdas"].append(re.sub(r"\s+", " ", "".join(f["cel"])).strip())
                f["cel"] = None
            elif tag == "tr" and f is not None:
                if self.tabla["en_thead"] or not self.tabla["cab"] and all(c for c in f["celdas"]) and False:
                    self.tabla["cab"] = f["celdas"]
                else:
                    cab = self.tabla["cab"]
                    partes = [f"{cab[i]}: {c}" if i < len(cab) and cab[i] else c for i, c in enumerate(f["celdas"]) if c]
                    if partes:
                        self.doc.unidad("fila_tabla", f["ini"], ln, self.sec(), " · ".join(partes))
                self.tabla["fila"] = None
            elif tag == "thead":
                self.tabla["en_thead"] = False
            elif tag == "table":
                self.tabla = None
            return
        if self.cap is not None and tag == self.cap["tag"]:
            t = re.sub(r"\s+", " ", "".join(self.cap["partes"])).strip()
            if t:
                self.doc.unidad("html_" + tag, self.cap["ini"], ln, self.sec(), t)
            self.cap = None

    def handle_data(self, data):
        if self.skip:
            return
        if self.svg is not None:
            ctx = self.svg["ctx"]
            if ctx and data.strip():
                if ctx[0] == "nodo":
                    self.svg["nodos"][ctx[1]].append(data.strip())
                else:
                    self.svg["elabels"][ctx[1]].append(data.strip())
            return
        if self.titulo_tag:
            self.titulo_tag[1].append(data)
            return
        if self.src:
            return
        if self.tabla is not None:
            f = self.tabla["fila"]
            if f is not None and f["cel"] is not None:
                f["cel"].append(data)
            return
        if self.cap is not None:
            self.cap["partes"].append(data)
            return
        ln = self.getpos()[0]
        if self.suelto is not None:
            self.suelto["partes"].append(data)
            self.suelto["fin"] = ln + data.count("\n")
        elif data.strip():
            # texto suelto (dentro de un div de tarjeta o sección): se acumula hasta que cierra su elemento padre
            if any("legend" in (a_.get("class") or "") for _, a_ in self.stack):
                self.doc.excluir(ln, ln, "leyenda de colores del diagrama")
                return
            inline = ("span", "strong", "em", "i", "b", "code", "a", "small", "sup", "sub")
            prof = len(self.stack)
            while prof > 0 and self.stack[prof - 1][0] in inline:
                prof -= 1
            self.suelto = {"ini": ln, "fin": ln + data.count("\n"), "partes": [data], "prof": prof,
                           "sec": self.sec()}

    def _cerrar_svg(self, ln):
        sv = self.svg
        nom = {k: " ".join(v) for k, v in sv["nodos"].items()}
        pasos = [f"{k}: {nom[k]}" for k in dict.fromkeys(sv["orden"])]
        conex = []
        for i, a in enumerate(sv["aristas"]):
            if "-" not in a:
                continue
            # los ids de nodo pueden contener '-'; se busca la partición que calza con dos nodos conocidos
            partes = a.split("-")
            par = None
            for c in range(1, len(partes)):
                x, y = "-".join(partes[:c]), "-".join(partes[c:])
                if x in nom and y in nom:
                    par = (x, y)
                    break
            if not par:
                continue
            et = " ".join(sv["elabels"][i]) if i < len(sv["elabels"]) else ""
            conex.append(f"{par[0]} → {par[1]}" + (f" [{et}]" if et else ""))
        txt = "Diagrama de flujo. Pasos: " + " | ".join(pasos) + ". Conexiones: " + "; ".join(conex)
        self.doc.unidad("diagrama", sv["ini"], ln, self.sec(), txt)
        self.svg = None


def parse_html(doc: Doc):
    seg = _HTMLSeg(doc)
    seg.feed("\n".join(doc.lineas))
    seg._flush()
    seg.close()
    cub = {x for u in doc.unidades for x in range(u["ini"], u["fin"] + 1)}
    for n_, t in enumerate(doc.lineas, 1):
        if t.strip() and n_ not in cub:
            doc.excluir(n_, n_, "marcado HTML/CSS sin texto (el texto de la página está en los registros)")


def parse_py_linter(doc: Doc):
    L = doc.lineas
    # docstring del módulo, un registro por parche P#
    i0 = next(i for i, t in enumerate(L) if t.strip().startswith('"""'))
    i1 = next(i for i in range(i0 + 1, len(L)) if L[i].strip().endswith('"""'))
    bloques, cur = [], None
    for i in range(i0, i1 + 1):
        t = L[i].replace('"""', "")
        if re.match(r"^P\d+\s", t) or cur is None:
            cur = {"ini": i + 1, "lineas": []}
            bloques.append(cur)
        cur["lineas"].append(t)
        cur["fin"] = i + 1
    for b in bloques:
        txt = "\n".join(b["lineas"]).strip()
        if txt:
            doc.unidad("linter_parche", b["ini"], b["fin"], "aurora prompt_linter.py (parcheado en el repo) › docstring", txt)
    # constantes de configuración (casos, presupuestos, alias)
    i = i1 + 1
    while i < len(L):
        m = re.match(r"^([A-Z][A-Z0-9_]+)\s*=\s*(.*)$", L[i])
        if m:
            ini = i
            while ini > 0 and L[ini - 1].startswith("#"):
                ini -= 1
            fin = i
            if m.group(2).rstrip().endswith(("{", "(", "[")):
                while fin < len(L) - 1 and not re.match(r"^[}\])]", L[fin]):
                    fin += 1
            doc.unidad("linter_constante", ini + 1, fin + 1, f"aurora prompt_linter.py › {m.group(1)}",
                       "\n".join(L[ini:fin + 1]))
            i = fin + 1
            continue
        i += 1
    cub = {x for u in doc.unidades for x in range(u["ini"], u["fin"] + 1)}
    for n_, t in enumerate(L, 1):
        if t.strip() and n_ not in cub:
            doc.excluir(n_, n_, "código del linter (implementación de las reglas de su docstring y constantes)")


# ---------------------------------------------------------------- inventario de fuentes

def fuentes():
    """(ruta_visible, Path, tipo, extra). Incluidas; las excluidas van en EXCLUIDAS con motivo."""
    out = []
    for p in sorted(SKILLS.rglob("*.md")):
        out.append((f"skills/{p.relative_to(SKILLS)}", p, "md", None))
    for p in sorted(SKILLS.rglob("*.tpl")):
        if p.name.endswith(".md.tpl"):
            out.append((f"skills/{p.relative_to(SKILLS)}", p, "md", None))
    out.append(("skills/aurora-prompt-linter/scripts/vocabularies.yaml",
                SKILLS / "aurora-prompt-linter/scripts/vocabularies.yaml", "yaml", None))
    out.append((".claude/hooks/aurora/vocabularies.yaml", REPO / ".claude/hooks/aurora/vocabularies.yaml", "yaml", None))
    out.append((".claude/hooks/aurora/README.md", REPO / ".claude/hooks/aurora/README.md", "md", None))
    out.append(("skills/visual-prompt-forge/adapters/_capabilities.json",
                SKILLS / "visual-prompt-forge/adapters/_capabilities.json", "capabilities", None))
    for rel in ("storyboard-architect/templates/shots.schema.json", "storyboard-architect/templates/text-overlays.schema.json",
                "storyboard-architect/templates/run.schema.json", "visual-asset-critic/templates/critique.schema.json",
                "visual-prompt-forge/adapters/capabilities.schema.json"):
        out.append((f"skills/{rel}", SKILLS / rel, "schema", None))
    reg = REPO / ".claude/rules/regimenes"
    for p in sorted(reg.glob("*.md")):
        out.append((f".claude/rules/regimenes/{p.name}", p, "md", None))
    for p in sorted((REPO / ".claude/rules/research").glob("*.md")):
        out.append((f".claude/rules/research/{p.name}", p, "md",
                    re.compile(r"hallazgos nuevos|reglas candidatas", re.I)))
    out.append((".claude/rules/DECISIONES.md", REPO / ".claude/rules/DECISIONES.md", "md", None))
    for p in sorted((PKG_REPO / "templates/v3.2").glob("*.md")):
        out.append((f"pkg/repo/templates/v3.2/{p.name}", p, "md", None))
    out.append(("pkg/repo/.claude/rules/v3/learned/LEARNING_REGISTRY_v3.2.md",
                PKG_REPO / ".claude/rules/v3/learned/LEARNING_REGISTRY_v3.2.md", "md", None))
    for f in ("production-learnings.v3.2.json", "production-learnings.v3.4.json"):
        out.append((f"pkg/repo/.claude/rules/v3/learned/{f}", PKG_REPO / ".claude/rules/v3/learned" / f, "learnings", None))
    out.append(("pkg/repo/.claude/rules/v3/learned/model-routing.v3.2.json",
                PKG_REPO / ".claude/rules/v3/learned/model-routing.v3.2.json", "routing", None))
    out.append(("pkg/repo/.claude/rules/v3/conflict-policies.v3.1.json",
                PKG_REPO / ".claude/rules/v3/conflict-policies.v3.1.json", "policies", None))
    out.append(("apd/apd/politicas.py", APD / "apd/politicas.py", "politicas", None))
    for f in ("flujo-anclas.html", "flujo-spot.html"):
        out.append((f"apd/originales/{f}", APD / "originales" / f, "html", None))
    out.append((".claude/hooks/aurora/prompt_linter.py", REPO / ".claude/hooks/aurora/prompt_linter.py", "linter", None))
    return out


EXCLUIDAS = [
    ("skills/*/tools/*.py, check.sh, prompt_linter.py", "código que implementa validaciones ya enunciadas en los .md (validate_*, linter)"),
    ("skills/*/LICENSE, NOTICE", "texto legal; la obligación de atribución ya está en production-package.md §4"),
    ("skills/**/examples/*.json, *.txt, run.json, shots.json de ejemplo", "salidas de ejemplo; su sintaxis está en los esquemas y adaptadores incluidos"),
    ("skills/storyboard-html-preview/templates/*.html.tpl, *.css.tpl", "plantillas de maquetación HTML/CSS, no normas de producción"),
    ("pkg/project_knowledge_pack/*", "concatenación de los mismos skills (KNOWLEDGE_MANIFEST: 272 archivos consolidados)"),
    ("pkg/repo/notebooklm-corpus, nblm-ids, review-source, review-rules, build/*, *.jsonl", "copias y derivados de los skills (NotebookLM retirado, decisión 9)"),
    ("pkg/repo/production-package/RULES_MATRIX.md", "reconstrucción de las 20 reglas de SW30, que se extraen de su fuente"),
    (".claude/rules/METODO.md, scope.yaml, esquemas v3/v3.4", "procedimiento de la base de reglas y esquemas de herramientas, no normas de producción"),
    ("apd/apd/conflictos.py", "resoluciones que citan reglas ya incluidas; las decisiones del usuario están en politicas.py"),
    (".claude/rules/research/*.md fuera de 'hallazgos nuevos'", "bitácora de búsqueda, citas y veredictos (evidencia, no reglas)"),
]


def construir():
    docs: list[Doc] = []
    for ruta, p, tipo, extra in fuentes():
        texto = p.read_text(encoding="utf-8", errors="replace")
        lineas = texto.split("\n")
        if lineas and lineas[-1] == "":
            lineas = lineas[:-1]
        d = Doc(ruta, lineas)
        if tipo == "md" and ruta.endswith(".tpl"):
            d.unidad("plantilla", 1, len(lineas), f"plantilla {p.name}", "\n".join(lineas))
        elif tipo == "md":
            parse_md(d, extra)
        elif tipo == "html":
            parse_html(d)
        elif tipo == "linter":
            parse_py_linter(d)
        elif tipo == "yaml":
            parse_yaml_toplevel(d)
        elif tipo == "capabilities":
            json_units_capabilities(d, json.loads(texto))
        elif tipo == "schema":
            json_units_schema(d, json.loads(texto), p.name)
        elif tipo == "learnings":
            for r in json.loads(texto).get("rules", []):
                rr, md = r.get("rule", {}), r.get("metadata", {})
                d.unidad("aprendizaje", 0, 0, f"{p.name} › {rr.get('id')}",
                         f"{rr.get('text')} (efecto={md.get('effect')}, prioridad={md.get('priority')}; "
                         f"{md.get('classification_provenance', {}).get('notes', '')})")
        elif tipo == "routing":
            for r in json.loads(texto).get("routes", []):
                d.unidad("ruteo", 0, 0, f"{p.name} › {r.get('id')}",
                         f"Preferir {json.dumps(r.get('preferred'), ensure_ascii=False)} cuando "
                         f"{json.dumps(r.get('when'), ensure_ascii=False)}; {r.get('override_policy')}; "
                         f"confianza {r.get('confidence')}. Evidencia: {r.get('evidence')}")
        elif tipo == "policies":
            for r in json.loads(texto).get("policies", []):
                d.unidad("politica", 0, 0, f"{p.name} › {r.get('id')}",
                         f"{r.get('conflict_key')}: gana la regla {r.get('winner_rule_id')}. {r.get('reason')}")
        elif tipo == "politicas":
            spec = importlib.util.spec_from_file_location("politicas_src", p)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            for nombre in dir(mod):
                v = getattr(mod, nombre)
                if isinstance(v, dict) and str(v.get("id", "")).startswith("U-"):
                    extra_t = "".join(f" {k}: {v[k]}." for k in ("dramatico_si", "factor_bloqueo", "compatible_con") if k in v)
                    d.unidad("politica_usuario", 0, 0, f"politicas.py › {v['id']}",
                             f"{v['regla']}{extra_t} (instrucción literal del usuario, {v.get('fecha')}: «{v.get('instruccion')}»)")
        docs.append(d)
    return docs


def verificar(docs, db_path: Path):
    problemas = []
    # 1. cobertura de líneas
    sin_cubrir = []
    for d in docs:
        if not any(u["ini"] for u in d.unidades) and d.ruta.endswith((".json", ".py")) and "prompt_linter" not in d.ruta:
            continue  # fuentes estructuradas: cobertura por objeto, no por línea
        cub = set()
        for u in d.unidades:
            if u["ini"]:
                cub.update(range(u["ini"], u["fin"] + 1))
        for n_, t in enumerate(d.lineas, 1):
            if t.strip() and n_ not in cub and n_ not in d.excl:
                sin_cubrir.append(f"{d.ruta}:{n_}: {t.strip()[:100]}")
    if sin_cubrir:
        problemas.append(("líneas sin registro ni exclusión", sin_cubrir))
    # índice por archivo
    por_archivo: dict[str, list[dict]] = {}
    for d in docs:
        por_archivo[d.ruta] = d.unidades

    def contiene(ruta, linea, texto):
        for u in por_archivo.get(ruta, []):
            if u["ini"] <= linea <= u["fin"]:
                if texto and norm(texto)[:80] not in norm(u["texto"]).replace("**", "") and \
                        norm(texto)[:80].replace("**", "") not in norm(u["texto"]).replace("**", ""):
                    continue
                return u
        return None

    # 2. reglas de la base actual
    faltan_reglas = []
    n_reglas = 0
    if db_path.exists():
        con = sqlite3.connect(db_path)
        for rid, skill, archivo, linea, texto in con.execute("select id, skill, archivo, linea, texto from reglas"):
            n_reglas += 1
            ruta = f".claude/rules/regimenes/{archivo.split('/')[-1]}" if skill == "regimenes" or archivo.startswith("regimenes/") \
                else f"skills/{skill}/{archivo}"
            t = re.sub(r"^[-*+]\s+|^\d+[.)]\s+|^\|", "", texto.strip())[:60]
            t = re.sub(r"\[(FUENTE|A PRUEBA|CAMPO|REFUTADA|CANONICA)[^\]]*\]\s*$", "", t)
            if not contiene(ruta, linea, "") :
                faltan_reglas.append(f"{rid} {ruta}:{linea} {texto[:80]}")
        con.close()
    if faltan_reglas:
        problemas.append(("reglas de rules.sqlite fuera de todo registro", faltan_reglas))
    # 3. puntos de sintaxis
    faltan_sx = []
    n_sx = 0
    sx = json.loads((APD / "data/sintaxis_fuente.json").read_text(encoding="utf-8"))

    def citas(o):
        if isinstance(o, dict):
            if "archivo" in o and "linea_ini" in o:
                yield o
            for v in o.values():
                yield from citas(v)
        elif isinstance(o, list):
            for v in o:
                yield from citas(v)
    vistos = set()
    for c in citas({k: v for k, v in sx.items() if k != "_meta"}):
        clave = (c["archivo"], c["linea_ini"], c["linea_fin"])
        if clave in vistos:
            continue
        vistos.add(clave)
        n_sx += 1
        arch = c["archivo"]
        if arch.startswith(".claude/rules/regimenes/") or arch.startswith("skills/") or arch.startswith(".claude/rules/"):
            ruta = arch
        else:
            ruta = arch
        if ruta not in por_archivo:
            faltan_sx.append(f"{arch}:{c['linea_ini']} (archivo no incluido) {c.get('texto', '')[:60]}")
            continue
        ok = all(any(u["ini"] <= ln_ <= u["fin"] for u in por_archivo[ruta])
                 for ln_ in range(c["linea_ini"], c["linea_fin"] + 1)
                 if (ln_ - 1) < len(next(d for d in docs if d.ruta == ruta).lineas)
                 and next(d for d in docs if d.ruta == ruta).lineas[ln_ - 1].strip()
                 and ln_ not in next(d for d in docs if d.ruta == ruta).excl)
        if not ok:
            faltan_sx.append(f"{arch}:{c['linea_ini']}-{c['linea_fin']} {c.get('texto', '')[:60]}")
    if faltan_sx:
        problemas.append(("citas de sintaxis fuera de todo registro", faltan_sx))
    return problemas, n_reglas, n_sx


def consolidar(docs):
    """Une duplicados exactos (copias idénticas en varios archivos) conservando todas las fuentes."""
    registros: dict[str, dict] = {}
    for d in docs:
        orden = sorted(range(len(d.unidades)), key=lambda k: (d.unidades[k]["ini"] or 10**9, k))
        for pos, k in enumerate(orden, 1):
            d.unidades[k]["parrafo"] = pos
        for u in d.unidades:
            clave = norm(u["texto"])
            rid = hashlib.sha1(clave.encode()).hexdigest()[:12]
            f = {"archivo": d.ruta, "linea_ini": u["ini"], "linea_fin": u["fin"], "seccion": u["seccion"],
                 "parrafo": u["parrafo"], "total": len(d.unidades)}
            if rid in registros:
                registros[rid]["fuentes"].append(f)
            else:
                registros[rid] = {"id": rid, "texto": u["texto"], "tipo": u["tipo"], "fuentes": [f],
                                  "palabras": palabras(u["texto"])}
    return list(registros.values())


def guardar(registros, docs, db_path: Path):
    con = sqlite3.connect(db_path)
    con.executescript("""
        DROP TABLE IF EXISTS registros;
        DROP TABLE IF EXISTS registros_fuente;
        DROP TABLE IF EXISTS registros_exclusion;
        CREATE TABLE registros (id TEXT PRIMARY KEY, orden INTEGER NOT NULL, texto TEXT NOT NULL,
                                tipo TEXT NOT NULL, palabras INTEGER NOT NULL);
        CREATE TABLE registros_fuente (registro_id TEXT NOT NULL REFERENCES registros(id), archivo TEXT NOT NULL,
                                       linea_ini INTEGER, linea_fin INTEGER, seccion TEXT,
                                       parrafo INTEGER, parrafos_en_documento INTEGER);
        CREATE TABLE registros_exclusion (archivo TEXT NOT NULL, linea INTEGER NOT NULL, texto TEXT, motivo TEXT NOT NULL);
    """)
    for n_, r in enumerate(registros, 1):
        con.execute("insert into registros values (?,?,?,?,?)", (r["id"], n_, r["texto"], r["tipo"], r["palabras"]))
        for f in r["fuentes"]:
            con.execute("insert into registros_fuente values (?,?,?,?,?,?,?)",
                        (r["id"], f["archivo"], f["linea_ini"], f["linea_fin"], f["seccion"], f["parrafo"], f["total"]))
    for d in docs:
        for ln_, mot in sorted(d.excl.items()):
            con.execute("insert into registros_exclusion values (?,?,?,?)", (d.ruta, ln_, d.lineas[ln_ - 1].strip(), mot))
    con.commit()
    con.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(APD / "data/rules.sqlite"))
    ap.add_argument("--json", default=None, help="volcado JSON de registros")
    a = ap.parse_args()
    docs = construir()
    problemas, n_reglas, n_sx = verificar(docs, Path(a.db))
    registros = consolidar(docs)
    n_unid = sum(len(d.unidades) for d in docs)
    print(f"fuentes: {len(docs)} · unidades: {n_unid} · registros únicos: {len(registros)} · "
          f"líneas excluidas con motivo: {sum(len(d.excl) for d in docs)}")
    print(f"verificadas: {n_reglas} reglas de rules.sqlite · {n_sx} citas de sintaxis")
    for titulo, lista in problemas:
        print(f"FALLA {titulo}: {len(lista)}")
        for x in lista[:40]:
            print("   ", x)
    if a.json:
        Path(a.json).write_text(json.dumps(registros, ensure_ascii=False, indent=1), encoding="utf-8")
    if problemas:
        sys.exit(1)
    guardar(registros, docs, Path(a.db))
    print("OK: tablas registros, registros_fuente, registros_exclusion escritas en", a.db)


if __name__ == "__main__":
    main()
