# Use of Software Metrics in Research Software

**Hero Image:**

- <img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0421_Metrics.jpg'>

#### Contributed by [Nasir Eisty](https://github.com/neisty)

#### Publication date: April #, 2021

### The importance of software metrics

Software metrics are a critical tool for building reliable software and assessing measurable software quality, especially in complex domains. Software metrics are important for many reasons, including measuring software performance, planning work items, measuring productivity, and more. Within the software development process, software metrics are related to the four functions of management: Planning, Organization, Control, and Improvement. The ultimate goal of software metrics is to provide continuous insight into products and processes. A useful metric typically provides a numerical assessment of the effectiveness of the underlying software or process. 

The complexity and criticality of research software certainly motivates the need for ensuring quality and reliability. Because a software metric is a key tool for assessing, measuring, and understanding software quality and reliability, Dr. Jeffrey Carver of the University of Alabama, Dr. George Thiruvathukal of Loyola University Chicago, and I surveyed the research software developers community to understand their knowledge and use of software metrics. The survey provided respondents an opportunity to share feedback on the impact various types of software metrics have had on their respective projects. While the detailed results we obtained from the survey were published as a research paper, I'm going to describe a few key findings in this article.

### Survey results

In general, the surveyed research software developers reported low knowledge of metrics. Many of them indicated they found metrics rarely or never useful. However, they were able to name many SE-related metrics in free-response questions. While respondents listed items in the free-responses that were not necessarily metrics by the traditional definition, they did mention most of the metrics that appear in classic texts.

We conducted a qualitative analysis of the specific metrics that respondents indicated they knew and used in their projects. In total, the respondents listed 89 unique metrics, indicating they were aware of a large number of metrics. We grouped these 89 unique responses into the following six high-level categories:
* **Code Metrics** – includes those metrics that measure complexity (e.g. McCabe, # of classes, and coupling) and that measure other characteristics of code (e.g. # of clones, and defect density).
* **Process Metrics** – includes metrics that are collected over longer periods of time and provide insight into the software development process (e.g. productivity, cycle time, or # of commits).
* **Testing Metrics** – includes metrics that measure and monitor testing activities by giving insight into test progress, productivity, and quality (e.g. code coverage or # of tests).
* **General Quality Metrics** – includes metrics related to desirable properties of software that are not easy to measure as part of the development process or through analysis of the source code (e.g. interoperability, portability, or sustainability).
* **Performance Metrics** – commonly of interest for software executing on high-performance computing platforms, the metrics address execution time, storage (e.g. RAM or disk space), or scalability (e.g. time vs. CPUs/cores).
* **Recognition Metrics** – includes metrics that measure how a project or its developers quantify outside interest in their work (e.g. citations or downloads). 

It is interesting to note that in addition to the four categories that are commonly found in the software metrics literature (Code, General Quality, Process, and Testing), we identified two categories of metrics (Performance and Recognition) that are not found in the traditional software metrics literature. These new categories are often of interest to research software developers working in high-performance computing environments. Recognition is particularly timely, as research software developers are increasingly interested in being recognized and receiving proper credit for developing research artifacts such as software, tools, and libraries.

### Additional insights

Another interesting result is that research software developers are generally the most knowledgeable in regards to code metrics, but rarely seem to use them. The reported use of code metrics was dreadfully low compared with the ratio between known and used for the other categories listed above. The data in the survey did not provide the type of information necessary to explain why this result may have occurred. Nevertheless, it is both interesting and potentially worrisome. One potential explanation is that while respondents were aware of many different code metrics, they did not believe that these metrics were actually useful in their research software projects. Further research is needed to better understand this discrepancy and identify and necessary solutions that can reduce the gap. Based on the results, we make some additional observations about the rest of the metric categories:
* **Testing metrics** – Respondents used testing metrics second only to performance metrics. This result is encouraging, considering their appearance in the SE literature and TDD.
* **General quality** – While these metrics do not always correspond directly to methods established in SE literature, they are interesting because they shed light on how research software developers view quality in general. We were also encouraged to see interest in sustainability, which is an area of growing importance within the research software community.
* **Performance metrics** – These metrics are clearly of value on the types of systems typically used by research software developers. When the software is written to run on a high-performance computer, for example, lack of performance is a negative characteristic.
* **Process metrics** – Respondents reported high usage of metrics of interest to agile software developers. Given that many of the responses came from small-to-medium sized teams, most of these suggest the use of agile processes.
* **Recognition** – From a traditional SE perspective, this set of metrics would be somewhat unexpected. Respondents reported many metrics as being significant for addressing recognition. The presence of these metrics reinforces the current notion that developers of research software need more and better ways to formally track and quantify their contributions to research.

While this is a short overview of the common usage of different categories of software metrics in research software development, the paper indicated in the “Further reading” section provides the full results from the survey. This study shows that various software metrics could be of value to research software development teams. While work remains to be done to increase knowledge of metrics within this community, I hope that this work can help research software developers see the potential merits of using metrics in their projects.

### Further reading
This article is based on a paper in the proceedings of the 14th IEEE International Conference on e-Science (2018). N.U. Eisty, George K Thiruvathukal, J.C. Carver, "A survey of software metric use in research software development" doi: [10.1109/eScience.2018.00036](https://doi.org/10.1109/eScience.2018.00036)

### Author bio
Nasir Eisty is an assistant professor in the Computer Science and Software Engineering Department of California Polytechnic State University, San Luis, Obispo, CA. He received his Ph.D. degree in Computer Science from the University of Alabama in Spring 2020. His research interests lie in the area of Empirical Software Engineering, Software Quality, and Research Software Engineering. He received a 2020 BSSw (Better Scientific Software) Fellowship award from the Department of Energy (DOE).

<!---
Publish: preview
Pinned: no
Topics: software engineering, software process improvement
RSS update: 2020-12-17
--->
