# Working Effectively with Legacy Code

## Feathers, Michael, 2005, ISBN-13: 978-0131177055

Legacy software is very hard to modify and extend, as it often relies on obsolete software and hardware, lacks testing, and may have no devlopers familiar with its complexities.  This book gives one hope that we can use targeted, incremental unit testing and refactoring to turn legacy software into better tested, understood, and extensible software while implementing and delivering new functionality at the same time.

If one read the book "Refactoring" by Martin Fowler and felt a little uneasy about how this would apply to large nasty software projects, then "Working Effectively with Legacy Code" is the book to read.
What’s more, Michael mentions and reviews many of the object-oriented principles in Agile Software Development as well as other bits of information that one would find in other great books about software development.
One can view this book as the logical culmination of the books "Refactoring" and "Test Driven Development" (TDD); it's where the rubber meets the road combining unit testing and refactoring.

The main contribution of this book is the "Legacy Code Change Algorithm":

1. **Get targeted legacy code into test harness and cover with tests:**
    - **Identify change points** for the target change or new code addition.
    - **Find test points** where the behavior of the code can be sensed.
    - **Break dependencies** (very carefully and often without sufficient tests) and get the targeted legacy code into a test harness.
   - **Cover targeted legacy code** with (characterization) unit tests.
2. **Add new functionality with new tests**, usually following the Test Driven Development (TDD) process.
3. **Refactor** to remove duplication, clean up, etc.

This book is packed with practical examples that show nearly every trick there is for refactoring nasty code to break dependencies and getting code into a unit test harness.  After reading this book, you should be convinced of the need for unit testing and TDD.

<img src='https://github.com/betterscientificsoftware/images/blob/master/WorkingEffectivelyWithLegacyCode.jpg' class='logo' />

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
