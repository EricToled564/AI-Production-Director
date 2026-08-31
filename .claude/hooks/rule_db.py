#!/usr/bin/env python3
"""Base de datos de reglas por caso. Se construye una vez, se consulta siempre.

El problema de preguntar "qué reglas aplican a este caso" en cada prompt es que
la respuesta cabe mal en un solo output y hay que confiar en que fue completa.
Esto lo invierte: se clasifica en tandas chicas, una vez, y queda una tabla.
Después seleccionar reglas es una consulta, no una pregunta a un modelo.

    --chunks    parte el registro en tandas del tamaño que aguante el output,
                cada una con su pregunta lista para pegar.
    --ingest    lee la respuesta de una tanda y la mete en la base. Reporta qué
                ids de esa tanda no vinieron, para volver a pedirlos.
    --status    cuántas reglas ya tienen casos y cuántas faltan.
    --caso      consulta: qué reglas aplican a un caso dado.

La base es un JSON legible: cada regla con su texto, su archivo y sus casos.
Se puede leer, discutir y corregir a mano.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Taxonomía de casos. T1..T5 son de produccion-visual-sw30/SKILL.md; los demás
# cubren el resto del pipeline. Es una lista cerrada a propósito: un caso nuevo
# se agrega aquí y se reclasifica, no se inventa al vuelo.
CASOS = {
    "T1": "maestro de rostro (still, persona, identidad)",
    "T2": "maestro de cuerpo (still, persona completa)",
    "T3": "cuadro con 1 persona (still de escena)",
    "T4": "cuadro con 2 personas (still, contacto/interaccion)",
    "T5": "edicion quirurgica sobre imagen existente",
    "CLIP": "prompt de video / movimiento",
    "SHOT": "planeacion de shots, storyboard, shots.json",
    "GUION": "escritura de guion o tratamiento",
    "MARCA": "extraccion o uso de brand-lock",
    "QA": "critica de render, revision de asset generado",
    "ENTREGA": "empaquetado, preview, entrega a cliente",
    "NINGUNO": "no aplica a ningun caso de produccion (meta, ejemplos, docs)",
}

LINE_RE = re.compile(
    r"\[?(?P<id>[0-9a-f]{12})\]?\s*[-—:]?\s*(?P<casos>[A-Z0-9,\s]+?)\s*$",
    re.MULTILINE,
)


def load_registry(paths: list[str]) -> dict[str, dict]:
    rules: dict[str, dict] = {}
    for p in paths:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        skill = data.get("skill", "?")
        for r in data.get("rules", []):
            r["skill"] = skill
            rules.setdefault(r["id"], r)
    return rules


def load_db(path: Path) -> dict:
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"casos": CASOS, "reglas": {}}


def save_db(path: Path, db: dict) -> None:
    path.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


def preamble(n: int, chunk: int, total: int) -> str:
    casos = "\n".join(f"  {k:8} {v}" for k, v in CASOS.items())
    return f"""TANDA {chunk} de {total} — {n} reglas.

Abajo hay {n} reglas de mi pipeline de produccion visual. Cada una tiene un id
de 12 caracteres entre corchetes.

Para CADA regla, dime a que casos de produccion es relevante. Los casos son
estos y solo estos:

{casos}

Formato exacto, una linea por regla, sin texto adicional:

  [id] T1,T3,T4
  [id] CLIP
  [id] NINGUNO

Reglas del formato:
- Deben aparecer los {n} ids de esta tanda. Ninguno puede faltar.
- Una regla puede tener varios casos separados por coma, sin espacios.
- Si una regla es general y aplica a todo still, marca T1,T2,T3,T4,T5.
- NINGUNO es solo para lineas que no son reglas de produccion (ejemplos,
  indices, notas de licencia, descripciones de archivos).
- No expliques. Solo la lista.
"""


def cmd_chunks(args) -> int:
    rules = load_registry(args.registry)
    db = load_db(Path(args.db))
    pendientes = [r for rid, r in rules.items() if rid not in db["reglas"]]
    pendientes.sort(key=lambda r: (r["skill"], r["file"], r["line"]))

    if not pendientes:
        print("no quedan reglas sin clasificar")
        return 0

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for f in out.glob("tanda-*.txt"):
        f.unlink()

    total = (len(pendientes) + args.size - 1) // args.size
    for i in range(total):
        grupo = pendientes[i * args.size : (i + 1) * args.size]
        cuerpo = [preamble(len(grupo), i + 1, total), ""]
        actual = None
        for r in grupo:
            ruta = f"{r['skill']}/{r['file']}"
            if ruta != actual:
                actual = ruta
                cuerpo.append(f"\n--- {ruta} ---")
            cuerpo.append(f"[{r['id']}] {r['text']}")
        (out / f"tanda-{i + 1:02d}.txt").write_text("\n".join(cuerpo), encoding="utf-8")

    print(f"{len(pendientes)} reglas sin clasificar -> {total} tandas de {args.size} en {out}/")
    return 0


def cmd_ingest(args) -> int:
    rules = load_registry(args.registry)
    db_path = Path(args.db)
    db = load_db(db_path)

    texto = Path(args.respuesta).read_text(encoding="utf-8")
    esperados = set()
    if args.tanda:
        for m in re.finditer(r"\[([0-9a-f]{12})\]", Path(args.tanda).read_text(encoding="utf-8")):
            esperados.add(m.group(1))

    nuevos, invalidos, desconocidos = 0, [], []
    vistos = set()
    for m in LINE_RE.finditer(texto):
        rid = m.group("id")
        casos = [c.strip().upper() for c in m.group("casos").split(",") if c.strip()]
        casos = [c for c in casos if c]
        if rid not in rules:
            desconocidos.append(rid)
            continue
        malos = [c for c in casos if c not in CASOS]
        if malos or not casos:
            invalidos.append((rid, ",".join(casos) or "(vacio)"))
            continue
        vistos.add(rid)
        r = rules[rid]
        db["reglas"][rid] = {
            "skill": r["skill"], "file": r["file"], "line": r["line"],
            "texto": r["text"], "casos": sorted(set(casos)),
        }
        nuevos += 1

    save_db(db_path, db)

    faltantes = sorted(esperados - vistos) if esperados else []
    print(f"clasificadas en esta tanda : {nuevos}")
    print(f"ids que no existen         : {len(desconocidos)}")
    print(f"lineas con caso invalido   : {len(invalidos)}")
    if esperados:
        print(f"ids de la tanda que faltan : {len(faltantes)}")
    print(f"total en la base           : {len(db['reglas'])} / {len(rules)}")
    for rid, casos in invalidos[:5]:
        print(f"   invalido {rid}: {casos}")
    if faltantes:
        print("\n  Vuelve a pedir estos ids:")
        for rid in faltantes[:20]:
            print(f"    [{rid}] {rules[rid]['skill']}/{rules[rid]['file']}:{rules[rid]['line']}")
        if len(faltantes) > 20:
            print(f"    … y {len(faltantes) - 20} mas")
    return 1 if (faltantes or invalidos or desconocidos) else 0


def cmd_status(args) -> int:
    rules = load_registry(args.registry)
    db = load_db(Path(args.db))
    hechas = set(db["reglas"])
    print(f"reglas en el registro : {len(rules)}")
    print(f"clasificadas          : {len(hechas)}  ({len(hechas)/max(len(rules),1)*100:.1f}%)")
    print(f"pendientes            : {len(rules) - len(hechas)}")
    print()
    por_skill: dict[str, list[int]] = {}
    for rid, r in rules.items():
        s = por_skill.setdefault(r["skill"], [0, 0])
        s[1] += 1
        if rid in hechas:
            s[0] += 1
    for skill, (hecho, tot) in sorted(por_skill.items(), key=lambda kv: kv[1][1] - kv[1][0], reverse=True):
        barra = "#" * int(hecho / max(tot, 1) * 20)
        print(f"  {skill:26} {hecho:>4}/{tot:<4} {barra}")
    if hechas:
        print("\n  reglas por caso:")
        conteo: dict[str, int] = {}
        for r in db["reglas"].values():
            for c in r["casos"]:
                conteo[c] = conteo.get(c, 0) + 1
        for c in CASOS:
            if conteo.get(c):
                print(f"    {c:8} {conteo[c]:>4}   {CASOS[c]}")
    return 0


def cmd_caso(args) -> int:
    db = load_db(Path(args.db))
    if args.caso not in CASOS:
        print(f"caso desconocido. Hay: {', '.join(CASOS)}", file=sys.stderr)
        return 2
    sel = [r for r in db["reglas"].values() if args.caso in r["casos"]]
    sel.sort(key=lambda r: (r["skill"], r["file"], r["line"]))
    print(f"# Reglas para el caso {args.caso} — {CASOS[args.caso]}")
    print(f"# {len(sel)} reglas, de {len(db['reglas'])} clasificadas\n")
    actual = None
    for r in sel:
        ruta = f"{r['skill']}/{r['file']}"
        if ruta != actual:
            actual = ruta
            print(f"\n## {ruta}")
        print(f"- {r['texto']}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Base de datos de reglas por caso")
    ap.add_argument("--registry", nargs="+", required=True)
    ap.add_argument("--db", default="rules.db.json")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("chunks", help="genera las tandas pendientes")
    c.add_argument("--size", type=int, default=50)
    c.add_argument("--out", default="tandas")
    c.set_defaults(fn=cmd_chunks)

    i = sub.add_parser("ingest", help="mete la respuesta de una tanda a la base")
    i.add_argument("--respuesta", required=True)
    i.add_argument("--tanda", help="archivo de la tanda, para detectar ids faltantes")
    i.set_defaults(fn=cmd_ingest)

    s = sub.add_parser("status", help="avance de la clasificacion")
    s.set_defaults(fn=cmd_status)

    q = sub.add_parser("caso", help="consulta las reglas de un caso")
    q.add_argument("caso")
    q.set_defaults(fn=cmd_caso)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
