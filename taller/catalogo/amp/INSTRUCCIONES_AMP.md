# Ampliación de la taxonomía — revisión de textos ya catalogados

Eric aprobó el 2026-10-23 estas ampliaciones (ya están en `taller/catalogo/taxonomia_f.json`):

- F04 Tipo de pieza: + `infografía o diagrama`, `concept art`, `pieza de portafolio`.
- F10 Modo de generación: + hijos de `edición de imagen existente (T5)`: `edición: quitar objeto`,
  `edición: añadir objeto`, `edición: cambiar luz o clima`, `edición: colorizar`, `edición: restaurar`,
  `edición: traducir texto`; + `análisis de imagen a prompt`. Una regla que vale para cualquier edición lleva el
  padre T5; una que vale solo para un tipo de edición lleva el hijo.
- F17 Estilo: + `anclado en época, cultura o autor`, `brutalista`, `futurista`.
- F06 Formato: + `3:2`. F05 Temática: + `finanzas y banca`, `sector público`.
- F33 Complejidad de escena (nueva): `simple`, `compleja (5 o más elementos)`.
- F34 Resolución (nueva): `1K`, `2K`, `4K`.
- Campos nuevos del catálogo:
  - `excepto`: objeto {faceta: [valores]}; la regla NO aplica si el caso tiene alguno (p. ej. "no usar en
    bancos" → {"F05": ["finanzas y banca"]}). Sustituye a codificar exclusiones con listas casi completas.
  - `excepto_texto`: lista de exclusiones sin faceta posible (p. ej. "audiencia mayor", "dashboards con muchos
    datos"); se comprueban en la confirmación.
  - `facetas_alternativas`: lista de objetos {faceta: [valores]}; la regla también aplica si el caso cumple
    todas las facetas de alguna alternativa. Úsalo para condiciones "o" entre facetas distintas (p. ej. quality
    high "si texto pequeño o identidad sensible o fotorrealismo").
  - `biblioteca`: true si el texto es una plantilla o variante de un look concreto (retrato con neón, póster
    streetwear, pavo real vintage…) que se ofrece por F04/F17 y de la que la confirmación elige como máximo una;
    false en todo lo demás.
- Textos que pedían "14 o más referencias" o "grounding de lugar real": se cierran sin valor nuevo (son de Nano
  Banana o comparan modelos; F29 ya los resuelve). Esa restricción queda solo en la condición.

La faceta F32 (texto en la imagen) la está revisando otra persona: no la toques.

## Qué haces con cada texto del lote

Cada texto trae su clasificación `actual` de algunas facetas y su `fuera_de_taxonomia`. Lee el texto completo y su
contexto (archivo fuente en `docs/d4ea0f84-BASE_TEXTOS_ORIGINALES_13005_20261019_055700_1/fuentes_originales/<archivo>`
dentro de la carpeta scratchpad) y decide, con la taxonomía ampliada:

1. F04, F05, F06, F10, F15, F16, F17, F19, F23: el valor final de cada una ("TODOS" o lista de valores válidos).
   Cambia lo que la ampliación permite expresar mejor: todo valor `EXT: …` desaparece (pasa al valor nuevo o se
   cierra), y las aproximaciones se corrigen (p. ej. estilo brutalista clasificado como "experimental" →
   "brutalista"; una edición que cambia solo luz o clima → hijo correspondiente; una exclusión codificada como
   "todos los sectores salvo X" → F05 "TODOS" con `excepto`). Si no hay nada que cambiar, copia el valor actual.
2. F33 y F34: "TODOS" salvo que el texto dependa de la complejidad de la escena o de la resolución.
3. `excepto`, `excepto_texto`, `facetas_alternativas`, `biblioteca` según lo anterior.
4. `fuera_de_taxonomia`: lo que todavía no cabe tras la ampliación (normalmente [] para todos). Si queda algo,
   se volverá a discutir con Eric; no lo fuerces.

Prohibido cualquier estado pendiente, duda o NO APLICA. Solo valores que existen en `taxonomia_f.json`.

## Salida

Lista JSON, un objeto por texto del lote, mismo orden:
`{"id", "F04", "F05", "F06", "F10", "F15", "F16", "F17", "F19", "F23", "F33", "F34", "excepto", "excepto_texto",
"facetas_alternativas", "biblioteca", "fuera_de_taxonomia", "razon_cambio"}` (`razon_cambio`: 20 palabras o
menos, vacío si no cambió nada). Escríbela con json.dump y ejecuta
`python3 -I taller/catalogo/amp/validar_amp.py <lote> <salida>` desde /home/user/AI-Production-Director hasta
que imprima OK.
