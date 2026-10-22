# INSTRUCCIONES DE EJECUCIÓN — PILOTO V5 CON PRUEBA A/B DE IMAGEN

Fecha: 19 de octubre de 2026. Autor de la instrucción: Eric Toledano.
Este mensaje es una aprobación explícita y acotada. No es aprobación por silencio ni aprobación del plan completo.

## 0. Qué se aprueba y qué no

1. Se aprueba ÚNICAMENTE el piloto del §10 de `PLAN_V5_COMPLETO_TAXONOMIA_TEMPLATES_20261019_054300.md`, con las modificaciones de este documento. Donde este documento y el plan difieran, manda este documento.
2. NO se aprueba H-25, H-60, H-100 ni ninguna ampliación a otros bloques. Ampliar requiere un mensaje nuevo de Eric después de ver el resultado de la §8.
3. NO se aprueba canonizar nada. El piloto produce evidencia, no catálogo vigente.
4. Siguen vigentes sin cambios: la taxonomía consolidada, las decisiones aplicables, la exclusión de Aurora, la prohibición de estados de diferimiento (NO APLICA, NO DETERMINADO, PENDIENTE, DESCONOCIDO, EN PROCESO y equivalentes), la prohibición de la palabra «photorealistic» en prompts y la regla de que el silencio no aprueba.

## 1. Por qué existe este piloto (objetivo que debe medir)

El objetivo del proyecto (§1.1 del plan) es obtener prompts que produzcan imágenes de apariencia fotográfica y alta calidad al primer intento o con el mínimo de iteraciones.

La hipótesis central del plan es: «clasificar exhaustivamente las reglas y conectarlas con templates produce mejores prompts». Esa hipótesis no está probada. En dos pruebas anteriores, una auditoría con alto cumplimiento de reglas (264/281) produjo una imagen rechazada, y una base de reglas existente no evitó prompts defectuosos.

Por eso el piloto tiene dos salidas obligatorias y ninguna sustituye a la otra:

- **Salida 1 (método):** el piloto del §10 del plan, ejecutado con su rigor completo sobre un bloque pequeño.
- **Salida 2 (objetivo):** una comparación A/B a ciegas con imágenes reales. Sin la Salida 2, el piloto NO se considera cerrado aunque todas las pruebas estructurales pasen. Esto sustituye, solo para el piloto, la frase del §22 «No se exige una evaluación visual real durante la fase documental».

## 2. Parámetros fijos del piloto

| Parámetro | Valor |
|---|---|
| Modelo (F29) | GPT Image 2 |
| Contrato de salida | `GPT2-GEN` de `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019.md`: cinco slots Scene / Subject / Important Details / Use Case / Constraints, en ese orden (fuente `image/references/gpt-image.md`) |
| Operación (F10) | Génesis sin referencias (`T-GENESIS`) |
| Flujo (P-01) | El que corresponda según la taxonomía a un activo de imagen independiente generado por génesis. Determinarlo leyendo la taxonomía y registrarlo con su evidencia; no preguntarlo a Eric salvo que la taxonomía no lo resuelva. |
| Tipo de pieza (F04) | Retrato |
| Sujeto (F15) / número (F19) | Persona / una |
| Identidad (F20) | No se exige reconocer a una persona real |
| Referencias (F23) | Ninguna |
| Generación de imágenes | La hace Eric. El sistema no genera imágenes por su cuenta. |

## 3. Entradas autorizadas (verificar identidad antes de empezar)

| Archivo | Comprobación |
|---|---|
| `TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md` | SHA-256 `7ec912aa92d8d1a6f54a6158550c0bcfa48861a05bbf6f6146b5b93b1f9bfeaa` |
| `BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite` (tabla `textos`) | SHA-256 `c991437028d9d731bf46e516efa315f08d9da71bd596495c119fa41d30f6c8d9`; 13.005 filas |
| `BASE_TEXTOS_ORIGINALES_13005_20261019_055700.csv` | SHA-256 `a2c5a59d3531512058d8bfc6f1446fd45942a49ea40b25c6b179febd5608a1cc` |
| Paquete `TEMPLATES_REVISADOS_IMAGEN_ORQUESTACION_20261019` | Hashes de su `MANIFIESTO.json` |
| Paquete `CASOS_OPCIONES_TAXONOMIA_20261019` | `validar.py` debe pasar antes de empezar |
| `PLAN_V5_COMPLETO_TAXONOMIA_TEMPLATES_20261019_054300.md` | Procedimiento, salvo lo modificado aquí |

Si un hash no coincide, detenerse y reportar. No continuar con otra versión.

## 4. Bloque del piloto

### 4.1 Documentos que entran completos

Se clasifican TODAS las unidades de estos documentos (sin filtrar por señal léxica):

1. `skills/image/SKILL.md`
2. `skills/image/references/gpt-image.md`
3. `skills/image/references/golden-rules.md`
4. `skills/image/references/prompt-framework.md`
5. `skills/image/references/patterns/portrait-cinema.md`
6. `skills/image/references/creative-direction.md`
7. `skills/image/references/characters.md`
8. `skills/image/references/models.md`
9. `skills/visual-prompt-forge/SKILL.md`
10. `skills/visual-prompt-forge/adapters/gpt-image.md`
11. `skills/visual-prompt-forge/adapters/_capabilities.json`
12. `skills/visual-prompt-forge/references/prompt-anatomy.md`
13. `skills/visual-prompt-forge/references/failure-modes.md`
14. `skills/ai-production-director/SKILL.md`
15. `skills/visual-asset-critic/SKILL.md`
16. `skills/visual-asset-critic/references/critique-rubric.md`

### 4.2 Sección que entra de un documento parcial

- `flujos/flujo-spot.html`: la sección completa del subflujo atómico de génesis (la que la taxonomía describe en «FL02 — Nivel 4 · subflujo atómico de génesis»), con todos sus encabezados y contexto. Es el recorrido de orquestación aplicable a imagen que exige el §10.

### 4.3 Antes de clasificar

1. Reportar el número exacto de unidades del bloque y su distribución por documento y por tipo de unidad.
2. Declarar como limitación del piloto que puede haber reglas aplicables a este caso en documentos fuera del bloque. El piloto mide el método y la hipótesis; no certifica exhaustividad del corpus.
3. No añadir ni quitar documentos sin un mensaje de Eric.

## 5. Briefs del piloto (escenarios de la prueba A/B)

Estos cinco briefs son a la vez los escenarios de extremo a extremo del piloto. Son propuesta: **Eric debe aprobarlos o editarlos con un mensaje explícito antes de que el revisor congele las referencias independientes.** Sin esa aprobación no se empieza la Ronda 3.

| # | Brief | Uso | Formato |
|---|---|---|---|
| B1 | Pescadora de unos 60 años en un muelle al amanecer, sol bajo lateral, piel curtida, plano medio corto, mirada fuera de cámara | Portada de reportaje | 4:5 vertical |
| B2 | Ejecutivo de unos 40 años en una oficina con ventanal, luz suave de ventana, plano medio, mirando a cámara | Página «equipo» de un sitio web corporativo | 3:2 horizontal |
| B3 | Atleta de unos 25 años justo después de entrenar en un gimnasio, sudor visible, luz dura cenital del gimnasio, primer plano | Campaña de un club deportivo | 4:5 vertical |
| B4 | Mujer de unos 30 años en una cocina doméstica de noche, una lámpara cálida como única fuente, sostiene una taza con ambas manos visibles, plano medio | Ilustración de artículo de estilo de vida | 3:2 horizontal |
| B5 | Músico de unos 70 años de perfil, contraluz de escenario, ángulo bajo, fondo oscuro | Póster de concierto (sin texto en la imagen) | 2:3 vertical |

Cada brief se completa con `T-BRIEF-IMG` (todos los campos que su ruta exija, con origen por campo). Las inferencias del sistema se presentan aparte y Eric las aprueba antes de compilar. La aprobación se liga al hash del brief; cualquier cambio la invalida.

## 6. Procedimiento de la Salida 1 (método V5 sobre el bloque)

Se aplica el plan V5 completo, en este orden, sobre el bloque de la §4:

1. Preparación mínima del §9 para el bloque: contrato de interpretación con matriz trazada, pares mínimos, alarmas, canarios con procedencia y referencias independientes de los cinco briefs. El revisor construye desde las fuentes, sin ver la clasificación, qué reglas y efectos espera para cada brief, y las congela con hash antes de la Ronda 3.
2. Un agente propietario del bloque. Texto por texto, en orden, las cuatro rondas lógicas (§11, §12, §13, §15) completas para cada texto antes del siguiente, con la matriz de revisión de TODOS los ítems de la taxonomía vigente (§1.12 de la taxonomía).
3. Revisor B independiente, adversario y tercera lectura sellada del 10 %, como dice el plan.
4. Adjudicación (§14) y registro de incidencias. Consultas a Eric solo si la fuente y las decisiones no resuelven, agrupadas por clase y con el formato del Anexo D.
5. Vinculación regla → efecto → destino de template (§15 y §16) para todas las aplicaciones del bloque.
6. Compilación del prompt A de cada brief: selección de reglas aplicables, comprobación de compatibilidad, compactación sin pérdida y salida `GPT2-GEN` con parámetros separados y traza completa.
7. Comparación de lo seleccionado por el sistema con las referencias congeladas: faltantes, sobrantes, diagnóstico y reejecución de cada diferencia.

## 7. Procedimiento de la Salida 2 (prueba A/B a ciegas)

### 7.1 Prompt B (línea base)

- Lo escribe un agente separado que NO tiene acceso al catálogo, a la clasificación, a la matriz ni a los prompts A.
- Solo recibe: el brief aprobado y estos archivos originales: `skills/image/SKILL.md`, `skills/image/references/gpt-image.md`, `skills/image/references/golden-rules.md`, `skills/image/references/patterns/portrait-cinema.md`.
- Mismo modelo, mismo contrato de cinco slots, mismas prohibiciones de vocabulario y mismo formato que A.

### 7.2 Cegado

1. Para cada brief, asignar al azar las etiquetas X e Y a los prompts A y B.
2. Guardar la correspondencia en un archivo sellado y mostrar a Eric solo su SHA-256 antes de que genere.
3. Entregar a Eric, por brief: brief aprobado, prompt X, prompt Y y parámetros de generación idénticos para ambos (`quality: high`; tamaño o ratio según el brief).
4. No revelar cuál es A hasta que Eric entregue todas sus calificaciones.

### 7.3 Generación (la hace Eric)

- Dos generaciones por prompt, con el prompt exacto y sin editarlo: 5 briefs × 2 prompts × 2 generaciones = 20 imágenes.
- Cada imagen se registra con su brief, etiqueta y número de generación.

### 7.4 Calificación (la hace Eric, por imagen)

| Criterio | Escala |
|---|---|
| Apariencia fotográfica | 1–10 |
| Fidelidad al brief | 1–10 |
| Defectos visibles (manos, rostro, piel plástica, luz incoherente, anatomía) | lista |
| ¿Usable sin regenerar ni retocar? | sí / no |
| Preferencia por brief | X / Y / empate |

## 8. Criterio de decisión (registrado antes de generar; no se cambia después)

| Resultado | Decisión |
|---|---|
| A preferido en 4 o 5 de 5 briefs Y A tiene igual o más imágenes «usables» que B | La hipótesis se sostiene en este caso. Se entrega el informe y Eric decide si amplía. |
| A preferido en 3 de 5 | No concluyente. Se propone ampliar a 5 briefs más del mismo caso antes de cualquier otra decisión. |
| A preferido en 2 o menos | La hipótesis no se sostiene en este caso. Se detiene el trabajo de clasificación, se diagnostica la causa (selección, compilación, contrato o modelo) y se replantea con Eric antes de gastar más. |

Un resultado favorable en este caso no se extrapola a grupos, producto, anclas ni otros modelos.

## 9. Presupuesto y control de costo

1. **Eric fija el tope del piloto (tiempo y costo) antes de la Ronda 1. Sin ese número no se empieza.**
2. Tras los primeros 10 textos clasificados completos, reportar el costo y el tiempo reales por texto y proyectar el total del bloque.
3. Si la proyección supera el tope, detenerse y presentar el dato real y alternativas. No continuar por inercia.
4. Registrar por separado: lectura semántica nueva, revisión B, adversario, tercera lectura, adjudicación y comprobaciones mecánicas.

## 10. Entregables del piloto (nombres nuevos con fecha y hora)

1. Inventario del bloque con conteos (§4.3).
2. Contrato de interpretación y matriz trazada del bloque.
3. Las cuatro rondas por texto, la matriz de revisión de todos los ítems y los certificados A/B.
4. Registro de adjudicación e incidencias.
5. Mapa regla → efecto → destino del bloque, con IDs reales.
6. Por brief: brief aprobado, referencia independiente congelada, selección del sistema, diferencias y su resolución, prompt A con traza, prompt B y archivo sellado X/Y.
7. Tabla de calificaciones de Eric, revelación de X/Y y aplicación literal del criterio de la §8.
8. Informe de costo real contra el tope.
9. Informe final que diga en una línea si la hipótesis se sostuvo, no se sostuvo o quedó sin concluir, con la evidencia. Nada se declara canónico.

## 11. Condiciones de parada inmediata

Detenerse y reportar a Eric si ocurre cualquiera de estas:

- un hash de entrada no coincide;
- la proyección de costo supera el tope;
- una decisión de política genuina bloquea el bloque (formato del Anexo D);
- un canario falla y su corrección cambia el método;
- falta la aprobación de los briefs o de las inferencias de un brief.
