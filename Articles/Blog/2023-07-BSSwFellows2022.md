# 2022 BSSw Fellows: Projects and Perspectives

Read about the 2022 BSSw Fellows and their contributions to the BSSw community!

<img src='../../images/Blog_2307_BSSwFellows.png'>

#### Contributed by:
[Elsa Gonsiorowski](https://github.com/gonsie "Elsa Gonsiorowski's GitHub Profile"),
[Ritu Arora](https://github.com/ritua2 "Ritu Arora's GitHub Profile"),
[Rob Latham](https://github.com/roblatham00 "Rob Latham's GitHub Profile"),
[Julia Lowndes](https://github.com/jules32 "Julia Lowndes's GitHub Profile"),
[Amiya Maji](https://github.com/amaji "Amiya Maji's GitHub Profile"),
[Nitin Sukhija](https://github.com/ "Nitin Sukhija's GitHub Profile"),
[Karan Vahi](https://github.com/vahi "Karan Vahi's GitHub Profile")


#### Publication date: July 26, 2023

[Better Scientific Software (BSSw) Fellowships](https://bssw.io/fellowship) provide resources and community support to those who foster and promote practices, processes, and tools to improve developer productivity and software sustainability of scientific codes.

The 2022 BSSw Fellows have used their skills to create tutorials, webinars, and tools to guide developers through various stages of the scientific software lifecycle and impact the culture of scientific software development.

Here's more about what they have been up to and their perspectives on the BSSw Fellowship Program.

### Optimizing I/O of scientific applications can be critical to simulation performance but is usually an afterthought in application development.

Ritu will create videos, articles/blogs, and examples/exercises to demonstrate how to optimize I/O in scientific applications including the area of AI/machine learning. Her materials will cover the following topics: (1) Optimizing I/O in serial and parallel applications written in C, C++, Fortran, Python, and R; (2) optimally writing and reading checkpoints in serial and parallel applications written using C, C++, Fortran, Python, R, MPI, OpenMP, and CUDA; (3) optimizing I/O and checkpointing AI/machine learning models/applications; and (4) techniques for leveraging the features in the underlying hardware and filesystems (e.g., Lustre) for optimizing applications’ I/O while being aware of portability issues. The videos will be posted on YouTube, sample code will be posted in a GitHub repository, and the blogs will be shared as LinkedIn articles and BSSw.io blogs.

<a href="URL" class="link-row">Link Text</a>

<br>

<div class='fellow'>
<div class='img_div'>
  <img src='../../images/People_RituArora.jpg' class='logo' />
</div>

<div class='short_bio'>
<p><!-- TODO: is Wayne state the right URL? -->
<a href="https://wayne.edu/people/hg8255">Ritu</a> is a faculty member in the Computer Science department at Wayne State University. She is also the founder of <a href="https://www.venratech.com/home">Venra Tech Inc.</a>, a company that provides solutions for advanced computing, data management, visualization, AI, and IT infrastructure development. Prior to joining Wayne State University, Ritu led the Research computing portfolio at the University of Texas at San Antonio (UTSA). She specializes in designing high-productivity and scalable infrastructure for powering discoveries and has led the development of the software infrastructure for integrating and efficiently utilizing supercomputing, cloud computing, and volunteer computing resources. Her areas of expertise and interest include High Performance Computing (HPC), data-intensive computing, cloud computing, advanced software engineering, and health informatics. Prior to joining UTSA, Ritu worked at the University of Texas (UT) at Austin, where she was appointed as a Research Scientist at the Texas Advanced Computing Center (TACC), and as Associated Faculty in the Department of Statistics and Data Sciences. Ritu received her Ph.D. in Computer and Information Science from the University of Alabama at Birmingham in 2010. She passionately promotes the use of technology for creating social impact, and actively engages in the causes for creating inclusive policies and communities.
</p>
</div>
</div>

*Perspectives on the BSSw Fellowship Program:* I am very grateful to the BSSw Fellowship Program team for selecting me and giving me an opportunity to highlight the cause of optimizing I/O in scientific applications. Through this fellowship, I was able to expand my professional network and the target audience for my tutorial on "Optimizing I/O in Scientific Applications". Due to the fellowship, I was able to take time and focus on expanding and updating my previous content on optimizing I/O. I also got a chance to attend the ECP meeting in January 2023 and learn about the great work that colleagues at the DOE laboratories are doing. It feels great to be a part of a very supoortive community!

*Advice for new (prospective) BSSw Fellows:* I would suggest proposing a topic that you are very passionate about and deciding on the scope of the proposed work to be undertaken well in advance.


- - -

### I/O sleuthing to track down errors in performance or correctness - at scale!

We often see computational science codes focusing on I/O only when something has gone wrong: A job took longer than expected, data was incorrect, or obscure failure messages come back from the storage system. Diagnosing and debugging I/O problems share many similarities to debugging any parallel application, but do have their own peculiarities and tools. In this one-day course Rob will cover the kinds of I/O problems one is likely to encounter in HPC, how to investigate those problems, and how to fix them.

<a href="URL" class="link-row">Link Text</a>

<br>

<div class='fellow'>
<div class='img_div'>
  <img src='../../images/People_LathamRobert.jpg' class='logo' />
</div>

<div class='short_bio'>
<p><a href="https://www.mcs.anl.gov/~robl/">Rob</a> strives to make scientific applications use I/O more efficiently. After earning his BS (1999) and MS (2000) in Computer Engineering at Lehigh University (Bethlehem, PA), he eventually ended up at Argonne National Laboratory (ANL). His research focus has been on high performance I/O for scientific applications and I/O metrics. He has worked on the ROMIO MPI-IO implementation, the parallel file systems PVFS (v1 and v2), Parallel NetCDF, and Mochi I/O services.
</p>
</div>
</div>

*Perspectives on the BSSw Fellowship Program:*

I have enjoyed seeing the concept of the Research Software Developer emerge
over the course of my career.  BSSW supports scientific software and elevates
the work developers like me carry out.  This program has connected me to lots
of bright folks and given me a peek at some of the good work going on across
the laboratory complex.

I've been giving I/O tutorials for quite a few years at this point in my
career.  With BSSW fellowship support, I reframed my typical I/O tutorial into
more of an ongoing collaboration.  I leaned on GitHub discussions for audience
engagement and structured my materials to accommodate contributions from users
running on other HPC platforms.


*Advice for new (prospective) BSSw Fellows:*

For new and future BSSw Fellows, recognize there's a tension between taking
risks and completing the task in the time allotted.  We aren't given endless
time and money -- but who is? As in many fields, operating under gentle
constraints can bring out creativity.  I appreciated BSSw's charge to produce
something that could live on once the fellowship is over.

- - -

### Increasing the value of open scientific software through helping researchers engage with existing open source tooling and communities rather than reinventing on their own

Julia empowers researchers with technical, team and leadership skills for data-intensive open science through Openscapes, which she founded and co-directs. Openscapes helps researchers do “better science for future us” – data-intensive science that is reproducible and transparent; enabled by open source software; and underscored by sustainability, inclusion, and kindness. Julia’s work focuses on the Openscapes Champions Program, a remote cohort series that is not a typical training workshop – it is an interactive co-learning experience where learners bring their own research projects and are able to make tangible progress together with their teams and with a cohort of peers. During the BSSw Fellowship, Julia will improve publicly accessible open educational resources: the Openscapes Champions Lesson Series (https://openscapes.org/series) that are available for Champions program participants as well as self-paced learning for everyone.

<a href="URL" class="link-row">Link Text</a>

<br>

<div class='fellow'>
<div class='img_div'>
  <img src='../../images/People_Lowndes_v2.jpg' class='logo' />
</div>

<div class='short_bio'>
<p><a href="https://jules32.github.io/">Julia</a>is Founder and Co-Director of Openscapes, championing kinder, better science for future us through open science and teamwork. As a marine data scientist, Mozilla Fellow ‘19 and Senior Fellow at NCEAS, she has nearly ten years designing and leading programs to empower science teams with skill sets and mindsets for reproducible research, empowering researchers with existing open tools and communities. She has been building communities of practice in this space since 2013 with the Ocean Health Index after earning her PhD at Stanford University studying drivers and impacts of Humboldt squid in a changing climate. She is a Carpentries instructor and a co-founder of Eco-Data-Science and R-Ladies Santa Barbara. Follow her on Twitter <a href="https://twitter.com/juliesquid">@juliesquid</a>.
</p>
</div>
</div>

*Perspectives on the BSSw Fellowship Program:*

*Advice for new (prospective) BSSw Fellows:*

- - -

### Simplifying scientific Python package installation and environment management

Amiya works to simplify scientific Python package installation by streamlining environment management, dependency tracking, and runtime customizations through easy-to-use tools. With the growing popularity of Python, installation and management of python packages on HPC clusters is emerging as a critical problem for researchers and is complicated by the need for providing consistency across traditional batch workloads and interactive notebooks. Amiya will collaborate with various HPC centers to document and present their best practices for managing Python applications and implement these practices in the development of the python-env-mod tool to simplify these processes. Python-env-mod helps users manage their Python environments more efficiently and load runtime configurations through the familiar abstraction of environment modules. HPC centers can further customize the module file templates to incorporate additional software dependencies and provide descriptive help messages. This work will significantly improve scientific productivity, reduce user errors, and enable sharing of Python package installations among users.

<a href="URL" class="link-row">Link Text</a>

<br>

<div class='fellow'>
<div class='img_div'>
  <img src='../../images/People_AmiyaMaji.jpg' class='logo' />
</div>

<div class='short_bio'>
<p><a href="https://www.rcac.purdue.edu/about/staff/amaji">Amiya</a> is a Senior Computational Scientist at Purdue Research Computing where he collaborates with faculty and researchers from various scientific domains to optimize their computational and data analysis workflows. Being an avid advocate for software reliability and security, Amiya has developed several algorithms and tools for software testing both during his graduate studies at Purdue ECE and then at Research Computing. He co-invented the “Testpilot” regression testing framework at Purdue (HUST17) and also developed the “conda-env-mod” tool for easy deployment of scientific Python applications (HUST20). Amiya currently leads the software build automation project for Purdue’s community clusters. Amiya’s contributions towards the Community Cluster program were recognized by the Bravo Award (2020) given to Purdue employees for outstanding achievement. Amiya also serves as a fellow of Trusted CI (2021) where he promotes best practices for secure computing.
</p>
</div>
</div>

*Perspectives on the BSSw Fellowship Program:*

I have always been passionate about writing robust software and spent countless hours finding
and fixing bugs (and creating a few myself!). In the BSSw Fellowship program, I found
a community of like-minded individuals who are all passionate about raising the quality of
scientific software through collaboration and dissemination of best practices. I am thankful to
the BSSw Fellowship committee for providing me the opportunity to explore the best practices for
installing and managing scientific python packages. During my work at Purdue Univeristy, I had the
first-hand experience of seeing researchers struggle with installation of Python packages on HPC
clusters. To alleviate many of the common issues, I wrote a tool called [conda-env-mod](https://github.com/amaji/conda-env-mod) which
simplified the process of python environment creation, dependency tracking, and usage. The BSSw
Fellowship helped me expand the project and shape it into a more useful tool. I am hopeful that it will
help HPC python developers manage their python environments more efficiently.

The BSSw Fellowship has helped me connect with the larger RSE community and learn about the
experiences of other scientists. I am also thankful for all the feedback that I have received
about best practices for managing HPC python packages. It was oddly encouraging to see that I was
not alone in my struggles with Python package installation! I will continue to cherish the collective
knowledge, support, and encouragement of the BSSw community.


*Advice for new (prospective) BSSw Fellows:*

For new and future Fellows, I'll echo the advice of the previous Fellows. Once you start working on
your project, it may quickly expand into a larger research problem. Identify the scope of your project and start early.
Take advantage of the great networking opportunities provided by the BSSw Fellowship and don't hesitate to reach out.

- - -

### Mitigate the risk of software vulnerabilities with best practices and tools for secure scientific software development

The sharp increase in computational power of computing ecosystems is likely to continue as we move toward exascale and beyond. In turn, we are seeing new convergent computing platforms along with a paradigm shift in scientific software applications leveraging these platforms. Unfortunately, this also leads to an unexpected growth in security risks pertaining to cybercriminals, as well as malicious insiders in the computing ecosystems. To address these issues, it is of paramount importance to integrate security within the scientific software development lifecycle. The need for best practices for secure software development has been highlighted in the President’s Executive Order on Improving the Nation’s Cybersecurity issued in May, 2021.

Nitin Sukhija will create a one-day workshop on securing scientific software development. The workshop components will include evaluating design practices for creating secure software, software processes for managing secure software, threat modeling, and quality assurance testing using both static and dynamic analysis tools. The workshop will include hands-on exercises with penetration testing tools and how to mitigate threats such as losing sensitive information due to a variety of potential vulnerabilities. The workshop is intended to aid members from diverse research domains in development of trustworthy and secure scientific software.

<a href="URL" class="link-row">Link Text</a>

<br>

<div class='fellow'>
<div class='img_div'>
  <img src='../../images/People_NitinSukhija.jpg' class='logo' />
</div>

<div class='short_bio'>
<p><a href="https://www.sru.edu/c2ac">Nitin</a> is an associate professor in the department of computer science and director of Center for Cybersecurity and Advanced Computing (C2AC) at Slippery Rock University of Pennsylvania. His areas of expertise are scientific computing focusing on performance modeling, robustness and resilience analysis, and cybersecurity.
</p>
</div>
</div>

*Perspectives on the BSSw Fellowship Program:*

*Advice for new (prospective) BSSw Fellows:*

- - -

### Enabling complex scientific computations and efficient use of HPC resources with scientific workflows

Karan will bring the use of workflows to the wider scientific community by developing easy to understand training materials that examine the workflow lifecycle and challenges associated with various steps such as creation, execution, monitoring and debugging. Workflows are needed to capture the complex interdependencies between processing steps in data analysis and simulation pipelines as well as the mechanisms to execute those steps reliably and efficiently. The training will walk users through how to model existing simulation pipelines into workflows, how to package application code in containers, and how to execute the workflow on HPC resources and distributed computing infrastructure such as Open Science Grid. The training materials will also build on existing interactive Jupyter notebooks that guide users on how to develop workflows using Pegasus (http://pegasus.isi.edu). The training materials will be self-guided and also well-suited for use in classroom teaching and virtually.

<a href="URL" class="link-row">Link Text</a>

<br>

<div class='fellow'>
<div class='img_div'>
  <img src='../../images/People_VahiKaran.jpg' class='logo' />
</div>

<div class='short_bio'>
<p><a href="https://www.isi.edu/people/vahi/about">Karan</a>is a Senior Computer Scientist in the Science Automation Technologies group at the USC Information Sciences Institute. He has been working in the field of scientific workflows since 2002, and has been closely involved in the development of the Pegasus Workflow Management System. He is currently the architect/lead developer for Pegasus and in charge of the core development of Pegasus. His work on implementing integrity checking in Pegasus for scientific workflows won the best paper and the Phil Andrews Most Transformative Research Award at PEARC19.
</p>
</div>
</div>

*Perspectives on the BSSw Fellowship Program:*

*Advice for new (prospective) BSSw Fellows:*

- - -

### Learn more about the BSSw Fellowship Program

BSSw Fellows are selected annually based on an application process that includes the proposal of a funded activity that promotes better scientific software. See more about the [BSSw Fellowship Program](https://bssw.io/fellowship), including ongoing work of the 2023 BSSw Fellows. We will begin accepting applications for 2024 BSSw Fellowships during mid-August 2023. Register for the [BSSw mailing list](https://bssw.io/pages/receive-our-email-digest) to receive information.

### Author bio

Elsa Gonsiorowski is deputy coordinator of the BSSw Fellowship Program, a member of the [IDEAS-ECP](https://ideas-productivity.org/ideas-ecp) team, and HPC I/O support specialist at [Livermore Computing, LLNL](https://hpc.llnl.gov/about-us).


<!---
Publish: yes
Pinned: no
Topics: Projects and organizations
RSS update: 2023-07-26
--->
