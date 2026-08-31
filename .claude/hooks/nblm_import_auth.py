#!/usr/bin/env python3
"""Instala un state.json exportado y deja el servidor autenticado.

NotebookLM no tiene API publica. El servidor guarda la sesion de Google como un
storageState de Playwright (cookies + localStorage) en:

    <dataDir>/browser_state/state.json

Ese archivo es portable: se genera con un login hecho una sola vez en cualquier
maquina y el servidor lo recarga al arrancar. Con el, este entorno queda
autenticado sin que la contrasena pase por ningun lado.

Rutas donde lo genera el login, segun sistema:
    Linux    ~/.local/share/notebooklm-mcp/browser_state/state.json
    macOS    ~/Library/Application Support/notebooklm-mcp/browser_state/state.json
    Windows  %APPDATA%\\notebooklm-mcp\\browser_state\\state.json

Uso:
    python3 nblm_import_auth.py --state /ruta/al/state.json
    python3 nblm_import_auth.py --state state.json --verificar
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Cookies que el servidor considera indispensables (dist/auth/auth-manager.js).
REQUIRED = ("__Secure-1PSID", "__Secure-3PSID")


def data_dir() -> Path:
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "notebooklm-mcp"
    if os.name == "nt":
        return Path(os.environ.get("APPDATA", Path.home())) / "notebooklm-mcp"
    return Path(
        os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share")
    ) / "notebooklm-mcp"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", required=True, help="state.json exportado")
    ap.add_argument("--verificar", action="store_true", help="correr get_health despues")
    a = ap.parse_args()

    src = Path(a.state)
    if not src.is_file():
        print(f"no existe: {src}", file=sys.stderr)
        return 2

    try:
        data = json.loads(src.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"no es JSON valido: {exc}", file=sys.stderr)
        return 2

    cookies = data.get("cookies")
    if not isinstance(cookies, list) or not cookies:
        print("el archivo no trae cookies. ¿Es el state.json correcto?", file=sys.stderr)
        return 2

    google = [c for c in cookies if "google.com" in (c.get("domain") or "")]
    nombres = {c.get("name") for c in cookies}
    faltan = [n for n in REQUIRED if n not in nombres]

    print(f"cookies totales:        {len(cookies)}")
    print(f"cookies de google.com:  {len(google)}")
    if faltan:
        print(f"FALTAN cookies clave:   {', '.join(faltan)}")
        print("  El login no quedo completo, o se exporto antes de terminar.")
        return 1
    print(f"cookies clave:          presentes ({', '.join(REQUIRED)})")

    dest_dir = data_dir() / "browser_state"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "state.json"
    if dest.exists():
        shutil.copy2(dest, dest.with_suffix(".json.bak"))
    shutil.copy2(src, dest)
    os.chmod(dest, 0o600)
    print(f"instalado en:           {dest}")

    if not a.verificar:
        return 0

    print("\nverificando…")
    client = Path(__file__).resolve().parent / "nblm_client.py"
    r = subprocess.run(
        [sys.executable, str(client), "--call", "get_health"],
        capture_output=True, text=True, timeout=300,
    )
    salida = r.stdout
    print(salida.strip()[:600])
    if '"authenticated": true' in salida:
        print("\nAUTENTICADO. Ya se puede correr nblm_load.py")
        return 0
    print("\nSigue sin autenticar. Las cookies pueden haber expirado; "
          "rehaz el login y exporta de nuevo.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
