# Toolkit Portfolio

**Student:** Puyang He  
**Course:** AI301 | AI Open Source Capstone  
**GitHub:** Starscreen2  
**Portfolio path:** `beat-3-portfolio/toolkit-portfolio.md`

## Featured Tools

I am featuring issue-scout, repro-check, PR precheck with ship-gate, and PR monitor because their records show what happened when the toolkit met a real open-source contribution. The examples cover choosing an issue, checking what the evidence actually supports, deciding whether a branch is ready to submit, and deciding whether to follow up after submission. I am separating the judgments encoded in the tools from the work performed by Claude, Codex, or other commands. A commit in my course repository does not, by itself, prove that I personally wrote or ran every part of the tool.

**issue-scout**

**What it is, and the judgment hole I wrote:** Issue-scout grades potential first contributions using a rubric instead of treating a `good first issue` label as enough. Its checks include repository activity, manageable scope, active ownership, contribution policies, and maintainer activity; a fit profile helps rank acceptable issues. The judgment is in those thresholds and ownership rules. The later locally installed version also distinguishes whether an issue is `scope-feasible` from how difficult its open edges might be. The available record does not establish who authored each original rule or local revision, so I am not claiming sole authorship.

**How it evolved, dated:** Commit `4e8a12c` added the course-repository skill and rubric on September 22, 2026. On October 27, an attempted Claude scan stopped before searching or grading because Claude Code OAuth had expired. A separate manual fallback used saved GitHub CLI searches and the rubric. After OAuth was restored, Claude re-graded the candidates: Logixia #9 was suitable, while #30 had a recent work claim and open PR #76. Later local review revised the scope and active-owner checks to pay attention to current assignees, open linked PRs, and current non-maintainer claims. The failed scan, manual fallback, and successful Claude re-grade were three distinct activities.

**Evidence:** The September 22 evaluation agreed with 19 of 20 scored examples, above its 18/20 pass bar (`4e8a12c`). The October 27 fallback and subsequent Claude re-grade both supported choosing Logixia #9 over #30; the open PR and claim were deciding evidence against #30. The local scan records are `~/.claude/skills/issue-scout/scan-notes.md` and `scan-output.md`. The later scope edits are local evidence, not a change I can attribute to the September 22 course-repository commit.

**repro-check**

**What it is, and the judgment hole I wrote:** Repro-check asks whether a claim or reproduction package has enough evidence to share. Its rubric requires a relevant environment, steps another contributor can repeat, an artifact showing the stated outcome, a conclusion no broader than that artifact, and communication that follows the repository's rules. A required check marked `unclear` does not pass. This makes the distinction between observed behavior and an attractive explanation part of the grading decision. The record establishes the saved rubric, not which individual authored each line.

**How it evolved, dated:** Commit `abb28e9` added the skill on September 23, 2026. For sandbox issue #65 in Unit 2, the recorded test run reproduced an async-mock problem. In Unit 6, work on Logixia #9 initially searched only `src/__tests__/`. Repro-check identified that the search was too narrow for a repository-wide coverage statement, and the search was expanded to `src/` and `test/`. The record does not identify who personally executed every search or command, so the expanded coverage check should not be described as my personal manual investigation.

**Evidence:** Unit 2 recorded `13 failed, 6 passed`, including `AttributeError: 'coroutine' object has no attribute 'first'` at `result.scalars().first()`; the saved evaluation agreed with 20/20 examples. The expanded Unit 6 static search covered 74 TypeScript test files and found no direct test references for five named correlation helpers. That establishes the searched direct-reference gap, not that a runtime bug was reproduced or that no indirect coverage existed. See `beat-1-sandbox/unit-2/reproduction.md` and commit `abb28e9`.

**pr-precheck with ship-gate**

**What it is, and the judgment hole I wrote:** PR precheck compares the issue, plan, diff, commits, test evidence, repository requirements, and draft PR text before issuing `accept` or `reject`. The ship-gate adds a local command gate: the real-branch manifest calls for focused Jest tests, the full Jest suite, typecheck, and lint, with dated explanations for excluded checks. These rules represent a decision that a clean description alone is not enough; the branch state and recorded commands have to support it. I cannot verify which manifest choices or gate implementation lines I personally wrote, so I am not presenting all of the gate construction as unaided work.

**How it evolved, dated:** Commit `4bd3365` introduced PR precheck on October 4, 2026. In Unit 4, it accepted sandbox PR #88 after the affected tests reached 19 passes and all five CI jobs passed. On October 27, commit `3b29692` added the packaged ship-gate, including its manifest runner, configuration, hook, installer, tests, and Logixia-scoped precheck copy. The first real Logixia gate run stopped because the new test file was untracked. Once commit `e9acda0` was pushed, a second run passed the required checks and the live precheck returned `accept`. The first hook-driven Claude wrapper stalled before invoking its command; the successful gate and voice checks were performed manually before PR #83 was opened. PR #83 discloses that Codex assisted with drafting and reviewing tests. That disclosure does not identify Codex as the sole author of the gate or every test command's operator.

**Evidence:** PR [Logixia/logixia#83](https://github.com/Logixia/logixia/pull/83) changes one test-only file with 20 focused tests. Recorded local results were `20 passed` for the focused Jest suite, `1,140 passed, 1 skipped` for the full Jest suite, and successful typecheck and lint exits. The ship-gate package also records seven unit tests. The before/after branch-state evidence is the first untracked-file block followed by the accepted run after `e9acda0`. PR #83 was open and awaiting review on October 27; none of these results establishes a merge.

**pr-monitor**

**What it is, and the judgment hole I wrote:** PR monitor reads GitHub state through read-only CLI commands and writes a report and possible follow-up draft locally. It does not post comments, edit the branch, or run on a schedule. Its current playbook considers a first review nudge after 14 days, waits at least seven days after a maintainer reply before another follow-up, limits nudges to those with a concrete question, and calls for reassessment after 30 days of silence. These are recorded playbook settings; I have not verified that I personally selected or endorsed each interval.

**How it evolved, dated:** The Unit 8 run on October 27, 2026, examined PR #83 less than a day after it opened. Because the first-nudge threshold had not been met, the draft body said to wait rather than contact maintainers. The generated move label nevertheless said `polite nudge`. That mismatch is a visible weakness in the output, not proof that a corrected monitor was implemented. The report and draft stayed local, and no follow-up comment was posted.

**Evidence:** The October 27 report showed PR #83 open, zero maintainer comments or reviews, one passing title check, `REVIEW_REQUIRED`, and `MERGEABLE` with merge state `BLOCKED`. The local files are `~/.claude/pr-monitor/run-report.md`, `drafted-move.md`, and `playbook.md`. Its concrete result was a local wait note, not a public message or a completed review.

## Inventory

- **plan-check** (`tools/plan-check`): Added September 24, 2026 (`43eb13f`), and evaluated at 20/20 agreement; applied to sandbox issue #65 and rejected evaluation package `pkg-20` for missing required AI-use disclosure, but no real Logixia use is established here.
- **voice-guard** (installed at `~/.claude/voice-guard/`): Used in Unit 6 to check the real issue #9 claim and PR #83 draft; early attempts stopped for an unreadable command body or temporary path, while later claim and PR checks passed. It checks wording against a guide, not whether a maintainer agrees.

## The Arc

**Beat 1**  
Date: September 22, 2026  
Friction: Issue selection needed criteria stronger than an issue label; no separate triggering incident is documented.  
Change: Issue-selection skill, rubric, scope, and evidence guide were added in commit `4e8a12c`.  
Result: Saved evaluation agreement was 19/20, above the 18/20 pass bar. The commit and evaluation record the outcome; they do not prove that I personally authored every file.

**Beat 2**  
Date: September 23, 2026  
Friction: Sandbox issue #65 needed a reproduction supported by command output, not just an explanation of its suspected mock problem.  
Change: Repro-check's required environment, repeatable-step, artifact, and communication checks were added in commit `abb28e9`.  
Result: The Unit 2 recorded run showed `13 failed, 6 passed`, including the coroutine error at `result.scalars().first()`; the saved evaluation matched 20/20 examples.

**Beat 3**  
Date: September 24, 2026  
Friction: A technically bounded plan could still be unsuitable if it ignored reproduction evidence or repository posting rules.  
Change: Plan-check was added in commit `43eb13f`, with checks for causal fit, scope, feasibility, and conventions.  
Result: Its evaluation matched 20/20 examples; `pkg-20` was rejected because the proposed comment omitted the required AI-use disclosure.

**Beat 4**  
Date: October 4, 2026  
Friction: Passing tests alone did not compare a proposed PR with its plan, diff, and repository requirements.  
Change: PR precheck was added in commit `4bd3365`.  
Result: A live check accepted sandbox PR #88 after its target tests reached 19 passes and all five CI jobs passed; the saved evaluation agreed with 20/20 examples.

**Beat 5**  
Date: October 27, 2026  
Friction: Claude Code OAuth expired before the first issue scan could search or grade; later issue-selection review exposed stale scope and ownership assumptions.  
Change: A recorded manual GitHub CLI fallback was kept separate from a later Claude re-grade after OAuth was restored. The installed scout's scope-feasibility and ownership checks were subsequently revised.  
Result: The fallback and Claude re-grade supported #9 and rejected #30 because of a recent claim and open PR #76. No post-revision evaluation result is supplied for the later local rubric changes.

**Beat 6**  
Date: October 27, 2026 (Unit 6)  
Friction: A search limited to `src/__tests__/` could not support a statement about direct tests across the repository.  
Change: The static search was expanded to `src/` and `test/` after repro-check flagged the scope problem.  
Result: The expanded search examined 74 TypeScript test files and found no direct references to five specified correlation helpers. This remained a static coverage finding, not a runtime reproduction.

**Beat 7**  
Date: October 27, 2026  
Friction: The first real ship-gate run found an untracked test file, and the initial hook-driven Claude wrapper stalled.  
Change: Ship-gate was packaged in `3b29692`; the test file was tracked and pushed in `e9acda0`, and the required gate and voice checks were run manually before PR creation. Codex assisted with test drafting and review; attribution for every other command and implementation step is not verified.  
Result: Focused Jest recorded 20 passes; the full suite recorded 1,140 passes and one skip; typecheck and lint passed; live precheck returned `accept`; PR #83 was opened, not merged.

**Beat 8**  
Date: October 27, 2026 (Unit 8)  
Friction: PR #83 was newly open with no review, and its monitor draft had a `polite nudge` label that conflicted with the wait instruction in the body.  
Change: The read-only monitor produced a local status report and wait draft under its existing playbook. No verified playbook or code fix followed.  
Result: No comment was posted; the PR remained open and awaiting review. The output mismatch remained visible in the saved local draft.

## Limitations and What's Next

These tools make evidence easier to collect and compare, but they do not replace judgment about what is worth fixing, which tests genuinely cover the issue, or what to say to a maintainer. Authentication can prevent a scan from starting. GitHub ownership and review state can change after an issue is checked. A static search does not reproduce behavior, and passing local tests do not prove that every relevant case is covered. The first Claude wrapper stall and the PR monitor's inconsistent move label also show that the surrounding automation can fail or communicate the wrong action even when some underlying checks work.

For PR #83, the decision to review, request changes, or merge belongs to the maintainers. Local precheck acceptance and passing commands only established submission readiness against the recorded rules. I do not have a confirmed personal implementation plan to report after this run. Fixing the monitor's mismatch between a `polite nudge` label and a wait-only body is a possible improvement, but I am not claiming that I have committed to it or completed it.

**Tool limits.**

issue-scout: An expired OAuth session can stop a scan, and ownership or scope judgments can become stale as GitHub activity changes.  
repro-check: Searching for direct test references cannot establish complete coverage or show a runtime failure.  
pr-precheck with ship-gate: Passing local checks and receiving `accept` cannot substitute for maintainer review or prove a merge.  
pr-monitor: It reads and drafts only on demand, never posts or edits, and its move label can disagree with its actual recommendation.
