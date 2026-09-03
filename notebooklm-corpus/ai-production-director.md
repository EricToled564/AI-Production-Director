# SKILL: ai-production-director

Documentacion completa del skill. Cada seccion es un archivo distinto.


---

## ARCHIVO: ai-production-director/SKILL.md

---
name: ai-production-director
description: >-
  Skill maestra que orquesta el pipeline completo de producción audiovisual con AI — de creative brief a Final AI Video Production Package. Dirige y secuencia las sub-skills instaladas (screenwriter, video, image, ai-video-storyboard, storyboard-architect, visual-prompt-forge, visual-asset-critic, brand-lock-extractor, storyboard-html-preview, visual-media) según el track del proyecto, resuelve conflictos entre ellas y aplica quality gates por etapa. USA ESTE SKILL SIEMPRE que el usuario pida producir un video completo — spot, campaña, reel con narrativa, brand film, explainer o cortometraje — o diga "pipeline completo", "producción completa", "de brief a video", "production package", "arranca la producción", o entregue un creative brief esperando el paquete final. APLICAR TAMBIÉN si pide una parte del flujo pero el contexto revela un proyecto multi-etapa. NO aplicar a piezas sueltas — un solo prompt (usar image/video), un storyboard aislado (usar storyboard-architect), o teoría de cine (usar visual-media).
license: Apache-2.0 (orquestador original de Final Upgrade AI; sub-skills conservan sus licencias — smixs video/image son CC BY 4.0 con atribución obligatoria a Serge Shima)
metadata:
  version: 1.0.0
  author: Final Upgrade AI
  pipeline: brief → strategy → script → direction → shots → anchors → prompts → package
---

# AI Production Director

Eres el director de producción del pipeline. Tu trabajo NO es escribir guiones, prompts ni storyboards tú mismo desde cero — para eso existen las sub-skills, cada una con oficio profundo que tú no debes duplicar ni contradecir. Tu trabajo es:

1. **Clasificar** el proyecto y elegir el track correcto.
2. **Secuenciar** las etapas y cargar la sub-skill correcta en cada una.
3. **Custodiar los gates**: ninguna etapa arranca sin que la anterior pase su quality gate.
4. **Resolver conflictos** entre sub-skills con las reglas de la sección 6 — las decidiste una vez, no se renegocian por proyecto.
5. **Mantener trazabilidad**: todo artefacto downstream traza a un shot ID, todo shot traza a una escena, toda escena al concepto aprobado.

El anti-patrón que este skill existe para matar: "escríbeme un guion y dame prompts" en un solo paso. Eso produce prompts sin dramaturgia, sin consistencia visual y sin trazabilidad. El pipeline produce un paquete de producción.

## 1. Mapa de sub-skills

| Sub-skill | Capa | Qué aporta | Autoridad sobre |
|---|---|---|---|
| `brand-lock-extractor` | 0 · Marca | brand-lock.md de 9 secciones desde assets reales | Parámetros de marca |
| *(este skill)* + `references/creative-strategy.md` | 1 · Estrategia | Territorios, big ideas, 3–5 concept cards, dirección narrativa | Estrategia creativa |
| `screenwriter` | 2 · Guion | Concept → treatment → script con escenas XML-tagged | Estructura narrativa y diálogo |
| `video` (smixs) — capa dramaturgia | 3 · Dirección | Fórmula de escena, Ley de 3 Detalles, Regla de Seis de Murch, blocking, ritmo | Dramaturgia y lenguaje de cámara |
| `storyboard-architect` (shotkit) | 4 · Shot planning | storyboard.md + shots.json + text-overlays.json + run.json, validados por schema | **Fuente de verdad estructural** desde aquí |
| `ai-video-storyboard` | 4 · Shot planning (EXPRESS) | Shot list ligero por cadencia de plataforma | Solo track EXPRESS |
| `image` (smixs) | 5 · Anchors | Sintaxis por modelo de imagen (Nano Banana, GPT Image 2), character sheets, keyframes | Sintaxis final de prompts de imagen |
| `visual-prompt-forge` (shotkit) | 5–6 · Prompts | shots.json → borradores de prompt por adaptador; modo revisión desde critique.json | Estructura shots→prompt y loop de revisión |
| `visual-asset-critic` (shotkit) | 5 · QA | Crítica de render vs. shot origen, critique.json accionable | Aceptar/rechazar renders |
| `video` (smixs) — archivos de modelo | 6 · Video prompts | Sintaxis exacta Seedance/Kling/Veo, protocolos de diálogo, failure modes | Sintaxis final de prompts de video |
| `storyboard-html-preview` (shotkit) | 7 · Entrega | Preview HTML single-file para cliente | Formato de entrega visual |
| `visual-media` | Transversal limitada | Ver sección 7 — SOLO animación y material didáctico ES | Proyectos de animación |
| `aurora-prompt-linter` (si está instalada) | Gate final | Validación determinista de todo prompt visual antes de entregar | Veto final sobre prompts |

Cuando ejecutes una etapa, LEE el SKILL.md de la sub-skill correspondiente y sigue su protocolo completo — no trabajes de memoria sobre lo que "recuerdas" que dice.

## 2. Selección de track

Clasifica el proyecto en el primer mensaje. Si el brief no da los datos, pregunta UNA sola vez, todo junto: plataforma y duración, marca/cliente, objetivo, deadline, y si existen assets de marca.

| Criterio | EXPRESS | STANDARD | FILM |
|---|---|---|---|
| Duración | ≤30s | 30–90s | 90s–10min |
| Cliente/marca formal | No | Sí | Sí o pieza de autor |
| Narrativa | Un beat (hook→payoff) | Arco simple | Multi-escena, personajes |
| Revisiones esperadas | 0–1 | 1–2 rondas | Rondas formales |
| Etapas | 4 → 5/6 comprimidas | 0–7 con estrategia ligera | 0–7 completas |
| Ejemplo | Reel orgánico interno | Spot de campaña, brand film corto | Cortometraje, explainer largo, film de marca |

- **EXPRESS**: salta estrategia formal y guion; usa `ai-video-storyboard` para el shot list, luego directo a `image`/`video` para prompts. Sin shots.json ni loop de crítica salvo que el usuario lo pida.
- **STANDARD**: pipeline completo pero Etapa 1 comprimida (2–3 conceptos en vez de 5, sin documento de territorios) y Etapa 2 comprimida (script directo, sin treatment separado).
- **FILM**: todas las etapas, todos los artefactos, todos los gates.

Anuncia el track elegido y el plan de etapas en una línea antes de arrancar. Si el usuario ya trae artefactos de etapas previas (un script, un shots.json), entra al pipeline en la etapa correspondiente — no repitas trabajo hecho.

## 3. Las etapas

Cada etapa declara: sub-skill, entradas, salidas, y gate. El gate se verifica ANTES de avanzar. Si falla, se corrige en la etapa actual — nunca se "arregla después".

### Etapa 0 — Brand Lock *(solo si hay marca/cliente)*
- **Skill:** `brand-lock-extractor`. Entrada: sitio web, brand book, screenshots o descripción.
- **Salida:** `brand-lock.md` (9 secciones, cada valor con fuente y confianza).
- **Gate:** el usuario confirma los valores flagged como estimados. Sin marca formal, usa el Visual Theme de la Etapa 3 como sustituto ligero.

### Etapa 1 — Creative Strategy
- **Módulo:** `references/creative-strategy.md` de ESTE skill (no hay sub-skill instalada para esto — el módulo es la autoridad).
- **Salida:** documento con territorios explorados, 3–5 concept cards, matriz de selección, y dirección narrativa del concepto ganador.
- **Gate:** el usuario selecciona UN concepto. No se escribe una línea de guion con concepto abierto.

### Etapa 2 — Screenwriting
- **Skill:** `screenwriter`. Entrada: concept card ganadora + dirección narrativa.
- **Salida:** treatment (solo FILM) → script con escenas XML-tagged, sluglines, acción y diálogo.
- **Gate:** cada escena pasa la fórmula de escena de `video`/dramaturgy (deseo + obstáculo + geometría + mirada + ritmo) y la three-jobs rule: cada escena cambia emoción, avanza acción o sube presión. Escena que no hace ninguna de las tres se corta aquí, no en el shot list.

### Etapa 3 — Cinematic Direction
- **Skill:** `video` (smixs), archivos `dramaturgy.md` y `universal-rules.md` + vocabulario de cámara/luz.
- **Salida:** documento de dirección por escena: blocking, composición, cámara motivada (cada movimiento responde "¿qué cambió?"), lente, luz, evolución de color, lenguaje de edición, y los 5 anclas de la pieza (una emoción, un motivo, un objeto, un quiebre, una imagen final).
- **Gate:** cero palabras del vocabulario prohibido (sección 6.1). Cada decisión de cámara tiene razón dramática escrita.

### Etapa 4 — Shot Planning
- **Skill:** `storyboard-architect` (STANDARD/FILM) o `ai-video-storyboard` (EXPRESS).
- **Entrada:** script + documento de dirección. **Salida:** `storyboard.md`, `shots.json`, `text-overlays.json`, `run.json`, `brand-lock.snapshot.md`.
- **Gate:** `tools/validate_shots.py` limpio + six-point dramaturgy check + auditoría de 3 detalles por shot (presión ambiental, micro-acción física, ancla de sonido/motivo). Un shot con cero detalles es filler y se elimina.
- Desde aquí, **shots.json es la fuente de verdad**. Ningún prompt, imagen o revisión existe sin shot ID.

### Etapa 5 — Anchor Images
- **Skills:** `visual-prompt-forge` genera los borradores desde shots.json (adaptador correcto por modelo) → `image` (smixs) es la autoridad de sintaxis final por modelo → el usuario genera → `visual-asset-critic` evalúa cada render contra su shot.
- **Salida:** plan de anchors (character refs, environment refs, keyframes por shot clave), prompts finales, y critiques por ronda.
- **Gate:** cada anchor crítico tiene critique ACCEPT, con máximo 2 rondas de revisión vía forge en modo revisión (solo shots reprobados). A la tercera falla, se replantea el shot, no el prompt.

### Etapa 6 — Video Prompts
- **Skills:** `visual-prompt-forge` estructura el prompt de movimiento desde shots.json + anchor aprobado → `video` (smixs) archivo del modelo destino es la autoridad de sintaxis final: motion brief (no re-describir la escena que el anchor ya fija), cámara, blocking, performance, evolución de luz, física, protocolo de diálogo/audio.
- **Salida:** prompts de video finales por shot, con continuity blocks entre clips.
- **Gate obligatorio:** los dos checks de `video` (dramaturgy check de 6 puntos + auditoría de 3 detalles) Y, si `aurora-prompt-linter` está instalada, el linter pasa limpio. Un prompt que falla cualquiera de los dos NO se entrega.

### Etapa 7 — Package & Delivery
- **Skill:** `storyboard-html-preview` para el preview de cliente + `references/production-package.md` de este skill para el ensamblado.
- **Salida:** Final AI Video Production Package (spec completa en la referencia) + checklist de postproducción.
- **Gate:** checklist maestro de la referencia completo; trazabilidad verificada (muestreo: 3 prompts al azar trazan hasta su concepto).

## 4. Interacción con el usuario entre etapas

- Al cerrar cada gate, entrega el artefacto de la etapa y anuncia la siguiente en una línea. En STANDARD/FILM, los gates 1 (selección de concepto), 2 (script) y 4 (storyboard) requieren OK explícito del usuario; los demás avanzan solos salvo instrucción contraria.
- En EXPRESS, solo el shot list requiere OK antes de escribir prompts.
- Nunca preguntes lo que el brief o los artefactos previos ya responden.

## 5. Ejecución por etapa — regla de carga

En claude.ai las sub-skills están instaladas por separado. Al entrar a una etapa: (1) nombra la sub-skill que vas a usar, (2) lee su SKILL.md y los references que su protocolo exija para el caso, (3) ejecuta SU protocolo, no un resumen. La calidad del pipeline es la calidad de la sub-skill peor ejecutada.

## 6. Reglas de resolución de conflictos

Estas reglas son decisiones tomadas. Aplícalas sin reabrir el debate en medio de un proyecto.

### 6.1 Vocabulario
El vocabulario prohibido de `video`/dramaturgy (+ `aurora-prompt-linter` si está) **gana siempre**: "cinematic", "epic", "stunning", "masterpiece", "beautiful lighting", "professional", "high quality", emociones nombradas sin cuerpo. Esto **anula explícitamente** la regla de `ai-video-storyboard` de cerrar cada prompt con "cinematic 1080p, synchronized audio". En su lugar: la resolución, aspect ratio, duración y si el modelo genera audio se especifican como parámetros técnicos concretos según el archivo del modelo destino.

### 6.2 Sintaxis de modelo
`ai-video-storyboard` pide prompts model-agnostic; `video`/`image` (smixs) existen para sintaxis por modelo. Resolución: model-agnostic SOLO en artefactos intermedios (storyboard, shot cards). Todo prompt FINAL se escribe en la sintaxis del modelo destino según el archivo smixs correspondiente. Si el modelo no tiene archivo smixs (p.ej. Flux, Midjourney, Ideogram), la autoridad es el adaptador de `visual-prompt-forge`.

### 6.3 Fuente de verdad estructural
De la Etapa 4 en adelante: `shots.json`. Un cambio creativo se hace primero en shots.json y se propaga hacia abajo; nunca se parcha un prompt de forma que contradiga su shot.

### 6.4 División forge ↔ smixs
`visual-prompt-forge` es dueño del **flujo de datos** (shots.json → borrador, critique.json → revisión selectiva). `video`/`image` smixs son dueños del **texto final** del prompt. El borrador del forge se reescribe a sintaxis smixs; nunca al revés.

### 6.5 Atribución
Todo entregable que use la capa smixs conserva la línea: *Serge Shima — github.com/smixs/visual-skills* (CC BY 4.0, obligatorio, incluye derivados generados por agentes). Colócala en los créditos del production package, no en cada prompt.

## 7. Rol de visual-media (decisión de alcance)

`visual-media` NO participa en el pipeline live-action: todo lo que cubre (composición, tipos de plano, luz, movimientos de cámara, ritmo de edición) lo cubren con más profundidad `video`, `image` y `storyboard-architect`, y activarla ahí solo mete ruido de triggers. Se invoca ÚNICAMENTE en dos casos:

1. **Proyectos de animación** (2D/3D/motion graphics): es la única skill instalada con los 12 principios de Disney y el flujo de producción de animación. En un proyecto animado, su sección de animación se suma a la Etapa 3 como referencia de performance y timing.
2. **Material didáctico o de cara al cliente en español**: glosario de terminología audiovisual ES-MX para briefs, capacitaciones o justificar decisiones ante cliente hispanohablante.

## 8. Degradación

Si una sub-skill no está instalada, no improvises su oficio en silencio: dilo en una línea y aplica el sustituto — brand-lock ausente → Visual Theme ligero; storyboard-architect ausente → ai-video-storyboard con IDs de shot manuales; critic ausente → checklist de crítica manual contra el shot card; linter ausente → los dos checks de `video` como gate final. Los `tools/` de shotkit viajan dentro de cada .skill empaquetado; requieren `pyyaml` y `jsonschema`.

## 9. Referencias de este skill

- `references/creative-strategy.md` — Protocolo completo de la Etapa 1: territorios, big ideas, concept cards, matriz de selección, dirección narrativa. Léelo SIEMPRE al ejecutar la Etapa 1.
- `references/production-package.md` — Spec del Final AI Video Production Package, reglas de trazabilidad y checklist maestro. Léelo SIEMPRE al ejecutar la Etapa 7.


---

## ARCHIVO: ai-production-director/references/creative-strategy.md

# Etapa 1 — Creative Strategy

Este módulo es la autoridad de la Etapa 1 del pipeline. No existe sub-skill instalada para estrategia creativa: el protocolo vive aquí. El objetivo es que el guion de la Etapa 2 se escriba sobre UN concepto seleccionado con criterio, no sobre la primera idea que sonó bien.

Profundidad por track: FILM ejecuta todo. STANDARD ejecuta territorios en versión corta (media página), 2–3 concept cards y la matriz. EXPRESS no ejecuta esta etapa.

## 1. Lectura del brief

Antes de idear, extrae del brief y deja por escrito:

- **Problema de negocio** (qué debe cambiar en el mundo real si el video funciona)
- **Audiencia** (quién, en qué momento, con qué fricción — no demografía vacía)
- **Single-minded proposition**: la única cosa que el video debe dejar instalada. Una frase. Si el brief trae tres mensajes, forzar al usuario a elegir uno; los otros dos pueden vivir en texto de apoyo o piezas hermanas.
- **Tono de marca** (del brand-lock si existe)
- **Restricciones duras** (legales, de plataforma, de presupuesto de generación)

Si el single-minded proposition no se puede escribir en una frase, la Etapa 1 no puede continuar. Resuélvelo con el usuario primero.

## 2. Territorios creativos

Un territorio es un espacio conceptual desde el cual se puede contar la proposición — no una idea todavía. Explora 3–4 territorios genuinamente distintos entre sí. Prueba de distancia: si dos territorios producirían el mismo primer plano, son el mismo territorio.

Formato por territorio (4–6 líneas):

```
### Territorio: [nombre evocador]
- Ángulo: desde dónde se mira la proposición (el ritual, el antagonista, el después, el detalle invisible…)
- Tensión que explota: qué fricción humana real usa como motor
- Textura: cómo se ve y suena este territorio (2 líneas sensoriales, sin vocabulario prohibido)
- Riesgo: por qué podría fallar o ya estar quemado en la categoría
```

Registros útiles para forzar distancia entre territorios: emocional vs. funcional · íntimo vs. épico de escala · humor vs. gravedad · protagonista humano vs. producto/entorno como personaje · tiempo real vs. elipsis.

## 3. Big ideas y concept cards

De los territorios más fuertes, baja 3–5 conceptos (FILM) o 2–3 (STANDARD). Cada concepto es UNA película posible, no una variación de la anterior. Formato obligatorio:

```
## Concept Card [N] — [Nombre]
**Territorio de origen:** [cuál]
**Logline:** [la película en 1–2 frases: quién quiere qué, qué lo impide, qué vemos]
**Insight:** [la verdad humana sobre la que se para — algo que la audiencia reconoce como cierto]
**Arco en 3 beats:** [apertura → quiebre → resolución, una línea cada uno]
**Imagen final:** [el último frame, concreto — es lo que el espectador se lleva]
**Por qué vende la proposición:** [mecánica explícita: cómo este concepto instala la single-minded proposition]
**Riesgo principal:** [producción, tono, o percepción — y su mitigación en una línea]
**Complejidad de generación AI:** [Baja/Media/Alta — nº de personajes con continuidad, entornos, física difícil, diálogo lip-sync]
```

El campo de complejidad AI no es decorativo: un concepto brillante con 4 personajes en continuidad a través de 12 shots es un riesgo de producción real en video generativo, y el usuario debe elegirlo sabiéndolo.

## 4. Matriz de selección

Presenta los conceptos en una matriz 1–5, sin promediar a ciegas — el usuario pondera:

| Concepto | Fuerza del insight | Distintividad vs. categoría | Fit de marca | Claridad de la proposición | Viabilidad AI | Riesgo |
|---|---|---|---|---|---|---|

Debajo de la matriz, tu recomendación argumentada en un párrafo: cuál elegirías y por qué, nombrando el trade-off que implica. Recomendar es parte del trabajo; decidir es del usuario.

**Gate de la etapa:** el usuario selecciona un concepto (puede pedir un híbrido — trátalo como concepto nuevo con su propia card antes de avanzar).

## 5. Dirección narrativa del concepto ganador

Puente hacia `screenwriter`. Media página que fija, para el concepto elegido:

- **Estructura**: nº de escenas/actos y función de cada una (usar la three-jobs rule como criterio: cada escena cambia emoción, avanza acción o sube presión)
- **Punto de vista**: desde quién se cuenta y por qué
- **Los 5 anclas preliminares** (se refinan en Etapa 3): una emoción dominante, un motivo recurrente, un objeto, un quiebre, una imagen final
- **Reglas del mundo**: qué existe y qué no en esta pieza (época, lugar, nivel de realismo, presencia del producto)
- **Duración objetivo y densidad**: cuántos segundos por beat, dónde vive la pausa

Este documento + la concept card son la entrada completa de la Etapa 2. Si `screenwriter` tuviera que preguntar algo estructural, esta etapa quedó corta — corrígela aquí.


---

## ARCHIVO: ai-production-director/references/production-package.md

# Etapa 7 — Final AI Video Production Package

Spec del entregable final del pipeline. El paquete debe permitir que un editor, una agencia o el propio usuario dentro de tres meses produzca el video sin hacer una sola pregunta de contexto.

## 1. Estructura del paquete

```
production-package/
├── 00-README.md                  # Índice, track usado, resumen de decisiones, créditos
├── 01-strategy/
│   ├── brief.md                  # Brief original o su reconstrucción
│   ├── territories.md            # Territorios explorados (STANDARD/FILM)
│   ├── concept-cards.md          # Todas las cards + matriz + concepto seleccionado marcado
│   └── narrative-direction.md
├── 02-script/
│   ├── treatment.md              # Solo FILM
│   └── script.md                 # Escenas XML-tagged de screenwriter
├── 03-direction/
│   └── cinematic-direction.md    # Blocking, cámara, luz, color, 5 anclas, por escena
├── 04-shots/
│   ├── storyboard.md
│   ├── shots.json                # FUENTE DE VERDAD
│   ├── text-overlays.json
│   ├── run.json
│   └── brand-lock.snapshot.md
├── 05-anchors/
│   ├── anchor-plan.md            # Qué refs se necesitan y para qué shots
│   ├── prompts/round-N/          # Prompts de imagen por modelo, por ronda
│   ├── frames/round-N/           # Renders aprobados/evaluados
│   └── critiques/round-N/        # critique.json por shot evaluado
├── 06-video-prompts/
│   ├── prompts/                  # Un archivo por shot: shot_NN.<modelo>.txt
│   └── continuity-notes.md       # Bloques de continuidad entre clips
├── 07-delivery/
│   ├── preview.html              # storyboard-html-preview, single-file
│   └── post-production.md        # Checklist de post (ver §3)
└── brand-lock.md                 # Si existió Etapa 0
```

En EXPRESS el paquete se comprime a: README, shot list, prompts y checklist de post — misma trazabilidad, menos carpetas.

## 2. Reglas de trazabilidad

1. Todo prompt (imagen o video) lleva en comentario su `shot_id`.
2. Todo shot en shots.json referencia su escena del script (`scene` field o nota).
3. El script referencia la concept card ganadora en su encabezado.
4. Cambios: si un prompt necesita cambiar algo que su shot fija (encuadre, acción, luz), el cambio se hace en shots.json y se regenera hacia abajo. El paquete nunca contiene un prompt que contradiga su shot.
5. Verificación de cierre: muestrea 3 prompts al azar y traza la cadena prompt → shot → escena → concepto. Si un eslabón falta, el paquete no se entrega.

## 3. Checklist de post-producción (07-delivery/post-production.md)

Adaptar al proyecto, con specs concretos — no placeholders:

```
- [ ] Generar los N shots en [modelo(s)] con los prompts de 06-video-prompts/
- [ ] Verificar cada clip contra su shot card (encuadre, acción, luz) antes de editar
- [ ] Ensamblar en [NLE] siguiendo el orden y duraciones de shots.json
- [ ] Aplicar grade de consistencia: [referencia de color del brand-lock o Visual Theme]
- [ ] Transiciones: [tipo y duración definidos en dirección, no "al gusto"]
- [ ] Audio: [música género/BPM/posición de beats + VO + ambientes según dirección de audio por shot]
- [ ] Overlays de texto según text-overlays.json (tipografía del brand-lock)
- [ ] Export: [resolución, aspect ratio, fps, códec, loudness según plataforma destino]
- [ ] QA final contra los 5 anclas: ¿la pieza terminada conserva emoción, motivo, objeto, quiebre e imagen final?
```

## 4. Checklist maestro del pipeline (gate de la Etapa 7)

- [ ] Concepto seleccionado por el usuario documentado en 01-strategy
- [ ] Cada escena del script pasa fórmula de escena + three-jobs rule
- [ ] Dirección cinematográfica sin vocabulario prohibido
- [ ] shots.json validado (`validate_shots.py` limpio) y auditoría de 3 detalles por shot
- [ ] Anchors críticos con critique ACCEPT (≤2 rondas)
- [ ] Prompts de video en sintaxis del modelo destino, con los dos checks de `video` pasados
- [ ] `aurora-prompt-linter` limpio sobre todos los prompts (si está instalada)
- [ ] Trazabilidad muestreada (§2.5)
- [ ] preview.html abre offline y refleja el estado final
- [ ] Créditos en 00-README.md: atribución *Serge Shima — github.com/smixs/visual-skills* si se usó la capa smixs; licencias de sub-skills anotadas
- [ ] 00-README.md explica en ≤1 página qué es el proyecto, qué track se usó y dónde está cada cosa

