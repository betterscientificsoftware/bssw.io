# Discontinuing a Research Software Project

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: January 22, 2024

<!--deck text start-->
A software (research) project can be discontinued in a way that allows stakeholders a smooth transition, the mining of lessons learned and useful subcomponents, and even to pick the project back up again if desired.
<!--deck text end-->

Software projects in High Performance Computing (HPC) / Computational Science and Engineering (CSE) involve at least two kinds of *deep* knowledge.
One is the computational science the software aims to enable.
The other is the computer science (aka software engineering) involved in designing, developing, deploying, and supporting the software for users.

Because the ultimate goal of most HPC/CSE projects is the advancement of the underlying science, publications concerning the computational science knowledge are often the priority.
When such a project ends, the primary risk of computational science knowledge loss involves reproducibility.
Setting reproducibility aside, most other aspects of the computational science knowledge are often captured in perpetuity in the publicly available literature.
On the other hand, the computer science knowledge is often at risk of being lost.

Scientific computing research software projects can come to an end in ways that ultimately impact our community's ability to ever reap any benefit from progress made or lessons learned or otherwise have available for posterity's sake any of the system design, architecture, implementation and software engineering know-how that went into the project.
We all can likely think of example projects where this has happened.

Software projects come to an end for a variety of reasons.
A newer project can render an older project obsolete.
The market or need for a capability can dwindle or completely disappear.
A sponsoring organization can wind up making a strategic decision to discontinue a software project.
Funding can run out.

Many *research* software projects have built-in sunset dates when the sponsoring organization's funding ends.
For SciDAC projects for example, a common duration is 3-5 years.
If a project is unable to gain traction within the community and win funding from other sources in that time frame, the project will most likely be discontinued.

Over time, project assets and artifacts and even contact information of the people involved can fall out of date and/or become inaccessible.
A common situation is a domain name and/or institutional domain alias/forward that expires.
When this happens, the main entry point to the project known throughout the community is lost.
Future researchers are then unable to discover the project even existed let alone find anyone with knowledge about it.

There are things project stakeholders and sponsoring organizations can do to *gracefully* discontinue a software project in such a way that the computer science knowledge remains available for the benefit of the community.
Firstly, the sponsor can actually fund the various activities (mentioned below) to gracefully discontinue the project.

Here we outline a number of actions software project members can take to ensure computer science knowledge will remain accessible after a project comes to an end.
With fair warning, a project can move to *tidy things up* before all funding is lost.

## Gracefully discontinuing

When there is a planned sunset date or with fair warning, taking any of the actions outlined below is easier than trying to cram them in at the last minute if funding is suddenly and unexpectedly lost.
If work must cease immediately, we acknowledge few of the actions listed here may be possible.

### Make an end-of-project release

   The purpose of an end-of-project release is to capture not only the most up to date version of the software but also as much of the computer science knowledge that is not already available through other resources.
   When scrambling to make an end-of-project release, there may be critical bug fix or feature enhancement work to bring to a close.
   If the project is hosted in a public repo, simply documenting which branches hold which critical work may be sufficient.
   Otherwise, merging in-progress work to the main line of development but conditionally disabling it (via CPP `#if` or `#ifdef` conditionals) may be appropriate.

   Alternatively, if the only publicly available artifact will be the release tarball itself, creating multiple variants of the associated source files will help to ensure critical in-progress work remains accessible for posterity.
   An untimely end-of-project release may mean hastily written testing and documentation.
   That's ok.
   It may even be below the quality standards that the project is accustomed to maintaining.
   That's ok too.
   If so, the release can be identified as *development* or *experimental* to help clarify these issues.
   Remember, the goal is primarily to document and make available critical computer science knowledge for others who may want to follow in your footsteps.

### Open-source the code

   If the project's source code is not already open source, a key way to ensure the computer science knowledge remains available to the community is to release it under a widely adopted open-source license.
   The institution(s) that sponsored development of the software may have specific processes to follow to release it as open-source.
   For example, Livermore Labs' Information Management (IM) office defines [a set of processes](https://computing.llnl.gov/sites/default/files/COMP_Poster_OSS.pdf) to follow for open-source releases.
   By making a project's software open source, it becomes possible to host the software in world-readable, public places (e.g., GitHub or GitLab) where the community can find it and learn from it.
   In these cases, it is best to choose a *permissive* type open source license that includes a *disclaimer of warranty*.
   Most open source licenses do. 
   Good options are [MIT](https://opensource.org/license/mit/) or [ISC](https://www.isc.org/licenses/).

### Document final status

   For a project that is quickly ending, there is likely very little resource available to fill in any *massive* gaps in documentation.
   In addition, the role of any remaining documentation effort should be to try to capture as complete a snapshot of the computer science knowledge as practical.
   This could be as simple as bunch of bulleted statements in a `final-status.txt` file at the root of the source code tree. 

   The goal is to capture, without too much effort, the software's design objectives, methodologies, and key findings.
   Include key design decisions, architecture notes, algorithms, and implementation details that may be valuable to others.
   If large swaths of documentation are located in restricted places (emails, slide decks, pdf files) that are not already available online and/or *with* the source code, consider getting this information *out there* with the source code as well, possibly by adding the relevant artifacts to the repository holding the source code.

### Establish an enduring on-line presence

   If the project doesn't already have a web site, create one.
   Even a single-page site that describes the software at a high level would be fine for this purpose.
   There are various free website hosting options.
   A good one is a [GitHub pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#) site because it offers a place to host both a web site about the project and the project's actual source code as well as other project artifacts.

### Archive the software

   Consider archiving the software with an online archival service.
   There are archival services available such as [DOE Code](https://www.code.gov), [netlib.org](https://netlib.org), [Software Heritage](https://www.softwareheritage.org), [Internet Archive](https://archive.org) and [Archive Team](https://wiki.archiveteam.org/index.php/Main_Page), which handle archival of software among other things.
   Another option to consider is archiving the software with a [Digital Object Identifier](https://bssw.io/items/persistent-identifiers-for-software-in-scientific-computing) (DOI) agency.
   There are many DOI agencies often specializing in certain kinds of digital assets; some handle source code.
   Consider [Crossref](https://www.crossref.org), [Zenodo](https://zenodo.org) and [Open Science Framework](https://osf.io).

### Present or publish

   Try to get at least one piece of literature (conference presentation or proceedings publication) anywhere it may be a good fit where one can write in more detail about the computer science known-how.
   Often case-studies and lessons learned are good candidate topical areas for a piece of literature focusing on the computer science aspects of the project.
   Published research papers, technical reports, or white papers that discuss the project's methodologies, challenges, and outcomes are a great way to capture the computer science knowledge of a project.

### Refactor critical dependencies

   Instead of the *whole* code base, it may be appropriate to carve out *pieces* of the code for the actions we're discussing here.
   Assess whether any parts of the code base or architecture can be reused in other projects.
   Salvaging valuable components can save time and effort in future development.
   Depending on how the software is architected, the work to refactor any such pieces of the code may be doable before funding runs out.
   Stakeholders with downstream dependencies that are highly localized to a refactorable piece of the code base may even be willing to take over maintaining that piece as its own package.
   Reach out to researchers working in a similar area to explore whether they could benefit from maintaining a *piece*.
   Graduate students looking for projects may be interested and willing to pick up and build upon a package.

### Gather lessons learned

   Conduct a lessons-learned session with the team to capture insights into what went well and what didn't during the project's development.
   Document these lessons, as they can be valuable for future projects, ensuring that the same mistakes are not repeated.
   If possible, conduct a code review of the final state of the code with the team to identify any critical issues or potential security vulnerabilities.
   Key findings should be documented so that others can be made aware of them.

   Understand the reasons why the project is being discontinued, for example, due to budget constraints, changing business priorities, or technical challenges.
   Knowing these reasons will help anyone following in your footsteps in making informed decisions for future projects.

   Hold a postmortem meeting with the team to discuss the reasons behind the project's discontinuation and reflect on the overall experience.
   Capture various key details of this discussion in some form to be included with other documentation.

### Communications

   The decision to discontinue a project needs to be communicated as soon as possible to all stakeholders.
   Whenever possible, be open and honest about the reasons and express gratitude for contributors' efforts.
   The sooner existing users are notified that the software is losing support, the more time they will have to consider what to do.

   One of the first things to decide is whether future project *communications* will go on some form of life-support or be discontinued entirely.
   Having life-support communications is obviously preferred, but it comes at some non-zero cost and so may not be practical in all cases.
   For life-support, it is important to identify *how* (e.g., email, chat services, etc.) any inquiries will be handled and by *whom*.
   This information should be posted prominently in all of the online spaces where the project has a presence.

   Even if communications will be discontinued entirely, it may make sense to provide way for inquirers to *register* their interest by a sign-up process that collects contact information.
   GitHub reactions can be used for this purpose.

   For projects that involve persistent data formats, provide users with documentation about how to convert their data to another format.
   For projects for which decent alternative software products exist, ensure that users are aware of these alternatives.

### What about reproducibility?

In this article, we have set aside the issue of reproducibility and the impact discontinuing a project can have on reproducibility.
That is not because we do not think reproducibility is important.
It is more a question of whose resources are responsible for addressing reproducibility concerns resulting from a project being discontinued.
Undoubtedly, projects can engage in practices that either help or hinder post-project reproducibility.
Many of the actions suggested here will likely help.
Nonetheless, the extent to which a project that has lost funding can be held responsible for reproducibility is an open question and outside the scope of this article.

## Conclusions

HPC/CSE software projects involve at least two kinds of *deep* knowledge.
One is the computational science the software enables, which is usually captured in publications where the science results from the project are described.
The other is the computer science (aka software engineering) know-how.
Important aspects of that knowledge is often at risk of being lost when a project is discontinued.

By following many of the suggested actions in this article, a project can be effectively discontinued in a partially completed state while retaining as much of the computer science knowledge as possible for posterity.

## Author bio

Mark C. Miller is a computer scientist supporting the
[WSC](https://wci.llnl.gov/about-us/weapon-simulation-and-computing)
program at [LLNL](https://www.llnl.gov) since 1995.
Among other things, he contributes to
[VisIt](https://wci.llnl.gov/simulation/computer-codes/visit),
[Silo](https://wci.llnl.gov/simulation/computer-codes/silo),
[HDF5](https://www.hdfgroup.org) and
[IDEAS-ECP](https://ideas-productivity.org/activities/ideas-ecp/).

<!---
Publish: yes
Track: how to
Pinned: no
Topics: projects and organizations, funding sources and programs, reproducibility, software sustainability
RSS updaate: 2024-01-22
--->
