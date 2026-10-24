# Plan — sistema de selección de reglas para prompts de GPT Image 2 (imagen)

Fecha: 2026-10-24. Estado: **propuesta para aprobación de Eric**. Nada de esto se ejecuta sin su OK.

## 0. Objetivo y restricciones (no se negocian)

1. Prompts de GPT Image 2 que producen imágenes de apariencia fotográfica y alta calidad al primer intento o con el
   mínimo de iteraciones.
2. **≤ 1 minuto** desde que el usuario entrega su texto hasta que el sistema emite el prompt.
3. **Costo aceptable por prompt** y **sustentable**: nunca se relee el corpus para un caso; el costo de clasificar se
   paga una vez por texto y solo se repite para los textos que cambien en la fuente.
4. Alcance: **solo textos de producción de imagen aplicables a GPT Image 2**. Esta regla no se rompe.
5. Lo que ya existe en el repo se conserva **solo si acerca a 1–3** (tabla de la §8).

Consecuencia de diseño: todo el trabajo caro (leer y clasificar) ocurre **antes**, una vez. En ejecución solo hay
dos llamadas al modelo con contexto chico y una selección determinista en milisegundos.

## 1. Cómo funciona en ejecución (lo que debe cumplir ≤ 1 minuto)

```
texto del usuario
  → [llamada 1] extracción del caso: el modelo devuelve el valor de cada columna de caso (§5), con salida
     restringida a las listas cerradas; lo que el texto no dice queda marcado como inferido
  → [sin modelo] selección: consulta SQL sobre la matriz de específicas activas (< 0.1 s)
  → [sin modelo] compilación: template de la rama + contenidos de las reglas seleccionadas por destino
  → [llamada 2] redacción: el modelo escribe los 5 slots a partir del template ya armado, sin añadir reglas
  → [sin modelo] validación: verificador de cada regla seleccionada y de las universales del template
  → prompt + parámetros + traza
```

- Contexto de cada llamada: el texto del usuario y las listas cerradas (llamada 1); el template armado y unas
  decenas de reglas seleccionadas (llamada 2). Nunca el corpus.
- Si la validación falla, una llamada de reparación con el error exacto; si vuelve a fallar, se entrega el error,
  no un prompt malo.
- Las inferencias de la llamada 1 se muestran junto al prompt; si el usuario cambia un valor, se recompila
  (selección + llamada 2) sin repetir la llamada 1. **Decisión pendiente D5** (§9).

## 2. Paso 1 — tipificar cada texto (una vez, todo el corpus en alcance)

### 2.1 Unidad y número
- Unidad = una línea no vacía de un documento fuente (la misma de la base de 13,005 textos).
- Número = id `INV-xxxxxx` de esa base (estable). Documentos añadidos con aprobación: `EXT-<skill>/<archivo>-<línea>`.
- Cada texto guarda `sha256` de su contenido: si la fuente cambia, solo se reclasifican los textos con hash nuevo.
- `grupo`: cuando un texto no se entiende solo (ítem de una lista con su frase introductoria, fila de tabla con su
  cabecera), se enlazan en un grupo y el grupo es el enunciado que se clasifica. El número de la matriz es el del
  primer texto del grupo.

### 2.2 Filtro de alcance (antes de tipificar)
Cada texto recibe `alcance`: **en alcance** o **fuera de alcance** con motivo cerrado:
`otro modelo (sin GPT Image 2)` · `video o clip` · `audio` · `pipeline de video o storyboard multi-etapa`.
Fuera de alcance no se borra: queda registrado y no entra a ninguna base de trabajo.

### 2.3 Lista cerrada de tipos (propuesta; **D2**)

| Tipo | Qué es | Va a la base | Ejemplo real |
|---|---|---|---|
| estructural | encabezado, separador, cabecera de tabla, frontmatter, atribución | `textos` solamente | `## Quality Settings` |
| explicativo | contexto sin efecto en el prompt, sus parámetros ni su validación | `textos` solamente | historia de una decisión |
| regla | prescribe, prohíbe o recomienda | `reglas` | «sin elogios vagos» |
| sintaxis | fija estructura, formato o redacción del prompt | `reglas` | los 5 slots en orden |
| excepción | anula una regla en un caso definido | `reglas` (con `anula_a`) | high obligatorio con texto pequeño |
| tabla de opciones | filas condición → valor (tamaños, quality, luz por caso) | `tablas` (una fila por opción) | `quality: low` para borradores |
| plantilla | prompt o fragmento reutilizable con huecos | `plantillas` | «Photoreal Editorial» |
| ejemplo | prompt o caso concreto que ilustra una regla | `ejemplos` (con `ilustra`) | el prompt del florista |
| vocabulario | lista de términos prohibidos o de sustitución | `vocabulario` | stunning / masterpiece → hechos visuales |
| verificación | qué comprobar en el prompt o en la imagen | `verificaciones` | manos al 100%, rúbrica de crítica |

Un texto tiene **un tipo principal**. Si también cumple otro papel (una regla que trae su ejemplo), lleva
`tipos_secundarios` y aparece en las dos bases con el mismo número.

## 3. Paso 2 — grado de las reglas y reglas de template

Solo para tipos `regla`, `sintaxis` y `excepción`.

### 3.1 Grado (escala existente: `uso_operativo` del esquema + §1.2 VALOR/UNIVERSAL de la taxonomía)

| Grado | Definición operativa | Destino |
|---|---|---|
| universal | aplica a todo prompt de imagen de GPT Image 2 en alcance; ninguna columna de caso la restringe | template base |
| semi-universal | aplica siempre dentro de una **rama** fijada solo por la operación (F10) y, si hace falta, por texto en imagen (F32) | template de esa rama |
| específica | depende de valores del caso (pieza, sujeto, luz, plano, estilo…) | matriz de selección |

Ramas propuestas (**D3**): génesis sin referencias · con referencias · edición de imagen existente · análisis de
imagen a prompt; cada una con variante «con texto en la imagen». `operation_packs.json` ya tiene 4 packs: se
verifican contra esta lista, no se reescriben a ciegas.

### 3.2 Incorporación a template y desactivación
Para cada regla universal o semi-universal:
1. Se ubica la línea del template que la implementa (`template_ref`: archivo, sección, texto).
2. Se ata a una comprobación automática del validador (`check_id`) que falla si el prompt emitido no la cumple.
3. Si no está en el template, se propone el cambio del template y Eric lo aprueba.
4. Con 1 y 2 hechos: `estado_template = incorporada y verificada (fecha)` y `activa_en_seleccion = no`.

La regla sigue en la base y en la matriz (trazabilidad), pero la selección la ignora. Si el template cambia, el
validador detecta qué reglas perdieron su línea y se reactivan solas.

## 4. Paso 3 — matriz de selección de las específicas

### 4.1 Una fila por aplicación
Una regla con dos condiciones alternativas son dos filas: `N.1`, `N.2`. Cada fila es autocontenida.

### 4.2 Columnas

| Bloque | Columnas |
|---|---|
| Identidad | A número · B archivo:línea · C tipo · D grado · E activa en selección (sí/no) |
| Efecto | F acción · G destino · H contenido a aplicar (literal) · I anula a (número) · J precedencia |
| Condición | una columna por cada **columna de caso** (§5) |

- **Acción** (lista cerrada): agregar al prompt · fijar parámetro · seleccionar estructura · excluir del prompt ·
  validar el prompt · validar la imagen · solo traza.
- **Destino** (lista cerrada): slot Scene / Subject / Important Details / Use Case / Constraints · parámetro
  quality / size / background / output_format · Notes · checklist de crítica.
- **Contenido a aplicar**: el texto o valor literal que entra al prompt, en el idioma de la fuente cuando es
  vocabulario de prompt. Sin esto la acción no se puede ejecutar por código.

### 4.3 Celdas de condición (según tu instrucción: valores, no X/0)
- `TODOS` = la regla no restringe esa columna.
- Un valor o lista de valores de la lista cerrada de esa columna = aplica solo si el caso tiene uno de esos valores.
  Ejemplo: columna `luz.tipo` = «claroscuro»; columna `luz.hora` = «atardecer · amanecer».
- `excepto: …` = aplica a todos menos a esos valores.
- **Vacío = error**: el validador no deja cerrar la matriz con una celda vacía. No existe «no aplica»: no aplicar
  es no estar en la lista de valores.

### 4.4 Selección (determinista)
Una fila entra en el caso si: está activa, y para **cada** columna de condición la celda es `TODOS` o contiene el
valor del caso (respetando la jerarquía de F10) y el valor no está en `excepto`.
Conflictos: `anula a` primero; si no, la precedencia (**D7**): brief > excepción > específica > semi-universal >
universal, y regla del archivo del modelo > regla genérica. Cada fila no seleccionada queda con la primera columna
que la excluyó: la traza es automática y la exhaustividad se demuestra, no se supone.

## 5. Columnas de caso (lo que el brief fija y la matriz lee)

Solo columnas que cambian el prompt de **imagen** de GPT Image 2. Salen de la taxonomía y de `template_brief.json`:

| Origen | Columnas |
|---|---|
| Taxonomía (listas ya cerradas en `esquema_taxonomia.json`) | F04 tipo de pieza · P04 lugar de publicación · F05 temática · F06 formato · F10 operación · F13 tipo de acción · F14 régimen físico · F15 sujeto · F16 espacio · F17 estilo · F18 técnica · F19 número de sujetos · F20 identidad · F21 contacto · F22 tamaño de rostro · F23 referencias · F24 tamaño de plano · F25 ángulo · F32 texto en imagen · F33 complejidad · F34 resolución |
| Brief (`template_brief.json`; **listas cerradas por definir, D4**) | luz.fuente · luz.dirección · luz.dureza · luz.hora · color_material.paleta · color_material.grade · cámara.lente_intención · cámara.efecto_óptico · composición |

Fuera de la matriz (fijas por alcance o de video): F01–F03, P01, F07–F09, F11, F12, F26–F28, F29 (siempre GPT Image 2),
F31, F35 (siempre «no»). F30 «qué regula» no es columna de caso: alimenta `destino`.

La taxonomía no tiene faceta de luz: tu ejemplo (claroscuro, atardecer) obliga a crear las listas cerradas de luz,
color y cámara. Se proponen desde `creative-direction.md` y `template_brief.json` y Eric las aprueba antes de llenar.

## 6. Bases de datos

Un archivo SQLite (`catalogo_gpt2_v3.sqlite`) con una tabla por base, más una hoja xlsx por base para la revisión
de Eric (**D6**: un archivo con tablas separadas o un archivo por base).

| Tabla | Campos clave |
|---|---|
| `textos` | número, archivo, línea, encabezado, texto, sha256, grupo, alcance, motivo_fuera, tipo, tipos_secundarios |
| `reglas` | número, grado, fuerza (obligación/prohibición/recomendación/permiso), acción, destino, contenido, anula_a, precedencia, rama, template_ref, check_id, estado_template, activa_en_seleccion |
| `condiciones` | número, aplicación (N.1…), columna, valores, excepto — formato largo; la matriz xlsx es una vista de esta tabla |
| `tablas` | número, tabla, fila, condición (columna = valor), valor resultante, destino |
| `plantillas` | número, nombre, texto con huecos, rama, condición de uso (columna = valor) |
| `ejemplos` | número, texto, ilustra (números de regla), condición (columna = valor) |
| `vocabulario` | término, tipo (prohibido/sustituto), sustituto, alcance, número fuente |
| `verificaciones` | número, qué comprueba, sobre (prompt/imagen), método (código/visual), check_id |
| `listas_cerradas` | columna, valor, definición, origen (taxonomía/extensión aprobada, fecha) |
| `cambios` | número, campo, valor anterior, valor nuevo, quién, fecha, motivo |

## 7. Cómo se llena, en orden, con compuertas

| Fase | Qué | Quién / cómo | Compuerta |
|---|---|---|---|
| 0 | Aprobación de D1–D7 | Eric | sin esto no se empieza |
| 1 | Filtro de alcance + tipo de los textos del piloto | clasificación con salida restringida a las listas cerradas; validador | 0 textos sin tipo ni alcance |
| 2 | Grado de las reglas del piloto; universales contra el template | idem; propuesta de cambios de template a Eric | cada universal con `template_ref` y `check_id` |
| 3 | Matriz de las específicas del piloto | idem | 0 celdas vacías; 100% de valores dentro de las listas cerradas |
| 4 | Ejecución: 2 llamadas + selección + validador | código | medir tiempo y costo en 5 briefs: ≤ 60 s cada uno |
| 5 | Aceptación | comparar contra referencias (§8) y Eric genera las imágenes | sin exclusiones falsas; decisión de Eric de ampliar |
| 6 | Resto del corpus en alcance | mismo método, por archivo | las mismas compuertas por archivo |

**Piloto propuesto**: `gpt-image.md`, `golden-rules.md`, `prompt-framework.md`, `portrait-cinema.md` y
`creative-direction.md` (unos 450 textos). Mide velocidad y costo de clasificar antes de comprometer los ~1,500.

Clasificación: una pasada con salida restringida a las listas cerradas (el modelo no puede escribir un valor fuera de
la taxonomía; ese fue el fallo de los clasificadores descartados) más el validador. La segunda opinión no se paga de
nuevo: se usan las referencias de la §8. Los desacuerdos van a Eric.

## 8. Lo que ya existe: se conserva solo si acerca al objetivo

| Existente | Veredicto | Por qué |
|---|---|---|
| `universo_ids.json` (1,511) e ids INV | **se conserva** | universo y numeración estables de la decisión 1 |
| `esquema_taxonomia.json` | **se conserva** | son las listas cerradas que impiden valores inventados |
| `template_brief.json` | **se conserva como fuente** | trae las columnas de luz, cámara y color que pediste |
| `universal_rules.json` (12 universales) y `operation_packs.json` | **candidatos** | se verifican en la Fase 2; su estado actual es «no aceptado por el usuario» |
| piloto `gpt-image.md` (61 aplicaciones) | **se conserva como referencia** | respuesta conocida para medir la clasificación nueva |
| veredictos de la prueba de retratos (13,225 pares, 96.3 % de acuerdo) | **se conserva como referencia** | prueba de aceptación gratuita de la selección para B1–B5 |
| catálogo 2026-10-11, salidas automáticas v2 | **no se usa** | decisión 2 y PENDIENTES #4 |
| app con 852 reglas embebidas en cada petición | **no se usa** | contradice 1 minuto y costo: manda todo el corpus en cada llamada |
| taller de 4 llamadas | **se reduce a 2** | PENDIENTES #2 ya apuntaba a 2 llamadas para ≤ 1 minuto |

Dato de tamaño, medido sobre los 1,511 con las dos pasadas de la prueba: 508 sin contenido normativo en ambas;
164 normativos que aplican a los 5 retratos (candidatos a universal o semi-universal); 711 normativos que no
aplican a ningún retrato (específicos de otras piezas o fuera de alcance); 128 con desacuerdo o aplicación parcial.

## 9. Decisiones que necesito de Eric antes de empezar

| # | Decisión | Mi recomendación |
|---|---|---|
| D1 | Universo exacto | los 1,511 de la decisión 1, más los textos de imagen GPT Image 2 de `produccion-visual-sw30/SKILL.md` (T1), `visual-prompt-forge` prompt-anatomy y failure-modes, y la rúbrica del crítico; los de Nano Banana solo se marcan fuera de alcance |
| D2 | Lista cerrada de tipos | la tabla de la §2.3 |
| D3 | Ramas de semi-universales | las de la §3.1 |
| D4 | Listas cerradas de luz, color y cámara | las propongo desde `creative-direction.md` y `template_brief.json` y las apruebas antes de llenar |
| D5 | ¿La revisión de inferencias del brief cuenta dentro del minuto? | no: se emite el prompt con las inferencias marcadas y un cambio recompila en segundos |
| D6 | Un archivo con tablas separadas o un archivo por base | un archivo SQLite con tablas separadas y una hoja xlsx por base |
| D7 | Orden de precedencia en conflictos | brief > excepción > específica > semi-universal > universal; archivo del modelo > genérico |
| D8 | Tope de costo del piloto | lo fijas tú |
