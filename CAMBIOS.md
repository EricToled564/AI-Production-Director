# Registro de cambios del repo

Cada cambio al repo se anota aquí en el mismo commit que lo hace: fecha, qué cambió, por qué y con qué orden. Empieza
con la reorganización del 2026-10-30, que dejó el repo en su estructura actual. Lo anterior está en el historial de
git. Los commits del 2026-10-30 se reescribieron al borrar contenido del historial por orden de Eric; los
identificadores de abajo son los vigentes.

| Fecha | Commit | Cambio | Orden |
|---|---|---|---|
| 2026-10-30 | `5eb1025` | Repo reorganizado en `1_originales/` a `6_mapa/`, con `LEEME.md`; templates y casos en carpetas propias | Eric: acomodar el repo de forma profesional |
| 2026-10-30 | `434eba0` | Niveles de generalidad y jerarquía de lectura extraídos de PLAN_V5 a `4_diseno/`; resto de PLAN_V5 borrado y desligado; `CONSULTA.md` reescrito como índice | Eric |
| 2026-10-30 | `3ee81e2` | Registrado que el paso de gates de los flujos originales no obliga al sistema nuevo | Eric |
| 2026-10-30 | `4d69110` | Hooks y registro de lectura del sistema anterior borrados | Eric: borrar todo el sistema anterior |
| 2026-10-30 | `15a4c11` | Sección «Cambios» en `.claude/rules/DECISIONES.md` (decisiones 1, 2, 7 y 9) | Eric |
| 2026-10-30 | `65325a6` | Zip original restaurado sin los 30 archivos de NotebookLM | Eric: no borrar el zip hasta revisarlo, salvo NotebookLM |
| 2026-10-30 | `1096cc1` | Archivos viejos del mapa borrados (capítulos, PDF y HTML, 141 explicaciones y sus programas); el mapa queda como índice | Eric |
| 2026-10-30 | `7891f6d` | Identificadores de commit citados, actualizados tras reescribir el historial | — |
| 2026-10-30 | `27aaffe` | Verificación: los casos de la decisión 4 están en la taxonomía | Eric |
| 2026-10-30 | `b328b26` | Corregidas dos afirmaciones falsas (régimen en `wip-verificacion`; recuperación de lo purgado) | — |
| 2026-10-30 | `3cb2af7` | NotebookLM quitado del zip anidado y de `project_knowledge_pack/` | Eric |
| 2026-10-30 | `a2bf96e` | Identificadores de commit citados, actualizados tras reescribir el historial | — |
| 2026-10-30 | — | Historial de `main` y de `wip-verificacion` reescrito: sin NotebookLM; `wip-verificacion` además sin las familias de régimen ni su investigación | Eric |
| 2026-10-30 | `bbc0581` | Regla de basura, auditorías y registro de cambios (`CLAUDE.md`); carpeta `7_auditorias_y_verificaciones/` con los verificadores de templates y casos, sus resultados y la verificación de la decisión 4; `MANIFIESTO.json` de templates con las rutas nuevas y la huella vigente de `FUENTES_CONTRATOS.json`; este registro | Eric |
| 2026-10-30 | `ee80e66` | Identificador del commit anterior anotado en este registro | — |
| 2026-10-30 | `29d88ce` | `METODO.md` borrado del zip, del zip anidado y de la parte 1 de `project_knowledge_pack/` (describía el método en el que NotebookLM decidía las reglas); también se borran del historial de `main` y de `wip-verificacion` sus versiones en `.claude/rules/METODO.md`. Corregida en `DECISIONES.md` la fila que decía que `wip-verificacion` no se había reescrito | Eric: opción A |
| 2026-10-30 | este commit | Historial de `main` y `wip-verificacion` reescrito sin `METODO.md`; identificadores de commit citados actualizados | Eric: opción A |
