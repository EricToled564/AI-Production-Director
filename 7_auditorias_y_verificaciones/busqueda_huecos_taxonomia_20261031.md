# Búsqueda de huecos de la taxonomía (2026-10-31)

Orden de Eric: buscar las categorías que el corpus usa para describir un caso y que la taxonomía no tiene (ejemplo: «atardecer»).

## Método

1. **Universo.** Textos de imagen del corpus: `skills/image/**` (sin licencias), los adaptadores de modelos de imagen de visual-prompt-forge, sus referencias y sus ejemplos. Son 2,039 textos de 40 documentos.
2. **Frases candidatas.** Se sacaron todas las palabras y combinaciones de 2 y 3 palabras que aparecen en 3 textos o más: 2,662.
3. **Lo que la taxonomía ya cubre.** Se compararon con todos los nombres, alias y valores de la taxonomía actual (1,729 registros). Quedan sin cubrir 1,962 frases. Este paso no leía las definiciones; la comprobación con lectura completa está en la sección «Lo que ya tiene la taxonomía».
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

## Lo que ya tiene la taxonomía (lectura completa)

Corrección del 2026-10-31: la primera versión de este informe solo comparó frases con nombres y alias. Esta sección sale
de leer completos los 1,729 registros de la taxonomía (nombre, alias y definición; `4_diseno/casos/catalogo_opciones.json`),
más las extensiones de la propuesta (F32 a F35). Se leyó cada registro, no solo los que coincidían con una palabra.

Estados:
- **Falta:** ningún registro lo menciona.
- **Solo como ejemplo:** aparece dentro de la definición de otra categoría de imagen, sin valor propio que el sistema pueda rastrear.
- **Solo fuera de imagen:** aparece solo en categorías de audio o de guion.
- **Existe en parte:** hay un valor propio, pero más estrecho que el hueco.

Ninguno de los 49 valores existe completo. Resultado: 21 faltan, 22 están solo como ejemplo, 4 solo fuera de imagen y 2 existen en parte.

| Familia | Valor | Estado | Lo que hay en la taxonomía |
|---|---|---|---|
| Momento del día | hora dorada | Falta | — |
| Momento del día | tarde | Falta | — |
| Momento del día | mañana | Falta | — |
| Momento del día | luz de día | Solo como ejemplo | Opción citada en Balance de blancos (TRM-0386); DAY en Circunstancia temporal de escena (TRM-0978, guion) |
| Momento del día | noche | Solo fuera de imagen | NIGHT en TRM-0978 (guion). La luz tiene Luz lunar (TRM-0333), que es una fuente, no el momento |
| Momento del día | hora azul | Solo como ejemplo | Ejemplo en Luz ambiente continua (TRM-1244) |
| Momento del día | atardecer | Solo fuera de imagen | DUSK en TRM-0978 (guion) |
| Clima y atmósfera | niebla o bruma | Solo como ejemplo | Fenómeno meteorológico (TRM-0124), «07 luz y clima» (F14), Bloque de iluminación (TRM-0538), Difusión (TRM-0362). Fog y Pro-Mist (TRM-1165 a 1168) son filtros ópticos, no clima |
| Clima y atmósfera | vapor | Existe en parte | Vapor a contraluz (TRM-0378), solo a contraluz; ejemplo en Partículas (TRM-0651) |
| Clima y atmósfera | polvo | Solo como ejemplo | Partículas (TRM-0651), «07 luz y clima» (F14) |
| Clima y atmósfera | lluvia | Solo como ejemplo | TRM-0124, TRM-0651, «07 luz y clima» (F14) |
| Clima y atmósfera | humo | Solo como ejemplo | TRM-0538, Estela (TRM-0648), Luz de baño (TRM-1238) |
| Tipo de entorno | estudio | Solo como ejemplo | Lugar genérico (TRM-0136) |
| Tipo de entorno | calle | Solo como ejemplo | Lugar genérico (TRM-0136); «calle llena» en «08 multitud anónima» (F14) |
| Tipo de entorno | ciudad o urbano | Solo fuera de imagen | Ambiente (TRM-0761) y SFX de ambiente (TRM-0232), ambos de audio |
| Tipo de entorno | oficina | Solo como ejemplo | Fluorescente (TRM-0337) |
| Tipo de entorno | hogar | Falta | «Tragedia doméstica» (F07) es un género narrativo, no un lugar |
| Tipo de entorno | tienda | Solo como ejemplo | Suciedad (TRM-0492). «Retail y supermercado» (F05) es temática, no lugar |
| Tipo de entorno | azotea | Falta | — |
| Tipo de entorno | cocina | Solo como ejemplo | Lugar genérico (TRM-0136), LED de techo (TRM-0336), Refrigerador (TRM-0341) |
| Tipo de fondo | fondo blanco | Solo como ejemplo | Fondo opaco (TRM-1263) |
| Tipo de fondo | fondo degradado | Falta | Divisor degradado (TRM-1111) separa zonas; no es un fondo |
| Tipo de fondo | fondo de estudio | Falta | — |
| Tipo de fondo | fondo liso o limpio | Solo como ejemplo | Mockup (TRM-0015), character ref (TRM-0099), Maestro de identidad (TRM-0478) |
| Tipo de material | metal | Solo como ejemplo | Cobre en Pátina (TRM-0490) |
| Tipo de material | madera | Falta | Grabado en madera (TRM-0169) es una técnica |
| Tipo de material | vidrio | Solo como ejemplo | Estilo Glassmorfismo (TRM-0157); ejemplos en Suciedad, Condensación, Gotas adheridas y Cáusticas |
| Tipo de material | tejido | Existe en parte | Trama textil (TRM-0496), Caída de tejido (TRM-1176): propiedades del tejido; no hay tipos de tela |
| Tipo de material | plástico o vinilo | Solo como ejemplo | Vinilo en Identidad de personaje estilizado (TRM-0471). Plastilina (TRM-1052) es técnica |
| Tipo de material | mármol | Falta | — |
| Tipo de material | iridiscente | Falta | — |
| Tipo de material | piedra | Falta | — |
| Tipo de material | cuero | Falta | — |
| Tipo de material | cerámica | Solo como ejemplo | Esmalte cerámico en Imperfección material (TRM-0493) |
| Familia tipográfica | serif | Falta | — |
| Familia tipográfica | sans-serif | Falta | — |
| Familia tipográfica | script o cursiva | Falta | — |
| Familia tipográfica | versalitas | Falta | — |
| Atmósfera o mood | calma | Solo fuera de imagen | «Tranquila» en Entrega interpretativa (TRM-0966, voz) |
| Atmósfera o mood | lujo o premium | Solo como ejemplo | Tono de pieza (TRM-0558, marca); Futurista/SaaS (TRM-0158) |
| Atmósfera o mood | dramática | Falta | La dramaturgia trata emoción narrativa (p. ej. Contraste dramático, TRM-0593), no la atmósfera de la imagen |
| Atmósfera o mood | nostálgica | Solo como ejemplo | Cámara desechable (TRM-0302). «Retro o vintage» (F17) es estilo de época |
| Atmósfera o mood | sombría | Falta | — |
| Atmósfera o mood | elegante | Falta | — |
| Tipo de pieza | lookbook | Solo como ejemplo | Moda (TRM-0055, F05) |
| Tipo de pieza | portada de álbum | Solo como ejemplo | «Portadas» en Música (TRM-0054, F05) |
| Tipo de pieza | lámina artística | Falta | Lámina científica vintage (TRM-1062) es un estilo; las «láminas» de F04 son diapositivas |
| Tipo de pieza | carrusel | Solo como ejemplo | Instagram (PLT-02) y LinkedIn (PLT-06) en publicación |
| Efecto óptico | viñeteado | Falta | Tira de viñetas (TRM-1086) es cómic |

Categorías que ya existen y bajo las que caerían los valores:
- **Clima:** Fenómeno meteorológico (TRM-0124), «D fenómeno de luz o clima» (F13), «07 luz y clima» (F14), Partículas atmosféricas (TRM-1175) y Cielo cubierto (TRM-0332). Además, las operaciones Cambio meteorológico (TRM-0514) y Cambio de estación (TRM-0513). Faltan los valores por tipo de clima.
- **Entorno:** F16 solo tiene interior y exterior; Lugar genérico (TRM-0136) nombra ejemplos sin valores.
- **Fondo:** Fondo (TRM-0433) es la capa espacial; Fondo opaco (TRM-1263) y Fondo de paleta de marca (TRM-1287) son los únicos tipos.
- **Material:** la materia «materialidad y superficie» tiene propiedades (mate, brillante, satinada, translucidez, reflexión, pátina…), la referencia Material (TRM-0750) y la operación Cambio de material (TRM-0518). No tiene tipos de material.
- **Tipografía:** roles de marca (TRM-0560, TRM-1289 a 1291) y tamaños y pesos de texto en pantalla (TRM-1024 a 1034). No tiene familias.
- **Mood:** solo de marca (Adjetivo de mood TRM-0568, Tono de pieza TRM-0558). El modo de prompt Detallado (TRM-1225) tiene un apartado de ánimo sin valores.
- **Momento del día:** «Luz natural y ambiente» tiene Luz solar directa, Cielo cubierto, Luz lunar, Ventana y Luz ambiente continua. Amanecer aparece como ejemplo en Fenómeno luminoso (TRM-0123) y en F14 «07 luz y clima».

## Familias que se descartan como categoría

Son dominios abiertos: el valor lo pone cada caso y no se puede enumerar. La guía de casos (`4_diseno/casos/README_CASOS_DE_USO.md`) ya trata edades, posiciones y literales como dominios abiertos.

- **Colores concretos** (navy, teal, cream, gold, amber, coral, emerald…). La taxonomía ya tiene los tipos de paleta.
- **Prendas concretas** (crewneck, shirt, jacket, blazer…). Ya existen «identidad de vestuario» y la edición «cambiar vestuario».
- **Edad, cabello, género y productos concretos** (mid-thirties, salt-and-pepper hair, laptop, coffee cup…).
- **Poses concretas** (leaning forward, standing, holding…). Ya existen postura, gesto y dirección de la mirada.
- **Fotógrafos y estudios de referencia** (Peter Lindbergh, Studio Ghibli). Ya existen el ancla de género o autor y la extensión F17 «anclado en época, cultura o autor».
- **Potenciadores de calidad** (masterpiece, stunning, epic, highly detailed). Ya son vocabulario excluido.

Se descarta además «naturaleza o paisaje». En estos documentos, «landscape» casi siempre es la orientación horizontal, y el resto (beach, forest…) sale en menos de 3 textos.
