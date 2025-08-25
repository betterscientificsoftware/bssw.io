# Don't Package Your Libraries, Write Packageable Libraries

<!--deck text start-->
Do you want to ensure your libraries are easily packaged into any system—even ones you've never heard of and may never hear of?
This two-part series presents valuable information and guidance on how to write **packageable** libraries.

<!--deck text end-->

#### Contributed by [Patricia Grubel](https://github.com/pagrubel "Patricia Grubel")

#### Publication date: August 7, 2025

Resource information | Details
:--- | :---
Title | Don't Package Your Libraries, Write Packageable Libraries! (Parts I & II)
Presenter | Robert Schumacher
Web Links, Part I | [Video](https://www.youtube.com/watch?v=sBP17HQAQjk), [Slides](https://github.com/CppCon/CppCon2018/blob/master/Presentations/dont_package_your_libraries_write_packagable_libraries/dont_package_your_libraries_write_packagable_libraries__robert_schumacher__cppcon_2018.pdf)
Web Links, Part II | [Video](https://www.youtube.com/watch?v=_5weX5mx8hc)

*"Don't Package Your Libraries, Write Packageable Libraries!"*, an informative two-part series presented by Robert Schumacher at CppCon, delivers practical guidelines for designing and writing libraries with a strong emphasis on the needs of the maintainers who will integrate them into systems.

Schumacher explains the **four key facets** of the packaging ecosystem:

1. **Library Authors** – who write libraries and want others to adopt them.  
2. **System Users** – who depend on systems that rely on these libraries.  
3. **Other Libraries** – that might build on or include your library.  
4. **Maintainers** – who package your library for use in their systems, often without deep knowledge of your code or its domain.

Schumacher's guidance helps library authors anticipate the needs of each facet and design accordingly.
While the talks are C++-focused, the concepts are broadly applicable and relevant to library authors working in other programming languages.
Through real-world examples, Schumacher illustrates both successful applications of the guidelines and pitfalls of neglecting them.
Though originally presented in 2018 and 2019, the principles in this series remain relevant for today's software development challenges.

Following the guidelines presented in this series will help you design libraries that are easily and reliably packaged into the systems you intended—and those you've never even heard of.

<!---
Publish: yes
Topics: Configuration and Builds, Release and Deployment, Software Interoperability, Software Sustainability
Pinned: no
RSS update: 2025-08-07
--->