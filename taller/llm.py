"""Proveedores de inferencia.

- openai: Responses API (OPENAI_API_KEY, OPENAI_MODEL, OPENAI_REASONING_EFFORT opcional).
- anthropic: Messages API (ANTHROPIC_API_KEY, ANTHROPIC_MODEL).
- manual: la app muestra la solicitud exacta; el usuario la pega en ChatGPT o Claude y
  devuelve la respuesta JSON. Se valida igual que una respuesta de API.
- fixture: solo para pruebas automáticas; nunca se ofrece en la interfaz.

Cada llamada es una solicitud independiente: ningún rol ve el razonamiento de otro.
Las respuestas se guardan en caché por hash de la solicitud, así reintentar no cobra dos veces
y el modo manual puede retomar una operación de varios pasos.
"""
import json
import os
import re
import urllib.error
import urllib.request

from recursos import huella


class ManualPendiente(Exception):
    """La operación necesita que el usuario pegue la respuesta de esta solicitud."""

    def __init__(self, solicitud):
        super().__init__("Respuesta manual pendiente")
        self.solicitud = solicitud


class ErrorModelo(Exception):
    pass


class RespuestaInvalida(Exception):
    pass


def clave_solicitud(rol, sistema, carga):
    return huella({"rol": rol, "sistema": sistema, "carga": carga})


def texto_para_copiar(solicitud):
    return (
        "INSTRUCCIONES DEL ROL (" + solicitud["rol"] + "):\n" + solicitud["sistema"] +
        "\n\nDATOS DE ENTRADA (JSON):\n" + json.dumps(solicitud["carga"], ensure_ascii=False, indent=1) +
        "\n\nResponde ÚNICAMENTE con un objeto JSON válido, sin texto antes ni después."
    )


def extraer_json(texto):
    texto = texto.strip()
    if texto.startswith("```"):
        texto = re.sub(r"^```[a-zA-Z]*\s*", "", texto)
        texto = re.sub(r"\s*```$", "", texto)
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        inicio, fin = texto.find("{"), texto.rfind("}")
        if inicio == -1 or fin <= inicio:
            raise RespuestaInvalida("La respuesta no contiene un objeto JSON.")
        try:
            return json.loads(texto[inicio:fin + 1])
        except json.JSONDecodeError as e:
            raise RespuestaInvalida(f"JSON inválido: {e}")


def _post(url, cuerpo, cabeceras, segundos):
    req = urllib.request.Request(url, data=json.dumps(cuerpo).encode("utf-8"), headers=cabeceras)
    try:
        with urllib.request.urlopen(req, timeout=segundos) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detalle = e.read().decode("utf-8", "replace")[:600]
        raise ErrorModelo(f"HTTP {e.code}: {detalle}")
    except urllib.error.URLError as e:
        raise ErrorModelo(f"Sin conexión con el proveedor: {e.reason}")


class Proveedor:
    nombre = "base"
    lote_seleccion = 40

    def __init__(self, almacen):
        self.almacen = almacen  # objeto con leer_respuesta(clave) / guardar_respuesta(clave, ...)

    def llamar(self, rol, sistema, carga, validar):
        clave = clave_solicitud(rol, sistema, carga)
        guardada = self.almacen.leer_respuesta(clave)
        if guardada is not None:
            return guardada
        solicitud = {"clave": clave, "rol": rol, "sistema": sistema, "carga": carga}
        valor = self._obtener(solicitud, validar)
        self.almacen.guardar_respuesta(clave, rol, self.nombre, valor)
        return valor

    def _obtener(self, solicitud, validar):
        raise NotImplementedError

    def descripcion(self):
        return self.nombre


class Manual(Proveedor):
    nombre = "manual"
    lote_seleccion = 160

    def _obtener(self, solicitud, validar):
        pegado = self.almacen.leer_pegado(solicitud["clave"])
        if pegado is None:
            raise ManualPendiente(solicitud)
        self.almacen.borrar_pegado(solicitud["clave"])
        validar(pegado)
        return pegado


class _API(Proveedor):
    segundos = 600

    def _obtener(self, solicitud, validar):
        texto = self._completar(solicitud["sistema"], solicitud["carga"])
        try:
            valor = extraer_json(texto)
            validar(valor)
            return valor
        except RespuestaInvalida as e:
            # Un reintento con el error explícito; si vuelve a fallar se informa al usuario.
            carga = dict(solicitud["carga"], error_respuesta_anterior=str(e))
            texto = self._completar(solicitud["sistema"], carga)
            valor = extraer_json(texto)
            validar(valor)
            return valor


class OpenAI(_API):
    nombre = "openai"

    def __init__(self, almacen):
        super().__init__(almacen)
        self.clave = os.environ.get("OPENAI_API_KEY", "")
        self.modelo = os.environ.get("OPENAI_MODEL", "")
        self.esfuerzo = os.environ.get("OPENAI_REASONING_EFFORT", "")
        if not self.clave or not self.modelo:
            raise ErrorModelo("Faltan OPENAI_API_KEY u OPENAI_MODEL en el entorno.")

    def descripcion(self):
        return f"openai:{self.modelo}"

    def _completar(self, sistema, carga):
        cuerpo = {"model": self.modelo, "instructions": sistema,
                  "input": "Datos de entrada en JSON. Responde solo con JSON.\n" + json.dumps(carga, ensure_ascii=False),
                  "text": {"format": {"type": "json_object"}}}
        if self.esfuerzo:
            cuerpo["reasoning"] = {"effort": self.esfuerzo}
        r = _post("https://api.openai.com/v1/responses", cuerpo,
                  {"Authorization": "Bearer " + self.clave, "Content-Type": "application/json"}, self.segundos)
        partes = [c.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                  for c in o.get("content", []) if c.get("type") == "output_text"]
        if not partes:
            raise ErrorModelo(f"Respuesta sin texto (estado {r.get('status')}).")
        return "".join(partes)


class Anthropic(_API):
    nombre = "anthropic"

    def __init__(self, almacen):
        super().__init__(almacen)
        self.clave = os.environ.get("ANTHROPIC_API_KEY", "")
        self.modelo = os.environ.get("ANTHROPIC_MODEL", "claude-opus-5-5")
        self.base = os.environ.get("TALLER_ANTHROPIC_URL", "https://api.anthropic.com").rstrip("/")
        if not self.clave:
            raise ErrorModelo("Falta ANTHROPIC_API_KEY en el entorno.")

    def descripcion(self):
        return f"anthropic:{self.modelo}"

    def _completar(self, sistema, carga):
        cuerpo = {"model": self.modelo, "max_tokens": 32000, "system": sistema,
                  "messages": [{"role": "user", "content": "Datos de entrada en JSON. Responde solo con un objeto JSON.\n" + json.dumps(carga, ensure_ascii=False)}]}
        r = _post(self.base + "/v1/messages", cuerpo,
                  {"x-api-key": self.clave, "anthropic-version": "2023-06-01", "content-type": "application/json"},
                  self.segundos)
        partes = [b.get("text", "") for b in r.get("content", []) if b.get("type") == "text"]
        if not partes:
            raise ErrorModelo(f"Respuesta sin texto (stop_reason {r.get('stop_reason')}).")
        return "".join(partes)


class Fixture(Proveedor):
    """Respuestas programadas para pruebas: función (rol, carga) -> valor."""
    nombre = "fixture"
    lote_seleccion = 50

    def __init__(self, almacen, responder):
        super().__init__(almacen)
        self.responder = responder

    def _obtener(self, solicitud, validar):
        valor = self.responder(solicitud["rol"], solicitud["carga"])
        validar(valor)
        return valor


def crear(nombre, almacen):
    nombre = (nombre or "manual").lower()
    if nombre == "openai":
        return OpenAI(almacen)
    if nombre == "anthropic":
        return Anthropic(almacen)
    if nombre == "manual":
        return Manual(almacen)
    raise ErrorModelo(f"Proveedor desconocido: {nombre}")
