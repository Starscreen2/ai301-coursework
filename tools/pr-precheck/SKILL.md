---
name: pr-precheck
description: Grade a pull-request package against its posted plan and issue, then decide whether it is ready to submit. Use before opening or updating a Path Review PR, or when grading an eval bundle.
---

# pr-precheck: rubric-driven PR grading

## The question

Answer exactly one question: is this one pull request ready to submit? A PR package is
the issue and repo standards, the accepted plan with its deviation notes, the branch
diff, the draft title and description, the commits, and the test evidence. Read those
artifacts against one another; do not grade a different task or a second PR.

## Inputs and modes

In live mode, read the student's `plan.md` (including `## Deviations`), the branch diff
from `git diff main...HEAD`, commit list, draft PR title/description, test evidence, and
the real issue, PR template, and repository policy. Read the PR's own fork branch against
the scoped Path Review repository. A house-chain student uses the routed house plan and
repro pack instead of inventing a new target.

In eval mode, the package bundle is the entire world. Read only its issue, repo-facts,
plan-context, candidate PR, diff, commits, and test-evidence text; fetch nothing and use
the full verdict rule for every check.

## The scope seam (live mode only)

Read `scope.md` before grading anything else in live mode. Refuse a PR targeting a
repository outside the scope, and stop if the repo line still contains a placeholder.
Apply the Path Review rules about using a branch on the student's fork, one PR for the
issue, the required template, and classmates' PRs not blocking this work. Ignore
`scope.md` entirely in eval mode.

## The voice seam (live mode only)

Read `voice-guide.md` and hold the draft PR title and description against it. Report a
broken voice rule in the readable summary, but do not change the verdict on voice alone
unless `rubric.md` contains a communication check. Ignore the voice guide in eval mode.

## Component reads

Read `rubric.md` for the named checks and verdict rule, `references/evidence-guide.md`
for where each fact lives, and `procedure.md` for the exact read and comparison order.
If the procedure is silent, report that gap rather than inventing a step. If the rubric
or procedure has no student-written content, refuse to grade.

## Verdict and output

The only verdicts are `accept` (ready to submit) and `reject` (hold). Grade each check
`pass`, `fail`, or `unclear` with one deciding fact or quote. End with this fenced JSON
block, valid and last, with nothing after it:

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

## Grading discipline

Use evidence first; never write "looks fine" without a deciding fact. Grade the diff and
observed test outcome, not the polish or length of the description. The rubric decides,
and the procedure decides how evidence is gathered. An honest, documented shortfall can
pass when it is within the plan and clearly disclosed; silent drift cannot. Required
`unclear` is a failure under the rubric's rule.
