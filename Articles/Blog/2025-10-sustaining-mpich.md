# Sustaining MPICH: 30+ Years of High-Performance Computing Software

#### Contributed by: [Ken Raffenetti](https://github.com/raffenet)

#### Publication Date: October 28, 2025

<!-- begin deck -->
This article provides a look at the software engineering practices behind MPICH, the widely-used MPI implementation that received the 2024 ACM Software System Award, the first software package from the scientific computing community to do so.
<!-- end deck -->

## Introduction

In high-performance computing, MPI is known as the de facto standard
programming model for parallel applications. In the era before MPI, HPC
vendors each provided their own communication API for scaling
applications on multiple processors. The differences in APIs meant that
developers needed to modify applications to run on different machines and/or
networks. The development of MPI was an effort to standardize the
communication constructs for parallel applications. Users could write
their code once and run anywhere that MPI was supported, without having to
know the details of the underlying system.

MPICH was the first publicly available implementation of MPI and has
been continually developed since its inception. This May, the
Association for Computing Machinery (ACM) announced MPICH as the
recipient of the 2024 [ACM Software System Award](https://awards.acm.org/software-system). The award
"recognizes MPICH for powering 30 years of progress in computational
science and engineering by providing scalable, robust, and portable
communication software for parallel computers." It is an honor to be
recognized alongside other significant award winners such as GCC, Unix,
TCP/IP, and Java. In this article, we look at some of the key
aspects of MPICH's success as a software project and how the MPICH
developers have sustained the project for more than 30 years.

## Origins and evolution

The MPICH project began during the development of the MPI-1 Standard and
closely tracked its evolution before initial publication. MPICH was
instrumental to MPI's success in that it served as a valuable proving
ground, showcasing that the standard was practical to implement and
use. Developing a reference implementation alongside the standard helped
bring to light the complexities of early drafts and contributed concrete
examples of good and bad design choices. Distributing MPICH as open
source made MPI accessible to everyone and, with its permissive license,
provided vendors with a solid foundation on which to base their own MPI
implementations.

From the beginning, the MPICH team designed for extension. A permissive
license allowed vendors to package and sell software derived from MPICH
without the need for licensing or fees. Developing the core code
adhering to the C89 (later C99) standard made MPICH widely portable. The
internal abstractions in MPICH isolated the "generic" parts of
implementing MPI, such as argument validation, object management, and
functionality tests, from the nitty-gritty machine-dependent code. These
design choices meant that the code needed to extend MPICH to support a
new platform was relatively small, yet offered enough flexibility to get
the best performance.

Over time, MPICH has grown from a primarily research-oriented package
to a viable production software library. A rigorous testing
infrastructure, built with the help of vendor partners, now verifies
each change and/or addition to the code. Recently, more MPICH partners
have begun pushing their developments directly to upstream rather than
keeping them in a separate fork or closed source. The resulting ecosystem
empowers users to build and use the latest MPICH not only on laptops and
workstations but also on many of the top HPC systems in the world.

## Sustainability practices

MPICH is a large software project consisting of hundreds of thousands of
lines of code written over 30+ years. The core development team at
Argonne is small (3-5 people), developers change over time, and not all
participate in the project as their sole effort. Code maintainability,
therefore, is of critical importance. What does that mean for MPICH, and
how do we achieve it?

### Revision control

[Revision control](https://bssw.io/items/what-is-revision-control) is essential for developing a large
software project like MPICH. Often, with multiple developers working on
the project simultaneously, revision control helps make sense of the
changes being made to the code. In MPICH, emphasis is placed on good
commit practices. Do the commits in a pull request stand on their own?
Does each commit message explain what change is being made and why?
These are helpful breadcrumbs for developers and users when they are
investigating an issue in the code. Commit messages capture the
context of a change when it was made, more so than inline comments that
can get stale over time. Furthermore, tools like [git bisect](https://git-scm.com/docs/git-bisect)
are better able to track down the exact commit where a bug was introduced when
every commit can be built and tested independently.

Over the years, MPICH has used several revision
control systems. Lost to time are the RCS logs
from the earliest days of the project. Following the trends in open
source software management, MPICH transitioned to CVS, then Subversion,
and finally Git. These transitions were not always straightforward. When
MPICH adopted Subversion, the decision was made not to import prior
history from CVS, likely due to a lack of good tooling for the import
process. Instead, the entire repository was imported as a single "big
bang" commit that functionally erased prior history. This was
detrimental to our ability to trace development history back beyond a
certain point. Thankfully, tooling eventually improved, and the MPICH CVS
history was successfully ported to Git. To avoid rewriting the history
of the main repository, it lives in a [separate repo](https://github.com/pmodels/mpich-CVS) for
historical purposes. Perhaps if/when Git is overtaken in popularity by
another revision control system, the history can once again be combined.

### Issue tracking

Hand in hand with revision control is [issue
tracking](https://bssw.io/items/what-is-issue-tracking). MPICH has relied on issue tracking software
for many years to keep track of all types of easily forgotten tasks. Bug
reports, new feature development, performance regressions, testing
issues, and so on are all entered into the publicly available tracker on our
GitHub page. From there, developers can tag, sort, and filter bugs for
importance, and users can track the resolutions of their individual
issues. Release plans list all the issues required to be closed for
completeness.

Before the ubiquity of web-based issue tracking software, MPICH utilized
[req](https://www.usenix.org/conference/lisa-viii/managing-ever-growing-do-list) for managing issues. Req's limited handling of email
attachments and lack of support for external contributor access led
maintainers to search for alternatives. The MPICH team adopted
[Trac](https://trac.edgewall.org/) along with its move to Subversion for revision
control. Trac offered a convenient web interface for viewing, searching,
and modifying issues. It also offered neat integrations with the
underlying source code management, like the ability to close issues with
special phrases in the commit message that resolved them. These
integrations were maintained even when MPICH transitioned to Git, as
Trac offered native support for both Subversion and Git. However, the
MPICH Trac site was internally managed at Argonne and eventually became
burdensome to maintain. New release, security patches, and environment
updates by the Argonne IT team led to frequent downtimes.

In 2016, GitHub eventually became the sole home for MPICH source code
and issue tracking. GitHub was (and is) widely popular with open source
projects because of its modern features and free hosting
options. Third-party tools allowed us to import issue history from Trac
to GitHub so that important context was carried over from one system to
the other and eliminated the need to maintain both sites for an
extended period. Today, users can find the latest MPICH
development and releases all in one place using the same workflows
common to many open source projects.

### Pull requests

For changes to the MPICH source code, we use a pull request workflow
typical of many of today's projects. Before we can approve a pull
request, it must first pass several of our automated checks. Our
pre-approval scripts check for code style, contributor agreement,
compiler warnings, test regressions, and even spelling mistakes via
continuous integration. This automation helps make many aspects of the
pull request process mechanical and frees up developers to focus on the
most important part of the process -- code review.

The MPICH code review process places a premium on *understanding*
proposed changes. The author must communicate to the reviewer why and
how the changes are being made. It is one thing for code to work, but to
be maintainable, it must be understandable. That means that if someone
other than the original author needs to modify the contributed code one
day, the chances are higher that it can be done in a reasonable amount of
time and without unintentionally breaking things. Some questions we ask
when reviewing code are "Is this code easy to understand? If not, is the
complexity needed to achieve a goal? Can the code be simplified without
losing functionality or performance?" Simple code is preferable because
it is easier to debug and modify, but complexity may sometimes be
necessary, for example, to improve the performance of a critical
function. As developers, we prefer that complexity be isolated (and
documented) as much as possible to avoid polluting otherwise
straightforward code.

Carefully formatting commits and answering these types of questions can
seem burdensome, but such steps are critical to maintainability. Guidelines for
commit best practices are described in our [developer
documentation](https://github.com/pmodels/mpich/blob/main/doc/wiki/developer_guide.md) so contributors are not flying blind. Also in
our documentation are *[coding standards](https://github.com/pmodels/mpich/blob/main/doc/wiki/source_code/Coding_Standards.md)*. This is where we
state in clear terms how MPICH code should be written to help both the
author and the reviewer know what is acceptable.

### Design for extension

Emphasizing maintainability allows MPICH the flexibility needed to be a
vehicle for extension. For example, MPICH partners may wish to extend
and optimize MPICH to work on their preferred platform. Previous
target platforms of such work include IBM BlueGene, SiCortex, InfiniBand,
OmniPath, and many others. The ability to extend and optimize MPICH has been
critical to the continued success of MPICH, and any impediments to this
extension work would risk driving developers (and users)
away.

Typically, MPICH partners are interested only in the machine-dependent
areas of the code, that is, internal APIs for supporting inter- or
intranode memory communication. They are happy to leave the chores of
argument validation and object management to the core MPICH team. Clean
layering of the software in MPICH makes requirements and expectations
clear for developers looking to add new code for their platform. In most
cases, fallback or reference implementations of MPI functionality exist
and can easily be plugged into a machine-dependent module. Developers
need only implement the pieces of software that matter most for their
users.

## Community engagement

Maintaining code is a challenge unto itself, but so is knowing what code
to write in the first place. For MPICH, community participation is
crucial to ensuring that the software we produce is in demand.

### Mailing lists

Even before the advent of revision control systems and issue trackers,
email was widely used by open source developers to conveniently share
updates and interact with users from around the world. MPICH has
maintained several public mailing lists over the years, the core
three being as follows:

- discuss@mpich.org: for user-focused discussions of issues installing and
  using MPICH.
- devel@mpich.org: for developer-focused discussions of
  MPICH code
- announce@mpich.org: broadcast-only list for MPICH release
  announcements

These lists see less traffic than in the past, primarily because most
users and developers now go directly to GitHub. Nevertheless, for those
who either do not have GitHub accounts or prefer to work over email,
the lists remain a useful option.

### MPI Forum

MPICH developers have participated in the MPI standardization process
since the beginning. The [MPI Forum](https://www.mpi-forum.org) continues meeting to this
day to discuss updates and changes to the standard based on new
research. MPICH strives to be the first implementation to support the
newest MPI standard releases as they are published. This strategy benefits our
downstream partners because they can quickly adapt the new code and include
it in a release of their own.

MPICH team participation goes beyond just implementing the new
standards. We develop original proposals, provide feedback on others'
work, and help publicize activities of the forum with the broader MPI
user community. Our deep involvement in the forum continues the work
started during the origins of the project.

### MPICH community

The MPICH distribution model has historically been vendor-driven. The
core MPICH team puts out new releases, and our downstream partners typically
take those and port their additions and optimizations for releases of
their own. Keeping everyone up to date on the core code changes can be
challenging, considering the number of interested parties and their
geographical distribution. A strong community model is necessary to
avoid disruptions in development.

For many years, the MPICH team has hosted a Birds of a Feather (BoF) session
at the [Supercomputing](https://supercomputing.org/) conferences. The BoF is a gathering of MPICH
developers and users to share release plans, new research, and
discuss whatever issues people are facing with MPICH software. However,
this de facto annual developer meeting could not go in-depth on many
issues due to the relatively short 90-minute format. For deeper
discussions, another venue was needed. In 2018, we began hosting a
weekly virtual developer meeting just as MPICH was undergoing a large
internal redesign effort. Many institutions were helping the core
Argonne team with this effort, so the goal of the meeting was to share
updates and discuss any hot-button issues that could block people's
progress.

These weekly meetings continue to this day, well after the initial redesign
was completed. Developers from several companies and research institutions regularly attend. We continue to encourage
external collaborators to attend and provide feedback on our work. These
interactions help us be aware of any external issues and plan
developments to address key issues or features in demand by the
community.

### MPICH in production

Funding for MPICH development primarily comes from the Department of
Energy's Advanced Scientific Computing Research (ASCR) program. MPICH
remains a research project at its core, even though its derivatives are
used on many large-scale production systems.

The [Aurora](https://www.alcf.anl.gov/aurora) supercomputer at the Argonne Leadership Computing
Facility is the second machine in the world to break the exaflop
barrier. Built by Intel in partnership with Hewlett Packard Enterprise,
the massive machine relies on MPICH to scale scientific applications
beyond previous hardware-imposed limits. Aurora represents a deepening
of the partnerships between MPICH, Intel, and ALCF. Aurora has also
pushed MPICH to be a production-ready library in new ways.

With Intel, code changes for Aurora were contributed directly to
upstream MPICH, rather than in the closed-source Intel MPI
library. Regular meetings and hackathons were held with Intel developers
to solve Aurora-related issues and ensure agreement on development
direction. Being part of open-source MPICH means that the system
administrators can quickly generate new MPICH builds for evaluation and
testing on the system, leading to shorter wait times for new features
and bug fixes.

The MPICH team has also been working closely with ALCF application
developers and experts to understand the workloads running on the
machine. This input has been critical for tuning MPICH and guiding
additional development to enable applications to run efficiently and at
scale. At the same time, we have spent considerable effort with the ALCF
team to implement additional testing infrastructure for MPICH on
Aurora. These tests monitor MPICH changes for regression in both
correctness and performance, leading to more stable and consistent
performance of the machine for users.

## Conclusion

There are no secrets to MPICH's success that led to its selection as the
2024 ACM Software System Award winner. As discussed, the principles of
sustainability are many of the same topics that have already been
covered on the Better Scientific Software website. Well-implemented
revision control, issue tracking, and code review are necessary for a
healthy software project with many active contributors. Projects must
also regularly engage with their community to gather feedback and
requirements to guide future directions. A bit of good fortune also
helps, like the rare instance of multivendor cooperation that led to
the MPI standard in the first place. Or the willingness of the Aurora
system designers and builders to embrace open source and contribute
directly to upstream MPICH.

The work of software sustainability is not necessarily difficult, but it
is constant. Continued funding support from the Department of Energy has
kept MPICH in active development all these years, leading to adoption
from vendors and users and laying the groundwork for MPI to become the
de facto standard programming model for scientific software. We are
grateful to everyone who has contributed to the software over the years
and look forward to its continued success in the years to come.

## Author bio

Ken Raffenetti is a research software engineer in the Mathematics and
Computer Science Division at Argonne National Laboratory. He received
his B.S. in computer science from the University of Illinois at
Urbana-Champaign. He joined Argonne in 2006 , where he worked for seven
years as a systems administrator. In 2013, Ken shifted his activities to
software development, joining the Programming Models and Runtime Systems
group, focused on the development of systems software for
high-performance computing applications. His research interests
include parallel programming models, low-level communication libraries,
and distributed runtime systems. In additional to being a maintainer of
MPICH, he is a member of the MPI Forum and PMIx Administrative
Steering Committee.  Ken was a 2024 Better Scientific Software Fellow.

<!---
Publish: Yes
Track: Deep Dive
Topics: software engineering, software sustainability
--->
