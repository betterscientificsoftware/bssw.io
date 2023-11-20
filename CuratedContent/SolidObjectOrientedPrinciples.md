# SOLID Object Oriented Design Principles

<!--deck text start-->
A lot knowledge about how to design robust, extensible and maintainable software can be distilled into just five principles known as the S.O.L.I.D. principles.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe "Roscoe A. Bartlett GitHub Profile")
#### Publication date: ???

Resource information | Details
:--- | :--- 
Article title |  [SOLID Design Principles Wikipedia Page](https://en.wikipedia.org/wiki/SOLID)
Authors | Wikipedia Maintainers (Based on work from Robert C. Martin)
Focus | Software Design

At the foundation of software design and design pattern<sup>[1]</sup> are five software design principles as first articulated by Robert C. Martin and published in several of his books<sup>[2],[3]</sup> and articles.
The names and short descriptions of these five principles (as published in 2003<sup>[3]</sup>) making up the S.O.L.I.D. Principles are:

* **1) SRP** (Single Responsibility Principle): Classes should have only one reason to change.

* **2) OCP** (Open-Closed Principle): Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

* **3) LSP** (Liskov Substitution Principle): Subtypes must be substitutable for their base types.

* **4) ISP** (Interface Segregation Principle): Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.

* **5) DIP** (Dependency Inversion Principle): Abstractions should not depend on details. Details should depend on abstractions.

Beyond Robert Martin's books on the SOLID principles, there are many articles, tutorials, and videos on the SOLID principles developed by many other authors that can be found on the open web (too many to list here).
One of these articles or videos may be of the ideal focus and length for a given interested developer wishing to start learning about these important principles.
However, to really learn these principles, one cannot go wrong with reading about them in one of Robert's books<sup>[2],[3]</sup> in the broader context of software design and architecture.

While these design principles were first articulated in the 1990s in the era of object-oriented "Big Design Up-Front" (BDUF<sup>[4]</sup>) and statically typed programming languages (e.g. C++), they still apply just as much today as they are the foundation for all maintainable and extensible software<sup>[5],[6]</sup>.
It is hard to image a robust, flexible, extensible, and maintainable software package that does not employ one more of these design principles.
For example, every plug-in architecture in existence (regardless of the programming language being used) depends on the principles OCP and LSP at the very least.

Learning the SOLID design principles are a key foundation for any serious software design effort and likely any software developer that does not understand these principles (if not by name) is in for a rough future in the world of software development.

<!---
Publish: yes
Pinned: no
Topics: ???
--->

<!-- References -->

[DesignPatterns-sfer-ezikiw]: https://www.google.com/books/edition/_/iyIvGGp2550C "Design Patterns: Elements of Reusable Object-Oriented Software. {Gamma, Erich, Richard Helm, Ralph Johnson, and John Vlissides. Addison-Wesley. 1995}"

[CleanArchitecture-sfer-ezikiw]:  https://books.google.com/books?id=uGE1DwAAQBAJ "Clean Architecture: A Craftsman's Guide to Software Structure and Design. {Martin, Robert C., Prentice Hall. 2017, ISBN 9780134494166.}"

[AgileSoftwareDevelopment-sfer-ezikiw]: https://books.google.com/books?id=0HYhAQAAIAAJ "Agile Software Development: Principles, Patterns, and Practices. {Martin, Robert C., Pearson Education. 2003, ISBN 978-0135974445}"

[BDUF-sfer-ezikiw]: https://en.wikipedia.org/wiki/Big_design_up_front "Big Design Up Front. {Wikipedia}"

[SolidRelevance-sfer-ezikiw]: https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html "Solid Relevance. {Martin, Robert C., The Clean Code Blog. October 18, 2020}"

[SolidFoundationModernSoftware-sfer-ezikiw]: https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/ "Why SOLID principles are still the foundation for modern software architecture. {Orner, Daniel. StackOverflow Blog. November 1, 2021}"
<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "Design Patterns: Elements of Reusable Object-Oriented Software."
[2]: #sfer-ezikiw-2 "Clean Architecture: A Craftsman's Guide to Software Structure and Design."
[3]: #sfer-ezikiw-3 "Agile Software Development: Principles, Patterns, and Practices."
[4]: #sfer-ezikiw-4 "Big Design Up Front."
[5]: #sfer-ezikiw-5 "Solid Relevance."
[6]: #sfer-ezikiw-6 "Why SOLID principles are still the foundation for modern software architecture."
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[Design Patterns: Elements of Reusable Object-Oriented Software.<br>Gamma, Erich, Richard Helm, Ralph Johnson, and John Vlissides. Addison-Wesley. 1995](https://www.google.com/books/edition/_/iyIvGGp2550C)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[Clean Architecture: A Craftsman's Guide to Software Structure and Design.<br>Martin, Robert C., Prentice Hall. 2017, ISBN 9780134494166.](https://books.google.com/books?id=uGE1DwAAQBAJ)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[Agile Software Development: Principles, Patterns, and Practices.<br>Martin, Robert C., Pearson Education. 2003, ISBN 978-0135974445](https://books.google.com/books?id=0HYhAQAAIAAJ)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[Big Design Up Front.<br>Wikipedia](https://en.wikipedia.org/wiki/Big_design_up_front)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[Solid Relevance.<br>Martin, Robert C., The Clean Code Blog. October 18, 2020](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[Why SOLID principles are still the foundation for modern software architecture.<br>Orner, Daniel. StackOverflow Blog. November 1, 2021](https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/)
