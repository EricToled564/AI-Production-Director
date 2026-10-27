# Verificación antes de la tarea 2 — 2026-10-27

Antes de contestar las preguntas de arranque y empezar la tarea 2, se comprobó que cada archivo que cita el plan
reescrito (commit 0e00205) está en el universo o leído completo.

## 1. Citas archivo:línea del plan contra el universo

Un script compara cada cita `archivo:línea` del plan con las líneas de `universo_prueba_textos.jsonl`.

| Cita | Resultado | Consecuencia |
|---|---|---|
| `camera-lighting-vocabulary.md:228` | fuera del universo (sección de vocabulario de video, decisión por sección 26 §19) | C: el plan no puede citarla como regla. La regla de lente de la cara (24 §3) se apoya en los textos del universo anotados en `05`: INV-002125, INV-003020, INV-008157–008167, INV-008582–008584 |
| `dimensional.md`, `editing.md`, `golden-rules.md:140–150`, `gpt-image.md:94–100` | las únicas líneas fuera son líneas en blanco o cercas de código (comprobado: los archivos de `image/` tienen 0 líneas no vacías fuera, salvo las de otro modelo de `07`) | N |
| el resto de las citas | dentro del universo | N |

## 2. `visual-asset-critic` (tarea 11), leído completo

- `tools/validate_critique.py`, 385 líneas.
- `templates/critique.schema.json`, 183 líneas.
- `_shotkit.py` en las partes que usa el validador: `REPO_ROOT` (L19) y `capability_ids` (L112–120).

| Hallazgo | Evidencia | Consecuencia para el plan |
|---|---|---|
| El validador no corre en la copia instalada. `REPO_ROOT` es la carpeta padre de `tools/` y busca el schema en `REPO_ROOT/skills/visual-asset-critic/templates/` | `_shotkit.py:19`, `validate_critique.py:44–46`. Corrido: «schema not found at …/visual-asset-critic/skills/visual-asset-critic/templates/critique.schema.json» | C: la tarea 11 arma un entorno con `tools/` (`_shotkit.py`, `validate_critique.py`), `skills/visual-asset-critic/templates`, `skills/visual-asset-critic/examples` y `skills/visual-prompt-forge/adapters/_capabilities.json`, copiados del skill instalado, y corre el validador desde ahí. Probado: `--selftest` pasa y `--examples` sale «All critiques valid» |
| `generator` debe ser un id de la matriz de capacidades; el id de GPT Image es `gpt-image` (model_version «1.5/2»). `gpt-image-2` falla | `validate_critique.py:120–124`; `_capabilities.json`. Probado: «generator 'gpt-image-2' is not an id in the capability matrix» | C: la crítica lleva `generator: "gpt-image"` y `model_version: "2"` |
| HIGH exige `shot_id`, `brand_lock_ref` y `prompt_ref`; sin storyboard ni brand-lock la confianza máxima es MEDIUM | `validate_critique.py:107–118`; schema L56 («caps confidence at MEDIUM»). Probado: HIGH con `shot_id` y `brand_lock_ref` en null falla | C: confianza MEDIUM como máximo en todos los casos |
| En 1.1 son obligatorios, aunque admiten null: `run_id`, `round`, `created_at`, más la procedencia. `run_id` con formato `AAAAMMDDTHHMMSSZ-8hex` | schema L20–43, L154–181 | C: cada crítica lleva `run_id` de la ejecución, `round` (1 en la primera generación, 2 y 3 en las repeticiones de 26 §10) y `created_at` |
| Reglas de veredicto: un `blocking` obliga REJECT; un `major` impide ACCEPT; 3 o más `major` obligan REJECT | `validate_critique.py:66–86` | N: ya cubierto por «veredicto derivado» (`05`, INV-009776–009871) |

Probado con un JSON del caso K01 (`generator` «gpt-image», `model_version` «2», `shot_id`/`brand_lock_ref`/`seed` null,
MEDIUM): «All critiques valid».
