# Practices for Productive Software Development in Kokkos

#### Contributed by [Nathan Ellingwood](https://github.com/ndellingwood) and [Siva Rajamanickam](https://github.com/srajama1)

#### Publication date: June 15, 2021

<!-- deck -->
The folks behind the Kokkos performance portable C++ library explain some of the development practices they've adopted to ensure that their product works well for their growing user base.
<!-- end deck -->

As we move closer to computing systems capable of exascale performance coming online, an ever-expanding set of technologies (such as CPUs, GPUs, and ARM based processors) will be employed as part of our platforms, all using their own memory technologies. Accompanying this wave of technologies is a complex web of software, including programming models and compilers which expose the hardware to developers for use with their applications.

Performance portable software libraries aim to ease the burden on application developers and boost productivity by providing a common programming model toward which to write their code. To have a programming model with the ability to support the plethora of architectures and compilers employed by the diverse set of platforms, as well as support interoperability requirements with applications, creates a trade-off faced by several software frameworks. New architectures and changes in lower-level programming models such as CUDA necessitate new capabilities in portable programming models. Computational science applications require a stable environment for their productivity, despite changes in hardware, systems software, runtime, and lower-level programming models. We balance this trade-off with extensive testing and maintain a stable, performance portable software stack without crippling developers’ efforts to contribute new capabilities. We share some current practices and efforts toward these challenges based on the [Kokkos Ecosystem](https://kokkos.org/about/), a performance portable C++ library that is part of the [US Department of Energy’s Exascale Project](https://www.exascaleproject.org/).

### Branching model

Projects in the Kokkos Ecosystem reside on [GitHub](https://github.com/kokkos) and employ a branching process that looks similar to the [Git Flow workflow]( https://nvie.com/posts/a-successful-git-branching-model/):

- The master branch is default, production-ready code, and held frozen between releases. 
- The develop branch tracks contributions by developers, such as bug fixes, new features, enhancements, etc. Completed features are submitted as pull requests to the develop branch for code review and acceptance testing. GitHub’s issue tracker is used for communication regarding requests, bug reports, and progress.
- Release cycles last approximately three to four months, at which point a release candidate branch is created off of develop. What follows next is extensive testing, including integration testing with frameworks such as [Trilinos](https://trilinos.github.io/), and a tagged release.

This process, coupled with testing requirements described in more detail next, aims to balance developer productivity with code stability: the compilers, hardware and configurations most widely used are shielded by acceptance testing of pull requests to the develop branch and leaving it in a relatively stable state for users eager to incorporate the newest features and capabilities. This process is also somewhat unusual for Git based libraries where the default master branch is updated more frequently. Release branches could also be used in similar way. However, we chose this approach so the default branch is a stable master that has been through integration testing with selected applications.

### Testing, testing, testing

As a performance-portable software library, we are expected to support a variety of compilers and versions, hardware, and library configurations. For example with the Kokkos Ecosystem regular testing includes (at the time of writing):

- Compilers: GCC (5.3.0 – 10); Clang (4.0-11); Intel (17-19); NVCC (9.2-11); ROCm/HIP (4.2); OneAPI (sycl-nightly tag); IBM/XL (16.1.1)
- Hardware: x86_64 (various), KNL, ARMv8 ThunderX2, NVIDIA (K80, P100, V100, A100), AMD (Zen CPU, Vega MI25, MI50, MI60, MI100)
- Backends: Serial, OpenMP, Pthreads, Cuda, HIP (Experimental), OpenMPTarget (Experimental), Sycl (Experimental), HPX

Notice that we test several experimental options and support several older compilers that are years old in order to address the trade-off mentioned above. Total testing coverage requires hours of testing across several computing systems. It would be an unreasonable burden and detriment to coder productivity to require testing the full combinatorial set of supported builds and configurations. To balance developer productivity while preserving software quality and stability, testing of the code base consists of three stages:

#### 1. Pull request acceptance testing

  - Pull request testing is automated through use of [Jenkins](https://www.jenkins.io/solutions/github/) and [GitHub Actions](https://docs.github.com/en/actions) and triggered automatically when a new pull request is submitted to the repository through GitHub.
  - A fixed subset from the full combinatorial explosion of the test coverage space is selected to provide enough testing-breadth to give reasonable confidence that code changes can pass full testing coverage with high likelihood; clang-format is used to enforce consistency of style and readability across the code base.
  - Final acceptance of a pull request requires code review by a team member. Code reviews help improve software quality and disseminate knowledge of code updates to members of the team.

#### 2. Nightly testing

  - Nightly testing is automated by Jenkins. Nightly tests significantly expand on pull request testing to fill the missing gaps in coverage, including various configuration options (some costly), older compilers, and experimental builds. More than 200 nightly tests run on all the aforementioned platforms.

#### 3. Release testing

Kokkos and Kokkos Kernels exist as standalone libraries available on GitHub, and are foundational packages within the Trilinos scientific software library (under the “data services” scope). A new release of the Kokkos Ecosystem requires passing testing within Trilinos, providing additional robustness:

- We do not assume the Kokkos testing suite is fully comprehensive – testing with Trilinos exposes corner cases that may have been missed in the testing suite.
- Trilinos testing is assumed to be complex enough to provide coverage for most customer applications.

### Support

While the above mentioned features help us sustain a reasonable balance between evolving architectures and stability requirements of applications, as with any software, the possibility of a bug is always there. We provide a robust support mechanism for applications at several levels. Kokkos developers reside at major DOE computing facilities who serve as the point of contact for their corresponding institutions. We use Slack and GitHub as the primary resource for direct user support. As of this writing, the [Kokkos Slack channel](https://kokkosteam.slack.com) has 585 members across multiple institutions. Community contributions in evaluating new features, alpha users who use the develop branch and provide feedback, and hardware vendors who test Kokkos with new compilers and runtimes, all contribute to the stability of the software ecosystem.

### Author bios

Nathan Ellingwood is a senior member of Technical Staff at Sandia National Laboratories. He is a developer and contributor on the Kokkos, Kokkos Kernels and Trilinos projects, and has interests in high-performance computing, mathematical and data analytics software.

Siva Rajamanickam is a principal member of Technical Staff at the Center for Computing Research at Sandia National Laboratories. His interests are in performance portability, linear solvers, graph algorithms and machine learning. 

<!--
### Disclaimer

Sandia National Laboratories is a multimission laboratory managed and operated by National Technology and Engineering Solutions of Sandia LLC, a wholly owned subsidiary of Honeywell International Inc. for the U.S. Department of Energy’s National Nuclear Security Administration under contract DE-NA0003525.

Unclassified Unlimited Release (UUR) SAND2021-6146 S
-->

<!---
Publish: yes
Pinned: no
Topics: release and deployment, issue tracking, testing, continuous integration testing, 
RSS update: 2021-06-15
Track: experience
--->
