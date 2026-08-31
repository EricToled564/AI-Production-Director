# Reglas del skill: ai-production-director

25 enunciados normativos extraidos mecanicamente.
El id entre corchetes es la referencia obligatoria para clasificar.


## ai-production-director/SKILL.md

- [1f8ed1aa2f82] **Clasificar** el proyecto y elegir el track correcto.
- [976919fb7afd] **Secuenciar** las etapas y cargar la sub-skill correcta en cada una.
- [8a2a24e72003] **Custodiar los gates**: ninguna etapa arranca sin que la anterior pase su quality gate.
- [c83679230b88] **Resolver conflictos** entre sub-skills con las reglas de la sección 6 — las decidiste una vez, no se renegocian por proyecto.
- [2c2da899a44d] **Mantener trazabilidad**: todo artefacto downstream traza a un shot ID, todo shot traza a una escena, toda escena al concepto aprobado.
- [4ca2dc8c76f1] Cada etapa declara: sub-skill, entradas, salidas, y gate. El gate se verifica ANTES de avanzar. Si falla, se corrige en la etapa actual — nunca se "arregla después".
- [36dd5696e226] **Gate:** el usuario selecciona UN concepto. No se escribe una línea de guion con concepto abierto.
- [043b9dc0b02e] **Gate:** cero palabras del vocabulario prohibido (sección 6.1). Cada decisión de cámara tiene razón dramática escrita.
- [3fb8782f57b8] **Gate obligatorio:** los dos checks de `video` (dramaturgy check de 6 puntos + auditoría de 3 detalles) Y, si `aurora-prompt-linter` está instalada, el linter pasa limpio. Un prompt que falla cualquiera de los dos NO se entrega.
- [5673820bc473] Nunca preguntes lo que el brief o los artefactos previos ya responden.
- [f556f97c9939] El vocabulario prohibido de `video`/dramaturgy (+ `aurora-prompt-linter` si está) **gana siempre**: "cinematic", "epic", "stunning", "masterpiece", "beautiful lighting", "professional", "high quality", emociones nombradas sin cuerpo. Esto **anula explícitamente** la regla de `ai-video-storyboard` de cerrar cada prompt con "cinematic 1080p, synchronized audio". En su lugar: la resolución, aspect ra
- [4c5ba2b2ce9e] De la Etapa 4 en adelante: `shots.json`. Un cambio creativo se hace primero en shots.json y se propaga hacia abajo; nunca se parcha un prompt de forma que contradiga su shot.
- [1cf2b2af3609] `visual-prompt-forge` es dueño del **flujo de datos** (shots.json → borrador, critique.json → revisión selectiva). `video`/`image` smixs son dueños del **texto final** del prompt. El borrador del forge se reescribe a sintaxis smixs; nunca al revés.
- [b2a93a3b39b9] **Proyectos de animación** (2D/3D/motion graphics): es la única skill instalada con los 12 principios de Disney y el flujo de producción de animación. En un proyecto animado, su sección de animación se suma a la Etapa 3 como referencia de performance y timing.
- [036eba29584d] **Material didáctico o de cara al cliente en español**: glosario de terminología audiovisual ES-MX para briefs, capacitaciones o justificar decisiones ante cliente hispanohablante.
- [201666abd399] `references/creative-strategy.md` — Protocolo completo de la Etapa 1: territorios, big ideas, concept cards, matriz de selección, dirección narrativa. Léelo SIEMPRE al ejecutar la Etapa 1.
- [0574ba956e73] `references/production-package.md` — Spec del Final AI Video Production Package, reglas de trazabilidad y checklist maestro. Léelo SIEMPRE al ejecutar la Etapa 7.

## ai-production-director/references/creative-strategy.md

- [476511682f20] Si el single-minded proposition no se puede escribir en una frase, la Etapa 1 no puede continuar. Resuélvelo con el usuario primero.
- [240748ade236] De los territorios más fuertes, baja 3–5 conceptos (FILM) o 2–3 (STANDARD). Cada concepto es UNA película posible, no una variación de la anterior. Formato obligatorio:

## ai-production-director/references/production-package.md

- [eee77c7d576a] Todo prompt (imagen o video) lleva en comentario su `shot_id`.
- [f999ef3808aa] Todo shot en shots.json referencia su escena del script (`scene` field o nota).
- [8c97f2430a2a] El script referencia la concept card ganadora en su encabezado.
- [ed8f12484923] Cambios: si un prompt necesita cambiar algo que su shot fija (encuadre, acción, luz), el cambio se hace en shots.json y se regenera hacia abajo. El paquete nunca contiene un prompt que contradiga su shot.
- [69545d03256e] Verificación de cierre: muestrea 3 prompts al azar y traza la cadena prompt → shot → escena → concepto. Si un eslabón falta, el paquete no se entrega.
- [9848dbda5e26] [ ] Dirección cinematográfica sin vocabulario prohibido