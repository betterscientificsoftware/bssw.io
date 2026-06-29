# Comparing Scaling Behavior Across Diverse Parallel Architectures
<!--- deck text start --->
Explore how characterizing performance portability in the presence of extreme architectural diversity is enabled through node-to-node scaling as a cross-platform framework.

<!--- deck text end --->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: June 29, 2026

Resource information | Details
:--- | :--- 
Paper title  | Comparing Cross-Platform Performance via Node-to-Node Scaling Studies
Authors | Kenneth Weiss, Thomas M. Stitt, Daryl Hawkins, Olga Pearce, Stephanie Brink, Robert N. Rieben
Publication | Year 2026, The International Journal of High Performance Computing Applications. 2026;40(1):80-95. DOI: [10.1177/10943420251381191](https://doi.org/10.1177/10943420251381191)

Scientific applications are now deployed across increasingly heterogeneous computing environments, ranging from CPU based clusters to GPU accelerated supercomputers. 
As portable programming models and shared codebases become more common, understanding performance behavior across these diverse systems has become an important concern in modern HPC workflows.

The paper, ``Comparing Cross-Platform Performance via Node-to-Node Scaling Studies``, argues that traditional HPC scaling methodologies are increasingly inadequate for modern HPC systems composed of CPUs, GPUs or other accelerators as well as diverse memory hierarchies and layouts.
The authors contend that the most meaningful unit for cross-platform performance comparison is the compute node rather than individual processors, cores, or MPI ranks.

A methodology is proposed for *node-to-node* scaling studies, including node-to-node strong scaling, weak scaling, combined strong-weak scaling, and throughput scaling.
Standardized plotting conventions are also proposed using log<sub>2</sub>–log<sub>2</sub> axes, ideal scaling reference lines, and time-per-cycle metrics to improve clarity and comparability across systems.

The authors demonstrate their proposed approach using the [MARBL](https://www.researchgate.net/publication/344230366_The_MARBL_Multi-physics_Code) multiphysics simulation code on several LLNL systems, including CPU-only and GPU-accelerated supercomputers such as [Sierra](https://en.wikipedia.org/wiki/Sierra_(supercomputer)) and [EAS-3](https://www.llnl.gov/article/48121/early-access-systems-llnl-mark-progress-toward-el-capitan).
The studies show how node-based scaling analysis highlights GPU saturation effects, memory bandwidth limitations, and differences in scaling behavior across diverse architectures.

The paper concludes that node-to-node scaling studies provide a practical framework for evaluating portable performance of HPC applications, complementing rather than replacing traditional scaling studies.

Readers will take away an approach that uses node-to-node scaling as a per-node baseline, enabling more consistent cross-platform comparisons across heterogeneous systems where traditional scaling metrics can be harder to interpret.

<!---
Publish: yes
Topics: Performance Portability, High-Performance Computing (HPC)
Pinned: no
--->
