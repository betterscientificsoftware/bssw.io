# Surveys to Understand Developer Health and Happiness

 **Hero Image:**

  - <img src='../../images/Blog_2304_DeveloperSurvey.png' />

#### Contributed by [Vanessa Sochat](https://github.com/vsoch)

#### Publication date: May 10, 2023

Vanessa Sochat, a Computer Scientist at Lawrence Livermore National Laboratory (LLNL), has worked as a software engineer for over a decade.
She received her Ph.D. in Biomedical Informatics from Stanford University, and
has been involved in extensive work on container technologies, developer tools, and fostering open-source communities.
Vanessa also founded and hosts the [Developer Stories](https://rseng.github.io/devstories/) podcast.
In her current role at LLNL, she supports several open-source projects, including Flux Framework and the Flux Operator, and she focuses on bridging the space between traditional HPC and cloud-native technologies.

Earlier this month, Vanessa took some time to share with the BSSw.io editorial team her experiences in a recent effort to survey software developer needs at LLNL.
Here, we share some of Vanessa's perspectives on that work in a Q&A style format.

**Q**: Why did you want to do a developer survey?

**Vanessa Sochat**: I joined Lawrence Livermore National Lab (LLNL) right after the start of the pandemic.
From the beginning, I knew I wanted to continue my basic work to understand open-source software and developer needs that I had started at Stanford University with their first (and maybe last) [software survey](https://stanford-rc.github.io/stanford-software-survey/).
My interest at the time was to survey the needs for open-source software and development.
And, if you've looked around the internet in the last decade, you'll notice that a lot of big companies tend to do surveys. Some notable ones include the [Stack Overflow Developer Survey](https://survey.stackoverflow.co/), the [GitHub Octoverse [Survey](https://octoverse.github.com/), and the [JetBrains](https://www.jetbrains.com/lp/devecosystem-2022/) State of the Developer Ecosystem](https://www.jetbrains.com/lp/devecosystem-2022/).

These companies want to understand the needs of developers to cater products and services to developer needs.
At academic institutions and national labs alike, we also have that need; however, the motivation typically comes from a different place. While we don't have the resources of a company to expend on new services for our customers, having a signal that reflects the needs of developers is important.

**Q**: What are some of the main insights you were hoping to learn from a survey?

**Vanessa**: I think developer needs can be grouped into two categories: those that are practical (e.g., tools and resources) and those that are intangible (e.g., happiness, communication, or motivation).

At LLNL, we generally want our developers to be happy, and to feel like they are working on meaningful projects, with the resources they need, and with good people.
For example, if you are on a team that provides general support to code teams, unless you interact with many teams regularly, you can get easily disconnected from the heartbeat of developers at your institution.
You may develop tunnel vision that reflects the immediate needs of your team, or worse, develop solutions for problems that don't exist!
It's OK.
We've all been there.
This is why I think we need to ask developers about their happiness and needs directly.
When our developers are happy and have what they need to be successful, the work will be more productive and fun, and everyone wins.

**Q** Was there any prior developer survey work at LLNL?

**Vanessa**: Prior to my starting at LLNL, there had been an annual applications survey that resulted in a dense, internally distributed PDF of text and plots.
I saw a missed opportunity because instead of this, we might have a more fun annual tradition to give out a survey, and then provide results (still internally) in a more interactive web interface, and give the larger public community an update about what's going on in developer land at LLNL.
I proposed the idea for an annual Developer Survey, strategically focusing the questions on developer needs to help the RADIUSS team guide their work, and started designing the questions.

The new RADIUSS lead loved the idea.
I was given permission to move forward full force.
We would embark on the first LLNL Developer Survey to have a little bit of fun and expose the needs of developers at LLNL.

*Editor's note*: The [RADIUSS](https://software.llnl.gov/radiuss/) team served as a focal point for early work on the survey because the RADIUSS project involves a wide variety of interdependent LLNL software projects.

**Q**: What was involved in designing the survey?

**Vanessa**: Designing the survey was a bit of a creative task because I wanted to include questions that were relevant for LLNL developers but still touch on expected content like favorite languages and editors.
I spent a few weeks carefully going through public developer surveys that I knew about, along with previous application surveys at LLNL.
I decided on a set of categories that would be important for LLNL (e.g., Developer Experience, Developer, Happiness, Innovation, Collaboration, Cloud, to name a few) and then fine-tuned questions within each category.

While many surveyors don't like open-ended (e.g. free text) questions because the data is harder to throw into an Excel sheet and plot, I had an instinct that the best feedback might come from open responses.
I decided to take a balanced approach of using (for the most part) structured questions, but in each section, giving an opportunity for open-ended answers.
While Likert scales could
show a general sentiment, these open-ended responses would be where the heart of developer feedback came in.
You really can't put people in a check box, nor can you ask them to express a full need or sentiment in one.

**Q**: Did you test and revise the survey before launching it?

**Vanessa**: Yes. Once I had created all of my questions, I put them into a Microsoft Form (what we have to use) and then had the RADIUSS team test and give feedback. As an aside, if you are able to use Google Forms, I highly recommend this over what we had to use, because I found Microsoft Forms much harder to use. We had a few rounds of feedback and also sent the survey out for some additional testing by a set of volunteers. As you might expect, many questions were refined, simplified, or entirely removed. Our perspective at this time was to do our best and not worry if it wasn't perfect.
We would learn from the experience and try differently the next time. A few months before the end of 2022, the survey was ready.

**Q**: How did you launch the survey and gather results?

**Vanessa**: We sent out the survey in the last few months of 2022, making sure to give it fun branding, and to advertise it on many lists.
We gave people about 2 months to complete it and sent out a few reminders.
At the end of the day, we had over 100 responses, half of which were self-reported developers.
About a quarter were staff scientists (who likely worked with code), and the remainder were group leaders, managers, technical support, or other support staff.
We had more participation than the application surveys of previous years.
So, we were relatively happy with the response.

**Q**: How did you analyze and present the results?

**Vanessa**: I wanted to host the results on a Jekyll web site.

Over the 2022 winter break, I started the web interface and results data parsing logic, even before the survey had closed.
What you can't see from any web interface is that the plots are programmatically generated from the raw data, and the raw data is parsed from an exported comma separated value (csv) file.
Plots are generated via Jekyll [include snippets](https://jekyllrb.com/docs/includes/), so the logic for each plot type only needs to be written once.
This approach means that the site has a results [collection](https://jekyllrb.com/docs/includes/) under which we create a small header markdown file to coincide with one question.
It was tedious work to create these (40+) files, being careful to choose the correct plot types, but the good news is that this work needs to be done only once; the survey given next year will use the same page and add updated data.

*Editor's note*: We would link to the site from this page, but it is available on LLNL's internal network only. See below for a link to some of the publicly available results.

When the survey closed in the new year, I was able to generate the full interface internally and share with the RADIUSS team for initial review and feedback, adding the full comments of all open response fields.
For the final version (to share internally with LLNL), the raw data for the open responses was removed, and we show only the high-level summary plots.
As a final piece to the internal submission, I wrote a summary post (and again received feedback from the RADIUSS team) about learned insights.
Finally, we took a small sample of highlights and got approval for [a public facing](https://software.llnl.gov/radiuss/2023/02/08/first-developer-survey/) post.
This is where we shared fun things we learned like favorite languages, editors, etc.

**Q**: What were some key takeaways or surprises from the survey?

**Vanessa**: You can see the [highlights](https://software.llnl.gov/radiuss/2023/02/08/first-developer-survey/) of our survey on the public-facing page, and notably, these tend to be positively-oriented things.
We chose not to share challenges or gripes, which would (maybe ironically) be the most valuable information for us.
The feedback that came in is what you would expect---an overwhelmingly positive flow of gratitude for people and quality of work, and gripes about developer environments and/or tooling.
I say "as you would guess" because this is the classic problem dichotomy at an academic institution or a national lab.
Anyplace where shared high-performance computing environments are present, there is a dual need to be conservative and consistent, and that is challenged by the constant reality and drive for change and new things.

One of the biggest challenges in this process isn't necessarily knowing what should be worked on, but figuring out how to do that.
As an example, the RADIUSS team is a small group of people, each only 10-50% of time devoted to RADIUSS, and often in the context of a specific code project under the RADIUSS umbrella.
Even when we know there is a huge problem that needs attention, we might not have the people-power to do it.
So we decided that we would spread the overall message of the survey to these teams so they might be empowered to do something.
As an example, one strong piece of insight we got (that is public) is that developers really like VS Code.
It was very easy for me to see this, pair it with [this announcement from GitLab](https://sdtimes.com/software-development/gitlab-announces-beta-of-its-new-web-ide/), and approach one of the leads of the team that maintains GitLab at LLNL to ask if this could be provided on our installation.
It was also easy to see that many folks were asking for a piece of software to be updated, but then to go to the team responsible and find out that they had good reasons not to be able to do the update yet.

*Q:* Is there anything you would do differently?

**Vanessa**: One of my greatest worries about the survey is that we might put it out, get great insights, but not be empowered to take action on many of them.
I'm hopeful that if we identify many problems, we can target at least two to three of them a year so that we can slowly make progress toward better developer experience and happiness.

**Q**: Any closing thoughts?

**Vanessa**: You can read our first public set of highlights at [the RADIUSS news](https://software.llnl.gov/radiuss/2023/02/08/first-developer-survey/)
blog.
We hope that other academic institutions and/or national labs take interest in the happiness and productivity of their developers, and consider contributing to this space.
An important point to remember is that while we may not be able to respond to every desire or gripe, the fact that we are asking, period, means that we are trying our best, and our hearts are in the right place.
Even large, meaningful changes can start with small steps, and this kind of effort is exactly that.
Perhaps if we could identify shared gripes, the combined forces of multiple institutions would have enough people power to work on them?
This is something I would be excited about.

The BSSw.io editorial team would like to thank Vanessa for her time in sharing her work on the recent LLNL developer survey.
We hope to learn more from surveys in future years.

<small>LLNL-JRNL-846594</small>

<!---
Publish: yes
Pinned: no
Topics: strategies for more effective teams
Track: Bright spots
--->
