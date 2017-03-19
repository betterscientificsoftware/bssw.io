# What is Continuous Integration Testing?

Continuous integration (CI) testing is a particular way of testing software that is aimed at testing
the merged changes from multiple branches of development, with the highest _reasonable_ frequency
and smallest _reasonable_ granularity of changes. _Continuous_ means that merged changes are continuously
tested. _Integration_ means a
couple of things. First, it means that the changes from multiple branches are merged and the _integrated_
result is tested. It also means that testing processes are integrated with as opposed to standing apart 
from development processes. Instead of develop, develop, develop, test, test, test, it is
develop, test, develop, test, develop, test. 

What constitutes _reasonable_ frequency and granularity for CI testing? Teams are free to define what
is _reasonable_ and this can vary among and even within teams for different categories of work.
For some teams, frequency may be once at the end of each day and granularity may be _completed_ bug fixes.
Even within a team, different categories of work may be handled with different frequency and granularity.
For example, major enhancments requiring many person-weeks of development, may be use a frequency of a week
and a granularity of whatever amount of work is completed in a week. For high functioning CI, frequency
may be many times per day and granularity may be each method/function/subroutine added or changed.
As a purely conceptual tool in understanding the aims of CI, one can imagine CI testing takien to the extreme
being like _auto correct_ in a word processor where programmers would get immediate feedback regarding test
status with each key-stroke they enter.

CI testing may have a number of implications for **both** software and test development. First, it can demand a
very high level of _automation_.

* Commits on multiple branches can be automatically merged.
* Tests can be automatically triggered as commits are made.
* _Relevant_ tests can be automatically determined for a given commit.
* The cause of test failures can be automatically attributed to a given developer's commit(s).

Next, CI testing can often require that tests be designed with several important attributes

* Tests _know_ which code blocks they depend on.
* Different tests do not depend on each other.
* Incremental re-test of only failed tests is supported.
* Multiple tests can be executed in parallel.
* Tests are designed and compute resources are such that tests complete with immediacy.

The ability to do CI testing can also mean that software changes are designed to follow incrimental
stages of development. It means that new tests are added and obsoleted tests updated or removed,
almost as often as the code that is being tested. Finally, it can require that test coverage be high
enough that relatively small, isolated code changes anywhere in the code wind up being tested. In
particlar, CI testing can mean that developers are prevented from working on separate branches of
development for extended periods without being required to merge other's work with their own on a
routine basis.

Compute resources necessary to complete tests must be sufficient that CI testing feedback to developers
is immediate or nearly so. Typically, for CSE/HPC codes, this means that only certain types of tests are
appropriate for CI testing. For example, a test that checks convergence of a numerical algorithm at scale is
likely to require too much time (or too large of a compute resource) to be appropriate for CI testing.

