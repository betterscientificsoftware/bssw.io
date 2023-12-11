# Requirements and Requirements Engineering in Scientific Computing

<!-- deck text start -->
Do you understand Requirements and Requirements Engineering in scientific software life cycle? This article provides a good introduction.
<!-- deck text end --> 

#### Contributed by [Reed Milewicz](https://github.com/rmmilewi)
#### Publication date: October 26, 2017

A software **requirement** is a description of a specific capability that a software product is expected to have in order to satisfy the needs of stakeholders. While there is no single, agreed-upon definition of the term, it encompasses both the things that the software must do and the conditions under which it must do them. **Requirements engineering** is the process of formally identifying, documenting, and validating software requirements. For software engineers, requirements engineering represents the first steps in the development of a software product; requirements translate into specifications that then inform the design and implementation. 

Special emphasis is given to the requirements process because it is well known that the most painful struggles and the most spectacular failures in software development stem from oversights and misestimations early  in the life of a project (Reel 1999). Scientific software is no exception. Studies conducted by NASA in the early 1990s found that while cost overruns were rampant among R&D projects, projects that invested 2% to 3% of their budget on planning and developing requirements saw cost overruns between 80% and 200%, whereas those that invested 8% to 14% of their budget had overruns between 0% and 50% (Hihn and Habib-Agahi 1991, Habib-Agahi et al. 1991). The benefits are well established: requirements engineering, by far the least expensive development activity, has an outsized impact on everything that follows.

Nevertheless, numerous studies have found that scientific software developers, as a rule, do not produce requirements documents (Segal 2005, Segal 2009, Sanders and Kelly 2008, Li et al. 2011, Heaton and Carver 2015). There are several reasons for this situation, perhaps the greatest one being that researchers simply don't know how. Many scientific software projects are exploratory in character, and the requirements are discovered in the course of development. Trying to produce complete, well-articulated requirements upfront would be an exercise in futility. However, with some considerations and adaptations, readers will find that requirements engineering techniques can yield tremendous benefits.


## Understanding Requirements for Scientific Software

In the broadest terms, a requirement is a condition or capability that a software product ought to have. However, by this definition, virtually anything could be considered a requirement. Moreover, because requirements are often subject to change and not all can be known in advance, the name itself can seem misleading. Rather, as a starting point, requirements should be understood as *a device for communication between stakeholders*. Codifying requirements presents an opportunity for everyone involved to express their needs, wants, and expectations for the software. For the customer, that establishes a traceable, verifiable contract against which the software product can be compared, and for the developer, it informs the design specification and the implementation. 

Ralph Young, author of *The Requirements Engineering Handbook*, enumerates criteria for a good requirement (Young 2004). These include the following:


- A requirement should be *necessary* in the sense that if it can be done without, it should be discarded. At the same time, a requirement should only be given if it is *feasible* within a given budget and schedule.
- A requirement should be *unambiguous* and *concise*, written in a way that is straight-forward and intelligible to all stakeholders. On the other hand, a requirement should also be *complete*, detailing all the conditions for its fulfillment.
- The fulfillment of a requirement should be *verifiable*, and *traceable* from the requirements, to the design, and finally the code. Meanwhile, a requirement should also be *design independent*, written in such a way that the requirements are not married to a particular implementation.

In other words, a requirements document is neither a wish list nor a design document, but rather an instrument that explicitly connects the needs of stakeholders to the software product that satisfies them.

### Classifying and Characterizing Requirements

The goal of scientific software is to enable researchers to pose and answer scientific questions. This can give the impression that the requirements will be self-evident: the software needs to solve, process, simulate, interpolate, or analyze the object of study. However, high-level, abstract statements of purpose do not fulfill the criteria we have laid out, and they do not readily translate to solutions. Rather, we must decompose the goals of the software into smaller, more concrete units. There are numerous ways of categorizing the resulting requirements, but we will begin by dividing them into two broad categories:

- A **Functional requirement** (FR) defines a specific, fundamental action or behavior which the software must perform. These requirements are constrain the *design* of the system.
- A **Non-functional requirement** (NFR) describes a non-behavioral quality or attribute that the software must possess. These requirements constrain the *architecture* of the system.

For functional requirements, the words "specific" and "fundamental" should carry special weight. A requirement stating "the software must solve X" is certainly fundamental, but it is not specific enough to translate to a design or an implementation. In breaking down those goals into realizable steps, we often discover nuances and complications that enrich the design. 

Meanwhile, explicitly documenting non-functional requirements is important because maximizing quality in every sense is impossible. This is both because a perfect product is too expensive and time-consuming to build, and more importantly because there can be many competing or mutually exclusive measures of quality. Portability conflicts with reliability, maintainability supports reliability but rarely efficiency, and adding functionality strains usability.


## Writing Requirements for a Scientific Software

Gathering requirements and charting them down is a typical process in any kind of software development. In this section, we walk-through some examples of different kinds of requirements and understand how to write them. 

### Technological Requirements on Data Types 

Some functional requirements can be technological requirements; that is, there are particular constraints on the technologies that are employed in the solution. This is a common situation in the scientific computing world, which operates on the ever-changing cutting edge of hardware and software. For example, a team developing a tool to simulate ice sheet dynamics needs to translate geometry data provided by glaciologists to construct a mesh. That data is most often stored in a NetCDF format, and the team might write a requirement like the following:

> **Description**: The product shall support the NetCDF format.

The requirement is specific and fundamental. However, we can identify several ambiguities. First, it isn't clear whether the tool will need to read NetCDF files, write data in that format, or both. Second, the very meaning of "NetCDF" is ambiguous because the standard comprises multiple binary formats. Version 3.6+ extends the classic format with 64-bit offsets, and version 4 allows for data to be stored in an HDF5-equivalent format. In this case, consultation with clients reveals that data is stored in both version 3 and version 4 formats, which in turn informs the following requirement:

> **Description**: The product shall support data input both in NetCDF-3.6.0+ and NetCDF-4.0+ formats.

### Ease of Installation

One barrier to usability of scientific software applications is the need to build and configure the complex software stacks that support them. To reach a wider audience and remain relevant, a team may want to make their software as easy to install as possible. This leads to a nonfunctional requirement:

> **Description**: The software shall be easy to install.

This requirement raises several questions:

- *Easy to what extent?* The software may have a complex dependency structure, and incompatibilities may crop up with different versions of dependencies on different platforms. Setting limits on support implies limits to portability, but an open-ended commitment is unlikely to be feasible or practical.
- *Easy at what expense?* There may be a need to provide fine-tuned configurations in order to maximize performance on specific platforms. Supporting additional builds adds to maintenance costs unless sacrifices can be made (e.g., performance guarantees).
- *Easy for whom?* If the software is being developed for use by internal customers, one may be able to plan around their specific production environments. If the software is to be released as a general-use library, however, then fewer assumptions can be made. A more diverse audience may demand additional documentation or a more flexible build system.

Having to establish the scope on nonfunctional requirements is a key benefit of enumerating them. Finite resources must be spent satisfying the requirement, and doing so may require compromises with other important nonfunctional requirements. For these reasons, both functional and nonfunctional requirements can be extended with criteria that help set those bounds. Possible addenda to our ease-of-use requirement could include the following:

> **Description**: The software shall be easy to install.
>
> **Criterion**: The software shall provide performance portable builds for the Bacon and Parachute compute platforms.
>
> **Criterion**: A new customer shall be able to install the software in under thirty minutes, not including build times.

Thus, its important for requirements to be clearly defined, be un-ambiguous and as specific as possible, so as to ensure that correct expectations about the software are conveyed to all stakeholders and that the resulting product is well-defined, complete and functions as expected.

## Executing the Requirements Engineering Process
In this section, we elaborate on the requirements process - which encompasses the discovery and documentation of requirements. No single methodology exists for requirements engineering. The process can be sequential or iterative. It may target internal or external users. The requirements documentation needs for, say, a web service framework are radically different from those for avionics software. In any case, a full treatment of requirements engineering praxis goes beyond the scope of this article. Instead, we outline the four common steps involved. 

- **Requirements Elicitation**: Gathering data on the needs and wants of stakeholders.
- **Requirements Analysis**: Identifying the requirements.
- **Requirements Specification**: Producing a requirements specification artifact that models and expresses the requirements.
- **Requirements Validation**: Ensuring that the requirements match the needs and wants of stakeholers.

<!-- The below portion of text is taken from the article Part5-PerformingRequirementsEngineeringREVISE.md since it is incomplete -->

The elicitation and analysis steps are collectively known as the *sensemaking* phase of the requirements process, and the specification and validation steps are known as the *problem structuring* phase.

How should the requirements process be carried out in the context of a scientific software development project? A review of the literature suggests three trends of interest:
- Scientific software tends to be exploratory. Many key requirements may be unknown at the start.
- It is often long-lived. It is likely that the requirements will change over time.
- Software developed for the broader community has frequently come out of smaller projects intended for internal use. Therefore, stakeholders can change, and with them, the requirements.

Because of these factors, one should ensure that the requirements process is being thought of not as a singular event but as an ongoing activity that spans the lifecycle of the scientific product.


### Citations
- John S Reel. Critical success factors in software projects. *IEEE Software*, 16(3):18–23, 1999.
- Jairus Hihn and Hamid Habib-Agahi. Cost estimation of software intensive projects: A survey of current practices. In *Proceedings of the 13th international conference on Software engineering*, pages 276–287. IEEE Computer Society Press, 1991.
- Hamid Habib-Agahi, Shantanu Malhotra, and James Quirk. Estimating software productivity and cost for NASA projects. *Journal of Parametrics*, 11(1):59–71, 1991.
- Judith Segal. When software engineers met research scientists: A case study. *Empirical Software Engineering*, 10(4):517–536, 2005.
- Judith Segal. Some challenges facing software engineers developing software for scientists. In Software Engineering for Computational Science and Engineering, 2009. *SECSE’09*. ICSE Workshop, pages 9–14. IEEE, 2009.
- Rebecca Sanders and Diane Kelly. Dealing with risk in scientific software development. *IEEE software*, 25(4), 2008.
- Yang Li, Nitesh Narayan, Jonas Helming, and Maximilian Koegel. A domain specific requirements model for scientific computing (NIER track). In *Proceedings of the 33rd International Conference on Software Engineering*, pages 848–851. ACM, 2011.
- Dustin Heaton and Jeffrey C Carver. Claims about the use of software engineering practices in science: A systematic literature review. *Information and Software Technology*, 67:207–219, 2015.
- Ralph Rowland Young. The requirements engineering handbook. Artech House, 2004.


<!---
Publish: yes
Topics: Requirements
Track: Deep Dive
Pinned: no
RSS update: 2017-10-26
--->
