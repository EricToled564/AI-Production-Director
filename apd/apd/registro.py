"""Registro vigente de reglas: construcción, importación, validación y carga.

Una REGLA es una fila de la tabla `reglas`. Las filas de `regla_caso`,
`regla_tarea`, `regla_faceta`, `auditorias`, `embeddings` o `brief_regla` son
RELACIONES o evidencia sobre una regla: nunca se cuentan como reglas y nunca
deciden por sí solas si una regla aplica.
"""

from __future__ import annotations

import json
import re
import sqlite3
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

from . import fuentes as F

TABLAS_REQUERIDAS = {
    "reglas": {"id", "skill", "archivo", "linea", "texto"},
    "casos": {"codigo", "descripcion"},
    "regla_caso": {"regla_id", "caso", "origen"},
}
TABLAS_RELACION = ["regla_caso", "regla_tarea", "regla_faceta", "auditorias",
                   "importacion_huerfana", "embeddings", "brief_regla", "prompt_regla"]
ID_RE = re.compile(r"^[0-9a-f]{12}$")
CONTEO_DECLARADO = 1398


def construir(db: Path = F.RULES_DB, forzar: bool = False) -> dict:
    """Reconstruye rules.sqlite con el constructor ORIGINAL (rules_v3.py build + derive)."""
    if db.exists() and not forzar:
        return {"db": str(db), "construida": False}
    db.parent.mkdir(parents=True, exist_ok=True)
    if db.exists():
        db.unlink()
    env = F.env_constructor()
    log = []
    for paso in ("build", "derive"):
        r = subprocess.run([sys.executable, str(F.HOOKS / "rules_v3.py"), "--db", str(db), paso],
                           capture_output=True, text=True, env=env, cwd=str(F.REPO), timeout=600)
        log.append({"paso": paso, "exit": r.returncode, "salida": r.stdout[-4000:], "error": r.stderr[-2000:]})
        if r.returncode != 0:
            raise RuntimeError(f"rules_v3.py {paso} falló: {r.stderr[-800:]}")
    return {"db": str(db), "construida": True, "log": log,
            "script": ".claude/hooks/rules_v3.py",
            "script_sha256": F.sha256_file(F.HOOKS / "rules_v3.py"),
            "skills_root": str(F.skills_root())}


def validar(db: Path, esperado: int | None = CONTEO_DECLARADO) -> dict:
    """Comprueba esquema y conteos reales. Separa reglas de relaciones."""
    rep: dict = {"db": str(db), "errores": [], "avisos": []}
    if not Path(db).is_file():
        rep["errores"].append("no existe el archivo")
        return rep
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        tablas = {r[0] for r in con.execute("select name from sqlite_master where type in ('table','view')")}
        rep["tablas"] = sorted(tablas)
        for t, cols in TABLAS_REQUERIDAS.items():
            if t not in tablas:
                rep["errores"].append(f"falta la tabla {t}")
                continue
            tiene = {r[1] for r in con.execute(f"pragma table_info({t})")}
            falta = cols - tiene
            if falta:
                rep["errores"].append(f"a {t} le faltan columnas {sorted(falta)}")
        if rep["errores"]:
            return rep
        ids = [r[0] for r in con.execute("select id from reglas")]
        rep["reglas_filas"] = len(ids)
        rep["reglas_ids_distintos"] = len(set(ids))
        malos = [i for i in ids if not ID_RE.match(str(i))]
        if malos:
            rep["errores"].append(f"{len(malos)} ids con formato inválido (ej. {malos[:3]})")
        if len(ids) != len(set(ids)):
            rep["errores"].append("ids de regla duplicados")
        rel = {}
        idset = set(ids)
        for t in TABLAS_RELACION:
            if t not in tablas:
                continue
            cols = {r[1] for r in con.execute(f"pragma table_info({t})")}
            n = con.execute(f"select count(*) from {t}").fetchone()[0]
            info = {"filas": n}
            if "regla_id" in cols and t != "importacion_huerfana":
                info["reglas_distintas"] = con.execute(f"select count(distinct regla_id) from {t}").fetchone()[0]
                huer = [r[0] for r in con.execute(f"select distinct regla_id from {t}") if r[0] not in idset]
                info["ids_que_no_son_regla"] = len(huer)
                if huer:
                    rep["avisos"].append(f"{t}: {len(huer)} ids no están en reglas")
            rel[t] = info
        rep["relaciones"] = rel
        if "regla_caso" in tablas:
            rep["por_origen_caso"] = dict(con.execute("select origen,count(*) from regla_caso group by 1").fetchall())
            rep["reglas_sin_caso_distinto_de_NINGUNO"] = con.execute(
                "select count(*) from reglas r where not exists (select 1 from regla_caso c "
                "where c.regla_id=r.id and c.caso!='NINGUNO')").fetchone()[0]
        if esperado is not None and len(set(ids)) != esperado:
            rep["errores"].append(f"se esperaban {esperado} ids de regla y hay {len(set(ids))}")
        rep["version"] = version_de(con)
    finally:
        con.close()
    rep["ok"] = not rep["errores"]
    return rep


def version_de(con: sqlite3.Connection) -> str:
    filas = [tuple(r) for r in con.execute("select id, skill, archivo, texto from reglas order by id")]
    h = F.sha256_text(F.canon_json(filas))
    return f"R{len(filas)}-{h[:12]}"


@dataclass
class Registro:
    version: str
    reglas: dict[str, dict]
    casos: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    tareas: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    facetas: dict[str, dict[str, list[tuple[str, str]]]] = field(default_factory=dict)
    cat_casos: dict[str, str] = field(default_factory=dict)
    cat_tareas: dict[str, dict] = field(default_factory=dict)
    cat_facetas: dict[str, dict[str, str]] = field(default_factory=dict)
    archivos: dict[str, str] = field(default_factory=dict)
    db: str = ""

    @property
    def ids(self) -> list[str]:
        return sorted(self.reglas)

    def ficha(self, rid: str) -> dict:
        r = dict(self.reglas[rid])
        r["casos"] = [{"caso": c, "origen": o} for c, o in self.casos.get(rid, [])]
        r["tareas"] = [{"tarea": t, "origen": o} for t, o in self.tareas.get(rid, [])]
        r["facetas"] = {d: [{"valor": v, "origen": o} for v, o in vs] for d, vs in self.facetas.get(rid, {}).items()}
        return r


def cargar(db: Path = F.RULES_DB) -> Registro:
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        cols = [r[1] for r in con.execute("pragma table_info(reglas)")]
        quitar = {"texto_emb", "extraido"}
        reglas = {}
        for row in con.execute("select * from reglas"):
            d = {k: row[k] for k in cols if k not in quitar}
            reglas[d["id"]] = d
        reg = Registro(version=version_de(con), reglas=reglas, db=str(db))
        for rid, caso, origen in con.execute("select regla_id, caso, origen from regla_caso order by regla_id, caso"):
            reg.casos.setdefault(rid, []).append((caso, origen))
        tablas = {r[0] for r in con.execute("select name from sqlite_master where type='table'")}
        if "regla_tarea" in tablas:
            for rid, t, o in con.execute("select regla_id, tarea, origen from regla_tarea order by regla_id, tarea"):
                reg.tareas.setdefault(rid, []).append((t, o))
        if "regla_faceta" in tablas:
            for rid, d, v, o in con.execute("select regla_id, dimension, valor, origen from regla_faceta order by 1,2,3"):
                reg.facetas.setdefault(rid, {}).setdefault(d, []).append((v, o))
        reg.cat_casos = dict(con.execute("select codigo, descripcion from casos"))
        if "tareas" in tablas:
            for row in con.execute("select * from tareas"):
                reg.cat_tareas[row["codigo"]] = {k: row[k] for k in row.keys() if k != "texto_emb"}
        if "facetas_catalogo" in tablas:
            for d, v, desc in con.execute("select dimension, valor, descripcion from facetas_catalogo"):
                reg.cat_facetas.setdefault(d, {})[v] = desc
        if "archivos" in tablas:
            for sk, ruta, sha in con.execute("select skill, ruta, sha256 from archivos"):
                reg.archivos[f"{sk}/{ruta}"] = sha
        return reg
    finally:
        con.close()


# --------------------------------------------------------------------------- reconciliación 852

def reglas_ejecutor(html: Path = F.REPO / "app" / "ejecutor.html") -> dict:
    """Extrae el bloque de datos embebido del ejecutor anterior (const D = {...})."""
    h = html.read_text(encoding="utf-8")
    m = re.search(r"const D\s*=\s*(\{.*?\});\n", h, re.S)
    if not m:
        raise ValueError("no se encontró const D en el ejecutor")
    return json.loads(m.group(1))


def reconciliar(reg: Registro) -> dict:
    """Explica por qué el ejecutor embebe 852 reglas y el registro tiene 1,398."""
    D = reglas_ejecutor()
    emb = set(D["idx"])
    reg_ids = set(reg.reglas)
    ambos = emb & reg_ids
    solo_emb = sorted(emb - reg_ids)
    solo_reg = sorted(reg_ids - emb)
    motivo = {}
    for rid in solo_reg:
        r = reg.reglas[rid]
        casos = [c for c, _ in reg.casos.get(rid, [])]
        if r["skill"] == "regimenes":
            m = "regimenes: familias de régimen físico añadidas en v3 (2026-09-25), posteriores al ejecutor"
        elif r["skill"] == "aurora-prompt-linter":
            m = "aurora-prompt-linter: skill incorporado a la base en v3"
        elif not casos or set(casos) <= {"NINGUNO"}:
            m = "sin caso de producción (NINGUNO o sin clasificar): build_app.py las descarta"
        else:
            m = ("regla del registro v3 que el ejecutor no tenía: el ejecutor sólo embebe las reglas "
                 "que tenían caso distinto de NINGUNO en la base v2 (build_app.py:1147)")
        motivo.setdefault(m, []).append(rid)
    return {
        "ejecutor": {"archivo": "app/ejecutor.html", "sha256": F.sha256_file(F.REPO / "app" / "ejecutor.html"),
                     "reglas_embebidas": len(emb), "meta": D.get("meta")},
        "registro": {"version": reg.version, "reglas": len(reg_ids)},
        "en_ambos": len(ambos),
        "solo_en_ejecutor": {"n": len(solo_emb), "ids": solo_emb,
                             "motivo": "id ya no existe en el registro: la redacción de la regla cambió en el skill "
                                       "(el id es sha1(ruta+texto)); quedan en importacion_huerfana"},
        "solo_en_registro": {"n": len(solo_reg), "por_motivo": {k: {"n": len(v), "ids": v} for k, v in motivo.items()}},
        "causa_en_codigo": [
            "app/build_app.py:1142-1147 — las filas de regla_caso con caso NINGUNO se saltan y "
            "`idx` se filtra a las reglas usadas por algún caso: toda regla sin caso de producción "
            "desaparece del ejecutor sin aviso.",
            "app/build_app.py (JS empacarReglas) — al generar, las reglas del caso se cortan por presupuesto "
            "de bytes (`if(usado+b>presupuesto) break`); la nota 'caben X de Y' remite el resto a la auditoría.",
            "app/build_app.py (JS auditoría en tandas) — si una tanda de auditoría falla, se anota y se sigue: "
            "la cobertura de esa tanda se pierde sin bloquear.",
        ],
        "conclusion": (f"{len(ambos)} de las {len(emb)} reglas del ejecutor siguen en el registro; "
                       f"{len(solo_emb)} cambiaron de id; {len(solo_reg)} reglas del registro nunca "
                       "llegaron al ejecutor. La diferencia 1,398 − 852 no son relaciones ni facetas: "
                       "son reglas que el ejecutor filtró o que se añadieron después."),
    }
