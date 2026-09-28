"""Decisiones del usuario tomadas durante la construcción de la app (no forman parte de los originales;
DECISIONES.md del repo no se modifica). Cada una con fecha y texto literal de la instrucción."""

LONGITUD = {
    "id": "U-2026-09-28-LONGITUD",
    "fecha": "2026-09-28",
    "instruccion": ("quiero que no hags la restrccion en elumero de plabras de lols prompts bloqueante sino mas bien spiracional "
                    "y que solo si excede al doble del numeor d epalaras establecido por el cidgo entonces si se bkliqueee u se regenere"),
    "regla": "La longitud es aspiracional: fuera del rango de la fuente sólo avisa. Bloquea y exige regenerar si supera 2× el máximo.",
    "factor_bloqueo": 2.0,
    "compatible_con": "DECISIONES.md #2 (el conteo de palabras nunca bloquea: advertencia con el presupuesto como referencia)",
}
