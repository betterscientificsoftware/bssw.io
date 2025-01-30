# Creating An Offboarding Checklist for Technical Projects
<!--deck text start-->
Don't wait until someone is leaving a project to figure out all the things that need to be done before they're gone.
<!--deck text end-->

#### Contributed by [Keith Beattie](https://github.com/ksbeattie "Keith Beattie")
#### Publication date: January 29, 2025

Resource information | Details 
:--- | :--- 
Article Title | [Technology Moving Positions & Offboarding for Resigning or Retiring Employees](https://servicecenter.twu.edu/TDClient/1956/Portal/KB/ArticleDet?ID=128448)
Source | Texas Woman's University

What happens when someone on a project, specifically a technical contributor, leaves?
Even in the best of situations, there is not enough time to get everything done if your project
hasn't already prepared for any such departure with an offboarding plan.

There are many good resources on the web for understanding the importance of offboarding.  Atlassian
details the "What" and "Why" in their [Understanding the Offboarding
Process](https://www.atlassian.com/itsm/esm/offboarding) article.  StrongDM proposes an excellent
check-list with [All Offboard! The 2025 Tech Staff Offboarding
Checklist](https://www.strongdm.com/blog/technical-staff-offboarding-checklist).

These articles cover the important tasks like exit interviews, recovering physical assets, removing
access to internal accounts and resources, etc.  
But what are the less practiced offboarding steps specific to software contributors?
The referenced article above from Texas Woman's University starts with an essential observation: The first step to a successful offboarding process is a well-planned _onboarding_ process.

The day a person starts on a project is the best time to identify what parts of the code base they
are responsible for, where the documentation for it lives, where the tests are and how they are run.
While TMU's article covers the transfer of access to important documents or emails, the same applies
to functionality ownership and expertise within the source code of a software project.
In the spirit of starting the offboarding process early, the software team should regularly review these
roles and add to them the secondary or backup people for each area.  
In the event someone leaves the project (or even is unavailable for a significant period of time) having that list can ensure that
functionality is not abandoned and contribute to technical debt.  Tools to support this currently
exist.  
Both
[Github](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
and [Gitlab](https://docs.gitlab.com/ee/user/project/codeowners/) support a CODEOWNERS file where
people or teams of people are identified and automatically added as reviews for pull or merge
requests.

Early identification of who inherits the code and responsibilities of a person leaving a project is
just one of the many things an onboarding and offboarding process or checklist needs to identify.
In this reviewers opinion, it is an often overlooked and very important step highlighted in the
TWU article.

<!---
Publish: no
Topics: software process improvement, strategies for more effective teams
Pinned: no
RSS update: 2025-01-29
--->
