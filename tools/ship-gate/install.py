#!/usr/bin/env python3
"""Install or refresh the self-contained ship-gate package and Claude hook."""

from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

SOURCE = Path(__file__).resolve().parent


def install(home: Path) -> tuple[Path, bool]:
    config = json.loads((SOURCE / "config.json").read_text(encoding="utf-8"))
    destination = (home / ".claude" / "ship-gate").resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, destination, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"))

    settings_path = home / ".claude" / "settings.json"
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    if settings_path.is_file():
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
    else:
        settings = {}

    hooks = settings.setdefault("hooks", {}).setdefault(config["hook_event"], [])
    hook = {
        "matcher": config["tool_matcher"],
        "hooks": [
            {
                "type": "command",
                "command": config["hook_command"],
                "timeout": config["timeout_seconds"],
                "statusMessage": config["status_message"],
            }
        ],
    }
    already_installed = any(
        item.get("matcher") == hook["matcher"]
        and any(
            nested.get("command") == config["hook_command"]
            for nested in item.get("hooks", [])
        )
        for item in hooks
    )
    if already_installed:
        return destination, False

    hooks.append(hook)
    serialized = json.dumps(settings, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=settings_path.parent, delete=False
    ) as temporary:
        temporary.write(serialized)
        temporary_path = Path(temporary.name)
    os.replace(temporary_path, settings_path)
    return destination, True


if __name__ == "__main__":
    home = Path.home()
    if len(sys.argv) > 1:
        home = Path(sys.argv[1]).expanduser().resolve()
    try:
        target, changed = install(home)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ship-gate install failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Installed package: {target}")
    print("Claude Code hook: " + ("added" if changed else "already installed"))
