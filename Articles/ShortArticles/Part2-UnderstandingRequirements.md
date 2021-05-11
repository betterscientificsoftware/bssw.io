# Understanding Requirements for Scientific Software

<!--- deck text start -->
Understanding and gathering requirements is an essential process in software development. Learn about how to understand requirements for scientific software!
<!---deck text end --->

#### Contributed by [Reed Milewicz](https://github.com/rmmilewi)
#### Publication date: October 26, 2017

In the broadest terms, a requirement is a condition or capability that a software product ought to have. However, by this definition, virtually anything could be considered a requirement. Moreover, because requirements are often subject to change and not all can be known in advance, the name itself can seem misleading. Rather, as a starting point, requirements should be understood as *a device for communication between stakeholders*. Codifying requirements presents an opportunity for everyone involved to express their needs, wants, and expectations for the software. For the customer, that establishes a traceable, verifiable contract against which the software product can be compared, and for the developer, it informs the design specification and the implementation. 

Ralph Young, author of *The Requirements Engineering Handbook*, enumerates criteria for a good requirement (Young 2004). These include the following:


- A requirement should be *necessary* in the sense that if it can be done without, it should be discarded. At the same time, a requirement should only be given if it is *feasible* within a given budget and schedule.
- A requirement should be *unambiguous* and *concise*, written in a way that is straight-forward and intelligible to all stakeholders. On the other hand, a requirement should also be *complete*, detailing all the conditions for its fulfillment.
- The fulfillment of a requirement should be *verifiable*, and *traceable* from the requirements, to the design, and finally the code. Meanwhile, a requirement should also be *design independent*, written in such a way that the requirements are not married to a particular implementation.

In other words, a requirements document is neither a wish list nor a design document, but rather an instrument that explicitly connects the needs of stakeholders to the software product that satisfies them.

## Classifying and Characterizing Requirements

The goal of scientific software is to enable researchers to pose and answer scientific questions. This can give the impression that the requirements will be self-evident: the software needs to solve, process, simulate, interpolate, or analyze the object of study. However, high-level, abstract statements of purpose do not fulfill the criteria we have laid out, and they do not readily translate to solutions. Rather, we must decompose the goals of the software into smaller, more concrete units. There are numerous ways of categorizing the resulting requirements, but we will begin by dividing them into two broad categories:

- A **Functional requirement** (FR) defines a specific, fundamental action or behavior which the software must perform. These requirements are constrain the *design* of the system.
- A **Non-functional requirement** (NFR) describes a non-behavioral quality or attribute that the software must possess. These requirements constrain the *architecture* of the system.

For functional requirements, the words "specific" and "fundamental" should carry special weight. A requirement stating "the software must solve X" is certainly fundamental, but it is not specific enough to translate to a design or an implementation. In breaking down those goals into realizable steps, we often discover nuances and complications that enrich the design. 

Meanwhile, explicitly documenting non-functional requirements is important because maximizing quality in every sense is impossible. This is both because a perfect product is too expensive and time-consuming to build, and more importantly because there can be many competing or mutually exclusive measures of quality. Portability conflicts with reliability, maintainability supports reliability but rarely efficiency, and adding functionality strains usability.

## Mini-series list
- [Overview of Requirements and Requirements Engineering](Part1-RequirementsAndRequirementsEngineering.md)
- [Understanding requirements](Part2-UnderstandingRequirements.md)
- [Writing requirements](Part3-WritingRequirements.md)
- [Understanding and Performing the requirements engineering process](Part4-UnderstandingPerformingRequirementsEngineering.md)

### Citations
- Ralph Rowland Young. The requirements engineering handbook. Artech House, 2004.


<!---
Publish: yes
Topics: requirements
Pinned: no
RSS update: 2017-10-26
--->
