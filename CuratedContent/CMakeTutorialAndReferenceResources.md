# CMake Tutorial and Reference Resources

<!--deck text start-->
The CMake meta-build system is a large and powerful set of tools to create cross-platform builds from source for C, C++, Fortran and many other compiled programming languages.
CMake continues to rapidly evolve and best practices in its use are changing almost as rapidly.
Here we provide links and descriptions for the best tutorial and reference materials that exist for CMake to help stay on the forefront of effective CMake usage.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)
#### Publication date: ???

Resource information | Details 
:--- | :--- 
Book title | [Professional CMake](https://crascit.com/professional-cmake/)
Authors | Craig Scott
Publication | Self published, new editions put out after each new CMake release
Web links | https://crascit.com/professional-cmake/

Resource information | Details 
:--- | :--- 
Web Page | [CMake Reference Documentation](https://cmake.org/cmake/help/latest/)
Authors | Kitware Staff
Web links | https://cmake.org/cmake/help/latest/ (and drop-down section of all CMake versions)

Resource information | Details 
:--- | :--- 
Book title | [Mastering CMake](https://crascit.com/professional-cmake/)
Authors | Kitware Staff
Publication | Year 2022, Self published, currently not versioned
Web links | https://crascit.com/professional-cmake/

The CMake meta-build tool and ecosystem (which includes the tools CTest and CPack with each CMake installation) continues to evolve and improve fairly rapidly from release to release.
Kitware (the company that owns the primary CMake repository and provides the official releases of CMake) puts out three major releases of CMake each year (or about every four months).
The best practices for using CMake evolve as new versions of CMake are released.
(For example, at the time of this writing, CMake support for a feature called Generator Expressions is still rapidly evolving and can have a dramatic impact on the best way to write CMakeList.txt files.)
Therefore, unlike other programming tools, trying to use web searches to find solutions for CMake can be ineffective; because even advice from just a year ago on Stack Overflow or Stack Exchange can be outdated.
Therefore, this page gives advice based on 13+ years of CMake usage and hundreds of hours of searching for and reading CMake documentation, especially in the years 2021-2022.

<img src='../images/ProfessionalCMake.jpg' class='page'/>

Arguably, the best resource for finding up-to-date guidance on how to use CMake is the most recent edition of the book ***Professional CMake*** (the 11th edition covering CMake versions up to 3.22 as of this writing).
The 560+ page 11th edition of the book contains excellent tutorial material for CMake and yet goes into deep concepts in the CMake language where needed (such as the gotchas and workarounds for dealing with lists and function/macro arguments with data containing quotes `"`, spaces ` ` and semi-colons `;` which is one of the most confusing aspects to using CMake).
This book covers every basic CMake feature in great detail.
It explains modern CMake idioms and best practices.
Also, it covers older CMake commands and idioms to avoid and why.
This book seems to answer the "why" and big picture questions for CMake in a way that no other material has matched.
It also provides really critical low-level details and tips that are absent in even the official CMake reference documentation.
This book is self published by the author in a downloadable PDF format with new editions coming out after each new CMake release (i.e. three new editions each year).
The current edition of the book costs $30 which includes 9 updates for new editions of the book as they come out.
(Therefore, $30 would cover every new edition over a 3 year period which includes 9 new CMake releases or 6 years if only downloading every other updated edition across 18 CMake releases.)
The author is not currently a Kitware employee but is a significant contributor to CMake and collaborates closely with Kitware staff.
The author starts evaluating and updating the book at the beginning of each new CMake release cycle (i.e. right after the first release candidate `vX.Y.0-rc1` is tagged).
Through this process, the author often provides feedback to Kitware and help addressing issues with new CMake features and changes to existing CMake functionality which feeds back into bug fixes and better CMake reference and release notes documentation.

Another important source of CMake documentation is Kitware's official online ***CMake Reference Documentation***.
This documentation is produced and versioned for every CMake release and contains a wealth of information including:

* Reference material for the entire CMake language including for every supported command, property, variable and related topic
* Documentation for the large collection of standard `*.cmake` modules that are installed along with CMake
* Targeted guides including:
  * CMake Tutorial (for developers contributing to projects that use CMake)
  * User interaction Guide (for users trying to configure, build, install and test projects that use CMake)
* Release notes for each version of CMake
* Command-line documentation for the `cmake`, `ctest`, and `cpack` executables

As a developer contributing to a project using CMake (i.e. editing the project's `CMakeLists.txt` files), when consulting the official reference documentation, it is advisable to only view documentation for the minimum version of CMake supported by the project (i.e. for the version `X.Y` listed in the project's top-level `CMakeLists.txt` file calling `cmake_minimum_required(VERSION X.Y)`).
For example, if minimum version was 3.17, then one would select that version in the drop-down box (taking you to https://cmake.org/cmake/help/v3.17/).  This helps to avoid accidentally using CMake features not present in the minimum CMake version supported by the project.

If one does not want to spend the $30 for the book "Professional CMake", then one may consider Kitware's ***Mastering CMake*** book.
This is an updated, free online version of Kitware's classic "Mastering CMake" paperback book that used to be sold, (last updated for [CMake 3.1 published in 2015](https://www.amazon.com/Mastering-CMake-Ken-Martin/dp/1930934319)).
It also contains tutorial coverage of key CMake concepts and other basic tutorial content (but usually at a less complete and detailed level compared to "Professional CMake").
Note that the "guides" provided in the online CMake Reference Documentation are also exactly duplicated in the online "Mastering CMake" book.

Finally, if one searches the above mentioned documentation sources "Professional CMake", the online CMake Reference Documentation, and "Mastering CMake" and does not find the answer, then one can turn to web searches.
Just note that, as warned above, the answers found may be outdated (even from a few years ago).
But if one cannot find the answer any other way (short of asking the CMake maintainers themselves) these web searches can be helpful to learn how to address issues with CMake.

<!---
Publish: yes 
Pinned: no
RSS update: ???
Topics: configuration and builds, release and deployment, development tools, testing, online learning
--->

<!---
LocalWords:  
--->
