## C++ Core Guidelines

<!-- deck text start -->
The C++ Core Guidelines website is a living online, community-developed document that contains up-to-date idioms and advice from C++ community thought leaders that is continuously updated as new C++ standards come out and better approaches are discovered for creating fast, robust, safe, interoperable, and sustainable C++ software.
<!-- deck text end -->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe "Roscoe A. Bartlett")
#### Publication date: August ???, 2024

Resource information | Details
:--- | :---
Resource name | C++ Core Guidelines
Website | https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines
Editors | Bjarne Stroustrup and Herb Sutter
Version | July 2, 2024 (Git commit 50afe0234ce4f2f6bde7d9b0d86e926bd479f9aa)
Focus | Language idioms and guidelines


### Background

C++ was originally created by Bjarne Stroustrup in 1979 while he was at Bell Labs as "C with Objects" (which was just a set of macros that generated C code before being compiled by a C compiler) with the first public version of Bell Labs Cfront C++ released in 1985.
C++ was originally designed and built on top of C and designed to interoperate with C at a fundamental level.
(This legacy with C has been one of C++'s greatest strengthens and one of its greatest weaknesses.)
In the years since then, C++ has undergone several ISO standards updates and is currently developing an updated ISO (International Standards Organization) C++ standard every three years, starting with ISO C++11 (where C++23 is the most recent approved standard at the time of this writing).
Over the last 40 years, billions of lines of C++ code have been written and deployed with varying degrees of quality, safety, robustness and sustainability.
The way that C++ has evolved over the last 40+ years from a thin layer on top of C (together with the need for backward compatibility supporting billions of lines of previously written C++ code), has given rise to a huge and complex language and standard library.
When used in raw form by undisciplined developers, C++ has been used to arguably create some of the most confusing, fragile, unsafe, and unsecure software in existence (riving C in this respect).
However, dispite this, C++ has seen a resurgence in popularity and usage in recent years with C++ being the fastest growing language in 2022 and overtaking C to become the second most popular language (behind Python) in June 2024.<sup>[9],[10]</sup>

Over the years as C++ as evolved, numerous authors have written numerous books on how to successfully use the C++ programming language to create quality C++ software.<sup>[2]</sup>
However, with each new C++ standard (which includes new language features and library extensions) and with updated experience and new idioms, much of the guidance in these prior books become obsolete (and even counter-productive) as time passes.
While some authors have put out updated versions of their books to compensate for new C++ standards and idioms (e.g., Scott Meyer's popular Effective C++ book<sup>[4],[6],[7]</sup> and other Effective C++ books<sup>[5],[8]</sup>), this is unsustainable and leaves a hole in guidance for the most effectively usage of modern C++ (as it evolves).


### Overview of the C++ Core Guidelines

Would it not be nice if there was a way to take the best advice and idioms all of the excellent books that have been written by the thought leaders in the C++ community and update and combine them with modern language features, libraries, and idioms?
And what if these could be kept up-to-date as new C++ standards come out and the C++ community responds to the shifting needs of the software development community?
That is exactly what the **C++ Core Guidelines** website seeks to do.
Bjarne Stroustrup and Herb Sutter are the primary editors of the C++ Core Guidelines site and the content has been contributed by at least 330+ other C++ authors and developers.

The site is currently organized as a single `github.io` page with that is broken up into major sections covering a number of areas including:

* **In**: Introduction
* **P**: Philosophy
* **I**: Interfaces
* **F**: Functions
* **C**: Classes and class hierarchies
* **Enum**: Enumerations
* **R**: Resource management
* **ES**: Expressions and statements
* **Per**: Performance
* **CP**: Concurrency and parallelism
* **E**: Error handling
* **Con**: Constants and immutability
* **T**: Templates and generic programming
* **CPL**: C-style programming
* **SF**: Source files
* **SL**: The Standard Library

with additional supporting sections and material.

These guidelines are based only on the standard C++ language and standard C++ library, with the addition of a small and simple "GSL: Guildelines support library".<sup>[3]</sup>
(The latter is needed to codify important idioms that are not directly supported by the C++ standard library.
The GSL does not represent a significant pieces of software from a function perspective.)

A major motivation and focus of the C++ Core Guidelines is the creation of safe and secure C++ software.
In fact, the main page contains some form of the words "safe", "check", "bounds" (i.e., "bounds check"), and "secure" over 600 times!

<!--- safe=182, safety=75, safely=15, unsafe=10, check=199, checked=47, unchecked=5, bounds=65, secure=1, security =16, --->


### Some Important Details

When converted to a single PDF file, the main C++ Core Guidelines page<sup>[1]</sup> is currently an 869 page book.
(Therefore, this would represent the largest book ever written on C++ coding guidelines.)
In addition, some of the material is not yet filled in and there are placeholders denoted by `???` (currently 270 of these).
(So there is still a number of issues yet to be addressed.)

As a github.io site, it is generated from a set of Markdown files maintained in a collaborative GitHub repository.
That GitHub repository currently has 1963 watchers, 5.5k forks, 42k stars, and over 330 contributors.
Therefore, this is significant effort to define guidelines and best practices for modern C++.

Many of the C++ Core Guidelines have LLVM Clang-Tidy checks that can be turned on to ensure that C++ software follows them.
(At the time of this writing, there are 30 of the `cppcoreguidelines-*` clang tidy checks of which eight can be automatically fixed using an auto-refactoring.<sup>[11]</sup>
Therefore, most of the C++ Core Guidelines are not checked and/or cannot be easily checked or enforced by a static analysis tool.)
The Microsoft C++ compiler also has support for enforcing many


### Summary

The C++ Core Guidelines site represents a major step forward in the development, dissemination, and enforcement (through tools like Clang-Tidy) of idioms and best practices for developing quality sustainable C++ software.
While there is more work to be done in expanding the coverage of these guidelines and tweaking the existing guidelines (and you can help with that effort by submitting issues and pull requests to the `CppCoreGuidelines` GitHub project), the greatest challenge will be on refactoring the large amount of legacy C++ software that does not follow these guidelines.
For that, the C++ community will need to continue to develop and improve C++ static analysis and refactoring tools.


<!---
Publish: yes
Topics: ???
Pinned: no
RSS update: ???
--->


<!--- ToDo:

* Edit using grammarly.com ...

--->


<!--- Original References --->

[CppCoreGuidelines-sfer-ezikiw]: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines "C++ Core Guildelines: github.io site"

[CppCodingGuidelinesBooks-sfer-ezikiw]: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rfbooks-books-with-coding-guidelines "C++ Coding Guidelines Books"

[CppCoreGuidelinesSupportLibrary-sfer-ezikiw]: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#gsl-guidelines-support-library "GSL: Guidelines support library"

[Meyers92-sfer-ezikiw]: https://www.amazon.com/Effective-Specific-Improve-Programs-Designs/dp/0201563649 "Effective C++, First Edition {Scott Meyers. Addison-Wesley 1992}"

[Meyers96-sfer-ezikiw]: https://www.amazon.com/More-Effective-Improve-Programs-Designs/dp/020163371X "More Effective C++ {Scott Meyers. Addison-Wesley, 1996}"

[Meyers97-sfer-ezikiw]: https://www.amazon.com/Effective-Specific-Addison-Wesley-Professional-Computing/dp/0201924889 "Effective C++, Second Edition {Scott Meyers. Addison-Wesley, 1997}"

[Meyers05-sfer-ezikiw]: https://www.amazon.com/Effective-Specific-Improve-Programs-Designs/dp/0321334876 "Effective C++, Third Edition {Scott Meyers. Addison-Wesley, 2005}"

[Meyers15-sfer-ezikiw]: https://www.amazon.com/Effective-Modern-Specific-Ways-Improve/dp/1491903996 "Effective Modern C++ {Scott Meyers. O'Reilly. 2015}"

[TiobeIndexCxxSecond_2024-06-sfer-ezikiw]: https://www.techrepublic.com/article/tiobe-index-june-2024 "TIOBE Programming Language Index News (June 2024): C++ Rises to Second Place {Megan Crouse, TechRepublic, June 11, 2024}"

[TiobeIndex-sfer-ezikiw]: https://www.tiobe.com/tiobe-index/ "Tiobe Programming Language Index"

[ExtraClangTidyChecks-sfer-ezikiw]: https://clang.llvm.org/extra/clang-tidy/checks/list.html "Extra Clang Tidy Checks"

<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "C++ Core Guildelines: github.io site"
[2]: #sfer-ezikiw-2 "C++ Coding Guidelines Books"
[3]: #sfer-ezikiw-3 "GSL: Guidelines support library"
[4]: #sfer-ezikiw-4 "Effective C++, First Edition"
[5]: #sfer-ezikiw-5 "More Effective C++"
[6]: #sfer-ezikiw-6 "Effective C++, Second Edition"
[7]: #sfer-ezikiw-7 "Effective C++, Third Edition"
[8]: #sfer-ezikiw-8 "Effective Modern C++"
[9]: #sfer-ezikiw-9 "TIOBE Programming Language Index News (June 2024): C++ Rises to Second Place"
[10]: #sfer-ezikiw-10 "Tiobe Programming Language Index"
[11]: #sfer-ezikiw-11 "Extra Clang Tidy Checks"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[C++ Core Guildelines: github.io site](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[C++ Coding Guidelines Books](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rfbooks-books-with-coding-guidelines)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[GSL: Guidelines support library".](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#gsl-guidelines-support-library)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[Effective C++, First Edition<br>Scott Meyers. Addison-Wesley 1992](https://www.amazon.com/Effective-Specific-Improve-Programs-Designs/dp/0201563649)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[More Effective C++<br>Scott Meyers. Addison-Wesley, 1996](https://www.amazon.com/More-Effective-Improve-Programs-Designs/dp/020163371X)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[Effective C++, Second Edition<br>Scott Meyers. Addison-Wesley, 1997](https://www.amazon.com/Effective-Specific-Addison-Wesley-Professional-Computing/dp/0201924889)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[Effective C++, Third Edition<br>Scott Meyers. Addison-Wesley, 2005](https://www.amazon.com/Effective-Specific-Improve-Programs-Designs/dp/0321334876)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[Effective Modern C++<br>Scott Meyers. O'Reilly. 2015](https://www.amazon.com/Effective-Modern-Specific-Ways-Improve/dp/1491903996)
* <a name="sfer-ezikiw-9"></a><sup>9</sup>[TIOBE Programming Language Index News (June 2024): C++ Rises to Second Place<br>Megan Crouse, TechRepublic, June 11, 2024](https://www.techrepublic.com/article/tiobe-index-june-2024)
* <a name="sfer-ezikiw-10"></a><sup>10</sup>[Tiobe Programming Language Index](https://www.tiobe.com/tiobe-index/)
* <a name="sfer-ezikiw-11"></a><sup>11</sup>[Extra Clang Tidy Checks](https://clang.llvm.org/extra/clang-tidy/checks/list.html)
