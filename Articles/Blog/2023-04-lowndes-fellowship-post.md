# How open source tooling is changing the way professional researchers learn to code

**Hero Image:**

  - <img src='../../images/Blog_openscapes_grassland_1500px.png' /> 

#### Contributed by [Julia Stewart Lowndes](https://github.com/jules32)

#### Publication date: April 14, 2023

<!-- start deck -->
The same open source tooling that is changing how we do science — R, Python, Git, GitHub — is changing the way we teach professional researchers how to code. 
<!-- end deck -->

Tooling like Jupyter Notebooks, RMarkdown, and now Quarto enable researchers to combine narrative, code, and outputs like figures in the same document, enabling transparency and reproducibility workflows that shared openly on GitHub. This same setup can be used to teach professional researchers to code, so that the teaching narrative unfolds interspersed with code the learner can run. Since the resources are openly available, and learners can work and learn in the same tools used to create those resources, there is consistency between what they see in the materials they learn from, what they see on their end, and the expected outcomes. But what is truly remarkable is the culture shift enabled by this setup — learners have these documents in front of them that reinforces what the teacher screenshares live, and continues to be there for reference and self-paced learning when the teacher isn't there at all. This builds trust and resilience with learners, and role-models a new way of working openly — all of this is a paradigm shift for how professional researchers learn new skills, work, and then teach others in turn. I am a marine scientist who can say from experience that this mode of teaching is game-changing; in fact I am making it my career to amplify this to empower more researchers. For my BSSw Fellowship, I modernized Openscapes' open educational resources that I first built with RMarkdown by refactoring them in Quarto, and have since used these updated resources to teach 6 cohorts (50 teams) of professional environmental and Earth scientists at NASA, NOAA, and the EPA.

### A new learning paradigm of trust and empowerment

It was through Jenny Bryan that I first felt this trust and empowerment as a new coder and learner. Jenny Bryan, then a statistics professor at University of British Columbia and now a software engineer at Posit (formerly RStudio), shared her [Stat 545 Course](https://stat545.com/) materials as open source book (made originally with RMarkdown and now Quarto) that were a delight and light-hearted to read as it walks you through highly technical material for data wrangling, exploration, and analysis with R. Jenny went on to create additional books that are still my go-to resources and recommendations: [Happy Git With R](https://happygitwithr.com/) (which is in my opinion the best place to learn Git/GitHub, regardless of whether you are an R user), and [What They Forgot to Teach You About R](https://rstats.wtf/) (designed for an audience that "has a moderate amount of R and RStudio experience; is largely self-taught; suspects they have drifted into some idiosyncratic habits that may slow them down or make their work products more brittle; is interested in (re)designing their R lifestyle, to be more effective and more self-sufficient").

When she teaches, Jenny provides these resources openly to her students, breaking the paradigm of the teacher being the sole source of information; she is teaching live what I can also reference from a tab in my browser. As a learner, having the book open in my browser helps me because looking between my own console and the teacher's screen means I can miss syntax and now I don't fall behind or have to interrupt the class to say "could you scroll up ?". Futher, since these books are also Jenny's teaching narrative, it also has the effect of having everything she needs in one place. Being open with her script and sharing it with us in advance, we feel trusted and empowered as peers. Sidenote: Jenny live-codes as she teaches, role-modeling that coders make typos and get errors and look things up, and further building confidence in ourselves as learners.

This mode is already shifting the paradigm in a powerful way - because we can fork this idea. When learners see this style of scientific coding and teaching, they repeat it as they work, and share, and they become teachers too. That's what I did, first when I built [open data science educational resources](http://ohi-science.org/data-science-training/) to teach marine scientists, and then dialed it up when I founded [Openscapes](https://openscapes.org).

### Forking this paradigm for different learning modalities 

Openscapes' vision draws from what I experienced with open source tooling from the R and Mozilla communities. We build and share everything openly using open source tooling, and teach researchers in a different modaility than hands-on coding: Openscapes cohorts teach a "Future Us" mindset via discussion-based lessons for teams, in part through our flagship program: [Openscapes Champions](https://openscapes.org/champions).

For my BSSw fellowship, I updated the [Champions Lesson Series](https://openscapes.github.io/series/) book architecture. Originally I built it with RMarkdown\'s [Bookdown](https://bookdown.org/) (left image below). Now it is built with [Quarto](https://quarto.org) (right image). This upgrade streamlines much future work, including that it enables it to have more subchapters in the left navbar, and a right navbar for each page. Also added to this architecture is Community Lessons and How To\'s, which have helped the 50 teams of professional environmental and Earth scientists we've taught since (see [impact blogs](https://www.openscapes.org/tags/impact/)). Modernizing the Lesson Series helped me practice using Quarto, which we've also used with the NASA Openscapes Mentors to develop the [NASA Earthdata Cloud Cookbook](https://nasa-openscapes.github.io/earthdata-cloud-cookbook) with Jupyter Notebooks as the first Quarto external users. Sidenote: through this collaboration, I keynoted the global launch of Quarto atRStudio::conf (Cetinkaya-Rundel & Lowndes, 2022: [slides](https://mine.quarto.pub/hello-quarto), [video](https://www.youtube.com/watch?v=p7Hxu4coDl8), [blog](https://www.openscapes.org/blog/2022/08/10/quarto-keynote/)).

<br>

<img src='../../images/Blog_openscapes_series_bookdown.png' class='page' />

<br>

<img src='../../images/Blog_openscapes_series_quarto.png' class='page' />[Comparison of Openscapes Champions Lesson Series created originally in RMarkdown's Bookdown (left) and updated in Quarto (right). Available at https://openscapes.org/series.]

<br>

And, this culture shift is growing as we're seeing researchers we work with and the broader community fork this mode of working and teaching for their own needs. Gavin Fay created the [FayLab Manual](https://thefaylab.github.io/lab-manual/) onboarding resources for his lab --- a beautifully radical idea in science which itself has now been forked at least 45 times, including by NOAA Fisheries' [OpenSci Resource Book](https://nmfs-opensci.github.io/resourcebook). We're also seeing this for community building at the [California Water Boards](https://cawaterboarddatacenter.github.io/swrcb-openscapes/) and other NASA programs like [VEDA](https://nasa-impact.github.io/veda-docs/).

### Join us!

The best way to join this movement is to reuse and amplify existing community resources, and then fork them to fit your needs and fill the gaps. All of our work is available from [openscapes.org](https://openscapes.org), which is also where you can sign up for our infrequent newsletter with upcoming events. You can also follow us on Twitter and Mastodon \\\@openscapes.

### Author Bio

Julia Stewart Lowndes, PhD is a marine ecologist working at the intersection of actionable environmental science, data science, and open science. Julia\'s main focus is mentoring teams to develop technical and leadership mindsets and skills for data-intensive research, grounded in climate solutions, inclusion, and kindness. She founded Openscapes in 2018 as a Mozilla Fellow and is a Senior Fellow at the National Center for Ecological Analysis and Synthesis (NCEAS), having earned her PhD from Stanford University in 2012 studying drivers and impacts of Humboldt squid in a changing climate.

<!---
Publish: yes
Pinned: no
Topics: online learning
--->

