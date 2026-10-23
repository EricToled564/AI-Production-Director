# Catalogación texto por texto — imagen, GPT Image 2

Clasificas cada texto de tu lote con la taxonomía F01–F31 del 19 de octubre (`taxonomia_f.json`). El catálogo
sirve para que una app, dado el brief validado de UNA imagen para GPT Image 2, saque por filtro las reglas que
aplican sin leer todas. Ningún texto queda sin clasificar. Usa SOLO valores que existen en `taxonomia_f.json`,
copiados exactamente (mismo texto, mismas mayúsculas y acentos).

Prohibido: estados "pendiente", "propuesta", "duda", "desconocido", "NO APLICA", confianza baja o similares.
Cada texto se resuelve. Si una restricción real del texto NO cabe en ningún valor de la taxonomía, no la fuerces
ni la omitas: escribe el valor que haría falta como `"EXT: <valor necesario>"` en esa faceta y explícalo en
`fuera_de_taxonomia`. Esos casos se discuten con el usuario para ampliar la taxonomía; úsalo solo cuando de verdad
no hay valor adecuado.

Para entender un texto lee su contexto: el archivo fuente completo está en
`docs/d4ea0f84-BASE_TEXTOS_ORIGINALES_13005_20261019_055700_1/fuentes_originales/<archivo>` (ruta relativa a la
carpeta scratchpad). Un ítem de lista hereda el alcance de su encabezado y de la frase que lo introduce: un ítem
bajo "## Nano Banana" es de Nano Banana aunque no lo nombre.

## Campos, de lo general a lo específico (en este orden)

1. `id`: el id del texto.
2. `naturaleza` (uno):
   - `regla`: prescribe, prohíbe o recomienda algo (aunque no use "must").
   - `sintaxis`: define estructura del prompt, slots, plantilla, formato de parámetros, palabras o fórmulas a usar.
   - `ejemplo`: prompt de ejemplo o ilustración literal de una regla o sintaxis.
   - `explicativo`: describe o explica sin prescribir (contexto, definición, razón, capacidad del modelo).
   - `estructural`: encabezado, separador, cabecera o separador de tabla, frontmatter, valla de código sin contenido.
3. `aplicacion` (uno):
   - `INCORPORADA A TEMPLATE`: vale para TODA imagen de GPT Image 2 (o toda imagen) sin condición del caso; se
     aplica una vez a la plantilla del brief o del prompt y no entra a la selección por imagen.
   - `ACTIVO EN SELECCIÓN`: vale solo cuando la imagen tiene ciertas características (valores de facetas). Incluye
     reglas de otro modelo: se restringen por F29 y el filtro las deja fuera de GPT Image 2.
   - `APLICACIÓN EN CONTROL O ENTREGA`: comprobación, crítica, validación o forma de entregar el resultado.
   - `SIN EFECTO NORMATIVO`: solo para naturaleza `explicativo` o `estructural`.
4. `plantilla_destino`: dónde actúa. Uno o varios de: un campo del brief (`entrada.<ruta>` del contrato, p. ej.
   `entrada.camara.angulo`, `entrada.luz`, `entrada.referencias[]`, `entrada.texto_marca.literales`), un slot del
   prompt GPT Image 2 (`Scene`, `Subject`, `Important Details`, `Use Case`, `Constraints`; en edición `Change`,
   `Preserve`, `Constraints`), `parametros` (quality, size), `validacion`, `entrega`. Para `estructural`: [].
5. `ambito`: lista de valores de `AMBITO` (p. ej. ["Creación de imagen"]). Para `estructural`: [].
6. `facetas`: objeto con las 31 claves F01…F31. Cada una:
   - `"TODOS"` si el texto no se restringe por esa faceta (vale para cualquier valor de ella);
   - o una lista de valores de esa faceta: el texto aplica solo cuando el caso tiene alguno de ellos.
   Reglas fijas:
   - F29 Modelo: lista de modelos a los que aplica según la fuente, o "TODOS" si es agnóstica. Un texto solo de
     Nano Banana lleva ["Nano Banana 2","Nano Banana Pro"] (o el que corresponda), nunca "TODOS".
   - F30 Qué regula: SIEMPRE lista con todas las materias pertinentes, nunca "TODOS".
   - F31 Condición para avanzar: SIEMPRE lista con exactamente un valor.
   - F26–F28 solo se restringen si el texto habla de FF/LF o contexto de clip; si no, "TODOS".
   - F01 Etapa: casi todos estos textos son "5 Imagen"; F02 Paso según la operación (E5.2 génesis, E5.4 cuadros
     con referencias, E5.5 edición, E5.7 crítica…), o "TODOS" si vale para cualquier paso de imagen.
   - Para `explicativo`: llena F01, F02, F29 y F30 con lo que el texto trata; el resto "TODOS".
   - Para `estructural`: `facetas` = {} (objeto vacío).
7. `condicion`: para `ACTIVO EN SELECCIÓN`, frase corta comprobable contra el brief ("el caso tiene texto
   renderizado en la imagen", "la operación es edición"). Para los demás: "siempre" o "" si es estructural.
8. `fuera_de_taxonomia`: [] o lista de {"faceta","valor_necesario","por_que"} (ver arriba).
9. `razon`: 25 palabras o menos, por qué esta clasificación.

## Salida

Un archivo JSON: lista con un objeto por texto del lote, en el mismo orden, con exactamente estas claves:
`id, naturaleza, aplicacion, plantilla_destino, ambito, facetas, condicion, fuera_de_taxonomia, razon`.
Antes de terminar ejecuta `python3 -I cat2/validar.py <lote> <salida>` (desde la carpeta scratchpad) y corrige
hasta que imprima OK. Escribe el JSON con un script de Python (json.dump) para no romper el formato.
