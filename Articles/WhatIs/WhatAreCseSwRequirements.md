
# What Are CSE Software Requirements?
<!--deck start--->

Software Requirements provide a bridge to translate the computational needs of scientists into capabilities of the software that developers aim to provide. While software requirements, thus, play a critical role in CSE domain, specifying such requirements can come with its own set of challenges.
<!--deck end--->

<!--body start--->

In software development, a *requirement* is a singular, documented statement identifying a capability, characteristic, or
quality a software product must possess in order to satisfy *one* of the needs of its stakeholders (e.g., developers, users, sponsors).

Software requirements *specification* is the process of eliciting and documenting whole sets of requirements aimed at defining
the complete capabilities of a software component, product, or system. The resulting document is also often referred to as the
*Requirements Specification* or *Requirements Spec.* or, imprecisely, just *Spec*.

### Need for CSE Software Requirements  
In CSE, software requirements typically arise out of the needs of users to perform some computational operation. For example,
given a software product to model the [heat equation](https://en.wikipedia.org/wiki/Heat_equation), users may *require* that
the package support anisotropic thermally conductive media or that it support time-varying boundary conditions.

For developers, requirements are necessary in order to understand the capabilities the software they create must meet. For users,
sponsors, and other stakeholders, requirements are necessary in order to communicate the capabilities they seek. Requirements
serve to define a contract between those developing software, those funding its development, and those using it.

A full specification commonly comprises many different types of requirements. These include functional, performance,
interface, and reliability requirements.

### Challenges Often Encountered in Defining Requirements
Eliciting and defining requirements can often be tricky for developers and users alike. New software development projects
are almost always seeking to develop some capability. Users clearly have trouble articulating a statement about something they have not previously seen. User statements about requirements thus may wind up being steeped in
verbiage about products and practices with which they are already familiar.

Another challenge in defining requirements is the fact that for long software development cycles, requirements often change with time. Thus, the software product that the
developers are creating can become a moving target.

Perhaps the biggest challenge in defining requirements is common confusion over *what* vs. *how* statements. Requirements need
to be statements about *what* the software will do; they should avoid as much as practical any entanglements about *how* the software should do it.
However, *how* statements are sometimes necessary in order to define any relevant *constraints* under which the software must operate.

For example, is it fair for an end user to *require* that a piece of software *"run on GPUs"*? Probably not. An end user
may care about performance and about floating-point power efficiency (flops/watt). However, the requirement needs to
be stated in those terms (e.g., "We require 6 gigaflops/watt power efficiency") and not in terms of a particular implementation
(e.g., "we require GPUs"").

### Requirements in Waterfall vs. Agile Development Processes
In the traditional [Waterfall](https://en.wikipedia.org/wiki/Waterfall_model) software development process,
development costs are heavily front loaded by investing significant resources in a complete requirements specification
before a single class is designed or a single line of code is written. This is in stark contrast
to the [Agile](https://en.wikipedia.org/wiki/Agile_software_development) development process where the requirement's specification
is iterated and refined right along with the software it specifies.


#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
<!--body end--->

<!---
Publish: yes
Pinned: yes
Topics: requirements
--->
