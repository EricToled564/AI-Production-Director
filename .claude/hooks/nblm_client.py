#!/usr/bin/env python3
"""Cliente MCP mínimo por stdio para hablar con notebooklm-mcp sin registrarlo.

Sirve para probar el servidor y para cargar el corpus desde la línea de comandos.

Uso:
    python3 nblm_client.py --list
    python3 nblm_client.py --call get_health
    python3 nblm_client.py --call add_source --args '{"content":"...","title":"x"}'
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import threading
import time

CMD = ["npx", "-y", "notebooklm-mcp@latest"]


class Client:
    def __init__(self, timeout: float = 180.0):
        self.timeout = timeout
        self.proc = subprocess.Popen(
            CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, text=True, bufsize=1,
        )
        self._id = 0
        self._lock = threading.Lock()

    def _send(self, method: str, params: dict | None = None, notify: bool = False):
        with self._lock:
            msg: dict = {"jsonrpc": "2.0", "method": method}
            if params is not None:
                msg["params"] = params
            if not notify:
                self._id += 1
                msg["id"] = self._id
                want = self._id
            self.proc.stdin.write(json.dumps(msg) + "\n")
            self.proc.stdin.flush()
            if notify:
                return None

        deadline = time.time() + self.timeout
        while time.time() < deadline:
            line = self.proc.stdout.readline()
            if not line:
                raise RuntimeError("el servidor cerró la salida")
            line = line.strip()
            if not line.startswith("{"):
                continue  # banner / logs
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue
            if data.get("id") == want:
                return data
        raise TimeoutError(f"sin respuesta a {method} en {self.timeout}s")

    def initialize(self):
        r = self._send("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "fupai-nblm-client", "version": "1.0"},
        })
        self._send("notifications/initialized", {}, notify=True)
        return r

    def list_tools(self):
        return self._send("tools/list", {})

    def call(self, name: str, args: dict):
        return self._send("tools/call", {"name": name, "arguments": args})

    def close(self):
        try:
            self.proc.terminate()
            self.proc.wait(timeout=10)
        except Exception:
            self.proc.kill()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--call")
    ap.add_argument("--args", default="{}")
    ap.add_argument("--timeout", type=float, default=180.0)
    a = ap.parse_args()

    c = Client(timeout=a.timeout)
    try:
        init = c.initialize()
        info = (init.get("result") or {}).get("serverInfo", {})
        print(f"servidor: {info.get('name')} {info.get('version')}", file=sys.stderr)

        if a.list:
            tools = (c.list_tools().get("result") or {}).get("tools", [])
            print(f"{len(tools)} tools:")
            for t in tools:
                print(f"  {t['name']:22} {(t.get('description') or '')[:88]}")
            return 0

        if a.call:
            r = c.call(a.call, json.loads(a.args))
            if "error" in r:
                print(json.dumps(r["error"], ensure_ascii=False, indent=2))
                return 1
            for block in (r.get("result") or {}).get("content", []):
                print(block.get("text", json.dumps(block, ensure_ascii=False)))
            return 1 if (r.get("result") or {}).get("isError") else 0

        ap.print_help()
        return 2
    finally:
        c.close()


if __name__ == "__main__":
    sys.exit(main())
