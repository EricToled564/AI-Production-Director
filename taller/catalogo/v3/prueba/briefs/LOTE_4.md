# Lote 4 de briefs: entradas E5 y E6, ediciones K17 y K18, transferencia K26 (tarea 3)

E5 y E6 son entradas (génesis de persona con `armar.py`) y se aprueban por el sha256 del brief; sus
facetas son propuesta del sistema. K17, K18 y K26 usan imágenes que aún no existen y se aprueban por el
«sha256 del contenido»; se aprueban de nuevo cuando existan (PLAN §5, tarea 3).

## E5 · foto en blanco y negro de una persona

Entrada de K17 (colorizar): retrato de estudio en blanco y negro de los años cincuenta de una persona inventada (no real). Hombre de unos 30 años, cabeza y hombros, traje oscuro y corbata, luz dura de estudio. Su QA solo comprueba que es blanco y negro y sirve de entrada.

- Facetas (propuesta del sistema: E5 es entrada de K17, no caso (PLAN §4)): F10 génesis sin referencias (caso 1, T1) · F15 persona · F32 sin texto · F04 editorial · F13 A pose sostenida
- Formato: 4:5 · tamaño de referencia 1024x1280 · quality high
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "interior", "entorno": "estudio fotográfico de los años cincuenta con fondo pintado gris moteado"}; cámara {"plano": "CU close-up", "angulo": "eye-level", "efecto_optico": "profundidad de campo corta", "lente_intencion": "85mm feel"}; luz {"fuente": "una luz dura de estudio", "direccion": "desde arriba a la izquierda de cámara", "dureza": "dura", "distribucion": "sombra en lazo bajo la nariz, fondo con luz suave", "contraste": "alto"}; sujetos [{"id": "hombre", "clase": "persona", "descripcion": "hombre de unos 30 años de los años cincuenta", "edad": 30, "genero": "hombre", "rasgos": ["nariz algo desviada", "hoyuelo en el mentón", "lunar pequeño en la mejilla izquierda", "cara ovalada"], "cabello": "oscuro y ondulado, peinado hacia atrás con brillantina", "vestuario": "saco de lana oscuro, camisa blanca y corbata angosta estampada", "expresion": "tranquila, boca cerrada", "posicion": "centrado, cuerpo girado tres cuartos, mirada junto a la lente"}]; rostro {"ocupacion": 0.35, "detalles": ["poros visibles", "grano de película"]}
- Restricciones: en blanco y negro, sin color; sin texto ni marcas de agua; una sola persona
- Módulos activos: fotografia, sujetos_visibles
- **sha256 del brief:** `c524428fbc800e0baf3dffd117fd4ec6bd045b084e2d0214bb779e9896b688ed`

## E6 · foto antigua dañada de una persona

Entrada de K18 (restaurar): copia en sepia de los años treinta, dañada, con el retrato de una persona inventada (no real). Mujer de unos 20 años, cabeza y hombros. Daños: rotura diagonal en la esquina inferior derecha, un pliegue, rayones finos, una mancha de agua en el borde superior y luces desvanecidas. Su QA solo comprueba que está dañada y sirve de entrada.

- Facetas (propuesta del sistema: E6 es entrada de K18, no caso (PLAN §4)): F10 génesis sin referencias (caso 1, T1) · F15 persona · F32 sin texto · F04 editorial · F13 A pose sostenida
- Formato: 4:5 · tamaño de referencia 1024x1280 · quality high
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "interior", "entorno": "estudio fotográfico de los años treinta con fondo pintado liso; la copia en papel tiene rotura, pliegue, rayones, mancha de agua y luces desvanecidas"}; cámara {"plano": "CU close-up", "angulo": "eye-level", "efecto_optico": "profundidad de campo corta", "lente_intencion": "85mm feel"}; luz {"fuente": "una luz de estudio de borde suave", "direccion": "desde la izquierda de cámara", "dureza": "suave", "distribucion": "el lado derecho de la cara cae en una sombra suave", "contraste": "medio"}; sujetos [{"id": "mujer", "clase": "persona", "descripcion": "mujer de unos 20 años de los años treinta", "edad": 20, "genero": "mujer", "rasgos": ["cara redonda de mejillas llenas", "nariz estrecha", "cicatriz pequeña en el mentón"], "cabello": "oscuro y corto, con ondas al agua de los años treinta", "vestuario": "blusa clara de cuello redondo y una cadena delgada al cuello", "expresion": "sonrisa leve con la boca cerrada", "posicion": "centrada, de frente, cabeza un poco inclinada"}]; rostro {"ocupacion": 0.35, "detalles": ["grano de plata", "textura del papel"]}
- Restricciones: copia en sepia dañada: rotura, pliegue, rayones, mancha y desvanecido; la rotura lejos del rostro; sin texto ni marcas de agua; una sola persona
- Módulos activos: fotografia, sujetos_visibles
- **sha256 del brief:** `b038aeabb8689d91054a30b6e7e15e40f69a522cd2d5a4b72a8e9dcb87fa83ed`

## K17 · edición: colorizar

Colorizar la foto en blanco y negro de E5 con colores propios de los años cincuenta y tonos de piel naturales. Todo lo demás queda igual. Plantilla: editing.md:48–55.

- Facetas (lista aprobada): F10 edición: colorizar · F15 persona · F32 sin texto · F04 editorial
- Formato: 4:5 · tamaño de referencia 1024x1280 · quality high
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "colorear la foto en blanco y negro con colores propios de los años cincuenta y tonos de piel naturales", "preservar": ["rostro e identidad", "peinado", "pose y expresión", "forma de la ropa", "luz y sombras", "grano de película", "encuadre"]}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; sin texto ni marcas de agua
- Módulos activos: 
- Referencia 1: E5 · rol: imagen a editar · preservar: rostro e identidad; peinado; pose y expresión; forma de la ropa; luz y sombras; grano de película; encuadre
- **sha256 del contenido (referencias pendientes):** `364047b7c1ebe10abb09503297acc17ea51dfa3164ca0cc6deea28deac3a1249`

## K18 · foto antigua dañada de una persona

Restaurar la copia dañada de E6: reparar rotura, pliegue, rayones, mancha y desvanecido, y recuperar nitidez y contraste, conservando el carácter y el grano de la época. Plantilla: editing.md:65–71.

- Facetas (lista aprobada): F10 edición: restaurar · F15 persona · F32 sin texto · F04 editorial
- Formato: 4:5 · tamaño de referencia 1024x1280 · quality high
- Propuesto por el sistema (inferencia para aprobación): edicion {"cambio": "restaurar la copia: reparar la rotura, el pliegue, los rayones, la mancha de agua y el desvanecido, y recuperar nitidez y contraste", "preservar": ["rostro e identidad", "peinado", "pose y expresión", "blusa y collar", "tono sepia", "grano original de la época", "encuadre"]}
- Restricciones: sin objetos nuevos fuera del cambio; sin rediseño; sin deriva de color, contraste ni encuadre; sin colorear; sin texto ni marcas de agua
- Módulos activos: 
- Referencia 1: E6 · rol: imagen a editar · preservar: rostro e identidad; peinado; pose y expresión; blusa y collar; tono sepia; grano original de la época; encuadre
- **sha256 del contenido (referencias pendientes):** `fc7faba3a702870d840442904b9ec81c3da2dd612237f353072f33b633cb3b23`

## K26 · transferencia de estilo

Transferencia de estilo: el vaso de K05 (contenido, Image 1) con el estilo de la bahía de K02 (Image 2): su paleta de gris acero, azul pizarra y franjas ámbar, su contraluz lateral duro, sus sombras sin relleno, su contraste alto y su bruma fina. No se copia el contenido de K02. Key visual. Plantilla: gpt-image.md Style Transfer (INV-002389–002390), referencias con rol (INV-002386–002388).

- Facetas (lista aprobada): F10 transferencia de estilo · F15 producto · F32 sin texto · F04 key visual de campaña
- Formato: 1:1 · tamaño de referencia 1024x1024 · quality usuario
- Propuesto por el sistema (inferencia para aprobación): escena {"espacio": "interior", "entorno": "superficie de piedra oscura mojada y fondo degradado gris tormenta"}; cámara {"plano": "objeto entero", "angulo": "eye-level", "altura": "frontal, a la altura del vaso", "efecto_optico": "nitidez total"}; luz {"fuente": "una sola luz baja", "direccion": "contraluz lateral desde la derecha, como el sol de la imagen 2", "dureza": "dura", "distribucion": "franjas brillantes en el borde del vidrio y en la superficie mojada, frente del vaso en penumbra", "contraste": "alto"}; sujetos [{"id": "vaso", "clase": "producto", "descripcion": "el vaso de la imagen 1: vidrio transparente, recto, liso, sin marca, vacío", "posicion": "centrado, frontal"}]
- Restricciones: no copiar el contenido de la imagen 2: sin mar, boya, nubes ni horizonte; un solo vaso; sin marca, logo ni texto; sin marcas de agua
- Módulos activos: fotografia, sujetos_visibles
- Referencia 1: K05 · rol: contenido: el vaso · preservar: forma y proporción del vaso; vidrio liso y transparente; vaso vacío
- Referencia 2: K02 · rol: estilo: paleta, luz, contraste y bruma; no su contenido · preservar: paleta gris acero, azul pizarra y ámbar; contraluz lateral duro; sombras sin relleno
- **sha256 del contenido (referencias pendientes):** `daee1340a90ed78bf0dae6c287ea15b3711139ebd0bab570fb9c909a1854406a`
