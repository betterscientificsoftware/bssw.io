# Writing Requirements

In this resource, we work through a number of examples of requirements and how to write them.

### Technological Requirements on Data Types 

Some functional requirements can be technological requirements; that is, there are particular constraints on the technologies that are employed in the solution. This is a common situation in the scientific computing world, which operates on the ever-changing cutting edge of hardware and software. For example, a team developing a tool to simulate ice sheet dynamics needs to translate geometry data provided by glaciologists to construct a mesh. That data is most often stored in a NetCDF format, and the team might write a requirement like sthe following:

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

#### Contributed by [Reed Milewicz](https://github.com/rmmilewi)

#### Publication date: October 26, 2017

<!---
Publish: yes
Categories: Planning
Topics: requirements
Tags: requirements, howto
Level: 2
Prerequisites: defaults
Aggregate: subresource

% LCM: Temporarily change to level 2, reconsider later for aggregate WhatIs content for requirements
--->
