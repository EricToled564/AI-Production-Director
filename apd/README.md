# Director de Prompts — creador y auditor de prompts de imagen y video

App web local que recibe un brief, decide **cada una** de las 1,398 reglas del registro vigente, ensambla
el prompt desde bloques trazados, ejecuta los gates originales del proyecto y sólo deja copiar o exportar
un texto cuyo hash coincide con el auditado. No genera imágenes ni video.

## 1. Arrancar (≈1 minuto)

Requisitos: Python 3.11+. Opcional: `pip install jsonschema` (valida `shots.json` contra el esquema
original en spots).

```bash
cd AI-Production-Director
python3 apd/server.py            # la primera vez reconstruye rules.sqlite desde los originales (~5 s)
# abrir http://127.0.0.1:8765
```

Con modelo (flujo automático de revisión por lotes y revisión semántica):

```bash
export OPENAI_API_KEY=…          # o ANTHROPIC_API_KEY=…   (sólo en el entorno del servidor)
export OPENAI_MODEL=gpt-6-astra  # opcional; ANTHROPIC_MODEL=claude-sonnet-5
python3 apd/server.py
```

Sin clave la app funciona en modo determinista y lo dice: puede inspeccionar, decidir a mano, firmar
revisión humana o exportar los lotes a un revisor externo e importarlos con la misma validación.
`APP_PASSWORD=…` protege la API. Escucha sólo en 127.0.0.1.

## 2. Ejecutar un brief

1. **Nuevo brief** → texto (y referencias con su rol, modelo y formato si los sabe) → *Analizar brief*.
2. **Plan**: recorrido (imagen / referencia / edición / clip / ancla / spot + track), etapas que aplican y
   que no (con razón), subprocesos, gates. *Aceptar propuestas* para cerrar ambigüedades (cada propuesta
   dice si viene de una fuente citada o es creativa de la app).
3. **Prompts**: texto final, parámetros fuera del texto, bloques con las reglas que satisfacen; cuatro
   estados separados — cobertura de IDs, semántica, redacción, resultado visual.
4. **Auditoría**: *Auditar todas* ejecuta los gates originales sin modificar (gate_image, gate_dramaturgy,
   aurora, AST gate v3.4, render v3.4). Revisión con modelo, revisión externa o firma humana. Un NO_CUMPLE del
   revisor sólo se cierra corrigiendo el bloque fuente o con *Disputar con autoridad* (archivo:línea citado).
   *Resolver en Reglas* lleva de un bloqueo a las reglas que lo causan. Si editar el brief cambia el contexto de
   una revisión de reglas ya hecha, la revisión se **hereda** visiblemente y bloquea hasta re-revisar o confirmar.
5. **Reglas**: las 1,398 con estado, razón y capa; filtros por caso, tarea, faceta, fuente y motivo;
   ficha con texto original y trazabilidad; decisión humana en bloque.
6. *Aprobar redacción* → *Copiar prompt final* (verifica sha256 en el navegador) → **Exportar**.

Cambios: **Especificación** (editar campos crea una versión y recompila sólo lo afectado), **Versiones**
(antes/después), **Feedback** (primer contrato afectado), **Evaluación visual** (defectos del render,
separados de la cobertura de reglas).

## 3. Pruebas

```bash
cd apd/tests && python3 -m unittest -v      # 68 pruebas: registro, gates, lotes, flujos, e2e, HTTP, adaptadores
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
| `apd/demo/` | proyecto de demostración (quinteto, 11 versiones): base SQLite, exportación, prompts y auditorías — `APD_DB=apd/demo/demo.sqlite python3 apd/server.py` |
| `apd/evidencia/` | informes de ejecución (tests originales, pruebas de la app) |
| `apd/CHECKLIST_CUMPLIMIENTO.md` | checklist con evidencia |

Los originales del repo (`.claude/`, `app/`, `api/`, `produccion/`, …) no se modifican: la app los lee y
ejecuta sus gates como subprocesos.
