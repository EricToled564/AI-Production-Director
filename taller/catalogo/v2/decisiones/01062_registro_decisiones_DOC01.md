# Registro de decisiones del usuario sobre DOC01
Fuente separada de skills/ai-production-director/SKILL.md (sha256 687c2eda93647dce1b94b04938a1fd52b70a48cc5e34a972dfea2d428922df34); las decisiones no forman parte del texto original del documento. Cada decisión es una unidad DEC-nnnnnn con su texto tal como se recibió (con sus erratas).

## DEC-000001
[Mensaje del usuario] esraba ya decididio que si derrnate la clasificacin neneceustabqmos ampliar la taxonomi entoncers lo hacuamos auqi es un claor ejemplp d euq evamos ancestar una seccion der orquestracion
[Respuesta del usuario a «¿Cómo amplío C18 para las reglas de orquestación?»] Ámbito + materia F30 (Recomendado): nuevo ámbito P-05 «Orquestación y control de flujo» y nuevo valor F30 «orquestación y control de flujo».

## DEC-000002
[Mensaje del usuario] tu ;ectura es cirrecta  6.2 solo aplica si no jhat archivo smixs

## DEC-000003
[Respuesta del usuario a «¿Qué etapas NO se ejecutan en modo EXPRESS?»] Solo 1 y 2 (literal): la línea 57 dice solo «salta estrategia formal y guion»; las etapas 0, 3 y 7 SÍ aplican en EXPRESS.

## DEC-000004
[Mensaje del usuario] Esta regla practicamente no tiene sentodo porque no hay sustituto, lo que se debe de poner es lo siguinete y es una reg;a de orquestracion si existe algun caso d euso especifico para lo cual no existe na regla que soluciona entonces se debe de levar a la ataneicon dle usuario y solicitar persomiso para investigacion en linea sobre reglas disponible spara solucionar el caso, una vez que dichas reglas se hallan probado con exito en una ejecucion real se pedira al usuario sua autorizacion para agregarlas al catalago

## DEC-000005
[Respuesta del usuario a «Sustitutos de §8: existen 3 … ¿Los mantengo y añado tu regla de escalamiento para todas las sub-skills sin sustituto?»] Mantener los 3 + gate + tu regla (Recomendado).
[Mensaje del usuario] si hay sistitutos definidios entiojces los mencionas o los catalogas para el caso y las regla spara los cuales hy susutitutios pero de todaas forma sno hace sentido porque tenemos tanto la regla original como el sustituti por loq ue esa regl nunca se epliocaroa

## DEC-000006
[Respuesta del usuario a ««los dos» (x6/x_rev4_1) en la regla de los chequeos: ¿a quiénes se refiere?»] Los dos chequeos de video (Recomendado).

## DEC-000007
[Respuesta del usuario a «Etapa 0 (brand-lock): ¿se ejecuta cuando es pieza de autor / cliente SIN marca formal?»] No: solo Visual Theme (Recomendado): la Etapa 0 corre solo si hay marca/cliente con marca formal; sin marca formal se usa el Visual Theme ligero y se omite brand-lock-extractor.

## DEC-000008
[Respuesta del usuario a «Gate de la Etapa 0 (confirmar valores estimados) vs «los demás gates avanzan solos»»] Gate 0 exige OK; en EXPRESS avanzan solos (Recomendado): los gates 0, 1, 2 y 4 requieren OK explícito del usuario en STANDARD/FILM; los demás avanzan solos. En EXPRESS solo se exige OK al shot list y el resto avanza solo.

## DEC-000009
[Mensaje del usuario] tienes que difremeciar asi, para evitar confuisiiones un film pubicitario es el flijo mqs largo y para ese aplican todas las etapas sin excepcion, para un clip de video se le deben de dar al uaurio todas las etapas del proeceso de prep produccion y preguntarle cuales quiere mantener, por eso el menu inicial debe de ser Video publicitarioo (flujo completo) , clip (secciones de la pre a elegir), Imagen genesis, imagen ancla sin referemci, y imagen ancla con referencia, Edicion de imagen y ve si habria otras opciones

## DEC-000010
[Mensaje del usuario] la durcion no tiene nda que ver el usuaruio debe de elegir

## DEC-000011
[Respuesta del usuario a «Tracks y menú inicial: … ¿cómo lo catalogo?»] Texto + decisión que lo reemplaza (Recomendado): las reglas del texto sobre EXPRESS/STANDARD/FILM y el criterio por duración se catalogan tal cual con adopción «excluida por decisión del usuario» (reemplazadas); se añaden reglas de orquestación con origen «Decisión del usuario», no DOC01.

## DEC-000012
[Delegación del usuario] y ve si habria otras opciones
[Propuesta comunicada al usuario el 2026-10-04, sin objeción] Entradas adicionales del menú inicial según el corpus: Storyboard aislado (storyboard-architect), Guion/screenplay (screenwriter), Prompt suelto de video (video y sus 2 checks), Crítica de un render (visual-asset-critic), Brand-lock de una marca (brand-lock-extractor), Preview HTML de storyboard (storyboard-html-preview), Consulta de cine/animación (visual-media) e Imagen a video.

## DEC-000013
[Respuesta del usuario a «Tres ambigüedades de alcance de DOC01 (x_rev22_1, x_rev22_2, x_r30_4)»] Aprobar las 3 lecturas (Recomendado): (1) la lista de tipos de pieza (spot, campaña, reel…, línea 4) es ilustrativa: cualquier video completo activa el skill; (2) «teoría de cine → visual-media» es un tercer caso de invocación de visual-media, además de animación y material en español; (3) en live-action, visual-media solo participa para material didáctico o de cara al cliente en español (caso 2), no en el pipeline.

## DEC-000014
[Respuesta del usuario a «Shots y entrega (x_r30_3/x_rev33_2, x_r28_2, x_r24_1, x_rev22_4)»] Aprobar las 4 lecturas (Recomendado): (1) shots.json es fuente de verdad desde la Etapa 4 cuando existe; si no existe (flujo con ai-video-storyboard e IDs manuales), la fuente de verdad es ese shot list y la prohibición de parchear un prompt contra su shot rige igual; (2) la trazabilidad shot→escena→concepto (línea 20) exige solo los eslabones de etapas ejecutadas; (3) la línea de créditos smixs va en los créditos del production package y, si el flujo no genera paquete, acompaña al entregable final; (4) «Solo track EXPRESS» de ai-video-storyboard es restricción de uso: se usa solo en el flujo Clip (y como sustituto de storyboard-architect).

## DEC-000015
[Mensaje del usuario] no el shot nunca se reconsidera  amenos que el usuario lo pida, lo que e sustema  hace es reevaluar el set de reglas y si fakka una vez mas entonce shacer bsuqyedas en lineas con el caso de uso especifuici y formula runa recomendacion

## DEC-000016
[Respuesta del usuario a «Ámbito de reglas de flujo y de prompts (x_r4a_1, x_rev33_3, x_r30_6, x_r30_8)»] Aprobar las 4 lecturas (Recomendado): (1) «si falla, se corrige en la etapa actual, nunca se arregla después» es control de flujo: ámbito Orquestación y control de flujo; (2) la revisión selectiva del forge tiene una aplicación en Crítica, validación y aceptación y otra en Creación de imagen (reemisión de prompts); (3) las reglas de prompts de ai-video-storyboard (cierre anulado, model-agnostic) aplican también a Preproducción (shot list de la Etapa 4), además de Creación de imagen/video; (4) «resolución, aspect ratio, duración y audio como parámetros según el archivo del modelo» es principio general para todo prompt de video.

## DEC-000017
[Respuesta del usuario a «Etapas y gates (x_rev33_1, x_r4a_2, x_r4a_p1_1, x_r28_3/x_r4a_p1_3, x_rev22_6)»] Aprobar las 5 lecturas (Recomendado): (1) Etapa 1: la regla de carga se cumple nombrando y leyendo references/creative-strategy.md (su módulo), porque no tiene sub-skill; (2) el OK explícito del usuario en gates 0, 1, 2 y 4 es del gate completo; cada criterio lo verifica el agente; (3) si la etapa anterior no se ejecuta (sin marca formal, o etapas omitidas en Clip), el gate previo exigido es el de la última etapa ejecutada; (4) «entra en la etapa correspondiente» = la etapa siguiente a la del último artefacto aportado (un script → Etapa 3; un shots.json → Etapa 5); no se repite trabajo hecho; artefactos de Etapa 7 no aplican; (5) en Clip, las Etapas 5 y 6 se ejecutan comprimidas (sin loop de crítica salvo petición del usuario) porque el texto no define otra compresión.

## DEC-000018
[Mensaje del usuario] no se como solucuonar esto pero si debemos de tener un tracking de las versiones y en cuento slaga una nueva debemos de identificar todas lassregklas ligadas al modleo y redefinrlas ocn bas ene la nueva version, entonce shay dis opcione sun sub proeeso de refres de las reglas por modelo o de la adicion d eun modelo nuevo, en la que el usuario manualmente selecciona el modelo para el que hay una nueva version  triguerea la identificacion d etodas lasreglas ligadas a la version anterior del modelo y la investiogacion en klinea de la nueva version d etales reglas para que depsues suisyituan las antiguas dejando un registro en eln log de camnios y oara agregar un nueov modelo, se deifneel modelo por el usuairo y el sistema identifia todas klas categoras exustentes para el tipo d emodelo (iagen o vodeo) en la taxonomia y entojes va y busca la syntaaixis tde las rega spara duicjo modelo en libne apresenta para aprobacion y agrega al sustem

## DEC-000019
[Respuesta del usuario a «Precedencia y nombres (x_r30_2, x_r24_3, x_r30_5)»] aqui como no estan instaladas separadamente no hace sentido decir eso no rees?
[Lecturas (1) y (2) de esa pregunta, sin objeción del usuario] (1) §6 (resolución de conflictos, línea 123) prevalece sobre la línea 14: es un conflicto ya resuelto por el director; (2) «(storyboard, shot cards)» son ejemplos de la clase «artefactos intermedios», no lista cerrada.

## DEC-000020
[Respuesta del usuario a «Piezas sueltas: descripción (línea 4) vs menú inicial (DEC-000009/012)»] promot suelto d ebidoe no entra eso es un clip uya te lo havia dicho peor klo ighniraste , peor fuers d eeso tu sugeriencia es cirrecta
[Opción recomendada que el usuario declara correcta] Menú manda; multi-etapa aplica: una pieza suelta se atiende por su entrada del menú (sub-skill directa); si el contexto revela un proyecto multi-etapa, el director se activa y lleva el flujo completo.

## DEC-000021
[Respuesta del usuario a «Reglas del mapa de capas (líneas 28–38): ¿se aplican igual si la sub-skill no está instalada?»] que sub skill no esta instalada
[Respuesta comunicada al usuario, sin objeción] Ninguna sub-skill del mapa falta en el corpus (11 SKILL.md presentes); la línea 146 solo prevé sustituto para tres casos (brand-lock-extractor, storyboard-architect y el crítico); las descripciones del mapa rigen siempre y la degradación se rige por la línea 146 y por la regla de escalamiento (DEC-000004).

## DEC-000022
[Respuesta del usuario a «Clip vs tracks: DEC-000011 excluye las reglas del texto sobre EXPRESS/STANDARD/FILM, pero DEC-000003/008/014/017 describen comportamientos de Clip idénticos a lo que el texto decía de EXPRESS: ¿cómo lo reconcilio?»] Clip hereda solo lo ya aprobado (Recomendado): el texto de tracks (REG-000034 a REG-000049) queda excluido tal cual; STANDARD excluido; FILM ≙ Video publicitario. Lo que DEC-000003/008/014/017 aprobaron para Clip se re-expresa como reglas de Clip con origen «Decisión del usuario». Las Etapas 1 y 2 en Clip se ejecutan si el usuario las mantiene (ya no se omiten por defecto).

## DEC-000023
[Respuesta del usuario a «En Clip con la Etapa 4 (shot planning) mantenida, ¿qué sub-skill hace el shot planning?»] den serio me estas preguntando eso? eso claramente deveria de estar definidio o por la regla misma o por el header d elaseccion en la qwue se necuerntra
[Respuesta del usuario a «Si el shot falla otra vez tras reevaluar el set de reglas (DEC-000015), ¿la búsqueda en línea necesita permiso previo del usuario como en DEC-000004?»] No, DEC-000015 ordena buscar directamente (Recomendado)
[Mensaje del usuario] pero el sistema debe de miostarr evidencia cuantitativa de uq e la busqyeda en linea fue ehecha

## DEC-000024
[Mensaje del usuario] las licencias la saplicas al sustemna una vez y ya, y no quieor que parezca ningun tipop de TRUBUCION A UN TERCERO EN NINGUN MATEIRLA QE VA AL CLINETE

## DEC-000025
[Mensaje del usuario] LPS TEMPLATES DEBEN DE SEHUIRO LA S REGLAS D ESUNTAXIOS D ELOS MODELOS QUE SE APLICNA UNA VEZ AL TEMPLATE Y NO SE VUELVEN A EXTARER

