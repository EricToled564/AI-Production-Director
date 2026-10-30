# Lectura: catálogo de casos de uso (2026-10-30)

Documento: la carpeta `4_diseno/casos/`, leída completa (16 archivos) para la revisión de estructura pedida por Eric.

| Archivo | Qué dice | Consecuencia |
|---|---|---|
| `README_CASOS_DE_USO.md` | Contenido y uso del catálogo; pasos para armar un caso | Conteos viejos (112/57, 184) y cita a «V5» en L28: informe §4.5 |
| `build_catalog.py` | Lee la taxonomía hasta el Anexo 1 (valores y definiciones) y el Anexo 2 (faceta, nombre, respaldo, cita); fija a mano 4 facetas y 3 tracks | Informe §4.1 |
| `bind_templates.py` | Vincula cada registro con su ruta en el schema de templates; rehace `case_selectable` de F30 | Diccionario sin uso y cálculo repartido: informe §4.6 |
| `validar.py` | Comprueba IDs, facetas, rutas y disposiciones; con un caso, su completitud y aprobación | No comprueba línea frente a ID: informe §5.2.3 |
| `case.schema.json` | Formato del caso | Sin cambios |
| `catalogo_opciones.json`/`.csv`, `casos_opciones.sqlite` | 1,729 registros; líneas y sha comprobados contra la taxonomía actual: cero errores | Informe §4 |
| `jerarquia_valores.json`, `relaciones_documentadas.json`, `rutas_documentadas.json` | 1,729, 473 y 183 registros, todos con su línea correcta | Ningún script los genera: informe §4.2 |
| `mapa_facetas.json`, `mapa_materias_f30.json`, `mapa_materias_f30_paths.json` | Destinos de las 31 facetas y de las 24 materias de F30 | Sin cambios |
| `conteos.json`, `manifest_fuentes.json` | Conteos y sha de la taxonomía (coincide con la actual) | Sin cambios |

Informe: `7_auditorias_y_verificaciones/revision_estructura_taxonomia_y_casos_20261030.md`.
