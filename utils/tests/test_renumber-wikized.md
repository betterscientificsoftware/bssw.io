# Coding Conventions

<!--deck text start-->
Coding conventions are critical for fostering shared ownership of the codebase, improving peer reviews, and enhancing several other aspects of internal software quality.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication date: October ???, 2021

While there are a wide variety of "best practices" that can be adopted when developing a software project, an important subset include *coding conventions* which impact the internal source code in ways that generally do **not** influence the behavior of the software. Selecting, documenting, and implementing coding conventions are an important part of professional, productive, and healthy software projects.

Coding conventions<sup>[5]</sup>, also know as *coding standards* or *coding guidelines*, generally falls into the following categories:

* **Formatting guidelines**: Guidelines for the layout and usage of whitespace in the source code and how source code is organized in and between source files and directories
* **Naming guidelines**: Guidelines for how variables, functions, and other code entities are named
* **Other general coding guidelines**: Other paradigm- and language-agnostic guidelines 
* **Paradigm- and language-specific guidelines**: Other guidelines that are more specific to a given programming paradigm or programming language

*Formatting guidelines*, include how functions and control structures are laid out and formatted, how many spaces are used for indentation (2-to-4 spaces is typical), how many horizontal and vertical spaces are used between different constructs, etc.
Formatting guidelines are the easiest to check for and to provide automated tools to enforce and even auto-reformat source code to the chosen conventions.
*Naming guidelines* influence how source files, variables, functions, and other internal software entities are named.
Some of these naming conventions may be language specific (because some constructs are unique to some languages) but many constructs like variables and functions are universal across almost all languages (and therefore guidelines like using a noun for a variable or class and using a verb for a function or method universally apply).
After formatting and naming guidelines, there are many *other general guidelines* that are fairly universal to all programming paradigms and languages such as writing comments, elimination of duplication (i.e. don't repeat yourself), and KISS (keep it simple, stupid).
Lastly, many other types of conventions/guidelines/standards fall that under "coding conventions" are more *paradigm- and/or language-specific guidelines* such as object-oriented design principles and language-specific guidelines for C++, Perl, Java, etc.

While coding conventions for formatting, naming and other general guidelines may not impact the behavior of the software at all, they can have a dramatic influence on the readability and maintainability of the code, especially for expert programmers.
In *Code Complete: 2nd Edition*<sup>[6]</sup>, McConnell cites a study and notes:

> "The importance to comprehension and memory of structuring one’s environment in a familiar way
has led some researchers to hypothesize that layout might harm an expert’s ability to read a program
if the layout is different from the scheme the expert uses (Shell 1981, Soloway and Ehrlich 1984)"
[7, Section 31.1]. This implies that working with an unfamiliar style might handicap expert coders
more than beginner and intermediate coders.

Having a project, organization, or even an entire company adopt consistent coding conventions is useful to:

* **increase productivity in the initial development** (by removing arbitrary choices and focusing effort on essentials),
* **foster shared ownership of the codebase** (by using the same style one can't tell who wrote the code initially and therefore it does not imply ownership),
* **streamline and improve peer code reviews** (by avoiding wasted time arguing about arbitrary choices and allowing tools to catch violations of the coding conventions so the reviewer does not need to bother with them),
* **improve the understandably and maintainability of the codebase** (by using a coding style that is very familiar and consistent), and
* **provide targets for refactorings** (by helping to highlight code problems that violate the accepted conventions).

There are some excellent, widely accepted, and largely language-agnostic, code formatting and naming guidelines given in Chapter 31 "Layout and Style" of the book *Code Complete: 2nd Edition* by Steve McConnell and in Chapters 1 through 5 of the book *Clean Code*<sup>[7]</sup> by Robert Martin.
Other chapters in *Code Complete: 2nd Edition* and *Clean Code* also cover many of the other general coding guidelines that are applicable to almost every programming language.
These two authors are some of the most respected in the software industry whose guidance has held up over time and they give very consistent advice in this area.
(But not that one should look to more recent references for language-specific guidelines instead of those given in *Code Complete: 2nd Edition*.)
These guidelines apply to every procedural programming language (or the parts of program that are programmed using procedural approaches) and therefore apply to object-oriented programs as well.
Other options exist in the software development community but the views expressed by these two authors seem to be fairly widely accepted.

The different categories of conventions have different consequences, are often handled differently, and are more or less amiable to automated tools.
For example, by definition, the formatting of source code and the naming of internal entities does not change the meaning of the program at all.
In fact, changes in formatting and internal naming conventions may not change the linked optimized binaries at all for compiled languages like C++.
Alternatively, formatting and naming conventions are very different when it comes to automated checks and enforcement.
For instance, automated source-code formatting and indentation tools for popular languages like `clang-format`<sup>[9]</sup> can automatically reformat source files according to a chosen language-specific formatting convention and can be used in development and automated checking workflows.
(That is, clang-format can be run as part of a pull-request (PR) check to ensure that proposed code matches the project's published code formatting conventions and removes the need for the PR reviewer  to have to bother with that aspect of the review.)
Also, many language-specific coding standards can be enforced using automated tools such as using `clang-tidy`<sup>[10]</sup>.
However, it is much harder to write a tool to automatically check and enforce naming conventions or enforce other general guidelines like KISS for internal software constructs.
(In fact, a major part of peer code review is to use expert judgment to evaluate code against naming and other general coding guidelines that would be very hard to write a robust automated tool to check.)

Coding conventions are recognized to be of such importance to the open-source community that the Linux Foundation's CII Best Practices Program's Silver Badge Level<sup>[8]</sup> **requires** a project to adopt coding standards <sup>[11]</sup> and to enforce them with automated tools when possible <sup>[12]</sup>.

The general consensus in the software engineering community around coding conventions seems to be:

* **In many cases, specific choices of coding conventions** (especially code formatting choices) **cannot be shown to be better or worse than other choices** (i.e. they are matter personal preference and are therefore arbitrary).
* However, **a software development project should still adopt a a set coding conventions even in these areas** (and what is important is that a set of conventions are agreed upon and adopted, not so much the details or the choices that are made).
* **Everyone should adhere to the currently accepted coding conventions** for the project.
* However, (rare) **exceptions to even required conventions should be allowed** (with explanations) and tools to check and enforce the conventions should support such exceptions (if they exist and are in use). 
* Also, **anyone should be able to suggest improvements to the current coding conventions** and there should be a process to make changes to these conventions.

As a postscript, note that the Wikipedia page *Coding conventions* does not even mention the Fortran programming language in the section "Coding conventions for languages" (which only covers about 17 languages at the time of this writing) but a simple web search for "fortran coding conventions" or "fortran coding standards" will yield a number of hits for different groups and organizations providing their opinions.
However, many of the basic formatting, naming and other general coding guidelines described in *Code Complete: 2nd Edition* and *Clean Code* apply equally well to every Fortran standard from Fortran 77 through modern Fortran standards.

[ccw-sfer-ezikiw]: https://en.wikipedia.org/wiki/Coding_conventions "Coding Conventions (Wikipedia)"
[cc2nd04-sfer-ezikiw]: https://bssw.io/items/code-complete-a-practical-handbook-of-software-construction "Code Complete (Second Edition) {McConnell, Steve. Microsoft Press, 2004}"
[cc08-sfer-ezikiw]: https://dl.acm.org/doi/10.5555/1388398 "Clean Code: A Handbook of Agile Software Craftsmanship {Robert C. Martin. Prentice Hall PTR, 2008}"
[ciibpc-sfer-ezikiw]: https://bestpractices.coreinfrastructure.org/en/criteria "CII Best Practices Criteria"
[cf-sfer-ezikiw]: https://clang.llvm.org/docs/ClangFormat.html "clang-format"
[ct-sfer-ezikiw]: https://clang.llvm.org/extra/clang-tidy/ "clang-tidy"
[cs-sfer-ezikiw]: https://bestpractices.coreinfrastructure.org/en/criteria?details=true&rationale=true#1.coding_standards "[coding_standards]"
[cse-sfer-ezikiw]: https://bestpractices.coreinfrastructure.org/en/criteria?details=true&rationale=true#1.coding_standards_enforced "[coding_standards_enforced]"

<!---
Publish: yes
Pinned: no
Topics: Software engineering, refactoring, design
RSS update: 2021-10-???
--->
<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[5]: #sfer-ezikiw-5 "Coding Conventions (Wikipedia)"
[6]: #sfer-ezikiw-6 "Code Complete (Second Edition)"
[7]: #sfer-ezikiw-7 "Clean Code: A Handbook of Agile Software Craftsmanship"
[8]: #sfer-ezikiw-8 "CII Best Practices Criteria"
[9]: #sfer-ezikiw-9 "clang-format"
[10]: #sfer-ezikiw-10 "clang-tidy"
[11]: #sfer-ezikiw-11 "[coding_standards]"
[12]: #sfer-ezikiw-12 "[coding_standards_enforced]"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[Coding Conventions (Wikipedia)](https://en.wikipedia.org/wiki/Coding_conventions)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[Code Complete (Second Edition)<br>McConnell, Steve. Microsoft Press, 2004](https://bssw.io/items/code-complete-a-practical-handbook-of-software-construction)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[Clean Code: A Handbook of Agile Software Craftsmanship<br>Robert C. Martin. Prentice Hall PTR, 2008](https://dl.acm.org/doi/10.5555/1388398)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[CII Best Practices Criteria](https://bestpractices.coreinfrastructure.org/en/criteria)
* <a name="sfer-ezikiw-9"></a><sup>9</sup>[clang-format](https://clang.llvm.org/docs/ClangFormat.html)
* <a name="sfer-ezikiw-10"></a><sup>10</sup>[clang-tidy](https://clang.llvm.org/extra/clang-tidy/)
* <a name="sfer-ezikiw-11"></a><sup>11</sup>[[coding_standards]](https://bestpractices.coreinfrastructure.org/en/criteria?details=true&rationale=true#1.coding_standards)
* <a name="sfer-ezikiw-12"></a><sup>12</sup>[[coding_standards_enforced]](https://bestpractices.coreinfrastructure.org/en/criteria?details=true&rationale=true#1.coding_standards_enforced)
