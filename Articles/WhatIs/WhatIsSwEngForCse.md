# What is Software Engineering for CSE?
#### Contributed by [Anshu Dubey](https://github.com/adubey64)
#### Publication date: April 20, 2019

<!--deck start--->
Projects with CSE can lie on wide spectrum when it comes to team size and requirements and code complexity. Software engineering practices, thus, need to be wisely adapted based on the project needs since one size will probably not fit all.  
<!--deck end--->

<!--body start--->
Any software development should be cognizant of quality control, and ideally should adopt software practices that lead to reproducible results. Beyond that the rigor and extent of software practices adopted should reflect the scope and complexity of the project. A small project with limited lifecycle has different software engineering needs from those of a large and complex multicomponent software. The process we describe addresses most demanding project needs, others can adopt a subset of these practices depending upon their needs.  

An unambiguously defined software process that includes a rigorous verification and testing regime is critical. Verification can be classified into three categories: verification during development, verification of ongoing correctness of the code, and verification before and during a production schedule. All code components should be subjected to verification tests before they are accepted into the stable code base. The tests should be designed to stress not only the component in question, but also its interoperability with other components.  In addition to correctness, one must also ensure that there is no regression in either capabilities or performance. A subset of tests built during code development, whether unit tests or tests at higher grnaularities, can become part of regular automated testing. The selection of tests should ensure good code and interoperability coverage with an emphasis on being able to isolate error sources quickly.

The process should also define practices for services such as issue tracking and agile tools project management for development and maintenance of the software. The policies for code contribution and maintenance should be defined early in the project, with provisions for modification if circumstances warrant. If software is to be released publicly, another issue is determination of a suitable license.

For software sustainability documentation is critical. All interfaces should be fully documented with description of their functionality, input and output parameters, and any changes in the state that they may cause. Inline documentation explaining the control flow and parameter choices as appropriate is critical in preventing loss of capabilities when developers leave. Similarly, documentation and availability of training modules can be helpful in bringing new team members online rapidly.

<!--body end--->


<!---
Publish: yes
Pinned: yes
Topics: software engineering
--->
