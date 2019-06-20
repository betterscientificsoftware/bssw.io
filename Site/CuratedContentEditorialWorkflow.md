

# A Proposed Editorial Workflow for BSSw.io Curated Content

*Note: might be equally appropriate for other types of content, but we’re starting with Curted Content.*

This is a rough outline of a process that I think might be suitable to our needs that can be
carried out using tools provided by GitHub and perhaps some helper automations/bots/scripts.
There is plenty of room for discussion and refinement.

Reference: 

[https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/projects/3](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/projects/3) 

# Actors
* **Anyone** who can submit a GitHub issue can use this approach to suggest a curated content topic.
* **Editorial Board Member**
* **Author** who can submit a pull request with a draft of the article, possibly from a fork.
* **Editorial Assistant** is a role that was first recognized in the blog workflow.
  It is someone familiar with the BSSw.io site and its operations, but who does not
  need to have the technical expertise to evaluate content that an editorial board
  member or subject matter expert would be expected to have.

# Workflow
1. **Somehow** is used in the steps described here to refer to one of several proposed modalites
   of action when it is not otherwise clear.
   * Automatically via Git/GitHub features or via yet to be developed scripts.
   * Organically via some **EB Member** simply volunteering to do it.
   * Meeting via decision/action at proposed bi-weekly content meetings.
1. **Anyone** submits (the *submitter*) a GitHub issue using the curated content issue template. 
1. Somehow, the issue is added to the “Content Development” project board *Idea Backlog* column.
1. Somehow, the issue is selected from the *Idea Backlog* for discussion and review and moved to the *Topic Review* column.
   * Automation could be based on comments and/or reactions in an issue while it is in *Idea Backlog*.
1. Somehow, a deadline for completion of discussion and review period is set. See [below](#setting-deadlines)
1. Discussion and reaction proceeds among **EB Members**.
1. Somewhow, the issue is either accepted and moved to the *Development Backlog* or rejected.
   * Acceptance criteria:
     * When there are two or more “thumbs up” than “thumbs down” reactions 
   * Rejection criteria:
     * if an issue has not reached +2 by deadline
     * if the issue is inactive for 30 days
1. Somehow, an **Author** is selected and then assigned using the *assignees* feature on GitHub issues
   and a deadline for completion is set. See [below](#setting-deadlines)
1. Somehow, issue is moved from the *Development Backlog* column.
1. **Author** produces a draft of the item as a pull request (PR) and associates with the issue using GitHub.
1. Somehow, the pull request is added to the *Item Review* column and *submitter* is notified.
1. Any desired automated tests run on the PR and results are reported.
1. **EB members** review the item, interact with the **Author** to refine as necessary, and
   approves the PR.
1. Somehow, the PR is moved to the *Ready for Publication* column.
1. An **Editorial Assistant** merges the PR and marks the metadata for publication. The PR is
   moved to the *Done* column.

# Criteria for Content

1. **In-scope Content** ( The exact scope of relevant content will evolve as we learn about community interests. )
   * General issues in productivity and sustainability that overlap with common challenges faced in the HPC/CSE software community.
   * General tools for productivity and sustainability that can be widely used by HPC/CSE developers.
   * Characterization of challenges and solutions that may be particularly valuable to the HPC/CSE community.
   * Likely to impact or inform HPC/CSE software devlopment process or planning.

1. **Highlight Connections to HPC/CSE**
   * How the topic intersects with themes that are of particular interest to HPC/CSE, for example MPI, Fortran, C++, architectures, modeling and simulation.
   * Why the topic could be of particular interest to HPC/CSE.
   * Not broadly covered in other common HPC/CSE venues.

1. **Ease of Adoption and Use**
   * Does it address how easy or hard it is to benefit from the topic?
   * Does it address who would be particularly interested in the topic?

1. **Out-of-scope Content**
   * Narrow scope, focused on a particular HPC/CSE subcommunity.
   * Tools, processes, and practices that have little in common with HPC/CSE.
   * Content that is deemed incomplete or biased, as determined by the BSSW leaders.

## Notes
1. We agreed its ok that we require submitters and **Authors** to have GitHub accounts 
1. Possible [resource link](https://www.youtube.com/watch?v=e3bjQX9jIBk&t=157s)
   for instruction on submitting a PR @rinkug found.
1. We need to use *symbolic constants* here in this workflow document for actual people
   (e.g. **EB Member** for an editorial board) and maintain a list of the *values* of those
   constants (e.g. who currently comprises the editorial board) elsewhere. In this way,
   the workflow doesn't change when staffing changes.
1. There are a lot of **Somehows** here suggesting we have to think through these steps.
1. It feels like the original workflow was designed around the concept of a *pool* of **EB Members** who
   organically cultivate activity and perform various steps on a volunteer, as-needed or as-available
   basis. That modality of operation might work but does some a bit more complicated than simple
   *assignment* of a responsible **EB Member** to marshal a given approved content idea from inception
   to completion.
1. **Editorial Assistant** role is mentioned only in last step. Do we really need a special role for this?

###### Setting deadlines
Periodically, we can run a script that deletes past *milestones* and
creates one-per-month *milestones* for a period of time in the future via the
[GitHub web api](https://developer.github.com/v3/issues/milestones/#create-a-milestone). This
would give EB members one month granularity to set deadlines yet avoid creating a milestone each time
we wanna set a deadline.
