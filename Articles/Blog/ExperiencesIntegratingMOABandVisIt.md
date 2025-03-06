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
`iMesh` defined a *generic* interface to any package providing *services* to manage discrete meshes composed of sets of node, edge, face and/or volume entities as well as tags and tag data associated thereon.	
The teams participating in ITAPS, [MOAB](https://sigma.mcs.anl.gov/moab-library/), [GRUMMP](https://www.researchgate.net/publication/254313656_GRUMMP_User's_Guide) and [FMDB](https://scorec.rpi.edu/FMDB/), each implemented the `iMesh` interface to their respective mesh management software packages.

VisIt's [ITAPS plugin](https://github.com/visit-dav/visit/blob/2.10RC/src/databases/ITAPS_C/avtITAPS_CFileFormat.C) could then be compiled against each `iMesh` implementation producing separate plugin instances for ITAPS-MOAB, ITAPS-GRUMMP and ITAPS-FMDB.
A single implementation of the `iMesh` plugin source code supported multiple different mesh management packages demonstrating a key goal of the ITAPS project.
With the ability to *read* from one implementation and *write* to another, this version of the plugin also demonsrated the use of `iMesh` to easily translate data between different mesh management packages.

This early version of the plugin was used successfully to examine a large MOAB [reactor model](https://publications.anl.gov/anlpubs/2013/10/76766.pdf#page=12) consisting of hundreds of thousands of subsets for various components of a novel nuclear fuel assembly.
However, as funding for the ITAPS SciDAC project ended, so did further development and support of the `iMesh` interface and it was eventually removed from MOAB.
A new VisIt database plugin integrating *directly* with MOAB's native interface was needed.

### The MOAB Native plugin

Some of the key routines to be implemented in a database plugin in VisIt are
* `avtMOABFileformat::PopulateDatabaseMetaData(...)`:
  This method is used when *opening* files in VisIt.
  It should avoid as much disk I/O as possible to maintain responsiveness for users.
  This method is intended to be fast and light-weight to tease enough information from the input file(s) to prime VisIt's GUI.
  During the *first* attempt to open a file in a VisIt session, the user chooses how to launch the parallel engine.
* `vtkDataset* avtMOABFileFormat::GetMesh(char const *meshName, ...)`:
  This method is executed in response to a user's request to draw a plot in VisIt.
  It returns a VTK *grid* object that specifies the geometric and topological configuration of the selected data.
* `vtkDataArray *avtMOABFileFormat::GetVar(char const *variableName, ...)`:
  This method is executed in response to a user's request to draw a plot in VisIt.
  This method returns a VTK *field* object holding data for a node-centered or cell-centered field on an associated mesh object returned from `GetMesh()`.

A plugin developer has many choices in designing a plugin which ultimately effect the user experience (UX); the performance and functionality VisIt's GUI will provide in interacting with the data.

Except for simple cases, VisIt will not divide a large, monolithic mesh into pieces for parallel processing.
Instead, it piggy backs off of a parallel decomposition an upstream data producer would have already created.
In VisIt, a mesh consisting of `K` pieces can be stored and distributed among `M` files (typically `K>>M`) and then processed by VisIt on `R` MPI ranks.
The user choses an `R` when launching the VisIt *engine*.
Typically `R<=K` though if `R>K`, VisIt still functions albeit less efficiently because `R-K` ranks will idle.

However, in MOAB, a large mesh is stored as a monolithic whole single piece in a single file.
It is divided into pieces, one piece per rank, which are scattered to MPI ranks during read.
This process is reversed and the pieces are gathered and reassembled into a monolithic whole during write.
Thus, for the MOAB database plugin in VisIt, `K` is not fixed but variable. 
MOAB always reports to VisIt that `K=R`, whatever the number of ranks the user chose when launching the VisIt *engine*.

















