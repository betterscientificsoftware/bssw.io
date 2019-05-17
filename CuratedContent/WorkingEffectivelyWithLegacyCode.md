# Working Effectively with Legacy Code

## Feathers, Michael, 2005, ISBN-13: 978-0131177055

Legacy software is very hard to modify and extend, as it often relies on obsolete software and hardware, lacks testing, and may have no developers familiar with its complexities.
This book gives one hope that we can use targeted, incremental unit testing and refactoring to turn legacy software into better tested, understood, and extensible software while implementing and
delivering new functionality at the same time.

If one read the book "Refactoring" by Martin Fowler and felt a little uneasy about how this would apply to large nasty software projects, then "Working Effectively with Legacy Code" is the book to read.
What’s more, Michael mentions and reviews many of the object-oriented principles in "Agile Software
Development" as well as other bits of information that one would find in other
great books about software development.
One can view this book as the logical culmination of the books "Refactoring" and "Test Driven Development" (TDD); it's where the rubber meets the road combining unit testing and refactoring.

The definition of "Legacy Code" given in this book is simple and yet shocking (to many people):

> Legacy Code == Code Without Tests

Micheal Feathers States:

> "Code without tests is bad code. It does not matter how well written it is; it doesn't matter how pretty or object-oriented or well-encapsulated it is. With tests, we can change the behavior of our code quickly and verifiably. Without them, we really don’t know if our code is getting better or worse."

Micheal lists four reasons to change software:

* Adding a feature
* Fixing a bug
* Improving the design (i.e. refactoring)
* Optimizing resource usage

He argues that no matter what change is made to the code, we must always maintain other behavior that we are not meaning to change and states:

> "Behavior is the most important thing about software. It is what users depend on. Users like it when we add behavior (provided it is what they really wanted), but if we change or remove behavior they depend on (introduce bugs), they stop trusting us."

The main contribution of this book is the "Legacy Code Change Algorithm":

1. **Identify the targeted legacy code:**
    1. **Identify change points** for the target change or new code addition.
    2. **Find test points** where the behavior of the code can be sensed.
2. **Get targeted legacy code into test harness and cover with tests:**
    1. **Break dependencies** (very carefully and often without sufficient tests) and get the targeted legacy code into a test harness.
    2. **Cover targeted legacy code** with (characterization) unit tests.
3. **Add new functionality with new tests** (usually following the Test Driven Development (TDD) process).
4. **Refactor** tested code to remove duplication, clean up, etc.

Above, Step 1 defines the targeted subset of legacy code that must have tests which depends on what needs to change, what can be sensed, and where dependencies can be broken.
After the targeted legacy code has been covered with unit tests in Step 2, it should have close to 100% coverage (otherwise one can not claim that existing behavior is being preserved, unless the uncovered code and behavior is never used by anyone, in which case it should likely be removed).
Any refactorings in Step 4 are safe to perform once the targeted code is sufficiently covered with tests.
Refactoring is critical to improve the clarity and maintainability of the code.
WARNING: The refactorings must not extend outside code that is sufficiently covered by tests!

The most challenging part of the Legacy Software Change Algorithm is getting the targeted legacy code into a unit test harness and covering it with tests which (in more detail) includes the steps:

* **Identify change points**: Find out where in the legacy code you want to make a change or add new code.
Targeted changes should be done in small iterations so this should hopefully just be a single function or a few functions and hopefully only a single class if possible.

* **Find test points**: Find out where in the code you can sense variables, or call functions, etc. such that you can detect the behavior of the code you want to change.
You may need to add "sensing" variables to help see what you need to see in a unit test.

* **Break dependencies**: Dependencies need to be broken for one of two reasons: Sensing and Separation.  With **Sensing**, one must be able to inspect the behavior of the code that we can’t otherwise see.  While **Separation** is needed to allow the code to be run in a test harness outside of the production setting.
Actually breaking the dependencies involves doing minimal refactorings with careful hyper-sensitive editing.
(There are special dependency-breaking refactorings defined in this book to help with this critical task.)

* **Cover legacy code with unit tests**: If you have the specification for how the targeted legacy code is supposed to work, then write tests to that specification.
Otherwise, write "Characterization Tests" to see what the code actually does under different input scenarios.
NOTE: When the official specification differs from the actual observed behavior of the code, go with the actual behavior for because that is what users actually depend on.
(Differences between specified/desired behavior and actual behavior can be addressed in later iterations if one desires breaking backward compatibility.)

Another major contribution of this book is in detailing the strategies that can be used in the various steps of the Legacy Code Change Algorithm which include:

* **Faking Collaborators:**  Needed to get targeted code into a unit test harness and drive unit tests.:
  - **Fake Objects**: Impersonates a collaborator to allow sensing and control.
  - **Mock Objects**: Extended Fake Objects that asserts expected behavior.
* **Seams**: Ways of inserting test-related code:
  - **Preprocessing Seams**: Preprocessor macros to replace functions, replace header files, etc.
  - **Link Seams**: Replace implementation functions (program or system) to define behavior or sense changes.
  - **Object Seams**: Define interfaces and replace production objects with mock or fake objects in a test harness. (NOTE: Prefer object seams to link or preprocessing seams!)

The Legacy Code Change Algorithm is applied in many small iterations over and over again as pieces of the legacy software are changed.
Over time, these small refactorings can result in significant improvements to the quality and sustainability of the software and can even perform major (beneficial) architectural changes over time.
In fact, at some point, the software may have improved to the point where there is enough strong testing that it is no longer considered legacy code!

This book is packed with practical examples that show nearly every trick there is for refactoring nasty code to break dependencies and getting code into a unit test harness.
After reading this book, you should be convinced of the need for unit testing and TDD.

<img src='https://github.com/betterscientificsoftware/images/raw/master/WorkingEffectivelyWithLegacyCode.jpg' class='logo' />

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication date:  April 11, 2019


<!---
Publish: preview
Categories: Development, Reliability, Skills
Topics: refactoring, design, software engineering, testing, personal productivity and sustainability
Tags: book
Level: 2
Prerequisites: defaults
Aggregate: none
--->
