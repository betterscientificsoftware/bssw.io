# Coding Conventions

<!--deck text start-->
Coding conventions (or coding standards) are critical for fostering shared ownership of the codebase, improving peer reviews, and enhancing several other aspects of internal software quality.
Selecting, documenting, and enforcing coding conventions are an important part of professional, productive, and healthy software projects.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication date: September ???, 2021

Resource information | Details
:--- | :---
Wikipedia article | [Coding Conventions](https://en.wikipedia.org/wiki/Coding_conventions)
Book | [Code Complete: 2nd Edition](https://bssw.io/items/code-complete-a-practical-handbook-of-software-construction)
Book | [Clean Code: A Handbook of Agile Software Craftsmanship, Robert Martin, 2009](https://dl.acm.org/doi/10.5555/1388398)
CII Best Practices | [FLOSS Best Practices Criteria (All Levels)](https://bestpractices.coreinfrastructure.org/en/criteria)

While there are a wide variety of "best practices" that can be adopted when developing a software project, an important subset include *coding conventions* which covers the internal source code in ways that generally does **not** influence code behavior.
Coding conventions, also know as *coding standards*, generally falls into the following categories:

* **Formatting guidelines**: Guidelines for the layout, formatting, and usage of whitespace of the source code and how it is organized in and between source files and directories
* **Naming guidelines**: Guidelines for how variables, functions, and other code entities are named
* **Other general coding guidelines**: Other paradigm- and language-agnostic guidelines 
* **Paradigm- and language-specific guidelines**: Other guidelines that more specific for a given programming paradigm or programming language and may not be universally applicable

*Formatting guidelines*, include how functions and control structures are laid out and formatted, how may spaces are used for indentation (2-to-4 spaces is typical), how many horizontal and vertical spaces are used between different constructs, etc.
Formatting guidelines are the easiest to check for and to provide automated tools to enforce and even auto-reformat source code to the chosen conventions.
*Naming guidelines* influence how source files, variables, functions, and other internal software entities are named.
Some of these naming conventions many be language specific (because some constructs are unique to some languages) but many constructs like variables and functions are universal across almost all languages (and therefore guidelines like using a noun for a variable or class and using a verb for a function or method universally apply).
After formatting and naming guidelines, there are many *other general guidelines* that are fairly universal to all programming paradigms and languages such as for good code comments, elimination of duplication (i.e. Don't repeat yourself), and KISS (keep it simple, stupid).
Lastly, many other types of conventions/guidelines/standards fall that under "coding conventions" are more *paradigm- and language-specific guidelines* such as object-oriented design principles and language-specific guidelines like for C++, Perl, Java, etc.

Having a project, organization, or even an entire company adopt consistent coding conventions is useful to:

* increase productivity in the initial development (by removing arbitrary choices and focusing effort on essentials),
* foster shared ownership of the codebase (by using a coding style that everyone is familiar with and comfortable with using),
* streamline and improve peer code reviews (by avoiding wasted time arguing about arbitrary choices and allowing tools to catch violations of the coding conventions before the reviewer does the real review),
* improve the understandably and maintainability of the codebase (by using a coding style that is very familiar and in a style consistent with what the reader would use), and
* provide targets for refactorings (by helping to highlight code smells).

There are some excellent, widely accepted, and largely language-agnostic, code formatting and naming guidelines given in Chapter 31 "Layout and Style" of "Code Complete: 2nd Edition" by Steve McConnell and in Chapters 1 through 5 of the book "Clean Code" by Robert Martin.
Other chapters in "Code Complete: 2nd Edition" and "Clean Code" also cover many of the other general coding guidelines that are applicable to almost every programming language.
These two authors are some of the most respected in the software industry and their guidance has held up over time and they give very consistent advice in this area.
(Note, one should look for more recent references for language-specific guidelines instead of those given in "Code Complete: 2nd Edition".)
These guidelines apply to every procedural programming language (or the parts of program that are programmed using procedural approaches) and therefore apply to object-oriented programs as well.
Other options exist in the software development community but the views expressed by these two authors seem to be fairly widely accepted.
(Likewise, general coding guidelines that are dramatically opposed to those provided in these references should be viewed with some caution.)

Coding conventions are recognized to be of such importance to the open-source community that the Linux Foundation's CII Best Practices Program's Silver Badge Level **requires** a project adopt coding standards <sup>[[coding_standards]](https://bestpractices.coreinfrastructure.org/en/criteria#1.coding_standards)</sup> and enforce them with automated tools  when possible. <sup>[[coding_standards_enforced]](https://bestpractices.coreinfrastructure.org/en/criteria#1.coding_standards_enforced)</sup>

The different categories of conventions have different consequences, are often handled differently, and are more or less amiable to automated tools.
For example, by definition, the formatting of source code and the naming of internal entities do not change the meaning of the program at all.
In fact, changing in formatting and internal naming conventions may not change the linked optimized binaries at all for compiled languages like C++.
Alternatively formatting and naming conventions are very different when it comes to automated checks and enforcement.
For instance, automated source-code formatting and indentation tools for popular languages like [clang-format](https://clang.llvm.org/docs/ClangFormat.html) can automatically reformat source files according to a chosen language-specific formatting convention and can be used in development and automated checking workflows.
(That is, clang-format can be run as part of a pull-request (PR) check to ensure that proposed code matches the project's published code formatting conventions and removes the need for the PR reviewer  to have to bother with that aspect of the review.)
Also, many language-specific coding standards can be enforced using automated tools such as using [clang-tidy](https://clang.llvm.org/extra/clang-tidy/).
However, it is much harder to write a tool to automatically check and enforce naming conventions or enforce other general guidelines like KISS for internal software constructs.
(In fact, as major part of a peer code review is to use expert human judgment is to evaluate code against naming and other general coding guidelines that would be very hard to write an automated tool to check and would require very sophisticated AI-based implementations.)

While coding conventions for formatting, naming and other general guidelines may not impact the behavior of the software at all, they can have a dramatic influence on the readability and maintainability of the code, especially for expert programmers.
In "Code Complete: 2nd Edition", McConnell cites a study and notes:

> "The importance to comprehension and memory of structuring one’s environment in a familiar way
has lead some researchers to hypothesize that layout might harm an expert’s ability to read a program
if the layout is different from the scheme the expert uses (Shell 1981, Soloway and Ehrlich 1984)"
[7, Section 31.1]. This implies that working with an unfamiliar style might handicap expert coders
more than beginner and intermediate coders.

Many respected voices in the agile software development community suggest that:

* Except for some extremes, many coding conventions cannot be shown to be better or worse than others (and are therefore matter personal preference and are therefore arbitrary).
* However, a software development project, team, or organization should adopt an appropriate set of coding conventions (and provide tiered guidelines with required and suggested items).
* Exceptions to even required conventions should be allowed (with explanations) and tools (if they exist and are in use) should support such exceptions. 
* Everyone must use the currently accepted coding convention for a given project.
* However, anyone should be able to suggest an improvement to the current coding conventions and there should be a process to process and adopt such improvements if warranted.

Note that the Wikipedia site *Coding conventions* does not even mention the Fortran programming language at all but a simple web search for "fortran coding conventions" and "fortran coding standards" will yield a number of hits for different groups and organizations proving their opinions.
However, many of the basic formatting, naming and other general coding guidelines described in "Code Complete: 2nd Edition" and "Clean Code" apply equally well to every Fortran standard from Fortran 77 through Fortran 2018.
(The reader will need to discern what guidelines are clearly not applicable to Fortran since these books tend to be biased towards more popular languages like C++ and Java and therefore should look to some of these more Fortran-specific sites for advice.)

<!---
Publish: yes
Pinned: no
Topics: Software engineering, refactoring, design
RSS update: 2021-09-???
--->
