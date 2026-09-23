---
name: repro-check
description: Grade a reproduction package (a claim comment plus a repro report against its issue) and decide whether it is ready to post upstream. Use when checking a draft claim or repro comment before posting, or when grading an eval package bundle.
---

# repro-check: rubric-driven reproduction grading

You are grading one reproduction package to answer a single question: is this ready to
post? Execute the rubric in `rubric.md` check by check against evidence in the package.

## Inputs

- **Live mode:** read `scope.md`, verify the issue is in the scoped Path Review repo,
  read `voice-guide.md`, gather issue-side evidence from GitHub, and grade the student's
  claim-only or full draft. For a claim-only draft, checks needing a repro are
  `unclear` with evidence `not yet applicable: claim-only draft` and are omitted from
  the verdict. For a full package, grade every check.
- **Eval mode:** use only the supplied package bundle. Do not fetch the live issue;
  the bundle is the complete frozen world.

## Workflow

1. Read the scope in live mode, then read `rubric.md` and the complete evidence guide.
2. Read the whole package in order: issue context, repo facts, claim, and repro report.
3. For each rubric row, gather the named evidence and grade it `pass`, `fail`, or
   `unclear` with one deciding fact or quote.
4. Apply the rubric's verdict rule. In live mode, also note any broken voice-guide rule.
5. Output a fenced JSON block last, with `item`, `checks`, and `verdict`.

## Grading discipline

Grade the proof, not the formatting. A terse complete report may pass and a long polished
report may fail. An artifact must show the issue's behavior rather than an adjacent
symptom. An honest, evidenced cannot-reproduce is acceptable. Treat unverified evidence
as `unclear`, and follow the rubric's rule that required `unclear` is a failure.
