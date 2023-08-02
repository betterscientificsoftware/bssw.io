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


### Use a few subheaders to guide the reader at a glance

xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx.

### Use a few subheaders to guide the reader at a glance

xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx xxxx xxxx xxxxx.

### Author bio

Karan Vahi is a Senior Computer Scientist in the Science Automation Technologies group at the USC Information Sciences Institute. He has been working in the field of scientific workflows since 2002, and has been closely involved in the development of the Pegasus Workflow Management System. He is currently the architect/lead developer for Pegasus and in charge of the core development of Pegasus. His work on implementing integrity checking in Pegasus for scientific workflows won the best paper and the Phil Andrews Most Transformative Research Award at PEARC19.


<!---
Publish: No
Categories: reliability
Topics: testing
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
