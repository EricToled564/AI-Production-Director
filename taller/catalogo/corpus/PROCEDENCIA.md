# Procedencia del corpus de 13,005 textos

Dos archivos con el mismo contenido, entregados por Eric Toledano el 2026-10-24.

| Archivo | sha256 | Papel |
|---|---|---|
| `BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite` (tabla `textos`) | `c991437028d9d731bf46e516efa315f08d9da71bd596495c119fa41d30f6c8d9` | Entrada autorizada. Es la base que leen los scripts |
| `CORPUS_LITERAL_COMPLETO_13005.jsonl` | `d75acf41d4520eb12c7d892b2ebc8dcece08b9b4665624592771b50a00789519` | Copia legible en texto, una unidad por línea |

13,005 unidades, ids `INV-000001` a `INV-013005`, de 206 archivos fuente, con 16 campos: id, archivo, skill,
tipo_documento, encabezado, linea_inicial, linea_final, pagina_inicial, pagina_final, tipo_unidad, texto,
sha256_unidad, sha256_archivo, senal_lexica_normativa, texto_duplicado_en_otra_unidad, paginacion.

## Comprobaciones hechas al recibirlos (2026-10-24)

| Comprobación | Resultado |
|---|---|
| sha256 del `.sqlite` igual al de `PILOTO_V5_INSTRUCCIONES_20261019.md:43` | igual |
| `.sqlite` contra `.jsonl`: mismos ids y los 16 campos de cada unidad | 13,005 de 13,005, 0 diferencias |
| sha256 de `texto` igual a `sha256_unidad` | 13,005 de 13,005 |
| Las 1,511 unidades de `v2/lotes/` (alcance imagen + GPT Image 2) existen con el mismo id, archivo y texto | 1,511 de 1,511 |
| `v2/piloto_gpt-image/construir.py` | verificación correcta; 88 filas idénticas al original por carácter y sha256 |
| `v2/matriz_eric.py` regenera `matriz_gpt-image.xlsx` | celda por celda igual a la versión en git |
| sha256 del `.sqlite` después de correr los scripts | sin cambio |

## Uso

`v2/matriz.py` abre el `.sqlite` y se detiene si su sha256 no es el autorizado, como pide
`PILOTO_V5_INSTRUCCIONES_20261019.md` §3 ("Si un hash no coincide, detenerse y reportar").
