# What is Continuous Integration Testing?
<!--deck start--->
Continuous integration testing is a process where code changes are automatically merged with key branches of development, built and tested at a routine frequency and granularity in an effort to reduce integration risk and merge conflicts and improve overall code quality.
<!--deck end--->

<!--body start--->
Continuous integration (CI) testing is a particular category of testing software that is aimed at testing
the merged changes from multiple branches of development, with the highest _reasonable_ frequency
and smallest _reasonable_ granularity of changes. _Continuous_ means that changes are being continuously
merged and tested. _Integration_ means that changes from multiple branches are merged and the _integrated_
result is tested. _Integration_ also means that testing processes are integrated with as opposed to handled apart
from development processes. Instead of develop, develop, develop, test, test, test, it is
develop, test, develop, test, develop, test.

What constitutes _reasonable_ frequency and granularity for CI testing? Teams are free to define what
is _reasonable_. This can vary among teams. Even within a team, different categories of work may be
handled with different frequency and granularity. For example, for bug-fix work, frequency may be once
at the end of each day and granularity may be _completed_ bug fixes whereas for
feature enhancements requiring many person-weeks, frequency may be once a week and granularity whatever
changes are completed in a week. For high functioning CI, frequency may be many times per day and granularity
may be each method/function/subroutine added or changed. To understand the ultimate aims of CI, one can imagine CI
testing taken to the extreme is like _auto correct_ in a word processor where programmers would get immediate
feedback regarding test status with literally each key-stroke they enter.

CI testing may have a number of implications for **both** software and test development. First, it can demand a
very high level of _automation_.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &bull; Commits on multiple branches can be automatically merged.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &bull; Tests can be automatically triggered as commits are made.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &bull; _Relevant_ tests can be automatically determined for a given commit.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &bull; The cause of test failures can be automatically attributed to a given developer's commit(s).

Next, CI testing can often require that tests be designed with several important attributes

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &bull; Tests _know_ which code blocks they depend on.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &bull; Different tests do not depend on each other.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &bull; Incremental re-test of only failed tests is supported.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &bull; Multiple tests can be executed in parallel.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &bull; Tests are designed and compute resources are such that tests complete with immediacy.

High frequency and/or fine granularity of CI testing can also mean that software changes are required
to follow incremental stages of development. It means that new tests are added and obsoleted tests updated
or removed, almost as often as the code that is being tested. Finally, it may require that test coverage be high
enough that relatively small, isolated code changes anywhere in the code wind up being tested. In
particular, CI testing typically means that developers are prevented from working on separate branches of
development for extended periods without being required to merge other's work with their own on a
routine basis. Indeed, this is one of the aims of CI testing; to prevent any one branch of development to
fall too far out of sync with any other.

Compute resources necessary to complete tests must be sufficient that CI testing feedbacks to developers
are immediate or nearly so. Typically, for scientific software, this means that only certain types of tests are
appropriate. For example, a test that checks convergence of a numerical algorithm at large scale is
likely to require too much time (or too large of a compute resource) to be appropriate for CI testing.

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: May 8, 2017
<!--body end--->

<!---
Publish: yes
Pinned: yes
Categories: reliability
Topics: continuous integration testing
Tags:
Level: 0
Prerequisites: none
Aggregate: none
--->
