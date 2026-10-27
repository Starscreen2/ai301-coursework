#!/usr/bin/env python3
"""Run a repo-local manifest and the bundled live pr-precheck before a PR ships."""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
REQUIRED_DRAFTS = ("plan.md", "pr-title.md", "pr-description.md", "test-evidence.md")
MANIFEST_COLUMNS = {"status", "check", "command", "source", "reason"}
CONFIG = json.loads((PACKAGE_ROOT / "config.json").read_text(encoding="utf-8"))


class GateError(RuntimeError):
    """A missing or invalid gate input that must block the PR doorway."""


def git_root(path: Path) -> Path:
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    )
    return Path(result.stdout.strip()).resolve()


def verify_scoped_repo(root: Path) -> None:
    """Refuse to execute a manifest in a repository outside this package's scope."""
    root = git_root(root)
    result = subprocess.run(
        ["git", "-C", str(root), "remote", "-v"],
        check=True,
        capture_output=True,
        text=True,
    )
    remotes = result.stdout.lower()
    if "github.com/logixia/logixia" not in remotes or "github.com/starscreen2/logixia" not in remotes:
        raise GateError(
            "Scope refusal: expected upstream Logixia/logixia and fork Starscreen2/logixia remotes."
        )


def read_manifest(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise GateError(f"Missing repo-root manifest: {path}")
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```csv\s*\n(.*?)\n```", text, re.DOTALL | re.IGNORECASE)
    if not match:
        raise GateError("Manifest needs one fenced csv table with required check rows.")

    reader = csv.DictReader(io.StringIO(match.group(1)))
    columns = {name.strip().lower() for name in (reader.fieldnames or [])}
    if not MANIFEST_COLUMNS.issubset(columns):
        missing = ", ".join(sorted(MANIFEST_COLUMNS - columns))
        raise GateError(f"Manifest is missing columns: {missing}")

    rows: list[dict[str, str]] = []
    for row in reader:
        normalized = {key.strip().lower(): (value or "").strip() for key, value in row.items() if key}
        status = normalized.get("status", "").lower()
        if status not in {"required", "excluded"}:
            raise GateError(f"Manifest row has invalid status: {status or '(blank)'}")
        for field in ("check", "command", "source"):
            if not normalized.get(field):
                raise GateError(f"Manifest {status} row is missing {field}.")
        if status == "excluded" and not re.search(r"\b20\d{2}-\d{2}-\d{2}\b", normalized.get("reason", "")):
            raise GateError(f"Excluded check '{normalized['check']}' needs a dated reason.")
        rows.append(normalized)

    if not rows or not any(row["status"].lower() == "required" for row in rows):
        raise GateError("Manifest must contain at least one required check.")
    return rows


def run_checks(root: Path, rows: list[dict[str, str]]) -> tuple[bool, list[str]]:
    output: list[str] = []
    ok = True
    for row in rows:
        if row["status"].lower() != "required":
            output.append(f"EXCLUDED: {row['check']} — {row['reason']}")
            continue
        output.append(f"\nCHECK: {row['check']}\nCOMMAND: {row['command']}\nSOURCE: {row['source']}")
        completed = subprocess.run(
            row["command"],
            cwd=root,
            shell=True,
            executable="/bin/bash",
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        output.append(completed.stdout.rstrip())
        output.append(f"RESULT: exit {completed.returncode}")
        if completed.returncode:
            ok = False
    return ok, output


def read_candidate(root: Path, title: str | None, body: str | None) -> tuple[str, str, str, str]:
    files = {name: root / name for name in REQUIRED_DRAFTS}
    for name, path in files.items():
        if not path.is_file():
            raise GateError(f"Missing candidate evidence file: {name}")
    final_title = title or files["pr-title.md"].read_text(encoding="utf-8").strip()
    final_body = body or files["pr-description.md"].read_text(encoding="utf-8").strip()
    evidence = files["test-evidence.md"].read_text(encoding="utf-8")
    if not final_title or not final_body:
        raise GateError("The candidate PR title and description must not be empty.")
    return final_title, final_body, evidence, files["plan.md"].read_text(encoding="utf-8")


def precheck(root: Path, title: str, body: str, evidence: str, plan: str) -> tuple[int, str]:
    skill_dir = PACKAGE_ROOT / "pr-precheck"
    prompt = f"""pr-precheck: grade one live candidate PR package for Logixia issue #9.
Use the bundled live scope and rubric. Read the actual branch diff, commits, repo rules,
issue, plan.md, and test-evidence.md in this checkout. Compare them with this draft.

Draft PR title:
{title}

Draft PR description:
{body}

Candidate plan (also saved in plan.md):
{plan}

Test evidence (also saved in test-evidence.md):
{evidence}

Grade every required check. Return the readable summary and the required final JSON block.
Do not create or update a pull request.
"""
    allowed = (
        "Read,Bash(gh issue view *),Bash(gh repo view *),Bash(gh pr list *),"
        "Bash(gh pr view *),Bash(gh pr diff *),Bash(gh api *),Bash(git status *),"
        "Bash(git rev-parse *),Bash(git remote *),Bash(git diff *),Bash(git log *)"
    )
    env = os.environ.copy()
    # PreToolUse can run inside Claude Code. Start the read-only grader as a separate CLI process.
    env.pop("CLAUDECODE", None)
    result = subprocess.run(
        [
            "claude",
            "-p",
            prompt,
            f"--add-dir={skill_dir}",
            "--max-turns",
            str(CONFIG["precheck_max_turns"]),
            "--max-budget-usd",
            str(CONFIG["precheck_max_budget_usd"]),
            f"--allowedTools={allowed}",
        ],
        cwd=root,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return result.returncode, result.stdout


def accepted(output: str) -> bool:
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", output, re.DOTALL)
    if not blocks:
        return False
    try:
        result = json.loads(blocks[-1])
    except json.JSONDecodeError:
        return False
    return result.get("verdict") == "accept" and all(
        check.get("grade") == "pass" for check in result.get("checks", [])
    )


def save_log(root: Path, output: str) -> Path | None:
    try:
        git_dir_text = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--git-dir"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, OSError):
        return None
    git_dir = Path(git_dir_text)
    if not git_dir.is_absolute():
        git_dir = root / git_dir
    log_dir = git_dir / "ship-gate" / "runs"
    log_dir.mkdir(parents=True, exist_ok=True)
    path = log_dir / f"{time.strftime('%Y%m%d-%H%M%S')}.log"
    path.write_text(output, encoding="utf-8")
    return path


def run_gate(root: Path, title: str | None, body: str | None, dry_run: bool) -> int:
    root = git_root(root)
    verify_scoped_repo(root)
    candidate_title, candidate_body, evidence, plan = read_candidate(root, title, body)
    rows = read_manifest(root / "ship-manifest.md")

    report = [f"ship-gate — {'dry run' if dry_run else 'manual gate'}", f"Repository: {root}"]
    checks_ok, check_output = run_checks(root, rows)
    report.extend(check_output)
    if not checks_ok:
        report.append("\nGATE BLOCKED: one or more required repository checks failed.")
        code = 2
    else:
        report.append("\nAll required repository checks passed; invoking live pr-precheck.")
        precheck_code, precheck_output = precheck(
            root, candidate_title, candidate_body, evidence, plan
        )
        report.append(precheck_output.rstrip())
        if precheck_code == 0 and accepted(precheck_output):
            report.append("\nGATE ACCEPTED: all required checks passed and pr-precheck accepted.")
            code = 0
        else:
            report.append("\nGATE BLOCKED: pr-precheck did not return an accept verdict.")
            code = 2

    complete = "\n".join(report).strip() + "\n"
    log_path = save_log(root, complete)
    if log_path:
        complete += f"\nGate log: {log_path}\n"
    sys.stdout.write(complete)
    return code


def parse_pr_create(command: str, cwd: Path | None = None) -> tuple[bool, str | None, str | None]:
    try:
        args = shlex.split(command)
    except ValueError:
        return False, None, None
    segments: list[list[str]] = [[]]
    for token in args:
        if token in {"&&", "||", ";"}:
            segments.append([])
        else:
            segments[-1].append(token)
    target = next((segment for segment in segments if segment[:3] == ["gh", "pr", "create"]), None)
    if target is None:
        return False, None, None

    title: str | None = None
    body: str | None = None
    index = 0
    while index < len(target):
        token = target[index]
        if token in {"--title", "-t"} and index + 1 < len(target):
            title = target[index + 1]
            index += 1
        elif token in {"--body", "-b"} and index + 1 < len(target):
            body = target[index + 1]
            index += 1
        elif token in {"--body-file", "-F"} and index + 1 < len(target):
            body_path = Path(target[index + 1])
            if cwd and not body_path.is_absolute():
                body_path = cwd / body_path
            try:
                body = body_path.read_text(encoding="utf-8")
            except OSError:
                body = None
            index += 1
        index += 1
    return True, title, body


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="action", required=True)
    gate_parser = subparsers.add_parser("gate", help="run manifest checks and live pr-precheck")
    gate_parser.add_argument("--root", type=Path, default=Path.cwd())
    gate_parser.add_argument("--title")
    gate_parser.add_argument("--body")
    gate_parser.add_argument("--body-file", type=Path)
    gate_parser.add_argument("--dry-run", action="store_true")
    hook_parser = subparsers.add_parser("hook", help=argparse.SUPPRESS)
    hook_parser.add_argument("--input", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    try:
        if args.action == "gate":
            body = args.body
            if args.body_file:
                body = args.body_file.read_text(encoding="utf-8")
            return run_gate(args.root.resolve(), args.title, body, args.dry_run)

        event = json.loads(args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read())
        tool_input = event.get("tool_input", {})
        command = str(tool_input.get("command", ""))
        root = Path(event.get("cwd") or Path.cwd()).resolve()
        is_create, title, body = parse_pr_create(command, root)
        if not is_create:
            return 0
        return run_gate(root, title, body, dry_run=True)
    except (GateError, OSError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        sys.stdout.write(f"GATE BLOCKED: {exc}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
