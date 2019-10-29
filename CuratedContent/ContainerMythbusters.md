

# Introducing Container Mythbusters

In the video *Container Mythbusters*, Michael Jennings presents some common
myths about containers and explains the facts that include container
technologies, the difference between containers and Virtual Machines (VM's),
security vulnerabilities and container runtimes for High Performance Computing
(HPC).

#### Contributed by [Patricia  Grubel](https://github.com/pagrubel)

Resource information | Details 
:--- | :--- 
Tutorial title  | Container Mythbusters 
Presenter | Michael Jennings, 2019
Web links | [Video](https://www.youtube.com/watch?v=FFyXdgWXD3A&feature=youtu.be)
Focus | Container Technologies and Vulnerabilities

Containers may seem like a solution for portability when deploying applications
on HPC platforms. However, deploying containers
for scientific software on HPC leads to many questions such as: Will building
our application in a container make it run anywhere?  What are the
vulnerability risks? Will it give me performance portability? Are containers
the solution to reproducibility?  Along with these questions and more come
discussions that can lead to assumptions or "myths" about containers.  Michael
Jennings explains the facts about container technologies for HPC in *Container
Mythbusters*.

Some of the interesting topics in *Container Mythbusters* are:

 - History from early attempts with chroot() to Docker and more
 - What containers are/are not
 - Privileged and unprivileged container runtimes
 - Security vulnerabilities of privileged runtimes
 - Docker is not the only container system
 - Reproducibility challenges for Computational and Data Science
 - Explanation about user namespace for unprivileged container systems.
 
 
This is a very informative talk about container technologies and uses for HPC.
However, it does not provide any information on how to use any particular
container solution.

**Subresources:**
- [Charliecloud](https://hpc.github.io/charliecloud/)
- [Podman](https://podman.io/)
- [Shifter](https://www.nersc.gov/research-and-development/user-defined-images/)
<!---
Publish: 
Categories: Development, Reliability, Performance
Topics: Release and Deployment, Performance Portability, Reproducibility 
Level: 
Prerequisites: defaults
Aggregate: none
Review: LA-UR-19-30997
--->