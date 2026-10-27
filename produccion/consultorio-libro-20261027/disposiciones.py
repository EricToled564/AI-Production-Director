"""disposiciones.py: escribe disposiciones.json, la disposición CHECK o NA de cada enunciado de reg_image.json y
reg_produccion-visual-sw30.json para este caso (SW30 §Sistema de cobertura). Las NA por archivo valen solo para
archivos cuyo alcance entero no es este caso; cada una dice por qué."""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
C = "construir.py"
POR_ID = {
 # produccion-visual-sw30/SKILL.md
 "dadff5459383": ("CHECK", "pregunta de avance respondida en la entrega, después de este ledger"),
 "a4a34906e54d": ("CHECK", "rule_ledger.py con 0 PENDING antes de entregar; si no, no se entrega"),
 "ab216a6c933f": ("CHECK", "pregunta de avance respondida tras ledger y auditor en verde"),
 "5c17fa63163e": ("CHECK", "pregunta de avance respondida sí/no, sin matices"),
 "241ea833ab9d": ("CHECK", "LECTURAS.md: archivos aplicables leídos completos, con su registro"),
 "26da6aecb6fb": ("CHECK", f"{C}: catalogar (T5/T3), secciones y ensamblado por template_engine"),
 "87eadbf796d1": ("CHECK", f"{C}: tipo T5 (paso 1) y T3 (pasos 2 y 3) según herramientas/RULES_MATRIX.md"),
 "d48021c639e6": ("CHECK", f"{C}: secciones del tipo y bloques nombrados anatomy, idlock, optics_deep"),
 "4a2eeac6c89d": ("CHECK", f"{C}: build() de template_engine; salida Model/Quality/Size, referencias, Prompt y Notes"),
 "6658223ecd3e": ("CHECK", "reg_image.json y reg_produccion-visual-sw30.json extraídos con rule_registry.py en este turno"),
 "3348210ad98e": ("CHECK", "rule_ledger.py sobre disposiciones.json"),
 "b37aa531231e": ("CHECK", f"{C}: audit_gi2.audit() por paso; falla si una columna da FAIL"),
 "d5b415caa2cd": ("NA", "bloque light_hard del maestro de rostro T1; aquí no se genera rostro maestro: los rostros vienen "
                        "de referencias y la luz es la de Image 7 por dirección de Eric"),
 "5a5348b20c81": ("NA", "bloque usecase_doc del maestro de rostro T1; no hay maestro de rostro en este caso"),
 "7ba769efe2d7": ("CHECK", f"{C}: los tres prompts salen de template_engine.build"),
 "c0bc3ce2b122": ("CHECK", f"{C}: build(tipo, ..., notes=...)"),
 "f75cfcf75330": ("CHECK", f"{C} --probar: «sección obligatoria vacía» lanza TemplateViolation"),
 "ed3f4a2ab62f": ("CHECK", f"{C}: anatomy, idlock y optics llegan como Block; template_engine rechaza texto suelto"),
 "ca17e7d8bf24": ("CHECK", f"PROMPTS.txt se regenera solo desde {C}; no se edita a mano"),
 "a36cebf95d83": ("NA", "no se genera ni se gastan créditos desde aquí: Eric genera en la app"),
 "5cf46d07bcac": ("CHECK", f"{C}: tres pasos, un sujeto por paso; audit_gi2 single_job=PASS con jobs=1"),
 "613774db48c2": ("CHECK", f"{C} verificar(): rechaza left half, centre, central, just left of; posiciones por cuadro, "
                           "puerta abierta, escritorio y borde inferior de Image 1"),
 "762ce60bec5e": ("CHECK", f"{C} verificar(): paso 1 exige verbo operativo y rechaza again / has become"),
 "cb50b580f819": ("CHECK", f"{C} verificar(): toda Image N citada tiene su imagen adjunta en ese paso"),
 "ff510d7ca127": ("CHECK", "las referencias dan rostro, pelo, lentes, aretes y complexión; el texto solo describe los "
                           "deltas: vestuario, pose, mirada y posición (revisión manual registrada en NOTAS.md)"),
 "4fcb4afa54c3": ("NA", "no hay swap de identidad: las personas se insertan, no se reemplazan"),
 "4d4ea0758b3f": ("CHECK", f"{C} verificar(): pasos 2 y 3 llevan use only the person from Images 2 and 3, ignore their "
                           "setting y keep the world of Image 1 untouched; el paso 1 prepara el mundo antes"),
 "b6df20344be1": ("CHECK", f"{C} verificar(): exige frozen y rechaza moving, moves, walking, in motion"),
 "7dc14c265b1a": ("NA", "no hay contacto entre personas: la mano de la doctora toca el libro, no a la pareja"),
 "204113433c22": ("CHECK", "el nombre dorado del libro queda bajo la mano: no se genera lettering; ningún logo"),
 "0895bf9c3c72": ("CHECK", "cada paso parte de la imagen aprobada del anterior (NOTAS.md: guardar su sha256 al aprobar)"),
 "3f9822c97a3a": ("CHECK", "NOTAS.md: un paso correcto al 80 % se corrige con una edición puntual, no se re-tira"),
 "f9fee85351f3": ("CHECK", "NOTAS.md: máximo 2 intentos por paso; después, cambio de método con causa o consulta"),
 "0aad9d5a3dfa": ("CHECK", f"{C}: audit_gi2 y techo de 300 palabras en verde; NOTAS.md: zoom al 100 % de rostros y manos "
                           "antes de pasar al paso siguiente"),
 "aeb5f5e9292c": ("NA", "esta pieza no tiene shots.json; la fuente es el texto de Eric (BRIEF.md)"),
 "2dddf6f48ba3": ("NA", "regla de clips de video; aquí son stills"),
 "44283e478fd4": ("CHECK", "entrega en tres pasos, cada uno aprobable por separado"),
 "84846df151fa": ("CHECK", "la entrega abre con la cabecera obligatoria y después el entregable"),
 "6da8440e93ad": ("CHECK", "límites citados solo de gpt-image.md leído en este turno (hasta 16 referencias, tamaños)"),
 "f502856eb05e": ("NA", "no se usa /research, /briefing ni /handoff"),
 # image/SKILL.md
 "11ea00e863de": ("CHECK", "LECTURAS.md: models.md, gpt-image.md, golden-rules.md, characters.md, creative-direction.md, "
                           "prompt-framework.md y patterns/portrait-cinema.md leídos completos"),
 "3f921ee68519": ("NA", "no es movimiento ni clip"),
 "0358891ec685": ("NA", "el modelo es GPT Image 2 (alcance de las reglas, CLAUDE.md)"),
 "c5eb6fd7f6f8": ("CHECK", f"{C} verificar(): cinco slots en orden (GPT2-GEN) y Change/Preserve/Constraints (GPT2-EDIT)"),
 "485206c1697b": ("CHECK", f"{C} verificar(): verbo en Scene, hex en colores nuevos, sin texto que citar, un cambio por "
                           "paso, referencias con rol"),
 "67a7dd9329dc": ("CHECK", "el paso 1 lleva lista Preserve explícita"),
 "890a0b28f120": ("CHECK", "hex en los colores nuevos y materiales concretos (lana-cachemira, merino, punto, lino)"),
 "0e7900ffe2af": ("CHECK", "audit_gi2 anti_slop y framing_positive en PASS; sin comparaciones externas"),
 # creative-direction.md
 "09ec7d23fe12": ("NA", "no se nombra cámara: la toma la fija Image 7"),
 "b921448eda9a": ("NA", "el encuadre lo fija la posición de cámara de Image 7"),
 "b8fa85d560e3": ("NA", "la dirección pide deep focus, no profundidad de campo corta"),
 "5ad1340da288": ("CHECK", "foco descrito como deep focus, sin números de diafragma"),
 "862a4c0ea3bc": ("CHECK", "vestuario descrito por su material: lana-cachemira, merino, punto acanalado"),
 # golden-rules.md
 "d9bcca3cf113": ("CHECK", "audit_gi2 framing_positive=PASS; restricciones en positivo salvo los límites del slot Constraints"),
 "1dd54b582a02": ("CHECK", "se describe lo presente: la silla queda vacía, solo la pareja y la mano en cuadro"),
 "7fff008d0b4a": ("CHECK", "ídem: formulación en positivo"),
 "f5bdd52eae18": ("CHECK", "ídem: «only the couple and the doctor's hand in frame»"),
 "cc4167f1d432": ("CHECK", "gate_image R4 (keyword soup) en la entrega; el prompt es prosa"),
 "8d02f99b51e9": ("CHECK", "ídem: frases completas"),
 "8901152207fe": ("CHECK", "Use Case da el contexto: fotograma clave de una película"),
 "dd9305290d20": ("CHECK", "cada referencia con su rol en el slot (golden-rules.md, Reference Images)"),
 "04c28ccbddf9": ("NA", "no se usa ancla de época, cultura ni género: el mundo lo fija Image 7"),
 "3db8f42e251f": ("NA", "ídem"),
 "16ec02525ce7": ("NA", "ídem"),
 "47652229b5ab": ("NA", "ídem"),
 # gpt-image.md
 "1848820351ae": ("CHECK", "requisitos funcionales dichos de forma directa (only the couple..., five fingers...)"),
 "20e10fa23ffc": ("NA", "no hay texto en cuadro; quality high se pide por identidad (gpt-image.md:45–47)"),
 "26e0c5fc6ab4": ("NA", "no es remoción de objeto"),
 "822ae545689f": ("NA", "no se usa ancla de conocimiento del mundo"),
 # models.md
 "c10c7e21ff29": ("CHECK", f"{C} verificar(): cinco slots"),
 # prompt-framework.md
 "e3f6e1ce49a2": ("CHECK", "sujeto y contexto presentes en cada paso"),
 "c8d4fff1dabe": ("CHECK", "colores nuevos con hex"),
 "58817d380494": ("NA", "regla de Nano Banana"),
 "85e2a5dc4aa8": ("CHECK", "formulación positiva (audit_gi2 framing_positive)"),
 "5856058c8a75": ("NA", "no se usa plantilla parametrizada"),
 "84828d3c69a2": ("NA", "ídem"),
 "a90636943228": ("CHECK", "los pasos 2 y 3 comparten la misma estructura de slots"),
 "8005da81a345": ("NA", "no es generación en lote"),
 "42a42a73fa09": ("NA", "desgaste de superficies heredado de Image 7; no se redescribe (SW30 regla 5)"),
 "4bc498edcc17": ("CHECK", "poros visibles, tejido de lana y punto"),
 "bc6d5c9aff5f": ("NA", "partículas atmosféricas: la luz y el aire son los de Image 7"),
 "318b118d917d": ("NA", "especulares del mármol heredados de Image 7"),
 "92eeb4747a7e": ("NA", "caída de la tela la dan la pose sentada y el saco abierto; no se añade más texto para no pasar el techo"),
 "51b0bfedb210": ("CHECK", "sombra de contacto mano-libro y libro-mármol en el paso 1"),
 "329aa0a4fa84": ("NA", "reflejos del entorno heredados de Image 7"),
 "11ec80431f42": ("CHECK", "instante congelado nombrado: frozen mid-reach"),
 # storyboards.md
 "c9068adfe734": ("CHECK", "identidad sostenida entre pasos: idlock en cada inserción y keep the world of Image 1 untouched"),
 "3244bb3011e7": ("NA", "no es secuencia de viñetas"),
 # vision-decomposer.md: solo imagen a prompt
}
POR_ARCHIVO = {
 "references/multi-panel.md": "no es una composición de varios paneles",
 "references/nano-banana.md": "el modelo es GPT Image 2",
 "references/patterns/character-design.md": "patrón de hoja de personaje; aquí es un fotograma de película",
 "references/patterns/ecommerce.md": "patrón de producto para comercio electrónico",
 "references/patterns/fashion-editorial.md": "patrón de campaña de moda",
 "references/patterns/food-beverage.md": "patrón de alimentos y bebidas",
 "references/patterns/poster-illustration.md": "patrón de póster o ilustración",
 "references/patterns/ui-social.md": "patrón de UI o redes",
 "references/patterns/portrait-cinema.md": "plantillas de retrato (contraluz callejero, neón, glitch, película japonesa, "
                                           "subacuático) que no son esta escena de interior con luz de Image 7",
 "references/slides.md": "no son diapositivas",
 "references/structural.md": "no hay boceto ni wireframe de entrada",
 "references/text-rendering.md": "no hay texto en cuadro",
 "references/vision-decomposer.md": "no es análisis de imagen a prompt",
}
disp = {}
for s in ("image", "produccion-visual-sw30"):
    for r in json.loads((AQUI / f"reg_{s}.json").read_text(encoding="utf-8"))["rules"]:
        if r["id"] in POR_ID:
            st, txt = POR_ID[r["id"]]
            disp[r["id"]] = {"status": st, ("by" if st == "CHECK" else "reason"): txt}
        elif r["file"] in POR_ARCHIVO:
            disp[r["id"]] = {"status": "NA", "reason": POR_ARCHIVO[r["file"]]}
(AQUI / "disposiciones.json").write_text(json.dumps(disp, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(disp), "disposiciones")
