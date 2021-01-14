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

By now, most HPC/CSE'ers are likely familiar with a *pull requests*. It is
GitHub/Bitbucket parlance (GitLab uses *merge request*) for a batch of related
code changes on one branch of development submitted for *review* prior to
merging into another branch. For example, a PR might include all the changes
necessary to fix a bug or add a new feature. A key word in the preceding and
a key aspect of PRs is *review*. In fact, another way to think about the
PR acronym is that it stands for *peer review*.

When you are developing code, how often do you consider the impact on reviewers
in your design and development processes? How often do you wind up *adjusting* the
way you are changing a code base primarily to accomodate the review process? Do
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
and defect rate. Reviewers suffer one or more of the follwing consequences the larger a
PR is...
* ...the more work reviewing the PR involves.
* ...the more difficult it is to divy up review work among multiple reviewers.
* ...the more difficult it is for reviewers to schedule time for review.
* ...the more likely reviewers will put off even starting the review.
* ...the more likely a first reviewer will give only a cursory review.
* ...the more likely second (and later) reviewers will either merely rubber-stamp an
already approved PR or not bother to start a review if changes have already been requested.

It is a [best practice](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
to keep PRs small. The smaller the better. When many changes
are necessary as part of a major feature enhancement or a large refactoring effort,
it is a best practice to spread the changes over multiple PRs, each one representing
an independently useful, value-added contribution to the code base and which builds
towards the ultimate enhancement or refactor goal.

Consider the changes to migrate a large code base from Autotools to CMake for example.
When this was undertaken in VisIt in 2009,
[250K lines of code across 2,800+ files](https://github.com/visit-dav/visit/commit/4c9f66cdbbd0d311e24023da441024cf85de936b).
were changed. To split this massive change across multiple PRs and branches (**note:**
[binary content in VisIt's Subversion repo at the time](https://bssw.io/blog_posts/continuous-technology-refreshment-an-introduction-using-recent-tech-refresh-experiences-on-visit) would have made this impractical),
the team could have agreed to a period of transition where both build systems
were allowed to temporarily coexist or where portions of the code base are temporarily
disabled or broken much like portions of a building or roadway system are closed during
remodeling or construction.

Experience with
[Functional (or Feature) Breakdown Structure (FBS)](https://www.syngenics.com/papers/2009JPC5344F_AIAA_DeHoff.pdf)
(the cousin to
[Work Breakdown Structure](https://en.wikipedia.org/wiki/Work_breakdown_structure) and
which might also be thought of as code *pre-factoring* as opposed to *refactoring*),
is a useful skill in breaking large changes into smaller, manageable steps In addition,
learning to use an
[integration branch](https://www.toptal.com/git/git-workflows-for-pros-a-good-git-guide#integration-branch) 
workflow may be useful.
But, planning and implementing large software changes in small increments is not
always practical. Even when it is, it is important to keep in mind that there is a
*balance* of productivity concerns to manage here.

So far, we've focused on the productivity of the PR review process and what submitters
can/should do to minimize the effort of review. However, there are productivity costs
for submitters too. First, this approach really discourages a good whousekeeping attitude
(*while I am here fixing problem A, why don't I go ahead and also fix problem B*) because
it leads to mixing unrelated changes and to larger PRs. Next, there is just a lot of
overhead associated with multiple PRs including creating branches
and PRs, running and waiting for CI on those PRs, ensuring the PRs are probably handled in
logical order, handling change requests and waiting for reviewers to approve each PR, potentially
applying changes to multiple branches.

In addition, there can be some amount
of *transition-specific* software engineering required (designing and coding work devoted
solely to holding things together) *during* a major transition which is later removed. The
point is, overall project productivity requires *balancing* all these concerns meaning that
in some cases where it might make some sense to split work across multiple PRs, the costs
in so doing may outweigh the benefits. But, this should be something that is discussed with
the team ahead of the changes.

While this article was focused on pull requests, some literature instead uses the concept of a 
[*reviewable unit of work*](https://insights.dice.com/2013/01/28/how-to-take-pain-out-of-code-reviews/)
to separate the concept of code review from the implementation. A reviewable unit could be a PR,
a commit, a patch/diff. In fact, long before GitHub introduced pull requests in 2008 (which was
in turn based on Git's *request pull* functionality), seasoned software professionals enaged in
the conceptually equivalent processes using a
[patchwork of tools](https://www.cmcrossroads.com/article/pros-and-cons-four-kinds-code-reviews)
(or something like [CodeStriker](http://codestriker.sourceforge.net))
which sometimes even included emailing around patchfiles.

* [splitting](https://www.thedroidsonroids.com/blog/splitting-pull-request)
* [Stacked Pull Requests](https://www.michaelagreiler.com/stacked-pull-requests/)
* [More on stacked PRs](https://divyanshu013.dev/blog/code-review-stacked-prs/)
* [Stacked Diffs](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/)
* [Useful Git Commands for Splitting a PR that has become unmanabeable](https://derwolfe.net/2016/01/23/splitting-up-pull-requests/)
* [Temporary SE (scaffolding) strategies](https://glennstovall.com/5-ways-to-carve-large-pull-requests-into-bite-sized-ones/)
* [GitHub API tools](https://github.com/marketplace/stacked-pull-requests)
* [Google's Billion Lines of Code](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext)
* [churn](https://textexpander.com/blog/what-is-code-churn-and-how-to-reduce-it/)
* [reviewable unit](https://insights.dice.com/2013/01/28/how-to-take-pain-out-of-code-reviews/)

[1]: https://sback.it/publications/icse2018seip.pdf
[2]: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf
[3]: https://www.microsoft.com/en-us/research/wp-content/uploads/2015/05/PID3556473.pdf

