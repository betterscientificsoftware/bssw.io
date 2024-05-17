# What is Debugging?
#### Publication date: July 20, 2019


<!--deck start--->
Debugging in a well-known, important concept while developing software - discussed below are some topics that arise when one talks about debugging in scientific environments.
<!--deck end--->

<!--body start--->
Defects in software (e.g. *bugs*) can take many forms. Defects are generally described as causing
unexpected or unintended behavior including outright crashes, incorrect or invalid
results, missing or disabled functionality, and unexpected time and/or space performance

The *first* and most important step in debugging is to develop a *reproducer*. That is, the *recipe*
by which the defective behavior can be reliably observed. It is common for a defect to manifest
only under certain software configurations which include such things as the operating system, compiler, third-party libraries, and various user-specific controls such as preferences, input gestures and commands
and input data. In complex situations involving large collections of interacting software components,
*reproducers* can often be burdensome to develop. It is best when users and developers alike share this
burden. This is unavoidable when the defect manifests in configurations that are inaccessible
to the software developers. Perhaps the most challenging of all defects to reproduce are those that
manifest only at large-scale parallelism.

Once a *reproducer* is available, the process of finding the cause can involve various creative
strategies, including the use of debugging tools such as *[gdb](https://en.wikipedia.org/wiki/GNU_Debugger)*
or *[TotalView](https://hpc.llnl.gov/software/development-environment-software/totalview-debugger)* (which require the software to have been compiled with debugging symbols included), performance assesement tools such as
*[Valgrind](http://valgrind.org)* or *[gprof](https://sourceware.org/binutils/docs/gprof/Compiling.html)*,
intrusive code modifications (e.g. printf), and even simply eye-balling code to
identify possible candidate code paths that could lead to the observed defective behavior.

When UNclassified codes manifest defects in Classified environments, the debugging may be done in the
Classified environment but the correction still needs to be implemented in the UNclassified environment.
Defects arising out of unintended time and/or space performance can be particularly difficult to diagnose
and correct. For example, an *O(n^2)* algorithm deep in the bowels of a large and complex application with
many dependencies may manifest noticeable performance behavior only for extremely large *n*, not typically
encountered in routine testing. When its practical to do so, it is good practice for
developers to add the *reproducer* recipe to the software's routine testing so as to ensure the defect
won't creep back into the software in later versions. This practice is typically called *regression* testing.

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
<!--body end--->

<!---
Publish: yes
Pinned: yes
Topics: debugging
--->
