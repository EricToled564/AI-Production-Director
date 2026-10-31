# Investigación y prueba del nivel 1 de la taxonomía para imágenes (2026-10-30)

Orden de Eric: investigar las mejores prácticas, probar con ejemplos reales y decidir con esa evidencia. Resultado
aplicado en `3_taxonomia/TAXONOMIA_CANONICA.md`, nivel 1.

## 1. Investigación

Todas las fuentes de esta tabla se leyeron completas: se descargaron y se leyó su texto entero. Hay dos excepciones:
- *The Prompt Report*: solo §1 a §1.3, que es su terminología.
- NISO Z39.19: §2.5, §2.6, §5 completo, §6.2.2 a §6.2.3 y §11.1 a §11.2. Lo que no se leyó trata de la forma gramatical de los términos, términos compuestos, relaciones entre términos del tesauro y su presentación.

La página de Anthropic *Use prompt templates and variables*, citada en la versión anterior de este archivo, ya no existe:
redirige a otra página. Por eso se quitó.

| Fuente | Qué dice (leído completo) | Qué se decidió con eso |
|---|---|---|
| A. Fitzgerald, *Purpose-Driven Taxonomy Design* (2025) | El error común es hacer una taxonomía «of» un tema y no «for» un propósito: primero objetivos y usos, después estructura. Evitar la polijerarquía sin razón. Una categoría que vale para todo («all content») no acota. Definir cada término uno mismo. Probar con contenido real, etiquetando 5 piezas y siguiendo el resultado | El nivel 1 se ordena por lo que se hace con cada texto: cómo entra al prompt. Cada valor con definición. Prueba con 24 textos reales |
| H. Hedden, *Faceted Classification and Faceted Taxonomies* (2024) | Un concepto pertenece a una sola faceta. «A logical and practical number of facets tends to be in the range of three to seven». La mayoría de las facetas debe aplicar a la mayoría del contenido | 5 facetas en el nivel 1. «Qué es» queda solo para lo que no impacta, y los tipos de documento salen del nivel 1 |
| Nielsen Norman Group, *Taxonomy 101* | Lista cerrada de términos. Hacer inventario del contenido, buscar primero una taxonomía estándar, evitar términos con muy poco contenido, revisar con los expertos y mantenerla con gobierno | Los valores de «qué es» salen de lo observado en el corpus. La propuesta pasa por Eric |
| Wikipedia, *Faceted classification* | Facetas «clearly defined, mutually exclusive, and collectively exhaustive aspects». Se pueden crear facetas nuevas sin desarmar las demás | Facetas que no se pisan. Las extensiones (F32–F35) entran como facetas nuevas |
| ANSI/NISO Z39.19-2005 (R2010) | Cada término con un solo significado. La nota de alcance dice el significado elegido y lo que se excluye. Facetas para atributos del contenido; con menos de unos cien términos basta una lista simple. Elegir términos por «warrant» del propio contenido. Probar y evaluar periódicamente | Cada efecto lleva «incluye» y «no incluye» (estilo visual frente a forma de redacción). Listas simples para facetas pequeñas. Valores tomados del corpus |
| ANSI/NISO Z39.19, §11.1–11.2 | No duplicar vocabularios existentes; decidir la estructura antes de reunir términos; para un vocabulario nuevo, de lo general a lo particular. Para evaluar: que varias personas indexen los mismos ítems, porque «disagreements can point out problems in the controlled vocabulary» | Se reutilizan las categorías de la taxonomía actual. El nivel 1 se fijó antes de clasificar. Antes de clasificar a escala, una prueba de concordancia: dos clasificaciones independientes de los mismos textos, y cada desacuerdo se resuelve en la definición |
| Schulhoff et al., *The Prompt Report* (arXiv 2406.06608), §1 | Componentes del prompt: directiva, ejemplos, formato de salida, instrucciones de estilo («a type of output formatting»), rol, información adicional. «A prompt template is a function that contains one or more variables». Una técnica puede tener lógica condicional o de ramas | Efecto «da un ejemplo o una plantilla». La forma de redacción separada del contenido. El template con variables que se llenan desde el brief |
| J. Oppenlaender, *A Taxonomy of Prompt Modifiers for Text-to-Image Generation* (2023) | Seis tipos de modificadores: sujeto, estilo, prompt de imagen, potenciador de calidad, repetición y términos mágicos. El sujeto es obligatorio y el resto opcional. Pesos negativos para excluir | En imagen, estilo y calidad son contenido de la imagen y entran en «agrega contenido». Las exclusiones van en «fija restricciones» |
| V. Liu y L. Chilton, *Design Guidelines for Prompt Engineering Text-to-Image Generative Models* (CHI 2022) | Prompts como plantilla con parámetros («SUBJECT in the style of STYLE»). Las palabras de enlace no cambiaron la calidad; sí el sujeto y el estilo. Generar 3 a 9 variantes | El prompt es una plantilla que se llena con datos del caso, lo que respalda el destino «template + llenado» |
| OpenAI, *Image generation models prompting guide* (cookbook, archivada) | Orden «background/scene → subject → key details → constraints». «State exclusions and invariants explicitly». Edición: «change only X» + «keep everything else the same». Fundamentos generales más guías por caso de uso (infografías, logos, anuncios, UI, cómics, edición, transferencia de estilo, prueba virtual de ropa, eliminar objetos…) | «Establece un orden». «Fija restricciones» incluye lo que se preserva. Lo general va al template; lo de cada caso de uso u operación se inserta al fijarse en el brief |
| MindStudio, *Static vs Dynamic Context in AI Agents* | Lo fijo debe ser universal, pequeño y estable; las reglas críticas, fijas. Bloques condicionales que se cargan cuando el flujo detecta el tipo de tarea. Lo grande o variable, por recuperación. Las capas no deben contradecirse | Template para lo universal, con instrucciones y no texto copiado. Inserción mecánica por datos del brief. Selección solo para lo que hay que interpretar |
| Decisión de Eric, `5_decisiones/DECISIONES_ERIC_20261023.md` §4 | Las plantillas de un look son biblioteca: se ofrecen por tipo de pieza y estilo y se confirma como máximo una | Destino «biblioteca de plantillas» |

## 2. Prueba con 24 textos reales

Muestra al azar (semilla 20261030) de los 1,135 textos de párrafo, lista, tabla, código y cita del universo de imagen
(decisión del 23 de octubre §1).

| Texto | Documento | Lo que dice (resumen) | Impacta | Efecto | Entra por | Qué es (si no impacta) |
|---|---|---|---|---|---|---|
| INV-002072 | characters.md L67 | «Mid-stride, dynamic motion» (control de pose) | Sí | Ejemplo | Selección (hay que interpretar qué acción es) | — |
| INV-002103 | creative-direction.md L28 | Nombrar el tipo de cámara cambia el ADN visual | Sí | Agrega contenido | Template | — |
| INV-002217 | editing.md L51 | Plantilla de colorización con [DECADE] | Sí | Ejemplo o plantilla; agrega contenido | Inserción mecánica (edición: colorizar) | — |
| INV-002323 | golden-rules.md L176 | «Cultural anchor + новый контекст:» | No | — | — | Rótulo |
| INV-002372 | gpt-image.md L74 | Texto pequeño, denso o con varias fuentes → quality high obligatorio | Sí | Fija un parámetro | Inserción mecánica (F32 texto extenso o pequeño) | — |
| INV-002374 | gpt-image.md L78 | Endpoint `openai/gpt-image-2/edit` | No | — | — | Dato técnico de interfaz |
| INV-002390 | gpt-image.md L113 | No escribir en abstracto; nombrar propiedades visuales concretas de la referencia | Sí | Fija restricciones; agrega contenido | Template (GPT Image 2, transferencia de estilo) | — |
| INV-002429 | models.md L18 | Storyboard con foco tipográfico → GPT Image 2 | Sí | Fija un parámetro (modelo) | Inserción mecánica (tipo de pieza) | — |
| INV-002586 | multi-panel.md L306 | Más paneles, menos detalle; 12 paneles: 3–8 palabras cada uno | Sí | Fija la forma | Selección (número de paneles, valor abierto) | — |
| INV-002704 | character-design.md L108 | Chibi: GPT Image 2 con quality medium; high para close-ups de marketing | Sí | Fija un parámetro | Biblioteca de plantillas | — |
| INV-002731 | ecommerce.md L33 | Plantilla completa de cosmético de lujo con huecos | Sí | Plantilla | Biblioteca de plantillas | — |
| INV-002773 | fashion-editorial.md L37 | Plantilla de retrato editorial 2x2 | Sí | Plantilla | Biblioteca de plantillas | — |
| INV-002786 | fashion-editorial.md L81 | Comentario HTML «Source concept: …» | No | — | — | Nota interna o de origen |
| INV-002882 | portrait-cinema.md L61 | «Key levers»: los huecos de la plantilla y sus opciones | Sí | Agrega contenido | Biblioteca de plantillas | — |
| INV-002912 | poster-illustration.md L32 | Versión Nano Banana de una plantilla de póster | Sí | Plantilla | Biblioteca de plantillas (F29 Nano Banana) | — |
| INV-002929 | poster-illustration.md L88 | «Use for fashion drops, event announcements…» | No | — | — | Condición de uso de una plantilla |
| INV-002963 | ui-social.md L55 | «Use to create a polished App Store…» | No | — | — | Condición de uso de una plantilla |
| INV-003137 | slides.md L144 | Colores de texto #ffffff, #e0e0e0 | Sí | Agrega contenido | Biblioteca de plantillas (paleta) | — |
| INV-003138 | slides.md L146 | «Light palette:» | No | — | — | Rótulo |
| INV-003147 | slides.md L158 | «Subtle gradient haze» | Sí | Ejemplo | Selección (elegir efecto) | — |
| INV-003214 | slides.md L301 | Especificación glassmorphism (material, bordes, sombra) | Sí | Agrega contenido | Biblioteca de plantillas | — |
| INV-003408 | vision-decomposer.md L26 | Tamaños de plano para describir la imagen | Sí | Agrega contenido | Inserción mecánica (operación: análisis de imagen a prompt) | — |
| INV-011730 | adapters/gpt-image.md L27 | `style`: natural para foto, vivid para estilizado | Sí | Fija un parámetro | Inserción mecánica (F18 técnica) | — |
| INV-011745 | adapters/gpt-image.md L62 | «Same shot data as previous examples.» | No | — | — | Nota interna o de origen |

También se probaron los textos vistos antes: INV-011267 (impacta, fija la forma, template), INV-008288 (control o
validación), INV-011268 (descripción) e INV-001428 (código).

## 3. Lo que decidió la prueba

- **Impacto.** 17 de 24 impactan y 7 no.
- **Efecto.** Aparecieron cinco efectos. «Establece un orden» no salió en la muestra, pero está en la guía de OpenAI y en
  los apartados de GPT Image 2.
- **Cómo entra al prompt.** De los 17 que impactan, 2 van al template, 5 a inserción mecánica, 7 a la biblioteca y 3 a
  selección.
  - La biblioteca no estaba en la propuesta anterior. Es la decisión de Eric del 23 de octubre.
  - La inserción mecánica no se queda en el tipo de pieza: también la piden la operación, F32 y F18, todas listas
    cerradas.
- **Qué es (si no impacta).** Los 7 que no impactan y los 3 vistos antes caben en 8 valores que salen de lo observado.
  Los tipos de documento de la base (referencia, SKILL, etc.) ya se ven en el nivel 2, así que se quitan del nivel 1
  para no mezclar facetas.
- **Límite.** La muestra es de 24 textos de un solo universo. Si la clasificación encuentra un texto que no cabe en
  ningún valor, se informa, no se fuerza.

## 4. Corrección del 2026-10-30 (orden de Eric)

El brief no se clasifica: lo que debe entregar sale de la taxonomía (nivel 3) y de los campos de los templates. Se quitó la faceta «dónde actúa» y la columna correspondiente de la tabla §2. Los dos textos que estaban marcados «brief» quedan así: INV-002429 fija un parámetro (modelo) por tipo de pieza; INV-002882 da los huecos de una plantilla de la biblioteca.
