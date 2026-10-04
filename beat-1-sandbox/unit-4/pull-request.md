# Unit 4 — Test and Submit

Path: `beat-1-sandbox/unit-4/pull-request.md`

## Your pull request

**Pull request**

https://github.com/codepath/pathreview-ai301-fa26-s1/pull/88

**Branch**

`fix/65-async-review-mocks`

**AI disclosure for the PR**

Claude helped me spiritually. Codex helped prepare the Unit 4 precheck skill and run its evaluation. Codex also helped update the test fixtures, remove the issue-specific xfail markers, and correct the ordered-list query-count assertion. The production service was not changed; the checks listed above were run locally.

## Live precheck verdict

I ran the live precheck against PR #88 after GitHub Actions completed. Verdict: **accept**. All required checks passed:

- **Plan fidelity:** The diff changes only `tests/unit/test_review_service.py`; the count-query expectation is documented in the plan's deviation note and PR description.
- **Decisive evidence:** The target changed from 13 failures and 6 passes to 19 passes. The full unit suite and all five PR CI jobs passed; local lint, typecheck, format, and frontend checks also passed. The empty integration directory is noted, and its CI job passed.
- **Focused diff:** One planned test file changed; the diff is limited to synchronous result mocks, removal of seeded xfails, and the documented two-query assertion.
- **Standards:** The PR uses the repository template, closes issue #65, includes the required course AI disclosure, and has green CI.
- **Accurate description:** Title, scope, and test results match the diff and evidence.

```json
{
  "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/pull/88",
  "checks": [
    {"name": "Plan fidelity and honest scope", "grade": "pass", "evidence": "Only tests/unit/test_review_service.py changed; the two-query expectation is recorded as a plan deviation and in the PR description."},
    {"name": "Decisive test evidence", "grade": "pass", "evidence": "The target moved from 13 failed, 6 passed to 19 passed; all five PR CI jobs passed."},
    {"name": "Diff is reviewable and focused", "grade": "pass", "evidence": "The single-file diff contains only the planned mock correction, xfail removal, and documented query-count assertion."},
    {"name": "Repository standards and template satisfied", "grade": "pass", "evidence": "The PR follows the template, closes #65, includes the course-required AI disclosure, and all five CI jobs passed."},
    {"name": "Description and title are evidence-accurate", "grade": "pass", "evidence": "The PR claims match the test-only diff and recorded local and CI results."}
  ],
  "verdict": "accept"
}
```

## Reflection

- **What did the package review show?** `pkg-20` showed that tests and a focused diff are not enough when the repository or course requires a clear AI-use disclosure.
- **What trade-off did the rubric make?** `pkg-01` showed that requiring evidence to match the diff can hold a package when its claimed before/after result is implausible; that is a deliberate cost of avoiding unsupported claims.

## Eval iterations

**Run history**

- Full run: agreement `20/20` scored items; every category matched and the category floor passed.

**Package analysis**

`pkg-20`: my rubric decided `reject`, and the gold label was `reject`. The package's repository policy explicitly requires disclosure of AI use and its extent, but the PR description has no AI-use disclosure. The repository-standards check therefore holds it even though the other parts of a PR might be ready.

**Check rationale**

The exact check text in `tools/pr-precheck/rubric.md` is:

> Pass when every required template section has concrete content, the issue is linked using the requested form, maintainer direction is engaged, required tests/docs/changelog asks are addressed, and any repository AI-use policy is met. If policy requires AI disclosure, the description contains an explicit truthful disclosure; if policy is silent, no disclosure is invented as a requirement.

I kept this check required because a ready diff can still miss a repository's stated submission rules. It looks for the actual policy and corresponding PR text, so it does not demand a disclosure when the repository is silent, but it will hold a PR that omits one when the policy requires it.

**Trade-offs**

`pkg-01` shows the cost of requiring evidence to agree with the diff: my rubric held a package whose reported before/after result was not plausible because the diff duplicated an unconditional reservation call instead of implementing the planned capacity check. That can hold a terse or unusual patch when its evidence is unclear, but it prevents a result claim from substituting for an observable change.
