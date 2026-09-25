# RESEARCH DE CAMPO — Familia 05 · Vehículo en movimiento

Archivo auditado: `.claude/rules/regimenes/05-vehiculo.md` (BORRADOR 2026-09-25).
Fecha de acceso de todas las URLs: **2026-09-25**. Protocolo: skill `research` v2 (6 fases).

## Fase 1 — Pre-flight

```
TEMA DE RESEARCH: evidencia de campo para las 9 líneas [A PRUEBA] de la familia 05
                  (inclinación en moto, cadencia en bici, discos de hélice, paleta cálida
                  comercial, rig casco/chest mount, fallos moto vertical y palas nítidas).
PROPÓSITO DOWNSTREAM: cambiar etiqueta [A PRUEBA] → [CAMPO: url] / [REFUTADA: url];
                  corregir redacción de la regla de bicicleta si el campo la contradice.
MÍNIMOS: queries 5+ · fetches 7+ (4+ ok) · fuentes profesionales 4+ · anti-patrón 2+
```

## Fase 2 — Bitácora cuantitativa

### Queries (6 ejecutadas, 3 anti-patrón)

| # | Herramienta | Query | Ángulo | Resultado |
|---|---|---|---|---|
| Q-1 | firecrawl_search (web) | `motorcycle racing photography lean angle knee down panning shutter speed guide` | fotografía real | ✅ 6 (motorsportphotographer, racetagger, Tamron, r/photography) |
| Q-2 | firecrawl_search (web) | `propeller blur photography shutter speed aircraft "prop disc" frozen propeller looks wrong` | **anti-patrón** (hélice congelada) | ✅ 6 (Piemags, Van's Air Force, DPReview) |
| Q-3 | firecrawl_search (web) | `AI image motorcycle cornering wrong physics lean angle midjourney OR "stable diffusion" OR "nano banana" motorbike prompt` | **anti-patrón** AI | ✅ 6 (media.io, pixloop, YouTube ER Art) |
| Q-4 | firecrawl_search (web) | `cycling photography panning legs blur cadence sweat shutter speed tips` | fotografía real | ✅ 6 (singletracks, Pinkbike, Nick Dale, Tamron Americas) |
| Q-5 | firecrawl_search (web) | `AI generated car motion blur wheels frozen spokes sharp fail prompt fix "wheels"` | **anti-patrón** AI | ✅ 6 (r/Wheels, coinis, Adobe Community) |
| Q-6 | firecrawl_search (web) | `GoPro chest mount vs helmet mount motorcycle POV handlebars in frame` | rig | ✅ 6 (telesin, r/MTB, vitalmx, singletrackworld) |

### Fetches (18 intentos, 14 exitosos)

| # | URL | Resultado |
|---|---|---|
| F-1 | https://blog.professionalaviationphotography.com/propeller-blur-shutter-speed/ | ✅ guía completa Piemags (Paul Fearn, 2026-06-20) |
| F-2 | https://www.motorsportphotographer.com/how-to-photograph-motorcycle-racing/ | ✅ Rhys Vandersyde, 2026-06-13 |
| F-3 | https://racetagger.cloud/blog/NEW-2-Panning-Photography-Masterclass | ✅ 2026-02-11 |
| F-4 | https://www.telesinstore.com/blogs/news/helmet-vs-chest-vs-handlebar-mount | ✅ (116 KB, extraído por script) |
| F-5 | https://www.singletracks.com/community/how-to-snag-a-mountain-bike-panning-shot/ | ✅ Matt Miller, 2020 |
| F-6 | https://www.reddit.com/r/Wheels/comments/1ommqqm/how_to_accurately_render_any_wheels_on_any_car/ | ❌ Reddit no soportado (Firecrawl y WebFetch) |
| F-7 | https://www.reddit.com/r/MTB/comments/tiz5mn/chest_mount_vs_helmet_mount_for_go_pro/ | ❌ Reddit no soportado |
| F-8 | https://www.reddit.com/r/photography/comments/6khvwj/tips_for_shooting_motorcycle_racing/ | ❌ Reddit no soportado |
| F-9 | https://www.dpreview.com/forums/threads/notes-on-shooting-air-shows-with-propeller-planes.4609658/ | ✅ hilo completo (80 KB, extraído por script) |
| F-10 | https://www.vitalmx.com/forums/moto-related/gopro-or-action-camera-chin-mount-or-chest-mount | ❌ timeout ×3 (60 s) |
| F-11 | https://www.pixloop.ai/prompts/video-2051647669890650570 | ✅ parcial (metadatos + prompts similares; el cuerpo del prompt no se renderiza) |
| F-12 | https://www.media.io/ai-prompts/gemini-ai-motorcycle-photo-prompt.html | ✅ 25 prompts Nano Banana Pro |
| F-13 | https://www.tamron.com/global/consumer/sp/impression/detail/article-how-to-shoot-motorsport-photography.html | ✅ Tamron oficial, 2024-11-29 |
| F-14 | https://vansairforce.net/threads/capturing-the-prop-blur.56891/ | ✅ hilo de foro completo |
| F-15 | https://www.youtube.com/watch?v=aA5X6vSiWNo | ✅ transcript Pinkbike / Matt Delorme |
| F-16 | https://www.nickdalephotography.com/blog/the-slow-pan | ✅ |
| F-17 | https://coinis.com/blog/bicycle-ad-photo-warped-spokes-fix-coinis | ✅ 2026-08-27 |
| F-18 | https://www.youtube.com/watch?v=10fhs81W6Bc | ✅ descripción con 4 prompts Nano Banana MotoGP |

Fuentes profesionales (4+): Tamron Co. (F-13, fabricante); Sony Alpha Universe (ver familia 04 F-13, panning 1/30–1/60); Piemags / Paul Fearn, fotografía de aviación profesional (F-1); Rhys Vandersyde, fotógrafo de motorsport en activo desde 2012 (F-2); Matt Delorme, fotógrafo de Pinkbike (F-15). Foros de usuarios expertos: DPReview (F-9), Van's Air Force (F-14).

## Fase 3 — Citas verbatim

| Q# | URL | Cita verbatim |
|----|-----|---------------|
| C-01 | F-2 motorsportphotographer | "With bikes, the lean angle of the bike and rider is one of the most useful tools you have for showing speed." |
| C-02 | F-2 motorsportphotographer | "The apex is usually where the rider has their knee, and sometimes their elbow, closest to the ground, and it's also where they're at their most stable." |
| C-03 | F-2 motorsportphotographer | "Normally in motorsport we try to hide the wheels on high shutter speed shots, because frozen, stationary wheels make the car look like it's simply parked on the track." |
| C-04 | F-2 motorsportphotographer | "Down the straight, the rider tucks in as tight to the bike as they can to cut wind resistance and chase top speed. In the braking zone, they sit up and use their body as natural drag to help slow the bike down. Through the corner, they hang off and put the bike on its ear." |
| C-05 | F-2 motorsportphotographer | "Worse, because the rider is looking through the corner on the low side of the bike, shooting from above leaves you with a rider who's looking away from the camera." |
| C-06 | F-13 tamron | "At the moment of cornering, capturing the extreme ground contact between the rider, machine, and ground will create a tense and dynamic image." |
| C-07 | F-3 racetagger | "MotoGP / Motorcycle Racing: - Speed: 200+ km/h - Shutter: 1/200s - 1/320s - Challenge: Smaller subject, lean angles make tracking harder - Best angle: Apex of corners (dramatic lean + motion blur)" |
| C-08 | F-12 media.io (Track Day Speed Blur) | "A rider in a bright racing suit cornering a superbike on a racetrack, aggressive lean angle, motion blur in the background, sharp focus on helmet and front fairing, harsh midday sun with crisp shadows" |
| C-09 | F-12 media.io | "Add motion language for speed: panning shot, background streaks, subtle wheel blur, but keep the rider sharp." |
| C-10 | F-1 piemags | "A frozen propeller on a flying aircraft reads as a mistake to almost everyone, even people who cannot articulate why." |
| C-11 | F-1 piemags | "At the demanding end is the full disc, where the blades merge completely into a single translucent circle, like a faint grey coin laid over the engine." |
| C-12 | F-1 piemags | "A frozen-looking prop is more forgivable head-on than side-on, but aim for at least some movement." |
| C-13 | F-1 piemags | "If a propeller looks like a strange curved scythe, your electronic shutter is reading the sensor too slowly for the fast blade movement." |
| C-14 | F-14 vansairforce (Snowflake) | "I find that photos of planes look more \"believable\" when the prop has between 1/6 and 1/4 of a sweep blurred." |
| C-15 | F-14 vansairforce (Snowflake) | "Photos of stopped props look very, very wrong somehow." |
| C-16 | F-9 dpreview | "To get a good prop blur, you need to shoot at below 1/250 and more like 1/125th." |
| C-17 | F-4 telesin | "A chest mount puts the bike and your hands in the shot, which usually creates the strongest sense of speed." |
| C-18 | F-4 telesin | "A helmet mount follows your line of sight, making it easier to film the trail or a rider ahead." |
| C-19 | F-4 telesin | "The bars, hands and front of the bike also give viewers a reference point, making drops look steeper and rough sections feel more physical." |
| C-20 | F-5 singletracks | "Everything from his eyes to the sole of his shoes are still sharp, while there is still a blurred background." |
| C-21 | F-15 youtube Pinkbike (transcript) | "so a speed pan shot essentially we are freezing the action of the rider but blurring the land around them as they travel through it" |
| C-22 | F-16 nickdale | "If your shutter speed is high (at least 1/1000 of a second), then it just looks as if the car is parked on the track!" |
| C-23 | F-16 nickdale | "However, the cheetah's legs and the background are also blurred, and that gives a much more vivid impression of the movement of the animal" |
| C-24 | prompt-architects (#15, ver familia 04 F-14) | "Fast shutter freezes the rider's face and the near pedal, motion blur on the spinning wheel's spokes. Camera panning at the rider's speed, the spokes blurred into a wheel-shaped smear." |
| C-25 | prompt-architects (ver familia 04 F-14) | "Spinning wheels are the tell here. A frozen wheel reads as parked; a blurred one reads as moving, rider sharp or not." |
| C-26 | F-17 coinis | "a six-blade propeller photographed with a rolling-shutter phone camera renders as a warped, sickle-shaped smear instead of straight blades" |
| C-27 | F-11 pixloop (prompt relacionado, listado) | "The black-and-red sportbike is already leaned extremely low" |
| C-28 | F-12 media.io (Desert Highway Cinematic) | "golden hour sun flare, warm rim light on leather jacket, wide open sky" |

Citas SNIPPET-ONLY:
- Q-6, r/MTB: "Helmet mount makes the video look like a drone flying through the trails because you can't see any of the bike." `[SNIPPET-ONLY]`
- Q-3, pixloop og:description: "High-speed cornering with accurate lean angles, proper braking points, and weight transfer." `[SNIPPET-ONLY]`
- Q-6, Facebook CFMTB: "Chest mount is great to see the bars and allows the view to 'feel' the ride." `[SNIPPET-ONLY]`

## Fase 4 — Tabla de veredictos por regla [A PRUEBA]

| # | Texto exacto de la regla | Veredicto | URLs que lo sostienen | Nota |
|---|---|---|---|---|
| 1 | Este archivo se carga después, solo para las extensiones: moto, bicicleta, tren, lancha, dron y avión ligero. | **SIN EVIDENCIA** | — | Regla de enrutamiento. |
| 2 | En moto la física visible es el ángulo de inclinación y el borde del neumático trabajando: rodilla o codo cerca del suelo, el cuerpo descolgado hacia el interior de la curva. | **CONFIRMADA EN CAMPO** | F-2 (C-01, C-02, C-04), F-13 (C-06), F-3 (C-07), F-12 (C-08) | Cuatro fuentes independientes, dos de ellas profesionales. Los prompts de campo ya usan "aggressive lean angle". |
| 3 | En bicicleta la velocidad se lee en la cadencia barrida de las piernas y en la cadena, con el cuerpo tenso sobre el manillar; el sudor es el specular de este vehículo. | **REFUTADA** (en su formulación) | F-5 (C-20), F-15 (C-21), F-12 (C-09), prompt-architects (C-24, C-25) | El campo muestra lo contrario: ciclista **nítido de ojos a suela** y velocidad leída en **rayos barridos + fondo barrido**. Solo Nick Dale (C-23, animales, 1/100) defiende barrer las patas. Sudor: sin evidencia. Reformular: "piernas y pedal nítidos, rayos en disco, fondo barrido". |
| 4 | En dron o hélice, las palas se dibujan como discos translúcidos, nunca como palas nítidas. | **CONFIRMADA EN CAMPO** (con matiz) | F-1 (C-10, C-11, C-12), F-14 (C-14, C-15), F-9 (C-16) | "Nunca palas nítidas" confirmado por tres fuentes. Matiz: el disco completo no es el único objetivo; un arco parcial (1/6–1/4 de barrido) se lee más creíble para algunos fotógrafos, y de frente la hélice congelada es más perdonable. Toda la evidencia es de avión/helicóptero; **ninguna fuente habla de dron**. |
| 5 | Fuera del registro race, un spot comercial de vehículo puede usar paleta cálida: entonces se declara el tratamiento comercial en la tarjeta y el ban de ámbar no aplica. | **SIN EVIDENCIA** | F-12 (C-28) como indicio | Regla editorial interna. Indicio débil: los packs comerciales de prompts de moto usan golden hour sin restricción, pero nadie discute la política de paleta. |
| 6 | En bici y moto el rig cercano es la cámara de casco o el chest mount: POV con manillar y manos en primer plano duro. | **CONFIRMADA EN CAMPO** (corregir redacción) | F-4 (C-17, C-18, C-19), snippets r/MTB y Facebook | El manillar y las manos en cuadro son propios del **chest mount**; la cámara de **casco** sigue la mirada y **no muestra la bici** ("como un dron"). La regla debe separar los dos rigs. |
| 7 | Moto vertical en curva: declarar el ángulo de inclinación y el lado de la rodilla. | **CONFIRMADA EN CAMPO** | F-2 (C-01, C-02), F-12 (C-08), F-11 (C-27) | Misma base que la regla 2; los prompts de campo declaran la inclinación de forma explícita. "Lado de la rodilla": ninguna fuente lo nombra, pero C-05 (piloto mira hacia el lado bajo) lo justifica. |
| 8 | Palas de dron nítidas: pedir discos translúcidos. | **CONFIRMADA EN CAMPO** (con matiz) | F-1 (C-11, C-13), F-14 (C-14), F-17 (C-26) | Añadir a la corrección: "nunca palas curvadas tipo hoz" (artefacto de rolling shutter que los modelos pueden imitar). Sin evidencia específica de dron. |
| 9 | [checklist] Inclinación y borde de neumático en moto; cadencia barrida en bici; discos en hélices. | **PARCIAL**: moto ✅ · hélices ✅ · bici ❌ | ver reglas 2, 3, 4 | Sustituir "cadencia barrida en bici" por "rayos barridos, ciclista nítido". |

**Resumen familia 05:** 9 reglas A PRUEBA → **5 CONFIRMADAS** (2 con matiz, 1 con corrección de redacción), **1 REFUTADA** (bici), **1 PARCIAL** (checklist), **2 SIN EVIDENCIA** (enrutamiento y paleta).

## Fase 4b — Hallazgos nuevos

1. En moto la postura del piloto **debe** declararse según la fase: tumbado sobre el depósito en recta, erguido haciendo freno aerodinámico en la frenada, descolgado en la curva; la postura cuenta más que cualquier técnica compositiva. [CAMPO: https://www.motorsportphotographer.com/how-to-photograph-motorcycle-racing/] — (C-04) `[QUOTED]`
2. La cámara **siempre** baja a la altura del piloto en moto: desde arriba la moto se ve pequeña y el piloto mira hacia el lado bajo, lejos de cámara. [CAMPO: https://www.motorsportphotographer.com/how-to-photograph-motorcycle-racing/] — (C-05) `[QUOTED]`
3. Si el rim no se puede barrer, **debe** ocultarse: las ruedas congeladas hacen que el vehículo parezca aparcado. [CAMPO: https://www.motorsportphotographer.com/how-to-photograph-motorcycle-racing/] — (C-03) `[QUOTED]` — refuerza `race-and-speed.md §10` y añade la salida de encuadre.
4. **Nunca** aceptar rayos ni palas curvados en forma de hoz: es el artefacto de rolling shutter y se lee como defecto de cámara barata. [CAMPO: https://coinis.com/blog/bicycle-ad-photo-warped-spokes-fix-coinis] — (C-26, C-13) `[QUOTED]`
5. Para hélice, el objetivo por defecto **debe** ser un arco de 1/6 a 1/4 de barrido, no necesariamente el disco completo; el disco completo puede desaparecer contra el fondo. [CAMPO: https://vansairforce.net/threads/capturing-the-prop-blur.56891/] — (C-14) `[QUOTED]`
6. Frase de campo para bici y moto: "camera panning at the rider's speed, the spokes blurred into a wheel-shaped smear", con "near pedal" o "front fairing" nítidos. [CAMPO: https://prompt-architects.com/blog/359-sports-and-action-motion-prompts] — (C-24) `[QUOTED]`
7. El rig POV **debe** nombrarse por lo que muestra: chest mount = manillar + manos + horquilla en cuadro; helmet/chin mount = sigue la mirada, bici fuera de cuadro. [CAMPO: https://www.telesinstore.com/blogs/news/helmet-vs-chest-vs-handlebar-mount] — (C-17, C-18, C-19) `[QUOTED]`
8. Referencia física para describir el "panning look": 1/125–1/250 s en autos, 1/60–1/125 s en motos (racetagger) y 1/30–1/60 s en atletas (Sony); un prompt puede anclar el cue con el número. [CAMPO: https://racetagger.cloud/blog/NEW-2-Panning-Photography-Masterclass] — `[DERIVED]` de C-07 y de Sony F-13 (familia 04).
9. Los prompts de MotoGP que circulan en tutoriales de Nano Banana piden logos de patrocinador y el número "46": **nunca** copiarlos tal cual; violan la regla de marcas generadas. [CAMPO: https://www.youtube.com/watch?v=10fhs81W6Bc] — `[QUOTED]` (descripción del video: "full Yamaha racing suit with sponsor logos and racing number '46'").
10. En la frenada, la carrocería **debe** mostrar el cabeceo ("the car's body dipping during braking") como cue de física. [CAMPO: https://www.tamron.com/global/consumer/sp/impression/detail/article-how-to-shoot-motorsport-photography.html] — `[QUOTED]` — coincide con `race-and-speed.md §1` (nariz/squat).

## Fase 5 — Forbidden patterns scan

☑ Ejecutado · sin detecciones. Toda cifra de obturación lleva URL; los snippets están marcados.

## Fase 6 — Checklist de auditoría del skill

- [x] 5+ queries (6)
- [x] 7+ fetch attempts (18)
- [x] 4+ fetches exitosos con quotes (14 exitosos, 28 citas)
- [x] 4+ fuentes profesionales (Tamron, Sony, Piemags, Vandersyde, Pinkbike)
- [x] 2+ queries anti-patrón (Q-2, Q-3, Q-5)
- [x] Cada veredicto con C-#/F-#
- [x] Etiquetas epistémicas en hallazgos
- [x] Sin paráfrasis como cita
- [x] Sin autoridad sin URL
- [x] Forbidden patterns scan limpio
- [x] Limitaciones presentes

## Limitaciones del research

- Reddit (r/Wheels, r/MTB, r/photography) y Vital MX inaccesibles; las citas de usuario de esos hilos son solo snippets.
- No hay ninguna fuente sobre **dron** (multirrotor); toda la evidencia de hélice es de aviación tripulada y helicópteros. La extrapolación a dron sigue siendo inferencia.
- No se encontró evidencia sobre tren, lancha ni avión ligero como stills de velocidad.
- La regla de paleta cálida comercial es una decisión editorial; no es esperable encontrarla en campo.
- pixloop no renderiza el cuerpo del prompt; la cita "accurate lean angles" es solo del og:description.

## Sugerencia de próximo paso

Reescribir la regla 3 (bici) con la formulación de campo y correr el ejercicio de canonización con el prompt #15 de prompt-architects (C-24) en NBP; comprobar al 100% si el modelo barre los rayos sin barrer el pedal.
