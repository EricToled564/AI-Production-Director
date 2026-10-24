# Plan — sistema de selección de reglas para prompts de GPT Image 2 (imagen)

Versión 2026-10-24 b. Propuesta para Eric; nada se ejecuta sin su OK. Cada afirmación cita su fuente; se comprueba con
`python3 -I taller/catalogo/v3/rag/consultar_rag.py`. Qué se leyó, sección por sección, con prueba de que cada línea
leída está en el índice: `python3 -I taller/catalogo/v3/rag/registrar_lectura.py --ver`.

## 0. Objetivo y restricciones

1. Prompts de GPT Image 2 que den imagen de apariencia fotográfica y alta calidad al primer intento o con el mínimo de
   iteraciones (PILOTO_V5 §1).
2. ≤ 1 minuto desde el texto del usuario hasta el prompt emitido; costo aceptable; sustentable (instrucción de Eric
   del 2026-10-24).
3. Solo textos de producción de imagen para GPT Image 2 (instrucción de Eric del 2026-10-24).
4. Lo existente se conserva solo si acerca a 1–3.

## 1. Lo que dicen las fuentes

Leídas completas y registradas el 2026-10-24: extracto de la taxonomía 10-19; esquema 10-19 entero (1,197 términos,
37 facetas con 376 valores, 19 campos con 97 valores, 204 destinos, 29 extensiones, 11 citas); decisiones 10-11,
10-23 y del repo; templates 10-19; guía v2; taxonomía 09-28; árbol 09-13 (JSON, catálogo y las 4,337 líneas del
árbol); universales candidatas; piloto `gpt-image.md` (61 aplicaciones, 27 conciliaciones).

Límites de las fuentes, no de la lectura:
- El archivo completo de la taxonomía 00688 no está en ninguna rama ni en el contenedor; solo existen su extracto
  (4 tramos) y el esquema construido de ella con número de línea.
- Las citas de listas del esquema vienen cortadas a ~400 caracteres en el propio JSON.
- El árbol 09-13 corta el texto de cada regla a ~150 caracteres.

Los 1,511 textos originales (25 archivos) también están en el índice, pero son lo que se va a clasificar, no una
clasificación: cada uno se lee completo en la tarea que clasifica su archivo (T3, T4, T6+).

| Tema | Lo que establece la fuente | Dónde |
|---|---|---|
| Tipos de texto | regla · ejemplo · alternativa · sintaxis · valor de campo · selección «y demás valores existentes» | taxonomía 10-19 §1.12 punto 5 |
| Tipo de enunciado | Prescripción · Descripción · Ejemplo | campo `tipo_enunciado` del esquema, líneas 2644–2646 de la taxonomía (TRM-1321..1323) |
| Fuerza normativa | Obligación · Prohibición · Recomendación · Permiso · Sin fuerza normativa | campo `fuerza_normativa`, líneas 2650–2657 |
| Condiciones | grupos TODAS / ALGUNA / NINGUNA; átomo = faceta o campo, operador (=, ≠, ∈, ∉, <, ≤, >, ≥, entre, existe, no existe), valor, unidad | taxonomía §7.2, línea 2800 |
| Texto no normativo | estructura · código auxiliar · duplicado referenciado · otro contenido no normativo | taxonomía 10-19, gate final punto 1 |
| Universalidad por faceta | VALOR (valores concretos) o UNIVERSAL (sin restricción de esa faceta, con evidencia) | taxonomía 10-19 §1.2 |
| De dónde sale una restricción | del cuerpo, del encabezado o del documento; no basta buscar palabras | taxonomía 10-19 §1.6 y §1.12.4; DEC-000023 |
| Uso de cada regla | ACTIVO EN SELECCIÓN · INCORPORADA A TEMPLATE · APLICACIÓN EN CONSTRUCCIÓN DE TEMPLATE · APLICACIÓN EN CONTROL O ENTREGA | taxonomía 10-19 §5.3 |
| Sintaxis de modelo en el template | se aplica una vez al template y no se vuelve a extraer | DEC-000025 |
| Atribución | ninguna atribución a terceros en material que va al cliente | DEC-000024 |
| Luz, color, cámara | términos TRM de F30 por materia (luz 48, color 34, encuadre y lente 42, composición 68…) y destinos `entrada.luz/camara/color_material.*` | esquema 10-19; templates 10-19 §3 |
| Orden de general a particular | media → referencias → personas → una o grupo / tipo de escena → estilo, luz, toma, tema, complejidad de acción, texto, modelo | árbol 09-13 (`construida_por`: instrucción literal de Eric) |

### El árbol del 2026-09-13
Su **orden de niveles** es instrucción tuya y se conserva como orden de las columnas de la matriz.
Su **asignación de reglas no sirve**: puso una regla en una rama solo si su texto contenía palabras de un léxico; si no,
en «TODAS» (642). Eso contradice §1.6, §1.12.4 y DEC-000023. Pruebas en el propio árbol: la rama `deportiva` recibe
«futuristic sports car…» (golden-rules.md:27) por la palabra «sports»; `viaje` recibe «direction of travel»
(forge SKILL.md:303); `médica` recibe «clinical specification» (brand-lock-extractor SKILL.md:114) y «surgical image
edit» (production-learnings v3.2:11); «GRUPO DE PERSONAS» tiene 0 reglas propias y ramas idénticas a «UNA PERSONA».

Medido en `gpt-image.md` contra tu piloto. El piloto tiene 22 aplicaciones sin restricción de faceta para GPT Image 2
(18 si además se exige que valgan en todos los pasos F02). De las 6 líneas que el árbol marcó universales, 4 coinciden
(L3, L39, L53, L55), 2 no lo son (L34 es cabecera de tabla; L74 está condicionada a F32 «texto extenso o pequeño») y
omite 18 (o 14).

### Correcciones a lo que dije antes
- Dije que L186 (INV-002412) era universal: falso. El piloto la restringe a F29 = `gpt-image-1-mini`
  (clasificacion.py:377–378). Mi índice omitía F29; ya lo muestra.
- Dije «faltan 19 de las 23»: el 23 contaba INV-002412. Las cifras correctas son las de arriba.
- En la prueba de retratos, el veredicto del lote 07 sobre APD L5 y L135 dice «conservar atribución Serge Shima»;
  contradice DEC-000024 (ninguna atribución a terceros en material del cliente). Sigue sin corregir.

## 2. Diseño (sin cambios de fondo respecto a tu instrucción)

1. **Número**: id INV de la base de 13,005 (estable, §1.8). Una fila por aplicación cuando un texto tiene dos condiciones (§7.2).
2. **Tipo de texto**: los de la tabla de §1 (tipos de §1.12.5 o §6.1, decisión D1). Cada tipo va a su tabla.
3. **Universalidad de una regla** = el nivel más profundo del orden de §1 en el que tiene VALOR. Universal = UNIVERSAL en
   todas las columnas, incluidas F29 (modelo) y F02 (paso), que el piloto registra aparte de las demás restricciones.
   Se decide leyendo cuerpo, encabezado y documento, nunca por palabras.
4. **Uso**: las universales y las de sintaxis del modelo se incorporan al template (§5.3, DEC-000025) con vínculo
   regla → bloque → validación, y quedan desactivadas para la selección. Las demás quedan ACTIVO EN SELECCIÓN.
5. **Matriz**: columnas en el orden de §1; en cada celda «TODOS», el valor o valores de la taxonomía (p. ej. luz =
   «Contraluz [backlight]») o «excepto: …»; vacío = error. Más acción, destino y contenido literal a aplicar.
6. **Ejecución por caso**: llamada 1 (texto → valores de columnas, salida restringida a la taxonomía) → selección SQL
   (milisegundos) → template + reglas seleccionadas → llamada 2 (redacción de los 5 slots) → validación → prompt.

## 3. Qué mide qué (sin presentar forma como verdad)

| Verificador | Qué prueba | Qué NO prueba |
|---|---|---|
| validador de la matriz | que no haya celdas vacías ni valores fuera de la taxonomía | que la clasificación sea correcta |
| comparación con tu piloto `gpt-image.md` | acierto contra una clasificación aprobada por ti | acierto en otros archivos |
| tus imágenes | que el prompt funciona | — |

## 4. Tareas cortas, en orden (cada una se entrega y se para)

| # | Tarea | Entrega | Quién decide |
|---|---|---|---|
| T1 | Índice de consulta de las fuentes maestras | `taller/catalogo/v3/rag/` — **hecho** | — |
| T2 | Medir el minuto: las 2 llamadas + selección con las 61 aplicaciones del piloto, un brief | tiempo y costo reales de una corrida | si no cabe en 60 s, se replantea antes de clasificar nada más |
| T3 | Matriz de `gpt-image.md` en el formato de §2 desde tu piloto (sin reclasificar) | xlsx | tú lo miras |
| T4 | Clasificar `golden-rules.md` con el mismo método | xlsx + lista de dudas citadas | tú resuelves solo las dudas |
| T5 | Prompt de un brief real con T3+T4 y tu generación | imagen | tú |
| T6+ | Un archivo por tarea hasta cubrir los textos de imagen GPT Image 2 | un xlsx por archivo | dudas citadas |

## 5. Decisiones que necesito

| # | Decisión | Opciones |
|---|---|---|
| D1 | Tipos de texto | lista de §1.12.5 · lista de §6.1 · ambas (tipo de §1.12.5 dentro de tipo de enunciado de §6.1) |
| D2 | Orden de columnas | el del árbol 09-13 (tu instrucción) · otro |
| D3 | Empezar por T2 (medir el minuto) antes de clasificar | sí · no |
