# Exploring Containers for Research Software

#### Contributed by [Chris Richardson](https://github.com/chrisrichardson)

#### Publication Date: March 7, 2017

<!-- deck text start -->
Containers have gained popularity in software development and testing environments in the scientific community. Lets talk about containers and explore the docker container platform and its usage.
<!-- deck text end -->

## Introduction

Distributing research software on diverse platforms can become time-consuming. One way to improve productivity, for both developers and end users, is to encapsulate the software environment in a "container." Unlike traditional virtual machines, containers are more lightweight and can often be started up almost instantly, for example just to run a single command. The underlying technology requires a Linux kernel to be running on the host machine, but this is now almost always the case and can even be provided on Windows machines easily.

## Example

The most popular container format at present is [docker](https://www.docker.com). The docker software is available from their website for Linux, MacOS, and Windows.
Many of the popular base environments are available in the docker online registry. For example, one can start up an ubuntu container such as the following.

```
docker run -ti ubuntu
```
(the `-ti` option means "connect a terminal in interactive mode"). Running this command will give you a root terminal in an
ubuntu distribution, and you can do whatever you like with it. Other distributions are available, for example, `docker run -ti centos`. You also can specify a revision, for example, `docker run -ti ubuntu:16.04`. *Note*: docker requires a direct internet connection in order to pull the images. Since VPNs or caching DNS servers can cause problems, you should disable any VPN and/or DNS proxy configuration before running docker.

## Managing docker

Docker is a complex package, with  a lot of online documentation to read through. Here we will review a few basics. It is important to distinguish between "images," which are snapshots of a filesystem and settings, and "containers," which are the running instances. The following commands are useful to remember.

- `docker run -ti image` - run a container from the named image. The image may be locally cached; but if it is not, docker will try to find it in an online registry. Note that the container will *not be deleted* when you exit it.
- `docker ps` - list all running containers.
- `docker ps -a` - list all containers, including "stopped" ones.
- `docker images` - list all locally cached images.
- `docker rm` and `docker rmi` - remove containers and images respectively.
- `docker commit` - convert a container to an image (i.e., take a snapshot).

You will need some time experimenting with docker to fully get a feel for how it works. Bear in mind that each container you create takes up some disk space, so you should run `docker ps -a` and `docker rm` from time to time. Another option is to use
`docker run --rm`, which automatically deletes containers when you exit.

## Installing your stack in a container

Interactive docker can be handy for trying out different OS environments; but to build a software stack, we
would like to be able to write a script to describe the setup. You can do so by using a `Dockerfile`. This lists all the steps needed to build an image. It starts with a `FROM` statement, which defines the base image. Usually, this will be a stock OS. Following from that, you can add "layers" onto it by running any arbitrary set of commands. Here is a simple example, which just creates an image with some python libraries installed.
```
FROM ubuntu:16.10

RUN apt-get update && apt-get install -y python-numpy python-scipy python-matplotlib

```
We can save this file as 'Dockerfile' and run `docker build --tag mypythonimage .` in the same directory (note the period). Docker will run the commands in the `Dockerfile' and create an image with the name "mypythonimage." In the `RUN` command, you can put any sequence of commands that you would normally execute; for example, you could use `wget` to download some external software and then `cmake` and/or `make install` to install it in the image.

If you have an account at an online registry, you can also `docker push` the image to the registry, so it can be shared with others.

### Online with github and automatic image building

Once you have a `Dockerfile` describing your software stack, you'll want to put the Dockerfile under revision control and push it to a repository, such as [github](https://github.com) or [bitbucket](https://bitbucket.org). With a little bit more work, you can also have it [build automatically every time you make a revision](https://docs.docker.com/docker-hub/builds/) and store the image in an online registry. Dockerhub polls the repository and rebuilds your image online, every time ([quay.io](https://quay.io) offers a similar service).

### Continuous integration testing in docker images

When you have an image in an online registry (such as dockerhub or quay.io), you can point your users to it, and they will
be able to use it to run your application. Another useful application of container technology is in automated testing or continuous integration. If we create an image that contains the ideal development environment for your library or software package, for example, by including all necessary compilers and third-party libraries, then that image can be used for automated testing. For example, on [bitbucket](https://bitbucket.org), we can use the "pipelines" tab to define a set of commands that are run in a docker image, in order to test your package. Every time a change is made to the repository, it launches a container and runs the commands that are in the `bitbucket-pipelines.yml` file. See bitbucket for more details. At the time of writing, there is not a similar service on github, but that may change.

Of course, you can always  do your testing in a container on your own machines, rather than relying on an online service.

## HPC with shifter and singularity

Apart from making a reliable environment for end users and enabling continuous integration testing, another obvious application for containers is high-performance computing. HPC machines tend to have variable installations and can be difficult to configure, even for experts. Running inside a container on HPC machines would save everyone a lot of time.

Because docker runs as root, it is not suitable for HPC installations; but some projects will allow you to run docker format images on HPC systems. [Shifter](https://github.com/NERSC/shifter) has focused on Cray systems, and [singularity](https://singularity.lbl.gov) is more general. Both have seen rapid development during 2015-2016 and will probably be deployed more widely in the near future. MPI performance can be a concern, but you can get good performance provided that the MPI in the container adheres to MPICH ABI compatibility (as most HPC MPI implementations do). Because this is a rapidly changing area, you should probably refer directly to the project websites.

## Cloud computing with docker

In the case of cloud computing, such as Amazon Web Services, Google Compute Engine, or Microsoft Azure, we usually get a virtual machine (VM). Running docker inside the cloud provider's VM is easy; and in many cases there is a predefined VM with docker preinstalled. Many cloud instances are now powerful, so you can run serious codes on a single node.

Nevertheless, if MPI is also needed on a cloud platform, Microsoft Azure now also has RDMA InfiniBand instances available and a project called [Batch Shipyard](https://github.com/Azure/batch-shipyard) that allows you to run docker images across multiple nodes with MPI.

In conclusion, leveraging container technology, exemplified by Docker, streamlines the distribution and management of research software across diverse platforms, offering lightweight and efficient encapsulation of software environments. From enabling rapid experimentation to facilitating continuous integration testing and addressing specific needs in areas like high-performance computing and cloud platforms, containers prove to be a versatile solution enhancing productivity for developers and end users alike.

<!---
Publish: yes
Topics: release and deployment, cloud computing
Track: Experience
Pinned: no
--->
