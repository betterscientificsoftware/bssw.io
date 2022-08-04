# Bright Spots: Team Experiences Implementing Continuous Integration

**Hero Image:**

<img src='../../images/Blog_Brightspot.png' />

#### Contributed by [David M. Rogers](https://github.com/frobnitzem)

#### Publication date: August 12, 2022

*This is the first in an occasional series of Bright Spots blog articles, highlighting success stories of Exascale Computing Project software teams implementing and benefitting from software development best practices.  If you'd like to contribute to a future Bright Spot article, please contact the [BSSw Editorial Board](mailto:bssw-editorial@lists.mcs.anl.gov?subject=Bright Spots).*

[Continuous Integration](https://bssw.io/items/what-is-continuous-integration-testing) is an enabling technology that allows code development teams to insert testing directly into their development workflow[2] .  Although there are many advantages to CI, including more stable working code bases, faster test feedback with less distraction, and greater support for community contributions, there are also some pitfalls[3] , like initial adoption and support burden, disruptive changes to team processes, and a potentially disorienting array of competing, overlapping, new technologies.

How do these trade-offs influence the difficulty of adopting and maintaining CI automation?  What’s the simplest way to get started?  What kinds of team organizational and communication challenges can be expected?

To understand what has worked best, this article interviews three development teams across the DOE Exascale Computing Project that have adopted CI: ExaSMR, Visit, and ZFP.  The ExaSMR project develops simulations of small modular reactors that provide the engineering community with highly detailed, benchmark datasets.  The Visit project is a highly scalable, turnkey application for data analysis, visualization, and movie making.  ZFP is a compact library for lossy compression of multi-dimensional arrays of integer and floating-point data with controllable rate, precision and accuracy.

Each of these teams has a unique story about how CI fits into their overall project goals, the evolution of their pipelines, and of the challenges they faced along the way.  The adopters of CI have all described its value to be “obvious” in retrospect because of the numerous occasions where either testing or pull-request reviews have caught errors that would have gone undetected otherwise.  ZFP put significant effort into developing tests, resulting in over 5,000 unit tests with nearly full code coverage.  VisIt’s extensive nightly regression testing combined with a permissive policy with respect to breaking the mainline of development meant that the project’s initial CI testing could be rather modest and fit within time limits of freely available services. The project has seen a greater impact from formal reviews of pull-requests.  ExaSMR noted that having CI in place sets the expectation that new contributions come with corresponding tests.  This results in better quality code contributions from the community that are less stressful for the maintainers to review.

### ExaSMR

ExaSMR writes about their CI experience with the [OpenMC](https://github.com/openmc-dev/openmc) package.  This package simulates Monte Carlo particle transport for use within multiphysics, fluid dynamics models.  It is a C++ library built on top of 3 geometry and math libraries (DAMC, GSL, xtensor), and 3 I/O libraries (HDF5, pugixml, {fmt} a.k.a. fmtlib), and building both an executable and a modular Python ctypes interface.  The project was first hosted on GitHub in 2012, and Travis CI was first added in February of 2015.  They used CI to install system packages and run its Python test harness.  In December, 2020, the project switched to GitHub actions, which supported the automation features the project had adopted by that time: a matrix of compilation and test options (turning on/off MPI/OpenMP/compiler optimizations), coveralls.io code-coverage integration, and automated creation of docker images for releases.

Paul Romano noted it was surprisingly easy for the team to get a first useful CI pipeline working with Travis CI. Switching over the GitHub Actions was also relatively straightforward.

One of the unique aspects of the project is that the Monte Carlo method, being stochastic in nature, results in the possibility of otherwise identical simulations diverging from one another on two systems with ever-so-slightly different characteristics; for example, a different implementation of standard library math functions might result in completely different answers (within uncertainty) if the simulations are run long enough.

This has sometimes made it difficult to reproduce CI failures locally.  Romano has seen quite a few circumstances where developers report “it works for me but always fails on Travis/GitHub Actions”.  This is especially prone to occur when someone makes a change that *is* expected to change reference answers (against which the tests check).  Then, updating the reference results requires some sensitivity to the platform differences between development and CI environments to get just right.

Another hidden challenge the team noticed is keeping up with changes in dependencies. Every so often, a library will change their API, deprecate something, or otherwise change some behavior that forces us to deal with it right away because not doing so means our tests no longer pass. ExaSMR tries to stay on top of this by *not* pinning dependencies to specific versions.  The consequence, however, is that issues pop up periodically and divert attention from other areas.

### Visit

The biggest testing focus is on the (C++) source code for [Visit](https://github.com/visit-dav/visit)’s executable metadata-server, engine, viewer and controller.  It has dozens of external dependencies for geometry, graphics, file formats, and I/O.  Visit’s code base was hosted on NERSC’s Subversion servers until early 2019 when it was [migrated](https://bssw.io/blog_posts/continuous-technology-refreshment-an-introduction-using-recent-tech-refresh-experiences-on-visit) to git and GitHub. [Cyrus Harrison](https://github.com/cyrush) first added CI to the codebase around March 2019. Prior to that, only [nightly testing](https://visit-dav.github.io/visit-website/dashboard/) was in use. Adding CI testing was complicated because of the graphical nature of the code and the large number of dependencies.  He opted to use docker images to provide pre-built dependency binaries, combined with a set of scripts that allowed running on both Travis and Circle-CI.  The process to develop the scripts took weeks of trial and error.  The team went on to add more features and switch to Azure pipelines in Aug. 2020.  The CI tests run using a vanilla RedHat Linux base image, but the release process also builds images for Centos, Fedora, Debian and Ubuntu.

Mark Miller observed that “Costs and time limits were some of the key factors affecting our CI provider choice.”  One of the largest continuing challenges faced by the team is the compute time required to build and run the tests.  “Dependencies aside, it takes a 2017, 4-core MacBook-Pro about 15 mins to build VisIt using `make -j 8` (oversubscription by 2x). It takes another 90+ mins to build dependencies. The entire nightly test suite itself can take 2-4 hours.” Even though Azure Pipelines provides unlimited run times for open-source projects, there is still a practical limit on what can be effectively tested in CI.

This has led VisIt’s CI to utilize mainly the command-line controller.  As a Python interface to a single executable, these can exercise different code-paths for things like plots, database readers, operators, rendering modalities, etc., without requiring a complete rebuild of VisIt.  They also use stand-alone tests of some key classes.  Substantial unit testing, however, would require refactoring the core of VisIt to support that modality of build and execution.

Miller notes there’s always a trade-off between testing better vs improving the product itself.  There’s a laundry list of things that the project would like to have more testing for, like GUI events, multiple client/server modalities, numerical corner cases like handling of NaN and Inf floating-point exceptions, and more comprehensive doc-tests.  Rather than trying to tackle all these directly, the project developers have found that regular discussions comparing all these potential improvements have made them extremely productive.  Discussing ideas at length allows them to document ideas via GitHub issues, understand tradeoffs, and prioritize their work.

Miller also had a lot of advice to teams developing an initial process for CI.  As a guiding principle, he advocates for starting small, and aiming for the ultimate goal of moving a subset of tests into CI -- ones that are responsive, informative, and cover areas that the team agree should be continuously checked.  Those tests should use the code in the way it’s intended for users to run, minimizing surprises down the road.

Visit’s own development path was heavily influenced by the prior experience of its developers with CI, along with a healthy dose of combing through documentation (see this [blog article](https://bssw.io/blog_posts/continuous-technology-refreshment-an-introduction-using-recent-tech-refresh-experiences-on-visit)).  Perhaps uniquely, they use CI primarily as a “smoke test” for compilation, dependencies, and their release process, then place a majority of their software quality focus on reviewing pull requests and running nightly tests on local resources.  Those nightly tests generate, then check 3500+ images and 2000+ numbers/textual results.  Although they require bit-for-bit accuracy, they have a rolling error-resolution process.

### ZFP

ZFP’s [main repository](https://github.com/LLNL/zfp/) contains a C++ library and its C, Fortran, and Python interfaces.  A separate repository, [zfpy-wheels](https://github.com/LLNL/zfpy-wheels), builds python-wheels binary distributions.  ZFP was first hosted on GitHub in March 2016.  In early 2017, it migrated from a simple Makefile to CMake and added CI using Travis and AppVeyor.  That initial investment was somewhat difficult because documentation on google test, mocha, and CI services was in an early state and relevant guides were hard to find.  Since then, the team has steadily expanded its test coverage to 95% with over 5,000 unit tests.  Internally, this effort was made possible by hiring a full-time developer to focus on ZFP’s testing and CI pipeline.

As a library for lossy array compression, most of ZFP’s tests make use of either checksums or fuzzy matching of the compressed and the compressed-then-uncompressed data.  The former demand bit-for-bit identical results, while the latter can account for cases where floating point computations may vary across compilers, CPUs, etc.  By adopting this paradigm, it becomes simple to create a massive array of tests over compression options, 1, 2, 3, and 3D arrays of 32/64 bit integer and floating point on a slew of compilers and OSs.

Testing is not without its challenges, however.  As the codebase evolves, the “golden” standard checksums sometimes need to be updated.  That requires careful manual inspection of results across systems.  Also, the CI tests are valuable for debugging issues, but are hard to reproduce and interact with.  When things fail without leaving good diagnostic and error messages, one needs to make a small change and re-run the entire pipeline!  Of course, this makes it hard to quickly track down the root cause.  The ZFP team encourages adopters of CI to expect to use a lot of trial and error to get oriented.

With CI, the need for good diagnostics and logs extends beyond your own codebase.  Like other teams, ZFP noted that sometimes intermittent issues come from inside the CI process’s network, software and hardware stack that later disappear after re-running the test a few times.  Issues like this can look like logs that don’t come back to [CDash](https://open.cdash.org/index.php?project=zfp), or log names and formats that don’t directly map to actual jobs on a given CI service.  This demands extra work on the part of the development team to gain experience diagnosing errors, while avoiding wild goose chases that soak up time and effort.  Many of these issues are opportunities for making systems better and building collaborations with GitLab CI experts, facility teams, and upstream developers.

The ZFP project would also like to increase performance testing, coverage of shipped executable programs, stay up to date with compiler releases and platform libraries, and have a CI system that skips over tests that are provably “still working”.

Like Visit, ZFP doesn’t require 100% of its tests to pass before merging unless the merge is going into the main development branch.  This allows the main branch to serve as a base for releases, but lets the feature branches be a place to work collaboratively on issues.

### Summary

As a technology, CI has evolved and developed a lot over the past several years.  Mature systems, connected to ubiquitous version control platforms like GitHub, GitLab, and Bitbucket, offer many examples, tutorials, and documentation that make the entry barrier low.  The projects we interviewed talked about their specific adaptations for scientific and numerical software.  All three projects mentioned comparing with “golden-results” from full program runs, as well as the unique mindset needed to develop and maintain unit tests.  Testing is a mode and scope of work motivated by adding armor to your codebase. The most cited benefit was identifying potential bugs early, which increased the project’s ability to collaborate within the open source community.

All three projects also noted some drawbacks to CI: maintaining tests requires time and effort, along with trial-and-error with new tools, and long-running tests can be an issue.  Teams noted that random failures (due to network, etc.) were initially annoying, but infrequent enough to safely ignore, and usually resolved by a restart.  Long-running tests can stress CI resources, with the mixed benefit/drawback of needing more careful attention to how tests are designed.  Other than adding that development work, the teams didn’t notice excessively disruptive changes to team process.

Aside from CI, there’s a lot to be learned from studying code construction choices across open-source projects.  For example, the three projects here all use a different strategy to create Python interfaces to their codes.  ExaSMR uses Python’s ctypes to wrap the C API, then installs those wrappers in site-packages so they can be found by setting PYTHONPATH.  VisIt has an integrated Python environment.  ZFP’s Python interface is built using [Cython’s support for wrapping C++ classes]([https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html#using-c-in-cython](https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html#using-c-in-cython)), with a build and install process managed using the [scikit-build]([http://www.scikit-build.org](http://www.scikit-build.org)) plugin to CMake.

Overall, CI adds value by providing more stable working code bases, test feedback without developer intervention, and greater support for community contributions.  As we watch the evolution of CI technologies, there are several features our teams are looking for.  The ability to freeze the state of tests would both reduce redundant tests after small changes, and also allow interaction with these states.  Greater availability of testing hardware and runners would also boost the usefulness of this technology.

### Acknowledgements

We thank the VisIt team members: A, B, C; ExaSMR members: X, Y, Z, …; and .

### NOTES (TO BE DELETED?)

The team says / the project policy is… (organization vs. ).

-- mostly off-topic stuff I cut from the manuscript --

Forward-looking statements about benefits and potential of CI pipelines - ecosystem delivery (use cases across projects, release notifications / security alerts), greater automation of integration tests, more focused test selection, cross-project science cases, connecting networks of developers, integrating with documentation

Unique story of ExaSMR, Visit, and ZFP

value: numerous occasions where either testing or pull-request reviews have caught errors that would have gone undetected otherwise, code quality improvements

### Author bios

<!---
Publish: yes
Pinned: no
Topics: continuous integration testing
--->
