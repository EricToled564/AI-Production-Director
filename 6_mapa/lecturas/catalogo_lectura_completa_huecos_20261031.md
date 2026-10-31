# Lectura: taxonomía completa para la búsqueda de huecos (2026-10-31)

Documento: `4_diseno/casos/catalogo_opciones.json`, los 1,729 registros leídos uno por uno (nombre, alias y definición),
más las extensiones F32 a F35 de `3_taxonomia/TAXONOMIA_CANONICA.md`. Motivo: Eric preguntó si la búsqueda de
huecos había leído la taxonomía completa o solo palabras clave; la respuesta era no, y se rehízo.

| Tramo | Qué dice para los huecos | Consecuencia |
|---|---|---|
| TRM-0001 a 0261 (F03 a F29, METADATOS) | Lugar genérico (TRM-0136) nombra calle, cocina y estudio como ejemplos; F16 solo interior y exterior; Fenómeno meteorológico (TRM-0124) y Fenómeno luminoso (TRM-0123) con ejemplos; F05 moda y música citan lookbooks y portadas; SFX de ambiente cita ciudad y lluvia | Estado «solo como ejemplo» o «solo fuera de imagen» de esos valores en el informe |
| TRM-0262 a 0496 (F30: lente, luz, color, composición, anatomía, identidad, materialidad) | Luz natural: solar, cubierto, lunar, ventana; Balance de blancos cita luz de día; Cámara desechable cita nostalgia; materialidad solo tiene propiedades; cobre, cerámica y vidrio como ejemplos | Ídem; ningún tipo de material ni momento del día como valor |
| TRM-0497 a 0899 (F10, estructura del prompt, marca, dramaturgia, física, F23, F08, F09, F12) | Cambio meteorológico y de estación son operaciones; Bloque de iluminación cita niebla y humo; Tono de pieza cita premium; Partículas cita polvo, vapor y lluvia; F23 Material | Ídem; mood solo de marca |
| TRM-0900 a 1369 (parámetros, guion, texto en pantalla, F17, F18, composición, filtros, trazabilidad, F29) | TRM-0978 DAY/NIGHT/DUSK es campo de guion; texto en pantalla solo tamaños y pesos; Luz ambiente continua cita hora azul; Fondo opaco cita fondo blanco; modo Detallado tiene apartado de ánimo | Ídem; ninguna familia tipográfica |
| OPT y PLT (valores de las facetas) | «07 luz y clima», «08 multitud anónima», Instagram y LinkedIn citan carrusel | Ídem |

Resultado: tabla «Lo que ya tiene la taxonomía» en `7_auditorias_y_verificaciones/busqueda_huecos_taxonomia_20261031.md`.
