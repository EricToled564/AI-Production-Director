#!/usr/bin/env python3
"""Consulta la base v3: de un brief a las reglas que aplican, con traza.

Tres pasos, en este orden:

  1. Facetas. Deterministas por regex sobre el brief (modelo d8, caso T1..T5 y
     compañía, tipo de acción d2, sujetos d3, tratamiento d4, ángulo d9, tarea
     E?.? citada). Las que el brief no fija se SUGIEREN por similitud contra los
     prototipos (centroide de la descripción de cada valor), pero no se aplican
     salvo --aplicar-sugeridas: una sugerencia del modelo no filtra reglas.
     Las facetas pasadas por línea de comandos (--caso, --tarea, --modelo, --d2…)
     son del usuario y mandan sobre el regex.
  2. Filtro duro en SQL por las facetas confirmadas. Una regla entra si tiene el
     valor o si NO tiene ninguna faceta en esa dimensión: nunca se excluye por
     ausencia de clasificación; se marca "sin faceta". Las REFUTADA no se sirven.
  3. Ranking híbrido dentro del conjunto: RRF de BM25 (FTS5) y coseno (e5-large),
     con boost por prioridad y fuerza. Lo que no cabe en --presupuesto queda
     contado como "fuera por presupuesto", nunca callado.

Cada consulta se registra en briefs / brief_regla con sus scores y su rank.

Uso:
    python3 rule_query.py --db rules.sqlite --brief "maestro de rostro T1 para Nano Banana Pro, documental"
    python3 rule_query.py --db rules.sqlite --brief "…" --caso T4 --d3 2_sin_contacto --presupuesto 20000 --json

Sin fastembed/numpy en el intérprete, el paso 3 usa sólo BM25 y el paso 1 no sugiere;
se dice en la cabecera. El venv del proyecto tiene ambos.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

HOOKS = Path(__file__).resolve().parent
sys.path.insert(0, str(HOOKS))
import rules_v3 as v3  # noqa: E402

RRF_K = 60
DIMENSIONES = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9"]

# Detección determinista de caso por palabras clave ES/EN. Se acumulan todos los que peguen.
CASO_REGEX: list[tuple[str, re.Pattern]] = [
    ("T1", re.compile(r"\bT1\b|maestro de rostro|face master|master face|rostro maestro|headshot|identity master", re.I)),
    ("T2", re.compile(r"\bT2\b|maestro de cuerpo|body master|full[- ]body master|cuerpo completo", re.I)),
    ("T3", re.compile(r"\bT3\b|cuadro (?:con )?(?:1|una) persona|one person in (?:a )?scene|una persona en", re.I)),
    ("T4", re.compile(r"\bT4\b|cuadro (?:con )?(?:2|dos) personas|dos personas|two people|2 people|pareja|couple", re.I)),
    ("T5", re.compile(r"\bT5\b|edici[oó]n quir[uú]rgica|surgical edit|\bedit(?:ar|a)?\b (?:la|una|esta) imagen|retoque|inpaint", re.I)),
    ("PROD", re.compile(r"\bPROD\b|\bproducto\b|\bproduct shot\b|\bpackshot\b|\bcomida\b|\bfood\b|\bbebida\b|\bbeverage\b", re.I)),
    ("GRAF", re.compile(r"\bGRAF\b|\bposter\b|\bp[oó]ster\b|\bslide\b|\bdiapositiva\b|\bUI\b|\bmockup\b|\bthumbnail\b|\bbanner\b", re.I)),
    ("MULTI", re.compile(r"\bMULTI\b|multi[- ]?panel|\bgrid\b|\bcuadr[ií]cula\b|\bcontact sheet\b|character sheet", re.I)),
    ("REF", re.compile(r"\bREF\b|imagen de referencia|image[- ]to[- ]prompt|recrear (?:esta|la) imagen|reverse prompt", re.I)),
    ("CLIP", re.compile(r"\bCLIP\b|\bclip\b|\bvideo\b|\bv[ií]deo\b|image[- ]to[- ]video|\bkling\b|\bveo\b|\bseedance\b|\bhailuo\b|\bsora\b", re.I)),
    ("SHOT", re.compile(r"\bSHOT\b|shot ?list|storyboard|shots\.json|\bplaneaci[oó]n de shots\b", re.I)),
    ("GUION", re.compile(r"\bGUION\b|\bgui[oó]n\b|\bscreenplay\b|\bscript\b|\btreatment\b|\btratamiento narrativo\b", re.I)),
    ("MARCA", re.compile(r"\bMARCA\b|brand[- ]lock|\bbrand book\b|\bmarca\b", re.I)),
    ("QA", re.compile(r"\bQA\b|\bcr[ií]tica\b|\bcritique\b|\brevisar (?:el|este) render\b|\breview this render\b", re.I)),
    ("ENTREGA", re.compile(r"\bENTREGA\b|\bpackage\b|\bpaquete\b|\bpreview html\b|\bentrega al cliente\b", re.I)),
    ("LUGAR", re.compile(r"\bLUGAR\b|placa de lugar|environment (?:ref|plate)|\blocaci[oó]n vac[ií]a\b|\bempty plate\b", re.I)),
    ("EDIF", re.compile(r"\bEDIF\b|\bedificio\b|\bedificaci[oó]n\b|\blandmark\b|\bfachada\b|\barquitectura\b", re.I)),
    ("ANIMAL", re.compile(r"\bANIMAL\b|\banimal\b|\bperro\b|\bgato\b|\bcaballo\b|\bdog\b|\bcat\b|\bhorse\b|\bave\b|\bbird\b", re.I)),
    ("OBJ", re.compile(r"\bOBJ\b|\bobjeto\b|\bprop\b|\bveh[ií]culo\b|\bauto\b|\bcoche\b|\bcar\b|\bmoto\b|\bpelota\b|\bbal[oó]n\b", re.I)),
    ("MULTITUD", re.compile(r"\bMULTITUD\b|\bmultitud\b|\bcrowd\b|\bestadio\b|\bstadium\b|\bp[uú]blico\b", re.I)),
    ("ENSAMBLE", re.compile(r"\bENSAMBLE\b|\bensamble\b|\bensemble\b|\bequipo titular\b|\bbanda\b|\bfamilia\b|\bfamily\b|\bgrupo de\b", re.I)),
]

TAREA_REGEX = re.compile(r"\b(E[0-7]\.\d|POST\.[12]|PROMPT_IMAGEN|PROMPT_VIDEO|ESTRATEGIA|DOC)\b")

STOPWORDS = set("""
de la el los las un una unos unas para por con sin sobre entre del al en y o u que como más mas muy
the a an of to in on for with and or not is are be this that from by at as into
""".split())


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------------- paso 1: facetas

def detectar_facetas(brief: str) -> dict[str, list[str]]:
    """Facetas deterministas por regex. Devuelve {dimension: [valores]} (dimensiones: caso, tarea, d1..d9)."""
    det: dict[str, list[str]] = {}
    for caso, pat in CASO_REGEX:
        if pat.search(brief):
            det.setdefault("caso", []).append(caso)
    for cod in TAREA_REGEX.findall(brief):
        if cod not in det.setdefault("tarea", []):
            det["tarea"].append(cod)
    for dim, valor, pat in v3.REGEX_FACETA:
        if dim in ("d5", "d6", "d7"):
            continue  # abiertas: sugerir, no filtrar
        if pat.search(brief) and valor not in det.setdefault(dim, []):
            det[dim].append(valor)
    # "keyframe de inicio / first frame" fija el rol
    if re.search(r"keyframe (?:de )?inicio|first frame|start frame|frame inicial", brief, re.I):
        det.setdefault("d1", []) and None
        if "keyframe_ff" not in det.setdefault("d1", []):
            det["d1"].append("keyframe_ff")
    # Un brief de imagen que menciona un modelo de imagen y no dice video no es CLIP
    # aunque cite 'veo' dentro de otra palabra: los patrones ya llevan \b, no hace falta más.
    return det


def cargar_np():
    try:
        import numpy as np  # type: ignore
        return np
    except ImportError:
        return None


def vector_brief(brief: str):
    """Vector normalizado del brief con prefijo 'query: '. None si no hay fastembed."""
    np = cargar_np()
    if np is None:
        return None
    try:
        modelo = v3.cargar_modelo()
    except Exception:  # noqa: BLE001
        return None
    if modelo is None:
        return None
    return v3.vectorizar(modelo, ["query: " + brief])[0]


def sugerir_facetas(con: sqlite3.Connection, vb, confirmadas: dict[str, list[str]], top: int = 1) -> dict[str, list[tuple[str, float]]]:
    """Para cada dimensión sin valor confirmado, el prototipo más cercano al brief."""
    np = cargar_np()
    if vb is None or np is None:
        return {}
    filas = con.execute("SELECT tipo, codigo, vector FROM prototipos WHERE modelo_emb=?", (v3.MODELO_EMB,)).fetchall()
    if not filas:
        return {}
    por_dim: dict[str, list[tuple[str, float]]] = {}
    for tipo, codigo, blob in filas:
        v = np.frombuffer(blob, dtype="<f4")
        score = float(np.dot(v, vb))
        if tipo == "caso":
            dim, valor = "caso", codigo
        elif tipo == "tarea":
            dim, valor = "tarea", codigo
        else:
            dim, valor = codigo.split(":", 1)
        por_dim.setdefault(dim, []).append((valor, score))
    sugeridas: dict[str, list[tuple[str, float]]] = {}
    for dim, lista in por_dim.items():
        if confirmadas.get(dim):
            continue
        lista.sort(key=lambda kv: -kv[1])
        sugeridas[dim] = [(v, round(s, 3)) for v, s in lista[:top]]
    return sugeridas


# --------------------------------------------------------------------------- paso 2: filtro duro

def filtrar(con: sqlite3.Connection, confirmadas: dict[str, list[str]]) -> tuple[list[str], dict[str, list[str]]]:
    """Ids que pasan el filtro y, por id, las dimensiones en las que entró 'sin faceta'."""
    condiciones: list[str] = ["r.estado <> 'REFUTADA'"]
    params: list = []
    for dim, valores in confirmadas.items():
        if not valores:
            continue
        marcas = ",".join("?" * len(valores))
        if dim == "caso":
            condiciones.append(f"(EXISTS (SELECT 1 FROM regla_caso x WHERE x.regla_id=r.id AND x.caso IN ({marcas}))"
                               " OR NOT EXISTS (SELECT 1 FROM regla_caso x WHERE x.regla_id=r.id))")
        elif dim == "tarea":
            condiciones.append(f"(EXISTS (SELECT 1 FROM regla_tarea x WHERE x.regla_id=r.id AND x.tarea IN ({marcas}))"
                               " OR NOT EXISTS (SELECT 1 FROM regla_tarea x WHERE x.regla_id=r.id))")
        else:
            # 'ninguno' es un valor explícito que significa "esta regla no discrimina por esta
            # dimensión": se comporta exactamente como no tener fila, nunca excluye.
            condiciones.append(f"(EXISTS (SELECT 1 FROM regla_faceta x WHERE x.regla_id=r.id AND x.dimension=? AND x.valor IN ({marcas}))"
                               " OR NOT EXISTS (SELECT 1 FROM regla_faceta x WHERE x.regla_id=r.id AND x.dimension=?)"
                               " OR EXISTS (SELECT 1 FROM regla_faceta x WHERE x.regla_id=r.id AND x.dimension=? AND x.valor='ninguno'))")
            params.append(dim)
        params.extend(valores)
        if dim not in ("caso", "tarea"):
            params.append(dim)
            params.append(dim)
    sql = "SELECT r.id FROM reglas r WHERE " + " AND ".join(condiciones)
    ids = [row[0] for row in con.execute(sql, params)]
    # qué dimensiones confirmadas no tiene la regla (entró por ausencia)
    sin: dict[str, list[str]] = {}
    tiene_caso = {r[0] for r in con.execute("SELECT DISTINCT regla_id FROM regla_caso")}
    tiene_tarea = {r[0] for r in con.execute("SELECT DISTINCT regla_id FROM regla_tarea")}
    tiene_dim: dict[str, set[str]] = {}
    for rid, dim in con.execute("SELECT DISTINCT regla_id, dimension FROM regla_faceta WHERE valor <> 'ninguno'"):
        tiene_dim.setdefault(dim, set()).add(rid)
    for rid in ids:
        faltan = []
        for dim, valores in confirmadas.items():
            if not valores:
                continue
            if dim == "caso" and rid not in tiene_caso:
                faltan.append(dim)
            elif dim == "tarea" and rid not in tiene_tarea:
                faltan.append(dim)
            elif dim.startswith("d") and rid not in tiene_dim.get(dim, set()):
                faltan.append(dim)
        if faltan:
            sin[rid] = faltan
    return ids, sin


# --------------------------------------------------------------------------- paso 3: ranking

def consulta_fts(brief: str) -> str:
    tokens = [t for t in re.findall(r"\w+", brief.lower()) if len(t) >= 3 and t not in STOPWORDS]
    vistos: list[str] = []
    for t in tokens:
        if t not in vistos:
            vistos.append(t)
    return " OR ".join(f'"{t}"' for t in vistos)


def ranking(con: sqlite3.Connection, brief: str, ids: list[str], vb) -> dict[str, dict]:
    """RRF de BM25 y coseno, con boost por prioridad y fuerza. Devuelve por id sus scores."""
    conjunto = set(ids)
    n = len(ids)
    rank_bm25: dict[str, int] = {}
    score_bm25: dict[str, float] = {}
    q = consulta_fts(brief)
    if q:
        try:
            filas = con.execute("SELECT id, bm25(reglas_fts) FROM reglas_fts WHERE reglas_fts MATCH ? ORDER BY 2",
                                (q,)).fetchall()
        except sqlite3.OperationalError:
            filas = []
        pos = 0
        for rid, s in filas:
            if rid in conjunto:
                pos += 1
                rank_bm25[rid] = pos
                score_bm25[rid] = -float(s)
    rank_cos: dict[str, int] = {}
    score_cos: dict[str, float] = {}
    np = cargar_np()
    if vb is not None and np is not None:
        filas = con.execute("SELECT regla_id, vector FROM embeddings WHERE modelo_emb=?", (v3.MODELO_EMB,)).fetchall()
        filas = [(rid, blob) for rid, blob in filas if rid in conjunto]
        if filas:
            mat = np.frombuffer(b"".join(b for _, b in filas), dtype="<f4").reshape(len(filas), -1)
            sims = mat @ vb  # barrido exhaustivo: 1k x 1024 cabe de sobra en memoria
            orden = np.argsort(-sims)
            for pos, k in enumerate(orden, 1):
                rank_cos[filas[k][0]] = pos
                score_cos[filas[k][0]] = float(sims[k])
    meta = {rid: (p, f) for rid, p, f in con.execute("SELECT id, prioridad, fuerza FROM reglas")}
    out: dict[str, dict] = {}
    for rid in ids:
        rb = rank_bm25.get(rid, n + 1)
        rc = rank_cos.get(rid, n + 1)
        rrf = 1.0 / (RRF_K + rb) + 1.0 / (RRF_K + rc)
        prioridad, fuerza = meta.get(rid, (3, "ESTRUCTURA"))
        boost = 1.0 + 0.15 * (5 - prioridad) / 4 + {"PROHIBICION": 0.2, "OBLIGACION": 0.1}.get(fuerza, 0.0)
        out[rid] = {"bm25": score_bm25.get(rid), "cos": score_cos.get(rid), "final": rrf * boost}
    return out


# --------------------------------------------------------------------------- salida

def linea_md(rid: str, skill: str, texto: str) -> str:
    return f"- [{rid}] ({skill}) {texto}"


def ejecutar(con: sqlite3.Connection, brief: str, explicitas: dict[str, list[str]], presupuesto: int,
             aplicar_sugeridas: bool, registrar: bool = True) -> dict:
    detectadas = detectar_facetas(brief)
    confirmadas: dict[str, list[str]] = {}
    for dim, vals in detectadas.items():
        confirmadas[dim] = list(vals)
    for dim, vals in explicitas.items():
        if vals:
            confirmadas[dim] = list(vals)  # el usuario manda sobre el regex en esa dimensión
    confirmado_por = "usuario+regex" if explicitas and detectadas else ("usuario" if explicitas else "regex")

    vb = vector_brief(brief)
    sugeridas = sugerir_facetas(con, vb, confirmadas)
    if aplicar_sugeridas:
        for dim, lista in sugeridas.items():
            confirmadas[dim] = [lista[0][0]]
        confirmado_por += "+sugeridas"

    ids, sin = filtrar(con, confirmadas)
    scores = ranking(con, brief, ids, vb)
    orden = sorted(ids, key=lambda r: -scores[r]["final"])
    filas = {rid: (skill, archivo, linea, texto) for rid, skill, archivo, linea, texto in con.execute(
        f"SELECT id, skill, archivo, linea, texto FROM reglas WHERE id IN ({','.join('?' * len(ids))})", ids)} if ids else {}

    incluidas: list[str] = []
    usado = 0
    for rid in orden:
        skill, _a, _l, texto = filas[rid]
        largo = len(linea_md(rid, skill, texto)) + 1
        if usado + largo > presupuesto:
            continue
        usado += largo
        incluidas.append(rid)
    fuera = len(ids) - len(incluidas)
    sin_faceta_incl = sum(1 for rid in incluidas if rid in sin)

    brief_id = hashlib.sha1(f"{brief}\x00{now()}".encode()).hexdigest()[:12]
    if registrar:
        con.execute("INSERT INTO briefs VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (brief_id, brief, now(), json.dumps(confirmadas, ensure_ascii=False),
                     json.dumps(sugeridas, ensure_ascii=False), confirmado_por, presupuesto,
                     len(ids), len(incluidas), fuera, sum(1 for r in ids if r in sin)))
        incl = set(incluidas)
        con.executemany(
            "INSERT OR REPLACE INTO brief_regla (brief_id, regla_id, rank, score_bm25, score_cos, score_final, incluida, sin_faceta)"
            " VALUES (?,?,?,?,?,?,?,?)",
            [(brief_id, rid, k, scores[rid]["bm25"], scores[rid]["cos"], scores[rid]["final"],
              1 if rid in incl else 0, 1 if rid in sin else 0) for k, rid in enumerate(orden, 1)])
        con.commit()

    # agrupado por archivo, en orden de mejor score del grupo; dentro, por línea
    grupos: dict[str, list[str]] = {}
    for rid in incluidas:
        skill, archivo, _l, _t = filas[rid]
        grupos.setdefault(f"{skill}/{archivo}", []).append(rid)
    for k in grupos:
        grupos[k].sort(key=lambda r: filas[r][2])
    return {
        "brief_id": brief_id, "brief": brief, "facetas_confirmadas": confirmadas,
        "facetas_sugeridas": sugeridas, "confirmado_por": confirmado_por,
        "vectorial": vb is not None, "presupuesto": presupuesto,
        "total_filtro": len(ids), "incluidas": len(incluidas), "fuera_presupuesto": fuera,
        "sin_faceta_total": sum(1 for r in ids if r in sin), "sin_faceta_incluidas": sin_faceta_incl,
        "grupos": [{"archivo": k, "reglas": [
            {"id": rid, "skill": filas[rid][0], "linea": filas[rid][2], "texto": filas[rid][3],
             "score": round(scores[rid]["final"], 5), "sin_faceta": sin.get(rid, [])} for rid in v]}
            for k, v in grupos.items()],
    }


def render_md(res: dict) -> str:
    out: list[str] = []
    out.append(f"# Reglas para el brief `{res['brief_id']}`")
    out.append(f"brief: {res['brief']}")
    conf = " · ".join(f"{d}={','.join(v)}" for d, v in res["facetas_confirmadas"].items() if v) or "ninguna"
    out.append(f"facetas confirmadas ({res['confirmado_por']}): {conf}")
    if res["facetas_sugeridas"]:
        sug = " · ".join(f"{d}={v[0][0]} ({v[0][1]})" for d, v in sorted(res["facetas_sugeridas"].items()))
        out.append(f"facetas sugeridas por similitud (no aplicadas): {sug}")
    out.append(f"ranking: {'BM25 + coseno (RRF)' if res['vectorial'] else 'sólo BM25 (sin fastembed en este intérprete)'}"
               f" · presupuesto {res['presupuesto']} caracteres")
    out.append(f"total del filtro: {res['total_filtro']} · incluidas: {res['incluidas']} · "
               f"fuera por presupuesto: {res['fuera_presupuesto']} · sin faceta: {res['sin_faceta_total']} "
               f"(de ellas incluidas: {res['sin_faceta_incluidas']})")
    out.append("")
    for g in res["grupos"]:
        out.append(f"## {g['archivo']}")
        for r in g["reglas"]:
            marca = f"  [sin faceta: {','.join(r['sin_faceta'])}]" if r["sin_faceta"] else ""
            out.append(linea_md(r["id"], r["skill"], r["texto"]) + marca)
        out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Reglas aplicables a un brief (base v3)")
    ap.add_argument("--db", default="rules.sqlite")
    ap.add_argument("--brief", required=True)
    ap.add_argument("--caso", action="append", default=[])
    ap.add_argument("--tarea", action="append", default=[])
    ap.add_argument("--modelo", action="append", default=[], help="faceta d8")
    for d in DIMENSIONES:
        ap.add_argument(f"--{d}", action="append", default=[], help=f"faceta {d} ({v3.FACETAS[d]['nombre']})")
    ap.add_argument("--presupuesto", type=int, default=40000, help="caracteres del bloque markdown")
    ap.add_argument("--aplicar-sugeridas", action="store_true")
    ap.add_argument("--sin-registrar", action="store_true", help="no escribe en briefs/brief_regla")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    explicitas: dict[str, list[str]] = {}
    if args.caso:
        explicitas["caso"] = [c.upper() for c in args.caso]
    if args.tarea:
        explicitas["tarea"] = args.tarea
    for d in DIMENSIONES:
        vals = list(getattr(args, d))
        if d == "d8":
            vals += args.modelo
        if vals:
            explicitas[d] = vals

    con = v3.connect(args.db)
    res = ejecutar(con, args.brief, explicitas, args.presupuesto, args.aplicar_sugeridas,
                   registrar=not args.sin_registrar)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(render_md(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
