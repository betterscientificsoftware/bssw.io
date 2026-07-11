# Experiences with the Scalable Integration of MOAB and VisIt

**Hero Image:**

- <img src='../../images/visit-moab-bssw-hero.jpg' />

#### Contributed by [Iulian Grindeanu](https://github.com/iulian787), [Vijay Mahadevan](https://github.com/vijaysm), [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: July 15, 2026

<!-- begin deck -->
Close collaboration and creative problem solving can overcome significant challenges integrating packages employing disparate data models and parallel execution paradigms.
<!-- end deck -->

## Introduction

Funding from OASIS (now part of [RAPIDS](https://rapids.lbl.gov)) and SciDAC ([FASTMath](https://sites.google.com/lbl.gov/scidacfastmathinstitute/home)) and [ECP](https://www.exascaleproject.org) has facilitated collaborations between developers of tools such as [VisIt](https://visit.llnl.gov) and [ParaView](https://www.paraview.org) and the broader scientific computing community.
Examples include collaborations between developers of [VisIt](https://visit.llnl.gov) at LLNL and developers of I/O technologies such as [ADIOS/ADIOS2](https://adios2.readthedocs.io/en/latest/#) at ORNL, [BoxLib/AMReX](https://amrex-codes.github.io) at LBNL and [MOAB](https://sigma.mcs.anl.gov/moab-library/) at ANL.
This article describes our experiences developing a MOAB [database plugin](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/data_into_visit/CreatingDatabasePlugin.html#creating-a-database-reader-plugin) for VisIt.
Key differences in the two products' scientific data models and parallel execution paradigms have presented several interesting challenges requiring innovative solutions.

## What are MOAB and VisIt?

MOAB (Mesh-Oriented datABase) is a scalable in-situ library for managing mesh-based scientific data.
It excels at scalable processing of mesh data in bulk parcels or in fine-grained iterations over individual mesh elements.
Some aspects of MOAB trace their origins to earlier [TSTT](https://www.researchgate.net/publication/259197545_The_TSTTM_Interface) and [ITAPS](https://www.osti.gov/biblio/971531/) SciDAC efforts.
VisIt is a scalable scientific visualization tool for analyzing mesh-based scientific data in files or in-situ.
Database plugins in VisIt employ various I/O strategies to marshal data from files on disk into Visualization ToolKit ([VTK](https://vtk.org)) grid ([`vtkDataset`](https://vtk.org/doc/nightly/html/classvtkDataSet.html)) and array ([`vtkDataArray`](https://vtk.org/doc/nightly/html/classvtkDataArray.html)) objects used in VisIt's internal parallel storage and processing framework.

MOAB is more than a database for *storing* data.
VisIt is more than a tool for *displaying* data.
Both also support a variety of scalable, data processing and analysis *services* such as topological and spatial queries, ghost layer management and solution transfer.
The critical MOAB service exploited here for the VisIt plugin is scalable, parallel I/O from a [single shared file](https://www.hdfgroup.org/2017/03/21/mif-parallel-io-with-hdf5/) via [HDF5](https://support.hdfgroup.org/documentation/hdf5/latest/).

### Early Success with the ITAPS/iMesh plugin

As part of the [ITAPS](https://markcmiller86.github.io/ITAPS/) project, a VisIt plugin supporting the [iMesh](https://markcmiller86.github.io/ITAPS/software/iMesh_html/i_mesh_8h.html) interface was initially developed.
MOAB, [GRUMMP](https://www.researchgate.net/publication/254313656_GRUMMP_User's_Guide), and [FMDB](https://scorec.rpi.edu/FMDB/) developers participating in ITAPS each implemented the `iMesh` interface for their respective packages.
The same [ITAPS plugin](https://github.com/visit-dav/visit/tree/2.10RC/src/databases/ITAPS_C) source code was then compiled and linked against the three `iMesh` implementations producing three shared library plugins; ITAPS-MOAB, ITAPS-GRUMMP, and ITAPS-FMDB.
This work demonstrated a key ITAPS goal; that a single interface could support data exchange among a variety of disparate mesh management packages.

The ITAPS-MOAB plugin was used successfully to examine a large MOAB [reactor model](https://publications.anl.gov/anlpubs/2013/10/76766.pdf#page=12) consisting of hundreds of thousands of subsets for various components of a novel nuclear fuel assembly.
However, as funding for the ITAPS SciDAC project ended, so did further development and support of the `iMesh` interface.
It was eventually removed from MOAB.
A new VisIt database plugin integrating *directly* with MOAB's native interface was needed.

### Key Differences Between MOAB and VisIt

MOAB’s data model consists of mesh *entities* of 0...3 topological dimensions, *entity sets*, *tags* (both *sparse* and *dense*) attached to mesh entities and/or entity sets and *relations* (topological, containment, and/or hierarchical) between these.
VisIt’s data model consists of *meshes* (structured, unstructured, AMR, CSG, etc.) comprised of *nodes* (0 dimension) and, optionally, *zones* (1...3 dimensions), decompositions of meshes into different classes of *subsets* (domains, blocks, materials, enumerations), continuous *variables* (scalar, vector or tensor) and ordered lists of these as *time series*.

MOAB's data model emphasizes topological and relational aspects of scientific data whereas VisIt's data model emphasizes computational modeling aspects of scientific data.
These differences lead to some challenges in integrating MOAB with VisIt.
For example, while a MOAB dense tag is almost certainly a VisIt variable, MOAB tags do not carry information about their tensor rank or continuous interpolation.
On the other hand, a MOAB sparse tag almost certainly requires some sort of enumerated subset in VisIt in order to be properly defined.
Some entity sets in MOAB are best treated as material subsets in VisIt whereas others are best treated as enumerations.
Selecting which approach is best is not always obvious.
While both MOAB and VisIt have services to manage ghost layers used in parallel processing, it remains to be determined which approach is optimal from either a time or space performance perspective in producing a *first* plot after opening a new MOAB database.

In addition, like many other scientific data technologies both MOAB and VisIt rely to some extent upon *usage conventions*.
For example, in MOAB, there are [tables of conventional tag names](https://web.cels.anl.gov/projects/sigma/docs/moab/metadata.html#appendixA).
Likewise, in VisIt a time-series is little more than a list of names of files for individual time states obeying a predefined naming convention.
Determining the set of conventions appropriate for any given dataset is not always possible programmatically.
User intervention may be required which can lead to the need for tedious and repetitive user interface operations when frequently switching between MOAB source databases.

Finally, MOAB uses the [*single shared file (SSF)*](https://www.hdfgroup.org/2017/03/21/mif-parallel-io-with-hdf5/) parallel I/O paradigm which involves MPI *collective* calls whereas VisIt uses the [*multiple independent file (MIF)*](https://www.hdfgroup.org/2017/03/21/mif-parallel-io-with-hdf5/) parallel I/O paradigm which involves MPI *independent* calls.
The next section dives more deeply into this particular issue.

### Bridging SSF and MIF Parallel I/O Paradigms

VisIt's database subsystem is designed around the MIF parallel I/O paradigm.
In MIF, an upstream data producer once and for all pre-decomposes a massive mesh into `K` pieces, called *domains*, and stores the pieces among `M` files ([shard](https://en.wikipedia.org/wiki/Shard_(database_architecture))-like).
When processing the mesh on `R` MPI ranks, VisIt uses various [*load balance*](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/getting_started/Startup_Options.html#:~:text=Load%20balance%20options) algorithms to assign domains to ranks.
`K`, `M` and `R` can be chosen mostly independently allowing for significant flexibility in parallel resource allocation.
Typically, `K>>M` and `R≈K/n` where `n` is a small integer divisor of `K`, often 1.

Consequently, in MIF domains represent an *atomic unit of storage* at which VisIt makes problem-sized (or bulk) data requests.
All requests from VisIt to a plugin are parameterized in terms of a domain (and also a timestep) identifier.

For the MOAB plugin, a somewhat unique design question is what will constitute the all-important mesh domains.
In a MOAB (`.h5m`) file, mesh coordinates and connectivities are stored and expressed in one massive, monolithic global address space of mesh entities.
Except for a handful of simple, structured mesh cases, VisIt itself offers no help in decomposing a massive, monolithic, globally enumerated mesh into pieces for parallel processing.
Fortunately, MOAB combined with the *collective* parallel I/O capabilities of HDF5 does.
In the MOAB plugin, the partition sets identified by `PARALLEL_PARTITION` are used to define HDF5 dataset selections so that each MPI rank reads only the subset of the global mesh assigned to it during collective `H5Dread()` operations.

In every MOAB database (`.h5m` file) there exists a conventional tag named `PARALLEL_PARTITION` which identifies a collection of `K` entity sets.
These entity sets will serve as the all-important mesh domains for VisIt.
Typically, the `PARALLEL_PARTITION` tag is computed by an upstream partitioner such as [Zoltan](https://sandialabs.github.io/Zoltan/) or [METIS](https://github.com/KarypisLab/METIS).
The MOAB plugin uses this tag to define [HDF5 dataspace selections](https://support.hdfgroup.org/documentation/hdf5/latest/_h5_s__u_g.html) used in collective `H5Dread()` calls.
When `R>K`, some ranks will not read any entity set of `PARALLEL_PARTITION`.
When `R<K`, multiple entity sets will be read by the same rank.

### Resolving Other Differences

The remaining issues impacting users' ability to use VisIt to analyze MOAB data involve bridging the VisIt and MOAB data models.
MOAB Dense tags on 0D entities (nodes) are used to define *node-centered* (piecewise-linear interpolation) variables for VisIt.
Dense tags on >0D entities are used to define *zone-centered* (piecewise-constant interpolation) variables.
Length 1 tags define *scalar* variables whereas length 2 or 3 define *vector* variables and length >3 tags define array variables.
Entity sets for materials and boundary conditions get handled as *enumerated* subsets in VisIt.
With the exception of `PARALLEL_PARTITION`, sparse tags in MOAB are not yet supported in VisIt but will likely also involve creative uses of VisIt's enumerated subset functionality.

MOAB users often wish to manipulate the mesh in terms of different primitive entity types (e.g. 0D nodes, 1D edges, 2D faces and/or 3D volumes).
To support this in VisIt, a database read option allows users to set which dimensionality entities they wish to have included when the mesh is read.
When the same mesh is expressed with different types of entities, this can lead to additional challenges for users in selecting and combining plots in VisIt.

### VisIt and MOAB with MPAS and ROMS Ocean Models

The visualization above demonstrates the use of VisIt and MOAB in analyzing ocean data.
A coarse whole global ocean model, using polygonal elements (hexagons extruded in depth), is characterized by the [MPAS](https://mpas-dev.github.io/MPAS-Analysis/1.2.7/index.html) modeling and simulation application.
A handful of much higher resolution regional models (using structured ijk hexahedral meshes), outlined in red, are characterized by the [ROMS](https://www.pnnl.gov/projects/seahorce) modeling and simulation application.
Some insets represent critical regions of open ocean while others represent inland water bodies such as the Chesapeake Bay.
Both MPAS and ROMS use MOAB to store and manage the data and, in particular, to also handle coupling between the global and regional models.

The global ocean visualization, above, involves a number of different MOAB data sources and plots thereof together with VisIt's **Threshold** operator set to display different features of interest.
Then these multiple plots were layered, somewhat tediously, as concentric, spherical shells using VisIt's **Transform** operator with various [cmocean](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/using_visit/MakingItPretty/Color_tables.html#the-cmocean-color-tables) color maps applied.
This helps to provide context for individual inset regions depicted in insets at left.

Of the [150+ database plugins](https://github.com/visit-dav/visit/tree/develop/src/databases) in VisIt, [MOAB](https://github.com/visit-dav/visit/tree/develop/src/databases/MOAB) is the only plugin employing SSF collective parallel I/O via HDF5.

## Author Bios

Iulian Grindeanu is a computational scientist with more than two decades of experience in scientific computing, parallel algorithms, and mesh-based simulation technologies.
He has made significant contributions to MOAB's parallel infrastructure, distributed mesh algorithms, mesh intersection methods, and climate-modeling applications that rely on scalable mesh data structures and parallel I/O.

Vijay S. Mahadevan is a computational scientist at Argonne National Laboratory. His work focuses on scientific computing, mesh technologies, multiphysics coupling, and high-performance computing.
He is a principal contributor to the MOAB mesh infrastructure and related tools for scalable mesh and data management in large-scale simulation workflows.

Mark C. Miller is a retired computer scientist who continues to support the [SD](https://sd.llnl.gov) program at [LLNL](https://www.llnl.gov).
He is a contributor to [VisIt](https://visit.llnl.gov), [Silo](https://silo.llnl.gov) and [HDF5](https://www.hdfgroup.org).

<!---
Publish: Yes
Topics: High-Performance Computing (HPC)
Track: Experience
--->
