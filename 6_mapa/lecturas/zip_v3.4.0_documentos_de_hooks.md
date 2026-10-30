# Lectura: documentos del zip original que explican los hooks (2026-10-30)

Archivo: `1_originales/AI_Production_Director_v3.4.0_COMPLETE.zip`, carpeta interna `AI_Production_Director_v3.4.0_COMPLETE/`.
El zip tiene 750 archivos: 214 en `skills/` y 536 fuera. Los 536 no están en el corpus (taxonomía §0.1, L37–76) y nunca
se leyeron completos (PENDIENTES P-18).

| Documento | Líneas | Leído |
|---|---:|---|
| `repo/.claude/hooks/README.md` | 214 | Completo |
| `START_HERE.md` | 75 | Completo |
| `INDEX.md` | 318 | Solo L1–120 |

## `repo/.claude/hooks/README.md`

| Líneas | Qué dice | Consecuencia |
|---|---|---|
| L1–9 | «Seis hooks que hacen ejecutables reglas que los skills ya declaraban obligatorias». Corren fuera del modelo y devuelven `exit 2`, y el turno no cierra | Son validadores de reglas que ya están en el corpus, no reglas nuevas |
| L13–19 | La tabla de cada gate: `gate_dramaturgy` (Stop, director §6.1 → `video/references/dramaturgy.md`), `gate_image` (Stop, director Etapa 5 y §6.2 → `image/references/golden-rules.md`), `gate_shots` (PostToolUse → `storyboard-architect/tools/validate_shots.py`), `gate_microgate` (`produccion-visual-sw30` §MICRO-GATE) e `inject_rules` (`produccion-visual-sw30` §PREGUNTA DE AVANCE) | Los tres primeros delegan en archivos del corpus. Los dos últimos dependen de `produccion-visual-sw30`, que no está en el corpus (taxonomía L74) |
| L21–41 | `inject_rules.py` inyecta completas las fuentes que gobiernan cada prompt visual (41,226 caracteres para imagen); `gate_microgate.py` exige la cabecera `SKILL:` / `RIESGOS:` / `TÉCNICA:` | Controlan la conducta del agente en el chat, no el prompt |
| L43–58 | `gate_image`: R1 verbo inicial (bloquea), R4 lenguaje natural (bloquea), §6.2 modelo declarado (bloquea), R2 encuadre positivo (solo advierte, porque el ejemplo aprobado dice `no makeup`) | Es la validación de imagen que piden los flujos (INV-000247) |
| L60–72 | `gate_dramaturgy` lee la lista prohibida de `dramaturgy.md` al correr; hoy son 11 términos. Solo revisa bloques de código. Override con `OVERRIDE: término - razón` | Es la validación de vocabulario que piden los flujos (INV-000248) |
| L74–84 | `gate_shots` corre `validate_shots.py` y repara dos defectos de instalación: falta de `jsonschema` y la ruta `REPO_ROOT` de `_shotkit.py` | Validación de la etapa 4 |
| L86–97 | `verify.sh`: 34 casos de prueba | No está en el repo; está en el zip |
| L99–133 | Cobertura: 1,263 enunciados normativos en los skills; los gates verifican 26 controles, el 2.1 % | Los gates no sustituyen la clasificación del corpus |
| L135–149 | `rule_registry.py` y `rule_ledger.py`: cada regla con disposición o queda `PENDING` | Antecedente de un catálogo de reglas; está en el zip |
| L151–167 | Dos contradicciones: el ejemplo ✅ de la Regla 4 de `image` empieza con «A» y usa `cinematic`; la lista prohibida de `image` está en `gpt-image.md:36` y `models.md:49` | Hay que contrastarlas con las explicaciones del capítulo 5 cuando se clasifique |
| L169–195 | Probado al ejecutarlos a mano; **no** se probó que Claude Code los dispare solo | Si se restauran como hooks activos, hay que probarlos en una sesión nueva |
| L197–214 | Requiere `pyyaml` y `jsonschema`. El gate de vocabulario es léxico. Los hooks no existen en el chat de claude.ai | — |

## `START_HERE.md`

| Líneas | Qué dice | Consecuencia |
|---|---|---|
| L1–4 | Copia autosuficiente de la v3.4.0 «construida en la sesión»; no elimina ningún archivo del árbol original | — |
| L8–17 | Contenido: `repo/` (runtime, hooks, rulesets, schemas, API/app, producción y validadores), `skills/`, `ruleset-3.4.0.json`, `production-package/` (`RULES_MATRIX.md`, `template_engine.py`, `audit_gi2.py`), el zip fuente original, `project_knowledge_pack/`, `requirements.txt`, `VERIFY_COMPLETE_PACKAGE.py` y `MANIFEST_SHA256.txt` | Dentro del zip hay un sistema anterior completo que no está en el corpus (P-18) |
| L40–55 | La verificación obligatoria exige `rule_count = 1704` en el ruleset 3.4.0 | Ese ruleset es un catálogo de reglas anterior; nunca se leyó |
| L57–71 | El runtime está en `repo/.claude/hooks/`; un cambio a la base de conocimiento se recompila y se publica en una versión nueva | — |
| L73–75 | `RULES_MATRIX.md`, `template_engine.py` y `audit_gi2.py` son `SOURCE_RECONSTRUCTED`: reconstruidos a partir del zip fuente | `audit_gi2` es el paso que los flujos nombran junto a los gates (INV-000565) |

## `INDEX.md` (L1–120 de 318)

| Líneas | Qué dice | Consecuencia |
|---|---|---|
| L3–5 | Generado el 2026-09-10; los skills vienen de las skills sincronizadas de la cuenta; el repo, de `EricToled564/AI-Production-Director` @ `8b204f7` | — |
| L9–31 | 13 skills, con su capa en el pipeline; `aurora-prompt-linter` y `produccion-visual-sw30` están entre ellas | El corpus tiene 11 de las 13 (taxonomía §0.1). Aurora está excluida por decisión |
| L35–120 | Inventario de archivos: hooks, `.claude/rules/`, app Vercel, corpus NotebookLM, `nblm-ids/` y skills | Sin consecuencia nueva. L121–318 no se leyeron |
