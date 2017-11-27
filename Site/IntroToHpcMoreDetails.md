# Intro to HPC

### What Makes High-Performance Computers So Powerful?  

By way of example, the Cray XK7 system "[Titan](https://www.olcf.ornl.gov/computing-resources/titan-cray-xk7/)" at the [Oak Ridge Leadership Computing Facility](https://www.olcf.ornl.gov/) was the fastest computer system in the world when it went into service in 2012 (third fastest as of November 2016).  It comprises 18,688 nodes, each of which contains a 16-core server-class CPU as well as a graphical processing uint (GPU) that is used to provide additional compute capability rather than graphics.  They are integrated by a proprietary network called Gemini, with a 3D torus topology.  The system has a peak performance in excess of 20 petaFLOPs (20 x 10<sup>15</sup> floating-point operations per second), and it occupies 4,352 ft<sup>2</sup> of floor space.  Titan itself contains no hard discs at all -- the storage system is separate, connected via a specially architected InfiniBand network. In 2012, it comprised 32 PB of storage, utilizing 20,160 2 TB hard drives, and was capable of moving data to Titan with an aggregate read/write bandwidth of > 1 TB/s.

Modern supercomputers can range from a small *cluster*, which might serve a research group or a department, to the largest *leadership-class* systems, which are resources at the national and international level.  The [Top500 list](https://www.top500.org/) tracks the world's 500 most powerful supercomputers  based on performance on the [LINPACK benchmark](https://www.top500.org/project/linpack/).  The list is updated twice a year. PetaFLOP performance levels were first achieved in [2008](https://www.top500.org/lists/2008/06/). The largest systems in 2017 provide performance in the tens of petaFLOPS.  The next major performance milestone in HPC is the [exaFLOP](Communities/ExascaleComputing.md), which is the subject of a great deal of work around the world on both hardware and software.  Current timelines have exascale computers becoming available in the early to middle 2020s.

<!---  Currently we're not attributing the Intro articles
#### Contributed by [David E. Bernholdt](https://github.com/bernhold), [Suzanne Parete-Koon](https://github.com/suzannepk), and [Rebecca Hartman-Baker](https://github.com/hartmanbaker)
--->

<!---
BSSw Site: Get Oriented: About HPC: More Details
--->
