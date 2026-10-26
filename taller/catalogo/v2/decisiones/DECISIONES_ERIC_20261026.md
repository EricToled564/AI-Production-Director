# Decisiones de Eric Toledano — 2026-10-26

Fuente: sesión `session_01RkzWqCTfrzRXTVrroB7zfi`, mensajes de Eric citados textualmente.

1. **Cuando un texto da una cifra que no es la de GPT Image 2, vale la cifra que el corpus da para GPT Image 2**, y el
   texto se corrige para que la especifique: «entonces las que valen son las que da el corpus, modifica el texto para
   que especifique el número de GPT 2».
   - Primer caso: INV-002054 (`skills/image/references/characters.md:3`). Original: «Up to 14 reference images
     (6 high-fidelity)», el desglose de Nano Banana Pro (`nano-banana.md:64-66`, `:144`). Corregido: «Up to 16
     reference images, each indexed with its role (GPT Image 2; high fidelity by default)» (`SKILL.md:43`,
     `gpt-image.md:96`, `:102`, `:104`, `golden-rules.md:93`, `models.md:54`).
   - La base de 13,005 textos no se modifica (está fijada por sha256). Las correcciones viven en
     `v3/universo/correcciones.json` y las aplica `v3/universo/textos_universo.py`.
2. «No estás aprobado para asumir nada, siempre lo verificas»: toda afirmación sobre un texto se comprueba leyendo el
   documento completo y su jerarquía hacia arriba, no por coincidencia de números o palabras.
3. «Siempre que hay una supuesta contradicción o incoherencia tienes que leer exhaustivamente los textos
   relacionados»: ninguna contradicción se declara, se corrige ni se marca sin haber leído completos todos los textos
   del corpus que tratan el mismo punto, con su sección y su jerarquía de carga.
4. **Interfaces de GPT Image 2: OpenAI API y fal.ai** (respuesta a la decisión 1 de 6). Manda
   `image/references/gpt-image.md:78` («`openai/gpt-image-2/edit` (на fal.ai) или соответствующий через OpenAI API»)
   sobre `visual-prompt-forge/adapters/gpt-image.md:94` («GPT Image is OpenAI-only as of Q2 2026»): DEC-000002
   («6.2 solo aplica si no hay archivo smixs») y T-BRIEF-IMG §1 (gpt-image.md gobierna GPT Image 2; `_capabilities.json`
   no se extrapola). `correr.py` conserva `INTERFACES = ("OpenAI API", "fal.ai")`.
5. **F20 con una sola persona que debe seguir reconocible: «todas»** (decisión 2 de 6). Base: TRM-0175 (taxonomía L1220,
   «cada persona del cuadro debe mantener un rostro reconocible») y L1210 (reconocimiento separado de cantidad). Aplica a
   C1 y B6; con edición activa INV-002352 A3 (quality high).
6. **Extensión F24 + «objeto entero»** (decisión 3 de 6): un objeto completo como sujeto del cuadro. Los 8 valores
   originales describen el sujeto por el cuerpo (taxonomía L1329–1336). Se registra en `v2/construir_esquema.py` con
   origen `extension_aprobada_2026-10-26`, aparte de la taxonomía original. Primer uso: C2 (póster del saxofón).
7. **F05 de B1 y B4 deja de ser lista vacía** (decisión 4 de 6; la lista vacía viola taxonomía §1.12.8): B1 (pescadora en
   el muelle) = «hospitalidad y viajes»; B4 (cocina, artículo de estilo de vida) = valor nuevo «estilo de vida», extensión
   de F05 registrada en `v2/construir_esquema.py`. Ninguna regla del piloto condiciona F05: la selección no cambia.
