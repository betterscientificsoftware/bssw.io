# Understanding Interoperable Software Libraries
#### Contributed by [Lois Curfman McInnes](https://github.com/curfman), [Michael A. Heroux](https://github.com/maherou), [Barry Smith](https://github.com/BarrySmith), [Ulrike Meier Yang](https://github.com/ulrikeyang), Xiaoye Li
#### Publication date: Aug 6, 2019

<!-- deck start -->
Software libraries excel in delivering widely reusable, robust, efficient, and scalable solutions for high-performance computing. 
Delve into the pivotal role of these libraries in extreme-scale computational science, where collaborative efforts leverage independently developed tools to meet the multifaceted demands of predictive science.
<!-- deck end -->

As computational science increasingly incorporates multiscale and multiphysics modeling, simulation, and analysis, the combined use of software developed by independent groups has become imperative: no single team has resources for the full range of capabilities needed for predictive science and decision support.

**Software libraries** have proven effective in providing widely reusable software that is robust, efficient, and scalable for high-performance computing (HPC). 
Scientific application codes can employ library design principles to manage complexity and achieve optimal performance, whether the application software is intended for a single context or modest reuse across applications in the same domain (e.g., as **domain components**). 
This article discusses software library interoperability, or the ability of two or more libraries to be used together in an application code, without special effort on the part of the user. The document also introduces the Extreme-scale Scientific Software Development Kit (xSDK), a community endeavor focused on overcoming challenges in software interoperability and building the foundation of a scientific software ecosystem.

While the following discussion uses the terminology of software library interoperability, the concepts also apply to application-specific domain components.


## Software Libraries
A software library is a high-quality, encapsulated, documented, tested, and multiuse software collection that offers functionality commonly needed by application developers. 
Key advantages of software libraries include leveraging the expertise of library developers and reducing the effort required in application coding. 
For instance, numerical software libraries provide easy access to sophisticated mathematical algorithms and high-performance data structures developed by experts. 
This eliminates the need for application users to write complex code, allowing them to focus on their scientific domain software.

Libraries can provide control inversion through abstract interfaces, callbacks, or similar techniques, enabling the invocation of user-defined functionality by the library—such as a user-defined sparse matrix multiplication routine. 
They can also facilitate the construction of related specific objects that offer customizable behavior to enhance performance or flexibility. 
Additionally, libraries may incorporate domain-specific software components designed for use by multiple applications.

## Software Library Interoperability
Software library interoperability refers to the ability of two or more libraries to be used together in an application code, without special effort on the part of the user. 
For simplicity, we discuss interoperability between two libraries; extension to interoperability among three or more libraries is conceptually straightforward. 
Depending on application needs, various levels of interoperability can be considered:
  * **Interoperability level 1:** both libraries can be used (side by side) in an application.
  * **Interoperability level 2:** the libraries can exchange data (or control data) with each other.
  * **Interoperability level 3:** each library can call the other library to perform unique computations.

The simplest case (**interoperability level 1**) occurs when an application needs to call two distinct libraries for different functionalities (for example, an [MPI](https://www.mpi-forum.org/) library for message-passing
communication and [HDF5](https://www.hdfgroup.org/solutions/hdf5/) for data output). 
As discussed in [this talk](https://figshare.com/articles/Package_Management_Practices_Essential_for_Interoperability_Lessons_Learned_and_Strategies_Developed_for_FASTMath/789055), even this basic level of interoperability requires consistency among libraries to be used within the same application, in terms of compiler, compiler version/options, and other third-party capabilities. 
If both libraries have a dependence on a common third party, the libraries must be able to use a single common instance of it. 
For example, more than one version of the popular SuperLU linear solver library exists, and interfaces have evolved. 
If two libraries both use SuperLU, they must be able to work with the same version of SuperLU. 
In practice, installing multiple independently developed packages together can be a tedious trial-and-error process.

**Interoperability level 2** builds on level 1 by enabling conversion, or encapsulation, and exchange of data between libraries. 
This level can simplify use of libraries in sequence by an application.
In this case, the libraries themselves are typically used without internal modification to support the interoperability.

**Interoperability level 3** builds on level 2 by supporting the use of one library to provide functionality on behalf of another library. 
This level of interoperability provides significant value to application developers because they can access capabilities of additional libraries through the familiar interfaces of the first library.

## The Extreme-Scale Scientific Software Development Kit (xSDK)

<!-- <p align="left">
<img align="right" src="https://i.ibb.co/C9h43tR/Screen-Shot-2020-07-10-at-10-34-30-AM.png">
-->

A key aspect of work in the [IDEAS-Classic project](https://ideas-productivity.org/activities/ideas-classic/) is development of the [Extreme-scale Scientific Software Development Kit (xSDK)](http://xsdk.info/) - a collection of related and complementary software elements that provide the building blocks, tools, models, processes, and related artifacts for rapid and efficient development of high-quality applications.

#### xSDK community policies:
The xSDK addresses interoperability among the high-performance numerical libraries [hypre](https://computing.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods), [PETSc](https://www.mcs.anl.gov/petsc/), [SuperLU](crd.lbl.gov/%7Exiaoye/SuperLU/), and [Trilinos](https://trilinos.github.io/). 
The xSDK ensures level 1 interoperability for each xSDK library via a full-featured build script and testing environment and a collection of community policies. The following draft xSDK community policies address challenges in interoperability level 1.

 * **[xSDK package community policies:](https://figshare.com/articles/xSDK_Community_Package_Policies/4495136)** **A set of required policies** (including topics of configuring, installing, testing, use of MPI, portability, contact and version information, open source licensing, namespacing, and repository access) that a software package must satisfy in order to be considered **xSDK compatible**.
This designation informs potential users that the package can be easily used with other xSDK libraries and components.
Also presented are *recommended policies* (including topics of public repository access, error handling, freeing system resources, and library dependencies), which are encouraged but not required.
Similarly, a package can become an xSDK member package if (1) it is an xSDK-compatible package, ***and*** (2) it uses or can be used by another package in the xSDK, and the connecting interface is regularly tested for regressions.

 * **[xSDK community installation policies: GNU Autoconf and CMake options:](https://figshare.com/articles/xSDK_Community_Installation_Policies_GNU_Autoconf_and_CMake_Options/4495133)** **A standard subset of configure and CMake options for xSDK and other HPC packages** in order to make the configuration and installation as efficient as possible on standard Linux distributions and Mac OS, as well as on target machines at DOE computing facilities ([ALCF](https://www.alcf.anl.gov/), [NERSC](https://www.nersc.gov/), and [OLCF](https://www.olcf.ornl.gov/)).

The xSDK collection of software packages commits to adhere to these community policies in order to ensure compatibility with other packages that meet the same standards. 
The aim is to simplify the combined use of multiple independently developed software packages and to provide a foundation for addressing broader issues in interoperability and performance portability.

#### Deeper Levels
Deeper levels of xSDK interoperability involve exchanging, controlling, and interpreting data, as well as calling routines between libraries (interoperability levels 2 and 3 described above). 
Initial xSDK capabilities of hypre, PETSc, SuperLU, and Trilinos support interoperability among scalable linear solvers, so that applications can readily experiment with algorithms across multiple packages, in combination.
Forthcoming companion documents will explain approaches used for interfaces and adapters between packages as well as work on interoperability layers for other functionalities. 
A longer-term goal is collaboration among members of the HPC community to improve software interoperability as needed by extreme-scale computational science.

### Note: 
This document was prepared by the authors with contributions from all xSDK developers. This material is based upon work supported by the U.S. Department of Energy Office of Science, Advanced Scientific Computing Research and Biological and Environmental Research programs.

<!---
Publish: yes
Pinned: no
Track: how to
Topics: Software Interoperability
--->
