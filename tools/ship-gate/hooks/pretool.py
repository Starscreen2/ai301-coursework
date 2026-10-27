#!/usr/bin/env python3
"""Claude Code PreToolUse adapter for ship_gate.py."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ship_gate import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main(["hook"]))
