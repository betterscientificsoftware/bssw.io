# Software Deployment: Bringing resources into effective action

#### Contributed by [Shahzeb Siddiqui](https://github.com/shahzebsiddiqui), [Sameer Shende](https://github.com/sameershende)

#### Publication date: June XX, 2022

## Introduction

Software development involves the step-by-step process of inventing, specifying,
coding, recording, testing and fixing bugs.  But, just because you’ve built it 
doesn’t mean it’s ready for prime time. Software deployment is a set of crucial 
activities that takes software and makes it available for use on the target 
system. 

Many of us deploy software for ourselves - build, test, set up paths, etc. But,
as our software grows in capability, so also can the deployment process grow in 
complexity. The High-Performance Computing (HPC) software landscape contains a 
wide range of workloads that require third-party software and commercial 
products to be installed on HPC systems.  This complexity requires expertise 
from HPC centers to invest time in deploying a software stack to meet the needs 
of their user community and ensure software runs with optimal performance on the 
target system architecture.

*What is your software deployment strategy at your organization?* *Have you 
thought about how you plan to build, install and deploy a software stack that 
can be sustainable for the lifetime of an HPC system?* 

Every community needs to think about their software deployment strategy, 
including:

- **Users** need to think about how to create a portable and reproducible 
environment, perhaps using containers versus software provided on the system vs 
building their own stack such as spack, conda, pip, easybuild.
- **Developers** of software need to think about how to make it easier for users 
to use their software, software dependencies, and correct usage.
- **HPC facilities** need to think about how to support a large community of 
users, opting to install some software packages and using modules for easier
deployment.

When deploying a software stack, you may want to consider the following
- *What type of workloads do your users run?*
- *How many versions of particular software should you support?*
- *To what extent do you want to support the Python, R, Ruby, Perl, and Anaconda 
software ecosystem or should this be responsibility of user?*
- *Should the facility install any software requested by the user or have a 
formal process for software request that goes through a review process?* 
- *Determine what software needs to be installed by HPC centers vs which software 
needs to be managed by users or groups?* 

## Software Deployment in an HPC Environment

In an HPC environment, this complexity requires a community to tackle the issue.  
The [Extreme-scale Scientific Software Stack (E4S)](https://e4s.readthedocs.io/en/latest/introduction.html)
is a community effort supported by the [Exascale Computing Project (ECP)](http://exascaleproject.org)
to provide open source software packages for developing, deploying and running 
scientific applications on high-performance computing (HPC) platforms. Even with 
software seemingly packaged and delivered with a bow like E4S, the actual 
deployment can be fraught with pitfalls and decisions to make for site-specific 
customizations. 

E4S is a collection of 100+ top-level scientific software packages needed
for scientific computing in high-performance computing (HPC) environments.  
E4S member packages must demonstrate compatibility with the E4S
[community policies](https://e4s-project.github.io/policies.html), 
including a production quality spack-based build and installation procedure. 
The Department of Energy Office of Science (DOE SC)
[Advanced Scientific Computing Research](https://www.energy.gov/science/ascr/advanced-scientific-computing-research)
Facilities (NERSC, OLCF and ALCF) are expected to build and deploy E4S on 
thepre-exascale system, which helps to ensure a consistent programming environment 
for users across facilities. 

In 2021, [National Energy Research Scientific Computing Center (NERSC)](https://nersc.gov/)
released their first deployment of E4S/20.10 on Cori using the [spack](https://spack.io/) 
package manager. We wanted to leverage E4S to enable ECP and NERSC users to accelerate 
their scientific research with updated versions of software products needed for 
simulations and to provide feedback to ECP 
[Software Technology](https://www.exascaleproject.org/research/#software) 
teams with build failures during deployment so they can be fixed in future versions. 
Here, we describe the steps and lessons learned to deploy the E4S software stack at 
NERSC to help you navigate your E4S deployment.  The lessons learned can also 
guide future developers of packaged community software on development-to-deployment 
requirements. Here is the [link](https://www.osti.gov/biblio/1868332-software-deployment-process-nersc-deploying-extreme-scale-scientific-software-stack-e4s-using-spack-national-energy-research-scientific-computing-center-nersc)
to the full technical report. An HPC facility software deployment process is 
typically aligned with planned system upgrades, since both may require a rebuild 
of the full software stack. 


## Software Deployment Recipe at NERSC

Here the high-level steps to deploy E4S at NERSC
1.Acquire spack configuration from E4S Project (https://github.com/E4S-Project/e4s)
2. Configure your spack configuration with compilers, package preference and list of
packages to install
3. Build the entire spack stack via spack install using Gitlab 
4. Generate modulefiles for spack stack
5. Create user facing **e4s** modulefile
6. Write user documentation for e4s stack in  NERSC user documentation 
7. Share spack configuration in https://github.com/spack/spack-configs and update
E4S documentation page https://e4s.readthedocs.io/en/latest/facility_e4s.html 
8. Add announcement in NERSC weekly email

<img src='../../images/Blog_2205_SoftwareDeploymentProcess.png'>[Figure 1: NERSC Software Deployment Process from inception to deployment]

## Deployment Tools

We can also leverage containers to provide a software stack to end-users for 
instance E4S comes with several pre-built containers that can be ready to use 
instantly. If one supports containers the [Singularity Registry HPC](https://singularity-hpc.readthedocs.io/en/latest/) 
can be handy in converting containers into modules so one can access containers 
using the module command. 

We can leverage other packaging tools like [pip](https://pip.pypa.io/en/stable/)
and [conda](https://docs.conda.io/en/latest/) to support Python community, 
[gem](https://rubygems.org/) for Ruby, [cpan](https://www.cpan.org/) for Perl, 
[cran](https://cran.r-project.org/) for R community. 

The [NVIDIA GPU Cloud (NGC)](https://www.nvidia.com/en-us/gpu-cloud/) can be used 
to provide pre-built containers optimized for NVIDIA GPUs. 

[Spack](https://spack.io/) and [Easybuild](https://easybuild.io/) provide HPC 
teams to build software stack from source. 

The [OpenHPC](https://openhpc.community/) project is a community effort to 
provide tools for deploying HPC clusters including provision tools, 
resource manager, development tools and scientific libraries, you can deploy
OpenHPC at your site as a means to provide a Software Stack at your HPC site.

HPC support team should take into account user requirements and any monitoring
data such as module tracking or software library tracking such as [XALT](https://xalt.readthedocs.io/en/latest/) 
to see usage trends to determine which packages to install in their Software Stack. 

Software stack deployment requires intimate knowledge of the HPC system with 
in-depth knowledge of the software package to ensure each package is built 
optimally for the system. Nowadays, there is a wide variety of workloads running 
on HPC systems including AI, Data Analysis, Simulation & Modeling, remote sensor 
data and HPC center needs to support all types of workload applicable for their
site. 

This complexity requires a Software Deployment team as an integral part of 
HPC centers.  We need to train our existing staff and/or increase the workforce 
to support a comprehensive software stack, like E4S, at the facilities. HPC 
centers can also benefit from each other by learning the Software Deployment 
process, especially for centers that don’t have a well-established process. 

We welcome the community to share their deployment strategy and/or best 
practices for Software Stack Deployments. Let’s share game plans.


### Author bio

#### Shahzeb Siddiqui

[Shahzeb Siddiqui](https://github.com/shahzebsiddiqui) is a HPC 
Consultant/Software Integration Specialist at 
[Lawrence Berkeley National Laboratory](https://www.lbl.gov/) at 
[NERSC](http://nersc.gov/). He is part of 
[User Engagement Team](https://www.nersc.gov/about/nersc-staff/user-engagement/) 
that is responsible for engaging with NERSC user community through user support 
tickets, user outreach, training, documentation. Shahzeb is part of the 
[Exascale Computing Project (ECP)](https://www.exascaleproject.org/) in 
[Software Deployment](https://www.exascaleproject.org/research-group/software-deployment-at-the-facilities/) (SD) group 
where he is responsible for building Spack [Extreme-Scale Scientific Software Stack](https://e4s-project.github.io/) (E4S) at the DOE facilities. 

Shahzeb Siddiqui started out his career in High Performance Computing (HPC) in 2012 
at [King Abdullah University of Science and Technology](https://www.kaust.edu.sa/en) (KAUST) 
while pursuing his Masters. His focus in HPC includes Parallel Programming, 
Performance Tuning, Containers (Singularity, Docker), Linux system administration,
Scientific Software Installation and testing, Scheduler Optimization, and 
Job Metrics. Shahzeb has held multiple roles in his HPC career in the following 
companies: Dassault-Systemes, Pfizer, Penn State, and IBM. Prior to 2012, he was 
a software engineer holding multiple roles at Global Science & Technology, 
Northrop Grumman, and Penn State.

#### Sameer Shende

Dr. Sameer Shende has helped develop the 
[TAU Performance System](http://www.cs.uoregon.edu/research/tau/home.php), the 
[Program Database Toolkit (PDT)](https://www.cs.uoregon.edu/research/pdt/home.php), 
the [Extreme-scale Scientific Software Stack (E4S)](https://e4s.io) 
and the HPCLinux distro. His research interests include tools and techniques for 
performance instrumentation, measurement, analysis, runtime systems, 
HPC container runtimes, and compiler optimizations. He serves as a 
Research Associate Professor and the Director of the 
[Performance Research Laboratory](https://nic.uoregon.edu/prl/home.php) at the 
[University of Oregon](https://www.uoregon.edu/), 
and as the President and Director of [ParaTools](https://www.paratools.com/),
Inc., ParaTools, SAS, and ParaTools, Ltd. He leads the SDK project for the 
Exascale Computing Project (ECP), in the Programming Models and Runtime (PMR). 
He received his B.Tech. in Electrical Engineering from IIT Bombay, and his M.S.
and Ph.D. in Computer and Information Science from the University of Oregon.


  

