# Working Remotely: The Spack Team

**Hero Image:**
 
- <img src='../../images/Blog_0520_WorkRemoteSpack.png' />

#### Contributed by [Todd Gamblin](https://github.com/tgamblin "Todd Gamblin GitHub Profile") and [Elaine Raybourn](https://github.com/elaineraybourn "Elaine Raybourn GitHub Profile")

#### Publication date: May 16, 2020

Elaine Raybourn interviews Todd Gamblin about the Spack project's experience working remotely.

[Spack](https://spack.io) is a package manager for supercomputers, Linux, and macOS that makes installing scientific software easy. With Spack, users can build a package with multiple versions, configurations, platforms, and compilers, and all of these builds can coexist on the same machine.  Created in 2013 by Todd Gamblin, Spack now incorporates the contributions of over 550 contributors from around the world. Spack was the recipient of a 2019 R&D 100 award, also winning a silver medal in the Market Disruptor category.

**Elaine Raybourn:** Todd, now that most of us are working remotely, I'd like to ask you to say a few words about how your team is adapting. What is the composition of the Spack team (remote and co-located)? How do you communicate as a team, and what tools and/or communication strategies have been most helpful?

**Todd Gamblin:** The team is pretty distributed.  Four main core developers work at Lawrence Livermore National Laboratory (LLNL), another core developer lives in Italy, and 3 developers at Kitware work on the project from New York, North Carolina, and New Mexico.  We have regularly scheduled meetings and we plan work directly for these folks.  We were already holding those meetings via WebEx, so really not a lot has changed with home isolation.  

Outside the core, we’ve always had a weekly conference call for Spack, as well as a mailing list. We use the concall to collaborate with other organizations like Fermilab, as well as to answer general questions.  Lately, the mailing list has been pretty low volume, and the conference call is now biweekly and has more narrow attendance than it used to, but I think that is because other fora have gained traction.

Most of the communication now happens on GitHub and Slack.  If I look at a recent week, there were ~125 messages (comments/new issues/new PRs) per day on GitHub.  Our Slack instance has 560 users now, and there are over 180 active users per week.  Of those, over 60 people actually interacted by posting something, so I think Slack is really the best place to interact with Spack now.  You can ask questions in the general channel and get quick responses, and teams at different organizations have been able to use Spack Slack to collaborate on their own sub-projects.

**Elaine:** It sounds like you're using a combination of synchronous and asynchronous strategies and tools. What are your favorite 3 tips for leading scientific software development meetings in which all members are dispersed [working remotely]?

**Todd:**

<!-- formatting for ordered list: no space between items -->
1. My main tip would be: for a lot of stuff, you don’t need meetings.  If we’re planning major technical features, we’ll discuss those on our weekly Webex, but we try to keep the updates low-overhead, and we do most of the interaction on Pull Requests and in Slack.  We can do impromptu conference calls pretty easily through Slack (at least for 1x1) and WebEx.
2. I think having lots of different ways of interacting with the project is important.  Some people do well with email, others like GitHub, and others like Slack.  Some of these work better across time zones, others have quicker response time — there’s no one best medium.  
3. Keep people busy. If you give people too little to do, you’re going to need more communication.  We’re lucky that we had a bunch of clear-cut technical directions that we were already pursuing before home isolation began, and there’s always more work to be done with the number of GitHub issues and PRs we have.  So, so far, people have not run out of things to do.  This has helped make coordination easy.

**Elaine:** Those are great tips for teams of all sizes. The Spack team also supports your largely virtual community with hands-on face-to-face interaction. How will the Spack team be making adjustments to the way you assist your customers (ECP, ORNL, LLNL, Fermilab, in Japan, etc.) in light of recent travel restrictions? Here I am wondering if you'll be conducting more outreach via online training, webinars, video conferences, etc.

**Todd:** We’ve already managed to do our tutorial online — we did our usual 1-day tutorial split over two days for AMD and Cray as part of the CORAL-2 quarterly meeting.  We had to split the tutorial over two days due to time zone differences — there were people across the US and in Bangalore, and the only workable time slot was 8:30-12 PT.  That approach actually worked out well, giving people a break between days.  I think we will end up doing something similar for ISC if they end up holding part of the conference as a virtual event.

We did have to rethink the way we did the tutorial a bit.  It was actually easier to set up the tutorial script and terminal that we usually use; we can get away with smaller fonts on a screen share than we can with a typical room projector.  Q&A and interactivity were different, though.  

We had 50-60 people on the call, and Greg Becker and I managed to make the session work by having one of us speaking at a time.  The other person would get people set up with VM logins and answer questions in the chat.  I think one person could give the tutorial effectively in person, but I don’t think that would work as well online — there would be too much contention over asking questions, and one person wouldn’t be able to keep up with the chat.

Given that we’ve been able to make this work for a large group once, we might just start doing more frequent tutorial sessions in general.  I think we could reach a lot of people that way.

**Elaine:** You've successfully made a number of adjustments that impact your core team. Spack is a huge global community of open source developers and users, and many find themselves in "unplanned" remote work as well--possibly unable to work they way they are used to. What impact do you foresee this having on the way your community is managed, if any?

**Todd:** Given that we’re already remote, I don’t see this having a major impact.  Nearly all the interaction in Spack is asynchronous and remote, so little changes day to day in forums like GitHub and Slack.

**Elaine:** That's a good point about communication and coordination in large communities. What are your lessons learned over the years about supporting large virtual communities that might apply to the smaller teams you work with that suddenly find themselves in unplanned remote work?

**Todd:** A lot of smaller teams at LLNL rely on being able to walk down the hall and ask developers for help, and I think that’s no longer workable.  Probably the most important thing we did early on (with respect to scaling the project) was to write lots of documentation.  I don’t think we’d be able to function without that.  There just isn’t enough bandwidth to tell everyone everything, and there has to be an authoritative place to read about features.

Similarly, I think the biggest bottleneck in Spack is core developer and package maintainer time.  We’ve been able to gradually expand the number of people who own some aspect of the project — giving more people commit access and encouraging more groups to work on their own features and contribute them back.  Having lots of people who feel empowered to work on the project and speak about it helps tremendously, and it means that often, people don’t have to go to the core developers to get help.  They can just ask online and *someone* will answer.  I don’t think we could continue to grow without that.

## Author bios

Todd Gamblin is a Computer Scientist in the Advanced Technology Office in Livermore Computing at Lawrence Livermore National Laboratory. His research focuses on scalable tools for measuring, analyzing, and visualizing parallel performance data. In addition to his research, Todd leads LLNL's DevRAMP (Reproducibility, Analysis, Monitoring, and Performance) team. He is the creator of Spack, a popular HPC package management tool, and he leads the Software Packaging Technologies area in the U.S. Exascale Computing Project. Todd has been at LLNL since 2008. He received the Early Career Research Award from the U.S. Department of Energy in 2014. He received Ph.D. and M.S. degrees in Computer Science from the University of North Carolina at Chapel Hill in 2009 and 2005, and his B.A. in Computer Science and Japanese from Williams College in 2002.

Elaine Raybourn is a social scientist in the Statistics and Human Systems Group (Applied Cognitive Science) at Sandia National Laboratories. Her research focuses on virtual teams, software developer productivity, and transmedia learning.  She has worked remotely for a combined total of 14 years while at Sandia National Laboratories: from the UK as a guest researcher at British Telecom Global Research and Development; Germany (Fraunhofer - FhG FIT) and France (French National Institute for Computer Science - INRIA) as a Fellow of the European Research Consortium in Informatics and Mathematics (ERCIM), and most recently from Orlando, Florida as Sandia's Institutional PI for Interoperable Design of Extreme-scale Application Software (IDEAS-ECP). She also leads the IDEAS Productivity project panel series on [Strategies for Working Remotely](https://ideas-productivity.org/resources/series/strategies-for-working-remotely//). 

<!---
Publish: yes
Track: experience
RSS update: 2020-05-16
Categories: Planning, Collaboration
Topics: Software Engineering, Projects and Organizations, Strategies for More Effective Teams
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
SAND #: SAND2020-5152 O
--->
