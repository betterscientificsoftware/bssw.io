# Working Effectively with Legacy Code
<!--deck text start-->
Legacy code can be challenging to use and extend. The book *Working Effectively with Legacy Code*, written by *Michael Feathers*, talks about legacy code and how to work effectively with it.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication date: June 5, 2019


Resource information | Details
:--- | :---
Book title  | [Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052)
Authors | Michael Feathers
Publication | 2005, ISBN-13: 978-0131177055

Legacy software is very hard to modify and extend, as it often relies on obsolete software and hardware, lacks testing, and may have no developers familiar with its complexities.
This book gives us hope that we can use targeted, incremental unit testing and refactoring to turn legacy software into better tested, understood, and extensible software while implementing and
delivering new functionality at the same time.

If you've read *Refactoring*<sup>[1]</sup> and felt a little uneasy about how this would apply to large, nasty software projects, then *Working Effectively with Legacy Code*<sup>[2]</sup> is the book to read.
Feathers mentions and reviews many of the object-oriented principles in *Agile Software Development*<sup>[3]</sup> as well as other bits of information in other great books about software development.
*Working Effectively with Legacy Code* is the logical culmination of  *Refactoring* and *Test Driven Development*<sup>[4]</sup> (TDD); it's where the rubber meets the road when combining unit testing and refactoring.

The definition of "Legacy Code" given in this book is simple but often shocking to the uninitiated:

> Legacy Code == Code Without Tests

Feathers states:

> Code without tests is bad code. It does not matter how well written it is; it doesn't matter how pretty or object-oriented or well-encapsulated it is. With tests, we can change the behavior of our code quickly and verifiably. Without them, we really don’t know if our code is getting better or worse.

He lists four reasons to change software:

* Adding a feature
* Fixing a bug
* Improving the design (i.e., refactoring)
* Optimizing resource usage

He argues that no matter what change is made to the code, we must always maintain other behavior that we do not intend to change. He states:

> Behavior is the most important thing about software. It is what users depend on. Users like it when we add behavior (provided it is what they really wanted), but if we change or remove behavior they depend on (introduce bugs), they stop trusting us.

The main contribution of this book is the *Legacy Code Change Algorithm*:

1. **Identify the targeted legacy code:**
   * **Identify change points** for the target change or new code addition.
   * **Find test points** where the behavior of the code can be sensed.
2. **Get targeted legacy code into test harness and cover with tests:**
   * **Break dependencies** (very carefully and often without sufficient tests) and get the targeted legacy code into a test harness.
   * **Cover targeted legacy code** with (characterization) unit tests.
3. **Add new functionality with new tests** (usually following the Test Driven Development (TDD) process).
4. **Refactor** tested code to remove duplication, clean up, etc.

Step 1 defines the targeted subset of legacy code that must have tests, which depend on what needs to change, what can be sensed, and where dependencies can be broken.
After unit tests that cover the targeted code have been implemented in Step 2, the code should have close to 100% test coverage.
Without full coverage, it is difficult to know if existing behavior is preserved.
Any refactoring in Step 4 is safe to perform once the targeted code is sufficiently covered with tests.
Refactoring is critical to improve the clarity and maintainability of the code.
**WARNING:** The refactoring must not extend outside code that is sufficiently covered by tests!

The most challenging part of the *Legacy Software Change Algorithm* is getting the targeted legacy code into a unit test harness and covering it with tests, which (in more detail) includes these steps:

* **Identify change points**: Find out where in the legacy code you want to make a change or add new code.
Targeted changes should be done in small iterations, so this should hopefully just be a single function or a few functions and hopefully only a single class if possible.

* **Find test points**: Find out where in the code you can sense variables, or call functions, etc. such that you can detect the behavior of the code you want to change.
You may need to add "sensing" variables to help see what you need to see in a unit test.

* **Break dependencies**: Dependencies need to be broken for one of two reasons: Sensing and Separation.
With **Sensing**, we must be able to inspect the behavior of the code that we can’t otherwise see, while **Separation** is needed to allow the code to be run in a test harness outside of the production setting.
Actually breaking the dependencies involves applying minimal refactorings with careful hyper-sensitive editing.
(There are special dependency-breaking refactorings defined in this book to help with this critical task.)

* **Cover legacy code with unit tests**: If you have the specification for how the targeted legacy code is supposed to work, then write tests to that specification.
Otherwise, write "Characterization Tests" to see what the code actually does under different input scenarios.
NOTE: When the official specification differs from the actual observed behavior of the code, go with the actual behavior because that is what users actually depend on.
(Differences between specified/desired behavior and actual behavior can be addressed in later iterations if one desires breaking backward compatibility.)

Finally, another major contribution of this book is in detailing the strategies that can be used in the various steps of the Legacy Code Change Algorithm, which include:

* **Faking Collaborators:**  Needed to get targeted code into a unit test harness and drive unit tests.:
  * **Fake Objects**: Impersonate a collaborator to allow sensing and control.
  * **Mock Objects**: Extend Fake Objects that asserts expected behavior.
* **Seams**: Ways of inserting test-related code:
  * **Preprocessing Seams**: Preprocessor macros to replace functions, replace header files, etc.
  * **Link Seams**: Replace implementation functions (program or system) to define behavior or sense changes.
  * **Object Seams**: Define interfaces and replace production objects with mock or fake objects in a test harness. (NOTE: Prefer object seams to link or preprocessing seams!)

The Legacy Code Change Algorithm is applied in many small iterations over and over again as pieces of the legacy software are changed.
Over time, these small incremental refactorings can result in significant improvements to the quality and sustainability of the software and can even perform major (beneficial) architectural changes.
In fact, at some point, the software may have improved to the point where there is enough strong testing that it is no longer considered legacy code!

This book is packed with practical examples that show nearly every trick there is for refactoring nasty code to break dependencies and getting code into a unit test harness.
After reading this book, you should be convinced of the need for unit testing and TDD.

<img src='https://github.com/betterscientificsoftware/images/raw/master/WorkingEffectivelyWithLegacyCode.jpg' class='logo' />

<br>

[1]: #ref1 "Fowler, Martin. Refactoring, Addison Wesley, 1999"
[2]: #ref2 "Feathers, Micheal C. Working Effectively with Legacy Code.  Prentice Hall, 2004"
[3]: #ref3 "Martin, Robert C. Agile Software Development (Principles, Patterns, and Practices). Prentice Hall, 2003"
[4]: #ref4 "Beck, Kent. Test Driven Development: By Example. Addison Wesley, 2003"

<br>


References | &nbsp;
:--- | :---
<a name="ref1"></a>1 | [Fowler, Martin. Refactoring, Addison Wesley, 1999](https://martinfowler.com/books/refactoring.html)
<a name="ref2"></a>2 | [Feathers, Michael C. Working Effectively with Legacy Code.  Prentice Hall, 2004, ISBN: 0131177052](https://www.oreilly.com/library/view/working-effectively-with/0131177052/)
<a name="ref3"></a>3 | [Martin, Robert C. Agile Software Development (Principles, Patterns, and Practices). Prentice Hall, 2003](https://www.pearson.com/us/higher-education/program/Martin-Agile-Software-Development-Principles-Patterns-and-Practices/PGM272869.html)
<a name="ref4"></a>4 | [Beck, Kent. Test Driven Development: By Example. Addison Wesley, 2003](https://www.pearson.com/us/higher-education/program/Beck-Test-Driven-Development-By-Example/PGM206172.html)

<br>


<!---
Publish: yes
RSS update: 2019-06-05
Categories: Development, Planning, Reliability
Topics: refactoring, design, testing
Tags: book
Level: 2
Prerequisites: defaults
Aggregate: none
--->

