# Persistent Identifiers for Software in Scientific Computing
<!-- deck text start -->
Unlock the power of Persistent Identifiers in scientific software to ensure traceability, reproducibility, and collaborative innovation!
<!-- deck text end -->

#### Contributed by [Rinku Gupta](https://github.com/rinkug)
#### Publication date: June 02, 2023

Persistent Identifiers (PIDs) are unique and persistent references for digital objects, such as code, data, publications, or any other research outputs. 
They can be used to reliably locate, access, and cite these objects over long periods of time.
Although PIDs are similar to Uniform Resource Locators (URLs), they can be far superior to URLs for a number of reasons.

Unlike URLs, which often experience link-rot within a few years, PIDs remain consistent and provide a stable means of identification for the long term.
PIDs are resolvable, meaning the associated digital object, including any metadata, will be found even if it has been moved. 
By using PIDs, digital objects become easier to find, track, and reference, ensuring their long-term discoverability, accessibility, and proper attribution.

PIDs are becoming an essential utility in scientific computing.
In this context, they are used to identify software artifacts, such as code, libraries, and frameworks, used in scientific research and computational experiments and play a critical role in ensuring the traceability and reproducibility of computational science results. 
By assigning a PID to a specific version of software, researchers can accurately identify and access the exact code used in their experiments, promoting transparency and enabling others to reproduce and verify their results. 

PIDs also facilitate collaboration in scientific computing. 
They allow researchers to easily attribute, share and cite software, facilitating effective communication and enabling others to build upon existing work. 
In addition, PIDs enable the tracking of software usage and impact within the scientific community, offering insights into the adoption and influence of specific software tools.

PIDs enjoy the above advantages primarily because there usually exists a *service provider* of some kind that has responsibility for generating and assigning PIDs when requested and maintaining their integrity over time.
In some cases, this service is made available for free and in other cases, it may come at a cost.
Your home institution may pay membership fees to make such a service available to all employees.

The Digital Object Identifier (DOI) standard is an example of a PID system used primarily to identify scholarly publications, such as journal articles, conference papers, reports, or book chapters.
Other standards include the Handle System standard, the Archival Resource Key (ARK) standard and the Persistent Uniform Resource Locator (PURL) standard.

There are several ways, outined below, to obtain Persistent Identifiers (PIDs) for scientific software.

| Resource information | Details |
| :--- | :--- |
| Resource | GitHub Integration with Zenodo |
| Website | [https://guides.github.com/activities/citable-code/](https://guides.github.com/activities/citable-code/) |
| Focus | Archiving and Persistent Identifiers for Code |

**GitHub Integration with Zenodo**: GitHub, a widely used platform for hosting and collaborating on code repositories, offers an integration with Zenodo, a popular research data repository and PID service provider.
This integration allows developers to easily obtain PIDs for their software code repositories.
When a developer wants to archive and assign a PID to their GitHub repository, they can initiate the integration with Zenodo. 
Zenodo creates a snapshot of the repository at a specific version and generates a DOI for that snapshot. 
The DOI serves as a persistent identifier for the code, ensuring its long-term accessibility and traceability.
Zenodo also provides archiving of other digital research objects such as datasets, posters, presentations, and publications.

| Resource information | Details |
| :--- | :--- |
| Resource | FigShare |
| Website | [https://figshare.com/](https://figshare.com/) |
| Focus | General-purpose data repository with focus on research data and software code |

**Figshare**: Figshare is a reputable data repository that provides researchers with a platform to share and publish their research outputs, including code. 
While Figshare does not have a direct integration with GitHub like Zenodo, it still offers the capability to assign PIDs to code. 
To obtain a PID for code on Figshare, developers can deposit their code as a zip or tarball file along with any associated documentation or metadata. 
Figshare then assigns a DOI to the deposited package, which can be used to reference and cite the code in publications. 
Figshare also provides features for versioning, licensing, and tracking usage statistics, allowing researchers to manage and share their code effectively.

| Resource information | Details |
| :--- | :--- |
| Resource | Software Heritage |
| Website | [https://www.softwareheritage.org/](https://www.softwareheritage.org/) |
| Focus | Archiving and Persistent Identifiers for Software Code |

**Software Heritage**: Software Heritage is an initiative that aims to preserve all software source code in a publicly accessible archive. 
It provides a PID for each software artifact and offers multiple ways to access and use the archived code. 
The archive is updated daily, and the source code is archived in its original form with its dependencies.

| Resource information | Details |
| :--- | :--- |
| Resource | DOECode |
| Website | https://www.osti.gov/doecode/ |
| Focus | Repository for software developed through DOE-funded projects |

**DOECode**: DOECode is a repository specifically designed for software developed through DOE-funded projects. 
It provides persistent identifiers in the form of DOIs and supports versioning of code. 
DOECode requires a login, but access is free and available to anyone.

In conclusion, Persisent Identifiers help ensure that digital objects of any kind remain available and accessible for the long term.
The methods described here are just a few examples of how to archive snapshots of code and create PIDs.
Each has advantages and limitations.
With any of these methods, researchers can obtain PIDs for their scientific software, enhancing its traceability, reproducibility, collaborative potential, and overall impact within the scientific community.

<!---
Publish: yes
Pinned: no
Topics: software publishing and citation
--->
