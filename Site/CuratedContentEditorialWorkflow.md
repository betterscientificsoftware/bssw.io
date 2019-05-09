

# A Proposed Editorial Workflow for BSSw.io Curated Content

*Note: might be equally appropriate for other types of content, but we’re starting with Curted Content.*

This is a rough outline of a process that I think might be suitable to our needs that can be
carried out using tools provided by GitHub and perhaps some helper automations/bots/scripts.
There is plenty of room for discussion and refinement.

Reference: 

[https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/projects/3](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/projects/3) 

# Actors
* **Anyone** who can submit a GitHub issue can use this approach to suggest a curated content topic
  * Do we need to do anything to accommodate those who can’t (or don’t want to) submit a GH issue?
* **Editorial Board Member**
* **Author** who can fork the repository and submit a pull request for a new article
  * Do we need to do anything to accommodate those who can’t (or don’t want to) use the GH pull request process?
* **Editorial Assistant** is a role that was first recognized in the blog workflow.
  It is someone familiar with the BSSw.io site and its operations, but who does not
  need to have the technical expertise to evaluate content that an editorial board
  member or subject matter expert would be expected to have.

# Workflow
1. **Anyone** creates a GitHub issue for a proposed curated content (CC) item
   * We should use issue templates to tailor the requested data and automatically
   apply an appropriate label/project board assignment
1. The issue is added to the “Curated Content Ideas” (CCI) project board *Idea Backlog* column.
   * Ideally, this should be done automatically on creation of the issue.  From research on the web,
     it doesn’t appear that issue templates allow direct assignment to boards yet.  Maybe this can be
     done with a bot for issues with the appropriate label. *This can be done automatically by a setting
     on the project board column.*
1. An **Editorial Board member** (EB) moves the issue into the *Topic Review* column and provides input
   via the discussion and/or reaction capabilities of GitHub issues.
   * Perhaps this move can be automated by a bot that notices discussion or reaction in an issue in Backlog.
1. Discussion and reaction proceeds among the **EB**.  When there are two or more “thumbs up” than
   “thumbs down” reactions on a topic in review, it moves to the Item *Development Backlog* column.
   * I think this can be automated via GitHub’s API.
   * We need to be able to say that if an issue has not reached +2 in a certain time frame, it is
     considered not appropriate as a CC item.  This probably needs to set a label in the issue
     indicating this decision, and move it to the _Done_ column.  An example of a rule that might
     be workable is that there is no further activity on the issue (new discussion or reactions)
     within 30 days.  There could be a bot that reminds the Editorial Board when issues in
     Topic Review are aging.
1. An interested **Author** picks an issue from the *Development Backlog* column and produces a
   draft of the item as a pull request (PR), associated with the issue.  The pull request is added
   to the *Item Review* column.
1. Any desired automated tests run on the PR and results are reported.
1. An **EB member** reviews the item, interacts with the **Author** to refine as necessary, and
   approves the PR. The PR is moved to the *Ready for Publication* column.
1. An **editorial assistant** merges the PR and marks the metadata for publication. The PR is
   moved to the *Done* column.
