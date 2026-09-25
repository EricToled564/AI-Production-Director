#!/usr/bin/env python3
"""Extrae mecánicamente cada enunciado normativo de un skill (o de los regímenes).

Especificado en produccion-visual-sw30/SKILL.md:

    `rule_registry.py` — relee los N archivos del skill y EXTRAE mecánicamente
    cada enunciado normativo. Si el skill cambia, el registro cambia solo.
    Mi interpretación deja de ser etapa.

Ningún modelo decide qué cuenta como regla. Una línea es normativa porque lleva
un marcador deóntico, no porque alguien la recordara. Los marcadores están
declarados abajo y son auditables.

Ids: sha1(ruta relativa + texto normalizado). Una regla conserva su id cuando se
mueven líneas a su alrededor y lo cambia cuando cambia su redacción. El id se
calcula sobre el texto SIN la etiqueta de origen (`[A PRUEBA]`, `[FUENTE: …]`…)
y SIN el prefijo `{d9: low}` de facetas, así canonizar una regla o afinar sus
facetas no cambia su id.

Versión 3 — campos nuevos por regla (compatibles hacia atrás: mismos ids):

    seccion   breadcrumb de encabezados "H1 > H2 > H3"
    idioma    en | es | ru, por heurística léxica
    ambito    PIPELINE | EJEMPLO | HERRAMIENTA | META, derivado de la ruta
    fuerza    PROHIBICION | OBLIGACION | RECOMENDACION | EJEMPLO | ESTRUCTURA
    estado    CANONICA_SKILL para skills; A_PRUEBA | CAMPO | REFUTADA | CANONICA
              para regímenes, según su etiqueta
    fuente    texto de la etiqueta de origen (vacío en skills)
    facetas   dict {d1..d9: [valores]} heredado del frontmatter del archivo de
              régimen y sobrescrito por un prefijo `{d9: low}` en la línea
    facetas_origen  {d?: 'archivo' | 'manual'} — de dónde salió cada faceta

Dos ruidos medidos que ya no entran: las líneas bajo un encabezado "Contents" /
"Contenido" / "Table of contents" (son índice, no reglas) y las filas de
cabecera de tabla (la línea de tabla cuya siguiente línea es el separador
`|---|`). Se cuentan en `descartes`, no desaparecen en silencio.

Raíces: los skills instalados bajo SKILLS_ROOT, más las raíces de régimen:
`<repo>/.claude/rules/regimenes` (skill='regimenes') por defecto y cualquier
`--root DIR` adicional. En una raíz de régimen una línea normativa sin etiqueta
de origen NO entra (README de regímenes, decisión 2) y se cuenta como descarte.

Uso:
    python3 rule_registry.py --skill image --out registry.json --stats
    python3 rule_registry.py --skill regimenes --root tests/fixtures/regimenes --stats
    python3 rule_registry.py --list-skills
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

SKILLS_ROOT = Path(
    os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude" / "skills" / "synced")
)
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
REGIMENES_ROOT = REPO_ROOT / ".claude" / "rules" / "regimenes"
REGIMENES_SKILL = "regimenes"

# Los 13 skills del pipeline visual, en el orden del director §1.
PIPELINE_SKILLS = [
    "ai-production-director", "screenwriter", "video", "image", "ai-video-storyboard",
    "storyboard-architect", "visual-prompt-forge", "visual-asset-critic",
    "brand-lock-extractor", "storyboard-html-preview", "visual-media",
    "produccion-visual-sw30", "aurora-prompt-linter",
]

# Marcadores deónticos. Cada uno es una razón por la que una línea es normativa;
# el marcador queda registrado en la regla para poder discutir la clasificación.
MARKERS: dict[str, re.Pattern] = {
    "prohibition": re.compile(
        r"\b(never|do not|don't|avoid|prohibit(?:ed|s)?|banned|forbidden|"
        r"no se|prohibid[oa]s?|nunca|jam[áa]s|evita[rn]?|"
        r"нельзя|не используй|никогда|запрещ)\w*\b",
        re.IGNORECASE,
    ),
    "obligation": re.compile(
        r"\b(must|shall|always|required|mandatory|ensure|has to|need to|"
        r"siempre|obligatori[oa]s?|se debe|hay que|debe[ns]?|deber[áa]n?|exig[ei]\w*|requiere[n]?|"
        r"должен|обязательн|всегда)\w*\b",
        re.IGNORECASE,
    ),
    "recommendation": re.compile(
        r"\b(should|prefer|recommend(?:ed)?|better to|use\b|"
        r"conviene|se recomienda|"
        r"лучше|используй|рекомендуется)\w*",
        re.IGNORECASE,
    ),
    "good_example": re.compile(r"✅"),
    "bad_example": re.compile(r"❌"),
    "numbered_rule": re.compile(r"^\s{0,3}\d{1,2}[.)]\s+\S"),
}

# Prioridad de marcadores al asignar fuerza (el primero que aparezca gana).
FUERZA_POR_MARCADOR = [
    ("prohibition", "PROHIBICION"),
    ("obligation", "OBLIGACION"),
    ("recommendation", "RECOMENDACION"),
    ("good_example", "EJEMPLO"),
    ("bad_example", "EJEMPLO"),
    ("numbered_rule", "ESTRUCTURA"),
    ("etiqueta", "RECOMENDACION"),   # regla de régimen sin verbo deóntico: se sirve como recomendada
]

# Líneas que son estructura, no reglas.
SKIP = (
    re.compile(r"^\s*$"),
    re.compile(r"^\s*(#{1,6})\s"),          # encabezados
    re.compile(r"^\s*[-*_]{3,}\s*$"),       # hr
    re.compile(r"^\s*\|[\s:|-]+\|\s*$"),    # separadores de tabla
    re.compile(r"^\s*>\s*\*?Author"),       # pies de atribución
    re.compile(r"^\s*\[!\["),               # badges
)

FENCE = re.compile(r"^\s*```")
LIST_START = re.compile(r"^\s*(?:[-*+]\s|\d{1,2}[.)]\s)")
FRONTMATTER = re.compile(r"^---\s*$")
HEADING = re.compile(r"^\s*(#{1,6})\s+(.*?)\s*#*\s*$")
INDICE = re.compile(r"^(contents|contenido|table of contents|[íi]ndice)\b", re.IGNORECASE)
TABLE_SEP = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
# Metadatos del paquete, no enunciados normativos.
META = re.compile(
    r"^\s*(license|name|description|version|author|metadata|pipeline|allowed-tools|"
    r"compatibility)\s*:",
    re.IGNORECASE,
)
ATTRIBUTION = re.compile(r"(CC[ -]BY|attribution required|Serge Shima|t\.me/|©)", re.IGNORECASE)

# Etiqueta de origen (README de regímenes §"Etiquetas de origen"), al final de la línea.
TAG = re.compile(
    r"\s*\[(?P<tag>FUENTE:\s*[^\]]+|A PRUEBA|CAMPO:\s*[^\]]+|REFUTADA:\s*[^\]]+|"
    r"CANONICA(?:\s+\d{4}-\d{2}-\d{2})?)\]\s*$"
)
# Prefijo de facetas al inicio de la línea: {d9: low} o {d8: [kling, veo], d2: B_pico}
FACETAS_PREFIJO = re.compile(r"^\{(?P<cuerpo>[^{}]*)\}\s*")
FACETA_CLAVE = re.compile(r"^d([1-9])(?:_\w+)?$", re.IGNORECASE)

ESTADO_POR_TAG = {
    "FUENTE": "CANONICA_SKILL",   # textual en un skill: hereda la prioridad del skill
    "A PRUEBA": "A_PRUEBA",
    "CAMPO": "CAMPO",
    "REFUTADA": "REFUTADA",
    "CANONICA": "CANONICA",
}

CIRILICO = re.compile(r"[Ѐ-ӿ]")
ES_SENALES = re.compile(
    r"[áéíóúñ¿¡]|\b(de la|del|las|los|una|para|con|que|nunca|siempre|debe|cada|sin|"
    r"pero|porque|cuando|antes|después|sobre|entre|hasta|desde|esto|esta|este|"
    r"prompt de|imagen|regla|reglas|usar|solo|sólo)\b",
    re.IGNORECASE,
)
EN_SENALES = re.compile(
    r"\b(the|and|of|to|is|with|for|not|never|always|must|should|this|that|are|"
    r"from|before|after|when|each|every|only|into|than|then|does|you|your|it|its)\b",
    re.IGNORECASE,
)


# --------------------------------------------------------------------------- utilidades

def normalise(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^[-*+]\s+", "", text)
    text = re.sub(r"^\s*\d{1,2}[.)]\s+", "", text)
    return text.strip(" |")


def rule_id(rel: str, text: str) -> str:
    return hashlib.sha1(f"{rel}\x00{normalise(text).lower()}".encode()).hexdigest()[:12]


def idioma(text: str) -> str:
    """ru si hay cirílico; si no, el que tenga más señales léxicas (empate: en)."""
    if CIRILICO.search(text):
        return "ru"
    es = len(ES_SENALES.findall(text))
    en = len(EN_SENALES.findall(text))
    return "es" if es > en else "en"


def ambito(rel: str) -> str:
    """Derivado de la ruta dentro del skill. Lo que no es pipeline se marca, no se borra."""
    partes = Path(rel).parts
    nombre = partes[-1].lower()
    if "tools" in partes:
        return "META" if nombre in ("readme.md", "license.md", "notice.md") else "HERRAMIENTA"
    if nombre in ("license.md", "notice.md"):
        return "META"
    if "examples" in partes:  # incluye brand-packs/examples/
        return "EJEMPLO"
    return "PIPELINE"


def fuerza(markers: list[str]) -> str:
    for marcador, valor in FUERZA_POR_MARCADOR:
        if marcador in markers:
            return valor
    return "ESTRUCTURA"


def limpiar_encabezado(texto: str) -> str:
    texto = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", texto)  # enlaces
    texto = texto.replace("**", "").replace("`", "").strip()
    return re.sub(r"\s+", " ", texto)


def parse_tag(text: str) -> tuple[str, str, str]:
    """Separa la etiqueta de origen. Devuelve (texto sin etiqueta, estado, fuente)."""
    m = TAG.search(text)
    if not m:
        return text, "", ""
    fuente = m.group("tag").strip()
    clave = fuente.split(":")[0].split(" ")[0].strip()
    if fuente.startswith("A PRUEBA"):
        clave = "A PRUEBA"
    return text[: m.start()].rstrip(), ESTADO_POR_TAG.get(clave, ""), fuente


def normalizar_clave_faceta(clave: str) -> str | None:
    m = FACETA_CLAVE.match(str(clave).strip())
    return f"d{m.group(1)}" if m else None


def normalizar_valores(valor) -> list[str]:
    if valor is None:
        return []
    if isinstance(valor, (list, tuple)):
        return [str(v).strip() for v in valor if str(v).strip()]
    texto = str(valor).strip()
    if texto.startswith("[") and texto.endswith("]"):
        texto = texto[1:-1]
    return [v.strip().strip("'\"") for v in texto.split(",") if v.strip()]


def parse_facetas_texto(cuerpo: str) -> dict[str, list[str]]:
    """Parsea `d9: low, d8: [kling, veo]` sin depender de yaml."""
    facetas: dict[str, list[str]] = {}
    # separa por comas que no estén dentro de corchetes
    partes = re.split(r",(?![^\[]*\])", cuerpo)
    for parte in partes:
        if ":" not in parte:
            continue
        clave, valor = parte.split(":", 1)
        d = normalizar_clave_faceta(clave)
        if d:
            facetas[d] = normalizar_valores(valor)
    return facetas


def parse_prefijo_facetas(text: str) -> tuple[str, dict[str, list[str]]]:
    m = FACETAS_PREFIJO.match(text)
    if not m:
        return text, {}
    facetas = parse_facetas_texto(m.group("cuerpo"))
    if not facetas:
        return text, {}
    return text[m.end():], facetas


def parse_frontmatter(lines: list[str]) -> dict:
    """Frontmatter YAML del archivo. Usa pyyaml si está; si no, clave: valor plano."""
    if not lines or not FRONTMATTER.match(lines[0]):
        return {}
    cuerpo: list[str] = []
    for raw in lines[1:]:
        if FRONTMATTER.match(raw):
            break
        cuerpo.append(raw)
    texto = "\n".join(cuerpo)
    try:
        import yaml  # type: ignore

        datos = yaml.safe_load(texto)
        return datos if isinstance(datos, dict) else {}
    except Exception:
        datos = {}
        for raw in cuerpo:
            if ":" in raw and not raw.startswith((" ", "\t", "-")):
                k, v = raw.split(":", 1)
                datos[k.strip()] = v.strip()
        return datos


def facetas_de_frontmatter(fm: dict) -> dict[str, list[str]]:
    facetas: dict[str, list[str]] = {}
    for clave, valor in fm.items():
        d = normalizar_clave_faceta(clave)
        if d:
            valores = normalizar_valores(valor)
            if valores:
                facetas[d] = valores
    return facetas


# --------------------------------------------------------------------------- extracción

def extract_file(path: Path, root: Path, *, regimen: bool = False,
                 descartes: list[dict] | None = None) -> list[dict]:
    """Extrae las reglas de un .md. `descartes` (opcional) recibe lo excluido y por qué."""
    rel = str(path.relative_to(root))
    rules: list[dict] = []
    in_fence = False
    in_frontmatter = False
    in_indice = False
    pila: list[str] = []  # breadcrumb de encabezados por nivel

    raw_lines = path.read_text(encoding="utf-8").splitlines()
    fm = parse_frontmatter(raw_lines) if regimen else {}
    facetas_archivo = facetas_de_frontmatter(fm)

    def descartar(lineno: int, raw: str, razon: str) -> None:
        if descartes is not None:
            descartes.append({"file": rel, "line": lineno, "razon": razon,
                              "text": normalise(raw)[:200]})

    # Una regla envuelta en varias líneas es UNA regla. Sin esto, la segunda
    # mitad ("de colocación probada; nunca 'a ver si sale'") queda como entrada
    # propia e inclasificable, e infla el conteo.
    lines: list[tuple[int, str]] = []
    for lineno, raw in enumerate(raw_lines, 1):
        continuacion = (
            lines
            and raw.strip()
            and not FENCE.match(raw)
            and not raw.lstrip().startswith(("-", "*", "+", "|", "#", ">"))
            and not re.match(r"^\s*\d{1,2}[.)]\s", raw)
            and (raw.startswith((" ", "\t")) or LIST_START.match(lines[-1][1]))
            and lines[-1][1].strip()
        )
        if continuacion:
            prev_no, prev = lines[-1]
            lines[-1] = (prev_no, prev.rstrip() + " " + raw.strip())
        else:
            lines.append((lineno, raw))

    for idx, (lineno, raw) in enumerate(lines):
        # Frontmatter YAML: metadatos del skill, no reglas.
        if lineno == 1 and FRONTMATTER.match(raw):
            in_frontmatter = True
            continue
        if in_frontmatter:
            if FRONTMATTER.match(raw):
                in_frontmatter = False
            continue

        if FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue  # las plantillas de prompt son ejemplos, no enunciados sobre reglas

        h = HEADING.match(raw)
        if h:
            nivel = len(h.group(1))
            titulo = limpiar_encabezado(h.group(2))
            pila = pila[: nivel - 1] + [""] * max(0, nivel - 1 - len(pila)) + [titulo]
            in_indice = bool(INDICE.match(titulo))
            continue
        if in_indice:
            if any(p.match(raw) for p in SKIP) or len(normalise(raw)) < 12:
                continue
            if any(pat.search(raw) for pat in MARKERS.values()):
                descartar(lineno, raw, "indice")
            continue
        if any(p.match(raw) for p in SKIP):
            continue
        if META.match(raw) or ATTRIBUTION.search(raw):
            continue
        # Fila de cabecera de tabla: la línea siguiente es el separador |---|.
        if raw.lstrip().startswith("|") and idx + 1 < len(lines) and TABLE_SEP.match(lines[idx + 1][1]):
            if any(pat.search(raw) for pat in MARKERS.values()):
                descartar(lineno, raw, "cabecera_tabla")
            continue

        hits = [name for name, pat in MARKERS.items() if pat.search(raw)]
        texto = normalise(raw)
        texto, facetas_linea = parse_prefijo_facetas(texto)
        texto, estado, fuente = parse_tag(texto)
        texto = texto.strip()
        # En un régimen, la etiqueta de origen es en sí un marcador: el README
        # establece que toda regla la lleva, así que una línea etiquetada es
        # normativa por contrato aunque no use un verbo deóntico.
        if regimen and fuente:
            hits.append("etiqueta")
        if not hits:
            continue
        if len(texto) < 12:
            continue
        if regimen and not fuente:
            descartar(lineno, raw, "sin_etiqueta")
            continue
        if not estado:
            estado = "CANONICA_SKILL"

        facetas = {k: list(v) for k, v in facetas_archivo.items()}
        facetas_origen = {k: "archivo" for k in facetas}
        for k, v in facetas_linea.items():
            facetas[k] = v
            facetas_origen[k] = "manual"

        rules.append(
            {
                "id": rule_id(rel, texto),
                "file": rel,
                "line": lineno,
                "markers": hits,
                "text": texto[:400],
                "seccion": " > ".join(p for p in pila if p),
                "idioma": idioma(texto),
                "ambito": ambito(rel),
                "fuerza": fuerza(hits),
                "estado": estado,
                "fuente": fuente,
                "facetas": facetas,
                "facetas_origen": facetas_origen,
            }
        )
    return rules


# --------------------------------------------------------------------------- raíces

def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def skill_roots(skill: str, extra_roots: list[Path] | tuple[Path, ...] = ()) -> list[tuple[Path, bool]]:
    """Raíces (directorio, es_regimen) donde vive un skill. Puede haber varias para regímenes."""
    roots: list[tuple[Path, bool]] = []
    if skill == REGIMENES_SKILL:
        if REGIMENES_ROOT.is_dir():
            roots.append((REGIMENES_ROOT, True))
    else:
        instaladas = sorted(SKILLS_ROOT.glob(f"*/{skill}")) + sorted(SKILLS_ROOT.glob(f"*/*/{skill}"))
        instaladas = [r for r in instaladas if r.is_dir()]
        if instaladas:
            roots.append((instaladas[0], False))
    for extra in extra_roots:
        extra = Path(extra)
        if extra.is_dir() and extra.name == skill and (extra, True) not in roots:
            roots.append((extra, True))
    return roots


def archivos_de(root: Path, regimen: bool) -> list[Path]:
    archivos = sorted(root.rglob("*.md"))
    if regimen:
        # El README de la carpeta documenta la convención; no es un régimen.
        archivos = [p for p in archivos if p.name.lower() != "readme.md"]
    return archivos


def build_v3(skill: str, extra_roots: list[Path] | tuple[Path, ...] = ()) -> dict:
    """Registro completo de un skill: reglas, descartes y hash de cada archivo."""
    roots = skill_roots(skill, extra_roots)
    if not roots:
        if skill == REGIMENES_SKILL or any(Path(e).name == skill for e in extra_roots):
            return {"skill": skill, "root": "", "roots": [], "rules": [], "descartes": [],
                    "archivos": []}
        raise SystemExit(f"rule_registry: skill '{skill}' not found under {SKILLS_ROOT}")

    rules: list[dict] = []
    descartes: list[dict] = []
    archivos: list[dict] = []
    seen: set[str] = set()
    for root, regimen in roots:
        for md in archivos_de(root, regimen):
            antes = len(rules)
            for rule in extract_file(md, root, regimen=regimen, descartes=descartes):
                if rule["id"] in seen:
                    continue
                seen.add(rule["id"])
                rule["skill"] = skill
                rules.append(rule)
            archivos.append({"file": str(md.relative_to(root)), "root": str(root),
                             "sha256": _sha256(md), "reglas": len(rules) - antes})
    return {"skill": skill, "root": str(roots[0][0]), "roots": [str(r) for r, _ in roots],
            "rules": rules, "descartes": descartes, "archivos": archivos}


def build(skill: str, extra_roots: list[Path] | tuple[Path, ...] = ()) -> tuple[Path, list[dict]]:
    """Compatibilidad con la firma anterior: (raíz, reglas)."""
    reg = build_v3(skill, extra_roots)
    return Path(reg["root"]) if reg["root"] else REGIMENES_ROOT, reg["rules"]


def listar_skills(extra_roots: list[Path] | tuple[Path, ...] = ()) -> list[str]:
    nombres: list[str] = []
    for d in sorted(SKILLS_ROOT.glob("*/*")):
        if d.is_dir() and (d / "SKILL.md").is_file():
            nombres.append(d.name)
    if REGIMENES_ROOT.is_dir():
        nombres.append(REGIMENES_SKILL)
    for extra in extra_roots:
        if Path(extra).is_dir():
            nombres.append(Path(extra).name)
    return nombres


# --------------------------------------------------------------------------- cli

def main() -> int:
    ap = argparse.ArgumentParser(description="Extracción mecánica de enunciados normativos")
    ap.add_argument("--skill", default="image")
    ap.add_argument("--out")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--list-skills", action="store_true")
    ap.add_argument("--root", action="append", default=[],
                    help="raíz extra de régimen (repetible); el nombre del directorio es el skill")
    args = ap.parse_args()
    extra_roots = [Path(r) for r in args.root]

    if args.list_skills:
        for nombre in listar_skills(extra_roots):
            print(nombre)
        return 0

    reg = build_v3(args.skill, extra_roots)
    rules = reg["rules"]

    if args.out:
        Path(args.out).write_text(
            json.dumps(
                {"skill": args.skill, "root": reg["root"], "roots": reg["roots"],
                 "count": len(rules), "rules": rules, "descartes": reg["descartes"],
                 "archivos": reg["archivos"]},
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    if args.stats or not args.out:
        files = sorted({r["file"] for r in rules})
        by_marker: dict[str, int] = {}
        for r in rules:
            for m in r["markers"]:
                by_marker[m] = by_marker.get(m, 0) + 1
        conteo = lambda campo: sorted(  # noqa: E731
            {v: sum(1 for r in rules if r[campo] == v) for v in {r[campo] for r in rules}}.items(),
            key=lambda kv: -kv[1])
        print(f"skill:      {args.skill}")
        print(f"root:       {reg['root'] or '(no existe)'}")
        print(f"archivos:   {len(reg['archivos'])} .md leidos, {len(files)} con reglas")
        print(f"enunciados: {len(rules)}")
        print("por marcador:")
        for m, n in sorted(by_marker.items(), key=lambda kv: -kv[1]):
            print(f"  {m:16} {n}")
        for campo in ("fuerza", "ambito", "idioma", "estado"):
            print(f"por {campo}:")
            for v, n in conteo(campo):
                print(f"  {v:16} {n}")
        razones: dict[str, int] = {}
        for d in reg["descartes"]:
            razones[d["razon"]] = razones.get(d["razon"], 0) + 1
        print(f"descartes:  {len(reg['descartes'])}" + (
            "  (" + ", ".join(f"{k} {v}" for k, v in sorted(razones.items())) + ")" if razones else ""))
        if args.out:
            print(f"\nescrito en {args.out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
