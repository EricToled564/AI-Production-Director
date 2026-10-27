# Brief · La doctora cierra el libro (fotograma clave)

Fuente: texto de Eric del 2026-10-27, en esta sesión. Lo que el texto no dice está en la última sección.

## Qué es

Un fotograma clave de una película: en un consultorio, una doctora cierra el libro de una mujer mientras la pareja
escucha. Fotografía documental editorial que parezca una foto real. Modelo GPT Image 2, quality high.

## Imágenes de entrada (numeración del texto de Eric)

| Imagen | Qué es | Qué se toma de ella |
|---|---|---|
| Image 1 | primer plano del rostro del hombre | el rostro exacto |
| Image 2 | placa aprobada de cuerpo entero del hombre | solo pelo, lentes y complexión |
| Image 3 | primer plano del rostro de la mujer | el rostro exacto |
| Image 4 | placa aprobada de cuerpo entero de la mujer | solo pelo, aretes y complexión |
| Image 5 | placa aprobada de la doctora | solo su mano derecha y el puño blanco de la bata |
| Image 6 | el libro negro de lino de la doctora, cerrado | el libro |
| Image 7 | el consultorio vacío | el lugar, la posición de cámara y la luz, exactos: es el mundo de la imagen |

## Escena

- **Cámara:** desde el asiento de la doctora, en la posición de cámara de Image 7.
- **Luz:** la luz de ventana fría y suave de la mañana de Image 7.
- **Las sillas:** las dos sillas grises se quedan donde están en Image 7, muy detrás del escritorio de mármol.
- **Él:** se sienta en la silla bajo el cuadro abstracto. Lleva un saco gris carbón de lana-cachemira sin estructura, abierto, sobre un suéter negro de cuello redondo de merino.
- **Ella:** se sienta en la silla frente a la puerta abierta. Lleva una polo de punto gris perla con el cuello abierto.
- **Escala y altura:**
  - sus hombros son tan anchos como los respaldos de las sillas;
  - sus cabezas quedan a la altura del borde inferior del cuadro, así que todo el escritorio queda entre ellos y la cámara;
  - el tablero del escritorio queda a la altura de sus codos, y el pecho entero y la parte superior de los brazos quedan por encima.
- **Instante congelado:**
  - ella se inclina hacia delante a media acción, con el brazo izquierdo extendido sobre el escritorio. La mano va a mitad de camino hacia el libro, con los dedos un poco abiertos para tomarlo. Mira el libro, con una sonrisa leve de labios cerrados;
  - él se inclina un poco hacia delante y escucha a la doctora con una sonrisa leve de labios cerrados. Sube los ojos por la manga blanca de la doctora hacia su cara, justo fuera del borde derecho del cuadro. Su mirada pasa junto a la cámara por la derecha y nunca entra en la lente.
- **Primer plano:**
  - donde en Image 7 está el libro abierto queda el libro cerrado de Image 6, a ese mismo tamaño;
  - la mano derecha de la doctora descansa plana sobre su esquina inferior y tapa el nombre dorado. Es una mano delgada de mujer con cinco dedos;
  - de la doctora solo entran la mano y el puño blanco de Image 5, por el borde inferior.
- **En cuadro:** solo la pareja y esa mano.
- **Calidad:**
  - rostros idénticos a Image 1 e Image 3, limpios y nítidos, con ojos claros;
  - cinco dedos en cada mano;
  - piel natural sin retoque;
  - foco profundo, contraste natural y grano fino de película.

## Cómo se produce: tres pasos, un chat nuevo por paso

Lo exigen dos reglas críticas de `produccion-visual-sw30/SKILL.md`:

- la 1: «Un solo trabajo por generación. Con dos personajes: un sujeto por generación, o técnica de colocación probada»;
- la 7: «Mundos por dos pasos: placa vacía primero».

No hay técnica probada para meter a dos personas con referencias en una sola pasada de GPT Image 2. En `.claude/rules/research/09-grupo-ensamble.md` esa pregunta quedó «sin evidencia».

1. **Paso 1 (edición):** sobre Image 7, el libro abierto pasa a ser el libro cerrado de Image 6, con la mano de la doctora de Image 5.
2. **Paso 2:** el hombre (Image 1 y 2) sobre el resultado del paso 1.
3. **Paso 3:** la mujer (Image 3 y 4) sobre el resultado del paso 2.

## Lo que se infirió o se cambió, porque el texto no lo decía o una regla lo exigía

- **Tamaño:** 1536x1024 (3:2). El texto no da formato; debe ser el ratio de Image 7. Si Image 7 tiene otro, se usa el suyo.
- **Hex de los colores nuevos** (golden-rules.md; SKILL.md:50):
  - gris carbón #36383B;
  - negro #121212;
  - gris perla #D8D6D0.
- **«Her white sleeve»** en la mirada de él se escribe «the doctor's white sleeve». Así se evita leerlo como la manga de la mujer.
- **«The couple inside the central horizontal band of the frame»** no va: la regla 2 del SW30 prohíbe la posición por «centre». La altura ya la fijan las anclas del propio texto: el borde inferior del cuadro y el tablero a la altura de los codos.
- **«Her hand moving toward the book»** pasa a «her hand halfway to the closed book»: la regla 8 del SW30 pide el instante congelado, sin verbos de proceso.
- **Frase de identidad:** se añade «Keep facial features exactly the same as Image 2», la frase de bloqueo de identidad de `characters.md:14`. Va además de «copy this exact face».
- **Sombras de contacto:** se añade una sombra de contacto suave donde la mano toca el libro y donde el libro toca el mármol (`prompt-framework.md:217`).
