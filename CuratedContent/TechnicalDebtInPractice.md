## Technical Debt in Practice: How to Find It and Fix It

<!--- deck text start --->
This book describes a comprehensive and systematic approach to measuring, quantifying, and reducing various types of technical debt that are slowing down a given software project, making it more agile and sustainable.
<!--- deck text end --->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)
#### Publication date: December 19, 2024

Resource Information | Details
:--- | :---
Book title  | [Technical Debt in Practice: How to Find It and Fix It](https://books.google.com/books/about/Technical_Debt_in_Practice.html?id=m2WCzgEACAAJ)
Authors | Neil Ernst, Rick Kazman, Julien Delange
Publication | 2021, ISBN: 780262366304, DOI: https://doi.org/10.7551/mitpress/12440.001.0001

Technical debt can build up in a software project to the point where it chokes the life out of it by stagnating development, ballooning defects, slipping schedules, and ultimately resulting in scrapped systems.
The concept of ***Technical Debt*** was created in 1992 by Ward Cunningham as a way to communicate to and motivate management to support software developer efforts to improve the design and implementation of software to make it easier to maintain and extend.

A more general definition of software technical debt might be:

> Choices in software design, implementation, testing, documentation, and other areas made for short-term gains in development and deployment speed (or for faster learning) that make the software more expensive to maintain and extend longer-term.

While there are many free sources of information about software technical debt and how to address it ([for example](https://bssw.io/items/keep-interest-on-technical-debt-from-sinking-your-software-project)), arguably, none of them provide the type of cohesive, comprehensive, in-dept treatment on the topic provided by the book ***Technical Debt in Practice: How to Find It and Fix It***.

### Categories and common sources of technical debt

This book covers the detection, quantification, and correction of technical debt in the following standard areas of software development (along with common sources of technical debt in each area):

* **Requirements debt**:
  * Poor requirements engineering
  * Ignorance of requirements
* **Design and architecture debt**:
  * Improper separation of concerns
  * Clone and own
  * Tangled dependencies
  * Unplanned evolution
* **Implementation debt**:
  * Lack of coding standards
  * Needlessly inefficient code
  * Deprecated libraries
  * Code duplication
* **Testing debt**:
  * Poor test coverage
  * Flaky tests
  * Fragile tests
  * Slow tests
* **Deployment debt**:
  * Manual deployment
  * No staging
  * Single velocity
  * Poor observability
* **Documentation debt**:
  * Developers have to answer a lot of user questions
  * Documents not traceable
  * Documents outdated
  * Too much documentation

In addition to these universal categories, the book also covers more specialized types of technical debt:

* **Technical debt in machine learning systems**:
  * Poor integration (with non-model components)
  * Poor explainability (i.e. black-box systems)
  * ML parameter configuration issues
  * Lack of testing (hard with probabilistic systems)

The authors also take on broader types of (non-technical) software project debt in:

* **Team management and social debt**:
  * Cookbook development (developers stuck in their ways and not willing to consider alternatives)
  * Time warp (not accounting for communication time and coordination levels)
  * Cognitive distance (differences in social, education, and other areas making it hard to work together)
  * Newbie free-riding (not on-boarding new developers and the free-riding of older employees)
  * Power distance (some developers assuming they have less power than others)
  * Disengagement (thinking the software is more mature than it is)
  * Piggish members (rigid and unreasonable requirements on others)
  * Institutional isomorphism (one size fits all for all projects within the same institution)
  * Hypercommunity (hyperconnected community with group-think and lack of diverse views)
  * DevOps clash (between developers and operations teams, multiple locations, etc.)
  * Informatively excess (lack of processes and information management)
  * Unlearning (team members not able to use newer practices due to members unwilling to change)
  * Organizational silo (Siloed teams of developer teams that do not communicate)
  * Black cloud (Information overload due to lack of structured communication and info management)
  * Lone wolf (Renegade contributors that don't coordinate or collaborate with peers)

### Technical debt principle and interest payments

The comparison of technical debt to financial debt and the concepts of debt ***principle*** and debt ***interest*** payments have been widely embraced in the software development community.
The differentiation between the *principle* of paying down a given source of technical debt as opposed to the *interest* payment for not paying down that debt is critical.
For example, suppose a given technical debt principal cost is massively larger than the interest payment.
In that case, paying down that debt may never be justified (unless there is a very long time horizon).
For instance, while the cost to maintain a Rust program may be less than maintaining an equivalent C++ program for the same functionality, the principal payment cost to convert a large C++ program to Rust may be massive and a project may never recoup the cost compared to maintaining the existing C++ software, even over many years.

<!---
The interest payment cost accumulates over time, so the length of time between when given tech debt is added and when it is paid off is an important consideration.
Even a smaller interest payment integrated over a long period of time can result in a huge cumulative cost to the project.
--->

### Insights and guidance on the management of technical debt

Some of the more interesting (and non-obvious) arguments and insights the authors make about technical debt in this book include:

* **The accumulation of some technical debt is actually beneficial** in that it allows projects to go faster and get to market before competitors.  (This is *deliberate* and *prudent* technical debt.)
* **All software projects constantly and naturally accumulate technical debt.** (This can either be *deliberate* or *inadvertent*, *prudent* or *reckless*.  For example, [*Emergent Design*](https://en.wikipedia.org/wiki/Emergent_design#Emergent_design_in_agile_software_development) naturally creates some architectural/design debt as new features are added and the architecture and design must be constantly refactored to match.)
* While projects should never try to eliminate all technical debt, **projects should actively monitor, measure, and manage technical debt** to keep the interest payments from becoming too high (thereby damaging the software and productivity, quality, etc. too much).
* **Some sources of technical debt can only be detected and quantified by analyzing the dynamics of processes** (such as software development, deployment, user support, and other software processes).  (For example, detecting architecture/design debt requires analyzing commits, issue trackers, common sets of files frequently changed together, and other information that is not evident in a static analysis of the file contents for the project.)
* **Implementation debt tends to <u>not</u> be the largest sources of technical debt** in most projects.
* **Technical debt should be paid down based on priority and a cost/benefit analysis.** (For example, technical debt with high interest/principle ratios should be paid down before debt with lower ratios.)
* Most projects should **plan to spend between 15% to 20%** of their development effort on **paying down technical debt**.
* Technical debt metrics and quantification are critical for **making the business case for identifying and paying down technical debt** by focusing on the **impact of technical debt interest payment cost on the value stream**.
* **Some technical debt may never need to be repaid.**  (For example, a very complex, poorly designed and coded piece of legacy code may not need to be addressed if it works and does not need to change and/or will be completely replaced soon.)
* Much of the otherwise **reckless and/or inadvertent technical debt can and should be avoided in the first place** by applying well-known software development best practices.
* Companies and **organizations that don't view software as a core asset tend to produce software with large amounts of unmanaged technical debt**.
* Software projects that don't pay down significant and obvious technical debt **drive away good developers and result in lower-performing development teams** (which in turn create more unmanaged technical debt).

### Software engineering best practices and technical debt

A lot of the material in this book espouses the virtues of modern agile software development technical practices and principles such as:

* [SOLID design principles](https://bssw.io/items/solid-design-principles)
* [Design patterns](https://en.wikipedia.org/wiki/Software_design_pattern)
* [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development)
* [Peer code review](https://bssw.io/items?topic=peer-code-review)
* [Continuous integration](https://bssw.io/items?topic=continuous-integration-testing) and modern [DevOps](https://bssw.io/items/what-is-devops)
* Usage of newer language features and tools (e.g., [modern C++20+ vs. C++98](https://bssw.io/items/c-core-guidelines), [static analyzers and linters](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#appendix-d-supporting-tools), [code formatters](https://bssw.io/blog_posts/coding-conventions), etc.)

and many others.  However, the book places these agile technical practices within the consistent framework of technical debt avoidance, reduction, and management (thereby providing a solid connection to bottom-line software productivity and sustainability).
Therefore, this book could be used to introduce many of these modern software engineering practices and help motivate them better than is often done in other software engineering literature.

### Technical debt case studies

The book is filled with many case studies in the application of technical debt analysis, quantification, and reduction efforts.
Examples of some of the more interesting case studies include:

* **FaceBook** started out using PHP and switched the implementation of critical parts to C++ incrementally to improve performance and scalability.
  * => A success story for going fast early and then incrementally paying down technical debt
* **Phoenix Payment System** deployed with massive defects due to poor requirements engineering and poor testing.
  * => An example of a massive failure due to requirements and testing debt
* **Netscape 6** (which became Mozilla and then FireFox) was a complete rewrite from scratch that took too long and resulted in a massive loss in market share to competitors like Microsoft Internet Explorer (IE).
  * => A massive failure due to ignoring technical debt and then trying to eliminate it by starting over (which is rarely successful for a complex piece of software, see [Things You Should Never Do, Part I](https://bssw.io/items/things-you-should-never-do-part-i))
* **Google Chromium Project** where significant architecture and design debt related to the Plus10 bugs were identified, quantified, and addressed.
  * => An example of the successful usage of architecture/design debt identification tools and remediation through refactoring
* **SoftServe SS1** project:
  * => A detailed example of applying architectural/design debt identification and quantification tools and metrics-based prioritization and remediation of the largest sources of technical debt with quantified payoff
* **Brightsquid** project:
  * => Another detailed example of applying architecture/design debt identification and quantification tools and remediation of the largest sources of technical debt with solid evidence for the payoff
* **Twitter** refactored from a monolithic Ruby on Rails website to an architecture using microservices with several different implementations and redundancy.
  * => A detailed example of how changing architecture allowed changing programming languages for different pieces and incrementally paying down technical debt
* **Atacama Large Millimeter Array (ALMA)** scientific software to manage radio telescopes and data.
  * => An example of how large amounts of technical debt can be created in these types of scientific projects staffed by domain experts with little software backgrounds and how that can slow down development, deployment, and maintenance, compared to more traditional software projects.

### Summary

In summary, the unique contribution of this book (compared to what one gets from reading the standard software engineering texts) is the systematic approach to identifying issues that slow down and harm a software project (using the analogy of technical debt), which are then addressed in priority order through the application of modern software engineering best practices.

<!---
Publish: yes
Pinned: no
Topics: Software engineering, Software process improvement, Projects and organizations, Requirements, Design, Software sustainability, Refactoring, Issue Tracking, Release and Deployment, Documentation, Peer Code Review, Testing, Continuous Integration Testing
--->

<!---
LocalWords:  observability
--->
