# Procedencia de los originales del 2026-10-19

Entregados por Eric Toledano el 2026-10-24. Son las entradas autorizadas de `PILOTO_V5_INSTRUCCIONES_20261019.md` §3
(líneas 41–47) que no estaban en el repo. La base de 13,005 textos está aparte, en `../corpus/`.

| Archivo o paquete | sha256 entregado | Hash esperado y dónde está fijado | Resultado |
|---|---|---|---|
| `00688_TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md` | `7ec912aa92d8d1a6f54a6158550c0bcfa48861a05bbf6f6146b5b93b1f9bfeaa` | el mismo: `PILOTO_V5…:42`, PLAN_V5 §7.6 (L297), `casos/manifest_fuentes.json` | coincide |
| `PLAN_V5_COMPLETO_TAXONOMIA_TEMPLATES_20261019_054300.md` | `36abfa00f28033c6422342285cd393071a6fade22c2707d62206a29d13e7a493` | el mismo: `casos/manifest_fuentes.json` | coincide |
| `CASOS_OPCIONES_TAXONOMIA_20261019/` (zip `e7183a14…`, 19 archivos en `casos/` y `templates/`) | — | `PILOTO_V5…:45`: `validar.py` debe pasar | `validar.py` PASA; su `verificacion.json` sale idéntico al entregado (1,369 TRM, 31 facetas, 0 destinos vacíos) |
| `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019/` (zip `fb0cc6b1…`, 11 archivos en `templates/`) | — | `PILOTO_V5…:44`: hashes de su `MANIFIESTO.json` | 10 de 10 coinciden; `verificar_templates.py` PASA con 369 rutas y 0 inválidas, resultado idéntico al entregado |

Los nombres de las carpetas no llevan el prefijo de subida (`59239886-`, `08fe4a51-`, `p2/ARCHIVOS/`) que usaba la versión
anterior de `v2/construir_esquema.py`; el contenido es el de los zips, sin cambios.

## Duplicados comprobados

- `templates/CONTRATO_IMAGEN_ORQUESTACION.schema.json` y `templates/REGISTRO_DESTINOS_TEMPLATE.json` vienen en los dos
  paquetes con el mismo sha256 (`49b9470b…` y `c1ac0ec3…`).
- `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md` es igual a `v2/decisiones/TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`
  (`ef46fa11…`).

## Lo que esto comprueba de lo ya hecho

- `v2/construir_esquema.py`, corrido desde estos originales, regenera `v2/esquema_taxonomia.json` **idéntico byte a byte**
  al que estaba en el repo.
- Las 106 líneas de contenido de `v2/taxonomia_extracto.md` están literalmente en la taxonomía (4,365 líneas).

## Búsqueda previa de faltantes (2026-10-24)

Antes de esta entrega se buscó en el repo completo: historial sin recortar (275 commits de `main`,
`wip-verificacion`, `claude/notebook-lm-content-control-br0gs4` y los 10 PR), 3,597 objetos y el contenido de los 4 zips en
todas sus versiones, por nombre, por sha256 y por frases propias de cada documento. Estos cinco no estaban en ninguna
forma. Una afirmación anterior de "no está" se había hecho sobre un clon recortado (52 commits) y solo por nombre. Por
eso dio por faltantes `specific_catalog.json` y `TEMPLATE_BRIEF_VIGENTE.json`, que están como
`taller/recursos/catalogo_especificas.json` y `taller/recursos/template_brief.json`, y los 206 documentos fuente del
corpus, que están, verificados por sha256, en `apd/originales/` y su zip.
