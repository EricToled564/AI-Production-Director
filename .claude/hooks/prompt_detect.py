#!/usr/bin/env python3
"""Decide si un bloque cercado es la entrega de un prompt visual.

Los tres gates de `Stop` necesitan la misma decision, y tenerla en un solo lugar
evita que se separen. La primera version de gate_image.py no la tenia: trataba
cualquier bloque como prompt de imagen, y bloqueaba mensajes que solo contenian
comandos de shell.

Regla: un bloque cuenta como entrega si tiene una senal POSITIVA de prompt y no
es evidentemente codigo. El default es NO bloquear — un gate que bloquea texto
que no es un prompt se desactiva a la semana, y entonces no protege nada.
"""

from __future__ import annotations

import re

IMAGE_MODELS = (
    "nano banana", "nano-banana", "nanobanana", "nbp", "nb2",
    "gpt image", "gpt-image", "seedream", "midjourney", "flux", "ideogram",
)
VIDEO_MODELS = (
    "kling", "veo", "sora", "seedance", "hailuo", "runway", "luma", "pika",
)

# Señal positiva: abre con un verbo de generación, o trae los campos de un brief.
PROMPTISH = re.compile(
    r"^\s*(create|generate|design|transform|convert|edit)\b"
    r"|^\s*(subject|lighting|background|mood|format|aspect[ _]ratio|negative[ _]prompt"
    r"|typography|camera|framing|scene|use ?case|constraints|preserve|change)\s*:"
    r"|^\s*(wide shot|close-?up|medium shot|mcu|ecu|extreme close-?up)\b",
    re.IGNORECASE | re.MULTILINE,
)

# Señal de que es código, salida de terminal o datos: nunca es un prompt.
CODEISH = re.compile(
    r"^\s*(\$|#!|//|#\s|npx |npm |pnpm |yarn |pip |pip3 |python3? |node |bash |sh |zsh "
    r"|git |cd |ls |cat |mkdir |rm |cp |mv |chmod |curl |wget |sudo |apt |brew "
    r"|export |source |echo |grep |sed |awk |find |for |while |if |fi\b|done\b)"
    r"|^\s*(from|import|def|class|return|const|let|var|function|package|module)\s"
    r"|^\s*[{\[<]"
    r"|^\s*[\w./%-]+\s*(→|->|=>)\s"
    r"|^\s*[A-Za-z_][A-Za-z0-9_]*\s*[:=]\s*(true|false|null|none|\d)"
    r"|^\s*(EXIT|exit|PASS|FAIL|WARN|ERROR|OK)\b",
    re.MULTILINE,
)

FENCE_INFO = re.compile(r"```([^\n]*)\n")
# Lenguajes que jamas son un prompt visual.
CODE_LANGS = {
    "bash", "sh", "shell", "zsh", "console", "terminal", "python", "py", "js",
    "javascript", "ts", "typescript", "json", "yaml", "yml", "toml", "xml",
    "html", "css", "sql", "diff", "patch", "go", "rust", "java", "c", "cpp",
}


def fenced_blocks(message: str) -> list[tuple[str, str]]:
    """Devuelve (lenguaje, contenido) por cada bloque cercado."""
    out: list[tuple[str, str]] = []
    pos = 0
    while True:
        m = FENCE_INFO.search(message, pos)
        if not m:
            return out
        end = message.find("```", m.end())
        if end == -1:
            return out
        out.append((m.group(1).strip().lower(), message[m.end():end]))
        pos = end + 3


def is_visual_prompt(block: str, lang: str = "", message: str = "") -> bool:
    """True si el bloque es la entrega de un prompt visual."""
    if lang in CODE_LANGS:
        return False

    # La señal positiva gana sobre la de código: campos como "Format: 4:5" son
    # del template de imagen y también se parecen a una asignación.
    if PROMPTISH.search(block):
        return True
    low_block = block.lower()
    if any(m in low_block for m in IMAGE_MODELS + VIDEO_MODELS):
        return True

    if CODEISH.search(block):
        return False
    # El modelo destino casi siempre se nombra en la prosa que introduce el
    # bloque ("Prompt para Nano Banana:"), no dentro del bloque. Si el mensaje
    # nombra un modelo y el bloque no es codigo, es la entrega.
    low_msg = (message or "").lower()
    return any(m in low_msg for m in IMAGE_MODELS + VIDEO_MODELS)


def visual_blocks(message: str) -> list[tuple[int, str]]:
    """(indice base 1, contenido) de los bloques que son entrega de prompt."""
    return [
        (i, body)
        for i, (lang, body) in enumerate(fenced_blocks(message), start=1)
        if is_visual_prompt(body, lang, message)
    ]


def names_image_model(text: str) -> bool:
    return any(m in text.lower() for m in IMAGE_MODELS)


def names_video_model(text: str) -> bool:
    return any(m in text.lower() for m in VIDEO_MODELS)
