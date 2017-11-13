# Intro to HPC

The initialism *HPC* can refer to either high-performance *computers* (the systems themselves) or high-performance *computing* (the *use* of high-performance computers).  It is usually clear from the context which is meant.

The idea of *high-performance computers*, or *supercomputers*, began to emerge in the 1960s as systems specially designed to address high-end computing needs. High-performance computers are significantly more powerful than their general-purpose counterparts and are used to tackle particularly challenging computational problems in science and engineering, as well as economics, that are too large for commodity computers or would take too long to solve.

### What Makes High-Performance Computers So Powerful?

Early supercomputers tended to rely on custom processors that were typically faster than the general-purpose processors of the day; and the processors and other aspects of the system often included special architectural features not present in general-purpose computers, such as vector processors and solid-state disc drives. (Many unique features of supercomputers eventually work their way into commodity systems, as technologies improve and prices drop.) More recently, limits related to semiconductor physics as well as cost have dictated that most modern supercomputers be based primarily on commodity components, with the extra computational capability coming from parallelism.  Today's supercomputers typically comprise tens to hundreds or even many thousands of individual *nodes* integrated via a high-performance network.  Each individual node resembles a personal computer or server.  

By way of example, the Cray XK7 system "[Titan](https://www.olcf.ornl.gov/computing-resources/titan-cray-xk7/)" at the [Oak Ridge Leadership Computing Facility](https://www.olcf.ornl.gov/) was the fastest computer system in the world when it went into service in 2012 (third fastest as of November 2016).  It comprises 18,688 nodes, each of which contains a 16-core server-class CPU as well as a graphical processing uint (GPU) that is used to provide additional compute capability rather than graphics.  They are integrated by a proprietary network called Gemini, with a 3D torus topology.  The system has a peak performance in excess of 20 petaFLOPs (20 x 10<sup>15</sup> floating-point operations per second), and it occupies 4,352 ft<sup>2</sup> of floor space.  Titan itself contains no hard discs at all -- the storage system is separate, connected via a specially architected InfiniBand network. In 2012, it comprised 32 PB of storage, utilizing 20,160 2 TB hard drives, and was capable of moving data to Titan with an aggregate read/write bandwidth of > 1 TB/s.

Modern supercomputers can range from a small *cluster*, which might serve a research group or a department, to the largest *leadership-class* systems, which are resources at the national and international level.  The [Top500 list](https://www.top500.org/) tracks the world's 500 most powerful supercomputers  based on performance on the [LINPACK benchmark](https://www.top500.org/project/linpack/).  The list is updated twice a year. PetaFLOP performance levels were first achieved in [2008](https://www.top500.org/lists/2008/06/). The largest systems in 2017 provide performance in the tens of petaFLOPS.  The next major performance milestone in HPC is the [exaFLOP](Communities/ExascaleComputing.md), which is the subject of a great deal of work around the world on both hardware and software.  Current timelines have exascale computers becoming available in the early to middle 2020s.

### Why Is HPC So Important?

HPC and [computational science and engineering (CSE)](IntroToCSE.md) are intertwined in a symbiotic relationship: HPC technology enables breakthroughs in CSE research, and leading-edge CSE applications are the main drivers for the evolution of supercomputer systems.  Advances in CSE typically come from some combination of being able to model larger physical systems, with greater resolution, for longer periods of time, and with greater fidelity to the actual physics.  These improvements are enabled by a combination of computer hardware and the software (and algorithms) that run on it.  Enabled by increasingly powerful supercomputers, computational modeling and simulation has become an increasingly important component of modern science. HPC-enabled CSE is also playing an increasingly significant role in industry.

### What Are the Unique Aspects of HPC?

CSE software on high-performance computers must address a broad range of complexities.  A primary concern on modern HPC systems is parallelism, especially at the largest scales.  However, the various architectures on the market -- including heterogeneous processor types, hierarchical memories, and other distinctive features -- make it particularly challenging to express algorithms in a way that is portable across the variety of architectures.  The hardware-related challenges of programming HPC systems are exacerbated by the increasing complexity on the science side, with multiscale and multiphysics simulations and increasingly complex models. The Better Scientific Software community is working to overcome challenges in CSE software complexity in both traditional HPC environments (clusters, networks of workstations, petascale machines) and [emerging extreme-scale architectures](Communities/ExascaleComputing.md).

### More Introductory Material on HPC
- [InsideHPC](http://insidehpc.com/)'s article on [What is High-Performance Computing?](http://insidehpc.com/hpc-basic-training/what-is-hpc/)
- [Wikipedia](https://wikipedia.org) entry on [Supercomputers](https://en.wikipedia.org/wiki/Supercomputer)
- The [Pawsey Supercomputer Centre](https://www.pawsey.org.au/) [training material archive](https://support.pawsey.org.au/documentation/display/US/Training+Material) includes several introductory tutorials:
  - [Introductory Supercomputing](https://support.pawsey.org.au/documentation/download/attachments/2162899/Introductory%20Supercomputing.pdf?api=v2)
  - [Introduction to Supercomputer Technology](https://support.pawsey.org.au/documentation/download/attachments/2162899/Introduction%20to%20Supercomputer%20Technology.pdf?api=v2)
  - [Intermediate Supercomputing](https://support.pawsey.org.au/documentation/download/attachments/2162899/Intermediate%20Supercomputing.pptx?api=v2)
- The [Archer](http://www.archer.ac.uk/) (UK National Supercomputing Service) [training archive](http://www.archer.ac.uk/training/past_courses.php) includes a [Hands-On Introduction to HPC](http://www.archer.ac.uk/training/course-material/2016/11/intro_newcastle/index.php)
- HPC software productivity challenges are discussed in the following community report: _**Software Productivity for Extreme-Scale Science**_, H. Johansen, L.C. McInnes, et al., 2014, Report on DOE Workshop, http://www.orau.gov/swproductivity2014/SoftwareProductivityWorkshopReport2014.pdf.

<!---  Currently we're not attributing the Intro articles
#### Contributed by [Lois Curfman McInnes](https://github.com/curfman), [David E. Bernholdt](https://github.com/bernhold), [Suzanne Parete-Koon](https://github.com/suzannepk), and [Rebecca Hartman-Baker](https://github.com/hartmanbaker)
--->

<!---
BSSw Site: Get Oriented: About HPC
--->
