# What is CSE Software Refactoring?
#### Publication date: April 20, 2019

<!--deck start--->
Software  refactoring is the process of restructuring existing software code but without changing its external functionality. Refactoring is gaining recognition as a way of improving developer productivity!
<!--deck end--->

<!--body start--->
[Software refactoring](https://en.wikipedia.org/wiki/Code_refactoring) is the process of restructuring source code
to achieve improvements in various [*non-functional*](https://en.wikipedia.org/wiki/Non-functional_requirement) or
*quality* attributes of the software such as maintainability, readability, complexity, and extensibility to name a few.
In particular, refactoring does not change any of the software product's external functionality. Refactoring is a way
of improving developer productivity.

Ideally, refactoring should not proceed *without* first having a collection of
[*unit tests*](https://en.wikipedia.org/wiki/Unit_testing) with sufficient
[*coverage*](https://en.wikipedia.org/wiki/Code_coverage) of the code to be refactored. In practice, however,
in high functioning development teams some common forms of re-factoring occur routinely and organically as part of
their development processes to avoid duplication of closely related functionalities and reuse bits and pieces of
source code.

It should be noted that in all but the most trivial of situations, the common practice of *cut-n-paste-n-adjust*
programming, although possibly the most expedient, inevitably creates a re-factoring burden rather than solving one.
Later on, another developer having to maintain such code will have to do the software engineering work to collapse all
the cut-n-paste instances into a single implementation that can be reused where necessary.

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
<!--body end--->

<!---
Publish: yes
Pinned: yes
Topics: refactoring
--->
