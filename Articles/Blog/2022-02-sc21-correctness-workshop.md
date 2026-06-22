# Celebrating the Fifth Anniversary of the Correctness Workshop: Looking Back and Looking Forward

**Hero Image:**

 - <img src='https://github.com/betterscientificsoftware/bssw.io/raw/main/images/Blog_2112_SC21.png' />

#### Contributed by: [Ignacio Laguna](https://github.com/ilagunap) and [Cindy Rubio-González](https://github.com/crubiog)
#### Publication date: February 22, 2022

In 2021, the International Workshop on Software Correctness for HPC Applications
(Correctness) celebrated its fifth anniversary at the Supercomputing (SC)
conference. To mark this occasion, the co-organizers, Ignacio Laguna (LLNL) and
Cindy Rubio-González (UC Davis), are proud to share this article, reflecting on
its inception and providing their perspective looking forward.

## Workshop History

The Correctness workshop started as an attempt to bring together researchers and
developers to discuss ideas on the problem of correctness in HPC and scientific
software. Over the last decades, the computer science community has seen
significant advances in the areas of debugging, testing, and verification for
non-HPC and non-scientific applications. However, it has been found that applying existing approaches to debug, test, and verify HPC software is much more complicated than for non-HPC software.

Some of the reasons that make correctness in HPC difficult are: growing use of
mixed programming models in scientific software, increasing use of
accelerators in HPC systems, the use of different levels of floating-point
precision, and compiler optimizations that can change the semantics
and correctness of programs (sometimes producing different results between CPU
and GPU executions). In general, porting code across multiple platforms and
reproducing numerical results (or statistics of such results) is one of the
biggest challenges that scientific computing programmers face today.

While performance is the primary driver of innovation in HPC conferences such as
SC, the co-organizers thought that innovation in software correctness was needed
to address several existing challenges in HPC. The SC conference was the
appropriate venue for the workshop since it gathers a large number of
researchers and practitioners annually. Since its inception in 2017, the
workshop has provided a forum for discussions on software correctness in the HPC
and scientific computing community.

## Topics and Attendance

The workshop is attended annually by dozens of participants from several
countries. Thirty four papers have been presented and published as part of the
Correctness workshop over the past five years. The papers have touched on
numerous topics of interest in scientific software, including correctness in MPI
and OpenMP programs, floating-point error detection, data race checking,
debugging tools, mixed-precision correctness, correctness in algorithms and
applications, and correctness in emerging programming models.

<br>

[A word cloud from the titles of the papers published in the first five years of the Correctness workshop]<img src='../../images/wordcloud_correctness_article.png' class='page'>

<br>

The workshop has had the honor of hosting six keynote speakers who have shared
their work and thoughts on the importance and challenges of software
correctness: Stephen Siegel (University of Delaware), Ganesh Gopalakrishnan
(University of Utah), Jim Demmel (UC Berkeley), Alex Aiken (Stanford
University), Allison Baker (NCAR), and David Bailey (LBNL and UC Davis).

## Community Impact

Before the Correctness workshop, the community did not have a specific venue to
discuss important topics about the correctness of scientific software. Some
discussions occurred during the presentation of technical papers at the SC
conference; however, such discussions most often emerged in the context of 
papers which were not related to correctness. The
workshop has served as a venue to bring together the community and enable such
discussions in a dedicated forum.

With several US-based and international attendees, various collaborations among
researchers have emerged due to presentations and discussions at the workshop.
In addition, an essential role of the workshop has been connecting scientists
and tool developers. This connection is crucial for scientists to express their
needs and tool developers to receive feedback on their tools.

Training and mentoring young researchers have played another critical role in
the workshop. The workshop has opened the opportunity for training junior
researchers by participating in the program committee and for connecting
students with internship and job opportunities.

## Looking Forward

With programming models and HPC systems becoming more complex and heterogeneous,
correctness will continue to be a challenge in scientific software—the workshop
will continue to provide a venue for discussing methods, tools, and techniques
to address such a challenge.

This year, the workshop hosted a panel discussion on a future tool competition
to promote the adoption of correctness tools and make existing tools more robust
and usable. Moving forward, the co-organizers expect that emerging areas in HPC,
such as machine learning, artificial intelligence, and quantum computing, may
pose increasingly more significant correctness challenges, which will require a
larger community to be solved. The co-organizers also would like to encourage
the scientific software community to contribute to the workshop by submitting
papers or suggesting speakers or panel topics.

## Additional Resources

* Workshop web sites: [2017](https://correctness-workshop.github.io/2017/), [2018](https://correctness-workshop.github.io/2018/), [2019](https://correctness-workshop.github.io/2019/), [2020](https://correctness-workshop.github.io/2020/), [2021](https://correctness-workshop.github.io/2021/)
* Workshop proceedings: [2017](https://doi.org/10.1145/3145344), [2018](https://doi.org/10.1109/Correctness46496.2018), [2019](https://doi.org/10.1109/Correctness49594.2019), [2020](https://doi.org/10.1109/Correctness51934.2020), [2021](https://doi.org/10.1109/Correctness54621.2021)

## Author bios

Ignacio Laguna is a Computer Scientist at the Center for Applied Scientific Computing (CASC) at the Lawrence Livermore National Laboratory (LLNL), California. His main area of research is programming models and systems for high-performance computing. He is particularly interested in software correctness, program analysis, compilers, fault tolerance, and debugging. He received his PhD degree in Computer Engineering from Purdue University in 2012 and is the co-founder of the International Workshop on Software Correctness for HPC Applications (Correctness), which has been held at SC for several years.

Cindy Rubio-González is an Associate Professor of Computer Science at UC Davis.  She received her Ph.D. from UW-Madison in 2012, and was a Postdoctoral Researcher at UC Berkeley before joining UC Davis. Her research spans the areas of Programming Languages and Software Engineering, with a focus on program analysis and software testing for automated bug finding and program optimization. She is particularly interested in the reliability and performance of systems software and scientific applications. Cindy is a recipient of several awards including a DOE Early Career award and an NSF CAREER award, and is a co-founder of the Correctness workshop.

<!---
Publish: yes
Track: community
Pinned: no
Topics: conferences and workshops, reproducibility, debugging
--->
