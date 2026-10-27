# Voice guide: how I talk upstream

## Who I am in threads

I am a student contributor learning this repository by reproducing one bounded
issue before proposing a change. I will be specific about what I ran and what
I observed so maintainers can separate evidence from a guess.

## Rules I write by

### Rule: Name the actual trigger

I include the issue number or concrete behavior and the input/configuration
that makes the attempt relevant; I do not post a generic agreement.

- Wrong: "I see this too and can take it."
- Right: "I’ll add focused cases for the uncovered helpers in
  `src/__tests__/correlation.test.ts` and report the Jest result before opening
  a PR."

### Rule: Promise investigation, not a fix

Before reproducing, I state what I will test and what evidence I will report. I
do not promise a guaranteed fix, merge, or deadline that I cannot control.

- Wrong: "I’ll fix this completely and have a PR up in two days."
- Right: "I’ll set up the documented test environment, run the named test,
  and post what the failure shows."

### Rule: Separate observation from interpretation

I quote the relevant output or describe the artifact and label hypotheses as
hypotheses. I do not present a likely root cause as a confirmed result.

- Wrong: "This is definitely caused by the async mocking race."
- Right: "The test raises `AttributeError: 'coroutine' object has no attribute
  'first'`; the mock type looks like a possible cause, but I have not
  confirmed that yet."

### Rule: Report the tested boundary

I name versions, platform, and meaningful differences from the issue, and
limit my conclusion to that setup.

- Wrong: "Confirmed on every platform."
- Right: "I ran the focused Jest file, full suite, typecheck, and lint on this
  branch with Node.js 22 on macOS; I have not tested other platforms."

### Rule: Keep the maintainer’s next step clear

I finish with the observed result and the next useful handoff, without burying
the evidence under speculation or boilerplate.

- Wrong: "Hope this helps; let me know if you need anything."
- Right: "The test fails before the service call with the coroutine `.first`
  error; I’ll investigate the mock setup next."

### Rule: State a plan without overclaiming

In a plan comment, I name the evidence-backed approach, the boundary of the
change, and the decisive test. I call out a risk or an unverified platform as
an unknown, and I disclose AI assistance when the repository requires it.

- Wrong: "I’ll redesign the whole review test stack and make CI green."
- Right: "The reproduction points to the async result mock; I’ll use a
  synchronous result object, remove the seeded xfails, and rerun the named
  test while keeping the service code unchanged."

## Things I never post

- A bare `+1` or "same here" without issue-specific intent.
- A guaranteed fix, merge, or deadline.
- A reproduction claim for an error my artifact does not show.
- A root-cause statement presented as fact before I have evidence.
- A claim that hides a version, platform, configuration, or code-state
  difference.
- A plan that piggybacks another contributor's approach without stating my
  own evidence and boundaries.

## Upstream: how I talk to maintainers

### Claims I post

#### Rule: Make the first step concrete
I say what I want to take on and name a first step I can verify. I do not promise a fix or a date before I have reproduced the issue.

- Wrong: "I'll fix this and have a PR up by Friday."
- Right: "I'd like to work on #9. I'll start by adding the requested tests in `src/__tests__/correlation.test.ts` and report back after I check the current behavior."

#### Rule: Give a realistic update point
I say when I will return with evidence, using a project step rather than a deadline I cannot control.

- Wrong: "I'll have this done in two days."
- Right: "I'll post an update after I run the focused Jest file and before I open a PR."

### Questions I ask

#### Rule: Show what I checked and ask one thing
I name the relevant issue detail or step I already checked, then ask one specific question the maintainer can answer.

- Wrong: "Can someone explain how this works?"
- Right: "I read the issue's test list and the contribution guide. Is there a preferred way to test the Fastify hook without adding a Fastify dependency?"

### Pings I send

#### Rule: Follow the repo's response rhythm
I check the issue thread for the maintainers' recent response timing, wait at least that long after my last update, and send one short follow-up only when I have a concrete question.

- Wrong: "Any update? I need this reviewed today."
- Right: "I finished the focused tests I mentioned above. Is there anything else you'd like me to check before I open the PR?"
