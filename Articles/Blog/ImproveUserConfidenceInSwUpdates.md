# Improve User Confidence in Your Software Updates

**Hero Image:**
- <img src="https://s-media-cache-ak0.pinimg.com/736x/e2/59/71/e2597197db792223d23e75146f5c8678--sleeping-puppies-the-office.jpg">[Puppy at work]

#### Contributed by [Mike Heroux](https://github.com/maherou "Mike Heroux GitHub Profile")

#### Publication date: July 14, 2017

Informing users about what has changed is key to instilling confidence.

When customers update to a new version of your software, the changes they will encounter are not just about new features: often (perhaps mostly) such changes include improvements to existing capabilities.

Customers who are integrating your latest version are looking for changes in behavior.  Such changes include timing differences and changes in input requirements and output data.  In HPC software, changes in output can be common, especially with floating-point computations where difference in the order of operations can produce correct but different results.

In these situations, customers don’t necessarily mind that results have changed, but they want to know that the change is expected, not the result of a regression.

You can improve customer confidence in your updates by considering the following:
- Create an issue in your database (e.g., a GitHub or JIRA issue) for the feature, and give it a label indicating that the feature may change software behavior from the user’s perspective.
- Notify known users of the change prior to release.
- Document any changes that result in different behavior from your software.
- Describe in release notes what kind of behavior change can be expected.
- Provide users with an option to restore previous behavior (e.g., via a runtime or compile time parameter).
- Include performance differences, even if the changes are improvements.

Sources for behavior change may include the following:
- **Performance optimizations for vectorization:** Vectorization represents one of the current commodity performance improvement curves.  As a resource for concurrency, we continue to increase the number of simultaneous operations a process can perform (as either SIMD or SIMT).  Introducing vector operations into your code, directly or through compiler transformations, will lead to differences in floating-point results, including differences from one architecture to the next.
- **Reordering of irregular (gather/scatter) computations for better performance:**  Changes in the order of irregular computations can improve cache utilization and reduce memory bandwidth requirements, leading to better performance.  These changes also lead to differences in floating-point results.
- **Changes in heuristics for automatic parameter settings:**  Many algorithms are tunable, able to exploit problem details to improve robustness, reliability, or performance.  Automatic parameter setting can improve software usability by reducing how many details the user needs to explicitly manage.  Improved heuristics, often derived from customer use, can lead to changes in behavior, even though the change is an improvement.

<!---
Publish: Yes
Track: deep dive
Topics: testing, reproducibility, documentation
Pinned: no
--->
