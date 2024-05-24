
## Manual Work is a Bug

<!-- deck text start -->
Work to automate routine computing processes using an Agile incremental approach, starting by documenting the manual steps and then incrementally automating pieces of the process using scripts/code.
Continuing to do routine processes repeatedly with manual execution is a bug!
<!-- deck text end -->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe "Roscoe A. Bartlett")
#### Publication date: May 27, 2024

Resource information | Details
:--- | :---
Paper Title | Manual Work is a Bug
Authors | Thomas A. Limoncelli
Publication | [ACM Queue, March 14, 2018, Volume 16, Issue 1](https://queue.acm.org/detail.cfm?id=3197520)

Nearly everyone who works with computers often has to perform routine tasks.
Some people like system administrators (sysadmins) and DevOps engineers have **many** such tasks to perform.
However, even other types of developers and users often have repetitive tasks that they need to execute repeatedly.
And others in their teams and organizations often need to perform similar processes/tasks (or the same tasks, with minor variations).
These routine processes may take long enough, be complex enough, have severe enough consequences if they are done in correctly, and/or be likely to be repeated enough to justify automating them to some degree.
Thomas A. Limoncelli's article "Manual Work is a Bug" describes an Agile incremental process for developing increasing levels of automation for routine processes like these.
(Thomas mainly speaks to sysadmins in this article, but the process and the principles described are the same for any individual or team that needs to perform routine tasks with computers.)

The basic idea is to start by writing documentation right from the beginning while manually performing the steps for the first time for every process that is a potential candidate to become a routine (automatable) process.
Then, future iterations performing the process involve a) incrementally following and improving the process's documentation, b) adding more details and automating larger pieces of the process.
The end state is a largely automated process that will save developers' time and avoid mistakes.

> This culture can be summarized in two sentences:
> (1) Every manual action must have a dual purpose of completing a task and improving the system.
> (2) Manual work should not be tolerated unless it generates an artifact or improves an existing one.

This Agile automation process is broken down into four phases:

* **Phase 1: Document the steps**: Document the process as you do the steps manually the first time.

* **Phase 2: Create automation equivalents**: When executing the process again, go back over the process manually following the existing documentation while refining the process and adding exact command-line snippets to the documentation.

* **Phase 3: Create automation**: Develop an expanding set of scripts/code to automate parts of the process as it is executed repeatedly.
(Every process iteration should expand the automation scripts/code scope and reduce the manual effort.)

* **Phase 4: Self-service autonomous systems**:  The final phase is to turn the process into a stand-alone tool using the developed scripts/code that runs with a single invocation.
In some cases, such processes justify being set up as an ***autonomous process** (i.e., a process that runs automatically without any explicit action by the user.)
(Processes performed **very frequently** as an autonomous system reduces complexity and mistakes, and improves productivity of developers and users.)

There are several issues and considerations that go along with this Agile automation development process.

**Discipline:**
Engineers must consistently document their work and seek opportunities to automate repetitive tasks.
This disciplined approach reduces errors, improves system reliability, and frees up time for more complex problem-solving.

**The Leftover Principle:**
Focus on automating the boring and time-consuming parts; don't (initially) automate the parts that require more complex logic and problem-solving.
(This is the **Compensatory Principle**: "People and machines should each do what they are good at and not attempt what they don’t do well.")

**Ambiguous requirements:**
It is often difficult or impossible to write down the exact requirements for many of these processes a-priori.
Only by performing these processes repeatedly can we understand what is really needed and what should be automated.
(i.e., an iterative Agile approach to requirements gathering and implementation is often far superior to a waterfall approach in these situations.)

**Enable early collaboration:**
It is critical to store the documentation and the automation scripts/code in a (Git) version repository or other appropriate system (e.g., a wiki for the documentation) right from the start.
Such an approach allows others to collaborate to improve and expand on the documentation and the automation scripts/code.


<!---
Publish: yes
Topics: documentation, development tools, continuous integration testing, reproducibility, personal productivity and sustainability
Pinned: no
RSS update: 2024-05-27
--->
