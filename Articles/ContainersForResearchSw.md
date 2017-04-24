# Containers for Research Software

#### Contributed by [Chris Richardson](https://github.com/chrisrichardson)

### Introduction

Distributing research software on diverse platforms can become very time consuming. One way to improve productivity, both for developers and end users, is to encapsulate the software environment in a "container". Unlike traditional Virtual Machines (VMs), containers are more lightweight, and can often be started up almost instantly, for example just to run a single command. The underlying technology requires a Linux kernel to be running on the host machine, but this is now almost always the case, and can even be provided on Windows machines quite easily.

### Example

The most popular container format at present is [docker](https://www.docker.com). The docker software is available from their website for Linux, MacOS and Windows.
Many of the popular base environments are available in the docker online registry. For example, one can start up an ubuntu container like this:

```
docker run -ti ubuntu
```
(the `-ti` option means "connect a terminal in interactive mode"). Running this command will give you a root terminal in an
ubuntu distribution, and you can do whatever you like with it. Other distributions are available, e.g. `docker run -ti centos`. It is also possible to specify a revision, e.g. `docker run -ti ubuntu:16.04`. **Note**: docker requires a direct internet connection in order to pull the images. It has been observed that VPNs or caching DNS servers can cause problems. Disable any VPN and/or DNS proxy configuration before running docker.

### Managing docker

Docker is a complex package, in itself. There is a lot of online documentation to read through, but here we will review a few basics. It is important to distinguish between "images", which are a snapshot of a filesystem and settings, and "containers" which are the running instances. The following commands are useful to remember:

- `docker run -ti image` - run a container from the named image. The image may be locally cached, but if not, docker will try to find it in an online registry. Note that the container will *not be deleted* when you exit it.
- `docker ps` - lists all running containers.
- `docker ps -a` - lists all containers, including "stopped" ones.
- `docker images` - lists all locally cached images.
- `docker rm` and `docker rmi` - remove containers and images respectively.
- `docker commit` - convert a container to an image, i.e. take a snapshot.

It will take some time experimenting with docker to fully get a feel for how it works. One thing to bear in mind is that each container that is created takes up some disk space, so it is important to run `docker ps -a` and `docker rm` from time to time (another option is to use `docker run --rm` which automatically deletes containers when you exit).

### Installing your stack in a container

Interactive docker can be quite handy to try out different OS environments, but in order to build a software stack, we
would like to be able to write a script to describe the setup. This is possible using a `Dockerfile`. The `Dockerfile` lists all the steps needed to build an image. It start with a `FROM` statement, which defines the base image. Usually, this will be a stock OS. Following from that, you can add "layers" onto it by running any arbitrary set of commands. Here is a simple example, which just creates an image with some python libraries installed:
```
FROM ubuntu:16.10

RUN apt-get update && apt-get install -y python-numpy python-scipy python-matplotlib

```
We can save this file as 'Dockerfile' and run `docker build --tag mypythonimage .` in the same directory (note the "."). Docker will run the commands in the Dockerfile and create an image with the name "mypythonimage". In the `RUN` command, you can put any sequence of commands that you would normally execute, so for example, you could use `wget` to download some external software, and then `cmake` and/or `make install` to install it in the image.
If you have an account at an online registry, it is also possible to `docker push` the image to the registry, so it can be shared with others.

#### Online with github and automatic image building

Once you have a `Dockerfile` describing your software stack, it is only natural to put the Dockerfile under revision control, and push it to a repository, such as [github](https://github.com) or [bitbucket](https://bitbucket.org). With a little bit more work, it is also possible to have it [build automatically every time you make a revision](https://docs.docker.com/docker-hub/builds/) and store the image in an online registry. Dockerhub polls the repository, and rebuilds your image online, every time ([quay.io](https://quay.io) also offers a similar service).

#### Continuous integration testing in docker images

When you have an image in an online registry (such as dockerhub or quay.io), you can point your users at it, and they will
be able to use it to run your application. Another useful application of container technology is in automated testing or continuous integration. If we create an image that contains the ideal development environment for your library or software package, e.g. by including all necessary third party libraries, compilers, etc., then that image can be used for automated testing. For example, on [bitbucket](https://bitbucket.org), we can use the "pipelines" tab to define a set of commands that are run in a docker image, in order to test your package. Every time a change is made to the repository, it launches a container, and runs the commands which are in the `bitbucket-pipelines.yml` file. See bitbucket for more details. At the time of writing, there is not a similar service on github, but that may change.
Of course, it is always possible to do your testing in a container on your own machines, rather than relying on an online service.

### HPC with shifter and singularity

Apart from making a reliable environment for end users, and continuous integration testing, another obvious application for containers is High Performance Computing (HPC). HPC machines tend to have very variable installations, and can be difficult to configure, even for experts. If it would be possible to run inside a container on HPC, that would save a lot of time for everyone.

Because docker runs as root, it is not suitable for HPC installations, but there are some projects which will allow you to run docker format images on HPC. [Shifter](https://github.com/NERSC/shifter) has focused on Cray systems, whilst [singularity](https://singularity.lbl.gov) is more general. Both have seen rapid development during 2015/2016 and will probably be deployed more widely in the near future. MPI performance can be a concern, but it is actually possible to get very good performance provided the MPI in the container adheres to MPICH ABI compatibility (as most HPC MPI implementations do). Because this is a rapidly changing area, it is probably best to refer directly to the project websites.

### Cloud computing with docker

In the case of cloud computing, such as Amazon Web Services, Google Compute Engine or Microsoft Azure, we usually get a VM. It is quite easy to run docker inside the cloud provider's VM, and in many cases, there is a predefined VM with docker preinstalled. Many cloud instances are now quite powerful, so it is possible to run serious codes on a single node.
Nevertheless, if MPI is also needed on a cloud platform, Microsoft Azure now also has RDMA infiniband instances available, and a project called [Batch Shipyard](https://github.com/Azure/batch-shipyard) which allows you to run docker images across multiple nodes with MPI.

<!---
Publish: yes
Categories: planning
Topics: development, deployment
Tags: docker, containers, HPC
Level: 2
Prerequisites: default
Aggregate: none
--->
