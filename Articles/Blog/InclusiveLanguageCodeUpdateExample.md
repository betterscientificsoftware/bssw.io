# Experiences replacing master/slave terminology in Ale3d and Sierra

Outline (notes to self)
1. where did m/s come from
2. How much effort to change?
3. What effort was involved?
4. What's next
* accuracy of terminology does it convey meaning.


One of the ways software projects can improve their inclusive practices is to begin the work of improving language that represent barriers to inclusion.
An unfortunately [prolific](https://github.com/search?q=master+slave&type=code) and unmistakably [problematic](https://www.wired.com/story/tech-confronts-use-labels-master-slave/) example is the use of *master/slave* terminology.
While there has [recently been](https://www.google.com/search?q=%22master%22+%22slave%22+terminology+in+software&sxsrf=AOaemvIy5OkrC1xJEV_CJrUNIG3Tvmtlrg:1643308409486&source=lnt&tbs=qdr:y&sa=X&ved=2ahUKEwjdlYPwyNL1AhVuD0QIHXqoBOsQpwV6BAgBEBk&biw=1616&bih=948&dpr=1) much discussion of this issue in the media, it is a well known and [long standing](https://www.jstor.org/stable/40061475) issue with the earliest online references going back [almost 20 years](http://www.cnn.com/2003/TECH/ptech/11/26/master.term.reut/index.html) and other public discourse almost certaily much earlier.

### A Brief History Lesson

The terminology may have [taken root](https://www.cise.ufl.edu/~sahni/papers/masterslave2.pdf) in technology in the 1940s.
Examination of [Google's NGram viewer](https://books.google.com/ngrams/graph?content=master-slave&year_start=1800&year_end=2019&case_insensitive=on&corpus=26&smoothing=3&direct_url=t4%3B%2Cmaster%20-%20slave%3B%2Cc0%3B%2Cs0%3B%3Bmaster%20-%20slave%3B%2Cc0%3B%3BMaster%20-%20Slave%3B%2Cc0%3B%3BMaster%20-%20slave%3B%2Cc0%3B%3BMASTER%20-%20SLAVE%3B%2Cc0) shows a sharp rise in the use of *master/slave* terminology beginning about that time where it was used by [Raymond Geortz](https://en.wikipedia.org/wiki/Raymond_Goertz) to describe a [remote manipulator](https://en.wikipedia.org/wiki/Remote_manipulator) which is a sort of robotic version of a [glove box](https://en.wikipedia.org/wiki/Glovebox).

Regardless of origin, master-slave terminology has become *pervasive* throughout scientific computing.
It appears in many HPC/CSE contexts such as [slide surfaces](https://abaqus-docs.mit.edu/2017/English/SIMACAEITNRefMap/simaitn-c-contactpairform.htm), [shell-solid element interfacing](https://www.dynasupport.com/tutorial/contact-modeling-in-ls-dyna/contact-types), [parallel runtime execution models](http://charm.cs.uiuc.edu/research/masterSlave), [periodic boundary conditions](https://www.researchgate.net/figure/Master-slave-set-up-for-periodic-boundary-conditions-on-VE-with-a-non-periodic-mesh-see_fig3_320079614), [file systems](https://activemq.apache.org/shared-file-system-master-slave) and [hard drive technology](https://computer.howstuffworks.com/ide.htm), [grid computing](https://sites.cs.ucsb.edu/~rich/publications/shao-hcw.pdf), and [graph traversal](https://dl.acm.org/doi/abs/10.1145/3350546.3352536) to name just a few.

On the one hand, the terminology is seen as a quick, shorthand or metaphor used for conveying rudimentary behavior and/or relationships among the abstract parts or objects of an algorithm or mechanism.
On the other hand, the metaphor often fails miserably in *accurately* communicating any of these aspects.
For example, in modern slide surface algorithms (where one object comes into *contact* with another and the two objects slide along their shared contact boundary), the side designated as a `master` does not actually have the effect of dictating the behavior of any other surface designated as a `slave`.
Instead, numerical algorithms often take into account both surfaces as peers to each other and compute a next timestep where both surfaces contributions are treated equally and with reciprocity.

In HPC/CSE software use of the terminlogy can manifest in the names of data types, variables, functions, files, images, GUI widgets, databases, command-line arguments, URLs, server names, documentation, and publications as well as people's mental models and abstractions for talking about objects, algorithms and associated software or hardware architecture.

Towards the end of the 2020 calender year, two flagship DOE simulation projects, Ale3d at LLNL and Sierra at SNL, completed updates to replace the use of master/slave terminology throughout their projects.

If the work involved only a global, textual replacement of the words "master" and "slave", there wouldn't be much reason for writing about their experiences here.
The work involved changes to source code, dependency interfaces, documentation, test input parameter files and test data files as well as how developers and users alike talk about features of the code where this terminology was used.
Because it involved interfaces to dependent packages and collaborations, it also involved discussions with relevant stakeholders.

Managers of both projects had a long-standing interest in replacing master/slave terminology in their respective projects.
However, mustering the motivation, resources and the critical mass to make it happen remained elusive.
Then, the summer of 2020 happened...
The whole country once again turned its attention to talking about racially-oriented inequities of our society.
This included the world of technology and software.
Gabriel read an article about master/slave terminology in technology and approached project leadership for Sierra about addressing it.

For Ben on the Ale3d project, the catalyzing event was a dependency announcing its plans to replace "master/slave" with "primary/secondary".
For NNSA labs, the terms "primary" and "secondary" typically refer to the major components of a thermonuclear weapon.
Their presence is often accompanied by requirements for handling classified information.
Although the terms "primary" and "secondary" are not themselves classified, using them as prolificly as "master/slave" have been used would present significant challenges in ensuring clean and clear separation between classified and UNclassified information.

Ben felt it was important to get out ahead of these plans and facilitate broader dialog on more workable alternative terms.
In the Ale3d project, "master/slave" terminology was restricted almost entirely to their implementation of slide surfaces where two different parts in a real-world object maintain surface-contact but move relative to each other.
After negotiations with numerous stakeholders, everyone agreed a suitable replacement was simply "Side A" and "Side B".
However, to be thorough Ben felt it was important to replace not only these specific terms but also any terms that *derived* from them.
For example, in the source code `nslvs` might be used as a variable representing the number of slave surfaces or in a data file `M_tire` and `S_Road` might be used to indicate the tire object played the role of a master slide surface and the road object the role of a slave slide surface.
Although automated tooling handled the *common* cases, to reliably replace *derivative* terminology required careful study and manual entry of replacements.


For Sierra, "master/slave" terminlogy was used for multiple different topical areas including contact surfaces, 

Apart from the practical aspects of changing code, documentation, test data, there was also effort required in getting all stakeholders to agree to the changes and support the work involved in completing it. 

When the teams began this work, the total effort and resources required to complete were not well known.
The total effort only revealed itself as dominos began to fall.
In addition, no new resources were allocated to complete the work.
The teams had to forego other activities in order to prioritize and complete this work.

> I think that the “racial reckoning” brought more awareness (to a broader segment of the population) to how systems and language can reinforce and propagate injustice and oppression.  In particular, both how seemingly little things can add up (microaggressions, etc).  For myself, this really made me more aware of the need to change this; I think this was also true for other developers and users.  I’m not sure that this change has “moved the needle” necessarily, but I hope that it can lead to more substantive change (not code changes, but things like hiring, pipeline and things like that).

> The protests made me think more about what I’m doing in my day-to-day to become a better member of society. Am I educating myself enough about these issues? Am I putting myself in other people’s shoes? Am I considering my own biases in my opinions and thoughts? I came across the Washington post opinion piece trying to answer some of these questions. Trying to get a different perspective from my own, and those around me.
> I would like to think these efforts allow other people to ask similar questions. That they motivate thoughtful discussions about topics that are considered taboo to discuss with your co-workers, or even your friends and family.

It is worth nothing that in the latter half of 2021, many authors and critics report seeing what can only be called a *backlash* against such activities.

It likely does not escape the reader's attention that in these examples anyways, the people spearheading the work are people of color.
It also wont escape the reader's attention
