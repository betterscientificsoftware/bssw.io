# A Report on the SC21 Research Software Engineers in HPC (RSE-HPC-2021) Workshop

**Hero Image:**

- <img src='https://github.com/betterscientificsoftware/bssw.io/raw/main/images/Blog_2112_SC21.png' />

#### Contributed by: [Charles Ferenbaugh](https://github.com/cferenba), [Sandra Gesing](https://github.com/sandragesing), [Simon Hettrick](https://github.com/SimonHettrick), and [Daniel S. Katz](https://github.com/danielskatz)
#### Publication date: March 14, 2022

The [RSE-HPC-2021 workshop](https://us-rse.org/rse-hpc-2021/) was held in
November as part of the [SC21](https://sc21.supercomputing.org/) conference.
Following up on the successful SC20 workshop, this year's full-day workshop
included 20 speakers (with slides posted on the [workshop
website](https://us-rse.org/rse-hpc-2021/agenda/)) and over 50 participants,
in a hybrid format of onsite plus virtual content. The workshop's structure
was designed to maximize audience participation, and consisted of six
sessions, summarized below.

## Conversation: Exascale computing and RSEs

Lois Curfman McInnes of Argonne National Lab opened the workshop with a
short talk and extended discussion on the subject "Does exascale computing
change research software?" She described how software has become the
foundation of sustained collaboration in many HPC domains, including
computational science and engineering, data science, machine learning, and
computational infrastructure. Many efforts in recent years have helped to
improve scientific software, and the Exascale Computing Project (ECP) in
particular has driven significant advances. Exascale computing has magnified
the complexity and scope of traditional software challenges: adding support
for heterogeneous architectures and next-generation science, and
coordinating a wide range of software and teams, with all the resulting
technical and sociological challenges. In response, ECP has developed an
open, hierarchical software ecosystem, building a "team of teams" based on
community collaboration and shared policies, while advancing scientific
productivity through better scientific software. She concluded her talk with
a shout-out to her ECP RSE colleagues at Argonne and elsewhere, describing
them as "the linchpin of all things exascale - and beyond"!

## Short talks

Marion Weinzierl gave the first short talk on "Training HPC RSEs: What We
Learned From Our Performance." This was based on training workshops
developed by a team at Durham University and given in 
seven sessions over seven months. These lessons were
tutorial-style in the mornings and hackathon-style in the afternoons. They
were taken by 79 people in 13 teams, with 20-50 participants per session.
Lessons from this work included that 1) HPC research software developers
need a sound foundation in in-depth computer science and hardware-ware
programming to be able to understand performance analysis and turn insights
into performance optimization; 2) performance analysis has to be a team
effort and you (really) need to know the code base; 3) performance analysis
has to be a first-class activity for high-performance code development; and
4) training for HPC-RSEs has to take into account the range of people who
develop HPC software, who have different backgrounds and skills, interests,
and priorities, and that it
needs to spell out the basic concepts that are used and needs to bridge the
gap between hardware and software knowledge. They also have written a
detailed report: <https://doi.org/10.5281/zenodo.5155502>.

The next short talk was on "Building an AI-ready RSE Workforce," by Ying
Zhang. This talk discussed AI's increasing impact on research software, and
what the University of Florida is doing to give RSEs (and others) AI skills,
including an AI curriculum with a certificate in AI, as well as AI training.

The final short talk, "An Exploration of the Mentorship Needs of Research
Software Engineers" was presented by Reed Milewicz. The talk discussed
mentorship as a strategy to enable the career growth and retention of RSEs;
key needs that RSEs may have in providing and receiving mentorship; and
directions for future work. The talk defined mentorship as a relationship in
which a more experienced or more knowledgeable person (a mentor) helps to
guide a less experienced or less knowledgeable person (a mentee), and talked
about the benefits for both the mentee and mentor. Milewicz found that RSEs
need interdisciplinary mentorship networks, long-term mentoring
relationships, and training in soft skills. The talk called for us to start
mentorships now, to build explicit institutional support for them, and to
conduct research to create better mentorship policies.

## Breakout sessions

An hour-long breakout session was organized to draw on the rich variety of
experience that the attendees brought to the workshop. Several questions
had arisen around the training of RSEs during the organization of the workshop,
so we used this as the theme for the breakout. Four groups of
four-to-six people were asked to discuss their views on good examples of RSE
training, HPC training for RSEs, what training needs are unfulfilled and how
these should be discovered, and what other forms of support are needed to
progress an RSE in their career.

There is a critical need for a centralized point through which RSE training
can be accessed. Training resources in skills that are important to RSEs are
available from a number of organizations (e.g., The Carpentries, Code
Refinery, Archer, IET, Intersect), but this training was not developed
specifically for RSEs and even taken together, these resources do not
provide a comprehensive set of materials to develop RSE skills.

The discussion moved to aspects of RSE training that are missing, which
included some technical skills, but also focused on managerial and soft
skills (mirroring the results of the skills question in the international
RSE survey). People management, project management, writing proposals,
dealing with clients, implicit bias, and communication skills were all
highlighted as important skills that lacked training. The need for mentoring
and coaching was also identified, as was the new mentoring scheme that has
been launched by the Society of RSE. Unsurprisingly for this conference, HPC
skills were discussed as important, but it was noted that not all RSEs
conduct HPC.

Training will deal with the short-term needs in skills, but if the RSE
community is to grow to meet the demand for software engineering in the
research community, investment will also have to be made in
education, i.e. undergraduate and Masters courses, to ensure that a
sufficient number of RSEs are being trained.

Understanding training requirements throughout a career requires
first an understanding of the potential career structure. This will require
a pooling of RSE role descriptions (as is happening via the UK and
international RSE associations) and the development of shared key performance indicators (KPIs) which can
be used to measure progress throughout an RSE career. To support this work,
it was noted that there must be further progress on stabilizing RSEs within
the academia, and that this work would be advanced if parallel efforts to
recognize software as a vital research output are successful.

## Panel discussion: What role(s) do RSEs play in the HPC community? What kind of support do they need?

Five panelists from diverse backgrounds - academia, national lab, industry -
and HPC experience discussed the unique challenges and roles RSEs have in
HPC, being themselves RSEs, or supporting building career paths for RSEs.
Efficient parallelization is hard in HPC and, while RSEs aim at following
good or best practices in software engineering, there is a lack of available
literature and practices in HPC yet. Tools supporting software engineering
often do not work well in an exascale environment and the whole programming
paradigm changes. The panelists agreed that the role of HPC RSEs is still
missing good career paths in academia and that their expertise is often not
acknowledged. The panelists have different experiences with support in HPC
centers - some experienced good support with training and incentives, while others
have seen that it got better over the last few years, but was also a
battle for recognition in the past. They agreed that the national and
international movements and events for RSEs also improves the situation for
HPC RSEs and there is the need for more events and more training. To be an
effective RSE is often dependent on each institution and it is still
necessary to follow the traditional academic "benchmarks" with contributing
to publications etc. to get recognized for contributions.

## Conversation: RSEs and HPC in China

The conversation with James Lin, Vice Director of the HPC center of the
Shanghai Jiao Tong University, gave insights into the HPC ecosystem and that
software has been added to the focus besides hardware and applications in
HPC. The support of self-developed domestic software such as molecular
simulations and optimizations of software has started to be especially
supported via HPC centers. Research software is developed in China via
universities, research institutes, companies, and HPC centers. Building out
RSE teams is not very common in China yet though and to the best of his knowledge, 
his university 
currently has the only dedicated RSE team in China. He is one of the
advocates for the role and profession in China and aims at starting with a
local community. The path to build teams would differ between universities,
HPC centers and research institutes because of differences in existing
possibilities, like hiring staff for software development and funding
resources. He encourages his team to closely interact with researchers and
to publish papers collaboratively to keep the option for a career path in
the current academic landscape.

## Panel: RSE Communities Worldwide

Our final session was a panel on building RSE communities worldwide, with
six panelists from four continents. All of their countries have RSEs and RSE
activities in some form, though often without using or even knowing the term
RSE. (One panelist mentioned that she first heard the term RSE when we
invited her to be on the panel!). The panelists noted several common factors
that have helped build their communities. Communication channels such as
mailing lists, Slack, and community calls are very effective ways for RSEs
to start connecting. Raising RSE awareness in other software or research
conferences can also build connections and provide a nucleus for new RSE
communities. Sustainability of newly-forming groups is a key concern:
several countries have grown their communities to where they would be
sustainable beyond the loss of any single person, although perhaps not yet
beyond the loss of a small core group. And several examples were given
showing that RSEs could effectively leverage existing community efforts
among practitioners and students.

## Summary

Overall, the workshop discussions were very active. Many good questions
were asked, and many of the participants afterward expressed their
excitement about the workshop. Our thanks to all who helped
[organize](https://us-rse.org/rse-hpc-2021/committee/) the workshop and all
those who participated in it. And, we'll be starting to plan soon for
another RSE-HPC workshop at [SC22](https://sc22.supercomputing.org/) this
fall; we hope that many of you will be able to join us!

## Author bios

Charles Ferenbaugh is the Computer Science Lead for the Eulerian Applications Project at Los Alamos National Laboratory. He received a Ph.D. in Mathematics from Princeton University in 1992. He spent several years working at Raytheon developing high-performance signal processing software, before coming on staff at LANL in 2001. At LANL he has been a software developer contributing to large multiphysics code projects running on supercomputer clusters. He has also been a part of LANL research efforts in advanced architectures and programming models. He was a founding steering committee member of the US Research Software Engineer Association.

Sandra Gesing is a senior scientist, Scientific Outreach and DEI Lead at the University of Illinois Discovery Partners Institute in Chicago. Her research focuses on science gateways, computational workflows as well as distributed computing which inherently leads to highly interdisciplinary projects. She is especially interested in the sustainability of research software, the usability of computational methods, and the reproducibility of research results. She advocates for improving career paths for research software engineers and facilitators and for incentivizing their work via means beyond the traditional academic rewarding system. She is a founding steering committee member of the US Research Software Engineer Association (US-RSE).

Simon Hettrick is Deputy Director of the Software Sustainability Institute and a Director of the Southampton Research Software Group. Simon's research focuses on the use of software in the research community with the aim of understanding practices and demographics. Simon is a passionate advocate for Research Software Engineers. He orchestrated a campaign to gain recognition for this community, which has grown from a handful of people in 2013 to a substantial international community. He was the founding chair of the UK's Association of Research Software Engineers and was a founding Trustee of the Society of Research Software Engineering.

Daniel S. Katz is Chief Scientist at the National Center for Supercomputing Applications (NCSA) and Research Associate Professor in Computer Science, Electrical and Computer Engineering, and the School of Information Sciences (iSchool) at the University of Illinois Urbana-Champaign. Dan's interest is in the development and use of advanced cyberinfrastructure to solve challenging problems at multiple scales. His technical research interests are in applications, algorithms, fault tolerance, and programming in parallel and distributed computing, including HPC, Grid, Cloud, etc. He is also interested in policy issues, including citation and credit mechanisms and practices associated with software and data, organization and community practices for collaboration, and career paths for computing researchers.

<!---
Publish: yes
Track: community
Pinned: no
Topics: conferences and workshops, Research Software Engineers
--->
