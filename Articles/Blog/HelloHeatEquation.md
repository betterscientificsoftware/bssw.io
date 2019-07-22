# The Heat Equation is the "Hello World" of Scientific Computing

#### Contributed by [Heather M. Switzer](https://github.com/heatherms27 "Heather Switzer GitHub Profile") and [Elsa Gonsiorowski](https://github.com/gonsie "Elsa Gonsiorowski GitHub Profile")

"Hello World!" is a prototypical program that is universally used by programmers to illustrate the basic syntax of a programming language. At a glance, it can demonstrate a programming language's syntactic structure and can indicate how easy or difficult implementing a basic program may be (see several [Hello World implementations at WikiBooks](https://en.wikibooks.org/wiki/Computer_Programming/Hello_world)). For the scientific software community, a programming language is only the most basic building block of a program. Scientific software must use various programming models or math libraries to achieve high performance for any particular problem. These communities need a version "Hello World!" to compare programming options. The Heat Equation, a well known partial differential equation (PDE), is the perfect formula for this task.

## What is the Heat Equation?
The Heat Equation, also known as the Diffusion Equation, was developed by Joseph Fourier in 1822. Primarily used in the fields of Mathematics and Physics, the equation shows how heat (or something similar) changes over time in a solid medium. While there are many adaptations for different dimensions and scenerios, new programmers are often first introduced to the 1-dimensional version of the Heat Equation as a tutorial problem. Specifically, the Forward-Time, Central-Space (FTCS) version of the equation is used.

The following description is adapted from [a Trinity University lecture](http://ramanujan.math.trinity.edu/rdaileda/teach/s14/m3357/lectures/lecture_2_25_slides.pdf "One-Dimensional Heat Equation").

Suppose you have a thin metal rod along the x-axis starting at position 0 and ending at position _L_. The goal is to model the temperature distribution throughout the rod at a given time, with the following (ideal) assumptions:

* An initial temperature distribution is given
* Boundary conditions (established tempuratures at each end of the rod) are known
* Heat only moves horizontally through the bar
* There are no external heating/cooling sources

<div style="text-align:center"><img width="75%" src="Bar.png" /></div>

To model the temperature distribution of the rod, we can use the 1-dimensional Heat Equation given by the formula:

_&part;u / &part;t = &alpha;&nabla; &sup2;u_

Where:
* _u_ = Temperature at a position, _x_
* _t_ = time
* _&alpha;_  = thermal diffusity of the material
* _&nabla;_ = The LaPlace operator

### FTCS: Assumptions and Discretization
To make the problem more approachable, we make some simplifying assumptions:
* _&alpha;_ is constant
* The heat/cooling source only comes from initial/boundary conditions
* Only Cartesian coordinates in 1 dimension are used

Since the heat equation takes the form of a PDE over a continuous space, most programs create a discretization of the formula over a finite set of sampling points. By approximating the first derivative of _&part;u / &part;t_, the equation can be discretized to:

_u_<sup>_k_+1</sup><sub>_i_</sub> = _ru_<sup>_k_</sup><sub>_i_+1</sub> + (1 - 2 _r_)_u_<sup>_k_</sup><sub>_i_</sub> + _ru_<sup>_k_</sup><sub>_i_-1</sub>
(The full discretization process can be found [here](https://xsdk-project.github.io/ATPESC2018HandsOnLessons/lessons/hand_coded_heat/ "Hand-Coded Heat").)

Where _r = &alpha;_ &Delta;_t&sup2; /_ &Delta;_x&sup2;_. This is the Forward-Time, Central-Space (FTCS) scheme which is considered numerically stable as long as _r_ is less than or equal to 0.5.

### Why the Heat Equation?
PDEs are widely used among the different sciences to model various phenomena such as electromagnetism, fluid mechanics, and heat transfers. While PDEs extend across multiple fields, they can still be quite tricky to work with because unlike ordinary differential equations, they are comprised of derivatives of more than just a single variable. A single example of a PDE is the Heat Equation, which is used calculate the distribution of heat on a region over time. While here we just focus on the 1-dimensional version of the Heat Equation, it can actually take a multitude of forms including the [Fourier](https://fenix.tecnico.ulisboa.pt/downloadFile/3779571609326/transp3.pdf "Fourier Equation"), [LaPlace](https://www.britannica.com/science/Laplaces-equation "LaPlace's Equation") (also known as steady-state), [2D](http://ramanujan.math.trinity.edu/rdaileda/teach/s12/m3357/lectures/lecture_3_6_short.pdf "2D Heat Equation"), and [3D](https://ocw.mit.edu/courses/mathematics/18-303-linear-partial-differential-equations-fall-2006/lecture-notes/pde3d.pdf "3D Heat Equation") heat equations.

By taking a continuous PDE and turning it into a discrete formula, parallelism can be accomplished. For example, the equation for finding the tempurature at a given point in time in the 1-dimensional Heat Equation is:

_u_<sup>_k_+1</sup><sub>_i_</sub> = _ru_<sup>_k_</sup><sub>_i_+1</sub> + (1 - 2 _r_)_u_<sup>_k_</sup><sub>_i_</sub> + _ru_<sup>_k_</sup><sub>_i_-1</sub>

with _k_ being the time, and _i_ being a point in our axis. We can see that the temperature of _u_<sup>_k+1_</sup><sub>_i_</sub> is only dependent on temperatures from spots _i_, _i-1_, and _i+i_ from the previous iteration. By having two arrays to store of old and new temperatures, each location for time _k_ is independent and can be distributed among different processors and cores.

As a consequence of PDEs being so expansive, several implementations are available for multiple programming languages and numerical libraries. Users who are new to coding are often first introduced to the Heat Equation as a means of teaching them different programming languages or tools such as MPI and OpenMP. By reviewing these implementations a solid foundation of specfic language's characteristics can be seen.

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
We begin with the most basic implementation. Again, this demonstrates little beyond the syntax of a for-loop.
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
OpenMP is a portable way to add parallelism to a program. Here, we demonstrate its syntax and use of `#pragma`. We see that this implementation is a 2 line change from the base implementation.
```c
bool update_solution_ftcs(int n, double *uk1, const double *uk0,
double alpha, double dx, double dt, double bc0, double bc1){
    double r = alpha * dt / (dx * dx);

    // Sanity check for stability
    if (r > 0.5) return false;

    //FTCS update algorithm
    #pragma omp parallel num_threads(n-2) private(tid) shared(uk1, uk0, r){
        i = omp_get_thread_num();    // Thread numbers will range from 0 to n-3
        uk1[i+1] = r*uk0[i+2] + (1-2*r)*uk0[i+1] + r*uk0[i];
     }

    // Enforce boundary conditions
    uk1[0] = bc0;
    uk1[n-1] = bc1;

    return true;
}
```

### Library Example: MFEM (C++)
Scientific software programmers are able to take advantage of numerical libraries instead of hand-coding implementations, which can optimize performance and allow access to the additional features. Most of these implementations have multiple steps that are outlined to produce accurate outputs and visual depictations of the solution.

[MFEM](https://mfem.org/ "MFEM") is an opensource C++ library for finite element methods. Their serial implementation of the Heat Equation can be found [here](https://mfem.github.io/doxygen/html/ex16_8cpp_source.html "ex16.cpp"), though they also produce a parallelized version of this code. A (very) condensed version of the code is shown below.

```c++
// 1. Read mesh from a given mesh file
Mesh *mesh = new Mesh(mesh_file, 1, 1);
int dim = mesh->Dimension();

// 2. Define ODE solver type
switch(ode_solver_type){
    case 1: ode_solver = new BackwardEulerSolver; break;
    // other solvers are provided
}

// 3. Refine mesh to increase resolution
for (int lev = 0; lev < ref_levels; lev++){
    mesh->UniformRefinement();
}

// 4. Define vector element space, initial conditions for u, and conductor operator
H1_FECollection fe_coll(order, dim);
FiniteElementSpace fespace(mesh, &fe_coll);
FunctionCoefficient u_0(InitialTemperature);
u_gf.ProjectCoefficient(u_0);
Vector u;
u_gf.GetTrueDofs(u);
ConductionOperator oper(fespace, alpha, kappa, u);

// 5. Perform time-integration
ode_solver->Init(oper);
double t = 0.0;
bool last_step = false;
for (int ti = 1; !last_step; ti++){
// Time integration at each step
}

// 6. Save the final solution that can be viewed later
ofstream osol("ex16-final.gf");
osol.precision(precision);
u_gf.Save(osol);

```

This implementation clearly demonstrates the complexity introduced by using a third-party library. However, users gain access to a number of numerical solvers, parallelism, and even GPU capability.

### Library Example 2: FD1D\_HEAT\_EXPLICIT (C)
While highly developed numerical libraries such as MFEM have a wide range of functionality and support options, others are smaller. While they still provide support for different use cases of function like the heat equation, they do not come which the obscurity and extra features that may intimidate users.

[FD1D\_HEAT\_EXPLICIT](https://people.sc.fsu.edu/~jburkardt/c_src/fd1d_heat_explicit/fd1d_heat_explicit.html "FD1D\_HEAT\_EXPLICIT") is a simple 1-dimensional Heat Equation solver which uses the explicit version of the finite difference method to handle time integration. Versions of this library are written in C, C++, Fortran90, Matlab, and Python. The code example from the library shown below is sequential, but can easily be adapted to become parallelized.

```c
double *fd1d_heat_explicit ( int x_num, double x[], double t, double dt, 
  double cfl, double *rhs ( int x_num, double x[], double t ), 
  void bc ( int x_num, double x[], double t, double h[] ), double h[] )
  {
  double *f;
  double *h_new;
  int j;

  f = rhs ( x_num, x, t );

  h_new = ( double * ) malloc ( x_num * sizeof ( double ) );

  h_new[0] = 0.0;

  for ( j = 1; j < x_num - 1; j++ )
  {
    h_new[j] = h[j] + dt * f[j] 
      + cfl * (         h[j-1]
                - 2.0 * h[j]
                +       h[j+1] );
  }
  h_new[x_num-1] = 0.0;

  bc ( x_num, x, t + dt, h_new );

  free ( f );

  return h_new;
}
```

While this code is almost identical the hand-coded example shown above, this library does include some extra features that allows users to implement some additional functionality including writing results to different kinds of R8 files, adding a timestamp, and solving for the Courant-Friedrichs-Loewy coefficient.

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
