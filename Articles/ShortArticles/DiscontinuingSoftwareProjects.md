# Discontinuing a Research Software Project

Software projects come to an end for a variety of reasons.
A newer project can render an older project obsolete.
The market or need for a capability can dwindle or completely disappear.
A sponsoring organization can wind up making a strategic decision to discontinue a software project.
Funding can run out.

Many *research* software projects have built-in sunset dates when the sponsoring organization's funding ends.
For SciDAC projects for example, a common duration is 3-5 years.
If a project is unable to gain traction within the community and win funding from other sources in that time frame, the project will most likely be discontinued.

A challenge in how scientific software projects end is that often a lot of the technical knowhow with respect to softare design and development can be at risk of being totally lost.
This is because for scientific software projects, their publicly available record of work (e.g. presentations, papers, etc.)  have to mostly remain focused on the science their software enables and not so much the design and development of the software itself.

Scientific computing research software projects can come to an end in ways that ultimately impact our community's ability to ever reap any benefit from progress made or lessons learned or otherwise have available for posterity's sake any of the system design, architecture, implementation and software engineering know how that went into the project.
We all can likely think of example projects where this has happened.

Over time, project assets and artifacts and even contact information of the people involved can fall out of date and/or become inaccessible.
A common situation is a domain name and/or institutional domain aliase/forward that expires.
When this happens, the main entry point to the project known throughout the community is lost.
Future researchers are then unable to discover the project even existed let alone find anyone with knowledge about it.
In that case, the only available information is likely to be in whatever published articles there are that the project produced.
However, in scientific computing projects, publications tend to focus on the *science* enabled by the software such that little if any knowledge about the software itself remains available.

Here we outline a number of choices sofware project members can make that will improve the ability for project software assets to remain accessible after a project comes to an end.

1. End-of-project release

   Making a final release when there is a planned sunset date is easier than doing so when funding is suddenly and unexpectedly lost.
   If work must cease immediately, then there really isn't much more that can be done.
   However, with fair warning, a project can move to *tidy things up* all funding is lost.
   There is likely work in progress to bring to a close but nonetheless leaves the software in a reasonably functional state.
   That may mean conditionally disabling (via well-documented CPP `#if` or `#ifdef`) in-progress code blocks.
   It may mean hastily written testing and documentation too.
   An untimely, end-of-project release may even be below the quality standards the project is accustomed to maintaining.
   If so, the release can be identified as *development* or *experimental*.
   The goal of an untimely end-of-project release is to capture the most comprehensive snapshot with as much information about the state of the software (its design, architecture, implementation, etc.) as possible.

1. Open-source the code

   If the project's source code is not already open source, a key way to ensure it remains available to the community is to release it under a widely adopted open-source license.
   The institution(s) that sponsored its development may require an open-source release to follow specific processes.
   For example, Livermore Labs' Information Management (IM) office defines the processes to follow for open-source releases.
   By making a project's software open source, it becomse possible to host the software in world-readable, public places (e.g. GitHub or GitLab) where the community can find it and learn from it.
   In these cases, it is best to choose a *permissive* type open source license which includes a *disclaimer of warranty* which most do. 
   Good options are [MIT](https://opensource.org/license/mit/) or [ISC](https://www.isc.org/licenses/).

   Utilization of software project hosting providers such as SourceForge, GitHub, GitLab,
   etc.  definitely helps software projects avoid some issues when discontinuing by enabling
   the project to maintain a continued presence even after funding is lost. The more
   services (issue tracking, email lists, web site hosting, etc.) the project utilizes
   from hosting providers, the easier it is for informabout about the project to remain
   available even after all work has ended.
   For example, GitHub features the ability to put a repository in an *archived* state.
   But, even that has its limits (security updates for example take effort).

1. Document final status

   In any project, documentation is important.
   Ordinarily, documentation has various roles such as for users, developers and/or installers/maintainers of the software.
   For a project that is ending, there is probably very little resource available to continue writing documentation or fill in massive gaps in documentation before all funding is lost.
   In addition, the role of any remaining documentation should be to try to capture a complete snapshot of *key* aspects of the software design and implementation as possible.
   This could be as simple as bunch of bullets in a `final-status.txt` file that remains with the software.
   The goal is to capture the software's objectives, methodologies, and key findings.
   Include any design decisions, algorithms, and implementation details that may be valuable to others who might be interested in following in your footsteps.

This includes code, design decisions, architecture, and any relevant discussions or meetings. Create comprehensive documentation that can help other developers understand the project's scope, progress, and any challenges encountered.
 If you are aware of large swaths of documentation that is sitting around in places (emails, slide decks, pdf files) that are not already available online *with* the source code, consider getting this information *out there*.


1. Establish an enduring on-line presence

   If the project doesn't already have one, create a website.
   There are various free website hosting options.
   A good option is a [GitHub pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#) site because it offers a place to host both a web site about the project and the project's actual source code as well as other project artifacts.

1. Archive the software

   Consider archiving the software.
   There are archival services available such as [DOE Code](https://www.code.gov), [netlib.org](https://netlib.org), [Software Heritage](https://www.softwareheritage.org), [Internet Archive](https://archive.org) and [Archive Team](https://wiki.archiveteam.org/index.php/Main_Page) all of which handle archival of software among other things.
   Another option to consider is archiving the software with a [Digital Object Identifier](https://bssw.io/items/persistent-identifiers-for-software-in-scientific-computing) (DOI) agency.
   There are many DOI agencies often specializing in certain kinds of digital assets.
   Some handle source code.
   Consider [Crossref](https://www.crossref.org), [Zenodo](https://zenodo.org) and [Open Science Framework](https://osf.io).

6. **Archive Assets**: Store all relevant assets, such as design files, mockups, and any research conducted during the project. These assets can be beneficial for future projects or as reference material.

1. Present or Publish (about the software)

   Get at least one piece of literature (conference presentation or proceedings publication) anywhere it may be a good fit where you can write in more detail about the *software* (and less about the science it may enable).
   Often case-studies and lessons learned are good candidate topical areas for a piece of literature about the software itself.
   Publish research papers, technical reports, or whitepapers that discuss the project's methodologies, challenges, and outcomes.
   By actively sharing knowledge of the software design and development, you increase the chances of the community benefiting from the project's know-how.

1. Consider refactoring critical dependencies

   Consider identifying key pieces of the software which may be worth splitting out for a life as an independent package apart from the originating project.
   Engage any stakeholders with down stream dependencies to ask if anyone is interested in taking over maintaining a package.
   Seek researchers working in similar area to see if they may see a benefit to maintaining any of these packages.
   There may be graduate students looking for projects to build upon who may be interested and willing to pick up and build upon a package.
**Evaluate Salvageable Components**: Assess if any parts of the codebase or architecture can be reused in other projects. Salvaging valuable components can save time and effort in future development.

1. Have a Post-Mortem Meeting:

**Lessons Learned**: Conduct a lessons-learned session with the team to capture insights into what went well and what didn't during the project's development. Document these lessons, as they can be valuable for future projects, ensuring that the same mistakes are not repeated.
**Code Review**: If possible, conduct a code review with the team to identify any critical issues or potential security vulnerabilities. This will allow you to address these concerns and prevent them from carrying over to other projects.

**Identify Reasons for Discontinuation**: Understand the reasons why the project is being discontinued. It could be due to budget constraints, changing business priorities, or technical challenges. Knowing these reasons will help in making informed decisions for future projects.
**Post-Mortem Meeting**: Hold a post-mortem meeting with the team to discuss the reasons behind the project's discontinuation and reflect on the overall experience. This can lead to valuable insights for future projects.
**Communication**: Communicate the discontinuation decision transparently and promptly to stakeholders, clients, or anyone affected by the project. Be honest about the reasons and express gratitude to the team for their efforts.

By following these steps, you can effectively discontinue a partially completed software project while retaining the knowledge gained and leveraging the lessons learned for future endeavors.


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


Which modality(s) of communication with former project stakeholders will
be maintained 
`
   The use of mailing list for this purpose should be discouraged and avoided at all costs.

* Identify the modality(s) of contact that will be maintained for any inquiries
  occurring *after* project discontinuation (e.g. email, twitter, GitHub discussions, etc.).

* Identify at least one person (preferrably also a backup) who will serve as point
  of contact for any inquiries occuring after the project is discontinued. If this
  role needs to be transferred

* Some stakeholders should set semi-annual reminders on their calenders just to
  check and confirm the project's on-line presence is still healthy.
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
* On GitHub, projects can be *archived* (converted to read-only)
* What can be done to ensure that if the project gets re-started, it can be easily
  picked back up and restarted by possibly new developers?
* Sponsoring organizations should be willing to allocate a small amount of remaining
  funds for teams to expend effort preparing the project for discontinuation. A good
  motive is helping to ensure the sponsor's investments to that point are not lost
  entirely.
