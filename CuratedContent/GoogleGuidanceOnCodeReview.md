# Google Guidance on Code Review

<!--deck text start-->
Google provides a very nice summary of peer code review best practices which is likely a great place to start for many teams.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe "Roscoe A. Bartlett GitHub Profile")
#### Publication date: ???

Resource information | Details
:--- | :--- 
Resource name | Google Code Review Developer Guide
Website | [Code Review Developer Guide](https://google.github.io/eng-practices/review/)
Focus | Peer Code Review

The Google Code Review Developers Guide condenses the latest research and long-
learned best practices on conducting peer code reviews.
Thousands of Google developers write and modify hundreds of millions of lines of code every year so these guidelines condense a lot of experience from a successful software company.
The guidelines are consistent with many aspect of Agile and Lean software development methodologies and this guide can help to highlight and teach many of these principles.

In the Google Code Review Developers Guide, reviewers are directed to focus on design, functionality, complexity, tests, naming, comments, style and documentation for changes to the set of code and related artifices under review.
These review artifacts are called a *Change List* (CL) and correspond a single Git commit (i.e. an atom related set of changes with a specific purpose).
(Most of Google's code is manged with a highly customized version control tool called Perforce, and Perforce uses the term *changelist* described a set of related changes to a set of files.)

The Google Code Review Developer Guide provides guidance on how to pick good reviewers.
It also allows for in-person reviews and pair-programming reviews (i.e. real-time reviews by a pair of programmers as the code is being designed and written).

Some examples of the great guidance in this developers guide include (which "Commit" has been substituted for "CL in the Google Developers Guide):

* In general, reviewers should favor approving a commit once it is in a state where it definitely improves the overall code health of the system being worked on, even if the commit isn’t perfect.

* Reviews are an opportunity to mentor developers and pass along user pieces of information.

* Don’t let a commit sit around because the author and the reviewer can’t come to an agreement.

* Implement only what is needed now, and not speculative functionality (e.g. don't over engineer the code)

* Tests and documentation changes should be in the same commit as the code changes.

* Every human-written line in every files in a commit should be reviewed.

* Praise the developer when you see something good in the commit (positive reinforcement helps to offset requests for changes and is a powerful motivator).

* Be courteous and respectful.

* Ask people to suggest changes before they post new commits (in case you have been rejecting may commits).

* Split large commits into smaller more cohesive commits.

* If there a major design problem, don't bother doing a line-by-line review.

* One business day is the maximum time it should take to respond to a code review request.

* If you are in the middle of a focused task, such as writing code, don’t interrupt yourself to do a code review.

* Don’t compromise on the code review standards or quality for an imagined improvement in velocity.

* Encourage developers to simplify code or add code comments instead of just explaining the complexity to you.

* In general it is the developer’s responsibility to fix a commit, not the reviewer’s.

* It is usually best to insist that the developer clean up their CL now, before the code is in the codebase and "done." (Letting people "clean things up later" is a common way for codebases to degenerate.)

* Responding to code reviews and follow-ups usually makes complaints about string code reviews go away.

Reading through all of the pages for the Google Code Review Developer Guide should only take one or two hours or so (depending on how fast one reads and how familiar one may to this topic).
Most developers and teams will likely learn a lot about peer code review best practices with a fairly small time investment.

<!---
Publish: yes
Pinned: no
Topics: peer code review
RSS update: ???
--->
