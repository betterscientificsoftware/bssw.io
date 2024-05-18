### What are Programming Languages in Scientific Computing?

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: June, 2024

<!--deck start-->
Scientific programming languages are designed to facilitate the development of software that performs scientific computations.
These languages are typically used by researchers and scientists to solve complex mathematical problems, simulate scientific experiments, and process large datasets.
<!--deck end-->

<!--body start--->
Introduced in the late 1950s, Fortran is largely regarded as the first scientific computing language.
Indeed, the name is an acronym for "FORMula" "TRANslation" reflecting its purpose in translating mathematical formulas into instructions for a machine to follow.

Since the 1950s, a large variety of programming languages have been introduced but not all are good choices for scientific computing.
A Programming language suitable for scientific computing typically includes the following basic features:

1. **Numerical Accuracy and Precision**: The language supports both integer and [floating-point](https://www.volkerschatz.com/science/float.html) numbers with high accuracy and precision.
   This may include support for various *levels* of precision (e.g. single, double, quad) including mixed and arbitrary precision.
   It may also include native, built-in support for complex numbers, quaternions, and/or interval arithmetic.
   In addition, the language may directly support various arithmetic operations such as exponentiation, logarithm and square-root.

2. **Efficient Computation**: The language is optimized for performing large numbers of arithmetic operations on large amounts of data often by leveraging hardware acceleration such as GPUs (or vector co-processors of the past), instruction pipelining, multi-level memory caches and parallel processing.

3. **Numerical Libraries**: The language often comes *standard* with many libraries that support commonly needed mathematical operations and functions such as vector and matrix operations, root finding, random number generation, trigonometric functions, numerical methods, statistical analysis, machine learning and other operations relevant to scientific computing.

More recently, [memory safety](https://bssw.io/items/us-federal-government-effort-to-champion-adoption-of-memory-safe-languages) in scientific computing languages has become an important topic.

Some popular scientific programming languages include [Python](https://www.python.org), [R](https://www.r-project.org), [Fortran](https://j3-fortran.org), [C](https://www.open-std.org/JTC1/SC22/WG14/)/[C++](https://www.open-std.org/JTC1/SC22/WG21/)/[C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)), [Julia](https://julialang.org) and [MATLAB](https://www.mathworks.com/products/matlab.html).
These languages help streamline the process of scientific research and analysis by providing the necessary tools to handle the specific demands of scientific computing.
Read more about [resources for scientific computing](https://bssw.io/items/fundamental-resources-for-scientific-computing).
<!--body end--->

<!---
Publish: yes
Pinned: yes
Topics: programming languages
--->
