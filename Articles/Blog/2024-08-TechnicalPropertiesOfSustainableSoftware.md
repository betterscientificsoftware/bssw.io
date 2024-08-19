# Technical Properties of Sustainable Software

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication date: August ???, 2024

<!-- begin deck -->
While there are many different enablers or obstacles to software sustainability, arguably, some of the most important are related to the technical properties of the software itself, independent of any individual developer, development team, user community, or funding source.
<!-- end deck -->

While some authors have looked at software sustainability from mostly institutional and social perspectives (e.g. "Software sustainability - lessons learned from different disciplines"), here, we consider key technical properties of the software itself that helps to improve sustainability and some development practices that aid in the creation and maintenance of technically sustainable software.

<img src='../../images/2024-08-TechnicalPropertiesOfSustainableSoftware-hero-image.jpg' class='page'/>


### Definitions of Sustainable Software

There are various definitions of "software sustainability" in usage in the software development community.
The Better Scientific Software (BSSw.io) community defines software sustainability as<sup>[bssw-ss]</sup>:

> The ability of software to continue or evolve.
> Considerations are often different when viewed from different perspectives (user, developer, manager, funder), but generally relates to resources to maintain or evolve the code, adaptability of the codebase to new uses and new computational platforms.

and as<sup>[bssw-whatis-ss]</sup>:

> Sustainable software means that an existing product remains viable in the future such that it makes sense to continue using, adapting, and expanding its capabilities instead of replacing it with another new or existing product.

and:

> Sustainability is a measure of the cost to maintain and improve a product over its lifetime.

It is this latter concentration on the "cost to maintain and improve" software over time will be the focus in this article.

With this latter cost/feasibility focus in mind, we define different levels of **Technically Sustainable Software**:

* **Weak Definition of Sustainable Software**: The same team of developers that originally created the software can continue to add new features and fix bugs in the software at a reasonable cost (i.e. where starting from scratch would be more expensive, even in the long term).

* **Medium Definition of Sustainable Software**: New developers can reasonably make contributions to the software but these contributions are integrated back by the original development team.

* **Strong Definition of Sustainable Software**: A different set of developers from the original developers can take over new feature development and bug fixes and the original developers can go away (and the new team can do so cheaper than starting over from scratch).

At the extreme end of the "Strong Definition" is  the **Extreme uses case for Sustainable software**:
Your project uses some external software package X in such a way that it would be very difficult and expensive to rip it out and/or change to use something else.
At some point, the developers of package X go away and no one is left in the development community to help extend or support package X.
What technical properties of package X would make it so that you could continue support (with reasonable cost and risk) your own project's usage of package X which includes activities like adding some new features, porting, and fixing bugs (i.e. that may be exposed by adding new features and porting to new platforms and upgrading upstream dependencies)?

Software that satisfies key technical properties listed below would tend to meet the Strong Definition of Sustainable Software and enable the extreme use case for software sustainability described above.
Such software could be said to be **Self-Sustaining Software** since such software does not need a dedicated team to sustain the software for your (limited) continued usage.


### Key Technical Properties of Sustainable Software

The following technical properties have been widely recognized to lead to software that less expensive to maintain according the above definition(s) of sustainable software.
High quality software that contains all of these properties can be said to be self-sustaining software:

**Open Source License**:
Allow the user to change and use the software in any way that is needed for the success of their projects.
Note, this does not require a fully open-source license in many cases.
It just has to allow your project to change the source and use the software as needed.

**Documented history of development**:
The development history of the software (which can be captured in the version-control history and linked issue trackers) can answer many questions that are important to the future of the software.
What factors caused the software to be in its current state?
What requirements went into the development of the software?  (Might some of those requirements and features no longer be necessary for future versions of the software to allow breaking some backward compatibility?)

**Core domain model distillation document**:
Has a clear documented core domain model (which is represented in the code or a clear documented mapping of the domain model to software) been given?
Need document is needed to constrain the scope of the software and to continue to improve software cohesion and internal consistency with future changes.

* **Portable, well-documented, robust tests that demonstrate and protect the important behaviors of the software**:
These tests should give the key use cases and embody the requirements of the code and not be just simple no-change regression tests<sup>[e2s-book-2016]</sup>
It must be made clear how to run these tests and ensure they pass or fail.
The reason for why a test passes or fails must be obvious from the output of the test without having to open a debugger or add extra print statements.
These tests can take the place of a lot of documentation that one would otherwise need to write and such tests are, in a way, better than more standard documentation since automated tests are always checked after every change where standard documentation cannot.
These tests are needed to safely change or port the software and to understand the intended behavior of the software for future usage or change.

**Clean, logical and understandable code interfaces and implementation**:
Properties of clean code include self-documenting code, other minimal necessary internal and external documentation, elimination of duplication, other well-known design and implementation principles.

**Fast building code and fast running test suite**:
An important aspect of sustainable software that is often overlooked is the computational overhead needed to build the software and the tests and then to run the test suites.
A software package that requires significant computational resources to test the code after any change represents a huge type of technical debt that must be carried around by future maintainers of the package.
Alternatively, software that builds fairly fast and where the tests can be run in a smaller amount of time can take advantage of free cloud continuous testing services.
(At the time of this writing, services like GitHub Actions and GitLab CI provide free cloud computing cycles to test software projects on these platforms with various limits on the computational cost.)
However, software that is very computationally expensive to build and test, or requires special hardware like GPUs, can impose a huge burden on the sustainability of such software in the need to procure, setup, and maintain the needed computing resources.

**Well-defined and well-regulated internal and external dependencies**:
Reuse and sustainability are greatly aided by minimizing external dependencies and having the internal dependencies of the software package itself established using good design and build modularity.
For example, even if your project only depends on small piece of a large software package, if that smaller piece cannot easily be targeted and extracted, then you may be stuck having to configure and build a large amount of software as you port to new platforms.
The less code you have to configure and build, the easier it will be to modify and fix if you have to do so.
(Need this to avoid having to support the build and support lots of code that you don’t need.)

* **All upstream dependencies are also sustainable software**:
If any of the upstream dependencies of a software package are not sustainable software, then the downstream packages cannot be sustainable either.
(That is, a chain is only as strong as its weakest link.)
This recursive requirement only stops at standard tools like standard compilers and other ubiquitous tools and libraries that are guaranteed to be sustained and supported over the long term.
This requirement is also another motivation for minimizing external dependencies.

Therefore, the technical requirements for sustainable software are quite strict and difficult to achieve for many software projects.


### Some key practices for creating and maintaining sustainable software

While this article as been focused on the technical properties of the software itself, there are key practices that can aid in the creation and maintenance of sustainable software.

**Development and Collaboration Workflows practices:**
* For shared development, use a distributed version control tool (e.g. Git) to manage the source and use appropriate development and integration workflows according to well-established idioms appropriate for your project.
* To encourage peer contributions, use an open-source software development platform that facilitates these workflows (e.g. GitHub, GitLab, BitBucket, etc.)

**Requirements collection and maintenance:**
* Every non-trivial change to the software should be driven by a clear requirement or other clearly defensible argument.
* Create well structured and well documented version control (i.e. Git) commits for every change to the software, describing why the change was made and point to any requirements-related documentation (e.g. issue trackers).

**Clean Understandable Code Practices:**
* Favor languages that are more widely known and/or well supported over confusing or less well-known languages.
* Use domain-driven design for the key interfaces and implementation details.
* Strive for self-documenting code (i.e. reduce the need for extra documentation that typically does not get maintained).
* Reduce or eliminate code duplication (to avoid complicating future changes).
* Reduce software complexity (e.g. deep nested control structures, deep inheritance hierarchies)
* Continuously refactor the code while adding new features and fixing bugs to maintain or improve the code and other good code properties.

**Testing Practices:**
* Favor verification and acceptance tests over no-change regression tests<sup>[se2s-book-2016]</sup>.
* Use acceptance-test driven development (ATDD) and unit-test driven development (TDD) (because these tend to lead to better tests with better code coverage and better feature coverage than tests that get written after the code is written).
* Invest is making tests run as fast as possible (expensive tests are a significant form of technical debt to a software project).

**Building and Running Tests Practices:**
* Use build and tests systems that are better known and/or supported that can create portable builds on all target platforms (e.g. CMake and CTest)
* Make it easy to see summaries of test results and the ability to drill down into more details about what ran and what passed or failed and why (e.g. CTest and CDash).
* Set up automated builds that run tests before integrating changes to the main development branch (e.g. CI builders that are linked into GitHub or GitLab).


### Summary

The technical properties of a software package and its upstream dependencies can have a major impact in reducing the cost to maintain and extend a given software package.
In some cases, software can be sufficiently clean, well-tested, well-structured, and documented, and with minimal enough upstream dependencies that it can be reasonable sustained by any motivated developer, even if the originating development team and/or origination goes away.
This is the extreme form of sustainable software approaches the idea of ***self-sustaining software*** and should be the goal for many key software packages in the software system.
In identifying these desirable technical properties, projects can structure development processes that produce and maintain these desirable properties.


<!--- ToDos:

* Mention pulls (user demand, unique features, not easy to duplicate, little-to-no competition, high surface areas interaction with the code,...) and pushes for software sustainability?  => May not have room for this.  Article is already too long!

* Run wikize_refs.py ...

* Do detailed editing with Grammarly.com ...

--->


<!--- References --->

[bssw-ss]: https://bssw.io/items?topic=software-sustainability "BSSw: Software Sustainability"

[bssw-whatis-ss]: https://bssw.io/items/what-is-software-sustainability "BSSw: What is Software Sustainability?"

[se2s-book-2016]: https://www.routledge.com/Software-Engineering-for-Science/Carver-ChueHong-Thiruvathukal/p/book/9780367574277?srsltid=AfmBOorz50aK1Mkuti9WCQOMdLz8QPohQpMnZw3HLsxcrYWHuGEyKvju "'Testing of Scientific Software: Impacts on Research Credibility, Development Productivity, Maturation, and Sustainability' in 'Software Engineering for Science' {Bartlett, Roscoe A., Anshu Dubey, Xiaoye Sherry Li, J. David Moulton, James W. Willenbring, and Ulrike M. Yang. November 3, 2016}"


### Author bio

Roscoe A. Bartlett earned his PhD in chemical engineering from Carnegie Mellon University researching numerical approaches for solving large-scale constrained optimization problems applied to chemical process engineering.
At Sandia National Laboratories and Oak Ridge National Laboratory, he continued research and development in constrained optimization, sensitivity methods, and large-scale numerical software design and integration for computational science & engineering (CSE).
Dr. Bartlett currently focuses on software engineering challenges in CSE as well as the development of build, test, and integration software and processes for CSE.

<!---
Publish: Yes
Track: Deep Dive
Topics: Software sustainability
--->
