# Registro de cambios del repo

Cada cambio al repo se anota aquí en el mismo commit que lo hace: fecha, qué cambió, por qué y con qué orden. Empieza
con la reorganización del 2026-10-30, que dejó el repo en su estructura actual. Lo anterior está en el historial de
git. Los commits del 2026-10-30 se reescribieron al borrar contenido del historial por orden de Eric; los
identificadores de abajo son los vigentes.

| Fecha | Commit | Cambio | Orden |
|---|---|---|---|
| 2026-10-30 | `cd15644` | Repo reorganizado en `1_originales/` a `6_mapa/`, con `LEEME.md`; templates y casos en carpetas propias | Eric: acomodar el repo de forma profesional |
| 2026-10-30 | `95d7f16` | Niveles de generalidad y jerarquía de lectura extraídos de PLAN_V5 a `4_diseno/`; resto de PLAN_V5 borrado y desligado; `CONSULTA.md` reescrito como índice | Eric |
| 2026-10-30 | `510de3b` | Registrado que el paso de gates de los flujos originales no obliga al sistema nuevo | Eric |
| 2026-10-30 | `234dcfc` | Hooks y registro de lectura del sistema anterior borrados | Eric: borrar todo el sistema anterior |
| 2026-10-30 | `1a17894` | Sección «Cambios» en `.claude/rules/DECISIONES.md` (decisiones 1, 2, 7 y 9) | Eric |
| 2026-10-30 | `1fa76a0` | Zip original restaurado sin los 30 archivos de NotebookLM | Eric: no borrar el zip hasta revisarlo, salvo NotebookLM |
| 2026-10-30 | `98d8319` | Archivos viejos del mapa borrados (capítulos, PDF y HTML, 141 explicaciones y sus programas); el mapa queda como índice | Eric |
| 2026-10-30 | `4ec61bd` | Identificadores de commit citados, actualizados tras reescribir el historial | — |
| 2026-10-30 | `b04cddd` | Verificación: los casos de la decisión 4 están en la taxonomía | Eric |
| 2026-10-30 | `d307e84` | Corregidas dos afirmaciones falsas (régimen en `wip-verificacion`; recuperación de lo purgado) | — |
| 2026-10-30 | `7d03066` | NotebookLM quitado del zip anidado y de `project_knowledge_pack/` | Eric |
| 2026-10-30 | `26f5023` | Identificadores de commit citados, actualizados tras reescribir el historial | — |
| 2026-10-30 | — | Historial de `main` y de `wip-verificacion` reescrito: sin NotebookLM; `wip-verificacion` además sin las familias de régimen ni su investigación | Eric |
| 2026-10-30 | este commit | Regla de basura, auditorías y registro de cambios (`CLAUDE.md`); carpeta `7_auditorias_y_verificaciones/` con los verificadores de templates y casos, sus resultados y la verificación de la decisión 4; `MANIFIESTO.json` de templates con las rutas nuevas y la huella vigente de `FUENTES_CONTRATOS.json`; este registro | Eric |
