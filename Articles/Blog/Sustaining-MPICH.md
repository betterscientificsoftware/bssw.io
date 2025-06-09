# Sustaining MPICH: 30+ Years of High-Performance Computing Software*

## **Introduction**

In high-performance computing, MPI is known as the de facto standard
programming model for parallel applications. In the era before MPI, HPC
vendors each provided their own communication API for scaling
applications on multiple processors. The differences in APIs meant that
applications needed to be modified to run on different machines and/or
networks. The development of the MPI was an effort to standardize the
communication constructs for parallel applications. Users could write
their codes once and run anywhere MPI was supported, without having to
know the details of the underlying system.

MPICH was the first publicly available implementation of MPI, and has
been continually developed since its inception. This May, MPICH was
announced as the latest recipient of the [ACM Software System
Award][acm-award]. The award "recognizes MPICH for powering 30 years of
progress in computational science and engineering by providing scalable,
robust, and portable communication software for parallel computers". It
is an honor to be recognized alongside other significant award winners
such as GCC, Unix, TCP/IP, Java, and more. In this article we will look
at some of the key aspects of MPICH's success as a software project and
how they have sustained the project for 30+ years.

## **Origins and Evolution**

The MPICH project was founded during the development of the MPI-1
Standard, and closely tracked its evolution prior to initial
publication. MPICH was instrumental to MPI's success in that it served
as a valuable proving ground, showcasing that the standard was practical
to implement and use. Distributing MPICH as open source made MPI
accessible to everyone, and with its permissive license, provided
vendors with a solid foundation to base their own MPI implementations.

From the beginning, MPICH was designed for extension. Its permissive
license allowed vendors to package and sell software derived from MPICH
without the need for licensing or fees. The core code was developed to
adhere to the C89 (later C99) standard, which is widely portable. The
internal abstractions in MPICH isolated the "generic" parts of
implementing MPI, such as argument validation, object management, and
functionality tests from the nitty gritty machine-dependent code. These
design choices meant that the code needed to extend MPICH to support a
new platform was relatively small, but offered enough flexibility to get
the best performance.

Over time, MPICH has grown from primarily research-oriented development
to a viable production software library. Rigorous testing
infrastructure, built with the help of vendor partners, now verifies
each change and/or addition to the code. Recently, more MPICH partners
have begun pushing their development directly to upstream rather than
remaining in a separate fork or closed source. The resulting ecosystem
empowers users to build and use the latest MPICH not only on laptops and
workstations, but on many of the top HPC systems in the world.

## **Sustainability Practices**

MPICH is a large software project consisting of hundreds of thousands of
lines of code written over 30+ years. The core development team at
Argonne is small (3-5 people), developers change over time, and not all
participate on the project as their sole effort. Code maintainability
therefore is of critical importance. What does that mean for MPICH and
how do we achieve it?

### **Revision Control**

[Revision control][revision-control] is essential for developing a large
software project like MPICH. Often with multiple developers working on
the project simultaneously, revision control helps to make sense of the
changes being made to the code. In MPICH, an emphasis is placed on good
commit practices. Do the commits in a pull request stand on their own?
Does each commit message explain what change is being made and why?
These are helpful breadcrumbs for developers and users when they are
investigating some issue in the code. Commit messages capture the
context of a change when it was made, moreso than inline comments which
can get stale over time. Furthermore, tools like [git bisect][bisect]
are better able to track down the exact commit a bug was introduced when
every commit can be built and tested independently.

Over the years, MPICH has used a number of [revision
control][revision-control] systems. Lost to time are the [RCS][rcs] logs
from the earliest days of the project. Following the trends in open
source software management, MPICH transitioned to CVS, then Subversion,
and finally Git. These transitions were not always straightforward. When
MPICH adopted Subversion, the decision was made not to import prior
history from CVS, likely due to a lack of good tooling for the import
process. Instead, the entire repository was imported as a single "big
bang" commit that functionally erased prior history. This was
detrimental to our ability to trace development history back beyond a
certain point. Thankfully, tooling eventually improved and the MPICH CVS
history was successfully ported to Git. To avoid rewriting the history
of the main repository, it lives in a [separate repo][mpich-cvs] for
historical purposes. Perhaps if/when Git is overtaken in popularity by
another revision control system, the history can once again be combined.

### **Issue Tracking**

Hand in hand with revision control is [issue
tracking][issue-tracking]. MPICH has relied on issue tracking software
for many years to keep track of all types of easily forgotten tasks. Bug
reports, new feature development, performance regressions, testing
issues, etc., are all entered into the publicly available tracker on our
GitHub page. From there, developers can tag, sort, and filter bugs for
importance and users can track the resolutions of their individual
issues. Release plans list all the issues required to be closed for
completeness.

Before the ubiquity of web-based issue tracking software, MPICH utilized
[req][req] for managing issues. As more and more projects moved to
web-based workflows, MPICH adopted [Trac][trac] along with its move to
Subversion for revision control. Trac offered a convenient web interface
for viewing, searching, and modifying issues. It also offered neat
integrations with the underlying source code management, like the
ability to close issues with special phrases in the commit message that
resolved them. These integrations were maintained even when MPICH
transitioned to Git, as Trac offered native support for both Subversion
and Git. However, the MPICH Trac site was internally managed at Argonne,
and eventually became burdensome to maintain. New release, security
patches, and environment updates by the Argonne IT team led to frequent
downtimes.

In 2016, GitHub eventually became the sole home for MPICH source code
and issue tracking. GitHub was (and is) widely popular with open source
projects because of its modern features and free hosting
options. Third-party tools allowed us to import issue history from Trac
to GitHub so that important context was carried over from one system to
the other, and eliminated the need to maintain both sites for an
extended period of time. Today, users can find the latest MPICH
development and releases all in one place using the same workflows
common to many open source projects.

### **Pull Requests**

For changes to the MPICH source code, we use a pull request workflow
typical of many of todays projects. In order for a pull request to be
approved for merge, it must first pass a number of automated checks. All
changes are checked for code style, contributor agreement, compiler
warnings, test regressions, and even spelling mistakes via continuous
integration scripts. This automation is helpful because it makes many
aspects of the pull request process mechanical and frees up developers
to focus on the most important part of the process -- code review.

The MPICH code review process places are premium on on _understanding_
proposed changes. The author must communicate to the reviewer why and
how the changes are being made. It is one thing for code to work, but to
be maintainable it must be understandable. That means that if the same
code needs to be modified by someone other than the original author, the
chances are higher it can be done in a reasonable amount of time and
without unintentionally breaking things. Some questions we ask when
reviewing code: Is this code easy to understand? If not, is the
complexity needed to achieve a goal? Can the code be simplified without
losing functionality or performance? Simple code is preferable because
it is easier to debug and modify, but complexity may sometimes be
necessary, e.g. to improve performance of a critical function. As
developers, we prefer that complexity be isolated (and documented) as
much as possible to avoid polluting otherwise straightforward code.

Carefully formatting commits and answering these types of questions can
seem burdensome, but it is critical to maintainability. Guidelines for
commit best practices are desribed in our [developer
documentation][devel-docs] so contributors are not flying blind. Also in
our documentation are [_coding standards_][standards]. This is where we
state in clear terms how MPICH code should be written to help both the
author and the reviewer know what is acceptable.

### **Design for Extension**

Emphasizing maintainability allows MPICH the flexibility needed to be a
vehicle for extension. For example, MPICH partners who wish to extend
and optimize MPICH to work on their preferred platform. Previous
target platforms of such work include IBM BlueGene, SiCortex, Infiniband,
OmniPath, and many others. The extend and optimize model has been
critical to the continued success of MPICH, and any impediments to this
extension work would risk driving developers (and users)
away.

Typically, MPICH partners are only interested in the machine-dependent
areas of the code. That is, internal APIs for supporting inter- or
intra-node memory communication. They are happy to leave the chores of
argument validation and object management to the core MPICH team. Clean
layering of the software in MPICH makes requirements and expectation
clear for developers looking to add new code for their platform. In most
cases, fallback or reference implementations of MPI functionality exist
and can easily be plugged into a machine-dependent module. Developers
need only implement the pieces of software that matter most for their
users.

## **Community Engagement**

Maintaining code is a challenge unto itself, but so is knowing what code
to write in the first place. For MPICH, community participation is
crucial to ensuring the software we produce is in-demand..

### **Mailing Lists**

Even before the advent of revision control systems and issue trackers,
email was widely used by open source developers to conveniently share
updates and interact with users from around the world. MPICH has
maintained a number of public mailing lists over the years, the core
three being:

discuss@mpich.org: for user-focused discussions of issues installing and
  using MPICH.
devel@mpich.org: for developer-focused discussions of
  MPICH code
announce@mpich.org: broadcast-only list for MPICH release
  announcements

These lists see less traffic than in the past primarily because most
users and developers now go directly to GitHub. Nevertheless, for those
that either do not have GitHub accounts or prefer to work over email,
they remain a useful option.

### MPI Forum

MPICH developers have participated in the MPI standardization process
since the beginning. The [MPI Forum][forum] continues meeting to this
day to discuss updates and changes to the standard based on new
research. MPICH strives to be the first implementation to support the
newest MPI standard releases as they are published. This benefits our
downstream partners as they can quickly addapt the new code and include
it in release of their own.

MPICH participation goes beyond just implementating the new
standards. We develop original proposals, provide feedback on others'
work, and help to publicize activities of the forum with the broader MPI
user community.

### MPICH Community

The MPICH distribution model has historically been vendor-driven. The
core MPICH team puts out new releases, and our downstream partners would
take those and port their additions and optimizations for releases of
their own. Keeping everyone up-to-date on the core code changes can be
challenging considering the number of interested parties and their
geographical distribution. A strong community model is necessary to
avoid disruptions in development.

For many years, the MPICH team has hosted a Birds-of-a-Feather session
at the [Supercomputing][sc] conference. The BoF is a gathering of MPICH
developers and users to share release plans, new research, and otherwise
discuss whatever issues people are facing with MPICH software. However,
this de facto annual developer meeting could not go in-depth on many
issues due to the relatively short 90-minute format. For deeper
discussions, another venue was needed. In 2018, we began hosting a
weekly virtual developer meeting just as MPICH was undergoing a large
internal redesign effort. Many institutions were helping the core
Argonne team with this effort, so the goal of the meeting was to share
updates discuss any hot-button issues that could block peoples'
progress.

These weekly meetings continue today, well after the initial redesign
was completed. They are regularly attended by developers from a number
of companies and research institutions. We continue to encourage
external collaborators to attend and give feedback on our work. These
interactions help us be aware of any external issues, and plan
developments to address key issues or features in-demand by the
community.

### **MPICH on Aurora (or MPICH in Production)**

Funding for MPICH development primarily comes from the Department of
Energy's Advanced Scientific Computing Research (ASCR) program. MPICH
remains a research project at its core even though its derivitives are
used on many large-scale production systems.

The [Aurora][aurora] supercomputer at Argonne's Leadership Computing
Facility is the second machine in the world to break the exaflop
barrier. Built by Intel in partnership with Hewlett Packard Enterprise,
the massive machine relies on MPICH to scale scientific applications
beyond previous hardware-imposed limits. Aurora represents a deepening
of the partnerships between MPICH, Intel, and ALCF. It also has
pushed MPICH to be a producion-ready library in new ways.

With Intel, code changes for Aurora were contributed directly to
upstream MPICH, rather than in the closed source Intel MPI
library. Regular meetings and hackathons were held with Intel developers
to solve Aurora-related issues and ensure agreement on development
direction. Being part of open-source MPICH means that system
administrators can quickly generate new MPICH builds for evaluation and
testing on the system, leading to shorter wait times for new features
and bug fixes.

The MPICH team has also been working closely with ALCF application
developers and experts to understand the workloads running on the
machine. This input has been critical for also guiding development to
directly enable applications to run efficiently and at-scale. At the
same time, we have spent considerable effort with the ALCF team to
implement additional testing infrastructure for MPICH on Aurora. These
tests monitor MPICH changes for regression in both correctness and
performance, leading to more stable and consistent performance of the
machine for users.

## Conclusion

There are no secrets to MPICH's success that led to its selection as the
2024 ACM Software System Award winner. As discussed, the priciples of
sustainability are many of the same topics that have already been
covered on the Better Scientific Software website. Well-implemented
revision control, issue tracking, and code review are necessary for a
healthy software project with many active contributors. Projects must
also regularly engage with their community to gather feedback and
requirements to guide future directions. A bit of good fortune also
helps, like the rare instance of multi-vendor cooperation that led to
the MPI standard in the first place. Or the willingness of the Aurora
system designers and builders to embrace open-source and contribute
directly to upstream MPICH.

The work of software sustainability is not necessarily difficult, but it
is constant. Continued funding support from the Department of Energy
kept MPICH in active development all these years, leading to adoption
from vendors and users and laying the groundwork for MPI to become the
de facto standard programming model for scientific software. We are
grateful for everyone who has contributed to the software over the years
and look forward to its continued success in the years to come.

---

[devel-docs](https://github.com/pmodels/mpich/blob/main/doc/wiki/developer_guide.md)
[standards](https://github.com/pmodels/mpich/blob/main/doc/wiki/source_code/Coding_Standards.md)
[revision-control](https://bssw.io/items/what-is-revision-control)
[bisect](https://git-scm.com/docs/git-bisect)
[mpich-cvs](https://github.com/pmodels/mpich-CVS)
[issue-tracking](https://bssw.io/items/what-is-issue-tracking)
[req](https://www.usenix.org/conference/lisa-viii/managing-ever-growing-do-list)
[trac](https://trac.edgewall.org/)
[cla](https://en.wikipedia.org/wiki/Contributor_License_Agreement)
[aurora](https://www.alcf.anl.gov/aurora)
[forum](https://www.mpi-forum.org)
[sc](https://supercomputing.org/)
[acm-award](https://awards.acm.org/software-system)
