# Unit Testing C++ with Catch

#### Contributed by [Mark Dewing](https://github.com/markdewing)

### Introduction

Unit testing is valuable for ensuring correctness of a program, performing regression testing,
 and decomposing the program into small, testable units.


Using an existing framework is not strictly necessary - it is straight forward write a piece of code that exercises some functionality, tests it, and prints the results ('PASS' or 'FAIL').
Compile this into an executable and you have a unit test.
As more tests are written, you will want some way to organize them, run all of the tests and track the overall number of passes and fails.
As this builds in complexity, it will evolve into a unit test framework.
Before going down this path it is worth a look at existing frameworks and see what issues arise and how they are addressed.

We needed to add unit tests to our project ([QMCPACK](https://github.com/QMCPACK/qmcpack)) to improve testing.
We evaluated Google Test and Catch, and decided to use Catch.

The main advantages of Catch for our project are:
 - It is single include file (about 400KB), making it easy to integrate into the project source tree.
 - Tests use simple assertion macro with C++ comparison operators.


The [Catch website](https://github.com/catchorg/Catch2) has a longer description of the [rationale for Catch and feature list](https://github.com/catchorg/Catch2/blob/master/docs/why-catch.md#top)


## Using Catch

The existing [Catch tutorial](https://github.com/catchorg/Catch2/blob/master/docs/tutorial.md#top)
is a good place to start learning.

Here we will give a very brief introduction.

Test cases start with the `TESTCASE` macro.
```
TESTCASE("Test name", "[test label]")
```
The macro takes two arguments. The first is the test name, and the second is one or more test labels.
The test name must be unique, else Catch will print an error at runtime.

The Catch macros are added to the project by including the `"catch.hpp` header file.
One file should also define `CATCH_CONFIG_MAIN` before inclusion in order to define the
main function for the test runner.  (Only one file should do this, or you will get multiple definition errors at link time)

Once the test is compiled, it can be run.  The runner defines a number of command line options, which can be displayed with `-h`.

### Assertion macros

Catch uses the `REQUIRE` macro for testing an expression.
For example, `REQUIRE(a == 1)` or `REQUIRE(a < 1)`
Upon failure, Catch reports the value in the expression:
```
simple_test.cpp:9: FAILED:
  REQUIRE( a == 1 )
with expansion:
  2 == 1
```
To understand the value in this, compare this to other approaches.

The most basic test is to use the existing `assert` macro.  The downside of this is a simple test in an assert (e.g. `assert(a == 1)`) loses the values under test (`a`) when the test fails. That is, the assertion message cannot print the value that led to the failure.

One solution is to make assertion macros with two arguments, such as `ASSERT_EQ(a, 1);`
 This lets the framework report the value of 'a' upon failure.
 However this requires several macros for the various comparison operators and types (e.g. `ASSERT_GT`, `ASSERT_LT`, ...)

Catch uses templates to decompose the expression into parts so that it can use more natural comparison syntax and still be able to report values in the comparison.
 There is a limitation that the comparisons must be simple expressions.
   For example, `REQUIRE((a==1) || (a==2))` will not be decomposed.


### Organization

The default organization is to put all the unit tests in a single executable.
Most frameworks, including Catch, offer a way to run a subset of tests from the command line.
However, a single large executable for the entire project may get difficult to manage.

Our solution is to use multiple test executables, with one executable per top level source directory.
The test sources are placed in a `tests` directory under the source directory.

For example,
```
     src/Utilties/tests
     src/Numerics/tests
     ...
```

The test executables are named after the directory, such as `test_utilities`, `test_numerics`, etc.


### Interaction with CMake and CTest
  Our project uses CMake and CTest for building and running tests.
  Tests can be added to CTest with the `add_test` command,
```
   add_test(NAME ${TESTNAME} COMMAND ${TEST_BINARY})
```

   Tests can be given stylized names to facilitate selections, or you can use labels.
   In our case, the label "unit" is added to denote the unit tests. ( `set_tests_properties(${TESTNAME} PROPERTIES LABELS "unit")`

   Tests can be selected from ctest using the `-R` option to perform a regular expression filter
on the test name, or with the `-L` options to select a label.
   For example, all the unit tests can be run with `ctest -L unit`.


### Floating point values

Floating point values need some allowable tolerance in the comparison.
This can be achieved with the Approx class.

```
REQUIRE(a == Approx(3.1));
```
The `Approx` class has methods for adjusting the tolerance of the comparison (e.g. `Approx(1.0).epsilon(1e-12)`)


### Custom main

We may want to perform some initialization or shutdown for the unit tests.
For example, some versions of MPI will output a warning if `MPI_Finalize` is not called before the program exits.
However, calling `MPI_Finalize` at the end of a test will disable MPI for all the other tests.

This can be addressed by creating a custom runner, such as
```
#define CATCH_CONFIG_RUNNER
#include "catch.hpp"

int main(int argc, char *argv[])
{
    MPI_Init(argc, argv);
    int result = Catch::Session().run(argc, argv);
    MPI_Finalize();
    return  result;
}

```
This can be incorporated into the project by defining an include file, such at 'catch_mpi_main.hpp', and including this file in place of `#define CATCH_CONFIG_MAIN / #include <catch.hpp>`.


<!---
Publish: preview
Categories: reliability
Topics: testing, reliability
Tags: bssw-article
Level: 2
Prerequisites: defaults
Aggregate: none
--->
