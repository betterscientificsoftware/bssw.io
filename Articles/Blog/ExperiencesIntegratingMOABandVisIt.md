## What are MOAB and VisIt?
The Mesh-Oriented datABase ([MOAB](https://sigma.mcs.anl.gov/moab-library/)) package is an in-situ, scalable, library for managing mesh-based scientific data.
It is optimized to process mesh data in bulk parcels (or [shards](https://en.wikipedia.org/wiki/Shard_(database_architecture))) or fine-grained iterations over subsets of mesh entities.
Some aspects of MOAB's design and data model are derived from earlier SciDAC efforts including the Terascale Simulation Tools and Technologies ([TSTT](https://www.researchgate.net/publication/259197545_The_TSTTM_Interface)) and the Interoperable Tools for Advanced Petascale Simulations ([ITAPS](https://www.osti.gov/biblio/971531/)) projects.
In addition, MOAB supports scalable I/O to and from [HDF5](https://support.hdfgroup.org/documentation/hdf5/latest/) files.
These files are often used to export MOAB data to other software components in a larger workflow often including visualization tools such as [VisIt](https://visit.llnl.gov) or [ParaView](https://www.paraview.org).

VisIt is a scalable scientific visualization tool for analyzing mesh-based scientific data either in files or in-situ.
Database plugins in VisIt use the Visualization ToolKit ([VTK](https://vtk.org)) grid (`vtkDataset`) and field (`vtkDataArray`) objects to marshal data from files on disk into VisIt's internal memory and parallel processing models.

In this article, we describe our experiences developing and using a MOAB database plugin for VisIt.
Funding from the OASIS project (and from xxx earlier) aims to facilitate collaborations between developers of tools such as VisIt and the broader scientific computing community.
These funding streams have supported a mutually beneficial collaboration between the VisIt core development team at LLNL and the MOAB development team at ANL.

### The ITAPS Generic plugin

As part of the [ITAPS](https://markcmiller86.github.io/ITAPS/) project, a VisIt plugin supporting MOAB was first developed using the [iMesh](https://markcmiller86.github.io/ITAPS/software/iMesh_html/i_mesh_8h.html) interface.
`iMesh` defined a *generic* interface for any package providing unstructured, discrete meshing *services*.	
The [MOAB](https://sigma.mcs.anl.gov/moab-library/), [GRUMMP](https://www.researchgate.net/publication/254313656_GRUMMP_User's_Guide) and [FMDB](https://scorec.rpi.edu/FMDB/) teams participating in ITAPS each implemented the `iMesh` interface to their respective packages.

VisIt's [ITAPS plugin](https://github.com/visit-dav/visit/tree/2.10RC/src/databases/ITAPS_C) could then be compiled against each `iMesh` implementation producing separate plugin instances for ITAPS-MOAB, ITAPS-GRUMMP and ITAPS-FMDB.
A single implementation of the `iMesh` plugin source code supported multiple different mesh management packages demonstrating a key goal of the ITAPS project.
With the ability to *read* from one implementation and *write* to another, this version of the plugin also demonsrated the use of `iMesh` to easily translate data between different mesh management packages.

This early version of the plugin was used successfully to examine a large MOAB [reactor model](https://publications.anl.gov/anlpubs/2013/10/76766.pdf#page=12) consisting of hundreds of thousands of subsets for various components of a novel nuclear fuel assembly.
However, as funding for the ITAPS SciDAC project ended, so did further development and support of the `iMesh` interface and it was eventually removed from MOAB.
A new VisIt database plugin integrating *directly* with MOAB's native interface was needed.

### VisIt Database Plugin Basics

Some of the key routines to be implemented in a database plugin in VisIt are
* `avtMOABFileformat::PopulateDatabaseMetaData(avtDatabaseMetaData *md, ...)`:
  This method runs in response to a user's request to open a database.
  It should avoid as much disk I/O as possible to maintain responsiveness for users.
  This method is intended to be fast and light-weight to tease just enough information from the input database to prime VisIt's GUI.
  During the *first* attempt to open a file in a VisIt session, the user chooses how to launch the parallel engine including setting the number of nodes, `N`, and MPI ranks, `R`.
* `vtkDataset* avtMOABFileFormat::GetMesh(char const *meshName, ...)`:
  This method runs in response to a user's request to draw a plot.
  It returns a VTK *grid* object holding the geometric and topological configuration of the mesh identified by `meshName`.
  The `meshName` identifier will appear in various places in VisIt's GUI menus according to information provided by `PopulateDatabaseMetaData(...)`.
* `vtkDataArray *avtMOABFileFormat::GetVar(char const *variableName, ...)`:
  This method runs in response to a user's request to draw a plot.
  It returns a VTK *field* object identified by `variableName` holding data for a point-centered or cell-centered field.
  The `variableName` identifier will appear in various places in VisIt's GUI menus according to information provided in `PopulateDatabaseMetaData(...)`.
  In addition, that `variableName` (say `"foo"`) is also associated with a `meshName` (say `"bar"`) such that `GetVar("foo",...)` returns a `vtkDataArray*` object that is 1:1 with either the points or cells of the mesh returned by `GetMesh("bar",...)`. 

A developer has many choices in designing a plugin and these ultimately determine a majority of the user experience (UX); the performance and functionality VisIt's GUI will provide in interacting with the data.

Except for simple cases, VisIt will not divide a large, monolithic mesh into pieces for parallel processing.
Instead, it piggy backs off of a parallel decomposition an upstream data producer would have already created.
In VisIt, a mesh consisting of `K` pieces can be stored and distributed among `M` files (typically `K>>M`) and then processed by VisIt on `R` MPI ranks.
The user choses an `R` when launching the VisIt *engine*.
Typically `R<=K` though if `R>K`, VisIt still functions albeit less efficiently because `R-K` ranks will idle.

Furthermore, there are a number of ways of using VisIt such that the number of pieces that need to be processed for any given plot is often `K'<<K`.
Each time VisIt produces a plot, a list of the relevant pieces is computed.
This list is sorted in increasing number and then pieces are assigned to ranks according to various [*load balance*](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/getting_started/Startup_Options.html#:~:text=Parallel%20launch%20options) algorithms.

### The MOAB Native plugin

However, in MOAB, a large mesh is stored as a monolithic whole single piece in a single file.
It is divided into pieces, one piece per rank, which are scattered to MPI ranks during read.
This process is reversed and the pieces are gathered and reassembled into a monolithic whole during write.
Thus, for the MOAB database plugin in VisIt, `K` is not fixed but variable. 
MOAB always reports to VisIt that `K==R`, the number of ranks the user chose when launching the VisIt *engine*.
