# Containers for Deploying Workflow Systems and Application Codes

**Hero Image:**

 - <img src='../../images/Blog_081318_SoftVer.png' />
 
The hero image must be this dimension ((1125 x 432 pixels); we can crop an image to the required size.  Put it in the `images/` directory of the bssw.io repo.

#### Contributed by [Karan Vahi](https://github.com/vahi "Karan Vahi GitHub Profile")

#### Publication date: August 20, 2023

Use of containers to deploy workflow systems with a HPC center DMZ, and also use for job execution.

Scientific workflows are a key enabler for complex scientific computations. They capture the interdependencies between processing steps in data analysis and simulation pipelines as well as the mechanisms to execute those steps reliably and efficiently. Workflows can capture complex processes, promote sharing and reuse, and also provide provenance information necessary for the verification of scientific results and scientific reproducibility. Workflows bring the promise of lowering the barrier for using large HPC resources for the end scientist.


### Pegasus
Pegasus (https://pegasus.isi.edu) is used in a number of scientific domains doing production grade science. Pegasus allows users to describe their pipelines in a high level resource agnostic manner, and then execute these on a variety of execution environments ranging from local campus clusters, computational clouds to large national CI such as OSG, ACCESS and DOE supercomputing resources. A key benefit of using Pegasus is it's data management capabilities, whereby it ensures that the data required for the workflow is transferred to the compute nodes automatically, stages out generated output to a location of users choosing, cleanup data that is no longer required, and also ensures scientific integrity of the data during workflow execution. 

### Use of containers in a workflow to manage application dependencies
In the context of scientific workflows, container technologies are especially interesting for two reasons
1. provide an important tool to the end user to enable reproduicibility of their scientific work, by  providing a fully defined and reproducible environment; 
2. decrease the reliance on the system administrators of centrally managed compute clusters to deploy scientific codes and its dependencies. System administrators often have a conflicting goal of providing a stable, slow-moving, multi-user environment and maynot be willing to install libraries or pacakges that a scientists application code requires.

Pegasus provides support for users to easily describe the container that a job in the workflow depends on. Pegasus supports all major container technologies such as Docker, Singularity and Shifter. Once described, Pegasus ensures that the underlying container is deployed automatically at runtime on the node, where a job runs along with it's input data.

New training material in form of jupyter notebooks has been integrated into the main Pegasus Tutorial(https://pegasus.isi.edu/documentation/user-guide/tutorial.html). [Chapter 4](https://github.com/pegasus-isi/pegasus/tree/master/tutorial/docker/notebooks) of the tutorial covers the basics of how to package your code into a Docker container, push it an image repository such as DockerHUB, and then describe how to assocaite the container with specific jobs in the worklfow and run the workflow using Pegasus.

### Use of Containers for Deploying a Workflow Submit Node
 


### Author bio

Karan Vahi is a Senior Computer Scientist in the Science Automation Technologies group at the USC Information Sciences Institute. He has been working in the field of scientific workflows since 2002, and has been closely involved in the development of the Pegasus Workflow Management System. He is currently the architect/lead developer for Pegasus and in charge of the core development of Pegasus. His work on implementing integrity checking in Pegasus for scientific workflows won the best paper and the Phil Andrews Most Transformative Research Award at PEARC19.

### Acknowledgements

This work was supported by the Better Scientific Software Fellowship Program, funded by the Exascale Computing Project (17-SC-20-SC), a collaborative effort of the U.S. Department of Energy (DOE) Office of
Science and the National Nuclear Security Administration; and by the National Science Foundation (NSF) under Grant No. 2154495.


<!---
Publish: No
Categories: reliability
Topics: testing
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
