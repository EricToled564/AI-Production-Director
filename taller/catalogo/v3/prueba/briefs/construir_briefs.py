"""construir_briefs.py: tarea 3 del plan (PLAN_FINAL_PRUEBA.md §5). Briefs de los casos para la aprobación de Eric.

    python3 -I taller/catalogo/v3/prueba/briefs/construir_briefs.py

Por cada caso del lote escribe en `briefs/`:
- `Kxx.contrato.json`: instancia de CONTRATO_IMAGEN_ORQUESTACION (`entrada`, `procedencia_campos`, `modulos_activos`),
  sin `aprobacion_brief`, que se añade cuando Eric aprueba;
- `Kxx.caso.json`: caso del catálogo (`case.schema.json`), con `confirmado` y `aprobacion` en falso hasta la aprobación;
- para persona sin referencias (K01), `Kxx.armar.json`: el brief de `armar.py` (CLAUDE.md, paso 1);
- `LOTE_<n>.md`: el brief en español de cada caso, sus valores y lo inferido, con el sha256 que Eric aprueba.

Todos los valores que no vienen de una decisión de Eric son propuesta del sistema: van con origen
`inferencia_para_aprobacion` (contrato) e `INFERENCIA_PROPUESTA` (catálogo). Los de facetas que fija la lista de
casos aprobada (26 §16, §17) van con origen `herencia_aprobada` / `USUARIO`.

Controles (salen con código 1 si fallan):
- `verificar_templates.validate_instance(contrato, 'brief')` sin errores y `modelo.nombre` exactamente «GPT Image 2»;
- `casos/validar.py` sin más errores que los de aprobación pendiente («Dato propuesto sin confirmar», «Falta
  aprobación comprobable»);
- K01: `armar.py` acepta su brief (código 0);
- cada valor de faceta del caso es el de `prueba/casos.json`.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PRUEBA = AQUI.parent
CAT = PRUEBA.parents[1]
REPO = CAT.parents[1]
TPL = CAT / "fuentes_20261019/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/templates"
CASOS_CAT = CAT / "fuentes_20261019/CASOS_OPCIONES_TAXONOMIA_20261019/casos"
sys.path.insert(0, str(TPL))
from verificar_templates import validate_instance  # noqa: E402

_AP = AQUI / "aprobaciones.json"
APROBACIONES = json.loads(_AP.read_text(encoding="utf-8")) if _AP.exists() else {}
PLAN = {c["id"]: c for c in json.loads((PRUEBA / "casos.json").read_text(encoding="utf-8"))["casos"]}
OPCIONES = json.loads((CASOS_CAT / "catalogo_opciones.json").read_text(encoding="utf-8"))
ESQ = json.loads((CAT / "v2/esquema_taxonomia.json").read_text(encoding="utf-8"))
VALORES = {k: {v["valor"] if isinstance(v, dict) else v for v in f["valores"]} for k, f in ESQ["facetas"].items()}
SHA_TAX = json.loads((CASOS_CAT / "manifest_fuentes.json").read_text(encoding="utf-8"))["taxonomy"]["sha256"]
FUENTE_PROPUESTA = "propuesta del sistema para el caso {} (PLAN_FINAL_PRUEBA.md §4), para aprobación de Eric"
FUENTE_LISTA = "lista de casos aprobada por Eric (DECISIONES_ERIC_20261026 §16, §17; prueba/casos.json)"
MODELO = {"nombre": "GPT Image 2", "version": "gpt-image-2", "interfaz": "App de ChatGPT para escritorio"}
FACETA_RUTA = {"F04": "entrada.pieza.tipo", "F10": "entrada.operacion", "F11": "entrada.ancla.rol",
               "F13": "entrada.accion", "F14": "entrada.fisica.regimen", "F15": "entrada.sujetos.items[].clase",
               "F32": "entrada.selecciones_taxonomicas"}
FACETA_NOMBRE = {"F04": "F04 Tipo de pieza", "F10": "F10 Modo de generación", "F11": "F11 Rol del ancla",
                 "F13": "F13 Tipo de acción", "F14": "F14 Régimen físico", "F15": "F15 Sujeto",
                 "F32": "F32 Texto en la imagen (extensión 2026-10-23)"}

# Fotografía: módulo activo en todo caso que no es edición (CONTRATOS L775–790; plan §3).
LOTE_1 = {
 "K01": dict(
   brief="Rostro maestro T1 de una persona inventada (no real), para usarlo después como referencia de identidad en "
         "K10, K11, K12, K13 y K33. Mujer de unos 35 años, cara irregular y asimétrica, cabeza y hombros sobre fondo "
         "gris liso, luz dura rasante desde la izquierda que deja ver poros, piel documental sin retoque.",
   ratio="4:5", px=(1024, 1280), pieza=("retrato", "maestro de identidad de rostro para la prueba",
                                        "referencia de identidad para composición y anclas"),
   sujetos=[dict(id="mujer", clase="persona", descripcion="mujer de unos 35 años, cara irregular y algo asimétrica",
                 edad=35, genero="mujer", rasgos=["nariz con una ligera desviación", "ceja izquierda más alta",
                                                   "pecas irregulares en pómulos", "labios secos"],
                 cabello="castaño oscuro, corto a la altura de la mandíbula, con mechones sueltos",
                 vestuario="camiseta de algodón gris carbón de cuello redondo", expresion="neutra, boca cerrada",
                 posicion="centrada, cuerpo girado tres cuartos, mirada a cámara")],
   escena=dict(espacio="interior", entorno="estudio con fondo continuo gris claro liso"),
   camara=dict(plano="CU close-up", angulo="eye-level", efecto_optico="profundidad de campo corta",
               lente_intencion="85mm feel, sin distorsión de gran angular en la cara"),
   luz=dict(fuente="una sola luz dura", direccion="lateral desde la izquierda de cámara, rasante",
            dureza="dura", distribucion="el lado de sombra queda uno o dos pasos más oscuro, sin relleno",
            contraste="alto"),
   rostro=dict(ocupacion=0.35, detalles=["poros visibles", "rojeces en nariz y mejillas", "pigmento desigual"]),
   restricciones=["sin texto ni marcas de agua", "sin retoque ni piel de estudio", "una sola persona"],
   estilo=["documental"], representacion=["fotorrealista"],
   armar=dict(id="K01", ratio="4:5", pronombre="her", rostro_menor_20=False,
              escena="in a studio against a seamless light grey backdrop #C8C8C6.",
              elementos=["mujer", "fondo"],
              sujeto="A woman of about 35, head and shoulders (close-up), body turned three-quarters to camera, "
                     "looking into the lens with a neutral closed-mouth expression; an irregular, slightly "
                     "asymmetrical face with a faintly crooked nose and a higher left eyebrow, uneven freckles on the "
                     "cheekbones, dry lips, dark brown jaw-length hair with loose strands, a charcoal grey cotton "
                     "crew-neck t-shirt.",
              luz="One hard raking light from camera left grazes her face so pores, fine lines and dry lips cast "
                  "small shadows; the shadow side stays one to two stops darker, with no fill.",
              microdetalle="Individual loose hair strands catch the light; visible redness on the nose and cheeks "
                           "and uneven pigment; the cotton weave shows at the neckline.",
              camara="Eye-level camera, 85mm feel, shallow depth of field",
              paleta=[["light grey", "#C8C8C6"], ["charcoal", "#3A3B3C"], ["dark brown", "#3B2A20"]],
              uso="face master for identity references in later compositions",
              restriccion_extra="", libre_de="text and watermarks, with no retouching or studio gloss")),
 "K02": dict(
   brief="Placa vacía de un lugar genérico: bahía de mar abierto con oleaje suave al atardecer, nubes de tormenta "
         "entrando y una cortina de lluvia lejana iluminada por sol rasante. Sin personas ni barcos. Servirá de lugar "
         "para K11 (persona sobre el agua), de base para K14 (quitar objeto) y de estilo para K26.",
   ratio="3:2", px=(1536, 1024), pieza=("editorial", "placa de lugar para composición", "fondo de K11 y entrada de K14 y K26"),
   sujetos=[], escena=dict(espacio="exterior", entorno="bahía de mar abierto con oleaje suave y una boya "
                           "roja aislada a media distancia", momento="atardecer", clima="tormenta entrando, lluvia lejana",
                           planos=["primer plano de agua con textura de oleaje", "boya roja a media distancia",
                                   "horizonte con cortina de lluvia y nubes"]),
   camara=dict(plano="WS wide", angulo="eye-level", efecto_optico="todo nítido, sin desenfoque de fondo"),
   luz=dict(fuente="sol bajo bajo las nubes", direccion="contraluz lateral desde la derecha", dureza="dura en el agua, "
            "difusa en las nubes", distribucion="franjas de luz sobre el agua, cielo oscuro", contraste="alto"),
   restricciones=["sin personas", "sin barcos ni construcciones", "sin texto ni marcas de agua",
                  "una sola presión ambiental: la tormenta"],
   estilo=["documental"], representacion=["fotorrealista"]),
 "K03": dict(
   brief="Edificación real anclada por época y cultura, sin exigir geometría exacta: la fachada del Palacio de Bellas "
         "Artes de Ciudad de México en una mañana de los años cincuenta, vista desde la Alameda, con autos y "
         "transeúntes de la época a escala pequeña. Se verifica contra fotos reales lo que el brief declara.",
   ratio="3:2", px=(1536, 1024), pieza=("editorial", "fotografía de lugar real de época", "entrada de K15, K16 y K23"),
   sujetos=[dict(id="palacio", clase="edificación o landmark",
                 descripcion="Palacio de Bellas Artes, Ciudad de México: fachada de mármol blanco y cúpulas")],
   escena=dict(espacio="exterior", entorno="Alameda Central con árboles y avenida con autos de los años cincuenta",
               momento="media mañana", clima="despejado"),
   camara=dict(plano="WS wide", angulo="eye-level", efecto_optico="nitidez de cerca a lejos"),
   luz=dict(fuente="sol de media mañana", direccion="lateral desde la izquierda", dureza="dura",
            distribucion="fachada iluminada con sombras de cornisas", contraste="medio"),
   restricciones=["sin texto legible ni marcas de agua", "personas pequeñas sin rostro reconocible",
                  "no se exige geometría exacta del edificio"],
   estilo=["anclado en época, cultura o autor"], representacion=["fotorrealista"]),
 "K04": dict(
   brief="Animal real: retrato de cabeza de un zorro rojo (Vulpes vulpes) en nieve, mirando a cámara, con pelaje "
         "de invierno detallado. Primero cabeza y pelaje (INV-000480). Se verifica anatomía y pelaje contra fotos "
         "reales de la especie.",
   ratio="4:5", px=(1024, 1280), pieza=("editorial", "retrato de fauna", "artículo de naturaleza"),
   sujetos=[dict(id="zorro", clase="animal", descripcion="zorro rojo adulto, pelaje de invierno espeso, hocico blanco, "
                 "orejas con dorso negro", posicion="cabeza de frente, ligeramente girada")],
   escena=dict(espacio="exterior", entorno="bosque nevado desenfocado", momento="mañana", clima="nieve fina"),
   camara=dict(plano="CU close-up", angulo="eye-level", altura="a la altura de la cabeza del animal", efecto_optico="profundidad de campo corta",
               lente_intencion="teleobjetivo, fondo comprimido"),
   luz=dict(fuente="sol bajo", direccion="lateral trasera desde la derecha", dureza="dura con borde en el pelaje",
            distribucion="rim de luz en el contorno del pelaje", contraste="medio"),
   restricciones=["sin texto ni marcas de agua", "anatomía de la especie real"],
   estilo=["documental"], representacion=["fotorrealista"]),
 "K05": dict(
   brief="Producto genérico sin marca: un vaso de vidrio liso y vacío, en hero frontal sobre fondo blanco limpio, "
         "para catálogo. Es la base de K24 (relleno con física) y del contenido de K26.",
   ratio="1:1", px=(1024, 1024), pieza=("e-commerce o catálogo", "foto de producto hero", "ficha de catálogo"),
   sujetos=[dict(id="vaso", clase="producto", descripcion="vaso de vidrio transparente, recto, liso, sin marca ni "
                 "grabado, vacío", posicion="centrado, frontal")],
   escena=dict(espacio="interior", entorno="estudio con fondo blanco opaco y superficie blanca"),
   camara=dict(plano="objeto entero", angulo="eye-level", altura="frontal, a la altura del vaso", efecto_optico="nitidez total"),
   luz=dict(fuente="dos ventanas de luz", direccion="laterales y una luz trasera", dureza="suave",
            distribucion="bordes del vidrio definidos por reflejos verticales", contraste="medio"),
   restricciones=["sin marca, logo ni texto", "un solo vaso", "sombra de contacto suave"],
   estilo=["comercial pulido"], representacion=["fotorrealista"]),
 "K06": dict(
   brief="Objeto en el instante pico: una pelota de tenis aplastada contra las cuerdas de una raqueta en el impacto, "
         "con pelusa de fieltro y polvo de arcilla saliendo, a contraluz. Solo la raqueta y la pelota, sin manos.",
   ratio="3:2", px=(1536, 1024), pieza=("key visual de campaña", "imagen de impacto", "key visual de una campaña deportiva"),
   sujetos=[dict(id="pelota", clase="objeto o prop", descripcion="pelota de tenis amarilla deformada contra las cuerdas, "
                 "fieltro erizado"), dict(id="raqueta", clase="objeto o prop", descripcion="marco de raqueta oscuro "
                 "sin marca con cuerdas deflectadas")],
   escena=dict(espacio="exterior", entorno="cancha de arcilla desenfocada", momento="tarde"),
   accion=dict(tipo="B instante pico", estado_visible="la pelota ya aplastada contra las cuerdas, cuerdas cediendo",
               evidencia_fisica=["pelusa de fieltro y polvo de arcilla en el aire", "cuerdas deflectadas"]),
   fisica=["04 objeto balístico"],
   camara=dict(plano="ECU extreme close-up", angulo="eye-level", altura="a la altura del punto de impacto", efecto_optico="profundidad de campo muy "
               "corta, macro", lente_intencion="macro"),
   luz=dict(fuente="sol bajo", direccion="contraluz", dureza="dura", distribucion="polvo y pelusa iluminados en el borde",
            contraste="alto"),
   restricciones=["sin manos ni personas", "sin marca, logo ni texto", "una sola pelota y una sola sombra"],
   estilo=["comercial pulido"], representacion=["fotorrealista"]),
 "K07": dict(
   brief="Planta real: un agave azul (Agave tequilana) maduro en un campo de Jalisco, con hojas azul grisáceo y "
         "espinas terminales, al amanecer. Se verifica contra fotos reales de la especie.",
   ratio="4:5", px=(1024, 1280), pieza=("editorial", "retrato de especie vegetal", "artículo sobre agricultura"),
   sujetos=[dict(id="agave", clase="planta o especie vegetal", descripcion="agave azul maduro, roseta de hojas "
                 "rígidas azul grisáceo con espinas en la punta y bordes dentados", posicion="centrado en primer plano")],
   escena=dict(espacio="exterior", entorno="campo con hileras de agaves y cerros al fondo, tierra roja", momento="amanecer",
               clima="despejado con bruma baja"),
   camara=dict(plano="MS medium", angulo="high", altura="ligeramente por encima de la planta", efecto_optico="fondo con desenfoque moderado"),
   luz=dict(fuente="sol al amanecer", direccion="lateral desde la izquierda", dureza="dura",
            distribucion="bordes de las hojas iluminados, bruma en el fondo", contraste="medio"),
   restricciones=["sin personas", "sin texto ni marcas de agua", "anatomía de la especie real"],
   estilo=["documental"], representacion=["fotorrealista"]),
 "K08": dict(
   brief="Texto corto del mundo: la fachada de una panadería de barrio con un letrero de madera pintado a mano que "
         "dice «Panadería». No es una marca real. Luz de primera hora. Pieza: miniatura; el titular de la "
         "miniatura se compone aparte. Es la entrada de K25 (adaptación a otro mercado).",
   ratio="16:9", px=(1536, 864), pieza=("miniatura", "foto con texto en el mundo", "miniatura de video; titular aparte"),
   sujetos=[dict(id="fachada", clase="lugar genérico", descripcion="fachada de panadería con puerta de madera y "
                 "escaparate con pan")],
   escena=dict(espacio="exterior", entorno="calle empedrada tranquila", momento="primera hora de la mañana"),
   camara=dict(plano="WS wide", angulo="eye-level", efecto_optico="letrero nítido"),
   luz=dict(fuente="sol bajo", direccion="lateral desde la derecha", dureza="dura", distribucion="letrero iluminado",
            contraste="medio"),
   texto_marca=dict(literales=["Panadería"], posicion="letrero de madera sobre la puerta",
                    tipografia="letras serif blancas pintadas a mano"),
   restricciones=["no extra words, no duplicate text, no watermarks", "el único texto es el letrero",
                  "ninguna marca real"],
   estilo=["documental"], representacion=["fotorrealista"]),
 "K09": dict(
   brief="Texto pequeño del mundo: un frasco de miel con etiqueta genérica (no marca real) con texto pequeño: "
         "«Miel de azahar», «Peso neto 500 g», «Hecho en Veracruz». Sobre mesa de madera, para catálogo. Quality high. "
         "Es la entrada de K19 (traducir texto).",
   ratio="1:1", px=(1024, 1024), pieza=("e-commerce o catálogo", "producto con etiqueta", "ficha de catálogo"),
   sujetos=[dict(id="frasco", clase="producto", descripcion="frasco de vidrio con miel ámbar, tapa metálica dorada lisa, "
                 "etiqueta de papel crema", posicion="centrado, etiqueta de frente")],
   escena=dict(espacio="interior", entorno="mesa de madera clara, fondo neutro desenfocado"),
   camara=dict(plano="objeto entero", angulo="eye-level", altura="frontal, a la altura de la etiqueta", efecto_optico="etiqueta nítida"),
   luz=dict(fuente="ventana", direccion="lateral desde la izquierda", dureza="suave", distribucion="miel translúcida "
            "iluminada", contraste="medio"),
   texto_marca=dict(literales=["Miel de azahar", "Peso neto 500 g", "Hecho en Veracruz"],
                    posicion="etiqueta frontal, nombre arriba y dos líneas pequeñas debajo",
                    tipografia="serif oscura sobre papel crema"),
   restricciones=["no extra words, no duplicate text, no watermarks", "texto legible al 100 %", "ninguna marca real"],
   estilo=["documental"], representacion=["fotorrealista"]),
}


def sha(v):
    return hashlib.sha256(json.dumps(v, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def opcion(faceta, valor):
    ids = [r["id"] for r in OPCIONES if r["facet"] == faceta and r["label"] == valor and r["case_selectable"]]
    return ids[:1]


def contrato(kid, d, p=None):
    p = p or PLAN[kid]
    e = {"ruta": {"flujo": "FL04", "paso": d.get("paso", "E5.2 génesis")}, "operacion": p["operacion"],
         "modelo": dict(MODELO),
         "pieza": dict(zip(("tipo", "objetivo", "uso"), d["pieza"])),
         "formato": {"ratio": d["ratio"], "ancho_px": d["px"][0], "alto_px": d["px"][1]}, "idioma_prompt": "en",
         "escena": d["escena"], "camara": d["camara"], "luz": d["luz"], "restricciones": d["restricciones"],
         "estilo": d["estilo"], "representacion": d["representacion"],
         "sujetos": {"cantidad": len(d["sujetos"]), "items": d["sujetos"]}}
    for k in ("rostro", "texto_marca", "identidad", "composicion", "blocking"):
        if k in d:
            e[k] = d[k]
    if "accion" in d:
        e["accion"] = d["accion"]
        e["fisica"] = {"regimen": d["fisica"]}
    sel = [f"F10: {p['F10']}", f"F15: {p['F15']}", f"F32: {p['F32']}", f"F04: {p['F04']}", "F29: GPT Image 2",
           "F18: fotorrealista"]
    sel += [f"{f}: {p[f]}" for f in ("F11", "F13", "F14") if p[f]]
    sel += [f"F16: {d['escena']['espacio']}"]
    sel += [f"F24: {v}" for v in d.get("f24", [d["camara"]["plano"]])]
    sel += [f"F25: {v}" for v in d.get("f25", [d["camara"]["angulo"]])]
    sel += [f"F17: {v}" for v in d["estilo"]]
    e["selecciones_taxonomicas"] = sel
    modulos = ["fotografia"] + (["sujetos_visibles"] if d["sujetos"] else []) + (["accion_fisica"] if "accion" in d else [])
    e["modulos_activos"] = modulos
    proc = []
    lista = {"entrada.operacion", "entrada.pieza.tipo", "entrada.selecciones_taxonomicas", "entrada.modelo.nombre",
             "entrada.modelo.version", "entrada.modelo.interfaz", "entrada.idioma_prompt", "entrada.modulos_activos"}

    def add(path, val):
        heredado = path in lista
        proc.append({"path": path, "origen": "herencia_aprobada" if heredado else "inferencia_para_aprobacion",
                     "fuente": FUENTE_LISTA if heredado else FUENTE_PROPUESTA.format(kid),
                     "valor_sha256": sha(val), "aprobacion_id": ""})
    planas = {"entrada.ruta.flujo": e["ruta"]["flujo"], "entrada.ruta.paso": e["ruta"]["paso"],
              "entrada.operacion": e["operacion"], "entrada.modelo.nombre": MODELO["nombre"],
              "entrada.modelo.version": MODELO["version"], "entrada.modelo.interfaz": MODELO["interfaz"],
              "entrada.pieza.tipo": e["pieza"]["tipo"], "entrada.pieza.objetivo": e["pieza"]["objetivo"],
              "entrada.pieza.uso": e["pieza"]["uso"], "entrada.formato.ratio": d["ratio"],
              "entrada.formato.ancho_px": d["px"][0], "entrada.formato.alto_px": d["px"][1],
              "entrada.idioma_prompt": "en", "entrada.restricciones": d["restricciones"],
              "entrada.selecciones_taxonomicas": sel, "entrada.sujetos": e["sujetos"], "entrada.escena": d["escena"],
              "entrada.estilo": d["estilo"], "entrada.representacion": d["representacion"],
              "entrada.modulos_activos": modulos}
    for k, v in d["camara"].items():
        planas[f"entrada.camara.{k}"] = v
    for k, v in d["luz"].items():
        planas[f"entrada.luz.{k}"] = v
    for k in ("rostro", "texto_marca", "identidad", "composicion", "blocking"):
        if k in d:
            planas[f"entrada.{k}"] = d[k]
    if "accion" in d:
        planas["entrada.accion"] = d["accion"]
        planas["entrada.fisica.regimen"] = d["fisica"]
    for path, val in planas.items():
        add(path, val)
    return {"contrato_id": f"{kid}:{d.get('plantilla_id', 'T-GENESIS')}+GPT2-GEN", "version": "20261019", "entrada": e,
            "procedencia_campos": proc}


def caso_catalogo(kid, d, x, p=None):
    p = p or PLAN[kid]
    campos = []
    for f in ("F04", "F10", "F11", "F13", "F14", "F15", "F32"):
        v = p[f]
        if not v:
            continue
        ids = opcion(f, v)
        campos.append({"path": FACETA_RUTA[f], "valor": v, "origen": "USUARIO", "option_ids": ids,
                       "evidencia": FUENTE_LISTA if ids else FUENTE_LISTA + "; valor de extensión aprobada sin id en el "
                       "catálogo (DECISIONES_ERIC_20261023 §4)", "confirmado": False})
    for path in ("entrada.escena", "entrada.camara", "entrada.luz", "entrada.sujetos", "entrada.formato.ratio"):
        node = x["entrada"]
        for part in path.split(".")[1:]:
            node = node[part]
        campos.append({"path": path, "valor": node, "origen": "INFERENCIA_PROPUESTA", "option_ids": [],
                       "evidencia": FUENTE_PROPUESTA.format(kid), "confirmado": False})
    req = [{"path": r, "motivo": "campo exigido por T-GENESIS o el módulo fotografía", "resuelto": True}
           for r in ("entrada.sujetos", "entrada.escena", "entrada.camara.plano", "entrada.luz.fuente")]
    req += d.get("requisitos", [])
    return {"case_id": kid, "taxonomy_sha256": SHA_TAX, "brief_literal": d["brief"], "campos": campos,
            "requisitos_de_completitud": req, "aprobacion": {"aprobado": False, "evidencia": ""}}


def brief_sha(x):
    return hashlib.sha256(json.dumps(x["entrada"], ensure_ascii=False, sort_keys=True, separators=(",", ":"))
                          .encode()).hexdigest()


def validar_caso(path):
    p = subprocess.run([sys.executable, "-I", "-c", f"import sys,runpy; sys.argv=['validar.py', {str(path)!r}]; "
                        f"sys.path.insert(0, {str(CASOS_CAT)!r}); runpy.run_path({str(CASOS_CAT / 'validar.py')!r}, "
                        f"run_name='__main__')"], capture_output=True, text=True)
    return json.loads(p.stdout)["case_gate_errors"]


def main():
    fallas, md = [], ["# Lote 1 de briefs: génesis K01–K09 (tarea 3)", "",
                      "Cada caso se aprueba por su sha256 (serialización de `verificar_templates.py`). Todo lo que no",
                      "viene de la lista de casos aprobada (26 §16) es propuesta del sistema: Eric aprueba, cambia o quita.",
                      "Las personas, lugares y objetos de los briefs son inventados, salvo los sujetos reales de K03, K04 y",
                      "K07, que se verifican contra fotos reales.", ""]
    aprobados = []
    for kid, d in LOTE_1.items():
        x = contrato(kid, d)
        errs = validate_instance(x, "brief")
        for sv in x["entrada"]["selecciones_taxonomicas"]:
            fac, val = sv.split(": ", 1)
            if fac in VALORES and val not in VALORES[fac]:
                errs.append(f"{fac} «{val}» no está en el esquema")
        if x["entrada"]["modelo"]["nombre"] != "GPT Image 2":
            errs.append("modelo.nombre distinto de «GPT Image 2»")
        c = caso_catalogo(kid, d, x)
        # Aprobación de Eric ligada al sha256 del brief (T-BRIEF-IMG L13–15): solo vale si el brief no cambió.
        ap = APROBACIONES.get(kid)
        aprobado = bool(ap) and ap["brief_sha256"] == brief_sha(x)
        if ap and not aprobado:
            print(f"  aviso {kid}: el brief cambió desde su aprobación; la aprobación queda invalidada")
        if aprobado:
            x["aprobacion_brief"] = {"aprobado": True, "mensaje_id": ap["mensaje_id"], "brief_sha256": ap["brief_sha256"]}
            for pc in x["procedencia_campos"]:
                pc["aprobacion_id"] = ap["mensaje_id"]
            for campo in c["campos"]:
                campo["confirmado"] = True
            c["aprobacion"] = {"aprobado": True, "evidencia": f"mensaje {ap['mensaje_id']} ({ap['fecha']}): "
                               f"«{ap['texto']}» sobre {ap['documento']}; sha256 {ap['brief_sha256']}"}
            errs += validate_instance(x, "seleccion")
        if errs:
            fallas.append(f"{kid} contrato: {errs}")
        (AQUI / f"{kid}.contrato.json").write_text(json.dumps(x, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        cp = AQUI / f"{kid}.caso.json"
        cp.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        pendiente = () if aprobado else ("Dato propuesto sin confirmar", "Falta aprobación")
        resto = [e for e in validar_caso(cp) if not e.startswith(pendiente)] if pendiente else validar_caso(cp)
        if resto:
            fallas.append(f"{kid} caso: {resto}")
        aprobados.append(kid) if aprobado else None
        if "armar" in d:
            ap = AQUI / kid / "briefs.json"
            ap.parent.mkdir(exist_ok=True)
            ap.write_text(json.dumps([d["armar"]], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", str(REPO / "produccion/template-retrato-gpt2/armar.py"), str(ap)],
                               capture_output=True, text=True)
            (ap.parent / "PROMPTS.txt").unlink(missing_ok=True)  # el prompt es de la tarea 9; aquí solo se valida
            if r.returncode != 0:
                fallas.append(f"{kid} armar.py: {r.stdout.strip()}")
        p = PLAN[kid]
        e = x["entrada"]
        md += [f"## {kid} · {p['descripcion']}", "", d["brief"], "",
               f"- Facetas (lista aprobada): F10 {p['F10']} · F15 {p['F15']} · F32 {p['F32']} · F04 {p['F04']}"
               + "".join(f" · {f} {p[f]}" for f in ("F11", "F13", "F14") if p[f]),
               f"- Formato: {d['ratio']} · tamaño de referencia {d['px'][0]}x{d['px'][1]} · quality {p['quality']}",
               f"- Propuesto por el sistema (inferencia para aprobación): escena {json.dumps(e['escena'], ensure_ascii=False)}; "
               f"cámara {json.dumps(e['camara'], ensure_ascii=False)}; luz {json.dumps(e['luz'], ensure_ascii=False)}; "
               f"sujetos {json.dumps(e['sujetos']['items'], ensure_ascii=False)}"
               + (f"; texto {json.dumps(e['texto_marca'], ensure_ascii=False)}" if "texto_marca" in e else "")
               + (f"; rostro {json.dumps(e['rostro'], ensure_ascii=False)}" if "rostro" in e else ""),
               f"- Restricciones: {'; '.join(d['restricciones'])}",
               f"- Módulos activos: {', '.join(e['modulos_activos'])}",
               f"- **sha256 del brief:** `{brief_sha(x)}`", ""]
    (AQUI / "LOTE_1.md").write_text("\n".join(md), encoding="utf-8")
    for f in fallas:
        print("  FALLA", f)
    print(f"lote 1: {len(LOTE_1)} casos · aprobados {len(aprobados)} · " + ("OK" if not fallas else f"{len(fallas)} fallas"))
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
