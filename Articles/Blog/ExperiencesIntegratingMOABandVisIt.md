## What are MOAB and VisIt?
The Mesh-Oriented datABase ([MOAB](https://sigma.mcs.anl.gov/moab-library/)) package is an in-situ, scalable, library for managing mesh-based scientific data.
It is optimized to process mesh data in bulk parcels (or [shards](https://en.wikipedia.org/wiki/Shard_(database_architecture))) or fine-grained iterations over subsets of mesh entities.
Some aspects of MOAB's design and data model are derived from earlier SciDAC efforts including the Terascale Simulation Tools and Technologies ([TSTT](https://www.researchgate.net/publication/259197545_The_TSTTM_Interface)) and the Interoperable Tools for Advanced Petascale Simulations ([ITAPS](https://www.osti.gov/biblio/971531/)) projects.
In addition, MOAB supports scalable I/O to and from [HDF5](https://support.hdfgroup.org/documentation/hdf5/latest/) and [PNETCDF](https://parallel-netcdf.github.io/) files.
These files are often used to export MOAB data to other software used in a larger workflow such as [VisIt](https://visit.llnl.gov) or [ParaView](https://www.paraview.org).

VisIt is a scalable scientific visualization tool for analyzing mesh-based scientific data either in files or in-situ.
Database plugins in VisIt use the Visualization ToolKit ([VTK](https://vtk.org)) grid (`vtkDataset`) and field (`vtkDataArray`) objects to marshal data from files on disk into VisIt's internal memory and parallel processing models.

In this article, we describe our experiences developing and using a MOAB database plugin for VisIt.
Funding from the OASIS project (and from xxx earlier projects) aims to facilitate collaborations between developers of tools such as VisIt and the broader scientific computing community.
These funding streams have supported a mutually beneficial collaboration between VisIt developers at LLNL and MOAB developers at ANL.

### The ITAPS Generic plugin

As part of the [ITAPS](https://markcmiller86.github.io/ITAPS/) project, a VisIt plugin supporting MOAB was first developed using the [iMesh](https://markcmiller86.github.io/ITAPS/software/iMesh_html/i_mesh_8h.html) interface.
`iMesh` defined a *generic* interface for any package providing any kind of unstructured, discrete meshing *service*.	
[MOAB](https://sigma.mcs.anl.gov/moab-library/), [GRUMMP](https://www.researchgate.net/publication/254313656_GRUMMP_User's_Guide) and [FMDB](https://scorec.rpi.edu/FMDB/) developers participating in ITAPS each implemented the `iMesh` interface to their respective packages.

VisIt's [ITAPS plugin](https://github.com/visit-dav/visit/tree/2.10RC/src/databases/ITAPS_C) could then be compiled against each `iMesh` implementation producing separate plugin instances for ITAPS-MOAB, ITAPS-GRUMMP and ITAPS-FMDB.
This work demonstrated a key goal of ITAPS, that a single implementation of some mesh service (visualization in this case) via `iMesh` could support multiple different mesh management packages.
With the ability to *read* from one implementation and *write* to another, this version of the plugin also demonstrated the use of `iMesh` to easily convert data between different mesh management packages.

This early version of the plugin was used successfully to examine a large MOAB [reactor model](https://publications.anl.gov/anlpubs/2013/10/76766.pdf#page=12) consisting of hundreds of thousands of subsets for various components of a novel nuclear fuel assembly.
However, as funding for the ITAPS SciDAC project ended, so did further development and support of the `iMesh` interface.
It was eventually removed from MOAB.
A new VisIt database plugin integrating *directly* with MOAB's native interface was needed.

### VisIt Database Plugin Basics

Some of the key routines to be implemented in a database plugin in VisIt are
* `void PopulateDatabaseMetaData(avtDatabaseMetaData *md, ...)`: is called *collectively* in parallel when *opening* a new database and intended to tease just enough information from the input database to prime VisIt's GUI with the names and types of objects available to visualize.
  The user also chooses the number of nodes, `N`, and MPI ranks, `R` for launching the parallel *engine*.
* `vtkDataSet* GetMesh(char const *meshName, ...)` and `vtkDataArray* GetVar(char const *varName, ...)`: are called *independently* in parallel and return VTK *grid* and *array* objects, respectively, holding the geometry+topology of the mesh as well as data for a variable that is 1:1 with either the points (e.g. *node-centere* variable) or cells (e.g. *zone-centered* variable) of the mesh. 

In designing a plugin, a developer has many choices which ultimately effect the performance and functionality VisIt will provide in visualizing and analyzing the data.

Except for simple cases, VisIt itself does not decompose a large, monolithic mesh into pieces for parallel processing.
Instead, it *piggy backs* off of a parallel decomposition an upstream data producer would have already created using the [Multiple Independent File (MIF) parallel I/O paradigm](https://www.hdfgroup.org/2017/03/21/mif-parallel-io-with-hdf5/).
In MIF, `K` pieces of mesh (also called *domains*) can be stored and distributed among `M` files (typically `K>>M`) and then processed by VisIt on `R` MPI ranks.
`K`, `M` and `R` are completely independently determined.
The user choses `R` when launching the VisIt *engine*.
For example, for `K=20` domains spread across `M=4` files, good choices for `R` are `R=20` (`R=K`), `R=10` (`R=K/2`), `R=5` (`R=K/4`) or `R=4` (`R=K/5`) though choosing `R=8` or `R=12` would be fine too except that this can lead to uneven load balance.
Typically `R<=K` though if `R>K`, VisIt still functions albeit less efficiently because `R-K` ranks will idle with no domains to process.

Each time VisIt needs to draw a plot, a list of domains *relevant* to the current plot, `K'<=K`, is computed.
This list, which can change from plot to plot, is sorted in increasing domain number.
The domains are assigned to MPI ranks according to various [*load balance*](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/getting_started/Startup_Options.html#:~:text=Load%20balance%20options) algorithms.
In turn, those MPI ranks then make independent (e.g. not *collective*) `GetMesh()` (and `GetVar()`) calls to the database plugin for pieces they are assigned.

### The MOAB Native plugin

In MOAB's native HDF5 format, a large mesh is stored as a monolithic whole single piece in a single file.
A MOAB *tag* named `PARALLEL_PARTITION` identifies the domain number (`[0...K-1]`) each element in the mesh belongs to.
Typically, this tag (aka a mesh *coloring*) is computed by an upstream partitioner such as [Zoltan](https://sandialabs.github.io/Zoltan/) or [METIS](https://github.com/KarypisLab/METIS).

When a file is being read, the MOAB plugin uses the `PARALLEL_PARTITION` tag to define [HDF5 dataspaces](https://support.hdfgroup.org/documentation/hdf5/latest/_h5_s__u_g.html) representing how each of the `K` domains are carved out of the whole dataset in the file.
Currently, the MOAB plugin requires that `R>=K` so that each MPI rank can be assigned at most, one domain.
When `R>K`, `R-K` ranks will idle.
**MCM: HOW DOES MOAB IDLE any of the `R-K` ranks yet still engage in collective I/O? Pass empty dataspaces on those ranks?**
**What happens when VisIt culls pieces that are known not to be involved in the current plot operation (e.g. slicing with domain spatial extents)? Have we tested this?**
MOAB then engages in [HDF5 collective read operations](https://support.hdfgroup.org/documentation/hdf5/latest/_intro_par_h_d_f5.html) where each of the `K` ranks reads its domain (specified by an HDF5 dataspace) of the *whole* mesh.
In this way, the MOAB database plugin, not VisIt, takes responsibility for breaking the whole mesh in the file into pieces to be processed by VisIt's parallel engine.
It is also worth mentioning here that in a data producer such as [E3SM](https://e3sm.org/), this process is essentially reversed; each MPI rank defines an HDF5 dataspace representing its part of the whole and then engages in a collective write operation producing a single, monolothic whole mesh object in a single file.

To affect the above behavior in VisIt, during the `PopulateDatabaseMetaData()` call, the MOAB database plugin informs VisIt that there is just one large piece and that it will do its own domain decomposition.
This has the effect of bypassing VisIt's *relevant* domains computation and forcing VisIt to always issue `GetMesh()` (and `GetVar()`) calls *collectively* on all MPI ranks.
In the plugin, MOAB native mesh and tag data is processed to create the equiavelent VTK `vtkDataSet` (for the mesh) and `vtkDataArray` (for a tag) objects to serve back up to VisIt in response to `GetMesh()` and `GetVar()` calls.

**TO DO**:
1. Tags vs. fields (interpolation schemes)
2. Entity set dimensions (points, edges, faces and volumes)
3. 

