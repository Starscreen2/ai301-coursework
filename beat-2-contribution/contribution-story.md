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
**Pull Request:** https://github.com/Logixia/logixia/pull/83

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

Each section below has a Toolkit block with four fields: Tool, What it
produced, Difficulties, and What changed. Keep those fields concrete
and specific to that phase.

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

**Unit 7: I packaged and installed the ship-gate, then ran it on the real branch**

I packaged the Logixia-scoped `pr-precheck` with a `gh pr create` hook, manifest runner, config, and idempotent installer; installing twice preserved the existing voice guard and added only one gate hook. My root-level manifest requires the focused and full Jest suites, typecheck, and lint, and records dated reasons for excluding the production build and whole-repo format check. The first real-branch run passed the checks but blocked because the test file was still untracked; I committed and pushed `e9acda0`, reran the gate, and all five PR checks passed, so I opened [PR #83](https://github.com/Logixia/logixia/pull/83). **Student-reported time estimate: 2 hours; not independently timed.**

**Unit 8: I installed the PR monitor and wrote a playbook for when to wait or follow up**

I installed the headless PR monitor and wrote its playbook from Logixia's contribution guidance, my voice-guide rules, and recent PR activity; the repository gives no review-time promise, so my first-review threshold is 14 days. The free state run found PR #83 open for under a day, with no comments or reviews, one passing title check, and GitHub still awaiting review. The full run drafted a wait note, explaining that the threshold was unmet and that nothing should be sent; I reviewed it and left it unposted. The tool's “polite nudge” label was broader than the action in its body, so I checked the actual draft and followed its explicit wait decision.

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
- **Command output:** the first search returned no matching lines and `rg` exited 1; the positive-control search returned these existing imports and exited 0:

  ```text
  src/__tests__/correlation-header-case.test.ts:11:import { childFromRequest, correlationMiddleware } from '../correlation';
  src/__tests__/correlation-id.test.ts:10:import { generateCorrelationId } from '../correlation';
  src/__tests__/correlation-fetch.test.ts:13:import { correlationFetch, withCorrelationId } from '../correlation';
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

This is a test-coverage gap, not a reproduced production-code defect. At the baseline commit, `src/correlation.ts` had several exported helpers with no direct references in the test tree. Existing tests already covered ID generation, fetch propagation, and parts of middleware/request handling, so the issue's opening statement was stale. The helpers use `LogixiaContext` from `src/context/async-context.ts`; their observable contracts can be exercised with fake HTTP request/reply objects, a fake logger, and plain Kafka/SQS message shapes.

**Proposed Solution**

Add `src/__tests__/correlation.test.ts` with focused tests for context scoping, Express middleware, the Fastify hook, the Axios interceptor, request metadata and forwarded IP, Kafka/SQS/envelope extraction, Kafka header construction, and ID generation. Keep production code, dependencies, package metadata, and public documentation unchanged; report a newly discovered bug separately rather than making an unplanned fix.

**Implementation Plan**

1. Add fake-object tests for context helpers and both request middleware shapes, including generation and response-header opt-out.
2. Add tests for the Axios interceptor, child logger fields, and the supported message and Kafka-header forms.
3. Run the focused Jest file, the full suite, typecheck, and lint; keep the diff limited to the new test file.

**Deviations:** The issue said none of the nine exports had tests, but Unit 6's broad search showed existing partial coverage. I added the requested missing cases in one dedicated file and included direct contract assertions for already-covered helpers. The checkout has no package lock, so I installed dependencies with `HUSKY=0 npm install --no-package-lock`; no dependency files were added to the diff.

**Toolkit**

- Tool: Codex edited the test-only branch using the issue checklist, existing Jest conventions, and `CLAUDE.local.md` subsystem notes.
- What it produced: `src/__tests__/correlation.test.ts`, with 20 focused cases covering the requested helper behavior.
- Difficulties: `npm ci` could not run because the upstream checkout has no lockfile.
- What changed: installed declared dependencies without creating or committing a lockfile; production source remained untouched.

---

## Testing Strategy

The issue asks for focused coverage, so the decisive check is `npx jest src/__tests__/correlation.test.ts`: it exercises the listed inputs and context boundaries. The candidate result is 1 suite and 20 tests passed. Repository checks passed too: `npm test -- --runInBand` reported 73 suites passed, 1 skipped, 1,140 tests passed, 1 skipped; `npm run typecheck` (`tsc --noEmit`) and `npm run lint` (`eslint src/`) both exited 0. Production source was not changed, so no source-level failure/fix comparison is claimed.

**Toolkit**

- Tool: Jest and the repository's npm scripts, run on `codex/9-correlation-tests` at Node.js v22.22.1 and npm 10.9.4.
- What it produced: focused suite 20/20; full suite 1,140 passed and 1 skipped; typecheck and lint passed.
- Difficulties: the initial clean-install command was unavailable because there is no package lock; the install reported three dependency audit advisories.
- What changed: used `npm install --no-package-lock`, preserved the repository manifests, and recorded the advisory count without applying unrelated dependency updates.

---

## Implementation Notes

**2026-10-27**

Created branch `codex/9-correlation-tests` from upstream `main` and added only `src/__tests__/correlation.test.ts`. The focused tests, full test suite, typecheck, and lint passed. The first ship-gate run blocked on the untracked file; after commit `e9acda0` and push to my fork, it passed all five checks and PR #83 was opened.

**2026-10-27**

No production implementation was needed for this test-only issue. The new tests cover behavior named in #9; I did not infer or patch a runtime bug.

**2026-10-27**

Installed the Unit 8 monitor and wrote a personal playbook. Its state-only canary found PR #83 open for under a day, with no comments or reviews, one passing title check, and review still required. The full run produced a wait note because my 14-day first-review threshold was not met; I checked the body against the broader “polite nudge” label and did not post anything.

**Toolkit**

- Tool: Git for the fork branch and Codex for focused tests, test evidence, and story notes.
- What it produced: one new test file and a repeatable branch state with all required repo checks green.
- Difficulties: the base repository omits a lockfile; the first install attempt with `npm ci` stopped before installing packages.
- What changed: dependencies were installed without modifying the repository's package metadata; no source bug or extra change was added.

---

## Pull Request

**PR Link:** https://github.com/Logixia/logixia/pull/83

**PR Description:** Adds the focused tests in `src/__tests__/correlation.test.ts` for correlation context, middleware, Fastify, Axios, child request metadata, Kafka/SQS/envelope extraction, Kafka headers, and UUIDs. It states that existing partial coverage made the issue's opening claim stale, links `Closes #9`, lists the four passing checks, and discloses Codex assistance.

**Maintainer Feedback:**

- 2026-10-27: the PR monitor read the live thread; there were no maintainer comments or reviews, so there was no feedback to address.

**Status:** Open, awaiting review; at the Unit 8 monitor run on 2026-10-27, the PR was mergeable, review was required, and the Conventional PR title check passed.

**Toolkit**

- Tool: `tools/ship-gate` runs the manifest checks and the live Logixia-scoped `pr-precheck`; its installed hook guards `gh pr create`, and the voice guard checks the outgoing description.
- What it produced: first run blocked on the untracked test file; after commit and push, the gate passed all required checks and returned `accept`. The PR title/body passed the voice check and PR #83 is open.
- Difficulties: `npm ci` was unavailable because the upstream checkout has no lockfile; the first gate run correctly saw no committed diff. A hook-driven Claude wrapper stalled before invoking the command, so I used the passing manual gate and voice check before opening the PR directly.
- What changed: used `npm install --no-package-lock`, committed and pushed the single planned test file, expanded the grader turn limit after its first run hit the cap, and kept the initial block and successful rerun in the record.

---

## Learnings and Reflections

**Technical Skills Gained**

I learned to distinguish GitHub's `REVIEW_REQUIRED` and `BLOCKED` states from a problem with the patch, and to treat mergeability and check results as separate evidence. I also used a headless monitor's read-only state mode, per-PR run history, and playbook-driven draft mode, then checked that its output remained a local draft rather than a posted comment.

**Challenges Overcome**

The monitor's move label said “polite nudge” even though its body correctly said to wait. I read the full draft against my playbook instead of treating the label as an instruction; the PR was less than a day old and had no maintainer activity, so I sent nothing. The repository gives no review SLA, and a small sample of recent PRs did not support a reliable average, so I chose a conservative 14-day first-review threshold and recorded why.

**What I'd Do Differently Next Time**

I would write down the repository's response guidance and my follow-up threshold when I open the PR, then use the monitor's state-only mode before asking any tool to draft a response. I would also check the draft's actual action and rationale, not just its move label, and revisit the decision only when the thread changes or my stated threshold is reached.

---

## Resources Used

- Logixia's [CONTRIBUTING.md](https://github.com/Logixia/logixia/blob/main/CONTRIBUTING.md), especially its patience guidance, test requirements, and PR review rules.
- The AI301 Unit 8 starter's `skill/INSTALL.md`, `skill/monitor.py`, and `skill/playbook-template.md`, used to install the monitor, inspect live state, and write the playbook.
- The live [PR #83 thread](https://github.com/Logixia/logixia/pull/83), which the monitor read and which had no comments or reviews during this run.
