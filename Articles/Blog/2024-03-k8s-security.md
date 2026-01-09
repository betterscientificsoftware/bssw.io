# Security Misconfigurations in Kubernetes Configuration Files

**Hero Image:**

 - <img src='../../images/Blog_2312_SecurityB.png' />

#### Contributed by [Akond Rahman](https://github.com/akondrahman)

#### Publication date: March 26, 2024

In recent years, Kubernetes has become popular to manage scientific workloads. Kubernetes is used to implement the practice of container orchestration, i.e., the practice of pragmatically managing the lifecycle of containers with tools. In this article, I describe some of our [research findings](https://dl.acm.org/doi/10.1145/3579639) related to security misconfigurations that occur in configuration files for Kubernetes. 

Since its inception in 2014, Kubernetes has established itself as the *de facto* tool for automated container orchestration. According to a Stackrox survey, 91% of the 500 practitioners surveyed use Kubernetes for container orchestration. As of September 2020, Kubernetes has a market share of 77% among all container orchestration tools. Organizations such as Adidas, Twitter, IBM, the U.S. Department of Defense (DOD), and Spotify are currently using Kubernetes for automated container orchestration. The use of Kubernetes has resulted in significant benefits, e.g., using Kubernetes the U.S. DOD decreased their release time to 1 week from from 3-8 months.

Kubernetes-based container orchestration, similar to every other configurable software, is susceptible to security misconfigurations. However, due to the pervasive nature of Kubernetes-based container orchestration, such misconfigurations can have severe security implications. According to the 2021 *State of Kubernetes Security Report*, 94% of 500 practitioners experienced at least one Kubernetes-related security incident, the majority of which can be attributed to security misconfigurations. Therefore, there is a need to systematically study the common security misconfigurations with respect to categorization and quantitative measurements.

### Our approach

We investigated the common security misconfigurations by analyzing 2,039 configuration files and derived a catalog of 11 categories of security misconfigurations. We then built a tool to automatically detect security misconfigurations. We also interviewed nine practitioners on the usefulness of our tool and ways to improve it. The datasets used in our paper are publicly available [online](https://figshare.com/s/bced7c8353853a983cd7).

<img src='../../images/k8s-misconfigs.png' />

### Major findings

- In our work, we identified 11 categories of security misconfigurations: nine are Kubernetes-specific, and two are generic.
- Using our research prototype, named [SLI-Kube](https://hub.docker.com/repository/docker/akondrahman/sli-kube/general), we identified 1,051 security misconfigurations in 2,039 configuration files.  
- Security misconfigurations affect Kubernetes entities that perform mesh-related load balancing, as well as provision pods and stateful applications.
- Practitioners found our tool useful but also suggested ways to improve adoption by integrating flexibility, severity-based prioritization, and tighter integration with Kubernetes.

### What do these insights mean for practitioners working in the scientific software space?

- When using Kubernetes for managing scientific workloads, please inspect for security misconfigurations in your Kubernetes configuration files. Consider applying code review practices.
- Many tools exist to automatically detect security misconfigurations and later repair them, such as [Trivy](https://trivy.dev/), [SLI-Kube](https://hub.docker.com/repository/docker/akondrahman/sli-kube/general), and [ValidKube](https://validkube.com/). Please consider using one or more of these tools (each may identify different issues).
- When using a CI/CD pipeline, please add checks for security misconfigurations, and stop the build/deploy process when issues are found.  

### Author bio

Akond Rahman is an assistant professor at Auburn University. His research interest is software engineering focused on development and operations (DevOps) and secure software development. His motivation stems from the foundational challenge of integrating quality assurance into the development process without sacrificing developer productivity and software sustainability. His research is sponsored by the U.S. National Science Foundation (NSF) and the U.S. National Security Agency (NSA). He received his PhD from North Carolina State University. He won the Microsoft Open Source Challenge Award in 2016, the ACM SIGSOFT Doctoral Symposium Award at ICSE in 2018, and the ACM SIGSOFT Distinguished Paper Award at ICSE in 2019. He actively collaborates with practitioners from industry, such as GitHub and WindRiver. To learn more about his work visit https://akondrahman.github.io/.

<!---
Publish: yes
Topics: configuration and builds, development tools
Track: experience
--->
