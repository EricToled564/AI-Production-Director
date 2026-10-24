"""Veredictos del lote 07 (pasada única, revisión manual del agente principal tras detener los revisores).

Cada línea del lote tiene una decisión escrita aquí a mano, por número de línea de su documento. El script falla
si una unidad del lote no tiene decisión o si una decisión cita una línea que no existe.
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parents[1]
C = ["B1", "B2", "B3", "B4", "B5"]


def S(m):
    return {"tipo": "sin contenido normativo", "motivo": m}


def A(ef, epc=None, solo=None, fuera=None):
    aplica = solo or C
    r = {"tipo": "normativo", "aplica": list(aplica), "fuera": {c: fuera[c] for c in C if c not in aplica} if fuera
         else {}, "efecto": ef}
    if epc:
        r["efecto_por_caso"] = epc
    return r


def F(m):
    return {"tipo": "normativo", "aplica": [], "fuera": {c: m for c in C}}


def rango(a, b, v):
    return {n: v for n in range(a, b + 1)}


H = S("encabezado de sección")
TAB = S("cabecera o separador de tabla")
FM = S("frontmatter del skill: nombre y descripción de activación")
FENCE = S("delimitador de bloque de código")
NOTX = {"B2": "uso página «equipo» de web corporativa: la foto no lleva texto compuesto encima",
        "B4": "ilustración de artículo: la foto no lleva texto compuesto encima"}

# ---------------------------------------------------------------- produccion-visual-sw30/SKILL.md
SW = {}
SW.update(rango(1, 4, S("frontmatter; el micro-gate que menciona la descripción está regulado en las líneas 106–113")))
SW[6] = H
SW[8] = A("Objetivo que gobierna cada decisión: máxima calidad de imagen conforme al brief al menor costo de generación.")
SW[9] = A("La fuente de verdad del caso es casos.json (equivale al production-package): nada del prompt lo contradice.")
SW[11] = H
SW.update(rango(12, 16, A("Gate de entrega: antes de entregar los prompts se responde honestamente SÍ o NO a «¿usaste de forma "
                          "exhaustiva y correcta todas las reglas aplicables a este caso?»; solo se entrega con SÍ sin matices.")))
SW[18] = S("rótulo «Reglas de uso:» que introduce 19–30")
SW.update(rango(19, 23, A("La pregunta de avance se responde antes de entregar; con NO no se entrega y se completa lo que falte; "
                          "prohibido el SÍ complaciente o con matices.")))
SW.update(rango(24, 27, A("«Exhaustiva» = leídos completos todos los archivos aplicables; «correcta» = cada regla verificable corre "
                          "en un verificador ejecutable (verificar.py, cruzar.py traza, validar_prompts.py) y las demás se "
                          "contrastan una a una.")))
SW.update(rango(28, 29, A("Ante duda sobre si un archivo aplica, leer su sección «cuándo cargar» en vez de decidir por criterio propio.")))
SW[30] = A("Solo se pregunta a Eric por dirección creativa, no por reglas.")
SW[32] = H
SW[33] = A("Nunca escribir el prompt de corrido ni parchear texto: catalogar, definir secciones y ensamblar por sección.")
SW.update(rango(35, 36, A("Catalogar: el conjunto de reglas aplicables del caso es seleccion.json (equivalente a RULES_MATRIX.md).")))
SW.update(rango(37, 38, A("Tipo del caso: retrato de una persona por génesis sin referencia; el más cercano de SW30 es T1 (rostro "
                          "protagonista sin referencia), del que se aplican los bloques transferibles de piel y luz (71–77).")))
SW.update(rango(39, 41, A("Antes de redactar, listar las secciones; cada regla vive en un bloque nombrado y compartido entre los "
                          "cinco prompts (optics, skin, anatomy, unique, colour, hair, fabric, clean), nunca como texto suelto.")))
SW.update(rango(42, 45, A("Ensamblar P(scene, subject, details, mood, usecase, constraints) = los 5 slots de GPT2-GEN; salida con "
                          "cabecera Model/Quality/Size + References + «Prompt:» + «Notes:» fuera del cuerpo del prompt.")))
SW[47] = H
SW.update(rango(48, 50, S("diagnóstico histórico de la causa raíz (12% de cobertura); la regla operativa está en 52–58")))
SW.update(rango(52, 53, A("Extraer mecánicamente cada enunciado de la fuente: cumplido por construir_universo.py (una línea no vacía = "
                          "un texto, sin filtro léxico).")))
SW.update(rango(54, 55, A("Cada regla aplicable con disposición explícita y salida con código 1 si queda una sin disponer: "
                          "verificar.py por lote y cruzar.py traza por caso.")))
SW[56] = A("Verificar los prompts columna por columna con un validador ejecutable (validar_prompts.py).")
SW[58] = A("Gate de cobertura: no se emiten prompts si la traza no cierra al 100% (cruzar.py traza con exit 0).")
SW.update(rango(59, 60, S("estado medido del proyecto SW30 en su fecha; descriptivo")))
SW.update(rango(62, 63, A("Si Eric detecta un defecto en una imagen, su regla se añade al registro con su verificación en el mismo turno.")))
SW[65] = H
SW.update(rango(66, 67, A("Los cuatro bloques canónicos de rostro (light_hard, skin_doc, usecase_doc, clean_doc) se aplican en su "
                          "contenido transferible a un retrato final (ver 71–74); no se sustituyen por luz suave de estudio ni por "
                          "Portra.")))
SW[69] = TAB
SW[70] = TAB
SW[71] = A("light_hard: luz dura rasante sin relleno para que los poros proyecten sombra; prohibida la luz de softbox en rostros.",
           epc={"B1": "sol bajo lateral rasante, lado en sombra sin relleno (no fill light)",
                "B2": "el brief pide luz suave de ventana: la ventana es la única fuente, direccional desde un lado, el lado "
                      "opuesto cae a sombra sin relleno; nada de softbox ni luz frontal pareja",
                "B3": "luz cenital dura del gimnasio sin relleno: sombras bajo cejas, nariz y pómulos",
                "B4": "la lámpara cálida es la única fuente, pequeña y dura, sin relleno; el resto de la cocina cae a sombra",
                "B5": "contraluz duro de escenario que dibuja el perfil con rim; sin relleno frontal"})
SW[72] = A("skin_doc: describir defectos concretos de piel, no «imperfecciones sutiles».",
           epc={"B1": "piel curtida por sol y sal: arrugas profundas, manchas solares, rojeces en pómulos, descamación en labios",
                "B2": "poros visibles en nariz y frente, pelos de barba individuales, leve rojez alrededor de la nariz",
                "B3": "sudor en gotas y película en frente y cuello, rojez por esfuerzo, poros abiertos",
                "B4": "pigmento desigual, poros visibles, ojeras leves, sin maquillaje de estudio",
                "B5": "arrugas profundas, manchas de edad, pelos de barba gris individuales, piel fina en el cuello"})
SW[73] = A("usecase_doc: registro de fotografía documental de reportaje; nunca nombrar Kodak Portra (suaviza la piel). El stock "
           "Kodak Tri-X no se nombra porque es blanco y negro y la luz de cada brief se define por su color (amanecer, ventana, "
           "deporte bajo luz de gimnasio, lámpara cálida, escenario).")
SW[74] = A("clean_doc en Constraints: «no beauty retouching, no skin smoothing, no even complexion, no soft fill light».")
SW.update(rango(76, 77, A("Describir una cara irregular y asimétrica con rasgos concretos (nariz con caballete, cicatriz, ojos "
                          "hundidos, asimetrías); la cara regular y simétrica se lee como maniquí.")))
SW.update(rango(79, 80, A("Longitud del prompt alrededor de 250 palabras; ningún slot llega a 300.")))
SW[82] = H
SW.update(rango(83, 85, A("El prompt se instancia por secciones obligatorias en orden, no se escribe libre; validar_prompts.py rechaza "
                          "lo que no cumple.")))
SW[86] = A("Rechazar el prompt si falta una sección obligatoria (los 5 slots en orden).")
SW[87] = A("Rechazar el prompt si trae una sección no declarada por la plantilla.")
SW[88] = A("Las secciones que vienen de bloques compartidos no se reescriben como texto suelto en un prompt individual.")
SW[89] = A("Rechazar el prompt si falta el bloque Notes.")
SW[90] = A("Rechazar el prompt si Model/Quality/Size/aspect ratio aparecen dentro del cuerpo del prompt.")
SW.update(rango(91, 92, A("El validador se prueba con un prompt que debe fallar (prueba negativa) además de los prompts válidos.")))
SW[94] = H
SW.update(rango(95, 96, A("Un cambio se hace en el bloque compartido una vez y se propaga a los cinco prompts.")))
SW.update(rango(97, 98, A("Prohibido parchear el texto de un prompt individual para arreglar algo que vive en un bloque compartido.")))
SW[100] = H
SW.update(rango(101, 103, A("Validar: slots · anti-slop · ratio estándar · metadatos fuera del prompt · Notes · cámara con los 5 efectos "
                            "ópticos (compresión de focal, bokeh, viñeta, halación, grano) · mood · color · texto de marca ausente · "
                            "framing positivo · mirada · manos. Identity-lock no tiene objeto: persona ficticia sin identidad que "
                            "sostener.")))
SW[104] = A("Cualquier desviación de plantilla rompe la validación; no se entrega con el validador en rojo.")
SW[106] = H
SW.update(rango(107, 111, A("La entrega de los prompts abre con 3 líneas: SKILL (archivos y secciones leídos en este turno), RIESGOS "
                            "(qué puede fallar y qué línea lo mitiga), TÉCNICA (técnica probada y fuente, o «no encontrada»).")))
SW.update(rango(112, 113, A("Entrega sin cabecera de micro-gate es inválida; no se genera sin preflight de costo (Eric genera: 5 "
                            "prompts × quality high).")))
SW[115] = H
SW.update(rango(116, 117, A("Un solo trabajo por generación: una persona, un retrato, sin segundo sujeto.")))
SW.update(rango(118, 119, A("La posición del sujeto se declara por anclas legibles de la propia escena (el poste del muelle, el marco "
                            "del ventanal, la barra, la encimera, el foco), nunca «left half», «centre» ni «just left of X».")))
SW.update(rango(120, 121, F("génesis sin referencias: no hay edición ni editor (comunes.operacion)")))
SW[122] = F("génesis sin referencias: no hay referentes adjuntos para comparar «same X» (comunes.operacion)")
SW.update(rango(123, 124, F("sin referencia de persona: no hay nada que heredar (comunes.operacion)")))
SW.update(rango(125, 126, F("persona ficticia por génesis: no hay swap de identidad (comunes.sujetos)")))
SW.update(rango(127, 128, F("génesis de una persona en una pasada, sin placa ni inserción desde otra imagen (comunes.operacion)")))
SW[129] = A("Still en instante congelado: verbos de estado, nada de movimiento en curso («frozen», «holding», no «walking»).")
SW.update(rango(130, 131, F("una sola persona: no hay contacto entre personas (comunes.sujetos)")))
SW.update(rango(132, 133, A("Sin logos ni lettering: no hay asset de marca aprobado ni brand-lock (comunes.texto_en_imagen).")))
SW[134] = A("Si Eric aprueba una imagen, se registra con su hash junto al prompt exacto y su traza (biblioteca de la decisión 8).")
SW.update(rango(135, 136, F("una sola pasada por prompt sin edición posterior (comunes.generacion)")))
SW.update(rango(137, 138, F("una sola pasada por prompt: no hay segundo intento dentro de esta prueba (comunes.generacion)")))
SW.update(rango(139, 141, A("Validadores y techo de palabras en verde antes de entregar; la inspección al 100% de rostro y manos se hace "
                            "sobre la imagen generada y va al checklist de Eric; si algo falla no se entrega y se dice en una línea.")))
SW[142] = F("imagen suelta sin shots.json (comunes.medio)")
SW.update(rango(143, 144, F("imagen fija, no clip (comunes.medio)")))
SW.update(rango(145, 146, A("Entrega en unidad chica con el delta; toda regla nueva se aplica a los cinco prompts, no a una parte.")))
SW.update(rango(147, 148, A("Respuesta con el entregable en la primera línea; sin adulación; error = una línea de corrección.")))
SW.update(rango(149, 150, A("No afirmar capacidades de GPT Image 2 (p. ej. parámetro style) sin verificarlas en la fuente; lo no "
                            "verificado se etiqueta como inferencia en Notes.")))
SW.update(rango(151, 152, A("No invocar /research, /briefing ni /handoff por defecto.")))

# ---------------------------------------------------------------- visual-asset-critic/references/critique-rubric.md
NOBL = "casos ficticios sin marca ni brand-lock (comunes.sujetos, comunes.texto_en_imagen)"
NOSL = "imagen suelta sin series_lock ni serie (comunes.medio)"
NOPREV = "imagen suelta sin piezas previas con las que comparar continuidad (comunes.medio)"
CR = {1: H, 3: A("La rúbrica por capas es el checklist con que se revisa cada imagen generada (capas aplicables abajo)."),
      5: H, 7: TAB, 8: TAB, 9: F(NOBL), 10: F(NOBL), 11: F(NOBL),
      12: A("Comprobar en la imagen que el ratio es el del brief (4:5, 3:2 o 2:3)."), 14: F(NOBL),
      16: H, 18: TAB, 19: TAB, 20: F(NOSL), 21: F(NOSL), 22: F(NOSL), 23: F(NOSL), 25: F(NOSL),
      27: H, 29: TAB, 30: TAB,
      31: A("Comprobar el plano pedido (plano medio corto, plano medio, primer plano, perfil); dos pasos de diferencia = hard fail."),
      32: A("Comprobar el ángulo pedido (ángulo bajo en B5; altura de ojos en los demás)."),
      33: A("Comprobar la acción del sujeto (mirada fuera de cámara, mira a cámara, recién entrenado, sostiene la taza, de perfil)."),
      34: A("Comprobar la profundidad de campo declarada en el prompt."),
      36: A("Soft fail = arreglo en post o aceptar; hard fail = revisar."),
      38: H, 40: TAB, 41: TAB,
      42: A("Comprobar que queda espacio negativo libre para el texto que se compondrá después.", solo=["B1", "B3", "B5"], fuera=NOTX),
      43: A("Comprobar la colocación del sujeto respecto al uso y a las anclas declaradas."),
      44: A("Comprobar que la mirada va adonde pide el brief."),
      45: A("Comprobar headroom: sin cortar en la línea del pelo ni aire excesivo."),
      47: A("Los fallos de composición se corrigen en el prompt con lenguaje de composición explícito."),
      49: H, 51: TAB, 52: TAB,
      53: A("Comprobar manos: dedos, articulaciones (crítico en B4, dos manos en la taza)."),
      54: A("Comprobar ojos: simetría, foco, reflejos correctos."),
      55: A("Comprobar textura de piel natural; piel plástica = fallo."),
      56: A("Comprobar anatomía general."),
      57: A("Comprobar artefactos de fondo: texto deformado, objetos fundidos, geometría imposible."),
      59: A("Un hard fail técnico es de re-roll: el prompt puede estar bien; se presupuestan 2–3 re-rolls."),
      61: H, 63: TAB, 64: TAB, 65: F(NOPREV), 66: F(NOPREV), 67: F(NOPREV), 68: F(NOPREV), 70: F(NOPREV),
      72: H, 78: TAB, 79: TAB, 85: H, 89: TAB, 90: TAB, 105: H}
CR.update(rango(74, 76, A("La crítica registra severidad por defecto (minor/major/blocking) con el mapeo de la rúbrica, y de ahí sale el veredicto.")))
CR.update(rango(80, 83, A("Mapeo: soft fail → minor; hard fail con arreglo → major; defecto que inutiliza la imagen → blocking.")))
CR[87] = A("El veredicto se deriva de las severidades, no se elige.")
CR.update(rango(91, 94, A("Veredicto: algún blocking o 3+ major → REJECT; 1–2 major → REVISE; solo minor → ACCEPT con notas de post.")))
CR.update(rango(96, 99, A("Correr el validador de la crítica: una crítica que contradice la tabla de veredicto falla.")))
CR.update(rango(101, 103, A("Tres o más soft fails: volver a mirar, probablemente uno es hard fail.")))
CR.update(rango(107, 111, A("En la crítica: no criticar lo no pedido, no amontonar, ser específico, citar la capa y distinguir fallo de "
                            "prompt de fallo del generador.")))

# ---------------------------------------------------------------- visual-asset-critic/SKILL.md
NOSH = "imagen suelta sin storyboard ni shots.json (comunes.medio)"
CRIT = "En la crítica de la imagen generada (cuando Eric la sube, decisión 8): "
VC = {}
VC.update(rango(1, 4, FM))
VC[6] = H
VC[8] = S("presentación del rol del skill")
VC[10] = A(CRIT + "notas concretas y accionables a nivel prompt o post, no impresiones.")
VC[12] = H
VC[14] = S("rótulo que introduce la lista de activadores")
VC[16] = A(CRIT + "se activa cuando Eric sube una imagen generada y pregunta por su calidad.")
VC[17] = F(NOSH)
VC[18] = A(CRIT + "se activa con «review this render», «what should I change».")
VC[19] = F(NOSH)
VC[20] = A(CRIT + "aplica también sin storyboard, como feedback editorial contra el brief.")
VC[22] = H
VC[24] = A(CRIT + "dos artefactos siempre: crítica en markdown y crítica JSON.")
VC.update(rango(26, 29, A(CRIT + "un JSON por imagen y por ronda, nunca un nombre compartido.")))
VC[31] = A(CRIT + "el markdown usa las secciones Verdict / What's working / What's not working / Revision plan / Confidence.")
VC[33] = FENCE
VC.update(rango(34, 50, A(CRIT + "plantilla de secciones de la crítica en markdown.")))
VC[51] = FENCE
VC[53] = H
VC[55] = S("rótulo «You need:»")
VC[57] = TAB
VC[58] = TAB
VC[59] = A(CRIT + "sin la imagen generada no hay crítica.")
VC[60] = A(CRIT + "sin shots.json la intención del cuadro es el brief del caso.")
VC[61] = A(CRIT + "sin brand-lock la crítica es técnica y contra el brief.")
VC[62] = A(CRIT + "el prompt exacto usado está disponible y se adjunta.")
VC[64] = A(CRIT + "si falta contexto se pide una sola cosa: qué debía ser el cuadro (aquí: el brief).")
VC[66] = H
VC[68] = H
VC[70] = A(CRIT + "establecer la intención desde las fuentes disponibles.")
VC[72] = F(NOSH)
VC[73] = F(NOSH)
VC[74] = A(CRIT + "la intención declarada es el brief y su uso.")
VC[75] = F("imagen suelta sin secuencia narrativa ni beat (comunes.medio)")
VC[77] = A(CRIT + "si la intención no cabe en una frase, preguntar; no criticar a ciegas.")
VC[79] = H
VC[81] = A(CRIT + "revisar por capas con references/critique-rubric.md.")
VC[83] = F(NOBL)
VC[84] = F(NOSL)
VC[85] = A(CRIT + "capa Shot Spec: plano, ángulo y composición contra el brief.")
VC[86] = A(CRIT + "capa Composition: espacio reservado para el texto compuesto después.", solo=["B1", "B3", "B5"], fuera=NOTX)
VC[87] = A(CRIT + "capa Technical: piel, manos, ojos, anatomía, artefactos.")
VC[88] = F(NOPREV)
VC[90] = A(CRIT + "cada capa: pass / soft fail / hard fail.")
VC[92] = H
VC[94] = A(CRIT + "cada problema lleva su arreglo en uno de tres cubos.")
VC.update({n: A(CRIT + "arreglo a nivel prompt: el cambio exacto en el prompt.") for n in (96, 97)})
VC.update({n: A(CRIT + "arreglo en post: qué ajustar en edición.") for n in (99, 100)})
VC.update({n: A(CRIT + "re-roll: sin cambio de prompt, 2–3 intentos.") for n in (102, 103)})
VC[105] = H
VC[107] = TAB
VC[108] = TAB
VC.update(rango(109, 111, A(CRIT + "ACCEPT / REVISE / REJECT según las capas.")))
VC[113] = H
VC[115] = A(CRIT + "declarar la confianza con honestidad.")
VC[117] = TAB
VC[118] = TAB
VC.update(rango(119, 121, A(CRIT + "sin storyboard ni brand-lock la confianza máxima es MEDIUM.")))
VC.update(rango(123, 126, A(CRIT + "no declarar HIGH con shot_id, brand_lock_ref o prompt_ref nulos.")))
VC[128] = H
VC.update(rango(130, 134, A(CRIT + "escribir también el JSON conforme a templates/critique.schema.json v1.1.")))
VC[136] = A(CRIT + "mapear el markdown al esquema sección por sección.")
VC[138] = TAB
VC[139] = TAB
VC.update(rango(140, 143, A(CRIT + "verdict, working[], issues[] (capa, nota, fix_type, fix) y confidence.")))
VC.update(rango(145, 146, A(CRIT + "procedencia completa con hashes en v1.1.")))
VC[148] = TAB
VC[149] = TAB
VC[150] = A(CRIT + "run_id y round: sin run.json se registra null y ronda 1.")
VC[151] = A(CRIT + "created_at en UTC.")
VC[152] = A(CRIT + "shot_id null (imagen suelta).")
VC[153] = A(CRIT + "image_ref e image_sha256 de la imagen revisada.")
VC[154] = A(CRIT + "prompt_ref y prompt_sha256 del prompt exacto.")
VC[155] = A(CRIT + "brand_lock_ref y su hash: null (sin brand-lock).")
VC[156] = A(CRIT + "generator y model_version: GPT Image 2 (gpt-image-2).")
VC[157] = A(CRIT + "seed: null si la plataforma no lo expone.")
VC[159] = FENCE
VC.update(rango(160, 162, A(CRIT + "calcular SHA-256 de imagen y prompt.")))
VC[163] = FENCE
VC.update(rango(165, 168, A(CRIT + "todos los campos requeridos y nulables: null registra lo que no hubo; no omitir claves.")))
VC.update(rango(170, 172, A(CRIT + "los hashes impiden que un ACCEPT viejo quede pegado a una imagen regenerada.")))
VC[174] = A(CRIT + "una severidad por problema, mapeada de la rúbrica.")
VC[176] = TAB
VC[177] = TAB
VC.update(rango(178, 180, A(CRIT + "minor / major / blocking según la rúbrica.")))
VC[182] = A(CRIT + "el veredicto se deriva de las severidades.")
VC.update(rango(184, 187, A(CRIT + "blocking o 3+ major → REJECT; 1–2 major → REVISE; solo minor → ACCEPT.")))
VC.update(rango(189, 191, S("historia del umbral; la regla está en 184–187")))
VC[193] = A(CRIT + "el veredicto del markdown sigue la misma regla.")
VC[195] = H
VC[197] = A(CRIT + "correr el gate, no basta con un JSON válido.")
VC[199] = FENCE
VC[200] = A(CRIT + "python tools/validate_critique.py sobre el JSON.")
VC[201] = FENCE
VC.update(rango(203, 204, A(CRIT + "o validar el árbol completo recalculando hashes.")))
VC[206] = FENCE
VC[207] = A(CRIT + "python tools/validate_provenance.py.")
VC[208] = FENCE
VC.update(rango(210, 212, A(CRIT + "el paso no es opcional: un ACCEPT con un major es un error.")))
VC[213] = S("historia de CI; descriptivo")
VC.update(rango(215, 218, A(CRIT + "formato de referencia: examples/critique.accept.json, critique.revise.json, worked-run.")))
VC[220] = H
VC[222] = H
VC[224] = A(CRIT + "nada de crítica por sensaciones: cada observación cita algo visible.")
VC[226] = H
VC[228] = A(CRIT + "un arreglo de prompt dice el texto exacto a añadir o cambiar.")
VC[230] = H
VC[232] = A(CRIT + "no criticar lo que el brief no pidió.")
VC[234] = H
VC[236] = A(CRIT + "declarar los límites conocidos del generador (manos, reflejos) y recomendar re-roll o post.")
VC[238] = H
VC[240] = A(CRIT + "en la duda, ACCEPT con notas de post si es 80% correcto y el resto se arregla en post.")
VC[242] = H
VC[244] = A(CRIT + "leer references/critique-rubric.md.")
VC[246] = H
for n in range(248, 268):
    VC[n] = S("línea vacía de cita") if n in (250, 255, 260, 265) else A(CRIT + "ejemplo del formato de salida de la crítica.")
VC[269] = H
VC.update({n: F("imagen suelta sin árbol output/ de storyboard para el modo revisión de forge (comunes.medio)")
           for n in (271, 273, 274)})
VC.update(rango(276, 279, A(CRIT + "si REJECT, decir qué bloqueó y qué decisión requiere (brief, generador); no ofrecer revisión automática.")))
VC[281] = A(CRIT + "no auto-revisar: Eric elige.")
VC[282] = VC[281]

# ---------------------------------------------------------------- ai-production-director/SKILL.md
PS = ("pieza suelta: un retrato, un prompt de imagen fija; el propio skill (línea 4) se excluye de piezas sueltas y su pipeline "
      "multi-etapa no corre en este caso (comunes.medio)")
AP = {}
AP.update({n: S("frontmatter: metadatos del skill") for n in (1, 2, 3, 6, 7, 8, 9, 10)})
AP[4] = A("Pieza suelta: el pipeline del director no corre; la sintaxis final del prompt la da el skill image (gpt-image.md).")
AP[5] = A("Conservar la atribución obligatoria a Serge Shima (CC BY 4.0) en los créditos del entregable que usa image.")
AP[12] = H
for n in (14, 16, 17, 18, 19, 20, 22):
    AP[n] = F(PS)
AP[24] = H
AP[26] = TAB
AP[27] = TAB
for n in range(28, 34):
    AP[n] = F(PS)
AP[34] = A("image (smixs) es la autoridad de la sintaxis final del prompt de GPT Image 2.")
AP[35] = F("imagen suelta sin shots.json: el forge no genera borradores aquí (comunes.medio)")
AP[36] = A("visual-asset-critic es la autoridad para aceptar o rechazar la imagen generada.")
AP[37] = F("imagen fija, no video (comunes.medio)")
AP[38] = F("imagen suelta sin entrega de storyboard (comunes.medio)")
AP[39] = F("fotografía de retrato live-action, no animación ni material didáctico (comunes.tipo_pieza)")
AP[40] = F("Aurora está excluida por Eric (PILOTO_V5_INSTRUCCIONES §0.4); el gate determinista es validar_prompts.py")
AP[42] = A("Leer el SKILL.md de cada sub-skill usada y seguir su protocolo, no de memoria.")
AP[44] = H
AP[46] = F(PS)
AP[48] = TAB
AP[49] = TAB
for n in list(range(50, 56)) + [57, 58, 59, 61]:
    AP[n] = F(PS)
AP[63] = H
AP[65] = F(PS)
for n in (67, 72, 77, 82, 87, 93, 98, 103, 108, 114, 118, 122, 125, 128, 131, 134, 137, 144, 148):
    AP[n] = H
for n in (68, 69, 70, 73, 74, 75, 78, 79, 80, 83, 84, 85, 88, 89, 90, 91, 95, 99, 100, 101, 104, 105, 106, 110, 111):
    AP[n] = F(PS)
AP[94] = A("En imagen: image es la autoridad de sintaxis final, Eric genera y visual-asset-critic evalúa cada render.")
AP[96] = F("una sola pasada por prompt sin rondas de revisión (comunes.generacion)")
AP[112] = A("No preguntar lo que el brief ya responde.")
AP[116] = A("Al usar una sub-skill: nombrarla, leer su SKILL.md y los references que su protocolo exige, y ejecutar su protocolo.")
AP[120] = A("Las reglas de resolución de conflictos son decisiones tomadas; se aplican sin reabrirlas.")
AP[123] = A("Vocabulario prohibido que gana siempre: «cinematic», «epic», «stunning», «masterpiece», «beautiful lighting», "
            "«professional», «high quality» y emociones nombradas sin cuerpo; resolución y ratio van como parámetros concretos.")
AP[126] = A("El prompt final se escribe en la sintaxis del modelo destino según image/references/gpt-image.md.")
AP[129] = F("imagen suelta sin shots.json (comunes.medio)")
AP[132] = A("El texto final del prompt lo define image (smixs); nunca al revés.")
AP[135] = A("Atribución «Serge Shima — github.com/smixs/visual-skills» en los créditos del entregable, no en cada prompt.")
AP[139] = A("No usar visual-media en una pieza live-action fotográfica.")
AP[141] = F("fotografía de retrato, no animación (comunes.tipo_pieza)")
AP[142] = F("no es material didáctico ni de cara al cliente en español (comunes.tipo_pieza)")
AP[146] = A("Si falta una sub-skill, decirlo en una línea y aplicar el sustituto; aquí image y visual-asset-critic están presentes.")
AP[150] = F(PS)
AP[151] = F(PS)

MAPA = {"skills/produccion-visual-sw30/SKILL.md": SW, "skills/visual-asset-critic/references/critique-rubric.md": CR,
        "skills/visual-asset-critic/SKILL.md": VC, "skills/ai-production-director/SKILL.md": AP}


def main():
    lote = json.loads((AQUI / "lotes/lote_07.json").read_text(encoding="utf-8"))
    usados = {a: set() for a in MAPA}
    out, faltan = [], []
    for u in lote:
        n = int(u["linea"])
        d = MAPA[u["archivo"]].get(n)
        if d is None:
            faltan.append(f"{u['archivo']}:{n} {u['texto'][:60]}")
            continue
        usados[u["archivo"]].add(n)
        out.append({"id": u["id"], **d})
    pkg = AQUI.parents[1] / "apd/.cache/pkg/AI_Production_Director_v3.4.0_COMPLETE"
    lineas = {a: (pkg / a).read_text(encoding="utf-8").splitlines() for a in MAPA}
    # una decisión sobre una línea en blanco (dentro de un rango) no cuenta; una sobre una línea con texto ajena al lote, sí
    sobran = [f"{a}:{n}" for a, m in MAPA.items() for n in sorted(set(m) - usados[a])
              if n > len(lineas[a]) or lineas[a][n - 1].strip()]
    assert not faltan, "sin decisión:\n" + "\n".join(faltan)
    assert not sobran, "decisión para línea inexistente (vacía): " + ", ".join(sobran)
    (AQUI / "veredictos/pasada_1/lote_07.json").write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    print(len(out), "veredictos")


if __name__ == "__main__":
    main()
