### What is Continuous Integration Testing?
#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: May 8, 2017

<!--deck start--->
Continuous integration testing is a process where code changes are automatically merged with key branches of development, built and tested at a routine frequency and granularity in an effort to reduce integration risk and merge conflicts and improve overall code quality.
<!--deck end--->

<!--body start--->
Continuous integration (CI) testing is a particular category of testing software that is aimed at testing
the merged changes from multiple branches of development, with the highest *reasonable* frequency
and smallest *reasonable* granularity of changes. *Continuous* means that changes are being continuously
merged and tested. *Integration* means that changes from multiple branches are merged and the *integrated*
result is tested. *Integration* also means that testing processes are integrated with as opposed to handled apart
from development processes. Instead of develop, develop, develop, test, test, test, it is
develop, test, develop, test, develop, test.

What constitutes *reasonable* frequency and granularity for CI testing? Teams are free to define what
is *reasonable*. This can vary among teams. Even within a team, different categories of work may be
handled with different frequency and granularity. For example, for bug-fix work, frequency may be once
at the end of each day and granularity may be *completed* bug fixes whereas for
feature enhancements requiring many person-weeks, frequency may be once a week and granularity whatever
changes are completed in a week. For high functioning CI, frequency may be many times per day and granularity
may be each method/function/subroutine added or changed. To understand the ultimate aims of CI, one can imagine CI
testing taken to the extreme is like *auto correct* in a word processor where programmers would get immediate
feedback regarding test status with literally each key-stroke they enter.

CI testing may have a number of implications for **both** software and test development. First, it can demand a
very high level of *automation*.

- Commits on multiple branches can be automatically merged.

- Tests can be automatically triggered as commits are made.

- *Relevant* tests can be automatically determined for a given commit.

- The cause of test failures can be automatically attributed to a given developer's commit(s).

Next, CI testing can often require that tests be designed with several important attributes

- Tests _know_ which code blocks they depend on.

- Different tests do not depend on each other.

- Incremental re-test of only failed tests is supported.

- Multiple tests can be executed in parallel.

- Tests are designed and compute resources are such that tests complete with immediacy.

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

<!--body end--->

<!---
Publish: yes
Pinned: yes
Topics: continuous integration testing
--->
