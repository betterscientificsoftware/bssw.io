# A Proposed Alternative Editorial Workflow for BSSw.io Curated Content

The key difference in this alternative workflow is that it explicitly requires
**EB Members** engage in specific activities on a routine basis, in particular
a bi-weekly progress meeting.

# Actors
* **Anyone** who can submit a GitHub issue can use this approach to suggest a curated content topic.
* **Editorial Board Member**
* **Author** who can submit a pull request with a draft of the article, possibly from a fork.
* **Editorial Assistant** is a role that was first recognized in the blog workflow.
  It is someone familiar with the BSSw.io site and its operations, but who does not
  need to have the technical expertise to evaluate content that an editorial board
  member or subject matter expert would be expected to have.

# Process

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
     Topic Review and a deadline (milestone) is assigned.
1. Issues in Topic Review are handled as follows
   * Any more than 30 days old that have garnered insufficient interest are labeled
     as `wontdo`. A comment regarding to lack of interest is added the the issue is
     and closed.
   * Any issues with sufficient interest are moved to the Development Backlog. An
     **EB Member** is assigned. An author, if different from **EB Member** is
     identified (via @ mention) and a deadline is set (via milestone) for completion.
1. Issues in Development backlog are handled as follows
   * Issues in jeapordy of making deadline are reviewed and discussed. Authors are
     nudged and/or deadlines are adjusted.
   * Issues that are woefully beyond deadline are labeled as `insuffucient development`
     and closed.
   * Issues for which PR has been submitted are moved to Item Review and 1 reviewer is assigned.
1. Issues in Item review are handled as follows
   * Approved PRs are merged and metadata is added in preparation for publication
   * Unapproved PRs are reviewed in-situ and approved or not. If no approval forthcoming,
     revisions required by author are explained in comments in the PR.
1. Milestones (deadlines) are reviewed to ensure any items intended for a given
   date are either completed, have committments they will be completed or pushed

The key challenge in this process is the *iteration rate*. That is, how fast issues can
move through the steps. At a meeting interval of every other weeks. Any issues not
handled entirely during one meeting need to wait for the next. So, for example, suppose
a completed PR for a CC article is in the system but hasn't been approved by its assigned
approver. If the solution is to wait for the approver, then the item sits for two weeks
even if the approver provided approval the day after the meeting.

The solution to this problem is potentially a bit higher iteration rate of meetings once
a week instead of once every other week. Another solution is to empower (some) **EB Members**
to take steps agreed to during a meeting *as the work happens* instead of waiting until the
next meeting.
