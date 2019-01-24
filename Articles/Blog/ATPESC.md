# ATPESC Story Title

#### Contributed by [Marta Garcia Martinez](https://github.com/??)

#### Publication date: January 29, 2019

**Hero Image:**
 
- <img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0119_32311D13_crop.jpg' />

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<br>

<!--- Image to illustrate the complexity of EXAALT --->
<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0918_EXAALTfwork_1250_729.png' class='page' /><p class='caption'>Figure 1. Illustration of the EXAALT framework. The three main software components (LAMMPS, LATTE, and ParSplice) are represented as colored circles, while other libraries are represented as grey circles. Lines (graph edges) depict dependencies between the various software components.</p>

<br>

### Header 1
In 2017, LANL focused its annual [IS&T Co-Design Summer School] (http://lanl.github.io/cdss/history.html) program on the topic of accelerated molecular dynamics (AMD).  The idea was to gather a small group of elite graduate students to help optimize the performance of ParSplice, the AMD driver of EXAALT.  During the early weeks of that summer, the developers of ParSplice quickly recognized that their rapidly evolving code had become difficult for the typical (and even advanced) computational scientist to compile and run.  The reason was that the existing build system (or lack thereof) was becoming prohibitively difficult to negotiate.

The summer students overcame their early technical difficulties and accomplished great feats.  However, the experience inspired the EXAALT team to be more proactive about future productivity issues.  That is, the members decided to collaborate closely with members of the [IDEAS-ECP] (https://ideas-productivity.org/ideas-ecp/) project, to adopt modern and sustainable software-development practices.  In the short term, this decision meant the implementation of a more user-friendly and portable build system (compared with the manual Makefile-based compilation of several different packages). In the longer term, this meant the development of a continuous-integration (CI) pipeline to first automate build testing and ultimately accelerate all quality-control efforts.  

### Header 2

The fruitful EXAALT-IDEAS collaboration, which is still ongoing between researchers at LANL and Argonne National Laboratory (ANL), has proven mutually beneficial to both teams: providing EXAALT with technical advice and providing IDEAS with clear insight into the fundamental needs of an ECP application project. To help the IDEAS team map their collaboration efforts onto a manageable set of tasks, the group leveraged the [Productivity and Sustainability Improvement Planning (PSIP)] (https://bssw.io/resources/planning-for-better-software-psip-tools "PSIP Planning") process. For the first stage of the collaboration, the construction of a minimal end-to-end CMake build system, this process was implicitly used for project planning and execution. The work required CMake script/module implementations within all three major framework components (LAMMPS example: [CMakeLists.txt] (https://github.com/lammps/lammps/blob/master/cmake/CMakeLists.txt)). For the second (ongoing) stage, PSIP was followed more explicitly by compiling the *planning/tracking cards* shown in Figure 2 (in summarized form).   


One significant advantage of the PSIP management approach is that it forces the team to specify the 4-6 steps needed to reach a given goal.  In this case, the process helped formulate the actionable items needed to lay the foundation for CI within the existing EXAALT [software repository] (https://gitlab.com/exaalt).  Although PSIP can be used to manage the goals of any software project, the specific details of each step are highly dependent on the project.  For example, different projects will most likely need to work with slightly different technologies to build a practical CI pipeline.  Specific details will depend on where and how the repository is organized, as well as the limitations/capabilities of the existing library dependencies.  For EXAALT, after careful discussion between teams, it was decided that the CI pipeline would need to depend on four key technologies:

- [CMake] (https://cmake.org/): To manage the end-to-end compilation and testing execution using CTest
- [Boost] (https://www.boost.org/): To implement and organize functionality tests (integration, regression, and unit) inside CTest
- [GitLab CI] (https://about.gitlab.com/features/gitlab-ci-cd/): To automatically build and test the software framework (using CMake) to validate new repository commits (usually using docker)
- [Docker] (https://www.docker.com/): To generate standard system images (with library dependencies) for use in GitLab CI

### Author Bio
Richard Zamora is an assistant computer scientist in the [ALCF](https://www.alcf.anl.gov/) Data Science group at Argonne National Laboratory.  His research focuses on the development and optimization of parallel software for high-performance computing and machine learning. Before joining Argonne, Richard worked in the Theoretical Division at Los Alamos National Laboratory, where he was heavily involved in the design and application of accelerated molecular dynamics algorithms. While working on the EXAALT package at LANL, he helped manage the official software repository, and he has since taken a special interest in sustainable and productive development practices. 


<!---
Publish: preview
RSS update: 2018-09-25
Categories: reliability
Topics: training, ??
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
