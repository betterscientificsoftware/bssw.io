# Intro to HPC

<!--- This is meant to be the deck, if one is required for this type of document --->
High-performance computers are significantly more powerful than their general-purpose counterparts, and are used to tackle particularly challenging computational problems in science and engineering, as well as other areas.

As computers began to become generally available as commercial products, the community began to realize that different workloads place different demands on the systems.  The idea of *high-performance computers*, or *supercomputers*, began to emerge in the 1960s as systems specially designed to address high-end computing needs, most often for technical, scientific, and engineering problems.  While there is no strict definition of a supercomputer, they are generally recognized as offering significantly higher performance than the general-purpose or *commodity* counterparts of the day.  Note that the whole field of computer hardware has evolved very rapidly since its inception, so the distinction is to mainstream products available at the same time.  Most current smartpohone have significantly more computational capability than the iconic Cray-1 supercomputer introduced in 1976.

The ways in which supercomptuers get their extra capability have varied over the years.  In earlier times, supercomputers tended to rely on custom processors that were typically faster than the general-purpose processors of the day, and also often included special architectural features not present in general-purpose processors. such as vector processors.  More recently, limits related to semiconductor physics, as well as economics, have dictated that most (but not all) modern supercomputers be based primarily on commidity components with the extra computational capability coming from parallelism.  Today's supercomputers are typically comprised of tens to hundreds, or even many thousands of individual *nodes* integrated using a high-performance network.  Each individual node bears a resemblence to a personal computer or server.  By way of example, the Cray XK7 system "Titan" at the Oak Ridge Leadership Computing Facility was the fastest computer system in the world when it went into service in 2012 (third fastest as of November 2016).  It is comprised of 18,688 nodes, each of which contains a 16-core server-class CPU as well as graphical processing uint (GPU) which is used to provide additional compute capability rather than graphics.  They are integrated by a Cray proprietary network called Gemini, which provides a 3d torus network topology.  The system has a peak performance in excess of 20 PetaFLOPs (20 x 1015 floating-point operations per second) and it occupies 4,352 ft2 of floor space.  Titan itself contains no hard discs at all.  The storage system is separate, connected to Titan and other computers in the OLCF by a specially architected commodity InfiniBand network. In 2012, it comprised xxx PB of storage, utilizing yyyyy hard drives.

Due to this parallel architecture, modern supercomputers can be purchased at many scales, ranging from a small *cluster* that might serve a research group or a department to the largest *leadership-class* systems, which are resources at the national and international scale.  The Top500 list tracks the 500 most powerful supercomputers in world based on performance on the LINPACK benchmark.  The list is updated twice a year.

The initialism *HPC* can refer to either high-performance *computers* (the systems themselves) or high-performance *computing* (the *use* of high-performance computers).  It is usually clear from the context which is meant.

### Why is HPC so Important?

### What are the Unique Aspects of HPC?

High-performance computers are systems that are significantly more powerful than the mainstream "general-purpose" computers of the day.


High-Performance Computing (HPC) is the application of parallel computers to computational problems that are either too large for standard computers or would take too long.  HPC and CSE are intertwined in a symbiotic relationship: HPC technology enables breakthroughs in CSE research, and leading-edge CSE applications are the main drivers for the evolution of supercomputer systems.  

CSE software in HPC must address a broad range of complexities, including memory management for hierarchical and heterogeneous systems, refactoring to achieve portable performance in the face of evolving architectures, and challenges of multiscale and multiphysics modeling, simulation, and analysis.  The Better Scientific Software community is working to overcome challenges in CSE software complexity in both traditional HPC environments (clusters, networks of workstations, petascale machines) as well as [emerging extreme-scale architectures](Communities.ExascaleComputing.md).  More details on HPC software productivity challenges are provided in the following reports:

HPC software productivity challenges are discussed in the following community report: _**Software Productivity for Extreme-scale Science**_, H. Johansen, L.C. McInnes, et al., 2014, Report on DOE Workshop, http://www.orau.gov/swproductivity2014/SoftwareProductivityWorkshopReport2014.pdf.

For more information on better scientific software, go to the [Better Scientific Software main page](http://betterscientificsoftware.info).

<!---
BSSw Site: Get Oriented: About HPC
--->
