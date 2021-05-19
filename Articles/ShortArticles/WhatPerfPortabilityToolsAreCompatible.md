## Understanding Compatibility of Performance Portability Tools

<!--- deck text start --->
Tools such as OpenMP and CUDA are helping scientific applications achieve performance portability. However, do we understand the underlying compatibility challenges encountered by these tools?
<!--- deck text end --->

#### Contributed by [Dan Ibanez](https://github.com/ibaned)

#### Publication date: July 20, 2019

As applications begin to enable performance portability through the use of
tools such a OpenMP and Compute Unified Device Architecture (CUDA), they may encounter issues related to compability of tools used by different libraries they depend on. This short document describes known incompatibilities between performance portability tools, as well as cases of successful interoperation between such tools.

### Threading Tools
#### Thread Pool Incompatibilities

OpenMP is a standard which describes an interface to a thread pool.
Different compilers such as GNU and Intel have different implementations of thread pools.
Other tools provide implementations of thread pools based on the `pthread` library, for example.

Different implementations of thread pools are usually incompatible, because
each implementation assumes it has ownership of all on-node hardware thread
resources, and creates correspondingly many software threads.
The software threads from different thread pool implementations then compete
for the hardware thread resources.
This contention may be somewhat manageable if, while one thread pool executes,
the threads from all other thread pools are idle, but this is still a precarious situation.

#### Same-Compiler OpenMP is Compatible

What is compatible is for different software packages to all be compiled with the same
compiler and all use OpenMP directives.
This allows them all to use the same thread pool implementation and share the hardware
resources appropriately.
In the case where one package executes at a time, the currently executing package will benefit
from all software threads in the pool.
In the case where one package calls another package from within an OpenMP parallel region,
the nesting should be properly handled without overloading hardware resources.
Finally, each package is free to use a subset of the available threads depending on what
is optimal for that package.

### GPU Tools

Normal OpenMP threading is compatible with CUDA, and there are known examples of codes that use both at the same time. However, OpenMP added a target offload capability which can make use of GPUs, and some implementations of OpenMP target offload are incompatible with CUDA, because they each set up conflicting CUDA contexts. OpenACC, on the other hand, should be compatible with CUDA, in part because they are both
developed by NVIDIA.

### Higher-Level Tools

There are higher-level tools available including OCCA, Kokkos, and RAJA.
These tools make use of more fundamental tools like OpenMP and CUDA, and so their
compatibility can usually be derived from the compatibility of the lower-level tools they are using.
For example, if one package uses OCCA to transform their code into CUDA, and another
package uses Kokkos's CUDA backend, then those two packages should be reasonably interoperable.
Conversely, if one package uses OCCA to transform their code to use OpenMP,
and another package uses Kokkos's Threads backend, then they will not be as interoperable
because of the different implementations of thread pools.


<!---
Publish: preview
Pinned: no
Topics: Performance portability
RSS update: 2021-05-12
--->

