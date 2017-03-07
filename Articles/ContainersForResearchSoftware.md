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



<!--- 
Categories: 
Topics: 
Tags: docker, containers, HPC
Level: 
Prerequisites: 
Aggregate: Base: 
Aggregate: 
--->
