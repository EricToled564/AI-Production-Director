# Registro de cambios del repo

Cada cambio al repo se anota aquí en el mismo commit que lo hace: fecha, commit, qué cambió y con qué orden. Empieza
con la reorganización del 2026-10-30, que dejó el repo en su estructura actual. El historial de git se reescribió ese
día al borrar, por orden de Eric, los documentos que ordenó borrar y toda referencia a ellos.

| Fecha | Commit | Cambio | Orden |
|---|---|---|---|
| 2026-10-30 | — | Repo reorganizado en `1_originales/` a `7_auditorias_y_verificaciones/`, con `LEEME.md`, `PENDIENTES.md` y este registro; templates y casos de uso en carpetas propias; el mapa queda como índice (`6_mapa/CONSULTA.md`) | Eric |
| 2026-10-30 | — | Niveles de generalidad y jerarquía de lectura en `4_diseno/` | Eric |
| 2026-10-30 | — | Los 6 gates y su `settings.json` en `4_diseno/validadores/`, idénticos a los del zip y sin activar | Eric |
| 2026-10-30 | — | Regla de basura, auditorías y registro de cambios en `CLAUDE.md`; verificadores de templates y casos y sus resultados en `7_auditorias_y_verificaciones/` | Eric |
| 2026-10-30 | — | Borrados del repo y del historial los documentos que Eric ordenó borrar, y toda referencia a ellos: archivos del agente, registros de decisiones, taxonomía (L74, L444, L1030; TRM-1321 pasa a SIN PRESENCIA), catálogo de casos regenerado, corpus (2 textos menos: 13,003) y `flujo-anclas.html`. El zip solo cambió en lo que Eric ordenó | Eric: OK a la lista única |
| 2026-10-30 | 8e40baf | `README.md` de los hooks restaurado literal en `4_diseno/validadores/`, idéntico a la copia del zip | Eric: restaurarlo junto a los hooks |
| 2026-10-30 | cf411cc | Taxonomía L71–L73: retiradas las filas que nombraban documentos que ya no existen ni en el repo ni en el zip; catálogo de casos regenerado | Eric: borrar toda referencia a documentos que ya no existen, salvo los que están en el zip |
| 2026-10-30 | dce3046 | Verificación: la taxonomía prohíbe y no usa estados que excluyan reglas de la selección (`7_auditorias_y_verificaciones/`) | Eric |
| 2026-10-30 | este commit | Revisión de la estructura de la taxonomía y del catálogo de casos de uso, con recomendación de reestructura y pendientes R-1 a R-5 (`7_auditorias_y_verificaciones/revision_estructura_taxonomia_y_casos_20261030.md`); registros de lectura en `6_mapa/lecturas/`; hashes de las tres filas anteriores. Sin cambios en la taxonomía ni en el catálogo | Eric: revisión exhaustiva sin parchar |
