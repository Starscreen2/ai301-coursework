# Evidence guide: where evidence lives in a plan package

Use the named package sections rather than treating the whole bundle as one
undifferentiated source. In live mode, the same facts come from the issue,
its thread, the repository documents, and the student's posted reproduction.

## Diagnosis and grounding

Where it lives: the `Issue` section gives the reported behavior; the
`Repro evidence` block gives the observed result, controls, environment, and
any bounded interpretation; the candidate plan's `Diagnosis` and `Approach`
state what the author thinks is happening and what will change.

What good looks like: the diagnosis accounts for the reproduced symptom and
survives the controls. If the evidence only proves a symptom, a plan may name
the cause as a hypothesis and test it, but may not claim the controls proved a
different cause.

## Scope

Where it lives: the candidate plan's `Scope`, `Files`, `Proposed changes`,
and explicit `Not in scope` or deferral lines, read against the issue's
requested behavior in `Issue`.

What good looks like: the plan names one issue-sized change and the files or
areas needed for it. A bounded plan can defer adjacent redesigns; a plan that
adds migrations, broad refactors, new options, or unrelated cleanup is scope
creep even when its central diagnosis is right.

## Executability

Where it lives: the candidate plan's `Files`, `Approach`, and ordered steps;
the `Repo facts` block supplies the repository layout, conventions, and
available test commands. In live mode, confirm the same facts in the named
repository documents.

What good looks like: an executor can identify the first file or area, the
essential code path or configuration, and the implementation choice without
asking the author to resolve "maybe" alternatives. Exact function names are
helpful but not required when the named area and approach make the starting
point unambiguous.

## Test plan

Where it lives: the plan's `Test plan`, compared with the commands, inputs,
controls, and observed failure in `Repro evidence`.

What good looks like: the plan re-runs the issue's trigger and names the
expected-after output, status, or state, while preserving relevant controls.
Regression tests are useful, but "run the full suite," "verify it works," or
"nothing else breaks" without a decisive observation is not enough.

## Honesty

Where it lives: the plan's `Risks`, `Unknowns`, `Deferrals`, and `Deviations`
sections, plus any distinction between observed facts and proposed work.

What good looks like: uncertainty is labeled, not smuggled in as certainty;
the plan says what will be checked, what cannot be checked, and what is
deliberately left out. After implementation, `plan.md` records any change
between the posted plan and the built change in its deviations section.

## Comms

Where it lives: `Thread highlights` contains explicit maintainer direction,
prior-art or ownership constraints; `Repo facts` contains contribution
templates, branch rules, and any AI-use policy; `Candidate plan comment` is
the outgoing text. In live mode, use the actual issue thread, repository
documentation, and the student's posted Unit 2 reproduction comment.

What good looks like: the comment is specific to the issue and the author's
own evidence, acknowledges explicit direction or competing work when the
thread supplies it, and includes required disclosure when the repository
requires it. Silence in a package is not permission to invent a direction or
policy that is not stated there.
