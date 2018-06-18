# Debugging CSE Software

  Debugging tools help with identifying buggy code or code paths in software.

  What follows is a short list of tools that help with debugging applications.

  - [GDB](https://www.gnu.org/software/gdb/) The most commonly used
    tool is a debugger.  GDB is a commonly available debugger on
    various OSes.

    Similar to gdb - one might find
    [idb](https://software.intel.com/sites/default/files/m/8/4/c/5/7/6364-idb_manual.pdf)
    with Intel compilers, or [lldb](https://lldb.llvm.org/) with clang
    or [dbx](https://en.wikipedia.org/wiki/Dbx_(debugger)) on older
    unix OSes.

    One can also use [DDD](https://www.gnu.org/software/ddd/) a
    graphical frontend to gdb.

  - [totalview](https://www.roguewave.com/products-services/totalview)
    is a parallel debugger which is useful to debug
    [MPI](https://www.mpi-forum.org/) based applications.

  - [valgrind](http://valgrind.org/) provides tools for debugging
    memory corruption, memory leaks, and other tools.

  - [Clang Static Analyzer](https://clang-analyzer.llvm.org/) is
    useful to determine buggy code paths.

  - [Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html) is a tool to
    identify code coverage for an application run.

#### Contributed by [Satish Balay](https://github.com/balay "Satish Balay")

<!---
Publish: no
Categories: Development
Topics: debugging
Tags:
Level: 2
Prerequisites: defaults
Aggregate: none
--->
