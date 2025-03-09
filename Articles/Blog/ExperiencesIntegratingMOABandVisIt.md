## What are MOAB and VisIt?
The Mesh-Oriented datABase ([MOAB](https://sigma.mcs.anl.gov/moab-library/)) package is an in-situ, scalable, library for managing mesh-based scientific data.
It is optimized to process mesh data in bulk parcels (or [shards](https://en.wikipedia.org/wiki/Shard_(database_architecture))) or fine-grained iterations over subsets of mesh entities.
Some aspects of MOAB's design and data model are derived from earlier SciDAC efforts including the Terascale Simulation Tools and Technologies ([TSTT](https://www.researchgate.net/publication/259197545_The_TSTTM_Interface)) and the Interoperable Tools for Advanced Petascale Simulations ([ITAPS](https://www.osti.gov/biblio/971531/)) projects.
In addition, MOAB supports scalable I/O to and from [HDF5](https://support.hdfgroup.org/documentation/hdf5/latest/) files and [PNETCDF](https://parallel-netcdf.github.io/) files.
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
* `void avtMOABFileformat::PopulateDatabaseMetaData(avtDatabaseMetaData *md, ...)`:
  This method is called collectively in parallel and runs in response to a user's request to open a database.
  This method is intended to be fast (e.g. minimal disk I/O) and light-weight to tease just enough information from the input database to prime VisIt's GUI.
  During the *first* attempt to open a database in a VisIt session, the user chooses the number of nodes, `N`, and MPI ranks, `R` for the parallel *engine*.
* `vtkDataSet* avtMOABFileFormat::GetMesh(char const *meshName, ...)`:
  This method is called independently in parallel and runs in response to a user's request to draw a plot.
  It returns a VTK *grid* object holding the geometry and topology of the mesh identified by `meshName`.
  `meshName` will appear in various places in VisIt's GUI menus according to metadata provided in `PopulateDatabaseMetaData(...)`.
* `vtkDataArray *avtMOABFileFormat::GetVar(char const *varName, ...)`:
  This method is called independently in parallel and runs in response to a user's request to draw a plot.
  It returns a VTK *field* object identified by `varName` holding data for a point- or cell-centered field.
  `varName` will appear in various places in VisIt's GUI menus according to metadata provided in `PopulateDatabaseMetaData(...)`.
  In addition, a `varName` (say `"foo"`) is also associated with a `meshName` (say `"bar"`) such that `GetVar("foo",...)` returns a `vtkDataArray*` object that is 1:1 with either the points or cells of the `vtkDataSet*` returned by `GetMesh("bar",...)`. 

A developer has numerous choices in designing a plugin many of which ultimately determine the user experience (UX); the performance and functionality VisIt's GUI will provide in interacting with the data.

Except for simple cases, VisIt will not divide a large, monolithic mesh into pieces for parallel processing.
Instead, it piggy backs off of a parallel decomposition an upstream data producer would have already created.
The `K` pieces of mesh can be stored and distributed among `M` files (typically `K>>M`) and then processed by VisIt on `R` MPI ranks.
The user choses an `R` when launching the VisIt *engine*.
Typically `R<=K` though if `R>K`, VisIt still functions albeit less efficiently because `R-K` ranks will idle.

Each time VisIt produces a plot, a list of pieces *relevant* to the current plot, `K'<=K`, is computed.
This list is sorted in increasing piece number and assigned to ranks according to various [*load balance*](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/getting_started/Startup_Options.html#:~:text=Load%20balance%20options) algorithms.

### The MOAB Native plugin

In MOAB native hdf5 format, a large mesh is stored as a monolithic whole single piece in a single file. To enable parallel read, the mesh needs to be prepartitioned into parts using [Zoltan](https://sandialabs.github.io/Zoltan/) or [metis](https://github.com/KarypisLab/METIS), and the partitioning information is saved into the file. 

At read time, parts are assigned to MPI ranks in a balanced fashion, and it is better to have `K` >= `R`, otherwise some tasks will be idle. 
This process is reversed and the parts are gathered and reassembled into a monolithic whole during write.

When PopulateDatabaseMetaData is called, rank 0 reads information from the hdf5 header file, related to number of available parts, names of variables associated with the mesh. This information is then broadcast to all other tasks, and processed by Visit to populate menus. 
The file is read in parallel at the GetMesh command issued by Visit; Each task will read only its parts assigned, and the read process is collective. Each task will have its subparts converted to VTK objects, for visualization. 

