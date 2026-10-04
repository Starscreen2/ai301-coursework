# Evidence guide: where evidence lives in a PR package

## Plan fidelity (harness category: silent-drift)

Where it lives: the plan-context block's scope, implementation approach, test plan, and
deviation notes; the candidate diff's changed files and hunks; and the PR description's
claims about what changed.

What good looks like: every meaningful hunk belongs to the plan's stated boundary or to
a deviation explicitly recorded in the plan and repeated in the description. A planned
file or behavior that is absent is also drift when no deviation explains it. A
description saying "exactly as planned" is checked against the actual diff, not trusted.

## Test evidence (harness category: not-tested)

Where it lives: the plan-context test plan and repro evidence, the candidate PR's test-
evidence section, and the repo-facts block's required checks. Read the commands and
outputs, including before/after results, against the issue trigger.

What good looks like: the evidence runs the failure path named by the plan and shows an
observable before/after or expected result, then shows the required repository checks
with their commands and outcomes. A control that never exercises the bug, "verified
locally," or a green command with no result is not decisive. A deferred edge is okay
only when the plan and description explicitly disclose it.

## Diff quality (harness category: unreviewable)

Where it lives: the candidate's changed-file list, unified diff, and commit subjects.

What good looks like: the fix is focused, with no debug prints, dead helpers, commented-
out experiments, TODO debris, unrelated files, or broad reindent/formatting churn. A
necessary mechanical change must remain easy to inspect and be tied to the plan.

## Standards and comms (harness category: standards-wall)

Where it lives: the repo-facts PR template, contribution guide, issue/thread direction,
and AI-use policy, compared with every section of the candidate PR description and the
diff/test evidence that supports it.

What good looks like: required checklist items, issue linkage, tests/docs/changelog
asks, and maintainer questions are answered with concrete content. An AI-use disclosure
appears when the repository requires one. A silent policy does not create a disclosure
failure, but an explicitly required disclosure cannot be replaced with vague wording.
