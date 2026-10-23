# Templates revisados de entrada y salida: imagen y orquestación

Versión documental 20261019. Contratos rellenables. No constituyen un catálogo reclasificado ni una integración verificada de las 1887 reglas históricas. Los marcadores {{campo}} son variables del template, nunca contenido permitido de un prompt final.

## 1. Autoridad y alcance
La taxonomía corregida y las decisiones vigentes gobiernan clasificación y exclusiones. El texto original conserva autoridad sobre su materia y alcance de modelo/operación. El archivo específico image/references/gpt-image.md gobierna cinco slots de GPT Image 2 y tres de edición: la indicación genérica de tres párrafos del adaptador no se utiliza para alterar esa estructura. Los parámetros de _capabilities.json gobiernan exclusivamente los adaptadores/versiones que declara; no se extrapolan a variantes posteriores. La prohibición del usuario de la palabra photorealistic en sus prompts sustituye ese literal donde los adaptadores lo sugieren; se conserva el efecto mediante atributos observables. Un mandato genérico de empezar con verbo no añade un prefijo antes de Scene:; puede expresarse dentro del contenido sin destruir el contrato específico.
Este paquete cubre entrada/salida de imagen, FF/LF incluidos, y compuertas de orquestación. Video, audio, preproducción integral y postproducción tienen contratos de enlace en contratos_externos; registrar ese destino no implementa esas fases. No se cambian textos originales ni se inventan reglas para rellenar categorías.

## 2. Secuencia obligatoria de uso
1. Seleccionar flujo, operación, modelo/versión/interfaz y función del activo.
2. Recoger valores del usuario y documentos aprobados; proponer inferencias explícitas.
3. Activar campos dependientes por condiciones e IDs taxonómicos; resolver cada dato requerido y conflicto. Las preguntas se gestionan fuera del registro de clasificación, nunca como etiqueta de regla.
4. Mostrar el brief completo, con origen e inferencias y todas sus dependencias resueltas.
5. Registrar aprobación vinculada al hash exacto del brief.
6. Solo entonces ejecutar selección definitiva: universales del dominio, específicas, sintaxis, valores de campo, consultas, controles y efectos de orquestación. El esquema estable de campos puede consultarse antes; eso no es selección definitiva.
7. Compilar mediante operación + adaptador. Verificar mismo caso y compatibilidad antes de compactar; conservar todas las obligaciones después.
8. Validar salida, entregar prompt y parámetros separados; ejecutar generación únicamente con contrato técnico suficiente.
9. Criticar el activo, registrar evidencia y canonizar solo al cumplir las compuertas.
Ningún campo vacío o pregunta abierta habilita selección definitiva. Ninguna regla recibe NO APLICA, pendiente o desconocido como clasificación. Una omisión legítima de un campo de una instancia no modifica las etiquetas de una regla. Un contrato técnico insuficiente bloquea la ejecución, no la recuperación de reglas pertinentes.

## 3. Ficha rellenables T-BRIEF-IMG
El schema es la forma estructurada de esta ficha. La procedencia se registra por campo para no mezclar texto de usuario con inferencias. Orden de presentación: ruta → modelo/operación → uso/formato → sujetos/acción → escena/estilo → composición/cámara → iluminación/materiales → referencias/identidad → módulos de ancla/edición/texto → restricciones → aprobación.

| Campo exacto | Tipo | Cuándo se exige | Facetas |
|---|---|---|---|
| entrada.ruta.flujo | string | siempre | P-01 |
| entrada.ruta.seccion | string | si fuente define sección | F01 |
| entrada.ruta.etapa | string | cuando la operación, módulo o fuente lo exige | F01 |
| entrada.ruta.paso | string | cuando la operación, módulo o fuente lo exige | F02 |
| entrada.ruta.operativa | string | si existe ruta operativa en contexto | F03 |
| entrada.operacion | string | siempre | F10 |
| entrada.modelo.nombre | string | siempre | F29 |
| entrada.modelo.version | string | siempre | F29 |
| entrada.modelo.interfaz | string | siempre | F29 |
| entrada.pieza.tipo | string | siempre | F04 |
| entrada.pieza.tematica | array_string | si el caso tiene tema/sector | F05 |
| entrada.pieza.objetivo | string | siempre | F30 |
| entrada.pieza.uso | string | siempre | F04,F12 |
| entrada.formato.ratio | string | siempre | F06 |
| entrada.formato.ancho_px | integer | cuando contrato usa tamaño píxel | F06 |
| entrada.formato.alto_px | integer | cuando contrato usa tamaño píxel | F06 |
| entrada.formato.resolucion | string | cuando contrato usa resolución nominal | F06 |
| entrada.idioma_prompt | string | siempre | E |
| entrada.sujetos.cantidad | integer | cuando la operación, módulo o fuente lo exige | F19 |
| entrada.sujetos.items[].id | string | cada sujeto descrito | E |
| entrada.sujetos.items[].clase | string | cada sujeto descrito | F15 |
| entrada.sujetos.items[].descripcion | string | cada sujeto descrito | F15 |
| entrada.sujetos.items[].edad | number | si se prescribe edad | F15 |
| entrada.sujetos.items[].genero | string | si se prescribe | F15 |
| entrada.sujetos.items[].rasgos | array_string | si se prescriben | F15 |
| entrada.sujetos.items[].cabello | string | si se prescribe | F15 |
| entrada.sujetos.items[].vestuario | string | si se prescribe | F15 |
| entrada.sujetos.items[].expresion | string | cuando expresa emoción | F13 |
| entrada.sujetos.items[].posicion | string | si hay disposición espacial | F30 |
| entrada.accion.tipo | string | cuando la operación, módulo o fuente lo exige | F13 |
| entrada.accion.estado_visible | string | cuando la operación, módulo o fuente lo exige | F13 |
| entrada.accion.postura | string | si hay acción corporal | F13,F14 |
| entrada.accion.evidencia_fisica | array_string | si hay movimiento congelado | F14 |
| entrada.fisica.regimen | array_string | cuando la operación, módulo o fuente lo exige | F14 |
| entrada.escena.espacio | string | cuando la operación, módulo o fuente lo exige | F16 |
| entrada.escena.entorno | string | cuando la operación, módulo o fuente lo exige | F16 |
| entrada.escena.momento | string | si determina luz/acción | F16 |
| entrada.escena.clima | string | si tiene efecto visual | F16 |
| entrada.escena.planos | array_string | si la composición tiene capas | F30 |
| entrada.estilo | array_string | cuando la operación, módulo o fuente lo exige | F17 |
| entrada.representacion | array_string | cuando la operación, módulo o fuente lo exige | F18 |
| entrada.identidad.invariantes | array_string | si exige reconocimiento/continuidad | F20 |
| entrada.identidad.referencias | array_string | si identidad respaldada por referencias | F20,F23 |
| entrada.blocking.contactos | array_string | si hay contactos | F21 |
| entrada.blocking.relaciones | array_string | si hay múltiples elementos relacionados | F30 |
| entrada.rostro.ocupacion | number | si rostro visible y condiciona reglas; proporción 0..1 | F22 |
| entrada.rostro.detalles | array_string | si rostro visible | F30 |
| entrada.camara.plano | string | cuando la operación, módulo o fuente lo exige | F24 |
| entrada.camara.angulo | string | cuando la operación, módulo o fuente lo exige | F25 |
| entrada.camara.altura | string | cuando el ángulo requiere ubicación física | F25 |
| entrada.camara.efecto_optico | string | cuando la operación, módulo o fuente lo exige | F30 |
| entrada.camara.lente_intencion | string | cuando se prescribe óptica | F30 |
| entrada.luz.fuente | string | cuando la operación, módulo o fuente lo exige | F30 |
| entrada.luz.direccion | string | cuando la operación, módulo o fuente lo exige | F30 |
| entrada.luz.dureza | string | cuando la operación, módulo o fuente lo exige | F30 |
| entrada.luz.distribucion | string | cuando la operación, módulo o fuente lo exige | F30 |
| entrada.luz.contraste | string | cuando la operación, módulo o fuente lo exige | F30 |
| entrada.luz.specular | string | cuando afecta materiales | F30 |
| entrada.color_material.paleta | array_string | cuando la operación, módulo o fuente lo exige | F30 |
| entrada.color_material.grade | string | cuando tratamiento de color | F30 |
| entrada.color_material.materiales | array_string | cuando superficies relevantes | F30 |
| entrada.color_material.texturas | array_string | cuando superficies relevantes | F30 |
| entrada.color_material.acabado | string | cuando superficies relevantes | F30 |
| entrada.composicion | array_string | cuando la operación, módulo o fuente lo exige | F30 |
| entrada.referencias[].archivo | string | cada referencia | F23 |
| entrada.referencias[].sha256 | string | cada referencia | E |
| entrada.referencias[].medio | string | cada referencia | E |
| entrada.referencias[].rol | string | cada referencia | F23 |
| entrada.referencias[].indice | integer | cada referencia | F23 |
| entrada.referencias[].preservar | array_string | cada referencia con invariantes | F23 |
| entrada.restricciones | array_string | siempre; [] solo si no se impuso ninguna | F30 |
| entrada.contexto_narrativo.genero | array_string | si restringe activo | F07 |
| entrada.contexto_narrativo.beats | array_string | si restringe activo | F08 |
| entrada.contexto_narrativo.dialogo | string | si restringe efecto visible | F30 |
| entrada.contexto_secuencia.montaje | array_string | si restringe activo | F09 |
| entrada.plano.funcion | string | cuando la operación, módulo o fuente lo exige | F12 |
| entrada.publicacion.destino | string | si destino impone condiciones | P-04 |
| entrada.publicacion.ubicacion | string | si ubicación impone condiciones | P-04 |
| entrada.publicacion.literal | string | si fuente especifica publicación | P-04 |
| entrada.publicacion.fuente | string | si publicación citada | P-04 |
| entrada.ancla.rol | string | operación ancla | F11 |
| entrada.ancla.clip_id | string | FF/LF asociado clip | F11 |
| entrada.ancla.pareja_id | string | solo si exige pareja | F11 |
| entrada.ancla.estado_inicial | string | FF | F11 |
| entrada.ancla.estado_final | string | LF | F11 |
| entrada.ancla.invariantes | array_string | operación ancla | F20 |
| entrada.ancla.series_lock | string | ancla de proyecto con series lock | E |
| entrada.ancla.plan_anchors | string | ancla de proyecto con plan | E |
| entrada.ancla.contexto_clip.camara | string | FF/LF; estado o contexto efectivo, incluso cámara fija | F26 |
| entrada.ancla.contexto_clip.transicion | string | FF/LF; relación efectiva | F27 |
| entrada.ancla.contexto_clip.audio | string | FF/LF; contexto efectivo incluso silencio | F28 |
| entrada.ancla.contexto_clip.animacion | string | cuando condiciona frame | F30 |
| entrada.ancla.contexto_clip.duracion | number | cuando handoff lo requiere | E |
| entrada.ancla.contexto_clip.efecto_visible | string | si contexto sonoro tiene efecto visible | F28 |
| entrada.edicion.cambio | string | edición | F10 |
| entrada.edicion.preservar | array_string | edición | F10 |
| entrada.edicion.mascara | string | solo admitida por modelo/interfaz | F23 |
| entrada.transferencia.propiedades | array_string | transferencia de estilo | F10 |
| entrada.boceto.estructura_preservada | array_string | boceto a final | F10 |
| entrada.texto_marca.literales | array_string | texto integrado solicitado | F30 |
| entrada.texto_marca.posicion | string | texto integrado solicitado | F30 |
| entrada.texto_marca.tipografia | string | texto integrado solicitado | F30 |
| entrada.texto_marca.logos_aprobados | array_string | marca autorizada | F30 |
| entrada.texto_integrado_override.habilitado | boolean | Ideogram | F29,F30 |
| entrada.texto_integrado_override.rationale | string | Ideogram integrado | F29,F30 |
| entrada.grounding.objetivo | string | si grounding | F29 |
| entrada.grounding.evidencia | array_string | si grounding ejecutado | E |
| entrada.presupuesto.creditos_maximos | number | antes ejecución con costo | E |
| entrada.selecciones_taxonomicas | array_string | siempre | E |

Cada valor tiene procedencia_campos: path, origen, fuente, valor_sha256 y aprobacion_id. Origen toma usuario, herencia_aprobada, inferencia_para_aprobacion o fuente_documental. La aprobación global exige brief_sha256, mensaje_id y aprobado=true. La inferencia no se convierte en hecho por guardarse: debe aparecer en la revisión aprobada.

## 4. Tarjeta de ancla D1–D9
D1 rol → entrada.ancla.rol. D2 acción → entrada.accion. D3 sujetos → entrada.sujetos. D4 tratamiento → entrada.estilo/representacion. D5 paleta → entrada.color_material. D6 cámara → entrada.camara. D7 luz → entrada.luz. D8 modelo/resolución → entrada.modelo/formato. D9 ángulo/altura → entrada.camara.angulo/altura. Todos los nueve grupos se resuelven antes de compilar ancla. El original cita documentos externos; esa mención no equivale a haber recibido esos documentos.
Para FF/LF se completan cámara, transición y audio del contexto con datos positivos, incluido cámara fija o silencio cuando ese sea el caso aprobado. No se agrega una orden de animar ni audio al prompt fijo salvo el efecto visual que corresponda. Pareja solo cuando el caso la requiere; si existe, comprobar ratio, identidad, estado y vínculo. Génesis de proyecto hereda series_lock y plan_anchors cuando existen.

## 5. Contratos por operación

### T-GENESIS
Activación: entrada.operacion = genesis. sin referencias adjuntas.
Campos adicionales: entrada.sujetos, entrada.pieza, entrada.escena.
Salida: prompt bajo adaptador elegido, parámetros separados, referencias indexadas, validaciones y traza. La operación no autoriza trasladar capacidades entre modelos.

### T-REF-COMP
Activación: entrada.operacion = composicion_referencias. roles y preservaciones explícitos por imagen.
Campos adicionales: entrada.referencias, entrada.blocking.
Salida: prompt bajo adaptador elegido, parámetros separados, referencias indexadas, validaciones y traza. La operación no autoriza trasladar capacidades entre modelos.

### T-ANCLA-REF
Activación: entrada.operacion = ancla_referencia. character ref / environment ref / hero-macro / motif insert.
Campos adicionales: entrada.ancla.rol, entrada.ancla.invariantes.
Salida: prompt bajo adaptador elegido, parámetros separados, referencias indexadas, validaciones y traza. La operación no autoriza trasladar capacidades entre modelos.

### T-ANCLA-FF
Activación: entrada.operacion = ancla_ff. fotograma inicial visible; movimiento separado en handoff.
Campos adicionales: entrada.ancla.estado_inicial, entrada.ancla.contexto_clip.camara, entrada.ancla.contexto_clip.transicion, entrada.ancla.contexto_clip.audio.
Salida: prompt bajo adaptador elegido, parámetros separados, referencias indexadas, validaciones y traza. La operación no autoriza trasladar capacidades entre modelos.

### T-ANCLA-LF
Activación: entrada.operacion = ancla_lf. fotograma final visible; pareja solo cuando requerida.
Campos adicionales: entrada.ancla.estado_final, entrada.ancla.contexto_clip.camara, entrada.ancla.contexto_clip.transicion, entrada.ancla.contexto_clip.audio.
Salida: prompt bajo adaptador elegido, parámetros separados, referencias indexadas, validaciones y traza. La operación no autoriza trasladar capacidades entre modelos.

### T-EDIT
Activación: entrada.operacion = edicion. un cambio por iteración; preservar invariantes.
Campos adicionales: entrada.edicion.cambio, entrada.edicion.preservar, entrada.referencias.
Salida: prompt bajo adaptador elegido, parámetros separados, referencias indexadas, validaciones y traza. La operación no autoriza trasladar capacidades entre modelos.

### T-STYLE
Activación: entrada.operacion = transferencia_estilo. transferir propiedades visibles seleccionadas, preservar contenido indicado.
Campos adicionales: entrada.transferencia.propiedades, entrada.referencias.
Salida: prompt bajo adaptador elegido, parámetros separados, referencias indexadas, validaciones y traza. La operación no autoriza trasladar capacidades entre modelos.

### T-SKETCH
Activación: entrada.operacion = boceto_a_final. conservar estructura aprobada del boceto.
Campos adicionales: entrada.boceto.estructura_preservada, entrada.referencias.
Salida: prompt bajo adaptador elegido, parámetros separados, referencias indexadas, validaciones y traza. La operación no autoriza trasladar capacidades entre modelos.

## 6. Templates de salida por modelo
Los textos siguientes son formularios rellenables; solo los bloques completamente sustituidos van al generador. Los límites citados son contratos documentales del corpus, no una declaración de API vigente.

### GPT2-GEN
Modelos: GPT Image 2. Operaciones: genesis, composicion_referencias, ancla_referencia, ancla_ff, ancla_lf, transferencia_estilo, boceto_a_final.
Fuente: image/references/gpt-image.md#5-slots.
```text
Scene: {{escena}}
Subject: {{sujeto_accion}}
Important Details: {{detalles_visuales}}
Use Case: {{uso}}
Constraints: {{restricciones}}
```
Parámetros separados: quality, tamano.



### GPT2-EDIT
Modelos: GPT Image 2. Operaciones: edicion.
Fuente: image/references/gpt-image.md#Editing.
```text
Change: {{cambio_unico}}
Preserve: {{invariantes}}
Constraints: {{restricciones}}
```
Parámetros separados: quality, tamano.



### NB-PROSE
Modelos: Nano Banana 2, Nano Banana Pro, Nano Banana 2 Lite. Operaciones: genesis, ancla_referencia, ancla_ff, ancla_lf, transferencia_estilo, boceto_a_final.
Fuente: image/references/nano-banana.md#Стиль-промпта.
```text
{{sujeto_y_accion}}. {{lugar_y_contexto}}. {{composicion_luz_propiedades}}. {{estilo_observable_y_formato}}.
```
Parámetros separados: image_size.



### NB-COMP
Modelos: Nano Banana 2, Nano Banana Pro, Nano Banana 2 Lite. Operaciones: composicion_referencias.
Fuente: image/references/nano-banana.md#Multi-Reference.
```text
{{lineas_Image_indice_rol}}
Combine: {{elementos_por_referencia_e_invariantes}}. Match {{luz_perspectiva_escala}}.
```
Parámetros separados: image_size.



### NB-EDIT
Modelos: Nano Banana 2, Nano Banana Pro, Nano Banana 2 Lite. Operaciones: edicion.
Fuente: image/references/nano-banana.md#Editing.
```text
{{cambio_concreto}}. {{sustitucion_coherente_si_requerida}}. Keep {{invariantes}} exactly the same.
```
Parámetros separados: image_size.



### NB-COMPLEX
Modelos: Nano Banana 2, Nano Banana Pro, Nano Banana 2 Lite. Operaciones: genesis, composicion_referencias.
Fuente: image/references/nano-banana.md#JSON.
```json
{
  "subject": {
    "description": "{{sujeto}}",
    "expression": "{{expresion_postura}}"
  },
  "photography": {
    "angle": "{{angulo}}",
    "shot_type": "{{plano}}",
    "aspect_ratio": "{{ratio}}"
  },
  "background": {
    "setting": "{{entorno}}",
    "lighting": "{{luz}}"
  }
}
```
Parámetros separados: image_size.
escena compleja de cinco o más elementos y modo JSON elegido explícitamente


### FLUX-GEN
Modelos: Flux. Operaciones: genesis, ancla_referencia, ancla_ff, ancla_lf.
Fuente: visual-prompt-forge/adapters/flux.md#Syntax-pattern.
```text
{{sujeto_accion_composicion}}. {{entorno_luz}}. {{especificacion_visual}}. {{tratamiento_marca_si_corresponde}}.
```
Parámetros separados: aspect_ratio, seed, prompt_upsampling.



### MJ-GEN
Modelos: Midjourney. Operaciones: genesis, ancla_referencia, ancla_ff, ancla_lf.
Fuente: visual-prompt-forge/adapters/midjourney.md#Syntax-pattern.
```text
{{sujeto}}, {{accion}}, {{composicion}}, {{entorno}}, {{luz}}, {{color_tratamiento}}, {{estilo}} --ar {{ratio}} {{flags_admitidos}}
```
Parámetros separados: flags.



### IDEOGRAM-COMPOSITED
Modelos: Ideogram. Operaciones: genesis, ancla_referencia, ancla_ff, ancla_lf.
Fuente: visual-prompt-forge/adapters/ideogram.md#Mode-1.
```text
{{sujeto_composicion}}. {{entorno_luz}}. {{tratamiento_visual_espacio_para_overlay_si_requerido}}.
```
Parámetros separados: aspect_ratio, seed, magic_prompt, style_type.
texto_integrado_override.habilitado=false


### IDEOGRAM-TEXT
Modelos: Ideogram. Operaciones: genesis, ancla_referencia, ancla_ff, ancla_lf.
Fuente: visual-prompt-forge/adapters/ideogram.md#Mode-2.
```text
{{sujeto_composicion}}. {{entorno_luz}}. The text "{{literal_exacto}}" appears {{posicion}}, in {{tipografia}}. {{color_tratamiento}}.
```
Parámetros separados: aspect_ratio, seed, magic_prompt, style_type.
texto_integrado_override.habilitado=true y rationale aprobado


### SEEDREAM-GEN
Modelos: Seedream. Operaciones: genesis, ancla_referencia, ancla_ff, ancla_lf.
Fuente: visual-prompt-forge/adapters/seedream.md#Syntax-pattern.
```text
{{sujeto}}, {{accion}}, {{entorno}}, {{luz}}, {{tratamiento}}, {{nota_formato}}
```
Parámetros separados: aspect_ratio, seed, guidance_scale, steps.



### GPT15-GEN
Fuente: visual-prompt-forge/adapters/gpt-image.md, Syntax pattern. Tres párrafos:
```text
{{sujeto_accion_composicion_espacial}}

{{entorno_objetos_contexto}}

{{iluminacion_especificacion_visual_tratamiento}}
```
Parámetros separados: size y quality con valores respaldados para interfaz/versión. No heredar de este adaptador tamaños de GPT2. GPT15-EDIT usa el patrón de cambio concreto, preservaciones y restricciones respaldadas en image/references/gpt-image.md; input_fidelity high conserva su alcance de versión y operación.

### GPT-IMAGE-1-MIGRATION
Modelos: gpt-image-1. Operaciones: edicion.
Fuente: image/references/gpt-image.md#Migration-from-Older-GPT-Image.
```text
{{instruccion_respaldada_para_version}}
{{preservaciones_y_restricciones_respaldadas}}
```
Parámetros separados: exclusivamente los respaldados por el contrato exacto de versión.

Vincular contrato de versión/interfaz y prueba de sintaxis antes de ejecutar; la fuente enumera la variante pero no acredita una sintaxis completa nueva. Las reglas conservan elegibilidad. GPT1.5/1 object-removal puede citar input_fidelity high; no transferirlo a GPT2.

### GPT-IMAGE-1-MINI-MIGRATION
Modelos: gpt-image-1-mini. Operaciones: genesis.
Fuente: image/references/gpt-image.md#Migration-from-Older-GPT-Image.
```text
{{instruccion_respaldada_para_version}}
{{preservaciones_y_restricciones_respaldadas}}
```
Parámetros separados: exclusivamente los respaldados por el contrato exacto de versión.

Vincular contrato de versión/interfaz y prueba de sintaxis antes de ejecutar; la fuente enumera la variante pero no acredita una sintaxis completa nueva. Las reglas conservan elegibilidad. GPT1.5/1 object-removal puede citar input_fidelity high; no transferirlo a GPT2.

### Reglas de serialización de variantes
Nano Banana: 1–2 párrafos naturales en ruta normal; sin cifras ópticas 50mm/f2.8/ISO, describir efecto visible. En referencias, índice y rol real; no inventar entradas. NB2 Lite solo resolución 1K según fuente; NB2/NBP tienen límites por rol distintos, no sumar ciegamente las cuotas. El modo JSON es una alternativa explícita de escena compleja, no reemplazo universal. Grounding de la fuente NB2 se limita a objetos/lugares/especies, no identidad de personas.
GPT Image 2: Scene / Subject / Important Details / Use Case / Constraints en generación. Edición Change / Preserve / Constraints y un cambio. Referencias indexadas con rol. Quality y size fuera del prompt. No trasladar input_fidelity de modelos anteriores. Los patrones especializados de texto/infografía se documentan como módulos que conservan la información exigida; no sustituir automáticamente los cinco slots sin resolver la autoridad específica de su operación.
Midjourney: frases con comas y sufijo de flags documentados para la versión. Flux: frases completas y parámetros fuera. Seedream: frases cortas con comas, parámetros fuera. Ideogram: modo integrado requiere override y rationale; literal en comillas rectas, ubicación y tipografía. Mode 1 conserva el texto para composición externa.
Techos editoriales históricos: MJ v7=100, Flux 2 Pro=150, Ideogram v3=120, GPT familia1.5/2=300, Seedream4.5=120 palabras. NB Gemini2.5=120 no se traslada a NB2/NBP/Lite. Antes de ejecutar cada interfaz se verifica su contrato. La longitud nunca se resuelve suprimiendo reglas aplicables.

## 7. Salida común rellenables
```text
Model: {{modelo_version_interfaz}}
Quality: {{solo_si_modelo_lo_admite}}
Size / Ratio: {{formato_aprobado}}

Prompt:
{{prompt_compilado_sin_variables}}

Notes:
{{inferencias_ya_aprobadas_y_condiciones_de_entrega}}
```
Acompañan como registros separados salida.parametros, salida.referencias, salida.validaciones, salida.traza y salida.notas_entrega. Una traza no se concatena al prompt. La cabecera se omite cuando el usuario copia solo el texto destinado al modelo.

## 8. T-ORQ: contrato ejecutable de eventos y gates
Entrada: evento, paso, condición estructurada, datos de brief y evidencia previa. Salida: acción, compuerta, evidencia. Cada compuerta declara gate_id, condición, entradas, responsable, criterio, evidencia requerida y pasos habilitados. Solo solicitar OK humano donde la fuente/DEC lo exige.
Gates base: completar brief → aprobar hash → seleccionar reglas → resolver compatibilidad → compilar → validar → ejecutar → revisar activo → canonizar/entregar. El recorrido concreto activa los gates que corresponden y registra los que ejecutó. Una estructura diseñada no acredita ejecución.

## 9. T-ACEPTACIÓN y T-TRAZA
Registro de aceptación: activo/hash, prompt/hash, modelo/versión, brief/hash, resultados por control, detalles auditados, ronda, corrección requerida y evidencia del resultado. El archivo critique.json se materializa desde salida.aceptacion.critique; el hash de canonización corresponde al archivo real, no al nombre. La auditoría de tres detalles contiene tres detalles observables pertinentes y su evidencia; una plantilla vacía no la satisface. Cuando dramaturgia exige sus seis controles, se conservan los seis criterios fuente, sin reemplazarlos por un check genérico.
Cada aplicación real enlaza regla_id, aplicacion_id, ítems taxonómicos, fuente literal/documento/encabezado/página, condición, campo de brief, efecto, destino y prueba. Las decisiones incluyen identificador y cita literal verificable. El texto de un mensaje Sentinel sin resolver su autoría no acredita una DEC.

## 10. Cobertura y validación
REGISTRO_DESTINOS_TEMPLATE.json resuelve 31 facetas, extensiones, metadatos y 24 materias F30 a rutas existentes del schema. FIELD_MAP.csv permite auditoría. Las opciones del catálogo de casos deben materializar estas rutas por ítem, no solo escribir “hereda”.
El programa verificar_templates.py comprueba integridad de rutas y contratos. Esta prueba acredita estructura de los templates; no acredita pertinencia de clasificación ni selección exhaustiva del corpus. Los enlaces reales de reglas se rellenan y prueban durante clasificación. No se reutiliza la tabla histórica de 1887 como si hubiese sido revisada.

## 11. Fuentes y atribución
Fuentes suministradas y hashes en FUENTES_CONTRATOS.json. Los extractos y adaptaciones de image corresponden a Serge Shima, github.com/smixs/visual-skills, licencia CC BY 4.0; se mantienen atribución y referencia. Este paquete es una adaptación documental en español con esquemas de implementación añadidos. La fuente original se conserva intacta.

## 12. Obligatoriedad revisada por módulo
BASE exige ruta de flujo, operación, modelo/versión/interfaz, tipo/objetivo/uso, ratio, idioma, restricciones y selecciones taxonómicas. Los contratos de operación añaden sus campos. Cámara y luz detalladas se exigen en el módulo fotografía cuando hay que definir la toma; no se exige inventarlas para un icono, plano abstracto o una edición que ya las preserva. Acción física, sujetos y materialidad son módulos condicionales distintos. Cada activación se justifica por el caso aprobado y la fuente. En anclas, D1–D9 se resuelven con los datos positivos pertinentes de su representación. El archivo CONTRATOS_OPERACION_MODELO.json contiene los required_fields exactos, y el verificador evalúa operación más módulos activos. Ningún campo opcional equivale a una categoría NO APLICA de una regla.
