# How to Improve Testing for CSE Software

#### Contributed by  [Roscoe A. Bartlett](https://github.com/bartlettroscoe), [Barry Smith](https://github.com/BarrySmith), [Ulrike Meier Yang](https://github.com/ulrikeyang), [Glenn Hammond](https://github.com/ghammond86), [Xiaoye Li](https://github.com/xiaoyeli), and [James Willenbring](https://github.com/jwillenbring)

#### Publication Date: August 6, 2019

<!-- deck text start -->
Software requires regular extensive testing to ensure correctly functioning code.
This article provides a straightforward process to add testing to an existing software project that has no testing (or insufficient testing).
<!-- deck text end -->

### Overview
Adding tests of sufficient coverage and quality improves confidence in software and makes it easier to change and extend.
Tests should be added to existing uncovered code before the code is changed.
Tests should be added to new code before (or while) it is being written.
These tests then become the foundation of a regression test suite that helps effectively drive future development while maintaining behavior and improves long-term sustainability.

### Target Audience
Computational Science and Engineering (CSE) software project leaders and developers who are facing significant refactoring efforts because of hardware architecture changes or increased demands for multi-physics and multi-scale coupling, and who want to increase the quality and speed of development and reduce development and maintenance costs.

### Purpose
Show how to add quality testing to a project in order to support efficient modification of existing code or addition of new code.
Show how to add tests to support (1) **adding a new feature**, (2) **fixing a bug**, (3) **improving the design and implementation**, or (4) **optimizing resource usage**<sup>[1]</sup>

### Prerequisites

First read the document *[What Are Software Testing Practices?](./UnderstandingSoftwareTestingPractices.md)* and browse through *[Definition and Categorization of Tests for CSE Software](./DefinitionsCategorizationsOfTests.md)*.

### Steps

<ol>
<li>Set up <b>automated builds of the code</b> with high warning levels and eliminate all warnings.</li>
<li><b>Select test harness frameworks</b>
  <ol type="a">
  <li><b>Select a system-level test harness</b> for system-executable tests that report results appropriately (e.g., CTest/CDash).</li>
  <li><b>Select a unit test harness</b> to effectively define and run finer-grained integration and unit tests (e.g., Google Test, pFUnit).</li>
  <li><b>Customize or streamline</b> system-level and/or unit test frameworks for use in your particular project.</li>
  </ol>
  </li>
<li><b>Add system-level tests</b> to protect major user functionality.
  <ol type="a">
  <li>Select inputs for several important problem classes and run code to produce outputs.</li>
  <li>Set up no-change or verification tests with a system-level test harness in order to pin down important behavior.</li>
  </ol>
  </li>
<li><b>Add integration and unit tests</b> (as needed for adding/changing code)
  <ol type="a">
  <li><b>Incorporate tests for uncovered code to be changed</b> using the <b><it>Legacy Software Change Algorithm</it></b><sup><a href="#sfer-ezikiw-1">1</a></sup>
    <ul>
    <li><b>Identify change points</b> for target change or new code.</li>
    <li><b>Find test points</b> where code behavior can be sensed.</li>
    <li><b>Break dependencies</b> in order to get the targeted code into the unit test harness.</li>
    <li><b>Cover targeted code</b> to be changed with sufficient (characterization) tests.</li>
    </ul>
    </li>
  <li><b>Add new features or fix bugs</b><sup><a href="#sfer-ezikiw-1">1</a>,<a href="#sfer-ezikiw-2">2</a>,<a href="#sfer-ezikiw-3">3</a></sup>
    <ul>
    <li><b>Add new tests</b> that define desired behavior (feature or bug).</li>
    <li>Run new tests and <b>verify they fail</b>.</li>
    <li>Add the minimal code to <b>get new tests to pass</b>.</li>
    <li><b>Refactor</b> the covered code to clean up and remove duplication.</li>
    <li><b>Review</b> all changes to existing code, new code and new tests.</li>
    </ul>
    </li>
  </ol>
  </li>
<li>Select <b>code coverage</b> (e.g., gcov/lcov) and <b>memory usage error detection</b> (e.g., valgrind, clang memory/address/leak sanitizers) analysis tools.</li>
<li>Define a set of <b>regression test suites</b>.
  <ol type="a">
  <li>Define a faster-running <b>pre-merge regression test suite</b> (e.g., single build with faster running tests) and <b>run it before every merge to the mainline branch</b>.</li>
  <li>Define a more comprehensive nightly <b>regression test suite</b> (e.g., builds and all tests on several platforms and compilers, code coverage, and memory usage error detection) and <b>run every night</b>.</li>
  </ol>
  </li>
<li>Have a policy of <b>100% passing pre-merge regression tests</b> (run using a CI testing system like GitHub Actions, GitLab CI, or Jenkins) and work hard to maintain that.</li>
<li>8. Work to <b>fix all failing nightly regression tests</b> on a reasonable schedule.</li>
</ol>

### FAQs:

**Q: Why do you need both a system-level and a unit test harness?**<br>
**A**: A unit test harness aggregates hundreds of unit and integration tests into single executables.
A system-level test harness runs these aggregate integration and unit test executables along with the other system-level acceptance and verification tests and alerts developers of any failures.

**Q: Why not just add all of the tests for an existing code and get it over with?**<br>
**A**: Taking weeks or months (or years) to add sufficient tests for an entire existing code (that lacks sufficient testing) is not usually economical or necessary.
Tests need to be added to code only when it is changed (or when adding new code).
In that way tests can be added while regular development work is being done.

**Q: Why demand 100% passing pre-merge regression tests?**<br>
**A**: This avoids expensive debugging and other investigations needed to determine whether your changes are breaking failing tests or not (hard).
If all tests pass, then your changes could be breaking them (easy).

<!---

ToDos:

* Improve the deck text ...

--->

<!--- References --->

<!---
Publish: yes
Pinned: no 
Topics: Testing
Track: how to
--->

[1-sfer-ezikiw]: https://bssw.io/items/working-effectively-with-legacy-code "Working Effectively with Legacy Code {Michael Feathers. Prentice Hall, 2005}"
[2-sfer-ezikiw]: https://www.oreilly.com/library/view/test-driven-development/0321146530/ "Test Driven Development {Kent Beck, Addison-Wesley Professional, 2003, ISBN: 0321146530}"
[3-sfer-ezikiw]: https://bssw.io/items/code-complete-a-practical-handbook-of-software-construction "Code Complete: Second Edition}"

<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "Working Effectively with Legacy Code"
[2]: #sfer-ezikiw-2 "Test Driven Development"
[3]: #sfer-ezikiw-3 "Code Complete: Second Edition}"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[Working Effectively with Legacy Code<br>Michael Feathers. Prentice Hall, 2005](https://bssw.io/items/working-effectively-with-legacy-code)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[Test Driven Development<br>Kent Beck, Addison-Wesley Professional, 2003, ISBN: 0321146530](https://www.oreilly.com/library/view/test-driven-development/0321146530/)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[Code Complete: Second Edition}](https://bssw.io/items/code-complete-a-practical-handbook-of-software-construction)
