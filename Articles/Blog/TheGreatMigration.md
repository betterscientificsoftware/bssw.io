# Continuous Technology Refreshment (CTR)
## Most code teams already do it. Here we describe what CTR is and recent tech refresh experiences on VisIt.

**Hero Image:**

- <a href='https://raw.githubusercontent.com/betterscientificsoftware/images/blog_svn_gh_migration/Blog_TheGreatMigration_car.jpg'><img src='https://raw.githubusercontent.com/betterscientificsoftware/images/blog_svn_gh_migration/Blog_TheGreatMigration_car.jpg' /></a>

#### Publication date: April 11, 2019

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86) and [Holly Auten](https://github.com/hauten)

http://info.alphanumeric.com/blog/benefits-establishing-technology-refresh-cycle

In the IT world, the practice of *Continuous Technology Refreshment (CTR)* is defined as the
*periodic upgrade or replacement of infrastructure to deliver continued reliability, improved speed,
capacity and/or new features*. Technology refresh is a term used primarily for replacing obsolete *hardware*.
But, long lived *software* projects often wind up having to engage in equivalent work.
Recent examples of CTR for software scientific computing teams have faced include wide-spread adoption of new 
language standards, integration of performance portability solutions, application of burst buffers in
workflow and even new revision control systems. The longer lived and bigger a project is, the more
involved technology refresh can be. Using recent work for a major release of VisIt, 3.0.0 Beta,
we describe experiences and lessons learned refreshing several technologies
* Routine repository housekeeping and reorganization
* Source revision control: Subversion to GitHub
* Large binary content: Subversion to GitHub-LFS
* Issue tracking: Redmine to GitHub Issues
* Documentation: OpenOffice to Sphinx+ReadTheDocs
* Other Misc. Refreshments Completed and Planned

### Routine repository housekeeping and reorganization
In addition, as the code evolved the organization of development resources within the repo got
diffused and required some basic housekeeping and reorganization.

With Subversion, in the past the VisIt project team found it convenient to also use the repo as a sort of
internet-wide, world-readable shared file space including a lot of large binary files such as pre-built
release binaries and tar files, PowerPoint presentations, data ensembles used in tutorials, etc. These
didn't really require revision control and were only in the repo because it was a convenient way to *host*
the content on-line. Over many years of development, this and other binary content used in testing grew
in size making working with the whole repo unwieldly. For example, branch creation could take more than
an hour. In moving to GitHub, a key aim was to utilize GitHub Large File Support (LFS) to address issues
with this large binary content correctly. Because basic GitHub LFS has bandwidth and storage limits, we
needed to purchase upgraded LFS service.

### Source code repository and history migration
Migrating a single branch of a small project from Subversion to GitHub is trivial. There are several
tools available for this such as XXX. However, migrating all branches, tags and releases of a large project
(whilst side-stepping history of large binary content as described above) such that they are realized in
Git *correctly*, is complicated. There are no publicly available tools for doing this out of the box.

However, migrating a large project with a long development history such that the resulting GitHub
repository appears, more or less, as if all the development had originally occurred on GitHub and,
in particular, proper use of LFS for large, binary content, GitHub branches, tags and releases while also
capturing development history required advanced scripting of the GitHub api to basically *replay* all
the changes from the old Subversion repo into the new GitHub repo, a process that took hours. In addition,
these scripts were run, results tested and examined, repositories destroyed and re-created, several
times before all the kinks in the process were worked out. The result is....In particular, historical
contributions made by developers years ago are properly captured in GitHub history as are previous releases.

### Issues migration

A key challenge in migrating issues was mapping Redmine issue metadata
(e.g. trackers, statuses and custom fields, etc.) to their equivalent GitHub notions and/or labels and then
writing a script. To capture all issue history, we wanted to migrate both open and resolved issues. We found
that capturing Redmine issue comments as *true* GitHub conversations was not easily possible. All original
Redmine conversation was poured into the initial issue submission on GitHub. We also included all Redmine
metadata there as a hedge against unforeseen data loss. A final challenge
was attachments. Fewer than 10% of the issues contained attachments. However, attachments could be migrated
only manually. After migrating the issues themselves (which then defined a mapping between the old
Redmine and new GitHub issue ids), we scripted download of all Redmine attachments renaming
the resulting files with their new GitHub ids. The team then engaged an an attach-a-polooza exercise
where each team member was assigned about 10% of the attachments to manually attach to the appropriate
GitHub issues. The planning made that tedious work quick and easy.
Can we add detail links?

### Documentation
Finally, we migrated VisIt's GUI User Manual from OpenOffice to Sphinx+ReadTheDocs. This involved an initial
converstion script to bootstrap the process generating an initial restructured text output. Then, the
team engaged in 3-4 of documentation sprints, each of length 2-3 hours, manually reading, fixing, reogranizing,
updating and polishing the resulting .rst files. VisIt's CLI (Python) User Manual existed as a compileable
C code in the form of Python docstrings. This design facilitates in-line help within Python as well as 
Still completing migration of Python Doc strings to .rst files.

### Other refreshes completed or still in progress

When making big changes, it is a good idea to combine as many of them together as possible rather than
dribble out each over numerous releases. As part of the 3.0 beta release, the VisIt team also refreshed
or plans to refresh
* from VTK-6 to VTK-8
  * This required also refreshing GL, a key graphics technology critical to any visualization application
  * There is a still a small backlog testing issues related to VTK-8 changes we are working to complete.
* from `.tar.gz` to `.7z` for binary test data
  * This reduced storage of test data by almost 50%
  * Because `7z` isn't as ubiquitous as `.tar.gz` we've yet to switch to it for release binaries.
* Commit hooks
  * We have yet to convert several Subversion commit hooks to check things such as tabs, calls to abort(), file name case clashing
    to work in the new GitHub repo.
* Nightly testing vs. CI testing
  * We opted for Circle-CI for our CI tests on GitHub and this presently involves just compilation testing
  * We plan to refactor or test suite to define a subset suitable for CI testing
  * Note that nightly testing is not subsumbed by GitHub CI services. That is because nightly testing involves
    compiling all of VisIt's dependencies, many of which are non-essential for CI, can take hours to run and
    generates about 1/4G of results data.
* Web site and Testing Dashboard
  * We plan to migrate these to GitHub as well but that will happen later this year.
 
Most code teams find it necessary to engage in regular technology refresh activity often in response 
to changing development workflow. For example, in its 25+ year long history, the PETSc project has refreshed
revision control systems on four separate occasions. Each of these changes was motivated by the growing set of
distributed developers collaborating on PETSc. Technology refresh can represent a lot of work. Proper planning,
prototyping and testing can help to make it go more smoothly.

### Footnotes
- <sup>a</sup>Prior to that, it was hosted in a ClearCase repository private to LLNL.
- <sup>b</sup>By *raw*, we mean there was no convenient web *front-end*. It was basic, ssh command-line
access for developers and raw `https://` read-only access for users.

### Autho bios

Mark Miller ...

Holly Auten ....

Guidance for author bio:
- Length: 50-100 words (paragraph form).
- Can include hyperlinks.
- Mention your current position, employer, a bit about your background.
- Include info about your interests related to software productivity and sustainability.
- Anything else you want to mention.


<!--
Publish: preview
RSS update: 2019-04-XX
Categories: development
Topics: version control
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
-->

