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
ids = re.findall(r"^## ([KGE]\d+)", md, re.M)
PLAN = {c["id"]: c for c in json.loads((AQUI.parent / "casos.json").read_text(encoding="utf-8"))["casos"]}
# G1 y G2 son del mismo tipo que K01 (PLAN §4, tabla de entradas); su fila sale de construir_briefs_lote2.G_PLAN.
for g, m in (("G1", "B"), ("G2", "C")):
    PLAN[g] = dict(PLAN["K01"], id=g, descripcion=f"rostro maestro T1 del miembro {m} de K12")
# E5 y E6: entradas de K17 y K18; sus facetas son propuesta (construir_briefs_lote4.E_PLAN).
for e_, desc_, caso_ in (("E5", "foto en blanco y negro de una persona", "K17"),
                         ("E6", "foto antigua dañada de una persona", "K18")):
    PLAN[e_] = dict(PLAN["K01"], id=e_, descripcion=desc_, F04="editorial",
                    etiqueta=f"Propuesta del sistema ({e_} es entrada de {caso_}, no caso)")
INTRO = {"1": "Cada caso se aprueba por su sha256. Lo que no viene de la lista de casos aprobada (26 §16) es propuesta "
              "del sistema: usted aprueba, cambia o quita. Personas, lugares y objetos son inventados, salvo los "
              "sujetos reales de K03, K04 y K07, que se verifican contra fotos reales.",
         "2": "G1 y G2 se aprueban por el sha256 del brief, como el lote 1. K10–K13 usan como referencia imágenes que "
              "todavía no existen (K01, K02, G1, G2): se aprueba su contenido, que es el brief más las referencias "
              "previstas, por el «sha256 del contenido». Cuando exista cada imagen se escribe su sha256 y se aprueba "
              "de nuevo (PLAN §5, tarea 3). Lo que no viene de la lista de casos aprobada (26 §16) es propuesta del "
              "sistema: usted aprueba, cambia o quita. Las personas son inventadas.",
         "3": "Cada edición cambia una sola cosa de una imagen ya aprobada en los lotes 1 y 2 y lista lo que se "
              "preserva; no redefine la toma (escena, cámara y luz vienen de la imagen). La imagen a editar todavía "
              "no existe: se aprueba el contenido, que es el brief más la referencia prevista, por el «sha256 del "
              "contenido», y se aprueba de nuevo cuando exista (PLAN §5, tarea 3). K17, K18 y K21 van con el lote de "
              "sus entradas (E5, E6 y K30). Lo que no viene de la lista de casos aprobada (26 §16) es propuesta del "
              "sistema: usted aprueba, cambia o quita.",
         "4": "E5 y E6 son entradas, no casos: génesis de persona con armar.py, que se aprueban por el sha256 del "
              "brief; sus facetas son propuesta del sistema y su QA solo comprueba que sirven de entrada. K17 y K18 "
              "editan E5 y E6; K26 transfiere el estilo de K02 al vaso de K05. Esas tres usan imágenes que aún no "
              "existen: se aprueba el contenido por el «sha256 del contenido» y se aprueba de nuevo cuando existan "
              "(PLAN §5, tarea 3). Las personas son inventadas."}
ETQ = {"espacio": "Espacio", "entorno": "Entorno", "momento": "Momento", "clima": "Clima", "planos": "Planos",
       "plano": "Plano", "angulo": "Ángulo", "altura": "Altura de cámara", "efecto_optico": "Efecto óptico",
       "lente_intencion": "Lente", "fuente": "Fuente", "direccion": "Dirección", "dureza": "Dureza",
       "distribucion": "Distribución", "contraste": "Contraste", "id": "Id", "clase": "Clase",
       "descripcion": "Descripción", "edad": "Edad", "genero": "Género", "rasgos": "Rasgos", "cabello": "Cabello",
       "vestuario": "Vestuario", "expresion": "Expresión", "posicion": "Posición", "ocupacion": "Ocupación del rostro",
       "detalles": "Detalles", "literales": "Texto literal", "tipografia": "Tipografía", "tipo": "Tipo",
       "estado_visible": "Estado visible", "evidencia_fisica": "Evidencia física", "regimen": "Régimen",
       "postura": "Postura", "invariantes": "Invariantes", "referencias": "Referencias", "relaciones": "Relaciones",
       "contactos": "Contactos", "cambio": "Cambio (uno solo)", "preservar": "Se preserva",
       "propiedades": "Propiedades que se transfieren"}


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
    rp = AQUI / f"{kid}.referencias.json"
    refs = json.loads(rp.read_text(encoding="utf-8")) if rp.exists() else None
    objeto = {"entrada": en, "referencias_previstas": refs} if refs else en
    digest = hashlib.sha256(json.dumps(objeto, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    facetas = " · ".join(f"<b>{f}</b> {e(p[f])}" for f in ("F10", "F15", "F32", "F04", "F11", "F13", "F14") if p[f])
    s = [f"<section><h2>{kid} · {e(p['descripcion'] or p['F10'])}</h2>", f"<p class='brief'>{e(c['brief_literal'])}</p>",
         f"<p class='fac'>{p.get('etiqueta') or ('Mismo tipo que K01 (PLAN §4, tabla de entradas)' if kid.startswith('G') else 'Lista aprobada (26 §16)')}: {facetas}</p>",
         "<table>",
         f"<tr><th>Formato</th><td>{e(en['formato']['ratio'])} · referencia {en['formato']['ancho_px']}x"
         f"{en['formato']['alto_px']} · quality {e(p['quality'])}</td></tr>",
         f"<tr><th>Pieza</th><td>{valor(en['pieza'])}</td></tr></table>",
         "<h3>Propuesto por el sistema, para su aprobación</h3>"]
    if en.get("sujetos", {}).get("items"):
        for it in en["sujetos"]["items"]:
            s.append(f"<h4>Sujeto: {e(it['id'])}</h4><table>{filas(it)}</table>")
    for k, t in (("escena", "Escena"), ("camara", "Cámara"), ("luz", "Luz")):
        if k in en:
            s.append(f"<h4>{t}</h4><table>{filas(en[k])}</table>")
    for k, t in (("edicion", "Edición"), ("accion", "Acción"), ("fisica", "Física"), ("rostro", "Rostro"), ("texto_marca", "Texto en la imagen"),
                 ("identidad", "Identidad"), ("blocking", "Posiciones y miradas"), ("transferencia", "Transferencia de estilo")):
        if k in en:
            s.append(f"<h4>{t}</h4><table>{filas(en[k])}</table>")
    if "composicion" in en:
        s.append(f"<h4>Composición</h4><table><tr><th>Composición</th><td>{valor(en['composicion'])}</td></tr></table>")
    if refs:
        s.append("<h4>Referencias previstas (la imagen aún no existe)</h4><table>" + "".join(
            f"<tr><th>Image {r['indice']}: {e(r['entrada'])}</th><td><b>Rol:</b> {e(r['rol'])}<br><b>Preservar:</b> "
            f"{valor(r['preservar'])}</td></tr>" for r in refs) + "</table>")
    s.append("<h4>Estilo y restricciones</h4><table>"
             + (f"<tr><th>Estilo</th><td>{valor(en['estilo'])}</td></tr>" if "estilo" in en else "")
             + f"<tr><th>Restricciones</th><td>{valor(en['restricciones'])}</td></tr>"
             f"<tr><th>Módulos activos</th><td>{valor(en['modulos_activos']) or 'ninguno (la edición conserva la toma)'}"
             "</td></tr></table>")
    s.append(f"<p class='sha'>{'sha256 del contenido' if refs else 'sha256 del brief'}: <code>{digest}</code></p></section>")
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
<p>{INTRO[lote]}</p>
{''.join(partes)}
</body></html>"""
(AQUI / f"LOTE_{lote}.html").write_text(doc, encoding="utf-8")
print(f"LOTE_{lote}.html: {len(ids)} casos")
