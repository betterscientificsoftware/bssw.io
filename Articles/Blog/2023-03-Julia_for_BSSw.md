# Julia's value proposition for Better Scientific Software

 **Hero Image:**

  - <img src='../../images/Blog_2303_julia.svg' width="300" height="200" />[The Julia programming language logo from https://julialang.org.]

#### Contributed by: [William F Godoy](https://github.com/williamfgc)

#### Publication date: March 16, 2022

<!-- start of deck text -->
Julia provides a mathematical front end to LLVM to provide easy CPU/GPU performant access and lightweight interoperability with existing C, Fortran, R and Python codes, coupled with a rich unified ecosystem for packaging, data science, interactive computing. Hence, filling the gap at the intersection of high-performance + high-productivity for scientific software.
<!-- end of deck text -->
### Introduction

In 2023 our requirements for scientific software have expanded beyond number crunching, with reproducibility, AI workflows, data analysis and visualization, continuous integration and continuous deployment (CI/CD) pipelines, packaging and interactive computing taking a central role in the scientific discovery process.
The current "status-quo" in to use a compiled language (Fortran, C, C++) for performance critical code, while a higher-level language (e.g. Python) is preferred for non-performant aspects with the promise of higher-productivity. 
Nevertheless, we interact with ecosystem aspects typically offloaded to third-party components such as: build systems, packaging, and programming models to access heterogenous hardware, e.g. graphical processing units (GPUs).
Under this model, we must deal with a many-body language and ecosystem problem with code bases usually composed of a `Main Language` + `X`, in which X is a (very) long vector of components, e.g. `X = { Python, C, C++, Fortran, CMake, Make, Catch, doctest, pytest, pybind11, conda, pip, Jupyter, apt, yum, ...}`, with no guarantees for interoperability among these. Thus overall economics and productivity take a toll that scales with project size and performance portability requirements.
At a lower-level, LLVM has emerged in the last decade as the back end toolchain of choice for major compiler vendors. LLVM is a game changer creating not only a unifying layer, but a collaborative open-source model across vendors and the computing community.

### Why Julia?

**Why do we keep creating new languages and ecosystems?** We are in a constant need for new abstractions that empower practitioners by lowering existing technical, economical and social barriers. Just like Fortran (originally FORTRAN) allowed access to a "formula translator" model in the 1950s, while C enabled "portable assembly" for systems programming since the 1970s, or the success of Python as a friendly interface that enhances productivity in the twentieth first century era of cloud-based development; Julia proposes an evolutionary approach to today's scientific software development process that is highly exploratory and needs to constantly adapt to new, many times unexpected - e.g. COVID-19 -, science requirements.

As shown in Figure 2, Julia's high-productivity + high-performance layer builds upon LLVM for CPU and GPU access and a unified open-source packaging and data science ecosystem hosted on GitHub. Julia also provides lightweight interoperability with existing C and Fortran codes. Hence, the value proposition is not to replace a particular language, but to reduce current costs in the scientific software development process (e.g. from prototyping to publication with Python + X).

 - <img src='../../images/Blog_2303_julia_value_proposition.png' />[Figure 2: Julia's value proposition to the construction process in scientific software.]

**The Ecosystem is NOT an afterthought**
In Julia, project description and dependencies is your starting point when [creating a new package](https://pkgdocs.julialang.org/v1/creating-packages/), see [toml files](https://pkgdocs.julialang.org/v1/toml-files/). Just inspect any [Julia package](https://juliapackages.com/) source code on GitHub and see their Project.toml files for a list of dependencies and compatibility. In addition, [unit testing](https://docs.julialang.org/en/v1/stdlib/Test/), interactive computing via the read–eval–print loop (REPL), a [standard library](https://juliafs.readthedocs.io/en/stable/stdlib/index.html) with mathematical and data abstractions, and a unified package manager with access to a rich ecosystem for scientific computing, data [science](https://www.juliafordatascience.com/), [visualization](https://juliapackages.com/c/graphics), and [AI](https://fluxml.ai/Flux.jl/stable/ecosystem/).

So how is this different from Python's ecosystem? Just the other day GitHub Actions bumped its Python version to 3.11 on some of its runners, causing  breakage in some packages for which 59.4% - as of March of 2023 - of the most popular packages don't specify support yet on [PyPI]((https://pyreadiness.org/3.11/)). Thus, the cost of this coordination is passed to the end-user until package developers are able to react. This last word is key, since Julia promotes a more "predictive" rather than "reactive" maintenance approach in which packages in Julia's [General registry](https://github.com/JuliaRegistries/General) must meet certain requirements. We don't live in a perfect world, thus the value of this coordination is not just on "not breaking the API" or "fixing bugs", but in enriching user-developer communications using an open-source process for package updates prior to deployment. 

This model of "batteries included" is not new for more targeted (R, Matlab) languages, but it's new for modern languages that puts performance (Julia) and safety (Rust) at the forefront. I find myself writing more tests and verifiying my ideas on the REPL when using Julia, rather than writing boilerplate code as in general purpose language or dealing with mismatching package versions.

**Making heterogeneous hardware more accesible**
[JuliaGPU](https://juliagpu.org/) and [JuliaParallel](https://github.com/JuliaParallel) provide information on the packages that provide access to several vendor GPUs, e.g. NVIDIA ([CUDA.jl](https://github.com/JuliaGPU/CUDA.jl), AMD ([AMDGPU.jl](https://github.com/JuliaGPU/AMDGPU.jl)), Intel ([oneAPI.jl](https://github.com/JuliaGPU/oneAPI.jl)). These high-level interfaces provide an excellent mathematical playground for exploring fine-granularity parallelization on GPU. The [CUDA.jl docs](https://cuda.juliagpu.org/dev/) are a great starting point for those familiar with NVIDIA's CUDA or want to learn about GPU custom kernel programming. Python's proposition is to rely on CUDA (pyCUDA, cuPy) to pass custom kernels as strings, while Julia uses a common [GPUCompiler.jl](https://github.com/JuliaGPU/GPUCompiler.jl) layer. 

**Compose to prevent inheritance bloat**
Julia does not support object-oriented as C++ or Python. Julia projects are organized by modules and proper data locality and composition using "data container" structs and type hierarchy trees in which abstract types have no members, see related [discussion](https://github.com/JuliaLang/julia/issues/4935). Think of composition as Derived "has-a" Base, instead of Derived "is-a" Base. This weak-coupling prevents long hierarchies of classes that can go out of hand really quickly, while encouraging software developers to think of structs as data containers for which operations are applied - as one would do in languages like pre-2003 Fortran, R or C.

**Interoperate with existing software**
Julia enables lightweight reusability of existing Fortran and C infrastructure via the [`@ccall` macro](https://docs.julialang.org/en/v1/manual/calling-c-and-fortran-code/). Similarly, Python and R interoperability is possible with [PyCall.jl](https://github.com/JuliaPy/PyCall.jl) and [RCall.jl](https://github.com/JuliaInterop/RCall.jl), respectively. So Julia does not promote "reinventing", but rather "reusing" existing wheels (pun not intended) as mature scientific software can be a large investments.

**Jupyter and Pluto.jl Notebooks**
Notebooks, Jupyter in particular, have become a widely adopted environment in science with support to several language kernels and does not need an introduction. Jupyter is powered by Anaconda with Python kernels requiring setting a conda environment for managing the required dependencies prior to launching the server and web client interface. Notebooks are stored using a *.ipynb file format based on JSON. Julia kernels reuse the information readily available in your Project.toml, this is really neat when using services like [mybinder.org](https://mybinder.org/) for distributing and sharing notebook projects "as-is" with a broader audience.

[Pluto.jl](https://plutojl.org/) is the Julia-exclusive alternative which favors "reactive" notebooks for interactivity, essentially levelages the fact that packaging is part of the language. There is no need for setting an environment, just launch Pluto from the REPL, start importing package dependencies directly on you notebooks and save them as a Julia file (.jl) in which markdown and code cells are just identified by annotations. Despite being an amortized cost, the "time to first plot" (TTFP) is a recurrent issue that is actively being addressed in recent versions, see discourse [thread](https://discourse.julialang.org/t/julia-v1-9-0-beta2-is-fast/92290), I enjoy the plug and play approach in which the mathematical syntax, ecosystem and packaging simplify my work. The first time Pluto is launched it provides several sample notebooks of what can be done, the introduction to [Plots.jl](https://docs.juliaplots.org/stable/) is shown in Fig 3.

Launching a Pluto Notebook from the REPL.

```julia
$ julia
> using Pluto
> Pluto.run()
[ Info: Loading...
[ Info: Listening on: 127.0.0.1:1234, thread id: 1
┌ Info: 
└ Opening http://localhost:1234/?secret=AZ8Ynd82 in your default browser... ~ have fun!
┌ Info: 
│ Press Ctrl+C in this terminal to stop Pluto
└
```

<img src='../../images/Blog_2303_julia_pluto.png' />[Intro to Plots.jl Pluto notebook from default examples.]


**The Community**
This is where the real value of Julia lies upon. The community is very entusiasthic in helping others and uses a modern way to engage using the [Julia slack](https://julialang.org/slack/) and [discord](https://discourse.julialang.org/t/julialang-official-discord-server/45499) channel, and each package GitHub issues tracker. Stackoverflow can be outdated and many answers might have not aged well. [JuliaCon](https://juliacon.org/2023/) is the annual gathering for which several insteresting talks and tutorials can be found on YouTube. Many contributions and support come from [JuliaHub](https://juliahub.com/)(formerly Julia Computing) as part of the mission. One thing to keep in mind as the language and ecosystem matures is that the community is invested in performance from day one.

We organized a full-day workshop last summer centered around Julia for Oak Ridge National Laboratory (ORNL) Science, [JuFOS](https://ornl.github.io/events/jufos2022/), which to our surprise had a high number of registrations from different scientific domains. Out of the 101 registered participants, roughly 90% responded that they wanted to learn more about Julia, while roughly 50% indicated interest in alternatives to the current status-quo for building scientific workflows in the high-level + high-productivity space.  

On the high-performance computing (HPC) front, we put our thoughts in a [recent paper](https://arxiv.org/abs/2211.02740). Meanwhile, building the community has kept many of us very busy in the last few years. Several [venues](https://juliaparallel.org/resources/) were organized in the last years, including a tutorial and BoFs organized by the US Department of Energy [Exascale Computing Project](https://www.exascaleproject.org/), a Supercomputing [BoF](https://sc22.supercomputing.org/presentation/?id=bof136&sess=sess309), a JuliaCon [minisymposium](https://live.juliacon.org/talk/LUWYRJ), and a monthly [JuliaHPC call](https://julialang.org/community/#events) to provide exposurehighlight the work done by community members.

It's worth mentioning that unifying and coordinated initiatives comiong out of the Exascale Computing Project (ECP) like [Spack](https://spack.io/) and [e4s](https://e4s-project.github.io/) provide excellent interoperability opportunities for accessible HPC packages within the Julia ecosystem. 

### Where to start
For a more technical introduction, I wrote an article in 2020 that [I revised in 2023](https://williamfgc.github.io/programming/scientific-computing/2023/03/03/first-project-julia-language.html). The reader will find several resources and similar content with more details. I'd recommend to anyone trying the language for the first time to use Visual Studio Code, and the upcoming [Julia v1.9 version](https://julialang.org/downloads/#upcoming_release) for a better experience.
 In addition, find people in your community using or advocating (or not) the use of Julia and learn from them. Ultimately, scientific software can be heavily community-driven.
 *Bonus: using GitHub copilot + the simple Julia APIs are a welcome addition for productivity. It saves on typing, not thinking. Perhaps it's an opportunity for modernizing legacy Fortran codes?*

### Final Thoughts
Julia is part of the natural evolution of programming languages. Powered by LLVM and an orchestrated ecosystem, the value proposition and  design decisions target the high-performance + high-productivity space. Mastering a new programming language can be a steep initial investment, and final adoption is a result of technical and non-technical aspects. Still it's good that the community is exposed to the value proposition of newer alternatives like Julia and that's the goal of this article. The actual value is finally given by each user, project and their specific scientific software needs. 

### Acknowledgement
I want to thanks the many people in the community for enabling our efforts. This research was supported by the Exascale Computing Project (17-SC-20-SC), a collaborative effort of the U.S. Department of Energy Office of Science and the National Nuclear Security Administration. In particular the IDEAS, PROTEAS-TUNE sub-projects, the SRP program and the ASCR Bluestone project.

### Author Bio

[William F. Godoy](https://orcid.org/0000-0002-2590-5178) is a Senior Computer Scientist in the Computer Science and Mathematics Division at Oak Ridge National Laboratory (ORNL). His interests are in the areas of high-performance computing (HPC) scientific software, programming models, data and parallel I/O.
At ORNL, he has contributed to scientific software projects funded by the US Department of Energy Exascale Computing Project and the Neutron Science Facilities. Godoy received his PhD in Mechanical Engineering from the University at Buffalo, The State University of New York. He is a 2022 BSSw Fellowship honorable mention, a US-RSE and ACM member and a IEEE senior member serving in several technical venues.


<!---
Publish: yes
Pinned: no
Topics: programming languages and models, packaging, performance portability and productivity, high-performance computing (HPC), testing, software engineering
--->
