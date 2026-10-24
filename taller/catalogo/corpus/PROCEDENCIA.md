# Procedencia del corpus literal de 13,005 textos

- Archivo: `CORPUS_LITERAL_COMPLETO_13005.jsonl`, una unidad por línea.
- Entregado por Eric Toledano el 2026-10-24 en la sesión de revisión de estado.
- sha256 del archivo: `d75acf41d4520eb12c7d892b2ebc8dcece08b9b4665624592771b50a00789519`.
- 13,005 unidades, ids `INV-000001` a `INV-013005`, sin repetidos, de 206 archivos fuente. Campos: id, archivo, skill,
  tipo_documento, encabezado, linea_inicial, linea_final, pagina_inicial, pagina_final, tipo_unidad, texto,
  sha256_unidad, sha256_archivo, senal_lexica_normativa, texto_duplicado_en_otra_unidad, paginacion.

## Comprobaciones hechas al recibirlo (2026-10-24)

| Comprobación | Resultado |
|---|---|
| sha256 de `texto` igual a `sha256_unidad` | 13,005 de 13,005 |
| Las 1,511 unidades de `v2/lotes/` (alcance imagen + GPT Image 2) existen con el mismo id, archivo y texto | 1,511 de 1,511, 0 distintas |
| `v2/piloto_gpt-image/construir.py` con la base generada desde este archivo | verificación correcta; 88 filas idénticas al original por carácter y sha256 |
| `v2/matriz_eric.py` regenera `matriz_gpt-image.xlsx` | celda por celda igual a la versión en git (hojas `matriz` y `columnas`) |

No comprobado: que sea byte a byte la misma base que el SQLite `BASE_TEXTOS_ORIGINALES_13005_20261019_055700`
(SHA `c9914370…`), porque ese archivo no está disponible y el formato es otro. La coincidencia de ids, textos y
hashes por unidad en todo lo que el repo ya usaba es la evidencia disponible.

## Uso

`v2/matriz.py` genera `corpus_13005.sqlite` (tabla `textos`, mismas columnas) la primera vez que se importa, y aborta si
el archivo no tiene 13,005 unidades o si algún sha256 no coincide. El SQLite no se versiona; el JSONL es la fuente.
