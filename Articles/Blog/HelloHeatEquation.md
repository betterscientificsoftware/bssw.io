# That Time CSE Had Me at Hello World

**Hero Image:**

 - <img src='https://github.com/betterscientificsoftware/images/raw/master/hello_world_sun_heat.png'/>

#### Contributed by [Heather M. Switzer](https://github.com/heatherms27 "Heather Switzer GitHub Profile"), [Elsa Gonsiorowski](https://github.com/gonsie "Elsa Gonsiorowski GitHub Profile"), and [Mark C Miller](https://github.com/markcmiller86 "Mark C Miller GitHub Profile")

["Hello World!"](https://www.thesoftwareguild.com/blog/the-history-of-hello-world/)
is the canonical *first* program beginners write to learn new programming methodologies.
In computational science and engineering ([CSE](https://en.wikipedia.org/wiki/Computational_engineering))
circles, programming methodologies can involve a variety of languages, parallel execution
and programming models, discretization techniques, interdependent libraries, and more.
An application solving the [heat equation](https://en.wikipedia.org/wiki/Heat_equation)
represents the perfect "Hello World!" program for the CSE world.

### What is the heat equation?
The Heat Equation, a special case of the Diffusion Equation, was developed by Joseph
Fourier in 1822. It describes how the distribution of heat varies over space and time
in a material. While there are many adaptations for different scenarios, beginner CSE
programmers often start with the one-dimensional, homogeneous Heat Equation as an
introductory problem.

_&part;u / &part;t = &alpha;&nabla; &sup2;u_

Where:
* _u_ = Temperature
* _t_ = time
* _&alpha;_  = thermal diffusivity of the material
* _&nabla;_ = The Laplace operator

To make the equation even more approachable, we make some simplifying assumptions:
* _&alpha;_ is constant (the material is homogeneous)
* Apart from initial/boundary conditions, there are no other heat sources
* Only Cartesian coordinates in 1 dimension are used

### Why this form of the heat equation?
The one dimensional heat equation might not be sufficient to
model solar heating of the Earth. However, even in this relatively simple form,
interesting and meaningful science questions may be investigated involving
both transient and steady-state behavior. Examples are determining if water
pipes embedded in log cabin (solid wood) walls would freeze during a cold
storm or the required thickness of insulation around fuel pipeline to avoid
combustion from a fast burning brush fire. These and many other questions
involving heat flow can be investigated with this relatively simply form of
the heat equation.

Solutions to the one dimensional heat equation are also very easy for
beginners to visualize. This can help them understand how different
approaches work. The simplicity of the physics and mathematics also
allows beginners to focus more on the implementation details; the
programming language, parallel execution paradigm, discretization, and
mathematical support libraries.

### A repository for 'Hello CSE World' 
We are announcing the beginnings of an effort to populate and maintain a
repository of working implementations of the heat equation demonstrating various
aspects of CSE software. The resulting repository will be useful in training
about fundamental aspects of the design and development of CSE software as
well as provide examples of continuous integration testing including
demonstrating the use of ECP-CI resources.

Each implementation we gather will have to conform
to a *minimal* set of requirements including providing a fully self-contained
build, accommodating a common set of command-line arguments, producing ascii
text files for results output and providing ways to probe time and space performance
behavior via tools such as [PAPI](https://icl.utk.edu/papi/) or
[Caliper](https://software.llnl.gov/Caliper/).

Our goal in collecting such examples isn't so much to demonstrate the use of
different programming languages as it is to demonstrate different approaches
to computation and execution paradigms as well as provide instructive insights
by comparing of time, space, and scaling performance of various approaches.

As a precursor to that effort, we have begun collecting, documenting, and
articulating similarities and differences of various
[code snipits](https://github.com/betterscientificsoftware/hello-heat-equation)
in a *temporary* repository.

## Conclusion
The Heat Equation is well known and has many practical applications even in
its one dimensional form. Because of this, a variety of implementations are
easily available. This exemplar PDE makes it the perfect "Hello World!" for
the scientific software community. Collecting a number of working examples
together with unique implementation characteristics will help to create 
useful introductory CSE training material.

## Author bios

Heather M. Switzer is working as a computing summer intern at Lawrence Livermore National Laboratory. She graduated with her B.S. in Mathematics and Computer Science from Longwood University in 2018 and is currently a 2nd-year M.S./Ph.D. student in Computer Science with a specialization in Computational Science at the College of William & Mary.

Elsa Gonsiorowski is an HPC I/O Specialist at Lawrence Livermore National Laboratory. She graduated with her Ph.D. in Computer Science in 2016 from Rensselaer Polytechnic Institute. Elsa works on a number of open source, system software tools to support HPC users as they manage files across an increasingly complex storage hierarchy. She has a passion for useful documentation and CMake.

Mark C. Miller is a computer scientist at Lawrence Livermore National Laboratory supporting
[VisIt](https:/visit.llnl.gov), [Silo](https://silo.llnl.gov), and other visualization and
data infrastructure for LLNL simulation codes.

<!---
Publish: preview
RSS update:
Categories: Planning, Development
Topics: Software Engineering, Development Tools
Tags:
Level:
Prerequisites: default
Aggregate:
--->
