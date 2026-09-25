#!/usr/bin/env python3
"""Genera output/ del storyboard (Etapa 4) para "Anatomía del frío" desde una lista de shots
declarada aquí, atada al análisis medido de la grabación (audio-analisis.json).

Reproducible: python3 gen_storyboard.py  → output/{shots.json, text-overlays.json,
brand-lock.snapshot.md, storyboard.md, run.json}. Los tiempos son múltiplos de 0.4 s (pulso
medido ≈150 bpm) y los tres planos de quinteto caen en los tres eventos más fuertes medidos
(0.0 s, 52.0 s, 77.45 s). Si cambia la grabación, se editan start/end aquí, no los prompts.
"""
import hashlib, json, os, secrets, shutil
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "output"
SHOTKIT = Path("/root/.claude/skills/synced/66f050bc-c2fd-464b-a5c9-e5a53a1b4bd5_7864280b-d059-4109-8ad2-9cdd67e16a32/storyboard-architect")
DUR = 82.15

SERIES_LOCK = {
    "character": (
        "Five string players, all in matte black clothing so only skin and instrument varnish return light, "
        "all right-handed (instrument on the left, bow in the right hand). "
        "VERA, first violin, 34: very short black hair with a shaved nape, a thin scar cutting the left eyebrow, "
        "a nose with a visible bridge bump, black linen shirt rolled to the elbow, defined forearms. "
        "ILAN, second violin, 41: receding hairline, short grey beard, thin metal-rimmed glasses, black jacket, no tie. "
        "NOOR, viola, 28: long dark braid over the right shoulder, small gold nose ring on the left nostril, "
        "sleeveless black high-neck dress. "
        "TOMAS, cello, 52, seated: long white hair tied at the nape, large hands with knobby knuckles, "
        "open black waistcoat over a black shirt. "
        "KAI, double bass, 30, standing: tall, shaved head, fine-line geometric tattoo on the right forearm, "
        "fitted black t-shirt. Each identity is a canonized master (T1 face + T2 body) inserted one at a time."
    ),
    "environment": (
        "Bare black stage with no visible back wall, dark matte floor with white gaffer-tape marks at the feet of "
        "each of five black music stands set in an open arc: Vera front-left, Ilan front-right, Noor centre-back, "
        "Tomas seated back-left, Kai standing back-right. Rosin dust hangs in the air. Nothing else on stage, no audience."
    ),
    "lighting": (
        "One hard warm tungsten top light, slightly frontal, from above the quintet; beam edges visible in the rosin "
        "dust; no fill; everything outside the beam falls to black with no detail; one hard specular highlight on skin, "
        "bow hair and varnish; fine film grain heaviest in the shadows, soft halation on the brightest highlight."
    ),
    "color_grade": (
        "Warm amber tungsten on skin and varnish, deep neutral blacks with no teal or blue push, natural contrast, "
        "no HDR look, no added saturation; the palette never changes across the piece, only how much skin enters the light."
    ),
}

# (start, end, framing, angle, motion, dof, subject, rationale, beat)
SHOTS = [
    # Escena 1 — Puertas cerradas (0.0–14.0): golpe inicial, luego murmullo bajo
    (0.0, 1.6, "WS", "eye-level", "static", "deep",
     "The full quintet inside the single warm beam, five bows landing on the strings at once, rosin dust bursting up from the strings, white tape marks at their feet, black beyond the beam",
     "El único golpe fuerte del arranque (0.0 s, -22 dBFS) abre el mundo entero de una vez; el plano fuerte va ancho y no volverá a serlo hasta el segundo 52.", "puertas-cerradas"),
    (1.6, 4.8, "ECU", "eye-level", "static", "shallow",
     "Bow hair under tension with one loose hair separating and whipping, rosin dust drifting down through the warm beam onto it, black behind",
     "La música cae 17 dB en un segundo: el plano quieto va cerrado; el objeto ancla (la crin suelta) y el motivo (la resina) se presentan en el primer silencio.", "puertas-cerradas"),
    (4.8, 8.0, "CU", "eye-level", "static", "shallow",
     "Vera's right hand closed on the frog of the bow, knuckles whitening, one vein raised on the back of the hand, warm light carving the tendons, rest of frame black",
     "Primera anatomía en decisión (agarre): la resistencia se instala en la mano antes de que exista un rostro.", "puertas-cerradas"),
    (8.0, 11.2, "MCU", "eye-level", "push", "shallow",
     "Ilan in profile as a black silhouette at the edge of the beam, two warm reflections on his glasses, his bow trembling in a low tremolo rendered as a slight blur while his head stays sharp",
     "El tremolo grave del tramo 1-14 s es lo único que se mueve; la cámara se acerca despacio a leer ese temblor (qué cambió: el arco empezó a vibrar).", "puertas-cerradas"),
    (11.2, 14.0, "CU", "eye-level", "static", "shallow",
     "Tomas's left hand gripping the cello neck, knobby knuckles whitening, a white tape mark on the dark floor soft in the background",
     "Cierra la escena presentando la marca de cinta blanca (ancla de posición para la inserción) mientras la presión sigue subiendo en una mano.", "puertas-cerradas"),
    # Escena 2 — Sirocco (14.0–32.0): el violín solo
    (14.0, 16.4, "ECU", "eye-level", "static", "shallow",
     "Vera's left-hand fingertips running on the fingerboard, pads flattened and blanched against the strings, tendons rising on the back of the hand",
     "Los agudos dominan desde 14 s (60 % de la energía > 2 kHz): la solista entra por sus dedos, no por su cara.", "sirocco"),
    (16.4, 18.8, "MCU", "eye-level", "push", "shallow",
     "Vera's jaw locked, one bead of sweat catching the top light on her temple, the scar through her left eyebrow deepening as she presses, black behind",
     "Cambió el esfuerzo: el push lento se acerca a la mandíbula trabada y a la gota, los dos speculares del plano.", "sirocco"),
    (18.8, 20.8, "MS", "eye-level", "handheld", "deep",
     "Vera waist-up, right arm crossing the frame on a string change, shirt darkening with sweat at the back, four black silhouettes motionless at the edge of the beam behind her",
     "Único plano de la escena con el cuerpo entero trabajando; el handheld micro respira con el brazo (un solo movimiento).", "sirocco"),
    (20.8, 22.8, "ECU", "eye-level", "static", "shallow",
     "Rosin dust leaping off the bow hair at the moment of an accent and hanging in the warm beam, bow edge sharp, dust as a constellation of specular points",
     "El acento de 21-22 s se rinde como consecuencia física: la resina salta; el motivo se ata al ritmo.", "sirocco"),
    (22.8, 25.2, "CU", "eye-level", "static", "shallow",
     "The f-hole edge of Tomas's cello catching a single warm specular, the rest of the instrument and Tomas in black silhouette",
     "Valle de 25 s (-41 dBFS): el plano más oscuro de la escena, un solo brillo; loud only works next to quiet.", "sirocco"),
    (25.2, 27.6, "MCU", "eye-level", "pull", "shallow",
     "Vera from behind, the black linen shirt clinging wet to her back, shoulder blades working, the beam edge cutting across her",
     "Cambió el aire: la camisa mojada revela el costo; el pull leve abre para ver la espalda entera.", "sirocco"),
    (27.6, 29.6, "ECU", "eye-level", "static", "shallow",
     "Vera's fingertip pads blanched white against the string, nail edges pressing, one string vibrating to a blur beside a sharp one",
     "Segunda subida de agudos (28-30 s): la precisión se muestra en las yemas, con blur parcial solo en la cuerda.", "sirocco"),
    (29.6, 32.0, "MS", "low", "static", "shallow",
     "Vera in profile from a low angle, bow raised at the top of a stroke, chest expanded, four silhouettes behind at the edge of the light",
     "Cierre de Sirocco: el ángulo bajo da poder a la solista un instante antes de que el tutti responda.", "sirocco"),
    # Escena 3 — Borea (32.0–49.2): responden los cuatro; respiración contenida al final
    (32.0, 33.6, "CU", "eye-level", "static", "shallow",
     "Tomas's left hand on the cello neck, knuckles whitening, a vein crossing the forearm, warm light on the back of the hand",
     "Salto de nivel medido en 32.0-32.5 s: el tutti entra por la mano de Tomás.", "borea"),
    (33.6, 35.2, "CU", "eye-level", "handheld", "shallow",
     "Kai's right hand dropping the bow onto the double-bass strings, the geometric tattoo on his forearm tensing and slackening, the bass body vibrating against his hip",
     "El golpe del contrabajo se recibe en cámara: handheld como único movimiento del plano.", "borea"),
    (35.2, 36.8, "CU", "eye-level", "static", "shallow",
     "Noor's neck with a vein standing out, the dark braid jumping on her right shoulder, the gold nose ring returning one point of light",
     "Tercera voz del tutti; el aro es el specular del plano.", "borea"),
    (36.8, 38.4, "MCU", "eye-level", "push", "shallow",
     "Ilan's glasses catching the top light as two warm reflections moving with his head, grey beard shining with sweat",
     "Cuarta voz; el push acerca los reflejos que se mueven (qué cambió: la cabeza se inclina con el fraseo).", "borea"),
    (38.4, 40.8, "MS", "eye-level", "static", "shallow",
     "Over Vera's shoulder toward Ilan: Vera lifts her head and looks at Ilan, Ilan nods once without stopping, both bows in motion",
     "Subida medida en 39-40 s: el único plano de dos personas de la pieza fija la eyeline Vera→Ilan, Ilan→Vera.", "borea"),
    (40.8, 42.4, "ECU", "eye-level", "static", "shallow",
     "The shaved nape of Kai's head with one drop of sweat running down it, warm rim on the skin, black behind",
     "Cuerpo al límite sin rostro: la gota en la nuca es el indicador de estado.", "borea"),
    (42.4, 44.0, "CU", "eye-level", "static", "shallow",
     "Noor's hands on the viola, left fingers stopping the strings, right hand mid-stroke with the bow hair slightly blurred",
     "Manos de la viola con blur parcial solo en el arco; torso nítido.", "borea"),
    (44.0, 46.0, "MCU", "eye-level", "push", "shallow",
     "Vera's face in three-quarter, mouth slightly open, her breath visible as vapour in the cold air of the beam",
     "Subida medida en 44.5 s y luego caída: el aliento visible prepara la respiración contenida.", "borea"),
    (46.0, 49.2, "ECU", "eye-level", "static", "shallow",
     "Vera's bow hair held one millimetre above the string, absolutely still, zero blur, rosin dust falling slowly through the warm beam",
     "El punto más bajo de toda la grabación (46-49 s, -44.5 dBFS): la pausa obligatoria antes del corte más grande, quietud total.", "borea"),
    # Escena 4 — Todos los vientos en guerra (49.2–77.45)
    (49.2, 52.0, "MS", "low", "push", "shallow",
     "Vera from a low angle, bow rising to strike, shirt clinging, the beam behind her head, dust thickening",
     "La grabación sube 13 dB en dos segundos (49-52 s): el único push rápido de la pieza persigue esa subida.", "guerra"),
    (52.0, 54.4, "WS", "low", "static", "deep",
     "The full quintet from a low angle, five right arms at the same angle, five bows coming down together, rosin dust exploding into the beam so the light reads as a solid body",
     "La tormenta se abre (52.05 s, primer tramo fuerte): segundo plano de conjunto, ancho y bajo.", "guerra"),
    (54.4, 55.2, "ECU", "eye-level", "whip", "shallow",
     "Bow hair and rosin dust bursting in the beam, the whole frame raked into motion streaks with the bow edge surviving",
     "Ráfaga A entra con el acento de 54.65 s; el whip es la transición, no un movimiento apilado.", "guerra"),
    (55.2, 56.0, "CU", "eye-level", "static", "shallow",
     "Tomas's knuckles white on the cello neck, tendons raised, warm light hard on the hand",
     "Segundo panel de la ráfaga A: anatomía en decisión (agarre máximo).", "guerra"),
    (56.0, 57.2, "CU", "eye-level", "handheld", "shallow",
     "Kai's bow striking the bass strings, the forearm tattoo tensing, the instrument shaking against his hip, dust trailing the bow",
     "Acentos de 56.2 y 56.55 s: el golpe del contrabajo, cámara sacudida por el golpe.", "guerra"),
    (57.2, 58.4, "ECU", "eye-level", "static", "shallow",
     "A single string vibrating until it blurs into a band of light, the neighbouring string sharp, warm rim on both",
     "Cierra la ráfaga A con la cuerda borrada: blur parcial como prueba de un solo instante.", "guerra"),
    (58.4, 60.8, "MCU", "eye-level", "static", "shallow",
     "Noor in profile, vein on the neck, braid resting still on her shoulder, her bow arm sharp",
     "Valle medido 58.3-60.65 s: el plano quieto obligatorio entre dos ráfagas.", "guerra"),
    (60.8, 61.2, "ECU", "eye-level", "static", "shallow",
     "The frog of Ilan's bow gripped hard, thumb pressing white, warm specular on the ferrule",
     "Ráfaga B, acento 60.8 s.", "guerra"),
    (61.2, 61.6, "ECU", "eye-level", "static", "shallow",
     "Vera's fingertips slamming down on the fingerboard, pads blanched",
     "Ráfaga B, acento 61.05-61.15 s.", "guerra"),
    (61.6, 62.4, "CU", "eye-level", "static", "shallow",
     "One hair of Vera's bow snapping mid-stroke and whipping loose in the warm beam, her right hand not stopping, the hand sharp and the loose hair blurred",
     "El quiebre: la crin se rompe y la mano no se detiene; el objeto ancla cruza su umbral.", "guerra"),
    (62.4, 64.4, "MCU", "eye-level", "static", "shallow",
     "Vera's face in profile, motionless, mouth open, breath visible in the cold beam, rosin dust falling in front of her",
     "Valle 61.55-63.55 s: todo se detiene menos ella; el segundo plano quieto entre ráfagas.", "guerra"),
    (64.4, 65.6, "CU", "eye-level", "handheld", "shallow",
     "Kai's bow leaving a trail of rosin dust behind it in the beam, forearm tattoo sharp, bow hair blurred",
     "Tramo fuerte 63.55-64.5 s: la estela de polvo es el cue de velocidad (blur solo en el arco).", "guerra"),
    (65.6, 66.8, "ECU", "high", "static", "shallow",
     "Tomas's shoe planted on the white gaffer-tape mark on the dark floor, the cello endpin beside it, dust settling in the light",
     "Ángulo alto porque el sujeto es el piso: el pie clavado en la marca dice que el cuerpo no cede.", "guerra"),
    (66.8, 68.0, "MS", "low", "push", "shallow",
     "Ilan from a low angle, right arm driving the bow, glasses flaring warm, jacket pulling at the shoulder",
     "Tramo fuerte 65.75-69.4 s: el push bajo sube la presión hacia el acento de 69.1 s.", "guerra"),
    (68.0, 69.2, "ECU", "eye-level", "static", "shallow",
     "The loose broken hair of Vera's bow tangling around the tip and whipping free again, warm rim on the hair, black behind",
     "Acento 69.1 s: el objeto ancla en su nuevo estado (roto) sigue trabajando.", "guerra"),
    (69.2, 71.6, "MCU", "eye-level", "static", "shallow",
     "Noor's hands on the viola with her face low over the instrument, braid forward, one drop of sweat on the bridge of her nose",
     "Valles 69.4-70.1 y 70.95-71.7 s: tercer plano quieto antes de la carrera final.", "guerra"),
    (71.6, 72.0, "ECU", "eye-level", "whip", "shallow",
     "Bow hair and dust raked into streaks, bow tip surviving sharp",
     "Ráfaga C entra en 71.7 s con el primer acento de la carrera final (71.95 s).", "guerra"),
    (72.0, 72.4, "ECU", "eye-level", "static", "shallow",
     "Tomas's knuckles white on the neck, one vein raised",
     "Acento 72.2 s.", "guerra"),
    (72.4, 72.8, "ECU", "eye-level", "static", "shallow",
     "Kai's shaved nape, sweat running, muscles of the neck tight",
     "Acento 72.4-72.6 s.", "guerra"),
    (72.8, 73.6, "CU", "eye-level", "static", "shallow",
     "Vera's jaw clenched hard, scar deepening, sweat on the temple, hair plastered at the nape",
     "Acento 72.8 s: el rostro llega tarde y poco, como recompensa dentro de la ráfaga.", "guerra"),
    (73.6, 75.2, "MS", "low", "push", "deep",
     "The five right arms rising together for the final stroke, bows at the top, dust dense in the beam, five bodies leaning in",
     "Los cinco brazos suben a la vez: el push bajo acompaña la única subida colectiva antes del acorde final.", "guerra"),
    (75.2, 77.4, "ECU", "eye-level", "static", "shallow",
     "The broken bow hair hanging still from the frog against the warm beam, zero blur, dust falling slowly",
     "Valle medido 75.45-77.45 s: la pausa antes del último golpe, quietud total sobre el objeto ancla.", "guerra"),
    # Escena 5 — Quest'è 'l verno (77.45–82.15)
    (77.4, 80.0, "WS", "eye-level", "static", "deep",
     "The full quintet from the front at eye level, five bows stopped in the air at the same height after the last chord, five chests rising and falling together, all five faces legible, rosin dust still falling through the beam",
     "Acorde final (77.45-78.4 s): tercer plano de conjunto, frontal y a nivel de ojos para que las cinco identidades se lean y se verifiquen contra sus maestros.", "quest-e-l-verno"),
    (80.0, 82.15, "ECU", "eye-level", "static", "shallow",
     "Vera's right hand opening, the bow dropping a few millimetres onto the string and resting there, the broken hair hanging still from the frog, the last rosin dust settling",
     "Imagen final sobre la cola sonora: la mano se abre, el arco descansa, el polvo termina de caer; consecuencia, no explicación.", "quest-e-l-verno"),
]


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    OUT.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    shots = []
    for i, (s, e, fr, an, mo, dof, subj, rat, beat) in enumerate(SHOTS, 1):
        shots.append({
            "id": f"shot_{i:02d}", "beat": beat, "start": s, "end": e, "framing": fr, "angle": an,
            "motion": mo, "depth_of_field": dof, "subject": subj,
            "environment_ref": "series_lock.environment", "lighting_ref": "series_lock.lighting",
            "on_screen_text": None, "vo": None, "rationale": rat,
        })
    # contigüidad y duración total, antes del validador
    assert abs(shots[0]["start"]) < 1e-9 and abs(shots[-1]["end"] - DUR) < 1e-9
    for a, b in zip(shots, shots[1:]):
        assert abs(a["end"] - b["start"]) < 1e-9, (a["id"], b["id"])

    shots_doc = {
        "version": "1.2",
        "project": {"title": "Anatomía del frío — Vivaldi, L'inverno III (cierre)", "duration_s": DUR,
                    "aspect": "16:9", "framework": "Custom (music-driven; loudness = shot count)"},
        "brand_lock_ref": "brand-lock.snapshot.md",
        "series_lock": SERIES_LOCK,
        "shots": shots,
    }
    (OUT / "shots.json").write_text(json.dumps(shots_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "text-overlays.json").write_text(json.dumps({"version": "1.0", "overlays": []}, indent=2) + "\n", encoding="utf-8")

    brand_src = AQUI / "brand-lock.md"   # Visual Theme ligero (sustituto de Etapa 0 sin marca)
    snapshot = (f"<!-- snapshot taken: {now} -->\n<!-- source: produccion/vivaldi-invierno/brand-lock.md -->\n"
                + brand_src.read_text(encoding="utf-8"))
    (OUT / "brand-lock.snapshot.md").write_text(snapshot, encoding="utf-8")

    # storyboard.md desde la plantilla, renderizada aquí
    lines = [f"# {shots_doc['project']['title']}", "",
             "| | |", "|---|---|", f"| **Duration** | {DUR}s |", "| **Aspect** | 16:9 |",
             f"| **Beat framework** | {shots_doc['project']['framework']} |",
             "| **Brand lock** | [`brand-lock.snapshot.md`](./brand-lock.snapshot.md) |",
             f"| **Generated** | {now} |", "", "---", "", "## Brief", "",
             "Video musical de 82.15 s: quinteto de cuerdas (identidades inventadas, canonizadas) tocando el cierre del "
             "III Allegro de *L'inverno*. Concepto ganador: **Anatomía del frío** — la pieza se cuenta desde manos, arcos, "
             "cuellos y respiración; el quinteto completo aparece tres veces, en los tres eventos más fuertes medidos de la "
             "grabación (0.0 s, 52.0 s, 77.45 s). Sin diálogo, sin texto en pantalla, sin público.", "",
             "## Beat framework: Custom", "",
             "**Why custom:** los frameworks estándar sirven a conversión, producto o explicación; aquí la estructura la dicta la "
             "grabación (`audio-analisis.json`): la densidad de corte sigue al volumen medido y los cortes caen en el pulso (0.4 s).", "",
             "**Beats:**", "1. puertas-cerradas, presión que sube en voz baja, 0.0–14.0 s",
             "2. sirocco, el violín solo, 14.0–32.0 s", "3. borea, responden los cuatro y se contiene la respiración, 32.0–49.2 s",
             "4. guerra, tormenta en ráfagas separadas por planos quietos, 49.2–77.4 s",
             "5. quest-e-l-verno, acorde final y consecuencia, 77.4–82.15 s", "", "## Series lock", "", "| | |", "|---|---|"]
    for k, label in (("character", "Character anchor"), ("environment", "Environment"), ("lighting", "Lighting"), ("color_grade", "Color grade")):
        lines.append(f"| **{label}** | {SERIES_LOCK[k]} |")
    lines += ["", "---", "", "## Shots", ""]
    for sh in shots:
        lines += [f"### {sh['id']} · {sh['start']}–{sh['end']}s · {sh['framing']} · {sh['motion']}", "",
                  f"**Beat:** {sh['beat']}", "", f"**Angle / DOF:** {sh['angle']} · {sh['depth_of_field']}", "",
                  f"**Subject:** {sh['subject']}", "", "**On-screen text:** none", "", "**VO:** none", "",
                  f"**Rationale:** {sh['rationale']}", "", "---", ""]
    lines += ["## Text overlays", "", "Ninguno. Créditos, si los hay, van en post fuera de este storyboard.", "", "---", "",
              "## Handoff notes", "",
              "- **For image generation:** run `visual-prompt-forge` against `shots.json` (anclas NBP; ver 01-estrategia.md, decisión por regla)",
              "- **For HTML preview:** run `storyboard-html-preview` against this folder",
              "- **For QA on generated frames:** run `visual-asset-critic` with the generated image and the shot ID", "",
              "## Audit trail", "",
              f"Generado contra `brand-lock.snapshot.md` (plantilla sin configurar, congelada en {now}) y contra "
              "`../audio-analisis.json` (medición de la grabación entregada por Eric el 2026-09-25)."]
    (OUT / "storyboard.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    run = {
        "version": "1.0",
        "run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + secrets.token_hex(4),
        "created_at": now, "shotkit_version": "3.0.0",
        "project": {"title": shots_doc["project"]["title"], "duration_s": DUR, "aspect": "16:9"},
        "inputs": {
            "shots_ref": "shots.json", "shots_sha256": sha256(OUT / "shots.json"),
            "text_overlays_ref": "text-overlays.json", "text_overlays_sha256": sha256(OUT / "text-overlays.json"),
            "brand_lock_ref": "brand-lock.snapshot.md", "brand_lock_sha256": sha256(OUT / "brand-lock.snapshot.md"),
            "brand_lock_source": "produccion/vivaldi-invierno/brand-lock.md",
        },
        "rounds": [],
    }
    (OUT / "run.json").write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"output/: {len(shots)} shots · {DUR}s · run_id {run['run_id']}")


if __name__ == "__main__":
    main()
