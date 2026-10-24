# Template de retrato GPT Image 2

Congelado de los prompts B1–B6 aprobados por Eric el 2026-10-24 (`aprobados-20261024/`, resultados en
`produccion/prompts-sistema-20261024/RESULTADOS_20261024.md`).

## Campos que se llenan por caso

| Campo | Qué va | Regla que lo exige |
|---|---|---|
| `id` | nombre del caso | — |
| `ratio` | 2:3, 3:2, 1:1, 4:5 o 16:9 | gpt-image.md:53–63 |
| `pronombre` | her / him / them | — |
| `escena` | lugar, momento y fondo, sin el verbo inicial (lo pone el template) | gpt-image.md:9 |
| `elementos` | lista de 1 a 5 elementos distintos de la escena | forge gpt-image.md:88 |
| `sujeto` | edad, encuadre, pose, mirada, rasgos concretos, vestuario con material | creative-direction.md:78–92; golden-rules.md:34 |
| `luz` | fuente y dirección («from camera left», «from above», «backlight»…) y qué hace en la cara | creative-direction.md:7 |
| `microdetalle` | texturas, mechones a la luz, especulares, sombras de contacto, caída de tela | prompt-framework.md:208–219 |
| `camara` | altura o ángulo, «Nmm feel», profundidad de campo | prompt-framework.md:44 |
| `paleta` | lista de [nombre, #hex] | golden-rules.md:36 |
| `uso` | para qué es la imagen | golden-rules.md:39–44 |
| `restriccion_extra` | lo que el caso exige además (p. ej. «with exactly two hands») | — |
| `libre_de` | lo que no debe aparecer, en una frase | gpt-image.md:15 |

## Lo que pone el template, siempre

«Create a photograph», cinco slots en orden, «Real skin texture with visible pores», la paleta con hex, «looks like a
real photo», «Solo portrait», «natural skin texture and no AI rendering artifacts», y el tamaño por ratio.

## Lo que el validador rechaza

Ratio sin tamaño aprobado, falta de cualquier texto fijo, slots fuera de orden, elogios vagos y nombres de marca,
paleta sin hex, luz sin fuente o dirección, cámara sin «Nmm feel», más de 5 elementos o ninguno, más de 300 palabras.
