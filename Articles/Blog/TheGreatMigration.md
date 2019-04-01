# Continuous Technology Refreshment (CTR)
### Here we demonstrate what CTR is with recent tech refresh experiences on VisIt.

**Hero Image:**

- <a href='https://raw.githubusercontent.com/betterscientificsoftware/images/blog_svn_gh_migration/Blog_TheGreatMigration_bikes.png'><img src='https://raw.githubusercontent.com/betterscientificsoftware/images/blog_svn_gh_migration/Blog_TheGreatMigration_bikes.png' /></a>

#### Publication date: April 11, 2019

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86) and [Holly Auten](https://github.com/hauten)

In the IT world, the practice of
[*Continuous Technology Refreshment (CTR)*](http://info.alphanumeric.com/blog/benefits-establishing-technology-refresh-cycle)
is defined as the *periodic upgrade or replacement of infrastructure to deliver continued reliability, improved speed,
capacity and/or new features*. The term is used primarily for replacing obsolete *hardware*.
But, long lived *software* projects often wind up having to engage in equivalent activity.
Examples of CTR scientific computing software include wide-spread adoption of new 
language standards, integration of performance portability solutions, application of burst buffers in
workflow and even new revision control systems. The longer lived and bigger a project is, the more
involved technology refresh can be. Using recent work for a major release of
[VisIt](https://wci.llnl.gov/simulation/computer-codes/visit/), 3.0.0 Beta,
we describe experiences and lessons learned refreshing several technologies
* Wrangling binary content: Subversion to GitHub [Large File Support (LFS)](https://www.git-tower.com/learn/git/ebook/en/desktop-gui/advanced-topics/git-lfs)
* Revision control: Subversion to GitHub
* Issue tracking: Redmine to GitHub Issues
* Documentation: OpenOffice to Sphinx+ReadTheDocs
* Other Misc. Refreshments Completed and Planned

### Wrangling binary content: Subversion to GitHub Large File Support (LFS)
Due to lack of hosting alternatives, the VisIt team wound up having to use its Subversion repo as a sort of
internet-wide, world-readable shared file space including a lot of large binary files such as pre-built
release binaries and tar files, PowerPoint presentations, data ensembles used in tutorials, etc. These
didn't really require revision control and were in the repo only because it was the only means avaiable to
*host* the content on-line. Binary content is very
[problematic](https://hackernoon.com/what-should-be-in-version-control-d5f16e9a2bf2)
for revsion control systems. Over many years of development, this and other binary content used in testing grew
in size making working with the whole repo unwieldly. For example, branch creation could take more than
an hour. In moving to GitHub, a key aim was to utilize Git Large File Support (LFS) to address issues
with this large binary content correctly. Because basic GitHub LFS has bandwidth and storage limits, we
needed to purchase upgraded LFS service. $300 buys us 300 Gb of storage and 3Tb/year of data transfer.

### Revision control: Subversion to GitHub
Migrating a few branches of a small project from [Subversion to GitHub](https://blog.axosoft.com/migrating-git-svn/)
is trivial. A Google search of
[*migrate from subversion to git*](https://www.google.com/search?q=migrate+from+subversion+to+git&oq=migrate+from+subversion+to+git&aqs=chrome..69i57j0l5.2131j0j8&sourceid=chrome&ie=UTF-8)
reveals many options. However, there are no tools for migrating many branches, tags and releases of a large project
with a long development history while also culling and/or LFS'ing unwieldly binary content (described above)
such that the resulting GitHub repo captures all history and looks, more or less, as if all
the development had originally occurred on GitHub. We developed and tested custom Python scripts to basically
*replay* all the changes from the old Subversion repo into the new GitHub repo. The process takes hours.
In addition, these scripts were tested, results examined, repositories destroyed and re-created, several
times before all the kinks in the process were worked out. [The result](https://github.com/visit-dav/visit)
is that key branches and tags, all release
and development history are captured on GitHub in what one would expect to be the GitHub-native way.
Furthermore unwieldly binary content is properly LSF'd with only the revision history of essential binary
content is captured. We reduced the size of the repository from several tens of gigabytes in Subversion to
under half a gigabyte in Git.

### Issues migration
A key challenge in migrating issues was mapping Redmine issue metadata
(e.g. trackers, statuses and custom fields, etc.) to reasonable GitHub equivalents and then
automating the conversion with a script. To capture all issue history, we migrated both open and resolved issues.
We found that capturing Redmine issue comments as *true* GitHub conversations was not easily possible. All original
Redmine conversation was poured into the initial GitHub issue submission. We also included all Redmine
metadata there as a hedge against unforeseen data loss. A final challenge was attachments. Fewer than 10% of the
issues contained attachments. However, GitHub offered no way to automate adding attachments to issues.
After migrating the issues themselves (which then defined a mapping between the old
Redmine and new GitHub issue ids), we scripted download of all Redmine attachments renaming
the resulting files with their new GitHub ids. The team then engaged an an *attach-a-polooza* exercise
where each member was assigned about 10% of the attachments to manually attach to the appropriate
GitHub issues. The planning made this tedious work quick and easy.

### Documentation
Finally, we migrated VisIt's GUI User Manual from OpenOffice to
[Sphinx](http://www.sphinx-doc.org/en/master/) and [ReadTheDocs](https://readthedocs.org).
This involved an converstion script to bootstrap the process generating an initial
[restructured text](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) output. Then, the
team engaged in 3-4 documentation sprints, each of length 2-3 hours, manually reviewing, fixing, reogranizing,
and polishing the resulting `.rst` files. VisIt's CLI (Python) User Manual existed as compileable
C code in the form of Python docstrings. This design facilitates in-line help within Python
(e.g. `>>> help(myFunc)`) but is otherwise not the best format for humans to write documentation. We wrote
a script to automate conversion of the C code Python doc-strings to `.rst` files. We were very happy
with [the result](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/).

### Other refreshes completed or still in progress

When making big changes, it is a good idea to combine as many together as possible rather than
dribble them out over numerous releases. As part of the 3.0 beta release, the VisIt team also refreshed
from VTK-6 to VTK-8 (necessitating refreshing GL infrastructure as well), 
from `.tar.gz` to `.7z` for binary test data (reduced storage by 50%). And, we plan to refresh later this
year commit hooks (for tab characters, `abort()` calls, file name case clasing, etc.),
CI testing (we are presently testing only proper compilation), as well as moving our Web site and Test Dashboard
to GitHub.
 
### Summary
The HPC software community doesn't typically use the term *Continuous Technology Refreshment* because it is
seen as applying only to hardware. However, we hope this article describing recent experiences on the VisIt
project, which are by no means unique amoung HPC code teams, demonstrates that CTR is equally applicable to software.
Most code teams find it necessary to engage in activities similar to those described here on a regular basis often
in response to changing development workflow needs.  For example, in its 25+ year long history, the
[PETSc](https://www.mcs.anl.gov/petsc/) project
has refreshed revision control systems on four separate occasions. Each of these changes was motivated by the
growing set of distributed developers collaborating on PETSc. Technology refresh can represent a lot of work.
Proper planning, prototyping and testing can help to make it go more smoothly.

### Autho bios

Mark Miller is a computer scientist supporting [WSC](https://wci.llnl.gov/about-us/weapon-simulation-and-computing)
program at [LLNL](https://www.llnl.gov) since 1995.
He is a contributor to
[VisIt](https://wci.llnl.gov/simulation/computer-codes/visit)
and the lead developer of
[Silo](https://wci.llnl.gov/simulation/computer-codes/silo). He is also a contributor to the
[IDEAS-ECP](https://ideas-productivity.org/ideas-ecp/) project.

Holly Auten is the Web Content Lead for the Computation Web Team and
routinely contributes articles regarding various aspects of on-going software
development activities within the Computation department at [LLNL](https://www.llnl.gov).

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

