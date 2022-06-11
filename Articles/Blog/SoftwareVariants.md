# Rethinking Software Variants

 **Hero Image:**
 
  - <img src='../../images/Blog_SoftwareVariants.png' />

#### Contributed by: [Axel Huebl](https://github.com/ax3l)

## Introduction

Configuration options of a software package are selected in the installation phase of software: to be precise the configuration and compilation phase.
As a result, they cannot be changed without reinstalling the software.

As of today, nearly all high-performance computing (HPC) software uses configuration options and most of the time, these are implemented via pre-processor logic, i.e., using `#ifdef`s in C/C++/Fortran code.
It is extremely common that these switches are implemented as mutually exclusive pattern, creating incompatible variants and binaries.
Here, we argue that this can have severe productivity implications for users and developers alike, ranging from documentation and installation burdens, usability, testing overhead up to limited composability - and show potential solutions for a better binary variant design for HPC.

## HPC Examples

The most common pattern for HPC software are the options for parallelism.
In the simplest case, this is a flag that enables or disables MPI support for the software.
With the rise of GPU-computing over the last decade, a similar option is often added for GPU acceleration.

Library and application developers in HPC might then add further more domain-specific compilation options, such as:
- additional numerical solvers supported by external math libraries, e.g., BLAS/LAPACK/FFT
- choices of geometry of a model

## Motivation / The Catch (multiple)

Binary options can be as colorful as the creativity of the developer that writes them.
There are generally two options: boolean switches and multi-variant options.
Binary switches are simply turning a functionality on/off, e.g., MPI support.
Multi-variant options might be more involved, e.g., accelerating code for a specific GPU programming environment (CUDA/HIP/SYCL/OpenMP or OpenACC offloading).

The catch with such options lies in sharing software with other people that like to re-use it in their own libraries and applications, develop against it and deploy their own product further to other developers and users.
Problems for "downstream" depending developers of HPC software arise mainly from the implementation of these options.

For instance, runtime options that change with the choosen binary option need to be documented to users/downstream developers - and complicate user experience in already tricky installations.
Workflows have to be established when switching functionality downstream: change the software itself and install, find and use another variant of upstream packages.
Testing gets more complicated: full recompilations are needed of vast parts of the software stack if one cannot create a single environment that enables and tests all functionality, because it might conflict.
Even with sufficient automation, the latter increases continuous integration time and deployment resources.

Typical problems shall be illustrated in a few examples.

### Breaking Public API

A common issues from quickly scattered `#ifdef` switches are changing API interfaces: extra parameters in functions, different class signatures and constructors, varying members.
In the worst case, the change of the upstream option has to be mirrored 1:1 downstream with `#ifdef`s at call locations, e.g., because existing signatures are *changed*.

Such API changes also always lead to incompatible application binary interfaces (ABIs).
Likewise, it is easy to introduce breaking ABI changes that are more subtle, which will result in linkage failures for a new variant at best and subtle breakage at runtime in the worst case.
A typical example is the manipulation of the number of member variables of a public class based on a binary variant.

### The Transitive MPI Include

Adding transitive `#include`s to third party software in public APIs is one of the most common mistake in HPC binary variant design.
The problem can be exemplified as follows:
A developer writes a serial program using an HPC-capable third party software, e.g., to support desktop users or non-MPI based multi-node parallelism.
The third party software can be build with MPI enabled, and now introduces a compile-time dependency on MPI signatures even though the specific downstream translation unit never uses it.

The result are breaking builds, need to communicate additional, potentially unused dependencies and breakage in most desktop package managers.
A typical example is Debian and HDF5: you cannot install a MPI-parallel HDF5 package for development and the popular, serial HDFView package at the same time.

### The Unconditional MPI Initialize (or expectance thereof)

This is variation of the previous problem, which occurs at runtime as a result of an MPI binary variant.
If the MPI-enabled variant of the software *expects* that an MPI context will always be provided (or can be established), this breaks serial software applications.

One can make the same case for GPU context controls and any other runtime that needs to be initialized/finalized.

### On-Node Acceleration

Speaking of GPU contexts, the next cardinal pattern in HPC software is a mutually exclusive binary pattern for the "acceleration backend" of software.
This can be parallel threading or offloading.

Although it is not necessary to implement it that way, especially single-source implementations currently compile to exactly one on-node acceleration backend.
This takes away the choice to deploy binary packages or pre-build containers that could run on various GPU vendor hardware or be run on CPU or GPU as a runtime option, depending on user-need.

## Possible Solutions & Development Policies

The solution lie with "upstream" developers, so everyone that intends to publish software that shall be reused by someone else.
On a personal note, this includes even application developers - since someone might come up with a clever way to integrate an application again into another framework, e.g., for optimization of ensemble use cases or AI/ML workflows.

We propose the following guidance (or development policies) to take into account when introducing binary variants into a software.

#. Strict extension-only: using binary variants only for adding *additional* functionality
  - a variant *enhances* a package with extra functionality

#. Avoiding exclusive options:
  - variants that enable functionality at the cost of disabling another, e.g., `#ifdef FOUND_MPI ... #else ...`
  - *multi-options* should be treated as lists of functionality
    - e.g., compile multiple variants of CPU and GPU backends that can be selected at runtime
    - this can still make use of single-source programming patterns and just needs an additional runtime dispatch at a high-level in the program workflow, where latency is usually not an issue
    - similar solutions also exist already for runtime-dispatched vectorization control

#. Avoiding modifying the "base" behavior of the software if additional functionality is activated
  - existing functionality and dependencies, at compile and runtime, stays unchanged

#. add explicit configuration and runtime control to use such opt-in functionality/enhancements

## Package Managers

But hey, don't we have package managers to solve this problem for us by keeping track of the right variant?
Well, in part.
Of course, modern package managers like Spack allow developers to define various development environments with exactly chosen and combined variants of software.
This is helpful for correct results, but results in a combinatoric explosion for development environments and deployments.
But most package managers simply do not support binary variants at all - adding them as afterthoughts via package naming extensions, again combinatoric installs and complex conflict resolutions.

Indeed, independent if a package manager supports binary variants well, it is tremendously helpful if a package manager with great dependency resolution can just switch all options that are *potentially* useful for a system to "ON" (or selected) at the same time.
Less modules to build, no switching for development, and smaller binary caches to build.

## Hands-On Examples

### C/C++

The following design patterns can be used for C/C++ code.

**Header:** Selected opt-in variants should add *extra* header files that expose additional classes, API calls and expose functionality like MPI-enabled signatures.
This means at least one public "facade" header is needed per confiugration option, to avoid "polluting" base functionality with third party includes.

**Configuration:** An extra configuration header file that provides defines for enabled and disabled opt-in functionality should be used.
Likewise, a mirrored runtime API should be available to query these options.
This avoids propagating options solely through build systems, making downstream consumers agnostic of them, and cuttering command lines with defines.

**CMake:** For multiple variants, allow lists instead of either-or selections.

### Python and Fortran

The following design patterns can be used for Python and Fortran code.

**Modules:** Providing extra (sub)-modules that expose functionality that expects or creates a certain runtime context, e.g., MPI-parallelism.

**Properties:** Adding a properties to the base module to allow querying which opt-in functions are available at runtime.

## Modifications of WarpX

Over the last two years, we redesigned most binary options of the Exascale Computing Project application [WarpX](https://ecp-warpx.github.io) based on these experiences and insights.
We changed binary options that control additional fields solvers that require FFTs and linear algebra to provide additional runtime options when enabled, and without changing application behavior if compiled and not used.

More complicated are changes in simulation geometry, where currently a 1:1 dependency on AMReX geometry exists.
We are addressing this by progressively compiling all geometries "as 3D" and adding additional 1D and 2D calls to parallel kernel primitives in AMReX' 3D interfaces.
Until then, we increased usability by mirroring the compile time option as runtime user input, which allows to throw clean error messages, and compiling multiple runtime libraries per geometry for our Python bindings - which moves the task of a one-time dispatch to the Python level after reading the inputs file.

## Summary

Configuration variants are a common pattern in software design and in HPC software in particular.
They are quickly introduced via `#ifdef`s and often seen as an efficient way to reuse and extend already written code.
This leads to incompatible software variants for downstream developers and users.

Although modern package managers assist with the control of variants and modern build systems allow to propagate options at configuration time, the problem of a combinatoric explosion continues to exist and complicates user-friendly deployments.

Designing binary variants as strict extensions without breaking API and runtime behavior once selected is a way to address this problem.
As a result, deployment is simpler, development against multiple variants is faster, testing time can be reduced, and documentations can be simplified.

### Author Bio
 
[Axel Huebl](https://orcid.org/0000-0003-1943-7141) is a Computational Physicist working at the Accelerator Technology & Applied Physics Division at Berkeley Lab.
He works on Exascale modeling of particle accelerators, especially plasma-based accelerator concepts, self-describing I/O via the [openPMD](https://www.openPMD.org) meta-data standard, data reduction and in situ algorithms, and developer productivity.

<!---
Publish: yes
Pinned: no
Topics: design, performance portability, high-performance computing (hpc), testing, Software Engineering
RSS update: 2022-06-11
--->
