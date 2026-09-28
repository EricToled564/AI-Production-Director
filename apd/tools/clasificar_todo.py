"""Clasificación exhaustiva de las 1,398 reglas en todos los niveles de la taxonomía acordada, sin residuo.

Niveles (orden del director, 2026-09-28): fase del flujo (regla_tarea, ya completa) → medio (reglas.medio, completo) →
d10 creación (génesis/ancla/edición/clip) → d2 acción → d11 tipo de sujeto (persona/lugar/edificación/prop/producto/animal)
→ d12 interior/exterior → d4 tratamiento (documental/cinematográfico/…) → d3 número de sujetos (uno/dos/grupo/multitud)
→ d13 escala del rostro (< 20 % del cuadro) → d14 referencias (sí/no y de qué) · más d1, d5, d6, d7, d8, d9 y caso.

Método (sin revisión manual):
  - vector: k vecinos más cercanos sobre los embeddings multilingual-e5-large de las reglas ya etiquetadas
    (calibrado dejando una fuera: 93–99 % por dimensión cerrada, 96 % en caso);
  - modelo de lenguaje: dos pasadas independientes (A y B) con el vocabulario cerrado y su definición;
  - aceptación: A coincide con el vector, o A coincide con B; si no, una tercera pasada (C) decide entre las opciones
    ya propuestas. Nunca queda un par sin valor: 'ninguno' es un valor del vocabulario ("la regla no depende de esto").
Las etiquetas existentes (archivo, regex, llm, auditoría) no se tocan: sólo se llena lo que falta.

    python3 apd/tools/clasificar_todo.py --db apd/data/rules.sqlite [--solo-calcular] [--escribir]
"""

from __future__ import annotations

import argparse
import collections
import json
import random
import sqlite3
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
from apd import llm  # noqa: E402

NUEVAS = {
    # --- imagen: modo de creación y clase de sujeto (Mapa del Spot, E5.2–E5.5 y Nivel 3 «taxonomía de génesis»)
    "d10": {"nombre": "creacion", "valores": {
        "genesis": "génesis sin referencia: primera imagen que fija una identidad, lugar, edificación, animal, producto u objeto desde texto (E5.2)",
        "maestro_derivado": "maestro derivado con la génesis adjunta: cuerpo T2, variantes de pose o vestuario (E5.3)",
        "cuadro_compuesto": "cuadro con referencias canonizadas: sujeto en placa, T3/T4, producto en escena, inserción secuencial (E5.4)",
        "edicion": "edición quirúrgica sobre una imagen aprobada, T5 (E5.5)",
        "keyframe": "ancla o keyframe de inicio/fin de un clip (FF/LF)",
        "clip": "video: el clip mismo (E6)",
        "ninguno": "la regla no depende del modo de creación"}},
    "d11": {"nombre": "sujeto_tipo", "valores": {
        "persona": "persona: rostro, cuerpo, mano, atleta, niño", "lugar": "lugar genérico: exterior, interior, calle, gimnasio, estudio",
        "edificacion": "edificación o landmark real reconocible", "animal": "animal: especie real, mascota de marca, criatura",
        "producto": "producto: packaging, comida, bebida, cosmético, dispositivo",
        "objeto": "objeto o prop que no es producto: objeto ancla, herramienta, vehículo, instrumento, mobiliario",
        "ninguno": "la regla no depende de la clase de sujeto"}},
    "d12": {"nombre": "espacio", "valores": {
        "interior": "escena en interiores", "exterior": "escena en exteriores",
        "ninguno": "la regla no depende de si la escena es interior o exterior"}},
    "d13": {"nombre": "rostro_escala", "valores": {
        "rostro_dominante": "hay rostro y ocupa 20 % o más del cuadro (retrato, close-up)",
        "rostro_pequeno": "hay rostro pero ocupa menos del 20 % del cuadro (plano general, figura lejana, multitud)",
        "sin_rostro": "no hay rostro visible (producto, lugar, silueta, espalda, casco)",
        "ninguno": "la regla no depende del tamaño del rostro en el cuadro"}},
    "d14": {"nombre": "referencias", "valores": {
        "sin_referencias": "sin imágenes de referencia adjuntas (desde texto)",
        "ref_persona": "con referencia de persona o personaje", "ref_lugar": "con referencia de lugar o entorno",
        "ref_objeto": "con referencia de objeto, producto o prop", "ref_estilo": "con referencia de estilo, paleta o luz",
        "ref_frame": "con frame inicial o final (image-to-video, keyframe)",
        "ninguno": "la regla no depende de si hay referencias ni de qué tipo"}},
    # --- acción, segundo nivel: familias de régimen físico (DECISIONES #7, .claude/rules/regimenes/)
    "d15": {"nombre": "regimen_fisico", "valores": {
        "agua_superficie": "sujeto que se desplaza sobre el agua: wakeboard, surf, jet ski, remo",
        "agua_ruptura": "cruce de la superficie del agua: clavado, nadador emergiendo, split-level",
        "subacuatico": "cámara y sujeto sumergidos: buceo, cenote, apnea",
        "objeto_balistico": "objeto pequeño en vuelo o impacto: pelota, gota, flecha, chispa",
        "vehiculo": "vehículo en movimiento: auto, moto, bici, tren, dron",
        "cuerpo_esfuerzo": "cuerpo en el pico de esfuerzo: sprint, salto, golpe, levantamiento",
        "luz_clima": "fenómeno de luz o clima: rayo, amanecer, lluvia, niebla, polvo, nieve",
        "multitud_anonima": "multitud anónima: estadio, manifestación, público",
        "grupo_ensamble": "grupo con identidades: quinteto, banda, equipo, familia",
        "ninguno": "la regla no depende de un régimen físico"}},
    # --- video (E6)
    "d16": {"nombre": "clip_entrada", "valores": {
        "texto_a_video": "clip generado sólo desde texto", "frame_inicial": "image-to-video desde un frame inicial",
        "frame_inicial_final": "clip entre frame inicial y final (FF + LF)", "multi_shot": "varios shots en una generación",
        "extension": "extensión o continuación de un clip existente",
        "ninguno": "la regla no depende de cómo entra el clip (o no es de video)"}},
    "d17": {"nombre": "movimiento_camara", "valores": {
        "static": "cámara fija, locked-off", "push_pull": "push-in / pull-out, dolly adelante o atrás",
        "pan_tilt": "paneo o tilt", "tracking": "tracking lateral o seguimiento", "handheld": "cámara en mano",
        "orbit": "órbita alrededor del sujeto", "whip": "whip pan", "rack": "rack focus",
        "crane_drone": "grúa, dron o movimiento aéreo",
        "ninguno": "la regla no depende del movimiento de cámara (o no es de video)"}},
    "d18": {"nombre": "audio", "valores": {
        "dialogo_lipsync": "diálogo en cámara con sincronía labial", "voz_off": "voz en off o narración",
        "sfx_ambiente": "efectos y sonido ambiente", "musica": "música", "sin_audio": "clip sin audio",
        "ninguno": "la regla no depende del audio"}},
    "d19": {"nombre": "continuidad", "valores": {
        "entre_clips": "continuidad de identidad, vestuario, luz o eje entre varios clips o planos (U7, U13)",
        "clip_unico": "un clip o una imagen aislados",
        "ninguno": "la regla no depende de la continuidad entre piezas"}},
    "d20": {"nombre": "duracion", "valores": {
        "hasta_5s": "clip de 5 segundos o menos", "de_6_a_10s": "clip de 6 a 10 segundos",
        "mas_de_10s": "clip o pieza de más de 10 segundos (multi-clip, spot)",
        "ninguno": "la regla no depende de la duración"}},
    # --- preproducción (E0–E4)
    "d21": {"nombre": "track", "valores": {
        "express": "EXPRESS: ≤30 s, sin marca formal, entra directo en E4", "standard": "STANDARD: spot de 30–90 s",
        "film": "FILM: 90 s–10 min, estrategia completa y treatment", "ninguno": "la regla no depende del track"}},
    "d22": {"nombre": "marca", "valores": {
        "con_brand_lock": "hay marca o cliente con brand-lock (E0)", "sin_marca": "pieza sin marca formal",
        "ninguno": "la regla no depende de si hay marca"}},
    "d23": {"nombre": "plataforma_formato", "valores": {
        "9:16": "vertical 9:16 (Reels, TikTok, Shorts)", "16:9": "horizontal 16:9 (YouTube, TV)", "1:1": "cuadrado 1:1",
        "4:5": "vertical 4:5 (feed)", "21:9": "cinemascope 21:9", "2:3_3:2": "foto 2:3 o 3:2",
        "ninguno": "la regla no depende de la plataforma ni del formato"}},
}
ABIERTAS_NINGUNO = {"d5": "la regla no trata de paleta ni grade de color", "d6": "la regla no trata de encuadre, lente ni profundidad de campo",
                    "d7": "la regla no trata de la iluminación"}
EXISTENTES = ("d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9")
TODAS = EXISTENTES + tuple(NUEVAS)
LOTE = 10

SIS = """Clasificas reglas de producción de imagen y video con IA en una taxonomía de facetas. Para CADA regla y CADA
dimensión devuelve la lista de valores (uno o varios, SOLO del vocabulario dado) que describen en qué piezas se aplica la
regla. Usa "ninguno" cuando la regla no depende de esa dimensión (es general respecto de ella). No inventes valores.
Juzga por el texto de la regla y su archivo/sección: una regla del skill de retrato habla de personas aunque no lo diga.
Además da "caso" (lista de códigos de caso) sólo si se pide para esa regla.
Responde SOLO JSON: {"reglas":[{"id":"...","d1":["..."],...,"d23":["..."],"caso":["..."]}]} con TODAS las dimensiones del vocabulario para cada regla."""


def ahora():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def vocabulario(con) -> dict:
    voc = {}
    for dim in EXISTENTES:
        voc[dim] = {v: d for v, d in con.execute("SELECT valor, descripcion FROM facetas_catalogo WHERE dimension=?", (dim,))}
        if dim in ABIERTAS_NINGUNO:
            voc[dim]["ninguno"] = ABIERTAS_NINGUNO[dim]
    for dim, x in NUEVAS.items():
        voc[dim] = dict(x["valores"])
    return voc


def knn(con):
    ids = [r for r, in con.execute("SELECT regla_id FROM embeddings ORDER BY regla_id")]
    M = np.stack([np.frombuffer(b, dtype="<f4") for _, b in con.execute("SELECT regla_id, vector FROM embeddings ORDER BY regla_id")])
    return ids, {r: i for i, r in enumerate(ids)}, M


def votar_knn(rid, etiquetas: dict, ids, idx, M, k=7):
    """Valor más votado por los k vecinos etiquetados (peso = coseno) y su proporción."""
    lab = [r for r in etiquetas if r != rid]
    if not lab:
        return None, 0.0
    li = np.array([idx[r] for r in lab])
    s = M[li] @ M[idx[rid]]
    top = np.argsort(-s)[:k]
    votos = collections.Counter()
    for j in top:
        for v in etiquetas[lab[j]]:
            votos[v] += float(s[j])
    v, w = votos.most_common(1)[0]
    return v, w / sum(votos.values())


def pedir_lote(reglas, voc, casos_voc, pide_caso, variante, extra="") -> dict:
    p = llm.proveedor()
    orden = list(reglas)
    random.Random(variante).shuffle(orden)
    cuerpo = {"vocabulario": {d: voc[d] for d in TODAS},
              "casos": casos_voc,
              "reglas": [{"id": r["id"], "archivo": f"{r['skill']}/{r['archivo']}", "seccion": r["seccion"], "medio": r["medio"],
                          "texto": r["texto"][:700], "pedir_caso": r["id"] in pide_caso} for r in orden]}
    usuario = json.dumps(cuerpo, ensure_ascii=False) + extra
    esperados = {r["id"] for r in reglas}
    for intento in range(4):
        try:
            res = p.completar(SIS + ("\nSegunda opinión independiente: decide sin asumir ninguna clasificación previa." if variante == "B" else ""), usuario)
            j = llm.extraer_json(res["texto"])
            filas = {str(x.get("id")): x for x in j.get("reglas", [])}
            errores = []
            if set(filas) != esperados:
                errores.append(f"ids esperados {sorted(esperados)}; faltan {sorted(esperados - set(filas))}; sobran {sorted(set(filas) - esperados)}")
            out = {}
            for rid in esperados & set(filas):
                x = filas[rid]
                o = {}
                for d in TODAS:
                    vals = x.get(d)
                    vals = [vals] if isinstance(vals, str) else (vals or [])
                    malos = [v for v in vals if v not in voc[d]]
                    if not vals or malos:
                        errores.append(f"{rid}.{d}: {vals} no está en el vocabulario" if malos else f"{rid}.{d}: vacío")
                    o[d] = sorted(set(vals))
                if rid in pide_caso:
                    cs = x.get("caso") or []
                    cs = [cs] if isinstance(cs, str) else cs
                    if not cs or any(c not in casos_voc for c in cs):
                        errores.append(f"{rid}.caso: {cs} inválido")
                    o["caso"] = sorted(set(cs))
                out[rid] = o
            if not errores:
                return out
            usuario += "\n\nRECHAZADA: " + "; ".join(errores[:30]) + ". Corrige y responde de nuevo con todas las reglas."
        except Exception as ex:  # noqa: BLE001
            usuario += f"\n\nRECHAZADA: {type(ex).__name__}. Responde sólo JSON válido."
    raise RuntimeError(f"lote sin respuesta válida tras 4 intentos: {sorted(esperados)[:3]}…")


def correr_pasada(reglas, voc, casos_voc, pide_caso, variante, cache: Path, paralelo=6) -> dict:
    hecho = json.loads(cache.read_text()) if cache.exists() else {}
    pendientes = [r for r in reglas if r["id"] not in hecho]
    lotes = [pendientes[i:i + LOTE] for i in range(0, len(pendientes), LOTE)]
    mu = threading.Lock()
    t0 = time.time()

    def uno(lote):
        try:
            return lote, pedir_lote(lote, voc, casos_voc, pide_caso, variante)
        except RuntimeError:  # lote problemático: se parte en reglas sueltas hasta que cada una valide
            out = {}
            for r in lote:
                out.update(pedir_lote([r], voc, casos_voc, pide_caso, variante))
            return lote, out

    n = 0
    with ThreadPoolExecutor(max_workers=paralelo) as ex:
        for f in as_completed([ex.submit(uno, l) for l in lotes]):
            lote, out = f.result()
            with mu:
                hecho.update(out)
                cache.write_text(json.dumps(hecho, ensure_ascii=False))
                n += 1
                print(f"  pasada {variante}: lote {n}/{len(lotes)} · {len(hecho)}/{len(reglas)} reglas · {time.time() - t0:.0f}s", flush=True)
    return hecho


def desempatar(rid, regla, dim, opciones, voc, casos_voc):
    """Tercera pasada: elige entre las opciones ya propuestas (vector, A, B)."""
    p = llm.proveedor()
    vocd = casos_voc if dim == "caso" else voc[dim]
    usuario = json.dumps({"regla": {"id": rid, "archivo": f"{regla['skill']}/{regla['archivo']}", "seccion": regla["seccion"],
                                    "texto": regla["texto"][:900]}, "dimension": dim, "vocabulario": vocd,
                          "opciones_propuestas": opciones}, ensure_ascii=False)
    sis = ("Eres el árbitro final de una clasificación. Dos o tres clasificadores discrepan. Lee la regla y elige la lista de "
           "valores correcta SOLO del vocabulario dado (puede ser una de las opciones o su unión/intersección). 'ninguno' si la regla "
           'no depende de esa dimensión. Responde SOLO JSON: {"valores":["..."],"razon":"..."}')
    for _ in range(4):
        try:
            j = llm.extraer_json(p.completar(sis, usuario)["texto"])
            vals = j.get("valores") or []
            vals = [vals] if isinstance(vals, str) else vals
            if vals and all(v in vocd for v in vals):
                return sorted(set(vals)), j.get("razon", "")
            usuario += f"\n\nRECHAZADA: {vals} fuera del vocabulario."
        except Exception as ex:  # noqa: BLE001
            usuario += f"\n\nRECHAZADA: {type(ex).__name__}."
    raise RuntimeError(f"desempate imposible {rid}.{dim}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="apd/data/rules.sqlite")
    ap.add_argument("--cache", default=str(AQUI.parent / "data" / "clasificacion_cache"))
    ap.add_argument("--escribir", action="store_true", help="escribe en rules.sqlite y exporta apd/data/clasificacion_completa.json")
    a = ap.parse_args()
    cache = Path(a.cache)
    cache.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(a.db)
    reglas = [dict(zip(("id", "skill", "archivo", "seccion", "texto", "medio"), r))
              for r in con.execute("SELECT id, skill, archivo, seccion, texto, medio FROM reglas ORDER BY id")]
    por_id = {r["id"]: r for r in reglas}
    voc = vocabulario(con)
    casos_voc = {c: d for c, d in con.execute("SELECT codigo, descripcion FROM casos")}
    etiq = collections.defaultdict(lambda: collections.defaultdict(set))
    for rid, d, v in con.execute("SELECT regla_id, dimension, valor FROM regla_faceta"):
        etiq[d][rid].add(v)
    for rid, cs in con.execute("SELECT regla_id, caso FROM regla_caso"):
        etiq["caso"][rid].add(cs)
    pide_caso = {r["id"] for r in reglas if r["id"] not in etiq["caso"]}
    faltan = {d: [r["id"] for r in reglas if r["id"] not in etiq[d]] for d in TODAS}
    faltan["caso"] = sorted(pide_caso)
    print("pendientes antes:", {d: len(v) for d, v in faltan.items()}, flush=True)

    A = correr_pasada(reglas, voc, casos_voc, pide_caso, "A", cache / "pasada_A.json")
    B = correr_pasada(reglas, voc, casos_voc, pide_caso, "B", cache / "pasada_B.json")

    # calibración del juez: acuerdo de la pasada A con las etiquetas que ya existían
    calib = {}
    for d in EXISTENTES:
        ok = tot = 0
        for rid, vals in etiq[d].items():
            if rid in A:
                tot += 1
                ok += bool(set(A[rid][d]) & vals)
        calib[d] = {"acuerdo": ok, "total": tot}
    print("calibración pasada A vs etiquetas existentes:", {d: f"{x['acuerdo']}/{x['total']}" for d, x in calib.items()}, flush=True)

    ids, idx, M = knn(con)
    decisiones, desempates = [], []
    arbitrar = []
    for d, lista in faltan.items():
        for rid in lista:
            a_, b_ = set(A[rid][d]), set(B[rid][d])
            vec, share = (votar_knn(rid, etiq[d], ids, idx, M) if etiq[d] else (None, 0.0))
            if vec and vec in a_:
                decisiones.append((rid, d, sorted(a_ & {vec} | (a_ & b_)), "vector+llm", {"vector": [vec, round(share, 3)], "A": sorted(a_), "B": sorted(b_)}))
            elif a_ & b_:
                decisiones.append((rid, d, sorted(a_ & b_), "llm2", {"vector": [vec, round(share, 3)], "A": sorted(a_), "B": sorted(b_)}))
            else:
                arbitrar.append((rid, d, {"vector": vec, "A": sorted(a_), "B": sorted(b_)}))
    print(f"acuerdo directo: {len(decisiones)} · a desempate: {len(arbitrar)}", flush=True)
    cdes = cache / "desempates.json"
    hechos = json.loads(cdes.read_text()) if cdes.exists() else {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(desempatar, rid, por_id[rid], d, op, voc, casos_voc): (rid, d, op)
                for rid, d, op in arbitrar if f"{rid}|{d}" not in hechos}
        for f in as_completed(futs):
            rid, d, op = futs[f]
            vals, razon = f.result()
            hechos[f"{rid}|{d}"] = {"valores": vals, "razon": razon, "opciones": op}
            cdes.write_text(json.dumps(hechos, ensure_ascii=False))
    for rid, d, op in arbitrar:
        h = hechos[f"{rid}|{d}"]
        decisiones.append((rid, d, h["valores"], "llm_desempate", {**op, "razon": h["razon"]}))

    # comprobación de exhaustividad antes de escribir: cada (regla, dimensión) pendiente tiene al menos un valor
    cubiertos = {(rid, d) for rid, d, vals, *_ in decisiones if vals}
    residuo = [(rid, d) for d, lista in faltan.items() for rid in lista if (rid, d) not in cubiertos]
    print(f"decisiones: {len(decisiones)} · residuo: {len(residuo)}", flush=True)
    por_origen = collections.Counter(o for *_, o, _ in decisiones)
    print("por origen:", dict(por_origen), flush=True)
    resumen = {"fecha": ahora(), "pendientes_antes": {d: len(v) for d, v in faltan.items()}, "calibracion_juez": calib,
               "decisiones": len(decisiones), "residuo": len(residuo), "por_origen": dict(por_origen)}
    (cache / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1))
    if residuo:
        sys.exit(f"RESIDUO {len(residuo)}: no se escribe nada")
    if not a.escribir:
        return
    f = ahora()
    con.execute("CREATE TABLE IF NOT EXISTS clasificacion_auto (regla_id TEXT, dimension TEXT, valores TEXT, origen TEXT, "
                "evidencia TEXT, fecha TEXT, PRIMARY KEY (regla_id, dimension))")
    for dim, x in NUEVAS.items():
        for v, desc in x["valores"].items():
            con.execute("INSERT OR IGNORE INTO facetas_catalogo (dimension, valor, descripcion, cerrada) VALUES (?,?,?,1)", (dim, v, desc))
    for d, desc in ABIERTAS_NINGUNO.items():
        con.execute("INSERT OR IGNORE INTO facetas_catalogo (dimension, valor, descripcion, cerrada) VALUES (?,?,?,0)", (d, "ninguno", desc))
    for rid, d, vals, origen, ev in decisiones:
        con.execute("INSERT OR REPLACE INTO clasificacion_auto VALUES (?,?,?,?,?,?)", (rid, d, json.dumps(vals), origen, json.dumps(ev, ensure_ascii=False), f))
        for v in vals:
            if d == "caso":
                con.execute("INSERT OR IGNORE INTO regla_caso VALUES (?,?,?,?,?,?)", (rid, v, origen, 1.0, None, f))
            else:
                con.execute("INSERT OR IGNORE INTO regla_faceta VALUES (?,?,?,?,?)", (rid, d, v, origen, f))
    con.commit()
    export = [{"id": rid, "dimension": d, "valores": vals, "origen": o, "evidencia": ev} for rid, d, vals, o, ev in decisiones]
    (AQUI.parent / "data" / "clasificacion_completa.json").write_text(json.dumps({"resumen": resumen, "decisiones": export},
                                                                                ensure_ascii=False, indent=0))
    print("escrito en", a.db, flush=True)


if __name__ == "__main__":
    main()
