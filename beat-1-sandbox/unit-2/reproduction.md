# Unit 2 — Claim and Reproduce

Path: `beat-1-sandbox/unit-2/reproduction.md`

## Your identity upstream

**GitHub username**

Starscreen2

## Posted upstream

**Claim comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/65#issuecomment-5804498216

I’m going to investigate #65, where `tests/unit/test_review_service.py` reportedly fails because the async mock setup makes `result.scalars()` a coroutine before the test calls `.first()` or `.all()`. I’ll clone the repository, set up the documented Python test environment, run the issue’s pytest target with the seeded xfail markers exposed, and report the environment and observed output before suggesting a change.

**Reproduction comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/65#issuecomment-5804498483

## Environment

- Repository: `Starscreen2/pathreview-ai301-fa26-s1`, forked from `codepath/pathreview-ai301-fa26-s1`
- Commit: `f89c06f` (`main` at the time of the run)
- OS: macOS 15.6.1, Apple Silicon (`arm64`)
- Python: 3.14.0
- pytest: 9.1.1
- pytest-asyncio: 1.4.0
- SQLAlchemy: 2.0.54
- Test dependency set: the repository's `.[dev]` extra in a fresh `.venv`

The issue body does not specify a version or operating system. The test file currently marks the 13 affected tests with `@pytest.mark.xfail(strict=True, reason="issue #65: review_service tests misconfigure async mocks")`; I used `--runxfail` so those expected-failure markers do not hide the underlying failures.

## Steps

From a fresh clone of the fork:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m pytest --runxfail tests/unit/test_review_service.py -q
```

## Observed result

The command completed with:

```text
13 failed, 6 passed, 3 warnings in 3.84s
```

The first failing test, `TestReviewService.test_get_review_returns_review_for_correct_owner`, raised:

```text
AttributeError: 'coroutine' object has no attribute 'first'
```

at `core/services/review_service.py:48` on:

```python
return result.scalars().first()
```

The list-review failures show the corresponding error at line 66:

```text
AttributeError: 'coroutine' object has no attribute 'all'
```

The traceback shows the test fixtures create `mock_result = AsyncMock()` and configure `mock_result.scalars.return_value.first`/`.all`; the service calls `result.scalars()` synchronously on the awaited database result. The 13 failures therefore match the issue's async-mock symptom, while the six `create_review` tests pass.

## Conclusion

Reproduced on the fork's current `main` with the documented Python test dependencies. This confirms the reported test failure; it does not by itself prove the final mock types or a complete fix. The next step is to revise the affected test setup so the awaited `execute()` returns a synchronous result object whose `scalars()` returns a result object with synchronous `.first()`/`.all()` methods, then remove the strict xfail markers and rerun the target.

## Eval iterations

**Run history**

- Smoke run: `agreement: 3/3 scored items`.
- Full run: `agreement: 20/20 scored items (bar: 18/20: PASS)`.
- Final saved run: `agreement: 20/20 scored items (bar: 18/20: PASS)`.

**Package analysis**

`pkg-20`: the rubric decided `reject`, and the gold label was `reject`. This package is the disclosure canary: its reproduction evidence and communication are otherwise strong, but the package does not contain the required AI-assistance disclosure under the repository policy. The rubric therefore rejects it instead of treating a technically detailed reproduction as sufficient on its own.

**Check rationale**

The exact check text I retained in `tools/repro-check/rubric.md` is:

> Pass only when the artifact directly shows the reported behavior, or when a faithful attempt directly shows that the issue did not reproduce. A version banner, successful startup, unrelated error, control result alone, asserted diagnosis, or artifact for an adjacent trigger is not evidence of the issue. The conclusion must distinguish observed from expected behavior.

I kept this check strict because the earlier rubric needed to reject polished reports that asserted the issue without showing the issue's actual behavior. It makes the artifact and the conclusion carry the decision instead of letting a setup banner or an unsupported diagnosis count as proof.

**Trade-offs**

The final run shows `clear-accept 8/8`, `disclosure 1/1`, `no-evidence 4/4`, `unfollowable-comms 3/3`, and `wrong-target 4/4`, with 20/20 agreement. The main trade-off is intentional: the communication check rejects `pkg-20` despite its otherwise strong reproduction because repository-required disclosure is part of a postable package. That catches the policy failure, but it also means a technically excellent report can still be rejected when its communication does not meet the repo's contribution rules.
