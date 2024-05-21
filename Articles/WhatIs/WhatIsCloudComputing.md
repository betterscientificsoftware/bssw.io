### What is Cloud Computing?

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: May 20, 2024

<!--deck start-->
Historically, the computational resources needed to support HPC/CSE application requirements have involved a lot of specialized hardware (e.g. platforms, interconnects, networks, file systems and archival storage), skills and facilities infrastructure to commission and support them.
As cloud capabilities have evolved, more and more HPC/CSE applications can now be supported via cloud computing.
<!--deck end-->

<!--body start--->
Cloud computing refers to the delivery of computing services including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet ("the cloud") to offer faster innovation, flexible resources, and economies of scale.
Essentially, it allows the HPC/CSE community to access and use computing resources that are hosted on remote servers, managed by a third party, instead of having to build and maintain computing facilities locally.

Some key components of cloud computing are:

1. **On demand scaling**: Cloud services can scale up or down according to demand.
   This flexibility is crucial for handling varying workloads.

2. **Pay-for-what-you-use pricing**: Users typically pay only for the cloud services they use, helping them manage operating costs more effectively.

3. **Maintenance and Management**: The cloud provider is responsible for hardware and infrastructure software maintenance, updates, and regular improvements.

Cloud computing is categorized into three main types of services: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). Each type offers different levels of control, flexibility, and management, making cloud computing versatile for various applications and business needs.

While cloud computing may not yet be able to handle the most demanding scaling (interconnect size, bandwidth and latency) requirements of HPC/CSE applications, HPC/CSE in the cloud is becoming more and more common.
For example, in 2020, AWS started offering something it calls a [P4d instance](https://aws.amazon.com/ec2/instance-types/p4/) which can be up to 64 nodes with 4 GPUs per node with a cluster-type interconnect and an option of combining multiple P4d instances into something it calls an *UltraCluster*.
<!--body end--->

<!---
Publish: yes
Pinned: yes
Topics: cloud computing
--->
