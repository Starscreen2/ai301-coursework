# Contribution: test: cover the correlation ID helpers in src/correlation.ts

Path: `beat-2-contribution/contribution-story.md`

This file is Assignment 5, and it is graded at the path above; a copy kept anywhere else in
the repository is not read. **Keep every section header below under its exact name** — the
format criteria grade exactly that. Your course repo link is the whole submission: no tool
files and no evidence uploads are part of Assignment 5.

**Contribution Number:** [1]
**Student:** Puyang He
**GitHub Username:** Starscreen2
**Issue:** https://github.com/Logixia/logixia/issues/9
**Pull Request:** [GitHub PR link, once opened]

One repository, built across units 5 to 8, telling the whole story of your real
contribution. Fill it as you work, not at the end — the sections below ask for evidence that
is far easier to write down as it happens than to reconstruct in the last weekend.

Contribution Number stays `[1]` unless you make more than one contribution this term; it
just numbers them.

---

## Toolkit

Every story section below, from Why I Chose This Issue through Pull
Request, ends with a Toolkit block: which tool did that phase's work
and how you used it, what it produced, what difficulties or
shortcomings it presented, and what you changed or would change
because of them. Together the blocks are the thread the rubric's
Toolkit points read, and they are the raw material for your unit-9
portfolio, so keep them current as you work rather than
reconstructing them later.

A Toolkit block looks like this (copy it into each story section and
fill it there):

```text
**Toolkit**

- Tool: [which tool did this phase's work, and how you used it]
- What it produced: [described in a sentence or a short excerpt]
- Difficulties: [what fought you or fell short, or "none met"]
- What changed: [the patch, revision, or workaround, what you would
  update, or "nothing"]
```

This section also keeps one short dated entry per week of tool work,
starting below: what you built or changed that week, what broke, and
what you changed because of it. The blocks tell the story where it
happened; these entries are the toolkit's own timeline.

All four entries are graded. Keep every heading below, and fill each
one in the week it belongs to.

**Unit 5: I had Codex install the issue-scout overlay and build a reviewed shortlist**

I asked Codex to overlay the Unit 5 scout on my Unit 1 rubric and fit profile, and write three `gh search issues` queries with free ranking rules. Claude Code's scan command could not run because its OAuth session had expired, so Codex ran the searches and manually applied the rubric to the top five results, then reviewed two picks from the course issue site: Logixia #9 passed and #30 was rejected because another contributor had an active PR. The manual fallback and evidence are recorded separately; no Claude course credit was used, and I did not claim an issue. I recorded the login failure and manual review so I can rerun the scan with Claude after reauthentication and continue the story in Units 6–8.

**Unit 6: I had Codex set up the voice guard, claim #9, and reproduce its test gap**

After Claude Code OAuth completed, I used the voice guard to check my claim draft and posted it to [Logixia #9](https://github.com/Logixia/logixia/issues/9#issuecomment-6454333818). Claude's rubric re-grade accepted #9 and rejected #30 because an open PR and another contributor's current claim made #30 unavailable; that review also exposed and corrected a stale scope rule in my rubric. I started the reproduction report at upstream commit `e0ce05abf2ed10e3143be406d64228db9c5d6381`: existing tests already cover ID generation, fetch use, and parts of middleware/request handling, while a repo-wide search of 74 TypeScript test files found no direct references to five remaining helpers. I kept `CLAUDE.local.md` excluded from Git and made no source or test changes during this baseline reproduction.

**Unit 7: [one line on the tool work]**

[2-4 sentences: the ship-gate and your gate manifest. What it produced
on your real branch, what fought you, what changed because of it.]

**Unit 8: [one line on the tool work]**

[2-4 sentences: the PR-monitor and your playbook. What it read, what it
drafted, what you did with the draft.]

---

## Why I Chose This Issue

I found [Logixia issue #9](https://github.com/Logixia/logixia/issues/9) on the AI301 Issue Selection site. After restoring Claude Code authentication, the scout re-grade accepted #9 as straightforward and rejected #30 because an open PR and another contributor's current claim made it unavailable. The issue names `src/correlation.ts`, a requested test file, and concrete cases; the test-only TypeScript work fits the profile I saved in Unit 1, and I want to learn this repository's correlation context and test patterns. I read the live issue and `CONTRIBUTING.md`, confirmed #9 was open and unassigned with no PR linked to it when I claimed it, and posted the voice-checked claim on 2026-10-27: [claim comment](https://github.com/Logixia/logixia/issues/9#issuecomment-6454333818).

The live issue's blanket statement that no helpers are tested is now partly stale. My rubric re-grade also surfaced a scope rule that still carried a Path Review classroom exception; I revised it to evaluate current assignees, open PRs, and current non-maintainer claims while allowing closed or stale history. During reproduction I confirmed several helpers already have partial coverage, so I narrowed my report to the five exports with no direct test references across the 74 test files searched.

**Toolkit**

- Tool: Claude Code's issue-scout for the re-grade, the issue rubric for scope and difficulty, and the voice guard for the claim draft.
- What it produced: #9 accepted as straightforward, #30 rejected for an active claim and open PR, and a passed voice check before the public claim was posted.
- Difficulties: Claude OAuth initially blocked grading; the re-grade also found a stale Path Review exception in the scope rubric.
- What changed: fixed the scope rule to use current real-project ownership evidence, recorded difficulty separately, and posted the checked claim at the linked issue comment.

---

## Understanding the Issue

**Problem Description**

`src/correlation.ts` exports helpers for correlation IDs, request context, framework integrations, and message headers. The issue asks for focused tests around these helpers, but the current suite already covers some of them, so the remaining work is to document and test the uncovered behavior without presuming every export is untested.

**Expected Behavior**

The correlation helpers should have focused tests for context scoping and fallback behavior, middleware and Fastify request handling, Axios interceptor setup, child request propagation, message ID extraction, and Kafka header construction. The tests should use the repo's existing Jest style, avoid changing production code, and use `it.todo` if reproduction reveals a bug.

**Current Behavior**

At the selected baseline commit, tests cover `generateCorrelationId`, exercise `withCorrelationId` through `correlationFetch`, and partially cover `correlationMiddleware` and `childFromRequest`. `getCurrentCorrelationId`, `correlationFastifyHook`, `createCorrelationAxiosInterceptor`, `extractMessageCorrelationId`, and `buildKafkaCorrelationHeaders` have no direct test references in the 74 `*.test.ts` files searched under `src/` and `test/`. I did not run the test suite or establish a runtime failure in this baseline-only reproduction.

**Affected Components**

`src/correlation.ts` contains the public helpers; `src/context/async-context.ts` supplies the `AsyncLocalStorage` context. Existing correlation tests are under `src/__tests__/`, and the requested focused test file is `src/__tests__/correlation.test.ts`.

**Toolkit**

- Tool: Claude Code with the `repro-check` rubric, plus shell searches in the fork at the recorded upstream commit.
- What it produced: a reviewed problem statement and a boundary between existing partial coverage and five helpers with no direct test references.
- Difficulties: the issue's blanket claim was stale, and the first report searched only one test directory; repro-check caught the gap in that evidence.
- What changed: expanded the search to all 74 TypeScript test files under `src/` and `test/`, and added a positive control with literal output and exit statuses.

---

## Reproduction Process

**Environment Setup**

macOS 26.6.2, Node.js v22.22.1, npm 10.9.2, and `rg` were available. I cloned my public fork at `https://github.com/Starscreen2/logixia`; its `main` at `e0ce05abf2ed10e3143be406d64228db9c5d6381` matched upstream `main` when cloned on 2026-10-27. This was a static baseline search, so I did not install dependencies or change source files. The first report searched only `src/__tests__/`; I widened it to all `src/` and `test/` test files after repro-check identified that evidence gap.

**Steps to Reproduce**

1. From the repository root, run `rg -n 'getCurrentCorrelationId|correlationFastifyHook|createCorrelationAxiosInterceptor|extractMessageCorrelationId|buildKafkaCorrelationHeaders' src test --glob '*.test.ts'`.
2. The literal result is empty; `rg` exits 1, meaning no direct references were found in the searched files. This checkout contains 74 `*.test.ts` files under those directories.
3. Run the positive control `rg -n "from '.*correlation" src --glob '*.test.ts'`. It exits 0 and prints imports in `correlation-header-case.test.ts`, `correlation-id.test.ts`, and `correlation-fetch.test.ts`. The full outputs and interpretation are in the linked report.

**Reproduction Evidence**

- **Commit showing reproduction:** none; this was a baseline-only check at `e0ce05abf2ed10e3143be406d64228db9c5d6381`, with no source or test changes.
- **Screenshots/logs:** literal output from the two commands above:

  ```text
  [search for the five uncovered exports: no matching lines]
  exit=1
  src/__tests__/correlation-header-case.test.ts:11:import { childFromRequest, correlationMiddleware } from '../correlation';
  src/__tests__/correlation-id.test.ts:10:import { generateCorrelationId } from '../correlation';
  src/__tests__/correlation-fetch.test.ts:13:import { correlationFetch, withCorrelationId } from '../correlation';
  exit=0
  ```
- **My findings:** the old “no tests at all” description is too broad today. Three existing correlation test files cover ID generation, fetch use, and parts of middleware/request behavior; five named helpers still have no direct references across the searched test tree. No runtime bug was reproduced because I did not run tests or execute a failing scenario.

**Toolkit**

- Tool: ripgrep for the baseline evidence and Claude Code's `repro-check` skill to grade the claim and report against the live issue.
- What it produced: a repeatable static test-coverage check; repro-check accepted the revised claim and report after all five checks passed.
- Difficulties: searching only `src/__tests__/` could not support a repository-wide statement, and one grading rerun stalled before returning.
- What changed: expanded the search to all `src` and `test` TypeScript test files, added a positive control with literal output, and reran the rubric successfully.

---

## Solution Approach

**Analysis**

[Your analysis of the root cause: what is causing the issue, traced
to the files and functions involved.]

**Proposed Solution**

[High-level description of your fix approach, and what you are
deliberately NOT changing.]

**Implementation Plan**

1. [Modify file X to do Y]
2. [Add or change Z]
3. [Update tests]

[Record deviations here as they happen: what changed mid-build and
why. A recorded deviation is honest work; silent drift is not.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Testing Strategy

[What observable checks prove the fix: your reproduction steps re-run
against the built change (before and after), and the repo's own test
suite or checks with the outcome shown. "Tests pass" with nothing
observable named is not a strategy.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Implementation Notes

[A running log, added to as you work. Date each entry. What you
built, decisions you made when you made them, wrong turns included.]

**[Date]**

[Entry]

**[Date]**

[Entry]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Pull Request

**PR Link:** [GitHub PR URL when opened]

**PR Description:** [what the PR says; much of the content above
adapts into it]

**Maintainer Feedback:**

- [Date]: [feedback received, or "none yet"; silence is a normal
  state and costs you nothing]
- [Date]: [how you addressed it]

**Status:** [Awaiting review / Iterating / Merged / Closed. The
status is a fact you record, never a grade: the PR is graded as
opened.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Learnings and Reflections

**Technical Skills Gained**

[What you learned technically, named concretely.]

**Challenges Overcome**

[What was hard and how you solved it; point at the real events, the
Toolkit blocks above are full of them.]

**What I'd Do Differently Next Time**

[Reflection on your process.]

---

## Resources Used

[What actually helped, not a reading list. List things this story
already shows you using: the doc you followed to set the environment
up, the thread that explained the bug, the person who answered you.
One real entry beats ten plausible ones.]

- [Link to documentation that helped]
- [Discussion, issue, or post that helped]
