# Reproducibility in the Age of Approximate Computing

#### Contributed by [Harshitha Menon](https://github.com/harshithamenon)

#### Publication date: June 11, 2025

<!--deck start-->
From floating-point representation to iterative solvers, approximation has always been embedded in scientific computing. But today, hardware trends, especially those driven by AI workloads, bring that tradeoff to the forefront. The question is no longer *if* we can tolerate approximation, but *how much* and *where.* This shift redefines how we think about performance in future HPC systems.
<!--deck end-->

Reproducibility is the bedrock of any scientific process. In computational science, it historically has meant that running the simulation multiple times on the same input data should produce the same output – in some cases bit-for-bit identical results. However, as we push the boundaries of scale and performance in high-performance computing (HPC) to exascale and beyond, we face programming paradigms that enable tradeoffs between accuracy, performance, and energy efficiency. While new programming paradigms can accelerate discovery, they should also prompt us to rethink computational reproducibility.

### What is Approximate Computing and why it matters?

As we reach the limits of Moore’s law and the end of Dennard scaling, there is increased emphasis on alternative system architectures and computing paradigms to achieve future performance gains. Approximate computing, where accuracy is traded for performance, is a promising approach. Approximate computing is based on the intuitive observation that while performing exact computation or maintaining peak-level service demand requires a high amount of resources, allowing selective approximation or occasional violation of the specification can provide disproportionate gains in efficiency. This shift is particularly evident in exascale architectures, where lower-precision arithmetic plays an important role in meeting energy and performance targets. For example, the Frontier supercomputer at Oak Ridge National Laboratory demonstrated an impressive 7.94 EFlop/s on the HPL-MxP benchmark by leveraging mixed-precision computation, far surpassing its performance using double-precision computation. Mixed-precision computation involves using multiple levels of precision for floating-point data and arithmetic operations to balance accuracy and performance and has been shown to significantly enhance the performance of scientific applications.  

### Reproducibility

First, we must define what reproducibility means. Dr. Victoria Stodden, a leading expert in this field, classifies reproducibility into three distinct categories: empirical reproducibility, statistical reproducibility, and computational reproducibility.<sup>[1]</sup> 
Historically, computational reproducibility has often meant bit-exact reproducibility, though that has become harder to achieve while taking advantage of the features of modern HPC hardware, and is increasingly viewed as an unnecessarily high bar.
Statistical reproducibility ensures that results are consistent within statistical bounds across multiple runs. Bounded-error reproducibility guarantees that results remain within acceptable error margins for critical outputs. Semantic reproducibility focuses on whether high-level conclusions and decisions remain unchanged despite numerical differences. One needs to decide what makes sense for their application.

### Address the challenges

For approximate computing to be widely used in HPC, we need to have a balance between performance and maintaining the scientific validity of the results. One of the first and foremost steps is identifying where it can be safely applied without introducing unacceptable errors. The use of controlled inaccuracies has been applied in various linear algebraic kernels at the algorithmic level. Jack Dongarra, a pioneer in HPC, famously described certain linear algebra algorithms as “responsibly reckless”. These approaches encourage trying faster, less resource-intensive algorithms, even if they may be less stable or occasionally fail. The idea is to use approximations optimistically but monitor for instability, recomputing results using more stable algorithms only when necessary.<sup>[2]</sup> Recent work provides error analyses and insights that will enable the use of mixed-precision in numerical linear algebra.<sup>[3]</sup> For instance, Carson and Higham<sup>[4]</sup> introduced a three-precision iterative refinement algorithm for solving linear systems, using low precision for LU factorization, standard precision for the working solution, and high precision for residual computations, which provided significant performance improvements. Mixed-precision LU factorization with iterative refinement was successfully implemented on GPUs to exploit Tensor Cores for fast matrix solves.<sup>[5]</sup> These techniques illustrate how carefully designed mixed-precision algorithms, guided by numerical analysis, can provide speedups while ensuring result quality.

Formalizing and bounding the errors introduced by approximate computing strategies is crucial. Techniques like QDOT (Quantized Dot Product)<sup>[6]</sup> provide deterministic error guarantees while still achieving significant performance improvements. QDOT intelligently determines which data can be safely approximated, accelerating critical computations while maintaining user-specified error thresholds. Furthermore, techniques like uncertainty quantification (UQ)<sup>[7]</sup> and algorithmic differentiation (AD)<sup>[8]</sup> have proven effective in analyzing sensitivity and identifying code regions that can safely operate at lower precision with minimal impact on final results. These tools and techniques allow developers to understand the propagation of approximation errors and focus high-precision resources only where they are needed.

To make these methods accessible, we need better tools and frameworks. Solutions like the HPAC framework<sup>[9]</sup> help developers experiment with various approximation strategies in OpenMP-based HPC applications. These tools lower the barrier to adoption, helping developers confidently navigate the complex tradeoffs between performance, accuracy, and reproducibility.

### Conclusion

Approximate computing has moved from the sidelines to center stage as it has become essential for pushing the boundaries of science in the exascale era and beyond. We need to approach this shift with care, paying close attention to where and how approximations are applied. New tools that help us automatically analyze sensitivity, track reproducibility, and enforce error limits will play a big role in making this possible. In this new landscape, reproducibility isn’t about achieving perfection, it is about building trust. That means being transparent about the tradeoffs we make, experimenting carefully, and rethinking what it means to produce reliable, meaningful results in computational science.

### Author bio

Harshitha Menon is a Research Scientist at the Center for Applied Scientific Computing (CASC) at Lawrence Livermore National Laboratory (LLNL). Her research focuses on large language models (LLMs) and machine learning for HPC code development, approximate computing, and floating-point mixed-precision analysis. She has conducted research focused on understanding the tradeoff between accuracy and performance through the development of tools and methods, such as ADAPT, HPAC, Puppeteer, and QDOT, that quantify the impact of errors and guide precision tuning. Harshitha received her Ph.D. in 2016 and M.S. in 2012, both from the University of Illinois at Urbana-Champaign. She is a recipient of the ACM/IEEE-CS George Michael Fellowship in 2014, the Anita Borg Scholarship in 2014, and the Siebel Scholarship in 2012.

<!---
Publish: yes
Track: Deep dive 
Topics: reproducibility, requirements, design, "high-performance computing (hpc)"
--->

[1-sfer-ezikiw]: https://imstat.org/2013/11/17/resolving-irreproducibility-in-empirical-and-computational-research/ "Resolving irreproducibility in empirical and computational research {Stodden, V. (2013). Resolving irreproducibility in empirical and computational research. *IMS Bulletin*.}"

[2-sfer-ezikiw]: https://doi.org/10.1145/1188455.1188573 "Exploiting the Performance of 32 bit Floating Point Arithmetic in Obtaining 64 bit Accuracy {Langou, J., Langou, J., Luszczek, P., Kurzak, J., Buttari, A. and Dongarra, J. (2006), Exploiting the Performance of 32 bit Floating Point Arithmetic in Obtaining 64 bit Accuracy (Revisiting Iterative Refinement for Linear Systems), *SC '06: Proceedings of the 2006 ACM/IEEE Conference on Supercomputing*, doi:10.1145/1188455.1188573.}"

[3-sfer-ezikiw]: https://hal.science/hal-03537373v2 "Mixed precision algorithms in numerical linear algebra {Higham, N., Mary, T. (2022). Mixed precision algorithms in numerical linear algebra. Hal-03537373v2.}"

[4-sfer-ezikiw]: https://doi.org/10.1137/17M1140819 "Accelerating the solution of linear systems by using a three-precision iterative refinement algorithm {Carson, E., & Higham, N. J. (2018). Accelerating the solution of linear systems by using a three-precision iterative refinement algorithm. *SIAM Journal on Scientific Computing*, doi:10.1137/17M1140819.}"

[5-sfer-ezikiw]: https://doi.org/10.1109/SC.2018.00050 "Harnessing GPU tensor cores for fast FP16 arithmetic to speed up mixed-precision iterative refinement solvers {Haidar, A., Tomov, S., Dongarra, J. and Higham, N. (2018), Harnessing GPU tensor cores for fast FP16 arithmetic to speed up mixed-precision iterative refinement solvers, in Proceedings of the International Conference for High Performance Computing, Networking, Storage, and Analysis, SC18, doi:10.1109/SC.2018.00050.}"

[6-sfer-ezikiw]: https://doi.org/10.1137/21M1406994 "A framework for error-bounded approximate computing, with an application to dot products {Diffenderfer, J., Osei-Kuffuor, D., & Menon, H. (2022). A framework for error-bounded approximate computing, with an application to dot products. *SIAM Journal on Scientific Computing*, doi:10.1137/21M1406994.}"

[7-sfer-ezikiw]: https://dl.acm.org/doi/10.5555/3571885.3571974 "Approximate computing through the lens of uncertainty quantification {Parasyris, K., Diffenderfer, J., Menon, H., Laguna, I., Vanover, J., Vogt, R., & Osei-Kuffuor, D. (2022, November). Approximate computing through the lens of uncertainty quantification. In *SC22: International Conference for High Performance Computing, Networking, Storage and Analysis*.}"

[8-sfer-ezikiw]: https://doi.org/10.1109/SC.2018.00051 "Adapt: Algorithmic differentiation applied to floating-point precision tuning {Menon, H., Lam, M. O., Osei-Kuffuor, D., Schordan, M., Lloyd, S., Mohror, K., & Hittinger, J. (2018, November). Adapt: Algorithmic differentiation applied to floating-point precision tuning. In *SC18: International Conference for High Performance Computing, Networking, Storage and Analysis*, doi:10.1109/SC.2018.00051.}"

[9-sfer-ezikiw]: https://doi.org/10.1145/3458817.3476216 "HPAC: evaluating approximate computing techniques on HPC OpenMP applications {Parasyris, K., Georgakoudis, G., Menon, H., Diffenderfer, J., Laguna, I., Osei-Kuffuor, D., & Schordan, M. (2021, November). HPAC: evaluating approximate computing techniques on HPC OpenMP applications. In *Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis*, doi:10.1145/3458817.3476216.}"
<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "Resolving irreproducibility in empirical and computational research"
[2]: #sfer-ezikiw-2 "Exploiting the Performance of 32 bit Floating Point Arithmetic in Obtaining 64 bit Accuracy"
[3]: #sfer-ezikiw-3 "Mixed precision algorithms in numerical linear algebra"
[4]: #sfer-ezikiw-4 "Accelerating the solution of linear systems by using a three-precision iterative refinement algorithm"
[5]: #sfer-ezikiw-5 "Harnessing GPU tensor cores for fast FP16 arithmetic to speed up mixed-precision iterative refinement solvers"
[6]: #sfer-ezikiw-6 "A framework for error-bounded approximate computing, with an application to dot products"
[7]: #sfer-ezikiw-7 "Approximate computing through the lens of uncertainty quantification"
[8]: #sfer-ezikiw-8 "Adapt: Algorithmic differentiation applied to floating-point precision tuning"
[9]: #sfer-ezikiw-9 "HPAC: evaluating approximate computing techniques on HPC OpenMP applications"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[Resolving irreproducibility in empirical and computational research<br>Stodden, V. (2013). Resolving irreproducibility in empirical and computational research. *IMS Bulletin*.](https://imstat.org/2013/11/17/resolving-irreproducibility-in-empirical-and-computational-research/)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[Exploiting the Performance of 32 bit Floating Point Arithmetic in Obtaining 64 bit Accuracy<br>Langou, J., Langou, J., Luszczek, P., Kurzak, J., Buttari, A. and Dongarra, J. (2006), Exploiting the Performance of 32 bit Floating Point Arithmetic in Obtaining 64 bit Accuracy (Revisiting Iterative Refinement for Linear Systems), *SC '06: Proceedings of the 2006 ACM/IEEE Conference on Supercomputing*, doi:10.1145/1188455.1188573.](https://doi.org/10.1145/1188455.1188573)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[Mixed precision algorithms in numerical linear algebra<br>Higham, N., Mary, T. (2022). Mixed precision algorithms in numerical linear algebra. Hal-03537373v2.](https://hal.science/hal-03537373v2)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[Accelerating the solution of linear systems by using a three-precision iterative refinement algorithm<br>Carson, E., & Higham, N. J. (2018). Accelerating the solution of linear systems by using a three-precision iterative refinement algorithm. *SIAM Journal on Scientific Computing*, doi:10.1137/17M1140819.](https://doi.org/10.1137/17M1140819)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[Harnessing GPU tensor cores for fast FP16 arithmetic to speed up mixed-precision iterative refinement solvers<br>Haidar, A., Tomov, S., Dongarra, J. and Higham, N. (2018), Harnessing GPU tensor cores for fast FP16 arithmetic to speed up mixed-precision iterative refinement solvers, in Proceedings of the International Conference for High Performance Computing, Networking, Storage, and Analysis, SC18, doi:10.1109/SC.2018.00050.](https://doi.org/10.1109/SC.2018.00050)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[A framework for error-bounded approximate computing, with an application to dot products<br>Diffenderfer, J., Osei-Kuffuor, D., & Menon, H. (2022). A framework for error-bounded approximate computing, with an application to dot products. *SIAM Journal on Scientific Computing*, doi:10.1137/21M1406994.](https://doi.org/10.1137/21M1406994)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[Approximate computing through the lens of uncertainty quantification<br>Parasyris, K., Diffenderfer, J., Menon, H., Laguna, I., Vanover, J., Vogt, R., & Osei-Kuffuor, D. (2022, November). Approximate computing through the lens of uncertainty quantification. In *SC22: International Conference for High Performance Computing, Networking, Storage and Analysis*.](https://dl.acm.org/doi/10.5555/3571885.3571974)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[Adapt: Algorithmic differentiation applied to floating-point precision tuning<br>Menon, H., Lam, M. O., Osei-Kuffuor, D., Schordan, M., Lloyd, S., Mohror, K., & Hittinger, J. (2018, November). Adapt: Algorithmic differentiation applied to floating-point precision tuning. In *SC18: International Conference for High Performance Computing, Networking, Storage and Analysis*, doi:10.1109/SC.2018.00051.](https://doi.org/10.1109/SC.2018.00051)
* <a name="sfer-ezikiw-9"></a><sup>9</sup>[HPAC: evaluating approximate computing techniques on HPC OpenMP applications<br>Parasyris, K., Georgakoudis, G., Menon, H., Diffenderfer, J., Laguna, I., Osei-Kuffuor, D., & Schordan, M. (2021, November). HPAC: evaluating approximate computing techniques on HPC OpenMP applications. In *Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis*, doi:10.1145/3458817.3476216.](https://doi.org/10.1145/3458817.3476216)
