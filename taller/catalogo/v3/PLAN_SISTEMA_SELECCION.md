# Plan — sistema de selección de reglas para prompts de GPT Image 2 (imagen)

Versión 2026-10-24 c (tras la primera prueba con imágenes). Propuesta para Eric; nada se ejecuta sin su OK. Cada afirmación cita su fuente; se comprueba con
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

## 2. Lo aprendido con imágenes reales (2026-10-24)

Evidencia: `produccion/prompts-sistema-20261024/RESULTADOS_20261024.md`, `produccion/template-retrato-gpt2/`.

| # | Hecho medido | Consecuencia para el sistema |
|---|---|---|
| A1 | B1–B5 (plano cerrado o medio, rostro grande) salieron como Eric esperaba al primer intento, con prompts de 208–264 palabras que aplicaban reglas de gpt-image.md, golden-rules.md, creative-direction.md, prompt-framework.md y del adaptador de forge | Aplicar las reglas funciona: la hipótesis del sistema se sostiene en este caso |
| A2 | B6 (cuerpo entero, rostro <20 %) salió con piel de cera, ojos deformes y baja resolución. La regla que lo evitaba («rostro T1 antes que cuerpo T2») estaba en DECISIONES.md:20 y en la taxonomía (F15 persona, L1064); el agente la había leído y no la aplicó | Elegir reglas de memoria falla. La selección tiene que salir de facetas del caso, no del agente |
| A3 | Esa regla no está en los 1,511 textos del corpus: está en las decisiones de Eric y en las definiciones de la taxonomía | Las fuentes de reglas son tres: corpus, decisiones de Eric y definiciones de la taxonomía |
| A4 | El caso marcó F22 «<20 %» y ninguna regla del corpus depende de F22; el agente siguió sin avisar | Si un caso marca un valor de faceta que ninguna regla cubre, el sistema avisa antes de entregar |
| A5 | B2, B3 y B5 llegaron con otra proporción; la app de ChatGPT de escritorio no deja fijar el tamaño (respuesta de Eric en taller/demo) | El formato va también dentro del texto; F29 interfaz condiciona parámetros |
| A6 | El prompt anterior de spinning tenía 979 palabras; los que funcionaron, ≤300 (techo de GPT 2, templates §6 L355) | La longitud y los ≤5 elementos se validan en código |
| A7 | En tareas largas el agente se degrada y hace afirmaciones sin base (proyección de tiempo retirada) | Tareas chicas, cada una con un entregable revisable y un alto; solo se informan hechos medidos |

## 3. Diseño (ajustado)

1. **Fuentes de reglas**: corpus de 1,511 textos (alcance GPT Image 2) + decisiones de Eric + definiciones de la
   taxonomía que prescriben (A3). Cada regla con id, fuente literal y línea.
2. **Clasificación**: formato del piloto (`taller/catalogo/v2/piloto_gpt-image/clasificacion.py`), una fila por
   aplicación, condiciones por faceta (§7.2), uso operativo (§5.3), acción y destino.
3. **Selección**: el caso se describe con valores de faceta; la selección es SQL sobre las condiciones, no memoria.
   Aviso obligatorio por cada valor de faceta del caso sin ninguna regla que lo cubra (A4).
4. **Template**: las reglas universales y de sintaxis (INCORPORADA A TEMPLATE) se escriben una vez en el template con
   su vínculo regla → bloque → validación; el validador rechaza el prompt que no las cumple (A6).
5. **Ejecución por caso**: brief → valores de faceta (llamada 1) → selección → template + reglas del caso → redacción
   (llamada 2) → validación → prompt + lista de supuestos.

## 4. Qué mide qué

| Prueba | Qué demuestra | Qué no demuestra |
|---|---|---|
| verificador de forma del piloto | que cada texto está clasificado una vez y con valores de la taxonomía | que la clasificación sea correcta |
| prueba de acierto contra B1–B5 | que las reglas universales seleccionadas explican lo que funcionó, y cuáles faltan | acierto fuera de retratos |
| aviso de cobertura de facetas | que ningún valor del caso quedó sin reglas en silencio | que las reglas que sí hay basten |
| imágenes de Eric | que el prompt funciona | — |

## 5. Tareas chicas (una a la vez; cada una termina en un entregable y se detiene)

| # | Tarea | Entregable | Cómo se revisa | Estado |
|---|---|---|---|---|
| T1 | Índice de consulta y lectura registrada de las fuentes | `taller/catalogo/v3/rag/` | `registrar_lectura.py --ver` | hecho |
| T2 | Prueba con imágenes reales B1–B6 | RESULTADOS_20261024.md | imágenes de Eric | hecho (A1–A7) |
| T3 | Lista de reglas de las decisiones de Eric y de las definiciones de la taxonomía que prescriben algo (A3) | tabla id · texto literal · archivo:línea | Eric marca las que no son reglas | pendiente |
| T4 | `golden-rules.md` lote 2 (L39–L74: contexto, texto entre comillas, plantilla) | filas en `clasificacion_golden-rules/` + verificador sin errores + dudas | Eric revisa solo las dudas | pendiente |
| T5 | `golden-rules.md` lote 3 (L76–L132: costo, refinamiento, referencias) | ídem | ídem | pendiente |
| T6 | `golden-rules.md` lote 4 (L134–L198: anclas) | ídem | ídem | pendiente |
| T7 | Revisión de Eric del lote 1 ya hecho (L1–L37) contra su piloto | dudas resueltas | Eric | pendiente |
| T8 | Prueba de acierto: cada frase de B1–B5 trazada a una regla clasificada, y cada universal comprobada en los prompts | tabla frase → id; lista de faltantes | Eric lee la lista de faltantes | después de T3–T6 |
| T9 | Aviso de cobertura de facetas en el selector (A4) | código + prueba con B6 (debe avisar F22) | salida de la prueba | después de T8 |
| T10 | creative-direction.md, prompt-framework.md, portrait-cinema.md, adaptador forge: un lote de ~20 textos por tarea | como T4 | como T4 | después de T9 |
| T11 | Template generado desde las reglas INCORPORADA A TEMPLATE, con vínculo regla → bloque → validación | template + validador | reproduce B1–B5 | después de T10 |
| T12 | Corrida de punta a punta con un brief nuevo, tiempo medido | prompt + tiempos por paso | imagen de Eric | después de T11 |

## 6. Reglas de trabajo del agente

- Una tarea por vez; al terminarla, entregar y parar.
- Informar solo hechos medidos, con lo que la medición cubre y lo que no. Nada de proyecciones sin base.
- Ninguna regla se aplica de memoria: si no está clasificada, se dice que falta.

## 7. Decisiones que necesito

| # | Decisión | Opciones |
|---|---|---|
| D1 | ¿Entran las decisiones de Eric y las definiciones de la taxonomía como fuente de reglas (T3)? | sí · no |
| D2 | ¿Los 7 documentos del bloque del piloto fuera del universo de 1,511 entran? | **Resuelta: sí, y el universo se amplía a todo texto relevante para crear imágenes salvo lo que solo aplica a otros modelos** (`v2/decisiones/DECISIONES_ERIC_20261024.md` §1) |
| D3 | Orden: T3 primero, o T7 (tu revisión del lote 1) primero | T3 · T7 |
