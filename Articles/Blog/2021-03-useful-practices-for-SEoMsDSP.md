# Useful Practices for Software Engineering on Medium-sized Distributed Scientific Projects

**Hero Image:**

<!-- - <img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0321_useful-practices.png' /> -->
<img src='https://github.com/ksbeattie/images/raw/ksb_dkg_blog/Blog_0321_useful-practices.png' /><br/>
<sub><sup>Photo © 2010-2019 The Regents of the University of California, Lawrence Berkeley National Laboratory.</sup></sub>

#### Contributed by [Keith Beattie](https://github.com/ksbeattie "Keith Beattie's GitHub Profile") and [Dan Gunter](https://github.com/dangunter "Dan Gunter's GitHub Profile")

#### Publication date: March 10, 2021

Here's how we've approached producing reliable scientific software in the modern research context
with contributors from multiple labs, universities & disciplines, spread across timezones, etc.

### Introduction & Background

Modern science depends heavily on computing and computer software.  The correctness, efficiency, and
more generally the qualityof the software is instrumental to scientific advancement.  Software
engineering &mdash; *"the application of a systematic, disciplined, quantifiable approach to the
development, operation, and maintenance of software"* [IEEE Standard Glossary of Software
Engineering Terminology, IEEE std 610.12-1990, 1990] &mdash; is the major tool available to create
and maintain software quality.  Advances in software engineering such as "agile" processes and the
"devops" revolution, have been important factors in the creation of scientific software.

In our work, we are often in the position of leading, or helping to lead, the software engineering
efforts of medium-sized, distributed, multi-disciplinary scientific project teams. By
*medium-sized*, we mean from about 10 to 50 people; by *distributed*, we mean that the team is
comprised of people from multiple institutions that are geographically separated and do not have a
common management structure &mdash; typically a few universities and one or more national
laboratories; and by multi-disciplinary, we mean the team is usually composed of people who come
from scientific or engineering backgrounds other than Computer Science or Software Engineering, with
limited experience writing software for use outside their own or team’s projects. We have often tried
to apply software engineering and project management approaches from industry in this milieu, but
always end up frustrated with some of the assumptions about centralized authority, dedicated
software engineering effort, and incentive.

A good example of such a project team is the Institute for the Design of Advanced Energy Systems
([IDAES](https://idaes.org)), which was formed in 2016 to develop new advanced Process Systems
Engineering (PSE) capabilities. Funded by the DOE Office of Fossil Energy, and led by the National
Energy Technology Laboratory (NETL), the project's mission is to improve the efficiency and
reliability of the existing fleet of coal-fired power plants while accelerating the development of a
broad range of advanced fossil energy systems. The IDAES team spans three national laboratories
(NETL, SNL, and LBNL) and three Universities (Carnegie-Mellon University, West Virginia University,
and Notre Dame University). Most of the team is in two locations &mdash; CMU and NETL &mdash; in
Pittsburgh, PA. However, there are half a dozen participants at each of LBNL (Berkeley, CA) and
Sandia (Albuquerque, NM), as well as professors and several graduate students at WVU and Notre Dame.
From a software engineering perspective, the goal is to build a software package that is capable of
simulating important aspects of power plants and power grids. Many of the ideas for why and how to
build the IDAES software came from experience on an earlier project, the Carbon Capture Simulation
Initiative (CCSI), that used commercial tools to perform the process simulations. Though the target
users of this capability are power plant operators and power grid designers, the main user base is
currently the developers and graduate students themselves. Application of the tools to external
customer problems is currently performed at the level of the internal team themselves building the
models and iterating with the customer.

### Approach

While the IDAES project runs functionally as a unit, there are sub-hierarchies of control in each
national laboratory and university that set local priorities within the framework of the project
deliverables. And although most of the effort is being spent on new software to perform chemical
process engineering, there is also significant effort in addingrelated capabilities to an existing
software package, [Pyomo](https://www.pyomo.org/), that pre-dates IDAES and continues to be
developed at Sandia National Laboratories. This size and variation in scope makes project
coordination a challenge, but also is not unusual in our projects.

Although the specific approaches to increasing overall team productivity through software
engineering vary across projects, three elements of what we are doing for IDAES are, we
believe, generally applicable to projects with this kind of mix of institutions, disciplinesand
scale: weekly whole-team developer meetings, incrementally better automation, and
“soapboxing” (including software engineering in official goals & deliverables).

Many styles of meetings have been discussed in recent years with respect to software development
teams, most commonly the daily “standup” meetings combined with some semi-weekly longer
“retrospective” meetings. Neither of these cadences fit what we believe is a unique set of
constraints of our scientific environment, where we have:

* No common authority structure (due to the multi-institutional nature of our collaborations)
* Contributors split across timezones, sometimes continents
* Contributors split across multiple unrelated projects with no inherent interest in
  accommodating each other

As a result, people generally have very limited slots in their calendar that they can guarantee are
open on a regular basis. However, one weekly hour-long meeting is generally possible, and serves
multiple purposes that:

a. Lets people “context-switch” back to what they promised a mere week ago to have done
b. Provides an open forum for cross-cutting issues or questions that don’t get easily addressed in
   subgroup meetings (because, of course these also exist)
c. Provides some opportunity to disseminate practices and educate new team members
d. Builds camaraderie through regular (virtual) contact

For all these purposes, it is important that this meeting is open to the entire
developer team &mdash; however daunting that must seem at first. You can think of this meeting as a
little bit like going to a weekly religious service or tight-knit social group (church, temple, book
group, bicycling club, etc.) where the enthusiasm for the event may vary week to week, but the
overall experience is as much about the customand connectionsas the content.

Specifically what occurs during these meetings will probably depend on your development practices
and tools. But in general, we have found that there should be two main activities: an open agenda of
issues that people can edit before the meeting; and a standard task that focuses attention on the
active development across the project. For many projects, a modified Kanban “project board” approach
provides an excellent focus because it provides an easily summarized list of things done,
in-progress, and abandoned. Whoever is leading the meeting &mdash; and of course there should be
just one person who leads it, since anything else with 20+ people on the line would be chaos &mdash;
can in the absence of any other topics simply walk through all issues, categorize them against
release or other timelines, etc. Almost always, this simple practice will bring up interactions
between the different pieces of ongoing work that would have otherwise been discovered much later,
if at all.

Between meetings, the best friend of overall team productivity are automated practices, and in
particular automated tests. Although very few people disagree with this in principle, the truth is
that getting a large suite of automated tests to work, and keeping them working in the face of
constantly changing software, personnel, dependencies, etc., is non-trivial. Of course, most of the
tests must be written by people who understand the mathematics and science of the code being tested
(or, in the case of infrastructure code, the computer science principles of the code). However, we
must face the reality that this is a significant request of someone’s time, and is competing with
the next publication or result, which they may be encouraged to prioritize. Our position is that the
right approach to take to this problem is incremental: help people put in a few tests, but don’t
require that they pass; then add a requirement that the tests pass before the code is merged, but
don’t worry about code coverage or style; then start informally checking code coverage, and style,
but don’t enforce anything; then start enforcing low levels of code coverage and very basic style
rules; and finally &mdash; well, honestly we’ve never gotten farther than that. But by doing this
all in baby steps, and talking about it weekly in the developer meetings, you are building up a
culture of testing that will lead to eventually having a robust software environment that is broadly
supported by the team.

All told, these meetings serve to address the challenges we face developing software with teams
composed of not primarily computing or software engineering people working together without a common
authority.  The regular meeting baby step approach both educates and builds consensus simultaneously
on the best procedures, practices, and tools to adopt. Ideally this approach is driven by
demonstrated effectiveness from those with the most software development experience.

The final element that we think is useful is what we call “soapboxing”, in the sense of standing up
on a soapbox and shouting out to the world, by putting key elements of software engineering and
development practices where project management and funders can see them. Probably the least important
place for this is grant proposal text, since these are read at most once every few years, and this
is definitely a case where repetition is needed. One of the key places to try to insert some
discussion of software practices (and by extension, developer productivity) is in project meetings.
If your PIs and other project leads need any convincing that this is an important topic, an
excellent way to do so is to show them the team engaging in a spirited discussion in a public or
semi-public forum. Progress reports and general-audience publications about the project are also
opportunities to describe software engineering practices.

### Conclusion

We have spoken largely of social challenges, but of course there are numerous technical challenges
that scientific software presents to developer productivity, which must also be addressed. We
believe that conquering these technical challenges goes hand in hand with reducing the friction of
the software engineering environment so that developers in medium-sized teams don’t spend all their
time working in silos and unintentionally stepping on each other’s toes and, perhaps most
importantly, feel like they are working as a single team no matter how different their technical
backgrounds.

### Author bios

**Dan Gunter** leads the Integrated Data Frameworks (IDF) group in the Data Science and Technology
department of the Computational Research Division. Dan's interests include data management and data
processing pipelines in heterogeneous environments, software engineering for distributed
multidisciplinary scientific teams, and building usable interfaces to enable scientific exploration.
He has led software efforts in projects across multiple domains, collaborating with many science
divisions at LBNL as well as with scientific and engineering teams across the US and
internationally. He also brews a mean cup of coffee.

**Keith Beattie** is a Computer Systems Engineer at LBNL with experience in bringing modern,
open-source software engineering practices to academic and research contexts.  His interests are in
understanding and addressing the unique challenges in leading multi-institutional, geographically
dispersed scientific software development teams while still producing effective and usable software.
Particularly teams composed of members from scientific but not necessarily software engineering
backgrounds.  He has worked in industry as a software engineer and release manager with the last 20
years at LBNL.  He also tortures local music venue attendees playing bass in rock bands.

<!---
Publish: No
Categories: reliability
Topics: testing
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
