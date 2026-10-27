import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import install
import ship_gate


class ManifestTests(unittest.TestCase):
    def test_reads_required_checks_and_dated_exclusions(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "ship-manifest.md"
            manifest.write_text(
                """# Manifest

```csv
status,check,command,source,reason
required,tests,python -m unittest,CONTRIBUTING.md,
excluded,build,npm run build,package.json,2026-10-27 not required for this test-only change
```
""",
                encoding="utf-8",
            )

            rows = ship_gate.read_manifest(manifest)

        self.assertEqual([row["status"] for row in rows], ["required", "excluded"])

    def test_rejects_undated_exclusion(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "ship-manifest.md"
            manifest.write_text(
                """```csv
status,check,command,source,reason
required,tests,python -m unittest,CONTRIBUTING.md,
excluded,build,npm run build,package.json,not needed
```
""",
                encoding="utf-8",
            )

            with self.assertRaises(ship_gate.GateError):
                ship_gate.read_manifest(manifest)


class HookTests(unittest.TestCase):
    def test_matches_pr_create_and_reads_title_and_body(self):
        matched, title, body = ship_gate.parse_pr_create(
            "gh pr create --title 'test: add correlation tests' --body 'Closes #9'"
        )

        self.assertTrue(matched)
        self.assertEqual(title, "test: add correlation tests")
        self.assertEqual(body, "Closes #9")

    def test_ignores_other_commands(self):
        self.assertEqual(ship_gate.parse_pr_create("gh pr list"), (False, None, None))
        self.assertEqual(
            ship_gate.parse_pr_create("printf 'example: gh pr create'"), (False, None, None)
        )

    def test_finds_pr_create_after_a_shell_directory_change(self):
        matched, title, body = ship_gate.parse_pr_create(
            "cd /tmp/example && gh pr create --title 'test: coverage' --body 'Closes #9'"
        )

        self.assertTrue(matched)
        self.assertEqual(title, "test: coverage")
        self.assertEqual(body, "Closes #9")

    def test_only_accepts_valid_accept_json(self):
        output = "```json\n" + json.dumps(
            {"verdict": "accept", "checks": [{"grade": "pass"}]}
        ) + "\n```"
        self.assertTrue(ship_gate.accepted(output))
        self.assertFalse(ship_gate.accepted(output.replace('"accept"', '"reject"')))


class InstallTests(unittest.TestCase):
    def test_installer_preserves_existing_hooks_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            settings = home / ".claude" / "settings.json"
            settings.parent.mkdir(parents=True)
            settings.write_text(
                json.dumps(
                    {
                        "effortLevel": "medium",
                        "hooks": {
                            "PreToolUse": [
                                {
                                    "matcher": "Bash",
                                    "hooks": [
                                        {
                                            "type": "command",
                                            "command": "voice-guard",
                                        }
                                    ],
                                }
                            ]
                        },
                    }
                ),
                encoding="utf-8",
            )

            destination, changed_first = install.install(home)
            _, changed_second = install.install(home)
            self.assertTrue(destination.is_dir())
            applied = json.loads(settings.read_text(encoding="utf-8"))
            hook_commands = [
                nested["command"]
                for item in applied["hooks"]["PreToolUse"]
                for nested in item["hooks"]
            ]

        self.assertTrue(changed_first)
        self.assertFalse(changed_second)
        self.assertEqual(applied["effortLevel"], "medium")
        self.assertEqual(hook_commands.count("voice-guard"), 1)
        self.assertEqual(
            hook_commands.count('python3 "$HOME/.claude/ship-gate/hooks/pretool.py"'), 1
        )


if __name__ == "__main__":
    unittest.main()
