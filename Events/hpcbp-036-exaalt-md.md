# Webinar: Refactoring EXAALT MD for Emerging Architectures

- Date: 2020-01-15
- Location: Online
- Event Website: https://ideas-productivity.org/resources/series/hpc-best-practices-webinars/#webinar036
- Organizers: The IDEAS Productivity Project
			   
This event is a part of the "Best Practices for HPC Software
Developers" webinar series, produced by the IDEAS Productivity
Project. The HPC Best Practices webinars address issues faced by
developers of computational science and engineering (CSE) software on
high-performance computers (HPC) and occur approximately monthly.

Resource Information | Details
:--- | :---			   
Webinar Title | Refactoring EXAALT MD for Emerging Architectures
Date and Time | 2020-01-15 01:00 pm EST
Presenters | Aidan Thompson (<a href="http://www.sandia.gov/">Sandia National Laboratories</a>), Stan Moore (<a href="http://www.sandia.gov/">Sandia National Laboratories</a>),  and Rahulkumar Gayatri (<a href="http://www.nersc.gov/">National Energy Research Scientific Computing Center</a>)
Registration, Information, and Archives | 	<https://ideas-productivity.org/resources/series/hpc-best-practices-webinars/#webinar036>	   

**Webinars are free and open to the public, but advance registration is required through the Event website. Archives (recording, slides, Q&A) will be posted at the same link soon after the event.**

### Abstract
<p>As part of the DOE Exascale Computing Project, members of the EXAALT project are working to increase the accuracy, time, and length scales of molecular dynamics simulations of materials for fusion energy. Simulations rely on the SNAP machine-learning interatomic potential to accurately capture material properties. The SNAP kernel recursively evaluates a set of complex polynomial functions, requiring many deeply nested loops with irregular loop bounds. Last year, a worrisome trend in the SNAP force kernel was identified. With each new generation of emerging architectures, performance relative to theoretical peak was decreasing, particularly on GPUs. This webinar will discuss the approach used to rewrite the SNAP kernel from the ground up, using more compact memory representation, refactoring the main loop, using sub-kernels to reduce pressure on GPU threads, and improving coalesced memory accesses on the GPU. This work has enabled a spectacular increase of roughly 10x in performance over the baseline implementation of the SNAP benchmark running on NVIDIA V100 GPUs. Extrapolated to the full machine, this predicts an increase of over 100x in the Figure of Merit over the baseline on the ALCF/Mira system, putting EXAALT on track to meeting, and even exceeding performance targets on exascale systems. The webinar will emphasize key strategies and lessons learned in code transitions for emerging architectures.</p>



### Presenter Bios
<p>Dr. Thompson earned his undergraduate degree in Chemical Engineering at University College, Dublin, Ireland. He earned his Ph.D in Chemical Engineering at the University of Pennsylvania, 1994 in the area of statistical thermodynamics of complex fluids. Since 1997 he has worked in the Center for Computing Research at Sandia National Laboratories, first as a post-doctoral appointee, and since 2002 as principal member of the technical staff. Throughout that time he has worked as one of the core developers of the LAMMPS molecular dynamics code, while at the same time using it to study the atomic-to-mesoscale behavior of a wide variety of materials, described in over 50 publications. In recent years, frustrated with the limited accuracy of classical potentials, he has become a leading developer of machine-learned interatomic potentials fit to large databases of quantum calculations.</p>
<p>Stan Moore is a computational scientist at Sandia National Laboratories specializing in particle-based simulation methods such as molecular dynamics and direct simulation Monte-Carlo. He is a software developer of the LAMMPS and SPARTA codes, and his research currently focuses on extending particle-based codes to use Sandia’s Kokkos performance portability library to run efficiently on next-generation supercomputing platforms. Stan earned a PhD in chemical engineering from Brigham Young University, where his research focused on developing a new method to predict chemical potential using molecular simulations.</p>
<p>Rahulkumar (Rahul) Gayatri is an Application Performance Specialist at NERSC, LBNL. He is an HPC engineer and works closely with the application development teams to optimize compute intensive kernels in their code for future generation architectures. He is currently working with the LAMMPS team in the EXAALT ECP project to optimize the SNAP module for NVIDIA GPUs. He is also interested in testing the efficiency of OpenMP target directives as a paradigm to offload kernels onto GPUs. Rahul obtained his PhD in the field of Parallel Programming Models from Barcelona Supercomputing Center. His research focus was on speculative task execution in OMPSs, a task based programming model.</p>

    

#### Contributed by Aidan Thompson, [Stan Moore](https://github.com/stanmoore1 "Stan Moore GitHub profile"),  and [Rahulkumar Gayatri](https://github.com/rgayatri23 "Rahulkumar Gayatri GitHub profile")

#### Publication date: January 15, 2020

<!---
Publish: yes
Categories: skills
Topics: online learning
Level: 2
Prerequisites: default
Aggregate: none
--->
