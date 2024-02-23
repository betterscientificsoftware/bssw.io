# What is CSE Software Design?
#### Contributed by [Anshu Dubey](https://github.com/adubey64) and [Rinku Gupta](https://github.com/rinkug)

#### Publication date: May 17, 2017
<!--deck start--->
CSE Software design for scientific software is an intricate process composed of multiple steps - including the determination of what capabilities are needed to meet the targeted scientific goals to understanding how to balance tradeoffs between modularity, functionality, and performance in the resulting software product.
<!--deck end--->

<!--body start--->

Creating scientific software incorporates a broad range of expertise, spanning from domain knowledge to applied mathematics and computer science issues such as performance, scalability, portability, and quality. Untangling these issues and complexities is crucial to enable teams and experts to concentrate on their core strengths.

Before embarking on the design phase of scientific software, a critical prerequisite is a profound understanding of the underlying scientific problem. This entails a thorough comprehension of the objectives to be achieved and the explicit definition and understanding of requirements. The multifaceted nature of software design encompasses several key aspects, including defining the overall system architecture and charting out the high-level structure and interactions between components. Additionally, careful consideration is given to selecting appropriate algorithms, with a keen focus on factors like accuracy, efficiency, and scalability. The implementation of best practices for documentation is crucial, providing comprehensive insights into the software's architecture, algorithms, and usage. Collaborative tools play a pivotal role, enhancing communication and coordination among team members. Successful software design, therefore, necessitates a holistic approach that encompasses not only technical considerations but also a deep appreciation for the scientific problem at hand and effective collaboration practices.

In the context of scientific computing, one key aspect in the process of software design involves determining (1) a union of capabilities needed to achieve desired scientific objectives, (2) the decomposition of needed capabilities into smaller components that encapsulate functionality, and (3) an ability to design these components as needed by the application.

Decomposition occurs in both functional and data/spatial domains. In various application codes and frameworks, sections dedicated to the scientific aspects are independently written, verified, and then integrated into a composing framework using a wrapper. The internals of the framework handle data management and other infrastructural concerns such as parallelization if needed.

Therefore, one of the initial decisions in software design is choosing abstractions and establishing footholds in the framework to maintain the separation of concerns. Meeting these requirements faces long-standing obstacles, particularly the trade-off between modularity and performance. Although modularity is essential for code that is maintainable and reusable, it frequently comes at the expense of performance. Resolving conflicting requirements necessitates hard-nosed trade-offs in design. For instance, the majority of composable modularized codes tend to operate at a slower pace as they prioritize increased flexibility in designing independent components and their composability over optimal performance. At times, this involves employing less-than-optimal options for individual components. The framework should support these unconventional approaches by providing hooks to make such choices.

Another crucial aspect of scientific software design is its dynamic nature. Codes initially designed for one problem are frequently adapted for similar issues or require modifications as evolving understanding places additional demands on the current model. Thus, extensibility becomes a vital element in scientific software design.

When it comes to scientific software design, as seen above, multiple considerations come into play, requiring careful thought about the mentioned issues. It is crucial to assess whether the teams involved in the design process understand and possess experience in recognizing these issues, enabling them to proactively design effective solutions.

<!--body end--->

<!---
Publish: yes
Pinned: yes
Topics: design
--->
