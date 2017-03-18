# What is Continuous Integration Testing?

Continuous integration (CI) testing is a particular way of testing software that is aimed at testing
the combined changes from multiple branches of development, with the highest _reasonable_ frequency
and smallest _reasonable_ granularity of changes. _Continuous_ means that combined changes are continuously
tested. Typically, this will mean many times in a given work day. _Integration_ means a
couple of things. First, it means that the changes from multiple branches are merged and the _integrated_
result is tested. It also means that testing processes are integrated with as opposed to standing apart 
from development processes. Instead of develop, develop, develop, test, test, test, it is
develop, test, develop, test, develop, test. Taken to its extreme, one can imagine CI testing like _auto correct_
in a word processor where programmers would get immediate feedback regarding test status with each
key-stroke.

CI testing has a number of implications for **both** software and test development. First, it requires a very high
level of _automation_.

* Commits on multiple branches are automatically merged.
* Tests are automatically triggered as commits are made.
* Only _relevant_ tests are automatically determined and triggered for a given commit.
* The cause of test failures are automatically localized to a given developer's commit(s).

Next, it often requires that tests be designed with several important attributes

* Tests _known_ which code blocks they depend on.
* Tests are _orthogonalized_
* Incremental re-test of only failed tests is supported.
* Parallelism in test execution is supported.
* Compute resources are such that tests complete with immediacy.

The ability to do CI testing also means that software changes are designed to follow incrimental
stages of development. It means that new tests are added and obsoleted tests updated or removed,
almost as often as the code that is being tested. Finally, it requires that test coverage be high
enough that relatively small, isolated code changes anywhere in the code wind up being tested. In
particlar, CI testing means that developers are prevented from working on separate branches of
development for extended periods without being required to merge other's work with their own on a
routine basis.

Compute resources necessary to complete tests must be sufficient that CI testing feedback to developers
is immediate or nearly so. Typically, for CSE/HPC codes, this means that only certain types of tests are
appropriate for CI testing. For example, a test that checks convergence of a numerical algorithm at scale is
likely to require too much time (or too large of a compute resource) to be appropriate for CI testing.

