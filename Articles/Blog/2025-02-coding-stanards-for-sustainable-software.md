# Developing Coding Standards/Practices for Sustainable Software Development

#### Contributed by [Manoj K. Bhardwaj](https://www.linkedin.com/in/manoj-bhardwaj-22448932/)

#### Publication date: February 14, 2025

<!--deck start-->
Learn the top-9 standards and practices that a modern science and engineering company should adopt to go fast with quality in a sustainable manor (by keeping down technical debt to a manageable level) and ideas on how to get there.
<!--deck end-->


### Abstract

Despite the critical importance of sustainable software development, there remains a significant lack of awareness among software developers and managers on the importance of practices/standards on the quality of the software product.
This article explores the role of coding standards, practices, and guidelines in mitigating technical debt and enhancing software sustainability.
We have seen significant reduction in debt with the adoption of these standards which leads to substantial cost savings and increased efficiency in software development.
Our aim is for this article to serve as a catalyst for organizations to recognize the considerable gaps in current software development project management and development practices and to provide a roadmap for assessing and improving the sustainability of their software projects.
Imagine if debt can be reduced from 50% to 10%.
At one organization, we estimate that this could lead to $100M in annual savings.
This article is based on a presentation delivered at the 2024 Sustainable Scientific Software Conference (S3C), which was part of the National Labs Information Technology (NLIT) Summit held in Seattle, Washington (https://www.fbcinc.com/e/NLIT/).


### Introduction

In the realm of software engineering, the development of sustainable software is often overlooked or misunderstood.
Many development teams face technical debt that exceeds 50% of their budget, and worse, they are not aware of their own technical debt measures.
In addition, many software developers are not taught practices that help create more sustainable software.
Managers of software development projects are not sure how to measure their success.
Hopefully, this article can help by highlighting the importance of developing and adhering to coding standards, practices, and guidelines to create sustainable software.
The definition of sustainable software is presented in this article at a later section.
We hope to demonstrate various ideas through a fictional story of your onboarding experience at Fake Science and Engineering Company (FSEC), where you have been hired to work on a scientific software project.


### Fake Science and Engineering Company (FSEC)

Welcome to FSEC.
You have been hired as a software engineer for our latest scientific software project.
Today, we will set the standards and expectations for you as a team member of our project.
The concept of "standards" in this context extends beyond mere coding conventions.
It encompasses a holistic approach to software development, including practices like Test-Driven Development (TDD), Scrum, pair programming, and more.

We believe in our standards and practices because they lead to significant cost savings in two ways:

1. Technical debt is significantly reduced.
2. Adding features becomes faster or maintains a consistent cost over time.

The next point is very important, and we will start with a quote from Martin Fowler: "Any fool can write code that a computer can understand.
Good programmers write code that humans can understand."

As you work on the project, it is more important to make the software readable (which leads to sustainability) than it is to get the software merely working.
Your number one job as a software developer is to make the code you write readable!


### FSEC Software Development Standards and Practices

We will touch upon some of the more important standards and practices.
A summary of these is listed below:

1. Test-Driven Development (TDD)
2. Scrum
3. Pair Programming
4. Six-Line Functions
5. Minimize Function Parameters
6. No Comments in the Code
7. Improving Legacy Code
8. Development, Security, and Operations (DevSecOps)
9. Measuring Effectiveness

Next, we will delve into more details on each one.

#### Test-Driven Development (TDD)

All new software will be written using the Test-Driven Development (TDD) process.
You will be taught this process and expected to follow it.
You will learn about the Red, Green, Refactor cycle and refactoring practices to apply.
While upfront whiteboarding of design is important to set the initial direction, the TDD process will allow the design to emerge, which might not align with your initial expectations.

Additionally, you will learn about the "Four Rules of Simple Design" from Kent Beck, which will help you execute your refactoring cycle.
The rules, in priority order, are:

1. Passes the tests
2. Reveals intention
3. No duplication
4. Fewest elements

You will also be trained on the S.O.L.I.D.
principles (https://bssw.io/items/solid-design-principles)

* Single Responsibility Principle
* Open/Closed Principle
* Liskov Substitution Principle
* Interface Segregation Principle
* Dependency Inversion Principle

These principles will be useful in the refactoring step of the TDD cycle.
Applying TDD to our project will result in fast-running verification-type unit tests, providing nearly 100% code coverage.
Our Development, Security, and Operations (DevSecOps) pipelines will be able to deploy software quickly and with high confidence.

#### Scrum

You will be part of a Scrum team.
Following Scrum itself is not the sole goal or indicator of developing sustainable software; it is an integral part of delivering valued software to our customers.
However, without the remaining standards and practices, we risk delivering software with a lot of technical debt.

When estimating stories using points, we will allocate time for daily refactoring by including that effort as part of the estimate.
This refactoring can occur within the TDD cycle or when we touch legacy code, i.e., code without automated verification-like unit tests.
As one measure of success, we will measure our technical debt.
Consider the simplistic view of our capacity as follows: T=T1+T2+T3 where:

* T is the total capacity,
* T1 is the time spent on new development,
* T2 is the time spent refactoring,
* T3 is the time spent maintaining/fixing code.

With teams experiencing high debt (T3), the time available for new development (T1) is minimal.
At FSEC, we do TDD, which impacts T1, and we continuously refactor (T2) to keep T3 low and stay sustainable.
Teams that do not use TDD think it helps minimize T1.
They do not spend time refactoring (T2), hoping it gives them more new development time (T1).
However, experience shows this is a false hope.
Early at FSEC, we realized that many teams did not know how efficient their software development processes were.
Hence, managers and team members did not even know this was a problem.
Customers often did not receive the capabilities they requested (in a timely manner), found the development expenses unrealistic, or did not establish trust with the software due to usability issues.

You will be on ONE Scrum team, and you will be 100% dedicated to that team.
We do not encourage multitasking at FSEC since research and experience show that it immediately reduces an individual's capacity by 40%.

Here, you can see the measure of sustainable software development.
If T1 can be kept constantly high or increasing, we are doing well.
On many teams, T3/T is 50% or more, and as the code base grows, the technical debt increases with each new feature, and the time spent actually developing new features (T1) grows ever smaller.


#### Pair Programming

Kent Beck, author of Extreme Programming, states that the Pair Programming practice improves code quality and maintainability.
We have experienced this firsthand, so our practice is: "if it needs to be maintained, it shall be pair-programmed."
No, it is not paying two people to do the work of one.

To facilitate this practice, we all use the same software development IDE configured uniformly for everyone at FSEC.
This consistency aids our pair-programming practice.
We encourage different patterns for pair programming, but we start with the Navigator/Driver pattern.

In the Navigator/Driver pair-programming pattern, the individual who knows what code needs to be written does not touch the keyboard (or mouse) and acts as the Navigator.
The Driver follows the instructions of the Navigator.
Think of it as driving in a new city with a passenger navigating using a map on their mobile phone.


#### Six-Line Functions

Every function we write will be no longer than six lines.
Exceptions exist, mostly in cases where a large conditional or switch statement is necessary, where six lines cannot be accommodated.
However, for most of our code, you will be expected to keep the line count to a maximum of six.
Note that curly braces do not count.


#### Minimize Number of Function Parameters

At FSEC, code readability is critical.
This is also explained well in the book "Clean Code" by Robert Martin, which is part of your training.
All functions/methods will have at most three parameters, though the goal is to minimize them to zero.
Zero parameters are considered great, one is good, two are okay, and three are acceptable.


#### No Comments in the Code

This is also explained well in "Clean Code."
At FSEC, we require readable code without the need for comments.
Comments become part of the code maintenance, and it is hard enough to maintain the code itself.
Of course, there are exceptions, but they require written approval from the CEO of FSEC.


#### Improving Legacy Code

At FSEC, we have acquired legacy code from a national laboratory, which is now a critical software component of our project.
This is legacy code because it has sections not covered by automated verification-like unit tests.
You will be trained on various approaches to dealing with legacy code based on the book "Working Effectively with Legacy Code" by Michael Feathers.

At FSEC, we choose to refactor as our primary option rather than rewriting legacy code.
Hence, you will be expected to improve legacy code when you touch it.
Using the refactoring training you have received, you will be expected to add unit tests to cover the legacy code before you start modifying the code.
Additionally, if a bug is discovered, you will be expected to create a unit test that mimics the bug before the bug is fixed.


#### Development, Security, and Operations (DevSecOps)

At FSEC, we invest in having fast DevSecOps pipelines.
We want our working software to be deployed quickly to our users for rapid feedback without causing outages or software failures or being a source of a ransomware attack.
You will be trained on your role as the "Developer" in DevSecOps.
You will partner with DevSecOps engineers because our code needs rapid feedback cycles.
New code written using TDD will have a rapid cycle time, while legacy code will need to move more toward unit tests and fewer system tests to achieve the same outcome.
One of your primary responsibilities as a developer is to NOT create a system test that will significantly affect our continuous integration (CI) times.
Our hardware resources are NOT unlimited.


#### Measuring Our Effectiveness

Recall our capacity equation: T=T1+T2+T3.

From this, we measure debt as T1/T.
This measure will show trends of how sustainable our software is.
Our goal is to minimize T3 and maximize T1.
T2 can be an indicator of how much legacy code we have, and hopefully is not increasing over time.

We will also measure our Continuous Integration (CI) times, aiming to keep them under one minute.
Additionally, we will measure our line coverage, which will remain above 99%.
We are always experimenting to improve or find new measures.
We do not avoid this area because it is hard; we do it to ensure we are not flying blind and have a clear sense of how efficiently we are executing our software development projects.


### Scientific Software Thoughts

At FSEC, our software is primarily scientific.
We hire aerospace, electrical, civil, and other engineering disciplines, as well as mathematicians, data scientists, and user experience (UX) specialists.
We need the expertise you bring.
However, as part of a Scrum team, we encourage our developers to separate the idea of finding a solution to a problem from implementing that solution in code.
We do not expect everyone to be fungible in domain expertise, but we do expect fungibility in implementing code.
We prioritize team implementations over individual efforts.
We are keenly aware of developers who drive recklessly to get somewhere fast versus those who drive well and get us there sustainably.
Most developers recognize that our standards and practices are designed to get us there both fast and well.

### Path Forward Ideas to Consider

At this point in the article, we conclude our fictional FSEC onboarding story.
How can we move forward in improving our abilities to write sustainable software?
Here are some considerations:

1. Develop Standards for Software Development Teams
2. Start Measuring Technical Debt (T1/T)
3. Organizations Should Define Minimum Quality Criteria (Definition of Done)
4. Develop Awareness That This Is the Fast Way to Develop Software
5. Collaborate with Teams Interested in Adopting These Ideas
6. Study These Ideas and Present Results at Future S3Cs
7. Develop Tools for Developers That Help Enforce Good Habits
8. Research Ideas
    * Use AI/ML to turn system tests into smaller tests and invert the testing pyramid.
    * Use ChatGPT to pair-program.
    * Use AI/ML in CI pipelines to identify "unclean" code and "fail" it.


#### Idea #1: Develop Standards for Software Development Teams

What if we used the Sustainable Scientific Software Conference (S3C) as a collaborative platform to discuss and develop standards that most organizations could use as a starting point for their own standards and practices?
If so, please consider attending and supporting this initiative.
We aim to develop the initial set of standards at the 2025 NLIT Summit in Denver, Colorado.

Having said that, you could focus only on your organization and try idea #3.


#### Idea #2: Start Measuring Technical Debt (T1/T)

This is a great starting point to assess how your team is performing.
If you are on a Scrum team, this could be done by comparing total Sprint capacity (in points) to the number of points in the Sprint allocated for developing new capabilities.
This measure is not meant to be perfect, but it will give you an idea of where you stand.
Do not be surprised if it is around 50%.
If your organization uses external support staff to handle user support issues, you can include their capacity as part of the total time T.


#### Idea #3: Organizations Should Define Minimum Quality Criteria (Definition of Done)

Why do so many organizations avoid addressing this?
If your organization has multiple software development projects, should not we strive for consistency in the quality of code being developed and delivered?
This requires courageous leadership.
After all, who wants to be the one to tell their software development teams that this list is the minimum quality criteria?
Consider making a team event to create the initial list.
Bring change agents from different teams together, create an initial starting point, and then establish a structure that allows these criteria to be updated regularly.

Consider using the S3C as a venue for thinking about and discussing these ideas further.


### Conclusion

We believe that many organizations can improve their software development teams by focusing on improving knowledge and practices for creating sustainable software.
While there is not excellent scientific research on this topic, we should not be flying blind.
We should take a proactive approach to developing software sustainably.
At one facility, we estimate that if teams can move their practices toward sustainable standards/practices, there could be a savings of $100M annually.
Yes, that is correct.
That is how much technical debt can impact an organization, and worse, some might not even know they are swimming in it.


### Acknowledgments

We want to thank Scott Warnock, Stuart Baxley, Chris Sullivan, Gary Lawson, Akhil Potla, Richard Drake, Henry Gabaldon, Erik Strack, Terri Galpin, Tricia Gharagazloo, Dena Vigil, Richard Michael Jack Kramer, Salomé Thorson, Raisa Koshkin, and the Sierra Toolkit (STK) Team: Alan Williams, Jesse Thomas, Todd Coffey, Nate Roehrig, C. Riley Wilson, Tolu Okusanya, David Glaze, Johnathan Vo for their invaluable contributions. We would also like to acknowledge Roscoe Bartlett for his edits and valuable suggestions to this article.


### Author bios

Manoj K. Bhardwaj, Ph.D., is a technical staff member at Sandia National Laboratories with a lengthy background in numerical software development and simulation.
Manoj is passionate about Scrum, Extreme Programming (XP), and Development and Operations (DevOps).
He is also passionate about continuous improvement and the infinite game.
He has been fortunate enough to see the impact of the previously mentioned work.
Manoj has taught software development practices and principles at the University of New Mexico.
He believes that we can reduce maintenance and support costs to minimal amounts so every $ can be spent on adding value.


<!---
Publish: yes
Track: deep dive
Topics: software process improvement, software engineering, requirements, software sustainability, design, documentation, testing, continuous integration testing, peer code review, strategies for more effective teams
--->

<!--- NOTE: Above, the track could also be "how to"? --->

<!---
LocalWords:  Sandia
--->
