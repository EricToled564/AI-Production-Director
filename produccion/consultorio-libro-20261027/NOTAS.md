# Notas de uso · consultorio-libro-20261027

- **Dónde y cómo generar:** cada paso va en un chat nuevo de ChatGPT, con sus tres imágenes adjuntas en el orden que indica `PROMPTS.txt`. El prompt se pega tal cual sale.
- **Aprobar cada paso:** antes de pasar al siguiente se hace zoom al 100 % de rostros y manos (SW30 regla 14). Si el paso se aprueba, se guarda su sha256: esa imagen es la Image 1 del paso siguiente (regla 11).
- **Si un paso sale correcto en un 80 % o más:** se corrige con una edición puntual, sin volver a tirar (regla 12).
- **Límite de intentos:** máximo 2 intentos por paso. A la segunda falla se cambia de método declarando la causa, o se consulta (regla 13).
- **Herencia mínima (regla 5):**
  - de las referencias salen el rostro, el pelo, los lentes, los aretes y la complexión;
  - el texto solo describe lo que no está en ellas: vestuario, pose, mirada y posición.
- **Herramientas:** `herramientas/` es una copia sin cambios de `template_engine.py`, `audit_gi2.py` y `RULES_MATRIX.md` del production-package original (`AI_Production_Director_v3.4.0_COMPLETE/repo/production-package`). Tienen el mismo sha256 que el original.
- **Cómo regenerar y verificar:**
  - `python3 -I construir.py` regenera `PROMPTS.txt`;
  - `--probar` corre los casos que deben fallar;
  - `python3 -I disposiciones.py` y después `rule_ledger.py` comprueban la cobertura de reglas.
