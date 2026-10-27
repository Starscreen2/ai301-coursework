# Procedure: how this tool grades a PR package

## Read order

1. In live mode, read `scope.md` and confirm the target repository, fork branch, and
   issue are in scope; in eval mode, ignore scope and use only the bundle.
2. Read the whole issue and repo-facts block, including PR-template, contribution, and
   AI-use requirements.
3. Read the plan context and record its exact scope pair, planned files/behavior,
   test plan, and every deviation note before reading the diff.
4. Read the PR title and description, then the commit list and changed-file list.
5. Read the complete unified diff and the complete test-evidence section. This order
   makes the side-by-side comparisons explicit instead of letting a confident
   description define what the diff means.

## Evidence gathering

- For plan fidelity, make a short list of planned files/behaviors and deviations, then
  compare it with every changed file and meaningful hunk; record any silent addition,
  omission, or description-versus-diff mismatch.
- For test evidence, extract each command, the input or trigger it exercises, the
  before/after result, and the repo check outcomes. Compare those with the plan's test
  plan and the issue's reproduction, not merely with a green status sentence.
- For diff quality, inspect the changed-file list, each hunk, and commit subjects for
  debug output, dead/commented experiments, formatting churn, unrelated cleanup, or
  other debris that makes the intended change harder to review.
- For standards, list every PR-template checkbox/section, contribution-policy ask,
  maintainer direction, and AI-disclosure requirement, then locate the corresponding
  concrete text or evidence in the candidate description/diff.
- For title/description accuracy, compare every material claim with the plan, diff, and
  test evidence; record the narrowest fact that proves or disproves it.

## Check execution

Run the rubric checks in its listed order using the gathered notes. Grade `pass` only
when the stated outcome is observable and within the pass condition, `fail` when the
artifact contradicts it, and `unclear` only when the package genuinely lacks the named
evidence. Do not replace a missing command/output with an assumption that a test ran.
Do not treat an honest documented limitation as drift if the plan and description both
bound it.

## Verdict assembly

Apply the rubric's rule: every required check must pass, and any `fail` or `unclear`
means `reject`. If multiple checks fail, quote the first failing required check in
rubric order as the primary reason and retain one evidence line for every check in the
JSON output. In live mode, add voice-guide notes before the final JSON; the JSON block
must be valid and the last content emitted.
