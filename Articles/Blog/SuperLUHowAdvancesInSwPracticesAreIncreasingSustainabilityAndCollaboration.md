# SuperLU: How Advances in Software Practices are Increasing Sustainability and Collaboration

#### Contributed by [Sherry Li](https://github.com/xiaoyeli "Sherry Li GitHub Profile")

#### Publication date: April 30, 2018

Keeping software updated is a challenge. The SuperLU development team and its users have met that challenge – adding features that improve both the software quality and its usefulness by the scientific community. 

Applications developers have long expressed the need to solve sparse linear systems that arise in areas ranging from science and engineering to economics and ocean modeling. My interest lies mainly in direct solvers for such applications, and in particular [SuperLU](http://crd-legacy.lbl.gov/~xiaoye/SuperLU/ "SuperLU website").

First released in 1999 as a by-product of my thesis work, SuperLU can be considered "legacy code." But SuperLU has not stagnated. Users and developers alike have motivated the need for internal algorithmic advances as well as more "peripheral" development.

For example, early users generally had a single-purpose code requiring solution of a linear system for one application domain, using one library. Increasingly, however, many applications have involved multiphysics and multidisciplinary components, and one code may use multiple libraries for different components of the code. This situation has prompted adoption in SuperLU of modern software methodologies:

* **Proper namespacing**: Allows three versions of the libraries (serial, multithreaded, and distributed) to be used simultaneously and avoid name clashing with other libraries.
* **CMake support**: Migration from manual editing make.inc to CMake/Ctest helps increase build-test productivity and robustness.
  - It is now easier to manage dependencies (ParMetis, machine-dependent files), platform-specific versions (MT, DIST, GPU) and correctness.
  - The code also better accommodates special build requirements (e.g., disabling third-party software).
  - CMake also supports Microsoft Windows builds, which our build system did not.
* **Git**: Conversion from single-developer mode to use of a version control system. The first such tool we used was Subversion (SVN), which was good enough to coordinate code contributions within our development team but proved more difficult when we wanted to incorporate contributions from the user community. Our recent migration from SVN to Git has greatly improved distributed contributions, making the code truly open source.

Migration to CMake and Git have enabled further enhancements, contributed by the broader community.  We are particularly pleased with the recent addition of Windows support for SuperLU. Although such support had been requested for many years, we simply ignored those requests because none of our developers have computing experience with Windows. John Cary, a user from Tech-X is a knowledgeable Windows user. He implemented the needed changes in source code and CMake configuration files and set up the "pull request," which we easily merged into the git repo. This seemingly improbable task was in fact accomplished in just one weekend! 

An automated regression test suite is a crucial task for any major code. We implemented the following testing strategy in SuperLU:
-	Collected small- to medium-sized test matrices with different numerical properties and sparsity structures.
-	Wrote the coverage unit testing code with all possible combinations of input parameters and matrices to invoke all user-callable solver routines. For each test, we check backward and forward error bounds.
-	Set up a nightly regression test harness for Linux desktop and Mac laptop. The nightly test results are displayed on the CDash dashboard using the CMake/CTest facility.
-	Hooked up with Travis CI for continuous integration testing, which is triggered after each commit to the git repo, so any new code can be tested automatically and immediately.
The developers execute the testing code regularly to make sure that newly added features do not introduce errors in the production software.  

But SuperLU users also have a responsibility: they should execute the testing code at the installation stage to make sure the library delivers correct results and performs as intended. Passing the installation test increases user confidence in the software. Moreover, when the user code encounter errors, the testing code of each component can greatly help the user isolate the search space and pinpoint potential source of errors.  

In general, the Git workflow greatly simplifies the source code development and testing cycle, streamlines the process of absorbing users input of bug fixes as well as new features, and dramatically increases the overall productivity in both development and maintenance.

Moreover, the combined use of SuperLU with complementary numerical libraries has been greatly simplified by its inclusion in the initial release of the [xSDK](https://xsdk.info) (Extreme-scale Scientific Software Development Kit), a community effort that seeks to improve functionality, quality, and interoperability among software packages while working toward an extreme-scale scientific software ecosystem. Users can simply download and install a variety of xSDK packages, without worrying about handling software idiosyncrasies. The xSDK community are working to “identify, adapt, and adopt software engineering methodologies and use of best practices” in the context of the [Scientific Libraries Community](https://bssw.io/communities/scientific-libraries-community)---an important element of work on Better Scientific Software.


<!---
Publish: Yes
Categories: development, reliability
Topics: revision control, configuration and builds, testing, continuous integration testing
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
