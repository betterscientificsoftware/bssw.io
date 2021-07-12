---
layout: page
header:
  image_fullwidth: gallery-07a.png
permalink: "/contributors/"
foo: gorfo
---
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
*size* of a PR<sup>[10]</sup>
is typically measured in terms of number of files and/or lines of code (the sum of
counts of deleted lines, modified lines and added lines).
Some research<sup>[11]</sup>
suggests that more than 400 lines changed is considered *too large* for a single
*review*. Other research,<sup>[1],[2],[3]</sup> suggests an inverse correlation between PR size
and defect rate. Reviewers suffer one or more of the following consequences the larger a
PR is...
* ...the more work reviewing the PR involves.
* ...the more difficult it is to divy up review work among multiple reviewers.
* ...the more difficult it is for reviewers to schedule time for review.
* ...the more likely reviewers will put off even starting the review.
* ...the more likely a first reviewer will give only a cursory review.
* ...the more likely second (and later) reviewers will either merely rubber-stamp an
already approved PR or not bother to start a review if changes have already been requested.

It is a best practice<sup>[11]</sup>
to keep PRs small. The smaller the better. This is particularly true in high 
churn<sup>[12]</sup> code bases.
A first commandment in this enterprise is to never mix unrelated changes in the
same PR. When many related changes are necessary as part of a major feature enhancement
or maybe a large refactoring effort, a second commandment is to split the changes<sup>[4],[5],[6]</sup>
over multiple PRs, each one representing an independently useful, value-added contribution to the code
base and which builds towards the ultimate enhancement or refactor goal.

Consider the changes to migrate a large code base from VTK-6 to VTK-8.
When this was undertaken in VisIt in 2018,
450K lines of code across 2,000+ files<sup>[13]</sup>
were changed all committed in a single merge operation to the main development branch.
To split this massive change across multiple PRs and branches (**note:**
binary content in VisIt's Subversion repo at the time<sup>[14]</sup> would have made this impractical),
the team could have agreed to a period of transition where both VTK versions
were allowed to temporarily coexist or where portions of the code base were temporarily
disabled or broken much like portions of a building or roadway system are closed during
remodeling or construction.

Experience with
Functional (or Feature) Breakdown Structure (FBS)<sup>[15]</sup> (the cousin to
Work Breakdown Structure<sup>[16]</sup> and
which might also be thought of as code *pre-factoring* as opposed to *refactoring*) and
*stacked pull requests*<sup>[7],[8],[9]</sup>
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

Some literature uses the notion of a “reviewable unit of work”<sup>[19]</sup>
to separate the concept of code review from how it is practiced in any particular tool.
A reviewable unit could be a
PR, a commit, or a single file's patch/diff.<sup>[20]</sup>
In fact, long before GitHub introduced pull requests in 2008 (which was
in turn based on Git's `request-pull`<sup>[21]</sup> operation),
seasoned software professionals engaged in the conceptually equivalent processes using a
patchwork of approaches and tools<sup>[22]</sup>
(or using something like CodeStriker<sup>[23]</sup>) designed specifically for
code review) which often even included emailing around patchfiles.

Finally, some commercial companies such as Google claim not to use the branching mechanisms
in version control systems to manage code review. Instead, most new features and changes
in behavior are managed on a single, monolithic line of development<sup>[23],[24],[25]</sup>
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

[1-sfer-ezikiw]: https://sback.it/publications/icse2018seip.pdf “Modern Code Review: A Case Study at Google”
[2-sfer-ezikiw]: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf "Characteristics of Useful Code Reviews: An Empirical Study at Microsoft"
[3-sfer-ezikiw]: https://www.microsoft.com/en-us/research/wp-content/uploads/2015/05/PID3556473.pdf "Code Reviews Do Not Find Bugs: How the Current Code Review Best Practice Slows Us Down"
[4-sfer-ezikiw]: https://www.thedroidsonroids.com/blog/splitting-pull-request "How to Split Pull Requests – Good Practices, Methods and Git Strategies"
[5-sfer-ezikiw]: https://derwolfe.net/2016/01/23/splitting-up-pull-requests/ "Splitting Up Pull Requests"
[6-sfer-ezikiw]: https://glennstovall.com/5-ways-to-carve-large-pull-requests-into-bite-sized-ones/ "5 Ways to Carve Large Pull Requests Into Bite-Sized Ones"
[7-sfer-ezikiw]: https://www.michaelagreiler.com/stacked-pull-requests/ "Stacked pull requests: make code reviews faster, easier, and more effective"
[8-sfer-ezikiw]: https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/ ‘Stacked Diffs Versus Pull Requests’
[9-sfer-ezikiw]: https://github.com/marketplace/stacked-pull-requests "Stacked Pull Requests"
[10-sfer-ezikiw]: https://sourcelevel.io/blog/5-metrics-engineering-managers-can-extract-from-pull-requests "5 metrics Engineering Managers can extract from Pull Requests"
[11-sfer-ezikiw]: https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/ "Best Practices for Code Review"
[12-sfer-ezikiw]: https://www.pluralsight.com/blog/tutorials/code-churn "What is Code Churn"
[13-sfer-ezikiw]: https://github.com/visit-dav/visit/commit/110b95f270effecce04c9ce45a09aeee9ced5b22 "VisIt VTK Upgrade Commit"
[14-sfer-ezikiw]: https://bssw.io/blog_posts/continuous-technology-refreshment-an-introduction-using-recent-tech-refresh-experiences-on-visit "What is Continuous Technology Refresh (CTR)"
[15-sfer-ezikiw]: https://www.syngenics.com/papers/2009JPC5344F_AIAA_DeHoff.pdf "The Functional Breakdown Structure (FBS) and Its Relationship to Life Cycle Cost"
[16-sfer-ezikiw]: https://en.wikipedia.org/wiki/Work_breakdown_structure "Work Breakdown Structure"
[17-sfer-ezikiw]: https://www.toptal.com/git/git-workflows-for-pros-a-good-git-guide#integration-branch "Git Integration Branch Workflow"
[18-sfer-ezikiw]: https://smallbusinessprogramming.com/optimal-pull-request-size/ "Optimal pull request size"
[19-sfer-ezikiw]: https://insights.dice.com/2013/01/28/how-to-take-pain-out-of-code-reviews/ "Take the Pain out of Code Reviews"
[20-sfer-ezikiw]: https://gregoryszorc.com/blog/2020/01/07/problems-with-pull-requests-and-how-to-fix-them/ "Problems with Pull Requests and how to Fix them"
[21-sfer-ezikiw]: https://git-scm.com/docs/git-request-pull "Documentation for Git Request Pull Command"
[22-sfer-ezikiw]: https://www.cmcrossroads.com/article/pros-and-cons-four-kinds-code-reviews "Comparing Four Kinds of Reviews"
[23-sfer-ezikiw]: http://codestriker.sourceforge.net "CodeStriker Project Home Page"
[24-sfer-ezikiw]: https://dl.acm.org/doi/pdf/10.1145/2854146 "Google's Billion Lines of Code Repository"
[25-sfer-ezikiw]: https://news.ycombinator.com/item?id=13561096 "Hacker News commentary on Google's Billion Lines of Code Repository"
<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "“Modern Code Review: A Case Study at Google”"
[2]: #sfer-ezikiw-2 "Characteristics of Useful Code Reviews: An Empirical Study at Microsoft"
[3]: #sfer-ezikiw-3 "Code Reviews Do Not Find Bugs: How the Current Code Review Best Practice Slows Us Down"
[4]: #sfer-ezikiw-4 "How to Split Pull Requests – Good Practices, Methods and Git Strategies"
[5]: #sfer-ezikiw-5 "Splitting Up Pull Requests"
[6]: #sfer-ezikiw-6 "5 Ways to Carve Large Pull Requests Into Bite-Sized Ones"
[7]: #sfer-ezikiw-7 "Stacked pull requests: make code reviews faster, easier, and more effective"
[8]: #sfer-ezikiw-8 "‘Stacked Diffs Versus Pull Requests’"
[9]: #sfer-ezikiw-9 "Stacked Pull Requests"
[10]: #sfer-ezikiw-10 "5 metrics Engineering Managers can extract from Pull Requests"
[11]: #sfer-ezikiw-11 "Best Practices for Code Review"
[12]: #sfer-ezikiw-12 "What is Code Churn"
[13]: #sfer-ezikiw-13 "VisIt VTK Upgrade Commit"
[14]: #sfer-ezikiw-14 "What is Continuous Technology Refresh (CTR)"
[15]: #sfer-ezikiw-15 "The Functional Breakdown Structure (FBS) and Its Relationship to Life Cycle Cost"
[16]: #sfer-ezikiw-16 "Work Breakdown Structure"
[17]: #sfer-ezikiw-17 "Git Integration Branch Workflow"
[18]: #sfer-ezikiw-18 "Optimal pull request size"
[19]: #sfer-ezikiw-19 "Take the Pain out of Code Reviews"
[20]: #sfer-ezikiw-20 "Problems with Pull Requests and how to Fix them"
[21]: #sfer-ezikiw-21 "Documentation for Git Request Pull Command"
[22]: #sfer-ezikiw-22 "Comparing Four Kinds of Reviews"
[23]: #sfer-ezikiw-23 "CodeStriker Project Home Page"
[24]: #sfer-ezikiw-24 "Google's Billion Lines of Code Repository"
[25]: #sfer-ezikiw-25 "Hacker News commentary on Google's Billion Lines of Code Repository"
### References <!-- (sfer-ezikiw) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[“Modern Code Review: A Case Study at Google”](https://sback.it/publications/icse2018seip.pdf)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[Characteristics of Useful Code Reviews: An Empirical Study at Microsoft](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[Code Reviews Do Not Find Bugs: How the Current Code Review Best Practice Slows Us Down](https://www.microsoft.com/en-us/research/wp-content/uploads/2015/05/PID3556473.pdf)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[How to Split Pull Requests – Good Practices, Methods and Git Strategies](https://www.thedroidsonroids.com/blog/splitting-pull-request)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[Splitting Up Pull Requests](https://derwolfe.net/2016/01/23/splitting-up-pull-requests/)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[5 Ways to Carve Large Pull Requests Into Bite-Sized Ones](https://glennstovall.com/5-ways-to-carve-large-pull-requests-into-bite-sized-ones/)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[Stacked pull requests: make code reviews faster, easier, and more effective](https://www.michaelagreiler.com/stacked-pull-requests/)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[‘Stacked Diffs Versus Pull Requests’](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/)
* <a name="sfer-ezikiw-9"></a><sup>9</sup>[Stacked Pull Requests](https://github.com/marketplace/stacked-pull-requests)
* <a name="sfer-ezikiw-10"></a><sup>10</sup>[5 metrics Engineering Managers can extract from Pull Requests](https://sourcelevel.io/blog/5-metrics-engineering-managers-can-extract-from-pull-requests)
* <a name="sfer-ezikiw-11"></a><sup>11</sup>[Best Practices for Code Review](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
* <a name="sfer-ezikiw-12"></a><sup>12</sup>[What is Code Churn](https://www.pluralsight.com/blog/tutorials/code-churn)
* <a name="sfer-ezikiw-13"></a><sup>13</sup>[VisIt VTK Upgrade Commit](https://github.com/visit-dav/visit/commit/110b95f270effecce04c9ce45a09aeee9ced5b22)
* <a name="sfer-ezikiw-14"></a><sup>14</sup>[What is Continuous Technology Refresh (CTR)](https://bssw.io/blog_posts/continuous-technology-refreshment-an-introduction-using-recent-tech-refresh-experiences-on-visit)
* <a name="sfer-ezikiw-15"></a><sup>15</sup>[The Functional Breakdown Structure (FBS) and Its Relationship to Life Cycle Cost](https://www.syngenics.com/papers/2009JPC5344F_AIAA_DeHoff.pdf)
* <a name="sfer-ezikiw-16"></a><sup>16</sup>[Work Breakdown Structure](https://en.wikipedia.org/wiki/Work_breakdown_structure)
* <a name="sfer-ezikiw-17"></a><sup>17</sup>[Git Integration Branch Workflow](https://www.toptal.com/git/git-workflows-for-pros-a-good-git-guide#integration-branch)
* <a name="sfer-ezikiw-18"></a><sup>18</sup>[Optimal pull request size](https://smallbusinessprogramming.com/optimal-pull-request-size/)
* <a name="sfer-ezikiw-19"></a><sup>19</sup>[Take the Pain out of Code Reviews](https://insights.dice.com/2013/01/28/how-to-take-pain-out-of-code-reviews/)
* <a name="sfer-ezikiw-20"></a><sup>20</sup>[Problems with Pull Requests and how to Fix them](https://gregoryszorc.com/blog/2020/01/07/problems-with-pull-requests-and-how-to-fix-them/)
* <a name="sfer-ezikiw-21"></a><sup>21</sup>[Documentation for Git Request Pull Command](https://git-scm.com/docs/git-request-pull)
* <a name="sfer-ezikiw-22"></a><sup>22</sup>[Comparing Four Kinds of Reviews](https://www.cmcrossroads.com/article/pros-and-cons-four-kinds-code-reviews)
* <a name="sfer-ezikiw-23"></a><sup>23</sup>[CodeStriker Project Home Page](http://codestriker.sourceforge.net)
* <a name="sfer-ezikiw-24"></a><sup>24</sup>[Google's Billion Lines of Code Repository](https://dl.acm.org/doi/pdf/10.1145/2854146)
* <a name="sfer-ezikiw-25"></a><sup>25</sup>[Hacker News commentary on Google's Billion Lines of Code Repository](https://news.ycombinator.com/item?id=13561096)
