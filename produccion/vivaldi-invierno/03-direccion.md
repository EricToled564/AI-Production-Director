# Anatomía del frío — Etapa 3: Dirección cinematográfica

Autoridad: skill `video` (dramaturgy.md §1, §2, §12, §13; universal-rules U7, U8, U12; camera-lighting-vocabulary.md;
animatic-keyframes.md §3, §4, §6, §9) + familia `09-grupo-ensamble.md` + reglas recuperadas por `rule_query.py`
(ids citados). Entrada: guion aprobado (gate 2) + análisis medido de la grabación (`audio-analisis.json`).

## 0. El sonido primero — mapa medido de la grabación (82.15 s)

Medido con RMS a 50 ms y textura espectral (proporción de energía > 2 kHz) sobre el mp4 que entregó Eric.
Regla: "you storyboard the sound first; loudness = panel count" (`5f835d0eb35a`, `5e64b7c7d357`).

| Tramo (s) | Nivel medido | Lectura musical | Escena |
|---|---|---|---|
| 0.0–1.0 | golpe a −22 dBFS y caída inmediata | ataque inicial del tramo | 1 |
| 1.0–14.0 | −37 a −42 dBFS, textura grave | el murmullo bajo tras las "puertas cerradas" | 1 |
| 14.0–32.0 | −32 a −41, agudos dominan (60 %) en 18–24 y 36–38 | el violín solo: Sirocco | 2 |
| 32.0–46.0 | subidas a −32 en 32–34 y 39–40, mixto | respuestas del tutti: Borea | 3 |
| 46.0–49.2 | −41 a −44.5, el punto más bajo de toda la pieza | la respiración contenida | 3 (cierre) |
| 49.2–52.0 | subida de −38 a −25 en 2 s | la tormenta se abre | 4 |
| 52.0–77.45 | fuerte (−20 a −25) con valles de 0.7–2.4 s; acentos máximos 54.65 · 56.2 · 56.55 · 60.8 · 61.05 · 61.15 · 69.1 · 71.95 · 72.2 · 72.4 · 72.6 · 72.8 | todos los vientos en guerra; 71.7–75.45 es la carrera final | 4 |
| 75.45–77.45 | valle medio | la pausa antes del último golpe | 4 (cierre) |
| 77.45–78.4 | último tramo fuerte | acorde final | 5 |
| 78.4–82.15 | cola hasta −60 dBFS | resonancia y silencio | 5 |

Pulso detectado ≈ 150 bpm en los cuatro cuartos de la pieza → **un tiempo = 0.40 s**. Toda duración de plano
es múltiplo de 0.4 s: 0.4 · 0.8 · 1.2 · 1.6 · 2.0 · 2.4 · 2.8 · 3.2. Los cortes caen en el tiempo (`09ecf6f81ee5`).

Consecuencia sobre el guion aprobado: las proporciones estimadas (12/23/23/24/8) cambian a
**14 / 18 / 17 / 28 / 5 s**. Ninguna escena cambia de contenido; cambia cuánto vive cada una.

## 1. Ley de la pieza

- **Regla de escala** (`2d91bbc13caa`, invertida a favor nuestro): el plano fuerte va ancho, el plano quieto va cerrado. Los tres planos de quinteto completo caen en los tres eventos más fuertes de la grabación: 0.0 s (ataque), 52.0 s (la tormenta se abre), 77.45 s (acorde final). Todo lo demás es fragmento.
- **Un movimiento dominante por clip** (`a4cd347f4b1e`, vocabulario §2). La energía se construye con la **densidad de corte**, no apilando movimientos. Movimientos permitidos por escena: 1 static/push lento · 2 push, un handheld · 3 static, un push · 4 static en ráfagas, handheld en Kai, whip solo como transición entre ráfaga y ráfaga · 5 static.
- **Nunca dos ráfagas seguidas** (`b04a79b44100`): entre cada ráfaga de la escena 4, un plano quieto de 2.0–2.4 s.
- **Pausa antes del corte más grande** (`c2e0a3b45412`): 46.0–49.2 (antes de la tormenta) y 75.2–77.4 (antes del acorde final) son planos sostenidos con cero blur.
- **Emoción solo en el cuerpo** (U3, dramaturgy §2): mandíbula, nudillos, venas, sudor, aliento visible. Ningún adjetivo emocional en ningún prompt.
- **Paleta**: la familia 05 §4 y `race-and-speed.md` §7 prohíben el ámbar en el registro race; este proyecto es `d4=narrativo`, no race, y la luz cálida es el sujeto del brief. Se declara la excepción aquí, en la tarjeta, como manda la regla: **una sola fuente cálida** (tungsteno, ~2800 K en palabras: "warm tungsten"), negros neutros sin viraje a teal, piel y barniz como únicas superficies que devuelven luz.

## 2. Los cinco anclas (definitivos)

| Ancla | Valor |
|---|---|
| Emoción | Resistencia: el cuerpo que no cede al frío ni a la velocidad. Se ve, no se nombra. |
| Motivo | Polvo de resina suspendido en el haz cálido. Aparece en cada acento, cae más lento que la música, y es lo último que se mueve en la pieza. |
| Objeto | El arco del primer violín: una crin suelta desde el plano 2; se rompe en el quiebre; cuelga quieta en la imagen final. |
| Quiebre | 61.6 s: en plena ráfaga una crin se rompe y azota en el haz; la mano de Vera no se detiene (plano 32). |
| Imagen final | 80.0–82.15 s: la mano derecha de Vera se abre, el arco baja unos milímetros hasta la cuerda y se queda; la crin rota cuelga; el polvo termina de caer. |

## 3. Dirección por escena

Formato por escena: blocking · cámara motivada ("¿qué cambió?") · lente · luz · color · ritmo.

### Escena 1 — Puertas cerradas (0.0–14.0)

- **Blocking.** Los cinco en su marca. Vera frente-izquierda, Ilan frente-derecha, Noor centro-atrás, Tomás sentado atrás-izquierda, Kai de pie atrás-derecha. Al golpe inicial los cinco arcos bajan a la vez; después nadie se mueve más de lo que exige un tremolo bajo.
- **Cámara.** Plano 1: wide frontal, eye-level, static — cambió el sonido (el golpe), así que la cámara enseña todo el mundo de una vez y no vuelve a hacerlo hasta el segundo 52. Planos 2–5: macro y CU, static, con un solo push lento sobre Ilan (plano 4) porque su arco tiembla y la cámara se acerca a leer el temblor.
- **Lente.** Wide: 35 mm natural. Macros: "100mm macro, extreme close-up, shallow depth of field" (en prosa para NBP, `dabc108ffb16`).
- **Luz.** Top light cálido, duro, bordes del haz visibles en el polvo; rim en la crin; el resto negro. Ilan en silueta con dos reflejos en los lentes.
- **Color.** Ámbar de tungsteno sobre piel y barniz; negros neutros profundos; grano fino más pesado en la sombra; halación en el punto más brillante de la crin.
- **Ritmo.** 1.6 (el golpe) → 3.2 · 3.2 · 3.2 · 2.8. La escena más lenta de la pieza: la quietud es el contraste que hará leer la tormenta.

### Escena 2 — Sirocco (14.0–32.0)

- **Blocking.** Vera toca sola en el centro de la luz; los cuatro quedan como siluetas al borde del haz sin moverse. El brazo derecho de Vera cruza el cuadro en cada cambio de cuerda; la camisa se le pega a la espalda.
- **Cámara.** Push lento sobre la mandíbula de Vera (plano 7): cambió el esfuerzo. Handheld micro en el plano 8 (MS con las siluetas): es el único plano de la escena donde el cuerpo entero trabaja y la cámara respira con él. Pull leve en el plano 11 (espalda): cambió el aire, la camisa mojada revela lo que cuesta. Todo lo demás static.
- **Lente.** 85 mm para rostro y mandíbula (compresión, fondo comprimido en negro), macro para dedos y resina, 50 mm en el MS.
- **Luz.** Igual fuente. En el plano 10 (Tomás) solo un filo del violonchelo recibe luz: un specular, nada más.
- **Color.** Igual. La gota de sudor en la sien es el punto más brillante del plano 7.
- **Ritmo.** 2.4 · 2.4 · 2.0 · 2.0 · 2.4 (valle de 25 s) · 2.4 · 2.0 · 2.4.

### Escena 3 — Borea (32.0–49.2)

- **Blocking.** Los cuatro entran. Tomás aprieta el mástil; Kai golpea el arco contra las cuerdas y el contrabajo le vibra contra la cadera; Noor con la trenza saltando; Ilan inclina la cabeza. En 38.4 Vera levanta la cabeza y mira a Ilan; Ilan asiente sin dejar de tocar (eyeline declarada: Vera → Ilan; Ilan → Vera; los demás a su instrumento — familia 09 §5).
- **Cámara.** Static en los cuatro retratos de manos/cuello: cambió quién toca, no la cámara. Push en Ilan (plano 17): los reflejos de los lentes se acercan. El plano 18 es over-the-shoulder de Vera hacia Ilan, static: es el único plano de dos personas de la pieza y la cámara no lo adorna. Plano 22 (46.0–49.2): ECU static, cero blur, la crin a un milímetro de la cuerda — la respiración contenida antes de la tormenta.
- **Lente.** 85 mm en cuello y lentes; 50 mm en el over-the-shoulder; macro en el plano 22.
- **Luz.** El aro de Noor y los lentes de Ilan son los speculares de la escena. En el plano 22 la crin recibe el rim y el resto es negro.
- **Color.** Igual. Sin cambio de paleta en toda la pieza: lo que cambia es cuánta piel entra en la luz.
- **Ritmo.** 1.6 · 1.6 · 1.6 · 1.6 · 2.4 (la mirada) · 1.6 · 1.6 · 2.0 · **3.2 sostenido** (46.0–49.2).

### Escena 4 — Todos los vientos en guerra (49.2–77.45)

- **Blocking.** La formación no cambia; cambian las manos. A 61.6 s una crin del arco de Vera se rompe y queda azotando en el haz; ella no se detiene. Los cinco brazos suben a la vez en 73.6–75.2 para el último golpe.
- **Cámara.** Plano 23 (49.2–52.0): push rápido sobre Vera desde low angle, el único push rápido de la pieza — cambió el volumen 13 dB en dos segundos y la cámara lo persigue. Plano 24 (52.0): **segundo conjunto**, wide low static — el mundo entero se abre con la tormenta. Ráfagas A (54.4–56.0), B (60.8–62.4) y C (71.6–73.6): planos de 0.4–0.8 s, static salvo un whip de transición al entrar en cada ráfaga y handheld en los planos de Kai (el contrabajo golpea; la cámara recibe el golpe). Entre ráfagas, planos quietos de 2.0–2.4 s: Noor de perfil (58.4), Vera de perfil con el aliento visible (62.4, "todo se detiene menos ella"), Noor de nuevo (69.2). Plano 44 (75.2–77.4): la crin rota colgando quieta — la pausa antes del acorde final.
- **Lente.** Macro en las ráfagas, 85 mm en los perfiles, 35 mm en los dos wide.
- **Luz.** Igual fuente. El polvo es ahora denso: la luz se ve como un cuerpo. La estela de polvo detrás del arco de Kai (plano 34) es el cue de velocidad: partial blur en el arco, torso nítido (familia 09 §3).
- **Color.** Igual. Prohibido subir saturación en la tormenta: la intensidad la da el corte.
- **Ritmo.** 2.8 · 2.4 · **0.8 · 0.8** · 1.2 · 1.2 · 2.4 (quieto) · **0.4 · 0.4 · 0.8** (quiebre) · 2.0 (quieto) · 1.2 · 1.2 · 1.2 · 1.2 · 2.4 (quieto) · **0.4 · 0.4 · 0.4 · 0.8** · 1.6 · **2.2 sostenido**.

### Escena 5 — Quest'è 'l verno (77.45–82.15)

- **Blocking.** Último acorde: los cinco arcos se detienen a la misma altura y se quedan en el aire. Nadie se mueve; los pechos suben y bajan a la vez; una gota cae de la barba de Ilan. La mano de Vera se abre; el arco baja hasta la cuerda.
- **Cámara.** Plano 45 (77.4–80.0): **tercer conjunto**, wide frontal eye-level static — todas las caras legibles (familia 09 §5), cinco identidades verificables contra sus maestros. Plano 46 (80.0–82.15): ECU static sobre la mano de Vera. Ningún movimiento: el fin es consecuencia, no explicación (`animatic-keyframes.md` §3, aftermath).
- **Lente.** 35 mm el wide, macro la mano.
- **Luz.** Igual. El polvo que termina de caer es lo último que se mueve.
- **Ritmo.** 2.6 · 2.15. Corte a negro con la cola sonora.

## 4. Los tres detalles, por escena (auditoría U12 antes del storyboard)

| Escena | Presión ambiental | Micro-acción física | Motivo/ancla sonora |
|---|---|---|---|
| 1 | el haz cálido rodeado de negro | nudillos blancos en el talón; el tremolo del arco de Ilan | polvo de resina en el haz |
| 2 | siluetas inmóviles al borde de la luz | yemas blanqueadas; mandíbula trabada; camisa pegada | resina saltando en cada acento |
| 3 | el polvo se vuelve más denso | vena del cuello de Noor; nudillos de Tomás; el asentimiento de Ilan | el aro y los lentes como speculares |
| 4 | la luz se ve como un cuerpo sólido | la crin que se rompe; la mano que no se detiene; el aliento visible | la crin suelta azotando en el haz |
| 5 | el silencio con el polvo aún cayendo | la mano que se abre; los pechos que respiran a la vez | el arco que baja hasta la cuerda |

## 5. Gate de la Etapa 3

- Vocabulario prohibido: 0 ocurrencias (verificado con grep sobre este archivo antes de avanzar).
- Cada movimiento de cámara lleva su "qué cambió" escrito: sí (sección 3).
- Fuente de luz: una, motivada por el propio escenario (stage top light), repetida verbatim en el `series_lock`.
