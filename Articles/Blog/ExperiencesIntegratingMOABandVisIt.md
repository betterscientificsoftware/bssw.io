## What are MOAB and VisIt?
The Mesh-Oriented datABase ([MOAB](https://sigma.mcs.anl.gov/moab-library/)) is an in-situ, scalable, parallel, software component for mesh-based scientific data.
It is optimized for efficiency in space and time, processing mesh data either in bulk parcels (or [shards](https://en.wikipedia.org/wiki/Shard_(database_architecture))) or fine-grained iterations over specific sets of mesh entities.
In addition, MOAB provides a means for high performance, scalable I/O to and from [HDF5](https://support.hdfgroup.org/documentation/hdf5/latest/) files on disk.
Some aspects of MOAB's design and data model are derived from earlier SciDAC projects including the Terascale Simulation Tools and Technologies ([TSTT](https://www.researchgate.net/publication/259197545_The_TSTTM_Interface)) and the Interoperable Tools for Advanced Petascale Simulations ([ITAPS](https://www.osti.gov/biblio/971531/)).

One reason MOAB *writes* scientific data to files, as opposed to operate upon it in-situ, is to export its data to other software in a larger workflow.
A commonly used component in such workflows is a visualization tool such as [VisIt](https://visit.llnl.gov) or [ParaView](https://www.paraview.org).
VisIt, for example, is a scalable, parallel scientific visualization tool for analyzing mesh-based scientific data either in files or in-situ.
Database plugins in VisIt use the Visualization ToolKit ([VTK](https://vtk.org)) grid and field objects to marshal data from files on disk into its internal memory data model.
In this article, we describe our experiences developing and using a MOAB database plugin for VisIt.

Funding from the OASIS project (and from xxx earlier) aims to facilitate collaborations between developers of tools such as VisIt and the broader scientific computing community.
These funding streams have supported a mutually beneficial collaboration between the VisIt core development team at LLNL and the MOAB development team at ANL.

### The ITAPS Generic plugin

A plugin supporting MOAB was first developed using the [iMesh](https://markcmiller86.github.io/ITAPS/software/iMesh_html/i_mesh_8h.html) interface as part of the [ITAPS](https://markcmiller86.github.io/ITAPS/) project.
`iMesh` was developed to serve as a *generic* interface to any package providing *services* to manage discrete meshes composed of sets of entities, such as nodes, edges, faces and volumes, modifications to these entities and tags and tag data associated with sets of these entities.	
The teams participating in ITAPS, [MOAB](https://sigma.mcs.anl.gov/moab-library/), [GRUMMP](https://www.researchgate.net/publication/254313656_GRUMMP_User's_Guide) and [FMDB](https://scorec.rpi.edu/FMDB/), each implemented the `iMesh` interface to their respective mesh management software packages.

VisIt's [ITAPS plugin](https://github.com/visit-dav/visit/blob/2.10RC/src/databases/ITAPS_C/avtITAPS_CFileFormat.C) could then be compiled against each `iMesh` implementation producing separate plugin instances for ITAPS-MOAB, ITAPS-GRUMMP and ITAPS-FMDB.
A single implementation of the `iMesh` plugin source code supported multiple different mesh management packages demonstrating a key goal of the ITAPS project.
With the ability to *read* from one implementation and *write* to another, this version of the plugin also demonsrated the use of `iMesh` to easily translate data between different mesh management packages.

This early version of the plugin was used successfully to examine a large MOAB [reactor model](https://publications.anl.gov/anlpubs/2013/10/76766.pdf#page=12) consisting of hundreds of thousands of subsets for various components of a novel nuclear fuel assembly.
However, as funding for the ITAPS SciDAC project ended, so did further development and support of the iMesh interface and it was eventually removed from MOAB.
A new VisIt database plugin integrating *directly* with MOAB's native interface was needed.

### The MOAB Native plugin

Except for simple cases, VisIt cannot divide a large, monolithic mesh into pieces for parallel processing.
Instead, it piggy backs off an upstream data producer which would have already done this.
A dataset of `K` pieces stored and distributed among `M` files (typically `K>>M`) can be processed by VisIt on `R` MPI ranks.
Typically `R<=K` though `R>K` still functions albeit inefficiently because `R-K` ranks idle.

However, in MOAB, a large mesh is stored as a monolithic whole in a file.
It is divided into pieces, one piece per rank, which are scattered to MPI ranks during read.
This process is reversed and the pieces are gathered and reassembled into a monolithic whole during write.
Thus, VisIt is able to delegate the work of dividing a large mesh into pieces to the MOAB mesh management software component operating within the plugin.
MOAB always reports to VisIt that `K=R`.
The user decides `R` when the launch VisIt.

Key routines implemented in any database plugin are
* `avtMOABFileformat::PopulateDatabaseMetaData(...)`:
  This method is intended to be fast and light-weight to tease enough information from file(s) and inform VisIt about mesh and variable objects present.
  It should avoid as much disk I/O as possible to maintain responsiveness for users when opening files.
* `vtkDataset* avtMOABFileFormat::GetMesh(...)`:
  This method is executed in response to a user's request to draw a plot in VisIt.
  Every variable to be plotted in VisIt is defined on some sort of mesh and it is the `::GetMesh()` call that returns that object.
* `vtkDataArray *avtMOABFileFormat::GetVar(...)`:
  This method is executed in response to a user's request to draw a plot in VisIt.
  It returns a variable (or field) defined on a mesh.

A plugin implmentor has several choices in exposing objects in a database to VisIt.
There are a number of critical choices to make effecting how VisIt's GUI menus will behave with the data, how the subset inclusion lattice (SIL) will represent subsets in the data, memory and time performance, etc.

When running on `R` MPI ranks, MOAB informs VisIt that the mesh is available as `R` pieces

itself does not do any work to decompose a large dataset into pieces for parallel processing.
Instead, it simply uses the pieces that are typically already determined by the data producer, up stream of VisIt.
However, this approach also relies on the idea that all (or most) tools necessary to process the dataset in a large workflow all agree to permit *domain overload*.













