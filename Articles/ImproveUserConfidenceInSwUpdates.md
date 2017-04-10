# Improve user confidence in your software updates

#### Contributed by [Mike Heroux](https://github.com/maherou "Mike Heroux GitHub Profile")

#### Publication date: April 10, 2017

When a customer updates to a new version of your software, changes are not just about new features, but often (perhaps mostly) include improvements to existing capabilities.

When a customer is integrating your latest version, they are looking for changes in behavior.  Changes include timing differences and changes in input requirements and output data.  In HPC software, changes in output can be common, especially with floating point computations, where difference in order of operations can produce correct but different results.

In these situations, customers don’t necessarily mind that results have changed, but they want to know that the change is expected, not the result of a regression.

Improve customer confidence in your update by considering the following:
- Create an issue in your database (e.g., a GitHub or JIRA issue) for the feature and give it a label indicating that the feature may change software behavior from the user’s perspective.
- Notify known users of the change prior to release.
- Document any changes that result in different behavior from your software.
- Describe in release notes what kind of behavior change can be expected.
- Provide users with an option to restore previous behavior (e.g., via a runtime or compile time parameter).
- Include performance differences, even if the changes are improvements.

Some sources for behavior change:
- **Performance optimizations for vectorization:** Vectorization represents one of the current commodity performance improvement curves.  As a resource for concurrency, we continue to increase the number of simultaneous operations a process can perform (as either SIMD or SIMT).  Introducing vector operations into your code, directly or through compiler transformations, will result in floating point results differences, including differences from one architecture to the next.
- **Reordering of irregular (gather/scatter) computations for better performance:**  Changes in the order of irregular computations can improve cache utilization and reduce memory bandwidth requirements, leading to better performance.  These changes also lead to floating point result differences.
- **Changes in heuristics for automatic parameter settings:**  Many algorithms are tunable, able to exploit problem details to improve robustness, reliability or performance.  Automatic parameter setting can improve software usability by reducing how many details the user needs to explicitly manage.  Improved heuristics, often derived from customer use, can lead to changes in behavior, even though the change is an improvement.

<!---
Categories: reliability, collaboration
Topics: testing, reproducibility, documentation
Tags: reliability, reproducibility, robustness, HPC, documentation
Level: 2
Prerequisites: Defaults
Aggregate: None
--->
