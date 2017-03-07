# Containers for Research Software

#### Contributed by [Chris Richardson](http://www.bpi.cam.ac.uk/user/chris)

### Introduction

Distributing research software on diverse platforms can become very time consuming. One way to improve productivity, both for developers and end users, is to encapsulate the software environment in a "container".
Unlike traditional Virtual Machines (VMs), containers are more lightweight, and can often be started up almost instantly, for example just to run a single command. The underlying technology requires a Linux kernel
to be running on the host machine, but this is now almost always the case, and can even be provided on Windows machines quite easily.

### Example

The most popular container format at present is [docker](www.docker.com). The docker software is available from their website for Linux, MacOS and Windows.
Many of the popular base environments are available in the docker online registry. For example, one can start up an ubuntu container like this:

```
docker run -ti ubuntu
```
(the `-ti` option means "connect a terminal in interactive mode"). Running this command will give you a root terminal in an
ubuntu distribution, and you can do whatever you like with it. Other distributions are available, e.g. `docker run -ti centos`. It is also possible to specify a revision, e.g. `docker run -ti ubuntu:16.04`.

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
would like to be able to write a script to describe the setup. This is possible using a `Dockerfile`.



<!--- 
Categories: 
Topics: 
Tags: docker, containers, HPC
Level: 
Prerequisites: 
Aggregate: Base: 
Aggregate: 
--->
