# Security Misconfigurations in Kubernetes Configuration Files 

**Hero Image:**

 - <img src='../../images/k8s-misconfigs.png' />
 

#### Contributed by [Akond Rahman](https://github.com/akondrahman "Akond Rahman's GitHub Profile")

#### Publication date: January 15, 2024

In this article, I describe some of our [research findings](https://dl.acm.org/doi/10.1145/3579639) related to security misconfigurations that occur in configuration files for Kubernetes. In recent years, Kubernetes has become popular to manage scientific workloads. Kubernetes is used to implement the practice of container orchestration, i.e, the practice of pragmatically managing the lifecycle of containers with tools.   

Since its inception in 2014, Kubernetes has established itself as the `de-facto` tool for automated container orchestration. According to a Stackrox survey, 91% of the surveyed 500 practitioners use Kubernetes for container orchestration. As of Sep 2020, Kubernetes has a market share of 77% amongst all container orchestration tools. Organizations, such as Adidas, Twitter, IBM, U.S. Department of Defense (DOD), and Spotify are currently using Kubernetes for automated container orchestration. Use of Kubernetes has resulted in benefits, e.g., using Kubernetes the U.S. DoD decreased their release time from 3~8 months to 1 week.       

Kubernetes-based container orchestration, similar to every other configurable software, is susceptible to security misconfigurations. However, due to the pervasive nature of Kubernetes-based container orchestration, such misconfigurations can have severe security implications. According to the 2021 `State of Kubernetes Security Report', 94% of 500 practitioners experienced at least one Kubernetes-related security incident, majority of which can be attributed to security misconfigurations. Therefore, there is a need to systematically study the common security misconfigurations with respect to categorization and quantitative measurements. 

### Our Approach 

We investigate the common security misconfigurations by analyzing 2,039 configuration files and derive a catalog of 11 security misconfiguration categories. We then build a tool to automatically detect security misconfigurations. We also interview 9 practitioners on the usefulness of our tool and ways to improve it. Datasets used in our paper are publicly available [online](https://figshare.com/s/bced7c8353853a983cd7).  

### Major Findings 

- We identify 11 categories of security misconfigurations: 9 are Kubernetes-specific, and 2 are generic. 
- Using our research prototype called `SLI-KUBE`, we identify 1,051 security misconfigurations in 2,039 configuration files.  
- Security misconfigurations affect Kubernetes entities that perform mesh-related load balancing, as well as provision pods and stateful applications. 
- Practitioners found our tool useful but also suggested ways for better adoption by integrating flexibility, severity-based prioritization, and seamless integration with Kubernetes. 

### What Does it Mean for Practitioners Working in the Scientific Software Space? 

- If you are using Kubernetes for managing scientific workloads, please inspect for security misconfigurations in your Kubernetes configuration files. Consider applying code review practices. 
- There exists a wide range of tools, such as [Trivy](https://trivy.dev/), [SLI-Kube](https://hub.docker.com/repository/docker/akondrahman/sli-kube/general), and [ValidKube](https://validkube.com/). Please consider using any or multiple of these tools to automatically detect security misconfigurations, and later repair them. 
- When using a CI/CD pipeline, please add checks that will automatically detect instances of security misconfigurations, and stop the build/deploy process if there exists security misconfigurations in configuration files.  

### Author bio

Akond Rahman is an assistant professor at Auburn University. His research interest is in software engineering focused on development and operations (DevOps) and secure software development. His motivation stems from the foundational challenge of integrating quality assurance into the development process without sacrificing developer productivity and software sustainability. His research is sponsored by the U.S. National Science Foundation (NSF) and the U.S. National Security Agency (NSA). He received his PhD from North Carolina State University. He won the Microsoft Open Source Challenge Award in 2016, the ACM SIGSOFT Doctoral Symposium Award at ICSE in 2018, and the ACM SIGSOFT Distinguished Paper Award at ICSE in 2019. He actively collaborates with practitioners from industry, such as practitioners from GitHub and WindRiver. To know more about his work visit https://akondrahman.github.io/.
