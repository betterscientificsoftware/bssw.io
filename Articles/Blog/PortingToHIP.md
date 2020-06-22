# Porting Software to AMD's HIP ecosystem

#### Contributed by [Hartwig Anzt](https://hartwiganzt.github.io/ "GitHub Profile")

#### Publication date: September XX, 2020

Witnessing an explosion-like diversification in hardware architectures, hardware portability and the ability to adopt new processor designs has become a central property characterizing software sustainability. In this blog article, we report and discuss the experience of porting CUDA code to AMD's Heterogeneous-Computing Interface for Portability (HIP).

### General Purpose GPU Computing
For many years, NVIDIA's CUDA ecosystem has been the de-facto standard for scientific computing on GPUs. However, it now looks like AMD is gaining enough traction to challenge the NVIDIA hegemony with its ROCm ecosystem. The strategy behind the ROCm effort is different from AMD's previous attempts, as it puts a significant focus on the software ecosystem and offers the HIP language—a program interface very similar to the NVIDIA CUDA ecosystem. In fact, AMD takes an even more aggressive step by providing the ability to compile HIP code for both AMD and NVIDIA architectures. This is accomplished by utilizing source code conversion in combination with NVIDIA's nvcc compiler. Furthermore, AMD is providing the complete ROCm ecosystem and the HIP compiler as open source.

In addition, the US Exascale Computing Project has already announced that two out of three planned Exascale supercomputers will feature AMD GPUs, while none of them are planned to feature NVIDIA components. In short, the fastest supercomputers in the world will rely on AMD GPUs, and we expect to see an increasing number of AMD-based machines as AMD also pushes ROCm and HIP to the forefront.

<br>
<br>
<!--- Image to illustrate the Software Development Cycle --->
<img src='https://github.com/betterscientificsoftware/images/raw/master/ginkgo_overview.png' class='page' /><p class='caption'>Figure 1. Ginkgo's software design separates the high-level algorithms from the hardware-specific kernel implementations.</p>
</p>
<br>

### Designing for Extensibility
Given this setting, it is a natural step to prepare software packages for emerging AMD GPUs. Generally, porting a software package to a new hardware architecture using a different programming model is a cumbersome challenge. However, software packages like [Ginkgo](https://ginkgo-project.github.io/), which keep modularity and extensibility as a primary design principles by consequently separating algorithm implementations from hardware-specific kernels (Figure 1), allow for easy extension to new hardware architectures. It is important to note that the algorithms themselves are unable to execute without the hardware-specific kernels, and adding a back end does not require any changes to the algorithms. This enables the addition and removal of hardware back ends, as required, without impacting the library's functionality on other back ends.

### Converting CUDA Code to HIP
In an effort to make porting CUDA code to the HIP ecosystem as painless as possible, AMD provides a ''hipify'' script for this purpose. We found that AMD's script can successfully translate most of the CUDA code to HIP without problems, thereby reducing the porting effort dramatically. The script only struggles with namespace declarations, e.g., it converts `namespace::kernel<<<...>>> (...)` to `namespace::hipLaunchKernelGGL(kernel, ...)`, while the correct output would be `hipLaunchKernelGGL(namespace::kernel, ...)`. Also, as the HIP ecosystem currently lacks some technical functionality available in the CUDA ecosystem, there remains a small portion of the code that we have to port manually, e.g., cooperative groups. For those, [we developed a cross-platform cooperative group implementation](https://github.com/hartwiganzt/HartwigAnzt.github.io/blob/master/papers/PortingToHip.pdf) (Coop) that provides all functionality of the CUDA ecosystem for both AMD and NVIDIA GPUs and matches the performance of NVIDIA's legacy implementation (Figure 2).

<br>
<br>
<!--- Image to illustrate the Software Development Cycle --->
<img src='https://github.com/betterscientificsoftware/images/raw/master/cooperative_groups.png' class='page' /><p class='caption'>Figure 2. Performance of Ginkgo's cross-platform cooperative group implementation (Coop) in comparison with NVIDIA's legacy implementation on the NVIDIA V100 GPU.</p>
</p>
<br>

<br>
<br>
<!--- Image to illustrate the Software Development Cycle --->
<img src='https://github.com/betterscientificsoftware/images/raw/master/cuda_vs_hip.png' class='page' /><p class='caption'>Figure 3. Kernel syntax and kernel launch syntax for CUDA (left) and HIP (right).</p>
</p>
<br>


### Reducing Code Duplication
The HIP language is not only inspired by CUDA, but HIP kernels are in many cases
even identical to CUDA code (Figure 3). Only the kernel launch syntax and
hardware-specific (tuning) parameters like warp size (NVIDIA) and wavefront size
(AMD) are different. As a result, extending a software package with a complete
stack of HIP kernels for an AMD GPU back end results in significant code
duplication. Duplicated code is tedious to keep in sync and makes software more
error prone. To increase sustainability, we decided to create a ''common''
codebase containing the templated kernels that are configured during the
compilation process for the specific back ends. This strategy not only avoids
the duplication of code but also reduces the size of the codebase. In the
realization of the HIP back end, we rearranged Ginkgo's codebase to split the
code into 1/3 ''common'' code, 1/3 HIP-specific code, and 1/3 CUDA-specific code
(Figure 4). The CUDA-specific and HIP-specific code mostly contain the kernel
launches including the templated kernels of the ''common'' code. Only if a kernel disign differs significantly for the CUDA and the HIP backend, the kernel is seperated into the distinct back ends.

<br>
<br>
<!--- Image to illustrate the Software Development Cycle --->
<img src='https://github.com/betterscientificsoftware/images/raw/master/ginkgo_reorganization.png' class='page' /><p class='caption'>Figure 4. Reorganizing Ginkgo's codebase to avoid code duplication.</p>
</p>
<br>

### Compiling HIP code for NVIDIA Architectures
As previously mentioned, the HIP ecosystem enables one to compile for both AMD GPUs and NVIDIA GPUs. After completing a production-ready HIP back end for Ginkgo, we are interested in the performance penalty we pay when compiling HIP code for an NVIDIA GPU instead of using the native CUDA code. In Figure 5, we show the speedup of Ginkgo's CUDA back end vs. Ginkgo's HIP back end (compiled for NVIDIA architectures) when running on an NVIDIA V100 GPU. We processed 2,800 sparse matrices from the [Suite Sparse Matrix Collection](https://sparse.tamu.edu/) and visualize from left to right the performance ratios for: (1) Ginkgo's SellP SpMV, (2) the CSR SpMV of the vendor library, (3) Ginkgo's COO SpMV, and (4) Ginkgo's CG solver. As expected, the native CUDA code typically runs slightly faster. However, we note that (ignoring some outliers), the performance differences are typically within 5%, which demonstrates that AMD succeeds in providing a cross-platform GPU programming interface.

<br>
<br>
<!--- Image to illustrate HIP's performance portability --->
<img src='https://github.com/betterscientificsoftware/images/raw/master/hip_portability.png' class='page' /><p class='caption'>Figure 5. Performance of Ginkgo's HIP back end (compiled for NVIDIA architectures) vs. Ginkgo's native CUDA back end on NVIDIA's V100 GPU.</p>
</p>
<br>

### Further Reading and References
Tsai et al.: [<i>Preparing Ginkgo for AMD GPUs -- A Testimonial on Porting CUDA Code to HIP</i>](https://github.com/hartwiganzt/HartwigAnzt.github.io/blob/master/papers/PortingToHip.pdf)<br>
AMD: [<i>HIP Porting Guide</i>](https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP-porting-guide.html)<br>
AMD: [<i>HIP kernel
language</i>](https://rocmdocs.amd.com/en/latest/Programming_Guides/Kernel_language.html#kernel-language)



### Author's Bio
[Hartwig Anzt](https://github.com/hartwiganzt) is a Helmholtz Young Investigator Group leader at the Steinbuch Centre for Computing at the Karlsruhe Institute of Technology, Germany. He also holds a Research Consultant position in Jack Dongarra's [Innovative Computing Lab](http://www.icl.utk.edu/) at the University of Tennessee, USA. Hartwig Anzt has a strong background in numerical mathematics, specializes in iterative methods and preconditioning techniques for the next-generation hardware architectures, and has a long track record of high-quality software development. He is author of the [MAGMA-sparse](http://icl.cs.utk.edu/magma/) open source software package, managing lead and developer of the [Ginkgo project](https://ginkgo-project.github.io/), and part of the ["Production-ready, Exascale-enabled Krylov Solvers for Exascale Computing" (PEEKS)](http://icl.utk.edu/peeks/) effort for delivering production-ready numerical linear algebra libraries as part of the [Exascale Computing Project](https://www.exascaleproject.org/).


<!---
Publish: preview
RSS Update: 2019-08-27
Categories: development
Topics: testing, design
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
