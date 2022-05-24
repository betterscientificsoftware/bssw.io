# Programming Resources On Line
<!--deck text start-->
<!--deck text end-->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86 "Mark C. Miller GitHub Profile")

Programming<br>Technology | Versions, Variants<br>and/or Vendors | Other notes
:--- | :---: | ---:
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Formal Language Specifications and Standards**</td></tr>
C | [89][c89-spec]/[99][c99-spec]/[11][c11-spec]/[18][c18-spec] | Note 1
C++ | [03][c++03-spec]/[11][c++11-spec]/[14][c++14-spec]/[17][c++17-spec]/[20][c++20-spec] | Note 1
Fortran | [77][f77-spec]/[90][f90-spec]/[95][f95-spec]/[03][f03-spec]/[08][f08-spec]/[18][f18-spec] | Note 1
OpenCL | [1.2][ocl1.2-spec]/[2.2][ocl2.2-spec]/[3.0][ocl3.0-spec] | Language *extensions* for special devices<tr><td colspan=3 align="center">**Language/Compiler Reference Manuals**</td></tr>
C | [MS][c-ms]/[IBM][c-ibm]/[GNU][c-gnu]/[Cray][c-cray]
C++ | [MS][c++-ms]/[IBM][c++-ibm]/[Cray][c++-cray]/[Intel][c++-intel]|
Fortran | [PGI][f-pg]/[LF][f-lf]/[Intel][f-intel]/[Cray][f-cray]/[IBM][f-ibm]/[NAG][f-nag]/[GNU][f-gnu]
OpenCL | [NVIDIA][opencl-nvidia]/[AMD][opencl-amd]/[Intel][opencl-intel]|
Python | [2][py2]/[3][py3]
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Standard Libraries**</td></tr>
C Preprocessor | [GNU][cpp-gnu]/[MS][cpp-ms] |
C Standard Library | | |
C++ Standard Library | [0][c++-stdlib-0] |
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Accelerator Reference Manuals**</td></tr>
OpenCL | [Nvidia][]/[AMD][]/[Intel][]/[IBM][]/[ARM][]

<sup>1</sup>Version numbers are the last 2 digits of the year the standard was *initiated*. Sometimes, standards are formally *finalized* years after they were *initiated*.<br>
<sup>2</sup>Another note.

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


[cpp-gnu]: https://gcc.gnu.org/onlinedocs/cpp/
[cpp-ms]: https://docs.microsoft.com/en-us/cpp/preprocessor/c-cpp-preprocessor-reference?view=msvc-170

[//]: # (C language reference URLs)

[c-gnu]: https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.pdf
[c-cray]: https://support.hpe.com/hpesc/public/docDisplay?docId=a00115116en_us&docLocale=en_US&page=The_Cray_Compiling_Environment.html
[c-ibm]: https://www.ibm.com/docs/en/ssw_ibm_i_71/rzarg/sc097852.pdf
[c-ms]: https://docs.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-170

[//]: # (C++ language reference URLs)

[c++-intel]: https://www.intel.com/content/www/us/en/develop/documentation/cpp-compiler-developer-guide-and-reference/top.html
[c++-cray]: https://support.hpe.com/hpesc/public/docDisplay?docId=a00115116en_us&docLocale=en_US&page=The_Cray_Compiling_Environment.html
[c++-ibm]: https://www.ibm.com/docs/en/ssw_ibm_i_71/rzarg/sc097852.pdf
[c++-ms]: https://docs.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-170

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

[c++-stdlib-0]: https://www.cplusplus.com/reference/


### C, C++, C Pre-Processor

* C [Preprocessor]()|[Standard Library]()|

* [C Preprocessor](https://gcc.gnu.org/onlinedocs/cpp/)
* [Microsoft C, C++ and Assembler documentation](https://docs.microsoft.com/en-us/cpp/?view=msvc-170)
* [C++ Reference](https://en.cppreference.com/w/)
* [C++ Library Reference](https://www.cplusplus.com/reference/)
* [cplusplus.com](https://www.cplusplus.com)
* [C Standard Library Reference](https://www.cplusplus.com/reference/clibrary/)
* [Posix C Library](https://en.wikipedia.org/wiki/C_POSIX_library)
* [GNU C Reference Manaul](https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html)
* [GNU C Library Reference Manual](https://www.gnu.org/software/libc/manual/pdf/libc.pdf)
* [C Language Cheat Sheet](https://users.ece.utexas.edu/~adnan/c-refcard.pdf)

### Fortran

* [Fortran 77](https://docs.oracle.com/cd/E19957-01/805-4939/index.html)
* [Fortran 90](https://www.fortran90.org)
* [Fortran 95](https://wg5-fortran.org/N1151-N1200/N1191.pdf)
* [Fortran 2003](https://link.springer.com/book/10.1007/978-1-84628-746-6)
* [Fortran 2008](https://j3-fortran.org/doc/year/10/10-007.pdf)
* [Fortran 2018](https://j3-fortran.org/doc/year/18/18-007r1.pdf)

### Make, GNU Make 

* [GMake Language Reference](https://www.gnu.org/software/make/manual/make.html)
* [Make Cheat Sheet](https://devhints.io/makefile)
* [GMake Cheat Sheet](https://gist.github.com/rueycheng/42e355d1480fd7a33ee81c866c7fdf78)
* [O'Reilly Managing Projects with GNU Make](https://www.oreilly.com/library/view/managing-projects-with/0596006101/)

### CMake, Autoconf

* [CMake Reference Manual](https://cmake.org/cmake/help/latest/index.html)
* [Autoconf Manual](https://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.71/autoconf.html)

### Performance Portability

* [Kokkos](https://github.com/kokkos/kokkos/wiki/API-Reference)
* [Raja](https://raja.readthedocs.io/en/develop/sphinx/user_guide/index.html)

### Commonly used APIs

* MPI API Specification [1.3](https://www.mpi-forum.org/docs/mpi-1.3/mpi-report-1.3-2008-05-30.pdf), [2.2](https://www.mpi-forum.org/docs/mpi-2.2/mpi22-report.pdf), [3.1](https://www.mpi-forum.org/docs/mpi-3.1/mpi31-report.pdf), [4.0](https://www.mpi-forum.org/docs/mpi-4.0/mpi40-report.pdf)
* OpenMP: [3.1](https://www.openmp.org/wp-content/uploads/OpenMP3.1.pdf), [4.5](https://www.openmp.org/wp-content/uploads/openmp-4.5.pdf), [5.2](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf)
* [POSIX Threads (Pthreads)](https://hpc-tutorials.llnl.gov/posix/AppendixA/)
* [Cuda](https://docs.nvidia.com/cuda/cuda-runtime-api/index.html)
* [Linux System Calls](https://man7.org/linux/man-pages/man2/syscalls.2.html)
* [Posix System Calls](https://docs.oracle.com/cd/E19048-01/chorus4/806-3328/6jcg1bm05/index.html)

### Login shells

* [csh language reference](https://www.mkssoftware.com/docs/man1/csh.1.asp)
* [sh language reference](https://pubs.opengroup.org/onlinepubs/009604499/utilities/xcu_chap02.html)
* [Bash reference manual](https://www.gnu.org/software/bash/manual/bash.html)

<!---
Publish: no
Pinned: no
--->
