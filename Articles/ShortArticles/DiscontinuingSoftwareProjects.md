# Discontinuing a Research Software Project

Software projects come to an end for a variety of reasons.
A newer project can render an older project obsolete.
The market or need for a capability can dwindle or completely disappear.
A sponsoring organization can wind up making a strategic decision to discontinue a software project.
Funding can run out.

Many *research* software projects have built-in sunset dates when the sponsoring organization's funding ends.
For SciDAC projects for example, a common duration is 3-5 years.
If a project is unable to gain traction within the community and win funding from other sources in that time frame, the project will most likely be discontinued.

Scientific computing research software projects in particular can come to an end in ways that ultimately impact our community's ability to ever reap any benefit from progress made or lessons learned or otherwise have available for posterity's sake any of the system design, architecture, implementation and software engineering know how that went into the project.
We all can likely think of example projects where this has happened.

Over time, project assets and artifacts and even contact information of the people involved can fall out of date and/or become inaccessible.
A common situation is a domain name and/or institutional domain aliase/forward that expires.
When this happens, the main entry point to the project known throughout the community is lost.
Future researchers are then unable to discover the project even existed let alone find anyone with knowledge about it.
In that case, the only available information is likely to be in published articles.
However, in scientific computing projects, publications tend to focus on the *science* enabled by the software such that little if any knowledge about the software itself remains available.

Here we outline a number of choices sofware project members can make that will improve the ability for project software assets to remain accessible after a project comes to an end.

1. Open-source the code

   If the project's codebase is not already open source, a key way to ensure it remains available to the community to learn from is to release it under an open-source license.
   The institution(s) that sponsored its development may require an open-source release to follow specific processes.
   For example, Livermore Labs' Information Management (IM) office defines the processes to follow for open-source releases.
   By making a project's software open source, it becomse possible to host the software in world-readable, public places (e.g. GitHub or GitLab) where the community can find it and learn from it.

1. Document final status

   In any project, documentation is important.
   Ordinarily, documentation has various roles such as for users, developers and/or installers/maintainers of the software.
   For a project that is ending, there is probably very little resource available to continue writing documentation.
   In addition, the role of any remaining documentation should be to try to capture a complete snapshot of *key* aspects of the software as possible.
   This could be as simple as bunch of bullets in a `final-status.txt` file that remains with the software.
   The goal is to capture the project's objectives, methodologies, and key findings.
   Include any design decisions, algorithms, and implementation details that may be valuable to others who might be interested in following in your footsteps.

1. Establish an enduring on-line presence

   Create a website

   The use of mailing list for this purpose should be discouraged and avoided at all costs.

   Create a public repository: Set up a public code repository (e.g., GitHub) to store the project's code, documentation, and related resources. This repository can serve as a central hub for the project's artifacts, allowing others to easily discover and access them.

1. Archive the software

   DOE CODE (https://www.code.gov)
   DOI?
   Many Mirrors
   netlib.org
   internet archive
   software heritage (https://www.softwareheritage.org)
   https://wiki.archiveteam.org

1. Present or Publish (about the software)

   Get at least one piece of literature (conference presentation or proceedings publication) anywhere it may be a good fit where you can talk in more detail about the software (instead of the science it may enable).
   Often case-studies and lessons learned are good candidate topical areas
   Publish research papers, technical reports, or whitepapers that discuss the project's methodologies, challenges, and outcomes. By actively sharing knowledge, you increase the chances of the community benefiting from the project's know-how.

1. Refactor for critical dependencies

   Split out the pieces that may have a life of their own.
   Engage down stream dependencies to ask if they may be interested in taking over a piece
   Seek researchers working in similar area to see if they may want it
   There may be graduate students looking for projects

Discontinuing a partially completed software project can be challenging, but it's essential to handle it properly to preserve the knowledge gained and the lessons learned. Here are some steps and actions that can be useful in this process:

1. **Documentation**: Start by documenting everything related to the project. This includes code, design decisions, architecture, and any relevant discussions or meetings. Create comprehensive documentation that can help other developers understand the project's scope, progress, and any challenges encountered.

2. **Lessons Learned**: Conduct a lessons-learned session with the team to capture insights into what went well and what didn't during the project's development. Document these lessons, as they can be valuable for future projects, ensuring that the same mistakes are not repeated.

3. **Code Review**: If possible, conduct a code review with the team to identify any critical issues or potential security vulnerabilities. This will allow you to address these concerns and prevent them from carrying over to other projects.

4. **Knowledge Transfer**: Identify team members who were heavily involved in the project and arrange knowledge transfer sessions with them. This can include one-on-one meetings, pair programming, or knowledge-sharing sessions with the entire team.

5. **Version Control**: Ensure that all the code, even if incomplete, is properly version controlled. This will allow future developers to understand the project's evolution and have access to all the work done up to this point.

6. **Archive Assets**: Store all relevant assets, such as design files, mockups, and any research conducted during the project. These assets can be beneficial for future projects or as reference material.

7. **Identify Reasons for Discontinuation**: Understand the reasons why the project is being discontinued. It could be due to budget constraints, changing business priorities, or technical challenges. Knowing these reasons will help in making informed decisions for future projects.

8. **Communication**: Communicate the discontinuation decision transparently and promptly to stakeholders, clients, or anyone affected by the project. Be honest about the reasons and express gratitude to the team for their efforts.

9. **Maintain Contact Information**: Make sure you have contact information for all team members in case any follow-up questions or clarifications are required in the future.

10. **Evaluate Salvageable Components**: Assess if any parts of the codebase or architecture can be reused in other projects. Salvaging valuable components can save time and effort in future development.

11. **Review Contracts and Legal Obligations**: If the project involved any third-party contracts or legal obligations, review them to ensure all necessary termination procedures are followed.

12. **Post-Mortem Meeting**: Hold a post-mortem meeting with the team to discuss the reasons behind the project's discontinuation and reflect on the overall experience. This can lead to valuable insights for future projects.

By following these steps, you can effectively discontinue a partially completed software project while retaining the knowledge gained and leveraging the lessons learned for future endeavors.

Utilization of software project hosting providers such as SourceForge, GitHub, GitLab,
etc.  definitely helps software projects avoid some issues when discontinuing by enabling
the project to maintain a continued presence even after funding is lost. The more
services (issue tracking, email lists, web site hosting, etc.) the project utilizes
from hosting providers, the easier it is for informabout about the project to remain
available even after all work has ended.
For example, GitHub features the ability to put a repository in an *archived* state.
But, even that has its limits (security updates for example take effort).

There are things project stakeholders and sponsoring organizations can do to *gracefully* 
discontinue a software project in such a way that key assets remain aviailable for
the benefit of the community.

What to do about existing users? What to do about future users?
license to transfer or support continued development by others.

One of the first things to decide is whether future project *communications* will go on
some form of life-support or be discontinued entirely. Having life-support communications
is obviously preferred but it comes at some non-zero cost and so may not be practical in
all cases. For life-support, it is important to identify *how* (e.g. email, twitter, slack)
any inquiries will be handled and by *whom* (e.g. email address, twitter handle, slack
username). This information should be posted prominently in all of the on-line spaces where
the project has a continued presence. Even if communications will be discontinued entirely,
it may make sense to provide way for inquirers to *register* their interest by some kind of
a sign-up process that collects such contact information.
GitHub reactions can do this.


Some of he choices a project makes up front can impact these questions

Problems with email and email lists, etc.

Collecting such inquiries

 may be useful in substantiating the level of interest to future
stakeholders
The ability to collect contacts
Will interested parties be directed to make contact by email, twitter, slack, etc. or just
be directed to a web page?

of

 One of the nice things about email
is that

Which modality(s) of communication with former project stakeholders will
be maintained 

* Identify the modality(s) of contact that will be maintained for any inquiries
  occurring *after* project discontinuation (e.g. email, twitter, GitHub discussions, etc.).

* Identify at least one person (preferrably 2 or 3 persons) who will serve as point
  of contact for any inquiries occuring after the project is discontinued. If this
  role needs to be transferred

* Some stakeholders should set semi-annual reminders on their calenders just to
  check and confirm the project's on-line presence is still working.
* Ensure on-line access points have a continued maintinence plan
  * as well as the systems where the below resources are hosted
  * mailing lists, discussion boards, ...
  * issue trackers
  * web site(s)
  * custom domain names
    * Custom domain names cost money and have expiration dates. In many cases, these
      custom domain names are just re-directions to a sponsoring organization's 
      own hosting resources. If so, change the re-direction for the custom domain name
      as soon as possible to an announcement page (e.g. break the redirection) indicating
      the project is discontinued. This way, while the custome domain name remains active,
      this will give time for project hosted through the sponsoring organization's own
      resources to become well known.
* Set up appropriate auto-responders on email list(s)
* Ensure various on-line access points prominently indicate that the project
  has been discontinued (or is in hibernation mode).

or is seeking funding


* security updates for hosting modalities
* For projects that involve persistent data formats, provide users with documentation
  about how to convert their data to another format.
* For projects for which decent alternative software products exist, maybe 
* Gather together whatever resources the project may have produced that help to
  explain/describe the software (slide decks from presentations, etc.)
  * This could be a simple listing of key files in the repository interested
    consumers should be aware of if they need to go look
* On GitHub, projects can be *archived* (converted to read-only)
* What can be done to ensure that if the project gets re-started, it can be easily
  picked back up and restarted by possibly new developers?
* Sponsoring organizations should be willing to allocate a small amount of remaining
  funds for teams to expend effort preparing the project for discontinuation. A good
  motive is helping to ensure the sponsor's investments to that point are not lost
  entirely.
