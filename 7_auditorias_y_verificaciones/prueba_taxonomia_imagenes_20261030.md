# Investigación y prueba del nivel 1 de la taxonomía para imágenes (2026-10-30)

Orden de Eric: investigar las mejores prácticas, probar con ejemplos reales y decidir con esa evidencia. Resultado
aplicado en `3_taxonomia/TAXONOMIA_IMAGENES_PROPUESTA.md`, nivel 1.

## 1. Investigación

| Fuente | Qué dice | Qué se decidió con eso |
|---|---|---|
| A. Fitzgerald, *Purpose-Driven Taxonomy Design* (2025), andyfitzgeraldconsulting.com | «build a taxonomy "of" a topic rather than "for" a purpose» es el error común; primero objetivos y usos, después estructura; probar contra los usos | El nivel 1 se ordena por lo que se hace con cada texto: dónde entra al prompt |
| Wikipedia, *Faceted classification* | Facetas: «clearly defined, mutually exclusive, and collectively exhaustive aspects» | Facetas separadas: impacto, efecto, dónde actúa, cómo entra, qué es |
| H. Hedden, *Faceted Classification and Faceted Taxonomies* (2024) | Un término en una sola faceta; «a logical and practical number of facets tends to be in the range of three to seven» | 5 facetas en el nivel 1 |
| Nielsen Norman Group, *Taxonomy 101* | Faceta = jerarquías pequeñas que describen aspectos distintos; revisar y mantener | Cada faceta con valores definidos |
| Schulhoff et al., *The Prompt Report* (arXiv 2406.06608), §1.2.1 | Componentes de un prompt: directiva, ejemplos, formato de salida, instrucciones de estilo («a type of output formatting»), rol, información adicional | Efecto: «da un ejemplo o una plantilla» como valor propio; el estilo va dentro de «fija la forma» |
| OpenAI, *Image generation models prompting guide* (cookbook) | Orden «background/scene → subject → key details → constraints»; «State exclusions and invariants explicitly»; edición «change only X» + «keep everything else the same» | Efecto: «establece un orden»; «fija restricciones» incluye excluir y fijar lo que no cambia |
| Anthropic, *Use prompt templates and variables* | La plantilla combina contenido fijo (igual en cada llamada) y variable (cambia en cada pedido) | Destino «template» para lo fijo |
| MindStudio, *Static vs Dynamic Context in AI Agents* | Lo fijo debe ser universal, pequeño y estable; «Use conditional context loading for task-specific blocks where your workflow supports branching» | Destino «inserción mecánica»: bloques que se cargan por datos del brief sin selección |
| Decisión de Eric, `5_decisiones/DECISIONES_ERIC_20261023.md` §4 | Las plantillas de un look se tratan como biblioteca, se ofrecen por tipo de pieza y estilo y se confirma como máximo una | Destino «biblioteca de plantillas» |

## 2. Prueba con 24 textos reales

Muestra al azar (semilla 20261030) de los 1,135 textos de párrafo, lista, tabla, código y cita del universo de imagen
(decisión del 23 de octubre §1).

| Texto | Documento | Lo que dice (resumen) | Impacta | Efecto | Actúa en | Entra por | Qué es (si no impacta) |
|---|---|---|---|---|---|---|---|
| INV-002072 | characters.md L67 | «Mid-stride, dynamic motion» (control de pose) | Sí | Ejemplo | Prompt | Selección (hay que interpretar qué acción es) | — |
| INV-002103 | creative-direction.md L28 | Nombrar el tipo de cámara cambia el ADN visual | Sí | Agrega contenido | Prompt | Template | — |
| INV-002217 | editing.md L51 | Plantilla de colorización con [DECADE] | Sí | Ejemplo o plantilla; agrega contenido | Prompt | Inserción mecánica (edición: colorizar) | — |
| INV-002323 | golden-rules.md L176 | «Cultural anchor + новый контекст:» | No | — | — | — | Rótulo |
| INV-002372 | gpt-image.md L74 | Texto pequeño, denso o con varias fuentes → quality high obligatorio | Sí | Fija un parámetro | Prompt | Inserción mecánica (F32 texto extenso o pequeño) | — |
| INV-002374 | gpt-image.md L78 | Endpoint `openai/gpt-image-2/edit` | No | — | — | — | Dato técnico de interfaz |
| INV-002390 | gpt-image.md L113 | No escribir en abstracto; nombrar propiedades visuales concretas de la referencia | Sí | Fija restricciones; agrega contenido | Prompt | Template (GPT Image 2, transferencia de estilo) | — |
| INV-002429 | models.md L18 | Storyboard con foco tipográfico → GPT Image 2 | Sí | Fija un parámetro (modelo) | Brief | Inserción mecánica (tipo de pieza) | — |
| INV-002586 | multi-panel.md L306 | Más paneles, menos detalle; 12 paneles: 3–8 palabras cada uno | Sí | Fija la forma | Prompt | Selección (número de paneles, valor abierto) | — |
| INV-002704 | character-design.md L108 | Chibi: GPT Image 2 con quality medium; high para close-ups de marketing | Sí | Fija un parámetro | Brief y prompt | Biblioteca de plantillas | — |
| INV-002731 | ecommerce.md L33 | Plantilla completa de cosmético de lujo con huecos | Sí | Plantilla | Prompt | Biblioteca de plantillas | — |
| INV-002773 | fashion-editorial.md L37 | Plantilla de retrato editorial 2x2 | Sí | Plantilla | Prompt | Biblioteca de plantillas | — |
| INV-002786 | fashion-editorial.md L81 | Comentario HTML «Source concept: …» | No | — | — | — | Nota interna o de origen |
| INV-002882 | portrait-cinema.md L61 | «Key levers»: los huecos de la plantilla y sus opciones | Sí | Agrega contenido | Brief | Biblioteca de plantillas | — |
| INV-002912 | poster-illustration.md L32 | Versión Nano Banana de una plantilla de póster | Sí | Plantilla | Prompt | Biblioteca de plantillas (F29 Nano Banana) | — |
| INV-002929 | poster-illustration.md L88 | «Use for fashion drops, event announcements…» | No | — | — | — | Condición de uso de una plantilla |
| INV-002963 | ui-social.md L55 | «Use to create a polished App Store…» | No | — | — | — | Condición de uso de una plantilla |
| INV-003137 | slides.md L144 | Colores de texto #ffffff, #e0e0e0 | Sí | Agrega contenido | Prompt | Biblioteca de plantillas (paleta) | — |
| INV-003138 | slides.md L146 | «Light palette:» | No | — | — | — | Rótulo |
| INV-003147 | slides.md L158 | «Subtle gradient haze» | Sí | Ejemplo | Prompt | Selección (elegir efecto) | — |
| INV-003214 | slides.md L301 | Especificación glassmorphism (material, bordes, sombra) | Sí | Agrega contenido | Prompt | Biblioteca de plantillas | — |
| INV-003408 | vision-decomposer.md L26 | Tamaños de plano para describir la imagen | Sí | Agrega contenido | Prompt | Inserción mecánica (operación: análisis de imagen a prompt) | — |
| INV-011730 | adapters/gpt-image.md L27 | `style`: natural para foto, vivid para estilizado | Sí | Fija un parámetro | Prompt | Inserción mecánica (F18 técnica) | — |
| INV-011745 | adapters/gpt-image.md L62 | «Same shot data as previous examples.» | No | — | — | — | Nota interna o de origen |

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
