# ship-gate

`ship-gate` is a self-contained Claude Code package for the last step before creating a
GitHub pull request. It runs the target repository's `required` checks from its
`ship-manifest.md`, then runs the bundled live `pr-precheck` against one draft. It never
creates a PR itself.

## Install

From the AI301 coursework repository:

```sh
python3 tools/ship-gate/install.py
```

The installer copies the package into `~/.claude/ship-gate` and adds one Bash
`PreToolUse` hook for `gh pr create`. It preserves the existing `settings.json` values and
hooks, and a second install does not add a duplicate hook.

## Manual doorway and dry run

The target repository root needs:

- `ship-manifest.md`: required repo checks and dated excluded-check reasons.
- `plan.md`: accepted scope, implementation plan, test plan, and deviations.
- `pr-title.md` and `pr-description.md`: candidate PR text using the repo's template.
- `test-evidence.md`: literal commands and observed results.

Run from the target repository:

```sh
python3 "$HOME/.claude/ship-gate/ship_gate.py" gate --root "$PWD" --dry-run
```

This is the manual doorway for browser-created PRs and the dry-run path. The automatic
hook reads `--title`, `--body`, and `--body-file` from `gh pr create`; when a flag is
omitted, it uses the local PR draft. A missing input, failed required check, grader
error, or verdict other than `accept` blocks the command and quotes its reason.

## Scope and evidence

The included `pr-precheck/` folder is a complete skill package with its rubric,
procedure, voice guide, scope, and evidence guide. Its live scope names `Logixia/logixia`,
the contributor fork, and issue #9; it does not inherit the Path Review classroom scope.
The runner also verifies both Git remotes before executing any manifest command.

Each run writes a full transcript under `.git/ship-gate/runs/` in the target clone. The
tests for the package run with:

```sh
python3 -m unittest discover -s tools/ship-gate/tests -v
```
