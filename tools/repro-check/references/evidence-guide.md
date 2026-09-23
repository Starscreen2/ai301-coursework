# Evidence guide: where proof lives in a reproduction package

This guide maps each rubric check to the evidence a grader should use. The package is
read in the order issue context, repo facts, claim, and repro report; a polished report
does not substitute for the artifact it claims to show.

## Environment

Where it lives: the repro report's **Environment** section, read against the issue's
target versions/platforms and the repo-facts block. Look for the tool/library version,
OS and architecture, runtime or interpreter, and issue-specific dependencies such as a
driver, shell, browser language, terminal build, solver, or release channel.

What good looks like: the listed values identify where the attempt actually ran. When
they differ from the issue, the report says so and limits the conclusion accordingly;
it does not silently use an old release or a different platform and call that proof of
the current issue.

## Steps

Where it lives: the repro report's **Steps** or **Reproduction** section, plus commands,
fixtures, inline source, configuration, working-directory notes, and stated starting
state. Compare these with the issue body and thread highlights.

What good looks like: a stranger can copy the commands or perform the concrete actions
from the stated starting state and reach the same attempted trigger. Inputs and options
that determine the bug are present, including issue-specific syntax, layout, driver,
language setting, or configuration. A private monorepo, hidden fixture, vague phrase
such as "followed the issue," or an omitted prerequisite makes the steps unfollowable.

## Behavior shown

Where it lives: the report's **Observed result**, command output, traceback, log excerpt,
screenshot description, measurements, or control run. Read it directly against the
issue's stated failure and expected behavior.

What good looks like: the artifact contains the actual symptom that the issue names, or
it clearly shows that the faithful attempt did not reproduce it. A control run can make
the comparison stronger, but a version banner, successful startup, unrelated parser
error, or asserted root cause is not proof of the issue. The report should say what was
observed and what was expected rather than swapping those labels.

## Honesty

Where it lives: the report's conclusion and expected/observed comparison, together with
the claim comment and any version/configuration delta from the issue context.

What good looks like: "reproduced" is reserved for a matching artifact; otherwise the
author says "could not reproduce" and records what was tried and what differed. A report
may be short and still pass, including a real cannot-reproduce. It must not call a
different error the issue, hide a version or platform deviation, claim a crash when the
artifact shows the process survived, or generalize a result beyond the tested setup.

## Comms

Where it lives: the claim and reproduction comments, the issue's thread/policy text in
repo facts, and the report's links or pasted comment text when present.

What good looks like: the claim names the issue-specific behavior and promises only the
next investigation/reproduction step. The reproduction comment gives concrete observed
results in the author's own words. Check the repository's policy before judging AI
disclosure: a required disclosure must appear in a posted comment, while a silent or
permissive policy does not require one. Never treat a generic "+1," "I can fix this in
two days," or unsupported root-cause claim as specific communication.
