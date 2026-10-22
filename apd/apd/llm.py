"""Modelo de lenguaje del servidor. La clave vive en el entorno del servidor, nunca en el
navegador, en los prompts exportados ni en el repo.

    APD_LLM=openai     OPENAI_API_KEY=...     [OPENAI_MODEL=gpt-6-astra]   (motor del ejecutor anterior)
    APD_LLM=anthropic  ANTHROPIC_API_KEY=...  [ANTHROPIC_MODEL=claude-sonnet-5]
    APD_LLM=none       sin modelo: la app funciona en modo determinista y lo dice

Sólo stdlib (urllib). Cada llamada devuelve texto + uso (tokens, segundos) para que la
interfaz muestre el consumo real del procesamiento completo.
"""

from __future__ import annotations

import base64
import json
import os
import re
import time
import urllib.error
import urllib.request


class SinModelo(RuntimeError):
    pass


def _post(url: str, headers: dict, body: dict, timeout: int = 300) -> dict:
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers={"content-type": "application/json", **headers})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        detalle = e.read().decode(errors="replace")[:600]
        raise RuntimeError(f"HTTP {e.code}: {detalle}") from None


def extraer_json(texto: str):
    t = texto.strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", t, re.S)
    if m:
        t = m.group(1)
    i = min([x for x in (t.find("{"), t.find("[")) if x >= 0], default=-1)
    if i > 0:
        t = t[i:]
    return json.loads(t)


class Proveedor:
    nombre = "base"
    modelo = ""

    def disponible(self) -> bool:
        return False

    def completar(self, sistema: str, usuario: str, imagenes: list[dict] | None = None, json_mode=True) -> dict:
        raise SinModelo("no hay modelo configurado en el servidor (APD_LLM)")


class Ninguno(Proveedor):
    nombre = "none"
    motivo = "Sin modelo configurado: define APD_LLM y la clave del proveedor en el entorno del servidor."


class OpenAI(Proveedor):
    nombre = "openai"

    def __init__(self):
        self.clave = os.environ.get("OPENAI_API_KEY", "")
        self.modelo = os.environ.get("OPENAI_MODEL", "gpt-6-astra")
        self.base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
        self.esfuerzo = os.environ.get("OPENAI_REASONING_EFFORT", "").strip().lower()  # low | medium | high; vacío = default del modelo

    def disponible(self):
        return bool(self.clave)

    def completar(self, sistema, usuario, imagenes=None, json_mode=True):
        contenido = [{"type": "input_image", "image_url": f"data:{im['media_type']};base64,{im['data']}", "detail": "high"}
                     for im in (imagenes or [])]
        # Responses API con text.format json_object exige la palabra "json" en el input (no basta en instructions): HTTP 400.
        contenido.append({"type": "input_text", "text": usuario + ("\n\nResponde sólo con JSON válido." if json_mode else "")})
        body = {"model": self.modelo, "instructions": sistema,
                "input": [{"role": "user", "content": contenido}], "max_output_tokens": 32000,
                "prompt_cache_key": "apd-reglas"}
        if self.esfuerzo:
            body["reasoning"] = {"effort": self.esfuerzo}
        if json_mode:
            body["text"] = {"format": {"type": "json_object"}}
        t0 = time.time()
        d = _post(f"{self.base}/responses", {"authorization": f"Bearer {self.clave}"}, body)
        txt = "".join(c.get("text", "") for o in d.get("output", []) if o.get("type") == "message"
                      for c in o.get("content", []) if c.get("type") == "output_text")
        u = d.get("usage") or {}
        return {"texto": txt, "uso": {"entrada": u.get("input_tokens", 0), "salida": u.get("output_tokens", 0),
                                      "segundos": round(time.time() - t0, 2)}}


class Anthropic(Proveedor):
    nombre = "anthropic"

    def __init__(self):
        self.clave = os.environ.get("ANTHROPIC_API_KEY", "")
        self.modelo = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5")
        self.base = os.environ.get("APD_ANTHROPIC_URL", "https://api.anthropic.com/v1")

    def disponible(self):
        return bool(self.clave)

    def completar(self, sistema, usuario, imagenes=None, json_mode=True):
        contenido = [{"type": "image", "source": {"type": "base64", "media_type": im["media_type"], "data": im["data"]}}
                     for im in (imagenes or [])]
        contenido.append({"type": "text", "text": usuario + ("\n\nResponde sólo con JSON válido." if json_mode else "")})
        body = {"model": self.modelo, "max_tokens": 32000, "system": sistema,
                "messages": [{"role": "user", "content": contenido}]}
        t0 = time.time()
        d = _post(f"{self.base}/messages", {"x-api-key": self.clave, "anthropic-version": "2023-06-01"}, body)
        txt = "".join(c.get("text", "") for c in d.get("content", []) if c.get("type") == "text")
        u = d.get("usage") or {}
        return {"texto": txt, "uso": {"entrada": u.get("input_tokens", 0), "salida": u.get("output_tokens", 0),
                                      "segundos": round(time.time() - t0, 2)}}


class Falso(Proveedor):
    """Proveedor de pruebas: una función (sistema, usuario) -> texto. No finge ser un modelo real."""
    nombre = "falso"

    def __init__(self, fn, modelo="falso-determinista"):
        self.fn = fn
        self.modelo = modelo
        self.llamadas = 0

    def disponible(self):
        return True

    def completar(self, sistema, usuario, imagenes=None, json_mode=True):
        self.llamadas += 1
        txt = self.fn(sistema, usuario)
        return {"texto": txt, "uso": {"entrada": len(usuario) // 4, "salida": len(txt) // 4, "segundos": 0.0}}


_actual: Proveedor | None = None


def proveedor() -> Proveedor:
    global _actual
    if _actual is None:
        tipo = os.environ.get("APD_LLM", "").lower()
        if not tipo:
            tipo = "openai" if os.environ.get("OPENAI_API_KEY") else ("anthropic" if os.environ.get("ANTHROPIC_API_KEY") else "none")
        _actual = {"openai": OpenAI, "anthropic": Anthropic}.get(tipo, Ninguno)()
    return _actual


def fijar(p: Proveedor | None):
    global _actual
    _actual = p


def estado() -> dict:
    p = proveedor()
    return {"proveedor": p.nombre, "modelo": p.modelo, "esfuerzo": getattr(p, "esfuerzo", "") or None, "disponible": p.disponible(),
            "motivo": "" if p.disponible() else getattr(p, "motivo", f"falta la clave de {p.nombre} en el entorno del servidor")}


def b64(data: bytes) -> str:
    return base64.b64encode(data).decode()
