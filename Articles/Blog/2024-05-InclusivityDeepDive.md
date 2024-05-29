# A Deep Dive on the Role of Inclusivity in Scientific Computing

#### Contributed by [Rinku Gupta](https://github.com/rinkug) and [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: May 29, 2024

<!--deck start-->
Inclusive practices have a role to play in many aspects of any scientific computing project.
<!--deck end-->

<!--body start--->
> Inclusivity [in scientific computing] is about practices to ensure people with diverse identities and experiences have equitable access to resources and opportunities, feel safe, welcomed, respected and valued, and are encouraged to contribute as their full, authentic selves in any particular group or activity. [Tony Baylis](https://people.llnl.gov/baylis3) -- LLNL Director of Strategic Diversity

If *diversity* is being asked to the scientific computing party, *inclusivity* is being asked to dance.
Inclusivity is [accessibility’s](https://www.inclusionhub.com/articles/a11y-at-salesforce) close cousin.

Inclusivity and inclusive practices can play a role in improving almost every aspect of a scientific computing project, including documentation, user interface, user experience, customer support processes, collaborations, presentations, publications, and other communications (e.g., GitHub or email) and even the actual code we write.
The benefits of inclusive practices include reducing barriers to adoption, increasing a product's reach, improving productivity, increasing innovation, attracting and retaining a wider talent pool, and improving job satisfaction.

For some, inclusive practices and inclusivity can be indistinguishable from the often institutionalized enterprise of Diversity, Equity, and Inclusion (DE&I).
Viewed through a DE&I lens, inclusivity can wind up being seen as an exercise in achieving compliance more than in providing added value to a scientific computing project.
In turn, topics central to DE&I such as gender identity, sexual harassment, and racism can easily obscure our perception of the full landscape of inclusive practices.
It is important to keep in mind that although these topics tend to capture more of the news headlines and tend to be where a lot of the more serious DE&I work is needed, inclusivity is actually much, much wider than those topics.

There are many other dimensions to inclusivity such as neurodivergence (15-20% prevalence), mobility impairment (16%), handedness (10%), dyslexia/dyscalculia (3-7%), visual impairment (1%-40%, depending on how we count), hearing impairment (15%), speaking impairment (3-7%), being prone to migraines (10%), or being color vision deficient (CVD) (5%).
In addition, without trying too hard, it’s easy to think of many other ways in which large swaths of the scientific computing community have a shared experience impacting participation, which without care, can lead to [inclusivity bugs](https://bssw.io/items/inclusivity-bugs), including such things as English as a second language, immigration status, culturally or religiously relevant legal holidays, remote/hybrid work arrangements, and even time zones, just to name a few.

It is probably easy for most of us to connect the relevance of *some* of these dimensions (e.g., handedness, dyscalculia or color blindness) directly with the day-to-day work of developing scientific computing software.
Some of us may have more difficulty seeing how many of the *other* dimensions to inclusion (e.g., English as a second language, immigration status, culturally relevant legal holidays, etc.) also play a significant role in the work of scientific computing.

The software and the work involved in developing it is just one aspect of a successful and sustainable scientific computing project.
Most of the work in scientific computing involves large, multidisciplinary teams with contributors from all over the world to advance science in service to the world.
Ultimately, the scientific productivity of these projects is significantly impacted by the ability of people to work together, collaborate ethically and trustfully, communicate with clarity and empathy, and be inspired to contribute authentically and with enthusiasm and thoughtfulness.
Inclusivity and inclusive practices play a key role in facilitating all of that and more.
Likewise, the lack of attention to inclusivity and inclusive practices can dramatically negatively impact scientific productivity.

A flagship inclusivity practice in scientific computing is aimed at [broadening access and participation](https://bssw.io/blog_posts/increasing-productivity-by-broadening-participation-in-scientific-software-communities) by historically marginalized populations.
However, it is certainly not the *only* practice.
Examples of other practices include adopting a [code of conduct](https://www.acm.org/code-of-ethics), having well-defined on-boarding and off-boarding processes, removing [`master`/`slave` terminology](https://bssw.io/blog_posts/experiences-replacing-master-slave-terminology-in-ale3d-and-sierra) from a code base and other [inclusive language practices](https://bssw.io/items/inclusive-language-resources), engaging in [Inclusive Moment exercises](https://hpc-workforce-development-and-retention.github.io/hpc-wdr/jekyll/update/2023/04/08/inclusive-minute.html) as regular part of team meetings, using [inclusive design to improve user interfaces](https://uxdesign.cc/a-beginners-guide-to-inclusive-ux-design-b8dcc94f5068), using [CVD-friendly color combinations](https://www.tableau.com/blog/examining-data-viz-rules-dont-use-red-green-together) in documentation and presentations, [internationalization](https://www.tutorialspoint.com/run-a-qt-app-in-a-different-language) of documentation or interfaces, and supporting multiple language bindings (e.g. C/C++, Fortran and Python) to a key piece of infrastructure software.

To put things in perspective, it is worth considering just how much the scientific computing community already invests in inclusivity as it manifests in the software we develop and maintain.

The code that the scientific computing community has been developing has for decades exemplified all the best goals of inclusivity.
For example, our community values *interoperable* libraries so that, for example, an application can easily swap one solver library (e.g., PETSc) for another (e.g., HYPRE).
Software interoperability is a manifestation of inclusivity in the actual code we write.

We value computational kernels and tools that operate on single, double, quad and even mixed or arbitrary precision.
We also value both API (compile-time) and ABI (link-time) compatibility in successive or related versions of the same library. 
We also desire widely used libraries to support multiple different programming language interface bindings such as C, C++, Fortran, Python, or Java.
These are yet other manifestations of inclusivity in the actual code we write.

The whole goal of performance portability is to develop an HPC/CSE application *once* but have it run efficiently *everywhere* (e.g., CPUs, GPUs, co-processors, FPGAs, etc.).
Performance portability is an extremely challenging design goal that has required substantial effort and resources to achieve.
Performance portability and the effort we have invested in it is yet another example of how the goals of inclusivity manifest in the actual code we design and develop.

The truth is, it is quite obvious from the actual code we labor to produce that we are fully committed to inclusive practices and inclusivity.
A substantial level of effort in the design, implementation, and support of the software our HPC/CSE community develops and maintains is all about inclusivity for our software.
It only makes sense that we would be equally committed, if not more so, to inclusivity as well for the people developing and using this software.

<!--body end--->

### Author bios

Rinku Gupta has been a part of the high-performance scientific community for two decades and is a researcher in the field of high-performance fault tolerance, resiliency, middleware libraries and programming models. She is passionate about her work in the area of developer productivity and software sustainability; her current focus lies in partnering with the computational science community on these topics to design better scientific software.

Mark C. Miller is a computer scientist supporting the Strategic Deterrence (SD) program at LLNL since 1995. Among other things, he contributes to [VisIt](https://visit.llnl.gov), [Silo](https:silo.llnl.gov), [HDF5](https://www.hdfgroup.org/) and [Sustainable Research Pathways (SRP)](https://shinstitute.org/sustainable-research-pathways-2024-workshop/).

<!---
Publish: yes
Topics: inclusivity
Track: deep dive
--->
