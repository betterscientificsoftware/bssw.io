# Overcoming Complexity in Testing Multiphysics Coupling Software  

#### Contributed by: [Frédéric Simonis](https://github.com/fsimonis), [Gerasimos Chourdakis](https://github.com/MakisH), and [Benjamin Uekermann](https://github.com/uekerman)
#### Publication date: February 7, 2022

<!-- start of deck text -->
Testing complex software can easily get out of hand, especially when your product is a multiphysics coupling library.  Fortunately, we've found some strategies that have helped tame the nightmare. 
<!-- end of deck text -->

Testing is easy, right? Your code is probably already automatically tested to some extent, even if you always wanted to increase the coverage, granularity, or set up a more modern infrastructure. 

Well ... Testing starts to become challenging when one needs multiple software components to test even basic features of the code, and even more challenging when these components are MPI-parallel, written in different languages, and part of a larger simulation software ecosystem with a library at its core and several layers in between.

This article explores the some of the challenges we've faced in testing the preCICE coupling library and technical solutions we've used, which we believe would also be useful for testing other parallel C++ libraries with similar requirements.

## Maintaining research software

The [preCICE](https://precice.org/) project aims to provide an ecosystem of tools to assemble partitioned multiphysics simulations.
The core of this ecosystem is the open-source coupling library itself, which
aims to couple existing programs (solvers) capable of simulating parts of the complete physics involved in a simulation.
The coupling library is designed to be a highly flexible and scalable tool, which allows rapid prototyping of complex multiphysics scenarios.
A [vibrant community](https://precice.org/community.html) is already using preCICE on laptops, local clusters, and supercomputers.

As usual, flexibility comes at a cost, and in this case the cost is internal complexity.
A complex system is not _necessarily_ a problem, but it is prone to become one as soon as the fundamental know-how and the confidence in its correctness fade away.
This threat is especially apparent in rapidly changing environments such as academia.

We, the preCICE development team, faced exactly this situation four years ago and decided to tackle the issue before the project started to decay.
The departure of recent doctoral students led to knowledge gaps, and the lack of accessible testing directly impacted confidence in the correctness of the existing code.

Additionally, a growing user-base resulted in growing responsibility for support, as bugs effected an increasing number of users.
Software releases required in-person gatherings and extensive manual testing.
Bug fixes were possible only when the right know-how was present in a single room.
The result was stressful releases, leading to release anxiety and an overly conservative stance toward change.
To change this situation, the team needed to raise and keep confidence in the correctness of the code.

The solution sounded simple: migrate to a sustainable testing framework, make tests simple to run, setup a continuous integration system to prevent regressions, and establish development workflows prominently displaying the test status.
What started five years ago is an ongoing journey and nothing we had ever imagined.
In this article, we want to tell you where we are today, how we got there, and what we have learned on the way.

## The challenge

Testing the preCICE library has always been a challenge, mainly due to a combination of intrinsic complexities stemming from the nature of coupled simulations.
Individually, these special features do not sound daunting or unusual.
Handling all of them at the same time, however, is the real challenge.

First, preCICE follows a library-based approach, meaning that every solver links against the preCICE library and manages its own instance of preCICE; these instances require appropriate coordination.
Second, preCICE adheres to the parallelism of the solver.
While a solver using thread-level parallelization may still be seen as a single logical unit, things get complicated for process-based parallelizations such as MPI.
Multiple processes mean multiple instances, requiring additional coordination and hence internal communication.
Third, preCICE is used for partitioned simulations, meaning that at least two separate solver codes are involved in a simulation.
While these codes communicate via preCICE, they may still run in separate MPI communicators.
Finally, the preCICE project has been around for some years;
its code-base predates the C++11 Standard Template Library (STL), and portions followed outdated paradigms.
Efficiently modernizing such code requires a good test suite and confidence in the correctness of the code, which needed to be established first.

## Choosing a sustainable test system

Originally, preCICE used the testing functionality of the [Peano framework](https://gitlab.lrz.de/hpcsoftware/Peano/), which was part of a larger in-house utility library called tarch (technical architecture).
A copy of tarch was directly included in the source of preCICE. When the only developer of preCICE who also developed tarch left the team, the testing framework became an abandoned part of preCICE.
The tarch testing framework had fulfilled its duty and needed to be replaced with an actively maintained testing framework.

What features did we need?
We needed to write traditional unit tests for geometric functions, data mapping schemes and the like, none of which are a problem for existing testing frameworks.
We also needed to test functionality that relies on MPI communicators, such as distributed quasi-Newton acceleration methods or distributed data-mapping schemes using the PETSc library.
Therefore, we needed an MPI-aware testing framework, something that allows splitting and resizing a communicator, as well as output of meaningful information as it runs in parallel.

This is where we encountered our first hurdle.
We could not find a single MPI-aware C++ testing framework in the community;
thus, we had to customize an existing one.
The only constraint was support for a custom initialization method, which is mandatory as the framework needs to initialize MPI.
As we already had Boost as a dependency, we chose [Boost.Test](https://www.boost.org/doc/libs/release/libs/test/) for this task.

The initial testing strategy was as follows:
Unit tests that do not utilize a communicator ignore MPI altogether.
Higher-level (i.e., integration) tests may split and resize `MPI_COMM_WORLD` as needed and are responsible to cleanup afterwards.
As is often the case, simple solutions like this work, but sooner or later, they are challenged by unforeseen consequences. 

## Managing global resources

preCICE internally used a singleton style to manage global resources such as MPI or the logging system.
If a single test changes this global state and omits its cleanup, then this global state leaks into successive tests. 
Furthermore, failing parallel tests can lead to leftover entries in receive and send buffers, which leads to communication problems for subsequent tests.
Thus, all tests relying on global state implicitly depend on each one executed previously.
Thoroughly testing preCICE requires many fine-grained tests, leading to countless implicit dependencies.

After years of implementing tests for the majority of internal components, this cobweb of dependencies turned into a problem.
Inconsistent and complex setup and clean-up methods led to a copy-paste mentality, which was the perfect breeding ground for mistakes.
Some tests would succeed in isolation and fail as part of a test suite.
Some parallel tests would hang or fail due to receiving incorrect data from stale entries in receive buffers.
Debugging tests turned into a chore and often required experts in multiple components to find potential overarching issues.
While extensive testing improved the overall confidence in the correctness of code, it became a burden whenever things went wrong without obvious reasons.

## Unifying unit tests

We realized that we needed a uniform system that would allow us to define the _scenario_ of a test.
As an example scenario, let us consider a test using an MPI communicator with two ranks.
In this case, this uniform system would be responsible for checking if there are two ranks available, synchronizing all ranks to prevent interference between succeeding tests, restricting the communicator to two ranks, and exiting the test on all unused ranks.
During the test, the system should provide access to local information, such as the current rank, communicator size, and the communicator itself.
After the test completes, the system would have to revert all applied changes.

Translating the above into C++ can be done in small incremental steps, starting with the _context_.
The context is bound to the entire lifetime of a test, which can be represented using a context object.
Constructors and destructors then handle synchronization, initialization, and cleanup (following the concept of resource acquisition is initialization [RAII](https://en.cppreference.com/w/cpp/language/raii)):
```cpp
struct TestContext {
    TestContext(SCENARIO); // Synchronization and initialization
    ~TestContext();        // Cleanup
    bool valid() const;    // Is this rank used by the test?
    int rank, size;        // Local information
    MPI_COMM comm;         // Local communicator
};

BOOST_TEST(Feature) {
  // synchronize, initialize
  TestContext context(SCENARIO);
  // exit test if unused
  if (!context.valid()) return;
  
  BOOST_TEST(something);
  
  // implicit cleanup in ~TestContext() 
}
```

Next up is the description of a `SCENARIO`.
Its simplest form would be the number of ranks required for the test.
[User-defined literals in C++](https://en.cppreference.com/w/cpp/language/user_literal) allow us to create expressive constructs for this.
```cpp
struct Ranks { unsigned long long count; };
Ranks operator""_ranks(unsigned long long value) {
  return Ranks{value};
}
```
The example test mentioned at the beginning of this section, could then look like this:
```cpp
BOOST_TEST(ParallelFeature) {
  TestContext context(2_ranks);
  if (!context.valid()) return;
  
  BOOST_TEST(something);
}
```
A macro prevents needless repetition, potentially inconsistent names of the `context` object, and improves readability:
```cpp
#define PRECICE_TEST(...)           \
  TestContext context(__VA_ARGS__); \
  if (!context.valid()) return

BOOST_TEST(ParallelFeature) {
  PRECICE_TEST(2_ranks);
  
  BOOST_TEST(something);
}
```

As previously mentioned, some tests require to setup singleton-like components.
An example would be distributed data-mapping schemes implemented using PETSc.
To handle this circumstance, we define named requirements and let the test system handle the initialization order.
We use an `enum struct Require` to define requirements by name and then handle them by implementing a [variadic](https://en.cppreference.com/w/cpp/language/variadic_arguments) constructor for `TestContext`.
The `enum struct` requires the user to explicitly name of the enumeration, which improves readability.
This allows us to write expressive test scenarios by defining the requirement directly after the required number of ranks.
```cpp
enum struct Require { PETSc };

BOOST_TEST(ParallelPETScFeature) {
  // Test using 2 ranks and requiring PETSc to be setup.
  PRECICE_TEST(2_ranks, Require::PETSc);
  // test feature
}
```

At this point, we can write expressive unit tests using our new framework, which selects, initializes, and synchronizes all ranks required for the tests.
Furthermore, this system executes cleanup reliably at the end of the test.

## Unifying integration tests

Integration tests check features from the user perspective, relying primarily on the API of preCICE.
The main difference from unit tests is the partitioned nature of integration tests.
In practice, participants in the integration are started in isolation, connect to each other, and then communicate.
Hence, these participants require isolated communicators, and their identity needs to be available as local information within tests.
For example: a parallel participant called `Fluid` running on two ranks coupled to a serial participant called `Solid`.

Such scenarios should be easy to write and even easier to read; the closer to the written description, the better.
After some thought, the format we devised is very close to original test description.
Again, user-defined literals allow for an expressive solution.
```
PRECICE_TEST("Fluid"_on(2_ranks), "Solid"_on(1_rank));
             ^^^^^^^..............^^^^^^^............. Participant names
                    ^^^..................^^^.......... String-literal
                       ^.......^............^......^.. operator()
                        ^^^^^^^..............^^^^^^... Rank information
```

Defining the string-literal `"string"_on` allows us to transform the name of each participant into a custom type, which then provides an `operator()(Rank)` to add rank information.

```cpp
struct Participant {
    std::string name;
    Ranks ranks;
    Participant& operator()(Ranks r);
};

Participant operator""_on(const char *name, std::size_t) {
  return Participant{name, Ranks{0}};
}

Participant& Participant::operator()(Ranks r) {
    ranks = r;
    return *this;
}
```

These participants each require their own MPI communicator, which requires splitting the communicator during initialization of the test.
We implement this by computing the total number of ranks required, followed by a resize and finally a split.
This test system knows both the available MPI ranks as well as the complete requested setup allowing for early checks at run-time of common copy-paste mistakes, such as duplicated names or requesting too many ranks.
To simplify the implementation of integration tests, we turned common queries into methods of `TextContext`.
This approach is especially useful for simplifying the control-flow of distributed tests and integrating names and ranks directly into the code:
```cpp
BOOST_TEST(FSIWithParallelFluid) {
  PRECICE_TEST("Fluid"_on(2_ranks), "Solid"_on(1_rank));
  
  // Common setup
  SolverInterface precice(
      context.name, context.rank, context.size);
      
  if (context.isNamed("Fluid") {
    setupFluidMesh(precice, context);
  } else {
    setupSolidMesh(precice);
  }
  precice.initialize();
  
  while (precice.isCouplingOngoing()) {
    // Solver-specific behavior goes here
    if (context.isNamed("Fluid") {
      if(context.isRank(0)) {
        // context.rank == 0 context.size == 2
      } else {
        // context.rank == 1 context.size == 2
      }
    } else {
      // context.rank == 0 context.size == 1
    }
  }
  
  // Common cleanup
}
```

## Impact on usability and debuggability

This testing system has had a wide-ranging impact on the core library, which can be grouped into two key areas.

The first area is usability.
Tests are now far easier to write and most importantly easier to read.
Reduced complexity and improved consistency are not the only reasons though.
The codified scenarios are now easy to understand, which makes testing more approachable and generally less daunting for both seasoned developers as well as less involved contributors.
Beyond the scenario specification, the control flow becomes more natural as it directly incorporates names of participants and their ranks.
All of this is crucial for bringing new developers quickly up to speed.

The second area of impact is debuggability, which has improved dramatically.
Synchronization points at the beginning of the tests keep all ranks in a constrained state, which reduces interleaved output for better readability.
The consistent setup now guarantees a well-defined global state, which does not leak between tests anymore.
The remaining issue is leftover entries in receive and send buffers, which are now possible only if a test silently fails.

## Outlook

While testing the preCICE library has converged to a uniform system, an approach for testing the whole preCICE ecosystem effectively is still unclear.
The additional software layers and dependencies make this a far more complex matter.

While preCICE is a library written in C++, many solvers are not.
These solvers need a translation layer from their language to the preCICE C++ API.
Such _language bindings_ are required for languages like C, Fortran, Python, Julia, as well as systems like Matlab.
Going a step further, solver _adapters_ separate the coupling physics that the user wants to define, from the calls to preCICE.
What are efficient ways of testing such translation layers and adapters for correctness and compatibility, without relying on the pillars they bridge?

In the next layer, complete coupled simulations that rely on multiple components from the preCICE ecosystem require testing, both for correctness and performance regressions.
We test common combinations using validation cases, which often require various solvers, potentially written in various languages.
Testing this entire ecosystem of layers and dependencies between various software packages are what we call _system tests_.
After many development hours and multiple prototypes, this testing system has slowly begun to converge to a mature state.
But, the question still remains: What are efficient ways to test the complete ecosystem in a reasonable time-frame?

These are all open questions that we would like to defer to a future article.
Thankfully, the increasing stability of the core library frees up development time that can be used to tackle these issues and write about the journey of solving them.

## Additional information

If you are interested in more details, please check out section 5 of the new [preCICE reference paper](https://arxiv.org/abs/2109.14470).
You may also be interested in the [preCICE Workshop 2022 (Feb 21-25)](https://precice.org/precice-workshop-2022.html) for a hands-on experience with preCICE. 

## Author bios

Frédéric Simonis is a researcher at the Technical University of Munich and core developer of preCICE. Following his interests, he has progressed from computer graphics and main-memory database systems to HPC, where he joined the preCICE project. His primary research goal is the extension of preCICE to adaptive meshes to support adaptive solvers as well as run-time re-meshing. He currently takes the leading role in maintenance, code modernization and release management of the preCICE library.

Gerasimos Chourdakis is a doctoral candidate at the Technical University of Munich, working on transforming the preCICE project from an "as-is" 
coupling library into a "batteries included" multiphysics ecosystem. 
With this perspective, he takes the leading role in organizing the development and operations of the "flesh" of the preCICE ecosystem, including adapters for various solvers, tutorial cases, documentation, website, and testing, shaping these components for the preCICE community to grow upon. He is also researching methods for geometric multiscale coupling and enjoys teaching topics related to research software engineering.

Benjamin Uekermann is a junior professor in the CoE SimTech at the University of Stuttgart. He originally studied applied mathematics, followed by a PhD in computer science at the Technical University of Munich. As a postdoc, he was the scientific program manager of the German Priority Program for Exascale Computing Software (SPPEXA). He moreover held a Marie-Sklodowska-Curie postdoc fellowship at Eindhoven University of Technology. His research focuses on the development of numerical methods and algorithms for multiphysics, multiscale simulations. Since 2012, he has been one of the main developers of preCICE and is currently leading its development team.

<!---
Publish: yes
Track: deep dive
Pinned: no
Topics: software interoperability, testing, development tools
--->
