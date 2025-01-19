# How Investing in Documentation Makes Even a Single-Developer Project Better

#### Contributed by [Joe Frye](https://github.com/fryeguy52)

#### Publication date: January 28, 2025

<!-- begin deck -->
We usually think about documentation as being for others -- other developers, users, etc.  But documentation can be useful even if you're the sole person working on the project.
<!-- end deck -->

### Background: About the project

Scientific software requires complex sets of dependencies on a wide variety of platforms.  It is a challenge to create a standard environment for development, testing, and deployment.  These three phases of software creation often occur on separate machines and at different times.  Ideally, testing and deployment are automated processes which occur on dedicated systems.  Development usually takes place on a user's machine and that machine may need to have multiple software environments available.  Containers can help with these challenges and can be used to provide a standard environment on all of these different machines, matching what a developer needs, so they have potential to facilitate the use of standardized software environments for reproducibility and for portability.   We are trying to provide turn-key environment containers that look and feel like the systems project teams are used to using.  It is important for the container environment to closely match the environment on the current development, build, and test systems. The process for building typically looks something like this:

1. Log into the target system (usually for specific OS)
2. Load the environment (source a script, load modules, set environment variables, etc.)
3. Configure (run a script, call cmake, etc.)
4. Build (make, ninja)
5. Test

With the containerized environments we want to change this workflow as little as possible while still getting the reliability, reproducibility, mobility, and performance that projects need.  The idea is to provide containers that fit easily into existing workflows and require minimal changes to a project’s infrastructure or processes.  For a project to use our containers the workflow looks like:

1. Log into any system that runs the podman container system
2. Launch the environment container
3. Configure (run a script, call cmake, etc.)
4. Build (make, ninja)
5. Test

In this way a project does not need to change their configure and build scripts to use the containers. The only significant change is in setting up the environment.  Our containers are made to match our bare metal installations.  Users access the bare metal installations through environment modules. To make the above workflows equivalent, we had to exactly match how the modules set the environment inside the container to how it is set on the existing bare metal installations.   It required some research to figure out how to create containers that have the required software environment for our codes that are easy to use and easy to port to many platforms.  The initial effort was exploratory, informal, and mainly conducted by one developer. The bare metal installations are already installed with Spack so the obvious path to follow was to use Spack inside of containers.  We were able to use the same Spack configuration files in the containers as we use on the host machines.  To test our progress in recreating the existing environment we needed to build a code in a container using the same scripts that were used on bare metal.  While it made sense for the developers to be the first to exercise these container capabilities, it was clear that we needed ?????.  In the end we were able to build our entire software environments inside containers and to make those available via internal container registries.  In addition, we developed infrastructure that allows projects to build containers tailored to exactly their needs which can reduce the size of the containers.  More details of our container environment project were presented at NLIT (National Laboratories Information Technology) in 2024 and the slides can be found here: 2024_04_NLIT_SEMS_Containers.

### The role of documentation

In addition to containerizing scientific software development environments, we were also interested in improving our own development processes, including integrating the generation of project documentation into the daily workflow. The overall effort for the containerized environment project was small and relatively short lived with one developer working 20% time for a few months. This made it difficult to devote a large amount of time to documentation.  While it was important to capture the state of the investigation, we could not afford to slow the development process.  To help us improve the documentation we were inspired by some of the core ideas of the [Productivity and Sustainability Improvement Planning](https://bssw.io/blog_posts/productivity-and-sustainability-improvement-planning-psip) (PSIP) process, although we did not rigorously follow the PSIP process.  We created a progress tracking card (PTC) as a means of setting intermediate and final goals and revisited it a couple times to keep on track.  The process essentially provided a lightweight but structured way to have conversations about improvements we wanted to make in the project, and it helped us break an abstract goal into concrete, achievable steps.  The PSIP process also helped simply by making it a point of conversation during project meetings.

One challenge of integrating documentation into the developer workflow is to determine what level of documentation is appropriate.  The goal of having "good documentation" is both uncontroversial and too vague to be useful. We had to think about what kinds of documentation were needed, the audience for each type of documentation, and how large each audience is, among other factors. When considering this, it becomes clear that there are a lot of things that one can document about a software project.  You can imagine different documents with names like: “How to use this software”, “How the software actually works”, “Why we need this software”, “Why the developers made all the decisions that they made”.  All of these would have different audiences and would document very different things about the project.  In the case of a mature, widely used project it seems that you would want all those kinds of documentation.  For a small effort such as ours we needed to document the project, but it was not clear what was going to end up being ultimately fruitful or important.  Another challenge is that the developer on the project tends to get lost in the exploration and solving of problems and to leave documentation to an unspecified “later date,” with the results that details would often be lost and there was not a clear record of how the project came to be in its current state, why decisions were made, and what else was tried and did not pan out.   It seemed reasonable, given this situation, that we try to implement a lab notebook-style of documentation in a very lightweight way just to make improvements.  So we agreed to have a wiki open in one window and the terminal in the other during our work on the project.   As problems were encountered, we could copy and paste code snippets, notes, and commands run on the command line in the terminal, into the wiki to create a record of the process of investigating how to best create and use containers for our code teams.  Every month a new wiki page was created to give some idea of chronology to the documents.

This is a very lightweight and very rough form of documentation that I suspected at first would not be very useful.  However, I almost immediately realized it was useful in several ways.

- By creating such documents, I no longer had to keep all the information and experience in my active memory.  It became a useful reference document nearly as soon as I created it.  I was able to refer to it and refresh details that I otherwise would have missed.  The time cost of creating these lightweight notes was quickly recovered by the time it saved as a reference document for myself.

- These documents added depth and context to discussions about the project the project with other people. I was able to show colleagues exactly what had been tried, what had failed, and what succeeded.  This led to richer and more productive conversations about the project and how we should proceed.

- The documentation allowed for much better collaboration.  For example, we were able to point a summer intern at these documents and he was able to get up to speed quickly enough to use our containers and infrastructure as part of his summer project.  These documents were not only useful for me, but also for other contributors.

- Even in situations where more complete, clean, and detailed documentation is eventually needed, the rough notes provide a great starting point to work from, and decrease the risk of omitting details, as compared to going back and creating documentation from scratch after the fact.

Going into this project I knew that my usual process for documenting my work could be improved.  I always thought that useful documentation would take a significant amount of effort away from the "real work" of the project. I was surprised how quickly the documentation became valuable to me and others, and just how valuable it turned out to be.  In documentation I usually let the perfect be the enemy of the good -- or the enemy of any documentation at all.  I tend to think that creating documentation requires a lot of time and effort and quickly gets out of date without a sustained effort. Without the time to create "perfect" documentation, I tend to delay the creation of documentation until the project reaches that ill-defined state of being "ready".  I used to assume that there is some minimal level of documentation that is useful, but my experience with this project has demonstrated that the bar is much lower than I had thought. The addition of very rough, quick, and unedited lab notebook-style documentation to the workflow created a great benefit to the project overall. Writing down even a little helps a lot, even if more detail is required later.

But old habits die hard and new skills are sometimes hard to integrate.  In this case the good news is that some of these lessons have stuck around.   Realizing just how low the barrier for usefulness is when it comes to documentation, combined with seeing how helpful it can be for someone following along, I find myself documenting more frequently in other projects too.  I don't keep the "notebook wiki" open all the time, but I do have a sharper eye for when documentation will be useful for someone else and an understanding that it does not have to be formal and rigorous to be helpful.   I am also much more likely to log my process step-by-step on when I'm working on tickets submitted against a code because I know other people may encounter a similar problem later, and my notes may help them solve their problems too.

### Author bio

<!---
Publish: Yes
Track: deep dive
Topics: documentation
--->