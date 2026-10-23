# Catálogo de textos — imagen y GPT Image 2

Estado: **abierto**. Los 1,511 textos están clasificados y validados, pero el catálogo no se cierra hasta
resolver con Eric los huecos de la taxonomía listados por `consolidar.py` ("PARA DISCUTIR"). No está conectado
todavía a la app.

## Universo

Base de 13,005 textos originales (`BASE_TEXTOS_ORIGINALES_13005_20261019_055700`, sin categorías heredadas).
Alcance decidido el 2026-10-23: solo imagen y GPT Image 2. Entran los textos de `skills/image/**` (sin LICENSE
ni NOTICE), `skills/visual-prompt-forge/adapters/gpt-image.md` y su ejemplo `gpt-image.txt`: 1,511 textos
(`universo_ids.json`). Un texto de otro modelo queda clasificado con su F29 y el filtro lo deja fuera.
La catalogación histórica de 1,887 registros (2026-10-11) no se reutiliza.

## Clasificación (de lo general a lo específico)

`naturaleza` (regla · sintaxis · ejemplo · explicativo · estructural) → `aplicacion` (INCORPORADA A TEMPLATE ·
ACTIVO EN SELECCIÓN · APLICACIÓN EN CONTROL O ENTREGA · SIN EFECTO NORMATIVO) → `plantilla_destino` → `ambito` →
facetas F01–F31 de la taxonomía del 2026-10-19 (`taxonomia_f.json`), cada una "TODOS" o lista de valores →
`condicion` → `fuera_de_taxonomia` → `razon`. Sin estados pendiente, propuesta, duda ni NO APLICA. Lo que no
cabe en la taxonomía va como `EXT: <valor>` y se discute para ampliarla. Instrucciones completas en
`INSTRUCCIONES.md`.

## Archivos

- `catalogo_imagen_gpt2.json`: catálogo unido, con texto, archivo, encabezado y línea de cada texto.
- `lotes/`, `salidas/`: entrada y salida de cada uno de los 17 lotes.
- `validar.py <lote> <salida>`: cobertura total, valores válidos y estados prohibidos.
- `consolidar.py [--escribir]`: une las salidas, comprueba cobertura contra el universo y lista lo que va a
  discusión.
