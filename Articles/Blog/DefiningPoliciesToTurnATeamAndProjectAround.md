# Defining Policies to Turn a Team and Project Around

#### Contributed by [Jason M. Gates](https://github.com/jmgate "Jason M. Gates GitHub Profile")

#### Publication date: October 10, 2018

When trying to decide what software engineering best practices to apply to your scientific software project, the key task is to define your policies, whatever they may be, and get your team to commit to them, realizing that you can refine implementation details as you go along.

### EMPIRE's Story

Prior to the summer of 2017, the EMPIRE team&mdash;working on a next-generation electrostatic/electromagnetic/fluid dynamic code under the Advanced Technology Development and Mitigation program under the DOE Exascale Computing Project&mdash;was a bit of an unorganized mess.  Confusion arose as to who was actually on the team, what people were working on, what needed to be done, and how one went about getting started.  There were a few separate repositories, largely developed by one lone coder each, with no integration.  Pushes happened directly to "master." Testing, documentation, and code review were minimal.  In short, it was the wild west.

At the time, a few team members realized that if we were to hit the various milestones that loomed ominously ahead of us, we needed to rethink how we did things.  We wound up getting everyone in one room together (which was the first time I realized I was even part of this team) and made a few key decisions for moving forward.

First and foremost, we decided to use [GitLab] (https://gitlab.com) for everything we could; and with that as our starting point, we needed some sort of
* issue tracking;
* code review;
* documentation;
* code style guide;
* git workflow that gives us as much stability as possible; and
* automated testing.

When we made these decisions, we didn't fully know how to implement anything&mdash;we just knew what we needed and there was a team commitment to figuring it out.  Here's what we wound up settling on over the course of the past year.

#### Git Workflow

One of the first actions we took was to switch to a master/develop workflow.  Feature branches are created off of "develop" and the only way to get those changes into "develop" is via merge requests (discussed below).  The "master" branch gets updated via nightly testing (again, see below), and other than that no one can push or merge to it.

#### GitLab Issues

We also agreed early on  that all work should begin as an issue.  We created a handful of separate [issue templates] (https://gitlab.com/help/user/project/description_templates.md), which you can select from a drop-down menu when creating a new issue.  These have helped us get more and better information at the outset, rather than having to iterate back and forth with the issue submitter before everyone knows enough to start tackling the issue.  A collection of descriptive labels helps us see at a glance which issues are, for instance, blocked or have external dependencies.  We also educated the team on a Kanban process for moving issues through the various stages of work.  In addition, we encouraged the practice that commit messages should reference the issue number so that GitLab ties the commits and issues together for better traceability of why changes are being made.

#### GitLab Merge Requests

Instead of allowing developers to push directly to "develop," we decided that changes must come in via a GitLab merge request (MR).  You can set this up by [protecting the "develop" branch] (https://docs.gitlab.com/ee/user/project/protected_branches.html) and selecting that "Maintainers" can push and "Developers + Maintainers" can merge.  Code review comes built-in to MRs, and as a team policy we said that MRs must be reviewed and approved by at least one person.  Reviewers are supposed to compile and test the feature branch before approving.  Building this code review into the process has helped us catch bugs sooner rather than later, and we wind up training more team members in how various parts of the code work.

#### Documentation

Essentially two types of documentation exist, and how you handle them can differ considerably.

*  *Documenting the Code Itself:*  For documenting the code itself&mdash;the classes, their functions, and data&mdash;we decided on [Doxygen] (http://www.doxygen.nl/).  It's not a perfect system (no system is), but enough of our team already had at least moderate familiarity with it.  In terms of what to document, we specified that all new code written must have a minimum set of documentation ("\brief," "\parameter," and "\returns"), and beyond that we specified how we would like everything documented should you have time to write it all.  If you wound up modifying old code that lacked documentation, the suggestion was to either document it yourself or track down the original authors and have them document it.  Since all changes come in via MR, the reviewer was responsible for ensuring that our documentation policy was followed.

*  *Interacting with the Code and Team:*  In addition to documenting the code itself, we needed documentation for how to interact with the code.  For this we turned mainly to [GitLab wikis] (https://docs.gitlab.com/ee/user/project/wiki/), creating pages explaining all the policies outlined here.  Wiki pages were also created for how to get, configure, build, and test the code.  Some of this information was also put into a `CONTRIBUTING.md` file in the repository root, which GitLab treats specially and links to on the new issue and new merge request pages.

#### Code Style Guide

Discussions of code style are rarely productive, particularly in the realm of C++.  No right answer exists, so we all prefer the way we  do things.  Unfortunately if you have more than one developer on a project, the mixing of styles makes simply picking up and understanding the code harder.  Even with a single developer, your style will likely change over the years, making code you wrote seven years ago look entirely unlike code you wrote yesterday.  Ultimately it doesn't matter what you decide for a style guide&mdash;you're bound to upset someone either way&mdash;just pick something and get the team to stick with it.  In our case we wound up having the team vote on issues&mdash;we laid out all the possibilities as separate comments in a GitLab issue, and we used emoji reactions to tally the votes&mdash;in hopes of maximizing team agreement and minimizing team member retraining.  I'm not perfectly happy with what we landed on, but I am happy that we landed on something.

#### Automated Testing

With regard to testing, we had a particular problem we were trying to solve where changes to an underlying library would wind up breaking our testing.  We settled on utilizing [Jenkins Pipelines] (https://jenkins.io/doc/book/pipeline/), which allow us to fire off a number of jobs on all the machines and with all the configurations we care about, in order to test the underlying library and then aggregate those results.  If all is well, we can fire off a second stage of jobs to test our codes on top of the library update and then aggregate those results.  If all is well, we wind up updating our fork of the library.  In the process, we developed a library for driving this pipeline framework, which then allowed us to stand up a secondary pipeline to handle automatic merges from "develop" to "master."  When either of these pipelines succeeds, it  updates a wiki page that contains an ever-expanding table of all the SHA1s in all of our repositories that are known to work together.  Additionally, automated emails are sent out at the completion of either pipeline, with results summaries and links to job console output if something goes wrong and developers need to debug.

<br>

 [Poster presented at the [Third Conference of Research Software Engineers](https://rse.ac.uk/conf2018), Sept. 2018]<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0918_DefiningPoliciesPoster_2000_1198.png' class='page lightbox' />

### What Did All That Buy Us?

A lot.  We are easily in an infinitely better spot today than we were a year ago.  Of course we can improve, but that situation will always be true.  Here are some specific outcomes.
*  The combination of GitLab issues and merge requests has meant that **design discussions now happen that would not have otherwise.**  "Is that the best way to do things?"  "What you have currently works but won't be performant on GPUs, so we should restructure things this way."  "Actually, given what someone else is working on, we probably want to restructure how we do this so the two will work better together."  Previously such discussions simply didn't happen, and we were left to deal with the consequences when problems arose.  Additionally, team members now find themselves more knowledgeable about the code itself, and all the work being done on it, provided they pay attention to their GitLab notifications.
*  The combination of documenation and code style guidelines has given the code a **common look and feel** that makes the code significantly easier to pick up and understand.  This is important when onboarding new members, but also in cases where current team members are coming up to speed on sections of the code they haven't touched yet.
*  The combination of git workflow and automated testing has made the code **significantly more stable.**  A year ago we had three repositories with no interaction.  Today we're up to five repositories that are intimately integrated, and our automated testing is crucial for letting us know when something goes wrong, and where, so we can tackle the problem as soon as possible.

### Your Decisions Aren't Set in Stone Forever

While it sounds like we sat down and made a bunch of really good decisions at the outset and have just been living with the benefits ever since, in reality our policies matured organically over some time.  Key to our development as a team has been the process of weekly touchpoints and monthly retrospectives.  We built into the fabric of our team the ability to ask questions like the following:

*  How are we doing as a team?
*  Are our policies working well for us?
*  Do they need to be amended?

You don't want to switch up your policies every week or so&mdash;in that case the policies become relatively worthless&mdash;but you do need the ability to tweak the way you do things as your team grows and you discover how you collaborate best.

### Future Work

Along with the ability to evaluate your current practices and see how they could be improved, it's important to ask yourselves if you're not doing something yet that you should perhaps start.  Here are a few items on our to-do list.

*  *Improve automated testing:*  We will probably always want to be in a place where we're improving our automated testing to improve stability and ease debugging when something goes wrong. Specifically, in the near-future we'll be looking into the automated testing of merge request branches before they get merged in.  While our policy has been for MR reviewers to build and test these branches, this has become significantly more difficult as the ways our codes are built and integrated have become more complicated.  It would be nice to automate the process and take it out of the hands of developers and reviewers.
*  *Team room hackathons:*  We've tried these a few times and decided they need to be a more regular part of our team rhythm.  The general idea is to get everyone on the team in one room together in front of computers and working on some collaborative effort, for example, refactoring the way we do input deck parsing.  This has aided significantly in knowledge transfer throughout the team.
*  *Onboarding checklist:*  Our team has grown on the order of 50% over the past year; and while we had plenty of team policy documentation spread throughout our wikis, there wasn't a single digital point of contact for introducing new members to the team.  Additionally, even those who were around when these decisions were made a year ago often have forgotten where we documented various decisions, and it will be useful to have a single page where you start that will quickly point you to the information you need.
*  *More official Scrum adoption:*  While issue tracking has been great for us, we've found we could benefit from better defined (or perhaps just better enforced) rules of engagement and more formalized communication and documentation of work done and decisions made.

### Observations

Is there anything that stands out after our year and a half or so of experience?  Indeed.  To have success along the lines we've had, a few key components are necessary.  

*  First, you need a project lead who is open to experimenting with new ideas in terms of how you do things as a team.  

*  Second, you need individuals on the team who are passionate about improving the software engineering side of research who can feed such ideas to the project lead and push things in the right direction. 

*  Third, and somewhat implicit in the preceding two statements, you actually need a team&mdash;not a collection of individuals who don't act as a team.  

If you're missing any of these three pieces, initiating and maintaining forward momentum will be difficult.

Another interesting realization was that while we had high initial commitment to certain policies&mdash;e.g., GitLab usage, Doxygen, etc.&mdash;our enthusiasm in those areas had waned somewhat and we weren't as diligent at following the policies we'd laid out.  That wasn't entirely a bad thing&mdash;for instance, we wound up revamping our issue and MR templates to better fit how we work as a team&mdash;but it does mean we need a periodic reevaluation of and recommitment to our team policies.

**Peer pressure *does* work as an enforcement mechanism.**  In all that we've done with team policies over the past year,  relatively little has been mechanically enforced.  Most of the enforcement comes from us saying, "This is how we're going to do things," and then holding one another to it through issues and merge request reviews.  Personally I'd prefer a little more mechanical enforcement, but we have to balance the potential added benefit with the need for flexibility and speed in development.

While it may be tempting to walk away thinking, "Okay, I need to get set up with GitLab and Jenkins and Doxygen and&hellip;," keep in mind that those were just the implementation details we settled on and how we implemented them has developed over time.  The important thing&mdash;the big takeaway here&mdash;is that you actually sit down and **define your policies** and then **get your team to commit to them.**  If you're in a place where everything looks like a mess and you're wondering what to do, feel free to start small and let your policies grow over time.  What is your greatest need, your biggest pain point, today?  Start there, and just see how things go.


Take a look at the PDF version of [our poster] (https://cfwebprod.sandia.gov/cfdocs/CompResearch/docs/DefiningPoliciesToTurnATeamAndProjectAround.pdf "Defining Policies Poster") presented at the [Third Conference of Research Software Engineers](https://rse.ac.uk/conf2018), September 2018.

### Author Bio

Jason M. Gates is a Research Software Engineer in the Software Engineering and Research department of Sandia National Laboratories, where his role is to help scientific R&D codes and teams to transition toward becoming high-quality production-stable software engineering efforts.  To that end, he leads a team that offers introductory and intermediate git courses to Sandians throughout the year.  He has a background in engineering physics, simulating magnetically confined high-temperature plasmas, and applied mathematics, focusing on numerical methods and scientific computing, but his passions are teaching and helping people do the work they do in more usable, maintainble, and extensible ways.



<!---
Publish: yes
RSS-update: 2018-10-10
Categories: collaboration
Topics: strategies for more effective teams
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
