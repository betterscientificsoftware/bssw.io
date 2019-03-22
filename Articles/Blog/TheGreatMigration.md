# The Great Migration
## Experiences migrating 2 million lines of code and 20 years of development history from Subversion to GitHub.

# DRAFT DRAFT DRAFT

**Hero Image:**

- <a href='https://raw.githubusercontent.com/betterscientificsoftware/images/blog_svn_gh_migration/Blog_TheGreatMigration_car.jpg'><img src='https://raw.githubusercontent.com/betterscientificsoftware/images/blog_svn_gh_migration/Blog_TheGreatMigration_car.jpg' /></a>

#### Contributed by [Holly Auten](https://github.com/hauten) and [Mark C. Miller](https://github.com/markcmiller86)

Software sustainability demands continuous, yet strategic, migration to new technologies. Recent examples
the scientific computing community has been facing include C++ language standards, performance portability
solutions, integrating burst buffers into workflows and revision control systems. The older and bigger a project
is, the more involved such migrations can be. Using recent experiences on the VisIt project, we outline key
issues teams should be aware of and plan for in migrating from Subversion to GitHub.

| ![](https://raw.githubusercontent.com/betterscientificsoftware/images/blog_svn_gh_migration/Blog_TheGreatMigration_table.png) |
|:---:|
| VisIt project development process migrations |

The table above outlines key development processes (*services* column) in the VisIt project and how those process
were supported prior to the GitHub migration. The source code was hosted at NERSC as a *raw* conventional `trunk/branches/tags`
style Subversion repository<sup>b</sup> for more than 10 years prior to migrating to GitHub<sup>a</sup>. For
many reasons, the VisIt project found it convenient to use the Subversion respository not only for source
code revsion control but also as a sort of internet-wide, world-readable shared file space including a lot of
large binary files (e.g. binary releases and tarballs, PowerPoint presentations) for
which revision control was non-essential as well as large binary data for test inputs and outputs.
Over many years of development, this binary content grew in size such that the whole repo was several tens
of gigabytes.

In preparing to migrate to GitHub, we aimed to address this issue along with several other goals of 
a release of a major new version of VisIt, 3.0 *beta*.

* Using Large File Storage (LFS)
* Capturing development history in most *GitHub-natural* way.
* Optimizing use of GitHub bandwidth and storage limits
* Reorganizing our repo for better development workflows
* Migrating issues to GitHub issue tracking
* Miscellaneous other technology updates

## Repository Reorganization for Better Development Workflow

A key goal in the repository re-organization was to ensure a single GitHub repository would
contain *everything* a developer would need including documentation, test tools, data and baselines
yet not suffer any GitHub bandwidth penalties when engaging in development activities not involving
that content. In subversion, a checkout of trunk was so massive it would rarely if ever be done.
Instead, the subversion trunk was split into several top-level directories (src, test, data, docs,
third_party, releases), and only some of those would be checked out by developers. In the new
organization, test, data and docs are all under src and releases, even historical ones of the past,
was re-formulated to manifest properly as *true* GitHub releases. 


## Source Code Repository and History Migration

Migrating the state of a subversion repository at a specific moment in time (e.g. a *snapshot*) is very
simple. However, migrating a large project with a long development history such that the resulting GitHub
repository appears, more or less, as if all the development had originally occurred on GitHub and,
in particular, proper use of LFS for large, binary content, GitHub branches, tags and releases whilst also
capturing development history required advanced scripting of the GitHub api to basically *replay* all
the changes from the old Subversion repo into the new GitHub repo, a process that took hours. In addition,
these scripts were run, results tested and examined, repositories destroyed and re-created, several
times before all the kinks in the process were worked out. The result is....In particular, historical
contributions made by developers years ago are properly captured in GitHub history as are previous releases.

## Issues Migration

A key challenge in migrating issues was mapping Redmine issue metadata
(e.g. trackers, statuses and custom fields, etc.) to their equivalent GitHub notions and/or labels and then
writing a script. To capture all issue history, we wanted to migrate both open and resolved issues. We found
thta capturing Redmine issue comments as *true* GitHub conversations was not easily possible. All original
Redmine conversation was poured into the initial issue submission on GitHub. We also included all Redmine
metadata there as a hedge against unforeseen data loss. A final issue
was attachments. Fewer than 10% of the issues contained attachments. However, there was no way to
migrate these automatically. After migrating the issues themselves (which then defined a mapping
of the old Redmine issue id and the new GitHub issue id) we captured all Redmine attachments renaming
the resulting files with their new GitHub ids. The team then engaged an an attach-a-polooza exercise
where each team member was assigned about 10% of the attachments to manually attach to the appropriate
GitHub issues. That work was quick and easy.

## Other technology Updates

(add a sentence about LFS here)
As part of this major migration effort, we also folded in a number of other technology updates.
We switched from .tar.gz file formats for
our test data to 7z. This reduced the storage (and GitHib bandwidth) by almost half. We upgraded
from VTK-6 to VTK-8 and doing so involved also making a number of improvments to handling of GL, a key
graphics technology critical to any visualization applications. Finally, we migrated documentation
from OpenOffice to Sphinx with ReadTheDocs integration, which involved some scripted conversion to
bootstrap the process followed by a few team sprints to polish the .rst files.
Finally, we updated our BSD 3-clause license verbiage to match GitHub's built-in license recognition.
Still to make some remarks regarding
- LFS
- Travis-CI vs. Circle-CI
- Nightly testing vs. CI vs. "hooks"

Planning the migration took months mainly to make sure we'd position the project 
to optimize developer workflows using GitHub features. Executing the actual migration was only
a matter of days.

Note that nightly testing is not subsumbed by GitHub CI services. That is because nightly testing involves
compiling all of VisIt's dependencies, many of which are non-essential for CI, can take hours to run and
generates about 1/4G of results data. So, when integrating CI

<sup>a</sup>Prior to that, it was hosted in a ClearCase repository private to LLNL.
<sup>b</sup>By *raw*, we mean there was no convenient web *front-end*. It was basic, ssh command-line
access for developers and raw `https://` read-only access for users.
