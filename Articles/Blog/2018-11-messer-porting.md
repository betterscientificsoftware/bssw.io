
# Porting Codes to New Architectures

**Hero Image:**
- <img src="../../images/Blog_1118_SummitCabs_1176x432.png" />[Closeup of Summit computer at ORNL]

#### Contributed by [Bronson Messer](https://github.com/bronson79 "Bronson Messer GitHub Profile")

#### Publication date: November 26, 2018

The advent of new computing architectures in recent years has given new impetus to efforts to update and improve application performance. 

The inexorable march of Moore's law and Dennard scaling through the end of the first decade of this century allowed HPC application developers to rely on "scp and make" to provide increased performance. Every eighteen months provided a new platform, different from the last only in its computational power and raw speed. Even straightforward and well-known optimizations (e.g., arranging memory accesses to take advantage of high-speed caches) were often left undone, since the clear need to produce as much science as possible was greater than the need to improve performance. However, modern, highly parallel node architectures have brought this age of essentially effortless performance improvement to an end.

Achieving performance on GPU-based architectures, in particular, requires considerable effort by application developers to make their code amenable to opportunities and limitations of the hardware. The OLCF's Center for Accelerated Application Readiness (CAAR) has enabled GPU ports for a variety of application codes, on both Titan and Summit, in recent years. Though the programming tools and specific hardware characteristics have certainly changed over the time from the advent of Titan to today, basic notions remain that can be used to help port legacy codes to GPUs. Here are a few of the most fundamental things you can do to get started.

### Obtain an accurate code profile 

No, seriously: We know that you already know where all the time is being spent, but go ahead and use a tool to confirm.

Obtaining an accurate and up-to-date code profile is essential to beginning any GPU porting project. This profile should include, of course, where the FLOPs are being done, but also where and how memory references are being made throughout the code. ScoreP, TAU, ARM Forge, and a variety of other tools can be used to gather this information. Perhaps most important, the use of one of these tools does not preclude the use of any other. A "pincer movement," wherein several tools are used to obtain profiling information, can often be useful. Once an accurate profile is in hand, decisions will have to be made to determine where effort is best expended. If an application is "lucky" enough to have a handful of "hot" kernels, the choice is often obvious. More likely a few kernels are more-or-less obvious choices for acceleration, but a handful of other kernels could probably be accelerated with some additional effort. This calculus can be done only in the context of the developer's other work on the code, but care must be taken to realize that those unaccelerated kernels will become the bottleneck in the next stage of development. 

### Decide on a programming model 

Should I used CUDA? OpenACC? Kokkos? RAJA? OpenMP with offload? OpenCL? Raw PTX? 

The answer to this seeming dilemma is straightforward: It doesn't matter much. Differences will exist between any of these choices, of course, but the refactoring that will be done to accommodate the effective use of any of them is the same: aggregating work, ensuring locality of memory references, making loop nests as tight as possible, and so on. All these code modifications will require at least as much effort as the addition of some code in, for example, CUDA or decoration with directives. Indeed, CAAR developers found that for Titan, 70-80% of the total effort was dedicated to code refactoring, separate from any architecture-specific additions to the codes. Don't become paralyzed by the notion that you must pick one programming model once and for all at the beginning of the port. Do the bulk of the code refactoring, and add whatever specific code or directives you need to start work on the GPU. 

Code refactoring is not merely additional toil that must be undertaken in anticipation of using accelerators. The changes--especially changes that improve the locality of memory references--will almost always lead to improved performance on *any* architecture. During our CAAR experience on Titan, we found that every code that underwent refactoring for GPU porting also ran roughly 2x faster on CPU's! This performance enhancement was universal: *all* the codes got about a 2x improvement. Recent results suggest that the same effect has been seen for Summit CAAR codes. 

### Pay attention to where data are and where they are going

Though the need to understand and ameliorate the high cost of data movement was especially acute on Titan, all modern architectures have rich and deep memory hierarchies. Effective exploitation of these hierarchies is essential in order to realize maximum performance. Data structure placement in high-speed memories at the start of execution, and strategies to keep the data in those high-speed memories are among the most important considerations for any performance optimization. The use, for example, of managed memory on CPU-GPU nodes can be an effective way to start a port, but the first optimization will more often than not involve explicit memory management. A first cut at data placement--even if incomplete--can increase performance markedly. The use of asynchronous methods for moving data between memories is another primary strategy for achieving good performance. 

Other, more advanced techniques can be brought to bear on any specific architecture. But the above considerations are, at least, first among equals when it comes to ideas for porting codes to new, highly parallel architectures. 

### For more information on particular experiences from the OLCF CAAR program and other recent work, see the following:

<!--- David will add a curated content item --->

Joubert, W., Archibald, R., Berrill, M., Brown, W.M., Eisenbach, M., Grout, R., Larkin, J., Levesque, J., Messer, B., Norman, M. and Philip, B., 2015. Accelerated application development: The ORNL Titan experience. Computers & Electrical Engineering, 46, pp. 123-138. [https://www.sciencedirect.com/science/article/pii/S0045790615001366]

Straatsma, T.P., Antypas, K.B. and Williams, T.J., 2017. Exascale Scientific Applications: Scalability and Performance Portability. Chapman and Hall/CRC. [https://www.crcpress.com/Exascale-Scientific-Applications-Scalability-and-Performance-Portability/Straatsma-Antypas-Williams/p/book/9781138197541]

Messer, O.E.B., D’Azevedo, E., Hill, J., Joubert, W., Berrill, M. and Zimmer, C., 2016. MiniApps derived from production HPC applications using multiple programming models. The International Journal of High Performance Computing Applications, p. 1094342016668241. [https://journals.sagepub.com/doi/abs/10.1177/1094342016668241]

<!--- Guidance for blog author bios:
•       Length: 50-100 words.
•       Can include hyperlinks.
•       Mention your current position, employer, a bit about your background.
•       Include info about your interests related to software productivity and sustainability.
•       Anything else you want to mention.
--->

### Author Bio

[Bronson Messer](http://astro.phys.utk.edu/bronson) is a Senior R&D Staff Member at Oak Ridge National Laboratory (ORNL) and a Joint Faculty Associate Professor at the University of Tennessee. He is involved in the DOE Exascale Computing Project (ECP) as co-I of the [ExaStar](https://sites.google.com/lbl.gov/exastar) application development and [ECP Proxy Application](https://proxyapps.exascaleproject.org/) projects. He is also the computational PI of the Scientific Discovery through Advanced Computing (SciDAC) [TEAMS](https://teams-scidac.github.io/) project to study explosive astrophysical events. His research interests range from supernovae, stellar evolution, and numerical relativity to studies of mini-apps and performance modeling. His adventures in maintaining and extending several decades-old codes have led to his strong interest in software sustainability and productivity. 

<!---
Publish: yes
Track: experience
RSS update: 2018-11-26
Categories: Performance, Development
Topics: high-performance computing (hpc), performance at leadership computing facilities, performance portability, refactoring
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
