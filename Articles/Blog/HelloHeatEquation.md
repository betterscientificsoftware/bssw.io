# The Heat Equation is the "Hello World" of Scientific Computing

#### Contributed by [Heather M. Switzer](https://github.com/heatherms27 "Heather Switzer GitHub Profile") and [Elsa Gonsiorowski](https://github.com/gonsie "Elsa Gonsiorowski GitHub Profile")

"Hello World!" is a prototypical program that is universally used by programmers to illustrate the basic syntax and implementation difficulty of a programming language (see several [Hello World implementations at WikiBooks](https://en.wikibooks.org/wiki/Computer_Programming/Hello_world)). In scientific computing, software can be written in any number on languages and must use various programming models or math libraries to achieve high performance for any particular problem. The Heat Equation, a well known partial differential equation (PDE), is the perfect formula to demonstrate a "Hello World!" comparison for programming options.

## What is the Heat Equation?
The Heat Equation, also known as the Diffusion Equation, was developed by Joseph Fourier in 1822. Primarily used in the fields of Mathematics and Physics, the equation shows how heat (or something similar) changes over time in a solid medium. While there are many adaptations for different dimensions and scenerios, new programmers are often first introduced to the 1-dimensional version of the Heat Equation as a tutorial problem.

The following description is adapted from [a Trinity University lecture](http://ramanujan.math.trinity.edu/rdaileda/teach/s14/m3357/lectures/lecture_2_25_slides.pdf "One-Dimensional Heat Equation").

Suppose you have a thin metal rod along the x-axis starting at position 0 and ending at position _L_. The goal is to model the temperature distribution throughout the rod at a given time, with the following (ideal) assumptions:

* An initial temperature distribution is given
* Boundary conditions (established tempuratures at each end of the rod) are known
* Heat only moves horizontally through the bar
* There are no external heating/cooling sources

<div style="text-align:center"><img width="75%" src="https://github.com/betterscientificsoftware/images/blob/master/Blog_0719_HeatEqnBar.png" /></div>

To model the temperature distribution of the rod, we can use the 1-dimensional Heat Equation given by the formula:

_&part;u / &part;t = &alpha;&nabla; &sup2;u_

Where:
* _u_ = Temperature at a position, _x_
* _t_ = time
* _&alpha;_  = thermal diffusity of the material
* _&nabla;_ = The LaPlace operator

### Assumptions and Discretization
To make the problem more approachable, we make some simplifying assumptions:
* _&alpha;_ is constant
* The heat/cooling source only comes from initial/boundary conditions
* Only Cartesian coordinates in 1 dimension are used

Since the heat equation takes the form of a PDE over a continuous space, most programs create a discretization of the formula over a finite set of sampling points.

First, we approximate the derivative _&part;u / &part;t_, to be

_&part;u / &part;t_ &vert; _<sub>t<sub>k+1</sub></sub> &asymp;_ (_u_<sup>_k_+1</sup><sub>_i_</sub> - _u_<sup>_k_</sup><sub>_i_</sub>) / _&Delta;t_

Then, we approximate _&alpha;&nabla; &sup2;u_ to be

_&alpha;&nabla; &sup2;u_ &vert; _<sub>x<sub>i</sub></sub> &asymp;_ _&alpha;_ (_u_<sup>_k_</sup><sub>_i_-1</sub> - 2 _u_<sup>_k_</sup><sub>_i_</sub> + _u_<sup>_k_</sup><sub>_i_+1</sub>) / _&Delta;x&sup2;_

By setting these equations equal to each other, we can find the temperature at time _k+1_ at spot _i_ using the discretized formula:

_u_<sup>_k_+1</sup><sub>_i_</sub> = _ru_<sup>_k_</sup><sub>_i_+1</sub> + (1 - 2 _r_)_u_<sup>_k_</sup><sub>_i_</sub> + _ru_<sup>_k_</sup><sub>_i_-1</sub>

(More information about the [full discretization process](https://xsdk-project.github.io/ATPESC2018HandsOnLessons/lessons/hand_coded_heat/ "Hand-Coded Heat") is available.)

Where _r = &alpha;_ &Delta;_t&sup2; /_ &Delta;_x&sup2;_. This discretization is referred to as the Forward-Time, Central-Space (FTCS) scheme which is considered numerically stable as long as _r_ is less than or equal to 0.5.

### Algorithm

After the continuous formula is discretized into a programmable problem we can define our variables and calculate each iteration of the temperature distribution algorithm. Before each stage, we first need to check that _r = &alpha; * &part;t / (&part;x&sup2;)_ is greater than _0.5_ to verify it is numerically stable.

Once _r_ has been verified, we can cycle through the non-boundary locations of the mesh and update it according to the discretization _u_<sup>_k_+1</sup><sub>_i_</sub> = _ru_<sup>_k_</sup><sub>_i_+1</sub> + (1 - 2 _r_)_u_<sup>_k_</sup><sub>_i_</sub> + _ru_<sup>_k_</sup><sub>_i_-1</sub>, ensuring that the boundary conditions stay constant at each time iteration.

After this process has repeated some specified number of times, we can return the final distribution of our mesh.

## Why the Heat Equation?
PDEs are widely used among the different sciences to model various phenomena such as electromagnetism, fluid mechanics, and heat transfers. While PDEs extend across multiple fields, they can still be quite tricky to work with because unlike ordinary differential equations, they are comprised of derivatives of more than just a single variable. A single example of a PDE is the Heat Equation, which is used calculate the distribution of heat on a region over time. While here we just focus on the 1-dimensional version of the Heat Equation, it can actually take a multitude of forms including the [Fourier](https://fenix.tecnico.ulisboa.pt/downloadFile/3779571609326/transp3.pdf "Fourier Equation"), [LaPlace](https://www.britannica.com/science/Laplaces-equation "LaPlace's Equation") (also known as steady-state), [2D](http://ramanujan.math.trinity.edu/rdaileda/teach/s12/m3357/lectures/lecture_3_6_short.pdf "2D Heat Equation"), and [3D](https://ocw.mit.edu/courses/mathematics/18-303-linear-partial-differential-equations-fall-2006/lecture-notes/pde3d.pdf "3D Heat Equation") heat equations.

As a consequence of the Heat Equation being so expansive and well-known, it is commonly used as an introductory example to new users of scientific software. This problem is also very easy for users to visualize, which can help them understand how different algorithms approach the solution. It allows users to become familiar with the structure and syntax of a particular programming language, parallel paradigm, or mathematical library. Because this tutorial exercise is so common, several implementations exist that are able to be referenced with just a quick web search.

## Implementations
Similar to "Hello World!" programs, various implementations of the heat equation can demonstrate syntactic features of a programming language. However, a sequential implementation demonstrates little more than for-loop syntax. Scientific software demands parallel programming models and libraries. Thus, we can demonstrate some interesting implementations.

### Variable Definition
Throughout these implementations, we use the following parameters:
```
n     = Number of temperature samples        # Integer
uk1   = New temperatures across x-axis       # Array of Doubles
uk0   = Old temperatures across x-axis       # Array of Doubles
alpha = Thermal Diffusity                    # Double
dx    = Spacing in space                     # Double
dt    = Spacing in time                      # Double
bc0   = Beginning boundary condition (x = 0) # Double
bc1   = End boundary condition (x = L_x)     # Double
```

From here we can build a series of implementations.

### Sequential Implementation (C)
We begin with the most basic implementation. This demonstrates little beyond the syntax of a for-loop.
```c
bool update_solution_ftcs(int n, double *uk1, const double *uk0,
double alpha, double dx, double dt, double bc0, double bc1){
    double r = alpha * dt / (dx * dx);

    // Sanity check for stability
    if (r > 0.5) return false;

    //FTCS update algorithm
    for(int i = 1; i < n-1; ++i)
        uk1[i] = r*uk0[i+1] + (1-2*r)*uk0[i] + r*uk0[i-1];

    // Enforce boundary conditions
    uk1[0] = bc0;
    uk1[n-1] = bc1;

    return true;
}
```

### Programming Model Example: OpenMP (C)
OpenMP is a portable way to add parallelism to a program. The [OpenMP Heat Equation](https://github.com/betterscientificsoftware/hello-heat-equation/blob/master/Parallel1DHeat.md "Parallel 1D Heat") demonstrates the use of `#pragma` syntax. We see that this implementation is a 2-line change from the base implementation.

### Library Example: MFEM (C++)
Scientific software programmers are able to take advantage of numerical libraries instead of hand-coding implementations, which can optimize performance and allow access to the additional features. Most of these implementations have multiple steps that are outlined to produce accurate outputs and visual depictations of the solution.

[MFEM](https://mfem.org/ "MFEM") is an opensource C++ library for finite element methods. They provide a [serial implementation of the Heat Equation](https://mfem.github.io/doxygen/html/ex16_8cpp_source.html "ex16.cpp"), though they also produce a parallelized version of this code. This is simplified even further, in a (very) [condensed version of the code](https://github.com/betterscientificsoftware/hello-heat-equation/blob/master/LibraryImplementations.md "Condensed MFEM"), to demonstrate the core Heat Equation algorithm.

This implementation clearly demonstrates the complexity introduced by using a third-party library. However, users gain access to a number of numerical solvers, parallelism, and even GPU capability.

### Library Example 2: FD1D\_HEAT\_EXPLICIT (C)
While highly developed numerical libraries such as MFEM have a wide range of functionality and support options, others are smaller. They still provide support for different use cases of function like the heat equation, but do not come with the obscurity and extra features that may intimidate users.

[FD1D\_HEAT\_EXPLICIT](https://people.sc.fsu.edu/~jburkardt/c_src/fd1d_heat_explicit/fd1d_heat_explicit.html "FD1D\_HEAT\_EXPLICIT") is a simple 1-dimensional Heat Equation solver which uses the explicit version of the finite difference method to handle time integration. Versions of this library are written in C, C++, Fortran90, Matlab, and Python. A [code example from the library](https://github.com/betterscientificsoftware/hello-heat-equation/blob/master/LibraryImplementations.md "FD1D") demonstrates a sequential implementation, but can easily be adapted to become parallelized.

While this code is almost identical the hand-coded example above, this library does include some extra features that allows users to implement some additional functionality including writing results to different kinds of R8 files, adding a timestamp, and solving for the Courant-Friedrichs-Loewy coefficient.

### More Implementations!
Using the Heat Equation to demonstrate the power of a programming model or mathematical library is not new. In fact, it is common tutorial exercise for new scientific programmers. Since there are too many interesting examples to include in this article, we've started [a repository showcase](https://github.com/betterscientificsoftware/hello-heat-equation) to collect the many examples.

## Conclusion
The Heat Equation is well known and has several practical applications in the fields of Mathematics and Physics. Because of this, it clearly has a wide array of implementations, from a sequential for-loop, to a portable, GPU-ready, advanced numerical library example. This exemplar PDE makes it the perfect "Hello World!" for the scientific software community. 

## Author Bios

Heather M. Switzer is working as a computing summer intern at Lawrence Livermore National Laboratory. She graduated with her B.S. in Mathematics and Computer Science from Longwood University in 2018 and is currently a 2nd-year M.S./Ph.D. student in Computer Science with a specialization in Computational Science at the College of William & Mary.

Elsa Gonsiorowski is an HPC I/O Specialist at Lawrence Livermore National Laboratory. She graduated with her Ph.D. in Computer Science in 2016 from Rensselaer Polytechnic Institute. Elsa works on a number of open source, system software tools to support HPC users as they manage files across an increasingly complex storage hierarchy. She has a passion for useful documentation and CMake.

<!---
Publish: Yes
RSS update:
Categories: Developement
Topics: Software Engineering, Programming Languages and Tools
Tags:
Level:
Prerequisites: default
Aggregate:
--->
