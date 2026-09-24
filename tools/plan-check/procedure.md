# Procedure: how this skill grades a plan package

## Read order

1. In live mode, read `scope.md` and `voice-guide.md` first. If the scope
   repository is still a bracketed placeholder, stop without grading. In eval
   mode, ignore both files because the bundle is the complete world.
2. Read the `Issue` section and record the reported trigger, requested
   behavior, and any version or environment boundary.
3. Read `Thread highlights` and `Repo facts`. Record explicit maintainer
   directions, prior-art or ownership constraints, contribution templates,
   branch rules, and any AI-use disclosure requirement. Do not infer a rule
   that is not present.
4. Read `Repro evidence` in full before reading the plan. Record the exact
   observed failure, the controls, the inputs and commands, and what the
   evidence does and does not establish. This prevents the plan's diagnosis
   from becoming the assumed explanation.
   In live mode, map these bundle sections to the actual sources: the issue
   URL and thread comments (including maintainer direction), repository
   documents such as `docs/CONTRIBUTING.md` and any pull-request template,
   and the student's own posted Unit 2 reproduction comment. Do not grade
   from a guessed current issue state when the student's posted evidence is
   the stated source.
5. Read the candidate plan in this order: diagnosis, scope and exclusions,
   files and approach, test plan, then risks/unknowns/deviations. Finally read
   the candidate plan comment as the proposed public handoff. Keep the notes
   above; later checks use them instead of restarting from a different reading
   order.
   If `plan.md` already contains a post-build `Deviations` note, use it for
   the preferred honesty check only; still judge the proposed diagnosis,
   scope, approach, and test plan as the plan that was presented for posting.

## Evidence gathering

Create one compact evidence note for each family:

- Grounding: write the reproduced symptom, the strongest control, and the
  evidence-backed cause (or mark the cause unproven). Compare the plan's
  diagnosis and approach to those notes.
- Scope: list every proposed change and named file/area, then separate the
  issue-sized fix and regression coverage from redesigns, migrations,
  drive-by cleanup, or explicit deferrals.
- Executability: extract the first edit location, the chosen implementation
  path, and the ordered work steps. Mark an essential choice as missing when
  the author leaves it to build time with words such as "somewhere," "maybe,"
  or an unresolved list of alternatives.
- Test: extract the trigger, setup/input, command or fixture, controls, and
  expected-after observation. Mark a test as non-decisive when it only says
  to run a broad suite or judge a subjective impression.
- Comms: extract issue-specific nouns from the comment, each explicit thread
  direction it engages, and each repository convention or disclosure it must
  satisfy. In live mode, use the locations named by the evidence guide.
- Honesty: record risks, unknowns, deferrals, and any deviation. A missing
  statement is not automatically a failure of a preferred check, but a
  material unknown presented as settled fact is a failure of that check.

If a source section is genuinely absent, record `unclear: absent` rather than
searching another section for a replacement fact. The only exception is that
the plan's test and comment are deliberately compared with the issue/repro
notes and the thread/repo notes, respectively.

## Check execution

Run the checks in this order using the evidence notes: diagnosis, scope,
executability, test plan, thread/conventions, then honesty. For each check,
apply its table pass condition to the named evidence only and write one line
with `pass`, `fail`, or `unclear` plus the fact or quote that decided it.

Grade `fail` when the evidence contradicts the pass condition. Grade
`unclear` when the required evidence is absent or the plan leaves the decisive
choice unresolved; do not upgrade uncertainty because the prose sounds
confident. Do not re-read unrelated sections to rescue a missing fact. The
preferred honesty check is still reported, but it does not gate the verdict.

In live mode, apply the voice guide as an additional note about the comment;
the voice guide can identify a broken writing rule, but it cannot change the
rubric verdict unless the communication check names the same requirement.

## Verdict assembly

Accept only if every required check is `pass`. Any required `fail` or
`unclear` yields `reject`. Preferred checks never change that binary result.
For every check, quote or precisely identify the one observed fact that
decided its grade; for a failure or unclear grade, state the missing or
contradictory evidence. Emit the required JSON with the check names, grades,
evidence lines, and final verdict as the last fenced JSON block.
