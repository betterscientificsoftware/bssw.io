# Pull Request Size Matters

<!-- deck text start -->
Developers new to peer review via the Pull Request workflow supported by
hosting providers like GitHub, GitLab, etc., may not appreciate the
impact of the *size* of the Pull Request on overall productivity of the team.
This article outlines some issues and provides some links to several
supporting articles about the impact of Pull Request size on productivity.
<!-- deck text end --> 

#### Contributed by [Mark C. Miller](http://github.com/markcmiller86 "Mark C. Miller")
#### Publication date: Feb 18, 2021

By now, most HPC/CSE'ers are likely familiar with *pull requests (PR)*. That is
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
*size* of a PR<sup>[abd]</sup>
is typically measured in terms of number of files and/or lines of code (the sum of
counts of deleted lines, modified lines and added lines).
Some research<sup>[aac]</sup>
suggests that more than 400 lines changed is considered *too large* for a single
*review*. Other research,<sup>[aaa],[aab],[abc]</sup> suggests an inverse correlation between PR size
and defect rate. Reviewers suffer one or more of the following consequences the larger a
PR is...
* ...the more work reviewing the PR involves.
* ...the more difficult it is to divy up review work among multiple reviewers.
* ...the more difficult it is for reviewers to schedule time for review.
* ...the more likely reviewers will put off even starting the review.
* ...the more likely a first reviewer will give only a cursory review.
* ...the more likely second (and later) reviewers will either merely rubber-stamp an
already approved PR or not bother to start a review if changes have already been requested.

It is a best practice<sup>[aac]</sup>
to keep PRs small. The smaller the better. This is particularly true in high 
churn<sup>[ross]</sup> code bases.
A first commandment in this enterprise is to never mix unrelated changes in the
same PR. When many related changes are necessary as part of a major feature enhancement
or maybe a large refactoring effort, a second commandment is to split the changes<sup>[b],[c],[cc]</sup>
over multiple PRs, each one representing an independently useful, value-added contribution to the code
base and which builds towards the ultimate enhancement or refactor goal.

Consider the changes to migrate a large code base from VTK-6 to VTK-8.
When this was undertaken in VisIt in 2018,
450K lines of code across 2,000+ files<sup>[dave]</sup>
were changed all committed in a single merge operation to the main development branch.
To split this massive change across multiple PRs and branches (**note:**
binary content in VisIt's Subversion repo at the time<sup>[aae]</sup> would have made this impractical),
the team could have agreed to a period of transition where both VTK versions
were allowed to temporarily coexist or where portions of the code base were temporarily
disabled or broken much like portions of a building or roadway system are closed during
remodeling or construction.

Experience with
Functional (or Feature) Breakdown Structure (FBS)<sup>[15]</sup> (the cousin to
Work Breakdown Structure<sup>[16]</sup> and
which might also be thought of as code *pre-factoring* as opposed to *refactoring*) and
*stacked pull requests*<sup>[gorfo],[foo],[bar]</sup>
are useful skills in breaking large changes into smaller, manageable steps. In addition,
learning to use an integration branch<sup>[17]</sup> workflow may be useful.
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

The point is, productivity for the project *overall* requires
*balancing* all these concerns.<sup>[18]</sup>
In some cases strict adherence to the principle of not mixing unrelated changes in a 
single PR may outweigh the benefits of splitting such work across multiple PRs.
In other words, for very small bits of work (e.g. fixing a typo in a document), there may be
a minimum size PR below which the overheads of just managing the PR process become
the key productivity concern. Still, this should be something that is
discussed with the team ahead of submitting the changes.

The upshot is that keeping PRs as small as reasonably practical is a best practice. Investing
time up front to decide how to split large changes into manageable PRs that can be quickly
integrated into a large code base is as important as the design and coding work that goes
into the bug fixes and feature enhancements the changes are proposed for to begin with.

Some literature uses the notion of a *reviewable unit of work*<sup>[19]</sup>
to separate the concept of code review from how it is practiced in any particular tool.
A reviewable unit could be a
PR, a commit, or a single file's patch/diff.<sup>[mark]</sup>
In fact, long before GitHub introduced pull requests in 2008 (which was
in turn based on Git's `request-pull`<sup>[sue]</sup> operation),
seasoned software professionals engaged in the conceptually equivalent processes using a
patchwork of approaches and tools<sup>[rose]</sup>
(or using something like CodeStriker<sup>[e]</sup>) designed specifically for
code review) which often even included emailing around patchfiles.

Finally, some commercial companies such as Google claim not to use the branching mechanisms
in version control systems to manage code review. Instead, most new features and changes
in behavior are managed on a single, monolithic line of development<sup>[e],[f],[h]</sup>
(e.g. trunk or mainline) using *workspaces* (akin to a Subversion working-copy or a Git clone).
Both new and old code paths often coexist in the one and only main line of development
simultaneously, controlled by *toggle* flags, a practice that facilitates accepting large
changes in small, incremental steps. In all likelihood there are exceptions to this practice
for large and/or automated refactorings.

<!---
 Publish: yes
 Pinned: no
 Topics: revision control, development tools
 RSS update: 2021-02-18
 --->

<br>

[aaa]: https://sback.it/publications/icse2018seip.pdf "Modern Code Review: A Case Study at Google"
[aab]: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf "Characteristics of Useful Code Reviews: An Empirical Study at Microsoft"
[abc]: https://www.microsoft.com/en-us/research/wp-content/uploads/2015/05/PID3556473.pdf "Code Reviews Do Not Find Bugs: How the Current Code Review Best Practice Slows Us Down"
[b]: https://www.thedroidsonroids.com/blog/splitting-pull-request "How to Split Pull Requests – Good Practices, Methods and Git Strategies"
[c]: https://derwolfe.net/2016/01/23/splitting-up-pull-requests/ "Splitting Up Pull Requests"
[cc]: https://glennstovall.com/5-ways-to-carve-large-pull-requests-into-bite-sized-ones/ "5 Ways to Carve Large Pull Requests Into Bite-Sized Ones"
[gorfo]: https://www.michaelagreiler.com/stacked-pull-requests/ "Stacked pull requests: make code reviews faster, easier, and more effective"
[foo]: https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/ "Stacked Diffs Versus Pull Requests"
[bar]: https://github.com/marketplace/stacked-pull-requests "Stacked Pull Requests"
[abd]: https://sourcelevel.io/blog/5-metrics-engineering-managers-can-extract-from-pull-requests "5 metrics Engineering Managers can extract from Pull Requests"
[aac]: https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/ "Best Practices for Code Review"
[ross]: https://www.pluralsight.com/blog/tutorials/code-churn "What is Code Churn"
[dave]: https://github.com/visit-dav/visit/commit/110b95f270effecce04c9ce45a09aeee9ced5b22 "VisIt VTK Upgrade Commit"
[aae]: https://bssw.io/blog_posts/continuous-technology-refreshment-an-introduction-using-recent-tech-refresh-experiences-on-visit "What is Continuous Technology Refresh (CTR)"
[15]: https://www.syngenics.com/papers/2009JPC5344F_AIAA_DeHoff.pdf "The Functional Breakdown Structure (FBS) and Its Relationship to Life Cycle Cost"
[16]: https://en.wikipedia.org/wiki/Work_breakdown_structure "Work Breakdown Structure"
[17]: https://www.toptal.com/git/git-workflows-for-pros-a-good-git-guide#integration-branch "Git Integration Branch Workflow"
[18]: https://smallbusinessprogramming.com/optimal-pull-request-size/ "Optimal pull request size"
[19]: https://insights.dice.com/2013/01/28/how-to-take-pain-out-of-code-reviews/ "Take the Pain out of Code Reviews"
[mark]: https://gregoryszorc.com/blog/2020/01/07/problems-with-pull-requests-and-how-to-fix-them/ "Problems with Pull Requests and how to Fix them"
[sue]: https://git-scm.com/docs/git-request-pull "Documentation for Git Request Pull Command"
[rose]: https://www.cmcrossroads.com/article/pros-and-cons-four-kinds-code-reviews "Comparing Four Kinds of Reviews"
[e]: http://codestriker.sourceforge.net "CodeStriker Project Home Page"
[f]: https://dl.acm.org/doi/pdf/10.1145/2854146 "Google's Billion Lines of Code Repository"
[h]: https://news.ycombinator.com/item?id=13561096 "Hacker News commentary on Google's Billion Lines of Code Repository"
