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

VisIt's parallel execution paradigm is often described as *piggy-backing* off the data producer's parallel decomposition.
Once a dataset has been decmposed for parallel processing, it typically remains in its decomposed state forever more.
Given a dataset of `K` pieces, those `K` pieces may be distributed among `M` files where `K >> M` and then processed by VisIt on `R` MPI ranks where `R<=K` (well, its harmless if `R>K` except that `R-K` MPI ranks will simply go unused).

itself does not do any work to decompose a large dataset into pieces for parallel processing.
Instead, it simply uses the pieces that are typically already determined by the data producer, up stream of VisIt.
However, this approach also relies on the idea that all (or most) tools necessary to process the dataset in a large workflow all agree to permit *domain overload*.


VisIt supports both the Multiple Independent File ([MIF](https://www.hdfgroup.org/2017/03/21/mif-parallel-io-with-hdf5/)) and single shared file parallel I/O paradigms.
Of 150+ database plugins, the MOAB plugin is one of only two using HDF5's parallel I/O interface (which in turn uses both collective and independent MPI-IO interfaces) to a single, shared file.
Complicating matters, VisIt involves multiple executables working together; a *metadata server* and either a serial or a parallel *engine*.
Of these, only the parallel engine uses MPI.
The metadata server and serial engine require serial installs of MOAB and HDF5 whereas the parallel engine requires parallel installs of both.
This complicates build processes.











