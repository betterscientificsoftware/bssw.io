
## Manual Work is a Bug

<!-- deck text start -->
Work to automate routine computing processes using an Agile incremental approach, starting by documenting the manual steps and then incrementally automating pieces of the process using scripts/code.
Continuing to do routine processes over and over again with manual execution is a bug!
<!-- deck text end -->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe "Roscoe A. Bartlett")
#### Publication date: May 27, 2024

Resource information | Details
:--- | :---
Paper Title | Manual Work is a Bug
Authors | Thomas A. Limoncelli
Publication | [ACM Queue, March 14, 2018, Volume 16, Issue 1](https://queue.acm.org/detail.cfm?id=3197520)

Nearly everyone who works with computers a lot has to perform routine tasks many times.
Some people like system administrators (sysadmins) and DevOps engineers have **many** such tasks to perform.
But even other types of developers and users often have repetitive tasks that they need to execute over and over again.
And others in their teams and organizations often need to do similar processes/tasks (or the exact same tasks, with minor variations).
These routine processes may take long enough, and/or be complex enough, and/or have severe enough consequences if they are done in correctly, and/or are likely to be repeated enough in the future to justify automating them to some degree.
Thomas A. Limoncelli's article "Manual Work is a Bug" describes an Agile incremental process for developing increasing levels of automation for routine processes like these.
(Thomas is mainly speaking to sysadmins in this article, but the process and the principles described are the same for any individual or team that needs to perform routine tasks with computers.)

The basic idea is so start by writing documentation right from the beginning while doing the steps manually for the first time for every process that is a potential candidate to become a routine (automatable) process.
Then the future iterations performing the process involve incrementally following, improving the processes documentation, adding more details, and automating larger pieces of the process.
The end state is a largely automated process that saves large amounts of developer time in the future and avoids future mistakes.

> This culture can be summarized in two sentences:
> (1) Every manual action must have a dual purpose of completing a task and improving the system.
> (2) Manual work should not be tolerated unless it generates an artifact or improves an existing one.

This Agile automation process is broken down into four phases for any particular process:

* **Phase 1: Document the steps**: Document of the process as you do the steps manually the first time.

* **Phase 2: Create automation equivalents**: When executing the process again, go back over the process manually following the existing documentation and add exact command-line snippets to the documentation and they these are refined.

* **Phase 3: Create automation**: Develop an expanding set of scripts/code to automate parts of the process as the process is executed again and again.
(Every iteration of the process should expand the scope of the automation scripts/code and reduce the manual effort.)

* **Phase 4: Self-service autonomous systems**:  The final phase is to make the process into a stand-alone tool using the developed scripts/code that is run with a single invocation.
In some cases, such processes justify being set up as an ***autonomous process** (i.e. a process that runs automatically without any explicit action by the user based on some other event.)
(For processes that are performed **very frequently**, setting up an autonomous system is often required to reduce complexity, reduce mistakes, and improve the productivity for developers and users.)

There are several issues and considerations that go along with this Agile automation development process.

**Discipline:**
Engineers must consistently document their work and seek opportunities to automate repetitive tasks.
This disciplined approach reduces errors, improves system reliability, and frees up time for more complex problem-solving.

**The Leftover Principle:**
Focus on automating the boring and time consuming parts; don't (initially) automate the parts require more complex logic and problem solving.
(This is the Compensatory Principle "people and machines should each do what they are good at and not attempt what they don’t do well.")

**Ambiguous requirements:**
It is often difficult or impossible to write down the exact requirements for many of these processes a-priori.
It is only by performing these processes over and over that we can understand what is really needed and should be automated.
(i.e., an iterative Agile approach to requirements gathering and implementation is far superior to a waterfall approach here.)

**Enable early collaboration:**
It is critical to store the documentation and the automation scripts/code in a (Git) version repository or other appropriate system (e.g. a wiki for the documentation) right from the start.
This allows others to collaborate to improve and expand on the documentation and/or automation scripts/code.


<!---
Publish: yes
Topics: ???
Pinned: no
RSS update: 2024-05-27
--->
