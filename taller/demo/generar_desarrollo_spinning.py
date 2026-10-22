"""Paso 2 del caso real de spinning, desarrollado por Claude en la sesión de Claude Code del 2026-10-22.

Este archivo es la respuesta del rol "desarrollador_brief" para el caso real: la app la recibe por
el modo manual (copiar y pegar) y la valida igual que una respuesta de API. No es una decisión del
usuario: todas las propuestas quedan pendientes de la revisión de Eric (paso 3).

    python taller/demo/generar_desarrollo_spinning.py   -> escribe desarrollo_spinning.json
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def P(valor, cita, pregunta=""):
    return {"estado": "proporcionado", "valor": valor, "cita": cita, "pregunta": pregunta}


def I(valor, fundamento):
    return {"estado": "inferido", "valor": valor, "fundamento": fundamento}


def PR(valor, fundamento, alternativas=None, pregunta=""):
    return {"estado": "propuesta", "valor": valor, "fundamento": fundamento, "alternativas": alternativas or [], "pregunta": pregunta}


def F(pregunta, fundamento=""):
    return {"estado": "falta", "valor": None, "pregunta": pregunta, "fundamento": fundamento}


def C(fundamento):
    return {"estado": "condicion_inactiva", "valor": None, "fundamento": fundamento}


NO_ANCLA = "Condición «{c}»: la imagen es una génesis independiente para un reportaje, no un ancla, keyframe ni parte de un clip."

CAMPOS = {
    "entrada.ruta.flujo": P("Génesis: imagen nueva sin referencias", "es una imagen genesis",
                            "En la taxonomía, FL02 es la génesis sin referencia dentro del flujo de spot y FL04 es «activo directo sin preproducción». ¿Confirmas FL02 o prefieres FL04 para una foto suelta de reportaje?"),
    "entrada.ruta.seccion": C("Condición «si fuente define sección»: no hay un proyecto ni documento de flujo que defina sección para esta imagen."),
    "entrada.ruta.etapa": C("Condición «cuando la operación, módulo o fuente lo exige»: el contrato T-GENESIS no exige etapa y la imagen no pertenece a la producción de un spot."),
    "entrada.ruta.paso": C("Condición «cuando la operación, módulo o fuente lo exige»: igual que la etapa, ningún contrato ni fuente lo exige para esta génesis."),
    "entrada.ruta.operativa": C("Condición «si existe ruta operativa en contexto»: la ruta operativa distingue video publicitario o clip; esta pieza es una imagen fija."),
    "entrada.operacion": P("génesis", "es una imagen genesis"),
    "entrada.modelo.nombre": I("GPT Image", "La app trabaja exclusivamente con GPT Image 2."),
    "entrada.modelo.version": I("2", "La app trabaja exclusivamente con GPT Image 2."),
    "entrada.modelo.interfaz": P("App de ChatGPT para escritorio", "interfaz es la app de chat gpt para deshtop"),
    "entrada.pieza.tipo": P("Fotografía editorial deportiva", "fotografia editrial deportiva"),
    "entrada.pieza.tematica": P(["Deporte", "Clase de spinning (ciclismo indoor)"], "en una clase de spniing"),
    "entrada.pieza.objetivo": P("Capturar exactamente el momento pico de la clase: los tres ciclistas pedalean a toda velocidad, de pie sobre los pedales, con determinación en el rostro.",
                                "los quieor excatamente en el momento pico d ela clsse cuando estan pedalando a toda velocidad"),
    "entrada.pieza.uso": P("Reportaje sobre actividades deportivas en la Ciudad de México", "es par un reportake sivre acticidades deprttivas en cd,mx"),
    "entrada.formato.ratio": P("16:9", "16:9"),
    "entrada.formato.ancho_px": PR(2560, "GPT Image 2 acepta Size/Ratio; 2560×1440 es exactamente 16:9 y es el «Reliable upper bound» documentado en gpt-image.md (INV-002359). Da la mayor resolución fiable para un reportaje.",
                                   ["Usar solo el ratio 16:9 y dejar el tamaño a la interfaz de ChatGPT"]),
    "entrada.formato.alto_px": PR(1440, "Pareja de 2560 en 16:9 (INV-002359). Cumple los límites documentales: lados menores de 3840, múltiplos de 16 y área dentro del rango.",
                                  ["Usar solo el ratio 16:9"]),
    "entrada.formato.resolucion": C("Condición «cuando contrato usa resolución nominal»: la resolución nominal (1K/2K/4K) es un parámetro de Nano Banana; GPT Image 2 usa tamaño o ratio."),
    "entrada.idioma_prompt": P("Inglés", "en ingles esto es siemore"),
    "entrada.sujetos.cantidad": P(3, "3 cicleist as"),
    "entrada.sujetos.items[].id": I(["S1 (izquierda)", "S2 (centro)", "S3 (derecha)"], "Identificadores en el orden izquierda-centro-derecha que dio el usuario."),
    "entrada.sujetos.items[].clase": I(["persona", "persona", "persona"], "Los tres sujetos son ciclistas, es decir personas (faceta F15)."),
    "entrada.sujetos.items[].descripcion": P([
        "S1: ciclista mediterráneo, rubio, 23 años, musculatura marcada sin exagerar el volumen.",
        "S2: hombre mexicano de 32 años descrito por el usuario como «chacal», musculoso, con tatuajes en los brazos.",
        "S3: mujer mediterránea de 27 años, cabello castaño claro, largo, en cola de caballo, cuerpo delgado y tonificado."],
        "el ziclusta d ela izqyuerda es medierraneo rubio de 23 anis"),
    "entrada.sujetos.items[].edad": P([23, 32, 27], 'es un "chacal" mexicnao de 32 anos'),
    "entrada.sujetos.items[].genero": I(["masculino", "masculino", "femenino"], "«el ziclusta… medierraneo» y «e3l jhomvre» son masculinos; «una mujer meduterrnea» es femenino."),
    "entrada.sujetos.items[].rasgos": P([
        ["mediterráneo", "musculatura marcada sin exagerar el volumen muscular"],
        ["mexicano", "«chacal» (término literal del usuario)", "musculoso", "tatuajes en los brazos"],
        ["mediterránea", "cuerpo delgado y tonificado"]],
        "masrcado sin exagerar ne el vilumne muscular",
        "«chacal» es un término coloquial con varias lecturas visuales. Anunciaste una imagen para aclararlo: ¿qué rasgos concretos debe mostrar S2 (complexión, corte de cabello, vello facial, estilo de los tatuajes)?"),
    "entrada.sujetos.items[].cabello": P(["rubio", "no especificado por el usuario", "castaño claro, largo, en cola de caballo"],
                                         "ascatan claior significa cabello castano claro",
                                         "¿Cómo es el cabello de S2 (el hombre del centro)?"),
    "entrada.sujetos.items[].vestuario": PR([
        "S1: camiseta técnica negra ajustada de manga corta y culotte de ciclismo negro.",
        "S2: camiseta técnica negra sin mangas (deja ver los tatuajes de los brazos) y culotte negro.",
        "S3: top deportivo negro y leggings de ciclismo negros a media pantorrilla.",
        "Los tres: tela técnica negra mate de alta gama, sin logotipos, marcas ni texto visibles; zapatillas de ciclismo negras con calas."],
        "Desarrolla «ropa d elata fgama deportiva negra» en prendas concretas para que el modelo no invente. Sin mangas en S2 para que los tatuajes de los brazos se vean; sin logotipos porque no se pidieron y el modelo los deforma.",
        ["Los tres con camiseta de manga corta", "Sin especificar prendas: solo «ropa deportiva negra de alta gama»"]),
    "entrada.sujetos.items[].expresion": P(["determinación", "determinación", "determinación"], "con la expresion de terminacion en el riostro"),
    "entrada.sujetos.items[].posicion": P(["izquierda", "centro", "derecha"], "el ziclusta d ela izqyuerda"),
    "entrada.accion.tipo": P("Pedalear a toda velocidad de pie sobre bicicletas fijas en una clase de spinning", "cuando estan pedalando a toda velocidad"),
    "entrada.accion.estado_visible": P("Momento pico de la clase: los tres de pie, sin tocar el asiento, pedaleando a máxima velocidad, mirada al frente.",
                                       "ellos levntdos sin tocar el issento de la bicibleta"),
    "entrada.accion.postura": P("Cuerpo ligeramente inclinado hacia adelante, ambas manos firmes en el manubrio, de pie sin tocar el asiento, pies firmes en los pedales.",
                                "el cuerpop liegreamnete ncklujado al fernte con mabas manos firmaente en el manibrio"),
    "entrada.accion.evidencia_fisica": PR([
        "piernas en fases distintas del pedaleo (una arriba, una abajo) y desfasadas entre los tres",
        "tensión visible en antebrazos, hombros y pantorrillas",
        "sudor brillante en frente, cuello y brazos",
        "leve desenfoque de movimiento solo en pies, pedales y volantes de inercia",
        "la cola de caballo de S3 desplazada por el movimiento"],
        "Una foto fija solo muestra «a toda velocidad» si hay signos físicos del movimiento. El desenfoque se limita a las partes que giran para que rostros y torsos queden nítidos.",
        ["Congelado total, sin ningún desenfoque de movimiento"]),
    "entrada.fisica.regimen": PR(["cuerpo en esfuerzo máximo", "movimiento congelado con desenfoque parcial en las partes que giran"],
                                 "El instante pedido es el pico de esfuerzo de una clase; el régimen define cómo se ven cuerpo y movimiento en un fotograma."),
    "entrada.escena.espacio": P("Estudio de spinning (interior)", "ekl estyduio d esoinning"),
    "entrada.escena.entorno": P("Estudio de estética brutalista minimalista con iluminación de neón fría; clase llena pero no abarrotada.",
                                "es en yn estulio vritakista minumalisa con iluminaciuon neion fria"),
    "entrada.escena.momento": P("Momento pico de la clase", "en el momento pico d ela clsse"),
    "entrada.escena.clima": C("Condición «si tiene efecto visual»: es un interior sin ventanas mencionadas; el clima exterior no se ve."),
    "entrada.escena.planos": PR([
        "Primer término: los tres ciclistas protagonistas en la primera fila, nítidos.",
        "Segundo término: dos o tres filas de participantes pedaleando, con desenfoque suave, rostros no protagónicos.",
        "Fondo: muro de concreto con tubos de neón."],
        "El usuario pidió el encuadre en los tres ciclistas con más personas al fondo («clase lleba opeor no abarrtada»). El desenfoque del fondo separa a los protagonistas y deja ver que la clase está llena sin saturar.",
        ["Fondo nítido con todos los participantes legibles"]),
    "entrada.estilo": PR(["fotografía editorial deportiva a color", "color natural con dominante fría del neón", "contraste alto con detalle en sombras",
                          "piel con textura real, sin retoque fuerte ni aspecto de estudio"],
                         "Concreta «fotografia editrial deportiva» en atributos observables (regla U-VISUAL-SPECIFICITY: atributos concretos en vez de etiquetas de estilo).",
                         ["Blanco y negro de alto contraste"]),
    "entrada.representacion": I(["fotografía"], "El usuario pide «una fotografia editrial deportiva»."),
    "entrada.identidad.invariantes": C("Condición «si exige reconocimiento/continuidad»: no hay personas reales que reconocer ni continuidad entre imágenes. Se reactivaría si la imagen anunciada del «chacal» se usa como referencia de identidad."),
    "entrada.identidad.referencias": C("Condición «si identidad respaldada por referencias»: no se ha recibido ninguna referencia. Depende de tu respuesta en entrada.referencias[].archivo."),
    "entrada.blocking.contactos": P(["ambas manos firmes en el manubrio", "pies firmes en los pedales", "sin contacto con el asiento",
                                     "bicicletas fijas firmemente sujetas al piso"],
                                    "con los pies firmememente sujetios a los pedales"),
    "entrada.blocking.relaciones": PR([
        "Las tres bicicletas contiguas en la primera fila, alineadas de frente a cámara, separadas un metro aproximadamente.",
        "S2 al centro sobre el eje de la imagen; S1 a su izquierda y S3 a su derecha, según lo pedido.",
        "Las filas de participantes del fondo quedan detrás y ligeramente desplazadas, sin tapar a los protagonistas."],
        "Organiza en el espacio el orden izquierda-centro-derecha del usuario para que los tres se lean completos y la clase llena se vea detrás.",
        ["Fila en diagonal ligera hacia el fondo, con S1 más cerca de cámara"]),
    "entrada.rostro.ocupacion": PR(0.08, "Con tres personas y las bicicletas en cuadro, cada rostro ocupa cerca del 8 % de la altura de la imagen: suficiente para leer la determinación sin cortar el cuerpo.",
                                   ["0.15 si eliges un plano más cerrado (de muslos arriba)"]),
    "entrada.rostro.detalles": PR(["mirada fija al frente, fuera de cámara, hacia el instructor", "mandíbula apretada", "labios entreabiertos por la respiración",
                                   "ceño ligeramente fruncido", "gotas de sudor en sienes y frente", "poros y textura real de la piel"],
                                  "Traduce «determinación» y «mirada al frente» (palabras del usuario) en signos físicos visibles; una emoción nombrada sin cuerpo no se dibuja.",
                                  ["Mirada directa a cámara"]),
    "entrada.camara.plano": PR("Plano entero de grupo: los tres ciclistas y sus bicicletas completas, con el anclaje de las bicicletas al piso visible.",
                               "El usuario pidió bicicletas «fimememennte sjetasal piso» y pies en los pedales: para que eso se vea hace falta incluir piso y bicicletas completas.",
                               ["Plano americano (de muslos arriba) si se prioriza la expresión sobre las bicicletas"]),
    "entrada.camara.angulo": PR("Frontal, ligeramente contrapicado (cámara un poco por debajo de la altura de los ojos).",
                                "Frontal para que la mirada al frente y los rostros se lean; el leve contrapicado da potencia al esfuerzo sin deformar.",
                                ["Frontal a la altura de los ojos", "Tres cuartos desde la izquierda"]),
    "entrada.camara.altura": PR("A la altura del manubrio, aproximadamente 1.1 m, frente a la primera fila.",
                                "Ubica físicamente el contrapicado propuesto: por debajo de los ojos de ciclistas de pie."),
    "entrada.camara.efecto_optico": PR("Profundidad de campo media: los tres protagonistas nítidos de pies a cabeza; segundo término y fondo con desenfoque suave.",
                                       "Separa a los protagonistas de la clase llena y mantiene la lectura de los tres a la vez."),
    "entrada.camara.lente_intencion": PR("Perspectiva de un 35 mm en formato completo: abarca a los tres y algo del estudio sin deformar los cuerpos.",
                                         "GPT Image 2 admite una sensación de lente como apariencia general («50mm feel», INV-002453). Un 35 mm resuelve tres personas con bicicletas en 16:9.",
                                         ["50 mm desde más lejos, con más compresión del fondo"]),
    "entrada.luz.fuente": PR("Tubos de neón fríos (cian y blanco frío) en techo y muros como luz principal motivada, más un relleno frontal suave y débil para leer los rostros.",
                             "Desarrolla «iluminaciuon neion fria» del usuario: el neón es la luz real del estudio; el relleno evita rostros negros."),
    "entrada.luz.direccion": PR("Principal cenital y contraluz desde los tubos sobre y detrás de los ciclistas, que dibujan filo en hombros, brazos y cabello; relleno frontal bajo.",
                                "El contraluz separa a los protagonistas del fondo y marca la musculatura descrita por el usuario."),
    "entrada.luz.dureza": PR("Dura en los filos del contraluz; suave en el relleno frontal.",
                             "Filos duros dibujan el volumen y el sudor; el relleno suave no aplana el rostro."),
    "entrada.luz.distribucion": PR("Luz concentrada en los tres protagonistas; el fondo cae a penumbra con los tubos de neón visibles como líneas de luz.",
                                   "Jerarquiza: la mirada va a los tres; la clase del fondo se intuye."),
    "entrada.luz.contraste": PR("Alto, cerca de 4:1 entre luz y sombra en los rostros, con negros profundos que conservan detalle.",
                                "Coherente con estudio oscuro y neón; se conserva detalle en ropa y bicicletas negras."),
    "entrada.luz.specular": PR("Brillos especulares en el sudor de la piel y en el metal y el plástico satinado de las bicicletas.",
                               "El sudor y el metal son las superficies que revelan esfuerzo y materialidad bajo luz dura."),
    "entrada.color_material.paleta": PR(["negro #0B0B0D (ropa y bicicletas)", "gris concreto #8A8D90", "cian neón #3FD0FF", "blanco frío #E8F4FF", "tonos de piel naturales"],
                                        "Paleta fría del neón y del concreto con la piel natural; colores concretos en hexadecimal (INV-002259 como ejemplo de precisión)."),
    "entrada.color_material.grade": PR("Grade frío con piel de tono natural, negros profundos con detalle, contraste natural sin efecto HDR.",
                                       "Mantiene la dominante fría pedida sin volver la piel azul ni sobreprocesar."),
    "entrada.color_material.materiales": PR(["concreto aparente con marcas de cimbra en muros", "piso de concreto pulido oscuro",
                                             "bicicletas fijas negras mate de última generación con volante de inercia metálico", "tela técnica negra mate con costuras planas"],
                                            "Concreta «estulio vritakista minumalisa» y «vicicletassd fijas… negra… d euktuna egeneracion» en materiales visibles."),
    "entrada.color_material.texturas": PR(["poros y sudor en la piel", "trama fina de la tela técnica", "porosidad del concreto", "satinado del cuadro de las bicicletas"],
                                          "Texturas reales que hacen creíble la foto bajo luz dura."),
    "entrada.color_material.acabado": PR("Mate en ropa y bicicletas, con brillos puntuales en metal; piel con brillo de sudor.",
                                         "Contraste de acabados que separa piel, tela y metal."),
    "entrada.composicion": PR(["los tres ciclistas en la franja central horizontal, S2 en el eje vertical central", "líneas de neón del techo y muros que convergen hacia el centro",
                               "las filas del fondo crean profundidad detrás de los protagonistas", "aire suficiente sobre las cabezas y piso visible bajo las bicicletas"],
                              "Organiza 16:9 alrededor de los tres protagonistas; las líneas de luz guían la mirada al centro."),
    "entrada.referencias[].archivo": F("Escribiste «chacal te estoy asdhybntando una imagen», pero la imagen no se ha recibido. ¿La vas a adjuntar como referencia (entonces la operación deja de ser génesis y pasa a composición con referencias, con otro contrato) o prefieres describir con palabras cómo es S2 y seguir en génesis sin referencias?",
                                       "El contrato T-GENESIS admite cero referencias (references_max 0)."),
    "entrada.referencias[].sha256": C("Condición «cada referencia»: no hay referencias recibidas. Se activa si adjuntas la imagen."),
    "entrada.referencias[].medio": C("Condición «cada referencia»: no hay referencias recibidas."),
    "entrada.referencias[].rol": C("Condición «cada referencia»: no hay referencias recibidas."),
    "entrada.referencias[].indice": C("Condición «cada referencia»: no hay referencias recibidas."),
    "entrada.referencias[].preservar": C("Condición «cada referencia con invariantes»: no hay referencias recibidas."),
    "entrada.restricciones": P(["exactamente tres ciclistas protagonistas", "los tres de pie, sin tocar el asiento", "pies sujetos a los pedales y manos en el manubrio",
                                "bicicletas fijas ancladas al piso", "fondo con más participantes, clase llena pero no abarrotada"],
                               "aunaqwe ne el fondo s even m sperisnas en loq e sria una clase lleba opeor no abarrtada"),
    "entrada.contexto_narrativo.genero": C("Condición «si restringe activo»: es una foto suelta para un reportaje, sin guion ni género narrativo que la restrinja."),
    "entrada.contexto_narrativo.beats": C("Condición «si restringe activo»: no hay estructura de beats."),
    "entrada.contexto_narrativo.dialogo": C("Condición «si restringe efecto visible»: no hay diálogo."),
    "entrada.contexto_secuencia.montaje": C("Condición «si restringe activo»: no forma parte de una secuencia montada."),
    "entrada.plano.funcion": PR("Imagen de apertura del reportaje: transmite intensidad y comunidad de una clase de spinning en la ciudad.",
                                "Para un reportaje, la foto pico suele abrir la nota; esa función justifica el plano entero y la clase visible al fondo.",
                                ["Imagen de apoyo dentro del cuerpo del reportaje"]),
    "entrada.publicacion.destino": F("¿Dónde se publicará el reportaje: sitio web, revista impresa o redes sociales? Cambia el recorte final y si conviene dejar espacio libre para un titular."),
    "entrada.publicacion.ubicacion": C("Condición «si ubicación impone condiciones»: no se indicó una ubicación de publicación con requisitos propios."),
    "entrada.publicacion.literal": C("Condición «si fuente especifica publicación»: ninguna fuente lo especifica."),
    "entrada.publicacion.fuente": C("Condición «si publicación citada»: no hay publicación citada."),
    "entrada.ancla.rol": C(NO_ANCLA.format(c="operación ancla")),
    "entrada.ancla.clip_id": C(NO_ANCLA.format(c="FF/LF asociado clip")),
    "entrada.ancla.pareja_id": C(NO_ANCLA.format(c="solo si exige pareja")),
    "entrada.ancla.estado_inicial": C(NO_ANCLA.format(c="FF")),
    "entrada.ancla.estado_final": C(NO_ANCLA.format(c="LF")),
    "entrada.ancla.invariantes": C(NO_ANCLA.format(c="operación ancla")),
    "entrada.ancla.series_lock": C(NO_ANCLA.format(c="ancla de proyecto con series lock")),
    "entrada.ancla.plan_anchors": C(NO_ANCLA.format(c="ancla de proyecto con plan")),
    "entrada.ancla.contexto_clip.camara": C(NO_ANCLA.format(c="FF/LF; estado o contexto efectivo, incluso cámara fija")),
    "entrada.ancla.contexto_clip.transicion": C(NO_ANCLA.format(c="FF/LF; relación efectiva")),
    "entrada.ancla.contexto_clip.audio": C(NO_ANCLA.format(c="FF/LF; contexto efectivo incluso silencio")),
    "entrada.ancla.contexto_clip.animacion": C(NO_ANCLA.format(c="cuando condiciona frame")),
    "entrada.ancla.contexto_clip.duracion": C(NO_ANCLA.format(c="cuando handoff lo requiere")),
    "entrada.ancla.contexto_clip.efecto_visible": C(NO_ANCLA.format(c="si contexto sonoro tiene efecto visible")),
    "entrada.edicion.cambio": C("Condición «edición»: la operación es génesis, no edición de una imagen existente."),
    "entrada.edicion.preservar": C("Condición «edición»: la operación es génesis."),
    "entrada.edicion.mascara": C("Condición «solo admitida por modelo/interfaz»: no hay edición."),
    "entrada.transferencia.propiedades": C("Condición «transferencia de estilo»: no se pidió transferir el estilo de otra imagen."),
    "entrada.boceto.estructura_preservada": C("Condición «boceto a final»: no hay boceto de partida."),
    "entrada.texto_marca.literales": C("Condición «texto integrado solicitado»: no pediste texto dentro de la imagen."),
    "entrada.texto_marca.posicion": C("Condición «texto integrado solicitado»: no se pidió texto."),
    "entrada.texto_marca.tipografia": C("Condición «texto integrado solicitado»: no se pidió texto."),
    "entrada.texto_marca.logos_aprobados": C("Condición «marca autorizada»: no hay una marca autorizada; por eso el vestuario se propone sin logotipos."),
    "entrada.texto_integrado_override.habilitado": C("Condición «Ideogram»: es un control exclusivo de Ideogram; aquí el modelo es GPT Image 2."),
    "entrada.texto_integrado_override.rationale": C("Condición «Ideogram integrado»: no aplica a GPT Image 2."),
    "entrada.grounding.objetivo": C("Condición «si grounding»: GPT Image 2 no hace búsqueda de imágenes reales (grounding); el estudio es genérico, no un lugar real."),
    "entrada.grounding.evidencia": C("Condición «si grounding ejecutado»: no hay grounding."),
    "entrada.presupuesto.creditos_maximos": C("Condición «antes ejecución con costo»: este campo viene del template T-BRIEF-IMG (§3), no de las reglas de redacción. Solo se activa antes de que el sistema ejecute una generación con costo; esta app no genera imágenes: tú decides cuándo generar en ChatGPT."),
    "entrada.selecciones_taxonomicas": I(["P-01 flujo: génesis", "F04 tipo de pieza: editorial", "F05 temática: deporte", "F06 formato: 16:9", "F10 modo: génesis",
                                          "F13 acción: esfuerzo en el pico", "F14 régimen: cuerpo en esfuerzo", "F15 sujeto: persona", "F16 espacio: interior",
                                          "F19 número de sujetos: tres", "F29 modelo: GPT Image 2"],
                                         "Descriptores del caso derivados del brief para orientar la selección de reglas; los nombres exactos de valor se contrastan con la taxonomía en el paso 5."),
}

RESUMEN = ("Foto editorial a color, en 16:9, del pico de una clase de spinning en un estudio brutalista de concreto iluminado con neón frío. "
           "Plano entero de grupo, frontal y ligeramente contrapicado desde la altura del manubrio, con perspectiva de 35 mm: los tres "
           "protagonistas de pie sobre los pedales en la primera fila, S2 al centro, nítidos de pies a cabeza, y dos o tres filas de la clase "
           "detrás con desenfoque suave. El neón del techo y los muros funciona como contraluz que dibuja filos en hombros, brazos y sudor; un "
           "relleno frontal débil deja leer la determinación en los rostros. La velocidad se ve en piernas desfasadas, tensión muscular, sudor "
           "y un desenfoque leve solo en pies y volantes de inercia. Ropa técnica negra mate sin logotipos.")

CONFLICTOS = [
    "Anunciaste una imagen para el «chacal» que no se ha recibido; una génesis no admite referencias (T-GENESIS, references_max 0). Hay que decidir si se adjunta (cambia la operación) o se describe con palabras.",
]


def construir():
    import sys
    sys.path.insert(0, str(AQUI.parent))
    from recursos import cargar
    rec = cargar()
    campos = []
    for ruta in rec.rutas:
        base = {"path": ruta, "estado": "", "valor": None, "cita": "", "fundamento": "", "pregunta": "", "alternativas": []}
        base.update(CAMPOS[ruta])
        campos.append(base)
    faltan = set(rec.rutas) - set(CAMPOS)
    sobran = set(CAMPOS) - set(rec.rutas)
    assert not faltan and not sobran, (faltan, sobran)
    return {"campos": campos, "resumen_creativo": RESUMEN, "conflictos": CONFLICTOS}


if __name__ == "__main__":
    salida = construir()
    (AQUI / "desarrollo_spinning.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("campos:", len(salida["campos"]))
