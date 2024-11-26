## Balancing Productivity, Portability and Performance in CFD

<!--- deck text start --->
This article discusses how to identify an appropriate level of abstraction when balancing the "Three Ps" in CFD applications. 
<!--- deck text end --->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: November 25, 2024

Resource information | Details
:--- | :--- 
Paper title  | Productivity, performance, and portability for computational fluid dynamics applications
Authors | István Z. Reguly, Gihan R. Mudalige
Publication | Year 2020, Computers and Fluids, DOI: [10.1016/j.compfluid.2020.104425](https://doi.org/10.1016/j.compfluid.2020.104425)

This journal article discusses the evolving landscape of high performance computing (HPC) architectures over the past decade and their implications for computational fluid dynamics (CFD) applications in particular.
The paper focuses on balancing the "Three Ps"; Productivity, Portability and Performance.
Traditional programming approaches struggle to adequately address all three goals simultaneously.
Some recent technology introductions involving template libraries and Domain Specific Languages (DSLs) offer potential solutions by sacrificing generality for specialized focus.

The paper reviews various high-level libraries and low-level techniques that aid in describing partial differential equations (PDEs) symbolically and targeting specific algorithmic patterns respectively.
The article also examines the benefits and challenges of these methods, including their performance on different hardware architectures and with different programming models.

Significantly, the paper details the tension between maximizing performance and ensuring portability and productivity.
It discusses the adoption of separate computational accelerators like GPUs, which have led to heterogeneous computing environments.
This has necessitated the development of new programming paradigms and tools that separate the *what* of computation from the *how*, moving away from traditional imperative programming languages like C or Fortran.

Furthermore, the article discusses various software libraries and tools that have been developed to target specific problem domains in CFD, which help address these challenges by offering a balance between performance, portability, and productivity.
It mentions several notable libraries and frameworks, such as Kokkos and RAJA, which provide abstractions to facilitate portability across different computing environments while still aiming to harness optimal performance from the underlying hardware.

Overall, the article provides a comprehensive overview of the state-of-the-art techniques in programming for CFD within the context of modern and evolving HPC architectures, highlighting both the progress and ongoing challenges in the field.

<!---
Publish: yes
Pinned: no
Topics: performance portability, programming languages
--->
