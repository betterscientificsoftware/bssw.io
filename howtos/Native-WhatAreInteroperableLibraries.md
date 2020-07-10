<div align="center">
<h1> What Are Interoperable Software Libraries? </h1>
<h3> Introducing the xSDK </h3>
<h4> The IDEAS Scientific Software Productivity Project </h4>
<h5> <a href="https://ideas-productivity.org/resources/howtos/">https://ideas-productivity.org/resources/howtos</a> </h5>
<h4> Contributed by: </h4>
</div>

## Background:

As extreme-scale computational science increasingly incorporates multiscale and
multiphysics modeling, simulation, and analysis, the combined use of software developed by
independent groups has become imperative: no single team has resources for the full range of
capabilities needed for predictive science and decision support. **Software libraries** have proven
effective in providing widely reusable software that is robust, efficient, and scalable for
high-performance computing (HPC). Moreover, scientific application codes can employ library
design principles to help manage complexity and achieve good performance, whether the
application software is intended for use in a single context or modest reuse across applications
in the same domain (e.g., as **domain components**). While the following discussion uses
terminology of software library interoperability, the concepts also apply to application-specific
domain components.

#### *Software Libraries*
A software library is a high-quality, encapsulated, documented, tested, and multiuse software
collection that provides functionality commonly needed by application developers. Key
advantages of software libraries include leverage of library developer expertise and reduced
application coding effort. For example, numerical software libraries provide easy access to
sophisticated mathematical algorithms and high-performance data structures that have been
developed by experts, so that application users do not need to write this complex code and can
instead focus on their scientific domain software.

Libraries can provide control inversion via abstract interfaces, call-backs, or similar techniques
such that user-defined functionality can be invoked by the library, for example, a user-defined
sparse matrix multiplication routine. Libraries can also facilitate construction of related specific
objects that provide customizable behavior to improve performance or flexibility. Moreover,
libraries can include domain-specific software components that are designed to be used by
more than one application.

#### *Software Library Interoperability*
Software library interoperability refers to the ability of two or more libraries to be used
together in an application code, without special effort on the part of the user. For simplicity, we
discuss interoperability between two libraries; extension to interoperability among three or more
libraries is conceptually straightforward. Depending on application needs, various levels of
interoperability can be considered:
  * **Interoperability level 1:** both libraries can be used (side by side) in an application
  * **Interoperability level 2:** the libraries can exchange data (or control data) with each
other
  * **Interoperability level 3:** each library can call the other library to perform unique
computations

The simplest case (**interoperability level 1**) occurs when an application needs to call two distinct
libraries for different functionalities (for example, an [MPI](https://www.mpi-forum.org/) library for message-passing
communication and [HDF5](https://www.hdfgroup.org/solutions/hdf5/) for data output). As discussed in [[1](https://figshare.com/articles/Package_Management_Practices_Essential_for_Interoperability_Lessons_Learned_and_Strategies_Developed_for_FASTMath/789055), [2](https://wci.llnl.gov/codes/smartlibs/UCRL-JRNL-208636.pdf)], even this basic level of
interoperability requires consistency among libraries to be used within the same application, in
terms of compiler, compiler version/options, and other third-party capabilities. If both libraries
have a dependence on a common third party, the libraries must be able to use a single common
instance of it. For example, more than one version of the popular SuperLU linear solver library
exists, and interfaces have evolved. If two libraries both use SuperLU, they must be able to
work with the same version of SuperLU. In practice, installing multiple independently developed
packages together can be a tedious trial-and-error process.

**Interoperability level 2** builds on level 1 by enabling conversion, or encapsulation, and exchange
of data between libraries. This level can simplify use of libraries in sequence by an application.
In this case, the libraries themselves are typically used without internal modification to support
the interoperability.

**Interoperability level 3** builds on level 2 by supporting the use of one library to provide
functionality on behalf of another library. This level of interoperability provides significant value
to application developers because they can access capabilities of additional libraries through
the familiar interfaces of the first library.

## The Extreme-Scale Scientific Software Development Kit (xSDK)
