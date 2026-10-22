# Director de Prompts — creador y auditor de prompts de imagen y video

App web local que recibe un brief, decide **cada una** de las 1,398 reglas del registro vigente, ensambla
el prompt desde bloques trazados, ejecuta los gates originales del proyecto y sólo deja copiar o exportar
un texto cuyo hash coincide con el auditado. No genera imágenes ni video.

## 1. Arrancar (≈1 minuto)

Requisitos: Python 3.11+ (probado con 3.11 y 3.14) y dos paquetes, listados en `apd/requirements.txt`:
PyYAML (lo usa el linter aurora original en cada auditoría) y jsonschema (valida `shots.json` en spots y anclas).
En Ubuntu/WSL: `sudo apt install python3-yaml python3-jsonschema`; en otro entorno: `pip install -r apd/requirements.txt`.

En Windows use WSL (Ubuntu), no Python nativo: el `rule_registry.py` original calcula los ids con la ruta del
archivo y en Windows la ruta lleva `\`, así que los 1,398 ids cambiarían. Clone la rama `main`:
`git clone -b main https://github.com/EricToled564/AI-Production-Director.git`.

```bash
cd AI-Production-Director
python3 apd/server.py            # la primera vez reconstruye rules.sqlite desde los originales (~5 s)
# abrir http://127.0.0.1:8765
```

Con modelo (flujo automático de revisión por lotes y revisión semántica):

```bash
export OPENAI_API_KEY=…          # o ANTHROPIC_API_KEY=…   (sólo en el entorno del servidor)
export OPENAI_MODEL=gpt-6-astra  # opcional; ANTHROPIC_MODEL=claude-sonnet-5
export OPENAI_REASONING_EFFORT=medium  # opcional: low | medium | high; sin definir = default del modelo
python3 apd/server.py
```

Sin clave la app funciona en modo determinista y lo dice: puede inspeccionar, decidir a mano, firmar
revisión humana o exportar los lotes a un revisor externo e importarlos con la misma validación.
`APP_PASSWORD=…` protege la API. Escucha sólo en 127.0.0.1.

## 2. Ejecutar un brief

1. **Nuevo brief** → texto (y referencias con su rol, modelo y formato si los sabe) → *Analizar brief*.
2. **Plan**: la tarjeta *Brief en plantilla* muestra el brief ordenado en bloques; cada bloque coincide con una
   faceta de la base de reglas (caso, medio, D1–D9) y con un slot del prompt. Cámara, luz, ángulo, lugar,
   lente y encuadre **no se preguntan**: los infiere el modelo (con clave) o las reglas deterministas citadas
   (sin clave); lo que usted escribió siempre gana. *Falta y no se puede inferir* lista sólo lo imposible de
   deducir. Debajo: recorrido, etapas que aplican y que no (con razón), subprocesos y gates. *Aceptar
   propuestas* cierra ambigüedades (cada propuesta dice si viene de una fuente citada o es creativa).
3. **Prompts**: texto final, parámetros fuera del texto, bloques con las reglas que satisfacen; cuatro
   estados separados — cobertura de IDs, semántica, redacción, resultado visual.
4. **Auditoría**: *Auditar todas* ejecuta los gates originales sin modificar (gate_image, gate_dramaturgy,
   aurora, AST gate v3.4, render v3.4). Revisión con modelo, revisión externa o firma humana. Un NO_CUMPLE del
   revisor sólo se cierra corrigiendo el bloque fuente o con *Disputar con autoridad* (archivo:línea citado).
   *Resolver en Reglas* lleva de un bloqueo a las reglas que lo causan.
5. **Reglas**: las 1,398 con estado, razón y capa; filtros por caso, tarea, faceta, fuente y motivo;
   ficha con texto original y trazabilidad; decisión humana en bloque.
6. *Aprobar redacción* → *Copiar prompt final* (verifica sha256 en el navegador) → **Exportar**.

Cambios: **Especificación** (editar campos crea una versión y recompila sólo lo afectado), **Versiones**
(antes/después), **Feedback** (primer contrato afectado), **Evaluación visual** (defectos del render,
separados de la cobertura de reglas).

Un cambio es **quirúrgico** (`apd/politicas.py` U-2026-09-28-CAMBIO-QUIRURGICO). Hay tres niveles y lo decidido
en un nivel anterior queda fijo:

| Nivel | Qué cambia | Qué se vuelve a revisar |
|---|---|---|
| 0 · medio | imagen ↔ video | sólo las reglas del medio nuevo; las del otro medio nunca entran en la revisión |
| 1 · perfil de reglas | caso o tipo de pieza (retrato → editorial, una persona → grupo) | todas las reglas de ese medio |
| 2 · bloque | un campo (edad, fondo, luz…) | nada de la clasificación de reglas: se hereda y se confirma sola. Un cambio **dramático** (sexo, origen, franja de edad, o un bloque reescrito) re-revisa sólo las reglas de los bloques cambiados e invalida la aprobación de redacción; uno menor conserva revisión y aprobación |

La auditoría determinista (gates originales) siempre se vuelve a ejecutar.

Políticas permanentes del director para todo brief: compilación en los 5 slots de GPT Image (CF-MOTOR-SW30 → b)
y SW30 con máximo 2 intentos por método (CF-REROLL-SW30 → b).

## 3. Pruebas

```bash
cd apd/tests && python3 -m unittest -v      # 77 pruebas: registro, gates, lotes, flujos, plantilla, cambio quirúrgico, e2e, HTTP, adaptadores
python3 apd/tools/check_citas.py apd/data/sintaxis_fuente.json   # 831 citas de sintaxis verificadas
# prueba de interfaz: Chromium hace clic en la app real (necesita Node + Playwright)
NODE_PATH=$(npm root -g) node apd/tools/ui_aceptacion.cjs        # 29 comprobaciones → apd/evidencia/ui/
```

## 4. Estructura

| Ruta | Qué es |
|---|---|
| `apd/originales/` | los 4 archivos entregados, sólo lectura, con `SHA256SUMS` |
| `apd/data/` | derivados con procedencia: registro, reconciliación, clasificación completa, cruce v3.4, plantillas, sintaxis, inventario |
| `apd/apd/` | motor: `registro`, `spec`, `plan`, `ledger`, `conflictos`, `sintaxis`, `compilador`, `auditoria`, `revision`, `llm`, `proyecto`, `store` |
| `apd/web/` | interfaz |
| `apd/tests/` | pruebas |
| `apd/demo/` | proyecto de demostración (quinteto, 18 versiones): base SQLite, exportación, prompts y auditorías — `APD_DB=apd/demo/demo.sqlite python3 apd/server.py` |
| `apd/evidencia/` | informes de ejecución (tests originales, pruebas de la app) |
| `apd/CHECKLIST_CUMPLIMIENTO.md` | checklist con evidencia |

Los originales del repo (`.claude/`, `app/`, `api/`, `produccion/`, …) no se modifican: la app los lee y
ejecuta sus gates como subprocesos.
