# MPI Performance Guidelines

#### Contributed by: [Ken Raffenetti](https://github.com/raffenet)

#### Publication date: April 28, 2025

<!-- start of deck text -->
Find curated, expert-written content on how to improve your MPI application performance with easy-to-understand code examples and analysis in the MPI Performance Guidelines.
<!-- end of deck text -->

This blog post introduces [MPI Performance Guidelines](https://mpi-performance-guidelines.github.io/) – an online community resource for sharing independent, standards-based MPI performance guides. The guides are:

* **Best Practices**: Show users how to avoid common pitfalls or well-known bottlenecks when using MPI communication routines in their application. 
* **Portable**: The included [examples](https://github.com/mpi-performance-guidelines/examples) are MPI programs that can build and run using any MPI implementation (that supports the required standard APIs). Examples that rely on implementation-specific settings, such as environment variables, show results with at least two implementations to demonstrate portability.
* **Open Source**: The MPI Performance Guidelines site is open for [contributions](https://mpi-performance-guidelines.github.io/contributing)! Suggestions for new guides are welcome, as well as improvements to existing content.

### The focus is on performance

The [MPI Standard](https://www.mpi-forum.org/docs/) is vast. It contains 1000+ pages of technical specification that is not intended for end-users. Existing online MPI tutorial materials typically focus on functionality and correctness of MPI programs, with performance optimization left as an exercise for the reader. MPI Performance Guidelines aims to fill this gap by focusing on performance using common scientific application use-cases, e.g., halo exchange. By demonstrating the way MPI experts structure their communication, our guides can enable users to push their scientific applications further.

Our guides are intended for users who have some familiarity with MPI. That is, they have written MPI programs but may not have considered performance optimization yet for running on larger machines or larger problem sizes.

MPI Performance Guidelines' initial set of guides cover:

* **[Avoiding Unintended Synchronization](https://mpi-performance-guidelines.github.io/unintended-sync)**
* **[Ensuring Progress for MPI Nonblocking Operations](https://mpi-performance-guidelines.github.io/progress)**
* **[Minimizing Thread Contention Using Communication Objects](https://mpi-performance-guidelines.github.io/minimizing-thread-contention)**
* **[Dynamic Sparse Data Exchange with MPI_IBARRIER](https://mpi-performance-guidelines.github.io/dynamic-sparse)**

In addition to the written analysis and code examples, each guide contains a companion video explaining the topic in plain terms.

### Acknowledgement

This work was supported by the Better Scientific Software Fellowship Program, a collaborative effort of the U.S. Department of Energy (DOE), Office of Advanced Scientific Research via ANL under Contract DE-AC02-06CH11357 and the National Nuclear Security Administration Advanced Simulation and Computing Program via LLNL under Contract DE-AC52-07NA27344; and by the National Science Foundation (NSF) via SHI under Grant No. 2327079.

### Author bio

Ken Raffenetti is a principal software development specialist in the Mathematics and Computer Science Division at Argonne National Laboratory. He received his B.S. in computer science from the University of Illinois at Urbana-Champaign. He joined Argonne in 2006, where he worked for seven years as a systems administrator.

In 2013, Ken joined the Programming Models and Runtime Systems group, focused on the development of systems software for high-performance computing applications. Ken’s research interests include parallel programming models and low-level communication libraries. In particular, Ken is involved in the definition of the Message Passing Interface (MPI) standard and is a key maintainer of MPICH, the leading implementation of MPI. He is also a member of community working groups focused on the implementation and standardization of critical HPC software, including the [PMIx Administrative Steering Committee](https://pmix.github.io/), [OpenFabrics Interfaces Working Group](https://github.com/ofiwg), and [Unified Communication Framework](https://ucfconsortium.org/).

<!---
Publish: yes
Track: deep dive, bssw fellowship
Topics: high-performance computing (HPC), performance at leadership computing facilities
--->
