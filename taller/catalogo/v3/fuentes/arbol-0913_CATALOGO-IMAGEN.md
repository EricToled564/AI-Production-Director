# Catálogo de reglas de imagen — árbol v1.0.0

**956 reglas de imagen** catalogadas al **100.0%**. 748 reglas quedaron fuera por ser exclusivas de video.

Una regla vive en **TODAS las ramas** salvo que su propio texto nombre la condición que la acota. Hoy: **642 reglas aplican a cualquier caso de imagen** y **314 nombran al menos una categoría**.

La columna *reglas* es cuántas de las 956 hablan de esa rama. No es cuántas se le aplican: a cualquier caso se le aplican esas más las 642 de TODAS.

## Nivel 2 — references.count   (cuelga de `media = image`)
*¿Cuántas imágenes de referencia entregas? 0, 1, o 2 o más.*
Campo del caso: `references.count` — NUEVO — hoy sólo existe references.mode (none/partial/full), sin conteo

| rama | etiqueta | reglas |
|---|---|---:|
| `0` | sin referencia (texto a imagen) | 4 |
| `1` | una referencia | 12 |
| `2+` | ancla con 2 o más referencias | 12 |

## Nivel 3 — subject.human   (cuelga de `references.count = *`)
*¿Aparecen personas en la imagen?*
Campo del caso: `subject.human` — existe

| rama | etiqueta | reglas |
|---|---|---:|
| `true` | con personas | 75 |
| `false` | sin personas | 5 |

## Nivel 4 — subject.count_class   (cuelga de `subject.human = true`)
*¿Una sola persona o un grupo?*
Campo del caso: `subject.count_class` — NUEVO — hoy existe subject.count (entero) pero ninguna regla puede condicionar sobre 'grupo'

| rama | etiqueta | reglas |
|---|---|---:|
| `1` | una persona | 1 |
| `grupo` | grupo de personas ⚠️ **RAMA VACÍA** | 0 |

## Nivel 4 — scene.category   (cuelga de `subject.human = false`)
*Sin personas: ¿qué es? (exterior, interior, animales, arquitectónica, paisaje natural, producto/objeto, urbana)*
Campo del caso: `scene.category` — NUEVO — hoy environment.indoor_outdoor cubre exterior/interior y environment.type es texto libre; animales/arquitectura/paisaje no existen

| rama | etiqueta | reglas |
|---|---|---:|
| `exterior` | exterior | 3 |
| `interior` | interior | 14 |
| `animales` | animales / fauna | 1 |
| `arquitectonica` | arquitectónica / inmobiliaria | 2 |
| `paisaje_natural` | paisaje natural | 4 |
| `producto_objeto` | producto u objeto | 22 |
| `urbana` | urbana / cityscape | 3 |

## Nivel 5 — style.photography   (cuelga de `subject.human = *`)
*¿Qué estilo de fotografía? (editorial, documental, moda, producto, cinematográfico, vintage/analógico, calle, móvil, bellas artes)*
Campo del caso: `style.photography` — NUEVO — hoy sólo hay deliverable.purpose y task.family, que mezclan destino con estilo

| rama | etiqueta | reglas |
|---|---|---:|
| `editorial` | editorial | 16 |
| `documental` | documental / fotoperiodismo | 1 |
| `natgeo` | documental de naturaleza (National Geographic) ⚠️ **RAMA VACÍA** | 0 |
| `moda` | moda | 8 |
| `producto` | producto / e-commerce | 1 |
| `cinematografico` | cinematográfico | 9 |
| `vintage` | vintage / analógico | 7 |
| `calle` | fotografía de calle ⚠️ **RAMA VACÍA** | 0 |
| `movil` | móvil / snapshot | 3 |
| `bellas_artes` | bellas artes / conceptual | 1 |
| `estudio` | retrato de estudio ⚠️ **RAMA VACÍA** | 0 |

## Nivel 5 — lighting.setup   (cuelga de `subject.human = *`)
*¿Cómo está iluminada? (estudio, natural exterior, luz de ventana, golden hour, artificial nocturna, mixta)*
Campo del caso: `lighting.setup` — NUEVO — el schema no tiene NINGÚN campo de iluminación

| rama | etiqueta | reglas |
|---|---|---:|
| `estudio` | estudio (softbox, strobe, controlada) ⚠️ **RAMA VACÍA** | 0 |
| `natural_exterior` | natural exterior | 1 |
| `ventana` | luz entrando por ventana ⚠️ **RAMA VACÍA** | 0 |
| `golden_hour` | golden hour / atardecer | 1 |
| `artificial_nocturna` | artificial nocturna | 3 |
| `mixta` | mixta ⚠️ **RAMA VACÍA** | 0 |

## Nivel 5 — composition.shot_size   (cuelga de `subject.human = *`)
*¿Qué tamaño de toma? (macro, close-up, plano medio, cuerpo completo, plano general)*
Campo del caso: `composition.shot_size` — NUEVO — hoy subject.body_visibility cubre sólo cuerpo humano (face/upper_body/full_body) y no sirve para objetos ni paisaje

| rama | etiqueta | reglas |
|---|---|---:|
| `macro` | macro / detalle ⚠️ **RAMA VACÍA** | 0 |
| `close_up` | close-up | 3 |
| `plano_medio` | plano medio ⚠️ **RAMA VACÍA** | 0 |
| `cuerpo_completo` | cuerpo completo | 2 |
| `plano_general` | plano general / amplio | 2 |

## Nivel 5 — task.theme   (cuelga de `subject.human = *`)
*¿Cuál es el tema? (deportiva, musical, moda, gastronómica, corporativa, médica, viaje, automotriz, otra)*
Campo del caso: `task.theme` — NUEVO — hoy task.genre es texto libre y ninguna regla puede condicionar sobre él

| rama | etiqueta | reglas |
|---|---|---:|
| `deportiva` | deportiva | 6 |
| `musical` | musical / concierto | 2 |
| `moda` | moda ⚠️ **RAMA VACÍA** | 0 |
| `gastronomica` | gastronómica | 8 |
| `corporativa` | corporativa | 3 |
| `medica` | médica / científica | 3 |
| `viaje` | viaje / turismo | 3 |
| `automotriz` | automotriz | 1 |
| `otra` | otra ⚠️ **RAMA VACÍA** | 0 |

## Nivel 5 — motion.action_complexity   (cuelga de `subject.human = *`)
*¿Qué tan compleja es la acción? (estática, pose dirigida, acción simple, acción compleja / varios cuerpos en contacto)*
Campo del caso: `motion.action_complexity` — NUEVO — hoy hay motion.static_frame y motion.frozen_action (booleanos) pero no un grado de complejidad

| rama | etiqueta | reglas |
|---|---|---:|
| `estatica` | estática | 11 |
| `pose_dirigida` | pose dirigida | 6 |
| `accion_simple` | acción simple (un cuerpo) | 5 |
| `accion_compleja` | acción compleja (varios cuerpos, contacto, física) | 4 |

## Nivel 5 — text.mode   (cuelga de `media = image`)
*¿Lleva texto dentro de la imagen? (no / texto legible corto / tipografía compleja)*
Campo del caso: `text.mode` — existe (none/composite/in_image) — descubierto en el catálogo: 138 reglas hablan de texto

| rama | etiqueta | reglas |
|---|---|---:|
| `none` | sin texto ⚠️ **RAMA VACÍA** | 0 |
| `in_image` | texto dentro de la imagen | 16 |
| `composite` | texto compuesto después | 7 |

## Nivel 5 — generator.family   (cuelga de `media = image`)
*¿Con qué modelo se genera?*
Campo del caso: `generator.family` — existe — descubierto en el catálogo: 113 reglas son específicas de modelo

| rama | etiqueta | reglas |
|---|---|---:|
| `nano_banana` | Nano Banana / Pro | 39 |
| `gpt_image` | GPT Image 2 | 67 |
| `midjourney` | Midjourney | 14 |
| `flux` | Flux | 17 |
| `ideogram` | Ideogram | 15 |
| `seedream` | Seedream | 3 |

## Ramas vacías — ninguna regla del KB dice nada específico

Esto no son reglas muertas: son **casos sin regla**. Si pides una imagen en esa rama, el sistema sólo puede aplicarle las reglas generales.

- `subject.count_class=grupo`
- `style.photography=natgeo`
- `style.photography=calle`
- `style.photography=estudio`
- `lighting.setup=estudio`
- `lighting.setup=ventana`
- `lighting.setup=mixta`
- `composition.shot_size=macro`
- `composition.shot_size=plano_medio`
- `task.theme=moda`
- `task.theme=otra`
- `text.mode=none`

## Restricciones de alcance propuestas (NO aplicadas)

30 reglas enuncian su propia condición en el texto. Quedan como propuesta con su fragmento literal; ninguna se aplicó, porque acotar el alcance por error mataría la regla en los demás casos.

