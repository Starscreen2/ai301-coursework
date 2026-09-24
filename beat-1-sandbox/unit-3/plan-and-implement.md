# Unit 3 — Plan and Build

Path: `beat-1-sandbox/unit-3/plan-and-implement.md`

## Posted upstream

**GitHub username**

Starscreen2

**Plan comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/65#issuecomment-5823230126

I reproduced #65 on macOS 15.6.1 arm64 with Python 3.14.0 in
`tests/unit/test_review_service.py`: the awaited `db.execute()` result is
configured as an `AsyncMock`, so the service's `result.scalars().first()`/`.all()`
calls receive a coroutine (13 failures, 6 passes in the Unit 2 report). I plan
to keep `execute` asynchronous but use a synchronous `MagicMock` for the
returned SQLAlchemy result chain, remove the issue-65 xfail markers, and
correct the ordered-list test to expect its count and page queries. The scope
stays in that test file; the service code and unrelated cleanup are out. I’ll
rerun the named target and expect all 19 tests to pass, then report the output
and any deviation.

## Your branch

**Branch**

`fix/65-async-review-mocks`

**Evidence**

Before — the Unit 2 reproduction posted on issue #65:

```text
Repository: Starscreen2/pathreview-ai301-fa26-s1
Commit: f89c06f
OS: macOS 15.6.1, arm64
Python: 3.14.0
pytest: 9.1.1
Command: .venv/bin/python -m pytest --runxfail tests/unit/test_review_service.py -q
Result: 13 failed, 6 passed, 3 warnings in 3.84s
First failure: AttributeError: 'coroutine' object has no attribute 'first'
Other affected path: AttributeError: 'coroutine' object has no attribute 'all'
```

After — branch `fix/65-async-review-mocks`, commit `4e567c3`:

```text
Command: .venv/bin/python -m pytest --runxfail tests/unit/test_review_service.py -q
Result: 19 passed, 1 warning in 0.44s

Command: .venv/bin/python -m pytest tests/unit/test_review_service.py -q
Result: 19 passed, 1 warning in 0.47s
```

The warning is the repository's existing `PydanticDeprecatedSince20` warning
from `core/config.py`; the targeted test result is green in both modes.

## Eval iterations

### Run history

- Smoke run: agreement `3/3` scored items.
- Full run: agreement `20/20` scored items; every category matched.
- Final saved run: agreement `20/20` scored items (bar `18/20`: PASS); every
  category matched.

### Package analysis

`pkg-20`: my rubric decided `reject`, and the gold label was `reject`. The
package's plan is otherwise bounded and follows the thread, but its candidate
comment omits the repository's explicit requirement to disclose AI use. The
thread/conventions check therefore holds it; a technically strong plan cannot
override a stated posting policy.

### Check rationale

The exact check text retained in `tools/plan-check/rubric.md` is:

> Pass only when the proposed cause explains the reproduced behavior and respects the controls. A plan fails if it blames a layer the controls rule out, ignores decisive evidence, or presents an unsupported hypothesis as settled fact.

I kept this check required because Unit 2's reproduction is the foundation for
the plan: a polished plan that chooses the wrong layer is not ready to build
from. The procedure reads the reproduction before the plan's diagnosis so the
plan cannot define its own evidence.

### Trade-offs

The final run matches all five eval categories: `clear-accept 7/7`,
`scope-creep 4/4`, `thread-convention 2/2`, `unbuildable 3/3`, and
`wrong-cause 4/4`. The main intentional trade-off is that the conventions
check rejects `pkg-20` despite its strong technical plan because disclosure is
part of a postable package. On the implementation side, I kept production code
unchanged and accepted that the ordered-list test's `call_count == 2`
assertion is coupled to the current count-plus-page contract; the plan records
that coupling rather than broadening the fix.
