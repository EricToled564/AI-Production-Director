# Familias de régimen físico — reglas para anclas cinematográficas

Nueve archivos, uno por régimen. Cada uno especializa `video/references/animatic-keyframes.md`
igual que `race-and-speed.md` lo hace para el dominio de carreras: no repite el método general,
añade lo que cambia en ese medio físico.

Decisiones que gobiernan esta carpeta (sesión 2026-09-25):

1. Viven en el repo. `rule_registry.py` las lee además de los skills instalados.
2. Toda regla lleva una etiqueta de origen al final de la línea. Sin etiqueta, la regla no entra a la base.
3. Las inferencias entran con `[A PRUEBA]`, prioridad 4, y nunca bloquean un gate hasta canonizarse.
4. Canonización en tres pasos: investigación de campo en foros y tutoriales → un ejercicio real por
   familia → etiqueta `[CANONICA fecha]` con el template que funcionó.

## Etiquetas de origen

| Etiqueta | Significado | Prioridad en la base |
|---|---|---|
| `[FUENTE: skill/archivo.md §sección]` | La regla está textual o casi textual en un skill instalado | la del skill |
| `[A PRUEBA]` | Inferencia desde reglas vecinas o física; sin fuente textual | 4, nunca bloquea |
| `[CAMPO: url]` | Inferencia confirmada por casos de uso reales, foros o tutoriales; todavía sin ejercicio propio | 4, se muestra como recomendada |
| `[REFUTADA: url]` | La investigación de campo la contradijo; se conserva para no volver a inferirla | no se sirve |
| `[CANONICA 2026-MM-DD]` | Ejercicio real hecho, template registrado en el archivo | 1 dentro de su familia |

La etiqueta va al final de la línea normativa, entre corchetes. Una línea puede llevar una sola
etiqueta. El extractor la separa del texto, guarda `estado` y `fuente`, y el id de la regla se
calcula sobre el texto sin etiqueta, así canonizar no cambia el id.

## Esqueleto obligatorio de cada archivo

1. Cuándo cargar
2. Leyes físicas que el still debe evidenciar
3. Cue de movimiento congelado por defecto
4. Luz en este medio
5. Cámara, ángulo y rig montable
6. Modelo recomendado
7. Tratamiento de personas dentro del régimen
8. Fallos conocidos y su corrección
9. Checklist del crítico

## Archivos

| # | Archivo | Cubre |
|---|---|---|
| 01 | `01-agua-superficie.md` | wakeboarding, surf, jet ski, remo, esquí acuático |
| 02 | `02-agua-ruptura.md` | clavado entrando, nadador emergiendo, salto de ballena, split-level |
| 03 | `03-subacuatico.md` | buceador en cenote, nadador bajo el agua, apnea |
| 04 | `04-objeto-balistico.md` | pelota de tenis, balón, gota, flecha, chispa |
| 05 | `05-vehiculo.md` | auto de carreras, moto, bici, tren, dron; extiende race-and-speed |
| 06 | `06-cuerpo-en-esfuerzo.md` | corredor rompiendo la cinta, salto, golpe, levantamiento |
| 07 | `07-luz-y-clima.md` | rayo, amanecer, lluvia, polvo, niebla, nieve |
| 08 | `08-multitud-anonima.md` | estadio, manifestación, calle llena, público |
| 09 | `09-grupo-ensamble.md` | quinteto, grupo de K-pop, equipo titular, familia |

Facetas de la tarjeta de ancla que cada archivo declara en su frontmatter: `d2_accion`,
`d3_sujetos`, `d4_tratamiento`, `d8_modelo`, `d9_angulo`. El extractor las hereda a todas las
reglas del archivo salvo que una regla las sobrescriba con `{d9: low}` al inicio de la línea.
