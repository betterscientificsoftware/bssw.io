# Fundamental On Line Programming Resources for Scientific Computing
<!--deck text start-->
<!--deck text end-->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86 "Mark C. Miller GitHub Profile")

We host here in tabluar layout a number of online programming resources of fundamental importance in HPC/CSE.
We begin with the most fundamental of topics...formal specifications and standards for programming *languages* most commonly used in HPC/CSE.
These are formal documents primarily for implementors of compilers that define, in excrutiating detail, how programs in the language are supposed to behave and attempt to cover all possible *corner* cases.

Language specifications evolve with time and so are versioned, typically by the year a new specification is *initiated*.
Not all languages commonly used in HPC/CSE, notably Python, are defined by a *formal specification*.
Instead, they rely solely on a [*reference implementation*](https://en.wikipedia.org/wiki/Reference_implementation).
Python's reference implementation is [CPython](https://en.wikipedia.org/wiki/CPython).

From formal specifications, we move on to language *implementations*.
The *implementation* of a programming language is embodied in a [compiler](https://en.wikipedia.org/wiki/List_of_compilers) or, for interpretive languages like Python (or Basic), an *interpreter*.
The relevant documentation takes the form of compiler reference manuals.
These documents are created by each *vendor* that supports a given compiler.

A program consisting entirely of language statements typically does not make a useable application.
Programs need to interact with the outside world...to accept user input, to read and write data to terminal windows and/or files and to interact with other *devices*.
This functionality is typically provided in the form of an accompanying *standard library*...a set of function calls with *well defined interfaces* that do things like allocate and free memory, open and close files, read and write data, etc.

A challenge with standard libraries is that they aren't always very *standard*.
Different hardware vendors provide different and sometimes incompatible implementations.
[POSIX](https://en.wikipedia.org/wiki/POSIX) compliance was introduced in the 1990's to address this.

Hardware vendors are obliged to provide a compiler that supports their hardware.
No applications can use their hardware without one.
Often, hardware vendors develop and support their own *native* (and proprietary) compilers.
This ensures applications are maximally performant on their hardware.
Alternatively (or sometimes in additionally), existing compilers are enhanced to target performance features of the vendor's hardware.

Notably, GNU, Intel, Portland Group and Clang compilers are not tied to any particular hardware vendor.
These compilers are often made available on various vendor's hardware and in some cases can even produce higher performing code than the hardware vendor's *native* compiler.

It can take many years for compiler vendors to update their implementations to conform to new language standards.
It is not uncommon for a language/compiler reference manual or standard library to depart from a formal language specification in various minor ways especially during a period in which it is transitioning to new language standard.

For example, the GNU compiler collection (GCC) often supports a number of [language *extensions*](https://gcc.gnu.org/onlinedocs/gcc/C-Extensions.html) some of which eventually make their way into the formal language standard.
The use of language features unique to a specific standard and/or compiler can introduce portability issues.
To avoid such possibilities, projects often constrain which language standards and compiler versions they agree to use and support.
For example, the [VisIt](https://visit-dav.github.io/visit-website/) project decided to permit C++11 constructs (specific to the 2011 C++ standard) into the code base only in 2018, a full 7 years after the language standard had been released.

After languages and compilers, we cover commonly used technologies that are offered in the form of either *language extensions* or application programming interfaces (APIs).
Sometimes whether a technology is considered a *language extension* or an *API* isn't always very clear cut.
In addition, we cover a handful of other programming technologies commonly encountered when contributing to HPC/CSE code projects.

Programming<br>Technology | Versions, Variants<br>and/or Vendors | Other notes
:--- | :---: | ---:
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Formal Language Specifications and Standards**</td></tr>
C | [89][c89-spec]/[99][c99-spec]/[11][c11-spec]/[18][c18-spec] | ([1][1])
C++ | [03][c++03-spec]/[11][c++11-spec]/[14][c++14-spec]/[17][c++17-spec]/[20][c++20-spec] | ([1][1])
C Preprocessor | Part of C specification | ([4][4])
Fortran | [77][f77-spec]/[90][f90-spec]/[95][f95-spec]/[03][f03-spec]/[08][f08-spec]/[18][f18-spec] | ([1][1])
OpenCL | [1.2][ocl1.2-spec]/[2.2][ocl2.2-spec]/[3.0][ocl3.0-spec] | ([2][2])
Python | [2][py2-spec]/[3][py3-spec]| ([3][3])
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Language Implementations - Compiler Reference Manuals**</td></tr>
C | [MS][c-ms]/[IBM][c-ibm]/[GNU][c-gnu]/[Cray][c-cray]/[LLVM][c-clang]/[AMD][c-amd]/[Intel][c++-intel]
C++ | [AMD][c++-amd]/[MS][c++-ms]/[IBM][c++-ibm]/[LLVM][c++-clang]/[Cray][c++-cray]/[Intel][c++-intel]|
C Preprocessor | Usually part of C implementation<br>[GNU][cpp-gnu]/[MS][cpp-ms] |
Fortran | [PGI][f-pg]/[LF][f-lf]/[Intel][f-intel]/[Cray][f-cray]/[IBM][f-ibm]/[NAG][f-nag]/[GNU][f-gnu]
OpenCL | [NVIDIA][opencl-nvidia]/[AMD][opencl-amd]/[Intel][opencl-intel]|
Python | [2][py2]/[3][py3] |([3][3])
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Standard Library Reference**</td></tr>
C Standard Library | [C][c-stdlib]| |
C++ Standard Library | [0][c++-stdlib-0] |
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">**Standard Library Implementations**</td></tr>
C Standard Library | https://en.wikipedia.org/wiki/C_standard_library#Implementations | |
C++ Standard Library | https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library#Implementations |

[//]: # (Table footnotes. Text is dup'd for rendered HTML and balloon help)

[1]: #a1 "Version numbers are the last 2 digits of the year the standard was *initiated*. Sometimes, standards are formally *finalized* years after they were *initiated*."
[2]: #a2 "Language *extensions* for special devices (e.g. co-processors, GPUs, FPGAs, accelerators, etc.)."
[3]: #a3 "The most formal resource for Python is the [language reference](https://docs.python.org/dev/reference/) and the *reference* implementation, [CPython](https://github.com/python/cpython)"
[4]: #a4 "CPP is sometimes used to process other kinds of text files including those of other languages. CPP `#pragma`s are a common way for compiler vendors to extend the language."

<a name="a1"></a><sup>1</sup>Version numbers are the last 2 digits of the year the standard was *initiated*. Sometimes, standards are formally *finalized* years after they were *initiated*.<br>
<a name="a2"></a><sup>2</sup>Language *extensions* for special devices (e.g. co-processors, GPUs, FPGAs, accelerators, etc.).<br>
<a name="a3"></a><sup>3</sup>The most formal resource for Python is the *reference* implementation, [CPython](https://en.wikipedia.org/wiki/CPython)<br>
<a name="a4"></a><sup>4</sup>CPP is sometimes used to process other kinds of text files including those of other languages. CPP [`#pragma`s](https://gcc.gnu.org/onlinedocs/cpp/Pragmas.html) are a common way for compiler vendors to extend the language.

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

[c++-stdlib-0]: https://www.cplusplus.com/reference/
https://docs.microsoft.com/en-us/cpp/standard-library/cpp-standard-library-reference?view=msvc-170
https://docs.python.org/3/library/

https://gcc.gnu.org/onlinedocs/libstdc++/

https://learn.microsoft.com/en-us/cpp/standard-library/cpp-standard-library-reference?view=msvc-170

https://libcxx.llvm.org//


https://www.gnu.org/software/libc/manual/pdf/libc.pdf

https://gcc.gnu.org/onlinedocs/libstdc++

https://www.ibm.com/docs/en/SSGH3R_13.1.3/com.ibm.compilers.aix.doc/standlib.pdf/


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

Boost, POSIX

https://charmplusplus.org

<!---
Publish: no
Pinned: no
--->
