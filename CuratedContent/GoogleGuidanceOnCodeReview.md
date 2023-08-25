# Google Guidance on Code Review

<!--deck text start-->
Google provides a very nice summary of peer code review best practices, which is likely a great place to start for many teams.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe "Roscoe A. Bartlett GitHub Profile")
#### Publication date: Aug 24, 2023

Resource information | Details
:--- | :--- 
Resource name | Google Code Review Developer Guide
Website | [Code Review Developer Guide](https://google.github.io/eng-practices/review/)
Focus | Peer Code Review

The Google Code Review Developers Guide condenses the latest research and long-learned best practices for conducting peer code reviews.
Thousands of Google developers write and modify hundreds of millions of lines of code every year, so these guidelines condense a lot of experience from a successful software company.
The guidelines are consistent with many aspects of Agile and Lean software development methodologies, and this guide can help to highlight and teach many of these principles.

In the Google Code Review Developers Guide, reviewers are directed to focus on design, functionality, complexity, tests, naming, comments, style, and documentation for changes to the set of code and related artifices under review.

In this Google guide, review artifacts are organized into different *Change Lists* (CLs) where a CL is an atomic set of related changes in the Perforce version control tool (for which Google uses a highly scalable, customized version of Perforce for its online code suite).
A CL corresponds to a Git Commit for readers more familiar with the Git version control tool.
Below, we use "CL/commit" to represent these smallest units of review artifacts (where the Google guide just refers to them as "CLs").

The Google Code Review Developer Guide provides guidance on how to pick good reviewers.
It also allows for in-person reviews and pair-programming reviews (i.e., real-time reviews by a pair of programmers as the code is being designed and written).

Some examples of the good guidance in this developer guide include:

* In general, reviewers should favor approving a CL/commit once it is in a state where it definitely improves the overall code health of the system being worked on, even if the CL/commit isn’t perfect.

* Reviews are an opportunity to mentor developers and pass along user information.

* Don’t let a CL/commit sit around because the author and the reviewer can’t come to an agreement.

* Implement only what is needed now and not speculative functionality (e.g., don't over engineer the code).

* Tests and documentation changes should be in the same CL/commit as the code changes.

* Every human-written line in every file in a CL/commit should be reviewed.

* Praise the developer when you see something good in the CL/commit (positive reinforcement helps to offset requests for changes and is a powerful motivator).

* Be courteous and respectful.

* Ask people to suggest changes before they post new CLs/commits (in case you have been rejecting many CLs/commits).

* Split large CLs/commits into smaller, more cohesive CLs/commits.

* If there is a major design problem, don't bother doing a line-by-line review.

* One business day is the maximum time it should take to respond to a code review request.

* If you are in the middle of a focused task, such as writing code, don’t interrupt yourself to do a code review.

* Don’t compromise on the code review standards or quality for an imagined improvement in velocity.

* Encourage developers to simplify code or add code comments instead of just explaining the complexity to you.

* In general, it is the developer’s responsibility to fix a CL/commit, not the reviewer’s.

* It is usually best to insist that the developer clean up their CL now, before the code is in the codebase and "done". (Letting people "clean things up later" is a common way for codebases to degenerate.)

* Responding to code reviews and follow-ups usually makes complaints about string code reviews go away.

Reading through all of the pages for the Google Code Review Developer Guide should only take one or two hours or so (depending on how fast one reads and how familiar one may be with this topic).
Most developers and teams will likely learn a lot about peer code review best practices with a fairly small time investment.

<!---
Publish: yes
Pinned: no
Topics: peer code review
RSS update: 2023-08-24
--->
