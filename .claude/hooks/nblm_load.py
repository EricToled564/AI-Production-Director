#!/usr/bin/env python3
"""Carga toda la documentación de los skills a NotebookLM y corre la prueba.

Un comando. Hace, en orden:

  1. get_health          — si no hay auth, dice exactamente qué falta y para.
  2. add_notebook        — registra el notebook destino.
  3. add_source × N      — sube las 12 fuentes de notebooklm-corpus/.
  4. ask_question        — hace la pregunta de clasificación del caso.
  5. rule_answer_check   — mide si la respuesta cubrió TODAS las reglas.

El paso 5 es lo que convierte "fue exhaustivo" en un número.

Uso:
    python3 nblm_load.py --corpus notebooklm-corpus --url <URL del notebook>
    python3 nblm_load.py --corpus notebooklm-corpus --url <URL> --caso "T1 rostro, Nano Banana Pro"
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nblm_client import Client  # noqa: E402


def unwrap(resp: dict) -> dict:
    if "error" in resp:
        return {"success": False, "error": resp["error"]}
    blocks = (resp.get("result") or {}).get("content", [])
    for b in blocks:
        text = b.get("text", "")
        try:
            return json.loads(text)
        except Exception:
            continue
    return {"success": True, "raw": blocks}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default="notebooklm-corpus")
    ap.add_argument("--url", help="URL del notebook de NotebookLM")
    ap.add_argument("--notebook-id", default="fupai-pipeline")
    ap.add_argument("--caso", default="maestro de rostro T1, Nano Banana Pro")
    ap.add_argument("--pregunta", help="archivo con la pregunta; si no, se arma sola")
    ap.add_argument("--respuesta", default="respuesta.txt")
    ap.add_argument("--timeout", type=float, default=600.0)
    a = ap.parse_args()

    corpus = sorted(Path(a.corpus).glob("*.md"))
    if not corpus:
        print(f"nblm_load: no hay .md en {a.corpus}/. Corre primero el generador de corpus.",
              file=sys.stderr)
        return 2

    total_words = sum(len(p.read_text(encoding="utf-8").split()) for p in corpus)
    print(f"corpus: {len(corpus)} fuentes · {total_words:,} palabras")

    c = Client(timeout=a.timeout)
    try:
        c.initialize()

        health = unwrap(c.call("get_health", {}))
        if not (health.get("data") or {}).get("authenticated"):
            print()
            print("=" * 66)
            print("  FALTA AUTENTICACION DE GOOGLE — no se puede continuar.")
            print("=" * 66)
            print("  El servidor corre y las 20 tools responden, pero NotebookLM no")
            print("  tiene API publica: el login abre una ventana de Chrome y pide")
            print("  las credenciales de tu cuenta de Google. Eso lo tienes que")
            print("  hacer tu una vez; despues el perfil de Chrome queda guardado y")
            print("  este comando ya no lo vuelve a pedir.")
            print()
            print("  En tu maquina, una sola vez:")
            print("     npx -y notebooklm-mcp@latest   # y completa el login")
            print()
            print("  Despues vuelve a correr este comando.")
            print("=" * 66)
            return 1

        if a.url:
            r = unwrap(c.call("add_notebook", {
                "id": a.notebook_id,
                "name": "FUPAI — pipeline de produccion visual",
                "url": a.url,
                "description": "Documentacion completa de los 12 skills del pipeline.",
            }))
            print(f"notebook: {'ok' if r.get('success') else r.get('error')}")
            c.call("select_notebook", {"id": a.notebook_id})

        subidas, fallidas = 0, []
        for p in corpus:
            r = unwrap(c.call("add_source", {
                "type": "text",
                "content": p.read_text(encoding="utf-8"),
                "title": p.stem,
            }))
            if r.get("success"):
                subidas += 1
                print(f"  + {p.stem}")
            else:
                fallidas.append((p.stem, r.get("error")))
                print(f"  ! {p.stem}: {r.get('error')}")
        print(f"fuentes subidas: {subidas}/{len(corpus)}")
        if fallidas:
            print("  no se subieron:", ", ".join(n for n, _ in fallidas))

        if a.pregunta:
            pregunta = Path(a.pregunta).read_text(encoding="utf-8")
        else:
            pregunta = (
                f"CASO: {a.caso}\n\n"
                "De TODAS las reglas contenidas en las fuentes de este notebook, "
                "dime cuales aplican a este caso y cuales no.\n"
                "Una linea por regla, citando el archivo y la regla textual.\n"
                "No resumas ni agrupes: necesito la lista completa, no una seleccion "
                "de las mas relevantes."
            )

        print("\npreguntando…")
        r = unwrap(c.call("ask_question", {"question": pregunta}))
        answer = (r.get("data") or {}).get("answer") or r.get("answer") or ""
        if not answer:
            print(f"sin respuesta: {r.get('error') or r}", file=sys.stderr)
            return 1
        Path(a.respuesta).write_text(answer, encoding="utf-8")
        print(f"respuesta escrita en {a.respuesta} ({len(answer)} chars)")
        print("\nMide la cobertura con:")
        print(f"  python3 .claude/hooks/rule_answer_check.py --registry reg_*.json "
              f"--respuesta {a.respuesta}")
        return 0
    finally:
        c.close()


if __name__ == "__main__":
    sys.exit(main())
