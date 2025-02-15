## What are MOAB and VisIt
The Mesh-Oriented datABase ([MOAB](https://sigma.mcs.anl.gov/moab-library/)) is a scalable, parallel, scientific computing software component for representing and operating upon mesh-based scientific data in-situ.
MOAB can handle structured and unstructured meshes and fields thereon consisting of elements in the finite element “zoo”, including polygons and polyhedra.
The MOAB API provides a scalable, parallel representation of many types of mesh-based scientific data and metadata.
MOAB is optimized for efficiency in space and time, processing mesh data either in aggregate parcels (or [shards](https://en.wikipedia.org/wiki/Shard_(database_architecture))) as well as iterations over individual mesh entities.
In addition, MOAB provides a means for high performance, scalable I/O of the mesh-based scientific data it is processing to and from files on disk.
Some aspects of MOAB's design and data model are derived from earlier SciDAC projects including the Terascale Simulation Tools and Technologies ([TSTT](https://www.researchgate.net/publication/259197545_The_TSTTM_Interface)) and the Interoperable Tools for Advanced Petascale Simulations ([ITAPS](https://www.osti.gov/biblio/971531/)).

One of the reasons MOAB is used to *write* scientific data to files, as opposed to simply operate upon it in memory, is to export its data to other software components in use in a larger simulation and modeling workflow.
A commonly used component in such workflows is a visualization tool such as [VisIt](https://visit.llnl.gov) or [ParaView](https://www.paraview.org).
VisIt, for example, is a scalable, parallel scientific visualization tool for visualizing and analyzing mesh-based scientific data either in files or in-situ.
VisIt is built on top of the Visualization ToolKit ([VTK](https://vtk.org)) and relies upon VTK for a majority of its functionality.
However, I/O in VisIt is handled by VisIt's own database architecture and *plugins*.
In this article, we describe our experiences developing and using a MOAB database plugin for VisIt.

Funding from the OASIS project (and from xxx earlier) aims to facilitate collaborations between developers of tools such VisIt and the broader scientific computing community.
These funding streams have supported a long standing collaboration between the VisIt core development team at LLNL and the MOAB development team at ANL.

### Early integration work with ITAPS
The VisIt<->MOAB integration effort began with development a database plugin supporting the [iMesh](https://markcmiller86.github.io/ITAPS/software/iMesh_html/i_mesh_8h.html) interface of the [ITAPS]() project.
Multiple code teams implemented the iMesh interface in their scientific mesh management software components including the [MOAB](https://sigma.mcs.anl.gov/moab-library/), [GRUMMP](https://www.researchgate.net/publication/254313656_GRUMMP_User's_Guide) and [FMDB](https://scorec.rpi.edu/FMDB/) teams.
VisIt's [ITAPS plugin](https://github.com/visit-dav/visit/blob/2.10RC/src/databases/ITAPS_C/avtITAPS_CFileFormat.C) uniquely demonstrated the power of the iMesh interface because it supported all existing implementations via a *single* instance of the plugin source code.
When VisIt was compiled, it would compile the same database plugin source code against each iMesh implementation producing plugin instances for ITAPS-MOAB, ITAPS-GRUMMP and ITAPS-FMDB.
In turn, this enabled VisIt to be easily used as a data translator between these various, disparate mesh management software components.

This early version of the plugin was used successfully to examine a large MOAB [reactor model](https://publications.anl.gov/anlpubs/2013/10/76766.pdf#page=12) consisting of hundreds of thousands of subsets for various components of the nuclear fuel assembly.
This was how MOAB was first integrated with VisIt.
However, as development of the iMesh interface waned, MOAB continued to evolve such that eventually iMesh provided an insufficient path to access MOAB data and features.
In particular, this included scalable parallel mesh data processing and I/O features.
In addition, the iMesh interface eventually became obsolete and was removed from MOAB.
A new VisIt database plugin integrated *directly* with MOAB was needed.

### Direct integration of MOAB with VisIt

VisIt supports a variety of parallel I/O and execution paradigms for interacting with data in disk files through database plugins.
The most commonly used paradigm is the Multiple Indpendent File ([MIF](https://www.hdfgroup.org/2017/03/21/mif-parallel-io-with-hdf5/)) paradigm.
In this paradigm, a large, coherent mesh is decomposed into pieces (shards, chunks, domains) that are distributed to a number of different files.
In parallel, each VisIt MPI rank is assigned some number of those pieces.
If there are more MPI ranks than pieces, some ranks get no pieces.
If there are more pieces than MPI ranks, some ranks get multiple pieces.
Given 60 pieces, for example VisIt can run 1:1 on 60 tasks, 2:1 on 30 tasks, 3:1 on 20 tasks or even 3:1 on 12 together with 4:1 on 6 of 18 total tasks.

But, that paradigm does not require anything special in the way of parallel I/O.
In fact, it achieves parallelism by independently managing concurrent access via *sequential* interfaces to data in multile different files.
MOAB uses HDF5's parallel I/O interface (which in turn uses both collective and independent MPI-IO interfaces) to a single, shared file.
The MOAB plugin is unique in VisIt because of the 150+ database plugins VisIt supports, it is the only database plugin using single-shared file I/O.










