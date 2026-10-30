# Base de opciones y composición de casos de uso

## Qué contiene esta entrega

Base estructurada derivada de la taxonomía consolidada del 19 de octubre. Contiene 1.729 registros: los 1.369 términos TRM preservados y 360 valores autorizados de facetas, procesos, modelos y publicación. Las 31 facetas tienen registros. Cada registro conserva definición, faceta, materia cuando existe, sección/línea, huella de taxonomía y destino físico comprobado en el contrato de templates del paquete.

Un caso de uso es una combinación de valores con datos concretos. No se materializa el producto cartesiano de todos los valores: muchas combinaciones son incompatibles, y edades, posiciones y literales son dominios abiertos. Esta entrega no afirma contener todas las imágenes posibles. Conserva todo el vocabulario TRM y los valores tabulados de la taxonomía consultada; una necesidad no representada se investiga y se propone como extensión explícita antes de convertirla en nueva categoría canónica.

## Archivos

- `casos_opciones.sqlite`: base consultable, tabla `opciones`, índice por faceta.
- `catalogo_opciones.json` y `.csv`: mismos registros con procedencia y destinos.
- `case.schema.json`: formato de un caso, valores por campo, origen, evidencia, confirmación y aprobación.
- `mapa_facetas.json`: las 31 facetas y sus destinos lógicos literales.
- `mapa_materias_f30.json`: los 24 contratos de efecto de F30, literales.
- `mapa_materias_f30_paths.json`: destinos físicos por materia, comprobados contra el schema real del paquete.
- `jerarquia_valores.json`: padres de faceta y vínculos literales a valores, sin equivalencias inferidas.
- `rutas_documentadas.json`: 184 filas de estructura de flujos conservadas literalmente, incluidos los pasos editoriales FL04; no se convierten automáticamente en condiciones.
- `relaciones_documentadas.json`: relaciones explícitas e interpretación delimitada, sin inventar incompatibilidades globales.
- `manifest_fuentes.json`, `conteos.json`: huellas y conteos. La verificación mecánica (`verificacion.json`) está en `7_auditorias_y_verificaciones/casos/`.
- `validar.py`: verifica estructura, IDs, cobertura, destinos y, opcionalmente, completitud/aprobación de un caso.
- `build_catalog.py` y `bind_templates.py`: reproducción de extracción estructural y vinculación.

## Diferencias que deben preservarse

F04 es tipo de pieza; F17 estilo; F18 técnica; F24 tamaño de plano; F25 ángulo. No se fusionan. F11 describe rol del ancla, no el medio. F26–F28 son contexto del clip cuando condiciona FF/LF, no instrucciones para reproducir movimiento o audio dentro de una imagen fija. Plataforma, ubicación, ratio y modelo son dimensiones diferentes. F30 indica la materia del efecto y sus términos pueden describir atributos del caso; F30 no es por sí misma una condición que descarte una regla.

La ruta lógica de V5 `entrada.sujetos[].clase` se normaliza físicamente a `entrada.sujetos.items[].clase`, para coexistir con `entrada.sujetos.cantidad`. Los dos nombres quedan documentados, sin reinterpretar la faceta.

## Vocabulario operativo y conciliación

- 1.197 términos operativos con definición completa.
- 112 índices documentales de presencia.
- 57 conceptos conservados para conciliación histórica según §0.6.
- 3 tracks históricos por DEC22.
- 360 valores autorizados extraídos de las tablas.

Esto no excluye reglas originales: son disposiciones del vocabulario taxonómico, no clasificación de prescripciones del corpus. No se usa ausencia de respaldo de un término como exclusión automática de una regla. Los tres tracks conservan sus IDs y las decisiones que gobiernan su tratamiento. Las filas documentales tienen destino de procedencia, no se insertan como elecciones visuales del usuario.

`case_selectable` significa que el registro puede ofrecerse como descriptor del caso. Los controles, materias padre, operadores de evidencia y trazabilidad también tienen destinos, aunque no sean botones visuales. No equivale a habilitar ni deshabilitar ninguna regla original. Tampoco toda opción ofrecida puede combinarse con todas las demás.

## Construcción del caso, de general a específico

1. Registrar brief literal y referencias realmente entregadas.
2. Identificar ámbito, flujo, objeto/medio, operación, modelo/versión/interfaz, tipo de pieza y uso. FF/LF siguen siendo imágenes.
3. Recoger contexto, sujetos, cantidad, identidad, acción, régimen físico, espacio, estilo y representación; después cámara, luz, materialidad, color, composición y detalles específicos.
4. Resolver cada dato requerido por los contratos y las condiciones de reglas: aportado por usuario, heredado de documento o propuesto por inferencia. Los valores inferidos se muestran como propuestas y requieren confirmación; no se atribuyen al usuario.
5. Si falta un discriminante, formular la pregunta necesaria. La falta es una tarea de completar ese brief, nunca una etiqueta que vuelva inelegible una regla.
6. Mostrar el brief completo para revisión, con origen por campo. Registrar aprobación y evidencia. Cualquier cambio relevante invalida la aprobación y obliga a revisar las selecciones afectadas.
7. Seleccionar reglas universales y específicas según el alcance real: todas las imágenes, modelo, operación/tipo, conjuntos de casos, caso específico. Evaluar condiciones completas y excepciones. La búsqueda vectorial ayuda a localizar, pero no acredita por sí sola exhaustividad.
8. Aplicar reglas de sintaxis, valor, selección, control y contenido al destino correspondiente. Lo incorporado a template conserva vínculo regla–campo–condición–validación; una condición variable sigue evaluándose en cada instancia.
9. Verificar coherencia del caso, ausencia de contradicciones, cobertura de efectos y límites del contrato del modelo. Solo después compactar, sin perder obligaciones. No hay límite inventado de 15–20 reglas.
10. Entregar prompt conforme al contrato específico y parámetros separados; mantener traza de aplicaciones y validaciones. El éxito visual requiere comprobar el resultado generado.

## Verificación y límites medidos

La verificación actual acredita estructura del catálogo: todos los TRM, facetas, definiciones operativas y rutas existentes. No acredita que todas las reglas del corpus estén correctamente clasificadas o que un selector recupere todas y solo las aplicables. Este paquete no contiene enlaces REG inventados, ni respuestas de referencia generadas desde la clasificación antigua.

Para ejecutar: `python validar.py`. Para revisar un caso: `python validar.py caso.json`. La segunda modalidad bloquea falta de aprobación, propuestas sin confirmar, requisitos declarados sin resolver, ID desconocido y huella incorrecta. La lista de requisitos declarados debe derivarse de los contratos y reglas clasificadas: una lista vacía no demuestra completitud semántica. Un pase estructural no autoriza generación ni sustituye el control semántico.

Reproducción completa desde la raíz del paquete de trabajo: ejecutar `build_catalog.py`, luego `bind_templates.py`, luego `validar.py`. La vinculación requiere `../templates/CONTRATO_IMAGEN_ORQUESTACION.schema.json` y `REGISTRO_DESTINOS_TEMPLATE.json` del mismo paquete.
