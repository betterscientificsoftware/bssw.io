### Webinar Series: Best Practices for HPC Software Developers

**Venue:** Joint activity by ALCF, NERSC, OLCF, and the IDEAS Software Productivity Project

**Dates:** May—June, 2016

**Overview:**
This series of webinars presents best practices that help users of HPC systems carry out their software development more productively.   This series is designed for HPC software developers who are seeking help in increasing their team’s productivity, as well as facility staff who interact extensively with users.  

**Resources:**
slides and video for all presentations: https://www.olcf.ornl.gov/training-event/webinar-series-best-practices-for-hpc-software-developers/ 

**Topics:**

- _What All Codes Should Do: Overview of Best Practices in HPC Software Development_ - [Anshu Dubey (ANL)](http://www.mcs.anl.gov/person/anshu-dubey)
    - **Abstract:** Scientific code developers have increasingly been adopting software processes derived from the mainstream (non-scientific) community.  Software practices are typically adopted when continuing without them becomes impractical. However, many software best practices need modification and/or customization, partly because the codes are used for research and exploration, and partly because of the combined funding and sociological challenges. This presentation will describe the lifecycle of scientific software and important ways in which it differs from other software development.  We will provide a compilation of software engineering best practices that have generally been found to be useful by science communities, and we will provide guidelines for adoption of practices based on the size and the scope of the project.
    
- _Developing, Configuring, Building, and Deploying HPC Software_ - [Barry Smith (ANL)](http://www.mcs.anl.gov/person/barry-smith)
    - **Abstract:** The process of developing HPC software requires consideration of issues in software design as well as practices that support the collaborative writing of well-structured code that is easy to maintain, extend, and support.  This presentation will provide an overview of development environments and how to configure, build, and deploy HPC software using some of the tools that are frequently used in the community.  We will also discuss ways in which these and other tools are best utilized by various categories of scientific software developers, ranging from small teams (for example, a faculty member and graduate students who are writing research code intended primarily for their own use) through moderate/large teams (for example, collaborating developers spread among multiple institutions who are writing publicly distributable code intended for use by others in the community).
    
- _Distributed Version Control and Continuous Integration Testing_ - [Jeffrey Johnson (LBNL)](http://esd.lbl.gov/profiles/jeffrey-n-johnson/)
    - **Abstract:** Recently, many tools and workflows have emerged in the software industry that have greatly enhanced the productivity of development teams. GitHub, a site that hosts projects in Git repositories, is a popular platform for open source and closed source projects.  GitHub has encoded several best practices into easily followed procedures such as pull requests, which enrich the software engineering vocabularies of non-professionals and professionals alike.  GitHub also provides integration to other services (for example, continuous integration such as Travis CI, which allows code changes to be automatically tested before they are merged into a master development branch).   This presentation will discuss how to set up a project on GitHub, illustrate the use of pull requests to incorporate code changes, and show how Travis CI can be used to boost confidence that changes will not break existing code.
    
- _Testing and Documenting your Code_ - [Alicia Klinvex (SNL)](http://www.cs.sandia.gov/cr-amklinv)
    - **Abstract:** Software verification and validation are needed for high-quality and reliable scientific codes. For software with moderate to long lifecycles, a strong automated testing regime is indispensable for continued reliability. Similarly, comprehensive and comprehensible documentation is vital for code maintenance and extensibility. This presentation will provide guidelines on testing and documentation that can help to ensure high-quality and long-lived HPC software. We will present methodologies, with examples, for developing tests and adopting regular automated testing. We also will provide guidelines for minimum, adequate, and good documentation practices depending on the available resources of the development team.
    
- _How the HPC Environment is Different from the Desktop (and Why)_ - [Katherine Riley (ALCF)](https://www.alcf.anl.gov/staff-directory/katherine-riley)
    - **Abstract:** High performance computing has transformed how science and engineering research is conducted.  Answering a question in 30 minutes that used to take 6 months can quickly change the way one asks questions.  Large computing facilities provide access to some of the world’s largest computing, data, and network resources in the world.  Indeed, the DOE complex has the highest concentration of supercomputing capability in the world.  However, by nature of their existence, making use of the largest computers in the world can be a challenging and unique task. This talk will discuss how supercomputers are unique and explain how that impacts their use.
    
- _An Introduction to High-Performance Parallel I/O_ - Feiyi Li (ORNL)
    - **Abstract:** Parallel data management is a complex problem at large-scale HPC environments. The HPC I/O stack can be viewed as a multi-layered cake and presents an high-level abstraction to the scientists. While this abstraction shields the users from many of the I/O system details, it is very hard to obtain parallel I/O performance or functionality without understanding the end-to-end hierarchical I/O stack in today’s modern complex HPC environments. This talk will introduce the basic parallel I/O concepts and will provide guidelines on obtaining better I/O performance on large-scale parallel platforms.
    
- _Basic Performance Analysis and Optimization — An Ant Farm Approach_ - [Jack Disleppe (NERSC)](http://www.nersc.gov/about/nersc-staff/application-performance/jack-deslippe/)
    - **Abstract:** How is optimizing HPC applications like an Ant Farm? Attend this presentation to find out. We’ll discuss the basic concepts around optimizing code for the HPC systems of today and tomorrow. These systems require codes to effectively exploit both parallelism between nodes and an ever growing amount of parallelism on-node. We’ll discuss profiling strategies, tools (for profiling and debugging) and common issues with both internode communication and on-node parallelism. We will give an overview of traditional optimizations areas in HPC applications like parallel IO and MPI strong and weak scaling as well as topics relevant for modern GPU and many-core systems like threading, SIMD/AVX, SIMT and effectively using cache and memory hierarchies. The “Ant Farm” approach places a heavy emphasis on the roofline performance model and encouraging users to understand the compute, bandwidth and latency sensitivity of their applications and kernels through a series of easy to perform experiments and an easy to follow flow chart. Finally, we’ll discuss what we expect to change in the optimization process as we move towards exascale computers.


<!--- 
Categories: Planning, Reliability, Collaboration, Crosscutting, Performance
Topics: improving productivity and sustainability, reproducibility, testing, continuous integration testing, documentation
Tags: I/O, HPC
Level: 2 
Prerequisites: WhatIsSoftwareProductivity.md 
Aggregate: Base: Training.ProductivityAndSustainability.md
Aggregate: Section 1
--->
