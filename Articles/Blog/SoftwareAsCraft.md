# Software Is As Much or More Craft Than Science

**Hero Image:**

 - <img src='https://github.com/betterscientificsoftware/images/raw/master/use-case-meander.png' />

#### Contributed by [Paul Wolfenbarger](https://github.com/prwolfe "Paul Wolfenbarger's GitHub Profile")

#### Publication date: February 25th, 2019

A focus on craftsmanship in software can matter as much as algorithm design or optimization and show as great a reward.

As part of an effort to improve our software testing my group at work recently started watching Bob Martin’s “Clean Code” videos. What struck me most forcibly about them was not the content itself as I have read and used or rejected almost all of these methods in my career. The real surprise is that somehow I had ceased to utilize them in a full and robust manner. I can think of several reasons why this occurred, understaffing short deadlines and significant technical debt for starters. These are exactly the techniques that are best suited to help resolve those issues in the long term, so how did they get bypassed? The team has been very receptive to adopting good testing, and review practices (and is working on others.) I decided it is important to share reminders about how we should approach software work in general terms that can apply to all our code teams. We have groups in research, operations, and applications working in C, C++, python, bash, fortran, and matlab, so this will be vague. (Java and Ruby do happen, just not in our group as they don’t typically have the numerical libraries and historical support needed.)

### Keep it simple

Simple beats cool, fast, slick, and innovative, basically anything except simpler. Yes, I work in High Performance Computing (HPC) where every clock cycle can and usually does matter, but yes, simpler IS better than faster.

*“We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%.” - Donald Knuth.*

Of course, when it counts, we want the important code to be in that 3% and to run fast. The other 97% will be read more by humans, used to connect to other software, determine how reusable your software really is, and will carry more information and receive less attention. (This also unfortunately means it will contain more bugs). My wife's jokes about extra protein aside, those bugs matter - they will cost you much more to fix later than to resolve now. This less critical code needs to be as robust as possible upfront precisely because it will get less attention everyday. The good news is that once it is functioning well the odds that it will gather new problems is in direct proportion to how often developers modify that code, and that should be small. Take the time when you write any code to make it small, make it legible, to test it well, and to make the code compile cleanly. You will thank yourself later.

### Know your history

I won't reiterate the techniques, just advise that you read your programming history and study the best. Meyers, Stroustrup, Knuth, the Gang of Four, Kernighan, Ritchie, these are all important sources. (My apologies if I missed your favorite). But why should we look back?

*“I never look back darling - it distracts from the now” - Edna 'E' Mode in the Incredibles.*

*“No Capes!” - Edna 'E' Mode in the Incredibles.*

Yes - I know this is campy, but it illustrates the issue well. Everyone who works in a field learns something that can help everyone else. Do I need to understand the methods a roman engineer would have used to design an ancient aqueduct to create a modern dam overflow? Well not in detailed practice, but in some level of theory, understanding the same incompressible fluid dynamics is needed. I might stop with just what are the equations and how do I apply them, I might want to understand how they were discovered, or if I have an interest I can go all the way back to figure out how men without those equations designed structures that still bring water reliably over large distances. Similarly the design of the archways was robust despite lacking the math we would use today. Whatever level of interest you have you will learn something helpful to your current effort and improve your work.

### Consider interfaces carefully

So what exactly am I referring to? Interfaces are in fact so ubiquitous in software we often don’t even realize we have written them or violated the boundaries they are meant to represent. Each source file, each header, every library, data structure, function, and class, each decision about what headers will be installed and which will not represent a boundary that we set up for one reason or another. What those interfaces are and how they are (and can be) used will determine how your code can be understood by others and how they will use it. Allowing them to happen by chance is simply not acceptable.

*Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler, 2008*

While Fowler was not actually referring only to interface design it applies well. In my own case, we are dealing with several large legacy codes that use multiple research libraries and several commercial libraries. The dependency graph is the proverbial “[Big Ball of Mud](http://www.laputan.org/mud)”. That means our compile times are slow, extraordinary methods are in place to constrain configure times, and linking is not parallelized as the applications are simply to large. The compiler understands all of this at a cost of time and cpu cycles, but most of the developers are lost without reading prior examples. We do see that not all of our dependencies contribute to this issue. In fact two require only run-time linking to change versions in most cases. The difference is entirely in the volatility of the API and ABI, those products have been well designed to constrain the interfaces, while most of our in-house work and partners are more free-form or completely unstructured.

Interfacing to the compiler or interpreter is the easy part, the humans are harder. When you convolve both of those with build systems as complex as Ant or Makedepend (or worse,) it can seem hopeless. It's not. Look at and simplify every interface, from PiPiml headers to select library interfaces and readable functions and classes. Create proper python directory packages with small sets of interfaces. In short, make sure you can sort it out easily years down the line when you can't even remember writing this thing. The machine will have far less problems anyway.

### Remember craftsmanship

Craftsmanship in a project can be more important than the engineering, architecture or science involved. We use those terms to describe what we do, but they are ill-fitting. Perhaps you prefer artisanship or professionalism over craftsmanship, but attention to detail and care about what you are doing will make more of a difference than all the theory in the world.

My educational background is in structural engineering, and I have done many masonry buildings here in the Southwest. I got very good at the math, spent a lot of time reading about the theory and materials involved, wrote computer programs, and generally worked hard to do the best designs I could. I was finishing my internship when the Project Engineers started to send me out on my own to do the construction observation. I realized very quickly that the difference between having a good versus an excellent mason was equally as important as having a good engineer. Having a good mason often made a mediocre design feasible whereas a poor mason could make a good design have a very short lifespan.

In the same way that masonry craftsmanship makes a huge difference in a construction project, software ‘craftsmanship’ makes a critical difference as well. Good computer science and engineering knowledge are important, but we need to realize that proper software assembly and design are crucial. This is the thing that I forget the easiest. I see a lot of my colleagues forget it as well, and I have to think that’s because it’s not built into our reward structures (if it’s built into yours let me know).

### Test, test, test - is this thing on?

In 1999 I was working on a rule-based embedded AI system that did some very interesting stuff. Needless to say, the interactions between the various pieces was the actual algorithm, not any of the routines you could point at. I found bugs and unintended interactions left and right, and I started keeping a set of inputs that would allow me to be sure that issues I fixed did not come back. I had started a regression suite. Later I started to add unit tests and library level tests, and have gradually joined the vast majority of code monkeys on the planet in testing my code thoroughly. Or somewhat at least - we all know that most software is lucky to hit 75 or 80% of line coverage and a lot less of the use cases or scenarios are actually covered. Yet if that is so, how do we know it works. The answers range from bad *“the daily use is the best test”* to the dangerous *“it did what I wanted when I wrote it”* to the oblivious.

The stint watching Bob Martins videos lately has my team trending toward TDD (Test Driven Development). While I personally have for years tended more towards Development Driven Testing (no it’s not a thing, just what I have actually done,) the fact is it did not change the team policy of “new code is 100% covered and modifications to old code are new code.” It has helped us live up to that policy and that I cannot fault.

So, why do we test? What do we test? The answers to these are basically that we test to make sure the code does what we think it does and we should test everything if we can. That still leaves a lot of room for design and thought however. How do we know the code won’t be asked to do more than we expect? (it will.) What is everything? In python even covering main is difficult let alone the library declaration code. The answer is that every modification to the code should add modifications to the tests. And don’t let Joe down the hall use your code for something odd if he’s not going to add the tests. A number of people have compared TDD to double entry bookkeeping - tests and code must match or an error shows up. I was unable to find the first reference, but I see them back to the early 2000’s. It does give a very nice idea of what the goal is, but it’s insufficient.

### How to tie it all together

Each of us will have their own methods for keeping these principals working. Some will insist on the most modern ide, some that hand coding the make system is the best defense, others that generated documentation will reveal all. In the end it is attention to the work that really matters and each of us finds a way to that on our own.

This article was originally published as follows: https://www.linkedin.com/pulse/software-craft-paul-wolfenbarger

#### Author bio
<!---
- Length: 50-100 words.
- Can include hyperlinks.
- Mention your current position, employer, a bit about your background.
- Include info about your interests related to software productivity and sustainability.
- Anything else you want to mention.
---!>
 

<!---
Publish: preview
RSS update: 2019-02-25
Categories: development, reliability
Topics: design, testing
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
