
# What are CSE Software Requirements?

In software development, a *requirement* is a singular, documented statement identifying a capability, characteristic, or
quality a software product shall possess to satisfy *one* of the needs of it's stakeholders (e.g. developers, users, sponsors, etc.).

Software requirements *specification* is the process of eliciting and documenting whole sets of requirements aimed at defining
the complete capabilities of a software component, product or system. The resulting document is also often refered to as the
*Requirements Specification* or *Requirements Spec.* or, imprecisely, just *Spec*.

In CSE, software requirements typically arise out of the needs of users to perform some computational operation. For example,
given a software product to model the [Heat Equation](https://en.wikipedia.org/wiki/Heat_equation), users may *require* that
the package support anisotropic thermally conductive media or that it support time-varying boundary conditions.

For developers, requirements are necessary to understand the capabilities the software they create must meet. For users,
sponsors and other stakeholders, requirements are necessary to communicate the capabilities they seek. Requiements
serve to define a contract between those developing software, those funding its development and those using it.

It is common to have many different types of requirements in a full specification. These include functional, performance,
interface, and reliability requirements.

## Challenges Often Encountered in Defining Requirements
Eliciting and defining requirements can often be tricky for developers and users alike. First, new software development projects
are almost always seeking to develop some new capability not ever previously seen by any users. It is difficult for users to
articulate statements about something they've never seen before. User's statements about requirements wind up being steeped in
verbiage about products and practices with which they are already familiar.

For long software development cycles, it is not uncommon for requirements to change with time. This means the software product
developers are creating can become a moving target.

Perhaps the biggest pitfall in defining requirements is common confusion over *what* vs. *how* statements. Requirements need
to be statements about *what* the software shall do avoiding as much as practical any entanglements about *how* it shall do it.
However, *how* statements are sometimes necessary to define any relevant *constraints* under which the software shall operate.

For example, is it fair for an end-user to *require* that a piece of software *"run on gpus"*? Probably not. An end user
may care about performance and about floating point power efficiency (e.g. flops/watt). However, the requirement needs to
be stated in those terms (e.g. we require 6 gigaflops/watt power efficiency) and not in terms of a particular implementation
(e.g. we require gpus).

## Requirements in Waterfall vs. Agile Development Processes
In the traditional [Waterfall](https://en.wikipedia.org/wiki/Waterfall_model) software development process,
development costs are heavily front loaded by investing a significant resources in a complete requirements specification
before a single class is designed or line of code is written. This is in stark contrast
to the [Agile](https://en.wikipedia.org/wiki/Agile_software_development) development process where the requirements specification
is iterated and refined right along with the software it specifies.

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

<!---
Publish: yes
Categories: planning
Topics: requirements
Tags: waterfall, agile
Level: 0
Prerequisites: none
Aggregate: none
--->
