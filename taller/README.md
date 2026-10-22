# Taller de brief y prompt — GPT Image 2, imágenes

App local que convierte la idea original del usuario en un brief creativo y técnico completo y,
solo después de validarlo, en un prompt para GPT Image 2. Python estándar (sin dependencias) y una
interfaz web en el navegador. Funciona en Windows, macOS y Linux.

## Arranque

```bash
python taller/server.py
# abrir http://127.0.0.1:8770
```

Variables de entorno opcionales:

| Variable | Uso | Por defecto |
|---|---|---|
| `TALLER_PROVEEDOR` | `manual`, `openai` o `anthropic` | `manual` |
| `OPENAI_API_KEY`, `OPENAI_MODEL`, `OPENAI_REASONING_EFFORT` | proveedor OpenAI (Responses API) | — |
| `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL` | proveedor Anthropic (Messages API) | — |
| `TALLER_PUERTO` | puerto local | `8770` |
| `TALLER_DB` | ruta de la base SQLite de casos | `taller/datos/taller.sqlite3` |

Si la clave falta o el proveedor falla al crearse, la app cae al modo manual y lo avisa.

**Modo manual.** Cada vez que una etapa necesita al modelo, la app muestra la solicitud completa
(instrucciones + datos). Se copia a ChatGPT o Claude, se pega la respuesta JSON y la app la valida
con las mismas reglas que una respuesta de API. Una respuesta que no pasa la validación se rechaza
con el motivo; no se acepta a medias.

## El proceso (las compuertas no se pueden saltar)

| Paso | Etapa en la app | Qué exige para avanzar |
|---|---|---|
| 1 | `original` | El texto original se guarda tal cual y no se edita nunca. Los datos nuevos entran como aportes aparte. |
| 2 | desarrollo del brief | El modelo llena los 109 campos de `template_brief.json`. Cada campo queda `proporcionado` (con cita literal del original o de un aporte, verificada), `inferido` (con fundamento), `propuesta` (con fundamento, la decide el usuario), `falta` (con pregunta) o `condicion_inactiva` (prohibido en campos de condición "siempre" y en los requeridos de T-GENESIS). No hay campos vacíos silenciosos. |
| 3 | `brief_revision` | Se muestra el brief completo. El usuario acepta, modifica o rechaza cada propuesta y responde cada pregunta (o deja el campo vacío con explicación obligatoria). Debe marcar "Revisé el brief completo". |
| 4 | corrector | Solo con 0 pendientes y revisión marcada. Si falla, el brief vuelve al usuario con las observaciones; no se genera prompt. |
| 5 | `brief_validado` → selección | Con el brief validado se seleccionan reglas específicas del catálogo: cada una con fuente, por qué aplica (cita del brief) y bloque destino. Más de dos por bloque es aviso para evaluar el filtro, nunca un tope. Las dudas del revisor de selección las decide el usuario. |
| 6 | `plantilla_vista` | Se muestra la plantilla de 5 bloques con sus instrucciones de llenado y las 12 reglas universales literales. El usuario elige `quality` (la app no inventa un valor por defecto). |
| 7 | redacción | El redactor arma el prompt con el brief validado, las instrucciones y las reglas seleccionadas; el documento lleva al inicio las instrucciones y reglas con trazabilidad y los textos canónicos sin alterar. |
| 8 | revisor semántico | Verifica cumplimiento real regla por regla. Violaciones claras vuelven al redactor automáticamente (hasta 3 rondas). Comprobaciones deterministas adicionales: 5 bloques en orden, placeholders, vocabulario prohibido, quality y size válidos. |
| 9 | `prompt_ambiguedades` | Las ambigüedades se marcan en rojo en el texto con nota al pie. El usuario decide; la decisión va al redactor y al revisor y se guarda como nota contextual ligada a la regla (este caso o casos similares), sin reescribir el texto canónico. |
| 10 | `revision_final` → `aprobado` | Prompt revisado para revisión final. Un comentario repite el ciclo. El usuario aprueba y exporta; la generación de la imagen la decide y la hace el usuario fuera de la app. |

Cambiar el brief después de validarlo (reabrir o agregar un aporte) invalida todo lo posterior:
selección, plantilla y prompt se rehacen. Brief y prompt nunca se crean a la vez.

## Recursos

`taller/recursos/` contiene copias byte a byte de los archivos vigentes del proyecto
(`template_brief.json`, `universal_rules.json`, `canonical_sources.json`, `operation_packs.json`,
`user_directives.json`, `catalogo_especificas.json`) y dos archivos propios
(`instrucciones_llenado.json`, `directivas_taller.json`). `MANIFIESTO.json` guarda el sha256 y la
procedencia de cada uno; la app avisa en la interfaz si alguno fue modificado.

## Pruebas

```bash
python -m unittest discover -s taller/tests
```

20 pruebas: compuertas no saltables, corrector que devuelve al usuario, invalidación al reabrir,
flujo completo hasta aprobación con un modelo simulado, quality no inventada, redacción automática
tras fallo determinista, ambigüedades, notas contextuales, validadores, modo manual y API HTTP.

## Caso de demostración

```bash
python taller/demo/cargar_demo.py
```

Carga el caso real de spinning (`demo/ORIGINAL_SPINNING.txt` + respuesta previa como aporte) y pega
el desarrollo del brief de `demo/desarrollo_spinning.json` por la misma vía manual, validado por la
app. Se detiene en el paso 3 con las decisiones pendientes para revisión del usuario.

## Limitaciones conocidas

- El catálogo de reglas específicas (`catalogo_especificas.json`, 607 unidades) es provisional:
  el catálogo definitivo de textos todavía no se ha hecho.
- No se ha corrido ninguna etapa con un modelo real por API desde el entorno de desarrollo (la
  clave disponible no tenía crédito). El flujo completo está probado con un modelo simulado; con
  modelo real conviene empezar en modo manual o con una clave con crédito y revisar la primera
  corrida etapa por etapa.
- La app no genera imágenes.
