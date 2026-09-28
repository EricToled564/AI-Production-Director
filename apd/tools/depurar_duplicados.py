"""Elimina reglas duplicadas de la lista de registros, sin reescribir ningún texto.

Un solo flujo, de cero, con un control automático por cada error cometido antes:

  congelar   Re-extrae el zip entregado en limpio y guarda el sha256 de cada fuente (zip y archivos del repo).
             Todo paso posterior aborta si una fuente cambió: así ninguna línea se corre a mitad del proceso.
  extraer    Corre extraer_registros.py: cada registro es copia literal de sus líneas de origen (lo comprueba
             contra el zip), toda línea queda en un registro o excluida con motivo, y las 1,398 reglas y 610 citas
             de sintaxis de referencia quedan contenidas.
  lotes P / importar P, con P en:
    enunciar   por registro, un enunciado normativo y 1-3 temas; el lote lleva texto completo, documento,
               encabezado y contexto de cada registro.
    agrupar    por tema, el tema COMPLETO en un lote: se buscan registros que dicen la misma regla. Los grupos que
               comparten registros se unen.
    depurar    por grupo, con texto completo y encabezados: qué originales se conservan tal cual y cuáles se
               eliminan porque todo su contenido ya está en un conservado. Nada se redacta.
    verificar  un verificador distinto revisa cada eliminación contra su contenedor final.
  final      Reglas de cierre: una eliminación queda solo si pasó la verificación independiente Y el chequeo
             mecánico (cada número y cada cita literal del eliminado está en su contenedor); si no, el registro se
             conserva. Los ciclos de contención se conservan enteros. Escribe dd_eliminado.
  prueba     100 filas al azar del xlsx entregado contra el zip, byte a byte (HTML: texto visible).

Cada importación comprueba que los textos del lote son idénticos a los de la base (ningún recorte) y que el
manifiesto de fuentes no cambió. Los lotes y sus salidas quedan en data/depuracion/ (versionados).
Uso: python3 tools/depurar_duplicados.py congelar|extraer|estado|final|prueba XLSX|lotes P|importar P
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import random
import re
import shutil
import sqlite3
import subprocess
import sys
import zipfile
from pathlib import Path

APD = Path(__file__).resolve().parents[1]
DB = APD / "data/rules.sqlite"
DIR = APD / "data/depuracion"
MANIFIESTO = DIR / "manifiesto.json"
ZIP = APD / "originales/AI_Production_Director_v3.4.0_COMPLETE.zip"
RAIZ_ZIP = "AI_Production_Director_v3.4.0_COMPLETE/"
PALABRAS_LOTE = 7000

sys.path.insert(0, str(APD / "tools"))
import extraer_registros as ext  # noqa: E402

TEMAS = {
    "marca_brandlock": "brand-lock: secciones, paleta hex, tipografía, never list, voz, confianza de valores",
    "estrategia_conceptos": "brief, SMP, territorios, concept cards, matriz, dirección narrativa",
    "guion_formato": "guion: sluglines, acción, personajes, diálogo, XML, estructura, escenas",
    "dramaturgia_escena": "fórmula de escena, three-jobs, blocking, staging, poder, geometría, mirada",
    "tres_detalles": "ley de los tres detalles: presión ambiental, micro-acción, motivo sonoro/visual",
    "emocion_sin_nombrar": "mostrar no contar, emoción como cuerpo u objeto, 2-4 señales",
    "vocabulario_prohibido": "palabras vetadas, anti-slop, cinematic/epic/masterpiece, adjetivos vacíos",
    "cinco_anclas_motivo": "cinco anclas, objeto ancla, motivo, imagen final, quiebre",
    "ritmo_montaje": "ritmo, densidad de cortes, escalera, pausa, Murch, transiciones, cut types",
    "funcion_de_plano": "etiquetas Establish/Power/Pressure/Detail/..., captions de carrera, beats",
    "beat_framework_timing": "frameworks de beats, duración de shots, hook, CTA, curva de energía",
    "shots_json_schema": "shots.json, campos, schema, series_lock, rationale, run.json, versión",
    "texto_en_pantalla": "texto/overlays/tipografía en pantalla, text-overlays.json, nunca en el prompt, lectura",
    "logos_marcas_en_imagen": "logos, lettering, marcas generadas, patrocinadores, composición en post",
    "consistencia_identidad": "identidad de personaje, bloque de identidad, maestros, verbatim, clones, drift",
    "referencias_roles": "imágenes de referencia, @img, elements, ingredients, rol de cada referencia, límites de refs",
    "genesis_maestros": "génesis sin refs, T1 rostro, T2 cuerpo, placa vacía, canonizar, dos pasos",
    "composicion_insercion": "cuadros con varios sujetos, inserción secuencial, anclas de posición, contacto, manos",
    "edicion_imagen": "edición quirúrgica, preserve list, un cambio por iteración, edit no re-roll, inpainting",
    "estructura_prompt_imagen": "slots/secciones del prompt de imagen, orden, 5 slots, prosa NB, metadatos fuera",
    "estructura_prompt_video": "esqueletos de prompt de video por modelo, bloques, orden, peso al inicio",
    "longitud_prompt": "número de palabras, elementos máximos, compresión, presupuesto",
    "negativos": "negative prompt, no X, framing positivo, prohibiciones en el prompt",
    "parametros_tecnicos": "aspect ratio, resolución, duración, seed, quality, cfg, flags, parámetros API",
    "seleccion_modelo": "qué modelo usar para qué, ruteo, cuándo escalar, costos por modelo",
    "capacidades_modelo": "límites y capacidades de cada modelo, versiones, fallos conocidos del modelo",
    "camara_movimiento": "movimiento de cámara, uno por shot, motivado, vocabulario de movimientos, rig montable",
    "encuadre_lente_dof": "encuadre ECU-EWS, lente mm, profundidad de campo, compresión",
    "angulo_camara": "ángulo y altura de cámara, low/high/dutch/overhead, poder",
    "composicion_frame": "tercios, espacio negativo, capas FG/MG/BG, simetría, punto focal, dónde va el cuerpo",
    "luz": "fuente motivada, dirección, dureza, contraluz, specular, 70% sin luz, prácticos",
    "color_grade_paleta": "paleta concreta, grade, stock de película, textura, grano, halación, HDR",
    "piel_rostro_realismo": "piel, poros, look plástico, rostros, anti-AI look, realismo fotográfico",
    "anatomia_manos": "manos, dedos, anatomía, lateralidad, inspección al 100%",
    "movimiento_congelado_blur": "still como instante congelado, blur diferencial, cues de movimiento, estado posterior",
    "fisica_consecuencia": "física por consecuencia, agua, spray, humo, partículas, deformación",
    "velocidad_vehiculo": "cues de velocidad, rim barrido, carreras, vehículos, anti-fake",
    "multitud_grupo": "multitud anónima, ensamble, número de personas, rostros legibles",
    "clima_atmosfera": "lluvia, niebla, rayo, polvo, presión ambiental, una sola atmósfera",
    "audio_dialogo": "audio, diálogo, lip-sync, SFX, música, VO, marcadores de audio",
    "continuidad_multiclip": "continuidad entre clips, repetir bloque, luz constante, empalme de clips",
    "multishot": "varios shots en una generación, marcadores de corte, anti-mush",
    "i2v_keyframes": "imagen a video, primer/último frame, no re-describir, motion brief",
    "edicion_extension_video": "editar video existente, extender, ultra long, blockout, green screen",
    "critica_qa": "crítica por capas, severidad, verdict, ACCEPT/REVISE/REJECT, re-roll vs post",
    "revision_iteracion": "revisión selectiva, rondas, máximo de intentos, cambio de método, costo",
    "validacion_gates": "validadores, linter, gates, micro-gate, pregunta de avance, checks mecánicos",
    "trazabilidad_procedencia": "hashes, snapshot, run.json, rondas, procedencia, fuente de verdad",
    "entrega_paquete": "production package, preview HTML, estructura de carpetas, atribución, checklist",
    "postproduccion": "edición, grade, audio en post, export, specs de plataforma",
    "patrones_genero": "plantillas por género: moda, comida, producto, retrato, póster, UI, social",
    "layout_grafico": "slides, infografías, grids, multi-panel, bento, layouts",
    "animacion_ilustracion": "animación, principios Disney, estilos ilustrados, anime, 3D",
    "conducta_agente": "cómo responde y trabaja el agente: leer skills, preguntar, formato de respuesta, no inventar",
    "flujo_pipeline": "tracks, etapas, orden, sub-skills, carga de skills, gates entre etapas",
    "regimenes_etiquetado": "etiquetas FUENTE/A PRUEBA/CAMPO/CANONICA, investigación de campo, esqueleto de régimen",
    "herramientas_codigo": "instalación, uso y mantenimiento de herramientas, scripts, CI",
    "ejemplo_marca": "contenido de una marca o proyecto de ejemplo concreto (WhyStrohm, Acme, café, etc.)",
}

SIS = {
    "enunciar": """Recibes registros de una base de reglas de producción audiovisual con IA. Cada registro trae su texto
literal completo, el documento y la ruta de encabezados donde está, y a veces un contexto (encabezado de tabla o de
bloque). El encabezado dice el alcance: modelo, régimen, etapa, caso. Para CADA registro devuelve:
- "enunciado": la regla en español, UNA frase: qué exige, prohíbe, limita o especifica. Si es un ejemplo o una
  explicación sin norma, empieza con "Ejemplo:" o "Explicación:".
- "alcance": a qué aplica exactamente según texto y encabezado (modelo y versión, caso, etapa, régimen) o "general".
- "temas": de 1 a 3 claves de la lista, las que mejor describen de qué trata.
Lista de temas (clave: descripción):
{temas}
Devuelve JSON {{"registros": [{{"id": "...", "enunciado": "...", "alcance": "...", "temas": ["..."]}}]}} con
exactamente los ids recibidos, en el mismo orden.""",
    "agrupar": """Recibes TODOS los enunciados de un tema (id, alcance, enunciado, documento y encabezado). Encuentra
TODOS los grupos de registros que establecen LA MISMA REGLA aunque estén redactados distinto: misma obligación,
prohibición, límite o instrucción con el mismo alcance; uno puede ser más completo que otro. Método: reparte primero
en subtemas finos, compara dentro de cada subtema cada registro con todos los demás y revisa al final cruzando
subtemas vecinos. No agrupes reglas que solo comparten tema, que tienen valores distintos, ni un ejemplo con la
regla que ilustra. Mismo contenido bajo encabezados de modelos o regímenes distintos: relacion
"misma_regla_otro_alcance".
Devuelve JSON {"grupos": [{"ids": [...], "relacion": "misma_regla" | "misma_regla_otro_alcance", "regla": "la
regla común en una frase"}]} (o {"grupos": []}). Solo ids del listado.""",
    "depurar": """Eliminas duplicados SIN reescribir nada. Cada grupo trae registros originales (texto literal completo,
documento, encabezado y contexto). Decide qué originales se CONSERVAN tal cual y cuáles se ELIMINAN:
- Un original se elimina solo si TODO su contenido (cada exigencia, prohibición, valor, número, cita literal,
  excepción, ejemplo y alcance, incluido el que da su encabezado) ya está en UN conservado, que indicas en
  "contenido_en".
- Si dos registros dicen lo mismo pero cada uno tiene algo propio, se conservan los dos. En la duda, se conserva.
- El grupo puede mezclar reglas distintas: esas se conservan todas.
Devuelve JSON {"grupos": [{"grupo": "...", "conservar": [ids], "eliminar": [{"id": "...", "contenido_en": "id",
"razon": "..."}]}]}; cada id del grupo aparece exactamente una vez y "contenido_en" es un id conservado del grupo.""",
    "verificar": """Auditas eliminaciones de duplicados. Cada caso trae el registro ELIMINADO y el registro CONTENEDOR
que lo sustituye (texto literal completo, documento y encabezado de ambos). ¿TODO el contenido del eliminado
(cada exigencia, prohibición, valor, número, cita literal, excepción, ejemplo y alcance, incluido el que da su
encabezado) está en el contenedor? Si falta algo, aunque sea pequeño, "contenido" es false y dices exactamente qué
falta. La redacción y el formato distintos no cuentan como falta.
Devuelve JSON {"casos": [{"id": "...", "contenedor": "...", "contenido": true | false, "falta": "..."}]}, un objeto
por caso.""",
}


# ---------------------------------------------------------------- base, fuentes y controles

def con():
    c = sqlite3.connect(DB)
    c.executescript("""
        CREATE TABLE IF NOT EXISTS dd_enunciado (id TEXT PRIMARY KEY, enunciado TEXT, alcance TEXT, temas TEXT);
        CREATE TABLE IF NOT EXISTS dd_candidato (lote TEXT, ids TEXT, relacion TEXT, regla TEXT);
        CREATE TABLE IF NOT EXISTS dd_grupo (grupo TEXT, id TEXT, relacion TEXT, regla TEXT);
        CREATE TABLE IF NOT EXISTS dd_decision (grupo TEXT PRIMARY KEY, conservar TEXT, eliminar TEXT);
        CREATE TABLE IF NOT EXISTS dd_verificacion (id TEXT, contenedor TEXT, contenido INTEGER, falta TEXT,
                                                     PRIMARY KEY (id, contenedor));
        CREATE TABLE IF NOT EXISTS dd_eliminado (id TEXT PRIMARY KEY, contenedor TEXT, grupo TEXT, razon TEXT);
    """)
    return c


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def exigir_manifiesto():
    if not MANIFIESTO.exists():
        raise SystemExit("falta el manifiesto: correr 'congelar' primero")
    m = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    cambiadas = [r for r, h in m["fuentes"].items() if sha(Path(m["rutas"][r])) != h]
    if sha(ZIP) != m["zip"]:
        cambiadas.append(str(ZIP))
    if cambiadas:
        raise SystemExit(f"ABORTA: fuentes cambiadas desde 'congelar': {cambiadas[:10]}")


def textos(c):
    return dict(c.execute("select id, texto from registros"))


def ubicaciones(c):
    out: dict[str, list] = {}
    for rid, a, li, lf, sec in c.execute("select registro_id, archivo, linea_ini, linea_fin, seccion from registros_fuente"):
        out.setdefault(rid, []).append({"documento": a, "lineas": f"{li}-{lf}", "encabezado": sec or ""})
    return out


def ficha(c, rid, T, U, CTX):
    f = {"id": rid, "ubicaciones": U.get(rid, []), "texto": T[rid]}
    if CTX.get(rid):
        f["contexto"] = CTX[rid]
    return f


def grupos(c):
    g: dict[str, list] = {}
    for gr, rid in c.execute("select grupo, id from dd_grupo order by grupo"):
        g.setdefault(gr, []).append(rid)
    return g


def por_presupuesto(items, palabras, maximo):
    lotes, cur, n = [], [], 0
    for it, w in items:
        if cur and (n + w > palabras or len(cur) >= maximo):
            lotes.append(cur)
            cur, n = [], 0
        cur.append(it)
        n += w
    if cur:
        lotes.append(cur)
    return lotes


# ---------------------------------------------------------------- chequeo mecánico de literales

NUM = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)?(?:%|s|mm|px|K)?")
CITA = re.compile(r'"([^"\n]{3,120})"|`([^`\n]{2,120})`')


def literales_faltantes(eliminado: str, contenedor: str) -> list[str]:
    """Números y citas literales ("...", `...`) del eliminado que no aparecen tal cual en el contenedor."""
    num_c = set(NUM.findall(contenedor))
    faltan = [f"número {n}" for n in sorted(set(NUM.findall(eliminado))) if n not in num_c]
    for a, b in CITA.findall(eliminado):
        q = (a or b).strip()
        if q.strip(".") and q.lower() not in contenedor.lower():
            faltan.append(f"cita literal: {q}")
    return faltan


# ---------------------------------------------------------------- pasos

def cmd_congelar(_a):
    pkg = APD / ".cache/pkg"
    if pkg.exists():
        shutil.rmtree(pkg)
    pkg.mkdir(parents=True)
    with zipfile.ZipFile(ZIP) as z:
        z.extractall(pkg)
    rutas = {r: str(p) for r, p, _, _ in ext.fuentes()}
    faltan = [r for r, p in rutas.items() if not Path(p).exists()]
    if faltan:
        raise SystemExit(f"fuentes inexistentes: {faltan}")
    DIR.mkdir(parents=True, exist_ok=True)
    MANIFIESTO.write_text(json.dumps({"zip": sha(ZIP), "fuentes": {r: sha(Path(p)) for r, p in rutas.items()},
                                      "rutas": rutas}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"congelado: zip re-extraído en limpio · {len(rutas)} fuentes con sha256 en {MANIFIESTO}")


def cmd_extraer(_a):
    exigir_manifiesto()
    r = subprocess.run([sys.executable, str(APD / "tools/extraer_registros.py"), "--db", str(DB)])
    if r.returncode:
        raise SystemExit("ABORTA: el extractor no pasó sus controles")
    c = con()
    for t in ("dd_enunciado", "dd_candidato", "dd_grupo", "dd_decision", "dd_verificacion", "dd_eliminado"):
        c.execute(f"delete from {t}")
    c.commit()
    T = textos(c)
    (DIR / "registros.json").write_text(json.dumps(T, ensure_ascii=False, indent=0), encoding="utf-8")
    exigir_manifiesto()
    print(f"extraídos {len(T)} registros literales; tablas dd_* vaciadas")


def cmd_lotes(a):
    exigir_manifiesto()
    c = con()
    T, U = textos(c), ubicaciones(c)
    CTX = dict(c.execute("select id, contexto from registros"))
    d = DIR / a.paso
    if d.exists() and any(d.glob("*.in.json")):
        raise SystemExit(f"{d} ya tiene lotes; un paso se genera una sola vez")
    d.mkdir(parents=True, exist_ok=True)
    lotes = []
    if a.paso == "enunciar":
        items = [(ficha(c, i, T, U, CTX), len(T[i].split()) + 20) for (i,) in c.execute("select id from registros order by orden")]
        sis = SIS["enunciar"].format(temas="\n".join(f"{k}: {v}" for k, v in TEMAS.items()))
        lotes = [{"instrucciones": sis, "registros": l} for l in por_presupuesto(items, PALABRAS_LOTE, 200)]
    elif a.paso == "agrupar":
        if c.execute("select count(*) from dd_enunciado").fetchone()[0] != len(T):
            raise SystemExit("faltan enunciados")
        por_tema: dict[str, list] = {}
        for rid, en, al, te in c.execute("select id, enunciado, alcance, temas from dd_enunciado"):
            for t in json.loads(te):
                por_tema.setdefault(t, []).append({"id": rid, "alcance": al, "enunciado": en,
                                                   "ubicaciones": [{"documento": u["documento"], "encabezado": u["encabezado"]}
                                                                   for u in U[rid]]})
        for t, filas in sorted(por_tema.items()):
            lotes.append({"instrucciones": SIS["agrupar"], "tema": t, "descripcion_tema": TEMAS[t],
                          "filas": sorted(filas, key=lambda x: (x["alcance"], x["enunciado"]))})
    elif a.paso == "depurar":
        items = [({"grupo": g, "miembros": [ficha(c, i, T, U, CTX) for i in ids]},
                  sum(len(T[i].split()) + 20 for i in ids)) for g, ids in grupos(c).items()]
        lotes = [{"instrucciones": SIS["depurar"], "grupos": l} for l in por_presupuesto(items, PALABRAS_LOTE, 40)]
    elif a.paso == "verificar":
        items = []
        for rid, cont in c.execute("select id, contenedor from dd_eliminado order by grupo"):
            items.append(({"id": rid, "contenedor": cont, "eliminado": ficha(c, rid, T, U, CTX),
                           "registro_contenedor": ficha(c, cont, T, U, CTX)}, len(T[rid].split()) + len(T[cont].split()) + 40))
        lotes = [{"instrucciones": SIS["verificar"], "casos": l} for l in por_presupuesto(items, PALABRAS_LOTE, 70)]
    for k, l in enumerate(lotes, 1):
        (d / f"{k:03d}.in.json").write_text(json.dumps(l, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{a.paso}: {len(lotes)} lotes en {d}")


def _integridad(lote, T):
    """Los textos que vio quien procesó el lote deben ser idénticos a los de la base: ningún recorte."""
    malos = []

    def mirar(f):
        if isinstance(f, dict) and "id" in f and "texto" in f and T.get(f["id"]) != f["texto"]:
            malos.append(f["id"])
    for clave in ("registros",):
        for f in lote.get(clave, []):
            mirar(f)
    for g in lote.get("grupos", []):
        for f in g.get("miembros", []):
            mirar(f)
    for cs in lote.get("casos", []):
        mirar(cs.get("eliminado"))
        mirar(cs.get("registro_contenedor"))
    return malos


def cmd_importar(a):
    exigir_manifiesto()
    c = con()
    T = textos(c)
    d = DIR / a.paso
    errores, n = [], 0
    if a.paso == "agrupar":
        c.execute("delete from dd_candidato")
    if a.paso == "verificar":
        c.execute("delete from dd_verificacion")
    for fin in sorted(d.glob("*.in.json")):
        fout = d / fin.name.replace(".in.", ".out.")
        lote = json.loads(fin.read_text(encoding="utf-8"))
        rec = _integridad(lote, T)
        if rec:
            errores.append(f"{fin.name}: texto distinto al de la base en {rec[:5]}")
            continue
        if not fout.exists():
            errores.append(f"{fout.name}: falta")
            continue
        try:
            r = json.loads(fout.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errores.append(f"{fout.name}: JSON inválido ({e})")
            continue
        if a.paso == "enunciar":
            out = {x.get("id"): x for x in r.get("registros", [])}
            ids = [f["id"] for f in lote["registros"]]
            malos = [i for i in ids if not (out.get(i, {}).get("enunciado") and out[i].get("temas")
                                            and all(t in TEMAS for t in out[i]["temas"]))]
            if malos or set(out) - set(ids):
                errores.append(f"{fout.name}: {len(malos)} ids sin enunciado o con temas fuera de la lista")
                continue
            for i in ids:
                c.execute("insert or replace into dd_enunciado values (?,?,?,?)",
                          (i, out[i]["enunciado"], out[i].get("alcance", "general"), json.dumps(out[i]["temas"][:3])))
            n += len(ids)
        elif a.paso == "agrupar":
            validos = {f["id"] for f in lote["filas"]}
            if "grupos" not in r:
                errores.append(f"{fout.name}: sin clave grupos")
                continue
            for g in r["grupos"]:
                ids = sorted(set(g.get("ids", [])))
                if not set(ids) <= validos:
                    errores.append(f"{fout.name}: ids ajenos al tema")
                    break
                if len(ids) >= 2:
                    c.execute("insert into dd_candidato values (?,?,?,?)",
                              (fin.name, json.dumps(ids), g.get("relacion", "misma_regla"), g.get("regla", "")))
                    n += 1
        elif a.paso == "depurar":
            out = {x.get("grupo"): x for x in r.get("grupos", [])}
            for g in lote["grupos"]:
                ids = sorted(m["id"] for m in g["miembros"])
                x = out.get(g["grupo"])
                if not x:
                    errores.append(f"{fout.name}: falta {g['grupo']}")
                    continue
                cons = x.get("conservar", [])
                el = x.get("eliminar", [])
                reparto = sorted(cons + [e.get("id") for e in el])
                if reparto != ids or not cons or any(e.get("contenido_en") not in cons for e in el):
                    errores.append(f"{fout.name}: {g['grupo']} reparto inválido")
                    continue
                c.execute("insert or replace into dd_decision values (?,?,?)",
                          (g["grupo"], json.dumps(cons), json.dumps(el, ensure_ascii=False)))
                n += 1
        elif a.paso == "verificar":
            out = {(x.get("id"), x.get("contenedor")): x for x in r.get("casos", [])}
            for cs in lote["casos"]:
                x = out.get((cs["id"], cs["contenedor"]))
                if x is None or not isinstance(x.get("contenido"), bool):
                    errores.append(f"{fout.name}: falta el veredicto de {cs['id']}")
                    continue
                c.execute("insert or replace into dd_verificacion values (?,?,?,?)",
                          (cs["id"], cs["contenedor"], int(x["contenido"]), x.get("falta", "")))
                n += 1
    if errores:
        c.rollback()
        print(f"{a.paso}: NO importado · {len(errores)} errores")
        for e in errores[:30]:
            print("  " + e)
        sys.exit(1)
    if a.paso == "agrupar":
        _unir(c)
    if a.paso == "depurar":
        faltan = set(grupos(c)) - {g for (g,) in c.execute("select grupo from dd_decision")}
        if faltan:
            c.rollback()
            raise SystemExit(f"grupos sin decisión: {sorted(faltan)[:10]}")
        _eliminados_provisionales(c)
    c.commit()
    print(f"{a.paso}: {n} elementos importados · 0 errores")


def _unir(c):
    padre: dict[str, str] = {}

    def raiz(x):
        padre.setdefault(x, x)
        while padre[x] != x:
            padre[x] = padre[padre[x]]
            x = padre[x]
        return x
    cand = [(json.loads(i), rel, regla) for i, rel, regla in c.execute("select ids, relacion, regla from dd_candidato")]
    for ids, _, _ in cand:
        for i in ids[1:]:
            padre[raiz(i)] = raiz(ids[0])
    comp: dict[str, dict] = {}
    for ids, rel, regla in cand:
        d = comp.setdefault(raiz(ids[0]), {"ids": set(), "rel": set(), "reglas": []})
        d["ids"].update(ids)
        d["rel"].add(rel)
        d["reglas"].append(regla)
    c.execute("delete from dd_grupo")
    for k, d in enumerate(sorted(comp.values(), key=lambda d: (-len(d["ids"]), sorted(d["ids"]))), 1):
        rel = d["rel"].pop() if len(d["rel"]) == 1 else "mixta"
        for i in sorted(d["ids"]):
            c.execute("insert into dd_grupo values (?,?,?,?)", (f"G{k:04d}", i, rel, " / ".join(dict.fromkeys(d["reglas"]))))
    n_g, n_r = c.execute("select count(distinct grupo), count(*) from dd_grupo").fetchone()
    print(f"agrupación: {n_g} grupos · {n_r} registros implicados")


def _eliminados_provisionales(c):
    c.execute("delete from dd_eliminado")
    for g, el in c.execute("select grupo, eliminar from dd_decision").fetchall():
        for e in json.loads(el):
            c.execute("insert into dd_eliminado values (?,?,?,?)", (e["id"], e["contenido_en"], g, e.get("razon", "")))


def cmd_final(_a):
    """Cierre: una eliminación queda solo si pasó verificación independiente y chequeo literal; si no, se conserva."""
    exigir_manifiesto()
    c = con()
    T = textos(c)
    elim = {r: (cont, g, raz) for r, cont, g, raz in c.execute("select id, contenedor, grupo, razon from dd_eliminado")}
    ver = {(r, ct): (ok, f) for r, ct, ok, f in c.execute("select id, contenedor, contenido, falta from dd_verificacion")}
    sin_ver = [r for r, (ct, _, _) in elim.items() if (r, ct) not in ver]
    if sin_ver:
        raise SystemExit(f"eliminaciones sin verificación independiente: {len(sin_ver)}")
    quedan, vueltos = {}, []
    for r, (ct, g, raz) in elim.items():
        ok, falta = ver[(r, ct)]
        lit = literales_faltantes(T[r], T[ct])
        if ok and not lit:
            quedan[r] = (ct, g, raz)
        else:
            vueltos.append((r, "verificador: " + falta if not ok else "chequeo literal: " + "; ".join(lit)))
    # un contenedor eliminado debe tener, siguiendo la cadena, un contenedor final conservado; los ciclos se conservan
    cambio = True
    while cambio:
        cambio = False
        for r in list(quedan):
            visto, x = {r}, quedan[r][0]
            while x in quedan:
                if x in visto:
                    break
                visto.add(x)
                x = quedan[x][0]
            if x in visto:  # ciclo
                for y in visto:
                    if y in quedan:
                        vueltos.append((y, "ciclo de contención"))
                        del quedan[y]
                cambio = True
                break
    finales = {}
    for r in quedan:
        x = quedan[r][0]
        while x in quedan:
            x = quedan[x][0]
        finales[r] = x
    malos_trans = [r for r, x in finales.items() if literales_faltantes(T[r], T[x])]
    if malos_trans:
        raise SystemExit(f"cadena de contención con pérdida literal: {malos_trans[:10]}")
    c.execute("delete from dd_eliminado")
    for r, (ct, g, raz) in quedan.items():
        c.execute("insert into dd_eliminado values (?,?,?,?)", (r, finales[r], g, raz))
    c.commit()
    (DIR / "final.json").write_text(json.dumps({
        "registros": len(T), "eliminados": len(quedan), "lista_final": len(T) - len(quedan),
        "conservados_por_duda": [{"id": r, "motivo": m} for r, m in vueltos]}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    print(f"final: {len(T)} registros · {len(quedan)} duplicados eliminados · {len(vueltos)} conservados por duda · "
          f"lista final {len(T) - len(quedan)}")


def cmd_prueba(a):
    """100 filas al azar del xlsx entregado, cada una contra todas sus ubicaciones, leyendo el zip."""
    import openpyxl
    exigir_manifiesto()
    c = con()
    z = zipfile.ZipFile(ZIP)
    nombres = set(z.namelist())

    def lineas(ar):
        n = RAIZ_ZIP + ar if ar.startswith("skills/") else RAIZ_ZIP + ar[4:] if ar.startswith("pkg/") else None
        t = z.read(n).decode("utf-8") if n in nombres else (APD.parent / ar).read_text(encoding="utf-8")
        L = t.split("\n")
        return L[:-1] if L and L[-1] == "" else L
    ws = openpyxl.load_workbook(a.xlsx, read_only=True)["Registros"]
    cab = [x.value for x in next(ws.iter_rows(max_row=1))]
    col = cab.index("ID registro")
    filas = [(r[0], r[col]) for r in ws.iter_rows(min_row=2, values_only=True)]
    muestra = random.Random(int.from_bytes(os.urandom(8), "big")).sample(filas, 100)
    fallos = []
    for texto, rid in muestra:
        for ar, li, lf, lin in c.execute("select archivo, linea_ini, linea_fin, lineas from registros_fuente where registro_id=?", (rid,)):
            L = lineas(ar)
            if ar.endswith(".html"):
                vis = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", "\n".join(L[li - 1:lf]))))
                ok = all(re.sub(r"\s+", " ", x).strip() in vis for x in texto.split("\n") if x.strip())
            else:
                ok = texto == ("\n".join(L[x - 1] for x in json.loads(lin)) if lin else "\n".join(L[li - 1:lf]))
            if not ok:
                fallos.append(f"{rid} {ar}:{li}-{lf}")
    print(f"prueba: {len(filas)} filas en el xlsx · 100 al azar · {100 - len({f.split()[0] for f in fallos})}/100 iguales a su fuente")
    for f in fallos:
        print("  FALLA", f)
    if fallos:
        sys.exit(1)


def cmd_estado(_a):
    c = con()
    for t in ("registros", "dd_enunciado", "dd_candidato", "dd_grupo", "dd_decision", "dd_eliminado", "dd_verificacion"):
        print(t, c.execute(f"select count(*) from {t}").fetchone()[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("accion", choices=["congelar", "extraer", "lotes", "importar", "final", "prueba", "estado"])
    ap.add_argument("arg", nargs="?")
    a = ap.parse_args()
    if a.accion in ("lotes", "importar"):
        if a.arg not in ("enunciar", "agrupar", "depurar", "verificar"):
            ap.error("paso: enunciar | agrupar | depurar | verificar")
        a.paso = a.arg
    if a.accion == "prueba":
        a.xlsx = a.arg
    {"congelar": cmd_congelar, "extraer": cmd_extraer, "lotes": cmd_lotes, "importar": cmd_importar,
     "final": cmd_final, "prueba": cmd_prueba, "estado": cmd_estado}[a.accion](a)


if __name__ == "__main__":
    main()
