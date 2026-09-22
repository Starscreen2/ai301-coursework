# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

Record of the issue carried into Unit 2, and of the evaluation runs that produced
`eval-run.txt`.

## Selected issue

**Issue link**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/65

**Verdict output**

All three issues pass every required check — repo alive (pushed 2026-09-16, human commits by Andrew Burke), no CONTRIBUTING/AI-policy restriction found (silent → pass), each has a concrete bounded fix, and none has an assignee, open linked PR, or claim comment. Ranked by fit (bounded, clean, reproducible, tests/docs-oriented):

1. **#65** (async mock fix) — clearest bounded fix, concrete repro command (`pytest tests/unit/test_review_service.py -q`), exact error and fix approach named (`AsyncMock`/`MagicMock`), directly builds Python/testing skills.
2. **#64** (test fixture overlap bug) — equally clean, single-file fixture fix, exact repro and assertion given.
3. **#73** (README/.env.example doc mismatch) — smallest scope (docs/config only), good first PR but less technical depth than the other two.

All three are equally clean for ownership (no assignee/PR/comments), so ranking comes down to fit with your stated preference for bounded Python/test work.

```json
[
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/65",
    "checks": [
      {"name": "Repository is alive", "grade": "pass", "evidence": "isArchived:false, pushedAt 2026-09-16; newest commits authored by human Andrew Burke on 2026-09-16"},
      {"name": "Change is bounded and actionable", "grade": "pass", "evidence": "Names exact file/test (`tests/unit/test_review_service.py`), exact error (`AttributeError: 'coroutine' object has no attribute 'first'`), repro command with observed 13 failed/6 passed, and a concrete fix approach (AsyncMock/MagicMock)"},
      {"name": "No active owner or implementation", "grade": "pass", "evidence": "assignees: [], comments: [], no cross-referenced PRs in issue timeline"},
      {"name": "Contribution workflow is permitted", "grade": "pass", "evidence": "No CONTRIBUTING.md or AI policy file found (404) — repo is silent"},
      {"name": "Maintainer signal is present", "grade": "pass", "evidence": "5 newest default-branch commits all authored by human Andrew Burke (Aburke225), most recent 2026-09-16"},
      {"name": "Low-reuse fit", "grade": "pass", "evidence": "No assignee, no comments, no linked PR"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/64",
    "checks": [
      {"name": "Repository is alive", "grade": "pass", "evidence": "isArchived:false, pushedAt 2026-09-16; newest commits authored by human Andrew Burke"},
      {"name": "Change is bounded and actionable", "grade": "pass", "evidence": "Names exact file/test (`tests/unit/test_relevance_scorer.py::test_query_with_partial_overlap`), exact failing assertion (`assert 1.0 < 0.9`), and the fix direction (fixture needs genuine partial overlap)"},
      {"name": "No active owner or implementation", "grade": "pass", "evidence": "assignees: [], comments: [], no cross-referenced PRs in issue timeline"},
      {"name": "Contribution workflow is permitted", "grade": "pass", "evidence": "No CONTRIBUTING.md or AI policy file found (404) — repo is silent"},
      {"name": "Maintainer signal is present", "grade": "pass", "evidence": "5 newest default-branch commits all authored by human Andrew Burke, most recent 2026-09-16"},
      {"name": "Low-reuse fit", "grade": "pass", "evidence": "No assignee, no comments, no linked PR"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/73",
    "checks": [
      {"name": "Repository is alive", "grade": "pass", "evidence": "isArchived:false, pushedAt 2026-09-16; newest commits authored by human Andrew Burke"},
      {"name": "Change is bounded and actionable", "grade": "pass", "evidence": "Names exact target files (`README.md`, `.env.example`) and the concrete inconsistency (`OPENROUTER_API_KEY` missing, `LLM_PROVIDER` comment omits `openrouter`), estimated effort 1-2 hours"},
      {"name": "No active owner or implementation", "grade": "pass", "evidence": "assignees: [], comments: [], no cross-referenced PRs in issue timeline"},
      {"name": "Contribution workflow is permitted", "grade": "pass", "evidence": "No CONTRIBUTING.md or AI policy file found (404) — repo is silent"},
      {"name": "Maintainer signal is present", "grade": "pass", "evidence": "5 newest default-branch commits all authored by human Andrew Burke, most recent 2026-09-16"},
      {"name": "Low-reuse fit", "grade": "pass", "evidence": "No assignee, no comments, no linked PR"}
    ],
    "verdict": "accept"
  }
]
```

## Eval iterations

**Run history**

- “agreement: 2/3 scored items” — initial smoke run.
- “agreement: 1/1 scored items” — issue-01 scope recheck.
- “agreement: 17/20 scored items  (bar: 18/20: below the bar)” — first full run.
- “agreement: 2/3 scored items” — issue-04, issue-09, and issue-19 recheck.
- “agreement: 1/1 scored items” — issue-04 recheck.
- “agreement: 19/20 scored items  (bar: 18/20: PASS)” — final saved run.

**Issue analysis**

For `issue-15`, the final run records: “issue-15  reject  accept   NO     graded accept”. The rubric accepted it because the repository was active, the issue had no assignee or open linked PR, and the requested behavior was concrete. The gold label was `reject` because the issue had years of design discussion and abandoned attempts around the Slack-compatible webhook behavior. The run showed that the rubric still underweighted unresolved design history for this particular scope case.

**Check rationale**

The current check wording is:

> | Change is bounded and actionable | Read the issue body, its stated files or reproduction steps, labels, and the comment thread. | The request describes a finite contribution with a concrete behavior, file/location, test, or acceptance signal. A multi-file documentation or configuration change passes when it enumerates the target files/sections and the expected content or result. A bug report passes when it names one user-visible failure or interaction and gives a reproduction, affected examples, or a diagnosed location; possible root causes or implementation suggestions are context, not automatic scope failure. A maintainer-filed `good first issue` bug in one named feature area can pass with a concise list of at least two affected behaviors even when paths or tests are omitted. Fail an explicit umbrella/megaissue/tracking list, a codebase-wide initiative, a pure usage question, a request whose design or product decision is still unresolved, or a thread showing unresolved design debate plus repeated abandoned attempts. An old claim or closed PR alone does not make a concrete issue unbounded when the thread invites a fresh contributor. | required |

I kept this wording because the evaluation feedback showed that it needed to recognize bounded maintainer-filed bugs such as issue-04 and issue-19, while still naming the explicit patterns that make issue-05, issue-10, issue-15, and issue-20 too broad or unsettled.

**Trade-offs**

The final run records “categories: claimed 4/4  clear-accept 8/8  dead-repo 3/3  policy 1/1  scope 3/4” and “agreement: 19/20 scored items  (bar: 18/20: PASS)”. The trade-off is that the scope check accepts one arguable design-history case, issue-15, so it preserves all eight clear accepts while still passing the course bar and matching every other category. I accepted that one miss rather than adding a stricter rule that could reject concise, valid bug reports like issue-04 or issue-19.

## Selection rationale

**Selection rationale**

1. Issue #65 fits my interests because it is a focused Python testing problem with an exact failing command and a likely fix using async and sync mock types. It is small enough to investigate within a few hours and gives me useful practice with service-layer tests.
2. The verdict correctly identified the active repository, precise reproduction, bounded file set, and clean ownership state. It could not weigh my personal comfort with async mocks or the value of learning this particular test stack; those are fit decisions I made after the rubric accepted it.
3. Claiming difficulty appears low right now: the live run found no assignee, no open linked PR, and no claim comments. I will still re-check the issue immediately before claiming it in Unit 2 because classmates can act between runs.

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/issue-select/`.
