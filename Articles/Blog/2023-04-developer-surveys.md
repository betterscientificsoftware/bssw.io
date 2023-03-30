# Developer Surveys to Understand Health and Happiness

 **Hero Image:**

  - <img src='../../images/Blog_2304_DeveloperSurvey.png' />

#### Contributed by [Vanessa Sochat](https://github.com/vsoch)

#### Publication date: xxxxxxxxxxx

<sup>Why would you want to do a developer survey?</sup>

If you've looked around the internet in the last decade, you'll notice that big companies tend to do surveys.
Some notable ones include the [Stack Overflow Developer Survey](https://survey.stackoverflow.co/), the [GitHub Octoverse Survey](https://octoverse.github.com/), or the [JetBrains State of the Developer Ecosystem](https://www.jetbrains.com/lp/devecosystem-2022/).
Why might these companies want to understand the needs of developers?
It likely is not due to curiosity, but rather to cater products and services to developer needs.

At academic institutions and national labs alike, we also have that need, however the motivation typically comes from a different place.
While we don't have the resources of a company to expend on new services for our customers, having a signal that reflects the needs of developers is important.

### Why do we care about developer needs?

Developer needs can be grouped into two categories - those that are practical (e.g., tools and resources) and those that are intangible (e.g., happiness, communication, or motivation).
In our case, we generally want our developers to be happy, feel like they are working on meaningful projects, and with the resources they need and good people.
If you are on, for example, a team that provides general support to code teams, unless you interact with many teams regularly, you can get easily disconnected from the heartbeat of developers at your institution.
You may develop tunnel vision that reflects the immediate needs of your team, or worse, develop solutions for problems that don't exist!
It's OK, we've all been there.
This is why we need to ask
developers about their happiness and needs directly.
When our developers are happy and have what they need to be successful, the work will be more productive and fun, and everyone wins.

### Why did *we* do one this year?

I joined Lawrence Livermore National Lab (LLNL) right after the start of the pandemic.
From the start I knew I wanted to continue my basic work to understand open source software and developer needs that I had started at Stanford University with the first (and possibly last) [software survey](https://stanford-rc.github.io/stanford-software-survey/).
My interest at the time was to survey needs for open source software and development.
As I came upon the one year mark, there was a change in arms so a new lead joined a group I gave a small amount of time to called [RADIUSS](https://software.llnl.gov/radiuss/).
At the time there was an annual applications survey that resulted in a dense, internally distributed PDF of text and plots.
I saw a missed opportunity here, because instead of this, we might have a more fun annual tradition to give out a survey, and then provide results (still internally) in a more interactive web interface, and give the larger public community an update about what's going on in developre land at the lab.
I proposed the idea for an annual Developer Survey, strategically focusing the questions to be on developer needs to help the RADIUSS team guide their work, and got to designing the questions.
And the new lead loved the idea - I was given permission to move forward full force.
We would embark on the first LLNL Developer Survey to have a little bit of fun, and expose the needs of developers at the lab.

### What was involved in designing the survey?

Designing the survey was a bit of a creative task, because I wanted to include questions that were relevant for lab developers, but still touch on expected content like favorite languages and editors.
I spent a few weeks carefully going through public developer surveys that I knew about, along with previous application surveys at the lab.
I decided on a set of categories that would be important for the lab (e.g., about Developer Experience, Developer, Happiness, Innovation, Collaboration, Cloud, to name a few) and then fine tuned questions within each category.
While a lot of surveys don't like open answer questions because it's harder to throw into an Excel sheet and plot, I had an instinct that the best feedback might come from open response.
I decided to take a balanced approach of using (for the most part) structured questions, but along with each section, giving an opportunity for open ended answers.
While Likert scales could show a general sentiment, these open-ended responses would be where the heart of developer feedback came in.
You really can't put people in a check box, nor can you ask them to express a full need or sentiment in one.

Once I had created all of my questions, I put it into a Microsoft Form (what we have to use) and then showed to the RADIUSS team for feedback.
As an aside, if you are able to use Google Forms I highly recommend this over what we had to use, because I found Microsoft Forms much harder to use.
We had a few rounds of feedback, and also sent it out for some testing by a set of volunteers.
As you might expect, many questions were refined, simplified, or entirely removed.
Our perspective at this time was to do our best, and not worry if it wasn't perfect.
We would learn from the experience and try differently the next time.
A few months before the end of 2022, the survey was ready.

### Launch Away... to Results!

We sent out the survey in the last few months of 2022, making sure to give it fun branding, and advertise on many lists.
We sent out a few reminders, and gave people about 2 months to complete it.
While we don't have a definite number as the survey was sent out to these mailing lists, I suspect the primary demographic we hit was Livermore Computing, and in our Town Hall channel I can see a few hundred people.
At the end of the day, we had over 100 responses, half of which were self-reported developers, about a quarter of which were staff scientists (that likely worked with code) and the remainder roles like group leads, managers, technical support, or other support staff.
We had a larger participation than application surveys in previous years, so we were relatively happy.

It was over Christmas break that I started the web interface and parsing logic.
What you can't see from any web interface is that the plots are programmatically generated from the raw data, and the raw data is parsed from an exported comma separated value (csv) file.
Plots are generated via Jeklyll [includes snippets](https://jekyllrb.com/docs/includes/) so the logic for each
plot type only needs to be written once.
This mean that the site has a results [collection](https://jekyllrb.com/docs/includes/) under which we create a small header markdown file to coincide with one question.
It was arduous work to create these (40+) files, being careful to choose the correct plot types, but the good news is that it only needs to be done once - the survey given next year will use the same page and add update data.
The website branding is done in blue and purple to go along with lab branding (blue) and has an added blog or news section to write annual summaries.
When the survey closed in the new year, I was able to generate the full interface internally and share with the RADIUSS team, adding the full comments of all open response fields.
For the final version (to share internally with the lab) the raw data for the open responses was removed, and we only show the high-level summary plots.
As a final piece to the internal submission, I wrote a summary post (and received feedback again from the RADIUSS team) about learned insights.
As a final piece, we took a small sample of highlights and got approval for [a public facing](https://software.llnl.gov/radiuss/2023/02/08/first-developer-survey/) post.
This is where we shared fun learnings like favorite languages, editors, etc.

### What we learned

You can see the [highlights](https://software.llnl.gov/radiuss/2023/02/08/first-developer-survey/) of our survey on the public facing page, and notably these tend to be positive oriented things.
We chose to not share challenges or gripes, which would (maybe ironically) be the most valuable information for us.
The feedback that came in is what you would expect - an overwhelmingly positive flow of gratitude for people and quality of work, and gripes about developer environments and/or tooling.
I say "as you would guess" because this is the classic problem dichotomy at an academic institution or a national lab.
Anywhere where shared high performance computing environments are present, there is a dual need to be conservative and consistent, and that is challenged by the constant reality and drive for change and new things.

One of the biggest challenges in this process isn't necessarily knowing what should be worked on, but figuring out how to do that.
As an example, the RADIUSS team is a small group of people, each only 10-50% of time devoted to RADIUSS, and often in the context of a specific project.
Even when we know there is a huge problem that needs attention, we might not have the people power to do it.
So we decided that we would spread the overall messages of the survey to the teams or leaders that might be empowered to do something.
As an example, one strong piece of insight we got (that is public) is that developers really like VSCode.
It was very easy for me to see this and pair it with [this announcement from GitLab]([a public facing](https://software.llnl.gov/radiuss/2023/02/08/first-developer-survey/)) and approach one of the leads of the team that maintains GitLab and ask if this could be provided.
It was also easy to see that many folks were asking for a piece of software to be updated, but then to go to the team responsible and find out that they had good reasons to not be able to do it yet.

This leads to my greatest worry about the survey - that we might put it out, get great insights, but not be empowered to take action on many of them.
I'm hopeful that if we identify many problems, if we can minimally target two to three of them a year to work on for that year, we can slowly make progress toward better developer experience and happiness.

### Conclusion

You can read our first public set of highlights at [the RADIUSS news](https://software.llnl.gov/radiuss/2023/02/08/first-developer-survey/)
blog.
We hope that other academic institutions and/or national labs take interest in the happiness and productivity of their developers, and consider contributing to this space.
An important point to remember is that while we may not be able to respond to every desire or gripe, the fact that we are asking, period, means that we are trying our best, and our hearts are in the right place.
Even large, meaningful changes can start with small steps, and this kind of effort is exactly that.
Perhaps if we could identify shared gripes, the combined forces of multiple institutions would have enough people power to work on them?

### Author bio

Vanessa Sochat is a Computer Scientist at Lawrence Livermore National Laboratory, and a software engineer for over a decade.
She received her PhD in Biomedical Informatics from Stanford University, and has done extensive work on container technologies, developer tools, and fostering open source communities.
She founded and hosts the Developer Stories podcast.
In her current role, she supports several open source projects, including Flux Framework and the Flux Operator, and is focused on bridging the space between traditional HPC and cloud native technologies.
In her free time, Vanessa likes working on fun programming projects, running fast, and eating avocados.


<small>LLNL-JRNL-846594</small>
