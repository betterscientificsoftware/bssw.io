# Testing Non-Deterministic Research Software

#### Contributed by [Nasir Eisty](https://github.com/neisty "Nasir Eisty GitHub Profile")

#### Publication date: October 13, 2020

Testing scientific software is challenging, evident in the large number of [guides, tutorials and best practices](https://bssw.io/items?topic=testing) on how to create tests to avoid software defects and verify correctness.  BUT, how do you test when you can't even define *the* right answer?!  

During summer 2019, I had the opportunity to gain first-hand experience developing testing framework for a non-deterministic research software project.  Receiving recognition as a [2019 BSSw Fellowship](https://bssw.io/pages/bssw-fellowship-program) honorable mention for my work in software testing, I was invited to work as a graduate research assistant at Los Alamos National Laboratory with the [Exascale Atomistic capability for Accuracy, Length and Time (EXAALT)](https://gitlab.com/exaalt/exaalt) team, an [ECP](https://www.exascaleproject.org/research-group/chemistry-and-materials/)-funded materials modeling framework designed to leverage extreme-scale parallelism to produce accelerated molecular dynamics simulations.

My work on ParSplice described below, part of the EXAALT project, is part of my journey to create robust and automated testing in research software, and continues previous collaborations between [IDEAS-ECP](https://ideas-productivity.org/ideas-ecp/) and EXAALT which was the subject of an earlier BSSw.io blog article: **[Adopting Continuous Integration for Long-Timescale Materials Simulation](https://bssw.io/blog_posts/adopting-continuous-integration-for-long-timescale-materials-simulation)**

[How do we test non-deterministic research software that might not return the same result on different runs with the same input?]<img src='../../images/Blog_0820_Testing.png' />

### Non-determinism is becoming more common in research software

Research software often has complex, computational behavior, with many execution paths and requiring many inputs. This complexity makes it difficult for developers to manually identify critical input domain boundaries and partition the input space to identify a small but sufficient set of test cases. In addition, some research software can produce complex outputs whose assessment might rely on the experience of domain experts rather than on an objective test oracle.

A growing challenge in testing research software, especially software targeted to run in parallel on high-performance computing systems, is non-determinism.  In a non-deterministic system, the output can not be predicted because there are multiple possible outcomes for each input and there is no practical way for the tester (or test oracle) to predetermine the system's exact behavior. 

Non-determinism can be actual, which occurs when there is no theoretical way of predetermining the system's exact behavior, such as behavior that is determined by quantum physics (e.g., using nuclear decay to generate truly random numbers), or apparent non-determinism due to overwhelming complexity or to inadequate controllability, visibility, and oracle(s).

In terms of testability, both actual and apparent non-determinism have the same impact from a practical point of view. With non-deterministic systems and software, you can run the exact same test case multiple times and get different results. Running a single test case only once is insufficient to determine whether the test case truly passes or fails. Testers must take into account four types of non-deterministic behavior based on the source of that behavior: 
* physical non-determinism which occurs due to the nature of physical reality, 
* emergent non-determinism which occurs due to integration of subsystems into systems, 
* concurrent non-determinism which occurs due to system-internal and -external concurrency, and 
* exceptional non-determinism which occurs due to fault and failure behavior.

### ParSplice: accelerated molecular dynamics

[ParSplice](https://gitlab.com/exaalt/parsplice) (Parallel Trajectory Splicing) aims at overcoming the challenge of simulating the evolution of materials over long time scales through the timewise parallelization of long atomistic trajectories using multiple independent producers. The ParSplice code is a management layer that orchestrates a large number of calculations and does not perform the actual molecular dynamics itself. Instead, ParSplice uses external molecular dynamics engines (i.e. LAMMPS and LATTE). The simulations used in ParSplice rely on stochastic equations of motion to mimic the interaction of the system of interest with the wider environment, which introduces a first source of non-determinism. The lack of availability of the ground truth model (which is an extremely complex function of the underlying physical model) makes assessment of the results difficult. In addition, this type of stochastic simulation is not reproducible, adding to the difficulty of testing the code. 

In cases where development of test oracles is difficult due to the non-determinism, some potentially viable testing approaches include 
* metamorphic testing, 
* run-time assertions, and 
* machine learning techniques. 

However, for the ParSplice project, it was not feasible to apply these techniques, for reasons described in detail in the case study paper referenced below. After trying several techniques, I was finally able to implement a testing mechanism for the ParSplice project using the  Multinomial test. 

### The Multinomial test

The Multinomial test is a statistical test of the null hypothesis that the parameters of a multinomial distribution are given by specified values. The Multinomial test uses Pearson’s χ² test to test the null hypothesis that the observed counts are consistent with the given probabilities. The null hypothesis is rejected if the p-value of the following χ² test statistics is less than a given significance level. This approach enabled me to test whether the observed frequency of segments starting in i and ending in j is indeed consistent with the probabilities Pij given as input to the Monte Carlo backend.

The null hypothesis was that the observed counts generated by ParSplice are consistent with the probabilities in the model. If the p-value from the multinomial test is less than 0.05, we reject the null hypothesis and conclude that the observed counts differ from the expected ones. Conversely, if the p-value is greater than 0.05, we do not reject the null hypothesis and can conclude that the test passes. For the sake of verifying our Multinomial test, we ran ParSplice in different time frames and observed the result. In all cases, we got the p-values are greater than 0.05, which indicates that the tests passed during these instances of the execution. 

<img src='../../images/Blog_0920_BarGraph.png' />

The Multinomial Testing approach is ideal for ParSplice given its constraints, i.e. time, non-determinism, and the existing continuous integration system. The lessons learned from this case study can be valuable to the larger research software community because, like ParSplice, many research software projects have stochastic behavior which produces non-deterministic results. To know more about this case study please take a look at the paper linked below. Please feel free to send me an email if you have any questions.

### Further reading
This article is based on a paper in the proceedings of the International Conference on Computational Science. N.U. Eisty, D. Perez, J.C. Carver, J.D. Moulton, H.A. Nam (2020) *Testing Research Software: A Case Study.* In: Krzhizhanovskaya V. et al. (eds) Computational Science – ICCS 2020. ICCS 2020. Lecture Notes in Computer Science, vol 12143. Springer, Cham. DOI: [10.1007/978-3-030-50436-6_33](https://doi.org/10.1007/978-3-030-50436-6_33)


### Author bio
Nasir Eisty is an assistant professor in the Computer Science and Software Engineering Department of California Polytechnic State University, San Luis, Obispo, CA. He received his Ph.D. degree in Computer Science from the University of Alabama in Spring 2020. His research interests lie in the area of Empirical Software Engineering, Software Quality, and Research Software Engineering. He received a [2020 BSSw (Better Scientific Software) Fellowship](https://bssw.io/pages/meet-our-fellows) award from the Department of Energy (DOE).

<!---
Publish: yes
RSS update: 2020-10-13
Categories: Reliability
Topics: Testing
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
