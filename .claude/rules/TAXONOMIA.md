# Taxonomía de catalogación de reglas y sintaxis

Aprobada y canonizada por Eric Toledano el 2026-09-28 (decisión 10 de `DECISIONES.md`). Se revisa solo si al
vectorizar aparece una regla que no encaja en ningún valor, o un valor que queda sin reglas asignadas.

Los valores de la faceta 5 marcados "propuesto" no tienen fuente en los skills; salen de los sectores de los
proyectos de Final Upgrade.

## Reglas de asignación

| Regla | Qué significa |
|---|---|
| Multivalor | una regla lleva todos los valores en los que vale; así se combinan, por ejemplo tipo de pieza "editorial" + temática "deporte" = editorial deportiva |
| Faceta vacía | la regla vale para cualquier valor de esa faceta |
| Rama imagen o video | la da la etapa (5 = imagen, 6 = video); las facetas con dos ramas solo aceptan valores de la rama de la regla |
| Alcance por bloque | el bloque A aplica a todas las reglas; el bloque B a todas las etapas; el bloque C a las etapas 3 a 6, salvo las facetas marcadas "solo etapas 5 y 6"; el bloque D a todas |
| Orden | proceso → pieza → tu cascada (génesis o ancla → acción → sujeto → espacio → estilo → personas → rostro → referencias) → cámara y modelo, en el orden del flujo de anclas (A4 y A5) → atributos de la regla |

## Bloque A — Proceso

### 1. Etapa — ¿en qué etapa del pipeline se aplica? (director §3)

| Valor | Definición |
|---|---|
| 0 Brand Lock | identidad de marca: paleta, tipografía, never list, voz |
| 1 Estrategia creativa | brief, SMP, territorios, concept cards, selección |
| 2 Guion | escenas, sluglines, acción, diálogo, XML |
| 3 Dirección cinematográfica | fórmula de escena, blocking, cámara motivada, 5 anclas, vocabulario prohibido |
| 4 Shot planning | shots.json, timing, texto en pantalla, series lock |
| 5 Imagen | génesis, anclas, edición, crítica y canonización |
| 6 Video | prompts de movimiento |
| 7 Paquete y entrega | carpeta final, preview, trazabilidad, créditos |
| Post-producción | generar clips, ensamblar, grade, audio, export |

### 2. Paso — ¿en qué paso de esa etapa? (Mapa del Spot)

Si la regla vale para toda la etapa, va sin paso.

| Etapa | Pasos |
|---|---|
| 0 | E0.1 reunir fuentes · E0.2 extraer las 9 secciones · E0.3 asignar confianza · E0.4 escribir brand-lock.md |
| 1 | E1.1 lectura del brief · E1.2 territorios · E1.3 concept cards · E1.4 matriz · E1.5 dirección narrativa |
| 2 | E2.1 analizar concepto · E2.2 breakdown · E2.3 escribir escenas · E2.4 XML |
| 3 | E3.1 fórmula de escena · E3.2 blocking y staging · E3.3 cámara y lente · E3.4 luz, color y ritmo · E3.5 5 anclas |
| 4 | E4.1 beat framework · E4.2 timing · E4.3 shot list · E4.4 texto separado · E4.5 series lock · E4.6 rationale y run.json |
| 5 | E5.1 plan de anchors · E5.2 génesis sin referencias · E5.3 maestros derivados · E5.4 cuadros con referencias · E5.5 edición quirúrgica · E5.6 borradores · E5.7 crítica · E5.8 revisión · E5.9 canonizar |
| 6 | E6.1 motion draft · E6.2 sintaxis del modelo · E6.3 continuidad · E6.4 dramaturgy check · E6.5 linter · E6.6 micro-gate y entrega |
| 7 | E7.1 árbol del paquete · E7.2 preview · E7.3 checklist de post · E7.4 trazabilidad |
| Post | POST.1 generar y verificar clips · POST.2 ensamblar y exportar |

## Bloque B — La pieza (se decide en la etapa 1 y vale para todas las etapas)

### 3. Track — ¿de qué tamaño es el proyecto? (director §2)

| Valor | Definición |
|---|---|
| EXPRESS | hasta 30 s, sin marca formal |
| STANDARD | de 30 a 90 s, spot de campaña |
| FILM | de 90 s a 10 min, multi-escena |

### 4. Tipo de pieza — ¿qué pieza se entrega?

**Rama imagen**

| Valor | Definición | Fuente |
|---|---|---|
| editorial | imagen con lenguaje de revista; se combina con la temática: editorial de moda, deportiva, musical, gastronómica | image/patterns/fashion-editorial |
| key visual de campaña | imagen principal de una campaña publicitaria | image/patterns |
| e-commerce o catálogo | producto para tienda o catálogo | image/patterns/ecommerce |
| retrato | una persona como sujeto de la pieza | image/patterns/portrait-cinema |
| póster o key art | pieza gráfica con título o composición de cartel | image/patterns/poster-illustration |
| post o historia para redes | imagen para feed o historias | image/patterns/ui-social |
| miniatura | thumbnail de video con rostro y gancho | image/characters, Viral Thumbnails |
| UI o mockup | pantallas, apps, maquetas de interfaz | image/patterns/ui-social, image/structural |
| slide o presentación | una diapositiva: portada, datos, comparación, proceso | image/slides |
| storyboard o multipanel | varios paneles en una imagen | image/storyboards, image/multi-panel |
| diseño de personaje | hoja o maestro de un personaje | image/patterns/character-design |
| visualización arquitectónica | render de espacio, plano a 3D | image/dimensional |
| identidad de marca | logo, sistema visual, aplicaciones | image/structural, Brand Identity Systems |

**Rama video**

| Valor | Definición | Fuente |
|---|---|---|
| spot publicitario | comercial de producto o marca de 15, 30 o 60 s | director; patterns-and-genres §2 Commercial |
| campaña | serie de piezas con un mismo concepto | director |
| brand film o brand story | pieza de atmósfera sobre la marca, planos largos | director; ai-video-storyboard, Brand Story |
| videoclip | la música es la columna de la pieza | patterns-and-genres §2 Music video |
| fashion film | prenda en movimiento | patterns-and-genres §2 Fashion |
| cortometraje de ficción | historia de 90 s a 10 min | director (track FILM) |
| explainer de producto | problema, solución, cómo funciona, resultados, CTA | ai-video-storyboard, Product Explainer |
| demo educativa | enseña a hacer algo paso a paso | storyboard-architect, Educational Demo |
| founder o testimonial | una persona cuenta la marca a cámara | storyboard-architect, Founder Explainer |
| UGC o social ad | estética de creador con celular | patterns-and-genres §2 UGC / Social |
| reel con narrativa | reel, TikTok o Short con arco | director; ai-video-storyboard |
| anuncio para redes | Instagram o TikTok ad de 15 o 30 s | ai-video-storyboard |
| hook de 15 s | una sola idea con cortes rápidos | ai-video-storyboard, TikTok Hook |

### 5. Temática o industria — ¿de qué sector o tema es la pieza?

Se combina con el tipo de pieza: editorial + deporte = editorial deportiva; editorial + música = editorial musical.

| Valor | Definición | Fuente |
|---|---|---|
| deporte y fitness | atletas, clubes, competencia | regímenes 04 y 06; race-and-speed |
| automotriz y movilidad | autos, motos, bicis | regimen 05; race-and-speed |
| música | artistas, conciertos, videoclips | patterns-and-genres §2 |
| moda | prendas, modelos, pasarela | image/patterns/fashion-editorial |
| comida y bebida | producto comestible o bebida | image/patterns/food-beverage |
| arquitectura e inmobiliaria | espacios y edificios | image/dimensional |
| belleza y cuidado personal | cosmética, piel, cabello | propuesto |
| hospitalidad y viajes | hoteles, destinos | propuesto |
| retail y supermercado | tiendas, anaquel, promociones | propuesto |
| tecnología | apps, dispositivos, SaaS | propuesto (image/slides, estilo SaaS) |
| salud y bienestar | clínicas, bienestar | propuesto |
| educación | cursos, material didáctico | propuesto (visual-media §7) |
| corporativo | B2B, institucional | propuesto |

### 6. Formato de salida — ¿en qué proporción se entrega? (shots.schema)

| Valor | Definición |
|---|---|
| 16:9 | horizontal: TV, web, YouTube |
| 9:16 | vertical: Reels, TikTok, Shorts, historias |
| 1:1 | cuadrado: feed |
| 4:5 | vertical corto: feed de Instagram |
| 21:9 | cinemascope |

### 7. Género narrativo (rama video y guion) — ¿qué drama cuenta? (patterns-and-genres §2)

| Valor | Definición |
|---|---|
| tragedia doméstica | drama íntimo en interiores, objetos cotidianos cargados |
| drama psicológico | tensión interna del personaje |
| acción | persecución, pelea, riesgo físico |
| carrera y velocidad | vehículo o atleta a velocidad |

### 8. Estructura de beats — ¿qué arco sigue la pieza completa? (storyboard-architect/beat-frameworks; ai-video-storyboard paso 5)

| Valor | Definición |
|---|---|
| Pain-Reframe-Promise | dolor, reencuadre, promesa |
| Hero Trilogy | héroe, obstáculo, transformación |
| Founder Explainer | quién, por qué, qué se construyó |
| Content Spiral | una idea que se profundiza en vueltas |
| Educational Demo | paso a paso de una tarea |
| Hook / Build / Payoff / CTA | default de TikTok |
| Problem / Solution / Proof / CTA | default de anuncio |
| Atmosphere → Climax | brand story: atmósfera, revelación lenta, clímax, logo |
| Custom | estructura propia declarada |

### 9. Patrón de montaje — ¿cómo se encadenan los planos de una secuencia? (patterns-and-genres §1)

| Valor | Definición |
|---|---|
| escalada | cada plano sube la tensión |
| ansiedad | presión creciente e inestable |
| descubrimiento | la información se revela por partes |
| catástrofe | construcción hacia un quiebre |
| drama comercial de producto | el producto resuelve la tensión |
| loop de videoclip | ciclo visual sobre el ritmo |

## Bloque C — El cuadro o el clip (etapas 3 a 6)

### 10. Modo de generación (solo etapas 5 y 6) — ¿génesis o ancla en imagen; qué tipo de clip en video? (casos aurora; archivos de modelo de video)

| Rama | Valor | Definición |
|---|---|---|
| Imagen | génesis sin referencias (caso 1, T1) | solo texto; fija la parte del sujeto que lleva la identidad |
| Imagen | ancla con referencias (caso 2, T2 a T4) | texto más génesis aprobadas: cuerpo con rostro adjunto, cuadro de escena, keyframe |
| Imagen | composición de varias referencias | une elementos de varias referencias sin ser cuadro de clip: producto en escena, póster |
| Imagen | edición de imagen existente (T5) | cambia una zona de una imagen aprobada y conserva el resto |
| Imagen | transferencia de estilo | aplica el estilo de una imagen de referencia a otro contenido |
| Imagen | boceto o wireframe a final | un boceto, layout o plano controla la composición (image/structural, image/dimensional) |
| Video | texto a video | sin imagen de entrada; solo EXPRESS |
| Video | primer frame (3a) | el ancla es el primer cuadro |
| Video | primer y último frame (3b) | dos anclas con el mismo ratio definen inicio y fin |
| Video | con referencias | Elements de Kling, @Image de Seedance, ingredients de Veo |
| Video | motion control (3c) | copia el movimiento de un video de referencia |
| Video | diálogo y lip-sync (4) | el personaje habla y la boca sigue el audio |
| Video | motion brush | se animan regiones de la imagen por separado |
| Video | edición de video | re-render parcial, cambio de fondo, re-doblaje |
| Video | extensión | alarga un clip hacia adelante o atrás |
| Video | multi-shot | varios planos con cortes en una generación |
| Video | ultra long | de 30 a 180 s en una pasada |
| Video | blockout o green screen | una previz 3D o una placa verde controla cámara y staging |
| Video | storyboard como entrada | una grilla de paneles define orden y composición |

### 11. Rol del ancla (solo etapa 5) — ¿para qué sirve la imagen en el video? (flujo-anclas D1)

| Valor | Definición |
|---|---|
| character ref | maestro de identidad de un personaje |
| environment ref | placa del lugar, vacía |
| keyframe FF | primer frame del clip |
| keyframe LF | último frame del clip |
| hero/macro | producto u objeto en detalle |
| motif insert | objeto ancla que reaparece entre clips |

### 12. Función del plano — ¿qué trabajo hace este plano en la historia? (role-modes §4; ai-video-storyboard, Purpose labels)

| Valor | Definición |
|---|---|
| hook | detiene el scroll en el primer segundo |
| establecer | dónde estamos; plano abierto o master |
| revelar | entra información nueva al cuadro |
| poder | quién controla la escena; el staging lo dice |
| presión | la tensión crece; movimiento hacia la amenaza o la decisión |
| detalle | objeto, mano, ojo o textura en close-up o macro |
| reacción | consecuencia emocional en un rostro |
| giro interno | el cuerpo muestra el cambio antes de la decisión |
| impacto | el evento visual decisivo: la caída, el golpe, el quiebre |
| secuela | quietud después del impacto |
| salida | la imagen final que se lleva el espectador |
| CTA o logo | llamado a la acción o cierre de marca |

### 13. Tipo de acción — ¿qué pasa en el cuadro? (flujo-anclas D2 más G y H)

| Valor | Definición | Ejemplo |
|---|---|---|
| A pose sostenida | quietud; el sujeto no cambia de estado | retrato, maestro |
| B instante pico | un instante de máxima fuerza, congelado | clavadista entrando al agua |
| C movimiento continuo | desplazamiento sostenido | auto de carreras |
| D fenómeno de luz o clima | el evento es la luz o el clima | rayo |
| E interacción o diálogo | dos o más personas se relacionan o hablan | dos personas en un café |
| F multitud | la masa hace el trabajo | estadio |
| G acuática en superficie | el sujeto se desplaza sobre el agua | wakeboard, surf, jet ski, remo |
| H subacuática | cámara y sujeto sumergidos | buceador en cenote, apnea |

### 14. Régimen físico — ¿en qué medio físico ocurre? (regimenes/README)

| Valor | Cubre |
|---|---|
| 01 agua en superficie | wakeboarding, surf, jet ski, remo, esquí acuático |
| 02 ruptura de superficie | clavado, nadador emergiendo, salto de ballena, split-level |
| 03 subacuático | buceador en cenote, nadador bajo el agua, apnea |
| 04 objeto balístico | pelota, balón, gota, flecha, chispa |
| 05 vehículo | auto de carreras, moto, bici, tren, dron |
| 06 cuerpo en esfuerzo | corredor en la cinta, salto, golpe, levantamiento |
| 07 luz y clima | rayo, amanecer, lluvia, polvo, niebla, nieve |
| 08 multitud anónima | estadio, manifestación, calle llena, público |
| 09 grupo ensamble | quinteto, grupo de K-pop, equipo, familia |

### 15. Sujeto — ¿qué clase de cosa se fija en la imagen? (flujo-spot, Nivel 3)

| Valor | Definición |
|---|---|
| persona | ser humano; identidad fijada con rostro T1 y cuerpo T2 |
| lugar genérico | sitio sin identidad real: una calle, una cocina |
| edificación o landmark | lugar real y reconocible |
| animal | especie animal |
| producto | objeto con marca o etiqueta real; siempre con referencia |
| objeto o prop | herramienta, vehículo, mobiliario, objeto ancla |

### 16. Espacio — ¿dónde ocurre?

| Valor | Definición |
|---|---|
| interior | bajo techo |
| exterior | al aire libre, incluida el agua abierta |

### 17. Estilo visual — ¿qué look tiene? (flujo-anclas D4; image/creative-direction, Color Grading & Film Stock)

| Valor | Definición |
|---|---|
| documental | luz dura, piel real, grano de reportaje |
| narrativo cinematográfico | una fuente domina, 70% en sombra |
| comercial pulido | luz limpia, producto legible |
| editorial | contraste alto y desaturado, pose y styling de revista |
| retro o vintage | película de otra época: "1980s color film", tonos análogos, negros levantados |
| blanco y negro | grano clásico tipo Ilford HP5 |
| minimalista | manda el espacio negativo |
| race/kinetic | velocidad, paleta fría |
| UGC/social | celular, luz natural |
| experimental | cross-processing, colores desplazados |

### 18. Técnica de representación — ¿con qué técnica se hace la imagen? (prompt-framework, Task Types; image/structural)

| Valor | Definición |
|---|---|
| fotorrealista | debe parecer foto o filmación real |
| ilustración | stickers, íconos, arte dibujado |
| render 3D | objeto o espacio modelado |
| animación 2D | dibujo animado |
| animación 3D | personajes o mundos 3D animados |
| motion graphics | gráfico y tipografía en movimiento |
| pixel art | imagen por píxeles |

### 19. Número de personas — ¿cuántas hay en cuadro? (flujo-anclas D3)

| Valor | Definición |
|---|---|
| 0 | placa sin personas |
| 1 | un sujeto |
| 2 | dos sujetos |
| 3 o más | grupo o multitud |

### 20. Identidad de las personas — ¿se deben reconocer?

| Valor | Definición |
|---|---|
| todas | grupo ensamble: cada miembro reconocible y consistente |
| solo los héroes | hasta 3 reconocibles, el resto anónimo |
| ninguna | multitud anónima: nadie con rostro legible |

### 21. Contacto físico entre personas — ¿se tocan?

| Valor | Definición |
|---|---|
| sí | abrazo, tackle, manos que se tocan |
| no | no hay contacto |

### 22. Tamaño del rostro — ¿cuánto ocupa del cuadro?

| Valor | Definición |
|---|---|
| ≥20% | el rostro manda; la identidad se verifica al zoom |
| <20% | rostro pequeño en el cuadro |
| sin rostro visible | silueta, casco, espalda |

### 23. Referencias adjuntas (solo etapas 5 y 6) — ¿qué referencias acompañan al prompt? (aurora)

| Valor | Definición |
|---|---|
| ninguna | sin referencias |
| persona (P) | rostro o cuerpo de un personaje |
| vestuario (O) | ropa o accesorios |
| lugar (L) | escenario o locación |
| producto o prop (PR) | producto u objeto |
| estilo (S) | referencia de look, color o textura |

### 24. Tamaño de plano — ¿cuánto del sujeto entra en cuadro? (shot-grammar; camera-lighting-vocabulary §1)

| Valor | Definición |
|---|---|
| EWS extreme wide | sujeto pequeño en el entorno |
| WS wide | cuerpo entero con entorno |
| MLS medium wide | cuerpo entero, poco entorno |
| MS medium | de la cintura para arriba |
| MCU medium close-up | cabeza y hombros |
| CU close-up | cabeza, o mano con objeto |
| ECU extreme close-up | ojos, manos, un detalle |
| macro insert | detalle a escala macro |

### 25. Ángulo — ¿desde dónde mira la cámara? (flujo-anclas D9; shot-grammar; vocabulary §1)

| Valor | Definición |
|---|---|
| eye-level | a la altura de los ojos; paridad |
| low | desde abajo; dominio o fuerza |
| high | desde arriba; vulnerabilidad |
| top-down u overhead | cenital; esquema, geometría |
| dutch | cámara inclinada; un beat de inestabilidad |
| worm's eye | desde el suelo |
| POV | lo que ve el personaje |
| over-the-shoulder | sobre el hombro de otro personaje |
| perfil | el sujeto de lado |

### 26. Movimiento de cámara (rama video) — ¿cómo se mueve la cámara? (camera-lighting-vocabulary §2; shots.schema)

| Valor | Definición |
|---|---|
| estática o locked-off | sin movimiento |
| push-in (lento o rápido) | la cámara avanza hacia el sujeto |
| pull-back | la cámara se aleja |
| dolly in / dolly out | avance o retroceso sobre riel |
| tracking o lateral | acompaña al sujeto en paralelo |
| pan | giro horizontal |
| tilt | giro vertical |
| handheld | temblor orgánico de cámara en mano |
| orbit | rodea al sujeto |
| gimbal glide | deslizamiento estabilizado |
| crane | grúa que sube o baja |
| aéreo o dron | desde el aire |
| FPV | vuelo de dron en primera persona |
| whip pan | paneo rápido como transición |
| snap zoom | zoom brusco |
| rack focus | el foco cambia de plano |
| dolly zoom | efecto Hitchcock |
| dive | la cámara se desploma hacia abajo |
| one-take | plano secuencia |
| bullet time | tiempo congelado con cámara girando |
| speed ramp | acelera, frena, acelera |

### 27. Transición (rama video) — ¿cómo pasa este clip al siguiente? (camera-lighting-vocabulary §11)

| Valor | Definición |
|---|---|
| corte natural | punto de edición simple |
| fade in / fade out | desde o hacia negro |
| disolvencia | fundido cruzado de 1 a 2 s |
| flash blanco o negro | un cuadro de golpe como puntuación |
| wipe | el cuadro nuevo empuja al anterior |
| occlusion mask | un objeto tapa la lente y revela la escena nueva |
| match cut | una forma o movimiento parecido une dos escenas |
| action cut o whip | el corte se esconde en un movimiento rápido |
| motion relay | el sujeto sale del cuadro A y sigue en el B |
| zoom-through | la cámara atraviesa una pupila, cerradura o ventana |
| ink-wash dissolve | sangrado estilizado, animación |

### 28. Audio (rama video) — ¿qué suena? (camera-lighting-vocabulary §8)

| Valor | Definición |
|---|---|
| diálogo | personajes hablando en cuadro |
| voz en off | narración fuera de cuadro |
| SFX de ambiente | room tone, ciudad, lluvia, viento |
| SFX de cuerpo y acción | respiración, pasos, tela, puerta |
| SFX de evento dramático | silencio súbito, golpe grave, vidrio que se rompe |
| música | pista musical |
| silencio | ausencia deliberada de sonido |

### 29. Modelo (solo etapas 5 y 6) — ¿para qué modelo vale la regla? (flujo-anclas D8)

Se asigna cuando la regla nombra el modelo o usa su sintaxis.

| Rama | Valores |
|---|---|
| Imagen | Nano Banana 2 · Nano Banana Pro · GPT Image 2 · Flux · Midjourney · Ideogram · Seedream |
| Video | Kling 3.0 · Veo 3.1 · Seedance 2.0 · Seedance 2.5 · Hailuo |

## Bloque D — Atributos de la regla (todas las reglas)

### 30. Qué regula — ¿sobre qué aspecto decide la regla?

| Valor | Definición |
|---|---|
| estrategia y concepto | brief, territorios, concepto |
| estructura narrativa y diálogo | escenas, beats, líneas |
| dramaturgia | fórmula de escena, 3 detalles, emoción traducida a cuerpo |
| encuadre y lente | tamaño de plano, focal, profundidad de campo |
| ángulo | altura y orientación de la cámara |
| movimiento de cámara | cómo se mueve la cámara |
| luz | fuente, dirección, dureza, ratio |
| color, grade y textura | paleta, grade, grano, halación |
| composición | spine, planos, espacio negativo |
| identidad y consistencia | que el sujeto se sostenga entre imágenes y clips |
| anatomía, rostro y piel | manos, rostro, piel documental |
| física y movimiento congelado | cues de velocidad, blur, estado posterior |
| texto en pantalla | overlays y texto dentro de la imagen |
| marca y logos | brand-lock, logos, productos reales |
| estructura y sintaxis del prompt | orden de bloques, slots, palabras permitidas y prohibidas |
| parámetros técnicos | ratio, resolución, duración, calidad |
| audio | diálogo, VO, SFX, música |
| continuidad entre clips | que un clip empate con el siguiente |
| crítica y revisión | criterios para aceptar o rechazar |
| trazabilidad y entrega | registro, carpeta, créditos |

### 31. Condición para avanzar — ¿bloquea el paso a la siguiente etapa?

| Valor | Definición |
|---|---|
| no | no es un gate |
| sí, la verifica una herramienta | validate_shots, linter, auditor |
| sí, la aprueba el usuario | gates 1, 2 y 4 del director |

### 32. Fuente con autoridad — ¿qué skill la dicta? (director §1)

Se asigna sola por el archivo de origen.

| Valor | Autoridad sobre |
|---|---|
| brand-lock-extractor | parámetros de marca |
| creative-strategy.md | estrategia creativa |
| screenwriter | estructura narrativa y diálogo |
| video (dramaturgia) | dramaturgia y lenguaje de cámara |
| storyboard-architect | fuente de verdad estructural (shots.json) |
| ai-video-storyboard | shot list EXPRESS |
| image | sintaxis final de prompts de imagen |
| visual-prompt-forge | estructura de shots a prompt y loop de revisión |
| visual-asset-critic | aceptar o rechazar renders |
| video (archivos de modelo) | sintaxis final de prompts de video |
| storyboard-html-preview | formato de entrega visual |
| visual-media | animación y material didáctico en español (§7) |
| aurora-prompt-linter | veto final sobre prompts |
| produccion-visual-sw30 | templates y reglas de producción SW30 |
| regímenes del repo | física por régimen |
| decisiones del usuario | DECISIONES.md |

## Dónde quedaron los valores que ya no tienen faceta propia

| Antes | Ahora |
|---|---|
| Tipo de imagen: fotorrealista, ilustración | faceta 18, técnica de representación |
| Tipo de imagen: minimalista | faceta 17, estilo visual |
| Tipo de imagen: producto o comercial | faceta 4, e-commerce o key visual; faceta 15, producto |
| Tipo de imagen: secuencial | faceta 4, storyboard o multipanel |
| Tipo de imagen: texto como protagonista | faceta 4, póster o slide; faceta 30, texto en pantalla |
| Tratamiento D4 | faceta 17, estilo visual, ampliada con editorial, retro, blanco y negro y experimental |
| Tratamiento: animación | faceta 18 |
| Género imagen: moda editorial, comida y bebida | faceta 4 (editorial, e-commerce) + faceta 5 (moda, comida y bebida) |
| Género imagen: retrato cinematográfico | faceta 4, retrato + faceta 17, narrativo cinematográfico |
| Género video: videoclip, comercial, moda, UGC | faceta 4 (videoclip, spot, fashion film, UGC) |
| Género video: tragedia, drama, acción, carrera | faceta 7, género narrativo |
