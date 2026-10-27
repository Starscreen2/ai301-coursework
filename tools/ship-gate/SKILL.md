---
name: ship-gate
description: Run a repository's declared checks and the scoped pr-precheck before opening a GitHub pull request. Use for the manual browser doorway, dry runs, and the gh pr create hook.
---

# ship-gate

The gate answers one question before a PR leaves the fork: are the repository's declared
checks green, and does the bundled live `pr-precheck` accept the title, description,
plan, diff, and evidence for this branch?

## Manual doorway

From the candidate repository root, run:

```sh
python3 "$HOME/.claude/ship-gate/ship_gate.py" gate --root "$PWD" --dry-run
```

The command reads `ship-manifest.md`, runs every `required` command in it, then invokes
the bundled `pr-precheck` skill. It never opens a PR. Use it before a browser-based PR
creation, for a dry run, or to read the gate result after a change.

The candidate root also needs `plan.md`, `pr-title.md`, `pr-description.md`, and
`test-evidence.md`. The `gh pr create` hook takes title/body flags from that command and
uses the local drafts when flags are omitted.

## Automatic doorway

The installed PreToolUse hook watches Bash commands for `gh pr create`. Other commands
pass through untouched. On a match, it runs the same manifest checks and live PR
precheck; any failed check, missing evidence, or non-accept verdict blocks the tool call
and prints the deciding reason. The existing voice-guard hook remains installed and
continues to check PR text against the voice guide.

## Package layout

- `ship_gate.py`: manifest runner, candidate loader, live precheck runner, and manual CLI.
- `hooks/pretool.py`: Claude Code `PreToolUse` adapter.
- `install.py` and `config.json`: idempotent package installation and hook wiring.
- `pr-precheck/`: the complete live skill, including the Logixia scope and evidence guide.

Install or refresh the package with `python3 install.py`. It copies the package into
`~/.claude/ship-gate` and merges one hook into Claude Code's settings without replacing
other hooks. The current command is visible in `~/.claude/settings.json`.
