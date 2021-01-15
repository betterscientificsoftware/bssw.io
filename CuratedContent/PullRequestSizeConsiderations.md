# PR Size Matters

<!-- deck text start -->
Developers new to peer review via the Pull Request workflow supported by
hosting providers like GitHub, GitLab, etc., may not appreciate the
impact of the *size* of the PR on overall productivity of the team.
This article outlines some issues and provides some links to several
supporting articles about the impact of PR size on productivity.
<!-- deck text end --> 

#### Contributed by [Mark C. Miller](http://github.com/markcmiller86 "Mark C. Miller")
#### Publication date: Dec 12, 2020

By now, most HPC/CSE'ers are likely familiar with *pull requests*. That is
GitHub/Bitbucket parlance (GitLab uses *merge request*) for a batch of related
code changes on one branch of development submitted for *review* prior to
merging into another branch. For example, a PR might include all the changes
necessary to fix a bug or add a new feature. A key word in the preceding and
a key aspect of PRs is *review*. In fact, another way to think about the
PR acronym is that it stands for *peer review*.

When you are developing code, how often do you consider the impact on reviewers
in your design and development processes? How often do you wind up *adjusting* the
way you are changing a code base primarily to accommodate the review process? Do
you often wind up breaking a group of related changes across *multiple* PRs and
subsequently planning and executing associated development far differently than
you might have if you had treated them all in a single PR? If your answer to any
of these question is *not often* or *not ever*, you may be creating PRs that are
by industry standards and practices too large.

The
[*size* of a PR](https://sourcelevel.io/blog/5-metrics-engineering-managers-can-extract-from-pull-requests)
is typically measured in terms of number of files and/or lines of code (the sum of
counts of deleted lines, modified lines and added lines).
[Some research](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
suggests that more than 400 lines changed is considered *too large* for a single
*review*. Other research ([[1]], [[2]], [[3]]), suggests an inverse correlation between PR size
and defect rate. Reviewers suffer one or more of the following consequences the larger a
PR is...
* ...the more work reviewing the PR involves.
* ...the more difficult it is to divy up review work among multiple reviewers.
* ...the more difficult it is for reviewers to schedule time for review.
* ...the more likely reviewers will put off even starting the review.
* ...the more likely a first reviewer will give only a cursory review.
* ...the more likely second (and later) reviewers will either merely rubber-stamp an
already approved PR or not bother to start a review if changes have already been requested.

It is a [best practice](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
to keep PRs small. The smaller the better. This is particularly true in high 
[churn](https://www.pluralsight.com/blog/tutorials/code-churn) code bases.
A first commandment in this enterprise is to never mix unrelated changes in the
same PR. When many related changes are necessary as part of a major feature enhancement
or maybe a large refactoring effort, a second commandment is to split the changes
([[4]], [[5]], [[6]]) over multiple PRs,
each one representing an independently useful, value-added contribution to the code
base and which builds towards the ultimate enhancement or refactor goal.

Consider the changes to migrate a large code base from Autotools to CMake for example.
When this was undertaken in VisIt in 2009,
[250K lines of code across 2,800+ files](https://github.com/visit-dav/visit/commit/4c9f66cdbbd0d311e24023da441024cf85de936b)
were changed all committed in a single merge operation to the trunk.
To split this massive change across multiple PRs and branches (**note:**
[binary content in VisIt's Subversion repo at the time](https://bssw.io/blog_posts/continuous-technology-refreshment-an-introduction-using-recent-tech-refresh-experiences-on-visit) would have made this impractical),
the team could have agreed to a period of transition where both build systems
were allowed to temporarily coexist or where portions of the code base are temporarily
disabled or broken much like portions of a building or roadway system are closed during
remodeling or construction.

Experience with
[Functional (or Feature) Breakdown Structure (FBS)](https://www.syngenics.com/papers/2009JPC5344F_AIAA_DeHoff.pdf)
(the cousin to
[Work Breakdown Structure](https://en.wikipedia.org/wiki/Work_breakdown_structure) and
which might also be thought of as code *pre-factoring* as opposed to *refactoring*) and
*stacked pull requests* ([[7]], [[8]], [[9]], [[10]]),
are useful skills in breaking large changes into smaller, manageable steps. In addition,
learning to use an
[integration branch](https://www.toptal.com/git/git-workflows-for-pros-a-good-git-guide#integration-branch) 
workflow may be useful.
But, planning and implementing large software changes in small increments is not
always practical. Even when it is, it is important to keep in mind that there is a
*balance* of productivity concerns to manage here.

Always maximizing productivity for reviewers and the review process may create unwelcome
productivity issues for other developers and collaborators submitting PRs. So far,
we've focused on the productivity of the PR review process and what submitters can do
to minimize review effort. However, there are productivity costs for submitters too.

First, strict adherence to avoiding mixing unrelated changes in a single PR
may simply discourage some good housekeeping
(*while I am here fixing problem A, why don't I go ahead and also fix problem B*).
There is just a lot of overhead associated with splitting
changes over multiple PRs including creating branches and PRs, running and waiting
for CI in each PR, ensuring each PR is reviewed and merged in logical order and
possibly having to apply each PR's changes to multiple branches (e.g. release candidate and main).

In addition, when splitting large changes over multiple PRs, there can be some amount
of *transition-specific* software engineering required (design and coding work devoted
solely to holding things together *during* a major transition) which is later removed. 
This effort is needed *only* to support the software through multiple stages of a major
transition which would have otherwise been unnecessary. So, it represents extra work.

The point is, productivity for the project *overall* requires *balancing* all these concerns.
In some cases strict adherence to the principle of not mixing unrelated changes in a 
single PR may outweight the benefits of splitting such work across multiple PRs.
In other words, for very small bits of work (e.g. fixing a typo in a document), there may be
a minimum size PR below which the overheads of just managing the PR process become
the key productivity concern. Still, this should be something that is
discussed with the team ahead of submitting the changes.

The upshot is that keeping PRs as small as reasonably practical is a best practice. Investing
time up front to decide how to split large changes into manageable PRs that can be quickly
integrated into a large code base is as important as the design and coding work that goes
into the bug fixes and feature enhancements the changes are proposed for to begin with.

Some literature instead uses the concept of a 
[*reviewable unit of work*](https://insights.dice.com/2013/01/28/how-to-take-pain-out-of-code-reviews/)
to separate the concept of code review from how it is practiced in any particular tool.
A reviewable unit could be a
[PR, a commit, or a single file's patch/diff](https://gregoryszorc.com/blog/2020/01/07/problems-with-pull-requests-and-how-to-fix-them/).
In fact, long before GitHub introduced pull requests in 2008 (which was
in turn based on Git's [`request-pull`](https://git-scm.com/docs/git-request-pull) operation),
seasoned software professionals engaged in the conceptually equivalent processes using a
[patchwork of approaches and tools](https://www.cmcrossroads.com/article/pros-and-cons-four-kinds-code-reviews)
(or using something like [CodeStriker](http://codestriker.sourceforge.net) designed specifically for
code review) which often even included emailing around patchfiles.

Finally, while this
article relies heavily on the concept of branches in the revision control system, it is worth
pointing out that many commercial companies, including Google, don't use branches and instead
keep everything merged on a single,
[monolithic line of development (e.g. *trunk* or *mainline*)](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext).
In portions of the code base in transition, both new and old code paths commonly exist
simultaneously, controlled through the use of conditional flags, a practice that is highly
conducive to incorporating large changes in small, incremental pieces.

[1]: https://sback.it/publications/icse2018seip.pdf
[2]: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf
[3]: https://www.microsoft.com/en-us/research/wp-content/uploads/2015/05/PID3556473.pdf

[4]: https://www.thedroidsonroids.com/blog/splitting-pull-request
[5]: https://derwolfe.net/2016/01/23/splitting-up-pull-requests/
[6]: https://glennstovall.com/5-ways-to-carve-large-pull-requests-into-bite-sized-ones/

[7]: https://www.michaelagreiler.com/stacked-pull-requests/
[8]: https://divyanshu013.dev/blog/code-review-stacked-prs/
[9]: https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/
[10]: https://github.com/marketplace/stacked-pull-requests
