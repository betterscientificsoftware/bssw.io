# What is Debugging?

<!--deck start--->
Debugging in a well-known, important concept while developing software - discussed below are some topics that arise when one talks about debugging in scientific environments.
<!--deck end--->

<!--body start--->
Defects in software (e.g. _bugs_) can take many forms. Defects are generally described as causing
unexpected or unintended behavior including outright crashes, incorrect or invalid
results, missing or disabled functionality and unexpected time and/or space performance. <!-- [_time and/or space performance_](http://www.leda-tutorial.org/en/official/ch02s02s03.html). -->

The _first_ most important step in debugging is to develop a _reproducer_. That is, the _recipe_
by which the defective behavior can be reliably observed. It is common for a defect to manifest
only under certain software configurations which includes such things as the operating system, compiler,
third party libraries and various user-specific controls such as preferences, input gestures and commands
and input data. In complex situations involving large collections of interacting software components,
_reproducers_ can often be burdensome to develop. It is best when users and developers alike share this
burden. This is unnavoidable when the defect manifests in configurations that are inaccessible
to the software developers. Perhaps the most challenging of all defects to reproduce are those that
manifest only at large scale parallelism.

Once a _reproducer_ is available, the process of finding the cause can involve various creative
strategies, including the use of debugging tools such as [_gdb_](https://en.wikipedia.org/wiki/GNU_Debugger)
or [_TotalView_](https://hpc.llnl.gov/software/development-environment-software/totalview-debugger) (which require the software to have been compiled with debugging symbols included), performance assesement tools such as
[_Valgrind_](http://valgrind.org) or [_gprof_](https://sourceware.org/binutils/docs/gprof/Compiling.html),
intrusive code modifications (e.g. printf), and even simply eye-balling code to
identify possible candidate code paths that could lead to the observed defective behavior.

When UNclassified codes manifest defects in Classified environments, the debugging may be done in the
Classified environment but the correction still needs to be implemented in the UNclassified environment.
Defects arising out of unintended time and/or space performance can be particularly difficult to diagnose
and correct. For example, an _O(n^2)_ algorithm deep in the bowels of a large and complex application with
many dependencies may manifest noticeable performance behavior only for extremely large _n_, not typically
encountered in routine testing. When its practical to do so, it is good practice for
developers to add the _reproducer_ recipe to the software's routine testing so as to ensure the defect
won't creep back into the software in later versions. This practice is typically called _regression_ testing.

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
<!--body end--->

<!---
Publish: yes
Pinned: yes
Categories: reliability
Topics: debugging
Tags:
Level: 0
Prerequisites: none
Aggregate: none
--->
