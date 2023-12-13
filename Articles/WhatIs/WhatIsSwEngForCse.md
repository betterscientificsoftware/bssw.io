# What is Software Engineering for CSE?
#### Contributed by [Anshu Dubey](https://github.com/adubey64) and [Rinku Gupta](https://github.com/rinkug)
#### Publication date: April 20, 2019

<!--deck start--->
Projects with CSE can lie on wide spectrum when it comes to team size and requirements and code complexity. Software engineering practices, thus, need to be wisely adapted based on the project needs since one size will probably not fit all.  
<!--deck end--->

<!--body start--->

Embarking on the intersection of software engineering and computational science and engineering (CSE) demands a solid understanding of the delicate balance between producing functional and reproducible software, the sustainability of the software, coupled with the unique demands posed by diverse project scopes, teams, and complexities. The software development process is not a one-size-fits-all endeavor; rather, it requires a tailored approach that aligns with the project's specific characteristics. It needs a comprehensive software engineering framework that not only navigates the challenges posed by the most demanding projects but also offers adaptability for others to embrace a subset of these practices based on their distinct needs.

In the foundational stages of software engineering for CSE, the importance of best practices resonates from the earliest conceptualization to the final implementation. Beginning with the meticulous gathering of requirements, a critical step involves understanding the specific needs and objectives of the project. Subsequently, the design phase shapes the blueprint for the software, establishing the architecture and functionalities that align with the project's goals. Equally crucial is the thoughtful selection of a proficient team, composed of researchers and research software engineers, ensuring an efficient collaboration of diverse skills and expertise tailored to the project's requirements. With these prerequisites in place, the implementation phase unfolds, guided by the overarching principles of best practices that prioritize functionality, performance, efficiency, maintainability, and scalability. By embedding these best practices into the foundational stages, the software engineering process sets a robust trajectory, laying the groundwork for seamless development, testing, and long-term sustainability.

Any software development should be cognizant of the importance of quality control, encompassing a robust verification and testing regime. As software development unfolds, this becomes pivotal to ensure correctness, reliability, and adaptability in the ever-evolving landscape of computational projects. Ideally, one should adopt software practices that lead to reproducible results. Beyond that, the rigor and extent of software practices adopted should reflect the scope and complexity of the project. A small project with a limited lifecycle has different software engineering needs from those of a large and complex multicomponent software.

An unambiguously defined software process that includes a rigorous verification and testing regime is critical. Verification can be classified into three categories: verification during development, verification of ongoing correctness of the code, and verification before and during a production schedule. All code components should undergo verification tests before they are accepted into the stable code base. The tests should be designed to stress not only the component in question but also its interoperability with other components. In addition to correctness, one must also ensure that there is no regression in either capabilities or performance. A subset of tests built during code development, whether unit tests or tests at higher granularities, can become part of regular automated testing. The selection of tests should ensure good code and interoperability coverage, with an emphasis on being able to isolate error sources quickly.

The software engineering process should also define practices for services such as issue tracking and agile tools project management for the development and maintenance of the software. The policies for code contribution and maintenance should be defined early in the project, with provisions for modification if circumstances warrant. If the software is to be released publicly, another issue is the determination of a suitable license.

For software sustainability, documentation is critical. All interfaces should be fully documented, providing a description of their functionality, input and output parameters, and any changes in the state that they may cause. Inline documentation explaining the control flow and parameter choices, as appropriate, is critical in preventing the loss of capabilities when developers leave. Similarly, documentation and the availability of training modules can be helpful in bringing new team members online rapidly.

<!--body end--->


<!---
Publish: yes
Pinned: yes
Topics: software engineering
--->
