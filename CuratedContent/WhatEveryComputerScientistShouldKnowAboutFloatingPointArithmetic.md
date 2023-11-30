# What Every Computer Scientist Should Know About Floating-Point Arithmetic

<!--deck text start-->
Floating point computations are the foundation for computational science and engineering software.
As such, understanding the foundations of floating point data-types and operations is critical in the development of robust portable numerical software.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)
#### Publication date: January 24, 2022

Resource information | Details 
:--- | :--- 
Paper title | [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://doi.org/10.1145/103162.103163)
Authors | David Goldberg
Publication | Year 1991, Journal of Information and Software Technology, DOI: [https://doi.org/10.1145/103162.103163](https://doi.org/10.1145/103162.103163)

Resource information | Details 
:--- | :--- 
Web Page | [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)
Authors | David Goldberg

NOTE: The original [journal article](https://doi.org/10.1145/103162.103163) has been republished as a [hyperlinked HTML page](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html).

Doing sufficiently accurate computations of infinite precision real numbers using finite precision computer approximations requires a solid understanding of floating-point formats, computational issues, and standards.
When implementing numerical algorithms involving real-world data solving ill-conditioned mathematical problems, a single sloppy floating-point expression can break an implemented algorithm and make it impossible to compute a solution to the needed precision (or any solution at all).

The paper *"What Every Computer Scientist Should Know About Floating-Point Arithmetic"* provides a critical foundation for understanding modern floating-point data-types and computations approximating algorithms involving real numbers.
The issues involved must be well understood by computer hardware developers, system software developers, and numerical software developers alike in order for it to be possible to implement robust numerical algorithms in a portable way.

This paper covers the basics of floating-point, including:

* floating-point formats,
* rounding error (e.g., guard digits) and measures of error (e.g., machine epsilon &epsilon;, absolute error),
* loss of basic associativity and loss of other basic properties of real arithmetic, and
* catastrophic cancellation.

In addition, the author covers IEEE floating-point standards, including the IEEE 754 binary standard which addresses:

* bit-wise floating-point number data-structures (i.e., significant digits, exponents, sign),
* rounding and accuracy requirements for basic floating-point operations,
* overflow, underflow and special quantities (i.e., (signed) zero, denormalized numbers, NaNs, (signed) infinity &infin;),
* floating-point exceptions, flags, and trap handlers,
* rounding modes, and
* conversions with integers and decimal (i.e., human-readable text-based) formats.

Great attention is given to the issue of catastrophic cancellation (the subtraction of two nearby numbers where the operands are also subject to rounding errors) and related floating-point issues.
Several examples are given of how different numerical expressions can be reformulated to eliminate a catastrophic cancellation and/or avoid underflow/overflow and thereby increase the robustness and accuracy of the floating-point calculation to a wide range of input data.
(Reformulating an expression to reduce floating-point errors and exceptions can often increase the complexity of the code and increase the operation count and computational cost, so there are often trade-offs of numerical accuracy, robustness, code maintainability, and runtime speed that must be made when implementing a numerical algorithm using floating-point computations.)

System and compiler issues are also discussed where violations of basic floating-point foundations can make it very difficult to implement a robust numerical algorithm. For example, the author unequivocally states:

> A language definition that does not require parentheses to be honored is useless for floating-point calculations.

Several compilers and systems over the years have been known to violate this and other necessary basic foundations of floating-point and the IEEE 754 standard, especially when compiler optimizations are turned up.
In addition, full implementation of the IEEE 754 standard on a system is rare and controlling behavior such as floating-point exceptions, rounding modes, and trap handlers is difficult or impossible in a portable way with many programming languages and libraries.
This is especially true on some of the more bleeding-edge high-performance computing (HPC) accelerators and systems.
As a result, numerical algorithm developers often have to rely on a smaller subset of the IEEE standard in order to develop a maximally portable robust implementation.

Finally, the paper contains quite a few proofs of floating-point arithmetic, and these proofs serve several purposes.
First, the proofs establish the foundation of floating-point operations, which demonstrate that floating-point is not black magic but is a well-established mathematical approximation/discretization of real number arithmetic.
Second, the proofs show that one can rigorously analyze the expressions in a floating-point algorithm and use that to spot areas of concern.
Finally, these proofs show how important it is to have a standard like IEEE 754 in designing and implementing numerical algorithms by being able to rely on a few key numerical properties.

In summary, the paper *"What Every Computer Scientist Should Know About Floating-Point Arithmetic"* represents a must-read for any serious numerical algorithm developer. In addition to learning the basics of floating-point, it is important that numerical algorithm developers have a strong knowledge of the IEEE 754 standard and be aware of what properties are supported or not supported on the set of compilers and systems that their algorithm implementations must run.
It is especially important to numerical developers exposed to bleeding-edge HPC systems.
When these early systems violate basic IEEE standards, it is useful for these numerical algorithm developers to provide feedback to the vendors to see if floating-point standards compliance can be restored.

<!---
Publish: yes 
Pinned: no
RSS update: 2022-01-24
Topics: Programming languages, High-performance computing (HPC), Reproducibility, Refactoring
--->

<!---
LocalWords:  associativity denormalized discretization
--->
