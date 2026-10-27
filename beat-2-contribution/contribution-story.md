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

**Unit 6: I had Codex install the voice guard and prepare repo memory**

Codex helped extend my voice guide with rules for claims, questions, and pings, make it the shared guide for my installed skills, and install the voice-guard hook; the hook configuration was found and a direct wiring check stopped a comment command with no readable body. The claim-draft review could not run because Claude Code was logged out, so I left the GitHub claim pending instead of posting without the required check. Codex also prepared a short `CLAUDE.local.md` for the issue's subsystem and excluded it from Git so it stays in my fork.

**Unit 7: [one line on the tool work]**

[2-4 sentences: the ship-gate and your gate manifest. What it produced
on your real branch, what fought you, what changed because of it.]

**Unit 8: [one line on the tool work]**

[2-4 sentences: the PR-monitor and your playbook. What it read, what it
drafted, what you did with the draft.]

---

## Why I Chose This Issue

I found [Logixia issue #9](https://github.com/Logixia/logixia/issues/9) on the AI301 Issue Selection site. Codex manually rechecked it against my updated rubric because Claude Code could not authenticate. The manual result was accept, straightforward: the issue names `src/correlation.ts`, the requested test file, nine exports, and concrete test cases; the live thread has no comments, assignee, or linked open PR. The test-only TypeScript work fits the profile I saved in Unit 1, and I want to learn how this repository uses its correlation context and test patterns.

Codex helped with the search and grading, so I read the live issue and `CONTRIBUTING.md` before choosing. The rubric’s old strict scope gate would have rejected issues with open edges; I replaced it with `scope-feasible` and a difficulty note, then manually rechecked #9 and rejected #30 because another contributor has an active claim and open PR. This is a manual fallback, not the required Claude scout result. **Claim comment:** claim pending — 2026-10-27; the required voice check is blocked by the expired Claude Code login, so I have not posted a comment.

**Toolkit**

- Tool: issue-scout search strategy and rubric, with Codex doing a documented manual fallback after Claude Code authentication failed.
- What it produced: a manual accept for #9 with a straightforward difficulty note, based on its named test file, explicit cases, and current open ownership state.
- Difficulties: the required Claude scan and re-grade could not run, so no Claude grading credit was used.
- What changed: replaced the strict newcomer-scope check with `scope-feasible` and added non-verdict difficulty notes; manually rechecked #9 and #30.

---

## Understanding the Issue

**Problem Description**

[In your own words, what is broken or missing?]

**Expected Behavior**

[What should happen?]

**Current Behavior**

[What actually happens?]

**Affected Components**

[Which parts of the codebase are involved?]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Reproduction Process

**Environment Setup**

[What a stranger would need to stand this up: your operating system,
the relevant versions (language, runtime, package manager, the project
itself), and how you set the project up. Then the challenges you faced
and how you solved them, or that none came up.]

**Steps to Reproduce**

1. [Step 1]
2. [Step 2]
3. [Observed result]

**Reproduction Evidence**

- **Commit showing reproduction:** [link to commit in your fork]
- **Screenshots/logs:** [if applicable]
- **My findings:** [what you discovered during reproduction; an
  honest, evidenced cannot-reproduce that led you to re-pick or ask
  the maintainer belongs here and costs you nothing]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

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
