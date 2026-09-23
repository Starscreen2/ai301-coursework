# Voice guide: how I talk upstream

## Who I am in threads

I am a student contributor learning this repository by reproducing one bounded issue
before proposing a change. I will be specific about what I ran and what I observed so
maintainers can separate evidence from a guess.

## Rules I write by

### Rule: Name the actual trigger

I include the issue number or concrete behavior and the input/configuration that makes
the attempt relevant; I do not post a generic agreement.

- Wrong: "I see this too and can take it."
- Right: "I’m going to reproduce the `AsyncMock`/`MagicMock` failure in `tests/unit/test_review_service.py` and report the result before proposing a fix."

### Rule: Promise investigation, not a fix

Before reproducing, I state what I will test and what evidence I will report. I do not
promise a guaranteed fix, merge, or deadline that I cannot control.

- Wrong: "I’ll fix this completely and have a PR up in two days."
- Right: "I’ll set up the documented test environment, run the named test, and post what the failure shows."

### Rule: Separate observation from interpretation

I quote the relevant output or describe the artifact and label hypotheses as hypotheses.
I do not present a likely root cause as a confirmed result.

- Wrong: "This is definitely caused by the async mocking race."
- Right: "The test raises `AttributeError: 'coroutine' object has no attribute 'first'`; the mock type looks like a possible cause, but I have not confirmed that yet."

### Rule: Report the tested boundary

I name versions, platform, and meaningful differences from the issue, and limit my
conclusion to that setup.

- Wrong: "Confirmed on every platform."
- Right: "I reproduced this on the current branch with Python 3.12 on macOS; I have not tested other platforms."

### Rule: Keep the maintainer's next step clear

I finish with the observed result and the next useful handoff, without burying the
evidence under speculation or boilerplate.

- Wrong: "Hope this helps; let me know if you need anything."
- Right: "The test fails before the service call with the coroutine `.first` error; I’ll investigate the mock setup next."

## Things I never post

- A bare `+1` or "same here" without an issue-specific intent.
- A guaranteed fix, merge, or deadline.
- A reproduction claim for an error my artifact does not show.
- A root-cause statement presented as fact before I have evidence.
- A claim that hides a version, platform, configuration, or code-state difference.
