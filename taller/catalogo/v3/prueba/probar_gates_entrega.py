"""probar_gates_entrega.py: los tres gates de Stop con un mensaje de entrega con el formato de la tarea 10.

    python3 -I taller/catalogo/v3/prueba/probar_gates_entrega.py

Arma el mensaje como lo pide el plan:
- cabecera SKILL / RIESGOS / TÉCNICA;
- Model, Quality y Size fuera del bloque;
- el prompt GPT2-GEN en bloque cercado;
- la línea OVERRIDE de R1.

Comprueba que los tres gates lo dejan pasar (código 0) y que lo bloquean sin cabecera, sin OVERRIDE o con vocabulario
prohibido. Cada gate recibe el payload por stdin, igual que como hook de Stop. Sale con código 1 si un resultado no es
el esperado.
"""
import json
import subprocess
import sys
import uuid
from pathlib import Path

HOOKS = Path(__file__).resolve().parents[4] / ".claude/hooks"
GATES = ["gate_microgate", "gate_dramaturgy", "gate_image"]

PROMPT = ("Scene: A vertical 4:5 photograph of a quiet street cafe at dusk, warm window light from camera left.\n"
          "Subject: A hand-painted wooden sign above the door.\n"
          "Important Details: The sign reads \"Florista\" in white serif letters; 50mm feel, natural texture.\n"
          "Use Case: Editorial thumbnail; the headline is composited later.\n"
          "Constraints: No extra words, no duplicate text, no watermarks.")
CABECERA = ("SKILL: image/references/gpt-image.md (5 slots, Text in Image) leído en este turno\n"
            "RIESGOS: texto mal escrito; la línea Constraints lo limita\n"
            "TÉCNICA: Text in Image de gpt-image.md:67-74")
OVERRIDE = "OVERRIDE: R1 - GPT2-GEN abre con el rótulo Scene: y el verbo dentro del slot (INV-002335)"


def mensaje(cabecera=True, override=True, prompt=PROMPT):
    partes = [CABECERA] if cabecera else []
    partes += ["Model: gpt-image-2 · Quality: high · Size: 1024x1280", "```", prompt, "```"]
    if override:
        partes.append(OVERRIDE)
    return "\n".join(partes)


def correr(gate, texto):
    payload = json.dumps({"last_assistant_message": texto, "session_id": "prueba-" + uuid.uuid4().hex[:8],
                          "stop_hook_active": False})
    p = subprocess.run([sys.executable, "-I", str(HOOKS / f"{gate}.py")], input=payload, capture_output=True,
                       text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


casos = [("entrega completa", mensaje(), {g: 0 for g in GATES}),
         ("sin cabecera", mensaje(cabecera=False), {"gate_microgate": "bloquea"}),
         ("sin OVERRIDE de R1", mensaje(override=False), {"gate_image": "bloquea"}),
         ("con vocabulario prohibido", mensaje(prompt=PROMPT.replace("natural texture", "stunning masterpiece")),
          {"gate_dramaturgy": "bloquea"})]
fallos = 0
for nombre, texto, esperado in casos:
    for gate, want in esperado.items():
        codigo, salida = correr(gate, texto)
        ok = codigo == 0 if want == 0 else codigo != 0
        fallos += not ok
        print(("  ok    " if ok else "  FALLA ") + f"{nombre} · {gate}: código {codigo}"
              + ("" if ok else f"\n        {salida[:300]}"))
print("todo como se esperaba" if not fallos else f"{fallos} resultados inesperados")
sys.exit(1 if fallos else 0)
