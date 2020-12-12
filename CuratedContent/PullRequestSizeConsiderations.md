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

A Pull Request (PR) is a batch of *related* code changes on one branch of development
submitted for review prior to merging into another branch. The
[*size* of a PR](https://sourcelevel.io/blog/5-metrics-engineering-managers-can-extract-from-pull-requests)
is typically measured in terms of number of changes (files and/or lines of code). Some
of the ways in which PR size impacts software quality and productivity are...

* A good houskeeping attitude
(*while I am here fixing problem A, why don't I go ahead and also fix problem B*) leads to
mixing independent changes in the same PR and to larger PRs.
* The *bigger* the PR, the more work the *submitter* of the PR imposes upon the *reviewer(s)*.
* The larger the PR, the more difficult it will be for reviewers to schedule the time
needed to review it.
* The larger the PR, the more likely already overburden reviewers will
  * Put off even starting the review.
  * Give only a cursory (rubber-stamp) review defeating the whole purpose of review.
* There is an inverse correlation between PR size and defect
rate.<sup>[1](https://sback.it/publications/icse2018seip.pdf),
[2](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf),
[3](https://www.microsoft.com/en-us/research/wp-content/uploads/2015/05/PID3556473.pdf)</sup>
* Experience with
[Functional (or Feature) Breakdown Structure (FBS)](https://www.syngenics.com/papers/2009JPC5344F_AIAA_DeHoff.pdf)
(the cousin to
[Work Breakdown Structure](https://en.wikipedia.org/wiki/Work_breakdown_structure))
is a useful skill in breaking large changes into smaller, manageable steps.

It is a [best practice](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
to keep PRs small. The smaller the better. When many changes
are necessary as part of a major feature enhancement or a large refactoring effort,
it is a best practice to spread the changes over multiple PRs, each one representing
an independently useful, value-added contribution to the code base and which builds
towards the ultimate enhancement or refactor goal. But, planning and implementing
large software changes in this way is not always easily possible and even when it is,
it can impose impractical burdens on the submitter.

Consider the changes to migrate a large code base from Autotools to CMake for example.
When this was undertaken in VisIt in 2009,
[250K lines of code across 2,800+ files](https://github.com/visit-dav/visit/commit/4c9f66cdbbd0d311e24023da441024cf85de936b).
were changed. To split this across multiple PRs and branches (**note:**
[binary content in VisIt's Subversion repo at the time](https://bssw.io/blog_posts/continuous-technology-refreshment-an-introduction-using-recent-tech-refresh-experiences-on-visit) would have made this near impractical),
the team could have agreed to permit both build systems to temporarily co-exist
in the main line of development during a period of tansition. While the rest of the team
continued to operate on Autotools, developer(s) handling the migration to CMake could
have structured the changes over multiple intermediate phases...

* CMake doing some checks and no building
* CMake doing more checks and optionally building a small portion of the code base
* CMake doing more checks and optionally building a larger portion of the code base
* CMake doing all checks and optionally building the whole code base
* Autotools removed and CMake no longer optional

During this transition period, there would be agreement not to make any public releases
or change Autotools build logic in any significant way (small changes may have to be accomodated).
There is also probably a small amount of software engineering required to enable
the code base to temporarily operate in this intermediate state. The effort to develop
and maintain that temporary code is likely worth the impact it has on enabling the work
to be managed in smaller pieces. However, this is a *thinking cap* towards software
engineering/planning that is likely not too common across the HPC/CSE community.

For another illustrative example, it is also worth considering what is the *smallest*
size for a PR? Suppose some code was converted from Fortran to C and several off-by-one
indexing bugs escaped everyone's attention in the initial commit. Each represents a one-line
fix. Does it make sense to split each into its own PR? It could. On the other hand,
the overhead involved in creating branches and PRs, waiting for CI to run in each PR,
applying the changes to both a release candidate and a main line not to mention email
notifications and perhaps adding seperate bug-fix entries to a release notes file may be
more than its worth to separate each into its own PR.
