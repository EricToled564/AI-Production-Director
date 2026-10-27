# Verificación de las herramientas del plan: proceso y resultado — 2026-10-27

Tercera pregunta de arranque de Eric: «¿Verificaste que todas las herramientas creadas funcionan según su proceso, y no
solo que existen, sino que entregan lo que el plan y el procedimiento de la prueba esperan de ellas?».

Método: cada herramienta que existe y que el plan usa se corrió con un caso que debe pasar y otro que debe fallar. Se
comprobó el código de salida o la lista de errores que entrega. Antes y después de cada prueba se revisó `git status`:
ningún archivo del repo quedó cambiado sin querer.

| Herramienta (tarea) | Prueba | Resultado | Consecuencia |
|---|---|---|---|
| `v3/universo/decidir_textos.py` y `textos_universo.py` (1) | regenerar | salidas idénticas byte a byte (sha256 iguales); 2,724 textos | N |
| `textos_universo.py`, guardia de correcciones (1) | `sha256_original` alterado en `correcciones.json` | `AssertionError`, código 1; restaurado y regenerado igual | N |
| `v3/universo/adenda/construir_adenda.py` (1) | regenerar | 125 textos, 40 entran, código 0, salida idéntica | N |
| `v3/revision/verificar_lectura.py` (lectura) | real; sin la fila de INV-002383 | 0 / 0, código 0; 1 sin veredicto, código 1 | N |
| `v3/prueba/verificar_mapa.py` (2) | real; sin K38 y con un F15 inventado | código 0; 4 fallas (valor fuera del esquema, F11, F13 y F14 sin caso), código 1 | encontró que K18 debía ir en quality high; corregido |
| `verificar_templates.py` (3, 9) | `main` y las 14 pruebas de `probar_contratos.py` | código 0, 14/14; salidas idénticas | N |
| `validate_instance` con las formas del plan: `prueba/probar_verificar_templates.py` (3, 9) | 12 pruebas: K08 con texto del mundo, K32 con procedencia por inferencia, K14 edición, ancla sin D1–D9, LF sin estado final, slots fuera de orden, elipsis, brief cambiado | 12/12 como se esperaba | C: (a) con `modelo.nombre` distinto de «GPT Image 2» no se revisan los slots y no avisa: el plan lo exige exacto; (b) «...» o «…» en cualquier parte del prompt rechaza: el plan lo prohíbe también en los literales |
| `casos/validar.py` (3): `prueba/probar_validar_caso.py` | 8 casos: original, valor de extensión, sin confirmar, id desconocido, requisito sin resolver, sin aprobación, huella cambiada, ruta fuera del template | 8/8 como se esperaba | C: sale con código 0 aunque haya errores; el control lee `case_gate_errors`. Los valores de extensión no tienen id de opción: van con `option_ids` vacío y la decisión como evidencia |
| `.claude/hooks/rule_answer_check.py` (4) | registro de 2 reglas; respuesta completa y respuesta con duplicada, inventada y faltante | código 0 y 100 %; código 1 con 1 faltante, 1 inexistente, 1 contradictoria | N: funciona como dice; la tarea 4 crea la versión para ids INV/ADD y tres clases (es herramienta nueva, se prueba en su tarea) |
| `v2/piloto_gpt-image/construir.py` (6) | real; F15 «humano» en INV-002382 | «CORRECTA», código 0; «1 ERRORES … marca que no existe», código 1; restaurado con `git checkout` y borrado el xlsx generado | N |
| `produccion/template-retrato-gpt2/armar.py` (3, 9) | briefs aprobados; con «photorealistic»; con 470 palabras | código 0 y `PROMPTS.txt` idéntico; código 1 (rechazo); antes del cambio, 470 palabras daba código 1 | C: aplicado 26 §11; más de 300 palabras ahora da AVISO con código 0; la palabra prohibida sigue rechazando. `LEEME.md` actualizado |
| `gate_microgate`, `gate_dramaturgy`, `gate_image` (10): `prueba/probar_gates_entrega.py` | mensaje con el formato de la tarea 10; sin cabecera; sin OVERRIDE; con vocabulario prohibido | los tres código 0; cada falta bloquea su gate (código 2) | N |
| `visual-asset-critic/tools/validate_critique.py` (11): `prueba/validar_critica.py` | `--selftest`, `--examples`, crítica de K01 como la pide el plan, `generator` «gpt-image-2», HIGH sin storyboard ni brand-lock | código 0, 0, 0; código 1; código 1 | C: en la copia instalada no corre (no encuentra el schema); `validar_critica.py` lo corre sin modificarlo desde un entorno temporal con la estructura que espera |
| `list_events` (3, `mensaje_id`) | mensajes de usuario de esta sesión | cada mensaje de Eric trae su uuid (último: `c2da1f8f-4330-44a1-b9d7-edd7b8d360d9`, 09:54:01 UTC); el filtro «user» también trae resultados de herramientas, así que hay que quedarse con los que tienen texto | N |

Las herramientas que el plan manda crear en tareas posteriores todavía no existen, así que no se pueden correr hoy:
- el `rule_answer_check` adaptado (tarea 4);
- el verificador de forma extendido (tarea 6);
- `seleccionar.py` (tarea 8);
- `armar_contrato.py` (tarea 9);
- el script de QA mecánica (tarea 11).

El plan (§5) obliga a probar cada una igual, con un caso que pasa y uno que falla, antes de usarla.

## Añadido el 2026-10-27: herramientas de los insumos del universo y del esquema

La respuesta «Sí» a la tercera pregunta se dio antes de volver a correr estas herramientas. Se corrieron después:

| Herramienta | Prueba | Resultado |
|---|---|---|
| `v3/universo/verificar_origen.py` | contra los originales (`apd/originales`, SHA256SUMS OK, extraídos en el scratchpad); con una carpeta vacía | A, B, C 13,005/13,005, E 6/6, solo los 62 fallos D conocidos, `verificacion_origen.json` idéntico; con la carpeta vacía, código 1 |
| `secciones.py`, `decidir_secciones.py`, `clasificacion_misma_posicion.py` | regenerar | código 0; todas sus salidas idénticas byte a byte |
| `v2/construir_esquema.py` | regenerar | código 0; `esquema_taxonomia.json` idéntico |

La primera vez `verificar_origen.py` se corrió sin su argumento (la carpeta de originales) y dio código 1 por ese motivo.
Corrido como indica su uso, pasa.
