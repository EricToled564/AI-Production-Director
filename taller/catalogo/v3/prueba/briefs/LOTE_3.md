# Lote 3 de briefs: ediciones K14–K16, K19, K20, K22–K25 (tarea 3)

Cada edición cambia una sola cosa de una imagen de un lote aprobado y lista lo que se preserva. La imagen
a editar aún no existe: se aprueba el contenido (la entrada sin `referencias` más la referencia prevista)
por el «sha256 del contenido», y se aprueba de nuevo cuando exista (PLAN §5, tarea 3). K17, K18 y K21
van con el lote de sus entradas (E5, E6, K30). Lo que no viene de la lista aprobada es propuesta del
sistema.

## K14 · edición: quitar objeto

Quitar un objeto del lugar: sacar la boya roja de la bahía de K02 y llenar su lugar con agua que continúa el oleaje y los reflejos de alrededor. Todo lo demás queda igual. Plantilla: gpt-image.md:96 (INV-002383 corregido); editing.md:10–19.

- Facetas (lista aprobada): F10 edición: quitar objeto · F15 lugar genérico · F32 sin texto · F04 editorial
- Formato: 3:2 · tamaño de referencia 1536x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "quitar la boya roja y llenar su lugar con agua abierta que continúa el oleaje y los reflejos de alrededor", "preservar": ["cielo de tormenta y cortina de lluvia", "dirección y color de la luz del sol bajo", "línea del horizonte", "textura del oleaje en el resto del cuadro", "encuadre y ángulo de cámara"]}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; sin texto ni marcas de agua
- Módulos activos: 
- Referencia 1: K02 · rol: imagen a editar · preservar: cielo de tormenta y cortina de lluvia; dirección y color de la luz del sol bajo; línea del horizonte; textura del oleaje en el resto del cuadro; encuadre y ángulo de cámara
- **sha256 del contenido (referencias pendientes):** `ca921ef7e37d55fa5208c11da64ed0810e7255de3671a59988c74825943686f7`

## K15 · edición: añadir objeto

Añadir un objeto a la edificación de época de K03: un puesto de periódicos de madera de los años cincuenta en la banqueta del primer plano, bajo el primer árbol de la Alameda, a escala de una persona adulta y con la misma luz de media mañana. Plantilla: editing.md:21–27.

- Facetas (lista aprobada): F10 edición: añadir objeto · F15 edificación o landmark · F32 sin texto · F04 editorial
- Formato: 3:2 · tamaño de referencia 1536x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "añadir un puesto de periódicos de madera pintado de verde, de los años cincuenta, en la banqueta del primer plano bajo el primer árbol de la Alameda, del alto de una persona adulta, iluminado por el mismo sol de media mañana desde la izquierda y con su sombra hacia la derecha", "preservar": ["fachada y cúpulas del Palacio de Bellas Artes", "árboles de la Alameda", "autos y transeúntes de la época y su posición", "luz de media mañana desde la izquierda", "encuadre y ángulo de cámara"]}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; los periódicos sin texto legible; sin marcas de agua
- Módulos activos: 
- Referencia 1: K03 · rol: imagen a editar · preservar: fachada y cúpulas del Palacio de Bellas Artes; árboles de la Alameda; autos y transeúntes de la época y su posición; luz de media mañana desde la izquierda; encuadre y ángulo de cámara
- **sha256 del contenido (referencias pendientes):** `14246df20232057a7a577790cd8cf0e8873e1218ad4071a0674b2b58d9495b62`

## K16 · edición: cambiar luz o clima

Cambiar el clima de K03: la mañana despejada pasa a una mañana de lluvia, con cielo cubierto, luz difusa y pavimento mojado que refleja la fachada. La arquitectura y todo lo demás quedan igual. Plantilla: gpt-image.md:98; editing.md:29–46.

- Facetas (lista aprobada): F10 edición: cambiar luz o clima · F15 edificación o landmark · F32 sin texto · F04 editorial
- Formato: 3:2 · tamaño de referencia 1536x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "cambiar solo el clima: de mañana despejada a mañana de lluvia, con cielo cubierto, luz difusa sin sombras duras, lluvia fina y pavimento mojado que refleja la fachada", "preservar": ["arquitectura del Palacio de Bellas Artes exactamente igual", "árboles de la Alameda", "autos y transeúntes de la época y su posición", "encuadre y ángulo de cámara"]}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; sin paraguas ni personas nuevas; una sola presión ambiental: la lluvia; sin marcas de agua
- Módulos activos: 
- Referencia 1: K03 · rol: imagen a editar · preservar: arquitectura del Palacio de Bellas Artes exactamente igual; árboles de la Alameda; autos y transeúntes de la época y su posición; encuadre y ángulo de cámara
- **sha256 del contenido (referencias pendientes):** `55099f18f64cdbc17e15d155ea5d01982a28d9c81b019e91f8d7f00ed6413894`

## K19 · edición: traducir texto

Traducir al inglés el texto de la etiqueta del frasco de K09: «Miel de azahar» → «Orange Blossom Honey», «Peso neto 500 g» → «Net weight 500 g», «Hecho en Veracruz» → «Made in Veracruz». Misma tipografía, tamaño y posición. Plantilla: editing.md:73–78.

- Facetas (lista aprobada): F10 edición: traducir texto · F15 producto · F32 texto extenso o pequeño · F04 e-commerce o catálogo
- Formato: 1:1 · tamaño de referencia 1024x1024 · quality high
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "traducir al inglés las tres líneas de la etiqueta: «Miel de azahar» por «Orange Blossom Honey», «Peso neto 500 g» por «Net weight 500 g» y «Hecho en Veracruz» por «Made in Veracruz»", "preservar": ["frasco, miel y tapa", "mesa de madera y fondo", "luz de ventana desde la izquierda", "tipografía serif oscura, tamaño y posición de cada línea", "papel crema de la etiqueta", "encuadre"]}; texto_marca {"literales": ["Orange Blossom Honey", "Net weight 500 g", "Made in Veracruz"], "posicion": "etiqueta frontal, nombre arriba y dos líneas pequeñas debajo, en el lugar de las originales", "tipografia": "la misma serif oscura de la etiqueta original"}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; no extra words, no duplicate text, no watermarks; texto legible al 100 %; ninguna marca real
- Módulos activos: 
- Referencia 1: K09 · rol: imagen a editar · preservar: frasco, miel y tapa; mesa de madera y fondo; luz de ventana desde la izquierda; tipografía serif oscura, tamaño y posición de cada línea; papel crema de la etiqueta; encuadre
- **sha256 del contenido (referencias pendientes):** `83e2ab4b2045758f483fb5cd9a3c3504fd84bfd4115a89af017a70d93d94e2c7`

## K20 · edición: cambiar vestuario

Cambiar el vestuario de la corredora de K10: solo la ropa pasa a una camiseta de tirantes técnica azul cobalto y unas mallas cortas negras. Rostro, cuerpo, pose, pelo, expresión, zapatillas, fondo y luz quedan igual. Plantilla: gpt-image.md:94 (INV-002382).

- Facetas (lista aprobada): F10 edición: cambiar vestuario · F15 persona · F32 sin texto · F04 post o historia para redes
- Formato: 9:16 · tamaño de referencia 1008x1792 · quality high
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "cambiar solo la ropa: camiseta de tirantes técnica azul cobalto y mallas cortas negras, con la luz y las sombras de la foto para que se vean llevadas de verdad", "preservar": ["rostro exacto", "forma del cuerpo", "pose de la zancada", "cabello", "expresión", "zapatillas blancas", "pista y fondo barrido", "luz desde la derecha de cámara", "ángulo de cámara y encuadre"]}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; sin logos ni texto en la ropa; sin marcas de agua
- Módulos activos: 
- Referencia 1: K10 · rol: imagen a editar · preservar: rostro exacto; forma del cuerpo; pose de la zancada; cabello; expresión; zapatillas blancas; pista y fondo barrido; luz desde la derecha de cámara; ángulo de cámara y encuadre
- **sha256 del contenido (referencias pendientes):** `03eb474cf448e99547ffd95131378a2a3a2eeb3f4399b7f0a9328c72432b91f2`

## K22 · cambio de fondo, misma persona

Cambiar el lugar de la corredora de K10: la pista pasa a un paseo marítimo de concreto con barandal y el mar al fondo, con el mismo barrido horizontal del paneo. La misma persona y la misma luz en la cara y el cuerpo. Plantilla: characters.md:80 (TRM-0511).

- Facetas (lista aprobada): F10 edición de imagen existente (T5) · F15 persona · F32 sin texto · F04 post o historia para redes
- Formato: 9:16 · tamaño de referencia 1008x1792 · quality high
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "cambiar el fondo y el suelo de la pista por un paseo marítimo de concreto con barandal y el mar al fondo, a última hora de la tarde, barrido en horizontal como el fondo original", "preservar": ["rostro exacto", "forma del cuerpo", "pose de la zancada", "cabello", "ropa y zapatillas", "luz en la cara y el cuerpo desde la derecha de cámara", "ángulo de cámara y encuadre"]}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; sin otras personas; sin texto ni logos; sin marcas de agua
- Módulos activos: 
- Referencia 1: K10 · rol: imagen a editar · preservar: rostro exacto; forma del cuerpo; pose de la zancada; cabello; ropa y zapatillas; luz en la cara y el cuerpo desde la derecha de cámara; ángulo de cámara y encuadre
- **sha256 del contenido (referencias pendientes):** `ec655fec5f2b791c36eed783e184f672852e7297cc1701b63284a8ab06f049b1`

## K23 · textura de material

Cambiar la textura de un material en K03: la banqueta del primer plano pasa a adoquín de basalto gris, mate y rugoso. El palacio y todo lo demás quedan igual. Plantilla: editing.md:97–100 (TRM-0518).

- Facetas (lista aprobada): F10 edición de imagen existente (T5) · F15 edificación o landmark · F32 sin texto · F04 editorial
- Formato: 3:2 · tamaño de referencia 1536x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "dar a la banqueta del primer plano textura de adoquín de basalto gris, mate y rugosa", "preservar": ["fachada y cúpulas del Palacio de Bellas Artes", "árboles de la Alameda", "autos y transeúntes de la época y su posición", "luz de media mañana desde la izquierda", "encuadre y ángulo de cámara"]}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; sin marcas de agua
- Módulos activos: 
- Referencia 1: K03 · rol: imagen a editar · preservar: fachada y cúpulas del Palacio de Bellas Artes; árboles de la Alameda; autos y transeúntes de la época y su posición; luz de media mañana desde la izquierda; encuadre y ángulo de cámara
- **sha256 del contenido (referencias pendientes):** `fe574696983b7d255954cded3339b707c20414514f45980e7ba0a49a5ceb40c1`

## K24 · relleno con física

Llenar con física el vaso de K05: agua mineral con gas hasta tres cuartos de la altura del vaso, con refracción, menisco, burbujas finas y condensación en el vidrio, con la misma luz. Plantilla: editing.md:91–95 (TRM-1142).

- Facetas (lista aprobada): F10 edición de imagen existente (T5) · F15 producto · F32 sin texto · F04 e-commerce o catálogo
- Formato: 1:1 · tamaño de referencia 1024x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "llenar el vaso con agua mineral con gas hasta tres cuartos de su altura, con refracción del fondo a través del agua, menisco en el borde del líquido, burbujas finas y condensación en el vidrio, con la luz existente", "preservar": ["forma, tamaño y posición del vaso", "fondo y superficie blancos", "luces laterales y trasera", "sombra de contacto suave", "encuadre"]}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; sin hielo, rodajas ni salpicaduras; sin marca, logo ni texto; sin marcas de agua
- Módulos activos: 
- Referencia 1: K05 · rol: imagen a editar · preservar: forma, tamaño y posición del vaso; fondo y superficie blancos; luces laterales y trasera; sombra de contacto suave; encuadre
- **sha256 del contenido (referencias pendientes):** `b8c92e8fa968d843b6041afa97050714a58a93a836e5ea05dc60b13b29521959`

## K25 · adaptación de anuncio a otro mercado

Adaptar la miniatura de K08 al mercado francés con la plantilla de adaptación cultural: la calle pasa a una calle de París con adoquines y fachadas de piedra clara, y el letrero dice «Boulangerie». La plantilla junta en un cambio el lugar y el texto; se conservan la fachada de la panadería, su composición y la luz. Plantilla: editing.md:80–86 (TRM-0520).

- Facetas (lista aprobada): F10 edición de imagen existente (T5) · F15 lugar genérico · F32 texto corto · F04 miniatura
- Formato: 16:9 · tamaño de referencia 1536x864 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "adaptar al mercado francés: la calle pasa a una calle de París con adoquines y fachadas de piedra clara, y el letrero de madera dice «Boulangerie»", "preservar": ["fachada de la panadería, puerta de madera y escaparate con pan", "posición y forma del letrero", "letras serif blancas pintadas a mano", "luz de primera hora desde la derecha", "composición y encuadre"]}; texto_marca {"literales": ["Boulangerie"], "posicion": "letrero de madera sobre la puerta, en el lugar del original", "tipografia": "las mismas letras serif blancas pintadas a mano"}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; no extra words, no duplicate text, no watermarks; el único texto es el letrero; ninguna marca real
- Módulos activos: 
- Referencia 1: K08 · rol: imagen a editar · preservar: fachada de la panadería, puerta de madera y escaparate con pan; posición y forma del letrero; letras serif blancas pintadas a mano; luz de primera hora desde la derecha; composición y encuadre
- **sha256 del contenido (referencias pendientes):** `301b98b93baf07805e7f9992cac0bfc519e6ba79418bfc8c9303cbc4bbc50eb5`
