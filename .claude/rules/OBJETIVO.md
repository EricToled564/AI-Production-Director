# El objetivo, declarado por Eric

> El objetivo es siempre obtener prompts que funcionen a la primera o con el mínimo
> número de iteraciones, para producir resultados hiperrealistas que compitan con
> imágenes reales a los ojos de los observadores.

Todo lo que se construya en este repositorio se juzga contra esa frase. Antes de
añadir una etapa, una regla o un gate, hay que poder contestar en una línea cómo
acerca a ese objetivo. Si la respuesta es "deja constancia" o "prueba cumplimiento",
no es razón suficiente: la constancia no hace que una imagen pase por real.

Dos consecuencias operativas:

1. **La única medida final es la imagen generada.** Ninguna verificación sobre el
   texto del prompt puede afirmar que el resultado se verá real. Un proceso que
   nunca mira un frame renderizado no está midiendo el objetivo.
2. **Una regla vale lo que valga el defecto visible que evita.** Las reglas que
   entraron por haber roto una generación real (el registro aprendido de v3.2) pesan
   más que las extraídas de documentación, y así deben tratarse cuando compitan.

3. **El largo del prompt cede ante el contenido que las reglas exigen, pero el prompt
   se escribe en su mínimo posible.** Decisión de Eric. El tope de
   `_capabilities.json` deja de ser un bloqueo cuando lo que sobra es contenido que
   una regla obliga a incluir: dejar fuera un concepto exigido para caber es peor que
   pasarse. Lo que sí bloquea es la redundancia, y por eso el gate `minimalidad`
   rechaza todo fragmento repetido entre slots: una palabra que ya dijo lo suyo en
   otro lado no añade nada y sí resta.
