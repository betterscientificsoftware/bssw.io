
The Mesh-Oriented datABase ([MOAB](https://sigma.mcs.anl.gov/moab-library/)) is a scalable, parallel, scientific computing software component for representing and operating upon mesh-based scientific data in-situ.
MOAB can handle structured and unstructured meshes and fields thereon consisting of elements in the finite element “zoo”, including polygons and polyhedra.
The MOAB API provides a scalable, parallel representation of many types of mesh-based scientific data and metadata.
MOAB is optimized for efficiency in space and time, processing mesh data either in aggregate parcels (or [shards](https://en.wikipedia.org/wiki/Shard_(database_architecture))) as well as iterations over individual mesh entities.
In addition, MOAB provides a means for high performance, scalable I/O of the mesh-based scientific data it is processing to and from files on disk.

One of the reasons MOAB is used to *write* scientific data to files, as opposed to simply operate upon it in memory, is to export its data to other software components in use in a larger simulation and modeling workflow.
A commonly used component in such workflows is a visualization tool such as [VisIt](https://visit.llnl.gov) or [ParaView](https://www.paraview.org).
VisIt is a scalable, parallel scientific visualization tool for visualizing and analyzing mesh-based scientific data either in files or in-situ.
VisIt is built on top of the Visualization ToolKit ([VTK](https://vtk.org)) and relies upon VTK for a majority of its functionality.
However, I/O in VisIt is handled by VisIt's own database architecture and *plugins*.

In this article, we describe our experiences developing a MOAB database plugin for VisIt.




