"""validar_critica.py: corre visual-asset-critic/tools/validate_critique.py desde un entorno con la estructura que espera.

    python3 -I taller/catalogo/v3/prueba/validar_critica.py --selftest
    python3 -I taller/catalogo/v3/prueba/validar_critica.py ruta/a/critique.json [...]

En la copia instalada el validador no encuentra su schema: `_shotkit.py:19` toma como raíz la carpeta padre de `tools/`
y busca `skills/visual-asset-critic/templates/critique.schema.json` debajo de ella (ver
`revision/08_verificacion_antes_tarea2.md`). Aquí se copian a un directorio temporal, sin cambiarlos:
`tools/_shotkit.py`, `tools/validate_critique.py`, `skills/visual-asset-critic/{templates,examples}` y
`skills/visual-prompt-forge/adapters/_capabilities.json`. Después se corre el validador con los mismos argumentos y se
devuelve su código de salida.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SKILLS = Path(os.environ.get("FUPAI_SKILLS_ROOT", Path.home() / ".claude/skills/synced"))
critic = next(SKILLS.glob("*/visual-asset-critic"), None) or SKILLS / "visual-asset-critic"
forge = critic.parent / "visual-prompt-forge"
if not (critic / "tools/validate_critique.py").exists():
    sys.exit(f"no se encontró visual-asset-critic en {SKILLS}")

with tempfile.TemporaryDirectory() as raiz:
    r = Path(raiz)
    (r / "tools").mkdir()
    for f in ("_shotkit.py", "validate_critique.py"):
        shutil.copy(critic / "tools" / f, r / "tools" / f)
    shutil.copytree(critic / "templates", r / "skills/visual-asset-critic/templates")
    shutil.copytree(critic / "examples", r / "skills/visual-asset-critic/examples")
    (r / "skills/visual-prompt-forge/adapters").mkdir(parents=True)
    shutil.copy(forge / "adapters/_capabilities.json", r / "skills/visual-prompt-forge/adapters/_capabilities.json")
    args = [a if a.startswith("--") else str(Path(a).resolve()) for a in sys.argv[1:]]
    p = subprocess.run([sys.executable, str(r / "tools/validate_critique.py"), *args])
    sys.exit(p.returncode)
