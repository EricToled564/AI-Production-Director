"""Carga de recursos canónicos del taller.

Los archivos de recursos/ son copias byte a byte de los paquetes del proyecto (ver
recursos/MANIFIESTO.json). Este módulo solo los lee: nunca reescribe un literal canónico.
"""
import hashlib
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent / "recursos"

SLOTS_GEN = ["Scene", "Subject", "Important Details", "Use Case", "Constraints"]


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def huella(obj):
    """Hash estable de cualquier valor JSON."""
    return sha256_bytes(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def _leer(nombre):
    return json.loads((RAIZ / nombre).read_text(encoding="utf-8"))


def verificar_manifiesto():
    """Devuelve la lista de archivos cuyo hash no coincide con el manifiesto."""
    manifiesto = _leer("MANIFIESTO.json")
    distintos = []
    for nombre, info in manifiesto["archivos"].items():
        actual = sha256_bytes((RAIZ / nombre).read_bytes())
        if actual != info["sha256"]:
            distintos.append(nombre)
    return distintos


class Recursos:
    def __init__(self):
        plantilla = _leer("template_brief.json")
        self.campos = plantilla["brief"]
        self.rutas = [c["path"] for c in self.campos]
        self.campo_por_ruta = {c["path"]: c for c in self.campos}
        self.anotacion_brief = plantilla["annotations"]
        self.contrato_genesis = plantilla["operation_contract"]
        self.fuente_plantilla = plantilla["source"]

        self.canonicos = {x["id"]: x for x in _leer("canonical_sources.json")}
        reglas = _leer("universal_rules.json")
        self.universales = []
        for r in reglas["rules"]:
            self.universales.append({
                "regla_id": r["rule_id"],
                "fuentes": [self._literal(i) for i in r["source_ids"]],
                "intencion": r["intent"],
                "criterio_falla": r["failure_criteria"],
                "criterio_duda": r["uncertainty_criteria"],
                "notas": r.get("notes", ""),
            })
        self.version_universales = reglas["version"]

        self.packs = {p["pack_id"]: p for p in _leer("operation_packs.json")}

        directivas = [d for d in _leer("user_directives.json") if d.get("scope") == "task"]
        directivas += _leer("directivas_taller.json")
        self.directivas = directivas

        self.catalogo = _leer("catalogo_especificas.json")
        self.catalogo_por_id = {u["id"]: u for u in self.catalogo}

        self.llenado = _leer("instrucciones_llenado.json")

    def _literal(self, inv_id):
        src = self.canonicos[inv_id]
        return {"id": inv_id, "archivo": src["archivo"], "encabezado": src["encabezado"],
                "lineas": f'{src["linea_inicial"]}-{src["linea_final"]}', "texto": src["texto"],
                "sha256_unidad": src["sha256_unidad"]}

    def pack_gen(self):
        pack = self.packs["GPT2-GEN"]
        checks = [{"regla_id": f"PACK::GPT2-GEN::{i + 1}", "texto": t,
                   "fuentes": [self._literal(s) for s in pack["source_ids"]]}
                  for i, t in enumerate(pack["checks"])]
        return {"pack_id": pack["pack_id"], "rotulos": pack["fixed_labels"], "checks": checks,
                "no_requisito": pack.get("not_a_requirement", []),
                "mapeo_derivado": pack.get("derived_mapping", {}),
                "advisorios": pack.get("scoped_adapter_checks", [])}

    def reglas_directivas(self):
        return [{"regla_id": "USER::" + d["constraint_id"], "literal": d["literal"],
                 "interpretacion": d["interpretation"], "autoridad": d["authority"]}
                for d in self.directivas]

    def instrucciones_slots(self):
        literal = self._literal("INV-002335")
        salida = []
        for s in self.llenado["slots"]:
            salida.append(dict(s, literal_inv_002335=literal["texto"]))
        return salida

    def unidad_compacta(self, unidad):
        src = unidad["source"]
        return {"id": unidad["id"], "archivo": src["archivo"], "encabezado": src["encabezado"],
                "texto": src["texto"], "alcance": unidad.get("scope", ""),
                "activador": unidad.get("trigger", ""), "interpretacion": unidad.get("interpretation", "")}


_INSTANCIA = None


def cargar():
    global _INSTANCIA
    if _INSTANCIA is None:
        _INSTANCIA = Recursos()
    return _INSTANCIA
