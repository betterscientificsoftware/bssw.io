# Pull Request (PR) Size Considerations

<!-- deck text start -->
Developers new to peer review via the Pull Request workflow supported by
hosting providers like GitHub, GitLab, etc., may not appreciate the
impact of the *size* of the PR on productivity. This article outlines some
issues and provides some links to several supporting articles about
the impact of PR size on productivity.
<!-- deck text end --> 

#### Contributed by [Mark C. Miller](http://github.com/markcmiller86 "Mark C. Miller")
#### Publication date: Dec 12, 2020

Resource information | Details
:--- | :--- 
Film name | Coded Bias
Presenter(s) | [Joy Buolamwini](https://en.wikipedia.org/wiki/Joy_Buolamwini), [Cathy O’Neil](https://en.wikipedia.org/wiki/Cathy_O%27Neil), [Safiya Umoja Noble](https://safiyaunoble.com), and others
Website | https://www.codedbias.com

A Pull Request (PR) is a batch of code changes on one branch of development
submitted for review prior to merging into another branch. Some of the impacts
of PR size on software quality and productivity are...

* The *bigger* the PR, the more work the *submitter* of the PR imposes upon the *reviewer(s)*.
* [Google](https://sback.it/publications/icse2018seip.pdf) and Microsoft
([A](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf,
[B](https://www.microsoft.com/en-us/research/wp-content/uploads/2015/05/PID3556473.pdf))
have research showing an inverse correlation between PR size and defect rate.
* The larger the PR, the more it encourages already overburden reviewers to give it only
a cursory (rubber-stamp) review instead of a thorough one which sort of defeats the whole
purpose of peer review.
* The larger the PR, the harder it is for a reviewer to schedule the time to review it. 
* The good houskeeping approach to work ("While I am here fixing problem A, let me go ahead
and also fix problem B) leads to mixing independent work in the same PR and to larger PRs.

It is a best practice to keep PRs small. The smaller the better. When many changes
are necessary as might be the case for a major feature enhancement or a large
refactoring effort, it is a best practice to spread the changes over many PRs,
each one representing an independently useful, value-added contribution to the code
base and which builds towards the ultimate enhancement or refactor goal. But,
planning and implementing the software changes in this way is not always easily
possible and even when it is, it can impose impractical burdens on the submitter.

For example consider migrating a large code base from Autotools to CMake.
When this work was undertaken on VisIt in 2009, 2,800+ files were changed as part
of a single merge commit in Subversion. But, this work could have been structured
across multiple PRs and branches (not
the way Subversion worked for us) by making the both CMake and Autotools live
together within the code base for a period of time. Building with CMake would
have been optional and initially, not very functional whereas continuing to 
build with Autotools would be still supported.

* Autotools + CMake (optional) doing only checks and no building
* Autotools + CMake (optional) building a small portion of the code base with either
* Autotools + CMake (optional) building a larger portion of the code base with either 
* Autotools + CMake (optional) building the whole code base with either
* Autotools removed and CMake no longer optional

The code base might remain in an intermediate state (Autotools + CMake optional for
some parts) for some mutually agreed upon period of time without harm. All developers,
except the submitter, continue to operate doing business with Autotools. If one of those
developers makes changes to a part of the Autotools build system that has already been
ported to CMake, that will have to be revisited.

There is probably a small amount of software engineering required to enable the code
base to operate in this intermediate state for a period of time and the effort to
develop and maintain that is worth the impact it has on enabling smaller chunks of
work.

Suppose some converted a routine from Fortran to C and there are
several instances of off-by-one indexing errors, each a one-line fix. Does
it make sense to split each into its own PR? If the overhead involved in
creating branches, running any local checks, etc. is high, the inclination
is to 

Depending on experience including potentially negative past experiences with
*branching* logistics in other VCSs, its an all too common practice for 
developers to combine many small, isolated, self-contained changes to be
glommed together into a single PR.

