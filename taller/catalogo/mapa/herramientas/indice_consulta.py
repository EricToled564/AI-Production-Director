"""indice_consulta.py: escribe ../CONSULTA.md, el índice que el agente consulta antes de preguntar a Eric o de afirmar
que algo no existe.

    python3 -I indice_consulta.py      (desde taller/catalogo/mapa/herramientas)

Todo lo que no es la guía de la sección 1 se genera mecánicamente desde los archivos, con su ruta y su línea:
  2. cada decisión e instrucción de Eric (texto literal de su primera línea, recortado);
  3. cada documento del corpus → dónde está su explicación verificada y su utilidad;
  4. cada archivo versionado del repo, por carpeta.
"""
import json
import re
import subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MAPA = AQUI.parent
REPO = MAPA.parents[2]


def rel(p):
    return str(Path(p).resolve().relative_to(REPO))


def corta(s, n=170):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


GUIA = """# Consulta rápida del agente

Se consulta **antes** de preguntarle algo a Eric y **antes** de decir que algo falta, no existe o no está decidido.
Si la respuesta está aquí o en el archivo que señala, no se pregunta: se lee y se cita. Este índice se regenera con
`herramientas/indice_consulta.py` cada vez que cambia una decisión, un archivo del repo o una explicación.

## 1. Dónde está cada cosa

| Duda | Dónde mirar |
|---|---|
| Instrucciones de trabajo vigentes | `CLAUDE.md` (sección 2 de este índice) |
| ¿Eric ya decidió esto? | Sección 2 de este índice: todas las decisiones con archivo y línea. Orden de autoridad: decisiones de Eric → taxonomía 00688 → C18 base → textos del corpus → PLAN_V5, TEMPLATES y CASOS (capítulo 3 §3.1) |
| Pendientes abiertos y quién los resuelve; qué etapa sigue | `taller/catalogo/PENDIENTES.md` |
| Diseño de la aplicación y del procedimiento de clasificación (propuesta del 2026-10-29) | `taller/catalogo/DISENO_APLICACION_Y_CLASIFICACION.md` |
| Objetivo del sistema | PLAN_V5 L29 (capítulo 3 §3.4): aplicación que extrae exhaustivamente las reglas aplicables a un tipo y caso de imagen y las convierte en prompts de apariencia fotográfica al primer intento. El sistema genera prompts; Eric genera las imágenes |
| Qué contiene un documento del corpus | Sección 3 de este índice → su explicación verificada. La explicación orienta; lo que vale es el texto original de la base |
| Texto original de una regla | Base `taller/catalogo/corpus/BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite`, tabla `textos`, por `id` (INV-xxxxxx). Fiel al original: los 206 archivos coinciden por sha256 y los textos coinciden con sus líneas, salvo los HTML, que son el texto visible sin etiquetas (sus números de línea no son líneas del HTML crudo) |
| Taxonomía: bloques, facetas, valores y términos | `fuentes_20261019/00688_…md`; explicada en el capítulo 7 y detallada en el 8 |
| Etapas y flujos | Capítulo 6; taxonomía §2 |
| Matriz de casos | Capítulo 11; `fuentes_20261019/CASOS_OPCIONES_TAXONOMIA_20261019/casos/` |
| Brief, contratos y adaptadores por modelo | Capítulo 12; `fuentes_20261019/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates/` |
| Universalidad | Capítulo 10 |
| Contradicciones del corpus ya resueltas o pendientes | Capítulo 14 §14.3 |
| Prompt de retrato para GPT Image 2 | `produccion/template-retrato-gpt2/` con `armar.py` (CLAUDE.md) |
| Algo borrado del repo | `git checkout 77678d8 -- <ruta>`; qué se borró, en el capítulo 1 §1.4 |
| Estructura del repo | Sección 4 de este índice |
"""


def decisiones():
    o = ["\n## 2. Decisiones e instrucciones de Eric (literal, con archivo y línea)\n"]
    fuentes = [REPO / "CLAUDE.md", REPO / ".claude/rules/DECISIONES.md"] + sorted(
        (REPO / "taller/catalogo/v2/decisiones").glob("*.md"))
    for f in fuentes:
        if f.name.startswith("TEMPLATES_REVISADOS"):
            continue
        lineas = f.read_text(encoding="utf-8").splitlines()
        o.append(f"\n### `{rel(f)}`\n")
        for i, l in enumerate(lineas, 1):
            if re.match(r"^#{2,4} ", l):
                sig = next((x for x in lineas[i:i + 4] if x.strip() and not x.startswith("#")), "")
                o.append(f"- L{i} **{corta(l.lstrip('# '), 90)}** — {corta(sig)}")
            elif re.match(r"^\d+\. ", l) or re.match(r"^\| \d+ \|", l) or re.match(r"^- \*\*", l):
                o.append(f"- L{i} {corta(l)}")
    for f in sorted((REPO / "taller/catalogo/fuentes_eric_20261021").glob("*directiv*.json")):
        o.append(f"\n### `{rel(f)}`\n")
        for d in json.loads(f.read_text(encoding="utf-8")):
            o.append(f"- `{d['constraint_id']}`: «{corta(d['literal'])}»")
    return o


def documentos():
    o = ["\n## 3. Documentos del corpus → explicación verificada\n",
         "| Documento | Explicación | Utilidad |", "|---|---|---|"]
    for lote in sorted((MAPA / "documentos/verificado").glob("lote*.md")):
        lineas = lote.read_text(encoding="utf-8").splitlines()
        doc = None
        for i, l in enumerate(lineas, 1):
            m = re.match(r"## (\S+)", l)
            if m:
                doc, ini = m.group(1).strip("`"), i
            mu = re.search(r"\*\*Utilidad para el sistema de prompts\.\*\*\s*\**(ALTA|MEDIA|NULA)", l)
            if mu and doc:
                o.append(f"| `{doc}` | `{rel(lote)}` L{ini} | {mu.group(1)} |")
                doc = None
    o.append("\nLas 65 copias idénticas remiten al original: capítulo 5 §5.2.")
    return o


def repo():
    archivos = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True, text=True, check=True).stdout.split()
    o = [f"\n## 4. Archivos versionados del repo ({len(archivos)})\n"]
    carpeta = None
    for a in archivos:
        c = str(Path(a).parent)
        if c != carpeta:
            o.append(f"\n**`{c}/`**\n")
            carpeta = c
        o.append(f"- `{Path(a).name}`")
    return o


texto = "\n".join([GUIA] + decisiones() + documentos() + repo()) + "\n"
(MAPA / "CONSULTA.md").write_text(texto, encoding="utf-8")
print(f"CONSULTA.md: {texto.count(chr(10))} líneas")
