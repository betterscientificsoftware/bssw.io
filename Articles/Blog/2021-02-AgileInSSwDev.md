# When Not to Use Agile in Scientific Software Development

**Hero Image:**

 - <img src='../../images/Blog_0221_Agile.png'>

#### Contributed by [Anshu Dubey](https://github.com/adubey64 "Anshu Dubey GitHub Profile")

#### Publication date: February 12, 2021
 
<!-- deck text start --> 
Using Agile principles in the development of scientific software is widely accepted as a best practice.  But in some situations, a deeper initial dive into requirements and design can be beneficial.
<!-- deck text end -->

###  Agile principles in science vs enterprise software
Over the past few years, it has almost become an orthodoxy among 
better-informed scientific software developers to follow 
[Agile](https://agilemanifesto.org/) principles in their software processes. Several
reasons have driven this scenario. Initially, the models that
dominated enterprise software before the advent of Agile methods had far too many process overheads to be even remotely feasible in science environments. More important, two key ideologies coincided with one another: the growing popularity of Agile principles in
enterprise software and the scientific software community's growing awareness of the adverse impact on productivity in the absence of defined
software processes.  However, the ways in which the
adoption of Agile principles have affected these two  areas of software
development could not be more different.

In enterprise software, Agile methods have served to reduce the upfront
overheads and made  processes more nimble. In most science
domains, the software development process has traditionally 
resembled dysfunctional Agile, in the sense that the development was
driven by results needed for the next science paper. The emphasis was on quick
development and availability to the "client," who was often the
developers themselves. The flip side was that the amount of technical debt
accrued through such  unplanned development led to the
untimely demise of many scientific software projects. So, ironically,
the introduction of Agile methods in these scientific domains 
was doing the exact opposite of what it was doing for 
enterprise software. That is, Agile methodology was slowing down the next "delivery"
of scientific software to incorporate some process where none had existed before.

### Is Agile always the right answer?
Over the course of two major version revisions of [FLASH](https://arxiv.org/pdf/0903.4875.pdf), a large and long-lived scientific software project,  I have come to the conclusion that while the incorporation of more formal processes as part of Agile has generally been helpful, the evangelization of
Agile in the community may have gone too far for some classes of
scientific software, in particular multiphysics multidomain
codes. For example, because of their mathematical complexity, long-lived
multiphysics codes tend to exercise separation of concerns, where
bookkeeping is kept separate from the numerics. This approach is
driven partly by the interdisciplinary nature of these projects and
partly by the highly dynamic world of algorithms used in scientific
software.  Many multiphysics application software projects rely on a
robust framework to enable flexibility and extensibility
of the software.  As with anything that needs to be robust and has to
last a long time, a great deal of thought needs to go into
requirements gathering and design. In this instance, Agile methods can be counterproductive. The exploration of the design space itself can follow
Agile principles, but the overall design of the framework requires a more holistic
approach.

FLASH  had been quickly stitched together
initially using three pre-existing codes following the "quicker than
Agile" approach common in science. Use of Agile would have been 
appropriate for the first functional version; but once a tool was
available to do science, it was equally important to redesign and
refactor.  The availability of this "quick and dirty" solution
permitted a more considered approach to design for longevity. In two
instances of major architectural revisions of FLASH that I have been
associated with, the design phase took longer than 6 months of discussions, white
boarding, prototyping, refining, and even discarding ideas. Both
times the architectural revision took more than two years from the start before the first
simple application instance could be configured. As a result of this
upfront investment in requirements gathering and thoroughly understanding the design
space,  the code has been able to pivot
to several science domains (it was built for astrophysics, and it is
now used by at least six other domains), saving huge infrastructure
development efforts in those domains.  

### Software processes should fit the needs
As with everything else in the world, process should fit needs. Where modifications impact a lot of code, making the cost of modifications high, but where the rate of change is very low, more thorough planning is called for. On the other hand, where changes are frequent, relatively inexpensive, and local (e.g., some numerical algorithms), Agile is the perfect choice.

### Acknowledgement
This blog post was first presented as a whitepaper at the [2020 Collegeville Workshop](https://collegeville.github.io/CW20/) (CW20).

### Author bio
Anshu Dubey is a computational scientist in the Mathematics and Computer
Science Division at Argonne National Laboratory and a Senior Scientist
in the Department of Computer Science at the University of
Chicago. She is the chief software architect for FLASH, 
a multiphysics, multiscale HPC application that is used by multiple
science and engineering domains as their community code. She is
interested in all aspects of HPC scientific software, with special
emphasis on design, productivity, and sustainability issues.


<!---
Publish: yes
Track: experience
RSS update: 2021-02-12
Categories: planning, development
Topics: software engineering, refactoring
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
