# Mapa de pasos — imagen fija con una persona (GPT Image 2)

Fuente: textos del universo de la prueba (`v3/universo/universo_prueba_textos.jsonl`), leídos completos el 2026-10-27.
Cada paso dice qué produce, qué textos lo gobiernan y con qué condición. Lo marcado «lectura» es interpretación de la
estructura, no texto literal; el resto se cita.

## 1. Los pasos (flujo-spot, etapa E5, y subflujo de génesis, nivel 4)

| Paso | Produce | Entra | Textos que lo gobiernan | Condición |
|---|---|---|---|---|
| E5.2 génesis de persona | rostro T1 canonizado | solo texto | INV-000394 (E5.2), INV-000427 («paso 1: rostro T1 sin refs»), INV-000604 («Persona: template T1 obligatorio»), INV-000442 / INV-000558 (bloques light_hard · skin_doc · usecase_doc · clean_doc), INV-000561 (~250 palabras), INV-000440 (GPT Image 2 quality high para piel), INV-000553 (leer characters + portrait-cinema), INV-000526 (orden de lectura, secciones, micro-gate, veto de vocabulario) | sin referencias adjuntas (INV-000610: «Referencias adjuntas: eso es T2 en adelante») |
| E5.2 génesis de lugar | placa vacía | solo texto | INV-000445 («Placa VACÍA, sin persona»), INV-000447 (una presión ambiental), INV-000502 | cuando la imagen final pone a la persona en un lugar |
| E5.3 maestro derivado | cuerpo T2 | rostro T1 adjunto como Image 1 | INV-000395, INV-000428 («cuerpo entero T2 con el rostro adjunto»), INV-000474 («Nunca cuerpo entero de un solo tiro»), INV-000486–000487 («keep facial features exactly the same»), INV-000508–000509 (same face and clothes + deltas) | cuando la imagen final muestra el cuerpo entero |
| E5.4 cuadro | imagen final T3 | sujeto canonizado + placa canonizada | INV-000396 («Mundos por dos pasos; posición por ancla legible»), INV-000511–000512 («use only the person from image N»), INV-000490 («keep the world untouched») | persona dentro de un lugar |
| E5.5 edición | cuadro corregido T5 | cuadro ≥80 % | INV-000397, INV-000584–000585 (editar, no re-tirar; hasta 3 ediciones) | resultado casi correcto |
| Común a cada generación | — | — | INV-000564–000566 (lints), INV-000567–000570 (pregunta de avance y micro-gate), INV-000573–000577 (barato → alta), INV-000578–000579 (inspección al 100 %), INV-000591 (máximo dos intentos por método) | siempre |

## 2. Lo que es de video y no gobierna una imagen suelta (lectura)

El flujo de anclas (`flujo-anclas.html`) trata «la imagen fija que el modelo de video va a heredar» (INV-000004); su
rol D1 dice «qué modelo de video la recibe» (INV-000035). Ahí «maestro de identidad» es el *character ref* para Kling
Elements, con «luz pareja, sin sombras duras» (INV-000012, INV-000125, INV-000046). Esa condición (el que recibe es un
modelo de video) no se da en una imagen suelta, así que no compite con la plantilla T1 de la génesis.

La tabla de tratamientos (INV-000209 a INV-000215, aplicada en A4, INV-000094) fija el look por proyecto para las
anclas. En una imagen suelta, el look que pide el brief (comercial pulido, narrativo) se aplica en el paso que produce
la imagen final, E5.4, no en la génesis.

## 3. Dónde cae cada caso

| Caso | Imagen final | Pasos |
|---|---|---|
| B1 pescadora en el muelle, MCU, documental | persona en lugar | T1 rostro → placa del muelle → T3 |
| B2 ejecutivo en oficina, MS, comercial pulido | persona en lugar | T1 rostro → placa de la oficina → T3 con el look comercial |
| B3 atleta en el gimnasio, CU, documental | persona en lugar | T1 rostro → placa del gimnasio → T3 |
| B4 mujer en la cocina, MS, narrativo | persona en lugar | T1 rostro → placa de la cocina → T3 con el look narrativo |
| B5 músico en escenario, MCU, narrativo | persona en lugar | T1 rostro → placa del escenario → T3 con el look narrativo |
| B6 hombre de cuerpo entero, estudio | cuerpo entero | T1 rostro → T2 cuerpo (ya hecho: B6-T1 y B6-T2) |

Lectura: B1–B5 no son cuerpo entero, así que no llevan T2; el T3 usa el rostro T1 como sujeto canonizado.
