# Decisiones de Eric Toledano — 2026-10-23

1. Alcance de esta fase: solo textos de imagen y GPT Image 2. Universo: los 1,511 textos de `skills/image/**`
   (sin LICENSE ni NOTICE), `skills/visual-prompt-forge/adapters/gpt-image.md` y
   `skills/visual-prompt-forge/examples/one-shot-all-adapters/gpt-image.txt` de la base de 13,005 textos
   originales. Un texto que solo vale para otro modelo se clasifica igual, con su F29, y el filtro lo deja fuera.
2. La catalogación previa (2026-10-11, 1,887 registros) y la catalogación provisional del 2026-10-23 no se
   reutilizan como respuesta: se reclasifica de forma exhaustiva desde el inventario original según §1.12.
3. Ningún texto queda como pendiente, propuesta, duda, NO APLICA ni equivalente. Lo que no cabe en la taxonomía se
   discute con Eric antes de ampliarla.
4. Extensiones de la taxonomía aprobadas (se registran aparte de la taxonomía original):
   - F32 Texto en la imagen: sin texto · texto corto · texto extenso o pequeño.
   - F33 Complejidad de escena: simple · compleja (5 o más elementos).
   - F34 Resolución: 1K · 2K · 4K.
   - F04 + infografía o diagrama · concept art · pieza de portafolio.
   - F05 + finanzas y banca · sector público.
   - F06 + 3:2.
   - F10 + hijos de «edición de imagen existente (T5)»: edición: quitar objeto · edición: añadir objeto ·
     edición: cambiar luz o clima · edición: colorizar · edición: restaurar · edición: traducir texto;
     + análisis de imagen a prompt.
   - F17 + anclado en época, cultura o autor · brutalista · futurista.
   - Las plantillas de un look concreto se tratan como biblioteca: se ofrecen por tipo de pieza y estilo y la
     confirmación elige como máximo una.
   - F10 + edición: cambiar vestuario · edición: cambiar mobiliario u objeto (consulta C2 del piloto).
   - F35 Migración de versión de modelo: sí · no (consulta C3 del piloto). Las reglas de migración llevan «sí»; la app
     trabaja con «no».
   - Campo unidad + imagen fija suelta (respuesta a la consulta U1 del piloto gpt-image.md).
   - Los textos sobre "14 o más referencias" o "grounding de lugar real" se cierran sin valor nuevo.
5. Toda etiqueta usada en la catalogación debe coincidir al 100% con la taxonomía original (o con una extensión
   aprobada, contada aparte). Si no coincide, se corrige y se repite hasta que coincida.
6. Las pruebas se hacen solo con GPT Image 2; otros modelos se añaden después.
7. quality en GPT Image 2 (consulta C1 del piloto): la elige el usuario; «medium como punto de partida» y «empieza con
   low» se le muestran como opciones. high sigue siendo obligatorio en los casos que la fuente lo exige.
8. Biblioteca de prompts efectivos (precisada por Eric el 2026-10-23):
   - Después de cada generación, el usuario puede subir la imagen o el video para evaluarlo: revisión visual más
     la opinión del usuario. Si se llega a un acuerdo sobre la calidad, el prompt se guarda con su trazabilidad al
     caso específico (brief validado, facetas, reglas aplicadas, parámetros, archivo generado).
   - Cuando un brief nuevo tiene como mínimo 85% de similitud con los datos del brief que generó ese prompt, se le
     sugiere al usuario ir directo por ese prompt sin generar de nuevo. El usuario decide.
   - Se implementa después de cerrar el catálogo. Corresponde en la taxonomía a E5.7 crítica, E5.9 canonizar,
     «Canonizada» y «Observación de ejecución».
