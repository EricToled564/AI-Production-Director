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
