# Practical Reproducibility: Building a More Robust Research Ecosystem

#### Contributed by [Kate Keahey](https://github.com/keahey) and [Marc Richardson](https://github.com/marcwitasee)

#### Publication date: October 23, 2024

<!--deck start-->
The community needs to address many questions to work toward practical reproducibility throughout the research ecosystem.   
<!--deck end-->

There is broad agreement that in the digital age, science should be shared digitally through artifacts such as code and data. [The adoption of practices enabling the reproducibility of computational results can lead to more robust science and increased scientific productivity](https://wordpress.cels.anl.gov/nimbusproject/wp-content/uploads/sites/116/2023/08/Reproducibility_On_Chameleon-3.pdf). While the computer science community actively supports initiatives like artifact evaluation at conferences, data preservation efforts, and reproducibility hackathons, it remains unclear how much science gets reproduced beyond these targeted initiatives.

Unless reproducing research becomes as vital and mainstream a part of scientific exploration as reading papers is today, reproducibility will be hard to sustain. The incentives to make research results reproducible won't outweigh the considerable costs of making them so. Thus, in addition to seeking ways to ensure that every experiment can be repeated regardless of effort, we should explore mechanisms for practical reproducibility—where many experiments are packaged in such a way that they can be repeated cost effectively.

Imagine a research ecosystem where scientists could "click-through" results presented in a paper, reproduce experiments, or redo data analysis to try it on different hardware. Researchers could introduce variations into algorithms and provide side-by-side comparisons or answer new questions with available data. Rather than just reading about new research, scientists could explore science interactively, immediately verify or challenge results, extend them on the fly, or more easily integrate new research into teaching. This approach could accelerate the evolution of curricula to keep pace with advancing science.

### The critical role of infrastructure in research reproducibility

Supporting practical reproducibility in computer science requires dedicated infrastructure that makes reproducing research as natural as reading papers. Open, programmable experimental platforms are essential, as computational research artifacts typically require specific computing environments to interpret and validate, especially in high-performance computing. Beyond just providing resources, infrastructure must actively promote reproducibility through features that make it easier to package, share, and reproduce experiments while creating incentives that align with the academic goals of both experiment authors and reviewers.

[Chameleon](https://chameleoncloud.org) is one such testbed that is taking this challenge seriously. As an NSF-funded testbed supporting over 11,000 users working on more than 1,300 projects with over 750 publications, Chameleon provides bare metal reconfigurability that enables precise replication of experimental environments. The platform has become integral to reproducibility initiatives across major computer science conferences, including SC, ICPP, SIGCOMM, FAST, OSDI/ATC, and EuroSys. Through its [python-chi library](https://python-chi.readthedocs.io/), researchers can programmatically create and manage experimental environments. At the same time, [Trovi](https://trovi.chameleoncloud.org/dashboard/), Chameleon's artifact repository, enables the sharing and discovery of packaged experiments with built-in metrics to measure impact. The [Chameleon Daypass](https://chameleoncloud.readthedocs.io/en/latest/technical/daypass.html) feature allows experiment authors to provide reviewers with temporary access specifically for reproducing experiments, removing traditional barriers to validation. These tools, combined with Jupyter integration for experiment documentation, integration with GitHub, and automated DOI assignment for citation tracking, create a comprehensive ecosystem that makes reproducing research more practical and accessible.

### Fostering reproducibility initiatives: Beyond the platform

While pubic research infrastructure has brought practical reproducibility within reach, significant challenges remain in fully achieving the vision in computer science research, extending far beyond platform-level solutions. These challenges require careful consideration and input from all members of the research community—from organizers of reproducibility initiatives to authors, reviewers, tool developers, and platform providers alike. Many fundamental questions still need to be clearly defined before we can begin offering solutions: How do we create seamless transitions between different stages of experimentation? What incentive structures will effectively encourage researchers to prioritize reproducibility? How do we ensure the long-term sustainability of research artifacts? How do we address the fact that some experiments are more complicated to replicate than others? These questions touch on technical, social, and institutional aspects of how we conduct and share research, making the questions impossible to address without broad community engagement and consensus building.

### First steps toward consensus: [Community Workshop on Practical Reproducibility in HPC](https://reproduciblehpc.org)

To explore these critical questions and foster discussion around practical reproducibility and the unique challenges faced in HPC, we are hosting a workshop on November 18, 2024, in Atlanta, GA. This workshop will bring together authors, reviewers, tool developers, and researchers interested in advancing practical reproducibility in computer science. Together, we can work toward making reproducibility a natural and integral part of the research process.

*For more information and registration details, visit [reproduciblehpc.org](https://reproduciblehpc.org).*

### Author bios

[Kate Keahey](https://cs.uchicago.edu/people/kate-keahey) is one of the pioneers of infrastructure cloud computing. She created the [Nimbus project](http://www.nimbusproject.org/), recognized as the first open source Infrastructure-as-a-Service implementation, and continues to work on research aligning cloud computing concepts with the needs of scientific datacenters and applications. To facilitate such research for the community at large, Kate leads the [Chameleon project](http://www.chameleoncloud.org/), providing a deeply reconfigurable, large-scale, and open experimental platform for computer science research. To foster the recognition of contributions to science made by software projects, Kate co-founded and serves as co-Editor-in-Chief of the [SoftwareX journal](http://www.journals.elsevier.com/softwarex/), a new format designed to publish software contributions. Kate is a Scientist at Argonne National Laboratory and a Senior Scientist The University of Chicago Consortium for Advanced Science and Engineering (UChicago CASE).

[Marc Richardson](https://www.linkedin.com/in/marcwitasee) is the technical project manager for Chameleon Cloud and 3 other NSF-funded CS projects at the University of Chicago. He holds an undergraduate degree in Economics and International Relations from William & Mary and a master’s degree in Computational Analysis and Public Policy from the University of Chicago. Before shifting gears to technical project management, Marc worked as an analyst in economic consulting at a firm that specialized in high-tech markets. He has served a variety of research groups at UChicago (Nimbus Project and Internet Equity Initiative) and mentored students in Data Science and Computer Science. On his time off, Marc is exploring the globe for the tastiest food or skiing in his home state of Colorado.


<!---
Publish: yes
Track: community
Topics: conferences and workshops, reproducibility
--->
