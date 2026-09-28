"""Fusiona reglas repetidas (mismo contenido normativo con distinta redacción) SIN vectores.

1. enunciar  — el modelo reduce cada registro a un enunciado normativo en español + alcance + 1-3 temas de
               una lista cerrada. Todos los registros pasan; se verifica que vuelva cada id.
2. agrupar   — por tema, el modelo ve TODOS los enunciados del tema a la vez y devuelve los grupos que
               establecen la misma regla con el mismo alcance. Los grupos que comparten registros se unen.
3. fusionar  — por grupo, el modelo redacta un registro fusionado que conserva cada exigencia de cada miembro
               y un segundo llamado verifica miembro por miembro que no se perdió nada.
Tablas: registros_enunciado, registros_grupo, registros_fusion (originales intactos en registros).

Dos formas de ejecutar cada paso:
- por API: python3 tools/fusionar_duplicados.py enunciar|agrupar|fusionar  (usa apd.llm; requiere crédito)
- por lotes en archivo: python3 tools/fusionar_duplicados.py lotes <paso>  escribe data/fusion_lotes/<paso>/NNN.in.json
  con instrucciones + datos; quien procese el lote (p. ej. un subagente) escribe NNN.out.json con el mismo formato
  JSON que devolvería la API; python3 tools/fusionar_duplicados.py importar <paso>  valida cada salida (ids completos,
  temas de la lista, ids de grupo válidos) y la carga. Pasos por lotes: enunciar, agrupar, refinar (parte los componentes grandes o mixtos
  formados por encadenamiento en subgrupos de una sola regla), confirmar (cada grupo se revisa con el documento y la
  ruta de encabezados de cada miembro, que fijan su alcance), fusionar, verificar.
Uso: python3 tools/fusionar_duplicados.py enunciar|agrupar|fusionar|estado|lotes <paso>|importar <paso>
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

APD = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APD))
from apd import llm  # noqa: E402

DB = APD / "data/rules.sqlite"
CACHE = APD / "data/fusion_cache"
LOTES = APD / "data/fusion_lotes"
PALABRAS_LOTE = 7000
LOTE = 25
HILOS = 8

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

SIS_ENUNCIAR = """Recibes registros de una base de reglas de producción audiovisual con IA (texto completo, puede estar en
inglés, ruso o español). Para CADA registro devuelve:
- "enunciado": la regla en español, UNA frase, sin adornos: qué exige, prohíbe, limita o especifica. Si el registro
  es un ejemplo o una explicación sin norma, di qué ilustra ("Ejemplo: ...", "Explicación: ...").
- "alcance": a qué aplica exactamente (modelo y versión, caso T1-T5, etapa, tipo de pieza, régimen) o "general".
- "temas": de 1 a 3 claves de la lista, las que mejor describen de qué trata la regla.
Lista de temas (clave: descripción):
{temas}
Devuelve JSON {{"registros": [{{"id": "...", "enunciado": "...", "alcance": "...", "temas": ["..."]}}]}} con
exactamente los ids recibidos, en el mismo orden."""

SIS_AGRUPAR = """Eres auditor de una base de reglas. Recibes TODOS los enunciados normativos de un tema (id | alcance |
enunciado). Encuentra los registros que establecen LA MISMA REGLA aunque estén redactados distinto.
- MISMA regla = misma obligación, prohibición, límite o instrucción, con el mismo alcance. Uno puede ser más
  completo que otro (añade razón o ejemplo) y sigue siendo la misma regla.
- Si el contenido normativo es idéntico pero el alcance declarado es otro modelo o caso, es "misma_regla_otro_alcance".
- NO agrupes reglas que solo comparten tema, que tienen valores distintos (3-4 vs 5-7 elementos), o un ejemplo
  con la regla que ilustra.
Devuelve JSON {"grupos": [{"ids": [...], "relacion": "misma_regla" | "misma_regla_otro_alcance",
"regla": "la regla común en una frase"}]}. Solo grupos de 2 o más ids del listado."""

SIS_REFINAR = """Recibes componentes de duplicados formados al unir grupos que compartían registros; por encadenamiento
un componente puede mezclar reglas relacionadas pero DISTINTAS. Para cada componente, pártelo en subgrupos donde cada
subgrupo sea UNA sola regla (misma obligación, prohibición, límite o instrucción; un miembro puede ser más completo o
repetir la regla en un checklist, fallo conocido o resumen). Un miembro que no es la misma regla que ningún otro queda
en "sueltos". No juntes una regla general con una variante que añade condiciones o valores propios, ni reglas de
regímenes o modelos distintos salvo que el contenido normativo sea idéntico (entonces relacion = misma_regla_otro_alcance).
Devuelve JSON {"componentes": [{"grupo": "DUP-....", "subgrupos": [{"ids": [...], "relacion": "misma_regla" |
"misma_regla_otro_alcance", "regla": "la regla común en una frase"}], "sueltos": [ids]}]}; cada id del componente
aparece exactamente una vez (en un subgrupo o en sueltos)."""

SIS_CONFIRMAR = """Recibes grupos de posibles duplicados. Cada miembro trae su documento de origen, la ruta de encabezados
bajo la que está (skill › sección › subsección) y su texto completo. El encabezado dice el alcance real de la regla:
modelo, régimen, etapa, tipo de pieza, caso, checklist o fallo conocido. Para cada grupo decide, leyendo texto Y
encabezado, qué miembros son la misma regla:
- misma_regla: misma exigencia con el mismo alcance (la misma regla repetida en otra sección, checklist o resumen).
- misma_regla_otro_alcance: contenido normativo idéntico pero el encabezado la sitúa en otro modelo, régimen o caso.
- Si el encabezado muestra que dos miembros regulan cosas distintas (otro paso, otro modelo con otro valor, un ejemplo
  frente a la regla), sepáralos.
Devuelve JSON {"componentes": [{"grupo": "...", "subgrupos": [{"ids": [...], "relacion": "misma_regla" |
"misma_regla_otro_alcance", "regla": "la regla común en una frase, con su alcance"}], "sueltos": [ids]}]}; cada id del
grupo aparece exactamente una vez."""

SIS_FUSIONAR = """Fusiona registros que establecen la misma regla en UN registro. Reglas de la fusión:
- Conserva cada exigencia, límite, valor, excepción, ejemplo corto y alcance de cada miembro; nada se pierde.
- No agregues nada que no esté en algún miembro. Mantén términos técnicos y citas literales (entre comillas) tal
  como aparecen. Escribe en español; los términos y frases de prompt que deben ir en inglés se dejan en inglés.
- Si los alcances difieren (misma regla para varios modelos), nómbralos todos en el registro fusionado. El alcance lo
  dicen el documento y el encabezado de cada miembro (campo ubicaciones): consérvalo en el texto fusionado.
Devuelve JSON {"texto": "registro fusionado", "cobertura": [{"id": "...", "elementos": ["cada exigencia del
miembro y dónde quedó en el texto"]}]}"""

SIS_VERIFICAR = """Verifica una fusión. Recibes los registros originales y el texto fusionado. Para cada original,
lista las exigencias, límites, valores, excepciones y alcances que contiene y di si están en el fusionado.
Devuelve JSON {"completo": true|false, "faltan": [{"id": "...", "elemento": "..."}], "agregado_sin_fuente": ["..."]}"""


def llamar(sis, usuario, clave):
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / (hashlib.sha1((sis + usuario).encode()).hexdigest()[:20] + ".json")
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    ultimo = None
    for _ in range(4):
        try:
            r = llm.extraer_json(llm.proveedor().completar(sis, usuario)["texto"])
            f.write_text(json.dumps(r, ensure_ascii=False), encoding="utf-8")
            return r
        except Exception as e:  # noqa: BLE001
            ultimo = e
    raise RuntimeError(f"{clave}: {ultimo}")


def con():
    c = sqlite3.connect(DB)
    c.execute("create table if not exists registros_enunciado (registro_id text primary key, enunciado text, "
              "alcance text, temas text)")
    c.execute("create table if not exists registros_grupo (grupo text, registro_id text, relacion text, regla text)")
    c.execute("create table if not exists registros_fusion (grupo text primary key, texto text, relacion text, "
              "miembros text, verificado integer, faltan text)")
    c.execute("create table if not exists _grupos_crudos (lote text, ids text, relacion text, regla text)")
    return c


def cmd_enunciar(_a):
    c = con()
    hechos = {r for (r,) in c.execute("select registro_id from registros_enunciado")}
    regs = [(i, t) for i, t in c.execute("select id, texto from registros order by orden") if i not in hechos]
    lotes = [regs[i:i + LOTE] for i in range(0, len(regs), LOTE)]
    sis = SIS_ENUNCIAR.format(temas="\n".join(f"{k}: {v}" for k, v in TEMAS.items()))

    def uno(lote):
        usuario = json.dumps([{"id": i, "texto": t} for i, t in lote], ensure_ascii=False)
        for intento in range(3):
            r = llamar(sis, usuario + ("" if intento == 0 else f"\n(reintento {intento})"), lote[0][0])
            out = {x.get("id"): x for x in r.get("registros", [])}
            ok = all(i in out and out[i].get("enunciado") and out[i].get("temas") for i, _ in lote)
            if ok:
                return [(i, out[i]) for i, _ in lote]
        raise RuntimeError(f"lote {lote[0][0]}: faltan ids o campos tras 3 intentos")

    n = 0
    with cf.ThreadPoolExecutor(HILOS) as ex:
        for res in ex.map(uno, lotes):
            for i, x in res:
                temas = [t for t in x["temas"] if t in TEMAS][:3] or ["conducta_agente"]
                c.execute("insert or replace into registros_enunciado values (?,?,?,?)",
                          (i, x["enunciado"], x.get("alcance", "general"), json.dumps(temas)))
            c.commit()
            n += len(res)
            print(f"enunciados {n + len(hechos)}/{len(regs) + len(hechos)}", file=sys.stderr, flush=True)
    total = c.execute("select count(*) from registros").fetchone()[0]
    hechos = c.execute("select count(*) from registros_enunciado").fetchone()[0]
    print(f"enunciados: {hechos}/{total}")


def cmd_agrupar(_a):
    c = con()
    por_tema: dict[str, list] = {}
    for rid, en, al, temas in c.execute("select registro_id, enunciado, alcance, temas from registros_enunciado"):
        for t in json.loads(temas):
            por_tema.setdefault(t, []).append((rid, al, en))
    MAX = 220

    def uno(item):
        tema, filas = item
        filas = sorted(filas, key=lambda x: x[1])
        # un tema grande se revisa en ventanas solapadas del 50% para que todo par cercano por alcance se compare
        ventanas = [filas] if len(filas) <= MAX else [filas[i:i + MAX] for i in range(0, len(filas), MAX // 2)]
        grupos = []
        for v in ventanas:
            usuario = f"Tema: {tema} — {TEMAS.get(tema, '')}\n" + "\n".join(f"{r} | {a} | {e}" for r, a, e in v)
            res = llamar(SIS_AGRUPAR, usuario, tema)
            validos = {r for r, _, _ in v}
            for g in res.get("grupos", []):
                ids = [i for i in g.get("ids", []) if i in validos]
                if len(set(ids)) >= 2:
                    grupos.append({"ids": sorted(set(ids)), "relacion": g.get("relacion", "misma_regla"),
                                   "regla": g.get("regla", "")})
        return tema, len(filas), len(ventanas), grupos

    todos = []
    with cf.ThreadPoolExecutor(HILOS) as ex:
        for tema, n, nv, gs in ex.map(uno, sorted(por_tema.items())):
            print(f"{tema}: {n} registros, {nv} ventana(s), {len(gs)} grupos", file=sys.stderr, flush=True)
            todos.extend(gs)
    guardar_grupos(c, todos)


def guardar_grupos(c, todos):
    # unir grupos que comparten registros (misma_regla domina sobre otro_alcance)
    padre = {}

    def raiz(x):
        padre.setdefault(x, x)
        while padre[x] != x:
            padre[x] = padre[padre[x]]
            x = padre[x]
        return x
    for g in todos:
        for i in g["ids"][1:]:
            padre[raiz(i)] = raiz(g["ids"][0])
    comp: dict[str, dict] = {}
    for g in todos:
        r = raiz(g["ids"][0])
        d = comp.setdefault(r, {"ids": set(), "relaciones": set(), "reglas": []})
        d["ids"].update(g["ids"])
        d["relaciones"].add(g["relacion"])
        d["reglas"].append(g["regla"])
    c.execute("delete from registros_grupo")
    for k, d in enumerate(sorted(comp.values(), key=lambda d: -len(d["ids"])), 1):
        rel = "misma_regla" if d["relaciones"] == {"misma_regla"} else "misma_regla_otro_alcance" \
            if d["relaciones"] == {"misma_regla_otro_alcance"} else "mixta"
        for rid in sorted(d["ids"]):
            c.execute("insert into registros_grupo values (?,?,?,?)", (f"DUP-{k:04d}", rid, rel, " / ".join(dict.fromkeys(d["reglas"]))))
    c.commit()
    n_g = c.execute("select count(distinct grupo) from registros_grupo").fetchone()[0]
    n_r = c.execute("select count(distinct registro_id) from registros_grupo").fetchone()[0]
    print(f"{n_g} grupos de duplicados · {n_r} registros implicados")


def cmd_fusionar(_a):
    c = con()
    texto = dict(c.execute("select id, texto from registros"))
    grupos: dict[str, dict] = {}
    for g, rid, rel, regla in c.execute("select grupo, registro_id, relacion, regla from registros_grupo"):
        d = grupos.setdefault(g, {"ids": [], "rel": rel, "regla": regla})
        d["ids"].append(rid)
    hechos = {g for (g,) in c.execute("select grupo from registros_fusion where verificado = 1")}

    def uno(item):
        g, d = item
        miembros = json.dumps([{"id": i, "texto": texto[i]} for i in d["ids"]], ensure_ascii=False)
        faltan = []
        for intento in range(3):
            extra = "" if not faltan else "\nEn el intento anterior faltaron: " + json.dumps(faltan, ensure_ascii=False)
            f = llamar(SIS_FUSIONAR, miembros + extra, g)
            v = llamar(SIS_VERIFICAR, json.dumps({"originales": json.loads(miembros), "fusionado": f.get("texto", "")},
                                                 ensure_ascii=False), g)
            faltan = v.get("faltan", []) + [{"agregado_sin_fuente": x} for x in v.get("agregado_sin_fuente", [])]
            if v.get("completo") and not faltan:
                return g, d, f["texto"], 1, []
        return g, d, f.get("texto", ""), 0, faltan

    pend = [(g, d) for g, d in grupos.items() if g not in hechos]
    with cf.ThreadPoolExecutor(HILOS) as ex:
        for n, (g, d, t, ok, faltan) in enumerate(ex.map(uno, pend), 1):
            c.execute("insert or replace into registros_fusion values (?,?,?,?,?,?)",
                      (g, t, d["rel"], json.dumps(d["ids"]), ok, json.dumps(faltan, ensure_ascii=False)))
            c.commit()
            print(f"fusionados {n}/{len(pend)} ({'ok' if ok else 'FALTA'} {g})", file=sys.stderr, flush=True)
    malos = c.execute("select count(*) from registros_fusion where verificado = 0").fetchone()[0]
    print(f"{len(grupos)} grupos · {len(grupos) - malos} fusiones verificadas completas · {malos} con faltantes")
    if malos:
        sys.exit(1)


# ---------------------------------------------------------------- ejecución por lotes en archivo

MAX_VENTANA = 400  # el tema más grande (390) cabe entero: dentro de un tema se compara todo contra todo


def ventanas_por_tema(c):
    por_tema: dict[str, list] = {}
    for rid, en, al, temas in c.execute("select registro_id, enunciado, alcance, temas from registros_enunciado"):
        for t in json.loads(temas):
            por_tema.setdefault(t, []).append((rid, al, en))
    out = []
    for tema, filas in sorted(por_tema.items()):
        filas = sorted(filas, key=lambda x: (x[1], x[2]))
        # un tema grande se revisa en ventanas solapadas del 50% para que todo par cercano por alcance se compare
        if len(filas) <= MAX_VENTANA:
            vs = [filas]
        else:
            vs = [filas[i:i + MAX_VENTANA] for i in range(0, len(filas) - MAX_VENTANA // 2, MAX_VENTANA // 2)]
        for k, v in enumerate(vs, 1):
            out.append((tema, k, len(vs), v))
    return out


def grupos_actuales(c):
    grupos: dict[str, dict] = {}
    for g, rid, rel, regla in c.execute("select grupo, registro_id, relacion, regla from registros_grupo order by grupo"):
        d = grupos.setdefault(g, {"ids": [], "rel": rel, "regla": regla})
        d["ids"].append(rid)
    return grupos


def por_presupuesto(items, palabras, maximo):
    lotes, actual, n = [], [], 0
    for it, w in items:
        if actual and (n + w > palabras or len(actual) >= maximo):
            lotes.append(actual)
            actual, n = [], 0
        actual.append(it)
        n += w
    if actual:
        lotes.append(actual)
    return lotes


def cmd_lotes(a):
    c = con()
    d = LOTES / a.paso
    d.mkdir(parents=True, exist_ok=True)
    for f in d.glob("*.in.json"):
        if not (d / f.name.replace(".in.", ".out.")).exists():
            f.unlink()
    hechos = {f.name.split(".")[0] for f in d.glob("*.out.json")}
    texto = dict(c.execute("select id, texto from registros"))
    lotes = []
    if a.paso == "enunciar":
        ya = {r for (r,) in c.execute("select registro_id from registros_enunciado")}
        items = [({"id": i, "texto": t}, len(t.split())) for i, t in c.execute("select id, texto from registros order by orden")
                 if i not in ya]
        sis = SIS_ENUNCIAR.format(temas="\n".join(f"{k}: {v}" for k, v in TEMAS.items()))
        for lote in por_presupuesto(items, PALABRAS_LOTE, 200):
            lotes.append({"paso": "enunciar", "instrucciones": sis, "registros": lote})
    elif a.paso == "agrupar":
        for tema, k, n, v in ventanas_por_tema(c):
            lotes.append({"paso": "agrupar", "instrucciones": SIS_AGRUPAR, "tema": tema, "descripcion_tema": TEMAS.get(tema, ""),
                          "ventana": f"{k} de {n}", "filas": [{"id": r, "alcance": al, "enunciado": e} for r, al, e in v]})
    elif a.paso == "refinar":
        en = {r: (e, al) for r, e, al in c.execute("select registro_id, enunciado, alcance from registros_enunciado")}
        items = []
        for g, dd in grupos_actuales(c).items():
            if len(dd["ids"]) >= 4 or dd["rel"] == "mixta":
                miembros = [{"id": i, "alcance": en[i][1], "enunciado": en[i][0], "texto": texto[i][:1200]} for i in dd["ids"]]
                items.append(({"grupo": g, "miembros": miembros}, sum(len(m["texto"].split()) + 30 for m in miembros)))
        for lote in por_presupuesto(items, PALABRAS_LOTE, 30):
            lotes.append({"paso": "refinar", "instrucciones": SIS_REFINAR, "componentes": lote})
    elif a.paso == "confirmar":
        ubic: dict[str, list] = {}
        for rid, arch, sec in c.execute("select registro_id, archivo, seccion from registros_fuente"):
            ubic.setdefault(rid, []).append({"documento": arch, "encabezado": sec or ""})
        items = []
        for g, dd in grupos_actuales(c).items():
            miembros = [{"id": i, "ubicaciones": ubic.get(i, []), "texto": texto[i][:2500]} for i in dd["ids"]]
            items.append(({"grupo": g, "miembros": miembros},
                          sum(len(m["texto"].split()) + 15 * len(m["ubicaciones"]) for m in miembros)))
        for lote in por_presupuesto(items, PALABRAS_LOTE, 80):
            lotes.append({"paso": "confirmar", "instrucciones": SIS_CONFIRMAR, "componentes": lote})
    elif a.paso == "fusionar":
        hechos_f = {g for (g,) in c.execute("select grupo from registros_fusion where verificado = 1")}
        ubic = {}
        for rid, arch, sec in c.execute("select registro_id, archivo, seccion from registros_fuente"):
            ubic.setdefault(rid, []).append({"documento": arch, "encabezado": sec or ""})
        items = []
        for g, dd in grupos_actuales(c).items():
            if g in hechos_f:
                continue
            miembros = [{"id": i, "ubicaciones": ubic.get(i, []), "texto": texto[i]} for i in dd["ids"]]
            previo = c.execute("select faltan from registros_fusion where grupo = ?", (g,)).fetchone()
            item = {"grupo": g, "relacion": dd["rel"], "regla_comun": dd["regla"], "miembros": miembros}
            if previo and previo[0] not in (None, "[]"):
                item["faltaron_en_el_intento_anterior"] = json.loads(previo[0])
            items.append((item, sum(len(m["texto"].split()) for m in miembros)))
        for lote in por_presupuesto(items, PALABRAS_LOTE, 40):
            lotes.append({"paso": "fusionar", "instrucciones": SIS_FUSIONAR.replace(
                'Devuelve JSON {"texto"', 'Para CADA grupo devuelve {"grupo": "...", "texto"') +
                '\nDevuelve JSON {"fusiones": [ ...un objeto por grupo, con su "grupo"... ]}', "grupos": lote})
    elif a.paso == "verificar":
        items = []
        for g, t, miembros in c.execute("select grupo, texto, miembros from registros_fusion where verificado is null"):
            orig = [{"id": i, "texto": texto[i]} for i in json.loads(miembros)]
            for o in orig:
                o["ubicaciones"] = [{"documento": a_, "encabezado": s_ or ""} for a_, s_ in c.execute(
                    "select archivo, seccion from registros_fuente where registro_id = ?", (o["id"],))]
            items.append(({"grupo": g, "originales": orig, "fusionado": t},
                          sum(len(o["texto"].split()) for o in orig) + len(t.split())))
        for lote in por_presupuesto(items, PALABRAS_LOTE, 40):
            lotes.append({"paso": "verificar", "instrucciones": SIS_VERIFICAR.replace(
                'Devuelve JSON {"completo"', 'Para CADA grupo devuelve {"grupo": "...", "completo"') +
                '\nDevuelve JSON {"verificaciones": [ ...un objeto por grupo, con su "grupo"... ]}', "grupos": lote})
    base = max([int(x) for x in hechos] + [0])
    for k, lote in enumerate(lotes, base + 1):
        (d / f"{k:03d}.in.json").write_text(json.dumps(lote, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{a.paso}: {len(lotes)} lotes nuevos en {d}")


def cmd_importar(a):
    c = con()
    d = LOTES / a.paso
    errores, n = [], 0
    for fin in sorted(d.glob("*.in.json")):
        fout = d / fin.name.replace(".in.", ".out.")
        if not fout.exists():
            errores.append(f"{fin.name}: sin salida")
            continue
        lote = json.loads(fin.read_text(encoding="utf-8"))
        try:
            r = json.loads(fout.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errores.append(f"{fout.name}: JSON inválido ({e})")
            continue
        if a.paso == "enunciar":
            out = {x.get("id"): x for x in r.get("registros", [])}
            faltan = [x["id"] for x in lote["registros"] if not (out.get(x["id"], {}).get("enunciado") and out[x["id"]].get("temas"))]
            malos = [i for i, x in out.items() if any(t not in TEMAS for t in x.get("temas", []))]
            if faltan or malos:
                errores.append(f"{fout.name}: faltan {len(faltan)} ids, {len(malos)} con temas fuera de la lista")
                continue
            for x in lote["registros"]:
                y = out[x["id"]]
                c.execute("insert or replace into registros_enunciado values (?,?,?,?)",
                          (x["id"], y["enunciado"], y.get("alcance", "general"), json.dumps(y["temas"][:3])))
            n += len(lote["registros"])
        elif a.paso == "agrupar":
            validos = {x["id"] for x in lote["filas"]}
            for g in r.get("grupos", []):
                ids = sorted({i for i in g.get("ids", []) if i in validos})
                if len(ids) >= 2:
                    c.execute("insert into _grupos_crudos values (?,?,?,?)",
                              (fin.name, json.dumps(ids), g.get("relacion", "misma_regla"), g.get("regla", "")))
                    n += 1
        elif a.paso in ("refinar", "confirmar"):
            out = {x.get("grupo"): x for x in r.get("componentes", [])}
            for comp in lote["componentes"]:
                g, ids = comp["grupo"], [m["id"] for m in comp["miembros"]]
                x = out.get(g)
                vistos = [i for sg in (x or {}).get("subgrupos", []) for i in sg.get("ids", [])] + list((x or {}).get("sueltos", []))
                if x is None or sorted(vistos) != sorted(ids):
                    errores.append(f"{fout.name}: {g} no reparte cada id exactamente una vez")
                    continue
                c.execute("delete from registros_grupo where grupo = ?", (g,))
                for k, sg in enumerate([sg for sg in x["subgrupos"] if len(sg["ids"]) >= 2], 1):
                    for i in sg["ids"]:
                        c.execute("insert into registros_grupo values (?,?,?,?)",
                                  (f"{g}.{k}", i, sg.get("relacion", "misma_regla"), sg.get("regla", "")))
                n += 1
        elif a.paso == "fusionar":
            out = {x.get("grupo"): x for x in r.get("fusiones", [])}
            for item in lote["grupos"]:
                g = item["grupo"]
                if not out.get(g, {}).get("texto"):
                    errores.append(f"{fout.name}: falta la fusión de {g}")
                    continue
                c.execute("insert or replace into registros_fusion values (?,?,?,?,NULL,NULL)",
                          (g, out[g]["texto"], item["relacion"], json.dumps([m["id"] for m in item["miembros"]])))
                n += 1
        elif a.paso == "verificar":
            out = {x.get("grupo"): x for x in r.get("verificaciones", [])}
            for item in lote["grupos"]:
                g = item["grupo"]
                v = out.get(g)
                if v is None:
                    errores.append(f"{fout.name}: falta la verificación de {g}")
                    continue
                faltan = v.get("faltan", []) + [{"agregado_sin_fuente": x} for x in v.get("agregado_sin_fuente", [])]
                ok = 1 if v.get("completo") and not faltan else 0
                c.execute("update registros_fusion set verificado = ?, faltan = ? where grupo = ?",
                          (ok, json.dumps(faltan, ensure_ascii=False), g))
                n += 1
    if a.paso == "agrupar" and not errores:
        crudos = [{"ids": json.loads(i), "relacion": rel, "regla": regla}
                  for i, rel, regla in c.execute("select ids, relacion, regla from _grupos_crudos")]
        guardar_grupos(c, crudos)
    c.commit()
    print(f"{a.paso}: {n} elementos importados · {len(errores)} errores")
    for e in errores:
        print("  " + e)
    if errores:
        sys.exit(1)


def cmd_estado(_a):
    c = con()
    for q in ("select count(*) from registros", "select count(*) from registros_enunciado",
              "select count(distinct grupo), count(*) from registros_grupo",
              "select count(*), sum(verificado) from registros_fusion"):
        print(q, "→", c.execute(q).fetchone())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("accion", choices=["enunciar", "agrupar", "fusionar", "estado", "lotes", "importar"])
    ap.add_argument("paso", nargs="?", choices=["enunciar", "agrupar", "refinar", "confirmar", "fusionar", "verificar"])
    a = ap.parse_args()
    if a.accion in ("lotes", "importar"):
        if not a.paso:
            ap.error("lotes/importar requieren el paso")
        {"lotes": cmd_lotes, "importar": cmd_importar}[a.accion](a)
        return
    a.paso = a.accion
    {"enunciar": cmd_enunciar, "agrupar": cmd_agrupar, "fusionar": cmd_fusionar, "estado": cmd_estado}[a.accion](a)


if __name__ == "__main__":
    main()
