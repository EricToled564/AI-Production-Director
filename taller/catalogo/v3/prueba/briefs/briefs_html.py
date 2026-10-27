"""briefs_html.py: escribe LOTE_<n>.html, una versión legible de los briefs del lote para que Eric los abra en la app.

    python3 -I taller/catalogo/v3/prueba/briefs/briefs_html.py 1

Lee los `Kxx.contrato.json` y `Kxx.caso.json` del lote (los mismos que valida `construir_briefs.py`) y presenta cada
campo en español, con su origen y el sha256 que Eric aprueba. No cambia ningún dato.
"""
import hashlib
import html
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
lote = sys.argv[1] if len(sys.argv) > 1 else "1"
md = (AQUI / f"LOTE_{lote}.md").read_text(encoding="utf-8")
ids = re.findall(r"^## (K\d\d)", md, re.M)
PLAN = {c["id"]: c for c in json.loads((AQUI.parent / "casos.json").read_text(encoding="utf-8"))["casos"]}
ETQ = {"espacio": "Espacio", "entorno": "Entorno", "momento": "Momento", "clima": "Clima", "planos": "Planos",
       "plano": "Plano", "angulo": "Ángulo", "altura": "Altura de cámara", "efecto_optico": "Efecto óptico",
       "lente_intencion": "Lente", "fuente": "Fuente", "direccion": "Dirección", "dureza": "Dureza",
       "distribucion": "Distribución", "contraste": "Contraste", "id": "Id", "clase": "Clase",
       "descripcion": "Descripción", "edad": "Edad", "genero": "Género", "rasgos": "Rasgos", "cabello": "Cabello",
       "vestuario": "Vestuario", "expresion": "Expresión", "posicion": "Posición", "ocupacion": "Ocupación del rostro",
       "detalles": "Detalles", "literales": "Texto literal", "tipografia": "Tipografía", "tipo": "Tipo",
       "estado_visible": "Estado visible", "evidencia_fisica": "Evidencia física", "regimen": "Régimen"}


def e(v):
    return html.escape(str(v))


def valor(v):
    if isinstance(v, list):
        return "; ".join(valor(x) for x in v)
    if isinstance(v, dict):
        return "<br>".join(f"<b>{e(ETQ.get(k, k))}:</b> {valor(x)}" for k, x in v.items())
    return e(v)


def filas(d):
    return "".join(f"<tr><th>{e(ETQ.get(k, k))}</th><td>{valor(v)}</td></tr>" for k, v in d.items())


partes = []
for kid in ids:
    x = json.loads((AQUI / f"{kid}.contrato.json").read_text(encoding="utf-8"))
    c = json.loads((AQUI / f"{kid}.caso.json").read_text(encoding="utf-8"))
    en, p = x["entrada"], PLAN[kid]
    digest = hashlib.sha256(json.dumps(en, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    facetas = " · ".join(f"<b>{f}</b> {e(p[f])}" for f in ("F10", "F15", "F32", "F04", "F11", "F13", "F14") if p[f])
    s = [f"<section><h2>{kid} · {e(p['descripcion'])}</h2>", f"<p class='brief'>{e(c['brief_literal'])}</p>",
         f"<p class='fac'>Lista aprobada (26 §16): {facetas}</p>",
         "<table>",
         f"<tr><th>Formato</th><td>{e(en['formato']['ratio'])} · referencia {en['formato']['ancho_px']}x"
         f"{en['formato']['alto_px']} · quality {e(p['quality'])}</td></tr>",
         f"<tr><th>Pieza</th><td>{valor(en['pieza'])}</td></tr></table>",
         "<h3>Propuesto por el sistema, para su aprobación</h3>"]
    if en["sujetos"]["items"]:
        for it in en["sujetos"]["items"]:
            s.append(f"<h4>Sujeto: {e(it['id'])}</h4><table>{filas(it)}</table>")
    s.append(f"<h4>Escena</h4><table>{filas(en['escena'])}</table>")
    s.append(f"<h4>Cámara</h4><table>{filas(en['camara'])}</table>")
    s.append(f"<h4>Luz</h4><table>{filas(en['luz'])}</table>")
    for k, t in (("accion", "Acción"), ("fisica", "Física"), ("rostro", "Rostro"), ("texto_marca", "Texto en la imagen")):
        if k in en:
            s.append(f"<h4>{t}</h4><table>{filas(en[k])}</table>")
    s.append(f"<h4>Estilo y restricciones</h4><table><tr><th>Estilo</th><td>{valor(en['estilo'])}</td></tr>"
             f"<tr><th>Restricciones</th><td>{valor(en['restricciones'])}</td></tr>"
             f"<tr><th>Módulos activos</th><td>{valor(en['modulos_activos'])}</td></tr></table>")
    s.append(f"<p class='sha'>sha256 del brief: <code>{digest}</code></p></section>")
    partes.append("\n".join(s))

doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Briefs lote {lote}</title>
<style>
:root{{--bg:#ffffff;--fg:#1d1d1f;--mut:#5f6368;--line:#dadce0;--acc:#0b57d0;--card:#f8f9fa}}
@media (prefers-color-scheme: dark){{:root{{--bg:#16181b;--fg:#e8eaed;--mut:#9aa0a6;--line:#3c4043;--acc:#8ab4f8;--card:#202327}}}}
body{{background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif;margin:0;padding:16px;max-width:860px;margin-inline:auto}}
h1{{font-size:22px}} h2{{font-size:19px;margin:0 0 8px;color:var(--acc)}} h3{{font-size:15px;margin:14px 0 4px}} h4{{font-size:14px;margin:10px 0 4px;color:var(--mut)}}
section{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;margin:16px 0}}
table{{border-collapse:collapse;width:100%}} th,td{{border-top:1px solid var(--line);padding:5px 6px;text-align:left;vertical-align:top}}
th{{width:30%;color:var(--mut);font-weight:600}} .brief{{font-size:15px}} .fac{{color:var(--mut);font-size:13px}}
code{{font-size:12px;word-break:break-all}} .sha{{margin-top:10px}}
</style></head><body>
<h1>Lote {lote} de briefs ({ids[0]}–{ids[-1]})</h1>
<p>Cada caso se aprueba por su sha256. Lo que no viene de la lista de casos aprobada (26 §16) es propuesta del sistema:
usted aprueba, cambia o quita. Personas, lugares y objetos son inventados, salvo los sujetos reales de K03, K04 y K07,
que se verifican contra fotos reales.</p>
{''.join(partes)}
</body></html>"""
(AQUI / f"LOTE_{lote}.html").write_text(doc, encoding="utf-8")
print(f"LOTE_{lote}.html: {len(ids)} casos")
