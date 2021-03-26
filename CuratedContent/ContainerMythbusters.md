# Introducing Container Mythbusters

<!--deck text start-->
In the video *Container Mythbusters*, Michael Jennings presents some common
myths about containers and explains the facts, including container
technologies, the difference between containers and Virtual Machines (VM's),
security vulnerabilities, and container runtimes for high-performance computing
(HPC).
<!--deck text end-->

#### Contributed by [Patricia  Grubel](https://github.com/pagrubel)
#### Publication date: November 26, 2019

Resource information | Details 
:--- | :--- 
Tutorial title  | Container Mythbusters 
Presenter | [Michael Jennings](https://github.com/mej)
Web links | [Video](https://www.youtube.com/watch?v=FFyXdgWXD3A&feature=youtu.be)

Containers may seem like a solution for portability when deploying applications
on HPC platforms. However, deploying containers
for scientific software on HPC leads to many questions, such as: Will building
our application in a container enable it to run on particular HPC platforms?  What are the
vulnerability risks? Will this approach provide performance portability? Are containers
a solution to reproducibility?  Along with these questions and more, come
discussions that can lead to assumptions or "myths" about containers.  Michael
Jennings explains the facts about container technologies for HPC in *Container
Mythbusters*.

Some of the interesting topics in *Container Mythbusters* are:

 - History from early attempts with chroot() to Docker and more
 - What containers are (and are not)
 - Privileged and unprivileged container runtimes
 - Security vulnerabilities of privileged runtimes
 - Docker is not the only container system
 - Reproducibility challenges for computational and data science
 - Explanation about user namespace for unprivileged container systems
 
 
This is a very informative talk about container technologies and uses for HPC.
However, it does not provide any information on how to use any particular
container solution.

### Links to additional information
- [Charliecloud](https://hpc.github.io/charliecloud/)
- [Docker](https://www.docker.com/)
- [Podman](https://podman.io/)
- [Shifter](https://www.nersc.gov/research-and-development/user-defined-images/)


<!---
Publish: yes
Topics: Release and Deployment, Performance Portability, Reproducibility 
Pinned: no
RSS update: 2019-11-26
--->
