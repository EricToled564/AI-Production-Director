# Registro de lectura — metodología de clasificación (2026-10-27)

Leídos para escribir el plan de construcción del sistema (solo GPT Image 2, sin pruebas: instrucción de Eric de esta
fecha).

| Documento | Lectura | Qué dice (línea) | Consecuencia |
|---|---|---|---|
| `fuentes_20261019/PLAN_V5_COMPLETO_TAXONOMIA_TEMPLATES_20261019_054300.md` | completo, L1–1450 | §1.1 L29 objetivo; §5.2 L172–174 un propietario por bloque, texto por texto; §5.3–5.5 L176–190 revisor B, adversario, tercera lectura 10 %; §7.3 L258–270 sin estados de aplazamiento; §7.4 L272–283 seis mecanismos; §7.8 L352–368 destinos de todos los valores; §7.9 L370–376 certificado de evaluación exhaustiva por texto; §8 L425–440 secuencia; §9.1–9.7 L446–524 preparación, validadores probados, pares mínimos, canarios; §9.10 L540–552 hoja por texto; §11–§15 L576–695 rondas 1–4 y adjudicación; §16 L697–934 brief, plantillas, contrato GPT Image 2 L831–864; §17 L936–981 verificación; §20 R01–R20; §21 L1192–1215 tokens; §23 L1232–1241 participación del usuario | Es la metodología de construcción del catálogo. La verificación de extremo a extremo (§17) y las referencias de escenario (§9.8) se excluyen por la instrucción de Eric de no hacer pruebas |
| `fuentes_20261019/00688_TAXONOMIA_…_054122.md` | §1.12–§1.13 (L184–201) y §7 (L2784–2830); no el resto | §1.12 doce puntos del contrato de lectura y clasificación por texto; §1.13 correspondencia taxonomía → templates; §7.1 registro; §7.2 lógica de condiciones; §7.3 discriminantes; §7.4 consulta y tres clases | Reglas del registro, de las condiciones y de la selección |
| `v2/GUIA_CLASIFICACION.md` | completo, 114 l | formato del registro de regla (bloque_E, bloque_D, aplicaciones, todas las facetas en VALOR o UNIVERSAL con evidencia); consultas; validación con `validar_v2.py` | Formato de salida de la clasificación |
| `INSTRUCCIONES.md` | completo, 63 l | formato anterior (TODOS / lista, EXT:) | Superado por GUIA v2 y por 23 §2 (no se reutiliza la catalogación previa) |
| `PILOTO_V5_INSTRUCCIONES_20261019.md` (borrado el 2026-10-27, prueba preliminar) | completo, 177 l | §3: hashes de entrada; §9: tope de costo antes de clasificar | Los hashes se copian abajo. El control de costo se sostiene en PLAN_V5 §21.3 y R16 (desvío del presupuesto autorizado bloquea). El tope no está en ninguna decisión registrada |
| `v2/piloto_gpt-image/clasificacion.py` (borrado el 2026-10-27, prueba preliminar) | docstring, constantes y 31 de 65 aplicaciones | formato de aplicación | Sin consecuencia: el formato del registro es el de `v2/GUIA_CLASIFICACION.md` |

## Hashes de entrada (copiados de PILOTO_V5 §3 antes de borrarlo)

| Archivo | SHA-256 |
|---|---|
| `TAXONOMIA_CONSOLIDADA_SIN_ESTADOS_DIFERIMIENTO_20261019_054122.md` | `7ec912aa92d8d1a6f54a6158550c0bcfa48861a05bbf6f6146b5b93b1f9bfeaa` (también PLAN_V5 §7.6 L297) |
| `BASE_TEXTOS_ORIGINALES_13005_20261019_055700.sqlite` (tabla `textos`, 13,005 filas) | `c991437028d9d731bf46e516efa315f08d9da71bd596495c119fa41d30f6c8d9` |
| `BASE_TEXTOS_ORIGINALES_13005_20261019_055700.csv` | `a2c5a59d3531512058d8bfc6f1446fd45942a49ea40b25c6b179febd5608a1cc` |
