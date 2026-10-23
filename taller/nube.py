"""Modo nube (Vercel): sin disco persistente ni hilos en segundo plano.

- El estado vive en el navegador. Cada petición POST trae {"metodo", "cuerpo", "instantanea", "proveedor"};
  la instantánea se hidrata en AlmacenMemoria y la actualizada vuelve en la respuesta.
- Cada petición hace como máximo una llamada nueva y cobrada al modelo; si la operación necesita más,
  responde {"continuar": true} y la interfaz repite la petición, que reutiliza la caché de respuestas.
- Toda llamada a la API exige la contraseña TALLER_CLAVE_ACCESO (cabecera X-Taller-Clave). Sin esa variable
  definida, la API rechaza todo salvo /api/estado: la URL es pública y gasta la cuenta del proveedor.
"""
import hmac
import os

import llm
import proceso as P
import rutas

PROVEEDORES_NUBE = ("anthropic", "openai", "manual")
# Una sola llamada debe caber en el maxDuration de la función (300 s en el plan Hobby).
llm._API.segundos = float(os.environ.get("TALLER_LIMITE_LLAMADA_S", "280"))


class ContextoNube:
    def __init__(self, almacen, nombre, fabrica=None):
        self.almacen = almacen
        self.aviso = ""
        self.fabrica = fabrica or llm.crear  # las pruebas inyectan un proveedor simulado
        self.cambiar_proveedor(nombre)

    def cambiar_proveedor(self, nombre):
        nombre = nombre if nombre in PROVEEDORES_NUBE else os.environ.get("TALLER_PROVEEDOR", "anthropic")
        try:
            base = self.fabrica(nombre, self.almacen)
            self.aviso = ""
        except llm.ErrorModelo as e:
            base = llm.crear("manual", self.almacen)
            self.aviso = f"{e} Se usa el modo manual."
        self.nombre = base.nombre
        self.proceso = P.Proceso(self.almacen, llm.UnaLlamadaPorPeticion(base))

    def nombre_proveedor(self):
        return self.nombre

    def aviso_proveedor(self):
        return self.aviso

    def operacion(self, cid):
        return self.almacen.operaciones.get(cid)

    def lanzar(self, cid, nombre, nueva):
        actual = self.almacen.operaciones.get(cid)
        if nueva and actual and actual.get("estado") == "en_curso" and actual.get("nombre") != nombre:
            raise P.Compuerta(f"Ya hay una operación en curso: {actual['nombre']}.")
        op = rutas.nueva_operacion(nombre) if nueva or not actual else actual
        self.almacen.operaciones[cid] = op
        rutas.ejecutar_operacion(self.proceso, cid, nombre, nueva, op)
        return 200, {"operacion": nombre, "estado": op["estado"], "continuar": op["estado"] == "en_curso"}

    def continuar(self, cid, nombre):
        return self.lanzar(cid, nombre, False)


def clave_valida(recibida):
    esperada = os.environ.get("TALLER_CLAVE_ACCESO", "")
    return bool(esperada) and hmac.compare_digest(esperada.encode(), (recibida or "").encode())


def atender(partes, sobre, clave, fabrica=None):
    """Atiende una petición de la nube. Devuelve (codigo, datos)."""
    sobre = sobre or {}
    almacen = P.AlmacenMemoria(sobre.get("instantanea"))
    ctx = ContextoNube(almacen, sobre.get("proveedor") or os.environ.get("TALLER_PROVEEDOR", "anthropic"), fabrica)
    if partes == ["api", "estado"]:
        datos = rutas.estado_base(ctx)
        datos.update(modo="nube", casos=[], clave_configurada=bool(os.environ.get("TALLER_CLAVE_ACCESO")),
                     clave_ok=clave_valida(clave), proveedores=list(PROVEEDORES_NUBE))
        return 200, datos
    if not os.environ.get("TALLER_CLAVE_ACCESO"):
        return 503, {"error": "Falta configurar TALLER_CLAVE_ACCESO en Vercel: sin contraseña la app no se abre."}
    if not clave_valida(clave):
        return 401, {"error": "Contraseña incorrecta."}
    metodo = (sobre.get("metodo") or "POST").upper()
    codigo, datos = rutas.despachar(metodo, partes, sobre.get("cuerpo"), ctx.proceso, ctx)
    if codigo == 200 and "_markdown" in datos:
        datos = {"texto": datos["_markdown"], "nombre": datos["_nombre"]}
    return codigo, {"datos": datos, "instantanea": almacen.instantanea()}
