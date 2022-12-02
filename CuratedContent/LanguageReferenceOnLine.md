# Fundamental Resources for Scientific Computing
<!--deck text start-->
This article hosts a number of online documentation resources of fundamental importance in HPC/CSE.
<!--deck text end-->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86 "Mark C. Miller GitHub Profile")
#### Publication date: December 02, 2022

This article hosts a number of online documentation resources of fundamental importance in HPC/CSE.

We begin with the most fundamental of topics - formal specifications and standards for programming *languages* most commonly used in HPC/CSE.
These are formal documents primarily for implementors of compilers that define, in excruciating detail, how programs in the language are supposed to behave and attempt to cover all possible *corner* cases.
Language specifications evolve with time and so are versioned, typically by the year, in which the new specification is *initiated*.
But not all languages commonly used in HPC/CSE, notably Python, are defined by a *formal specification*.
Instead, they rely solely on a [*reference implementation*](https://en.wikipedia.org/wiki/Reference_implementation).
Python's reference implementation is [CPython](https://en.wikipedia.org/wiki/CPython).

From formal specifications, we move on to language *implementations*.
The *implementation* of a programming language is typically embodied in a [compiler](https://en.wikipedia.org/wiki/List_of_compilers) or, for interpretive languages like Python (or Basic), an *interpreter*.
The relevant documentation takes the form of compiler reference manuals.
A key bit of information compiler reference manuals provide is how a compiler may deviate from the standard it implements.

A program consisting solely of language statements typically does not make a useful application.
Useful applications need to interact with the outside world...memory, a terminal display, disk files, etc.
This functionality is typically provided in the form of an accompanying *standard library*...a set of function calls with *well defined interfaces* that do things like allocate and free memory, open and close files, read and write data, etc.

A challenge with standard libraries is that they aren't always very *standard*.
Different hardware vendors provide different and sometimes incompatible implementations.
[POSIX](https://en.wikipedia.org/wiki/POSIX) compliance was introduced in the 1990's to address this not only for the C standard library but also for many other aspects of how programs and humans (e.g. command-line *shells*) interact with an operating system.

As new hardware is introduced, its kinda sorta useless if there doesn't exist any compilers that produce executable (binary) code that runs on that hardware (and takes maximal advantage of any of its unique features).
Therefore, hardware vendors are more or less obliged to provide a compiler that supports their hardware.
No applications can use their hardware without one.
Often, hardware vendors develop and support their own *native* (and proprietary) compilers.
This ensures applications are maximally performant on their hardware.
Alternatively (or sometimes additionally), existing compilers are enhanced to target performance features of the vendor's hardware. Notably, GNU, Intel, Portland Group and Clang compilers are not tied to any particular hardware vendor.
These compilers are often made available on various vendor's hardware and in some cases can even produce higher performing code than the hardware vendor's *native* compiler.

It can take many years for compiler vendors to update their implementations to conform to new language standards.
It is not uncommon for a language/compiler reference manual or standard library to depart from a formal language specification in various minor ways especially during a period in which it is transitioning to new language standard.
For example, the GNU compiler collection (GCC) often supports a number of [language *extensions*](https://gcc.gnu.org/onlinedocs/gcc/C-Extensions.html) some of which eventually make their way into the formal language standard.
The use of language features unique to a specific standard and/or compiler can introduce portability issues.
To avoid such possibilities, projects often constrain which language standards and compiler versions they agree to use and support.
The [VisIt](https://visit-dav.github.io/visit-website/) project decided to permit C++11 constructs (specific to the 2011 C++ standard) into the code base only in 2018, a full 7 years after the language standard had been released.

Perhaps the next most fundamental aspect of scientific computing after languages, compilers and standard libraries is parallelism; the decomposition of a single, large computing task into many smaller tasks that execute simultaneously on separate copies of hardware resources.
Parallelism can manifest in a myriad of ways in both hardware and software creating significant portability challenges.
Nonetheless, one critical differentiator is [shared memory vs. distributed memory](https://en.wikipedia.org/wiki/Distributed_memory) parallelism.
Another critical differentiator is whether parallelism manifests as the same computational task running simultaneously everywhere except on different data (e.g. [Data parallelism](https://en.wikipedia.org/wiki/Data_parallelism)) or something more generalized than this where computational tasks which can be wholly disparate are queued and divvied out to resources as they become available (e.g. Task parallelism).
A number of technologies are aimed at addressing portability challenges.
Though their key aim is portability of parallelism, these technologies are referred to as *performance portability* solutions.

We round out this discussion of resources by identifying several other commonly used technologies that are available in the form of either *language extensions* or application programming interfaces (APIs) to third party libraries.
Sometimes whether a technology is considered a *language extension* or an *API* isn't always very clear cut.
That said, API's are also sometimes decomposed into two pieces - a *specification* piece and an *implementation* piece.
This is entirely analogous to programming language specification and implementation described above.
The canonical example of an API that is managed in this way is the [Message Passing Interface (MPI)](https://www.mpi-forum.org/).
Another example is [OpenGL](https://www.opengl.org/), a graphics programming API (the *L* in OpenGL stands for *Library* but many often treat it as thought it stands for *Language*).
The MPI API has evolved with time and so has multiple specifications, each versioned.
The most currently agreed upon MPI interface specification is version 4.0.
But, there are a number of earlier interface specifications as well.
[MPICH](https://www.mpich.org/) serves as a *reference* implementation of MPI.

Finally, we end with a handful of other miscellaneous programming technologies commonly encountered when contributing to HPC/CSE code projects.

---

Programming<br>Technology | Versions, Variants<br>and/or Vendors | Other notes
:---: | :---: | ---:
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Formal Language Specifications and Standards**</td></tr>
C | [89][c89-spec]/[99][c99-spec]/[11][c11-spec]/[18][c18-spec] | ([1][1])
C++ | [03][c++03-spec]/[11][c++11-spec]/[14][c++14-spec]/[17][c++17-spec]/[20][c++20-spec] | ([1][1])
CPP | Part of C specification | ([4][4])
Fortran | [77][f77-spec]/[90][f90-spec]/[95][f95-spec]/[03][f03-spec]/[08][f08-spec]/[18][f18-spec] | ([1][1])
OpenCL | [1.2][ocl1.2-spec]/[2.2][ocl2.2-spec]/[3.0][ocl3.0-spec] | ([2][2])
Python | [2][py2-spec]/[3][py3-spec]| ([3][3])
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Language Implementations - Compiler Reference Manuals**</td></tr>
C | [MS][c-ms]/[IBM][c-ibm]/[GNU][c-gnu]/[Cray][c-cray]/[LLVM][c-clang]/[AMD][c-amd]/[Intel][c++-intel]
C++ | [AMD][c++-amd]/[MS][c++-ms]/[IBM][c++-ibm]/[LLVM][c++-clang]/[Cray][c++-cray]/[Intel][c++-intel]|
CPP | Usually part of C implementation<br>[GNU][cpp-gnu]/[MS][cpp-ms] |
Fortran | [PGI][f-pg]/[LF][f-lf]/[Intel][f-intel]/[Cray][f-cray]/[IBM][f-ibm]/[NAG][f-nag]/[GNU][f-gnu]
OpenCL | [NVIDIA][opencl-nvidia]/[AMD][opencl-amd]/[Intel][opencl-intel]|
Python | [2][py2]/[3][py3] |([3][3])
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Standard Library Reference**</td></tr>
C | [Gen][c-stdlib-0]/[GNU][c-stdlib-gnu]/[LLVM][c-stdlib-llvm]/[MS][c-stdlib-ms]/[IBM][c-stdlib-ibm] | |
C++ | [Gen][c++-stdlib-0]/[GNU][c++-stdlib-gnu]/[LLVM][c++-stdlib-llvm]/[MS][c++-stdlib-ms]/[IBM][c++-stdlib-ibm] | |
Fortran | [0.2.1][f-stdlib-0.2.1] | ([5][5])
Python | [2][py-stdlib-2]/[3][py-stdlib-3] | |
Implementations | [C][imp-stdlib-c]/[C++][imp-stdlib-c++] | |
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Parallelism**</td></tr>
Shared<br>Memory | [PThreads][smpar-pthreads]/[TBB][smpar-tbb]/[C++MT][smpar-c++mt]<br>[Cuda][smpar-cuda]/[HIP][smpar-hip] | ([6][6]) |
Distributed<br>Memory | MPI-[2.2][dmpar-mpi-2.2],[3.1][dmpar-mpi-3.1],[4.0][dmpar-mpi-4.0] (specification)<br>MPICH-[1.5][dmpar-mpich-1.5],[3.4][dmpar-mpich-3.4],[4.0.3][dmpar-mpich-4.0.3]/OpenMPI-[2.1][dmpar-ompi-2.1],[3.1][dmpar-ompi-3.1],[4.1][dmpar-ompi-4.1] | |
Data (SIMD) | [C++-17][pparc-stl]/[HPX][pparc-hpx]<br>[Thrust][pparc-thrust]/[RAJA][pparc-raja]/[Kokkos][ppard-kokkos]/[OpenMP][smpar-omp-5.2]/[openACC][smpar-openacc]<br>[GA][ppard-ga]/[SYCL][pparc-sycl]/[ROCm][pparc-rocm]/OpenCL-[1.2][ocl1.2-spec],[2.2][ocl2.2-spec],[3.0][ocl3.0-spec] | |
Task (MIMD) | [Charm++][ppard-charm++]/[Legion][ppard-legion] (libraries)<br>[Chapel][ppard-chapel]/[Julia][ppard-julia] (languages)||
I/O | [Posix][api-posixio]/[MIFIO][api-mifio]/[HDF5][api-hdf5-1.12]/[Lustre][api-lustre]/[GPFS][api-gpfs]<br>[MPI-IO][api-mpiio]/[DAOS][api-daos]/[Adios][api-adios]/[PnetCDF][api-pnetcdf]
File transfer | [sftp][api-sftp]/[scp][api-scp]<br>Big: [pftp][api-hpss]/[HPSS][api-hpss]/[Drive][api-gdrive]/[Globus][api-globus]/USPSnet
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**APIs and Tools**</td></tr>
Login shells | [bash][api-bash]/[zsh][api-zsh]/[tcsh][api-tcsh]/[ksh][api-ksh]
Secure<br>connectivity | [ssh][api-ssh]/[vpn][api-vpn]
Batch job<br>control | [Cobalt][api-cobalt]/[Slurm][api-slurm]/[Moab][api-moab]
System Calls | [Linux][api-sys-linux]/[POSIX][api-sys-posix]/[Windows][api-sys-windows] | |
Python | Extensions:[2][api-pyc-2],[3][api-pyc-3]/[NumPy][api-py-numpy] | |
Build and<br>Install | [make][api-make]/[gmake][api-gmake]/[AutoTools][api-autotools]/[CMake][api-cmake]/[Spack][api-spack]
Test | [ctest][api-ctest]/[GoogleTest][api-gtest] 
Meta data | [Yaml][api-yaml]/[Json][api-json]/[XML][api-xml]/[Conduit][api-conduit]
Raw data | [HDF5][api-hdf5]/[netCDF][api-netcdf]/[CGNS][api-cgns]/[Blueprint][api-blueprint]
Documentation | [LaTex][api-latex]/[GFM][api-gfm]/[reST][api-rest]/[Doxygen][api-doxygen]/[ReadTheDocs][api-rtd]/[GHPages][api-ghpages]
Version Control | [Git][api-git]/[Subversion][api-svn]/[GitLab][api-gitlab]/[GitHub][api-github]


[//]: # (Table footnotes. Text is dup'd for rendered HTML and balloon help)

[1]: #a1 "Version numbers are the last 2 digits of the year the standard was *initiated*. Sometimes, standards are formally *finalized* years after they were *initiated*."
[2]: #a2 "Language *extensions* for special devices (e.g. co-processors, GPUs, FPGAs, accelerators, etc.)."
[3]: #a3 "The most formal resource for Python is the [language reference](https://docs.python.org/dev/reference/) and the *reference* implementation, [CPython](https://github.com/python/cpython)"
[4]: #a4 "CPP is sometimes used to process other kinds of text files including those of other languages. CPP `#pragma` directives are a common way for compiler vendors to extend the language."
[5]: #a5 "The fortran specification does not define a *standard library*. Nonetheless, there is a community driven effort to develop one."
[6]: #a6 "A critical aspect of these technologies is whether they work on CPUs only, GPUs only or can *target* both. Some technologies are designed to target a variety of other *devices* such as FPGAs, etc."

<a name="a1"></a><sup>1</sup>Version numbers are the last 2 digits of the year the standard was *initiated*. Sometimes, standards are formally *finalized* years after they were *initiated*.<br>
<a name="a2"></a><sup>2</sup>Language *extensions* for special devices (e.g. co-processors, GPUs, FPGAs, accelerators, etc.).<br>
<a name="a3"></a><sup>3</sup>The most formal resource for Python is the *reference* implementation, [CPython](https://en.wikipedia.org/wiki/CPython)<br>
<a name="a4"></a><sup>4</sup>CPP is sometimes used to process other kinds of text files including those of other languages. CPP [`#pragma](https://gcc.gnu.org/onlinedocs/cpp/Pragmas.html) directives are a common way for compiler vendors to extend the language.<br>
<a name="a5"></a><sup>5</sup>The fortran specification does not define a *standard library*. Nonetheless, there is a community driven effort to develop one.<br>
<a name="a6"></a><sup>6</sup>A critical aspect of these technologies is whether they work on CPUs only, GPUs only or can *target* both. Some technologies are designed to target a variety of other *devices* such as FPGAs, etc.

[//]: # (Formal C language specification URLs)

[c89-spec]: http://port70.net/~nsz/c/c89/c89-draft.html
[c99-spec]: https://open-std.org/JTC1/SC22/WG14/www/docs/n1256.pdf
[c11-spec]: https://www.open-std.org/jtc1/sc22/WG14/www/docs/n1570.pdf
[c18-spec]: https://web.archive.org/web/20181230041359if_/http://www.open-std.org/jtc1/sc22/wg14/www/abq/c17_updated_proposed_fdis.pdf

[//]: # (Formal C++ language specification URLs)

[c++03-spec]: https://www.open-std.org/Jtc1/sc22/WG21/docs/papers/2001/n1316/
[c++11-spec]: https://www.open-std.org/Jtc1/sc22/WG21/docs/papers/2011/n3242.pdf
[c++14-spec]: https://www.open-std.org/Jtc1/sc22/WG21/docs/papers/2013/n3797.pdf
[c++17-spec]: https://www.open-std.org/Jtc1/sc22/WG21/docs/papers/2017/n4659.pdf
[c++20-spec]: https://www.open-std.org/Jtc1/sc22/WG21/docs/papers/2020/n4849.pdf

[//]: # (Formal Fortran language specification URLs)

[f77-spec]: https://web.archive.org/web/20070205092427/http://www.fortran.com/fortran/F77_std/rjcnf0001.html
[f90-spec]: https://wg5-fortran.org/N001-N1100/N692.pdf
[f95-spec]: https://wg5-fortran.org/N1151-N1200/N1191.pdf
[f03-spec]: https://wg5-fortran.org/N1601-N1650/N1601.pdf
[f08-spec]: https://j3-fortran.org/doc/year/10/10-007r1.pdf
[f18-spec]: https://j3-fortran.org/doc/year/18/18-007r1.pdf

[//]: # (OpenCL language specification URLs)

[ocl1.2-spec]: https://www.khronos.org/registry/OpenCL/specs/opencl-1.2.pdf
[ocl2.2-spec]: https://www.khronos.org/registry/OpenCL/specs/2.2/html/OpenCL_API.html
[ocl3.0-spec]: https://www.khronos.org/registry/OpenCL/specs/3.0-unified/html/OpenCL_C.html

[//]: # (Python language reference URLs)
[py2-spec]: https://docs.python.org/2/reference/
[py3-spec]: https://docs.python.org/3/reference/

[cpp-gnu]: https://gcc.gnu.org/onlinedocs/cpp/
[cpp-ms]: https://docs.microsoft.com/en-us/cpp/preprocessor/c-cpp-preprocessor-reference?view=msvc-170

[//]: # (C language reference URLs)

[c-gnu]: https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.pdf
[c-cray]: https://support.hpe.com/hpesc/public/docDisplay?docId=a00115116en_us&docLocale=en_US&page=The_Cray_Compiling_Environment.html
[c-ibm]: https://www.ibm.com/docs/en/ssw_ibm_i_71/rzarg/sc097852.pdf
[c-ms]: https://docs.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-170
[c-clang]: https://clang.llvm.org
[c-amd]: https://developer.amd.com/amd-aocc/

[//]: # (C++ language reference URLs)

[c++-intel]: https://www.intel.com/content/www/us/en/develop/documentation/cpp-compiler-developer-guide-and-reference/top.html
[c++-cray]: https://support.hpe.com/hpesc/public/docDisplay?docId=a00115116en_us&docLocale=en_US&page=The_Cray_Compiling_Environment.html
[c++-ibm]: https://www.ibm.com/docs/en/ssw_ibm_i_71/rzarg/sc097852.pdf
[c++-ms]: https://docs.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-170
[c++-amd]: https://developer.amd.com/amd-aocc/
[c++-clang]: https://clang.llvm.org/cxx_status.html

[//]: # (Fortran language reference URLs)

[f-pg]: https://www.pgroup.com/resources/docs/17.10/x86/fortran-ref-guide/index.htm "Portland Group Compilers"
[f-lf]: http://www.lahey.com/docs/LangRefEXP73_revG05.pdf "Lahey/Fujitsu Fortran 95"
[f-intel]: https://www.intel.com/content/www/us/en/develop/documentation/fortran-compiler-oneapi-dev-guide-and-reference/top/language-reference.html "All Fortran standards 90-18"
[f-cray]: https://support.hpe.com/hpesc/public/docDisplay?docId=a00115296en_us&page=About_the_Cray_Fortran_Reference_Manual.html
[f-ibm]: https://www.ibm.com/support/pages/system/files/support/swg/swgdocs.nsf/0/7e46ea600b6646d0852579dc00331978/$FILE/langref.pdf
[f-nag]: https://www.nag.com/nagware/np/r70_doc/compiler.pdf
[f-gnu]: https://devdocs.io/gnu_fortran/

[//]: # (GPU language reference URLs)

[opencl-amd]: https://rocmdocs.amd.com/en/latest/Programming_Guides/Opencl-programming-guide.html#opencl-programming-guide
[opencl-intel]: https://www.intel.com/content/www/us/en/develop/documentation/iocl_rt_ref/top.html
[opencl-nvidia]: https://developer.download.nvidia.com/compute/DevZone/docs/html/OpenCL/doc/OpenCL_Programming_Guide.pdf

[//]: # (Pythone language reference URLs)

[py2]: https://docs.python.org/2/reference/
[py3]: https://docs.python.org/3/reference/

[//]: # (Standard libraries)

[c-stdlib-0]: https://cplusplus.com/reference/clibrary/
[c++-stdlib-0]: https://www.cplusplus.com/reference/
[c-stdlib-gnu]: https://gcc.gnu.org/onlinedocs/libc/
[c++-stdlib-gnu]: https://gcc.gnu.org/onlinedocs/libstdc++/
[c-stdlib-llvm]: https://libc.llvm.org/
[c++-stdlib-llvm]: https://libcxx.llvm.org/
[c-stdlib-ms]: https://learn.microsoft.com/en-us/cpp/c-runtime-library/c-run-time-library-reference?view=msvc-170
[c++-stdlib-ms]: https://docs.microsoft.com/en-us/cpp/standard-library/cpp-standard-library-reference?view=msvc-170
[c-stdlib-ibm]: https://www.ibm.com/docs/en/i/7.3?topic=c-ile-cc-runtime-library-functions
[c++-stdlib-ibm]: https://www.ibm.com/docs/en/i/7.3?topic=c-ile-cc-runtime-library-functions
[py-stdlib-2]: https://docs.python.org/2.7/library/
[py-stdlib-3]: https://docs.python.org/3.8/library/
[f-stdlib-0.2.1]: https://github.com/fortran-lang/stdlib
[imp-stdlib-c]: https://en.wikipedia.org/wiki/C_standard_library#Implementations
[imp-stdlib-c++]: https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library#Implementations

[//]: # (Shared Memory Parallelism)

[smpar-pthreads]: https://hpc-tutorials.llnl.gov/posix/AppendixA/
[smpar-tbb]: https://spec.oneapi.io/versions/latest/elements/oneTBB/source/nested-index.html
[smpar-c++mt]: https://cplusplus.com/reference/multithreading/
[smpar-cuda]: https://docs.nvidia.com/cuda/cuda-runtime-api/index.html
[smpar-hip]: https://github.com/RadeonOpenCompute/ROCm/raw/rocm-4.5.2/AMD_HIP_Programming_Guide.pdf
[smpar-omp-3.1]: https://www.openmp.org/wp-content/uploads/OpenMP3.1.pdf
[smpar-omp-4.5]: https://www.openmp.org/wp-content/uploads/openmp-4.5.pdf
[smpar-omp-5.2]: https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf
[smpar-openacc]: https://www.openacc.org/sites/default/files/inline-files/openacc-guide.pdf

[//]: # (Distributed Memory Parallelism)

[dmpar-mpi-1.3]: https://www.mpi-forum.org/docs/mpi-1.3/mpi-report-1.3-2008-05-30.pdf
[dmpar-mpi-2.2]: https://www.mpi-forum.org/docs/mpi-2.2/mpi22-report.pdf
[dmpar-mpi-3.1]: https://www.mpi-forum.org/docs/mpi-3.1/mpi31-report.pdf
[dmpar-mpi-4.0]: https://www.mpi-forum.org/docs/mpi-4.0/mpi40-report.pdf
[dmpar-mpich-1.5]: https://www.mpich.org/static/docs/v1.5.x/
[dmpar-mpich-3.4]: https://www.mpich.org/static/docs/v3.4.x/
[dmpar-mpich-4.0.3]: https://www.mpich.org/static/docs/v4.0.3/
[dmpar-ompi-4.1]: https://www.open-mpi.org/doc/v4.1/
[dmpar-ompi-4.0]: https://www.open-mpi.org/doc/v4.0/
[dmpar-ompi-3.1]: https://www.open-mpi.org/doc/v3.1/
[dmpar-ompi-2.1]: https://www.open-mpi.org/doc/v2.1/

[//]: # (Portable Parallelism via Abstract Code)

[pparc-stl]: https://en.cppreference.com/w/cpp/experimental/parallelism
[pparc-hpx]: https://hpx-docs.stellar-group.org/latest/html/index.html
[pparc-thrust]: https://thrust.github.io/doc/modules.html
[pparc-raja]: https://raja.readthedocs.io/en/develop/sphinx/user_guide/index.html
[pparc-sycl]: https://sycl.readthedocs.io/en/latest/
[pparc-rocm]: https://rocmdocs.amd.com/_/downloads/en/latest/pdf/

[//]: # (Portable Parallelism via Abstract Data)

[ppard-kokkos]: https://kokkos.org/programming-guide/
[ppard-ga]: https://hpc.pnl.gov/globalarrays/documentation.shtml
[ppard-legion]: https://legion.stanford.edu/pdfs/legion-manual.pdf
[ppard-charm++]: https://charm.readthedocs.io/en/latest/charm++/manual.html
[ppard-chapel]: https://chapel-lang.org/docs/language/spec/index.html
[ppard-julia]: https://julialang.org/blog/2019/07/multithreading/

[//]: # (Commonly used APIs)

[api-pyc-2]: https://docs.python.org/2.7/extending/extending.html 
[api-pyc-3]: https://docs.python.org/3.10/extending/extending.html
[api-py-numpy]: https://numpy.org/doc/stable/reference/index.html#reference
[api-sys-linux]: https://man7.org/linux/man-pages/man2/syscalls.2.html
[api-sys-posix]: https://docs.oracle.com/cd/E19048-01/chorus4/806-3328/6jcg1bm05/index.html
[api-sys-windows]: https://learn.microsoft.com/en-us/cpp/c-runtime-library/run-time-routines-by-category?view=msvc-170
[api-mifio]: https://www.hdfgroup.org/2017/03/mif-parallel-io-with-hdf5/
[api-posixio]: https://www.gnu.org/software/libc/manual/html_mono/libc.html#I_002fO-Overview
[api-hdf5-1.12]: https://docs.hdfgroup.org/hdf5/v1_12/index.html
[api-lustre]: https://doc.lustre.org/lustre_manual.xhtml#file_striping.lfs_setstripe
[api-gpfs]: https://www.ibm.com/docs/en/STXKQY_5.1.5/pdf/scale_cpr.pdf
[api-daos]: https://docs.daos.io/v2.2/user/workflow/
[api-adios]: https://adios2.readthedocs.io/en/latest/
[api-pnetcdf]: https://parallel-netcdf.github.io/wiki/Documentation.html
[api-mpiio]: https://www.mpi-forum.org/docs/mpi-4.0/mpi40-report.pdf?#page=683

[api-sftp]: https://access.redhat.com/articles/5594481
[api-scp]: https://www.computerhope.com/unix/scp.htm

[api-hpss]: https://www.hpss-collaboration.org/documents/HPSS_7.5.3_Users_Guide.pdf?#page=9
[api-gdrive]: https://support.google.com/a/users/answer/9282958?hl=en
[api-globus]: https://docs.globus.org/cli/


[api-zsh]: https://zsh.sourceforge.io/Guide/zshguide.html
[api-bash]: https://www.gnu.org/software/bash/manual/bash.html
[api-ksh]: https://docs.oracle.com/cd/E36784_01/html/E36870/ksh-1.html
[api-tcsh]: https://linux.die.net/man/1/tcsh

[api-ssh]: https://man.openbsd.org/ssh
[api-vpn]: https://en.wikipedia.org/wiki/Virtual_private_network

[api-make]: https://man7.org/linux/man-pages/man1/make.1p.html
[api-gmake]: https://www.gnu.org/software/make/manual/make.html
[api-cmake]: https://cmake.org/cmake/help/latest/
[api-spack]: https://spack.readthedocs.io/en/latest/
[api-autotools]: https://www.lrde.epita.fr/~adl/autotools.html

[api-ctest]: https://cmake.org/cmake/help/latest/manual/ctest.1.html
[api-gtest]: https://google.github.io/googletest/

[api-yaml]: https://yaml.org/spec/1.2.2/
[api-json]: https://www.json.org/json-en.html
[api-xml]: https://www.w3.org/TR/xml/
[api-conduit]: https://llnl-conduit.readthedocs.io/en/latest/index.html

[api-hdf5]: https://docs.hdfgroup.org/hdf5/v1_12/_r_m.html
[api-netcdf]: https://docs.unidata.ucar.edu/nug/current/
[api-cgns]: https://cgns.github.io/CGNS_docs_current/user/index.html
[api-blueprint]: https://llnl-conduit.readthedocs.io/en/latest/blueprint.html

[api-latex]: https://www.latex-project.org/help/documentation/
[api-gfm]: https://www.markdownguide.org/tools/github-pages/
[api-rest]: https://docutils.sourceforge.io/rst.html
[api-doxygen]: https://www.doxygen.nl/manual/
[api-rtd]: https://docs.readthedocs.io/en/stable/tutorial/
[api-ghpages]: https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages

[api-git]: https://git-scm.com/docs/user-manual
[api-svn]: https://svnbook.red-bean.com
[api-gitlab]: https://docs.gitlab.com
[api-github]: https://docs.github.com/en

[api-slurm]: https://slurm.schedmd.com
[api-cobalt]: https://trac.mcs.anl.gov/projects/cobalt/wiki/CommandReference
[api-moab]: https://iitj.ac.in/uploaded_docs/cc/HPC_training/mcmuserguide.pdf


<!---
Publish: yes
Pinned: no
RSS update: 2022-12-02
Topics: online learning
--->
