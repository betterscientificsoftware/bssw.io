# Rethinking Software Variants

 **Hero Image:**
 
  - [WarpX: longitudinal electric field in a laser-plasma accelerator, rendered with Ascent and VTK-m.]<img src='../../images/Blog_2209_SoftwareVariants_WarpX.png' />

#### Contributed by: [Axel Huebl](https://github.com/ax3l)

#### Publication date: September 27, 2022

### Introduction

Configuration options of a software package are selected in the installation phase of software: to be precise the configuration and compilation phase.
As a result, they cannot be changed without reinstalling the software.

These days, nearly all high-performance computing (HPC) software uses configuration options and most of the time, these are implemented via pre-processor logic, i.e., using `#ifdef`s in C/C++/Fortran code.
It is extremely common that these switches are implemented exclusively, creating incompatible variants and binaries.
Here, we argue that this can have severe productivity implications for users and developers alike, including documentation and installation burdens, usability, testing overhead, and limited composability - and show potential solutions for a better binary variant design for HPC.

### HPC examples

The most common pattern of variations for HPC software are options for parallelism.
In the simplest case, this is a flag that enables or disables MPI support in the software.
With the rise of GPU computing over the last decade, a similar option is often added for GPU acceleration.

Library and application developers in HPC might then add further more domain-specific compilation options, such as:
- additional numerical solvers supported by external math libraries, e.g., BLAS/LAPACK/FFT
- choices of geometry of a model

[Some of the WarpX compile-time options exposed in the Spack package manager.]<img src='../../images/Blog_2209_SoftwareVariants_Spack.png' />

### The catch

There are generally two was of implementing such configuration options at build-time: boolean switches and multi-variant options.
Binary switches are simply turning a functionality on or off, e.g., MPI support.
Multi-variant options might be more involved, e.g., accelerating code for a specific GPU programming environment (CUDA/HIP/SYCL/OpenMP or OpenACC offloading).

The catch with such options lies in sharing software with other people who want to re-use it in their own libraries and applications, develop against it, and deploy their own product to other developers and users.
My experience is that problems for developers of "downstream" HPC software arise mainly from the implementation of these options.

For instance, runtime options that change with the chosen binary option need to be carefully documented for users/downstream developers - and complicate user experience in already tricky installations.
Workflows have to be established when switching functionality downstream: do you change configuration of the upstream dependency and re-build/re-install? Do you find and use the new variant of the dependency that is packaged separately?
Testing also gets more complicated: if you cannot create a single environment that enables and tests all functionality, you might need to recompile significant portions of the software stack to enable different tests.
Even with sufficient automation, the this increases continuous integration time and deployment resources.

A few specific examples will help illustrate the challenges.

#### Breaking public APIs

Without due care, it is easy for scattered `#ifdef` switches to end up changing public APIs that downstream applications may depend upon: extra parameters in functions, different class signatures and constructors, varying members, etc.
In the most common case in HPC, the change of the upstream option has to be mirrored 1:1 downstream with `#ifdef`s at call locations, because existing signatures are *changed*.

Such API changes also always lead to incompatible application binary interfaces (ABIs) when building library interfaces.
In the best case, the linker will catch an incompatible binary variant of the same software version via missing symbol errors.

In the worst case, a more subtle ABI break will only manifest at runtime.
For example, the addition/removal/exchange of member variables of public classes via `#ifdef`s can, even if these members are private, create undefined behavior when copying or accessing the class.
The homepage [ABI Laboratory](https://abi-laboratory.pro) summarizes more details on this topic.
For examples that track potentially breaking ABI changes over time, see for instance [MPICH](https://abi-laboratory.pro/index.php?view=timeline&l=mpich), [OpenMPI](https://abi-laboratory.pro/index.php?view=timeline&l=openmpi) and [c-blosc](https://abi-laboratory.pro/index.php?view=timeline&l=c-blosc).


#### The transitive MPI include

Adding transitive `#include`s to third party software in public APIs is one of the most common mistake in HPC binary variant design.
The problem can be exemplified as follows:
A developer writes a serial program using an HPC-capable third-party software package, e.g., to support desktop users or non-MPI based multi-node parallelism.
The third-party software can be build with MPI enabled, and now introduces a compile-time dependency on MPI signatures even though the specific downstream translation unit never uses it.

The results include breaking builds, the need to communicate additional, potentially inaccurate (unused) dependencies, and breakage in most desktop package managers.
A typical example is Debian and HDF5: you cannot install a MPI-parallel HDF5 package for development and the popular, serial HDFView package at the same time.

#### The unconditional MPI initialize (or expectation thereof)

This is variation of the previous problem, which occurs at runtime as a result of an MPI binary variant.
If the MPI-enabled variant of the software *expects* that an MPI context will always be provided (or can be established), this breaks serial software applications.

One can make the same case for any other runtime that needs to be initialized/finalized, such as (un)conditional initialization of GPU devices, GPU streams, etc.

#### On-node acceleration

Going into more detail on the previous point, a cardinal pattern in HPC software is to define mutually exclusive binary pattern for the "acceleration backend" of software.
Many single-source performance-portability implementations currently compile to exactly one on-node acceleration backend at a time.

For example, one might compile a numerical package to run with a CUDA backend.
Or compile it again with an OpenMP backend.
Or with a HIP/ROCm backend, etc.

Delegating this decision to compile-time takes away the choice to deploy binary packages or pre-build unified containers that could run on various GPU vendor hardware or be run on CPU or GPU as a runtime option, depending on user-need.
It also hinders dependent developments that want to utilize CPU and GPU at the same time, e.g., in simulations with dynamic load balancing.

So called "fat binary" artifacts can address this problem in part, by compiling multiple backends into the same executable and delegating the code path to choose to runtime.
Unfortunately, there are currently little established conventions and tooling for such an approach, especially across different vendors.

### Possible solutions and development policies

The solution to these challenges starts with everyone thinking of themselves as "upstream" developers and thinking about how downstream users might reuse their software.
This even includes application developers: someone might come up with a clever way to integrate an application - like a library - into a larger context, e.g., for optimization of ensemble use cases or AI/ML workflows.

We propose the following guidelines or development policies when introducing binary variants into a software.

1. Strict extension-only: using compilation variants only for adding *additional* functionality - a variant *enhances* a package with extra functionality.
    - rationale: the primary reason for this pattern is to disable dependencies for simplified development & deployment

2. Avoid exclusive compilation options:
    - variants that enable functionality at the cost of disabling another, e.g., `#ifdef FOUND_MPI ... #else ...`,
    - *multi-options* should be treated as lists of functionality
      - e.g., compile multiple variants of CPU and GPU backends that can be selected at runtime,
      - this can still make use of single-source programming patterns and just needs an additional runtime dispatch at a high-level in the program workflow, where latency is usually not an issue,
      - similar solutions also exist already for runtime-dispatched vectorization control.
    - rationale: avoids incompatibilities, supports feature-complete deployments and enhances clarity in documentation

3. Avoid modifying the "base" behavior of the software if additional functionality is activated - existing functionality and dependencies, at compile and runtime, stays unchanged.
    - rationale: supports feature-complete deployments and enhances clarity in documentation

4. Add explicit configuration and runtime control to use such opt-in functionality/enhancements.
    - rationale: avoids implicit assumptions that do not necessarily hold true when combined in a combined software ecosystem

### Package managers

But hey, don't we have package managers to solve this problem for us by keeping track of the right variant?
Well, in part.
Of course, modern package managers like Spack allow developers to define various development environments with exactly chosen and combined variants of software.
This is helpful for correct results.
Yet, if one needs to use all features of a software, this results in a combinatorial explosion of artifacts for development environments and deployments.
On top of that, most package managers do not support binary variants at all - and are adding them as afterthoughts via package naming extensions, again combinatorial installs and require complex conflict resolutions.

Indeed, independent if a package manager supports binary variants well, it is tremendously helpful if a package manager with great dependency resolution can just switch all options that are *potentially* useful for a system to "ON" (or selected) at the same time.
Consequently, there are fewer modules to build, no environment switching is needed for development, and binary caches can be smaller.

### Hands-on examples

#### C/C++

The following design patterns can be used for C/C++ code.

**Header:** Selected opt-in variants should add *extra* header files that expose additional classes, API calls and expose functionality like MPI-enabled signatures.
This means at least one public "facade" header is needed per configuration option, to avoid "polluting" base functionality with third party includes.
  - Examples:
    - [pybind11/numpy.h](https://pybind11.readthedocs.io/en/stable/advanced/pycpp/numpy.html#arrays)
    - an additional public API header with separate classes & functions for MPI-related functionality

**Configuration:** An extra configuration header file that provides defines for enabled and disabled opt-in functionality should be used.
Likewise, a mirrored runtime API should be available to query these options.
This avoids propagating options solely through build systems, making downstream consumers agnostic of them, and avoids the need to clutter command lines with defines.
  - Examples:
    - [AMReX_Config.H](https://github.com/AMReX-Codes/amrex/blob/22.09/Tools/CMake/AMReX_Config.H.in)
    - [openPMD/config.hpp](https://github.com/openPMD/openPMD-api/blob/0.14.5/include/openPMD/config.hpp.in)
  - Note: avoid changing variables in these files, [e.g. Git hashes or build time](https://github.com/AMReX-Codes/amrex/pull/2653), to avoid interference with productivity tools such as [CCache](https://ccache.dev)

**CMake:** For multiple variants, [allow lists](https://www.kitware.com/constraining-values-with-comboboxes-in-cmake-cmake-gui/) instead of either-or selections.
  - Don't:
    ```cmake
    set(App_Backend "OpenMP" CACHE STRING
        "On-node, accelerated computing backend")

    set(App_Backend_Values "omp;cuda;hip;sycl;none" CACHE INTERNAL
        "List of possible values for the Language cache variable")

    set_property(CACHE App_Backend PROPERTY STRINGS ${App_Backend_Values})
    ```
  - Do:
    ```cmake
    set(App_Backend "OpenMP;CUDA" CACHE STRING
        "On-node, accelerated computing backend")
    ```

#### Python and Fortran

The following design patterns can be used for Python and Fortran code.

**Modules:** Providing extra (sub-)modules that expose functionality that expects or creates a certain runtime context, e.g., MPI-parallelism.

**Properties:** Adding a properties to the base module to allow querying which opt-in functions are available at runtime.

### Modifications of WarpX

Over the last two years, we redesigned most binary options of the Exascale Computing Project application [WarpX](https://ecp-warpx.github.io) based on these experiences and insights.
We changed binary options that control additional fields solvers that require FFTs and linear algebra to provide additional runtime options when enabled, and without changing application behavior if compiled and not used.

More complicated are changes in simulation geometry.
Ideally, WarpX developers would like to offer users a single deployment that provides 1D, 2D, 3D and quasi-cylindrical (RZ) geometry at the same time.
In AMReX, this is a compile-time option.

We are addressing this by progressively compiling all geometries "as 3D" and adding additional 1D and 2D calls to parallel kernel primitives in AMReX' 3D interfaces.
Until then, we increased usability by mirroring the compile time option as runtime user input, which allows us to throw clean error messages, and compiling multiple runtime libraries per geometry for our Python bindings - which moves the task of a one-time dispatch to the Python level after reading the inputs file.

### Summary

Configuration variants are a common pattern in software design and in HPC software in particular.
They are often expressed via `#ifdef`s and seen as an efficient way to reuse and extend already written code.
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
--->
