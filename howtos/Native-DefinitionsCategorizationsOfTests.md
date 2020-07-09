<div align="center">
<h1> Definition and Categorization of Tests for CSE Software </h1>
<h4> The IDEAS Scientific Software Productivity Project </h4>
<h5> <a href="https://ideas-productivity.org/resources/howtos/">https://ideas-productivity.org/resources/howtos</a> </h5>
<h4> Contributed by: </h4>
</div>

### Table of Contents: 
  * [Purpose of this Document](#purpose)
  * [Definitions and Categories of Tests](#definitions)
      * [Granularity of Tests](#granularity)
          * Unit
          * Integration
          * System-level
      * Types of Tests
          * Verification
          * Acceptance
          * No-change
          * Performance
      * Test Analysis Tools
          * Memory Usage Error Detection
          * Code Coverage
  * Discussion
  
<h2 id="purpose">Purpose of this Document</h3>
  
This document provides common classification and definitions for tests for CSE software. These
definitions and classifications are largely consistent with accepted definitions in the broader software
engineering community (for example, as defined on [Wikipedia](https://en.wikipedia.org/wiki/Software_testing) and other online sources). The goal is to define a minimal set of definitions and classifications to cover the types of testing performed in many
CSE projects. The goal is not to create an exhaustive list of all the types of testing that have ever been
defined (such as on the [Wikipedia Software Testing page](https://en.wikipedia.org/wiki/Software_testing)).

In addition to defining these categories and tests, some of the consensus views of the broader (agile)
software engineering community are injected. These views help to motivate and contrast the different
types of tests and help to guide how they can be applied in an effective software development process.

<h2 id="definitions">Definitions and Categories of Tests</h2>
Tests can be categorized by the granularity of the test and the type of test . In addition, different types
of analysis tools/tests can be run using an existing test suite.

<h3 id="granularity"><b><i>Granularity of Tests</h3></b></i>
Tests can be defined at different levels of granularity. The levels of granularity vary from the smallest
units of the software to the entire software system.

  * **Unit Tests:**
   Unit tests are focused on testing individual software units such as individual functions or individual
classes. By definition, unit tests must build fast, run fast, and localize errors. Unit tests are considered
a foundation for modern agile software development methods (e.g. [test-driven
development](https://en.wikipedia.org/wiki/Test-driven_development)) and also
provide a foundation for fast, efficient development and [refactoring efforts](https://en.wikipedia.org/wiki/Code_refactoring). In order to make unit testing cost effective, it is important to use a welldesigned
and easy to use unit test harness (e.g. in the style of [xUnit](https://en.wikipedia.org/wiki/XUnit) tailored to the programming language and particular software being tested.

 * **Integration Tests:** 
   Integration tests are focused on testing the interaction of larger pieces of software but, not at the full
system level . Integration tests typically test several different objects from several different types of
classes together. Integration tests are contrasted from unit tests in that they typically don’t build as
fast, or run as fast or localize errors as well as unit tests. However, these types of more coarse-grained tests may still build and run fast enough to drive effective development and refactoring efforts in many
cases (but not localize errors as well and therefore require more debugging effort when they fail).
