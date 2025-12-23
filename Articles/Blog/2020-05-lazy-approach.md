# The Lazy Approach to Developing Scientific Research Software

**Hero Image:**

 - <img src='../../images/Blog_0620_YAGNI.jpg' />

#### Contributed by [Carl S. Adorf](https://github.com/csadorf "Carl S. Adorf GitHub Profile") and [Vyas Ramasubramani](https://github.com/vyasr "Vyas Ramasubramani GitHub Profile")

#### Publication date: June 16, 2020

## Scientific software developers tend to extremes

A common obstacle in the development of scientific software is that it
is typically carried out by researchers doubling as software
engineers, a profession in which they usually lack formal training or
experience. While they may try to educate themselves via online
courses or other materials, historically those materials have
typically been targeted at software developers in industry, where
different best practices may apply. Moreover, software quality and
reusability are generally secondary considerations at best since
development itself is only indirectly funded and rewarded through the
scientific results it produces. Thus, scientists funded to
achieve certain scientific goals face difficult design decisions with
respect to the scope and generality of their software.

Experience shows that many scientists in this position fall into one
of two extremes. On the one hand, scientists for whom code is purely a
means to an end spend minimal time educating themselves on best
practices in software development, instead opting for the minimal
scope, generality, and overall quality that gets the job done. On the
other hand, scientists who enjoy software development educate
themselves on good development practices and tend to write more
readable, reusable, and generalizable code; but they expend
unnecessary effort on generalizing software well beyond the needs of
any demonstrated practical application. The former strategy is
expedient in the short term but highly inefficient in the long run
since it ultimately results in many researchers simply reinventing the
wheel. Conversely, the latter strategy is usually inefficient in the
short term since the time and effort put into development hinder
research progress; and without suitable evidence that this effort will
pay off in the long term, such development cannot be justified on
scientific grounds. Furthermore, efficient generalization requires a
lot of experience and foresight that are usually hard to obtain.

## Finding the middle path

While organizations such as [The Carpentries](https://carpentries.org/)
have emerged to help researchers gain the skills needed for proper
software development, the problem of finding the right balance between
these two development extremes is usually still left to
researchers. In an ideal scenario, researchers would develop software
that solves their immediate needs while maintaining just enough
flexibility to enable later generalization if needed. In practice, however,
achieving this balance is notoriously difficult. In our
[article](https://doi.org/10.1109/MCSE.2018.2882355) for Computing in
Science & Engineering we proposed the *lazy refactoring* technique as
a practical approach to finding that balance.

In short, lazy refactoring advocates that new development should
remain at a prototype stage until the specific scientific goal is
achieved, but it should be refactored into more general, reusable code
once a third use for it is found. This ensures that the majority of
development time is spent on solving the problem that motivated the
development.

The lazy refactoring approach depends on adhering to certain minimal code standards to
ensure that prototypes can be generalized with reasonable effort once
their reuse potential has been identified. Specifically, prototype
code should do the following:
* Be under version control to track the logical development, for example,
  with git.
* Provide minimal documentation: a README file is a must. As a
  benchmark, the documentation should be sufficient such that one can digest the logical flow of the code without significant
  effort.
* Adhere to some common sense  standard applicable for the 
  programming language used (e.g., PEP8 for Python or the C++ Core
  Guidelines).
* Be validated (ideally against known results) in the context of the
  scientific application.
* Include a license (ideally permissive) such that people other than the
  original author are able to reuse the code at a later stage.

Lazy refactoring has several advantages. First, it ties all
development to specific, tangible research goals, removing the burden
of needing to justify development efforts to funding sources that are
 interested  primarily in scientific outcomes. Second, it defers any
generalization to a stage at which the problem and software use cases
are better understood, which helps in designing a better API. Third,
it reduces the risk that the additional development effort spent on
producing generalized code is completely wasted. This situation could happen
when, for example, a method is implemented within a general software
package  but is quickly superseded by a superior
method before being used enough to justify the implementation effort.

## Applying lazy refactoring  to new software or new feature development

Since we originally proposed this method, we have found it suitable as
a general guideline for making decisions on how to prototype and
generalize software. It is especially easy to apply in the
development of completely new software. Initially, it may seem less
applicable in the context of mature software projects, but the basic
concept remains  the same: any new feature should still be justified by immediate
need and be prototyped before being generalized.

Eventually, some projects reach a level of maturity at which there are
a large number of users and use cases and it becomes increasingly
challenging to tie all development efforts to specific scientific
research needs. At this stage, lazy refactoring can still be applied
to the development of new features, but regular maintenance efforts
such as reducing technical debt or resolving dependency
incompatibilities need not be vetted through this process. Ensuring
that such software remains usable and amenable to development within a
rapidly changing hardware and software environment is justified by the
existing applications of the software, and maintainers should consider
seeking dedicated funding.

## Balancing immediate needs with a path forward
In summary, lazy refactoring helps developers of scientific software
in academic contexts effectively prioritize software development
efforts by focusing on immediate scientific needs balanced with a
clear path toward general-purpose utilization. This process helps
justify development efforts to funding agencies while effectively
improving overall code quality.

## Acknowledgments

This article is based on a paper in the IEEE Computing in Science and
Engineering special issue on *Accelerating Scientific Discovery with
Reusable Software:* Carl S. Adorf, Vyas Ramasubramani, Joshua
A. Anderson, and Sharon C. Glotzer, *How to Professionally Develop
Reusable Scientific Software -- And When Not To,* Computing in Science
and Engineering 21, 66-79 (2019). DOI:
[10.1109/MCSE.2018.2882355](https://doi.org/10.1109/MCSE.2018.2882355)

## Image Attribution
Image by Dave Taylor from Boulder, CO, is licensed under CC BY 2.0.

## Author bios

Dr. Carl Simon Adorf is a postdoctoral researcher in the group of
Prof. Nicola Marzari at École polytechnique fédérale de Lausanne
(EPFL). He obtained his Ph.D. at the University of Michigan under
the supervision of Sharon C. Glotzer in 2019. Dr. Adorf is an expert in
employing machine learning algorithms for identifying and
analyzing crystallization pathways of colloidal crystals and has
made a huge impact on the scientific computing community by inventing
and leading the development of the signac framework ([signac.io](http://signac.io/)). He is
currently a developer for the AiiDA computing infrastructure
([aiida.net](http://aiida.net/)) and the Materials Cloud open science platform
([materialscloud.org](http://materialscloud.org/)) as part of his involvement with the Horizon 2020
MARKETPLACE project.

Vyas Ramasubramani is a Ph.D. candidate in the group of Sharon Glotzer
at the University of Michigan, Ann Arbor, where he studies particle
self-assembly, especially of
proteins, at the nanoscale and microscale. Vyas is a maintainer and lead developer for both the [signac](http://signac.io/)
data management framework and the [freud](http://freud.readthedocs.io/) simulation analysis toolkit,
and he created the [rowan](https://rowan.readthedocs.io/) package for quaternion mathematics. He is
also a core developer for [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/), a popular particle simulation
package that is highly optimized for GPUs.

<!---
Publish: yes
Track: experienc
RSS update: 2020-06-16
Categories: Planning, Development
Topics: Software Engineering, Requirements, Refactoring
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
