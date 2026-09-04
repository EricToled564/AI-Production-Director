# Desplegar el ejecutor en Vercel

La misma página corre en dos lugares y se adapta sola:

| | Dentro de claude.ai (artifact) | Servida desde Vercel |
|---|---|---|
| Modelo | Claude, capacidad `sample` del visor | OpenAI (`OPENAI_MODEL`, por defecto `gpt-6-astra`) vía `POST /api/sample` |
| Quién paga | la cuenta de quien abre la página | la cuenta del `OPENAI_API_KEY` |
| Guardado | capacidad `db` | `localStorage` del navegador |
| Evaluador de video | análisis escena por escena de Higgsfield | cuadros extraídos en el navegador |

La detección es automática: si no hay `window.claude`, la página consulta
`/api/config` y usa el servidor.

## Variables de entorno del proyecto

| Variable | Obligatoria | Para qué |
|---|---|---|
| `OPENAI_API_KEY` | sí | Sin ella la app carga pero no puede generar ni auditar nada. Se crea en platform.openai.com → API keys. |
| `APP_PASSWORD` | recomendada | Sin ella, cualquiera con la URL gasta la cuenta del API key. La página la pide una vez y la guarda en el navegador. |
| `OPENAI_MODEL` | no | Id del modelo. Si falta se usa `gpt-6-astra`. Debe ser uno al que la cuenta tenga acceso (platform.openai.com → Limits). |

Se ponen en Vercel → Project → Settings → Environment Variables, y después
hay que volver a desplegar para que las tome.

## Qué sirve cada ruta

- `/` → `public/index.html`, la app completa con las 852 reglas embebidas.
- `/api/config` → `{servidor, ia, modelo, clave, claveOk}`. La página la consulta al abrir.
- `/api/sample` → puente con la Responses API de OpenAI. Responde SSE. El
  ajuste de esfuerzo de la app (alto/medio/bajo) se traduce a
  `reasoning.effort` (`xhigh`/`high`/`low`); el resumen del razonamiento se
  transmite como "pensando" mientras el modelo no ha escrito la primera letra.
- El bloque de reglas va primero en cada petición y con `prompt_cache_key`
  fijo, para que el cache de prompt de OpenAI lo reutilice entre rondas.

`maxDuration` de `/api/sample` está en 300 segundos porque una etapa con
esfuerzo alto puede tardar varios minutos.

## Regenerar la página

`public/index.html` y `app/ejecutor.html` se generan de la base de reglas:

```bash
python3 app/build_app.py --db rules.sqlite --out app/ejecutor.html --public public/index.html
```

No se editan a mano: el contenido vive en `app/build_app.py` y en
`rules.sqlite`.
