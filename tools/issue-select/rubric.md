# Rubric: is this a good first issue?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever checks
you define here. It ships empty on purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where. Name the source
     (repo-facts block, issue body, comment thread, or the locations in
     references/evidence-guide.md). "The repo" is not a source; "the last
     5 default-branch commit dates" is.
   - Pass condition: a condition someone else could apply and get your
     answer. Prefer thresholds with numbers ("a maintainer commented
     within 30 days") over adjectives ("maintainer is responsive").
   - Weight: `required` (a fail here rejects the issue) or `preferred`
     (never changes the verdict; a nice-to-have that helps rank the
     issues you accept).

2. A verdict rule below the table: how the check grades combine into
   accept or reject, including how `unclear` is treated. The verdict
   space is binary. If you write no rule for `unclear`, the skill treats
   it as fail.

Cover what actually kills first contributions. The lecture named four
families: the maintainer is alive, the repo is in use, the scope fits a
newcomer, and nobody else is already on it. A rubric that ignores a family
will fail eval issues designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Repository is alive | In the repo-facts block, inspect `archived`, `last push to any branch`, the five default-branch commits, and the latest release date. | The repository is not archived, and either the last push to any branch or the newest default-branch commit is within 365 days of the bundle's capture date. A repository that is archived fails even if its issue is otherwise clear. | required |
| Change is bounded and actionable | Read the issue body, its stated files or reproduction steps, labels, and the comment thread. | The request describes a finite contribution with a concrete behavior, file/location, test, or acceptance signal. A multi-file documentation or configuration change passes when it enumerates the target files/sections and the expected content or result. A bug report passes when it names one user-visible failure or interaction and gives a reproduction, affected examples, or a diagnosed location; possible root causes or implementation suggestions are context, not automatic scope failure. A maintainer-filed `good first issue` bug in one named feature area can pass with a concise list of at least two affected behaviors even when paths or tests are omitted. Fail an explicit umbrella/megaissue/tracking list, a codebase-wide initiative, a pure usage question, a request whose design or product decision is still unresolved, or a thread showing unresolved design debate plus repeated abandoned attempts. An old claim or closed PR alone does not make a concrete issue unbounded when the thread invites a fresh contributor. | required |
| No active owner or implementation | In the repo-facts block, inspect `this issue: assignees` and `linked PRs`; read the issue thread for current work claims. | No assignee is listed and no linked pull request is open. Closed or merged PRs and clearly stale/abandoned claims do not fail this check. In live Path Review mode, apply the scope file's classroom rule: another student's claim comment by itself does not block the issue; an assignee or open linked PR is the active-ownership signal. | required |
| Contribution workflow is permitted | Read the contribution-policy line in repo facts and any named AI policy or contributor document. | Pass when the repository is silent, permits AI-assisted work, or permits it with disclosure, review, testing, or understanding requirements. Fail only when the policy expressly bans AI-generated code or documentation, rather than merely discouraging it or requiring human review. | required |
| Maintainer signal is present | Inspect the authors of the five newest default-branch commits and the maintainer first-response sample in repo facts. | At least one of the five newest default-branch commits is a human-authored commit within 365 days of capture. Bot-only activity does not satisfy this check, although a recent human commit may be a merge commit. | required |
| Low-reuse fit | In live mode, inspect the issue thread, assignee box, Development box, and participant list; in eval mode, inspect the comment thread and ownership facts. | Preferred pass when there is no visible non-maintainer comment saying someone will take or is working on the issue, no assignee, and no open linked PR. This check never changes accept/reject; it ranks accepted candidates and lets the student prefer a cleaner, less-reused issue. | preferred |

## Verdict rule

Accept only when every required check passes. A required `unclear` is a
failure because a first issue that cannot be verified is not ready to take.
Preferred checks never change the verdict; they only rank issues that already
pass the required checks.
