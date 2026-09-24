# Rubric: is this plan ready to post and build from?

The checks judge the plan's outcome against the issue, the captured
reproduction, the thread, and the repository facts. They do not reward
length or headings by themselves.

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Diagnosis follows the reproduction | The issue statement and the package's `Repro evidence` block, especially observed behavior, controls, and any stated cause; then the plan's diagnosis and approach | Pass only when the proposed cause explains the reproduced behavior and respects the controls. A plan fails if it blames a layer the controls rule out, ignores decisive evidence, or presents an unsupported hypothesis as settled fact. | required |
| Scope is one bounded change | The plan's scope/in-scope/not-in-scope text, named files or areas, and the issue's requested behavior | Pass only when the change is limited to the issue-sized fix and its necessary regression coverage, with unrelated redesigns, migrations, drive-by cleanup, and speculative fronts explicitly excluded or deferred. A plan that buries the narrow fix inside a broader campaign fails. | required |
| A stranger can start the work | The plan's files/areas and ordered approach, read with the `Repo facts` block and `Evidence guide: Executability` | Pass only when the essential implementation decisions are made: a stranger can identify where to edit, what behavior to change, and the order to begin without asking the author to choose between unresolved layers or "somewhere/maybe" options. | required |
| The test plan is decisive | The plan's test plan read against the repro steps, controls, and expected outcome in `Repro evidence` | Pass only when the plan names a runnable or otherwise concrete check, the relevant input/setup, and an observable expected-after result that distinguishes the bug from a generic green suite. A full-suite-only or subjective test plan fails. | required |
| Thread and repository conventions are respected | `Thread highlights`, `Repo facts` contribution policy/templates/AI-use policy, and the candidate plan comment | Pass when the comment names the issue-specific behavior, engages explicit maintainer direction or prior-art constraints when present, states the author's own plan rather than piggybacking, and satisfies any stated disclosure or contribution rule. If the package states no applicable policy or direction, do not invent one. | required |
| Unknowns and trade-offs are honest | The plan's risks, unknowns, deferrals, controls, and deviation note if present | Pass when material uncertainty is labeled as uncertainty, risks have a bounded validation step or an explicit deferral, and the plan does not promise certainty beyond the evidence. This is a quality signal; it never overrides the required checks. | preferred |

## Verdict rule

Accept only when every required check passes. A failed or unclear required
check produces `reject`; an unclear preferred check is reported but does not
change the verdict. Preferred checks never gate acceptance.
