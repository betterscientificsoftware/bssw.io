# Intro to HPC

The initialism *HPC* can refer to either high-performance *computers* (the systems themselves) or high-performance *computing* (the *use* of high-performance computers).  It is usually clear from the context which is meant.

The idea of *high-performance computers*, or *supercomputers*, began to emerge in the 1960s as systems specially designed to address high-end computing needs. High-performance computers are significantly more powerful than their general-purpose counterparts and are used to tackle particularly challenging computational problems in science, engineering, analytics, and other areas that are too large for commodity computers or would take too long to solve.

### What Makes High-Performance Computers So Powerful?

Early supercomputers tended to rely on custom processors that were typically faster than the general-purpose processors of the day; and the processors and other aspects of the system often included special architectural features not present in general-purpose computers, such as vector processors and solid-state disc drives. (Many unique features of supercomputers eventually work their way into commodity systems, as technologies improve and prices drop.) More recently, limits related to semiconductor physics as well as cost have dictated that most modern supercomputers be based primarily on commodity components, with the extra computational capability coming from parallelism.  Today's supercomputers typically comprise tens to hundreds or even many thousands of individual *nodes* integrated via a high-performance network.  Each individual node resembles a personal computer or server.  

<!---
[More details](HpcMoreDetails.md)
--->

### Why Is HPC So Important?

HPC and [computational science and engineering (CSE)](https://bssw.io/pages/intro-to-cse) are intertwined in a symbiotic relationship: HPC technology enables breakthroughs in CSE research, and leading-edge CSE applications are the main drivers for the evolution of supercomputer systems.  Advances in CSE typically come from some combination of being able to model larger physical systems, with greater resolution, for longer periods of time, and with greater fidelity to the actual physics.  These improvements are enabled by a combination of computer hardware and the software (and algorithms) that run on it.  Enabled by increasingly powerful supercomputers, computational modeling, simulation, and analytics have become increasingly important components of modern science. HPC-enabled CSE is also playing an increasingly significant role in industry.

### What Are the Unique Aspects of HPC?

CSE software on high-performance computers must address a broad range of complexities.  A primary concern on modern HPC systems is parallelism, especially at the largest scales.  However, the various architectures on the market — including heterogeneous processor types, hierarchical memories, and other distinctive features — make it particularly challenging to express algorithms in a way that is portable across the variety of architectures.  The hardware-related challenges of programming HPC systems are exacerbated by increasing complexity on the science side, with multiscale and multiphysics simulations and increasingly complex models. The Better Scientific Software community is working to overcome challenges in CSE software complexity in both traditional HPC environments (clusters, networks of workstations, petascale machines) and [emerging extreme-scale architectures](https://bssw.io/communities/exascale-computing-community).

### More Introductory Material on HPC
- [InsideHPC](http://insidehpc.com/)'s article on [What is High-Performance Computing?](http://insidehpc.com/hpc-basic-training/what-is-hpc/)
- [Wikipedia](https://wikipedia.org) entry on [Supercomputers](https://en.wikipedia.org/wiki/Supercomputer)
- The [Pawsey Supercomputer Centre](https://www.pawsey.org.au/) [training material archive](https://support.pawsey.org.au/documentation/display/US/Training+Material) includes several introductory tutorials:
  - [Introductory Supercomputing](https://support.pawsey.org.au/documentation/download/attachments/2162899/Introductory%20Supercomputing.pdf?api=v2)
  - [Intermediate Supercomputing](https://support.pawsey.org.au/documentation/download/attachments/2162899/Intermediate%20Supercomputing.pdf?api=v2)
- The [Archer](http://www.archer.ac.uk/) (UK National Supercomputing Service) [training archive](http://www.archer.ac.uk/training/past_courses.php) includes a [Hands-On Introduction to HPC](http://www.archer.ac.uk/training/course-material/2016/11/intro_newcastle/index.php)
- HPC software productivity challenges are discussed in the following community report: [_Software Productivity for Extreme-Scale Science_](https://science.osti.gov/-/media/ascr/pdf/research/cs/Exascale-Workshop/SoftwareProductivityWorkshopReport2014.pdf), H. Johansen, L.C. McInnes, et al., 2014, Report on DOE Workshop. 


<!---  Currently we're not attributing the Intro articles
#### Contributed by [Lois Curfman McInnes](https://github.com/curfman), [David E. Bernholdt](https://github.com/bernhold), [Suzanne Parete-Koon](https://github.com/suzannepk), and [Rebecca Hartman-Baker](https://github.com/hartmanbaker)
--->

<!---
BSSw Site: Get Oriented: About HPC
--->

<!--
Publish: yes
-->
