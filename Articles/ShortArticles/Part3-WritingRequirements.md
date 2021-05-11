# A Walk-through for Writing Requirements for a Scientific Software

<!--- deck start -->
Gathering and writing requirements is an essential process in  software development. Do you know how to write good requirements for  scientific software?
<!---deck end --->


#### Contributed by [Reed Milewicz](https://github.com/rmmilewi)
#### Publication date:  July 21, 2019

Gathering requirements and charting them down is a typical process in any kind of software development. In this short article, we walk-through some examples of different kinds of requirements and understand how to write them. 

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

## Mini-series list
- [Overview of Requirements and Requirements Engineering](Part1-RequirementsAndRequirementsEngineering.md)
- [Understanding requirements](Part2-UnderstandingRequirements.md)
- [Writing requirements](Part3-WritingRequirements.md)
- [Understanding and Performing the requirements engineering process](Part4-UnderstandingPerformingRequirementsEngineering.md)

<!---
Publish: yes
Topics: requirements
Pinned: no
RSS update: 2019-07-21
--->
