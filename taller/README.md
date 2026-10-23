# Taller de brief y prompt — GPT Image 2, imágenes

App que convierte la idea original del usuario en un brief creativo y técnico completo y, solo después
de validarlo, en un prompt para GPT Image 2. Python estándar (sin dependencias) y una interfaz web.
Corre en local (Windows, macOS, Linux) o desplegada en Vercel (ver "Despliegue en Vercel").

## Arranque

```bash
python taller/server.py
# abrir http://127.0.0.1:8770
```

Variables de entorno opcionales:

| Variable | Uso | Por defecto |
|---|---|---|
| `TALLER_PROVEEDOR` | `anthropic`, `manual` u `openai` | `anthropic` |
| `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL` | proveedor Anthropic (Messages API) | modelo `claude-opus-5-5` |
| `OPENAI_API_KEY`, `OPENAI_MODEL`, `OPENAI_REASONING_EFFORT` | proveedor OpenAI (Responses API) | — |
| `TALLER_LIMITE_LLAMADA_S` | tiempo máximo de una llamada al modelo | `600` local, `280` en Vercel |
| `TALLER_PUERTO` | puerto local | `8770` |
| `TALLER_DB` | ruta de la base SQLite de casos | `taller/datos/taller.sqlite3` |

Si la clave falta o el proveedor falla al crearse, la app cae al modo manual y lo avisa.

**Modo manual.** Cada vez que una etapa necesita al modelo, la app muestra la solicitud completa
(instrucciones + datos). Se copia a ChatGPT o Claude, se pega la respuesta JSON y la app la valida
con las mismas reglas que una respuesta de API. Una respuesta que no pasa la validación se rechaza
con el motivo; no se acepta a medias.

## Despliegue en Vercel

Proyecto con `rootDirectory = taller`. La función `api/index.py` atiende `/api/*`; `static/` se sirve como
sitio estático (`vercel.json`). Las rutas y compuertas son las mismas del servidor local (`rutas.py`).

Diferencias con el modo local, porque una función de Vercel no tiene disco persistente ni hilos en
segundo plano:

- **Los casos viven en el navegador** (IndexedDB, con localStorage de respaldo). Cada petición envía la
  instantánea del caso y el servidor devuelve la actualizada (`nube.py`, `AlmacenMemoria`). Otro
  navegador u otra computadora no ven tus casos: usa **Exportar respaldo / Importar respaldo**.
- **Una llamada al modelo por petición.** Si una operación necesita varias (selección por lotes,
  rondas de redacción), la interfaz repite la petición sola y reutiliza las respuestas ya guardadas.
  Cada llamada debe caber en `maxDuration` = 300 s (plan Hobby).
- **Contraseña obligatoria.** La URL es pública y gasta la cuenta del proveedor: la API exige la cabecera
  `X-Taller-Clave` igual a `TALLER_CLAVE_ACCESO`. Sin esa variable definida la app no se abre. La página la
  pide una vez y la guarda en el navegador.

Variables del proyecto en Vercel (Settings → Environment Variables; después volver a desplegar):

| Variable | Obligatoria | Para qué |
|---|---|---|
| `ANTHROPIC_API_KEY` | sí, para usar la API | Sin ella la app cae al modo manual (copiar y pegar). |
| `TALLER_CLAVE_ACCESO` | sí | Contraseña de la app. |
| `ANTHROPIC_MODEL` | no | Por defecto `claude-opus-5-5`. |

## El proceso (las compuertas no se pueden saltar)

| Paso | Etapa en la app | Qué exige para avanzar |
|---|---|---|
| 1 | `original` | El texto original se guarda tal cual y no se edita nunca. Los datos nuevos entran como aportes aparte. |
| 2 | desarrollo del brief | El modelo llena los 109 campos de `template_brief.json`. Cada campo queda `proporcionado` (con cita literal del original o de un aporte, verificada), `inferido` (con fundamento), `propuesta` (con fundamento, la decide el usuario), `falta` (con pregunta) o `condicion_inactiva` (prohibido en campos de condición "siempre" y en los requeridos de T-GENESIS). No hay campos vacíos silenciosos. |
| 3 | `brief_revision` | Se muestra el brief completo. El usuario acepta, modifica o rechaza cada propuesta y responde cada pregunta (o deja el campo vacío con explicación obligatoria). Debe marcar "Revisé el brief completo". |
| 4 | corrector | Solo con 0 pendientes y revisión marcada. Solo un error objetivo (FAIL) devuelve el brief al usuario; lo que solo el usuario puede decidir nunca lo devuelve: sale como nota (UNCERTAIN) visible que no bloquea. El corrector responde solo con excepciones y tiene un máximo de 45 s por API (tope de 4000 tokens de salida; razonamiento bajo en OpenAI, ajustable con `TALLER_ESFUERZO_REVISION`). Si el proveedor no responde a tiempo, la app lo informa y se reintenta. |
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

28 pruebas: modo nube (contraseña, instantánea en el navegador, una llamada por petición, manual en la nube, despacho compartido), compuertas no saltables, corrector que devuelve al usuario, invalidación al reabrir,
flujo completo hasta aprobación con un modelo simulado, quality no inventada, redacción automática
tras fallo determinista, notas del corrector que no devuelven el brief, límite de 45 s en la revisión, ambigüedades, notas contextuales, validadores, modo manual y API HTTP.

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
- No se ha corrido ninguna etapa contra la API de Anthropic desde el entorno de desarrollo (no había
  clave). El flujo completo se corrió con instancias de Claude por la vía manual (ver
  `demo/PRUEBA_SPINNING_prompt_exportado.md`) y con un modelo simulado en las pruebas.
- La app no genera imágenes.
