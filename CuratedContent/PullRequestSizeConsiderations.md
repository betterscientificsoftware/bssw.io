# Pull Requests: Size Does Matter

<!-- deck text start -->
Developers new to peer review via the Pull Request workflow supported by
hosting providers like GitHub, GitLab, etc., may not appreciate the
impact of the *size* of the PR on overall productivity of the team.
This article outlines some issues and provides some links to several
supporting articles about the impact of PR size on productivity.
<!-- deck text end --> 

#### Contributed by [Mark C. Miller](http://github.com/markcmiller86 "Mark C. Miller")
#### Publication date: Dec 12, 2020

A Pull Request (PR) is a batch of *related* code changes on one branch of development
submitted for review prior to merging into another branch. The
[*size* of a PR](https://sourcelevel.io/blog/5-metrics-engineering-managers-can-extract-from-pull-requests)
is typically measured in terms of number of files and/or lines of code (the sum of
counts of delete lines, modified lines and added lines).
[Some research](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
suggests that more than 400 lines of code changed is considered *too large* for a single
review. Other research suggests an inverse correlation between PR size and defect
rate.<sup>[1](https://sback.it/publications/icse2018seip.pdf),
[2](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf),
[3](https://www.microsoft.com/en-us/research/wp-content/uploads/2015/05/PID3556473.pdf)</sup>

Some of the ways in which PR size can impact software quality and productivity are
described below. The bigger a PR is...
* ...the more work reviewing the PR involves.
* ...the harder it is to divy up review work.
* ...the more difficult it is for reviewers to fit the review into their schedules.
* ...the more likely reviewers will put off even starting the review.
* ...the more likely a first reviewer will give only a cursory review.
* ...the more likely a second reviewer will merely rubber-stamp a review already approved by another reviewer.


* Experience with
[Functional (or Feature) Breakdown Structure (FBS)](https://www.syngenics.com/papers/2009JPC5344F_AIAA_DeHoff.pdf)
(the cousin to
[Work Breakdown Structure](https://en.wikipedia.org/wiki/Work_breakdown_structure))
is a useful skill in breaking large changes into smaller, manageable steps.
* A good housekeeping attitude
(*while I am here fixing problem A, why don't I go ahead and also fix problem B*) leads to
mixing independent changes in the same PR and to larger PRs.

It is a [best practice](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
to keep PRs small. The smaller the better. When many changes
are necessary as part of a major feature enhancement or a large refactoring effort,
it is a best practice to spread the changes over multiple PRs,

**note to self**: some literature uses the concept of a "reviewable unit" to try to be more workflow
agnostic. A reviewable unit could be a PR, a commit, a patch or diff.

 each one representing
an independently useful, value-added contribution to the code base and which builds
towards the ultimate enhancement or refactor goal. But, planning and implementing
large software changes in this way is not always easily possible and even when it is,
it can impose impractical burdens on the submitter.

Consider the changes to migrate a large code base from Autotools to CMake for example.
When this was undertaken in VisIt in 2009,
[250K lines of code across 2,800+ files](https://github.com/visit-dav/visit/commit/4c9f66cdbbd0d311e24023da441024cf85de936b).
were changed. To split this across multiple PRs and branches (**note:**
[binary content in VisIt's Subversion repo at the time](https://bssw.io/blog_posts/continuous-technology-refreshment-an-introduction-using-recent-tech-refresh-experiences-on-visit) would have made this impractical),
the team could have agreed to permit both build systems to temporarily co-exist
in the main line of development during a period of tansition. While the rest of the team
continued to operate on Autotools, developer(s) handling the migration to CMake could
have structured the changes over multiple intermediate phases...

* CMake doing some checks and no building
* CMake doing more checks and optionally building a small portion of the code base
* CMake doing more checks and optionally building a larger portion of the code base
* CMake doing all checks and optionally building the whole code base
* Autotools removed and CMake no longer optional

**notes to self**
* May be acceptable to team to allow portions of the code base to be temporarily broken
during intermediate phases too...much like portions of a building or roads may be closed
during re-modeling and construction.
* Does it make sense to use the term "pre-factoring" here?
* Good refs.
  * https://www.thedroidsonroids.com/blog/splitting-pull-request
* What if your pushing one PR in a series and the reviewers don't know this? They
may likely wonder why you've pushed the PR without having an idea where your headed.
* analogy with home remodeling
* code you are aiming to merge into is changing...more time = more changes to have to integrate
* idea about an "integration" branch

During this transition period, there would be agreement not to make any public releases
or change Autotools build logic in any significant way (small changes could be accomodated).
There is also probably a small amount of software engineering required to enable
the code base to temporarily operate in this intermediate state. The effort to develop
and maintain that temporary code is likely worth the impact it has on enabling the work
to be managed in smaller pieces. However, this is a *thinking cap* towards software
engineering/planning that is likely not too common across the HPC/CSE community.

For another illustrative example, it is also worth considering what is the *smallest*
size for a PR? Suppose some code was converted from Fortran to C and several off-by-one
indexing bugs crept in. Each represents a one-line fix. Does it make sense to split each
into its own PR? It could. On the other hand, the overhead involved of creating branches
and PRs, running and waiting for CI, applying the changes to both a release and development
branch and perhaps adding seperate entries to a release notes file not to mention all the
additional notification traffic may be more than its worth.

Methods for handling

* [Stacked Pull Requests](https://www.michaelagreiler.com/stacked-pull-requests/)
* [More on stacked PRs](https://divyanshu013.dev/blog/code-review-stacked-prs/)
* [Stacked Diffs](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/)
* [Useful Git Commands for Splitting a PR that has become unmanabeable](https://derwolfe.net/2016/01/23/splitting-up-pull-requests/)
* [Temporary SE (scaffolding) strategies](https://glennstovall.com/5-ways-to-carve-large-pull-requests-into-bite-sized-ones/)
* [GitHub API tools](https://github.com/marketplace/stacked-pull-requests)
* [Google's Billion Lines of Code](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext)
