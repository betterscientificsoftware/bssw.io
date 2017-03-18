# Continuous Integration Testing

Continuous integration (CI) testing is a particular way of testing software that is aimed at testing
the combined code changes from multiple branches of development, with the highest reasonable frequency
and smallest reasonable granularity of changes. The word "continuous" means that changes are continuously
tested. Typically, this will mean many times in a given day of work. The word "integration" means a
couple of things. First, it means that the changes from multiple branches are combined and the integrated
result is tested. It also means that testing processes are integrated with development processes. Instead
of develop, develop, develop, test, test, test, it is develop, test, develop, test, develop, test.

CI testing has a number of implications for software and test development. First, it requires a very high
level of _automation_. Commits on multiple branches are automatically merged. Tests are automatically triggered
as commits are made. Only _relevant_ tests are
triggered for a given commit. The cause of test failures are localized to a given developer's commit(s).
Next, it requires that tests be designed with a number of important attributes such as dependency with
associated blocks of code, orthognalization, incremental re-test, parallelism in test execution and
resource efficiency. It also means
that software changes are designed to follow incrimental (e.g. evolutionary) stages of development. It means
that new tests are added and obsoleted tests updated or removed, almost as often as the code that is being tested.
Finally, it requires that test coverage be high enough that relatively small, isolated code changes anywhere
in the code wind up being tested. In particlar, CI testing means that developers are prevented from working
on separate branches of development for extended periods without being required to merge other's work with
their own on a daily basis.

Compute resources necessary to complete tests must be sufficient that CI testing feedback to developers
is immediate or closely so. Typically, for CSE/HPC codes, this means that only certain types of tests are
appropriate for CI testing. For example, a test that checks convergence of a numerical algorithm at scale is
likely to require too much time (or too large of a compute resource) to be useful in CI testing.

