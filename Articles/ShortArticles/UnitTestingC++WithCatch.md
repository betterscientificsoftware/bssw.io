# Unit Testing C++ with Catch

#### Contributed by [Mark Dewing](https://github.com/markdewing)

#### Publication date: January 9, 2019

### Introduction

After more than ten years of growth and development, our project -- [QMCPACK](https://github.com/QMCPACK/qmcpack) -- needed  improvements to its development processes.
Changing and understanding the code had become increasingly difficult amid added features,
platforms supported, and the normal student turnover.

Our team determined that one step toward enhancing development velocity was to add unit testing.
Unit testing is valuable for ensuring correctness of a program, performing regression tests, and decomposing the program into small, testable units.
The next step was to choose a method for implementing unit tests.

### Choosing a framework

But before diving into examining unit test frameworks, we might ask whether using a framework is even necessary.
After all, it is straightforward to write a piece of code that exercises some functionality, tests it, and prints the results (pass or fail).
Compiling this code into an executable yields a unit test.
As more tests are written, however, having an easy method to organize them, run all the tests, and track the overall number of passes and fails becomes essential.
Instead of writing such a test from scratch, it is worth looking first at existing frameworks.

After considering several C++ unit test frameworks, we took two of them -- Google Test and Catch -- out for a trial run.
After integrating each test framework into the project build system and
writing several tests, we decided to use Catch.

The main advantages of Catch for our project are twofold:

 * It is a single include file (about 400 KB), making it easy to integrate into the project source tree. (By comparison, Google Test is 3.8 MB and over 200 files.)
 * Being able to use simple C++ comparison operators in the assertion macros looks neater to us than the type and comparison-specific macros in Google Test.


The [Catch website](https://github.com/catchorg/Catch2) has a longer description of the [rationale for Catch and feature list](https://github.com/catchorg/Catch2/blob/master/docs/why-catch.md#top).


## Catch overview

The existing [Catch tutorial](https://github.com/catchorg/Catch2/blob/master/docs/tutorial.md#top) is the essential first stop for learning more about Catch.

Here is a simple example to give the flavor of using Catch.
```
// Define this in only one file to add 'main'
#define CATCH_CONFIG_MAIN
// include the Catch framework
#include "catch.hpp"

// Test cases start with the 'TESTCASE' macro
TESTCASE("Simple Addition", "[test label]")
{
  std::vector<double> v;
  v.push_back(2.1);
  v.push_back(3.1);

  // Test values with the 'REQUIRE' macro
  REQUIRE(v.size() == 2);

  double sum = std::accumulate(v.begin(), v.end(), 0.0);

  // Floating point comparisons with tolerance using 'Approx'
  REQUIRE(sum == Approx(5.1));
}
```

### Assertion macros

Catch uses the `REQUIRE` macro for testing an expression, for example, `REQUIRE(a == 1)` or `REQUIRE(a < 1)`.
Upon failure, Catch reports the value in the following expression.
```
simple_test.cpp:9: FAILED:
  REQUIRE( a == 1 )
with expansion:
  2 == 1
```
To understand the advantage in how Catch handles test expressions, compare it with other approaches. The most basic test is to use the existing `assert` macro.  The downside of this is that a simple test in an assert (e.g., `assert(a == 1)`) loses the value under test (`a`) when the test fails. That is, the assertion message cannot print the value that led to the failure.

One solution is to make assertion macros with two arguments, such as `ASSERT_EQ(a, 1);`. This lets the framework report the value of 'a' upon failure.  However, several macros are needed for the various comparison operators and types (e.g., `ASSERT_GT`, `ASSERT_LT`).

Catch uses templates to decompose the expression into parts so that it can use more natural comparison syntax and still be able to report values in the comparison.

There is, of course, a limitation: the comparisons must be simple expressions. For example, `REQUIRE((a==1) || (a==2))` will not be decomposed.

### Floating-point values

Floating-point values need some allowable tolerance in the comparison. This can be achieved with the Approx class.

```
REQUIRE(a == Approx(3.1));
```
The Approx class has methods for adjusting the tolerance of the comparison (e.g., `Approx(1.0).epsilon(1e-12)`).

### Custom main

Some versions of MPI will output a warning if `MPI_Finalize` is not called before the program exits. However, calling `MPI_Finalize` at the end of a test will disable MPI for all the other tests. This can be handled by creating a custom runner that performs initialization before any tests run and shuts down after all tests complete.
```
#define CATCH_CONFIG_RUNNER
#include "catch.hpp"

int main(int argc, char *argv[])
{
    MPI_Init(argc, argv);
    int result = Catch::Session().run(argc, argv);
    MPI_Finalize();
    return result;
}

```
This custom main can be incorporated into a project by placing it in an include file, such as `catch_mpi_main.hpp`, and including this file in place of `#define CATCH_CONFIG_MAIN / #include <catch.hpp>`.


### Organization

The default organization is to put all the unit tests in a single executable. Most frameworks, including Catch, offer a way to run a subset of tests from the command line. However, a single large executable for the entire project may get difficult to manage.

Our solution is to use multiple test executables, with one executable per top-level source directory. The test sources are placed in a `tests` directory under the source directory. The following is an example.

 ```
     src/Utilities/tests
     src/Numerics/tests
     ...
```

The test executables are named after the directory, such as `test_utilities` and `test_numerics`.


### Interaction with CMake and CTest

Our project uses CMake and CTest for building and running tests. After  the unit test executable is defined, it can be added to CTest with the `add_test` command (assuming the test executable is in the `TEST_BINARY` variable).
```
   add_test(NAME ${TESTNAME} COMMAND ${TEST_BINARY})
```

Tests can be given stylized names to facilitate selections or can be given labels. In our case, the label "unit" is added to denote the unit tests (`set_tests_properties(${TESTNAME} PROPERTIES LABELS "unit")`.

Tests can be selected from CTest by using the `-R` option to perform a regular expression filter on the test name or by using the `-L` options to select a label. For example, all the unit tests can be run with `ctest -L unit`.


### Interaction with other software development processes
Other changes to our development process included adding code review with pull requests on Github.
Unit tests enabled a continuous integration step where the code is built and unit tests are run for every submitted change to the code.  This helps catch errors earlier in the development cycle.

### Conclusion
We added the Catch framework for unit testing to our project, and now it is an integral part of our development process.


<!---
Publish: yes
RSS update: 2018-01-09
Categories: reliability
Topics: testing, reliability
Track: Deep Dive
Tags: bssw-article
Level: 2
Prerequisites: defaults
Aggregate: none
--->

