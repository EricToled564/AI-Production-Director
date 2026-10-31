# Búsqueda de huecos de la taxonomía (2026-10-31)

Orden de Eric: buscar las categorías que el corpus usa para describir un caso y que la taxonomía no tiene (ejemplo: «atardecer»).

## Método

1. **Universo.** Textos de imagen del corpus: `skills/image/**` (sin licencias), los adaptadores de modelos de imagen de visual-prompt-forge, sus referencias y sus ejemplos. Son 2,039 textos de 40 documentos.
2. **Frases candidatas.** Se sacaron todas las palabras y combinaciones de 2 y 3 palabras que aparecen en 3 textos o más: 2,662.
3. **Lo que la taxonomía ya cubre.** Se compararon con todos los nombres, alias y valores de la taxonomía actual (1,729 registros). Quedan sin cubrir 1,962 frases.
4. **Revisión a mano.** Se revisaron las 1,962 frases una por una. La mayoría no son descriptores del caso: firmas de autor, licencias, URL, palabras de función, nombres de campos o frases de un solo ejemplo. Los descriptores que sí lo son se agruparon en familias.
5. **Conteo final.** Cada valor se volvió a contar con límite de palabra en el universo de imagen y en el corpus completo. Para cada uno se separa:
   - **prosa:** párrafo, lista, tabla o cita;
   - **ejemplo o plantilla:** bloque de código.

Límites:
- La búsqueda es por palabras.
- «Aparece en prosa» no quiere decir que haya una regla que dependa de ese valor; eso lo confirma la clasificación.
- Las frases que salen en menos de 3 textos no se revisaron.

## Huecos encontrados

| Familia | Dónde iría | Valor | Término en el corpus | Textos de imagen | En prosa | En ejemplo o plantilla | Corpus completo | Ejemplos de texto |
|---|---|---|---|---|---|---|---|---|
| Momento del día | luz | hora dorada | golden hour | 24 | 6 | 18 | 43 | INV-002094, INV-002209, INV-002388 |
| Momento del día | luz | tarde | afternoon | 19 | 3 | 16 | 46 | INV-002321, INV-002889, INV-011696 |
| Momento del día | luz | mañana | morning | 7 | 2 | 5 | 19 | INV-002324, INV-002530, INV-002909 |
| Momento del día | luz | luz de día | daylight | 6 | 6 | 0 | 6 | INV-002099, INV-002343, INV-002767 |
| Momento del día | luz | noche | night | 9 | 6 | 3 | 17 | INV-002182, INV-002211, INV-002253 |
| Momento del día | luz | hora azul | blue hour | 3 | 1 | 2 | 3 | INV-002101, INV-002338, INV-003054 |
| Momento del día | luz | atardecer | sunset, dusk | 3 | 2 | 1 | 7 | INV-002182, INV-002209, INV-002249 |
| Clima y atmósfera | física y movimiento congelado | niebla o bruma | fog, mist, haze | 15 | 9 | 6 | 29 | INV-002324, INV-002731, INV-002787 |
| Clima y atmósfera | física y movimiento congelado | vapor | steam | 7 | 4 | 3 | 16 | INV-002830, INV-002835, INV-002842 |
| Clima y atmósfera | física y movimiento congelado | polvo | dust | 5 | 2 | 3 | 12 | INV-002807, INV-002918, INV-003027 |
| Clima y atmósfera | física y movimiento congelado | lluvia | rain | 4 | 3 | 1 | 18 | INV-002253, INV-002606, INV-003075 |
| Clima y atmósfera | física y movimiento congelado | humo | smoke | 3 | 2 | 1 | 29 | INV-002730, INV-002731, INV-002817 |
| Tipo de entorno | F16 Espacio | estudio | studio | 28 | 8 | 20 | 30 | INV-002038, INV-002085, INV-002088 |
| Tipo de entorno | F16 Espacio | calle | street | 22 | 13 | 9 | 30 | INV-002097, INV-002159, INV-002160 |
| Tipo de entorno | F16 Espacio | ciudad o urbano | city, urban | 16 | 12 | 4 | 25 | INV-002253, INV-002527, INV-002740 |
| Tipo de entorno | F16 Espacio | oficina (casi todo de un mismo ejemplo repetido) | office | 17 | 0 | 17 | 49 | INV-011696, INV-011747, INV-011951 |
| Tipo de entorno | F16 Espacio | hogar (casi todo de un mismo ejemplo repetido) | home | 18 | 1 | 17 | 49 | INV-002925, INV-011696, INV-011747 |
| Tipo de entorno | F16 Espacio | tienda | storefront, shop, convenience store | 7 | 4 | 3 | 14 | INV-002338, INV-002871, INV-002873 |
| Tipo de entorno | F16 Espacio | azotea | rooftop | 6 | 5 | 1 | 7 | INV-002767, INV-002824, INV-002885 |
| Tipo de entorno | F16 Espacio | cocina | kitchen | 4 | 2 | 2 | 11 | INV-002184, INV-002740, INV-002824 |
| Tipo de fondo | composición | fondo blanco | white background | 8 | 1 | 7 | 8 | INV-002681, INV-002688, INV-002709 |
| Tipo de fondo | composición | fondo degradado | gradient background | 8 | 2 | 6 | 8 | INV-002702, INV-002706, INV-002924 |
| Tipo de fondo | composición | fondo de estudio | studio background | 5 | 1 | 4 | 5 | INV-002156, INV-002499, INV-002746 |
| Tipo de fondo | composición | fondo liso | solid, plain, clean background | 4 | 2 | 2 | 4 | INV-002245, INV-002401, INV-003035 |
| Tipo de material | materialidad y superficie | metal | metal, chrome, brass, copper, aluminum, steel, silver | 24 | 14 | 10 | 59 | INV-002145, INV-002148, INV-002186 |
| Tipo de material | materialidad y superficie | madera | wood, oak | 21 | 5 | 16 | 55 | INV-002725, INV-002809, INV-002833 |
| Tipo de material | materialidad y superficie | vidrio | glass | 20 | 10 | 10 | 37 | INV-002186, INV-002228, INV-002725 |
| Tipo de material | materialidad y superficie | tejido | linen, denim, cotton, wool, silk | 14 | 11 | 3 | 20 | INV-002321, INV-002498, INV-002696 |
| Tipo de material | materialidad y superficie | plástico o vinilo | plastic, vinyl | 11 | 5 | 6 | 15 | INV-002186, INV-002701, INV-002702 |
| Tipo de material | materialidad y superficie | mármol | marble | 9 | 7 | 2 | 9 | INV-002725, INV-002730, INV-002732 |
| Tipo de material | materialidad y superficie | iridiscente | iridescent | 6 | 1 | 5 | 6 | INV-002895, INV-002899, INV-002938 |
| Tipo de material | materialidad y superficie | piedra | stone | 5 | 4 | 1 | 7 | INV-002731, INV-002824, INV-002868 |
| Tipo de material | materialidad y superficie | cuero | leather | 4 | 4 | 0 | 8 | INV-002868, INV-002875, INV-002918 |
| Tipo de material | materialidad y superficie | cerámica | ceramic | 3 | 2 | 1 | 9 | INV-002146, INV-002833, INV-003212 |
| Familia tipográfica | texto en pantalla | serif | serif | 8 | 6 | 2 | 10 | INV-002781, INV-002847, INV-002959 |
| Familia tipográfica | texto en pantalla | sans-serif | sans-serif | 19 | 11 | 8 | 22 | INV-002344, INV-002481, INV-002644 |
| Familia tipográfica | texto en pantalla | script o cursiva | script, cursive, handwritten | 9 | 7 | 2 | 9 | INV-002644, INV-002875, INV-002959 |
| Familia tipográfica | texto en pantalla | versalitas | small caps | 3 | 0 | 3 | 3 | INV-002951, INV-002958, INV-002972 |
| Atmósfera o mood | dramaturgia o estilo | calma | calm | 21 | 5 | 16 | 67 | INV-002530, INV-002688, INV-011696 |
| Atmósfera o mood | dramaturgia o estilo | lujo o premium | luxury, premium | 16 | 7 | 9 | 20 | INV-002344, INV-002728, INV-002729 |
| Atmósfera o mood | dramaturgia o estilo | dramática | dramatic | 15 | 8 | 7 | 34 | INV-002090, INV-002092, INV-002182 |
| Atmósfera o mood | dramaturgia o estilo | nostálgica | nostalgic | 6 | 5 | 1 | 6 | INV-002107, INV-002129, INV-002324 |
| Atmósfera o mood | dramaturgia o estilo | sombría | moody | 4 | 4 | 0 | 4 | INV-002729, INV-002805, INV-002839 |
| Atmósfera o mood | dramaturgia o estilo | elegante | elegant | 4 | 2 | 2 | 5 | INV-003230, INV-003371, INV-011752 |
| Tipo de pieza | F04 | lookbook | lookbook | 5 | 0 | 5 | 5 | INV-002509, INV-002539, INV-002766 |
| Tipo de pieza | F04 | portada de álbum | album cover | 5 | 2 | 3 | 5 | INV-002524, INV-002865, INV-002867 |
| Tipo de pieza | F04 | lámina artística | art print | 5 | 2 | 3 | 5 | INV-002895, INV-002935, INV-002937 |
| Tipo de pieza | F04 | carrusel | carousel | 3 | 0 | 3 | 3 | INV-002524, INV-002724, INV-002766 |
| Efecto óptico | encuadre y lente | viñeteado | vignette | 5 | 2 | 3 | 8 | INV-002840, INV-002867, INV-003044 |

## Familias que se descartan como categoría

Son dominios abiertos: el valor lo pone cada caso y no se puede enumerar. La guía de casos (`4_diseno/casos/README_CASOS_DE_USO.md`) ya trata edades, posiciones y literales como dominios abiertos.

- **Colores concretos** (navy, teal, cream, gold, amber, coral, emerald…). La taxonomía ya tiene los tipos de paleta.
- **Prendas concretas** (crewneck, shirt, jacket, blazer…). Ya existen «identidad de vestuario» y la edición «cambiar vestuario».
- **Edad, cabello, género y productos concretos** (mid-thirties, salt-and-pepper hair, laptop, coffee cup…).
- **Poses concretas** (leaning forward, standing, holding…). Ya existen postura, gesto y dirección de la mirada.
- **Fotógrafos y estudios de referencia** (Peter Lindbergh, Studio Ghibli). Ya existen el ancla de género o autor y la extensión F17 «anclado en época, cultura o autor».
- **Potenciadores de calidad** (masterpiece, stunning, epic, highly detailed). Ya son vocabulario excluido.

Se descarta además «naturaleza o paisaje». En estos documentos, «landscape» casi siempre es la orientación horizontal, y el resto (beach, forest…) sale en menos de 3 textos.
