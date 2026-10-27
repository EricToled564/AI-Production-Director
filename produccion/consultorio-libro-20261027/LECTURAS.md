# Registro de lecturas · consultorio-libro-20261027 (2026-10-27)

Todos los archivos leídos completos en este turno. Al lado de cada uno, la consecuencia para este caso.

| Archivo | Consecuencia |
|---|---|
| `produccion-visual-sw30/SKILL.md` (inyectado por el hook) | Pregunta de avance; cabecera SKILL/RIESGOS/TÉCNICA; armar por secciones con `template_engine.py`, auditar con `audit_gi2.py`, cerrar `rule_ledger.py`. La regla 1 y la regla 7 dan los tres pasos. La 2 quita «central horizontal band». La 8 congela el gesto. La 3 pide verbos operativos en el paso 1. La 4 exige adjuntar toda imagen citada. La 5 limita el texto a los deltas. La regla de ~250 palabras deja el techo en 300. |
| `ai-production-director/SKILL.md` (inyectado) | §6.4: el texto final lo decide `image`, así que van los cinco slots rotulados aunque `template_engine` una las secciones sin rótulo. §6.1: vocabulario prohibido. |
| `image/SKILL.md` (inyectado) | Orden de lectura obligatorio y formato de salida: Model/Quality/Size, Prompt, Notes y lista Preserve en la edición. |
| `image/references/golden-rules.md` (inyectado) | Empezar con verbo, el «Create» va dentro de Scene. Formulación positiva. Hex en colores. Referencias con rol. |
| `image/references/models.md` | GPT Image 2 por edición con preservación de identidad y por los cinco slots; hasta 16 referencias con rol. |
| `image/references/gpt-image.md` (líneas 1–190) | Cinco slots. Lista anti-slop. quality high para retratos y ediciones que tocan identidad (:45–47). Tamaños (:53–63). Edición Change/Preserve/Constraints, un cambio por iteración (:76–90). Varias imágenes indexadas con rol (:102–109). |
| `image/references/characters.md` | «Keep facial features exactly the same as Image N» (:14) como bloque idlock. |
| `image/references/creative-direction.md` | Términos descriptivos y no números de diafragma (:55–56); se usa «deep focus». Materiales concretos (:78). |
| `image/references/prompt-framework.md` | Micro-detalles de cinematic verbose (:208–219): se aplican poros y tejido (:213), sombra de contacto (:217) y el instante congelado (:219). El resto se hereda de Image 7. |
| `image/references/patterns/portrait-cinema.md` | Ninguno de sus cinco patrones es esta escena; no se usa plantilla. |
| `production-package/RULES_MATRIX.md` | Tipos: T5 para el paso 1, T3 para el paso 2 y T4 para el paso 3 (dos personas en cuadro, :13); secciones exigidas por tipo. |
| `production-package/template_engine.py` | Motor: secciones, bloques nombrados y metadatos fuera del cuerpo. Su autoprueba da 6/6. |
| `production-package/audit_gi2.py` | 15 columnas; identity_lock exige frase de identidad, lo que llevó a añadir el idlock. Su autoprueba pasa. |
| `.claude/hooks/gate_image.py`, `gate_microgate.py` | Requisitos de la entrega: cabecera de tres líneas con un archivo .md real, verbo al inicio o línea OVERRIDE de R1, modelo nombrado. |
| `.claude/hooks/rule_ledger.py` (cabecera y uso) | Disposición CHECK o NA por regla; sale con 1 si falta alguna. Prueba negativa: con una disposición menos sale con 1. |
| `reg_image.json`, `reg_produccion-visual-sw30.json` (206 enunciados) | Los 206 leídos uno por uno; disposiciones en `disposiciones.json`. |
