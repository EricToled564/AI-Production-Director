# Lote 1 de briefs: génesis K01–K09 (tarea 3)

Cada caso se aprueba por su sha256 (serialización de `verificar_templates.py`). Todo lo que no
viene de la lista de casos aprobada (26 §16) es propuesta del sistema: Eric aprueba, cambia o quita.
Las personas, lugares y objetos de los briefs son inventados, salvo los sujetos reales de K03, K04 y
K07, que se verifican contra fotos reales.

## K01 · rostro maestro T1

Rostro maestro T1 de una persona inventada (no real), para usarlo después como referencia de identidad en K10, K11, K12, K13 y K33. Mujer de unos 35 años, cara irregular y asimétrica, cabeza y hombros sobre fondo gris liso, luz dura rasante desde la izquierda que deja ver poros, piel documental sin retoque.

- Facetas (lista aprobada): F10 génesis sin referencias (caso 1, T1) · F15 persona · F32 sin texto · F04 retrato · F13 A pose sostenida
- Formato: 4:5 · tamaño de referencia 1024x1280 · quality high
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "interior", "entorno": "estudio con fondo continuo gris claro liso"}; cámara {"plano": "CU close-up", "angulo": "eye-level", "efecto_optico": "profundidad de campo corta", "lente_intencion": "85mm feel, sin distorsión de gran angular en la cara"}; luz {"fuente": "una sola luz dura", "direccion": "lateral desde la izquierda de cámara, rasante", "dureza": "dura", "distribucion": "el lado de sombra queda uno o dos pasos más oscuro, sin relleno", "contraste": "alto"}; sujetos [{"id": "mujer", "clase": "persona", "descripcion": "mujer de unos 35 años, cara irregular y algo asimétrica", "edad": 35, "genero": "mujer", "rasgos": ["nariz con una ligera desviación", "ceja izquierda más alta", "pecas irregulares en pómulos", "labios secos"], "cabello": "castaño oscuro, corto a la altura de la mandíbula, con mechones sueltos", "vestuario": "camiseta de algodón gris carbón de cuello redondo", "expresion": "neutra, boca cerrada", "posicion": "centrada, cuerpo girado tres cuartos, mirada a cámara"}]; rostro {"ocupacion": 0.35, "detalles": ["poros visibles", "rojeces en nariz y mejillas", "pigmento desigual"]}
- Restricciones: sin texto ni marcas de agua; sin retoque ni piel de estudio; una sola persona
- Módulos activos: fotografia, sujetos_visibles
- **sha256 del brief:** `5b8a86ff0f84e4e6d1ce9131021c270b4c2a6759569dec1fe403e91b80f82a43`

## K02 · agua abierta con clima, placa vacía

Placa vacía de un lugar genérico: bahía de mar abierto con oleaje suave al atardecer, nubes de tormenta entrando y una cortina de lluvia lejana iluminada por sol rasante. Sin personas ni barcos. Servirá de lugar para K11 (persona sobre el agua), de base para K14 (quitar objeto) y de estilo para K26.

- Facetas (lista aprobada): F10 génesis sin referencias (caso 1, T1) · F15 lugar genérico · F32 sin texto · F04 editorial · F13 D fenómeno de luz o clima · F14 07 luz y clima
- Formato: 3:2 · tamaño de referencia 1536x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "exterior", "entorno": "bahía de mar abierto con oleaje suave y una boya roja aislada a media distancia", "momento": "atardecer", "clima": "tormenta entrando, lluvia lejana", "planos": ["primer plano de agua con textura de oleaje", "boya roja a media distancia", "horizonte con cortina de lluvia y nubes"]}; cámara {"plano": "WS wide", "angulo": "eye-level", "efecto_optico": "todo nítido, sin desenfoque de fondo"}; luz {"fuente": "sol bajo bajo las nubes", "direccion": "contraluz lateral desde la derecha", "dureza": "dura en el agua, difusa en las nubes", "distribucion": "franjas de luz sobre el agua, cielo oscuro", "contraste": "alto"}; sujetos []
- Restricciones: sin personas; sin barcos ni construcciones; sin texto ni marcas de agua; una sola presión ambiental: la tormenta
- Módulos activos: fotografia
- **sha256 del brief:** `5c140f65379b70cdeb2a479d109710fd3d5f1ab76f61c80e6f928fce155907d9`

## K03 · lugar real por época y cultura

Edificación real anclada por época y cultura, sin exigir geometría exacta: la fachada del Palacio de Bellas Artes de Ciudad de México en una mañana de los años cincuenta, vista desde la Alameda, con autos y transeúntes de la época a escala pequeña. Se verifica contra fotos reales lo que el brief declara.

- Facetas (lista aprobada): F10 génesis sin referencias (caso 1, T1) · F15 edificación o landmark · F32 sin texto · F04 editorial · F13 A pose sostenida
- Formato: 3:2 · tamaño de referencia 1536x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "exterior", "entorno": "Alameda Central con árboles y avenida con autos de los años cincuenta", "momento": "media mañana", "clima": "despejado"}; cámara {"plano": "WS wide", "angulo": "eye-level", "efecto_optico": "nitidez de cerca a lejos"}; luz {"fuente": "sol de media mañana", "direccion": "lateral desde la izquierda", "dureza": "dura", "distribucion": "fachada iluminada con sombras de cornisas", "contraste": "medio"}; sujetos [{"id": "palacio", "clase": "edificación o landmark", "descripcion": "Palacio de Bellas Artes, Ciudad de México: fachada de mármol blanco y cúpulas"}]
- Restricciones: sin texto legible ni marcas de agua; personas pequeñas sin rostro reconocible; no se exige geometría exacta del edificio
- Módulos activos: fotografia, sujetos_visibles
- **sha256 del brief:** `a78e0710a1962955e74aa37ae4dd0141e90025789c93be0dd5dc05649572cb02`

## K04 · cabeza y pelaje primero

Animal real: retrato de cabeza de un zorro rojo (Vulpes vulpes) en nieve, mirando a cámara, con pelaje de invierno detallado. Primero cabeza y pelaje (INV-000480). Se verifica anatomía y pelaje contra fotos reales de la especie.

- Facetas (lista aprobada): F10 génesis sin referencias (caso 1, T1) · F15 animal · F32 sin texto · F04 editorial · F13 A pose sostenida
- Formato: 4:5 · tamaño de referencia 1024x1280 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "exterior", "entorno": "bosque nevado desenfocado", "momento": "mañana", "clima": "nieve fina"}; cámara {"plano": "CU close-up", "angulo": "eye-level", "altura": "a la altura de la cabeza del animal", "efecto_optico": "profundidad de campo corta", "lente_intencion": "teleobjetivo, fondo comprimido"}; luz {"fuente": "sol bajo", "direccion": "lateral trasera desde la derecha", "dureza": "dura con borde en el pelaje", "distribucion": "rim de luz en el contorno del pelaje", "contraste": "medio"}; sujetos [{"id": "zorro", "clase": "animal", "descripcion": "zorro rojo adulto, pelaje de invierno espeso, hocico blanco, orejas con dorso negro", "posicion": "cabeza de frente, ligeramente girada"}]
- Restricciones: sin texto ni marcas de agua; anatomía de la especie real
- Módulos activos: fotografia, sujetos_visibles
- **sha256 del brief:** `17cee58213c4330e8583aa9901a20cfc8428d81e1029a7ef9804d7494ee5d21f`

## K05 · vaso de vidrio sin marca, hero frontal

Producto genérico sin marca: un vaso de vidrio liso y vacío, en hero frontal sobre fondo blanco limpio, para catálogo. Es la base de K24 (relleno con física) y del contenido de K26.

- Facetas (lista aprobada): F10 génesis sin referencias (caso 1, T1) · F15 producto · F32 sin texto · F04 e-commerce o catálogo · F13 A pose sostenida
- Formato: 1:1 · tamaño de referencia 1024x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "interior", "entorno": "estudio con fondo blanco opaco y superficie blanca"}; cámara {"plano": "objeto entero", "angulo": "eye-level", "altura": "frontal, a la altura del vaso", "efecto_optico": "nitidez total"}; luz {"fuente": "dos ventanas de luz", "direccion": "laterales y una luz trasera", "dureza": "suave", "distribucion": "bordes del vidrio definidos por reflejos verticales", "contraste": "medio"}; sujetos [{"id": "vaso", "clase": "producto", "descripcion": "vaso de vidrio transparente, recto, liso, sin marca ni grabado, vacío", "posicion": "centrado, frontal"}]
- Restricciones: sin marca, logo ni texto; un solo vaso; sombra de contacto suave
- Módulos activos: fotografia, sujetos_visibles
- **sha256 del brief:** `044492156d9265fe3f8c4d3bac6247ace051282ea2ec2e5d6158380e6244bd18`

## K06 · pelota en el impacto

Objeto en el instante pico: una pelota de tenis aplastada contra las cuerdas de una raqueta en el impacto, con pelusa de fieltro y polvo de arcilla saliendo, a contraluz. Solo la raqueta y la pelota, sin manos.

- Facetas (lista aprobada): F10 génesis sin referencias (caso 1, T1) · F15 objeto o prop · F32 sin texto · F04 key visual de campaña · F13 B instante pico · F14 04 objeto balístico
- Formato: 3:2 · tamaño de referencia 1536x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "exterior", "entorno": "cancha de arcilla desenfocada", "momento": "tarde"}; cámara {"plano": "ECU extreme close-up", "angulo": "eye-level", "altura": "a la altura del punto de impacto", "efecto_optico": "profundidad de campo muy corta, macro", "lente_intencion": "macro"}; luz {"fuente": "sol bajo", "direccion": "contraluz", "dureza": "dura", "distribucion": "polvo y pelusa iluminados en el borde", "contraste": "alto"}; sujetos [{"id": "pelota", "clase": "objeto o prop", "descripcion": "pelota de tenis amarilla deformada contra las cuerdas, fieltro erizado"}, {"id": "raqueta", "clase": "objeto o prop", "descripcion": "marco de raqueta oscuro sin marca con cuerdas deflectadas"}]
- Restricciones: sin manos ni personas; sin marca, logo ni texto; una sola pelota y una sola sombra
- Módulos activos: fotografia, sujetos_visibles, accion_fisica
- **sha256 del brief:** `b34e1816b141661bae6c7b9469ca56e38c5d58d3fad6826a67f4489c89acb47c`

## K07 · especie vegetal real

Planta real: un agave azul (Agave tequilana) maduro en un campo de Jalisco, con hojas azul grisáceo y espinas terminales, al amanecer. Se verifica contra fotos reales de la especie.

- Facetas (lista aprobada): F10 génesis sin referencias (caso 1, T1) · F15 planta o especie vegetal · F32 sin texto · F04 editorial · F13 A pose sostenida
- Formato: 4:5 · tamaño de referencia 1024x1280 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "exterior", "entorno": "campo con hileras de agaves y cerros al fondo, tierra roja", "momento": "amanecer", "clima": "despejado con bruma baja"}; cámara {"plano": "MS medium", "angulo": "high", "altura": "ligeramente por encima de la planta", "efecto_optico": "fondo con desenfoque moderado"}; luz {"fuente": "sol al amanecer", "direccion": "lateral desde la izquierda", "dureza": "dura", "distribucion": "bordes de las hojas iluminados, bruma en el fondo", "contraste": "medio"}; sujetos [{"id": "agave", "clase": "planta o especie vegetal", "descripcion": "agave azul maduro, roseta de hojas rígidas azul grisáceo con espinas en la punta y bordes dentados", "posicion": "centrado en primer plano"}]
- Restricciones: sin personas; sin texto ni marcas de agua; anatomía de la especie real
- Módulos activos: fotografia, sujetos_visibles
- **sha256 del brief:** `b0565bdc229d0e3f27f8d753f41b4496cde1d35e4f02f65fea197f83ac678a36`

## K08 · letrero pintado a mano, no marca

Texto corto del mundo: la fachada de una panadería de barrio con un letrero de madera pintado a mano que dice «Panadería». No es una marca real. Luz de primera hora. Pieza: miniatura; el titular de la miniatura se compone aparte. Es la entrada de K25 (adaptación a otro mercado).

- Facetas (lista aprobada): F10 génesis sin referencias (caso 1, T1) · F15 lugar genérico · F32 texto corto · F04 miniatura · F13 A pose sostenida
- Formato: 16:9 · tamaño de referencia 1536x864 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "exterior", "entorno": "calle empedrada tranquila", "momento": "primera hora de la mañana"}; cámara {"plano": "WS wide", "angulo": "eye-level", "efecto_optico": "letrero nítido"}; luz {"fuente": "sol bajo", "direccion": "lateral desde la derecha", "dureza": "dura", "distribucion": "letrero iluminado", "contraste": "medio"}; sujetos [{"id": "fachada", "clase": "lugar genérico", "descripcion": "fachada de panadería con puerta de madera y escaparate con pan"}]; texto {"literales": ["Panadería"], "posicion": "letrero de madera sobre la puerta", "tipografia": "letras serif blancas pintadas a mano"}
- Restricciones: no extra words, no duplicate text, no watermarks; el único texto es el letrero; ninguna marca real
- Módulos activos: fotografia, sujetos_visibles
- **sha256 del brief:** `308e0e27fd9ca7f4ecbad814075726676e24a5aeac0529c7b55b87af5c688f70`

## K09 · producto con etiqueta genérica

Texto pequeño del mundo: un frasco de miel con etiqueta genérica (no marca real) con texto pequeño: «Miel de azahar», «Peso neto 500 g», «Hecho en Veracruz». Sobre mesa de madera, para catálogo. Quality high. Es la entrada de K19 (traducir texto).

- Facetas (lista aprobada): F10 génesis sin referencias (caso 1, T1) · F15 producto · F32 texto extenso o pequeño · F04 e-commerce o catálogo · F13 A pose sostenida
- Formato: 1:1 · tamaño de referencia 1024x1024 · quality high
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "interior", "entorno": "mesa de madera clara, fondo neutro desenfocado"}; cámara {"plano": "objeto entero", "angulo": "eye-level", "altura": "frontal, a la altura de la etiqueta", "efecto_optico": "etiqueta nítida"}; luz {"fuente": "ventana", "direccion": "lateral desde la izquierda", "dureza": "suave", "distribucion": "miel translúcida iluminada", "contraste": "medio"}; sujetos [{"id": "frasco", "clase": "producto", "descripcion": "frasco de vidrio con miel ámbar, tapa metálica dorada lisa, etiqueta de papel crema", "posicion": "centrado, etiqueta de frente"}]; texto {"literales": ["Miel de azahar", "Peso neto 500 g", "Hecho en Veracruz"], "posicion": "etiqueta frontal, nombre arriba y dos líneas pequeñas debajo", "tipografia": "serif oscura sobre papel crema"}
- Restricciones: no extra words, no duplicate text, no watermarks; texto legible al 100 %; ninguna marca real
- Módulos activos: fotografia, sujetos_visibles
- **sha256 del brief:** `d3e7121a5206f57f8cd1dfd4dbed6f10c7042c4d75e63536bbcfb2838d1d8c5b`
