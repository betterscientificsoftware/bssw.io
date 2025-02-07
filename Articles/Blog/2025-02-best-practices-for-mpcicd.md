# Best Practices for Multi-Project Continuous Integration and Deployment

#### Contributed by [Ryan M. Richard](https://github.com/ryanmrichard)

#### Publication data: February 7, 2025

<!-- begin deck -->
Implementing and managing continuous integration/deployment for multiple
projects has its own challenges. Emerging best practices can help.
<!-- end deck -->

This article is cross published with the Multi-Project DevOps
[website](https://multiprojectdevops.github.io/bssw_summary/). 

This article summarizes the initial efforts of the [Multi-Project DevOps
organization](https://github.com/MultiprojectDevOps) to establish best practices
for implementing and maintaining continuous integration (CI) / 
continuous deployment (CD) in a multi-project (MP) software ecosystem.

## CI/CD vs MPCI/CD

Very briefly, CI is a software development practice where contributions to a
software package are merged into a centralized repository as they are ready. 
This contrasts with older philosophies such as the
["waterfall model"](https://www.geeksforgeeks.org/waterfall-model/) where 
changes are only merged at select times (e.g., features are merged during the 
*Development* stage and bug-fixes are merged during *Testing*). CD refers to the
practice of releasing updates to a software package when they are ready. CD 
differs from other release strategies such as timed releases, or waterfall when
releases happen during the *Deployment* stage.

Because of their asynchronous nature, CI and CD almost mandate the use of 
automation to ensure changes do not break the system and that steps are not
skipped. Automation is accomplished by means of pipelines. With CI and CD each 
automated, it is natural to combine the pipelines so that when a CI pipeline 
successfully completes, a CD pipeline automatically starts. The result is a
unification of CI and CD into a single practice, CI/CD. 

CI/CD is usually described in the context of a single software repository. 
With a push to make scientific software more modular, there is a propensity
for developers to create many smaller software repositories instead of one large
monolithic repository. **MPCI/CD is the practice of practicing CI/CD across many 
software repositories.**

## MPCI/CD

As just introduced MPCI/CD  generalizes the practice of CI/CD to multiple 
repositories. The key realization of MPCI/CD is that considering the CI/CD
needs of each project together imparts advantages over considering the CI/CD
needs separately. As an example, all projects written in a compiled language
will require compilation as part of their CI/CD pipeline. Furthermore, this 
process is often similar across the projects. While it may be tempting to 
duplicate the compilation logic in each repository, this is a known 
["code smell"](https://tinyurl.com/465v56wz).

Over the last year we have held a few workshops designed to understand what
best practices the community follows in the context of MPCI/CD. From these
workshops several themes have emerged:

- Treat infrastructure as code.
- Dependencies.
- Avoiding code duplication.
- Creation of reusable pipeline components.
- Security.

The remainder of this article provides a high-level overview of each of these
themes. More information on best practices can be found on the Multi-Project
DevOps [website](https://multiprojectdevops.github.io/best_practices/).

### Treat Infrastructure as Code (IaC)

IaC refers to the practice of preferring configuration scripts/files to setup
a computing environment, as opposed to graphical user interfaces or other
mechanisms which are harder to automate. In the context of MPCI/CD IaC is
important because:

- Easier to scale CI/CD pipelines up/down, e.g., to massively parallel tests.
- Reliability. You know exactly what environment you will run in.
- Reproducibility. Others can recreate the environment.

Mechanisms for IaC differ depending on the CI/CD service. For GitHub actions
this is mainly controlled by which base image you use. For GitLab this is
controlled by the runner you pick.

### Dependencies

In the context of MPCI/CD *dependencies* include not just the software's
dependencies, but also the dependencies of the CI/CD pipelines (e.g., the
reusable components). Dependencies are a natural part of any software system and
also the source of many DevOps problems. The best practices in this theme aim
to make usage of dependencies in CI/CD pipelines as painless as possible. To
that end general best practices include:

- Use dependency management software to the extent possible.
- Pin versions.
- Institute nightly builds with the newest releases of dependencies.

Dependency management is a complicated issue best managed by specialized
software. Choices for this software range from operating system wide (e.g., 
Aptitude for Ubuntu and Homebrew for MacOS) to language specific (e.g., PyPI
for Python and Conan for C++). In the context of MPCI/CD it does not matter what
dependency management software is used. What matters is that such software is
used instead of trying to directly manage dependencies in the CI/CD pipelines,
i.e., the pipeline should be implemented in terms of the dependency management
software.  

CI/CD pipelines will need to pull dependencies automatically, frequently, and 
asynchronously. Pinning versions ensures that pipelines always use the same
dependency version, thus avoiding hard to debug problems caused by grabbing 
different versions. Related is the idea of instituting nightly builds with
bleeding edge dependencies. The goal of such builds is to preemptively know when
upstream changes are breaking. This is particularly important in modular
ecosystems where downstream developers are creating plugins or apps. In this
case, downstream developers want to know when changes to the framework break
compatibility. Even if the upstream developers adhere to semantic versioning,
it is unlikely that they will backport every new feature to earlier versions.
Meaning, even pinning dependency versions will not be sufficient if downstream 
developers want to use the new features and nightly builds help developers
plan for such upgrades.

### Avoiding Code Duplication

*Don't Repeat Yourself*, or the DRY principle, is a cornerstone of software
development. In fact, our initial foray into MPCI/CD emerged from wanting our
CI/CD infrastructure to obey this principle. In MPCI/CD applying DRY can be a
bit of a balancing act. This is because CI/CD is boilerplate heavy and the
threshold for what constitutes "repeating oneself" can be quite high. For 
example, calling a GitHub action requires specifying: the name of the action, 
the  options for the action, and the secrets for the option. Since this 
information must be specified in a configuration file the number of lines scales 
with the number of options and secrets. In some cases, the action may simply 
wrap a single command (quintessential examples are actions which install 
dependencies), meaning factoring out the command may actually require more lines
of code in the pipeline file than it replaces!

When DRY is used to factor out a large block of duplicated code, the benefits
are obvious: easier to read code and a single source of truth for the code block
across all pipelines. For smaller units of duplicated code, DRY still leads to
a single source of truth, but it may actually come at the cost of obfuscating
the code. Thus when to apply DRY is a judgement call for the developer. 
Generally speaking, we recommend factoring out duplicate code, regardless of 
size, if:

- The block of code contains details likely to be used by another pipeline, 
  e.g., lists of dependencies, dependency versions, or deployment endpoints.
- The block of code is time-consuming, e.g., installing dependencies may be a
  succinct call, but may require a lot of run time. If the call is factored
  out it becomes easier to cache the results to reduce time.
- The code block generates an artifact that will persist after the CI/CD
  pipeline is run. Similar to caching, managing artifacts is easier if their 
  generation is factored out.

The exact mechanism for factoring out CI/CD pipeline components will vary
among CI/CD systems. As a baseline, most systems allow you to call external
scripts. GitHub additionally provides several additional 
[mechanisms](https://tinyurl.com/88tjyjnj) including actions, composite
actions, and reusable workflows. Similarly, GitLab provides 
[components](https://docs.gitlab.com/ee/ci/components/).

### Creation of Reusable Pipeline Components

The last theme called for factoring out duplicate CI/CD code blocks into
components. In practice, many of those components will be heavily tied to
the workflows the organization has opted for. However, some components may
have broader appeal and thus have reuse potential. Reusable components should be 
developed as full-fledged software projects.

As an example, when developing modular software, there is a tendency to adopt
plugin architectures. In such architectures the main project, *the framework*, 
is designed to be extendable by users. To extend the framework users write 
*plugins*, downstream libraries meant to be consumed by the framework. Both
framework and plugin developers need to ensure ecosystem compatibility as part
of their CI/CD pipeline and it thus makes sense to create reusable CI/CD
components that can be used by both the framework and plugin developers. Other
examples include when the main project is a tool meant to be used during a
CI/CD pipeline (e.g., documentation generator), or when a project is not
available via package managers (then a reusable CI/CD component makes it
easier for downstream dependencies to include it in their CI/CD pipelines).

The best practices for building reusable pipeline components are the same as
any other software product and at a high-level include:

- Thoughtfully designed and stable interfaces.
- Documentation.
- Testing (yes that means CI/CD for your CI/CD component).
- Versioning.

The key insight is a practice we term *Code as Code* (CaC). For whatever reason, 
developers of scientific software have a tendency to only apply software
engineering best practices to the main software project and not the utilities
designed to support it. CaC is a reminder that utilities are also software.
This realization is particularly important when those utilities are reused
across projects. In which case they should be developed following best 
practices.

### Security

We are not security experts and the content of this subsection is meant to make
the reader cognizant that all CI/CD has security concerns and that reuse of 
CI/CD components can exacerbate these concerns. For example, if you self host 
CI/CD runners then you should note that the pipelines will physically run on 
your system. This means that maliciously written pipeline components can
conceivably access unintended parts of your system.  Even if you only run on a 
CI/CD provider's hardware, the fact that pipelines often have elevated 
permissions means that the pipeline may do potentially destructive actions 
(e.g., deleting files, locking you out of websites, introducing malware into the
code). If you reuse components you may potentially spread infections.

Generally speaking best practices related to security in a MPCI/CD setting
include:

- Only use trusted components.
- Think carefully about permissions.
- Isolate steps which have elevated permissions.

If security is a concern for you, then note that these practices alone are not 
sufficient to protect you from harm. You should include actual cyber security
experts in your CI/CD development and trust their wisdom/guidance.

## Conclusion

The Multi-Project DevOps organization is excited to share with the BSSW.io
community the results of Dr. Ryan Richard's 2024 BSSw Fellowship. It is our
hope that others who are interested in MPCI/CD will consider joining the
Multi-Project CI/CD organization and helping continue to add content. We intend
to for the Multi-Project CI/CD organization to continue, but note that content
additions may be slower as priorities shift. Nonetheless, we think that the
MPCI/CD best practices described here should provide a foundation for others
interested in improving how they manage CI/CD pipelines across multiple 
projects.

## Acknowledgements

This work was supported by the Better Scientific Software Fellowship Program, a
collaborative effort of the U.S. Department of Energy (DOE), Office of Advanced
Scientific Research via ANL under Contract DE-AC02-06CH11357 and the National
Nuclear Security Administration Advanced Simulation and Computing Program via
LLNL under Contract DE-AC52-07NA27344; and by the National Science Foundation
(NSF) via SHI under Grant No. 2327079.

Any opinions, findings, and conclusions or recommendations expressed in this
material are those of the author(s) and do not necessarily reflect the views of
the DOE or NSF.

## Author bio

Ryan M. Richard is a research software engineer in the Chemistry and Biological
Sciences Division at Ames National Laboratory. Ryan is also a 2024 Better 
Scientific Software Fellow. He is the lead software architect and developer of 
the NWChemEx ecosystem, a series of plugins focused on high-performance
quantum chemistry. His research interests include high-performance computing,
software engineering, and reduced scaling many-body methods. He earned his
Ph.D. in chemistry from The Ohio State University and his B.S. in chemistry
from Cleveland State University.

<!---
Publish: Yes
Track: deep dive
Topics: continuous integration testing
--->