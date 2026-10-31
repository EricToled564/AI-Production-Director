# AI Production Director: sistema que genera prompts

El sistema extrae del corpus las reglas que aplican a un caso de imagen y las convierte en prompts. No genera imágenes:
Eric hace las imágenes.

## Dónde está cada cosa

Las carpetas siguen el orden del sistema, de la fuente al prompt.

| Carpeta | Qué hay | Para qué sirve |
|---|---|---|
| `1_originales/` | Zip del paquete v3.4.0 (en revisión con Eric), `flujo-spot.html`, `flujo-anclas.html` y `SHA256SUMS` | La fuente de todo; no se modifica |
| `2_corpus/` | Los textos de los originales (SQLite y JSONL) | El material del que salen las reglas |
| `3_taxonomia/` | La taxonomía canónica (`TAXONOMIA_CANONICA.md`), su precatalogación por encabezado y la taxonomía anterior 00688 | Los ejes con que se clasifica cada texto |
| `4_diseno/templates/` | Brief, contratos por operación y adaptadores por modelo | Lo que entra al sistema y lo que sale |
| `4_diseno/casos/` | Catálogo de 1,729 opciones de caso y su validador | Cómo se arma un caso |
| `4_diseno/` (raíz) | `jerarquia_de_lectura.md`, `niveles_de_generalidad.md` y la propuesta de aplicación y clasificación | El método |
| `4_diseno/copias_identicas/` | 3 copias idénticas de archivos de `4_diseno/templates/` | No se usan; esperan decisión |
| `4_diseno/validadores/` | Los 6 gates del paquete original, su `settings.json` y su `README.md`, sin activar como hooks | Restaurados por orden de Eric |
| `5_decisiones/` | Las decisiones de Eric por fecha y, en `directivas_20261021/`, sus directivas | Mandan sobre todo lo demás |
| `6_mapa/` | La memoria del agente; empieza en `6_mapa/CONSULTA.md` | Saber rápido qué existe y qué está decidido |
| `7_auditorias_y_verificaciones/` | Verificadores de templates y casos, sus resultados y las verificaciones del agente | Comprobar que lo demás está bien |
| `CAMBIOS.md` | Cada cambio al repo, con fecha, commit y orden | Saber qué cambió y por qué |
| `PENDIENTES.md` | Los pendientes por etapa y quién los resuelve | Qué falta |
| `CLAUDE.md` y `.claude/rules/DECISIONES.md` | Las instrucciones que el agente carga en cada sesión | Cómo trabaja el agente |

Verificación: `python3 4_diseno/casos/validar.py`, `python3 7_auditorias_y_verificaciones/templates/verificar_templates.py`, `python3 7_auditorias_y_verificaciones/templates/probar_contratos.py` y, desde `1_originales/`, `sha256sum -c SHA256SUMS`.
