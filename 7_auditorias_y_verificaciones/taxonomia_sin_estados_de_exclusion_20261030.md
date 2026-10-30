# Verificación: la taxonomía prohíbe y no usa estados que dejen una regla fuera de toda selección (2026-10-30)

Pedido de Eric: que la clasificación no use «no aplica», «pendiente», «ausente», «no encontrado» ni nada equivalente que
deje una regla o un texto fuera de cualquier selección futura. Revisado en `3_taxonomia/00688_…md` y en el catálogo de
casos, buscando esas palabras y sus equivalentes en inglés en todo el archivo, y leyendo completas §1.12 y §6.0–§6.1.

## Dónde lo prohíbe

| Línea | Qué dice |
|---|---|
| L14 | Cada faceta se resuelve con VALOR o UNIVERSAL; UNIVERSAL «jamás sustituye una duda» |
| L29 | Ninguna etiqueta de desconocimiento, verificación pendiente, capacidad no verificada, adopción documental, antigüedad o NO APLICA puede convertir una regla en no seleccionable |
| L31 | La exclusión permanente exige una decisión expresa del usuario |
| L32, L2808 | Un dato ausente en el brief se pide antes de seleccionar; no se vuelve una clase de regla |
| L161 (§1.2) | Vacíos, omisiones y etiquetas de duda no son clasificaciones válidas |
| L166, L1394, L1455, L1505 | En F26–F28, VALOR o UNIVERSAL, «nunca NO APLICA» |
| L195 (§1.12.8) | Se prohíben NO DETERMINADO, NO APLICA, DESCONOCIDO, PENDIENTE, EN PROCESO y equivalentes, también ocultos en vacíos, null, listas vacías, flags o condiciones imposibles |
| L196 (§1.12.9) | Solo una decisión expresa, identificada y aplicable autoriza exclusión permanente |
| L197 (§1.12.10) | Las etiquetas de confianza, adopción, prueba y antigüedad nunca integran los estados de clasificación ni el filtro de elegibilidad |
| L199 (§1.12.12) | Control de aceptación: cero valores de diferimiento habilitados |
| §6.0 | El medio no lleva «valor ficticio» fuera de la rama activo; los descriptores de evidencia «nunca estados de clasificación ni filtros de elegibilidad» |
| §7.4 | Tres salidas por regla y caso: excluida por decisión expresa, fuera de este caso, aplicable confirmada; «no se produce una tercera clase» |
| L4342 | Gate final: una señal léxica ausente no autoriza excluir un texto; ninguna regla se elimina para alcanzar el cero |

## Si los usa

Ningún valor de faceta ni campo es «no aplica», «pendiente», «ausente», «no encontrado» ni equivalente.

Términos cuyo nombre se parece, y que la taxonomía declara expresamente como no estados de clasificación:
- «Afirmación fuente por contrastar» (TRM-1332) y «Refutada» (TRM-1334): descriptores documentales (§6.1, título del campo; §1.12.10).
- «Informe de capacidad sin prueba de ejecución» (TRM-0680) y «Capacidad obsoleta» (TRM-0682): acompañan a la regla seleccionada, no la excluyen (L29–L30).
- «Solicitud de confirmación de atributo fuente» (TRM-0765): tarea de consulta que se resuelve antes de usar el dato (L2684).
- «Contacto ausente» (TRM-0181): valor real de la faceta 21 (las personas no se tocan).

Menciones en el Anexo 1 (histórico, no operativo según §1.12.10): L2839 «Orden EXCLUIDA → PENDIENTE → APLICABLE» de la
versión 3, reemplazado por §7.4, y L2841 «NO APLICA justificado» de la edición C16, que ya no existe en los campos vigentes.

## Catálogo de casos

Ninguna disposición es NO APLICA, NO DETERMINADO ni PENDIENTE; `validar.py` lo exige. Las disposiciones son
VALOR_AUTORIZADO, VOCABULARIO_OPERATIVO, INDICE_DOCUMENTAL, CONCILIACION_HISTORICA y TRACK_HISTORICO_DEC22; las tres
últimas marcan términos del tesauro que no describen un caso, no reglas ni textos.

## Límite

Hoy hay 0 textos clasificados. La regla está escrita y nada la contradice, pero su cumplimiento en la clasificación
solo se puede comprobar cuando exista.
