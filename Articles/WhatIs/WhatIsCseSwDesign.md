# What is CSE Software Design?
<!--deck start--->
CSE Software design for scientific software is an intricate process composed of multiple steps - including determination of what capabilities are needed to meet the targeted scientific goals to understanding how to balance tradeoffs between modularity, functionality and performance in the resulting software product.
<!--deck end--->

<!--body start--->

Scientific software incorporates a broad range of expertise ranging
from domain knowledge and applied mathematics to computer science
issues such as performance and portability. It is necessary to untangle various complexities so that
experts can focus on what they know best. Therefore, the process of software design in the
context of scientific software involves determining a union of
capabilities needed to achieve scientific objectives, the
decomposition of needed capabilities into components that encapsulate a
functionality and an ability to compose these components as needed by
the application. Decomposition can be functional and data/spatial
domain. There are several examples of application codes and frameworks
where sections of the code that pertain to the science of the application
are written and verified separately and then plugged into a composing
framework with a wrapper. The internals of the framework handle the
data management and other infrastructural concerns such as
parallelization if needed.

Therefore, one of the very first choices to make in designing a software
is which abstractions to use, and how to provide footholds for the
abstractions in the framework so that they maintain separation of
concerns. There are many long standing obstacles to meeting requirements above.
There has always been a trade-off between modularity and
performance. Modularity is necessary for maintainable and reusable
code, but it compromises performance. Some of the conflicting
requirements require hard-nosed trade-offs in design. For example, most
composable codes run relatively slowly because they sacrifice performance for
multiphysics and composability. Sometimes this means using suboptimal options for individual
components. The framework should be able to facilitate such unorthodox
approaches and therefore should provide hooks for being able to make
these choices. 
<!--- For more details on framework design see
[Dubey2009,uintah2,valiev2010nwchem,case2014amber,O'Shea2005,Dubey2015] 
--->

Another important consideration in scientific software design is its
dynamic nature. Codes designed for one problem are routinely modified
to use other similar problems, or need modification because growing
understanding places more demands on the current model. Therefore,
extensibility in also a very important aspect of scientific software design.

#### Contributed by [Anshu Dubey](https://github.com/adubey64)

#### Publication date: May 17, 2017
<!--body end--->

<!---
Publish: yes
Pinned: yes
Topics: design
--->
