# A Proposed Alternative Editorial Workflow for BSSw.io Curated Content

This description of workflow for content development of Curated Content ideas
is based entirely on [earlier workflow document](CuratedContentEditorialWorkflow.md).

A key difference in this alternative workflow is that it explicitly requires
**EB Members** to engage in specific activities on a routine basis, in particular
a weekly progress meeting.

Below, we describe the *states* a Curated Content issue can
move through from inception to disposition. In each state, there are only a few
*directions* (e.g. new states) an issue may move. Those are the bullets under
each of the numbered steps in the description below.

# Actors
* **Anyone** who can submit a GitHub issue can use this approach to suggest a curated content topic.
* **Editorial Board Member**
* **Author** who can submit a pull request with a draft of the article, possibly from a fork.
* **Editorial Assistant** is a role that was first recognized in the blog workflow.
  It is someone familiar with the BSSw.io site and its operations, but who does not
  need to have the technical expertise to evaluate content that an editorial board
  member or subject matter expert would be expected to have.

# Curated Content States

1. **Anyone** with a GitHub account may submit ideas for curated content articles
   using curated content issue template by anyone with a GitHub account.
1. **EB Members** meet every other week for a half-hour meeting to consider new
   issue submissions, update on progress of current content development tasks, assign
   members new work. During such meetings, the **EB Member** leading the meeting for that
   day performs various GitHub tasks using a shared screen including
   * Leading discussion of *new issues* since last meeting.
   * Adjusting labels on issues.
   * Moving issues to various columns of the Content Development project board.
   * Assigning issues.
   * Creating and assigning milestones to various issues.
   * Recording notes on progress in comments of various items in progress.
   * Merging to master any PRs that are known ready.
1. New issues are reviewed and one of the following actions is taken:
   * The issue is rejected for one of a variety of reasons. The reason is
     recorded in a comment and the issue is labeled as `wontdo` and closed.
   * The issue is considered a candidate for further development and moved to
     *Topic Review*.
1. Issues in *Topic Review* are handled as follows
   * Any more than 30 days old that have garnered insufficient interest are labeled
     as `no-interest` and closed.
   * Any issues with sufficient interest are moved to *In Progress*. An **EB Member**
     which must be different than the actual **Author** is assigned. The author is
     indicated by @ mention in the issue comments a deadline is set by assigning a
     milestone.
1. Issues in *In Progress* are handled as follows
   * Issues in jeopardy of making deadline are reviewed and discussed. Authors are
     nudged and/or deadlines are adjusted.
   * Issues that are woefully beyond deadline are labeled as `no-development` and closed.
   * Issues for which a PR has been submitted are moved to *Item Review* and 1 reviewer
     is assigned.
1. Issues in *Item Review* are handled as follows
   * Unapproved PRs are reviewed on the spot and approved or not. If no approval is
     forthcoming, revisions required by author are explained in review comments in the
     PR (if they have not already py preceding review(s))
   * Approved PRs
     * **Editorial Assistance** review is requested assigning an **EA**.
     * **EA** may request or explicitly revise the content with commits to the PR.
     * **Author** should indicate approval (or not) of any changes made by **EA** via
       comments in the PR.
   * Approved PRs with **EA** and **Author** approval are merged and metadata is added
     in preparation for publication.
1. Milestones (deadlines) are reviewed to ensure any items intended for a given
   date are either completed, have reliable commitments they will be completed
   by deadline or are re-assigned a new milestone deadline.

# Editorial Workflow

The section above describes the various states *Curated Content* may move through.
The actual workflow of **EB Members** during weekly meetings is really the *reverse*
of the above steps. Working from the
[*project board*](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/projects/3),
**EB Members** work *first* with issues in the *right-most*, *Item Review* column.
and subsequently issues in columns further to the left.

## Notes

###### Light Weight Process for Authors
It is important to keep in mind that we aim for a light-weight process here, particularly
for *Authors* submitting content. Towards this end, we ask **EB Members** to exercise
discretion in the degree of commentary and engagement with *Authors* on GitHub perhaps
leaving the work to the assigned **EB Member**. A short list of criteria to be watching
for is
* Unnecessarily critical or negative tone associated with specific projects or people
* Significant factual inaccuracies or departures from widely adopted standards of practice.
* Substantially lacking in relevance to HPC/CSE software development.

###### Quantization of Progress
The key challenge in this process is the *iteration rate*. That is, how fast issues can
move through the steps. At a meeting interval of every other week. Any issues not handled
entirely during one meeting need to wait for the next. So, for example, suppose a
completed PR for a CC article is in the system but hasn't been approved by its assigned
approver. If the answer is to wait for the approver, then the item sits for two weeks
even if the approval is provided the day after the meeting.

###### Some EB Members Work As Needed
The solution to the above problem is potentially a bit higher iteration rate of meetings once
a week instead of once every other week. Another solution is to require (some) **EB Members**
to take steps agreed to during a meeting *as the work happens* instead of waiting until the
next meeting.

###### Setting Deadlines
The only way to set deadlines on GitHub is by using *Milestones*. Periodically, we will
create milestones for the first and third Friday of each month for some period of time
into the future. These milestones will represent succeeding *publications* of BSSw content.
Periodically, we will also need to delete old milestones.

###### Automation with GitHub Web API 
There is a [GitHub web api](https://developer.github.com/v3/issues/milestones/#create-a-milestone)
that could help automate a number of these steps. Lets keep this on the todo list until
we determine it is essential for productivity's sake.
